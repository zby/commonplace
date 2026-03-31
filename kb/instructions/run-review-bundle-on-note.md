---
description: Run review gates directly on one note — load gates, execute every review, write results
---

# Run a review bundle on one note

Review a specific note against an explicit list of gates.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/backlinks.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

## Steps

### 1. Load gates and note

```bash
uv run scripts/resolve_gates.py --note {note-path} {gate-or-bundle}...
```

This resolves bundle names to individual gates, reads each gate file, and prints the concatenated gate text. Each gate block is labeled with its gate id and the canonical review output path. A bundle name (e.g. `prose`) expands to all gates in that directory.

Read `{note-path}`.

### 2. Review the note against each gate

For each gate:

1. Run `scripts/review_prereqs.sh {note-path} {gate-id}` and use the emitted metadata block at the top of the review file.
2. Apply the gate's failure mode and test to the note.
3. Write a fresh review body for the current note state.

### 3. Write each review

Write each review body to the path printed by `resolve_gates.py` for that gate. The metadata block marks the accepted note revision and gate fingerprint — no filesystem timestamp contract is used.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not load the old monolithic review instructions as the source of truth for checks.
- Do not skip writing a fresh review body for any provided gate.
