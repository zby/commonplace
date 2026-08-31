---
description: "DreamCoder shows how an executable program library and neural recognition model jointly reshape later search within a fixed wake-sleep architecture."
source: https://arxiv.org/abs/2006.08381
captured: "2026-08-31"
capture: pdftotext
capture_scope: full-source
capture_url: https://arxiv.org/pdf/2006.08381
genre: scientific-paper
snapshot_sha256: 8d056c1f2216a33a5be196cc7253d95a6d81955b8cb640bcf330163a7028b7a9
ingested: "2026-08-31"
occasion: "Determine what this source establishes about learning reusable executable abstractions that restructure later search, including the relation between the learned library and learned search guidance. Distinguish reusable program knowledge from a theory of the learner's own purposes, architecture, or improvement machinery."
type: kb/sources/types/ingest-report.md
domains: [program-induction, library-learning, search-guidance, neuro-symbolic-learning]
---

# Ingest: DreamCoder: Growing Generalizable, Interpretable Knowledge

## Classification

This is a scientific paper: it specifies a probabilistic model and wake-sleep learning algorithm, then evaluates the system with held-out tasks, component ablations, and baselines across several program-induction domains. Author: Kevin Ellis and collaborators from MIT, CSAIL, NeuroSpin, and the Center for Brains, Minds, and Machines, with prior work in program synthesis, probabilistic program induction, and cognitive modeling.

## Summary

DreamCoder jointly learns two forms of domain expertise across repeated program-induction tasks. Its explicit symbolic library is a generative prior over programs; an abstraction phase searches semantic refactorings of solved programs and retains routines that improve a Bayesian description-length objective. Its distributed-parametric recognition model predicts task-conditioned program distributions; a dreaming phase trains it on replayed solutions and library-generated fantasies so it can guide later enumeration. Library routines shorten solution programs and thereby reduce search depth, while recognition guidance concentrates probability on promising construction choices and thereby reduces effective search breadth. Experiments across list processing, text editing, graphics, tower building, generative text, symbolic regression, functional programming, and physics show learned reusable routines, improved held-out task solving, and performance losses when either library learning or recognition learning is removed.

## Quotes

No source quotes have been retained yet.

## Connections Found

The full paper is a technical basis for [representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md): an executable symbolic library and a distributed-parametric recognition model change different dimensions of later search and bootstrap one another. It also sharpens the [proposal-selection loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), because candidate library routines are searched, scored by a Bayesian description-length criterion, and installed into the prior, whereas recognition guidance is updated directly by gradient training. As bounded evidence for [theory-mediated learning](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md), the retained routines mediate later induction, but the experiments do not test the note's structured distribution shifts. Read through the [fixed-decomposition boundary](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), the gains support learning within supplied task interfaces, representation languages, objectives, and phase structure rather than those fixed choices themselves.

## Extractable Value

1. **Executable abstractions become operative search structure.** The abstraction phase does not merely archive solved programs: it refactors them, selects reusable routines under a Bayesian description-length objective, and adds accepted routines to the library prior used in later wake search. This is direct evidence that learned reusable program knowledge can alter which later solutions are short enough to find. [quick-win]
2. **The library and search guidance reshape different search dimensions.** Higher-level library routines shorten construction trajectories, while the recognition model lowers the effective branching entropy by assigning task-conditioned probability to program components. Keeping the depth and breadth effects separate makes the coevolution claim mechanistic rather than a generic appeal to hybrid neuro-symbolic learning. [quick-win]
3. **The two learned forms participate in distinct but coupled update loops.** Library growth uses explicit candidate generation, Bayesian/MDL evaluation, and operative retention; recognition learning uses direct gradient updates on replayed and fantasized task-program pairs. The learned library changes the model that generates fantasies, while better guidance yields more solved programs for the next abstraction phase. [quick-win]
4. **The ablations support component contribution, not architectural optimality.** Removing either recognition learning or library abstraction reduces held-out performance, and memorization variants test wholesale reuse against compression-based abstraction. These contrasts support the value of both learned components within DreamCoder, but they do not compare alternative objectives, task decompositions, representation languages, or wake-sleep organizations. [deep-dive]
5. **The retained knowledge is not a theory of the learner itself.** Library entries encode executable regularities in a task domain, and the recognition model encodes task-conditioned search guidance. DreamCoder does not learn its purpose, task source, evaluation criterion, representation architecture, search algorithm, or improvement machinery, nor does it model why those fixed choices should persist. [just-a-reference]
6. **Outgrowing a sparse bootstrap remains conditional on substantial supplied structure and compute.** DreamCoder can derive functional-programming and physics vocabularies from relatively minimal bases, but the bases still include types, control flow, recursion or sequence operations, domain observation interfaces, and fixed learning machinery; the most minimal recursive-programming run consumed about a year of aggregate CPU time. [just-a-reference]

## Limitations (our opinion)

The experiments use curated task sets whose solutions fit crisp symbolic programs, with held-out tests drawn from the same named domains rather than controlled structural distribution shifts. The paper acknowledges that messier real-world data, commonsense reasoning, natural-language understanding, and causal inference require further work. Its claims about general-purpose expertise should therefore be read as breadth across several designed program-induction settings, not evidence of open-ended cross-domain learning.

The effective update space is narrower than the overall system. Behavior can condition on supplied task observations such as input-output examples, images, scenes, or numerical data, plus replayed and fantasized task-program pairs. The learner can compose typed lambda-calculus programs from initial and acquired primitives, search bounded semantic refactorings for compressive routines, and learn task-to-program distributions within a domain-specific neural architecture. The task corpus and interface, initial primitive basis and type system, likelihood and equivalence rules, refactoring bound, enumeration procedure, neural architecture, Bayesian/MDL objective, wake-sleep phase partition, and compute budget remain fixed. Improvement inside that space does not establish that these fixed representations and partitions are necessary, preferable, or revisable by the learner.

The no-dreaming and no-abstraction ablations identify the contribution of the component each removes under the rest of DreamCoder's configuration; they do not isolate every feedback path between components. The reported association between deeper libraries and performance is also correlational. Neither the training runs nor implementation code were independently reproduced for this ingest, and many detailed analyses are deferred to a separate supplement. The paper's analogies to human expertise and biological sleep are motivating interpretations, explicitly not validated biological models.

## Recommended Next Action

Update [Treat continual learning as representational-form coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md) with a bounded DreamCoder evidence case that states the library's search-depth effect, the recognition model's search-breadth effect, their distinct update mechanisms, and the architecture choices fixed outside both learning loops.
