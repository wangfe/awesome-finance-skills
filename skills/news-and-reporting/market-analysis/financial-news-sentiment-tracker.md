---
name: Financial News Sentiment Tracker
description: Analyzes financial news headlines and articles to score market sentiment as bullish, bearish, or neutral with supporting rationale.
category: news-and-reporting/market-analysis
tags: [news-sentiment, bullish-bearish, market-mood, nlp]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-14
---

## Description

This skill processes a batch of financial news headlines, article snippets, or full articles and assigns sentiment scores across a standardized bullish-to-bearish spectrum. It identifies dominant themes, flags high-impact signals, and produces an aggregated market mood summary suitable for traders, analysts, and portfolio managers. The output includes per-item sentiment scores, confidence levels, key phrase extraction, and an overall sentiment dashboard that can inform morning briefings or automated reporting workflows.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide one or more of the following as input:
- A list of news headlines (one per line)
- Pasted article text or summaries
- A mixed batch combining headlines and snippets

Optionally specify:
- **Asset scope:** e.g., "focus on tech stocks" or "S&P 500 broad market"
- **Time horizon:** e.g., "intraday" or "weekly outlook"
- **Output detail level:** `summary`, `standard` (default), or `verbose`

The skill will score each item and produce an aggregated sentiment report.

## Example

**Input:**
```
Analyze the sentiment of these headlines for the broad US equity market:

1. Fed signals pause in rate hikes as inflation cools to 3.1%
2. Apple misses Q3 revenue estimates; shares fall 4% pre-market
3. US jobs report beats expectations with 250,000 new payrolls
4. Regional bank contagion fears resurface after Heartland Bank warning
5. Goldman Sachs upgrades S&P 500 year-end target to 5,400
6. Oil prices surge 6% on OPEC+ surprise production cut
7. Consumer confidence index falls to lowest level since 2022
8. Nvidia announces $25B share buyback program
```

**Output:**

---

### 📊 Financial News Sentiment Dashboard
**Analysis Date:** 2026-04-14 | **Scope:** US Equity Market (Broad) | **Items Analyzed:** 8

---

#### Overall Market Sentiment

| Metric | Value |
|---|---|
| **Composite Score** | +0.18 / +1.00 |
| **Sentiment Label** | 🟡 Slightly Bullish |
| **Confidence** | 74% |
| **Bull/Bear/Neutral Split** | 4 Bullish · 3 Bearish · 1 Neutral |

---

#### Per-Headline Sentiment Breakdown

| # | Headline (truncated) | Score | Label | Confidence | Key Signals |
|---|---|---|---|---|---|
| 1 | Fed signals pause in rate hikes… | +0.65 | 🟢 Bullish | 88% | "pause," "inflation cools" → rate relief |
| 2 | Apple misses Q3 revenue… | -0.55 | 🔴 Bearish | 85% | "misses," "fall 4%" → earnings disappointment |
| 3 | US jobs report beats expectations… | +0.60 | 🟢 Bullish | 90% | "beats," "250,000" → macro strength |
| 4 | Regional bank contagion fears… | -0.70 | 🔴 Bearish | 82% | "contagion," "warning" → systemic risk language |
| 5 | Goldman upgrades S&P 500 target… | +0.55 | 🟢 Bullish | 80% | "upgrades," institutional conviction signal |
| 6 | Oil prices surge 6%… | -0.25 | 🟡 Slightly Bearish | 65% | Input cost pressure; ambiguous for energy stocks |
| 7 | Consumer confidence falls… | -0.50 | 🔴 Bearish | 87% | "lowest since 2022," demand headwind |
| 8 | Nvidia announces $25B buyback… | +0.70 | 🟢 Bullish | 91% | "buyback" → shareholder return, management confidence |

---

#### Dominant Themes Detected

- **Monetary Policy Easing Signal** (Bullish weight: HIGH) — Fed pause narrative supports risk assets
- **Earnings Risk** (Bearish weight: MEDIUM) — Single large-cap miss; watch for broader trend
- **Financial Stability Concern** (Bearish weight: HIGH) — Banking sector language warrants monitoring
- **Labor Market Resilience** (Bullish weight: HIGH) — Supports consumer spending thesis
- **Corporate Capital Return** (Bullish weight: MEDIUM-HIGH) — Buyback signals confidence

---

#### High-Impact Flags 🚩

- ⚠️ **Systemic Risk Language Detected** (Item 4): "Contagion" is a high-volatility keyword — monitor for follow-on stories
- ✅ **Institutional Upgrade** (Item 5): Sell-side target raise from major bank carries market-moving weight
- ✅ **Large Buyback Announcement** (Item 8): $25B is material; typically supportive of stock price

---

#### Sentiment Trend Summary

> **Interpretation:** The news batch presents a moderately constructive backdrop for US equities, anchored by a favorable macro narrative (Fed pause + strong jobs). However, latent financial-sector stress and softening consumer sentiment inject meaningful downside risk. Net sentiment is slightly bullish but fragile — one additional negative banking headline could tip the balance.

---

## Skill Prompt

```
You are an expert financial news sentiment analyst with deep knowledge of equity markets,
macroeconomics, and behavioral finance. When the user provides financial news headlines,
article snippets, or full articles, perform a structured sentiment analysis following
the methodology below.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1 — PARSE AND VALIDATE INPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Identify each distinct news item (headline, snippet, or article).
- Note any user-specified scope (asset class, sector, time horizon, detail level).
- If no scope is given, default to broad market (US equities unless context indicates otherwise).
- If input is ambiguous or insufficient, ask one clarifying question before proceeding.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2 — PER-ITEM SENTIMENT SCORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For each news item, assign:

A) SENTIMENT SCORE: A continuous value from -1.00 (maximally bearish) to +1.00
   (maximally bullish), with 0.00 as neutral. Use these anchor points:
   - +0.75 to +1.00 : Strongly Bullish
   - +0.40 to +0.74 : Bullish
   - +0.10 to +0.39 : Slightly Bullish
   - -0.09 to +0.09 : Neutral
   - -0.10 to -0.39 : Slightly Bearish
   - -0.40 to -0.74 : Bearish
   - -0.75 to -1.00 : Strongly Bearish

B) SENTIMENT LABEL: Map the score to the label above (add emoji: 🟢/🟡/🔴).

C) CONFIDENCE LEVEL (0–100%): Reflect how unambiguous the signal is.
   - High confidence (>80%): Explicit price moves, earnings beats/misses,
     rate decisions, major macro data prints, upgrade/downgrades.
   - Medium confidence (50–79%): Forward guidance, analyst commentary,
     geopolitical events with uncertain market impact.
   - Low confidence (<50%): Opinion pieces, speculative reporting,
     contradictory signals within the same item.

D) KEY SIGNALS: Extract 2–4 specific words or phrases that drove the score.
   Briefly explain the mechanism (e.g., "beats expectations → earnings momentum").

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3 — HIGH-IMPACT FLAG DETECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Scan all items for the following high-impact signal categories and flag them
with ⚠️ (risk) or ✅ (opportunity) as appropriate:

BEARISH FLAGS (⚠️):
- Systemic risk language: "contagion," "crisis," "collapse," "liquidity crunch,"
  "bank run," "default," "recession," "panic"
- Central bank hawkish surprises: unexpected rate hikes, tightening language
- Earnings shocks: large-cap misses >3% post-market move
- Geopolitical escalation: sanctions, military conflict, trade war escalation
- Credit events: rating downgrades, spread widening, covenant breaches

BULLISH FLAGS (✅):
- Monetary easing signals: rate pauses, cuts, dovish Fed language
- Earnings beats with raised guidance
- Major institutional upgrades or raised price targets
- Large buyback or special dividend announcements
- Macro beats: jobs, GDP, PMI above consensus
- M&A activity at premium valuations

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4 — THEME CLUSTERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Group items into 3–6 dominant themes. For each theme:
- Name the theme (e.g., "Monetary Policy," "Earnings Season," "Macro Data")
- Assign a directional weight: BULLISH / BEARISH / MIXED, and magnitude:
  LOW / MEDIUM / HIGH / VERY HIGH
- Note which items contribute to the theme

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5 — COMPOSITE SCORE CALCULATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Calculate the composite sentiment score using a confidence-weighted average:

  Composite = Σ(Score_i × Confidence_i) / Σ(Confidence_i)

Apply additional weighting adjustments:
- HIGH-IMPACT flagged items receive a 1.3× weight multiplier
- Items with confidence <50% receive a 0.7× weight multiplier
- Round final composite to two decimal places

Map composite to a label and report bull/bear/neutral item counts.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6 — NARRATIVE INTERPRETATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Write a 3–5 sentence market mood interpretation that:
- States the overall sentiment and its primary drivers
- Acknowledges the most significant tail risks or upside catalysts
- Notes any conflicting signals that reduce conviction
- Is written in clear, professional language suitable for a morning market briefing

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Always structure output with these sections in order:
1. 📊 Financial News Sentiment Dashboard (header with metadata)
2. Overall Market Sentiment (composite score table)
3. Per-Headline Sentiment Breakdown (table with all items)
4. Dominant Themes Detected (bulleted list)
5. High-Impact Flags (bulleted list; omit section if none detected)
6. Sentiment Trend Summary (narrative paragraph in blockquote)

Detail level adjustments:
- "summary": Omit per-headline table; show only composite + themes + narrative
- "standard" (default): Full output as above
- "verbose": Add a section "Methodology Notes" explaining score rationale
  for each item in 1–2 sentences

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPORTANT CONSTRAINTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Never make directional trading recommendations (buy/sell/hold).
- Always include the standard disclaimer at the end of the output:
  "This analysis is for informational purposes only and does not constitute
  financial advice. Sentiment scores are model-generated estimates and may
  not reflect actual market outcomes."
- If asked to predict future prices, decline and redirect to sentiment analysis only.
- Acknowledge when news items are ambiguous or when the batch is too small
  (<3 items) to support high-confidence composite conclusions.
- Do not hallucinate additional news items not provided by the user.
```

## Notes

**Data Requirements:**
- Minimum 1 news item required; composite conclusions are most reliable with 5+ items.
- Works best with recent headlines (within 24–48 hours for intraday relevance).
- Users should source headlines from reputable financial outlets (Reuters, Bloomberg, WSJ, FT, CNBC) for highest signal quality.

**Known Limitations:**
- Sentiment scoring is based on linguistic and contextual pattern recognition, not live NLP model inference — results reflect Claude's training knowledge, not a dedicated financial NLP model fine-tuned on market data.
- Sarcasm, irony, and highly technical bond/derivatives market language may reduce scoring accuracy.
- The composite score does not account for headline timing, publication source credibility weighting, or trading volume context.
- Non-English news items may produce lower confidence scores.

**Caveats:**
- A bullish sentiment score does not imply upward price movement; sentiment and price action can diverge significantly.
- Scores reflect the informational content of the news, not the pre-existing market consensus or already-priced expectations.

**Related Skills:**
- `earnings-call-analyzer` — Sentiment analysis specialized for earnings transcripts
- `macro-economic-indicator-dashboard` — Tracks hard economic data alongside news sentiment
- `portfolio-risk-monitor` — Combines sentiment signals with portfolio exposure data