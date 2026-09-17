# Main-path plan: completion record

> **Status:** Workshop plan, 2026-09-17, revised the same day after Astra's
> review and implemented in commits `2567ad4c`, `5f57a709`, and `c10463a1`.
> Trimmed to a completion record in the cleanup; the step-by-step version is
> in git history. The [implementation review](./implementation-review.md)
> owns the review dispositions and remaining promotion conditions.

## Purpose

Concentrate the research program on one main path, the
[externally tested theory builder](../../notes/definitions/externally-tested-theory-builder.md),
and keep the general case as a boundary that tells an agent when a claim has
left the main path. The operator chose this on 2026-09-17 after the
definitions review found that the general definitions exist to replace what
the special case's evidence interface supplies from outside.

The selected [ingests](./ingest-plan-from-astra-review.md) provide examples
and limits, not a general theorem about successful systems. The main path is
chosen because its outcomes can be assessed outside the builder and compared
with a human-staffed builder under declared conditions.

## Decisions applied

Operator direction of 2026-09-17, in the order given:

1. The externally tested theory builder is the main path. The general case
   is kept as a fence: a list of what a builder must supply for itself when
   a claim lacks external assessment, with open questions marked open.
2. The workshop uses Popper's tentative theory as a borrowed term, with the
   structure left in the theory-refinement definition and the policy clauses
   moved to [theory retention and use](../../notes/a-claim-without-external-assessment-carries-three-obligations.md). Done
   in `b7520224`. The later library migration follows the
   [KB adoption plan](./tentative-theory-kb-adoption-plan.md).
3. Commonplace's product is a knowledge base built for consuming projects.
   Commonplace is then a [software house](../../notes/definitions/software-house.md)
   whose product is its KB and supporting software, and its evidence
   interface is that product's use.

The research target's fixed model weights remain a constraint on the
target, not on the general definitions, which still admit weight learning.

### Where the boundary sits

The fence is about who warrants an outcome, not about who investigates.
Diagnosing an evaluator or retrieval failure, constructing a hypothesis
about the builder's own machinery, choosing an experiment, or requesting a
user test all stay inside the main path while the consequences of the
resulting change still face the declared external assessment. A claim
leaves the main path when the claim being made has no external assessment
of its consequences, for example a methodology note retained on the
builder's own judgment of its worth. Active versus passive evidence
acquisition is a field of the interface, not a boundary.

The operator's remark that the system "does not need to make open-ended
experiments" is read as an experiment constraint, recorded in the
[protocol's](../first-downstream-run/commonplace-evidence-protocol.md) acquisition-mode field,
not as a definitional exclusion of active testing.

## Decisions still open

The implementation uses separate sufficiency and comparative hypotheses,
doctrine-edit counts as a diagnostic, and reflection as a separate
condition. These are the working choices that made the proposal reviewable,
not adopted workshop conclusions. The [README](./README.md#goal) states the
resulting hypotheses. Adoption of these three, together with the definition
destinations, is what triggers promotion and the terminology migration.

The first consuming project, exact models, budgets, task population,
reliability target, comparison margin, and horizon remain run choices. Their
absence blocks a scored evaluation, not protocol drafting. The
[Commonplace protocol](../first-downstream-run/commonplace-evidence-protocol.md) records them.

## Implementation state

| Step | Result |
|---|---|
| 1. Observable Commonplace protocol | [Drafted](../first-downstream-run/commonplace-evidence-protocol.md); run parameters explicit and unfilled; PAST-Bench baseline, controls, and expectation contract added in `ca8a2d95`. |
| 2. Episodes | [Three constructed cases](../first-downstream-run/main-path-episodes.md); no empirical results. |
| 3. Definitions and general-case obligations | Five drafts revised against the episodes and trimmed; [general obligations](../../notes/a-claim-without-external-assessment-carries-three-obligations.md) separated by claim and use. |
| 4. Boundary cases | [Eleven cases assessed](../../reports/retained/theory-builder-boundary-cases-20260917.md), with primary-source checks and access limits. |
| 5. Conjecture | [Working hypotheses restated](./README.md#goal); sufficiency, comparison, and reflection evidence separated. |
| 6. Review and inventory | [Seven review rows and fourteen artifact dispositions](./implementation-review.md) recorded. |
| 7. Promotion and migration | Conditional on adoption; not executed. Workshop closure also requires closing condition 3 to be satisfied or explicitly revised. |

Promotion uses only adopted conclusions. Before it, each definition needs
its own boundary cases restored, since library artifacts may not link into
the workshop, and the boundary-case assessment rows that give no main-path
placement should state one or say open.
