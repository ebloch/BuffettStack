# Phase 1: Company Overview Synthesis Prompt

Use this reference for the synthesis pass for company-overview.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are synthesizing a multi-year Business Overview for [COMPANY].

**Output Path:** [OUTPUT_PATH]

## Your Task

Create a longitudinal business overview that synthesizes all available Foundation materials for [COMPANY]. This answers the question: "How has this business evolved over time?"

## Step 0: Check Prerequisites (REQUIRED)

This skill requires Foundation materials to exist. At minimum, one of the following must be present:

### Required (At Least One)

| # | Folder | Pattern | Purpose |
|---|--------|---------|---------|
| 1 | **Annual Filing Memos** | `**/[COMPANY]/1.1-Annual-Filings/*.md` | Primary source — business context, financials, management commentary |
| 2 | **Investor Presentation Memos** | `**/[COMPANY]/1.2-Investor-Presentations/*.md` | Strategy, guidance, promises |
| 3 | **Financial Data** | `**/[COMPANY]/1.3-Financial-Statements/*.json` AND `*.md` | Historical financials |

### File Exclusions

**Exclude files matching these patterns** (meta-documents, not source research):
- Files containing "QC" in filename
- Files containing "Gap" in filename
- Files containing "Improve" in filename
- Files containing "Audit" in filename

### Prerequisite Check Process

1. Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default
2. Use Glob to search for files in `{RESEARCH_BASE_PATH}/[COMPANY]/` subfolders
3. Filter out excluded files (QC, Gap, Improve, Audit)
4. If NO qualifying Foundation materials exist, return:

```json
{
  "output_file_path": null,
  "years_covered": 0,
  "source_count": 0,
  "status": "failed",
  "notes": "No Foundation materials found for [COMPANY]. Required: 10-K memos, investor presentations, or financial data."
}
```

### Limitations Notice

If only 1 year of data exists, include a prominent notice in the output:

```
> ⚠️ **Limited Data:** Only 1 year of Foundation materials available.
> This overview provides a snapshot rather than a longitudinal view.
```

---

## Step 1: Read All Foundation Materials

**Only proceed here if Step 0 passes (at least one Foundation folder has materials).**

### Annual Filing Memos
```
File search pattern: {RESEARCH_BASE_PATH}/[COMPANY]/1.1-Annual-Filings/*.md
```
Read all annual filing synthesis memos. Extract:
- YAML frontmatter metrics
- Key takeaways
- Segment breakdowns
- Management commentary and promises
- Risk factors
- Financial snapshots

### Investor Presentation Memos
```
File search pattern: {RESEARCH_BASE_PATH}/[COMPANY]/1.2-Investor-Presentations/*.md
```
Read investor materials if available. Extract:
- Strategic messaging
- Guidance and targets
- Capital allocation priorities
- Management promises

### Financial Data
```
File search pattern: {RESEARCH_BASE_PATH}/[COMPANY]/1.3-Financial-Statements/*.json
File search pattern: {RESEARCH_BASE_PATH}/[COMPANY]/1.3-Financial-Statements/*.md
```
Read financial statements. Extract time series data for:
- Revenue, operating income, net income
- FCF, ROIC
- Balance sheet metrics

---

## Step 2: Build Multi-Year Analysis

### Financial Evolution

Build a table tracking core metrics across all available years:

| Metric | [Start Year] | [End Year] | CAGR | Trajectory |
|--------|--------------|------------|------|------------|
| Revenue | | | | |
| Operating Income | | | | |
| Net Income | | | | |
| FCF | | | | |
| Employees | | | | |
| ROIC | | | | |
| Op Margin | | | | |

**CAGR Calculation:**
```
CAGR = ((End Value / Start Value) ^ (1 / Years)) - 1
```

**Trajectory Descriptions:**
- Accelerating — growth rate increasing
- Steady — consistent growth
- Decelerating — growth rate decreasing
- Volatile — inconsistent
- Declining — negative growth

### Segment Mix Shift

Track how revenue composition changed over time:

| Segment | [Start Year] % | [End Year] % | Δ | Significance |
|---------|----------------|--------------|---|--------------|

Flag segments that:
- Grew from <10% to >20% (emerging driver)
- Shrank from >20% to <10% (declining relevance)
- Became majority contributor

### Management Credibility Scorecard

Score trackable promises extracted from source memos:

| Promise | Source Year | Outcome | Score |
|---------|-------------|---------|-------|
| [Promise] | FY[Year] | [Delivered/Partial/Missed/Abandoned] | +2 to -2 |

**Scoring Scale:**
| Score | Meaning |
|-------|---------|
| +2 | Exceeded promise |
| +1 | Delivered as stated |
| 0 | Partial with valid explanation |
| -1 | Missed with excuses |
| -2 | Abandoned/ignored |

**Overall Credibility Rating:**
| Total Score | Rating |
|-------------|--------|
| >+5 | HIGH |
| 0 to +5 | MODERATE |
| -5 to 0 | LOW |
| <-5 | CONCERNING |

*If no trackable promises found in source memos, state: "Credibility: Unable to assess — no trackable promises in source materials."*

### Risk Evolution Matrix

Track how risks evolved across years:

| Risk Category | [Year 1] | [Year 2] | [Year 3] | Current Status | Trend |
|---------------|----------|----------|----------|----------------|-------|
| Competitive | | | | | ↑/→/↓ |
| Regulatory | | | | | ↑/→/↓ |
| Financial | | | | | ↑/→/↓ |
| Operational | | | | | ↑/→/↓ |
| Technology | | | | | ↑/→/↓ |
| Market/Macro | | | | | ↑/→/↓ |

**Trend Arrows:**
- ↑ = Risk increasing
- → = Risk stable
- ↓ = Risk decreasing

Note risks that:
- **[NEW]** — Appeared for the first time
- **[RETIRED]** — No longer mentioned

### Key Events Timeline

Extract significant events from source memos:

| Year | Event | Impact |
|------|-------|--------|
| | | |

Include: Acquisitions, divestitures, leadership changes, new products, regulatory changes, strategic pivots.

---

## Brevity Guidelines (CRITICAL)

These rules apply to ALL sections of the output. Violating them is a validation failure.

- **Commentary = key takeaway, not table walkthrough.** After each table, write 1-2 sentences summarizing the most important insight. Do NOT walk through every row or repeat numbers already visible in the table.
- **No extra sections beyond template.** Do NOT invent sections like "Valuation Context," "Balance Sheet Snapshot," "Product Innovation Pipeline," etc. Stick strictly to the output template.
- **Key Takeaways: 60 words max per bullet, 2 sentences max.** Cut any bullet that merely restates a table row.
- **The Business: ~200 words total, 2-3 short paragraphs.** Assume the reader understands the industry. Don't explain what products do if obvious from the name.
- **Financial Narrative: 2-4 sentences.** Summarize the key story — don't walk through every metric.
- **Questions: parenthetical "why it matters"** — one sentence after the question, not a separate indented line.

---

## Step 3: Synthesize Insights

### Key Takeaways

Write 5-8 bullet points that synthesize the most important insights across all years. Each bullet should:
- Identify a multi-year pattern or trend
- Provide specific supporting data
- Answer "so what?" — why this matters for investment analysis

Focus on:
- What has improved over time?
- What has deteriorated?
- What remained consistent?
- What surprised you?
- What patterns emerged?

### The Business

Write ~200 words in 2-3 short paragraphs covering: what the company does, how it makes money, and the economic engine. Assume the reader understands the industry — don't explain what products do if obvious from the name. Do NOT add sub-sections or extra tables beyond the Segments table.

### Year Card Summary

For each fiscal year, provide a brief 3-line summary:

```
### FY[Year]
**Theme:** [One phrase capturing the year]
**Key developments:** [2-3 most significant events/changes]
**Performance:** [Revenue: $XB (+X%), Op Income: $XM (+X%)]
```

---

## Step 4: Write Output

### Output Template

Read the output template from: `.codex/skills/company-overview/references/output-template.md`

Follow the template structure when producing the final output.

### Validation Checklist

Read the validation checklist from: `.codex/skills/company-overview/references/validation-checklist.md`

Before saving, verify:
1. At least 1 Foundation material was read
2. YAML frontmatter is complete
   - Includes the formal review gate fields with QC pending and audit blocked until QC completes
3. Key Takeaways present (5-8 bullets, cross-year synthesis)
4. The Business section explains business model clearly
5. Financial Evolution table with CAGRs (math verified)
6. Source Files section lists all materials read

### Write the Memo

Write the completed memo to: [OUTPUT_PATH]

---

## Variable Time Period Guidance

| Years Available | Approach |
|-----------------|----------|
| **1 year** | Limited utility — produce overview but note limitations prominently |
| **2-3 years** | Patterns may not be established — be cautious about trajectory claims |
| **4-5 years** | Ideal — sufficient for pattern recognition |
| **6+ years** | Summarize older years briefly; focus detail on recent 3-5 years |

---

## Guidelines

**Longitudinal, Not Point-in-Time:** The value of this skill is showing *evolution* over time. Always compare across years.

**Patterns, Not Repetition:** Don't repeat facts from each year. Synthesize into trends and patterns.

**Quantified Where Possible:** Use specific numbers — CAGRs, percentage changes, mix shifts.

**Source-Grounded:** Every insight should trace back to specific source memos. Include "Source Files" section.

**Investment-Relevant:** Focus on what matters for making investment decisions.

**Dense, Not Long:** Target 3,000-4,000 words / 200-300 lines. Commentary should summarize the key takeaway from each table, not walk through every row. Do NOT add sections beyond the output template.

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written memo]",
  "years_covered": [number of fiscal years in analysis],
  "source_count": [number of source files read],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```
```
