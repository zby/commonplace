---
description: "Superseded historical decision: batch prepare/ingest endpoints and runner adapters were replaced by queued jobs and parent-dispatched workers"
type: ../types/adr.md
tags: []
status: superseded
---

# 030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters

**Status:** superseded by [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md) and the current parent-dispatched workflow
**Date:** 2026-06-12

## Context

Review execution needed a seam where deterministic Python prepared review work and an external agent or harness supplied semantic judgment. This ADR recorded an intermediate design after [ADR 029](./029-review-execution-unified-on-note-gate-pairs.md):

1. batch-granular prepare/ingest endpoints for external executors;
2. adapter objects for subprocess harness CLIs.

The current system keeps the useful seam but removes the subprocess dispatch layer. `commonplace-create-review-jobs` creates queued jobs from selector JSON, workers write only the job-owned output file, and `commonplace-finalize-review-job` records optional provenance, parses, and finalizes that output. The parent agent or harness owns fan-out and model calls.

## Decision

1. **Deterministic endpoints remain.** Job creation and finalization are stable command boundaries around prompt artifacts and database state.
2. **Subprocess execution is removed.** Commonplace no longer owns model invocation, vendor CLI command construction, stream decoding, or telemetry scraping. Those belong to the parent harness if needed.
3. **The review protocol remains shared.** The pair grammar, parser, and result artifacts from ADR 029 are still the boundary between workers and finalization. ADR 035 later made live finalization all-or-nothing.

## Consequences

Easier:
- Harness-orchestrated review composes from existing endpoints: selector JSON -> queued jobs -> worker output -> finalize. Parallelism, budgets, and retries belong to the orchestrator.
- Vendor CLI churn no longer touches Commonplace review code.
- The command surface is smaller and has one execution story.

Harder / accepted costs:
- Job creation still supports only note or gate packing until a mixed-packing caller needs a stronger manifest and naming contract.
- Commonplace cannot enforce worker-level retries or concurrency; the parent harness owns them.

---

Relevant Notes:

- [review architecture](../review-architecture.md) — part-of: the subsystem these seams expose
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — see-also: the pair protocol these endpoints surface to external executors
- [035-review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — supersedes-in-part: removes claim and partial salvage from the live workflow
- [Claude Code dynamic workflows](../../agentic-systems/claude-code-dynamic-workflows.md) — abstracted-from: the harness orchestration model (script coordinates, agents execute, deterministic endpoints at the edges) these seams are shaped for
