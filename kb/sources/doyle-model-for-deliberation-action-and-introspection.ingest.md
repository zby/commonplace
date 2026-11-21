---
description: "Doyle separates detecting a conflict from deciding what to give up. His dissertation specifies how policies could guide that choice and identifies where the implementation still chose randomly."
source: https://hdl.handle.net/1721.1/6883
captured: "2026-11-21"
capture: internet-archive-dtic-djvu-ocr
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: bce8433c7f49766dc57865aaa43db84e2877c9b46100bc8458a0716e529c5735
ingested: "2026-11-21"
occasion: "What starts reconsideration, and how does a reasoner choose among competing revisions?"
type: types/ingest-report.md
domains: [reason maintenance, belief revision, dialectical deliberation, skill modification]
tags: [judgment-governed-self-improvement]
learning_claims: true
---

# Ingest: A Model for Deliberation, Action, and Introspection

## Classification

Jon Doyle’s [1980 MIT doctoral dissertation](https://hdl.handle.net/1721.1/6883) presents a theoretical architecture, compares it with earlier reasoning programs, and reports which components he implemented. The worked decisions illustrate the design rather than evaluate it.

## Summary

Doyle treats drawing an inference as an action: a program can have reasons to draw it now, postpone it, or challenge it. The proposed program describes its beliefs, desires, intentions, plans, and reasons in a common language. A reason maintenance system tracks which beliefs still have support; an interpreter uses policies to decide what to do when support alone does not settle the question. A policy can introduce an option, offer a reason for it, or object to a particular argument without ruling out the option. The same machinery could deliberate about changing a skill rather than just using it. Doyle reports tests of parts of the interpreter, not a working system that performed all these operations together (§1.5).

## Contribution assessment (our opinion)

The strongest contribution is an answer to a problem that dependency tracking leaves open: several changes can restore consistency but imply different actions. Unlike a rule that always retracts a planned move when it encounters an obstacle, Doyle’s procedure can ask whether the move was merely planned or actually made, then consider reasons to doubt the plan, the observation, or a background assumption. That gives a precise comparison with the earlier repair procedures discussed in §6.2.1. Its significance is as a model of what a decision needs to represent, not a demonstrated advantage in choosing the right repair.

## Quotes

No source quotes have been retained yet.

## Connections Found

The dissertation supplies the revision choice left open in [Doyle’s earlier truth maintenance memo](./doyle-1979-truth-maintenance-system-aim-521.ingest.md): finding the assumptions behind a contradiction identifies alternatives, not which one to give up. The new proposal is to make that choice an explicit intention and let policies argue over it. This also distinguishes Doyle’s question from [de Kleer’s assumption-based TMS](./an-assumption-based-tms.ingest.md): recording the contexts in which each conclusion holds need not select one to act on now.

## Learning Claims (our opinion)

Doyle distinguishes patching a procedure that failed from retaining a critic that can recognize the same defect in another plan (§6.2.5). Against the [theory builder](../theory/definitions/theory-builder.md) criteria, localization is explicit: a plan, its justification, and an objection to that justification can each be named. Consumption has partial implementation support in the interpreter’s initial use of deliberation. Content-directed criticism is illustrated in §5.8: an objection defeats one reason to hold a door, while an independent reason still supports holding it. Iteration is specified within that decision, since the remaining reason shapes the next choice. This is not yet revision of the standing policy. The reusable critic would carry a result across problems, but the reconstruction of HACKER is a design, not a reported run showing Doyle’s program learned it or improved its later performance.

## Extractable Value

1. **Distinguish a reason to reopen a question from a reason to choose a repair.** Adding a justification starts routine support maintenance. A supported contradiction or unresolved choice of consistent updates can instead prompt an intention to decide. Reflection can also propose reconsideration when an action’s observed effects differ from its predicted effects; that discrepancy does not by itself discredit the prediction rather than the observation (§§3.10, 6.1.1). [quick-win]
2. **Compare partial repairs in context.** If a planned block move would cause a collision, retracting the proposed move preserves the report of the obstacle. After an actual move, simply deleting the plan does not explain what happened. Doyle’s policies express which beliefs to preserve in each situation. The reasoner adds or defeats a justification, propagates its consequences, and decides again if the partial repair exposes another choice (§6.2.1). A separate decision governs whether to consider another argument, commit now, or defer (§5.7). [quick-win]

## Limitations (our opinion)

Section 3.10 draws the decisive boundary: the existing maintenance system still chose among ambiguous revisions randomly. The dissertation offers neither a comparison showing that deliberation selects better repairs nor a general method for recognizing which surprising facts deserve investigation. Even a reasoned choice can protect a preferred belief rather than identify the source of error. As the [addressable theory definition](../theory/definitions/addressable-theory.md) cautions, locating a candidate for repair is not establishing fault.

## Recommended Next Action

Add Doyle’s planned-versus-executed move to the [addressable theory definition](../theory/definitions/addressable-theory.md) as a worked example of why the same conflict can warrant different revisions.
