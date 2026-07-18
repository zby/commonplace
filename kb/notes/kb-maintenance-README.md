---
description: Index of notes about keeping the KB healthy over time — detection of staleness and quality degradation, maintenance operations, and the dynamics that govern system entropy
type: kb/types/tag-readme.md
index_source: tag
index_key: kb-maintenance
---

# KB maintenance

How an agent-operated KB stays healthy as it grows. Detection, operations, and the dynamics that govern quality over time. For how the KB is *built*, see [tags](./tags-README.md). For document structure, see [document-system](./document-system-README.md).

## Dynamics

- [entropy-management-must-scale-with-generation-throughput](./entropy-management-must-scale-with-generation-throughput.md) — cleanup throughput must match generation throughput; agents replicate patterns including bad ones, so without proportional maintenance quality degrades with volume
- [traversal-improves-the-graph](./traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md) — every traversal is a read-write opportunity; agents should log improvement opportunities during reading, then process them separately to avoid context-switching
- [title-as-claim-exposes-commitments-enabling-popperian-maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — claim titles make maintenance cheap: scan the index, ask "do I still believe this?", open only the doubtful ones

## Detection

- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — composite oracle from graph-topology, content-proxy, and LLM-hybrid signals; the evaluation layer the learning loop needs
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — recomputable note scores (type, inbound links, review vetting, recency) filter /connect candidates and truncate budget-bounded listings as the KB grows
- [semantic-review-catches-content-errors-that-structural-validation-cannot](./semantic-review-catches-content-errors-that-structural-validation.md) — four semantic checks (enumeration completeness, grounding alignment, boundary-case coverage, internal consistency) that require LLM adversarial reading
- [link-graph-plus-timestamps-enables-make-like-staleness-detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — existing links encode dependencies; comparing note and target timestamps flags staleness without new annotation
- [stale-indexes-are-worse-than-no-indexes](./stale-indexes-are-worse-than-no-indexes.md) — a missing index entry suppresses search entirely; absence of an index degrades to search, presence of a stale index prevents it
- [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — a copy of mechanically recomputable information must be validator-checked against its source or not exist; hand-maintained-and-trusted is the forbidden middle
- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned.md) — successful runs can still conceal broken helpers and paths; maintenance needs log sweeps or other observability for hidden failures

## Operations

- [maintenance-operations-catalogue-should-stage-stable-procedures](./maintenance-operations-catalogue-should-stage-stable-procedures.md) — staging catalogue for periodic operations before they are turned into reusable procedures
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) — periodic audits belong in externally triggered operations, not always-loaded routing docs
- [gate-learning-from-accepted-edits](../reference/proposals/gate-learning-from-accepted-edits.md) — proposal: turn accepted edit diffs into review-gate candidates with a promotion/rollback lifecycle and budget-bounded loading; the oracle constraint is [an-accepted-edit-verifies-the-change-not-the-rule](./an-accepted-edit-verifies-the-change-not-the-rule.md)

## Related Tags

- [tags](./tags-README.md) — parent area: architecture and design of the KB itself
- [document-system](./document-system-README.md) — type system and validation that maintenance operations check against
- [links](./links-README.md) — linking methodology that staleness detection and quality signals operate on
