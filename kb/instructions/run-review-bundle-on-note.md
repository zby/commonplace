---
description: Run review gates on one note from inside a live agent harness
---

# Run a review bundle on one note

Review a specific note against an explicit list of gates from inside the current agent harness.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/backlinks.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

## Live agent path

### 1. Create the review run and canonical prompt

```bash
commonplace-create-review-run --runner {codex|claude-code} --model {model-id} --with-prompt {note-path} {gate-or-bundle}...
```

Capture the JSON output, especially:

- `review_run_id`
- `prompt`
- `bundle_output_path`
- `gate_ids`

Do not invent or reorder `gate_ids`; use exactly what the helper resolves.

### 2. Follow the returned prompt

Use the `prompt` field as the authoritative reviewer instruction. It contains the reading scope, gate definitions, link-resolution table, and sentinel output contract for this run.

Write the full sentinel-bracketed review bundle to `bundle_output_path`.

### 3. Ingest the bundle output

```bash
commonplace-ingest-bundle-output --review-run-id {review-run-id} --input-file {bundle-output-path}
```

This parses the bundle with the same parser used by `commonplace-run-review-bundle`, records the per-gate reviews, and finalizes the review run.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not invoke `commonplace-record-bundle-review`; that command is no longer part of the shipped CLI.
- Do not call `commonplace-write-gate-review` in the normal live-agent bundle flow; use `commonplace-ingest-bundle-output` instead.
- Do not skip a requested gate block in the bundle output.
