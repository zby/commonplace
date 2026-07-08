---
description: "COLLECTION.md files carry frontmatter and a collection type spec, making the contract validated, navigable, and reviewable against its own type — closing part of the type/collection gate-document asymmetry"
type: ../types/adr.md
tags: []
status: accepted
---

# 042-Collection contracts are typed artifacts

**Status:** accepted
**Date:** 2026-07-08

## Context

[ADR 041](./041-collection-conformance-reviews-use-collection-md-as-the-gate.md) made `COLLECTION.md` an enforced contract surface but accepted an artifact-level asymmetry: "`COLLECTION.md` files carry no frontmatter, so unlike catalog gates they cannot declare `watches:` or gate metadata; all filtering is positional." A type spec — the other conformance gate document — is itself a typed artifact: `type: kb/types/type-spec.md`, schema-validated, carrying a retrieval `description`. A bare `COLLECTION.md` was invisible to `rg "^description:"` navigation sweeps, structurally unvalidated beyond the nested-contract check, and reviewable by no pair — and its exclusion from review-target enumeration was implicit, resting on the selector's has-frontmatter filter rather than a stated rule.

The option space is mapped in [making the conformance lenses symmetric](../proposals/making-the-conformance-lenses-symmetric.md); this ADR adopts its axis A (option A1) and leaves axes B (`watches:` on conformance gates) and C (shared lens abstraction) in the proposal.

## Decision

Every `COLLECTION.md` is a typed artifact bound to a new global type spec.

- **`kb/types/collection.md` + `kb/types/collection.schema.yaml`.** The schema requires `type` and `description` and nothing else; body structure stays unconstrained because contracts legitimately vary by collection. No `status` or `tags`: a contract is not a note moving through a writing lifecycle. The type spec's body states the contract's content obligations (purpose/register, quality goal, title/description conventions, type guidance, link policy) and the clause-placement rule (collection-scoped clauses only).
- **All contracts carry frontmatter.** The seven source-repo `COLLECTION.md` files and the three scaffold templates (`user-*-COLLECTION.md`) declare `type: kb/types/collection.md` plus a retrieval `description`. Installed projects keep `kb/types/` at top level, so the same type path resolves in both layouts.
- **Validating a collection validates its contract.** `commonplace-validate <collection>` includes the collection's `COLLECTION.md` in scope; contracts are exempt from the orphan info check (they are routed to positionally, not by links).
- **Note enumeration excludes contracts explicitly.** The review-target selector previously excluded `COLLECTION.md` only via its has-frontmatter filter; that exclusion is now an explicit rule, matching how type-spec content is excluded. Directory sweeps and `--current` keep their membership. Explicitly selecting a `COLLECTION.md` by path still works and derives its type-conformance pair against `kb/types/collection.md` — the contract is reviewable on demand, and the collection lens still never pairs a contract with itself.
- **Auto-ack semantics unchanged.** Contracts declare no `watches:`, so no note change is trivial against a conformance pair; adopting `watches:` remains axis B of the proposal.

## Consequences

Easier:

- Contract shape errors are caught deterministically, and every collection's role is visible to description-based navigation sweeps.
- The contract itself is reviewable: `commonplace-review-target-selector <path>/COLLECTION.md type` derives a `(contract, collection type spec)` pair, giving contract prose the same review machinery notes have.
- The gate documents of both conformance lenses are now typed artifacts, and future gate metadata (axis B's `watches:`, the open-ended-contracts proposal's profile declaration) has a validated home.

Harder / costs:

- Adding frontmatter changed every contract's text, so every collection's conformance cohort flips `gate-changed` once — the cohort-blast-radius case the [factored-pairs proposal](../proposals/factored-dependency-pairs-for-review-freshness.md) names; acks are per-note until a cohort-scoped ack exists.
- ADR 041's "no frontmatter, all filtering positional" consequence is amended by this decision; pair *derivation* stays positional — the frontmatter must never restate the collection's location or identity.
- The scaffold templates and shipped contracts must keep frontmatter in sync with the schema as it evolves.
