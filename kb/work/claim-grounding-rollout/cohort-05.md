# Cleanup cohort 05 — frozen 2026-08-24

Frozen at repository `15f4080f`. Follow [the procedure](./procedure.md)
and its **Executing a cohort** section, which carries the literal grounding and
re-ingest routes and explains why the claim inventory must precede source reading.

**Disjointness.** This cohort's notes and ingests are disjoint from every other
cohort's, on both axes — no two agents append to the same `Claims` section or
edit the same note. Cohorts 02–07 may therefore run fully in parallel.

Snapshot volume: 0.31 MB across 5 ingests.

## Targets

| Target | Blob | Ingests |
|---|---|---|
| `bounded-context-orchestration-model` | `b06b3041` | `context-providers-the-missing-layer-between-agents-and-tools` |
| `final-task-success-does-not-establish-intended-path-health` | `18fd0bf0` | `the-self-healing-agent-harness-2048912026018484317` |
| `maintenance-capacity-must-match-harmful-artifact-inflow` | `254e5e7f` | `hacker-news-ai-dr-ai-didnt-read` |
| `oracle-accumulation-improves-the-selection-environment` | `e40efdea` | `harness-engineering-leveraging-codex-agent-first-world` |
| `world-models-assess-explanatory-reach-through-action-conditioned` | `48a31ff4` | `why-ai-systems-dont-learn-and-what-to-do-about-it` |

## Your first task

Inventory each target's load-bearing claims **from the note itself, before
reading any source**, as a table of `ID | target | claim as frozen | source-side
need`. [Cohort 01](./cohort-01.md) is the shape. Then ground, disposition,
repair, and record — one row per claim use, not per note.

## Completion record

| ID | Disposition | Target change | Validation |
|---|---|---|---|
| | | | |
