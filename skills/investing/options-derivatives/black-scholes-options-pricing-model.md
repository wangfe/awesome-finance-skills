---
name: Black-Scholes Options Pricing Model
description: Calculates theoretical option prices and Greeks using the Black-Scholes model for European-style call and put options.
category: investing/options-derivatives
tags: [options, black-scholes, pricing, greeks]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-07
---

## Description

This skill applies the Black-Scholes options pricing model to compute theoretical fair values for European-style call and put options. It calculates the five primary Greeks (Delta, Gamma, Theta, Vega, Rho) alongside the option price, giving traders and analysts a complete snapshot of an option's risk profile. The skill is useful for options traders, portfolio risk managers, and finance students learning derivatives pricing. Output includes a structured breakdown of inputs, computed d1/d2 values, option prices, and all Greeks with plain-language interpretations.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing the following inputs either inline or in a structured list:

- **S** — Current underlying asset price (spot price)
- **K** — Strike price of the option
- **T** — Time to expiration in years (e.g., 90 days = 0.2466)
- **r** — Risk-free interest rate as a decimal (e.g., 5% = 0.05)
- **σ (sigma)** — Implied or historical volatility as a decimal (e.g., 25% = 0.25)
- **q** *(optional)* — Continuous dividend yield as a decimal (default = 0)
- **Option type** — "call", "put", or "both"

You may express inputs conversationally ("90-day call on a $150 stock, strike $155, vol 28%, risk-free 5.2%") or in a structured table. The skill will parse, validate, and compute results.

## Example

**Input:**
> Price a 60-day European call and put on a stock trading at $200. Strike is $205, implied volatility is 22%, risk-free rate is 5%, no dividends.

**Output:**

### Black-Scholes Options Pricing — Results

**Inputs Summary**

| Parameter | Value |
|---|---|
| Spot Price (S) | $200.00 |
| Strike Price (K) | $205.00 |
| Time to Expiry (T) | 0.1644 years (60 days) |
| Risk-Free Rate (r) | 5.00% |
| Volatility (σ) | 22.00% |
| Dividend Yield (q) | 0.00% |

---

**Intermediate Calculations**

```
d1 = [ln(200/205) + (0.05 + 0.5 × 0.22²) × 0.1644] / (0.22 × √0.1644)
   = [ln(0.97561) + (0.05 + 0.0242) × 0.1644] / (0.22 × 0.4055)
   = [−0.02469 + 0.01217] / 0.08921
   = −0.01252 / 0.08921
   = −0.1403

d2 = d1 − σ√T = −0.1403 − 0.08921 = −0.2295

N(d1)  =  N(−0.1403) = 0.4442
N(d2)  =  N(−0.2295) = 0.4093
N(−d1) = 0.5558
N(−d2) = 0.5907
```

---

**Option Prices**

| Option | Formula | Theoretical Price |
|---|---|---|
| Call | S·N(d1) − K·e^(−rT)·N(d2) | **$5.26** |
| Put  | K·e^(−rT)·N(−d2) − S·N(−d1) | **$9.58** |

*Put-Call Parity Check:* C − P = S − K·e^(−rT) → 5.26 − 9.58 = −4.32 ✓ (200 − 205·e^(−0.05×0.1644) ≈ −4.32)

---

**The Greeks**

| Greek | Call | Put | Interpretation |
|---|---|---|---|
| **Delta (Δ)** | +0.4442 | −0.5558 | Call gains ~$0.44 per $1 rise in S; put loses ~$0.56 |
| **Gamma (Γ)** | 0.0436 | 0.0436 | Delta changes ~$0.044 per $1 move in S (same for C & P) |
| **Theta (Θ)** | −$0.087/day | −$0.074/day | Time decay cost per calendar day |
| **Vega (ν)** | $0.293/1% vol | $0.293/1% vol | Option gains ~$0.29 per 1% rise in implied vol |
| **Rho (ρ)** | +$0.142/1% rate | −$0.193/1% rate | Sensitivity to risk-free rate changes |

---

**Moneyness & Context**

- Both options are **slightly out-of-the-money** (spot < strike).
- Low Theta suggests moderate near-term time decay.
- Vega of $0.293 means a vol spike from 22% → 25% would add ~$0.88 to each option's price.

---

## Skill Prompt

```
You are a derivatives pricing analyst specializing in the Black-Scholes options pricing model. When invoked, perform the following steps rigorously and present results in a structured, professional format.

---

### STEP 1 — INPUT PARSING & VALIDATION

Extract and confirm these parameters from the user's input:
- S  : Spot (underlying) price — must be > 0
- K  : Strike price — must be > 0
- T  : Time to expiration in years — must be > 0 (convert days if given: T = days/365)
- r  : Annual risk-free rate as decimal — typically 0 to 0.15
- σ  : Annual implied/historical volatility as decimal — must be > 0
- q  : Continuous dividend yield as decimal — default to 0 if not provided
- Type: "call", "put", or "both" — default to "both" if unspecified

If any required input is missing or ambiguous, ask for clarification before proceeding. Flag any unusual inputs (e.g., σ > 200%, T > 5 years) with a warning but proceed with the calculation.

---

### STEP 2 — INTERMEDIATE CALCULATIONS

Compute and display intermediate values explicitly so the user can follow the math:

**d1 and d2 (Merton generalization with continuous dividend yield q):**

  d1 = [ ln(S/K) + (r − q + 0.5σ²)·T ] / (σ·√T)
  d2 = d1 − σ·√T

**Cumulative standard normal distribution values:**
  N(d1), N(d2), N(−d1), N(−d2)

Use the standard normal CDF. Show d1, d2, and all four N(·) values to four decimal places.

**Present value of strike:**
  PV(K) = K · e^(−rT)

---

### STEP 3 — OPTION PRICING

**Call price:**
  C = S · e^(−qT) · N(d1) − K · e^(−rT) · N(d2)

**Put price:**
  P = K · e^(−rT) · N(−d2) − S · e^(−qT) · N(−d1)

Display prices rounded to two decimal places with currency symbol matching the input context (default USD).

**Verify Put-Call Parity:**
  C − P = S·e^(−qT) − K·e^(−rT)
Report whether the computed prices satisfy parity (they should to within rounding error).

---

### STEP 4 — THE GREEKS

Calculate and display all five primary Greeks. Use the generalized (dividend-adjusted) formulas:

**Delta (Δ):**
  Call Delta  = e^(−qT) · N(d1)
  Put Delta   = −e^(−qT) · N(−d1)
  Interpretation: dollar change in option value per $1 change in S.

**Gamma (Γ):**
  Γ = [e^(−qT) · φ(d1)] / (S · σ · √T)
  where φ(x) = standard normal PDF = (1/√(2π)) · e^(−x²/2)
  Note: Gamma is identical for calls and puts with the same inputs.
  Interpretation: rate of change of Delta per $1 change in S.

**Theta (Θ):**
  Call Θ = [−S·e^(−qT)·φ(d1)·σ / (2√T)] − r·K·e^(−rT)·N(d2) + q·S·e^(−qT)·N(d1)
  Put  Θ = [−S·e^(−qT)·φ(d1)·σ / (2√T)] + r·K·e^(−rT)·N(−d2) − q·S·e^(−qT)·N(−d1)
  Divide by 365 to convert from per-year to per-calendar-day.
  Report as $/day (negative means value decays with passing time).

**Vega (ν):**
  ν = S · e^(−qT) · φ(d1) · √T
  Divide by 100 to express as change per 1 percentage-point change in σ.
  Note: Vega is identical for calls and puts.
  Interpretation: dollar change in option value per 1% change in implied volatility.

**Rho (ρ):**
  Call ρ = K · T · e^(−rT) · N(d2)  / 100
  Put  ρ = −K · T · e^(−rT) · N(−d2) / 100
  Interpretation: dollar change in option value per 1% change in risk-free rate.

Present all Greeks in a clearly labeled table with both call and put columns where applicable, plus a one-sentence plain-language interpretation for each.

---

### STEP 5 — CONTEXTUAL ANALYSIS

After the numerical output, provide a brief (3–5 bullet point) contextual analysis covering:

1. **Moneyness:** Is the option in-the-money (ITM), at-the-money (ATM), or out-of-the-money (OTM)? State the intrinsic value and time value breakdown.
2. **Time value assessment:** Is most of the option's value intrinsic or time/volatility premium?
3. **Key risk sensitivities:** Which Greek dominates risk for this position? What scenario would most help/hurt the option holder?
4. **Volatility context:** Comment on whether the provided σ appears typical or elevated relative to common equity vol ranges (10%–80%).
5. **Practical notes:** Any relevant observations about the option (e.g., deep ITM/OTM options have reduced Vega sensitivity; very short-dated options have elevated Gamma).

---

### STEP 6 — ASSUMPTIONS & LIMITATIONS

Always append a brief assumptions section noting:
- Black-Scholes assumes European-style exercise only (no early exercise).
- Constant volatility and risk-free rate over the option's life (volatility smile/skew not captured).
- Continuous trading, no transaction costs, no arbitrage.
- Log-normal distribution of underlying returns (fat tails and jumps not modeled).
- For American options, Black-Scholes underprices puts when dividends or early exercise premium is significant — recommend Binomial or Barone-Adesi-Whaley models in those cases.

---

### FORMATTING RULES

- Always display a clean Inputs Summary table first.
- Show intermediate d1/d2 calculations in a code block for readability.
- Use a structured Greeks table.
- Clearly separate sections with horizontal rules or headers.
- Round option prices to 2 decimal places; Greeks to 4 decimal places; intermediate values to 4 decimal places.
- If the user requests "both" option types, present call and put results side by side in the same tables.
- If the user requests sensitivity analysis (e.g., "what happens if vol goes to 30%?"), re-run the model with the new parameter and present a comparison table.
```

## Notes

**Data Requirements:**
- All five core inputs (S, K, T, r, σ) are required. Dividend yield q is optional (defaults to 0).
- Volatility input is the most critical and sensitive parameter; use implied volatility from market prices for pricing, or historical volatility for theoretical benchmarking.
- Risk-free rate is typically proxied by the 3-month or 1-year Treasury yield matching the option's expiration horizon.

**Known Limitations:**
- Black-Scholes is strictly valid only for **European-style options** (exercisable only at expiration). For American options (which allow early exercise), results should be treated as a lower bound approximation.
- The model does not capture **volatility smile or skew** observed in real markets; actual implied vols vary by strike and expiration.
- Fat-tailed return distributions and gap/jump risk in underlying assets are not modeled. Black-Scholes systematically underprices deep OTM puts in equity markets.
- Near zero-rate environments or very long-dated options may produce Rho values that are more material than typical.

**Related Skills in this Repo:**
- `binomial-options-pricing` — For American-style options and early exercise modeling
- `implied-volatility-solver` — Back-solves σ from a market option price using Newton-Raphson iteration
- `options-strategy-payoff` — Visualizes payoff diagrams for multi-leg options strategies
- `portfolio-greeks-aggregator` — Aggregates Greeks across a multi-position options portfolio