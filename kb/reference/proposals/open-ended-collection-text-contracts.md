---
description: "Proposal: demote register from closed taxonomy to default profiles — the binding requirement is that each collection's COLLECTION.md declare its text contract, and the contract set is open-ended"
type: kb/types/note.md
traits: [design-proposal]
tags: [document-system]
status: seedling
---

# Open-ended collection text contracts

Commonplace currently grounds its writing conventions in a **closed taxonomy**: three registers (theoretical, descriptive, prescriptive), claimed exhaustive — "if you try to state a fourth register, it collapses into one of the three." This proposal demotes the taxonomy. The binding requirement was never the tripartition; it is that **each writable collection declares its text features** — quality goal, title convention, attribution requirements, maintenance semantics, link grammar — in its `COLLECTION.md`. The three registers become named **default profiles** in an open-ended library: proven bundles of text features a new collection adopts, extends, or replaces, not a partition every artifact must fit.

The trigger is concrete: casework on stance-neutral evidence maps (the `kb/work/epistack-framework-additions/` workshop) needs a dialectical/evidential text contract — topical titles, mandatory attribution of every proposition, "faithfully represents the contestation" as the quality bar. Under the closed taxonomy this must either be argued into one of the three modes or falsify the exhaustiveness claim. Under open-ended contracts it is just another profile, provable in a consuming project without theory surgery.

## Current state (as of 2026-07-08)

Where register is load-bearing today, ordered by how much this proposal would change it:

- **Theory layer** — [register](../../notes/definitions/register.md) (definition) and [a knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) (foundation note) both state the three registers are *exhaustive*, argued from query shapes ("why/what/how") and the classical epistemology/ontology/praxeology tripartition.
- **AGENTS.md** — the vocabulary entry defines register as "one of three content modes"; the collection routing table names each collection's register.
- **Convention machinery** — [ADR 017](../adr/017-collection-md-is-the-register-convention-boundary.md) already made `COLLECTION.md` the convention boundary and explicitly notes that register-per-collection is a design choice, with mixed-register collections allowed. [ADR 019](../adr/019-collection-owned-link-vocabulary.md) already made the collection, not the register, the anchor for link vocabulary ("Collection, not register, is the anchor"), with register surviving as the grouping scheme for default templates in the [link-vocabulary catalogue](../link-vocabulary.md) (e.g. ADR 020's "theoretical-register default template").
- **Enforcement machinery** — [ADR 038](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) and [ADR 041](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md) made both contract surfaces semantically enforced: every note carries derivable conformance pairs against its type spec and its collection's `COLLECTION.md`, so a text contract is a review gate rather than advisory prose, and a contract edit stales exactly its cohort. ([ADR 012](../adr/012-types-for-structure-traits-for-review.md)'s traits-only semantic-review boundary is amended accordingly.) The binding requirement this proposal rests on is therefore mechanically checkable.
- **Collection surfaces** — each `COLLECTION.md` headlines its register ("Writing conventions for kb/notes/ (theoretical register)") and links the definition.

So the architecture has already moved: authority over conventions and vocabulary sits in `COLLECTION.md` per collection, and the contract itself is enforced. The exhaustiveness claim no longer gates any mechanism — it survives only as theory prose and naming. This proposal finishes the move the ADR 017 → ADR 019 → ADR 041 trajectory started.

## The design

1. **Binding requirement (unchanged in substance, restated as the primitive).** Every writable collection's `COLLECTION.md` declares its **text contract**: orientation (what the artifacts do), quality goal, title and description conventions, any attribution/evidentiality requirements, maintenance semantics (what makes an artifact here stale), and outbound link grammar. This is what ADR 017 already requires; the change is that the contract is the primitive, not an instantiation of a register.
2. **The three registers become default profiles.** Theoretical, descriptive, and prescriptive persist as named, documented profiles — the same bundles of features they are today, kept because they are proven and cover most collections. A new collection adopts one wholesale (one line plus exceptions, as today), extends one, or writes its contract from scratch.
3. **The profile set is open-ended, guarded.** New profiles are not taxonomy amendments; they are new entries justified the same way ADR 019 governs new link labels — demonstrated need from a real collection, build-local-first in a consuming project or single collection, promoted to the shared library only after surviving a worked case. The guard replaces what exhaustiveness used to do (blocking premature taxonomy growth) without forbidding growth outright.
4. **The theory weakens honestly rather than disappearing.** The foundation note's tripartition survives as an empirical claim: why/what/how are strong attractors that recur across KBs, and the classical tripartition is evidence they are natural — but attractors, not a partition. The two properties that made registers real — the formulation constraint and maintenance asymmetry — are untouched: they are features *of specific profiles* (the theoretical profile's formulation constraint; the theory→prescription→description flow), not of the taxonomy.

The linguistics supports the demotion, and the supporting claim should be promoted to a theory note on adoption (per this collection's contract, transferable requirements live in `kb/notes/`): linguistic *register* proper (Halliday; Biber & Conrad) is open-ended situational variation with no exhaustive list, so the borrowed term never licensed a closed set. The closed sets that do exist are text-type typologies — Werlich's five (description, narration, exposition, argumentation, instruction), Longacre's four, Smith's five discourse modes — which disagree on the count and are typologies, not proofs. Notably most include modes Commonplace already handles *outside* the register system (narration → `kb/log.md`, workshop state), which is itself evidence the tripartition was a chosen profile set, not an exhaustive partition.

## How a contract decomposes across surfaces

A text contract is not one document. Its clauses land on the system's contract surfaces, and the placement rule is the clause's *quantifier* — what set of artifacts it binds:

- binds everything in the subtree, whatever its shape → the collection's `COLLECTION.md`;
- binds every artifact of a shape, wherever it lives → a global type spec;
- binds a shape that only exists under this contract → a collection-local type spec (locality expresses the coupling);
- binds only artifacts that opt in → a trait.

Enforcement is orthogonal to placement and chosen per clause, not per surface. Since ADR 038/041, both contract surfaces are enforceable at every tier: unenforced prose; reviewed prose (the conformance pair against the contract document, sharpened by an authored `## Review` section the freshness hash sees); and code (the type schema, checked deterministically). A clause typically migrates up that ladder as it proves out — born as contract prose, hardened into a reviewable criterion, codified into a schema field. This is the constraining→codification axis run *within* one surface rather than between surfaces, and it is what keeps an open-ended contract set cheap to govern: a new contract costs one `COLLECTION.md` and is born enforceable — its conformance pair exists the moment the file does — while heavier machinery is earned clause-by-clause.

The decomposition also resolves the trigger case without a choice of surface: the dialectical contract's "every proposition attributed" is a collection clause (it binds the whole casebook subtree), and its mechanization, if wanted, is a field on a collection-local `claim` type schema — obligation and mechanism, same clause at different tiers. On adoption, the decomposition rule (placement by quantifier; enforcement tier per clause; prose → review → schema migration) should be promoted to a theory note in `kb/notes/`, alongside the linguistics claim above.

## Forces

- **For: the exhaustiveness claim has no remaining enforcement role.** After ADR 017/019, nothing mechanical reads the taxonomy; only prose does. A theory claim that no longer gates anything but still blocks new contracts is pure liability.
- **For: it unblocks the dialectical/evidential contract** without forcing a false choice between "argue it into descriptive" and "falsify a foundation note." The casework experiment can define its contract locally and the result promotes cleanly either way.
- **For: terminological honesty.** "Register" currently implies linguistic backing for a closed set that linguistics doesn't provide.
- **For: enforcement no longer favors the incumbent surfaces.** Before ADR 041 the type spec was the only enforced prose contract, which pushed collection-scoped clauses into type specs to get them checked. With symmetric enforcement, a new contract states its clauses at their honest scope from day one and is no worse-policed than the three defaults.
- **Against: the tripartition does cheap routing work.** "Theoretical / descriptive / prescriptive" in the AGENTS.md routing table lets an agent infer the writing goal from one word. Mitigation: the profiles keep their names and the table keeps working; only the claim that the list is closed goes.
- **Against: proliferation risk.** Open-ended contracts invite one-off profiles with inconsistent quality bars. Mitigation: the ADR 019-style guard (worked-case-first promotion) plus the default profiles covering the common cases — and, since ADR 041, mechanical enforcement: every contract is a conformance gate, so even a one-off contract is reviewable and its drift tracked. The guard governs entry to the shared profile library; enforcement governs quality within each contract.
- **Against: revision cost.** The definition, the foundation note, AGENTS.md, and four-plus `COLLECTION.md` headers all need coordinated edits, and the foundation note carries `title-as-claim` — weakening its claim may mean retitling and re-linking.

## Free choices

- **Keep or retire the word "register."** (a) Keep it, redefined as open-ended — matches the linguistic sense, minimal churn; (b) rename to "text contract" (the requirement) + "profile" (the library entry) — clearer split, more churn. The design works under either.
- **Where the profile library lives.** Inside the register/contract definition note, or as a catalogue document in `kb/reference/` parallel to [link-vocabulary.md](../link-vocabulary.md).
- **Revise the foundation note in place or supersede it** with a new claim note (roughly: *collection text contracts are open-ended; theory, description, and prescription are attractors, not a partition*), keeping the old note as superseded history.
- **Whether narrative/log becomes a named profile** now that the set is open, or stays an unnamed convention of `kb/log.md` and workshops.

## Adoption criteria

Adopt (convert to an ADR) when the first non-tripartition text contract survives a worked case — the dialectical/evidential contract from the epistack casework is the natural candidate, and its build-local-first path is already agreed. ADR 041 makes that trial cheaper than when this was first drafted: the contract is one `COLLECTION.md` (plus an optional `## Review` section) in the casebook repo, born with conformance enforcement and cohort invalidation, no new mechanism. If that contract instead folds cleanly into the descriptive profile plus an evidentiality clause, adopt the weaker form: keep the taxonomy demotion (the open-endedness and the guard) but skip the profile-library split until a second real profile appears.

---

Relevant Notes:

- [Register](../../notes/definitions/register.md) — operates-on: the definition this proposal would redefine or supersede
- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — operates-on: the foundation note whose exhaustiveness claim this proposal weakens to an attractor claim
- [ADR-017: COLLECTION.md is the register convention boundary](../adr/017-collection-md-is-the-register-convention-boundary.md) — part-of: the convention-boundary decision this proposal completes; its mechanism is unchanged
- [ADR-019: collection-owned link vocabulary](../adr/019-collection-owned-link-vocabulary.md) — part-of: precedent for the anchor move (collection over register) and for the worked-case guard on vocabulary growth
- [ADR-038: type-conformance reviews use the type spec as the gate](../adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — part-of: made the type-side contract enforced, decoupling enforcement tier from contract surface
- [ADR-041: collection-conformance reviews use COLLECTION.md as the gate](../adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — part-of: made the collection contract enforced, so a new text contract is born with review machinery and the open-ended set stays governable
- [Design proposals differ from claims in kind, not confidence](../../notes/design-proposals-differ-from-claims-in-kind-not-confidence.md) — rationale: why this ships as a proposal object rather than edits to the theory layer
