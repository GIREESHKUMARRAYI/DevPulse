import os
import tempfile
import git
from pydriller import Repository
from github import Github
import json

from models.churn_model import extract_churn_metrics, predict_churn
from models.techdebt_model import predict_techdebt
from models.delay_model import predict_delay

GITHUB_TOKEN = "your_personal_token"  # 🔒 Replace securely in production

def analyze_github_repo(repo_url):
    results = {
        "commits": [],
        "prs": []
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Cloning {repo_url} into {tmpdir}")
        repo = git.Repo.clone_from(repo_url, tmpdir)

        # Analyze commits using pydriller
        for commit in Repository(tmpdir).traverse_commits():
            if not commit.modifications:
                continue
            full_diff = "\n".join([m.diff for m in commit.modifications if m.diff])
            churn_score = predict_churn(full_diff)
            td_flag, td_prob = predict_techdebt(commit.msg)

            results["commits"].append({
                "hash": commit.hash,
                "author": commit.author.name,
                "date": commit.author_date.isoformat(),
                "message": commit.msg,
                "churn_score": churn_score,
                "technical_debt_flag": td_flag,
                "technical_debt_confidence": round(td_prob, 3)
            })

    return results
