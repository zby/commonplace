---
description: "Doctrine that once an automated software house carries the production loop, project-specific continual learning runs over the whole house with the model as one update surface; training steps, write governance, explicit-theory hypothesis"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/behavior-determining-organization.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
  - kb/notes/opacity-is-a-scale-threshold.md
  - kb/notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md
  - kb/notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md
  - kb/notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/treat-continual-learning-as-representational-form-coevolution.md
---
# The Software House as the Unit of Training

*Production-driven learning across models, theory, and code*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** We use *software house* for whatever keeps changing a piece of
software for its users. Suppose an automated software house carries the
complete production loop for a product: it receives requirements, changes
the software, observes the consequences, and revises the machinery of later
production. That system is then itself a trainable actor, and production is
its training environment. The alternative this article denies is the
model-only loop: a product's accumulated learning lives in the model's
weights, training the model is the learning, and everything around the model
stays fixed. The doctrine proposed here is that project-specific continual
learning should be organized over the whole house. A training step is a
governed, evidence-caused change to any retained component that determines
later production: project theory, code, tests, tools, evaluators, context
assembly (what the model is given to read), policies, and the model's weights
among them. The model is one component, and its weights are one surface among
several where an update can be written, not the place where a product's
accumulated learning is presumed to live. The article states the doctrine,
gives the argument for it, says what changes if it is accepted, names the
hard core of the doctrine as the governance of writes that change the house's
behaviour (deciding which changes are admitted, and which earlier change a
later consequence counts for or against), and states two hypotheses the
doctrine predicts, which a house whose model stays fixed can test: that
project theory kept as its own revisable artifact beats understanding rebuilt
from raw records each time, and that a house holding such a theory adapts to
a change with fewer observations when the theory captures what the change
preserves.

## The premise

The [companion article](./automated-software-houses-with-fixed-llms.md)
conjectures that an automated [software
house](../notes/definitions/software-house.md), meaning whatever keeps
changing a piece of software for its users, is practically reachable with LLMs
available today while every model stays fixed. In that regime the house learns
only through changes that computation produces and retains in its notes and
code: the natural-language and symbolic state around the model. The conjecture
is existential and constructive. If one such house exists, that establishes
that learning in the state around a fixed model can suffice for open-ended
coherent software change over a declared scope and horizon.

Pinning the model was an experimental isolation. It answered the question
whether learning in the state around the model can be enough. It said nothing
about whether that is how such a house should be trained once it exists. This
article takes up that question, on the assumption that the premise holds: a
house that carries the production loop, with no human in an internal
production role, over a declared scope and horizon.

## The doctrine

**The software house is the unit of project-specific training.** Once a
house carries the production loop, the learning that makes the product
better over time should be organized over the house, not confined to the
model inside it. A training step is a governed, evidence-caused change to any
retained component that determines later production. The house's
[behaviour-determining
organization](../notes/definitions/behavior-determining-organization.md) is
the writable surface: project theory, code, schemas, tests, tools,
evaluators, context assembly, scheduling, retention rules, and, where the
house has access to them, model weights. The model is one component and one
possible update surface inside that organization.

Three things follow directly. Production is the training environment: the
requirements, consequences, and retained history that the house already
receives are the evidence, and there is no separate training set. Training
runs at the cadence of the product: a failure can produce a new test on the
job that exposed it, and a revised assumption can alter project theory before
the next demand arrives. And the question shifts from *which weights* to
*which component, under what admission rule*. What distinguishes a training
step from an ordinary edit is not the form of the changed component but that
evidence caused the change, a governed process admitted it, and the retained
result changes how the house handles a job it has not yet been given.

The doctrine is not "never update the weights." Nor is it "save more
memories." It is that the evidence-to-update process runs over the whole
behaviour-determining organization, and that each component is chosen as a
target on the merits of the change, not by default.

## Why the house is the unit

The argument has two parts: what produces the behaviour, and what a
model-only loop cannot reach.

User-visible behaviour is produced jointly. [The deployed system, not the
model alone, is the unit of
learning](../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md)
because prompts, retrieval, context assembly, scheduling, memory, tools,
validators, and execution boundaries all shape what the user receives. A
retriever determines which evidence becomes available. A scheduler
determines which calls happen and what state survives. A validator
determines which candidate outputs can take effect. Changing any one of
them changes the result while the model stays the same, so attributing the
result to "model behaviour" credits joint behaviour to one component.

A model-only training loop therefore freezes the rest. [Learning inside a
fixed decomposition inherits its
mistakes](../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md):
optimizing the weights can improve every choice the model is allowed to
make, but it cannot touch a mistaken distinction, a missing tool, a poor
division of work, or a context policy that never loads the note that
matters. A capable model can sometimes compensate, inferring an intention a
prompt omitted or reconstructing state the harness failed to keep. That
improves measured behaviour without showing the fixed layer was right; it
spends model capacity repairing the same system error on every run.

A software house makes this concrete. Most of what the house learns about
its product is not a fact about language or programming in general. It is
that installs must be a single file, so the store is SQLite; that a
documentation-only change is safe unless a build tool reads the file; that
the tenant identifier belongs in the request context and not in the data
model. Such learning can be written into a note, enforced by a validator,
compiled into a tool, or, in principle, trained into weights. The cheapest
and most locatable surface differs by case. A loop that can only reach one
of them takes the others' lessons out of reach.

The house is also the boundary at which learning can respond to production
at all. [Retained artifacts give a deployed system a persistent adaptation
path outside weight
updates](../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md).
When production evidence can cause a retained change to a note, test, tool,
or policy, and that change affects the next job without a training run, the
house learns at the cadence of its own product. A loop that ships traces
back to a model-training pipeline learns at the cadence of that pipeline.

## What changes if the doctrine is accepted

**Two training layers.** Project-specific learning separates from general
model training, and each has its own principal target.

| Training layer | Principal target |
|---|---|
| General model training | Cross-project linguistic, reasoning, programming, and world competence |
| Software-house training | Project-specific theory, production machinery, constraints, evaluators, and accumulated operating competence |

**A newer model is a substitution, not a migration.** When a stronger base
model appears, it enters the house as a general-capability replacement to be
evaluated inside the house's existing behaviour-determining organization. The
product's accumulated learning stays in the house. Some of it may become
redundant, since a stronger model may absorb a heuristic a note used to carry,
and the house may then retire the note. But nothing forces the house to
relearn what it already holds. This is also why a project that has trained its
house should exploit a newer model better than an unprepared one: it hands the
new model a settled theory and a working production loop rather than a blank
repository.

**The hand-built harness is a seed to outgrow.** A house starts with
hand-written tools, prompts, validators, and provisional notes. Under the
doctrine these are seed engineering, and training is expected to displace
repeated human construction of the decisive project-specific theory,
decomposition, evaluators, and selection over the claimed scope. A house whose
important product-specific decisions remain human design is edited, not
trained.

**Which surface, and at what cost.** The doctrine makes the choice of update
surface a decision, and the decision has a structure. Neither weights nor
notes nor code make the whole system transparent; enough software and notes
[exceed practical inspection](../notes/opacity-is-a-scale-threshold.md) too.
The difference is how a change can be located, inspected, revised, and
reverted on its own. A change trained into weights is spread across
parameters, and a changed behaviour is hard to find, hard to revise
selectively, and hard to roll back without retraining. A change kept in a note
or a function is a unit the house can identify, inspect the history of, revise
on its own, and revert without touching anything else. That is a governance
cost, not a representational prohibition: the weights are the surface whose
changes are hardest to govern, so a house with a working non-parametric path
should have a reason before it trains weights on project evidence. Which
surface should hold which kind of learning, and when a lesson should move
between surfaces, is itself a trainable choice. [Continual learning is
representational-form
coevolution](../notes/treat-continual-learning-as-representational-form-coevolution.md):
the question is how the improvement loops over weights, natural language, and
code relate, not which of them is the real locus of learning.

## Governance is the hard core

The doctrine does not say that writing artifacts is learning. A memory file
that grows with every session is not a trained house; it is a store. [Continual
learning requires governing behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md):
for each candidate change the process must select it from the alternatives,
validate that it does what it claims, decide what authority it carries over
later work, and coordinate it with the components it affects. The doctrine
therefore names its own hard core. It is to construct a computational
evidence-to-update process over the behaviour-determining organization of
the house, and the parts of that process that no current system does well
are the parts the automated software house conjecture also flagged: admission, deciding
which changes of meaning may enter retained state; and credit assignment,
deciding which earlier note, test, tool, context policy, or selection rule a
delayed consequence counts for or against.

Two features of software houses make these harder than in a single-episode
learner. Consequences are delayed: a design choice may show its cost three
demands later, when the evidence has to be attributed back across several
intervening changes. And the house modifies its own machinery: an update to
the update process changes how every later piece of evidence is handled, so a
wrong admission can compound. Regression control, rollback, and safe
self-modification enter the doctrine here, as constraints on the
evidence-to-update process rather than as separate topics. This article
supplies no general solution; it locates the problem and says what a solution
must do.

## Testable consequences

The doctrine makes predictions that a fixed-model house can test without
settling the doctrine as a whole.

**The explicit-theory advantage hypothesis.** Hold the model, source evidence,
demand sequence, and total budget fixed. Then a house that synthesizes,
retrieves, applies, and revises an explicit project theory, meaning a
rationale that can be found and revised on its own, performs better under
structured change than a house that repeatedly reconstructs its understanding
from raw records or searches the implementation directly. *Better* means some
combination of higher success on later demands it has not been given, faster
diagnosis and recovery, fewer collateral regressions, more proportional
rescoping after a counterexample, cheaper rollback and local revision, and
lower total cost once theory search, validation, retrieval, and maintenance
are counted. Both routes require retained evidence to reach the relevant
decision and change it. Only the explicit route additionally requires
selecting, retaining, and revising the explicit theory. The comparison
isolates [the causal contribution of the explicit theory surface, not
possession of the house's whole program
theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md);
a trace showing that a note was loaded is not evidence that it governed the
decision.

**The sample-efficiency hypothesis.** When explicit theory captures structure
that a change preserves, the house [may need fewer new observations to
adapt](../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md).
It revises one premise and derives several consequences instead of relearning
each. A coding agent that has retained "a changed file cannot affect
integration behaviour when no executed process consumes it" can, on one
failure, narrow the exemption to files no tooling reads; an agent holding the
correlation "documentation files are safe" can only delete the rule or
enumerate exceptions. The advantage depends on the theory being both adequate
and used in later decisions; a broad wrong theory misleads as widely as a
right one would have helped. Fewer observations also need not mean lower total
cost.

A test of either hypothesis needs a baseline the fixed-model regime cannot
supply on its own: adapting the model's weights on the same production
evidence. Without it, an advantage of explicit theory over unsynthesized
records shows that synthesis pays; it does not distinguish training the state
around the model from adapting the model itself, which is the contrast the
doctrine draws.

The doctrine survives if the explicit-theory hypothesis fails. A house can
learn through tests, tools, learned critics, episodic retrieval, or weight
updates, and the doctrine says only that the loop must be able to reach
whichever of them the evidence warrants. Conversely, explicit theory could
help in some structured-shift regimes without becoming the surface for every
lesson.

## The Bitter Lesson objection

The standard objection is Sutton's Bitter Lesson: general methods that scale
with computation beat hand-built structure, so learning that lives in
readable notes and programs is the hand-built approach in a new costume.
The reply is that [the lesson selects how behaviour-shaping structure is
produced, not the form in which it is
retained](../notes/the-bitter-lesson-selects-production-methods-not-representational.md).
Notes, programs, schemas, tests, and evaluators are learned products when
computation produces and retains their evidence-responsive changes. What the
lesson does rule out is the case where the important product-specific
structure keeps coming from people. A hand-built starting house is compatible
with the lesson only if [learning outgrows the task-specific knowledge the
seed
supplies](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
as the claimed scope widens, computation must increasingly produce or
challenge the theory, representations, decompositions, methods, and
evaluators the house requires, and the retained result must affect later
work beyond the episode that exposed the need.

Read this way the lesson supports the doctrine rather than opposing it. It
demands that task-specific structure be computationally produced, and the
doctrine's whole content is a computational evidence-to-update process over
that structure. It also warns the doctrine against fixing permanently which
surface holds which lesson: no note, program, or validator is promised
survival, and a future model may absorb a theory or replace an evaluator with
a cheaper learned one. That is a possibility the doctrine already
accommodates, since which surface holds a lesson is a trainable choice. The
[companion
article](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
gives the full argument and the tests that would show a bootstrap has not
outgrown its seed.

## What the doctrine does not claim

It does not claim that weights must stay fixed. Pinning the model was the
conjecture's experimental isolation; the doctrine treats the weights as one
update surface among several, the one with the highest governance cost.

It does not claim that explicit theory is the best surface for what the house
learns. That is a hypothesis the doctrine predicts and a test can refute, and
the doctrine survives its refutation.

It does not claim that the current allocation among weights, notes, and code
is final, or that any current surface will persist.

It does not claim that current whole-system learners scale. Cross-component
credit assignment, validation cost, and safe retention of self-modifying
changes are open problems, and the doctrine names them as its hard core
rather than assuming them solved.

It is conditional on the premise. If no automated software house is
reachable, the doctrine has no actor to apply to, and what remains is the
weaker claim from the unit-of-learning argument: even a house with people in
internal roles should evaluate and improve the deployed system, not only the
model inside it.
