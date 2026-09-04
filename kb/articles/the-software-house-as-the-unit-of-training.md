---
description: "Doctrine that once an automated software house exists, production can train it through theory-mediated changes to project theory and production machinery while all model weights remain fixed"
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

*A fixed-model, theory-mediated training regime*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** Assume an automated [software
house](../notes/definitions/software-house.md) already exists: over a declared
scope and horizon, every internal production role is computational. This
article does not ask how that first house was built. It asks how the house can
keep learning while all of its model weights remain fixed. The proposed regime
trains the house as a whole. Production supplies requirements, consequences,
and retained experience. The house forms and revises an explicit project
theory, then uses that theory to guide governed changes to the retained
organization around the fixed models: theory, code, tests, tools,
evaluators, context assembly, workflows, and the learning process itself. A
change that only satisfies the current requirement is production; a retained
change that alters how later requirements are handled is training. The regime
can be general across project-specific software learning because it can build
new representations, tools, decompositions, and evaluators instead of learning
only inside a fixed task structure. It is compatible with the Bitter Lesson
because computation, not people, produces and selects the task-specific
structure. Its hard problem is governing those behaviour-changing writes.

## The premise

The [companion article](./automated-software-houses-with-fixed-llms.md)
conjectures that an automated software house is practically reachable with
LLMs available by 2026-09-02 while every model stays fixed. This article begins
after such a house exists. It assumes that the house receives requirements,
changes a product, observes operating consequences, retains project-specific
state, and can computationally revise the retained machinery around its fixed
models. No person diagnoses its internal failures, writes its project theory,
chooses its successors, or admits its internal changes. Users may still supply
requirements, domain facts, feedback, and acceptance judgments about visible
behaviour; those are inputs from outside the house.

How the initial house was constructed is outside the argument. It may have
been hand-built, trained, evolved, produced by another house, or reached by the
[bootstrap program](./bootstrapping-the-first-automated-software-house.md). The
claim here begins from the resulting automated house and concerns the training
lineage that follows.

The models remain fixed throughout that lineage. They still interpret natural
language, propose theories and programs, use tools, and judge candidates. What
they do not receive is a weight update from the house's production experience.
The question is whether the surrounding house can nevertheless acquire and
retain general project-specific production competence.

## The doctrine

**The automated software house is the unit of project-specific training.** Its
[behaviour-determining
organization](../notes/definitions/behavior-determining-organization.md) is the
trainable state. The models are part of that organization but remain fixed; the
writable training surface is the retained state and machinery around them. The
explicit project theory mediates the transition from production experience to
a governed change in that surface.

The basic loop is:

> **production experience → project-theory revision → theory-guided revision of
> the house → later production → further evidence**

A revision may change the project theory itself, product or production code,
schemas, tests, tools, evaluators, retrieval, context assembly, scheduling,
retention rules, or the update process. The theory need not remain the final
storage place of every lesson. A conclusion stated first as a fallible
explanation may become a test, validator, tool, or program. The learning is
theory-mediated because the theory explains the evidence, identifies what
should change, and guides the construction and assessment of the retained
revision.

Production supplies the training stream. Requirements provide new demands;
operating consequences provide evidence about the results; retained history
provides material for diagnosis and comparison. These episodes may be replayed,
simulated, or augmented. A separate model-training pipeline is not
constitutive of training the house.

Not every product change is a training step. A patch that only carries the
current requirement into the product is production. It counts as training only
insofar as the retained change also alters the house's capacity on later
requirements: for example by revising an assumption, introducing a reusable
abstraction, adding an invariant, creating a tool, or changing how later work
is evaluated.

## Why the house is the unit

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
on which later evolution depends. That complete persistent producer is the
automated software house.

A fixed-model training regime can revise this wider system. Much of what the
house learns is specific to the product: that installs must be a single file,
so the store is SQLite; that a documentation-only change is safe unless a
build tool consumes the file; that the tenant identifier belongs in request
context rather than the data model. Such lessons can be stated as theory,
enforced by tests, compiled into tools, or embodied in code without changing
model weights.

This wider update space matters because [learning inside a fixed decomposition
inherits its
mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
A learner confined to a supplied task structure cannot directly repair a
missing distinction, tool, action, or mapping outside it. Training the house
can instead revise the decomposition, construct a new representation, or add
the missing operation.

## Why the learning is theory-mediated

An explicit project theory is more than a memory of past episodes. It states
what the house currently takes to explain the product: its design commitments,
causal assumptions, invariants, mechanisms, and the scope within which they are
expected to hold. It gives production experience an addressable object to
confirm, challenge, narrow, or replace.

Theory mediates learning when it changes the update path. It can direct search
toward one component, explain why a failure counts against an earlier
assumption, predict which other behaviour a candidate revision may affect, and
supply the rationale from which a test or tool is constructed. Merely loading
or citing a note is not enough. A [retained-theory
intervention](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
can test the causal role of the theory by withholding, replacing, or perturbing
it while holding the rest of the house fixed.

The fixed model supplies the semantic machinery needed to operate on theories
that have not been formalized. Symbolic artifacts supply exact execution and
checks once a commitment is settled enough to encode. Production can move a
lesson between these [representational
forms](../notes/definitions/representational-form.md): experience revises a
theory, the theory motivates a validator, and later failures may reopen the
validator's premise for interpretation and revision. The model remains fixed
while the theory and symbolic production machinery coevolve around it.

## Why the regime can be general

Here *general* does not mean unlimited intelligence or competence outside the
capabilities of the fixed models and available computation. It means that the
training method is not restricted in advance to a predefined family of
changes, ontology, list of skills, or kind of retained update.

For a new software demand within its capability envelope, the house can in
principle construct the project-specific structure the demand requires: a new
concept, representation, decomposition, tool, workflow, test, evaluator, or
piece of update machinery. Its model weights remain fixed, but its effective
house-level hypothesis space is not limited to choosing among responses inside
a frozen harness. Programs and theories can create new state and operations
that later production can use.

The generality claim is still scoped. Some objectives, authority boundaries,
hard dependencies, runtimes, and trusted kernels may remain fixed. A claim of
general training must name its product scope and operating horizon, and it
fails where new demand classes repeatedly require people to supply the missing
project-specific ontology, decomposition, or evaluator.

## What the regime buys

**Training at production cadence.** [Retained artifacts provide a persistent
deployment-time adaptation
path](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
A failure can revise a theory or add a test before the next demand without a
model-training cycle.

**Addressable revision.** A particular assumption, rule, test, or function can
be identified, challenged, revised, and often rolled back without reverting
unrelated learning. This does not make a large house transparent, but it gives
its update process semantic and symbolic units on which to operate.

**Expandable production machinery.** The house can turn recurring semantic
work into tools, checks, and workflows. It need not spend fixed-model capacity
reconstructing the same project decision on every run.

**Project continuity.** The accumulated project theory and machinery are not
bound to a trained checkpoint. Replacing the fixed model is outside the
training lineage considered here and requires revalidation, but it need not
reset the project's retained learning.

**Testable mediation.** Explicit theory can be varied independently enough to
ask whether it changed diagnosis, search, evaluation, recovery, or later
revision. Purely behavioural success does not offer the same direct
intervention on a named project assumption.

These are architectural affordances, not a proof that the regime is cheaper or
more capable than weight adaptation. Discovery, retrieval, validation,
coordination, and maintenance can consume the apparent gain.

## Governance is the hard core

The doctrine does not say that writing files is learning. A memory file that
grows after every session is a store, not a trained house. [Continual learning
requires governing behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
the house must select a candidate revision, validate what it claims, decide
what authority it receives over later work, coordinate it with affected
components, and retain or reject it.

Two problems dominate. **Admission** decides which proposed changes may enter
the behaviour-determining organization. **Credit assignment** decides which
earlier theory, test, tool, context policy, or selection rule a later
consequence counts for or against. Delayed effects make both hard: a design
choice may show its cost several demands later, after other revisions have
intervened.

The house also changes its own learning machinery. A revision to an evaluator
or admission rule changes how later evidence is interpreted, so a wrong update
can compound. Regression control, independent checks, versioning, rollback,
and safe self-modification are therefore parts of the training regime, not
separate concerns. Holding model weights fixed does not solve these problems;
it only makes the proposed update path clear.

## Testable hypotheses

**The explicit-theory advantage hypothesis.** Hold the fixed models, source
evidence, demand sequence, and total budget constant. Compare the proposed
house with one that reconstructs its understanding from raw records, searches
the implementation directly, or revises artifacts without an explicit project
theory. The theory-mediated house should perform better under structured
change if the theory has a real causal role.

A test must choose its measures in advance: success on later demands, diagnosis
and recovery cost, regressions, proportional rescoping after a counterexample,
rollback cost, and total cost after theory search, retrieval, validation, and
maintenance are counted. A trace showing that a note was loaded is not enough;
withholding or replacing it should change the relevant decision.

**The sample-efficiency hypothesis.** When an explicit theory captures
structure that a change preserves, the house [may need fewer new
observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It can revise one premise and derive several consequences instead of relearning
each behaviour separately. A broad wrong theory creates the opposite risk: it
can mislead as widely as a right theory would have helped. Fewer observations
also need not mean lower total cost.

Model-weight adaptation on the same production evidence is an important
baseline. It compares this fixed-model regime with a different training regime;
it is not an update surface inside the doctrine. If theory interventions make
no causal difference, or artifact search without theory repeatedly matches the
proposed method at lower total cost, the theory-mediated claim fails in that
tested regime.

## Bitter Lesson compatibility

The expected objection is Sutton's Bitter Lesson: general methods that scale
with computation outperform methods built from human knowledge, so learning in
readable theories and programs is hand-crafted structure under another name.
The answer is that [the lesson selects how behaviour-shaping structure is
produced, not the form in which it is retained](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

In this regime, computation forms and revises the project theory, searches over
programs and tools, constructs tests and evaluators, and admits changes from
production evidence. Natural-language and symbolic artifacts are learned
products when the automated house produces and selects them. Keeping model
weights fixed does not make those changes human-authored.

The claim attaches to the training lineage, not to the provenance of the
initial house. This article does not say whether constructing that seed was
Bitter-Lesson compatible. After the lineage begins, however, task-specific
structure cannot keep arriving from people: there are no people in internal
production roles. Across new demands in the declared scope, and any later
scope expansion, the house must computationally produce or revise the theory,
representations, decompositions, methods, and evaluators it needs.

This makes the regime structurally compatible with the lesson; it does not show
that it will win the scaling comparison. The regime may still lose if
search, validation, and credit assignment over localized artifacts do not
scale, or if weight adaptation reaches the same competence at lower total cost.
The Bitter Lesson makes that comparison necessary; it does not decide it by
calling one retained form "learning" and another "structure."

## What the doctrine does not claim

It does not explain how the first automated software house is built. That is a
separate construction problem.

It does not claim that model weights are never useful to update. They are held
fixed to isolate and define this training regime. Parametric and hybrid regimes
remain alternatives.

It does not claim unbounded learning. Fixed models, available tools,
computation, objectives, and authority set a capability envelope.

It does not count every software change as training. The change must alter how
the house handles later demands, not only satisfy the present one.

It does not claim that current systems have solved the regime. Theory search,
causal use of retained theory, cross-artifact credit assignment, validation,
and safe admission remain open problems. The article states the target: a
fully automatic, general project-specific training loop in which the model
stays fixed and the software house learns.
