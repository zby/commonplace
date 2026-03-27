---
description: Inspect diffs for note-changed review pairs and ack insignificant changes — run before a review sweep to reduce the review queue
---

# Review triage

Inspect `note-changed` stale pairs and ack those where the diff is insignificant for the gate. This reduces the review queue before launching review sub-agents or a bash sweep script.

Inputs:

- `{bundle-or-all}` — a bundle name (e.g. `prose`, `semantic`) or `--all-gates`
- `{note-paths}` (optional) — one or more note paths to limit scope

## Steps

### 1. Get note-changed pairs

```bash
uv run scripts/gate_selector.py {bundle-or-all} {note-paths} --json
```

Filter the output to entries with `"reason": "note-changed"`. These are the only entries that need triage — `missing-review` and `gate-changed` always need a fresh review.

If there are no `note-changed` entries, stop — nothing to triage.

### 2. For each note-changed pair, judge the diff

For each entry, read the `diff` field and the `gate_id`. Ask: does this diff affect what the gate tests?

Guidelines:

- A typo fix, whitespace change, or link-text tweak is insignificant for almost every gate.
- A rewording of a claim is significant for `semantic/grounding-alignment` and `semantic/internal-consistency` but probably not for `structural/broken-link-path`.
- Adding or removing a section is significant for `prose/proportion-mismatch` and `semantic/completeness-boundary-cases`.
- Adding or removing a source citation is significant for `prose/orphan-references` and `semantic/grounding-alignment`.

When in doubt, don't ack — let the review handle it.

### 3. Ack insignificant pairs

For each pair judged insignificant, get the review file path:

```bash
uv run scripts/resolve_gates.py --note {note-path} {gate-id}
```

Then ack:

```bash
touch {review-file-path}
```

### 4. Report

Report which pairs were acked and which were left for review. The remaining stale pairs will be picked up by the next review sweep or bash sweep script.
