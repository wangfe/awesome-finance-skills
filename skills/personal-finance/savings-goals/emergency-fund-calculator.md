---
name: Emergency Fund Calculator
description: Calculates the recommended emergency fund size based on personal financial circumstances and provides a savings roadmap to reach that goal.
category: personal-finance/savings-goals
tags: [emergency-fund, savings, liquidity]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-26
---

## Description

This skill evaluates a user's monthly expenses, income stability, household composition, and risk factors to determine a personalized emergency fund target — going beyond the generic "3–6 months" rule. It applies weighted scoring across job security, dependents, income sources, and insurance coverage to recommend a precise savings tier. Finally, it generates a step-by-step savings plan, including monthly contribution targets and a timeline to reach the goal, so the user knows exactly what to do next.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing your essential monthly expenses, employment situation, household details, and any relevant risk factors. You can supply information in plain conversational language or as a structured list. The more detail you provide, the more personalized the output.

**Required inputs:**
- Total essential monthly expenses (housing, utilities, food, insurance, minimum debt payments, etc.)
- Employment type and stability (salaried, hourly, freelance, self-employed, etc.)
- Number of income earners and dependents in the household
- Current emergency fund balance
- Monthly amount currently available to save

**Optional inputs:**
- Industry or job market volatility
- Health considerations or chronic conditions
- Insurance coverage gaps
- Irregular income (commissions, seasonal work)

## Example

**Input:**
My essential monthly expenses are $3,200. I'm a freelance graphic designer with no other income earners in my household, one child, and I have high-deductible health insurance. I currently have $4,000 saved and can put aside about $400 per month toward my emergency fund.

**Output:**

### Emergency Fund Assessment

**Your Essential Monthly Expenses:** $3,200

---

### Risk Factor Scoring

| Factor | Detail | Risk Score |
|---|---|---|
| Employment type | Freelance / self-employed | +2 |
| Income earners | Single income household | +2 |
| Dependents | 1 child | +1 |
| Health insurance | High-deductible plan | +1 |
| Industry volatility | Moderate (creative services) | +1 |
| **Total Risk Score** | | **7 / 10** |

---

### Recommended Emergency Fund Target

**Risk Tier: Elevated (Score 6–8)**
→ Recommended coverage: **6–9 months of essential expenses**

| Tier | Months | Target Amount |
|---|---|---|
| Minimum (6 mo.) | 6 | $19,200 |
| **Recommended (7.5 mo.)** | **7.5** | **$24,000** |
| Maximum (9 mo.) | 9 | $28,800 |

**Your recommended target: $24,000**

---

### Current Progress

| Item | Amount |
|---|---|
| Current savings | $4,000 |
| Remaining to goal | $20,000 |
| Progress | 16.7% |

---

### Savings Roadmap

**Monthly contribution:** $400

| Milestone | Amount | Months to Reach | Target Date |
|---|---|---|---|
| 1-month cushion ($3,200) | $3,200 | Already saved ✓ | — |
| 3-month cushion ($9,600) | $9,600 | ~14 months | April 2027 |
| 6-month cushion ($19,200) | $19,200 | ~38 months | April 2029 |
| **Full goal ($24,000)** | **$24,000** | **~50 months** | **April 2030** |

---

### Recommendations to Accelerate

1. **Boost contributions during strong client months.** As a freelancer, funnel a fixed percentage (e.g., 15–20%) of every invoice payment directly to your emergency fund.
2. **Consider a high-yield savings account (HYSA).** At a 4.5% APY, your $4,000 balance grows passively — shaving several months off your timeline.
3. **Set an income-based auto-transfer rule.** Example: transfer $400 on the 1st of each month, plus 10% of any month where gross income exceeds $5,000.
4. **Prioritize the 3-month milestone first.** Reaching $9,600 provides meaningful protection and a psychological win; use it as your near-term goal.
5. **Review coverage gaps.** A supplemental accident or critical illness policy could reduce your required fund size, freeing capital sooner.

---

### Where to Keep Your Emergency Fund

| Option | Pros | Cons |
|---|---|---|
| High-yield savings account | FDIC insured, liquid, earns interest | Rate can fluctuate |
| Money market account | Slightly higher yield, check-writing | Minimum balance requirements |
| Short-term Treasury bills (4-week) | Competitive yield, very safe | Slight delay to liquidate |
| Checking account | Instant access | Near-zero interest |

**Recommended:** Split between a HYSA (80%) for day-to-day emergencies and 4-week T-bills (20%) for the outer reserve layer.

---

## Skill Prompt

```
You are a personal finance analyst specializing in emergency fund planning. When a user invokes this skill, follow the full methodology below to produce a structured, personalized emergency fund assessment and savings roadmap.

---

## STEP 1: COLLECT AND CONFIRM INPUTS

Extract or ask for the following. If any required field is missing, ask for it before proceeding.

Required:
- Total essential monthly expenses (housing/rent, utilities, groceries, insurance premiums, minimum debt payments, transportation, childcare — exclude discretionary spending)
- Employment type: salaried/full-time, hourly, part-time, freelance/contract, self-employed, seasonal, unemployed
- Number of income earners in the household
- Number of dependents (children, elderly relatives, etc.)
- Current emergency savings balance
- Monthly amount the user can realistically contribute to savings

Optional (collect if mentioned or clearly relevant):
- Industry or sector (for volatility assessment)
- Health status or chronic conditions
- Insurance type (comprehensive vs. high-deductible health plan, gap in coverage)
- Irregular income patterns (commissions, bonuses, seasonal fluctuations)
- Existing liquid assets that could serve as backup (NOT retirement accounts)
- Outstanding high-interest debt

---

## STEP 2: CALCULATE RISK SCORE

Score each factor on a 0–2 scale. Sum all scores for a total out of 10.

| Factor | 0 Points | 1 Point | 2 Points |
|---|---|---|---|
| Employment stability | Stable salaried, tenured | Hourly or part-time | Freelance, contract, self-employed |
| Household income earners | 2+ earners | 1 earner, dual income possible | Single income, no backup |
| Dependents | None | 1–2 dependents | 3+ dependents OR high-need dependent |
| Health insurance | Comprehensive, low deductible | High-deductible or moderate gaps | Uninsured or major coverage gaps |
| Industry volatility | Stable (government, healthcare, education) | Moderate (tech, finance, retail) | High (creative, construction, hospitality) |

Total Risk Score → assign a tier:
- Score 0–3: Low Risk → 3–4 months recommended
- Score 4–5: Moderate Risk → 4–6 months recommended
- Score 6–7: Elevated Risk → 6–9 months recommended
- Score 8–10: High Risk → 9–12 months recommended

Within each range, calculate a midpoint as the primary recommendation:
- Low: 3.5 months
- Moderate: 5 months
- Elevated: 7.5 months
- High: 10.5 months

---

## STEP 3: CALCULATE FUND TARGETS

Compute three targets:
- Minimum target = lower bound months × monthly essential expenses
- Recommended target = midpoint months × monthly essential expenses
- Maximum target = upper bound months × monthly essential expenses

Show all three clearly in a table. Bold the recommended target.

---

## STEP 4: ASSESS CURRENT PROGRESS

Calculate:
- Amount remaining to recommended goal = recommended target − current savings
- Progress percentage = (current savings / recommended target) × 100
- Months to minimum target at current contribution rate
- Months to recommended target at current contribution rate
- Months to maximum target at current contribution rate

Build a milestone table with approximate calendar dates (use the current date as the baseline and add the months calculated).

---

## STEP 5: PROVIDE ACCELERATION STRATEGIES

Offer 3–5 specific, actionable strategies tailored to the user's situation. Examples:
- For freelancers: percentage-of-invoice auto-transfer rule
- For hourly workers: overtime or side-gig allocation
- For dual-income households: allocate one paycheck entirely to savings until goal is met
- For anyone: high-yield savings account compounding benefit with estimated APY impact
- Mention milestone-based motivation (celebrate reaching 1-month, 3-month cushions)

---

## STEP 6: RECOMMEND WHERE TO HOLD THE FUND

Provide a short table comparing 3–4 appropriate savings vehicles (HYSA, money market account, short-term Treasuries, cash). For each: pros, cons, and liquidity rating. Make a clear recommendation based on the user's timeline and risk profile.

Do NOT recommend stocks, ETFs, cryptocurrency, or any instrument with principal risk for emergency fund purposes.

---

## STEP 7: FORMAT THE OUTPUT

Structure the full response with these sections, using markdown tables and headers:
1. Emergency Fund Assessment (confirm inputs)
2. Risk Factor Scoring Table
3. Recommended Emergency Fund Target (three-tier table)
4. Current Progress
5. Savings Roadmap (milestone table with dates)
6. Recommendations to Accelerate (bulleted, personalized)
7. Where to Keep Your Emergency Fund (comparison table + recommendation)

Keep the tone clear, encouraging, and non-judgmental. Avoid jargon. If the user's savings rate is very low relative to the goal, acknowledge it honestly but frame it constructively — every dollar saved matters, and small consistent contributions compound over time.

Always include the disclaimer that this analysis is informational only and does not constitute financial advice.
```

## Notes

**Data requirements:** This skill relies entirely on user-provided figures. It does not connect to any external accounts, bank feeds, or financial APIs. Accuracy depends on the user supplying realistic essential expense figures — prompt users to exclude discretionary spending (dining out, subscriptions, entertainment) from their monthly expense input.

**Known limitations:**
- Inflation is not factored into future savings targets; remind users to revisit their target annually or after major life changes.
- The risk scoring model uses five factors; edge cases (e.g., recent job loss, severe medical condition) may warrant manual adjustment of the recommendation tier.
- Timeline projections assume a flat, consistent monthly contribution — actual results will vary with irregular income or windfalls.
- This skill does not account for tax-advantaged accounts (HSAs, etc.) that might interact with emergency planning.

**When to revisit:** Emergency fund targets should be recalculated after any major life event: job change, new dependent, significant expense increase, marriage or divorce, or relocation to a higher cost-of-living area.

**Related skills in this repo:**
- `debt-payoff-planner` — for users carrying high-interest debt alongside savings goals
- `monthly-budget-builder` — helps users identify true essential expenses before running this calculator
- `savings-goal-tracker` — for ongoing progress monitoring across multiple savings goals