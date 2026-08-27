# RF-18 — Snapshot-route telemetry prices the wrong artifact

**State:** open  
**Repair shape:** local telemetry correction  
**Severity:** low

## Finding

For `(snapshot required)` grounding, the worker is supposed to read the derived
snapshot, but availability, size, and consumption telemetry charge the linked
ingest path. The snapshot may be much larger, so the recorded context cost does
not describe the artifact actually consumed.

## Evidence

- [`resolve_note_markdown_links()`](../../../src/commonplace/review/job_prompt.py)
  intentionally prices the ingest while checking only snapshot availability.
- [The prompt protocol](../../../src/commonplace/review/protocol/prompt.py) tells
  workers to report the ingest path for this route.
- [`test_resolve_note_markdown_links_does_not_charge_required_snapshot_in_v1`](../../../tests/commonplace/review/test_job_prompt.py)
  fixes the mismatch as current expected behavior.

## Why it matters

Telemetry cannot support prompt-cost, reading-budget, or capacity decisions if
the charged object is not the object read. The mismatch also obscures the exact
evidence dependency described in RF-04.

## Provisional repair direction

Resolve snapshot-required links to both the logical ingest and the physical
consumption target. Charge the latter's bytes and require consumption metadata
to name it, while preserving the ingest as lineage metadata.

## Done when

- Availability and consumption telemetry name the derived snapshot.
- Charged bytes equal the actual snapshot size.
- The ingest-to-snapshot lineage remains explicit.
- The existing V1 mismatch test is replaced by the intended behavior.
