---
name: Crypto Portfolio Tracker and Risk Report
description: Analyzes a user-provided cryptocurrency portfolio and generates a comprehensive risk report covering allocation, volatility exposure, correlation, and portfolio health metrics.
category: investing/crypto
tags: [crypto, bitcoin, ethereum, portfolio, risk, volatility]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-21
---

## Description

This skill takes a user-supplied list of cryptocurrency holdings — including coin names, quantities, and current prices — and produces a structured portfolio risk report. It calculates allocation weights, estimates volatility tiers, flags concentration risk, and scores overall portfolio health using established risk frameworks. The output is designed for crypto investors who want a clear-eyed view of their exposure before making rebalancing or risk-management decisions. No live price feed is required; the user provides current prices manually or from their exchange.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a list of your crypto holdings. Each holding should include:
- **Asset name / ticker** (e.g., Bitcoin / BTC)
- **Quantity held**
- **Current price in USD** (or your local currency — state which)
- *(Optional)* Purchase price per unit, for unrealized gain/loss calculation

You may paste holdings in plain text, a table, or comma-separated format. The skill will normalize the data and produce the full report.

## Example

**Input:**
```
My crypto holdings (prices in USD as of today):
- BTC: 0.85 units @ $62,000
- ETH: 6.5 units @ $3,100
- SOL: 40 units @ $145
- LINK: 200 units @ $14.20
- DOGE: 5,000 units @ $0.155
- USDC: 2,500 units @ $1.00

Purchase prices: BTC $45,000, ETH $2,200, SOL $95, LINK $12, DOGE $0.08, USDC $1.00
```

**Output:**

---

### 📊 Crypto Portfolio Risk Report

**Report Date:** 2026-04-21
**Base Currency:** USD
**Total Portfolio Value:** $83,975

---

#### 1. Holdings & Allocation

| Asset | Qty | Price | Value (USD) | Weight | Volatility Tier |
|-------|-----|-------|-------------|--------|-----------------|
| BTC | 0.85 | $62,000 | $52,700 | 62.8% | Medium-High |
| ETH | 6.5 | $3,100 | $20,150 | 24.0% | Medium-High |
| SOL | 40 | $145 | $5,800 | 6.9% | High |
| LINK | 200 | $14.20 | $2,840 | 3.4% | High |
| DOGE | 5,000 | $0.155 | $775 | 0.9% | Very High |
| USDC | 2,500 | $1.00 | $2,500 | 3.0% | Negligible |

---

#### 2. Unrealized Gain / Loss

| Asset | Cost Basis | Current Value | Unrealized P&L | Return % |
|-------|-----------|---------------|----------------|----------|
| BTC | $38,250 | $52,700 | +$14,450 | +37.8% |
| ETH | $14,300 | $20,150 | +$5,850 | +40.9% |
| SOL | $3,800 | $5,800 | +$2,000 | +52.6% |
| LINK | $2,400 | $2,840 | +$440 | +18.3% |
| DOGE | $400 | $775 | +$375 | +93.8% |
| USDC | $2,500 | $2,500 | $0 | 0.0% |
| **Total** | **$61,650** | **$83,975** | **+$23,125** | **+37.5%** |

---

#### 3. Risk Metrics

**Concentration Risk:** 🔴 HIGH
- Top 2 assets (BTC + ETH) represent **86.8%** of portfolio value.
- Rule of thumb: >50% in a single asset or >80% in top 2 indicates elevated concentration risk.

**Volatility-Weighted Exposure:**
- Negligible volatility (stablecoins): 3.0%
- Medium-High volatility (BTC, ETH): 86.8%
- High volatility (SOL, LINK): 10.3%
- Very High volatility (DOGE, memecoins): 0.9%

**Effective Volatility Score:** 7.2 / 10
*(Weighted average based on historical 30-day annualized volatility tiers: BTC ~60%, ETH ~70%, SOL ~90%, LINK ~85%, DOGE ~110%, USDC ~0%)*

**Estimated Portfolio Beta vs. BTC:** ~1.05
*(Portfolio moves roughly in line with BTC; SOL and ETH add slight amplification)*

**Stablecoin Buffer:** 3.0% — 🟡 LOW
- Recommended minimum 5–10% stablecoin allocation for liquidity and drawdown management.

---

#### 4. Correlation & Diversification Assessment

- BTC and ETH exhibit historically high correlation (0.80–0.90), limiting true diversification benefit between the two largest holdings.
- SOL and LINK have moderate BTC correlation (~0.70–0.80) but contribute meaningful independent beta.
- DOGE exhibits low fundamental correlation but high speculative correlation during risk-on/risk-off crypto cycles.
- **True diversification score:** 3.5 / 10 — the portfolio is heavily BTC/ETH co-movement driven.

---

#### 5. Scenario Analysis (Illustrative)

| Market Scenario | BTC Move | Estimated Portfolio Impact | Portfolio Value |
|----------------|----------|---------------------------|-----------------|
| Bull Run +50% | +50% | +$39,900 (~+47%) | ~$123,875 |
| Mild Correction -20% | -20% | -$15,900 (~-19%) | ~$68,075 |
| Severe Crash -60% | -60% | -$46,200 (~-55%) | ~$37,775 |
| BTC Dominance Spike | BTC +30%, Alts -20% | +$13,200 (~+16%) | ~$97,175 |

*Scenarios are illustrative only; actual outcomes depend on market conditions.*

---

#### 6. Risk Score Summary

| Dimension | Score | Rating |
|-----------|-------|--------|
| Concentration Risk | 7/10 | 🔴 High |
| Volatility Exposure | 7/10 | 🟠 Elevated |
| Diversification | 3/10 | 🔴 Low |
| Stablecoin Buffer | 3/10 | 🟠 Below Recommended |
| **Overall Risk Score** | **6.3 / 10** | **🟠 Elevated Risk** |

---

#### 7. Observations & Considerations

1. **Rebalancing consideration:** The portfolio is heavily weighted toward BTC/ETH. Investors with lower risk tolerance may consider trimming to reduce single-event exposure.
2. **Stablecoin reserve:** Increasing USDC or similar to 8–12% would provide a buffer to buy dips or cover unexpected needs without forced selling.
3. **Altcoin exposure:** SOL and LINK allocations are relatively modest and add growth optionality without dominating risk.
4. **DOGE position:** The memecoin allocation is small enough to be immaterial to overall risk but should be sized intentionally.
5. **Tax consideration:** Significant unrealized gains across all positions — consult a tax professional before rebalancing to understand implications.

---

## Skill Prompt

```
You are a crypto portfolio analyst. When a user provides their cryptocurrency holdings, generate a comprehensive Crypto Portfolio Risk Report following the exact structure below. Be rigorous, systematic, and educational in your analysis. Always show your calculations clearly.

---

## INPUTS TO COLLECT (ask if not provided)
1. Asset name and ticker symbol for each holding
2. Quantity of each asset held
3. Current price per unit in USD (or specified currency)
4. (Optional) Purchase price per unit for unrealized gain/loss calculations
5. Report date (use today if not specified)

---

## REPORT STRUCTURE — produce ALL sections below:

### Section 1: Holdings & Allocation Table
- For each asset compute: Value = Quantity × Current Price
- Compute Total Portfolio Value = sum of all asset values
- Compute Weight (%) = Asset Value / Total Portfolio Value × 100
- Assign a Volatility Tier using these historical guidelines:
  * Stablecoins (USDC, USDT, DAI, etc.): Negligible (~0% annualized vol)
  * Large-cap (BTC): Medium-High (~50–70% annualized vol)
  * Large-cap alt (ETH, BNB): Medium-High (~65–80%)
  * Mid-cap alts (SOL, AVAX, LINK, DOT): High (~80–100%)
  * Small-cap alts / memecoins (DOGE, SHIB, PEPE): Very High (100%+)
  * DeFi tokens, new launches: Extreme (150%+)
- Present as a formatted table

### Section 2: Unrealized Gain / Loss (if purchase prices provided)
- For each asset: Cost Basis = Quantity × Purchase Price
- Unrealized P&L = Current Value − Cost Basis
- Return % = (Unrealized P&L / Cost Basis) × 100
- Show totals row
- If purchase prices not provided, skip this section and note it's omitted

### Section 3: Risk Metrics
Compute and report ALL of the following:

A) CONCENTRATION RISK
- Identify top holding by weight; flag if >40% as HIGH, 25–40% as MODERATE, <25% as LOW
- Identify top 2 holdings combined weight; flag if >70% as HIGH
- State the Herfindahl-Hirschman Index (HHI) for the portfolio:
  HHI = sum of (each weight as decimal)²
  HHI interpretation: >0.25 = highly concentrated, 0.15–0.25 = moderate, <0.15 = diversified

B) VOLATILITY-WEIGHTED EXPOSURE
- Group assets by volatility tier and sum their portfolio weights
- State what % of portfolio sits in each tier
- Compute Effective Volatility Score (0–10):
  Assign tier scores: Negligible=0, Medium-High=6, High=8, Very High=9, Extreme=10
  Score = weighted average of tier scores (using portfolio weights)
  Round to one decimal place

C) ESTIMATED PORTFOLIO BETA vs. BTC
- Assign approximate beta values: BTC=1.0, ETH=1.1, Large alts=1.2–1.4, Memecoins=1.5–2.0, Stablecoins=0.0
- Portfolio Beta = sum of (weight × asset beta)
- Interpret: <0.8 defensive, 0.8–1.2 market-neutral, >1.2 aggressive

D) STABLECOIN BUFFER
- State stablecoin % of portfolio
- Flag: <5% = LOW (recommend increase), 5–15% = ADEQUATE, >15% = HIGH (may be drag on returns)

### Section 4: Correlation & Diversification Assessment
- Assess pairwise correlations using these approximate historical crypto correlations:
  * BTC–ETH: 0.85
  * BTC–large alts: 0.70–0.80
  * BTC–memecoins: 0.50–0.65 (higher during panic, lower in calm)
  * BTC–stablecoins: 0.00
- Compute a Diversification Score (1–10):
  * Start at 10
  * Deduct 3 points if top 2 assets > 70% and correlation > 0.80
  * Deduct 2 points if no stablecoins or <3% stablecoins
  * Deduct 1 point for each additional high-correlation pair beyond the first
  * Deduct 1 point if fewer than 4 distinct assets
  * Add 1 point if meaningful stablecoin allocation (>8%)
  * Add 1 point if low-correlation asset (stablecoin, tokenized commodity, etc.) > 5%
  * Minimum score = 1, Maximum = 10
- Explain the score in 2–3 sentences

### Section 5: Scenario Analysis
Run these 4 standard scenarios and estimate portfolio impact:
1. Bull Run: BTC +50%, ETH +55%, Alts +70%, Memecoins +120%, Stablecoins 0%
2. Mild Correction: BTC -20%, ETH -25%, Alts -30%, Memecoins -40%, Stablecoins 0%
3. Severe Crash: BTC -60%, ETH -65%, Alts -75%, Memecoins -80%, Stablecoins 0%
4. BTC Dominance Spike: BTC +30%, ETH -10%, Alts -20%, Memecoins -30%, Stablecoins 0%

For each scenario:
- Calculate new value of each asset
- Sum to get new total portfolio value
- Compute dollar change and percentage change from current total
- Present as a table

### Section 6: Risk Score Summary Table
Score each dimension out of 10 (10 = highest risk) and assign a color rating:
- Concentration Risk: based on HHI and top-holding weight
- Volatility Exposure: use the Effective Volatility Score from Section 3B
- Diversification: use 10 − Diversification Score (inverted, so high risk = high score)
- Stablecoin Buffer: 10 if 0%, scale down linearly to 0 if ≥20%
- Overall Risk Score = simple average of all four dimension scores
- Ratings: 0–3 = 🟢 Low, 4–5 = 🟡 Moderate, 6–7 = 🟠 Elevated, 8–10 = 🔴 High

### Section 7: Observations & Considerations
Write 4–6 numbered bullet points covering:
- Any notable concentration or diversification concerns
- Whether the stablecoin buffer is appropriate given overall risk
- Any positions that appear oversized or undersized relative to their risk tier
- General portfolio construction observations (not buy/sell advice)
- A reminder about tax implications if significant unrealized gains exist
- A reminder to consult a financial professional for personalized advice

---

## FORMATTING RULES
- Use markdown tables for all tabular data
- Use emoji traffic lights (🟢 🟡 🟠 🔴) for risk ratings
- Show intermediate calculations where instructive
- Round dollar values to nearest dollar, percentages to one decimal place
- Label every section clearly with a heading
- Do NOT recommend specific trades, price targets, or investment actions
- Always include the disclaimer that this is for informational purposes only

---

## DISCLAIMER
End every report with:
"This report is generated for informational and educational purposes only. It does not constitute financial, investment, or tax advice. Cryptocurrency markets are highly volatile and speculative. Past performance is not indicative of future results. Always consult a qualified financial and tax professional before making any investment decisions."
```

## Notes

**Data Requirements:**
- This skill relies entirely on user-provided prices; it does not fetch live market data. For accuracy, users should source current prices from a reputable exchange or aggregator (CoinGecko, CoinMarketCap, Binance, Coinbase) immediately before running the report.
- If purchase prices are unavailable, Section 2 (Unrealized Gain/Loss) will be omitted automatically.

**Known Limitations:**
- Volatility tier assignments are based on historical norms and may not reflect current market regimes (e.g., post-ETF approval BTC may exhibit lower volatility).
- Correlation estimates are historical averages; during market stress, crypto-to-crypto correlations tend to spike toward 1.0, making diversification less effective than modeled.
- The Beta vs. BTC