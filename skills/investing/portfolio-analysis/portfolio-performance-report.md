---
name: Portfolio Performance Report Generator
description: Generate a detailed periodic portfolio performance report with returns, benchmark comparison, attribution, risk metrics, and commentary
category: investing/portfolio-analysis
tags: [portfolio-report, performance, benchmark, attribution, sharpe-ratio, monthly-report]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Produces a professional-grade portfolio performance report for any period (monthly, quarterly, annual). Takes opening/closing values, individual position returns, and benchmark returns, then computes total return, alpha, attribution by position, risk-adjusted metrics (Sharpe, Sortino), and narrative commentary. Suitable for personal reporting or sharing with advisors.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Provide:
- Reporting period (e.g., Q4 2025, January 2026)
- Opening and closing portfolio value
- Net cash flows during the period (deposits/withdrawals)
- Benchmark return for the same period (e.g., S&P 500 return)
- Individual position returns or opening/closing values per holding
- (Optional) Risk-free rate, prior period return for YTD context

## Example

**Input:**
```
Period: Q4 2025 (Oct 1 – Dec 31, 2025)
Opening value: $115,000
Closing value: $127,500
Cash flows: +$2,000 deposit on Oct 15
Benchmark (S&P 500 Q4 return): +8.2%
Risk-free rate (annualized): 5.0% → quarterly: 1.25%

Position returns:
NVDA: opened $12,000 / closed $15,600  (+30.0%)
AAPL: opened $10,500 / closed $11,340  (+8.0%)
MSFT: opened $9,800  / closed $10,780  (+10.0%)
AMZN: opened $7,200  / closed $7,776   (+8.0%)
GOOGL:opened $5,400  / closed $5,724   (+6.0%)
JNJ:  opened $6,300  / closed $5,985   (-5.0%)
JPM:  opened $7,000  / closed $7,700   (+10.0%)
VTI:  opened $11,200 / closed $12,040  (+7.5%)
Cash: opened $45,600 / closed $50,556  (interest + deposit)
```

**Output:**
```
╔══════════════════════════════════════════════════════════════╗
║     PORTFOLIO PERFORMANCE REPORT — Q4 2025                   ║
║     Oct 1 – Dec 31, 2025                                     ║
╚══════════════════════════════════════════════════════════════╝

━━━ RETURN SUMMARY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Opening Value:         $115,000
  + Cash Flows:          +$2,000  (deposit Oct 15)
  Closing Value:         $127,500

  Time-Weighted Return:  +9.1%      🟢
  Benchmark (S&P 500):   +8.2%
  Alpha (vs. benchmark): +0.9%     🟢 Outperformed

  YTD Return:            [not provided]
  Annualized (if 1yr):   ~38.6% (extrapolated — 1-quarter snapshot)

━━━ PERFORMANCE ATTRIBUTION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Position   Open      Close     Return  Weight  Contribution
  NVDA       $12,000   $15,600   +30.0%  10.4%   +3.1%  🏆
  JPM        $7,000    $7,700    +10.0%  6.1%    +0.6%
  MSFT       $9,800    $10,780   +10.0%  8.5%    +0.9%
  AAPL       $10,500   $11,340   +8.0%   9.1%    +0.7%
  AMZN       $7,200    $7,776    +8.0%   6.3%    +0.5%
  VTI        $11,200   $12,040   +7.5%   9.7%    +0.7%
  GOOGL      $5,400    $5,724    +6.0%   4.7%    +0.3%
  Cash/Other $45,600   $50,556   +1.0%   39.6%   +0.4%
  JNJ        $6,300    $5,985    -5.0%   5.2%    -0.3%  📉

  Best contributor:  NVDA (+3.1% to portfolio)
  Worst contributor: JNJ (-0.3% to portfolio)

━━━ RISK-ADJUSTED METRICS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Quarterly Return:        +9.1%
  Risk-Free Rate (qtr):    +1.25%
  Excess Return:           +7.85%

  Note: Sharpe and Sortino require monthly/daily return series.
  With single-period data, showing excess return vs. risk-free only.
  Excess return vs. benchmark: +0.9% (alpha)

━━━ QUARTERLY COMMENTARY ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  The portfolio delivered +9.1% in Q4 2025, outperforming the S&P 500
  (+8.2%) by 90 basis points.

  Key driver: NVDA (+30%) was the standout performer, contributing 3.1
  percentage points to total return — nearly a third of total portfolio gains
  from a single position. This reflects continued AI infrastructure demand
  but also highlights growing single-stock concentration risk.

  Broad market exposure via VTI (+7.5%) and mega-cap tech (MSFT, AAPL, AMZN)
  performed broadly in line with the benchmark.

  JNJ was the only losing position (-5.0%), though its contribution was minor
  (-0.3%) given relatively small weighting.

  The 39.6% cash allocation was a modest drag relative to the equity rally,
  but provides dry powder and reduces downside exposure.

━━━ FORWARD NOTES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  • NVDA now likely represents 12–13% of portfolio after strong run —
    review concentration vs. risk tolerance.
  • JNJ thesis review recommended; continued underperformance warrants
    position reassessment.
  • Consider deploying some cash allocation if conviction in thesis is high.
```

## Skill Prompt

```
You are a portfolio manager generating a formal periodic performance report.

Given the user's portfolio data for the reporting period, produce a structured report:

**1. RETURN SUMMARY**
Calculate Time-Weighted Return (TWR):
- If no intra-period cash flows: TWR = (Ending Value / Beginning Value) − 1
- With cash flows: use Modified Dietz method:
  Modified Dietz Return = (Ending Value − Beginning Value − Cash Flows) /
                          (Beginning Value + Weighted Cash Flows)
  where Weighted Cash Flow = CF × (Days Remaining in Period / Total Days)
- Show: Opening Value, Cash Flows, Closing Value, TWR.
- Compare to benchmark: show alpha (TWR − benchmark return).
- If prior period data provided, show YTD return.

**2. PERFORMANCE ATTRIBUTION**
Build a contribution table:
Position | Open Value | Close Value | Return % | Portfolio Weight | Contribution %
- Weight = opening position value / opening portfolio value.
- Contribution = position return × weight.
- Sort by contribution descending.
- Label top contributor 🏆 and worst contributor 📉.
- Sum contributions (should approximately equal portfolio TWR; note any gap due to cash flows).

**3. RISK-ADJUSTED METRICS**
If only a single period is provided:
- Show excess return over risk-free rate (return − risk-free rate for period).
- Note that Sharpe/Sortino require a series of periodic returns and cannot be calculated from one data point.
If multiple period returns are provided:
- Sharpe Ratio = Mean(excess returns) / StdDev(returns) × √n (annualized)
- Sortino Ratio = Mean(excess returns) / StdDev(negative returns only) × √n
- Max Drawdown if high/low values provided.

**4. QUARTERLY / PERIOD COMMENTARY**
Write a 3–4 paragraph narrative:
- Overall performance vs. benchmark.
- Key drivers (top contributors and why they mattered).
- Notable laggards and whether the thesis remains intact.
- Portfolio-level observations (concentration, cash drag, sector rotation).

**5. FORWARD NOTES**
2–4 specific action items or watch points for the next period, based on what the data reveals.

**FORMATTING**
- Use box headers and dividers.
- Show all calculations explicitly.
- If data is missing for any metric, state what is needed rather than estimating.
```

## Notes

- Modified Dietz is the industry-standard approximation for time-weighted return with cash flows. For precision, a true TWR requires daily portfolio valuation — note this limitation.
- Sharpe/Sortino ratios require at least 12 monthly data points for statistical reliability.
- This skill does not fetch live prices; users must supply opening and closing values.
- For a forward-looking portfolio view: `skills/investing/portfolio-analysis/stock-portfolio-analyzer.md`
- For individual position analysis: `skills/investing/stock-analysis/buffett-checklist.md`
