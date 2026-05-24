# Phase 2: Quality Control Prompt

Use this reference for the QC pass for analyze-competitive-landscape.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing quality control on a Competitive Landscape Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

**Source Documents (for re-reading):**
- 10K Synthesis Memos: [SOURCE_MEMO_PATHS]
- Scuttlebutt Analysis: [SCUTTLEBUTT_PATH]

---

## CRITICAL: Skill Distinction

**You are running `$quality-control`, NOT `$audit-output`.** These are different skills:

| Skill | What It Does |
|-------|-------------|
| `$quality-control` | Re-reads source docs (10K memos + scuttlebutt) to find CONTENT gaps, then edits documents in-place |
| `$audit-output` | Checks compliance against templates (no source reading), then edits documents in-place |

**DO NOT** confuse these. This phase uses `$quality-control` which:
- Re-reads the original 10K synthesis memos AND scuttlebutt analysis
- Finds missing content that exists in sources
- Surgically edits the output document(s) to fill gaps — does NOT save a separate report file

---

## Your Task

Run the quality-control skill on the competitive landscape analysis to identify and fix content gaps.

**Step 1: Invoke the quality-control skill**
```
$quality-control analyze-competitive-landscape "[COMPANY]"
```

**Step 2: Provide source document paths**

The QC skill will need to re-read the source documents. There are TWO source types:

**10K Synthesis Memos:**
```
[SOURCE_MEMO_PATHS]
```

**Scuttlebutt Analysis:**
```
[SCUTTLEBUTT_PATH]
```

Read all source documents from the workspace to extract facts for comparison.

**Step 3: Monitor the QC process**

The skill will:
1. Re-read ALL 10K synthesis memos from the workspace
2. Re-read the scuttlebutt analysis from the workspace
3. Compare extracted content vs. what's in the analysis
4. Identify gaps (missing competitors, unsourced claims, thin analysis)
5. Surgically edit the analysis to fill gaps

---

## Quality Focus Areas for Competitive Landscape

Pay special attention to these competitive-landscape-specific issues:

### Market Share Accuracy

| Check | What to Verify |
|-------|----------------|
| Market share sourced | Every market share % cites a source or is marked "[est.]" |
| No tildes | No "~70%" — use "70% [est.]" instead |
| Arithmetic verified | If claiming "top 3 = X%", sum of individual shares = X% |
| Historical consistency | Market share trends (5yr/10yr ago) directionally match source narrative |

### CAGR Quality

| Check | What to Verify |
|-------|----------------|
| Single figures | No ranges like "4-6% CAGR" — must be single number |
| Year ranges present | Every CAGR includes "(FY20XX-FY20XX)" |
| No tildes | No "~25% CAGR" — must be calculated or sourced |
| Internal consistency | Same company's CAGR matches everywhere it appears (profile, table, footnotes) |
| COVID normalization | Industries impacted by COVID note distortion if CAGR spans 2020-2021 |

### Competitor Profile Completeness

| Check | What to Verify |
|-------|----------------|
| 3-5 profiles | At least 3 competitors profiled in depth |
| Financial depth | Each profile includes revenue, margins, ROIC, 5yr CAGR |
| Geographic focus | Each profile explicitly states geographic focus (regions/countries) |
| Customer focus | Each profile explicitly states customer segment focus |
| Management quality | Each profile includes brief management assessment |
| Recent moves | Each profile includes recent strategic moves (M&A, products, market entry) |

### Source Document Alignment

| Check | What to Verify |
|-------|----------------|
| Competitors from 10K | All competitors mentioned in 10K risk factors are captured in analysis |
| Competitive claims verified | Management's competitive positioning claims from 10K are addressed |
| Scuttlebutt integrated | Customer/employee perspectives on competitors incorporated |
| Risk factors reflected | Competitive risks from 10K appear in appropriate sections |
| Multi-year context | Historical competitive shifts visible from reading multiple 10K years are captured |

### Value Chain & Porter's Forces

| Check | What to Verify |
|-------|----------------|
| All value chain stages | Complete chain from inputs to end customer |
| Vertical integration present | Subsection explicitly discusses integration dynamics |
| All 5 forces rated | Each force has Low/Moderate/High rating |
| Force evidence | Each rating supported by evidence, not just assertion |
| Summary table present | Five Forces summary table with all 5 rows |
| Industry attractiveness rated | Overall attractiveness with justification |

### Emerging Threats Coverage

| Check | What to Verify |
|-------|----------------|
| Tech giants assessed | At least Amazon and Google considered |
| Private/VC assessed | Startup and VC-backed threats evaluated |
| International assessed | Foreign competitor threats evaluated |
| Converging industries | Adjacent industry expansion risks evaluated |
| Summary table present | Threat summary table with probability, timeline, severity |

---

## Gap Classification

Gaps should be classified as:

| Classification | Definition | Examples |
|---------------|------------|----------|
| **CRITICAL** | Undermines the analysis | Wrong market share data, missing major competitor, fabricated data point |
| **HIGH** | Reduces usefulness | Thin competitor profiles (missing financials), missing source citations, incomplete Porter's analysis |
| **MINOR** | Nice-to-have enhancement | Additional context, formatting improvements, supplementary data |

Focus on CRITICAL and HIGH gaps. MINOR gaps can be noted but don't require fixes.

---

## Re-Reading Source Documents

### From 10K Synthesis Memos, extract:
- Competitors explicitly named in risk factors or competitive discussion
- Market positioning claims by management
- Revenue breakdown by segment/geography
- Risk factors related to competition
- Changes in competitive language across years (if multiple memos)

### From Scuttlebutt Analysis, extract:
- Customer views on competitive alternatives
- Employee perspectives on company vs. competitors
- Partner/supplier market dynamics insights
- Grassroots competitive intelligence

Compare these extractions against the analysis to identify:
- Missing competitors that 10K explicitly names
- Competitive claims from 10K not addressed
- Scuttlebutt insights not integrated
- Historical competitive shifts not captured

---

## Return Value

When complete, return a JSON object:
```json
{
  "gaps_found": [number],
  "gaps_addressed": [number],
  "status": "success" | "partial" | "failed",
  "remaining_issues": ["list of unresolved issues if any"]
}
```

---

## Important Notes

- You have fresh context — no anchoring on the original synthesis
- Focus on what's MISSING or WRONG, not reformatting what exists
- If the QC skill identifies issues it cannot fix (need source verification), note them in the return value
- Maximum 3 iteration loops within the QC skill
```
