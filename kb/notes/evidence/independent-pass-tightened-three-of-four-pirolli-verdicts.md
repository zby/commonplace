---
description: "A Commonplace grounding case changed three of four support verdicts after separating source reconstruction from target-claim judgment, making bilateral isolation a candidate control rather than a proven cause."
type: kb/types/note.md
traits: [title-as-claim, has-comparison, has-external-sources]
tags: [evaluation, kb-maintenance]
---

# An independent pass tightened three of four Pirolli grounding verdicts

In one Commonplace source-grounding case on 2026-08-24, a first pass compared
four claims from [Agents navigate by deciding what to read
next](../agents-navigate-by-deciding-what-to-read-next.md) with [Peter Pirolli's
account of proximal information scent](../../sources/pirolli-proximal-information-scent-distal-content.ingest.md).
The target claims had been inventoried before the source was read, but one
working context then held the target, the source, and the comparison. It
classified C1-C3 as subsumed and C4 as not established.

A second pass separated the roles. One fresh worker reconstructed the source
without the target note or first comparison. A separate judge compared the
frozen C1-C4 inventory with only that source-side reconstruction. It retained
the C4 verdict and tightened the other three:

| Claim | First pass | Separated pass | Boundary the second pass restored |
|---|---|---|---|
| C1: follow/skip is the fundamental unit of navigation | Subsumed | Narrowing needed | The separated pass did not treat the source's navigation-action account as support for the target's fundamental-unit wording. |
| C2: pointer choice combines relevance likelihood with discovery cost | Subsumed | Narrowing needed | Retained source passages separately establish stochastic choice and a value-over-interaction-cost tendency; the pass did not treat them as the target's composed pointer-level trade-off. |
| C3: surrounding pointer context avoids loading the target | Subsumed | Partly supported; narrowing needed | The pass treated the proximal-cue/distal-source structure as supported and the surrounding-context, tractability, and avoided-load additions as target-side transfer. |
| C4: more pointer context makes navigation cheaper | Not established | Not established | Both passes withheld support; [linking theory](../linking-theory.md) now separates cue diagnosticity from consumed context cost. |

The changes mattered to artifact disposition. “Subsumed” could license
replacing the note with a source route. “Needs narrowing” preserves a local
claim or transfer that the source route cannot recover. The separated pass
therefore did more than alter wording: it changed which content appeared to
survive source comparison.

## What this establishes

The case establishes that comparison procedure is not outcome-neutral in every
source-grounding task. In at least one live case, a source-blind target
inventory plus target-blind source reconstruction and a separate comparison
produced materially different support verdicts from a context that held both
sides together.

It also supplies a second integrated witness for the distinction between
[candidacy evidence and verdict evidence](../candidacy-evidence-licenses-escalation-not-acceptance.md).
Search and ingest correctly nominated Pirolli from thematic overlap. That
nomination justified the comparison; it could not decide which target claims
the source established.

The candidate workflow control is **bilateral isolation**: reconstruct target
claims without source vocabulary, reconstruct source claims without target
prose, then compare the frozen representations in a third role. The order of
the first two reconstructions need not matter if their contexts are genuinely
independent.

## Scope

This is one source, four target claims, one initial comparison, and one
decomposed rerun. The runs also differed in role decomposition, prompts, and
intermediate representation, so the observation does not identify isolation
as the cause of the improvement or estimate how often simultaneous reading
over-attributes support. It makes bilateral isolation a candidate control that
needs prospective comparison, not an established universal procedure.

The evidence is also asymmetric. The case shows charitable over-attribution;
it does not show whether separated reconstruction can instead become too
literal, miss a distributed source claim, or increase false narrowing.

## Provenance

Git commit `f7b22543` retains the correction, the three changed verdicts, and
the rationale for each. The source-grounding workshop that staged the run was
consumed after this bounded result and its open procedural choice were promoted;
git remains the change-history path for the full episode.

---

Relevant Notes:

- [Candidacy evidence licenses escalation to assessment, not acceptance](../candidacy-evidence-licenses-escalation-not-acceptance.md) — exemplifies: source resemblance nominated an assessment but failed when treated as support authority
- [Reasoning production is not reasoning evaluation](../reasoning-production-is-not-reasoning-evaluation.md) — exemplifies: the first pass accepted plausible routes to the target claims that the separated pass did not find in the source reconstruction
- [An experiment identifies only the contrast it actually runs](../an-experiment-identifies-only-the-contrast-it-actually-runs.md) — exemplifies: fresh roles, prompts, and intermediate representations changed together, so the rerun identifies only a bundle-level contrast
- [A borrowed pattern transfers only as far as source and target share a mechanism](../borrowed-patterns-transfer-only-over-shared-mechanism.md) — exemplifies: the C1-C3 verdicts retain shared source mechanisms while withholding stronger target-side additions

Operationalized into:

- [Assess a claim-bearing artifact against external literature](../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) — turns the bounded result into a conditional diagnostic with explicit triggers, frozen representations, and checks for both over-attribution and false narrowing
