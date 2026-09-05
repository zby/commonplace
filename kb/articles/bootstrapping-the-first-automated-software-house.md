---
description: "Commonplace as a seed that still includes people and a bootstrap program that separately transfers production decisions and the machinery that produces them"
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
coding agents may write and test much of the code while people supply
requirements from outside and still fill
internal production roles such as noticing that several failures share one
cause, deciding that a design assumption no longer holds, choosing among
changes that all pass the tests, approving new evaluators, and authorizing
changes with effects beyond the current job.

The [conjecture article](./automated-software-houses-with-fixed-llms.md) draws
the boundary that matters here. An *internal production role* is work the house
depends on to produce the software, whoever performs
it. A person in such a role is inside the house. A person who supplies
requirements, facts, observed outcomes, or acceptance judgments about visible
behaviour is a user and stays outside. An automated house has no person in an
internal production role over its declared scope and horizon.

## Two kinds of transfer

The program measures two kinds of transfer separately.

| Claim | What must be shown |
|---|---|
| **Operational transfer** | Computation now makes the declared production decisions, including hard cases, without a person supplying them. External outcome and cost measures remain acceptable. |
| **Learning transfer** | Production evidence causes the house's own process to produce or revise the project-specific machinery that makes those decisions, and the retained change affects later work. |

A hand-written validator can complete operational transfer. It makes the
declared production decision inside the house without a person being present at
each case. But its criterion still came from a person. It does not complete
learning transfer until the house can produce or revise that criterion and its
machinery from production evidence.

A wholly human-built house can be a witness if it also applies its *program
theory*—its capacity to relate the software to its purpose and new demands—
revises coherently, and operates reliably without human production decisions.
The witness conditions do not require learning transfer. The separate proposal
to [train the house from production](./the-software-house-as-the-unit-of-training.md)
does: its own process must produce or revise project-specific machinery from
evidence. The bootstrap aims at both transfers.

## Commonplace as a seed instance

Commonplace combines retained project knowledge, computational proposal and
revision, and checks implemented in code. Three control problems remain partly
human. *Admission* decides which proposed change takes effect. *Credit
assignment* decides which earlier state or decision a later consequence
supports or counts against. *Authority* sets which later behaviour an admitted
change may control.

- **Explicit project theory supplies revisable assumptions and rationale.**
  Notes state claims, scope, and evidence, and link to the claims they depend
  on. Agents can load them at
  the point of decision. A note shown to be wrong can be revised, superseded, or
  withdrawn, with its address redirected to its replacement.
- **Some recurring failures have produced machinery.** For example, evidence
  that bounded reviewers could pass material they had not read led to [a
  validator rule that limits unquoted source use on the
  artifact](../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md).
  Other repeated operator corrections have been retained as instructions for
  later passes.
- **Review supplies evaluation and provenance, not full admission or credit
  assignment.** The [review system](../reference/README-REVIEW-SYSTEM.md)
  records verdicts against pinned note and criterion snapshots. This shows
  which note and criterion formed the registered baseline and when either one
  changed. Review is opt-in, however, and a verdict does not itself decide which
  change is kept. Its [freshness
  model](../reference/review-architecture.md) also treats linked files as
  reading context rather than freshness inputs. Most importantly, staleness is
  not delayed credit assignment: it does not show that a later production
  outcome was caused by an earlier change.
- **Some episodes record who decided.** One revision records that [the model
  retrieved retained theory, searched over formulations, and produced edits,
  while the operator supplied the decisive judgments about global
  fit](../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md).
  This is the kind of decision record the bootstrap needs.

People still choose objectives, judge whether a claim fits the explicit project
theory, assign blame when a change fails, decide which review findings to
accept, approve new gates, and authorize changes whose effects reach beyond the
current job. Nothing here shows acquisition of program theory by computation
alone, and there has been no witness run in the first article's sense.

A memory file by itself is weaker. It can affect later behaviour, but it may admit
entries without a settled rule, keep wrong entries without tracing later
failures back to them, omit their scope, and leave unclear whether a person or
the harness chose the rule. A harness can add the missing parts. The difference
is the process that governs the file, not the file's name.

## The bootstrap program

Try a bounded decision class, or the smallest coupled bundle that cannot be
separated. Build the functions it lacks, measure the transfer, and use the
result to select the next trial.

The house should require fewer human decisions, not fewer people.
One operator may stop doing one internal production role while still doing
several others.

## The readiness conditions

A decision can be transferred to an automatic process with warrant when that
process has the premises it needs, an acceptance rule or grant of authority
settled enough to apply, and a check independent enough to reject a plausible
harmful candidate. It also needs continuity when the decision or its evidence
arrives after the current run.

If a house first transfers decisions that meet these conditions, the decisions
left with people should disproportionately involve missing premises, unsettled
criteria, weak checks, and delayed consequences. This is a prediction about the
transfer policy, not a claim that every real automation approach already follows
it. The
[residue analysis](../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)
turns the remaining work into a list of missing functions:

| Why a decision stays human | What the program must build |
|---|---|
| A needed premise is unavailable | Representation, retrieval, or acquisition of that premise |
| No objective, criterion, commitment, or grant of authority settles acceptance | A settled rule or represented grant of authority within declared limits |
| No independent check can reject a wrong candidate | Verification, criticism with different failure modes, delayed exposure, or an accepted error tolerance |
| The decision arises after the automatic process stops | Persistent state, scheduling, and later reactivation |
| Transfer is possible but too expensive | No new capacity; wait for the cost to fall |

The table says what is ready; it does not give a full schedule. Among several
ready transfers, value, cost, risk, and dependencies decide which one to try
next. A role whose only missing premise is already recorded may be inexpensive
to transfer. A role with an unsettled criterion must wait for more decided cases. A
role with no usable check must wait for a stronger check or a declared tolerance
for error.

The remaining human decisions require different
[functions](../notes/residue-classes-need-different-mechanisms-so-architecture-is-mixed.md):
representation, interpretation of settled guidance, verification, and
continuity. Commonplace currently implements these through natural-language
notes, LLM interpretation, symbolic checks and scheduling, and retained
evidence. The final house need not keep those forms separate. The program
requires the functions, not a permanent split among notes, models, and code.

## How each trial is specified and evaluated

Declare each local trial before it runs so the result cannot be used to
rationalize its selection after the fact. The declaration records:

- the decision class or coupled bundle;
- the declared workload, boundary, objective, and horizon;
- which decisions people currently supply;
- which premise, rule, check, or continuity mechanism is thought to be missing;
- the separate operational-transfer and learning-transfer claims;
- measures of external outcomes, costs, human interventions, and reopened roles.

Keep the result whether the transfer succeeds, fails, reverses, or later
reopens. The discovered order must include unsuccessful cases.

An operational transfer may precede evidence of learning: a narrow hand-written
rule can automate a routine decision before retained theory has shown a causal
effect. The record must keep the two claims separate.

Admission can also be automated in parts: a deterministic formatter or a
well-tested dependency update may already be admitted automatically. The
training endpoint requires project-specific successors to take effect without
a person choosing them, including revisions to update machinery when evidence
exposes its failure. In a gated architecture this includes admission machinery;
the requirement does not fix when its transfer occurs.

Operational transfer can look complete while a person still handles the cases
that matter. A person who fixes the three hard failures each month still holds
the diagnosis role. The record must show who made the decisions in each class,
for which demands, and when. During the bootstrap, a human intervention is
allowed but must be recorded. After the declared start of a witness run, any
internal diagnosis, successor selection, or state edit by a person ends that
witness run and breaks the human-free training lineage.

Transfers may also reopen. A new demand can show that a rule covered only the
old workload, or that moving one role created another human review role. A
reopened role returns to the human set until the missing function is built. The
program measures the decrease in that set over declared windows; it does not
assume every step is permanent.

A process can operate without people while a self-approving evaluator hides
declining quality.
[Usefulness, autonomy, warrant, and power are separate
dimensions](../notes/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md).
Each transfer claim must say which dimension changed. The program therefore keeps an
independent outcome measure: user-visible success on later demands, failures
the role missed, and total cost.

The wrong benchmark can omit the remaining internal production roles. A test
that compares an agent with a remote programmer while holding the same brief,
tools, feedback, and client fixed measures the worker role under that division
of labour. It [does not test the client decisions it holds
fixed](../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md).
Which of those decisions must transfer depends on the software-house boundary.
A user may request tenant isolation, supply domain facts, or reject visible
behaviour. If the client instead chooses the internal design, diagnoses an
implementation failure, or selects which internal revision takes effect, the
client supplies an internal production decision. The bootstrap must record and
transfer those decisions; ordinary user requirements and feedback remain
permitted external inputs.

## What the house's training must produce

Later transfers must increasingly depend on machinery that the house produces
and retains from production evidence. The seed is outgrown
when [learning displaces repeated human construction of the task-specific
knowledge it supplied](../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)
over the claimed scope. New explicit project theories, checks, decompositions,
and evaluators then come from the house's own process rather than another round
of human design.

This does not require every component to change. General machinery such as the
version-control system, test runner, or model client may [stay fixed when its
scope is warranted](../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md).
It becomes a revision target only when the declared scope needs a change it
cannot supply. The house must produce the project-specific specializations it
needs; it need not change every inherited tool.

In the current explicit-artifact approach, machinery is usually produced
through a [proposal-selection
loop](../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md):
produce candidates, evaluate them with a real chance of rejection, and make an
accepted change take effect. Early in the bootstrap a person may supply the
final rejection. Later, the house automates more of that acceptance. Other
update forms are also allowed. Reward-, error-, viability-, or gradient-driven
updates may change the house without a separate candidate-admission event. The
bootstrap program requires an evidence-caused change that takes effect, not one
permanent update architecture.

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
