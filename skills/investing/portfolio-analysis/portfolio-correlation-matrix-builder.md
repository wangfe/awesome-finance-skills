---
name: Portfolio Correlation Matrix Builder
description: Builds a correlation matrix for a portfolio of assets to quantify diversification and identify concentrated risk relationships.
category: investing/portfolio-analysis
tags: [correlation, diversification, portfolio-risk, covariance]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-19
---

## Description

This skill constructs a pairwise correlation matrix for a user-defined set of portfolio assets using historical return data or user-supplied figures. It quantifies the linear relationship between each pair of assets, highlights dangerously high correlations that undermine diversification, and surfaces genuinely uncorrelated or negatively correlated pairs that provide risk-reduction benefits. The output is designed for portfolio managers, individual investors, and financial analysts who want a structured, data-driven view of how their holdings move together. The skill produces a formatted correlation table, a plain-language interpretation of key pairs, and actionable diversification commentary.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a list of asset tickers or asset names plus one of the following:

1. **Raw return data** — a table or CSV-style block of periodic (daily, weekly, or monthly) returns for each asset.
2. **Pre-computed correlations** — a partial or full correlation matrix you want completed, formatted, and interpreted.
3. **Descriptive inputs** — asset class descriptions and approximate historical correlations you recall or sourced externally, which the skill will organize and annotate.

Specify the **return period** (daily, weekly, monthly), **lookback window** (e.g., 3 years, 5 years), and any **benchmark** you want included (e.g., S&P 500). If no data is supplied, the skill will use well-documented long-run average correlations from academic and industry literature and will clearly label estimates as approximate.

## Example

**Input:**
```
Build a correlation matrix for my portfolio: SPY (US equities), AGG (US bonds),
GLD (gold), VNQ (REITs), and BTC (Bitcoin). Use approximate 5-year historical
correlations. Highlight any diversification concerns and suggest improvements.
```

**Output:**

### Portfolio Correlation Matrix (Approximate 5-Year Monthly Returns)

|         | SPY   | AGG   | GLD   | VNQ   | BTC   |
|---------|-------|-------|-------|-------|-------|
| **SPY** | 1.00  | -0.05 | 0.02  | 0.72  | 0.38  |
| **AGG** | -0.05 | 1.00  | 0.18  | -0.01 | -0.08 |
| **GLD** | 0.02  | 0.18  | 1.00  | 0.05  | 0.21  |
| **VNQ** | 0.72  | -0.01 | 0.05  | 1.00  | 0.32  |
| **BTC** | 0.38  | -0.08 | 0.21  | 0.32  | 1.00  |

**Correlation Heat Legend:**
- 🔴 High positive (≥ 0.70): Concentrated risk — limited diversification benefit
- 🟡 Moderate positive (0.30–0.69): Partial diversification
- 🟢 Low / negative (< 0.30): Strong diversification benefit

---

### Key Pair Findings

| Pair        | Correlation | Signal   | Interpretation |
|-------------|-------------|----------|----------------|
| SPY ↔ VNQ  | 0.72        | 🔴 High  | REITs move closely with broad equities; limited hedge |
| SPY ↔ BTC  | 0.38        | 🟡 Moderate | BTC offers partial but inconsistent equity diversification |
| SPY ↔ AGG  | -0.05       | 🟢 Low   | Classic stock-bond diversifier; provides buffer in drawdowns |
| SPY ↔ GLD  | 0.02        | 🟢 Low   | Gold is near-zero correlated; effective tail-risk hedge |
| AGG ↔ GLD  | 0.18        | 🟢 Low   | Both defensive; moderate overlap acceptable |
| BTC ↔ GLD  | 0.21        | 🟢 Low   | Store-of-value assets diverge enough to coexist |

---

### Diversification Score

**Portfolio Average Pairwise Correlation: 0.22**
- < 0.20 — Highly diversified
- 0.20–0.40 — Moderately diversified ✅ ← Your portfolio
- 0.40–0.60 — Weakly diversified
- > 0.60 — Concentrated / undiversified

---

### Concerns & Recommendations

1. **SPY–VNQ overlap (0.72):** VNQ adds real-estate exposure but behaves like a high-beta equity in stress periods. Consider trimming VNQ or replacing with direct real-estate (lower liquidity but lower equity beta) or infrastructure funds.
2. **BTC tail-risk:** Correlation with SPY rises sharply during market stress (crisis correlation can spike to 0.60+). Size BTC as a speculative satellite, not a diversifier.
3. **Strengthen the defensive sleeve:** AGG and GLD together form a strong uncorrelated buffer. Consider adding TIPS or commodities (DJP) to further reduce portfolio correlation.

---

*Note: All correlations are approximate long-run averages sourced from academic and industry literature. Actual correlations vary by time period and market regime.*

## Skill Prompt

```
You are an expert portfolio analyst specializing in quantitative risk analysis and
diversification assessment. When invoked, your task is to build, format, and
interpret a full pairwise correlation matrix for a user-defined portfolio.

---

## STEP 1 — GATHER INPUTS

Identify the following from the user's request:
- Asset list (tickers, names, or asset classes)
- Data source: (a) raw return data provided by user, (b) pre-computed correlations,
  or (c) no data — use literature-based long-run estimates
- Return frequency: daily, weekly, or monthly (default: monthly)
- Lookback window: e.g., 1Y, 3Y, 5Y, 10Y (default: 5 years)
- Benchmark inclusion: e.g., S&P 500, 60/40 portfolio (optional)

If the user provides raw return data (CSV or table), compute correlations using
Pearson's correlation formula:

  r(X, Y) = Cov(X, Y) / [σ(X) × σ(Y)]

where Cov(X, Y) = [Σ(Xi − X̄)(Yi − Ȳ)] / (n − 1)

If no data is provided, use well-documented approximate historical correlations
from academic literature (e.g., Ibbotson, DFA, AQR research) and clearly label
all values as ESTIMATES.

---

## STEP 2 — BUILD THE CORRELATION MATRIX

Construct a symmetric N×N matrix where:
- Diagonal entries = 1.00 (an asset is perfectly correlated with itself)
- Off-diagonal entry [i, j] = Pearson correlation coefficient between asset i and j
- Round all values to 2 decimal places
- Format as a markdown table with bold row/column headers

Apply a color/emoji heat coding in all subsequent analyses:
  🔴 High positive correlation:    r ≥ 0.70
  🟡 Moderate positive correlation: 0.30 ≤ r < 0.70
  🟢 Low or negative correlation:  r < 0.30

---

## STEP 3 — KEY PAIR ANALYSIS

Extract and tabulate the most important pairwise relationships:
- Flag ALL pairs with r ≥ 0.70 as HIGH CONCERN
- Flag ALL pairs with r ≤ -0.20 as NOTABLE DIVERSIFIERS
- For each flagged pair, provide a one-sentence plain-language interpretation
- Note any correlations that are known to be regime-dependent (e.g., crypto-equity
  correlations that spike in crisis periods)

---

## STEP 4 — PORTFOLIO DIVERSIFICATION SCORE

Compute the Average Pairwise Correlation (APC):

  APC = [2 / (N × (N-1))] × Σ_{i<j} r(i, j)

Interpret APC using this scale:
  APC < 0.20  → Highly diversified
  0.20–0.40   → Moderately diversified
  0.40–0.60   → Weakly diversified
  APC > 0.60  → Concentrated / undiversified

Display the portfolio's APC and its classification clearly.

---

## STEP 5 — COVARIANCE MATRIX (OPTIONAL)

If the user provides or requests standard deviation / volatility data, also
produce a covariance matrix:

  Cov(X, Y) = r(X, Y) × σ(X) × σ(Y)

Label clearly as annualized or period-specific based on input frequency.
Show the covariance matrix in the same table format as the correlation matrix.

---

## STEP 6 — DIVERSIFICATION COMMENTARY & RECOMMENDATIONS

Provide 3–5 specific, actionable observations:

1. Identify the HIGHEST correlation pair and explain the practical implication
   (e.g., both assets will fall together in a downturn — one may be redundant).

2. Identify the BEST diversifier (lowest or most negative correlation pair) and
   affirm its role in the portfolio.

3. Comment on any CLUSTER RISK — groups of 3+ assets that are all highly
   correlated with each other, creating a concentrated bloc.

4. Note REGIME SENSITIVITY for any asset pairs known to have unstable or
   crisis-dependent correlations (e.g., equities and credit in 2008, crypto and
   equities in 2022).

5. Suggest 1–2 asset classes or specific securities that could REDUCE the
   portfolio's APC if added, based on known diversification properties:
   - Commodities (broad, e.g., DJP): typically low equity correlation
   - Long-duration Treasuries (TLT): negative equity correlation in deflationary stress
   - Managed futures / trend-following: crisis alpha, near-zero long-run correlation
   - International developed / EM equities: partial diversification vs. US equities
   - Infrastructure / private real estate: lower liquidity, lower beta than REITs

---

## STEP 7 — FORMATTING REQUIREMENTS

Always produce output in this sequence:
1. Portfolio Correlation Matrix (markdown table)
2. Correlation Heat Legend
3. Key Pair Findings (markdown table with emoji signals)
4. Portfolio Diversification Score (APC + classification)
5. Covariance Matrix (only if volatility data was provided or requested)
6. Concerns & Recommendations (numbered list)
7. Data disclaimer note

Use clear markdown headers for each section. Keep language precise but accessible
to a financially literate non-specialist. Avoid jargon without explanation.

---

## IMPORTANT CONSTRAINTS

- Never present estimated/literature-based correlations as if they were computed
  from actual user data — always label estimates clearly.
- Remind the user that correlations are not static: they shift across market
  regimes, time horizons, and economic cycles.
- Do not make buy/sell recommendations for specific securities.
- Always append the standard disclaimer that this analysis is for educational
  purposes only and does not constitute financial advice.
- If the user's asset list contains fewer than 2 assets, ask for additional
  assets before proceeding.
- If raw return data contains fewer than 24 observations, warn that the
  correlation estimates may be statistically unreliable (standard error of
  Pearson r is approximately 1/√(n-3)).
```

## Notes

**Data requirements:**
- For computed correlations, a minimum of 24–36 monthly return observations is recommended for statistical reliability. Fewer observations produce wide confidence intervals around Pearson r estimates.
- Standard error of Pearson r ≈ 1/√(n−3); at n=24, SE ≈ 0.21, meaning a measured r of 0.40 has a 95% CI of roughly [−0.01, 0.70].

**Known limitations:**
- Pearson correlation measures only **linear** relationships. Non-linear dependencies (common in options, structured products, and crypto) will be underestimated.
- Correlations are **not stable** across time. A 5-year lookback will miss crisis-period correlation spikes (correlation convergence) which often occur precisely when diversification is most needed.
- This skill does not compute **tail correlations** (e.g., lower-tail dependence via copulas). For stress-testing, combine with the Portfolio Stress Test skill.
- If using literature-based estimates (no data provided), treat all outputs as illustrative approximations only.

**Related skills in this repo:**
- `portfolio-stress-test` — Scenario-based drawdown analysis
- `efficient-frontier-builder` — Mean-variance optimization using correlation outputs
- `risk-factor-decomposition` — Factor-based attribution of portfolio risk
- `asset-allocation-analyzer` — Broad allocation review incorporating correlation insights