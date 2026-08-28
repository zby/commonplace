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

### 2. Execute or delegate

Run a single-note queue locally unless several notes have disjoint note and
report paths and a fresh per-note context or parallel capacity gives a specific
benefit. When that condition holds, launch one single-use worker per note with
this complete packet:

- run `kb/instructions/fix-warnings/fix-review-warnings.md` on the exact
  `{note-path}`;
- own only that note and
  `kb/reports/fixes/{note-stem}.fix-report.md`;
- read the inputs authorized by that instruction and no unrelated notes;
- do not delegate or use another orchestration skill;
- validate the note and return its diff summary, report path, and validation;
- defer and return the exact substantive choice when the instruction's edit
  boundary would be crossed.

The parent owns queue selection, collision checks, scheduling, integration, and
failure recovery. After each worker returns, verify its note diff, report, and
validation, then close, terminate, or release it before dispatching more work.
Stop on missing or partial output; workers are single-use and receive no
follow-up task.

### 3. Report

After sub-agents complete, report:
- **Fixed by strategy:** count of fixes per taxonomy strategy name
- **Rejected:** findings judged spurious or inapplicable, with evidence
- **Deferred:** exact claim/evidence/source choices, affected passages,
  acceptable responses, and why the worker could not select one
- **New patterns:** any `new-pattern` classifications

### 4. Evolve taxonomy

If new patterns recur (3+ instances of the same pattern), propose adding them to `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`. Present the proposed entry to the user before adding.
