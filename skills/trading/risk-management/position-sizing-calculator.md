---
name: Position Sizing Calculator
description: Calculate optimal trade position size using risk-based methods (fixed dollar risk, Kelly Criterion, volatility-adjusted)
category: trading/risk-management
tags: [position-sizing, risk-management, kelly-criterion, trading, portfolio-risk]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---

## Description

Computes trade position sizes using three industry-standard methods: Fixed Dollar Risk (1–2% rule), Kelly Criterion, and Volatility-Adjusted sizing (ATR-based). Presents all three results side-by-side so traders can choose the method that fits their risk tolerance and strategy.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Trading involves substantial risk of loss.
> Always consult a qualified financial professional before making trading decisions.

## Usage

Provide your account details and trade setup:
- Total account equity
- Maximum risk per trade (% or dollar amount)
- Entry price
- Stop-loss price
- (Optional for Kelly) Historical win rate and average win/loss ratio
- (Optional for ATR sizing) Current ATR value and ATR multiplier for stop

## Example

**Input:**
```
Account equity: $50,000
Max risk per trade: 2% ($1,000)
Entry price: $150.00
Stop-loss price: $144.00
Win rate (historical): 55%
Avg win / Avg loss ratio: 1.8
ATR (14-day): $3.50
ATR stop multiplier: 2x
```

**Output:**
```
=== Position Sizing Calculator ===

Trade Setup
  Entry:      $150.00
  Stop-Loss:  $144.00
  Risk/Share: $6.00

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

METHOD 1: Fixed Dollar Risk (2% Rule)
  Max dollar risk:    $1,000
  Shares to buy:      166 shares  ($1,000 / $6.00)
  Position value:     $24,900
  Portfolio exposure: 49.8%

METHOD 2: Kelly Criterion
  Kelly % = W − (1−W)/R = 0.55 − (0.45/1.8) = 30.0%
  Half-Kelly (recommended): 15.0%
  Dollar amount:      $7,500
  Shares to buy:      50 shares
  Position value:     $7,500
  Portfolio exposure: 15.0%

METHOD 3: Volatility-Adjusted (ATR-Based)
  ATR stop distance: $7.00 (2 × $3.50)
  Shares to buy:     142 shares  ($1,000 / $7.00)
  Position value:    $21,300
  Portfolio exposure: 42.6%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATION
  Most conservative: Kelly Half (50 shares, 15% exposure)
  Balanced approach: ATR-based (142 shares, 42.6% exposure)
  Note: Fixed Dollar Risk and ATR methods both stay within your 2% risk limit.
  Kelly suggests significantly smaller size — consistent with uncertain edge.
```

## Skill Prompt

```
You are a risk management specialist helping a trader size positions correctly.

Given the user's inputs, calculate position sizes using these three methods:

**METHOD 1: Fixed Dollar Risk**
- Risk per share = Entry Price − Stop-Loss Price
- Shares = Max Dollar Risk / Risk per Share
- Round down to whole shares
- Show: shares, position value, % of portfolio

**METHOD 2: Kelly Criterion**
- Full Kelly % = W − (1−W)/R
  where W = win rate (decimal), R = avg win / avg loss ratio
- Half-Kelly % = Full Kelly / 2 (standard recommendation to reduce variance)
- Dollar amount = Account Equity × Half-Kelly %
- Shares = Dollar Amount / Entry Price (round down)
- Show: Full Kelly %, Half-Kelly %, shares, position value, % of portfolio
- If win rate or R not provided, skip this method and note the missing input.

**METHOD 3: Volatility-Adjusted (ATR-Based)**
- ATR stop distance = ATR × ATR multiplier
- Shares = Max Dollar Risk / ATR stop distance
- Round down to whole shares
- Show: ATR stop distance, shares, position value, % of portfolio
- If ATR not provided, skip this method and note the missing input.

**SUMMARY**
- Present a side-by-side comparison table.
- Label which is most conservative and which is most aggressive.
- Flag if any method results in position exposure > 50% of portfolio (concentration risk warning).
- Note: If stop-loss is wider than ATR-based stop, the ATR method would imply fewer shares.

Keep math explicit and clearly formatted. Do not recommend a specific method — present trade-offs neutrally.
```

## Notes

- The 1–2% rule per trade is a widely cited risk management guideline for swing traders; day traders may use tighter limits (0.25–0.5%).
- Full Kelly often implies an uncomfortably large position size; Half-Kelly or Quarter-Kelly is standard practice.
- ATR-based sizing links stop placement to actual market volatility, making it adaptive across different instruments.
- This skill calculates size in shares (equities). For futures/forex, position sizing uses contract multipliers — adapt accordingly.
- Related skills: `skills/trading/quantitative/`, `skills/trading/backtesting/`.
