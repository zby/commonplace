---
description: "Draft, not live. Use when a commonplace-review run revise report ends with a continuation record: finish in a session with the operator the work the pass left, from the text the pass published"
type: types/instruction.md
---

# Continue a revise pass

Goal: the work a revise pass left unfinished is done, dropped or handed to a new pass, each item by an actor who can settle it, and the operator knows what changed in the note.

Consumption: an agent in a session with the operator, reached from the `continuation` field of a `commonplace-review run revise` report. The rules below are the whole procedure, apart from the two instructions it names for recording decisions.

This procedure changes no rule about who decides an item. Proposals of a per-item operation, findings and exact candidate texts are decided by the operator, as [decide items](../../instructions/decide-items.md) and [approve a text](../../instructions/approve-a-text.md) state.

## Inputs

- The continuation record. `made-for` identifies the checkout text at handoff, not necessarily the text an item's evidence describes. Each item has `what`, `actor`, `after`, `how` and `evidence`.
- The run report: the plan with its `purpose` and `must-keep`, the state of each plan entry, and `publications`.
- The note.

## Before the items

1. Start with `made-for` as the expected checkout hash. If returning after a pause, ask for the [session handoff](#pause-between-sessions). Trace its authorized changes from `made-for`: each change must start at the preceding expected text. Use the last verified output hash as the expected hash. If the history is uncertain or the note's SHA-256 differs, go to [Stop continuing](#stop-continuing). Never adopt the checkout hash merely because it is current.
2. If the report has `published: true`, tell the operator what was published: the plan entries covered, the note's path and the publication's diff. The change is uncommitted, and git reverses it.
3. Tell the operator the remaining items in order: what each is, and who is expected to resolve it. Ask which to take up. An item the operator leaves stays in the record; do not work on it.

## The items

Work through the chosen items in the record's order. An item waits for the items its `after` names. Before each item, check the note against the expected hash. After an authorized publication, advance that hash to the publication's output hash and report its diff as in step 2. For an authorized direct edit, verify the diff contains only the agreed change and retain its before and after hashes. Neither kind of change updates `made-for` or makes old proposals fresh. If proposals concern a held candidate, wait for that exact text to be published before applying its answers.

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

If the operator leaves items for later, give them a handoff to bring to the next session: the original record path; items done, dropped and remaining; and the expected checkout hash. Cite the publications or authorized direct-edit diffs in order, with their before and after hashes. Point to recorded answers rather than copying decisions. The next agent verifies the handoff and asks which remaining items to take up; it does not repeat the run or treat the handoff as approval.

## Stop continuing

Stop and recommend a new pass when any of these holds:

- the note differs from the expected checkout text, or you cannot verify how the authorized changes led to it;
- two leftover entries in a row no longer fit the current text;
- the operator changed the note's purpose, scope or write brief during the session.

Say which items were done, which were dropped and why, and which remain. Leave published edits in place. Do not start a new pass unless the operator asks.

## Record the episode

Append to `kb/work/full-pass-continuation/episodes.md`: the run directory, each item with its expected actor and who settled it, each proposal the operator changed or rejected with the item's path, each entry dropped as no longer fitting, and any step that took long and that the workflow could have prepared. Record decisions and their reasons only in the answers files; do not copy them here.

## Verify

- Every item the operator took up is done, dropped with a stated reason, or handed to the operator.
- Each publication during the session was reported to the operator with its diff.
- No answers file was approved, and no item decided, without the operator's word for it.
- The episode is recorded.
