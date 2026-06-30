# Workshop: review-execution-pipeline

## Question

Can review execution be represented as one queued-job pipeline with pluggable execution media, instead of separate subprocess, live-agent, batch-prepare, and batch-ingest paths?

## Why this workshop exists

The current review subsystem already has the right low-level abstraction: each emitted review block is keyed by `(note_path, gate_path)` and parsed through one pair protocol. The model partition comes from the enclosing execution record and is retained in persistent review/acceptance state; current acceptances are keyed by `(note_path, gate_path, model_partition)`. The remaining complexity is orchestration. Several modules still perform variants of the same sequence:

1. resolve requested notes and gates;
2. capture note/gate snapshots;
3. create a persisted execution record and pair rows;
4. render the prompt;
5. execute or suspend for an external executor;
6. parse output;
7. finalize pairs, runs, artifacts, and acceptances.

The variants are legitimate, but the code shape duplicates policy:

- [executor.py](../../../src/commonplace/review/executor.py) owns subprocess execution and shared parse/finalize behavior.
- [batch.py](../../../src/commonplace/review/batch.py) exposes deterministic prepare/ingest endpoints for external executors.
- [run_review_bundles.py](../../../src/commonplace/review/run_review_bundles.py) creates note-packed subprocess runs.
- [run_gate_sweep.py](../../../src/commonplace/review/run_gate_sweep.py) creates gate-packed subprocess runs.
- [create_review_runs.py](../../../src/commonplace/cli/review/create_review_runs.py) wraps batch preparation for the live-agent single-note flow.

This workshop isolates the pipeline simplification from the larger review-store source-of-truth question in [src-architecture-alternatives](../src-architecture-alternatives/README.md).

## Scope

In scope:

- pipeline stage boundaries for review execution;
- a shared queued-job schema and stage result used by subprocess and external executors;
- eliminating duplicated prompt/artifact/finalization paths where behavior should not diverge;
- preserving the flat CLI entry points that agents call by bare command name;
- the queue/job schema changes: add `queued`, make job timing honest, mechanically rename `review_runs` / `review_run_id` to `review_jobs` / `review_job_id`, drop pair-level `model_partition`, and make ack carry forward an existing review pair.

Out of scope:

- changing the pair sentinel grammar;
- changing review freshness semantics beyond the queued-job and ack carry-forward decisions captured here;
- changing the review-store source-of-truth shape, which remains owned by [src-architecture-alternatives](../src-architecture-alternatives/README.md);
- replacing subprocess runner adapters, which are already a clean boundary.

## Working Hypothesis

The minimal useful refactor is not a new framework. It is a small pipeline core around persisted review jobs:

- `select`: produce a stable stale-target list;
- `prepare`: normalize pairs, filter applicability, capture snapshots, create queued job/pair rows, build targets, compute artifact paths;
- `render`: write or return the prompt for a chosen output mode;
- `queue`: leave prepared jobs available for a subprocess worker, live-agent worker, or external orchestrator;
- `execute`: claim or dispense queued jobs through a subprocess runner, live-agent worker, or external orchestrator-owned step;
- `finalize`: parse bundle output and finalize with the same salvage policy.

`commonplace-review-target-selector`, `commonplace-create-review-jobs`, `commonplace-run-review-jobs`, and `commonplace-finalize-review-job` become the canonical stages. Existing convenience commands either compose those stages or retire.

## First Work

1. Inventory the run/job creation paths and list the exact data each caller needs back. Initial inventory: [scenario-inventory.md](./scenario-inventory.md).
2. Stabilize the target-list producer contract from `commonplace-review-target-selector --json`.
3. Map current callers onto queued job rows and the command JSON returned by create/list commands.
4. Identify a first patch that introduces `queued`, honest job timing, job-owned bundle output, and review-provenance-preserving ack semantics.

## Working Files

- [scenario-inventory.md](./scenario-inventory.md) - current execution, selection, ingest, and acknowledgement scenarios the pipeline design must preserve.
- [queue-oriented-pipeline.md](./queue-oriented-pipeline.md) - proposed selector to queued jobs to queue-worker command shape, with parallelism moved into queue execution.
- [phase-1-honest-job-state.md](./phase-1-honest-job-state.md) - implemented first phase: migration substrate plus the `queued` status and honest clock, on current table names.
- [phase-2-mechanical-job-rename.md](./phase-2-mechanical-job-rename.md) - **ready to implement**: mechanical run to job rename, using schema version 2 and preserving Phase 1 behavior while keeping pair vocabulary.
- [phase-3-job-creation-and-listing.md](./phase-3-job-creation-and-listing.md) - ready to implement: concrete model-specific selector JSON handoff, queued job creation, shared job plan, and job listing.
- [phase-4-job-owned-finalization.md](./phase-4-job-owned-finalization.md) - planned: parent-dispatch claiming, finalize by job id using the job-owned output path, write result provenance frontmatter, and retire explicit ingest surfaces.
- [phase-5-subprocess-job-runner.md](./phase-5-subprocess-job-runner.md) - planned: subprocess workers claim queued jobs, run adapters, and finalize through the shared path.
- [phase-6-ack-provenance.md](./phase-6-ack-provenance.md) - implemented: new ack writes carry forward existing review evidence; legacy nullable cleanup is deferred.
- [phase-7-no-review-relocation.md](./phase-7-no-review-relocation.md) - ready to finish implementation: relocation no longer rekeys review state.
- [phase-8-docs-adr-and-workshop-close.md](./phase-8-docs-adr-and-workshop-close.md) - planned: promote ADR/reference docs and close the workshop.
- [adr-draft-034-queued-review-jobs-and-execution-provenance.md](./adr-draft-034-queued-review-jobs-and-execution-provenance.md) - draft ADR for the queued-job SQL model, execution provenance columns, and two execution paths.
- [implementation-plan.md](./implementation-plan.md) - the remaining queued-job refactor plan; Phase 1 has landed, everything else is Phase 2.

## Closure Conditions

Close when this workshop produces one of:

- a scoped implementation plan with tests and the queue/job schema changes listed in this workshop;
- a promoted ADR/reference update if the pipeline boundary becomes architectural;
- an explicit decision to keep the paths separate, with the reason and the cost of duplication accepted.
