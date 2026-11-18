---
description: "Use when a run left a pending answers file over proposals or review findings, such as <pass>-answers.md, a triage's finding-answers-<key>.md or a per-item edit result: take and record the operator's decision on each item"
type: types/instruction.md
---

# Decide items

Goal: every item of the question carries the operator's own decision, with the operator's reason where one is required, so that only what the operator approved is applied and the reasons stay available for revising the procedure that proposed the items.

Consumption: an agent in a session with the operator. It is reached from a `proposals`, `findings` or `plan-stop` item of a continuation record through [continue a revise pass](./continue-a-revise-pass.md), from [revise an article or note](./simplification-passes/revise-an-article-or-note.md) step 3, from a triage (`commonplace-review run revise NOTE --triage`), after `commonplace-review run edit` returned `proposed`, or after `commonplace-review record` wrote answers files over an overtaken run's findings ([below](#findings-answered-by-a-structural-change)). Nothing here is inherited from the worker instruction; the rules below are the whole procedure. For the approval of one exact text, follow [approve a text](./approve-a-text.md) instead.

Inputs:

- the answers file (`type: types/answers.md`): its `question` names the question file, and each item holds an `id`, the question's `proposal` and `state: pending`, or, for a carried-over item, the earlier decision and `carried-from`;
- the question: an edit result with outcome `proposed`, whose `note` and `input-sha256` name the text the proposals were made for; or, at a triage, a review result with outcome `warn` or `fail`, whose items are its `warn` and `fail` findings;
- that text: in a revise run, the continuation record's `made-for.text`; the run published that text to the note before it asked for the proposals, or it is the run's start text; for a single edit, the note, or the `--text` file the edit ran on; at a triage, the note's file: a triage takes only fresh results, so the note holds the text they judged, in the parts the criterion watches;
- the operation the proposals came from, for its preserve rules; at a triage, the review result's `criterion` file instead.

If no answers file exists yet for a proposed edit result, create it: `commonplace-review answers create --from <result path>`. It writes `<result stem>-answers.md` beside the result, every item `pending`. Never write a hash by hand.

Authority: the decisions are the operator's. The agent presents, records and runs commands. It never approves, rejects or defers an item on its own judgment. `deferred` is a decision too: set it only when the operator says to defer the item.

## Procedure

1. Before the items, give the operator the full paths of the note, the answers file and the question file, so they can open each. Present each item: the quoted passage in context, the proposed `change`, the worker's `reason`, and any preserve rule of the operation that bears on it. Choose the context by what the operator needs to judge the item. The sentence is enough for a local rewording. Show the paragraph, or the neighbouring sentences, when the change drops or moves a clause, when the passage refers to text around it, or when the same wording occurs nearby. Show more whenever the operator asks. Ask the operator: approve, reject or defer. One item per question unless the operator asks for the whole list.
   A finding item, at a triage, is one finding of a review result. Present the criterion (the result's `criterion` and its file), the passages the finding's `quotes` name, in context as above, and the reviewer's `reason` and `level`; a `document` finding has no quotes. The operator decides whether the finding stands: approve means the finding is right and the plan fixes it; reject means the finding is wrong, and nothing fixes it; defer leaves it for later.
   On a rejection, ask the operator one more question: is the finding wrong for this note only, or is the criterion too broad? Record the answer in the `reason`, in the operator's words. When the operator says the criterion is too broad, also append one line under Open observations in `kb/log.md` on the operator's word: `- OBSERVATION: [<criterion path>, <answers file>] — <the operator's reason>`.
   A carried-over item has `carried-from`: the operator already decided the same proposal, with the same `quote` and `change`, or the same finding of the same criterion, for an earlier text of the note. Present it as carried over: the earlier `state`, the operator's `reason` and `revisit` when present, `decided-at`, and the answers file `carried-from` names. Ask only whether the operator wants to change that decision. If not, leave the item as it is.
2. Record each answer in the item, exactly:
   - approve: `state: approved`; a `reason` only if the operator gives one;
   - reject: `state: rejected` and `reason` in the operator's words; do not suggest a reason and do not carry one over from another item;
   - defer: `state: deferred`, `reason`, and `revisit`, the condition under which the operator wants the item taken up again, in the operator's words;
   - every decided item also gets `decided-by: operator` and `decided-at` with the current UTC time, quoted, such as `'2026-11-15T12:00:00Z'`.
   - a changed decision on a carried-over item: record it as above with a new `decided-at`. Replace the earlier `reason` and `revisit` with the operator's new words, or remove them when the new state takes none. Remove `carried-from`.
   Change no `id`, `proposal`, `question` or `question-sha256`; add and delete no item. An item the operator does not decide stays `pending`.
3. Run `commonplace-validate <answers file>`. Fix only what you recorded wrongly; if it reports that the question changed, stop: the proposals are stale.
4. Show the operator the recorded decisions. Continue on the operator's stated word for this exact file; naming the file to a command is the approval, and no separate approval precedes it:
   - in a revise run, when some item is approved, run the command the continuation record's item gives in `how.command`: `commonplace-review run revise NOTE --answers FILE`, with every decided file of a triage named by its own `--answers`. It starts a new run and keeps a copy of each named file;
   - in a revise run, when no item is approved, run `commonplace-review answers record FILE` instead, so that later runs receive the rejections and deferrals;
   - for a single edit, run the same operation again with `--input answers=<answers file>`.
5. If the revise command refuses the file, read the refusal to the operator. When the validator refused it, correct the file as the refusal says, confirm with the operator and run the command again. When the note is no longer the text the proposals were made for, the write brief changed, or a review result no longer matches the note, the items are stale: keep the file with `answers record FILE` and run the operation again only on the operator's word.
6. The new revise run applies the approved items and publishes them without asking for approval of the whole text. When its report has `published: true`, follow [approve a text](./approve-a-text.md#after-a-revise-run-publishes): tell the operator what was published, with the path of the note and of the publication's diff; the change is uncommitted, `git diff` shows it, and the operator reverses it with git. When its report has `held` or a `continuation`, continue with [continue a revise pass](./continue-a-revise-pass.md).

Verification: `commonplace-validate` passes on the answers file. In a revise run, the new run's report lists the file under `answers` and shows the pass `applied` or `no-change`, and the run published, or held the candidate because it adds a validation warning; after a triage, the plan holds one fix entry per review result with an approved finding; a file that approved nothing was kept with `answers record` and appears in `commonplace-review decisions`. A single edit returns `changed`. Only `approved` items are applied; `pending`, `rejected` and `deferred` items are not.

The reasons stay in the answers file and, for a revise run, in the copy a command kept under the run's `answers/`, where `commonplace-review decisions` lists them. Do not copy them elsewhere.

Stop and leave the items `pending` when the operator declines to decide them.

## Findings answered by a structural change

The operator may answer a run's findings with a split or another structural change instead of at a stop. The note's text then changes, and no command applies the run's findings. Record the decisions this way:

1. Run `commonplace-review record <run directory>`. It writes one pending answers file per review result of the run that has a `warn` or `fail` finding, and prints each file with the command that records it. It changes nothing else.
2. Record each finding the operator discussed: its `state` and the operator's `reason`, as in step 2 above; in `resolution`, what was done; in `refs`, the new notes or the commit. A rejected diagnosis whose question the operator kept is `state: rejected`, and the `resolution` names the kept question and the change that answers it.
3. Leave every finding the operator did not discuss `pending`.
4. Never record a rejected finding as `approved` because a useful edit followed from it. `approved` means the finding is right.
5. Validate each file, then keep it on the operator's word for that file with the printed command, `commonplace-review answers record FILE`.
6. Run a fresh review on each resulting note. The decisions reach only later runs on the original note path.

## A plan that stopped on a proposal

A full or assessed revise run ends with nothing edited when its plan sets `stop`. The stop names proposals from the depth 1 reports and leaves `artifact/stop-answers.md` with one item. A stop is advice: the run has ended, and no command waits for the answer. It puts one question to the operator: follow the stop's proposal, or go on editing the note. The depth 1 reports are written to find the strongest objection, so a revised note gets a new one. A completed review does not show that its argument is right, and neither does a stop.

1. Read the plan's `stop`, the reports it names and the note. Do not revise the note because the run stopped.
2. For each proposal, tell the operator its kind as the plan gives it: a defect in the claim as scoped, a choice of a different artifact, or an extension that asks the note to cover more. For a defect, state the case, the two statements or the two readings, and check it against the note yourself.
3. Give your own recommendation for each proposal against the operator's stated purpose for the note and its write brief. Recommend a change only when its value against that purpose is clear. Say so plainly when a proposal is right in general and not needed here.
4. Record the operator's answer in `artifact/stop-answers.md`, once, when the operator decides: `approved` when the operator takes the proposed route, `rejected` with the reason, or `deferred` with the reason and a `revisit` condition. On the operator's word, keep the file with `commonplace-review answers record FILE`, the `how.record` of the continuation record's `plan-stop` item. The kept decision reaches the assessor of the next run on the note, so state in the reason which proposals it covers. Do not record again after the work: what followed is in the commits and in later runs on the note.
5. The work that follows is a separate task. The stop's text names the route it proposes, such as a rewrite. A rejected stop is followed, when the operator wants edits, by a new run with a replacement plan: `commonplace-review run revise NOTE --plan FILE`, with `stop` cleared and the passes the operator agreed to. Start either only on the operator's word.
6. A run that does not stop may still leave questions. Its assessment (`artifact/assessment.md`) lists `Claim questions for the operator`: small defects the passes cannot correct, and choices the assessor did not rank first. Tell the operator each one with its passage and report, with your recommendation as in step 3. Change the note for one only on the operator's word.
7. When successive runs on one note stop on new proposals after each revision, tell the operator that this is happening. Offer to write the note's contribution and its exclusions into a write brief, which the assessor reads; write it only on the operator's word.
