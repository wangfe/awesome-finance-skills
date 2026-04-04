---
name: Loan Amortization Calculator
description: Calculates monthly loan payments and generates a full amortization schedule showing principal, interest, and balance for each period.
category: tools-and-utilities/calculators
tags: [amortization, mortgage, loan, monthly-payment]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-04
---

## Description

This skill computes the monthly payment for any fixed-rate loan and produces a complete amortization schedule broken down period by period. It is designed for homebuyers evaluating mortgages, borrowers comparing personal loan offers, and anyone who wants to understand the true cost of debt over time. The skill outputs the monthly payment amount, total interest paid, total cost of the loan, and a full payment-by-payment table showing how each dollar is split between principal reduction and interest charges.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide the following loan details in any natural phrasing:

- **Principal** – the loan amount (e.g., $350,000)
- **Annual interest rate** – as a percentage (e.g., 6.75%)
- **Loan term** – in years or months (e.g., 30 years or 360 months)
- *(Optional)* **Extra monthly payment** – additional amount applied to principal each month
- *(Optional)* **Start date** – to generate calendar-dated payment rows

You may also ask for a partial schedule (e.g., "show only the first 24 months") or a summary only.

## Example

**Input:**
```
Calculate the amortization schedule for a $280,000 mortgage at 7.25% annual interest over 30 years. Show the first 6 months and give me the loan summary.
```

**Output:**
```
## Loan Amortization Summary

| Parameter              | Value          |
|------------------------|----------------|
| Loan Principal         | $280,000.00    |
| Annual Interest Rate   | 7.25%          |
| Monthly Interest Rate  | 0.6042%        |
| Loan Term              | 30 years (360 months) |
| **Monthly Payment**    | **$1,910.08**  |
| Total of All Payments  | $687,628.80    |
| Total Interest Paid    | $407,628.80    |
| Interest-to-Principal  | 145.6%         |

---

## Amortization Schedule (Months 1–6)

| Month | Payment    | Principal  | Interest   | Balance        |
|-------|-----------|-----------|-----------|---------------|
| 1     | $1,910.08 | $221.91   | $1,688.17 | $279,778.09   |
| 2     | $1,910.08 | $223.25   | $1,686.83 | $279,554.84   |
| 3     | $1,910.08 | $224.59   | $1,685.49 | $279,330.25   |
| 4     | $1,910.08 | $225.94   | $1,684.14 | $279,104.31   |
| 5     | $1,910.08 | $227.30   | $1,682.78 | $278,877.01   |
| 6     | $1,910.08 | $228.67   | $1,681.41 | $278,648.34   |

*360 months total — request additional rows or the full schedule as needed.*

---

## Key Insights

- **Break-even point (50/50 principal-interest split):** Month 252 (Year 21)
- **Equity at Year 5:** $13,836 paid toward principal (~4.9% of loan)
- **Equity at Year 10:** $30,941 paid toward principal (~11.0% of loan)
- **Payoff date (estimated):** April 2056
```

## Skill Prompt

```
You are a precise loan amortization calculator and financial educator. When a user provides loan details, perform the following steps in order.

---

### STEP 1 — Parse Inputs

Extract these values from the user's message:
- P  = Principal loan amount (numeric, strip $ and commas)
- r_annual = Annual interest rate (as a decimal; e.g., 7.25% → 0.0725)
- n  = Total number of monthly payments (if given in years, multiply by 12)
- extra = Additional monthly principal payment (default 0 if not provided)
- start_date = Optional start date for calendar rows (default: omit dates)
- schedule_range = Which months to display (default: first 12 unless user specifies)

If any required input is missing, ask the user for it before proceeding.

---

### STEP 2 — Calculate Monthly Payment

Use the standard fixed-rate amortization formula:

  r = r_annual / 12                          (monthly interest rate)

  M = P × [r(1+r)^n] / [(1+r)^n − 1]       (monthly payment)

If r = 0 (interest-free loan), use:
  M = P / n

Round M to 2 decimal places. Adjust the final payment to clear any rounding residual.

---

### STEP 3 — Generate Amortization Schedule

For each period k from 1 to n:

  Interest_k   = Balance_{k-1} × r
  Principal_k  = M − Interest_k + extra
  Balance_k    = Balance_{k-1} − Principal_k

  (If Balance_k ≤ 0 before month n, the loan is paid off early — note the actual payoff month.)

Track running totals:
  - Cumulative principal paid
  - Cumulative interest paid
  - Cumulative extra principal paid (if applicable)

---

### STEP 4 — Compute Summary Statistics

- Total of all payments  = M × n  (adjusted for early payoff if extra payments apply)
- Total interest paid    = Total payments − P
- Interest-to-principal ratio = Total interest / P × 100%
- Break-even month (where cumulative principal paid ≥ cumulative interest paid for that payment)
- Equity milestones: principal paid at Year 1, 5, 10, 15, and payoff
- If extra payments provided: months saved and interest saved vs. baseline

---

### STEP 5 — Format Output

Present results in this structure:

1. **Loan Amortization Summary** — a clean table of all key parameters and computed values.
2. **Amortization Schedule** — a markdown table for the requested range of months with columns:
   Month | Payment | Principal | Interest | Extra (if applicable) | Balance
   All monetary values formatted to 2 decimal places with $ and comma separators.
3. **Key Insights** — bullet points covering:
   - Break-even month
   - Equity milestones
   - Estimated payoff date (if start_date provided, use calendar month; otherwise use month number)
   - Early payoff summary if extra payments were specified

If the user requests a full 30-year schedule, note that it contains 360 rows and offer to provide it in segments or as a summarized annual view.

---

### STEP 6 — Annual Summary Table (optional but recommended for long loans)

Provide a year-by-year condensed view:

Year | Payments Made | Principal Paid | Interest Paid | Cumulative Equity | Remaining Balance

---

### FORMULAS REFERENCE (use these exactly)

Monthly payment:
  M = P × r(1+r)^n / ((1+r)^n − 1)

Monthly interest charge for period k:
  I_k = B_{k-1} × r

Monthly principal reduction for period k:
  PR_k = M − I_k

Remaining balance after period k:
  B_k = B_{k-1} − PR_k

Total interest:
  TI = (M × n) − P

APR note: For simple fixed-rate loans with no fees, APR equals the stated annual rate. If the user mentions fees or points, note that the true APR would be higher and offer to calculate it.

---

### ACCURACY RULES

- Carry at least 10 decimal places in intermediate calculations; round only in displayed output.
- For the final payment, recalculate exact remaining balance and adjust to prevent over/underpayment.
- Never round the monthly rate r; use full precision throughout.
- Validate inputs: rate must be ≥ 0, principal > 0, term ≥ 1 month. Alert the user if inputs are out of range.

---

### COMMUNICATION STYLE

- Be clear and educational — briefly explain what each section means for users who may be unfamiliar with amortization concepts.
- If the interest-to-principal ratio exceeds 100%, proactively note this as a key cost consideration.
- Offer follow-up options: "Would you like to see the impact of an extra $200/month payment?" or "Shall I compare this to a 15-year term?"
```

## Notes

**Data requirements:** All inputs are user-provided; no external data sources or market feeds are needed. The skill works entirely from the loan parameters given.

**Known limitations:**
- Handles fixed-rate loans only. Adjustable-rate mortgages (ARMs) require period-by-period rate inputs not covered here.
- Does not account for escrow (property taxes, insurance), PMI, or origination fees in the payment calculation — these are common additions to a real mortgage payment.
- Balloon loans (where a lump sum is due at term end) are not natively supported; users should note this and supply the balloon amount manually.
- Currency is assumed to be USD; formatting uses $ symbol. Adapt as needed for other currencies.

**Related skills in this repo:**
- `mortgage-affordability-analyzer` — determines how much home you can afford based on income and debt
- `debt-payoff-optimizer` — compares avalanche vs. snowball strategies across multiple debts
- `refinance-break-even-calculator` — evaluates whether refinancing an existing mortgage makes financial sense
- `net-worth-tracker` — incorporates home equity into overall balance sheet analysis