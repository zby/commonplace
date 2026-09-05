---
description: "Commonplace as a human-agent seed, separate operational and learning transfers, and a worked component trial of learning which checks a Markdown edit needs"
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

Commonplace is a seed for this program: agents use and revise retained project
knowledge, while people still supply decisive judgments. The target is a
*witness house* that sustains coherent software change with fixed learned
components and no human production decisions over a declared scope and horizon.
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
An automated house performs every internal role computationally over its
declared scope and horizon.

## Two kinds of transfer

The program measures two kinds of transfer separately.

| Claim | What must be shown |
|---|---|
| **Operational transfer** | Computation makes the declared production decisions, including hard cases, without human decisions. External outcomes and costs remain acceptable. |
| **Learning transfer** | Production evidence causes the house to produce or revise the machinery that makes those decisions, and the retained change affects later work. |

A hand-written validator can complete operational transfer. Learning transfer
requires the house to produce or revise its criterion and machinery from
experience.

The conjecture permits a human-built seed, provided the house applies its
program theory—its understanding of the software's purpose and organization—
revises coherently, and continues reliably without human production decisions.
The separate proposal to [train the house from
production](./the-software-house-as-the-unit-of-training.md) asks whether its
own process can also produce the project-specific machinery. The bootstrap
aims at both transfers.

## Commonplace as a seed instance

Commonplace combines retained project knowledge, computational revision, and
checks implemented in code. Three control problems remain partly human:
*admission* decides which change takes effect; *credit assignment* decides
which earlier decision a later consequence supports or counts against; and
*authority* sets which later behaviour an admitted change may control.

- **Revisable project theory.** Notes state claims, scope, evidence, and
  dependencies. Agents can load them at a decision and revise, supersede, or
  withdraw them when their claims fail.
- **Machinery built from failures.** Evidence that bounded reviewers could pass
  material they had not read led to [a validator rule limiting unquoted source
  use](../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md).
  Other operator corrections persist as instructions.
- **Evaluation records.** The [review system](../reference/README-REVIEW-SYSTEM.md)
  records verdicts against pinned note and criterion snapshots. Review is
  opt-in; a verdict does not decide which revision is kept. Its [freshness
  model](../reference/review-architecture.md) tracks changes to those inputs,
  treating linked files as reading context. It does not establish that an
  earlier change caused a later production outcome.
- **Decision records.** One episode records [the model retrieving retained
  theory and producing edits while the operator selected global
  fit](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).

People still choose objectives, judge fit, attribute failures, accept review
findings, approve gates, and authorize broader changes. There has been no
witness run or demonstrated acquisition of program theory by computation alone.
The governing process, rather than merely the presence of memory, is what the
bootstrap must develop.

## The bootstrap program

Try a bounded decision class, or the smallest inseparable bundle. Build the
functions it lacks, measure the transfer, and use the result to select the next
trial. Count internal decisions still supplied by people: one operator may
stop performing one role while retaining several others.

## The readiness conditions

A warranted transfer requires the necessary premises, a settled acceptance
rule or grant of authority, and a check independent enough to reject a
plausible harmful candidate. It also requires continuity when the decision or
its evidence arrives after the current run.

Transferring ready decisions first should leave people disproportionately
handling missing premises, unsettled criteria, weak checks, and delayed
consequences. The [residue
analysis](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
turns this prediction about the transfer policy into a list of missing
functions:

| Why a decision stays human | What the program must build |
|---|---|
| A needed premise is unavailable | Representation, retrieval, or acquisition of that premise |
| Acceptance lacks a settled criterion or grant of authority | A usable rule or represented grant within declared limits |
| No independent check can reject a wrong candidate | Verification, criticism with different failure modes, delayed exposure, or an accepted error tolerance |
| The decision arises after the automatic process stops | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | No new capacity; wait for the cost to fall |

Among ready transfers, value, cost, risk, and dependencies determine what to
try next. The remaining decisions require different
[functions](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md):
representation, interpretation, verification, and continuity. Commonplace uses
notes, models, code, and retained evidence to supply them; a final house need
not preserve that division.

## A first trial: learning which checks a Markdown edit needs

This proposed pilot transfers the decision about which checks a Markdown edit
must pass. It tests whether experience teaches the house to revise its *check
selector*, the procedure that chooses those checks, and use the revision on
untouched files. The product is a small fixture that exports a configuration
manifest. Scripted product changes supply the workload; building the exporter
is outside the transferred role. The pilot can therefore run before a complete
automated house exists.

**Evidence and authority.** Initially, the build consumes configuration files
and no Markdown. The house receives the source, build configuration, past
check results, and a selector that applies Markdown syntax checks while
exempting Markdown from manifest checks. The theory treatment explains the
exemption by the build's input list, which initially exhausts the files that
can affect the manifest.

The house may inspect the fixture, run checks, and revise its retained account,
selector, and selector tests. Workload edits, reference checks, and scoring
remain outside its write scope. Each decision applies a proposed edit to a
fresh copy of the specified product version. Only the selector, its tests, and
the retained account persist, so an accepted defect cannot contaminate later
cases.

**Workload.** Compare two twelve-decision histories:

| Decisions | Workload | What it tests |
|---|---|---|
| 1–3, identical in both histories | Markdown edits under the original build | The initial exemption |
| 4–6, identical in both histories | The exporter starts reading named Markdown files; valid and invalid edits follow | Applying the existing dependency explanation to new facts |
| 7–9, histories diverge | One adds another named input; the other adds snippets included by a named input | Preserving or breaking the assumption that the input list is exhaustive |
| 10–12 | Edits to untouched files under each history's dependencies | Transfer after the house has had a chance to revise its policy |

At decision seven, a valid edit exercises the new dependency. Decision eight
introduces an invalid manifest while preserving Markdown syntax. An unrelated
edit intervenes before the reference result arrives after decision nine. It
identifies the bad manifest without prescribing a selector change. The report
records a prevented defect if the house rejected the edit, or supplies delayed
evidence against its decision if it accepted it.

The final three decisions contain an invalid edit to a different file with the
same dependency, a valid edit to another consumed file, and a valid edit to an
unrelated file. Randomize their order and file names across repetitions, keeping
them identical within each comparison. Hide the schedule and expected
classifications from the decision process, and withhold final reference
feedback until all three are complete. Adding only the first failing filename
to an exception list will not suffice.

**Comparisons and resources.** Use the four [retained-account
treatments](./the-software-house-as-the-unit-of-training.md#testable-hypotheses):
theory, raw records, descriptive summary, and plausible wrong theory. An
account that treats file extension as decisive predicts missed checks after
Markdown enters the build. Construct each treatment from the same observation
inventory, excluding future cases and answers, and retain later material under
that treatment's rules.

Run ten paired repetitions per history and treatment. Cap each continuation
at 100,000 total model tokens and twenty minutes; exhaustion makes the run
incomplete. Declare exact model versions, sampling settings, treatment texts,
fixture versions, workload orders, and reference outputs before testing. These
are pilot choices, not thresholds for whole-house reliability.

After decision nine, branch each continuation again. Keep the product
identical but restore the initial selector and retained account in the
comparison branch. Freeze policy updates in both branches for the final three
decisions. Better decisions with the retained revision test acquired checking
capacity beyond product changes. Separate [theory
interventions](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
can isolate the explanation's contribution from that of the revised selector.

**Admission and outcomes.** The selected checks determine whether an edit is
accepted. The house may revise its selection policy without human approval,
while a fixed reference process runs the full manifest check on every proposed
edit. Record missed defects, unnecessary checks, and checking CPU time in the
same execution environment. Report reference-evaluation cost alongside the cost
of operating the selector. The reference result can reject an improvement claim
even when the revised gate accepts every edit.

A successful local operational transfer requires completion within the
ceilings, no human production decisions, rejection of the invalid final edit,
acceptance of the two valid final edits, and lower final checking cost than
always running the full suite. Record earlier misses and recovery costs too.
Evidence of learning requires improvement over the restored policy and account;
theory advantage requires improvement over the other treatments.

People prepare the fixture; the harness supplies demands and reference
outcomes. Any human diagnosis, policy edit, or successor choice during a
continuation is an intervention that defeats its operational-transfer claim.
Report every repetition, including failures and paired differences. The pilot
tests this bounded transfer, not reliable operation across an open-ended
workload.

## How each trial is specified and evaluated

The example makes explicit what every local trial needs before it runs:
its decision class, workload, boundary, objective, horizon, current human
contributions, missing functions, separate transfer claims, and measures of
outcomes, costs, interventions, and reopened roles. Retain failures and reversals
as well as successes so they can inform the next transfer.

Record who made each decision, for which demand, and when. A person who fixes
three hard failures each month still holds the diagnosis role. Such
interventions are allowed and recorded during bootstrapping; after a witness
run begins, an internal human decision ends that run and breaks its autonomous
training lineage.

Transfers can reopen when a new demand exceeds a rule's scope or creates a new
human review role. Return that role to the human set until the missing function
is built. Measure change over declared windows rather than assuming each step
is permanent.

[Usefulness, autonomy, warrant, and power are separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).
A self-approving evaluator can hide declining quality, so state which dimension
changed and retain independent measures of later success, missed failures, and
total cost.

The declared boundary also determines what the comparison can establish. A
worker benchmark [does not test the client decisions it holds
fixed](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
Requirements and judgments about visible behaviour remain external inputs;
client-supplied design, diagnosis, or successor selection remains internal
production work that the bootstrap must record and transfer.

## What the house's training must produce

Later transfers must increasingly depend on machinery produced from experience.
The seed is outgrown when [learning displaces repeated human construction of
project-specific knowledge](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
over the claimed scope. The house then produces its own theories, checks,
decompositions, and evaluators.

General tools such as version control, a test runner, or a model client may
[stay fixed while their scope remains
warranted](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
They become revision targets when new demands exceed what they can supply.

In the current approach, a [proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md)
produces candidates, evaluates them with a real chance of rejection, and makes
an accepted change take effect. Admission itself can transfer in parts, from
formatting and routine updates to revisions of the admission machinery. The
endpoint requires these decisions to be computational without fixing their
transfer order. Other update architectures are possible: reward, error,
viability, or gradients can drive changes without a separate admission event.
The requirement is an evidence-caused change that takes effect.

## Stop or redirect conditions

The program may fail. The following patterns, observed in a declared regime,
are reasons to stop or change the approach rather than attempt the next
transfer.

- **Retained state makes no causal difference.** Repeatedly withholding or
  replacing project state does not change later decisions in the predicted
  way.
- **The human set does not decrease.** Interventions per demand do not decrease,
  transferred roles repeatedly reopen, or each transfer creates equal or
  harder human work elsewhere.
- **Each new demand class needs new human design.** A person must supply a new
  ontology, evaluator, or decomposition whenever the scope expands.
- **Evaluation becomes self-confirming.** The house's approval is the only
  evidence of quality, while external outcomes stop tracking it.
- **A more direct method performs better at comparable total cost.**
  Reconstruction from raw records, direct search, or model adaptation reaches
  the same result more cheaply, or reaches it more reliably at comparable total
  cost.

These results alone do not refute the conjecture that a house can exist. They
show that this approach, in the tested regime, is not working or is not the best
use of resources. The same production history that supports a transfer must
also be able to reveal these failures.

## Where this leaves the series

The [conjecture](./automated-software-houses-with-fixed-llms.md) supplies the
witness conditions; the [training proposal](./the-software-house-as-the-unit-of-training.md)
supplies the learning target. This program tests a route toward both by measuring
changes in the production decisions and project-specific machinery supplied by
people. Failed and reopened transfers determine where that route needs repair.
