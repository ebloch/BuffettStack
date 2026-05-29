---
formal_qc_run: true
qc_status: complete
qc_completed_at: 2026-05-29-0953
qc_result:
  gaps_found: 0
  gaps_addressed: 0
  remaining_issues: []
formal_audit_run: true
audit_status: complete
audit_completed_at: 2026-05-29-0953
audit_result:
  violations_found: 1
  fixes_applied: 1
  flagged_for_review: []
---

# Berkshire Hathaway Inc. - Owner's Earnings

**Date:** 2026-05-29
**Ticker:** BRK-B
**Business Type:** insurance
**OE Formula:** Net Income - SBC, adjusted to operating earnings when source-supported
**Fiscal Years:** FY2024-FY2024

---

## Summary

| Metric | FY2024 |
| --- | ---: |
| Total OE ($M) | 47,437 |
| OE per Share | $22.00 |
| OE Growth YoY |  |
| OE Margin (OE/Rev) | 12.8% |
| SBC ($M) | 0 |
| SBC % of OE | 0.0% |

**OE CAGR:** 
**Average OE Margin:** 12.8%

---

## OE Calculation Detail

| Component | FY2024 | Source |
| --- | ---: | ---: |
| Net Income | 88,995 | Income Statement / Cash Flow |
| - SBC | 0 | Cash Flow JSON unless source-overridden |
| +/- One-time adjustments | (41,558) | Source-backed adjustment to FY2024 operating earnings |
| = Owner's Earnings | 47,437 |  |
| Diluted Shares (M) | 2,156.6 | Income Statement |
| OE per Share | $22.00 |  |

---

## Input Data

### Income Statement Extract

| Line Item | FY2024 |
| --- | ---: |
| Revenue | 371,433 |
| Operating Income | 59,436 |
| Net Income | 88,995 |
| EBITDA | 72,291 |
| D&A | 12,855 |
| EPS (Diluted) |  |
| Diluted Shares (M) | 2,156.6 |

### Cash Flow Extract

| Line Item | FY2024 |
| --- | ---: |
| Operating Cash Flow | 30,592 |
| Capital Expenditure | (18,976) |
| Free Cash Flow | 11,616 |
| Stock-Based Compensation | 0 |

---

## One-Time Adjustments

The deterministic script started from GAAP net income. The annual-filing memo and Business Economics analysis identify Berkshire's FY2024 operating earnings as $47.437 billion and flag GAAP investment gains and losses as period-to-period volatility that should be valued separately from recurring operating earnings.

| Year | Item | Amount ($M) | Action | Rationale |
|---|---|---:|---|---|
| FY2024 | Investment gains/losses and other GAAP mark-to-market volatility | (41,558) | Adjust to operating earnings | Source-backed adjustment from GAAP net income of $88.995 billion to operating earnings of $47.437 billion |

---

## Key Assumptions & Notes

### Business Type Rationale

Classified as `insurance` because the Business Economics analysis identifies Berkshire as an insurance-led decentralized conglomerate and the annual-filing memo identifies insurance underwriting, insurance investment income and float as central to the earnings engine.

### OE Formula Rationale

Applied deterministic formula: Net Income - SBC. Post-run review adjusted FY2024 to operating earnings because the source memo explicitly flags GAAP net income as less useful for Berkshire due to investment mark-to-market volatility.

### Maintenance Capex

Maintenance capex estimated at 0% of total capital expenditure. Update this if company disclosures support a better split.

### SBC Source

SBC is sourced from cash flow statement JSON. Years with blank or zero SBC require source review against the 10-K memo.

### Data Gaps

No deterministic data gaps identified.

---

## Cross-Check

### vs. Business Economics Section 8

Business Economics file available for manual cross-check: `/Users/ethanbloch/Projects/BuffettStack/research/Berkshire Hathaway Inc./2.1-Business-Economics/Business Economics Analysis - Berkshire Hathaway Inc. - 2026-05-23-1041.md`

| Metric | This Calculation | Biz Econ Section 8 | Difference | Explanation |
|---|---:|---:|---:|---|
| Owner's Earnings ($M) | 47,437 | 47,437 | 0 | Matches Business Economics Section 8 normalized operating owner earnings |
| OE per Share | $22.00 | N/A | N/A | Business Economics provides the total OE cross-check, not a per-share figure |

### vs. Free Cash Flow

| Metric | FY2024 |
| --- | ---: |
| Owner's Earnings | 47,437 |
| Reported FCF | 11,616 |
| Difference | 35,821 |
| Explanation | Berkshire's operating earnings are not designed to equal industrial free cash flow because insurance float, investment income, railroad/utility capex and subsidiary reinvestment create different cash conversion dynamics. |

---

## Sources

- Income Statement: `/Users/ethanbloch/Projects/BuffettStack/research/Berkshire Hathaway Inc./1.3-Financial-Statements/BRK-B-income-statement.json`
- Cash Flow Statement: `/Users/ethanbloch/Projects/BuffettStack/research/Berkshire Hathaway Inc./1.3-Financial-Statements/BRK-B-cash-flow.json`
- Annual Filing Memos:
  - FY2024: `/Users/ethanbloch/Projects/BuffettStack/research/Berkshire Hathaway Inc./1.1-Annual-Filings/FY2024 - Berkshire Hathaway - 10-K Synthesis - Memo - 2026-05-09-1358.md`
- Business Economics: `/Users/ethanbloch/Projects/BuffettStack/research/Berkshire Hathaway Inc./2.1-Business-Economics/Business Economics Analysis - Berkshire Hathaway Inc. - 2026-05-23-1041.md`
