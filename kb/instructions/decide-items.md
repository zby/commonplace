---
description: "Use when a procedure stopped on a pending answers file over a list of proposals, such as a per-item pass's <pass>-answers-<key>.md or a per-item edit result: take the operator's decision on each item in a session and record it"
type: types/instruction.md
---

# Decide items

Goal: every item of the question carries the operator's own decision, with the operator's reason where one is required, so that only what the operator approved is applied and the reasons stay available for revising the procedure that proposed the items.

Consumption: an agent in a session with the operator. It is reached from a run report's `waiting-for` text, from [revise an article or note](./simplification-passes/revise-an-article-or-note.md) step 3, or after `commonplace-review run edit` returned `proposed`. Nothing here is inherited from the worker instruction; the rules below are the whole procedure. For the approval of one exact text, follow [approve a text](./approve-a-text.md) instead.

Inputs:

- the answers file (`type: types/answers.md`): its `question` names the question file, and each item holds an `id`, the question's `proposal` and `state: pending`;
- the question: an edit result with outcome `proposed`, whose `note` and `input-sha256` name the text the proposals were made for;
- that text: in a revise run, the `text` of the last applied pass in the report, or `artifact/start.md` when none applied; for a single edit, the note, or the `--text` file the edit ran on;
- the operation the proposals came from, for its preserve rules.

If no answers file exists yet for a proposed edit result, create it: `commonplace-review answers create --from <result path>`. It writes `<result stem>-answers.md` beside the result, every item `pending`. Never write a hash by hand.

Authority: the decisions are the operator's. The agent presents, records and runs commands. It never approves, rejects or defers an item on its own judgment. `deferred` is a decision too: set it only when the operator says to defer the item.

## Procedure

1. Present each item: the quoted passage inside its sentence or paragraph, the proposed `change`, the worker's `reason`, and any preserve rule of the operation that bears on it. Ask the operator: approve, reject or defer. One item per question unless the operator asks for the whole list.
2. Record each answer in the item, exactly:
   - approve: `state: approved`; a `reason` only if the operator gives one;
   - reject: `state: rejected` and `reason` in the operator's words; do not suggest a reason and do not carry one over from another item;
   - defer: `state: deferred`, `reason`, and `revisit`, the condition under which the operator wants the item taken up again, in the operator's words;
   - every decided item also gets `decided-by: operator` and `decided-at` with the current UTC time, quoted, such as `'2026-11-15T12:00:00Z'`.
   Change no `id`, `proposal`, `question` or `question-sha256`; add and delete no item. An item the operator does not decide stays `pending`.
3. Run `commonplace-validate <answers file>`. Fix only what you recorded wrongly; if it reports that the question changed, stop: the proposals are stale.
4. Show the operator the recorded decisions. Continue on the operator's stated word for this exact file:
   - in a revise run, run the reported approval command, then the repeat command;
   - for a single edit, run the same operation again with `--input answers=<answers file>`.
5. If a revise repeat stops on the same file again, its `what` names what the validator refused. Correct the file as it says, confirm with the operator, approve again and repeat.

Verification: `commonplace-validate` passes on the answers file. In a revise run, the repeat's report shows the pass `applied` or `no-change`, or the run waiting on `artifact/publication-answers.md`; an edit after approval is reported as unapproved and not used. A single edit returns `changed`. Only `approved` items are applied; `pending`, `rejected` and `deferred` items are not.

The reasons stay in the answers file and, for a revise run, in the operator record beside it, where `commonplace-review decisions` lists them. Do not copy them elsewhere.

Stop and leave the items `pending` when the operator declines to decide them.
