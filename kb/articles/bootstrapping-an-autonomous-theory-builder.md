---
description: "Supplement: Commonplace as a human-inclusive seed, separate operational and learning transfers of internal theory-building roles to computation, readiness conditions, and an illustrative trial of learning which checks a Markdown edit needs"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/theory-builder.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
---
# Bootstrapping an Autonomous Theory Builder

*A research program from human-inclusive operation to computational internal roles*

> **Draft supplement.** This develops the route from Commonplace today to
> the system that [Learning by Theory Refinement with Fixed
> Models](./learning-by-theory-refinement-with-fixed-models.md) would test.
> It may change. Comments and counterexamples are welcome on [the
> repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A *theory builder* is the complete persistent system responsible
for developing and revising the written theories it learns by. Commonplace
is one: it produces a knowledge base for consuming projects, and people
still fill several of its internal roles. This bootstrap program transfers
bounded classes of those internal decisions to computation, one trial at a
time. Each trial tests two things separately: whether computation now makes
the decisions, and whether the builder's own experience teaches it to build
or revise the machinery that makes them. Transferring the best-supported
decisions first should leave people the hardest-to-warrant ones, and what
those still need identifies the functions the builder must grow. The target
is an *autonomous* builder, one whose internal roles are all computational,
whose work is still judged from outside by the projects that consume its
product. No transfer trial has been run.

Commonplace is the starting point: a human-inclusive [theory
builder](../notes/definitions/theory-builder.md), in which agents use and
revise retained project knowledge while people still supply decisive
judgments. The proposed first assessment asks whether consuming projects do better with
its retained changes; internal approval of a note is not that outcome evidence.

## The starting point

A theory builder's boundary follows roles, not people. Users are outside
when they supply questions, cases, evidence, preferences, or acceptance
judgments. An *internal role* is work the builder depends on to develop its
theories, whoever performs it: constructing a first theory, interpreting
what a theory implies, choosing what to blame for a failure, producing or
evaluating a revision, selecting what to retain, and repairing the
machinery. In a human-inclusive builder, agents may draft and revise much of
the content while people diagnose shared causes, revise design assumptions,
choose among passing candidates, and approve new evaluators. An
[autonomous](../notes/definitions/autonomous-theory-builder.md) builder
performs every internal role computationally. Its product is still judged
by its users, which is what keeps it [externally
tested](../notes/definitions/externally-tested-theory-builder.md).

During an assessed run, model weights, adapters, embedding models,
parametric routers, and parametric critics all stay fixed. The program's
hypotheses restrict an assessment to models publicly available as of
2026-09-17; the bootstrap may use newer models before an assessed run.

## Two kinds of transfer

The program measures two kinds of transfer separately. Each trial declares a
boundary: the decisions being assessed.

| Claim | What must be shown |
|---|---|
| **Operational transfer** | Computation makes the declared internal decisions, including hard cases, without human decisions. External outcomes and costs remain acceptable. |
| **Learning transfer** | Evidence from the builder's own work causes it to produce or revise the machinery that makes those decisions, and the retained change affects later work. |

The difference shows in a simple case. A validator that a person wrote can
complete operational transfer: computation now makes the decision. Learning
transfer requires the builder to have produced or revised the validator's
criterion and machinery from its own experience. In the lead article's
terms, learning transfer is [theory refinement turned on the builder's own
machinery](./learning-by-theory-refinement-with-fixed-models.md#theory-refinement-and-what-is-new-here),
the reflective case: the refined object is a check, evaluator, or procedure
rather than the delivered product.

The program's [hypotheses](./testing-the-theory-refinement-program.md#the-hypotheses)
allow a human-built seed. The sufficiency hypothesis asks whether a builder
can then reach a reliability target with no person in an internal role,
which presupposes operational transfer of every such role. The reflection
hypothesis asks whether machinery changes that pass through the builder's
theory of itself yield capabilities a matched builder does not gain.
Learning-transfer trials are where evidence for it would come from. The
bootstrap aims at both transfers.

## Commonplace as a seed instance

Commonplace combines retained project knowledge, computational revision, and
checks implemented in code. Notes state claims, scope, evidence, and
dependencies; agents load and revise them. But [governing behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
still depends partly on people in three ways:

- **Admission: which change takes effect.** The [review
  system](../reference/README-REVIEW-SYSTEM.md) records verdicts against pinned
  note and criterion snapshots; choosing which revision is kept is a separate
  decision that a verdict does not make. One episode records [the model
  retrieving theory and producing edits while the operator judged which
  fitted the research program as a
  whole](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).
- **Credit assignment: what a later consequence supports or counts against.**
  The [freshness model](../reference/review-architecture.md) tracks which of
  a review's inputs have changed since its verdict; files the note links to
  count as reading context, not as tracked inputs. Knowing that an input
  changed does not establish that an earlier change caused a later outcome, so
  people still help attribute failures.
- **Authority: what an admitted change may control.** Evidence that bounded
  reviewers passed unread material led to [a validator rule limiting unquoted
  source use](../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md).
  People authorized that evidence to become a binding rule for later artifacts.

These three governing decisions are part of what the bootstrap must transfer.
There has been no externally assessed run, and no demonstration that
computation alone performs these roles.

## The bootstrap program

Bounded decision classes make transfer easier to measure. A trial can focus on
one class, a bundle of coupled decisions, or a broader redesign when the
current division of work is itself the problem. Exploratory trials, run while
people remain involved, can expose which functions the builder still lacks, and
their results should guide which responsibilities to transfer and how to group
them. The next section names those functions.

Measure progress by counting the internal decisions people still make, not the
people: one operator may stop performing one role while retaining several
others. The program needs evidence of transfer without assuming a fixed order
or steady progress at every step.

## The readiness conditions

A transfer is ready, or *warranted*, when the deciding process has the
premises it needs, a settled acceptance rule or grant of authority, and a check
independent enough to reject a plausible harmful candidate. It also needs
continuity when the decision or its evidence arrives after the current run.

If the program transfers its best-supported decisions first, people should
increasingly be left with the decisions that fail one of these conditions: a
missing premise, an unsettled criterion, a weak check, or a delayed
consequence. The [residue
analysis](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
helps identify what those remaining decisions need:

| Why a decision stays human | Possible response |
|---|---|
| A needed premise is unavailable | Representation, retrieval, or acquisition of that premise |
| Acceptance lacks a settled criterion or grant of authority | A usable rule or represented grant within declared limits |
| No independent check can reject a wrong candidate | Verification, criticism with different failure modes, delayed exposure, or an accepted error tolerance |
| The decision arises after the automatic process stops | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | Reduce its cost, change the method, or defer it |

Among ready transfers, value, cost, risk, and dependencies determine what to
try next. The decisions that are not ready each need a different
[function](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md)
to grow before they can move: representation for a missing premise,
interpretation for an unsettled criterion, verification for a missing check,
and continuity for a decision that arrives late. Commonplace currently supplies
these functions with notes, models, code, and retained evidence; a later
builder need not keep them in separate kinds of carrier.

## A possible early trial: learning which checks a Markdown edit needs

This trial would test whether computation can decide which checks a Markdown
edit needs, and whether experience improves later check selection. The [lead
article's release
exporter](./learning-by-theory-refinement-with-fixed-models.md#a-case)
provides a concrete setting: it produces a deployment manifest for an
installer, and duplicate service identifiers make that manifest invalid. The
setting is a small software product because its failures are cheap to
observe. A decision of the same kind arises in Commonplace whenever a
Markdown edit could affect code that reads it.

**A change that challenges the checking policy.** Initially, the exporter reads
only configuration files. Markdown edits receive syntax checks and are exempt
from manifest checks. A retained *dependency account* has two parts: an edit
needs a manifest check when an executable consumer reads the edited file, and
the configured input list identifies every file the exporter reads.

When the exporter starts reading service definitions from named Markdown files
added to that list, the account should lead the builder to extend manifest
checks to those files. A further change introduces snippets that a configured
file includes. An edit to one can pass its syntax check yet produce an invalid
manifest. Revealing that failure after intervening edits would test whether
the builder traces the consequence to the account's second part: the list
identifies entry points, not everything the exporter reads. Later edits to
other affected and unaffected files would test whether it learns more than an
exception for the first failing filename.

**Evidence and authority.** A component trial could supply scripted exporter
changes while the builder inspects source, build configuration, and prior results,
then revises its *check selector* (the procedure that chooses the checks),
along with any supporting tests and the retained account. This bounded trial could begin before a
autonomous builder exists. Authority over the result is split: an
independent manifest check, the *reference judgment*, can reject a claimed
improvement even after the revised selector accepts the edit, and the selector
being evaluated must not control that check.

**Comparisons depend on the claim.** Operational transfer requires useful check
selection within declared outcome and cost limits, without people making the
transferred decisions. Always running the full suite is the baseline: it omits
no available check, so a selector must match its measured outcomes at lower
total cost. The suite itself can still miss defects.
Learning transfer additionally requires evidence that retained changes improve
later decisions. One way to isolate that contribution is to run two copies of
the builder from identical product snapshots, one keeping the revised state and
one with its earlier version restored, on cases the failure did not touch,
while holding fixed every other place the learned information could be carried.

The trial could also support the [evidence supplement's
comparison](./testing-the-theory-refinement-program.md#component-experiments-that-can-run-first)
of an explicit theory with raw records, a descriptive summary, and a
plausible wrong theory. Changes that preserve the initial dependency account
and changes that break it test different predictions: the first should favour
the theory treatment, while the second may cancel or reverse that advantage
until the account is revised. Record initial errors separately from recovery
after feedback, because rapid recovery can hide the initial loss in a whole-run
score. Targeted [interventions on retained
theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
can help distinguish the account's contribution from that of a revised
selector.

**What to settle for an actual trial.** Choose the workload size, feedback
timing, resource limits, repetitions, and decision thresholds for the claim
being tested, before using results to judge it. Report failed and incomplete
runs, variation across repetitions, and the uncertainty of any treatment
difference. Keep operating cost separate from reference-evaluation cost, while
reporting both. Fewer checks can still cost more overall once selection and
learning are included.

People may prepare the workload and provide outcome evidence. Human diagnosis
or policy repair within the transferred role would defeat a claim of autonomous
operation for that run, while still informing the next trial.

## How each trial is specified and evaluated

The example makes explicit what every trial needs before it runs: its decision
class, workload, boundary, objective, horizon, current human contributions,
missing functions, separate transfer claims, and measures of outcomes, costs,
interventions, and reopened roles. Retain failures and reversals as well as
successes so they can inform the next transfer.

Record who made each decision, for which request, and when. A person who fixes
three hard failures each month still holds the diagnosis role. Such
interventions are allowed and recorded during bootstrapping. During an
assessed run, an internal human decision is an intervention: it is recorded,
its result is not credited to the builder, and it defeats a claim of autonomy
for that run. The changes retained from then on no longer form an autonomous
*lineage*, a history of successor states each produced by the builder's own
revision process while the models stay pinned and no person decides.

Transfers can reopen when a new request exceeds a rule's scope or creates a new
human review role. Record the reopened responsibility and test a response:
narrowing its scope, revising the machinery, or restoring human involvement.
Measure change over declared windows rather than assuming each step is
permanent.

[Usefulness, autonomy, warrant, and power are separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md),
and a transfer can raise one while another falls. A self-approving evaluator,
for example, raises autonomy while hiding declining quality. So state which
dimension changed, and retain independent measures of later success, missed
failures, and total cost.

The declared boundary also determines what a comparison can establish. A
benchmark that treats the builder as a worker and holds the client fixed, the
party that chooses the task, writes the brief, and accepts the result, [does
not test the decisions it leaves with the
client](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
Which of those decisions matter depends on their kind. Requirements and
judgments about visible behaviour remain external inputs, so a client may keep
supplying them. Design, diagnosis, or successor selection supplied by the
client is internal work that the bootstrap must record and transfer.

## What learning transfer must produce

Learning transfer requires evidence that experience produces or revises the
builder's project-specific machinery. The seed is outgrown when [learning displaces repeated human
construction of project-specific
knowledge](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
as new work arises. This may show up in new theories, checks, decompositions,
or evaluators, depending on what later work requires.

Not all machinery must be outgrown. General tools such as version control, a
test runner, or a model client may [stay fixed while their scope remains
warranted](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
They become revision targets when new requests exceed what they can supply.

The current approach uses a [proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md):
it produces candidates, evaluates them with a real chance of rejection, and
makes an accepted change take effect. In that loop, admission itself can
transfer in parts, from formatting and routine updates to revisions of the
admission machinery. The endpoint requires all of these decisions to be
computational without fixing the order in which they transfer. The loop is not
the only option. Other update architectures let reward, error, gradients, or a
viability filter (a change stays if the system still works) drive changes
without a separate admission event. What the endpoint requires of any
architecture is the same: an evidence-caused change that takes effect.

## Stop or redirect conditions

Repeated failures under reported test conditions should guide what to repair,
compare, or stop. Different findings challenge different parts of the approach:

- **The proposed retained account makes no causal difference.** Interventions
  on the account still fail to change later decisions in the predicted way,
  even after ruling out *equivalent reconstruction*, the builder rebuilding
  the same understanding from other records.
- **Human internal work does not decrease.** Across comparable workloads,
  interventions persist, transferred roles repeatedly reopen, or each transfer
  creates equal or harder human work elsewhere.
- **Each new request class needs new human design.** A person must supply a new
  ontology, evaluator, or decomposition as the builder takes on new kinds of
  work.
- **Evaluation becomes self-confirming.** The builder's approval is the only
  evidence of quality, while external outcomes stop tracking it.
- **A more direct method performs better at comparable total cost.**
  Reconstruction from raw records, direct search, or model adaptation reaches
  the same result more cheaply, or reaches it more reliably at comparable total
  cost.

These results alone do not refute the sufficiency hypothesis. They
show that this approach, under the tested conditions, is not working or is not
the best use of resources. The records that count as evidence for a transfer
must be able to show these failures too; a history that can only confirm
success is the self-confirming evaluation above.

## Where this leaves the series

The [lead article](./learning-by-theory-refinement-with-fixed-models.md)
supplies the learning paradigm, and the [evidence
supplement](./testing-the-theory-refinement-program.md) supplies the
hypotheses and the protocol under which a consuming project would judge the
result. This program tests a route toward an autonomous builder by measuring
changes in the internal decisions and project-specific machinery supplied by
people. Failed and reopened transfers determine where that route needs
repair.

The transfer analysis does not depend on the product. Applied to a software
house, the internal roles are production roles and the target is a house
meeting the [four witness
conditions](./an-automated-software-house-as-a-second-test-of-theory-refinement.md#what-a-witness-house-must-show).
The [transition-closure
supplement](./transition-closure-and-continuation-reliability.md) defines
continuation reliability for a system that is already adequate; how
human-inclusive operation can lead to such a system is this article's
separate question.
