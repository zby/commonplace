# Commonplace delegation in Pi

These instructions describe this project's Pi subagent extension. They do not
replace a workflow's authority, evidence boundaries, or stop conditions.

## Coordinator preflight

If your exposed tools include `subagent`, you can dispatch project workers.
Before opening a workflow that requires workers, run one harmless diagnostic
through that tool with the following arguments. Set `cwd` to the absolute
repository root of your current worktree, not another checkout.

```json
{
  "agent": "commonplace-worker",
  "agentScope": "project",
  "cwd": "<absolute current worktree root>",
  "task": "This is a Commonplace worker-launch diagnostic. Reply with COMMONPLACE_WORKER_OK and any agent-depth or nesting-limit values explicitly exposed in your runtime instructions; report unknown otherwise. Do not read files, use tools, invoke skills, spawn workers, or modify anything."
}
```

If the tool is missing or the diagnostic fails, stop before opening the run and
report the exact evidence. Do not infer maximum depth or capacity from success.
Do not launch an agent CLI through `bash` as a substitute for the tool.

## Dispatch format

- `agent` is an agent definition's name: use `commonplace-worker`, not `single`,
  a workflow job name, or a model name.
- Always set `agentScope: "project"` for this worker. The extension's default
  scope is `user`, which does not search this project's `.pi/agents/`.
- Single mode uses `agent` and `task`. Parallel mode uses `tasks`, an array of
  objects containing `agent`, `task`, and optionally `cwd`, `model`, and
  `thinkingLevel`, plus top-level `agentScope: "project"`. Optional top-level
  `model` and `thinkingLevel` apply to every task; per-task values override them.
  Do not use a chain where isolation rules forbid forwarding previous outputs.
- The Commonplace worker inherits the coordinator's model and thinking level
  unless the call overrides them with `model` or `thinkingLevel`. Each call
  starts a fresh non-persisted session without the parent's conversation.
  Repository context still loads; this is not a filesystem sandbox.
- For a code-scheduled job, pass the exact handoff prescribed by the workflow,
  with its printed prompt path. Do not add parent context or read the job prompt
  yourself. Dispatch all jobs of a round before advancing the workflow.
- `fork_turns: "none"` expresses no parent conversation; this extension supplies
  that isolation by construction. It is not a supported tool argument. If any
  other launch requirement cannot be applied, report the launch failure rather
  than silently dropping it.
- `Unknown agent` is a definition/name/scope lookup failure, not proof that Pi
  cannot create subprocesses. Preserve the returned error exactly.

If `subagent` is not in your selected tools, these coordinator instructions do
not authorize you to acquire delegation tools or launch workers. Execute only
your assigned invocation within its stated scope.
