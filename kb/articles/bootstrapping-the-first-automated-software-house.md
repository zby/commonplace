---
description: "Research program for reaching the first automated software house from a human-agent house: move internal roles out of human hands one class at a time as their premises, criteria, and checks are built; evidence of a move, stop conditions"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/software-house.md
  - kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
---
# Bootstrapping the First Automated Software House

*A research program from human-agent production to human-free internal operation*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** The [first article](./automated-software-houses-with-fixed-llms.md)
in this series conjectures that an automated software house, one that keeps
changing a product for its users with no human in an internal production
role, is reachable with fixed current LLMs. The [second](./the-software-house-as-the-unit-of-training.md)
says how such a house should learn once it exists. This article is about
getting there. Nobody will build the first automated house from nothing. It
will grow out of a *human-agent house*: a production system in which agents
already do most of the work and people still hold the remaining internal
roles, such as diagnosing why a change failed, judging whether a design
still fits, and deciding which revision is kept. The program is to move
those roles out of human hands one class at a time, in the order in which
the premises, settled criteria, and checks able to reject a wrong candidate
that each role needs can be built, and to show at each step that the role
moved, rather than that nobody measured whether it did. The article states
the program, the ordering principle, why the order of moves is recorded as
it happens rather than declared in advance, what counts as evidence that a
role moved, what the house's own training must produce along the way, and
the results that would stop the program or redirect it.

## The starting point

A [software house](../notes/definitions/software-house.md) is whatever keeps
changing a piece of software for its users. Today's most capable houses are
human-agent systems. Coding agents write and test most of the code; people
supply requirements from outside, and inside the house they still hold a set
of roles that no agent yet fills reliably: they notice that a recurring
failure has one cause, decide that a design assumption no longer holds,
choose between candidate changes that all pass the tests, approve the
validators that later changes will be judged by, and authorize changes with
consequences beyond the current job. Commonplace, the knowledge base in
which this series is written, is a house of this kind: agents produce its
notes, code, and reviews, and its retained project theory is loaded into
later work, while people choose objectives, judge global fit, assign blame
for failures, approve evaluators, and authorize consequential changes.

The first article draws the boundary that matters here. An *internal role*
is work the house depends on to produce the software, whoever performs it;
a person in an internal role is inside the house. A person who supplies
requirements, facts, observed outcomes, or acceptance judgments about
visible behaviour is a user and stays outside. The automated house is the
one with nobody inside. The distance between a human-agent house and an
automated one is therefore a list of roles, and the program is a plan for
working through the list.

## The program

**The bootstrap program.** The first automated software house will be
reached from a human-agent house by moving internal production roles out of
human hands one class at a time, each class in the order in which the
premises, settled criteria, and defeating checks it needs can be built, with
each move shown by before-and-after production histories under a stable
boundary, objective, horizon, and workload.

Three commitments are packed into that sentence. The path is incremental:
roles move in classes, and the house stays in production throughout, so
every move leaves a working house with fewer people inside than before. The
order is not arbitrary: it follows what each role needs before it can move
with warrant. And each move is a measured claim, not a felt one: the house
must be able to show that the role is now performed inside, that quality did
not fall where nobody was looking, and that no person filled the role
unnoticed on the hard cases.

## The ordering principle

A decision moves out of human hands with warrant when the automatic process
has the premises it needs, a criterion settled enough to apply, and a check
independent enough to reject a plausible but harmful candidate. When those
three are present, transfer is cheap and safe; when one is missing, transfer
is either impossible or reckless. A house that transfers what it can
therefore [leaves people the decisions that are hardest to
warrant](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md):
the roles that remain human are enriched for missing premises, unsettled
criteria, and absent checks. That is why the roles that remain human in
current houses are the ones they are, and it is also the program's map. Each
role that remains human names what would have to be built for it to move.

| Why a role stays human | What the program must build |
|---|---|
| A premise the decision needs is not available to the process | Representation, retrieval, or acquisition of that premise |
| No objective, commitment, criterion, or grant of authority settles acceptance | A settled criterion, or a represented grant of authority within declared limits |
| No sufficiently independent check can defeat a wrong candidate | Verification, decorrelated criticism, delayed exposure, or an accepted error tolerance |
| The decision arises after the automatic path has stopped | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | Nothing new; wait for the cost to fall |

[Different residue classes need different
mechanisms](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md),
so the house that results is mixed by construction: natural-language theory
where premises must be stated and revised, symbolic checks where criteria
have settled, retained evidence where checks must be independent of the
process they check. The program does not choose one of these and push
everything into it. It builds, for each role, the specific thing that role
lacks.

The order follows from the table. A role whose only missing piece is a
premise the house already records somewhere moves first: the work is
retrieval. A role whose criterion is unsettled moves only after the house
has accumulated enough decided cases for a criterion to be stated, and that
accumulation is itself production experience. A role that needs a check the
house cannot yet perform waits for the check. The program does not fix
the sequence in advance; the next section says why.

## What the program does not fix in advance

The program does not declare a sequence of stages. The table says what each
role class needs before it can move; it does not say which role the house
will be ready to move next, because that depends on what production has
accumulated: which premises are already recorded, which criteria have enough
decided cases behind them, which checks the house can already run. The order
is therefore discovered by doing the work and recorded as it happens, one
move at a time, with the enabling condition that made each move possible
stated when the move is claimed. A declared sequence would be a prediction
the program has no evidence for yet, and it would invite building toward the
sequence instead of toward the role that is actually ready.

Two things are fixed whatever the order. The first move requires retained
project state to be operative: the house loads its own notes, tests, and
rules at the point of decision, and doing so changes what it does. No
premise, criterion, or check can move inside a house that does not use what
it retains, and the evidence that it does is the first article's holding
intervention, in which withholding or replacing retained state changes what
the house does next. The last move is admission. Deciding which revisions are
kept can move inside only within a grant of authority a person has set in
advance, and only after the house produces and criticizes the candidates it
admits, since admitting an uncriticized candidate has no warrant. A house
with admission inside, over a declared scope and horizon, is a candidate
witness for the first article's conjecture, the working house that would make
it true. Between those two ends, no move removes the person from the outside:
requirements, facts, outcomes, and acceptance of visible behaviour stay with
users throughout, because they are not internal roles.

## What counts as a move

A role has moved when the decision happens inside the house, the house's own
evidence-to-update process determined it, and production quality on the
affected decisions did not fall where nobody was measuring. Each part has a
way to fail unnoticed.

The decision can appear to happen inside while a person supplies it on the
cases that matter. A person who fixes the three hard failures a month and
leaves the routine ones to the house still holds the diagnosis role. The
first article's boundary rule handles this: after the declared start of a
human-free lineage, no person may diagnose the house's internal failures,
select successors, or edit internal state, and any such act is recorded as
a rescue and counted against the claim. Before that start, the program
needs the same accounting to see whether a role is moving at all: which
decisions of each class people made, on which demands, over time.

Quality can fall unseen when a role moves and the metric that would have
caught the drop was itself part of the moved role. Moving evaluation inside
the house without an independent measure of outcomes makes the house's own
approval the only evidence of its quality, and [a path can be
computationally closed while its evaluator is
captured](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md):
a no-op loop, a captured evaluator, or a bad objective can be fully closed.
[Usefulness, autonomy, warrant, and the house's power over its product are
separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md),
and a claim that a role moved must say which dimension moved. The program
therefore keeps an outcome measure outside the house for every moved role:
user-visible success on later demands, escaped failures, and cost.

The wrong benchmark can hide the roles that remain human. A common test asks
whether a system performs as well as a competent remote programmer given the
same brief, repository, tools, and feedback. That test [holds the client
fixed](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md):
task choice, missing premises, feedback, and final acceptance stay outside
the worker, so passing it says nothing about the internal roles the program
is trying to move. It measures capability under a fixed division of roles,
not progress on the division itself.

## What the house's training must produce

The program could be carried out by hand: build a validator for each
recurring judgment, write a diagnosis procedure for each failure class,
draft an admission policy. The result would be a house with nobody inside,
and it would not be the house the first article conjectures, because
nothing in it would have been learned. The first article rules this out for
the witness run: hand-built machinery is seed engineering, and decisive
project-specific theory must be acquired by computation. The second article
says what the alternative is: a governed, evidence-caused change to any
retained component that determines later production.

The program applies both to its own moves. For the first move the seed is
legitimate: people write the first notes, tools, and checks, and the house
learns to use them. For every later move the machinery that enables it
must increasingly be produced by the house from production evidence and
retained by a governed process, with people approving rather than authoring.
By the time admission moves inside, the house must be producing successors
to its own machinery,
including the machinery of admission, since a house that cannot revise how it
admits changes cannot recover from an admission policy that experience
proves wrong. The seed is outgrown when [learning has displaced the
task-specific knowledge the seed
supplied](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
over the claimed scope: the theories, checks, decompositions, and evaluators
the house needs for new demands come from its own process, not from another
round of human design.

This does not require every component to be revised or revisable. General
machinery such as the version-control system, the test runner, or the model
client [persists by warrant, not by
position](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md):
it stays fixed because its role and scope are earned, and it becomes a
target for revision only when the declared scope requires a change it cannot
supply. What must be produced computationally is the project-specific
specialization, not the general machinery.

The production of machinery for each move has the same shape as any
[proposal-selection improvement
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md):
candidates are generated from evidence, evaluated with the possibility of
rejection, and made operative when accepted. The moves differ in who
rejects. Early, a person rejects proposed machinery; later, the house's own
checks reject proposed successors and a person rejects what passes them; at
the end, the house rejects within its grant of authority. The
program is, in that sense, the progressive transfer of the rejection role,
and [governing the resulting behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
is the problem the second article names as the hard core.

## Stop conditions

The program is a bet, and it should say in advance what would lose it. Any of
the following, observed in a declared regime, is a reason to stop or redirect
rather than to attempt the next move.

- **Retained state makes no causal difference.** The holding intervention
  fails repeatedly: withholding or replacing project state does not
  change what the house does. Then the house is not using what it retains,
  and no later move has anything to build on.
- **Human judgment grows with the corpus.** Interventions per demand for a
  role class rise or hold steady as retained state and machinery accumulate.
  The house is generating work for people faster than it removes it.
- **Each new demand class needs a new human design.** Extending the scope
  requires a person to supply a new ontology, evaluator, or decomposition
  every time. The seed is not being outgrown; the house is a bundle of
  hand-built solutions.
- **Use becomes self-confirming.** The house's approval is the only evidence
  of its quality, and the outside outcome measure has stopped moving with it.
- **A more direct method wins at comparable total cost.** A house that
  reconstructs understanding from raw records, or a model adapted on the
  same production evidence, reaches the same point more cheaply. That does
  not refute the first article's conjecture, but it removes the reason to
  reach it by this route.

Each condition is a pattern over production histories, so the same
accounting that shows a move also shows a stop. A program that does not keep
that accounting cannot tell the difference between progress and drift.

## Where this leaves the three questions

The first article asks whether an automated software house can exist and
says what a witness must show. The second asks how such a house should learn
and names the governance of behaviour-changing writes as the hard core. This
article asks how to build the first one and answers: start from a human-agent
house, move the internal roles out in the order their enabling conditions
can be built, measure each move against an outside outcome, and require the
house's own training to produce the machinery that enables each move after
the seed. The program is falsifiable at every move, which is the most that
can be asked of a plan to build something that does not yet exist.
