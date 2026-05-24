# Phase 1: Investor Materials Synthesis Prompt

Use this reference for the synthesis pass for synthesize-investor-materials.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are synthesizing investor materials for [COMPANY] ([TICKER]).

**Input Mode:** [MODE]
**Event Specifier:** [EVENT_SPECIFIER]
**Direct Files:** [FILE_PATHS]

**Output Directory:** [OUTPUT_DIR]
**Timestamp:** [TIMESTAMP]

---

## Your Task

Complete the full investor materials synthesis workflow:

### Step 1: Locate Materials

**Based on input mode:**

| Mode | Action |
|------|--------|
| `most-recent` | Find IR page, identify most recent investor presentation |
| `last-N` | Find IR page, identify N most recent presentations |
| `specific-event` | Find IR page, locate specific event materials |
| `direct-file` | Use provided file paths directly |

**Finding IR page (if needed):**
Use web search query: `"[COMPANY] investor relations presentations"`

Common patterns:
- `investor.company.com`
- `company.com/investors`
- `ir.company.com`

### Step 2: Download Materials

Download PDFs to `/tmp`:
```bash
curl -L -o "/tmp/[company]-[event]-[desc].pdf" "[url]"
```

**Limits:**
- Most recent event: max 5 files
- Last N events: max 5 files per event
- Specific event: max 10 files
- Direct input: all provided files

**CRITICAL:** Track all downloaded PDF paths — these are needed for Phase 2 QC.

### Step 3: Identify Event Type

Classify the event:

| Event Type | Characteristics |
|------------|-----------------|
| `investor-day` | Multi-year strategy, TAM/SAM, management showcase |
| `capital-markets-day` | Financial targets, capital allocation, efficiency |
| `quarterly-presentation` | Results vs. expectations, near-term guidance |
| `shareholder-letter` | Philosophy, retrospective, vision |
| `standing-overview` | Periodic deck, not tied to specific event |

Read the appropriate checklist:
```
.codex/skills/synthesize-investor-materials/references/event-type-checklists/[event-type].md
```

### Step 4: Read and Classify Materials

Read each PDF from the workspace. For each file, classify:

| Type | Description |
|------|-------------|
| Strategy | CEO/corporate overview, long-term vision |
| Financial | CFO presentation, guidance, targets |
| Segment | Business unit deep-dives |
| Overview | Fact sheets, one-pagers |

### Step 5: Extract Key Information

For each document, extract with **mandatory source references**:

**Strategic Messaging:**
- Management's thesis about the company's future
- Strategic priorities and initiatives
- Competitive positioning claims
- What's NEW vs. previously communicated

**Financial Information:**
- Revenue/earnings guidance with timelines — `(Slide XX)`
- Margin targets — `(Slide XX)`
- Capital allocation priorities
- Buyback/dividend policies

**Operational Details:**
- Segment performance and outlook
- Key initiatives by business unit
- Capacity expansions, product launches

**Promises and Commitments (CRITICAL):**
- Capture **VERBATIM quotes** for anything trackable
- Note the source: `(Slide XX)`
- Categorize: Financial / Operational / Strategic / Capital Allocation
- Minimum 3 trackable promises required

**Claims to Verify:**
- Competitive positioning claims
- Market share assertions
- Assess verifiability: Strong / Moderate / Weak

### Step 6: Read Templates

Read required templates:
- Output template: `.codex/skills/synthesize-investor-materials/references/output-template.md`
- Validation checklist: `.codex/skills/synthesize-investor-materials/references/validation-checklist.md`

### Step 7: Synthesize into Unified Memo

Create a single memo following the output template structure:

**YAML Frontmatter (Required):**
- type, company, ticker, event_type, event_date, event_name
- metrics (if presented)
- capital (if discussed)
- quality (new_information, specificity, event_significance)

**Body Sections (Prose-Driven):**
1. Key Takeaways — 5-7 narrative bullets with **bold lead-ins**
2. Source Materials — table of files analyzed
3. Strategic Messaging — prose + New vs. Known table + Priorities table
4. Guidance & Targets — table + capital allocation commentary
5. Promises to Track — verbatim quotes table
6. Claims to Verify — verifiability assessment table
7. Business Updates by Segment — prose bullets
8. Red Flags & Concerns — prose bullets + Unanswered Questions
9. Investment Implications — prose for current/prospective holders

### Step 8: Complete Validation Checklist

**MANDATORY:** Complete ALL validation passes before writing final memo:
- A: Event type verified
- B: YAML frontmatter complete
- C: Key Takeaways quality verified
- D: Promises extracted (min 3)
- E: Claims assessed
- F: Guidance table complete
- G: New vs. Known assessed
- H: Red flags identified
- I: Investment implications completed
- J: Editorial language checked

### Step 9: Write Output

Write memo to:
```
[OUTPUT_DIR]/[Event Name] - Memo - [Company] - [TIMESTAMP].md
```

### Step 10: Determine Event Name

Extract or construct the event name:
- Investor Day: "[Year] Investor Day"
- Capital Markets Day: "[Year] Capital Markets Day"
- Quarterly: "Q[N] [Year] Earnings Presentation"
- Shareholder Letter: "[Year] Annual Letter"
- Standing Overview: "[Month] [Year] Overview"

---

## Output Format Requirements

### YAML Frontmatter (REQUIRED)

Every memo MUST start with valid YAML frontmatter containing:
- Basic metadata: company, ticker, event_type, event_date, event_name, synthesis_date
- Formal review gate fields: `formal_qc_run: false`, `formal_audit_run: false`, `qc_status: pending`, `audit_status: blocked_until_qc_complete`, `qc_completed_at: null`, `audit_completed_at: null`, `qc_result: null`, `audit_result: null`
- Key metrics presented (if any)
- Capital allocation (if discussed)
- Quality assessment ratings

### Number Formats

- Tables: M suffix, no $ (e.g., `4272M`)
- Prose: Full currency (e.g., `$4.3 billion`)
- Percentages: One decimal (e.g., `21.4%`)
- Growth targets: Sign prefix (e.g., `+15%`)

### Quality Requirements

- **Source References:** ALL quotes MUST include slide references `(Slide XX)`
- **Promises to Track:** Minimum 3 with verbatim quotes
- **Claims to Verify:** Include verifiability rating
- **New vs. Known:** Must be completed
- **Bold Lead-ins:** Key Takeaways start with **bold phrase** followed by colon

---

## Tool Usage (CRITICAL)

- **Bash:** Use for downloading PDFs with `curl -L -o ...`
- **Read:** Use for reading PDFs, template files, and checklists
- **Write:** Use for saving the output memo
- **Web search:** Use for finding IR page and materials

---

## Return Value

When complete, return a JSON object:
```json
{
  "output_file_path": "[path to written memo]",
  "event_type": "[detected event type slug]",
  "event_name": "[Event Name as used in filename]",
  "pdf_paths": [
    "/tmp/company-file1.pdf",
    "/tmp/company-file2.pdf"
  ],
  "status": "success" | "partial" | "failed",
  "notes": "[any issues encountered]"
}
```

The `pdf_paths` list is CRITICAL — Phase 2 QC will use these to re-read source documents.
```
