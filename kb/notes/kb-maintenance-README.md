---
description: Index of notes about keeping the KB healthy over time — detection of staleness and quality degradation, maintenance operations, and the dynamics that govern system entropy
type: kb/types/tag-readme.md
index_source: tag
index_key: kb-maintenance
---

# KB maintenance

How an agent-operated KB stays healthy as it grows. Detection, operations, and the dynamics that govern quality over time. For how the KB is *built*, see [tags](./tags-README.md). For document structure, see [document-system](./document-system-README.md).

## Dynamics

- [maintenance-capacity-must-match-harmful-artifact-inflow](./maintenance-capacity-must-match-harmful-artifact-inflow.md) — stable quality requires prevention, containment, detection, and repair capacity to keep pace with risk-weighted harmful-artifact inflow; gross generation is only a proxy
- [traversal-improves-the-graph](./traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md) — every traversal is a read-write opportunity; agents should log improvement opportunities during reading, then process them separately to avoid context-switching
- [title-as-claim-exposes-commitments-enabling-popperian-maintenance](./title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — claim titles make maintenance cheap: scan the index, ask "do I still believe this?", open only the doubtful ones

## Detection

- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — composite oracle from graph-topology, content-proxy, and LLM-hybrid signals; the evaluation layer the learning loop needs
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — recomputable note scores (type, inbound links, review vetting, recency) filter /connect candidates and truncate budget-bounded listings as the KB grows
- [semantic-review-catches-content-errors-that-structural-validation-cannot](./semantic-review-catches-content-errors-that-structural-validation.md) — four semantic checks (enumeration completeness, grounding alignment, boundary-case coverage, internal consistency) that require LLM adversarial reading
- [link-graph-plus-timestamps-enables-make-like-staleness-detection](./link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — existing links encode dependencies; comparing note and target timestamps flags staleness without new annotation
- [stale-indexes-reduce-discovery-when-they-suppress-fallback-search](./stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md) — an apparently complete, incomplete index lowers route-specific recall when it suppresses a more complete search
- [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — a copy of mechanically recomputable information must be validator-checked against its source or not exist; hand-maintained-and-trusted is the forbidden middle
- [seven documentation cases left routing and synthesis](./evidence/seven-documentation-cases-left-routing-and-synthesis.md) — a bounded Commonplace sweep where direct source access removed exact-fact prose while checked discovery and cross-component synthesis survived
- [final task success does not establish intended-path health](./final-task-success-does-not-establish-intended-path-health.md) — identical terminal outcomes can conceal broken prescribed paths; maintenance needs independent path events
- [domain-pricing-routes-an-exception-to-idealization-assessment](./domain-pricing-routes-an-exception-to-idealization-assessment.md) — separates truth verdicts from repair dispositions: pricing routes a defeated claim to idealization assessment, and a retained idealization carries an adequacy record later passes can attack

## Operations

- [maintenance-operations-catalogue-should-stage-stable-procedures](./maintenance-operations-catalogue-should-stage-stable-procedures.md) — staging catalogue for periodic operations before they are turned into reusable procedures
- [periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in-routing](./periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) — periodic audits belong in externally triggered operations, not always-loaded routing docs
- [gate-learning-from-accepted-edits](../reference/proposals/gate-learning-from-accepted-edits.md) — proposal: turn accepted edit diffs into review-gate candidates with a promotion/rollback lifecycle and budget-bounded loading; the oracle constraint is [an-accepted-edit-verifies-the-change-not-the-rule](./an-accepted-edit-verifies-the-change-not-the-rule.md)

## Related Tags

- [tags](./tags-README.md) — parent area: architecture and design of the KB itself
- [document-system](./document-system-README.md) — type system and validation that maintenance operations check against
- [links](./links-README.md) — linking methodology that staleness detection and quality signals operate on
