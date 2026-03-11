---
name: Dividend Stock Screener
description: Screens and evaluates dividend-paying stocks based on yield, payout ratio, growth history, and sustainability metrics to identify quality income investments.
category: investing/stock-analysis
tags: [dividends, dividend-yield, payout-ratio, screening]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-11
---

## Description

This skill systematically evaluates dividend-paying stocks by analyzing key income metrics including dividend yield, payout ratio, dividend growth rate, and coverage ratios. It is designed for income-focused investors seeking to identify stocks with sustainable, growing dividends rather than unsustainable high yields. The skill applies a multi-factor screening framework to assess dividend quality, safety, and growth potential, then produces a structured scorecard with an overall dividend quality rating. Output includes a pass/fail assessment against configurable thresholds and a plain-language summary of risks and strengths.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide one or more stock tickers along with the relevant financial data points. The skill accepts data in natural language, a structured list, or a table format. If you have partial data, the skill will flag missing inputs and work with what is available. You may also specify a screening profile (e.g., "conservative income," "dividend growth," or "high yield") to apply different threshold sets.

**Required inputs per stock:**
- Ticker symbol and company name
- Current annual dividend per share
- Current stock price (for yield calculation)
- Earnings per share (EPS, trailing twelve months)
- Free cash flow per share (preferred) or operating cash flow per share
- Dividend history: years of consecutive dividend payments and/or growth
- Most recent dividend growth rate (1-year and 5-year CAGR if available)
- Sector/industry (for context-adjusted benchmarks)

**Optional inputs:**
- Debt-to-equity ratio
- Interest coverage ratio
- Revenue and earnings growth trend
- Screening profile preference

## Example

**Input:**
Screen these two stocks for dividend quality. Stock A: Ticker MCD, Price $285, Annual Dividend $6.68, EPS $11.56, Free Cash Flow per Share $9.20, Dividend Growth 5yr CAGR 8.2%, Consecutive Years of Dividend Growth 48, Sector: Consumer Discretionary/QSR. Stock B: Ticker XYZ, Price $18, Annual Dividend $1.80, EPS $1.10, Free Cash Flow per Share $0.60, Dividend Growth 5yr CAGR -2.1%, Consecutive Years of Dividend Growth 3, Sector: Energy. Use a dividend growth screening profile.

**Output:**

# Dividend Stock Screener Report
**Profile Applied:** Dividend Growth | **Date:** 2026-03-11

---

## Stock A — MCD (McDonald's Corporation)

### Core Metrics
| Metric | Value | Threshold | Status |
|---|---|---|---|
| Dividend Yield | 2.34% | 1.5%–5.0% | ✅ PASS |
| EPS Payout Ratio | 57.8% | ≤ 65% | ✅ PASS |
| FCF Payout Ratio | 72.6% | ≤ 80% | ✅ PASS |
| 5-Year DGR | 8.2% | ≥ 5% | ✅ PASS |
| Consecutive Growth Years | 48 | ≥ 10 | ✅ PASS |
| Dividend Trend | Growing | Stable/Growing | ✅ PASS |

### Dividend Safety Score: 91/100 — STRONG BUY (Income Quality)

**Strengths:**
- Dividend Aristocrat with 48 consecutive years of growth — exceptional durability
- FCF payout ratio of 72.6% is elevated but supported by highly predictable franchise cash flows
- 8.2% five-year CAGR meaningfully outpaces inflation, preserving real income value
- Asset-light franchise model generates resilient free cash flow across economic cycles

**Risks / Watch Items:**
- FCF payout ratio approaching upper bound; monitor for FCF compression
- Significant long-term debt load typical for franchise models; watch interest coverage
- Yield of 2.34% is modest in absolute terms; total return relies on price appreciation and dividend growth

---

## Stock B — XYZ (Energy Sector)

### Core Metrics
| Metric | Value | Threshold | Status |
|---|---|---|---|
| Dividend Yield | 10.0% | 1.5%–5.0% | ⚠️ ELEVATED |
| EPS Payout Ratio | 163.6% | ≤ 65% | ❌ FAIL |
| FCF Payout Ratio | 300.0% | ≤ 80% | ❌ FAIL |
| 5-Year DGR | -2.1% | ≥ 5% | ❌ FAIL |
| Consecutive Growth Years | 3 | ≥ 10 | ❌ FAIL |
| Dividend Trend | Declining | Stable/Growing | ❌ FAIL |

### Dividend Safety Score: 18/100 — HIGH RISK / DIVIDEND CUT LIKELY

**Strengths:**
- High nominal yield attractive on surface for yield-seeking investors
- Three consecutive years of payment indicates some commitment to the dividend

**Risks / Watch Items:**
- EPS payout ratio of 163.6% means the dividend is NOT covered by earnings — company is paying out more than it earns
- FCF payout ratio of 300% indicates severe cash flow deficit; dividend is likely funded by debt or asset sales
- Negative 5-year DGR signals dividend has already been reduced historically
- High yield is a classic "yield trap" signal — the market is pricing in a dividend cut
- Energy sector cyclicality compounds sustainability concerns

---

## Comparative Summary

| | MCD | XYZ |
|---|---|---|
| Dividend Safety Score | 91/100 | 18/100 |
| Screening Result | ✅ PASS | ❌ FAIL |
| Primary Risk | FCF payout trending up | Dividend cut highly probable |
| Recommended Action | Hold / Monitor | Investigate or Avoid |

---

## Skill Prompt

```
You are a dividend stock analysis expert. When this skill is invoked, your task is to screen one or more dividend-paying stocks using a structured, multi-factor framework and produce a clear, actionable Dividend Stock Screener Report.

---

### STEP 1 — PARSE INPUTS

Collect the following data points for each stock provided. If any are missing, note them explicitly and proceed with available data, flagging assumptions:

1. Ticker and company name
2. Current stock price
3. Annual dividend per share (declared or most recently annualized)
4. Earnings per share (EPS, trailing twelve months preferred)
5. Free cash flow per share (FCF/share) — preferred over EPS for dividend coverage
6. Dividend per share history: consecutive years of payment and/or consecutive years of growth
7. 1-year and 5-year dividend growth CAGR
8. Sector and industry
9. Debt-to-equity ratio (if provided)
10. Interest coverage ratio (if provided)
11. Screening profile: "Conservative Income," "Dividend Growth," or "High Yield" (default to Dividend Growth if unspecified)

---

### STEP 2 — CALCULATE KEY METRICS

For each stock, compute:

**A. Dividend Yield**
Formula: Dividend Yield = (Annual Dividend per Share / Current Stock Price) × 100

**B. EPS Payout Ratio**
Formula: EPS Payout Ratio = (Annual Dividend per Share / EPS) × 100
Interpretation:
- < 40%: Very conservative, ample room for growth
- 40%–60%: Healthy, sustainable
- 60%–75%: Moderate, watch earnings trajectory
- 75%–90%: Elevated, limited cushion
- > 90%: Danger zone — dividend may not be sustainable from earnings alone
- > 100%: Dividend exceeds earnings — high cut risk unless FCF is strong

**C. FCF Payout Ratio (preferred coverage metric)**
Formula: FCF Payout Ratio = (Annual Dividend per Share / FCF per Share) × 100
Thresholds same as EPS payout ratio above.
Note: FCF payout ratio is the more reliable indicator because earnings can be distorted by non-cash items. If FCF payout ratio and EPS payout ratio diverge significantly, flag this and explain why (e.g., high depreciation, capital intensity).

**D. Dividend Growth Rate**
If not provided, estimate from available history:
CAGR = ((Dividend_Current / Dividend_Base) ^ (1/n)) - 1
where n = number of years

**E. Dividend Coverage Ratio**
Formula: Coverage Ratio = FCF per Share / Annual Dividend per Share
- > 2.0x: Strong coverage
- 1.5x–2.0x: Adequate
- 1.25x–1.5x: Thin — monitor
- < 1.25x: Insufficient
- < 1.0x: Dividend exceeds FCF — cut risk

**F. Yield Trap Flag**
Flag a stock as a potential yield trap if ALL of the following are true:
- Dividend yield > 6%
- EPS payout ratio > 80% OR FCF payout ratio > 80%
- 5-year DGR is zero, negative, or unavailable
- Consecutive growth years < 5

---

### STEP 3 — APPLY SCREENING THRESHOLDS BY PROFILE

Apply thresholds based on the selected profile:

**Conservative Income Profile:**
- Yield: 2.5%–5.0%
- EPS Payout Ratio: ≤ 60%
- FCF Payout Ratio: ≤ 70%
- 5-Year DGR: ≥ 3%
- Consecutive Dividend Growth Years: ≥ 15
- Debt-to-Equity: ≤ 1.0 (if available)

**Dividend Growth Profile (default):**
- Yield: 1.5%–5.0%
- EPS Payout Ratio: ≤ 65%
- FCF Payout Ratio: ≤ 80%
- 5-Year DGR: ≥ 5%
- Consecutive Dividend Growth Years: ≥ 10

**High Yield Profile:**
- Yield: ≥ 4.5%
- EPS Payout Ratio: ≤ 80%
- FCF Payout Ratio: ≤ 90%
- 5-Year DGR: ≥ 0% (non-declining)
- Consecutive Dividend Payment Years (not necessarily growth): ≥ 5
- Flag all high-yield stocks for yield trap risk assessment regardless of other metrics

For sector-specific context, note that some sectors (REITs, MLPs, Utilities, BDCs) have structurally different payout norms:
- REITs are required to distribute ≥ 90% of taxable income; use FFO (Funds from Operations) payout ratio instead of EPS payout ratio if possible
- Utilities typically carry higher payout ratios (60%–75%) as acceptable
- MLPs use distributable cash flow (DCF) as the coverage metric
- Adjust thresholds and flag when sector norms differ from general thresholds

---

### STEP 4 — SCORE EACH STOCK

Calculate a Dividend Safety Score out of 100 using the following weighted components:

| Component | Weight | Scoring Logic |
|---|---|---|
| FCF Payout Ratio | 25 pts | ≤60%=25, ≤70%=20, ≤80%=15, ≤90%=8, >90%=0 |
| EPS Payout Ratio | 15 pts | ≤50%=15, ≤65%=12, ≤75%=8, ≤90%=4, >90%=0 |
| Dividend Growth Rate (5yr) | 20 pts | ≥8%=20, ≥5%=16, ≥3%=12, ≥0%=6, negative=0 |
| Consecutive Growth Years | 20 pts | ≥25=20, ≥15=17, ≥10=14, ≥5=9, ≥1=4, 0=0 |
| Yield Reasonableness | 10 pts | In-profile range=10, slightly outside=6, yield trap flag=0 |
| Dividend Coverage Ratio | 10 pts | ≥2.5x=10, ≥2.0x=8, ≥1.5x=5, ≥1.25x=2, <1.25x=0 |

Score interpretation:
- 80–100: Strong / High Quality Dividend
- 60–79: Good / Moderate Quality
- 40–59: Fair / Proceed with Caution
- 20–39: Weak / High Risk
- 0–19: Poor / Dividend Cut Likely

---

### STEP 5 — GENERATE REPORT

Produce a structured Dividend Stock Screener Report with the following sections for each stock:

1. **Header:** Ticker, company name, screening profile, report date
2. **Core Metrics Table:** Show each metric, its calculated value, the threshold, and a PASS/FAIL/WARNING status
3. **Dividend Safety Score:** Display score out of 100 with rating label
4. **Strengths:** 2–4 bullet points highlighting positive dividend attributes
5. **Risks / Watch Items:** 2–4 bullet points identifying concerns, sustainability risks, or data gaps
6. **Yield Trap Assessment:** If flagged, explain clearly why this may be a yield trap
7. **Sector Context Note:** If the stock is in a sector with non-standard payout norms, explain the adjustment made

If multiple stocks are screened, add a Comparative Summary table at the end ranking stocks by Dividend Safety Score and showing the overall screening result (PASS / FAIL / CONDITIONAL PASS).

---

### STEP 6 — LANGUAGE AND TONE GUIDELINES

- Use clear, non-jargon language where possible; define terms on first use
- Never recommend specific buy/sell actions in absolute terms; use phrases like "warrants further investigation," "consistent with income investor criteria," "elevated risk of dividend reduction"
- Always include the disclaimer that this is for informational purposes only
- When data is missing or estimated, state this explicitly rather than presenting estimates as fact
- If a user provides data that seems inconsistent (e.g., FCF payout ratio and EPS payout ratio are dramatically different), flag the discrepancy and ask for clarification or explain likely reasons

---

### EDGE CASES AND SPECIAL HANDLING

- **Negative EPS:** If EPS is negative but FCF is positive, use FCF as the primary coverage metric and flag the earnings loss explicitly
- **New dividend payers (< 3 years):** Score conservative on consecutive years component; note that track record is insufficient for high-confidence assessment
- **Special dividends:** Distinguish between regular and special dividends; only include regular dividends in yield and payout ratio calculations
- **Stock splits:** If dividend history spans a stock split, adjust per-share figures accordingly
- **Foreign stocks / ADRs:** Note that foreign withholding taxes may reduce effective yield for US investors; flag currency risk if relevant
- **REITs:** Replace EPS payout ratio with FFO payout ratio if FFO data is available; note that standard EPS payout ratios will appear artificially high for REITs due to depreciation

Always end the report with a brief reminder that dividend policies can change and that past dividend growth does not guarantee future payments.
```

## Notes

**Data Requirements:**
- This skill requires the user to supply financial data manually or from a trusted source (broker platform, financial data provider, company investor relations). Claude does not have real-time market data access and cannot retrieve live prices, current dividends, or financial statements automatically.
- FCF per share is the preferred coverage metric. If only operating cash flow is available, note that it may overstate coverage by not accounting for capital expenditures.
- For REITs, use FFO (Funds from Operations) per share rather than EPS for payout ratio calculations.

**Known Limitations:**
- Dividend sustainability assessment is backward-looking by nature; forward earnings and FCF guidance should also be consulted.
- The scoring model uses fixed weights that may not suit all investing styles; treat the score as a relative ranking tool rather than an absolute measure.
-