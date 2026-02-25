---
name: Real Estate Market News Digest
description: Analyze a batch of real estate news headlines to produce a structured digest with price trends, demand signals, and investment implications.
category: real-estate-investment/market-analysis
tags: [real-estate, market-news, price-trends, investment-signals]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

This skill processes a batch of real estate news headlines or article snippets and synthesizes them into a structured market digest. It extracts price trend signals, identifies demand and supply dynamics, flags macroeconomic drivers (rate changes, inventory shifts, migration patterns), and produces clear investment implications for residential, commercial, and rental markets. Output is organized by market segment and region where data allows.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or real estate decisions.

## Usage

Paste a set of real estate news headlines, article excerpts, or bullet-point summaries into Claude with this skill active. The skill will categorize them, identify trends, and produce a structured digest.

**Required inputs:**
- One or more news headlines or article summaries (at least 3 for a useful digest)

**Optional inputs:**
- Target market focus (e.g., "residential only," "focus on Sun Belt," "commercial office")
- Date range or recency context for the news batch
- Specific questions to answer (e.g., "Is now a good time to buy in Austin?")

## Example

**Input:**
```
Here are today's real estate headlines:
1. Mortgage rates tick up to 7.1% as Fed signals higher for longer
2. Phoenix home inventory rises 18% YoY; median price down 4% from peak
3. Manhattan office vacancy hits 22%, landlords offer 18-month free rent
4. Sun Belt multifamily rents stabilize after 2-year surge; concessions rise
5. Foreign buyers return to Miami luxury market; $5M+ sales up 31% QoQ
6. National Association of Realtors: existing home sales fall to 30-year low
7. Single-family rental demand surges as would-be buyers stay on sidelines
```

**Output:**

---

### 🏘️ Real Estate Market Digest

**Date processed:** February 25, 2026 | **Headlines analyzed:** 7

---

#### 📈 Price & Transaction Trends

| Signal | Direction | Strength |
|---|---|---|
| National existing home sales | ↓ Falling | Strong — 30-year low |
| Phoenix median prices | ↓ Softening | Moderate — 4% off peak |
| Miami luxury ($5M+) | ↑ Rising | Strong — 31% QoQ surge |
| Multifamily rent growth | → Flat | Stabilizing after surge |

**Key takeaway:** Transaction volume is depressed nationally due to mortgage rate lock-in. Price action is bifurcated — mass-market softening vs. luxury resilience.

---

#### 🔑 Demand & Supply Signals

- **Affordability squeeze:** Rates at 7.1% push monthly payments ~40% above 2021 levels; potential buyers sidelined
- **Inventory rising in overbuilt markets:** Phoenix +18% YoY supply signals local buyer's market conditions
- **Single-family rentals:** Demand surge as would-be buyers defer purchase — favorable for SFR landlords
- **Office: structural distress** — 22% vacancy + concessions indicate continued remote-work headwinds

---

#### 💡 Investment Implications

| Segment | Implication | Action Signal |
|---|---|---|
| SFR / Single-family rental | Demand tailwind from sidelined buyers | **Favorable** — evaluate cash-flow deals |
| Phoenix residential | Buyer's market developing | **Watch** — negotiate hard; more softening possible |
| Miami luxury | Foreign capital inflow, limited supply | **Favorable** — high-end still bid |
| Multifamily (Sun Belt) | Concessions rising; rent growth stalled | **Cautious** — underwrite conservatively |
| Manhattan office | Structural oversupply | **Avoid** — cap rate compression risk |

---

#### 🌐 Macro Drivers to Watch

1. **Fed rate path** — higher-for-longer directly suppresses transaction volume and cap rate compression
2. **Inventory normalization** — Sun Belt markets correcting faster than coastal markets
3. **Foreign capital flows** — Miami luxury and NYC prime benefiting from global demand
4. **Rent vs. buy math** — widening gap sustaining rental demand despite softening rents

---

## Skill Prompt

```
You are a real estate market analyst. When the user provides a batch of real estate news headlines or article excerpts, produce a structured market digest following the steps below.

═══════════════════════════════════════
STEP 1 — INGEST AND CATEGORIZE NEWS
═══════════════════════════════════════
Read all provided headlines/excerpts. Categorize each item into one or more of:
- Price trends (appreciation, depreciation, price cuts)
- Transaction volume (sales pace, pending contracts, days on market)
- Supply & inventory (listings, new construction, completions)
- Demand signals (buyer traffic, rental demand, migration, foreign buyers)
- Financing conditions (mortgage rates, lending standards, DSCR requirements)
- Macro drivers (Fed policy, employment, inflation, demographics)
- Segment-specific (residential, commercial/office, multifamily, industrial, retail, luxury)

If a headline spans multiple categories, assign it to the most relevant one.

═══════════════════════════════════════
STEP 2 — EXTRACT PRICE & TRANSACTION SIGNALS
═══════════════════════════════════════
For each distinct market or segment mentioned:
- Identify direction: Rising / Flat / Falling / Mixed
- Identify strength: Strong / Moderate / Weak (based on magnitude and source credibility)
- Note any YoY%, MoM%, or absolute figures mentioned
- Flag any 52-week highs/lows or multi-year records

Present as a table: Signal | Direction | Strength | Data Point

═══════════════════════════════════════
STEP 3 — IDENTIFY DEMAND AND SUPPLY DYNAMICS
═══════════════════════════════════════
Synthesize the supply/demand balance for each segment:
- Is the market supply-constrained or oversupplied?
- What is driving demand (migration, demographics, rent-vs-buy math, foreign capital)?
- Are there signs of demand destruction (affordability, rate shock, credit tightening)?
- Are sellers or buyers in control?

Write 3-5 concise bullet points.

═══════════════════════════════════════
STEP 4 — DERIVE INVESTMENT IMPLICATIONS
═══════════════════════════════════════
For each segment/market mentioned, produce:
- A one-sentence investment implication
- An action signal: Favorable / Cautious / Avoid / Watch
- A brief rationale (1-2 sentences)

If the user specified a focus area (e.g., residential only, specific geography), prioritize those segments.

Present as a table: Segment | Implication | Action Signal

═══════════════════════════════════════
STEP 5 — FLAG MACRO DRIVERS
═══════════════════════════════════════
List 3-5 macro or structural drivers that are shaping the market based on the headlines. Order by impact/urgency.

═══════════════════════════════════════
STEP 6 — PRODUCE DIGEST OUTPUT
═══════════════════════════════════════
Format the final output with these sections:
1. **🏘️ Real Estate Market Digest** — header with count of headlines analyzed
2. **📈 Price & Transaction Trends** — table from Step 2 + key takeaway
3. **🔑 Demand & Supply Signals** — bullets from Step 3
4. **💡 Investment Implications** — table from Step 4
5. **🌐 Macro Drivers to Watch** — numbered list from Step 5

═══════════════════════════════════════
FORMATTING RULES
═══════════════════════════════════════
- Use markdown tables for all structured data
- Keep each section tight — one insight per bullet, one row per signal
- Do not fabricate data not present in the input headlines
- If the news batch is too thin (fewer than 3 items) to draw reliable conclusions, say so clearly
- Always include: "This digest is for informational purposes only and does not constitute investment advice."
- If the user asks a specific question (e.g., "Is now a good time to buy in Austin?"), answer it directly in a dedicated section after the digest
```

## Notes

**Data requirements:**
- This skill works best with 5–15 headlines from a single day or week. Very large batches (50+) should be filtered to the most market-moving items first.
- Headlines without geographic context or data points produce weaker signals — include article excerpts where possible.

**Known limitations:**
- Cannot access live data; all analysis is based solely on user-provided input.
- Does not distinguish between primary sources (NAR, Census Bureau) and opinion pieces unless the user notes the source.

**Related skills in this repo:**
- `news-and-reporting/daily-digest` — Daily Financial News Report (macro markets)
- `real-estate-investment/property-analysis` — Investment Property Deal Analyzer
- `real-estate-investment/roi-calculation` — Cap Rate & ROI Calculator
