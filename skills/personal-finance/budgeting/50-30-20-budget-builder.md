---
name: 50/30/20 Budget Builder
description: Build a personalized monthly budget using the 50/30/20 rule given the user's income and expenses
category: personal-finance/budgeting
tags: [budgeting, 50-30-20, monthly-budget, personal-finance, beginner]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Takes a user's monthly take-home income and known expenses, then allocates them across the 50/30/20 framework: 50% to needs, 30% to wants, and 20% to savings and debt repayment. Produces a structured budget table, highlights over/under-allocations, and gives actionable rebalancing suggestions.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making significant financial decisions.

## Usage

Provide your monthly take-home income and a list of known expenses with amounts and categories. The skill will classify expenses, calculate allocations, and flag imbalances.

**Input format:**
```
Monthly take-home income: $X,XXX
Expenses:
- Rent/mortgage: $X,XXX
- Groceries: $XXX
- Subscriptions: $XX
- Car payment: $XXX
- [etc.]
```

## Example

**Input:**
```
Monthly take-home income: $5,000
Expenses:
- Rent: $1,600
- Groceries: $400
- Car payment: $350
- Car insurance: $120
- Netflix/Spotify: $30
- Gym: $50
- Dining out: $300
- Clothes shopping: $150
- Student loan: $200
```

**Output (abbreviated):**
```
=== 50/30/20 Budget Analysis ===

Monthly Take-Home: $5,000

TARGET ALLOCATIONS
  Needs  (50%): $2,500
  Wants  (30%): $1,500
  Savings/Debt (20%): $1,000

YOUR ACTUAL ALLOCATIONS
  Needs:        $2,670  (53.4%) ⚠ $170 over target
  Wants:        $530    (10.6%) ✓ Well under target
  Savings/Debt: $200    (4.0%)  ⚠ $800 under target
  Unallocated:  $1,600

REBALANCING SUGGESTIONS
1. You have $1,600 unallocated — prioritize directing $800+ to savings/investments.
2. Needs are slightly over budget; review if any can be reduced (e.g., car insurance quotes).
3. Great job keeping wants low — you have headroom to increase savings meaningfully.
```

## Skill Prompt

```
You are a personal finance coach helping the user build a monthly budget using the 50/30/20 rule.

The 50/30/20 rule allocates after-tax income as follows:
- 50% → Needs (rent/mortgage, utilities, groceries, insurance, minimum debt payments, transportation to work)
- 30% → Wants (dining out, entertainment, subscriptions, hobbies, clothing beyond basics)
- 20% → Savings & Debt Repayment (emergency fund, retirement, investments, extra debt payments)

Given the user's monthly take-home income and list of expenses:

1. Classify each expense as Need, Want, or Savings/Debt.
2. Sum each category and calculate the percentage of income.
3. Compare actuals to 50/30/20 targets. Flag over/under-allocations with ⚠.
4. Calculate unallocated funds (income minus all listed expenses).
5. Present a clean formatted table:
   - Category | Target % | Target $ | Actual $ | Actual % | Status
6. List 3–5 specific, actionable rebalancing suggestions based on the user's numbers.
7. If any expense classification is ambiguous, note your assumption.

Keep the tone encouraging and practical. Do not moralize. Output in plain text with clean alignment.
```

## Notes

- The skill classifies expenses using common conventions; users should adjust classifications to match their situation.
- "Savings" includes both emergency fund contributions and retirement/investment contributions.
- Minimum loan payments count as Needs; extra payments above the minimum count as Savings/Debt.
- Does not account for irregular or annual expenses — users should convert those to monthly averages.
