# Phase 2: Quality Control Prompt

Use this prompt when reviewing an owner's earnings memo produced by `$calc-oe`.

```text
You are performing quality control on an Owner's Earnings calculation.

Context:
- Company: [COMPANY]
- OE Calculation Path: [MEMO_PATH]

Source Documents:
- Income Statement: [INCOME_STATEMENT_PATH]
- Cash Flow Statement: [CASH_FLOW_PATH]
- Annual Filing Memos: [10K_MEMO_PATHS]

Run $quality-control calc-oe "[COMPANY]".

Focus areas:
- Verify component sums equal OE for every fiscal year.
- Verify OE per share equals OE divided by diluted shares.
- Verify YoY growth, CAGR, OE margin, and SBC percentage calculations.
- Confirm SBC is deducted every year and $0 SBC is source-supported.
- Confirm maintenance capex percentage is reasonable and documented.
- Confirm one-time exclusions are source-supported and not recurring in 3+ years.
- Confirm all input data matches the statement JSON or documented 10-K overrides.
- Confirm the FCF cross-check is present and discrepancies are explained.

Classify gaps:
- CRITICAL: wrong math, wrong formula, missing SBC deduction, missing required component.
- HIGH: unsourced figure, unsupported one-time adjustment, questionable assumption.
- MINOR: rounding or non-material formatting issue.

Return:
{
  "gaps_found": number,
  "gaps_addressed": number,
  "status": "success|partial|failed",
  "remaining_issues": ["..."]
}
```
