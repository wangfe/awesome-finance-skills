---
name: FIRE Number Calculator
description: Calculate your Financial Independence / Retire Early (FIRE) number and years to FI based on savings rate, expenses, and expected returns
category: personal-finance/fire-planning
tags: [fire, financial-independence, retire-early, savings-rate, 4-percent-rule]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Calculates the FIRE number (target nest egg), years to financial independence, and safe withdrawal projections using the 4% rule and variations. Supports all FIRE variants: Lean FIRE, Regular FIRE, Fat FIRE, and Barista FIRE. Produces a roadmap showing savings milestones year-by-year.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. The 4% rule is a historical guideline,
> not a guarantee. Always consult a qualified financial professional for retirement planning.

## Usage

Provide:
- Annual expenses in retirement (current or projected)
- Current net worth / invested assets
- Annual savings (or monthly)
- Expected annual investment return (nominal or real)
- (Optional) FIRE variant preference, current age, target retirement age

## Example

**Input:**
```
Annual retirement expenses: $60,000
Current invested assets: $150,000
Annual savings: $36,000 ($3,000/month)
Expected real return (inflation-adjusted): 5%
Current age: 32
FIRE variant: Regular FIRE (4% withdrawal rate)
```

**Output:**
```
=== FIRE Calculator ===

YOUR FIRE NUMBER
  Annual expenses:    $60,000
  Withdrawal rate:    4.0%
  FIRE number:        $1,500,000  ($60,000 / 0.04)

CURRENT PROGRESS
  Current assets:     $150,000
  Progress to FI:     10.0%
  Remaining gap:      $1,350,000

YEARS TO FIRE
  Annual savings:     $36,000
  Real return:        5.0%
  Years to FIRE:      ~22.4 years  → Retire at age 54.4

YEAR-BY-YEAR ROADMAP
Age  Year  Portfolio Value  Progress
33   2027  $193,500         12.9%
35   2029  $285,214         19.0%
40   2034  $549,227         36.6%
45   2039  $920,173         61.3%
50   2044  $1,346,004       89.7%
54   2048  $1,500,000+      100% 🎉 FIRE!

FIRE VARIANTS COMPARISON
  Lean FIRE  (3% WR):  $2,000,000 needed → +4.8 years
  Regular FIRE (4% WR): $1,500,000 ← your target
  Fat FIRE   (3% WR, 2× expenses): $4,000,000 → +14.6 years
  Barista FIRE ($20K/yr part-time): $1,000,000 needed → reach at age 48

SAFE WITHDRAWAL ANALYSIS
  At $1,500,000 with 4% WR: $60,000/year ✅
  Historical success rate (Trinity Study, 30yr): ~96%
  At 3.5% WR (more conservative): $52,500/year
  At 4.5% WR (more aggressive): $67,500/year
```

## Skill Prompt

```
You are a financial independence planning expert. Help the user calculate their FIRE number and roadmap.

**STEP 1 — FIRE NUMBER**
FIRE Number = Annual Retirement Expenses / Withdrawal Rate
- Standard: 4% rule → multiply expenses by 25
- Conservative: 3.5% → multiply by ~28.6
- Aggressive: 4.5% → multiply by ~22.2

**STEP 2 — YEARS TO FIRE**
Use the future value formula to find when the portfolio reaches the FIRE number:
FV = PV × (1+r)^n + PMT × [((1+r)^n − 1) / r]
Solve for n iteratively (or use the formula analytically if possible).
- PV = current invested assets
- PMT = annual savings
- r = real annual return (nominal return − inflation, or use user-provided real return)
- FV = FIRE number

**STEP 3 — YEAR-BY-YEAR ROADMAP**
Show portfolio value at each age (or every 1–2 years) until FIRE number is reached.
Columns: Age | Year | Portfolio Value | % of FIRE Number.
Mark the FIRE year with 🎉.

**STEP 4 — FIRE VARIANTS**
Show how the FIRE number and years to FI change for:
- Lean FIRE: same expenses but with 3% WR (very conservative)
- Fat FIRE: 2× current expenses at 3% WR
- Barista FIRE: user works part-time covering $X/yr (ask if not provided, assume $20K)
For each: state the FIRE number and estimated age of achievement.

**STEP 5 — SAFE WITHDRAWAL ANALYSIS**
At the calculated FIRE number:
- Show annual income at 3.5%, 4%, and 4.5% withdrawal rates.
- Note the historical 30-year success rate for 4% WR (~96% based on Trinity Study).
- If retirement period > 40 years, suggest using 3.5% WR for greater safety.

**FORMATTING**
- All dollar amounts in thousands or millions as appropriate.
- Clearly state whether returns are real (inflation-adjusted) or nominal.
- If nominal returns are used, note that actual purchasing power will be lower.
```

## Notes

- The 4% rule is based on the Trinity Study (1998) analyzing US stock/bond portfolios 1926–1995. Actual sustainability depends on asset allocation, sequence-of-returns risk, and portfolio flexibility.
- For early retirees (40+ year horizons), a 3–3.5% withdrawal rate is generally recommended.
- Social Security, pensions, or other income sources reduce the required FIRE number — subtract expected annual income from expenses before calculating.
- Does not account for taxes on withdrawals (Roth vs. Traditional accounts can significantly affect the real withdrawal rate).
- Related skills: `skills/personal-finance/budgeting/50-30-20-budget-builder.md`, `skills/tools-and-utilities/calculators/compound-interest-calculator.md`.
