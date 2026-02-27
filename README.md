# Awesome Finance Skills

> A curated, open collection of Claude Code skills for finance — personal finance, investing, financial modeling, accounting, trading, and more.

[![Skills](https://img.shields.io/badge/skills-29-blue)](#skill-index)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## What Is This?

This repo is an **awesome list for Claude Code finance skills** — a single place to discover, copy, and use high-quality prompt skills that help with:

- Building budgets and savings plans
- Analyzing stocks and investment opportunities
- Running financial models (DCF, LBO, comps)
- Interpreting financial statements
- Managing trading risk
- Researching earnings and market data

All skills are free, open source, and ready to drop into Claude Code.

> **Auto-updated daily** — a GitHub Actions workflow generates one new skill every day from a curated topic queue using the Claude API.

---

## Quick Start

**1. Browse** the category index below to find a skill.

**2. Open** the skill's `.md` file and copy the prompt from the `## Skill Prompt` section.

**3. Use it** — paste it into Claude Code, or install it as a Claude Code skill:

```bash
# Place the .md file in your Claude Code skills directory:
~/.claude/skills/
```

---

## How to Use Skills

There are three ways to use any skill in this collection, depending on how you work with Claude.

---

### Method 1 — Install as a Claude Code Skill (Recommended)

Claude Code can load `.md` files as persistent named skills that you invoke with a `/` command.

**Step 1 — Copy the skill file to your skills directory:**

```bash
# Create the directory if it doesn't exist
mkdir -p ~/.claude/skills

# Download a skill directly from this repo (example)
curl -o ~/.claude/skills/daily-news-report.md \
  https://raw.githubusercontent.com/wangfe/awesome-finance-skills/main/skills/news-and-reporting/daily-digest/daily-financial-news-report.md
```

Or clone the whole repo and symlink the skills you want:

```bash
git clone https://github.com/wangfe/awesome-finance-skills.git ~/awesome-finance-skills

# Symlink individual skills into your Claude skills directory
ln -s ~/awesome-finance-skills/skills/investing/portfolio-analysis/stock-portfolio-analyzer.md \
      ~/.claude/skills/stock-portfolio-analyzer.md
```

**Step 2 — Use the skill inside Claude Code:**

```
/stock-portfolio-analyzer

Holdings:
AAPL  50 shares  cost $155  current $189
MSFT  30 shares  cost $290  current $415
...
```

Claude will automatically apply the skill's prompt and produce the full analysis.

---

### Method 2 — Copy & Paste into Any Claude Interface

No installation needed. Works in Claude.ai, Claude Code, or the API.

1. Open the skill's `.md` file in this repo.
2. Scroll to the `## Skill Prompt` section.
3. Copy the prompt text inside the code block.
4. Paste it at the start of your Claude conversation, followed by your data.

**Example:**

```
[paste the full skill prompt here]

---

My data:
Monthly income: $6,500
Expenses:
- Rent: $1,800
- Groceries: $450
...
```

---

### Method 3 — Use via the Claude API

Integrate skills into your own apps or scripts by passing the skill prompt as a system prompt.

```python
import anthropic
from pathlib import Path

# Load the skill prompt
skill_file = Path("skills/personal-finance/budgeting/50-30-20-budget-builder.md")
content = skill_file.read_text()

# Extract the prompt block between the ``` fences in ## Skill Prompt
import re
match = re.search(r"## Skill Prompt\s+```[^\n]*\n(.*?)```", content, re.DOTALL)
skill_prompt = match.group(1).strip()

# Call the API
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2048,
    system=skill_prompt,
    messages=[{
        "role": "user",
        "content": "Monthly income: $5,000\nRent: $1,500\nGroceries: $400\nCar: $300"
    }]
)
print(response.content[0].text)
```

---

### Chaining Skills Together

Many workflows benefit from running multiple skills in sequence. For example:

```
Morning routine:
1. /daily-financial-news-report   → paste today's headlines → get market briefing
2. /stock-portfolio-analyzer      → paste your holdings    → see how news affects your positions
3. /earnings-call-analyzer        → paste an earnings transcript → dig into a specific name
```

Each skill is self-contained — output from one can be pasted as input to the next.

---

### Tips

- **Supply your own data.** Skills don't fetch live prices or news — you paste the data, Claude does the analysis. This keeps your data private and the output accurate.
- **Adjust the prompts.** Every skill prompt is plain text. Edit the `## Skill Prompt` section to tailor the output format, add custom benchmarks, or change the tone.
- **Check the `## Notes` section** of each skill for data requirements, known limitations, and links to complementary skills.

---

## Skill Index

### Personal Finance

<!-- SKILLS:personal-finance:START -->
| Skill | Description | Tags |
|---|---|---|
| [50/30/20 Budget Builder](skills/personal-finance/budgeting/50-30-20-budget-builder.md) | Build a personalized monthly budget using the 50/30/20 rule given the user's income and expenses | `budgeting` `50-30-20` `monthly-budget` |
| [Debt Avalanche vs Snowball Payoff Planner](skills/personal-finance/debt-management/debt-avalanche-vs-snowball-payoff-planner.md) | Compares the avalanche and snowball debt payoff strategies side-by-side, calculating total interest, payoff timelines, and monthly payment schedules for each method. | `debt` `avalanche` `snowball` |
| [FIRE Number Calculator](skills/personal-finance/fire-planning/fire-number-calculator.md) | Calculate your Financial Independence / Retire Early (FIRE) number and years to FI based on savings rate, expenses, and expected returns | `fire` `financial-independence` `retire-early` |
| [Emergency Fund Calculator](skills/personal-finance/savings-goals/emergency-fund-calculator.md) | Calculates the recommended emergency fund size based on personal financial circumstances and provides a savings roadmap to reach that goal. | `emergency-fund` `savings` `liquidity` |
| [Net Worth Tracker](skills/personal-finance/savings-goals/net-worth-tracker.md) | Calculates and analyzes a user's current net worth by organizing assets and liabilities into a structured snapshot with trend insights and actionable recommendations. | `net-worth` `assets` `liabilities` |
<!-- SKILLS:personal-finance:END -->

<details>
<summary>Subcategories</summary>

- `budgeting/` — Monthly and zero-based budget builders
- `debt-management/` — Debt avalanche/snowball calculators, payoff planners
- `savings-goals/` — Goal-based savings trackers, emergency fund planners
- `fire-planning/` — FIRE calculators, withdrawal strategy tools
- `tax-personal/` — Tax bracket estimators, deduction finders

</details>

---

### News & Reporting

<!-- SKILLS:news-and-reporting:START -->
| Skill | Description | Tags |
|---|---|---|
| [AlphaEar News](skills/news-and-reporting/daily-digest/alphaear-news/SKILL.md) | Fetch real-time hot finance news and unified trend reports from multiple sources (财联社, WallStreetCN, Weibo, Zhihu, etc.) and Polymarket prediction data | `real-time-news` `chinese-markets` `polymarket` |
| [Daily Financial News Report](skills/news-and-reporting/daily-digest/daily-financial-news-report.md) | Analyze a batch of financial news headlines and articles to produce a structured daily market briefing with key themes, market-moving events, and investment implications | `daily-briefing` `financial-news` `market-summary` |
| [Fed Statement & FOMC Analyzer](skills/news-and-reporting/market-analysis/fed-statement-analyzer.md) | Analyze Federal Reserve statements, FOMC minutes, or Fed chair speeches to extract policy signals, rate path implications, and market impact | `fed` `fomc` `monetary-policy` |
<!-- SKILLS:news-and-reporting:END -->

<details>
<summary>Subcategories</summary>

- `daily-digest/` — Morning briefs, end-of-day recaps, earnings season summaries
- `market-analysis/` — Fed/central bank analysis, analyst upgrade/downgrade trackers
- `macro-events/` — Economic calendar analysis, geopolitical risk impact
- `sector-news/` — Sector rotation detectors, industry news synthesizers

</details>

---

### Investing

<!-- SKILLS:investing:START -->
| Skill | Description | Tags |
|---|---|---|
| [Portfolio Performance Report Generator](skills/investing/portfolio-analysis/portfolio-performance-report.md) | Generate a detailed periodic portfolio performance report with returns, benchmark comparison, attribution, risk metrics, and commentary | `portfolio-report` `performance` `benchmark` |
| [Stock Portfolio Analyzer](skills/investing/portfolio-analysis/stock-portfolio-analyzer.md) | Analyze a stock portfolio's performance, allocation, risk concentration, sector exposure, and key metrics — and generate a comprehensive portfolio health report | `portfolio-analysis` `stock-portfolio` `performance` |
| [Buffett-Style Stock Checklist](skills/investing/stock-analysis/buffett-checklist.md) | Evaluate a stock using Warren Buffett's fundamental investing criteria and produce a pass/fail scorecard | `fundamental-analysis` `value-investing` `buffett` |
<!-- SKILLS:investing:END -->

<details>
<summary>Subcategories</summary>

- `portfolio-analysis/` — Performance reports, allocation analysis, stress tests
- `stock-analysis/` — Fundamental screens, checklist evaluators
- `etf-funds/` — ETF comparison, expense ratio analyzers
- `options-derivatives/` — Options pricing, Greeks explainers, strategy builders
- `crypto/` — Token analysis, on-chain metrics
- `real-estate/` — Rental yield calculators, cap rate analyzers
- `portfolio-management/` — Allocation advisors, rebalancing tools

</details>

---

### Real Estate Investment

<!-- SKILLS:real-estate-investment:START -->
| Skill | Description | Tags |
|---|---|---|
| [Mortgage Payment Calculator](skills/real-estate-investment/financing/mortgage-payment-calculator.md) | Calculate monthly mortgage payments, total interest paid, and a full amortization schedule for any residential or investment property loan. | `mortgage` `amortization` `payment-calculator` |
| [Real Estate Market News Digest](skills/real-estate-investment/market-analysis/real-estate-market-news-digest.md) | Analyze a batch of real estate news headlines to produce a structured digest with price trends, demand signals, and investment implications. | `real-estate` `market-news` `price-trends` |
| [Investment Property Deal Analyzer](skills/real-estate-investment/property-analysis/investment-property-deal-analyzer.md) | Evaluate an investment property opportunity — price, location, condition, comparable sales — and produce a deal quality scorecard with buy/pass recommendation. | `real-estate` `deal-analysis` `property-investment` |
| [Rental Property Cash Flow Analyzer](skills/real-estate-investment/rental-analysis/rental-property-cash-flow-analyzer.md) | Full rental property cash flow analysis — NOI, monthly and annual cash flow, break-even occupancy, and 5-year projection with rent growth assumptions. | `rental-property` `cash-flow` `noi` |
| [Cap Rate & ROI Calculator](skills/real-estate-investment/roi-calculation/cap-rate-and-roi-calculator.md) | Calculate cap rate, cash-on-cash return, gross rent multiplier, and total ROI from property financials, with interpretation benchmarks. | `cap-rate` `cash-on-cash` `roi` |
<!-- SKILLS:real-estate-investment:END -->

<details>
<summary>Subcategories</summary>

- `market-analysis/` — Real estate news digests, price trend analysis, market conditions
- `property-analysis/` — Deal analyzers, investment opportunity screeners, scorecards
- `roi-calculation/` — Cap rate, cash-on-cash return, GRM, total ROI calculators
- `rental-analysis/` — Rental cash flow, NOI, break-even, 5-year projections
- `financing/` — Mortgage calculators, amortization schedules, DSCR analysis

</details>

---

### Financial Modeling

<!-- SKILLS:financial-modeling:START -->
| Skill | Description | Tags |
|---|---|---|
| [DCF Model Builder](skills/financial-modeling/dcf-valuation/dcf-model-builder.md) | Build a discounted cash flow valuation from user-supplied financials and assumptions to estimate intrinsic value per share | `dcf` `valuation` `intrinsic-value` |
| [AlphaEar Predictor](skills/financial-modeling/forecasting/alphaear-predictor/SKILL.md) | Time-series market forecasting using the Kronos model with news-aware sentiment adjustment for OHLC price prediction | `forecasting` `time-series` `kronos` |
<!-- SKILLS:financial-modeling:END -->

<details>
<summary>Subcategories</summary>

- `dcf-valuation/` — Discounted cash flow models
- `lbo-analysis/` — Leveraged buyout modeling
- `comparable-analysis/` — Comps tables, EV/EBITDA multiples
- `scenario-modeling/` — Bull/base/bear scenario builders
- `forecasting/` — Revenue and cost forecasting tools

</details>

---

### Accounting

<!-- SKILLS:accounting:START -->
| Skill | Description | Tags |
|---|---|---|
| [Financial Ratio Analyzer](skills/accounting/ratio-analysis/financial-ratio-analyzer.md) | Calculate and interpret the full suite of financial ratios from a company's income statement, balance sheet, and cash flow statement | `financial-ratios` `fundamental-analysis` `accounting` |
<!-- SKILLS:accounting:END -->

<details>
<summary>Subcategories</summary>

- `bookkeeping/` — Journal entry generators, account reconciliation
- `financial-statements/` — Income statement, balance sheet, cash flow builders
- `ratio-analysis/` — Full ratio suite with interpretation
- `tax-business/` — Business tax estimators, deduction categorizers

</details>

---

### Trading

<!-- SKILLS:trading:START -->
| Skill | Description | Tags |
|---|---|---|
| [AlphaEar Signal Tracker](skills/trading/quantitative/alphaear-signal-tracker/SKILL.md) | Track and update investment signal evolution — assess whether signals are Strengthened, Weakened, or Falsified based on new market data and news | `signal-tracking` `investment-signals` `quantitative` |
| [Position Sizing Calculator](skills/trading/risk-management/position-sizing-calculator.md) | Calculate optimal trade position size using risk-based methods (fixed dollar risk, Kelly Criterion, volatility-adjusted) | `position-sizing` `risk-management` `kelly-criterion` |
<!-- SKILLS:trading:END -->

<details>
<summary>Subcategories</summary>

- `technical-analysis/` — Chart pattern identifiers, indicator explainers
- `quantitative/` — Stat-based strategy builders, factor models
- `risk-management/` — Position sizing, drawdown analysis, VaR calculators
- `backtesting/` — Strategy backtesting templates, performance metrics

</details>

---

### Data & Research

<!-- SKILLS:data-and-research:START -->
| Skill | Description | Tags |
|---|---|---|
| [Earnings Call Analyzer](skills/data-and-research/earnings-analysis/earnings-call-analyzer.md) | Analyze an earnings call transcript to extract key metrics, management tone, guidance changes, and hidden risks | `earnings` `earnings-call` `transcript-analysis` |
| [AlphaEar Sentiment](skills/data-and-research/market-data/alphaear-sentiment/SKILL.md) | Analyze financial text sentiment using FinBERT or LLM, returning a scored label (positive/negative/neutral) from -1.0 to 1.0 | `sentiment-analysis` `finbert` `nlp` |
| [AlphaEar Stock](skills/data-and-research/market-data/alphaear-stock/SKILL.md) | Search A-Share and HK stock tickers by name or code and retrieve OHLCV historical price data | `a-shares` `stock-data` `ohlcv` |
<!-- SKILLS:data-and-research:END -->

<details>
<summary>Subcategories</summary>

- `market-data/` — Data source guides, API usage templates
- `earnings-analysis/` — Transcript analyzers, surprise calculators
- `economic-indicators/` — Macro data interpreters (CPI, GDP, PMI)
- `sec-filings/` — 10-K/10-Q summarizers, risk factor extractors

</details>

---

### Tools & Utilities

<!-- SKILLS:tools-and-utilities:START -->
| Skill | Description | Tags |
|---|---|---|
| [AlphaEar Search](skills/tools-and-utilities/api-integrations/alphaear-search/SKILL.md) | Perform finance web searches across multiple engines (Jina, DuckDuckGo, Baidu) and local RAG document retrieval with smart search caching | `web-search` `rag` `multi-engine` |
| [Compound Interest Calculator](skills/tools-and-utilities/calculators/compound-interest-calculator.md) | Calculate compound interest growth, final balance, and total interest earned for any investment or loan scenario | `compound-interest` `calculator` `savings` |
| [AlphaEar Logic Visualizer](skills/tools-and-utilities/report-generators/alphaear-logic-visualizer/SKILL.md) | Generate Draw.io XML diagrams to visualize finance logic flows, investment theses, and signal transmission chains | `visualization` `drawio` `logic-flow` |
| [AlphaEar Reporter](skills/tools-and-utilities/report-generators/alphaear-reporter/SKILL.md) | Plan, write, and assemble professional financial reports by clustering signals into themes, writing analysis sections, and compiling a final structured report | `report-generation` `financial-reports` `signal-clustering` |
| [Skill Creator](skills/tools-and-utilities/report-generators/alphaear-skill-creator/SKILL.md) | Design and package new Claude Code AgentSkills — covers structure, principles (concise, degrees of freedom), and the SKILL.md + resources anatomy | `skill-authoring` `meta` `agent-skills` |
<!-- SKILLS:tools-and-utilities:END -->

<details>
<summary>Subcategories</summary>

- `calculators/` — Compound interest, loan amortization, break-even
- `converters/` — Currency, unit, rate converters
- `report-generators/` — Monthly summaries, portfolio snapshots
- `api-integrations/` — Templates for connecting to financial data APIs

</details>

---

## Contributing

We welcome new skills from anyone! See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

**Quick contribution steps:**
1. Fork the repo and create a branch: `add/<skill-name>`
2. Add your skill `.md` file in the right `skills/` folder (follow the file format in CONTRIBUTING.md)
3. Submit a PR — the README index is auto-regenerated by the daily workflow

All submissions must pass the [Quality Checklist](QUALITY_CHECKLIST.md).

---

## Acknowledgements

Skills in this collection come from the open-source community. We gratefully credit:

| Contributor | Source | Skills |
|---|---|---|
| [RKiding](https://github.com/RKiding) | [Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | AlphaEar suite: alphaear-logic-visualizer, alphaear-news, alphaear-predictor, alphaear-reporter, alphaear-search, alphaear-sentiment, alphaear-signal-tracker, alphaear-stock, skill-creator |

Want your skills credited here? [Open a PR](CONTRIBUTING.md) and include your source repo in the skill's YAML frontmatter.

---

## Disclaimer

All skills in this collection are for **informational and educational purposes only**. Nothing here constitutes financial, investment, tax, or legal advice. Always consult qualified professionals before making financial decisions.

---

## License

[MIT](LICENSE) — free to use, modify, and distribute with attribution.

---

*Built by the open finance community. Star the repo if it helps you!*
