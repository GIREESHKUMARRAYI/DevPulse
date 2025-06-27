**📘 devlog.md – DevPulse Development Log**

---

# DevPulse – My Journey Building an AI-Powered Developer Productivity Tool

## Day 0 – \[June 26, 2025]

* 🔍 I started by searching for **real AI software problems** that companies care about but most students ignore.
* ❌ I didn’t want to build another social issue project or clone app. I wanted something that would **catch the attention of CTOs and recruiters**.
* 🤖 Searched terms like:

  * "AI problems companies urgently want solved"
  * "internal developer tools problem statements"
  * "how companies measure productivity of devs"
* 💡 Realized that **code churn, review delays, and tech debt** were hidden problems every company faces — but very few students even understand them.
* 🔎 Found forums where engineers complained about delivery issues, and read GitHub blog posts on metrics like DORA, PR latency, etc.
* ✅ Finalized my problem: **AI-powered GitHub activity analyzer to improve developer productivity**.
* 🧠 Named the project: `DevPulse`.

## Day 1 – \[June 27, 2025]

* ✅ Created repo `DevPulse`, added Apache 2.0 license, and started initial commit.
* 🧱 Set up folders: `src/`, `public/`, `proof/`, `docs/`
* 📄 Created `README.md`, `devlog.md`, `prompts.md`, `architecture.md`
* 💭 Started thinking about what core metrics to include.
* 🔐 Decided to keep daily evidence in `proof/` including screen recordings and logs.


**🧱 architecture.md – DevPulse System Architecture**

---

## 🎯 Goal:

Build an AI-powered tool that analyzes GitHub repos and identifies friction points like churn, tech debt, PR delay, and inefficiency — then explains them using natural language insights.

## 🧩 Modules:

### 1. GitHub Data Layer

* GitHub API (REST or GraphQL)
* Pulls commits, PRs, timestamps, file diffs, labels, review states
* Language: Python or Node.js

### 2. Metrics Engine

* Calculates:

  * Code churn (file frequency)
  * PR review delays
  * Inactivity windows
  * File heatmaps
* Normalizes metrics for comparison

### 3. AI Insight Generator

* Uses OpenAI API
* Prompts customized to:

  * Detect burnout indicators
  * Flag areas for refactor
  * Score delivery risk
* Outputs in natural language + scoring scale

### 4. Dashboard UI

* React + TailwindCSS
* Modules:

  * Churn Heatmap
  * Review Delay Timeline
  * AI Recommendations
  * Repo Summary Card
* Optional Export (PDF report)

## 🔄 Data Flow

1. Repo URL entered → backend fetches GitHub data
2. Metrics engine parses & stores data in memory
3. AI module processes and generates insights
4. Frontend displays data with charts + summaries

---

Project is modular. Can be extended later to VS Code plugin, Slack alert bot, or full team dashboard suite.
