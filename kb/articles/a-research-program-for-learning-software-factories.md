---
description: "Research program on whether a software factory can learn from its production experience — acquiring, holding, and revising project theory — so that a later factory state passes a declared better-factory comparison against its predecessor"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
  - kb/notes/factory-construction-does-not-establish-knowledge-acquisition.md
  - kb/notes/factory-learning-retains-experience-in-reusable-machinery.md
  - kb/notes/commitment-not-derivation-creates-new-ground-truth.md
  - kb/notes/theory-mediation-can-coordinate-heterogeneous-factory-development.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/project-theory-relates-new-demands-to-existing-organization.md
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

> **TL;DR.** A software factory learns when its production experience causes retained changes to its machinery that later work depends on; it improves when a later factory state beats an earlier one under a declared comparison. This program tests whether LLM-based factories can learn this way without training new models, by acquiring, holding, using, and revising project theories.

## Better software factories

A [software factory](../notes/definitions/software-factory.md) is a configured production environment containing reusable production knowledge for a declared family of software. Its machinery can include models, prompts, natural-language artifacts, code, tools, workflows, tests, and evaluators.

Prior work describes software factories configured to produce software factories as members of their declared family. In the [examples reviewed here](../notes/factory-construction-does-not-establish-knowledge-acquisition.md), people supply the production knowledge that determines the produced factory.

The research target is a factory that learns from what it produces. A factory undergoes [factory-level learning](../notes/factory-learning-retains-experience-in-reusable-machinery.md) when production experience—failures, surprises, evaluations, corrections, delayed consequences—causes a retained change to its reusable production machinery, and later production or factory development depends on that change.

In current agentic coding systems this learning is interleaved with operation rather than confined to a separate phase. A failed task can immediately cause a note to be written, a test added, a rule revised, a tool changed, and the task retried; [Compound Engineering's retention pathway](../agentic-systems/compound-engineering-plugin.md) works this way. Some of those changes already change the factory. There need be no phase in which an unchanged factory merely accumulates experience before improvement begins. The process is a loop, not a pipeline:

```text
production and factory development under the current factory state
  <-> experience from that work
  <-> retained, organized state: project theory, indexes, tests, tools
  -> later production and factory-development decisions
```

Improvement is judged in a second view that takes snapshots of this process. Fix two factory states and compare them:

```text
factory state F
  -> intervening production, learning, and factory development
  -> factory state F'
  -> evaluate F' against F under a fixed declared comparison
  -> adopt F' only if the evidence supports improvement
  -> use F' in later production and factory development
```

The successor F' is a measurement boundary on a continuous process, not necessarily the product of one discrete construction step. It can be the factory state after a period of experience-responsive development, or after a single retained change. Adoption and later use make F' the operative successor.

Under the declared comparison, F' must meet non-regression thresholds on the predecessor's prior scope—including an operative path for producing and improving further factories—and exceed a specified target on at least one relevant dimension of software production. This prevents a one-off gain that consumes the capacity for further improvement.

The comparison is between [deployed systems rather than only model weights](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). The successor may improve through changes to any operative part of its production machinery.

Passing the comparison does not by itself establish learning. The constructors reviewed above show that a capable builder can produce a better factory from supplied specifications, with people holding the production knowledge that matters. The learning claim requires the experience link: retained experience from the predecessor's own production must causally enter the changes the improvement depends on. [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), so the experiments below manipulate that link directly.

## Coherent modification requires held project theory

The hard part of experience-responsive development is changing software and reusable production machinery without silently destroying purposes and organization that immediate acceptance tests capture only partly.

Peter Naur's [1985 essay *Programming as Theory Building*](../sources/programming-as-theory-building.ingest.md) argues that programmers do this by building and holding a project-specific theory: an understanding of how the program maps onto the activity it supports, why it is organized as it is, and how new demands relate to that organization.

Naur's compiler example makes the last capacity especially important. The original group recognized that existing compiler facilities applied to novel modification requests. A later group, despite receiving the program and extensive documentation, proposed locally plausible additions that bypassed those facilities. Access to information was not enough; the relevant connection had to be recognized when the new demand appeared.

The program treats this project-theory requirement as a functional hypothesis to be challenged experimentally, not as a necessity result established by Naur's cases.

This gives a useful distinction. A **retained theory** persists in a recoverable form. A **held theory** is a capability of the theory-bearing system: it recognizes when retained project theory is relevant to a novel demand and brings it to bear without the task author naming the project-specific connection. Modern learned interpreters make Naur's formerly human-only bearer question [empirically open](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

> Can an LLM-based software factory acquire and hold a project theory, revise it in response to evaluation and consequences, and use it to make a later factory state better than its predecessor?

Holding a theory guides search rather than guaranteeing a correct change in one step. The theory can be fallible—partial, provisional, or wrong—while still shaping what changes are considered, what must be preserved, how failures are interpreted, when to backtrack, and what should be revised. The bearer test is longitudinal: whether the system can [sustain coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

Fallibility has a structural source. Acquiring a theory from experience is not only reorganizing information the experience already contains: the theory commits to content the experience does not determine—a mechanism conjectured beyond the observed cases, and resolutions adopted because production needed some choice, not because that choice was judged better. [Commitment, not derivation, creates new ground truth](../notes/commitment-not-derivation-creates-new-ground-truth.md): once committed, such content cannot be recovered from the production record; it can only be revised. That is what makes theory revision a real event in the diagnostic path below rather than a recomputation, and it is why theory mediation is a substantive bet rather than a restatement of retrieval.

## Natural-language theory is the implementation bet

Project theory may be carried in many forms. Natural language is the tested realization because LLMs can interpret it into changes across heterogeneous factory machinery while it remains addressable, inspectable, and revisable.

Natural language also makes the theory directly manipulable in experiments. The same project theory can be retained, withheld, surfaced, corrupted, or replaced while model weights remain fixed. These interventions expose a central failure mode: knowledge may exist in weights or artifacts, and may even appear in the live context, without becoming action-relevant. [Storage and exposure do not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

Such a theory can guide generate-and-verify, program search, and learned policies by allocating search and interpreting failures before decisive evidence is available. Other representations and direct or mixed learning methods are competing approaches and should be compared empirically.

## How to test the program

The first experiment isolates Naurian theory-holding in ordinary software projects. Each project should contain a non-obvious reusable design idea, a novel requirement that can be met either by extending that idea or by adding a local special case, and a later demand that exposes whether the earlier modification preserved the program's [existing organization](../notes/project-theory-relates-new-demands-to-existing-organization.md).

The initial benchmark supplies the project theory to isolate holding and activation. A later acquisition condition starts without it and requires the system to construct and revise project theory from permitted project and production evidence.

The diagnostic path is:

```text
retained theory
  -> held theory under a novel demand
  -> theory-guided modification
  -> later consequence
  -> theory revision
  -> changed later modification
```

A direct probe tests whether the relevant theory is recoverable. An ordinary modification demand tests whether the system recognizes its relevance without a project-specific cue. The recognition test is informative only when the retained corpus is large enough that the relevant theory competes with other retained material; a single design note in a small context would be used almost by default. A mechanism-specific hint then distinguishes failure to recognize relevance from failure to apply the theory. Withholding the theory or replacing it with a plausible but wrong alternative tests whether its content causally changes the modification rather than merely appearing in an explanation. The decisive control is information-matched: a record with the same project facts but without the organizing theory, so that a positive result shows more than that context helps.

A later experiment packages the interleaved process into one attributable episode: after a period of operation, a factory is given the explicit task of constructing a successor. Candidate successors are evaluated under the fixed comparison against the predecessor's prior scope, the target improvement, and their ability to repeat the factory-development process. Evaluation must guide revision of the candidate; an accepted candidate must then be adopted and used in later production and factory development. Two interventions carry the causal claims. Holding model weights fixed isolates the proposed non-weight route. Withholding or supplying the predecessor's retained production record and theory, with the task specification fixed, separates learning from construction: a successor that comes out equally good without the record was built from the specification, not from experience.

The declared comparison has an unresolved oracle problem. Judging a factory's capability over a family is itself expensive, an acceptance test the constructing factory can inspect can be gamed, and if people supply the decisive acceptance judgments, the human-inclusive boundary re-enters at the headline result. The program does not yet have an evaluation design that removes this; it is recorded as an open problem of the second experiment, not a solved part of it.

The program uses two complementary testbeds. **Commonplace** supplies a live, long-horizon human–LLM process for studying theory-holding and revision; the [recorded revision episode](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) illustrates part of the mechanism but is not a controlled better-factory result. Its learning is interleaved in exactly the sense above, which makes it realistic and also raises the evidence cost: attributing an improvement to retained experience requires recording, at production time, which retained state entered which decision—git history alone cannot reconstruct that. A controlled software-project testbed can run the interventions that Commonplace cannot. Current Commonplace evidence is human-inclusive, so progress also means reducing how often the operator must name the relevant theory, choose the decisive branch, or supply another task-specific learning decision.

The program is staged accordingly. In the current phase, the theory's main use is to guide the design of Commonplace itself, and the first experiment is runnable in this phase; the controlled interventions and the successor-factory experiment wait until the system is sound enough to support them. Using the theory to design the system is not yet evidence for the theory, but it produces the testbed in which that evidence can be gathered.

The theory-mediated approach loses support if changing or withholding project theory does not change construction decisions, if another learning mechanism—including plain retention and retrieval of the raw production record—performs better at comparable total cost, or if each new area still requires substantial human-built specialization. The bootstrap fits the Bitter Lesson only if it can [outgrow recurring human-supplied specialization](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).

A successful transition would establish a bounded result: a software factory can turn its own production experience into held project theory strongly enough that a later factory state passes the declared better-than comparison and becomes operative, without training a new model. Indefinite compounding and computational closure would remain open.
