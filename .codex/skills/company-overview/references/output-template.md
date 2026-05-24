# Company Overview Output Template

This template defines the output structure for the company-overview skill.

**Core Priority:** Do a few things really well — give the reader key takeaways and a great sense of what the business is.

**Target:** ~200-300 lines, ~3,000-4,000 words. Dense and scannable. Tables carry the data; prose adds only what tables cannot show.

**Structural Constraints:**
- **No sections beyond what this template defines.** Do NOT invent sections like "Valuation Context," "Balance Sheet Snapshot," "Product Innovation Pipeline," etc.
- **Commentary = key takeaway, not table walkthrough.** After each table, commentary should summarize the 1-2 most important insights (1-2 sentences). Do NOT describe every row.
- **Tables carry data; prose explains "why."** If a number is in the table, don't repeat it in prose unless you're explaining what caused it or why it matters.

---

## YAML Frontmatter

```yaml
---
type: company-overview
company: [Company Name]
ticker: [TICKER]
period_start: [YYYY]  # Earliest fiscal year covered
period_end: [YYYY]    # Most recent fiscal year covered
years_analyzed: [N]   # Number of fiscal years in analysis
synthesis_date: [YYYY-MM-DD]
formal_qc_run: false
formal_audit_run: false
qc_status: pending
audit_status: blocked_until_qc_complete
qc_completed_at: null
audit_completed_at: null
qc_result: null
audit_result: null
source_count:
  annual_filings: [N]
  investor_presentations: [N]
  financial_statements: [N]
---
```

---

# [Company] — Business Overview

*Multi-year synthesis covering FY[Start]-FY[End] ([N] years)*

---

## Key Takeaways

<!-- 5-8 bullets synthesizing the most important insights across all years -->
<!-- Each bullet: pattern/trend + supporting data + "so what?" -->
<!-- Most important insights first -->
<!-- HARD LIMIT: 60 words max per bullet. Two-sentence maximum per bullet. -->

- **[Lead-in phrase]:** [Cross-year insight with specific supporting data. Connect the trend to what it means for the business.]

- **[Lead-in phrase]:** [Another key pattern. Focus on what changed, what remained consistent, what surprised you.]

*Each bullet should synthesize across years, not repeat point-in-time facts. Keep each bullet to 60 words max / 2 sentences.*

---

## The Business

<!-- 2-3 SHORT paragraphs. Target: 200 words total. -->
<!-- Assume the reader understands the industry. Don't explain what products do if obvious from the name. -->
<!-- Do NOT add sub-sections or extra tables beyond the Segments table. -->

[Paragraph 1: What the company does, who it serves, how it makes money. Be direct.]

[Paragraph 2: Economic engine — what drives value creation, competitive position.]

[Paragraph 3 (optional): Only if there's something non-obvious about the business model.]

**Segments:**

| Segment | Description | % of Revenue (Latest) |
|---------|-------------|----------------------|
| [Segment 1] | [Brief description] | [X]% |
| [Segment 2] | [Brief description] | [X]% |
| [Segment 3] | [Brief description] | [X]% |

**Geographic Mix:** [Region breakdown if available, or "Not disclosed"]

**Customer Concentration:** [Concentration data if available, or "No single customer >10%"]

---

## Financial Evolution

<!-- Core financial metrics tracked across all available years -->
<!-- CAGR = ((End/Start)^(1/Years) - 1) × 100 -->

| Metric | FY[Start] | FY[End] | CAGR | Trajectory |
|--------|-----------|---------|------|------------|
| Revenue | [X]M | [X]M | [X.X]% | [Accelerating/Steady/Decelerating/Volatile/Declining] |
| Operating Income | [X]M | [X]M | [X.X]% | |
| Net Income | [X]M | [X]M | [X.X]% | |
| FCF | [X]M | [X]M | [X.X]% | |
| Employees | [X] | [X] | [X.X]% | |
| Operating Margin | [X.X]% | [X.X]% | [+/-X.Xpts] | |
| ROIC | [X.X]% | [X.X]% | [+/-X.Xpts] | |

*CAGR verification: ((End/Start)^(1/Years) - 1) × 100*

**Financial Narrative:**

[2-4 sentences. Summarize the key story — what drove growth, what surprised. Don't walk through every metric; highlight the 1-2 most important patterns and explain WHY they happened.]

---

## Segment Mix Shift

<!-- Track how revenue composition changed over time -->
<!-- Flag significant shifts: segments that emerged, declined, or became dominant -->

| Segment | FY[Start] | FY[End] | Δ | Significance |
|---------|-----------|---------|---|--------------|
| [Segment 1] | [X]% | [X]% | [+/-X]pts | [Emerging driver / Stable core / Declining relevance / New segment] |
| [Segment 2] | [X]% | [X]% | [+/-X]pts | |
| [Segment 3] | [X]% | [X]% | [+/-X]pts | |

**Mix Shift Interpretation:**

[1-2 sentences highlighting the most important shift and what it signals. Don't describe every row.]

---

## Management Credibility Scorecard

<!-- Score trackable promises from source memos -->
<!-- If no trackable promises, state that clearly -->

| Promise | Source | Outcome | Score |
|---------|--------|---------|-------|
| "[Exact promise text]" | FY[Year] 10-K | [Delivered / Partial / Missed / Abandoned] | [+2 to -2] |
| "[Exact promise text]" | [Source] | [Outcome] | [Score] |
| "[Exact promise text]" | [Source] | [Outcome] | [Score] |

**Total Score:** [Sum] / **Rating:** [HIGH / MODERATE / LOW / CONCERNING]

<!-- Rating thresholds: HIGH (>+5), MODERATE (0 to +5), LOW (-5 to 0), CONCERNING (<-5) -->

**Credibility Commentary:**

[1-2 sentences on the overall pattern. Don't re-describe each promise.]

*If insufficient data: "Credibility: Unable to assess — no trackable promises with outcomes in source materials."*

---

## Risk Evolution Matrix

<!-- Track how risks evolved across years -->
<!-- Trend: ↑ (increasing), → (stable), ↓ (decreasing) -->
<!-- Flag [NEW] and [RETIRED] risks -->

| Risk Category | FY[Year] | FY[Year] | FY[Year] | Current Status | Trend |
|---------------|----------|----------|----------|----------------|-------|
| Competitive | [Brief note] | [Brief note] | [Brief note] | [Current status] | ↑/→/↓ |
| Regulatory | | | | | ↑/→/↓ |
| Financial | | | | | ↑/→/↓ |
| Operational | | | | | ↑/→/↓ |
| Technology | | | | | ↑/→/↓ |
| Market/Macro | | | | | ↑/→/↓ |

**New Risks (appeared during period):**
- [Risk] — First mentioned FY[Year]

**Retired Risks (no longer mentioned):**
- [Risk] — Last mentioned FY[Year]

**Risk Commentary:**

[1-2 sentences on the most important risk evolution. Don't walk through every category.]

---

## Key Events Timeline

<!-- Significant events extracted from source memos -->
<!-- Include: Acquisitions, divestitures, leadership changes, products, regulatory, strategic pivots -->

| Year | Event | Impact |
|------|-------|--------|
| FY[Year] | [Event description] | [Brief impact assessment] |
| FY[Year] | [Event description] | [Brief impact assessment] |
| FY[Year] | [Event description] | [Brief impact assessment] |
| FY[Year] | [Event description] | [Brief impact assessment] |
| FY[Year] | [Event description] | [Brief impact assessment] |

*Minimum 3 events. Focus on events that shaped the business trajectory.*

---

## Questions for Monitoring

<!-- 3-5 forward-looking questions based on observed patterns -->
<!-- Each question should be specific and investment-relevant -->
<!-- "Why it matters" is a parenthetical after the question, not a separate line -->

1. **[Question]?** *(Why it matters: [one sentence on investment relevance])*

2. **[Question]?** *(Why it matters: [one sentence])*

3. **[Question]?** *(Why it matters: [one sentence])*

---

## Year Card Summary

<!-- Brief 3-line summary per fiscal year -->
<!-- Provides quick reference for each year's story -->

### FY[Year]

**Theme:** [One phrase capturing the year]
**Key developments:** [2-3 most significant events/changes]
**Performance:** Revenue: $[X]B ([+/-X]%), Op Income: $[X]M ([+/-X]%)

### FY[Year]

**Theme:** [One phrase]
**Key developments:** [2-3 items]
**Performance:** Revenue: $[X]B ([+/-X]%), Op Income: $[X]M ([+/-X]%)

<!-- Repeat for each fiscal year covered -->

---

## Source Files

<!-- List all Foundation materials read -->
<!-- Organized by type -->

**Annual Filing Memos:**
- `[filename]` — FY[Year]
- `[filename]` — FY[Year]

**Investor Presentation Memos:**
- `[filename]` — [Event/Date]

**Financial Statements:**
- `[filename]`

**Total Sources:** [N] files

---

*Generated: [YYYY-MM-DD]*
