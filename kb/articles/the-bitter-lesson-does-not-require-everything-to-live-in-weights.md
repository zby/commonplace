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

Representation still changes the optimization problem. At scale, an artifact-learning system must assign credit across many artifacts and reject harmful updates. It must also preserve an adequate decomposition—the artifact types and rules that link, update, and evaluate them—as conditions change, or revise it safely when needed. A mixed system is one plausible outcome, not a conclusion supplied by the two-axis distinction.

## Two axes, not one

Sutton discusses chess, Go, speech recognition, and computer vision. In each domain, researchers encoded what they knew: chess strategy, Go patterns, phonemes and vocal anatomy, edges and visual features. Those knowledge-based methods helped, then plateaued. Search and learning methods eventually used more computation to outperform them.

The relevant distinction is therefore how content is produced. Designers can specify it directly, or a search or learning procedure can select it using evidence and additional computation. Classify each component and update separately, not the artifact as a whole. A prompt can combine directly written wording with search-selected revisions, while designers still specify its schema, evaluator, candidate generator, and acceptance rule.

A separate axis is [representational form](../notes/definitions/representational-form.md): how retained content is encoded and consumed. For agent systems, the main forms are natural-language artifacts such as prompts and instructions, symbolic artifacts such as programs and schemas, and distributed-parametric state such as model weights. Natural-language and symbolic artifacts expose identifiable content-bearing units, even when a behavior depends on several of them. Content in weights is usually distributed across dense numerical state. Grouping the first two as localized for this comparison yields four broad combinations:

| | Directly specified | Selected through search or learning |
|---|---|---|
| **Distributed-parametric** | Dense parameter values set directly by experts | Parameters fitted to data through gradient-based learning |
| **Localized (natural-language or symbolic)** | Designer-written prompts, feature extractors, tools, skills, rules, and schemas | Prompts, programs, skills, and harnesses selected through measured computational search |

The axes describe different things, but they interact in practice. Representational form changes what can be searched, how credit can be assigned, how many dependent artifacts must be rechecked, and what it costs to retain a result.

## What this proves—and what it does not

The lower-right cell is the one a weights-only reading erases. Suppose an optimizer searches ten thousand candidate deployment policies, tests them in a simulator and regression suite, and installs the best survivor as a natural-language file. The result is still localized, but search rather than the designer selected its behavior-shaping content.

That production history defeats the categorical claim that localized artifacts are inherently incompatible with the Bitter Lesson. It does not show that the optimizer is economical, that its simulator captures production, or that the retained policy will generalize. Sutton's argument therefore does not confine scalable learning to weights. But localized domain structure offered as a source of generalizable competence still faces his scaling test; it cannot remain exempt from search and learning merely because experts produced it. The compatible proposal is not to protect such structure from learning, but to make the artifacts that carry it targets of learning too.

The stronger empirical claim is much harder. As systems, corpora, and task horizons grow, can systems that search for and retain localized artifacts remain competitive once both performance and total cost are counted? The comparison must use matched alternatives that spend comparable compute and human effort on stronger models, parametric training, distillation, or simpler memory. The answer depends on evaluator quality, maintenance, retrieval, and the remaining human work. The immediate engineering problem is how to assign credit, reject bad updates, and test or revise the decomposition that defines what can change.

## The machinery gap inside fixed decompositions

Gradient-based parametric learning has a repeatable credit-assignment procedure inside a chosen differentiable decomposition. Given a fixed computation graph, parameterization, data path, and objective, backpropagation uses the chain rule to calculate the local sensitivity of the chosen loss to each connected trainable parameter. Gradient descent turns those sensitivities into update directions. The process may optimize the wrong objective, exploit a spurious feature, require enormous data and compute, or distribute a fact so widely that no local edit can isolate it. It does not determine whether the architecture, loss, decomposition, or training distribution is wrong.

A large artifact system has no comparable default. Imagine an agent deployment governed by 5,000 instructions, tests, schemas, tool definitions, and memory items. A failed release does not identify whether the cause was a retrieval rule, an outdated instruction, a bad tool contract, a missing test, or an interaction among them. Asking a model to "reflect and improve the repository" delegates the diagnosis; it does not solve credit assignment.

Localized artifact systems offer partial substitutes. Explicit dependency links can limit which artifacts need rechecking. Recorded execution traces preserve evidence about where a failure arose. Tests and validators can reject some bad candidates. [Localized retention helps most](../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) when an update changes a few well-matched units and affects few others. The systems examined here do not show these mechanisms composing into a general update rule for heterogeneous artifacts.

The [same analysis applies recursively](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). A system may select prompt content through search while designers still specify its artifact types, routing rules, mutation operators, evaluator, and update schedule. That does not invalidate the learned update; it identifies its scope. The system searches inside an effective update space chosen in advance. Fixed choices are not defects by themselves. But when a consequential choice is neither imposed by the problem nor independently warranted, improvement inside the boundary cannot validate it. Changing artifact boundaries may also change the units of attribution, validation, and rollback, so safely revising such choices becomes part of the empirical scaling burden.

This missing machinery helps explain why people conflate representational form with production method. Gradient-based parametric learning has a mature optimization loop; artifact learning has partial counterparts. That engineering difference is real, but it does not define what learning must look like.

## What current systems learn—and leave fixed

Bounded instances of the learned-localized cell already exist. The three systems below should be read through three questions: what can change, what accepts an update, and what enclosing structure remains directly specified.

[Agent Symbolic Learning](../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) models an agent pipeline as a network whose editable state includes prompts, tools, nodes, and their connections. Execution traces produce language-based feedback that is propagated backward through the network. Separate operators revise prompts, tool code, and topology; worsening changes can be rolled back. This is an offline proof of concept for search over a mixed natural-language and symbolic harness with frozen model weights. Its "backpropagation" vocabulary is an analogy, and its experiments do not isolate what each operator contributes.

[Memento-Skills](../sources/memento-skills-let-agents-design-agents.ingest.md) treats folders containing `SKILL.md`, prompts, and executable code as persistent, evolving memory around a frozen language model. A router selects a skill. An observed failure can trigger a rewrite; repeated low utility can trigger a new skill. With Gemini-3.1-Flash, the paper reports large gains over a read-write ablation that disables skill optimization. The gains are strongest where later tasks revisit the same subject structure; reuse is weaker on heterogeneous tasks. The language model remains frozen, but the behavior-trained router is parametric, so the whole system is mixed.

[Co-Harness](../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) makes the mixture explicit. Its harness loop repairs prompts, tools, skills, middleware, and memory from failed trajectories. The repaired harness generates verified trajectories for supervised fine-tuning; the updated model then exposes the next harness bottlenecks. The design aims to move some behavior into weights while keeping the harness independently revisable. Its dual-loop evidence is limited to three 30-problem competition-math sets. A separate 200-hour study covers harness evolution without weight updates. No matched ablation isolates the migration, so the gains cannot yet be assigned to coevolution rather than additional fine-tuning or harness search alone.

Their update gates and enclosing structures make the comparison clearer:

| System | How artifact updates are accepted | Important structure left directly specified |
|---|---|---|
| Agent Symbolic Learning | The same prompt-based loss seeds feedback and scores the rerun; rollback follows if the score worsens | Node and trajectory model, optimizer families, loss and feedback prompts, edit language |
| Memento-Skills | One generated test runs through the updated skill and is scored by the judge; failure triggers rollback | Skill-folder contract, single-skill attribution, router design, utility rule, test gate |
| Co-Harness | A patch must improve targeted failures without regressing on held-out behavior; weight updates use filtered training trajectories | Five-part harness division, failure taxonomy, local-diff protocol, alternating schedule |

The acceptance mechanisms remain bounded: Agent Symbolic Learning reuses its loss machinery, Memento-Skills relies on one generated test, and Co-Harness applies held-out regression only to harness patches. All three revise substantial structure, but each also leaves an enclosing update space directly specified. Their results test learning inside those spaces. They do not test whether excluded decompositions would perform better or how to revise the boundaries safely.

## The scaling test remains open

To make the learned-artifact hypothesis falsifiable, compare systems that search for and retain localized artifacts with matched systems that invest comparable compute and human effort in stronger models, parametric training, distillation, or simpler memory. Scale the corpus, dependency density, task horizon, model capability, and compute budget. Measure not only task success but also search cost, evaluator calls, retrieval failures, regressions, maintenance work, and human decisions.

The hypothesis loses its scaling case if, relative to those baselines, its human-design, evaluation, or maintenance burden grows faster than the useful behavior it preserves. Warning signs include a bespoke ontology for every new domain, evaluation costs that exceed the failures they avert, or failures that require repository-wide review to diagnose. In that case, localized artifacts may survive as interfaces and records while most learned competence moves into weights.

The hypothesis succeeds in a modest form if different representations remain efficient for different kinds of change. Dense, diffuse adaptation may favor gradient-based updates. Sparse changes may favor localized artifacts when the units match the change and their explicit dependency closure remains small. Co-Harness illustrates the shape of such an architecture: its harness supplies verified trajectories for supervised fine-tuning, its training loop attempts to distill selected behavior into weights, and the harness remains available for later localized repairs.

Even in a mixed system, the chosen decomposition must continue to admit the relevant distinctions and corrections while keeping credit assignment and revalidation tractable as domains change, or the system must revise that decomposition without making every change require exhaustive corpus-wide search. Otherwise, mixed representation has only moved the scaling problem.

## A separate corollary: authority still needs an operative record

Whatever the result of this scaling test, a separate issue remains: some artifacts do not merely encode knowledge; they record commitments. Consider the policy "production retries use exponential backoff." A model might reproduce that sentence perfectly from its weights. But [reproduction does not establish authority](../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md): it does not show that the policy is current, where it applies, or who approved it. The policy becomes operational ground truth only when an authorized process records it and the system consumes that record.

The same is true of API schemas, access-control rules, release approvals, and tests that gate changes. These artifacts do more than carry information: they declare current interfaces, grant authority, and accept or reject changes. This answers the adjacent claim that accurate reproduction alone makes an operative external record redundant; it does not establish that learned semantic artifacts scale. Stronger models may generate and revise these records, and some content may move into weights. Even so, current commitments and executable interfaces need an authoritative record that the system actually uses.

## The research program

The main scaling question remains empirical. The Bitter Lesson therefore sets the research program rather than deciding its outcome. Do not protect human-authored knowledge from search. Build methods that can propose, test, retain, revise, and retire explicit structure—then compare them honestly with approaches that learn the same behavior elsewhere.

## Where to go next

The [production-method versus representational-form analysis](../notes/the-bitter-lesson-selects-production-methods-not-representational.md) develops the full argument and its empirical burden. The [fixed-decomposition analysis](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) explains why improvement inside an update space does not validate what remains outside it. The [defense portfolio](../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) separates this narrow rebuttal from adjacent claims about authority, scaffolding, and sample efficiency. For the practical learning loop, [the readable-artifact analysis](../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) asks what would make cross-artifact credit assignment tractable.
