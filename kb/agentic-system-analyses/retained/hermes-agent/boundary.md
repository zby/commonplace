---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Hermes Agent at commit 0e427d788d253630d38a3a51cd76849e73cd6925, with the complete repository frozen and partial runtime-loop inspection."
run-id: AAS-2026-10-14-hermes-agent-bfb4bdc54d37-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: "0e427d788d253630d38a3a51cd76849e73cd6925"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/nousresearch/hermes-agent
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/hermes-agent-bfb4bdc54d37/related-systems/nousresearch--hermes-agent
  revision: "0e427d788d253630d38a3a51cd76849e73cd6925"
  sha256: null
---

# Hermes Agent boundary

## Boundary and evidence

This run examines Hermes Agent as an enclosing agent runtime, including its model-dependent execution and retained-context mechanisms. The intended use is to establish a source-grounded account of the runtime and its memory, skill and session-state responsibilities, not to measure effectiveness or recommend adoption. The evidence is the complete repository at the frozen commit above. The applicability cutoff is 2026-10-14; no later revision or external service behavior is included.

The classification is supported by the shipped command entry points and a traced caller into the agent, rather than by the repository's product description alone. SRC-1 `pyproject.toml` declares:

> [project.scripts]
> hermes = "hermes_cli.main:main"
> hermes-agent = "agent.legacy_cli:main"
> hermes-acp = "acp_adapter.entry:main"
> --- `pyproject.toml`

The `hermes` command's one-shot dispatch reaches `hermes_cli.oneshot`, which imports and constructs `run_agent.AIAgent` and calls its conversation API. That class inherits `TurnFacadeMixin`; the facade invokes `agent.conversation_loop.run_conversation` (SRC-1 `hermes_cli/main.py`, `hermes_cli/oneshot.py`, `run_agent.py`, `agent/turn_facade.py`). The caller is shipped target code, not an excluded application. The call site retains this minimum implementation evidence:

> result = agent.run_conversation(prompt, conversation_history=conversation_history or None)
> --- `hermes_cli/oneshot.py`

The conversation module describes the responsibilities behind that call (doctrine/design evidence, not an independently verified execution trace):

> ``run_conversation(agent, ...)`` drives one user turn (model call, tool dispatch,
> retries, fallbacks, compression, post-turn hooks).
> --- `agent/conversation_loop.py`

The selected boundary is **complete artifact, partial loop**, not whole-system. The repository tree and entry-point routing were inspected, but every material producer, admission path, maintenance path and consumer has not been traced. This is a completed declaration of a partial inspection boundary, not a claim of completed whole-system coverage. All files at the registered commit remain available to later source inspection; the paths below are initial inspection coverage, not an evidence allowlist.

Functional inclusions are the core agent and model/tool loop; shipped CLI, gateway and ACP callers; session persistence and recall; prompt/context assembly and compression; memory and skill read/write mechanisms; background maintenance; shipped scheduler and evaluation paths where they bear on those responsibilities. These responsibilities remain part of the target even where initial inspection is incomplete. In particular, gateway or ACP state ownership must not be attributed to an external host merely because those modules call `AIAgent`.

| Area | Initial coverage and remaining limit |
|---|---|
| Command admission | Inspected script declarations in `pyproject.toml`; searched routing in `hermes_cli/main.py` and `agent/legacy_cli.py`; read the agent-construction and conversation-call segment of `hermes_cli/oneshot.py`. Interactive `cli.py` and terminal frontends are not yet traced. This prevents a conclusion that all entry points have identical admission or cleanup behavior. |
| Core runtime | Read `run_agent.py` class, constructor forwarding and lazy session-database acquisition; read the actual facade-to-loop call in `agent/turn_facade.py`; inspected the loop module's declared responsibilities and searched its entry points. Provider requests, tool execution, retries and finalization are not yet traced end to end. This prevents an exhaustive control-flow or failure-recovery claim. |
| Memory and prompts | Read memory/skill guidance in `agent/prompt_builder.py`; searched memory-tool exposure in `agent/memory_manager.py`; read the declared review design in `agent/background_review.py` and located review hooks in `run_agent.py`. Provider implementations, built-in memory writes, skill admission and subsequent reload still require inspection. This prevents a claim that the entire retention loop or its safeguards has been verified. |
| Session state | Read the lazy database acquisition and persistence-isolation guard in `run_agent.py`; enumerated the root `hermes_state*.py` modules. The schema, message writes, repair, rewind and search implementations remain untraced. This prevents durability, isolation and recovery guarantees. |
| Other shipped callers | Inspected ACP startup/import routing in `acp_adapter/entry.py` and searched its server wrapper; searched gateway configuration and cached-agent responsibilities in `gateway/run.py` and `gateway/run_agent_cache.py`. Gateway turn execution, session rehydration and ACP lifecycle remain incomplete. This prevents cross-frontend equivalence claims. |
| Maintenance, extensions and evaluation | Enumerated `cron/`, `evals/`, `tools/`, `skills/`, `plugins/`, `providers/` and frontend paths in the tracked tree. These are available but not substantively inspected at this stage. Scheduler-driven use, extension boundaries and evaluation results cannot yet be characterized. |

The persistent-context component is materially relevant rather than incidental. The inspected prompt-building function explicitly distinguishes task-specific skills from across-session memory (SRC-1 `agent/prompt_builder.py`). Its function contract states:

> """Adapt store and skill-write guidance without widening what belongs in memory."""
> --- `agent/prompt_builder.py`

Background review is also shipped target responsibility, not an external maintenance service. The following passage establishes its declared design only; later analysis must trace the implementation before asserting actual write isolation or cache behavior (SRC-1 `agent/background_review.py`):

> """Background memory/skill review — fork the agent to evaluate the turn. After every turn
> ``AIAgent.run_conversation`` may spawn a daemon thread that replays the conversation snapshot in a
> forked :class:`AIAgent` and asks "should any skill/memory be saved or updated?". Writes go
> straight to the memory + skill stores; the main conversation and prompt cache are never touched.
> --- `agent/background_review.py`

External dependencies include model-provider endpoints, configured credentials, optional memory services, MCP servers, platform APIs and operating-system/tool backends. The source exposes provider, API mode, credentials, model, toolsets and session-database configuration at the agent constructor (SRC-1 `run_agent.py`); ACP startup imports the external `acp` protocol package (SRC-1 `acp_adapter/entry.py`). Only the repository-side integration is included. External implementations and deployments are excluded, preventing conclusions about their independent persistence, privacy, availability or correctness. User-installed configuration, user data and dynamically acquired skills are not frozen here; their actual contents and effects cannot be established.

There is no identified repository access gap. Uninspected files are pending inspection, not unavailable evidence. No target code, tests, examples or services were executed. The overall evidence tier is code-grounded because executable caller and delegation code was inspected; individual module comments and prompt text remain doctrine/design evidence. There is no observed-run or causal-experiment evidence, so this boundary supports neither operational reliability measurements nor claims that skill creation or memory improves outcomes.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/nousresearch/hermes-agent` | 0e427d788d253630d38a3a51cd76849e73cd6925 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/hermes-agent-bfb4bdc54d37/related-systems/nousresearch--hermes-agent`. Implementation: tracked top-level tree; script declarations in `pyproject.toml`; bounded inspection/search of `hermes_cli/main.py`, `hermes_cli/oneshot.py`, `agent/legacy_cli.py`, `run_agent.py`, `agent/turn_facade.py`, `agent/conversation_loop.py`, `agent/memory_manager.py`, `acp_adapter/entry.py`, `acp_adapter/server.py`, `gateway/run.py`, `gateway/run_agent_cache.py`. Doctrine/design: memory routing in `agent/prompt_builder.py`, review module description in `agent/background_review.py`, loop module description in `agent/conversation_loop.py`. | Implementation: [entry points](https://github.com/nousresearch/hermes-agent/blob/0e427d788d253630d38a3a51cd76849e73cd6925/pyproject.toml), [shipped caller](https://github.com/nousresearch/hermes-agent/blob/0e427d788d253630d38a3a51cd76849e73cd6925/hermes_cli/oneshot.py), [runtime facade](https://github.com/nousresearch/hermes-agent/blob/0e427d788d253630d38a3a51cd76849e73cd6925/agent/turn_facade.py). Doctrine/design: [prompt assembly](https://github.com/nousresearch/hermes-agent/blob/0e427d788d253630d38a3a51cd76849e73cd6925/agent/prompt_builder.py), [background review](https://github.com/nousresearch/hermes-agent/blob/0e427d788d253630d38a3a51cd76849e73cd6925/agent/background_review.py), [loop contract](https://github.com/nousresearch/hermes-agent/blob/0e427d788d253630d38a3a51cd76849e73cd6925/agent/conversation_loop.py). | No identified checkout access gap. Partial inspection limits are enumerated above; they prevent whole-system coverage and unqualified retention-loop claims. External services and user state are not captured. No observed operation or causal experiment is supplied. |
