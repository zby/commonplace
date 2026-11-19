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

   When readers scan a list or table to choose or compare items, recommend
   [Readability and flow](./readability-and-flow.md) if repeated openings bury
   the distinction those readers need. Name the reader’s task and two entries
   that hide the distinction. Repetition alone is not a reason to edit.

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

   Earlier stops the operator decided may come too, in the section
   `Earlier stops` of `earlier-decisions`, each with its stop, the
   operator's decision and reason, and any resolution. A rejected stop is
   one decision on everything the stop named, so read the operator's reason
   to see which proposals it covers. Do not stop again on a proposal the
   operator rejected, and do not list it again as a claim question, unless
   the text changed in a way that answers the operator's reason or the new
   report gives a case the reason does not address; when you raise it
   again, say which.

   Depth 1 review reports may come with the artifact as well: critique,
   composition friction and premise decomposition. These reports are
   written to find the strongest objection, so every text gets one, and a
   revised text gets a new one. A proposal is not a defect because a report
   made it. Judge each proposal that would change what the artifact is (a
   split, a merge, a different claim or a rejection) against the claim as
   the artifact scopes it, and place it in one of three kinds:

   - **Defect.** The report shows the claim is wrong or unusable as scoped:
     a case inside the artifact's stated conditions for which the claim is
     false, two statements of the artifact that cannot both hold, or two
     readings that the artifact's own wording both supports and under
     which the reader would conclude or do different things. You can state
     the case, the two statements or the two readings. A term the artifact
     does not define is not by that fact a defect.
   - **Choice.** The report proposes a different artifact without showing a
     defect: a split, a merge, a different thesis or contribution.
   - **Extension.** The report asks the artifact to cover more: further
     cases, grounds for a premise the artifact states as its condition, or
     a neighbouring question. The claim as scoped stands without it. A
     claim made relative to a stated condition does not have to establish
     that condition.

   The compression synthesis's proposals are sorted in the same way.

   A defect stops the run when correcting it would replace or restructure
   the text the passes work on: a different thesis, a split, a merge, a
   reordered argument. A choice stops the run only when you judge, against
   the purpose and the brief, that it is the highest-value change; a
   report's making the proposal is not that judgment. Then set the plan's
   `stop` and list no passes. In the stop, give each proposal's kind and
   the repository path of its report; for a defect, state the case, the
   two statements or the two readings; for a choice, say that no defect is
   shown, why you rank it first, and that the operator may decline it. The
   run then ends with nothing edited, and the operator decides the
   proposal.

   Everything else goes in the assessment under the heading `Claim
   questions for the operator`, and the passes are planned as usual. This
   covers a defect that one or two sentences would correct, with its
   passage, its case and the report's path; a choice you do not rank
   first, marked as a choice with no defect shown; and a proposed change
   of title or file name. The passes cannot make these changes, because
   they do not change claims. Scope a pass away from a passage that has an
   open claim question.

   An extension does not stop the run. List it once among the findings not
   acted on, with the reason, and plan the passes as usual. Recommend an
   extension only when the purpose or the brief asks for that coverage. An
   extension into something the brief excludes is never recommended. When
   you cannot tell a defect from an extension, say so in the plan and
   treat it as a choice.
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
no assessment either: it ends with one answers file per fresh `warn` or
`fail` result, the operator decides each finding with
[decide items](../decide-items.md), and a new run that names the decided
files with `--answers` fixes the approved findings only, one entry per
result with an approved finding. The full procedure, `--full`,
first runs every review operation that declares a `depth` on the artifact,
and the type and collection reviews, through the same route as `commonplace-review run gates`. Its results go to
the shared store, and fresh results are reused. The compression synthesis
then runs on the compression checks' results, and the role report on the
artifact's inbound contexts; neither publishes a result. The assessment
receives the fresh `warn` and `fail` results, the depth 1 reports, the
synthesis report and the role report. A review that ends without a result stops the run before the
assessment. The full procedure does not review the edited text. Every
invocation is a new run, named by its start time under the artifact's path;
no run is repeated or resumed. The run ends at its first stop, where this
procedure waits for the operator, and leaves a continuation record in its
report: each piece of unfinished work, the actor expected to resolve it and
the command or step that proceeds. In a session, follow
[continue a revise pass](../continue-a-revise-pass.md). Assessment, planning
and settled intermediate passes are preauthorized; never wait for routine
plan approval. Each stop's file is a pending [answers](../../types/answers.md)
file: record the operator's decision on its items, then name the file to the
command that acts on it. Naming it is the approval. An agent names a file
only on the operator's stated word for that exact file; it must not infer
approval from a request to retry. This instruction and the pass files own
judgment; worker prompts name inputs, not additional criteria.

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
   run ends; its continuation record names it in a `plan-stop` item.
   A stop is advice; no command waits for its answer. Record the
   operator's decision on the proposal there once: `approved` to take the
   proposed route, or `rejected` or `deferred` with the operator's reason.
   Keep the file with `commonplace-review answers record FILE`. The work
   that follows is a separate task and is not recorded in the file.
   The command rejects a plan that names an unknown pass, misses a field,
   has a field it does not know,
   names a `finding` that is not a review result of the artifact, or breaks
   the depth order the pass files and the findings' criteria declare. A replacement supplied
   with `--plan` runs as a new run.
2. Step 2 runs each listed pass as one run of the edit route, the same one
   `commonplace-review run edit` uses, on the profile from
   `instructions/review-profiles.yaml` that its `effort` selects. Code checks
   the edit result and the revised text (title, type, brief declaration and
   H1 kept; no new validation failure; link targets and quoted spans kept),
   and the next pass works on that text. Each run's result and candidate are
   retained under `artifact/edits/`. A `problem` pass ends the run: the
   run publishes what the passes before it applied, and that pass and the
   later ones are left in the continuation record.
   The workflow does not commit.
3. A pass whose `decision` is `per-item` (plain-wording, abstractions) first
   returns proposals. The run publishes what the earlier passes applied,
   asks for the proposals on that text, writes the pending answers file
   `artifact/<pass>-answers.md` and ends: one item per proposal, holding its
   `quote`, `change` and `reason`, every item `pending`. Later passes wait in
   the continuation record. In a session, follow
   [decide items](../decide-items.md): the agent presents each item in
   context, asks, and records the operator's answer as `approved`,
   `rejected` with a reason, or `deferred` with a reason and a revisit
   condition. On the operator's word for that file,
   `commonplace-review run revise ARTIFACT --answers FILE` starts a new run
   of that pass with the answers file as its `answers` input, which applies
   only the `approved` items and publishes. Code refuses a candidate that
   changed the passage of an item that is not approved. The command refuses
   answers the validator refuses, a note that is not the text the proposals
   were made for, a changed write brief, and a file that approves no item;
   keep such a file with `commonplace-review answers record FILE`.
   Decisions carry over between runs on the same note. When a
   run starts, code collects the operator's decided items from the earlier
   runs on the note and keeps them in the run as `earlier-decisions.json`.
   The pass receives them as its `earlier-decisions` input. A proposal with
   the same `quote` and `change` as an item the operator already decided
   starts decided as before, with `carried-from` naming the earlier answers
   file. The run still ends at the stop, and the operator may change such an item.
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
5. The command publishes a changed text to the artifact without a stop:
   before a per-item pass is asked for proposals, what the earlier passes
   applied, and when the run ends, what the passes applied since. Approved
   items are published when applied, with no second approval. It writes
   only while the artifact holds the text the run last knew and the
   captured brief is unchanged. Each publication is kept under
   `artifact/publications/` with its diff and listed in the report's
   `publications`. Nothing is committed. After a run publishes, follow
   [approve a text](../approve-a-text.md): tell the operator what was
   published, with the path of the note and of the diff; `git diff` shows
   the change, and the operator reverses it with git.
   A text that adds a validation warning the artifact does not have is held
   instead, and the run ends. Follow [approve a text](../approve-a-text.md):
   show the operator `artifact/final.md` and `artifact/final.diff`, and on
   the operator's word run `commonplace-review publish RUN`, or
   `publish RUN --revised FILE` for the operator's revision. Do not edit
   the candidate to revise the text: supply `--plan`, change workflow
   inputs, or start a new run.
6. Every invocation is a new run and needs a mode: `--assess` to commission
   planning, `--triage` to decide the findings, `--answers FILE` to apply
   decided answers, or `--plan FILE` to execute fixed work. A bare command
   does not choose a mode. An artifact changed during a run is a conflict:
   nothing is written, and the report names the run file holding the
   proposed text.

Step 3 stays with the operator: each pass's report and the text it left are
under `artifact/reports/` and `artifact/texts/`; read each diff after the
run publishes. If a report does not account for an edit, revise through workflow
inputs or `--plan`, not by editing the generated candidate, or reverse the
publication with git. Commit only after the operator has seen the
published diff. Use this procedure in a
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
  headless workflow instead retains per-pass reports and checked texts, and
  writes the artifact only through its recorded publications, without
  committing.
- Operator reverts have been recorded as thresholds.

---

Relevant Notes:

- [Intent-framed delegation is a control regime; prompt length does not establish it](../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) — rests-on: the packet fixes purpose, bounds, and return; the worker chooses means
- [An author should fix what the executor can't determine, not what it will](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: why the passes state outcomes and preservation rules rather than edit sequences
