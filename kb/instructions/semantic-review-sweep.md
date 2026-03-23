---
description: Batch semantic review across all notes in kb/notes/. Delegates each note to a sub-agent running semantic-review, saves individual reports, then writes a summary with aggregate findings.
---

# Semantic Review Sweep

Run the [semantic review](./semantic-review.md) across all notes in `kb/notes/`. Each note is reviewed by a sub-agent. Individual reports are saved to `reviews/` and a summary aggregates findings across the KB.

## Steps

### 1. Inventory

Run `uv run scripts/list_notes.py` to get the list of notes to review. The script finds all frontmatter notes in `kb/notes/`, excluding indexes and subdirectories.

### 2. Delegate

Launch sub-agents to review notes in parallel. Each sub-agent receives this prompt:

```
Read kb/instructions/semantic-review.md for the review procedure.
Apply it to: {note-path}

Write the full report (in the output format specified by the instruction)
to: reviews/{note-stem}.semantic-review.md

Do not modify the note. Only write the review file.
```

Where `{note-stem}` is the filename without `.md` (e.g., `knowledge-storage-does-not-imply-contextual-activation`).

Semantic review follows linked sources (up to 5 per note), so it is heavier than prose review. Batch sub-agents in groups of 3–5 to manage concurrency. Wait for each batch to complete before launching the next.

### 3. Summarize

After all reviews are complete, run:

```
uv run scripts/summarize_reviews.py semantic-review
```

This reads all `reviews/*.semantic-review.md` files and writes `reviews/SUMMARY.semantic-review.md` with WARN tables, check distribution, most common findings, and clean notes.

### 4. Report to user

Print the "most common findings" section from the summary. Link to the full summary.

## Re-running

Subsequent runs overwrite individual review files and the summary. To track changes over time, commit the reviews directory before re-running.
