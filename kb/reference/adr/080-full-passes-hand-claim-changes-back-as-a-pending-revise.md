---
description: "The full improvement pass applies only edits that keep a note's claim; a finding that requires changing the claim becomes a pending revise disposition handed to the author, and the packet records its execution phase and final capture"
type: ../types/adr.md
tags: []
status: accepted
---

# 080-Full passes hand claim changes back as a pending revise

**Status:** accepted
**Date:** 2026-08-26

## Context

The full improvement pass reconciles six method families into a packet and then repairs the note. Its repair vocabulary was subtractive — narrow, qualify, delete, reframe to a weaker claim — because the pass derives what a note is for from the note's own text and the reports, and cannot extend the note's evidence. Six recorded episodes show the consequence: when a critique or premise defeat lands, the cheapest defensible repair is the claim no gate can touch, and the closing cycle scores that retreat against the reframed update, so drift reads as improvement. Two same-day guards (no reframe on doubt; no reframe on a defeat that misreads the note's own term) each caught one case and missed the next, and the second contained an immunizing loophole. A coherence audit of the instruction found the reframe machinery internally inconsistent: reframes were declared bidirectional but only a weakening could satisfy the packet rules; the mandatory post-reframe rename could not pass the guard the instruction required before it; routed-attention findings were both "never a verdict" and decision authority for an applied edit; the required final hash had no field; and an interrupted keep pass was invisible to preflight.

The forces recur under any repair the pass applies on its own: the pass reads the text, not the author's theory of it; in-pass repair optimizes defensibility; and every added guard is a rule the next counterexample can equivocate on.

An instrumented run immediately exposed a second boundary at closing. Pass `20260826T214434Z-8272bf` reached schema-valid `phase: complete` while its final capture contained the sentence “Search results and thematic fit Peter Pirolli's account of proximal information scent as prior art for an agent-navigation note.” Closing sentence review correctly failed it because the edit had dropped the finite verb `nominated`; closing also found two misleading link texts and a title/body mismatch. The procedure recorded those findings as Open items but still declared completion. Structural validity and a matching capture had therefore certified retention of a defect the pass itself introduced. The retained [closing-completion failure evidence](../../work/full-pass-instruction-coherence-audit/closing-completion-failure-evidence.md) fixes the exact evidence boundary.

## Decision

1. **Five dispositions, four of them hand-backs.** `keep` is the only disposition the pass executes. `revise`, `delete`, `merge`, and `rehome` are pending hand-backs resolved by a person under `resolve-full-pass-disposition.md`. A finding that requires changing the note's title-level claim — a defeated load-bearing premise, a grounding failure on the passage carrying the claim, an unanswerable objection, or a warranted update that differs from the title in strength, direction, scope, modality, or category in either direction — is `revise`. The pass never changes a title, thesis, or title-as-claim.
2. **The revise packet carries the brief, not the repair.** It records the objection with the evidence that decides it, candidate replacement claims each with the mode it would assert and that mode's guard under the notes contract, and the citer scope. None is applied; the author may adopt, alter, or reject them.
3. **Routed attention routes.** Friction and premise-decomposition output is carried verbatim and used only in the decision table's objection question, which can select a hand-back and nothing else. Whether a counterexample meets the note's antecedent as the note means it is the author's call; the packet quotes both so the author can make it.
4. **One decision table, one packet contract, one state machine.** Contribution → fit → objection → disposition, answered in order and recorded once. The packet gains `phase` (`packet`, `editing`, `closing`, `complete`) distinct from `resolution`, and a `final_capture`/`final_sha256` pair written after the copyedit. The guard compares each guarded path with its latest capture, so post-pass operations on a completed keep pass have a guard that can pass, and preflight can detect an orphan directory or an unfinished keep pass. The edited note is validated after the copyedit and the packet after the closing cycle.
5. **The copyedit is a handoff.** The fresh worker writes a candidate file; the orchestrator applies the acceptable diff. The orchestrator never copyedits directly.
6. **Closing is a bounded retention gate.** A packet becomes `complete` only with `closing_status: ready`: its selected update survives and no pass-introduced defect remains. A local defect that does not change the title, thesis, selected update, or evidence permits one correction followed by a new immutable final capture and a complete closing rerun. A claim-level closing failure, a newly introduced angle, or any defect that survives that one recovery becomes `closing_status: hand-back`; the pass restores the pass-start text and stops. Claim-level hand-back takes precedence over local cleanup. `closing_repair_attempted` makes the one-recovery bound schema-visible.

This amends ADR 051 (the disposition set and the packet's fields) and ADR 066 (decision 4: the full pass no longer converts claim modality in-pass; a mode mismatch is a `revise` whose brief names the target mode and its guard, and conversions outside a pass remain permitted under the same guards).

## Considered alternatives

- **Keep in-pass reframes and authorize the synthesis agent explicitly**, dropping the "unresolved" claim about routed attention. Coherent, but it keeps every mechanism the episodes show failing and leaves the bidirectional-reframe, post-reframe-guard, and log-handoff defects to be repaired one by one.
- **Keep reframes as a pending disposition the human confirms before step 8 applies them.** Preserves the ADR 066 conversions, but requires the pass to re-enter after resolution — the interruption machinery in a harder form — and still has the pass author the replacement claim.
- **Add guards to in-pass reframing** (the two adopted earlier the same day). Each caught its case and missed the next; the audit found the second guard immunizing. Guards on the repair cannot supply what the repair lacks, which is the author's theory of the note.

The deciding force was the operator's preference for simplification over further guarding, together with the six-episode record that the pass is reliable as critique and not as claim-level repair. Left open: whether a `revise` hand-back proves too frequent in practice (every landing critique is now a candidate), which the pending-packet count will show.

## Consequences

Easier: a claim-level defect stops the pass with the objection and candidates in hand; a false defeat costs one human read instead of a rewritten note; the packet's phase and final capture make interruption and post-pass follow-up inspectable; and a closing reviewer cannot leave an introduced defect behind a `complete` marker.

Harder: claim-level repairs now wait on a person; the pass produces more pending packets; ADR 066's in-pass mode conversions, validated over 23 passes, are no longer exercised by the pass and depend on authors applying the mode guards themselves. A bounded recovery repeats the whole closing suite because every closing result must assess one exact capture; this spends another review cycle rather than selectively retaining results from stale text.

Operativity: the instruction `run-full-improvement-pass-on-note.md` binds the orchestrator; `full-pass-report.schema.yaml` and `commonplace-validate` enforce the packet fields and phase/disposition combinations; `commonplace-guard-full-pass-report` enforces latest-capture guarding; `resolve-full-pass-disposition.md` binds whoever executes a hand-back.

Limits: decided for `kb/notes/` passes on this installation's review machinery. Not tested on passes over other collections, and not a claim that agent-applied claim repair is impossible — only that this pass, with the inputs it has, should not attempt it.

## Links

- [ADR 051 — Full-pass packets own guarded captures and resolutions](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) — amends: adds `revise`, `phase`, and the final capture to the packet contract
- [ADR 066 — Claims declare modality in text, and passes repair mode mismatch](./066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) — amends: decision 4; mode mismatch becomes a revise brief rather than an in-pass conversion
- [Run a full improvement pass](../../instructions/run-full-improvement-pass-on-note.md) — procedure: the decision table and state machine
- [Resolve a full-pass disposition](../../instructions/resolve-full-pass-disposition.md) — procedure: executes hand-backs
- [Full-pass report type](../../reports/types/full-pass-report.md) — implemented-by: packet fields
- [Narrowing bought to survive review is paid for in content](../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — rests-on: the drift mechanism this decision removes from the pass
