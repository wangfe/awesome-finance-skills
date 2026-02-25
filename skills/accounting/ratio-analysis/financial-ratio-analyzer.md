---
name: Financial Ratio Analyzer
description: Calculate and interpret the full suite of financial ratios from a company's income statement, balance sheet, and cash flow statement
category: accounting/ratio-analysis
tags: [financial-ratios, fundamental-analysis, accounting, liquidity, profitability, solvency]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Takes raw financial statement data and computes liquidity, profitability, efficiency, leverage, and market ratios. Each ratio is interpreted against industry benchmarks with a green/yellow/red signal, and a summary health assessment is provided.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or business decisions.

## Usage

Paste or type the key line items from the company's most recent annual financials:
- Income Statement: Revenue, Gross Profit, EBIT, Net Income, Interest Expense
- Balance Sheet: Current Assets, Current Liabilities, Inventory, Total Assets, Total Equity, Total Debt, Cash
- Cash Flow: Operating Cash Flow, Capital Expenditure

## Example

**Input:**
```
Company: RetailCo Inc.
Revenue: $500M
Gross Profit: $200M
EBIT: $60M
Net Income: $40M
Interest Expense: $10M
Current Assets: $120M
  of which Inventory: $50M
  of which Cash: $20M
Current Liabilities: $80M
Total Assets: $400M
Total Equity: $180M
Total Debt: $150M
Operating Cash Flow: $55M
Capital Expenditure: $20M
```

**Output (abbreviated):**
```
=== Financial Ratio Analysis: RetailCo Inc. ===

LIQUIDITY RATIOS
  Current Ratio         1.50   🟡 Adequate (target >1.5; retail avg ~1.3)
  Quick Ratio           0.88   🟡 Watch (target >1.0; inventory-heavy)
  Cash Ratio            0.25   🔴 Low (target >0.5)

PROFITABILITY RATIOS
  Gross Margin          40.0%  🟢 Strong
  EBIT Margin           12.0%  🟢 Healthy for retail
  Net Margin            8.0%   🟢 Above average
  ROE                   22.2%  🟢 Excellent (>15% target)
  ROA                   10.0%  🟢 Solid

LEVERAGE RATIOS
  Debt/Equity           0.83x  🟢 Conservative
  Interest Coverage     6.0x   🟢 Comfortable (>3x target)
  Debt/EBITDA           ~2.1x  🟢 Manageable

EFFICIENCY RATIOS
  Asset Turnover        1.25x  🟢 Good
  Inventory Turnover    10.0x  🟢 Fast-moving

CASH FLOW
  FCF                   $35M   🟢 Positive
  FCF Margin            7.0%   🟢 Healthy

OVERALL HEALTH: 🟢 STRONG
Strong profitability and leverage profile. Watch liquidity — cash ratio
is low; ensure credit facilities cover short-term obligations.
```

## Skill Prompt

```
You are a financial analyst performing a comprehensive ratio analysis.

Given the user's financial statement data, calculate and interpret the following ratios:

**LIQUIDITY**
- Current Ratio = Current Assets / Current Liabilities (target: >1.5)
- Quick Ratio = (Current Assets − Inventory) / Current Liabilities (target: >1.0)
- Cash Ratio = Cash / Current Liabilities (target: >0.5)

**PROFITABILITY**
- Gross Margin = Gross Profit / Revenue
- EBIT Margin = EBIT / Revenue
- Net Margin = Net Income / Revenue
- Return on Equity (ROE) = Net Income / Total Equity (target: >15%)
- Return on Assets (ROA) = Net Income / Total Assets (target: >5%)

**LEVERAGE / SOLVENCY**
- Debt-to-Equity = Total Debt / Total Equity (target: <1.0 for most industries)
- Interest Coverage = EBIT / Interest Expense (target: >3x; >5x is comfortable)
- Debt/EBITDA = Total Debt / EBITDA [estimate EBITDA as EBIT + D&A if not given; note assumption]

**EFFICIENCY**
- Asset Turnover = Revenue / Total Assets
- Inventory Turnover = Revenue / Inventory (or COGS / Inventory if COGS available)

**CASH FLOW**
- Free Cash Flow (FCF) = Operating Cash Flow − CapEx
- FCF Margin = FCF / Revenue

For each ratio:
1. Show the formula and calculated value.
2. Assign a signal: 🟢 Healthy / 🟡 Watch / 🔴 Concern based on general benchmarks.
3. One-line interpretation referencing the specific number.

End with:
- Overall Health summary (🟢 Strong / 🟡 Mixed / 🔴 Stressed) with a 2–3 sentence narrative.
- Top 2 strengths and top 2 areas to watch.

If any line item is missing, note it and skip or estimate the ratio with a clear assumption stated.
```

## Notes

- Benchmarks vary by industry. The skill uses general benchmarks; users should compare to sector peers.
- EBITDA is estimated if depreciation/amortization is not provided — note this assumption in output.
- Market ratios (P/E, EV/EBITDA, Price/Book) are not included here as they require share price data; use alongside market data tools.
- Related skills: `skills/investing/stock-analysis/buffett-checklist.md`, `skills/financial-modeling/comparable-analysis/`.
