---
description: "Research program on whether agentic software factories can learn reusable production machinery and whether fallible natural-language project theory can make open-ended modification coherent"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
  - kb/notes/a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md
  - kb/notes/an-agentic-substrate-becomes-a-software-factory-through-family-specific-production-machinery.md
  - kb/notes/broad-software-demands-create-pressure-for-agentic-factory-development.md
  - kb/notes/a-software-factory-learns-when-production-experience-changes-reusable-machinery-used-later.md
  - kb/notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md
  - kb/notes/theory-mediation-can-coordinate-heterogeneous-factory-development.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md
  - kb/notes/a-retained-theory-intervention-isolates-one-explicit-theory-surface.md
  - kb/notes/disconnected-witnesses-do-not-establish-a-full-causal-path-through-theory.md
  - kb/notes/natural-language-project-state-specializes-search-heuristics.md
  - kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md
  - kb/notes/open-ended-improvement-allocates-search-before-evaluation.md
  - kb/notes/lightweight-search-control-does-not-license-adoption.md
  - kb/notes/backtracking-keeps-lightweight-search-control-provisional.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for learning software factories

> **Draft.** Comments and counterexamples are welcome through the repository's issue tracker.

> **TL;DR.** If software factories can build software factories, production experience could improve the machinery used to build later software without training new models. The hard part is not retaining more information but keeping open-ended modification coherent. This program tests whether an LLM-based system can acquire, hold, use, and revise a fallible project theory that guides search and factory development as consequences arrive.

## Learning software factories

An agentic coding system becomes a [software factory](../notes/definitions/software-factory.md) when a general substrate is configured with reusable production knowledge for a declared family of software products or solutions. [Factory development](../notes/definitions/factory-development.md) constructs or revises that reusable machinery; solution development uses it to build or maintain one family member.

As software demands widen, it becomes less plausible that every useful decomposition, representation, workflow, tool, evaluator, context policy, and recovery procedure can be supplied in advance. A general agentic system should therefore be able to participate in factory development when its installed machinery is inadequate. This is an empirical conjecture: a fixed sufficiently general substrate remains a live alternative.

Factories that build factories are prior art. Learning requires a stronger relation:

```text
production under current factory machinery
  -> experience bearing on that machinery
  -> system-determined change to reusable machinery
  -> retention
  -> changed later production
```

Experience without a reusable change is feedback; repairing only the current product is solution development. The relevant learning unit is the [deployed system rather than only the model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), so retained changes may live in weights, natural-language artifacts, symbolic software, retrieved memories, or mixtures.

## Coherent modification requires held project theory

Minimal factory learning does not require theory. Trial-and-error retention, trajectory reuse, program search, learned policies, direct optimization, and mixtures can all change reusable machinery. The harder target is open-ended coherent modification: integrating new demands without destroying purposes and organization that local acceptance criteria capture only partly.

Peter Naur's [1985 essay *Programming as Theory Building*](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf) argues that programmers build and hold a project-specific theory: an understanding of how the program maps onto the activity it supports, why it is organized as it is, and how new demands relate to that organization. For this target, the program adopts Naur's functional constraint: some project-specific state or capacity must perform those mapping, justification, and integration roles. The claim is about a function, not a carrier; the theory may be distributed across weights, artifacts, tools, and participants.

Naur treated the theory as held by programmers rather than by the program or its documentation. Modern learned interpreters make that boundary testable. A retained theory is not yet a held theory: the theory-bearing system must recognize when it is relevant to a novel demand and bring it to bear. For LLM-based systems, theory may be recoverable when explicitly requested yet fail to guide a modification when its relevance is not named in advance.

> Can an agentic system become a bearer of a fallible project theory—holding and revising it well enough to keep successive modifications coherent when decisive feedback arrives only later?

Holding a theory does not mean deducing the correct change in one step. Human developers work from partial and sometimes mistaken understanding: they inspect, search, make tentative changes, test assumptions, backtrack, and revise both the program and their understanding. A computational theory-holder should be judged by the same longitudinal standard. The theory counts because it shapes which changes are considered, what must be preserved, how failures are interpreted, when to reverse course, and what should be revised. [Holding a program theory means sustaining coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

```text
partial theory
  -> theory-guided search and tentative change
  -> provisional check
  -> later or external consequence
  -> retain, repair, backtrack, or revise
  -> changed theory and later search
```

Generic search remains part of the system. Theory can guide generate-and-verify by allocating search and interpreting failures before decisive evaluation is available; backtracking keeps those choices provisional. The empirical question is whether project-specific theory improves coherent modification at comparable information and total cost.

## Natural-language theory is the implementation bet

The functional claim does not require project theory to be explicit or natural-language. The implementation hypothesis is narrower:

> Fallible natural-language theory may provide an unusually versatile, addressable surface for coordinating heterogeneous production machinery.

An LLM can interpret retained project state into changes across decomposition, context selection, schemas, workflows, prompts, tests, evaluators, tools, and code. One possible mechanism is that [natural-language project state specializes search heuristics already present in model weights](../notes/natural-language-project-state-specializes-search-heuristics.md).

The claim is causal. A theory that merely accompanies the work is documentation. Theory mediation requires the retained theory to change search, diagnosis, evaluation, recovery, or revision. A failure of the explicit natural-language surface would not show that a successful alternative had no project theory; another representation may carry the same functional organization more effectively.

## How the program is tested

The program couples two testbeds. **Commonplace** is the live human-agent system in which agents use retained theory to revise the knowledge base, software, and methodology that guide later work. The operator still supplies much global-fit judgment and final authorization. The **programming-agent testbed** will place persistent fallible theory inside an agentic software-production system and give it sequences of modifications whose later demands can expose earlier mistakes.

The strongest path the program wants to observe is:

```text
retained theory
  -> held theory
  -> theory-mediated search or factory-development decision
  -> realized change
  -> independent or delayed consequence
  -> retained theory-state revision
  -> changed later operation
```

Evidence comes in levels: **mediation**, where changing or withholding theory changes a consequential decision; **empirical contact**, where the intervention produces an outcome bearing on the theory; **theory learning**, where that outcome changes the retained theory; and **recurrence**, where the revised theory changes later operation. A contemporaneous citation is only a trace; withholding, replacement, or perturbation gives stronger evidence that theory was load-bearing.

The [2026-08-30 Commonplace revision record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) illustrates part of this path: retained theory guided work, operator feedback revised it, and the result affected later work. It was not recorded prospectively enough for causal or comparative attribution.

The first controlled contrast can isolate the retained-to-held transition: is relevant theory merely recoverable when explicitly requested, or does the system recognize its relevance to a novel modification demand without a project-specific cue and bring it to bear? Matched runs can then compare usable theory with theory withheld, plausible but wrong theory, and information-matched factual records. Later demands must be able to expose mistakes introduced by earlier modifications. A factory-learning claim additionally requires changed reusable machinery to affect later production; otherwise the result concerns theory-mediated solution modification.

System use can test a theory's causal usefulness and fit, but it is not an independent truth oracle. Factual and formal checks, held-out demands, rival theories, and later consequences remain necessary to prevent a self-confirming loop.

## Bootstrap and failure conditions

The current Commonplace loop is human-inclusive. Agents already retrieve, synthesize, criticize, write, execute repository changes, test, validate, and retain results, while the operator still supplies decisive high-level direction, global-fit judgment, and authorization. The bootstrap target is therefore not to introduce computation but to reduce recurring task-specific human decisions by turning them into reusable computational machinery.

Progress should be reported against a fixed boundary: how much of the learning path can the computational subsystem carry without a person supplying the task-specific decomposition, evaluator, selection, promotion, or recovery choice? [The decisions that stay human, and what would move them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops the fuller boundary, warrant, and transfer argument.

The Bitter Lesson is a constraint on this strategy, not a reason that learned state must live in weights. [Learning can produce explicit artifacts as well as weights](../notes/the-bitter-lesson-selects-production-methods-not-representational.md), but a bootstrap is credible only if learning can outgrow recurring human-supplied specialization as scope widens. The companion article [The Bitter Lesson does not require everything to live in weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) develops that scaling argument and the competing weight-update view.

The strategy should be narrowed or abandoned where retained theory is causally inert, another representation or direct or mixed learning process performs better at comparable total cost, or each new covered area continues to require substantial human-built specialization. Factory learning also does not by itself establish reflection, computational closure, self-improvement, compounding, or broad production reach; those require separate evidence.

The program therefore makes two claims at different strengths. It does **not** claim that every factory update must be theory-mediated or that project theory must remain explicit or natural-language. It **does** claim that open-ended coherent modification requires a project-specific theory-bearing capacity. The contingent bet is that LLM-interpreted natural-language theory is a useful way to build and study that capacity while software factories learn better machinery for their own future production.
