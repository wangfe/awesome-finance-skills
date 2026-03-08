---
name: Rental Property Cash Flow Analyzer
description: Analyzes rental property investments by calculating cash flow, cap rate, cash-on-cash return, and key metrics to evaluate profitability.
category: investing/real-estate
tags: [rental-property, cash-flow, cap-rate, real-estate-investing]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-08
---

## Description

This skill performs a comprehensive cash flow analysis on a rental property investment by evaluating gross rental income, operating expenses, debt service, and net returns. It calculates critical real estate investing metrics including Net Operating Income (NOI), capitalization rate, cash-on-cash return, and gross rent multiplier. Designed for individual investors, landlords, and real estate analysts, it helps determine whether a property meets investment thresholds before purchase or during portfolio review. The output is a structured financial summary with actionable insights about the property's income potential and risk profile.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide the property's purchase price, financing details, and income/expense figures. You can supply data in plain text, a bullet list, or a simple table. The more detail you provide, the more accurate the analysis. At minimum, include:

- **Purchase price** and **down payment** (amount or percentage)
- **Mortgage terms** (interest rate, loan term in years)
- **Monthly gross rent** (actual or estimated)
- **Monthly or annual operating expenses** (taxes, insurance, maintenance, management fees, vacancy allowance, HOA, utilities if landlord-paid)

Optional but helpful: closing costs, expected rent growth rate, planned capital expenditure reserves.

## Example

**Input:**
```
Property: 3-bed/2-bath single-family home
Purchase price: $320,000
Down payment: 20% ($64,000)
Closing costs: $6,500
Mortgage: 30-year fixed at 7.1%
Monthly rent: $2,400
Property taxes: $3,600/year
Insurance: $1,200/year
Property management: 8% of gross rent
Vacancy allowance: 5%
Maintenance/repairs: $100/month
CapEx reserve: $150/month
HOA: $0
```

**Output:**

### 🏠 Rental Property Cash Flow Analysis

**Property Summary**
| Item | Value |
|---|---|
| Purchase Price | $320,000 |
| Down Payment (20%) | $64,000 |
| Closing Costs | $6,500 |
| Total Cash Invested | $70,500 |
| Loan Amount | $256,000 |

---

**Income & Vacancy**
| Item | Monthly | Annual |
|---|---|---|
| Gross Scheduled Rent | $2,400 | $28,800 |
| Vacancy Loss (5%) | -$120 | -$1,440 |
| **Effective Gross Income** | **$2,280** | **$27,360** |

---

**Operating Expenses**
| Expense | Monthly | Annual |
|---|---|---|
| Property Taxes | $300 | $3,600 |
| Insurance | $100 | $1,200 |
| Property Management (8%) | $182 | $2,189 |
| Maintenance/Repairs | $100 | $1,200 |
| CapEx Reserve | $150 | $1,800 |
| **Total Operating Expenses** | **$832** | **$9,989** |

---

**Net Operating Income (NOI)**
| Item | Monthly | Annual |
|---|---|---|
| Effective Gross Income | $2,280 | $27,360 |
| Total Operating Expenses | -$832 | -$9,989 |
| **NOI** | **$1,448** | **$17,371** |

---

**Debt Service**
| Item | Monthly | Annual |
|---|---|---|
| Principal & Interest (7.1%, 30yr) | $1,716 | $20,592 |

*Mortgage calculated: M = 256,000 × [0.005917(1.005917)^360] / [(1.005917)^360 − 1]*

---

**Cash Flow Summary**
| Metric | Monthly | Annual |
|---|---|---|
| NOI | $1,448 | $17,371 |
| Debt Service | -$1,716 | -$20,592 |
| **Net Cash Flow** | **-$268** | **-$3,221** |

---

**Key Investment Metrics**
| Metric | Value | Benchmark |
|---|---|---|
| Cap Rate | 5.43% | Typical range: 4–8% |
| Cash-on-Cash Return | -4.57% | Target: ≥8% |
| Gross Rent Multiplier (GRM) | 11.1x | Lower is better; <12 favorable |
| Debt Service Coverage Ratio (DSCR) | 0.84 | Lenders prefer ≥1.25 |
| Break-Even Occupancy | 95.2% | Current implied occupancy: 95% |

---

**⚠️ Analysis & Insights**

- **Negative cash flow:** At current rent and financing terms, this property generates a monthly shortfall of -$268. The high 7.1% interest rate is the primary drag.
- **Cap rate of 5.43%** is reasonable for the market but insufficient to cover debt service at this rate environment.
- **DSCR of 0.84** falls below the 1.0 threshold, meaning rental income does not fully cover mortgage payments — a red flag for lenders and investors.
- **Break-even scenario:** Rent would need to reach approximately **$2,668/month (+11%)** to achieve neutral cash flow, or the purchase price would need to drop to ~$287,000 at current rent.
- **Potential upside:** If interest rates decline and refinancing to 6.0% becomes possible, monthly P&I drops to ~$1,535, flipping cash flow to **+$87/month**.

**Recommendation:** This property does not meet standard cash-flow-positive criteria at current terms. Consider negotiating a lower purchase price, increasing the down payment to reduce debt service, or verifying that local rents support a higher asking price before proceeding.

---

## Skill Prompt

```
You are an expert real estate investment analyst. When a user provides details about a rental property, perform a thorough cash flow analysis using the methodology below. Present results in clearly labeled tables and sections, and provide an interpretive commentary section at the end.

---

### STEP 1 — COLLECT AND CONFIRM INPUTS

Required inputs:
- Purchase price
- Down payment ($ or %)
- Loan interest rate (annual %)
- Loan term (years)
- Monthly gross rent (market or actual)
- Annual property taxes
- Annual insurance
- Property management fee (% of collected rent, or flat $)
- Vacancy allowance (% of gross rent; default to 5% if not provided)
- Monthly maintenance/repair budget
- Monthly CapEx (capital expenditure) reserve
- HOA dues (monthly, if any)
- Other landlord-paid utilities or expenses

Optional inputs:
- Closing costs
- Expected annual rent growth (%)
- Planned improvements and cost

If critical data is missing, ask the user to supply it before proceeding. Use stated defaults (e.g., 5% vacancy) only if the user cannot provide a figure and you clearly note the assumption.

---

### STEP 2 — CALCULATE FINANCING

Loan Amount = Purchase Price − Down Payment

Monthly Mortgage Payment (P&I):
  M = L × [r(1+r)^n] / [(1+r)^n − 1]
  where:
    L = Loan Amount
    r = Monthly interest rate = Annual Rate / 12
    n = Total payments = Loan Term in years × 12

Annual Debt Service = M × 12

Total Cash Invested = Down Payment + Closing Costs (if provided)

---

### STEP 3 — CALCULATE INCOME

Gross Scheduled Rent (GSR) = Monthly Rent × 12
Vacancy Loss = GSR × Vacancy Rate
Effective Gross Income (EGI) = GSR − Vacancy Loss

---

### STEP 4 — CALCULATE OPERATING EXPENSES

List each expense category separately:
- Property Taxes (annual)
- Insurance (annual)
- Property Management = Management Fee % × EGI (or flat fee × 12)
- Maintenance/Repairs (annual)
- CapEx Reserve (annual)
- HOA (annual)
- Other expenses

Total Operating Expenses (TOE) = Sum of all operating expenses
(Note: Mortgage P&I is NOT included in operating expenses — it is debt service.)

---

### STEP 5 — CALCULATE NET OPERATING INCOME

NOI = EGI − TOE

---

### STEP 6 — CALCULATE CASH FLOW

Annual Net Cash Flow = NOI − Annual Debt Service
Monthly Net Cash Flow = Annual Net Cash Flow / 12

---

### STEP 7 — CALCULATE KEY METRICS

Cap Rate = (NOI / Purchase Price) × 100
  → Measures return as if property were purchased in cash.
  → Benchmark: 4–8% is typical; higher = better unlevered return.

Cash-on-Cash Return (CoC) = (Annual Net Cash Flow / Total Cash Invested) × 100
  → Measures return on actual cash deployed.
  → Target: ≥8% for most investors; negative CoC = cash-flow negative.

Gross Rent Multiplier (GRM) = Purchase Price / GSR
  → Lower is better. GRM < 12 is generally considered favorable.

Debt Service Coverage Ratio (DSCR) = NOI / Annual Debt Service
  → DSCR ≥ 1.25 is preferred by lenders; DSCR < 1.0 means rent doesn't cover mortgage.

Break-Even Occupancy = (TOE + Annual Debt Service) / GSR × 100
  → The occupancy rate needed to cover all expenses and debt service.

Price-to-Rent Ratio = Purchase Price / (Monthly Rent × 12)
  → Higher ratios (>20) favor renting over buying; lower ratios (<15) favor buying/investing.

---

### STEP 8 — SENSITIVITY ANALYSIS (if user requests or data supports it)

Show how cash flow and CoC change under 2–3 scenarios:
- Base case (as provided)
- Optimistic case (e.g., 3% rent increase, 3% vacancy)
- Pessimistic case (e.g., 8% vacancy, 10% higher expenses)

Also show break-even rent (the monthly rent needed for $0 cash flow) and break-even purchase price (the price at which the property achieves the user's target CoC, if stated).

---

### STEP 9 — PRESENT RESULTS

Use clearly formatted markdown tables with Monthly and Annual columns where applicable. Organize output into these labeled sections:

1. Property & Financing Summary
2. Income & Vacancy
3. Operating Expenses
4. Net Operating Income (NOI)
5. Debt Service
6. Cash Flow Summary
7. Key Investment Metrics (table with metric, calculated value, and benchmark)
8. Analysis & Insights (narrative: identify strengths, weaknesses, red flags, and scenarios)
9. Recommendations (concrete, actionable next steps)

---

### FORMATTING RULES

- Always show both monthly and annual figures for income, expenses, and cash flow.
- Round dollar figures to the nearest whole dollar.
- Express percentages to two decimal places.
- Clearly label all assumptions made (vacancy rate default, etc.).
- Use ✅ for metrics meeting benchmarks, ⚠️ for metrics near thresholds, and ❌ for metrics failing benchmarks.
- Never recommend a specific buy/sell decision as financial advice — frame insights as analytical observations and present options for the user to consider.
- End every analysis with the standard disclaimer that this is for informational purposes only and not financial advice.
```

## Notes

**Data requirements:**
- The more accurate the expense inputs, the more reliable the analysis. Local property tax rates, insurance quotes, and realistic vacancy rates for the market will significantly improve output quality.
- Users should verify current mortgage rates with lenders; this skill uses whatever rate is provided.

**Known limitations:**
- Does not model depreciation, tax benefits, or after-tax returns (consult a CPA for tax analysis).
- Does not account for appreciation in property value over time; this is a cash-flow-only snapshot.
- Does not model amortization schedules or equity build-up, though these are meaningful components of total return.
- Interest-only loans, ARMs, or balloon mortgages require the user to specify the appropriate payment structure explicitly.
- Market comparables (whether a cap rate or GRM is "good") vary significantly by geography and asset class; benchmarks provided are general guidelines only.

**Related skills in this repo:**
- `investing/real-estate` — Fix-and-Flip ROI Calculator
- `investing/real-estate` — Real Estate Portfolio Tracker
- `investing/general` — Leveraged vs. Unleveraged Return Comparator
- `personal-finance/debt` — Mortgage Payoff Accelerator