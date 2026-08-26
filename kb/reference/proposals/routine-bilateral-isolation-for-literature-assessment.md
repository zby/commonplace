---
description: "Proposal: decide whether prospective matched evidence should promote bilateral isolation from a conditional diagnostic to a routine literature-assessment control"
type: ../types/design-proposal.md
tags: [kb-maintenance, review-system]
---

# Routine bilateral isolation for literature assessment

Only one design decision remains open: whether prospective matched evidence
should promote bilateral isolation from the conditional diagnostic adopted by
[ADR 081](../adr/081-literature-disposition-is-explicit-and-claim-grained.md)
to a routine control for all, or a declared class of, external-literature
assessments. This proposal does not reopen the adopted claim-grained
disposition method, its loading path, the ordinary-writer boundary, or the
existing diagnostic branch.

## Current state (as of 2026-08-26)

ADR 081 and [the literature-assessment
instruction](../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md)
already make bilateral isolation operative. They require fresh source-blind
target inventory, target-blind source reconstruction, and comparison of the
two frozen outputs when the user requests independence, a previous comparison
is challenged for cross-side shaping, or the task prospectively evaluates the
method. The source worker invokes `cp-skill-ground`; the multistage workshop
retains the three intermediate artifacts.

The control is not routine. ADR 081 explicitly rejects that option until a
prospective matched test measures both charitable over-attribution and false
narrowing. The retained [Pirolli
case](../../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md)
tightened three of four support verdicts after decomposition, but roles,
prompts, and intermediate representations changed together. It observed only
over-attribution and does not identify isolation as the cause of the change.

Source candidacy, claim-region disposition, semantic inbound classification,
ordinary-writing scope, direct-evidence grounding, and the conditional loading
path are settled by adopted ADRs and instructions. They are current-state
constraints, not options in this proposal.

## Problem

The conditional branch gives stronger information separation than the
ordinary comparison path, but it costs two additional clean contexts and makes
the comparator depend on frozen reconstructions. That may reduce
over-attribution, or it may miss a distributed source claim and increase false
narrowing. The present evidence estimates neither error rate nor the net value
of paying that cost routinely.

A routine policy therefore needs a bounded population, a comparison that
isolates the control closely enough to support attribution, and a declared
promotion rule. Without those, making isolation routine would generalize from
one confounded case.

## Design space

1. **Retain the conditional diagnostic.** Keep the three adopted triggers and
   make no further change. Bilateral isolation remains available for challenged
   comparisons and prospective evaluation without charging every assessment.
2. **Make isolation routine for every explicit literature assessment.** Every
   run pays for the three-context comparison shape, regardless of the likely
   disposition or contamination risk.
3. **Make isolation routine for a predeclared risk class.** An observable
   predicate automatically selects the stronger branch for that class; cases
   outside it retain the current conditional triggers.

No option is selected. A prospective test must distinguish them.

## Forces

- **Contamination protection.** Cross-side exposure can make one
  representation inherit the other side's vocabulary or assumptions.
- **Reconstructive fidelity.** A frozen source representation can omit a
  distributed claim that direct comparison would recover.
- **Cost.** Routine isolation adds clean contexts and review work to every case
  in its selected population.
- **Attribution.** A policy about isolation needs evidence that does not also
  change prompts, roles, representations, or judgment criteria without
  accounting for them.
- **Scope.** Evidence from one source genre, target type, or model may warrant a
  local trigger without warranting a universal default.

## Evidence needed to choose

- Compare runs that differ only in cross-side exposure as closely as practical.
  Hold the target, source evidence, questions, model, prompts, role count,
  intermediate formats, and comparison rubric fixed. If another factor changes,
  report a bundle-level contrast rather than attributing the result to
  isolation.
- Include cases where a source really does establish a distributed or
  differently worded claim and cases where a plausible thematic fit exceeds
  the source evidence. The set must expose both false narrowing and
  over-attribution.
- Predeclare the reference-judgment or adjudication protocol. It must decide
  claim-level support from direct source evidence without inheriting either
  arm's verdict as ground truth.
- Measure disposition-relevant errors in both directions and record the added
  context and review cost. A verdict change alone is not an improvement.

## Operativity options

The existing loader and instruction already execute bilateral isolation, so no
new command, assay, or workflow is needed for any option.

- Retaining the conditional diagnostic requires no system change. Closing this
  proposal would record an explicit no-change result.
- Universal routine use would require an ADR changing ADR 081's default and a
  synchronized edit to step 2 of the assessment instruction.
- Risk-class routine use would require the same two changes plus a predicate
  that the instruction can evaluate before either comparison arm sees the
  opposite side.

## Free choices

- Which target-source cases and risk strata form a credible prospective test.
- What independent adjudication protocol supplies the reference verdicts.
- What reduction in over-attribution would justify the measured
  false-narrowing and context costs.
- Whether a successful result warrants universal routine use or only a risk
  class, and how that class is recognized before comparison.

## Adoption criteria

- Routine use is considered only from a prospective comparison that measures
  both over-attribution and false narrowing against a declared reference
  protocol.
- The evaluation reports its population, all material treatment differences,
  and the incremental context and review cost. A bundled treatment cannot
  license an isolation-specific policy.
- A risk-class policy states an observable trigger and limits its conclusion to
  the tested class. A universal policy needs evidence whose sampling supports
  that broader scope.
- The proposal closes with either an explicit no-change result or an ADR and
  instruction revision that name the selected scope and promotion threshold.

## Urgency

There is no immediate production defect. The conditional diagnostic already
handles independence requests and challenged comparisons. Until a matched
evaluation is worth running, the adopted non-routine policy remains explicit.

## Risks

- **Evaluation confounding.** Fresh roles, prompt changes, or different
  representations can make a matched-looking test identify another bundle.
- **Isolation cost.** Fresh target, source, and comparison contexts increase
  assessment cost and may be wasteful outside the tested population.
- **False narrowing.** Decomposed comparison may miss a distributed source
  claim or mistake vocabulary differences for substantive boundaries.
- **Reference circularity.** A judge derived from either arm can reproduce that
  arm's bias and make the policy appear validated.
- **Scope overreach.** A result from one source genre, target type, or model can
  be promoted beyond the population it tested.

---

Relevant Notes:

- [An independent pass tightened three of four Pirolli grounding verdicts](../../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md) — rests-on: bounds the observed verdict change and the causal uncertainty that a prospective isolation test must preserve
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — rests-on: bounds which source-side mechanism can warrant a Commonplace transfer
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — rests-on: keeps source support and comparison judgments at claim rather than document grain
