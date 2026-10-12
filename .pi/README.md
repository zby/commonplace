# Pi workers in this worktree

Start Pi from this worktree's root and grant project trust to load the project
extension. Use `/reload` after changing resources in an already-running Pi
session whose working directory is this worktree.

For an analysis run, prepare the dedicated worktree's local command environment
using [isolated run setup](../kb/agentic-system-analyses/instructions/analyse-agentic-system/SKILL.md#isolated-run-setup)
before starting Pi; `commonplace-analysis prepare --name <system> -- pi`
prepares and launches it in one command. Worker processes inherit its `PATH`.
Starting Pi from a worktree alone does not isolate the shared editable Commonplace installation.
Keep the run's code and method files unchanged until completion.

[`APPEND_SYSTEM.md`](APPEND_SYSTEM.md) is the canonical Pi delegation contract,
including the worker call format and coordinator preflight. Pi can load it at
startup when project trust permits; do not assume a child inherits it. The
coordinator definition explicitly requires reading the complete file from the
current worktree's repository root before any delegation or opening a workflow,
then following it. An absent or unreadable file is a blocker, not permission to
guess launch arguments. The coordinator rules apply only when `subagent` is
exposed. Ordinary worker selection excludes that tool; coordinator selection
includes it. Keep runtime-specific guidance here rather than in shared `AGENTS.md`.

`extensions/subagent/{index.ts,agents.ts}` were copied from the subagent
example shipped with `@earendil-works/pi-coding-agent` 1.0.0. `index.ts` now
adds call-wide and per-task model and thinking-level overrides. The original
files came from:

```text
/home/zby/.pi/agent/install/releases/1.0.0/node_modules/@earendil-works/pi-coding-agent/examples/extensions/subagent/
```

The extension launches separate Pi processes with fresh, non-persisted
sessions. It does not copy the coordinator's conversation. Children still load
applicable repository context and resources. This is not a filesystem sandbox.

## Worker configuration

`agents/commonplace-worker.md` allows `read`, `bash`, `edit`, and `write`.
It omits `model`, so the worker inherits the dispatching session's model and
thinking level unless the tool call overrides them. Configure OpenAI
authentication in Pi, not in this repository.

`agents/commonplace-coordinator.md` additionally selects `subagent`. Use it
when commissioning an entire standard skill that must launch its own workers;
keep individual scheduled jobs on `commonplace-worker`. Both definitions are
discovered afresh on each invocation, so this role selection needs no extension
reload. The extension passes the definition body through a temporary file via
`--append-system-prompt`; that body instructs the child coordinator to explicitly
read the canonical contract rather than relying on automatic startup loading.
Before opening a run, it must successfully launch the required diagnostic
worker. This tests the intended parent → coordinator → worker path, not a
maximum supported depth. Do not use agent CLIs through Bash as a substitute.

The tool accepts optional `model` and `thinkingLevel` at the top level in all
modes and on each item in `tasks` or `chain`. Item values override top-level
values independently. Model precedence is item, top-level, agent definition,
then coordinator. Thinking precedence is item, top-level, then coordinator
when the model is inherited or explicitly overridden. With no model override,
an agent definition that pins a model retains Pi's own default thinking level
unless the call supplies `thinkingLevel`.

`thinkingLevel` accepts `off`, `minimal`, `low`, `medium`, `high`, `xhigh`, and
`max`. Overrides become `--model` and `--thinking` arguments on the child Pi
process. Pi may clamp the requested thinking level to the model's capabilities;
result details record the requested level, not verified effective effort.

Example single launch:

```json
{
  "agent": "commonplace-worker",
  "agentScope": "project",
  "model": "openai/gpt-6.1-sol",
  "thinkingLevel": "medium",
  "task": "<workflow handoff>",
  "cwd": "<absolute worktree root>"
}
```

After editing the extension, use `/reload` before calling the new parameters.
This does not change the schema already exposed to an in-flight invocation.

Run the extension's mocked-process tests against an installed Pi package:

```bash
PI_PACKAGE_DIR=<absolute path to node_modules/@earendil-works/pi-coding-agent> \
  node --test .pi/extensions/subagent/tests/*.test.mjs
```

These tests load the extension and inspect child arguments without launching
agents or making model calls.

Select the worker with `agentScope: "project"`; the example defaults to user
agents. Set `cwd` to this worktree's absolute root when dispatching jobs.

Before starting or resuming a workflow, use the exposed `subagent` tool for a
single diagnostic with this task:

```text
This is a Commonplace worker-launch diagnostic. Reply with
COMMONPLACE_WORKER_OK and any agent-depth or nesting-limit values explicitly
exposed in your runtime instructions; report unknown otherwise. Do not read
files, use tools, invoke skills, spawn workers, or modify anything.
```

Success establishes that one worker can run, not a maximum depth or capacity.
For code-scheduled analysis jobs, use the exact handoff prescribed by
`kb/agentic-system-analyses/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md`.
Do not add parent conversation or source interpretations to the job handoff.

## Rolling dispatch

After updating the extension, use `/reload` **before** launching work. Check that
`subagent` exposes `action` and `handles`; an already-loaded old schema cannot
use these operations. Do not reload while jobs are active.

Start each independent system pipeline separately:

```json
{
  "action": "start",
  "agent": "commonplace-coordinator",
  "agentScope": "project",
  "cwd": "<absolute prepared system worktree>",
  "model": "openai/gpt-6.1-sol",
  "thinkingLevel": "medium",
  "task": "<source-only workflow commission>"
}
```

`start` returns a handle without awaiting the child. Keep a handle-to-assignment
map in the workflow's bookkeeping. Start up to four jobs, then call:

```json
{"action": "wait", "handles": ["<handle-1>", "<handle-2>", "<handle-3>", "<handle-4>"]}
```

`wait` returns the first finished selected job, including failure or cancellation,
not the whole group. Remove that handle from the pending set. A completed result
is repeatable: passing its handle again returns it again. Launch the next job
for that slot while the others continue. For the rerun workshop, the next job is
the fresh audit; only after its disposition may the slot receive a new system.
The extension limits active jobs, not workflow pipelines; the orchestrator owns
that distinction. Synchronous parallel mode remains a wait-for-all operation.

Other handle-only calls accept `action` and `handles`, not launch fields:

- `status`: list states and agent/worktree labels; omit handles to list all.
- `cancel`: request cancellation; a `cancelling` job still occupies its slot.
  Use `wait` to observe termination before reassigning its destination.
- `forget`: release terminal handles after recording their results. Active jobs
  cannot be forgotten. At most 128 handles are retained per session.

An interrupted `wait` leaves jobs running. Interactive completion notifications
identify the handle; they do not replace reading its result. Full result details
retain the child messages, while model-facing summaries may be truncated.

Handles and results are session-local, not a durable job service. Orderly
shutdown, session replacement and reload cancel active jobs and wait for process
closure; they invalidate handles. POSIX root launches use process groups so
cancellation also targets descendants that remain in that group, escalating
from TERM to KILL after five seconds. Windows cancellation targets the direct
child only. An abrupt parent crash or a descendant that detaches is not covered:
reconcile ownership and retained workflow evidence before any replacement run.
No workflow failure or recovery decision is automatically resolved by a job's
process exit. Do not end a print-mode parent with jobs still pending.

## Limits

The example permits at most eight tasks per parallel call and runs at most four
concurrently. Asynchronous mode separately permits four active jobs per session;
do not mix modes to evade a workflow's capacity limit. It has no explicit nesting
limit or continuing-worker interface: each start creates a fresh child.
The ordinary worker does not have `subagent`; the coordinator does. Neither
selection is a filesystem sandbox: the no-launch and write-scope rules are
instructions, not OS enforcement. Nested results remain embedded in the
parent's tool details; coordinators also use non-persisted sessions.

Loading this extension does not release an already-blocked workflow. Follow the
workflow's operator recovery procedure separately; do not edit workflow state.
