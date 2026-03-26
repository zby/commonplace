---
description: Batch semantic review across all notes in kb/notes/. Delegates each note to a sub-agent running semantic-review, saves individual reports, then writes a summary with aggregate findings.
---

# Semantic Review Sweep

Run the semantic gate bundle across top-level notes in `kb/notes/`. Selection is gate-based: the selector emits stale `(note, gate)` pairs, then execution groups them by note and lens.

## Steps

### 1. Inventory

Run `uv run scripts/gate_selector.py semantic-review --json` to get the stale gate queue.

The selector checks missing recorded gate reviews, gate-file hash changes, and watched-region hash changes for each semantic gate.

If you only need grouped plain text, omit `--json`.

### 2. Delegate

Group stale pairs by `(note, lens)`. For each group, load:

- the note
- `kb/instructions/review-bundles/semantic-review.md`
- the specific gate files under `kb/instructions/review-gates/semantic/`

Have the reviewer ask the storage script for the canonical review path, write one recorded review body there per stale gate, then finalize it with:

```
uv run scripts/gate_reviews.py path {note-path} {gate-id}
```

Then run:

```
uv run scripts/gate_reviews.py finalize {note-path} {gate-id}
```

This finalizes the recorded gate review file and regenerates `kb/reports/review-csv/gate_reviews.csv`.

If the change is too small to justify a fresh review, acknowledge one or more stale gates for the note with:

```
uv run scripts/ack_gate_review.py {note-path} {gate-id}
uv run scripts/ack_gate_review.py {note-path} {gate-id-1} {gate-id-2} ...
```

### 3. Rebuild index

```
uv run scripts/gate_reviews.py rebuild-csv
```

This is idempotent and safe to run after batch review writes.

### 4. Report to user

Report which `(note, gate)` pairs were reviewed and point to the stored gate review files.

## Re-running

Subsequent runs overwrite recorded gate review files for the same `(note, gate)` pair. Commit the reviews directory before re-running if you want history.

If selector, finalize, or ack commands fail complaining that `COMMONPLACE_REVIEW_MODEL` is not set, stop and report that the runtime has not provided the current review model to the scripts.
