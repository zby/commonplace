---
description: "Proposal: the undecided remainder of repair-policy design after ADR 066 — declaring repair policy per text-contract profile for installations with non-decision-support goals, and freshness-store drift tracking for idealization pricing attestations"
type: ../types/design-proposal.md
tags: [document-system, review-system]
---

# Repair dispositions for defeated claims are an epistemic policy with an option space

Which repairs review may take on a defeated claim is epistemic policy, not review mechanics, and different installations can legitimately want different policies. ADR 066 decided this installation's policy: claims declare one of three modes (universal, statistical, ideal-type) in the claim text, and the full pass repairs mode mismatch through mode-guarded reframes in both directions. What remains undecided here is the cross-installation half — whether repair policy becomes a declared text-contract profile feature that other installations can set differently — and one deferred mechanism, drift tracking for the attestations an ideal-type claim's pricing rests on.

## Current state (as of 2026-08-19)

- **ADR 066 adopted the single-installation core** from this proposal: the three-mode vocabulary and its refuters in `kb/notes/COLLECTION.md` ("Claim modality"), in-text mode declaration with undeclared-reads-universal, modality-aware premise reading with counterexample-shape annotations in the premise-decomposition gate, and mode-guarded bidirectional reframes in the full-pass instruction. The evidence base — four trigger episodes and a 22-note corpus survey — is recorded in `kb/work/popperian-maintenance-episode/` and summarized in the ADR.
- **The adopted policy binds this installation only.** `kb/reference/text-contract-profiles.md` catalogues profile features (quality goal, title convention, attribution, maintenance semantics, link grammar); repair policy is not among them, so a downstream installation inherits ADR 066's policy silently with the framework. No second installation with explanation-first goals exists to demand the parameterization.
- **Pricing attestations are immutable snapshots.** An ideal-type claim's routing evidence cites `kb/sources/` captures. Repository-input freshness cannot notice an immutable attestation becoming obsolete as external domain practice drifts (an exception becoming ordinary unmarked practice) — the criterion note's re-testing open question. Review pairs carry exactly two tracked inputs (note, criterion); the freshness architecture admits new dependencies as factored `(note, dependency)` pairs, the direction held open in [factored dependency pairs for review freshness](./factored-dependency-pairs-for-review-freshness.md), not shipped machinery.

## The design space

1. **Profile-level repair policy.** The text-contract profile declares which repair dispositions review may take on defeated claims — reframe-to-warranted only, mode-guarded reframes (ADR 066's policy), keep-as-conjecture-at-declared-stage — and the pass instruction reads the declaration. Installations with explanation-first goals choose differently from decision-support installations. Operativity: no consumer yet; the profile catalogue would need a declared-feature slot and the pass instruction a parameterization it currently does not have — both must be built, which is exactly what the adoption decision needs to see. Cost: epistemic-policy proliferation across installations, and the pass instruction's disposition logic becomes conditional on a document it currently never reads.
2. **Attestation drift tracking.** Register an ideal-type claim's pricing attestations as factored `(note, attestation)` freshness pairs so domain drift surfaces as input staleness instead of waiting for a noticed counterexample. Rides the factored-dependency-pairs proposal; adopting it here means adopting that machinery for this consumer. The alternative is the ADR 066 status quo: drift is caught only when a pass re-runs the premise gate over the claim's adequacy record.

## Free choices

- **Where the policy is declared** (option 1): the profile catalogue, the collection contract, or both — the catalogue names the feature for discovery, the contract binds it; a catalogue-only declaration would be decorative.
- **Whether conjecture-stage keeping is a distinct policy value** (option 1) or collapses into the existing status-conjecture idiom — the discovery lifecycle already names the stages; what is missing is only a disposition that routes to one.
- **Drift-detection granularity** (option 2): one factored pair per attestation, or one per claim aggregating its attestations.

## Adoption criteria

- **Option 1 adopts on a second installation**, or a first concrete case of an installation wanting a policy other than ADR 066's — the profile catalogue's worked-case-first bar; building the parameterization ahead of any demand repeats the implementation-plan-first mistake this collection's contract warns against.
- **Option 2 adopts with the factored-dependency-pairs proposal**, on its criteria, with an ideal-type claim's attestation set as the demanding consumer.
- **Whatever ships is consumed, not decorative**: the pass instruction's disposition step reads the declaration, and a downstream installation reading the profile catalogue can see which repair policy it has adopted.

## Risks

- **Policy proliferation.** Per-installation epistemic policy invites every installation to invent its own falsification rules; the mitigation is shipping named, proven policy bundles rather than free-form declaration.
- **Silent inheritance is the live default.** Until option 1 ships, downstream installations get ADR 066's policy without a surface that tells them so.

---

Relevant Notes:

- [Domain pricing routes an exception to idealization assessment but does not decide it](../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) — rests-on: the two-stage requirement any policy bundle's ideal-type option must encode, and the source of the re-testing question option 2 answers
- [Narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: the analytic limit that makes repair policy consequential — a policy is what stands between defeat and degenerate repair
- [Generality bought to avoid counterexamples is paid for in precision](../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — rests-on: each escape from counterexamples needs a discriminator for honest versus degenerate use; a policy bundle is a chosen set of such discriminators
