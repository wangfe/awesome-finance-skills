---
name: Compound Interest Calculator
description: Calculate compound interest growth, final balance, and total interest earned for any investment or loan scenario
category: tools-and-utilities/calculators
tags: [compound-interest, calculator, savings, investment, loan, time-value-of-money]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Computes compound interest for savings, investments, or loans. Supports one-time lump sums and regular contributions (monthly/annual). Produces a year-by-year growth table, final balance, total contributions, and total interest earned. Also shows the power of compounding by comparing to simple interest.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Returns are illustrative only; actual
> investment returns vary and are not guaranteed.

## Usage

Provide:
- Principal (initial amount)
- Annual interest rate
- Compounding frequency (daily, monthly, quarterly, annually)
- Time period (years)
- (Optional) Regular contributions and frequency

## Example

**Input:**
```
Principal: $10,000
Annual rate: 7%
Compounding: Monthly
Period: 20 years
Monthly contributions: $500
```

**Output:**
```
=== Compound Interest Calculator ===

INPUTS
  Principal:            $10,000
  Annual Rate:          7.00%
  Compounding:          Monthly (12×/year)
  Period:               20 years
  Monthly Contribution: $500

RESULTS
  Final Balance:        $278,927
  Total Contributions:  $130,000  ($10,000 + $500×240 months)
  Total Interest Earned: $148,927
  Effective Annual Rate: 7.229%

YEAR-BY-YEAR GROWTH
Year  Balance     Contributions  Interest Earned (cumul.)
1     $17,351     $16,000        $1,351
5     $52,282     $40,000        $12,282
10    $113,882    $70,000        $43,882
15    $204,532    $100,000       $104,532
20    $278,927    $130,000       $148,927

SIMPLE INTEREST COMPARISON
  Simple interest (7% on $10,000 only): $24,000 interest
  Compound interest (this scenario):    $148,927 interest
  Compounding advantage:                $124,927

MILESTONE PROJECTIONS
  $50,000 reached:  ~Year 4.8
  $100,000 reached: ~Year 8.5
  $200,000 reached: ~Year 14.2
```

## Skill Prompt

```
You are a financial calculator. Compute compound interest growth with the following precision and structure.

**FORMULAS**

For lump sum only:
  A = P × (1 + r/n)^(n×t)

For lump sum + regular contributions:
  A = P × (1 + r/n)^(n×t) + PMT × [((1 + r/n)^(n×t) − 1) / (r/n)]
  where PMT is the per-period contribution (adjust for contribution frequency vs. compounding frequency)

Variables:
  P = Principal
  r = annual rate (decimal)
  n = compounding periods per year (daily=365, monthly=12, quarterly=4, annually=1)
  t = time in years
  PMT = contribution per compounding period

**OUTPUT STRUCTURE**

1. INPUTS — restate all inputs cleanly.

2. RESULTS
   - Final Balance
   - Total Contributions (principal + all contributions)
   - Total Interest Earned (Final Balance − Total Contributions)
   - Effective Annual Rate (EAR) = (1 + r/n)^n − 1

3. YEAR-BY-YEAR TABLE
   Show balance at years: 1, 2, 3, 5, 7, 10, 15, 20 (or all years if period ≤ 10).
   Columns: Year | Balance | Cumulative Contributions | Cumulative Interest Earned.

4. SIMPLE INTEREST COMPARISON
   Compute simple interest on principal only: SI = P × r × t
   Show the compounding advantage (compound interest earned − simple interest earned).

5. MILESTONE PROJECTIONS (if applicable)
   Estimate when balance crosses $50K, $100K, $200K, $500K, $1M thresholds (only show milestones within the period).

Show all math steps. Format currency in dollars with commas. Round to nearest dollar for balances, 3 decimal places for rates.

If inputs are ambiguous (e.g., "monthly contributions" with "quarterly compounding"), state your assumption clearly.
```

## Notes

- This calculator assumes contributions are made at the beginning of each period (annuity-due). For end-of-period contributions (ordinary annuity), the formula slightly differs — note this if precision matters.
- Inflation-adjusted returns: subtract the inflation rate from the nominal rate to estimate real purchasing power growth (e.g., 7% nominal − 3% inflation = ~4% real return).
- For loan amortization (mortgages, personal loans), use the amortization skill in `skills/tools-and-utilities/calculators/`.
- Related skills: `skills/personal-finance/fire-planning/`, `skills/personal-finance/savings-goals/`.
