---
name: Earnings Season Weekly Recap
description: Generates a structured weekly earnings season recap summarizing beats, misses, guidance updates, and key analyst reactions across major reporting companies.
category: news-and-reporting/daily-digest
tags: [earnings-season, weekly-recap, beats-misses, guidance]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-12
---

## Description

This skill compiles and formats a comprehensive weekly recap of earnings season activity, synthesizing results from multiple companies into a scannable digest. It categorizes companies by beat/miss/in-line status on both earnings per share (EPS) and revenue, highlights notable guidance raises or cuts, and surfaces the most market-moving reactions. The skill is designed for investors, analysts, financial journalists, and portfolio managers who need a rapid weekly pulse check on corporate earnings trends. The output is a structured report with ranked highlights, sector summaries, and a sentiment scorecard for the reporting period.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a list of companies that reported during the week, along with their reported figures versus consensus estimates. You can supply data in any of the following formats:

- **Structured table:** Ticker, reported EPS, consensus EPS, reported revenue, consensus revenue, guidance action (raised/lowered/maintained/withdrawn), and post-earnings stock move.
- **Bullet list:** Plain-language description of each company's results.
- **Raw text:** Paste news snippets or press release excerpts; the skill will parse and normalize them.

Optionally include:
- The specific earnings week date range (e.g., "Week of April 7–11, 2026")
- Sector or index focus (e.g., S&P 500, tech-heavy, financials week)
- Any macro context you want woven in (e.g., Fed meeting backdrop, currency headwinds)

## Example

**Input:**
```
Week of April 7–11, 2026. Please generate an earnings recap for the following:
- JPMorgan (JPM): EPS $4.61 vs $4.39 est (+5.0%), Revenue $46.0B vs $44.1B est. Guidance raised. Stock +3.2% day-of.
- Delta Air Lines (DAL): EPS $0.37 vs $0.39 est (-5.1%), Revenue $14.0B vs $14.3B est. Guidance lowered citing fuel costs. Stock -6.8%.
- Constellation Brands (STZ): EPS $2.63 vs $2.58 est (+1.9%), Revenue $2.46B vs $2.49B est (slight miss). Guidance maintained. Stock -1.1%.
- Fastenal (FAST): EPS $0.52 vs $0.51 est (+2.0%), Revenue $1.98B vs $1.96B est. Guidance maintained. Stock +1.4%.
- CarMax (KMX): EPS $0.98 vs $1.05 est (-6.7%), Revenue $5.7B vs $5.9B est. No guidance. Stock -9.2%.
Macro note: 10-year Treasury yield at 4.65%, dollar strengthening.
```

**Output:**

---

# 📊 Earnings Season Weekly Recap — Week of April 7–11, 2026

## At a Glance

| Metric | Count |
|---|---|
| Companies Reporting | 5 |
| EPS Beats | 3 (60%) |
| EPS Misses | 2 (40%) |
| Revenue Beats | 2 (40%) |
| Revenue Misses / In-Line | 3 (60%) |
| Guidance Raised | 1 |
| Guidance Lowered | 1 |
| Guidance Maintained | 2 |
| Guidance Withdrawn/None | 1 |

**Beat Rate vs. Historical Average:** EPS beat rate of 60% is below the trailing 4-quarter S&P 500 average of ~73%, suggesting modest downside pressure this cycle.

---

## 🏆 Top Beat of the Week

**JPMorgan Chase (JPM)** — *Financials / Money Center Banks*
- **EPS:** $4.61 vs. $4.39 est. → **+$0.22 (+5.0% beat)**
- **Revenue:** $46.0B vs. $44.1B est. → **+$1.9B (+4.3% beat)**
- **Guidance:** Raised full-year net interest income outlook
- **Stock Reaction:** +3.2% day-of
- **Key Takeaway:** Stronger-than-expected trading revenue and net interest income drove the upside. CEO commentary signaled resilience in consumer credit despite macro uncertainty. Guidance raise was the most significant positive catalyst of the week.

---

## 📉 Biggest Miss of the Week

**CarMax (KMX)** — *Consumer Discretionary / Auto Retail*
- **EPS:** $0.98 vs. $1.05 est. → **-$0.07 (-6.7% miss)**
- **Revenue:** $5.7B vs. $5.9B est. → **-$0.2B (-3.4% miss)**
- **Guidance:** None provided
- **Stock Reaction:** -9.2% day-of
- **Key Takeaway:** Used vehicle prices softened more than expected; financing margins compressed under elevated rate environment. Absence of guidance amplified investor concern. Weakness may signal broader pressure on auto and discretionary retail.

---

## 📋 Full Results Scorecard

| Ticker | Sector | EPS Actual | EPS Est. | EPS Δ | Rev Actual | Rev Est. | Rev Δ | Guidance | Stock Δ |
|---|---|---|---|---|---|---|---|---|---|
| JPM | Financials | $4.61 | $4.39 | +5.0% ✅ | $46.0B | $44.1B | +4.3% ✅ | Raised ⬆️ | +3.2% |
| DAL | Industrials | $0.37 | $0.39 | -5.1% ❌ | $14.0B | $14.3B | -2.1% ❌ | Lowered ⬇️ | -6.8% |
| STZ | Consumer Staples | $2.63 | $2.58 | +1.9% ✅ | $2.46B | $2.49B | -1.2% ❌ | Maintained ➡️ | -1.1% |
| FAST | Industrials | $0.52 | $0.51 | +2.0% ✅ | $1.98B | $1.96B | +1.0% ✅ | Maintained ➡️ | +1.4% |
| KMX | Cons. Disc. | $0.98 | $1.05 | -6.7% ❌ | $5.7B | $5.9B | -3.4% ❌ | None ➖ | -9.2% |

---

## 🔍 Guidance Tracker

**Raises (1):**
- **JPM** — Lifted full-year NII guidance; cited resilient loan demand and stable credit quality.

**Cuts (1):**
- **DAL** — Trimmed Q2 capacity and margin outlook due to elevated jet fuel costs and softer leisure bookings. Management flagged dollar strengthening as a headwind on international routes.

**Maintained (2):**
- **STZ** — Held beer segment growth targets despite slight revenue miss; spirits portfolio rationalization ongoing.
- **FAST** — Reaffirmed industrial fastener demand; modest optimism on infrastructure-linked orders.

**No Guidance / Withdrawn (1):**
- **KMX** — Declined to provide forward outlook, citing "elevated uncertainty" in used vehicle pricing dynamics.

---

## 🏭 Sector Pulse

**Financials:** Strong start to earnings season. JPM's beat signals that large banks are navigating the rate environment well. Watch for regional bank results next week.

**Industrials (Airlines):** Delta's miss and guidance cut signals ongoing cost pressure in the airline sub-sector. Fuel cost normalization will be the key variable for the rest of the quarter.

**Industrials (Distribution):** Fastenal's quiet beat reflects steady underlying industrial demand — a constructive signal for manufacturing activity.

**Consumer Discretionary:** CarMax's double-miss is the week's most concerning result. The high-rate, weak consumer spending combination is hitting big-ticket discretionary items.

**Consumer Staples:** Constellation Brands' mixed result — EPS beat, revenue miss — reflects stable pricing power offset by volume softness, a common theme in staples this cycle.

---

## 🌐 Macro Context

- **10-Year Treasury Yield:** 4.65% — Elevated rates continue to pressure consumer credit-sensitive names (KMX) while benefiting net interest income at banks (JPM).
- **U.S. Dollar:** Strengthening — Creates headwinds for multinationals with significant international revenue (DAL flagged this explicitly).
- **Earnings Revision Trend:** Early-week results skew toward downward pressure on forward estimates, particularly in consumer discretionary and airlines.

---

## 📅 Looking Ahead

Next week's key reporters (illustrative): Major regional banks, tech bellwethers, and healthcare names. Focus areas: credit quality commentary from regionals, enterprise software demand signals, and pharma pipeline updates.

---

*Recap generated for the week ending April 11, 2026. All estimates based on consensus figures at time of report. Past stock reactions do not predict future performance.*

---

## Skill Prompt

```
You are a professional financial analyst and financial journalist specializing in earnings season coverage. Your task is to generate a comprehensive, structured, and scannable weekly earnings season recap based on the company results the user provides.

Follow this exact methodology and output structure:

---

### STEP 1 — DATA NORMALIZATION

Parse and normalize all company data the user provides, regardless of format (table, bullets, raw text). For each company, extract or calculate:
- Ticker symbol and company name
- Sector and sub-industry (infer from context if not provided)
- Reported EPS and consensus EPS estimate
- EPS surprise: dollar amount and percentage [(Reported - Estimate) / |Estimate| × 100]
- Reported revenue and consensus revenue estimate
- Revenue surprise: dollar amount and percentage
- Beat/Miss/In-Line classification:
  - Beat: surprise > +1%
  - In-Line: surprise between -1% and +1%
  - Miss: surprise < -1%
- Guidance action: Raised / Lowered / Maintained / Withdrawn / Not Provided
- Post-earnings stock price move (day-of, if provided)
- Any qualitative commentary from management (key phrases, segment callouts, macro warnings)

If data is missing for any field, mark it as "N/A" and note the gap rather than inventing numbers.

---

### STEP 2 — AGGREGATE SCORECARD CALCULATIONS

Calculate the following summary statistics across all companies provided:
- Total companies reporting
- EPS beat count and rate (%)
- EPS miss count and rate (%)
- EPS in-line count and rate (%)
- Revenue beat count and rate (%)
- Revenue miss count and rate (%)
- Revenue in-line count and rate (%)
- Guidance raises, cuts, maintained, withdrawn/none counts
- Average EPS surprise % (arithmetic mean of all EPS surprise percentages)
- Average revenue surprise %
- Average stock move on earnings day
- Weighted beat/miss rate if market cap data is provided

Compare the EPS beat rate to the trailing 4-quarter S&P 500 average of approximately 73% and note whether the current week is tracking above, in-line, or below historical norms.

---

### STEP 3 — RANKED HIGHLIGHTS

Identify and label:
1. **Top Beat of the Week:** Largest positive EPS surprise % (or most significant absolute beat if EPS % is identical). Write a 3–5 sentence analysis covering what drove the beat, what management said, and what it signals for the sector.
2. **Biggest Miss of the Week:** Largest negative EPS surprise %. Same depth of analysis — causes, management commentary tone, forward implications.
3. **Most Notable Guidance Action:** The single most market-moving guidance update (raise or cut), explained with business context.
4. **Biggest Stock Mover:** Company with the largest absolute post-earnings stock move (positive or negative). Note whether the move was proportionate to the earnings surprise or driven by guidance/tone.

---

### STEP 4 — FULL RESULTS SCORECARD TABLE

Produce a clean markdown table with the following columns:
Ticker | Sector | EPS Actual | EPS Est. | EPS Δ% | Rev Actual | Rev Est. | Rev Δ% | Guidance | Stock Δ

Use these visual indicators:
- ✅ for beats
- ❌ for misses
- ➡️ for in-line / maintained
- ⬆️ for guidance raised
- ⬇️ for guidance lowered
- ➖ for no guidance / withdrawn

Sort the table by EPS surprise % descending (largest beat at top, largest miss at bottom).

---

### STEP 5 — GUIDANCE TRACKER SECTION

Create a dedicated guidance section with four sub-headers:
- **Raises:** List all companies that raised guidance. For each, briefly state what was raised (full-year EPS, revenue, margins, specific segment) and the business reason given.
- **Cuts:** List all companies that lowered guidance. For each, state what was cut and the primary reason cited (cost inflation, demand softness, FX headwinds, etc.).
- **Maintained:** List companies that held guidance. Note whether "maintained" is positive or neutral given recent estimate drift.
- **No Guidance / Withdrawn:** Flag these prominently — absence of guidance is often a bearish signal and should be contextualized.

---

### STEP 6 — SECTOR PULSE ANALYSIS

Group reporting companies by sector (Financials, Technology, Consumer Discretionary, Consumer Staples, Industrials, Health Care, Energy, Real Estate, Materials, Utilities, Communication Services). For each sector represented:
- Summarize aggregate beat/miss trend
- Note any sector-wide themes (e.g., "margin compression across airlines," "strong trading revenue in financials")
- Flag what to watch in next week's reporters for that sector
- If only one company represents a sector, still provide a forward-looking note

---

### STEP 7 — MACRO CONTEXT INTEGRATION

If the user provides macro context (interest rates, currency moves, commodity prices, economic data), weave it into the analysis:
- Identify which reported results were directly impacted by macro factors (e.g., "elevated rates pressured auto finance margins")
- Flag macro-sensitive companies for future monitoring
- Note any management commentary that corroborates or contradicts the macro narrative
- If no macro context is provided, include a brief note: "No macro context provided — consider cross-referencing current rate, FX, and commodity data for fuller interpretation."

---

### STEP 8 — FORWARD LOOK

Include a brief "Looking Ahead" section that:
- Notes what sectors or themes to monitor in the coming week
- Flags any second-derivative signals from this week's results (e.g., a distributor's beat implies manufacturing demand is stable)
- Identifies any open questions raised by this week's guidance commentary that future reporters might answer

---

### OUTPUT FORMATTING RULES

- Use clear markdown headers (##, ###) for all sections
- Use emoji sparingly but consistently for visual scanning (📊 for recap title, 🏆 for top beat, 📉 for biggest miss, 📋 for scorecard, 🔍 for guidance, 🏭 for sector pulse, 🌐 for macro, 📅 for forward look)
- Keep individual company analysis concise: 3–5 sentences max per company in highlight sections
- The full scorecard table must include every company provided — do not omit any
- Add a footer noting the date range, that estimates are consensus at time of report, and a brief disclaimer that past stock reactions do not predict future performance
- Do not fabricate or estimate any numerical data not provided by the user — mark missing data as N/A and explain what data would be needed to complete the analysis
- Maintain a professional, neutral tone — avoid hyperbolic language like "crushing it" or "disaster"; use precise financial language
- If fewer than 3 companies are provided, note that the sample is too small for reliable sector or beat-rate trend analysis, but still complete all sections with the available data
- If the user provides more than 20 companies, produce abbreviated per-company notes and expand only the top 3 beats, top