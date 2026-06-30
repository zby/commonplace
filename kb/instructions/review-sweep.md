---
description: Batch review sweep — run the selector, triage note-changed pairs, and execute direct-write review jobs for the rest
type: kb/types/instruction.md
---

# Review sweep

Batch review across reviewable notes. Works with any bundle or all gates.

Inputs:

- `{bundle-or-all}` — a bundle name (e.g. `prose`, `semantic`, `frontmatter`) or `--all-gates`
- `{note-scope}` — one or more note paths or directories to limit the sweep; omit only when using `--current`
- `--current` (optional) — limit the sweep to notes whose frontmatter says `status: current`
- `--runner {claude-code|codex}` (optional) — choose which review runner executes each note-local bundle job

## Steps

### 1. Triage

Launch a sub-agent to run `kb/instructions/review-triage.md` with `{bundle-or-all}` and `{note-scope}`. This uses `commonplace-ack-gate-review` to ack insignificant `note-changed` pairs, reducing the review queue.

### 2. Inventory

```bash
commonplace-review-target-selector --model {model-id} {bundle-or-all} --note {note-scope} --json
```

Or for current notes only:

```bash
commonplace-review-target-selector --model {model-id} {bundle-or-all} --current --json
```

Check the `targets` array in the JSON object.

- **`"targets": []`**: stop — everything is fresh or acked.
- **More than ~20 targets**: stop and tell the user to run `commonplace-review-sweep` instead. This instruction cannot orchestrate that many sub-agents.
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

This batches notes into one prompt while recording one gate-packed review job containing one review pair per reviewed note.

If there are many notes, use:

```bash
commonplace-review-sweep --model {model-id} {bundle-or-all} {note-scope...}
```

Or:

```bash
commonplace-review-sweep --model {model-id} --current {bundle-or-all}
```

`commonplace-review-sweep` executes note-local bundle reviews in parallel, up to 4 at a time by default. Override with `REVIEW_SWEEP_JOBS=<n>` if needed.

Example for current notes in Codex:

```bash
commonplace-review-sweep --model gpt-5-4-xhigh --runner codex --current semantic
```

For explicit one-note review from an agent harness, run `kb/instructions/run-review-batches-on-note.md` once per note.

Multiple note-local jobs can execute in parallel since each note's reviews are independent.

### 4. Report

Report which pairs were reviewed and which were acked.

## Do not

- Do not ack when the diff is significant. The purpose of the review is to catch problems the diff introduces.
- Do not skip `note-changed` entries without inspecting the diff.
