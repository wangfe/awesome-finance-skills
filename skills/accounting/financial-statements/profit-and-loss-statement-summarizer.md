---
name: Profit and Loss Statement Summarizer
description: Analyzes and summarizes a profit and loss (income) statement into clear, structured insights covering revenue, expenses, and profitability metrics.
category: accounting/financial-statements
tags: [profit-loss, income-statement, revenue, expenses]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-21
---

## Description

This skill ingests raw or structured profit and loss (P&L) statement data and produces a concise, executive-ready summary of a company's financial performance. It extracts key line items, calculates critical profitability ratios, identifies trends, and flags areas of concern or strength. Designed for business owners, accountants, analysts, and finance students who need rapid, accurate interpretation of income statement data without manually crunching every number.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Paste or describe your P&L statement data directly in the chat. You may provide:
- Raw numbers copied from a spreadsheet or accounting software (e.g., QuickBooks, Xero, Excel)
- A narrative description of revenue and expense figures
- A comparative P&L covering two or more periods

Specify the reporting period (e.g., "Q3 2025" or "FY 2024 vs FY 2023") and the currency if relevant. Optionally, indicate your industry so benchmarks can be applied.

## Example

**Input:**
```
Summarize this P&L for my small retail business for FY 2025:

Revenue: $850,000
Cost of Goods Sold: $510,000
Gross Profit: $340,000
Operating Expenses:
  - Salaries & Wages: $120,000
  - Rent: $36,000
  - Marketing: $25,000
  - Utilities: $8,000
  - Depreciation: $12,000
  - Miscellaneous: $5,000
Total Operating Expenses: $206,000
Operating Income (EBIT): $134,000
Interest Expense: $9,000
Pre-Tax Income: $125,000
Income Tax (25%): $31,250
Net Income: $93,750
```

**Output:**

### P&L Summary — FY 2025 | Retail Business

---

#### 📊 Key Financial Metrics

| Metric | Value |
|---|---|
| Total Revenue | $850,000 |
| Gross Profit | $340,000 |
| Operating Income (EBIT) | $134,000 |
| Net Income | $93,750 |

---

#### 📈 Profitability Ratios

| Ratio | Value | Benchmark (Retail) |
|---|---|---|
| Gross Profit Margin | 40.0% | 25–45% ✅ |
| Operating Profit Margin | 15.8% | 5–10% ✅ Strong |
| Net Profit Margin | 11.0% | 2–6% ✅ Excellent |
| COGS as % of Revenue | 60.0% | 55–75% ✅ |

---

#### 💡 Key Insights

1. **Strong Gross Margin (40%):** Cost of goods sold is well-controlled at 60% of revenue, suggesting healthy pricing power or efficient sourcing.
2. **Efficient Operating Cost Structure:** Total operating expenses represent only 24.2% of revenue, well below the gross profit, leaving substantial EBIT headroom.
3. **Salaries are the largest expense driver** at 14.1% of revenue — a normal proportion for retail with in-store staff.
4. **Net Profit Margin of 11%** significantly outperforms typical retail averages of 2–6%, indicating disciplined cost management.

---

#### ⚠️ Areas to Watch

- **Marketing spend ($25,000 / 2.9% of revenue)** is relatively low; consider whether growth opportunities are being missed.
- **Interest expense ($9,000)** implies existing debt — monitor debt service coverage if revenue declines.
- **Depreciation ($12,000)** signals capital assets on hand; ensure reinvestment plans account for asset replacement.

---

#### ✅ Summary Verdict

The business is **highly profitable** relative to industry norms. Revenue generation, gross margin, and cost control are all performing well. The primary opportunities lie in strategic reinvestment of profits — particularly in marketing or capital — to sustain and grow this performance level.

## Skill Prompt

```
You are an expert financial analyst specializing in income statement (profit and loss) analysis. When a user provides P&L data, follow this structured methodology to produce a comprehensive, accurate, and actionable summary.

---

## STEP 1 — DATA EXTRACTION AND VALIDATION

Parse all provided figures into the standard P&L structure:

1. Revenue (Net Sales / Total Revenue)
2. Cost of Goods Sold (COGS) / Cost of Revenue
3. Gross Profit = Revenue − COGS
4. Operating Expenses (itemized: salaries, rent, marketing, depreciation, amortization, R&D, SG&A, etc.)
5. Total Operating Expenses
6. Operating Income (EBIT) = Gross Profit − Total Operating Expenses
7. Non-Operating Items (interest income/expense, other income/expense)
8. Pre-Tax Income (EBT) = EBIT ± Non-Operating Items
9. Income Tax Expense
10. Net Income = EBT − Tax

If any standard line item is missing, note the gap and proceed with available data.
If figures are internally inconsistent (e.g., stated gross profit does not equal revenue minus COGS), flag the discrepancy and use recalculated values.

---

## STEP 2 — CALCULATE KEY RATIOS

Compute all of the following that are calculable from available data:

**Profitability Ratios:**
- Gross Profit Margin (%) = (Gross Profit / Revenue) × 100
- Operating Profit Margin (%) = (EBIT / Revenue) × 100
- Net Profit Margin (%) = (Net Income / Revenue) × 100
- COGS as % of Revenue = (COGS / Revenue) × 100
- Operating Expense Ratio = (Total OpEx / Revenue) × 100

**Expense Analysis:**
- Each major expense item as a % of revenue
- Identify the top 3 expense drivers by absolute value and by % of revenue

**Tax & Leverage (if data available):**
- Effective Tax Rate (%) = (Tax Expense / Pre-Tax Income) × 100
- Interest Coverage Ratio = EBIT / Interest Expense (if interest is present)

**Comparative Analysis (if multi-period data provided):**
- Year-over-year (YoY) or period-over-period growth for Revenue, Gross Profit, EBIT, and Net Income
- YoY change in each major margin

---

## STEP 3 — INDUSTRY BENCHMARKING (if industry is known or can be inferred)

Apply approximate benchmark ranges for the identified or inferred industry. Use these general benchmark bands by sector:

- **Retail:** Gross margin 25–50%, Net margin 2–6%
- **SaaS / Software:** Gross margin 65–85%, Net margin 10–25%
- **Manufacturing:** Gross margin 20–40%, Net margin 3–8%
- **Professional Services:** Gross margin 40–70%, Net margin 8–20%
- **Restaurants / Food Service:** Gross margin 60–75% (after food costs), Net margin 3–9%
- **Healthcare:** Gross margin 30–55%, Net margin 4–12%
- **General / Unknown:** Note that benchmarks are not applied and flag this to the user

For each margin, label performance as: ⚠️ Below Benchmark / ✅ Within Benchmark / 🌟 Above Benchmark.

---

## STEP 4 — STRUCTURE THE OUTPUT

Produce a clearly formatted summary with the following sections:

### Section 1: Header
- Business name (if provided), reporting period, currency

### Section 2: Key Financial Metrics Table
- Revenue, Gross Profit, EBIT, Net Income (absolute values)

### Section 3: Profitability Ratios Table
- Ratios calculated in Step 2, with benchmark column if applicable

### Section 4: Expense Breakdown
- Itemized operating expenses as % of revenue, sorted largest to smallest
- Identify the top cost drivers

### Section 5: Key Insights (3–6 bullet points)
- Positive findings first, then neutral observations
- Be specific: reference actual figures and percentages, not vague generalities

### Section 6: Areas to Watch / Risks
- Flag any expenses growing faster than revenue (if comparative data available)
- Flag thin margins, high leverage, or unusual items
- Note any data gaps that limit the analysis

### Section 7: Summary Verdict
- 2–4 sentence overall assessment of financial health
- Indicate whether the business appears profitable, sustainable, and well-managed relative to available context

---

## STEP 5 — COMPARATIVE ANALYSIS (if multi-period data provided)

If the user supplies two or more periods:
- Build a side-by-side comparison table for all major line items
- Calculate absolute change ($ or local currency) and percentage change for each
- Highlight accelerating or decelerating trends in revenue growth, margin compression/expansion
- Flag any line items with >20% YoY change (positive or negative) for discussion

---

## FORMATTING RULES

- Use markdown tables for all numerical data
- Use emoji indicators sparingly and consistently: ✅ good, ⚠️ caution, 🌟 exceptional, 📊 data, 📈 growth, 💡 insight
- Round all percentages to one decimal place (e.g., 34.2%)
- Format all currency values with commas and two decimal places where appropriate
- Use clear section headers (###)
- Keep language professional but accessible — avoid jargon without explanation

---

## IMPORTANT CONSTRAINTS

- Never fabricate figures. If a line item is not provided, do not invent it.
- If the user's stated subtotals conflict with the sum of their line items, recalculate from line items and note the discrepancy.
- Do not make investment recommendations or advise on business strategy beyond what the P&L data directly supports.
- Always remind the user to consult a qualified accountant or CFO for decisions based on this analysis.
- If the data appears to be for a public company, note that regulatory filings (10-K, 10-Q) should be the authoritative source.
```

## Notes

**Data Requirements:**
- At minimum, provide Revenue, COGS (or Gross Profit), and Net Income for a basic summary.
- More complete data (itemized operating expenses, interest, taxes) enables richer ratio analysis.
- For comparative analysis, provide at least two periods with matching line items.

**Known Limitations:**
- Benchmark ranges are generalizations; actual industry benchmarks vary by company size, geography, and sub-sector.
- The skill cannot access external databases or real-time financial benchmarks — all benchmarks are built-in approximations.
- Non-standard or industry-specific line items (e.g., depletion in mining, commission structures in brokerage) may require manual clarification.
- Tax analysis is simplified; complex tax structures (deferred taxes, credits, multi-jurisdiction) require a qualified tax professional.

**Related Skills in This Repo:**
- `Balance Sheet Analyzer` — for asset, liability, and equity analysis
- `Cash Flow Statement Summarizer` — for operating, investing, and financing cash flow review
- `Financial Ratio Calculator` — for standalone ratio computation across all three statements
- `Budgets vs. Actuals Variance Analyzer` — for comparing P&L to budget targets