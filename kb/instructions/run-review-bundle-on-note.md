---
description: Run review gates directly on one note — create a review run, load exact gates, write one review per gate, finalize acceptance
---

# Run a review bundle on one note

Review a specific note against an explicit list of gates.

Use this instruction when you are already inside an agent harness and can execute shell commands directly. For unattended shell automation, use `uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} {gate-or-bundle}...` instead.

The goal is to keep deterministic workflow plumbing in Python while leaving semantic judgment with the current agent. Do not write directly into canonical review artifact paths under `kb/reports/reviews/`.

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

## Live agent path

### 1. Create the review run and capture the resolved gates

```bash
uv run scripts/create_review_run.py --runner {codex|claude-code} --json {note-path} {gate-or-bundle}...
```

Capture from the JSON output:

- `review_run_id`
- `gate_ids`
- `gates`
- `model_id`

Do not invent or reorder `gate_ids`; use exactly what the helper resolves. `gates` is the authoritative gate payload for this run. Each entry includes:

- `gate_id`
- `path`
- `text`

### 2. Read the target note

Read `{note-path}`.

### 3. Review the note against each gate

For each entry in `gates`:

1. Apply the gate's failure mode and test to the note.
2. Write a fresh review body for the current note state.

The review body must be decision-parseable by `scripts/write_gate_review.py`. Use one of these formats:

- `## Result: PASS`
- `## Result: CONCERN`
- `## Result: FAIL`
- `## Result: ERROR`

If you use a findings-style body instead, include explicit `WARN`, `FAIL`, `ERROR`, or `INFO` severities in the findings so the parser can derive the decision.

### 4. Record each review

Use a temporary file per gate and record it with:

```bash
python3 scripts/write_gate_review.py --review-run-id {review-run-id} --gate-id {gate-id} --input-file {tmp-review-file}
```

Use exactly one review body per requested gate. Do not write duplicate reviews for the same `(review_run_id, gate_id)`.

### 5. Finalize the run

Finalize only after every requested gate has been recorded:

```bash
python3 scripts/finalize_review_run.py --review-run-id {review-run-id}
```

## Shell automation

For unattended shell automation or batch wrappers, use:

```bash
uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} {gate-or-bundle}...
```

That wrapper is for automation convenience. It is not the preferred path for live agents already running inside Codex or Claude Code.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not load the old monolithic review instructions as the source of truth for checks.
- Do not write directly into `kb/reports/reviews/` in the live path.
- Do not skip writing a fresh review body for any provided gate.
