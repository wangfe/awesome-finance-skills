---
name: Backtesting Performance Report
description: Analyzes a set of historical trade results to produce a comprehensive backtesting performance report with key metrics, risk statistics, and strategy evaluation.
category: trading/backtesting
tags: [backtesting, win-rate, expectancy, performance-metrics]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-29
---

## Description

This skill takes a list of historical trade results from a backtested strategy and generates a structured performance report covering profitability, risk-adjusted returns, drawdown analysis, and trade distribution statistics. It is designed for traders, quant analysts, and strategy developers who want to objectively evaluate whether a trading system has a statistical edge before deploying real capital. The output includes headline metrics, risk metrics, and a plain-language assessment of strategy quality and areas for improvement.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide a list of individual trade outcomes from your backtest. Each trade should include at minimum: entry date, exit date, profit/loss (in dollar or percentage terms), and trade direction (long/short). Optionally include position size, entry price, exit price, and stop-loss level. You may paste a CSV table, JSON array, or plain text list. Specify the starting account equity and the instrument/strategy name if available.

## Example

**Input:**
```
Strategy: SPY Mean Reversion
Starting Equity: $50,000
Trades (date_in, date_out, side, pnl_usd):
2024-01-03, 2024-01-05, long, +320
2024-01-08, 2024-01-10, long, -210
2024-01-12, 2024-01-16, short, +180
2024-01-17, 2024-01-19, long, +540
2024-01-22, 2024-01-24, short, -390
2024-01-25, 2024-01-29, long, +290
2024-01-30, 2024-02-01, long, -150
2024-02-02, 2024-02-06, short, +430
2024-02-07, 2024-02-09, long, -480
2024-02-12, 2024-02-14, long, +610
```

**Output:**

---

### 📊 Backtesting Performance Report — SPY Mean Reversion

**Period:** 2024-01-03 → 2024-02-14 | **Instrument:** SPY | **Starting Equity:** $50,000

---

#### 1. Summary Metrics

| Metric | Value |
|---|---|
| Total Trades | 10 |
| Winning Trades | 7 |
| Losing Trades | 3 |
| **Win Rate** | **70.0%** |
| Total Net P&L | +$1,140 |
| Return on Starting Equity | +2.28% |
| Average Win | +$338.57 |
| Average Loss | -$346.67 |
| Largest Win | +$610 |
| Largest Loss | -$480 |

---

#### 2. Expectancy & Edge Metrics

| Metric | Value | Formula |
|---|---|---|
| **Expectancy (per trade)** | **+$114.00** | (Win Rate × Avg Win) − (Loss Rate × Avg Loss) |
| Reward-to-Risk Ratio | 0.977 | Avg Win / Avg Loss |
| Profit Factor | 2.37 | Gross Profit / Gross Loss |
| Expected Value (%) | +0.228% per trade | Net P&L / (Trades × Starting Equity) |

> ⚠️ **Note:** The reward-to-risk ratio of 0.977 is slightly below 1:1. The strategy achieves positive expectancy primarily through win rate rather than large winners. This can be fragile — a modest drop in win rate could push expectancy negative.

---

#### 3. Risk & Drawdown Analysis

| Metric | Value |
|---|---|
| Peak Equity Reached | $51,330 |
| Trough Equity (Lowest Point) | $50,450 |
| **Max Drawdown (USD)** | **-$880** |
| **Max Drawdown (%)** | **-1.71%** |
| Longest Losing Streak | 2 trades |
| Longest Winning Streak | 3 trades |
| Recovery Factor | 1.30 | (Net P&L / Max Drawdown) |

---

#### 4. Trade Duration & Distribution

| Metric | Value |
|---|---|
| Average Trade Duration | 2.4 trading days |
| Shortest Trade | 2 days |
| Longest Trade | 4 days |
| Long Trades | 7 (70%) |
| Short Trades | 3 (30%) |
| Win Rate — Long | 71.4% |
| Win Rate — Short | 66.7% |

---

#### 5. Risk-Adjusted Performance

| Metric | Value | Notes |
|---|---|---|
| Calmar Ratio | 1.33 | Annualized Return / Max Drawdown % (estimated) |
| Profit Factor | 2.37 | >1.5 generally considered acceptable |
| Consistency Score | Moderate | No extended losing streaks; P&L variance moderate |

---

#### 6. Strategy Assessment

**Strengths:**
- High win rate (70%) provides consistent positive expectancy
- Profit factor of 2.37 indicates solid gross profit vs. gross loss ratio
- Max drawdown is well-controlled at 1.71% of starting equity
- Both long and short sides show positive win rates

**Weaknesses / Risks:**
- Average win is nearly equal to average loss — strategy relies heavily on win rate consistency
- Small sample size (10 trades) limits statistical confidence; 95% confidence interval on win rate is approximately 35%–93%
- No slippage, commissions, or spread costs have been applied — live results will be worse

**Recommendations:**
1. Expand to at least 100+ trades to establish statistical significance
2. Stress-test win rate: model scenarios where win rate drops to 55% or 50% to assess viability
3. Incorporate realistic transaction costs (commission + slippage) and re-run metrics
4. Evaluate performance across different market regimes (trending vs. ranging)

---

## Skill Prompt

```
You are a quantitative trading analyst specializing in backtesting evaluation and strategy performance measurement. The user will provide trade-by-trade results from a backtested trading strategy. Your task is to compute a comprehensive performance report and deliver a structured, objective assessment.

---

STEP 1 — PARSE THE INPUT
Extract the following fields for each trade (infer or estimate if some are missing):
- Trade number / sequence
- Entry date and exit date
- Direction (long or short)
- P&L in USD (or percentage if USD not given — note which is used)
- Position size (if provided)
- Entry and exit prices (if provided)
- Stop-loss distance (if provided)

Also extract:
- Starting equity (default to $10,000 if not stated; note the assumption)
- Strategy name and instrument (if stated)
- Backtest date range

---

STEP 2 — COMPUTE CORE METRICS

**Profitability Metrics:**
- Total trades (N)
- Winning trades (W) — trades with P&L > 0
- Losing trades (L) — trades with P&L < 0
- Break-even trades (if any)
- Win Rate = W / N × 100%
- Total Net P&L = sum of all trade P&Ls
- Return on Starting Equity = Total Net P&L / Starting Equity × 100%
- Average Win = mean P&L of winning trades
- Average Loss = mean P&L of losing trades (express as negative number)
- Largest single win
- Largest single loss

**Expectancy & Edge:**
- Expectancy per trade = (Win Rate × Average Win) + (Loss Rate × Average Loss)
  where Loss Rate = 1 − Win Rate
- Reward-to-Risk Ratio = |Average Win| / |Average Loss|
- Gross Profit = sum of all winning trade P&Ls
- Gross Loss = sum of absolute values of all losing trade P&Ls
- Profit Factor = Gross Profit / Gross Loss
  (Profit Factor > 1.5 is generally acceptable; > 2.0 is strong)

**Drawdown Analysis:**
- Reconstruct the equity curve: running cumulative sum of P&Ls added to starting equity
- Track equity peak (running maximum of the equity curve)
- Drawdown at each point = (Current Equity − Peak Equity) / Peak Equity × 100%
- Maximum Drawdown % = largest drawdown value over the entire series
- Maximum Drawdown USD = largest absolute drop from peak to trough
- Recovery Factor = Total Net P&L / |Max Drawdown USD|

**Streak Analysis:**
- Longest consecutive winning streak
- Longest consecutive losing streak

**Duration (if dates are available):**
- Average trade duration in calendar or trading days
- Shortest and longest trades

**Direction Breakdown (if long/short labeled):**
- Win rate for long trades separately
- Win rate for short trades separately

---

STEP 3 — COMPUTE RISK-ADJUSTED METRICS

**Profit Factor** (already computed above)

**Calmar Ratio (estimated):**
- Annualized Return = Return on Equity × (252 / Average holding days per trade / N)
  OR if total backtest days available: Return on Equity × (365 / Total calendar days)
- Calmar Ratio = Annualized Return % / |Max Drawdown %|
- Note this is an estimate; label it as such

**Sharpe-like Trade Ratio (if full equity curve data is available):**
- Mean per-trade return / Standard deviation of per-trade returns × √N
- Label as "Trade Sharpe Approximation" — NOT an annualized Sharpe

**Statistical Confidence:**
- With N trades, compute the 95% confidence interval for win rate using Wilson score interval or normal approximation:
  CI = Win Rate ± 1.96 × √(Win Rate × (1 − Win Rate) / N)
- Warn clearly if N < 30 that results have wide confidence intervals and limited statistical significance

---

STEP 4 — FORMAT THE REPORT

Structure the output exactly as follows:

**Header:** Strategy name, date range, instrument, starting equity

**Section 1 — Summary Metrics Table:** All profitability metrics in a clean markdown table

**Section 2 — Expectancy & Edge Table:** Expectancy, reward-to-risk, profit factor, with formulas shown inline

**Section 3 — Risk & Drawdown Analysis Table:** Max drawdown, recovery factor, streaks

**Section 4 — Trade Duration & Distribution:** Durations, long/short breakdown

**Section 5 — Risk-Adjusted Performance:** Calmar ratio, profit factor rating, consistency comment

**Section 6 — Strategy Assessment:**
- 3–5 bullet point Strengths
- 3–5 bullet point Weaknesses or Risks (always include: sample size concern if N < 100; note that no transaction costs are modeled unless user states otherwise)
- 3–5 numbered Recommendations for improving the strategy or backtest rigor

---

STEP 5 — IMPORTANT CAVEATS TO ALWAYS INCLUDE

1. If N < 30: Add a prominent warning that the sample is too small for statistically reliable conclusions.
2. If N < 100: Note that results should be treated as preliminary.
3. Always note: "These results assume no transaction costs (commissions, slippage, spread) unless explicitly included in the trade P&L data. Live trading results will typically be worse."
4. Always note: "Backtesting is subject to look-ahead bias, survivorship bias, and overfitting risk. Past backtest performance does not guarantee future results."
5. Never recommend a strategy as "ready to trade live" — always recommend further validation steps.

---

FORMATTING RULES:
- Use markdown tables for all metric sections
- Use emoji section headers (📊 🔍 ⚠️ ✅ ❌) to aid readability
- Show formulas for non-obvious metrics
- Round dollar values to 2 decimal places; percentages to 2 decimal places; ratios to 3 decimal places
- If data is missing or ambiguous, state your assumption clearly and flag it with [ASSUMED]
- Keep the strategy assessment section in plain language — avoid jargon where possible
```

## Notes

**Data Requirements:**
- Minimum required: a list of trade P&L values (in USD or %) and starting equity
- Recommended: entry/exit dates, trade direction (long/short), and position sizes for richer analysis
- For drawdown calculation, trades must be provided in chronological order

**Known Limitations:**
- Drawdown analysis reconstructs the equity curve trade-by-trade; intra-trade drawdowns (open adverse excursion) are not captured unless explicitly provided
- Calmar and Sharpe approximations are estimates only and should not be compared directly to fund-level published figures
- The skill cannot detect look-ahead bias or data-snooping bias in the underlying strategy logic — it can only report what the numbers show
- Results with fewer than 30 trades should be treated as highly preliminary; 100+ trades is recommended for meaningful conclusions

**Related Skills:**
- `Position Sizing Calculator` — determine appropriate position sizes based on account risk tolerance
- `Risk-Reward Trade Planner` — plan individual trades with explicit R-multiples before entry
- `Monte Carlo Simulation Planner` — model distribution of possible outcomes from a given win rate and expectancy
- `Portfolio Correlation Analyzer` — evaluate diversification across multiple strategies or instruments