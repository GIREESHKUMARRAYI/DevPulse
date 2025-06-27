🧱 architecture.md – DevPulse System Architecture

🎯 Goal:

Build an AI-powered tool that analyzes GitHub repos and identifies friction points like churn, tech debt, PR delay, and inefficiency — then explains them using natural language insights.

🧩 Modules:

1. GitHub Data Layer

GitHub API (REST or GraphQL)

Pulls commits, PRs, timestamps, file diffs, labels, review states

Language: Python or Node.js

2. Metrics Engine

Calculates:

Code churn (file frequency)

PR review delays

Inactivity windows

File heatmaps

Normalizes metrics for comparison

3. AI Insight Generator

Uses OpenAI API

Prompts customized to:

Detect burnout indicators

Flag areas for refactor

Score delivery risk

Outputs in natural language + scoring scale

4. Dashboard UI

React + TailwindCSS

Modules:

Churn Heatmap

Review Delay Timeline

AI Recommendations

Repo Summary Card

Optional Export (PDF report)

🔄 Data Flow

Repo URL entered → backend fetches GitHub data

Metrics engine parses & stores data in memory

AI module processes and generates insights

Frontend displays data with charts + summaries

Project is modular. Can be extended later to VS Code plugin, Slack alert bot, or full team dashboard suite.

