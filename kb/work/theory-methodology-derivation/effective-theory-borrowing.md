# Philosophy-of-science framing: effective theories

Candidate borrowing for the [philosophy-borrowing](../philosophy-borrowing/README.md) workshop, kept here until the mapping is judged operational rather than decorative.

## The claim

Physics' **effective theory** structure is the closest existing analogue to the [two-layer theory–methodology pattern](../../notes/theory-and-methodology-form-a-two-layer-execution-system.md). An effective theory — thermodynamics over statistical mechanics, ray optics over wave optics — is a generator–derivative pair designed for action: derivable from the deeper theory, dramatically cheaper to apply, strictly less general, with a *known* breakdown boundary where you drop back to the fundamental layer. Physics ships both layers permanently because the domain of application is open-ended — the source passage's claim 2 exactly.

Physics has no single word for the relation; it has a term cluster, each naming one aspect, and the cluster maps piecewise onto the pattern's moving parts:

| Physics term | Names | Maps to |
|---|---|---|
| integrating out / coarse-graining | the derivation direction: discard degrees of freedom that don't matter at the use scale | the derivation step (lossy, purpose-directed, regime-of-use-driven) |
| **matching** | fix the effective theory's constants by computing the same quantity in both theories at the validity boundary and requiring agreement | the **promotion** step: compute once in the general layer, commit into the fast layer, never recompute |
| cutoff (Λ) | the scale beyond which the effective theory is known invalid — carried *as part of the theory* | the methodology's declared breakdown boundary (stated, not discovered by failure) |
| correspondence principle | any new general theory must recover the established effective theory in its limit | the regression relation: revised theory must reproduce the methodology on its home turf |
| UV completion | given a working effective theory, find the deeper theory that generates it | theory reconstructed after practice — the spec-mining direction, where the methodology exists first |

Philosophy side: Nancy Cartwright (*How the Laws of Physics Lie*) is the philosophical treatment — phenomenological laws are the true-of-practice, usable layer; fundamental theory buys reach at the price of direct applicability. The umbrella term is **intertheoretic reduction**, with a directional wrinkle: Nagel-style derivational reduction vs limiting-case reduction run in opposite directions (Nickles 1973 split them). Robert Batterman (*The Devil in the Details*) argues the limiting relation is often *singular* — the effective theory contains organizing concepts that don't smoothly derive from the fundamental one. For methodologies: some content is genuinely not derivable from the theory, which makes real methodologies mixed artifacts (see the caveat in the structure thread).

Secondary analogues for the *dynamics*: Kuhn's exemplars (normal science as pattern-matching against a solved-problem library; promotion grows the library) and Lakatos's research programmes (growth at the boundary under anomaly pressure — looser fit, since his protective belt shields the core rather than serving its application).

## The adoption bar

Per the philosophy-borrowing workshop's criteria, the borrowing must change a concrete KB operation. Candidate operational content — a checklist for derived-methodology artifacts:

1. Does the methodology declare its cutoff (a stated validity boundary, rather than breakdown discovered by failure)?
2. Is fallback to the generator an expected, documented operation rather than an error path?
3. Is there a matching procedure — how a corner-case derivation gets verified against the theory and committed into the methodology?
4. Is the correspondence direction enforced — when the theory is revised, is the methodology re-checked on its home turf?

If these become a review criterion or a type-spec section for methodology-shaped artifacts, the borrowing is operational. If they stay a nice analogy in one note, it is decorative and should be cited-in-passing only.

## Open questions

- Promote to the philosophy-borrowing candidate list now, or only after the structure note exists to anchor it?
- Is "matching" worth borrowing as a KB term (the promotion-with-verification step), or does it collide with too many software senses of the word?
- The Batterman point may deserve independent treatment: it is the strongest argument that derivation is graded and methodologies are mixed artifacts — which feeds the [vocabulary thread](./derivation-selection-vocabulary.md) directly.

---

Working links:

- [philosophy-borrowing workshop](../philosophy-borrowing/README.md) — produces: this thread is a candidate for its list, subject to the same adoption bar
- [spec mining as codification](../../notes/spec-mining-as-codification.md) — see-also: UV completion is the physics name for its direction (practice first, theory reconstructed)
- [first-principles reasoning selects for explanatory reach](../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: existing Deutsch borrowing this analogue composes with
