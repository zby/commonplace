---
description: "Proposal: close the remaining conformance-lens asymmetries — optional watches: on conformance gate documents and a shared conformance-lens code abstraction; typed COLLECTION.md contracts adopted (ADR 042)"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, document-system]
status: seedling
---

# Making the conformance lenses symmetric

Commonplace now enforces two authored contracts against every note by the same factored-pair mechanism: the type spec ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) and the collection's `COLLECTION.md` ([ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)). The two are meant to be interchangeable so that a clause lives where its scope says it belongs — kind-bound in the type spec, location-bound in `COLLECTION.md` — rather than migrating to whichever surface has teeth. But the two lenses are only symmetric at the freshness layer. This proposal originally mapped three asymmetries above it; the first — the gate documents' unequal artifact status — was adopted as [ADR 042](../adr/042-collection-contracts-are-typed-artifacts.md) (typed `COLLECTION.md` contracts), and this proposal now holds the two that remain. It decides nothing, and symmetry is a goal to weigh against ADR 041's deliberate simplicity choices, not an axiom.

## Current state (as of 2026-07-08)

The two conformance lenses share the freshness/acceptance/ack stack unchanged from catalog gates. Axis A (typed `COLLECTION.md` contracts) is adopted: [ADR 042](../adr/042-collection-contracts-are-typed-artifacts.md) shipped `kb/types/collection.md` + schema, frontmatter on every contract and scaffold template, contract validation in collection scope, and an explicit (formerly implicit) exclusion of contracts from note sweeps — with explicit path selection deriving the contract's own type-conformance pair. Two asymmetries remain:

- **The auto-ack path.** `ack_trivial_note_changes.py` treats a gate with no valid `watches:` list as watching the whole note, so no note edit is ever trivial against it. Both conformance lenses land here by omission of the field: both gate documents now carry frontmatter, but neither declares `watches:`. A frontmatter-only note edit therefore cannot be auto-acked against either contract even when the contract plainly governs only body prose. `KNOWN_WATCHES = {"body", "title", "description"}`.
- **The code.** `review/type_conformance.py` and `review/collection_conformance.py` are structurally parallel — each exports `is_*_gate_request`, `is_*_gate_path`, `*_gate_id_for_path`, `resolve_*_gate_id`, and a `note_*_path` deriver — differing only in the lens name, the gate-path predicate, and whether the pair derives from note frontmatter (`type:`) or note location (nearest `COLLECTION.md`). `resolve_gates.py` hardcodes both lenses by name in `resolve_gate_requests` and `all_gate_requests`. Source-as-gate, the next factored pair named in [factored dependency pairs](./factored-dependency-pairs-for-review-freshness.md), would be a third near-copy of the same shape.

The freshness layer below is already symmetric: the snapshot table is role-neutral ([ADR 032](../adr/032-review-freshness-uses-db-snapshots-not-git.md)), a contract edit flips `gate-changed` for its cohort, and a mechanical wrapper renders either contract as a gate by reference. Nothing below pair derivation needs to change for any option here.

## The two remaining axes

### B. Optional `watches:` on conformance gate documents

Let a conformance gate document declare `watches:` (reusing the existing `{body, title, description}` vocabulary) and have `ack_trivial_note_changes.py` honor it for conformance pairs exactly as it does for catalog gates. A collection contract that governs only body prose could declare `watches: [body]`, making a pure-frontmatter note edit auto-ackable against it; a type spec whose authoring instructions never touch the description could do likewise.

- **B1 — honor `watches:` on conformance gates.** The ack loader already reads `watches:` from the gate path; it would simply find a value where today it finds none. Since ADR 042 both gate documents carry frontmatter, so the field has a home in each and the lenses can adopt it symmetrically — nothing beyond the declaration and the ack-side rule change is needed.
- **B2 — always-whole-note (status quo).** Conformance pairs never auto-ack. Safe by construction, at the cost of N per-note manual acks after any contract-irrelevant note edit.
- **B3 — conformance-specific coarse rule.** A blanket "frontmatter-only edits are trivial against any conformance gate" rule, no per-contract declaration. Cheapest, but wrong for a contract whose clauses *do* bind frontmatter (a description-convention clause), so it trades correctness for uniformity — the reason `watches:` is author-declared per gate in the first place.

*Forces.* `watches:` encodes which note edits leave a verdict valid — the criteria-vs-process distinction ([criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md)). A conformance gate is criteria over a known slice of the note, so declaring that slice is well-typed. The risk is that an author under-declares `watches:` and silently narrows what the contract polices; the current whole-note default is the conservative failure mode, and any move off it is a claim that the contract's scope is genuinely narrower.

### C. A shared conformance-lens abstraction in code

Collapse `type_conformance.py`, `collection_conformance.py`, and the pending source lens into one `ConformanceLens` abstraction — a record parameterizing the four varying pieces (lens name; gate-path predicate; gate-id ↔ path derivation; note → gate-path deriver, keyed on frontmatter *or* location) — with `resolve_gates.py` iterating a registry instead of naming lenses.

- **C1 — registry abstraction now.** One module, one list of lenses; adding source-as-gate is a registration, not a fourth near-duplicate file. Risk: with only two instances the abstraction is fitted to a sample of two and may misparameterize the frontmatter-vs-location split (the one axis where the two genuinely differ).
- **C2 — keep per-lens modules (status quo).** Explicit, greppable, each lens self-contained. Cost: `resolve_gate_requests`, `all_gate_requests`, and `paths.py` grow an `or is_*_gate_request(...)` clause per lens, and the shared shape is enforced only by convention.
- **C3 — extract the shared shape only when the third lens lands.** Write source-as-gate as C2's third copy, then factor all three — the boundary is stated by three worked instances rather than guessed from two.

*Forces.* This is a rule-of-three call: [abstract an experience only when you can state the boundary](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) and the repo's YAGNI rule both argue that the abstraction earns its keep at the third instance, not the second — and source-as-gate is that third instance, already named and motivated. Two instances that differ in exactly one structural dimension (derivation basis) are the minimum from which that dimension can be parameterized correctly, but also the maximum at which keeping them separate stays cheap.

## Cross-cutting dependencies

- **B and C are independent of each other**, but C's payoff scales with B: more per-lens metadata handling (watches, `## Review` detection, future profile fields) is more surface to either duplicate across modules or centralize once.

## Free choices

- **`watches:` vocabulary for conformance gates.** Reuse `{body, title, description}` unchanged, or add a conformance-specific token (e.g. `placement`) for clauses about where a note sits — which is not a note-part at all and may not fit the watches model.
- **Registry shape for C.** A dataclass list, a protocol with per-lens classes, or a dict keyed by lens name; the frontmatter-vs-location deriver is the field that must stay first-class whichever is chosen.

## Forces keeping this at planning

- **No demand signal.** No contract edit has yet produced enough contract-irrelevant note-ack churn to make B worth its correctness risk, and the two-module duplication in C is small and static.
- **ADR 041 chose the simple side on purpose.** Axis B reopens its always-whole-note auto-ack rule, a decision that was made deliberately; the proposal should not be adopted as a bundle just because the pieces are adjacent.
- **Symmetry is instrumental, not terminal.** The point of parity is letting clause placement follow scope; an asymmetry that never distorts placement is not worth machinery to erase.

## Adoption criteria

- Adopt **B** when the first real contract edit forces more than a handful of per-note acks whose note diffs never touched the slice the contract governs. This is the same demand signal the [cohort-scoped ack](./factored-dependency-pairs-for-review-freshness.md) waits on, approached from the note-edit side. ADR 042's migration itself is one data point: adding frontmatter staled every collection's cohort at once.
- Adopt **C** when source-as-gate is built — write it as the third instance, then factor, so the abstraction is drawn from three worked lenses rather than fitted to two.

---

Relevant Notes:

- [038-type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — part-of: the type lens this proposal would bring the collection lens level with
- [041-collection-conformance reviews use COLLECTION.md as the gate](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — part-of: the collection lens whose deferred symmetry choices this proposal maps
- [042-collection contracts are typed artifacts](../adr/042-collection-contracts-are-typed-artifacts.md) — part-of: the adopted first axis; its migration is the demand-signal data point axis B's criterion cites
- [factored dependency pairs for review freshness](./factored-dependency-pairs-for-review-freshness.md) — part-of: source-as-gate is the third lens that motivates axis C; cohort-scoped ack is the gate-side twin of axis B
- [open-ended collection text contracts](./open-ended-collection-text-contracts.md) — see-also: the typed COLLECTION.md frontmatter shipped by ADR 042 is where its per-collection profile declaration would live
- [review architecture](../review-architecture.md) — part-of: the code carrying the two conformance gate sources axis C would unify
- [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — rationale: why a conformance gate's watches: slice is a well-typed triviality declaration
- [abstract an experience only when you can state the boundary](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — rationale: the rule-of-three timing for the code abstraction
- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the build-product/prerequisite model both lenses realize and any new lens inherits
