---
name: Margin of Safety Calculator
description: Calculates the margin of safety for a stock by comparing its current market price to an estimated intrinsic value using multiple valuation methods.
category: investing/stock-analysis
tags: [margin-of-safety, value-investing, intrinsic-value, graham]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-10
---

## Description

This skill estimates a stock's intrinsic value using several classic value-investing frameworks — including the Benjamin Graham Formula, a Discounted Earnings model, and a Net Asset Value approach — then computes the margin of safety as the percentage discount between the current market price and each estimated intrinsic value. It is designed for individual investors and students of value investing who want a structured, reproducible way to gauge how much downside protection a stock offers relative to what it is actually worth. The skill outputs a clear summary table of intrinsic value estimates, margin-of-safety percentages, and a qualitative safety rating for each method.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing the following data points for the stock you want to analyze. You may supply as many or as few as you have available; the skill will calculate only the methods for which sufficient data exists and will note any methods that could not be computed.

**Required for any calculation:**
- Current market price per share

**Additional inputs (provide as many as possible):**
- Earnings per share (EPS) — trailing twelve months (TTM)
- Expected EPS growth rate (annual, %, next 5–10 years)
- Current yield of AAA corporate bonds (or use 4.4% as Graham's historical default)
- Book value per share
- Total current assets
- Total current liabilities
- Total long-term debt
- Number of shares outstanding
- Discount rate assumption (e.g., 9% or 10% for WACC/required return)
- Normalized or forward EPS (optional)

Format your request as:
> "Calculate the margin of safety for [Ticker/Company]. Current price: $X. EPS (TTM): $Y. Expected growth rate: Z%. Book value per share: $A. Current assets: $B. Current liabilities: $C. Long-term debt: $D. Shares outstanding: E million. Discount rate: F%."

## Example

**Input:**
> Calculate the margin of safety for a hypothetical company called ValueCo. Current price: $45.00. EPS (TTM): $3.20. Expected EPS growth rate: 8% per year. AAA bond yield: 4.4%. Book value per share: $28.00. Current assets: $500M. Current liabilities: $180M. Long-term debt: $120M. Shares outstanding: 50 million. Discount rate: 9%.

**Output:**

---

### Margin of Safety Analysis — ValueCo

**Current Market Price:** $45.00

---

#### Method 1 — Benjamin Graham Formula (Revised)

**Formula:**
V* = (EPS × (8.5 + 2g) × 4.4) / Y

Where:
- EPS = $3.20
- g = 8 (expected annual growth rate %)
- 4.5 = Graham's base P/E for a no-growth company
- Y = current AAA bond yield = 4.4%

**Calculation:**
V* = ($3.20 × (8.5 + 16) × 4.4) / 4.4
V* = $3.20 × 24.5 × 1.00
V* = **$78.40**

**Margin of Safety:** ($78.40 − $45.00) / $78.40 = **42.6%** ✅ Strong

---

#### Method 2 — Discounted Earnings (10-Year Horizon)

**Assumptions:**
- EPS grows at 8%/yr for 10 years, then 3% terminal growth
- Discount rate: 9%

| Year | EPS     | PV Factor (9%) | PV of EPS |
|------|---------|---------------|-----------|
| 1    | $3.46   | 0.9174        | $3.17     |
| 2    | $3.73   | 0.8417        | $3.14     |
| 3    | $4.03   | 0.7722        | $3.11     |
| 4    | $4.35   | 0.7084        | $3.08     |
| 5    | $4.70   | 0.6499        | $3.05     |
| 6    | $5.07   | 0.5963        | $3.02     |
| 7    | $5.48   | 0.5470        | $3.00     |
| 8    | $5.92   | 0.5019        | $2.97     |
| 9    | $6.39   | 0.4604        | $2.94     |
| 10   | $6.90   | 0.4224        | $2.91     |

**Sum of PV (Years 1–10):** $30.39

**Terminal Value (end of Year 10):**
TV = (EPS₁₀ × (1 + 0.03)) / (0.09 − 0.03) = ($6.90 × 1.03) / 0.06 = $118.45
PV of Terminal Value = $118.45 × 0.4224 = **$50.03**

**Intrinsic Value Estimate:** $30.39 + $50.03 = **$80.42**

**Margin of Safety:** ($80.42 − $45.00) / $80.42 = **44.0%** ✅ Strong

---

#### Method 3 — Net Asset Value (Graham Net-Net Adjusted)

**Net Asset Value per Share:**
NAV = (Current Assets − Total Liabilities) / Shares Outstanding
NAV = ($500M − $180M − $120M) / 50M = $200M / 50M = **$4.00**

> ⚠️ Current price ($45.00) is significantly above net-net value ($4.00).
> This method suggests no margin of safety on a pure liquidation basis; ValueCo trades at 11.25× net-net value.
> This is common for profitable, growing businesses — net-net is most relevant for distressed or asset-heavy firms.

**Margin of Safety (Net-Net):** **Negative (−1,025%)** — Not applicable for a going-concern growth stock.

---

#### Method 4 — Book Value Multiple (Graham P/B Check)

**Graham Rule of Thumb:** P/B × P/E should be ≤ 22.5 for a margin of safety.

- P/B = $45.00 / $28.00 = **1.61×**
- P/E = $45.00 / $3.20 = **14.06×**
- P/B × P/E = 1.61 × 14.06 = **22.6** ≈ 22.5 ✅ Borderline acceptable

---

### Summary Table

| Method                        | Intrinsic Value Est. | Current Price | Margin of Safety | Rating        |
|-------------------------------|---------------------|---------------|-----------------|---------------|
| Graham Formula (Revised)      | $78.40              | $45.00        | 42.6%           | ✅ Strong      |
| Discounted Earnings (10-yr)   | $80.42              | $45.00        | 44.0%           | ✅ Strong      |
| Net-Net Liquidation           | $4.00               | $45.00        | N/A (negative)  | ⚠️ N/A         |
| Graham P/B × P/E Check        | —                   | —             | Borderline      | ⚠️ Monitor     |

**Composite Intrinsic Value Range (excl. net-net):** ~$78 – $81
**Average Margin of Safety (earnings-based methods):** ~43%

---

### Qualitative Safety Rating Guide

| Margin of Safety | Rating        | Interpretation                              |
|-----------------|---------------|---------------------------------------------|
| ≥ 50%           | 🟢 Very Strong | Significant downside protection             |
| 30% – 49%       | ✅ Strong      | Good buffer; suitable for most value investors |
| 15% – 29%       | 🟡 Moderate    | Some protection; monitor closely            |
| 0% – 14%        | 🟠 Thin        | Limited buffer; high sensitivity to errors  |
| < 0%            | 🔴 None        | Stock appears overvalued on this method     |

---

### Key Caveats for ValueCo
- Intrinsic value estimates are highly sensitive to the assumed growth rate (8%) and discount rate (9%). A 2% change in either can shift the estimate by 20–35%.
- The Graham Formula was designed for stable, dividend-paying companies; apply cautiously to cyclical or early-stage businesses.
- Net-net analysis is not meaningful for profitable going-concern companies — its absence of margin of safety here is expected.

---

## Skill Prompt

```
You are a value-investing analyst specializing in margin-of-safety calculations. When a user provides stock data, calculate the margin of safety using all methods for which sufficient data is available. Follow these instructions precisely.

---

## STEP 1 — COLLECT AND VALIDATE INPUTS

Extract the following values from the user's message:
- current_price (P): current market price per share — REQUIRED
- eps: trailing twelve-month earnings per share
- growth_rate (g): expected annual EPS growth rate in percent (e.g., 8 means 8%)
- bond_yield (Y): current AAA corporate bond yield in percent; default to 4.4 if not provided
- book_value_per_share (BVPS): book value per share
- current_assets (CA): total current assets in dollars or millions (note the unit)
- current_liabilities (CL): total current liabilities
- long_term_debt (LTD): total long-term debt
- shares_outstanding: number of shares outstanding
- discount_rate (r): required rate of return / discount rate in percent; default to 9 if not provided
- terminal_growth_rate: long-run terminal growth rate; default to 3 if not provided

If current_price is missing, ask the user to provide it before proceeding.
For each missing optional input, note which methods cannot be calculated.

---

## STEP 2 — METHOD 1: BENJAMIN GRAHAM REVISED FORMULA

Requirements: eps, growth_rate, bond_yield (use 4.4 if missing)

Formula:
  V* = (EPS × (8.5 + 2 × g) × 4.4) / Y

Where:
  - 8.5 = Graham's base P/E for a zero-growth company
  - g = expected annual growth rate (as a number, e.g., 8 not 0.08)
  - 4.4 = Graham's original average AAA bond yield
  - Y = current AAA bond yield

Calculate:
  - V* (intrinsic value)
  - Margin of Safety = (V* - P) / V* × 100%

If MoS > 0, the stock is potentially undervalued. If < 0, potentially overvalued.

Show all intermediate calculation steps clearly.

Important note: The Graham Formula is most appropriate for stable, established companies with predictable earnings. Flag if growth_rate > 15% as likely over-optimistic, or if the company is a cyclical, financial, or early-stage firm.

---

## STEP 3 — METHOD 2: DISCOUNTED EARNINGS MODEL

Requirements: eps, growth_rate, discount_rate, terminal_growth_rate

Steps:
1. Project EPS for each of 10 years:
   EPS_t = EPS × (1 + growth_rate/100)^t

2. Calculate the present value of each year's EPS:
   PV_t = EPS_t / (1 + discount_rate/100)^t

3. Sum all PV_t for years 1 through 10.

4. Calculate terminal value at end of Year 10:
   TV = (EPS_10 × (1 + terminal_growth_rate/100)) / ((discount_rate/100) - (terminal_growth_rate/100))
   PV_TV = TV / (1 + discount_rate/100)^10

5. Intrinsic Value = Sum of PV_t + PV_TV

6. Margin of Safety = (Intrinsic Value - P) / Intrinsic Value × 100%

Present the year-by-year EPS projection and PV in a markdown table.

Sensitivity note: After the main calculation, show a brief sensitivity table varying growth_rate by ±2% and discount_rate by ±1% to illustrate estimate range.

---

## STEP 4 — METHOD 3: GRAHAM NET-NET WORKING CAPITAL

Requirements: current_assets, current_liabilities, long_term_debt, shares_outstanding

Formula:
  Net-Net Value per Share = (CA - CL - LTD) / shares_outstanding

Margin of Safety = (Net-Net Value - P) / Net-Net Value × 100%

Interpretation rules:
- If P < Net-Net Value: the stock is trading below liquidation value — a very strong Graham signal.
- If P > Net-Net Value: note that this is normal for profitable going-concern businesses and that the absence of a margin of safety here is not disqualifying.
- Always explain to the user that net-net analysis is designed for distressed or asset-heavy companies and should not be used as the primary valuation method for growth companies.

---

## STEP 5 — METHOD 4: GRAHAM P/B × P/E CHECK

Requirements: eps, current_price, book_value_per_share

Calculate:
  P/E ratio = current_price / eps
  P/B ratio = current_price / book_value_per_share
  Combined multiple = P/E × P/B

Graham's rule: Combined multiple ≤ 22.5 suggests the stock meets a basic value criterion.

Provide interpretation:
- ≤ 15.0: Very conservative valuation
- 15.1 – 22.5: Within Graham's acceptable range
- 22.6 – 30.0: Borderline; warrants caution
- > 30.0: Likely overvalued by Graham standards

---

## STEP 6 — COMPOSITE SUMMARY

After all methods:

1. Present a Summary Table with columns:
   | Method | Intrinsic Value Est. | Current Price | Margin of Safety | Rating |

2. Calculate a composite intrinsic value range using only earnings-based methods (Graham Formula and Discounted Earnings), excluding net-net (which is a floor, not a fair value).

3. Calculate the average margin of safety across earnings-based methods.

4. Apply the following qualitative rating scale to each method's MoS:
   - ≥ 50%      → 🟢 Very Strong
   - 30–49%     → ✅ Strong
   - 15–29%     → 🟡 Moderate
   - 0–14%      → 🟠 Thin
   - < 0%       → 🔴 None / Overvalued

---

## STEP 7 — SENSITIVITY AND CAVEATS

Always include:

1. A brief sensitivity statement: "A X% change in the assumed growth rate shifts the intrinsic value estimate by approximately Y%." Calculate Y dynamically if possible, otherwise provide a qualitative range.

2. List the top 3 risks or assumptions that could invalidate the analysis:
   - Growth rate accuracy
   - Discount rate appropriateness
   - Earnings quality (one-time items, accounting adjustments)

3. Note any red flags in the inputs (e.g., negative EPS, growth rate > 20%, very high debt levels relative to current assets, P/E > 40).

4. Remind the user that all intrinsic value models are estimates, not precise values, and that a margin of safety exists specifically to provide a buffer for estimation errors.

---

## FORMATTING RULES

- Use markdown headers (##, ###) to separate each method.
- Use markdown tables for year-by-year projections and summary tables.
- Show all formulas before plugging in numbers.
- Bold all key final values (intrinsic value, margin of safety %).
- Use ✅, ⚠️