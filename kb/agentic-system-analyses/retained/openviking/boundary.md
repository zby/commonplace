---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenViking's context database and shipped consumers at commit 5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b, with partial loop coverage."
run-id: AAS-2026-10-14-openviking-7b5b57541af5-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/volcengine/OpenViking
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/openviking-7b5b57541af5/related-systems/volcengine--OpenViking
  revision: "5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b"
  sha256: null
---

# OpenViking boundary

## Boundary and evidence

This run analyses OpenViking as a system for retaining and retrieving agent context, not merely as its Python client API. Its intended use is to explain how resources, memories and skills are represented, produced, maintained and returned to callers, and where model-dependent processing enters that process. The target's own description supplies the intended role, not evidence of effectiveness (SRC-1, `README.md`):

> OpenViking is an open-source context database for AI agents — one filesystem for everything an agent knows: knowledge, memory, and skills.
> --- `README.md`

The target class is **memory/knowledge/context-engineering system**. It is in scope even when an external agent owns the enclosing conversation loop: the target itself performs model-dependent context processing. For example, the inspected intent analyzer builds a retrieval prompt, calls the configured planner and parses its response into queries (SRC-1, `openviking/retrieve/intent_analyzer.py`). The corresponding shipped prompt declares its task (SRC-1, `openviking/prompts/templates/retrieval/intent_analysis.yaml`):

> You are OpenViking's context query planner. Given the session context and the current message, decide what context information is missing and emit retrieval queries to fill the gap.
> --- `openviking/prompts/templates/retrieval/intent_analysis.yaml`

> response = await query_planner.get_completion_async(prompt)
> --- `openviking/retrieve/intent_analyzer.py`

### Functional scope and initial tracing

The functional boundary includes the repository's shipped server, storage and retrieval machinery, session processing, prompts, maintenance paths, clients, plugins, gateway and VikingBot integration. Shipped callers are not classified as external simply because they invoke the service. Repository tests and evaluators are available as source evidence about their specified conditions; they are not observed runs in this analysis.

The boundary kind is **complete artifact, partial loop**. The complete repository is frozen, but the initial inspection establishes selected production and consumption paths rather than exhaustive coverage of all shipped loops. It does not establish a whole-system coverage claim. In particular, gateway processing, native storage, alternative host integrations, bot execution and evaluator internals remain incompletely traced. These are available but not yet inspected in depth, not access gaps and not functional exclusions. Their untraced behavior prevents conclusions about uniform lifecycle guarantees across every deployment and consumer.

| Area | Initial inspection and role | Coverage limit |
|---|---|---|
| Package and server entry | SRC-1, `pyproject.toml` declares `ov`, `openviking`, `openviking-server`, `openviking-gateway` and `vikingbot`; `openviking_cli/server_bootstrap.py` forwards normal startup to `openviking.server.bootstrap`; `openviking/server/bootstrap.py`, `openviking/server/app.py` and `openviking/service/core.py` were inspected or searched for application assembly and service wiring. | Setup and route registration establish shipped surfaces, not complete behavior of every route or startup mode. |
| Session production and maintenance | SRC-1, `openviking/service/session_service.py` delegates commit to the session and exposes extraction; `openviking/session/session.py` describes archive preparation and persistent phase-two processing; `openviking/session/compressor_v3.py` resolves the account's model configuration, prepares extraction context and runs the extraction orchestrator. | Selected commit and extraction ranges were inspected; queue recovery, memory admission, merge and deletion internals are not yet fully traced. |
| Retrieval | SRC-1, `openviking/service/search_service.py` obtains optional session context and delegates search/find to VikingFS; `openviking/retrieve/intent_analyzer.py` and `openviking/prompts/templates/retrieval/intent_analysis.yaml` implement the planner interface. | Initial inspection does not establish end-to-end ranking, index consistency, budget assembly or backend equivalence. |
| Instruction-driven consumer | SRC-1, `agent-plugins/skills/openviking-memory/SKILL.md` specifies recall, persistence and maintenance responsibilities for an MCP client. | This is a shipped instruction, not proof a host follows it or that every deployment exposes every optional tool. |
| Shipped automatic consumers | SRC-1, `examples/opencode-plugin/index.mjs` registers recall and session-flush hooks; `bot/vikingbot/agent/context.py` conditionally retrieves memory and appends it to context; `bot/vikingbot/agent/memory.py` was searched for retrieval, local persistence and formatting paths. | Plugin implementation below the hook calls and the complete bot persistence/reload loop are not yet established. These callers remain inside the target boundary. |
| Additional entry and evaluation paths | SRC-1, `openviking_gateway/cli.py` was inspected for configuration and standalone application construction. The tracked tree identifies `benchmark/`, `tests/`, `crates/`, `src/`, `sdk/`, `npm/`, `web-studio/` and further examples. | Gateway internals, evaluator protocols, native implementations and other client paths are available but not yet inspected in depth. Their presence supplies no efficacy, safety or reliability result. |

The session implementation's own phase description is more specific than the service-level description of background work. It identifies a persistent queue, not merely an unretained task (SRC-1, `openviking/session/session.py`):

> Phase 2 (Memory extraction): Runs through the persistent QueueFS queue.
> --- `openviking/session/session.py`

The consumer boundary matters because automatic recall is not universal. The bundled MCP skill assigns responsibility to its host agent (SRC-1, `agent-plugins/skills/openviking-memory/SKILL.md`):

> This client has no lifecycle hooks, so nothing is recalled or captured
> automatically — you drive both halves of the loop with the `openviking` MCP
> tools.
> --- `agent-plugins/skills/openviking-memory/SKILL.md`

By contrast, the OpenCode plugin's inspected hooks invoke session injection, recall and commit-oriented flushes, and VikingBot's context builder calls its memory store when OpenViking tools are enabled (SRC-1, `examples/opencode-plugin/index.mjs`; `bot/vikingbot/agent/context.py`). Those are shipped target responsibilities; the external OpenCode runtime and its actual scheduling behavior are not thereby frozen.

### Frozen evidence and exclusions

The sole source is SRC-1 at **5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b**, with applicability cutoff **2026-10-14**. The acquired checkout's HEAD was checked against that pin, and `git status --short` returned no changes. The source object above is the acquired object unchanged. No additional repository, live documentation page, hosted demo or mutable provider response is part of the evidence set.

The overall evidence tier is **code-grounded**: source inspection supports implementation claims, while README and prompt/skill text support declared intent and contracts. No target, tests, examples or model calls were executed. No observed run or causal experiment is registered. Benchmark claims in the README therefore remain attributed claims rather than reproduced results.

External dependencies include model providers and the configured model implementations, package dependencies, deployment-specific storage/services and enclosing third-party agent runtimes. The package declares model and service dependencies in SRC-1, `pyproject.toml`; the extraction and retrieval interfaces pass work to configured model handles in `openviking/session/compressor_v3.py` and `openviking/retrieve/intent_analyzer.py`. Their external implementations and live operation are excluded: this prevents conclusions about actual model quality, production latency, service availability, third-party host compliance or deployed security. Hosted OpenViking service behavior is likewise not established by this repository pin. Later changes after the frozen revision are excluded, preventing claims about the current moving branch or later releases. No required source access gap was encountered.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/volcengine/OpenViking` | 5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/openviking-7b5b57541af5/related-systems/volcengine--OpenViking`. Implementation: tracked top-level tree; entry declarations in `pyproject.toml`; startup forwarding in `openviking_cli/server_bootstrap.py`; selected ranges/searches in `openviking/server/bootstrap.py`, `openviking/server/app.py`, `openviking/service/core.py`, `openviking/service/session_service.py`, `openviking/session/session.py`, `openviking/session/compressor_v3.py`, `openviking/service/search_service.py`, `openviking/retrieve/intent_analyzer.py`, `openviking_gateway/cli.py`, `examples/opencode-plugin/index.mjs`, `bot/vikingbot/agent/context.py` and `bot/vikingbot/agent/memory.py`. Doctrine/design: introductory README, retrieval prompt and MCP memory skill. Reported operation: README benchmark statements, not independently verified. | Implementation: [entry declarations](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/pyproject.toml), [session commit](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/openviking/session/session.py), [planner](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/openviking/retrieve/intent_analyzer.py), [plugin hooks](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/examples/opencode-plugin/index.mjs). Doctrine/design: [retrieval prompt](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/openviking/prompts/templates/retrieval/intent_analysis.yaml), [memory skill](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/agent-plugins/skills/openviking-memory/SKILL.md). Reported operation: [README](https://github.com/volcengine/OpenViking/blob/5242d28d7792411e1a6eeecdc2b1d94d7fc98e6b/README.md). | No repository access gap. Initial inspection is partial, as detailed above; listed paths are not an allowlist. No observed execution, provider internals or deployed host evidence: cannot establish actual effectiveness, fault recovery or operational guarantees. |
