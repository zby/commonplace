---
description: "The focused, quick and full improvement procedures are three ways to make the plan commonplace-review run revise executes; the full-pass workflow and the fix procedure are retired, and the decision record still reads their packets and fix reports"
type: reference/types/adr.md
status: accepted
---

# 135 — Improvement procedures are three plans on one runner

**Status:** accepted; implemented under the operator's approval of the grouping design, in three steps.
**Date:** 2026-11-16
**Supersedes:** [ADR 051](./051-full-pass-packets-own-guarded-captures-and-resolutions.md) (packets own captures and resolutions) and [ADR 080](./080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) (full passes hand claim changes back as a pending revise).
**Extends:** [ADR 133](./133-edit-operations-run-alone-through-one-typed-route.md) and [ADR 134](./134-stops-record-the-operators-answers-in-one-typed-file.md): the runner uses their edit route, bounds, answers stops and publication unchanged.

## Context

Commonplace had three procedures that improve a note. The full-pass workflow ran method reports, wrote a packet with a disposition for the whole note, and for a `keep` ran an editor, a copyeditor and a closing cycle that reviewed the edited text again, with one repair. The fix procedure was a session instruction: an agent fixed the current review warnings and wrote a fix report with one row per finding. The revise workflow ran a plan of simplification passes.

ADRs 132 to 134 made review operations, edit operations and stops atoms: each is a typed file that runs alone with typed inputs and a typed result. After that, the revise workflow already did what each procedure needs. It executes a plan of edit operations in depth order, each through the `run edit` route. It stops for per-item answers and for approval of the exact final text, and it writes the note once. Its run directory resumes and replays. The full pass kept its own editor, record format and stop rules for the same steps, and the fix procedure kept a third way to edit and a third record.

The operator wants three procedures chosen by the time available and by what the operator sees in the note: a full one, a faster one, and a focused one in which the operator names one defect.

## Decision

**One runner, three ways to make its plan.** `commonplace-review run revise ARTIFACT` is the only workflow that improves a note. The procedures differ only in how the plan is made:

- **Focused.** The operator names the work. `--pass NAME` writes a one-entry plan for one edit operation on the whole note. `--finding RESULT` writes a one-entry plan for the edit operation [fix a finding by a named strategy](../../instructions/fix-warnings/fix-strategy-taxonomy.md), with that review result as its `finding` input; the operation changes only the passage the finding names. `--plan FILE` supplies any other plan. Nothing is assessed or reviewed.
- **Quick.** `--assess`. One assessor chooses the edit operations from the note and the note's fresh stored `warn` and `fail` results. No review is launched.
- **Full.** `--full`. Every review operation that declares a `depth` runs first, through the sweep's route, and fresh results are reused. The assessor then also reads the new findings, the depth 1 reports and the compression synthesis report. When a depth 1 report proposes changing what the note is, the assessor sets the plan's `stop` with that proposal and its source report, and nothing is edited. The operator acts on the proposal outside the run, or replaces the plan with `--plan`.

The plan is data, so the grouping can change without a code change. Code checks what it checked before: the plan lists known operations in increasing depth, each edit stays within its bounds, and publication needs answers that approve the exact candidate. Findings choose edits through the assessor. A finding whose criterion an edit operation names in `responds-to` becomes a plan entry for that operation, at the criterion's depth.

**The full-pass workflow is retired.** Its editor, copyeditor, packet, closing cycle and repair are removed, with `commonplace-review run full-pass`, `commonplace-review packet` and the two full-pass instructions. No workflow writes or resolves a packet.

**The fix procedure is retired.** Its instructions are removed, except the strategy codebook, which is the edit operation `--finding` runs. No procedure writes a fix report. Its use case is the focused procedure with a finding.

**The decision record still reads the old records.** `commonplace-review decisions` keeps its readers for full-pass packets under `kb/reports/state/review/packets/`, fix reports under `kb/reports/state/fixes/`, and operator records in full-pass run directories. Removing them would hide operator decisions already recorded. They are marked as a compatibility shim, to be removed when the operator says the old records are dispensable. This is the one place the cutover keeps old code.

## Considered alternatives

**Keep the full pass beside the runner.** Rejected. It duplicated the editor, the record and the stop rules, and its closing check was weak evidence (below). Keeping it would leave two answers to "how do I improve this note".

**Rename the workflow, for example to `improve`, in the cutover.** Not adopted, on the operator's choice. `revise` stays the command and the procedures are named by flag. A rename can follow without changing the plan model.

**Re-review the candidate in the full procedure.** Rejected. In the first run of the fix variant, on 2026-11-14, the re-review took 41 of the run's launches and most of its cost. Of four pairs whose findings were fixed, two passed and two still warned on other sentences, and one pair whose passage was not edited went from warn to pass. One re-review does not show whether a fix worked. After publication the changed parts' results are stale, and the next sweep refreshes them.

**Map findings to edits in code.** Not adopted. Only one edit operation declares `responds-to`, so there is no data to build a table from. The assessor uses the shared `depth` scale as its default.

**A stated criterion per review operation for the depth 1 stop.** Not adopted. It needs run data that does not exist. The assessor's judgment decides, and the plan names the proposal and its report.

**Give the assessor INFO-level findings.** Not adopted. The first run read about a dozen and acted on none.

**Run split out a treatment in a procedure.** Not adopted. It writes a second file and is not an edit operation. It stays a session instruction that the assessor can recommend in a depth 1 stop.

**Remove the old decision readers in the cutover.** Rejected, on the operator's choice: they are the only listing of the operator decisions already recorded in packets and fix reports.

**Keep the full-pass report type for the remaining packets.** Left open for the operator. No workflow writes the type, and the decision reader parses a packet's frontmatter without it. Only an explicit validation of an old packet would use it.

## Consequences

The operative consumer is `commonplace-review run revise`: its `--pass`, `--finding`, `--assess`, `--full` and `--plan` flags each make a plan, and the runner executes it through the edit route. Session agents reach the procedures through the [review-system guide](../README-REVIEW-SYSTEM.md) and the [simplification-pass guide](../../instructions/simplification-passes/README.md), with binding force for the order of steps; Python enforces the plan checks, the bounds and publication. `commonplace-review decisions` keeps reading the retired records.

Three things are given up. No procedure checks that an edit fixed its finding; the closing cycle did this, weakly. No procedure hands a note back with a typed disposition; a depth 1 stop gives a proposal with no typed states. No procedure keeps a per-finding fix record; a finding fixed by the focused procedure leaves an edit result and a publication decision, and a finding the operator rejects as spurious leaves nothing unless a stop asks.

Limits: whether the assessor chooses well from findings is not known; it has chosen only from the note alone, and those choices have not been judged. How often depth 1 reports propose a change is not known; if they propose on most notes, the full procedure stops on most notes and its default has to change. The `depth` values are a first guess on both kinds of operation. The full procedure's cost has not been measured.
