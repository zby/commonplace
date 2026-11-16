---
description: "Use when commonplace-review run revise stopped waiting on artifact/publication-answers.md: show the operator the exact candidate and its diff, record their decision, and continue on their word"
type: types/instruction.md
---

# Approve a text

Goal: a candidate text replaces the note only when the operator has seen that exact text and approved it, and a refusal leaves the operator's reason in the run.

Consumption: an agent in a session with the operator, reached from a run report's `waiting-for` text. Nothing here is inherited from the worker instruction; the rules below are the whole procedure. For a list of proposals, follow [decide items](./decide-items.md) instead.

Inputs:

- the run's JSON report: `waiting-for` gives the file `artifact/publication-answers.md`, its proposal key, the approval command and the command to repeat;
- the answers file (`type: types/answers.md`): its `question` is the candidate `artifact/final.md`, and its one item, `text`, names that file and its SHA-256 with `state: pending`;
- `artifact/final.md` and `artifact/final.diff` beside it.

Authority: the decision is the operator's. The agent shows, records and runs commands. It never approves, rejects or defers on its own judgment, and never edits `final.md`: the candidate is a workflow output, not an input.

## Procedure

1. Show the operator `final.diff`, and `final.md` when they ask for the whole text. Ask: approve this exact text for publication, reject it, or defer.
2. Record the answer in the `text` item, exactly:
   - approve: `state: approved`;
   - reject: `state: rejected` and `reason` in the operator's words;
   - defer: `state: deferred`, `reason`, and `revisit` in the operator's words;
   - in each case `decided-by: operator` and `decided-at` with the current UTC time, quoted.
   Change no `id`, `proposal`, `question` or `question-sha256`.
3. Run `commonplace-validate` on the answers file. Stop if it reports that the question changed: the candidate is not the one the operator saw.
4. On the operator's stated word for this exact file, run the reported approval command, then the repeat command.
5. If the repeat stops on the same file with a `what` that names a refusal, read it to the operator. A rejection or deferral is a normal end: the note keeps its text. To revise the candidate, the operator changes the workflow inputs, such as a replacement plan with `--plan`; do not edit `final.md`.

Verification: a repeat after approval reports `applied: true` and the note holds `final.md`. Code writes the note only when the approved answers pass the validator, the item is `approved`, its hash is the candidate's, and the note still holds the text the run started from. Any other case writes nothing.

Stop and leave the item `pending` when the operator declines to decide.
