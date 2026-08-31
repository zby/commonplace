# Agent operability audit follow-through

Opened 2026-08-31 at the operator's request after reviewing the retained
[agent operability audit](../../reports/retained/agent-operability-audit-2026-08-31.md).
The audit is evidence and design synthesis, not authority to ship every
recommendation. This workshop tracks the bounded changes chosen from it and
the evidence needed to accept, revise, or reject each change.

## Intended result

Reduce the reconstruction work an agent must perform before it can identify,
execute, and verify ordinary Commonplace operations. Preserve correctness,
warrant, authored authority, and explicit mutation boundaries while reducing
irrelevant output, repeated discovery, and silent lifecycle drift.

The first program is deliberately narrow:

1. record a small before-change task baseline;
2. make `commonplace-validate` concise by default while retaining deliberate
   access to complete results;
3. add deterministic diagnostics for the lifecycle contradictions already
   observed in workshops and tasks;
4. reconcile the current contradictions after the diagnostics can detect
   them; and
5. evaluate a read-only status-view pilot that composes existing facts without
   becoming a scheduler or a new source of truth.

## Work tracker

### 0. Baseline

- [x] Define representative cold-start, validation-recovery, lifecycle-triage,
  and status-discovery cases.
- [x] Record correctness, output bytes, tool calls, retries, elapsed time, and
  operator decisions where the runtime exposes them.
- [x] Preserve enough input and command identity to repeat each case.

Recorded in [the pre-change baseline](./baseline-2026-08-31.md).

Acceptance: the baseline is small enough to rerun and distinguishes a quieter
interface from a merely different one.

### 1. Compact validation

- [x] Define the decision-ready default result: scope, counts, warnings,
  failures, and the next drill-down route.
- [x] Preserve the current per-artifact transcript behind an explicit detailed
  mode.
- [x] Add a stable structured result only after its fields and compatibility
  boundary are explicit.
- [x] Measure output reduction and confirm that no failure or warning becomes
  harder to inspect.

Acceptance: an agent can identify every failing or warning subject without
scanning passing artifacts, and can request the full evidence deliberately.

### 2. Lifecycle diagnostics

- [x] Detect a top-level workshop that is absent from the active-workshop
  index or lacks required framing.
- [x] Detect a completed checklist retained as a backlog task.
- [x] Detect a recurring task whose declared output or target is absent.
- [x] Give each diagnostic a stable identifier, subject, reason, and evidence
  path.
- [x] Add regression fixtures rather than depending on the live contradictions
  remaining present.

Acceptance: each dated baseline contradiction is reported mechanically and a
clean fixture passes.

### 3. Current-state reconciliation

Baseline observed 2026-08-31:

- [x] Classify the 18 top-level workshop directories absent from
  `kb/work/README.md`; register active work, close completed work, and preserve
  intentional workflow grouping without bulk-adding every directory.
- [x] Move or close the backlog task whose four subtasks are complete.
- [x] Repair, redirect, or retire the recurring explanatory-reach task's
  missing log target.
- [x] Reassess `semantic-search-replacement` against the current operational
  search path and either give it a live question or close it.
- [x] Confirm whether the absence of an active task artifact is healthy state
  or an undisclosed resume point.

Acceptance: every changed lifecycle position has an explicit reason, and the
new diagnostics no longer report the reconciled contradictions.

### 4. Read-only status pilot

- [x] Select only existing deterministic inputs needed to show Git state,
  validation failures, and lifecycle contradictions by default; keep review
  warnings, jobs, and freshness behind `--review` while that subsystem is not a
  regular operational surface.
- [x] Define a compact human view and a stable structured view with evidence
  drill-down.
- [x] Keep ranking deterministic and modest; do not invent action authority or
  infer semantic priority from age alone.
- [x] Compare the pilot with the cold-start baseline before deciding whether it
  should become a shipped `commonplace-status` command.

Acceptance: a cold-start agent finds the highest-priority current facts from
one small read-only result and can inspect their evidence without loading
unrelated rows.

The measurements, reconciliation decisions, and verification are recorded in
[the first-slice result](./result-2026-08-31.md).

## Boundary and deferred work

This workshop does not yet commission:

- the project-source manifest or three-way upgrade mechanism;
- a common inspect/plan/apply/receipt protocol across every command;
- operation-packet compilers;
- receipt retention or a governed learning-candidate queue;
- graph, full-text, or semantic retrieval infrastructure; or
- automated promotion, retirement, or semantic mutation.

Those changes require their own evidence, design decision, and authority. A
small implementation must not expose a generic framework incidentally merely
because a later recommendation could reuse it.

## Closure

Close this workshop when the baseline and four bounded work areas have each
been implemented and accepted, deliberately rejected, or transferred to a
named owner; the measured result and any shipped design decisions have been
extracted to their durable collections; and no unresolved item depends on this
README as its only state.
