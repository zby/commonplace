---
description: Since you can't identify which side of the bitter lesson boundary you're on until scale tests it, practical systems must crystallise and soften — with spec mining avoiding the vision-feature failure mode
type: note
traits: []
areas: [learning-theory]
status: current
---

# Crystallisation and softening navigate the bitter lesson boundary

The [bitter lesson boundary](./bitter-lesson-boundary.md) separates arithmetic (spec is the problem) from vision features (spec is a theory about the problem). Since you can't reliably tell which regime you're in until scale tests the distinction, practical systems will always be hybrids — part crystallised, part learned.

## The trade-off depends on which regime you're in

[Crystallisation](./deploy-time-learning-the-missing-middle.md) encodes knowledge into repo artifacts — tests, specs, conventions — each at a different grade of verifiability. Each crystallisation step [trades generality for compound gains in reliability, speed, and cost](./stabilisation-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). But every such artifact also encodes a decomposition of some larger problem, and the arithmetic/vision-feature boundary determines whether that trade-off has a real cost:

- **Arithmetic-regime decompositions**: the spec fully captures the subproblem, so crystallisation is pure gain — reliability+speed+cost improve and there's no generality loss, because the spec exhausts the problem space and the solution is algorithmically determined.
- **Vision-feature decompositions**: the spec is a plausible theory, so crystallisation involves the real trade-off — you gain the compound but lose generality. When scale makes the general approach good enough on reliability+speed+cost, the generality loss isn't worth it anymore.

Crystallisation therefore has a complement: **softening** — replacing a crystallised component with a learned or general-purpose one when scale makes that viable, accepting higher cost and lower reliability in exchange for regaining generality.

The trajectory runs in both directions, and can repeat at different levels of the stack. Edge detection was crystallised (hand-coded algorithms), softened (replaced by learned features), and may re-crystallise as an accelerator inside a learned architecture. FlashAttention is hand-crafted algorithmic optimization embedded within learned architectures; tokenizers are engineered preprocessing that learned models depend on. The bitter lesson describes a trajectory, not a law of nature.

## Every crystallisation is a bet

Crystallisation extracts a regularity and commits it to code. The bet is that what you extracted is genuinely part of the spec — load-bearing behavior that the system needs — rather than an accidental pattern that happens to hold on observed data.

In the arithmetic regime, the bet is safe: the spec IS the problem, and the solution is algorithmically determined. In the vision-feature regime, the bet is risky: the spec is a theory, and scale may reveal a better path. Most practical crystallisation happens in the blurry zone between them, where you can't tell which regime you're in.

The vision researchers made this bet at maximum disadvantage. They formalized subproblems — edge detection, corner detection — without a working "seeing" system to extract from. They were betting that theorized components would compose into the target capability, with no evidence of successful composition.

[Spec mining](./spec-mining-as-crystallisation.md) improves the odds by starting from a working system. You watch a system that already achieves the target behavior (however unreliably), identify regularities, and extract those into formal checks. The bet shifts from "will these pieces compose?" (which the vision researchers lost) to "is this specific pattern load-bearing?" — a narrower bet with better odds, because you've already observed the behavior composing successfully.

But it's still a bet. A mined spec might capture an accidental regularity — a pattern that holds on the observed data but isn't what makes the system work. [Softening signals](./softening-signals.md) are how you detect a losing bet: distribution shift, paraphrase brittleness, and isolation-vs-integration gaps reveal when a crystallised component encodes an accident rather than a spec.

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
