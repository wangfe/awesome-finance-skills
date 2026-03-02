---
name: ETF Expense Ratio Comparator
description: Compares expense ratios across multiple ETFs to quantify the long-term cost impact on portfolio returns.
category: investing/etf-funds
tags: [etf, expense-ratio, index-funds, cost-comparison]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-02
---

## Description

This skill analyzes and compares expense ratios across a user-supplied list of ETFs, calculating the cumulative drag on investment returns over multiple time horizons. It helps investors understand how seemingly small differences in annual fees compound into significant wealth erosion over time. The skill produces a side-by-side comparison table, break-even analysis, and a ranked recommendation based purely on cost efficiency. It is designed for both beginner investors evaluating their first index fund and experienced portfolio managers auditing existing holdings.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing a list of ETFs you want to compare. For each ETF, supply:
- **Ticker symbol** (e.g., VOO, SPY, IVV)
- **Expense ratio** as a percentage (e.g., 0.03%)
- **Optional:** Current net asset value (NAV) or share price
- **Optional:** Initial investment amount (defaults to $10,000)
- **Optional:** Assumed annual gross return (defaults to 7%)
- **Optional:** Time horizons for projection (defaults to 5, 10, 20, and 30 years)

You may also simply list ticker symbols and ask Claude to use known/publicly available expense ratios, with the understanding that figures should be verified against official fund prospectuses.

## Example

**Input:**
Compare the expense ratios of VOO (0.03%), SPY (0.0945%), and IVV (0.03%) assuming a $50,000 initial investment, 7% gross annual return, over 10, 20, and 30 years.

**Output:**

### ETF Expense Ratio Comparison Report

**Inputs Assumed**
| Parameter | Value |
|---|---|
| Initial Investment | $50,000 |
| Gross Annual Return | 7.00% |
| Time Horizons | 10, 20, 30 years |

---

### 1. Expense Ratio Summary

| ETF | Expense Ratio | Annual Cost on $50,000 | Category |
|---|---|---|---|
| VOO | 0.0300% | $15.00 | Ultra-Low |
| IVV | 0.0300% | $15.00 | Ultra-Low |
| SPY | 0.0945% | $47.25 | Low |

---

### 2. Projected Portfolio Value After Fees

*Formula: FV = PV × (1 + r_net)^t, where r_net = gross_return − expense_ratio*

| ETF | Net Return | 10 Years | 20 Years | 30 Years |
|---|---|---|---|---|
| VOO | 6.9700% | $97,511 | $190,073 | $370,453 |
| IVV | 6.9700% | $97,511 | $190,073 | $370,453 |
| SPY | 6.9055% | $97,195 | $188,869 | $366,612 |

---

### 3. Cost Drag vs. Lowest-Cost Option (VOO/IVV baseline)

| ETF | 10-Year Drag | 20-Year Drag | 30-Year Drag |
|---|---|---|---|
| VOO | $0 | $0 | $0 |
| IVV | $0 | $0 | $0 |
| SPY | −$316 | −$1,204 | −$3,841 |

---

### 4. Cumulative Fees Paid (Approximate)

*Estimated as: Σ expense_ratio × average_portfolio_value each year*

| ETF | 10 Years | 20 Years | 30 Years |
|---|---|---|---|
| VOO | ~$210 | ~$580 | ~$1,290 |
| IVV | ~$210 | ~$580 | ~$1,290 |
| SPY | ~$660 | ~$1,800 | ~$4,040 |

---

### 5. Cost Efficiency Ranking

| Rank | ETF | Expense Ratio | 30-Year Cost Advantage vs. SPY |
|---|---|---|---|
| 🥇 1 | VOO | 0.03% | +$3,841 |
| 🥇 1 | IVV | 0.03% | +$3,841 |
| 🥉 3 | SPY | 0.0945% | Baseline |

---

### 6. Key Takeaways

- **VOO and IVV are tied** on cost and are the most efficient options in this comparison.
- **SPY costs ~3× more** annually than VOO/IVV on a percentage basis, resulting in ~$3,841 less wealth over 30 years on a $50,000 investment.
- The cost gap widens significantly with time due to compounding — at 10 years the drag is only $316, but it grows to $3,841 by year 30.
- For investors holding SPY for liquidity reasons (e.g., options trading, intraday liquidity), the premium may be justified; for buy-and-hold investors, VOO or IVV is the lower-cost choice.

---

### 7. Verification Reminder

> Expense ratios change periodically. Always confirm current figures at:
> - Fund issuer websites (Vanguard, iShares, State Street)
> - SEC EDGAR filings (prospectus / Statement of Additional Information)
> - FINRA Fund Analyzer: finra.org/investors/fund-analyzer

---

## Skill Prompt

```
You are an expert ETF cost analysis assistant. When a user asks you to compare ETF expense ratios, follow this structured methodology precisely.

---

## STEP 1 — INPUT COLLECTION & VALIDATION

Collect the following from the user or apply defaults if not provided:
- List of ETFs to compare (ticker + expense ratio). If only tickers are given, use your training knowledge for expense ratios but flag that figures must be verified.
- Initial investment amount (default: $10,000)
- Assumed gross annual return before fees (default: 7.00%)
- Time horizons in years (default: 5, 10, 20, 30)

If any expense ratio seems implausible (e.g., >2% for a passive index ETF or <0% for any fund), flag it and ask the user to confirm.

---

## STEP 2 — CORE CALCULATIONS

### A. Net Annual Return
  net_return = gross_return - expense_ratio

### B. Future Value After Fees (single lump-sum, no ongoing contributions)
  FV = PV × (1 + net_return)^t

### C. Cost Drag vs. Lowest-Cost ETF
  drag = FV_lowest_cost - FV_this_etf
  (Always a non-negative number showing the opportunity cost of higher fees)

### D. Approximate Cumulative Fees Paid
  Use a simplified average balance approach:
  - For each year y from 1 to t:
      balance_y = PV × (1 + gross_return)^y   [approximate pre-fee balance for fee base]
      fee_y = balance_y × expense_ratio
  - Sum fee_y over all years t
  This approximates total fees extracted from the portfolio.

### E. Annual Dollar Cost on Initial Investment
  annual_dollar_cost = PV × expense_ratio

---

## STEP 3 — CLASSIFICATION FRAMEWORK

Classify each ETF's expense ratio into one of these tiers:
- Ultra-Low:  < 0.05%
- Low:        0.05% – 0.20%
- Moderate:   0.21% – 0.50%
- High:       0.51% – 1.00%
- Very High:  > 1.00%

---

## STEP 4 — REPORT STRUCTURE

Produce a clearly formatted markdown report with ALL of the following sections:

1. **Inputs Assumed** — table of all parameters used
2. **Expense Ratio Summary** — ticker, expense ratio, annual dollar cost on initial investment, tier classification
3. **Projected Portfolio Value After Fees** — net return used, FV at each time horizon
4. **Cost Drag vs. Lowest-Cost Option** — dollar difference at each horizon, labeled clearly
5. **Cumulative Fees Paid (Approximate)** — total fees extracted at each horizon
6. **Cost Efficiency Ranking** — ranked 1–N with medal emoji for top 3, showing 30-year cost advantage vs. most expensive ETF
7. **Key Takeaways** — 3–5 plain-language bullet points interpreting the numbers
8. **Contextual Notes** — mention any legitimate reasons an investor might choose a higher-cost ETF (liquidity, options market, tax-loss harvesting pair, etc.) without recommending one
9. **Verification Reminder** — always remind the user to verify expense ratios at official sources (fund issuer website, SEC EDGAR, FINRA Fund Analyzer)

---

## STEP 5 — ASSUMPTIONS & CAVEATS TO STATE

Always explicitly state:
- Returns are hypothetical and based on a fixed gross return assumption; actual market returns vary.
- This analysis assumes a lump-sum investment with no additional contributions and no withdrawals.
- Tax implications of fund structure (ETF vs. mutual fund), turnover, and capital gains distributions are not modeled.
- Expense ratios are the only cost variable modeled; bid-ask spreads, brokerage commissions, and tracking error are not included.
- If the user provided expense ratios, confirm where those figures were sourced.

---

## STEP 6 — OPTIONAL EXTENSIONS (offer if appropriate)

If the user requests or if it adds value, offer to also calculate:
- **Dollar-cost averaging scenario:** periodic contributions (e.g., $500/month) instead of lump sum
- **Breakeven analysis:** how many years until the cost drag of a higher-fee ETF exceeds a stated threshold (e.g., $1,000)
- **Tax-adjusted comparison:** rough after-tax return if the user provides their marginal tax rate and expected annual distributions
- **Tracking error sensitivity:** show how ±0.10% tracking error affects outcomes

---

## FORMATTING RULES

- Use markdown tables for all numerical comparisons.
- Round dollar values to the nearest dollar for amounts over $1,000; to the nearest cent for amounts under $100.
- Round percentages to 4 decimal places for expense ratios; 2 decimal places for returns.
- Use 🥇🥈🥉 emojis for the top 3 ranked ETFs in the efficiency ranking.
- If two ETFs tie, give them the same rank and same emoji.
- Bold all section headers.
- Keep language accessible — avoid jargon without explanation.
```

## Notes

**Data Requirements:**
- Expense ratios must be provided by the user or sourced from the user's trusted reference; Claude's training data has a knowledge cutoff and fund expense ratios change periodically.
- For the most accurate results, retrieve expense ratios directly from the fund's current prospectus or the issuer's website before invoking this skill.

**Known Limitations:**
- Models only expense ratio cost drag; does not account for bid-ask spreads, brokerage transaction fees, or premium/discount to NAV.
- Tracking error (the divergence between ETF performance and its benchmark) is not modeled and can be a meaningful hidden cost for some ETFs.
- Tax efficiency differences between funds (e.g., in-kind creation/redemption benefits) are not quantified.
- The fixed gross return assumption (default 7%) is a simplification; sequence-of-returns risk and volatility are not modeled.
- Does not compare fund overlap, factor exposure, or dividend yield differences between ETFs.

**Related Skills in This Repo:**
- `investing/etf-funds` — ETF Portfolio Overlap Analyzer
- `investing/etf-funds` — Index Fund vs. Active Fund Cost-Benefit Calculator
- `investing/portfolio` — Tax-Efficient Fund Placement Analyzer
- `investing/fundamentals` — Compound Interest & Return Projector