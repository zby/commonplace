# Workshop: Agentic-system learning re-foundation

**Posed by:** the operator, 2026-08-31.

## Intent

Re-found the theory-mediated system-learning research program on a more general
architectural argument. Preserve the existing theory-mediated claims,
experiments, and evidence, but make them downstream of the architecture they
are proposed to improve.

This is not a rewrite around *software factory* or any other new vocabulary.
The argument must remain intelligible if the provisional labels are replaced by
plain descriptions of the machinery and its causal role.

The intended conceptual spine is:

```text
agentic system
  + practical generality over a broad task family
  -> extensible software factory
  + continual learning
  -> learning software factory
  + hard machinery-construction problems
  -> recursive and, where the criteria are met, reflective factory structure
  -> alternative learning mechanisms
  -> theory mediation as a particularly versatile candidate
```

Each `+` introduces an additional premise. None of the arrows is licensed by
terminology alone. The [conceptual spine](./conceptual-spine.md) states the
premises, conclusions, and failure tests in detail.

## Research question

For a sufficiently broad task family, can an agentic system improve how it
constructs and retains the software machinery used to solve later tasks? If so,
does natural-language theory provide a particularly versatile way to organize
evidence and translate it into heterogeneous changes to that machinery?

The first question establishes the learning architecture. The second is the
research proposal. A negative answer to the second must not undo the first.

## Direction fixed by the operator

### Start from the agentic system

Use a modest minimal architecture: bounded LLM calls operate with persistent
software machinery outside the calls. The machinery may schedule calls, retain
state, assemble context, expose tools, execute transitions, and check results.
The [bounded-context orchestration
model](../../notes/bounded-context-orchestration-model.md) and
[scheduler–LLM separation](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
support this separation without proving that one scheduler design is mandatory.

The starting point does not require the software substrate to learn or modify
itself. A fixed and universal substrate remains possible in principle.

### Derive the software-factory role from practical generality

For a sufficiently broad task family, it is unrealistic to predefine every
useful schema, workflow, decomposition, validator, algorithm, representation,
tool, and coordination structure. When the agent constructs such software
machinery for its own work, the agentic system is functioning as a software
factory in the sense relevant to this program. The machinery may initially be
task-local; cross-task retention enters only with the continual-learning step.

This is a practical generality claim, not a logical necessity claim. It does
not say that every agentic system is a software factory, that no fixed universal
substrate could exist, or that Greenfield's family-specific software-factory
ontology must define the research program. The relation between the plain
architectural role and that narrower historical vocabulary remains a question
for the supporting notes.

### Add continual learning independently

Use the minimal cross-task condition: experience on earlier tasks changes how
later tasks are solved. Persistent changes may live in model weights, retrieved
memories, natural-language artifacts, symbolic software, or mixtures. The
software substrate is therefore part of the possible learning surface, not
merely fixed support around model learning.

Stronger claims remain separate. An improvement attribution needs an objective
and evidence that the change helped. Self-improvement, computational closure,
warrant, and autonomy each add further causal or evaluative requirements. Do
not build those stronger requirements into the minimal continual-learning
premise.

### Derive the learning and reflective factory

When the agent constructs software machinery, retains a successful change, and
later work depends on it, the production machinery has learned in the minimal
cross-task sense. Decompositions, context-management strategies,
representations, evaluators, search procedures, tools, and coordination
structures become examples of learnable production machinery. They are not
foundational assumptions.

Introduce recursion only when constructing useful machinery is itself a task
that needs constructed machinery. Introduce reflection only when a causally
connected representation of the factory's own relevant organization
participates in changing later operation. A factory that emits factory-valued
artifacts is not reflective merely because the word *factory* recurs.

### Compare learning mechanisms before proposing theory mediation

At the learning-factory stage, compare trial and error, trajectory reuse,
program search, learned policies, optimization, theory mediation, and mixtures.
The list is provisional rather than an exhaustive taxonomy.

The positive research claim is narrower: natural-language theory may be
unusually versatile because one LLM-interpretable medium can represent task
structure, solver limitations, failure explanations, proposed interventions,
and evidence, then guide heterogeneous changes to software machinery. This is a
comparative hypothesis to test, not a premise used to derive the architecture.

## Explicit non-goals

- Do not claim that theory mediation is necessary, universally superior, or
  sufficient for general learning.
- Do not claim that every agentic system must construct software machinery.
- Do not infer practical breadth, improvement, warrant, autonomy, or closure
  from the presence of a loop or from software authorship alone.
- Do not require universal self-modification. Fixed general machinery,
  interfaces, objectives, resource controls, or trusted kernels may remain.
- Do not equate recursion, factory-valued production, reflection, learning,
  self-improvement, and compounding.
- Do not let a historical software-factory definition carry the broad-task
  generality argument by stipulation.
- Do not discard existing theory-mediated material merely because its
  argumentative position changes.

## Relationship to the existing workshop

The [theory-mediated self-improvement series
workshop](../theory-mediated-self-improvement-series/README.md) remains active.
This workshop does not close, delete, rename, or silently supersede it.

The old workshop continues to own its source controls, accepted and rejected
drafts, ledgers, completed investigations, and current account of the
theory-mediated program. This workshop owns the new architectural derivation
and the decisions about how existing material should be repositioned. The
[transition map](./transition-map.md) records those decisions without moving
anything yet.

Later transfer uses four dispositions:

- **carry downstream unchanged** — the claim remains sound but no longer opens
  the argument;
- **revise dependency or scope** — the claim survives after its premise or
  strength is corrected;
- **split** — a general architectural claim and a theory-specific claim need
  separate homes; or
- **retire after replacement** — the old formulation disappears only after its
  durable contribution has a validated successor.

Until the foundational notes settle the arrows, do not restructure the main
article. At the time this workshop was commissioned, the article and several
software-factory notes had unrelated in-flight edits in the shared worktree.
Inspect current diffs and establish ownership before editing any of them.

## Implementation sequence

1. **Write or revise the supporting theory notes.** Give each arrow in the
   spine an independent argument. Prefer a small number of notes organized by
   argumentative job rather than one note per new noun.
2. **Adversarially check the derivation.** Remove the theory-mediation premise
   and confirm that the learning-factory architecture still follows. Remove the
   software-factory label and confirm that the practical argument still makes
   sense. Check fixed-substrate, non-reflective learning, one-off generated
   code, and factory-valued-but-inert counterexamples.
3. **Survey alternative learning mechanisms.** Compare what state each changes,
   how experience controls the change, how the result becomes operative, and
   what it costs. Do not arrange the mechanisms as a ladder with theory at the
   top.
4. **Restructure the research-program article.** Make the article follow the
   architectural spine. Preserve the strongest existing theory-mediated
   material as the downstream proposal, experiment, and evidence sections.
5. **Disposition the old workshop.** Move or promote only after every retained
   artifact has a destination and the old source-handling constraints have been
   honored. Close the old workshop in a later, explicit step.

The sequence fixes dependencies, not exact filenames, article headings, or the
number of notes. Live evidence may change the implementation within these
bounds.

## Evaluation

The re-foundation succeeds only if a skeptical reader can recover the following
argument without accepting the theory-mediation hypothesis:

1. bounded model calls rely on consequential persistent software machinery;
2. broad practical generality creates pressure to construct task-appropriate
   machinery rather than predefine all of it;
3. cross-task experience can persist by changing that machinery;
4. changes to machinery-construction machinery create the higher-order
   factory structure; and
5. several learning mechanisms could drive those changes.

The theory-mediation proposal then earns its place by making a positive,
testable comparative claim. Useful evidence includes matched tasks where a
theory-mediated condition and credible alternatives receive comparable
information and budgets; interventions on retained theory; heterogeneous
software changes traced to the mechanism; delayed or cross-task consequences;
and failures that expose where natural-language theory adds cost, distortion,
or no advantage.

Terminology passes only when it compresses an already established relation.
If replacing *software factory*, *learning factory*, or *reflective factory*
with its plain causal description changes the argument, the derivation is not
ready.

## Current working material

- [Conceptual spine](./conceptual-spine.md) — dependency ledger and
  counterexamples for the new argument.
- [Transition map](./transition-map.md) — provisional disposition of current
  notes, articles, and old-workshop records; no files have moved.
- [The deployed system, not the model alone, is the unit of
  learning](../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
  — current support for putting software machinery inside the learning
  boundary.
- [Orchestration strategies and run-state have opposite persistence
  economics](../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md)
  — concrete case where a constructed control strategy can be retained for
  later tasks.
- [Learning inside a fixed decomposition inherits its
  mistakes](../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md)
  — pressure to make some task-specific production choices constructible.
- [Reflective system](../../notes/definitions/reflective-system.md) — the
  criterion that prevents recursion or self-production from being mislabeled as
  reflection.
- [A research program for theory-mediated system
  learning](../../articles/a-research-program-for-theory-mediated-system-learning.md)
  — eventual article target, deliberately held behind the supporting-note gate.

## Hand-back conditions

Return to the operator before changing the researcher-facing purpose, making a
necessity or universal-superiority claim for theory mediation, choosing a
historical terminology that materially narrows the intended architecture,
discarding a load-bearing old-workshop result without a successor, or creating
an external research commitment.

## What closes this workshop

The workshop closes when:

1. durable supporting notes carry every arrow in the conceptual spine without
   circular dependence on theory mediation or on a software-factory label;
2. the relation among minimal continual learning, improvement,
   self-improvement, reflection, recursion, closure, and compounding is explicit
   enough to classify the main counterexamples;
3. alternative learning mechanisms are represented fairly and the positive
   theory-mediation hypothesis is testable against credible rivals;
4. the research-program article has been restructured around the derived spine,
   with existing theory-mediated material preserved downstream where it remains
   warranted;
5. every old-workshop artifact has a recorded disposition, its durable outputs
   validate in their receiving collections, and the old workshop can be closed
   separately without loss; and
6. the resulting research surface states the fixed-substrate possibility and
   the theory-mediation non-goals plainly.

Article completion without the supporting derivation does not close the
workshop.
