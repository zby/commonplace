---
description: Inspect diffs for note-changed assay pairs and acknowledge changes that do not invalidate their existing evidence
type: kb/types/instruction.md
---

# Review triage

Inspect `note-changed` stale pairs and acknowledge those where the diff does not invalidate the existing evidence for that criterion. This reduces the assay queue before launching workers. For closed-ended verdict pairs, ack carries the decision forward; for open-ended report pairs, it only reuses the report as fresh evidence and does not imply that its findings were handled.

Inputs:

- `{model-partition}` — the freshness partition whose existing evidence may be carried forward
- `{criteria}` — gate ids, bundle names, conformance requests, or the opt-in `critique` report assay; `--all-gates` selects verdict criteria only
- `{note-scope}` — one or more note paths or directories to limit scope

## Steps

### 1. Get note-changed pairs

```bash
commonplace-review-target-selector --model-partition {model-partition} {criteria} --note {note-scope} --json --reason note-changed
```

If the output object has `"targets": []`, stop — nothing to triage.

### 2. For each note-changed pair, judge the diff

For each entry in `targets`, read the `diff`, `gate_id`, and `result_kind`. Ask: does this diff invalidate what the criterion's existing result says?

Guidelines:

- A typo fix, whitespace change, or link-text tweak is insignificant for almost every gate.
- A rewording of a claim is significant for `semantic/grounding-alignment` and `semantic/internal-consistency` but probably not for `structural/general-before-specific`.
- Adding or removing a section is significant for `prose/proportion-mismatch` and `semantic/completeness-boundary-cases`.
- Adding or removing a source citation is significant for `prose/orphan-references` and `semantic/grounding-alignment`.

When in doubt, do not ack — rerun the assay.

### 3. Ack insignificant pairs

Ack all insignificant pairs in one command:

```bash
commonplace-ack-gate-review --model-partition {model-partition} {note-path} {gate-id} [{gate-id} ...]
```

This upserts the one current acceptance row so its snapshot baseline matches the current note and criterion while retaining the completed review pair as evidence. It produces no new judgment and does not rely on `touch` or filesystem timestamps.

### 4. Report

Report which pairs were acked and which were left for review. The remaining stale pairs will be picked up by the next review sweep.
