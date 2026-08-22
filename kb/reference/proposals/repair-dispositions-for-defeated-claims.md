---
description: "Proposal: the undecided remainder of repair-policy design after ADR 066 — declaring repair policy in an installation's local collection contract, and freshness-store drift tracking for idealization pricing attestations"
type: ../types/design-proposal.md
tags: [document-system, review-system]
---

# Repair dispositions for defeated claims are an epistemic policy with an option space

Which repairs review may take on a defeated claim is epistemic policy, not review mechanics, and different installations can legitimately want different policies. ADR 066 decided this installation's policy: claims declare one of three modes (universal, statistical, ideal-type) in the claim text, and the full pass repairs mode mismatch through mode-guarded reframes in both directions. What remains undecided here is the cross-installation half — whether repair policy becomes a clause that each installation declares in its own notes collection contract — and one deferred mechanism, drift tracking for the attestations an ideal-type claim's pricing rests on.

## Current state (as of 2026-08-19)

- **ADR 066 adopted the single-installation core** from this proposal: the three-mode vocabulary and its refuters in `kb/notes/COLLECTION.md` ("Claim modality"), in-text mode declaration with undeclared-reads-universal, modality-aware premise reading with counterexample-shape annotations in the premise-decomposition gate, and mode-guarded bidirectional reframes in the full-pass instruction. The evidence base — four trigger episodes and a 22-note corpus survey — is recorded in `kb/work/popperian-maintenance-episode/` and summarized in the ADR.
- **The adopted policy binds this installation only.** Its clauses live in `kb/notes/COLLECTION.md` and the full-pass instruction. No declaration surface lets another installation select a different policy while reusing the procedure, so a downstream installation that takes the shipped pass receives ADR 066's disposition logic silently. Collection prototypes are creation-time copies and cannot maintain or update an installed contract. No second installation with explanation-first goals exists to demand the parameterization.
- **Pricing attestations are immutable snapshots.** An ideal-type claim's routing evidence cites `kb/sources/` captures. Repository-input freshness cannot notice an immutable attestation becoming obsolete as external domain practice drifts (an exception becoming ordinary unmarked practice) — the criterion note's re-testing open question. Review pairs carry exactly two tracked inputs (note, criterion); the freshness architecture admits new dependencies as factored `(note, dependency)` pairs, the direction held open in [factored dependency pairs for review freshness](./factored-dependency-pairs-for-review-freshness.md), not shipped machinery.

## The design space

1. **Collection-contract repair policy.** Each installation's notes `COLLECTION.md` declares which repair dispositions review may take on defeated claims — reframe-to-warranted only, mode-guarded reframes (ADR 066's policy), or keep-as-conjecture-at-declared-stage — and the pass instruction reads the local declaration. Installations with explanation-first goals choose differently from decision-support installations. Operativity: the pass already loads the target collection contract, but no repair-policy parser or branch exists; both the declaration vocabulary and conditional disposition logic must be built. Cost: epistemic-policy proliferation across installations, and a currently fixed instruction becomes conditional on an additional contract clause.
2. **Attestation drift tracking.** Register an ideal-type claim's pricing attestations as factored `(note, attestation)` freshness pairs so domain drift surfaces as input staleness instead of waiting for a noticed counterexample. Rides the factored-dependency-pairs proposal; adopting it here means adopting that machinery for this consumer. The alternative is the ADR 066 status quo: drift is caught only when a pass re-runs the premise gate over the claim's adequacy record.

## Free choices

- **The declaration shape** (option 1): one controlled value in the local collection contract, or explicit permitted dispositions with compatibility checks. In either case the local contract binds and the pass consumes it; a collection prototype may show starting prose for future copies but supplies no installed value.
- **Whether conjecture-stage keeping is a distinct policy value** (option 1) or collapses into the existing status-conjecture idiom — the discovery lifecycle already names the stages; what is missing is only a disposition that routes to one.
- **Drift-detection granularity** (option 2): one factored pair per attestation, or one per claim aggregating its attestations.

## Adoption criteria

- **Option 1 adopts on a second installation**, or a first concrete case of an installation wanting a policy other than ADR 066's. Building the parameterization ahead of any demand repeats the implementation-plan-first mistake this collection's contract warns against.
- **Option 2 adopts with the factored-dependency-pairs proposal**, on its criteria, with an ideal-type claim's attestation set as the demanding consumer.
- **Whatever ships is consumed, not decorative**: the pass instruction's disposition step reads the local declaration and its report names the policy value that governed the repair.

## Risks

- **Policy proliferation.** Per-installation epistemic policy invites every installation to invent its own falsification rules; the mitigation is a small instruction-owned vocabulary whose values have distinct, tested disposition behavior rather than free-form declarations.
- **Silent inheritance is the live default.** Until option 1 ships, downstream installations get ADR 066's policy without a surface that tells them so.

---

Relevant Notes:

- [Domain pricing routes an exception to idealization assessment but does not decide it](../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) — rests-on: the two-stage requirement any policy bundle's ideal-type option must encode, and the source of the re-testing question option 2 answers
- [Narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: the analytic limit that makes repair policy consequential — a policy is what stands between defeat and degenerate repair
- [Generality bought to avoid counterexamples is paid for in precision](../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — rests-on: each escape from counterexamples needs a discriminator for honest versus degenerate use; a policy bundle is a chosen set of such discriminators
