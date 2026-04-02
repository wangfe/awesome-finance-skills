---
name: Analyst Estimate Tracker and Surprise Calculator
description: Tracks analyst consensus estimates and calculates earnings surprise metrics when actual results are reported.
category: data-and-research/earnings-analysis
tags: [analyst-estimates, earnings-surprise, consensus, eps]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-02
---

## Description

This skill ingests analyst consensus estimate data alongside reported actual earnings figures to compute earnings surprise magnitude, direction, and historical surprise patterns for a given company or set of companies. It is designed for equity research analysts, portfolio managers, and individual investors who want to systematically evaluate how a company's reported results compare to Wall Street expectations. The skill produces a structured surprise summary including percentage beat/miss, normalized surprise score, and a rolling surprise history table, making it easy to identify companies with consistent beat or miss tendencies.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing the following inputs in any readable format (table, bullet list, or plain text):

- **Ticker / Company name**
- **Fiscal period** (e.g., Q1 2025, FY 2024)
- **Consensus EPS estimate** — the mean analyst estimate at the time of reporting
- **Actual reported EPS** — the company's announced figure
- *(Optional)* **Revenue consensus estimate** and **actual reported revenue**
- *(Optional)* **Historical estimate/actual pairs** for prior quarters to compute a surprise trend

You may also provide the number of analysts contributing to the consensus and the standard deviation of estimates if available, to enable a normalized surprise score calculation.

## Example

**Input:**
```
Ticker: ACME Corp (ACM)
Period: Q2 2025
Consensus EPS Estimate: $1.42 (18 analysts, std dev $0.08)
Actual EPS Reported: $1.61
Consensus Revenue Estimate: $4.20B
Actual Revenue Reported: $4.35B

Historical EPS data:
Q1 2025 — Est: $1.31, Act: $1.38
Q4 2024 — Est: $1.55, Act: $1.49
Q3 2024 — Est: $1.28, Act: $1.33
Q2 2024 — Est: $1.19, Act: $1.26
```

**Output:**

### ACME Corp (ACM) — Earnings Surprise Report: Q2 2025

#### Current Quarter Summary

| Metric | Consensus Estimate | Actual Reported | Surprise ($) | Surprise (%) |
|---|---|---|---|---|
| EPS | $1.42 | $1.61 | +$0.19 | **+13.4%** |
| Revenue | $4.20B | $4.35B | +$0.15B | **+3.6%** |

**Normalized EPS Surprise Score:** +2.38σ
*(Surprise of $0.19 divided by consensus std dev of $0.08)*

Interpretation: The reported EPS exceeded consensus by more than 2 standard deviations — a statistically significant beat that falls outside the typical range of analyst forecast error for this stock.

---

#### Historical EPS Surprise Tracker

| Period | Est. EPS | Act. EPS | Surprise ($) | Surprise (%) | Direction |
|---|---|---|---|---|---|
| Q2 2025 | $1.42 | $1.61 | +$0.19 | +13.4% | ✅ Beat |
| Q1 2025 | $1.31 | $1.38 | +$0.07 | +5.3% | ✅ Beat |
| Q4 2024 | $1.55 | $1.49 | −$0.06 | −3.9% | ❌ Miss |
| Q3 2024 | $1.28 | $1.33 | +$0.05 | +3.9% | ✅ Beat |
| Q2 2024 | $1.19 | $1.26 | +$0.07 | +5.9% | ✅ Beat |

**Beat Rate (5 quarters):** 80% (4 of 5 quarters beat consensus)
**Average EPS Surprise:** +4.9%
**Median EPS Surprise:** +5.3%
**Largest Beat:** Q2 2025 (+13.4%) | **Largest Miss:** Q4 2024 (−3.9%)

---

#### Pattern Analysis

- ACME Corp displays a **consistent positive surprise bias**, beating consensus in 4 of the last 5 quarters.
- The average beat of ~5% suggests analysts may be systematically under-estimating this company's earnings power, a common phenomenon known as **analyst anchoring or sandbagging**.
- The single miss in Q4 2024 (−3.9%) was modest and may have been driven by a known one-time charge rather than fundamental weakness.
- The current quarter's +13.4% beat is notably larger than historical norms and warrants scrutiny for non-recurring items or one-time gains before drawing conclusions about sustainable outperformance.

---

#### Whisper Number Context *(if provided)*

If a whisper number (buy-side or street consensus above official consensus) was available, the effective surprise vs. informal expectations would be recalculated here.

---

## Skill Prompt

```
You are an expert financial analyst specializing in earnings analysis and sell-side research interpretation. When this skill is invoked, your task is to calculate, structure, and interpret analyst estimate surprises for one or more companies based on user-provided data.

## STEP 1 — PARSE INPUTS

Extract the following from the user's input:
- Ticker symbol and/or company name
- Fiscal reporting period (quarter or full year)
- Consensus EPS estimate (mean analyst estimate)
- Actual reported EPS
- Number of analysts in consensus (N) — if provided
- Standard deviation of EPS estimates (σ) — if provided
- Consensus revenue estimate — if provided
- Actual reported revenue — if provided
- Historical estimate/actual pairs for prior periods — if provided

If critical inputs (consensus estimate or actual result) are missing, ask the user to supply them before proceeding. Do not fabricate or assume numerical data.

## STEP 2 — CALCULATE CURRENT QUARTER SURPRISE METRICS

For each available metric (EPS, Revenue, and any other provided line items), compute:

1. **Absolute Surprise:**
   Surprise ($) = Actual − Consensus Estimate

2. **Percentage Surprise:**
   Surprise (%) = ((Actual − Consensus Estimate) / |Consensus Estimate|) × 100
   - Use absolute value of the denominator to handle negative EPS estimates correctly.
   - Round to one decimal place.

3. **Normalized Surprise Score (if std dev is available):**
   Z-Score = (Actual − Consensus Estimate) / σ
   - Report to two decimal places.
   - Interpret: |Z| < 1.0 = within normal range; 1.0–2.0 = moderate surprise; > 2.0 = significant statistical outlier.

4. **Direction Label:**
   - Beat: Actual > Consensus Estimate
   - Miss: Actual < Consensus Estimate
   - In-Line: Actual within ±1% of Consensus Estimate (flag as in-line even if technically a beat/miss)

## STEP 3 — BUILD HISTORICAL SURPRISE TABLE (if historical data provided)

For each historical period provided, compute the same Surprise ($), Surprise (%), and Direction metrics. Present as a chronological table, most recent first.

Then compute summary statistics across all available periods:
- Beat Rate (%) = (Number of Beat quarters / Total quarters) × 100
- Average Surprise (%) = arithmetic mean of all Surprise (%) values
- Median Surprise (%)
- Largest Beat quarter and value
- Largest Miss quarter and value
- Streak: note if the company has beaten/missed in N consecutive quarters

## STEP 4 — PATTERN ANALYSIS

Write a concise 3–5 sentence qualitative analysis covering:

a) **Consistency:** Does the company have a track record of beating, meeting, or missing estimates?

b) **Analyst Bias Check:** A consistent positive surprise pattern may indicate systematic analyst under-estimation (anchoring, sandbagging, or conservative guidance culture). A consistent miss pattern may indicate overly optimistic sell-side coverage or operational execution problems.

c) **Current Quarter Context:** Is the current quarter's surprise consistent with historical patterns, or is it an outlier? Flag if the current surprise is more than 2× the historical average surprise magnitude.

d) **Quality Caveat:** Remind the user that EPS surprises can be inflated by non-recurring items, share buybacks reducing share count, or tax rate fluctuations. Revenue surprises are often considered a cleaner signal of fundamental demand.

e) **Whisper Number Note:** If the user provided a whisper number (informal buy-side expectation above the official consensus), recalculate the surprise against the whisper number and note whether the stock is likely to react positively even if it beat the official consensus.

## STEP 5 — OUTPUT FORMAT

Present the results using the following structure:

1. **Current Quarter Summary Table** — metrics, estimates, actuals, surprise $, surprise %
2. **Normalized Surprise Score** — with interpretation (if std dev available)
3. **Historical Surprise Tracker Table** — if historical data provided
4. **Summary Statistics Block** — beat rate, average/median surprise, streaks
5. **Pattern Analysis** — narrative paragraph(s)
6. **Whisper Number Section** — only if whisper data is provided
7. **Data Caveats** — flag any inputs that were estimated, assumed, or seem inconsistent

Use markdown tables for all tabular data. Use ✅ for Beat, ❌ for Miss, and ➖ for In-Line in the Direction column.

## FORMULAS REFERENCE

Percentage Surprise = ((Actual − Estimate) / |Estimate|) × 100
Normalized Z-Score = (Actual − Estimate) / σ
Beat Rate = (Beats / N_periods) × 100
Average Surprise = Σ(Surprise_i) / N_periods

## IMPORTANT CONSTRAINTS

- Never invent, interpolate, or assume numerical data the user has not provided. If data is missing, clearly state what is needed and ask for it.
- Do not provide stock recommendations, price targets, or investment advice.
- Always include the disclaimer that earnings surprises are backward-looking and do not predict future performance.
- If the user provides data that appears internally inconsistent (e.g., actual EPS that differs from the surprise they stated), flag the discrepancy and ask for clarification.
- When EPS is negative, interpret the surprise directionally with care: a "beat" on negative EPS means the loss was smaller than expected (actual is less negative than consensus), which is still generally positive.
```

## Notes

**Data Requirements:**
- At minimum, you need a consensus EPS estimate and an actual reported EPS to run the core calculation.
- Historical data (4–8 prior quarters) is strongly recommended for meaningful pattern analysis.
- Standard deviation of analyst estimates enhances the normalized score but is not required.
- Data can be sourced from Bloomberg, FactSet, Refinitiv, Yahoo Finance (earnings history tab), or earnings call press releases.

**Known Limitations:**
- This skill performs calculations on data you supply — it does not connect to live financial data APIs. All figures must be provided manually.
- Consensus estimates can vary by data provider (mean vs. median, timing of snapshot relative to report date). Be consistent in your data source.
- EPS surprise calculations are sensitive to the denominator when EPS is near zero or negative; interpret with caution in those cases.
- Revenue surprises, while generally cleaner, can be affected by currency translation, deconsolidations, and accounting reclassifications.

**Related Skills in This Repo:**
- `earnings-call-transcript-analyzer` — extracts key themes and guidance from earnings call transcripts
- `guidance-vs-actuals-tracker` — compares management guidance to realized results over time
- `forward-pe-and-estimate-revision-monitor` — tracks how EPS estimate revisions affect valuation multiples
- `seasonal-earnings-pattern-analyzer` — identifies seasonal trends in quarterly results by sector