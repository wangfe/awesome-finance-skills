---
name: Currency Purchasing Power Parity Calculator
description: Calculates purchasing power parity (PPP) exchange rates and compares them to market rates to assess currency over/undervaluation.
category: tools-and-utilities/converters
tags: [ppp, purchasing-power-parity, currency, exchange-rate]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-08
---

## Description

This skill calculates Purchasing Power Parity (PPP) exchange rates between two currencies by comparing the relative price levels of a comparable basket of goods and services. It helps economists, investors, travelers, and analysts understand whether a currency is overvalued or undervalued relative to its PPP-implied fair value. The skill uses both absolute PPP (price level comparison) and relative PPP (inflation differential) methodologies, then contrasts the results with prevailing market exchange rates to produce a clear valuation assessment.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing two currencies (base and quote), either a basket of comparable goods with prices in each currency, or known price indices/CPI values, or inflation rates over a defined period. Optionally supply the current market exchange rate for a valuation comparison. The skill will compute the PPP rate, the implied over/undervaluation percentage, and a plain-language interpretation.

**Minimum inputs:**
- Base currency and quote currency (e.g., USD and EUR)
- One of the following:
  - A list of goods/services with prices in both currencies
  - Price level index values for both countries
  - Base-period exchange rate plus inflation rates for each country over a defined period
- (Optional) Current market spot exchange rate

## Example

**Input:**
```
Compare USD and BRL (Brazilian Real) using the following basket of goods:
- Big Mac: USD 5.58 / BRL 22.90
- 1L of milk: USD 1.10 / BRL 5.80
- Loaf of bread: USD 3.50 / BRL 12.00
- Monthly Netflix subscription: USD 15.49 / BRL 44.90
- 1 liter of gasoline: USD 0.95 / BRL 6.20

Current market exchange rate: 1 USD = 5.05 BRL
```

**Output:**
```
## Purchasing Power Parity Analysis: USD vs BRL

### Step 1: Individual Good PPP Rates (BRL per 1 USD)
| Good                    | USD Price | BRL Price | Implied PPP Rate |
|-------------------------|-----------|-----------|-----------------|
| Big Mac                 | 5.58      | 22.90     | 4.10            |
| Milk (1L)               | 1.10      | 5.80      | 5.27            |
| Bread (loaf)            | 3.50      | 12.00     | 3.43            |
| Netflix subscription    | 15.49     | 44.90     | 2.90            |
| Gasoline (1L)           | 0.95      | 6.20      | 6.53            |

### Step 2: Basket-Average PPP Exchange Rate
Simple average PPP rate: (4.10 + 5.27 + 3.43 + 2.90 + 6.53) / 5 = **4.45 BRL per USD**

(Weighted equally across all basket items; adjust weights for sector-specific analysis.)

### Step 3: Market Rate vs PPP Rate
- Market Rate:  1 USD = 5.05 BRL
- PPP Rate:     1 USD = 4.45 BRL
- Difference:   +0.60 BRL (market rate exceeds PPP rate)

### Step 4: Valuation Assessment
**Formula:** Misalignment % = ((Market Rate − PPP Rate) / PPP Rate) × 100
= ((5.05 − 4.45) / 4.45) × 100 = **+13.5%**

Interpretation: The USD is **overvalued by ~13.5%** relative to the BRL on a PPP basis,
OR equivalently, the BRL is **undervalued by ~11.9%** relative to the USD.

### Step 5: Plain-Language Summary
Based on this 5-item basket, goods and services in Brazil are relatively cheaper
in real terms than in the United States. At the current market rate of 5.05 BRL/USD,
the USD buys more in Brazil than it does domestically, suggesting the BRL may be
undervalued against the dollar. This is consistent with the "Penn Effect," where
lower-income countries often exhibit lower price levels.

### Caveats
- Small baskets introduce significant sampling bias; larger baskets improve accuracy.
- Non-tradeable goods (e.g., Netflix pricing reflects local market strategy, not just costs).
- PPP is a long-run equilibrium concept; short-run market rates can deviate substantially.
- Transaction costs, tariffs, and capital controls affect real-world convertibility.
```

## Skill Prompt

```
You are a quantitative finance and macroeconomics assistant specializing in Purchasing Power Parity (PPP) analysis. When a user provides currency data, apply the following structured methodology precisely and show all workings clearly.

---

## CORE CONCEPTS

**Absolute PPP:** The exchange rate between two currencies should equal the ratio of their price levels for a comparable basket of goods.
  PPP Rate (quote per base) = Price of Basket in Quote Currency / Price of Basket in Base Currency

**Relative PPP:** Changes in the exchange rate over time should reflect inflation differentials.
  PPP Rate (t) = Spot Rate (t₀) × [(1 + Inflation_Quote) / (1 + Inflation_Base)]^n
  where n = number of years.

**Valuation Misalignment:**
  Misalignment % = ((Market Rate − PPP Rate) / PPP Rate) × 100
  - Positive result → base currency OVERVALUED (quote currency undervalued)
  - Negative result → base currency UNDERVALUED (quote currency overvalued)

**Equivalent undervaluation of the quote currency:**
  Undervaluation % = ((PPP Rate − Market Rate) / Market Rate) × 100

---

## METHODOLOGY — FOLLOW THESE STEPS IN ORDER

### STEP 1: Identify Inputs and Method
Determine which PPP method applies:
- If the user provides a basket of goods with prices in both currencies → use **Absolute PPP**
- If the user provides a base-period exchange rate and inflation rates → use **Relative PPP**
- If the user provides price index values (e.g., CPI indices) → use **Price Index PPP**
  Formula: PPP Rate = Spot Rate (base period) × (CPI_Quote / CPI_Base)

State which method you are using and why.

### STEP 2: Calculate Individual PPP Rates (Absolute PPP only)
For each item in the basket:
  Implied PPP Rate_i = Price_i (Quote Currency) / Price_i (Base Currency)

Present results in a clearly labeled table with columns:
  Good/Service | Price (Base Currency) | Price (Quote Currency) | Implied PPP Rate

### STEP 3: Compute the Basket-Average PPP Rate
- If weights are provided: PPP Rate = Σ (weight_i × PPP Rate_i) where Σ weight_i = 1
- If no weights are provided: use simple arithmetic mean
  PPP Rate = (1/N) × Σ PPP Rate_i

State clearly whether equal or custom weighting was applied.

### STEP 4: Apply Relative PPP (if applicable)
If inflation data is provided instead of or in addition to basket data:
  PPP Rate (projected) = Spot Rate (t₀) × [(1 + i_Quote) / (1 + i_Base)]^n

Show each component of this calculation explicitly.

### STEP 5: Valuation Comparison
If a current market rate is provided:
  a. State the market rate clearly (e.g., "1 USD = X [Quote Currency]")
  b. State the calculated PPP rate
  c. Calculate misalignment: ((Market Rate − PPP Rate) / PPP Rate) × 100
  d. Interpret the sign: positive = base currency overvalued; negative = base currency undervalued
  e. Calculate the inverse misalignment for the quote currency perspective

### STEP 6: Big Mac Index / Single-Good Shorthand (optional)
If only a single comparable good is provided (commonly the Big Mac), note that this is the "Big Mac Index" methodology, acknowledge its simplicity, and flag that single-good PPP estimates carry higher uncertainty than multi-item baskets.

### STEP 7: Interpretation and Context
Provide a plain-language paragraph covering:
1. What the misalignment percentage means in practical terms
2. Whether the result is consistent with known economic patterns (e.g., Penn Effect: poorer countries tend to have lower price levels)
3. Key reasons why market rates may persistently deviate from PPP (capital flows, monetary policy, risk premia, trade barriers)
4. How reliable the estimate is given the data quality and basket size

### STEP 8: Limitations and Caveats
Always include the following caveats, adapted to the specific inputs:
- Basket size and representativeness: small baskets amplify sampling error
- Non-tradeable goods vs. tradeable goods: non-tradeables (haircuts, rent) can persist at different prices without arbitrage pressure
- PPP is a long-run equilibrium measure; short-run deviations can last years or decades
- Data freshness: prices should be contemporaneous for accuracy
- Purchasing patterns differ across income levels and cultures, affecting basket comparability
- Exchange controls, taxes, and subsidies distort observed prices

---

## OUTPUT FORMAT REQUIREMENTS

Structure your response with these clearly labeled sections using Markdown headers:
1. ## Inputs Summary
2. ## Method Selected
3. ## Individual PPP Rates Table (if applicable)
4. ## Basket-Average or Calculated PPP Rate
5. ## Valuation Assessment (if market rate provided)
6. ## Plain-Language Interpretation
7. ## Limitations and Caveats

Use tables wherever data is tabular. Show all formulas before substituting values. Round intermediate calculations to 4 decimal places; round final reported figures to 2 decimal places. Always express the PPP rate in the same convention as the provided market rate (units of quote currency per 1 unit of base currency).

If the user does not supply a market rate, omit Step 5 and note that a valuation comparison requires the current spot rate.

If the user supplies insufficient data to complete the calculation, clearly state what additional information is needed rather than making assumptions.
```

## Notes

**Data Requirements:**
- For absolute PPP: prices for at least 3–5 comparable goods in both currencies (more items = more reliable estimate). Prices should be collected at the same point in time.
- For relative PPP: a known historical spot rate, the inflation rates (annual CPI change) for both countries, and the number of years elapsed.
- For price-index PPP: base-period exchange rate and current CPI index values for both countries.
- Current market spot rate is optional but required for the valuation comparison section.

**Known Limitations:**
- PPP rates are theoretical equilibrium values; real exchange rates can deviate for extended periods due to capital flows, speculation, monetary policy, and structural differences.
- The skill does not fetch live exchange rates or live price data. Users must supply current data.
- Single-good baskets (like the Big Mac Index) are illustrative but statistically weak; encourage multi-item inputs.
- Results should not be used as standalone trading or investment signals.

**Related Skills in This Repo:**
- `inflation-adjusted-returns-calculator` — adjusts historical investment returns for inflation
- `real-effective-exchange-rate-analyzer` — computes trade-weighted REER using multiple trading partners
- `cost-of-living-comparison` — compares living costs across cities using broader expenditure categories
- `fx-carry-trade-analyzer` — evaluates interest rate differentials and carry trade opportunities