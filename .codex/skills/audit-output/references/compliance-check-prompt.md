# Compliance Check Prompt

You are auditing a skill's output document against its requirements. Your job is to systematically check compliance and classify any violations.

---

## Your Inputs

1. **Requirements** — The skill's requirements from:
   - SKILL.md ("Covers:" section, required sections)
   - output-template.md (section structure, table formats)
   - validation-checklist.md (pass/fail criteria)
   - industry-checklists/[industry].md (industry-specific requirements)

2. **Output Document** — The skill output being audited

3. **Industry** — The company's industry (for checklist selection)

---

## Your Task

For each requirement, determine:
- **COMPLIANT** — Requirement is fully met
- **FIXABLE** — Violation can be fixed without source documents
- **FLAG-ONLY** — Violation requires source verification to fix

---

## Classification Rules

### FIXABLE Violations (can fix autonomously)

These violations can be fixed because they don't require reading source documents:

| Violation Type | Fix Approach |
|----------------|--------------|
| **Missing "Not disclosed" statement** | Add "X: Not disclosed in 10-K" for required-but-missing items |
| **Missing YAML field** | Add field with `null` value and comment |
| **Malformed table** | Fix structure to match template |
| **Missing required section** | Add section header with placeholder text |
| **Missing topic tags** | Add `[TAG-SLUG]` where referenced in Topic Index |
| **Orphaned topic tags** | Remove from Topic Index or add reference |
| **Missing page reference** | Add "p.XX - verify" placeholder |
| **Format mismatch** | Adjust to match template format |
| **Missing Watch Items section** | Add section with "Pending assessment" placeholder |

### FLAG-ONLY Violations (cannot fix without sources)

These violations require source data to fix properly:

| Violation Type | Why Flag-Only |
|----------------|---------------|
| **Incorrect data value** | Need source to verify correct value |
| **Missing extracted content** | Content must come from source document |
| **Missing calculation** | Need source data to calculate (take rate, ROIC, etc.) |
| **Incomplete analysis** | Requires source reading to expand |
| **Unverified claim** | Must check against source |
| **Missing trend data** | Need multi-period data from source |

---

## How to Check

### Step 1: YAML Frontmatter Audit

Check all required YAML fields per the template and industry checklist:

```yaml
# Required for all
company:
ticker:
fiscal_year:
industry:
form_type:   # 10-K, 20-F, or 40-F
accounting_standard:  # GAAP or IFRS

# Financial metrics
revenue_m:
operating_income_m:
net_income_m:
fcf_m:
# ... etc based on industry

# Industry-specific (example: platform)
gmv_m:
take_rate_pct:
# ... per industry checklist
```

For each missing required field:
- If it should be "Not disclosed" → FIXABLE (add null with comment)
- If it should have a value from the source → FLAG-ONLY

### Step 2: Section Structure Audit

Check all required sections exist per output-template.md:

| Section | Check |
|---------|-------|
| Key Takeaways | 5-7 bullets with bold lead-ins |
| Business Summary | 2-3 paragraphs + segment table |
| What Changed | Bullet list of material changes |
| Management Commentary | Quote + key points |
| Financial Snapshot | P&L, Balance Sheet tables |
| Capital Allocation | Sources/uses of cash |
| Risk Factors | 3-5 bullets with ratings |
| Accounting Quality | 7-item checklist |
| Questions | 3-5 numbered questions |
| Topic Index | All tags used in document |

For missing sections:
- If section header is missing → FIXABLE (add section skeleton)
- If section content is thin/incomplete → FLAG-ONLY (needs source)

### Step 3: Table Format Audit

Check tables match required format:

**P&L Table Required Rows:**
- Revenue
- Gross Profit / Gross Margin
- Operating Income
- Net Income
- EPS (Diluted)
- Operating Margin
- ROIC
- Cash from Operations
- FCF / FCF Conversion

**Balance Sheet Required Rows:**
- Total Assets
- Total Debt
- Net Debt / EBITDA
- Interest Coverage
- Shareholders' Equity

For missing table rows:
- If can be stated as "Not disclosed" or "Not applicable" → FIXABLE
- If requires calculation from source → FLAG-ONLY

### Step 4: Industry-Specific Audit

Check industry checklist requirements:

**Example: Platform/OTA Industry**
- [ ] GMV / Gross Bookings in YAML
- [ ] Take Rate in YAML
- [ ] Revenue vs GMV growth differential stated
- [ ] Watch Items section populated

**Example: Insurance Industry**
- [ ] Combined ratio components table
- [ ] GPW and NPW by segment
- [ ] Investment portfolio metrics
- [ ] Reserve development

For each industry requirement:
- Check if present in output
- Classify violation per rules above

### Step 5: Cross-Reference Audit

Check consistency between sections:
- Topic Index tags all appear in body with `[TAG-SLUG]`
- Financial figures consistent between YAML and tables
- Promises table has page references
- Risk factors have probability/impact ratings

---

## Output Format

Return your findings in this exact format:

```markdown
## Compliance Summary

| Metric | Count |
|--------|-------|
| Requirements Checked | X |
| Compliant | X |
| Fixable Violations | X |
| Flag-Only Violations | X |

---

## Violations Found

### V1: [Brief Description]

- **Classification:** FIXABLE
- **Requirement:** [Quote from checklist/template]
- **Current State:** [What's in output or "Missing"]
- **Required State:** [What should be there]
- **Fix:** [Specific edit instruction]
- **Location:** [Section name or "YAML frontmatter"]

---

### V2: [Brief Description]

- **Classification:** FLAG-ONLY
- **Requirement:** [Quote from checklist/template]
- **Current State:** [What's in output or "Missing"]
- **Required State:** [What should be there]
- **Why Not Fixable:** [Explanation - e.g., "Requires take rate calculation from GMV and revenue figures in source"]
- **Location:** [Section name]

---

[Continue for all violations...]

## Compliant Items (Summary)

The following requirements were met:
- [List key compliant areas]
```

---

## Important Guidelines

1. **Be systematic** — Check every requirement, don't skip any
2. **Be precise** — Exact location and fix instructions
3. **Be conservative** — When in doubt, classify as FLAG-ONLY
4. **Don't fabricate** — Never suggest adding made-up data
5. **Respect the output** — Note what's done well, not just violations

---

## Example Violations

### Example FIXABLE Violation

```markdown
### V3: Missing unit economics disclosure statement

- **Classification:** FIXABLE
- **Requirement:** "For data genuinely not in 10-K: 'Not disclosed in 10-K'"
- **Current State:** No mention of unit economics in Business Summary
- **Required State:** Statement acknowledging unit economics not disclosed
- **Fix:** Add sentence in Business Summary: "Unit economics (CAC, LTV, payback period): Not disclosed in 10-K."
- **Location:** Business Summary section, after segment table
```

### Example FLAG-ONLY Violation

```markdown
### V5: Missing take rate trend analysis

- **Classification:** FLAG-ONLY
- **Requirement:** "Take Rate with YoY trend" per platform industry checklist
- **Current State:** YAML has `take_rate_pct: 18.2` but no trend comparison
- **Required State:** Take rate with prior year comparison showing trend direction
- **Why Not Fixable:** Requires prior year take rate calculation from source (GMV ÷ Revenue for both years)
- **Location:** Key Takeaways or Financial Snapshot
```
