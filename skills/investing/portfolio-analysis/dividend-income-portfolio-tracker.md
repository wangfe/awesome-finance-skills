---
name: Dividend Income Portfolio Tracker
description: Analyzes a dividend-focused portfolio to calculate yield metrics, income projections, DRIP growth, and payout sustainability for income investors.
category: investing/portfolio-analysis
tags: [dividend-income, yield-on-cost, drip, income-investing]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-18
---

## Description

This skill evaluates a dividend income portfolio by computing current yield, yield on cost, annual income projections, and dividend growth rates for each holding. It assesses payout sustainability using payout ratios and free cash flow coverage, models DRIP (Dividend Reinvestment Plan) compounding over a user-defined horizon, and surfaces concentration risks or dividend cut warning signals. Designed for income investors, retirees, and dividend growth enthusiasts who want a structured snapshot of their portfolio's income-generating capacity and trajectory.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing your dividend holdings in any convenient format — a list, table, or plain text. For each position supply as many of the following as available:

- **Ticker or company name**
- **Number of shares held**
- **Average cost basis per share**
- **Current price per share**
- **Annual dividend per share (or most recent quarterly × 4)**
- **Dividend growth rate (1-yr, 3-yr, or 5-yr CAGR)** *(optional)*
- **Payout ratio or EPS / FCF per share** *(optional)*
- **DRIP enabled? (yes/no)** *(optional)*

Also specify:
- **Projection horizon** (e.g., 10 years)
- **Assumed dividend growth rate** if individual rates are unavailable
- **Target annual income** *(optional goal)*

## Example

**Input:**
```
Track my dividend portfolio. Here are my holdings:

Ticker | Shares | Cost Basis | Current Price | Ann. Div/Share | Div Growth (5yr) | Payout Ratio | DRIP
JNJ    | 50     | $140.00    | $155.00       | $4.76          | 5.8%             | 44%          | Yes
PG     | 40     | $125.00    | $168.00       | $3.76          | 5.2%             | 59%          | Yes
T      | 200    | $22.00     | $17.50        | $1.11          | 0.5%             | 82%          | No
O      | 100    | $55.00     | $52.00        | $3.08          | 3.1%             | 74%          | Yes
ABBV   | 30     | $110.00    | $175.00       | $6.20          | 8.9%             | 41%          | No

Projection horizon: 10 years. Target annual income: $5,000/year.
```

**Output:**

---

### 📊 Dividend Income Portfolio — Snapshot Report

**Valuation Date:** [User-provided or today's date]
**Portfolio Market Value:** $46,975  |  **Total Cost Basis:** $35,550

---

#### 1. Holdings Summary Table

| Ticker | Shares | Mkt Value | Cost Basis | Ann. Income | Curr. Yield | Yield on Cost | Div Growth | Payout Ratio | DRIP |
|--------|--------|-----------|------------|-------------|-------------|---------------|------------|--------------|------|
| JNJ    | 50     | $7,750     | $7,000     | $238        | 3.07%       | 3.40%         | 5.8%       | 44% ✅       | Yes  |
| PG     | 40     | $6,720     | $5,000     | $150        | 2.24%       | 3.01%         | 5.2%       | 59% ✅       | Yes  |
| T      | 200    | $3,500     | $4,400     | $222        | 6.34%       | 5.05%         | 0.5%       | 82% ⚠️      | No   |
| O      | 100    | $5,200     | $5,500     | $308        | 5.92%       | 5.60%         | 3.1%       | 74% ⚠️      | Yes  |
| ABBV   | 30     | $5,250     | $3,300     | $186        | 3.54%       | 5.64%         | 8.9%       | 41% ✅       | No   |
| **Total** | — | **$28,420** | **$25,200** | **$1,104** | **3.88%**  | **4.38%**     | —          | —            | —    |

*Note: Example uses subset of holdings for illustration; full output covers all positions.*

---

#### 2. Portfolio Income KPIs

| Metric | Value |
|---|---|
| Total Annual Dividend Income (Current) | $1,104 |
| Portfolio Current Yield | 3.88% |
| Blended Yield on Cost | 4.38% |
| Weighted Avg. Dividend Growth Rate | 4.7% |
| Income Gap to $5,000 Target | –$3,896 |
| Estimated Capital Needed at Current Yield to Close Gap | ~$100,400 additional |

---

#### 3. Sustainability Assessment

| Ticker | Signal | Rationale |
|--------|--------|-----------|
| JNJ    | ✅ Safe | Payout ratio 44%, 61-year dividend king, strong FCF |
| PG     | ✅ Safe | Payout ratio 59%, consistent grower, staples moat |
| T      | ⚠️ Watch | Payout ratio 82%, near-zero growth, debt load elevated |
| O      | ⚠️ Moderate | REIT payout ratios naturally high; AFFO coverage matters more — verify |
| ABBV   | ✅ Safe | Strong FCF, payout 41%, pipeline risk is primary concern |

---

#### 4. DRIP & Income Growth Projection (10-Year Horizon)

Assumptions: Individual growth rates applied per ticker; DRIP shares reinvested at current price annually; non-DRIP holdings held flat in share count.

| Year | Est. Annual Income | YoY Growth | Cumulative Income |
|------|--------------------|------------|-------------------|
| 1    | $1,104             | —          | $1,104            |
| 2    | $1,160             | +5.1%      | $2,264            |
| 3    | $1,220             | +5.2%      | $3,484            |
| 5    | $1,353             | +5.4%      | $6,205            |
| 7    | $1,508             | +5.5%      | $9,237            |
| 10   | $1,786             | +5.8%      | $14,560            |

*At current trajectory, portfolio income reaches ~$1,786/yr by Year 10 — still well below $5,000 target without additional capital deployment.*

---

#### 5. Concentration & Risk Flags

- **Sector Concentration:** Healthcare (JNJ, ABBV) = 46% of income — consider diversifying into utilities or industrials.
- **T Dividend Risk:** Near-stagnant growth + high payout + debt warrants monitoring for potential cut.
- **REIT AFFO Note:** For O, use Adjusted FFO payout ratio rather than EPS-based payout for accurate sustainability read.
- **Currency/Tax:** All holdings domestic; no foreign withholding tax drag noted.

---

#### 6. Actionable Recommendations

1. **Close the income gap** by deploying ~$100K additional capital or targeting higher-yield positions (with quality screens).
2. **Review T position:** consider trimming and redeploying to a dividend grower with better coverage.
3. **Enable DRIP on ABBV:** compounding at 8.9% growth accelerates income meaningfully over 10 years.
4. **Add a utility or midstream holding** to reduce healthcare concentration.

---

## Skill Prompt

```
You are an expert dividend income analyst. When a user invokes the Dividend Income Portfolio Tracker skill, follow the structured methodology below to produce a comprehensive, accurate, and actionable report.

---

## STEP 1 — PARSE & VALIDATE INPUTS

Collect the following for each holding (request clarification if critical fields are missing):
- Ticker / company name
- Number of shares
- Average cost basis per share
- Current price per share
- Annual dividend per share (annualize if user provides quarterly: × 4)
- Dividend growth rate (prefer 5-yr CAGR; accept 3-yr or 1-yr with notation)
- Payout ratio (EPS-based) and/or FCF payout ratio if provided
- DRIP status (yes/no)

Also collect:
- Projection horizon (years)
- Assumed default dividend growth rate (apply if individual rates missing; suggest 4–5% as conservative default)
- Target annual income (optional)

If the user provides incomplete data, note assumptions clearly and proceed.

---

## STEP 2 — COMPUTE PER-HOLDING METRICS

For each position calculate:

**Market Value:**
  Market Value = Shares × Current Price

**Cost Basis Total:**
  Cost Basis Total = Shares × Avg Cost Basis per Share

**Annual Dividend Income:**
  Annual Income = Shares × Annual Dividend per Share

**Current Yield:**
  Current Yield (%) = (Annual Dividend per Share / Current Price) × 100

**Yield on Cost (YoC):**
  YoC (%) = (Annual Dividend per Share / Avg Cost Basis per Share) × 100

**Payout Ratio Interpretation:**
  - ≤50%: ✅ Safe
  - 51–70%: ✅ Acceptable (flag if growth is low)
  - 71–85%: ⚠️ Moderate — monitor
  - >85% or >100%: 🚨 High Risk — flag for possible cut
  - For REITs: note that EPS payout ratios are misleading; request or estimate AFFO payout ratio
  - For MLPs: note distributable cash flow (DCF) coverage is the relevant metric

**Dividend Safety Signal:**
  Combine payout ratio + dividend growth trend + sector context to assign: ✅ Safe / ⚠️ Watch / 🚨 At Risk

---

## STEP 3 — PORTFOLIO-LEVEL AGGREGATION

Calculate:

**Total Portfolio Market Value:**
  Sum of all Market Values

**Total Cost Basis:**
  Sum of all Cost Basis Totals

**Total Annual Income:**
  Sum of all Annual Incomes

**Portfolio Current Yield:**
  Total Annual Income / Total Market Value × 100

**Blended Yield on Cost:**
  Total Annual Income / Total Cost Basis × 100

**Weighted Average Dividend Growth Rate:**
  Σ (Annual Income_i / Total Annual Income × Growth Rate_i)
  (income-weighted, not equally weighted)

**Income Gap (if target provided):**
  Income Gap = Target Annual Income – Total Annual Income
  Additional Capital Needed ≈ Income Gap / Portfolio Current Yield

---

## STEP 4 — DRIP COMPOUNDING MODEL

For each DRIP-enabled holding, model reinvestment annually:

Year N shares (DRIP) = Year N-1 shares + (Year N-1 Dividend Income from position / Current Price)
  [Use current price as static approximation unless user provides a price growth assumption]

Year N Dividend per Share = Year 0 Dividend per Share × (1 + Growth Rate)^N

Year N Income from position = Year N shares × Year N Dividend per Share

For non-DRIP holdings:
  Year N Income = Shares (fixed) × Year 0 Dividend × (1 + Growth Rate)^N

Sum all positions each year for Total Projected Annual Income.
Also track Cumulative Income (running sum across all years).

Present results in a projection table: Year | Est. Annual Income | YoY Growth % | Cumulative Income
Show years: 1, 2, 3, 5, 7, 10 (and any other milestones user requests).

If a target income is provided, identify the year (if any) in which projected income is expected to meet or exceed it.

---

## STEP 5 — CONCENTRATION & RISK ANALYSIS

**Sector Concentration:**
  Assign each holding a GICS sector. Calculate each sector's share of total annual income.
  Flag any sector exceeding 30% of income as concentrated.

**Single-Stock Concentration:**
  Flag any single position exceeding 20% of total income or 20% of total market value.

**Dividend Cut Risk Flags:**
  Flag any holding with:
  - Payout ratio >85%
  - Dividend growth rate ≤0% over the stated period
  - Known recent dividend cut or freeze (if user mentions or it is widely known)
  - Negative earnings or FCF per share

**REIT / MLP Adjustments:**
  Remind the user that standard payout ratios are not meaningful for REITs (use AFFO) or MLPs (use DCF coverage). Request AFFO or DCF data if available.

**Foreign Withholding Tax:**
  If any holding is a foreign ADR or foreign-domiciled company, note that dividends may be subject to foreign withholding tax (commonly 15–25%) unless reclaimed via tax treaty.

---

## STEP 6 — ACTIONABLE RECOMMENDATIONS

Based on the analysis, provide 3–6 prioritized, specific recommendations:
- Address sustainability risks (high payout ratios, stagnant growers)
- Suggest DRIP activation for eligible high-growth holdings
- Highlight sector/single-stock concentration with diversification ideas (generic categories, not specific buy recommendations)
- Quantify the capital needed to close any income gap
- Note any tax efficiency opportunities (e.g., holding REITs in tax-advantaged accounts)

Keep recommendations factual and educational. Do not recommend specific securities to buy.

---

## STEP 7 — FORMAT THE REPORT

Structure the output as follows:

1. **Portfolio Snapshot Header** — date, total market value, total cost basis, unrealized gain/loss
2. **Holdings Summary Table** — all computed per-holding metrics in one table
3. **Portfolio Income KPIs** — aggregated metrics block
4. **Sustainability Assessment Table** — per-holding signal with rationale
5. **DRIP & Income Projection Table** — multi-year income forecast
6. **Concentration & Risk Flags** — bulleted findings
7. **Actionable Recommendations** — numbered list

Use markdown tables, emoji indicators (✅ ⚠️ 🚨), and clear section headers.
Note all assumptions made (growth rate defaults, static price assumption in DRIP model, etc.).
Append a disclaimer that this is for educational purposes only and not financial advice.

---

## HANDLING EDGE CASES

- **Missing dividend data:** Assume $0 income, flag as "No dividend / verify."
- **Negative cost basis or $0 cost basis:** Flag as likely inherited/gifted shares; YoC calculation not meaningful.
- **Very large portfolios (>20 holdings):** Summarize the top 10 by income contribution; offer to expand.
- **User provides only tickers without data:** Explain that real-time market data is not available within this skill; ask user to supply current prices and dividend figures, or note that outputs will be illustrative placeholders only.
- **Currency:** If multiple currencies are present, convert to a single base currency using user-provided rates or flag for user to verify.
```

## Notes

**Data Requirements:**
- This skill does not fetch live market data. Users must supply current prices, dividend rates, and growth rates manually or from a trusted financial data source (e.g., broker platform, Morningstar, Seeking Alpha, company IR pages).
- Payout ratios and FCF data significantly improve sustainability analysis; encourage users to include them.

**Known Limitations:**
- DRIP model assumes a static reinvestment price equal to the current share price — actual DRIP purchases occur at varying prices throughout the year.
- Dividend growth rates are backward-looking; future growth may differ materially.
- The skill does not model share price appreciation, total return, or tax drag on non-DRIP income.
- REIT and MLP holdings require