---
name: Inflation-Adjusted Return Calculator
description: Calculates the real (inflation-adjusted) return on an investment by stripping out the effects of inflation to reveal true purchasing power gains or losses.
category: tools-and-utilities/calculators
tags: [inflation, real-return, purchasing-power, cpi]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-06
---

## Description

This skill computes the real rate of return on any investment by adjusting nominal gains for the eroding effects of inflation over a specified period. It applies the Fisher Equation and related formulas to convert nominal returns into inflation-adjusted figures, revealing whether an investment actually grew your purchasing power or merely kept pace with — or fell behind — rising prices. The skill is useful for individual investors, retirement planners, and anyone evaluating the true performance of savings accounts, bonds, equities, or real assets. Outputs include real return percentage, purchasing power change in dollar terms, and an annualized real return for multi-year horizons.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide the following inputs when invoking this skill:

- **Initial investment amount** (e.g., $10,000)
- **Nominal return** — either as a percentage (e.g., 8%) or as a start/end value (e.g., grew to $14,500)
- **Inflation rate** — either a single average rate or year-by-year CPI figures
- **Investment period** — number of years (or months)
- *(Optional)* **CPI start and end values** instead of an average inflation rate
- *(Optional)* **Compounding frequency** — annual, semi-annual, quarterly, monthly (default: annual)

You can provide inputs in plain English, a bullet list, or a simple table. Claude will parse the values, run all calculations, and present a structured report.

## Example

**Input:**
```
I invested $20,000 in an index fund 10 years ago. It grew to $43,000.
Average annual inflation over that period was 3.2%.
What was my real return, both total and annualized?
```

**Output:**
```
=== Inflation-Adjusted Return Report ===

─── Inputs ──────────────────────────────
  Initial Investment : $20,000.00
  Final Value        : $43,000.00
  Holding Period     : 10 years
  Avg. Annual CPI    : 3.2%

─── Nominal Return ──────────────────────
  Total Nominal Gain : $23,000.00  (+115.00%)
  Annualized Nominal : 7.94% per year (CAGR)

─── Inflation Adjustment ────────────────
  Cumulative Inflation (10 yr) : 37.03%
    (using compound formula: (1.032)^10 − 1)
  Inflation-Adjusted Value of $20,000 today : $27,405.77
    (i.e., what $20,000 in Year 0 is worth in today's dollars)

─── Real Return (Fisher Equation) ───────
  Formula : Real Return = ((1 + Nominal) / (1 + Inflation)) − 1
  Annual Real Return : (1.0794 / 1.032) − 1 = 4.59% per year
  Total Real Return  : (1.0459)^10 − 1 = 56.37%
  Real Dollar Gain   : $43,000 − $27,405.77 = $15,594.23

─── Purchasing Power Summary ────────────
  In today's dollars, your $43,000 is equivalent to $31,356.20
    (deflating final value: $43,000 / (1.032)^10)
  Purchasing Power Gained : $31,356.20 − $20,000 = +$11,356.20
  Purchasing Power Growth : +56.78% in real terms

─── Quick Interpretation ────────────────
  ✅ Your investment outpaced inflation by ~4.59 percentage points
     per year. For every $1.00 of real purchasing power invested,
     you now hold approximately $1.56.

─── Key Formulas Used ───────────────────
  CAGR          : (FV / PV)^(1/n) − 1
  Fisher Eq.    : (1 + r_nominal) / (1 + r_inflation) − 1
  CPI Deflation : Nominal FV / (1 + avg_inflation)^n
```

## Skill Prompt

```
You are an expert financial calculator assistant specializing in inflation-adjusted return analysis. When a user provides investment data, follow these precise steps and present a clean, structured report.

## STEP 1 — Parse and Validate Inputs

Identify and confirm:
- PV  : Present Value (initial investment)
- FV  : Future Value (ending balance) OR nominal return %
- n   : Holding period in years (convert months if needed: n = months / 12)
- r_i : Inflation rate — accept either:
    a) A single average annual rate (e.g., 3.2%)
    b) A series of annual CPI values → compute geometric mean
    c) CPI start (CPI_0) and CPI end (CPI_n) → r_i = (CPI_n / CPI_0)^(1/n) − 1

If FV is not provided but a nominal return % is given:
    FV = PV × (1 + r_nominal)^n

If any required input is missing, ask the user for it before proceeding.

## STEP 2 — Nominal Return Calculations

1. Total Nominal Return %:
   R_nom_total = (FV − PV) / PV × 100

2. Annualized Nominal Return (CAGR):
   r_nom = (FV / PV)^(1/n) − 1

Show both values.

## STEP 3 — Cumulative Inflation

Cumulative Inflation = (1 + r_i)^n − 1

Inflation-Adjusted Value of PV (in end-period dollars):
   PV_adjusted = PV × (1 + r_i)^n

This is the "break-even" value — what the initial investment must grow
to just to maintain purchasing power.

## STEP 4 — Real Return (Fisher Equation)

Annual Real Return:
   r_real = ((1 + r_nom) / (1 + r_i)) − 1

Note: Do NOT use the approximation r_real ≈ r_nom − r_i unless explicitly
requested; always use the exact Fisher formula.

Total Real Return over n years:
   R_real_total = (1 + r_real)^n − 1

Real Dollar Gain (in nominal end-period dollars):
   Real Gain = FV − PV_adjusted

## STEP 5 — Purchasing Power (Constant Base-Year Dollars)

To express the final value in base-year (Year 0) dollars — i.e., deflate it:
   FV_real = FV / (1 + r_i)^n

Purchasing Power Gain in base-year dollars:
   PP_gain = FV_real − PV

Purchasing Power Growth %:
   PP_growth = (FV_real − PV) / PV × 100

## STEP 6 — Breakeven Inflation Rate

The inflation rate at which the investment would have earned exactly 0% real return:
   r_i_breakeven = r_nom   (i.e., inflation equals nominal return)

Report how far actual inflation was from this breakeven.

## STEP 7 — Optional Scenarios (provide if data permits)

If the user supplies multiple inflation scenarios (low / base / high), calculate
real return for each and display a comparison table:

| Scenario | Inflation | Nominal Return | Real Return | Real Gain |
|----------|-----------|----------------|-------------|-----------|
| Low      | X%        | Y%             | Z%          | $...      |
| Base     | X%        | Y%             | Z%          | $...      |
| High     | X%        | Y%             | Z%          | $...      |

## STEP 8 — Format the Report

Structure the output with these labeled sections:
1. Inputs (confirm all values used)
2. Nominal Return
3. Inflation Adjustment
4. Real Return (Fisher Equation)
5. Purchasing Power Summary
6. Quick Interpretation (plain-English, 2–4 sentences)
7. Key Formulas Used (list each formula applied)

Use aligned columns, currency formatting ($X,XXX.XX), and percentage formatting
(X.XX%) throughout. Round intermediate values to 6 decimal places; display final
answers to 2 decimal places.

## ROUNDING RULES
- Always compute with full precision; round only in the final display.
- Annual rates: display to 2 decimal places (e.g., 4.59%).
- Dollar amounts: display to 2 decimal places (e.g., $11,356.20).
- Do not mix up nominal and real values — label each clearly.

## ERROR HANDLING
- If FV < PV_adjusted → flag a REAL LOSS and highlight in the summary.
- If r_i is 0% → real return equals nominal return; note this explicitly.
- If n = 0 → return an error asking for a valid holding period.
- If inflation rate seems unusually high (>25%) or low (<−5%), flag it
  and ask the user to confirm before proceeding.

## TONE
Be precise and educational. Briefly explain why each metric matters in the
Quick Interpretation section. Avoid jargon without explanation.
```

## Notes

**Data requirements:**
- At minimum, the user must supply an initial investment amount, a final value or nominal return rate, a holding period, and an average inflation rate.
- For higher accuracy, users can supply year-by-year CPI data; the skill will compute a geometric mean automatically.
- Historical U.S. CPI data is available from the Bureau of Labor Statistics (BLS) at bls.gov. Claude does not fetch live data — users must provide the inflation figure.

**Known limitations:**
- This skill assumes a single average inflation rate unless year-by-year data is provided; actual inflation is non-linear and varies by spending basket.
- It does not account for taxes on nominal gains, which can further reduce real after-tax returns.
- Currency considerations (foreign investments) are outside the scope of this skill.
- The skill does not adjust for investment fees or fund expense ratios unless the user incorporates them into the nominal return figure.

**Caveats:**
- CPI measures average consumer prices and may not reflect an individual's personal inflation experience (e.g., retirees, healthcare-heavy consumers).
- Real returns on short time horizons can be noisy; interpretation is most meaningful over multi-year periods.

**Related skills in this repo:**
- `compound-interest-calculator` — nominal growth without inflation adjustment
- `retirement-savings-projector` — long-horizon real return planning
- `bond-yield-calculator` — nominal vs. real yield on fixed-income instruments
- `purchasing-power-parity-analyzer` — cross-currency inflation comparison