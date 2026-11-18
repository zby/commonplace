---
description: "Draft, not live. Use when a commonplace-review run revise report ends with a continuation record: finish in a session with the operator the work the pass left, from the text the pass published"
type: types/instruction.md
---

# Continue a revise pass

Goal: the work a revise pass left unfinished is done, dropped or handed to a new pass, each item by an actor who can settle it, and the operator knows what changed in the note.

Consumption: an agent in a session with the operator, reached from the `continuation` field of a `commonplace-review run revise` report. The rules below are the whole procedure, apart from the two instructions it names for recording decisions.

This procedure changes no rule about who decides an item. Proposals of a per-item operation, findings and exact candidate texts are decided by the operator, as [decide items](../../instructions/decide-items.md) and [approve a text](../../instructions/approve-a-text.md) state.

## Inputs

- The continuation record. `made-for` names the note's text when the pass ended; every item was computed on it. Each item has `what`, `actor`, `after`, `how` and `evidence`.
- The run report: the plan with its `purpose` and `must-keep`, the state of each plan entry, and `publications`.
- The note, and its run directories, which are listed in time order under the note's path. Each run records the hash of its start text and each text it published.
- After a pause, the entry of the earlier session in `kb/work/full-pass-continuation/episodes.md`.

## Before the items

1. Compare the note's SHA-256 with `made-for`. If they differ, account for the difference: read the note's later run directories for publications that lead from `made-for` to the current text, and after a pause read the earlier session's episode entry. Tell the operator what changed the note. If part of the difference has no record, say so and show `git diff` on the note. A difference does not end the procedure: each item below is checked against the current text.
2. If the report has `published: true`, tell the operator what was published: the plan entries covered, the note's path and the publication's diff. The change is uncommitted, and git reverses it.
3. Tell the operator the remaining items in order: what each is, and who is expected to resolve it. Ask which to take up. An item the operator leaves stays in the record; do not work on it.

## The items

Work through the chosen items in the record's order. An item waits for the items its `after` names. After each command that publishes, report the publication and its diff as in step 2. When you change the note by hand on the operator's word, check that the diff holds only the agreed change. No change to the note makes old proposals fresh: the command that applies answers refuses when the note is not the text the proposals were made for.

**Proposals awaiting decision.** Follow [decide items](../../instructions/decide-items.md) steps 1 to 3 on the answers file the item names. Then, on the operator's word for that file, apply the approved items with the command in `how`; naming the file to that command is the approval, and no separate approval precedes it. When the operator approved no item, nothing is applied: record the file with the recording command in `how`, so that later runs receive the rejections and deferrals. If the command reports that the note no longer holds the text of the proposals, the proposals are stale: say so and run the operation again only on the operator's word.

**A plan entry not run, for an operation that applies directly.** Read the entry's reason in `artifact/assessment.md` and the passages it concerns in the current note. Run it only when the reason still describes the current text. Run `commonplace-review run revise NOTE --pass NAME`, with the plan's `--purpose` and each `--must-keep`. When the reason no longer holds, tell the operator and drop the entry.

**A plan entry not run, for a per-item operation.** Run it as above. It ends with proposals; treat them as proposals awaiting decision.

**A plan entry that fixes a finding.** The finding was made on an earlier text. Open the review result and find each passage its `quotes` name in the current note. Use the quotes to locate the passages, then reread them in context against the finding's reason. Run `commonplace-review run revise NOTE --finding RESULT` only if every quoted passage survives unchanged and the reason still holds. If an edit elsewhere resolved the issue, drop the finding and explain why. If the passage moved beyond recognition or the judgment is uncertain, leave it for the next review and say so. A finding without quotes concerns the whole document: bring it to the operator.

**An operation skipped as interactive.** `narrow-overclaims` needs the evidence for each claim, which only the conversation has. Ask the operator for it, then run the pass with each piece of evidence as `--must-keep`. `split-out-a-treatment` writes a second note: do it with the operator under the instructions for writing a note, not through this command.

**Claim questions from the assessment.** Tell the operator each one with its passage and report, and your recommendation against the note's purpose and write brief. Change the note for one only on the operator's word.

**A candidate held back for a validation warning.** Follow [approve a text](../../instructions/approve-a-text.md#at-a-publication-stop).

**A plan that stopped on a proposal.** Follow [decide items](../../instructions/decide-items.md#a-plan-that-stopped-on-a-proposal).

**A worker or review failure.** Read the failure in the report. If you can repair its cause, repair it and tell the operator; otherwise tell the operator what failed and where its output is. Start a new pass only on the operator's word.

**Stale reviews.** Every publication makes the note's stored review results stale. Tell the operator once, at the end, how many review operations a new review would launch. Run it only on the operator's word.

## When the named actor cannot settle an item

The `actor` of an item is an estimate. When a worker's run ends with a problem, or you cannot judge whether an entry still fits, bring the item to the operator with what you found. Do not retry the same command more than once, and do not decide an item whose inputs you could not check.

## Pause between sessions

If the operator leaves items for later, [record the episode](#record-the-episode) now. Its entry is what the next session starts from, so it must list the items done, dropped and remaining, and each change made to the note by hand, with what was agreed. The next agent reads that entry, follows [Before the items](#before-the-items) and asks which remaining items to take up. It does not repeat the run, and the entry approves nothing.

## Stop continuing

Stop and recommend a new pass when any of these holds:

- the note changed in a way no record explains, and the operator does not want to continue on the current text;
- two leftover entries in a row no longer fit the current text;
- the operator changed the note's purpose, scope or write brief during the session.

Say which items were done, which were dropped and why, and which remain. Leave published edits in place. Do not start a new pass unless the operator asks.

## Record the episode

Append to `kb/work/full-pass-continuation/episodes.md`: the run directory and the path of its continuation record, each item with its expected actor and who settled it or that it remains, each change made to the note by hand, each proposal the operator changed or rejected with the item's path, each entry dropped as no longer fitting, and any step that took long and that the workflow could have prepared. Record decisions and their reasons only in the answers files; do not copy them here.

## Verify

- Every item the operator took up is done, dropped with a stated reason, or handed to the operator.
- Each publication during the session was reported to the operator with its diff.
- No answers file was approved, and no item decided, without the operator's word for it.
- The episode is recorded.
