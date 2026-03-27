---
description: Batch review sweep — run the selector, triage note-changed pairs, review the rest in sub-agents
---

# Review sweep

Batch review across reviewable notes. Works with any bundle or all gates.

Inputs:

- `{bundle-or-all}` — a bundle name (e.g. `prose`, `semantic`, `frontmatter`) or `--all-gates`
- `{note-paths}` (optional) — one or more note paths to limit the sweep to specific notes

## Steps

### 1. Triage

Launch a sub-agent to run `kb/instructions/review-triage.md` with `{bundle-or-all}` and `{note-paths}`. This acks insignificant `note-changed` pairs, reducing the review queue.

### 2. Inventory

```bash
uv run scripts/gate_selector.py {bundle-or-all} {note-paths} --json | wc -l
```

Check the line count first (~5 lines per stale pair in JSON output).

- **0–2 lines** (empty array): stop — everything is fresh or acked.
- **More than 100 lines** (~20+ pairs): stop and tell the user to run `scripts/review_sweep.sh` instead. This instruction cannot orchestrate that many sub-agents.
- **Otherwise**: read the JSON output and continue.

```bash
uv run scripts/gate_selector.py {bundle-or-all} {note-paths} --json
```

### 3. Review in sub-agents

Group the remaining pairs by note. For each note, launch a sub-agent with a prompt to:

> Run `kb/instructions/run-review-bundle-on-note.md` on `{note-path}` for gates: `{gate-id-1} {gate-id-2} ...`

Multiple sub-agents can run in parallel since each note's reviews are independent.

### 4. Report

Report which pairs were reviewed and which were acked.

## Do not

- Do not ack when the diff is significant. The purpose of the review is to catch problems the diff introduces.
- Do not skip `note-changed` entries without inspecting the diff.
