---
description: "run revise and run rewrite end at their first stop and are never resumed; a revise run leaves a continuation record, and a later command naming the answers file or the run is the approval, replacing approve and operator records"
type: reference/types/adr.md
status: accepted
---

# 138 — A stop ends the run, and naming its output is the approval

**Status:** accepted; decided by the operator on 2026-11-18 and implemented the same day. No live run has exercised it yet.
**Date:** 2026-11-18
**Amends:** [ADR 137](./137-revise-publishes-without-a-publication-stop.md), whose clause "a run continues after it publishes" this replaces: a run publishes and then ends. It also changes what [ADR 127](./127-review-runs-as-workflows-over-result-files.md), [ADR 134](./134-stops-record-the-operators-answers-in-one-typed-file.md), [ADR 135](./135-improvement-procedures-are-three-plans-on-one-runner.md) and [ADR 136](./136-note-rewrites-run-as-a-workflow-that-ends-at-operator-approval.md) say about approval, repeating a command and the publication stop, and what [ADR 130](./130-the-operator-decision-record-is-a-query-over-the-state-tree.md) names as the source of the decision listing. Their other decisions stand.

## Context

A revise or rewrite run stops where it needs something no worker in the run can supply: the operator's decision on proposals, findings or a candidate text, a plan's `stop`, or a repair after a failed worker. Four forces act on what happens after a stop.

A run that publishes changes the note's text. A rule that finds a run again by the note's text must then also find it by the text it published, and must tell it apart from a later run on a reverted text.

An approval must be bound to what it approves. An [answers](../../types/answers.md) file already names its question by path and hash, and the validator checks that binding. A second capture of the file, bound by a key, repeats that binding and adds one command at every stop.

Plan entries after a per-item entry should run on a text that has the operator's approved items. If they run first, they edit a text that is about to change.

The operator wants continuation to be interactive first. An agent in a session with the operator takes up what a run left. Moving parts of that session back into the workflow is later work, decided from recorded sessions.

## Decision

**A stop ends the run.** A run ends in one of three ways: it completed, it needs continuation, or it failed. Every invocation of `run revise` or `run rewrite` starts a new run. No run is repeated or resumed. A run's directory is named by its UTC start time under the note's path, and the run records the hashes of its start text and of the write brief it captured.

**A revise run publishes what it can, then ends.** It ends at its first per-item entry. Before that entry is asked for proposals, the run publishes what the earlier entries applied. The proposals are then made on the published text, their pending answers file is written, and the run ends. Later entries wait. A failed entry does not hold back the entries before it: they are published under the usual checks. A candidate that adds a validation warning is held, and the run ends there without asking for proposals. Publications of one note, by any run or by `publish`, take the note's publication lock, so two runs cannot both publish over the same text. So every item a run leaves concerns the text it last published, or its start text.

**What is left is a continuation record.** The run writes it and gives it in its report. It names the text it was made for and one item per piece of unfinished work, in dependency order. Each item names the actor expected to be able to resolve it (the operator, a session agent, or a worker at a stated effort), the items to settle first, the command or instruction step that proceeds, and the evidence. An entry not run proceeds from a one-entry plan the run writes, which keeps the entry's scope; a fix names the run's copy of its review result. The actor is an estimate, not a permission. A session agent continues with the operator by [continue a revise pass](../../instructions/continue-a-revise-pass.md).

**Naming the file or the run is the approval.** A later command acts on a stop's output by naming it. `run revise NOTE --answers FILE` applies decided proposals or fixes approved findings, in a new run. `publish RUN` publishes the candidate a run held, and `publish RUN --revised FILE` the operator's revision of it. The agent runs such a command only on the operator's word for that exact file or run. There is no separate approval step, no operator record and no proposal key. Each command checks its own input. A run over answers keeps a copy of each named file. It refuses answers the validator refuses, proposals made for another text of the note or under another write brief, and a file that approves nothing. `publish` refuses when the note, the candidate, its diff, a rewrite's accepted review or the brief changed since the run, or when the operator already published the candidate.

**Decisions nothing consumes are kept by a recording command.** A rejection, a deferral, a plan-stop answer and decisions on an overtaken run's findings have no command that acts on them. `commonplace-review answers record FILE` keeps such a file in the run that asked it, with no key and no tie to a waiting run.

**The decision listing and the carry-over read kept answers.** `commonplace-review decisions` lists the kept answers, each publication, the answers files a continuation record waits for, and each held candidate not yet published. The carry-over of earlier decisions to later runs reads the same kept answers. Answered operator records of revise and rewrite runs are converted once, in place, by a script; the code has no reader for them. Operator records of the retired full pass are still read, as ADR 135 decided.

**Every rewrite holds its accepted candidate.** A rewrite run whose accepted candidate differs from the note ends with it held; `publish RUN` publishes it.

## Considered alternatives

**Keep the approval step.** Rejected by the operator. ADR 134 kept `approve` because the key bound an answer to its context, so that a changed context withdrew the approval. Each consuming command now checks the context that matters to it: the note's text, the brief and the candidate files. The validator binds the answers to their question. A separate capture added a command at every stop and a second file per decision.

**Let the old run finish its stopped entry.** Rejected. The run must be found again after it published, which is the lookup this decision removes, and its end depends on a later invocation. The operator's rule that no run is repeated excludes it.

**A handoff carried by the operator, chained by hashes.** Not adopted. A later session takes up unfinished items from the continuation record, the note's run records and the record of the earlier session. A stricter handoff is the fallback if recorded sessions show that a later session cannot tell what changed and what remains.

**A reader for old operator records.** Not adopted. A one-time conversion turns answered records into kept answers, so the code keeps one reader. Old run directories keep their hash names, and the listing reads both forms.

**Apply approved answers with `run edit`, then publish with a separate command.** Not adopted. It costs the session agent two commands on every per-item entry.

Free choices resolved by the implementing agent, open to the operator: the files that capture what a run read (`triage-inputs.json`, `earlier-decisions.json`, the earlier stop decisions) stay as a record, though nothing reads them back; the record of continuation sessions stays in the workshop that defines the trial.

## Consequences

A failed pass is not continued. A new pass pays again for the assessment, the edits and, in the full procedure, the compression synthesis and the role report. Fresh review results are reused from the shared store.

Continuation depends on a session agent following an instruction. Nothing schedules the items of a continuation record. A record nobody reads leaves its work undone; `decisions` shows the answers files it waits for as pending, and the held candidate as a pending publication.

A run may publish twice: before a per-item entry's proposals and at its end, when that entry proposed nothing. Nothing detects an answers file edited between the operator's word and the command; the kept copy records the text the command acted on. A held candidate the operator declines has no consuming command; it stays listed as a pending publication until the note changes.

Until the conversion script has run on a state tree, the decisions in that tree's revise and rewrite operator records are neither listed nor carried over.

Operativity: `commonplace-review run revise`, `run rewrite`, `publish`, `answers record` and `decisions` consume the change in Python, which enforces the end of a run, the checks on a named input and the kept copies. Session agents reach it through the [review-system guide](../README-REVIEW-SYSTEM.md), continue a revise pass, [decide items](../../instructions/decide-items.md), [approve a text](../../instructions/approve-a-text.md) and the multistage writing skill, with the force of instructions. The rule that a command runs only on the operator's word for that exact file rests on those instructions, as it did before.

Limits: no live run has ended at a stop under this decision, and no session has continued from a continuation record. Whether a later session can take up items from the records alone, without a handoff, is untested. The decision covers revise and rewrite runs. Gate sweeps keep `--resume` and `retry`.
