# Rerun the previously analysed agentic systems

## Commission

The operator commissioned this workshop on 2026-10-12 to rerun all systems
analysed under the previous analysis system. Produce fresh, source-grounded
coverage through the current
[`analyse-agentic-system` workflow](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md),
not conversions of old reviews. Use a rolling pool of four parallel system
pipelines, each with a quick independent audit before integration. Refill each
slot when its audit is resolved, without waiting for the other pipelines.
This document is the handoff; revising it does not launch runs. New dispatch is
currently stopped by operator direction, as recorded in the checkpoint below;
that stop takes precedence over the rolling-pool instructions.

Success means published, audited and integrated analyses for the checklist,
with consequential limits visible and unresolved targets honestly blocked.
Choose target order and execution details within the boundaries below. The
operator authorizes the bounded validation-path maintenance below as part of
execution. Other method changes, comparison regeneration and public landscape
synthesis remain separate commissions. This handoff includes the authority and
resume conditions; execution must not depend on the commissioning conversation.

## Population

[Systems](./systems.md) is the scheduling authority: **206 targets from 223
analysis records**, initially drawn from:

- 155 legacy implementation-grounded reviews.
- Seven legacy lightweight reviews.
- 12 authored agentic-system accounts.
- 43 generated historical reviews.
- Six current-engine sets already counted as complete by operator direction.

The six completed sets retain their recorded limits and prior audits; do not
reopen them for this commission. There were initially 200 remaining targets;
use the checklist and the current execution checkpoint below for progress.

Repeated reviews of the same named system share a row. Dated Instinctual Memory
reviews are grouped, and `gbrain-garrytan` is grouped with GBrain. Four
`.replaced.` predecessor files are excluded as extra targets. Paper-only
WikiSkill and the independent Stahl-G implementation stay separate, as do the
two SAGE systems and the LLM Wiki variants.

This is an inventory, not a verified count of upstream repositories. Resolve
identity and scope before assignment; record justified splits or merges rather
than silently dropping coverage. Historical links establish inclusion and help
resolve identity, not fresh analytical findings. Unreviewed TODOs, ingests alone
and workshop trials are not extra targets.

The earlier [agentic-memory-refresh workshop](../agentic-memory-refresh/README.md)
retains its pilots and history. Coordinate with unfinished assignments there
before assigning the same system. Legacy-engine completion does not count here;
published new-engine sets do. Preserve the historical evidence.

## Current execution checkpoint and next action

The [resume record](./resume-2026-10-12.md) records eight completed targets,
195 pending and three blocked or recovery-required. AgeMem and Agent-R are
integrated; the retained integration queue is empty. These are recorded facts,
not proof of current process ownership. Reconcile newer checklist entries,
execution records and active assignments before making writes or dispatching.

Rolling-dispatch support is implemented in the project Pi extension. Verify the
loaded tool schema as described below; do not treat the older runtime blocker
as current when `action` and `handles` are available.

The [validation-path maintenance decision](./validation-path-maintenance.md)
resolves the shared producer suspicion and lifts the pause for fresh eligible
runs. Worker path transcription, not supplied invocations, caused the inspected
failures. Individual recovery holds remain unchanged.

The operator subsequently directed the execution session to finish the running analyses,
stop new dispatch and check substantive reasonableness of the analyses affected
by path confusion. [Rolling execution 04](./rolling-04.md) records four stopped
runs, no new publications and the retrospective checks. The operator then
marked those four systems for fresh reruns rather than recovery of their old
runs. Progress is now eight complete, 195 pending (including four marked for
fresh rerun) and three recovery-required. **Do not resume the pool until the
operator releases this stop.** The earlier maintenance release does not override
this later execution stop.

The separately authorized worker convenience command is implemented in commit
`9b110e2f5`: [`commonplace-run validate-output <prompt-path>`](../../reference/commands.md#commonplace-run)
resolves validation parameters from the recorded open handout. Generated worker
instructions use it for immediate write–check–repair feedback; workflow-side
validation is unchanged. The command and instructions passed 1,161 selected
tests, including relevant slow tests. This implementation does not certify
historical drafts, modify frozen runs or release the operator stop. After release,
prepare fresh runs from a committed method containing this command and reconcile
all reserved assignments before filling the four slots.

The maintenance commission below retains the authority and evidence boundary
for the completed investigation. It superseded the older requirement for a
separate maintenance commission; it is not a requirement to repeat the work or
an independent authorization to restart dispatch.

Reserved or blocked assignments:

- **Agent Skills for Context Engineering:** the operator reported another agent
  still working on this target after the historical stop record. Treat it as
  reserved until its owner confirms completion, termination or an explicit
  handoff. An empty session-local job registry does not release that ownership.
- **ACE:** its open reconciliation attempt requires prior-worker status and a
  supported recovery decision before any replacement; see the checklist.
- **Academic Research Skills:** its source-exposure stop requires a separate
  recovery decision; see the checklist. Validation-path maintenance does not
  waive source-isolation rules.

After the operator releases the current dispatch stop, these individual holds
do not block other eligible systems. Preserve their evidence and keep them incomplete unless a
supported recovery or operator-approved exclusion is recorded.

## Bounded validation-path maintenance

Status: resolved by the linked maintenance decision. The following is the
retained scope of the investigation, not pending startup work. Reopen it only
if new validation-path evidence contradicts that decision; any such maintenance
release remains subject to the separate operator dispatch stop.

Purpose: establish whether nonexistent validation artifact paths came from the
supplied invocation or worker execution, and make new analyses safe to resume.
The bounded authority covers investigation, the minimum necessary current-method
correction, regression coverage and an evidence-based maintenance disposition.

1. Read the validation-path findings and evidence locations in the
   [prior execution record](./batch-03.md), the
   [AgeMem audit](./audits/batch-03-agemem.md), and the
   [Agent-R audit](./audits/batch-03-agent-r.md). Inspect the retained handouts,
   exact tool calls and returned validation results in their referenced run
   worktrees and traces. Include Agent Skills' `000008-epistemic` attempt only
   as read-only evidence; coordinate with its owner before accessing changing
   files. Do not reconstruct a missing result as if it had executed.
2. Compare the frozen invocation with the actual command and intended artifact
   path, then check the current producer and validation contract. Distinguish a
   producer defect, worker transcription error and unsupported command
   substitution. Successful publication alone does not discharge a worker's
   validation obligation. If evidence is unavailable, record the specific gap
   and keep the affected scope paused rather than inferring compliance.
3. If necessary, fix only the current validation-invocation producer, its
   associated instructions or path handling and regression tests. Follow
   repository test selection, including affected analysis suites and relevant
   slow tests for changed behavior. Do not weaken validation or isolation
   requirements. If the current method is already correct, document the
   evidence and the execution check needed to prevent recurrence instead of
   inventing a code change.
4. Retain a maintenance decision in this workshop with exact evidence locators,
   diagnosis, affected scope, any correction commit, checks and results, and an
   explicit lift-or-retain disposition for the shared pause. Link it from this
   README and update the checklist's operational status. Commit owned method
   corrections before preparing new runs so their frozen method includes the
   fix. Do not edit frozen methods, run states, retained outputs or historical
   traces, and do not retrospectively certify old failed validation attempts.
5. Once evidence and checks justify lifting a maintenance pause, record that
   disposition. Resume the rolling pool only when no operator dispatch stop is
   in force; the current stop requires explicit operator release. Supply fresh
   analysis coordinators only their source-first commissions, not historical
   findings or maintenance audit conclusions. Keep individual recovery holds
   separate. Escalate only missing evidence, unresolved ownership, or a repair
   requiring broader method or acceptance changes than authorized here.

## Execution and ownership

On a fresh start or resume, reconcile the checklist and retained execution
records with any active coordinators and assigned runs before dispatching.
Do not duplicate an assignment or assume a procedure edit stopped existing work.
If another orchestrator may still own the queue, establish an explicit handoff
or stop for clarification. Existing runs retain their frozen method and evidence;
this procedure does not authorize rewriting or discarding them. Then verify the
runtime prerequisites below before launching new work.

Use `openai/gpt-6.1-sol`, medium thinking, for the orchestrator, fresh
per-system coordinators and fresh auditors; analytical workers use `pi-sol`.
Keep **four system pipelines active while eligible work remains**, unless a
blocker requires a pause. A slot holds one analysis followed by its fresh audit;
four is the limit on these pipelines, not on their internal analytical workers.
Launch one fresh `commonplace-coordinator` for each system through the
`subagent` tool with `agentScope: "project"` and `cwd` set to that system's
isolated worktree. These per-system coordinators occupy the rolling window of
four pipelines; do not assign whole system analyses to `commonplace-worker`.
Each coordinator follows the standard skill and delegates its code-scheduled
analytical jobs to `commonplace-worker`; internal worker scheduling remains
unchanged.

Rolling dispatch requires a runtime that lets the orchestrator launch work,
receive an individual completion and dispatch its successor while other work
continues. The Pi `subagent` parallel call waits for the entire call's task set;
progress updates alone do not satisfy this requirement. Use the project
extension's asynchronous `action: "start"` for each coordinator, then
`action: "wait"` with the active handles to receive one completion. Remove the
completed handle from the pending set and launch that slot's auditor without
waiting for the other slots. After audit disposition, refill with the next
eligible system. Record the handle-to-assignment map and each result before
forgetting terminal handles. See [Pi rolling dispatch](../../../.pi/README.md#rolling-dispatch)
for call examples and lifecycle limits.

Before launch, verify that the loaded schema exposes `action` and `handles`,
as well as completing the standing worker-launch preflight. An older loaded
extension requires `/reload` before any jobs are started. Reload or orderly
shutdown cancels active jobs; handles do not survive it. Reconcile interrupted
assignments before replacement. If asynchronous operations are unavailable,
report the runtime blocker. Do not substitute wait-for-all dispatch, agent CLIs
or additional scheduling coordinators.

The orchestrator owns assignments, checklist updates, recovery decisions
and serial integration into `main`. Per-system coordinators own their isolated
runs and return results without integrating. Auditors own distinct reports
under `audits/`, not analysis outputs or shared bookkeeping. No two active runs
may own the same publication destination.

Keep analyses source-first: do not supply legacy findings, comparison values or
previous results to analysis coordinators or workers. The orchestrator may
use historical records for identity; only the subsequent auditor may compare
old and new findings. Preserve the skill's frozen-source and isolation rules.

After each new publication, commission a fresh auditor in that slot under
[Audit a rerun before integration](./audit-a-rerun.md), while other pipelines
continue. Once the audit disposition is recorded, queue a cleared result for
serial integration and refill the slot with the next eligible target. Do not
wait for the other slots or a shared completion checkpoint. Integration is owned by
the orchestrator, outside the four analysis/audit slots; queued results are not
yet complete. Drain that queue as results arrive rather than deferring it until
all analyses finish. Audit clearance does not replace integration's publication
checks.

A held or failed system releases its slot once its evidence, blocker and unblock
condition are recorded. It does not prevent other eligible systems from running.
A suspected shared-method defect pauses affected work and requires a maintenance
decision. For the known validation-path issue, use the retained maintenance
decision; do not repeat the resolved investigation as a startup gate. New
contradictory evidence follows the bounded scope above. A different shared
defect requires a new maintenance decision.
Do not repair accepted content outside a supported workflow or quietly broaden
the commission to work around a blocker.

Preparation permits unrelated uncommitted origin changes by default, excludes
their bytes, and records their exclusion; startup instructions and configuration
must still match the selected commit. `--require-clean-origin` requests strict
preparation. Integration still requires a clean origin on `main`. Coordinate origin writes
and commit owned audit/checklist bookkeeping at each integration boundary;
parallel analyses need not stop, but shared writes must not race with integration.
Resolve pre-existing uncommitted work with its owner before integration; this
commission does not authorize staging unrelated files. Preserve run worktrees and traces.
No cleanup or push is commissioned. Method edits are limited to the bounded
validation-path maintenance authorized above.

## Progress and checkpoints

Keep each checklist assignment traceable to its run and frozen source boundary.
For new runs, check a target complete only after publication, audit clearance
and verified integration; link its overview, audit and integration commit.
Distinguish work awaiting audit or integration from completed work. Failures and
local blocked/out-of-scope results remain incomplete unless the operator
explicitly approves exclusion.

Record each pipeline outcome as it arrives and report consequential findings,
worker problems and unresolved blockers without waiting for other slots. Keep
active assignments and the integration queue recoverable so an interruption
does not cause duplicate dispatch. Choose replacement targets from eligible work.
Escalate unresolved identity, authority or recovery decisions rather than
inventing an answer. Partial progress is useful; do not describe it as a
completed corpus refresh.

## Optional fast inventory

The existing [report statistics script](../../../scripts/agentic_system_rerun_stats.py)
can summarize generated reports cheaply. Its
[documentation](../../../scripts/README.md#agentic-analysis-rerun-statistics)
describes run filters and report-directory selection. It is not a source audit,
publication check or checklist-completion count; reportless failures are invisible.
Use it when it helps select what to inspect, not as an additional mandatory gate.

## Closure

The workshop closes when every target has an audited, integrated analysis or
an explicit operator-approved exclusion, and no running assignment remains.
Retain durable operational lessons in the appropriate library collection before
removing this temporary workshop and its Active Workshops entry. The accepted
analysis sets remain the durable outputs.
