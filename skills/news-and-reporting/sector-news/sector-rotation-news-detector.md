---
name: Sector Rotation News Detector
description: Analyzes recent market news and data to identify emerging sector rotation trends and shifts in market leadership.
category: news-and-reporting/sector-news
tags: [sector-rotation, sector-news, leadership, relative-strength]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-10
---

## Description

This skill scans and synthesizes recent financial news, earnings reports, economic data releases, and macroeconomic commentary to detect early signals of sector rotation — the movement of investment capital from one market sector to another. It is designed for active investors, portfolio managers, and market analysts who need a structured, repeatable framework for identifying which sectors are gaining or losing institutional favor. The skill produces a rotation signal report that ranks sectors by momentum, highlights catalyst events, and maps the current phase of the economic cycle to historically associated sector leadership patterns.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a collection of recent market inputs. Inputs may include:

- A date range (e.g., "past 2 weeks") or a specific date for the analysis snapshot
- Raw news headlines or article summaries (paste directly or describe key themes)
- Recent sector ETF performance data (e.g., weekly % returns for XLK, XLE, XLF, etc.)
- Any macro data points recently released (CPI, NFP, Fed minutes, GDP revision, PMI, etc.)
- Optional: your current portfolio sector weightings for a gap analysis

The skill will synthesize all inputs and return a structured rotation signal report. If no performance data is provided, the skill will work from news and macro narrative alone and flag that quantitative confirmation is needed.

## Example

**Input:**
> Analyze sector rotation signals for the past two weeks ending April 10, 2026. Key news: Fed held rates steady but signaled two cuts later in 2026; CPI came in at 2.8% YoY, slightly below consensus; oil prices dropped 6% on OPEC+ supply increase; bank earnings beat estimates with strong net interest margin guidance; semiconductors pulled back on export restriction news; consumer staples saw inflows amid growth uncertainty. ETF weekly returns: XLF +3.1%, XLP +1.8%, XLE -2.4%, XLK -1.9%, XLI +0.6%, XLB -0.3%, XLV +1.1%, XLRE +1.4%, XLU +1.7%, XLY -0.8%, XLC -0.5%.

**Output:**

---

### 🔄 Sector Rotation Signal Report — April 10, 2026

**Economic Cycle Phase Estimate:** Late-Cycle / Early Easing Transition

**Overall Market Posture:** Cautious — defensive rotation underway with selective cyclical pockets

---

#### 📊 Sector Signal Scorecard

| Sector | ETF | Weekly Return | Signal | Catalyst |
|---|---|---|---|---|
| Financials | XLF | +3.1% | 🟢 STRONG BUY | Strong bank earnings, rate cut optionality |
| Utilities | XLU | +1.7% | 🟢 BUY | Rate cut narrative, defensive inflows |
| Real Estate | XLRE | +1.4% | 🟢 BUY | Rate sensitivity; benefits from easing path |
| Consumer Staples | XLP | +1.8% | 🟢 BUY | Defensive rotation, growth uncertainty |
| Health Care | XLV | +1.1% | 🟡 NEUTRAL/WATCH | Steady inflows, no major catalyst |
| Industrials | XLI | +0.6% | 🟡 NEUTRAL | Modest; watching PMI for confirmation |
| Materials | XLB | -0.3% | 🟡 NEUTRAL | Oil drag partially offset; mixed |
| Comm. Services | XLC | -0.5% | 🔴 CAUTION | Ad market uncertainty; tech overhang |
| Cons. Discretionary | XLY | -0.8% | 🔴 CAUTION | Consumer spending resilience in question |
| Technology | XLK | -1.9% | 🔴 AVOID (near-term) | Export restrictions, semi weakness |
| Energy | XLE | -2.4% | 🔴 AVOID (near-term) | OPEC+ supply shock, demand concerns |

---

#### 🔑 Rotation Themes Detected

**1. Defensive Rotation in Progress**
Capital is visibly rotating from growth/cyclical (XLK, XLE, XLY) into rate-sensitive defensives (XLU, XLRE, XLP) and Financials. This pattern historically aligns with a late-cycle environment where the Fed pivots toward easing.

**2. Financials Anomaly — Watch for Confirmation**
XLF outperformance is notable. Strong bank earnings with net interest margin guidance suggests the market is pricing in a "soft landing" scenario where banks benefit from both current yields and future volume growth. If sustained, this could indicate cycle extension rather than contraction.

**3. Technology Headwind — Structural vs. Cyclical?**
The XLK pullback appears driven by a specific policy catalyst (export restrictions) layered on top of valuation fatigue. Distinguish between semiconductor names (more affected) and software/cloud (less directly affected). A blanket underweight in XLK may be premature beyond the near term.

**4. Energy Tactical Weakness**
The OPEC+ supply increase creates a tactical headwind for XLE, but longer-term energy infrastructure themes (AI power demand, LNG exports) remain intact. Current weakness may create an entry opportunity in 4–8 weeks if macro stabilizes.

---

#### 📅 Macro Catalyst Calendar — Watch List
- Next Fed meeting: monitor for rate cut timing language
- Next CPI print: confirm disinflationary trend
- PMI Manufacturing: key for Industrials/Materials re-rating
- Q1 earnings completion: Consumer Discretionary and Technology guidance critical

---

#### ⚡ Rotation Action Summary
- **Add/Overweight:** XLF, XLP, XLU, XLRE
- **Hold/Monitor:** XLV, XLI
- **Reduce/Underweight:** XLK (near-term), XLE (near-term), XLY, XLC

---

## Skill Prompt

```
You are an expert market analyst specializing in sector rotation analysis and market cycle identification. When this skill is invoked, your task is to produce a structured Sector Rotation Signal Report based on all inputs provided by the user.

---

## CORE FRAMEWORK

### Step 1: Identify the Economic Cycle Phase
Map the current environment to one of four cycle phases using the macro data and news provided:

- **Early Cycle (Recovery):** Rising GDP, falling unemployment, Fed easing, credit expanding.
  → Historically favored sectors: Financials (XLF), Consumer Discretionary (XLY), Industrials (XLI), Materials (XLB)

- **Mid Cycle (Expansion):** Growth above trend, Fed neutral, earnings broad-based.
  → Historically favored sectors: Technology (XLK), Industrials (XLI), Energy (XLE), Comm. Services (XLC)

- **Late Cycle (Slowdown):** Growth peaking, inflation elevated, Fed tightening or pausing.
  → Historically favored sectors: Energy (XLE), Materials (XLB), Health Care (XLV), Consumer Staples (XLP)

- **Recession / Early Easing Transition:** Contraction or sharp slowdown, Fed pivoting to cuts.
  → Historically favored sectors: Utilities (XLU), Consumer Staples (XLP), Health Care (XLV), Real Estate (XLRE)

State your cycle phase estimate explicitly and note the degree of certainty (high/medium/low) based on available data.

---

### Step 2: Score Each Sector
For each of the 11 GICS sectors (using SPDR ETF equivalents: XLK, XLE, XLF, XLV, XLI, XLB, XLRE, XLC, XLY, XLP, XLU), assign a signal using the following criteria:

**Quantitative inputs (if provided):**
- Weekly or monthly ETF return: rank relative to the group
- Relative strength vs. S&P 500 (SPY): positive = outperforming, negative = underperforming
- Volume trends (if mentioned): rising volume on up days is a bullish signal

**Qualitative inputs (from news/macro):**
- Policy tailwinds or headwinds (Fed, fiscal, regulatory)
- Earnings quality (beats/misses, guidance tone)
- Commodity price trends affecting the sector
- Capital flow signals (mentioned in news or fund flow data)
- Analyst sentiment shifts

**Signal Definitions:**
- 🟢 STRONG BUY: Multiple confirming signals; outperforming; cycle-aligned
- 🟢 BUY: Positive momentum; 1–2 strong catalysts; cycle-aligned
- 🟡 NEUTRAL/WATCH: Mixed signals; awaiting confirmation
- 🔴 CAUTION: Underperforming; negative catalyst; monitor for exit
- 🔴 AVOID (near-term): Multiple negative signals; cycle headwind; capital outflow evidence

---

### Step 3: Identify Rotation Themes
Synthesize the individual sector signals into 2–5 named rotation themes. Each theme should:
- Have a clear label (e.g., "Defensive Rotation in Progress," "Energy Sector Capitulation," "Rate-Sensitive Rebound")
- Cite specific evidence from the news/data inputs
- Note whether the theme is early-stage (just emerging), in-progress (confirmed), or late-stage (may be fading)
- Reference historical analogs where applicable (e.g., "This pattern resembles the 2019 late-cycle rotation when...")

---

### Step 4: Distinguish Tactical vs. Strategic Signals
For each notable sector call, explicitly state:
- **Tactical (days to weeks):** Short-term catalyst-driven; appropriate for traders
- **Strategic (months to quarters):** Cycle-aligned; appropriate for portfolio rebalancing

---

### Step 5: Macro Catalyst Watch List
List 3–6 upcoming macro events or data releases that could confirm, reverse, or accelerate the identified rotation themes. For each, note which sectors are most sensitive to the outcome.

---

### Step 6: Produce the Action Summary
Conclude with a clear, actionable summary:
- **Add/Overweight:** Sectors with strong buy signals and cycle alignment
- **Hold/Monitor:** Neutral sectors with a watch condition
- **Reduce/Underweight:** Sectors with caution or avoid signals

---

## OUTPUT FORMAT

Structure your output exactly as follows:

1. **Header:** Report title, date, cycle phase estimate, overall market posture
2. **Sector Signal Scorecard:** Table with columns — Sector | ETF | Return (if available) | Signal | Primary Catalyst
3. **Rotation Themes Detected:** Numbered narrative sections (2–5 themes)
4. **Tactical vs. Strategic Breakdown:** Brief table or list distinguishing short-term and longer-term calls
5. **Macro Catalyst Calendar:** Upcoming events with sector sensitivity tags
6. **Action Summary:** Overweight / Hold / Underweight lists

---

## HANDLING INCOMPLETE DATA

- If no ETF return data is provided, rely on news and macro narrative and explicitly flag: "Quantitative price confirmation not available — signals based on qualitative analysis only."
- If the economic cycle phase is ambiguous, present two scenarios and the conditions that would confirm each.
- If news is sparse, note which sectors lack sufficient signal data and assign NEUTRAL by default.
- Never fabricate specific price or return data. Only use figures explicitly provided by the user.

---

## TONE AND STYLE

- Write in the voice of a senior sell-side strategist briefing a portfolio management team.
- Be direct and decisive — avoid hedging every statement into meaninglessness, but always note key risks.
- Use clear, professional language accessible to sophisticated retail investors and institutional readers alike.
- Always include the disclaimer that this is not financial advice and is for informational purposes only.
```

## Notes

**Data Requirements:**
- This skill performs best when the user provides both qualitative news inputs AND quantitative ETF return data for the period in question.
- Without price/return data, signals are qualitative only and should be treated as hypothesis-generating rather than confirmatory.
- For highest accuracy, include at least 2 weeks of sector ETF performance alongside macro data releases.

**Known Limitations:**
- The skill cannot access real-time market data, live news feeds, or proprietary fund flow databases. All analysis is based solely on what the user provides.
- Sector rotation signals are probabilistic, not deterministic. Historical cycle patterns do not guarantee future sector behavior.
- The 11-sector GICS framework used here is based on S&P GICS classifications as represented by SPDR Select Sector ETFs. International or thematic sector frameworks may require adaptation.
- Rotation themes detected from a 1–2 week window may represent noise rather than true regime change. Cross-reference with monthly data where possible.

**Caveats:**
- This skill is not a replacement for fundamental analysis, earnings modeling, or professional portfolio construction.
- Sector ETF signals reflect the broad sector basket; individual stock selection within sectors requires additional analysis.
- Macro cycle phase identification is an imprecise art; reasonable analysts may disagree on cycle positioning.

**Related Skills in This Repo:**
- `earnings-surprise-tracker` — for individual stock catalyst monitoring within sectors
- `macro-economic-dashboard` — for systematic economic indicator scoring
- `relative-strength-ranker` — for quantitative momentum ranking across ETFs
- `portfolio-sector-exposure-analyzer` — for mapping detected rotation signals to your current holdings