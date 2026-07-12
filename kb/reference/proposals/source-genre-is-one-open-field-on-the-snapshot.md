---
description: "Proposal: record source genre once as an open-vocabulary source_type field on the snapshot, drop the ingest-report enum and genre-carrying tags, and unify two divergent vocabularies"
type: kb/types/note.md
traits: [design-proposal]
tags: [document-system]
---

# Source genre is one open-vocabulary field on the snapshot

Source genre — is this a scientific paper, a practitioner report, a court opinion — is currently recorded twice in `kb/sources/`, in two vocabularies that neither agree nor defer to each other, and neither is authoritative. Snapshot `tags` carry a mixed genre/platform label; the ingest-report carries a closed `source_type` enum. The same genre appears under different names on the two sides (`academic-paper` on snapshots, `scientific-paper` in reports), so a retrieval query keyed to either vocabulary misses roughly half the corpus, and the one distinction the ingest lens machinery actually consumes — practitioner-report versus conceptual-essay — is invisible at the snapshot level, where both collapse to `blog-post` or `x-article`.

This proposal collapses the two into a single open-vocabulary genre field that lives on the snapshot, where the source artifact itself is the ground truth. It stays inside the boundary that [collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md): the field's meaning is fixed and type-owned ("genre of the captured source"), and only its value list extends — the sanctioned value-set-extension operation, not meaning relativization.

## Current state (as of 2026-07-12)

**Two vocabularies, measured.**

- Snapshot `tags` — `snapshot.md` instructs "put the content family in `tags`". Across ~131 snapshots: academic-paper 65, x-article 26, blog-post 17, x-post 5, web-page 4, x-thread 3, news-article 3, github-repo 3, documentation 3, encyclopedia-article 1, plus one stray topical tag. This is a mixed axis: a few values name genre, most name the container or platform (x-article, web-page, github-repo) — an axis already carried by the snapshot's `capture` field and the source URL.
- Ingest-report `source_type` — a closed 11-value enum in `kb/sources/types/ingest-report.schema.yaml`. Across ~134 reports: scientific-paper 62, conceptual-essay 28, practitioner-report 27, tool-announcement 7, design-proposal 4, conversation-thread 4, code-repository 2. The last three enum values (court-opinion, news-article, official-statement) were added under epistack casework pressure — by PR against the framework schema, which is the pressure this proposal relieves.

**The concrete breakage.** `academic-paper` (snapshot tags) and `scientific-paper` (report enum) name the same genre; a query on either misses the other's ~half of the corpus. And genre lives on the ingest-report — an analysis artifact that exists only once someone writes it — so an un-ingested snapshot is never classified at all.

**Adjacent facts.** [ADR 044](../adr/044-user-verification-replaces-global-note-status.md) recently resolved the sibling problem of a fused global `status` field by deleting it rather than making its meaning collection-relative — the same shape of fix this proposal applies to genre. The extensible-controlled-vocabularies workshop is open, designing the open-list mechanism for exactly this `source_type` field, with two directions (A and B, below) still unevaluated.

## The design

1. **One field, on the snapshot.** A single genre field (working name `source_type`) moves to the snapshot schema. Genre is a property of the source, and the snapshot is the source artifact, so the snapshot is the ground truth. It is set at capture time by the capturing agent — a surface judgment — and ingestion may correct the snapshot's field if deeper reading disagrees, so the correction lands in the one authoritative place.
2. **The ingest-report drops its `source_type` field.** The report's Classification section keeps its prose justification, and the Limitations Standards lens is selected by reading the paired snapshot's field — the ingest process opens the snapshot anyway. No duplicated field means no unchecked derived copy, per [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md).
3. **Snapshot `tags` stop carrying genre.** Container/platform information (x-article, web-page, github-repo) is redundant with `capture` plus the URL plus platform metadata; `tags` return to topical duty or may be empty.
4. **The vocabulary is open-ended with fixed per-value meaning.** Different installed KBs and caseworks need different genre lists — the epistack casework added court-opinion, news-article, and official-statement by PR against the framework schema. The field's meaning stays fixed and type-owned; only the value list extends. The concrete open-list mechanism is what the extensible-controlled-vocabularies workshop is designing: direction A (a vocabulary file under `kb/`, with the schema generated or looked up from it) or direction B (per-constraint severity: warn on out-of-list values, available today via the ADR 024 machinery with zero new code). B can be the enforcement floor while A supplies the documented default list.

## Forces

**For:**

- **One vocabulary, one query.** Retrieval unifies across ~265 artifacts; the live academic-paper/scientific-paper split is direct evidence of the cost of not doing this.
- **No derived-copy risk.** Removing the report's copy eliminates the checked-or-absent hazard between snapshot and report — absent is the simpler safe state.
- **Right shape for the evidential-weight use.** The epistack direction treats genre as an evidential-weight proxy for a source; a classification that only exists once an analysis artifact is written is the wrong shape for that.
- **Classified at capture, not never.** Un-ingested snapshots become classified when captured rather than remaining unclassified until (or unless) someone ingests them.

**Against:**

- **It bends the snapshot type's "no analysis" boundary.** `snapshot.md` says capture metadata only, no analysis. The reframe — one genre judgment is capture metadata, not analysis — must be stated explicitly in `snapshot.md`, or it will read as contract drift. (The separate rule "do not use source-family labels as `type:` values" is untouched: this is a field, not a type.)
- **Capture-time classification is shallower** than ingestion-time classification, and the correction flow mutates a snapshot after capture, which the current stamped-at-capture reading of snapshots does not anticipate.
- **Migration is wide though mechanical.** It touches ~131 snapshots (add field, clean genre tags), ~134 reports (drop field), two schemas, two type specs, and the lens-selection instruction in `ingest-report.md`. No backwards compatibility is needed per repo policy.
- **Lens selection now needs a join.** Selecting the Limitations Standards lens at report-authoring time requires reading the snapshot's field — a join, though one the authoring flow already performs when it opens the snapshot.

## Free choices

- **Field name.** Keep `source_type` (continuity with existing reports) or rename to `genre` (sharper — "type" collides with the artifact type-system vocabulary).
- **Copy for file-only renderers.** Whether the report carries a machine-checked copy of the snapshot's value for renderers that see only the report file, or no copy at all. Checked-or-absent applies; absent is simpler.
- **Open-vocabulary mechanism.** A vs B vs B-then-A — owned by the extensible-controlled-vocabularies workshop, not this proposal.
- **Tag cleanup aggressiveness.** Whether platform/container tags are actively removed during migration or merely stop being required.
- **Lens home.** Whether the per-genre Limitations Standards lenses become per-value docs (the ADR-018-shaped move: each genre value is a small doc carrying its lens paragraph, so adding a genre and its guidance is one act) or stay a prose table in `ingest-report.md` with a generic default lens for unknown values.

## Adoption criteria

Adopt together with the extensible-controlled-vocabularies workshop's mechanism choice — moving the field while leaving the enum closed would merely relocate the pressure. If the workshop picks direction B alone, this proposal is implementable immediately: schema move, severity annotation, migration. When adopted, the choice becomes an ADR and this proposal is superseded by it.

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the single-ground-truth rule behind dropping the report's copy of genre
- [The collection–type split is asymmetric: collections never own frontmatter semantics](../collections-never-own-frontmatter-semantics.md) — part-of: the boundary this proposal stays inside — genre's value set extends while its meaning stays type-owned
- [ADR 044: user verification replaces global note status](../adr/044-user-verification-replaces-global-note-status.md) — see-also: the sibling resolution of an adjacent fused-field problem, fixed by deleting the field rather than relativizing it
- [ADR 024: schema severity is per-constraint, fail by default](../adr/024-schema-severity-is-per-constraint-fail-by-default.md) — see-also: the existing per-constraint severity machinery that makes open-vocabulary mechanism B available with no new code
- [ADR 018: types are path references to instruction docs](../adr/018-types-are-path-references-to-instruction-docs.md) — see-also: the precedent for a per-value doc carrying a prose payload, if the Limitations lenses become per-genre docs
- [Snapshot type spec](../../sources/types/snapshot.md) — see-also: the type that gains the genre field and whose "no analysis" boundary must be reframed
- [Ingest-report type spec](../../sources/types/ingest-report.md) — see-also: the type that drops the `source_type` field and reads it from the paired snapshot for lens selection
