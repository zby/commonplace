---
description: Since you can't identify which side of the bitter lesson boundary you're on until scale tests it, practical systems must crystallise and soften — with spec mining avoiding the vision-feature failure mode
type: note
traits: []
areas: [learning-theory]
status: current
---

# Crystallisation and softening navigate the bitter lesson boundary

The [bitter lesson boundary](./bitter-lesson-boundary.md) separates arithmetic (spec is the problem) from vision features (spec is a theory about the problem). Since you can't reliably tell which regime you're in until scale tests the distinction, practical systems will always be hybrids — part crystallised, part learned. This note is about how to operate in that hybrid regime.

## Crystallisation and softening

[Crystallisation](./deploy-time-learning-the-missing-middle.md) encodes knowledge into repo artifacts — tests, specs, conventions — each at a different grade of verifiability. Each crystallisation step [trades generality for compound gains in reliability, speed, and cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). But every such artifact also encodes a decomposition of some larger problem, and the arithmetic/vision-feature boundary determines whether that trade-off has a real cost:

- **Arithmetic-regime decompositions**: the spec fully captures the subproblem, so crystallisation is pure gain — reliability+speed+cost improve and there's no generality loss, because the spec exhausts the problem space. There's nothing for a general method to discover.
- **Vision-feature decompositions**: the spec is a plausible theory, so crystallisation involves the real trade-off — you gain the compound but lose generality. When scale makes the general approach good enough on reliability+speed+cost, the generality loss isn't worth it anymore.

Crystallisation therefore has a complement: **softening**. Where crystallisation trades generality for the reliability+speed+cost compound, softening is the reverse: replacing a crystallised component with a learned or general-purpose one when scale makes that viable — accepting higher cost and lower reliability in exchange for regaining generality. The bitter lesson describes a trajectory, not a law of nature — and the trajectory runs in both directions. Edge detection was crystallised (hand-coded algorithms), softened (replaced by learned features), and may re-crystallise at a different level of the stack (as an accelerator inside a learned architecture). FlashAttention is hand-crafted algorithmic optimization inside learned architectures; tokenizers are engineered preprocessing that learned models depend on. Approaches that get bitter-lessoned away at one level sometimes reappear embedded within the general method at another.

## Crystallisation is not what failed with vision features

This raises an obvious objection: the vision researchers also formalized subproblems — and every one turned out to be a vision feature. If crystallisation is what we recommend, aren't we recommending the same move that failed?

The difference is whether you have a working whole to extract from. The vision researchers had formalizable problems but no working "seeing" system; they were assembling theorized components and hoping composition would deliver the target capability.

[Spec mining](./spec-mining-as-crystallisation.md) starts from the other end: a system that already achieves the target behavior, however unreliably. You watch it work, identify regularities, and extract those into formal checks. The critical advantage is that you're formalizing behavior you've already observed composing successfully — not hoping that independently formalized pieces will compose into something you've never seen work.

The risk shifts accordingly. The vision-feature failure mode was formalizing components that turned out not to compose into the target capability. The spec-mining risk is formalizing an accidental regularity — a pattern that holds on observed data but isn't load-bearing. These are different failure modes caught by different signals: composition failure reveals theorized components that don't add up; [distribution shift and paraphrase brittleness](./softening-signals.md) reveal accidental regularities.

## Working heuristics

1. **Crystallise for current leverage, not permanence.** A test that checks "does this function return the right number" is in the arithmetic regime. A convention that says "always decompose agents into these three phases" is probably a vision feature. Crystallise both — but expect the second kind to eventually soften.

2. **Prefer specs that describe what over how.** The more a crystallised artifact encodes a theory of how something works (rather than what it should produce), the more likely it is a softening candidate. "This endpoint returns X given Y" survives longer than "always process requests in three stages."

3. **Watch for composition failure as a softening signal.** If crystallised conventions don't compose into better systems, that's the signal to soften — replace the rigid decomposition with a learned one.

---

Relevant Notes:

- [the bitter lesson has a boundary](./bitter-lesson-boundary.md) — foundation: the arithmetic/vision-feature distinction this note operationalizes
- [deploy-time-learning](./deploy-time-learning-the-missing-middle.md) — crystallisation's verifiability gradient
- [stabilisation and distillation both trade generality for reliability, speed, and cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — the trade-off crystallisation enacts
- [spec mining as crystallisation](./spec-mining-as-crystallisation.md) — the bottom-up extraction method that avoids the vision-feature failure mode
- [softening signals](./softening-signals.md) — detects when crystallised components are encoding vision features

Topics:

- [learning-theory](./learning-theory.md)
