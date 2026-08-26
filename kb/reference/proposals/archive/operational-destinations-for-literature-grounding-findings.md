---
description: "Proposal (adopted by ADR 081): dated cohort, propagation, and bilateral-isolation design texture behind claim-grained literature disposition and the ordinary-writer prior-art boundary"
type: ../../types/design-proposal.md
tags: [kb-maintenance, review-system]
---

# Operational destinations for literature-grounding findings

> **Archived** (see [archive README](./README.md)). Adopted by [ADR 081](../../adr/081-literature-disposition-is-explicit-and-claim-grained.md): the live claim-grained assessment, conditional isolation branch, and ordinary-writer prior-art boundary now reside in that ADR and the [assessment instruction](../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md). What remains here is the dated cohort state, propagation trace, and bilateral-isolation option texture — design texture only.

Commonplace should not let source-grounding or literature-disposition workshop
closure strand method-bearing findings in `kb/work/`. Most of that disposal is
now complete: [ADR 081](../../adr/081-literature-disposition-is-explicit-and-claim-grained.md)
adopted the claim-grained disposition method and made ordinary prior-art search
an explicit no-change decision. This proposal retains the remaining design
choice: whether a bounded Pirolli result warrants bilateral isolation of target
inventory, source reconstruction, and comparison. It does not preserve the
workshops as historical registers.

## Current state (as of 2026-08-26)

The direct grounding path is already operative. ADRs
[073](../../adr/073-untracked-source-snapshots-require-ingest-grounding.md),
[076](../../adr/076-source-claim-grounding-is-a-promoted-skill.md), and
[078](../../adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md)
put exact retained quotes or a declared pinned snapshot between a named source
dependency and the standard grounding gate. The writer invokes
[`cp-skill-ground`](../../../instructions/cp-skill-ground/SKILL.md), while the
target owns its interpretation and transfer argument. The rollout's decision
not to add normalized claim identifiers is bounded by
[the retained evidence](../../../notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md).
Those results need no second implementation.

All fourteen candidates in the literature-disposition cohort are resolved:
thirteen dated artifact dispositions keep their targets, several after
narrowing, rewriting, attribution repair, or removal of stale material, and one
candidate was removed from the cohort after failing its membership test. ADR
081 now routes an explicit retrospective literature question into [a
claim-grained assessment instruction](../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md),
loaded conditionally by `cp-skill-write-multistage`. The instruction inventories
live claims before source selection, separates source-established units from
the Commonplace remainder, attempts the smallest faithful replacement, and
classifies inbound uses by imported claim.

ADR 081 also selected the write-time boundary. The ordinary writer keeps its
intra-KB duplicate search and named-source guard but does not search for missing
external prior art. Model recall, search results, and topical resemblance may
nominate a reading assignment inside an explicitly bounded assessment; direct
tracked evidence decides the claim. No prior-art assay, validator, or new
command was adopted.

One worked propagation trace also remains methodologically relevant: among
twenty inbound links to a note carrying one defeated claim, one artifact copied
the error, fifteen consumed sound claims, and four were incidental. The count
measured the inspection surface but did not identify the semantic blast radius.
ADR 081 adopted semantic inbound classification without depending on the
numeric rate, so git remains the audit path and no propagation evidence note is
needed.

The source-grounding workshop is now consumed. Its independent Pirolli pass is
retained as [bounded evidence](../../../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md):
three of four support verdicts tightened after source reconstruction,
target-claim inventory, and comparison were separated. The case motivates a
bilateral-isolation control but cannot attribute the change to isolation alone,
because prompts, role decomposition, and intermediate representations also
changed.

## Problem

ADR 081 resolves source selection, claim-grained disposition, semantic inbound
inspection, and the ordinary-writer boundary. It does not resolve how the two
sides of a source comparison are represented. The current multistage path can
reconstruct a source without the incumbent, but the same claim architect later
sees that reconstruction before inventorying the incumbent. A grounding helper
may also inherit target prose from its caller. Closing the workshop without a
durable destination for this residual finding would collapse a specific
comparison-control question into the broader method that exposed it.

Copying every conclusion into prose would fail differently. A methodology that
no operation loads is inert, while a measurement retained without a claim or
decision it warrants becomes an unconsumed casebook. The destination must be
chosen by the force each finding should have.

## Design space

1. **Keep the adopted comparison path unchanged.** The observed verdict change
   remains bounded evidence, and operators may request fresh roles case by
   case. This avoids new context cost but gives no repeatable isolation
   guarantee.
2. **Make bilateral isolation the default for every external-literature
   assessment.** A source-blind role inventories target claims, a target-blind
   role reconstructs the source, and a third role compares frozen outputs. This
   offers the strongest contamination control but prices every assessment for
   three contexts before its benefit is known.
3. **Adopt a risk-triggered branch after a matched test.** Define the cases where
   over-attribution would materially change disposition, then compare the
   adopted method with bilateral isolation on both over-attribution and false
   narrowing. This is the candidate direction; the current case motivates the
   test but cannot select its trigger or prove its effect.

## Disposal register

| Finding | Destination | Operative consumer or terminal state |
|---|---|---|
| Select a source corpus from the exact live claims, not a topical cluster label or famous reading list | The adopted literature-assessment instruction | Resolved by ADR 081: target inventory precedes source selection, and each admitted source is tied to a proposition it could adjudicate |
| Source overlap does not determine artifact disposition | The adopted claim-region disposition and replacement test | Resolved by ADR 081: the operator separates source-established units from the target-local remainder and attempts the smallest faithful replacement |
| Backlinks identify the impact-search population, not the inherited claim | Semantic inbound classification in the adopted instruction | Resolved by ADR 081: raw count prices inspection and rewiring; imported claims determine semantic impact |
| The one-of-twenty propagation result bounds that step | Git history unless an operative decision depends on the rate | Explicit no-change in ADR 081: the instruction uses semantic classification without relying on the measurement's numeric value |
| Write-time grounding does not discover missing prior art | Ordinary writing remains bounded; explicit retrospective questions load the adopted assessment | Resolved for the current system by ADR 081. A future candidacy assay still needs its own trigger, search boundary, budget, and consumption path |
| Model recall can nominate prior art but cannot settle overlap or disposition | A binding boundary in the adopted instruction | Resolved by ADR 081: suggestions create reading assignments that must reach tracked direct evidence, since [candidacy evidence licenses escalation rather than acceptance](../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) |
| A decomposed pass tightened three of four Pirolli support verdicts after a source-blind target inventory and target-blind source reconstruction were given to a separate comparator | The bounded evidence record plus a bilateral-isolation option in an adopted literature-assessment procedure | A prospective test must form the target inventory without source exposure, form the source reconstruction without target exposure, and give only the frozen outputs to a comparator; the existing case motivates this control but does not establish its causal effect |
| Thirteen consecutive keeps may reflect either the cohort or an incumbent-preserving test | The adopted outcome-neutral replacement test | Resolved by ADR 081: keep is not a default, and the cohort-removal case is the negative control that shows the procedure can reject the assessment premise |
| Exact Quotes or snapshot grounding, target-owned interpretation, and no V1 claim identifiers | Existing ADRs, skills, gate, and evidence note | Explicit no-change: do not duplicate these settled results in the new procedure beyond its preconditions |

## Operativity options

ADR 081 selected one named loading path. `cp-skill-write` hands an explicit
external-literature disposition request to `cp-skill-write-multistage`, which
conditionally loads the standalone assessment instruction. Ordinary grounding,
synthesis, revision, and writing do not pay for that branch.

The current
[`cp-skill-write-multistage`](../../../instructions/cp-skill-write-multistage/SKILL.md)
path provides only asymmetric protection. Its claim architect receives a source
reconstruction before receiving the incumbent, then inventories the incumbent
in that same context, so source vocabulary can still shape the target
representation. Likewise, a grounding helper that forks from a caller cannot
guarantee that it has never seen target prose; [ADR
076](../../adr/076-source-claim-grounding-is-a-promoted-skill.md) records that
limitation. True bilateral isolation would create the target
inventory in a fresh source-blind context, create the source reconstruction in
a fresh target-blind context, freeze both, and give only those outputs to a
third comparator. It could be a bounded multistage branch or part of a
standalone literature-assessment instruction.

ADR 081 selected no missing-prior-art machinery for ordinary writing. A future
open-ended review assay could generate candidates only after gaining a trigger,
search boundary, context budget, and consumer. Its output could route reading;
it could not issue a subsumption or novelty verdict from model recall. No new
command is implied.

## Free choices

- Which claims or assessment risks warrant the additional contexts required by
  bilateral isolation, and whether its two frozen inventories remain ephemeral
  or become review evidence.
- What matched cases and outcome measure can distinguish reduced
  over-attribution from increased false narrowing.

## Adoption criteria

- Any adopted bilateral-isolation branch prevents the target-inventory role
  from seeing the source, prevents the source-reconstruction role from seeing
  the target, and gives the comparator only frozen outputs. A prospective
  matched test must check both over-attribution and false narrowing before this
  control becomes the default.
- Any risk-triggered branch states its trigger and names how the instruction
  loads it; existence under `kb/instructions/` is not enough.
- Measurements retain their population and limits. The thirteen keeps do not
  become a general keep rule, the one-of-twenty trace does not become a
  universal propagation rate, and the Pirolli rerun does not become proof that
  isolation caused its tighter verdicts.
- Workshop removal does not wait on this choice because the evidence and open
  design are now durable. This proposal closes only when bilateral isolation
  resolves to an explicit no-change decision or a named operative branch.

## Urgency

There is no immediate production defect: ADR 081 supplies the claim-grained
comparison path and keeps open-ended prior-art search out of ordinary writing.
Bilateral isolation should not become a default until a prospective matched
test separates its effect from prompt, role, and representation changes. The
current evidence justifies that test, not the implementation.

## Risks

- **Inert control.** An isolation branch without a trigger and invocation path
  preserves prose but changes no behavior.
- **Incumbent bias.** Recovery can always find a verbal difference unless the
  replacement test asks whether that difference changes a consumer's warranted
  use.
- **Circular graph warrant.** Existing inbound citations show current use and
  rewiring cost; they do not prove that the cited artifact is the cheapest or
  best home for the imported claim.
- **Discovery inflation.** A prior-art check can turn every write into an
  open-ended survey unless triggers and budgets are explicit.
- **False authority.** Model recall or search ranking can be useful candidacy
  evidence while remaining unfit to decide novelty, subsumption, or
  disposition.
- **Isolation cost.** Fresh target, source, and comparison contexts increase
  assessment cost and may be wasteful for low-risk source uses.
- **False narrowing.** Decomposed comparison may miss a distributed source
  claim or treat vocabulary differences as substantive boundaries. The one
  observed correction does not measure that error mode.
- **Duplicate theory.** The operative procedure should reuse the existing
  transfer, warrant-granularity, and candidacy boundaries rather than restating
  them as new workshop discoveries.

---

Relevant Notes:

- [An independent pass tightened three of four Pirolli grounding verdicts](../../../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md) — rests-on: bounds the observed verdict change and the causal uncertainty that a prospective isolation test must preserve
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — rests-on: bounds which source-side mechanism can warrant a Commonplace transfer
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — rests-on: keeps grounding and propagation judgments at claim rather than document grain
- [Narrowing bought to survive review is paid for in content](../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: supplies the adversarial warning against accepting a defensible but empty local remainder
