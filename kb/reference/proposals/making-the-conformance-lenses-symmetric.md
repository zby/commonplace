---
description: "Proposal: make the type- and collection-conformance lenses symmetric via typed COLLECTION.md frontmatter, optional watches: on conformance gates, and a shared conformance-lens code abstraction"
type: kb/types/note.md
traits: [design-proposal]
tags: [kb-maintenance, document-system]
status: seedling
---

# Making the conformance lenses symmetric

Commonplace now enforces two authored contracts against every note by the same factored-pair mechanism: the type spec ([ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)) and the collection's `COLLECTION.md` ([ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)). The two are meant to be interchangeable so that a clause lives where its scope says it belongs — kind-bound in the type spec, location-bound in `COLLECTION.md` — rather than migrating to whichever surface has teeth. But the two lenses are only symmetric at the freshness layer. Three concrete asymmetries remain, each a place where the collection lens is the poorer cousin. This proposal maps the option space for closing them; it decides nothing, and symmetry is a goal to weigh against ADR 041's deliberate simplicity choices, not an axiom.

## Current state (as of 2026-07-08)

The two conformance lenses share the freshness/acceptance/ack stack unchanged from catalog gates, but diverge above it:

- **The gate document's own status.** A type spec is itself a typed artifact: `type: kb/types/type-spec.md`, a `schema:` field, `name`/`description` frontmatter, deterministically validated by `commonplace-validate`. A `COLLECTION.md` carries *no frontmatter at all* — it is untyped prose, unvalidated in shape, positional-only. ADR 041 accepted this explicitly: "`COLLECTION.md` files carry no frontmatter, so unlike catalog gates they cannot declare `watches:` or gate metadata; all filtering is positional." No `kb/types/collection.md` type spec exists.
- **The auto-ack path.** `ack_trivial_note_changes.py` treats a gate with no valid `watches:` list as watching the whole note, so no note edit is ever trivial against it. Both conformance lenses land here by omission — the safety is *the absence of frontmatter* (COLLECTION.md) or an unread frontmatter field (type spec). A frontmatter-only note edit therefore cannot be auto-acked against either contract even when the contract plainly governs only body prose. `KNOWN_WATCHES = {"body", "title", "description"}`.
- **The code.** `review/type_conformance.py` and `review/collection_conformance.py` are structurally parallel — each exports `is_*_gate_request`, `is_*_gate_path`, `*_gate_id_for_path`, `resolve_*_gate_id`, and a `note_*_path` deriver — differing only in the lens name, the gate-path predicate, and whether the pair derives from note frontmatter (`type:`) or note location (nearest `COLLECTION.md`). `resolve_gates.py` hardcodes both lenses by name in `resolve_gate_requests` and `all_gate_requests`. Source-as-gate, the next factored pair named in [factored dependency pairs](./factored-dependency-pairs-for-review-freshness.md), would be a third near-copy of the same shape.

The freshness layer below is already symmetric: the snapshot table is role-neutral ([ADR 032](../adr/032-review-freshness-uses-db-snapshots-not-git.md)), a contract edit flips `gate-changed` for its cohort, and a mechanical wrapper renders either contract as a gate by reference. Nothing below pair derivation needs to change for any option here.

## The three axes

### A. Typed `COLLECTION.md` contracts

Give `COLLECTION.md` frontmatter and a `type: kb/types/collection.md` binding with a schema, reaching the parity a type spec already has: a validated shape, and a place to declare metadata. Candidate fields: `register`/`profile` (already headlined in prose — see [open-ended collection text contracts](./open-ended-collection-text-contracts.md)), presence of an authored `## Review` section, and the `watches:` list axis B needs.

- **A1 — full type spec + schema.** `kb/types/collection.md` with `kb/types/collection.schema.yaml`, validated like every other typed artifact. This has a self-referential consequence worth stating plainly: once a `COLLECTION.md` carries `type: kb/types/collection.md`, the *type-conformance* lens (ADR 038) derives a `(COLLECTION.md, collection type spec)` pair for it — the collection contract becomes a typed artifact reviewed against its own type spec, which is arguably the cleanest possible symmetry. It does not collide with the collection lens, which already refuses to pair a `COLLECTION.md` with itself (`note_collection_md_path` returns `None` for `COLLECTION.md`). One further flip is implicit and must be made explicit: the review-target selector admits a file as a reviewable note by checking for frontmatter (`_has_frontmatter` in `review_target_selector.py`), so today `COLLECTION.md` is excluded from note enumeration by its very lack of frontmatter. Typing it makes it enumerable — the self-referential type pair arrives through this door — so A1 must either accept `COLLECTION.md` as a first-class review target or add an explicit exclusion where an implicit one silently disappears.
- **A2 — minimal frontmatter, no schema.** Allow (or require) a small frontmatter block without a full type contract — enough to carry `watches:` and `register` — leaving shape unvalidated. Lower ceremony, but reintroduces the very hand-maintained-and-trusted metadata the derived-copy rule forbids: a `register:` field that duplicates the prose header must be machine-checked or absent.
- **A3 — stay positional (status quo).** Keep `COLLECTION.md` frontmatterless. Forecloses axis B for collections and keeps the lens asymmetry, but preserves ADR 041's simplicity.

*Forces.* ADR 041 chose A3 deliberately, reasoning that `requires_trait`/`requires_type` filtering "has no meaning" for a collection contract. That is true of *filtering* but not of `watches:`, which is not a filter — it is a triviality declaration. Typing also settles a latent question: `COLLECTION.md` is referenced by a definition (`kb/reference/definitions/collection.md`) but has no type governing its shape, so its required sections are convention, not contract.

### B. Optional `watches:` on conformance gate documents

Let a conformance gate document declare `watches:` (reusing the existing `{body, title, description}` vocabulary) and have `ack_trivial_note_changes.py` honor it for conformance pairs exactly as it does for catalog gates. A collection contract that governs only body prose could declare `watches: [body]`, making a pure-frontmatter note edit auto-ackable against it; a type spec whose authoring instructions never touch the description could do likewise.

- **B1 — honor `watches:` on conformance gates.** The ack loader already reads `watches:` from the gate path; it would simply find a value where today it finds none. For type specs this needs *nothing from axis A* — type specs already carry frontmatter and could declare `watches:` today. For `COLLECTION.md` it *requires axis A* — there is no frontmatter to hold the field. This is itself an asymmetry: the type lens can gain trivial-ack independently, the collection lens cannot.
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

- **B-for-collections requires A.** A `watches:` field on `COLLECTION.md` presupposes frontmatter, so the collection lens cannot gain trivial-ack without typing. B-for-types stands alone.
- **A opens a self-referential pair, not a cycle.** Typing `COLLECTION.md` makes it a type-conformance target of the collection type spec; because the collection lens never self-pairs, there is no loop — the collection contract is reviewed against its type, and notes are reviewed against the collection contract, two distinct edges.
- **C is orthogonal to A and B** but its payoff scales with them: more per-lens metadata handling (register, watches, `## Review` detection) is more surface to either duplicate across modules or centralize once.

## Free choices

- **Where the collection type spec lives** (if A1): global `kb/types/collection.md` (uniform with `note`, `adr`) versus a reference-local type. Global matches how every collection already loads its `COLLECTION.md` from a shared shape.
- **`watches:` vocabulary for conformance gates.** Reuse `{body, title, description}` unchanged, or add a conformance-specific token (e.g. `placement`) for clauses about where a note sits — which is not a note-part at all and may not fit the watches model.
- **Registry shape for C.** A dataclass list, a protocol with per-lens classes, or a dict keyed by lens name; the frontmatter-vs-location deriver is the field that must stay first-class whichever is chosen.
- **Whether A is adopted for its own sake** (validating `COLLECTION.md` shape, carrying `register`) independent of B, or only as B's prerequisite.

## Forces keeping this at planning

- **No demand signal.** No contract edit has yet produced enough contract-irrelevant note-ack churn to make B worth its correctness risk, and the two-module duplication in C is small and static.
- **ADR 041 chose the simple side on purpose.** Each axis here partially reopens a decision that was made deliberately; the proposal should not be adopted as a bundle just because the pieces are adjacent.
- **Symmetry is instrumental, not terminal.** The point of parity is letting clause placement follow scope; an asymmetry that never distorts placement is not worth machinery to erase.

## Adoption criteria

- Adopt **A** when a `COLLECTION.md` shape error ships undetected, or when [open-ended collection text contracts](./open-ended-collection-text-contracts.md) needs a validated `register`/`profile` field — its build-local-first path already wants one place to declare a collection's profile.
- Adopt **B** (types first, collections after A) when the first real contract edit forces more than a handful of per-note acks whose note diffs never touched the slice the contract governs. This is the same demand signal the [cohort-scoped ack](./factored-dependency-pairs-for-review-freshness.md) waits on, approached from the note-edit side.
- Adopt **C** when source-as-gate is built — write it as the third instance, then factor, so the abstraction is drawn from three worked lenses rather than fitted to two.

---

Relevant Notes:

- [038-type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — part-of: the type lens this proposal would bring the collection lens level with
- [041-collection-conformance reviews use COLLECTION.md as the gate](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — part-of: the collection lens whose three deferred symmetry choices this proposal maps
- [factored dependency pairs for review freshness](./factored-dependency-pairs-for-review-freshness.md) — part-of: source-as-gate is the third lens that motivates axis C; cohort-scoped ack is the gate-side twin of axis B
- [open-ended collection text contracts](./open-ended-collection-text-contracts.md) — see-also: typed COLLECTION.md frontmatter (axis A) is where its per-collection profile declaration would live
- [review architecture](../review-architecture.md) — part-of: the code carrying the two conformance gate sources axis C would unify
- [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — rationale: why a conformance gate's watches: slice is a well-typed triviality declaration
- [abstract an experience only when you can state the boundary](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — rationale: the rule-of-three timing for the code abstraction
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: why COLLECTION.md frontmatter that duplicates prose (register) must be schema-checked, not hand-trusted
- [link graph plus timestamps enables make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — rationale: the build-product/prerequisite model both lenses realize and any new lens inherits
