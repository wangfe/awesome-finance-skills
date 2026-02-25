---
name: Buffett-Style Stock Checklist
description: Evaluate a stock using Warren Buffett's fundamental investing criteria and produce a pass/fail scorecard
category: investing/stock-analysis
tags: [fundamental-analysis, value-investing, buffett, checklist, long-term]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Walks through Warren Buffett's core investing criteria — economic moat, consistent earnings, return on equity, debt levels, management quality, and margin of safety — and produces a structured scorecard. The user supplies the financial data; the skill does the analysis and scoring.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Provide the company name/ticker and key financial metrics (or paste a financial summary). The skill scores the company on each Buffett criterion and gives an overall verdict.

**Data to provide:**
- Company name and ticker
- Last 5–10 years of EPS (or "consistently growing" / "erratic")
- Return on Equity (ROE) for last 3 years
- Long-term debt-to-earnings ratio (or total debt and net income)
- Net profit margin
- Current stock price and estimated intrinsic value (or P/E ratio)
- Brief description of the business and competitive position

## Example

**Input:**
```
Company: Coca-Cola (KO)
EPS trend (10yr): $1.60, $1.67, $1.74, $1.79, $1.92, $2.08, $2.11, $2.19, $2.25, $2.32 — consistent growth
ROE (3yr avg): 38%
Long-term debt: $35B, Net income: $10B → LT Debt/NI ratio: 3.5x
Net profit margin: 23%
P/E ratio: 24x, estimated fair value P/E: 20–22x
Business: Global beverage brand with dominant market share and pricing power.
```

**Output (abbreviated):**
```
=== Buffett Checklist: Coca-Cola (KO) ===

CRITERION                     RESULT    NOTES
─────────────────────────────────────────────────────────────
1. Consistent EPS Growth      ✅ PASS   10yr uninterrupted growth
2. ROE > 15%                  ✅ PASS   38% — exceptional
3. Debt manageable (<5x NI)   ✅ PASS   3.5x — comfortable
4. Net margin > 20%           ✅ PASS   23%
5. Economic Moat              ✅ PASS   Brand + distribution dominance
6. Understandable Business    ✅ PASS   Simple, global consumer product
7. Margin of Safety           ⚠ WATCH  Trading at slight premium to fair value
8. Management (proxy)         ✅ PASS   Long track record of capital returns

SCORE: 7.5 / 8

VERDICT: Strong Buffett-style candidate. Monitor valuation — consider
         accumulating on pullbacks toward fair value P/E of 20–22x.
```

## Skill Prompt

```
You are a value investing analyst applying Warren Buffett's core stock selection criteria.

Evaluate the provided company on these 8 criteria:

1. **Consistent EPS Growth** — Has EPS grown consistently over 7–10 years without major declines? (Target: yes)
2. **Return on Equity (ROE)** — Is ROE consistently above 15%? Above 20% is excellent. (Target: >15%)
3. **Manageable Debt** — Is long-term debt less than 5x annual net income? Less than 3x is ideal. (Target: <5x)
4. **Strong Net Profit Margin** — Is net margin above 15–20% for the industry? (Target: varies by sector)
5. **Economic Moat** — Does the company have durable competitive advantages (brand, network effects, switching costs, cost advantages, patents)? (Target: clear moat)
6. **Understandable Business** — Is the business simple enough to understand and predict? (Target: yes)
7. **Margin of Safety** — Is the stock trading at a discount (or reasonable premium) to intrinsic value? (Target: discount preferred)
8. **Management Quality** — Does management have a track record of shareholder-friendly decisions (buybacks, dividends, low dilution, honest communication)? (Target: yes)

For each criterion:
- State PASS, FAIL, or WATCH (borderline).
- Provide a one-line justification using the user's data.
- Score: PASS = 1pt, WATCH = 0.5pt, FAIL = 0pt.

Then provide:
- Total score (X / 8)
- Overall verdict: Strong candidate / Watchlist / Avoid — with a brief rationale.
- 2–3 specific follow-up questions the investor should research before deciding.

If data is missing for any criterion, note the gap rather than guessing.
```

## Notes

- This checklist is a qualitative + quantitative screen, not a full valuation model. Use alongside a DCF or comps analysis.
- "Economic moat" assessment is inherently qualitative — the skill makes its best judgment from the user's business description.
- For accurate ROE and margin comparisons, industry benchmarks matter; the user should provide sector context if available.
- Related skills: `skills/financial-modeling/dcf-valuation/`, `skills/investing/portfolio-management/`.
