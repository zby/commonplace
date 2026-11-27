---
description: "Continual learning in model weights and in the systems around them: learning from use, retaining lessons across runs, and evaluating changes."
type: types/tag-readme.md
---

# continual-learning

Commonplace’s work on continual learning asks what a system learns from successive tasks or actual use, what changes, and how later work benefits. Start with [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) for the system-level case and [Sutton and Javed on why AI models stop learning](../sources/sutton-javed-why-ai-models-stop-learning.ingest.md) for the argument for continued weight learning.

Assign the tag when learning across experiences, or a mechanism or limit of that learning, is substantive. Deployment alone is not enough. [Improvement loop](./improvement-loop-README.md) focuses instead on how proposed changes are selected.

## Where learning lives in a deployed system

- [Retain reusable orchestration strategies](../theory/orchestration-strategies-and-run-state-have-opposite-persistence.md) — selected control logic persists as tested library code, while task-specific state stays temporary
- [A retained instruction preserves what testing selected](../theory/a-retained-instruction-preserves-what-testing-selected.md) — an instruction retains an empirically selected procedure outside model weights
- [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) — the framework claim: evaluated artifact changes persist outside weights
- [The deployed system, not the model alone, is the unit of learning](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — prompts, retrieval, tools, and runtime policy jointly set behavior, so model-only learning leaves them fixed
- [Constraining during deployment can produce learning outside weights](../theory/constraining-during-deployment-can-produce-learning-outside-weights.md) — narrowing interpretations through prompts, schemas, and tests is one form the accumulation takes
- [Instantiation alone cannot model agent learning across sessions](../theory/instantiation-alone-cannot-model-agent-learning-across-sessions.md) — the class/instance picture misses the update relation across sessions
- [Discarding all experience-dependent state prevents cross-run accumulation](../theory/ephemeral-computation-prevents-accumulation.md) — the failure condition: nothing learned survives when no experience-dependent state carries over
- [Factory learning is experience-responsive retention that improves the factory](../theory/factory-learning-is-experience-responsive-retention-that-improves.md) — the same mechanism applied to reusable production machinery

## Loops across representational forms

- [Treat continual learning as representational-form coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md) — parametric, natural-language, and symbolic forms each change; the question is how their loops relate
- [The readable-artifact loop is the tractable unit for continual learning](../theory/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — start with the natural-language-plus-symbolic pair, which shares context and a codification boundary
- [LLM-executed methodologies are metacircular interpreters, not compilers](../theory/llm-executed-methodologies-are-metacircular-interpreters.md) — rules are re-interpreted every session while stable paths codify into validators and commands
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../theory/moving-the-interpretation-enforcement-boundary-requires-coverage.md) — shifting a rule into code crosses forms, so governing it needs coverage of both and their mapping
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) — a formal-only loop relocates pre-formal work, it does not remove it

## Governing updates and their limits

- [Storing past incidents does not ensure their lessons guide later reviews](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) — the shared-source citation example separates finding a past incident from recognizing the same failure under new source names
- [Learning inside a fixed decomposition inherits its mistakes](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — optimization cannot repair distinctions outside the decomposition's update space
- [What gaps remain in our learning loop?](../theory/questions/what-gaps-remain-in-our-learning-loop.md) — open gaps between Commonplace's human-assisted selection-based learning loop and an autonomous fixed-weight loop

## The Bitter Lesson defense

- [The bitter lesson selects production methods, not representational forms](../theory/the-bitter-lesson-selects-production-methods-not-representational.md) — the lesson's axis is hand-crafted versus search-and-learning, so learned readable forms remain a coherent scaling bet
- [The bitter lesson selects against unearned reach, not against structure](../theory/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — what the lesson penalizes is asserted reach, not structure or origin
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — the condition on a hand-built starting state: scalable learning must displace what it supplies
- [The Bitter Lesson defense portfolio has one load-bearing member for the form-only rebuttal](../theory/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) — which defense actually carries weight, and why bootstrapping is only provisional

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — the case where the system changes its own organization.
- [Learning theory](./learning-theory-README.md) — the broader area.
- [Abstract an experience only when you can state where the lesson stops](../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) — deciding what to carry forward from an episode.
- [reflection](./reflection-README.md) — whether the retained changes are represented and selectively revisable
- [warranted-autonomy](./warranted-autonomy-README.md) — who may authorize the behavior-changing writes
- [improvement-loop](./improvement-loop-README.md) — candidate search, reject-capable evaluation, and retention; one update architecture, distinct from direct updates
- [software-factory](./software-factory-README.md) — shares the factory-learning note; continual learning applied to production machinery
- [theory-builder](./theory-builder-README.md) — learning through retained, criticized theory
