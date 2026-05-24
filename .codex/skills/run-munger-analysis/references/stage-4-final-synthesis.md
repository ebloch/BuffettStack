# Stage 4: Final Synthesis

**Purpose:** Finalize all scores, resolve tensions, apply Holistic Adjustment, and produce the final Munger Analysis memo.

**Input Documents (~4K tokens):**
- Working Analysis v3 only (no new source documents)

**Output:** Final Munger Analysis memo (saved to file)

---

## Instructions

You are conducting Stage 4 of a 4-stage Munger Analysis. Your role is to synthesize all prior stage findings into a final memo, resolve any tensions, and ensure the verdict accurately reflects the analysis.

### Document to Read

**Working Analysis v3** — From Stage 3 output (in conversation context)

This contains:
- All 7 category scores with evidence
- Complete "Why Not Higher?" for each category
- Tensions registry from all stages
- Holistic adjustment recommendation

### What to Do

#### 1. Score Reconciliation (REQUIRED)

Before writing the memo, review each score and ask:

| Category | Score | Gut Check |
|----------|-------|-----------|
| Circle of Competence | [From v3] | Does this feel right? |
| Moat | [From v3] | Is this appropriate given evidence? |
| Management | [From v3] | Does credibility data support this? |
| Predictability | [From v3] | Short-term vs. long-term aligned? |
| Financial Strength | [From v3] | Any concerns missed? |
| Long-Term | [From v3] | Tailwinds vs. headwinds balanced? |
| Lollapalooza | [From v3] | Is there really a virtuous cycle? |

**If any score feels wrong:**
- Review the evidence from Working Analysis v3
- Consider if tensions affected the score
- Adjust if justified, with explanation

#### 2. Tension Resolution

Review the Tensions Registry from Working Analysis v3.

For each tension:
- **If resolved:** Note how it was resolved
- **If unresolved:** Determine impact on final verdict
  - May justify Holistic Adjustment
  - May require qualitative caveat in memo

#### 3. Holistic Adjustment

Apply the Holistic Adjustment (0 / -1 / -2) based on:
- Cross-cutting concerns not captured in category scores
- Gut check vs. mechanical score
- Compounding risks across categories
- Unresolved tensions

| Adjustment | When to Apply |
|------------|---------------|
| 0 | Category scores accurately reflect overall quality |
| -1 | Material cross-cutting concern OR gut says "too high" |
| -2 | Significant compounding risk OR multiple soft concerns |

**Document the rationale clearly.**

#### 4. Calculate Final Score and Verdict

**Subtotal:** Sum of 6 category scores (Circle of Competence is assessment, not scored)
**Final Score:** Subtotal + Holistic Adjustment

| Score Range | Verdict |
|-------------|---------|
| +9 to +12 | EXCEPTIONAL |
| +5 to +8 | STRONG |
| +1 to +4 | ACCEPTABLE |
| -4 to 0 | WEAK |
| -12 to -5 | AVOID |

**Calibration check:**
- EXCEPTIONAL should be rare
- Most high-quality businesses land at STRONG
- If giving EXCEPTIONAL, verify no +2 score has substantive "Why Not Higher?"

#### 5. Final Gut Check

Before writing the memo, answer:

| Check | Answer |
|-------|--------|
| Does the verdict match my gut? | Yes / No |
| What would change my mind? | [1-2 things] |
| Compared to other [VERDICT] companies, does this belong? | Yes / No |

**If gut and mechanical score disagree:** The Holistic Adjustment exists for this. Go back and adjust if needed.

#### 6. Write Final Memo

Use the `output-template.md` in this skill directory.

The memo should:
- Reflect all findings from Working Analysis v3
- Incorporate any score adjustments made in Stage 4
- Resolve or acknowledge tensions
- Provide clear rationale for the Holistic Adjustment
- Answer "Would Munger Buy This?" with conviction

### Output Location

Save the final memo to:
```
{RESEARCH_BASE_PATH}/[Company]/3-Synthesis/3.2-Munger-Analysis/Munger Analysis - Memo - [Company] - [YYYY-MM-DD-HHMM].md
```

**Research Base:** Resolve the research root from `RESEARCH_BASE_PATH`, `.codex/settings.local.json`, or the repo-local `research/` default

---

## Quality Checklist

Before completing, verify:

- [ ] All 7 categories have scores and assessments
- [ ] Every score has "Why Not Higher?" populated (or "N/A" if +2)
- [ ] Summary table matches detailed sections
- [ ] Holistic Adjustment has clear rationale
- [ ] Final Score calculation is correct
- [ ] Verdict matches the score range
- [ ] "Would Munger Buy This?" is answered definitively
- [ ] Sources list all Working Analysis stages and original research files
- [ ] Key Strengths and Key Concerns are populated (3 each)
- [ ] One-Sentence Thesis is clear and specific

---

## Key Principles

1. **Synthesis, not copy-paste:** Transform Working Analysis findings into polished prose
2. **Conviction required:** Don't hedge excessively. Make a call.
3. **Tensions acknowledged:** If unresolved, note them in the memo rather than hiding
4. **Calibration matters:** Compare to your mental model of what EXCEPTIONAL vs. STRONG means
5. **Munger lens:** Would Munger actually want to own this? Answer honestly.
6. **Audit trail:** List all Working Analysis stages in Sources for transparency
