# RF-18 — Snapshot-route telemetry prices the wrong artifact

**State:** fixed 2026-08-27
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
- [The former V1 regression in `test_job_prompt.py`](../../../tests/commonplace/review/test_job_prompt.py)
  fixed the mismatch as expected behavior before this repair.

## Why it matters

Telemetry cannot support prompt-cost, reading-budget, or capacity decisions if
the charged object is not the object read. The mismatch also obscures the exact
evidence dependency described in RF-04.

## Provisional repair direction

Resolve snapshot-required links to the logical ingest and both physical inputs
the grounding check consumes: ingest metadata and derived snapshot bytes. Charge
both files and require consumption metadata to name each one actually opened.

## Done when

- Availability and consumption telemetry name the ingest and derived snapshot.
- Charged bytes equal both files' actual whole-file sizes.
- The logical ingest-to-physical-input routes remain explicit.
- The existing V1 mismatch test is replaced by the intended behavior.

## Resolution

Resolved links now distinguish one `link_target_path` from one or more physical
consumption targets. Ordinary routes map the path to itself. A `(snapshot
required)` route maps the linked ingest to both the ingest and its derived
snapshot, using each file's actual size. Availability schema v3 exposes both
route mappings, separate logical and physical counts, and both priced artifacts.
The generated prompt requires `opened_paths` to name each physical target the
reviewer opened. Consumption schema v2 then prices those reported paths. Tests
cover resolution, missing snapshots, prompt instructions, multi-target lineage
telemetry, combined byte cost, and the logical-count/physical-cost boundary.
