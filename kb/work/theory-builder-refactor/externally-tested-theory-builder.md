# Externally tested theory builder

> **Status:** Workshop definition, 2026-09-15; revised 2026-09-17 against the
> [main-path episodes](./main-path-episodes.md). This is the selected research
> path. The [downstream protocol](./commonplace-evidence-protocol.md) and
> episodes are proposed arrangements, not evidence of a completed run.

Every assessed [theory builder](./theory-builder.md) declares an
[evidence interface](./theory-builder.md#evidence-interface): how cases,
consequences, and acceptance judgments reach it, which claims they assess,
and under what assumptions. This definition specifies where outcome
assessment occurs.

An **externally tested theory builder** is a [theory builder](./theory-builder.md)
whose evidence interface supplies all three of the following from outside
the declared boundary, for a stated claim and scope:

1. **An external falsifier.** Application produces consequences assessed
   against an externally supplied outcome contract. A failing test, invalid
   release, bug report, or user's rejection can provide evidence of a failed
   outcome. The signal need not uniquely contradict a particular internal
   theory: the theory, consumer, retrieval, judge, or task setup may need
   investigation.
2. **An external objective.** Acceptance requirements are supplied and
   judged outside the builder. They may remain fixed across many requests;
   a new task need not change the objective. Any change to acceptance
   requirements is declared and assessed separately, following the
   [retention policy's objective clause](./theory-retention-policy.md#the-objective-clause).
3. **An outcome level independent of the builder's evaluators.** Work is
   assessed without treating the builder's internal approval of a theory or
   revision as the outcome judgment. This is independence of roles, not a
   guarantee of correct measurement, unbiased judges, or statistically
   independent evidence. Internal approval and external acceptance can each
   be mistaken.

The paradigm arrangement is a [software house](../../notes/definitions/software-house.md)
whose product operation and users' assessment of visible behaviour supply
this interface. The research-program articles investigate an
[autonomous](./autonomous-theory-builder.md) builder in that arrangement;
the four witness conditions of the
[conjecture article](../../articles/automated-software-houses-with-fixed-llms.md#what-a-witness-house-must-show)
state what its evaluation must show.

The boundary follows roles, not identities. One person can supply external
tasks or judge outputs in one interaction and perform internal diagnosis or
revision in another. Those acts must be recorded separately. A different
person judging can reduce role ambiguity without guaranteeing measurement
quality.

Assessment is also relative to the claim. A builder may have external
assessment of product performance without external assessment of a broader
methodology claim. Success under the interface does not establish every
internal theory or use outside its scope. The third
[episode](./main-path-episodes.md#3-a-broader-claim-without-external-assessment)
shows such a broader claim; entertaining it does not reclassify the whole
builder.

## Evaluation protocol

An evaluation in this path declares the builder's boundary and seed, claim
and population, product versions, task supply, judges, consumption records,
feedback, acquisition mode, budgets, horizon, and stopping rule. It also
states how development evidence is separated from assessment evidence,
prior exposure, and how cases are renewed or reused. A finite evaluation can
support a bounded claim; a limited horizon alone does not invalidate it.

Commonplace's [initial protocol](./commonplace-evidence-protocol.md#learning-evidence-and-assessment-evidence)
reserves final assessment evidence until a candidate is frozen. Feedback
used to construct or select a successor becomes development evidence for
that successor. Adaptive reuse requires a specified information-release
mechanism, sampling assumptions, and enforced budget; merely declaring a
reuse limit or returning binary feedback establishes no validity guarantee.
The [adaptive-evaluation source analysis](../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
is an input to such a protocol, not a theorem that arbitrary user judgments
satisfy its assumptions.

Renewal is an interface property that contributes to this protocol. New
tasks or users can repeat the same misleading acceptance proxy, and a
changing task mix can change a score. They do not guarantee validity or
preserve the objective. Record changes in acceptance requirements or in
what unchanged objective text means; do not credit an easier criterion as
builder improvement. Objective preservation requires its own checks.

Use a comparable frozen seed to assess
[extension](./theory-builder.md#extension), and a human-staffed builder under
the same demands and declared resources for the research comparison. Retain
failures, abstentions, missing feedback, coverage, and costs alongside
accepted outcomes. Establishing that a particular KB change caused a gain
requires matched interventions; attributing it to the methodology that
produced the change requires further evidence.

## Investigation stays inside the main path

Internal diagnosis, active probes, targeted experiments, and requests for
user tests are permitted while consequences of the resulting change still
face the declared external assessment. Record their selection, exposure,
and cost. Passive acquisition is an experiment choice, not a condition of
this definition.

The builder still interprets theories, identifies candidate faults,
produces revisions, selects what to retain, and changes its machinery. An
external failure can motivate a self-theory revision and a machinery repair;
the second [episode](./main-path-episodes.md#2-reflective-machinery-revision)
keeps that reflective work inside this path. The final outcome comparison
does not need to settle whether the original failure arose in interpretation
or in the theory. A claim about that cause does need additional evidence.

## What remains for the general case

A claim whose consequences lack the declared external assessment must say
so and identify the support its proposed use needs. It may remain a
candidate for inquiry. The [general-case obligations](./general-case-obligations.md)
collect the missing contradiction and use rules, comparison level for
objective changes, and interpretation-versus-theory attribution questions.
Those obligations remain open where their owning drafts leave them open;
they do not define what makes a theory tentative.

Even in the main path, an outcome signal alone does not license retention
or codification of every contributing theory. The
[retention-policy draft](./theory-retention-policy.md) owns those use
thresholds and revision-sequence questions. Outcome assessment makes the
main comparison possible without first solving all of them.

## What does not simplify

Credit assignment along the internal path remains necessary for mechanism
claims. A failure may lie in the product theory, the evaluator that admitted
a change, the retrieval that never surfaced the theory, or a skipped check.
The interface can report that the product failed without identifying which
cause to repair. The
[training article](../../articles/the-software-house-as-the-unit-of-training.md#why-this-is-theory-refinement)
lists these as the cases that force a theory of the builder's own path.

The interface also has practical limits. Feedback that arrives late, rarely,
or at great expense limits what can be assessed within a budget. The
[transition-closure supplement](../../articles/transition-closure-and-continuation-reliability.md)
carries this as the input process's effect on the evaluation.

## Consequence for the conjecture

Testing the workshop's [conjecture](./README.md#goal) in a consuming project's
domain begins by declaring and observing its interface. The proposed
Commonplace arrangement takes the product to be the delivered KB and its
supporting software. It tests downstream work under a budget; internal note
approval cannot substitute for that outcome measure. The working conjecture
separates sufficiency from comparison and uses doctrine-edit counts as a
diagnostic. The [plan](./main-path-plan.md#decisions-still-open) records the
remaining adoption and run choices.

Whether broad theory building requires the builder to become a software
house, the [side conjecture](../../notes/an-open-domain-theory-builder-becomes-a-software-house-when-new-domains-require-production-machinery-changes.md),
is unchanged. Commonplace is taken as a KB-producing software house for this
experiment, so that conditional claim is unnecessary as a premise. An
externally assessed domain need not, by that fact alone, be a software house.

## Boundary cases

- **Commonplace's ordinary note-review loop** assesses the note itself. Its
  internal verdicts do not independently assess the note's downstream use.
  Other self-use episodes require their own declared assessment.
- **Commonplace as a KB house** is a candidate under the
  [downstream protocol](./commonplace-evidence-protocol.md). It becomes an
  observed instance only when a consuming project supplies the required
  release, consumption, and outcome records. The draft episodes supply none
  of those measurements.
- **Historical architectures** receive deployment-specific assessments in
  the [boundary-case assessment](./boundary-case-assessment.md). For the
  Darwin Gödel Machine, distinguish staged search evidence from untouched
  transfer assessment and examine continuing responsibility separately. A
  finite experiment is not invalid merely because it is finite; a detected
  proxy failure motivates objective-preservation checks, not a claim that
  renewed users would necessarily catch it. The Gödel-machine classification
  stays under review: an internally represented utility or fixed objective
  alone does not decide where outcome assessment occurs.
