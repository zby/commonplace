---
description: "commonplace-review run revise writes its candidate to the note without a publication stop; the stop remains for rewrites and for a candidate with a new validation warning; each automatic publication is recorded and nothing is committed"
type: reference/types/adr.md
status: accepted
---

# 137 — Revise publishes without a publication stop

**Status:** accepted; decided by the operator on 2026-11-16 and implemented on 2026-11-17. Not yet run live.
**Date:** 2026-11-17
**Amends:** [ADR 134](./134-stops-record-the-operators-answers-in-one-typed-file.md) and [ADR 135](./135-improvement-procedures-are-three-plans-on-one-runner.md), under which the operator approved the exact text of every change by `revise`. That approval now applies only in the cases named below.

## Context

Every `revise` run that changed a note ended at a publication stop, where the operator approved the exact final text. A run with nothing to ask the operator still waited. A run with a per-item stop asked twice: once for each proposal, and again for the whole text that applying the approved proposals produced.

The operator's goal is automatic improvement, with stops becoming rarer. A stop is warranted where a decision is needed that nobody has made. The publication stop of `revise` asked for a decision on changes of two kinds: changes an operation is defined to apply without a decision, and changes whose items the operator had already decided.

## Decision

**A `revise` run writes its candidate to the note without a publication stop.** It writes at the end of its plan, and before each per-item stop. A plan of only directly applying operations runs to the end with no stop. Approved items are published when applied, with no second approval.

**A publication stop remains in two cases.** Every [rewrite](./136-note-rewrites-run-as-a-workflow-that-ends-at-operator-approval.md) run stops, because a rewrite may change claims and nobody has decided its content. A `revise` candidate stops when it has a validation warning that the text the run last knew did not have. Acceptance with a revision stays available at that stop.

**The other stops are unchanged.** The operator still decides each per-item proposal and each finding in triage. The plan's own `stop` and the depth 1 stop of the full procedure still end the run.

**The automatic checks are unchanged.** A candidate that changes the title, type, brief declaration or H1, drops a link target without naming it, or alters a quoted span is rejected as a worker's output. The note is written only when it still holds the text the run last knew. A changed brief stops the run.

**A run continues after it publishes.** The run keeps a record of each text it wrote. A repeat of the command finds the open run whose last publication is the note's current text. An edit by anyone else after a publication stops the run, and it writes nothing.

**Each publication is recorded and none is committed.** The run keeps the published text, its hash, the diff from the text before, the plan entries it covers and the time. `commonplace-review decisions` lists it as decided by `automatic`, never by the operator. Publication writes the working tree only. After a run publishes, the session agent tells the operator what was published and where the diff is; the operator reverses a change with git.

## Considered alternatives

**Keep the publication stop.** Rejected by the operator. It asks for a decision that either the operation's definition or the operator's item answers have already made.

**Remove the stop from rewrites too.** Not adopted. No decision by the operator precedes a rewrite's content.

**Commit each publication.** Not adopted. An uncommitted change is visible in `git diff` before it enters history, which is the review that replaces the stop.

**Publish a candidate with a new warning and report the warning.** Not adopted. A new warning is the one cheap signal that a candidate made the note worse by a declared rule.

## Consequences

The operator no longer sees every changed text before it is written. What protects the note is the bounds of each edit operation, the candidate checks, the brief, and the operator's reading of the uncommitted diff.

The earlier closure policy against moving authority toward automation is overridden for this case by the operator's decision. The evidence that would test the decision is in the run records: published diffs the operator reverses or corrects.

A candidate with a new warning at a per-item stop is not published there; it stays in the run until the end, because a run cannot wait at two stops.

A note reverted with git to a text a finished run started from gets a new run directory with a numeric suffix.

The next step in the same direction is to move a per-item operation to applying directly, one operation at a time, on evidence from the decision record. That is a separate decision for each operation ([edit operation](../../types/edit-operation.md): `decision` records what an operation does and grants no authority).
