---
name: Morning Market Pre-Open Briefing
description: Generates a structured pre-market briefing covering overnight news, futures, key events, and actionable watch-list items before the trading day opens.
category: news-and-reporting/daily-digest
tags: [pre-market, morning-brief, futures, overnight-news]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-09
---

## Description

This skill compiles a concise, trader-focused morning briefing that synthesises overnight macro developments, U.S. and global equity futures, currency and commodity moves, scheduled economic releases, and corporate catalysts before the cash session opens. It is designed for active traders, portfolio managers, and market analysts who need a fast, structured read on the landscape before the opening bell. The output follows a standardised template so readers can scan it in under five minutes and immediately identify the key risks, themes, and tickers of the day.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a date and any raw context you have gathered — paste in futures levels, headlines, earnings results, or economic data points you want incorporated. The more source material you supply, the richer the briefing. If you provide no data, Claude will clearly label sections as requiring live data population and offer template placeholders with guidance on where to source each figure.

**Typical inputs:**
- Target date (required)
- Futures snapshot (e.g., ES, NQ, YM, RTY levels and % change)
- Overnight headlines or pasted news articles
- Earnings pre-market / after-close results
- Upcoming economic calendar events for the session
- Any specific sectors or tickers to highlight

## Example

**Input:**
> Date: 2026-04-09. Futures: S&P 500 futures (ES) -0.8%, Nasdaq (NQ) -1.2%, Dow (YM) -0.6%, Russell 2000 (RTY) -1.1%. Overnight news: China CPI came in at -0.1% YoY, missing estimates of +0.3%, raising deflation fears. Fed's Waller spoke late Tuesday, signalling rates on hold until at least Q3. Oil (WTI) $78.40, down 1.4% after API inventory build of 4.2M barrels. Gold $2,980, up 0.5%. USD/JPY 147.20. 10-yr Treasury yield 4.31%. Pre-market earnings: Delta Air Lines (DAL) beat EPS by $0.12, revenue in-line, guides FY above consensus. Levi Strauss (LEVI) missed revenue by 3%, cut guidance. Economic calendar: 8:30 AM Initial Jobless Claims est. 215K; 10:00 AM Wholesale Inventories. Sector watch: semiconductors under pressure after ASML export restriction headlines in Europe.

**Output:**

---

# 🌅 Morning Market Pre-Open Briefing — Thursday, April 9, 2026

**Generated:** Pre-market | **Session Bias:** Risk-Off | **Volatility Outlook:** Elevated

---

## 1. OVERNIGHT SNAPSHOT

| Asset | Level | Change |
|---|---|---|
| S&P 500 Futures (ES) | ~5,420 | -0.8% |
| Nasdaq Futures (NQ) | ~18,950 | -1.2% |
| Dow Futures (YM) | ~40,110 | -0.6% |
| Russell 2000 (RTY) | ~2,045 | -1.1% |
| WTI Crude Oil | $78.40 | -1.4% |
| Gold (XAU/USD) | $2,980 | +0.5% |
| USD/JPY | 147.20 | Flat |
| 10-Yr Treasury Yield | 4.31% | -2 bps |

**Session Tone:** Broad risk-off. Equities retreating across the board driven by China deflation data and semiconductor export headlines. Safe-haven bid in gold and bonds.

---

## 2. MACRO THEMES OF THE DAY

**🔴 Theme 1 — China Deflation Resurfacing**
China CPI printed -0.1% YoY vs. +0.3% estimate, the first negative reading since late 2023. This reignites concerns about domestic demand weakness and potential knock-on effects for global growth, commodity demand, and EM currencies. Watch: basic materials, energy, luxury goods with China exposure.

**🟡 Theme 2 — Fed on Hold, Waller Confirms Patience**
Governor Waller's late-Tuesday comments reinforced a data-dependent, no-rush posture into Q3. Rate-cut pricing has not materially shifted; the 2-year yield is steady. Short-term negative for rate-sensitive growth stocks expecting near-term relief.

**🔴 Theme 3 — Semiconductor Export Restrictions**
European session saw ASML shares slide on fresh headlines around potential tightened export curbs to China. U.S. chip names likely to open under pressure. Watch: NVDA, AMAT, LRCX, MU, KLAC.

**🟢 Theme 4 — Oil Inventory Overhang**
API reported a 4.2M barrel build, pressuring WTI to $78.40. EIA data follows at 10:30 AM. If confirmed, energy sector faces further headwinds intraday.

---

## 3. EARNINGS MOVERS (PRE-MARKET)

| Ticker | Result | Key Detail | Pre-Mkt Move |
|---|---|---|---|
| DAL | ✅ Beat | EPS +$0.12 vs est.; FY guide raised above consensus | +4–5% est. |
| LEVI | ❌ Miss | Revenue -3% vs est.; FY guidance cut | -8–10% est. |

**DAL Context:** Strength in domestic leisure and transatlantic premium demand cited. Fuel cost tailwind from lower oil helps margins. Positive read-through for UAL, AAL.
**LEVI Context:** Wholesale channel weakness in North America. Macro caution from management. Potential negative read-through for consumer discretionary apparel (PVH, HBI, VF Corp).

---

## 4. ECONOMIC CALENDAR

| Time (ET) | Event | Estimate | Previous | Importance |
|---|---|---|---|---|
| 8:30 AM | Initial Jobless Claims | 215K | 211K | 🔴 High |
| 10:00 AM | Wholesale Inventories (MoM) | +0.2% | +0.3% | 🟡 Medium |
| 10:30 AM | EIA Crude Oil Inventories | — | — | 🟡 Medium |

**Claims Watch:** A print above 225K would reinforce labour softening narrative and potentially accelerate rate-cut pricing. Below 210K = labour resilience, hawkish hold narrative strengthened.

---

## 5. SECTORS & TICKERS TO WATCH

- **Semiconductors (BEARISH BIAS):** NVDA, ASML, AMAT, LRCX — export restriction headlines + NQ underperformance
- **Airlines (BULLISH BIAS):** DAL, UAL, AAL — DAL beat and guidance raise
- **Energy (BEARISH BIAS):** XOM, CVX, OXY — oil inventory build, weak China demand
- **Apparel/Consumer Discretionary (BEARISH BIAS):** PVH, HBI — LEVI guidance cut read-through
- **Gold Miners (BULLISH BIAS):** NEM, AEM, GDX — gold catching safe-haven bid

---

## 6. KEY LEVELS TO MONITOR (S&P 500 FUTURES / ES)

- **Resistance:** 5,465 (overnight high), 5,490 (Wednesday close)
- **Support:** 5,400 (psychological), 5,375 (prior consolidation low)
- **Break scenario:** A move below 5,375 opens path toward 5,320 on elevated volume

---

## 7. RISK RADAR

| Risk | Probability | Impact |
|---|---|---|
| Claims print surprises high (>225K) | Medium | Market sells off further |
| EIA confirms API inventory build | Medium-High | Energy names extend losses |
| Additional semiconductor export headlines | Medium | Tech underperforms all session |
| USD/JPY breaks below 146.50 | Low | Yen carry unwind, broad risk-off |

---

## 8. BRIEFING SUMMARY (30-Second Read)

Markets open risk-off Thursday. China deflation data, semiconductor export fears, and a soft oil picture are the macro headwinds. DAL is the standout upside mover on earnings; LEVI a drag on consumer sentiment. Jobless claims at 8:30 AM are the day's pivotal data point. Defensive posture warranted until claims clear; semiconductor and energy sectors face the most acute pressure at the open.

---

*Data as of pre-market compilation. Verify all levels with live feeds before trading.*

---

## Skill Prompt

```
You are an expert financial markets analyst specialising in pre-market intelligence. When invoked, your task is to produce a complete Morning Market Pre-Open Briefing following the exact structure and standards below.

---

ROLE & OBJECTIVE
Produce a concise, trader-grade morning briefing that a professional market participant can read in under five minutes. The briefing must be factual, clearly sourced from the inputs provided, and free of unsupported speculation. Where live data is not supplied, insert clearly labelled placeholders and note where the data can be sourced.

---

REQUIRED INPUT PARAMETERS (request these if not provided)
1. Target date
2. Equity index futures snapshot (ES, NQ, YM, RTY — levels and % change vs. prior close)
3. Key overnight asset levels: WTI crude, Brent crude, gold, silver, DXY or major currency pairs, 2-yr and 10-yr Treasury yields
4. Overnight macro news headlines or full article text
5. Pre-market and after-hours earnings results (company, ticker, EPS beat/miss, revenue beat/miss, guidance)
6. Economic calendar events for the upcoming session (time, event name, consensus estimate, prior reading)
7. Any sector-specific developments or analyst actions the user wants highlighted

If any section's data is missing, insert: [DATA REQUIRED — source from: {suggested source}] and continue building the rest of the briefing.

---

BRIEFING STRUCTURE (follow this order exactly)

## 1. OVERNIGHT SNAPSHOT
- Produce a markdown table: Asset | Level | Change (%) | Direction arrow
- Include: major U.S. index futures, WTI, Brent, Gold, Silver, DXY, key FX pairs (EUR/USD, USD/JPY, GBP/USD), 2-yr yield, 10-yr yield, VIX futures if available
- Add a 1–2 sentence "Session Tone" summary label (e.g., Risk-Off / Risk-On / Mixed) with a brief rationale

## 2. MACRO THEMES OF THE DAY
- Identify 3–5 distinct macro themes driving overnight price action
- For each theme: assign a colour-coded label (🔴 Bearish, 🟢 Bullish, 🟡 Neutral/Watch), write 2–4 sentences of context, and list "Watch" tickers or sectors
- Rank themes by estimated market impact (highest first)
- Draw explicit connections between macro themes and asset class implications (e.g., China CPI miss → commodity demand → BHP, RIO, FCX; or Fed language → duration risk → TLT, rate-sensitive growth)

## 3. EARNINGS MOVERS
- Build a table: Ticker | Company | Beat/Miss | Key Metric | Pre-Mkt Move Est. | Guidance
- For each company, write 2–3 sentences of context including read-through implications for peers or sectors
- Separate pre-market reporters from after-hours reporters with clear sub-headers
- If no earnings, state "No major earnings this session" and note any upcoming earnings within 48 hours

## 4. ECONOMIC CALENDAR
- Build a table: Time (ET) | Event | Consensus Estimate | Previous | Importance (🔴 High / 🟡 Medium / ⚪ Low)
- After the table, write a "Data Watch" paragraph: identify the single most important release, explain why it matters today specifically, and describe the bull-case and bear-case reaction scenarios for equities and rates

## 5. SECTORS & TICKERS TO WATCH
- List 4–8 sectors or individual names with a directional bias (BULLISH / BEARISH / NEUTRAL) and a one-line rationale
- Prioritise names with the highest confluence of overnight catalysts (earnings + macro + technicals if levels are provided)

## 6. KEY TECHNICAL LEVELS
- For S&P 500 futures (ES) and Nasdaq futures (NQ), list:
  - Overnight high and low
  - Key resistance levels (1–3)
  - Key support levels (1–3)
  - Break scenario: what happens if support breaks or resistance is reclaimed
- If the user provides additional tickers, generate levels for those as well using any price data provided

## 7. RISK RADAR
- Table: Risk Event | Probability (Low/Medium/High) | Potential Market Impact | Affected Assets
- Include 4–6 risks: known scheduled risks (data, Fed speakers, earnings) and tail risks (geopolitical, surprise policy changes)

## 8. BRIEFING SUMMARY
- Write a 4–6 sentence executive summary a portfolio manager could read in 30 seconds
- Include: overall market bias, the 2 most important catalysts, the key data point to watch, and one tactical observation
- Do NOT introduce new information not already covered above

---

FORMATTING RULES
- Use markdown throughout: headers (##), tables, bold for key terms, colour-coded emojis for directional signals
- Keep each section tight: eliminate filler words and passive voice
- Numbers: always include units (%, $, bps); use consistent decimal places (2 for %, 2 for yields, nearest $0.10 for commodities)
- Time references: always specify timezone (ET)
- Directional signals: 🔴 = risk/bearish, 🟢 = opportunity/bullish, 🟡 = watch/neutral
- End every briefing with: "*Data as of pre-market compilation. Verify all levels with live feeds before trading.*"

---

ANALYTICAL STANDARDS
- Always identify second-order effects: if oil falls, note airline margin implications; if yen strengthens, note carry trade unwind risk
- Cross-asset linkages: explicitly connect macro data surprises to their most direct equity sector impact
- Avoid vague language ("markets are uncertain" — instead say "ES futures indicate a -0.8% open, with the tech-heavy NQ leading declines at -1.2%")
- When guidance or forward-looking estimates are discussed, clearly label them as estimates or management commentary, not facts
- Do not fabricate data. If a number is not in the user's inputs, use a placeholder and cite the correct source

---

TONE & VOICE
- Professional, direct, and precise — written for sophisticated market participants
- Neutral analytical stance: present bull and bear cases without editorial bias toward either
- Avoid hyperbole ("massive rally", "catastrophic sell-off") — use measured, quantified language
- Active voice throughout

---

OUTPUT LENGTH
Target 600–900 words for the full briefing body. The snapshot table and calendar table do not count toward the word target. Each section should be self-contained and scannable.
```

## Notes

**Data Requirements:**
- This skill requires the user to supply raw market data inputs; Claude does not have real-time data access. For production use, pipe in data from a financial data provider (Bloomberg, Refinitiv, Yahoo Finance API, Quandl, or a broker's API feed) before invoking the skill.
- Futures levels should be captured within 30 minutes of intended use to avoid stale data in the briefing.
- Earnings data should be sourced from the company's IR release or a reliable aggregator (Seeking Alpha, Earnings Whispers, FactSet).

**Known Limitations:**
- Without live data, sections 1, 3, and 4 will contain placeholders that must be manually populated.
- The skill does not perform technical chart analysis autonomously; key levels in Section 6 are derived only from price data the user explicitly provides.
- Pre-market moves for earnings are estimates based on reported results and guidance — actual open prices will differ.
- The skill is calibrated for U.S. equity markets (NYSE/NASDAQ). For non-U.S. session briefings (LSE, TSE, ASX), adjust timezone references and index