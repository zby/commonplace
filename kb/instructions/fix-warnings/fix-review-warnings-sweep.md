---
description: Batch fix actionable findings from fresh warn and fail review results across notes, with optional per-note workers, re-review and strategy reporting
type: types/instruction.md
---

# Fix Review Warnings Sweep

## Steps

### 1. Build the work queue

```bash
commonplace-review status --fresh --outcome warn fail --json
```

Each row in `pairs` is one current warning: a (note, criterion) pair whose
fresh result has outcome `warn` or `fail`, with `criterion-id` and `result`,
the path of its result file. Group the rows by `note` and order the notes by
row count, descending. If the user did not name a scope and the queue spans
more than one collection, report the counts and ask which notes or
collections to take first; to filter, pass note paths or directories before
the options.

If `pairs` is empty, stop — there are no current warn findings to fix. Rows
for stale results are excluded by `--fresh`; report them as needing
re-review if the user asked about them, and do not fix from their text.

### 2. Execute or delegate

Run a single-note queue locally unless several notes have disjoint note and
report paths and a fresh per-note context or parallel capacity gives a specific
benefit. When that condition holds, launch one single-use worker per note with
this complete packet:

- run [fix-review-warnings.md](./fix-review-warnings.md) (give the worker its
  absolute path, resolved from this file's location) on the exact
  `{note-path}`, skipping its re-review step;
- own only that note and
  `kb/reports/state/fixes/{note-stem}.fix-report.md`;
- read the inputs authorized by that instruction and no unrelated notes;
- do not use another orchestration skill, and do not run `commonplace-review run`;
- validate the note and return its diff summary, report path, and validation;
- defer and return the exact substantive choice when the instruction's edit
  boundary would be crossed.

The parent owns queue selection and collision checks. After each worker
returns, verify its note diff, report, and validation, then close, terminate,
or release it before dispatching more work. Stop on missing or partial output;
workers are single-use and receive no follow-up task.

### 3. Re-review the edited notes

Run one gate sweep over every note that changed, asking for all gates:

```bash
commonplace-review run gates {edited-notes...} --all-gates --grouping bundle
```

The edits stale every pair whose watched parts changed, including pairs that
passed before, and the sweep asks exactly those, skipping fresh results. Read its report as [run review batches](../run-review-batches.md)
describes.

### 4. Report

After the re-review, report:
- **Fixed by strategy:** count of fixes per taxonomy strategy name
- **Rejected:** findings judged spurious or inapplicable, with evidence
- **Deferred:** exact claim/evidence/source choices, affected passages,
  acceptable responses, and why the worker could not select one
- **Re-reviewed:** each re-asked pair's new outcome, and any pair the sweep
  left without a current result
- **New patterns:** any `new-pattern` classifications

### 5. Evolve taxonomy

If new patterns recur (3+ instances of the same pattern), propose adding them to the [fix strategy taxonomy](./fix-strategy-taxonomy.md). Present the proposed entry to the user before adding.
