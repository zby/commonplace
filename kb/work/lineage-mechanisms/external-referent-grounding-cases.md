# External-referent grounding cases: docs-on-code and outlines-on-literature

Working file. Two forcing witnesses from the 2026-08-19 product-direction session: leading Commonplace toward being a good llm-wiki for **software documentation** and for **scientific article outlines**. Both segments turned out to be the same generalization — grounding a KB artifact against a referent outside the KB's editable text: source code for documentation, published literature for scientific claims. That is exactly the immutable/external-source carrier gap this workshop already owns ([contradiction 2](./current-contradictions.md), [matrix decision 3](./lineage-profile-matrix.md#decisions-exposed-by-the-matrix)), so the cases enter here as test inputs for decisions 1–3, not as a separate design track.

The direction does not add a new problem to the lineage model. It supplies candidates for the **activation condition** the matrix deferrals name: "a real consumer must need an independent audit query, or a second automatic dependency mechanism must develop churning many-to-many edge state and a repeated selector."

## Case A: documentation grounded on code

Normalized shape: `(doc, depends-on, code-file-or-region@revision)`.

- **Hypothesized topology and churn.** If retained documents each make exact claims about several code regions, the relation is many-to-many and code changes faster than KB text. That topology made this the strongest candidate for a second churning mesh under the storage predicate in [many-to-many-edge-state-is-where-files-yield-to-a-database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md). The disposition result below shows that topology cannot be assumed from the product direction alone.
- **Nearest existing profile row if exact docs survive.** External Git-backed review: L1 stable verification handle plus L2 on-demand upstream query. Documentation escalates past that row only if its consumer repeatedly asks a swept-selector question — "which retained exact docs are stale against the current code?" — rather than reading the implementation live or checking one artifact on demand.
- **Ladder assignment is per-edge, not per-class.** A reference doc whose warrant *is* accuracy-to-code carries L3-watched edges. An explanation doc whose claims survive most code churn stays at L1/L2. The graduated ladder in [verification-locus-and-provenance-theory](./verification-locus-and-provenance-theory.md) already supports this; the case confirms the assignment must be made where the edge is authored, not uniformly by collection.
- **Mechanism available but not earned.** The verification-locus gaps section sketches a factored `(note, cited-target)` pair for radius-1 assay results with unhashed inputs. A doc-vs-code pair could reuse the two-input review relation the way ADR 038 put the type spec on the criterion side: the referent supplies one hashed input, and the criterion text ("still accurate to this referent") supplies the other. No current consumer requires that escalation.
- **New sub-questions the case forces.** (a) Input identity for an external referent: `repository@revision + path`, or a content hash of a named region — region-level identity avoids staling every doc on every commit. (b) Where the pinned handle is recorded, since the referent cannot carry a footer (see draft rule below). (c) Whether referent snapshots enter the Commonplace store or stay as pinned handles resolved against the repo.

### Observed disposition result (2026-08-24)

[Seven Commonplace documentation cases](../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md)
tested the hypothesized mesh after agents gained a guaranteed route to the
executing source. Two reference artifacts were retired and five were reduced.
Exact fields, arguments, schemas, module inventories, and local behavior moved
to source or command help. The surviving documents carry command discovery,
approximate topology, authority and lifecycle maps, and cross-component
transition or concurrency boundaries. None now declares a complete set of
code-file or region dependencies whose every change implies staleness.

Before the sweep, the seven pages lagged their code by only 0–3 commits, so
co-maintenance was occurring. The audit still found an incorrect claim,
incomplete inventory, or broken live-read prerequisite in every case. The
effective repair was to remove the exact-copy obligation rather than register
granular freshness edges. No recurring "which docs are stale against code?"
consumer was observed after that reduction.

This disconfirms Case A as a current activation witness; it does not make the
normalized dependency impossible. A consuming project may deliberately retain
an exact code summary after showing that it substitutes for source work. That
project must then demonstrate the retained edges, their churn, and a repeated
selector before L3 factored pairs or a generic edge store are warranted. Until
then, any external code dependency that remains uses the L1/L2 carrier rule
below, and exact implementation questions read the pinned source live.

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

- The generic lineage SQLite schema and shared event ledger stay deferred. The Commonplace audit failed to produce a second mesh; activation requires a real consuming project that retains exact code-dependent documentation for demonstrated read-path value and repeatedly selects those edges for refresh.
- The external-referent review-pair proposal is deferred with its implementation. The derivative-side carrier decision can land without speculating about region identity, snapshot storage, or watched-pair transitions before a consumer earns them.
- Bibliographic export and profile work for the segments (scholarly, pedagogical) are downstream and outside this workshop.

## Proposed extraction path

1. Resolve matrix decisions 1–3 with these two cases plus the existing article/snapshot witnesses; extract the normalized direction and contract-selected carrier rule as an ADR plus edits to `kb/reference/link-vocabulary.md` and the affected `COLLECTION.md`/skill surfaces.
2. Do not write the external-referent review-pair proposal until a real consumer demonstrates the watched-edge requirement. At activation, the proposal must decide referent identity (revision pin vs region hash), staleness semantics on referent change, and storage weight per the observed selector.
3. Segment-specific work (scholarly profile from the ASIS&S paper case, pedagogical profile, bibliographic types) proceeds in its own workshops once 1–2 land.

---

Relevant Notes:

- [lineage-profile-matrix](./lineage-profile-matrix.md) — tests: these cases are decision inputs for its decisions 1–3 and its deferral activation conditions
- [current-contradictions](./current-contradictions.md) — is-evidence-for: contradiction 2 gains two consumer cases; contradiction 1's resolution shape is sketched above
- [verification-locus-and-provenance-theory](./verification-locus-and-provenance-theory.md) — rests-on: the ladder and the factored-pair escalation these cases instantiate
- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — rests-on: the storage predicate case A is measured against
- [README-REVIEW-SYSTEM](../../reference/README-REVIEW-SYSTEM.md) — draws-on: the two-input review relation the external-referent pair would generalize
- [articles COLLECTION](../../articles/COLLECTION.md) — is-evidence-for: the existing derivative-side lineage carrier the draft rule generalizes
- [Seven documentation cases left routing and synthesis](../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md) — tests: disconfirms docs-on-code as a current churning-mesh witness while preserving the conditional external-carrier case
