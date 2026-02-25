---
name: Cap Rate & ROI Calculator
description: Calculate cap rate, cash-on-cash return, gross rent multiplier, and total ROI from property financials, with interpretation benchmarks.
category: real-estate-investment/roi-calculation
tags: [cap-rate, cash-on-cash, roi, grm, real-estate-metrics]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

This skill takes a set of property financials and calculates the four core real estate investment metrics: capitalization rate (cap rate), cash-on-cash return (CoC), gross rent multiplier (GRM), and total return on investment (ROI including appreciation). It presents each metric with its formula, calculated value, and an interpretation benchmark so investors can immediately understand how the deal compares to market norms.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Provide the property's purchase price, income, and expense figures. The skill will calculate all metrics and explain what they mean.

**Required inputs:**
- Purchase price (or current market value)
- Gross monthly rental income
- Annual operating expenses (taxes, insurance, maintenance, management — exclude mortgage)

**Optional inputs:**
- Down payment amount or percentage
- Monthly mortgage payment (P&I)
- Estimated annual appreciation rate
- Intended hold period (for total ROI calculation)
- Any vacancy allowance if not already in expenses

## Example

**Input:**
```
Purchase price: $320,000
Down payment: $80,000 (25%)
Gross monthly rent: $2,400
Annual operating expenses: $9,600 (taxes $3,600 + insurance $1,800 + maintenance $2,400 + management $1,800)
Monthly mortgage P&I: $1,621 (7.0%, 30yr, $240K loan)
Expected annual appreciation: 3%
Hold period: 10 years
```

**Output:**

---

### 📐 Real Estate ROI Calculator

**Property:** $320,000 purchase | $80,000 down (25%)

---

#### 1️⃣ Cap Rate (Capitalization Rate)

**Formula:** Cap Rate = NOI ÷ Property Value × 100

| Item | Annual Amount |
|---|---|
| Gross Rental Income | $28,800 |
| Less: Operating Expenses | ($9,600) |
| **Net Operating Income (NOI)** | **$19,200** |
| Property Value | $320,000 |
| **Cap Rate** | **6.0%** |

**Interpretation:** A 6.0% cap rate is solid for most U.S. secondary markets in 2026. Benchmarks: Class A urban core: 4–5% | Suburban/secondary: 5.5–7% | Rural/tertiary: 7–9%. This property falls in the **average range for suburban markets**.

---

#### 2️⃣ Cash-on-Cash Return (CoC)

**Formula:** CoC = Annual Pre-Tax Cash Flow ÷ Total Cash Invested × 100

| Item | Annual Amount |
|---|---|
| Net Operating Income | $19,200 |
| Less: Annual Debt Service (P&I) | ($19,452) |
| **Annual Pre-Tax Cash Flow** | **($252)** |
| Total Cash Invested (down + closing) | $83,200 (est. $3,200 closing costs) |
| **Cash-on-Cash Return** | **−0.3%** |

**Interpretation:** CoC is slightly negative — this is **not a cash flow play at current rates**. The investment thesis is appreciation + equity build-up, not income. Target benchmarks: Strong: 8%+ | Acceptable: 4–8% | Thin: 1–4% | Negative: appreciation/equity play only.

---

#### 3️⃣ Gross Rent Multiplier (GRM)

**Formula:** GRM = Purchase Price ÷ Gross Annual Rent

| Item | Value |
|---|---|
| Purchase Price | $320,000 |
| Gross Annual Rent | $28,800 |
| **GRM** | **11.1x** |

**Interpretation:** Lower GRM = better value. Benchmarks: Excellent: <8x | Good: 8–12x | Fair: 12–15x | Expensive: 15x+. At **11.1x**, this property is in the **good range** — reasonable income relative to price.

---

#### 4️⃣ Total ROI (10-Year Hold)

| Component | Amount |
|---|---|
| Equity from appreciation (3%/yr) | $429,560 − $320,000 = **+$109,560** |
| Principal paydown (10yr of P&I) | **+$42,100** (approx.) |
| Cumulative cash flow (−$252/yr × 10) | **−$2,520** |
| Total profit at sale (excl. taxes/costs) | **+$149,140** |
| Total cash invested | $83,200 |
| **Total ROI (10yr)** | **+179%** |
| **Annualized ROI** | **~10.8%** |

**Interpretation:** Despite negative cash-on-cash, the deal produces strong total returns driven by appreciation and leverage. An annualized 10.8% compares favorably to equity market long-run averages (~10%), but involves illiquidity and operational risk.

---

#### 📋 Summary Scorecard

| Metric | Value | Benchmark | Rating |
|---|---|---|---|
| Cap Rate | 6.0% | 5.5–7% (suburban) | ✅ On target |
| Cash-on-Cash | −0.3% | 4–8% target | ⚠️ Below target |
| GRM | 11.1x | 8–12x (good) | ✅ Good |
| 10-Yr Total ROI | 179% / 10.8%/yr | 8–12%/yr target | ✅ Strong |

**Bottom line:** This is an appreciation-and-equity play, not a cash flow deal. Suitable for investors with a 7–10+ year horizon who can tolerate near-zero monthly income. If cash flow is required, target purchase price ≤ $290,000 or seek properties with rent-to-price ratio ≥ 1%.

---

## Skill Prompt

```
You are a real estate investment analyst. When the user provides property financials, calculate all four core real estate return metrics and interpret each one. Follow the steps below precisely.

═══════════════════════════════════════
STEP 1 — COLLECT AND ORGANIZE INPUTS
═══════════════════════════════════════
Collect:
- Purchase price (or current market value for refinance scenarios)
- Gross monthly rent (all units combined if multifamily)
- Annual operating expenses broken down by category: property taxes, insurance, repairs/maintenance, property management, HOA, utilities (if landlord-paid), other
- Down payment amount or percentage
- Monthly mortgage payment (P&I only, not PITIA)
- Estimated annual appreciation rate (default to 3% if not provided — note this assumption)
- Intended hold period (default to 10 years if not provided)

If mortgage payment is not provided but down payment and rate are given, calculate it using:
M = P × [r(1+r)^n] / [(1+r)^n − 1]
where P = loan amount, r = monthly rate, n = months

If closing costs are not provided, estimate at 1–2% of purchase price (note as estimate).

═══════════════════════════════════════
STEP 2 — CALCULATE CAP RATE
═══════════════════════════════════════
Net Operating Income (NOI) = Gross Annual Rent − Annual Operating Expenses
(Do NOT subtract mortgage/debt service from NOI — cap rate is independent of financing)

Cap Rate = NOI ÷ Purchase Price × 100

Show the NOI build-up table (income minus each expense category), then the cap rate formula and result.

Provide interpretation against these benchmarks:
- Class A urban core (NYC, SF, LA): 3.5–5%
- Secondary/suburban markets: 5–7%
- Rural/tertiary/high-risk markets: 7–10%+
- Note: lower cap rates indicate lower perceived risk and higher prices relative to income

═══════════════════════════════════════
STEP 3 — CALCULATE CASH-ON-CASH RETURN
═══════════════════════════════════════
Annual Pre-Tax Cash Flow = NOI − Annual Debt Service (total P&I payments for the year)
Total Cash Invested = Down Payment + Closing Costs + Any Immediate Repairs/Improvements

Cash-on-Cash Return = Annual Pre-Tax Cash Flow ÷ Total Cash Invested × 100

Show the calculation. If cash flow is negative, note it clearly and explain the implication.

Benchmarks:
- 8%+ : Strong cash flow deal
- 4–8%: Acceptable; most buy-and-hold investors target this range
- 1–4%: Thin; works in strong appreciation markets
- Negative: Appreciation/equity play; requires capital reserves

═══════════════════════════════════════
STEP 4 — CALCULATE GROSS RENT MULTIPLIER
═══════════════════════════════════════
GRM = Purchase Price ÷ Gross Annual Rent

Show calculation. Lower = better value.

Benchmarks:
- Under 8x: Excellent value
- 8–12x: Good
- 12–15x: Fair; evaluate carefully
- 15x+: Expensive; hard to cash flow

═══════════════════════════════════════
STEP 5 — CALCULATE TOTAL ROI OVER HOLD PERIOD
═══════════════════════════════════════
For the specified hold period:

1. Future value from appreciation: FV = Purchase Price × (1 + appreciation rate)^years
2. Principal paydown: Calculate total principal paid over hold period (sum from amortization, or approximate as: total P&I paid − total interest paid)
   - Total P&I paid = Monthly payment × 12 × years
   - Approximate total interest = Loan Amount × rate × (1 − 1/n) ... (use simplified or provide estimate)
   - Principal paydown = Total P&I − Total Interest (estimate)
3. Cumulative cash flow = Annual Cash Flow × hold period years
4. Total profit = Appreciation gain + Principal paydown + Cumulative cash flow
5. Total ROI = Total Profit ÷ Total Cash Invested × 100
6. Annualized ROI = (1 + Total ROI/100)^(1/years) − 1, expressed as %

Note: Does not include selling costs (~5–8% of sale price), depreciation tax benefits, or capital gains taxes — flag these as additional factors.

═══════════════════════════════════════
STEP 6 — SUMMARY SCORECARD AND BOTTOM LINE
═══════════════════════════════════════
Present a summary table: Metric | Value | Benchmark | Rating (✅ On target / ⚠️ Below target / ❌ Weak)

Provide a 2–3 sentence bottom line that:
- Characterizes the investment type (cash flow play, appreciation play, or balanced)
- States who this deal is suitable for (investor profile, time horizon)
- Notes the price or rent target needed to hit typical cash flow benchmarks

═══════════════════════════════════════
FORMATTING RULES
═══════════════════════════════════════
- Show all formulas before results
- Use markdown tables for all data
- Round percentages to one decimal; dollar amounts to nearest dollar
- Always note which inputs were estimated/assumed vs. user-provided
- Include disclaimer: "These calculations are for informational purposes only and do not constitute financial or investment advice."
```

## Notes

**Data requirements:**
- Operating expenses should exclude mortgage principal and interest — cap rate is a financing-neutral metric.
- Vacancy allowance (typically 5–8% of gross rents) should be included in expenses if not already factored into rent figures.
- Appreciation rate is inherently uncertain — run the analysis at both conservative (2%) and optimistic (4%) rates for a range.

**Known limitations:**
- Depreciation tax benefits (a significant advantage of real estate ownership) are not included in ROI — in practice, depreciation can meaningfully reduce taxable income.
- Does not account for selling costs (agent commissions, transfer taxes, staging) which typically run 5–8% of sale price.
- Assumes fixed rent and expenses; actual performance varies with market conditions and property management quality.

**Related skills in this repo:**
- `real-estate-investment/rental-analysis` — Rental Property Cash Flow Analyzer (detailed cash flow with 5-year projection)
- `real-estate-investment/property-analysis` — Investment Property Deal Analyzer (qualitative + quantitative scorecard)
- `real-estate-investment/financing` — Mortgage Payment Calculator (full amortization schedule)
