# Management Credibility Audit Output Template

Use this structure when writing the audit document.

---

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

# [Company] - Management Credibility Audit

**Date:** [Audit Date]
**Ticker:** [TICKER]
**Period Covered:** [Start Year] - [End Year] ([X] quarters reviewed)

---

## Data Sources

| Source | Count | Date Range | Coverage |
|--------|-------|------------|----------|
| Earnings Transcripts (FMP) | X | YYYY-QX to YYYY-QX | X of Y quarters |
| Earnings Transcripts (web search) | X | YYYY-QX to YYYY-QX | Fallback for missing quarters |
| Press Releases (FMP) | X | YYYY-MM to YYYY-MM | Guidance, M&A, strategic announcements |
| Web Research | N/A | Various | Insider ownership, compensation, proxy data |

**Data Gaps:** [Note any missing quarters or periods with incomplete data. If none, state "None — full coverage for audit period."]

---

## Executive Summary

[3-5 paragraphs covering:]
- Overall credibility assessment and rating
- Key strengths (where management has delivered)
- Key concerns (where management has fallen short)
- Capital allocation track record summary
- Bottom line: Can you trust this management team?

**Overall Credibility Rating:** [HIGH / MODERATE / LOW / CONCERNING]

---

## Quantitative Scorecard

### Promise Delivery Summary

| Category | Promises Made | Scored | Hit Rate | Avg Score |
|----------|---------------|--------|----------|-----------|
| Financial Targets | X | X | X% | X.X |
| Capital Allocation | X | X | X% | X.X |
| Operational Goals | X | X | X% | X.X |
| Cost/Efficiency Programs | X | X | X% | X.X |
| Strategic Initiatives | X | X | X% | X.X |
| **Total** | **X** | **X** | **X%** | **X.X** |

*Note: "Scored" excludes promises too recent to evaluate or too vague to verify. Timeline commitments are tracked as an attribute of each promise via the "Timeframe" column, not as a separate category.*

### Trend Over Time

| Year | Promises Scored | Hit Rate | Avg Score | Notable Events |
|------|-----------------|----------|-----------|----------------|
| 20XX | X | X% | X.X | [CEO change, acquisition, etc.] |
| 20XX | X | X% | X.X | |
| 20XX | X | X% | X.X | |
| 20XX | X | X% | X.X | |
| 20XX | X | X% | X.X | |

**Trend:** [Improving / Stable / Declining] — [1-2 sentence explanation]

### Guidance Accuracy

| Metric | Times Guided | Beat | Met | Missed | Accuracy |
|--------|--------------|------|-----|--------|----------|
| Revenue | X | X | X | X | X% |
| EPS | X | X | X | X | X% |
| Margins | X | X | X | X | X% |
| Other | X | X | X | X | X% |

*Note: If the company does not provide guidance for a metric, include a row: "[Metric] | Not Provided | — | — | — | N/A — Management does not guide on [metric]"*

**Guidance style:** [Conservative sandbagging / Tight and accurate / Optimistic and often missed / Highly variable]

---

## Say/Do Matrix Placement

```
                      DELIVERS
                          |
           UNDERPROMISE   |   CREDIBLE
           OVERDELIVER    |   CONSISTENT
                          |
VAGUE ────────────────────┼──────────────────── SPECIFIC
                          |
           EMPTY          |   OVERPROMISE
           SUITS          |   UNDERDELIVER
                          |
                     FAILS TO DELIVER
```

**Placement:** [Quadrant name]

**Rationale:** [2-3 sentences explaining why management falls in this quadrant, with specific evidence]

**Investment Implication:** [What this means for how to interpret management statements]

---

## Key Management Quotes

[Include 5-10 of the most important verbatim quotes that capture management's commitments and communication style. These quotes should be the "evidence trail" for your assessment.]

### Commitments That Were Delivered

> "[Exact verbatim quote]"
> — [Executive Name], [Title], [Quarter Year]

**Outcome:** [What happened and when]

> "[Exact verbatim quote]"
> — [Executive Name], [Title], [Quarter Year]

**Outcome:** [What happened and when]

### Commitments That Were Missed or Partially Delivered

> "[Exact verbatim quote]"
> — [Executive Name], [Title], [Quarter Year]

**Outcome:** [What actually happened]
**Management Response:** [How did they address the miss? Quote their explanation if available.]

---

## Missed & Partial Promises (Detailed)

**IMPORTANT:** This section documents every promise scored 0, -1, or -2. Even highly credible management teams miss sometimes — what matters is how they handle misses.

| Date | Original Promise (Verbatim Quote) | What Happened | Management Response | Score |
|------|----------------------------------|---------------|---------------------|-------|
| QX 20XX | "[Exact quote]" | [Actual outcome] | [How addressed / Not addressed] | 0/-1/-2 |
| QX 20XX | "[Exact quote]" | [Actual outcome] | [How addressed / Not addressed] | 0/-1/-2 |

**Analysis of Misses:**

- **Total promises missed or partial:** X of Y scored promises (X%)
- **Pattern in misses:** [Are they concentrated in one area? One time period? Related to external factors?]
- **How management handles failure:** [Transparent acknowledgment / Excuses and blame-shifting / Quietly ignored]
- **Recovery after misses:** [Do they adjust and deliver later, or do misses compound?]

[If no misses identified, state: "No promises scored below +1 during audit period. This is unusual — verify scoring rigor."]

---

## Promise-by-Promise Detail

### Financial Targets

| Date | Promise (Verbatim Quote) | Source | Specificity | Timeframe | Outcome | Score |
|------|--------------------------|--------|-------------|-----------|---------|-------|
| Q1 20XX | "[Exact quote]" | Transcript | Specific | FY20XX | [Result] | +X |
| Q2 20XX | "[Exact quote]" | PR | Directional | 2 years | [Result] | +X |

### Capital Allocation

| Date | Promise (Verbatim Quote) | Source | Specificity | Timeframe | Outcome | Score |
|------|--------------------------|--------|-------------|-----------|---------|-------|
| Q1 20XX | "[Exact quote]" | Transcript | Specific | FY20XX | [Result] | +X |

### Operational Goals

| Date | Promise (Verbatim Quote) | Source | Specificity | Timeframe | Outcome | Score |
|------|--------------------------|--------|-------------|-----------|---------|-------|
| Q1 20XX | "[Exact quote]" | Transcript | Specific | FY20XX | [Result] | +X |

### Cost/Efficiency Programs

| Program | Announced | Savings Target | Timeline | Restructuring Cost | Actual Savings | Score |
|---------|-----------|----------------|----------|-------------------|----------------|-------|
| "Project X" | Q2 20XX | $Xm annual | By 20XX | $Xm | $Xm achieved | +X |

*Note: Only include formal programs with names, targets, and timelines. Use "~$Xm (estimated from [source])" if exact figures not disclosed. Use "Not disclosed" if company announced restructuring without savings target. Do NOT create rows with "N/A" for informal initiatives.*

*Additional efficiency initiatives (not formally tracked): [List any informal initiatives mentioned but not tracked with specific targets, e.g., "marketing transformation to digital (60% digital mix achieved)", "supply chain productivity (ongoing)". If none, omit this line.]*

### Strategic Initiatives

| Date | Promise (Verbatim Quote) | Source | Specificity | Timeframe | Outcome | Score |
|------|--------------------------|--------|-------------|-----------|---------|-------|
| Q1 20XX | "[Exact quote]" | Transcript | Specific | FY20XX | [Result] | +X |

---

## Pattern Analysis

### Positive Patterns

[List with specific evidence. Format:]

- **[Pattern name]:** [Description with examples and dates]

### Concerning Patterns

[List with specific evidence. Format:]

- **[Pattern name]:** [Description with examples and dates]

### Kitchen Sink Analysis

**Identified kitchen sink quarters:** [List any, or "None identified"]

| Quarter | Charges/Write-downs | Guidance Cut? | Subsequent Beats? | Assessment |
|---------|---------------------|---------------|-------------------|------------|
| Q2 20XX | $Xm restructuring, $Xm impairment | Yes, -X% | 4 consecutive beats | Manufactured recovery |

---

## Capital Allocation Track Record

### M&A Synergy Tracking

| Acquisition | Date | Price | Synergy Promise | Timeline | Actual Result | Score |
|-------------|------|-------|-----------------|----------|---------------|-------|
| [Target] | 20XX | $XB | "$Xm cost synergies" | By Year 3 | $Xm achieved | +X |

**M&A commentary:** [Overall assessment of acquisition track record]

### Buyback Timing Analysis

| Year | $ Spent | Avg Price Paid | Stock Range | Intrinsic Value Est. | Score |
|------|---------|----------------|-------------|---------------------|-------|
| 20XX | $XB | $XX | $XX - $XX | $XX | +X |

**Buyback assessment:** [Did they buy smart or buy dumb? Evidence of value discipline?]

**Insider selling overlap:** [Any evidence of executives selling while company bought back? If none, state "No concerning overlap identified."]

### Other Capital Allocation

| Decision | Date | Stated Rationale | Outcome | Score |
|----------|------|------------------|---------|-------|
| Dividend increase | 20XX | "Confidence in cash flow" | Sustained | +1 |
| Major capex | 20XX | "ROI of X%" | Achieved X% | +1 |

**Capital allocation rating:** [Excellent / Good / Mixed / Poor]

---

## Insider Ownership & Compensation Alignment

### Executive Ownership

| Executive | Title | Base Salary | Shares Owned | Value (approx) | % of Company | Multiple of Salary |
|-----------|-------|-------------|--------------|----------------|--------------|-------------------|
| [Name] | CEO | $X.XM | X,XXX,XXX | $XXM | X.X% | XXx |
| [Name] | CFO | $X.XM | X,XXX,XXX | $XXM | X.X% | XXx |
| [Name] | [Segment President/COO] | $X.XM | X,XXX,XXX | $XXM | X.X% | XXx |

*Source: FYxxxx Proxy Statement (DEF 14A), pages XX-XX*

*Note: Minimum 3 executives required. Include segment/division presidents who speak on earnings calls. If additional executive data unavailable, state: "Additional executive ownership data not separately disclosed in proxy statement."*

*[If executive transition during audit period, add:] Note: [CEO/CFO] transition [announced/completed] [date] — [Predecessor Name] succeeded by [Successor Name] as [Title] effective [date].*

**Ownership assessment:** [Strong alignment / Moderate / Minimal skin in the game]

### Recent Insider Transactions (Last 12-24 Months)

| Date | Executive | Transaction | Shares | Price | Value | Context |
|------|-----------|-------------|--------|-------|-------|---------|
| 20XX-XX | [Name] | Buy/Sell | XX,XXX | $XXX | $X.XM | [10b5-1 plan / Open market / Options exercise] |

**Transaction pattern:** [Net buyer / Neutral / Net seller]

**Red flags identified:** [None / List any concerning patterns]

### Compensation Structure

| Component | % of CEO Total Comp | Metrics/Vesting |
|-----------|---------------------|-----------------|
| Base Salary | X% | Fixed |
| Annual Bonus | X% | [Metrics used] |
| Long-term Incentive | X% | [Metrics used, vesting period] |
| Stock Awards | X% | [Time-based / Performance-based, vesting] |

**Total CEO compensation (most recent year):** $XX.XM

**Compensation vs. performance:**
- CEO pay growth over audit period: X%
- Stock price growth over same period: X%
- EPS growth over same period: X%

**Alignment assessment:**
- Are incentives tied to long-term value creation? [Yes/Partially/No]
- Are metrics easy to manipulate (adjusted EPS) or harder (ROIC, FCF)? [Harder/Mixed/Easier]
- Is there meaningful equity ownership requirement? [Yes/No]

### Overall Alignment Score

| Factor | Assessment | Score |
|--------|------------|-------|
| Insider ownership level | [High/Moderate/Low] | +1/0/-1 |
| Recent transaction pattern | [Net buyer/Neutral/Net seller] | +1/0/-1 |
| Compensation structure | [Aligned/Mixed/Misaligned] | +1/0/-1 |
| Pay vs. performance | [Reasonable/Stretched/Excessive] | +1/0/-1 |
| **Overall Alignment** | | **+X** |

---

## Non-GAAP Definition Drift

| Metric | Year 1 Adjustments | Year 5 Adjustments | Drift? |
|--------|-------------------|-------------------|--------|
| Adjusted EPS | [List] | [List] | Y/N |
| Adjusted EBITDA | [List] | [List] | Y/N |
| Free Cash Flow | [Definition] | [Definition] | Y/N |

**GAAP vs. Non-GAAP gap:**

| Year | GAAP EPS | Adjusted EPS | Gap | Gap as % of GAAP |
|------|----------|--------------|-----|------------------|
| 20XX | $X.XX | $X.XX | $X.XX | X% |
| 20XX | $X.XX | $X.XX | $X.XX | X% |

**Assessment:** [Is the gap widening? Are adjustments becoming more aggressive?]

---

## Red Flags Identified

[List all red flags with severity ratings]

| Red Flag | Severity | Evidence | Implication |
|----------|----------|----------|-------------|
| [Flag] | High/Med/Low | [Specific examples] | [What it means] |

**Summary:** [Overall red flag assessment — clean, some concerns, or significant issues]

---

## Deep Dive: Key Issues

[For each major concern, provide detailed analysis]

### [Issue 1 Title]

**What was promised:** [Exact quote with date]

**Context:** [Market conditions, company situation at time of promise]

**What happened:** [Actual outcome]

**Management's explanation:** [How they addressed it, or didn't]

**Pattern:** [First time or recurring?]

**Implication:** [What this tells us about trusting future statements]

### [Issue 2 Title]

[Same structure]

---

## Conclusion and Investment Implications

### Credibility Assessment

**Rating:** [HIGH / MODERATE / LOW / CONCERNING]

**Rating criteria:**
- HIGH: >80% delivery rate, transparent about misses, no significant red flags
- MODERATE: 60-80% delivery, occasional excuses but generally trustworthy
- LOW: 40-60% delivery, pattern of overpromising, some red flags
- CONCERNING: <40% delivery, systemic credibility issues, significant red flags

**Rationale:** [Why this rating, with key supporting evidence]

### What This Means for Investors

- **Can you trust guidance?** [Yes / With discount / No — and explanation]
- **How should you interpret forward-looking statements?** [Take at face value / Apply X% haircut / Ignore entirely]
- **What discount should be applied to management projections?** [Specific recommendation based on track record]

### Comparison Context

[If relevant, how does this compare to industry norms or peer companies?]

### Monitoring Points

[What to watch going forward to track credibility changes]

- [ ] [Specific thing to monitor with threshold]
- [ ] [Specific thing to monitor with threshold]
- [ ] [Specific thing to monitor with threshold]

---

## Appendix: Source Documents

### Earnings Transcripts Reviewed

| Quarter | Date | Source | Notes |
|---------|------|--------|-------|
| Q4 20XX | YYYY-MM-DD | FMP | |
| Q3 20XX | YYYY-MM-DD | FMP | |
| Q2 20XX | YYYY-MM-DD | FMP | |
| Q1 20XX | YYYY-MM-DD | FMP | |
| Q4 20XX | YYYY-MM-DD | web search | FMP unavailable |
| ... | ... | ... | |

### Key Press Releases Referenced

| Date | Title | Relevance |
|------|-------|-----------|
| YYYY-MM-DD | [Title] | M&A announcement |
| YYYY-MM-DD | [Title] | Guidance update |
| ... | ... | ... |
```
