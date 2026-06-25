---
description: "Fractal as a code-grounded RLM harness: PredictRLM workspace turns, SBX sandbox mounts, headless delegation, and session continuity outside the repo."
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model, tool-loop]
status: seedling
---

# Fractal

**Evidence basis:** first-hand reading of the `Trampoline-AI/fractal` checkout at commit [5954a07d](https://github.com/Trampoline-AI/fractal/commit/5954a07d464feeaf6c311a9fa5ca2e54200a6794) (2026-06-25), covering README/docs, `src/fractal`, bundled agent skills, and tests. I did not run a live Fractal turn.

Fractal is an agentic harness and delegation surface for Recursive Language Model work, not an agent-memory system. Its product boundary is narrow: package `predict-rlm` as a terminal/headless coding agent, mount a real workspace into an SBX sandbox, let the model write and run its own Python orchestration code and sub-model calls, then preserve enough session state to resume multi-turn work.

The memory Fractal adds is session continuity for the harness. It does not maintain durable project knowledge, semantic recall indexes, cross-task retrieval, or policy about how retained knowledge should bind future agent behavior. That makes it useful to Commonplace as an external heavy-analysis delegate or RLM implementation reference, while any findings it produces still need ordinary source capture, review, and validation before becoming KB artifacts.

## Runtime Shape

`FractalAgent.aforward` constructs a `PredictRLM` call over a direct workspace mount. The model receives `workspace`, optional `included_paths`, `user_message`, and `session_history`; the output contract is `response` plus `changed_files` ([agent/service.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/service.py), [agent/signature.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/signature.py)). The configured skills are Fractal's filesystem-coding skill plus PredictRLM spreadsheet, PDF, and docx skills; the filesystem skill instructs the generated code to use `rg`, `os.open`, `os.pread`, `os.pwrite`, `os.ftruncate`, and `os.replace` rather than broad recursive reads or ad hoc shell text edits ([agent/skills.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/skills.py)).

The sandbox boundary is direct but not copy-based. Fractal builds an `SbxBackend` with `DirectWorkspaceMount` entries for the primary workspace and any included directories, so the sandbox sees the host paths and edits host files in place ([agent/service.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/service.py)). `--include` accepts only existing non-symlink directories, and `.fractal` is excluded from the workspace object passed to PredictRLM ([cli.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/cli.py), [agent/service.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/service.py)). The README states that each turn runs in Docker SBX with no network access by default, while the direct passthrough mount means file edits appear on the host immediately ([README.md](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/README.md)).

Fractal also injects workspace instructions. It reads `AGENTS.md` from the workspace root, truncates it at 20,000 characters, and splices it into the dynamic DSPy signature before the session summary ([agent/service.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/service.py), [agent/signature.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/signature.py)). That makes Fractal an agent that honors local harness instructions, but those instructions are prompt text, not a typed policy substrate.

## Session Continuity

The session model has two layers. `SessionSummary` stores ordered turns with user message, agent status, response, counts of files read/changed, commands run, errors, and usage. `SessionHistoryTurn` stores exact prior trace material: files, commands, PredictRLM `RunTrace`, status, error, and timestamps ([session.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/session.py), [docs/session-management.md](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/docs/session-management.md)).

The placement matters. The rendered summary is embedded into the per-turn signature under "Always-visible session summary", because PredictRLM input fields are mainly REPL variables and the summary needs to be visible before the model decides what variables to inspect. The full history is passed as the `session_history` input field for exact recall from Python ([agent/signature.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/agent/signature.py)). Runtime submission saves a pending user/history turn before calling the model, then records success, failure, max-iteration, or interrupt outcomes after the call ([runtime.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/runtime.py)).

At this commit, sessions are not workspace artifacts. `default_state_dir` chooses `FRACTAL_STATE_HOME`, `$XDG_STATE_HOME/fractal`, or `~/.local/state/fractal`; `workspace_key` hashes the resolved workspace path; each session lands under `<state-root>/workspaces/<workspace-key>/sessions/<session_id>.json` ([session.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/session.py)). Tests assert that `sessions_dir_path(workspace)` is stable, outside the workspace, and specifically not `<workspace>/.fractal/sessions` ([tests/test_session.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/tests/test_session.py)). The bundled skill and recipes still describe a workspace-local `.fractal/sessions` location in places, so operators should trust the source and `docs/session-management.md` over those stale snippets until the repo reconciles them ([.agents/skills/fractal/SKILL.md](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/.agents/skills/fractal/SKILL.md), [.agents/skills/fractal/RECIPES.md](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/.agents/skills/fractal/RECIPES.md)).

## Delegation Surface

Headless mode is the practical integration point. `fractal -p` runs one non-interactive turn; stdout is the final response, stderr carries progress, changed files, usage, and status; `--json` emits a structured object with `session_id`, `workspace`, `status`, `response`, `changed_files`, `usage`, and `error` ([cli.py](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/src/fractal/cli.py), [docs/headless.md](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/docs/headless.md)). Exit codes distinguish success, runtime/setup error, max-iteration best effort, and interrupt.

The repo ships a `fractal` agent skill that tells another coding agent to delegate context-heavy audits, large codebase analysis, log/diff synthesis, and open-ended investigation to `fractal -p` ([.agents/skills/fractal/SKILL.md](https://github.com/Trampoline-AI/fractal/blob/5954a07d464feeaf6c311a9fa5ca2e54200a6794/.agents/skills/fractal/SKILL.md)). That is the strongest Commonplace-relevant use: Fractal can scout a large working set and return a distilled answer, but the parent agent must still inspect diffs, preserve evidence, and decide what to promote.

## Reading Against Commonplace

Fractal is a shipped instance of the [RLM model-authorship pattern](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md). The model writes symbolic orchestration code inside the turn, while the REPL and PredictRLM runtime execute the bookkeeping outside conversational context. Fractal adds a CLI, sandbox, provider/config layer, workspace instructions, and session persistence around that pattern.

The comparison with [Claude Code dynamic workflows](./claude-code-dynamic-workflows.md) is useful. Dynamic workflows expose a sandboxed JavaScript orchestrator over sub-agents inside a larger Claude Code session, with a path to save the whole script as a command. Fractal instead makes the whole turn an RLM call: the generated orchestration is not exposed as a reusable workflow artifact, but the session stores summaries and traces that could later be mined. It partially softens RLM ephemerality by retaining traces, while leaving orchestration-strategy promotion outside the product.

For Commonplace operations, Fractal is better read as a bounded-context workbench than as a memory substrate. It can be asked to audit a large repo, inspect a source corpus, or synthesize candidate findings without flooding the parent agent's context. The output should enter Commonplace through normal commitments: source snapshots or ingests for evidence, authored notes for claims, and validation for structure. A Fractal response alone is not a KB artifact with binding force.

## What To Watch

- Whether PredictRLM runtime hooks consistently capture file reads and commands; Fractal's session summaries depend on backend event coverage.
- Whether the stale `.fractal/sessions` references in shipped skills/recipes are fixed, since agent-facing instructions currently conflict with code and session docs.
- Whether session history limits, trace size, and privacy boundaries become configurable enough for long-running workspace use.
- Whether headless JSON remains stable enough for agents and CI to depend on.
- Whether Fractal adds a promotion path from useful RLM-generated orchestration into tested reusable workflow artifacts.

---

Relevant Notes:

- [RLM has the model write ephemeral orchestrators over sub-agents](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) - see-also: the theoretical pattern Fractal packages into a terminal and headless coding agent.
- [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) - see-also: situates Fractal's trace persistence and missing promotion path on the symbolic-work persistence axis.
- [Claude Code dynamic workflows](./claude-code-dynamic-workflows.md) - see-also: another shipped harness that exposes model-authored symbolic orchestration, but with a different language, sandbox boundary, and promotion surface.
- [tool loop](../notes/tool-loop-README.md) - see-also: the local theory cluster for reading Fractal's RLM loop and delegation surface.
