---
name: Options Portfolio Greeks Aggregator
description: Aggregates and analyzes Greeks across a multi-leg options portfolio to produce net exposure summaries, hedge recommendations, and risk scenario analysis.
category: investing/options-derivatives
tags: [options, greeks, delta-hedge, portfolio-greeks, risk]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-23
---

## Description

This skill takes a multi-leg options portfolio as input and computes net first- and second-order Greeks (Delta, Gamma, Theta, Vega, Rho) across all positions, adjusting for contract multipliers, position direction, and underlying price. It identifies dominant exposures, flags concentrated risks, and generates delta-hedge recommendations using the underlying asset or futures. The output is suitable for traders, risk managers, and sophisticated investors who need a consolidated view of their options book's sensitivity to market moves, time decay, and volatility shifts.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide your options portfolio as a list of legs. Each leg should include:
- **Underlying symbol** (e.g., SPY, AAPL)
- **Option type** (Call or Put)
- **Expiration date** (YYYY-MM-DD)
- **Strike price**
- **Position size** (number of contracts; negative = short)
- **Per-contract Greeks**: Delta, Gamma, Theta, Vega, Rho (as decimals)
- **Underlying spot price**
- **Contract multiplier** (default 100 for equity options)

You may also specify:
- A target net delta for hedging (default: 0 = delta-neutral)
- Whether to include scenario analysis (±5%, ±10% moves in underlying and ±1–2 vol points)

Invoke by describing your portfolio or pasting a structured table/CSV.

## Example

**Input:**
```
Aggregate my options portfolio and recommend a delta hedge. Target: delta-neutral.

Symbol | Type | Expiry     | Strike | Contracts | Delta  | Gamma  | Theta   | Vega   | Rho    | Spot   | Multiplier
SPY    | Call | 2026-05-16 | 520    | +10       | 0.55   | 0.018  | -0.12   | 0.25   | 0.08   | 518.00 | 100
SPY    | Put  | 2026-05-16 | 500    | +10       | -0.30  | 0.015  | -0.10   | 0.22   | -0.05  | 518.00 | 100
SPY    | Call | 2026-06-20 | 530    | -5        | 0.42   | 0.014  | -0.09   | 0.30   | 0.07   | 518.00 | 100
AAPL   | Call | 2026-05-16 | 200    | +8        | 0.60   | 0.025  | -0.15   | 0.18   | 0.06   | 198.50 | 100
AAPL   | Put  | 2026-05-16 | 190    | -6        | -0.35  | 0.020  | -0.11   | 0.16   | -0.04  | 198.50 | 100
```

**Output:**

---
### Options Portfolio Greeks Aggregation Report
**Generated:** 2026-04-23 | **Target Delta:** 0 (Delta-Neutral)

---

#### 1. Position-Level Greeks (Dollar-Adjusted)

| Leg | Type | Strike | Exp | Contracts | Dollar Delta | Dollar Gamma | Dollar Theta | Dollar Vega | Dollar Rho |
|-----|------|--------|-----|-----------|-------------|-------------|-------------|------------|------------|
| SPY Call | C | 520 | May-26 | +10 | +55,000 | +1,800 | -1,200 | +2,500 | +800 |
| SPY Put | P | 500 | May-26 | +10 | -30,000 | +1,500 | -1,000 | +2,200 | -500 |
| SPY Call | C | 530 | Jun-26 | -5 | -21,000 | -700 | +450 | -1,500 | -350 |
| AAPL Call | C | 200 | May-26 | +8 | +47,880 | +1,992 | -1,200 | +1,440 | +480 |
| AAPL Put | P | 190 | May-26 | -6 | +25,200 | -1,440 | +792 | -1,152 | +288 |

*Dollar Delta = Per-contract Delta × Contracts × Multiplier × Spot Price*
*Dollar Gamma = Per-contract Gamma × Contracts × Multiplier × Spot²  / 100*
*Dollar Theta/Vega/Rho = Per-contract Greek × Contracts × Multiplier*

---

#### 2. Net Portfolio Greeks Summary

| Greek | SPY Book | AAPL Book | **Portfolio Total** | Interpretation |
|-------|----------|-----------|---------------------|----------------|
| **Dollar Delta** | +$4,000 | +$73,080 | **+$77,080** | Long ~149 shares SPY-equivalent |
| **Dollar Gamma** | +$2,600 | +$552 | **+$3,152** | Gamma-positive; benefits from large moves |
| **Dollar Theta** | -$1,750 | -$408 | **-$2,158/day** | Paying ~$2,158/day in time decay |
| **Dollar Vega** | +$3,200 | +$288 | **+$3,488/vol pt** | Long vol; gains ~$3,488 per +1 vol point |
| **Dollar Rho** | -$50 | +$768 | **+$718/100bps** | Mild positive rate sensitivity |

---

#### 3. Risk Flags

⚠️ **HIGH POSITIVE DELTA** — Net dollar delta of +$77,080 represents significant directional long exposure. A 1% adverse move costs approximately $770.
⚠️ **THETA BLEED** — Portfolio loses ~$2,158/day. Over 30 days, that is ~$64,740 assuming static positions and no underlying move.
✅ **POSITIVE GAMMA** — Portfolio is convex (long gamma). Accelerating gains on large up/down moves partially offset theta cost.
ℹ️ **LONG VEGA** — Portfolio benefits from volatility expansion. Monitor IV levels relative to entry.

---

#### 4. Delta-Hedge Recommendation

**Target:** Net Dollar Delta = $0

**Current Net Dollar Delta:** +$77,080

**Hedge Action:**
- SPY spot price: $518.00 | Multiplier: 1 (shares)
- Shares to sell short: **77,080 ÷ 518 ≈ 149 shares of SPY** (sell short)
- Alternative: Short **~1.49 SPY futures contracts** (if 1 contract = $50 × SPY index, adjust accordingly)

**Post-Hedge Greeks (Estimated):**

| Greek | Pre-Hedge | Hedge Instrument | Post-Hedge |
|-------|-----------|-----------------|------------|
| Dollar Delta | +$77,080 | -$77,154 | ≈ $0 |
| Dollar Gamma | +$3,152 | $0 | +$3,152 |
| Dollar Theta | -$2,158/day | $0 | -$2,158/day |
| Dollar Vega | +$3,488 | $0 | +$3,488 |

*Note: Stock/futures hedge does not affect Gamma, Theta, or Vega.*

---

#### 5. Scenario Analysis — P&L Estimate

Assumptions: instantaneous moves, all else equal (vol unchanged). Uses Dollar Delta + ½ × Dollar Gamma × move².

| Underlying Move | Est. SPY P&L | Est. AAPL P&L | Portfolio P&L (Pre-Hedge) | Portfolio P&L (Post-Hedge) |
|----------------|-------------|--------------|--------------------------|---------------------------|
| -10% | -$3,842 | -$6,992 | -$10,834 | -$2,136 |
| -5% | -$1,843 | -$3,358 | -$5,201 | -$1,023 |
| Flat (0%) | $0 | $0 | $0 | $0 |
| +5% | +$1,857 | +$3,414 | +$5,271 | +$1,038 |
| +10% | +$3,924 | +$7,108 | +$11,032 | +$2,174 |

*Positive gamma produces slight upside asymmetry in both scenarios.*

---

#### 6. Vega Scenario (Vol Shift, Delta-Neutral Post-Hedge)

| Vol Change | Est. P&L |
|-----------|----------|
| -2 vol pts | -$6,976 |
| -1 vol pt | -$3,488 |
| Flat | $0 |
| +1 vol pt | +$3,488 |
| +2 vol pts | +$6,976 |

---

#### 7. Summary & Next Steps

1. **Execute delta hedge** — sell ~149 SPY shares or equivalent futures to neutralize directional risk.
2. **Monitor theta decay** — reassess position sizing if time decay exceeds risk budget (~$2,158/day).
3. **Re-hedge triggers** — consider re-hedging if net delta drifts beyond ±$10,000 (gamma drift from underlying moves).
4. **Volatility watch** — long vega exposure is beneficial if IV rises; consider trimming if IV collapses below entry levels.
5. **Expiration management** — May-16 legs expire in ~23 days; plan roll or close strategy by May-9 to avoid gamma risk near expiry.

---

## Skill Prompt

```
You are an expert options risk analyst. When a user provides a multi-leg options portfolio, perform the following steps precisely and output a structured Greeks Aggregation Report.

---

### STEP 1 — Parse and Validate Input

Extract for each leg:
- Symbol, Option Type (Call/Put), Expiration Date, Strike Price
- Number of Contracts (positive = long, negative = short)
- Per-contract Greeks: Delta, Gamma, Theta, Vega, Rho
- Underlying Spot Price
- Contract Multiplier (default 100 for equity options unless stated otherwise)

If any required field is missing, state the assumption made (e.g., "Assumed multiplier = 100").

---

### STEP 2 — Compute Dollar-Adjusted Greeks Per Leg

For each leg, compute dollar-adjusted (notional) Greeks using these formulas:

**Dollar Delta** = Delta_per_contract × Contracts × Multiplier × Spot
  → Measures $ P&L per 1% move in underlying (divide by 100 for strict interpretation, but present as full sensitivity)
  → Sign convention: positive = net long delta, negative = net short delta

**Dollar Gamma** = Gamma_per_contract × Contracts × Multiplier × Spot²
  → Represents the change in Dollar Delta for a 1-point move in the underlying
  → Optionally scale: Dollar Gamma per 1% move = Gamma × Contracts × Multiplier × Spot² / 100

**Dollar Theta** = Theta_per_contract × Contracts × Multiplier
  → Daily P&L from time decay (typically negative for long options, positive for short)

**Dollar Vega** = Vega_per_contract × Contracts × Multiplier
  → P&L change per +1 percentage point increase in implied volatility

**Dollar Rho** = Rho_per_contract × Contracts × Multiplier
  → P&L change per +100 basis points change in interest rates

Present these in a clearly labeled table per leg.

---

### STEP 3 — Aggregate to Portfolio Level

Sum each dollar-adjusted Greek across all legs to produce:
- Total Portfolio Dollar Delta
- Total Portfolio Dollar Gamma
- Total Portfolio Dollar Theta (daily)
- Total Portfolio Dollar Vega (per vol point)
- Total Portfolio Dollar Rho (per 100 bps)

If the portfolio spans multiple underlyings, also present per-underlying subtotals.

Interpret each aggregate Greek in plain English:
- Dollar Delta: translate to approximate equivalent share count of the primary underlying
- Dollar Gamma: state whether portfolio is gamma-long (convex) or gamma-short (concave)
- Dollar Theta: state daily decay cost/income and 30-day projection
- Dollar Vega: state whether portfolio is long or short volatility and sensitivity magnitude
- Dollar Rho: note if material (typically small for short-dated equity options)

---

### STEP 4 — Risk Flag Analysis

Evaluate and flag the following conditions:

1. **Delta Risk**: If |Dollar Delta| > $25,000, flag as HIGH and quantify 1% move P&L impact.
2. **Gamma Risk Near Expiry**: If any leg expires within 14 days and has significant gamma, warn about pin risk and rapid delta change.
3. **Theta Burden**: If daily theta exceeds 0.5% of total portfolio notional, flag as HIGH DECAY.
4. **Vega Concentration**: If Dollar Vega is large relative to portfolio, flag direction (long/short vol) and quantify a 2-vol-point move impact.
5. **Rho Sensitivity**: Flag only if Dollar Rho exceeds $500 per 100 bps (material for long-dated or rate-sensitive positions).
6. **Expiration Clustering**: Warn if >50% of legs expire within the same week (event/pin risk concentration).

Use ✅ (acceptable), ⚠️ (caution), or 🚨 (high risk) indicators.

---

### STEP 5 — Delta-Hedge Recommendation

Determine the user's target net delta (default: 0, delta-neutral, unless specified).

Calculate:
- Delta Gap = Target Dollar Delta − Current Portfolio Dollar Delta
- Shares to trade = Delta Gap ÷ Spot Price of primary underlying (positive = buy, negative = sell short)
- If futures are preferred: Shares ÷ Futures Contract Size (state assumption on contract size)

Show a before/after table of all Greeks after the hedge is applied. Note that a stock or futures hedge affects only Delta (Gamma, Theta, Vega, Rho remain unchanged).

If the portfolio has multiple underlyings, recommend a per-underlying delta hedge unless the user requests cross-hedging with an index ETF (e.g., SPY).

---

### STEP 6 — Scenario Analysis

Compute estimated P&L for underlying price scenarios: −10%, −5%, 0%, +5%, +10% moves.

Use the second-order Taylor approximation:
  Est. P&L ≈ (Dollar Delta × ΔS/S) + 0.5 × (Dollar Gamma) × (ΔS/S)²

Where ΔS/S is the fractional move (e.g., 0.05 for +5%).

Present results for both pre-hedge and post-hedge portfolio.

Also compute vega scenario P&L for implied volatility shifts of −2, −1, 0, +1, +2 vol points:
  Est. Vega P&L = Dollar Vega × Δvol (in percentage points)

If theta scenario is requested, show cumulative theta at 7-day intervals up to the nearest expiration.

---

### STEP 7 — Actionable Summary

Provide a numbered list of 4–6 specific, actionable recommendations based on the analysis:
- Hedge execution (size, instrument, urgency)
- Re-hedge triggers (delta drift thresholds)
- Theta management (position reduction if decay is excessive)
- Volatility strategy (adjust for long/short vega positioning)
- Expiration management (roll or close timeline for near-term legs)
- Any concentration or correlation risks to monitor

---

### FORMATTING RULES

- Use markdown tables for all Greek summaries and scenarios.
- Label all tables clearly with units (e.g., "