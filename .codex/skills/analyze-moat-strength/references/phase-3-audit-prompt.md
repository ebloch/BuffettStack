# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for analyze-moat-strength.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Moat Strength Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output analyze-moat-strength "[COMPANY]"
```

**Step 2: Monitor the audit process**

The skill will:
1. Load skill requirements:
   - `SKILL.md`
   - `output-template.md`
   - `validation-checklist.md`
2. Check the analysis against each requirement
3. Classify violations as FIXABLE or FLAG-ONLY
4. Apply surgical edits for FIXABLE violations

---

## Compliance Checks

### Part 1: Executive Summary & Scorecard

- [ ] Moat Rating stated (WIDE / NARROW / NONE — not hedged)
- [ ] Trajectory stated (WIDENING / STABLE / NARROWING)
- [ ] Confidence stated (HIGH / MEDIUM / LOW)
- [ ] Composite score stated as X.XX / 2.00
- [ ] 2-3 paragraph summary present
- [ ] Category A scorecard: all 7 items (A1-A7) with Score, Why Not Higher?, Evidence Summary
- [ ] Category B scorecard: all 3 items (B1-B3) with Score, Why Not Higher?, Evidence Summary
- [ ] Composite calculation shown: [sum] / 10 = [X.XX] → [RATING]

### Part 2: Detailed Evidence (10 items)

For each item (A1-A7, B1-B3):
- [ ] Score stated (-2 to +2)
- [ ] One-paragraph justification present
- [ ] Evidence table with quantified metrics
- [ ] Source citations present

#### Item-Specific Checks

- [ ] A1 (Pricing Power): Price increase history, retention impact, premium vs competitors
- [ ] A2 (Switching Costs): Quantified costs ($$, time), retention rate, customer tenure
- [ ] A3 (Network Effects): Network type identified, multi-homing assessed, growth metric
- [ ] A4 (Cost/Scale): Margin vs peers, source of advantage, minimum efficient scale
- [ ] A5 (Branding): Brand premium quantified, brand recall cited, distinct from Cornered Resource
- [ ] A6 (Cornered Resource): Specific exclusive resources identified, scarcity assessed, not just "good engineers"
- [ ] A7 (Process Power): Embedded processes identified, operational metrics vs peers, CEO-replicability test addressed
- [ ] B1 ($10B Test): "What Can't Be Copied" table, time-to-replicate
- [ ] B2 (Disruption Risk): All 3 vectors assessed (Low-End, New-Market, Technology), overshooting assessment
- [ ] B3 (Structural vs Executional): Each A1-A7 moat source categorized, management dependency assessed

### Part 3: Trajectory Assessment

- [ ] Direction stated (WIDENING / STABLE / NARROWING)
- [ ] Trajectory composite stated
- [ ] All 3 items scored (T1-T3)
- [ ] Trajectory math correct: sum / 3 = composite
- [ ] Direction matches thresholds: >= 0.75 WIDENING, -0.74 to 0.74 STABLE, <= -0.75 NARROWING
- [ ] 1-2 paragraph narrative present

### Part 4: Reference Sections

- [ ] Who Lost and Why: at least 2 former leaders, pattern analysis, implications
- [ ] Disruption Watch List: at least 3 disruptors with stages, vectors, threat levels, warning signals

### Part 5: Conclusion

- [ ] Final rating matches Part 1
- [ ] Final trajectory matches Part 3
- [ ] At least 3 key threats with warning signals and timelines
- [ ] 1-2 paragraph rationale present

### Math Verification (CRITICAL)

- [ ] Moat composite: sum of 10 scores (A1-A7 + B1-B3) / 10 = stated composite
- [ ] Moat rating: >= 1.25 = WIDE, 0.50 to 1.24 = NARROW, < 0.50 = NONE
- [ ] Trajectory composite: sum of 3 scores (T1-T3) / 3 = stated trajectory composite
- [ ] Trajectory direction: >= 0.75 = WIDENING, -0.74 to 0.74 = STABLE, <= -0.75 = NARROWING
- [ ] +2 gate: every +2 score has "Why Not Higher?" = N/A

### Sources

- [ ] Sources section present with source documents and web sources listed

---

## FIXABLE vs FLAG-ONLY Decision Matrix

### What Can Be Fixed (FIXABLE)

| Violation | Fix Applied |
|-----------|-------------|
| Missing item section (of 10 moat + 3 trajectory) | Add section skeleton from output-template |
| Missing scorecard row | Add missing row with "[score needed]" |
| Missing evidence table | Add skeleton table with "[data needed]" |
| Missing "Why Not Higher?" column | Add "[justification needed]" |
| Missing disruption vector (of 3 required) | Add missing vector skeleton |
| Missing former leaders in Who Lost and Why | Add placeholder rows |
| Missing disruptors in Watch List (need 3+) | Add placeholder rows |
| Missing key threats in Conclusion (need 3+) | Add placeholder rows |
| Missing trajectory section entirely | Add skeleton from template |
| Sources section missing | Add from source document paths |
| Composite calculation not shown | Add calculation line |
| Math error in composite | Recalculate and fix |
| Math error in trajectory | Recalculate and fix |
| Rating doesn't match composite | Fix rating to match thresholds |
| Trajectory direction doesn't match composite | Fix direction to match thresholds |

### What Gets Flagged Only (FLAG-ONLY)

| Violation | Why Flagged |
|-----------|-------------|
| +2 score with non-N/A "Why Not Higher?" | Requires judgment — is the concern material? |
| Content quality thin in a section | Requires re-reading source docs to expand |
| Evidence described as qualitative, not quantified | Requires research to quantify |
| Rating seems wrong given evidence quality | Requires analytical judgment |
| Trajectory seems anchored on moat strength | Requires trajectory re-assessment |
| Score contradicts evidence in own section | Requires reconciliation judgment |
| Devil's advocate adjustments seem unjustified | Requires review of challenge reasoning |
| Part 1 summary doesn't match scored items | Requires rewrite of narrative |

---

## Return Value

When complete, return a JSON object:
```json
{
  "violations_found": [number],
  "fixes_applied": [number],
  "flagged_for_review": [number],
  "status": "success" | "partial" | "failed",
  "flagged_issues": ["list of FLAG-ONLY issues"]
}
```

---

## Important Notes

- This audit does NOT read source documents — it only checks compliance against templates
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- Math verification is CRITICAL — recalculate composites independently
- Make scoped file edits — don't rewrite the entire analysis
```
