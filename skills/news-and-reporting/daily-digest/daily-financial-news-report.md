---
name: Daily Financial News Report
description: Analyze a batch of financial news headlines and articles to produce a structured daily market briefing with key themes, market-moving events, and investment implications
category: news-and-reporting/daily-digest
tags: [daily-briefing, financial-news, market-summary, macro, sentiment]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Takes a paste of financial news headlines, article snippets, or a raw news feed and transforms it into a clean, structured daily briefing. Covers macro events, equity movers, sector themes, central bank signals, geopolitical risks, and a forward-looking watchlist. Ideal for morning prep before markets open or end-of-day recaps.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Paste your news headlines or article excerpts. Sources can include:
- RSS feeds or news aggregators (Bloomberg, Reuters, WSJ, FT, CNBC)
- Google News finance section
- Reddit r/investing, r/wallstreetbets notable posts
- Any plain-text news dump

The skill works with just headlines, or with headlines + article snippets for deeper analysis.

**Format:**
```
Date: [YYYY-MM-DD]
[Paste headlines and/or article excerpts here]
```

## Example

**Input:**
```
Date: 2026-02-25

- Fed signals possible rate pause amid cooling inflation data; CPI came in at 2.7% vs 2.9% expected
- Nvidia Q4 earnings beat: EPS $5.16 vs $4.84 expected; data center revenue up 93% YoY
- Apple reportedly cutting Vision Pro production by 50% due to weak demand
- China's PMI drops to 48.1, signaling manufacturing contraction for third straight month
- Oil slides 2.3% after IEA raises demand growth forecast cut; Brent at $74.40
- Treasury yields fall: 10Y at 4.21%, 2Y at 4.55%; yield curve inversion narrows
- JPMorgan upgrades Amazon to Overweight, raises PT to $240
- Regional bank index down 1.8%; CRE loan concerns resurface after Signature Bank filing
```

**Output:**
```
╔══════════════════════════════════════════════════════╗
║     DAILY FINANCIAL BRIEFING — 2026-02-25            ║
╚══════════════════════════════════════════════════════╝

━━━ MACRO SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Fed / Rates
  • CPI 2.7% (beat expectations of 2.9%) → disinflation trend intact
  • Fed signals potential rate pause — dovish shift; market pricing 2 cuts in 2026
  • 10Y Treasury: 4.21% ↓ | 2Y: 4.55% ↓ | Yield curve inversion narrowing ✅
  Signal: 🟢 Rates tailwind for equities and duration

  Global
  • China PMI 48.1 — 3rd straight month of contraction ⚠
  Signal: 🔴 EM and commodity demand risk; watch China-exposed names

━━━ EQUITY HIGHLIGHTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Beats / Upgrades
  • NVDA ✅ EPS +6.6% beat; data center +93% YoY → AI capex cycle continues
  • AMZN ↑ JPMorgan upgrade to Overweight, PT $240 → cloud + retail optionality

  Misses / Warnings
  • AAPL ⚠ Vision Pro production cut 50% → consumer hardware demand concern
  • Regional Banks 🔴 -1.8% on CRE loan concerns; sector under pressure

━━━ SECTOR THEMES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🟢 Tailwinds         AI / Semiconductors (NVDA beat), Big Tech (rate pause)
  🟡 Mixed             Energy (oil -2.3%, IEA demand cut vs. OPEC supply)
  🔴 Headwinds         Regional Banks (CRE), Consumer Hardware (AAPL), China-linked

━━━ COMMODITIES & FX ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Oil (Brent): $74.40  ↓ 2.3%   (IEA demand cut)
  Gold:        [not mentioned]
  USD:         [not mentioned — likely soft given dovish Fed signal]

━━━ OVERALL MARKET SENTIMENT ━━━━━━━━━━━━━━━━━━━━━━━

  Signal: 🟡 MIXED-BULLISH
  Bullish: Disinflation + Fed pause signal + NVDA AI beat
  Bearish: China weakness, regional bank stress, AAPL hardware miss

━━━ WATCHLIST FOR TOMORROW ━━━━━━━━━━━━━━━━━━━━━━━━━

  📌 Watch NVDA reaction at open — often sets tech tone
  📌 Monitor regional bank ETF (KRE) for CRE contagion signals
  📌 China data follow-through: watch FXI, copper, commodity exporters
  📌 Fed speaker calendar — any push-back on pause narrative?
```

## Skill Prompt

```
You are a senior financial markets analyst producing a daily briefing from raw news input.

Given the provided news headlines and/or article excerpts, produce a structured Daily Financial Briefing with the following sections:

**1. MACRO SNAPSHOT**
For each macro theme present in the news (Fed/rates, inflation, GDP, employment, geopolitics, central banks):
- Summarize the key development in 1–2 bullet points.
- Assign a market signal: 🟢 Bullish / 🟡 Neutral / 🔴 Bearish — with a one-line rationale.
- Note the direction of key rates/yields if mentioned.

**2. EQUITY HIGHLIGHTS**
Separate into:
- Beats / Upgrades / Positive catalysts (with ticker if mentioned)
- Misses / Downgrades / Negative catalysts (with ticker if mentioned)
For each: state what happened and the key number or metric.

**3. SECTOR THEMES**
Identify which sectors appear as tailwinds, mixed, or headwinds based on the news.
Format: 🟢 Tailwinds | 🟡 Mixed | 🔴 Headwinds — with sector names and the driving news item.

**4. COMMODITIES & FX**
Extract any commodity prices, moves, or FX developments mentioned.
If not mentioned, note "not reported."

**5. OVERALL MARKET SENTIMENT**
Give a single composite signal: 🟢 Bullish / 🟡 Mixed-Bullish / 🟠 Mixed-Bearish / 🔴 Bearish.
List the top 2–3 bullish factors and top 2–3 bearish factors from the day's news.

**6. WATCHLIST FOR TOMORROW**
List 3–5 specific items to monitor: upcoming data releases, earnings, policy decisions, or technical levels implied by today's news.

**FORMATTING RULES**
- Use box headers and section dividers for scannable layout.
- Keep each bullet to one line where possible.
- Use tickers in caps (NVDA, AAPL) when companies are clearly identified.
- If a metric is mentioned (e.g., CPI, EPS), always include the number and vs. expectation if available.
- Do not add information beyond what is in the provided news — note gaps rather than filling them.
- Flag any conflicting signals explicitly (e.g., "bullish earnings vs. bearish macro").
```

## Notes

- For best results, include 8–20 news items covering a range of topics (macro, equities, commodities, rates).
- The skill analyzes only what is provided — it does not have access to live market data. Prices and levels are extracted from the news text itself.
- For sector-specific deep dives, pair with: `skills/data-and-research/earnings-analysis/earnings-call-analyzer.md`
- For macro indicator context: `skills/data-and-research/economic-indicators/`
- Related skills: `skills/news-and-reporting/market-analysis/`, `skills/investing/portfolio-analysis/`
