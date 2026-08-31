---
description: "Research program on whether a software factory configured to produce factories can directly build a better successor by acquiring, holding, and revising project theory"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
  - kb/notes/factory-construction-does-not-establish-knowledge-acquisition.md
  - kb/notes/theory-mediation-can-coordinate-heterogeneous-factory-development.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/knowledge-storage-does-not-imply-contextual-activation.md
  - kb/notes/natural-language-project-state-specializes-search-heuristics.md
  - kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for learning software factories

> **Draft.** Comments and counterexamples are welcome through the repository's issue tracker.

> **TL;DR.** If a software factory can build a better software factory, improvement can happen through changes to software-production machinery without training new models. This program tests whether LLM-based factories can do this by acquiring, holding, using, and revising project theories.

## Better software factories

A [software factory](../notes/definitions/software-factory.md) is a configured production environment containing reusable production knowledge for a declared family of software. Its machinery can include models, prompts, natural-language artifacts, code, tools, workflows, tests, and evaluators.

Prior work describes software factories configured to produce software factories as members of their declared family. In the [examples reviewed here](../notes/factory-construction-does-not-establish-knowledge-acquisition.md), people supply the production knowledge that determines the produced factory.

The research target begins with a factory of this kind and gives it an explicit task: build a successor factory that is better than itself. The successor is the intended product of the task.

```text
factory F configured to produce factories
  -> construct candidate successor F'
  -> evaluate F' against the declared objective and prior scope
  -> revise F'
  -> accept F' only if it is better
```

The accepted successor is the evidence of improvement; intermediate revisions are part of its construction.

A successor is better if it is at least as capable as its predecessor on the declared prior scope—including the ability to produce and improve further factories—and strictly better on at least one relevant dimension of software production. This preserves the capacity for further improvement rather than trading it away for a one-off gain.

The comparison is between [deployed systems rather than only model weights](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). The successor may improve through changes to any operative part of its production machinery.

## Coherent modification requires held project theory

The hard part is constructing a successor that changes software and reusable production machinery without silently destroying purposes and organization that immediate acceptance tests capture only partly.

Peter Naur's [1985 essay *Programming as Theory Building*](../sources/programming-as-theory-building.ingest.md) argues that programmers do this by building and holding a project-specific theory: an understanding of how the program maps onto the activity it supports, why it is organized as it is, and how new demands relate to that organization.

Naur's compiler example makes the last capacity especially important. The original group recognized that existing compiler facilities applied to novel modification requests. A later group, despite receiving the program and extensive documentation, proposed locally plausible additions that bypassed those facilities. Access to information was not enough; the relevant connection had to be recognized when the new demand appeared.

This gives a useful distinction. A **retained theory** persists in a recoverable form. A **held theory** is a capability of the theory-bearing system: it recognizes when retained project theory is relevant to a novel demand and brings it to bear without the task author naming the project-specific connection. Modern learned interpreters make Naur's formerly human-only bearer question [empirically open](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

> Can an LLM-based software factory acquire and hold a project theory, revise it in response to evaluation and consequences, and use it to construct a better successor factory?

Holding a theory guides search rather than guaranteeing a correct change in one step. The theory can be fallible—partial, provisional, or wrong—while still shaping what changes are considered, what must be preserved, how failures are interpreted, when to backtrack, and what should be revised. The bearer test is longitudinal: whether the system can [sustain coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

## Natural-language theory is the implementation bet

Project theory may be carried in many forms. Natural language is the tested realization because LLMs can interpret it into changes across heterogeneous factory machinery while it remains addressable, inspectable, and revisable.

Natural language also makes the theory directly manipulable in experiments. The same project theory can be retained, withheld, surfaced, corrupted, or replaced while model weights remain fixed. These interventions expose a central failure mode: knowledge may exist in weights or artifacts, and may even appear in the live context, without becoming action-relevant. [Storage and exposure do not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

Such a theory can guide generate-and-verify, program search, and learned policies by allocating search and interpreting failures before decisive evidence is available. Other representations and direct or mixed learning methods are competing approaches and should be compared empirically.

## How to test the program

The first experiment isolates Naurian theory-holding in ordinary software projects. Each project should contain a non-obvious reusable design idea, a novel requirement that can be met either by extending that idea or by adding a local special case, and a later demand that exposes whether the earlier modification preserved the program's organization.

The diagnostic path is:

```text
retained theory
  -> held theory under a novel demand
  -> theory-guided modification
  -> later consequence
  -> theory revision
  -> changed later modification
```

A direct probe tests whether the relevant theory is recoverable. An ordinary modification demand tests whether the system recognizes its relevance without a project-specific cue. A mechanism-specific hint then distinguishes failure to recognize relevance from failure to apply the theory. Withholding the theory or replacing it with a plausible but wrong alternative tests whether its content causally changes the modification rather than merely appearing in an explanation.

A later experiment gives a factory the explicit task of building a successor factory. Candidate successors are evaluated against the predecessor's prior scope, the target improvement, and their ability to repeat the factory-development process. Evaluation must guide revision of the candidate. Success is measured by the successor factory itself: it must be better under the declared comparison. Holding model weights fixed isolates the proposed non-weight route.

The program uses two complementary testbeds. **Commonplace** supplies a live, long-horizon human–LLM process for studying theory-holding and revision; the [recorded revision episode](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) illustrates part of the mechanism but is not a controlled better-factory result. A controlled software-project testbed can run the interventions that Commonplace cannot. Current Commonplace evidence is human-inclusive, so progress also means reducing how often the operator must name the relevant theory, choose the decisive branch, or supply another task-specific learning decision.

The theory-mediated approach loses support if changing or withholding project theory does not change construction decisions, if another learning mechanism performs better at comparable total cost, or if each new area still requires substantial human-built specialization. The bootstrap fits the Bitter Lesson only if it can [outgrow recurring human-supplied specialization](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

A successful transition would establish a bounded result: a software factory configured to produce factories can hold project theory strongly enough to construct, evaluate, and revise a successor that is better than itself without training a new model. Indefinite compounding and computational closure would remain open.
