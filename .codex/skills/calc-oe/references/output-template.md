# Output Template: Owner's Earnings

Use this structure for `$calc-oe` output files. Tables should have one column per fiscal year with an annual-filing synthesis memo.

```markdown
---
formal_qc_run: false
qc_status: pending
qc_completed_at: null
qc_result: null
---

# [Company] - Owner's Earnings

**Date:** [YYYY-MM-DD]
**Ticker:** [TICKER]
**Business Type:** [business type]
**OE Formula:** [formula used]
**Fiscal Years:** FY[first]-FY[last]

---

## Summary

| Metric | FY20XX | FY20XX |
|---|---:|---:|
| Total OE ($M) | | |
| OE per Share | | |
| OE Growth YoY | | |
| OE Margin (OE/Rev) | | |
| SBC ($M) | | |
| SBC % of OE | | |

**OE CAGR:** X.X%
**Average OE Margin:** X.X%

---

## OE Calculation Detail

Include only formula-relevant calculation rows. For example, omit `+ D&A` and `- Maint Capex` for insurance and bank-lender outputs unless a source-backed manual adjustment uses them.

| Component | FY20XX | FY20XX | Source |
|---|---:|---:|---|
| Starting metric | | | Income Statement |
| + D&A | | | Cash Flow / Income Statement |
| - Maint Capex | | | EST: X% of total capex |
| - SBC | | | Cash Flow / 10-K override |
| +/- One-time adjustments | | | 10-K memo |
| = Owner's Earnings | | | |
| Diluted Shares (M) | | | Income Statement |
| OE per Share | | | |

---

## Input Data

### Income Statement Extract

| Line Item | FY20XX | FY20XX |
|---|---:|---:|
| Revenue | | |
| Operating Income | | |
| Net Income | | |
| EBITDA | | |
| D&A | | |
| EPS (Diluted) | | |
| Diluted Shares (M) | | |

### Cash Flow Extract

| Line Item | FY20XX | FY20XX |
|---|---:|---:|
| Operating Cash Flow | | |
| Capital Expenditure | | |
| Free Cash Flow | | |
| Stock-Based Compensation | | |

---

## One-Time Adjustments

| Year | Item | Amount ($M) | Action | Rationale |
|---|---|---:|---|---|

If no one-time adjustments were made, state that no material one-time items were identified.

---

## Key Assumptions & Notes

### Business Type Rationale

### OE Formula Rationale

### Maintenance Capex

### SBC Source

### Data Gaps

---

## Cross-Check

### vs. Business Economics Section 8

| Metric | This Calculation | Biz Econ Section 8 | Difference | Explanation |
|---|---:|---:|---:|---|

### vs. Free Cash Flow

| Metric | FY20XX |
|---|---:|
| Owner's Earnings | |
| Reported FCF | |
| Difference | |
| Explanation | |

---

## Sources

- Income Statement: `[file path]`
- Cash Flow Statement: `[file path]`
- 10-K Memos: `[file path(s)]`
- Business Economics: `[file path]` if used
```
