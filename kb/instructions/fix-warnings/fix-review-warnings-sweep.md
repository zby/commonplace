---
description: Batch fix of review warnings across notes. Builds a priority queue from CSV data, delegates per-note fixes to sub-agents, collects fix reports with strategy classifications.
---

# Fix Review Warnings Sweep

## Steps

### 1. Build the work queue

Read `kb/reports/reviews/csv/notes_by_warnings.csv` (or the `current.` variant if scoped to current notes). This is sorted by warning count descending.

If the user specified a check filter (e.g., "Source residue only"), also read `kb/reports/reviews/csv/findings.csv` and filter to notes that have WARNs for that check.

Print the queue: note name, WARN count, top check types.

### 2. Delegate

Launch sub-agents to fix notes in parallel. Each sub-agent receives:

```
Read kb/instructions/fix-warnings/fix-review-warnings.md for the fix procedure.
Apply it to: {note-path}

Write the fix report to kb/reports/fixes/{note-stem}.fix-report.md
```

Batch sub-agents in groups of 3–5. Wait for each batch to complete before launching the next.

### 3. Collect results

After each batch, collect the fix reports. Aggregate:
- **Fixed by strategy:** count of fixes per taxonomy strategy name
- **Deferred:** list of items needing human review
- **New patterns:** any `new-pattern` classifications reported

### 4. Report

Write a sweep summary to `kb/reports/SUMMARY.fix-report.md`:

```
# Fix Warnings Sweep — {date}

Notes processed: N
Fixes applied: N (by strategy: stale-paths: 3, hedge-own-framework: 7, ...)
Deferred: N items across M notes
New patterns: N

## Deferred items
[list each with note, check, and reason]

## New patterns
[list each with note, check, and pattern description]

## Per-note reports
- `kb/reports/fixes/{note-stem}.fix-report.md`
- ...
```

### 5. Evolve taxonomy

If new patterns recur (3+ instances of the same pattern), propose adding them to `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`. Present the proposed entry to the user before adding.

### 6. Commit

If fixes were applied, offer to commit. Stage only modified note files. Use a commit message like:

```
Fix review warnings across N notes

Strategies applied: [top 3 strategy names]
Deferred: M items for human review
```
