# Externally tested theory builder

> **Status:** Workshop definition, 2026-09-15; revised 2026-09-17 against the
> [main-path episodes](./main-path-episodes.md) and trimmed the same day.
> This is the selected research path. The
> [downstream protocol](./commonplace-evidence-protocol.md) and episodes are
> proposed arrangements, not evidence of a completed run.

Every assessed [theory builder](./theory-builder.md) declares an
[evidence interface](./theory-builder.md#evidence-interface): how cases,
consequences, and acceptance judgments reach it, which claims they assess,
and under what assumptions. This definition specifies where outcome
assessment occurs.

An **externally tested theory builder** is a [theory builder](./theory-builder.md)
whose evidence interface supplies all three of the following from outside
the declared boundary, for a stated claim and scope:

1. **An external falsifier.** Application produces consequences assessed
   against an externally supplied outcome contract: a failing test, an
   invalid release, a bug report, a user's rejection. The signal reports a
   failed outcome; it does not locate the fault among the theory, the
   consumer, retrieval, the judge, or the task setup.
2. **An external objective.** Acceptance requirements are supplied and
   judged outside the builder. They may stay fixed across many requests; a
   change to them is declared and assessed separately under the
   [retention policy's objective clause](./theory-retention-policy.md#the-objective-clause).
3. **An outcome level independent of the builder's evaluators.** Work is
   assessed without treating the builder's internal approval of a theory or
   revision as the outcome judgment. This is independence of roles, not a
   guarantee of correct measurement.

The paradigm arrangement is a [software house](../../notes/definitions/software-house.md)
whose product operation and users' assessment of visible behaviour supply
this interface. The research-program articles investigate an
[autonomous](./autonomous-theory-builder.md) builder in that arrangement;
the four witness conditions of the
[conjecture article](../../articles/automated-software-houses-with-fixed-llms.md#what-a-witness-house-must-show)
state what its evaluation must show.

The boundary follows roles, not identities. One person can judge outputs in
one interaction and perform internal diagnosis or revision in another; the
acts are recorded separately.

Assessment is relative to the claim. A builder may have external assessment
of product performance without external assessment of a broader methodology
claim, and entertaining such a claim does not reclassify the builder. The
third [episode](./main-path-episodes.md#3-a-broader-claim-without-external-assessment)
shows one.

## Evaluation protocol

An evaluation in this path declares the builder's boundary and seed, claim
and population, product versions, task supply, judges, consumption records,
feedback, acquisition mode, control conditions, budgets, horizon, and
stopping rule. It also states how development evidence is separated from
assessment evidence, prior exposure, and how cases are renewed or reused. A finite evaluation
supports a bounded claim.

Commonplace's [initial protocol](./commonplace-evidence-protocol.md#learning-evidence-and-assessment-evidence)
reserves final assessment evidence until a candidate is frozen; feedback
used to construct or select a successor becomes development evidence for
that successor. Adaptive reuse of a fixed set requires a specified
information-release mechanism, sampling assumptions, and an enforced budget,
for which the
[adaptive-evaluation source analysis](../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
is the input.

Controls bound the alternative explanations of a gain: the same task with
the retained state removed, with a distractor that resembles it, with a
stale version of it, and with the wrong mechanism able to supply the
answer. Consumption is scored against an expectation contract that states,
before the task runs, which artifact should be written and read and which
retrieval signal should fire. [PAST-Bench](../../sources/past-bench-personal-agents-pdf.ingest.md)
operationalizes both, and its own finding applies here: conformance to an
expected pathway is evidence of use, not of causal necessity, which
interventions on the artifact establish.

Renewal of the task stream contributes to this protocol without preserving
the objective: new users can repeat the same misleading acceptance proxy,
and a changing task mix can move a score. Changes in acceptance
requirements, or in what unchanged objective text means, are recorded and
not credited as builder improvement.

[Extension](./theory-builder.md#extension) is assessed against a comparable
frozen seed, and the research comparison against a human-staffed builder
under the same demands and declared resources. Failures, abstentions,
missing feedback, coverage, and costs are retained beside accepted outcomes.
A claim that a particular KB change caused a gain requires matched
interventions; attributing it to the methodology that produced the change
requires further evidence.

## Investigation stays inside the main path

Internal diagnosis, active probes, targeted experiments, and requests for
user tests are permitted while the consequences of the resulting change
still face the declared external assessment, with their selection, exposure,
and cost recorded. Passive acquisition is an experiment choice, not a
condition of this definition.

The builder still interprets theories, identifies candidate faults, produces
revisions, selects what to retain, and changes its machinery. An external
failure can motivate a self-theory revision and a machinery repair; the
second [episode](./main-path-episodes.md#2-reflective-machinery-revision)
keeps that reflective work inside this path. The final outcome comparison
does not need to settle whether the original failure arose in interpretation
or in the theory; a claim about that cause needs its own evidence.

## What remains for the general case

Each supplied item removes an obligation the builder must otherwise meet for
itself. A claim whose consequences lack the declared external assessment
must say so and identify the support its proposed use needs; it may remain a
candidate for inquiry. The
[general-case obligations](./general-case-obligations.md) collect the three.

| Supplied by the interface | Obligation in the general case | Owner |
|---|---|---|
| External falsifier | A rule for what counts as a contradiction and what support licenses each use | [Retention-policy draft](./theory-retention-policy.md) |
| External objective | A comparison level for an objective change when no acceptance arrives from outside | The policy's [objective clause](./theory-retention-policy.md#the-objective-clause) and the [Gödel-machine comparison](./goedel-machine-comparison.md) |
| Independent outcome level | Attribution of a failure between interpreting a theory and the theory | The [ideal interpreter](./resource-bounded-ideal-interpreter.md), with its open fidelity questions |

The first obligation applies inside the main path too, for the internal
theories behind an assessed outcome: outcome assessment makes the main
comparison possible without settling their retention thresholds.

## What does not simplify

Credit assignment along the internal path remains necessary for mechanism
claims. A failure may lie in the product theory, the evaluator that admitted
a change, the retrieval that never surfaced the theory, or a skipped check,
and the interface reports only that the product failed. The
[training article](../../articles/the-software-house-as-the-unit-of-training.md#why-this-is-theory-refinement)
lists these as the cases that force a theory of the builder's own path.

Feedback that arrives late, rarely, or at great expense limits what can be
assessed within a budget. The
[transition-closure supplement](../../articles/transition-closure-and-continuation-reliability.md)
carries this as the input process's effect on the evaluation.

## Consequence for the conjecture

Testing the workshop's [conjecture](./README.md#goal) in a consuming
project's domain begins by declaring and observing its interface. The
proposed Commonplace arrangement takes the product to be the delivered KB
and its supporting software and tests downstream work under a budget. The
working conjecture
separates sufficiency from comparison and uses doctrine-edit counts as a
diagnostic; the [plan](./main-path-plan.md#decisions-still-open) records the
remaining adoption and run choices.

Whether broad theory building requires the builder to become a software
house, the [side conjecture](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md),
is unchanged. Commonplace is taken as a KB-producing software house for this
experiment, so that conditional claim is unnecessary as a premise here. An
externally assessed domain is not by that fact a software house.

## Boundary cases

- **Commonplace's ordinary note-review loop** assesses the note itself; its
  verdicts do not independently assess the note's downstream use.
- **Commonplace as a KB house** is a candidate under the
  [downstream protocol](./commonplace-evidence-protocol.md) and becomes an
  observed instance when a consuming project supplies the required release,
  consumption, and outcome records.
- **Historical architectures** receive deployment-specific assessments in
  the [boundary-case assessment](./boundary-case-assessment.md). The Darwin
  Gödel Machine's marker deletion is a detected proxy failure, which
  motivates objective-preservation checks. The Gödel-machine classification
  stays under review: an internally represented utility does not by itself
  decide where outcome assessment occurs.
