---
description: "Accepted decision that explicit external-literature disposition uses a claim-grained multistage procedure with an optional isolation control, while ordinary writing does not search for missing prior art"
type: ../types/adr.md
tags: []
status: accepted
---

# 081-Literature disposition is explicit and claim-grained

**Status:** accepted
**Date:** 2026-08-26

## Context

Direct source grounding already separates a named source's retained evidence
from the target's interpretation. It does not answer a different question:
whether external literature makes a local artifact redundant, leaves an
independent transfer or synthesis, or shows that the artifact was selected for
assessment on a false premise.

The literature-disposition workshop exposed three recurring forces. Sources
selected from a topic label miss the exact claims that decide overlap. A
document-level overlap judgment spreads source warrant across claims the source
does not establish. And inbound link count identifies an inspection and
rewiring surface, not which claim consumers import. The completed cohort also
supplied a negative control: one target did not make the alleged
literature-repeating claim and was removed from the cohort without an artifact
edit. A reusable procedure can therefore be adopted without encoding the
cohort's predominately keep-shaped artifact outcomes as a prior.

A bounded Pirolli rerun adds a procedural warning. After source reconstruction
and target-claim judgment were separated, three of four support verdicts became
narrower. The rerun also changed prompts, roles, and intermediate
representations, and it did not test false narrowing. It makes bilateral
isolation a useful diagnostic control, not an established default.

The proposal *Operational destinations for literature-grounding findings*
left one separate choice open: whether missing-prior-art discovery should run
during every ordinary write. Such a search has no natural completeness
boundary, and model recall or search rank can nominate a source without
warranting a novelty or subsumption verdict.

## Decision

1. **External-literature disposition is an explicit multistage branch.** A
   standalone instruction governs source selection and disposition when the
   request explicitly asks whether literature duplicates or subsumes a
   claim-bearing artifact, or asks for a keep, rewrite, thin, merge, retire, or
   cohort decision on that basis. `cp-skill-write-multistage` loads the
   instruction conditionally and supplies reconstruction, audit, promotion,
   and validation. Ordinary grounding, synthesis, and revision do not load it.
2. **The decision unit is a live claim region.** The procedure inventories the
   target before selecting sources, admits sources against exact propositions,
   separates source-established content from the local transfer, synthesis,
   application, counterexample, or boundary, and attempts the smallest
   faithful replacement. A merely verbal remainder does not preserve an
   artifact. The available outcomes include cohort removal, keep, rewrite,
   thin, merge, and retire; none is the default.
3. **Bilateral isolation is a conditional diagnostic control.** Use separate
   fresh target, source, and comparison contexts when the user requests an
   independence control, a previous comparison is challenged for cross-side
   contamination, or the task prospectively evaluates the method. Freeze the
   two independent inventories before comparison and give the comparator only
   those outputs. The target-blind source worker invokes `cp-skill-ground`
   itself; the skill's ordinary `context: fork` from a target-bearing caller
   does not establish isolation. Do not make the control routine until a
   prospective matched test measures both over-attribution and false narrowing.
4. **Inbound links are impact candidates, not warrant.** Each inbound use is
   classified by whether it imports the affected claim, another claim, or
   nothing material. Raw count may price inspection and rewiring but cannot
   decide semantic propagation or artifact value.
5. **Candidacy and verdict authority stay separate.** A user-named source,
   model recollection, search result, or citation graph may create a reading
   assignment. For each admitted source-side claim, the literature procedure
   invokes `cp-skill-ground` rather than reproducing its ingest, Quotes, or
   snapshot decisions. A user-supplied canonical URL may take that skill's
   missing-ingest path. An agent-nominated untracked URL requires user approval
   before it is passed to the skill. The target cannot change until direct
   source evidence is read against the exact claim through the resulting
   Quotes-or-pinned-snapshot path.
6. **Ordinary writing does not search for missing external prior art.** Its
   intra-KB near-duplicate check and named-source dependency guard remain
   bounded as designed. `cp-skill-write` routes an explicit literature
   disposition request to the multistage branch without asking for a second
   confirmation. No absence of candidates within a bounded assessment
   certifies global novelty.
7. **No new assay, validator, command, or propagation evidence note is added.**
   A validator cannot discover an unnamed source. A report-kind assay lacks a
   chosen trigger and search budget and would still carry only candidacy
   authority. The observed propagation trace motivates semantic inbound
   classification, but this decision does not depend on its numeric rate, so
   git remains its audit path.

The user-supplied or separately authorized URL path in decision 5 narrowly
amends ADR 078. Its ordinary-writer boundary remains: a generic named-source
dependency with no tracked ingest stops for a separate ingest run. The
exception applies only inside an explicit literature-disposition assessment,
where source acquisition is itself part of the authorized operation.

## Considered alternatives

**Run external prior-art discovery during every ordinary write.** This would
place source discovery near the point of authorship. Rejected because a
universal search has no justified stopping rule, would turn a bounded writer
into an open-ended survey, and could make an empty result look like a novelty
certificate. Explicit routing captures the cases where the operator actually
needs the comparison.

**Add a deterministic provenance check or a report-kind prior-art assay.** A
deterministic check can validate known provenance but cannot find an unnamed
source; named dependencies already have a guard. An open-ended assay could
nominate sources, but its trigger, budget, and candidate-consumption path are
unsettled, and its model output cannot decide the verdict. Both remain possible
future additions if those missing choices acquire evidence.

**Put the full procedure inside the multistage skill.** This would guarantee a
loading path but enlarge every multistage read with a specialised retrospective
branch. Rejected in favour of a standalone instruction that the skill loads
only on the explicit trigger. The instruction is shipped with the framework in
installed projects, so the conditional route is not checkout-local.

**Make bilateral isolation the default comparison shape.** This would prevent
source wording from shaping the target inventory and target wording from
shaping source reconstruction in every assessment. Rejected because one
confounded four-claim rerun does not estimate the control's benefit, cost, or
false-narrowing risk. The adopted diagnostic triggers preserve the option while
a prospective matched test remains open.

**Retain an omnibus methodology note or the producing workshop.** Either would
preserve the reasoning but give the procedure no binding consumer. Rejected:
the operational rules belong in an instruction, this architectural selection
belongs in an ADR, and git retains the change narrative and unused measurement.

**Generalize the cohort's keep-shaped results.** Rejected because an outcome
frequency does not warrant an outcome prior. The membership failure supplies
the required negative control, and the adopted procedure requires an
adversarial replacement attempt before any keep.

Free choices left open: whether a later prior-art assay is useful as a bounded
candidate generator; which artifact classes, queries, and budgets would
trigger it; whether a prospective matched test justifies making bilateral
isolation routine; and whether repeated propagation measurements eventually
warrant a durable evidence artifact.

## Consequences

An explicit literature-disposition request now reaches one executable method:
claim inventory precedes source selection, source evidence stays scoped to the
claim it supports, a local remainder must survive an adversarial replacement,
and inbound users are inspected by imported claim. Keep and cohort-removal
results can complete without touching the live artifact; merges and
retirements retain their existing user-approval boundaries.

An independence challenge has a defined stronger route rather than an informal
rerun: source-blind target inventory, target-blind source reconstruction, then
comparison of frozen outputs. That route costs two additional clean contexts
and can miss a distributed relation present in the live inputs, so it remains a
diagnostic until prospective evidence measures both error directions.

The method is deliberately expensive when invoked. It may require source
capture, grounding, claim-by-claim comparison, and semantic inspection of
inbound links. Ordinary writing does not pay that cost, but it can still
rediscover known external ideas when no one asks the prior-art question. The
system makes no novelty claim from that silence.

Operativity path: harness selection loads the promoted `cp-skill-write` or
`cp-skill-write-multistage` body. The ordinary writer routes an explicit
request; the multistage skill then reads
`assess-a-claim-bearing-artifact-against-external-literature.md` from the
source-checkout or installed-framework instruction tree and treats it as a
binding decision contract. That instruction invokes `cp-skill-ground` for each
admitted source-side proposition; grounding may invoke `cp-skill-ingest` for an
authorized canonical URL or return the conditional re-ingest route. The
multistage promotion and validation stages carry any selected edit into the
library. No validator enforces the semantic disposition.

Where the decision stops applying: it covers explicit retrospective comparison
of claim-bearing artifacts against external literature. It does not require
continuous novelty surveillance, guarantee exhaustive literature coverage,
or grant source suggestions verdict authority. A future bounded discovery
path can extend the candidate surface without reopening the claim-grained
verdict procedure, provided it preserves that authority boundary.

---

Relevant Notes:

- [Assess a claim-bearing artifact against external literature](../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) — procedure: the claim-grained assessment adopted here
- [Write a KB artifact through multiple stages](../../instructions/cp-skill-write-multistage/SKILL.md) — procedure: the conditional loader and execution workflow
- [Write one KB note](../../instructions/cp-skill-write/SKILL.md) — procedure: the ordinary writer's explicit no-search boundary and handoff
- [Ground a source-dependent claim](../../instructions/cp-skill-ground/SKILL.md) — procedure: the source-resolution and retained-evidence subroutine
- [ADR 076 — Source-claim grounding is a promoted skill](./076-source-claim-grounding-is-a-promoted-skill.md) — see-also: the grounding entry point and inherited-context caveat used by the bilateral-isolation branch
- [ADR 078 — Writers invoke grounding and evidence stays in the ingest](./078-writers-invoke-grounding-and-evidence-stays-in-the-ingest.md) — see-also: the ordinary-writer grounding boundary preserved outside this decision's explicit literature-assessment exception
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) — rests-on: source nomination cannot decide overlap, novelty, or disposition
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — rests-on: external support stays scoped to the exact claim region it licenses
