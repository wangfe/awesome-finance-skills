---
name: DCF Model Builder
description: Build a discounted cash flow valuation from user-supplied financials and assumptions to estimate intrinsic value per share
category: financial-modeling/dcf-valuation
tags: [dcf, valuation, intrinsic-value, financial-modeling, investing]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Guides the user through a 5–10 year discounted cash flow model. The user provides revenue, free cash flow margins, growth assumptions, discount rate (WACC), terminal growth rate, and share count. The skill constructs the projection table, calculates terminal value, discounts all cash flows, and outputs an estimated intrinsic value per share with a sensitivity table.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions. DCF models are highly sensitive
> to assumptions; treat outputs as a range of estimates, not a precise prediction.

## Usage

Provide:
- Base year revenue and free cash flow (FCF) margin
- Revenue growth rate assumptions (can be stage-based: high growth then slowdown)
- WACC (discount rate)
- Terminal growth rate (long-run FCF growth)
- Net debt (total debt minus cash)
- Shares outstanding

## Example

**Input:**
```
Company: Example Corp
Base year revenue: $1,000M
FCF margin: 15%
Growth assumptions:
  Years 1–5: 20% per year
  Years 6–10: 10% per year
WACC: 10%
Terminal growth rate: 3%
Net debt: $200M
Shares outstanding: 100M
Projection period: 10 years
```

**Output (abbreviated):**
```
=== DCF Valuation: Example Corp ===

PROJECTION TABLE ($M)
Year  Revenue   FCF Margin  FCF      Discount Factor  PV of FCF
1     $1,200    15%         $180     0.909            $163.6
2     $1,440    15%         $216     0.826            $178.4
...
10    $4,241    15%         $636     0.386            $245.5

Sum of PV (FCF Years 1–10):     $1,820M
Terminal Value (FCF Yr11/WACC-g): $9,337M
PV of Terminal Value:            $3,602M

Enterprise Value:                $5,422M
Less: Net Debt:                  ($200M)
Equity Value:                    $5,222M
Shares Outstanding:              100M

INTRINSIC VALUE PER SHARE: $52.22

SENSITIVITY TABLE (Intrinsic Value per Share)
            WACC
            8%      10%     12%
TGR  2%    $68     $47     $35
     3%    $79     $52     $38
     4%    $96     $61     $43
```

## Skill Prompt

```
You are a financial analyst building a discounted cash flow (DCF) model.

Given the user's inputs, perform these steps:

**Step 1 — Revenue & FCF Projections**
- Project revenue for each year of the forecast period using the stated growth rates.
- Apply the FCF margin to get free cash flow each year.
- Present as a table: Year | Revenue | FCF Margin | Free Cash Flow.

**Step 2 — Discount Cash Flows**
- Calculate the discount factor for each year: 1 / (1 + WACC)^n
- Calculate PV of each year's FCF: FCF × discount factor.
- Sum all PV(FCF) values.

**Step 3 — Terminal Value**
- Use the Gordon Growth Model: TV = FCF_final_year × (1 + TGR) / (WACC − TGR)
- Discount TV to present: PV(TV) = TV / (1 + WACC)^n

**Step 4 — Equity Value & Per Share Value**
- Enterprise Value = Sum of PV(FCF) + PV(TV)
- Equity Value = Enterprise Value − Net Debt
- Intrinsic Value per Share = Equity Value / Shares Outstanding

**Step 5 — Sensitivity Table**
- Build a 3×3 sensitivity table varying WACC (±2%) and Terminal Growth Rate (±1%) around the base case.
- Show resulting intrinsic value per share in each cell.

**Step 6 — Commentary**
- State what % of the total enterprise value comes from the terminal value (a key risk indicator).
- Briefly note which assumptions most heavily influence the valuation.
- If TV/EV > 80%, flag that the valuation is highly sensitive to terminal assumptions.

Show all calculations clearly. Use consistent currency units ($M or $B). Round to 2 decimal places.
```

## Notes

- This model uses unlevered free cash flow (FCF to firm). Equity FCF models require different inputs.
- WACC should reflect the company's cost of capital; for a rough estimate: WACC = risk-free rate (4%) + equity risk premium (5–6%) × beta.
- Terminal growth rate should not exceed long-run GDP growth (~2–3%) for mature companies.
- The model does not account for stock-based compensation dilution; users should adjust share count accordingly.
- Related skills: `skills/financial-modeling/comparable-analysis/`, `skills/investing/stock-analysis/buffett-checklist.md`.
