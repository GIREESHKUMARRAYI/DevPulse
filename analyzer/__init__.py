# analyzer/__init__.py

from .github_auto_analyzer import analyze_github_repo
from .pr_analyzer import analyze_pull_requests

__all__ = ["analyze_github_repo", "analyze_pull_requests"]
