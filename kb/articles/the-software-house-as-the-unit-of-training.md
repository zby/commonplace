---
description: "Proposal that once an automated software house exists, production can train it through theory-mediated changes to project theory and production machinery while all model weights remain fixed"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/behavior-determining-organization.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
---
# The Automated Software House as the Unit of Training

*A fixed-model training regime for theory-mediated learning*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A [software house](../notes/definitions/software-house.md) is the
complete persistent system that keeps changing software for its users. Assume
an automated one exists. The proposed *fixed-model training regime* trains
the house through production: experience changes retained knowledge and
machinery that affect later work, while every model weight stays fixed.

In this regime, an *explicit project theory*—a retained statement of design
commitments, causal assumptions, and invariants—mediates those changes. Experience revises
the theory, which guides revisions elsewhere in the house. Whether this
mediation improves learning is an empirical hypothesis. The central difficulty
is selecting and validating changes, assigning their authority, and tracing
later consequences back to the decisions that produced them.

## The fixed-model premise

The [companion article](./automated-software-houses-with-fixed-llms.md)
conjectures that an automated software house is practically reachable with
LLMs and other learned components available by 2026-09-02 and held fixed. Here
that house is the starting point. Computation performs every *internal
production role*: interpreting project knowledge, implementing changes,
diagnosing failures, revising retained state, and choosing which revision takes
effect. Users may still supply requirements, domain facts, feedback, and
acceptance judgments about visible
behaviour; those are inputs from outside the house.

The initial house may be human-built or reached by the
[bootstrap program](./bootstrapping-the-first-automated-software-house.md).
The training lineage studied here begins afterward and keeps its models fixed
throughout. They interpret natural language, propose theories and programs,
use tools, and judge candidates; production experience changes the surrounding
state and machinery.

## What is trained: the whole house

User-visible production is joint behaviour. [The deployed system, not the
model alone, is the unit of
learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
because retrieval, context assembly, scheduling, memory, tools, validators,
and execution boundaries all shape what the model can do and which outputs can
take effect. A retriever determines which evidence becomes available. A
scheduler determines which calls happen and what state survives. A validator
determines which candidate can be admitted. Changing any of them changes the
result while the model stays fixed.

The relevant system is more than one deployed agent. The behaviour at issue is
coherent product evolution across a sequence of requirements and operating
consequences. The learning boundary must therefore include the current product,
retained project knowledge, production machinery, and every computational role
on which later evolution depends. That production system is the automated
software house.

The mutable part of the house's [behaviour-determining
organization](../notes/definitions/behavior-determining-organization.md) is the
trainable state. A revision may change the explicit project theory, product or
production code, schemas, tests, tools, evaluators, retrieval, context
assembly, scheduling, retention rules, or the update process.

Much of what the house learns is specific to the product: that installs must
be a single file, so the store is SQLite; that a documentation-only change is
safe unless a build tool consumes the file; that the tenant identifier belongs
in request context rather than the data model. Such lessons can be stated in
the theory, enforced by tests, compiled into tools, or embodied in code.

This wider update space matters because [learning inside a fixed decomposition
inherits its
mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
A learner confined to a supplied task structure cannot directly repair a
missing distinction, tool, action, or mapping outside it. Training the house
can instead revise the decomposition, construct a new representation, or add
the missing operation.

## What counts as training

Production supplies the training stream. Requirements provide new demands;
operating consequences provide evidence about the results; retained history
provides material for diagnosis and comparison. These episodes may be replayed,
simulated, or augmented. Training the house does not require a separate
model-training pipeline.

Not every product change is a training step. A patch that only carries the
current requirement into the product is production. It counts as training only
when and to the extent that the retained change also alters the house's capacity
on later requirements: for example by revising an assumption, introducing a
reusable abstraction, adding an invariant, creating a tool, or changing how
later work is evaluated.

## Why this is theory-mediated learning

An explicit project theory explains the product and states where its
commitments and assumptions are expected to hold. It gives production
experience an object to confirm, challenge, narrow, or replace.

The proposed loop is:

> **production experience → explicit project theory revision → changes guided
> by the theory → later production → further evidence**

The theory mediates learning when it changes how updates are produced. It can
direct search toward one component, explain why a failure counts against
an earlier assumption, predict which other behaviour a candidate revision may
affect, and supply the rationale from which a test or tool is constructed. The
theory need not remain the final storage place of every lesson. A tentative
explanation may become a test, validator, tool, or program.

The regime relies on the model for semantic operations over theories that have
not been formalized. Whether the available fixed models can perform those operations reliably
across the declared scope is part of the empirical claim, not established by
the architecture. Symbolic artifacts supply exact execution and checks once a
commitment is settled enough to encode. Production can re-express a lesson in
these [representational
forms](../notes/definitions/representational-form.md): experience revises the
theory, the theory motivates a validator, and later failures may prompt the
house to reconsider the validator's premise.

## Bitter Lesson compatibility

The expected objection is AI researcher Rich Sutton's Bitter Lesson: general
methods that scale with computation outperform methods built from human
knowledge, so learning in readable theories and programs is hand-crafted
structure under another name. The answer is that [the lesson selects how behaviour-shaping structure is
produced, not the form in which it is retained](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

In this regime, computation forms and revises the theory, searches over
programs and tools, constructs tests and evaluators, and admits changes from
production evidence. Natural-language and
symbolic artifacts are learned products when the automated house produces and
selects them.

Compatibility is assessed over this training lineage; it does not judge how
the seed was constructed. Across new demands and any later scope expansion,
the house must computationally produce or revise the task-specific structure
it needs.

This makes the regime structurally compatible with the lesson; it does not
show that it will perform better in the scaling comparison. It may still
perform worse if search, validation, and credit assignment over localized
artifacts do not scale, or if weight
adaptation reaches the same competence at lower total cost. The Bitter Lesson
makes that comparison necessary; it does not decide it by calling one retained
form "learning" and another "structure."

## Why the fixed-model training regime can be general

Here *general* means that the training method is not restricted in advance to
a predefined family of changes, ontology, list of skills, or kind of retained
update.

Within its fixed-model capabilities and available computation, the house must
construct the project-specific structure a new demand requires: a new concept,
representation, decomposition, tool, workflow, test, evaluator, or piece of
update machinery. Programs and theories provide a house-level hypothesis
space beyond responses inside a predefined harness. The architecture provides such construction as an update
mechanism; it does not establish that the house will find and admit the needed
structure.

The generality claim is still scoped. Some objectives, authority boundaries,
hard dependencies, runtimes, and trusted kernels may remain fixed. A claim of
general training must name its product scope and operating horizon, and it
fails where new demand classes repeatedly require people to supply the missing
project-specific ontology, decomposition, or evaluator.

## What the fixed-model training regime buys

**Training as production happens.** [Retained artifacts provide a persistent
deployment-time adaptation
mechanism](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
A failure can revise the theory or add a test before the next demand without a
model-training cycle.

**Revision of identified components.** A particular assumption, rule, test, or
function can be identified, challenged, revised, and often rolled back without
reverting unrelated learning. This does not make a large house fully
understandable, but it gives its update process semantic and symbolic units on
which to operate.

**Expandable production machinery.** The house can turn recurring semantic
work into tools, checks, and workflows. It need not spend fixed-model capacity
reconstructing the same project decision on every run.

**Project continuity.** The accumulated theory and machinery persist as
artifacts outside a trained checkpoint, but their effective use may
still depend on the model. Replacing the fixed model is outside the training
lineage considered here and requires revalidation. Whether the retained
learning transfers without substantial repair is an empirical question.

**Testable mediation.** The theory can be varied independently enough to ask
whether it changed diagnosis, search, evaluation, recovery, or
later revision. Purely behavioural success does not offer the same direct
intervention on a named project assumption.

These benefits must pay for discovery, retrieval, validation, coordination,
and maintenance. The comparisons below test whether they do.

## Governance is the main difficulty

Persistence leaves the update decision unresolved. [Continual learning requires
governing behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
the house must select a candidate revision, validate what it claims, decide
what authority it receives over later work, coordinate it with affected
components, and retain or reject it.

Two problems are most important. **Admission** decides which proposed changes
may become part of the behaviour-determining organization. **Credit assignment**
decides which earlier part of the theory, test, tool, context policy, or
selection rule a later consequence counts for or against. Delayed
effects make both hard: a design choice may show its cost several demands later,
after other revisions have intervened.

The house also changes its own learning machinery. A revision to an evaluator
or admission rule changes how later evidence is interpreted, so a wrong update
can cause further errors to accumulate. Regression control, independent checks,
versioning, rollback, and safe self-modification are therefore parts of the
regime.

## Testable hypotheses

**Causal mediation.** A [retained-theory
intervention](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
varies the explicit project theory while holding the models, other retained
state, source evidence, demands, and budget fixed.
Withholding or replacing it should change proposal, diagnosis, evaluation, or
recovery in a predicted way. Merely loading or citing it is not enough. This
test asks whether the explicit project theory affects learning; comparative
performance requires a separate test.

**The explicit-project-theory advantage hypothesis.** Hold the fixed models,
source evidence, demand sequence, and total budget constant. Compare the
proposed house with one that reconstructs its program theory from raw records,
searches the implementation directly, or revises artifacts without an explicit
project theory. The hypothesis predicts better performance from theory-mediated
learning under changes that preserve the structure its theory captures.

A test must choose its measures in advance: success on later demands, diagnosis
and recovery cost, regressions, proportional rescoping after a counterexample,
rollback cost, and total cost after search over explicit project theories,
retrieval, validation, and maintenance are counted.

**The sample-efficiency hypothesis.** When the theory captures structure that a
change preserves, the house [may need fewer new
observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can revise one premise and derive several consequences instead of relearning
each behaviour separately. For example, a house may explain a testing exemption
by the fact that no executable process consumes the changed file. If a build
tool starts reading documentation, the house can use that explanation to
reconsider exemptions for other files the tool consumes, before each causes a
failure. A broad but wrong theory creates the opposite risk: it can mislead as
widely as a correct one would have helped. Fewer observations also need not
mean lower total cost.

Model-weight adaptation on the same production evidence is an important
baseline from a different training regime.

If interventions make no causal difference, they do not establish mediation by
the explicit project theory varied in that test; the house may reconstruct
equivalent understanding from other retained state. If artifact search without
an explicit project theory repeatedly matches the proposed method at lower
total cost, the advantage hypothesis fails in that regime even if the explicit
project theory affects learning. Neither result settles whether the house is
the unit of training or whether it can be trained with its models fixed: a
house that learns through tests, tools, and search without an explicit project
theory would still be trained as a whole around fixed models.

## Limits

Parametric and hybrid regimes remain alternatives. The proposed regime still
needs reliable theory search and use, credit assignment across artifacts,
validation, and safe admission. Until those functions work together, it remains
a proposal for training the house as a whole.
