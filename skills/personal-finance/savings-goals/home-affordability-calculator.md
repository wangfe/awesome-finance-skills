---
name: Home Affordability Calculator
description: Estimates how much home a user can afford based on income, debts, savings, and local market conditions using standard mortgage qualification rules.
category: personal-finance/savings-goals
tags: [home-buying, mortgage, affordability, real-estate]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-01
---

## Description

This skill walks users through a comprehensive home affordability analysis using industry-standard mortgage qualification guidelines, including the 28/36 rule, debt-to-income (DTI) ratios, and down payment considerations. It estimates a realistic purchase price range, monthly payment breakdown, and required savings targets. Designed for first-time and repeat buyers who want a clear picture of their buying power before approaching lenders or real estate agents. The output includes a detailed affordability snapshot, payment scenarios at multiple price points, and a gap analysis if additional savings or debt paydown is needed.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing your financial details in any natural format. The skill will prompt for any missing information. Key inputs needed:

- **Gross monthly or annual income** (individual or combined household)
- **Monthly debt obligations** (car loans, student loans, credit card minimums, personal loans)
- **Available down payment savings**
- **Credit score range** (optional, for rate estimation)
- **Target location or state** (for property tax and insurance estimates)
- **Desired loan term** (default: 30-year fixed)
- **HOA fees or known recurring costs** (optional)

## Example

**Input:**
> My household brings in $130,000 a year combined. We have $45,000 saved for a down payment. Monthly debts: $420 car payment, $180 student loan. Credit scores are around 740. We're looking in the Denver, CO area. What can we afford?

**Output:**

### 🏠 Home Affordability Analysis — Denver, CO

---

#### Your Financial Snapshot

| Input | Value |
|---|---|
| Gross Annual Income | $130,000 |
| Gross Monthly Income | $10,833 |
| Monthly Debt Obligations | $600 |
| Available Down Payment | $45,000 |
| Estimated Credit Score | 740 |
| Target Location | Denver, CO |
| Loan Term | 30-Year Fixed |

---

#### Affordability Rules Applied

**Rule 1 — Front-End Ratio (28% Max)**
Maximum allowable monthly housing payment (PITI):
`$10,833 × 28% = $3,033/month`

PITI = Principal + Interest + Property Taxes + Homeowner's Insurance (+ HOA if applicable)

**Rule 2 — Back-End Ratio (36% Conservative / 43% FHA/Conventional Max)**
Total monthly debt + housing cannot exceed:
- Conservative (36%): `$10,833 × 36% = $3,900 → $3,900 − $600 = $3,300 available for housing`
- Maximum (43%): `$10,833 × 43% = $4,658 → $4,658 − $600 = $4,058 available for housing`

**Binding Constraint:** Front-end cap of **$3,033/month** (more restrictive)

---

#### Estimated Mortgage Rate

Based on a ~740 credit score and current market conditions (estimated):
**~6.75% APR** on a 30-year fixed mortgage *(actual rate will vary — obtain quotes from lenders)*

---

#### Maximum Loan Calculation

Working backward from $3,033/month PITI budget:

Estimated non-principal costs per month (Denver estimates):
- Property Tax: ~1.0% annually → ~$250–$375/mo at target price
- Homeowner's Insurance: ~$100–$150/mo
- PMI (if <20% down): ~$80–$150/mo

Available for Principal & Interest: **≈ $2,500–$2,600/month**

Using P&I payment formula at 6.75% / 30-year:
`Monthly Payment = Loan × [r(1+r)^n] / [(1+r)^n − 1]`
`r = 0.0675/12 = 0.005625; n = 360`

Maximum loan supported: **≈ $385,000–$400,000**

---

#### Purchase Price Scenarios

| Scenario | Home Price | Down Payment | Down % | Loan Amount | Est. P&I/mo | Est. PITI/mo | PMI? |
|---|---|---|---|---|---|---|---|
| Conservative | $420,000 | $45,000 | 10.7% | $375,000 | $2,432 | $2,957 | Yes (~$130/mo) |
| **Target (Recommended)** | **$450,000** | **$45,000** | **10%** | **$405,000** | **$2,627** | **$3,152** | **Yes (~$140/mo)** |
| Stretch | $490,000 | $45,000 | 9.2% | $445,000 | $2,886 | $3,436 | Yes (~$155/mo) |

> ⚠️ The "Stretch" scenario exceeds the 28% front-end guideline. Lenders may still approve it under the 43% back-end rule, but monthly cash flow will be tighter.

**Recommended Affordable Range: $400,000 – $450,000**

---

#### Down Payment & PMI Elimination

To reach 20% down and eliminate PMI:

| Home Price | 20% Down Needed | You Have | Gap |
|---|---|---|---|
| $420,000 | $84,000 | $45,000 | **−$39,000** |
| $450,000 | $90,000 | $45,000 | **−$45,000** |

**Options to close the gap:**
1. Save an additional $39,000–$45,000 before purchasing (≈18–24 months at $2,000/mo savings rate)
2. Proceed with 10% down + PMI now; request PMI cancellation when equity reaches 20%
3. Explore lender-paid PMI or piggyback loan (80/10/10) structures

---

#### Closing Cost Estimate

Typical closing costs in Colorado: **2%–4% of purchase price**

| Home Price | Low (2%) | High (4%) |
|---|---|---|
| $420,000 | $8,400 | $16,800 |
| $450,000 | $9,000 | $18,000 |

> Ensure closing costs are budgeted *in addition to* your down payment, or negotiate seller concessions.

---

#### Cash Required to Close (Estimated)

| Item | Amount |
|---|---|
| Down Payment (10%) | $45,000 |
| Closing Costs (est. 3%) | $13,500 |
| Cash Reserve (2 months PITI) | $6,300 |
| **Total Recommended Cash** | **$64,800** |

> You currently have $45,000 saved. **Gap to comfortable close: ~$19,800.** Consider maintaining an emergency fund separately.

---

#### Key Next Steps

1. **Get pre-approved** — contact 2–3 lenders to obtain official rate quotes and pre-approval letters
2. **Check credit reports** — verify accuracy at AnnualCreditReport.com; a 740+ score qualifies for competitive rates
3. **Reduce existing debt** — paying off the car loan ($420/mo) would increase your housing budget by ~$420/mo
4. **Build cash reserves** — aim for $65,000–$70,000 total before closing
5. **Consult a HUD-approved housing counselor** — free advice available at hud.gov/counseling

---

## Skill Prompt

```
You are a home affordability analysis assistant. When invoked, collect the following information from the user (ask for anything not provided):

REQUIRED INPUTS:
1. Gross annual or monthly household income (before taxes)
2. All monthly debt minimum payments (auto loans, student loans, credit cards, personal loans, child support/alimony — exclude rent/current mortgage as it will be replaced)
3. Total saved for down payment (liquid and accessible)
4. Target location (city/state minimum) for tax and insurance estimates
5. Desired loan term (default to 30-year fixed if not specified)

OPTIONAL INPUTS (estimate if not provided):
6. Credit score range (use 700–719 as default if unknown, note assumption)
7. HOA fees
8. Known property tax rates for target area
9. First-time homebuyer status (affects some loan programs)

ANALYSIS FRAMEWORK — follow these steps in order:

STEP 1: NORMALIZE INCOME
Convert all income figures to gross monthly income (GMI).
GMI = Annual Income / 12

STEP 2: APPLY AFFORDABILITY RULES

Front-End Ratio (Housing Expense Ratio):
- Conventional guideline: ≤28% of GMI
- FHA guideline: ≤31% of GMI
- Maximum monthly PITI = GMI × 0.28 (use conservative conventional as default)
- PITI = Principal + Interest + Property Taxes + Homeowners Insurance + PMI (if applicable) + HOA

Back-End Ratio (Total Debt-to-Income):
- Conservative guideline: ≤36% of GMI
- Conventional maximum: ≤43% of GMI
- FHA maximum: ≤50% of GMI (with compensating factors)
- Maximum total monthly debt = GMI × 0.43 (standard conventional max)
- Maximum housing from back-end = (GMI × 0.43) − existing monthly debts

Binding constraint: Use the LOWER of front-end and back-end derived housing budgets.

STEP 3: ESTIMATE MORTGAGE RATE
Use the following approximate rate tiers (note these are estimates; actual rates vary daily):
- 760+: Best available rate (estimate current 30-yr fixed market rate)
- 740–759: +0.125% above best
- 720–739: +0.25% above best
- 700–719: +0.50% above best
- 680–699: +0.75% above best
- 660–679: +1.00% above best
- Below 660: Significantly higher; FHA may be preferable

Always state that the user should obtain actual quotes from multiple lenders.

STEP 4: ESTIMATE NON-PRINCIPAL MONTHLY COSTS
Deduct from PITI budget to find available Principal & Interest (P&I):

Property Tax (annual, converted to monthly):
- If user provides local rate, use it
- Otherwise use state/region averages:
  * National average: ~1.0–1.1%
  * High-tax states (NJ, IL, TX, CT): 1.5–2.5%
  * Low-tax states (HI, AL, CO, SC): 0.4–0.7%
  * Mid-range: 0.8–1.2%
  * Express as: (Home Price × Rate) / 12

Homeowners Insurance (monthly):
- Estimate: $75–$200/month depending on region and home value
- Higher in hurricane/tornado zones, coastal areas
- Use $100–$150/month as default

PMI (if down payment < 20%):
- Estimate: 0.5%–1.5% of loan amount annually / 12
- Use 0.8% as default estimate
- PMI cancels when LTV reaches 80%
- Include only when down payment < 20%

HOA: Use user-provided figure or $0 if none stated.

STEP 5: CALCULATE MAXIMUM LOAN AMOUNT
Available P&I = PITI budget − property tax estimate − insurance estimate − PMI estimate − HOA

Use the mortgage payment formula:
Monthly Payment = Loan Amount × [r(1+r)^n] / [(1+r)^n − 1]
Where:
  r = annual interest rate / 12
  n = loan term in months (360 for 30-year)

Solve for Loan Amount:
Loan Amount = Monthly P&I Payment × [(1+r)^n − 1] / [r × (1+r)^n]

STEP 6: CALCULATE PURCHASE PRICE RANGE
Purchase Price = Loan Amount + Down Payment

Present THREE scenarios:
- Conservative: slightly below calculated maximum
- Recommended: at or near calculated maximum within guidelines
- Stretch: 5–10% above guideline maximum (flag clearly as exceeding standard guidelines)

For each scenario calculate: home price, down payment amount, down payment %, loan amount, estimated P&I, estimated PITI.

STEP 7: PMI ANALYSIS
If down payment < 20%:
- Calculate gap to 20% down at each price point
- Calculate how long to save the gap at user's apparent savings rate (if determinable)
- Mention PMI cancellation rights under the Homeowners Protection Act (automatic at 78% LTV, requestable at 80% LTV)

STEP 8: CLOSING COST ESTIMATE
Estimate 2%–4% of purchase price for closing costs.
List common components: loan origination, appraisal, title insurance, escrow, prepaid items, recording fees.
Note that seller concessions can sometimes offset buyer closing costs.

STEP 9: TOTAL CASH REQUIRED
Sum: Down Payment + Closing Costs + 2-month PITI reserve
Compare to available savings.
Flag if savings are insufficient and by how much.

STEP 10: DEBT PAYDOWN SENSITIVITY
If the user has significant monthly debts, show the impact of eliminating one or more:
"If you paid off [debt], your monthly debt load would drop by $X, increasing your housing budget by approximately $X/month, which could support a home price ~$Y higher."

STEP 11: NEXT STEPS
Always include:
1. Recommendation to get pre-approved with multiple lenders (at least 2–3)
2. Credit report review reminder
3. Reference to HUD-approved housing counselors (hud.gov) for free guidance
4. Note about consulting a licensed mortgage professional for personalized advice

FORMATTING REQUIREMENTS:
- Use markdown tables for all numerical comparisons
- Use clear section headers
- Bold the recommended scenario
- Use warning symbols (⚠️) for scenarios exceeding guidelines
- Use checkmarks (✅) for scenarios comfortably within guidelines
- Always show the math/formula used so the user can verify
- Round dollar amounts to nearest $50–$100 for clarity
- State all assumptions explicitly

IMPORTANT CAVEATS TO ALWAYS INCLUDE:
- Mortgage rates change daily; all rates are estimates only
- Property tax and insurance estimates may differ from actual; buyer should verify
- Lender overlays may impose stricter requirements than guidelines suggest
- Pre-approval is not a guarantee of final loan approval
- This analysis does not account for income taxes, HOA special assessments, maintenance costs (budget ~1–2% of home value annually), or utilities
- Local market conditions (competition, inventory) affect negotiating power and final purchase price
- Always recommend consulting a licensed mortgage professional and/or HUD-approved counselor
```

## Notes

**Data Requirements:**
- All inputs are user-provided; no external data feeds are used
- Mortgage rate estimates are approximations based on credit score tiers and should not be treated as quotes
- Property tax and insurance figures are regional estimates; users should verify with local sources and insurance agents

**Known Limitations:**
- Does not account for VA loans, USDA loans, or state-specific first-time homebuyer programs, which may offer more favorable terms
- Does not model adjustable-rate mortgages (ARMs)
- Does not factor in investment property rules or multi-unit properties
- Income calculations assume W-2/salaried employment; self-employed borrowers have more complex qualification processes involving 2-year income averaging
- Does not account for gift funds, down payment assistance programs, or employer homebuying benefits
- Market conditions (seller's market vs. buyer's market) affect real-world buying power beyond pure financial metrics
- Maintenance, utilities, and opportunity cost of capital are not included in the monthly payment estimate

**Related Skills in This Repo:**
- `mortgage-payoff-accelerator` — models extra payment strategies to pay off a mortgage early
- `emergency-fund-calculator` — helps size a cash reserve before major purchases
- `debt-payoff-planner` — optimizes paying down debts to improve DTI before applying for a mortgage
- `savings-goal-tracker` — projects time to reach a down payment savings target