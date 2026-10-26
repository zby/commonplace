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
ownership, `launcher.ts` Pi arguments and JSON collection, `process.ts`
process cancellation, `budgets.ts` depth and worker grants, and `sessions.ts`
continuation and audit ownership.
`session-info.ts` is a child extension that reports the session Pi selected.
The original files came from:

```text
/home/zby/.pi/agent/install/releases/1.0.0/node_modules/@earendil-works/pi-coding-agent/examples/extensions/subagent/
```

The extension launches separate Pi processes with fresh, persistent sessions
unless a recorded worker's `sessionFile` is supplied explicitly. It never copies
the parent's conversation. Children still load applicable repository context and
resources. This is not a filesystem sandbox.

Worker results use the latest assistant response and process outcome to classify
failure. An earlier assistant error recovered by Pi's built-in retries remains
in the returned messages but does not make the final result fail. A terminal
assistant error or abort, nonzero process exit, process error or missing assistant
result still fails. Recovery does not certify the worker's output; the workflow
checks it through its normal completion and acceptance path.

## Launch configuration

The repository ships [`commonplace-worker`](agents/commonplace-worker.md), a general-purpose agent
with `read`, `bash`, `edit`, `write`, and `subagent`. Assign its specific role and
authorized inputs/outputs in each handoff. It can delegate only within the
runtime's depth and worker budgets, both zero by default. Select it with
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

`maxDepth` and `maxWorkers` are nonnegative integer budgets, defaulting to 0 on
**every launch**, including continuation. They are accepted at the top level and
on each parallel task; item values override call-wide values. `maxDepth` grants
further delegation levels to the child. `maxWorkers` reserves a worker pool for
that child from the caller's capacity. Depth alone does not grant worker slots.
For example, `maxDepth: 1, maxWorkers: 1` lets a worker launch one leaf worker.

The child's depth is capped at the caller's remaining depth minus one. Its
worker pool is capped at the caller's capacity minus one. The caller reserves
`1 + maxWorkers` slots for the granted child subtree until the child's execution
settles, including cancellation and cleanup. Reservations are not shrunk just
because other jobs are busy: async calls reject if the reservation will not fit;
blocking calls wait. Idle reserved slots are unavailable to siblings.

Example single launch:

```json
{
  "agent": "<definition name>",
  "agentScope": "project",
  "model": "openai/gpt-6.1-sol",
  "thinkingLevel": "medium",
  "maxDepth": 1,
  "maxWorkers": 1,
  "task": "<handoff>",
  "cwd": "<absolute worktree root>"
}
```

After editing the extension, use `/reload` before calling the new parameters.
This does not change the schema already exposed to an in-flight invocation.

Persistent worker sessions require the session APIs and CLI behavior verified
against Pi 1.3.0. Run the extension tests against the installed Pi package:

```bash
PI_PACKAGE_DIR=<absolute path to node_modules/@earendil-works/pi-coding-agent> \
  node --test .pi/extensions/subagent/tests/*.test.mjs
```

Mocked tests cover discovery, approval-free destination launches, argument
construction, shared capacity and lifecycle. Real-process tests launch harmless Node children to check output,
shutdown, escalation and (on Linux) descendant termination. Native Pi startup
tests use isolated directories and no prompts to check session references,
working-directory grouping, settings and environment storage overrides. SDK
reopening checks retained history. No test makes model calls; model-backed
continuation and real model/resource inheritance remain untested.

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

## Persistent sessions and continuation

Workers use Pi's normal session storage rules. The default is
`~/.pi/agent/sessions/`, grouped by the child's working directory. Pi's
`PI_CODING_AGENT_SESSION_DIR` and `sessionDir` setting retain their normal
precedence. No project-local store or custom worktree routing is introduced.
The child reports its actual session ID and file through a private stderr
control record; the adapter does not reconstruct Pi's directory or file names.

Completed results expose `sessionId`, `sessionFile` and `executionDir` in both
structured details and the model-facing summary. Result details and each
`execution.json` also record `parentSessionId`, `parentSessionFile`, `maxDepth`
and `maxWorkers`. Parent files are null for an ephemeral parent. This permits
walking from a child execution upward to its parent, including after a resume
from a different parent. A new call always starts a new
conversation. To continue a particular worker, supply its exact saved file:

```json
{
  "agent": "commonplace-worker",
  "agentScope": "project",
  "cwd": "<same absolute worktree root>",
  "sessionFile": "<sessionFile returned by the earlier execution>",
  "task": "<next staged handoff>"
}
```

`sessionFile` works for single calls, asynchronous `start`, and individual
parallel tasks. It cannot be supplied once for an entire parallel batch.
Omitted model/thinking overrides retain the worker's recorded launch selection
on continuation, rather than inheriting a different parent's selection.
Explicit overrides still apply. Changed agent instructions, tools, definition
identity or working directory reject continuation. Ambient project resources
still reload normally; a saved conversation is not a frozen environment.

The file must be nonempty and belong to a worker recorded by this adapter.
Missing files never silently create replacement conversations. An exclusive
filesystem lock serializes this adapter's continuations across parent processes.
Other Pi clients must not write that session concurrently. After an abrupt
crash, a retained `active/` lock blocks continuation: inspect its owner record,
processes and evidence before manually removing the stale lock. Do not infer
that a dead parent means every descendant stopped.

Each native `<session>.jsonl` has a sibling `<session>.jsonl.subagent/` directory.
It holds worker identity, an active lock while running, and a separate directory
per execution containing:

- `events.jsonl`: raw JSON stdout, including recovered errors and retry events;
- `stderr.log`: raw stderr, including the session-reference control record;
- `execution.json`: task, agent prompt/tools, launch arguments, requested model
  and thinking, parent session identity, granted budgets, start/end timestamps,
  final outcome and usage.

These records are retained after success, failure, cancellation, `forget`,
shutdown and reload. Temporary prompt transport files are still removed; their
contents are retained in execution metadata. An audit-write failure aborts the
worker and fails the execution rather than certifying an unrecorded success.
Failures before the child reports its session may have no child audit files;
the parent result still reports startup diagnostics. No automatic retention
cleanup is implemented. Sessions and logs can contain sensitive source content;
keep a custom session-directory override out of Git if it points into a checkout.

For multistage writing, record the author's `sessionFile` in the run's handoff
bookkeeping and use it for the incumbent reveal and any permitted repair.
Reconstructors and independent reviewers still start fresh conversations. This
does not recover earlier ephemeral workers or release an already-blocked run.
Reload before using the new tool schema, and do not reload with active jobs.

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
map in the workflow's bookkeeping. Start while unreserved slots remain, then call:

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

Parallel calls permit at most eight tasks. A root session has four worker
slots. Each child receives a statically partitioned pool, rather than a new pool
of four: its job plus its reserved descendant slots count against its caller.
The extension-controlled tree therefore fits within the root's four slots;
the root coordinator itself is not counted. Job details expose reserved `slots`.
Blocking calls queue on the weighted capacity and release their handles when
they return; async `start` rejects when its reservation cannot fit. Interrupting
a blocking call cancels its children, unlike interrupting async `wait`. Slots
remain reserved while cancelling, until process closure and cleanup. Shutdown
prevents queued blocking tasks from spawning.

The extension reads `PI_SUBAGENT_DEPTH` and `PI_SUBAGENT_WORKERS` at load. Both
absent means a root with unlimited inherited depth and four slots. Otherwise
both must contain nonnegative integers, with at most four worker slots. Invalid
or partial environment budgets fail closed. At zero depth or zero capacity the
tool stays registered and control operations remain available, but all launches
are refused. Its description states the remaining depth and capacity. Resuming
a saved session never restores its old grant: this launch's budgets apply.

These are runtime bounds on this extension, not an OS sandbox or a prohibition
on arbitrary processes. Different root sessions have independent budgets; no
cross-process shared counter or automatic redistribution is implemented.

There is no chain mode or automatic answer forwarding. Use explicit workflow
handoffs. Each launch creates a new process;
it starts a fresh conversation unless `sessionFile` explicitly continues a
recorded worker.
A child has `subagent` only when its definition selects it. No selection is a
filesystem sandbox: no-launch and write-scope rules are instructions, not OS
enforcement. Nested results remain embedded in the parent's tool details.

Loading this extension does not release an already-blocked workflow. Follow the
workflow's operator recovery procedure separately; do not edit workflow state.
