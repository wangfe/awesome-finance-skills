# Awesome Finance Skills

> A curated, open collection of Claude Code skills for finance — personal finance, investing, financial modeling, accounting, trading, and more.

[![Skills](https://img.shields.io/badge/skills-8-blue)](#skill-index)
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

## Skill Index

### Personal Finance

<!-- SKILLS:personal-finance:START -->
| Skill | Description | Tags |
|---|---|---|
| [50/30/20 Budget Builder](skills/personal-finance/budgeting/50-30-20-budget-builder.md) | Build a personalized monthly budget and get rebalancing suggestions | `budgeting` `50-30-20` `beginner` |
| [FIRE Number Calculator](skills/personal-finance/fire-planning/fire-number-calculator.md) | Calculate your FIRE number, years to FI, and compare FIRE variants | `fire` `financial-independence` `4-percent-rule` |
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

### Investing

<!-- SKILLS:investing:START -->
| Skill | Description | Tags |
|---|---|---|
| [Buffett-Style Stock Checklist](skills/investing/stock-analysis/buffett-checklist.md) | Scorecard for evaluating stocks against Warren Buffett's core criteria | `fundamental-analysis` `value-investing` `checklist` |
<!-- SKILLS:investing:END -->

<details>
<summary>Subcategories</summary>

- `stock-analysis/` — Fundamental screens, checklist evaluators
- `etf-funds/` — ETF comparison, expense ratio analyzers
- `options-derivatives/` — Options pricing, Greeks explainers, strategy builders
- `crypto/` — Token analysis, on-chain metrics
- `real-estate/` — Rental yield calculators, cap rate analyzers
- `portfolio-management/` — Allocation analyzers, rebalancing tools

</details>

---

### Financial Modeling

<!-- SKILLS:financial-modeling:START -->
| Skill | Description | Tags |
|---|---|---|
| [DCF Model Builder](skills/financial-modeling/dcf-valuation/dcf-model-builder.md) | Build a DCF valuation model with sensitivity analysis from user-supplied inputs | `dcf` `valuation` `intrinsic-value` |
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
| [Financial Ratio Analyzer](skills/accounting/ratio-analysis/financial-ratio-analyzer.md) | Calculate and interpret liquidity, profitability, leverage, and efficiency ratios | `financial-ratios` `fundamental-analysis` `profitability` |
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
| [Position Sizing Calculator](skills/trading/risk-management/position-sizing-calculator.md) | Calculate trade size using Fixed Risk, Kelly Criterion, and ATR-based methods | `position-sizing` `risk-management` `kelly-criterion` |
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
| [Earnings Call Analyzer](skills/data-and-research/earnings-analysis/earnings-call-analyzer.md) | Extract key metrics, guidance, sentiment, and risks from an earnings transcript | `earnings` `transcript-analysis` `sentiment` |
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
| [Compound Interest Calculator](skills/tools-and-utilities/calculators/compound-interest-calculator.md) | Calculate growth with compound interest, regular contributions, and milestone projections | `compound-interest` `calculator` `savings` |
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

## Disclaimer

All skills in this collection are for **informational and educational purposes only**. Nothing here constitutes financial, investment, tax, or legal advice. Always consult qualified professionals before making financial decisions.

---

## License

[MIT](LICENSE) — free to use, modify, and distribute with attribution.

---

*Built by the open finance community. Star the repo if it helps you!*
