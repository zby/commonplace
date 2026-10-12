# Rerun the previously analysed agentic systems

## Commission

The operator commissioned this workshop on 2026-10-12 to rerun all systems
analysed under the previous analysis system. Produce fresh, source-grounded
coverage through the current
[`analyse-agentic-system` workflow](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md),
not conversions of old reviews. Use a rolling pool of four parallel system
pipelines, each with a quick independent audit before integration. Refill each
slot when its audit is resolved, without waiting for the other pipelines.
This document is the handoff; revising it does not launch runs.

Success means published, audited and integrated analyses for the checklist,
with consequential limits visible and unresolved targets honestly blocked.
Choose target order and execution details within the boundaries below. Method
changes, comparison regeneration and public landscape synthesis are separate
commissions.

## Population

[Systems](./systems.md) is the scheduling authority: **206 targets from 223
analysis records**, initially drawn from:

- 155 legacy implementation-grounded reviews.
- Seven legacy lightweight reviews.
- 12 authored agentic-system accounts.
- 43 generated historical reviews.
- Six current-engine sets already counted as complete by operator direction.

The six completed sets retain their recorded limits and prior audits; do not
reopen them for this commission. The remaining 200 targets are pending.

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
continues. The current Pi `subagent` parallel call waits for the entire call's
task set; progress updates alone do not satisfy this requirement. Before launch,
verify asynchronous launch and completion handling as well as the standing
worker-launch preflight. If unavailable, report the runtime blocker. Do not
silently fall back to batches, agent CLIs or additional scheduling coordinators.
This procedure does not itself implement the missing runtime support.

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
wait for the other slots or a shared batch checkpoint. Integration is owned by
the orchestrator, outside the four analysis/audit slots; queued results are not
yet complete. Drain that queue as results arrive rather than deferring it until
all analyses finish. Audit clearance does not replace integration's publication
checks.

A held or failed system releases its slot once its evidence, blocker and unblock
condition are recorded. It does not prevent other eligible systems from running.
A suspected shared-method defect pauses affected work and requires a maintenance
decision.
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
No cleanup, push or method edits are commissioned.

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
