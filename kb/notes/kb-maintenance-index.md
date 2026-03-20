---
description: Index of notes about keeping the KB healthy over time — detection of staleness and quality degradation, maintenance operations, and the dynamics that govern system entropy
type: index
status: current
---

# KB maintenance

How an agent-operated KB stays healthy as it grows. Detection, operations, and the dynamics that govern quality over time. For how the KB is *built*, see [tags](./tags-index.md). For document structure, see [document-system](./document-system-index.md).

## Dynamics

- [entropy-management-must-scale-with-generation-throughput](./entropy-management-must-scale-with-generation-throughput.md) — cleanup throughput must match generation throughput; agents replicate patterns including bad ones, so without proportional maintenance quality degrades with volume
- [traversal-improves-the-graph](./traversal-improves-the-graph.md) — every traversal is a read-write opportunity; agents should log improvement opportunities during reading, then process them separately to avoid context-switching
- [title-as-claim-exposes-commitments-enabling-popperian-maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — claim titles make maintenance cheap: scan the index, ask "do I still believe this?", open only the doubtful ones

## Detection

- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — composite oracle from graph-topology, content-proxy, and LLM-hybrid signals; the evaluation layer the learning loop needs
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — note quality scores (status, type, inbound links, recency) filter /connect candidates as the KB grows
- [semantic-review-catches-content-errors-that-structural-validation-cannot](./semantic-review-catches-content-errors-that-structural-validation-cannot.md) — four semantic checks (enumeration completeness, grounding alignment, boundary-case coverage, internal consistency) that require LLM adversarial reading
- [link-graph-plus-timestamps-enables-make-like-staleness-detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — existing links encode dependencies; comparing note and target timestamps flags staleness without new annotation
- [stale-indexes-are-worse-than-no-indexes](./stale-indexes-are-worse-than-no-indexes.md) — a missing index entry suppresses search entirely; absence of an index degrades to search, presence of a stale index prevents it
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — successful runs can still conceal broken helpers and paths; maintenance needs log sweeps or other observability for hidden failures

## Operations

- [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — staging catalogue for periodic operations before they are distilled into reusable procedures
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) — periodic audits belong in externally triggered operations, not always-loaded routing docs

## Related Tags

- [tags](./tags-index.md) — parent area: architecture and design of the KB itself
- [document-system](./document-system-index.md) — type system and validation that maintenance operations check against
- [links](./links-index.md) — linking methodology that staleness detection and quality signals operate on

## Other tagged notes <!-- generated -->

- [Brainstorming: how reach informs KB design](./brainstorming-how-reach-informs-kb-design.md) — Brainstorming on Deutsch's "reach" concept applied to KB notes — reach is a maintenance risk signal (not a retrieval signal) because high-reach revisions break downstream reasoning silently
- [Title as claim makes overlap between notes visible](./title-as-claim-makes-overlap-between-notes-visible.md) — When note titles are claims, overlap between notes is visible at the index level — similar assertions are obvious without opening files; topical titles hide overlap behind different labels for the same territory
- [Traditional debugging intuitions break when tool loops can recover semantically](./traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) — Programmers trained on traditional software expect broken infrastructure to fail loudly; semantic recovery in agent tool loops violates that expectation, so successful outcomes can create false confidence during debugging and maintenance
