# Commonplace delegation in Pi

These instructions describe this project's Pi subagent extension. They do not
replace a workflow's authority, evidence boundaries, or stop conditions.

An analysis needs no `subagent` launches: `commonplace-analysis run` launches
its own workers through the worker profile's headless harness. Use the
extension only for work you were commissioned to delegate.

## Dispatch format

- `agent` is an agent definition's name, not `single`, a workflow job name,
  or a model name. This repository ships the general-purpose `commonplace-worker`
  definition; select it with `agentScope: "project"` and assign its role,
  authorized inputs and owned outputs in the handoff.
- `agentScope` selects where definitions are searched: `user` (the default)
  searches your Pi agent directory, `project` the `.pi/agents/` of the child's
  effective `cwd`, `both` both. The extension loads destination agent
  definitions without a separate approval dialog in either interactive or
  non-interactive mode. Use only destinations within the commission's scope;
  tool availability does not expand mutation authority.
- Single mode uses `agent` and `task`. Parallel mode uses `tasks`, an array of
  objects containing `agent`, `task`, and optionally `cwd`, `model`,
  `thinkingLevel`, `sessionFile`, `maxDepth`, and `maxWorkers`. Top-level model,
  thinking and budget values apply to every task; per-task values override them.
  Chain mode is not supported; use explicit isolated handoffs. Blocking calls
  wait for capacity, while asynchronous starts reject when full.
- For rolling dispatch, when the loaded schema exposes `action` and `handles`,
  use `action: "start"` with the single-job launch fields. Keep its returned
  handle. Start only while unreserved worker slots remain, then use `action: "wait"` with their handles
  to receive the first finished result; remove that handle before waiting again.
  Handle operations take only `action` and `handles`. `status` may omit handles
  to list all jobs; `cancel` requests termination; `forget` releases terminal
  results. Interrupted waits leave jobs running. Handles do not survive shutdown
  or reload, which cancel active jobs. Record assignments and results durably;
  reconcile ownership after interruption rather than blindly relaunching.
  See `.pi/README.md` for lifecycle and platform limits. An old schema requires
  reload before launching work, not a fallback to wait-for-all dispatch.
- `maxDepth` and `maxWorkers` default to 0 on every launch, including a resumed
  worker. Root sessions have four worker slots and no inherited depth cap.
  A child receives at most the caller's remaining depth minus one and at most
  its worker capacity minus one. The child's job plus its reserved worker slots
  count against the caller until it settles. Supply both budgets to allow
  nesting; depth alone grants no worker slots. `PI_SUBAGENT_DEPTH` and
  `PI_SUBAGENT_WORKERS` carry the granted limits. The tool remains registered at
  depth 0 but refuses launches and states its limits in its description. Budgets
  constrain execution; they do not expand the commission's authority.
- A child inherits the dispatching session's model and thinking level unless
  the call overrides them with `model` or `thinkingLevel`. A new call starts a
  fresh persistent session without the parent's conversation, using Pi's normal
  storage rules. Results return `sessionId`, `sessionFile`, `executionDir`,
  `parentSessionId`, `parentSessionFile` and the granted budgets.
  Supply that worker's `sessionFile` with the same agent and `cwd` to continue
  its conversation; omitted overrides then retain its recorded launch selection.
  Only resume a worker when the workflow permits its accumulated context.
  Reconstructors and independent reviewers remain fresh where required.
  `forget`, shutdown and reload do not delete sessions or audit files. Missing
  files, changed worker definitions and active/stale session locks reject
  continuation. Reconcile ownership before removing a stale lock; see
  `.pi/README.md`. Repository context still loads; this is not a filesystem
  sandbox.
- `fork_turns: "none"` expresses no parent conversation; this extension supplies
  that isolation by construction. It is not a supported tool argument. If any
  other launch requirement cannot be applied, report the launch failure rather
  than silently dropping it.
- `Unknown agent` is a definition/name/scope lookup failure, not proof that Pi
  cannot create subprocesses. Preserve the returned error exactly.

If `subagent` is not in your selected tools, these instructions do not
authorize you to acquire delegation tools or launch agents. Execute only
your assigned invocation within its stated scope.
