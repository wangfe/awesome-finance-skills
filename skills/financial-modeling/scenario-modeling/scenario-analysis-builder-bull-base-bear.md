---
name: Scenario Analysis Builder (Bull / Base / Bear)
description: Constructs a structured three-scenario financial analysis with bull, base, and bear cases, including key driver assumptions, output metrics, and probability-weighted expected values.
category: financial-modeling/scenario-modeling
tags: [scenario-analysis, bull-case, bear-case, sensitivity]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-15
---

## Description

This skill guides Claude through building a rigorous bull / base / bear scenario analysis for any company, project, or investment. The user provides core business details and key value drivers; Claude produces a fully structured three-scenario model with explicit assumptions, projected financial outputs, scenario probabilities, and a probability-weighted expected outcome. It is designed for analysts, investors, founders, and finance students who need a disciplined framework for stress-testing forecasts and communicating range of outcomes.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by describing the subject of the analysis and providing as much of the following as possible:

- **Subject:** Company name, project, or asset being analyzed
- **Sector / industry:** e.g., SaaS, retail, real estate, manufacturing
- **Time horizon:** e.g., 3-year, 5-year forecast
- **Key value drivers:** Revenue growth rate, margins, capex intensity, churn, TAM penetration, commodity prices, etc.
- **Current baseline metrics:** Latest revenue, EBITDA, or any known financials
- **Any specific risk factors or upside catalysts** to incorporate

Claude will then generate the full scenario framework. If key inputs are missing, Claude will ask targeted clarifying questions before building the model.

## Example

**Input:**
> Build a 3-year bull/base/bear scenario analysis for a B2B SaaS company currently generating $20M ARR with 75% gross margins. The main drivers are ARR growth rate, net revenue retention (NRR), and EBITDA margin expansion. Time horizon is 3 years. No debt.

**Output:**

---

### Scenario Analysis: B2B SaaS Company — 3-Year Forecast (FY1–FY3)

#### 1. Key Assumptions by Scenario

| Driver | Bear Case | Base Case | Bull Case |
|---|---|---|---|
| ARR Growth Rate (Yr 1) | 10% | 25% | 45% |
| ARR Growth Rate (Yr 2) | 8% | 22% | 40% |
| ARR Growth Rate (Yr 3) | 6% | 20% | 35% |
| Net Revenue Retention | 95% | 108% | 120% |
| Gross Margin | 72% | 75% | 77% |
| EBITDA Margin (Yr 3) | -5% | 12% | 22% |
| Churn Rate (annual) | 12% | 6% | 3% |

**Bear Case Rationale:** Market saturation or macro-driven budget cuts compress new ARR additions; elevated churn from competitive displacement; margins pressured by higher S&M spend to retain customers.

**Base Case Rationale:** Steady mid-market expansion, NRR above 100% driven by upsells, disciplined hiring; mirrors median SaaS growth cohort at this ARR scale.

**Bull Case Rationale:** Enterprise segment breaks through, NRR expansion from new product modules, operating leverage accelerates; execution matches top-quartile SaaS benchmarks.

---

#### 2. Revenue Build (ARR, $M)

| Metric | Bear Yr1 | Bear Yr3 | Base Yr1 | Base Yr3 | Bull Yr1 | Bull Yr3 |
|---|---|---|---|---|---|---|
| Beginning ARR | $20.0 | — | $20.0 | — | $20.0 | — |
| New ARR Added | $2.0 | $1.4 | $5.0 | $8.6 | $9.0 | $19.4 |
| Churned ARR | ($2.4) | ($2.0) | ($1.2) | ($2.3) | ($0.6) | ($1.4) |
| Ending ARR | $19.6 | $17.8 | $23.8 | $40.5 | $28.4 | $65.8 |
| YoY ARR Growth | -2% | -6% | +19% | +20% | +42% | +35% |

---

#### 3. P&L Summary (Year 3, $M)

| Line Item | Bear | Base | Bull |
|---|---|---|---|
| Revenue (recognized) | $18.5 | $38.2 | $61.0 |
| Gross Profit | $13.3 | $28.7 | $47.0 |
| Gross Margin % | 72% | 75% | 77% |
| Operating Expenses | $14.2 | $23.6 | $33.6 |
| EBITDA | ($0.9) | $4.6 | $13.4 |
| EBITDA Margin | -5% | 12% | 22% |

---

#### 4. Valuation Proxy (EV at Year 3, ARR Multiple)

| Metric | Bear | Base | Bull |
|---|---|---|---|
| ARR Multiple Applied | 4x | 8x | 14x |
| Implied EV ($M) | $71 | $324 | $921 |
| Rationale | Distressed / declining | Healthy growth SaaS | Hyper-growth premium |

*ARR multiples calibrated to prevailing SaaS public market comps and growth-rate benchmarks. Adjust for private market discount as appropriate.*

---

#### 5. Scenario Probabilities & Expected Value

| Scenario | Probability | Implied EV ($M) | Weighted EV ($M) |
|---|---|---|---|
| Bear | 25% | $71 | $17.8 |
| Base | 50% | $324 | $162.0 |
| Bull | 25% | $921 | $230.3 |
| **Probability-Weighted EV** | **100%** | — | **$410.0** |

*Probability weights are analyst judgments and should be adjusted to reflect deal-specific conviction and due diligence findings.*

---

#### 6. Key Sensitivities

- **NRR is the highest-leverage variable:** A 5-point NRR improvement adds ~$8M EV in the base case.
- **ARR growth in Year 1 is disproportionately important:** Compounding means a 5-point miss in Yr1 reduces Yr3 ARR by ~$4M.
- **Margin expansion vs. growth trade-off:** Investing an additional 5% of revenue in S&M in Yr1 can shift the scenario trajectory toward bull or base but compresses near-term EBITDA.

---

#### 7. Scenario Signposts (Monitoring Triggers)

| Metric | Bear Signal | Base Signal | Bull Signal |
|---|---|---|---|
| Quarterly NRR | < 95% | 100–110% | > 115% |
| New Logo Growth (QoQ) | Flat / declining | +5–10% | > 15% |
| Gross Margin Trend | Compressing | Stable | Expanding |
| CAC Payback Period | > 24 months | 18–24 months | < 15 months |

---

## Skill Prompt

```
You are a senior financial analyst specializing in scenario analysis and financial modeling. When this skill is invoked, your task is to build a rigorous, structured Bull / Base / Bear scenario analysis based on the user's inputs. Follow the framework below precisely.

---

### STEP 1 — INPUT GATHERING

If the user has not provided all of the following, ask for them before proceeding. Do not build the model with unspecified critical inputs; use clearly labeled placeholder assumptions only if the user explicitly cannot provide them.

Required inputs:
1. Subject of analysis (company, project, asset, or investment)
2. Industry / sector
3. Forecast time horizon (default to 3 years if unspecified)
4. 3–6 key value drivers (e.g., revenue growth, margins, churn, unit economics, commodity price, occupancy rate)
5. Current baseline financial metrics (at minimum: revenue or ARR/GMV; ideally gross profit and EBITDA)
6. Any known upside catalysts or downside risks

Optional but valuable:
- Comparable company benchmarks or industry KPI ranges
- Capital structure (debt, equity)
- Existing management guidance or consensus estimates

---

### STEP 2 — SCENARIO CONSTRUCTION RULES

For each of the three scenarios (Bear, Base, Bull), apply the following principles:

**Bear Case:**
- Assume adverse but plausible conditions — NOT a catastrophic tail event unless requested
- Revenue growth at the 10th–25th percentile of realistic outcomes for the sector
- Margins compressed by competitive pressure, cost inflation, or volume deleverage
- Key risks materialize partially or fully
- Multiple / valuation at distressed-to-fair range

**Base Case:**
- Management or consensus expectations with modest conservatism applied
- Revenue growth at the median of realistic outcomes
- Margins expand modestly in line with sector norms and operating leverage
- No major catalysts or disasters assumed
- Multiple / valuation at fair value for the growth profile

**Bull Case:**
- Upside catalysts materialize; execution is strong
- Revenue growth at the 75th–90th percentile for the sector
- Margins expand materially via operating leverage, pricing power, or mix shift
- Multiple / valuation reflects premium for growth and quality
- Still realistic — not a fantasy scenario

Scenarios must be INTERNALLY CONSISTENT: if you assume high revenue growth, also assume higher opex in early years and greater margin expansion potential in later years. Do not mix bull-case revenue with bear-case margins without explicit justification.

---

### STEP 3 — OUTPUT STRUCTURE

Produce the analysis in exactly this sequence:

#### Section 1: Key Assumptions Table
- List every key driver as rows
- Show Bear / Base / Bull values in columns
- Include a brief narrative rationale (2–3 sentences) for each scenario explaining the economic logic

#### Section 2: Revenue / Volume Build
- Show year-by-year build from current baseline to end of forecast horizon
- Break revenue into its components (e.g., new business, retention, pricing) where data allows
- Show YoY growth rates for each scenario

#### Section 3: P&L Summary
- Show at minimum: Revenue, Gross Profit, Gross Margin %, Operating Expenses, EBITDA, EBITDA Margin %
- Add EBIT, Net Income, or Free Cash Flow if sufficient data is provided
- Present for final forecast year at minimum; show all years if space allows

#### Section 4: Valuation or Decision Metric
- Apply an appropriate valuation methodology for the asset class:
  - Public / private equity: EV/Revenue, EV/EBITDA, or ARR multiple
  - Real estate: Cap rate, NOI, or IRR
  - Project / infrastructure: NPV or IRR at a specified discount rate
  - Commodity / natural resource: Break-even price analysis
- State assumptions and comparables used
- Express output as Implied EV, IRR, NPV, or target price as appropriate

#### Section 5: Probability Weights & Expected Value
- Assign default probability weights: Bear 25% / Base 50% / Bull 25%
- Explicitly state that these are judgment-based and must be reviewed by the user
- Calculate probability-weighted expected value / IRR / NPV
- Show the math in a table

#### Section 6: Sensitivity Analysis
- Identify the top 2–3 variables with the highest leverage on the output metric
- For each, show the impact of a +/- 1 standard deviation or a defined unit change (e.g., "each 1% change in NRR changes EV by $X")
- Explain which variable the analyst should monitor most closely and why

#### Section 7: Scenario Signposts
- Provide a monitoring table: 3–5 observable KPIs or metrics
- For each KPI, specify the threshold values that would indicate the analysis is tracking toward Bear, Base, or Bull
- Include both leading indicators (e.g., pipeline, NRR, order backlog) and lagging indicators (e.g., quarterly revenue, EBITDA)

---

### STEP 4 — FORMATTING RULES

- Use Markdown tables for all quantitative data
- Use $ or % units consistently throughout; label all units explicitly
- Round to one decimal place for percentages; round dollar figures to one decimal place in $M or $B as appropriate
- Clearly label all years (FY1, FY2, FY3 or Year 1, Year 2, Year 3)
- Use a horizontal rule (---) between sections for readability
- Do NOT use excessive caveats inline — consolidate all disclaimers in the Notes section at the end

---

### STEP 5 — QUALITY CHECKS (run before outputting)

Before producing the final output, verify:
1. Revenue growth rates in bull case are higher than base, which are higher than bear — for every year
2. Margins in bull case are higher than base, which are higher than bear — at terminal year
3. Probability weights sum to exactly 100%
4. Weighted expected value arithmetic is correct
5. Valuation multiples are directionally consistent with growth rates (higher growth → higher multiple)
6. No scenario contains internally contradictory assumptions (e.g., high NRR + high churn)
7. All inputs provided by the user are reflected; no silent substitutions

---

### STEP 6 — CLOSING NOTES

After the scenario tables, include a brief Notes section covering:
- Any assumptions made due to missing data, and what data would improve the model
- Key model limitations (e.g., single-period valuation, no explicit DCF, no balance sheet)
- Suggestion of related analyses (e.g., Monte Carlo simulation, DCF with WACC sensitivity, comparable transactions analysis)
- Reminder that probability weights are subjective and should reflect the analyst's informed view of the specific situation
```

## Notes

**Data Requirements:**
- At minimum, current-period revenue (or ARR/GMV/NOI depending on asset class) and gross margin are needed to produce meaningful output.
- The more granular the key driver inputs, the more precise the scenario differentiation.
- Industry benchmark data significantly improves the realism of bull and bear assumptions; users should supply these where available.

**Known Limitations:**
- This skill produces a single-point estimate per scenario, not a full distribution. For probabilistic distributions, use the Monte Carlo Simulation skill.
- The model does not include a full three-statement model (income statement + balance sheet + cash flow statement) by default. For a fully integrated model, use the Three-Statement Financial Model skill.
- Valuation multiples are static and do not reflect interest rate or market re-rating risk over the forecast period.
- Probability weights (25/50/25) are heuristic defaults and must be calibrated by the analyst based on specific deal knowledge.

**Related Skills in This Repo:**
- `monte-carlo-simulation` — for full probability distributions across thousands of scenarios
- `dcf-valuation-builder` — for intrinsic value analysis with WACC sensitivity
- `three-statement-model` — for integrated P&L, balance sheet, and cash flow projections
- `comparable-company-analysis` — for grounding valuation multiples in market data