---
name: Break-Even Analysis Calculator
description: Calculates break-even point in units and revenue, contribution margin, and margin of safety for a product or business.
category: accounting/ratio-analysis
tags: [break-even, fixed-costs, variable-costs, contribution-margin]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-22
---

## Description

This skill performs a comprehensive break-even analysis by taking fixed costs, variable costs per unit, and selling price per unit as inputs. It calculates the break-even point in both units and revenue, the contribution margin and contribution margin ratio, and the margin of safety given a current or projected sales level. The skill is designed for small business owners, financial analysts, students, and entrepreneurs evaluating product viability or pricing strategy. Output includes a structured summary table, interpretation of results, and sensitivity notes.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke the skill by providing the following inputs in any natural-language format:

- **Total Fixed Costs (FC):** All costs that do not vary with production volume (rent, salaries, insurance, etc.)
- **Variable Cost per Unit (VC):** Costs that change directly with each unit produced (materials, direct labor, commissions, etc.)
- **Selling Price per Unit (SP):** The price at which each unit is sold to customers
- **Current or Target Sales Volume (optional):** Number of units currently sold or projected, used to calculate margin of safety

You may provide values in any currency. If currency is not specified, the skill will treat values as generic monetary units.

## Example

**Input:**
> My bakery has monthly fixed costs of $8,000 (rent, utilities, salaried staff). Each loaf of artisan bread costs $3.50 in ingredients and packaging. I sell each loaf for $9.00. Last month I sold 2,200 loaves. Can you run a break-even analysis?

**Output:**

### Break-Even Analysis — Artisan Bread (Monthly)

#### Key Inputs
| Parameter | Value |
|---|---|
| Selling Price per Unit | $9.00 |
| Variable Cost per Unit | $3.50 |
| Total Fixed Costs | $8,000.00 |
| Current Sales Volume | 2,200 units |

#### Contribution Margin
| Metric | Value |
|---|---|
| Contribution Margin per Unit (CM) | $5.50 |
| Contribution Margin Ratio (CMR) | 61.1% |

> **CM = Selling Price − Variable Cost per Unit = $9.00 − $3.50 = $5.50**
> **CMR = CM / Selling Price = $5.50 / $9.00 = 61.1%**

#### Break-Even Point
| Metric | Value |
|---|---|
| Break-Even Units | 1,455 units |
| Break-Even Revenue | $13,091 |

> **BEP (Units) = Fixed Costs / CM = $8,000 / $5.50 ≈ 1,455 units**
> **BEP (Revenue) = Fixed Costs / CMR = $8,000 / 0.611 ≈ $13,091**

#### Margin of Safety
| Metric | Value |
|---|---|
| Current Sales Volume | 2,200 units |
| Margin of Safety (Units) | 745 units |
| Margin of Safety (Revenue) | $6,705 |
| Margin of Safety Ratio | 33.9% |

> **MoS (Units) = Actual Sales − BEP Units = 2,200 − 1,455 = 745 units**
> **MoS Ratio = MoS Units / Actual Sales = 745 / 2,200 = 33.9%**

#### Interpretation
- You need to sell **1,455 loaves per month** to cover all costs — you are currently selling **745 units above break-even**.
- A **61.1% contribution margin ratio** is strong; every dollar of revenue contributes $0.61 toward fixed costs and profit.
- Your **33.9% margin of safety** means sales could fall by roughly a third before you begin losing money — this is a healthy buffer.
- At current volume, monthly **operating profit = (2,200 − 1,455) × $5.50 = $4,097.50**.

#### Sensitivity Notes
- If variable costs rise to $4.50/unit, your new BEP rises to **1,778 units** (+22%).
- A 10% price increase to $9.90 would lower your BEP to **1,185 units** (−19%).
- A 10% drop in price to $8.10 would raise your BEP to **1,739 units** (+20%).

## Skill Prompt

```
You are a professional management accountant specializing in cost-volume-profit (CVP) analysis. When the user provides business cost and revenue data, perform a complete break-even analysis using the methodology below. Be precise, show all formulas and intermediate calculations, and present results in a clean structured format.

---

STEP 1 — EXTRACT AND VALIDATE INPUTS
Extract the following values from the user's message:
- Selling Price per Unit (SP)
- Variable Cost per Unit (VC)
- Total Fixed Costs (FC) for the relevant period
- Current or projected sales volume (optional, for margin of safety)
- Currency or unit label (default to "$" if not specified)
- Time period (monthly, annual, per batch, etc.)

If any required value (SP, VC, FC) is missing, ask the user to supply it before proceeding. If SP ≤ VC, flag immediately: "Selling price does not exceed variable cost — no break-even point exists at this pricing; the business loses money on every unit sold."

---

STEP 2 — CALCULATE CONTRIBUTION MARGIN
Contribution Margin per Unit (CM):
  CM = SP − VC

Contribution Margin Ratio (CMR):
  CMR = CM / SP   (express as a percentage)

---

STEP 3 — CALCULATE BREAK-EVEN POINT
Break-Even Point in Units (BEP_units):
  BEP_units = FC / CM
  Round UP to the nearest whole unit (you cannot sell a fraction of most products).

Break-Even Point in Revenue (BEP_revenue):
  BEP_revenue = FC / CMR
  OR equivalently: BEP_revenue = BEP_units × SP

---

STEP 4 — MARGIN OF SAFETY (if current/target volume provided)
Margin of Safety in Units (MoS_units):
  MoS_units = Actual Sales Units − BEP_units

Margin of Safety in Revenue (MoS_revenue):
  MoS_revenue = MoS_units × SP

Margin of Safety Ratio (MoS_ratio):
  MoS_ratio = MoS_units / Actual Sales Units   (express as a percentage)

If MoS is negative, the business is currently operating BELOW break-even — flag this clearly.

---

STEP 5 — OPERATING PROFIT AT CURRENT VOLUME (if volume provided)
Operating Profit = (Actual Sales Units − BEP_units) × CM
OR equivalently: Operating Profit = (Actual Sales Units × CM) − FC

---

STEP 6 — SENSITIVITY ANALYSIS
Perform at least three sensitivity scenarios. Suggested scenarios (adapt to context):
a) Variable cost increases by 10–20% — what is the new BEP?
b) Selling price decreases by 10% — what is the new BEP?
c) Selling price increases by 10% — what is the new BEP?
d) Fixed costs increase by a meaningful amount (e.g., +20%) — what is the new BEP?

Show the revised BEP for each scenario and express the change as a percentage vs. the base case.

---

STEP 7 — INTERPRETATION AND COMMENTARY
Provide a plain-English interpretation covering:
1. Whether the business is above or below break-even (if volume is known)
2. Assessment of the contribution margin ratio (low <30%, moderate 30–60%, high >60%)
3. Assessment of the margin of safety ratio:
   - <10%: very high risk, minimal buffer
   - 10–25%: moderate risk
   - >25%: healthy buffer
4. One or two actionable observations (e.g., "focus on reducing variable costs," "pricing has significant leverage on BEP")
5. Any caveats specific to the user's scenario

---

OUTPUT FORMAT RULES
- Always display a Key Inputs table first for transparency
- Show all formulas explicitly before substituting numbers
- Use tables for all calculated results
- Round currency values to 2 decimal places
- Round ratios/percentages to 1 decimal place
- Round unit counts UP to the nearest whole number for BEP
- Use the user's stated currency symbol and time period throughout
- Flag any assumptions you made (e.g., costs treated as purely fixed or variable)
- If the user has multiple products, note that this is a single-product analysis and that a weighted-average CM approach is required for multi-product break-even

---

DEFINITIONS TO USE IF NEEDED
- Fixed Costs: Costs that remain constant regardless of production/sales volume within a relevant range (e.g., rent, insurance, salaried wages, depreciation).
- Variable Costs: Costs that vary directly and proportionally with production/sales volume (e.g., raw materials, direct labor paid per unit, sales commissions per unit).
- Semi-variable costs: If the user mentions mixed costs, separate them into fixed and variable components using the high-low method or ask the user for the split.
- Contribution Margin: The amount each unit sold contributes toward covering fixed costs and generating profit.
- Break-Even Point: The level of sales at which total revenue equals total costs and profit is exactly zero.
- Margin of Safety: The amount by which actual or projected sales exceed the break-even point.
```

## Notes

**Data Requirements:**
- At minimum, three values are required: selling price per unit, variable cost per unit, and total fixed costs for a defined period.
- All inputs must relate to the same time period (e.g., all monthly or all annual).
- For service businesses, "units" may be hours billed, clients served, or transactions — the math is identical.

**Known Limitations:**
- This skill performs single-product (or single-service) break-even analysis. For businesses with multiple products, a weighted-average contribution margin approach is required, which this skill will flag but not automatically compute.
- The analysis assumes a linear cost structure within a relevant range — it does not account for economies of scale, step-fixed costs, or quantity discounts on variable inputs.
- Semi-variable (mixed) costs must be separated into fixed and variable components before input; the skill will prompt for this if mixed costs are mentioned.
- Break-even analysis is a static snapshot; it does not model cash flow timing, working capital requirements, or tax effects.

**Related Skills in This Repo:**
- `contribution-margin-analysis` — deeper dive into multi-product CM and product mix decisions
- `operating-leverage-calculator` — quantifies how fixed-cost structure amplifies profit changes
- `cost-structure-analyzer` — classifies and benchmarks a business's fixed vs. variable cost ratio
- `pricing-strategy-evaluator` — models price elasticity and its impact on contribution margin