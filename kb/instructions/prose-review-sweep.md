---
description: Batch prose review across all notes in kb/notes/. Delegates each note to a sub-agent running prose-review, saves individual reports, then writes a summary with aggregate findings.
---

# Prose Review Sweep

Run the [prose review](./prose-review.md) across all notes in `kb/notes/`. Each note is reviewed by a sub-agent. Individual reports are saved to `reviews/` and a summary aggregates findings across the KB.

## Steps

### 1. Inventory

Run `uv run scripts/notes_selector.py prose-review --json` to get the changed-note queue. The script compares each top-level note's current blob hash against the `last-accepted-note-sha` stored in `reviews/{note-stem}.prose-review.md`, filters out notes whose content did not change at all, and includes a compact diff for changed notes.

If you only need note paths, omit `--json`.

### 2. Delegate

Launch sub-agents to review notes in parallel. The orchestrator should inspect each diff first; link-only or otherwise trivial edits may not need a full re-review. For notes whose diffs are trivial, acknowledge them with:

```
uv run scripts/ack_review.py prose-review {note-path}
```

For notes that do need a full review, each sub-agent receives this prompt:

```
Read kb/instructions/prose-review.md for the review procedure.
Apply it to: {note-path}

Write the full report (in the output format specified by the instruction)
to: reviews/{note-stem}.prose-review.md

Do not modify the note. Only write the review file.
```

Where `{note-stem}` is the filename without `.md` (e.g., `knowledge-storage-does-not-imply-contextual-activation`).

Batch sub-agents in groups of 5–8 to manage concurrency. Wait for each batch to complete before launching the next.

### 3. Summarize

After all reviews are complete, run:

```
uv run scripts/summarize_reviews.py prose-review
```

This writes ranked CSV tables in `reviews/csv/` and a compact `reviews/SUMMARY.prose-review.md` built from the top rows of those tables.

### 4. Report to user

Print the "most common findings" section from the summary. Link to the full summary.

## Re-running

Subsequent runs overwrite individual review files and the summary. To track changes over time, commit the reviews directory before re-running.
