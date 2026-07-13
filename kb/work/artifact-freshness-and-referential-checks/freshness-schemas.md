# Freshness JSON contracts

Canonical shapes for `commonplace-freshness-status`, `commonplace-freshness-accept`, and `commonplace-freshness-ack`. Target keys use sorted keys and compact separators before persistence; CLI JSON may pretty-print but must compare canonically.

## Shared fragments

### Target identity

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

```json
{
  "target_kind": "collection-maintenance",
  "target_key": {
    "collection_path": "kb/lhc/notes"
  }
}
```

### Input observation

```json
{
  "input_role": "note",
  "artifact_path": "kb/notes/example.md",
  "version_kind": "file-text",
  "content_sha256": "64 lowercase hex",
  "content_text": "exact UTF-8 text"
}
```

`content_text` is required in accept manifests and optional in status output when `--diff` is off.

### Changed input (status)

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

`status` is one of `input-changed`, `input-missing`, or `version-error`.

## Status output (`commonplace-freshness-status --json`)

Top-level object:

```json
{
  "schema": "commonplace-freshness-status/1",
  "generated_at": "ISO-8601 UTC timestamp",
  "exit_class": "fresh",
  "targets": []
}
```

`exit_class` is `fresh`, `stale`, or `error`. Each stale target entry:

```json
{
  "target_kind": "review-pair",
  "target_key": { "...": "..." },
  "baseline_revision": 3,
  "accepted_at": "ISO-8601 UTC timestamp",
  "changed_inputs": [
    { "...": "changed input object" }
  ]
}
```

Fresh targets appear only with `--all`. The payload is the canonical observation source for acknowledgement: ack must copy `baseline_revision` and the `current_content_sha256` values it intends to accept.

## Accept manifest (`commonplace-freshness-accept --input -`)

Observation refresh or initial acceptance only. `target_kind = review-pair` is rejected.

```json
{
  "schema": "commonplace-freshness-accept/1",
  "transition": "initial",
  "target_kind": "collection-maintenance",
  "target_key": {
    "collection_path": "kb/lhc/notes"
  },
  "expected_baseline_revision": null,
  "inputs": [
    {
      "input_role": "casebook",
      "artifact_path": "kb/lhc/notes",
      "version_kind": "collection-text",
      "content_sha256": "…",
      "content_text": "COMMONPLACE-COLLECTION-TEXT/1\n…"
    }
  ]
}
```

`transition` is `initial` or `refresh`. For `initial`, `expected_baseline_revision` must be `null`. For `refresh`, it must equal the current baseline revision. Every registered input role for the target must appear exactly once with observations whose hashes match live resolution at commit time.

## Ack manifest (`commonplace-freshness-ack --input -`)

Subset or full advance from a status observation. Review evidence is preserved automatically for `review-pair` targets.

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
      "content_sha256": "hash copied from status current_content_sha256"
    }
  ]
}
```

Omitted `selected_inputs` means all changed inputs from the paired status payload. Each selected hash must still match live resolution when the transaction commits.

## Retire manifest (`commonplace-freshness-retire --input -`)

```json
{
  "schema": "commonplace-freshness-retire/1",
  "target_kind": "review-pair",
  "target_key": { "...": "..." }
}
```

Retirement succeeds idempotently when the target is already absent.

## Exit codes

| condition | exit |
|---|---:|
| all selected targets fresh | 0 |
| any `input-changed` or `input-missing` | 1 |
| CLI misuse, `version-error`, malformed store, failed CAS | 2 |