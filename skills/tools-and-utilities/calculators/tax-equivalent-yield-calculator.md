---
name: Tax-Equivalent Yield Calculator
description: Calculates the tax-equivalent yield of municipal bonds and other tax-exempt securities to compare them fairly against taxable alternatives.
category: tools-and-utilities/calculators
tags: [tax-equivalent-yield, municipal-bonds, tax-bracket, after-tax]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-07
---

## Description

This skill computes the tax-equivalent yield (TEY) of tax-exempt investments — most commonly municipal bonds — so investors can make apples-to-apples comparisons against taxable bonds, CDs, money-market funds, and other yield-bearing instruments. It accounts for federal marginal tax rates, optional state income tax, and the net investment income tax (NIIT) where applicable. The output includes a side-by-side breakeven analysis and a sensitivity table across multiple tax brackets, giving investors a clear picture of when the tax-exempt option wins or loses.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing:
1. The **tax-exempt yield** (e.g., the stated yield on a municipal bond), as a percentage.
2. Your **federal marginal tax bracket** (e.g., 22%, 24%, 32%, 35%, 37%).
3. *(Optional)* Your **state income tax rate** on investment income (0% if the bond is also state-tax-exempt in your state).
4. *(Optional)* Whether the **3.8% NIIT** applies to you (yes/no, or "auto" to let the skill decide based on bracket).
5. *(Optional)* One or more **taxable yields** you want to compare against.

You may provide inputs in plain English: *"I'm looking at a muni bond yielding 3.2%. I'm in the 32% federal bracket, 6% state tax. Compare it against a Treasury at 5.1% and a corporate at 5.6%."*

## Example

**Input:**
> Municipal bond yield: 3.2%. Federal bracket: 32%. State tax rate: 6% (bond is state-tax-exempt in my state). NIIT applies. Compare against a 5-year Treasury at 5.1% and an investment-grade corporate bond at 5.6%.

**Output:**

### Tax-Equivalent Yield Analysis

**Your Inputs**
| Parameter | Value |
|---|---|
| Tax-exempt (muni) yield | 3.20% |
| Federal marginal rate | 32.00% |
| State income tax rate | 6.00% (exempt on this bond) |
| Net Investment Income Tax | 3.80% |
| Combined marginal rate on taxable income | 41.80% |

---

**Core Formula**

```
TEY = Tax-Exempt Yield ÷ (1 − Combined Marginal Rate)
TEY = 3.20% ÷ (1 − 0.4180)
TEY = 3.20% ÷ 0.5820
TEY = 5.50%
```

> To match the after-tax return of this 3.20% muni, a **taxable investment must yield at least 5.50%**.

---

**Head-to-Head Comparison**

| Investment | Stated Yield | After-Tax Yield* | vs. Muni (After-Tax) |
|---|---|---|---|
| Municipal Bond | 3.20% | **3.20%** (tax-exempt) | — baseline — |
| 5-Year Treasury | 5.10% | 2.97% (fed+NIIT only, state-exempt) | −0.23% ❌ |
| Investment-Grade Corporate | 5.60% | 3.26% (all taxes apply) | +0.06% ✅ |

*After-tax yield = Stated Yield × (1 − applicable combined rate)*

> **Treasury note:** Treasuries are state-tax-exempt. Combined rate applied = 32% + 3.8% = 35.8%.
> **Corporate note:** Fully taxable. Combined rate = 41.8%.

**Verdict:** At your tax rates, the muni outperforms the Treasury but is very slightly behind the corporate bond on an after-tax basis. The corporate's margin (+0.06%) is thin — credit risk and liquidity should factor into the final decision.

---

**Breakeven Muni Yield** *(to match each taxable alternative)*

| Taxable Instrument | Taxable Yield | Breakeven Muni Yield |
|---|---|---|
| 5-Year Treasury | 5.10% | 3.27% |
| IG Corporate | 5.60% | 3.26% (you need ≥ 3.26% muni to win) |

---

**Sensitivity Table — TEY Across Tax Brackets**
*(Muni yield held constant at 3.20%; state 6% exempt; NIIT where noted)*

| Federal Bracket | +State | +NIIT? | Combined Rate | TEY |
|---|---|---|---|---|
| 22% | 6% | No | 28.0% | 4.44% |
| 24% | 6% | No | 30.0% | 4.57% |
| 32% | 6% | Yes | 41.8% | **5.50%** ← you |
| 35% | 6% | Yes | 44.8% | 5.80% |
| 37% | 6% | Yes | 46.8% | 6.02% |

> Higher brackets benefit more from tax-exempt income. At 37%+NIIT+state, this muni is equivalent to a taxable yield above 6%.

---

## Skill Prompt

```
You are a precise financial calculator and educator specializing in fixed-income taxation. When this skill is invoked, perform a complete Tax-Equivalent Yield (TEY) analysis by following every step below.

---

## STEP 1 — GATHER INPUTS

Collect and confirm the following from the user's message:

1. TAX_EXEMPT_YIELD (%): The stated yield of the tax-exempt security (e.g., municipal bond coupon yield, SEC 30-day yield for a muni fund).
2. FEDERAL_RATE (%): The user's federal marginal income tax rate. Common values: 10, 12, 22, 24, 32, 35, 37.
3. STATE_RATE (%): State income tax rate on investment income. Default to 0% if not provided. Note whether the specific bond is also exempt from state tax (which is common for in-state munis or US territories like Puerto Rico bonds).
4. NIIT (%): Net Investment Income Tax surcharge of 3.8%, applicable to single filers with MAGI > $200,000 or MFJ > $250,000. If the user says "auto," apply NIIT if federal bracket is 32% or higher (a practical heuristic; note it is not exact).
5. STATE_EXEMPT (boolean): Is the bond also exempt from the user's state income tax? Default to true for "general obligation" munis issued in the user's own state; ask if unclear.
6. TAXABLE_COMPARISONS (optional list): One or more taxable yields to compare against. Note the type of each (Treasury, CD, corporate, agency, etc.) because Treasuries are state-tax-exempt.

If critical inputs are missing, ask the user before proceeding. Do not assume a tax bracket.

---

## STEP 2 — COMPUTE COMBINED MARGINAL RATE

The combined marginal rate depends on which taxes apply to the taxable alternative being compared:

For FULLY TAXABLE instruments (corporates, CDs, most agency bonds):
  COMBINED_RATE = FEDERAL_RATE + STATE_RATE + NIIT_RATE

For STATE-EXEMPT taxable instruments (US Treasury securities, I-Bonds):
  COMBINED_RATE_TREASURY = FEDERAL_RATE + NIIT_RATE   (no state tax)

For the tax-exempt bond itself:
  After-tax yield = TAX_EXEMPT_YIELD (no taxes owed, assuming full federal + state exemption)
  If only FEDERAL exempt (not state): After-tax yield = TAX_EXEMPT_YIELD × (1 − STATE_RATE)

All rates must be expressed as decimals in formulas (e.g., 32% → 0.32).

---

## STEP 3 — CALCULATE TAX-EQUIVALENT YIELD

Core TEY formula:
  TEY = TAX_EXEMPT_YIELD / (1 − COMBINED_RATE)

Where COMBINED_RATE is the rate applicable to a fully taxable alternative.

Show the formula with numbers substituted in, then the result rounded to two decimal places.

Interpret the result in plain English:
  "To match the after-tax return of [X]% tax-exempt, a taxable investment must yield at least [TEY]%."

---

## STEP 4 — AFTER-TAX YIELD OF TAXABLE COMPARISONS

For each taxable instrument provided by the user:
  After_Tax_Yield = Stated_Yield × (1 − Applicable_Combined_Rate)

Apply the correct combined rate based on the instrument type (see Step 2).

Round to two decimal places. Flag which taxes are applied for each instrument.

---

## STEP 5 — HEAD-TO-HEAD COMPARISON TABLE

Produce a table with columns:
  Investment | Stated Yield | After-Tax Yield | vs. Muni (After-Tax) | Verdict

Verdict logic:
  - If After-Tax Yield of taxable > TAX_EXEMPT_YIELD: taxable wins (✅ for taxable)
  - If After-Tax Yield of taxable < TAX_EXEMPT_YIELD: muni wins (❌ for taxable)
  - If difference < 0.10%: call it "essentially a tie — consider credit/liquidity risk"

---

## STEP 6 — BREAKEVEN ANALYSIS

For each taxable instrument, calculate the minimum muni yield needed to match it:
  Breakeven_Muni_Yield = Taxable_Yield × (1 − Applicable_Combined_Rate)

This is the inverse question: "How low can the muni yield fall before the taxable alternative wins?"

---

## STEP 7 — SENSITIVITY TABLE

Generate a sensitivity table showing TEY at different federal brackets (22%, 24%, 32%, 35%, 37%), holding:
  - TAX_EXEMPT_YIELD constant
  - STATE_RATE constant at user's value (or 0% if not provided)
  - NIIT applied for brackets 32%+ (use the auto heuristic)

Format as a clean markdown table. Highlight the user's actual bracket.

---

## STEP 8 — QUALITATIVE COMMENTARY

After the tables, provide 3–5 bullet points of relevant context:

1. CREDIT RISK: Munis are generally investment-grade but not risk-free. GO bonds vs. revenue bonds differ. US Treasuries are backed by the full faith and credit of the US government.
2. AMT: Some "private activity" municipal bonds are subject to the Alternative Minimum Tax. Ask if the user knows whether the bond is AMT-exempt.
3. LIQUIDITY: Munis can be less liquid than Treasuries or large corporate issues. Bid-ask spreads matter for shorter holding periods.
4. DURATION/INTEREST RATE RISK: Yield comparisons are point-in-time. Longer duration bonds carry more price risk.
5. STATE TAX NUANCE: If the user is not a resident of the issuing state, the muni may not be state-tax-exempt, which changes the calculation. Note this explicitly.
6. MUTUAL FUNDS / ETFs: For muni funds, use the SEC 30-day yield and note that fund expenses reduce effective yield.

---

## STEP 9 — FORMAT REQUIREMENTS

- Use markdown tables for all comparisons and the sensitivity table.
- Show all formulas with numbers substituted in (not just symbolic).
- Clearly label each section with a heading.
- Round all yields to 2 decimal places in tables; use 4 decimal places in intermediate formula steps only if needed for precision.
- Always include the disclaimer that this is informational only and not financial advice.
- Keep language accessible — define "tax-equivalent yield" briefly for users who may be unfamiliar.
- If the user provided no taxable comparisons, still compute the TEY and sensitivity table, and suggest they compare against current Treasury, CD, and high-grade corporate yields.

---

## ERROR HANDLING

- If the combined marginal rate is >= 100%, flag an error (impossible tax rate).
- If TAX_EXEMPT_YIELD is 0% or negative, note that TEY is trivially 0 and ask the user to confirm the input.
- If the user provides a bracket not in the standard set (e.g., 28%), use it as provided but note it is non-standard under current US tax law.
- Always sanity-check: TEY must always be greater than the tax-exempt yield when combined rate > 0.
```

## Notes

**Data Requirements:**
- User must know their federal marginal tax bracket (not effective/average rate).
- State income tax rate should reflect the marginal rate on investment income, which may differ from the ordinary income rate in some states.
- For muni funds, use the fund's published SEC 30-day yield, not distribution yield, for most accurate comparisons.

**Known Limitations:**
- The skill uses a simplified combined-rate model. In reality, the interaction between the NIIT, state taxes, and federal deductions (e.g., SALT cap) creates more complex effective rates for some taxpayers.
- AMT implications for private-activity bonds are noted qualitatively but not calculated numerically — this requires full AMT modeling.
- Does not account for capital gains treatment on bond price appreciation/discount accretion (OID or market discount rules).
- State tax exemption rules vary widely; a few states tax all bond interest including in-state munis. The skill prompts users to verify but cannot look up state-specific rules automatically.
- Yield-to-maturity vs. current yield distinction is not addressed — users should confirm which yield figure they are inputting.

**Related Skills in This Repo:**
- `bond-duration-convexity-calculator` — for interest rate risk analysis
- `after-tax-return-analyzer` — broader after-tax return framework across asset classes
- `marginal-vs-effective-tax-rate-explainer` — helps users identify the correct bracket to use