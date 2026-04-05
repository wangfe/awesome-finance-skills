---
name: Bond Yield and Duration Calculator
description: Calculates yield-to-maturity, Macaulay duration, modified duration, and convexity for fixed-income securities given bond parameters.
category: tools-and-utilities/calculators
tags: [bonds, yield-to-maturity, duration, fixed-income]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-04-05
---

## Description

This skill computes key fixed-income metrics — yield-to-maturity (YTM), Macaulay duration, modified duration, and convexity — for a bond given its face value, coupon rate, current price, maturity, and payment frequency. It is designed for fixed-income analysts, portfolio managers, students, and individual investors who need a rigorous, step-by-step breakdown of bond valuation and interest-rate sensitivity. The skill outputs all intermediate calculations alongside final figures, making it suitable both for quick lookups and for learning purposes. It also provides a plain-language interpretation of what each metric means for price risk.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke the skill by providing the following bond parameters in any natural-language format:

- **Face value (par):** e.g., $1,000
- **Annual coupon rate:** e.g., 6%
- **Current market price:** e.g., $950
- **Years to maturity:** e.g., 10 years
- **Coupon frequency:** annual, semi-annual, or quarterly (default: semi-annual)
- *(Optional)* **Settlement date / last coupon date** for accrued-interest calculations

The skill will confirm the inputs, display the full calculation walkthrough, and present a results table.

## Example

**Input:**
```
Calculate bond metrics for a bond with face value $1,000, annual coupon rate 5%, current price $920, 8 years to maturity, semi-annual coupons.
```

**Output:**

```
═══════════════════════════════════════════════════════
         BOND YIELD & DURATION CALCULATOR
═══════════════════════════════════════════════════════

INPUT SUMMARY
─────────────────────────────────────────────────────
Face Value (F):          $1,000.00
Annual Coupon Rate:       5.00%
Coupon Frequency:         Semi-annual (m = 2)
Periodic Coupon (C):     $25.00   (= 1000 × 5% / 2)
Current Price (P):        $920.00
Years to Maturity (n):    8 years
Total Periods (N):        16

─────────────────────────────────────────────────────
STEP 1 — YIELD TO MATURITY (YTM)
─────────────────────────────────────────────────────
YTM is the discount rate r that satisfies:

  P = Σ [C / (1+r)^t] + F / (1+r)^N
        t=1 to N

Solving numerically (Newton-Raphson iteration):

  Initial estimate (approximation method):
    r_approx = [C + (F−P)/N] / [(F+P)/2]
             = [25 + (1000−920)/16] / [(1000+920)/2]
             = [25 + 5.00] / [960]
             = 30.00 / 960 = 3.125% per period

  Iterative refinement:
    Iteration 1: r = 3.125% → P_calc = $924.18  (Δ = +$4.18)
    Iteration 2: r = 3.238% → P_calc = $920.43  (Δ = +$0.43)
    Iteration 3: r = 3.249% → P_calc = $920.02  (Δ = +$0.02)
    Iteration 4: r = 3.250% → P_calc = $920.00  ✓ Converged

  Periodic YTM (r):         3.250% per period
  ┌─────────────────────────────────────────────┐
  │  Annual YTM (BEY):  6.50%  (= r × 2)        │
  │  Effective Annual:  6.606% (= (1+r)² − 1)   │
  └─────────────────────────────────────────────┘

─────────────────────────────────────────────────────
STEP 2 — CASH FLOW SCHEDULE & PV WEIGHTS
─────────────────────────────────────────────────────
  Period  Cash Flow   Discount Factor   PV(CF)    t×PV(CF)
  ──────  ─────────   ───────────────   ───────   ────────
     1      $25.00        0.96851        $24.21     $24.21
     2      $25.00        0.93798        $23.45     $46.90
     3      $25.00        0.90841        $22.71     $68.13
     4      $25.00        0.87976        $21.99     $87.97
     5      $25.00        0.85201        $21.30    $106.50
     6      $25.00        0.82513        $20.63    $123.78
     7      $25.00        0.79908        $19.98    $139.83
     8      $25.00        0.77384        $19.35    $154.77
     9      $25.00        0.74939        $18.73    $168.60
    10      $25.00        0.72569        $18.14    $181.43
    11      $25.00        0.70272        $17.57    $193.24
    12      $25.00        0.68044        $17.01    $204.12
    13      $25.00        0.65884        $16.47    $214.12
    14      $25.00        0.63789        $15.95    $223.26
    15      $25.00        0.61757        $15.44    $231.60
    16   $1,025.00        0.59784       $612.79  $9,804.64
  ──────  ─────────                    ───────  ─────────
  TOTAL                                $920.00  $12,073.11

─────────────────────────────────────────────────────
STEP 3 — MACAULAY DURATION
─────────────────────────────────────────────────────
  Macaulay Duration (periods) = Σ[t × PV(CF)] / P
                               = 12,073.11 / 920.00
                               = 13.123 periods

  ┌──────────────────────────────────────────────────┐
  │  Macaulay Duration: 13.123 periods               │
  │                      6.561 years (÷ 2)           │
  └──────────────────────────────────────────────────┘

─────────────────────────────────────────────────────
STEP 4 — MODIFIED DURATION
─────────────────────────────────────────────────────
  Modified Duration = Macaulay Duration / (1 + r)
                    = 13.123 / (1 + 0.03250)
                    = 13.123 / 1.03250

  ┌──────────────────────────────────────────────────┐
  │  Modified Duration: 12.711 periods               │
  │                      6.356 years                 │
  └──────────────────────────────────────────────────┘

  Interpretation: For a 100 bps (1%) rise in YTM,
  the bond price is expected to fall by ≈ 6.356%.

  Price Change Approximation (Duration only):
    ΔP ≈ −ModDur × ΔYield × P
    ΔP ≈ −6.356 × 0.01 × $920 = −$58.47

─────────────────────────────────────────────────────
STEP 5 — CONVEXITY
─────────────────────────────────────────────────────
  Convexity = [Σ t(t+1) × PV(CF)] / [P × (1+r)²]

  Numerator = Σ t(t+1) × PV(CF_t):
    Period-by-period sum ≈ 369,842.50

  Convexity (periods²) = 369,842.50 / (920.00 × 1.06606)
                       = 369,842.50 / 980.77
                       = 377.11 periods²

  ┌──────────────────────────────────────────────────┐
  │  Convexity: 377.11 periods²                      │
  │              94.28 years²  (÷ m²= ÷4)            │
  └──────────────────────────────────────────────────┘

  Full Price Change with Convexity Adjustment:
    ΔP ≈ [−ModDur × Δy + ½ × Convexity × Δy²] × P
    For Δy = +1% (+0.01):
      ΔP ≈ [−6.356×0.01 + 0.5×94.28×0.0001] × $920
          ≈ [−0.06356 + 0.00471] × $920
          ≈ −0.05885 × $920
          ≈ −$54.14

═══════════════════════════════════════════════════════
                   RESULTS SUMMARY
═══════════════════════════════════════════════════════

  Metric                       Value
  ─────────────────────────    ──────────────
  Current Price                $920.00
  Yield to Maturity (BEY)      6.500%
  Effective Annual Yield       6.606%
  Current Yield                5.435%  (coupon/price)
  Macaulay Duration            6.561 years
  Modified Duration            6.356 years
  Convexity                   94.28 years²
  Dollar Duration (DV01)       $0.5847 per bp
  Price at +100bps (approx.)  $865.86  (duration only)
  Price at +100bps (adjusted)  $865.86  (with convexity)

─────────────────────────────────────────────────────
INTEREST RATE SENSITIVITY SCENARIOS
─────────────────────────────────────────────────────
  Yield Change   Duration-Only ΔP   Convexity-Adj ΔP   New Price
  ───────────    ────────────────   ────────────────   ─────────
    −200 bps         +$116.94           +$127.68        $1,047.68
    −100 bps          +$58.47            +$62.55          $982.55
     −50 bps          +$29.24            +$31.06          $951.06
      +50 bps         −$29.24            −$28.42          $891.58
    +100 bps          −$58.47            −$54.14          $865.86
    +200 bps         −$116.94           −$103.56          $816.44

─────────────────────────────────────────────────────
PLAIN-LANGUAGE INTERPRETATION
─────────────────────────────────────────────────────
  • The bond trades at a DISCOUNT ($920 < $1,000 par), so its
    YTM (6.50%) exceeds its coupon rate (5.00%).

  • A modified duration of 6.36 years means the bond has
    moderate interest-rate sensitivity — roughly comparable
    to a 6-year zero-coupon bond in terms of price risk.

  • Convexity of 94.28 is positive (as expected for a standard
    bullet bond), which means price gains from falling rates
    exceed price losses from rising rates by a small margin.

  • DV01 of $0.585 means a 1 basis-point increase in yield
    costs roughly $0.59 in bond price per $1,000 face value.
═══════════════════════════════════════════════════════
```

## Skill Prompt

```
You are a fixed-income analyst and educator. When the user provides bond parameters,
perform a complete bond yield and duration analysis following every step below with
precision, transparency, and clear labeling.

══════════════════════════════════════════════════════════════════
INPUTS TO COLLECT (ask for missing ones before proceeding)
══════════════════════════════════════════════════════════════════
1. Face value F (default: $1,000)
2. Annual coupon rate c (as a percentage)
3. Current market price P (clean price; ask if accrued interest applies)
4. Years to maturity T
5. Coupon frequency m: 1 = annual, 2 = semi-annual (default), 4 = quarterly
6. (Optional) Whether to show a full cash-flow schedule table

Derived inputs:
  N = T × m           (total coupon periods)
  C = F × c / m       (periodic coupon payment)

══════════════════════════════════════════════════════════════════
STEP 1 — YIELD TO MATURITY (YTM)
══════════════════════════════════════════════════════════════════
Solve for the periodic rate r such that:

  P = Σ_{t=1}^{N} [ C / (1+r)^t ] + F / (1+r)^N

METHOD: Use Newton-Raphson iteration.

  a) Compute initial estimate using the approximation formula:
       r_0 = [C + (F − P)/N] / [(F + P)/2]

  b) Iterate:
       r_{n+1} = r_n − f(r_n)/f'(r_n)
     where f(r) = P − Σ[C/(1+r)^t] − F/(1+r)^N
     and   f'(r) = Σ[t·C/(1+r)^{t+1}] + N·F/(1+r)^{N+1}

  c) Show at least 4 iterations with calculated price at each r.
     Stop when |P_calc − P| < $0.01.

  d) Report:
     - Periodic YTM: r
     - Bond Equivalent Yield (BEY):   r × m
     - Effective Annual Yield (EAY):  (1 + r)^m − 1
     - Current Yield: (C × m) / P

══════════════════════════════════════════════════════════════════
STEP 2 — CASH FLOW SCHEDULE & PRESENT VALUE WEIGHTS
══════════════════════════════════════════════════════════════════
Build a table with columns:
  Period t | Cash Flow CF_t | Discount Factor 1/(1+r)^t | PV(CF_t) | t × PV(CF_t)

  CF_t = C for t = 1 to N−1
  CF_N = C + F

Sum columns: verify Σ PV(CF_t) = P (within rounding tolerance ±$0.02)

══════════════════════════════════════════════════════════════════
STEP 3 — MACAULAY DURATION
══════════════════════════════════════════════════════════════════
  MacD_periods = Σ_{t=1}^{N} [ t × PV(CF_t) ] / P
  MacD_years   = MacD_periods / m

Report both. Interpret as: "the weighted-average time (in years)
until the bondholder receives the bond's cash flows."

══════════════════════════════════════════════════════════════════
STEP 4 — MODIFIED DURATION
══════════════════════════════════════════════════════════════