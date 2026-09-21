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

*A research program for moving a system's internal decisions from people to
computation*

> **Draft supplement.** This develops the route from Commonplace today to
> the system that [Conjectural Learning with Fixed
> Models](./conjectural-learning-with-fixed-models.md) would test.
> It may change. Comments and counterexamples are welcome on [the
> repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A *theory builder* is the complete persistent system responsible for
developing and revising addressable tentative theories about the subjects it
investigates. This responsibility does not itself establish successful
learning. Commonplace is one: it produces a knowledge base for consuming
projects, and people still fill several of its internal roles. This bootstrap
program transfers bounded classes of those internal decisions to computation,
one trial at a time. The view it denies is that automating a person's decisions
is by itself progress toward a system that learns. A person can write the
procedure that replaces them, and the system has then learned nothing. So each
trial tests two things separately: whether computation now makes the decisions,
and whether the builder's own experience teaches it to build or revise the
machinery that makes them. Transferring the best-supported decisions first
should leave people the ones hardest to hand over with justification, and what
those decisions still lack shows what the builder has to acquire next. The
target is an *autonomous* builder, one whose internal roles are all
computational, whose work is still judged from outside by the projects that
consume its product. No transfer trial has been run.

## The starting point

The boundary of a [theory builder](../notes/definitions/theory-builder.md)
follows roles, not people. Users are outside when they supply questions,
cases, evidence, preferences, or acceptance judgments. An *internal role*
is work the builder depends on to develop its theories, whoever performs
it: constructing a first theory, interpreting what a theory implies,
choosing what to blame for a failure, producing or evaluating a revision,
selecting what to retain, and repairing the machinery. In a human-inclusive
builder, agents may draft and revise much of the content while people
diagnose shared causes, revise design assumptions, choose among passing
candidates, and approve new evaluators. An
[autonomous](../notes/definitions/autonomous-theory-builder.md) builder
performs every internal role computationally. Its product is still judged
by its users. That outside judgment is part of what makes a builder
[externally tested](../notes/definitions/externally-tested-theory-builder.md).

During an assessed run, model weights, adapters, embedding models,
parametric routers, and parametric critics all stay fixed. The program's
hypotheses restrict an assessment to models publicly available as of
2026-09-17; the bootstrap may use newer models before an assessed run.

## Commonplace as a seed instance

Commonplace is the seed, the theories and machinery the program starts from.
It is a human-inclusive theory builder that combines retained project
knowledge, computational revision, and checks implemented in code. Notes
state claims, scope, evidence, and dependencies. Agents load, use, and
revise them, but people still supply decisive judgments. [Governing
behaviour-changing
writes](../notes/continual-learning-requires-governing-behaviour-changing-writes.md)
depends partly on people in three ways:

- **Admission: which change takes effect.** The [review
  system](../reference/README-REVIEW-SYSTEM.md) records verdicts against
  pinned note and criterion snapshots. Choosing which revision is kept is a
  separate decision that a verdict does not make. One episode records [the
  model retrieving theory and producing edits while the operator judged
  which fitted the research program as a
  whole](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).
- **Credit assignment: what a later consequence supports or counts against.**
  The [freshness model](../reference/review-architecture.md) tracks which of
  a review's inputs have changed since its verdict. Files the note links to
  count as reading context, not as tracked inputs. Knowing that an input
  changed does not establish that an earlier change caused a later outcome,
  so people still help attribute failures.
- **Authority: what an admitted change may control.** Evidence that bounded
  reviewers passed unread material led to [a validator rule limiting unquoted
  source use](../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md).
  People authorized that evidence to become a binding rule for later artifacts.

These three governing decisions are part of what the bootstrap must
transfer. There has been no externally assessed run, and no demonstration
that computation alone performs these roles. The proposed first assessment
asks whether consuming projects do better with Commonplace's retained
changes. Internal approval of a note is not that outcome evidence.

## Two kinds of transfer

One example runs through this article. When someone edits a Markdown file,
something has to decide which checks the edit needs: a syntax check only, or
also the checks on any program that reads the file. That recurring decision
is a *decision class*. The procedure that makes it, a *check selector*, and
the written account of why it selects as it does are *machinery*. Today a
person may make the decision or write the selector. A [later
section](#a-possible-early-trial-learning-which-checks-a-markdown-edit-needs)
develops the example into a trial.

The program measures two kinds of transfer separately. Each trial declares a
boundary: the decisions being assessed.

| Claim | What must be shown |
|---|---|
| **Operational transfer** | Computation makes the declared internal decisions, including hard cases, without human decisions. External outcomes and costs remain acceptable. |
| **Learning transfer** | Evidence from the builder's own work causes it to produce or revise the machinery that makes those decisions, and the retained change improves later decisions. |

In the example, a check selector that a person wrote can complete
operational transfer: computation now selects the checks. Learning transfer
requires the builder to have produced or revised the selector from its own
experience, for instance after a missed check led to a failed release. The
revised object is then a check, evaluator, or procedure rather than the
delivered product.

Learning transfer is the broader category, and it is not yet reflection. A
builder could satisfy it by patching its selector directly from failure
records, with no retained account of why. The lead article's [reflective
case](./conjectural-learning-with-fixed-models.md#reflection-and-autonomy)
asks for more: a theory of the builder's own machinery, connected to that
machinery in both directions, so that revising the theory changes the
machinery and changing the machinery updates the theory. A learning-transfer
trial supports the reflection hypothesis only when its records show that
path: the failure led to a revision of an identified part of the written
account, that revision guided the change to the selector, the installed
change was reflected back into the account, and later work used the changed
selector under external assessment. The comparison is a matched builder that
retains the same failure records and may patch its selector but keeps no
account.

The program's [hypotheses](./testing-the-conjectural-learning-program.md#the-hypotheses)
allow a human-built seed. The sufficiency hypothesis asks whether a builder
can then reach a reliability target with no person in an internal role,
which presupposes operational transfer of every such role. The reflection
hypothesis asks whether machinery changes that pass through the builder's
theory of itself yield extensions, retained machinery changes that show
capability beyond the seed, which a matched builder does not acquire. The
bootstrap aims at both transfers, and reports separately which
learning-transfer results also meet the reflective standard.

## The bootstrap program

Bounded decision classes make transfer easier to measure. A trial can focus on
one class, a bundle of coupled decisions, or a broader redesign when the
current division of work is itself the problem. Exploratory trials, run while
people remain involved, can expose which functions the builder still lacks, and
their results should guide which responsibilities to transfer and how to group
them. The next section names those functions.

Measure progress in internal decisions people still make, not in people: one
operator may stop performing one role while retaining several others. A raw
count of decisions is not a stable unit either. Automating hundreds of
routine approvals while adding one hard evaluator-design responsibility
would look like progress under a count. So measure over comparable
workloads, per declared decision class, and report three things for each
class: how often a person intervened, how much human effort those
interventions took, and how hard the remaining cases were. Report
responsibilities that a transfer newly created as their own line, not netted
against the decisions it removed. The program needs evidence of transfer
without assuming a fixed order or steady progress at every step.

## The readiness conditions

A transfer is ready, or *warranted*, when the deciding process has the
premises it needs, a settled acceptance rule or grant of authority, and a check
independent enough to reject a plausible harmful candidate. It also needs
continuity when the decision or its evidence arrives after the current run.

If the program transfers its best-supported decisions first, people should
increasingly be left with the decisions that fail one of these conditions: a
missing premise, an unsettled criterion, a weak check, or a delayed
consequence. The [analysis of which decisions are left
behind](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
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
to be in place before they can transfer: representation for a missing premise,
interpretation for an unsettled criterion, verification for a missing check,
and continuity for a decision that arrives late. Commonplace currently supplies
these functions with notes, models, code, and retained evidence; a later
builder need not keep them in separate kinds of artifact.

## A possible early trial: learning which checks a Markdown edit needs

This trial would test whether computation can decide which checks a Markdown
edit needs, and whether experience improves later check selection. The [lead
article's release
exporter](./conjectural-learning-with-fixed-models.md#a-case)
provides a concrete setting: it produces a deployment manifest for an
installer, and duplicate service identifiers make that manifest invalid. The
setting is a small software product because its failures are cheap to
observe. Commonplace has a rule of this kind today, written by a person:
edits confined to Markdown notes run the knowledge-base validators and skip
the code test suite. Whether a result on the exporter carries over to that
rule is not claimed.

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

**Evidence and authority.** A component trial could supply scripted
exporter changes while the builder inspects source, build configuration, and
prior results, then revises its check selector, along with any supporting
tests and the retained account. This bounded trial could begin before an
autonomous builder exists. Authority over the result is split: an
independent manifest check can reject a claimed improvement even after the
revised selector accepts the edit, and the selector being evaluated must not
control that check.

**Comparisons depend on the claim.** Operational transfer requires check
selection within declared outcome and cost limits, without people making the
transferred decisions. A selector that meets those limits has transferred
the decision, whether or not it is cheaper than the alternative. An
efficiency advantage is a further claim. Always running the full suite is
its baseline: the suite omits no available check, so a selector shows an
advantage only by matching the suite's measured outcomes at lower total
cost. The suite itself can still miss defects. A trial declares in advance
which of the two claims it tests and the thresholds for each.

Learning transfer additionally requires evidence that retained changes
improve later decisions. One way to isolate that contribution is to run two
copies of the builder from identical product snapshots, one keeping the
revised state and one with its earlier version restored, on cases the
failure did not involve, while holding fixed every other retained artifact
that could hold the learned information.

The trial could also support the [testing supplement's
comparison](./testing-the-conjectural-learning-program.md#component-experiments-that-can-run-first)
of a retained theory with retained criticisms used to reconstruct one,
records containing only inputs and outcomes, a descriptive summary, and a
plausible wrong theory. Changes that preserve the initial dependency account
and changes that break it test different predictions: the first should
favour the theory treatment, while the second may cancel or reverse that
advantage until the account is revised. Record initial errors separately
from recovery after feedback, because rapid recovery can hide the initial
errors in a whole-run score. Targeted [interventions on retained
theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
can help distinguish the account's contribution from that of a revised
selector.

**What to settle for an actual trial.** Choose the workload size, feedback
timing, resource limits, repetitions, and decision thresholds for the claim
being tested, before using results to judge it. Report failed and incomplete
runs, variation across repetitions, and the uncertainty of any treatment
difference. Keep operating cost separate from the cost of the independent
check, while reporting both. Fewer checks can still cost more overall once
selection and learning are included.

People may prepare the workload and provide outcome evidence. Human diagnosis
or policy repair within the transferred role would defeat a claim of autonomous
operation for that run, while still informing the next trial.

## How each trial is specified and evaluated

The example makes explicit what every trial needs before it runs: its decision
class, workload, boundary, objective, time horizon, current human
contributions,
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
revision process while no person decides.

Transfers can reopen when a new request exceeds a rule's scope or creates a new
human review role. Record the reopened responsibility and test a response:
narrowing its scope, revising the machinery, or restoring human involvement.
Measure change over declared windows rather than assuming each step is
permanent.

[Usefulness, autonomy, warrant, and power are separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md),
and a transfer can raise one while another falls. A self-approving evaluator,
for example, raises autonomy and can hide declining quality. So state which
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
builder's project-specific machinery and that the change improves its later
decisions. The seed is outgrown when [learning
displaces repeated human construction of project-specific
knowledge](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
as new work arises. This may show up in new theories, checks,
decompositions, or evaluators, depending on what later work requires.

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
architecture is the same: an evidence-caused change that takes effect and
improves later decisions.

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
- **Each new kind of request needs new human design.** A person must supply a new
  ontology, evaluator, or decomposition as the builder takes on new kinds of
  work.
- **Evaluation becomes self-confirming.** The builder's approval is the only
  evidence of quality, while external outcomes stop tracking it.
- **A more direct method performs better at comparable total cost.**
  Reconstruction from raw records, direct search, or model adaptation reaches
  the same result more cheaply, or reaches it more reliably at comparable total
  cost.

These results alone do not refute the sufficiency hypothesis. They show that
this approach, under the tested conditions, is not working or is not the
best use of resources. The records that count as evidence for a transfer
must be able to show these failures too. A history that can only confirm
success is the self-confirming evaluation above.

## Where this leaves the series

The [lead article](./conjectural-learning-with-fixed-models.md)
supplies the learning definition and the research arrangement, and the [testing
supplement](./testing-the-conjectural-learning-program.md) supplies the
hypotheses and the protocol under which a consuming project would judge the
result. This program tests a route toward an autonomous builder by measuring
changes in the internal decisions and project-specific machinery supplied by
people. Failed and reopened transfers show which parts of the program need
revision.

The transfer analysis does not depend on the product. Applied to a software
house, the internal roles are production roles and the target is a house
meeting the [four witness
conditions](./an-automated-software-house-as-a-second-test-of-conjectural-learning.md#what-a-witness-house-must-show).
The testing supplement [defines continuation
reliability](./testing-the-conjectural-learning-program.md#what-a-runs-path-can-and-cannot-show)
for a system that is already adequate; how
human-inclusive operation can lead to such a system is this article's
separate question.
