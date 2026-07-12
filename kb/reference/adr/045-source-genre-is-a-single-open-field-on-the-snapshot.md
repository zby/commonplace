---
description: "Source genre becomes one required open-vocabulary `genre` field on the snapshot; the ingest-report drops and rejects `source_type`, and snapshot tags return to optional topical duty"
type: ../types/adr.md
tags: []
status: accepted
---

# 045-Source genre is a single open field on the snapshot

**Status:** accepted  
**Date:** 2026-07-12

## Context

Source genre was recorded twice with divergent vocabularies: snapshot `tags` carried a mixed content-family list (65 `academic-paper`, plus container values like `x-article` and `web-page` that duplicate `capture` and the source URL), while ingest-reports carried a closed 11-value `source_type` schema enum (62 `scientific-paper` for the same sources the tags called `academic-paper`). A retrieval query on either vocabulary missed roughly half the corpus, and the distinction the Limitations-lens machinery consumes (`practitioner-report` vs `conceptual-essay`) was invisible at the snapshot level.

The closed enum also forced downstream KBs to extend the framework schema by PR — the epistack casework added `court-opinion`, `news-article`, and `official-statement` that way. The [source-genre proposal](../proposals/source-genre-is-one-open-field-on-the-snapshot.md) argued for one open field on the snapshot; [collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) sets the guard: value lists may extend, value meanings stay fixed and type-owned.

## Decision

The snapshot schema requires a `genre` field. Its known values are the former `source_type` vocabulary, expressed as an enum with `severity: warn` (the per-constraint severity machinery of [ADR 024](./024-schema-severity-is-per-constraint-fail-by-default.md)): a missing field fails validation, an off-list value warns. The vocabulary and value meanings live in the snapshot type spec; extension is deliberate and framework-schema-free.

The ingest-report schema drops `source_type` from its required fields and explicitly rejects it (`source_type: false`). The report reads the paired snapshot's `genre` for lens selection and restates it only in Classification prose. If ingestion's closer reading contradicts the capture-time classification, the agent corrects the snapshot's `genre` in place — the snapshot is the single ground truth, and the type spec reframes this one field as capture metadata rather than analysis.

Snapshot `tags` are no longer required and no longer carry the content family; they return to optional topical duty. Existing artifacts were migrated: 131 snapshots gained `genre` (130 from their paired report's value, one from its content-family tag), family tags were stripped, and 134 reports lost `source_type`. The capture skill stamps `genre` at capture; directory ingests, which have no snapshot artifact, state genre in Classification prose only.

Rejected alternatives:

- Genre as artifact type (per-genre snapshot types) — genre does not change the snapshot's structural contract, and the type spec already forbids source-family labels as `type:` values.
- Moving the closed enum to the snapshot unchanged — relocates the extend-by-framework-PR pressure without relieving it.
- Keeping a copy of the value on the report — an unchecked derived copy of ground truth recorded elsewhere.
- Per-collection reinterpretation of the field's meaning — forbidden by the frontmatter-semantics boundary; only the value list is open.

## Consequences

One query surface for genre across all source artifacts. Downstream KBs extend the vocabulary by committing off-list values (warned, visible) without touching framework schemas; the extensible-controlled-vocabularies workshop still owns the question of whether a structured vocabulary file (its direction A) should later supply documented default-list growth on top of this warn floor, and whether `source-tier` gets the same treatment.

A snapshot is no longer fully immutable after capture: exactly one field, `genre`, may be corrected by ingestion. New genres that recur deserve a dedicated Limitations lens in the ingest-report type spec alongside their vocabulary entry; unknown genres fall back to a generic lens.

The change is breaking: `source_type` in ingest-report frontmatter is rejected rather than aliased.

---

Relevant Notes:

- [Source genre is one open field on the snapshot](../proposals/source-genre-is-one-open-field-on-the-snapshot.md) — supersedes: the proposal this decision adopts
- [Collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — rationale: values extend, meanings stay type-owned — the boundary this mechanism respects
- [ADR 024: schema severity is per-constraint, fail by default](./024-schema-severity-is-per-constraint-fail-by-default.md) — implemented-by: the existing machinery that makes the enum warn instead of fail
- [Snapshot type](../../sources/types/snapshot.md) — implemented-by: the field, vocabulary, and correction contract
- [Ingest-report type](../../sources/types/ingest-report.md) — implemented-by: lens selection from the snapshot's genre and the field's removal
