---
description: "Curated head for the continual-learning tag — how a deployed AI system keeps learning outside model weights through retained prompts, rules, tools, and tests, and why that fits the Bitter Lesson"
type: types/tag-readme.md
complete: true
---

# continual-learning

Notes on the mechanisms by which a deployed system keeps learning after release without retraining model weights: retaining evaluated changes to prompts, rules, tools, schemas, and tests, and governing those behavior-changing writes. Two notes establish the tag: [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and [The readable-artifact loop is the tractable unit for continual learning](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md). Bitter Lesson notes defend the bet that learning in readable forms can scale. It is a child of [self-improving-systems](./self-improving-systems-README.md). Boundary: [deploy-time-learning](./deploy-time-learning-README.md) is the phenomenon, that deployment reveals what design could not; this tag holds the mechanisms that answer it.

## Where learning lives in a deployed system

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — the framework claim: evaluated artifact changes persist outside weights
- [The deployed system, not the model alone, is the unit of learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — prompts, retrieval, tools, and runtime policy jointly set behavior, so model-only learning leaves them fixed
- [Constraining during deployment is continuous learning](../notes/constraining-during-deployment-is-continuous-learning.md) — narrowing interpretations through prompts, schemas, and tests is one form the accumulation takes
- [Instantiation alone cannot model agent learning across sessions](../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) — the class/instance picture misses the update relation across sessions
- [Discarding all experience-dependent state prevents cross-run accumulation](../notes/ephemeral-computation-prevents-accumulation.md) — the failure condition: nothing learned survives when no experience-dependent state carries over
- [Factory learning is experience-responsive retention that improves the factory](../notes/factory-learning-is-experience-responsive-retention-that-improves.md) — the same mechanism applied to reusable production machinery

## Loops across representational forms

- [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md) — parametric, natural-language, and symbolic forms each change; the question is how their loops relate
- [The readable-artifact loop is the tractable unit for continual learning](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — start with the natural-language-plus-symbolic pair, which shares context and a codification boundary
- [LLM-executed methodologies are metacircular interpreters, not compilers](../notes/llm-executed-methodologies-are-metacircular-interpreters.md) — rules are re-interpreted every session while stable paths codify into validators and commands
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) — shifting a rule into code crosses forms, so governing it needs coverage of both and their mapping
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) — a formal-only loop relocates pre-formal work, it does not remove it

## Governing updates and their limits

- [Continual learning requires governing behaviour-changing writes, not just storing content](../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — persistence is not enough: updates must be selected, validated, authorized, and coordinated
- [Learning inside a fixed decomposition inherits its mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — optimization cannot repair distinctions outside the decomposition's update space
- [An optimal long-run learning strategy invests in its own machinery](../notes/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md) — a machinery improvement is reused by every later episode, so it can out-earn immediate learning
- [Automating KB learning is an open problem](../notes/automating-kb-learning-is-an-open-problem.md) — the KB learns through manual improvement; automating judgment-heavy mutations lacks oracles

## The Bitter Lesson defense

- [The bitter lesson selects production methods, not representational forms](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) — the lesson's axis is hand-crafted versus search-and-learning, so learned readable forms remain a coherent scaling bet
- [The bitter lesson selects against unearned reach, not against structure](../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) — what the lesson penalizes is asserted reach, not structure or origin
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) — the condition on a hand-built starting state: scalable learning must displace what it supplies
- [The Bitter Lesson defense portfolio has one load-bearing member for the form-only rebuttal](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) — which defense actually carries weight, and why bootstrapping is only provisional

## Related Tags

- [self-improving-systems](./self-improving-systems-README.md) — the parent; continual learning is the deployed-system case of self-improvement
- [deploy-time-learning](./deploy-time-learning-README.md) — the phenomenon these mechanisms answer; several members carry both tags
- [learning-theory](./learning-theory-README.md) — the general account of learning these notes apply
- [reflection](./reflection-README.md) — whether the retained changes are represented and selectively revisable
- [warranted-autonomy](./warranted-autonomy-README.md) — who may authorize the behavior-changing writes
- [improvement-loop](./improvement-loop-README.md) — the search, evaluation, and retention loop each form's learning runs through
- [software-factory](./software-factory-README.md) — shares the factory-learning note; continual learning applied to production machinery
- [theory-builder](./theory-builder-README.md) — learning through retained, criticized theory
