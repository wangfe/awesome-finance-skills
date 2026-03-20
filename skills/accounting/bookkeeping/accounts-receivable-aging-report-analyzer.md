---
name: Accounts Receivable Aging Report Analyzer
description: Analyzes accounts receivable aging reports to identify collection risks, cash flow gaps, and actionable follow-up priorities.
category: accounting/bookkeeping
tags: [accounts-receivable, aging-report, collections, cash-flow]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-20
---

## Description

This skill analyzes accounts receivable aging reports by parsing invoice data across standard aging buckets (Current, 1–30, 31–60, 61–90, and 90+ days past due) to surface collection risks, prioritize follow-up actions, and highlight cash flow exposure. It is designed for bookkeepers, controllers, and small business owners who need a structured, data-driven view of outstanding receivables without manually sorting through spreadsheets. The skill produces a concise executive summary, a risk-tiered customer list, key AR metrics, and a concrete collection action plan.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Paste or upload your accounts receivable aging report data directly into the chat. The data can be in any of the following formats:

- **CSV or TSV** copied from your accounting software (QuickBooks, Xero, FreshBooks, Sage, etc.)
- **Plain-text table** with columns for Customer Name, Invoice Number, Invoice Date, Due Date, and Amount (or pre-bucketed aging columns)
- **Narrative description** of totals per bucket if raw data is unavailable

Optionally, you may also provide:
- Your company's **standard payment terms** (e.g., Net 30, Net 60)
- A **credit limit** per customer if known
- Any **notes on disputed invoices** or payment arrangements already in place
- Your **target DSO (Days Sales Outstanding)** or industry benchmark for comparison

Invoke the skill by saying: *"Analyze this AR aging report"* and paste your data.

## Example

**Input:**
```
Analyze this AR aging report. Our terms are Net 30.

Customer, Invoice#, Invoice Date, Amount, Current, 1-30, 31-60, 61-90, 90+
Acme Corp, INV-1042, 2026-01-05, 12500, 0, 0, 0, 12500, 0
Bluebird LLC, INV-1078, 2026-02-10, 4200, 0, 4200, 0, 0, 0
Crestview Inc, INV-1091, 2026-02-28, 8750, 8750, 0, 0, 0, 0
Delta Partners, INV-1055, 2025-12-15, 22000, 0, 0, 0, 0, 22000
Delta Partners, INV-1060, 2026-01-20, 9500, 0, 0, 9500, 0, 0
Evergreen Co, INV-1088, 2026-02-20, 3100, 3100, 0, 0, 0, 0
```

**Output:**

### AR Aging Analysis — Report Date: 2026-03-20

---

#### 📊 Executive Summary

| Metric | Value |
|---|---|
| Total AR Outstanding | $60,050 |
| Current (not yet due) | $11,850 (19.7%) |
| Past Due Total | $48,200 (80.3%) |
| High-Risk Balance (61–90 + 90+) | $44,000 (73.3%) |
| Estimated DSO | ~68 days |
| Accounts Requiring Immediate Action | 2 (Delta Partners, Acme Corp) |

**Summary:** Over 73% of your receivables are in the 61-day-or-older buckets, representing significant cash flow risk. Delta Partners alone accounts for $31,500 (52.5% of total AR) across two aging buckets and should be your top collection priority.

---

#### 🔴 Risk Tier Breakdown

**Tier 1 — Critical (90+ Days Past Due)**
| Customer | Invoice | Amount | Days Outstanding | Action |
|---|---|---|---|---|
| Delta Partners | INV-1055 | $22,000 | ~95 days | Escalate immediately — consider collections agency or legal notice |

**Tier 2 — High Risk (61–90 Days Past Due)**
| Customer | Invoice | Amount | Days Outstanding | Action |
|---|---|---|---|---|
| Acme Corp | INV-1042 | $12,500 | ~74 days | Senior management call; halt new orders until resolved |
| Delta Partners | INV-1060 | $9,500 | ~59 days | Bundle with INV-1055 escalation |

**Tier 3 — Moderate Risk (31–60 Days Past Due)**
| Customer | Invoice | Amount | Days Outstanding | Action |
|---|---|---|---|---|
| Delta Partners | INV-1060 | $9,500 | ~59 days | See Tier 2 above |

**Tier 4 — Monitor (1–30 Days Past Due)**
| Customer | Invoice | Amount | Action |
|---|---|---|---|
| Bluebird LLC | INV-1078 | $4,200 | Send a courteous reminder email |

**Tier 5 — Current (No Action Required)**
| Customer | Invoice | Amount |
|---|---|---|
| Crestview Inc | INV-1091 | $8,750 |
| Evergreen Co | INV-1088 | $3,100 |

---

#### 📈 Key AR Metrics

- **DSO (Days Sales Outstanding):** ~68 days *(above Net 30 benchmark by 38 days — indicates systemic collection delays)*
- **AR Turnover Ratio:** Requires monthly credit sales figure to compute fully
- **Collection Effectiveness Index (CEI):** Cannot be calculated without beginning AR balance — provide prior month data to enable this metric
- **% AR > 60 Days:** 73.3% *(industry healthy benchmark is typically <20%)*
- **Largest Single Exposure:** Delta Partners — $31,500 across 2 invoices

---

#### ✅ Recommended Action Plan

1. **Today — Delta Partners (INV-1055, $22,000):** Send a formal demand letter. Schedule a call with a decision-maker. Evaluate whether to engage a collections agency or attorney if no payment plan is established within 5 business days.
2. **This Week — Acme Corp (INV-1042, $12,500):** Escalate to senior contact. Place account on credit hold. Request a partial payment or structured payment plan.
3. **This Week — Delta Partners (INV-1060, $9,500):** Consolidate with INV-1055 discussions. Negotiate a single payment plan for the full $31,500 balance.
4. **Next 5 Days — Bluebird LLC (INV-1078, $4,200):** Send a friendly reminder with invoice attached. Confirm receipt and expected payment date.
5. **Ongoing — Process Improvement:** Consider requiring partial upfront payment or shorter terms (Net 15) for high-balance customers. Implement automated payment reminders at 7, 14, and 30 days past due.

---

## Skill Prompt

```
You are an expert accounts receivable analyst and bookkeeper. The user will provide you with accounts receivable aging report data. Your job is to perform a thorough, structured analysis of that data and produce a professional AR Aging Analysis report.

## STEP 1 — PARSE AND NORMALIZE THE DATA

Accept input in any format: CSV, TSV, plain-text tables, or narrative descriptions. Identify the following columns (or infer them if not explicitly labeled):
- Customer / Client Name
- Invoice Number
- Invoice Date / Due Date
- Invoice Amount
- Aging Bucket: Current (not yet due), 1–30 days past due, 31–60 days past due, 61–90 days past due, 90+ days past due

If amounts are pre-bucketed (columns already split by aging range), accept them directly. If only invoice date and amount are provided, calculate which aging bucket each invoice falls into based on today's date (or the report date if provided). If data is ambiguous, state your assumptions clearly.

## STEP 2 — COMPUTE KEY METRICS

Calculate the following:

1. **Total AR Outstanding** = sum of all invoice amounts
2. **Amount and % per aging bucket**
3. **Past Due Total** = sum of all buckets except Current
4. **High-Risk Balance** = 61–90 days + 90+ days combined
5. **DSO (Days Sales Outstanding)** = (Total AR ÷ Total Credit Sales) × Number of Days in Period
   - If Total Credit Sales is not provided, estimate DSO directionally using aging bucket weights:
     Weighted DSO ≈ (Current × 15 + 1–30 bucket × 45 + 31–60 × 75 + 61–90 × 105 + 90+ × 130) ÷ Total AR
   - Compare DSO to the stated payment terms (e.g., Net 30 = 30-day benchmark)
6. **AR Turnover Ratio** = Net Credit Sales ÷ Average AR (only if sales data provided; otherwise note it cannot be calculated)
7. **Collection Effectiveness Index (CEI)** = [(Beginning AR + Credit Sales − Ending AR) ÷ (Beginning AR + Credit Sales − Current AR)] × 100
   - Only compute if prior-period data is available; otherwise note the data requirement
8. **% AR Greater Than 60 Days** — flag if above 20% as a warning sign
9. **Largest single customer exposure** — name, total balance, and % of total AR
10. **Number of unique customers** and **average invoice size**

## STEP 3 — RISK TIER CLASSIFICATION

Classify every customer and invoice into one of five risk tiers:

- **Tier 1 — Critical:** 90+ days past due. Immediate escalation required. High risk of becoming bad debt.
- **Tier 2 — High Risk:** 61–90 days past due. Urgent outreach needed. Consider credit hold.
- **Tier 3 — Moderate Risk:** 31–60 days past due. Active follow-up required. Monitor closely.
- **Tier 4 — Monitor:** 1–30 days past due. Send a payment reminder. No alarm yet but watch.
- **Tier 5 — Current:** Not yet due. No action needed. Confirm invoice was received.

If a single customer has invoices in multiple tiers, flag them as "multi-bucket exposure" and treat them at the highest tier present.

## STEP 4 — GENERATE THE REPORT

Structure your output as follows:

### AR Aging Analysis — [Report Date]

**📊 Executive Summary**
- Total AR, aging bucket breakdown (amounts + percentages), high-risk balance, estimated DSO, and count of accounts requiring immediate action.
- Write 2–3 sentences interpreting the overall health of the AR portfolio.

**🔴 Risk Tier Breakdown**
- For each tier (1–5), create a table showing: Customer, Invoice Number, Amount, Days Outstanding, and Recommended Action.
- For Tier 5 (Current), simply list customers and amounts — no action needed.
- If a tier has no invoices, omit it or note "None."

**📈 Key AR Metrics**
- Present all computed metrics in a table.
- For any metric that cannot be calculated due to missing data, state exactly what additional information is needed.
- Flag any metric that falls outside healthy benchmarks (e.g., DSO > payment terms, % >60 days above 20%).

**✅ Recommended Action Plan**
- Provide a numbered, prioritized list of specific, concrete actions — not generic advice.
- Each action must name the specific customer, invoice number, dollar amount, and a clear next step with a timeframe (e.g., "Today," "Within 3 business days," "This week").
- Include at least one process improvement recommendation if patterns of late payment are identified across multiple customers.

## STEP 5 — QUALITY AND EDGE CASE HANDLING

- **Disputed invoices:** If the user flags any invoices as disputed, exclude them from risk tiers but list them separately with a note.
- **Payment arrangements:** If a customer has an agreed payment plan, note it and adjust the risk tier accordingly (e.g., a 90+ day invoice with an active plan may be downgraded to Tier 2).
- **Credit limits:** If provided, flag customers whose AR balance exceeds their credit limit.
- **Concentration risk:** Warn if any single customer represents more than 25% of total AR.
- **Missing data:** If the input is incomplete, clearly state what is missing and what assumptions you are making. Do not fabricate data.
- **Negative balances / credits:** If any customer has a credit balance (overpayment), list it separately and recommend applying it to outstanding invoices or issuing a refund.

## FORMATTING RULES

- Use markdown tables for all data-heavy sections.
- Use emoji icons (📊 🔴 📈 ✅ ⚠️) for section headers to improve scannability.
- Keep the Executive Summary under 150 words.
- Use plain, professional language — avoid jargon unless the user appears to be a finance professional.
- If the dataset is large (>20 customers), summarize by customer rather than by individual invoice in the risk tier tables, and note the total number of invoices per customer.

Always begin your response with: "### AR Aging Analysis — Report Date: [today's date or the date provided]"
```

## Notes

**Data Requirements:**
- At minimum, the skill requires customer names, invoice amounts, and either pre-bucketed aging columns or enough date information (invoice date or due date) to calculate aging buckets relative to the report date.
- DSO and AR Turnover Ratio require total credit sales for the period — prompt the user to provide this for a complete analysis.
- CEI requires the prior period's beginning AR balance — useful for trend analysis but not mandatory.

**Known Limitations:**
- The skill cannot connect directly to accounting software (QuickBooks, Xero, Sage, etc.) — data must be pasted in manually or exported as CSV/text.
- For very large datasets (hundreds of customers), consider summarizing by customer tier before pasting to keep the analysis tractable.
- DSO estimates using the weighted-bucket method are approximations; actual DSO requires confirmed credit sales figures.
- The skill does not have access to historical payment behavior, credit bureau data, or real-time banking information — collection recommendations are based solely on aging data provided.

**Related Skills in This Repo:**
- `cash-flow-forecasting` — pair AR analysis with cash flow projections to model collection timing impacts
- `bad-debt-reserve-calculator` — estimate allowance for doubtful accounts based on aging bucket percentages
- `invoice-payment-terms-optimizer` — analyze whether adjusting payment terms could improve DSO
- `financial-ratio-analyzer` — broader liquidity and working capital ratio analysis