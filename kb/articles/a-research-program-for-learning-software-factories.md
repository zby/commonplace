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
  - kb/notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md
  - kb/notes/open-ended-theory-learning-and-factory-learning-close-the-same.md
  - kb/notes/theory-mediation-can-coordinate-heterogeneous-factory-development.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/notes/project-theory-relates-new-demands-to-existing-organization.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/knowledge-storage-does-not-imply-contextual-activation.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/natural-language-project-state-specializes-search-heuristics.md
  - kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for learning software factories

> **Draft.** Comments and counterexamples are welcome through [the repository's issue tracker](https://github.com/zby/commonplace/issues).

> **TL;DR.** A software factory learns when its production experience causes retained changes to its machinery that later work depends on. This is a causal definition with no quality requirement: a factory can learn badly. Improvement is claimed separately, under a comparison external to the definition of learning: declared in advance, between a later factory state and an earlier one. This program tests whether LLM-based factories can learn from experience and pass that comparison without training new models, by acquiring, holding, using, and revising project theories.

## Better software factories

A [software factory](../notes/definitions/software-factory.md) is a configured production environment containing reusable production knowledge for a declared family of software. Its machinery can include models, prompts, natural-language artifacts, code, tools, workflows, tests, and evaluators.

The software-factory literature already describes factories configured to produce factories as members of their declared family: Greenfield and Short's factory-building factory, Cook and Kent's Tool Factory, and Langlois and Exertier's MDSoFa, a self-described "software factory factory." In [these examples](../notes/factory-construction-does-not-establish-knowledge-acquisition.md), people supply the family definitions, metamodels, mappings, and expertise that determine the produced factory.

The research target is a factory that learns from what it produces. Relative to a declared learner boundary, a factory undergoes [factory-level learning](../notes/factory-learning-retains-experience-in-reusable-machinery.md) when production experience—failures, surprises, evaluations, corrections, delayed consequences—causes a retained change to its reusable production machinery, and later production or factory development depends on that change. The definition is boundary-relative because the same episode can be learning by a human-inclusive composite while remaining externally supplied engineering for the narrower technical subsystem inside it; what counts is what determined the update, not who typed the result.

In current agentic coding systems this learning is interleaved with operation rather than confined to a separate phase. A failed task can immediately cause a note to be written, a test added, a rule revised, a tool changed, and the task retried; [Compound Engineering's retention pathway](../agentic-systems/compound-engineering-plugin.md) works this way. Some of those changes already change the factory. There need be no phase in which an unchanged factory merely accumulates experience before learning begins. The process is a loop, not a pipeline:

```text
production and factory development under the current factory state
  -> experience from that work
  -> retention (project theory, indexes, tests, tools):
     judging what the experience means, organizing it,
     committing where the experience leaves the resolution open
  -> later production and factory-development decisions
  -> further experience, now under the changed factory state
```

Retention in this loop is an act, not storage. The factory judges what a failure means and what is worth keeping, organizes the result so later work can find it, and, where the experience leaves resolutions open, settles them with [explanatory and constructive commitments of the same fallible kind](../notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md) — content the evidence does not entail. Judging here names an act, not a standard. The definition of factory-level learning places no quality requirement on it: a factory whose retained judgements are poor still learns in the defined sense — it learns badly, and can degenerate.

This is the complete occurrence condition for factory-level learning. A particular factory may add internal controls on what it retains or adopts — heuristic self-evaluation, preregistered internal comparisons, up to a proof gate in the style of Schmidhuber's Gödel machine — but these are design choices of the factory, not parts of the definition, and a factory can choose them badly. Even a proof gate certifies only against the axioms it is given.

The program's target is not learning alone but learning that leaves the factory better, and the loop, internal controls included, cannot supply that improvement claim. The program's instrument is a measurement laid over snapshots of the process:

```text
declare the comparison while factory state F is current
  -> intervening production and factory development
  -> factory state F'
  -> compare F' with F under the declared comparison
```

The successor F' is a measurement boundary on a continuous process, not necessarily the product of one discrete construction step. It can be the factory state after a period of experience-responsive development, or after a single retained change; either way it is already the later operative state, and the measurement judges a realized trajectory rather than performing adoption. A factory constructed and evaluated before installation is a different case: a candidate, which becomes the successor only when installed and depended on — the shape the successor-factory experiment below uses. The two cases also separate two human roles: a person who only measures whether a realized change helped stays outside the learner boundary, while one whose judgment controls installation enters the causal update path.

The comparison is declared before the development it judges: its non-regression thresholds and target dimensions are fixed while only F exists, so improvement cannot be claimed on a dimension chosen after seeing F'. Under it, F' must meet non-regression thresholds on the predecessor's prior scope and exceed a specified target on at least one production dimension it names. The factories this program compares keep factory development in their declared scope, so the preserved prior scope includes an operative path for producing and improving further factories. This prevents a one-off gain that consumes the capacity for further improvement.

The comparison is between [deployed systems rather than only model weights](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md). The successor may improve through changes to any operative part of its production machinery.

Passing the comparison does not by itself establish learning. The constructors reviewed above show that a capable builder can produce a better factory from supplied specifications, with people holding the production knowledge that matters. The learning claim requires the experience link: retained experience from the predecessor's own production must causally enter the changes the improvement depends on. [An experiment identifies only the contrast it actually runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), so the experiments below manipulate that link directly.

## Held project theory is the program's hypothesis for coherent modification

The hard part of experience-responsive development is changing software and reusable production machinery without silently destroying purposes and organization that immediate acceptance tests capture only partly.

Peter Naur's [1985 essay *Programming as Theory Building*](../sources/programming-as-theory-building.ingest.md) argues that programmers do this by building and holding a project-specific theory: an understanding of how the program maps onto the activity it supports, why it is organized as it is, and how new demands relate to that organization.

Naur's compiler example makes the last capacity especially important. The original group recognized that existing compiler facilities applied to novel modification requests. A later group, despite receiving the program and extensive documentation, proposed locally plausible additions that bypassed those facilities. Access to information was not enough; [the new demand had to be compared with the program's existing organization](../notes/project-theory-relates-new-demands-to-existing-organization.md).

The research program treats the project-theory requirement as a functional hypothesis to be challenged experimentally, not as a necessity result established by Naur's cases.

This gives a useful distinction. A **retained theory** persists in a recoverable form. A **held theory** is a capability of the theory-bearing system: it recognizes when retained project theory is relevant to a novel demand and brings it to bear without the task author naming the project-specific connection. Modern learned interpreters make Naur's formerly human-only bearer question [empirically open](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

> Can an LLM-based software factory acquire and hold a project theory, revise it in response to evaluation and consequences, and use it to make a later factory state better than its predecessor?

Holding a theory guides search rather than guaranteeing a correct change in one step. The theory can be fallible—partial, provisional, or wrong—while still shaping what changes are considered, what must be preserved, how failures are interpreted, when to backtrack, and what should be revised. The bearer test is longitudinal: whether the system can [sustain coherent search under delayed feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

Fallibility has a structural source: experience underdetermines what should be retained. Not every retained change resolves this. An index or a summary is derived organization, rearranging evidence the production record already contains and regenerable from it. Acquiring a theory does more: it commits to content the experience does not determine—a mechanism conjectured beyond the observed cases, and resolutions adopted because production needed some choice, not because that choice was judged better. Machinery changes that select a design among live alternatives [make the same kind of fallible commitment](../notes/theory-and-capacity-building-make-the-same-kind-of-commitment.md). The classification is per resolution, not per artifact: one retained test can bundle a derived reproduction of an observed failure with a constructive commitment about what later behavior must hold.

[Commitment, not derivation, creates new ground truth](../notes/commitment-not-derivation-creates-new-ground-truth.md): once committed, such content cannot be authoritatively re-derived from the production record — a later system may rediscover the same resolution, but by fresh judgment, not recomputation — and retaining it makes it the current working account, not a truth. Retracting a constructive commitment means restructuring what was built on it—refactoring at small scale, redesign at large—rather than revising an account. That is what makes theory revision a real event in the diagnostic path below rather than a recomputation or a rebuilt index, and it is why theory mediation—routing production and factory development through a held project theory—is a substantive bet rather than a restatement of retrieval.

## Natural-language theory is the implementation bet

Project theory may be carried in many forms. Natural language is the first tested realization. The working hypothesis behind that choice—not an established comparative result—is that an LLM can [use one account to coordinate changes across heterogeneous factory machinery](../notes/theory-mediation-can-coordinate-heterogeneous-factory-development.md) while the account remains addressable, inspectable, and revisable.

Natural language also makes the theory [directly manipulable in experiments](../notes/retained-theory-intervention-isolates-one-explicit-surface.md). The same project theory can be retained, withheld, surfaced, corrupted, or replaced while model weights remain fixed. These interventions expose a central failure mode: knowledge may exist in weights or artifacts, and may even appear in the live context, without becoming action-relevant. [Storage and exposure do not imply contextual activation](../notes/knowledge-storage-does-not-imply-contextual-activation.md).

Such a theory may [specialize search heuristics already represented in the model](../notes/natural-language-project-state-specializes-search-heuristics.md): it can steer which candidate changes are generated, how failures are interpreted, and where search effort goes before decisive evidence is available. Other representations and direct or mixed learning methods are competing approaches and should be compared empirically.

## How to test the program

Two staged experiments carry the program's causal claims, and two testbeds host them.

### Experiment one: theory-holding and acquisition

The first experiment isolates theory-holding—recognizing and applying retained project theory without a project-specific cue—in ordinary software projects. Each project should contain a non-obvious reusable design idea, a novel requirement that can be met either by extending that idea or by adding a local special case, and a later demand that exposes whether the earlier modification preserved the program's [existing organization](../notes/project-theory-relates-new-demands-to-existing-organization.md).

The initial benchmark supplies the project theory to isolate holding and activation. A later acquisition condition starts without it and requires the system to construct and revise project theory from permitted project and production evidence. Acquisition is tested by the same probes as holding: the constructed theory must be recoverable, must change the system's modifications when withheld or replaced, and must be revised when its consequences arrive.

The diagnostic path is:

```text
retained theory
  -> held theory under a novel demand
  -> theory-guided modification
  -> later consequence
  -> theory revision
  -> changed later modification
```

A direct probe tests whether the relevant theory is recoverable. An ordinary modification demand tests whether the system recognizes its relevance without a project-specific cue. The recognition test is informative only when the retained corpus is large enough that the relevant theory competes with other retained material. A single design note in a small context would be used almost by default. A mechanism-specific hint then distinguishes failure to recognize relevance from failure to apply the theory. Withholding the theory or replacing it with a plausible but wrong alternative tests whether its content causally changes the modification rather than merely appearing in an explanation. The strongest current control is fact-matched: it supplies the same atomic project propositions without their theory-level organization, so a positive result shows more than that context helps. The relations, purposes, and scope conditions it removes are themselves information, so this arm identifies the contribution of the supplied organization as a bundle, not of an abstract category called theory; sharper attributions need finer contrasts, such as shuffling the relations or corrupting one controlled premise and predicting the specific later failure before the run.

Experiment one is a component test of the theory-holding function on ordinary program modification: the modified object is a single product, so it does not yet establish factory-level learning. That requires the object of modification to be the factory's own reusable production machinery, which is what the second experiment supplies.

### Experiment two: the successor factory

A later experiment packages the interleaved process into one attributable episode: after a period of operation, a factory is given the explicit task of constructing a successor. Candidate successors are evaluated under the fixed comparison against the predecessor's prior scope, the target improvement, and their ability to repeat the factory-development process. Evaluation must guide revision of the candidate; an accepted candidate must then be adopted and used in later production and factory development. Three contrasts carry the causal claims, all with model weights fixed to isolate the proposed non-weight route and the task specification held constant. Supplying versus withholding the predecessor's whole retained state — production record and theory together — separates learning from construction: a successor that comes out equally good without it was built from the specification, not from experience. Supplying the production record with versus without the distilled theory separates theory mediation from direct record reuse: it identifies what the theory surface adds beyond access to the raw record. Replacing the correct theory with a controlled wrong one, record unchanged, tests content-sensitive steering rather than the mere presence of a theory-shaped artifact.

The declared comparison has an unresolved oracle problem: the program has no trustworthy mechanism for deciding whether a successor is genuinely better. Each candidate mechanism fails in its own way. Judging a factory's capability over a family of software is expensive. An acceptance test the constructing factory can inspect can be gamed. And if people supply the decisive acceptance judgments, the human-inclusive boundary re-enters at the headline result. The program does not yet have an evaluation design that removes this; it is recorded as an open problem of the second experiment, not a solved part of it.

### Testbeds and staging

The program uses two complementary testbeds, and they enter the loop from opposite ends. **Commonplace**—the agent-operated knowledge-base framework this program is developed in, [used here as an instrument](../reference/commonplace-as-an-instrument.md)—enters from the theory side. Its operative machinery so far is theory machinery—writing, grounding, review, revision—and the family it produces is methodology and knowledge artifacts; production machinery for software does not yet exist here. It supplies a live, long-horizon human–LLM process for studying theory-holding and revision; the [recorded revision episode](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) illustrates part of the mechanism but is not a controlled better-factory result. Its learning is interleaved in exactly the sense above, which makes it realistic and also raises the evidence cost: attributing an improvement to retained experience requires recording, at production time, which retained state entered which decision—git history alone cannot reconstruct that. The controlled software-project testbed enters from the factory side—working software projects into which retained theory is supplied, withheld, or replaced—and can run the interventions that Commonplace cannot. Current Commonplace evidence is human-inclusive—the declared learner boundary includes the operator—so progress also means reducing how often the operator must name the relevant theory, choose the decisive branch, or supply another task-specific learning decision.

The program is staged accordingly. In the current phase, the theory's main use is to guide the design of Commonplace itself. Experiment one can run now in the controlled software-project testbed; controlled interventions on the live Commonplace process, and the successor-factory experiment, wait until the system is sound enough to support them. Using the theory to design the system is not yet evidence for the theory, but it produces the testbed in which that evidence can be gathered.

## What would count against the program

The theory-mediated approach loses support if changing or withholding project theory does not change construction decisions, if another learning mechanism—learned policies, trajectory reuse, direct structural search, or plain retention and retrieval of the raw production record—performs better at comparable total cost, or if each new area still requires substantial human-built specialization.

The last condition is where Richard Sutton's essay [*The Bitter Lesson*](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) bears. The program's hand-built starting state—its theories, benchmarks, and declared comparisons—is a bootstrap: the running system uses its current machinery to guide the search that produces later versions, rather than being scaffolding someone rebuilds for each new area. Sutton's essay argues that approaches built on human-supplied domain knowledge are eventually overtaken by general methods that use computation and learning, and calling the starting state a bootstrap does not by itself answer it: the bootstrap fits the lesson only if it can [outgrow recurring human-supplied specialization](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md). A [companion article](the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) argues the lesson does not require all learning to live in model weights.

## The reflective loop behind the program

The program's central bet can also be reached from two directions inside its own theory. [Open-ended theory learning and factory learning close the same reflective loop](../notes/open-ended-theory-learning-and-factory-learning-close-the-same.md) derives that loop from both ends: a factory that improves coherently past shallow patching needs a held, revisable theory of its own organization, and testing a theory about a system's own organization depends on making it operative in that system's machinery. The convergence is internal coherence, not external confirmation—the derivations share the program's premises and assume delayed, partial evaluation—and it argues what the loop would require, not that any current system closes it. The derivation also commits to the same rival the loss conditions above name—plain retention and retrieval of the raw production record—so the same evidence would count against both. The program's testbeds enter this loop from its two ends: Commonplace from theory learning, the controlled testbed from factory learning. That gives the theory-side derivation a prediction about Commonplace's own trajectory: the theory retained here is largely about factory learning, and by the derivation it can be tested only by becoming operative in machinery that acts on it—so the missing software-factory machinery should be forced into existence as retained theory demands consequences. If theory can instead accumulate and revise here indefinitely without forcing that machinery into existence, the derivation loses support in its own testbed. The same note places Schmidhuber's proof-gated Gödel machine as a contrast case rather than a maturity endpoint: it keeps its axiomatized self-description and utility function fixed as premises of every rewrite rather than acquiring or revising them from production experience—the supplied-and-fixed corner of the design space this program bets against.
