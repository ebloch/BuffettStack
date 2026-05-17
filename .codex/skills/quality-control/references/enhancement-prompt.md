# Enhancement Prompt

You are executing a surgical edit to improve an investment research document. You have been given a specific gap to address and the source content to incorporate.

---

## Your Task

1. **Read the source excerpt** — Understand the content that needs to be added
2. **Locate the target section** — Find where in the document this content belongs
3. **Generate the enhancement** — Write the missing content in the document's style
4. **Apply the edit** — Surgically update the document
5. **Verify** — Confirm the edit was applied cleanly

---

## Context Provided

### Document Being Enhanced
**File Path:** `{{OUTPUT_FILE_PATH}}`

**Current Content:**
```markdown
{{OUTPUT_DOCUMENT_CONTENT}}
```

### Gap to Address
```
{{GAP_DESCRIPTION}}
```

### Source Content to Incorporate
```
{{SOURCE_CONTENT}}
```

### Edit Instructions
- **Edit Type:** {{EDIT_TYPE}} (ADD / EXPAND / CORRECT)
- **Target Section:** {{TARGET_SECTION}}
- **Specific Instructions:** {{EDIT_INSTRUCTIONS}}

### Style Requirements
```
{{STYLE_REQUIREMENTS}}
```

---

## Instructions by Edit Type

### ADD: Adding New Content

When adding content that doesn't exist in the document:

1. Identify the correct location (after which section/paragraph)
2. Write the new content matching the document's:
   - Heading hierarchy
   - Formatting conventions (tables, bullets, etc.)
   - Tone and voice
   - Citation style
3. Edit the document to insert the new content
4. Ensure smooth transitions with surrounding content

**Example:**
```
old_string: "## Section A\n\n[Content]\n\n## Section B"
new_string: "## Section A\n\n[Content]\n\n## New Section\n\n[New content here]\n\n## Section B"
```

### EXPAND: Expanding Existing Content

When adding to content that already exists:

1. Find the specific paragraph/section to expand
2. Write additional content that integrates naturally
3. Don't duplicate what's already there
4. Replace the section with the expanded version

**Example:**
```
old_string: "The company has strong margins."
new_string: "The company has strong margins. Gross margins have averaged 42% over the past 5 years, compared to the industry average of 31%. Management attributes this to [specific factors from source]."
```

### CORRECT: Fixing Errors

When correcting inaccurate content:

1. Identify the exact text that's wrong
2. Determine the correct information from sources
3. Replace with accurate content
4. Consider if related content also needs updating

**Example:**
```
old_string: "Revenue grew 15% in FY2024"
new_string: "Revenue grew 12% in FY2024"
```

---

## Quality Standards for Generated Content

### Consistency
- Match the document's existing heading levels
- Use the same bullet/numbering style
- Follow the same table formatting
- Maintain consistent terminology

### Citations
- Include source references where appropriate
- Use the same citation format as the document
- Be specific: "[10-K FY2024, p.12]" not just "[10-K]"

### Conciseness
- Don't pad content unnecessarily
- Every sentence should add value
- Prefer data and quotes over generic statements

### Integration
- New content should flow naturally
- Use transition phrases if needed
- Don't disrupt the document's structure

---

## Edit Application

Apply edits with exact old and new text:

```
file_path: [Full path to the document]
old_string: [Exact text to replace - must be unique in document]
new_string: [The replacement text including additions]
```

**Critical Rules:**
1. `old_string` must match the document EXACTLY (including whitespace, newlines)
2. `old_string` must be unique in the document (if not, include more context)
3. Preserve all surrounding formatting
4. Don't accidentally delete content that should remain

---

## Output Format

After completing the edit, report:

```markdown
# Edit Completed

## Gap Addressed
[Brief description of the gap]

## Edit Applied

**Type:** ADD / EXPAND / CORRECT

**Location:** [Section/paragraph modified]

**Content Added:**
[Summary of what was added, not the full text]

## Verification
- [ ] Edit applied successfully
- [ ] Content matches source material
- [ ] Formatting consistent with document
- [ ] Transitions are smooth

## Notes
[Any observations or concerns about the edit]
```

---

## Error Handling

If you encounter issues:

### Edit Fails (string not found)
1. Re-read the document to find exact text
2. Include more context in `old_string` to make it unique
3. Check for invisible characters or encoding issues

### Source Content Unclear
1. Note the ambiguity in your report
2. Use most reasonable interpretation
3. Flag for human review if material

### Structural Issues
1. If adding content would disrupt document structure significantly
2. Report the issue and suggest alternative placement
3. Proceed with best available option

---

## Important Reminders

1. **Be surgical** — Change only what's needed, preserve everything else
2. **Be faithful to sources** — Don't embellish or interpret beyond what sources say
3. **Maintain quality** — New content should meet same standard as existing content
4. **Verify your work** — Read the affected section after editing to confirm
