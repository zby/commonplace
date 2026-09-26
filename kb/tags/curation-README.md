---
description: "Curated head for the curation tag — keeping indexes, tag heads, and the note set usable as the KB grows: index recall, quality scores, staleness signals, retirement, and hygiene operations"
type: types/tag-readme.md
complete: true
---

# curation

How the KB's indexes, tag heads, and body of notes stay usable as it grows: what a complete index can and cannot do, how to rank and prune notes, how to spot stale ones, and how periodic hygiene gets triggered. On the index side, the establishing notes are [an enforced tag-README combines a MOC pattern with checked membership](../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) and [indexes lower recall when they suppress retrieval that would find more](../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md). The audit procedure is [maintain curated indexes](../instructions/maintain-curated-indexes.md). Whether an individual note's content is correct belongs to [review-system](./review-system-README.md) and [claims-and-grounding](./claims-and-grounding-README.md); curation is about the collection and its navigation. A child of [kb-maintenance](./kb-maintenance-README.md).

## Indexes and tag heads

- [An enforced tag-README combines a MOC pattern with checked membership](../notes/an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) — a tag head keeps the map-of-content pattern while validation checks only declared membership
- [Indexes lower recall when they suppress retrieval that would find more](../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — why a completeness claim must be enforced or omitted
- [Index completeness does not determine editorial orientation](../notes/index-completeness-does-not-determine-editorial-orientation.md) — a complete listing gives membership, not grouping, role phrases, or reading order
- [Keyword tags without heads](../reference/proposals/keyword-tags-without-heads.md) — proposal for a weaker search-only tag with no head; set aside by ADR 089 until a need shows
- [Tag maintenance and derived browsing](../reference/proposals/tag-maintenance-and-derived-browsing.md) — proposal to test temporary topic groupings and reviewed tag suggestions before changing the canonical tag structure

## Ranking and staleness signals

- [Quality signals for KB evaluation](../notes/quality-signals-for-kb-evaluation.md) — graph-topology, content-proxy, and LLM-hybrid signals combined into a weak composite oracle
- [Notes need quality scores to scale curation](../notes/notes-need-quality-scores-to-scale-curation.md) — recomputable scores rank candidates once connect retrieves too many
- [Link graph plus timestamps enables make-like staleness detection](../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — existing links plus timestamps flag possibly stale notes without new annotation

## Growth and retirement

- [Maintenance capacity must match harmful-artifact inflow](../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) — quality holds only while prevention, detection, and repair keep pace with risk-weighted inflow
- [Cheap adoption and weak retirement accumulate cost](../notes/cheap-adoption-and-weak-retirement-accumulate-cost.md) — cheap structural additions become debt when retiring them lacks an equally operative path

## Hygiene operations

- [Maintenance operations catalogue should stage stable procedures for instructions](../notes/maintenance-operations-catalogue-should-stage-stable-procedures.md) — the staging catalogue of periodic operations before they become instructions
- [Periodic KB hygiene should be externally triggered, not embedded in routing](../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) — audits run on an external trigger, not from always-loaded routing docs
- [Traversal improvements should be deferred via logging to avoid mid-task context switching](../notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md) — log an improvement noticed while reading and fix it in a separate pass
- [Periodic connect-report mining](../reference/proposals/periodic-connect-report-mining.md) — proposal to mine connect reports on a schedule, automating the triage step from noticed connection to candidate

## Related Tags

- [kb-maintenance](./kb-maintenance-README.md) — the parent: curation is the collection-level half of keeping the KB healthy
- [review-system](./review-system-README.md) — sibling: LLM review of individual notes
- [claims-and-grounding](./claims-and-grounding-README.md) — sibling: whether a note's claims hold and are supported
- [document-system](./document-system-README.md) — the tag-README type and validation that enforce the completeness mark
- [observability](./observability-README.md) — shares the staleness and quality-signal notes
- [links](./links-README.md) — the link graph that staleness detection and quality signals read
