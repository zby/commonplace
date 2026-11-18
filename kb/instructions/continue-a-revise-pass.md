---
description: "Use when a commonplace-review run revise report carries a continuation record: finish in a session with the operator the work the run left, each item by an actor who can settle it, from the text the run published"
type: types/instruction.md
---

# Continue a revise pass

Goal: the work a revise run left unfinished is done, dropped or handed to a new run, each item by an actor who can settle it, and the operator knows what changed in the note.

Consumption: an agent in a session with the operator, reached from the `continuation` field of a `commonplace-review run revise` report, or from its `continuation.json` in the run directory. The rules below are the whole procedure, apart from the two instructions it names for recording decisions.

This procedure changes no rule about who decides an item. Proposals of a per-item operation, findings and exact candidate texts are decided by the operator, as [decide items](./decide-items.md) and [approve a text](./approve-a-text.md) state. You present, record and run commands; you run a command that names an answers file or a run only on the operator's stated word for that exact file or run. Naming it to the command is the approval; no separate approval precedes it.

## Inputs

- The continuation record. `run-dir` is the run directory. `made-for` names the note's text when the run ended: its path `note`, its `sha256` and `text`, the file holding that text (the run's last publication, or `artifact/start.md`). Every item was computed on that text, and the record is never updated. Each item in `items` has `id`, `kind`, `what`, `actor` (`operator`, `session-agent`, or `worker` with its `effort`), `after` (the ids of items to settle first), `how` and `evidence` (the files it rests on). `how.step` names the section below that handles it; `how.command` is the command that proceeds, where one exists; `how.record` is the command that keeps an answers file nothing consumes; `how.revised` is the command for an operator's revision of a held candidate. An item that waits for answers files names them in `answers`.
- The run report, `report.json` in the run directory: the plan with its `purpose` and `must-keep`, the state of each plan entry, and `publications`.
- The note, and its run directories under `kb/reports/state/review/runs/v2/revise/<note path without .md>/`. Runs are named by their UTC start time, so they list in time order; older runs are named by a hash. Each run records its start text's hash in `start.json` and each text it published in `published.json`.
- After a pause, the entry of the earlier session in `kb/work/full-pass-continuation/episodes.md`.

## Before the items

1. Compare the note's SHA-256 with `made-for.sha256`. If they differ, account for the difference: read the note's later run directories for publications that lead from `made-for` to the current text, and after a pause read the earlier session's episode entry. Tell the operator what changed the note. If part of the difference has no record, say so and show `git diff` on the note. A difference does not end the procedure: each item below is checked against the current text.
2. If the report lists `publications`, tell the operator what was published: the plan entries each covers, the note's path and the path of each publication's `diff`. The change is uncommitted, and git reverses it.
3. Tell the operator the remaining items in order: what each is, and who is expected to resolve it. Ask which to take up. An item the operator leaves stays in the record; do not work on it.

## The items

Work through the chosen items in the record's order. An item waits for the items its `after` names. After each command that publishes, report the publication and its diff as in step 2. A command you run may end with a continuation record of its own; take up its items the same way before the items that waited on this one. When you change the note by hand on the operator's word, check that the diff holds only the agreed change. No change to the note makes old proposals fresh: the command that applies answers refuses when the note is not the text the proposals were made for.

**Proposals awaiting decision.** Follow [decide items](./decide-items.md) steps 1 to 3 on the answers file in `answers`. Then, on the operator's word for that file, run `how.command`: a new run applies the approved items and publishes. When the operator approved no item, nothing is applied: run `how.record` instead, so that later runs receive the rejections and deferrals. If the command reports that the note no longer holds the text of the proposals, or that the write brief changed, the proposals are stale: say so, record the file with `how.record`, and run the pass again only on the operator's word.

**Findings awaiting decision.** A triage left one answers file per review result, listed in `answers`. Follow [decide items](./decide-items.md) steps 1 to 3 on each file. Then, on the operator's word for those files, run `how.command`, which names every file: a new run fixes the approved findings, one fix per result with an approved finding. When no file approves a finding, nothing is fixed: keep each file with `commonplace-review answers record FILE`. If the command reports that a result no longer matches the note, its findings are stale: tell the operator, keep that file with `answers record`, and run the command again without it on the operator's word.

**A plan entry not run, for an operation that applies directly.** Read the entry's reason in `artifact/assessment.md` and the passages it concerns in the current note. Run `how.command` only when the reason still describes the current text; it carries the plan's purpose and must-keep claims. When the reason no longer holds, tell the operator and drop the entry.

**A plan entry not run, for a per-item operation.** Run it as above. When `how.command` names an answers file with `--answers`, the operator already decided its items; confirm with the operator before running it. Otherwise the new run ends with proposals: treat them as proposals awaiting decision.

**A plan entry that fixes a finding.** The finding was made on an earlier text. Open the review result in `evidence` and find each passage its `quotes` name in the current note. Use the quotes to locate the passages, then reread them in context against the finding's reason. Run `how.command` only if every quoted passage survives unchanged and the reason still holds. If an edit elsewhere resolved the issue, drop the finding and explain why. If the passage moved beyond recognition or the judgment is uncertain, leave it for the next review and say so. A finding without quotes concerns the whole document: bring it to the operator.

**An operation skipped as interactive.** `narrow-overclaims` needs the evidence for each claim, which only the conversation has. Ask the operator for it, then run `commonplace-review run revise NOTE --pass narrow-overclaims` with each piece of evidence as `--must-keep`, and the plan's `--purpose`. `split-out-a-treatment` writes a second note: do it with the operator under the instructions for writing a note, not through this command.

**Claim questions from the assessment.** Tell the operator each one with its passage and report, and your recommendation against the note's purpose and write brief. Change the note for one only on the operator's word.

**A candidate held back for a validation warning.** Follow [approve a text](./approve-a-text.md#a-held-candidate). `how.command` publishes the exact candidate; `how.revised` publishes the operator's revision of it.

**A plan that stopped on a proposal.** Follow [decide items](./decide-items.md#a-plan-that-stopped-on-a-proposal) on the file in `answers`, and keep it with `how.record`. `how.command` is the form of a run with a replacement plan; write that plan only on the operator's word.

**A worker or review failure.** Read the failure in the report. If you can repair its cause, repair it and tell the operator; otherwise tell the operator what failed and where its output is. The failed entry and the entries after it are their own items, after this one. Start a new run only on the operator's word.

**Stale reviews.** Every publication makes the note's stored review results stale. Tell the operator once, at the end, how many review operations a new review would launch; `how.command` lists the stale results. Run a review only on the operator's word.

## When the named actor cannot settle an item

The `actor` of an item is an estimate, not a permission. When a worker's run ends with a problem, or you cannot judge whether an entry still fits, bring the item to the operator with what you found. Do not retry the same command more than once, and do not decide an item whose inputs you could not check.

## Pause between sessions

If the operator leaves items for later, [record the episode](#record-the-episode) now. Its entry is what the next session starts from, so it must list the items done, dropped and remaining, and each change made to the note by hand, with what was agreed. The next agent reads that entry, follows [Before the items](#before-the-items) and asks which remaining items to take up. It does not repeat the run, and the entry approves nothing.

## Stop continuing

Stop and recommend a new run when any of these holds:

- the note changed in a way no record explains, and the operator does not want to continue on the current text;
- two leftover entries in a row no longer fit the current text;
- the operator changed the note's purpose, scope or write brief during the session.

Say which items were done, which were dropped and why, and which remain. Leave published edits in place. Do not start a new run unless the operator asks.

## Record the episode

The episode record is a trial: it ends when the workshop `kb/work/full-pass-continuation/` closes. Until then, append to `kb/work/full-pass-continuation/episodes.md`: the run directory and the path of its continuation record, each item with its expected actor and who settled it or that it remains, each change made to the note by hand, each proposal the operator changed or rejected with the item's path, each entry dropped as no longer fitting, and any step that took long and that the workflow could have prepared. Record decisions and their reasons only in the answers files; do not copy them here.

## Verify

- Every item the operator took up is done, dropped with a stated reason, or handed to the operator.
- Each publication during the session was reported to the operator with its diff.
- No answers file was named to a command, and no item decided, without the operator's word for it.
- The episode is recorded.
