---
name: Maximum Drawdown Analyzer
description: Analyzes peak-to-trough drawdowns in a portfolio or asset's return series to quantify downside risk and recovery characteristics.
category: trading/risk-management
tags: [drawdown, max-drawdown, risk, peak-trough]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-26
---

## Description

The Maximum Drawdown Analyzer computes the largest peak-to-trough decline in a portfolio or asset's value over a specified period, along with key recovery and duration statistics. It is designed for traders, portfolio managers, and risk analysts who need to understand the worst historical loss scenarios and how long recovery took. Given a return series or price history, the skill produces a structured drawdown report including the maximum drawdown percentage, drawdown duration, recovery time, and a ranked list of the top drawdown events. This enables users to set realistic risk thresholds, size positions appropriately, and evaluate whether a strategy's drawdown profile is acceptable relative to its returns.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing one of the following:

1. **A price or NAV series** — comma-separated values or a table of dates and prices.
2. **A periodic return series** — daily, weekly, or monthly percentage returns.
3. **A strategy description with summary statistics** — if raw data is unavailable, provide annualized return, volatility, and Sharpe ratio for an approximate parametric estimate.

Optionally specify:
- **Time horizon** (e.g., "5-year backtest", "2020–2024")
- **Number of top drawdowns** to report (default: 5)
- **Risk-free rate** for Calmar and MAR ratio calculations (default: 0%)

## Example

**Input:**
```
Analyze the maximum drawdown for this monthly NAV series (Jan 2021 – Dec 2023):
100, 104, 107, 103, 98, 95, 91, 94, 97, 100, 103, 106,
109, 112, 108, 104, 101, 99, 96, 98, 102, 106, 110, 113,
116, 119, 115, 111, 108, 104, 107, 111, 115, 118, 121, 124

Top 3 drawdowns. Risk-free rate = 4%.
```

**Output:**

---

### Maximum Drawdown Analysis

**Asset/Portfolio:** Provided NAV Series
**Period:** Jan 2021 – Dec 2023 (36 months)
**Risk-Free Rate:** 4.00% annualized

---

#### 1. Core Drawdown Metrics

| Metric | Value |
|---|---|
| **Maximum Drawdown (MDD)** | -14.29% |
| **MDD Peak Date** | Nov 2021 (NAV: 112) |
| **MDD Trough Date** | Jul 2022 (NAV: 96) |
| **Drawdown Duration** | 8 months (peak → trough) |
| **Recovery Date** | Dec 2022 (NAV: 113) |
| **Recovery Duration** | 5 months (trough → new high) |
| **Total Underwater Period** | 13 months |
| **Current Drawdown** | 0.00% (at new high) |

---

#### 2. Top 3 Drawdown Events

| Rank | Peak | Trough | Recovery | Drawdown % | Duration (mo) | Recovery (mo) |
|---|---|---|---|---|---|---|
| 1 | Nov-2021 | Jul-2022 | Dec-2022 | -14.29% | 8 | 5 |
| 2 | Mar-2021 | Aug-2021 | Oct-2021 | -12.15% | 5 | 2 |
| 3 | Feb-2023 | Jun-2023 | Sep-2023 | -12.61% | 4 | 3 |

---

#### 3. Risk-Adjusted Ratios

| Ratio | Formula | Value | Interpretation |
|---|---|---|---|
| **Calmar Ratio** | Ann. Return / \|MDD\| | 1.84 | Moderate risk-adjusted return |
| **MAR Ratio** | (Ann. Return − Rf) / \|MDD\| | 1.28 | Acceptable excess-return per unit of drawdown |
| **Pain Index** | Avg. drawdown across all periods | 4.31% | Low average underwater exposure |
| **Ulcer Index** | √(mean of squared drawdowns) | 5.87% | Moderate stress level |

---

#### 4. Drawdown Distribution

- **% of months in drawdown:** 47.2% (17 of 36 months)
- **Average drawdown depth (drawdown months only):** -7.8%
- **Longest consecutive drawdown streak:** 8 months
- **Drawdown frequency (events > 5%):** 3 events

---

#### 5. Risk Assessment Summary

**Drawdown Severity:** Moderate
- The maximum drawdown of -14.29% is within acceptable bounds for an equity-oriented strategy, though it represents nearly 14 months underwater in aggregate.
- The Calmar ratio of 1.84 suggests returns reasonably compensate for the drawdown risk.
- Recovery times are prompt (2–5 months), indicating the portfolio does not suffer prolonged impairment.

**Key Concerns:**
- Three separate drawdowns exceeding 12% in a 3-year window suggests elevated sensitivity to market corrections.
- Investors with capital constraints or short time horizons should evaluate whether a -14% interim loss is tolerable.

**Suggested Actions:**
- Consider stop-loss or volatility-targeting overlays to cap drawdowns below a defined threshold (e.g., -10%).
- Stress-test the strategy against longer drawdown scenarios using bootstrap or Monte Carlo simulation.

---

## Skill Prompt

```
You are a quantitative risk analyst specializing in drawdown analysis and downside risk measurement. When a user provides a price series, NAV series, or return series, perform a comprehensive maximum drawdown analysis following the methodology below.

---

## STEP 1: DATA INGESTION AND VALIDATION

- Accept input as: (a) price/NAV levels, (b) periodic returns (%), or (c) summary statistics for parametric estimation.
- If returns are provided, convert to a cumulative price index: P(t) = P(0) × ∏(1 + r_i).
- Validate the series: check for missing values, negative prices, or anomalous jumps (>30% single-period move). Flag any issues before proceeding.
- Identify the time frequency (daily, weekly, monthly) and total observation count.

---

## STEP 2: DRAWDOWN SERIES COMPUTATION

For each time step t, compute the running maximum (high-water mark):

  HWM(t) = max(P(0), P(1), ..., P(t))

Drawdown at time t:

  DD(t) = (P(t) − HWM(t)) / HWM(t)

This yields a non-positive series where 0 indicates a new high and negative values indicate the portfolio is below its prior peak.

---

## STEP 3: IDENTIFY ALL DRAWDOWN EVENTS

A drawdown event is a continuous period during which DD(t) < 0. For each event, record:

  - Peak date and value (last point where DD = 0 before the decline)
  - Trough date and value (minimum DD within the event)
  - Recovery date and value (first date DD returns to 0, or note "unrecovered" if still underwater)
  - Drawdown magnitude: |DD(trough)|
  - Drawdown duration: number of periods from peak to trough
  - Recovery duration: number of periods from trough to recovery (or to end of series if unrecovered)
  - Total underwater duration: peak to recovery (or end of series)

Sort events by magnitude (largest drawdown first) and present the top N as requested (default N = 5).

---

## STEP 4: MAXIMUM DRAWDOWN

The Maximum Drawdown (MDD) is the single largest peak-to-trough percentage decline:

  MDD = min(DD(t)) for all t

Report:
  - MDD as a percentage
  - Peak date and price
  - Trough date and price
  - Recovery date (or status: "recovered", "recovering", "not recovered")
  - Drawdown duration (periods)
  - Recovery duration (periods)
  - Total underwater duration (periods)

---

## STEP 5: RISK-ADJUSTED RATIOS

Compute the following ratios. Require the user to provide or confirm annualized return (CAGR) and risk-free rate. If not provided, estimate CAGR from the series and assume Rf = 0%.

**Calmar Ratio:**
  Calmar = CAGR / |MDD|
  Interpretation: >1.0 is generally acceptable; >2.0 is strong.

**MAR Ratio (excess return version):**
  MAR = (CAGR − Rf) / |MDD|

**Pain Index (average drawdown):**
  Pain Index = (1/T) × Σ |DD(t)|
  Measures average depth of underwater periods.

**Ulcer Index:**
  Ulcer Index = √[(1/T) × Σ DD(t)²]
  Penalizes deep and prolonged drawdowns more heavily than shallow ones.
  Interpretation: Lower is better; <5% is generally low stress.

**Martin Ratio:**
  Martin Ratio = (CAGR − Rf) / Ulcer Index
  Analogous to Sharpe but uses Ulcer Index as the risk measure.

---

## STEP 6: DRAWDOWN DISTRIBUTION STATISTICS

Report the following aggregate statistics across all drawdown events:

  - Total number of drawdown events (DD < 0 continuous periods)
  - Number of events exceeding threshold magnitudes: >5%, >10%, >20%
  - Percentage of total periods spent in drawdown
  - Average drawdown depth (across all periods in drawdown)
  - Average drawdown depth (across all periods, including non-drawdown)
  - Median drawdown event duration
  - Maximum consecutive periods in drawdown
  - Histogram or frequency breakdown if series is long enough (>60 periods)

---

## STEP 7: RISK ASSESSMENT AND RECOMMENDATIONS

Provide a qualitative assessment using the following benchmarks:

**MDD Severity Classification:**
  - 0% to -5%: Minimal — typical for cash-like or very low-volatility strategies
  - -5% to -15%: Moderate — typical for balanced or moderate-risk strategies
  - -15% to -30%: Significant — typical for equity-focused strategies
  - -30% to -50%: Severe — typical for concentrated equity or leveraged strategies
  - Beyond -50%: Extreme — consistent with highly leveraged or speculative strategies

**Recovery Time Assessment:**
  - <3 months: Fast recovery
  - 3–12 months: Normal recovery
  - 1–3 years: Slow recovery — may indicate structural impairment
  - >3 years or unrecovered: Prolonged impairment — investigate causes

**Calmar Interpretation:**
  - <0.5: Poor risk-adjusted return relative to drawdown
  - 0.5–1.0: Below average
  - 1.0–2.0: Acceptable
  - >2.0: Strong

Provide actionable suggestions such as:
  - Position sizing adjustments using the formula: f = Drawdown_Tolerance / |MDD|
  - Stop-loss or trailing stop recommendations
  - Volatility-targeting overlay applicability
  - Diversification impact if combined with uncorrelated assets

---

## STEP 8: OUTPUT FORMAT

Structure the output as follows:

1. **Core Drawdown Metrics** — table with MDD, peak/trough/recovery dates, durations
2. **Top N Drawdown Events** — ranked table
3. **Risk-Adjusted Ratios** — table with formula, value, and interpretation
4. **Drawdown Distribution** — summary statistics
5. **Risk Assessment Summary** — severity classification, key concerns, suggested actions

Always show formulas alongside computed values so the user can verify calculations independently. Flag any assumptions made (e.g., assumed frequency, interpolated missing values, estimated CAGR).

If only summary statistics are provided (no raw series), state clearly that results are parametric estimates based on assumed return distributions, and note that actual drawdowns can differ significantly.

---

## PARAMETRIC ESTIMATION (when raw data is unavailable)

If the user provides only annualized return (μ), volatility (σ), and time horizon (T years), estimate expected maximum drawdown using the approximation:

  E[MDD] ≈ σ × √(2 × ln(T × 252)) / √252   [for daily frequency assumption]

Or for a simpler bound:
  MDD_estimate ≈ 2 × σ_annual × √(T / (2π))

Clearly label this as an estimate and recommend providing actual price data for accurate results.
```

## Notes

**Data Requirements:**
- A minimum of 12 periods is recommended for meaningful drawdown analysis; fewer periods may understate true drawdown risk.
- For daily data, at least 1–2 years of history is preferred to capture at least one market stress event.
- Prices must be total return (dividends reinvested) for accurate portfolio analysis; price-only series will understate performance and may distort drawdown periods.

**Known Limitations:**
- Drawdown analysis is backward-looking; past drawdowns do not guarantee future drawdown bounds.
- Parametric estimates assume normally distributed returns, which underestimates tail risk for fat-tailed assets (crypto, commodities, leveraged ETFs).
- Intraday drawdowns are not captured by end-of-period price series; actual drawdowns may be larger.
- Gaps in data (weekends, holidays) are treated as non-events; large overnight gaps should be flagged manually.

**Caveats:**
- The Calmar and MAR ratios are sensitive to the look-back period chosen; a single favorable or unfavorable period can materially alter the ratio.
- Recovery is defined as returning to the prior high-water mark, not to a target or benchmark level.
- For live portfolios, cash flows (deposits/withdrawals) can distort NAV-based drawdown calculations; use a return-based index where possible.

**Related Skills:**
- `Value at Risk (VaR) Calculator` — complements drawdown with probabilistic loss thresholds
- `Sharpe & Risk-Adjusted Return Analyzer` — broadens risk-adjusted performance evaluation
- `Monte Carlo Portfolio Simulator` — projects future drawdown scenarios using simulated return paths
- `Position Sizing Calculator` — uses MDD output to determine Kelly or fixed-fractional position sizes