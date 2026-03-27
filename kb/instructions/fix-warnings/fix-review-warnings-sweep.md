---
description: Batch fix of review warnings across notes. Runs warn_selector to build a priority queue, delegates per-note fixes to sub-agents, and collects fix reports with strategy classifications
---

# Fix Review Warnings Sweep

## Steps

### 1. Build the work queue

```bash
uv run scripts/warn_selector.py --json | wc -l
```

Check the line count first. If more than 100 lines, tell the user to filter to specific notes.

```bash
uv run scripts/warn_selector.py --json
```

This returns notes sorted by WARN count descending, with full WARN text and gate ids.

If the queue is empty, stop — no WARNs to fix.

### 2. Delegate

For each note in the queue, launch a sub-agent with a prompt to:

> Run `kb/instructions/fix-warnings/fix-review-warnings.md` on `{note-path}`

Multiple sub-agents can run in parallel since each note's fixes are independent.

### 3. Report

After sub-agents complete, report:
- **Fixed by strategy:** count of fixes per taxonomy strategy name
- **Deferred:** items needing human review with reasons
- **New patterns:** any `new-pattern` classifications

### 4. Evolve taxonomy

If new patterns recur (3+ instances of the same pattern), propose adding them to `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`. Present the proposed entry to the user before adding.
