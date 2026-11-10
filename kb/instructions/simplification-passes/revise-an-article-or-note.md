---
description: "Use when a settled article or note should be improved for a stated audience through the passes an assessment recommends, each run as a short intent packet, rather than a generic editorial rewrite or a full automated pass"
type: types/instruction.md
---

# Revise an article or note

Make the artifact serve the operator's stated purpose without changing what it
claims, by assessing first and then running only the passes the assessment
recommends.

## Prerequisites

- A purpose in one line: who the reader is and what they should notice or be
  able to do. If the operator named only the artifact, propose the purpose
  at the top of the assessment and proceed under it; the operator corrects
  it if it is wrong.
- The artifact's claims are settled. A claim in dispute goes to the operator
  as a question, not into a pass.

## Steps

1. **Assess before editing.** Read the whole artifact. Report a ranked list
   of changes, highest value against the purpose first, each with its cost
   in one phrase and the pass from this directory that would make it. Name
   the sentence a hostile reviewer would attack first. Say what reads well
   in one sentence. Recommend only passes whose value against the purpose
   is clear; an item you would not defend is not recommended. Do not edit.

   If the highest-value change is a rewrite or a restructuring of the
   argument, report that and stop. The passes work on text, and text a
   rewrite will replace is not worth a pass; recommend passes only over the
   parts the assessment expects to survive.

   Two things the passes cannot own belong in the assessment too. For each
   candidate overclaim, propose whether the sentence is support (may be
   narrowed) or divergence (defend); the divergence items become the
   packets' `Defend:` line unless the operator objects. And list
   qualifications that have gone stale against the body: a scope bullet
   qualifying words the body no longer uses, a table cell filed under the
   wrong row, a cross-note ordinal pointing at the wrong list. These are
   claim questions for the operator, applied as their own commits after
   approval, not passes.

2. **Dispatch each recommended pass as a packet.** Proceed without waiting;
   the report gives the operator the chance to interrupt. Run passes one at a time,
   since they share one write scope. Order them by depth, not by the
   assessment's ranking: a pass whose edits a later pass would rewrite runs
   after it. The order that has held is split-out-a-treatment,
   narrow-overclaims, abstractions, readability-and-flow, plain-wording,
   opening-and-title. Abstractions runs before the structural moves although
   it is a wording pass, because one name per thing is what makes a
   duplicated caveat or two paragraphs on one subject visible; the opening
   runs last because the TL;DR restates a body the earlier passes have
   settled. Make the plain-wording list after the structural moves land; a
   list made against the earlier text names passages that have moved or
   gone. Each pass file carries an `effort`
   field: `simple` passes run in a fresh worker on a cheaper model or lower
   effort; `judgment` passes run on the session model, in the current
   context or a fresh worker. Use a fresh worker when the pass benefits from
   not having seen the conversation, as the plain-wording and
   readability passes do; run narrow-overclaims in the parent context, where
   the conversation is the evidence. Apply one-word swaps and two-sentence
   narrowings in the parent context rather than as packets. Small scoped
   edits from different passes may share one packet when its scope is
   enumerated. The packet is:

   ```
   Purpose: {the operator's one line}
   Artifact: {path}
   Pass: {absolute path of {pass}.md in this instruction's directory}
   Defend: {claims the operator has marked as divergence; a pass may not narrow them}
   Write scope: {the artifact only | none, return proposals}
   Return: the pass's report, plus items noticed but not applied, nothing committed
   ```

   The worker chooses means within the pass. It does not widen the write
   scope, add claims, or remove evidence.

3. **Integrate.** After each pass read the diff, and read every replaced
   phrase in its full sentence, not in the diff summary; a literal
   replacement can supply a referent the original left implicit and supply
   the wrong one. List each mapping, contrast, example, price, or link the
   diff removed and check that the pass report accounts for it; restore what
   it does not, in the classes [audit-a-prior-pass](./audit-a-prior-pass.md)
   uses. A pass that narrows or tightens a sentence tends to take its
   neighbours with it. Run `commonplace-validate` on the artifact, and commit the
   pass alone with a body saying what it was meant to make true. If the operator reverts part of a pass, record the
   threshold they applied in the pass file or a memory, so the next run
   starts from it.

4. **Stop when the recommended passes are done.** Report what each pass
   changed. Items you assessed but did not recommend, and the not-applied
   items the workers returned, are listed once, not run.

## Run it as a workflow

`commonplace-review run revise ARTIFACT --purpose TEXT [--defend CLAIM ...]`
runs these steps with headless workers, which never write the checkout. Its
run directory is derived from the artifact's path and the hash of its text.
It stops with a proposal wherever this procedure waits for the operator.
Repeating alone never approves the proposal or starts its dependent work.
A repeat reuses the recorded `--purpose`, `--defend` and profiles unless you
give them again. Each stop prints a JSON report whose `waiting-for` gives
what to do, the file, proposal key, `approve-command` and command to repeat.
Read and optionally edit the proposal, run its `approve-command`, then
repeat the workflow command. Approval captures that text; later edits have
no effect until approved again, and the report lists each file edited after
its approval under `unapproved-edits`. Changed proposal inputs require fresh
approval. An agent may approve only on the operator's stated word for that
specific proposal; it must not infer approval from a request to retry.

1. Step 1 runs as one assessment ask, on the profile for `judgment`. The run
   writes `assessment.md` and proposes `plan.yaml` under the run directory's
   `artifact/` and stops. `--plan FILE` puts your plan there first, and then
   no assessment runs, but explicit approval is still required. The plan holds `purpose`, `defend`, `passes` in run
   order (each a `pass` name and an optional `scope`) and `stop`. Read the
   assessment, edit the plan in place and approve it. A proposed or approved
   plan with `stop` set ends the run without editing the artifact. To run
   passes anyway, clear `stop` and list the passes in the plan, run the
   `approve-command` in the report's `override`, then repeat.
   The command rejects a plan that names an unknown pass, misses a field or
   breaks the depth order the pass files declare. You may edit and reapprove
   the plan at any later stop: the passes whose inputs did not change replay, and the
   others run again.
2. Step 2 runs each listed pass as one worker, on the profile from
   `instructions/review-profiles.yaml` that its `effort` selects. Code checks
   the revised text (title, type, brief declaration and H1 kept; no new validation
   failure), and the next pass works on that text. The artifact is written
   once, at the end, and only when every pass ended `applied`, `no-change`
   or `skipped`. After a `problem` pass, or while the run waits, nothing is
   written, and `not-applied` names the run file holding the proposed text.
   It does not commit.
3. Plain-wording and abstractions stop with `artifact/<pass>-list-<key>.md`.
   Delete each entry you strike, with its indented lines, run the stop's
   approval command, then repeat; the worker applies only the approved entries. A list made again for
   another text gets a new file and stops again.
4. Narrow-overclaims runs only when the plan's `defend` list is not empty.
   Split-out-a-treatment does not run. Both are reported as skipped, left
   for this procedure in a conversation.
5. An artifact edited between invocations has another hash, so the command
   opens a new run and assesses again; `--plan FILE` names a plan and skips
   the assessment. An artifact changed during a run is a conflict: nothing
   is written, and the report names the run file holding the proposed text.

Step 3 stays with the operator: each pass's report and the text it left are
under `artifact/reports/` and `artifact/texts/`; read each diff, undo in the
artifact what a report does not account for, and commit. Use this procedure in a
conversation instead when the passes are chosen as the conversation goes,
when a pass needs the conversation as evidence, or when each pass should be
integrated and committed before the next one runs.

## Headless write briefs

When the artifact declares a [write brief](../../types/write-brief.md), the assessment and every pass
(including candidate-list and apply workers) receive its captured text as
`brief`. Pass workers also receive this revision instruction as `workflow`;
apply its constraints to the assigned pass, not additional passes or the
interactive dispatch procedure.

Treat the supplied brief as binding retained intent. Keep its must-keep,
must-exclude and reserved decisions in both the plan and the edited text.
Do not amend the brief or remove or change the artifact's `brief:` field.
If the purpose, defended claims, approved plan, approved candidate list or
pass instruction conflicts with it, report the conflict through the
worker-problem output and stop. Approval of a plan or list does not authorise
amending the brief. The operator must resolve the commission change outside
this workflow before continuing.

Use the captured input, not a reread of the live brief. A brief change between
invocations invalidates affected calls and plan approval; a change during an
invocation blocks publication. A missing or invalid declared brief stops the
run before workers launch. Supplying it does not mechanically verify that
an edit respects its meaning; the worker must identify conflicts.

## Budget

- The assessment is one full read. Each pass is one more. Do not re-read
  linked notes unless a pass names them.
- A worker gets the artifact path and the packet, never the conversation.
- Propose-only work (the assessment, the plain-wording list, title
  proposals) may run in parallel; edits to the artifact run in sequence.
- Stop when the recommended passes are done. An item not recommended costs
  nothing; recommending a pass of unclear value costs a read and a diff.

## Verify

- Every applied change traces to a recommended pass.
- Every passage a diff weakened is accounted for by that pass's report.
- No claim, evidence, or qualification changed unless the operator asked.
- Each pass has its own commit and validation passed before it.
- Operator reverts have been recorded as thresholds.

---

Relevant Notes:

- [Intent-framed delegation is a control regime; prompt length does not establish it](../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — rests-on: the packet fixes purpose, bounds, and return; the worker chooses means
- [An author should fix what the executor can't determine, not what it will](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: why the passes state outcomes and preservation rules rather than edit sequences
