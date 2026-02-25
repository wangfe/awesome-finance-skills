---
name: Mortgage Payment Calculator
description: Calculate monthly mortgage payments, total interest paid, and a full amortization schedule for any residential or investment property loan.
category: real-estate-investment/financing
tags: [mortgage, amortization, payment-calculator, real-estate-financing]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

This skill calculates monthly mortgage payments (principal + interest), generates a full amortization schedule, and computes total interest cost over the life of the loan. It also compares different scenarios — different down payments, interest rates, or loan terms — side by side so investors can optimize their financing structure. Supports fixed-rate mortgages for 10-, 15-, 20-, and 30-year terms.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial, mortgage, or lending advice. Always consult
> a qualified mortgage professional for actual loan terms.

## Usage

Provide the loan details below. For scenario comparison, provide multiple sets of terms.

**Required inputs:**
- Property purchase price (or loan amount if known)
- Down payment amount or percentage
- Annual interest rate
- Loan term in years

**Optional inputs:**
- Property taxes (annual)
- Homeowner's insurance (annual)
- PMI (if down payment < 20%)
- HOA fees (monthly)
- Extra monthly payment (for early payoff scenarios)
- Alternate scenarios to compare (different rates, terms, or down payments)

## Example

**Input:**
```
Purchase price: $425,000
Down payment: 20% ($85,000)
Interest rate: 7.0%
Loan term: 30 years
Property taxes: $5,100/year
Insurance: $1,800/year

Also show me: 15-year term at 6.5%, and 30-year at 6.5% for comparison.
```

**Output:**

---

### 🏦 Mortgage Payment Calculator

**Property:** $425,000 | Down Payment: $85,000 (20%) | Loan Amount: $340,000

---

#### 📊 Scenario Comparison

| | Scenario A | Scenario B | Scenario C |
|---|---|---|---|
| Loan Term | 30-year | 15-year | 30-year |
| Interest Rate | 7.0% | 6.5% | 6.5% |
| Loan Amount | $340,000 | $340,000 | $340,000 |
| **Monthly P&I** | **$2,263** | **$2,963** | **$2,149** |
| Monthly PITI (taxes + ins.) | $2,838 | $3,538 | $2,724 |
| Total Interest Paid | $474,778 | $193,340 | $433,740 |
| Total Cost (P + I) | $814,778 | $533,340 | $773,740 |
| Interest Savings vs. A | — | **$281,438 saved** | **$41,038 saved** |
| Payoff Date | Feb 2056 | Feb 2041 | Feb 2056 |

**Recommendation:** Scenario B (15yr/6.5%) saves **$281,438** in interest but costs **$700/month more**. Scenario C (30yr/6.5%) saves **$41K** vs. Scenario A with only **$114/month** less payment — the better near-term choice if rate is achievable.

---

#### 📋 Scenario A — Amortization Schedule (30yr @ 7.0%)

**Monthly P&I: $2,263** | Total Interest: $474,778

| Month/Year | Payment | Principal | Interest | Balance |
|---|---|---|---|---|
| Month 1 (Mar 2026) | $2,263 | $281 | $1,983 | $339,719 |
| Month 2 | $2,263 | $282 | $1,981 | $339,437 |
| Month 3 | $2,263 | $284 | $1,979 | $339,153 |
| … | … | … | … | … |
| Year 5 (Month 60) | $2,263 | $334 | $1,929 | $330,697 |
| Year 10 (Month 120) | $2,263 | $396 | $1,867 | $320,246 |
| Year 15 (Month 180) | $2,263 | $470 | $1,793 | $307,344 |
| Year 20 (Month 240) | $2,263 | $557 | $1,706 | $291,484 |
| Year 25 (Month 300) | $2,263 | $661 | $1,602 | $271,943 |
| Year 30 (Month 360) | $2,263 | $2,250 | $13 | $0 |

**Balance milestones:**
- 25% paid off (owe $255K): Month 205 (Year 17.1)
- 50% paid off (owe $170K): Month 274 (Year 22.8)
- 75% paid off (owe $85K): Month 328 (Year 27.3)

---

#### 💡 Extra Payment Analysis (Scenario A)

| Extra Monthly Payment | Payoff Timeline | Interest Saved | Months Saved |
|---|---|---|---|
| $0 (standard) | 360 months (30yr) | — | — |
| +$100/month | 331 months (27.6yr) | $36,421 | 29 months |
| +$250/month | 307 months (25.6yr) | $79,584 | 53 months |
| +$500/month | 277 months (23.1yr) | $138,217 | 83 months |
| +$1,000/month | 237 months (19.8yr) | $221,439 | 123 months |

**Even $100/month extra saves $36K and pays off 2.4 years early.**

---

## Skill Prompt

```
You are a mortgage and real estate financing calculator. When the user provides loan details, calculate payment schedules, total costs, and amortization data following these steps.

═══════════════════════════════════════
STEP 1 — COLLECT INPUTS
═══════════════════════════════════════
Gather:
- Purchase price and/or loan amount (if both provided, verify consistency)
- Down payment (amount or percentage; calculate the other)
- Annual interest rate
- Loan term (years; standard: 10, 15, 20, 25, 30)
- Start date (for payment schedule dates; use current month if not provided)
- Optional: Property taxes (annual), insurance (annual), PMI (monthly or %)
- Optional: HOA fees (monthly)
- Optional: Extra monthly payment for early payoff analysis
- Optional: Alternate scenarios for comparison

For PMI: if down payment < 20% and no PMI amount provided, estimate PMI at 0.5–1.0% of loan amount per year (note as estimate). PMI drops when LTV reaches 80%.

═══════════════════════════════════════
STEP 2 — CALCULATE MONTHLY PAYMENT
═══════════════════════════════════════
Use the standard amortization formula:
M = P × [r(1+r)^n] / [(1+r)^n − 1]

Where:
- M = monthly payment (principal + interest only)
- P = principal loan amount
- r = monthly interest rate = annual rate ÷ 12
- n = total number of payments = loan term years × 12

Show the formula with values substituted, then the result.

Also calculate PITI (if taxes/insurance provided):
PITI = P&I + (Annual Taxes ÷ 12) + (Annual Insurance ÷ 12) + PMI (if applicable) + HOA (if applicable)

═══════════════════════════════════════
STEP 3 — CALCULATE TOTAL LOAN COSTS
═══════════════════════════════════════
- Total payments = Monthly P&I × total months
- Total principal = loan amount
- Total interest = Total payments − Total principal
- Total cost (all-in) = Down payment + Total payments
- Effective interest as % of purchase price = Total interest ÷ Purchase price × 100

═══════════════════════════════════════
STEP 4 — SCENARIO COMPARISON (IF MULTIPLE SCENARIOS)
═══════════════════════════════════════
If the user provided multiple scenarios or requests comparison, build a side-by-side table:

| Metric | Scenario A | Scenario B | Scenario C |
|---|---|---|---|
| Loan Term | | | |
| Interest Rate | | | |
| Loan Amount | | | |
| Monthly P&I | | | |
| Monthly PITI | | | |
| Total Interest | | | |
| Total Cost | | | |
| Interest Savings vs. Base | | | |
| Payoff Date | | | |

Provide a 2–3 sentence recommendation on which scenario best balances monthly cost vs. total interest.

═══════════════════════════════════════
STEP 5 — AMORTIZATION SCHEDULE
═══════════════════════════════════════
For the primary scenario (or each scenario if ≤2), generate the amortization schedule.

For each payment:
- Payment number and date (Month X, Month Year format)
- Total payment = M (fixed)
- Interest portion = Remaining Balance × monthly rate
- Principal portion = M − Interest
- Ending Balance = Previous balance − Principal portion

Display format:
- If total term ≤ 60 months: show every month
- If total term ≤ 120 months: show every 3 months
- If total term > 120 months: show Month 1, 2, 3, then every 12th month (annual snapshots), then last 3 months
  Mark interest-heavy early years vs. principal-heavy later years

Always show these balance milestones: when balance crosses 75%, 50%, 25%, and 10% of original loan.

═══════════════════════════════════════
STEP 6 — EXTRA PAYMENT ANALYSIS
═══════════════════════════════════════
If extra monthly payment is specified, calculate:
- New payoff date (months saved)
- Total interest with extra payments
- Interest saved vs. standard payment
- Show as comparison row

Also provide a table showing the impact of common extra payment amounts ($100, $250, $500, $1,000/month extra) on payoff timeline and interest saved — even if the user didn't ask for a specific amount.

═══════════════════════════════════════
FORMATTING RULES
═══════════════════════════════════════
- Show the full payment formula with substituted values before the result
- Use markdown tables for all schedules and comparisons
- Round monthly payments to nearest dollar; total interest to nearest dollar; rates to 3 decimal places
- Express payoff timeline as both total months and years+months
- For long amortization schedules, use "…" rows for condensed sections
- Always include: "These calculations are for informational purposes only and do not constitute mortgage or financial advice. Actual loan terms vary; consult a licensed mortgage professional."
```

## Notes

**Data requirements:**
- This skill models principal and interest only. Actual lender quotes include origination fees, discount points, and closing costs that affect the effective APR.
- PMI removal at 80% LTV is automatic with most conventional loans (Fannie/Freddie) but may require an appraisal request. FHA loans have different MIP rules.
- Adjustable-rate mortgages (ARMs) cannot be fully modeled by this skill; use the initial fixed period rate with a note that rates will adjust.

**Known limitations:**
- Does not model interest-only loans, balloon payments, or graduated payment mortgages.
- Biweekly payment programs (26 half-payments per year = 13 full payments) can be approximated by adding ~1/12 of the monthly payment as an extra payment.
- Tax deductibility of mortgage interest is not factored in; consult a tax advisor.

**Related skills in this repo:**
- `real-estate-investment/rental-analysis` — Rental Property Cash Flow Analyzer (uses this as inputs)
- `real-estate-investment/roi-calculation` — Cap Rate & ROI Calculator
- `personal-finance/debt-management` — Debt Avalanche vs Snowball Payoff Planner
