---
name: Macro Economic Indicator Dashboard
description: Synthesizes and interprets key macroeconomic indicators into a structured dashboard summary with trend analysis and investment implications.
category: data-and-research/economic-indicators
tags: [cpi, gdp, pmi, macro, economic-indicators]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-31
---

## Description

This skill compiles and interprets the most important macroeconomic indicators — including GDP growth, CPI inflation, PMI readings, unemployment, yield curves, and more — into a single cohesive dashboard. It is designed for investors, analysts, and economists who want a rapid, structured snapshot of the macroeconomic environment. The skill evaluates each indicator against historical norms, identifies directional trends, assigns a composite macro regime label, and surfaces potential implications for asset classes. Output is formatted as a scannable dashboard with color-coded signal columns and a narrative summary.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a set of recent macroeconomic data points. You may supply as few or as many indicators as you have available. Inputs can be pasted as plain text, a table, or a bullet list. Specify the country or region (default: United States) and the reporting period. Optionally, request a specific output focus such as "recession risk", "inflation regime", or "central bank outlook".

**Supported indicators (include any available):**
- GDP growth (QoQ annualized or YoY %)
- CPI / Core CPI (YoY %)
- PCE / Core PCE (YoY %)
- PPI (YoY %)
- ISM / PMI Manufacturing and Services (index level)
- Unemployment rate (%)
- Non-Farm Payrolls (monthly change)
- Retail Sales (MoM or YoY %)
- Industrial Production (MoM %)
- Consumer Confidence / Sentiment index
- 10Y–2Y Treasury yield spread (bps)
- Federal Funds Rate / Policy rate (%)
- M2 Money Supply growth (YoY %)
- Housing Starts / Building Permits
- Trade Balance

## Example

**Input:**
```
Region: United States
Period: Q1 2026

GDP (Q4 2025, QoQ annualized): 2.3%
CPI (Feb 2026, YoY): 3.1%
Core CPI (Feb 2026, YoY): 3.4%
Core PCE (Jan 2026, YoY): 2.8%
ISM Manufacturing PMI (Feb 2026): 49.8
ISM Services PMI (Feb 2026): 53.5
Unemployment Rate (Feb 2026): 4.1%
Non-Farm Payrolls (Feb 2026): +151,000
Retail Sales (Jan 2026, MoM): -0.9%
10Y-2Y Yield Spread: +18 bps
Federal Funds Rate: 4.25%–4.50%
Consumer Confidence (Feb 2026): 98.3
```

**Output:**

```
╔══════════════════════════════════════════════════════════════════╗
║        MACRO ECONOMIC INDICATOR DASHBOARD — US / Q1 2026        ║
╚══════════════════════════════════════════════════════════════════╝

MACRO REGIME:  Late-Cycle Expansion / Disinflation in Progress
RISK POSTURE:  CAUTIOUS — Slowing momentum, residual inflation

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 INDICATOR SCORECARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Category          Indicator          Value      Trend    Signal
 ─────────────────────────────────────────────────────────────────
 GROWTH            GDP (QoQ Ann.)     2.3%       ↓        NEUTRAL
                   ISM Mfg PMI        49.8       →        WEAK
                   ISM Svcs PMI       53.5       →        POSITIVE
                   NFP (Monthly)      +151K      ↓        NEUTRAL
                   Retail Sales MoM   -0.9%      ↓        WEAK
                   Indust. Prod.      N/A        —        N/A

 INFLATION         CPI YoY            3.1%       ↓        CAUTION
                   Core CPI YoY       3.4%       ↓        CAUTION
                   Core PCE YoY       2.8%       ↓        NEUTRAL
                   PPI YoY            N/A        —        N/A

 LABOR             Unemployment       4.1%       ↑        NEUTRAL
                   NFP                +151K      ↓        NEUTRAL

 MONETARY          Fed Funds Rate     4.25–4.50% →        TIGHT
                   10Y–2Y Spread      +18 bps    ↑        CAUTIOUS
                   M2 Growth          N/A        —        N/A

 SENTIMENT         Consumer Conf.     98.3       ↓        WEAK

 Signal Key:  POSITIVE ▲  NEUTRAL ●  CAUTIOUS ▼  WEAK ✕

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 COMPOSITE SCORES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Growth Score:      5 / 10  — Modest expansion; manufacturing sub-50
 Inflation Score:   5 / 10  — Disinflating but above 2% Fed target
 Labor Score:       6 / 10  — Healthy but decelerating
 Financial Cond.:   5 / 10  — Tight policy; curve barely positive
 Sentiment Score:   4 / 10  — Below trend; retail sales confirm caution

 OVERALL MACRO SCORE:  5.0 / 10  (Neutral-to-Cautious)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 KEY OBSERVATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. DISINFLATION CONTINUING BUT INCOMPLETE
   Core PCE at 2.8% is approaching the Fed's 2% target, but Core CPI
   at 3.4% suggests services inflation remains stubborn. The "last mile"
   of disinflation is proving sticky, delaying rate cuts.

2. MANUFACTURING CONTRACTION RISK
   ISM Manufacturing at 49.8 sits just below the 50 expansion/contraction
   threshold. Two consecutive readings below 50 would confirm a
   manufacturing recession, a pattern historically preceding broader
   slowdowns by 2–4 quarters.

3. CONSUMER UNDER PRESSURE
   Retail Sales falling -0.9% MoM alongside declining Consumer Confidence
   (98.3 vs. long-run avg ~100) signals that higher-for-longer rates are
   beginning to bite household spending — a key risk to the GDP outlook.

4. LABOR MARKET NORMALIZING, NOT COLLAPSING
   NFP of +151K and unemployment at 4.1% describe a cooling rather than
   a cracking labor market. The Sahm Rule threshold (0.5pp rise in 3-mo
   avg unemployment) has not been triggered.

5. YIELD CURVE BARELY POSITIVE
   A +18 bps 10Y–2Y spread represents a very recent re-steepening from
   deep inversion. Historically, the recession signal fires not during
   inversion but 6–18 months after the curve re-steepens — warranting
   close monitoring.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CENTRAL BANK OUTLOOK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Current Policy Rate:   4.25–4.50%
 Neutral Rate Est.:     ~2.5–3.0% (Fed median)
 Policy Stance:         Restrictive
 Likely Next Move:      CUT (data-dependent; mid-2026 base case)
 Rate Cut Probability:  Gradual easing cycle; 2–3 cuts likely in 2026
                        contingent on Core PCE approaching 2.3% or below

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ASSET CLASS IMPLICATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Asset Class          Implication                          Tilt
 ─────────────────────────────────────────────────────────────────
 Equities (US)        Late-cycle; earnings risk rising      NEUTRAL
 Fixed Income         Rate cuts priced in; duration adds    OVERWEIGHT
 Credit (HY)          Spreads may widen if growth slows     UNDERWEIGHT
 Commodities          Weak demand signal; USD sticky        NEUTRAL
 USD                  Higher-for-longer supports USD        SLIGHT +
 EM Assets            USD strength is headwind              CAUTIOUS
 Real Estate          Rate-sensitive; improving slowly      NEUTRAL

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 RECESSION PROBABILITY ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 12-Month Recession Probability (qualitative):  25–35%
 Primary risk factors:
   • Consumer spending deceleration
   • Manufacturing contraction extending
   • Yield curve re-steepening signal (lagged)
   • Prolonged restrictive monetary policy

 Mitigating factors:
   • Services sector remains expansionary
   • Labor market still adding jobs
   • Disinflation allows Fed optionality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 DATA GAPS & MONITORING PRIORITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 Missing data:  PPI, Industrial Production, M2, Housing Starts
 Watch closely:
   [!] ISM Manufacturing — confirm if below 50 persists
   [!] Core PCE — next release critical for Fed timing
   [!] NFP trend — watch for sub-100K prints
   [!] Retail Sales — confirm whether Jan was weather-related
```

## Skill Prompt

```
You are a senior macroeconomic analyst. Your task is to synthesize a set of macroeconomic data points provided by the user into a comprehensive, structured Macro Economic Indicator Dashboard. Follow the methodology and output format below precisely.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — DATA INTAKE & VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Identify the region (default: United States) and reporting period.
- Catalog all provided indicators into these categories:
  • GROWTH: GDP, PMI Manufacturing, PMI Services, Industrial Production, Retail Sales, Housing Starts
  • INFLATION: CPI, Core CPI, PCE, Core PCE, PPI, Breakeven Inflation rates
  • LABOR: Unemployment Rate, Non-Farm Payrolls, Average Hourly Earnings, Job Openings (JOLTS)
  • MONETARY: Policy Rate, Yield Curve (10Y–2Y spread), M2 Money Supply growth, Credit spreads
  • SENTIMENT: Consumer Confidence, Consumer Sentiment (U. Michigan), Business Confidence
- Note any missing indicators. Do not fabricate data. Mark gaps clearly as "N/A".

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — INDIVIDUAL INDICATOR ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For each indicator provided, assign:

TREND (directional arrow):
  ↑ = improving/rising  ↓ = deteriorating/falling  → = stable/flat

SIGNAL (qualitative assessment relative to thresholds):
  POSITIVE  — Reading is clearly healthy and supports expansion
  NEUTRAL   — Reading is within normal range; no strong directional signal
  CAUTIOUS  — Reading is approaching a warning threshold or mixed
  WEAK      — Reading is clearly negative or contractionary

Apply these reference thresholds:
  GDP QoQ Ann.: >3% = POSITIVE, 1–3% = NEUTRAL, 0–1% = CAUTIOUS, <0% = WEAK
  CPI YoY:      <2% = NEUTRAL, 2–3% = CAUTIOUS, >3% = WEAK (for a 2%-target central bank)
  Core PCE YoY: <2.3% = POSITIVE, 2.3–2.7% = NEUTRAL, 2.7–3.2% = CAUTIOUS, >3.2% = WEAK
  ISM PMI (Mfg/Svcs): >55 = POSITIVE, 50–55 = NEUTRAL, 48–50 = CAUTIOUS, <48 = WEAK
  Unemployment: <4% = POSITIVE, 4–4.5% = NEUTRAL, 4.5–5% = CAUTIOUS, >5% = WEAK
  NFP Monthly:  >200K = POSITIVE, 100–200K = NEUTRAL, 50–100K = CAUTIOUS, <50K or negative = WEAK
  10Y–2Y Spread: >50bps = POSITIVE, 0–50bps = CAUTIOUS, negative = WEAK (lagged recession risk)
  Consumer Conf.: >110 = POSITIVE, 90–110 = NEUTRAL, 75–90 = CAUTIOUS