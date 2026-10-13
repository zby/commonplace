# Rerun the previously analysed agentic systems

## Commission

The operator commissioned this workshop on 2026-10-12 to rerun all systems
analysed under the previous analysis system. Produce fresh, source-grounded
coverage through the current
[`analyse-agentic-system` workflow](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md),
not conversions of old reviews. Success means published, independently audited
and integrated analyses for the checklist, with consequential limits visible
and unresolved targets honestly blocked.

**Current rolling window: two system pipelines.** The operator reduced it
from four on 2026-10-13. Each slot holds one analysis followed by its fresh audit;
refill the slot after audit disposition without waiting for the other pipeline.
Internal analytical-worker scheduling remains unchanged. This reduction may
reduce provider pressure; it does not establish concurrency as the cause of
the recorded failures.

**Dispatch is released.** The next orchestrator may start fresh eligible work
after ownership reconciliation and runtime preflight, without asking for another
release or imposing a separate provider-availability gate. Individual holds
remain separate. This README is the current handoff; editing it launches no
runs. The [archived log](./archived-log.md) retains the superseded accumulated
handoff, historical restart instructions and checkpoint counts. Read it only
when a specific historical question requires it, not as another startup gate.

Choose target order and execution details within the boundaries below. Recovery
of held runs, other method changes, comparison regeneration, public landscape
synthesis, run cleanup and push remain separate commissions. The resolved
validation-path maintenance retains only its bounded authority below.

## Current execution checkpoint and next action

[Rolling execution 09](./rolling-09.md) has drained all four launched pipelines.
cass_memory_system and claude-obsidian are published, independently audited and
integrated with recorded limits. Autogenesis stopped before publication;
Claude Context Guard's coordinator failed after a discoverable publication.
Both remain held pending supported reconciliation/recovery; publication alone
does not clear the latter. All worktrees, outputs and available traces remain
preserved. The audits do not certify individual worker validation calls where
tool traces were not located.

**Corpus: 19 complete, 167 pending, 20 held. No active assignments or integration
backlog remain. Queue ownership is released.** The session drained for
retained-context capacity, not a new operator stop or shared provider pause.
A session-local job check found no active or retained jobs; this does not
release another owner's reserved target. Standing fresh dispatch remains
released after ownership reconciliation and runtime preflight.

To start the next execution:

1. Read [systems](./systems.md) and the latest execution checkpoint, currently
   [rolling-09](./rolling-09.md). Check for newer assignments and establish queue
   ownership. Do not duplicate a publication destination or assume process
   existence alone assigns this queue. Escalate unresolved ownership.
2. Verify the selected model and effort, loaded asynchronous tool schema and
   standing worker-launch diagnostic before opening workflows. Follow the
   runtime requirements below; a failure stops launch, not evidence preservation.
3. Select **two eligible pending targets**, resolving identity and source input
   from their historical identity references without forwarding old findings.
   Exclude the holds and older refresh reservations below. Record assignments
   durably in the next rolling execution record and checklist.
4. Prepare each isolated worktree from a committed method through the standard
   skill, then launch one fresh per-system coordinator in each slot. Carry the
   source-only commission, command prefix, ownership boundaries and approved
   project-agent launch settings in each handoff. Explicitly authorize the
   driver's bounded transient-worker retries in that commission; do not repeat
   the old unconditional stop-on-worker-failure instruction. The coordinator
   performs its own required preflight and uses harness `pi`, profile `pi-sol`.
5. Follow the rolling analysis–audit–integration loop below. Record each outcome
   as it arrives. Preserve failures, release their slots and continue eligible
   work unless evidence establishes a shared blocker.

Do not replay historical stops or release decisions from the archive. Fresh
dispatch does not authorize recovery, automatic retry or fresh replacement of
held targets. Partial progress is useful; it is not a completed corpus refresh.

## Holds and reservations

[Systems](./systems.md) records each held target's run, evidence and unblock
conditions. All 20 remain incomplete:

- Eight prior holds: Agent Skills for Context Engineering, ACE, AI-Context-OS,
  ai-memex-cli, Archie, arsumbris, Auto-claude-code-research-in-sleep and
  auto-harness.
- Ten rolling-08 holds: Autocontext, AutoSci, Binder, browzy.ai, Beever Atlas,
  Apache Maka, Amazon Science SAGE, AREX-Skill, byterover-cli and Agentic Harness
  Engineering.
- Two rolling-09 holds: Autogenesis and Claude Context Guard. The latter has a
  discoverable publication but no audit/integration clearance after its
  coordinator's terminal stream failure.

Agent Skills for Context Engineering remains reserved to its reported owner
until completion, termination or explicit handoff is confirmed. Do not access
potentially changing evidence without coordinating with that owner. ACE retains
an unsettled reconciliation attempt; recovery requires prior-worker status and
a supported operator decision. Agentic Harness Engineering's latest profile
refusal must also be resolved before publication; installed members alone are
not clearance.

Older [agentic-memory-refresh](../agentic-memory-refresh/README.md) reservations
remain excluded from fresh assignment until their owners release them: Agent-S,
MemoryOS, Basic Memory, OS-Copilot, A-mem and HippoRAG. Legacy-engine completion
does not count here; preserve that workshop's history.

Academic Research Skills is **pending**, not held, following the
[partial-outcome disposition](./partial-outcomes-2026-10-13.md). Its earlier
source-exposure problem remains a constraint: a fresh run must resolve exposure
and respect source isolation before proceeding. Target release does not waive
that rule or authorize resuming the old run. Do not silently lift a hold or
infer target eligibility from an empty job registry.

## Population

[Systems](./systems.md) is the scheduling authority: **206 targets from 223
analysis records**, initially drawn from 155 legacy implementation-grounded
reviews, seven lightweight reviews, 12 authored accounts, 43 generated historical
reviews and six current-engine sets already counted complete by operator
direction. The six retain their recorded limits and prior audits; do not reopen
them. Use the checklist for current progress.

Repeated reviews of the same named system share a row. Dated Instinctual Memory
reviews are grouped, and `gbrain-garrytan` is grouped with GBrain. Four
`.replaced.` predecessor files are excluded as extra targets. Paper-only
WikiSkill and the independent Stahl-G implementation stay separate, as do the
two SAGE systems and the LLM Wiki variants.

This is an inventory, not a verified count of upstream repositories. Resolve
identity and scope before assignment; record justified splits or merges rather
than silently dropping coverage. Historical links establish inclusion and help
resolve identity, not fresh findings. Unreviewed TODOs, ingests alone and
workshop trials are not extra targets.

## Execution and ownership

The operator authorizes **instruction-level bounded transient-worker recovery**
for fresh runs prepared from the committed method containing this advice. The
[run driver](../../agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md#retry-transient-worker-failures-when-authorized)
owns the rule. Carry this explicit permission in each per-system coordinator
handoff; the coordinator must read and follow that driver. A transient analyst
request failure need not discard completed analytical work, but retry never
waives source isolation, engine bounds or validation. No new retry tooling or
orchestrator-restart mechanism is commissioned.

This recovery advice applies only to the **per-system coordinator that launches
analysts** (`commonplace-coordinator`), not to the outer workshop coordinator.
If the per-system coordinator itself fails, the outer coordinator records its
terminal error, reconciles the run read-only, preserves evidence, holds the
target and refills the slot with the next eligible analysis. It does not restart
the failed coordinator. All 20 existing holds remain unchanged; this permission
is not retroactive recovery or replacement authority for them.

Use `openai/gpt-6.1-sol`, medium thinking, for the orchestrator, fresh per-system
coordinators and fresh auditors; analytical workers use `pi-sol`. Keep **two
system pipelines active while eligible work remains**, unless a blocker requires
a pause or the session must drain safely for context capacity. Two limits the
analysis/audit pipelines, not their internal analytical workers. Do not change
the standard skill's internal rounds to implement this outer-window reduction.

Launch one fresh `commonplace-coordinator` per system through `subagent`, with
`agentScope: "project"` and `cwd` set to the prepared isolated worktree.
Do not assign a whole analysis to `commonplace-worker`. Each coordinator follows
the standard skill and delegates its exact code-scheduled jobs to fresh
`commonplace-worker` contexts. Analysis coordinators and workers must not receive
legacy findings, comparison values, previous results or maintenance conclusions.
Only the subsequent auditor may compare old and new findings. Preserve the
skill's frozen-source and isolation rules.

The operator approves project-local `commonplace-coordinator` and
`commonplace-worker` definitions in isolated worktrees prepared by the standard
Commonplace setup from the selected committed method for this commission.
Set `agentScope: "project"` and that worktree's `cwd` for these launches.
The current Pi subagent extension has no separate destination-approval gate.
Carry the approved destination boundary in coordinator handoffs so they can
launch their workers without reading this workshop.
Approval does not extend to arbitrary directories, modified definitions outside
the selected method or agent definitions in external source repositories.
Obtain operator approval for destinations outside this commission's boundary;
removing the runtime gate does not expand the commission.

Verify that the loaded schema exposes `action` and `handles`, and complete the
standing worker-launch diagnostic before launch. An older schema requires
`/reload` before starting any job; asynchronous unavailability is a runtime
blocker. Use `action: "start"` for each coordinator and `action: "wait"` with
active handles to receive one completion. Remove the completed handle before
waiting again. Record assignments and results before forgetting terminal
handles. Do not substitute wait-for-all parallel calls, agent CLIs or extra
scheduling coordinators. See [Pi rolling dispatch](../../../.pi/README.md#rolling-dispatch)
for lifecycle limits. Reload and orderly shutdown cancel active jobs; reconcile
interrupted assignments before replacement. Do not finish a session with jobs
still pending; drain and leave a recoverable checkpoint.

The orchestrator owns scheduling, checklist updates, recovery coordination and
serial integration into `main`. Per-system coordinators own their isolated runs
and return without integrating. Auditors own distinct reports under `audits/`,
not analysis outputs or shared bookkeeping. No two active runs may own the same
publication destination. Existing runs keep their frozen method and evidence;
this handoff does not authorize rewriting or discarding them.

After each publication, launch a fresh auditor in that slot under
[Audit a rerun before integration](./audit-a-rerun.md), while the other pipeline
continues. The auditor receives the target/run, prepared worktree and command
environment, frozen source boundary, new publication, historical accounts,
available trace evidence and owned report path. After disposition, queue a
cleared result for serial integration and refill the slot with eligible work.
Do not wait for both slots to complete. Integration is outside the two slots;
drain its queue as results arrive. Audit clearance does not replace integration's
publication checks. Use the prepared worktree's command environment for
`commonplace-analysis integrate`, with the agent model as required by the skill;
do not copy publications into `main`.

A held or failed target releases its slot once evidence, blocker and unblock
condition are recorded. It does not block other eligible work. Stop on uncertain
effects or unresolved ownership; do not fabricate completion, repair accepted
outputs independently or silently broaden scope. A suspected shared-method
defect pauses affected work and requires a maintenance decision. A different
shared defect from the resolved validation-path issue needs separate authority.

Preparation permits unrelated uncommitted origin changes by default, excludes
their bytes and records their exclusion. Startup inputs must match the selected
commit; `--require-clean-origin` requests strict preparation. Integration requires
a clean origin on `main`. Coordinate shared writes and commit owned audit and
checklist bookkeeping at each integration boundary. Resolve unrelated dirty
files with their owner; this commission does not authorize staging them.
Preserve worktrees and traces. Handoff-document cleanup does not authorize run
cleanup, evidence deletion or push.

## Bounded validation-path maintenance

**Resolved; not startup work.** The
[maintenance decision](./validation-path-maintenance.md) attributes inspected
path failures to worker transcription, not supplied invocations, and lifts the
shared pause for fresh work. `commonplace-run validate-output <prompt-path>`
was implemented in `9b110e2f5`; prepare fresh runs from a committed method that
contains it. Workers use the generated invocation's command for immediate
write–check–repair feedback; workflow-side validation remains unchanged.
Do not repeat the investigation or certify historical drafts from publication
success alone.

Reopen this bounded investigation only if new validation-path evidence
contradicts the retained decision. Authority remains limited to inspecting exact
handouts, tool calls and returned results, distinguishing producer defects from
worker transcription or unsupported substitution, and making the minimum
necessary current-producer, instruction or path-handling correction with
regression tests. Follow repository test selection, including affected analysis
suites and relevant slow tests. Do not weaken validation or source isolation.
Use the [batch-03 evidence](./batch-03.md), [AgeMem audit](./audits/batch-03-agemem.md)
and [Agent-R audit](./audits/batch-03-agent-r.md) as locators when needed; coordinate
before accessing Agent Skills' changing evidence. Never reconstruct an absent
result as an executed check.

Record exact evidence, diagnosis, affected scope, correction commit, checks and
an explicit lift-or-retain disposition in a workshop maintenance decision.
Commit owned corrections before preparing new runs. Never edit frozen methods,
state, outputs or traces. Missing evidence keeps the affected scope paused;
escalate broader method/acceptance changes. Maintenance release does not resolve
individual recovery holds or override a subsequent operator stop.

## Progress and checkpoints

Keep assignments traceable to run identifiers and frozen source boundaries.
Mark a target complete only after publication, audit clearance and verified
integration; link overview, audit and integration commit in the checklist.
Work awaiting audit or integration is not complete. Failed and local
blocked/out-of-scope outcomes stay incomplete unless the operator approves
exclusion. Report consequential findings, worker problems and blockers as they
arrive. Keep ownership, handle maps and integration queues recoverable across
interruption. When draining a session, settle all launched jobs, record evidence
and release queue ownership explicitly; do not turn a context-capacity drain
into a new dispatch hold.

The [report statistics script](../../../scripts/agentic_system_rerun_stats.py)
and its [documentation](../../../scripts/README.md#agentic-analysis-rerun-statistics)
provide an optional cheap inventory. It is not a source audit, publication check
or completion count; reportless failures are invisible. Do not make it another
startup gate.

## Closure

The workshop closes when every target has an audited, integrated analysis or
an explicit operator-approved exclusion, and no running assignment remains.
Retain durable operational lessons in the appropriate library collection before
removing this temporary workshop and its Active Workshops entry. Accepted
analysis sets remain the durable outputs.
