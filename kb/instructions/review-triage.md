---
description: Inspect diffs for note-changed assay pairs and acknowledge changes that do not invalidate their existing evidence
type: kb/types/instruction.md
---

# Review triage

Inspect `note-changed` stale pairs and acknowledge those where the diff does not invalidate the existing evidence for that criterion. This reduces the assay queue before launching workers. For closed-ended verdict pairs, ack carries the outcome forward; for open-ended report pairs, it only reuses the report as fresh evidence and does not imply that its findings were handled.

Inputs:

- `{model-partition}` — the freshness partition whose existing evidence may be carried forward
- `{criteria}` — gate ids, bundle names, conformance requests, or the opt-in `critique` report assay; `--all-gates` selects verdict criteria only
- `{note-scope}` — one or more note paths or directories to limit scope

## Steps

### 1. Capture note-changed candidates

```bash
commonplace-review-target-selector --model-partition {model-partition} {criteria} --note {note-scope} --json --reason note-changed > {ack-manifest}
```

If the output object has `"targets": []`, stop — nothing to triage.
Keep this exact file: its baseline revisions and current hashes bind the later
acknowledgement to what you inspect.

### 2. For each note-changed pair, judge the diff

For each entry in `targets`, read `reasons`, every item in `changed_inputs`,
`criterion_id`, and `result_kind`. A joint note-and-criterion edit is returned
by the note filter but still carries both changes. Ask whether each diff
invalidates what the criterion's existing result says.

Guidelines:

- A typo fix, whitespace change, or link-text tweak is insignificant for almost every gate.
- A rewording of a claim is significant for `semantic/grounding-alignment` and `semantic/internal-consistency` but probably not for `structural/general-before-specific`.
- Adding or removing a section is significant for `prose/proportion-mismatch` and `semantic/completeness-boundary-cases`.
- Adding or removing a source citation is significant for `prose/orphan-references` and `semantic/grounding-alignment`.

When in doubt, do not ack — rerun the assay.

### 3. Retain only authorized observations

Edit `{ack-manifest}` so `targets` contains only pairs authorized for
acknowledgement. For a joint edit, retain every harmless `changed_inputs` item
and its corresponding reason; remove a role that must stay stale for rereview.
Do not update hashes, snapshot ids, paths, or baseline revisions.

### 4. Ack the inspected candidates

```bash
commonplace-ack-review --input {ack-manifest}
```

This advances only the retained input roles while preserving the evidence
review pair. An intervening file edit or baseline transition fails instead of
accepting uninspected state. It produces no new judgment and does not rely on
`touch` or filesystem timestamps.

### 5. Report

Report which pairs were acked and which were left for review. The remaining stale pairs will be picked up by the next review sweep.
