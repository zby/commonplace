---
description: "Superseded decision that placed the required open-vocabulary source genre on snapshots before tracked ingests became the durable source authority"
type: ../types/adr.md
tags: []
status: superseded
---

# 045-Source genre is a single open field on the snapshot

**Status:** superseded by [ADR 072](./072-ingests-own-source-authority-and-snapshots-are-local.md)

**Date:** 2026-07-12

## Context

Source genre was recorded twice with divergent vocabularies: snapshot `tags` carried a mixed content-family list (65 `academic-paper`, plus container values like `x-article` and `web-page` that duplicate `capture` and the source URL), while ingest-reports carried a closed 11-value `source_type` schema enum (62 `scientific-paper` for the same sources the tags called `academic-paper`). A retrieval query on either vocabulary missed roughly half the corpus, and the distinction the Limitations-lens machinery consumes (`practitioner-report` vs `conceptual-essay`) was invisible at the snapshot level.

The closed enum also forced downstream KBs to extend the framework schema by PR — the epistack casework added `court-opinion`, `news-article`, and `official-statement` that way. The proposal "Source genre is one open-vocabulary field on the snapshot" (archived) argued for one open field on the snapshot; [collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) sets the guard: value lists may extend, value meanings stay fixed and type-owned.

## Decision

The snapshot schema requires a `genre` field. Its known values are the former `source_type` vocabulary, expressed as an enum with `severity: warn` (the per-constraint severity machinery of [ADR 024](./024-schema-severity-is-per-constraint-fail-by-default.md)): a missing field fails validation, an off-list value warns. The vocabulary and value meanings live in the snapshot type spec; extension is deliberate and framework-schema-free.

The ingest-report schema drops `source_type` from its required fields and explicitly rejects it (`source_type: false`). The report reads the paired snapshot's `genre` for lens selection and restates it only in Classification prose. If ingestion's closer reading contradicts the capture-time classification, the agent corrects the snapshot's `genre` in place — the snapshot is the single ground truth, and the type spec reframes this one field as capture metadata rather than analysis.

Snapshot `tags` are no longer required and no longer carry the content family; they return to optional topical duty. Existing artifacts were migrated: 131 snapshots gained `genre` (130 from their paired report's value, one from its content-family tag), family tags were stripped, and 134 reports lost `source_type`. The capture skill stamps `genre` at capture; directory ingests, which have no snapshot artifact, state genre in Classification prose only.

## Considered alternatives

*Retrofitted 2026-07-25 under [ADR 056](./056-adopted-and-retired-proposals-archive-out-of-the-frontier.md), absorbing the decision-relevant content of the archived proposal.*

- **Genre as artifact type** (per-genre snapshot types) — rejected: genre does not change the snapshot's structural contract, and the type spec already forbids source-family labels as `type:` values.
- **Moving the closed enum to the snapshot unchanged** — rejected: relocates the extend-by-framework-PR pressure without relieving it. This was the option the proposal warned would merely move the problem, and it is why adoption was tied to an open-vocabulary mechanism rather than to the field's location alone.
- **Keeping a copy of the value on the report** — rejected: an unchecked derived copy of ground truth recorded elsewhere. Checked-or-absent applies and absent is the simpler safe state; the report's Classification prose carries the justification instead. A machine-checked copy for renderers that see only the report file was the alternative under this head, and it buys too little for a second enforcement path.
- **Per-collection reinterpretation of the field's meaning** — rejected: forbidden by the frontmatter-semantics boundary; only the value list is open.
- **Leaving genre on the ingest-report** (the status quo) — rejected: genre is a property of the source, and a classification that exists only once an analysis artifact is written leaves un-ingested snapshots permanently unclassified, which is the wrong shape for genre's use as an evidential-weight proxy.

Deciding forces: one query surface across ~265 artifacts, against the live `academic-paper`/`scientific-paper` split that made either vocabulary miss roughly half the corpus; classification at capture rather than never; and the cost of bending the snapshot type's no-analysis boundary, accepted by reframing one genre judgment as capture metadata and stating that reframe explicitly in the type spec.

Free choices resolved: the field is named `genre`, not `source_type` (the latter collides with the artifact type-system vocabulary); the report keeps no copy; the open-vocabulary mechanism is per-constraint severity (the proposal's direction B) rather than a vocabulary file (direction A), which stays available on top of this floor; family tags were actively stripped during migration rather than merely stopped being required. Left open: whether per-genre Limitations lenses become per-value docs or stay a prose table in the ingest-report type spec.

## Consequences

One query surface for genre across all source artifacts. Downstream KBs extend the vocabulary by committing off-list values (warned, visible) without touching framework schemas; the extensible-controlled-vocabularies workshop still owns the question of whether a structured vocabulary file (its direction A) should later supply documented default-list growth on top of this warn floor, and whether `source-tier` gets the same treatment.

A snapshot is no longer fully immutable after capture: exactly one field, `genre`, may be corrected by ingestion. New genres that recur deserve a dedicated Limitations lens in the ingest-report type spec alongside their vocabulary entry; unknown genres fall back to a generic lens.

The change is breaking: `source_type` in ingest-report frontmatter is rejected rather than aliased.

---

Relevant Notes:

- [Collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — implements: values extend, meanings stay type-owned — the boundary this mechanism respects
- [ADR 024: schema severity is per-constraint, fail by default](./024-schema-severity-is-per-constraint-fail-by-default.md) — implemented-by: the existing machinery that makes the enum warn instead of fail
- [Snapshot type](../../sources/types/snapshot.md) — implemented-by: the field, vocabulary, and correction contract
- [Ingest-report type](../../sources/types/ingest-report.md) — implemented-by: lens selection from the snapshot's genre and the field's removal
