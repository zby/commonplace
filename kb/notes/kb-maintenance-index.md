---
description: Index of notes about keeping the KB healthy over time — detection of staleness and quality degradation, maintenance operations, and the dynamics that govern system entropy
type: index
status: current
---

# KB maintenance

How an agent-operated KB stays healthy as it grows. Detection, operations, and the dynamics that govern quality over time. For how the KB is *built*, see [kb-design](./kb-design-index.md). For document structure, see [document-system](./document-system-index.md).

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

## Operations

- [maintenance-operations-catalogue-should-stage-distillation-into-instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — staging catalogue for periodic operations before they are distilled into reusable procedures
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) — periodic audits belong in externally triggered operations, not always-loaded routing docs

## Related Tags

- [kb-design](./kb-design-index.md) — parent area: architecture and design of the KB itself
- [document-system](./document-system-index.md) — type system and validation that maintenance operations check against
- [links](./links-index.md) — linking methodology that staleness detection and quality signals operate on

## All notes <!-- generated -->

- [Entropy management must scale with generation throughput](./entropy-management-must-scale-with-generation-throughput.md) — In agent-maintained systems, cleanup throughput must match generation throughput — agents replicate existing patterns including bad ones, so without proportional maintenance, quality degrades as a function of output volume
- [Link graph plus timestamps enables make-like staleness detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — Existing links already encode dependency information; comparing note and target timestamps flags notes that may be stale without any new annotation, analogous to make's file-based rebuild logic.
- [Maintenance operations catalogue should stage distillation into instructions](./maintenance-operations-catalogue-should-stage-distillation-into-instructions.md) — Catalogue of periodic KB maintenance operations and distillation status, used as a staging ground before promotion into kb/instructions procedures
- [Notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md) — As the KB grows, /connect will retrieve too many candidates — note quality scores (status, type, inbound links, recency, link strength) filter candidates and prioritise what's worth connecting
- [Periodic KB hygiene should be externally triggered, not embedded in routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing.md) — Periodic hygiene checks belong in externally triggered operations (user request, scheduler, CI), not in always-loaded routing instructions
- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — Catalogues graph-topology, content-proxy, and LLM-hybrid signals that could be combined into a weak composite oracle to drive a mutation-based KB learning loop without requiring usage data.
- [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation-cannot.md) — Four specific semantic checks (enumeration completeness, grounding alignment, boundary-case coverage, internal consistency) that require LLM adversarial reading — structural validation catches form errors but misses content errors like incomplete enumerations that contradict their own grounding definitions
- [Stale indexes are worse than no indexes](./stale-indexes-are-worse-than-no-indexes.md) — An agent trusts an index as exhaustive — a missing entry doesn't trigger search, it makes the note invisible
- [Title as claim exposes commitments, enabling Popperian maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — When an index is a list of claims rather than topics, reviewing the KB becomes scanning hypotheses — each title exposes its commitment and invites the question "do I still believe this?" without opening the file
- [Title as claim makes overlap between notes visible](./title-as-claim-makes-overlap-between-notes-visible.md) — When note titles are claims, overlap between notes is visible at the index level — similar assertions are obvious without opening files; topical titles hide overlap behind different labels for the same territory
- [Traversal improves the graph](./traversal-improves-the-graph.md) — Every traversal is a read-write opportunity — agents should log improvement opportunities during reading, then process them separately to avoid context-switching
