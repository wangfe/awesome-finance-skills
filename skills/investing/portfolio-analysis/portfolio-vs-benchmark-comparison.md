---
name: Portfolio vs Benchmark Comparison
description: Analyzes a portfolio's performance relative to a chosen benchmark by computing alpha, beta, tracking error, information ratio, and other key risk-adjusted metrics.
category: investing/portfolio-analysis
tags: [benchmark, alpha, beta, tracking-error, information-ratio]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-20
---

## Description

This skill performs a rigorous side-by-side comparison of a user's portfolio against a chosen benchmark index (e.g., S&P 500, MSCI World, Russell 2000). It calculates classic performance attribution and risk metrics — including alpha, beta, tracking error, and the information ratio — to help investors understand whether their portfolio is generating excess returns commensurate with the risk taken. The skill is suitable for individual investors, financial advisors, and students learning portfolio management. Output is a structured analytical report with a plain-language interpretation of each metric.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing:
1. **Portfolio returns** — a series of periodic returns (monthly or annual) for the portfolio, as percentages or decimals.
2. **Benchmark returns** — the corresponding periodic returns for the chosen benchmark over the same period.
3. **Risk-free rate** — an annualized risk-free rate (e.g., 3-month T-bill rate), or a constant to apply across the period.
4. **Optional context** — portfolio name, benchmark name, investment period, and any relevant notes.

Returns can be provided as a comma-separated list, a table, or a brief narrative description with summary statistics.

## Example

**Input:**
```
Portfolio (my US equity fund) monthly returns over 12 months:
2.1, -1.3, 3.4, 1.8, -0.5, 4.2, -2.1, 1.6, 3.0, -0.8, 2.7, 1.9

Benchmark (S&P 500) monthly returns over same period:
1.8, -1.0, 2.9, 1.5, -0.3, 3.8, -1.9, 1.4, 2.6, -0.6, 2.4, 1.7

Risk-free rate: 5.0% annualized (≈ 0.4167% per month)
```

**Output:**

---
### Portfolio vs Benchmark Comparison Report

**Portfolio:** My US Equity Fund  
**Benchmark:** S&P 500  
**Period:** 12 months (monthly data)  
**Risk-Free Rate:** 5.00% p.a. (0.4167% / month)

---

#### 1. Return Summary

| Metric                        | Portfolio  | Benchmark  |
|-------------------------------|------------|------------|
| Cumulative Return             | 18.42%     | 16.08%     |
| Annualized Return             | 18.42%     | 16.08%     |
| Average Monthly Return        | 1.417%     | 1.275%     |
| Monthly Standard Deviation    | 1.973%     | 1.737%     |
| Annualized Volatility         | 6.832%     | 6.016%     |

---

#### 2. Risk-Adjusted Performance Metrics

| Metric                  | Value       | Interpretation                                      |
|-------------------------|-------------|-----------------------------------------------------|
| **Alpha (annualized)**  | +1.86%      | Portfolio generated ~1.86% excess return above what beta alone predicts. |
| **Beta**                | 1.08        | Portfolio moves ~1.08% for every 1% move in the benchmark — slightly more volatile. |
| **R-squared**           | 0.97        | 97% of portfolio variance is explained by benchmark movement. |
| **Tracking Error (ann.)**| 1.24%      | Low tracking error; portfolio closely mirrors the benchmark. |
| **Information Ratio**   | 1.50        | Strong: each unit of active risk delivers 1.50 units of active return. |
| **Sharpe Ratio (Port.)** | 1.76       | Portfolio earns 1.76 units of return per unit of total risk above the risk-free rate. |
| **Sharpe Ratio (Bench.)**| 1.80       | Benchmark Sharpe is marginally higher due to lower volatility. |
| **Treynor Ratio (Port.)**| 0.1148     | Return per unit of systematic (beta) risk. |
| **Up-Capture Ratio**    | 108%        | In up months, portfolio captures 108% of benchmark gains. |
| **Down-Capture Ratio**  | 105%        | In down months, portfolio also captures slightly more losses. |

---

#### 3. Active Return Analysis

| Metric                        | Value   |
|-------------------------------|---------|
| Active Return (ann.)          | +2.34%  |
| Average Monthly Active Return | +0.142% |
| Months Outperforming          | 9 / 12  |

---

#### 4. Interpretation Summary

- **Alpha is positive (+1.86%)**, suggesting skilled stock selection or factor tilts are adding value beyond mere market exposure.
- **Beta of 1.08** indicates the portfolio takes on slightly more market risk than the benchmark. This is modest but worth monitoring in a downturn.
- **Information Ratio of 1.50** is considered strong (>0.5 is generally good; >1.0 is excellent), suggesting the active bets are efficient.
- **Down-capture slightly above 100%** is a caution flag: the portfolio gives back a bit more than the benchmark in falling markets, partially offsetting the alpha.
- **Recommendation:** Consider whether the marginal extra volatility (beta > 1, down-capture > 100%) is acceptable relative to the alpha generated.

---

## Skill Prompt

```
You are a quantitative portfolio analyst. When a user provides portfolio returns, benchmark returns, and a risk-free rate, produce a comprehensive Portfolio vs Benchmark Comparison Report. Follow these exact steps and formulas:

---

### STEP 1 — DATA VALIDATION
- Confirm that portfolio and benchmark return series have identical length.
- Confirm that a risk-free rate is provided; if annualized, convert to the same periodicity as the return data (e.g., monthly rf = (1 + annual_rf)^(1/12) − 1).
- Flag any missing values, obvious outliers, or mismatched periods before proceeding.
- Clarify whether returns are arithmetic (simple) or geometric (log). Assume arithmetic unless stated.

---

### STEP 2 — SUMMARY STATISTICS
For both portfolio (P) and benchmark (B), compute:

a) **Cumulative Return:**
   Cumulative = ∏(1 + r_t) − 1   for t = 1 to N

b) **Annualized Return** (if period ≠ 1 year):
   Annualized = (1 + Cumulative)^(periods_per_year / N) − 1

c) **Average Periodic Return:**
   Mean_r = (1/N) × Σ r_t

d) **Standard Deviation (sample):**
   σ = sqrt[ (1/(N−1)) × Σ(r_t − Mean_r)² ]

e) **Annualized Volatility:**
   σ_ann = σ × sqrt(periods_per_year)
   where periods_per_year = 12 for monthly, 252 for daily, 4 for quarterly, 1 for annual.

---

### STEP 3 — BETA AND ALPHA (Capital Asset Pricing Model basis)

a) **Excess Returns:**
   e_P,t = r_P,t − rf_t
   e_B,t = r_B,t − rf_t

b) **Beta (OLS slope):**
   β = Cov(e_P, e_B) / Var(e_B)
   where Cov and Var use sample formulas (divide by N−1).

c) **Alpha (Jensen's Alpha, periodic):**
   α_periodic = Mean(e_P) − β × Mean(e_B)

d) **Annualized Alpha:**
   α_ann = (1 + α_periodic)^(periods_per_year) − 1
   (For small values, α_ann ≈ α_periodic × periods_per_year is acceptable; note which approximation is used.)

e) **R-squared:**
   R² = [Cov(r_P, r_B) / (σ_P × σ_B)]²
   Interpret: proportion of portfolio variance explained by benchmark.

---

### STEP 4 — TRACKING ERROR AND INFORMATION RATIO

a) **Active Return (each period):**
   AR_t = r_P,t − r_B,t

b) **Mean Active Return:**
   AR_mean = (1/N) × Σ AR_t

c) **Tracking Error (TE, annualized):**
   TE = std_dev(AR_t) × sqrt(periods_per_year)
   where std_dev uses sample standard deviation.

d) **Information Ratio (IR):**
   IR = (AR_mean × periods_per_year) / TE
   Or equivalently: IR = Annualized Active Return / Annualized Tracking Error.
   Interpretation benchmarks:
   - IR > 0.5: Good
   - IR > 0.75: Very Good
   - IR > 1.0: Excellent

---

### STEP 5 — SHARPE AND TREYNOR RATIOS

a) **Sharpe Ratio (annualized):**
   Sharpe = (Annualized Return − Annual Risk-Free Rate) / Annualized Volatility

b) **Treynor Ratio (annualized):**
   Treynor = (Annualized Return − Annual Risk-Free Rate) / β
   (Compute for portfolio only, since benchmark β = 1 by definition.)

c) **M² (Modigliani-Modigliani, optional if data available):**
   M² = Sharpe_P × σ_B_ann + rf_ann
   Interpretation: hypothetical portfolio return if leveraged/de-leveraged to match benchmark volatility.

---

### STEP 6 — CAPTURE RATIOS

a) **Up-Capture Ratio:**
   - Filter periods where r_B,t > 0 (up periods).
   - Up_Capture = [geometric mean of (1 + r_P,t) for up periods − 1] /
                  [geometric mean of (1 + r_B,t) for up periods − 1] × 100
   - >100% means portfolio outperforms benchmark in rising markets.

b) **Down-Capture Ratio:**
   - Filter periods where r_B,t < 0 (down periods).
   - Down_Capture = [geometric mean of (1 + r_P,t) for down periods − 1] /
                    [geometric mean of (1 + r_B,t) for down periods − 1] × 100
   - <100% is desirable (loses less than benchmark in falling markets).

c) **Capture Ratio (Up/Down):**
   Capture_Ratio = Up_Capture / Down_Capture
   >1.0 is favorable.

---

### STEP 7 — ACTIVE RETURN ANALYSIS

- Count and percentage of periods the portfolio outperformed the benchmark.
- Best and worst active return periods.
- Annualized active return.

---

### STEP 8 — ASSEMBLE AND PRESENT THE REPORT

Structure the output as follows:

1. **Header:** Portfolio name, benchmark name, period, data frequency, risk-free rate used.
2. **Return Summary Table:** Cumulative return, annualized return, average periodic return, periodic std dev, annualized volatility — for both portfolio and benchmark.
3. **Risk-Adjusted Performance Table:** Alpha, Beta, R², Tracking Error, Information Ratio, Sharpe (both), Treynor, Up-Capture, Down-Capture — with a brief interpretation column for each.
4. **Active Return Analysis:** Table of annualized active return, average periodic active return, TE, IR, months/periods of outperformance.
5. **Interpretation Summary:** 4–8 bullet points in plain language summarizing the key findings, strengths, weaknesses, and any action considerations.
6. **Caveats section:** Note data limitations (short history, survivorship bias, single-factor model limitations, etc.).

---

### FORMATTING RULES
- Use markdown tables for all numerical results.
- Round percentages to 2 decimal places; ratios to 3–4 decimal places.
- Clearly label all units (%, annualized, per period, etc.).
- If the user provides fewer than 12 data points, warn that statistical reliability is limited.
- If beta is negative, flag this as unusual and suggest verifying data alignment.
- Always include the disclaimer that this is for educational purposes only and not financial advice.

---

### EDGE CASES
- If all benchmark returns are identical (zero variance), note that beta and R² are undefined.
- If there are no down periods in the benchmark, state that down-capture ratio cannot be computed.
- If the risk-free rate exceeds all portfolio returns, Sharpe will be negative — compute and report it accurately; do not truncate to zero.
- If returns appear to be in percentage form (e.g., values like 2.1 rather than 0.021), confirm with the user or state your assumption explicitly before computing.
```

## Notes

**Data Requirements:**
- Minimum recommended: 12 periods (monthly) or 3 years of monthly data for statistically meaningful beta/alpha estimates.
- Ideal: 36–60 monthly observations or 3–5 years of data.
- Returns must be for the same time periods; misaligned dates will distort all metrics.
- The risk-free rate should match the currency and region of the portfolio (e.g., use US T-bill for USD portfolios, EURIBOR for EUR portfolios).

**Known Limitations:**
- This skill uses a single-factor CAPM model. Multi-factor attribution (Fama-French, Carhart) is not included but may be added as a related skill.
- Alpha estimates are highly sensitive to the choice of benchmark; a poorly matched benchmark (e.g., comparing a small-cap fund to the S&P 500) will produce misleading results.
- Short data histories (< 24 months) produce unreliable beta and alpha estimates with wide confidence intervals.
- The skill does not account for transaction costs, taxes, or currency hedging effects.
- Capture ratios computed on monthly data may differ from those computed on daily data.

**Related Skills in This Repo:**
- `investing/portfolio-analysis` — Sharpe Ratio Calculator
- `investing/portfolio-analysis` — Portfolio Risk Decomposition (Multi-Factor)
- `investing/portfolio-analysis` — Drawdown and Recovery Analysis
- `investing/risk-management` — Value at Risk (VaR) Estimator