---
description: Since you can't identify which side of the bitter lesson boundary you're on until scale tests it, practical systems must codify and relax — with spec mining avoiding the vision-feature failure mode
type: types/note.md
traits: [has-external-sources]
tags: [learning-theory, constraining, continual-learning, self-improving-systems]
---

# Codification and relaxing navigate the bitter lesson boundary

The [fixed-artifact distinction](./exact-implementation-does-not-validate-a-requirement.md) separates exact specs (the spec is the problem) from proxy theories (the spec is a theory about a larger capability). Since you can't reliably tell which regime you're in until scale tests the distinction, practical systems will always be hybrids — combining explicit scripts and checks with learned components. This is not a partition into codified versus learned: an adopted model package can itself be a codified reference.

## The trade-off depends on which regime you're in

[Codification](./definitions/codification.md) moves a rule or operation into symbolic form by rewriting it or adopting a governing reference. This note concerns the code-extraction case: committing an interpreted rule to a script, executable test, schema, or validator whose behavior can be inspected and checked at acceptable cost. Retaining a prose convention alone is not codification. Adopting a model package can codify an operation without providing this case's readable rules or reducing inference cost.

Code extraction can [trade generality for gains in reliability, speed, and cost](./constraining-and-extraction-both-trade-generality-for-reliability.md) when the committed procedure fits and its execution and maintenance are cheaper than repeated interpretation. But such a procedure can also encode a decomposition of a larger problem, and the arithmetic/vision-feature boundary determines what capability the commitment risks excluding:

- **Arithmetic-regime decompositions**: the spec fully captures the subproblem, so implementing it need not lose generality within that declared scope. An inspectable script or validator can improve reliability, speed, and cost without excluding required behavior; the economic gain still depends on implementation and maintenance costs.
- **Vision-feature decompositions**: the spec is a plausible theory of a larger capability, so an efficient local implementation can lose generality at that larger scope. When scale makes the general approach good enough on reliability, speed, and cost, that loss may no longer be worth it.

Code extraction therefore has a complement: **relaxing** — replacing an extracted component with a more general one, often a model call, when scale makes that viable, accepting higher cost and lower reliability in exchange for regaining generality. The replacement can itself be codified by adoption; what relaxing reverses is the extraction, not symbolic membership.

The trajectory runs in both directions, and can repeat at different levels of the stack. Edge detection was codified (hand-coded algorithms), relaxed (replaced by learned features), and may re-codify as an accelerator inside a learned architecture. FlashAttention is hand-crafted algorithmic optimization embedded within learned architectures; tokenizers are engineered preprocessing that learned models depend on. The bitter lesson describes a trajectory, not a law of nature.

## Every code-extraction codification is a bet

In this case codification extracts a regularity and commits it to code. The bet is that what you extracted is genuinely part of the spec — load-bearing behavior that the system needs — rather than an accidental pattern that happens to hold on observed data. That is the same property [one case-level conjecture offers as the diagnosis of a structured method's loss under scaling](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md), seen from the author's side rather than the survivor's: a codification that commits an accident asserts a scope that nothing assessed, and relaxing is what happens to it later. That scale in fact selects on this property is conjectural, not established.

In the arithmetic regime, the bet is safe: the spec IS the problem, and the solution is algorithmically determined. In the vision-feature regime, the bet is risky: the spec is a theory, and scale may reveal a better path. Most practical codification happens in the blurry zone between them, where you can't tell which regime you're in.

The vision researchers made this bet at maximum disadvantage. They formalized subproblems — edge detection, corner detection — without a working "seeing" system to extract from. They were betting that theorized components would compose into the target capability, with no evidence of successful composition.

[Spec mining](./spec-mining-as-codification.md) improves the odds by starting from a working system. You watch a system that already achieves the target behavior (however unreliably), identify regularities, and extract those into formal checks. The bet shifts from "will these pieces compose?" (which the vision researchers lost) to "is this specific pattern load-bearing?" — a narrower bet with better odds, because you've already observed the behavior composing successfully.

But it's still a bet. A mined spec might capture an accidental regularity — a pattern that holds on the observed data but isn't what makes the system work. [Relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) are how you detect a losing bet: distribution shift, paraphrase brittleness, and isolation-vs-integration gaps reveal when a codified component encodes an accident rather than a spec.

Two formal results help bound when codification bets are safe. The epiplexity framework ([Finzi et al., 2026](https://arxiv.org/html/2601.03220v1)) separates information into time-bounded entropy (irreducible randomness) and epiplexity (learnable structure within computational bounds). High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer's computational budget. Low-epiplexity patterns that appear regular may be accidents visible only at current scale.

The induction bias results ([Ebrahimi et al., 2026](https://arxiv.org/pdf/2602.18333)) provide evidence from the other direction: for calculator-class state tracking, architectural induction bias (step-by-step decomposition) is a permanent advantage, not a temporary one that scale dissolves. Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats — they learn length-specific solutions in isolation, with training diversity actively hurting (κ = 0.28 for CoT). This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling.

## Working heuristics

1. **Codify for current leverage, not permanence.** An executable test that checks "does this function return the right number" is in the arithmetic regime relative to that numerical contract. A workflow that enforces "always decompose agents into these three phases" is probably a vision feature relative to broader task success. Both can be codified — but expect the second kind to eventually relax. Merely writing the convention in natural language constrains without codifying it.

2. **Prefer specs that describe what over how.** The more a codified artifact encodes a theory of how something works (rather than what it should produce), the more likely it is a relaxing candidate. "This endpoint returns X given Y" survives longer than "always process requests in three stages."

3. **Watch for composition failure as a relaxing signal.** If codified conventions don't compose into better systems, that's the signal to relax — replace the rigid decomposition with a more general one.

---

Sources:
- Finzi et al. (2026). [From entropy to epiplexity](https://arxiv.org/html/2601.03220v1) — formal framework distinguishing learnable structure from observer-relative artefacts; grounds when codification targets real patterns.
- Ebrahimi et al. (2026). [On the "induction bias" in sequence models](https://arxiv.org/pdf/2602.18333) — 190K training runs showing architectural induction bias is permanent for calculator-class tasks; codification bets in the arithmetic regime persist under scaling.

Relevant Notes:

- [Unsupported proxy scope may explain a structured method's loss under scaling](./bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — grounds: the case-level diagnosis this note reads from the author's side; it conjectures what may determine the outcome without establishing it or restoring the foresight this note denies
- [fixed artifacts split into exact specs and proxy theories](./exact-implementation-does-not-validate-a-requirement.md) — foundation: the exact-spec/proxy-theory distinction this note operationalizes
- [the verifiability gradient](./verifiability-gradient.md) — grounds: available checks guide whether to extract a rule into a script or validator
- [constraining and extraction can trade generality for reliability, speed, or cost](./constraining-and-extraction-both-trade-generality-for-reliability.md) — grounds: the trade-off code-extraction codification can enact
- [spec mining as codification](./spec-mining-as-codification.md) — the bottom-up extraction method that avoids the vision-feature failure mode
- [relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — detects when codified components are encoding vision features
