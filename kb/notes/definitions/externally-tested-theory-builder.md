---
description: "Definition — an externally tested theory builder gets an external falsifier, an external objective, and an evaluator-independent outcome level from its evidence interface, so outcomes compare without settling internal warrant"
type: kb/types/definition.md
tags: [foundations, self-improving-systems, learning-theory]
---

# Externally tested theory builder

An **externally tested theory builder** is a [theory builder](./theory-builder.md)
whose [evidence interface](./theory-builder.md#evidence-interface) supplies
all three of the following from outside the declared boundary, for a stated
claim and scope:

1. **An external falsifier.** Application produces consequences assessed
   against an externally supplied outcome contract: a failing test, an
   invalid release, a bug report, a user's rejection. The signal reports a
   failed outcome; it does not locate the fault among the theory, the
   consumer, retrieval, the judge, or the task setup.
2. **An external objective.** Acceptance requirements are supplied and
   judged outside the builder. They may stay fixed across many requests; a
   change to them is declared and assessed separately.
3. **An outcome level independent of the builder's evaluators.** Work is
   assessed without treating the builder's internal approval of a theory or
   revision as the outcome judgment. This is independence of roles, not a
   guarantee of correct measurement.

The KB needs the term because each supplied item removes an obligation the
builder must otherwise discharge for itself, and those obligations are where
the general case's unresolved questions live. In this case an outcome
comparison with a human-staffed builder under the same demands can proceed
without first settling the builder's internal warrant policy. The paradigm
arrangement is a [software house](./software-house.md), whose product
operation and users' assessment of visible behaviour supply the interface.

The boundary follows roles, not identities. One person can judge outputs in
one interaction and perform internal diagnosis or revision in another; the
acts are recorded separately. Assessment is relative to the claim: a
builder may have external assessment of product performance without
external assessment of a broader methodology claim, and entertaining such a
claim does not reclassify the builder.

## Evaluation protocol

An evaluation in this path declares the builder's boundary and seed, the
claim and population, product versions, task supply, judges, consumption
records, feedback, acquisition mode, control conditions, budgets, horizon,
and stopping rule. It states how development evidence is separated from
assessment evidence, prior exposure, and how cases are renewed or reused. A
finite evaluation supports a bounded claim.

Final assessment evidence is reserved until a candidate is frozen; feedback
used to construct or select a successor becomes development evidence for
that successor. Adaptive reuse of a fixed set requires a specified
information-release mechanism, sampling assumptions, and an enforced budget,
for which
[generalization in adaptive data analysis](../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
is the input. Renewal of the task stream contributes to the protocol
without preserving the objective: new users can repeat the same misleading
acceptance proxy, and a changing task mix can move a score.

Controls bound the alternative explanations of a gain: the same task with
the retained state removed, with a distractor that resembles it, with a
stale version of it, and with the wrong mechanism able to supply the
answer. Consumption is scored against an expectation contract stating,
before the task runs, which artifact should be written and read.
[PAST-Bench](../../sources/past-bench-personal-agents-pdf.ingest.md)
operationalizes both, with the qualification that conformance to an
expected pathway is evidence of use, not of causal necessity. Each
with-and-without comparison declares what the no-retention condition knows,
since removing retained content usually removes information the task needs
and then measures benefit, not harm; measuring harm needs current
authoritative evidence held available while the content varies, the split
[the Memory Trust Gap](../../sources/the-memory-trust-gap.ingest.md) makes
between its benefit and safety suites.

## Investigation stays inside the main path

Internal diagnosis, active probes, targeted experiments, and requests for
user tests are permitted while the consequences of the resulting change
still face the declared external assessment, with their selection,
exposure, and cost recorded. Passive acquisition is an experiment choice,
not a condition of this definition. An external failure can motivate a
self-theory revision and a machinery repair, and that
[reflective](./reflective-theory-builder.md) work stays inside this case.
The final outcome comparison does not need to settle whether the original
failure arose in interpretation or in the theory; a claim about that cause
needs its own evidence.

## What remains for the general case

| Supplied by the interface | Obligation in the general case |
|---|---|
| External falsifier | A rule for what counts as a contradiction and what support licenses each use |
| External objective | A comparison level for an objective change when no acceptance arrives from outside |
| Independent outcome level | A performance measure that does not rest on the builder's own evaluators; without it, an interpretation error and a theory error must be separated, since no outcome absorbs both |

A claim whose consequences lack the declared external assessment must say
so and identify the support its proposed use needs, since
[a claim without external assessment carries three obligations](../a-claim-without-external-assessment-carries-three-obligations.md).
The first applies inside this case too, for the internal theories behind an
assessed outcome: outcome assessment makes the comparison possible without
settling their retention thresholds.

## Scope

- **Credit assignment stays hard.** A failure may lie in the product
  theory, the evaluator that admitted a change, the retrieval that never
  surfaced the theory, or a skipped check, and the interface reports only
  that the product failed. Mechanism claims need the internal path.
- **The interface has practical limits.** Feedback that arrives late,
  rarely, or at great expense limits what can be assessed within a budget.
- **Degrees.** An interface may supply a falsifier for some consequences
  and not others, or acceptance for outcomes but not for the theories
  behind them. The term names the limit in which all three are supplied.

## Exclusions

- A builder whose only assessment is its own review of its theories, even
  when a person performs that review; the operator's acceptance of a
  methodology note is internal evaluation.
- A fixed benchmark that the builder can adapt to without a reuse protocol;
  external is not sufficient.
- The objective-preservation problem: an external interface does not by
  itself catch a proxy the builder has learned to satisfy without the
  outcome.

## Misuse Cases

- Calling a builder externally tested because a person outside it reads
  and approves its theories; approval of a theory is the internal role.
- Treating a task rejection as a refutation of a particular theory; it is
  evidence about the combined task, consumer, and product arrangement.
- Treating internal diagnosis or an active probe as leaving the main path;
  the boundary is about who warrants the outcome, not who investigates.
- Treating renewal of users or tasks as a guarantee that the objective was
  preserved.

## Boundary cases

- **Commonplace's ordinary note-review loop** assesses the note itself; its
  verdicts do not independently assess the note's downstream use.
- **Commonplace producing a KB for a consuming project** is a candidate:
  task outcomes judged by the consumer supply the falsifier and objective,
  and it becomes an observed instance when the release, consumption, and
  outcome records exist.
- **The Darwin Gödel Machine** has an external benchmark with validation
  reused and tests held out, and no continuing responsibility for any
  agent; its marker deletion is a detected proxy failure that motivates
  objective-preservation checks.
- **The Gödel machine** stays under review: an internally represented
  utility or a fixed objective does not by itself decide where outcome
  assessment occurs.

---

Relevant Notes:

- [Theory builder](./theory-builder.md) — defined-in: the system this case specializes and the evidence interface it fixes
- [Software house](./software-house.md) — exemplifies: the paradigm arrangement whose product operation and users supply the interface
- [A claim without external assessment carries three obligations](../a-claim-without-external-assessment-carries-three-obligations.md) — extends: the obligations the interface discharges and the general case must meet
- [Reflective theory builder](./reflective-theory-builder.md) — see-also: reflective work stays inside this case while its consequences face external assessment
- [Revising an improvement objective is licensed from outside it or is not improvement](../revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: why the external objective is what licenses objective change
- [Warranted autonomy is bounded by oracle domain](../warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: an external check discriminates only within its domain
