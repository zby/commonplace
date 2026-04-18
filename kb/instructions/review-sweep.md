---
description: Batch review sweep — run the selector, triage note-changed pairs, and execute direct-write review runs for the rest
type: instruction
---

# Review sweep

Batch review across reviewable notes. Works with any bundle or all gates.

Inputs:

- `{bundle-or-all}` — a bundle name (e.g. `prose`, `semantic`, `frontmatter`) or `--all-gates`
- `{note-scope}` — one or more note paths or directories to limit the sweep; omit only when using `--current`
- `--current` (optional) — limit the sweep to notes whose frontmatter says `status: current`
- `--runner {claude-code|codex}` (optional) — choose which review runner executes each note-local bundle run

## Steps

### 1. Triage

Launch a sub-agent to run `kb/instructions/review-triage.md` with `{bundle-or-all}` and `{note-scope}`. This uses `commonplace-ack-gate-review` to ack insignificant `note-changed` pairs, reducing the review queue.

### 2. Inventory

```bash
commonplace-review-target-selector --model {model-id} {bundle-or-all} --note {note-scope} --json | wc -l
```

Or for current notes only:

```bash
commonplace-review-target-selector --model {model-id} {bundle-or-all} --current --json | wc -l
```

Check the line count first (~5 lines per stale pair in JSON output).

- **0–2 lines** (empty array): stop — everything is fresh or acked.
- **More than 100 lines** (~20+ pairs): stop and tell the user to run `commonplace-review-sweep` instead. This instruction cannot orchestrate that many sub-agents.
- **Otherwise**: read the JSON output and continue.

```bash
commonplace-review-target-selector --model {model-id} {bundle-or-all} --note {note-scope} --json
```

Or:

```bash
commonplace-review-target-selector --model {model-id} {bundle-or-all} --current --json
```

### 3. Review remaining pairs

Group the remaining pairs by note.

If the remaining execution set is one gate across many notes, prefer:

```bash
commonplace-run-gate-sweep {gate-id} --runner {codex|claude-code} --model {model-id} [--current] [--note {note-scope} ...]
```

This batches notes into one prompt while still recording one review run per note.

If there are many notes, use:

```bash
commonplace-review-sweep --model {model-id} {bundle-or-all} {note-scope...}
```

Or:

```bash
commonplace-review-sweep --model {model-id} --current {bundle-or-all}
```

`commonplace-review-sweep` runs note-local bundle reviews in parallel, up to 4 at a time by default. Override with `REVIEW_SWEEP_JOBS=<n>` if needed.

Example for current notes in Codex:

```bash
commonplace-review-sweep --model gpt-5-4-xhigh --runner codex --current semantic
```

For explicit one-note review from an agent harness, run `kb/instructions/run-review-bundle-on-note.md` once per note.

Multiple note-local runs can execute in parallel since each note's reviews are independent.

### 4. Report

Report which pairs were reviewed and which were acked.

## Do not

- Do not ack when the diff is significant. The purpose of the review is to catch problems the diff introduces.
- Do not skip `note-changed` entries without inspecting the diff.
