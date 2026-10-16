---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Halo workflow: desktop trace diagnosis, bounded child investigation, retained report and user-confirmed coding-tool handoff."
run-id: AAS-2026-10-14-halo-c4ed89d7f99f-01
reviewed-boundary: b7f8509745d67b499b4e80efe20ea37c03426a74
---

# Halo workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is a desktop user's diagnostic question over selected stored traces, followed by a retained report and optional handoff to a coding tool. It was selected because the shipped caller connects trace selection, engine delegation, durable answer retention and delivery in one path. Child investigation is a model-selected branch, not a mandatory stage. The delivered Halo product is diagnostic text and its report, not an applied or deployed harness change. This follows the partial-loop boundary and [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis), [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call) and [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff).

Evidence is implementation and doctrine/design in SRC-1 at the frozen commit. Additional inspection covered the queue's export, bridge-event and follow-up branches; complete desktop Python bridge and report renderer; child construction and failure-result branches; the report preparation endpoint; coding-tool UI and link builder; and the skill's five-step improvement procedure. Anchors are `app/src/server/halo/runQueue.ts`, `app/scripts/halo-local-runner.py`, `app/src/server/halo/report.ts`, `engine/tools/subagent_tool_factory.py`, `app/src/server/router.ts`, `app/src/mainview/halo/OpenInToolBar.tsx`, `app/src/desktop/commands.ts` and `skills/claude/SKILL.md`. No execution trace was inspected and no target was executed. The account establishes source wiring, not exercised delegation, successful diagnosis or improved harness performance.

### 1. Request admission and host-to-engine handoff

The user supplies a question, target/filters and model/resource choices. The desktop queue owns scheduling and readiness, not the analysis model. It checks for an installed/importable engine, can request installation, exports matching stored telemetry to JSONL, and supplies the Python bridge with the trace path, conversation messages, provider settings and depth/parallel/turn limits. Engine installation is a separate machinery-admission route, [RT-RTE-engine-install](runtime.md#rt-rte-engine-install); importability does not verify diagnostic behavior. These responsibilities belong to the shipped desktop rather than an excluded external host (SRC-1, `app/src/server/halo/runQueue.ts`, `app/scripts/halo-local-runner.py`).

An empty export is a concrete rejection before analysis: code marks the run and active assistant turn failed and returns without launching the bridge. It rejects unavailable matching input, not a bad diagnostic answer (SRC-1, `app/src/server/halo/runQueue.ts`).

> if (exported.spanCount === 0 || exported.traceCount === 0) {
> --- `app/src/server/halo/runQueue.ts`

> errorMessage: "No traces matched the selected HALO filters.",
> --- `app/src/server/halo/runQueue.ts`

The bridge converts configuration into root/subagent model bindings and engine messages. Its desktop configuration does not grant repository access or enable checkpoints. Thus the optional code/Git route available to other callers must not be silently joined to this workflow. The root receives engine guidance and caller messages over the exported trace store, as established by [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis) and [RT-RTE-repository-inspection](runtime.md#rt-rte-repository-inspection) (SRC-1, `app/scripts/halo-local-runner.py`).

### 2. Model-selected investigation and child return

The root model decides which trace questions to investigate, whether to delegate, and what conclusion to produce. Prompt guidance prefers focused subagent work; the root still has leaf tools, so delegation is policy rather than enforced division of labor. The contrast and its retained evidence are [RT-CLM-delegation-policy](runtime.md#rt-clm-delegation-policy).

If the root calls a child, it supplies a focused input string. Code validates the tool arguments, checks depth, obtains a per-depth semaphore and allocates a child identity linked to the parent and tool call. The child starts with its own system prompt and delegated input, sharing trace access and configured provider but not the parent's accumulated conversation. It chooses its own investigation tools. The parent receives JSON carrying an answer, child identity, sequence bounds and usage counters; the host sees interleaved events. This is the fresh-work-context mechanism in [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call), not an independent persistent child conversation (SRC-1, `engine/tools/subagent_tool_factory.py`).

There is no distinct verifier that certifies the child's answer before the root receives it. Exhausted retries and ordinary child exceptions are returned through the same result shape as answer text. The parent model can respond to that failure text, but code does not guarantee replacement investigation. The inspected exception branch makes recovery ownership explicit (SRC-1, `engine/tools/subagent_tool_factory.py`):

> return _failure_result(child_execution, f"Subagent exhausted retries: {exc}")
> --- `engine/tools/subagent_tool_factory.py`

Root direct investigation and optional trace synthesis remain alternate branches. Synthesis receives reduced rendered trace metadata, not the child's or root's full transcript; oversized/truncated inputs qualify completeness. These limits are retained in [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis). No fixed ordered plan, universal answer oracle or child-result correctness gate is established by this workflow.

### 3. Finalization, retention and report delivery

The root is intended to terminate through `final_answer`. Engine retries and a bounded final-answer reprompt are best-effort recovery, not a whole-run budget or an exactly-once effect guarantee; see [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis). Desktop completion has a weaker acceptance predicate: the bridge prefers a final-flagged assistant answer but otherwise accepts the last assistant item, without restricting fallback to the root. A non-empty selection yields `completed`. This is a text-presence check, not verification of root finalization or truth, as quoted in [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis).

On a terminal completed/incomplete event, the queue writes a result file, updates the run and assistant turn, publishes state and attempts report materialization. A report-write exception does not undo the retained answer; the UI can request materialization later. The new part record [WF-RTE-report-materialization](#wf-rte-report-materialization) establishes the exact transformation: the file contains run metadata and selected conversation exchanges, not all emitted agent/tool activity. These are separate delivery milestones: persisted answer, report file, and external prompt initiation (SRC-1, `app/src/server/halo/runQueue.ts`, `app/src/server/halo/report.ts`).

### 4. Rejection, recovery and consequential user choice

The user can cancel a run; queue cancellation kills the bridge through its abort signal. Bridge exceptions emit failure, and the queue records failure rather than admitting an answer. The service exposes retry and follow-up; a follow-up is admitted only after a terminal state and re-enqueues new turns. It reuses the original export when that file exists, otherwise exports again. Prior user/non-empty assistant turns enter the next request, not full child/tool histories. Thus a sharper user question can change the next investigation, while the software does not guarantee that retry resolves the failure (SRC-1, `app/src/server/halo/runQueue.ts`; [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)).

On the handoff path, the UI first requests a report, then opens a path-bearing deep link or copies the path-bearing prompt. Failure to prepare/open produces a UI error; a successful open is described to the user as prefilled, requiring confirmation. The receiving tool must access the local report. Link success does not establish that the actor read it or edited anything (SRC-1, `app/src/mainview/halo/OpenInToolBar.tsx`, `app/src/desktop/commands.ts`; [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff)).

> description: "The prompt is prefilled — confirm it inside the tool.",
> --- `app/src/mainview/halo/OpenInToolBar.tsx`

The shipped improvement skill prescribes baseline evaluation, trace diagnosis, checking claims against the actual repository, a minimal hypothesis-driven edit and remeasurement. It explicitly treats an invented file path as grounds to re-search by concept rather than act on the guessed path. These are downstream coding-actor instructions, not an implemented Halo answer gate. Its blanket claim that the engine cannot see code is stale relative to optional repository tooling, though it matches this desktop bridge's lack of a repo grant. The distinction is retained in [RT-CLM-trace-only](runtime.md#rt-clm-trace-only) (SRC-1, `skills/claude/SKILL.md`, `app/scripts/halo-local-runner.py`).

The proposed ship-or-return-to-diagnosis decision compares evaluation delta and error-pattern frequency; the prescribed rejection path returns to diagnosis with a sharper question. [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) retains that passage and separately scopes the theory conditions and improvement-attribution limits. Evaluation execution, patch admission/rollback, deployment and later production behavior depend on the external harness and coding tool. The desktop request does not itself establish that the receiving actor loads the skill. Halo delivers an improvement input; the frozen source does not close the external improvement loop.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-report-materialization
Label: Desktop report materialization

Part of: [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)

This is the report-preparation subroute of the desktop container, not a duplicate of its full analysis invocation. Retained run/turns → final-answer eligibility and file freshness checks → Markdown rendering/file write → artifact registration and returned path. Code owns selection, rendering and retention; no model or human reviews the report content at this step. It also supplies the local file required by the distinct external [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff). Evidence: SRC-1, `app/src/server/halo/report.ts`, `app/src/server/halo/runQueue.ts`, `app/src/server/router.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Report path and size with an artifact row; null if no non-empty final answer exists. The preparation endpoint rejects null with a no-final-answer error.
- Later read-back: File can be read by the receiving coding tool after a path-bearing prompt; actual reading is uninspected. Re-materialization reads retained run and conversation turns.
- Delegated visibility: Markdown includes run metadata and user turns plus non-empty completed/incomplete answer turns, not the full engine event stream or child tool transcripts.
- Selection predicate: Run ID selects stored state; non-empty finalAnswer permits preparation; missing file or file older than run.updatedAt triggers rewrite; turn role/status/content select exchanges.
- Invalidation or expiry: Missing/stale file is rewritten at the same report path; queue catches materialization failure and permits later UI preparation. This branch supplies no versioned report rollback.
- Activation or effect: Writes model-authored findings and user questions to a local Markdown artifact by software rule, with no per-content approval. External behavioral reliance is uninspected.
- Evidence limits: File presence/freshness do not establish truth, root-final-answer provenance, receiving-tool access, or successful harness changes. Rendering is implementation evidence, not an observed delivery.

The trigger is terminal answer handling or explicit report preparation. The proposed product is a rendered conversation report; the admission gate is answer presence, not correctness. Automatic preparation and a human UI request share the same content-selection rule. The endpoint can reject preparation without an eligible answer. The report has natural-language findings and question text, with code-generated metadata; it persists on disk while symbolic artifact metadata persists in SQLite (SRC-1, `app/src/server/halo/report.ts`, `app/src/server/router.ts`).

> if (!run || !run.finalAnswer?.trim()) return null;
> --- `app/src/server/halo/report.ts`

> const stale =
>   !existing ||
>   (Number.isFinite(runUpdatedMs) && existing.mtimeMs < runUpdatedMs);
> --- `app/src/server/halo/report.ts`

> turn.role === "user" ||
> ((turn.status === "completed" || turn.status === "incomplete") &&
>   turn.content.trim().length > 0),
> --- `app/src/server/halo/report.ts`

> try {
>   ensureHaloReportFile(input.database, input.run.id);
> } catch {
>   // The report can still be materialized on demand from the UI.
> }
> --- `app/src/server/halo/runQueue.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call)

Workflow role: Optional focused investigation delegated by the root, not a required stage. Parent owns interpreting the returned answer or recoverable failure and deciding whether further work is needed. The depth/semaphore gate admits execution, not diagnostic correctness; it does not certify a child result before parent synthesis.

#### On [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis)

Workflow acceptance: Empty-export rejection precedes analysis. Bridge text-presence completion and report materialization are later, separate milestones. Follow-up/retry are host-owned recovery requests, not an engine-owned guarantee of resolving the previous diagnosis or execution failure.

#### On [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff)

Workflow delivery boundary: Halo supplies a local report path in a prefilled request. User confirmation controls initiation in the receiving tool; downstream claim verification, editing, evaluation and shipping remain external responsibilities. The shipped skill prescribes those stages but the desktop link does not establish skill loading or completed execution.
