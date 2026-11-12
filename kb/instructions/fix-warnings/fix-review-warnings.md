---
description: Fix actionable findings from fresh warn and fail review results on one note, re-review the edited note, then classify and report the fixes
type: types/instruction.md
---

# Fix Review Warnings

**Target: $ARGUMENTS**

If target is empty, ask which note to fix. If target is a name without path, search `kb/theory/` for a matching `.md` file.

## What this is

An editing pass that fixes actionable findings from review results whose
outcome is `warn` or `fail` and which are fresh: the hashes they record still
match the note and the criterion. The reviews already contain specific
recommendations. This instruction constrains how to apply them and gives the
fixes an auditable report format.

## Prerequisites

1. Run `commonplace-review status {note-path} --fresh --outcome warn fail --json`.
   Each row in `pairs` is one current warning: its `criterion-id`, `outcome`
   and `result`, the path of its result file. If `pairs` is empty, report "no
   current warn findings" and stop. Do not fix from a stale result: a `warn`
   or `fail` that `--fresh` drops needs re-review, not a fix.
2. If `kb/reports/state/fixes/{note-stem}.fix-report.md` exists, read it. A
   finding it records as rejected or deferred stays a fresh warning until the
   note or criterion changes; do not work it again unless its evidence changed.
3. Read the target note in full.
4. Read each row's result file. Its `### Findings` items (`- <severity>: <finding>`) are the findings; when it has none, use `### Summary`. The result file is the authoritative review text.
5. Read the [fix strategy taxonomy](./fix-strategy-taxonomy.md) for the named fix strategies.

## Procedure

For each actionable finding returned in a note entry:

1. **Read the recommendation** in the review finding. It tells you what to fix and usually how.
2. **Read enough context** around the flagged passage to understand the argument, the evidence relationship, and the flow.
3. **Decide** which disposition the evidence supports:
   - **Fixed** — the finding applies and can be resolved by changing framing or accuracy without changing the note's argument. Apply the smallest edit that resolves it.
   - **Rejected** — the finding is spurious, factually mistaken, or inapplicable to the passage. Leave the note unchanged and record the evidence or reasoning for rejection.
   - **Deferred** — the finding may be valid, but resolving it would change the argument or requires a substantive human decision. Leave the note unchanged and record the exact claim, evidence, or source choice; the affected passage; the acceptable response choices; and why this pass cannot select among them.
4. **Classify each applied fix** using a named strategy from the taxonomy. If no existing strategy fits, classify it as `new-pattern` and describe the pattern briefly. Use `—` for rejected or deferred findings because no fix strategy was applied.

After all fixes:

5. Re-read edited sections to verify flow and cohesion. Fixes should read as if they were always there.
6. If any fix was applied and the note carries `user-verified`, remove that field: a fix that changes framing or accuracy is a substantive edit, and only a human may restore verification (see the [note type](../../types/note.md)).
7. Produce the fix report (format below).
8. If any fix was applied, re-review the note. The edit stales every pair whose watched parts it changed, including pairs that passed before the edit, so ask for all gates and let freshness select the pairs; the sweep skips fresh results without `--force`:

   ```bash
   commonplace-review run gates {note-path} --all-gates
   ```

   Do not restrict the sweep to the worked rows with `--criteria`: a body edit stales most catalog gates, and a pass recorded against the pre-edit text is not a pass of the edited note. Read the report as [run review batches](../run-review-batches.md) describes, and add each re-reviewed pair's new outcome to the fix report, listing separately any previously passing pair that now warns. Skip this step when the user asked only for fixes, and say that the stale pairs, worked or not, await re-review.

## Constraints

- **Minimal edits.** Fix the warning, not the surrounding prose. Don't improve, refactor, or tighten text that wasn't flagged.
- **Only edit flagged passages.** If no warning targets the description, title, or a specific section, don't rewrite it. Scope creep into adjacent text produces lower-quality edits because there's no review finding guiding the change.
- **Description edits need their own procedure.** If you encounter description issues (from `commonplace-validate` or as a side effect), use [fix-descriptions.md](./fix-descriptions.md) rather than improvising a rewrite.
- **Don't change arguments.** Fixes change framing, accuracy, and attribution — not the note's claims or structure.
- **Don't remove examples.** Frame them ("In [domain], for instance...") instead of replacing with abstractions.
- **Don't edit result files.** A result is regenerated only by rerunning the gate sweep.
- **Verify before assuming staleness.** If a warning claims a path/field/mechanism is stale, check whether it actually exists before removing or updating it.

## Fix report format

Write the fix report to `kb/reports/state/fixes/{note-stem}.fix-report.md`.

```
## Fix Report: {note-stem}

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Source residue | stale-paths | Updated `docs/sources/` → `kb/sources/` | fixed |
| 2 | Confidence miscalibration | hedge-own-framework | Added "we propose" to taxonomy assertion | fixed |
| 3 | Grounding | — | Source supports the existing scoped claim; warning overstates it | rejected |
| 4 | Grounding | — | Claim vs source tension is substantive, not framing | deferred |

### Warning-to-fix mapping
For each fix, quote or paraphrase the review warning that triggered it, so the fix can be audited against the original finding.

- **#1 (Source residue):** "The note refers to `docs/sources/` but the actual path is `kb/sources/`."
- **#2 (Confidence miscalibration):** "The taxonomy is the note's own construction presented as established fact."
- **#3 (Grounding):** "The source does not support the note's scoped claim."
- **#4 (Grounding):** "The note uses the source to support context primacy, but the source argues for a broader view."

### Rejected findings
- **#3 (Grounding):** The cited passage explicitly supports the scoped claim; no note change is warranted.

### Deferred items
- **#4 (Grounding):** The affected passage uses source X for claim Y. Choose whether to narrow Y to Z or keep Y and replace the source; this pass lacks authority to select either response.

### New patterns
- (none, or describe any fix that didn't fit an existing taxonomy strategy)
```
