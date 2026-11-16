---
description: "A rewrite of an existing note runs as commonplace-review run rewrite: reconstruct from sources, account for claims, write and review a candidate, then stop for the operator's approval; new notes stay on the agent-run procedure"
type: reference/types/adr.md
status: accepted
---

# 136 — Note rewrites run as a workflow that ends at operator approval

**Status:** accepted; implemented at the operator's direction on 2026-11-16, with one live run.
**Date:** 2026-11-16
**Extends:** [ADR 135](./135-improvement-procedures-are-three-plans-on-one-runner.md), whose runner edits a note within bounds that preserve its claims, and [ADR 134](./134-stops-record-the-operators-answers-in-one-typed-file.md), whose publication stop the rewrite uses unchanged.
**Amends:** [ADR 129](./129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md) for rewrites of existing notes: their runs live under `kb/reports/state/review/runs/v2/rewrite/`, not under `kb/reports/state/multistage/`.

## Context

The improvement procedures edit a note without changing its claims. When a review finds a problem with a claim itself, the full procedure stops and leaves the change to the operator. On 2026-11-16 such a stop led to a rewrite done by hand in a conversation.

The procedure for that case existed as the multistage writing skill. A session agent ran three fresh workers and enforced by instruction who saw what: a reconstructor that must not see the existing note, an author, and a reviewer. The agent hashed the candidate, tracked the one allowed repair, and wrote the note when the reviewer accepted. The procedure kept no captured inputs, could not be repeated from its record, did not appear in the decision record, and published on a worker's acceptance. It did not use the note's write brief.

## Decision

**A rewrite of an existing note is a workflow.** `commonplace-review run rewrite NOTE --commission FILE` runs on the headless layer the review and revise workflows use. Its run directory is keyed by the note's path and start text, keeps every call's prompt, inputs and outputs, and continues when the command is repeated.

**The commission is a file the session agent writes with the operator.** It names the note and the authorized sources with their roles, and states the intended contribution, what to keep and exclude, the reserved decisions and the operator's current direction. The run captures it once; a changed commission needs `--restart`. When the note declares a write brief, every worker receives it as binding retained intent, and after publication the session agent writes or updates the brief from the commission's lasting parts.

**Four calls, each a fresh worker with only its listed inputs.** Reconstruct from the sources; account for the claims; write the candidate; review it. The first two workers are not given the note. One repair and a second review are allowed; a second blocking review ends the run with nothing published.

**The review step is a review operation.** Its criterion is the review instruction and its target is the candidate text, so it returns a typed review result bound to that text. `fail` blocks. `warn` findings reach the operator at the publication stop. When the operator publishes exactly the judged candidate, the result becomes the note's current result for that criterion, and its `warn` findings can be triaged like any review's. A revised candidate leaves the result unstored, because the published text is not the text judged.

**The candidate and review calls receive what the improvement procedures receive.** They get the operator's earlier decisions on the note and the role report's list of what other notes rely on. The first two calls get neither, because both describe the note's current text and claim selection must come from the sources alone. A fresh role report from a full `revise` run on the same text is reused; otherwise the rewrite runs it, at one more call.

**The operator approves the exact text.** An accepted candidate goes to the publication stop of `revise`: an answers file, acceptance with a revision, new validation warnings named, and a write only when the note still holds its start text. The reviewer's acceptance lets the run reach that stop and publishes nothing.

**Sources are captured or referenced.** A tracked text file is captured as an input. A file that is git-ignored or under a snapshot directory is passed by path and hash and never copied into the run.

**The candidate keeps the title.** The candidate checks of `revise` apply; the bounds of a single edit operation do not, because a rewrite may change claims. A retitle is a separate relocation on the operator's word.

**What stays on the agent-run procedure.** A new note, and an edit that poses a literature-disposition question ([ADR 081](./081-literature-disposition-is-explicit-and-claim-grained.md)). Grounding of sources stays with the session agent and happens before the run.

## Considered alternatives

**Keep the skill and add the write brief to it.** Not adopted, on the operator's choice to port now. It would have fixed the brief and left isolation, the record and approval as they were.

**One author across two steps, as in the skill.** Not adopted. Calls on the headless layer are fresh processes. The frozen claim account carries the first step's judgment to the second.

**Publish on the reviewer's acceptance.** Rejected. Every other procedure that writes a note requires the operator's approval of the exact text.

**Copy all sources into the run.** Rejected. Full copies of external sources must stay out of operational state that may be published.

**A typed result for each call.** Adopted for the review, whose findings triage and the fix operation consume. Not adopted for the reconstruction, the claim account and the candidate report, where code checks the headings and no other consumer reads them.

**Port the new-note path in the same change.** Deferred. It needs a run identity without a start text, collection and type resolution, a near-duplicate search and a create-only write.

## Consequences

The first live run, on the pre-rewrite text of the note rewritten by hand that morning, made four calls with no rejected output and reached the publication stop. Its candidate separated the same three questions as the hand rewrite. It marked each step as Popper's or as the note's own inference, which the hand rewrite had not done and a later review had to correct. The commission was written with hindsight, and this is one run, so the comparison shows that the workflow runs and little about how often its output is better.

Isolation is by supplied inputs and instruction. The first two workers can still read the checkout; nothing prevents a worker from opening the note.

A rewrite run costs four model calls at least, five when it must obtain the role report, and two more with a repair.

Known gaps: the one live run preceded the typed review, the role report and the earlier decisions, so none of these has run live. No run has exercised the repair, a referenced snapshot source, or a note with a write brief. A stale stored rewrite review cannot be rerun by `run gates`, though the project status counts it among stale results.
