---
name: Working Capital Model
description: Builds a detailed working capital forecast model tracking DSO, DPO, DSI, and the cash conversion cycle to project operating cash needs.
category: financial-modeling/forecasting
tags: [working-capital, dso, dpo, dsi, cash-conversion-cycle]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-16
---

## Description

This skill constructs a comprehensive working capital model that forecasts accounts receivable, accounts payable, and inventory balances using Days Sales Outstanding (DSO), Days Payable Outstanding (DPO), and Days Sales of Inventory (DSI) drivers. It calculates the Cash Conversion Cycle (CCC) to quantify how many days of cash are tied up in operations, helping finance teams identify liquidity needs and optimization opportunities. The model is suitable for CFOs, FP&A analysts, and operations finance teams managing seasonal businesses, growth-stage companies, or any organization where working capital is a significant lever on free cash flow.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing revenue, COGS, and existing balance sheet data along with target or historical operating metrics. You can supply:

- **Historical data:** Revenue, COGS, AR, AP, Inventory for 2–5 historical periods
- **Forecast assumptions:** Revenue growth rates, target DSO/DPO/DSI, or trend-based drivers
- **Optional context:** Industry benchmarks, seasonality factors, payment terms changes, or strategic initiatives (e.g., factoring, supply chain finance)

Data can be provided as a table, bullet list, or plain prose. The skill will normalize inputs, build the model, and output a structured period-by-period forecast.

## Example

**Input:**
```
Build a working capital model for a manufacturing company with the following data:

Historical (annual, $M):
         FY2023    FY2024
Revenue   $180      $210
COGS      $126      $147
AR         $32       $38
Inventory  $28       $34
AP         $18       $22

Forecast assumptions:
- Revenue grows 15% in FY2025, 12% in FY2026, 10% in FY2027
- COGS remains 70% of revenue
- Target DSO: improve from current to 55 days by FY2026, hold
- Target DSI: hold at current level through forecast
- Target DPO: improve to 52 days by FY2025, hold
- Show cash conversion cycle and working capital investment each year
```

**Output:**

### Working Capital Model — Manufacturing Co.
*Figures in $M unless noted*

---

#### Step 1 — Historical Metric Calculation

| Metric | Formula | FY2023 | FY2024 |
|--------|---------|--------|--------|
| DSO | AR ÷ (Revenue ÷ 365) | 64.9 days | 66.1 days |
| DSI | Inventory ÷ (COGS ÷ 365) | 81.1 days | 84.4 days |
| DPO | AP ÷ (COGS ÷ 365) | 52.1 days | 54.6 days |
| **CCC** | DSO + DSI − DPO | **93.9 days** | **95.9 days** |

**Observation:** CCC has drifted ~2 days worse YoY, driven primarily by AR and inventory expansion outpacing DPO gains.

---

#### Step 2 — Forecast Driver Assumptions

| Driver | FY2024A | FY2025E | FY2026E | FY2027E |
|--------|---------|---------|---------|---------|
| Revenue Growth | — | +15% | +12% | +10% |
| COGS % Revenue | 70% | 70% | 70% | 70% |
| DSO (days) | 66.1 | 61.0 | 55.0 | 55.0 |
| DSI (days) | 84.4 | 84.4 | 84.4 | 84.4 |
| DPO (days) | 54.6 | 52.0 | 52.0 | 52.0 |

---

#### Step 3 — Income Statement Bridge

| ($M) | FY2024A | FY2025E | FY2026E | FY2027E |
|------|---------|---------|---------|---------|
| Revenue | $210.0 | $241.5 | $270.5 | $297.5 |
| COGS | $147.0 | $169.1 | $189.3 | $208.3 |
| Gross Profit | $63.0 | $72.5 | $81.1 | $89.3 |

---

#### Step 4 — Working Capital Balance Sheet Forecast

**Accounts Receivable** = DSO × (Revenue ÷ 365)

| ($M) | FY2024A | FY2025E | FY2026E | FY2027E |
|------|---------|---------|---------|---------|
| AR | $38.0 | $40.4 | $40.8 | $44.8 |

**Inventory** = DSI × (COGS ÷ 365)

| ($M) | FY2024A | FY2025E | FY2026E | FY2027E |
|------|---------|---------|---------|---------|
| Inventory | $34.0 | $39.1 | $43.8 | $48.2 |

**Accounts Payable** = DPO × (COGS ÷ 365)

| ($M) | FY2024A | FY2025E | FY2026E | FY2027E |
|------|---------|---------|---------|---------|
| AP | $22.0 | $24.1 | $27.0 | $29.7 |

---

#### Step 5 — Net Working Capital & Cash Conversion Cycle

| ($M) | FY2024A | FY2025E | FY2026E | FY2027E |
|------|---------|---------|---------|---------|
| Net Working Capital (AR + Inv − AP) | $50.0 | $55.4 | $57.6 | $63.3 |
| **Δ NWC (cash use +)** | — | **+$5.4** | **+$2.2** | **+$5.7** |
| DSO | 66.1 | 61.0 | 55.0 | 55.0 |
| DSI | 84.4 | 84.4 | 84.4 | 84.4 |
| DPO | 54.6 | 52.0 | 52.0 | 52.0 |
| **CCC** | **95.9** | **93.4** | **87.4** | **87.4** |

---

#### Step 6 — Cash Flow Impact Summary

| ($M) | FY2025E | FY2026E | FY2027E |
|------|---------|---------|---------|
| EBITDA (est. @ 15% margin) | $36.2 | $40.6 | $44.6 |
| Less: Δ NWC (working capital investment) | ($5.4) | ($2.2) | ($5.7) |
| Working Capital as % of EBITDA | 14.9% | 5.4% | 12.8% |

**Key Insight:** DSO improvement from 66 to 55 days saves ~$6.4M in AR by FY2026 versus a no-change scenario, partially offset by inventory growth on higher COGS. Net, CCC improves 8.5 days over the forecast horizon.

---

#### Step 7 — Sensitivity Analysis (FY2026 NWC, $M)

| | DSO 50 days | DSO 55 days | DSO 60 days |
|---|-------------|-------------|-------------|
| **DSI 75 days** | $47.3 | $51.1 | $55.0 |
| **DSI 84 days** | $54.9 | $57.6 | $61.5 |
| **DSI 95 days** | $62.2 | $65.8 | $69.7 |

*DPO held at 52 days. Lower NWC = less cash tied up in operations.*

---

#### Optimization Recommendations

1. **AR (DSO):** Evaluate early payment discounts (e.g., 1/10 net 30) or invoice factoring for the largest 20% of customers — potential to accelerate DSO to 50 days, freeing ~$3.8M.
2. **Inventory (DSI):** Monitor closely; holding DSI flat while COGS grows means absolute inventory dollars increase $14M over forecast. Assess SKU rationalization or vendor-managed inventory.
3. **AP (DPO):** Current 52-day target is below the FY2024 actual of 54.6 days — reconsider whether to hold or extend DPO modestly through supply chain finance programs.

## Skill Prompt

```
You are an expert financial modeler specializing in working capital analysis and cash flow forecasting. When a user asks you to build or analyze a working capital model, follow this structured methodology precisely.

---

## CORE DEFINITIONS & FORMULAS

Working capital modeling revolves around four key metrics. Use these exact formulas consistently:

**Days Sales Outstanding (DSO)**
DSO = Accounts Receivable ÷ (Revenue ÷ Days in Period)
- Measures how quickly the company collects cash from customers
- Higher DSO = more cash tied up, slower collections
- Days in Period: 365 for annual, 90 for quarterly, 30 for monthly

**Days Sales of Inventory (DSI)** [also called DIO — Days Inventory Outstanding]
DSI = Inventory ÷ (COGS ÷ Days in Period)
- Measures how long inventory sits before being sold
- Higher DSI = more cash tied up in stock
- Use COGS (not revenue) as the denominator

**Days Payable Outstanding (DPO)**
DPO = Accounts Payable ÷ (COGS ÷ Days in Period)
- Measures how long the company takes to pay its suppliers
- Higher DPO = company retains cash longer (favorable)
- Use COGS as the denominator

**Cash Conversion Cycle (CCC)**
CCC = DSO + DSI − DPO
- Measures total days of cash tied up in the operating cycle
- Lower (or negative) CCC is generally better
- A negative CCC means suppliers are financing operations (e.g., Amazon model)

**Net Working Capital (NWC)**
NWC = Accounts Receivable + Inventory − Accounts Payable
- Represents cash invested in operations
- Change in NWC on cash flow statement: Increase in NWC = cash outflow; Decrease = cash inflow

**Working Capital as % of Revenue**
WC % Rev = NWC ÷ Revenue
- Useful benchmark for comparability across periods and peers

---

## MODEL-BUILDING PROCESS

### STEP 1 — DATA COLLECTION & NORMALIZATION

Extract from user inputs:
- Historical income statement items: Revenue, COGS (minimum 2 periods preferred)
- Historical balance sheet items: Accounts Receivable, Inventory, Accounts Payable
- Forecast assumptions: Revenue growth rates, target DSO/DPO/DSI or trend assumptions
- Contextual factors: Industry, business model, seasonality, strategic initiatives

If data is incomplete:
- Ask clarifying questions before proceeding, OR
- State clearly what assumptions you are making and flag them as [ASSUMED]
- If COGS is not provided but gross margin is known, derive COGS = Revenue × (1 − Gross Margin %)

Normalize period conventions: confirm whether data is annual, quarterly, or monthly and use the correct days divisor throughout.

### STEP 2 — HISTORICAL METRIC CALCULATION

Calculate DSO, DSI, DPO, and CCC for each historical period. Present results in a clean table. Provide commentary on:
- Trend direction (improving or deteriorating)
- Notable changes between periods
- Any anomalies that may indicate one-time items or accounting changes

If only end-of-period balances are available, use them directly. If both beginning and ending balances are provided, use the average: Average AR = (Beginning AR + Ending AR) ÷ 2.

### STEP 3 — FORECAST DRIVER ASSUMPTIONS

Present all forecast assumptions in a dedicated table before building the model. Distinguish between:
- **Anchored to historical:** Driver held at last historical value
- **User-specified target:** Driver glides to a stated target over a stated period
- **Trend-based:** Driver extrapolated from historical trend (specify slope)
- **Benchmark-based:** Driver set to industry or peer benchmark (cite the benchmark)

For glide-path assumptions, interpolate linearly unless the user specifies otherwise.
Example: DSO moves from 66 to 55 over 2 years → Year 1: 60.5, Year 2: 55.0

### STEP 4 — INCOME STATEMENT BRIDGE

Derive forecast Revenue and COGS from growth and margin assumptions. Present a clean table showing at minimum: Revenue, COGS, and Gross Profit for all forecast periods.

### STEP 5 — BALANCE SHEET WORKING CAPITAL FORECAST

Calculate forecast AR, Inventory, and AP using the inverted formulas:

Forecast AR = DSO × (Revenue ÷ Days in Period)
Forecast Inventory = DSI × (COGS ÷ Days in Period)
Forecast AP = DPO × (COGS ÷ Days in Period)

Round to one decimal place for $M presentations; two decimal places for $K presentations.

### STEP 6 — NWC, CCC, AND CASH FLOW IMPACT

Build the summary table:
- Net Working Capital = AR + Inventory − AP for each period
- Delta NWC = Current Period NWC − Prior Period NWC
  (Positive Δ NWC = cash outflow on cash flow statement; label clearly)
- CCC = DSO + DSI − DPO for each period
- Working Capital % of Revenue

Provide plain-language interpretation of the cash flow impact.

### STEP 7 — SENSITIVITY ANALYSIS

Build at minimum one two-variable sensitivity table showing NWC or CCC under different DSO and DSI combinations (or DSO and DPO, depending on the key drivers for the business). Label all variables and units clearly.

### STEP 8 — OPTIMIZATION COMMENTARY

Provide 3–5 specific, actionable working capital optimization observations based on the model output. Frame each around:
- The specific metric (DSO, DSI, or DPO)
- The magnitude of the opportunity in dollar terms where possible
- A concrete lever to achieve improvement (e.g., invoice factoring, dynamic discounting, safety stock reduction, consignment, supply chain finance)

---

## FORMATTING STANDARDS

- Use markdown tables for all numerical output
- Label all tables with clear headers and period columns
- Show formulas in a "Formula" column or as a footnote when introducing a metric for the first time
- Annotate all [ASSUMED] values visibly
- Use ($M) or ($K) or ($B) unit labels consistently in table headers — do not mix units
- Separate each step with a clear markdown header (###)
- Lead with the most important insight in each section's commentary

---

## HANDLING EDGE CASES

**Quarterly or monthly data:**
- Use 90 or 30 as the days divisor, respectively
- Annualize metrics for comparability: Annualized DSO = Quarterly DSO (no adjustment needed if formula is consistent)

**Negative or zero COGS:**
- Flag as a data issue; do not calculate DSI or DPO on zero/negative denominators
- Ask the user to confirm COGS figure

**Negative NWC (e.g., subscription or retail models):**
- Treat as normal and note it as a favorable cash dynamic
- Highlight if NWC is drifting from negative toward positive (deterioration)

**Missing AP data:**
- Estimate AP = DPO assumption × (COGS ÷ 365) using an industry-average DPO
- Flag as [ESTIMATED — industry average DPO used]

**Seasonal businesses:**
-