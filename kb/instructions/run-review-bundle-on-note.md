---
description: Run review gates on one note — create a review run, write one gate review per gate, then finalize acceptance
---

# Run a review bundle on one note

Review a specific note against an explicit list of gates.

Use this instruction when you are already inside an agent harness and can execute shell commands directly. For unattended shell automation, use `commonplace-run-review-bundle --runner {codex|claude-code} --model {model-id} {note-path} {gate-or-bundle}...` instead.

The goal is to keep deterministic workflow plumbing in Python while leaving semantic judgment with the current agent.

Inputs:

- first argument: `{note-path}` — repository-relative note path, for example `kb/notes/backlinks.md`
- remaining arguments: `{gate-or-bundle}...` — one or more gate ids or bundle names, for example `semantic/grounding-alignment`, `prose/source-residue`, or `prose` (= all prose gates)

Do not run the selector to choose gates. Treat the provided list as the exact execution set.

Reading scope for review:

- Read the target note in full.
- Read the requested gate definitions.
- For semantic grounding or consistency checks, follow only links that appear in the target note.
- When following a markdown link from the target note, resolve it directly from the note's path instead of searching by name.
- Ignore review backups, workshop copies, and historical artifacts unless the target note links to them explicitly.
- Do not do broad repo search or exploratory `rg` sweeps unless you need to resolve a specific linked path already referenced by the target note.

## Live agent path

### 1. Create the review run and capture the resolved gates

```bash
commonplace-create-review-run --runner {codex|claude-code} --model {model-id} --json {note-path} {gate-or-bundle}...
```

Capture from the JSON output:

- `review_run_id`
- `gate_ids`
- `gates` — each entry includes `gate_id`, `path`, `text`
- `model_id` — initial requested model partition for this run

Do not invent or reorder `gate_ids`; use exactly what the helper resolves.

### 2. Read the target note

Read `{note-path}` in full. For semantic grounding or consistency checks, follow only links from the target note and resolve them directly from the note's location.

### 3. Produce one review file per gate

For each requested gate, write one markdown review body with this layout:

```
### Summary
<short paragraph>

### Findings
- <severity>: <finding>

### Suggested Revision
<optional; omit if not needed>

## Result: PASS|WARN|FAIL|ERROR
```

Rules:

- Apply each gate's failure mode and test to the note.
- Write exactly one review file per requested gate, in the order from `gate_ids`.
- The `## Result:` line must use one of: `PASS`, `WARN`, `FAIL`, `ERROR`.
- Make the `## Result:` line the last non-empty line in each review file.

### 4. Record each gate review

For each requested gate:

```bash
commonplace-write-gate-review --review-run-id {review-run-id} --gate-id {gate-id} --input-file {review-file}
```

This records one `gate_reviews` row for that gate under the existing review run.

### 5. Finalize the run

After all requested gates are written:

```bash
commonplace-finalize-review-run --review-run-id {review-run-id}
```

This validates coverage and appends the acceptance events for the run.

## Shell automation

For unattended shell automation or batch wrappers, use:

```bash
commonplace-run-review-bundle --runner {codex|claude-code} --model {model-id} {note-path} {gate-or-bundle}...
```

This wrapper creates the review run, spawns a nested runner for semantic judgment, parses the bundle output, records gate reviews, and finalizes — all in one command.

## Do not

- Do not run the selector to choose gates before reviewing. This instruction is for explicit execution.
- Do not invoke `commonplace-record-bundle-review`; that command is no longer part of the shipped CLI.
- Do not skip writing a review file for any provided gate.
- Do not write files or invoke commands other than what this instruction specifies.
