---
description: "Research program on whether an agentic software-production system can learn reusable production machinery and whether natural-language theory improves that learning"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/bounded-context-orchestration-model.md
  - kb/notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md
  - kb/notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
  - kb/notes/a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md
  - kb/notes/an-agentic-substrate-becomes-a-software-factory-through-family-specific-production-machinery.md
  - kb/notes/task-families-and-product-families-classify-different-things.md
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
  - kb/notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  - kb/notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/natural-language-project-state-specializes-search-heuristics.md
  - kb/notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md
  - kb/notes/open-ended-improvement-allocates-search-before-evaluation.md
  - kb/notes/lightweight-search-control-does-not-license-adoption.md
  - kb/notes/backtracking-keeps-lightweight-search-control-provisional.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/sources/programming-as-theory-building.ingest.md
---

# A research program for learning software factories

> **Draft.** Comments and counterexamples are welcome through the repository's issue tracker.

> **TL;DR.** An agentic system is more than an LLM call: bounded model calls operate inside persistent software machinery. For software production, configuring that machinery with reusable knowledge for a declared product family yields a software factory. When production experience changes reusable factory machinery and later work depends on the change, the factory learns. Several mechanisms could drive that learning. This program tests whether natural-language theory is unusually versatile because it can connect task structure, solver limits, failures, evidence, and coordinated changes across prompts, schemas, workflows, tools, evaluators, and code.

## From agentic systems to learning software factories

An LLM call is bounded. It receives a finite context, produces a finite result,
and does not by itself provide durable state, exact iteration, tool execution,
permissions, aggregation, or long-horizon continuity. Agentic systems obtain
those capabilities from software surrounding the calls.

The [bounded-context orchestration
model](../notes/bounded-context-orchestration-model.md) makes one such
architecture explicit: symbolic state and transitions organize repeated bounded
calls. The [scheduler–LLM
separation](../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)
explains why exact progression and bookkeeping often belong in software rather
than accumulated natural-language context. Semantic interpretation can remain
model-mediated while code performs transitions that are cheaper to check than
to regenerate correctly on every call.

This starting point does not require the software to learn or modify itself. A
fixed, sufficiently general substrate could in principle express every useful
workflow and program.

### Family-specific production knowledge configures a factory

For software production, Greenfield's ontology supplies a more precise boundary
than the loose modern factory metaphor. A [software
factory](../notes/definitions/software-factory.md) is a configured,
family-specific production environment for a declared family of software
products or solutions. Its reusable production knowledge is distributed across
a schema, packaged assets, processes or guidance, tools, frameworks, tests, and
lifecycle support.

The mapping is:

```text
general agentic substrate
  + declared software product or solution family
  + reusable family-specific production knowledge
  -> configured agentic software factory
```

A generic coding agent, IDE, or harness is not yet a Greenfield-style factory.
Nor is every script or orchestrator generated during one task. Task-local
software becomes factory machinery only when it carries reusable production
knowledge for a declared family or admitted variation space. The [agentic
substrate mapping](../notes/an-agentic-substrate-becomes-a-software-factory-through-family-specific-production-machinery.md)
develops this boundary.

A [task family and a product
family](../notes/task-families-and-product-families-classify-different-things.md)
also classify different things. A benchmark may group tasks because they stress
the same solver capability. A product family groups software systems through
declared commonality, variability, and reusable production machinery. One
product may generate many tasks, and one task family may span many unrelated
product families.

### Broad demands create pressure for factory development

[Factory development](../notes/definitions/factory-development.md) constructs or
revises reusable family-level production machinery. Solution development uses
that machinery to create and sustain one family member.

As the covered software demands widen, it becomes increasingly implausible that
every useful decomposition, representation, workflow, tool, evaluator, context
policy, test, and recovery procedure will be supplied in advance. Novel
requirements and environments expose missing or mistaken production knowledge.
A general agentic system should therefore be able to participate in factory
development when its installed family machinery is inadequate.

This is a practical conjecture, not a necessity theorem. A fixed universal
substrate remains a live counterhypothesis. The burden is empirical: does
agentic construction of production machinery reduce recurring target-specific
human work and improve transfer at acceptable total cost? [Broad software
demands create this pressure](../notes/broad-software-demands-create-pressure-for-agentic-factory-development.md)
without requiring every fixed component to become self-modifying.

Recursive factory construction is not the novelty. Greenfield, Tool Factory,
and MDSoFa already describe factories or tool factories producing further
production machinery. In those cases, people still supply the family
definition, metamodels, mappings, frameworks, or expertise that determine the
target. [Constructing a factory from supplied family-specific production
knowledge is not acquiring that
knowledge](../notes/a-software-factory-can-produce-another-factory-without-acquiring-its-family-specific-production-knowledge.md).

### Continual learning changes later production

Software production and factory development do not by themselves imply
learning. The minimal factory-level learning path is:

```text
production under current factory machinery
  -> experience bearing on that machinery
  -> system-determined change to reusable family machinery
  -> retention
  -> changed later production
```

Experience without a reusable change is feedback. Repairing only the current
product is solution development. A generated candidate that is discarded does
not persist. Stored machinery that later production never consumes has no
demonstrated learning effect.

When the whole path is present, [the software factory
learns](../notes/a-software-factory-learns-when-production-experience-changes-reusable-machinery-used-later.md)
in a minimal cross-episode sense. The change need not be beneficial. Improvement,
warrant, computational closure, reflection, autonomy, and compounding add
separate claims.

The [deployed system rather than the
model](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) is
the relevant learning boundary. Retained changes may live in weights,
natural-language artifacts, symbolic software, retrieved memories, or mixtures.
The factory-level subset changes reusable production machinery.

## Theory mediation is one candidate mechanism

Factory-level learning does not require theory. Trial-and-error retention,
trajectory reuse, program search, learned construction policies, direct
optimization, and mixtures can all turn experience into later production
changes. They should be [compared on the same causal
job](../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md),
not ranked by whether their state is readable or whether it lives in weights.

The proposal tested here is narrower:

> Natural-language theory may be an unusually versatile coordination mechanism
> for learning heterogeneous production machinery.

A factory-relevant theory can jointly represent:

- task and domain structure;
- relevant capacities and limitations of the current solver;
- explanations of successes and failures;
- proposed interventions and their intended mechanisms;
- scope conditions and predictions; and
- evidence that should revise or defeat the account.

An LLM can interpret that state into changes across decomposition, context
selection, schemas, workflows, prompts, tests, evaluators, tools, and code. The
same explanation can coordinate several artifacts rather than leaving each to a
separate local update process.

The relevant self-knowledge is not a complete account of model internals. A
decomposition is relative to both a task and a solver: it must preserve the
task's dependencies while producing units that this system can execute, retain,
combine, and verify. Theory-mediated decomposition therefore needs a
task-relevant model of the task–solver relation and of interventions that can
make the task tractable.

Theory does not replace search. It can shape a generate-and-verify process by
controlling which failure explanations are plausible, which machinery is worth
changing, which candidates to try, which experiments are informative, and how
outcomes should revise the retained account. Blind exploration, learned
policies, program search, exact code execution, and independent tests can remain
inside the same system.

The claim is causal. A theory that merely accompanies the work is documentation.
Theory mediation requires the retained theory to change search, diagnosis,
evaluation, recovery, or revision. The supporting note states why [theory may
coordinate heterogeneous factory
development](../notes/theory-mediation-can-coordinate-heterogeneous-factory-development.md)
and what comparative results would support or defeat that claim.

## Naur's bearer question and the two testbeds

Peter Naur's [1985 essay *Programming as Theory
Building*](https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf)
argues that programmers do more than produce code. They build and hold a
project-specific theory: an understanding of what the program must do, why it is
organized as it is, and how that organization can survive new demands.

Naur treated this theory as something held by programmers rather than by the
program or its documentation. The machine could execute what had been
formulated, but the theory needed for coherent modification remained with
people—a boundary grounded partly in [Naur's equation of machine execution with
formulated
criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md).

Modern agentic systems make that boundary worth testing. Their learned
competence comes partly from model weights, while retained project state, tools,
schemas, tests, and runtime machinery determine what happens in a particular
project.

> Can such a system become a bearer of a fallible project theory—holding and
> revising it well enough to keep successive modifications coherent when
> decisive feedback arrives only later?

The program couples a live testbed with a prospective controlled one.

**Commonplace** is the live human-agent testbed. Agents use retained theory to
revise the knowledge base, software, and methodology that guide later work. The
operator still supplies much global-fit judgment and final authorization. This
makes the human-inclusive learning path visible and exposes which recurring
judgments might become reusable machinery.

The **programming-agent testbed** will place a persistent, fallible theory inside
an agentic software-production system and give it a sequence of modifications
whose later demands can expose earlier mistakes. It is the direct test of
whether theory changes factory-development choices and coherent modification.
Matched runs will vary the theory while holding specified background components
fixed.

## Holding a theory means controlling a fallible search

Naur's test is longitudinal. A coherent modification meets a new demand without
destroying the purpose and organization that make the program work. Because
those are only partly stated, a later demand may expose damage caused by an
earlier locally successful change.

The unit judged is therefore a sequence, not one patch. A failed first candidate
can belong to coherent modification when the process recognizes the failure and
recovers. A successful first candidate can fail when it passes narrow checks but
damages the wider organization in a way the process cannot detect. [Holding a
program theory means sustaining coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md).

Program-relevant understanding may extend beyond the retained theory surface.
The controlled experiment varies one addressable surface while holding specified
background components fixed. It tests the causal contribution of that surface,
not whether the surface exhausts the system's whole program theory, [as the
retained-theory intervention note makes
explicit](../notes/a-retained-theory-intervention-isolates-one-explicit-theory-surface.md).

Theory matters before a correct answer is available. [Open-ended improvement
must allocate search before decisive evaluation
exists](../notes/open-ended-improvement-allocates-search-before-evaluation.md).
Retained theory can focus work and guide recovery by exposing commitments a
local fix must preserve.

Generic search can also generate and test patches. One possible theory mechanism
is that [natural-language project state specializes search heuristics already
present in model
weights](../notes/natural-language-project-state-specializes-search-heuristics.md).
The empirical question is whether that specialization improves the sequence at
comparable information and total cost.

Theory-guided choices need not all meet the standard for final adoption.
[Lightweight search controls](../notes/lightweight-search-control-does-not-license-adoption.md)
can allocate work under weaker evidence, while [backtracking keeps them
provisional](../notes/backtracking-keeps-lightweight-search-control-provisional.md)
when contrary evidence arrives.

## What counts as theory-mediated learning

The strongest path the program wants to observe is:

```text
retained theory
  -> theory-mediated search or factory-development decision
  -> realized change
  -> independent or delayed consequence
  -> read-back against the same theory
  -> retained theory-state revision
  -> changed later operation
```

The evidence ladder distinguishes four levels:

1. **Mediation:** changing or withholding theory changes a consequential
   decision or intervention.
2. **Empirical contact:** the intervention produces an outcome that bears on the
   theory.
3. **Theory learning:** the outcome changes the retained theory's content, scope,
   or operational force.
4. **Recurrence:** the updated theory changes a later operation on the same
   behavior-determining path.

A [citation at the decision point is a mediation
trace](../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md),
not proof that the theory was load-bearing. Withholding, replacement, or
perturbation is stronger evidence. The higher levels must also belong to one
causal path. Separate witnesses for theory use, outcome, revision, and later work
do not compose automatically, [because disconnected witnesses do not establish
a full path through
theory](../notes/disconnected-witnesses-do-not-establish-a-full-causal-path-through-theory.md).

### Four functional roles

The current design separates four roles because they have different failure
modes and support different interventions.

| Functional role | Current realization | Typical failure |
|---|---|---|
| Retained project state | Addressable theory and other persistent artifacts | Omission, contradiction, drift, or retrieval failure |
| Model-mediated semantic operation | Model weights applied to call-specific context | Theory ignored, misapplied, or rationalized after the fact |
| Independently executed symbolic operation | Code and runtime carrying exact transitions and continuity | Exact execution of the wrong transition or a path that ends too early |
| Independent exposure and read-back | Tests, later consequences, and operator judgment | Weak or captured evaluation, delayed credit assignment, or exogenous selection |

These are roles, not permanent carriers. The same artifact can be read as
evidence in one path and executed as an instruction in another. Its role follows
how it is consumed, not who authored it. Exact execution does not establish that
the encoded requirement or theory is correct.

The table also exposes the present actor allocation. The operator still supplies
much independent global-fit judgment and authorization. Moving recurring parts
of that work into reusable machinery is a bootstrap target, not a completed
autonomy claim.

## Warrant and fit are different evaluations

A well-warranted claim can fit a working theory poorly. It may be irrelevant,
badly scoped, or incompatible with other commitments. Conversely, a weak claim
can appear useful because the current implementation already assumes it. [A
claim's warrant therefore does not determine its fit in a working
theory](../notes/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md).

No present automatic evaluator fully decides global fit. Consequences of live
use and comparisons with rival theories provide an [initial selection
environment](../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md),
but not an independent truth oracle. [System use provides evidence of theory
fit and causal usefulness, not independent
warrant](../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md).
Independent factual and formal checks, held-out demands, rival theories, and
later consequences remain necessary to prevent a self-confirming loop.

## Current evidence and next tests

The [2026-08-30 Commonplace revision
record](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)
illustrates part of the proposed path: retained theory guided the work, operator
feedback revised it, and the result affected later work. The episode was not
recorded prospectively enough for causal or comparative attribution.

Future consequential episodes should preserve the joins of the causal path,
including which theory state guided a decision, which consequence bore on it,
which revision was retained, and which later operation consumed that revision.
For nondeterministic production, missing joins cannot reliably be reconstructed
after the fact.

### Controlled programming-agent test

The minimum controlled test compares:

- usable retained theory;
- theory withheld;
- plausible but wrong theory; and
- an information-matched factual record when testing explanatory organization.

The base model, starting machinery, task sequence, protocol, and budget should
be matched across conditions; machinery changes are outcomes. A factory-learning
result additionally requires changed reusable machinery to affect later
production. Later demands must be able to expose mistakes introduced by earlier
locally successful modifications.

The primary questions are:

- Does theory change search allocation, decomposition, tool construction, or
  recovery?
- Do later consequences revise the same retained theory surface?
- Does that revision change later work?
- Does theory improve coherent modification, transfer, or total recovery cost?
- Does it outperform credible trajectory, search, policy, optimization, or mixed
  alternatives at comparable total cost?

Any result identifies only [the contrast it actually
runs](../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).
A theory-versus-no-theory result does not rank every alternative learning
mechanism.

### Longitudinal Commonplace study

Commonplace should record consequential revisions prospectively and ask whether:

- recurring operator judgments become reusable evaluators, methods, schemas, or
  code;
- the marginal human judgment required per useful revision falls;
- retained theory remains causally active rather than ceremonial;
- wrong theories produce detectable negative transfer and are revised; and
- improvements transfer beyond the episodes that produced them.

## The bootstrap and the system boundary

The current Commonplace loop is human-inclusive. Agents retrieve, synthesize,
criticize, and write much of the material, while the operator still supplies
decisive high-level direction, global-fit judgment, and final authorization.
Calling the inclusive system autonomous would be cheap: it would hide the very
human contribution the bootstrap is intended to reduce.

Progress should therefore be reported against a fixed boundary and a declared
set of decision-bearing functions. The relevant measure is how much of the
learning path the computational subsystem can complete without a person
supplying the decomposition, evaluator, selection, promotion, or recovery
choice that the path is meant to make.

The bootstrap has two related jobs.

First, move named functions from human toward joint or computational supply while
holding the human-inclusive system boundary visible. A technical closure claim
is reached only for a declared path, task scope, horizon, evidence protocol, and
coverage rule. Closure says where decisions occur, not whether they are good.
[The decisions that stay human, and what would move
them](./the-decisions-that-stay-human-and-what-would-move-them.md) develops the
warrant and transfer problem.

Second, widen the demands over which computation can acquire the required
task- or family-specific production knowledge. Theories, schemas,
decompositions, tools, methods, and evaluators must not remain a new human
construction project for every new region of claimed scope.

The Bitter Lesson constrains the production method, not only the carrier of what
is learned. [Learning can produce explicit artifacts as well as
weights](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Fixed general models, learning methods, runtimes, interfaces, resource controls,
and trusted kernels may remain. The scaling burden falls on recurring
human-supplied task- or family-specific competence that the claimed process is
supposed to find.

This is why calling current structure a bootstrap is not enough. The bootstrap
[fits the Bitter Lesson only if learning outgrows its supplied
specialization](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
At the same time, [machinery persists by warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md):
a fixed component need not be replaced merely because it is outside one update
surface.

## Stronger claims remain separate

The factory-learning foundation does not make every stronger property follow.

| Property | Additional requirement |
|---|---|
| Recursive or higher-order factory development | Production machinery constructs or revises machinery used for later factory development |
| Reflection | A causally connected representation of selected aspects of the same system participates in operation or revision |
| Computational closure | Every decision assigned to a declared learning path is supplied computationally, conditional on permitted external evidence and interaction |
| Self-improvement | Evidence supports that the system's own retained change improved a declared objective |
| Compounding | An earlier change improves the capacity to produce or select later improvements |
| Broad production reach | The process acquires adequate family-specific production knowledge across a declared class of demands |

A factory can learn without reflection. A reflective system can fail to learn. A
closed path can perform badly. A factory-valued product can be produced from a
complete human specification. One successful change can remove the path that
produced it. These distinctions prevent recursion or factory language from doing
causal work it has not earned.

## What would change the strategy

Three possible benefits motivate theory mediation. Explicit theory may improve
[sample efficiency under structured
shifts](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can leave an inspectable learning record. And theories of agentic systems can
become candidate self-theory for the systems that build and revise agentic
software. Commonplace therefore develops [agentic-systems
theory](../agentic-systems/README.md) both as an external research topic and as
potential operative state.

Each benefit must survive comparison at total system cost. The strategy should
be narrowed or abandoned in a tested regime when:

- retained theory is causally inert or reconstructed after decisions;
- the evaluation loop becomes self-confirming;
- natural-language coordination increases correlated error;
- theory maintenance and retrieval cost exceed its search or transfer benefit;
- each new covered area still requires human-built decomposition or evaluation
  machinery;
- the marginal human contribution does not fall;
- additional computation produces activity or candidates without better
  downstream selection; or
- a more direct or mixed learning mechanism performs better at comparable total
  cost.

The program is therefore not a claim that general agentic learning must be
theory-mediated. It is a test of whether retained natural-language theory gives
a learning software factory a useful, revisable way to coordinate what it
believes about tasks, itself, its failures, and the machinery it should build
next.

The companion article [The Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops the scaling argument and competing alternatives.