# External-referent grounding cases: docs-on-code and outlines-on-literature

Working file. Two forcing witnesses from the 2026-08-19 product-direction session: leading Commonplace toward being a good llm-wiki for **software documentation** and for **scientific article outlines**. Both segments turned out to be the same generalization — grounding a KB artifact against a referent outside the KB's editable text: source code for documentation, published literature for scientific claims. That is exactly the immutable/external-source carrier gap this workshop already owns ([contradiction 2](./current-contradictions.md), [matrix decision 3](./lineage-profile-matrix.md#decisions-exposed-by-the-matrix)), so the cases enter here as test inputs for decisions 1–3, not as a separate design track.

The direction does not add a new problem to the lineage model. It supplies candidates for the **activation condition** the matrix deferrals name: "a real consumer must need an independent audit query, or a second automatic dependency mechanism must develop churning many-to-many edge state and a repeated selector."

## Case A: documentation grounded on code

Normalized shape: `(doc, depends-on, code-file-or-region@revision)`.

- **Topology and churn.** Many-to-many: one doc cites many code files; one file backs many docs. Code churns far faster than any KB text. This is the strongest current candidate for a second churning mesh under the storage predicate in [many-to-many-edge-state-is-where-files-yield-to-a-database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md).
- **Nearest existing profile row.** External Git-backed review: L1 stable verification handle plus L2 on-demand upstream query. Documentation escalates past that row because its consumer repeatedly asks a swept-selector question — "which docs are stale against the current code?" — rather than an occasional per-artifact check.
- **Ladder assignment is per-edge, not per-class.** A reference doc whose warrant *is* accuracy-to-code carries L3-watched edges. An explanation doc whose claims survive most code churn stays at L1/L2. The graduated ladder in [verification-locus-and-provenance-theory](./verification-locus-and-provenance-theory.md) already supports this; the case confirms the assignment must be made where the edge is authored, not uniformly by collection.
- **Mechanism already sketched.** This is the factored-pair escalation named in the verification-locus gaps section ("radius-1 assay results have unhashed inputs" → factored `(note, cited-target)` pairs), with the cited target outside `kb/`. A doc-vs-code pair reuses the two-input review relation the way ADR 038 put the type spec on the criterion side: the referent supplies one hashed input, and the criterion text ("still accurate to this referent") supplies the other.
- **New sub-questions the case forces.** (a) Input identity for an external referent: `repository@revision + path`, or a content hash of a named region — region-level identity avoids staling every doc on every commit. (b) Where the pinned handle is recorded, since the referent cannot carry a footer (see draft rule below). (c) Whether referent snapshots enter the Commonplace store or stay as pinned handles resolved against the repo.

## Case B: scientific claims grounded on literature

Normalized shape: `(note-or-outline-section, evidenced-by, snapshot@capture)`.

- **Mostly kb-internal, deliberately.** Captured snapshots are immutable files in `kb/sources/`, so the pair itself sits inside the KB and the referent never drifts. Case B therefore exercises the carrier and direction decisions (a note cannot record its dependency via a source-side footer on an immutable snapshot — contradiction 2's live witness, now with a second consumer), not watched external edges.
- **What actually changes is the field, not the referent.** New literature invalidates a related-work claim without touching any existing pair. That is a coverage/completeness question — closer to the tag-README `complete` mark and open-ended assays than to pair staleness — and should be kept out of the carrier decision rather than forced into it.
- **Citation identity gap.** Snapshots currently lack bibliographic identity: citation keys, locators, exportable metadata. Whatever carrier rule decision 3 adopts should leave room for bibliographic fields on the pinned record (derivative-side) or the snapshot's capture metadata, without deciding the bibliography feature here.

## Draft carrier rule for immutable/external sources (input to decision 3)

Placement follows **source mutability plus desired invalidation surface**, not a universal side:

1. **Mutable KB source, edit-time interruption wanted** → source-side `... into:` footer (the current default survives, scoped to where it works).
2. **Immutable or externally owned source** (captured snapshot, external repository, published paper) → the normalized tuple `(derivative, relation, source@pinned-handle)` is recorded **derivative-side**, as a frontmatter field or footer link carrying the pinned version handle.
3. **Watched escalation** for either placement lives in the operational store as a factored pair keyed on `(derivative, referent@handle)` — never as text in either file.

Consequences worth stating when this is extracted:

- Articles' derivative-side `source_notes` becomes an instance of rule 2's *pattern* rather than an exception — though its sources are mutable notes, the frozen-publication lifecycle removes the edit-interruption rationale for source-side placement, which is the same reason immutability removes it. Contradiction 1 then resolves by making placement contract-selected under a declared default, and contradiction 5's fix is the write path asking the contract which rule applies.
- Rule 2 is what both new segments need on day one; rule 3 is the escalation only case A currently threatens to earn.

## What this direction does not activate yet

- The generic lineage SQLite schema and shared event ledger stay deferred; case A is a *candidate* second mesh, and activation still requires a real consuming project (a repo actually documenting itself through Commonplace), not the direction statement alone.
- No external-referent pair implementation before the design proposal; per YAGNI the gap becomes a proposal in `kb/reference/proposals/` first.
- Bibliographic export and profile work for the segments (scholarly, pedagogical) are downstream and outside this workshop.

## Proposed extraction path

1. Resolve matrix decisions 1–3 with these two cases plus the existing article/snapshot witnesses; extract as an ADR plus edits to `kb/reference/link-vocabulary.md` and the affected `COLLECTION.md`/skill surfaces.
2. Write the external-referent review-pair design proposal in `kb/reference/proposals/`: referent identity (revision pin vs region hash), pinned-handle carrier per the rule above, staleness semantics on referent change, storage weight per the ladder rung.
3. Segment-specific work (scholarly profile from the ASIS&S paper case, pedagogical profile, bibliographic types) proceeds in its own workshops once 1–2 land.

---

Relevant Notes:

- [lineage-profile-matrix](./lineage-profile-matrix.md) — tests: these cases are decision inputs for its decisions 1–3 and its deferral activation conditions
- [current-contradictions](./current-contradictions.md) — is-evidence-for: contradiction 2 gains two consumer cases; contradiction 1's resolution shape is sketched above
- [verification-locus-and-provenance-theory](./verification-locus-and-provenance-theory.md) — rests-on: the ladder and the factored-pair escalation these cases instantiate
- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — rests-on: the storage predicate case A is measured against
- [README-REVIEW-SYSTEM](../../reference/README-REVIEW-SYSTEM.md) — draws-on: the two-input review relation the external-referent pair would generalize
- [articles COLLECTION](../../articles/COLLECTION.md) — is-evidence-for: the existing derivative-side lineage carrier the draft rule generalizes
