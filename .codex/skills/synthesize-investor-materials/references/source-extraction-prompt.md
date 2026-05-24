# Investor Materials Synthesis Focused Pass Prompt

Use this reference for Codex-native source extraction during multi-file investor materials synthesis.

---

## When to Use Segment Passes

Separate extraction passes are useful when:
- Processing 5+ files from a single event
- Each file requires substantial extraction
- Files are from different presenters (CEO, CFO, segment heads)
- Parallel processing would improve efficiency

**Typical pattern:**
- Run one focused extraction pass per major file type (Strategy, Financial, Segment)
- Each extraction pass extracts to a structured intermediate format
- Main Codex run synthesizes intermediate outputs into final memo

---

## Extraction Agent Prompt

Replace placeholders in brackets with actual values:

```
You are extracting key information from an investor presentation for [COMPANY] ([TICKER]).

**Event:** [EVENT NAME]
**File:** [FILENAME]
**File Type:** [Strategy/Financial/Segment/Overview]

## Your Task

1. Read the presentation file from: [PATH_TO_FILE]
2. Extract information following the template below
3. Write extracted data to: [OUTPUT_PATH]

## Extraction Template

Return a structured extraction:

### Source Info
- File: [filename]
- Type: [Strategy/Financial/Segment/Overview]
- Slides/Pages: [count]
- Primary Focus: [1 sentence]

### Key Metrics Presented
| Metric | Value | Context | Slide |
|--------|-------|---------|-------|
| [Metric] | [Value] | [Brief context] | [#] |

### Guidance/Targets
| Metric | Target | Timeline | Specificity | Slide |
|--------|--------|----------|-------------|-------|
| [Metric] | [Value] | [When] | High/Med/Low | [#] |

### Promises (Verbatim Quotes)
| Promise | Quote | Slide |
|---------|-------|-------|
| [Description] | "[Exact words]" | [#] |

### Claims (Verbatim Quotes)
| Claim | Quote | Slide | Verifiability |
|-------|-------|-------|---------------|
| [Description] | "[Exact words]" | [#] | Strong/Mod/Weak |

### Strategic Messaging
- Core thesis: [1-2 sentences]
- Key priorities: [numbered list]
- What's new: [bullet list]

### Red Flags/Concerns
- [Any concerns noted]

### Notable Quotes
| Quote | Context | Slide |
|-------|---------|-------|
| "[Quote]" | [Why notable] | [#] |

## Extraction Guidelines

- **Verbatim quotes required** for all promises and claims
- **Slide numbers required** for all data points
- **Be specific** — numbers, not "growth" or "improvement"
- **Flag vague language** — note when management is non-specific
- **Capture what's NEW** — distinguish from known information
- **Note omissions** — what wasn't discussed that should have been

## Output Format

Write output as markdown with clear section headers.
Do not synthesize or interpret — just extract.
The main Codex run will synthesize across all file extractions.
```

---

## Synthesis Agent Prompt

After extraction passes complete, the main Codex run synthesizes:

```
You are synthesizing investor materials for [COMPANY] ([TICKER]).

**Event:** [EVENT NAME]
**Event Date:** [DATE]
**Event Type:** [investor-day/capital-markets-day/quarterly-presentation/shareholder-letter/standing-overview]

## Your Task

1. Read extraction outputs from:
   - [PATH_TO_EXTRACTION_1]
   - [PATH_TO_EXTRACTION_2]
2. Read the output template from: .codex/skills/synthesize-investor-materials/references/output-template.md
3. Read the event-type checklist from: .codex/skills/synthesize-investor-materials/references/event-type-checklists/[TYPE].md
4. Read the validation checklist from: .codex/skills/synthesize-investor-materials/references/validation-checklist.md
5. Synthesize into unified memo following template structure
6. Complete validation checklist before finalizing
7. Write final memo to: [OUTPUT_PATH]

## Output Format Requirements

### YAML Frontmatter (Required)
- Basic metadata: company, ticker, event_type, event_date, event_name
- Key metrics (if presented): revenue, operating income, net income
- Capital allocation (if discussed): buyback auth, dividend policy, M&A appetite
- Quality assessment: new_information, specificity, event_significance

### Body Section Style
The body uses a **prose-driven style** for comprehension:
- **Key Takeaways:** 5-7 narrative bullets with **bold lead-ins**
- **Source Materials:** Simple table of files analyzed
- **Strategic Messaging:** 2-3 paragraphs prose + New vs. Known table + Priorities table
- **Guidance & Targets:** Table + capital allocation commentary (prose)
- **Promises to Track:** Table with verbatim quotes and sources
- **Claims to Verify:** Table with verifiability ratings
- **Business Updates:** Prose bullets per segment
- **Red Flags & Concerns:** Prose bullets + Unanswered Questions list
- **Investment Implications:** Prose paragraphs for current/prospective holders

### Quality Requirements
- All verbatim quotes must retain source references (Slide XX)
- Guidance table must include ALL targets from ALL files
- Promises table minimum 3 entries (or explain why fewer)
- Claims must have verifiability assessment
- New vs. Known table must be completed
- Red flags consolidated from all extractions

### Synthesis Guidelines
- **Deduplication:** Combine overlapping information; prefer more specific versions
- **Token Efficiency:** Target ~2,400 tokens total
- **No tags/cross-references:** Drop the tagging system; keep content clean
- **Bold lead-ins:** Key Takeaways start with **bold phrase** followed by colon

## Output Location

Write to: [Company]/1.2-Investor-Presentations/[Event Name] - Memo - [Company] - [YYYY-MM-DD-HHMM].md
```

---

## File Processing Order

When processing multiple files, prioritize:

1. **Strategy/CEO Overview** — sets context for everything else
2. **Financial/CFO Presentation** — hard numbers and targets
3. **Segment Presentations** — depth on specific businesses
4. **Supporting Materials** — fact sheets, appendices

---

## Error Handling

**If a file is unreadable:**
- Note which file failed in extraction
- Continue with remaining files
- Flag in final memo: "Note: [filename] could not be processed"

**If extraction is minimal:**
- Some files may have little extractable content
- Note: "File contained primarily [visual/retrospective] content"
- Don't force extraction where none exists
