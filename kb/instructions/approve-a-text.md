---
description: "Use when commonplace-review run revise stopped waiting on artifact/publication-answers.md: show the operator the exact candidate and its diff, record their decision or supply their revised candidate, and continue on their word"
type: types/instruction.md
---

# Approve a text

Goal: a candidate text replaces the note only when the operator has seen that exact text and approved it, and a refusal leaves the operator's reason in the run.

Consumption: an agent in a session with the operator, reached from a run report's `waiting-for` text. Nothing here is inherited from the worker instruction; the rules below are the whole procedure. For a list of proposals, follow [decide items](./decide-items.md) instead.

Inputs:

- the run's JSON report: `waiting-for` gives the file `artifact/publication-answers.md`, its proposal key, the approval command and the command to repeat;
- the report's `new-warnings`: validation warnings that the text to publish has and the note did not have; empty when there are none;
- the answers file (`type: types/answers.md`): its `question` is the candidate `artifact/final.md`, or the revised candidate `artifact/revised.md` when the operator revised it, and its one item, `text`, names that file and its SHA-256 with `state: pending`;
- `artifact/final.md` and `artifact/final.diff` beside it; after a revision also `artifact/revised.md`, `artifact/revised-from-final.diff` (from the workflow's candidate) and `artifact/revised.diff` (from the note).

Authority: the decision is the operator's. The agent shows, records and runs commands. It never approves, rejects or defers on its own judgment, never revises the text on its own judgment, and never edits a file under the run's `artifact/`: the candidate and the revised candidate are workflow outputs, not inputs.

## Procedure

1. If the report's `new-warnings` lists warnings, tell the operator each one. A warning does not block approval; the operator decides with it in view.
2. Give the operator the full paths of the note, `final.md` and `final.diff`, so they can open each. Show the operator `final.diff`, and `final.md` when they ask for the whole text. Ask: approve this exact text for publication, approve it with changes, reject it, or defer. For approval with changes, follow [accept with a revision](#accept-with-a-revision).
3. Record the answer in the `text` item, exactly:
   - approve: `state: approved`;
   - reject: `state: rejected` and `reason` in the operator's words;
   - defer: `state: deferred`, `reason`, and `revisit` in the operator's words;
   - in each case `decided-by: operator` and `decided-at` with the current UTC time, quoted.
   Change no `id`, `proposal`, `question` or `question-sha256`.
4. Run `commonplace-validate` on the answers file. Stop if it reports that the question changed: the candidate is not the one the operator saw.
5. On the operator's stated word for this exact file, run the reported approval command, then the repeat command.
6. If the repeat stops on the same file with a `what` that names a refusal, read it to the operator. A rejection or deferral is a normal end: the note keeps its text. To revise the candidate beyond a stated change, the operator changes the workflow inputs, such as a replacement plan with `--plan`; do not edit `final.md`.

## Accept with a revision

Use this when the operator accepts the candidate with changes. The revised candidate replaces the candidate as the text to approve, and the operator approves that exact text.

1. Copy the candidate the run proposes, `final.md` or the current `revised.md`, to a file outside the run's `artifact/` directory.
2. In the copy, apply exactly the changes the operator stated, or the wording the operator approved. Change nothing else.
3. Supply the copy: `commonplace-review run revise NOTE --revised FILE`. It launches nothing. It is refused when the run is not waiting at its publication stop for the note's current text, or when the text fails the candidate checks (frontmatter, H1, validation); a refusal keeps the earlier candidate and its pending answers. Read a refusal to the operator.
4. Show the operator `revised-from-final.diff`, the diff from the workflow's candidate to the revised candidate. If the report's `new-warnings` lists warnings, tell the operator each one. The answers file now names `revised.md`, every item is `pending`, and any earlier approval is withdrawn.
5. Ask the operator to approve this exact revised text, approve it with further changes, reject it, or defer. Then follow steps 3 to 5 of the procedure. Do not set the item's `state` before the operator has seen the revised diff.

A repeat keeps the revised candidate. A further revision replaces it in the same way. If the workflow's candidate changes later, the run withdraws the revised candidate and says so in its report.

Verification: a repeat after approval reports `applied: true` and the note holds the approved text, `final.md` or `revised.md`. Code writes the note only when the approved answers pass the validator, the item is `approved`, its hash is that of the text to publish, and the note still holds the text the run started from. Any other case writes nothing.

Stop and leave the item `pending` when the operator declines to decide.
