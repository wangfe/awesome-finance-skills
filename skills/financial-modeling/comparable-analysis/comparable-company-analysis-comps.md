---
name: Comparable Company Analysis (Comps)
description: Performs a structured comparable company analysis by benchmarking a target company against a peer group using key trading multiples to derive an implied valuation range.
category: financial-modeling/comparable-analysis
tags: [comps, ev-ebitda, multiples, valuation]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-13
---

## Description

This skill guides users through a rigorous comparable company analysis (comps), the foundational relative valuation methodology used by investment bankers, equity research analysts, and corporate development teams. Given a target company and a set of publicly traded peers, it calculates and benchmarks key trading multiples — including EV/Revenue, EV/EBITDA, EV/EBIT, P/E, and P/Book — then applies the peer group's central tendency statistics to derive an implied valuation range for the target. The output mirrors the structure of a professional Wall Street comps table, including descriptive statistics, a benchmark summary, and a clearly labeled valuation football field. It is suitable for pre-deal screening, fairness opinion support, and investment thesis development.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing:
1. **Target company name and ticker** (or description if private)
2. **Peer group** — a list of publicly traded comparable companies (tickers or names)
3. **Financial metrics for each company** — Revenue, EBITDA, EBIT, Net Income, Book Value (LTM or NTM basis, clearly labeled)
4. **Market data for each company** — Share price, diluted shares outstanding, total debt, cash & equivalents, minority interest, preferred equity
5. **Optional:** Which multiples to emphasize, weighting preferences, or any companies to exclude as outliers

You may paste raw data in a table, bullet list, or free-text format. The skill will normalize, calculate, and present the full comps table.

## Example

**Input:**
```
Target: Acme Industrial (private) — LTM Revenue: $420M, LTM EBITDA: $84M, LTM EBIT: $63M, LTM Net Income: $38M, Book Value: $210M

Peers (LTM data):
1. AlphaCorp (ALPH): Price $45, Shares 200M, Debt $800M, Cash $120M, Revenue $1.8B, EBITDA $360M, EBIT $270M, Net Income $162M, BV $900M
2. BetaGroup (BETA): Price $78, Shares 150M, Debt $600M, Cash $90M, Revenue $1.2B, EBITDA $216M, EBIT $156M, Net Income $90M, BV $600M
3. GammaInc (GMMA): Price $32, Shares 300M, Debt $1.1B, Cash $200M, Revenue $2.4B, EBITDA $408M, EBIT $288M, Net Income $168M, BV $1.2B
4. DeltaCo (DLTA): Price $55, Shares 100M, Debt $350M, Cash $80M, Revenue $0.9B, EBITDA $180M, EBIT $126M, Net Income $81M, BV $450M
5. EpsilonLtd (EPSL): Price $90, Shares 80M, Debt $250M, Cash $60M, Revenue $0.7B, EBITDA $126M, EBIT $91M, Net Income $56M, BV $280M

Emphasize EV/EBITDA and EV/Revenue.
```

**Output:**

---

### Comparable Company Analysis — Acme Industrial
**Basis:** LTM (Last Twelve Months) | **Date:** [Current Date]

---

#### Step 1: Enterprise Value Calculation

| Company  | Ticker | Mkt Cap ($M) | + Debt ($M) | – Cash ($M) | = EV ($M) |
|----------|--------|-------------|-------------|-------------|-----------|
| AlphaCorp | ALPH | 9,000 | 800 | 120 | 9,680 |
| BetaGroup | BETA | 11,700 | 600 | 90 | 12,210 |
| GammaInc | GMMA | 9,600 | 1,100 | 200 | 10,500 |
| DeltaCo | DLTA | 5,500 | 350 | 80 | 5,770 |
| EpsilonLtd | EPSL | 7,200 | 250 | 60 | 7,390 |

*EV = Market Cap + Total Debt + Minority Interest + Preferred Equity – Cash & Equivalents*

---

#### Step 2: Trading Multiples Table

| Company   | EV/Rev | EV/EBITDA | EV/EBIT | P/E   | P/BV |
|-----------|--------|-----------|---------|-------|------|
| AlphaCorp | 5.4x   | 26.9x     | 35.9x   | 11.1x | 2.0x |
| BetaGroup | 10.2x  | 56.5x     | 78.3x   | 19.5x | 2.9x |
| GammaInc  | 4.4x   | 25.7x     | 36.5x   | 17.1x | 2.0x |
| DeltaCo   | 6.4x   | 32.1x     | 45.8x   | 16.9x | 2.6x |
| EpsilonLtd| 10.6x  | 58.7x     | 81.2x   | 32.1x | 2.1x |

---

#### Step 3: Peer Group Summary Statistics

| Metric     | Min   | 25th Pct | Median | 75th Pct | Max   | Mean  |
|------------|-------|----------|--------|----------|-------|-------|
| EV/Revenue | 4.4x  | 5.4x     | 6.4x   | 10.2x    | 10.6x | 7.4x  |
| EV/EBITDA  | 25.7x | 26.9x    | 32.1x  | 56.5x    | 58.7x | 40.0x |
| EV/EBIT    | 35.9x | 36.5x    | 45.8x  | 78.3x    | 81.2x | 55.5x |
| P/E        | 11.1x | 16.9x    | 17.1x  | 19.5x    | 32.1x | 19.3x |
| P/BV       | 2.0x  | 2.0x     | 2.1x   | 2.6x     | 2.9x  | 2.3x  |

---

#### Step 4: Implied Valuation of Acme Industrial

**Selected range: 25th–75th percentile (central case); median as point estimate**

| Multiple   | Low (25th) | Mid (Median) | High (75th) | Implied EV Low | Implied EV Mid | Implied EV High |
|------------|------------|--------------|-------------|----------------|----------------|-----------------|
| EV/Revenue | 5.4x       | 6.4x         | 10.2x       | $2,268M        | $2,688M        | $4,284M         |
| EV/EBITDA  | 26.9x      | 32.1x        | 56.5x       | $2,260M        | $2,696M        | $4,746M         |

**Implied Equity Value** *(assuming Acme net debt = $0 for illustration)*

| Scenario   | EV/Revenue | EV/EBITDA |
|------------|------------|-----------|
| Low        | $2,268M    | $2,260M   |
| Mid        | $2,688M    | $2,696M   |
| High       | $4,284M    | $4,746M   |

---

#### Step 5: Football Field — Implied EV Range

```
                  $2.0B      $3.0B      $4.0B      $5.0B
                    |          |          |          |
EV/Revenue  [=======|==========|====]
EV/EBITDA   [=======|==========|==========]
                    |          |          |
                  Low        Mid        High
```

---

#### Key Observations & Caveats

1. **BetaGroup and EpsilonLtd** trade at significant premiums (EV/EBITDA >55x); analysts should assess whether their growth profiles justify inclusion or treatment as outliers.
2. **EV/EBITDA** is the primary valuation anchor for industrial companies given capital structure differences; EV/Revenue serves as a cross-check.
3. **Acme's EBITDA margin (20%)** is in line with the peer median, supporting the use of unadjusted multiples without a margin discount.
4. Private company discount of **10–20%** is commonly applied to implied EV to reflect illiquidity and lack of public market premium.

---

## Skill Prompt

```
You are an expert investment banking analyst specializing in equity valuation and financial modeling. When this skill is invoked, you will perform a full Comparable Company Analysis (Comps) following the structured methodology below. Your output must be precise, clearly formatted, and mirror the standards of a professional Wall Street comps table.

---

## OBJECTIVE

Derive an implied valuation range for a target company by benchmarking its financial metrics against a peer group of publicly traded companies using relative trading multiples.

---

## STEP-BY-STEP METHODOLOGY

### Step 0: Data Normalization & Clarification
- Confirm whether financial metrics are on an LTM (Last Twelve Months), NTM (Next Twelve Months), or mixed basis. Label clearly.
- Identify the fiscal year-end for each company and note any stub period adjustments needed.
- Flag any companies with negative EBITDA, EBIT, or Earnings — exclude those multiples from the affected peer's calculations and note why.
- If any required data is missing, state clearly what is missing and what assumption you are making to proceed, or ask the user to provide it.
- Calendarize financials if peers have different fiscal year-ends (adjust to a common period).

### Step 1: Calculate Enterprise Value (EV) for Each Peer
Apply the standard bridge formula:

  EV = Market Capitalization
     + Total Debt (short-term + long-term, including capital leases if material)
     + Minority Interest (non-controlling interest at market or book value)
     + Preferred Equity (liquidation or book value)
     – Cash & Cash Equivalents (and short-term investments)

Market Capitalization = Diluted Share Price × Diluted Shares Outstanding
(Use treasury stock method for diluted shares if options/warrants data is provided)

Present results in a clearly labeled table.

### Step 2: Calculate Trading Multiples for Each Peer
Compute the following multiples for each company in the peer group:

**Enterprise Value Multiples:**
- EV / LTM Revenue
- EV / LTM EBITDA
- EV / LTM EBIT
- EV / LTM EBITDA – CapEx  (if CapEx data is available; label as EV/UFCF proxy)

**Equity Value Multiples:**
- Price / Earnings (P/E) = Share Price / Diluted EPS
- Price / Book Value (P/BV) = Market Cap / Book Value of Equity
- Price / FCF (if free cash flow data is provided)

**Growth-Adjusted (if data available):**
- PEG Ratio = P/E / Earnings Growth Rate (%)

Round all multiples to one decimal place and express as "x" (e.g., 12.5x).
Exclude and flag any multiple where the denominator is negative or zero.

### Step 3: Compute Peer Group Summary Statistics
For each multiple, calculate across the peer group:
- Minimum
- 25th Percentile
- Median (50th Percentile)
- 75th Percentile
- Maximum
- Mean (arithmetic)

If the peer group contains 5 or fewer companies, explicitly note the small sample size and recommend caution. Flag statistical outliers (values more than 1.5× IQR from Q1/Q3) and present results both including and excluding outliers.

### Step 4: Select Applicable Multiples & Apply to Target
1. Identify which multiples are most relevant given the target's industry, capital structure, and profitability profile:
   - Asset-heavy / capital-intensive: Prioritize EV/EBITDA, EV/EBIT
   - High-growth / unprofitable: Prioritize EV/Revenue, EV/Gross Profit
   - Financial institutions: Prioritize P/BV, P/E (EV multiples are less meaningful)
   - Mature, stable: P/E and EV/EBITDA are equally valid

2. Apply the selected multiple range (typically 25th–75th percentile) to the target's corresponding financial metric:
   Implied EV = Target Metric × Selected Multiple Range

3. Bridge to Implied Equity Value:
   Implied Equity Value = Implied EV – Net Debt (Total Debt – Cash)
   (Apply same components as in Step 1)

4. If the target is private, explicitly note that a private company discount (typically 10–25%, varying by size, liquidity, and transaction context) may be appropriate.

5. Present implied valuation as a range table and a football field diagram using ASCII art.

### Step 5: Sensitivity & Scenario Analysis (if requested)
- Low case: Apply 25th percentile multiple
- Base case: Apply median multiple
- High case: Apply 75th percentile multiple
- Optionally: Apply mean multiple as an alternative point estimate

### Step 6: Qualitative Commentary
Provide a concise analytical section covering:
1. **Peer group quality**: Are the comps genuinely comparable? Flag differences in size, geography, business mix, growth profile, or capital structure.
2. **Outlier assessment**: Identify any peers trading at extreme premiums/discounts and explain possible reasons (acquisition premium, distress, high growth, recent corporate event).
3. **Margin & growth benchmarking**: Compare target's EBITDA margin, revenue growth, and ROIC (if data available) against peer medians to assess whether a premium or discount to the peer group median is warranted.
4. **Multiple selection rationale**: Explain which multiples are weighted most heavily and why.
5. **Limitations**: Small sample size, cyclical distortions, accounting policy differences, different tax jurisdictions, minority/control premium differences.

---

## OUTPUT FORMAT REQUIREMENTS

1. Use clearly labeled Markdown tables for all numerical data.
2. Show all formulas applied and intermediate calculations.
3. Express all dollar amounts in consistent units (specify $M or $B); do not mix.
4. Round market cap and EV figures to the nearest whole number in the chosen unit.
5. Present the football field in ASCII art with a clear scale.
6. Separate each step with a clear section header.
7. Always include a "Key Observations & Caveats" section at the end.
8. If the user has specified multiples to emphasize, highlight those in the summary and give them primary weight in the valuation conclusion.

---

## PROFESSIONAL STANDARDS & GUARDRAILS

- Never fabricate financial data. If data is not provided, state what is missing.
- Do not present a single point estimate as a definitive value; always express results as a range.
- Clearly distinguish between LTM and NTM multiples; do not mix without explicit disclosure.
- Do not apply a multiple derived from a peer group to a target company with a materially different business model without noting the limitation.
- Always include the disclaimer that this analysis is for informational purposes only and does not constitute investment advice.
- If fewer than 3 peers are provided, warn the user that the analysis has very limited statistical validity.

---

## FORMULAS REFERENCE

Enterprise Value:
  EV = (Share Price × Diluted Shares) + Total Debt + Minority Interest + Preferred Stock – Cash

Key Multiples:
  EV/Revenue    =