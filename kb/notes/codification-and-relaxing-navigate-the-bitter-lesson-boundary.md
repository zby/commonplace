---
description: Since you can't identify which side of the bitter lesson boundary you're on until scale tests it, practical systems must codify and relax — with spec mining avoiding the vision-feature failure mode
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: current
---

# Codification and relaxing navigate the bitter lesson boundary

The [bitter lesson boundary](./bitter-lesson-boundary.md) separates arithmetic (spec is the problem) from vision features (spec is a theory about the problem). Since you can't reliably tell which regime you're in until scale tests the distinction, practical systems will always be hybrids — part codified, part learned.

## The trade-off depends on which regime you're in

[Codification](./codification.md) encodes knowledge into repo artifacts — tests, specs, conventions — each at a different grade of verifiability. Each codification step [trades generality for compound gains in reliability, speed, and cost](./constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md). But every such artifact also encodes a decomposition of some larger problem, and the arithmetic/vision-feature boundary determines whether that trade-off has a real cost:

- **Arithmetic-regime decompositions**: the spec fully captures the subproblem, so codification is pure gain — reliability+speed+cost improve and there's no generality loss, because the spec exhausts the problem space and the solution is algorithmically determined.
- **Vision-feature decompositions**: the spec is a plausible theory, so codification involves the real trade-off — you gain the compound but lose generality. When scale makes the general approach good enough on reliability+speed+cost, the generality loss isn't worth it anymore.

Codification therefore has a complement: **relaxing** — replacing a codified component with a learned or general-purpose one when scale makes that viable, accepting higher cost and lower reliability in exchange for regaining generality.

The trajectory runs in both directions, and can repeat at different levels of the stack. Edge detection was codified (hand-coded algorithms), relaxed (replaced by learned features), and may re-codify as an accelerator inside a learned architecture. FlashAttention is hand-crafted algorithmic optimization embedded within learned architectures; tokenizers are engineered preprocessing that learned models depend on. The bitter lesson describes a trajectory, not a law of nature.

## Every codification is a bet

Codification extracts a regularity and commits it to code. The bet is that what you extracted is genuinely part of the spec — load-bearing behavior that the system needs — rather than an accidental pattern that happens to hold on observed data.

In the arithmetic regime, the bet is safe: the spec IS the problem, and the solution is algorithmically determined. In the vision-feature regime, the bet is risky: the spec is a theory, and scale may reveal a better path. Most practical codification happens in the blurry zone between them, where you can't tell which regime you're in.

The vision researchers made this bet at maximum disadvantage. They formalized subproblems — edge detection, corner detection — without a working "seeing" system to extract from. They were betting that theorized components would compose into the target capability, with no evidence of successful composition.

[Spec mining](./spec-mining-as-codification.md) improves the odds by starting from a working system. You watch a system that already achieves the target behavior (however unreliably), identify regularities, and extract those into formal checks. The bet shifts from "will these pieces compose?" (which the vision researchers lost) to "is this specific pattern load-bearing?" — a narrower bet with better odds, because you've already observed the behavior composing successfully.

But it's still a bet. A mined spec might capture an accidental regularity — a pattern that holds on the observed data but isn't what makes the system work. [Relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) are how you detect a losing bet: distribution shift, paraphrase brittleness, and isolation-vs-integration gaps reveal when a codified component encodes an accident rather than a spec.

Two formal results help bound when codification bets are safe. The epiplexity framework ([Finzi et al., 2026](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md)) separates information into time-bounded entropy (irreducible randomness) and epiplexity (learnable structure within computational bounds). High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer's computational budget. Low-epiplexity patterns that appear regular may be accidents visible only at current scale.

The induction bias results ([Ebrahimi et al., 2026](../sources/induction-bias-sequence-models-ebrahimi-2026.md)) provide evidence from the other direction: for calculator-class state tracking, architectural induction bias (step-by-step decomposition) is a permanent advantage, not a temporary one that scale dissolves. Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats — they learn length-specific solutions in isolation, with training diversity actively hurting (κ = 0.28 for CoT). This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling.

## Working heuristics

1. **Codify for current leverage, not permanence.** A test that checks "does this function return the right number" is in the arithmetic regime. A convention that says "always decompose agents into these three phases" is probably a vision feature. Codify both — but expect the second kind to eventually relax.

2. **Prefer specs that describe what over how.** The more a codified artifact encodes a theory of how something works (rather than what it should produce), the more likely it is a relaxing candidate. "This endpoint returns X given Y" survives longer than "always process requests in three stages."

3. **Watch for composition failure as a relaxing signal.** If codified conventions don't compose into better systems, that's the signal to relax — replace the rigid decomposition with a learned one.

---

Sources:
- Finzi et al. (2026). [From entropy to epiplexity](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.md) — formal framework distinguishing learnable structure from observer-relative artefacts; grounds when codification targets real patterns.
- Ebrahimi et al. (2026). [On the "induction bias" in sequence models](../sources/induction-bias-sequence-models-ebrahimi-2026.md) — 190K training runs showing architectural induction bias is permanent for calculator-class tasks; codification bets in the arithmetic regime persist under scaling.

Relevant Notes:

- [the bitter lesson has a boundary](./bitter-lesson-boundary.md) — foundation: the arithmetic/vision-feature distinction this note operationalizes
- [deploy-time-learning](./deploy-time-learning-the-missing-middle.md) — codification's verifiability gradient
- [constraining and distillation both trade generality for reliability, speed, and cost](./constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) — the trade-off codification enacts
- [spec mining as codification](./spec-mining-as-codification.md) — the bottom-up extraction method that avoids the vision-feature failure mode
- [relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — detects when codified components are encoding vision features
