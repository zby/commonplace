---
description: "Use when a settled article or note should be improved for a stated audience through the passes an assessment recommends, each run as a short intent packet, rather than a generic editorial rewrite"
type: types/instruction.md
---

# Revise an article or note

Make the artifact serve the operator's stated purpose without changing what it
claims, by assessing first and then running only the passes the assessment
recommends. This is a planning-containing procedure. When the purpose, scope
and pass are already fixed, use the fixed-plan route in the
[simplification-pass guide](./README.md#fixed-plan-execution-the-simple-baseline)
instead of assessing again.

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

   When the assessment finds that a claim itself is wrong or unsupported,
   the passes cannot fix it: they do not change claims. Set the plan's
   `stop`, name the claim, and name the rewrite route:
   `commonplace-review run rewrite NOTE --commission FILE`, with the
   commission prepared with `cp-skill-write-multistage`.

   Two things the passes cannot own belong in the assessment too. For each
   candidate overclaim, propose whether the sentence is support (may be
   narrowed) or divergence (must be kept); the divergence items become the
   packets' `Must keep:` line unless the operator objects. And list
   qualifications that have gone stale against the body: a scope bullet
   qualifying words the body no longer uses, a table cell filed under the
   wrong row, a cross-note ordinal pointing at the wrong list. These are
   claim questions for the operator, applied as their own commits after
   approval, not passes.

   Review findings may come with the artifact. Each is a stored review
   result with outcome `warn` or `fail`, and each names its criterion and
   the depth that criterion declares. Read them with the artifact. By
   default, a finding at depth *n* points at the pass at depth *n*. A
   finding whose criterion is named in a pass's `responds-to` may instead
   become a plan entry for that pass, with the result file as the entry's
   `finding`. That entry takes the depth of the finding's criterion in the
   order. [Fix a finding by a named strategy](../fix-warnings/fix-strategy-taxonomy.md)
   is such a pass: it changes only the passage the finding names. Recommend
   the change a finding points at only when its value against the purpose
   is clear. List the findings you do not act on once, each with its reason.

   The operator's decisions on findings of the artifact may come as
   `earlier-decisions`: findings the operator rejected or deferred at a
   triage, each with the operator's reason. Plan no fix for a finding the
   operator rejected unless the text changed in a way that answers the
   operator's reason; say so when you plan one. Plan no fix for a deferred finding unless its
   `revisit` condition is met.

   Depth 1 review reports may come with the artifact as well: critique,
   composition friction and premise decomposition. If one of them proposes
   changing what the artifact is (a split, a merge, a different claim or a
   rejection), set the plan's `stop` and list no passes. The stop names the
   proposal and the repository path of the report it comes from. The run
   then ends with nothing edited, and the operator decides the proposal.
   When the proposal is to move a full argument into a separate file, the
   stop may recommend [split out a treatment](./split-out-a-treatment.md);
   no procedure runs it.

   The [role report](../role-in-the-kb-gate.md) may come as well. It states
   the artifact's role in the KB from the passages that link to it: what
   each dependent needs from it, what it duplicates, and which
   recommendations in linking sources it has not taken up. It does not
   judge whether a claim is good theory: do not plan to cut content
   because no dependent uses it. Read it before
   you stop on a depth 1 proposal or plan around one. Check whether the
   proposal's cause may be a term or claim that dependents rely on: a
   contradiction inside the artifact can come from a term a dependent
   uses in another sense. When the proposed change, or a pass you would
   plan, changes a claim or term that dependents rely on, set `stop` and
   name those dependents in it, with the role report's run directory: the
   passes edit only the artifact, so the operator must decide the
   dependents' change too.

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
   Must keep: {what this run keeps beyond the write brief's Must keep; a pass may not narrow it}
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

`commonplace-review run revise ARTIFACT --assess --purpose TEXT [--must-keep CLAIM ...]`
runs these steps with headless workers, which never write the checkout. This
is the quick procedure. The assessment also receives the artifact's fresh
stored review results with outcome `warn` or `fail`, when any exist; the
command launches no review. Results with only INFO-level findings are not
given. A finding the operator rejected at a triage of the same result is
removed, and the operator's rejected and deferred findings of the artifact
come as `earlier-decisions`. The focused procedure makes no assessment: `--pass NAME` runs a
one-entry plan for that pass, and `--finding RESULT` runs a one-entry plan
that fixes that review result of the artifact. The triage, `--triage`, makes
no assessment either: it stops with one answers file per fresh `warn` or
`fail` result, the operator decides each finding with
[decide items](../decide-items.md), and the plan fixes the approved findings
only, one entry per result with an approved finding. The full procedure, `--full`,
first runs every review operation that declares a `depth` on the artifact,
through the same route as `commonplace-review run gates`. Its results go to
the shared store, and fresh results are reused. The compression synthesis
then runs on the compression checks' results, and the role report on the
artifact's inbound contexts; neither publishes a result. The assessment
receives the fresh `warn` and `fail` results, the depth 1 reports, the
synthesis report and the role report. A review that ends without a result stops the run before the
assessment. The full procedure does not review the edited text. Its
run directory is derived from the artifact's path and the hash of its text.
It stops with a proposal wherever this procedure waits for the operator.
Repeating alone never approves the proposal or starts its dependent work.
A repeat reuses the recorded `--purpose`, `--must-keep` and profiles unless you
give them again. Each approval stop prints a JSON report whose `waiting-for` gives
what to do, the file, proposal key, `approve-command` and command to repeat.
Assessment, planning and settled intermediate passes are preauthorized;
never wait for routine plan approval. Each stop's file is a pending
[answers](../../types/answers.md) file: record the operator's decision on its
items before the `approve-command`, then repeat the workflow command.
Approval captures that text; later edits require approval again and are
listed under `unapproved-edits`. Changed proposal inputs require fresh approval. An agent
may approve only on the operator's stated word for that specific proposal;
it must not infer approval from a request to retry. This instruction and the
pass files own judgment; worker prompts name inputs, not additional criteria.

1. Step 1 runs as one assessment ask, on the profile for `judgment`. The run
   retains `assessment.md` and `plan.yaml` under the run directory's
   `artifact/` for inspection and proceeds with the validated plan.
   `--plan FILE` supplies an explicit input or override without assessment
   or approval, including replacement of a stopped plan. The plan holds
   `purpose`, `must-keep`, `passes` in run order (each a `pass` name, an
   optional `scope` and, for a pass that declares `responds-to`, the
   `finding` it fixes) and `stop`. A plan with `stop` set ends the run without
   editing the artifact. To run passes instead, supply a replacement with
   `stop` cleared and the desired passes through `--plan`; editing the
   retained `artifact/plan.yaml` alone is not an override.
   A stopped plan also leaves `artifact/stop-answers.md`, an
   [answers](../../types/answers.md) file with one item for the plan. The
   run does not wait for it; its report names it under `stop-answers`.
   Record the operator's decision on the proposal there: `approved` to act
   on it as made, or `rejected` or `deferred` with the operator's reason.
   When the work that followed is done, add `resolution` (what was done,
   when it differs from or goes beyond the proposal) and `refs` (commit
   hashes, paths, a workshop directory) to the item. Run the reported
   approval command each time the file changes, so that
   `commonplace-review decisions` lists the current text.
   The command rejects a plan that names an unknown pass, misses a field,
   has a field it does not know,
   names a `finding` that is not a review result of the artifact, or breaks
   the depth order the pass files and the findings' criteria declare. A replacement supplied
   with `--plan` reuses calls whose inputs did not change and reruns the others.
2. Step 2 runs each listed pass as one run of the edit route, the same one
   `commonplace-review run edit` uses, on the profile from
   `instructions/review-profiles.yaml` that its `effort` selects. Code checks
   the edit result and the revised text (title, type, brief declaration and
   H1 kept; no new validation failure; link targets and quoted spans kept),
   and the next pass works on that text. Each run's result and candidate are
   retained under `artifact/edits/`. Every pass must end
   `applied`, `no-change` or `skipped` before final publication is offered.
   After a `problem` pass, or while the run waits, the original artifact is
   untouched, and `not-applied` names the run file holding the proposed text.
   The workflow does not commit.
3. A pass whose `decision` is `per-item` (plain-wording, abstractions) first
   returns proposals, and stops with the pending answers file
   `artifact/<pass>-answers-<key>.md`: one item per proposal, holding its
   `quote`, `change` and `reason`, every item `pending`. In a session, follow
   [decide items](../decide-items.md): the agent presents each item in
   context, asks, and records the operator's answer as `approved`,
   `rejected` with a reason, or `deferred` with a reason and a revisit
   condition. Run the stop's approval command, then repeat; the same
   operation runs again with the answers file as its `answers` input and
   applies only the `approved` items. Code refuses a candidate that changed
   the passage of an item that is not approved. Answers the validator
   refuses stop the run again naming the problem: correct the file and
   approve it again. Answers that approve no item end the pass as
   `no-change`. Proposals made again for another text get a new file and
   stop again. Decisions carry over between runs on the same note. When a
   run starts, code collects the operator's decided items from the earlier
   runs on the note and keeps them in the run as `earlier-decisions.json`.
   The pass receives them as its `earlier-decisions` input. A proposal with
   the same `quote` and `change` as an item the operator already decided
   starts decided as before, with `carried-from` naming the earlier answers
   file. The run still stops, and the operator may change such an item.
   Every other proposal is asked as usual. These are temporary procedure-development points for
   unsettled selection rules. The run retains the answers with each
   rejection's and deferral's reason in the operator's words. Use them to revise
   selection rules and checks, then evaluate those changes on retained and
   fresh examples before seeking separate authorization to remove a
   selection stop. This requires no new automatic learning infrastructure;
   fewer proposals alone do not establish reliability.
4. Narrow-overclaims runs only when the plan's `must-keep` list is not empty.
   Split-out-a-treatment does not run. Both are reported as skipped, left
   for this procedure in a conversation.
5. For a changed final artifact, follow [approve a text](../approve-a-text.md):
   inspect `artifact/final.md` and `artifact/final.diff`, record the
   operator's decision on the one item of `artifact/publication-answers.md`,
   which names the candidate's hash, then run the report's
   `commonplace-review approve RUN FILE --key KEY` command. Repeat to
   publish. The command writes the original once, only when the approved
   answers approve that exact candidate and the original and captured brief
   are unchanged. Repeating never approves. Do not edit the candidate to
   revise the text: supply `--plan`, change workflow inputs, or start a new
   run.
6. An artifact edited between invocations has another hash, so the command
   opens a new run. Choose `--assess` again to commission planning,
   `--triage` to decide the findings, or `--plan FILE` to execute fixed work. A bare command does not choose a mode. An artifact changed during a run is a conflict: nothing
   is written, and the report names the run file holding the proposed text.

Step 3 stays with the operator: each pass's report and the text it left are
under `artifact/reports/` and `artifact/texts/`; read each diff before final
approval. If a report does not account for an edit, revise through workflow
inputs or `--plan`, not by editing the generated candidate. Commit only after
approved publication. Use this procedure in a
conversation instead when the passes are chosen as the conversation goes,
when a pass needs the conversation as evidence, or when each pass should be
integrated and committed before the next one runs.

## Headless write briefs

When the artifact declares a [write brief](../../types/write-brief.md), the assessment and every pass
(including candidate-list and apply workers) receive its captured text as
`brief`. Pass workers receive [execute a revision pass](./execute-a-revision-pass.md)
as `execution`, not this planning procedure. That execution instruction carries
the pass bounds and brief constraints without commissioning assessment or dispatch.

Treat the supplied brief as binding retained intent. It is the one lasting
statement of what the artifact must keep and exclude. Keep its Must keep,
Must exclude and Reserved decisions in both the plan and the edited text.
Do not amend the brief or remove or change the artifact's `brief:` field.

The plan starts from the brief. Its `must-keep` lists only what this run adds
to the brief's Must keep: the operator's must-keep items and the claims the
assessment marks as divergence. Do not restate the brief's items there; every
pass receives the brief. Never plan a pass that conflicts with the brief.
When the purpose or the operator's must-keep items conflict with the brief,
set the plan's `stop`, list no passes, and name the brief item and the
conflicting text.

A pass worker that finds the purpose, the must-keep list, the validated plan,
an approved candidate list or its instruction in conflict with the brief
reports the conflict through the worker-problem output and stops. Selection
or publication approval does not authorise amending the brief. The operator
must resolve the commission change outside this workflow before continuing.

Use the captured input, not a reread of the live brief. A brief change between
invocations invalidates affected calls and dependent approvals; a change during an
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
- Conversational execution validates and commits each integrated pass. The
  headless workflow instead retains per-pass reports and checked texts, then
  permits one final write only after publication approval.
- Operator reverts have been recorded as thresholds.

---

Relevant Notes:

- [Intent-framed delegation is a control regime; prompt length does not establish it](../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — rests-on: the packet fixes purpose, bounds, and return; the worker chooses means
- [An author should fix what the executor can't determine, not what it will](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: why the passes state outcomes and preservation rules rather than edit sequences
