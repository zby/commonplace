---
description: "Commonplace as a human-agent seed, separate operational and learning transfers, and an illustrative component trial of learning which checks a Markdown edit needs"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md
  - kb/notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md
  - kb/notes/continual-learning-requires-governing-behaviour-changing-writes.md
  - kb/notes/definitions/software-house.md
  - kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md
  - kb/notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md
  - kb/notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md
  - kb/notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md
  - kb/notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md
---
# Bootstrapping the First Automated Software House

*A research program from human-agent production to human-free internal operation*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** A *software house* is the complete persistent system that keeps
changing software for its users. This bootstrap program starts with a house
that includes people and transfers bounded classes of production decisions to
computation. Each trial separately tests whether computation now makes the
decisions and whether production evidence teaches the house to build or revise
the machinery that makes them. Evidence determines which transfer to try next.

Commonplace offers one starting point: agents use and revise retained project
knowledge, while people still supply decisive judgments. The target is a
witness house: a concrete system demonstrating the [conjecture's four
conditions](./automated-software-houses-with-fixed-llms.md#what-a-witness-house-must-show).
During its run, model weights, adapters, embedding models, parametric routers, and
parametric critics all stay fixed, and computation makes every internal production
decision throughout the observed operation. The conjecture's eligibility
cutoff is 2026-09-02; the bootstrap may use newer models before witness testing.
The program records failures, interventions, and reopened roles against
independent outcome and cost measures.

## The starting point

In a human-agent [software house](../notes/definitions/software-house.md),
agents may write and test much of the code while people diagnose shared causes,
revise design assumptions, choose among passing candidates, and approve new
evaluators. These are internal production roles: work the house depends on to
evolve software, whoever performs it.

The [conjecture article](./automated-software-houses-with-fixed-llms.md)
distinguishes these roles from external inputs. Users may supply requirements,
facts, observed outcomes, and acceptance judgments about visible behaviour.
An automated house performs every internal production role computationally.

## Two kinds of transfer

The program measures two kinds of transfer separately. A trial's boundaries
identify the decisions being assessed; they need not fix the house's future
products or responsibilities.

| Claim | What must be shown |
|---|---|
| **Operational transfer** | Computation makes the declared production decisions, including hard cases, without human decisions. External outcomes and costs remain acceptable. |
| **Learning transfer** | Production evidence causes the house to produce or revise the machinery that makes those decisions, and the retained change affects later work. |

The difference shows in a simple case. A validator that a person wrote can
complete operational transfer: computation now makes the decision. Learning
transfer requires the house to have produced or revised the validator's
criterion and machinery from its own experience.

The conjecture allows that: it permits a human-built seed, provided the house
applies its program theory, revises coherently, and continues reliably without
human production decisions. Program theory here means understanding the
software's purpose, organization, and how to handle new requests. An explicit
project theory is one possible written carrier of that understanding, stating
design commitments, causal assumptions, and invariants; the conjecture also
permits reconstructing understanding from records. The separate proposal to
[train the house from production](./the-software-house-as-the-unit-of-training.md)
asks a further question: whether the house's own process can also produce the
project-specific machinery. The bootstrap aims at both transfers.

## Commonplace as a seed instance

Commonplace combines retained project knowledge, computational revision, and
checks implemented in code. Notes state claims, scope, evidence, and dependencies;
agents load and revise them. But [governing behaviour-changing
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

There has been no witness run or demonstrated acquisition of program theory by
computation alone. These governing decisions are part of what the bootstrap
must transfer.

## The bootstrap program

Bounded decision classes make transfer easier to measure. A trial can focus on
one class, a bundle of coupled decisions, or a broader redesign when the
current division of work is itself the problem. Exploratory trials, run while
people remain involved, can expose which functions the house still lacks, and
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
these functions with notes, models, code, and retained evidence; a final house
need not keep them in separate kinds of carrier.

## A possible early trial: learning which checks a Markdown edit needs

One possible trial asks which checks a Markdown edit needs. It would test
whether computation can make that decision and whether experience improves
later check selection. The [training article's hypothetical release
exporter](./the-software-house-as-the-unit-of-training.md#why-this-is-theory-mediated-learning)
provides a concrete setting: it produces a deployment manifest for an installer,
and duplicate service identifiers make that manifest invalid.

**A change that challenges the checking policy.** Initially, the exporter reads
only configuration files. Markdown edits receive syntax checks and are exempt
from manifest checks. A retained explanation relates this exemption to the
build's dependencies and assumes its configured input list is exhaustive.

When the exporter starts reading service definitions from named Markdown files,
the explanation should lead the house to extend manifest checks to those
files. A further change introduces
indirectly included snippets. An edit to one can pass its syntax check yet
produce an invalid manifest. Revealing that failure after intervening edits
would test whether the house traces the consequence to the incomplete dependency
account. Later edits to other affected and unaffected files would test whether
it learns more than an exception for the first failing filename.

**Evidence and authority.** A component trial could supply scripted exporter
changes while the house inspects source, build configuration, and prior results,
then revises its *check selector*, the procedure choosing the checks, and any
supporting tests or retained account. This bounded trial could begin before a
complete automated house exists. Authority over the result is split: an
independent manifest check, the *reference judgment*, can reject a claimed
improvement even after the revised selector accepts the edit, and the selector
being evaluated must not control that check.

**Comparisons depend on the claim.** Operational transfer requires useful check
selection within declared outcome and cost limits, without people making the
transferred decisions. Always running the full suite is the baseline: it misses
nothing, so a selector must match its outcomes at lower cost.
Learning transfer additionally requires evidence that retained changes improve
later decisions. One way to isolate that contribution is to run two copies of
the house from identical product snapshots, one keeping the revised state and
one with its earlier version restored, on cases the failure did not touch,
while holding fixed every other place the learned information could be carried.

The trial could also support the [training article's
comparison](./the-software-house-as-the-unit-of-training.md#testable-hypotheses)
of explicit project theory with raw records, a descriptive summary, and a
plausible wrong theory. Changes that preserve the initial dependency account
and changes that break it test different predictions: the first should favour
the theory treatment, while the second may cancel or reverse that advantage
until the account is revised. Record initial errors separately from recovery
after feedback, because rapid recovery can hide the initial loss in a whole-run
score.
Targeted [interventions on retained theory](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
can help distinguish the account's contribution from that of a revised selector.

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

The example makes explicit what every trial needs before it runs:
its decision class, workload, boundary, objective, horizon, current human
contributions, missing functions, separate transfer claims, and measures of
outcomes, costs, interventions, and reopened roles. Retain failures and reversals
as well as successes so they can inform the next transfer.

Record who made each decision, for which request, and when. A person who fixes
three hard failures each month still holds the diagnosis role. Such
interventions are allowed and recorded during bootstrapping. After a witness
run begins, an internal human decision ends that run: the conjecture's
continuation condition allows none, and the changes retained from then on no
longer form an autonomous *training lineage*, a history of changes made while
the models stay pinned and no person decides.

Transfers can reopen when a new request exceeds a rule's scope or creates a new
human review role. Record the reopened responsibility and test a response:
narrowing its scope, revising the machinery, or restoring human involvement.
Measure change over declared windows rather than assuming each step is permanent.

[Usefulness, autonomy, warrant, and power are separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md),
and a transfer can raise one while another falls. A self-approving evaluator,
for example, raises autonomy while hiding declining quality. So state which
dimension changed, and retain independent measures of later success, missed
failures, and total cost.

The declared boundary also determines what a comparison can establish. A
benchmark that treats the house as a worker and holds the client fixed, the
party that chooses the task, writes the brief, and accepts the result, [does
not test the decisions it leaves with the
client](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
Which of those decisions matter depends on their kind. Requirements and
judgments about visible behaviour remain external inputs, so a client may keep
supplying them. Design, diagnosis, or successor selection supplied by the
client is internal production work that the bootstrap must record and
transfer.

## What the house's training must produce

Learning transfer requires evidence that experience produces or revises the
house's project-specific machinery. The seed is outgrown when [learning
displaces repeated human construction of
project-specific knowledge](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
as new work arises. This may show up in new theories, checks, decompositions,
or evaluators, depending on what later work requires.

General tools such as version control, a test runner, or a model client may
[stay fixed while their scope remains
warranted](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
They become revision targets when new requests exceed what they can supply.

The current approach uses a [proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md):
it produces candidates, evaluates them with a real chance of rejection, and
makes an accepted change take effect. In that loop, admission itself can
transfer in parts, from formatting and routine updates to revisions of the
admission machinery. The endpoint requires all of these decisions to be
computational without fixing the order in which they transfer. The loop is not
the only option. Other update architectures let reward, error, viability, or
gradients drive changes without a separate admission event. What the endpoint
requires of any architecture is the same: an evidence-caused change that takes
effect.

## Stop or redirect conditions

Repeated failures under reported test conditions should guide what to repair,
compare, or stop. Different findings challenge different parts of the approach:

- **The proposed retained account makes no causal difference.** Interventions
  on the account still fail to change later decisions in the predicted way,
  even after ruling out the house rebuilding the same understanding from other
  records (the conjecture article's *equivalent reconstruction*).
- **Human production work does not decrease.** Across comparable workloads,
  interventions persist, transferred roles repeatedly reopen, or each transfer
  creates equal or harder human work elsewhere.
- **Each new request class needs new human design.** A person must supply a new
  ontology, evaluator, or decomposition as the house takes on new kinds of work.
- **Evaluation becomes self-confirming.** The house's approval is the only
  evidence of quality, while external outcomes stop tracking it.
- **A more direct method performs better at comparable total cost.**
  Reconstruction from raw records, direct search, or model adaptation reaches
  the same result more cheaply, or reaches it more reliably at comparable total
  cost.

These results alone do not refute the conjecture that a house can exist. They
show that this approach, under the tested conditions, is not working or is not the best
use of resources. The same production history that supports a transfer must
also be able to reveal these failures.

## Where this leaves the series

The [conjecture](./automated-software-houses-with-fixed-llms.md) supplies the
witness conditions; the [training proposal](./the-software-house-as-the-unit-of-training.md)
supplies the learning target. The [transition-closure supplement](./transition-closure-and-continuation-reliability.md)
defines continuation reliability for a house that is already adequate. How
human-agent production can lead to such a house is this article's separate
question. This program tests a route toward both targets by measuring changes
in the production decisions and project-specific machinery supplied by people.
Failed and reopened transfers determine where that route needs repair.
