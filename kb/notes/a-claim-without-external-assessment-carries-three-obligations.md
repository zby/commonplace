---
description: "Without external assessment a claim needs its own contradiction-and-support rule, a comparison level for objective change, and a performance measure it does not grade itself, plus attribution when it asserts a cause"
type: types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems, learning-theory, warranted-autonomy]
---

# A claim without external assessment carries three obligations

A [theory builder](./definitions/theory-builder.md) can have some of its
claims assessed from outside its boundary. Full external assessment of a
claim supplies three items:

1. **An external falsifier.** Applying the claim produces consequences
   judged against an outcome contract supplied from outside: a failing
   test, an invalid release, a bug report, a user's rejection. The signal
   reports that an outcome failed, not where the fault lies.
2. **An external objective.** Acceptance requirements are supplied and
   judged outside the builder. They may stay fixed across many requests; a
   change to them is declared and assessed separately.
3. **An outcome level independent of the builder's evaluators.** Work is
   judged without treating the builder's own approval of a theory or
   revision as the outcome judgment. This is independence of roles, not a
   guarantee of correct measurement.

With all three, the builder's outcomes can be compared, for example with a
human-staffed builder's under the same demands, without first proving every
explanation used to produce them. A [software house](./definitions/software-house.md)
whose users assess the program's visible behaviour is one arrangement that
supplies them. The comparison supports performance on the assessed tasks and
conditions. It does not establish each internal theory or any broader scope
the builder proposes. For a claim the three items do not cover, the builder
must supply for itself what they would have supplied:

| Supplied from outside | Obligation without it |
|---|---|
| External falsifier | A rule for what counts as contradiction and what support licenses each use |
| External objective | A comparison level for an objective change |
| Independent outcome level | A performance measure that does not rest on the builder's own evaluators |

The third obligation carries a consequence: attribution. Outside
assessment never supplied it, because an outside signal does not locate a
fault. The section on attribution below states when it binds.

A claim leaves external assessment when its consequences face none, not when
the builder reasons about a failure. This boundary applies to a claim and a
proposed use, not to the builder as a whole. A builder can work on
externally assessed tasks while also retaining broader inquiry candidates;
entertaining an untested idea does not change its category. Which side of
the boundary an act falls on follows roles, not people. One person can
judge outputs in one interaction and diagnose or revise in another; the
acts are recorded separately. Review of the builder's own theories is
internal even when a person outside the rest of the system performs it,
because selecting which theory to keep is a builder operation. An operator's
acceptance of a methodology note is internal evaluation, and Commonplace's
note-review verdicts assess the note, not its downstream use.

## Support for the proposed use

State what would count against the claim, which unit the evidence supports,
and what kind of reliance that support licenses. The supported unit may be
a claim, a conjunction, or a model under a scope, since
[theory warrant is tracked at the finest granularity evidence licenses](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md).
A system-level outcome does not uniquely locate a faulty component or
validate every component of a successful system.

Candidate retention is separate from reliance. A claim may guide an
experiment without being ready for routine use or codification, because
[derivation and inheritance give starting warrant and evidence earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md)
and [current task fit alone does not warrant costly entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md).
Candidates below a use threshold can remain targets for inquiry; storing
them does not make them accepted theory, and calling a theory
[tentative](./definitions/tentative-theory.md) does not
license any use.
[WikiSkill](../sources/wikiskill-persistent-knowledge-for-skill-evolution.ingest.md)
is the paradigm case of this separation built as a system: a skill is
admitted only on strict validation improvement, while the wiki's diagnoses
and rejected proposals are retained regardless of outcome and remain
available to later proposals. [RuleMem](../sources/rulemem-active-rule-memory.ingest.md)
shows the failure when the separation is missing: a likelihood-based
admission score improves aggregate accuracy, and an admitted rule still
overrides explicit contrary evidence.

Assessment of support can itself be wrong. Distinguish actual support from
an evaluator's judgment that it is sufficient; the failure of concern is
[false-positive acceptance becoming operative](./false-positive-generation-is-filtered-before-retention.md).

This obligation also binds inside full external assessment, for the
internal theories behind an assessed outcome: outcome assessment makes the
comparison possible without settling their use thresholds.

## A comparison level for changing an objective

Identify what makes a claimed improvement better when a revision changes
the acceptance rule itself. External users can authorize a changed demand;
the comparison must then report the new objective and distinguish that
change from improvement under the old one. A new request may instead
instantiate the same objective without changing it. When no external
acceptance applies, the builder must state what comparison level licenses
the objective change or refrain from claiming improvement, since
[revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md).
A conceptual revision that changes what the objective commits to is an
objective change even when the objective's text is unchanged, and is
reported as such; the Darwin Gödel Machine agent that deleted the marker
its hallucination detector keyed on is the mechanical instance. This is an
obligation, not an inference that computation prohibits objective change.

Who may change the objective is a separate question from who performs the
builder's operations. An [autonomous](./definitions/theory-builder.md#qualifiers)
builder can still take its acceptance judgments from outside, and a
human-staffed builder can lack them. External assessment does not by itself
preserve the objective either: an outside judge can keep accepting a proxy
the builder has learned to satisfy without the outcome, and renewing users
or tasks does not prevent this, since new users can repeat the same
misleading acceptance proxy.

## A performance measure the builder does not grade itself

When no outside judge supplies the outcome level, a performance claim needs
a measure that does not rest on the builder's own evaluators. The builder's
approval of a theory or revision is an internal evaluation, however careful;
it can support retaining a candidate, not a claim that later work improved.
Candidate measures fix the answers before the change is made and keep the
evaluator that judges them apart from the process that proposed the change:
held-out cases whose outcomes are settled independently, or a comparison
against the same later work run without the change. Such a measure
supports only the contrast it runs, since
[an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md).
Where no such measure is available, the claim is reported as internal
approval and makes no performance claim.

## Attribution beyond the observed outcome

This obligation is conditional. It binds a claim that asserts a cause,
whether or not the claim is externally assessed, and it binds a performance
claim only when no independent outcome level absorbs interpretation and
theory errors together. An external judge may establish that a task failed
while leaving open whether the cause was the product theory, its
interpretation, the evaluator that admitted a change, retrieval that never
surfaced the theory, a skipped check, or the environment. A task rejection
is therefore evidence about the combined task, consumer, and product
arrangement, not a refutation of a particular theory. To assert a
particular cause, specify a discriminating trace, intervention, or test that
could distinguish the alternatives; a plausible explanation is a candidate
for that test. No adopted standard separates an interpretation error from a
theory error; failures are localized with ordinary probes. Failed
attribution limits the causal claim; it does not erase an observed
performance difference under a sound comparison.

## Investigating a failure stays externally assessed

Diagnosing a failure, choosing what to observe, revising a self-theory, or
running an active experiment does not take a claim outside external
assessment while the resulting performance claim still faces it. A diagnosis
may remain provisional while its proposed repair is tested. Internal proxy
tests can guide development; they do not become the external acceptance
criterion because the builder passed them.

For an unsupported extension of scope, record the unassessed consequence,
the intended use, the evidence missing for that use, and the next bounded
test or the reason to defer it.

## Scope

External assessment comes in degrees. An arrangement may supply a falsifier
for some consequences and not others, or acceptance for outcomes but not for
the theories behind them. Feedback that arrives late, rarely, or at great
expense also limits what can be externally assessed within a budget. Each
missing item leaves its own obligation; the case with all three supplied is
the limit, not the usual condition.

## Open Questions

- **Whether locally warranted revisions compose into a warranted lineage.**
  A succession of local approvals does not supply warrant for the sequence:
  once an evaluation result guides the next revision, the later candidate
  depends on the reused evidence, and
  [generalization in adaptive data analysis](../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md)
  shows the ordinary generalization argument no longer applies without a
  protocol. Whether the set of states reachable by warranted revisions is
  closed under the seed objective and the evidence it admits is argued in
  both directions and unsettled.
- **Which consumption paths need different thresholds**, and what evidence
  licenses each.
- **Which dependencies must survive revision.** Dependency maintenance,
  evidential warrant, and selection policy are separate, as the
  [assumption-based TMS](../sources/an-assumption-based-tms.ingest.md) and
  [belief-base contraction](../sources/in-defense-of-base-contraction.ingest.md)
  ingests separate them.
- **Which guarantees concern eventual learning rather than current
  permission to rely.** A convergence guarantee does not warrant the
  current output.

---

Relevant Notes:

- [Theory builder](./definitions/theory-builder.md) — defined-in: the system whose claims these obligations bind, and the operation-based boundary that separates internal review from outside assessment
- [Software house](./definitions/software-house.md) — defined-in: one arrangement whose users supply all three items
- [Theory warrant is tracked at the finest granularity evidence licenses](./theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — grounds: the supported unit may be a claim, conjunction, or model
- [Derivation and inheritance give starting warrant; evidence earns scope](./derivation-and-inheritance-give-starting-warrant-earns-scope.md) — grounds: candidate retention below a use threshold
- [Current task fit alone does not warrant costly entrenchment](./current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — grounds: codification needs more than one fit
- [Revising an improvement objective is licensed from outside it or is not improvement](./revising-an-improvement-objective-is-licensed-from-outside-it.md) — grounds: the comparison level an objective change needs
- [False-positive generation is filtered before retention](./false-positive-generation-is-filtered-before-retention.md) — grounds: misassessed support as the characteristic failure
- [Warranted autonomy is bounded by oracle domain](./warranted-autonomy-is-bounded-by-oracle-domain.md) — grounds: support sufficient for a consumption path at a required confidence
