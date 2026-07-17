# The polation structure of generalization

Tangent thread, split out of the [vocabulary thread](./derivation-selection-vocabulary.md): Toby Ord's [interpolation / extrapolation / hyperpolation](../../sources/interpolation-extrapolation-hyperpolation.md) triple maps onto the derivation / routine-induction / discovery split and gives the ampliative side a principled internal grading.

## The mapping

Ord carves function generalisation into mutually exclusive, jointly exhaustive cases by where the queried point lies relative to the data: **interpolation** (in the convex hull), **extrapolation** (in the affine hull but outside the convex hull), **hyperpolation** (off the data's subspace entirely); plus degenerate **autopolation** (at a data point). Read with a source artifact's claims as the data and claim space as the domain:

| Polation | KB operation | Signature |
|---|---|---|
| autopolation / interpolation | **derivation** | output stays inside the source's entailment closure; no new commitments |
| extrapolation | **routine induction** (failures→gate, episode→rule) | output extends along dimensions the instances already have; the [boundary clause](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) is the declared extrapolation range |
| hyperpolation | **discovery proper** (positing a generative model, naming a mechanism) | output lies off the source's subspace; the [discovery note](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md)'s "inventing the dimension along which the comparison becomes visible" is Ord's definition almost verbatim |

A clarification the mapping forces: **distance in representational form ≠ distance in content.** A derived artifact can be far in form (theory → procedure, prose → checklist) while being zero distance in content. The current "distillation" vocabulary blurs exactly this, which is one reason the ampliative leak went unnoticed.

## What the frame buys

1. **Routing.** The ampliative operation is one thing graded by off-manifold distance, and discovery's three-depths table (shared feature → shared structure → generative model) already runs this gradient: shared structure ≈ extrapolation, generative model ≈ hyperpolation. So the split can extend discovery rather than adding a term — the polation axis is discovery's internal structure, with routine induction as its shallow extrapolative end.
2. **Both bets get the same geometry, over different random variables.** Ord stresses that all three polations are the same Bayesian method — prior over functions, update on the data — differing only in where the queried point lies. Two distinct bets in this workshop inherit the frame: the **classification bet** (assistant proposal, [vocabulary thread](./derivation-selection-vocabulary.md)) is about where an artifact's *claims* sit relative to its source, with verification burden scaling off-manifold — hyperpolation is the least well-posed (Ord), which is the discovery note's "compellingly wrong (phlogiston)" restated. The **coverage bet** (operator position, [two-layer structure note](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md#the-coverage-bet-is-not-the-correctness-bet)) is about where the *future query distribution* sits relative to the derived methodology's hull — creating the effective layer is warranted only if enough traffic lands inside its cutoff.
3. **Abduction unifies two borrowings.** Ord explicitly proposes hyperpolation as a mathematical model of abduction; Peirce's abduction is already a [philosophy-borrowing](../philosophy-borrowing/README.md) candidate for note promotion. One borrowing, two entry points.
4. **A warrant criterion for positing generals.** Ord's condition for good hyperpolation — *the whole is simpler than the slice* (the ripple is simpler than the curve it explains) — is a one-sentence version of the KB's naming-amortizes-discovery-cost and [reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) criteria: discovery is licensed when the posited general is simpler than the particulars it explains.
5. **The two-layer structure gets hull language.** In the [theory–methodology structure](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md), a corner case is a query outside the methodology's hull; fallback works because the generator theory has a larger hull; the methodology's declared cutoff *is* its hull boundary; and promotion-by-matching extends the hull by one region. Reach, in this language, is roughly how much hyperpolation a theory supports.
6. **Inductive-bias thread connection.** Extrapolation needs bias; hyperpolation needs priors over functional forms (Ord's Bayesian reading — and his cited Lucas et al. "superspace extrapolation" experiments are literally inductive-bias measurements). The [methodology-as-inductive-bias](./methodology-as-inductive-bias.md) claim — promotion is the system acquiring its own bias — extends: *what* is acquired is a prior that makes tomorrow's extrapolations cheap.

## Caveat

The transfer is the qualitative carving (within / beyond-along-existing-dimensions / off-subspace), not the geometry. Claim space has no literal convex hull and entailment closure is not one. Ord himself applies the triple informally outside mathematics (music genres, futurism), so this is a licensed use — but a definition note leaning on it must say the space is metaphorical, or the unearned-generality gate should catch it.

## Open questions

- Is "polation distance" operationalizable as a review-time signal — e.g., a gate asking whether a note's claims are entailed by, extrapolated from, or off-manifold relative to its cited sources? That would make the bet doctrine checkable rather than declarative.
- Does autopolation earn a mention in the derivation definition (paraphrase/reformat as the degenerate case), or is that pedantry?
- Ord's flexible-vs-strict versions (fit exactly through data vs near it) may map onto quote-fidelity vs gloss in source handling — worth a look when the derivation definition is drafted.

---

Working links:

- [Ord, Interpolation/Extrapolation/Hyperpolation](../../sources/interpolation-extrapolation-hyperpolation.md) — derived-from: the source of the triple; abduction connection is his
- [discovery is seeing the particular as an instance of the general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — extends: supplies the polation axis as internal grading for the three depths
- [abstract an experience only when you can state the boundary](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — grounds: the boundary clause as declared extrapolation range
- [derivation-selection vocabulary](./derivation-selection-vocabulary.md) — produces: settles that thread's routing question toward extending discovery
- [methodology as inductive bias](./methodology-as-inductive-bias.md) — extends: promotion acquires the prior that cheapens future extrapolation
