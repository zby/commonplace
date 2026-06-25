---
description: Run review gates on one note from inside a live agent harness
type: kb/types/instruction.md
---

# Run review bundles on one note

Review a specific note against an explicit list of gates from inside the current agent harness.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/linking-theory.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

## Live agent path

### 1. Create review runs and canonical prompts

```bash
commonplace-create-review-runs --runner {codex|claude-code|live-agent} --model {model-partition} {note-path} {gate-or-bundle}...
```

The helper groups the requested gates by bundle/lens and returns a JSON object with `runs`. Capture each run object, especially:

- `review_run_id`
- `prompt_path`
- `bundle_output_path`
- `manifest_path`
- `gate_ids`
- `gate_paths`

Do not invent, merge, or reorder runs. Use exactly the run grouping and `gate_ids` the helper resolves.

### 2. Follow each canonical prompt

For each item in `runs`, read the file at `prompt_path` and treat it as the authoritative reviewer instruction. It contains the reading scope, gate definitions, link-resolution table, and sentinel output contract for that run.

Write the full sentinel-bracketed review bundle to that run's `bundle_output_path`. Do not combine multiple runs into one output file.

### 3. Ingest each bundle output

```bash
commonplace-ingest-bundle-output --review-run-id {review-run-id} --input-file {bundle-output-path}
```

Run ingest once per completed run. This parses the bundle with the same parser used by `commonplace-run-review-bundles`, records the per-pair reviews, and finalizes the review run.

After ingest, `MANIFEST.json` at `manifest_path` is refreshed with pair statuses and per-gate `result_path` files. For this single-note path, parsed review files are named by gate id, for example `sentence__clause-packing.md`.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not invoke retired manual review-writing commands; use `commonplace-ingest-bundle-output`.
- Do not skip a requested gate block in the bundle output.
