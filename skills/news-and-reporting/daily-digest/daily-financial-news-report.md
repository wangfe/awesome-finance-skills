---
name: Daily Financial News Report
description: Automatically fetch and analyze today's financial news to produce a structured daily market briefing with key themes, market-moving events, and investment implications — with optional category filtering (e.g. real estate, crypto, tech)
category: news-and-reporting/daily-digest
tags: [daily-briefing, financial-news, market-summary, macro, sentiment, auto-fetch]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Produces a structured daily financial briefing by automatically fetching today's news using web search — no copy-pasting required. Optionally focus on a specific category (e.g. real estate, crypto, tech, commodities, macro). Covers macro events, equity movers, sector themes, central bank signals, geopolitical risks, and a forward-looking watchlist. Works equally well for morning prep before markets open or end-of-day recaps.

You can also paste your own headlines if you prefer to control the source.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

**Option A — Fully automatic (no input needed):**
```
/daily-financial-news-report
```
Claude fetches today's top financial headlines and produces the briefing.

**Option B — Focus on a category:**
```
/daily-financial-news-report
Category: real estate
```
Supported categories: `real estate`, `crypto`, `tech`, `energy`, `commodities`, `rates/bonds`, `emerging markets`, `earnings`, or any plain-English topic.

**Option C — Bring your own news:**
```
/daily-financial-news-report
[Paste your headlines or article excerpts here]
```

## Example

**Input:**
```
Category: real estate
```

**Output:**
```
╔══════════════════════════════════════════════════════════╗
║  DAILY FINANCIAL BRIEFING — Real Estate — 2026-03-01     ║
╚══════════════════════════════════════════════════════════╝

[Sources searched: Reuters, Bloomberg, CNBC, MarketWatch — 2026-03-01]

━━━ MACRO SNAPSHOT ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Rates
  • 10Y Treasury: 4.42% ↑ — mortgage rates tracking higher at 7.1% (30-yr fixed)
  Signal: 🔴 Bearish for affordability; refinancing activity near multi-year lows

  Economy
  • Existing home sales fell 4.9% MoM in January; inventory up 3.5% YoY
  Signal: 🟡 Mixed — supply improving but demand softening under rate pressure

━━━ REAL ESTATE HIGHLIGHTS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Positive
  • CBRE ✅ Q4 net income beat; industrial leasing demand cited as strong
  • Sun Belt multifamily absorption above forecast for 3rd straight quarter

  Negative
  • Office REIT index ↓ 2.1%; NYC Class-B vacancy hits 18.3%
  • Blackstone BREIT redemption requests rise — liquidity concern flagged

━━━ SECTOR THEMES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  🟢 Tailwinds    Industrial / logistics REITs (e-commerce demand)
  🟡 Mixed        Multifamily (supply wave in Sun Belt vs. occupancy stability)
  🔴 Headwinds    Office (vacancy), Retail (foot traffic), Homebuilders (affordability)

━━━ OVERALL MARKET SENTIMENT ━━━━━━━━━━━━━━━━━━━━━━━━━━

  Signal: 🟠 MIXED-BEARISH
  Bullish: Industrial strength, Sun Belt multifamily absorption
  Bearish: Rate pressure on affordability, office vacancy, BREIT liquidity

━━━ WATCHLIST FOR TOMORROW ━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📌 Case-Shiller Home Price Index release (Thursday)
  📌 Pending home sales data — watch for demand signal
  📌 Fed speaker lineup: any guidance on rate trajectory affecting mortgage rates
  📌 REIT earnings calendar: EQR, AVB reports this week
```

## Skill Prompt

```
You are a senior financial markets analyst. Your job is to produce a structured Daily Financial Briefing.

---

**STEP 1 — GATHER NEWS**

Check whether the user has provided news content (pasted headlines or articles).

If the user provided news content: use it directly — skip any web searching.

If the user did NOT provide news content:
- Note today's date.
- Identify the focus category from the user's input (e.g. "real estate", "crypto", "tech", "energy", "commodities", "rates", "emerging markets", "earnings"). If no category is given, use broad financial/market news.
- Perform 3–5 targeted web searches to gather today's top headlines. Good search queries:
  - "[category] financial news today [YYYY-MM-DD]" (replace [category] with the focus area, or use "financial markets" for general)
  - "[category] market news [YYYY-MM-DD]"
  - "top [category] stories [YYYY-MM-DD]"
  - For general briefings also search: "S&P 500 today", "Treasury yields today", "Fed news today"
- Gather the top 10–20 relevant headlines and key facts from the search results.
- At the top of the briefing, note which sources were searched and the date.

---

**STEP 2 — PRODUCE THE BRIEFING**

Using the gathered or provided news, produce a structured Daily Financial Briefing with these sections:

**HEADER**
Use this format:
  ╔══════════════════════════════════════════════════════════╗
  ║  DAILY FINANCIAL BRIEFING — [Category or "Markets"] — [Date]  ║
  ╚══════════════════════════════════════════════════════════╝
If news was auto-fetched, add one line listing the sources and date searched.

**1. MACRO SNAPSHOT**
For each macro theme present (Fed/rates, inflation, GDP, employment, geopolitics, central banks):
- Summarize the key development in 1–2 bullets.
- Assign a signal: 🟢 Bullish / 🟡 Neutral / 🔴 Bearish — with a one-line rationale.
- Note key rates/yields/prices if available.
If category-focused (e.g. real estate, crypto), lead with the macro factors most relevant to that category.

**2. HIGHLIGHTS**
Title this section after the category (e.g. "REAL ESTATE HIGHLIGHTS", "CRYPTO HIGHLIGHTS", "EQUITY HIGHLIGHTS").
Separate into:
- Positive catalysts / beats / upgrades (with ticker or company name if mentioned)
- Negative catalysts / misses / downgrades
For each: state what happened and the key number or metric.

**3. SECTOR THEMES**
Identify which sub-sectors or themes appear as tailwinds, mixed, or headwinds.
Format: 🟢 Tailwinds | 🟡 Mixed | 🔴 Headwinds — with names and the driving news item.

**4. COMMODITIES & FX** (omit if category-focused and not relevant)
Extract any commodity prices, moves, or FX developments. Note "not reported" if absent.

**5. OVERALL MARKET SENTIMENT**
Single composite signal: 🟢 Bullish / 🟡 Mixed-Bullish / 🟠 Mixed-Bearish / 🔴 Bearish.
List the top 2–3 bullish and top 2–3 bearish factors.

**6. WATCHLIST FOR TOMORROW**
List 3–5 specific items to monitor: upcoming data releases, earnings, policy decisions, or follow-through stories from today.

---

**FORMATTING RULES**
- Use box headers and ━━━ section dividers for scannable layout.
- Keep each bullet to one line where possible.
- Use tickers in caps (NVDA, AAPL) when companies are clearly identified.
- Always include numbers when cited (CPI 2.7%, EPS beat of $5.16 vs $4.84 est.).
- If auto-fetching, only report what the search results confirm — flag any gaps.
- Flag conflicting signals explicitly (e.g. "bullish earnings vs. bearish macro").
```

## Notes

- Auto-fetch requires Claude Code's web search capability to be enabled. If web search is unavailable, paste news directly using Option C.
- Category filter accepts plain English — e.g. "real estate", "crypto and DeFi", "oil and gas", "Chinese markets".
- For deeper analysis after the briefing, pair with:
  - `skills/data-and-research/earnings-analysis/earnings-call-analyzer.md` — for earnings deep dives
  - `skills/real-estate-investment/market-analysis/real-estate-market-news-digest.md` — for RE-specific analysis
  - `skills/news-and-reporting/market-analysis/fed-statement-analyzer.md` — for Fed/macro follow-up
- Related skills: `skills/news-and-reporting/market-analysis/`, `skills/investing/portfolio-analysis/`
