# Live-source capture attempt: Workflow tool contract in the running session

- Capture date: 2026-08-20T20:09:31+02:00 (Europe/Warsaw)
- Capture method: direct inspection of this agent process's own tool roster + `claude --version`
- Capturing process: a Claude Code **sub-agent** (Agent-tool worker), model `claude-opus-5[1m]`, cwd `/home/zby/llm/commonplace`
- Host CLI version reported by `claude --version`: `2.1.237 (Claude Code)`

## What was inspected

The complete tool roster exposed to this process:

- Directly loaded: `Agent`, `Artifact`, `Bash`, `Edit`, `Read`, `Skill`, `ToolSearch`, `Write`
- Deferred (name-only, schema fetchable via `ToolSearch`): `EnterWorktree`, `ExitWorktree`, `Monitor`,
  `NotebookEdit`, `SendMessage`, `TaskStop`, `WebFetch`, `WebSearch`,
  `mcp__claude_ai_Gmail__authenticate`, `mcp__claude_ai_Gmail__complete_authentication`,
  `mcp__claude_ai_Google_Calendar__authenticate`, `mcp__claude_ai_Google_Calendar__complete_authentication`,
  `mcp__claude_ai_Google_Drive__authenticate`, `mcp__claude_ai_Google_Drive__complete_authentication`

A `ToolSearch` query for workflow/orchestration/subagent-script tooling
(`"+workflow orchestrate subagents script"`) returned only `EnterWorktree` — no
workflow-orchestration tool schema exists in this roster.

## Result

**No Workflow / dynamic-workflow tool contract is exposed in this process.** No tool
description, no parameter schema, no phase or agent-spawn API.

## Scope of this capture — what it can and cannot establish

- It establishes only that **this sub-agent process** at this timestamp had no workflow
  tool in its roster.
- Claude Code sub-agents are a different tool-roster tier from a main interactive session,
  and the docs (`SRC-1`) describe workflow authoring as something the **main session**
  Claude does. This capture therefore **cannot** establish that a main session lacks such
  a tool, that the feature is disabled on this host, or that no such contract exists.
- It also cannot establish anything about the workflow *runtime's* internals, which are
  described in the docs as executing outside the conversation entirely.

## Consequence for the run

The optional live source is **unavailable as substantive evidence**. It is registered as
`SRC-2` with evidence layer `observed run`, scope: negative/roster-only, and it supports
no positive finding about the target system. The analysis proceeds `doc-grounded` on
`SRC-1` alone.
