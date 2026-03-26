---
description: Run review gates directly on one note — load the explicit gate list, execute every review, and record each result
---

# Run a review bundle on one note

Use this instruction when you want to review a specific note against an explicit list of gates.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/backlinks.md`
- remaining arguments: `{gate-id}...` — one or more gate ids, for example `semantic/completeness-boundary-cases` or `prose/source-residue`

Do not run the selector to choose gates in this instruction. Treat the provided gate list as the exact execution set.

## Steps

### 1. Load the note

Read:

- `{note-path}`

### 2. Load every listed gate

For each provided gate id, read the corresponding gate file:

`kb/instructions/review-gates/{gate-id}.md`

The gate files are the canonical checks. Do not substitute the old monolithic review instructions.

### 3. Review the note against each listed gate

For each provided gate:

1. Apply the gate's failure mode and test to the note.
2. Write a fresh review body for the current note state.

### 4. Write and record each gate review

For each gate, ask the storage script for the canonical output path:

```bash
uv run scripts/gate_reviews.py path {note-path} {gate-id}
```

Write the review body directly to the printed path.

After writing the review body there, finalize it with:

```bash
uv run scripts/gate_reviews.py finalize {note-path} {gate-id}
```

This prepends or refreshes the recorded metadata and updates `kb/reports/review-csv/gate_reviews.csv`.

### 5. Verify

After recording all listed gates, run:

```bash
uv run scripts/gate_selector.py --all-gates --json
```

Inspect the JSON output and confirm that none of the gates you just processed still appear for `{note-path}`. If any do, inspect whether:

- the wrong gate was recorded
- the wrong note path or gate id was used
- a gate file changed during the review
- the saved review did not actually cover the current note state

## Do not

- Do not use `scripts/notes_selector.py` or `scripts/gate_selector.py` to choose gates before reviewing. This instruction is for explicit note-plus-gate execution.
- Do not load the old monolithic review instructions as the source of truth for checks.
- Do not skip writing a fresh review body for any provided gate.

## If scripts fail

If `gate_reviews.py`, `gate_selector.py`, or `ack_gate_review.py` fail complaining that `COMMONPLACE_REVIEW_MODEL` is not set, stop and report that the runtime has not provided the current review model to the scripts.
