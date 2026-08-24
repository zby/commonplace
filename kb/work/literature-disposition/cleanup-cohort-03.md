# Cleanup cohort 03 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./cleanup-procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.13 MB across 2 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `automating-kb-learning-is-an-open-problem` | `f559cd84` | `knowledge-centric-self-improvement-2607.19592` |
| `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts` | `b5b8d2b2` | `build-systems-a-la-carte` |
| `first-principles-analysis-maps-design-space-before-selection` | `4d105602` | `build-systems-a-la-carte` |
| `moving-the-interpretation-enforcement-boundary-requires-coverage` | `398209d3` | `knowledge-centric-self-improvement-2607.19592` |
| `topology-isolation-and-verification-form-a-causal-chain-for-reliable` | `7917a770` | `knowledge-centric-self-improvement-2607.19592` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cleanup-cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Completion record

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| | | | |
