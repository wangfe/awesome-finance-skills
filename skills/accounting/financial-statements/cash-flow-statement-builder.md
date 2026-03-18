---
name: Cash Flow Statement Builder
description: Builds a structured cash flow statement organized into operating, investing, and financing activities from raw transaction data or financial inputs.
category: accounting/financial-statements
tags: [cash-flow-statement, operating, investing, financing]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-03-18
---

## Description

This skill constructs a complete cash flow statement by organizing user-provided financial data into the three standard sections: operating activities, investing activities, and financing activities. It supports both the direct and indirect methods for presenting operating cash flows and calculates net changes in cash for a given period. Designed for accountants, CFOs, small business owners, and finance students, it produces a clearly formatted statement ready for review or reporting. The output includes subtotals for each section, a reconciliation of beginning and ending cash balances, and flags any anomalies or missing data.

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

Invoke this skill by providing financial data in any of the following forms:

- **Narrative description:** Describe your transactions or summarized line items in plain text.
- **Table or list:** Paste a list of amounts with labels (e.g., "Net Income: $120,000; Depreciation: $15,000").
- **Partial data:** Provide what you have; the skill will flag missing items and make reasonable assumptions where appropriate.

Specify:
1. The **reporting period** (e.g., "Year ended December 31, 2025").
2. The **method** preferred for operating activities: `direct` or `indirect` (defaults to indirect if not specified).
3. The **beginning cash balance** and **ending cash balance**, if known.
4. Any **currency** and **unit scale** (e.g., USD in thousands).

## Example

**Input:**
```
Build a cash flow statement for the year ended December 31, 2025 using the indirect method.
Currency: USD (in thousands)

Income Statement items:
- Net Income: $95,000
- Depreciation & Amortization: $18,500
- Gain on sale of equipment: $4,200

Balance Sheet changes:
- Accounts Receivable increased by $12,300
- Inventory decreased by $5,400
- Accounts Payable increased by $7,800
- Accrued Liabilities decreased by $2,100

Investing Activities:
- Purchased new machinery: $45,000
- Proceeds from sale of equipment: $9,500
- Purchased marketable securities: $10,000

Financing Activities:
- Repaid long-term debt: $20,000
- Issued common stock: $15,000
- Paid cash dividends: $8,500

Beginning Cash Balance: $22,400
```

**Output:**
```
════════════════════════════════════════════════════════════
         CASH FLOW STATEMENT (INDIRECT METHOD)
         For the Year Ended December 31, 2025
                   (USD in Thousands)
════════════════════════════════════════════════════════════

OPERATING ACTIVITIES
────────────────────────────────────────────────────────────
  Net Income                                      $95,000
  Adjustments to reconcile net income to
  net cash provided by operating activities:
    Depreciation & Amortization                   $18,500
    Gain on sale of equipment                     ($4,200)
  Changes in working capital:
    Accounts Receivable (increase)               ($12,300)
    Inventory (decrease)                           $5,400
    Accounts Payable (increase)                    $7,800
    Accrued Liabilities (decrease)                ($2,100)
────────────────────────────────────────────────────────────
  Net Cash Provided by Operating Activities      $108,100

INVESTING ACTIVITIES
────────────────────────────────────────────────────────────
  Purchase of machinery                          ($45,000)
  Proceeds from sale of equipment                  $9,500
  Purchase of marketable securities              ($10,000)
────────────────────────────────────────────────────────────
  Net Cash Used in Investing Activities          ($45,500)

FINANCING ACTIVITIES
────────────────────────────────────────────────────────────
  Repayment of long-term debt                   ($20,000)
  Proceeds from issuance of common stock         $15,000
  Cash dividends paid                            ($8,500)
────────────────────────────────────────────────────────────
  Net Cash Used in Financing Activities          ($13,500)

════════════════════════════════════════════════════════════
  Net Increase in Cash                            $49,100
  Beginning Cash Balance                         $22,400
────────────────────────────────────────────────────────────
  Ending Cash Balance                            $71,500
════════════════════════════════════════════════════════════

⚠ NOTES & FLAGS:
  • No ending cash balance was provided by the user.
    Calculated ending balance: $71,500. Please verify against
    your balance sheet.
  • Gain on sale of equipment ($4,200) is subtracted from
    operating activities and its full proceeds ($9,500)
    appear in investing activities to avoid double-counting.
  • Free Cash Flow (Operating − CapEx): $108,100 − $45,000
    = $63,100
```

## Skill Prompt

```
You are an expert accountant and financial statement preparer. When the user invokes the Cash Flow Statement Builder skill, follow these detailed instructions to produce an accurate, well-formatted cash flow statement.

────────────────────────────────────────────────────────────
STEP 1 — GATHER AND CLARIFY INPUTS
────────────────────────────────────────────────────────────
Before building the statement, identify the following from user input:
  a. Reporting period (e.g., "Year ended December 31, 2025")
  b. Presentation method: INDIRECT (default) or DIRECT for operating activities
  c. Currency and unit scale (e.g., USD, thousands, millions)
  d. Beginning and ending cash balances (request if not provided)
  e. All transaction data, categorized or uncategorized

If critical data is missing, make reasonable assumptions, clearly document them, and flag them with a ⚠ symbol in the output.

────────────────────────────────────────────────────────────
STEP 2 — CLASSIFY EACH ITEM INTO THE CORRECT SECTION
────────────────────────────────────────────────────────────
Apply the following classification rules strictly:

OPERATING ACTIVITIES — cash flows from primary business operations:
  Indirect Method:
    Start with Net Income (or Net Loss).
    Add back non-cash expenses: depreciation, amortization, impairment,
    stock-based compensation, deferred taxes.
    Remove non-operating gains (subtract) and losses (add).
    Adjust for changes in working capital:
      - Increase in current asset → cash outflow (subtract)
      - Decrease in current asset → cash inflow (add)
      - Increase in current liability → cash inflow (add)
      - Decrease in current liability → cash outflow (subtract)
  Direct Method:
    List actual cash receipts (from customers, interest received, etc.)
    and cash payments (to suppliers, employees, taxes paid, interest paid).

INVESTING ACTIVITIES — cash flows from acquisition/disposal of long-term assets:
  Cash outflows: purchase of PP&E, acquisitions, purchase of investments/securities
  Cash inflows: proceeds from asset sales, maturities of investments, loan collections
  Rule: Use gross proceeds from asset sales here; remove any related gain/loss from operating.

FINANCING ACTIVITIES — cash flows from debt and equity transactions:
  Cash inflows: issuance of stock, proceeds from borrowings, receipt of grants
  Cash outflows: repayment of debt, payment of dividends, share repurchases,
  payment of finance lease liabilities

CLASSIFICATION EDGE CASES:
  - Interest paid: Operating (US GAAP) or Financing (IFRS) — follow user's stated standard; default to US GAAP
  - Interest received: Operating (US GAAP) or Investing (IFRS)
  - Dividends paid: Financing (US GAAP) or Operating/Financing (IFRS)
  - Taxes: Operating, unless specifically identifiable with investing/financing
  - Non-cash transactions (e.g., stock-for-debt swap): Exclude from statement body;
    disclose in a supplemental schedule

────────────────────────────────────────────────────────────
STEP 3 — PERFORM CALCULATIONS
────────────────────────────────────────────────────────────
For each section, sum inflows and outflows:
  Net Cash from Operating Activities = Sum of all operating line items
  Net Cash from Investing Activities = Sum of all investing line items
  Net Cash from Financing Activities = Sum of all financing line items

  Net Change in Cash = Operating + Investing + Financing
  Ending Cash Balance = Beginning Cash Balance + Net Change in Cash

Validation check:
  If the user provided both beginning and ending cash balances, verify:
    Ending Balance − Beginning Balance = Net Change in Cash
  If there is a discrepancy, flag it prominently and ask the user to review.

Also calculate and display:
  Free Cash Flow (FCF) = Net Cash from Operating − Capital Expenditures
  Operating Cash Flow Ratio = Net Cash from Operating / Current Liabilities (if data available)

────────────────────────────────────────────────────────────
STEP 4 — FORMAT THE OUTPUT
────────────────────────────────────────────────────────────
Present the statement with clear visual hierarchy:
  - Use a header block with entity name (if given), statement title, period, and currency/unit
  - Separate each of the three sections with labeled dividers
  - Right-align all numeric values with consistent formatting
  - Show cash outflows as negative numbers in parentheses: ($X,XXX)
  - Show cash inflows as positive numbers: $X,XXX
  - Provide subtotals for each section clearly labeled
  - Show ending balance reconciliation at the bottom

After the main statement, include:
  ⚠ NOTES & FLAGS section covering:
    - Any assumptions made
    - Missing data that should be verified
    - Double-counting risks addressed (e.g., gains removed from operating)
    - Non-cash transactions disclosed separately if applicable
    - Supplemental disclosure: cash paid for interest and taxes (US GAAP requirement)
    - FCF calculation
    - Accounting standard applied (US GAAP or IFRS)

────────────────────────────────────────────────────────────
STEP 5 — QUALITY CHECKS
────────────────────────────────────────────────────────────
Before finalizing output, verify:
  □ Net income is the starting point for indirect method operating section
  □ Depreciation and amortization are added back (non-cash expense)
  □ Gains on asset sales are subtracted from operating; losses are added back
  □ Full proceeds from asset sales appear in investing activities
  □ Working capital changes follow the correct sign convention
  □ No item appears in more than one section
  □ Non-cash transactions are excluded from the body of the statement
  □ Ending cash balance reconciles with beginning balance + net change
  □ All line items are clearly labeled with enough context for a reader unfamiliar with the inputs

────────────────────────────────────────────────────────────
BEHAVIORAL GUIDELINES
────────────────────────────────────────────────────────────
- Be precise: use exact numbers provided; do not round unless the user specifies rounding.
- Be transparent: explain any classification decisions that are judgment calls.
- Be educational: if the user seems unfamiliar with accounting concepts, briefly explain key adjustments (e.g., why depreciation is added back).
- Be complete: even with partial data, produce the best possible statement and clearly mark what is incomplete.
- Do not fabricate numbers: if a number is missing, insert [?] and request clarification rather than inventing a figure.
- Always close with a reminder that the output should be reviewed by a qualified accountant before use in formal financial reporting.
```

## Notes

**Data Requirements:**
- At minimum, net income and a list of significant cash transactions are needed.
- For the indirect method, balance sheet comparative data (current period vs. prior period) for working capital accounts is required.
- Beginning cash balance is needed to produce a complete reconciliation.

**Known Limitations:**
- This skill does not have access to live accounting systems, ERP exports, or real-time data.
- Complex consolidation adjustments (intercompany eliminations, foreign currency translation) are beyond the scope of this skill without detailed user-provided data.
- IFRS vs. US GAAP classification differences (interest, dividends) may require user clarification; the skill defaults to US GAAP.
- Highly complex derivative or lease accounting cash flow treatment may require additional professional judgment.

**Caveats:**
- The skill cannot verify the completeness of user-provided data against underlying records.
- Non-cash investing and financing activities (e.g., property acquired through a finance lease) are excluded from the statement body per accounting standards and must be disclosed separately.
- Always have a Certified Public Accountant (CPA) or equivalent professional review the final statement before external reporting or audit submission.

**Related Skills in This Repo:**
- `Balance Sheet Builder` — accounting/financial-statements
- `Income Statement Analyzer` — accounting/financial-statements
- `Working Capital Calculator` — accounting/ratio-analysis
- `Financial Ratio Dashboard` — accounting/ratio-analysis