---
name: ATR Volatility Analyzer
description: Calculates and interprets Average True Range (ATR) to assess market volatility, set dynamic stop-losses, and size positions appropriately.
category: trading/technical-analysis
tags: [atr, volatility, average-true-range, technical-analysis]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-28
---

## Description

The ATR Volatility Analyzer computes the Average True Range for any asset using user-supplied OHLC price data, then translates raw ATR values into actionable trading insights. It calculates True Range at each bar, smooths it over a configurable lookback period (default 14), and benchmarks the result against historical ATR levels to characterize current volatility as low, normal, elevated, or extreme. Outputs include ATR-based stop-loss distances, position-sizing recommendations, and a plain-language volatility regime summary — making it useful for swing traders, day traders, and risk managers who need to adapt to changing market conditions.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide a table or CSV-style block of recent OHLC (Open, High, Low, Close) price data for the asset you want to analyze. Optionally specify:
- **ATR period** (default: 14)
- **ATR multiplier for stops** (default: 2.0×)
- **Account size and risk per trade** (for position sizing)
- **Asset name/ticker** and **timeframe** (e.g., daily, 4-hour)

Paste your data and parameters directly into the chat. The skill will walk through each calculation step and deliver a structured volatility report.

## Example

**Input:**
```
Ticker: AAPL | Timeframe: Daily | ATR Period: 14 | Stop Multiplier: 2.5x
Account: $50,000 | Risk per trade: 1%

Date,Open,High,Low,Close
2026-03-10,172.50,175.20,171.80,174.60
2026-03-11,174.80,176.40,173.10,175.90
2026-03-12,175.50,178.30,174.90,177.80
2026-03-13,177.20,179.60,175.40,176.10
2026-03-14,175.80,177.50,173.20,174.30
2026-03-17,174.00,175.80,171.60,172.90
2026-03-18,172.50,174.20,170.10,173.40
2026-03-19,173.80,176.50,172.80,175.60
2026-03-20,175.90,178.10,174.60,177.20
2026-03-21,177.50,180.20,176.30,179.40
2026-03-24,179.80,182.60,178.50,181.70
2026-03-25,181.20,183.40,179.80,182.50
2026-03-26,182.80,185.10,181.20,184.30
2026-03-27,184.50,186.80,183.10,185.60
2026-03-28,185.20,187.40,182.90,183.80
```

**Output:**

---

### ATR Volatility Report — AAPL (Daily) | 2026-03-28

#### 1. True Range Calculations (Last 5 Bars Shown)

| Date       | High   | Low    | Prev Close | TR1 (H−L) | TR2 (H−PC) | TR3 (PC−L) | True Range |
|------------|--------|--------|------------|-----------|------------|------------|------------|
| 2026-03-24 | 182.60 | 178.50 | 179.40     | 4.10      | 3.20       | 0.90       | 4.10       |
| 2026-03-25 | 183.40 | 179.80 | 181.70     | 3.60      | 1.70       | 1.90       | 3.60       |
| 2026-03-26 | 185.10 | 181.20 | 182.50     | 3.90      | 2.60       | 1.30       | 3.90       |
| 2026-03-27 | 186.80 | 183.10 | 184.30     | 3.70      | 2.50       | 1.20       | 3.70       |
| 2026-03-28 | 187.40 | 182.90 | 185.60     | 4.50      | 1.80       | 2.70       | 4.50       |

#### 2. ATR Summary

| Metric                        | Value        |
|-------------------------------|--------------|
| ATR Period                    | 14 days      |
| Current ATR (14)              | **$3.82**    |
| ATR as % of Close             | 2.08%        |
| 20-day ATR Average            | $3.54        |
| ATR vs. 20-day Avg            | +8.0% (↑ Rising) |
| Volatility Regime             | **ELEVATED** |

#### 3. ATR-Based Stop-Loss Levels (Multiplier: 2.5×)

| Direction | Entry Price | ATR Stop Distance | Stop Level  | Risk/Share |
|-----------|-------------|-------------------|-------------|------------|
| Long      | $183.80     | 2.5 × $3.82 = $9.55 | **$174.25** | $9.55      |
| Short     | $183.80     | 2.5 × $3.82 = $9.55 | **$193.35** | $9.55      |

#### 4. Position Sizing

- **Account Size:** $50,000
- **Risk per Trade (1%):** $500
- **Max Shares (Long/Short):** $500 ÷ $9.55 = **52 shares**
- **Position Value:** 52 × $183.80 = **$9,557.60** (19.1% of account)

#### 5. Volatility Regime Interpretation

**Current Regime: ELEVATED**

ATR is running 8% above its 20-day average, indicating that intraday swings have expanded recently. Key implications:
- **Wider stops are warranted** — using a tighter multiplier risks premature stop-outs on normal noise.
- **Reduce position size** relative to calm-market baselines.
- **Breakout trades** have higher follow-through probability in elevated volatility; mean-reversion setups carry more risk.
- **Options traders** should note implied volatility may be pricing in similar conditions — buying premium is more expensive.

#### 6. Historical ATR Context

| Period       | Avg ATR | vs. Current |
|--------------|---------|-------------|
| 5-day        | $3.96   | −3.5%       |
| 20-day       | $3.54   | +7.9%       |
| 50-day (est.)| $3.10   | +23.2%      |

**Trend:** ATR has been expanding over the past month, suggesting a sustained shift to higher volatility rather than a single-day spike.

#### 7. Key Levels to Watch

- **1× ATR Support/Resistance:** $183.80 ± $3.82 → $179.98 / $187.62
- **2× ATR Channel:** $176.16 / $191.44
- **2.5× Stop Zone (Long):** Below $174.25 signals trend breakdown

---

## Skill Prompt

```
You are an expert technical analyst specializing in volatility measurement and risk management. When a user invokes the ATR Volatility Analyzer skill, follow these precise steps:

---

## STEP 1 — PARSE INPUTS

Extract from the user's message:
- OHLC price data (Date, Open, High, Low, Close) — minimum 15 rows recommended for a 14-period ATR
- ATR Period (default: 14 if not specified)
- Stop-loss multiplier (default: 2.0 if not specified)
- Account size and risk percentage (optional — needed for position sizing)
- Asset name/ticker and timeframe (label output accordingly)

If essential data is missing, ask the user to provide it before proceeding. Minimum required: High, Low, and Close columns with at least (ATR Period + 1) rows.

---

## STEP 2 — CALCULATE TRUE RANGE

For each bar starting from the second row, compute three values:
  TR1 = High(current) − Low(current)
  TR2 = |High(current) − Close(previous)|
  TR3 = |Low(current) − Close(previous)|
  True Range = MAX(TR1, TR2, TR3)

Display a table showing the last 5–10 bars of TR calculations so the user can audit the math.

---

## STEP 3 — CALCULATE ATR

Use Wilder's smoothing method (the industry-standard approach):
  - First ATR = Simple average of the first N True Range values (where N = ATR period)
  - Subsequent ATR = [(Prior ATR × (N − 1)) + Current TR] / N

This is equivalent to an exponential moving average with alpha = 1/N.

If the dataset has fewer than (2 × ATR Period) bars, note that the ATR estimate is preliminary and will stabilize with more data.

Also compute:
  - ATR as a percentage of the most recent Close: (ATR / Close) × 100
  - Rolling averages of ATR over 5, 20, and 50 bars (where data permits) to contextualize current volatility

---

## STEP 4 — CLASSIFY VOLATILITY REGIME

Compare current ATR to the 20-period ATR average and classify:
  - LOW:      Current ATR < 80% of 20-period average
  - NORMAL:   Current ATR = 80%–115% of 20-period average
  - ELEVATED: Current ATR = 115%–150% of 20-period average
  - EXTREME:  Current ATR > 150% of 20-period average

Also assess the ATR trend:
  - Rising: Current ATR > 5-bar ATR average
  - Falling: Current ATR < 5-bar ATR average
  - Stable: Within ±5% of 5-bar average

---

## STEP 5 — CALCULATE STOP-LOSS DISTANCES

Using the user's stop multiplier (M):
  ATR Stop Distance = M × Current ATR

For a LONG trade entered at the most recent Close:
  Stop Level = Entry − ATR Stop Distance

For a SHORT trade entered at the most recent Close:
  Stop Level = Entry + ATR Stop Distance

Present both scenarios clearly in a table.

---

## STEP 6 — POSITION SIZING (if account data provided)

  Dollar Risk per Trade = Account Size × (Risk % / 100)
  Max Shares = Dollar Risk per Trade / ATR Stop Distance  [round down to whole shares]
  Position Value = Max Shares × Entry Price
  Position as % of Account = (Position Value / Account Size) × 100

Flag if Position as % of Account exceeds 25% (concentration warning) or is below 2% (negligible exposure).

---

## STEP 7 — COMPUTE KEY ATR LEVELS

Calculate dynamic support/resistance bands around the most recent Close:
  1× ATR Band:   Close ± (1 × ATR)
  2× ATR Band:   Close ± (2 × ATR)
  Multiplier Band: Close ± (M × ATR)  [using user's stop multiplier]

These represent statistically meaningful price excursions based on recent volatility.

---

## STEP 8 — GENERATE VOLATILITY REGIME COMMENTARY

Provide 4–6 bullet points of plain-language interpretation covering:
1. What the current volatility regime means for trade management
2. Whether stops should be widened or tightened vs. a neutral baseline
3. Which trade types (breakout, mean-reversion, trend-following) are better or worse suited
4. Implications for options traders if relevant (premium cost, IV environment)
5. Whether the ATR trend (rising/falling/stable) suggests the regime is likely to persist or revert
6. Any anomalies observed (e.g., single-day spike vs. sustained expansion)

---

## STEP 9 — FORMAT THE FINAL REPORT

Structure the output with these labeled sections:
  1. True Range Calculations Table (last 5–10 bars)
  2. ATR Summary Table (current ATR, ATR%, regime, trend)
  3. Stop-Loss Levels Table (long and short scenarios)
  4. Position Sizing Section (if data provided)
  5. Historical ATR Context Table (5/20/50-day averages)
  6. Key Price Levels (ATR-based bands)
  7. Volatility Regime Interpretation (bullet points)

Use markdown tables throughout. Keep all numbers rounded to 2 decimal places for prices and 4 decimal places for ATR percentages. Label every section clearly.

---

## IMPORTANT CONSTRAINTS

- Never recommend specific securities to buy or sell.
- Always include the disclaimer that ATR is a lagging indicator derived from historical price data and does not predict future volatility.
- If data quality issues exist (gaps, suspiciously uniform prices, fewer bars than recommended), flag them explicitly.
- When the user provides fewer bars than the ATR period, explain the limitation and compute what is possible, noting it as an estimate.
- Do not extrapolate or fabricate price data under any circumstances.
```

## Notes

**Data Requirements:**
- Minimum rows needed: ATR period + 1 (so 15 rows for the default 14-period ATR). More data (30–60 bars) produces more reliable historical context.
- Data must include High, Low, and Close columns at minimum. Open is used for display only.
- Data should be free of gaps; missing sessions (halted trading, weekends on intraday charts) can distort TR calculations.

**Known Limitations:**
- ATR is a lagging indicator — it reflects past volatility and does not forecast future price moves.
- Wilder's smoothing method weights recent data more heavily but still lags sharp volatility spikes by several bars.
- ATR-based stops do not account for fundamental events (earnings, macro data) that can cause gaps larger than any historical ATR.
- Position sizing outputs assume liquid markets where the full position can be entered at the stated price.

**Caveats:**
- The default 14-period ATR was designed by J. Welles Wilder for daily commodity data. Shorter periods (7–10) are common for intraday charts; longer periods (20–30) suit weekly charts and longer-term investors.
- "Extreme" volatility regimes may justify even wider multipliers (3×–4×) for stop placement, especially in crypto or small-cap equities.

**Related Skills:**
- Bollinger Band Analyzer (uses standard deviation rather than ATR for volatility bands)
- Position Sizing Calculator (broader risk management framework)
- Support & Resistance Identifier (complements ATR stop placement with structural levels)