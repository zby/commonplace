---
description: "Proposal: route unconsumed literature-grounding findings into executable procedures, bounded evidence, or explicit no-change decisions before their workshops close"
type: ../types/design-proposal.md
tags: [kb-maintenance, review-system]
---

# Operational destinations for literature-grounding findings

Commonplace should not close its source-grounding and literature-disposition
work with method-bearing findings available only in `kb/work/`. This proposal
defines a disposal bundle: each finding must enter an operative instruction or
review path, become bounded evidence needed by that path, resolve to an
explicit no-change decision, or be identified as already carried by the live
system. It does not preserve the workshops as a historical register and does
not decide implementation details before their consumers are chosen.

## Current state (as of 2026-08-26)

The direct grounding path is already operative. ADRs
[073](../adr/073-untracked-source-snapshots-require-ingest-grounding.md),
[076](../adr/076-source-claim-grounding-is-a-promoted-skill.md), and
[078](../adr/078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md)
put exact retained quotes or a declared pinned snapshot between a named source
dependency and the standard grounding gate. The writer invokes
[`cp-skill-ground`](../../instructions/cp-skill-ground/SKILL.md), while the
target owns its interpretation and transfer argument. The rollout's decision
not to add normalized claim identifiers is bounded by
[the retained evidence](../../notes/evidence/quotes-route-rollout-grounded-more-uses-without-earning-claim-ids.md).
Those results need no second implementation.

The first eleven dated dispositions in the fourteen-note cohort all keep the
target, although several required narrowing, rewriting, attribution repair, or
removal of stale material. The working method
selects sources against live claims, separates source-established units from
the Commonplace remainder, applies a recovery test to that remainder, and reads
inbound uses as claim-specific impact evidence. That method is not yet an
instruction a later operation loads.

The ordinary writer performs an intra-KB near-duplicate search and guards a
named external source dependency. It does not look for missing external prior
art. Model recall, search results, or topical resemblance can currently suggest
a source, but no operative rule says whether or how that suggestion reaches
source capture and assessment.

One worked propagation trace also remains methodologically relevant: among
twenty inbound links to a note carrying one defeated claim, one artifact copied
the error, fifteen consumed sound claims, and four were incidental. The count
measured the inspection surface but did not identify the semantic blast radius.
No durable evidence artifact currently retains that bounded result.

## Problem

Deleting the workshops without disposal would produce an asymmetric result.
Commonplace would retain the note repairs and source-grounding machinery but
lose the procedure that selected the sources, distinguished overlap from
subsumption, and decided what local content survived. A future sweep could then
repeat the original topical-corpus error or infer disposition from resemblance
and backlink count.

Copying every conclusion into prose would fail differently. A methodology that
no operation loads is inert, while a measurement retained without a claim or
decision it warrants becomes an unconsumed casebook. The destination must be
chosen by the force each finding should have.

## Design space

1. **Close with no further disposal.** Git retains the change narrative and the
   live notes retain their repairs. This is sufficient only if none of the
   workshop reasoning should govern a later source-selection or disposition
   operation. It loses the reusable method.
2. **Retain one omnibus methodology note.** This preserves the conclusions in a
   searchable artifact but gives procedural rules no binding consumer and
   mixes measurements, system choices, and execution steps under one force.
3. **Route each finding by force.** Put executable selection and disposition
   rules in instructions, retain a bounded measurement only when an operative
   artifact cites it, settle changes to the standard writer or review pipeline
   through an ADR, and record a deliberate no-change result where the evidence
   does not justify machinery. This is the candidate selection.

## Candidate disposal register

| Finding | Candidate destination | Operative consumer or terminal state |
|---|---|---|
| Select a source corpus from the exact live claims, not a topical cluster label or famous reading list | A source-selection step in a reusable literature-assessment instruction | The operation selecting sources first inventories the target's load-bearing claims; topical resemblance may nominate a source but cannot admit it without a named claim it could adjudicate |
| Source overlap does not determine artifact disposition | A literature-disposition procedure that works at claim-region grain | After grounding, the operator separates source-established units from the target-local transfer, synthesis, or boundary and tests whether the intended consumer can recover that remainder from the proposed replacement path |
| Backlinks identify the impact-search population, not the inherited claim | A propagation step in the same disposition procedure | The operator classifies what each inbound consumer imports before estimating semantic impact; raw count remains a rewiring-cost signal |
| The one-of-twenty propagation result bounds that step | A compact `kb/notes/evidence/` artifact only if the adopted procedure or decision cites the measurement | Otherwise git remains the audit path and no evidence note is created |
| Write-time grounding does not discover missing prior art | An explicit pipeline decision: no new check, a deterministic provenance check, a candidacy assay, or a combination | If behavior changes, an ADR names the trigger and consumer and the relevant writer or review instruction implements it; a no-change selection records why the existing intra-KB novelty check remains sufficient |
| Model recall can nominate prior art but cannot settle overlap or disposition | A binding boundary in any adopted prior-art path | A model-produced result emits non-authoritative reading assignments that must reach source capture and direct assessment before affecting a claim, since [candidacy evidence licenses escalation rather than acceptance](../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) |
| The first eleven consecutive keeps may reflect either the cohort or an incumbent-preserving test | An adoption gate on the general disposition procedure, not a standing claim yet | Before codification, an adversarial replacement test must show that the recovery method can reject a merely verbal local remainder and can select merge, retirement, or cohort removal when those are cheaper faithful paths |
| Exact Quotes or snapshot grounding, target-owned interpretation, and no V1 claim identifiers | Existing ADRs, skills, gate, and evidence note | Explicit no-change: do not duplicate these settled results in the new procedure beyond its preconditions |

## Operativity options

The source-selection, recovery, and propagation clauses need one named loading
path. Candidate surfaces are a standalone literature-assessment instruction
invoked by a maintenance or review workflow, or bounded branches in an existing
multistage writing procedure. The standalone surface keeps retrospective
artifact disposition out of ordinary writing; the multistage surface reuses an
existing claim-disposition phase but would load additional work for cases with
no external-prior-art question.

The missing-prior-art choice has a separate delivery space. A deterministic
check can identify absent or malformed provenance routes but cannot discover an
unnamed source. An open-ended review assay can generate candidates, but its
oracle is warranted only to route reading: it cannot issue a subsumption or
novelty verdict from model recall. A combined design may use deterministic
checks for identifiable provenance and the report-kind assay for bounded
reading assignments.

No new command is implied. Instructions and the existing review pipeline are
the default candidates until a concrete state transition requires additional
code.

## Free choices

- Whether source selection and artifact disposition are one instruction or two
  sequential procedures.
- Whether the disposition procedure is a standalone maintenance operation or a
  branch invoked by multistage writing and revision.
- Which claims trigger missing-prior-art candidacy, and what search and context
  budget prevents the check from becoming an unbounded literature review.
- Whether identifiable provenance earns a deterministic validator rule, a
  generated report, or no additional machinery.
- Whether the propagation measurement is needed as durable evidence after the
  operative rule is stated, or whether the bounded result can remain in git.
- What adversarial or negative-control case demonstrates that the recovery test
  discriminates among keep, merge, retire, and cohort-removal outcomes.

## Adoption criteria

- Every row in the disposal register ends in a named operative consumer, a
  bounded evidence artifact consumed by one, an existing artifact that already
  carries it, or an explicit no-change decision.
- The source-selection procedure starts from a claim inventory and records the
  exact claim each admitted source could adjudicate. Topical similarity alone
  cannot select the corpus.
- The disposition procedure tests the smallest faithful replacement path, not
  merely whether any locally worded remainder exists. Its validation includes
  an adversarial or negative-control case capable of producing a non-keep
  outcome.
- Any prior-art discovery path preserves the boundary between candidacy and
  verdict evidence. A suggested source cannot change a target until captured
  evidence is read against the exact claim.
- Every instruction or review change names how it is loaded. No procedure is
  accepted solely because it exists under `kb/instructions/`.
- Measurements retain their population and limits. The first eleven keeps do not
  become a general keep rule, and the one-of-twenty trace does not become a
  universal propagation rate.
- The producing workshops can then be removed without leaving a current
  operation dependent on them.

## Urgency

The only time-sensitive risk is premature codification of the current recovery
test after an all-keep sequence. The adoption criteria above block that move
until the remaining cohort and an adversarial replacement test demonstrate a
discriminating procedure. This does not require an immediate production edit:
the current artifact work already precedes any general-rule decision.

The prior-art path should not be rushed into the ordinary writer. A
recall-backed verdict would automate the provenance failure this work exposed,
while a universal literature search could impose unbounded cost on every note.
Its trigger, authority, and budget are genuine free choices.

## Risks

- **Inert procedure.** A new instruction without an invocation path preserves
  prose but changes no behavior.
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
- **Duplicate theory.** The operative procedure should reuse the existing
  transfer, warrant-granularity, and candidacy boundaries rather than restating
  them as new workshop discoveries.

---

Relevant Notes:

- [A borrowed pattern transfers only as far as source and target share a mechanism](../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — rests-on: bounds which source-side mechanism can warrant a Commonplace transfer
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — rests-on: keeps grounding and propagation judgments at claim rather than document grain
- [Narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: supplies the adversarial warning against accepting a defensible but empty local remainder
