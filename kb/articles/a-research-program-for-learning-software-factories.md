---
description: "Research program on whether a software factory can learn to build a better software factory by acquiring, holding, and revising fallible project theory"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
  - kb/notes/a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md
  - kb/notes/a-software-factory-learns-when-production-experience-changes-reusable-machinery-used-later.md
  - kb/notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md
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

> **TL;DR.** If a software factory can build a better software factory, improvement can happen through changes to software-production machinery without training new models. This program tests whether LLM-based factories can do this by acquiring, holding, using, and revising fallible project theories.

## Better software factories

A [software factory](../notes/definitions/software-factory.md) is a configured production environment containing reusable production knowledge for a declared family of software. For the present program, its machinery may include models, prompts, natural-language artifacts, code, tools, workflows, tests, and evaluators.

A factory can produce another factory. That is prior art, and it places factory machinery inside the space of things software production can build. But construction alone is neither learning nor improvement. A factory may merely realize production knowledge supplied by people without [acquiring or improving that knowledge](../notes/a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md).

The research target is stronger:

```text
factory F
  -> production experience
  -> retained change to reusable production machinery
  -> successor factory F'
  -> better later production
```

Experience that causally determines a retained machinery change used in later production is [factory learning](../notes/a-software-factory-learns-when-production-experience-changes-reusable-machinery-used-later.md). The change can still be harmful. Calling the successor *better* additionally requires evidence of improvement under a declared objective and scope.

For the recursive-improvement claim, that comparison includes the capabilities needed to continue factory development. The successor must be able to do at least the improvement-relevant work of its predecessor, including producing further factories, while improving some relevant part of software production. A factory that produces one better artifact by consuming the capability that made further improvement possible is not better in this sense.

The retained change need not be a weight update. The learning unit is the [deployed system rather than only the model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), so improvement may occur through any operative part of the factory's production machinery.

## Coherent modification requires held project theory

The hard part is not merely generating another configuration. A better factory must modify software and reusable production machinery without silently destroying purposes and organization that immediate acceptance tests capture only partly.

Peter Naur's [1985 essay *Programming as Theory Building*](../sources/programming-as-theory-building.ingest.md) argues that programmers do this by building and holding a project-specific theory: an understanding of how the program maps onto the activity it supports, why it is organized as it is, and how new demands relate to that organization.

Naur's compiler example makes the last capacity especially important. The original group recognized that existing compiler facilities applied to novel modification requests. A successor group, despite receiving the program and extensive documentation, proposed locally plausible additions that bypassed those facilities. Access to information was not enough; the relevant connection had to be recognized when the new demand appeared.

This gives a useful distinction. A **retained theory** persists in a recoverable form. A **held theory** is a capability of the theory-bearing system: it recognizes when retained project theory is relevant to a novel demand and brings it to bear without the task author naming the project-specific connection. Modern learned interpreters make Naur's formerly human-only bearer question [empirically open](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

> Can an LLM-based software factory acquire and hold a fallible project theory, revise it from consequences, and use it to build a better factory?

Holding a theory does not mean deducing the correct change in one step. A working theory may be partial or wrong. It matters because it shapes search: what changes are considered, what must be preserved, how failures are interpreted, when to backtrack, and what should be revised. The bearer test is longitudinal—whether the system can [sustain coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

## Natural-language theory is the implementation bet

The functional claim does not require theory to be explicit or natural-language. Natural language is the tested realization because LLMs can interpret it into changes across heterogeneous factory machinery while it remains addressable, inspectable, and revisable.

This creates a new experimental control surface. The same project theory can be retained, withheld, surfaced, corrupted, or replaced while model weights remain fixed. It also exposes a central failure mode: knowledge may exist in weights or artifacts, and may even appear in the live context, without becoming action-relevant. [Storage and exposure do not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

Theory does not replace generate-and-verify, program search, or learned policies. A fallible theory may guide those mechanisms by allocating search and interpreting failures before decisive evidence is available. Another representation or a direct or mixed learner may perform the same causal job better; that is an empirical competitor, not a terminological exception.

## How to test the program

The first experiment need not solve recursive self-improvement. It can test Naurian theory-holding in ordinary software projects. Each project should contain a non-obvious reusable design idea, a novel requirement that can be met either by extending that idea or by adding a local special case, and a later demand that exposes whether the earlier modification preserved the program's organization.

The diagnostic path is:

```text
retained theory
  -> held theory under a novel demand
  -> theory-guided modification
  -> later consequence
  -> theory revision
  -> changed later modification
```

Controlled runs can separate the links. A direct probe tests whether the relevant theory is recoverable. An ordinary modification demand tests whether the system recognizes its relevance without a project-specific cue. A mechanism-specific hint tests whether failure was one of activation rather than application. Withheld and plausible wrong theories test whether theory content causally changes the modification rather than merely appearing in an explanation.

A later stage moves from project modification to factory learning. Production experience must change reusable production machinery, the change must affect later production, and the successor must be better under the declared comparison—including preservation of factory-development capability. Holding model weights fixed isolates the proposed non-weight route.

The program uses two complementary testbeds. **Commonplace** supplies a live, long-horizon human–LLM development process; the [recorded revision episode](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) is illustrative but not a controlled causal result. A controlled software-project testbed can run the interventions that Commonplace cannot. Current Commonplace evidence is human-inclusive, so progress also means reducing how often the operator must name the relevant theory, choose the decisive branch, or supply another task-specific learning decision.

The strategy should be narrowed where theory interventions are causally inert, another learning mechanism performs better at comparable total cost, or wider scope continues to require substantial new human-built specialization. It is compatible with the Bitter Lesson only if the bootstrap can [outgrow recurring human-supplied specialization](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

One successful transition would establish neither indefinite compounding nor computational closure. It would establish a more basic and testable result: a software factory can learn from production, hold project theory strongly enough to guide coherent modification, and use that learning to build a better software factory without training a new model.
