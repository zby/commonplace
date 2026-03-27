---
description: General instruction for fixing review warnings. Reads current-model gate reviews for a note, applies fixes using judgment, classifies each fix by strategy from the taxonomy, and reports results
---

# Fix Review Warnings

**Target: $ARGUMENTS**

If target is empty, ask which note to fix. If target is a name without path, search `kb/notes/` for a matching `.md` file.

## What this is

An editing pass that fixes WARN-level findings from prose and/or semantic reviews. The reviews already contain specific recommendations — this instruction provides constraints on how to apply them and a reporting format that makes the fixes auditable.

## Prerequisites

1. Run `uv run scripts/warn_selector.py --json {note-path}` to get WARN-level findings for this note. If there are none, report "no WARNs" and stop.
2. Read the target note in full.
3. Read the gate review files listed in the warn_selector output (the `review_path` fields).
4. Read `kb/instructions/fix-warnings/fix-strategy-taxonomy.md` for the named fix strategies.

## Procedure

For each WARN from the current-model gate reviews:

1. **Read the recommendation** in the review finding. It tells you what to fix and usually how.
2. **Read enough context** around the flagged passage to understand the argument, the evidence relationship, and the flow.
3. **Decide**: can this be fixed by changing framing/accuracy without changing the note's argument?
   - **Yes** → apply the fix. Prefer the smallest edit that resolves the warning.
   - **No** → defer. Report it as needing human review with a reason.
4. **Classify the fix** using a named strategy from the taxonomy. If no existing strategy fits, classify as `new-pattern` and describe the pattern briefly.

After all fixes:

5. Re-read edited sections to verify flow and cohesion. Fixes should read as if they were always there.
6. Produce the fix report (format below).

## Constraints

- **Minimal edits.** Fix the warning, not the surrounding prose. Don't improve, refactor, or tighten text that wasn't flagged.
- **Only edit flagged passages.** If no warning targets the description, title, or a specific section, don't rewrite it. Scope creep into adjacent text produces lower-quality edits because there's no review finding guiding the change.
- **Description edits need their own procedure.** If you encounter description issues (from `/validate` or as a side effect), use `kb/instructions/fix-warnings/fix-descriptions.md` rather than improvising a rewrite.
- **Don't change arguments.** Fixes change framing, accuracy, and attribution — not the note's claims or structure.
- **Don't remove examples.** Frame them ("In [domain], for instance...") instead of replacing with abstractions.
- **Don't update review files.** Gate reviews are regenerated or re-recorded separately.
- **Verify before assuming staleness.** If a warning claims a path/field/mechanism is stale, check whether it actually exists before removing or updating it.

## Fix report format

Write the fix report to `kb/reports/fixes/{note-stem}.fix-report.md`.

```
## Fix Report: {note-stem}

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Source residue | stale-paths | Updated `docs/sources/` → `kb/sources/` | fixed |
| 2 | Confidence miscalibration | hedge-own-framework | Added "we propose" to taxonomy assertion | fixed |
| 3 | Grounding | — | Claim vs source tension is substantive, not framing | deferred |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Source residue):** "The note refers to `docs/sources/` but the actual path is `kb/sources/`."
- **#2 (Confidence miscalibration):** "The taxonomy is the note's own construction presented as established fact."
- **#3 (Grounding):** "The note uses the source to support context primacy, but the source argues for a broader view."

### Deferred items
- **#3 (Grounding):** Resolving this requires deciding whether to narrow the claim or reframe the source usage — human judgment needed.

### New patterns
- (none, or describe any fix that didn't fit an existing taxonomy strategy)
```
