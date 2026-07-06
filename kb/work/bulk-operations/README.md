# Workshop: Bulk Operations

## Question

How should Commonplace plan, shard, execute, validate, merge, and close operations that touch many artifacts without mixing selection, per-target work, review, and promotion authority into one overloaded task?

## Why this replaces ingestion-and-deep-search

The older `ingestion-and-deep-search` workshop asked how agents should run deep search over a KB without mixing discovery, source processing, synthesis, and promotion. That was a real case, but it is now one instance of a broader problem. The same shape appears in review reruns, connect-report triage, source re-ingest, whole-corpus type migrations, validation sweeps, matrix refreshes, relocation moves, and future lineage-driven refresh.

This workshop keeps the deep-search lesson, but generalizes the frame from "research over sources" to **bulk operations over KB artifacts**.

## Current Claim

A safe bulk operation is a staged context-engineering pipeline, not one long agent task.

The recurring stages are:

1. **Select** - identify targets and record why each target is in scope.
2. **Classify** - decide the operation class per target: read-only review, source processing, rewrite, move, merge-back, validation, or promotion candidate.
3. **Shard** - split work into bounded packets with explicit input paths, output paths, authority, and collision boundaries.
4. **Execute** - run each packet in a clean context or deterministic command, writing only its owned artifact(s).
5. **Integrate** - inspect outputs, apply valid changes, regenerate derived views, and leave uncertain findings as follow-up state.
6. **Validate** - run structural checks, semantic gates, or command-specific verification appropriate to the authority of the outputs.
7. **Close** - either promote durable conclusions, update the operating instruction/command, or delete the workshop state.

This separates judgment-heavy target selection from focused execution and keeps promotion authority out of intermediate reports.

## Case Families

Use these existing workflows as witnesses:

- **Deep research / directed reading** - source discovery, snapshot/ingest, instruction packet, clean-context synthesis, and promotion decision.
- **Agent-memory review reruns** - select rows from `systems.csv`, dispatch one source-grounded worker per review, edit only the review, then regenerate the matrix.
- **Review batches** - selector JSON, queued jobs, one output file per job, finalization, and freshness verification.
- **Connect maintenance triage** - scan generated reports, extract maintenance observations, classify each as done/open/moved/watch, and promote only the durable residue.
- **Source re-ingest / bulk import** - preserve source boundaries, update ingests, detect downstream references, and avoid promoting raw source claims directly.
- **Whole-corpus migrations** - type migration, path rewrites, directory relocation, link rewriting, generated-index refresh, and rollback boundaries.
- **Validation sweeps** - deterministic structural checks, semantic gates, and corpus-level consistency checks with different oracle strengths.
- **Lineage-driven refresh** - a future freshness layer emits refresh targets, but execution remains owned by review, connect, source-processing, or agent workflows.

## Design Questions

- What minimal run record should every bulk operation keep: target list, source revision, output paths, model/tool provenance, decisions, skipped targets, and residual warnings?
- When should the target list be a committed artifact, a gitignored report, a SQLite state row, or just command output?
- What should be deterministic selection versus agent judgment?
- Which operations can safely run in parallel, and what write scopes make conflicts impossible?
- How should a parent agent merge worker outputs without silently laundering uncertain findings into library artifacts?
- What validation is proportional to each output's behavioral authority?
- When should a recurring bulk operation become a command, a skill, an instruction, or a review-system feature?

## Retained Inputs From Deep Search

- [Directed-reading contract inventory](./directed-reading-inventory.md) - map of stable and ad hoc reading contracts that already exist in the KB.
- [Instructions: A-MEM automation-quality trade-off](./instructions-amem-automation-quality.md) - concrete example of a frontloaded instruction packet used in an experiment.

These files are historical inputs to the broader bulk-operations pattern. They should be revised or promoted only if the new frame needs a durable directed-reading subpattern.

## What Would Close This Workshop

Close when this workshop produces one of:

- a reusable bulk-operation runbook under `kb/instructions/`;
- a skill or command contract for recurring bulk operations;
- a reference design for target selection, sharding, output ownership, provenance, merge-back, and validation;
- or a decision that existing domain-specific workflows are sufficient, with the boundary conditions named.

Before closing, remove stale active-workshop entries for superseded or missing workshops and decide whether the directed-reading files above should be promoted, retained as examples, or deleted.
