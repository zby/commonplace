---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "kgai workflow account: edited coding task through optional side-model capture, validation, confirmation, retained decision and later recall."
run-id: AAS-2026-10-14-kgai-54bcae52e039-01
reviewed-boundary: "0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b"
---

# kgai workflow report

## Workflow account

### Selected workflow and evidence boundary

The selected workflow is a coding task followed by the optional kgai-mod end-of-turn capture check. It is representative of the shipped automatic trace-to-decision path, not of every kgai installation. It has an explicit model handoff, executable admission checks, an optional human decision, and a persistent result. The ordinary foreground capture path remains an alternative; this account does not splice its direct ingest into the mod's side-model sequence. The host owns the coding task and its tools; kgai owns the capture policy, mod orchestration and decision-memory engine. See [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture) and [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture).

All source evidence is SRC-1 at the frozen revision above. This is a source trace, not a successful execution trace. The implementation layer establishes the handoffs and gates; the doctrine/design layer establishes requested model behavior. No observed-run layer establishes that a model captured the right choice, that a user confirmed it, or that later coding depended on it. Host fork context selection and provider behavior remain external, as stated in [boundary](boundary.md#boundary-and-evidence).

### 1. Request, recall and coding

A user requests development work from the foreground host agent. The shipped skill requests recall before a nontrivial change through context, search and history, followed by respect or supersession of governing decisions. The agent supplies domain vocabulary and interprets the returned reasons; lexical retrieval does not independently establish that it has found every relevant decision. The agent then performs the requested coding work using host tools. These are requested foreground behaviors, not prerequisites enforced by the mod's end-of-turn eligibility test. SRC-1: `skills/knowledge-graph/SKILL.md`; supporting policy and lexical-limit passages: [RT-OBJ-knowledge-graph](runtime.md#rt-obj-knowledge-graph).

The mod counts successful Edit, Write, MultiEdit and NotebookEdit calls. Its Bash ingest detector excludes `--dry-run` and checks the host tool result's denial/error flags; invoking the decision skill can also mark a turn recorded. An eligible completion must be a foreground answer, contain a counted edit, lack a recording mark, and have a turn ID not already forked. Eligibility is therefore an event heuristic, not a semantic finding that a structural choice exists. A shell-only edit is outside this mod's edit counter. The existing route supplies the exact eligibility passage: [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture). SRC-1: `mods/kgai-mod/hooks/register.tsx`.

### 2. Code delegates capture to a side model

The mod, not the foreground model, schedules the capture check. When capture is active, it removes only the matching classic Stop capture nudge after underlying hooks run. Consequently the foreground turn is not continued by that nudge. On eligible completion it records the turn ID and clears the edit counter before attempting the check. Headless sessions await the check before returning from completion; drawn sessions schedule it beside the completed turn. The source makes this delivery distinction explicit:

> if ((await $.session.surfaces()).length === 0) {
>       await run()
>       return r
>     }
> --- `mods/kgai-mod/hooks/register.tsx`

> $.clock.after(0, () => {
>       void run()
>     })
>     return r
> --- `mods/kgai-mod/hooks/register.tsx`

The handoff calls the host's model-fork API with CAPTURE_PROMPT. It supplies structural DO/DON'T criteria, asks for NONE or ingest JSON, specifies rationale and mutations, requests exact reuse of session element names, and omits author. The host supplies the fork's session context; kgai does not specify its exact contents. The prompt says tools are unavailable and the answer is not shown to the user. That is a host contract and declared instruction, not locally verified isolation. See [RT-OBJ-capture-prompt](runtime.md#rt-obj-capture-prompt) and [RT-CMP-host-model](runtime.md#rt-cmp-host-model). SRC-1: `mods/kgai-mod/hooks/register.tsx`.

Only the parsed proposal crosses into engine admission. The side answer is not appended as a foreground transcript answer. UI compaction separately hides successful kgai result rows; it does not demonstrate removal of those results from the model's context. The delegation isolates a side question but provides no evidence of a host-wide context-compaction or subagent-management workflow.

### 3. Proposal parsing, validation and optional human veto

The side model selects structural relevance. The parser accepts a leading NONE, tolerates code fences, and otherwise requires parseable JSON containing titled decisions. NONE ends with a debug message and no decision ingest. An unanswered fork or invalid answer instead invokes failure reporting. These checks do not establish that the proposal describes the coding work truthfully. SRC-1: `mods/kgai-mod/hooks/register.tsx`; semantic-admission limits: [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture).

For a payload, the mod delegates name resolution and typed admission to the installed engine by passing JSON on stdin. Each process call has a 20-second timeout. The helper first dry-runs and then performs real ingest, stopping on a nonzero exit code. The dry-run and real ingest are separate process invocations, not a reserved transaction over a fixed store snapshot:

> for (const args of dryRunOnly ? [['ingest', '--dry-run']] : [['ingest', '--dry-run'], ['ingest']]) {
>     const out = await run(args, payload)
>     if (out.exitCode !== 0) {
>       return `kg ${args.join(' ')} exited ${out.exitCode}: ${(out.stdout || out.stderr).trim().slice(0, 300)}`
>     }
>   }
> --- `mods/kgai-mod/hooks/register.tsx`

The engine acquires and releases its store lock within each Ingest call. Dry-run builds decision events and returns resolved results without appending those events or applying their decision mutations. Real ingest must still succeed; intervening writes and real-write failures are not ruled out by prior validation. SRC-1: `src/internal/engine/engine.go`.

> if dryRun {
>             res.Decisions = append(res.Decisions, dr)
>             continue
>         }
> --- `src/internal/engine/engine.go`

In confirm mode on terminal/desktop surfaces, a successful initial dry-run produces pending UI state rather than a recorded decision. Record clears pending state and runs the helper again, including another dry-run; Skip clears it without ingest. A new prompt also clears pending state. The human veto therefore exists only on the supported confirmation surfaces. Confirm elsewhere follows automatic admission. The exact surface condition is retained in [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture). SRC-1: `mods/kgai-mod/hooks/register.tsx`.

The engine can reject schema and identity problems, but no reference answer or engineering-outcome oracle verifies the rationale. The side model proposes; software gates executable validity; supported confirm UI allows a human Record/Skip decision. In automatic mode no per-content human approval is required. This is task-driven extraction, not an experiment selecting an improved candidate against measured outcomes.

### 4. Persistence, return and later consumption

Accepted real ingest writes decision events to the local log before applying their effects to the graph, then commits the projection. The log retains rationale and mutations; graph authority and supersession determine current heads. A zero-exit helper result causes a recorded-title announcement. Headless surfaces receive a UI log; drawn surfaces receive a temporary status line. The mod uses process success rather than independently reading back the graph to verify delivery. An identical already-recorded decision can be an engine no-op, so an announcement need not mean a new event was appended. SRC-1: `src/internal/engine/engine.go`, `mods/kgai-mod/hooks/register.tsx`; append/projection evidence: [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture).

For this workflow, the foreground coding answer and capture delivery have separate completion boundaries. In a drawn session, the coding turn can finish before capture succeeds or fails. Pending confirmation is only a proposal. Successful ingest makes the decision eligible for later recall; the announcement reports that admission outcome. Later CLI context/history/search and editor replay provide consumer paths, not proof that a later agent respected the reason. Synchronization can distribute the events, but no successful exchange is necessary or established in this selected local workflow. See [RT-BAP-decision-recall](runtime.md#rt-bap-decision-recall), [RT-RTE-editor-read](runtime.md#rt-rte-editor-read) and [RT-RTE-team-sync](runtime.md#rt-rte-team-sync).

### 5. Rejection and recovery

A malformed side answer is a concrete rejection path: parseAnswer returns invalid, check calls fail, and no ingest follows. Dry-run rejection likewise prevents the helper's subsequent real-ingest call. Failure reports a debug diagnosis and at most one failure toast through the shared failure atom. The inspected mod supplies diagnostics, not an immediate retry or renewed foreground capture requirement. Because the turn ID is marked before the check, the same completion does not simply refork on failure. SRC-1: `mods/kgai-mod/hooks/register.tsx`.

> if (proposal.kind === 'invalid') {
>     return fail($, proposal.why)
>   }
> --- `mods/kgai-mod/hooks/register.tsx`

An error during real ingest is different: some events may already have reached the log. Append-before-projection failure names `kg rebuild` as the repair route, and batches are not all-or-nothing log transactions. The mod does not execute that repair itself. A caller must act on the diagnostic; durable acceptance cannot be inferred from a failed helper result, nor can total absence of writes. Later incorrect-but-accepted reasons require subsequent corrective/superseding decisions, not parser repair. See [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture). SRC-1: `src/internal/engine/engine.go`.

Added workflow inspection coverage: complete `mods/kgai-mod/hooks/register.tsx` for parsing, dispatch timing, pending UI, process admission and diagnostics; complete `skills/knowledge-graph/SKILL.md` for the task/recall/capture contract; and the Ingest function in `src/internal/engine/engine.go` for dry-run versus real-write progression and no-op behavior. These are implementation and doctrine/design evidence within SRC-1, not execution results.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-fork-capture](runtime.md#rt-rte-fork-capture)

Workflow completion: drawn foreground delivery precedes asynchronously scheduled capture; headless completion awaits the check. Pending confirmation is not persistence. Process-success announcement is the capture return, without an independent read-back verification. Rejection ownership: parser and engine reject; mod reports; supported UI permits human Skip. Recovery ownership: mod has no immediate repair loop in the inspected path; caller-driven correction or engine rebuild remains separate. Evidence and minimum passages appear in the workflow account, SRC-1: `mods/kgai-mod/hooks/register.tsx`, `src/internal/engine/engine.go`.

#### On [RT-RTE-foreground-capture](runtime.md#rt-rte-foreground-capture)

Workflow relationship: this is the alternative direct capture path and the source of the selected workflow's foreground recall contract, not a second mandatory capture stage. For the mod's real-ingest phase, append-before-projection and batch-prefix failure mean validation success is not an atomic delivery guarantee. The selected workflow does not establish model compliance, activation of retained rationale, or improved later action. SRC-1: `skills/knowledge-graph/SKILL.md`, `src/internal/engine/engine.go`.
