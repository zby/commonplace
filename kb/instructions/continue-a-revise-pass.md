---
description: "Use when a commonplace-review run revise report carries a continuation record: help the operator resolve what the run left open, in a session, from the text the run published"
type: types/instruction.md
---

# Continue a revise pass

Goal: resolve issues that a revise run left open. An issue you take up is finished, not left half done. At the end the operator knows what changed in the note and what remains.

Consumption: an agent in a session with the operator, reached from the `continuation` field of a `commonplace-review run revise` report, or from `continuation.json` in the run directory.

## Your task

The operator wants the note improved and has limited attention. The run did what needed no decision and left the rest. Help the operator resolve it: understand each open issue well enough to explain it and recommend, bring the operator the decisions that are theirs, and do the rest yourself.

How you run the session is yours to judge: the order, what to group, how much to show, what to prepare before asking, and when a question is better asked than explained. The record's order and its `actor` values are the run's estimates, not instructions. Reaching the goal matters more than following the record: when an item no longer fits the note, or two items are one decision, say so and treat them that way.

The sections below give what you cannot work out yourself: what counts as resolved, the limits, what the record holds, and what each kind of item needs.

## What resolved means

The session need not take up every issue. The operator chooses how much to do, and the rest stays in the record. But an issue you take up is resolved only when nobody has to come back to it to finish it. A decision alone does not resolve an issue. Its consequences must also be in place. An issue you took up ends in one of three states.

**Settled.** All of these hold:

- the decision is made by the one who can make it;
- its effect is in the note: the approved items were applied by their run, or the agreed sentence was written, and the diff holds that change and nothing else;
- the note still validates, and the operator saw the diff;
- the decision is recorded where a later run reads it, when such a place exists: an answers file for a proposal, a finding or a stop. Claim questions and held candidates have none;
- what the change set in motion is itself settled or named: the continuation record of a run you started, another passage of the note that the change made wrong, and a note or document elsewhere that relied on what changed.

**Dropped.** The issue no longer applies, or the operator declined it. The reason is stated to the operator, and recorded in the issue's answers file when it has one.

**Left.** The operator chose to leave it, or it is larger than this session, such as a rewrite or a change to other notes. It is left properly only when a later session can find it without this conversation: the episode entry names the issue, why it was left, what the next step is and what it waits on.

An issue is half done when the operator decided and nothing was applied; when a change was applied and its diff was never checked or shown; when a decision was only said in the session; when a run you started ended with open items that nobody took up; or when an issue was left without a record. Before the session ends, check each issue you took up against these states. Tell the operator which state each is in, and which issues were not taken up.

Changes to the note stay uncommitted unless the operator asks for a commit. Say so at the end, with the list of changed files.

## Limits

- **The operator decides** proposals of a per-item operation, review findings, exact candidate texts, claim questions and whether to rewrite. [Decide items](./decide-items.md) and [approve a text](./approve-a-text.md) state how each is presented and recorded. Give your own recommendation; do not decide.
- **Naming a file or run to a command is the approval.** Run a command that names an answers file or a run only on the operator's stated word for that exact file or run. Nothing else approves it.
- **Change the note by hand only on the operator's word**, and check that the diff holds only what was agreed.
- **Start a new run only on the operator's word.** Do not retry a failed command more than once.
- **Do not settle an item whose inputs you could not check.** Bring it to the operator with what you found.
- **Decisions and their reasons live in answers files**, kept by the command that consumes them or by `commonplace-review answers record FILE`. A decision that is only said in the session does not reach later runs.
- **Tell the operator about every publication**: which plan entries it covers and where its diff is. A publication is uncommitted, and git reverses it.

## What you have

- **The continuation record.** `made-for` names the note's text when the run ended: its `sha256` and the file holding it. Every item was computed on that text, and the record is never updated. Each item has `id`, `kind`, `what`, `actor` (`operator`, `session-agent`, or `worker` with its `effort`), `after` (items the run expected to come first), `how` and `evidence`. In `how`, `step` names the kind below; `command` proceeds, where a command exists; `record` keeps an answers file nothing consumes; `revised` publishes the operator's revision of a held candidate. `answers` lists the answers files an item waits on.
- **The run report**, `report.json` in the run directory: its `outcome` (`completed`, `needs-continuation` or `failed`), the plan with its `purpose` and `must-keep`, the state of each entry, and `publications`. A run with the outcome `needs-continuation` may have finished its plan and published. `ok: false` with no failure means only that some file outside the run changed while it was open, which another session can cause.
- **The assessment**, `artifact/assessment.md`: why each plan entry was chosen, the claim questions, and the findings not acted on.
- **The note's runs**, under `kb/reports/state/review/runs/v2/revise/<note path without .md>/`, in time order by name; older runs are named by a hash. Each records its start text's hash in `start.json` and its publications in `published.json`.
- **After a pause**, the earlier session's entry in the episode record.

The note may no longer hold the `made-for` text: an earlier step of this session, another run or a hand edit changed it. Account for the difference from the note's run records and `git diff`, and tell the operator what you cannot account for. A changed note does not end the work. The commands guard their own inputs: one that applies answers refuses when the note is not the text the proposals were made for, and no later change makes old proposals fresh.

A command you run may end with a continuation record of its own. Its items are part of the same work.

## What settles each kind of item

**Proposals awaiting decision.** The operator decides each item of the answers file. `how.command` starts a new run that applies the approved items and publishes. When nothing is approved, `how.record` keeps the rejections and deferrals for later runs. When the command reports that the note or the write brief changed, the proposals are stale: keep the file with `how.record`; running the pass again is the operator's call.

**Findings awaiting decision.** A triage left one answers file per review result. The operator decides each finding. `how.command` names every file and starts a run with one fix per result that has an approved finding. Keep a file with no approved finding, or one whose result no longer matches the note, with `commonplace-review answers record FILE`.

**A plan entry not run, for an operation that applies directly.** `how.command` runs a one-entry plan the run wrote under `artifact/continue/`, which keeps the entry's scope and the plan's purpose and must-keep claims. The entry was chosen for an earlier text. It is worth running only while its reason in the assessment still describes the note; otherwise drop it and tell the operator why.

**A plan entry not run, for a per-item operation.** As above. When `how.command` names an answers file with `--answers`, the operator already decided its items; confirm before running. Otherwise the new run ends with proposals for the operator.

**A plan entry that fixes a finding.** The finding was made on an earlier text. `evidence` holds the run's copy of the review result, which a later sweep does not replace. The fix is worth running only when the passages its `quotes` name survive in the note and its reason still holds on rereading them in context. An issue an earlier edit resolved is dropped with that explanation. An uncertain one is left for the next review. A finding without quotes concerns the whole document and goes to the operator.

**An operation skipped as interactive.** `narrow-overclaims` needs the evidence for each claim, which only the operator has: with it, `commonplace-review run revise NOTE --pass narrow-overclaims` takes each piece as `--must-keep`, with the plan's `--purpose`. `split-out-a-treatment` writes a second note, which is done with the operator under the instructions for writing a note.

**Claim questions from the assessment.** Each is a small defect the passes cannot correct or a choice the assessor did not rank first. The operator answers each, and may decline. Check a claimed defect against the note yourself before recommending. No file records these answers. An accepted one is settled by the change to the note. A declined one is dropped by telling the operator; a later assessor may raise it again. When the operator wants a declined question not to return, the place for it is the note's write brief, which every assessor reads; write it there only on the operator's word.

**A candidate held back for a validation warning.** [Approve a text](./approve-a-text.md#a-held-candidate) applies. `how.command` publishes the exact candidate; `how.revised` publishes the operator's revision of it.

**A plan that stopped on a proposal.** The run edited nothing because the assessor found something it judged no edit pass could correct. A stop is advice, and it puts one question to the operator: follow the route the stop proposes, go on editing with a replacement plan, or leave the note. [Decide items](./decide-items.md#a-plan-that-stopped-on-a-proposal) applies. Record the answer once and keep it with `how.record`: it reaches the assessor of the next run on the note, which otherwise may stop on the same proposal. The work that follows, such as a rewrite, is a separate task: start it on the operator's word, or leave it with a record of the next step.

**A worker or review failure.** The report states the failure. Repair its cause when you can, and tell the operator; otherwise say what failed and where its output is. The failed entry and those after it are items of their own.

**Stale reviews.** A publication makes stale the stored review results whose criterion watches the changed parts. `what` counts them and `how.command` lists them. The operator decides whether to review again.

## When to recommend a new run

Continuing stops being the cheaper path when the record no longer describes the note. Recommend a new run when the note changed in a way no record explains and the operator does not want to continue on it, when leftover entries keep failing to fit the current text, or when the operator changed the note's purpose, scope or write brief during the session. Say what was done, what was dropped and why, and what remains. Published edits stay in place.

## Pause between sessions

When the operator leaves items for later, record the episode before the session ends. The next session starts from that entry, so it lists the items done, dropped and remaining, and each change made to the note by hand with what was agreed. The next agent does not repeat the run, and the entry approves nothing.

## Record the episode

The episode record is a trial: it ends when the workshop `kb/work/full-pass-continuation/` closes. Until then, append to `kb/work/full-pass-continuation/episodes.md`: the run directory and its continuation record, each item with its expected actor and who settled it or that it remains, each change made to the note by hand, each proposal the operator changed or rejected with the item's path, each entry dropped as no longer fitting, and anything that took long and that the workflow could have prepared. Decisions and their reasons stay in the answers files; do not copy them.

## Verify

- Every issue taken up is settled, dropped or left as [what resolved means](#what-resolved-means) defines those states, and the operator was told which. The operator was told which issues were not taken up.
- No issue is half done: no decision without its effect, no applied change without a checked diff, no run of yours with open items nobody took up.
- The operator was told of each publication during the session, with its diff.
- No answers file or run was named to a command, and no operator's item decided, without the operator's word for it.
- The episode is recorded.
