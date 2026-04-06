---
description: Batch review sweep — run the selector, triage note-changed pairs, and execute direct-write review runs for the rest
---

# Review sweep

Batch review across reviewable notes. Works with any bundle or all gates.

Inputs:

- `{bundle-or-all}` — a bundle name (e.g. `prose`, `semantic`, `frontmatter`) or `--all-gates`
- `{note-paths}` (optional) — one or more note paths to limit the sweep to specific notes
- `--current` (optional) — limit the sweep to notes whose frontmatter says `status: current`
- `--runner {claude-code|codex}` (optional) — choose which review runner executes each note-local bundle run

## Steps

### 1. Triage

Launch a sub-agent to run `kb/instructions/review-triage.md` with `{bundle-or-all}` and `{note-paths}`. This uses `scripts/ack_gate_review.py` to ack insignificant `note-changed` pairs, reducing the review queue.

### 2. Inventory

```bash
python3 scripts/review_target_selector.py --model {model-id} {bundle-or-all} --note {note-paths} --json | wc -l
```

Or for current notes only:

```bash
python3 scripts/review_target_selector.py --model {model-id} {bundle-or-all} --current --json | wc -l
```

Check the line count first (~5 lines per stale pair in JSON output).

- **0–2 lines** (empty array): stop — everything is fresh or acked.
- **More than 100 lines** (~20+ pairs): stop and tell the user to run `scripts/review_sweep.sh` instead. This instruction cannot orchestrate that many sub-agents.
- **Otherwise**: read the JSON output and continue.

```bash
python3 scripts/review_target_selector.py --model {model-id} {bundle-or-all} --note {note-paths} --json
```

Or:

```bash
python3 scripts/review_target_selector.py --model {model-id} {bundle-or-all} --current --json
```

### 3. Review remaining pairs

Group the remaining pairs by note.

If the remaining execution set is one gate across many notes, prefer:

```bash
python3 scripts/run_gate_sweep.py --runner {codex|claude-code} --model {model-id} [--current] [--note {note-paths} ...] {gate-id}
```

This batches notes into one prompt while still recording one review run per note.

If there are many notes, use:

```bash
scripts/review_sweep.sh --model {model-id} {bundle-or-all} {note-paths...}
```

Or:

```bash
scripts/review_sweep.sh --model {model-id} --current {bundle-or-all}
```

`review_sweep.sh` runs note-local bundle reviews in parallel, up to 4 at a time by default. Override with `REVIEW_SWEEP_JOBS=<n>` if needed.

Example for current notes in Codex:

```bash
scripts/review_sweep.sh --model gpt-5-4-xhigh --runner codex --current semantic
```

If you are executing manually from the shell, run one bundle wrapper per note:

```bash
python3 scripts/run_review_bundle.py --runner {codex|claude-code} --model {model-id} {note-path} {gate-id-1} {gate-id-2} ...
```

If you are executing from an agent harness, run `kb/instructions/run-review-bundle-on-note.md` once per note instead of nesting `run_review_bundle.py` inside another agent.

Multiple note-local runs can execute in parallel since each note's reviews are independent.

### 4. Report

Report which pairs were reviewed and which were acked.

## Do not

- Do not ack when the diff is significant. The purpose of the review is to catch problems the diff introduces.
- Do not skip `note-changed` entries without inspecting the diff.
