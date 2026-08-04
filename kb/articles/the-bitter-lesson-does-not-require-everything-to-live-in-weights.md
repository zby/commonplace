---
description: "Separates Sutton's search-and-learning claim from a weights-only extrapolation, then identifies scalable credit assignment, reliable evaluation, and controlled decomposition revision as central challenges for learned artifacts"
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
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
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

Imagine two agents whose policies are system prompts. An engineer wrote the first prompt directly. An optimizer produced the second: it generated thousands of variants, evaluated them on held-out tasks, and kept the best. Both prompts are natural-language text. They have the same representational form but different production methods.

Now reverse the example. Two systems use the same parameterized controller architecture but different dense coefficient vectors. An expert sets one vector directly; gradient descent learns the other from data. Here too, the representational form is the same but the production method differs. An account that groups the two prompts together and the two controllers together, while separating prompts from controllers, is tracking representational form rather than production method.

Richard Sutton's [2019 essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) argues that methods built around human knowledge repeatedly lose to general methods that exploit increasing computation through search and learning. That historical claim is a serious challenge to directly specified prompts, skill libraries, agent harnesses, and knowledge bases.

The Bitter Lesson is not a weights-only theorem. The target here is a weights-only extrapolation from Sutton, not Sutton's argument itself. His argument puts directly specified domain knowledge under a scaling test: it must compete with methods that exploit more computation through search and learning. It does not determine whether the content those methods select should be retained in weights or in natural-language or symbolic artifacts.

Representation still changes the optimization problem. Artifact learning must assign credit, reject harmful updates, and keep its decomposition—the artifact types and rules that link, update, and evaluate them—adequate or safely revisable. A mixed system is one possible outcome, not a conclusion of the two-axis distinction.

## Two axes, not one

Across chess, Go, speech recognition, and computer vision, Sutton's pattern is that directly encoded domain knowledge helped, then plateaued as search and learning exploited more computation.

The relevant distinction is therefore how content is produced. Designers can specify it directly, or a search or learning procedure can select it using evidence and additional computation. Classify individual components and updates rather than whole artifacts. A prompt can combine directly written wording with search-selected revisions while designers still specify the surrounding schema, evaluator, candidate generator, and acceptance rule.

A separate axis is [representational form](../notes/definitions/representational-form.md): natural-language and symbolic artifacts usually expose identifiable content-bearing units, while content in model weights is usually distributed across dense numerical state. For this comparison, grouping the first two as localized yields four combinations:

| | Directly specified | Selected through search or learning |
|---|---|---|
| **Distributed-parametric** | Dense parameter values set directly by experts | Parameters fitted to data through gradient-based learning |
| **Localized (natural-language or symbolic)** | Designer-written prompts, feature extractors, tools, skills, rules, and schemas | Prompts, programs, skills, and harnesses selected through measured computational search |

The axes interact: representational form changes search, credit assignment, dependency checking, and retention costs.

## What this proves—and what it does not

The lower-right cell is the one a weights-only reading erases. Suppose an optimizer searches ten thousand candidate deployment policies, tests them in a simulator and regression suite, and installs the best survivor as a natural-language file. The result is still localized, but search rather than the designer selected its behavior-shaping content.

That production history defeats the categorical claim that localized artifacts are inherently incompatible with the Bitter Lesson. It does not show that the optimizer is economical, that its simulator captures production, or that the retained policy will generalize. Sutton's argument therefore does not confine scalable learning to weights. But localized domain structure offered as a source of generalizable competence still faces his scaling test; it cannot remain exempt from search and learning merely because experts produced it. The compatible proposal is not to protect such structure from learning, but to make the artifacts that carry it targets of learning too.

The remaining question is empirical: can learned localized artifacts compete on performance and total cost as systems, corpora, and task horizons grow? The answer depends on credit assignment, evaluation, maintenance, retrieval, and safe revision of the update space.

## The machinery gap inside fixed decompositions

Within a fixed differentiable computation graph, data path, and objective, backpropagation calculates loss gradients for trainable parameters, and gradient descent turns them into updates. The process may still optimize the wrong objective, exploit spurious features, require enormous resources, or distribute a fact too widely for local editing. It does not by itself establish that the architecture, loss, decomposition, or data are appropriate.

A large artifact system has no comparable default. Imagine an agent deployment governed by 5,000 instructions, tests, schemas, tool definitions, and memory items. A failed release does not identify whether the cause was a retrieval rule, an outdated instruction, a bad tool contract, a missing test, or an interaction among them. Asking a model to "reflect and improve the repository" delegates the diagnosis; it does not solve credit assignment.

Localized artifact systems offer partial substitutes. Explicit dependency links can limit which artifacts need rechecking. Recorded execution traces preserve evidence about where a failure arose. Tests and validators can reject some bad candidates. [Localized retention helps most](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) when an update changes a few well-matched units and affects few others. The systems examined here do not show these mechanisms composing into a general update rule for heterogeneous artifacts.

[Artifact learning also inherits its chosen decomposition](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): designers may still fix artifact types, routing, mutation operators, evaluators, and schedules. Success inside that space can show that the whole system sufficed in the tested setting, but not that the supplied choices were necessary or preferable to excluded alternatives. A consequential choice needs an independent warrant or a safe revision path. Changing artifact boundaries can also change the units of attribution, validation, and rollback.

This asymmetry can make parametric learning look synonymous with learning. It is an engineering gap, not a definition.

## What current systems learn—and leave fixed

Bounded instances of the learned-localized cell already exist. The three systems below should be read through three questions: what can change, what accepts an update, and what enclosing structure remains directly specified.

[Agent Symbolic Learning](../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) models an agent pipeline as a network whose editable state includes prompts, tools, nodes, and their connections. Execution traces produce language-based feedback that is propagated backward through the network. Separate operators revise prompts, tool code, and topology; worsening changes can be rolled back. This is an offline proof of concept for search over a mixed natural-language and symbolic harness with frozen model weights. Its "backpropagation" vocabulary is an analogy, and its experiments do not isolate what each operator contributes.

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) treats folders containing `SKILL.md`, prompts, and executable code as persistent, evolving memory around a frozen language model. A router selects a skill. An observed failure can trigger a rewrite; repeated low utility can trigger a new skill. With Gemini-3.1-Flash, the paper reports large gains over a read-write ablation that disables skill optimization. The gains are strongest where later tasks revisit the same subject structure; reuse is weaker on heterogeneous tasks. The language model remains frozen, but the behavior-trained router is parametric, so the whole system is mixed.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) makes the mixture explicit. Its harness loop repairs prompts, tools, skills, middleware, and memory from failed trajectories. The repaired harness generates verified trajectories for supervised fine-tuning; the updated model then exposes the next harness bottlenecks. The design aims to move some behavior into weights while keeping the harness independently revisable. Its dual-loop evidence is limited to three 30-problem competition-math sets. A separate 200-hour study covers harness evolution without weight updates. No matched ablation isolates the migration, so the gains cannot yet be assigned to coevolution rather than additional fine-tuning or harness search alone.

Their update gates and enclosing structures make the comparison clearer:

| System | How updates are accepted | Important structure left directly specified |
|---|---|---|
| Agent Symbolic Learning | The same prompt-based loss seeds feedback and scores the rerun; rollback follows if the score worsens | Node and trajectory model, optimizer families, loss and feedback prompts, edit language |
| Memento-Skills | One generated test runs through the updated skill and is scored by the judge; failure triggers rollback | Skill-folder contract, single-skill attribution, router design, utility rule, test gate |
| Co-Harness | A patch must improve targeted failures without regressing on held-out behavior; weight updates use filtered training trajectories | Five-part harness division, failure taxonomy, local-diff protocol, alternating schedule |

All three revise substantial structure inside directly specified update spaces. Their results do not test whether excluded decompositions would perform better or how to revise those boundaries safely.

## The scaling test remains open

To make the learned-artifact hypothesis falsifiable, compare systems that search for and retain localized artifacts with matched systems that invest comparable compute and human effort in stronger models, parametric training, distillation, or simpler memory. Scale the corpus, dependency density, task horizon, model capability, and compute budget. Measure not only task success but also search cost, evaluator calls, retrieval failures, regressions, maintenance work, and human decisions.

The hypothesis loses its scaling case if, relative to those baselines, its human-design, evaluation, or maintenance burden grows faster than the useful behavior it preserves. Warning signs include a bespoke ontology for every new domain, evaluation costs that exceed the costs of the failures they avert, or failures that require repository-wide review to diagnose. In that case, localized artifacts may survive as interfaces and records while most learned competence moves into weights.

The hypothesis succeeds in a modest form if representations divide work efficiently: dense, diffuse adaptation may favor gradients, while sparse changes may favor localized artifacts whose units match the change and whose dependency closure remains small. Co-Harness is an early example of this division.

A mixed system still faces the decomposition burden: its units must keep attribution and revalidation tractable or themselves be safely revisable. Otherwise it has only moved the scaling problem.

## Authority is a separate issue

Some artifacts record commitments, not merely knowledge. A model might reproduce a policy from its weights, but [reproduction does not establish authority](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): it does not show that the policy is current, where it applies, or who approved it. Models may generate or revise authoritative records, but accurate reproduction cannot replace the record the system actually uses.

## The research program

The main scaling question remains empirical. The Bitter Lesson therefore sets the research program rather than deciding its outcome. Do not protect human-authored knowledge from search. Build methods that can propose, test, retain, revise, and retire explicit structure—then compare them honestly with approaches that learn the same behavior elsewhere.

## Where to go next

The [production-method versus representational-form analysis](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) develops the full argument and its empirical burden. The [fixed-decomposition analysis](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains why improvement inside an update space does not validate what remains outside it. The [defense portfolio](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) separates this narrow rebuttal from adjacent claims about authority, scaffolding, and sample efficiency. For the practical learning loop, [the readable-artifact analysis](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) asks what would make cross-artifact credit assignment tractable.
