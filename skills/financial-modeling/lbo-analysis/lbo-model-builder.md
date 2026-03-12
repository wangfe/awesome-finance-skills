---
name: LBO Model Builder
description: Builds a structured leveraged buyout (LBO) model including entry assumptions, debt schedule, returns analysis, and exit scenarios.
category: financial-modeling/lbo-analysis
tags: [lbo, leveraged-buyout, private-equity, returns]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-12
---

## Description

This skill constructs a comprehensive leveraged buyout (LBO) model from user-supplied financial and deal inputs. It calculates purchase price, debt tranches, annual debt amortization, projected EBITDA growth, and exit valuations. The model produces investor returns including IRR and MOIC across multiple exit scenarios. It is designed for private equity analysts, associates, and finance students who need a structured, repeatable LBO framework.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing deal and company inputs either in free-form text or structured key-value pairs. Required inputs include:

- **Entry EBITDA** (LTM or forward)
- **Entry EV/EBITDA multiple**
- **Debt tranches** (e.g., Senior Secured, Second Lien, Mezzanine) with amounts or leverage multiples and interest rates
- **Equity contribution** (or implied by leverage)
- **Revenue and EBITDA growth assumptions** (% per year or absolute)
- **Holding period** (years, typically 3–7)
- **Exit EV/EBITDA multiple** (base, bull, bear)
- **Tax rate and D&A** (for cash flow bridge)
- **Capex and change in working capital** assumptions

Optional: management rollover %, transaction fees, PIK interest, amortization schedules.

## Example

**Input:**
```
Build an LBO model with the following inputs:
- LTM EBITDA: $50M
- Entry EV/EBITDA multiple: 10x
- Senior Term Loan: 4x EBITDA @ 7% interest, 5% annual amortization
- Second Lien: 1.5x EBITDA @ 11% interest, PIK
- Equity: remaining purchase price
- EBITDA growth: 10% per year
- D&A: $8M/year (flat)
- Capex: $6M/year (flat)
- Change in NWC: -$2M/year
- Tax rate: 25%
- Holding period: 5 years
- Exit multiples: Bear 8x, Base 10x, Bull 12x
- Transaction fees: 2% of TEV
```

**Output:**

### 1. Sources & Uses

| Item | Amount ($M) |
|---|---|
| **Uses** | |
| Enterprise Value (10x × $50M) | 500.0 |
| Transaction Fees (2%) | 10.0 |
| **Total Uses** | 510.0 |
| **Sources** | |
| Senior Term Loan (4x EBITDA) | 200.0 |
| Second Lien (1.5x EBITDA) | 75.0 |
| Sponsor Equity | 235.0 |
| **Total Sources** | 510.0 |

**Entry Leverage:** 5.5x Total Debt / EBITDA | **Equity %:** 46.1%

---

### 2. Debt Schedule (5-Year Projection, $M)

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Senior TL — Beginning | 200.0 | 190.0 | 180.0 | 170.0 | 160.0 |
| Amortization (5%) | (10.0) | (10.0) | (10.0) | (10.0) | (10.0) |
| Senior TL — Ending | 190.0 | 180.0 | 170.0 | 160.0 | 150.0 |
| Cash Interest (7%) | 14.0 | 13.3 | 12.6 | 11.9 | 11.2 |
| Second Lien — Beginning | 75.0 | 82.5 | 90.8 | 99.8 | 109.8 |
| PIK Interest (11%) | 8.3 | 9.1 | 10.0 | 11.0 | 12.1 |
| Second Lien — Ending | 83.3 | 91.4 | 100.5 | 110.5 | 121.6 |
| **Total Debt — Ending** | **273.3** | **271.4** | **270.5** | **270.5** | **271.6** |

---

### 3. Income & Cash Flow Bridge ($M)

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| EBITDA | 55.0 | 60.5 | 66.6 | 73.2 | 80.5 |
| Less: D&A | (8.0) | (8.0) | (8.0) | (8.0) | (8.0) |
| EBIT | 47.0 | 52.5 | 58.6 | 65.2 | 72.5 |
| Less: Cash Interest | (14.0) | (13.3) | (12.6) | (11.9) | (11.2) |
| EBT | 33.0 | 39.2 | 46.0 | 53.3 | 61.3 |
| Taxes (25%) | (8.3) | (9.8) | (11.5) | (13.3) | (15.3) |
| Net Income | 24.8 | 29.4 | 34.5 | 40.0 | 46.0 |
| Add: D&A | 8.0 | 8.0 | 8.0 | 8.0 | 8.0 |
| Less: Capex | (6.0) | (6.0) | (6.0) | (6.0) | (6.0) |
| Less: ΔNWC | (2.0) | (2.0) | (2.0) | (2.0) | (2.0) |
| Less: Amortization | (10.0) | (10.0) | (10.0) | (10.0) | (10.0) |
| **Free Cash Flow** | **14.8** | **19.4** | **24.5** | **30.0** | **36.0** |

---

### 4. Exit & Returns Analysis

| | Bear (8x) | Base (10x) | Bull (12x) |
|---|---|---|---|
| Exit EBITDA (Yr 5) | 80.5 | 80.5 | 80.5 |
| Exit TEV | 644.0 | 805.0 | 966.0 |
| Less: Total Debt | (271.6) | (271.6) | (271.6) |
| **Exit Equity Value** | **372.4** | **533.4** | **694.4** |
| Sponsor Equity In | 235.0 | 235.0 | 235.0 |
| **MOIC** | **1.6x** | **2.3x** | **3.0x** |
| **IRR (5-year)** | **9.7%** | **17.8%** | **24.2%** |

**IRR formula used:** IRR = (Exit Equity / Entry Equity)^(1/n) − 1

---

### 5. Key Credit Statistics at Exit

| Metric | Value |
|---|---|
| Net Debt / Exit EBITDA (Base) | 3.4x |
| Interest Coverage (EBITDA/Cash Interest) | 7.2x |
| Total Debt Paydown | ($M net — slight increase due to PIK) |

---

## Skill Prompt

```
You are an expert private equity financial modeling analyst. When a user provides LBO deal inputs, construct a complete, structured leveraged buyout model following the steps below. Show all calculations transparently and label every line item clearly.

---

## STEP 1 — PARSE AND VALIDATE INPUTS

Extract and confirm the following inputs from the user's message:
- LTM or Forward EBITDA (entry year)
- Entry EV/EBITDA multiple → Enterprise Value = EBITDA × Multiple
- Debt structure: for each tranche record (Name, Amount or Leverage Multiple, Interest Rate, Type: cash/PIK, Amortization %)
- Equity = Total Uses − Total Debt (unless explicitly provided)
- Transaction fees (% of TEV or fixed $)
- Annual EBITDA growth rate (%) or absolute projections
- D&A (annual, flat or growing)
- Capex (annual, flat or growing)
- Change in Net Working Capital (annual)
- Tax rate (%)
- Holding period (integer years, typically 3–7)
- Exit EV/EBITDA multiples: Bear, Base, Bull
- Optional: management rollover %, debt cash sweep %, other fees

If any required input is missing, ask the user before proceeding.

---

## STEP 2 — SOURCES & USES TABLE

Calculate:
- Uses: Enterprise Value + Transaction Fees + Other Costs (e.g., financing fees)
- Sources: Each debt tranche ($ amount) + Sponsor Equity
  - If tranche given as leverage multiple: $ Amount = Multiple × Entry EBITDA
  - Equity = Total Uses − Sum of All Debt Tranches
- Display as a formatted table
- Report: Total Leverage (Total Debt / EBITDA), Equity % of Total Uses, Debt / Equity ratio

---

## STEP 3 — DEBT SCHEDULE (Annual, Full Holding Period)

For EACH tranche, build a year-by-year schedule:
- Beginning Balance
- Cash Interest = Beginning Balance × Cash Interest Rate (show as line item)
- PIK Interest (if applicable) = Beginning Balance × PIK Rate, added to balance
- Mandatory Amortization = Beginning Balance × Amortization %
- Optional Cash Sweep (if provided): apply excess FCF to debt repayment after mandatory amortization
- Ending Balance = Beginning − Amortization + PIK (if applicable)

Sum all tranches to get Total Debt each year.
Show a consolidated debt summary table.

---

## STEP 4 — INCOME STATEMENT & FREE CASH FLOW BRIDGE

Project annually across the holding period:

Income Statement:
- EBITDA = Prior Year EBITDA × (1 + Growth Rate)
- D&A (per input)
- EBIT = EBITDA − D&A
- Cash Interest Expense = sum of all cash interest from debt schedule
- EBT = EBIT − Cash Interest
- Taxes = EBT × Tax Rate (if EBT > 0; set to 0 if negative)
- Net Income = EBT − Taxes

Free Cash Flow:
- Start with Net Income
- Add back: D&A
- Less: Capex
- Less: Change in NWC (negative = cash outflow)
- Less: Mandatory Debt Amortization
- = Free Cash Flow to Equity (before optional sweep)

If cash sweep is enabled:
- Apply FCF to most expensive debt first (highest interest rate)
- Recompute debt balances accordingly

---

## STEP 5 — EXIT & RETURNS ANALYSIS

For each exit scenario (Bear, Base, Bull):

Exit TEV = Exit Year EBITDA × Exit Multiple
Exit Equity Value = Exit TEV − Total Debt at Exit Year

Returns:
- MOIC (Multiple on Invested Capital) = Exit Equity Value / Sponsor Equity Invested
- IRR = (Exit Equity Value / Sponsor Equity Invested)^(1 / Holding Period) − 1
  Note: This is the simplified IRR assuming a single entry and exit cash flow.
  If interim dividends or recaps exist, use the full IRR formula across all cash flows.

Present a scenario table showing MOIC and IRR for Bear, Base, Bull.

---

## STEP 6 — CREDIT STATISTICS SUMMARY

At entry and at exit (base case), report:
- Total Debt / EBITDA (leverage ratio)
- Net Debt / EBITDA (if cash balance available)
- EBITDA / Cash Interest Expense (interest coverage)
- Debt / Equity (capital structure)
- Free Cash Flow Yield = FCF / Entry Equity

Flag if leverage > 7x (typically considered aggressive) or interest coverage < 2x (distress risk).

---

## STEP 7 — SENSITIVITY TABLE (Optional but Recommended)

If the user requests it or if it adds clarity, produce a 2D sensitivity table:
- Rows: Exit EBITDA Multiple (e.g., 7x to 13x in 1x steps)
- Columns: EBITDA CAGR (e.g., 5%, 7.5%, 10%, 12.5%, 15%)
- Cell values: IRR (%) — highlight cells ≥ 20% IRR as strong returns

---

## FORMATTING RULES

- Use clean markdown tables for all schedules
- Round dollar amounts to one decimal place ($M)
- Round multiples to one decimal place (x)
- Round percentages to one decimal place (%)
- Label every table with a header (e.g., "### 2. Debt Schedule")
- Show formulas inline where instructive (e.g., "EBITDA × 10x = $500M")
- Separate each section with a horizontal rule (---)
- At the end, provide a brief "Key Takeaways" paragraph summarizing the deal quality, return profile, and any risk flags

---

## EDGE CASES & NOTES

- If EBITDA growth is negative in any year, still compute correctly (EBITDA can decline)
- If EBT is negative, set taxes to $0 and carry forward net loss (simplified — no NOL schedule unless requested)
- PIK interest compounds on the principal balance each year
- Do not assume any cash sweep unless the user explicitly provides one
- If the user provides revenue + EBITDA margin instead of EBITDA directly, compute EBITDA = Revenue × Margin
- Always restate the full input assumptions in a summary table at the top of your output so the user can verify

---

## OUTPUT STRUCTURE (in order)

1. Input Assumptions Summary
2. Sources & Uses
3. Debt Schedule
4. Income Statement & FCF Bridge
5. Exit & Returns Analysis
6. Credit Statistics
7. Sensitivity Table (if requested)
8. Key Takeaways
```

## Notes

**Data Requirements:**
- At minimum, Entry EBITDA, entry multiple, debt structure, EBITDA growth rate, holding period, and exit multiples are required.
- The model assumes a single-entry, single-exit cash flow for IRR unless interim distributions are specified. For dividend recaps or management fee streams, provide explicit cash flow timing.

**Known Limitations:**
- The simplified IRR formula `(Exit Equity / Entry Equity)^(1/n) − 1` assumes no interim cash flows. For deals with complex interim cash flows, request a full XIRR-style calculation.
- The model does not include a detailed working capital build, balance sheet, or financing fee amortization unless the user requests it.
- PIK interest is compounded annually; semi-annual compounding is not modeled by default.
- No tax shield calculation beyond simple EBT × tax rate is included (no deferred taxes or NOL carryforwards).

**Related Skills in This Repo:**
- `DCF Valuation Builder` — for intrinsic value comparison at entry/exit
- `Debt Capacity Analyzer` — to stress-test leverage before building the LBO
- `M&A Accretion/Dilution Model` — for strategic buyer comparison
- `Comparable Company Analysis` — to validate entry and exit multiples