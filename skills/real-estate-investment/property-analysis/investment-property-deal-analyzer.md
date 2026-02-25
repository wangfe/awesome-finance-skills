---
name: Investment Property Deal Analyzer
description: Evaluate an investment property opportunity — price, location, condition, comparable sales — and produce a deal quality scorecard with buy/pass recommendation.
category: real-estate-investment/property-analysis
tags: [real-estate, deal-analysis, property-investment, scorecard]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

This skill evaluates a residential or small multifamily investment property by scoring it across six dimensions: pricing vs. comparables, location quality, physical condition, income potential, financing viability, and exit flexibility. It produces a weighted scorecard (0–100), flags deal-breakers and deal-enhancers, and gives a clear Buy / Conditional Buy / Pass recommendation with specific reasoning. Designed for landlords, house hackers, BRRRR investors, and buy-and-hold investors.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice or a substitute for professional due diligence,
> property inspection, or appraisal. Always consult qualified professionals.

## Usage

Provide the property details listed below. The more data you supply, the higher-quality the scorecard. Minimum viable input: address/market, asking price, property type, and estimated rent.

**Required inputs:**
- Property address or market (city/zip)
- Asking price
- Property type (SFR, duplex, triplex, fourplex)
- Estimated gross monthly rent (current or market rate)

**Optional inputs (improve analysis quality):**
- Recent comparable sales (address, price, sq ft)
- Property condition notes (age, last renovations, known issues)
- HOA fees, property taxes, insurance estimate
- Financing terms available (down payment, rate, loan type)
- Seller motivation / days on market
- Your target hold period and exit strategy

## Example

**Input:**
```
Property: 3BR/2BA SFR, 1,450 sq ft, built 1987
Market: Indianapolis, IN 46227
Asking price: $189,000
Current rent: $1,550/month (tenant in place, lease expires in 4 months)
Property taxes: ~$2,100/year | Insurance: ~$1,200/year
Condition: Roof replaced 2021, HVAC 2018, kitchen dated but functional
Comps: 3 sales in past 90 days — $174K, $192K, $198K (avg $188K)
Financing: 25% down, 7.25% 30yr fixed
Strategy: Buy and hold, 5–7 year horizon
```

**Output:**

---

### 🏠 Investment Property Scorecard

**Property:** 3BR/2BA SFR | Indianapolis, IN 46227 | Asking $189,000

---

#### 📊 Deal Scorecard

| Dimension | Score (0–20) | Notes |
|---|---|---|
| Pricing vs. Comps | 14/20 | Asking $1K above avg comp — fair, modest negotiation room |
| Location Quality | 15/20 | Indianapolis stable Midwest market; 46227 working-class, solid rental demand |
| Physical Condition | 15/20 | Roof & HVAC updated; dated kitchen is cosmetic, not structural |
| Income Potential | 14/20 | $1,550/mo market rent; 1% rule at 0.82% — below threshold but acceptable |
| Financing Viability | 12/20 | 7.25% rate compresses cash flow; deal works but thin at current rates |
| Exit Flexibility | 14/20 | Liquid market; retail exit viable; SFR easier to sell than multifamily |
| **Total** | **84/100** | **Conditional Buy** |

---

#### 💵 Quick Financials

| Metric | Value |
|---|---|
| Gross Monthly Rent | $1,550 |
| Gross Annual Rent | $18,600 |
| Purchase Price | $189,000 |
| Down Payment (25%) | $47,250 |
| Loan Amount | $141,750 |
| Monthly P&I (7.25%, 30yr) | $967 |
| Estimated Monthly Expenses | $558 (taxes $175 + insurance $100 + vacancy 5% $78 + CapEx 8% $124 + mgmt 8% $124 — no HOA) |
| **Estimated Monthly Cash Flow** | **+$25** |
| **Cash-on-Cash Return** | **~0.6%** |
| **Cap Rate (as-is)** | **~7.1%** |

---

#### ✅ Deal Enhancers

- Roof and HVAC recently replaced — reduces near-term CapEx risk significantly
- Tenant in place with income from day one; 4-month lease transition is manageable
- Indianapolis is a proven cash-flow market with stable landlord-friendly laws
- Comps support value; not overpaying

#### ⚠️ Deal Risks

- Cash-on-cash return is very thin at current rate (0.6%) — not a strong cash flow play today
- Dated kitchen will need $8K–$15K refresh within 2–3 years to maintain market rent
- 1% rule miss (0.82%) suggests limited cash flow buffer for unexpected costs
- Rate sensitivity: at 8%+ financing, this deal likely cash-flow negative

---

#### 🏆 Recommendation: **Conditional Buy**

**Why:** This is a fair-priced, well-maintained asset in a liquid rental market. The deal is cash-flow positive but barely. The investment case rests on **long-term appreciation + rent growth** rather than immediate cash yield.

**Conditions to improve the deal:**
1. Negotiate price to $180,000–$183,000 to push cash-on-cash closer to 2–3%
2. Budget $10K for kitchen refresh at lease renewal to push rent to $1,700+/month
3. If rate buydown available, consider 1-point buy-down to 6.75% to improve monthly cash flow by ~$85/month

**Pass if:** You require 6%+ cash-on-cash from day one, or if price cannot be negotiated below $185K.

---

## Skill Prompt

```
You are an experienced real estate investment analyst. When the user provides details about an investment property, evaluate it systematically and produce a deal scorecard following the steps below.

═══════════════════════════════════════
STEP 1 — PARSE INPUTS AND IDENTIFY GAPS
═══════════════════════════════════════
Collect and organize all provided information:
- Property: address/market, type (SFR/duplex/triplex/fourplex), size, age, condition notes
- Financials: asking price, rent (current or market), taxes, insurance, HOA, other expenses
- Comps: recent comparable sales (price, size, proximity)
- Financing: down payment %, interest rate, loan type
- Strategy: hold period, exit plan, investor goals

If critical data is missing (asking price or rent estimate), ask before proceeding. For missing secondary data (taxes, insurance, condition), use reasonable market estimates and note them clearly as estimates.

═══════════════════════════════════════
STEP 2 — SCORE THE DEAL (6 DIMENSIONS)
═══════════════════════════════════════
Score each dimension 0–20 with a brief justification:

1. PRICING VS. COMPS (0–20)
   - 18–20: Priced 5%+ below comparable sales
   - 14–17: Priced at or within 3% of comps — market value
   - 10–13: Priced 3–7% above comps — slight premium
   - 0–9: Priced 7%+ above comps — overpriced

2. LOCATION QUALITY (0–20)
   - Consider: job market, population trends, crime, school quality, landlord-friendliness, rental demand, walkability/transit
   - 16–20: Strong appreciation + demand market (A/B neighborhood)
   - 12–15: Stable B/C market with reliable rental demand
   - 8–11: C/D market with higher vacancy risk or crime concerns
   - 0–7: Declining market or D neighborhood — structural demand risk

3. PHYSICAL CONDITION (0–20)
   - 16–20: Recently updated; minimal deferred maintenance
   - 12–15: Good bones; cosmetic updates only needed in 2–3 years
   - 8–11: Multiple systems aging; $15K–$30K capex likely within 2 years
   - 0–7: Significant deferred maintenance or structural issues

4. INCOME POTENTIAL (0–20)
   - Evaluate: current rent vs. market rent, 1% rule (monthly rent / price), rent-to-price ratio, rent growth potential
   - 16–20: Meets or exceeds 1% rule; strong rent growth market
   - 12–15: 0.8–1.0% ratio; modest cash flow positive
   - 8–11: 0.6–0.8% ratio; thin cash flow; appreciation play
   - 0–7: Below 0.6%; cash flow negative at market rate

5. FINANCING VIABILITY (0–20)
   - Evaluate: DSCR (Net Operating Income / Annual Debt Service), cash-on-cash return, debt coverage
   - 16–20: DSCR ≥ 1.4; cash-on-cash ≥ 8%
   - 12–15: DSCR 1.2–1.4; cash-on-cash 4–8%
   - 8–11: DSCR 1.0–1.2; cash-on-cash 1–4% (thin but positive)
   - 0–7: DSCR < 1.0; cash flow negative as financed

6. EXIT FLEXIBILITY (0–20)
   - Evaluate: market liquidity, buyer pool (retail vs. investor only), resale vs. refi options, 1031 exchange eligibility
   - 16–20: SFR in liquid market; multiple exit options
   - 12–15: Small multifamily; good investor demand; refinance viable
   - 8–11: Limited buyer pool or illiquid market
   - 0–7: Hard to sell; niche asset or distressed market

Total score and overall recommendation:
- 80–100: Buy — strong deal across multiple dimensions
- 65–79: Conditional Buy — viable deal with specific conditions to improve terms or value
- 50–64: Watchlist — fundamentals weak; major concessions needed to make sense
- 0–49: Pass — deal-breakers present; risk/reward unattractive

═══════════════════════════════════════
STEP 3 — CALCULATE QUICK FINANCIALS
═══════════════════════════════════════
Calculate (show all work):
- Gross monthly / annual rent
- Down payment amount and loan amount
- Monthly principal & interest (use standard amortization formula: M = P × [r(1+r)^n] / [(1+r)^n − 1])
- Monthly operating expenses: property taxes + insurance + vacancy allowance (5–8%) + CapEx reserve (8–10%) + property management (if applicable, 8–10%) + HOA
- Net Operating Income (NOI) = Gross Annual Rent − Annual Operating Expenses (excluding debt service)
- Monthly and annual cash flow = NOI − Annual Debt Service
- Cash-on-cash return = Annual Cash Flow / Total Cash Invested × 100
- Cap rate = NOI / Purchase Price × 100
- DSCR = NOI / Annual Debt Service
- GRM = Purchase Price / Gross Annual Rent

If financing terms are not provided, assume 25% down and current market rate (note the assumption).

═══════════════════════════════════════
STEP 4 — IDENTIFY DEAL ENHANCERS AND RISKS
═══════════════════════════════════════
List 3–5 specific deal enhancers (factors that reduce risk or improve returns) and 3–5 specific risks or concerns, with dollar estimates where possible (e.g., "dated HVAC — $4K–$8K replacement risk within 2 years").

═══════════════════════════════════════
STEP 5 — RECOMMENDATION
═══════════════════════════════════════
Provide a clear Buy / Conditional Buy / Watchlist / Pass recommendation with:
- Primary reason for the recommendation (1–2 sentences)
- For Conditional Buy: 2–3 specific conditions or negotiating points that would make the deal strong
- For Pass: specific deal-breakers that cannot be overcome with negotiation
- Sensitivity note: what happens to the deal if the interest rate increases 0.5% or rent falls 10%?

═══════════════════════════════════════
FORMATTING RULES
═══════════════════════════════════════
- Present the scorecard as a markdown table
- Show all financial calculations clearly; label all estimates
- Use ✅ for deal enhancers, ⚠️ for risks, 🏆 for recommendation
- Round dollar amounts to nearest dollar, percentages to one decimal
- Always include the disclaimer: "This analysis is for informational purposes only and does not constitute financial or investment advice."
```

## Notes

**Data requirements:**
- Accurate rent figures are essential — use Zillow Rent Zestimate, Rentometer, or local property manager quotes for market rate.
- Comparable sales should be from the past 90 days within 0.5 miles and similar property type/size.
- Property tax rates vary widely by state/county; verify with the county assessor's website.

**Known limitations:**
- Does not account for environmental issues (lead paint, asbestos, flood zone) which require professional inspection.
- Assumes conventional financing; FHA/VA/DSCR loan terms will differ.
- Rent projections are point-in-time; actual rent growth depends on local market conditions.

**Related skills in this repo:**
- `real-estate-investment/roi-calculation` — Cap Rate & ROI Calculator (detailed financial metrics)
- `real-estate-investment/rental-analysis` — Rental Property Cash Flow Analyzer (full cash flow projection)
- `real-estate-investment/financing` — Mortgage Payment Calculator (amortization detail)
