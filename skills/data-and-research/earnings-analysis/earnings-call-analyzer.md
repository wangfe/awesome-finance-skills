---
name: Earnings Call Analyzer
description: Analyze an earnings call transcript to extract key metrics, management tone, guidance changes, and hidden risks
category: data-and-research/earnings-analysis
tags: [earnings, earnings-call, transcript-analysis, sentiment, guidance, research]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Processes an earnings call transcript (pasted by the user) and produces a structured analysis: headline results vs. expectations, management sentiment, forward guidance, key risks mentioned, analyst Q&A themes, and a bull/bear summary. Especially useful for quickly processing long transcripts to surface the most investment-relevant signals.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment decisions.

## Usage

Paste the full earnings call transcript (or as much as fits in context). The skill will work with partial transcripts but will note any gaps.

**Tip:** Most earnings transcripts are freely available on Seeking Alpha, The Motley Fool, or directly on the company's investor relations page.

## Example

**Input:**
```
[Paste earnings call transcript here]
```

**Output (abbreviated):**
```
=== Earnings Call Analysis: Example Corp Q4 2025 ===

HEADLINE RESULTS
  Revenue:     $2.1B  vs. $2.0B expected  ✅ +5% beat
  EPS (adj):   $1.45  vs. $1.38 expected  ✅ +5.1% beat
  Gross Margin: 42.1% vs. 41.5% prior yr  ✅ expanding

GUIDANCE
  Q1 2026 Revenue: $1.9–2.0B  [Street: $2.05B] ⚠ Below consensus
  FY 2026 EPS:     $5.80–6.00  [Street: $5.95B] 🟡 In-line

MANAGEMENT TONE
  Sentiment: 🟡 Cautious optimism
  Notable language: "macro headwinds," "prudent investment," "selective expansion"
  Confidence signals: Strong free cash flow commentary; buyback program reiterated

KEY RISKS MENTIONED
  1. FX headwinds (~$50M impact expected in H1 2026)
  2. Softening enterprise demand in EMEA
  3. Elevated inventory levels in hardware segment

ANALYST Q&A THEMES
  - 4 questions on guidance conservatism (management deflected specifics)
  - 3 questions on margin trajectory (constructive response)
  - 2 questions on M&A pipeline (no comment)

BULL CASE FROM CALL
  - Core business margin expanding
  - Share buyback program intact ($500M remaining)
  - New product cycle cited for H2 2026 acceleration

BEAR CASE FROM CALL
  - Q1 guidance below street; management credibility risk if missed again
  - FX drag not yet fully quantified
  - Enterprise softness is multi-quarter trend, not one-off

OVERALL SIGNAL: 🟡 MIXED — solid quarter but guidance reset warrants monitoring
```

## Skill Prompt

```
You are an equity research analyst processing an earnings call transcript.

Analyze the provided transcript and produce a structured report covering:

**1. HEADLINE RESULTS**
Extract: Revenue, EPS (GAAP and/or adjusted), Gross Margin, Operating Margin, Free Cash Flow.
If the transcript mentions consensus/street estimates, show actual vs. expected with beat/miss/in-line signal (✅/❌/🟡).

**2. GUIDANCE**
Extract all forward guidance provided (next quarter, full year, or multi-year).
Compare to any street estimates mentioned in the transcript.
Flag if guidance was raised, maintained, or lowered vs. prior guidance.

**3. MANAGEMENT TONE & SENTIMENT**
Assess overall tone: Bullish / Cautious Optimism / Neutral / Defensive / Bearish.
Quote 3–5 specific phrases that best reflect management's sentiment.
Note any language that signals confidence or hedging.

**4. KEY RISKS MENTIONED**
List the top 3–5 risks or headwinds management acknowledged (with any quantification provided).

**5. ANALYST Q&A THEMES**
Summarize the most frequently asked topics in the Q&A section.
Note any questions management deflected, avoided, or gave vague answers to.

**6. BULL CASE & BEAR CASE**
Based solely on what was said in the call:
- Bull Case: Top 3 positives or tailwinds discussed.
- Bear Case: Top 3 negatives or risks discussed.

**7. OVERALL SIGNAL**
Give a one-line investment signal: 🟢 Positive / 🟡 Mixed / 🔴 Negative
With a 2–3 sentence rationale.

Be objective. Only use information from the transcript — do not add outside knowledge.
Clearly note if the transcript appears partial or cut off.
```

## Notes

- Transcripts can be long; if the transcript exceeds the context window, ask the user to paste the prepared remarks and Q&A separately, or prioritize the Q&A section for risk/sentiment signals.
- This skill analyzes what management said — not whether it is true. Independent verification of numbers against filed financials is essential.
- For SEC filing analysis, see: `skills/data-and-research/sec-filings/`.
- Related skills: `skills/investing/stock-analysis/buffett-checklist.md`, `skills/accounting/ratio-analysis/financial-ratio-analyzer.md`.
