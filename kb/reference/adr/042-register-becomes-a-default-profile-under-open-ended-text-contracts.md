---
description: "Register retires as a closed taxonomy; COLLECTION.md must declare a text contract, and theoretical/descriptive/prescriptive persist as named default profiles in an open, worked-case-gated library"
type: ../types/adr.md
tags: []
status: accepted
---

# 042-Register becomes a default profile under open-ended text contracts

**Status:** accepted
**Date:** 2026-07-09
**Extends:** [ADR-017](./017-collection-md-is-the-register-convention-boundary.md), [ADR-019](./019-collection-owned-link-vocabulary.md), [ADR-038](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md), [ADR-041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md)

## Context

Commonplace grounded its writing conventions in a closed taxonomy: three registers (theoretical, descriptive, prescriptive), claimed exhaustive because every consumer question reduces to "why," "what," or "how." But ADR-017 → ADR-019 → ADR-038 → ADR-041 already moved authority elsewhere: `COLLECTION.md` is the register convention boundary (017), the collection rather than the register is the anchor for link vocabulary (019), and both the type contract (038) and the collection contract (041) are semantically enforced. Nothing mechanical reads the three-way taxonomy any more; only prose does. A claim that no longer gates any mechanism but still blocks new contracts is pure liability.

The trigger was concrete. Casework on stance-neutral evidence maps needed a dialectical/evidential text contract — topical titles, mandatory attribution of every proposition, "faithfully represents the contestation" as the quality bar. Under the closed taxonomy this had to be argued into one of the three registers or it falsified the exhaustiveness claim. The sibling `epistack-casebooks` repo instantiated the contract directly as `kb/lhc/notes/COLLECTION.md` and exercised it — five casebook notes over eight captured sources for the LHC/black-hole-fears case. The contract held: its distinguishing bar (stance-neutral attributed mapping, not truth or belief; topical not claim titles; maintenance is "still an accurate map of the debate," not "do I still believe this") survived all five notes without collapsing into an existing register. It did not fold into descriptive-plus-a-clause — descriptive's quality bar is fidelity to a known referent; the dialectical bar is non-adjudicated mapping between competing parties, a different epistemic stance. That result is the adoption evidence this ADR acts on.

## Decision

The binding requirement is restated as the primitive: every writable collection's `COLLECTION.md` declares a **text contract** — orientation, quality goal, title and description conventions, any attribution/evidentiality requirements, maintenance semantics, and outbound link grammar. This is what ADR-017 already required; what changes is that the contract, not the register, is the named primitive, and theoretical/descriptive/prescriptive become named **profiles** — proven bundles of text-contract features a collection may adopt wholesale, extend, or replace, drawn from an open, guarded library rather than a closed partition every artifact must fit.

**How a contract decomposes across surfaces.** A text contract is not one document — its clauses land on different system surfaces by their quantifier, what set of artifacts a clause binds:

- binds everything in the subtree, whatever its shape → the collection's `COLLECTION.md`;
- binds every artifact of a shape, wherever it lives → a global type spec;
- binds a shape that only exists under this contract → a collection-local type spec (locality expresses the coupling);
- binds only artifacts that opt in → a trait.

Enforcement is orthogonal to placement and chosen per clause, not per surface: since ADR-038/041 both contract surfaces are enforceable at every tier — unenforced prose, reviewed prose (a conformance pair, sharpened by an authored `## Review` section the freshness hash sees), or code (a type schema) — and a clause typically migrates up that ladder as it proves out, cheapest first. The dialectical profile is the worked example: its "every proposition attributed" clause binds the whole casebook subtree, so it is a `COLLECTION.md` clause; if ever mechanized, the mechanism would be a field on a collection-local `claim` type schema — obligation and mechanism, same clause at different tiers, no surface conflict. (The clause's transferable substrate — placement by quantifier, the directory-vs-frontmatter asymmetry — is promoted separately in [directory placement is total, frontmatter classification is partial](../../notes/directory-placement-is-total-frontmatter-classification-is-partial.md); the mapping above is its Commonplace-specific instantiation.)

This ADR adopts the proposal's four locked decisions:

1. **Retire "register."** Rename to **text contract** (the requirement — what a `COLLECTION.md` states) and **profile** (the library entry — a named, proven bundle). The definition note at `kb/notes/definitions/register.md` is renamed to `kb/notes/definitions/text-contract.md` and revised to define both terms in place of the single register concept. `AGENTS.md`'s vocabulary entry and each collection's `COLLECTION.md` header get the same mechanical rename. The concepts doing real analytical work — the theoretical profile's formulation constraint, the dialectical profile's mandatory evidentiality — carry over unchanged; only the taxonomy label retires.
2. **The profile library lives in `kb/reference/`**, as a catalogue document parallel to [link-vocabulary.md](../link-vocabulary.md), governed the same way: ADR-019's worked-case-first promotion. The catalogue tracks which profiles are decided and shipped, which collections use each, and which ADR promoted it. It stays separate from the text-contract definition note, which states the theory (what a text contract is, why the set is open but guarded) — mixing an invariant claim with system state that goes stale on its own schedule is the category mistake this ADR is fixing.
3. **The foundation note is revised in place, not superseded.** [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) keeps its title's claim unchanged — it never asserted exhaustiveness. Only the "the three registers are exhaustive because..." paragraph and the "correspond to classical sub-disciplines" section are rewritten to the weaker, honest claim: why/what/how are strong recurring attractors, evidenced by convergent traditions and by this KB's own bottom-up discovery, not a provable partition. The formulation-constraint and maintenance-asymmetry sections are unaffected — those two properties made the distinction real and stay features of specific profiles, not of a taxonomy.
4. **Narrative/log does not become a named profile in this round.** It stays an acknowledged-but-unnamed convention (`kb/log.md`, workshop state, backlog logs). It recurs and is real, but nobody has written out its actual contract (quality goal, title convention, attribution, maintenance semantics, link grammar) the way the dialectical contract was written and exercised, and the known instances of it may not even be the same profile. Naming it now would repeat the premature-taxonomy mistake this ADR exists to fix; revisit only if someone deliberately specifies and exercises a narrative contract later.

Mechanical execution of items 1–3 has shipped: the definition note is renamed to [text contract](../../notes/definitions/text-contract.md) and revised, the [profile catalogue](../text-contract-profiles.md) is added, the foundation note is revised in place, and `AGENTS.md`'s vocabulary entry and routing table are updated. The originating proposal is fully implemented, not merely superseded by a different design, and is removed rather than kept as a stub; this ADR is its complete historical record, including the surface-decomposition mapping above, which the proposal asked to be recorded here on adoption.

## Consequences

**Easier:**

- The exhaustiveness claim no longer blocks new contracts. A fourth profile — dialectical/evidential — is addable without theory surgery or falsifying a foundation note; `kb/lhc/notes/COLLECTION.md` in the sibling `epistack-casebooks` repo is retroactively the first proof of the open-ended shape.
- Terminological honesty: "register" stops borrowing linguistic-register prestige for a closed set that linguistics (Halliday; Biber & Conrad) doesn't actually support.
- Enforcement is already symmetric (ADR-038/041), so a new profile costs one `COLLECTION.md` and is born reviewable — no enforcement debt accrues as the library grows, unlike before ADR-041 when only the type surface was enforced and clauses migrated there to get checked.
- The cheap routing shortcut survives: `AGENTS.md`'s "theoretical / descriptive / prescriptive" table keeps working verbatim: profiles keep their names, only the closed-set claim is dropped.

**Harder / accepted costs:**

- Coordinated rename across four-plus surfaces (definition note and its backlinks, `AGENTS.md` vocabulary entry and routing table, each `COLLECTION.md` header, the foundation note) was executed as follow-up work after this ADR, not atomically with it — a real cost if any surface had been missed, though the rename tool's backlink sweep and per-file validation closed that gap.
- The foundation note got a partial, in-place revision (one paragraph and one section) rather than a clean supersession, which was more delicate to get right than replacing the whole note, and it carries `title-as-claim` so the edit had to be checked against that constraint.
- Profile-library growth is guarded, not free: a new profile still needs to survive contact with a real collection (as the dialectical profile did in `epistack-casebooks`) before promotion to the shared `kb/reference/` catalogue — proliferation risk is mitigated, not eliminated, and the guard is a step no closed taxonomy needed.
- The narrative/log convention stays a known, deliberately unnamed gap (Decision 4) rather than a closed one.

**Not changing:**

- The decomposition of a text contract across system surfaces — `COLLECTION.md` for subtree-wide clauses, global type specs for shape-wide clauses, collection-local type specs for shape-that-only-exists-here clauses, traits for opt-in clauses (recorded above) — is unaffected in substance by this ADR; only its record moves here. The transferable substrate behind it was already promoted independently of the register/profile rename, in [directory placement is total, frontmatter classification is partial](../../notes/directory-placement-is-total-frontmatter-classification-is-partial.md).
- ADR-017's boundary (`COLLECTION.md` owns collection conventions) and ADR-019's per-destination link-vocabulary architecture stand unchanged; this ADR only renames and opens the taxonomy those two ADRs already anchor to the collection rather than the register.

---

Relevant Notes:

- [Register](../../notes/definitions/text-contract.md) — operates-on: the definition note this decision renames to `text-contract.md` and revises
- [A knowledge base holds theories, descriptions, and prescriptions with asymmetric linking](../../notes/a-knowledge-base-holds-theories-descriptions-and-prescriptions-with.md) — operates-on: the foundation note revised in place per Decision 3
- [ADR-017: COLLECTION.md is the register convention boundary](./017-collection-md-is-the-register-convention-boundary.md) — extends: the convention-boundary mechanism this ADR renames but does not alter
- [ADR-019: collection-owned link vocabulary](./019-collection-owned-link-vocabulary.md) — extends: precedent for both the collection-as-anchor move and the worked-case-first promotion guard reused for the profile library
- [ADR-038: type-conformance reviews use the type spec as the gate](./038-type-conformance-reviews-use-the-type-spec-as-the-gate.md) — extends: made the type-side contract enforced, part of why the exhaustiveness claim stopped gating anything
- [ADR-041: collection-conformance reviews use COLLECTION.md as the gate](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md) — extends: made the collection-side contract enforced, so a new profile is born with review machinery
- [link-vocabulary.md](../link-vocabulary.md) — compares-with: the sibling open, worked-case-gated catalogue this ADR's profile library is modeled on
- [A universal knowledge framework demotes content taxonomies to defaults and keeps answerability](../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) — rationale: the transferable claim this ADR instantiates for registers
