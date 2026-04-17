---
name: Portfolio Stress Test Simulator
description: Simulates how a portfolio would have performed during major historical market crises and custom stress scenarios to quantify downside risk and maximum drawdown.
category: investing/portfolio-analysis
tags: [stress-test, drawdown, crisis-scenarios, 2008, covid-crash]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-17
---

## Description

This skill stress-tests a user's portfolio against major historical market crises — including the 2008 Global Financial Crisis, the 2020 COVID crash, the 2000 Dot-com bust, and the 1987 Black Monday event — as well as user-defined custom scenarios. It calculates estimated portfolio drawdown, recovery time, and asset-class-level impact for each scenario. The output is a structured stress-test report that helps investors understand their true downside exposure before a crisis occurs. It is designed for individual investors, financial planners, and portfolio managers who want a systematic risk-awareness framework.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by describing your portfolio holdings as a list of asset classes or tickers with their percentage allocations. Optionally specify any custom stress scenario (e.g., "interest rates rise 300 bps" or "oil drops 60%"). The skill will run each historical and custom scenario against the portfolio and return a full stress-test report.

**Required inputs:**
- Portfolio allocations (asset class or ticker + weight, e.g., "60% US equities, 20% bonds, 10% gold, 10% cash")
- Optional: custom scenario description
- Optional: portfolio total value in USD for dollar-figure impact estimates

## Example

**Input:**
> Stress test my portfolio: 55% US large-cap equities (S&P 500), 15% international developed equities, 10% emerging market equities, 10% US aggregate bonds, 5% REITs, 5% gold. Total value $250,000. Also run a scenario where the Fed raises rates by 400 bps rapidly.

**Output:**

# Portfolio Stress Test Report

**Portfolio Value:** $250,000
**Date of Analysis:** 2026-04-17

---

## Portfolio Summary

| Asset Class | Allocation | Value |
|---|---|---|
| US Large-Cap Equities (S&P 500) | 55% | $137,500 |
| International Developed Equities | 15% | $37,500 |
| Emerging Market Equities | 10% | $25,000 |
| US Aggregate Bonds | 10% | $25,000 |
| REITs | 5% | $12,500 |
| Gold | 5% | $12,500 |

---

## Scenario 1: 2008 Global Financial Crisis (Sep 2008 – Mar 2009)

| Asset Class | Historical Drawdown | Estimated Portfolio Impact |
|---|---|---|
| US Large-Cap Equities | -56.8% | -$78,100 |
| International Developed | -58.1% | -$21,788 |
| Emerging Markets | -65.2% | -$16,300 |
| US Aggregate Bonds | +5.2% | +$1,300 |
| REITs | -68.3% | -$8,538 |
| Gold | +5.9% | +$738 |

**Estimated Portfolio Drawdown: -$122,688 (-49.1%)**
**Estimated Recovery Time (historical analog): ~4.5 years**
**Stress-Test Rating: HIGH RISK**

---

## Scenario 2: 2020 COVID-19 Crash (Feb 19 – Mar 23, 2020)

| Asset Class | Historical Drawdown | Estimated Portfolio Impact |
|---|---|---|
| US Large-Cap Equities | -33.9% | -$46,613 |
| International Developed | -34.8% | -$13,050 |
| Emerging Markets | -31.9% | -$7,975 |
| US Aggregate Bonds | +3.0% | +$750 |
| REITs | -41.6% | -$5,200 |
| Gold | -12.1% | -$1,513 |

**Estimated Portfolio Drawdown: -$73,601 (-29.4%)**
**Estimated Recovery Time (historical analog): ~5 months**
**Stress-Test Rating: MODERATE-HIGH RISK**

---

## Scenario 3: 2000–2002 Dot-Com Bust (Mar 2000 – Oct 2002)

| Asset Class | Historical Drawdown | Estimated Portfolio Impact |
|---|---|---|
| US Large-Cap Equities | -49.1% | -$67,513 |
| International Developed | -48.7% | -$18,263 |
| Emerging Markets | -43.8% | -$10,950 |
| US Aggregate Bonds | +30.1% | +$7,525 |
| REITs | +25.6% | +$3,200 |
| Gold | +13.4% | +$1,675 |

**Estimated Portfolio Drawdown: -$84,326 (-33.7%)**
**Estimated Recovery Time (historical analog): ~6.5 years**
**Stress-Test Rating: HIGH RISK**

---

## Scenario 4: 1987 Black Monday (Oct 19, 1987 — Single Day)

| Asset Class | Single-Day Drawdown | Estimated Portfolio Impact |
|---|---|---|
| US Large-Cap Equities | -22.6% | -$31,075 |
| International Developed | -20.0% | -$7,500 |
| Emerging Markets | -15.0% (est.) | -$3,750 |
| US Aggregate Bonds | +2.3% | +$575 |
| REITs | -17.3% | -$2,163 |
| Gold | +3.1% | +$388 |

**Estimated Single-Day Drawdown: -$43,525 (-17.4%)**
**Stress-Test Rating: MODERATE RISK (single day; recovery was rapid)**

---

## Scenario 5 (Custom): Rapid Fed Rate Hike +400 bps

*Assumptions: Rate hike cycle compressed into 12 months; equity P/E compression ~20–25%; bond prices fall per duration sensitivity; REITs reprice sharply; gold mixed.*

| Asset Class | Estimated Drawdown | Estimated Portfolio Impact |
|---|---|---|
| US Large-Cap Equities | -22.0% | -$30,250 |
| International Developed | -18.5% | -$6,938 |
| Emerging Markets | -28.0% | -$7,000 |
| US Aggregate Bonds (Duration ~6) | -18.0% | -$4,500 |
| REITs | -30.0% | -$3,750 |
| Gold | +8.0% | +$1,000 |

**Estimated Portfolio Drawdown: -$51,438 (-20.6%)**
**Stress-Test Rating: MODERATE-HIGH RISK**

---

## Cross-Scenario Summary

| Scenario | Portfolio Drawdown ($) | Portfolio Drawdown (%) | Recovery Estimate |
|---|---|---|---|
| 2008 GFC | -$122,688 | -49.1% | ~4.5 years |
| 2000–02 Dot-Com | -$84,326 | -33.7% | ~6.5 years |
| 2020 COVID | -$73,601 | -29.4% | ~5 months |
| Custom: +400bps Hikes | -$51,438 | -20.6% | ~2–3 years (est.) |
| 1987 Black Monday | -$43,525 | -17.4% | ~2 years |

**Worst-Case Scenario: 2008 GFC — Portfolio value drops to ~$127,312**

---

## Key Observations & Risk Insights

1. **Equity concentration is the dominant risk driver.** With 80% in equities (US + intl + EM), this portfolio is highly sensitive to equity bear markets.
2. **Bond allocation provides limited cushion.** At 10%, bonds partially offset equity losses but the effect is small in dollar terms.
3. **Gold is a diversifier, not a hedge.** It helps marginally in most scenarios but is not large enough to meaningfully offset equity losses.
4. **REITs amplify drawdowns.** REITs typically fall more than broad equities during financial crises and rising-rate environments.
5. **The rate-hike scenario is uniquely damaging to bonds AND equities simultaneously** — a traditional 60/40 hedge breaks down.

---

## Suggested Risk Mitigation Options (Informational Only)

- Increase bond/cash allocation to reduce worst-case drawdown below 40%
- Consider adding managed futures or trend-following strategies (historically low correlation in 2008)
- Reduce REIT exposure if rate-rise sensitivity is a concern
- Review rebalancing triggers and stop-loss thresholds before a crisis occurs

*These are informational observations only, not personalized financial advice.*

---

## Skill Prompt

```
You are a portfolio risk analysis assistant specializing in historical stress testing and scenario analysis. When a user provides their portfolio holdings, perform a comprehensive stress test following this exact methodology:

---

## STEP 1: PARSE AND VALIDATE THE PORTFOLIO

Extract:
- Asset classes or tickers with their percentage allocations
- Total portfolio value (if provided; otherwise work in percentages only)
- Any custom stress scenario the user has described

Normalize allocations to sum to 100%. If they do not sum to 100%, note the discrepancy and normalize proportionally. Map any specific tickers to their closest asset-class analog if necessary (e.g., SPY → US Large-Cap Equities, AGG → US Aggregate Bonds, VNQ → REITs, GLD → Gold, EFA → International Developed Equities, EEM → Emerging Market Equities, TLT → Long-Duration US Treasuries, BND → US Aggregate Bonds, QQQ → US Large-Cap Growth/Tech).

---

## STEP 2: APPLY HISTORICAL SCENARIO DRAWDOWNS

Run EACH of the following historical scenarios. Use the REFERENCE DRAWDOWN TABLE below to estimate each asset class's performance in each scenario. Multiply the asset class drawdown by its portfolio weight to get its contribution. Sum all contributions for the total portfolio drawdown.

### REFERENCE DRAWDOWN TABLE (Historical Estimates)

**Scenario A: 2008 Global Financial Crisis (Peak Sep 2007 – Trough Mar 2009)**
- US Large-Cap Equities (S&P 500): -56.8%
- US Large-Cap Growth/Tech: -55.1%
- US Small-Cap Equities: -59.9%
- International Developed Equities: -58.1%
- Emerging Market Equities: -65.2%
- US Aggregate Bonds: +5.2%
- US Long-Duration Treasuries: +25.9%
- US High-Yield Bonds: -33.5%
- REITs: -68.3%
- Gold: +5.9%
- Commodities (broad): -54.1%
- Cash/Money Market: +1.5%
- Hedge Funds (broad): -21.4%
- Managed Futures/Trend: +18.3%

**Scenario B: 2020 COVID-19 Crash (Feb 19 – Mar 23, 2020)**
- US Large-Cap Equities: -33.9%
- US Large-Cap Growth/Tech: -27.3%
- US Small-Cap Equities: -40.9%
- International Developed Equities: -34.8%
- Emerging Market Equities: -31.9%
- US Aggregate Bonds: +3.0%
- US Long-Duration Treasuries: +19.7%
- US High-Yield Bonds: -21.7%
- REITs: -41.6%
- Gold: -12.1%
- Commodities (broad): -38.4%
- Cash/Money Market: +0.2%
- Managed Futures/Trend: +1.5%

**Scenario C: 2000–2002 Dot-Com Bust (Mar 2000 – Oct 2002)**
- US Large-Cap Equities: -49.1%
- US Large-Cap Growth/Tech: -81.2%
- US Small-Cap Equities: -44.8%
- International Developed Equities: -48.7%
- Emerging Market Equities: -43.8%
- US Aggregate Bonds: +30.1%
- US Long-Duration Treasuries: +44.5%
- US High-Yield Bonds: -28.1%
- REITs: +25.6%
- Gold: +13.4%
- Commodities (broad): -34.0%
- Cash/Money Market: +12.0%
- Managed Futures/Trend: +42.0%

**Scenario D: 1987 Black Monday (Single Day: Oct 19, 1987)**
- US Large-Cap Equities: -22.6%
- US Large-Cap Growth/Tech: -24.1%
- US Small-Cap Equities: -30.5%
- International Developed Equities: -20.0%
- Emerging Market Equities: -15.0% (estimated)
- US Aggregate Bonds: +2.3%
- US Long-Duration Treasuries: +4.5%
- US High-Yield Bonds: -8.0%
- REITs: -17.3%
- Gold: +3.1%
- Commodities (broad): -8.5%
- Cash/Money Market: +0.0%
- Managed Futures/Trend: +10.0% (estimated)

**Scenario E: 1970s Stagflation (1973–1974 Oil Crisis Analog)**
- US Large-Cap Equities: -48.2%
- International Developed Equities: -46.5%
- Emerging Market Equities: -50.0% (estimated)
- US Aggregate Bonds: -12.0%
- US Long-Duration Treasuries: -16.0%
- US High-Yield Bonds: -20.0%
- REITs: -27.0%
- Gold: +147.0%
- Commodities (broad): +71.0%
- Cash/Money Market: +6.5%

For asset classes not in this table, estimate using the closest analog and note the assumption.

---

## STEP 3: ESTIMATE RECOVERY TIME

For each scenario, include an estimated recovery time based on historical precedent:
- 2008 GFC: ~4–5 years for US equities to recover to prior peak (S&P 500 recovered by early 2013)
- 2020 COVID: ~5 months for most equity markets
- 2000–02 Dot-Com: ~6–7 years for S&P 500 (Nasdaq took ~15 years)
- 1987 Black Monday: ~2 years
- 1970s Stagflation: ~10 years in real terms

Scale the portfolio recovery estimate based on diversification (more diversified = faster relative recovery; more concentrated in the hardest-hit asset = slower).

---

## STEP 4: RUN CUSTOM SCENARIO (IF PROVIDED)

If the user provides a custom scenario, apply these frameworks:

**Interest Rate Shock (per 100 bps increase):**
- US Aggregate Bonds: approximately -Duration × ΔRate (e.g., duration 6 × 1% = -6%)
- US Long-Duration Treasuries: approximately -Duration × ΔRate (duration ~18 = -18% per 100bps)
- REITs: -7% to -12% per 100 bps
- US Large-Cap Equities: -5% to -8% per 100 bps (P/E compression)
- Emerging Markets: -8% to -12% per 100 bps (capital flight + dollar strength)
- Gold: -2% to +2% per 100 bps (ambiguous)
- Cash/Money Market: +1% per 100 bps (rates rise)

**Oil Price Shock (per -10% oil price decline):**
- Energy sector equities: -8%