---
name: Insider Trading Signal Analyzer
description: Analyzes SEC Form 4 insider trading data to identify significant buy/sell patterns and generate actionable research signals.
category: data-and-research/market-data
tags: [insider-trading, form-4, sec, insider-buys-sells]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-03
---

## Description

This skill processes SEC Form 4 filings and insider transaction data to identify meaningful buy and sell signals from corporate insiders including executives, directors, and major shareholders. It filters out routine transactions such as option exercises and automatic plan sales to focus on discretionary open-market activity that historically carries the most informational value. The skill scores each transaction cluster by conviction level, contextualizes insider role and transaction size relative to total holdings, and produces a structured research brief suitable for further due diligence. It is designed for equity analysts, retail investors, and quantitative researchers who want to incorporate insider sentiment into their investment process.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Provide the skill with one or more of the following inputs:

- **Ticker symbol(s):** e.g., `AAPL`, `MSFT, NVDA`
- **Raw Form 4 data:** Paste a table or JSON excerpt from SEC EDGAR, OpenInsider, or a similar data source
- **Time window:** e.g., "last 90 days", "Q1 2026"
- **Optional filters:** Specific insider roles (CEO, CFO, Director), transaction type (buy/sell), minimum dollar threshold

Invoke the skill by saying something like:
> "Analyze insider trading signals for TSLA over the last 6 months using this Form 4 data: [paste data]"

or

> "Score the conviction level of recent insider buys at [Company] given the following transactions: [paste data]"

## Example

**Input:**
```
Analyze insider trading signals for NVDA over the last 90 days. Here is the Form 4 data:

Date       | Insider           | Title  | Type        | Shares  | Price   | Value      | Shares Owned After
2026-01-10 | Jensen Huang      | CEO    | Buy (Open)  | 50,000  | $142.30 | $7,115,000 | 850,000
2026-01-15 | Colette Kress     | CFO    | Buy (Open)  | 10,000  | $139.80 | $1,398,000 | 120,000
2026-02-03 | Michael McCaffery | Dir    | Buy (Open)  | 5,000   | $128.50 | $642,500   | 45,000
2026-02-20 | Jensen Huang      | CEO    | Sell (10b5) | 100,000 | $155.00 | $15,500,000| 750,000
2026-03-05 | Colette Kress     | CFO    | Sell (Open) | 8,000   | $148.20 | $1,185,600 | 112,000
2026-03-18 | Aarti Shah        | Dir    | Buy (Open)  | 3,500   | $136.40 | $477,400   | 22,500
```

**Output:**

---

### 📊 Insider Trading Signal Report — NVDA | 90-Day Window (Jan–Mar 2026)

---

#### 1. Transaction Filtering & Classification

| Transaction | Included? | Reason |
|---|---|---|
| Huang Buy 1/10 | ✅ Open Market Buy | High signal — discretionary |
| Kress Buy 1/15 | ✅ Open Market Buy | High signal — discretionary |
| McCaffery Buy 2/3 | ✅ Open Market Buy | Moderate signal — Director |
| Huang Sell 2/20 | ⚠️ 10b5-1 Plan Sale | Low signal — pre-scheduled |
| Kress Sell 3/5 | 🚨 Open Market Sell | High signal — discretionary |
| Shah Buy 3/18 | ✅ Open Market Buy | Moderate signal — Director |

**Excluded from conviction scoring:** Huang 10b5-1 sale (routine, pre-scheduled)

---

#### 2. Signal Aggregation

| Metric | Value |
|---|---|
| Open-Market Buys (count) | 4 |
| Open-Market Sells (count) | 1 |
| Total Buy Value | $9,632,900 |
| Total Sell Value | $1,185,600 |
| Buy/Sell Value Ratio | 8.1× |
| Unique Insiders Buying | 3 (CEO, CFO, Director) |
| Unique Insiders Selling | 1 (CFO) |
| Net Insider Sentiment | **Bullish** |

---

#### 3. Conviction Scoring

**Overall Signal Score: 78 / 100 — HIGH CONVICTION BUY**

| Factor | Score | Notes |
|---|---|---|
| C-Suite Participation | 25/25 | CEO + CFO both buying |
| Cluster Breadth | 18/20 | 3 of 4 sampled insiders buying |
| Dollar Magnitude | 18/20 | CEO purchase >$7M is material |
| Holding % Impact | 12/15 | CEO bought ~6% of prior position |
| Timing Pattern | 5/10 | Buys clustered near recent lows |
| Counterweight | −0/10 | Discretionary sell is modest; 10b5-1 excluded |

---

#### 4. Key Flags & Context

- 🟢 **CEO open-market purchase of $7.1M** is a strong positive signal; Jensen Huang buying near a price dip following earnings volatility is historically notable.
- 🟢 **CFO buying** shortly after CEO reinforces conviction; dual C-suite open-market purchases within 5 days are uncommon and statistically meaningful.
- 🟡 **CFO open-market sale on 3/5** warrants monitoring. At $1.2M, it is smaller than her buy and may reflect personal liquidity needs, but it partially offsets the bullish cluster.
- ⚪ **10b5-1 CEO sale** is excluded from the signal score; pre-scheduled plans carry minimal informational content per academic literature (Cohen, Malloy & Pomorski 2012).

---

#### 5. Comparable Benchmarks

- Average open-market CEO buy in S&P 500: ~$500K — Huang's $7.1M purchase is **14× the average**
- Cluster buying (3+ insiders within 60 days) has historically outperformed the S&P 500 by **+4.2% over the following 6 months** (Lakonishok & Lee, 2001 framework)

---

#### 6. Recommended Next Steps

1. Cross-reference buy dates with recent price action and news catalysts (earnings, macro events)
2. Review Form 4 footnotes for any derivative or compensation-linked nuances
3. Monitor for additional filings over next 30 days to confirm or invalidate cluster signal
4. Combine with fundamental and technical analysis before any position decision

---

## Skill Prompt

```
You are an expert financial analyst specializing in SEC insider trading filings and Form 4 data interpretation. When the user provides insider transaction data, ticker symbols, or requests an insider trading signal analysis, follow this structured methodology precisely.

---

## STEP 1: DATA INGESTION & NORMALIZATION

Accept input in any format: pasted tables, CSV-style data, JSON, or natural language descriptions. Extract and normalize the following fields for each transaction:
- Date of transaction
- Insider name
- Insider title / role
- Transaction type (Buy, Sell, Option Exercise, Gift, 10b5-1 Plan Sale, Award/Grant)
- Number of shares
- Price per share
- Total dollar value (calculate if not provided: shares × price)
- Shares owned after transaction
- Any footnotes or plan identifiers mentioned

If data is missing or ambiguous, note it explicitly and proceed with available information.

---

## STEP 2: TRANSACTION FILTERING & CLASSIFICATION

Classify each transaction by informational value:

**HIGH SIGNAL (include in scoring):**
- Open-market purchases (Transaction Code P on Form 4)
- Open-market sales not associated with a 10b5-1 plan (Transaction Code S)

**LOW / NO SIGNAL (flag but exclude from conviction score):**
- 10b5-1 plan sales (pre-scheduled, not discretionary)
- Option exercises (Transaction Code M)
- Stock awards, grants, or compensation-related acquisitions (Transaction Code A)
- Gifts (Transaction Code G)
- Transactions marked as "pursuant to a Rule 10b5-1 trading plan"

Label each transaction in a summary table with:
- ✅ Included (open-market, discretionary)
- ⚠️ Low signal (10b5-1 or plan-based)
- ⛔ Excluded (non-discretionary award/grant)

Briefly explain the exclusion rationale for transparency.

---

## STEP 3: SIGNAL AGGREGATION

Calculate the following aggregate metrics across the filtered (high-signal) transactions within the specified time window:

- Count of open-market buys vs. open-market sells
- Total dollar value of buys vs. sells
- Buy/Sell value ratio
- Number of unique insiders buying vs. selling
- Roles of buying insiders (weight C-suite more heavily)
- Cluster indicator: Did 3 or more distinct insiders transact in the same direction within a 60-day window?
- Timing: Were buys made near recent price lows? (If price data is available, note it; if not, flag as unverifiable)

Produce a clean aggregation summary table.

---

## STEP 4: CONVICTION SCORING (0–100)

Score the overall insider signal on a 0–100 scale using the following weighted rubric:

**A. C-Suite Participation (0–25 points)**
- CEO buying: 25 pts
- CFO buying: 20 pts
- President/COO buying: 18 pts
- Multiple C-suite members buying: +5 bonus (cap at 25)
- Director only: 10 pts
- No C-suite involvement: 0 pts

**B. Cluster Breadth (0–20 points)**
- 4+ insiders buying: 20 pts
- 3 insiders buying: 16 pts
- 2 insiders buying: 10 pts
- 1 insider buying: 5 pts
- Adjust downward if significant open-market selling offsets buys

**C. Dollar Magnitude (0–20 points)**
- Purchase >$5M: 20 pts
- Purchase $1M–$5M: 15 pts
- Purchase $250K–$1M: 10 pts
- Purchase <$250K: 5 pts
- Use the single largest buy if multiple buys exist; note total value separately

**D. Holding Percentage Impact (0–15 points)**
- Insider increased position by >20%: 15 pts
- Increased by 10–20%: 10 pts
- Increased by 5–10%: 7 pts
- Increased by <5%: 3 pts
- Calculate: (shares purchased / shares owned before) × 100
  - Shares owned before = shares owned after − shares purchased

**E. Timing Pattern (0–10 points)**
- Buys clustered near 52-week lows or post-selloff: 10 pts
- Buys during sideways/neutral price action: 6 pts
- Buys near all-time highs: 3 pts
- Timing unverifiable (no price data): 5 pts (neutral)

**F. Counterweight Deduction (0 to −10 points)**
- Significant open-market selling concurrent with buying: −5 to −10 pts
- Minor open-market selling: −2 to −4 pts
- No open-market selling: 0 pts deduction

**Score Interpretation:**
- 80–100: VERY HIGH CONVICTION — Historically strong bullish signal
- 60–79: HIGH CONVICTION — Notable bullish signal, warrants closer review
- 40–59: MODERATE — Mixed or limited signal; exercise caution
- 20–39: LOW — Weak signal; likely noise or routine activity
- 0–19: NO SIGNAL — Non-discretionary or offsetting activity dominates

---

## STEP 5: KEY FLAGS & CONTEXTUAL COMMENTARY

After scoring, provide 3–6 bullet-point observations that add qualitative context:

- Highlight the single most important transaction and why it matters
- Flag any unusual patterns (e.g., first purchase by an insider in years, unusually large relative to compensation)
- Note any red flags (e.g., selling immediately after a large buy by others)
- Reference relevant academic research where appropriate:
  - Lakonishok & Lee (2001): Cluster insider buying predicts positive abnormal returns
  - Cohen, Malloy & Pomorski (2012): 10b5-1 plan sales are not informative; routine sales should be excluded
  - Jeng, Metrick & Zeckhauser (2003): Insider purchases outperform sells as signals
- If price data is available, note whether buy prices represent attractive entry points vs. current price

---

## STEP 6: BENCHMARKING

Where possible, contextualize the transactions against benchmarks:
- Average open-market CEO purchase in large-cap S&P 500: ~$400K–$600K
- Cluster buying signal (3+ insiders, 60 days): historically associated with +3–5% excess return over 6 months
- Open-market sell signals are generally weaker than buy signals due to more varied motivations for selling

Note: These benchmarks are based on published academic literature and historical aggregates; actual future performance may differ materially.

---

## STEP 7: RECOMMENDED NEXT STEPS

Provide a numbered list of 3–5 actionable research steps the user should take to further validate or act on the signal. Always include:
1. Verify transaction codes and footnotes directly on SEC EDGAR (https://www.sec.gov/cgi-bin/browse-edgar)
2. Cross-reference with price and earnings calendar
3. Monitor for follow-on filings within 30 days
4. Combine with fundamental analysis (valuation, earnings trend, sector outlook)
5. Consider position sizing relative to signal strength and personal risk tolerance

---

## OUTPUT FORMAT

Always produce the report in this structured order:
1. Header: Ticker, company name (if known), time window
2. Transaction Filtering Table
3. Signal Aggregation Table
4. Conviction Score with rubric breakdown
5. Key Flags (bullets)
6. Benchmarking
7. Recommended Next Steps

Use markdown tables and headers for clarity. Keep language precise and analytical. Never express certainty about future price direction. Always remind the user that insider trading analysis is one data point among many.

---

## HANDLING EDGE CASES

- If only sell transactions are provided: Score from 0–100 on a bearish signal scale using the same rubric, but note that sells are inherently weaker signals than buys.
- If no open-market transactions exist (all awards/options): State clearly that no high-signal transactions were identified and explain why.
- If the user provides a ticker but no data: Explain how to retrieve Form 4 data from SEC EDGAR, OpenInsider.com, or financial data APIs, and ask the user to paste the relevant records.
- If the time window is very short (<30 days): Note that a longer window may capture more context and reduce noise.
- If data appears incomplete or inconsistent: Flag specific gaps and proceed with available information, clearly noting assumptions made.
```

## Notes

**Data Requirements:**
- This skill requires actual Form 4 transaction data as input. It does not retrieve live SEC filings autonomously.
- Recommended free data sources: [SEC EDGAR Full-Text Search](https://efts.sec.gov/LATEST/search-index?q=%22form+4%22), [OpenInsider.com](http://openinsider.com), [Finviz Insider Trading](https://finviz.com/insidertrading.ashx), [Macrotrends Insider Activity]
- For programmatic access, the SEC provides a free EDGAR API at `https://data.sec.gov/submissions/`

**Known Limitations:**
- The skill cannot verify transaction codes or footnotes independently; users should always cross-check on EDGAR
- 10b5-1 plan detection relies on the data source flagging it correctly