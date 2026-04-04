---
description: Run review gates on one note — create a review run, produce a single bundled review document, then parse and record gate reviews via script
---

# Run a review bundle on one note

Review a specific note against an explicit list of gates.

Use this instruction when you are already inside an agent harness and can execute shell commands directly. For unattended shell automation, use `uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} {gate-or-bundle}...` instead.

The goal is to keep deterministic workflow plumbing in Python while leaving semantic judgment with the current agent.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/backlinks.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

Reading scope for review:

- Read the target note in full.
- Read the requested gate definitions.
- For semantic grounding or consistency checks, follow only links that appear in the target note.
- When following a markdown link from the target note, use the pre-resolved path table from the review run JSON instead of searching for targets by name.
- Ignore review backups, workshop copies, and historical artifacts unless the target note links to them explicitly.
- Do not do broad repo search or exploratory `rg` sweeps unless you need to resolve a specific linked path already referenced by the target note.

## Live agent path

### 1. Create the review run and capture the resolved gates

```bash
uv run scripts/create_review_run.py --runner {codex|claude-code} --json {note-path} {gate-or-bundle}...
```

Capture from the JSON output:

- `review_run_id`
- `gate_ids`
- `gates` — each entry includes `gate_id`, `path`, `text`
- `model_id`
- `resolved_links` — pre-resolved markdown link targets from the note
- `unresolved_links` — broken links to treat as broken if relevant

Do not invent or reorder `gate_ids`; use exactly what the helper resolves.

### 2. Read the target note

Read `{note-path}` in full. For semantic grounding or consistency checks, follow links from the target note using the pre-resolved paths from step 1.

### 3. Produce a single bundled review document

Write one markdown document containing one block per requested gate. Use these exact sentinels to delimit each block:

```
=== GATE REVIEW START: {gate-id} ===
## Result: PASS|CONCERN|FAIL|ERROR

### Summary
<short paragraph>

### Findings
- <severity>: <finding>

### Suggested Revision
<optional; omit if not needed>
=== GATE REVIEW END: {gate-id} ===
```

Rules:

- Apply each gate's failure mode and test to the note.
- Use exactly one block per requested gate, in the order from `gate_ids`.
- The `## Result:` line must use one of: `PASS`, `CONCERN`, `FAIL`, `ERROR`.
- End the document after the final gate block.

Write the bundled review document to:

```
kb/reports/bundle-reviews/review-run-{review-run-id}/bundle-output.md
```

This directory is gitignored.

### 4. Parse, record, and finalize

Run the parse-and-record script to extract individual gate reviews from the bundle, write them to the DB, and finalize acceptance:

```bash
uv run scripts/record_bundle_review.py --review-run-id {review-run-id}
```

This script reads the bundle output from `kb/reports/bundle-reviews/review-run-{review-run-id}/bundle-output.md`, parses the sentinel-delimited blocks, records one `gate_reviews` row per gate, and finalizes the review run with acceptance events.

## Shell automation

For unattended shell automation or batch wrappers, use:

```bash
uv run scripts/run_review_bundle.py --runner {codex|claude-code} {note-path} {gate-or-bundle}...
```

This wrapper creates the review run, spawns a nested runner for semantic judgment, parses the bundle output, records gate reviews, and finalizes — all in one command.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not invoke `write_gate_review.py` or `finalize_review_run.py` individually — the record script handles both.
- Do not skip writing a review block for any provided gate.
- Do not write files or invoke scripts other than what this instruction specifies.
