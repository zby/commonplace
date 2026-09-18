---
description: "Evidence supplement: theory-builder boundary and lineage, the three hypotheses with refuters, the externally tested evidence interface, the downstream protocol's shape, component experiments, and boundary cases; a first design, not a result"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/definitions/theory-builder.md
  - kb/notes/definitions/externally-tested-theory-builder.md
  - kb/notes/definitions/reflective-theory-builder.md
  - kb/notes/definitions/autonomous-theory-builder.md
  - kb/notes/definitions/actionable-methodology.md
  - kb/notes/definitions/theory-refinement.md
  - kb/notes/a-claim-without-external-assessment-carries-three-obligations.md
  - kb/notes/retained-theory-intervention-isolates-one-explicit-surface.md
  - kb/notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/an-action-model-matters-only-through-its-consumption-path.md
  - kb/notes/evidence/commonplace-as-a-reflective-system.md
  - kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
---
# How the Theory-Refinement Program Would Be Tested

*Hypotheses, external assessment, protocol shape, and component experiments: a first design*

> **Draft supplement.** This develops the testing side of [Learning by
> Theory Refinement with Fixed
> Models](./learning-by-theory-refinement-with-fixed-models.md). Everything
> here is a first design that needs much more testing before a scored run,
> and it may change. Comments and counterexamples are welcome on [the
> repository's GitHub Discussions
> page](https://github.com/zby/commonplace/discussions).

**TL;DR.** The lead article proposes that a system can learn by refining
written theories while its model weights stay fixed. This supplement says
what would count as evidence for that. The view it denies is that better
outcomes after a change are enough: a gain can come from a different task
mix, more computation, or a person's intervention, and an outcome does not
say which part of a system caused it. So the supplement defines the system
under test, states three hypotheses with what would refute each, and says
what has to come from outside that system for outcomes to be comparable:
failures it does not judge, an objective it does not set, and an outcome
level its own evaluators do not decide. It then gives the shape of the first
protocol, says what a run's path can and cannot show, specifies component
experiments that can run before a whole system exists, and shows where
existing systems fall under the definitions. No run has been performed. The
setup is stated so that it can be criticized, not because it is settled.

## The system under test

A [theory builder](../notes/definitions/theory-builder.md) is the complete
persistent system responsible for developing and revising tentative
theories about the subjects it investigates. The definition matters for
testing because a claim about a learning method is a claim about this whole
system, and the components usually named (a model, a harness, a refinement
algorithm) are each only part of it.

**Boundary.** The builder includes the theories it remains responsible for,
its machinery, and every person or program that fills an internal
theory-building role. Machinery means representations and the procedures
that derive their consequences, repair operators, evaluators, models,
retained instructions, tools, indexes, validators, and the records from
which these can be rebuilt. Users are outside when they supply questions,
cases, evidence, preferences, or acceptance judgments. A person is inside
only when the system depends on them to construct a first theory, interpret
one, choose what to blame, produce or evaluate a revision, select what to
retain, or repair the machinery. The same person can be on both sides in
different interactions. An assessment therefore declares the boundary it
was made against and reports each consequential role as human,
computational, or joint.

**Seed.** The seed is the machinery and theories the builder holds at the
declared start of an assessment. Interventions during the run, and any
extension, are measured against it. Fixed models are a constraint on
particular studies, not part of the definition.

**Persistence and lineage.** Persistence is continuity of responsibility
across demands (the tasks and questions put to the builder), plus lineage:
each successor state is produced through the preceding state's own revision
process. A change installed from outside that process is an intervention.
It is recorded, and its result is not credited to the builder. No
particular component need survive. A lineage that has revised away every
part of its seed is still the same builder. Persistence establishes neither
retention nor learning.

**Extension.** An extension is a retained change to the machinery that
demonstrates capability beyond what the seed delivered, on a stated demand
under a stated budget. The baseline is the same later demand run without
the retained change under matched conditions. The seed's earlier score on
an earlier demand is not the baseline, because a gain between episodes
confounds the change with task drift, model variance, and scoring noise.
[PAST-Bench](../sources/past-bench-personal-agents-pdf.ingest.md) builds
its evaluation on this matched ablation. Installing a change is not
evidence that later work used it, and use is not evidence that it caused an
improvement. An extension claim therefore needs an observed [consumption
path](../notes/an-action-model-matters-only-through-its-consumption-path.md)
and an outcome comparison.

**Two independent conditions.** A builder is
[reflective](../notes/definitions/reflective-theory-builder.md) when it
refines a causally connected theory of its own theory-building machinery,
its self-theory: machinery changes update the theory, and theory revisions
change the machinery. A builder is
[autonomous](../notes/definitions/autonomous-theory-builder.md) when
computation fills every internal role over the assessed horizon. Neither
implies the other, and neither implies extension, reliability, or the right
to change the objective. Extension is not a third condition; it is the
quantity the hypotheses measure.

## The hypotheses

The program adopted three hypotheses on 2026-09-17. They are quoted as
adopted. "Currently public" means available as of that date; an assessment
declares its model versions and keeps their weights fixed, and hosted
models count.

> **Sufficiency hypothesis.** A training methodology expressed in
> natural-language and symbolic form is
> [actionable](../notes/definitions/actionable-methodology.md) for a
> computational operator using fixed weights from currently public models.
> Without people performing its internal theory-building roles or designing
> a new learning method for each area, the builder develops, retains, and
> uses theories and procedures across declared practical areas. Its later
> work meets a reliability target under a stated budget and external
> assessment protocol. An area is a consuming project's domain with an
> interface that can be declared and observed.

Refuted, for the assessed areas and budget, by a builder that reaches the
target only with a person in an internal role, or only after a new learning
method is designed for an area, or that fails to reach it. Success on one
area supports that area; breadth needs several declared areas and evidence
about transfer between them.

> **Comparative hypothesis.** Under matched demands and declared resources,
> this methodology produces useful capability gains over the frozen seed
> and a baseline that searches the raw records without the learned
> methodology. Its downstream reliability is comparable to a human-staffed
> builder's under a margin set before assessment. The computational
> comparisons use the same fixed-model constraint and account for both
> adaptation and task costs.

Refuted by matched runs in which the frozen seed or the raw-record baseline
does as well at comparable cost, or in which the human-staffed builder
exceeds the preset margin. The raw-record baseline is the important
control: it asks whether the retained methodology adds anything beyond
access to the same records.

> **Reflection hypothesis.** A builder whose machinery changes pass through
> a causally connected self-theory acquires extensions that a matched
> builder without one does not, under the same demands, budget, and
> external assessment. Better downstream outcomes alone do not test this;
> the records of a reflective episode and a matched builder that retains
> content without a self-theory do.

Refuted by a matched builder without a self-theory that acquires the same
extensions under the same conditions, or by reflective episodes whose
records show the machinery changes did not pass through the self-theory.

None of the three promises success on every problem or within every
budget. A finite evaluation supports a bounded claim.

## The evidence interface

Every assessed builder declares an evidence interface: how cases,
consequences, and acceptance judgments reach it, which claims they can
assess, and under what assumptions. An [externally tested theory
builder](../notes/definitions/externally-tested-theory-builder.md) is one
whose interface supplies three things from outside the boundary, for a
stated claim and scope:

1. **An external falsifier.** Applying a theory produces consequences
   judged against an externally supplied outcome contract: a failing test,
   an invalid release, a rejected answer. The signal says the outcome
   failed; it does not locate the fault.
2. **An external objective.** Acceptance requirements are supplied and
   judged outside the builder. A change to them is declared and assessed
   separately.
3. **An outcome level independent of the builder's evaluators.** The
   builder's approval of its own theory or revision is not the outcome
   judgment. This is independence of roles, not a guarantee of correct
   measurement.

With these supplied, an outcome comparison against a human-staffed builder
can proceed before the builder has settled how much support its internal
theories need. Internal diagnosis, active probes, and targeted experiments
stay inside the externally tested case as long as the consequences of the
resulting change still face the external assessment, with their selection
and cost recorded.

For a claim the interface does not assess, [the builder owes three things
for
itself](../notes/a-claim-without-external-assessment-carries-three-obligations.md):
a rule for what counts as a contradiction and what support licenses each
use; a comparison level when a revision changes the acceptance rule; and a
performance measure that does not rest on its own evaluators. The third
raises a further requirement: attributing a failure to its cause. External
assessment does not locate a fault, so a claim that asserts a cause, inside
or outside the externally tested case, needs a trace, intervention, or test
that can discriminate between the theory, its interpretation, retrieval,
execution, and the environment.

That requirement is what reflection evidence must satisfy. A reflective episode
is evidenced by one connected path: externally assessed work exposes a
possible machinery limit; diagnosis revises an identified commitment in the
self-theory; that revision guides a machinery change whose installation
updates the self-theory in turn; later work uses the changed machinery and
its product is assessed externally.

A machinery change followed by better outcomes does not establish that
path. Nor does a predicted behavioural change after altering a commitment,
on its own: instruction-following produces one too. Evidence that a
retained theory was used as an explanation additionally needs predicted
changes on cases the text does not state verbatim, variation of the path by
which the theory is consumed, and an account of whether other records could
supply the same understanding.

The two-way causal connection between Commonplace's methodology notes and
its validators and skills is recorded in [Commonplace as a reflective
system](../notes/evidence/commonplace-as-a-reflective-system.md). That
record supports calling Commonplace reflective today, with people inside
the boundary. It does not show that any reflective episode improved
externally assessed work.

## The first arrangement and its protocol

Commonplace producing a knowledge base for a consuming project is the first
arrangement. The builder includes knowledge-base production, diagnosis,
revision, evaluation, selection, and machinery maintenance. The consumer
receives a versioned release and performs its own tasks. Task suppliers and
output judges are outside. The product is the delivered knowledge base
together with its validators, skills, and indexes. Whether the release
includes the builder's own methodology notes and diagnostic history, or only
the product knowledge base, is a design variable.
[WikiSkill](../sources/wikiskill-persistent-knowledge-for-skill-evolution.ingest.md)
reports lower performance when its solver could read the improvement record
during training, and its authors hypothesize that direct use made the record
less informative for later improvement.

The protocol freezes ten declarations before the first scored episode:

1. the consuming project and its admissible demands;
2. the seed, pinned at run start;
3. the exact model versions for builder and consumer;
4. the task supply rule and how omitted or failed tasks are recorded;
5. the outcome contract per task and who may change it;
6. budget ceilings for compute, time, evidence, and internal human work,
   equal across compared conditions;
7. the horizon and stopping rule, with no stopping when a desired score
   first appears;
8. the reliability target and comparison margin;
9. the feedback fields and their delay;
10. the acquisition mode, a passive stream by default with bounded
    diagnostic probes allowed and charged.

None of these is fixed yet, though a few have a proposed default.

Each episode retains the task and its contract, the delivered versions, the
consumer's configuration, budget usage, the output, the judge's decision and
reason, the feedback returned, and which artifacts the consumer actually
read before a consequential decision. An expectation contract stated per
task before it runs says which artifact should be consulted and what a
wrong-source answer would look like. Conformance to that expected path is
evidence of consultation, not of causal contribution.

Development evidence and assessment evidence are separated. Incoming work
and disclosed feedback drive development. Before the final comparison the
candidate release is frozen and assessed on reserved tasks whose outcomes
have not guided its construction. Once an assessment result is used to
choose or repair a candidate, it becomes development feedback for that
candidate's successors. Any later reuse of a fixed holdout needs a stated
information-release mechanism and an enforced budget. The [adaptive data
analysis
literature](../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
is what to check before designing such reuse, and the protocol does not
assume its theorems already apply to semantic judgments.

Four comparisons supply the evidence for the hypotheses. The matched
ablation, the same later task with a retained change removed, supports an
extension claim. Control runs bound the alternative explanations of a gain:
the task with the retained state removed, with a distractor that resembles
it, with a stale version, and with the wrong mechanism able to supply the
answer. Direct search over the raw records without the learned methodology
tests the comparative hypothesis. A human-staffed builder under the same
demands and resources, with every internal human intervention recorded,
supplies the reliability comparison.

Removing the knowledge base usually removes information the task needs, so
a comparison that removes it measures benefit only. Measuring the harm of
stale or wrong content needs a condition where current authoritative
evidence stays available while the knowledge-base content varies. [The
Memory Trust Gap](../sources/the-memory-trust-gap.ingest.md) makes this
split between its benefit and safety suites.

A consumer's rejection is evidence about the combined task, consumer, and
knowledge-base arrangement, not automatic refutation of a note. Success on
a selected subset does not establish reliable continuation across the
admitted workload.

## What a run's path can and cannot show

The lineage rule says every successor state must arise through the builder's
own process. Stated over a whole run, that gives a definition of which states
the builder could reach, and the definition shows three limits on what a run
establishes.

Take the builder's mutable state to be everything that can affect an update:
its product, theories, tools, evaluators, context assembly, and update
machinery, with model weights fixed. An *admissible path* starts at the seed,
takes inputs allowed by an input process declared in advance, and at each
step moves to a successor the current state permits. A state is reachable
when it occurs on such a path. The path matters, not only the set of inputs:
if the protocol permits request B only after request A, closing the state set
under each permitted input separately would wrongly admit a path that starts
with B. The definition permits self-modification. Rewriting an evaluator
changes what later gets accepted, and the rewrite is itself a step from the
preceding state, so the seed need not specify every later decision.

First, a possible path need not be a practical one. Call a state *adequate*
when the builder in that state can do the assessed work to the declared
target. If the update process can retain arbitrary state, an adequate
successor may be reachable and still extremely unlikely. The quantity a reliability claim needs is *continuation
reliability*: starting from an adequate builder, the chance of sustaining
adequate performance across later demands over the declared horizon within
the budget. A builder that stays adequate for a few demands and then drifts
differs from one that sustains adequacy, even if both pass an early
evaluation. How likely a process is to reach an adequate builder from an
inadequate seed is a different quantity, and it is the [bootstrap
supplement's](./bootstrapping-an-autonomous-theory-builder.md) question.

Second, the input process shapes the evaluation. Three things are distinct:
the set of admissible demand histories, the history realized in one run, and
the procedure that selects histories. Allowing more histories can enlarge the
reachable set without making adequate successors more probable, and a
selection procedure may direct more runs toward failure. The rules may
respond to the builder's actions and introduce new kinds of work, but they
are fixed before the run. The evaluator may not widen or narrow the workload
afterward, and failures stay in the record. The protocol must also say what
counts as success when the builder is nondeterministic: one successful path,
all paths, or a probability threshold. One lucky run does not establish
reliability.

Third, permitted self-modification can suppress adequate successors. The
policies reachable from the seed may exclude adequate states or make them
negligibly likely. An evaluator can govern a rewrite of itself, but the
current machinery must be capable of producing that rewrite, and [a
methodology governs its own extension only as far as it
settles](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).
A human correction during the run breaks the autonomous lineage even if the
machinery could have produced the same result, because the actual path is
what was observed. Successful evaluation supports claims only within [the
domain the available checks
cover](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md).

## Component experiments that can run first

The whole-system protocol waits on a consuming project. The paradigm's
central mechanism can be tested sooner in a bounded component, using the
release-exporter case from the lead article. The design separates three
questions: whether a retained theory influences decisions, whether it
improves transfer and recovery, and whether it reduces the observations
needed to learn.

Run paired continuations: copies of the system that resume work from the
same product snapshot. The copies share the same fixed models, tools,
request sequence, and resource ceilings, and the same source observations,
which each treatment retains in its own form. Vary that form.

| Retained treatment | What the comparison tests |
|---|---|
| An explicit theory with assumptions and scope | Whether a revisable explanation guides useful inference and later updates |
| Raw records of the same observations | Whether synthesis helps beyond reconstructing an account when needed |
| A descriptive summary of those observations | Whether the explanatory account helps beyond compact access to the facts |
| A plausible wrong theory | Whether a specified mistaken premise produces its predicted errors and is corrected after contrary evidence |

Every treatment may revise executable machinery and its tests, and in every
treatment the model may still build an explanation while reasoning. What
differs is what survives to the next decision. Publish the treatment texts,
retained revisions, and the fact inventory they were built from, so a
reader can inspect the differences.

A fifth treatment retaining curated worked cases instead of a general
explanation is the natural next comparison: an explanation reconstructed
and discarded is work repeated on every use, while a retained theory can
carry a mistaken abstraction forward.

Test two kinds of change as separate request histories. In the first,
adding another configured input preserves the theory's account. In the
second, adding indirect includes breaks its exhaustiveness assumption.
Include unaffected files in both, and reserve later edits to different
files for testing transfer.

- **Causal contribution.** A [retained-theory
  intervention](../notes/retained-theory-intervention-isolates-one-explicit-surface.md)
  at a selected decision holds everything else fixed and varies the theory
  text. It should change search, diagnosis, or recovery as predicted, and a
  wrong theory should add a specific error pattern. That establishes
  influence. Explanatory guidance additionally requires correct handling of
  consequences the text does not state and appropriate revision when
  evidence contradicts it.
- **Advantage.** The theory treatment should improve check selection and
  recovery while changes preserve its account. Its advantage may disappear
  or reverse when an assumption breaks and the theory misdirects. Measure
  that misdirection separately from recovery, because rapid recovery can
  hide the initial deficit in a whole-run score.
- **Sample efficiency.** A correct theory may [reduce the observations
  needed to
  adapt](../notes/theory-refinement-may-improve-sample-efficiency-under-shifts.md)
  by letting one discovered dependency change decisions for several files.
  Count inspected cases and feedback used, along with missed defects,
  unnecessary checks, regressions, rollbacks, and total cost including
  theory construction, retrieval, validation, and maintenance.

Report completion and defect counts, resource use, and all paired
differences per treatment and history, with exact binomial intervals for
pass rates. Small samples leave wide uncertainty even when every run
passes. Predeclare the primary comparisons.

A null intervention result does not show the system lacks a theory,
because the system may reconstruct the same understanding from other
retained state. If the controls repeatedly match the theory treatment at
lower cost, the advantage hypothesis fails in that regime. Neither result
settles the whole-system hypotheses.

## Boundary cases

Borderline systems show what each definition requires. These placements are
readings of published sources, not reproduced experiments.

| System | Theory builder? | Externally tested? | Reflective? | Autonomous? |
|---|---|---|---|---|
| FORTE, the classical refinement system | No: one offline run over supplied cases, no continuing responsibility | — | No | Not applicable |
| Schmidhuber's Gödel machine | Open: depends on whether retained content is revised against evidence or by proof alone | Open | Reflective system, yes; reflective builder, open | Every role it has, within what it can prove |
| Darwin Gödel Machine | No continuing responsibility for any agent | External benchmark with a detected proxy failure | — | — |
| Commonplace's note-review loop | Yes, human-staffed | No: a note's approval is internal evaluation | Yes, with the operator inside | No |
| Commonplace producing a knowledge base for a consuming project | Yes | Candidate; observed once release, consumption, and outcome records exist | Yes | No |

The [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
row is the informative one. It is persistent, holds a self-representation,
and rewrites itself computationally under the same requirement that every
successor arise through its own machinery. It admits a rewrite only on a
proof from its current axioms, and it has no route for admitting a fallible
change and recovering from a wrong one. Whether that makes it a theory
builder is assessed per deployment and stays open. The two admission routes
differ as follows.

| | Gödel machine | Theory builder under this program |
|---|---|---|
| Rewrite condition | Proof, under current axioms and utility, that switching pays | A fallible process produces a successor and, where applicable, admits it on evidence |
| External input | Observations enter through formalized operations; rewrites still require proof | The interpreter uses demands, tool results, and consequences to challenge a theory |
| Warrant | Conditional proof relative to the encoded formalization | Empirical warrant bounded by evaluators and later exposure |
| Characteristic failure | A useful change stays unavailable because the proof is not found or not expressible | Harmful successors get enough probability to undermine continued adequacy |

Deductive closure concerns the theorems derivable from the machine's axioms.
The path definition above concerns reachable states. Neither alone
establishes reliable operation.

## Limits

Everything above is design. None of the ten declarations is fixed, no
consuming project has been chosen, and the component experiment has not
been run. The definitions have been checked against constructed episodes,
to see whether the vocabulary can describe a run, and against published
systems, for their borderline cases. Neither check is a run. We expect the
first real run to show a definition to be wrong somewhere. The plan is to
revise the definition and retain the run record as evidence, not to adjust
the protocol so that the definition survives.

Two open questions bound what any result would establish. First, whether
revisions that are each justified by their own evidence compose into a
justified lineage is unsettled, and once an evaluation result guides the
next revision the ordinary generalization argument no longer applies
without a reuse protocol. Second, no standard separates an interpretation
error from a theory error. An outcome comparison records a failure without
attributing it, and every causal claim needs its own discriminating test.

Three further questions are open for any protocol. What evidence would
establish useful continuation reliability for a given product and risk
level. How a protocol keeps relevant novelty in the workload while
preventing removal of failed demands after the fact. And which
environmental state must be represented inside the builder, and which
inputs need separately reported provenance and authority.

## Where to go next

The four definitions, [theory
builder](../notes/definitions/theory-builder.md), [externally
tested](../notes/definitions/externally-tested-theory-builder.md),
[reflective](../notes/definitions/reflective-theory-builder.md), and
[autonomous](../notes/definitions/autonomous-theory-builder.md), state their
exclusions, misuse cases, and boundary cases. The [three
obligations](../notes/a-claim-without-external-assessment-carries-three-obligations.md)
note states where the externally tested case ends and records the open
questions. The [software-house
supplement](./an-automated-software-house-as-a-second-test-of-theory-refinement.md) gives
the alternative arrangement with its own conditions, and the [bootstrap
supplement](./bootstrapping-an-autonomous-theory-builder.md) says how
Commonplace's remaining human roles would transfer to computation.