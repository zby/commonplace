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
  node --test .pi/extensions/subagent/tests/launch-overrides.test.mjs
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
`kb/agentic-systems/instructions/analyse-agentic-system/drive-a-code-scheduled-run.md`.
Do not add parent conversation or source interpretations to the job handoff.

## Limits

The example permits at most eight tasks per parallel call and runs at most four
concurrently. It has no explicit nesting limit or continuing-worker interface.
The configured worker does not have the `subagent` tool, but `bash` is not a
sandbox: the no-launch and write-scope rules are instructions, not OS enforcement.

Loading this extension does not release an already-blocked workflow. Follow the
workflow's operator recovery procedure separately; do not edit workflow state.
