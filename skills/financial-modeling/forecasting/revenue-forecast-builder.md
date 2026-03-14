---
name: Revenue Forecast Builder
description: Builds a structured multi-method revenue forecast using both top-down and bottom-up approaches, with growth drivers, scenario analysis, and a reconciled projection table.
category: financial-modeling/forecasting
tags: [revenue-forecast, top-down, bottom-up, growth-modeling]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-14
---

## Description

This skill constructs a comprehensive revenue forecast for a business by combining top-down market-sizing analysis with bottom-up unit-economics modeling. It applies multiple growth methodologies—historical trend extrapolation, market-share capture, cohort-based customer growth, and pricing assumptions—to produce a three-scenario (bear / base / bull) projection for a 1–5 year horizon. The output includes a reconciled forecast table, key assumptions log, and sensitivity commentary, making it suitable for business planning, investor presentations, and internal budgeting.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing the following inputs in any order (structured or conversational):

- **Business description** – what the company sells, its model (SaaS, transactional, product, services, etc.)
- **Historical revenue data** – at least 2–3 years of annual or quarterly revenue figures (optional but strongly recommended)
- **Key metrics** – e.g., number of customers, average contract value (ACV), churn rate, units sold, average selling price (ASP), conversion rates
- **Market data** – total addressable market (TAM), serviceable addressable market (SAM), current market share
- **Forecast horizon** – number of years (1–5 recommended)
- **Growth assumptions or goals** – any known targets, hiring plans, pricing changes, or strategic initiatives
- **Scenario preferences** – whether to use standard ±ranges or custom bear/base/bull assumptions

If data is incomplete, the skill will state its assumptions explicitly and flag gaps for the user to validate.

## Example

**Input:**
```
Build a revenue forecast for my B2B SaaS company. We sell project management software at $120/user/month. Current ARR is $4.2M with 350 customers averaging 10 users each. Monthly churn is 1.2%. We're adding ~15 new customers/month organically, but plan to double our sales team in Q3. TAM is ~$18B, SAM ~$600M. Forecast 3 years, please.
```

**Output:**

### Revenue Forecast — B2B SaaS Project Management Tool
**Forecast Horizon:** 3 Years (Year 1–3) | **Base Date:** Current ARR $4.2M

---

#### 1. Key Assumptions Log

| Assumption | Bear | Base | Bull |
|---|---|---|---|
| New customers/month (pre-sales expansion) | 10 | 15 | 20 |
| New customers/month (post-sales expansion, Q3 Y1+) | 18 | 30 | 45 |
| Monthly gross churn rate | 1.6% | 1.2% | 0.8% |
| Avg. users per customer (expansion) | 10 | 11 | 13 |
| ASP ($/user/month) | $115 | $120 | $125 |
| SAM penetration ceiling (Y3) | 0.8% | 1.1% | 1.6% |

---

#### 2. Bottom-Up Customer & ARR Model (Base Case)

**Formula:**
```
Ending Customers(t) = Ending Customers(t-1) + New Customers(t) − Churned Customers(t)
Churned Customers(t) = Ending Customers(t-1) × Monthly Churn × 12
ARR(t) = Ending Customers(t) × Avg Users × ASP × 12
```

| Period | Starting Customers | New (Annual) | Churned | Ending Customers | ARR |
|---|---|---|---|---|---|
| Current | — | — | — | 350 | $4.20M |
| Year 1 | 350 | 270* | 63 | 557 | $7.37M |
| Year 2 | 557 | 360 | 87 | 830 | $10.97M |
| Year 3 | 830 | 360 | 116 | 1,074 | $15.44M |

*Year 1 blended: 15/mo for first 6 months, 30/mo thereafter = ~270 net new

---

#### 3. Top-Down Sanity Check (Base Case)

```
SAM = $600M
Implied Y3 Market Share = $15.44M / $600M = 2.6% of SAM
→ Slightly aggressive; validate against comparable SaaS comps at Series B/C stage
→ Top-down ceiling at 1.1% SAM penetration = ~$6.6M — suggests bottom-up may be optimistic
→ Reconciled Base: $12.5M–$15.4M range; use $13.5M as conservative base
```

---

#### 4. Three-Scenario Summary (ARR, End of Year)

| Year | Bear | Base | Bull |
|---|---|---|---|
| Year 1 | $5.8M | $7.4M | $9.1M |
| Year 2 | $7.9M | $11.0M | $15.6M |
| Year 3 | $10.2M | $13.5M | $24.3M |
| CAGR | ~34% | ~47% | ~79% |

---

#### 5. Key Risks & Sensitivities

- **Churn is the dominant lever:** A 0.4% increase in monthly churn reduces Y3 ARR by ~$2.1M
- **Sales team ramp lag:** Assume 3–4 month ramp to full productivity post-hire; delays bull case
- **Expansion revenue not modeled:** User seat growth within existing accounts could add 10–20% upside
- **Pricing sensitivity:** $5 ASP decrease reduces Y3 ARR by ~$640K at base customer count

---

## Skill Prompt

```
You are an expert financial modeler specializing in revenue forecasting for early-stage to growth-stage businesses. When this skill is invoked, follow the structured methodology below to build a rigorous, multi-method revenue forecast.

---

## STEP 1: INPUT COLLECTION & CLASSIFICATION

Before building any model, identify and classify the inputs provided:

A. BUSINESS MODEL TYPE — determine the revenue structure:
   - Recurring (SaaS/subscription): key metrics = ARR/MRR, churn, expansion, ACV, seat count
   - Transactional (e-commerce, marketplace): key metrics = orders, AOV, repeat rate, CAC
   - Usage-based: key metrics = active users, consumption rate, unit price
   - Project/services: key metrics = headcount, utilization, billing rate, project pipeline
   - Product (hardware/CPG): key metrics = units sold, ASP, distribution channels, reorder rate

B. HISTORICAL DATA — extract:
   - Revenue by period (annual or quarterly preferred)
   - Growth rates (YoY and QoQ if available)
   - Volume metrics (customers, units, transactions)
   - Any known inflection points (funding, product launches, market events)

C. FORWARD-LOOKING INPUTS — identify:
   - Planned operational changes (hiring, pricing, channel expansion, new products)
   - Market data (TAM, SAM, SOM, growth rate of addressable market)
   - User-stated targets or constraints

D. GAP IDENTIFICATION — explicitly list any missing inputs and state the assumptions you will use in their place. Flag these clearly with [ASSUMED] tags throughout the model.

---

## STEP 2: HISTORICAL TREND ANALYSIS (if data provided)

Calculate and present:
1. YoY and CAGR for available historical periods
2. Revenue per customer/unit trend (pricing power or dilution)
3. Growth rate trend (accelerating, decelerating, or stable)
4. Seasonal patterns if quarterly data is available

Use regression or visual trend description to characterize the historical baseline. State whether growth appears: organic, campaign-driven, market-expansion, or pricing-led.

---

## STEP 3: BOTTOM-UP FORECAST CONSTRUCTION

Build the forecast from unit economics upward. Apply the appropriate model for the business type:

### For Subscription/SaaS:
```
New MRR(t) = New Customers(t) × ACV/12
Expansion MRR(t) = Existing MRR(t-1) × Net Expansion Rate
Churned MRR(t) = Existing MRR(t-1) × Gross Churn Rate
Net New MRR(t) = New MRR(t) + Expansion MRR(t) − Churned MRR(t)
Ending MRR(t) = Starting MRR(t) + Net New MRR(t)
ARR(t) = Ending MRR(t) × 12
```

### For Transactional:
```
Revenue(t) = Active Customers(t) × Order Frequency(t) × AOV(t)
Active Customers(t) = New Customers(t) + Retained Customers(t)
Retained Customers(t) = Active Customers(t-1) × (1 − Churn Rate)
```

### For Usage-Based:
```
Revenue(t) = Active Users(t) × Avg Consumption per User(t) × Unit Price(t)
Active Users(t) = f(acquisition funnel, retention curve)
```

### For Services/Professional Services:
```
Revenue(t) = Billable Headcount(t) × Utilization Rate(t) × Avg Billing Rate(t) × Working Days(t)
```

### For Product/Hardware:
```
Revenue(t) = Units Sold(t) × ASP(t)
Units Sold(t) = Existing Channel Volume × (1 + Channel Growth) + New Channel Volume
```

Build annual projections for each year in the forecast horizon. Show intermediate calculations.

---

## STEP 4: TOP-DOWN FORECAST CONSTRUCTION

1. State TAM, SAM, and SOM (if provided or estimate from business description)
2. Calculate implied market share at end of each forecast year: Market Share(t) = Projected Revenue(t) / SAM
3. Research or estimate comparable market share benchmarks for businesses at similar stages
4. Assess whether implied market share is achievable, aggressive, or conservative
5. Derive a top-down revenue ceiling: Top-Down Revenue(t) = SAM × Achievable Share(t)
6. Compare top-down ceiling to bottom-up projection and explicitly reconcile any gap

---

## STEP 5: SCENARIO CONSTRUCTION

Build three scenarios — Bear, Base, and Bull — by adjusting the key growth levers:

For each scenario, define:
- Growth driver assumptions (acquisition rate, pricing, churn, expansion)
- Revenue outcome by year
- Implied CAGR over the full forecast period

Scenario guidance:
- BEAR: Conservative execution, slower ramp, higher churn, flat pricing
- BASE: Plan-of-record assumptions, moderate execution
- BULL: Accelerated growth, successful new channels, lower churn, price increases realized

Present scenarios in a clean comparison table:

| Year | Bear | Base | Bull |
|------|------|------|------|
| Y1   |      |      |      |
| Y2   |      |      |      |
| Y3+  |      |      |      |
| CAGR |      |      |      |

---

## STEP 6: SENSITIVITY ANALYSIS

Identify the 3–5 variables with the greatest impact on the forecast. For each:
1. Name the variable and its base-case value
2. State a ±range (e.g., ±20% or ±1 percentage point)
3. Quantify the revenue impact in the final forecast year
4. Rank variables by revenue sensitivity (highest impact first)

Present as a sensitivity table or tornado-style commentary.

---

## STEP 7: ASSUMPTIONS LOG

Produce a clean assumptions table covering every key input used. Flag each as:
- [PROVIDED] — given by the user
- [ASSUMED] — derived or estimated by you
- [BENCHMARK] — based on industry norms you are applying

---

## STEP 8: RECONCILIATION & OUTPUT SUMMARY

1. Reconcile bottom-up and top-down projections; select or blend for the final base case
2. Highlight the single most important risk to the forecast
3. Highlight the single most important upside driver
4. Note any data gaps the user should prioritize filling to improve forecast quality
5. Recommend a review cadence (e.g., monthly actuals vs. forecast tracking)

---

## FORMATTING RULES

- Always present numbers in consistent units ($M or $K — choose based on scale)
- Round to 2 decimal places for dollar figures, 1 decimal place for percentages
- Use tables for any multi-year, multi-metric comparisons
- Label every section clearly with a heading
- When making assumptions, be explicit: never bury assumptions in prose
- If the user provides insufficient data to build a meaningful model, ask targeted clarifying questions before proceeding — do not fabricate data

## TONE & STYLE

- Write like a senior FP&A analyst presenting to a CFO or investor
- Be precise but accessible; define any jargon used
- Provide brief qualitative commentary on what the numbers mean, not just what they are
- Flag model risks candidly — do not over-optimize for optimistic outcomes
```

## Notes

**Data Requirements:**
- Minimum viable input: business model type, one revenue figure, and at least one volume metric (e.g., customer count or units sold)
- Richer inputs (3+ years of history, full funnel metrics, market sizing data) produce significantly more reliable outputs
- If TAM/SAM data is not provided, the skill will estimate from business description context and flag as [ASSUMED]

**Known Limitations:**
- The skill does not connect to live financial databases or market research sources; all market benchmarks are knowledge-based and may be dated
- Multi-product or multi-segment revenue forecasts may require the user to run the skill separately per segment and consolidate
- The skill does not model COGS, gross margin, or operating expenses — see the "Unit Economics Analyzer" and "P&L Builder" skills for downstream modeling
- Forecast accuracy is highly sensitive to churn and acquisition assumptions; treat outputs as structured estimates, not guarantees

**Related Skills in This Repo:**
- `financial-modeling/forecasting` — Sales Pipeline Forecast
- `financial-modeling/valuation` — SaaS Valuation Multiples Analyzer
- `financial-modeling/unit-economics` — LTV:CAC Calculator
- `financial-modeling/scenario-analysis` — Monte Carlo Sensitivity Simulator