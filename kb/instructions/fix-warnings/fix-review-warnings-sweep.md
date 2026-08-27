---
description: Batch fix actionable findings from warn review pairs across notes using warn_selector, sub-agent delegation, and strategy reporting
type: kb/types/instruction.md
---

# Fix Review Warnings Sweep

## Steps

### 1. Build the work queue

```bash
commonplace-warn-selector --json | wc -l
```

Check the line count first. If more than 100 lines, tell the user to filter to specific notes.

```bash
commonplace-warn-selector --json
```

This returns notes sorted by actionable finding count descending, with full
finding text and gate ids. It collapses model partitions so each `(note, gate)`
contributes at most one current review. Only note entries with `warns` belong in
the work queue. A trailing `stale_pairs` entry is advisory: report those pairs
as needing re-review and do not delegate fixes from their retained text.

If there are no actionable note entries, stop — there are no current warn
findings to fix, even if stale pairs were reported.

### 2. Delegate

For each note in the queue, launch a sub-agent with a prompt to:

> Run `kb/instructions/fix-warnings/fix-review-warnings.md` on `{note-path}`

Multiple sub-agents can run in parallel since each note's fixes are independent. After each worker returns, verify its note changes and report, then close, terminate, or release that worker before dispatching more work. Workers are single-use; do not send follow-up tasks.

### 3. Report

After sub-agents complete, report:
- **Fixed by strategy:** count of fixes per taxonomy strategy name
- **Rejected:** findings judged spurious or inapplicable, with evidence
- **Deferred:** items needing human review with reasons
- **New patterns:** any `new-pattern` classifications

### 4. Evolve taxonomy

If new patterns recur (3+ instances of the same pattern), propose adding them to `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`. Present the proposed entry to the user before adding.
