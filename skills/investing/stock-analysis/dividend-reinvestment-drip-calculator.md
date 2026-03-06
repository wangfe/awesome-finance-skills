---
name: Dividend Reinvestment (DRIP) Calculator
description: Projects the long-term wealth-building impact of reinvesting dividends automatically, showing compound growth over time across customizable scenarios.
category: investing/stock-analysis
tags: [dividends, drip, reinvestment, compound-growth]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-06
---

## Description

This skill calculates the projected value of a dividend reinvestment plan (DRIP) over a user-defined time horizon, modeling how reinvested dividends compound alongside share price appreciation. It is designed for income investors and long-term equity holders who want to understand the snowball effect of continuous dividend reinvestment. The skill produces a year-by-year table of shares owned, dividends received, portfolio value, and cumulative return, along with a comparison against a non-reinvestment baseline. Users can optionally model dividend growth rates, share price appreciation, and tax drag on dividends.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing the following inputs, either in a structured list or natural language:

- **Initial investment** (dollar amount or number of shares + share price)
- **Current dividend yield** (annual, as a percentage)
- **Investment time horizon** (years)
- **Expected annual share price appreciation** (%, or 0 for static price)
- **Expected annual dividend growth rate** (%, optional — defaults to 0)
- **Tax rate on dividends** (%, optional — defaults to 0 for tax-advantaged accounts)
- **Additional periodic contributions** (optional — monthly or annual dollar amount)

The skill will output a year-by-year projection table, key summary statistics, and a comparison of DRIP vs. no-reinvestment scenarios.

## Example

**Input:**
I want to model a DRIP for Johnson & Johnson. I'm starting with $25,000, the current dividend yield is 3.2%, I expect 5% annual share price appreciation and 4% annual dividend growth. My time horizon is 20 years. Assume I'm in a taxable account with a 15% qualified dividend tax rate. No additional contributions.

**Output:**

### DRIP Projection Summary — Johnson & Johnson (Illustrative)

**Assumptions**
| Parameter | Value |
|---|---|
| Initial Investment | $25,000.00 |
| Starting Dividend Yield | 3.20% |
| Annual Price Appreciation | 5.00% |
| Annual Dividend Growth Rate | 4.00% |
| Dividend Tax Rate | 15.00% |
| After-Tax Yield (Year 1) | 2.72% |
| Time Horizon | 20 Years |
| Additional Contributions | None |

---

### Year-by-Year Projection (Selected Years)

| Year | Share Price | Shares Owned | Annual Dividend/Share | Gross Dividends | After-Tax Divs Reinvested | Portfolio Value |
|---|---|---|---|---|---|---|
| 0 | $100.00 | 250.00 | $3.20 | $800.00 | — | $25,000.00 |
| 1 | $105.00 | 256.48 | $3.33 | $853.87 | $725.79 | $26,930.40 |
| 2 | $110.25 | 263.17 | $3.46 | $910.77 | $774.15 | $29,024.99 |
| 5 | $127.63 | 285.91 | $3.89 | $1,112.39 | $945.53 | $36,497.82 |
| 10 | $162.89 | 327.14 | $4.74 | $1,550.64 | $1,318.04 | $53,289.74 |
| 15 | $207.89 | 376.02 | $5.76 | $2,166.00 | $1,841.10 | $78,175.23 |
| 20 | $265.33 | 433.91 | $7.01 | $3,041.83 | $2,585.56 | $115,119.44 |

*(Full year-by-year table provided in complete output)*

---

### Terminal Value Comparison (Year 20)

| Scenario | Portfolio Value | Total Dividends Received | Total Return |
|---|---|---|---|
| **DRIP (Reinvested, After-Tax)** | **$115,119** | $44,230 (reinvested) | **+360.5%** |
| Price Appreciation Only (No DRIP) | $82,993 | $44,230 (taken as cash) | +231.9% |
| No Appreciation, No DRIP | $25,000 | $44,230 (taken as cash) | +176.9% (cash only) |

**DRIP Advantage over No-Reinvestment:** +$32,126 (+38.7% more terminal wealth)

---

### Key Metrics
- **Compound Annual Growth Rate (DRIP scenario):** 7.94%
- **Dividend Income in Final Year:** $3,042 gross / $2,586 after-tax
- **Total Shares Accumulated:** 433.91 (vs. 250.00 initial)
- **Share Count Growth:** +73.6% purely from reinvestment
- **Break-Even Year vs. No-DRIP:** Year 4

---

### Observations
1. **Reinvestment compounding** contributes ~$32K of the terminal value beyond a no-DRIP strategy.
2. **Dividend growth** (4%/yr) causes income to more than double over 20 years, accelerating reinvestment in later years.
3. **Tax drag** at 15% reduces reinvested capital by ~$8,700 cumulatively vs. a tax-advantaged account — consider maximizing IRA/401(k) allocations for DRIP holdings.
4. The **snowball effect** becomes most pronounced after Year 12 as accumulated share count meaningfully exceeds the initial position.

---

## Skill Prompt

```
You are a quantitative finance assistant specializing in dividend reinvestment plan (DRIP) analysis. When a user invokes this skill, collect or infer the following parameters:

REQUIRED INPUTS:
1. initial_investment: Dollar amount invested (or shares × price)
2. starting_yield: Annual dividend yield as a percentage (e.g., 3.2 for 3.2%)
3. time_horizon: Number of years to project
4. price_appreciation: Expected annual share price growth rate (%)

OPTIONAL INPUTS (use defaults if not provided):
5. dividend_growth_rate: Annual dividend per share growth rate (%, default: 0)
6. tax_rate: Tax rate applied to dividends before reinvestment (%, default: 0)
7. additional_contribution: Extra dollars added per year or month (default: 0)
8. contribution_frequency: "annual" or "monthly" (default: annual)
9. ticker or company name: For labeling purposes only

If any required input is missing, ask the user before proceeding.

---

CALCULATION METHODOLOGY:

Define variables:
- P_0 = initial share price = initial_investment / initial_shares
  (If only dollar amount given, assume P_0 = 100 as a normalized price unless actual price provided)
- N_0 = initial_investment / P_0  [initial shares]
- y_0 = starting_yield / 100  [decimal yield]
- g_d = dividend_growth_rate / 100  [dividend growth rate]
- g_p = price_appreciation / 100  [price appreciation rate]
- t = tax_rate / 100  [tax rate on dividends]
- C = additional annual contribution in dollars

For each year i from 1 to time_horizon:

1. SHARE PRICE:
   P_i = P_(i-1) × (1 + g_p)

2. DIVIDEND PER SHARE (DPS):
   DPS_i = DPS_(i-1) × (1 + g_d)
   where DPS_0 = P_0 × y_0

3. GROSS DIVIDENDS RECEIVED:
   GrossDivs_i = N_(i-1) × DPS_i

4. AFTER-TAX DIVIDENDS AVAILABLE FOR REINVESTMENT:
   AfterTaxDivs_i = GrossDivs_i × (1 - t)

5. NEW SHARES PURCHASED VIA DRIP:
   NewShares_i = AfterTaxDivs_i / P_i

6. NEW SHARES FROM ADDITIONAL CONTRIBUTIONS:
   ContribShares_i = C / P_i  (if annual contribution C > 0)
   (If monthly: C_monthly = C/12, and aggregate over year at mid-year price)

7. TOTAL SHARES AT END OF YEAR i:
   N_i = N_(i-1) + NewShares_i + ContribShares_i

8. PORTFOLIO VALUE AT END OF YEAR i:
   V_i = N_i × P_i

9. CUMULATIVE RETURN:
   CumReturn_i = (V_i - initial_investment) / initial_investment × 100%

CAGR CALCULATION:
   CAGR = (V_final / initial_investment)^(1 / time_horizon) - 1

NO-DRIP BASELINE (for comparison):
   - Shares remain constant at N_0 throughout
   - Portfolio value = N_0 × P_i at each year
   - Dividends are tracked as cumulative cash received (after tax)
   - Total no-DRIP wealth = portfolio value + cumulative cash dividends

DRIP ADVANTAGE:
   DRIPAdvantage = V_final(DRIP) - V_final(price_only_no_drip)
   Express as both dollar amount and percentage of no-DRIP terminal value.

---

OUTPUT FORMAT:

1. **Assumptions Table** — echo back all inputs clearly, including derived values (e.g., after-tax yield, DPS year 1).

2. **Year-by-Year Table** — show all years if time_horizon ≤ 15; show years 0, 1, 2, 3, 5, 7, 10, 15, 20 (and any milestone years) if horizon > 15. Columns:
   - Year
   - Share Price
   - Shares Owned (end of year)
   - DPS (Dividend Per Share)
   - Gross Dividends
   - After-Tax Divs Reinvested
   - Portfolio Value

3. **Terminal Value Comparison Table** — Three rows:
   a. DRIP with reinvestment (after-tax)
   b. Price appreciation only, dividends taken as cash (after-tax)
   c. (Optional) No appreciation, no DRIP — if user wants a pure dividend-cash scenario
   Show: Terminal Portfolio Value, Cumulative Dividends Received, Total Return %, DRIP Advantage.

4. **Key Metrics Block:**
   - CAGR (DRIP scenario)
   - Final year dividend income (gross and after-tax)
   - Total shares accumulated and % growth from reinvestment
   - Break-even year: first year DRIP portfolio value exceeds No-DRIP total wealth
   - Tax drag: cumulative dividends lost to taxes

5. **Observations (3–5 bullet points):**
   - Highlight the most important insights: compounding inflection point, dividend growth contribution, tax efficiency recommendation, comparison context.
   - Flag if assumptions appear aggressive (e.g., yield > 8% may signal elevated risk, growth rate > 7% is historically high).

---

EDGE CASES AND VALIDATION:
- If dividend yield > 8%, add a warning: "High yields may indicate elevated payout risk. Verify dividend sustainability."
- If dividend_growth_rate > price_appreciation, note this implies the payout ratio is expanding, which has limits.
- If time_horizon > 40 years, add a note about inflation not being modeled.
- If tax_rate = 0 and context suggests a taxable account, ask the user to confirm or note the assumption.
- Always show calculations to at least 2 decimal places for share counts, 2 decimal places for currency.
- Never extrapolate past stock performance as a guarantee of future results.

---

TONE AND STYLE:
- Be precise and quantitative; show all formulas on request.
- Present tables in clean markdown format.
- Highlight the compounding story — the skill's core value is demonstrating how reinvestment creates exponential, not linear, growth.
- Always include the disclaimer that projections are illustrative only.
```

## Notes

**Data Requirements:**
- All inputs are user-provided projections; the skill does not fetch live market data, current dividend yields, or historical DPS growth rates. Users should verify current yield and dividend history from sources such as company investor relations pages, Morningstar, or financial data providers.
- For realistic dividend growth assumptions, users may reference a company's 5- or 10-year dividend CAGR.

**Known Limitations:**
- Does not model dividend cuts, suspensions, or irregular payment schedules.
- Does not account for inflation (real vs. nominal returns).
- Assumes dividends are reinvested once per year at year-end price; in practice, quarterly reinvestment at quarterly prices will differ slightly (generally favorably due to dollar-cost averaging).
- Does not model transaction costs or DRIP enrollment fees (most modern brokers offer fee-free DRIP).
- Share price appreciation is modeled as a constant annual rate; actual returns are volatile and path-dependent.

**Related Skills in This Repository:**
- `dividend-yield-analyzer` — for evaluating whether a dividend is sustainable before projecting it forward.
- `portfolio-income-projector` — for modeling dividend income across a multi-stock portfolio.
- `tax-efficient-investing-guide` — for guidance on account placement (Roth IRA vs. taxable) to minimize dividend tax drag.
- `stock-total-return-calculator` — for comparing DRIP total return against price-only benchmarks.