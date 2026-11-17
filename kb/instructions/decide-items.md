---
description: "Use when a procedure stopped on a pending answers file over proposals or review findings, such as <pass>-answers-<key>.md, a triage's finding-answers-<key>.md or a per-item edit result: take and record the operator's decision on each item"
type: types/instruction.md
---

# Decide items

Goal: every item of the question carries the operator's own decision, with the operator's reason where one is required, so that only what the operator approved is applied and the reasons stay available for revising the procedure that proposed the items.

Consumption: an agent in a session with the operator. It is reached from a run report's `waiting-for` text, from [revise an article or note](./simplification-passes/revise-an-article-or-note.md) step 3, from a triage (`commonplace-review run revise NOTE --triage`), or after `commonplace-review run edit` returned `proposed`. Nothing here is inherited from the worker instruction; the rules below are the whole procedure. For the approval of one exact text, follow [approve a text](./approve-a-text.md) instead.

Inputs:

- the answers file (`type: types/answers.md`): its `question` names the question file, and each item holds an `id`, the question's `proposal` and `state: pending`, or, for a carried-over item, the earlier decision and `carried-from`;
- the question: an edit result with outcome `proposed`, whose `note` and `input-sha256` name the text the proposals were made for; or, at a triage, a review result with outcome `warn` or `fail`, whose items are its `warn` and `fail` findings;
- that text: in a revise run, the `text` of the last applied pass in the report, or `artifact/start.md` when none applied; the run published that text to the note before it stopped, unless the report's `not-published` says why not; for a single edit, the note, or the `--text` file the edit ran on; at a triage, the note's file: a triage takes only fresh results, so the note holds the text they judged, in the parts the criterion watches;
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
4. Show the operator the recorded decisions. Continue on the operator's stated word for this exact file:
   - in a revise run, run the reported approval command, then the repeat command;
   - for a single edit, run the same operation again with `--input answers=<answers file>`.
5. If a revise repeat stops on the same file again, its `what` names what the validator refused. Correct the file as it says, confirm with the operator, approve again and repeat.
6. A revise repeat applies the approved items and publishes them without asking for approval of the whole text. When its report has `published: true`, follow [approve a text](./approve-a-text.md#after-a-revise-run-publishes): tell the operator what was published, with the path of the note and of the publication's diff; the change is uncommitted, `git diff` shows it, and the operator reverses it with git.

Verification: `commonplace-validate` passes on the answers file. In a revise run, the repeat's report shows the pass `applied` or `no-change`, and the run published, waits on the next stop, or waits on `artifact/publication-answers.md` because the final text adds a validation warning; after a triage, the plan holds one fix entry per review result with an approved finding, or no entry when none was approved; an edit after approval is reported as unapproved and not used. A single edit returns `changed`. Only `approved` items are applied; `pending`, `rejected` and `deferred` items are not.

The reasons stay in the answers file and, for a revise run, in the operator record beside it, where `commonplace-review decisions` lists them. Do not copy them elsewhere.

Stop and leave the items `pending` when the operator declines to decide them.
