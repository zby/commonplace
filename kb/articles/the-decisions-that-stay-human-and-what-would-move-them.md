---
description: "Research-program hub centered on whether fallible project theory can keep program modification coherent through search, recovery, and delayed feedback, with warranted transfer, closure, and a Bitter-Lesson-compatible bootstrap as supporting questions"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md
  - kb/notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/a-hand-crafted-bootstrap-fits-the-bitter-lesson-only-if-learning-can-outgrow-it.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md
  - kb/notes/reflection-buys-addressability.md
  - kb/notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
---

# The decisions that stay human, and what would move them

> **Draft.** This article is circulating for comments; its claims, structure, and central thesis may still change. Counterexamples, rival mechanisms, and disputed experimental controls are welcome through the repository's issue tracker.

The hardest programming decisions are not necessarily the ones that require the
most code. They are the ones for which no complete local rule or cheap test says
what change will preserve the program's purpose and organization.

Human programmers handle these decisions imperfectly. They use a partial theory
of the program to choose promising changes, notice conflicts, interpret failed
attempts, backtrack, and revise their understanding. The theory does not replace
search. It keeps search coherent until later requirements and operational
consequences reveal what the first tests could not.

This article presents a research program around one question:

> Can a computational composite use a fallible, project-specific theory to keep
> program modification coherent across proposal, search, backtracking,
> recovery, and delayed feedback — and revise both its theory and its behavior
> when consequences arrive?

Commonplace, an agent-operated knowledge base, is the human-inclusive bootstrap.
Programming agents supplied with persistent project-specific theory are the
first demanding external testbed. The goal is not to protect hand-written
knowledge from learning. It is to build a learning process that can eventually
produce, test, revise, and replace the theories and machinery it currently
receives from people.

## Easy automation leaves a different kind of work

A formatter can remove formatting decisions almost completely. Its inputs are
represented in source text, its criterion is supplied by a style specification,
and its output is cheap to check. Once formatting moves, better formatting tools
can become faster and cover more syntax, but they do not thereby take over
architecture or maintenance. Those decisions were outside the formatter's
method.

A request such as “support another output format without duplicating the
pipeline's validation logic” has a different shape. The repository may contain
tests for the immediate behavior, but no test fully states which abstraction is
central, which duplication is tolerable, or which present boundary exists for a
reason that the new request must preserve. The programmer uses code, tests,
design rationale, remembered failures, and an evolving account of the system as
a whole.

An agent can generate patches and run tests. The research question begins where
that is insufficient. Can it hold enough project-specific theory to understand
why the system has its present organization, use that theory during search, and
recover when a locally successful change proves globally wrong?

The companion article [What bound Naur's theory to programmers](./what-bound-naurs-theory-to-programmers.md)
starts from Peter Naur's claim that programming is theory building. Its main
repair is narrow: Naur's argument does not establish that only humans can hold a
program theory. But removing the human-only premise does not show that a current
agent passes his bearer tests. That remains an empirical question.

## Holding a theory means controlling a fallible search

A program theory need not be a complete formal specification or one document.
It may be spread across retained explanations, architectural decisions,
operational observations, learned competence, and code. Nor must it determine a
correct first change.

A theory is doing work when it changes the modification process. It can:

- narrow which candidates are considered;
- identify commitments a local fix must not silently break;
- give an unexpected result an interpretation;
- distinguish evidence against a candidate from evidence against the current
  theory;
- guide rollback and recovery; and
- change what the process tries on the next demand.

Generic search can also generate, test, and discard patches. The difference is
causal and project-specific. Withholding or replacing the retained theory should
change proposal, diagnosis, evaluation, recovery, or later revision. A theory
that merely accompanies the work is documentation, not a demonstrated part of
the learning path.

This makes the relevant standard longitudinal. A failed first candidate can
belong to coherent modification when the process recognizes the failure,
recovers, and revises. A successful first candidate can fail the standard when
it passes narrow tests while damaging the wider organization in a way the
process cannot detect. The detailed claim is that [holding a program theory
means sustaining coherent search under delayed feedback](../notes/holding-a-program-theory-means-sustaining-coherent-search-under-delayed-feedback.md).

## One path, several distinct functions

The current research architecture separates four functions because they fail in
different ways.

| Function | Current realization | Failure it exposes |
|---|---|---|
| Represent project-specific premises, purposes, commitments, and scope | Retained natural-language and symbolic artifacts | Omission, contradiction, drift, retrieval failure, inert documentation |
| Interpret theory and use it to guide search and diagnosis | A language model | Underspecification, stochastic deviation, bias, post-hoc rationale, theory ignored in practice |
| Execute exact transitions and keep the path alive | Code and a persistent runtime | Faithful execution of the wrong transition, frozen decomposition, truncated horizon |
| Correct proposals and theories | Tests, validators, held-out tasks, decorrelated criticism, later demands, and operational consequences | Weak proxies, captured evaluation, viability-only gates, delayed credit assignment |

This is a **functionally mixed** architecture. It is not a theorem that these
functions must remain in separate representational forms. A future learned
substrate may host several of them, and stronger models may absorb parts of the
current scaffolding. The present split is valuable because it makes the roles
addressable and supports interventions on each one.

The distinction between interpretation and correction is especially important.
A model can understand and apply a false theory. Semantic competence does not by
itself establish that the theory has genuine reach or that the proposed change
is good. Independent or sufficiently decorrelated evidence must remain able to
overturn the candidate's account.

Likewise, retained theory does not execute, and code does not decide which
unsettled objective should hold. The architecture is not a stack in which a
higher layer validates everything below it. It is a set of roles whose outputs
constrain and correct one another.

## Evidence comes in levels

The strongest theory-mediated loop is easy to state:

    retained theory
      -> theory-guided search or decision
      -> realized change
      -> independent or delayed consequence
      -> read-back against the same theory
      -> retained theory revision
      -> changed later operation

Using that complete chain as the minimum definition would hide useful partial
results. The program distinguishes four levels:

1. **Mediation:** changing or withholding the theory changes a proposal,
   evaluation, diagnosis, recovery step, or intervention.
2. **Empirical contact:** the intervention produces an outcome that bears on the
   theory.
3. **Theory learning:** the outcome changes the theory's content, scope,
   confidence, status, or operational role.
4. **Recurrence:** the updated theory state changes a later operation inside the
   same behavior-determining path.

A useful change can reach the first or second level without reaching the fourth.
The record should say so. A citation of retained theory at the decision point is
a cheap mediation trace, because it identifies the theory the process claims to
have used. It does not prove that the theory was load-bearing. An intervention
that withholds, replaces, or perturbs the theory provides stronger evidence.

The path must also be co-indexed. The theory that guided the change must be the
object against which the outcome is read, and the resulting theory state must be
the one used later. Three disconnected witnesses — a theory in one place, a
successful change in another, and a later revision elsewhere — do not establish
learning through theory. The full requirement is developed in [the note on
interpretation, retention, and independent read-back](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md).

## Why difficult decisions remain human

The same hard modification can be viewed from a boundary question: why has the
decision not yet moved out of the human part of the system?

A decision is easier to transfer with warrant when the process has the premises
it needs, an objective or criterion settled enough to apply, and evidence that
can reject a plausible but harmful candidate. When systems preferentially move
such decisions, the remaining human work becomes enriched for the opposite
properties.

| Why the decision remains human | What would have to grow |
|---|---|
| A required premise is unavailable to the deciding process | Representation, retrieval, or acquisition |
| The objective, commitment, criterion, or authority does not settle acceptance | Methodological settlement or a represented grant of authority |
| No sufficiently independent check can defeat the candidate | Verification, decorrelated criticism, delayed exposure, or accepted error tolerance |
| The decision arises after the automatic path stops | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | No new capacity; the transfer is currently uneconomic |

This is a conditional selection argument, not yet a prevalence result. Real
systems may automate whatever is cheap or whatever an unattended model will
attempt rather than preferentially moving warrantable decisions. A direct test
must compare decisions before and after successive transfers under a stable
boundary, objective, horizon, and workload.

The current comparative evidence finds that independent correction is often
weak or unstated in reported self-improvement paths. That is consistent with an
evaluator bottleneck. It does not by itself show that the residual decisions
became harder because easier ones moved first.

The bearer and transfer questions meet at open-ended modification but do not
collapse into one. The bearer question asks whether the composite can sustain
coherent, theory-guided search and recovery. The transfer question asks whether
the required premises, authority, correction, and continuity are sufficiently
inside the declared boundary for the decision to move with warrant.

## Closure is not evaluator quality

Computational closure should be stated only for a declared task selection,
objective, boundary, permitted exogenous inputs, horizon, resources, and
coverage rule. Conditional on those declarations, a path is structurally closed
when every required decision and transition occurs inside the automatic system.

That says where the decisions happen, not whether they are good. A no-op loop, a
bad objective, or a captured evaluator can be computationally closed. Evaluator
quality matters because a useful strong result needs correction, not because the
evaluator defines structural closure.

A **warranted, non-degenerate closure** claim therefore adds a capability floor,
consequential revision reach, reject-capable evaluation, continuity, explicit
boundary accounting, and measured outcomes. These are separate coordinates.
Tool usefulness, computational autonomy, warrant, and system power can move in
different directions, [so a progress claim must name which dimension
changed](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).

The remote-programmer benchmark is another coordinate. It asks whether a system
performs at least as well as a competent remote programmer given the same brief,
repository, tools, permissions, and feedback. That is a strong test of the
worker role. It deliberately holds the client fixed, so task choice, missing
premises, feedback, and final acceptance remain outside the worker. Passing the
benchmark would not close those decisions; [holding the client fixed exports
them by design](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).

The benchmark and warranted closure expose the same difficult client and
acceptance boundary from opposite sides. They do not measure the same thing.

## The Bitter Lesson is a bootstrap requirement

This program does not argue that natural-language theory and symbolic machinery
are exceptions to the Bitter Lesson. Present artifacts are partly hand-crafted,
and no carrier receives permanent protection.

The positive thesis is that they are bootstrap state for constructing a more
general search-and-learning process. The process should increasingly learn to
propose, test, retain, revise, operationalize, and retire theories, methods,
programs, tests, and parts of the machinery that performs those operations.

That differs from a hand-designed solution for one predefined area only if the
path can outgrow its starting structure. Competence in several domains is not
enough. A system with many hand-built ontologies and special update procedures
is still a bundle of predefined solutions. The relevant property is
**domain-extensibility**: can the same learning process construct the
project-specific theory, representations, methods, and checks needed in an area
that the designers did not enumerate?

Editable artifacts do not establish this. An agent may rewrite prompts while
the artifact types, mutation operators, routing, evaluators, and acceptance
rules remain fixed. The bootstrap thesis requires a reachable path by which
evidence can challenge consequential parts of that production machinery. It
also requires credit assignment and bounded human evaluation as the corpus,
horizon, and number of domains grow.

The companion article [The Bitter Lesson does not require everything to live in
weights](./the-bitter-lesson-does-not-require-everything-to-live-in-weights.md)
develops this argument. Its claim is deliberately asymmetric: the architecture
is conceptually compatible with the lesson, Commonplace is a useful
human-assisted bootstrap, and whether the path becomes a scalable,
domain-extensible learner remains open.

## Two linked testbeds

Programming agents with persistent project-specific theory provide the cleanest
first test of the bearer question. The target repository is external to the
agent. The experiment can ask whether correct theory changes search and recovery
without first proving that the agent is modifying its own behavior-determining
organization.

Commonplace provides the reflective bootstrap. It retains theory about its own
operation, routes that theory into later work, and turns some conclusions into
instructions, validators, schemas, and code. Humans still choose objectives,
supply unrecorded premises, assign much of the blame, approve consequential
changes, and repair paths beyond represented coverage.

This supports claims about useful human-agent theory work and inspectable causal
traces. It does not yet establish independent computational theory possession,
recurrence, task-scoped closure, or a scalable artifact-learning method.

## The next experiment

The most useful next result is a prospective theory intervention on sequential
program modifications. Hold the model, tools, repository state, budget, and
acceptance process fixed. Compare four conditions:

1. correct project theory;
2. an information-matched record without synthesized theory-level organization;
3. theory withheld; and
4. plausible but wrong or outdated theory.

Each sequence should contain an initial modification and a later demand or
delayed test that reveals whether the first change preserved the program's
organization. Measure which candidates are generated, what the process tries to
preserve, how it diagnoses failures, when it backtracks, how well it recovers,
what collateral regressions occur, how much human intervention is required, and
whether the outcome changes a later episode.

The diagnostic prediction is not simply that more context helps. Correct theory
should help most when the later demand preserves the structure the theory names.
Wrong theory should produce predictable negative transfer. Withholding theory
should especially damage diagnosis, recovery, and follow-on coherence. The
advantage should shrink where a complete specification and cheap oracle already
settle the task.

This result would not prove a scalable bootstrap. It would establish the more
basic causal claim that project theory can be a load-bearing part of coherent
modification. A later cross-domain experiment must test whether the process can
construct and revise the required theory and machinery rather than receiving
them already prepared.

## The invitation

The program now has several points where disagreement can be productive. A
researcher can challenge the account of human coherent modification, propose a
rival mechanism that does not require retained theory, design stronger controls
for the intervention, test whether residual work is actually adversely
selected, or show that evaluator and decomposition construction keep the
bootstrap permanently dependent on human design.

The goal is not to recruit agreement with a finished theory. It is to expose a
small set of claims whose status can change through criticism and evidence. The
central one is concrete: whether a fallible, project-specific theory can make
computational search and recovery more coherent across novel demands and
delayed consequences.
