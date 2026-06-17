---
description: "Review and critique systems need independent process-validity checks because a model can substitute answer reconstruction for reasoning evaluation"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [evaluation, llm-interpretation-errors]
status: seedling
---

# Reasoning production is not reasoning evaluation

A model that can produce a good answer is not thereby a good evaluator of the reasoning that led to an answer. Production asks "can I get there?" Evaluation asks "does this path get there validly?" Those are different capabilities, and a review system that collapses them risks accepting fluent but invalid reasoning whenever the conclusion looks right.

The VAIR paper makes the failure concrete: large reasoning models often evaluate a submitted math solution by independently solving the problem, confirming that the final answer matches, and then overlooking or rationalizing invalid steps in the submitted reasoning. The important abstraction is not "models are bad at grading math." It is that answer agreement can act like a misleading soft oracle: cheap, tempting, and high-performing on ordinary controls, but non-discriminating when answer validity and reasoning validity are deliberately separated.

This directly affects review and critique systems. If a semantic review gate asks an agent whether a note's argument works, the agent may reconstruct a plausible argument for the same conclusion rather than check whether the note's stated evidence actually entails that conclusion. If a critique pass asks for weaknesses, the agent may judge the destination claim instead of the route. If a fix review asks whether a revision preserved meaning, the agent may compare reconstructed gist rather than trace commitments, caveats, and evidence.

So review prompts need to force route inspection, not just destination agreement. A useful critique should ask:

- What claims does the artifact actually make?
- What evidence or premises does it actually cite?
- Which inference steps connect the premises to the conclusion?
- Which step would fail if the conclusion were unknown?
- Would the review verdict change if the same conclusion appeared with a different reasoning path?

This is the process-validity version of [process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md): output correctness and reasoning-path correctness must be tested separately. It also sharpens [the augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), because a reviewer that mostly accepts correct-looking conclusions may have high aggregate accuracy while lacking per-instance discrimination over invalid arguments.

For Commonplace, the consequence is not "stop using LLM review." It is that review should be treated as a soft oracle that needs adversarial structure, calibration, and human authority. [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation.md), but only if the semantic review is actually checking content-level entailment rather than answer agreement. [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](./adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) already makes the human judge load-bearing; this note adds a specific failure mode for the agent side of that loop.

The practical test for a review gate is whether it can catch a valid-conclusion-invalid-reasoning artifact. A gate that cannot distinguish "the conclusion is true" from "this artifact proves the conclusion" should not be trusted as an independent verifier of reasoning quality.

The existing [composition friction gate](../instructions/composition-friction-gate.md) is the closest operational witness: it refuses an overall green-check verdict and instead asks a fresh adversarial agent to enumerate load-bearing inferential joints and mark weak support. That shape should inform semantic review gates that claim to assess reasoning quality.

## Open Questions

- Which existing Commonplace review gates are vulnerable to conclusion-agreement substitution?
- Can we build a small VAIR-style regression set for notes: true claims supported by deliberately invalid or incomplete reasoning?
- Should semantic review prompts explicitly require a premise-to-conclusion trace before returning a verdict?

---

Relevant Notes:

- [An Enigma of Artificial Reason ingest](../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) — derived-from: source report for the VAIR paper and answer-confirmation-bias mechanism
- [The augmentation-automation boundary is discrimination not accuracy](./the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — grounds: explains why high apparent correctness is insufficient when the verifier lacks per-instance discrimination
- [Process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md) — grounds: separates checking the result from checking the reasoning path
- [Semantic review catches content errors that structural validation cannot](./semantic-review-catches-content-errors-that-structural-validation.md) — applies: semantic review must inspect entailment, not only plausible conclusion agreement
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](./adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) — extends: adds a concrete evaluator failure mode the adversarial loop must guard against
- [Quality signals for KB evaluation](./quality-signals-for-kb-evaluation.md) — extends: conclusion-agreement substitution is a calibration risk for LLM critique signals
- [Composition friction gate](../instructions/composition-friction-gate.md) — see-also: existing report-only instruction that checks inferential joints instead of emitting a fluent self-grade
- [Grounding alignment gate](../instructions/review-gates/semantic/grounding-alignment.md) — see-also: existing semantic review gate whose "does the conclusion follow" test is the right surface to harden against conclusion-agreement substitution
