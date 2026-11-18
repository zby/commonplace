---
description: "Register the answers type, which the validator checks against its hashed question; two stop instructions, decide items and approve a text; per-item edits and publication read answers"
type: reference/types/adr.md
status: accepted
---

# 134 — Stops record the operator's answers in one typed file

**Status:** accepted; implemented under the operator's commission for the stop group.
**Date:** 2026-11-15
**Extends:** [ADR 133](./133-edit-operations-run-alone-through-one-typed-route.md), from edit operations to the points where the operator decides. Its edit route, bounds and observations apply unchanged.

## Context

The operator wants every improvement operation to be an atom: a typed instruction file, file inputs, a typed stored result, runnable and testable alone. Review operations and edit operations are atoms. Stops, the points where a procedure waits for the operator, were not. There were four, each with its own record. A strike list kept the operator's strikes in a list format that only revise code parsed. The full pass kept a hand-back disposition in packet fields. The fix procedure let an agent mark an item `deferred` with no operator involved. Publication approval was an unedited JSON manifest.

A stop differs from the other atoms in one way that matters for testing. The operator is the one who answers, so repeated model trials cannot test it. What can be tested is whether a recorded answer is well formed and answers the question that was asked.

## Decision

**One typed result, `answers`.** An [answers](../../types/answers.md) file holds one item per decision: the item's `id`, the question's `proposal` copied unaltered, `state` (`pending`, `approved`, `rejected` or `deferred`), `reason`, `revisit`, `decided-by` and `decided-at`. It names its question by repository path and SHA-256. A question is either an edit result with outcome `proposed`, whose items are its proposals, or any other file, a text to approve, whose one item names the file's hash. An approval of a text is therefore an answers file with one item. `commonplace-review answers create --from QUESTION` writes the pending file, so nobody writes a hash by hand. Cross-run fields of the workshop draft (`applied-in`, `repeats`, `supersedes`, `expired`) are left out because no consumer reads them.

**Deterministic acceptance in the validator.** `commonplace-validate` checks every answers file: the question hash matches the file now; every item of the question appears once with its proposal unaltered, and no other item appears; `rejected` and `deferred` carry a reason; `deferred` carries a revisit condition; every decided item has `decided-by: operator` and `decided-at`; a pending item has neither. The schema states the per-item rules; a type rule compares the file with its question. Consumers read answers only through the validator and add their own checks.

**Two stops, as instructions for a session agent.** [Decide items](../../instructions/decide-items.md) presents each item of a list, asks the operator, and records the answer; it is the strike-list procedure in general form. [Approve a text](../../instructions/approve-a-text.md) shows the operator one exact candidate and records the decision. Neither decides anything itself. `deferred` is a state the operator gives an item, not a stop; an agent may not set it alone, and the fix procedure (retired by ADR 135) now records an item it cannot decide as `pending`. Both are plain `types/instruction.md`: the validator checks the answers file, not the instruction, so an instruction type would check nothing.

**The per-item edit reads answers.** The second run of a `per-item` operation takes an answers file as its `answers` input. Code accepts it only when the validator does and its question is an edit result of the same operation on the same input text. The worker applies the `approved` items; code refuses a candidate that changed the passage of any other item. `pending`, `rejected` and `deferred` items are not applied. The strike-list format is removed.

**Publication stays in code and reads answers.** Writing an approved candidate to the checkout is neither an edit operation nor a stop. The revise and full-pass workflows stop on `artifact/publication-answers.md`, an answers file whose question is the candidate `artifact/final.md`. Code writes the note only when the approved answers pass the validator, the item is `approved`, and the note still holds the start text. The proposal key still binds the start text, the candidate and the decision context, so a change in any of them withdraws the approval. The revise workflow's per-item stop writes `artifact/<pass>-answers-<key>.md` over the proposing run's edit result. Both still go through the existing operator record and `commonplace-review approve`.

**The decision record reads answers.** `commonplace-review decisions` lists one entry per item of an approved answers file, with its state, decider and reason; the publication approval stays one bundle entry.

## Amendments (2026-11-16)

Made after the first operator sessions through the stops, at the operator's direction.

**A decided item can record what followed.** Two optional fields on a decided item: `resolution` states what was done when it went beyond the proposal, and `refs` lists commit hashes, paths or a workshop directory. They are added after the decision and the file is approved again, because the decision record reads the approved capture. The case that prompted them: a reviewer's local contradiction led to a rewrite and two renames of the note, and the stop's record could not name them.

**A stopped plan leaves an answers file.** When a plan sets `stop`, the run writes `artifact/stop-answers.md` with one item over the plan. The run does not wait for it. It exists so the operator's decision on the proposal, and what followed, has a record.

**Decisions carry over to later runs on the same note.** A run collects the decided items of earlier runs on the note. Per-item operations and the fix operation receive them as the `earlier-decisions` input. A new proposal with the same `quote` and `change` as a decided item starts with that decision and `carried-from` naming the earlier answers file; the stop still waits for the operator's approval. Only an identical proposal is carried. The case that prompted it: an instruction change invalidated two runs after the operator had decided their items, and the decisions had to be applied by hand.

**A pending stop whose note has changed is reported as overtaken.** The decision record computes this when it lists; no item changes state.

Not changed: an approval stays bound to the exact candidate and the inputs that produced it. A candidate invalidated before publication is lost and asked again.

## Amendments (2026-11-18)

Made at the operator's direction, after the first continuations under [ADR 138](./138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md).

**A plan stop's answer is recorded once.** Since ADR 138 a stop ends the run, so no command waits for the answer to a stopped plan, and approving it starts nothing. The stop is advice with one question for the operator: follow its proposal, or go on editing. The answer is recorded once, when the operator decides, and kept with `answers record`. Its remaining use is that the next run's assessor reads it and does not stop again on a proposal the operator declined. The procedure no longer adds `resolution` and `refs` to a stop's item after the work and records the file again: the operator judged the commit history and the later runs on the note sufficient. The two fields stay in the answers type as optional. The continuation record's `plan-stop` item names the recording command and no other; the route is in the stop's text, and a replacement plan runs with `--plan`.

## Considered alternatives

**Four typed stops.** Rejected with the operator. A strike list and a hand-back disposition are the same act over different item kinds, and `deferred` is a state, not a point where a procedure waits.

**Keep the strike-list format beside the answers type.** Rejected. Two formats would need two parsers and two acceptance paths for one decision.

**A separate check command for answers.** Not adopted. `commonplace-validate` already runs schema and type rules for any typed file, so the acceptance lives where every other type's does.

**A stop instruction type.** Not adopted. Nothing in a stop instruction is mechanically checkable beyond the instruction type; the checkable part is the answers file.

**Move the full pass's hand-back disposition onto answers now.** Deferred. The packet records one resolution for the whole hand-back, with states (`accepted`, `alternative-applied`, `superseded`), a `version-guard` decider and filesystem postconditions (`resulting-paths`) that the answers states do not express, and `full_pass.blocking()` reads the packet's `resolution` field. Moving it needs a redesign of the packet, which this change does not make.

**Drop `commonplace-review approve` and read the answers file directly.** Not adopted. The operator record binds an answer to the proposal key, which is how a changed context withdraws an approval; replacing it would redesign the run record.

## Consequences

The operative consumers are the validator (schema and type rule for `types/answers.md`), the edit route (`run edit --input answers=PATH`), the revise workflow's per-item stop, both workflows' publication, `commonplace-review answers create`, `commonplace-review decisions`, and session agents that load the two stop instructions. Python enforces acceptance, the item filter and publication; the instructions bind how the agent presents and records.

An operator now records answers in YAML items instead of `struck:` lines, and a publication approval is an answers file instead of an unedited manifest. A decided item needs `decided-by` and `decided-at`, which costs typing in a session. Every pending item stays visible in the decision record.

Limits: no stop has run live with an operator. The presentation is tested only by a live session per stop, by reading whether the recorded answers say what the operator said. The validator cannot tell whether the operator actually gave an answer marked `decided-by: operator`; that rests on the instruction and on the approval command run on the operator's word. Code does not detect a change outside the answered items. The full pass's hand-back disposition and the fix report's statuses stay outside the answers type.
