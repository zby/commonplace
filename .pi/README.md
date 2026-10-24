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
including the call format. Pi can load it at startup when project trust
permits; do not assume a child inherits it. Keep runtime-specific guidance here
rather than in shared `AGENTS.md`.

An analysis run (`commonplace-analysis run`) launches its own workers through
the worker profile's headless harness (`pi -p` for a Pi profile); it needs no
`subagent` launches.

`extensions/subagent/{index.ts,agents.ts}` were copied from the subagent
example shipped with `@earendil-works/pi-coding-agent` 1.0.0. The adapter now uses
one session-local job owner for blocking and asynchronous launches, with compact
rendering. `index.ts` owns tool dispatch, `agents.ts` discovery, `jobs.ts` job
ownership, `launcher.ts` Pi arguments and JSON collection, and `process.ts`
process cancellation. The original
files came from:

```text
/home/zby/.pi/agent/install/releases/1.0.0/node_modules/@earendil-works/pi-coding-agent/examples/extensions/subagent/
```

The extension launches separate Pi processes with fresh, non-persisted
sessions. It does not copy the parent's conversation. Children still load
applicable repository context and resources. This is not a filesystem sandbox.

Worker results use the latest assistant response and process outcome to classify
failure. An earlier assistant error recovered by Pi's built-in retries remains
in the returned messages but does not make the final result fail. A terminal
assistant error or abort, nonzero process exit, process error or missing assistant
result still fails. Recovery does not certify the worker's output; the workflow
checks it through its normal completion and acceptance path.

## Launch configuration

The repository ships [`commonplace-worker`](agents/commonplace-worker.md), a general-purpose agent
with `read`, `bash`, `edit`, and `write`. Assign its specific role and authorized
inputs/outputs in each handoff; it has no nested delegation tool. Select it with
`"agent": "commonplace-worker", "agentScope": "project"` from this worktree. User-level
lookup remains the tool's default, so the scope must be explicit.

A definition supplies the child's system instructions and tools; one that
omits `model` inherits the dispatching
session's model and thinking level unless the call overrides them. The
extension passes the definition body through a temporary file via
`--append-system-prompt`. Definitions are discovered afresh on each invocation.
Configure model authentication in Pi, not in this repository.

The tool accepts optional `model` and `thinkingLevel` at the top level in all
modes and on each item in `tasks`. Item values override top-level
values independently. Model precedence is item, top-level, agent definition,
then parent. Thinking precedence is item, top-level, then parent
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
  "agent": "<definition name>",
  "agentScope": "project",
  "model": "openai/gpt-6.1-sol",
  "thinkingLevel": "medium",
  "task": "<handoff>",
  "cwd": "<absolute worktree root>"
}
```

After editing the extension, use `/reload` before calling the new parameters.
This does not change the schema already exposed to an in-flight invocation.

Run the extension tests against an installed Pi package:

```bash
PI_PACKAGE_DIR=<absolute path to node_modules/@earendil-works/pi-coding-agent> \
  node --test .pi/extensions/subagent/tests/*.test.mjs
```

Mocked tests cover discovery, approval-free destination launches, argument
construction, shared capacity and lifecycle. Real-process tests launch harmless Node children to check output,
shutdown, escalation and (on Linux) descendant termination. No test launches Pi
agents or makes model calls. Real model/resource inheritance remains untested.

`agentScope: "project"` selects definitions from the child's `.pi/agents/`;
the default remains user agents. Project definitions are discovered afresh from
each child's effective `cwd`, not the parent checkout. For parallel calls each
item can name its own directory. Results identify the child directory.

The subagent extension loads destination agent definitions without a separate
approval dialog in either interactive or non-interactive mode. Choose only
trusted destinations within the commission's scope: definitions supply the
child's system instructions and tools. Pi's project trust still controls loading
project configuration and extensions; this removes only the subagent-specific
destination confirmation.
Malformed explicit `tools` values (including empty lists) reject the selected
agent, never fall back to Pi's defaults. Omitting `tools` still selects defaults.
Names are syntax-checked, not checked against the destination's loaded tool
registry; extension-defined tools can differ between worktrees.

## Scry research

[`scry-research`](agents/scry-research.md) is a separate research agent with
`read` and `codemode`. Launch it with `"agent": "scry-research", "agentScope":
"project"` and a bounded research question. Scry provides analytical SQL over
indexed corpora, not generic web search. The agent checks account capabilities,
reads the live schema before writing SQL, and returns findings with queries,
provenance and coverage limitations. It does not write KB artifacts. Its default
budget is five research calls beyond account/schema discovery unless the
handoff supplies another limit. Paid inference and state-changing capabilities
need explicit authorization.

Profile guidance follows [Scry agent setup](https://scry.io/docs/agent-setup)
and its [public session contract](https://api.scry.io/v1/scry/context?mode=agent).
Use live discovery for available relations and tools rather than freezing a
corpus inventory here. Personal-key use is licensed for individual,
non-commercial research; other use requires checking Scry's terms. Public work
built on Scry must credit it visibly with a link to https://scry.io.

Configure the `scry` MCP server in the user's `~/.pi/agent/mcp.json` with the
endpoint `https://mcp.scry.io` and `codemode` exposure. Keep credentials and OAuth
state outside the repository. The parent owns interactive authentication:
run `pi mcp list` to check the connection, then `pi mcp login scry` when sign-in
is required and the operator authorizes it. The login command starts browser
approval; the headless research worker has no shell tool and returns this
recovery instruction instead. A missing tool namespace alone does not diagnose
the cause. After login, launch a fresh worker and verify `whoami`; an existing
parent session may need `/mcp reconnect scry`. A new session loads the user
configuration; use `/reload` for an existing session when no worker jobs are
active. Do not treat missing authentication as missing funds.

The agent definition is a task/tool profile, not exclusive account access:
user-level MCP configuration applies to other Pi sessions too. Codemode can
reach other registered tools; the profile's Scry-only boundary is instructional,
not an OS sandbox.

## Rolling dispatch

After updating the extension, use `/reload` **before** launching work. Check that
`subagent` exposes `action` and `handles`; an already-loaded old schema cannot
use these operations. Do not reload while jobs are active.

Start each independent job separately:

```json
{
  "action": "start",
  "agent": "<definition name>",
  "agentScope": "project",
  "cwd": "<absolute directory>",
  "task": "<handoff>"
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
for that slot while the others continue. The extension limits active jobs, not
pipelines of dependent jobs; the dispatching session owns that distinction. Synchronous parallel mode remains a wait-for-all operation.

Other handle-only calls accept `action` and `handles`, not launch fields:

- `status`: list states and agent/worktree labels; omit handles to list all.
  Blocking calls also appear while running; their handles are released when
  the blocking call returns.
- `cancel`: request cancellation; a `cancelling` job still occupies its slot.
  Use `wait` to observe termination before reassigning its destination.
- `forget`: release terminal handles after recording their results. Active jobs
  cannot be forgotten. At most 128 handles are retained per session.

An interrupted `wait` leaves jobs running. Interactive completion notifications
identify the handle; they do not replace reading its result. Full result details
retain the child messages, while model-facing summaries may be truncated.

Handles and results are session-local, not a durable job service. Orderly
shutdown, session replacement and reload cancel active jobs in all modes and wait for process
closure; they invalidate handles. POSIX root launches use process groups so
cancellation also targets descendants that remain in that group, escalating
from TERM to KILL after five seconds. Windows cancellation targets the direct
child only. An abrupt parent crash or a descendant that detaches is not covered:
reconcile ownership and retained workflow evidence before any replacement run.
No workflow failure or recovery decision is automatically resolved by a job's
process exit. Do not end a print-mode parent with jobs still pending.

## Limits

Parallel calls permit at most eight tasks. All modes share one four-active-job
limit per session. Blocking calls wait for capacity and release their handles
when they return; async `start` rejects when full. Interrupting a blocking call
cancels its children, unlike interrupting async `wait`. Shutdown prevents queued
blocking tasks from spawning. A child that has `subagent` has its own pool.

There is no chain mode or automatic answer forwarding. Use explicit workflow
handoffs. There is no explicit nesting limit or continuing-worker interface:
each launch creates a fresh child.
A child has `subagent` only when its definition selects it. No selection is a
filesystem sandbox: no-launch and write-scope rules are instructions, not OS
enforcement. Nested results remain embedded in the parent's tool details.

Loading this extension does not release an already-blocked workflow. Follow the
workflow's operator recovery procedure separately; do not edit workflow state.
