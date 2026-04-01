---
description: Run review gates directly on one note — load gates, execute every review, write results
---

# Run a review bundle on one note

Review a specific note against an explicit list of gates.

Preferred entrypoint for live reviews:

```bash
uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} {gate-or-bundle}...
```

This script creates a `review_run`, delegates the gate reviews, records them in the review DB, and finalizes acceptance state. Do not write directly to canonical review artifact paths during the live path.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/backlinks.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

Reading scope for review:

- Read the target note in full.
- Read the requested gate definitions.
- For semantic grounding or consistency checks, follow only links that appear in the target note.
- Do not do broad repo search or exploratory `rg` sweeps unless you need to resolve a specific linked path already referenced by the target note.
- Do not widen the context beyond the target note's linked neighborhood unless a gate explicitly requires it.

## Steps

## Preferred path

If you have shell access, run:

```bash
uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} {gate-or-bundle}...
```

Use `--runner codex` when executing from Codex and `--runner claude-code` when executing from Claude Code.

## Manual fallback

Only use this when debugging the review flow itself.

### 1. Load gates and note

```bash
uv run scripts/resolve_gates.py {gate-or-bundle}...
```

This resolves bundle names to individual gates, reads each gate file, and prints the concatenated gate text. Each gate block is labeled with its gate id. A bundle name (e.g. `prose`) expands to all gates in that directory.

Read `{note-path}`.

### 2. Review the note against each gate

For each gate:

1. Apply the gate's failure mode and test to the note.
2. Write a fresh review body for the current note state.

### 3. Record each review

Do not write directly into `kb/reports/reviews/`. If you are following the manual fallback, use a temporary file per gate and record it with:

```bash
python3 scripts/write_gate_review.py --review-run-id {review-run-id} --gate-id {gate-id} --input-file {tmp-review-file}
```

Finalize the run only after every requested gate has been recorded:

```bash
python3 scripts/finalize_review_run.py --review-run-id {review-run-id}
```

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not load the old monolithic review instructions as the source of truth for checks.
- Do not write directly into `kb/reports/reviews/` in the live path.
- Do not skip writing a fresh review body for any provided gate.
