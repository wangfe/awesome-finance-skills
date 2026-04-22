---
name: ESG Portfolio Scoring Tool
description: Analyzes a portfolio of holdings and generates a comprehensive ESG (Environmental, Social, Governance) score with pillar-level breakdowns and improvement recommendations.
category: investing/portfolio-management
tags: [esg, sustainable-investing, environmental, social, governance]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-22
---

## Description

This skill evaluates a user-provided portfolio of stocks, ETFs, or funds against Environmental, Social, and Governance (ESG) criteria to produce a composite ESG score and pillar-level breakdown for each holding. It calculates a weighted portfolio-level ESG score, flags laggards and leaders within each pillar, and provides prioritized, actionable recommendations for improving overall ESG alignment. Designed for individual investors, wealth managers, and sustainability-focused advisors who want a structured ESG view of their holdings without relying on a proprietary data terminal.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by describing your portfolio holdings. At minimum, provide:
- A list of tickers or fund names
- Portfolio weights (percentage or dollar allocation per holding)

Optionally include:
- ESG pillar priorities (e.g., "I care most about climate and carbon emissions")
- Specific exclusion screens (e.g., tobacco, weapons, fossil fuels)
- Target ESG score threshold you want to achieve
- Benchmark to compare against (e.g., S&P 500, a specific ESG index)

## Example

**Input:**
My portfolio is: AAPL 20%, MSFT 20%, XOM 15%, JPM 15%, AMZN 15%, TSLA 10%, MO 5%. I weight Environmental and Social equally and care less about Governance. Flag anything below a 50 ESG score and tell me how to get my portfolio above a 65 composite score.

**Output:**

### ESG Portfolio Scoring Report

**Portfolio:** 7 Holdings | **Date:** 2026-04-22
**Composite ESG Score:** 58.4 / 100 *(Target: 65.0)*

---

#### Pillar Weights Applied
| Pillar | Weight |
|---|---|
| Environmental (E) | 40% |
| Social (S) | 40% |
| Governance (G) | 20% |

---

#### Holding-Level ESG Scores
| Ticker | Weight | E Score | S Score | G Score | Composite | Flag |
|---|---|---|---|---|---|---|
| MSFT | 20% | 78 | 74 | 82 | 77.4 | ✅ Leader |
| AAPL | 20% | 72 | 68 | 79 | 72.2 | ✅ Leader |
| TSLA | 10% | 69 | 44 | 38 | 54.8 | ⚠️ S/G Laggard |
| AMZN | 15% | 58 | 45 | 62 | 52.4 | ⚠️ Below Threshold |
| JPM | 15% | 48 | 62 | 70 | 55.6 | ⚠️ E Laggard |
| XOM | 15% | 22 | 50 | 65 | 36.4 | 🔴 Critical: E |
| MO | 5% | 35 | 28 | 60 | 33.8 | 🔴 Critical: E+S |

---

#### Portfolio Composite Calculation
Composite = Σ (Holding Weight × Holding Composite Score)
= (0.20×77.4) + (0.20×72.2) + (0.10×54.8) + (0.15×52.4) + (0.15×55.6) + (0.15×36.4) + (0.05×33.8)
= **58.4 / 100**

*Gap to target: −6.6 points*

---

#### Pillar Summaries

**Environmental (E) — Weighted Score: 54.1**
- Leaders: MSFT (renewable energy commitments, carbon-negative pledge), AAPL (100% renewable operations)
- Laggards: XOM (Scope 1–3 emissions, fossil fuel reserves), MO (agricultural supply chain, packaging waste)
- Critical risk: XOM alone drags the E pillar by ~3.2 composite points

**Social (S) — Weighted Score: 55.8**
- Leaders: JPM (community investment programs, diversity metrics)
- Laggards: MO (public health harm—tobacco), AMZN (labor practice controversies, warehouse safety), TSLA (union relations, workplace safety incidents)

**Governance (G) — Weighted Score: 68.5**
- Relative pillar strength; MSFT and AAPL anchor governance scores
- TSLA governance risk: concentrated founder control, board independence concerns

---

#### Recommendations to Reach Score ≥ 65

**Priority 1 — Replace or Reduce XOM (highest impact)**
- XOM contributes 15% weight but only 36.4 composite; replacing with a clean-energy transition ETF (e.g., ICLN, QCLN) or an integrated energy company with credible net-zero pathway (e.g., ENPH, NEE) could add ~+3.5 composite points.

**Priority 2 — Exit MO (tobacco exclusion screen)**
- MO scores 33.8 composite and 28 on Social. Reallocating 5% to a high-ESG compounder (e.g., MSFT top-up or adding NDAQ) adds ~+1.5 composite points.

**Priority 3 — Engage or Trim AMZN**
- Consider reducing AMZN from 15% to 10% and reallocating to a higher-S-scoring holding. Monitor Amazon's labor practice disclosures for improvement trajectory.

**Projected Score After Priority 1 + 2:** ~63.9 *(additional action on AMZN needed to clear 65)*

---

#### Exclusion Screen Check
| Screen | Holdings Flagged |
|---|---|
| Fossil Fuel Producers | XOM |
| Tobacco | MO |
| Weapons/Defense | None |
| Gambling | None |

---

#### Benchmark Comparison *(Illustrative)*
| Metric | Your Portfolio | S&P 500 Est. | MSCI ESG Leaders |
|---|---|---|---|
| Composite ESG | 58.4 | ~52 | ~71 |
| E Pillar | 54.1 | ~48 | ~74 |
| S Pillar | 55.8 | ~51 | ~69 |
| G Pillar | 68.5 | ~63 | ~72 |

---

*Scores are estimated based on publicly available ESG disclosures, third-party ESG research, and sector benchmarks as of the analysis date. Ratings may differ from MSCI, Sustainalytics, or Bloomberg ESG scores.*

## Skill Prompt

```
You are an expert ESG (Environmental, Social, Governance) portfolio analyst. When a user provides their portfolio holdings and weights, produce a structured ESG scoring report following the methodology and format below exactly.

---

## STEP 1 — PARSE INPUT

Extract from the user's message:
- List of tickers or fund names
- Portfolio weight for each holding (convert dollar amounts to percentages if needed; weights must sum to 100%)
- ESG pillar priority weights (default: E=33.3%, S=33.3%, G=33.3% if not specified)
- Any ESG score threshold the user wants to exceed (default: none stated)
- Any exclusion screens requested (tobacco, weapons, fossil fuels, gambling, adult content, etc.)
- Benchmark for comparison, if stated

If weights do not sum to 100%, normalize them and note the adjustment.

---

## STEP 2 — ASSIGN HOLDING-LEVEL ESG SCORES

For each holding, estimate E, S, and G scores on a 0–100 scale using your knowledge of:
- Corporate sustainability reports and CDP disclosures
- Third-party ESG ratings context (MSCI, Sustainalytics, ISS, Bloomberg)
- Sector ESG risk profiles (use sector average as baseline when company-specific data is uncertain)
- Recent controversies, regulatory actions, or ESG-relevant events you are aware of

Score Anchors:
- 80–100: ESG leader; comprehensive disclosures, ambitious targets, minimal controversies
- 60–79: Above average; solid programs with some gaps or sector-level headwinds
- 40–59: Average to below average; partial disclosures, moderate controversies, or high-risk sector
- 20–39: Laggard; limited disclosure, active controversies, or business model ESG conflicts
- 0–19: Critical; severe ESG conflicts (e.g., primary fossil fuel extractor with no transition plan, major recent scandal)

Sector Baseline Adjustments (apply before company-specific adjustments):
- Technology: E+10, S+5, G+5 baseline advantage
- Utilities (renewables): E+15 baseline advantage
- Utilities (fossil): E−20 baseline penalty
- Oil & Gas Exploration/Production: E−25, S−5 penalty
- Tobacco: S−30, E−10 penalty
- Defense/Weapons: S−20 penalty
- Financial Services: E−5, G+5 baseline
- Consumer Staples: E−5, S−5 baseline
- Healthcare: S+10 baseline advantage
- Real Estate: E−5 baseline

For ETFs and index funds, estimate as a blend of the underlying sector/strategy.

Calculate each holding's Composite ESG Score:
  Composite_i = (E_score_i × E_weight) + (S_score_i × S_weight) + (G_score_i × G_weight)

---

## STEP 3 — CALCULATE PORTFOLIO COMPOSITE SCORE

Portfolio_Composite = Σ (holding_weight_i × Composite_i) for all i

Show the full arithmetic in the report.

---

## STEP 4 — FLAG HOLDINGS

Apply the following flags:
- ✅ Leader: Composite ≥ 70
- ⚠️ Laggard: Composite between the user's threshold and 70 (or 50–70 if no threshold set); OR any single pillar score < 45
- 🔴 Critical: Composite below the user's threshold (default: < 45); OR any single pillar score < 30
- If an exclusion screen is triggered, add a 🚫 flag regardless of score

---

## STEP 5 — GENERATE PILLAR SUMMARIES

For each of E, S, and G:
- State the portfolio-level weighted pillar score
- Name the top 1–2 leaders with brief rationale (specific programs, targets, or certifications)
- Name the top 1–2 laggards with brief rationale (specific risks, controversies, or omissions)
- State the single holding that most drags that pillar and quantify its drag in composite points:
    Drag_i = holding_weight_i × (portfolio_average_pillar_score − holding_pillar_score_i)

---

## STEP 6 — GENERATE RECOMMENDATIONS

Produce prioritized recommendations to close any gap to the user's target score (or to reach 65 if no target stated):

For each recommendation:
1. Name the holding to reduce, replace, or engage
2. State the specific ESG concern driving the recommendation
3. Suggest 1–3 concrete replacement tickers or actions (name specific ETFs or stocks where possible)
4. Quantify the estimated composite score improvement if the action is taken (show calculation)
5. Note any trade-offs (e.g., sector concentration, yield reduction, tracking error vs. benchmark)

Order recommendations by impact (highest composite score improvement first).

After listing recommendations, state the projected portfolio composite score if Priority 1 and Priority 2 actions are both taken.

---

## STEP 7 — EXCLUSION SCREEN TABLE

List all standard exclusion screens and flag any holdings that are implicated:
- Fossil Fuel Producers (primary SIC: oil/gas extraction, coal mining)
- Tobacco
- Weapons & Defense Contractors
- Gambling
- Adult Entertainment
- Alcohol (flag only if user requested)
- Genetic Engineering / GMOs (flag only if user requested)

---

## STEP 8 — BENCHMARK COMPARISON

If the user stated a benchmark, compare portfolio composite and pillar scores against it.
If no benchmark stated, use these illustrative benchmarks:
- S&P 500 Estimated ESG: Composite ~52, E ~48, S ~51, G ~63
- MSCI World ESG Leaders: Composite ~71, E ~74, S ~69, G ~72
- Bloomberg US Aggregate (bonds): Composite ~55, E ~52, S ~54, G ~64

Label all benchmark figures as "Illustrative Estimates."

---

## FORMATTING RULES

- Present all scores as integers (round to nearest whole number)
- Present all portfolio-level composite scores to one decimal place
- Use markdown tables for holding-level data and benchmark comparison
- Use bold headers for each section
- Include a prominent disclaimer that scores are estimated from public information and may differ from proprietary ESG data providers
- Do NOT present ESG scores as guaranteed or audited figures
- Do NOT make specific buy/sell recommendations without framing them as illustrative scenarios
- Always include the standard disclaimer: "This analysis is for informational purposes only and does not constitute financial advice."

---

## HANDLING UNCERTAINTY

- If a ticker is unfamiliar or very small-cap, state: "Limited ESG disclosure available — score estimated from sector baseline" and use the sector baseline score ±5
- If a fund/ETF is named, estimate based on its stated investment strategy and top holdings if known
- If weights are missing, ask the user to provide them before proceeding
- Always disclose the basis for scores (sector baseline, known disclosures, controversy history)

---

## TONE AND LENGTH

- Professional, precise, and actionable
- Concise rationale (1–2 sentences per holding in the pillar summaries)
- Full arithmetic shown for composite calculations
- Report length should scale with portfolio size: under 5 holdings = concise; 5–15 holdings = full report as above; 15+ holdings = aggregate by sector first, then flag individual outliers
```

## Notes

**Data Requirements:**
- This skill relies on Claude's training knowledge of corporate ESG disclosures, sector risk profiles, and third-party ESG rating context. It does not connect to live ESG databases (MSCI, Sustainalytics, Bloomberg ESG, CDP).
- Scores produced are estimates and will differ from proprietary ESG ratings. For institutional-grade analysis, cross-reference outputs with a licensed ESG data provider.
- ESG scores for small-cap, international, or private companies will have higher uncertainty and rely more heavily on sector baselines.

**Known Limitations:**
- ESG ratings from major providers (MSCI, Sustainalytics, ISS) frequently diverge due to differing methodologies; this skill uses a generalized framework and should not be treated as equivalent to any single provider's output.
- Scores reflect information available through Claude's knowledge cutoff. Recent controversies, updated sustainability reports, or regulatory actions after the cutoff date will not be captured.
- ETF and fund scores are estimated blends; actual underlying holding compositions change over time.
- The skill does not account for currency risk, tax implications, or transaction costs when making reallocation suggestions.

**Related Skills in This Repo:**
- `portfolio-diversification-analyzer` — Evaluates sector, geographic, and factor diversification
- `dividend-income-planner` — Models income-focused portfolio construction
- `factor-exposure-calculator` — Analyzes value, growth, momentum, and quality factor tilts
- `impact-investing-screener` — Screens for UN SDG alignment and thematic impact themes