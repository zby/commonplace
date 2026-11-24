---
description: "Bootstrap supplement: Commonplace builds a reflective self-improver by selection, starting human-assisted and moving update decisions to computation one kind at a time; progress is tested by withholding the operator"
type: articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
brief: bootstrapping-autonomous-selection-based-learning.brief.md
source_notes:
  - kb/theory/definitions/selection-based-learning.md
  - kb/theory/definitions/self-improving-system.md
  - kb/theory/definitions/reflective-system.md
  - kb/theory/definitions/single-loop-and-double-loop-learning.md
  - kb/theory/definitions/codification.md
  - kb/theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md
  - kb/theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  - kb/theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md
  - kb/theory/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md
  - kb/theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
  - kb/theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md
  - kb/theory/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/theory/methodological-and-computational-closure-track-different-changes.md
  - kb/theory/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md
  - kb/theory/increasing-computational-autonomy-relocates-human-effort.md
  - kb/theory/computationally-directed-self-improvement-is-a-reallocation.md
  - kb/theory/defining-improvement-for-open-ended-work.md
---

# Bootstrapping Autonomous Selection-Based Learning with Commonplace

> **Draft.** The claims and structure of this article may change. Comments
> and counterexamples are welcome on
> [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

[The lead article](./continual-learning-with-fixed-model-weights-llm-selected-updates.md)
bets that a deployed agent system can learn while its model weights stay
fixed, with an LLM selecting which updates to keep. The learning it has in
mind is
[selection-based learning](../theory/definitions/selection-based-learning.md):
a change to what the system retains for its later work is proposed,
evaluated on whether it makes that work better, and can be rejected. This
article describes how Commonplace, the knowledge base behind these
articles, builds a system that learns this way autonomously.

What Commonplace is building is a reflective self-improving system. It
selects updates to its own instructions, checks, and code, and it does so
through an inspectable self-representation: the same instructions, checks,
and code are what govern its later work, so changing them changes how it
behaves. It is a
[self-improving system](../theory/definitions/self-improving-system.md)
because the selection sits inside its own boundary, and
[reflective](../theory/definitions/reflective-system.md) because it changes
itself through that self-representation. The lead article calls this
process **reflective self-improvement by selection**. The two names relate
as follows: selection-based learning names the process, and the reflective
self-improver is the whole system that runs that process on its own
method. The rest of this article calls the system the self-improver.

The self-improver is autonomous, for a declared class of updates, when
computation rather than the operator supplies the search and selection
decisions: noticing a problem, diagnosing it, generating candidate changes
and the checks that discriminate between them, choosing which candidate to
keep, installing it, and revising the criterion by which it chooses.
People remain outside the loop as users. They supply tasks, bug reports,
and objections, and they judge the results against what they asked for. As
the lead article puts it, depending on such outside input does not make the
loop human-assisted; a person deciding which update to install does.

Designing such a self-improver whole would require knowing in advance how
computation should make each of these decisions, and we do not know that.
So Commonplace builds it by bootstrapping. It starts human-assisted: a
human operator sits inside the system boundary and makes many of the update
decisions, and computation makes the rest. This already counts as
selection-based learning, because the definition does not depend on who
selects. It is also reflective from the start: the instructions, criteria,
and checks that govern its updates are stored in forms the system can
inspect and change, so its own method is among the things it can learn.
The bootstrap moves update decisions from the operator to computation one
kind at a time, each once evidence shows that computation makes it
adequately.

The bootstrap has advanced when a kind of update that needed the operator's
decisions completes with those decisions withheld. It is working while the
kinds of update that pass this test keep growing.
[The last section](#the-bootstrap) states the test and what would count as
failure. Whether the updates it admits make later work better is a separate
question, which
[Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
takes up.

## Retain what is selected

A selected update must leave a durable change that later work draws on. In
Commonplace those changes take the form of notes, instructions, schemas,
validators, tests, code, and other persistent artifacts.

Who contributes the update matters less at the start. The operator may
contribute at any step: choosing problems, diagnosing failures, drafting
candidates, interpreting evidence, approving changes, or supplying missing
capabilities. Which decisions to transfer first can be decided as the work
proceeds.

This works only while the operator keeps contributing, which requires a
system people want to use. Then the judgments they supply are part of work
they would do anyway. Commonplace is built to be such a system: its
operator builds and uses the knowledge base for their own work. That use is
also an evaluation. A retained claim or instruction that later work relies
on, and that survives later demands, has passed a test, and
[use performs that test](../theory/system-use-selects-theory-fit-without-a-fixed-oracle.md)
before any fixed check of it exists.

## Make the selection method selectable

Some of what the system learns concerns its own updates. A recurring
failure in review, diagnosis, or evaluation can become the problem for a
further update, and the selected change then alters how future updates are
proposed or judged. Because Commonplace keeps this method in inspectable
instructions and checks, the same loop that edits a routing rule can edit
the procedure that proposes routing rules, or the criterion that admits
them. Changing an object-level rule under a fixed adoption criterion is
single-loop learning. Changing the adoption criterion itself is
[double-loop learning](../theory/definitions/single-loop-and-double-loop-learning.md).

This opens a feedback loop:

> update → better update method → more future updates succeed → further updates

An improvement to the update method is reused by every later update, so
over a long horizon its return can exceed that of any single update, and
where it does,
[an optimal long-run learning strategy invests in its own machinery](../theory/an-optimal-long-run-learning-strategy-invests-in-its-own-machinery.md).

Reflection makes the method open to change. To close the loop, method
changes must also compound, making later updates cheaper, more reliable, or
newly possible. That takes two further things. The self-improver must be able to
change its method beyond revising text, which the next section takes up.
And the evidence that a method change helped must come from outside the
check that admitted it. Showing compounding takes a later improvement
episode, measured independently of that check, with a trace connecting the
two; the
[compounding test](../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md)
states what counts.

So far the record shows only the loop's starting point: retention and
later use, with no change to the update method and no demonstrated
improvement in later work.
[In a 2026-08-30 revision](../theory/evidence/commonplace-revision-used-theory-guided-computational-search.md),
the model read retained project knowledge, searched over reformulations of
the research program, and proposed the edits. The operator selected among
them, supplying the decisive judgments about which formulation fit. Later
commits built on the revised state. That is human-assisted selection: the
operator was inside the loop at the selection step.

## Let the self-improver build its own software

Improving the update method can take more than revising text. A new
procedure can call for new tools, experiments, search procedures, or
schedulers. Testing candidates reliably or at scale can require exact
symbolic computation. So Commonplace uses LLMs both to revise retained
knowledge and to build and modify the software that puts it into
operation.

The LLM handles semantic interpretation. Software handles exact
bookkeeping, orchestration, and enforceable checks, where it is more
reliable, following
[the error-correction asymmetry between schedulers and LLMs](../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md).
The boundary between them moves: the software is part of the system and
changes as updates reveal new requirements. With model weights held fixed,
[procedures the system acquires must persist outside the weights](../theory/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md),
and code is one place to keep them.

Open-ended learning may even require this ability, if new updates keep
creating new ways to test, organize, and apply what is retained.

## Move decisions from the operator to computation

A hand-built start fits Richard Sutton's Bitter Lesson
[only if learning outgrows it](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md):
computation must take over supplying the knowledge each new demand needs.
Automation therefore grows one decision at a time.

Take a hypothetical case from the lead article. An agent keeps filing
unfinished drafts into the collection reserved for finished proposals.
Early in the bootstrap, the operator notices the misfiling, diagnoses its
cause in the routing instructions, asks the model for candidate rule
changes, and picks one. Each of those is a separate decision that can move
separately.

A decision the operator makes repeatedly can move by one of two routes once
its scope has stabilized. It can be
[codified](../theory/definitions/codification.md) into a test, validator,
or check whose consumers are held to a reference: fixed rules say what the
check permits, and a consumer that departs from them is wrong. A validator
that flags drafts in the proposals collection codifies the noticing step.
This settles the decision in the retained method. Or the decision can be
delegated to the LLM under a retained natural-language procedure, which
automates it while the method leaves it open. An LLM that compares
candidate routing rules against replayed past filings, under a written
procedure, takes over the selection step this way. These are
[different changes](../theory/methodological-and-computational-closure-track-different-changes.md),
and the record should say which one happened.

A decision has moved when computation makes it and evidence shows that it
decides adequately within a stated scope. The evidence condition matters
because handing a decision to an unattended model is easy;
[a computational decision can be trusted only where its checks are reliable](../theory/warranted-autonomy-is-bounded-by-oracle-domain.md).
A decision can also move back: it returns to the operator when its check
turns out to be a poor stand-in for what it was meant to catch.

Each transfer and each return is recorded, so that a later reader can see
what moved, by which route, and when. So is what stays with the operator. A
person still in the loop is named, and their contribution is credited to
them. That record is informative, because
[transfer leaves people the decisions hardest to warrant](../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md).
The decisions that remain with the operator show where the means to
automate them are missing, where an objective is unsettled, where authority
is deliberately kept, or where transfer costs more than it returns.

## The bootstrap

Commonplace is therefore a human-assisted reflective self-improver whose
selected updates are retained, applied to its own update method, turned
into new software, and moved decision by decision from the operator to
computation. The aim is to use that process to make the self-improver
autonomous.

The hard part is the decisions that currently make updates possible at
all: noticing the next problem, diagnosing it, and deciding which
candidate serves the objective better. We conjecture that this process can
transfer those decisions too, beyond the ones it has already stabilized.
The conjecture does not cover choosing the objective itself. The objective
stays declared, and
[changing it counts as improvement only against a standard outside it](../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md).
Users also keep one judgment under a fixed objective: whether a result is
worth what it costs them. The objective says what to weigh. It does not
calculate the answer.

Progress is judged by
[a removal test](../theory/computationally-directed-self-improvement-is-a-reallocation.md).
Take one kind of update, withhold the operator's decisions, and check
whether the update still completes, over a stated scope and time horizon.
Kinds are distinguished by the decision withheld, not by the file edited.
In the routing case, the kind "choose among candidate routing rules" has
moved if a misfiling now leads to a selected and installed rule change
with no operator choice, and that change passes its checks. The case stays
hypothetical until a recorded update meets both conditions. The bootstrap
has advanced when the kinds of update that pass the test have grown.

The removal test shows that a decision moved. It does not show that the
updates computation now selects make later work better than the operator's
did. That needs the comparisons on fresh work in
[Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md).

Seeing growth takes no overall score: a kind that failed now passes, and
none that passed now fails. A transfer can also let one kind pass while
another stops passing. Then we ask whether the change is better on
balance, which
[takes a judgment about who gains and who loses, not a global measure](../theory/defining-improvement-for-open-ended-work.md).

Human decisions are counted, but only within one kind of update. Operator
decisions per routing-rule change, before and after a transfer, can be
compared. A count across all updates cannot serve as the program's
measure. Updates differ in size, and in an open-ended system
[attention freed from routine work moves to harder work](../theory/increasing-computational-autonomy-relocates-human-effort.md),
which can need more decisions each. For the same reason operator hours can
stay flat while the bootstrap succeeds.

The conjecture fails, in the terms of
[the bootstrap condition](../theory/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md),
in either of two ways. The kinds of update that pass the removal test stop
growing while transfers continue. Or they stay confined to decisions that
had already stabilized, which is the limit the conjecture says the process
can pass. A failure needs an observation window, and that window must
contain eligible opportunities: a period in which no misfiling occurred
cannot show that routing selection stalled. We have not yet fixed the
length of that window.

Withholding the operator is not always practical. Where the test cannot be
run, it weakens to an argument from the record of who proposed, diagnosed,
selected, and installed each update.

## Where to go next

- [Testing Autonomous Selection-Based Learning](./testing-autonomous-selection-based-learning.md)
  — how Commonplace records who made each update decision, and the
  comparisons that test whether selected updates improve later work.
- [Can an LLM Judge Which Changes Are Worth Making?](./can-an-llm-judge-which-changes-are-worth-making.md)
  — the selection decision in detail, which the bootstrap must eventually
  transfer.
- [Computationally directed self-improvement is a reallocation](../theory/computationally-directed-self-improvement-is-a-reallocation.md)
  — the removal test and why progress is measured by which decisions
  people still supply.
- [Methodological and computational closure track different changes](../theory/methodological-and-computational-closure-track-different-changes.md)
  — the difference between codifying a decision and delegating it.
