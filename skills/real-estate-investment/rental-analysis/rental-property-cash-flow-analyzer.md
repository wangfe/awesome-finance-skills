---
name: Rental Property Cash Flow Analyzer
description: Full rental property cash flow analysis — NOI, monthly and annual cash flow, break-even occupancy, and 5-year projection with rent growth assumptions.
category: real-estate-investment/rental-analysis
tags: [rental-property, cash-flow, noi, break-even, real-estate]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

This skill performs a comprehensive rental property cash flow analysis for residential and small multifamily properties (1–4 units). It calculates Net Operating Income (NOI), monthly and annual pre-tax cash flow, break-even occupancy rate, and projects 5-year performance assuming user-specified rent growth and expense inflation. Output includes a month-1 cash flow waterfall, annual summary, and a 5-year projection table with cumulative equity and return metrics.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Provide property financials including income and all expense line items. The skill generates a detailed cash flow analysis and multi-year projection.

**Required inputs:**
- Property type (SFR, duplex, triplex, fourplex)
- Number of units and rent per unit (or total monthly gross rent)
- Purchase price and financing terms (down payment %, interest rate, loan term)
- Annual property taxes and insurance

**Optional inputs:**
- Vacancy rate assumption (default: 5%)
- CapEx reserve % of gross rent (default: 8%)
- Property management fee % (default: 10% if not self-managed, 0% if self-managed)
- Maintenance/repairs estimate (default: 1% of property value per year)
- Annual rent growth assumption (default: 3%)
- Annual expense inflation assumption (default: 2%)
- HOA fees, utilities (if landlord-paid), other recurring costs

## Example

**Input:**
```
Property: Duplex (2 units)
Unit A: $1,100/month | Unit B: $1,050/month
Purchase price: $285,000
Down payment: 20% ($57,000)
Rate: 7.0%, 30-year fixed
Property taxes: $3,400/year
Insurance: $1,600/year
Property management: 10%
Vacancy: 6%
CapEx reserve: 8%
Maintenance: 1% of value/year
Rent growth: 3%/year
Expense inflation: 2%/year
```

**Output:**

---

### 🏢 Rental Property Cash Flow Analysis

**Property:** Duplex | Purchase Price: $285,000 | Down Payment: $57,000 (20%)

---

#### 💧 Year 1 Cash Flow Waterfall

| Line Item | Monthly | Annual |
|---|---|---|
| Gross Scheduled Rent (2 units) | $2,150 | $25,800 |
| Less: Vacancy (6%) | ($129) | ($1,548) |
| **Effective Gross Income** | **$2,021** | **$24,252** |
| Less: Property Taxes | ($283) | ($3,400) |
| Less: Insurance | ($133) | ($1,600) |
| Less: Property Management (10%) | ($202) | ($2,425) |
| Less: Maintenance (1% of value) | ($238) | ($2,850) |
| Less: CapEx Reserve (8% of EGI) | ($162) | ($1,940) |
| **Net Operating Income (NOI)** | **$1,003** | **$12,037** |
| Less: Mortgage P&I | ($1,516) | ($18,192) |
| **Pre-Tax Cash Flow** | **($513)** | **($6,155)** |

---

#### 📊 Key Metrics (Year 1)

| Metric | Value |
|---|---|
| Cap Rate | 4.2% |
| Cash-on-Cash Return | −10.3% |
| Gross Rent Multiplier (GRM) | 11.1x |
| Break-Even Occupancy Rate | 124.6% ← cash flow negative at any occupancy |
| Debt Coverage Ratio (DSCR) | 0.66 |
| Total Cash Invested (incl. est. closing) | $59,850 |

> ⚠️ **Alert:** This property is cash-flow **negative at current financing**. The DSCR of 0.66 means the mortgage payment is 51% larger than NOI. This deal only makes sense as an appreciation or BRRRR play, or if the rents can be raised to approximately $2,750+/month total.

---

#### 📈 Break-Even Analysis

**Break-even rent (to cover all expenses + mortgage):**
Annual mortgage ($18,192) + Annual operating expenses ($12,215) = $30,407 needed
Required monthly rent = $30,407 ÷ 12 ÷ (1 − 0.06 vacancy) = **$2,693/month total**

**Gap to break-even:** Current rent $2,150 → need $2,693 (+**$543/month** or **+25.3%** rent increase)

---

#### 📅 5-Year Cash Flow Projection

| Year | Gross Rent | NOI | Mortgage P&I | Cash Flow | Cumulative Cash Flow | Loan Balance |
|---|---|---|---|---|---|---|
| 1 | $25,800 | $12,037 | $18,192 | ($6,155) | ($6,155) | $221,508 |
| 2 | $26,574 | $12,571 | $18,192 | ($5,621) | ($11,776) | $214,691 |
| 3 | $27,371 | $13,125 | $18,192 | ($5,067) | ($16,843) | $207,534 |
| 4 | $28,192 | $13,701 | $18,192 | ($4,491) | ($21,334) | $200,019 |
| 5 | $29,038 | $14,300 | $18,192 | ($3,892) | ($25,226) | $192,131 |

**At 3% annual rent growth, cash flow breaks even approximately in Year 7–8.**

---

#### 🏗️ 5-Year Equity Build (at 3% appreciation)

| Source | Amount |
|---|---|
| Down payment (equity at purchase) | $57,000 |
| Principal paydown (5 years) | $6,069 |
| Appreciation (3%/yr × 5yr ≈ 15.9%) | $45,315 |
| **Total Equity at Year 5** | **$108,384** |
| Less: Cumulative negative cash flow | ($25,226) |
| **Net equity gain** | **+$83,158** |
| **5-Year Total Return on Investment** | **+138.9%** (on $59,850 invested) |

---

## Skill Prompt

```
You are a rental property cash flow analyst. When the user provides property and financing details, perform a comprehensive cash flow analysis and multi-year projection. Follow these steps precisely.

═══════════════════════════════════════
STEP 1 — COLLECT AND NORMALIZE INPUTS
═══════════════════════════════════════
Gather:
- Property type and number of units
- Rent per unit or total monthly gross rent
- Purchase price, down payment, interest rate, loan term
- Annual property taxes and insurance
- Management fee % (or 0% if self-managed)
- Vacancy rate (if not provided, default to 5% SFR / 6% multifamily)
- CapEx reserve % (default 8% of Effective Gross Income)
- Maintenance/repairs (default 1% of purchase price per year)
- HOA fees and any other recurring costs
- Rent growth rate per year (default 3%)
- Expense inflation rate per year (default 2%)
- Hold period for projection (default 5 years)

If financing terms are incomplete, calculate the monthly P&I payment from available data:
M = P × [r(1+r)^n] / [(1+r)^n − 1]
where P = loan amount, r = monthly rate (annual/12), n = total months

Closing costs: if not provided, estimate at 2% of purchase price (note as estimate).

═══════════════════════════════════════
STEP 2 — BUILD YEAR 1 CASH FLOW WATERFALL
═══════════════════════════════════════
Present a table with Monthly and Annual columns:

1. Gross Scheduled Rent (all units at full occupancy)
2. Less: Vacancy allowance = Gross Rent × vacancy rate
3. = Effective Gross Income (EGI)
4. Less: Property Taxes
5. Less: Insurance
6. Less: Property Management Fee (on EGI)
7. Less: Maintenance/Repairs
8. Less: CapEx Reserve (% of EGI)
9. Less: HOA (if applicable)
10. Less: Utilities (if landlord-paid)
11. = Net Operating Income (NOI)
12. Less: Annual Mortgage P&I
13. = Pre-Tax Cash Flow (label as positive or negative)

═══════════════════════════════════════
STEP 3 — CALCULATE KEY METRICS
═══════════════════════════════════════
Calculate and present in a table:
- Cap Rate = NOI ÷ Purchase Price × 100
- Cash-on-Cash Return = Annual Cash Flow ÷ Total Cash Invested × 100
- GRM = Purchase Price ÷ Gross Annual Rent
- DSCR = NOI ÷ Annual Debt Service
- Break-Even Occupancy = (Operating Expenses + Debt Service) ÷ Gross Scheduled Rent × 100
  (If break-even > 100%, flag that the property is cash-flow negative at any occupancy level)
- Total Cash Invested = Down Payment + Closing Costs + Any immediate rehab costs

If DSCR < 1.0, display a prominent alert explaining what this means and what rent would be needed to reach DSCR of 1.0 and 1.2.

═══════════════════════════════════════
STEP 4 — BREAK-EVEN RENT ANALYSIS
═══════════════════════════════════════
Calculate the minimum total monthly rent needed to break even (cash flow = $0):
Break-Even Monthly Rent = (Annual Operating Expenses + Annual Debt Service) ÷ 12 ÷ (1 − vacancy rate)

Show the gap between current rent and break-even rent in dollars and percentage.
If the gap is within 10%, note that break-even is achievable with modest rent increases.
If the gap is >25%, flag this as a significant concern.

═══════════════════════════════════════
STEP 5 — MULTI-YEAR CASH FLOW PROJECTION
═══════════════════════════════════════
Project for each year of the hold period:
- Gross Rent = Prior Year Rent × (1 + rent growth rate)
- Operating Expenses = Prior Year Expenses × (1 + expense inflation rate)
  (Apply inflation to: taxes, insurance, management fee, maintenance, CapEx — NOT to mortgage P&I)
- NOI = Gross Rent × (1 − vacancy rate) − Operating Expenses
- Cash Flow = NOI − Annual Debt Service
- Cumulative Cash Flow = running total
- Loan Balance = remaining principal at year end (use standard amortization)

Present as a table: Year | Gross Rent | NOI | Mortgage P&I | Cash Flow | Cumulative Cash Flow | Loan Balance

If the hold period is 5+ years, note the year when cash flow first becomes positive (if it does).

═══════════════════════════════════════
STEP 6 — EQUITY BUILD SUMMARY
═══════════════════════════════════════
At end of hold period, summarize equity components:
1. Original equity (down payment)
2. Principal paydown over the period
3. Appreciation gain = Purchase Price × ((1 + appreciation rate)^years − 1)
   (Use 3% default if not provided; note this assumption)
4. Total equity = All three components combined
5. Net equity gain = Total equity − cumulative negative cash flow (if any)
6. Total return = Net equity gain ÷ Total Cash Invested × 100
7. Annualized total return = (1 + total return)^(1/years) − 1

Note: excludes selling costs (~5–8%), depreciation tax benefits, and capital gains taxes.

═══════════════════════════════════════
STEP 7 — INVESTOR PROFILE AND RECOMMENDATIONS
═══════════════════════════════════════
Based on the analysis:
- Characterize the deal: Cash Flow Deal / Appreciation Play / BRRRR Candidate / Not Recommended
- State what type of investor this property suits (time horizon, cash reserve, risk tolerance)
- Provide 2–3 specific levers to improve the deal (price negotiation target, rent increase needed, management self-management savings, etc.)

═══════════════════════════════════════
FORMATTING RULES
═══════════════════════════════════════
- Use markdown tables for all data
- Show all formulas used
- Highlight negative cash flow values with explicit labels — never hide losses
- Round to nearest dollar for amounts, one decimal for percentages
- Always note which inputs were assumed (not user-provided)
- Include: "This analysis is for informational purposes only and does not constitute financial or investment advice."
```

## Notes

**Data requirements:**
- For accurate CapEx modeling, it helps to know the age and condition of major systems (roof, HVAC, plumbing, electrical). Older properties warrant higher CapEx reserves (10–12%).
- Management fees vary by market (8–12% of collected rents). Always include even if self-managing — it represents the true economic cost and protects against lifestyle changes.
- Vacancy rates should reflect local market conditions. In tight markets (2% vacancy), use 3–4%; in soft markets, use 7–10%.

**Known limitations:**
- Does not model depreciation tax shelter (a major cash flow benefit; consult a CPA).
- Does not model refinancing scenarios or BRRRR equity recycling.
- Assumes fixed mortgage rate; adjustable-rate scenarios require separate modeling.
- Property condition and unexpected repairs can significantly exceed CapEx reserve estimates.

**Related skills in this repo:**
- `real-estate-investment/roi-calculation` — Cap Rate & ROI Calculator (metrics focus)
- `real-estate-investment/financing` — Mortgage Payment Calculator (amortization detail)
- `real-estate-investment/property-analysis` — Investment Property Deal Analyzer (full deal scorecard)
