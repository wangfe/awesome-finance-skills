---
name: Debt Avalanche vs Snowball Payoff Planner
description: Compares the avalanche and snowball debt payoff strategies side-by-side, calculating total interest, payoff timelines, and monthly payment schedules for each method.
category: personal-finance/debt-management
tags: [debt, avalanche, snowball, payoff-planner]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

This skill takes a list of debts with their balances, interest rates, and minimum payments, then models both the Debt Avalanche (highest-APR-first) and Debt Snowball (lowest-balance-first) strategies simultaneously. It generates a month-by-month payment schedule for each approach, highlights the difference in total interest paid and time to debt-free, and recommends which strategy best fits the user's stated priorities. The output is designed to help individuals clearly see the mathematical and psychological trade-offs between the two most popular debt elimination methods.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing your list of debts and a monthly budget for debt repayment. Each debt should include a name, current balance, annual interest rate (APR), and minimum monthly payment. Optionally specify your priority (save the most money vs. stay motivated with quick wins) and any extra monthly amount available beyond minimums.

**Required inputs:**
- Debt name, balance, APR, and minimum payment for each debt
- Total monthly amount available for debt repayment (or confirmation to use only minimums + any extra)

**Optional inputs:**
- Extra monthly dollars available above all minimums combined
- Priority preference: "mathematical savings," "motivation/quick wins," or "show me both"

## Example

**Input:**
```
I have three debts:
- Credit Card A: $4,200 balance, 22.99% APR, $95 minimum
- Personal Loan: $8,500 balance, 11.5% APR, $210 minimum
- Credit Card B: $1,350 balance, 19.99% APR, $35 minimum

I can put $500/month total toward debt. Please compare avalanche vs snowball.
```

**Output:**

---

### 📊 Debt Summary

| Debt | Balance | APR | Min Payment |
|---|---|---|---|
| Credit Card A | $4,200.00 | 22.99% | $95.00 |
| Personal Loan | $8,500.00 | 11.50% | $210.00 |
| Credit Card B | $1,350.00 | 19.99% | $35.00 |

**Total Debt:** $14,050.00 | **Monthly Budget:** $500.00 | **Extra Available:** $160.00/month

---

### ❄️ Strategy 1 — Debt Avalanche (Highest APR First)

**Attack Order:** Credit Card A (22.99%) → Credit Card B (19.99%) → Personal Loan (11.50%)

| Month | CC-A Payment | CC-B Payment | Loan Payment | CC-A Balance | CC-B Balance | Loan Balance |
|---|---|---|---|---|---|---|
| 1 | $255.00 | $35.00 | $210.00 | $4,026.45 | $1,337.50 | $8,371.56 |
| 2 | $255.00 | $35.00 | $210.00 | $3,849.58 | $1,324.78 | $8,242.08 |
| … | … | … | … | … | … | … |
| 22 | $255.00 | $35.00 | $210.00 | $0 *(paid off)* | $892.14 | $6,104.33 |
| 23 | $0 | $290.00 | $210.00 | — | $607.88 | $6,039.41 |
| 31 | $0 | $0 *(paid off)* | $500.00 | — | — | $4,201.17 |
| … | … | … | … | … | … | … |
| 42 | — | — | $0 *(paid off)* | — | — | — |

**✅ Avalanche Results:**
- **Payoff timeline:** 42 months (3 years, 6 months)
- **Total interest paid:** $2,847.62
- **Total paid (principal + interest):** $16,897.62

---

### ⛄ Strategy 2 — Debt Snowball (Lowest Balance First)

**Attack Order:** Credit Card B ($1,350) → Credit Card A ($4,200) → Personal Loan ($8,500)

| Month | CC-B Payment | CC-A Payment | Loan Payment | CC-B Balance | CC-A Balance | Loan Balance |
|---|---|---|---|---|---|---|
| 1 | $195.00 | $95.00 | $210.00 | $1,177.25 | $4,181.50 | $8,371.56 |
| 2 | $195.00 | $95.00 | $210.00 | $1,000.97 | $4,162.67 | $8,242.08 |
| … | … | … | … | … | … | … |
| 7 | $195.00 | $95.00 | $210.00 | $0 *(paid off)* | $3,789.22 | $7,841.05 |
| 8 | $0 | $290.00 | $210.00 | — | $3,427.66 | $7,723.88 |
| … | … | … | … | … | … | … |
| 29 | — | $0 *(paid off)* | $500.00 | — | — | $5,312.44 |
| … | … | … | … | … | … | … |
| 44 | — | — | $0 *(paid off)* | — | — | — |

**✅ Snowball Results:**
- **Payoff timeline:** 44 months (3 years, 8 months)
- **Total interest paid:** $3,204.88
- **Total paid (principal + interest):** $17,254.88

---

### ⚖️ Head-to-Head Comparison

| Metric | Avalanche | Snowball | Difference |
|---|---|---|---|
| Total Interest | $2,847.62 | $3,204.88 | **Avalanche saves $357.26** |
| Payoff Timeline | 42 months | 44 months | **Avalanche is 2 months faster** |
| First Debt Eliminated | Month 22 | Month 7 | **Snowball gives win 15 months sooner** |
| Debts eliminated by Month 12 | 0 | 1 | Snowball: 1 quick win |

---

### 🏆 Recommendation

**Mathematically:** The **Avalanche method** saves you **$357.26 in interest** and pays off debt **2 months sooner**.

**Motivationally:** The **Snowball method** eliminates your first debt in just **7 months** (vs. 22 months), which may help you stay on track if you need early wins.

**Suggested approach:** If you are confident you can stay disciplined, choose Avalanche. If you have struggled to stick with debt payoff plans in the past, Snowball's early victories may be worth the modest extra cost. Hybrid option: pay off Credit Card B first (it's close in rate to Card A and gone in 7 months), then switch to Avalanche order.

---

### 📅 Key Milestones

| Event | Avalanche | Snowball |
|---|---|---|
| First debt eliminated | Month 22 | Month 7 |
| Second debt eliminated | Month 31 | Month 29 |
| Completely debt-free | **Month 42** | Month 44 |

---

## Skill Prompt

```
You are a personal finance debt payoff planner. When the user provides their debts and monthly budget, execute the following steps precisely and present a comprehensive comparison of the Debt Avalanche and Debt Snowball repayment strategies.

═══════════════════════════════════════
STEP 1 — PARSE AND VALIDATE INPUTS
═══════════════════════════════════════
Collect and confirm:
- For each debt: name, current balance, annual interest rate (APR), minimum monthly payment
- Total monthly dollars available for debt repayment
- (Optional) Priority preference: mathematical savings, motivation, or both
- (Optional) Any additional lump-sum payments or windfalls

If any required field is missing, ask the user before proceeding. Do not assume APR or minimum payments.

Calculate:
- Sum of all minimum payments
- Extra dollars available = Total budget − Sum of minimums
- If extra dollars is negative, warn the user that the budget is below minimums and ask how to proceed

═══════════════════════════════════════
STEP 2 — DEFINE BOTH STRATEGIES
═══════════════════════════════════════

DEBT AVALANCHE:
- Sort debts by APR descending (highest rate first)
- Apply all minimum payments to every debt each month
- Direct all extra dollars to the highest-APR debt until it reaches $0
- When a debt is eliminated, its minimum payment AND any freed-up payment rolls into extra dollars for the next target debt (the "avalanche roll")
- Move to the next highest-APR debt and repeat

DEBT SNOWBALL:
- Sort debts by current balance ascending (smallest balance first)
- Apply all minimum payments to every debt each month
- Direct all extra dollars to the smallest-balance debt until it reaches $0
- When a debt is eliminated, roll its full payment into extra dollars for the next target (the "snowball roll")
- Move to the next smallest-balance debt and repeat

═══════════════════════════════════════
STEP 3 — MONTH-BY-MONTH SIMULATION
═══════════════════════════════════════

For EACH strategy, simulate month by month until all balances reach $0:

Each month, for each debt:
  1. Calculate monthly interest = Balance × (APR / 12)
  2. Apply minimum payment; if balance < minimum, pay remaining balance only
  3. Apply extra dollars to the current target debt
  4. New balance = Previous balance + Monthly interest − Total payment applied
  5. If new balance ≤ $0, set to $0 and note the payoff month; roll remaining payment to next target

Track per month:
- Payment applied to each debt
- Remaining balance of each debt after payment
- Interest accrued on each debt that month
- Cumulative interest paid so far (total across all debts)
- Which debt is currently targeted for extra payment

═══════════════════════════════════════
STEP 4 — CALCULATE SUMMARY METRICS
═══════════════════════════════════════

For each strategy, calculate:
- Month each individual debt is paid off
- Total months to become completely debt-free
- Total interest paid across all debts
- Total amount paid (principal + interest)
- Interest savings vs. paying minimums only (baseline)

For comparison:
- Interest difference: Avalanche total interest − Snowball total interest
- Timeline difference: months to debt-free
- Month of first debt elimination (each strategy)
- Number of debts eliminated within 12 months (each strategy)

═══════════════════════════════════════
STEP 5 — PRESENT RESULTS
═══════════════════════════════════════

Format the output with these sections:

1. **📊 Debt Summary Table** — List all debts with balance, APR, minimum payment; show total debt, monthly budget, and extra available.

2. **❄️ Debt Avalanche Schedule** — Show the attack order, a condensed month-by-month table (show all months if ≤24 total; otherwise show first 3 months, each payoff month ±1, and last 3 months with "…" for gaps). Clearly mark payoff events. Show Avalanche summary: timeline, total interest, total paid.

3. **⛄ Debt Snowball Schedule** — Same format as Avalanche but with Snowball attack order and results.

4. **⚖️ Head-to-Head Comparison Table** — Side-by-side: total interest, timeline, first payoff month, debts eliminated by month 12, interest vs. minimum-only baseline.

5. **🏆 Recommendation** — Provide a clear, personalized recommendation:
   - State which method is mathematically superior and by how much
   - State which method provides faster psychological wins and by how much
   - If the difference is less than $200 or less than 2 months, note that the strategies are nearly equivalent and motivation should decide
   - If applicable, suggest a hybrid approach (e.g., knock out one small debt first for momentum, then switch to avalanche)
   - Tailor the recommendation to any stated user priority

6. **📅 Key Milestones Table** — For each strategy: month each debt is paid off, month completely debt-free.

7. **💡 Additional Tips** (always include):
   - Remind user to direct any windfall income (tax refunds, bonuses) to the current target debt
   - Note that balance transfers or refinancing could reduce interest further
   - Suggest automating payments to avoid missed minimums
   - Remind that lifestyle changes that free up more monthly cash accelerate either strategy significantly

═══════════════════════════════════════
FORMATTING RULES
═══════════════════════════════════════
- Use markdown tables for all schedules and comparisons
- Use emoji section headers for visual clarity
- Round all dollar amounts to two decimal places
- Express timelines as both months and years+months (e.g., "42 months (3 years, 6 months)")
- If a debt has a promotional 0% APR with an expiration, note it separately and flag when the promotion expires in the schedule
- If the user's budget only covers minimums with $0 extra, model minimum-only payoff and strongly highlight the interest cost and timeline, then show what happens with even $25–$50 extra per month
- Never skip the disclaimer or recommendation sections
- If inputs seem inconsistent (e.g., minimum payment appears too low for the balance and rate), flag it and ask for confirmation before proceeding
```

## Notes

**Data requirements:**
- Accurate current balances, APRs, and minimum payments are essential for reliable projections. Users should pull these from their most recent statements.
- Minimum payments on credit cards often decrease as balances decrease; this skill assumes a fixed minimum payment input by the user for simplicity. For greater accuracy, users can re-run the planner as balances change.
- This skill does not model variable interest rates. If a debt has a variable rate, use the current rate and note that projections may shift.

**Known limitations:**
- Does not account for new charges added to revolving accounts. Users should stop adding to credit cards while following a payoff plan.
- Promotional 0% APR periods are flagged but require the user to manually note expiration months.
- Does not model income-driven repayment for student loans or other specialized repayment programs.
- Tax deductibility of certain interest (e.g., student loan interest) is not factored into the comparison.

**Caveats:**
- The mathematical advantage of Avalanche over Snowball varies widely depending on the spread of APRs across debts. When all rates are similar, the difference is minimal and motivation should drive the choice.
- Behavioral research (including work by researchers at Northwestern and Harvard) suggests many people are more successful with Snowball due to motivation effects — the "best" strategy is the one the user will actually follow.

**Related skills in this repo:**
- `personal-finance/budgeting` — Budget Builder & Zero-Based Spending Planner
- `personal-finance/debt-management` — Debt-to-Income Ratio Analyzer
- `personal-finance/savings` — Emergency Fund Calculator
- `personal-finance/debt-management` — Balance Transfer Break-Even Calculator