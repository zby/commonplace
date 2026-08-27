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
  - kb/sources/symbolic-learning-enables-self-evolving-agents.ingest.md
  - kb/sources/memento-skills-let-agents-design-agents.ingest.md
  - kb/sources/co-harness-co-evolving-harness-and-model-weights.ingest.md
---

# The Bitter Lesson does not require everything to live in weights

> **Draft.** This article is circulating for comments; its claims, structure, and even its central thesis may still change. Comments are welcome below.

Richard Sutton's [2019 essay](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) argues that methods built around human knowledge repeatedly lose to general methods that exploit increasing computation through search and learning. That historical pattern is a serious challenge to directly specified prompts, skill libraries, agent harnesses, and knowledge bases.

Sutton's lesson concerns how behavior-shaping content is generated and selected, but does not by itself determine how the selected content is encoded and consumed. Directly specified domain knowledge must compete with methods that exploit growing computation through search and learning. This article rejects only the inference from Sutton's pattern to a weights-only rule.

Consider two pairs. In the first, an engineer writes one system prompt, while an optimizer generates, evaluates, and selects another. Both are natural-language artifacts produced by different methods. In the second, an expert directly sets one dense controller vector, while gradient descent learns another inside the same parameterized architecture. Both are dense parameter vectors produced by different methods. In each pair, the kind of representation stays fixed while the production method changes.

That distinction settles a categorical point, not an empirical one. It does not show whether learned natural-language or symbolic artifacts are competitive at scale or whether a mixed system is best. Representation still matters because it changes the optimization problem. A system that learns artifacts must connect outcomes to the artifacts or interactions that should change, reject harmful updates, and keep the artifact types and governing rules adequate—or revise them safely.

## Two axes, not one

Across chess, Go, speech recognition, and computer vision, Sutton describes a pattern: directly encoded domain knowledge helped, then plateaued as search and learning exploited more computation.

That pattern has two separable axes. The first is how content is produced or revised. Designers can specify it directly, or a search or learning procedure can generate and select changes using evidence and computation. Classify each component and update separately: an optimizer may select a prompt revision while designers still specify the surrounding schema, evaluator, candidate generator, and acceptance rule.

The second axis is [representational form](../notes/definitions/representational-form.md): natural-language and symbolic artifacts usually expose identifiable content-bearing units, while content in model weights is usually distributed across dense numerical state. For this comparison, grouping the first two as localized yields four combinations:

| | Directly specified | Selected through search or learning |
|---|---|---|
| **Distributed-parametric** | Dense parameter values set directly by experts | Parameters fitted to data through gradient-based learning |
| **Localized (natural-language or symbolic)** | Designer-written prompts, feature extractors, tools, skills, rules, and schemas | Prompts, programs, skills, and harnesses selected through measured computational search |

The axes interact: representational form changes search, credit assignment, dependency checking, and retention costs.

## What this proves—and what it does not

Existing systems already populate the lower-right cell in bounded settings. [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) generates program functions with a pretrained language model, evaluates them, and retains successful programs for further search. [AlphaDev](https://www.nature.com/articles/s41586-023-06004-9) used reinforcement learning and tree search to discover assembly sorting routines later incorporated into LLVM's standard C++ library. Together they provide concrete bounded instances of computationally selected localized artifacts.

That settles only the categorical point: search-selected behavior-shaping content need not live in weights. These examples do not show that artifact search is economical, that its evaluators match deployment, or that retained artifacts generalize. Localized domain structure still faces Sutton's scaling test; human authorship does not exempt it from search and learning. The proposal is to make these artifacts learning targets, not protect them from learning.

The remaining question is empirical: can learned localized artifacts compete on performance and total cost as systems, corpora, and task horizons grow? The answer depends on credit assignment, evaluation quality, retrieval and maintenance costs, and whether the update space itself can be revised safely.

## The machinery gap inside fixed decompositions

Within a fixed differentiable computation graph, data path, and objective, backpropagation calculates loss gradients for trainable parameters, and gradient descent turns them into updates. This machinery may still optimize the wrong objective, exploit spurious features, require enormous resources, or distribute a fact too widely for local editing. Even successful training does not by itself show that the architecture, loss, decomposition, or data are appropriate.

A large artifact system has no comparable default. Imagine an agent deployment governed by 5,000 instructions, tests, schemas, tool definitions, and memory items. A failed release does not identify whether the cause was a retrieval rule, an outdated instruction, a bad tool contract, a missing test, or an interaction among them. Asking a model to "reflect and improve the repository" delegates the diagnosis. It does not solve credit assignment.

Artifact systems have partial substitutes: dependency links can limit rechecking, traces can preserve evidence about where a failure arose, and tests and validators can reject some bad candidates. [Localized retention helps most](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) when an update changes a few well-matched units and affects few others. The results examined here do not show that these mechanisms combine into a general method for updating heterogeneous artifacts.

[Artifact learners still operate inside a decomposition chosen by designers](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): artifact types, routing, mutation operators, evaluators, and schedules may all remain fixed. Success shows that the whole arrangement worked in the tested setting, not that these choices were necessary or better than excluded alternatives. Fixedness is not itself a defect. Consequential fixed choices need independent justification or a safe way to revise them. Decomposition is a difficult revision target because redrawing artifact boundaries also changes the units of credit assignment, validation, and rollback.

Parametric learning therefore has a default update mechanism that artifact learning lacks. Whether artifact systems can close that gap economically—or whether it reflects an unfavorable scaling law—remains empirical.

## What current systems learn—and leave fixed

Three recent systems already learn natural-language or symbolic artifacts inside bounded update spaces. The useful comparison is what can change, what accepts an update, and what designers still supply.

[Agent Symbolic Learning](../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) models an agent pipeline as a network whose editable state includes prompts, tools, nodes, and their connections. Execution traces produce language-based feedback that is propagated backward through the network. Separate operators revise prompts, tool code, and topology; worsening changes can be rolled back. This is an offline proof of concept for search over a mixed natural-language and symbolic harness with frozen model weights. Its "backpropagation" vocabulary is an analogy.

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) treats folders containing `SKILL.md`, prompts, and executable code as persistent, evolving memory around a frozen language model. A behavior-trained router selects a skill. After a judged failure, the write phase attributes it to one skill and rewrites that skill in place, or, when the skill's utility has stayed low over enough uses, creates a new one. Each mutation is guarded by a synthetic test case run through the updated skill and scored by a judge, with rollback on failure — a judge-scored single case, not a deterministic test suite, and a configurable gate in the algorithm as stated. With the Gemini-3.1-Flash language model underneath, the full system scores 66.0% on GAIA against 52.3% for a read-write ablation that disables skill optimization, and 38.7% against 17.9% on HLE; both are question-answering benchmarks. The underlying language model remains frozen, but the router is parametric, so the whole system is mixed.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) makes the mixture explicit. Its critic analyzes failed trajectories and proposes validated local updates to prompts, tools, skills, middleware, and memory. The improved harness generates trajectories for supervised fine-tuning, and the updated model enters the next harness-repair round. The paper runs two full rounds of this alternation. That establishes an implemented coupled loop, not that its allocation scales or beats matched alternatives.

The systems differ most clearly in how they accept updates and what designers still supply:

| System | How updates are accepted | Important structure left directly specified |
|---|---|---|
| Agent Symbolic Learning | The same prompt-based loss seeds feedback and scores the rerun; rollback follows if the score worsens | Node and trajectory model, optimizer families, loss and feedback prompts, edit language |
| Memento-Skills | A synthetic test case is generated, run through the updated skill, and scored by a judge; the mutation is rolled back on failure | Skill-folder contract, single-skill attribution, low-utility threshold for new skills, test-gate design, router design, underlying language model |
| Co-Harness | The critic proposes validated local harness updates; the accepted harness generates the next model's training trajectories | Five-part harness division and alternating harness/SFT schedule |

## The scaling test remains open

A fair test must compare end-to-end systems under comparable total budgets. The budget must include model training and inference, artifact search, evaluator calls, development, maintenance, and human decisions. As corpus size, dependency density, task horizon, model capability, and available compute grow, measure task success alongside retrieval failures, regressions, and the cost of retaining useful behavior.

The hypothesis fails on a tested growth regime if, relative to those baselines, its total design, evaluation, and maintenance cost grows faster than the useful behavior it retains, as measured by the comparison's task and regression outcomes. Warning signs include a bespoke ontology for every new domain, spending more on evaluation than the avoided failures would have cost, or failures that require repository-wide review to diagnose. In that case, localized artifacts may remain as interfaces and records while most learned competence moves into weights.

A modest success would be an efficient division of work. Dense, diffuse adaptation may favor gradients. Sparse changes may favor localized artifacts when their units match the change and their dependency closure remains small. Co-Harness is designed around this division, but its experiments do not establish that the allocation is efficient.

A mixed system does not escape the decomposition problem. Its units must keep attribution and revalidation tractable, or they must be safely revisable. Otherwise the mixture has only moved the scaling problem.

## The research program

The Bitter Lesson sets the research program rather than deciding its outcome: do not protect human-authored knowledge from search. Build methods that can propose, test, retain, revise, and retire explicit structure. Then compare them honestly with approaches that learn the same behavior elsewhere.

## Where to go next

The [production-method versus representational-form analysis](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) develops the full argument and its empirical burden. The [fixed-decomposition analysis](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains why improvement inside an update space does not validate what remains outside it. The [defense portfolio](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) separates this narrow rebuttal from adjacent claims about authority, scaffolding, and sample efficiency. For the practical learning loop, [the readable-artifact analysis](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) asks what would make cross-artifact credit assignment tractable.
