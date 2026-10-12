# Rerun the previously analysed agentic systems

## Commission

The operator commissioned this workshop on 2026-10-12 to rerun all systems
analysed under the previous analysis system. Produce fresh, source-grounded
coverage through the current
[`analyse-agentic-system` workflow](../../agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md),
not conversions of old reviews. The operator subsequently selected batches of
four parallel system pipelines, each with a quick independent audit before
integration. This document is the handoff; revising it does not launch runs.

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

Use `openai/gpt-6.1-sol`, medium thinking, for the batch coordinator, fresh
per-system coordinators and fresh auditors; analytical workers use `pi-sol`.
Keep at most **four system pipelines active**, where a pipeline includes analysis
and its audit. Each analysis follows the standard skill in its own worktree;
its internal worker scheduling remains unchanged. Verify runtime support using
the standing launch rules rather than assuming nested delegation works.

The batch coordinator owns assignments, checklist updates, recovery decisions
and serial integration into `main`. Per-system coordinators own their isolated
runs and return results without integrating. Auditors own distinct reports
under `audits/`, not analysis outputs or shared bookkeeping. No two active runs
may own the same publication destination.

Keep analyses source-first: do not supply legacy findings, comparison values or
previous results to analysis coordinators or workers. The batch coordinator may
use historical records for identity; only the subsequent auditor may compare
old and new findings. Preserve the skill's frozen-source and isolation rules.

After each new publication, commission a fresh auditor under
[Audit a rerun before integration](./audit-a-rerun.md). An audit may overlap the
other systems' analyses. Reconcile all pipeline outcomes in the batch, integrate
cleared results serially through the standard route, and commit owned bookkeeping
before starting the next batch. Audit clearance does not replace integration's
publication checks.

A held system need not prevent integrating its cleared peers or proceeding to
another batch once its blocker and unblock condition are recorded. A suspected
shared-method defect pauses affected work and requires a maintenance decision.
Do not repair accepted content outside a supported workflow or quietly broaden
the commission to work around a blocker.

Preparation permits unrelated uncommitted origin changes by default, excludes
their bytes, and records their exclusion; startup instructions and configuration
must still match the selected commit. `--require-clean-origin` requests strict
preparation. Integration still requires a clean origin on `main`. Resolve
pre-existing uncommitted work with its owner before integration; this commission
does not authorize staging unrelated files. Preserve run worktrees and traces.
No cleanup, push or method edits are commissioned.

## Progress and checkpoints

Keep each checklist assignment traceable to its run and frozen source boundary.
For new runs, check a target complete only after publication, audit clearance
and verified integration; link its overview, audit and integration commit.
Distinguish work awaiting audit or integration from completed work. Failures and
local blocked/out-of-scope results remain incomplete unless the operator
explicitly approves exclusion.

At each batch boundary, report outcomes, consequential audit findings, worker
problems and unresolved blockers. Choose the next batch of up to four eligible targets.
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
