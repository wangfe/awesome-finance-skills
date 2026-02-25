---
name: Fed Statement & FOMC Analyzer
description: Analyze Federal Reserve statements, FOMC minutes, or Fed chair speeches to extract policy signals, rate path implications, and market impact
category: news-and-reporting/market-analysis
tags: [fed, fomc, monetary-policy, interest-rates, central-bank, macro]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Processes Federal Reserve communications — FOMC statements, meeting minutes, Fed chair press conferences, or speeches — and extracts the policy signal, language changes from prior statements, rate path implications, and the likely market impact across equities, bonds, and currencies. Especially useful immediately after Fed events.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Paste the full text (or key excerpts) of:
- An FOMC post-meeting statement
- Fed meeting minutes
- A Fed chair (e.g., Powell) speech or press conference transcript
- Any central bank communication

Works best with the full text but can extract useful signals from key paragraphs.

## Example

**Input:**
```
[Paste FOMC statement or Fed speech text here]
```

**Output:**
```
=== FOMC STATEMENT ANALYSIS ===
Date: [statement date]

POLICY DECISION
  Rate Decision:    Held at 5.25–5.50% (unchanged)
  Vote:             11-1 (1 dissent: preferred 25bp cut)

LANGUAGE SHIFT TRACKER (vs. prior statement)
  ADDED:     "inflation has eased substantially toward our 2% goal"
  REMOVED:   "inflation remains elevated"
  CHANGED:   "additional firming" → "any additional firming" (dovish hedge)
  KEY PHRASE: "The Committee does not expect it will be appropriate to
               reduce rates until it has gained greater confidence..."
  Shift:     🟡 MILDLY DOVISH — softened language, maintained patience signal

POLICY SIGNAL
  Stance:         Data-dependent pause
  Rate Path:      No cuts imminent; market pricing 2–3 cuts over next 12 months
  Key Triggers:   Further inflation progress + labor market cooling needed
  Hawkish Risk:   Inflation re-acceleration or wage growth re-acceleration
  Dovish Risk:    Sharp labor market weakening or financial market stress

ECONOMIC ASSESSMENT (from statement)
  Growth:     "Economy has continued to expand at a solid pace"  🟢
  Labor:      "Job gains have moderated but remain strong"       🟡
  Inflation:  "Inflation has eased but remains somewhat elevated" 🟡
  Financial:  No stress language                                  🟢

MARKET IMPLICATIONS
  Equities:   🟢 Positive — rate pause removes near-term headwind
              Growth/tech names benefit from stable rate environment
  Bonds:      🟢 Positive for duration — yields likely to drift lower
              2Y Treasury most sensitive to Fed path; watch 4.50% level
  USD:        🟡 Neutral-to-weak — pause + eventual cuts = mild USD softness
  Gold:       🟡 Mild tailwind — real rates stable/declining

TRADERS' CHECKLIST
  📌 Watch next CPI print — path to cuts depends on sustained disinflation
  📌 Dot plot (next SEP): will median 2026 dot shift from 2 to 3 cuts?
  📌 Labor market: next NFP — any significant weakening accelerates cut timeline
  📌 Fed fund futures: monitor pricing for shift post-statement
```

## Skill Prompt

```
You are a monetary policy analyst specializing in Federal Reserve communications.

Analyze the provided Fed statement, FOMC minutes, or speech and produce a structured report:

**1. POLICY DECISION** (if a statement/meeting)
- Rate decision and new target range.
- Vote tally and any dissents (note dissenter's preference if mentioned).

**2. LANGUAGE SHIFT TRACKER**
This is the most important section. Compare language to what you know of recent Fed communications:
- ADDED phrases (new language, more prominent themes).
- REMOVED phrases (deleted from prior communication — often signals intent).
- CHANGED phrases (word substitutions that imply directional shift).
- KEY PHRASE: the single most important sentence in the document.
- Overall shift: 🟢 DOVISH / 🟡 NEUTRAL / 🔴 HAWKISH — with brief rationale.

**3. POLICY SIGNAL**
- Current stance in plain English (e.g., "data-dependent pause," "tightening bias," "easing cycle begun").
- Rate path implied by the language (not market pricing — what the statement itself suggests).
- Key data triggers that would push the Fed toward cuts vs. more hikes.
- Hawkish risk and Dovish risk in one line each.

**4. ECONOMIC ASSESSMENT**
Extract the Fed's characterization of: Growth | Labor Market | Inflation | Financial Conditions.
Rate each 🟢 Strong / 🟡 Mixed / 🔴 Weak based on Fed's own language.

**5. MARKET IMPLICATIONS**
For each asset class, state the directional implication (🟢/🟡/🔴) and a one-line rationale:
- Equities (broad; growth vs. value distinction if relevant)
- Bonds / Duration (short-end vs. long-end)
- USD
- Gold / Commodities

**6. TRADERS' CHECKLIST**
3–5 specific items to watch in the coming days/weeks: upcoming data, next Fed event, key levels.

**IMPORTANT**
- Base your language shift analysis on well-known Fed communication patterns.
- Do not fabricate specific prior statement text — if unsure, say "relative to recent hawkish tone."
- Clearly distinguish between what the statement says vs. market interpretation.
- Avoid jargon without explanation (e.g., explain "dot plot" if referenced).
```

## Notes

- FOMC statements are published at federalreserve.gov/monetarypolicy/fomccalendars.htm (free, public).
- For maximum value, provide both the new statement AND the prior statement so the skill can do precise language diff.
- Fed meeting minutes (released ~3 weeks after the meeting) provide richer context on internal debate — paste those for deeper analysis.
- Related skills: `skills/data-and-research/economic-indicators/`, `skills/news-and-reporting/daily-digest/daily-financial-news-report.md`
