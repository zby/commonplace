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

Now reverse the example. Two systems use the same parameterized controller architecture but different dense coefficient vectors. An expert sets one vector directly; gradient descent learns the other from data. Here too, the representational form is the same but the production method differs. Grouping the two prompts together and the two controllers together classifies them by representational form, not by how they were produced.

Richard Sutton's [2019 essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) argues that methods built around human knowledge repeatedly lose to general methods that exploit increasing computation through search and learning. That historical claim is a serious challenge to directly specified prompts, skill libraries, agent harnesses, and knowledge bases.

Sutton's lesson concerns how behavior is generated and selected, not where the result is stored. Directly specified domain knowledge must compete with methods that exploit growing computation through search and learning. His argument does not decide whether the selected result should be retained in weights, natural language, or symbolic artifacts. This article rejects only the inference from Sutton's pattern to a weights-only rule.

Representation still matters because it changes the optimization problem. A system that learns artifacts must connect outcomes to the artifacts or interactions that should change, reject harmful updates, and keep the artifact types and governing rules adequate—or revise them safely. A mixed system may be best, but the two-axis distinction alone does not show that.

## Two axes, not one

Across chess, Go, speech recognition, and computer vision, Sutton's pattern is that directly encoded domain knowledge helped, then plateaued as search and learning exploited more computation.

The first axis is how content is produced or revised. Designers can specify it directly, or a search or learning procedure can generate and select changes using evidence and computation. Classify each component and update separately: an optimizer may select a prompt revision while designers still specify the surrounding schema, evaluator, candidate generator, and acceptance rule.

The second axis is [representational form](../notes/definitions/representational-form.md): natural-language and symbolic artifacts usually expose identifiable content-bearing units, while content in model weights is usually distributed across dense numerical state. For this comparison, grouping the first two as localized yields four combinations:

| | Directly specified | Selected through search or learning |
|---|---|---|
| **Distributed-parametric** | Dense parameter values set directly by experts | Parameters fitted to data through gradient-based learning |
| **Localized (natural-language or symbolic)** | Designer-written prompts, feature extractors, tools, skills, rules, and schemas | Prompts, programs, skills, and harnesses selected through measured computational search |

The axes interact: representational form changes search, credit assignment, dependency checking, and retention costs.

## What this proves—and what it does not

The lower-right cell shows the central possibility: search can select a localized artifact. Suppose an optimizer searches ten thousand candidate deployment policies, tests them in a simulator and regression suite, and installs the best survivor as a natural-language file. The result remains localized, but search rather than the designer selected its behavior-shaping content.

This example settles only the categorical point: search-selected behavior-shaping content need not live in weights. It does not show that the optimizer is economical, that its simulator matches production, or that the retained policy will generalize. Localized domain structure still faces Sutton's scaling test; human authorship does not exempt it from search and learning. The proposal is to make these artifacts learning targets, not protect them from learning.

The remaining question is empirical: can learned localized artifacts compete on performance and total cost as systems, corpora, and task horizons grow? That depends on assigning credit, evaluating updates, retrieving and maintaining artifacts, and safely revising the update space.

## The machinery gap inside fixed decompositions

Within a fixed differentiable computation graph, data path, and objective, backpropagation calculates loss gradients for trainable parameters, and gradient descent turns them into updates. This machinery may still optimize the wrong objective, exploit spurious features, require enormous resources, or distribute a fact too widely for local editing. Even successful training does not by itself show that the architecture, loss, decomposition, or data are appropriate.

A large artifact system has no comparable default. Imagine an agent deployment governed by 5,000 instructions, tests, schemas, tool definitions, and memory items. A failed release does not identify whether the cause was a retrieval rule, an outdated instruction, a bad tool contract, a missing test, or an interaction among them. Asking a model to "reflect and improve the repository" delegates the diagnosis; it does not solve credit assignment.

Artifact systems have partial substitutes. Explicit dependency links can limit which artifacts need rechecking. Recorded execution traces preserve evidence about where a failure arose. Tests and validators can reject some bad candidates. [Localized retention helps most](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) when an update changes a few well-matched units and affects few others. The results examined here do not show these mechanisms combining into a general way to update heterogeneous artifacts.

[Artifact learners still operate inside a decomposition chosen by designers](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): artifact types, routing, mutation operators, evaluators, and schedules may all remain fixed. Success shows that the whole arrangement worked in the tested setting, not that these choices were necessary or better than excluded alternatives. Important fixed choices therefore need independent justification or a safe way to revise them. Redrawing artifact boundaries may also change what can be attributed, validated, or rolled back as one unit.

This asymmetry can make parametric learning look synonymous with learning. It is an engineering gap, not a definition.

## What current systems learn—and leave fixed

Three recent systems already learn natural-language or symbolic artifacts inside bounded update spaces. Compare them by asking what can change, what accepts an update, and what designers still supply.

[Agent Symbolic Learning](../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) models an agent pipeline as a network whose editable state includes prompts, tools, nodes, and their connections. Execution traces produce language-based feedback that is propagated backward through the network. Separate operators revise prompts, tool code, and topology; worsening changes can be rolled back. This is an offline proof of concept for search over a mixed natural-language and symbolic harness with frozen model weights. Its "backpropagation" vocabulary is an analogy, and its experiments do not isolate what each operator contributes.

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) treats folders containing `SKILL.md`, prompts, and executable code as persistent, evolving memory around a frozen language model. A router selects a skill. An observed failure can trigger a rewrite; repeated low utility can trigger a new skill. With Gemini-3.1-Flash, the paper reports large gains over a read-write ablation that disables skill optimization. The gains are strongest where later tasks revisit the same subject structure; reuse is weaker on heterogeneous tasks. The language model remains frozen, but the behavior-trained router is parametric, so the whole system is mixed.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) makes the mixture explicit. Its harness loop repairs prompts, tools, skills, middleware, and memory from failed trajectories. The repaired harness generates verified trajectories for supervised fine-tuning; the updated model then exposes the next harness bottlenecks. The design aims to move some behavior into weights while keeping the harness independently revisable. Its dual-loop evidence is limited to three 30-problem competition-math sets. A separate 200-hour study covers harness evolution without weight updates. No matched ablation isolates the migration, so the gains cannot yet be assigned to coevolution rather than additional fine-tuning or harness search alone.

The clearest comparison is how each system accepts an update and what designers still supply:

| System | How updates are accepted | Important structure left directly specified |
|---|---|---|
| Agent Symbolic Learning | The same prompt-based loss seeds feedback and scores the rerun; rollback follows if the score worsens | Node and trajectory model, optimizer families, loss and feedback prompts, edit language |
| Memento-Skills | One generated test runs through the updated skill and is scored by the judge; failure triggers rollback | Skill-folder contract, single-skill attribution, router design, utility rule, test gate |
| Co-Harness | A patch must improve targeted failures without regressing on held-out behavior; weight updates use filtered training trajectories | Five-part harness division, failure taxonomy, local-diff protocol, alternating schedule |

All three change substantial structure, but only inside update spaces specified by designers. Their studies do not compare those spaces with alternative decompositions or show how to revise their boundaries safely.

## The scaling test remains open

A fair test must compare systems that search for and retain localized artifacts with matched systems that spend comparable compute and human effort on stronger models, parametric training, distillation, or simpler memory. As corpus size, dependency density, task horizon, model capability, and compute grow, measure not only task success but also search cost, evaluator calls, retrieval failures, regressions, maintenance work, and human decisions.

The hypothesis fails its scaling test if, relative to those baselines, design, evaluation, or maintenance costs grow faster than the useful behavior retained. Warning signs include a bespoke ontology for every new domain, spending more on evaluation than the avoided failures would have cost, or failures that require repository-wide review to diagnose. In that case, localized artifacts may remain as interfaces and records while most learned competence moves into weights.

A modest success would be an efficient division of work: dense, diffuse adaptation may favor gradients, while sparse changes may favor localized artifacts when their units match the change and their dependency closure remains small. Co-Harness is an early example of this division.

A mixed system does not escape the decomposition problem. Its units must keep attribution and revalidation tractable or be safely revisable. Otherwise the mixture has only moved the scaling problem.

## Authority is a separate issue

Some artifacts record commitments, not merely knowledge. A model might reproduce a policy from its weights, but [reproduction does not establish authority](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): it does not show that the policy is current, where it applies, or who approved it. Models may generate or revise authoritative records, but accurate reproduction cannot replace the record the system actually uses.

## The research program

The Bitter Lesson sets the research program rather than deciding its outcome: do not protect human-authored knowledge from search. Build methods that can propose, test, retain, revise, and retire explicit structure—then compare them honestly with approaches that learn the same behavior elsewhere.

## Where to go next

The [production-method versus representational-form analysis](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) develops the full argument and its empirical burden. The [fixed-decomposition analysis](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains why improvement inside an update space does not validate what remains outside it. The [defense portfolio](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) separates this narrow rebuttal from adjacent claims about authority, scaffolding, and sample efficiency. For the practical learning loop, [the readable-artifact analysis](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) asks what would make cross-artifact credit assignment tractable.
