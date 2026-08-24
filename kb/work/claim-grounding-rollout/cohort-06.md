# Cleanup cohort 06 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.12 MB across 5 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision` | `2b29fb47` | `how-to-recursively-improve-your-agents-2084301728363462919` |
| `automated-synthesis-is-missing-good-oracles` | `8b89f83a` | `geometry-of-knowledge-extending-diversity-boundaries-llms` |
| `llm-generation-relaxes-goals-where-human-writing-stalls` | `29f897dd` | `borretti-human-routers-of-machine-words` |
| `structure-inference-needs-capture-at-the-decision-surface` | `2e01de4d` | `palantir-ontology-vs-decision-traces` **(blocked: no snapshot)** |
| `trace-extracted-memory-earns-authority-per-operation-not-at-capture` | `a4d17feb` | `trace-trajectory-attribution-for-automated-context-engineering` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Blocked

- `palantir-ontology-vs-decision-traces` — re-ingest before grounding

## Completion record

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| | | | |
