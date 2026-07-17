---
description: "Operational signals for when a component likely encodes a brittle proxy theory rather than an exact specification and should be relaxed instead of codified harder"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining]
---

# Operational signals that a component is a relaxing candidate

The [fixed-artifact distinction](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) says some codified components are exact-spec artifacts while others are proxy theories. That note offers confidence signals, but running systems need more operational tests for detecting proxy-theory components before full composition failure. The signals below shift confidence — they detect *badly-fitting* theories, not the theory/spec distinction itself, since a well-regularised learned component can pass all five early signals yet still encode a proxy theory.

## Signals that a component encodes theory, not specification

**Brittleness under paraphrase or reordering.** If the component breaks when inputs are rephrased, reordered, or padded with irrelevant content, it's relying on surface patterns rather than capturing the underlying structure. Metamorphic tests can detect this systematically. Rabanser et al.'s [agent reliability study](https://arxiv.org/pdf/2602.16666) operationalises a related signal as R_prompt — prompt robustness — and finds it is the key differentiator among robustness sub-dimensions: models handle genuine faults gracefully yet remain vulnerable to surface-level instruction rephrasings. [Ma et al.'s PromptSE framework](https://arxiv.org/pdf/2509.13680) provides a richer operationalisation: psychologically grounded emotion/personality templates at three calibrated perturbation distances (d=0.1 light lexical, d=0.2 moderate style, d=0.3 substantial transformation) across 14,760 variants and 14 models. Their finding that smaller models can achieve superior stability (Qwen-1.5B highest AUC-E) supports the interpretation that brittleness detects badly-fitting theories rather than capacity limitations. The [Mazur position-bias benchmark](../sources/position-bias.ingest.md) extends the brittleness signal to the LLM-as-judge layer: across 27 judges on 193 sibling-edit story pairs, the median judge flips its pairwise winner in 44.8% of decisive cases when display order alone is swapped — the signal measured on the evaluator, not the task-solver. None of these sources connect the brittleness signal to the fixed-artifact distinction, but we interpret the findings as evidence that paraphrase brittleness is a measurable and prevalent signal — exactly what you'd expect if many agent components encode theories about input format rather than specifications of meaning.

**Isolation-vs-integration gap.** The component performs well on unit tests but fails in integration. This was exactly the vision-features pattern: each feature (edge detection, corner detection) worked in isolation, but they didn't compose into "seeing." A growing gap between unit and integration performance is a relaxing signal. Note that composition failure has multiple causes — interface mismatches, protocol errors, environmental dependencies — so this signal is not conclusive on its own. It's strongest when the component's unit tests pass cleanly (ruling out implementation bugs) yet integration still degrades.

**Process constraints rather than outcome constraints.** The component encodes "always do steps A, B, C" rather than "output must satisfy property X." Process constraints are theories about how to achieve an outcome; outcome constraints are closer to specifications. The more process-heavy, the more likely it's a relaxing candidate.

**Hard to specify failure conditions.** If you can't articulate what a failure of this component would look like *before* seeing one, the spec is probably a theory. Arithmetic failures are obvious (wrong number); vision-feature failures are only obvious in retrospect.

**High sensitivity to distribution shift.** If the component works on training/development data but degrades on slightly different inputs, it has overfit to a particular theory of what inputs look like.

**Composition failure** (late-stage). The five signals above are early-detection — you can test for them before the system fails in production. Composition failure is the late-stage confirmation: individually sound components that don't compose into the target capability are the strongest evidence that their specs are theories, not definitions. This was the [vision researchers' experience](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — each feature worked alone, but the pieces didn't add up to "seeing." The distinction matters because composition failure is expensive to discover (you need to build and integrate) while the early signals are cheaper to test.

## Using the signals

These aren't binary tests. They're indicators that shift your confidence about where a component sits on the [oracle strength spectrum](./oracle-strength-spectrum.md).

When signals fire:
- Keep the component in a **replaceable slot** — clean interface, swappable implementation.
- Invest in **integration tests** over unit tests for this component.
- Maintain **alternative candidates** (different decompositions, learned replacements) so relaxing is cheap when the time comes.

When signals don't fire:
- The component is likely closer to exact-spec territory. Codify harder — [spec mining](./spec-mining-as-codification.md) provides the operational mechanism for extracting deterministic verifiers from observed behavior. More tests, stricter contracts, deterministic implementation where possible.

## Open questions

- Can these signals be measured automatically, or do they require human judgment? Brittleness and distribution sensitivity seem measurable; "hard to specify failure" seems inherently subjective.
- Is there a feedback loop? Investing in integration tests for suspected vision-features might *itself* reveal whether the theory is wrong, accelerating the relaxing decision.

---

Relevant Notes:

- [fixed artifacts split into exact specs and proxy theories](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — foundation: the exact-spec/proxy-theory distinction these signals operationalize
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — extends: signals shift confidence about where a component sits on the oracle strength gradient
- [spec-mining-as-codification](./spec-mining-as-codification.md) — complement: spec mining is the action when signals don't fire (codify harder); relaxing signals detect when to reverse it
- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operationalizes: these signals are the detection mechanism for the codify/relax cycle
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: unified calling makes acting on relaxing signals cheap — refactoring from codified to learned is a local operation
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: metamorphic checks are the operational mechanism for measuring the paraphrase brittleness signal automatically
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation.md) — exemplifies: disambiguation failure surfacing late is an instance of Signal 4 (hard to specify failure conditions)
- [memory-management-policy-is-learnable-but-oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: AgeMem confirms memory composition policy exhibits Signal 3 and Signal 4 in a concrete system
- [Rabanser et al. reliability study](https://arxiv.org/pdf/2602.16666) — evidence (interpreted): R_prompt metric shows paraphrase brittleness is the key differentiator among robustness sub-dimensions; we interpret this as support for the paraphrase brittleness signal, though the source doesn't connect to the fixed-artifact distinction
- [Ma et al. PromptSE framework](https://arxiv.org/pdf/2509.13680) — refines: richer operationalization of paraphrase brittleness via controlled emotion/personality templates at three perturbation distances; non-monotonic scaling (smaller models can be more stable) supports the interpretation that brittleness detects badly-fitting theories, not capacity limitations
- [Mazur position-bias benchmark](../sources/position-bias.ingest.md) — **evidence**: judge-layer measurement of the brittleness signal; order-swap alone shifts 27 LLMs' pairwise winners on 44.8% of decisive cases, and some models (Mistral Large 3) invert the direction rather than attenuate it — heterogeneity that matters for decorrelation (preprint-tier, sibling-edit surface)
- [Adaptation signals choose pressure; artifact analysis chooses the retained surface](./research/adaptation-agentic-ai-analysis.md) — extends: treats relaxing as one retained-surface move selected by adaptation evidence, alongside constraining and condensing
