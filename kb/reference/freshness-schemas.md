---
description: "Canonical JSON shapes for commonplace-freshness-status, accept, ack, and retire (v1: review-pair targets, file-text inputs)"
type: kb/types/note.md
tags: []
---

# Freshness JSON contracts (v1)

Canonical shapes for `commonplace-freshness-status`, `accept`, `ack`, and `retire`.

**v1 scope:** `review-pair` targets, `file-text` inputs. Non-review examples live in [collection-as-artifact freshness](./proposals/collection-as-artifact-freshness.md).

Target keys: sorted keys, compact separators before persistence. CLI may pretty-print; compare canonically.

## Target identity

```json
{
  "target_kind": "review-pair",
  "target_key": {
    "criterion_path": "kb/instructions/review-gates/prose/source-residue.md",
    "model_partition": "codex",
    "note_path": "kb/notes/example.md"
  }
}
```

## Input observation

```json
{
  "input_role": "note",
  "artifact_path": "kb/notes/example.md",
  "version_kind": "file-text",
  "content_sha256": "64 lowercase hex",
  "content_text": "exact UTF-8 text"
}
```

`content_text` required in accept manifests; optional in status without `--diff`.

## Changed input (status)

```json
{
  "input_role": "criterion",
  "artifact_path": "kb/instructions/critique-note.md",
  "version_kind": "file-text",
  "status": "input-changed",
  "accepted_snapshot_id": 12,
  "accepted_content_sha256": "…",
  "current_content_sha256": "…",
  "diff": "optional unified diff when --diff"
}
```

`status`: `input-changed` | `input-missing` | `version-error`.

## Status (`commonplace-freshness-status --json`)

```json
{
  "schema": "commonplace-freshness-status/1",
  "generated_at": "ISO-8601 UTC",
  "exit_class": "fresh",
  "targets": []
}
```

`exit_class`: `fresh` | `stale` | `error`. Stale target entry:

```json
{
  "target_kind": "review-pair",
  "target_key": { "...": "..." },
  "baseline_revision": 3,
  "accepted_at": "ISO-8601 UTC",
  "changed_inputs": []
}
```

Fresh targets only with `--all`. Ack copies `baseline_revision` and intended `current_content_sha256` values.

## Accept (`commonplace-freshness-accept --input -`)

```json
{
  "schema": "commonplace-freshness-accept/1",
  "target_kind": "example-target",
  "target_key": { "...": "..." },
  "transition": "refresh",
  "expected_baseline_revision": 3,
  "inputs": {
    "primary": {
      "input_role": "primary",
      "artifact_path": "kb/example.md",
      "version_kind": "file-text",
      "content_sha256": "64 lowercase hex"
    }
  }
}
```

Observation refresh or initial acceptance. **`review-pair` rejected in v1.** Non-review manifests ship with first non-review target kind.

`transition`: `initial` (`expected_baseline_revision: null`) or `refresh` (must match current revision). All registered roles required; hashes must match live resolution at commit.

## Ack (`commonplace-freshness-ack --input -`)

```json
{
  "schema": "commonplace-freshness-ack/1",
  "target_kind": "review-pair",
  "target_key": { "...": "..." },
  "expected_baseline_revision": 3,
  "selected_inputs": [
    {
      "input_role": "note",
      "artifact_path": "kb/notes/example.md",
      "version_kind": "file-text",
      "content_sha256": "from status current_content_sha256"
    }
  ]
}
```

Omitted `selected_inputs` → all changed inputs from paired status. Review evidence preserved automatically.

## Retire (`commonplace-freshness-retire --input -`)

```json
{
  "schema": "commonplace-freshness-retire/1",
  "target_kind": "review-pair",
  "target_key": { "...": "..." }
}
```

Idempotent when target already absent.

## Exit codes

| condition | exit |
|---|---:|
| all selected targets fresh | 0 |
| any `input-changed` or `input-missing` | 1 |
| misuse, `version-error`, store error, failed CAS | 2 |