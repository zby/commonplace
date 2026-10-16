---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "SoL-Pi workflow: Codex prompt-hook delegation through detached Pi work, result classification, parent review and return."
run-id: AAS-2026-10-14-sol-pi-42f04fbbc6bb-01
reviewed-boundary: "41fa7e0e230bedc5e639aed2e7b9cc5698726db1"
---

# SoL-Pi workflow report

## Workflow account

### Selected path and evidence

The representative workflow is a user handing a coding task to SoL-Pi from Codex with `$sol-pi`, followed by a detached Pi run and a return to the parent. It is selected because the repository ships the request recognizer, context exporter, launcher, durable result reader and notification formatter as one connected path. This is the Skill example, not automatic behavior of the default extension entry. Its identity is already declared by [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff); the workflow adds a delivery/verification account rather than duplicating that route.

The [boundary](boundary.md) supplies SRC-1. Additional inspection for this account covered `examples/sol-pi-skill/bin/sol-pi-run` functions from `summarize` through `cmd_hook_notify`, the full `examples/sol-pi-skill/bin/sol-pi-context`, `examples/sol-pi-skill/codex-hooks/hooks.json` and `examples/sol-pi-skill/codex-skill/sol-pi/SKILL.md`. These supply implementation and doctrine/design evidence. No target, evaluator or host hook was executed. Successful host delivery, verification and task completion remain unobserved.

### Request and delegated context

The shipped Codex hook configuration attaches synchronous `hook submit` and asynchronous `hook notify` to `UserPromptSubmit`. Submit recognizes the command prefix, separates leading model/effort options from the task, and selects the event's working directory. Non-handoff requests pass through. An empty task produces a blocking usage reply without starting work. A recognized task is written to a task file and passed to `start`; when an existing transcript path is supplied, the launch also requests exported session context. The hook writes a correlation record containing the resulting run id or startup error and returns a blocking handoff/start-failure message. Thus the hook's dispatch decision is software parsing of an explicit user request, not a model deciding whether to delegate (SRC-1, `examples/sol-pi-skill/codex-hooks/hooks.json`, `examples/sol-pi-skill/bin/sol-pi-run`).

> if block:
>     out['decision'] = 'block'
> --- `examples/sol-pi-skill/bin/sol-pi-run`

Context export is not full conversation sharing. The Codex parser begins at the latest compaction, uses replacement history or its summary where available, and selects user/assistant text and tool call/result representations. It filters instruction/noise messages, trims tool output, drops the in-flight handoff and later events, and retains recent rendered blocks under a character budget. The latest block can exceed that budget; header text is additional. The delegate receives this reference prefix followed by task text. It is told to reread files before relying on commands from the parent's environment. Export failure stops the launch rather than silently inventing context (SRC-1, `examples/sol-pi-skill/bin/sol-pi-context`, `examples/sol-pi-skill/bin/sol-pi-run`).

> 'so far, exported as reference. Tool calls are shown as one-line summaries and long outputs are trimmed. '
> 'The commands ran in the other agent\'s environment: re-read files before relying on them, and do not '
> 'repeat work that is already done.',
> --- `examples/sol-pi-skill/bin/sol-pi-context`

### Worker execution and coordination

`start` generates a run id, saves the task, launches a detached Python `run` invocation and records its launcher pid. `run_task` allocates a Pi session id/directory, saves the complete prompt and launch metadata, and starts Pi with JSON events directed to `events.jsonl` and stderr to a separate file. The subprocess runs in the selected shared working directory. The runtime baseline establishes separate agent configuration and enabled mechanisms, but also the `--no-approve` launch and lack of OS isolation ([RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff)). Workspace edits escape immediately, before any final-answer return or parent review.

Pi and its foreground model own the inner task's action sequence. The launcher does not decompose the task into checked subtasks. A worker can use the fused mutation/command, diagnostic reduction, observation recall and plan-boundary compaction mechanisms described in [RT-RTE-action-fusion](runtime.md#rt-rte-action-fusion), [RT-RTE-reducer-receipt](runtime.md#rt-rte-reducer-receipt), [RT-RTE-observation-replay](runtime.md#rt-rte-observation-replay) and [RT-RTE-online-compaction](runtime.md#rt-rte-online-compaction). Enabling them does not establish that this particular delegated task uses all four. There is no supplied trajectory demonstrating a successful inner repair/test cycle.

`run_state` reads a finished `result.json` first. Otherwise it uses launcher/run pids and recent event-file activity to classify the run as running or lost and derives a partial summary. Notify waits for the correlated submit record, then polls state until it is not running. `wait` similarly polls; its own deadline returns code 3 without killing the worker. This is distinct from the worker's execution timeout (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

### Acceptance is process classification, not task verification

After process termination, `summarize` scans events and session entries. It accumulates usage and mechanism counters and retains the last nonblank assistant text as `final`. That text need not be a verified final report. The classifier treats a zero exit with no error/aborted stop reason as done; it can classify such a process as done even without substantive final text. It does not compare changed files with an expected answer, rerun tests, or judge the worker's explanation (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

> status = 'done' if rc == 0 and stop not in ('error', 'aborted') else ('timeout' if rc == -9 else 'failed')
> --- `examples/sol-pi-skill/bin/sol-pi-run`

The parent-facing hook report asks the parent to check changes before relying on them. It includes current Git status/diff statistics where obtainable, not the complete patch or a clean pre-run baseline. Consequently this is a review prompt, not automatic attribution of every working-tree change to the delegate. There is no reference-answer oracle or per-change human approval in the launcher. Parent review can reject reliance on the result but does not prevent already executed filesystem changes (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

> 'in this working directory). Check the changes below before relying on them, then tell the user '
> 'what SoL-Pi did, whether it verified the result, and the cost line.',
> --- `examples/sol-pi-skill/bin/sol-pi-run`

### Failure, recovery and delivery

On execution timeout the launcher sends TERM to the Pi process group, waits up to twenty seconds, and sends KILL if needed; it classifies the result with `rc = -9`. It retains completed edits and available event/session artifacts rather than rolling back. Startup failure is reported by submit; a missing submit record causes notify to return without a report after its wait. A lost run is terminal for notify's polling, not evidence of successful completion. These are inspected control branches, not exercised recoveries (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

> except subprocess.TimeoutExpired:
>     os.killpg(proc.pid, signal.SIGTERM)
>     try:
>         proc.wait(timeout=20)
>     except subprocess.TimeoutExpired:
>         os.killpg(proc.pid, signal.SIGKILL)
>     rc = -9
> --- `examples/sol-pi-skill/bin/sol-pi-run`

The bundled skill supplies a model-mediated fallback when hooks did not run. It tells the parent not to work on the task concurrently, to inspect changes afterwards, and to report a wrong result rather than repair it or launch a reworded task. Separately, it advises rerunning provider 429/503 failures. These are instructions to the parent, not an automatic retry loop or enforced nonconcurrency (SRC-1, `examples/sol-pi-skill/codex-skill/sol-pi/SKILL.md`).

> 5. If the result looks wrong, report that and what you saw; do not fix it
>    yourself or start another run with a reworded task. If SoL-Pi seems to have
>    had the wrong context, run `sol-pi-context | head -20` and report which
>    session it exported.
> --- `examples/sol-pi-skill/codex-skill/sol-pi/SKILL.md`

Delivery has two boundaries. First, the launcher writes `result.json`, making the status, final text and artifact pointers readable through CLI commands. Second, Codex notify emits host-specific JSON with `additionalContext`; the host is expected to deliver it on a subsequent turn. The report trims final text to 4000 characters and includes a full-result command pointer when truncated. The parent receives status/cost, selected working-tree information and final text, not the complete inner transcript. It must still report the outcome to the user. Host consumption and parent compliance are external/unobserved, so writing the result and emitting JSON are wired delivery steps, not evidence that the user received a correct result (SRC-1, `examples/sol-pi-skill/bin/sol-pi-run`).

> print(json.dumps({'hookSpecificOutput': {'hookEventName': event.get('hook_event_name'),
>                                          'additionalContext': report}}))
> --- `examples/sol-pi-skill/bin/sol-pi-run`

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

#### On [RT-RTE-skill-handoff](runtime.md#rt-rte-skill-handoff)

- Workflow selection: explicit Codex command-prefix handoff with detached execution and asynchronous notification; fallback skill instructions are an alternate dispatch path, not evidence that hooks fired.
- Delegation ownership: submit dispatches; the launcher manages subprocess lifetime; Pi/model owns inner task actions; the parent owns review and user-facing reporting.
- Verification boundary: launcher accepts process/stop status, not task correctness. The parent is asked to inspect changes and assess reported verification; no successful review is observed.
- Recovery ownership: launcher terminates timed-out work without rollback; parent receives failures/wrong-result reporting guidance and a provider-error rerun instruction, not an automatic repair policy.
- Delivery boundary: result-file persistence and host JSON emission are wired; subsequent host delivery, parent review and final user receipt remain uninspected.
