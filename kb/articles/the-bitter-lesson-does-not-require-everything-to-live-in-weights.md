---
description: "Separates Sutton's search-and-learning claim from the weights-only interpretation, then tests learned prompts, skills, and harnesses against the scaling burden that remains"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md
  - kb/notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md
  - kb/notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md
  - kb/notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md
  - kb/notes/treat-continual-learning-as-representational-form-coevolution.md
  - kb/notes/parametric-reproduction-cannot-replace-an-authoritative-record.md
  - kb/notes/commitment-not-derivation-creates-new-ground-truth.md
  - kb/notes/oracle-accumulation-improves-the-selection-environment.md
  - kb/sources/sutton-the-bitter-lesson-original-essay.md
  - kb/sources/symbolic-learning-enables-self-evolving-agents.ingest.md
  - kb/sources/memento-skills-let-agents-design-agents.ingest.md
  - kb/sources/co-harness-co-evolving-harness-and-model-weights.ingest.md
---

# The Bitter Lesson does not require everything to live in weights

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

Imagine two agents running exactly the same system prompt. An engineer wrote the first prompt directly. An optimizer generated thousands of variants, evaluated them on held-out tasks, and retained the second. The two prompts have the same representational form: both are natural-language text. Their production methods are opposites.

Now reverse the example. Two systems contain the same array of numeric weights. One array was adjusted by hand to encode features chosen by its designer; gradient descent learned the other from data. Again the form is the same and the production methods differ. Any account of the Bitter Lesson that classifies the first pair together and the second pair together is tracking where knowledge is stored, not how it was produced.

Richard Sutton's [2019 essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) argues that methods built around human knowledge repeatedly lose to general methods that exploit increasing computation through search and learning. That historical claim is a serious challenge to hand-built prompts, skill libraries, agent harnesses, and knowledge bases. It is not, by itself, a requirement that everything learned must end up in model weights.

## Two axes, not one

Sutton's examples are chess, Go, speech recognition, and computer vision. In each case, researchers encoded what they understood about the domain: chess strategy, Go patterns, phonemes and vocal anatomy, edges and visual features. These methods helped, then plateaued. Search or learning eventually used growing computation to discover solutions that surpassed the supplied knowledge.

The decisive contrast is therefore between **production methods**. Who or what determines the behavior-shaping content? A human may specify it directly, or a computational process may search candidates, evaluate results, and retain what works.

A separate axis is [representational form](../notes/definitions/representational-form.md): how retained content is encoded and consumed. For agent systems, the main forms are natural-language artifacts such as prompts and instructions, symbolic artifacts such as programs and schemas, and distributed-parametric state such as model weights.

Crossing the two axes produces four possibilities:

| | Hand-crafted | Produced through search and learning |
|---|---|---|
| **Distributed-parametric** | Hand-tuned features and coefficients | Neural networks trained through gradient-based learning |
| **Natural-language or symbolic** | Hand-written prompts, tools, skills, rules, and schemas | Prompts, programs, skills, and harnesses selected through measured computational search |

The lower-right cell is the one a weights-only reading erases. Its existence is a conceptual possibility before it is an engineering success. A prompt does not remain hand-crafted forever because its first version came from a person; once measured search revises and selects it, that update belongs on the learned side. Conversely, putting a designer's chosen features into a numeric vector does not turn them into discoveries of a learning process.

This distinction rejects two positions at once. **Weights-only** says scalable learning is definitionally confined to distributed parameters. Sutton's argument does not establish that. **Hand-crafting forever** says readable artifacts should continue to be produced and maintained primarily through expert judgment. That position faces the Bitter Lesson directly. The compatible proposal is not to protect artifacts from learning, but to make them targets of learning too.

## The narrow rebuttal is not the empirical victory

Suppose an optimizer searches ten thousand deployment policies, runs each against a simulator and a regression suite, and installs the best surviving policy as readable text. The result remains a file, but it is no longer merely the designer's favored rule. Search proposed its content, evaluation rejected alternatives, and measured retention made one candidate operative.

That example is enough to defeat the categorical claim that readable artifacts are inherently incompatible with the Bitter Lesson. It does not show that the optimizer is economical, that its simulator captures production, or that the retained policy will generalize. The conceptual distinction settles where learning *may* operate. It does not settle whether learning over a particular artifact class works at scale.

The stronger empirical claim is much harder: as systems, corpora, and task horizons grow, learned localized artifacts can remain competitive with stronger models, parametric training, and simpler memory. That claim needs evidence about credit assignment, evaluator quality, inference and training compute, maintenance, retrieval, and human judgment. A two-axis diagram cannot supply it.

## Learning already reaches beyond weights

Current systems provide bounded examples of the lower-right cell.

[Agent Symbolic Learning](../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) models an agent pipeline as a network whose editable state includes prompts, tools, nodes, and their connections. Execution traces feed language-based feedback that is propagated across the network; separate operators revise prompts, tool code, and topology; worsening changes can be rolled back. This is a proof of concept of computational search over a mixed natural-language and symbolic harness with frozen model weights, shown in offline optimization rather than after deployment. Its "backpropagation" vocabulary is an analogy rather than a differentiable mechanism, its experiments do not isolate what each operator contributes, and the same prompted loss both produces updates and decides rollback, so a correlated evaluator error can admit a flattering change.

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) treats folders containing `SKILL.md`, prompts, and executable code as persistent evolving memory around a frozen language model. A router selects a skill; observed failure can trigger a rewrite, or repeated low utility a new skill; a generated unit test gates each mutation — a narrow check that can overfit the triggering example. With Gemini-3.1-Flash, the paper reports large gains over a read-write ablation that disables skill optimization, especially where later tasks revisit the same subject structure. It also reports the boundary: reuse is weaker on heterogeneous tasks, and its behavior-trained router is itself a learned parametric component. The system is mixed, not "learning without parameters" in every part.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) makes the mixture explicit. One loop repairs prompts, tools, skills, middleware, and memory from failed trajectories, accepting patches only after targeted improvement and held-out regression checks. The repaired harness generates verified trajectories for supervised fine-tuning; the updated model then exposes the next harness bottlenecks. The design intends behavior to migrate into weights while the harness remains independently revisable, but the reported evidence is three 30-problem competition-math sets, no ablation isolates the migration, and the gains cannot yet be assigned to coevolution rather than additional fine-tuning or harness search alone.

These examples establish that computation can optimize content in several forms. They do not yet establish that the methods scale like gradient-based learning. Their acceptance checks also differ in kind, not only in strength: Agent Symbolic Learning's rollback consults the same prompted loss that produced the update, Memento-Skills gates each mutation with one generated test, and only Co-Harness holds out a regression set. And each fixes important parts in advance: artifact types, routing, mutation operators, task interfaces, evaluators, and update schedules. The experiments test learning inside those decompositions, not whether the decompositions themselves are the right ones.

## Why weights dominate the comparison

Gradient descent does more than generate candidates. It comes with a general credit-assignment mechanism: the chain rule propagates an outcome signal through a differentiable parameter space. It may learn the wrong thing, require enormous data and compute, or distribute a fact so widely that no local edit can isolate it. But it supplies one repeatable answer to the question, "which parts should change after this error?"

A large artifact system has no comparable default. Imagine an agent deployment governed by 5,000 instructions, tests, schemas, tool definitions, and memory items. A failed release does not identify whether the cause was a retrieval rule, an outdated instruction, a bad tool contract, a missing test, or an interaction among them. Asking a model to "reflect and improve the repository" delegates the diagnosis; it does not solve credit assignment.

Readable-artifact systems offer partial substitutes. Explicit dependency links can bound which artifacts need rechecking. Retained execution traces can preserve evidence about where a failure arose. Tests and validators can reject some bad candidates. Localized retention is especially useful when a change affects a few well-matched units with a small downstream impact. None of these mechanisms yet composes into a general chain rule for heterogeneous artifacts.

This machinery gap explains why representational form and production method are often conflated. Parametric learning has a mature optimization loop, while artifact learning has promising fragments. The observed asymmetry is real. Treating it as a definition would turn today's engineering advantage into a permanent conceptual boundary.

## Some external state serves a different function

There is also a separate reason not to equate model capability with the whole system state. Consider the policy "production retries use exponential backoff." A model might reproduce that sentence perfectly from its weights. Reproduction does not establish that the policy is current, which service it governs, or who authorized it. A commitment becomes operational ground truth when an authorized process records and consumes it, not when a model can predict its text.

The same applies to API schemas, access-control rules, release approvals, and tests used as acceptance gates. Their job is partly epistemic—they contain knowledge—but also organizational: they declare current interfaces, allocate authority, or reject changes. Stronger models may generate and revise these artifacts, and some content may migrate into weights. The need for an authoritative current record does not disappear merely because the record can be reproduced parametrically.

This is not needed for the narrow rebuttal. Search over text is already enough to show that form and production method differ. It matters when the stronger claim becomes "all external state is temporary scaffolding." Some semantic guidance may indeed be absorbed. Current commitments and executable interfaces still need an operative carrier, whatever representation eventually supplies it.

## The scaling test remains open

The learned-artifact hypothesis should be stated so it can lose. Compare systems that search and retain localized artifacts against stronger-model, parametric-training, distillation, and simpler-memory baselines as corpus size, dependency density, task horizon, model capability, and available compute grow. Count not only task success but search cost, evaluator calls, retrieval failures, regressions, maintenance, and human decisions.

The hypothesis fails if artifact selection remains artisanal: if every new domain needs a human-designed ontology, if evaluators become more expensive than the work they protect, if failures cannot be assigned without repository-wide review, or if maintenance grows faster than the useful behavior it preserves. In that world, readable semantic artifacts may survive as interfaces and records while most learned competence moves into weights.

It succeeds in a more modest form if different representations remain efficient for different change patterns. Dense, diffuse adaptation may favor gradient-based updates. Sparse policy changes with explicit dependencies may favor local artifacts. Co-Harness illustrates the resulting architecture: external scaffolding can improve the trajectories used for training, selected behavior can be distilled into weights, and the harness can remain available for the next localized repair.

The Bitter Lesson therefore sets the research program rather than deciding its outcome. Do not protect human-authored knowledge from search. Build methods that can propose, test, retain, revise, and retire explicit structure—then compare them honestly with approaches that learn the same behavior elsewhere.

## Where to go next

The [production-method versus representational-form analysis](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) develops the full argument and its empirical burden. The [defense portfolio](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) separates this narrow rebuttal from adjacent claims about authority, scaffolding, and sample efficiency. For the practical learning loop, [the readable-artifact analysis](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) asks what would make cross-artifact credit assignment tractable.
