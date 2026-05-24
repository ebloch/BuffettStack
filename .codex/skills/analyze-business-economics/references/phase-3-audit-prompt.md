# Phase 3: Compliance Audit Prompt

Use this reference for the audit pass for analyze-business-economics.

---

## Prompt Template

Replace placeholders in brackets with actual values:

```
You are performing a compliance audit on a Business Economics Analysis.

**Context:**
- Company: [COMPANY]
- Analysis Path: [MEMO_PATH]
- Industry: [INDUSTRY] (or "none" if no industry checklist was used)
- Industry Checklist: [INDUSTRY_CHECKLIST_PATH] (or "N/A" if none)

---

## Your Task

Run the audit-output skill to check the analysis against skill requirements and fix compliance violations.

**Step 1: Invoke the audit-output skill**
```
$audit-output analyze-business-economics "[COMPANY]"
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

## Audit Focus Areas for Business Economics

### What Can Be Fixed (FIXABLE)

These violations can be fixed autonomously because they don't require source verification:

| Violation | Fix Applied |
|-----------|-------------|
| Quick Reference wrong questions | Replace with exact 6 template questions |
| Missing "; [concern threshold]" in benchmark | Add placeholder: "[concern threshold needed]" |
| Missing "[source]" in Owner's Earnings | Add placeholder: "[source needed]" |
| Missing Quirk-to-Calculation table | Add skeleton table with placeholder rows |
| Missing benchmark range for High/Medium multiple | Add placeholder: "[benchmark range needed]" |
| Missing GAAP Issues section headers | Add section headers with placeholder text |
| Missing "Red Flags That Aren't" section | Add section header |
| Format violations | Fix table structure, section headers |

### What Gets Flagged Only (FLAG-ONLY)

These violations are documented but NOT fixed because they require source data:

| Violation | Why Flagged |
|-----------|-------------|
| Incorrect Owner's Earnings dollar amounts | Needs 10K to verify correct value |
| Incomplete quirk mapping | Requires understanding of all quirks |
| Wrong business model classification | Needs source to verify |
| Benchmark values incorrect | Needs industry research to fix |
| Missing quirk examples | Content must come from 10K |
| Thin analysis sections | Requires source reading to expand |

---

## Compliance Checks

### Executive Summary

- [ ] Quick Reference table uses **exactly the 6 template questions**:
  1. "What type of business?"
  2. "What's the key metric?"
  3. "What's misleading in GAAP?"
  4. "What multiple to use?"
  5. "Who are true peers?"
  6. "Biggest analytical mistake?"
- [ ] At least 2 quirks in "The Big Quirks" section
- [ ] At least 3 metrics in "What to Focus On"
- [ ] At least 2 metrics in "What to Ignore"

### Section 3: Key Accounting Quirks

- [ ] At least 2 quirks documented
- [ ] Each quirk has: What, Distortion, Adjustment
- [ ] At least 1 quirk references specific GAAP treatment

### Section 4: Metrics That Matter

- [ ] At least 5 metrics in table
- [ ] Each metric has "Why It Matters" explanation
- [ ] Each metric has "Where to Find It" source
- [ ] **CRITICAL:** Each benchmark has BOTH good AND concern thresholds
  - Format: ">85% strong; <78% signals pricing erosion"
  - NOT: "15+ for large cap" (missing concern threshold)
- [ ] Primary KPIs ranked 1-2-3

### Section 5: Metrics to Ignore

- [ ] At least 2 misleading metrics
- [ ] GAAP Net Income Issues section present
- [ ] GAAP Cash Flow Issues section present
- [ ] Standard Ratio Assessment table present

### Section 6: Common Mistakes

- [ ] At least 2 mistakes in table
- [ ] At least 1 "Red Flag That Isn't" OR "Green Flag That Isn't"

### Section 7: Peer Selection

- [ ] At least 2 true comparables
- [ ] At least 1 false comparable
- [ ] "Best Comparables for Valuation" list

### Section 8: Valuation Implications

- [ ] At least 2 preferred valuation methods
- [ ] Multiples Assessment table with at least 4 multiples
- [ ] **CRITICAL:** Benchmark Range filled for every High/Medium multiple
  - Format: "<20x cheap, 20-28x typical, >30x expensive"
  - Use "N/A" only for Avoid/Low ratings
- [ ] Owner's Earnings calculation with dollar amounts
- [ ] All Owner's Earnings figures sourced or marked [EST]
- [ ] All figures from same fiscal year
- [ ] **CRITICAL:** Quirk-to-Calculation Mapping table present
- [ ] Every Section 3 quirk appears in mapping table

---

### Industry Compliance (If Checklist Loaded)

**Only apply these checks if `[INDUSTRY]` is not "none".**

If an industry checklist was used, read the checklist and verify compliance:

| Check | Classification | Description |
|-------|----------------|-------------|
| Missing required industry metric | FLAG-ONLY | A metric marked REQUIRED in checklist is absent from Section 4 |
| Missing required quirk | FLAG-ONLY | A quirk listed under "Required Quirks" is absent from Section 3 |
| Wrong valuation method | FLAG-ONLY | Primary valuation method contradicts checklist guidance |
| Industry benchmark mismatch | FLAG-ONLY | Benchmark ranges significantly deviate from checklist without explanation |

**For Insurance Companies Specifically:**

| Check | What to Flag |
|-------|--------------|
| Combined Ratio missing | Section 4 lacks Combined Ratio metric |
| Loss/Expense ratio missing | Section 4 lacks separate Loss Ratio and Expense Ratio |
| Investment Yield missing | Section 4 lacks Investment Yield or NII/Assets calculation |
| ROE vs COE missing | Section 4 lacks ROE vs. Cost of Equity spread analysis |
| Reserve Development missing | Section 3 lacks PYD/reserve estimation quirk |
| Float Economics missing | Section 3 lacks float accounting quirk |
| P/B not primary method | Section 8 uses P/E or EV/EBITDA as primary instead of P/B |

**Industry compliance violations are FLAG-ONLY** — they require content knowledge to fix properly.

---

## FIXABLE vs FLAG-ONLY Decision Matrix

| Check | If Missing/Wrong | Classification | Fix Action |
|-------|------------------|----------------|------------|
| Quick Reference questions | Wrong text | FIXABLE | Replace with exact questions |
| Benchmark format | Missing concern threshold | FIXABLE | Add "; [concern needed]" |
| Owner's Earnings sources | Missing citation | FIXABLE | Add "[source needed]" |
| Quirk-to-Calculation table | Missing entirely | FIXABLE | Add skeleton table |
| Multiple benchmark ranges | Missing for High/Medium | FIXABLE | Add "[verify range]" |
| GAAP Issues headers | Section missing | FIXABLE | Add header + placeholder |
| Owner's Earnings amounts | Wrong dollar value | FLAG-ONLY | Note for QC |
| Quirk mapping | Incomplete mappings | FLAG-ONLY | Note for QC |
| Business model | Wrong classification | FLAG-ONLY | Note for QC |
| Benchmark values | Incorrect numbers | FLAG-ONLY | Note for QC |

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

- This audit does NOT read source documents — it only checks compliance
- FLAG-ONLY issues should be passed to user for manual review
- All FIXABLE violations should be addressed before completing
- The analysis should pass all format/structure checks after this phase
- Make scoped file edits — don't rewrite the entire analysis
```
