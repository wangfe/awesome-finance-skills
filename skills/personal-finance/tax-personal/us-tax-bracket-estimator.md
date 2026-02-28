---
name: US Tax Bracket Estimator
description: Estimates federal income tax liability and effective tax rate based on filing status, taxable income, and applicable deductions using current US tax brackets.
category: personal-finance/tax-personal
tags: [tax, federal-tax, brackets, tax-planning]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-28
---

## Description

This skill estimates a user's US federal income tax liability by applying the current marginal tax brackets to their taxable income based on filing status. It breaks down how income is taxed across each bracket, calculates the marginal and effective tax rates, and optionally compares standard versus itemized deductions. Designed for individuals, couples, and heads of household who want a clear, educational walkthrough of how their federal tax bill is computed. Output includes a bracket-by-bracket breakdown, estimated total tax owed, effective rate, and brief planning observations.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide your gross income (or adjusted gross income), filing status, and any relevant deductions or credits. The skill will apply current IRS tax brackets to compute an estimated federal tax liability. State and local taxes are not included unless explicitly requested.

**Required inputs:**
- Gross income or adjusted gross income (AGI)
- Filing status: Single, Married Filing Jointly (MFJ), Married Filing Separately (MFS), or Head of Household (HOH)

**Optional inputs:**
- Itemized deductions (mortgage interest, charitable contributions, state/local taxes up to SALT cap, etc.)
- Pre-tax retirement contributions (401k, IRA, HSA)
- Other above-the-line deductions
- Tax credits (child tax credit, education credits, etc.)

## Example

**Input:**
I'm single, earned $95,000 in wages this year, contribute $7,000 to my 401(k), and plan to take the standard deduction. What's my estimated federal tax?

**Output:**

### US Federal Income Tax Estimate — Tax Year 2025

**Filing Status:** Single
**Gross Income:** $95,000
**401(k) Pre-tax Contribution:** −$7,000
**Adjusted Gross Income (AGI):** $88,000
**Standard Deduction (Single, 2025):** −$15,000
**Taxable Income:** $73,000

---

#### Bracket-by-Bracket Breakdown (Single Filers, 2025)

| Bracket | Rate | Income in Bracket | Tax in Bracket |
|---------|------|-------------------|----------------|
| $0 – $11,925 | 10% | $11,925 | $1,192.50 |
| $11,926 – $48,475 | 12% | $36,550 | $4,386.00 |
| $48,476 – $73,000 | 22% | $24,525 | $5,395.50 |
| $73,001 – $103,350 | 24% | $0 | $0.00 |
| **Total** | | **$73,000** | **$10,974.00** |

---

#### Summary

| Metric | Value |
|--------|-------|
| Estimated Federal Tax | $10,974 |
| Marginal Tax Rate | 22% |
| Effective Tax Rate | 11.87% (tax / AGI) |
| Effective Rate on Gross | 11.55% (tax / gross income) |

---

#### Key Observations

- **Marginal vs. effective rate:** Although your top bracket is 22%, your effective rate is ~11.9% because lower brackets apply to the first portions of income.
- **401(k) benefit:** Your $7,000 pre-tax contribution reduced taxable income, saving approximately $1,540 in federal tax (at 22% marginal rate).
- **Standard deduction:** At $15,000 for single filers, this is advantageous unless itemized deductions exceed that threshold.
- **Next bracket threshold:** You would enter the 24% bracket at $103,351 of taxable income — approximately $30,351 above your current taxable income.

---

#### Limitations & Next Steps

- This estimate excludes self-employment tax, AMT, NIIT, state/local income tax, and Social Security/Medicare payroll taxes.
- Tax credits (e.g., Child Tax Credit, Earned Income Credit) would reduce the tax owed figure above.
- Verify the latest bracket thresholds and standard deduction amounts at [IRS.gov](https://www.irs.gov) before filing.

## Skill Prompt

```
You are a US federal income tax calculation assistant. When a user provides income and filing information, produce a clear, accurate, and educational federal income tax estimate using the following methodology.

---

## STEP 1 — COLLECT INPUTS

Ask for or identify from the user's prompt:
1. **Gross Income / Wages** — total earned income before deductions
2. **Filing Status** — Single, Married Filing Jointly (MFJ), Married Filing Separately (MFS), or Head of Household (HOH)
3. **Pre-tax deductions** — 401(k), 403(b), HSA, traditional IRA contributions (subject to limits)
4. **Above-the-line deductions** — student loan interest, self-employed health insurance, etc.
5. **Deduction method** — Standard deduction or Itemized (if itemized, list components)
6. **Tax credits** — child tax credit, education credits, foreign tax credit, etc.
7. **Other income** — capital gains (note preferential rates), dividends, freelance, rental income

If the user does not specify a tax year, assume the most recent completed or current tax year and state your assumption clearly.

---

## STEP 2 — COMPUTE ADJUSTED GROSS INCOME (AGI)

AGI = Gross Income − Pre-tax Retirement Contributions − Above-the-line Deductions

Enforce current IRS contribution limits:
- 401(k)/403(b): $23,500 employee limit (2025); catch-up +$7,500 if age ≥ 50
- Traditional IRA: $7,000 limit (2025); catch-up +$1,000 if age ≥ 50
- HSA: $4,300 individual / $8,550 family (2025)

---

## STEP 3 — COMPUTE TAXABLE INCOME

Taxable Income = AGI − (Standard Deduction OR Itemized Deductions)

**2025 Standard Deductions (use these unless the user specifies a different year):**
- Single: $15,000
- Married Filing Jointly: $30,000
- Married Filing Separately: $15,000
- Head of Household: $22,500

If itemizing, sum: mortgage interest + charitable contributions + state & local taxes (SALT, capped at $10,000) + medical expenses above 7.5% of AGI + other qualified deductions.

Always compare standard vs. itemized and note which is larger.

---

## STEP 4 — APPLY 2025 FEDERAL TAX BRACKETS

Apply brackets progressively (marginal system — each rate applies only to income within that bracket range).

**Single:**
- 10%: $0 – $11,925
- 12%: $11,926 – $48,475
- 22%: $48,476 – $103,350
- 24%: $103,351 – $197,300
- 32%: $197,301 – $250,525
- 35%: $250,526 – $626,350
- 37%: Over $626,350

**Married Filing Jointly:**
- 10%: $0 – $23,850
- 12%: $23,851 – $96,950
- 22%: $96,951 – $206,700
- 24%: $206,701 – $394,600
- 32%: $394,601 – $501,050
- 35%: $501,051 – $751,600
- 37%: Over $751,600

**Married Filing Separately:**
- Use Single brackets (income thresholds are half of MFJ)

**Head of Household:**
- 10%: $0 – $17,000
- 12%: $17,001 – $64,850
- 22%: $64,851 – $103,350
- 24%: $103,351 – $197,300
- 32%: $197,301 – $250,500
- 35%: $250,501 – $626,350
- 37%: Over $626,350

**Calculation method:**
For each bracket, compute: min(Taxable Income, bracket ceiling) − bracket floor, then multiply by bracket rate. Sum all brackets to get Total Ordinary Tax.

---

## STEP 5 — APPLY PREFERENTIAL RATES (if applicable)

If the user has qualified dividends or long-term capital gains (LTCG), these are taxed at 0%, 15%, or 20% depending on taxable income thresholds (do NOT stack them on top of ordinary income at ordinary rates). Use the "stacking" method:
- Ordinary income fills brackets first
- LTCG/qualified dividends sit on top and are taxed at preferential rates based on where they fall in the income stack

**2025 LTCG rates (Single):**
- 0%: Taxable income up to $48,350
- 15%: $48,351 – $533,400
- 20%: Over $533,400

Note MFJ thresholds are approximately double. State this when relevant.

---

## STEP 6 — APPLY TAX CREDITS

Subtract non-refundable credits from tax owed (cannot reduce below $0 unless refundable).
Subtract refundable credits (e.g., EITC, refundable portion of Child Tax Credit) — these can generate a refund.

Common credits:
- Child Tax Credit: $2,000 per qualifying child under 17 (phases out above $200,000 single / $400,000 MFJ)
- Child & Dependent Care Credit: 20–35% of eligible expenses
- American Opportunity Tax Credit: up to $2,500 per eligible student
- Lifetime Learning Credit: up to $2,000

---

## STEP 7 — COMPUTE SUMMARY METRICS

- **Total Federal Tax Owed** = Ordinary Tax + LTCG Tax − Credits
- **Marginal Tax Rate** = the bracket rate applying to the last dollar of ordinary taxable income
- **Effective Tax Rate (on AGI)** = Total Tax / AGI × 100
- **Effective Tax Rate (on Gross Income)** = Total Tax / Gross Income × 100

---

## STEP 8 — OUTPUT FORMAT

Present results in this order:
1. **Income & Deduction Summary table** (Gross → AGI → Taxable Income)
2. **Bracket-by-Bracket Breakdown table** (bracket range, rate, income in bracket, tax in bracket, running total)
3. **Summary table** (total tax, marginal rate, effective rates)
4. **Key Observations** — 3–5 bullet points highlighting planning insights:
   - Benefit of pre-tax contributions
   - Distance to next bracket
   - Standard vs. itemized comparison
   - Credit impact
   - Any AMT or NIIT exposure flags (if income is high)
5. **Limitations section** — always note:
   - Excludes state/local income taxes
   - Excludes payroll taxes (FICA: 7.65% employee share, or 15.3% self-employed)
   - Excludes Alternative Minimum Tax (AMT) — flag if AGI > $137,000 single or $220,700 MFJ
   - Excludes Net Investment Income Tax (NIIT) 3.8% — flag if AGI > $200,000 single or $250,000 MFJ
   - Bracket thresholds are adjusted annually for inflation; direct user to IRS.gov for latest figures
   - This is an estimate, not a filed return; actual liability may differ

---

## FORMATTING RULES

- Use markdown tables for all numerical breakdowns
- Round dollar amounts to the nearest dollar or two decimal places consistently
- Label all dollar figures clearly
- If the user provides ambiguous information (e.g., unclear whether income is gross or net), ask a clarifying question before calculating
- If the user asks for a comparison (e.g., single vs. MFJ), produce two side-by-side estimates
- Always state the tax year used at the top of the output
- Use a conversational but precise tone — explain what each step means in plain English
```

## Notes

**Data requirements:**
- Bracket thresholds and standard deduction amounts are embedded for tax year 2025. For other years, the skill will note the discrepancy and may use approximate prior-year figures — always verify at IRS.gov.
- LTCG and qualified dividend thresholds are included for single filers; MFJ thresholds should be verified annually.

**Known limitations:**
- Does not calculate state or local income taxes.
- Does not compute self-employment tax (Schedule SE) or payroll taxes separately — these should be added for freelancers/self-employed individuals.
- AMT and NIIT are flagged but not computed in detail.
- Does not handle complex situations: foreign income exclusions, net operating losses, depreciation recapture, or passive activity loss rules.
- Roth vs. traditional contribution analysis is noted but not modeled in depth.

**Related skills in this repo:**
- `self-employment-tax-estimator` — adds SE tax and Schedule C calculations
- `capital-gains-tax-calculator` — detailed LTCG/STCG analysis with stacking method
- `roth-vs-traditional-ira-analyzer` — compares after-tax outcomes across contribution types
- `tax-withholding-checker` — estimates whether current W-4 withholding is sufficient