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

**TL;DR.** An automated [software
house](../notes/definitions/software-house.md) is the complete persistent
system that keeps changing software for its users while computation performs
every *internal production role*—work the house depends on to develop and
evolve that software. Assume such a house already exists over a declared scope
and horizon. This article does not ask how it was built. It makes three
separate claims about how the house learns afterward.

First, the whole software house is the unit of project-specific training, not
the model alone. A retained change is training when it alters how the house
handles later requirements; a change that only satisfies the current
requirement is production. Second, the proposed *fixed-model training regime*
keeps every model weight fixed while allowing production to revise the
house's retained state: code, tests, tools, evaluators, context assembly,
workflows, and the update process itself. This denies that project-specific
learning must be a weight change in one model.

Third, the regime proposes that an *explicit project theory*—a retained
statement of the product's design commitments, causal assumptions, and
invariants—mediates those revisions. Production experience revises the
explicit project theory, which then guides changes elsewhere in the house.
Whether this mediation improves learning is a separate empirical hypothesis,
not a consequence of treating the whole house as the training unit or keeping
its weights fixed.

The regime could support *general* project-specific learning only in the
limited sense that it can build new representations, tools, decompositions,
and evaluators instead of updating within a task structure fixed in advance.
Its generality remains bounded by the fixed models, available computation,
declared product scope, and operating horizon, and must be tested. It is
structurally compatible with AI researcher Rich Sutton's Bitter Lesson only
when computation, rather than people, produces and selects the task-specific
structure. That compatibility does not show that the regime will scale better
than weight adaptation. Its main difficulty is governing [behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
retained changes that affect later production must be selected, validated,
given bounded authority, coordinated with affected components, and retained
or rejected.

## The fixed-model premise

The [companion article](./automated-software-houses-with-fixed-llms.md)
conjectures that an automated software house is practically reachable with
LLMs available by 2026-09-02 while every model stays fixed. This article begins
after such a house exists. It assumes that the house receives requirements,
changes a product, observes operating consequences, retains project-specific
state, and can computationally revise the retained machinery around its fixed
models. No person diagnoses its internal failures, writes its explicit project
theory, chooses its successors, or admits its internal changes. Users may still supply
requirements, domain facts, feedback, and acceptance judgments about visible
behaviour; those are inputs from outside the house.

How the initial house was constructed is outside the argument. It may have
been hand-built, trained, evolved, produced by another house, or reached by the
[bootstrap program](./bootstrapping-the-first-automated-software-house.md). The
claim here begins from the resulting automated house and concerns the training
lineage that follows.

The models remain fixed throughout the training lineage. They still interpret
natural language, propose explicit project theories and programs, use tools,
and judge candidates. What they do not receive is a weight update from the
house's production experience. The question is whether the surrounding house
can nevertheless acquire and retain general project-specific production
competence.

## What is trained: the whole house

**The automated software house is the unit of project-specific training.**

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

Within the fixed-model training regime, the house's [behaviour-determining
organization](../notes/definitions/behavior-determining-organization.md) is the
trainable state. The models are part of that organization but remain fixed; the
retained components that training can change are the state and machinery around
them. A revision may change the explicit project theory itself, product or
production code, schemas, tests, tools, evaluators, retrieval, context
assembly, scheduling, retention rules, or the update process.

Much of what the house learns is specific to the product: that installs must
be a single file, so the store is SQLite; that a documentation-only change is
safe unless a build tool consumes the file; that the tenant identifier belongs
in request context rather than the data model. Such lessons can be stated in
the explicit project theory, enforced by tests, compiled into tools, or
embodied in code without changing model weights.

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

An explicit project theory is more than a memory of past episodes. It states
what the house currently takes to explain the product: its design commitments,
causal assumptions, invariants, mechanisms, and the scope within which they are
expected to hold. It gives production experience an explicit object to
confirm, challenge, narrow, or replace.

The proposed loop is:

> **production experience → explicit project theory revision → revision of the
> house guided by the explicit project theory → later production → further
> evidence**

The explicit project theory mediates learning when it changes how updates are
produced.
It can direct search toward one component, explain why a failure counts against
an earlier assumption, predict which other behaviour a candidate revision may
affect, and supply the rationale from which a test or tool is constructed. The
explicit project theory need not remain the final storage place of every
lesson. A conclusion stated first as an explanation that may be wrong may
become a test, validator, tool, or program. Merely loading or citing a note is
not enough. A [retained-theory
intervention](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
can test the causal role of the explicit project theory by withholding,
replacing, or perturbing it while holding the rest of the house fixed.

The fixed-model training regime relies on the fixed model for semantic
operations over explicit project theories that have not been formalized.
Whether the available fixed models can perform those operations reliably
across the declared scope is part of the empirical claim, not established by
the architecture. Symbolic artifacts supply exact execution and checks once a
commitment is settled enough to encode. Production can re-express a lesson in
these [representational
forms](../notes/definitions/representational-form.md): experience revises the
explicit project theory, the explicit project theory motivates a validator,
and later failures may prompt the house to reconsider the validator's premise.
The model remains fixed while the explicit project theory and symbolic
production machinery each change in response to the other.

Using an explicit project theory defines this proposed fixed-model training
regime. Whether an explicit project theory improves learning over the
alternatives is a separate empirical hypothesis, stated below.

## Bitter Lesson compatibility

The expected objection is Sutton's Bitter Lesson: general methods that scale
with computation outperform methods built from human knowledge, so learning in
readable explicit project theories and programs is hand-crafted structure under
another name.
The answer is that [the lesson selects how behaviour-shaping structure is
produced, not the form in which it is retained](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

In this fixed-model training regime, computation forms and revises the explicit
project theory, searches over programs and tools, constructs tests and
evaluators, and admits changes from production evidence. Natural-language and
symbolic artifacts are learned products when the automated house produces and
selects them. Keeping model weights fixed does not make those changes
human-authored.

The claim concerns the training lineage, not how the initial house was
constructed. This article does not say whether constructing that seed was
Bitter-Lesson compatible. After the training lineage begins, however,
people cannot keep supplying task-specific structure: there are no people
in internal production roles. Across new demands in the declared scope, and
any later scope expansion, the house must computationally produce or revise
the explicit project theory, representations, decompositions, methods, and
evaluators it needs.

This makes the fixed-model training regime structurally compatible with the
lesson; it does not show that it will perform better in the scaling comparison.
The fixed-model training regime may still perform worse if search, validation,
and credit assignment over localized artifacts do not scale, or if weight
adaptation reaches the same competence at lower total cost. The Bitter Lesson
makes that comparison necessary; it does not decide it by calling one retained
form "learning" and another "structure."

## Why the fixed-model training regime can be general

Here *general* does not mean unlimited intelligence or competence outside the
capabilities of the fixed models and available computation. It means that the
training method is not restricted in advance to a predefined family of
changes, ontology, list of skills, or kind of retained update.

To meet this definition on a new software demand, the house must be able, within
the capabilities of its fixed models and available computation, to construct
the project-specific structure the demand requires: a new concept,
representation, decomposition, tool, workflow, test, evaluator, or piece of
update machinery. Its model weights remain fixed, but programs and explicit
project theories provide a house-level hypothesis space beyond responses inside
a predefined harness. The architecture provides such construction as an update
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
A failure can revise the explicit project theory or add a test before the next
demand without a model-training cycle.

**Revision of identified components.** A particular assumption, rule, test, or
function can be identified, challenged, revised, and often rolled back without
reverting unrelated learning. This does not make a large house fully
understandable, but it gives its update process semantic and symbolic units on
which to operate.

**Expandable production machinery.** The house can turn recurring semantic
work into tools, checks, and workflows. It need not spend fixed-model capacity
reconstructing the same project decision on every run.

**Project continuity.** The accumulated explicit project theory and machinery
persist as artifacts outside a trained checkpoint, but their effective use may
still depend on the model. Replacing the fixed model is outside the training
lineage considered here and requires revalidation. Whether the retained
learning transfers without substantial repair is an empirical question.

**Testable mediation.** The explicit project theory can be varied independently
enough to ask whether it changed diagnosis, search, evaluation, recovery, or
later revision. Purely behavioural success does not offer the same direct
intervention on a named project assumption.

These are possible benefits of the architecture, not a proof that the
fixed-model training regime is cheaper or more capable than weight adaptation.
Discovery, retrieval, validation, coordination, and maintenance can consume the
apparent gain.

## Governance is the main difficulty

The proposal does not say that writing files is learning. A memory file that
grows after every session is a store, not a trained house. [Continual learning
requires governing behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
the house must select a candidate revision, validate what it claims, decide
what authority it receives over later work, coordinate it with affected
components, and retain or reject it.

Two problems are most important. **Admission** decides which proposed changes
may become part of the behaviour-determining organization. **Credit assignment**
decides which earlier part of the explicit project theory, test, tool, context
policy, or selection rule a later consequence counts for or against. Delayed
effects make both hard: a design choice may show its cost several demands later,
after other revisions have intervened.

The house also changes its own learning machinery. A revision to an evaluator
or admission rule changes how later evidence is interpreted, so a wrong update
can cause further errors to accumulate. Regression control, independent checks,
versioning, rollback, and safe self-modification are therefore parts of the
fixed-model training regime, not separate concerns. Holding model weights fixed
does not solve these problems; it only makes the proposed update mechanism
clear.

## Testable hypotheses

**Causal mediation.** Vary the explicit project theory while holding the
models, other retained state, source evidence, demands, and budget fixed.
Withholding or replacing it should change proposal, diagnosis, evaluation, or
recovery in a predicted way. Merely loading or citing it is not enough. This
test asks whether the explicit project theory affects learning; comparative
performance requires a separate test.

**The explicit-project-theory advantage hypothesis.** Hold the fixed models,
source evidence, demand sequence, and total budget constant. Compare the
proposed house with one that reconstructs its program theory from raw records,
searches the implementation directly, or revises artifacts without an explicit
project theory. The hypothesis predicts that the house using theory-mediated
learning performs better under changes that preserve structure captured by its
explicit project theory.

A test must choose its measures in advance: success on later demands, diagnosis
and recovery cost, regressions, proportional rescoping after a counterexample,
rollback cost, and total cost after search over explicit project theories,
retrieval, validation, and maintenance are counted.

**The sample-efficiency hypothesis.** When an explicit project theory captures
structure that a change preserves, the house [may need fewer new
observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can revise one premise and derive several consequences instead of relearning
each behaviour separately. For example, a house may explain a testing exemption
by the fact that no executable process consumes the changed file. If a build
tool starts reading documentation, the house can use that explanation to
reconsider exemptions for other files the tool consumes, before each causes a
failure. A broad but wrong explicit project theory creates the opposite risk:
it can mislead as widely as a correct explicit project
theory would have helped. Fewer observations also need not mean lower total
cost.

Model-weight adaptation on the same production evidence is an important
baseline. It compares this fixed-model training regime with model-weight
training; it is not a kind of update allowed inside the fixed-model training
regime.

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

Holding weights fixed isolates and defines this fixed-model training regime; it does not
claim that model weights are never useful to update. Parametric and hybrid
regimes remain alternatives. Current systems have not solved search over
explicit project theories, causal use of the explicit project theory,
cross-artifact credit assignment, validation, and safe admission. The target
is a fully automatic, general project-specific training loop in which the
model stays fixed and the software house learns.
