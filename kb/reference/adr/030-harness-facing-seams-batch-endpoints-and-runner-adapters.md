---
description: "Superseded historical decision: batch prepare/ingest endpoints and runner adapters were replaced by queued jobs and parent-dispatched workers"
type: ../types/adr.md
tags: []
status: superseded
---

# 030-Harness-facing seams: batch prepare/ingest endpoints and runner adapters

**Status:** superseded by [034-Queued review jobs and execution provenance](./034-queued-review-jobs-and-execution-provenance.md)
**Date:** 2026-06-12

## Context

Review execution needs a seam where deterministic Python prepares review work and an external agent or harness supplies semantic judgment. After [ADR 029](./029-review-execution-unified-on-note-gate-pairs.md) fixed the pair protocol, the open question was what shape that seam should take for external executors.

## Decision

Expose batch-granular prepare and ingest endpoints as stable command boundaries around prompt artifacts and database state, and add adapter objects that dispatch subprocess harness CLIs. The pair grammar, parser, and result artifacts from ADR 029 remain the shared boundary between executors and ingestion.

## Consequences

Harness-orchestrated review composes from deterministic endpoints, with parallelism, budgets, and retries owned by the orchestrator. Owning subprocess dispatch tied Commonplace to vendor CLI command construction, stream decoding, and telemetry scraping; ADR 034 kept the endpoint seam and removed the adapter layer, so Commonplace does not own model invocation and the parent harness does.

---

Relevant Notes:

- [review architecture](../review-architecture.md) — part-of: the subsystem these seams expose
- [029-review execution unified on (note, gate) pairs](./029-review-execution-unified-on-note-gate-pairs.md) — see-also: the pair protocol these endpoints surface to external executors
- [035-review jobs finalize all-or-nothing with derived artifacts](./035-review-jobs-finalize-all-or-nothing-with-derived-artifacts.md) — supersedes-in-part: removes claim and partial salvage from the live workflow
- [Claude Code dynamic workflows](../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — abstracted-from: the harness orchestration model (script coordinates, agents execute, deterministic endpoints at the edges) these seams are shaped for
