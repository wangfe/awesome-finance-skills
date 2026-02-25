---
name: Stock Portfolio Analyzer
description: Analyze a stock portfolio's performance, allocation, risk concentration, sector exposure, and key metrics — and generate a comprehensive portfolio health report
category: investing/portfolio-analysis
tags: [portfolio-analysis, stock-portfolio, performance, allocation, risk, diversification]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Takes a list of holdings (ticker, shares or weight, cost basis, current price) and produces a full portfolio health report: performance attribution, sector and geographic allocation, concentration risk, top/bottom performers, correlation concerns, dividend income, and actionable rebalancing recommendations. Works for any size portfolio.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Provide your holdings in any of these formats:

**Format A (detailed):**
```
Holdings:
Ticker | Shares | Avg Cost | Current Price
AAPL   | 50     | $145.00  | $189.50
MSFT   | 30     | $280.00  | $415.00
...
```

**Format B (weights only):**
```
Portfolio value: $100,000
Holdings: AAPL 18%, MSFT 15%, NVDA 12%, AMZN 10%, GOOGL 8%, BRK.B 7%, JNJ 6%, JPM 5%, VTI 10%, BND 9%
```

**Optional context to add:**
- Investment goal (growth / income / balanced / capital preservation)
- Time horizon
- Benchmark (e.g., S&P 500)
- Risk tolerance (low / medium / high)

## Example

**Input:**
```
Portfolio value: $125,000
Goal: Long-term growth | Horizon: 10+ years | Risk: Medium-High
Benchmark: S&P 500

Ticker | Shares | Avg Cost | Current Price | Sector
AAPL   | 60     | $155     | $189          | Technology
MSFT   | 25     | $290     | $415          | Technology
NVDA   | 15     | $420     | $875          | Technology
AMZN   | 20     | $130     | $198          | Consumer Discretionary
GOOGL  | 18     | $115     | $172          | Technology
JNJ    | 40     | $155     | $148          | Healthcare
JPM    | 35     | $170     | $225          | Financials
VTI    | 50     | $195     | $245          | Broad Market ETF
```

**Output:**
```
╔══════════════════════════════════════════════════════════╗
║         PORTFOLIO ANALYSIS REPORT                        ║
║         Goal: Long-Term Growth | Horizon: 10+ yrs        ║
╚══════════════════════════════════════════════════════════╝

━━━ PORTFOLIO SUMMARY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Total Value:        $125,840
  Total Cost Basis:   $96,550
  Total Gain/Loss:    +$29,290  (+30.3%)
  Unrealized P&L:     +$29,290

━━━ PERFORMANCE ATTRIBUTION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Ticker  Value     Weight   Cost    Gain/$    Gain/%   Contribution
  NVDA    $13,125   10.4%    $6,300  +$6,825   +108.3%  +5.4%  🏆
  MSFT    $10,375   8.2%     $7,250  +$3,125   +43.1%   +2.5%
  AMZN    $3,960    3.1%     $2,600  +$1,360   +52.3%   +1.1%
  AAPL    $11,340   9.0%     $9,300  +$2,040   +21.9%   +1.6%
  GOOGL   $3,096    2.5%     $2,070  +$1,026   +49.6%   +0.8%
  JPM     $7,875    6.3%     $5,950  +$1,925   +32.4%   +1.5%
  VTI     $12,250   9.7%     $9,750  +$2,500   +25.6%   +2.0%
  JNJ     $5,920    4.7%     $6,200  -$280     -4.5%    -0.2% 📉

  Top Performer:    NVDA (+108.3%)
  Worst Performer:  JNJ (-4.5%) — only losing position

━━━ SECTOR ALLOCATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Sector                  Portfolio  S&P 500  Delta
  Technology              52.4%      29.0%    +23.4% ⚠ OVERWEIGHT
  Broad Market (ETF)       9.7%       —
  Financials               6.3%      13.0%    -6.7%  UNDERWEIGHT
  Healthcare               4.7%      12.5%    -7.8%  UNDERWEIGHT
  Consumer Discretionary   3.1%      10.5%    -7.4%  UNDERWEIGHT
  Unallocated (cash/other) 23.8%

  ⚠ CONCENTRATION WARNING: Technology sector at 52.4% (2× S&P weight)
  Top 3 holdings (NVDA+MSFT+AAPL) = 27.6% of portfolio

━━━ RISK ANALYSIS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Concentration Risk:   🔴 HIGH — Top 5 holdings = 41.2%
  Sector Risk:          🔴 HIGH — Technology 52.4%
  Correlation Risk:     🟡 ELEVATED — AAPL/MSFT/NVDA/GOOGL highly correlated
  Defensive Exposure:   🔴 LOW — Healthcare + Utilities < 5%
  Geographic:           🟡 US-only portfolio; no international diversification
  Dividend Yield:       ~0.8% estimated (low; growth-oriented portfolio)

━━━ REBALANCING RECOMMENDATIONS ━━━━━━━━━━━━━━━━━━━━━━━━━

  1. ⚠ Reduce technology concentration: consider trimming NVDA (sitting on
     +108% gain; represents outsized single-stock risk) and recycling into
     underweight sectors.
  2. Increase defensive exposure: add Healthcare (XLV) or Consumer Staples
     (XLP) to buffer against tech drawdowns. Target: 10–15% combined.
  3. Add international diversification: consider VEA (Developed Markets)
     or VWO (Emerging Markets) at 10–15% to reduce US-only risk.
  4. JNJ (-4.5%): small position, minor drag. Monitor thesis — if
     fundamentals intact, hold; if thesis broken, exit.
  5. Increase fixed income / alternatives if horizon or risk tolerance shifts
     (currently 0% bonds for a "medium-high" risk profile — appropriate for
     10+ year horizon but review if horizon shortens).

━━━ OVERALL PORTFOLIO HEALTH ━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Performance:      🟢 STRONG (+30.3% unrealized gains)
  Diversification:  🔴 POOR (tech concentration, US-only)
  Risk-Fit:         🟡 ACCEPTABLE for high-risk/long-horizon; concerning for
                       medium-risk investors
  Action Needed:    Yes — rebalance tech exposure; add defensive/intl. layer
```

## Skill Prompt

```
You are a portfolio analyst generating a comprehensive stock portfolio report.

Given the user's holdings, produce a full analysis with these sections:

**1. PORTFOLIO SUMMARY**
- Total current value (sum of shares × current price for each position).
- Total cost basis (sum of shares × avg cost).
- Total unrealized gain/loss ($ and %).
- Note: if cost basis not provided, skip P&L section and note the gap.

**2. PERFORMANCE ATTRIBUTION**
Build a table: Ticker | Current Value | Portfolio Weight (%) | Cost Basis | Gain/Loss ($) | Gain/Loss (%) | Portfolio Contribution (%).
- Portfolio Contribution = position gain/loss / total portfolio value.
- Sort by gain/loss % descending.
- Label top performer 🏆 and worst performer 📉.

**3. SECTOR ALLOCATION**
- Group holdings by sector (use standard GICS sectors).
- Show portfolio weight vs. S&P 500 weight (approximate: Tech 29%, Healthcare 12.5%, Financials 13%, Consumer Disc. 10.5%, Industrials 8.5%, Comm. Services 8.5%, Consumer Staples 6.5%, Energy 4%, Utilities 2.5%, Materials 2.5%, Real Estate 2.5%).
- Flag OVERWEIGHT (>1.5× S&P) and UNDERWEIGHT (<0.5× S&P) sectors.
- Note concentration warnings if any single sector > 35% or top 5 holdings > 45%.

**4. RISK ANALYSIS**
Assess these risk dimensions with 🟢/🟡/🔴 signals:
- Concentration risk: top 5 holdings as % of portfolio (target: <35%)
- Sector risk: any single sector domination
- Correlation risk: note clusters of highly correlated stocks (e.g., mega-cap tech)
- Defensive exposure: Healthcare + Utilities + Consumer Staples combined
- Geographic diversification: US vs. international exposure
- Dividend yield: estimate from known dividend payers

**5. REBALANCING RECOMMENDATIONS**
Give 3–5 specific, actionable recommendations based on the analysis:
- What to trim and why (taking profits, reducing concentration)
- What sectors/assets are underweight
- Diversification additions that fit the stated goal and risk tolerance
- Tax considerations if cost basis data provided (e.g., harvesting losses, holding winners)

**6. OVERALL PORTFOLIO HEALTH**
Score: Performance | Diversification | Risk-Fit (each 🟢/🟡/🔴)
One-line action summary: "No action needed" / "Minor rebalance suggested" / "Significant rebalancing recommended"

**NOTES**
- If sector for a ticker is unknown to you, note "sector unknown" rather than guessing.
- ETFs should be classified by their exposure (e.g., VTI = Broad Market, XLK = Technology).
- Always tailor recommendations to the user's stated goal and risk tolerance.
- Do not recommend specific buy prices or predict future returns.
```

## Notes

- The S&P 500 sector weights used are approximate (as of 2025); actual weights shift over time — users should verify current weights for precision.
- This skill uses provided cost basis for P&L; it does not fetch live prices. Users must supply current prices.
- For tax optimization analysis, pair with: `skills/personal-finance/tax-personal/`
- For individual stock deep-dives: `skills/investing/stock-analysis/buffett-checklist.md`
- For forward-looking portfolio valuation: `skills/financial-modeling/dcf-valuation/`
- Related: `skills/news-and-reporting/daily-digest/daily-financial-news-report.md`
