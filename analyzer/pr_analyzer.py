from github import Github
from models.delay_model import predict_delay

GITHUB_TOKEN = "your_personal_token"

def analyze_pull_requests(repo_url):
    g = Github(GITHUB_TOKEN)
    repo_path = repo_url.replace("https://github.com/", "")
    repo = g.get_repo(repo_path)

    pr_results = []

    for pr in repo.get_pulls(state="closed"):
        try:
            delay_days = (pr.closed_at - pr.created_at).days
            lines_changed = pr.additions + pr.deletions
            meta = {
                "num_files_changed": pr.changed_files,
                "lines_changed": lines_changed,
                "comments_count": pr.comments
            }
            predicted_delay = predict_delay(meta)

            pr_results.append({
                "pr_number": pr.number,
                "title": pr.title,
                "delay_actual": delay_days,
                "delay_predicted": round(predicted_delay, 2),
                "created_at": pr.created_at.isoformat(),
                "closed_at": pr.closed_at.isoformat()
            })
        except Exception as e:
            continue

    return pr_results
