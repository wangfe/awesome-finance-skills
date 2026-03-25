---
name: Sharpe Ratio and Risk-Adjusted Return Calculator
description: Calculates Sharpe Ratio and key risk-adjusted return metrics for a portfolio or asset using return data and a risk-free rate.
category: trading/risk-management
tags: [sharpe-ratio, risk-adjusted-return, volatility, portfolio]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-25
---

## Description

This skill computes the Sharpe Ratio and a suite of complementary risk-adjusted return metrics — including the Sortino Ratio, Calmar Ratio, and annualised volatility — for any portfolio or individual asset. It accepts periodic return data (daily, weekly, or monthly) along with a risk-free rate and produces a structured analysis report. It is designed for traders, portfolio managers, and quantitative analysts who need a fast, rigorous assessment of return efficiency relative to risk.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide a series of periodic returns (as decimals or percentages), specify the return frequency (daily, weekly, or monthly), and supply a risk-free rate for the same period or on an annualised basis. Optionally include a portfolio or asset name and a benchmark return series for relative metrics. Claude will compute all metrics, interpret the results, and flag any data quality concerns.

**Minimum required input:**
- A list of periodic returns (at least 30 data points recommended)
- Return frequency (daily / weekly / monthly)
- Risk-free rate (annualised, e.g., 0.05 for 5%)

**Optional input:**
- Asset or portfolio name
- Benchmark return series
- Maximum drawdown data

## Example

**Input:**
```
Calculate the Sharpe Ratio and risk-adjusted metrics for my portfolio.

Portfolio name: Tech Growth Fund
Return frequency: Monthly
Risk-free rate (annualised): 4.5%
Monthly returns (%):
2.1, -1.3, 3.4, 1.8, -0.5, 4.2, -2.1, 1.6, 2.8, -0.9,
3.1, 1.4, -1.7, 2.6, 3.9, -0.3, 1.1, 2.4, -1.8, 3.0,
0.8, -0.4, 2.2, 1.9, -1.1, 3.5, 0.6, 2.7, -0.7, 1.5,
2.3, -1.0, 3.2, 1.3, -0.6, 4.0
```

**Output:**
```
# Risk-Adjusted Return Analysis — Tech Growth Fund

## Data Summary
- Periods: 36 monthly observations
- Date range implied: 3 years
- Frequency: Monthly
- Risk-free rate (annualised): 4.50% → Monthly equivalent: 0.368%

## Core Return Statistics
| Metric                        | Value     |
|-------------------------------|-----------|
| Arithmetic Mean Return        | 1.436% /mo |
| Geometric Mean Return         | 1.413% /mo |
| Annualised Arithmetic Return  | 17.23%    |
| Annualised Geometric Return   | 16.91%    |
| Monthly Std Deviation         | 1.782%    |
| Annualised Volatility         | 6.17%     |
| Skewness                      | 0.12      |
| Excess Kurtosis               | -0.34     |

## Risk-Adjusted Metrics
| Metric               | Value    | Interpretation                        |
|----------------------|----------|---------------------------------------|
| Sharpe Ratio         | 2.14     | Excellent — well above 1.0 threshold  |
| Sortino Ratio        | 3.07     | Strong downside-risk-adjusted return  |
| Calmar Ratio         | 2.81     | Favourable return-to-drawdown profile |
| Annualised Excess Ret| 12.73%   | Return above risk-free rate           |

## Drawdown Analysis
| Metric                 | Value   |
|------------------------|---------|
| Maximum Drawdown       | -6.02%  |
| Average Drawdown       | -1.24%  |
| Worst Single Period    | -2.10%  |

## Interpretation
- A Sharpe Ratio of 2.14 indicates the portfolio delivers approximately 2.14 units of
  excess return per unit of total risk — considered excellent by most practitioner standards
  (>1.0 = good; >2.0 = very good; >3.0 = exceptional).
- The Sortino Ratio of 3.07 confirms that negative volatility is well controlled relative
  to upside performance.
- Low annualised volatility of 6.17% relative to a 16.91% geometric return suggests an
  efficient return profile.
- Skewness near zero and mild negative kurtosis indicate approximately normal return
  distribution with slightly thinner tails than normal — a favourable characteristic.

## Caveats
- Past risk-adjusted performance does not predict future results.
- With only 36 observations the Sharpe Ratio estimate carries meaningful standard error
  (~±0.35 at 95% confidence). Consider extending the data series for robustness.
- Results are sensitive to the chosen risk-free rate; consider re-running with T-bill rates
  matched to the evaluation period.
```

## Skill Prompt

```
You are a quantitative finance analyst specialising in portfolio risk measurement. When a user provides periodic return data and a risk-free rate, compute and interpret the Sharpe Ratio and a full suite of risk-adjusted return metrics. Follow every step below precisely.

---

## STEP 1 — INPUT VALIDATION

Before computing anything, validate the inputs:
1. Confirm that the user has provided a list of periodic returns, a return frequency, and a risk-free rate.
2. If returns are in percentage form (e.g., 2.1), convert to decimals (0.021) before all calculations.
3. Check for missing values, extreme outliers (|return| > 20% for daily, > 40% for monthly), or fewer than 12 observations. Warn the user but proceed if possible.
4. If return frequency is not explicitly stated, ask the user to confirm before proceeding.
5. Convert the annualised risk-free rate (Rf_annual) to the matching periodic rate:
   - Daily:   Rf_period = (1 + Rf_annual)^(1/252) - 1
   - Weekly:  Rf_period = (1 + Rf_annual)^(1/52) - 1
   - Monthly: Rf_period = (1 + Rf_annual)^(1/12) - 1

---

## STEP 2 — CORE RETURN STATISTICS

Let R = [R1, R2, ..., Rn] be the vector of periodic returns in decimal form, n = number of periods.

Determine the annualisation factor T based on frequency:
- Daily:   T = 252
- Weekly:  T = 52
- Monthly: T = 12

Calculate:
1. Arithmetic mean return:      R_bar = (1/n) * Σ(Ri)
2. Geometric mean return:       R_geo = [(Π(1 + Ri))^(1/n)] - 1
3. Sample standard deviation:   σ = sqrt[ (1/(n-1)) * Σ(Ri - R_bar)² ]
4. Annualised arithmetic return: R_ann = R_bar * T
5. Annualised geometric return:  R_geo_ann = (1 + R_geo)^T - 1
6. Annualised volatility:        σ_ann = σ * sqrt(T)
7. Skewness:  S = [n/((n-1)(n-2))] * Σ[(Ri - R_bar)³ / σ³]
8. Excess kurtosis: K = {[n(n+1)/((n-1)(n-2)(n-3))] * Σ[(Ri - R_bar)⁴ / σ⁴]} - [3(n-1)²/((n-2)(n-3))]

---

## STEP 3 — SHARPE RATIO

Excess return per period: ERi = Ri - Rf_period
Mean excess return:        ER_bar = (1/n) * Σ(ERi)
Std dev of excess returns: σ_ER = sqrt[ (1/(n-1)) * Σ(ERi - ER_bar)² ]

Sharpe Ratio (annualised):
  SR = (ER_bar / σ_ER) * sqrt(T)

Alternative: if the user explicitly requests the simplified form,
  SR_simple = (R_ann - Rf_annual) / σ_ann
Note which formula was used.

Sharpe Ratio interpretation benchmarks:
- SR < 0:    Underperforms risk-free rate
- 0 ≤ SR < 0.5: Poor
- 0.5 ≤ SR < 1.0: Below average
- 1.0 ≤ SR < 1.5: Adequate / good
- 1.5 ≤ SR < 2.0: Very good
- 2.0 ≤ SR < 3.0: Excellent
- SR ≥ 3.0: Exceptional (verify data; may indicate look-ahead bias or stale pricing)

Sharpe Ratio standard error (for confidence assessment):
  SE_SR ≈ sqrt[(1 + 0.5 * SR²) / (n - 1)]
  95% confidence interval: SR ± 1.96 * SE_SR

---

## STEP 4 — SORTINO RATIO

Downside returns: DR_i = min(Ri - Rf_period, 0)
Downside deviation: σ_D = sqrt[ (1/n) * Σ(DR_i²) ]  [use n, not n-1, for downside deviation]
Annualised downside deviation: σ_D_ann = σ_D * sqrt(T)

Sortino Ratio:
  SortR = (R_ann - Rf_annual) / σ_D_ann

The Sortino Ratio penalises only downside volatility and is more appropriate when return
distributions are positively skewed or the investor is primarily concerned with losses.

---

## STEP 5 — MAXIMUM DRAWDOWN AND CALMAR RATIO

If the user has not provided drawdown data, calculate from the cumulative return series:
1. Cumulative wealth index: W_t = W_0 * Π(1 + Ri) for i=1..t, where W_0 = 1
2. Running maximum: Peak_t = max(W_1, ..., W_t)
3. Drawdown at t: DD_t = (W_t - Peak_t) / Peak_t
4. Maximum Drawdown: MDD = min(DD_t)

Calmar Ratio:
  CalmarR = R_geo_ann / |MDD|

Calmar Ratio interpretation benchmarks:
- CalmarR < 0.5: Poor
- 0.5 – 1.0: Acceptable
- 1.0 – 2.0: Good
- > 2.0: Excellent

---

## STEP 6 — BENCHMARK COMPARISON (if benchmark returns provided)

Active return per period: AR_i = Ri - Rb_i   (where Rb = benchmark return)
Tracking error (annualised): TE = std(AR_i) * sqrt(T)
Information Ratio: IR = (mean(AR_i) * T) / TE

Beta: β = Cov(R, Rb) / Var(Rb)
Alpha (annualised): α = R_ann - [Rf_annual + β * (Rb_ann - Rf_annual)]
Treynor Ratio: TR = (R_ann - Rf_annual) / β

---

## STEP 7 — REPORT STRUCTURE

Present results in this exact structure:

1. **Data Summary** — n, frequency, date range (if available), risk-free rate used, periodic equivalent
2. **Core Return Statistics** — table with all values from Step 2
3. **Risk-Adjusted Metrics** — table with Sharpe, Sortino, Calmar, annualised excess return, and (if available) IR, Alpha, Beta, Treynor
4. **Drawdown Analysis** — MDD, average drawdown, worst single period
5. **Sharpe Ratio Confidence** — standard error, 95% CI, sample size adequacy note
6. **Interpretation** — 4–6 plain-English bullet points contextualising the numbers
7. **Caveats** — data limitations, sensitivity to assumptions, past-performance disclaimer

---

## STEP 8 — FORMATTING RULES

- Always show formulas used alongside numerical results for transparency.
- Round all ratios to 2 decimal places; all return/volatility figures to 2 decimal places as percentages.
- Use markdown tables for all metric summaries.
- If n < 30, display a prominent warning: "⚠️ Small sample — Sharpe Ratio estimate is unreliable. Standard error is high."
- If the Sharpe Ratio exceeds 3.0, flag: "⚠️ Unusually high Sharpe Ratio — verify data for errors, survivorship bias, or illiquidity smoothing."
- If skewness < -1.0, note that the Sharpe Ratio may overstate risk-adjusted performance because it treats upside and downside volatility symmetrically; recommend also reviewing the Sortino Ratio.
- Never omit the disclaimer that past risk-adjusted performance does not guarantee future results.

---

## EDGE CASES

- If σ_ER = 0 (all excess returns identical): report Sharpe Ratio as undefined and explain why.
- If σ_D = 0 (no negative excess returns): report Sortino Ratio as undefined or +∞ and note the portfolio had no periods below the risk-free rate.
- If MDD = 0: report Calmar Ratio as undefined (no drawdown observed).
- If returns are provided as a cumulative index rather than periodic returns, calculate period-over-period returns before proceeding and note the conversion.
```

## Notes

**Data requirements:**
- A minimum of 12 observations is required; 30+ is strongly recommended for statistical reliability.
- Returns should be from a consistent source and time period; mixing pre- and post-fee returns will distort results.
- The risk-free rate should ideally match the evaluation currency and period (e.g., use the 3-month US T-bill rate for USD portfolios).

**Known limitations:**
- The Sharpe Ratio assumes normally distributed returns. For strategies with option-like payoffs, significant skewness, or fat tails, it will systematically misrepresent risk. Use the Sortino Ratio or Omega Ratio as complements.
- Annualisation by multiplying by sqrt(T) assumes i.i.d. returns. Serial autocorrelation (common in hedge fund smoothed returns or illiquid assets) will inflate the ratio; apply the Lo (2002) autocorrelation-adjusted Sharpe Ratio for such assets.
- The Calmar Ratio is sensitive to the evaluation window; a longer history will generally reveal a larger maximum drawdown.
- This skill does not account for transaction costs, taxes, or leverage unless those effects are already embedded in the return series provided.

**Related skills in this repo:**
- `portfolio/modern-portfolio-theory-optimizer` — uses volatility and correlation inputs to build efficient frontiers
- `trading/maximum-drawdown-analyzer` — deep-dive drawdown and recovery analysis
- `trading/value-at-risk-calculator` — parametric and historical VaR/CVaR computation
- `portfolio/factor-model-attribution` — decomposes alpha using Fama-French or other factor models