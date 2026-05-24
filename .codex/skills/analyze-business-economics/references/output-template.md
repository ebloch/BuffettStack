# Business Economics Analysis - Output Template

```markdown
---
formal_qc_run: false
formal_audit_run: false
qc_status: pending
audit_status: blocked_until_qc_complete
qc_completed_at: null
audit_completed_at: null
qc_result: null
audit_result: null
---

# [Company] - Business Economics Analysis

**Date:** [Current Date]
**Ticker:** [TICKER]
**Business Model:** [Primary Classification]

---

## Executive Summary

### Quick Reference

<!-- CRITICAL: This table MUST use exactly these 6 question rows. Do NOT substitute with different questions or an "attribute" format. -->

| Question | Answer |
|----------|--------|
| What type of business? | [Primary classification from Section 1] |
| What's the key metric? | [#1 Primary KPI from Section 4] |
| What's misleading in GAAP? | [Top quirk from Section 3 in 1 sentence] |
| What multiple to use? | [Preferred multiple from Section 8] |
| Who are true peers? | [Top 2-3 peers from Section 7] |
| Biggest analytical mistake? | [#1 mistake from Section 6] |

<!-- VALIDATION: All 6 rows must be filled with these exact questions. Each answer should directly reference the corresponding section. Do NOT change the question column. -->

### The Big Quirks

<!-- List 2-5 quirks, most important first -->

1. **[Quirk 1 Name]** — [1-2 sentence summary of what it is and why it matters]
2. **[Quirk 2 Name]** — [1-2 sentence summary]
3. **[Quirk 3 Name]** — [1-2 sentence summary]

### What to Focus On

<!-- Top 3-5 metrics that actually matter for this business -->

- [Key metric 1] — [why]
- [Key metric 2] — [why]
- [Key metric 3] — [why]

### What to Ignore

<!-- Metrics that are misleading for this business -->

- [Misleading metric 1] — [why]
- [Misleading metric 2] — [why]
- [Misleading metric 3] — [why]

---

## 1. Business Model Classification

**Primary Category:** [Category from classification table]

**Secondary Characteristics:** [Any hybrid elements, if applicable]

**How This Business Makes Money:**
[2-3 sentence clear explanation of the economic model - where cash comes from, what drives it]

---

## 2. Economic Engine

| Driver | Description |
|--------|-------------|
| Primary Cash Source | [Where does cash actually come from?] |
| Core Unit of Value | [e.g., policy, subscriber, AUM, transaction] |
| Growth Drivers | [Volume, price, mix, market growth?] |
| Margin Drivers | [Scale, pricing power, cost structure?] |
| Capital Intensity | [Capital-intensive or capital-light? Why?] |
| Reinvestment Requirements | [Maintenance vs. growth capex distinction] |

**Economic Engine Summary:**
[Paragraph explaining the true economics of this business in plain language]

**ROIC Calculation Note (for asset-light businesses):**
<!-- Only include if ROIC is mentioned or business is asset-light -->
[How to calculate invested capital for this business. State the approach and why.]

**Seasonality & Working Capital Timing:**
<!-- Only include if business has material deferred revenue, float, or working capital timing -->
[Quarterly pattern description. Which quarters see cash inflows vs. outflows? How does this affect period comparisons?]

---

## 3. Key Accounting Quirks

<!-- Document at least 2 quirks. Most businesses have 3-5. -->

### Quirk 1: [Name]

**What:** [Description of the accounting treatment]

**Distortion:** [What line items are affected and how]

**Adjustment:** [How to handle it / what to do about it]

**Example:** [Specific reference from filings if available]

### Quirk 2: [Name]

**What:** [Description]

**Distortion:** [Impact]

**Adjustment:** [How to handle]

### Quirk 3: [Name]

<!-- Add more quirks as needed -->

---

## 4. Metrics That Matter

| Metric | Why It Matters | Where to Find It | Benchmark |
|--------|----------------|------------------|-----------|
| [Metric 1] | [Explanation] | [10K section, earnings release, etc.] | [Good threshold + Concern threshold: e.g., ">85% strong; <78% signals pricing erosion"] |
| [Metric 2] | [Explanation] | [Source] | [Range with both ends: e.g., "15-22% typical; <12% underinvestment; >25% efficiency concern"] |
| [Metric 3] | [Explanation] | [Source] | [Must include what triggers concern, not just what's "good"] |
| [Metric 4] | [Explanation] | [Source] | [Quantified with alert threshold] |
| [Metric 5] | [Explanation] | [Source] | [Quantified with alert threshold] |

<!-- VALIDATION: Every benchmark MUST have two components:
  1. What "good" looks like (upper threshold or acceptable range)
  2. What "concerning" looks like (lower threshold or trigger for alert)

If you can't answer "what level would make me worried?", the benchmark is incomplete.
-->

<!-- BENCHMARK FORMAT CHECK:
REQUIRED FORMAT — include BOTH good and concern thresholds:
  - ">8% strong, 5-8% adequate, <5% concerning"
  - "80-85% for quality pharma; <78% signals pricing erosion"
  - ">80% excellent; 50-80% acceptable; <50% indicates cash conversion problem"
  - "15-22% typical; <12% underinvestment; >25% efficiency red flag"

FAIL — missing concern threshold (do not use):
  - "15+ for large cap" (no lower bound for concern)
  - ">30% growth is strong" (what if it's 10%?)
  - "90-95% for quality companies" (missing what <90% signals)
  - "consistent matters more than level" (qualitative, no numbers)
  - "quality matters more" (no thresholds at all)
  - "~92% (need verification)" (uncertain data — verify or omit)
-->

<!-- SHAREHOLDER RETURN CHECK (for capital-return-focused businesses):
If the company is a dividend aristocrat, has >80% FCF payout ratio, or emphasizes capital returns to shareholders, include at least one of:
  - FCF Payout Ratio: "<90% sustainable; 90-100% acceptable for stable franchisors; >100% unsustainable without balance sheet deterioration"
  - Dividend Yield: "[appropriate range]; >[X%] may signal distress or value trap; <[Y%] historically rare"
  - Dividend Coverage (FCF/Dividend): ">1.2x comfortable; 1.0-1.2x tight; <1.0x unsustainable"
-->

**Primary KPIs to Track:**

1. [Most important metric] — [why it's #1]
2. [Second most important] — [why]
3. [Third most important] — [why]

---

## 5. Metrics to Ignore or Adjust

| Metric | Problem | Alternative |
|--------|---------|-------------|
| [Metric 1] | [Why it's misleading] | [What to do instead] |
| [Metric 2] | [Why it's misleading] | [What to do instead] |
| [Metric 3] | [Why it's misleading] | [What to do instead] |

**GAAP Net Income Issues:**
<!-- Explain why reported net income is misleading for this specific company -->
[Specific issues: e.g., "Unrealized gains on equity securities flow through net income per ASC 321, causing earnings to swing +/- 30% based on market movements" or "Net income includes non-cash stock compensation of $X that understates true cash earnings"]

**GAAP Cash Flow Issues:**
<!-- Explain why reported cash flow statement may be misleading -->
[Specific issues: e.g., "Customer margin deposits flow through operating cash flow but aren't true operating cash" or "Deferred revenue growth makes operating cash flow exceed economic earnings during growth phases"]

**Standard Ratio Assessment:**

| Ratio | Usability | Notes |
|-------|-----------|-------|
| P/E | [Useful / Adjust / Avoid] | [Why] |
| EV/EBITDA | [Useful / Adjust / Avoid] | [Why] |
| P/B | [Useful / Adjust / Avoid] | [Why] |
| FCF Yield | [Useful / Adjust / Avoid] | [How to calculate correctly if needed] |

---

## 6. Common Analytical Mistakes

<!-- Document at least 2-3 mistakes analysts make -->

| Mistake | Why It's Wrong | Correct Approach |
|---------|----------------|------------------|
| [Mistake 1] | [Explanation] | [What to do instead] |
| [Mistake 2] | [Explanation] | [What to do instead] |
| [Mistake 3] | [Explanation] | [What to do instead] |

**Red Flags That Aren't Red Flags:**
<!-- Things that look bad but are normal for this business -->
- [Item] — [Why it's actually fine]

**Green Flags That Aren't Green Flags:**
<!-- Things that look good but are misleading -->
- [Item] — [Why it's misleading]

**Quantified Risk Impacts:**
<!-- For key structural risks, show the math -->
| Risk | Calculation | Impact |
|------|-------------|--------|
| [Risk 1] | [Formula, e.g., "50bps × $166B gross bookings"] | [Dollar impact, e.g., "~$830M revenue"] |
| [Risk 2] | [Formula] | [Impact] |

---

## 7. Peer Selection

**True Comparables:**

| Peer | Why Comparable | Key Differences |
|------|----------------|-----------------|
| [Peer 1] | [Similarity] | [How they differ] |
| [Peer 2] | [Similarity] | [How they differ] |
| [Peer 3] | [Similarity] | [How they differ] |

**False Comparables to Avoid:**

| Company | Why It Seems Similar | Why It's Not Comparable |
|---------|---------------------|------------------------|
| [Company 1] | [Surface similarity] | [Key difference] |
| [Company 2] | [Surface similarity] | [Key difference] |

**Best Comparables for Valuation:** [Ranked list]

**Best Comparables for Operating Metrics:** [Ranked list if different]

---

## 8. Valuation Implications

**Preferred Valuation Methods:**

1. [Primary method] — [Why it's best for this business]
2. [Secondary method] — [When to use it]

**Multiples Assessment:**

| Multiple | Usability | Notes | Benchmark Range |
|----------|-----------|-------|-----------------|
| P/E | High/Medium/Low/Avoid | [Explanation] | [Range if usable, e.g., "15-25x for mature SaaS"; N/A if Avoid] |
| EV/EBITDA | High/Medium/Low/Avoid | [Explanation] | [Range if usable; N/A if Avoid] |
| EV/EBIT | High/Medium/Low/Avoid | [Explanation] | [Range if usable; N/A if Avoid] |
| P/FCF | High/Medium/Low/Avoid | [Explanation] | [Range if usable; N/A if Avoid] |
| P/B | High/Medium/Low/Avoid | [Explanation] | [Range if usable; N/A if Avoid] |
| [Industry-specific, e.g., EV/cRPO] | High/Medium/Low | [Explanation] | [REQUIRED: Include benchmark range] |

<!-- VALIDATION: Every multiple rated High or Medium MUST have a benchmark range in the last column.

REQUIRED FORMAT: Include cheap, typical, AND expensive thresholds:
  - "<20x cheap, 20-28x typical, >30x expensive"
  - "25-35x typical; <25x cheap, >38x expensive"

FAIL if benchmark only shows "typical" range without cheap/expensive thresholds.
FAIL if benchmark says "15-20x typical; use as sanity check" — must include when it's cheap/expensive.

For multiples rated "Avoid" or "Low", write "N/A" in Benchmark Range column.
Do NOT leave Benchmark Range blank for usable multiples. -->

**DCF Considerations:**

| Issue | Implication | Adjustment |
|-------|-------------|------------|
| [Issue 1] | [How it affects DCF] | [How to handle] |
| [Issue 2] | [How it affects DCF] | [How to handle] |

**Owner's Earnings Calculation:**
<!--
CRITICAL: All figures must be from the SAME fiscal year. Do not mix FY2024 and FY2025 data.

Quirks fall into two categories:
1. DOLLAR ADJUSTMENTS: Add/subtract specific amounts (show as line items with [source])
2. INTERPRETATION NOTES: Affect how you read the result (show as inline notes)

Every dollar amount must be sourced (e.g., "per 10-K FY2024") or labeled as estimate (e.g., "[EST: X% based on Y]")
-->

```
Net Income                                    $X,XXXM (FY[Year]) [per 10-K synthesis]
+ Depreciation & Amortization                    $XXXM [per 10-K]
- Maintenance CapEx                              ($XXXM) [EST: X% of total, based on Y]
+/- [QUIRK 1]: [brief description]               $XXXM [source] — [why this adjustment]
+/- [QUIRK 2]: [brief description]               ($XXXM) [source]
= Owner's Earnings                            ~$X,XXXM

Note: [Any interpretation quirks that affect how to read this figure]
```

**Quirk-to-Calculation Mapping:**
| Section 3 Quirk | Treatment | Line Item or Note |
|-----------------|-----------|-------------------|
| [Quirk 1] | Dollar adjustment | [Line item name] |
| [Quirk 2] | Interpretation note | See calculation note |
[Map ALL quirks from Section 3]

**Terminal Value Considerations:**
[Any special considerations for terminal value given this business model]

---

## Sources

- [List sources used: 10-K sections, web research, etc.]
```
