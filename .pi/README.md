# Pi workers in this worktree

Start Pi from this worktree's root and grant project trust to load the project
extension. Use `/reload` after changing resources in an already-running Pi
session whose working directory is this worktree.

For an analysis run, prepare the dedicated worktree's local command environment
using [isolated run setup](../kb/agentic-systems/instructions/analyse-agentic-system/SKILL.md#isolated-run-setup)
before starting Pi; `commonplace-workflow prepare-analysis --name <system> -- pi`
prepares and launches it in one command. Worker processes inherit its `PATH`.
Starting Pi from a worktree alone does not isolate the shared editable Commonplace installation.
Keep the run's code and method files unchanged until completion.

`APPEND_SYSTEM.md` supplies the worker call format and coordinator preflight in
Pi's startup system prompt. It also loads in children; the coordinator rules
apply only when the `subagent` tool is exposed. Worker selection excludes that
tool. Keep runtime-specific guidance here rather than in shared `AGENTS.md`.

`extensions/subagent/{index.ts,agents.ts}` are unchanged copies of the subagent
example shipped with `@earendil-works/pi-coding-agent` 1.0.0. The original files
came from:

```text
/home/zby/.pi/agent/install/releases/1.0.0/node_modules/@earendil-works/pi-coding-agent/examples/extensions/subagent/
```

The extension launches separate Pi processes with fresh, non-persisted
sessions. It does not copy the coordinator's conversation. Children still load
applicable repository context and resources. This is not a filesystem sandbox.

## Worker configuration

`agents/commonplace-worker.md` allows `read`, `bash`, `edit`, and `write`.
It omits `model`, so the worker inherits the dispatching session's model and
thinking level. Configure OpenAI authentication in Pi, not in this repository.

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
`kb/agentic-systems/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md`.
Do not add parent conversation or source interpretations to the job handoff.

## Limits

The example permits at most eight tasks per parallel call and runs at most four
concurrently. It has no explicit nesting limit or continuing-worker interface.
The configured worker does not have the `subagent` tool, but `bash` is not a
sandbox: the no-launch and write-scope rules are instructions, not OS enforcement.

Loading this extension does not release an already-blocked workflow. Follow the
workflow's operator recovery procedure separately; do not edit workflow state.
