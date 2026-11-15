---
description: "Use when commonplace-review run revise stopped waiting on an artifact/<pass>-list-<key>.md file: take the operator's strikes in a session, record each with its reason, approve on their word and repeat the run"
type: types/instruction.md
---

# Resolve a strike list

Goal: the pass improves the text with only the replacements the operator wants, and each strike leaves the operator's reason in the run, so that the selection rules can later be revised from what the operator rejected and why.

Consumption: an agent in a session with the operator, reached from the run report's `waiting-for` text, from [revise an article or note](./revise-an-article-or-note.md) step 3, or from the passes README. Nothing here is inherited from the worker instruction; the rules below are the whole procedure.

Inputs:

- the run's JSON report: `waiting-for` gives the file, its proposal key, the approval command and the command to repeat;
- the proposed list in that file: one top-level `- ` entry per proposal, with its `quote` (the passage), its `change` (the proposed replacement or decision) and the worker's `reason`;
- the text the list was made for: the `text` of the last applied pass in the report, or `artifact/start.md` when none applied;
- the pass instruction, for its preserve rules.

Authority: the strikes are the operator's. The agent presents, records and runs commands; it never strikes, keeps or approves on its own judgment.

## Procedure

1. Present each entry: the quoted passage inside its sentence or paragraph, the proposed change, the worker's reason, and any preserve rule of the pass that bears on it. Ask the operator: approve, or strike. For a strike, take the reason in the operator's words; do not suggest one and do not carry one over from another entry. One entry per question unless the operator asks for the whole list.
2. Record in the file, exactly: under each struck entry, after its indented lines, one indented line `struck: <reason>`. Delete nothing, change no entry, add no entry. Approved entries stay as proposed.
3. Show the operator the recorded strikes and reasons. On the operator's stated word for this exact file, run the reported approval command, then the repeat command.
4. If the repeat stops on the same file again, its `what` names the blocking entry: deleted instead of struck, struck without a reason, or not as proposed. Correct the file as it says, confirm with the operator, approve again and repeat.

Verification: the repeat's report shows the pass `applied` or `no-change`, or the run waiting on `artifact/publication.json`. The file's text is the approved answer; an edit after approval is reported as unapproved and not used.

The reasons stay in the run, in the operator record beside the list file and in the selection context that binds publication. Do not copy them elsewhere; their reading across runs is the planning instruction's procedure-development step.

Stop and leave the run waiting when the operator declines to decide an entry.
