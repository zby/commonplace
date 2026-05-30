---
description: "OpenSage review: ADK agent framework with dynamic subagents, generated Skills, file memory, Neo4j graph memory, trace logging, plugins, and RL adapters"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# OpenSage

OpenSage, from opensage-agent, is an ADK-based agent framework for software-engineering and security agents. The inspected repository implements dynamic subagent creation, dynamically loaded and generated bash-tool Skills, sandboxed execution, optional file or Neo4j-backed memory, plugin callbacks, session persistence, evaluation trace export, and adapters for RL training systems. Its memory system is not one substrate; it is a bundle of retained artifacts with different authority: prompt-visible files, dynamic agent metadata, graph memory, raw execution traces, generated tools, plugin outputs, and external training trajectories.

**Repository:** https://github.com/opensage-agent/OpenSage

**Reviewed commit:** [481b4344f3d07de42082f367ecda4381f81c22c8](https://github.com/opensage-agent/OpenSage/commit/481b4344f3d07de42082f367ecda4381f81c22c8)

**Last checked:** 2026-05-16

## Core Ideas

**OpenSage extends ADK agents with session-scoped infrastructure.** Each `OpenSageSession` owns configuration, dynamic agents, sandboxes, Neo4j clients, ensemble management, and message boards for one session ([src/opensage/session/opensage_session.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_session.py)). The CLI and evaluation paths create these sessions, load an agent directory's `mk_agent(...)`, initialize required sandboxes, load plugins, and run ADK runners ([src/opensage/cli/opensage_cli.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/cli/opensage_cli.py), [src/opensage/evaluation/base.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/base.py)). The retained state is therefore session-bound by default, even when some surfaces persist past process exit.

**Dynamic subagents are system-definition artifacts stored as JSON metadata.** `create_subagent(...)` lets an agent create another `OpenSageAgent` with a chosen name, instruction, model, Python tools/toolsets, and enabled bash Skills; `call_subagent_as_tool(...)` wraps the created agent as an ADK `AgentTool` ([src/opensage/toolbox/general/dynamic_subagent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/toolbox/general/dynamic_subagent.py)). `DynamicAgentManager` persists metadata as `*_metadata.json` under `agent_storage_path` or `~/.local/opensage/dynamic_agents`, including instruction-bearing config, tool names, creator, status, and enabled Skills ([src/opensage/session/opensage_dynamic_agent_manager.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_dynamic_agent_manager.py)). Their representational form is mixed: prose instructions plus symbolic tool/model configuration. Their behavioral authority is strong because they become executable agent definitions.

**Bash-tool Skills are prompt-injected executable affordances, and agents can scaffold new ones.** `ToolLoader` scans `src/opensage/bash_tools` and `~/.local/opensage/bash_tools` for `SKILL.md` files, filters by `enabled_skills`, extracts metadata, and appends tool descriptions plus usage policy and sandbox layout to the agent instruction ([src/opensage/agents/opensage_agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/agents/opensage_agent.py)). The `new_tool_creator` Skill scaffolds a new Skill under `bash_tools/new_tools/<category>/<tool-name>` with execution-sandbox and JSON-return metadata ([src/opensage/bash_tools/new_tool_creator/SKILL.md](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/bash_tools/new_tool_creator/SKILL.md), [src/opensage/bash_tools/new_tool_creator/scripts/create_new_tool.sh](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/bash_tools/new_tool_creator/scripts/create_new_tool.sh)). Generated Skills are symbolic system-definition artifacts; the source code shows scaffolding and prompt exposure, not a reviewed promotion pipeline.

**File memory is a sandbox-local working-memory layout, not a typed KB.** When file memory is active, the agent prompt describes `/mem/<agent_name>/planning.md`, per-session `session_<session_id>.json` dumps, `/mem/topology.json`, and `/mem/shared/knowledge.jsonl` with `key` and `value` fields ([src/opensage/agents/opensage_agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/agents/opensage_agent.py)). The Neo4j logging patch also initializes the `/mem` layout, persists full ADK session JSON after each run, and records agent topology independent of whether Neo4j logging is enabled ([src/opensage/patches/neo4j_logging.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/patches/neo4j_logging.py)). The storage substrate is files mounted into the main sandbox; the representational form is prose plus symbolic JSON; lineage is mostly by session ID and topology fields.

**Neo4j memory has two roles: execution history and long-term graph search.** With Neo4j logging enabled, the patch records agent runs, events, raw tool responses, summarized events, call relationships, and session state to a history graph; history-management tools can list events or retrieve full raw tool responses behind summaries ([src/opensage/patches/neo4j_logging.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/patches/neo4j_logging.py), [src/opensage/toolbox/general/history_management.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/toolbox/general/history_management.py)). Separately, the memory module extracts entities from text, Q&A, or code, stores nodes and relationships in Neo4j, creates exact, full-text, and vector indexes, and exposes `search_memory(...)` through a memory-management agent when `MemoryManagement.DATABASE` is selected ([src/opensage/memory/update/update_controller.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/update/update_controller.py), [src/opensage/memory/update/graph_operations.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/update/graph_operations.py), [src/opensage/memory/search_tool.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search_tool.py), [src/opensage/util_agents/memory_management_agent/agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/util_agents/memory_management_agent/agent.py)).

**Plugins are an authority path for automatic trace processing.** The plugin loader resolves default, user-local, custom, and agent-local ADK plugins or Claude Code hook JSON files from config ([src/opensage/plugins/__init__.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/plugins/__init__.py), [src/opensage/config/config_dataclass.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/config/config_dataclass.py)). The `memory_observer_plugin` watches tool results, asks an LLM storage decider whether a result is worth storing, optionally saves full long outputs to a sandbox file, and writes extracted knowledge to the memory graph asynchronously ([src/opensage/plugins/default/adk_plugins/memory_observer_plugin.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/plugins/default/adk_plugins/memory_observer_plugin.py), [src/opensage/memory/storage_decider.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/storage_decider.py)). This is the clearest implemented trace-to-memory loop.

**RL hooks route agent trajectories into external learning systems.** The AReaL adapter runs an OpenSage evaluation task with an ADK-compatible AReaL model, computes a benchmark reward, and returns reward-bearing result metadata; the SLIME adapter creates a `SlimeLlm`, runs the OpenSage task, and builds a SLIME sample with token/loss-mask data for GRPO-style training ([src/opensage/evaluation/rl_adapters/adapters/areal.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/areal.py), [src/opensage/evaluation/rl_adapters/adapters/slime.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/slime.py), [rl/README.md](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/rl/README.md)). OpenSage supplies rollout scaffolding and reward plumbing; model-artifact storage and weight updates live in the external RL frameworks.

## Comparison with Our System

| Dimension | OpenSage | Commonplace |
|---|---|---|
| Primary purpose | Runtime framework for constructing and running ADK agents, tools, sandboxes, evaluations, and training hooks | Agent-operated methodology KB for durable notes, instructions, reviews, ADRs, validation, and indexes |
| Storage substrate | Sandbox files under `/mem`, dynamic-agent metadata JSON, Neo4j history and memory graphs, local web/eval session snapshots, generated Skill directories, external RL artifacts | Git-tracked Markdown, schemas, source snapshots, generated indexes, review outputs, scripts |
| Representational form | Mixed: prose instructions and memory entries, symbolic TOML/JSON/Cypher/Skill metadata, graph nodes/relationships, embeddings/vector indexes, external model-training traces | Typed prose and frontmatter, symbolic links/schemas/commands, generated indexes, validation code |
| Lineage | Session IDs, topology records, tool args, raw tool responses, event IDs, output files, and result directories; generated agents/tools and graph summaries have thinner source-to-artifact review state | Source-pinned artifacts, authored citations, statuses, replacement archives, validation, and review gates |
| Activation | Prompt injection, ADK tools, subagent calls, memory-management agent, plugin callbacks, Neo4j search, sandbox-visible files, RL rollout adapters | `rg`, indexes, titles/descriptions, authored links, skills, instructions, validation and review workflows |
| Behavioral authority | Agent definitions and Skills instruct execution; retrieved graph/file memory advises or conditions agents; plugins can automatically write memory; RL adapters feed learning loops | Knowledge-artifact context plus stronger system-definition artifacts such as instructions, validators, commands, schemas, and review workflows |

OpenSage is much more aggressive than commonplace about letting the runtime alter its own operative surface. A running agent can create subagents with new instructions, expose a different set of tools, scaffold new bash Skills, write shared knowledge files, and trigger plugin-mediated storage. Those are powerful system-definition-artifact paths because they can change which future tools exist and which instructions future agents follow.

Commonplace is more conservative about authority and lifecycle. A note, instruction, or schema is durable because it is reviewable in Git, typed, linked, validated, and replaceable. OpenSage has many behavior-changing retained artifacts, but they are spread across sandbox files, JSON metadata, graph databases, runtime plugin state, and external training systems. That gives OpenSage strong online adaptation but weaker inspectable governance.

The closest overlap is the distinction between working memory and library memory. OpenSage's `/mem/<agent>/planning.md`, `session_<id>.json`, topology, and message boards are useful workshop-like state: they keep a session coordinated and resumable. Its Neo4j memory and generated Skills are closer to library candidates, but the source does not show a promotion boundary with citations, human or semantic review, contradiction handling, retirement, or explicit authority escalation.

## Borrowable Ideas

**Treat generated agents as retained artifacts with explicit contracts.** OpenSage makes subagent definitions durable enough to list, search, call, and optionally persist. A commonplace analogue would require frontmatter, source trace links, review status, allowed tools, and expiration before a generated worker can become reusable infrastructure.

**Keep scratch memory, graph memory, and generated tools separate.** OpenSage's split between `/mem` files, Neo4j graph memory, dynamic-agent metadata, and Skill directories is worth borrowing as vocabulary. Commonplace should preserve that separation rather than flattening every retained surface into "memory."

**Use plugin callbacks as capture points, not authority endpoints.** The memory observer plugin shows a practical place to catch valuable tool results. For commonplace, the callback should create review candidates or source snapshots before promoting anything into notes, instructions, or validators.

**Borrow topology tracking for workshop state.** `/mem/topology.json` records agent-call structure in a form later agents can inspect. A commonplace workshop could use a similar lightweight topology or run manifest while keeping the library layer Git-reviewed.

**Do not borrow automatic generated-tool activation without review.** A generated Skill can change the action space more strongly than a retrieved note. In commonplace terms, that is system-definition authority and should pass through a stricter promotion path.

## Trace-derived learning placement

**Trace source.** OpenSage qualifies as trace-derived learning. It captures ADK session events, tool calls, tool responses, subagent calls, topology records, per-session JSON dumps, evaluation session traces, benchmark outputs, and optional Neo4j history graphs ([src/opensage/patches/neo4j_logging.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/patches/neo4j_logging.py), [src/opensage/evaluation/base.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/base.py)). Tool results are also consumed by the memory observer plugin as online trace signals ([src/opensage/plugins/default/adk_plugins/memory_observer_plugin.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/plugins/default/adk_plugins/memory_observer_plugin.py)).

**Extraction.** There are several extraction paths. The history path stores raw or summarized events and raw tool responses. The memory observer path asks `StorageDecider` whether a tool result contains durable information, then stores a summary or result content through `MemoryUpdateController`. The memory controller extracts entities, topics, code references, embeddings, and relationships. The RL path converts completed agent interactions into reward-bearing samples or token/loss-mask training data for AReaL or SLIME ([src/opensage/memory/storage_decider.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/storage_decider.py), [src/opensage/memory/update/entity_extractor.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/update/entity_extractor.py), [src/opensage/evaluation/rl_adapters/adapters/slime.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/slime.py)).

**Storage substrate.** Raw traces persist as sandbox `/mem` files, evaluation output files, local web snapshots, and optional Neo4j history databases. Distilled graph memory persists in Neo4j memory databases with regular, full-text, and vector indexes. Dynamic subagents persist as metadata JSON. Generated tools persist as Skill directories. RL interactions are passed outward to AReaL or SLIME rather than stored as OpenSage-owned weights ([src/opensage/cli/opensage_cli.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/cli/opensage_cli.py), [src/opensage/memory/update/graph_operations.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/update/graph_operations.py), [src/opensage/session/opensage_dynamic_agent_manager.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_dynamic_agent_manager.py)).

**Representational form.** Raw session traces are symbolic JSON wrapped around prose messages and tool payloads. `/mem/shared/knowledge.jsonl` is prose knowledge in JSONL records. Neo4j memory is mixed: symbolic node labels and relationships, prose text fields, and distributed-parametric embeddings. Generated agents and Skills are symbolic/prose system definitions. RL adapters produce or forward distributed-parametric learning inputs for external model updates, but OpenSage itself does not retain the learned weights.

**Lineage.** Lineage is strongest for raw traces because session IDs, event IDs, tool args, raw responses, session JSON, and topology calls remain inspectable. It weakens after storage decisions and entity extraction: graph nodes may include source metadata such as tool name, args, confidence, decision reason, session ID, hashes, and timestamps, but they are not managed as source-cited reviewed artifacts with regeneration rules or contradiction state. Generated subagents and Skills preserve creator/config or filesystem location, not a reviewed derivation chain.

**Behavioral authority.** Raw traces are knowledge artifacts when inspected as evidence. `/mem/shared/knowledge.jsonl` and graph search results are knowledge artifacts when retrieved as advice or context. Dynamic subagents, generated Skills, plugin configs, memory observer decisions, and injected tool/skill prompt sections are system-definition artifacts because they instruct, route, configure, or write behavior-changing surfaces. RL adapter outputs have learning authority once consumed by AReaL or SLIME.

**Scope.** File memory is per agent name and session-visible through the main sandbox, with `/mem/shared` reserved for cross-agent high-level knowledge. Dynamic agents are session-manager objects with optional metadata persistence. Neo4j history and memory are session/config scoped. Evaluation traces are per benchmark task. RL outputs are per external training run.

**Timing.** File memory and topology are updated online during runs. Memory observer storage is online after tool callbacks, often fire-and-forget. Evaluation trace export is post-run. RL adapters operate during rollout generation and hand traces/rewards to training frameworks.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), OpenSage spans several branches: raw execution trace retention, trace-to-graph-memory extraction, trace-to-generated-system-definition through dynamic agents and generated Skills, and trace-to-external-weight-learning through RL adapters. It strengthens the survey claim that trace-derived learning must be split by artifact authority: a session trace, a graph memory node, a generated Skill, and a reward-labeled rollout are not the same kind of memory.

## Takeaways

**OpenSage is an agent-runtime memory system, not just a graph memory package.** Its behavior-changing retained artifacts include agent definitions, tool metadata, prompt-injected Skill descriptions, sandbox files, graph records, event traces, plugins, and RL samples.

**Its strongest design move is making agent topology and tools first-class runtime objects.** Dynamic subagents and Skills are not merely retrieved context; they are executable changes to the agent's future action space.

**The memory vocabulary needs strict separation.** File memory, raw traces, Neo4j history, Neo4j long-term memory, generated Skills, dynamic-agent metadata, and RL trajectories have different storage substrates, representational forms, lineage, and behavioral authority.

**The trace-derived loop is real but unevenly governed.** The memory observer plugin is a concrete automatic trace-to-memory mechanism. The generated agent/tool paths are powerful, but the code does not show a review or promotion policy before those system-definition artifacts become active.

**RL support is scaffolding, not an internal learned-memory store.** OpenSage adapts agent evaluation to AReaL and SLIME so traces and rewards can train models elsewhere. It should be classified as a learning-input channel unless the external training artifact is also reviewed.

## Curiosity Pass

The most surprising detail is that file memory is initialized by the Neo4j logging patch even when file topology persistence is independent of the Neo4j logging toggle. That makes the patch a general trace/runtime persistence hook, not only a database logger.

The README's "hierarchical memory" phrase is partly true, but the hierarchy is distributed across runtime conventions rather than one coherent memory module. `/mem` files, Neo4j history, Neo4j long-term memory, dynamic agents, generated tools, plugins, and RL adapters each have their own lifecycle.

The `memory_management_agent` is more of a mediated query surface than a complete memory governance layer. It can inspect history and search long-term memory, but the reviewed code does not turn it into a curator with promotion, retirement, and contradiction duties.

The generated-tool path may be more behavior-shaping than the graph memory path. A graph memory can advise an agent; a Skill can add an executable operation that future prompts are explicitly told to prefer.

## Open Questions

- Should generated subagents and Skills carry explicit source trace IDs, creator task, review status, and expiration metadata before reuse?
- Should `/mem/shared/knowledge.jsonl` grow a schema with provenance, confidence, status, and authority, or remain lightweight working memory?
- How are contradictory graph memories detected, retired, or superseded after the memory observer stores summaries?
- Should memory observer writes be blocked, staged, or reviewed when they would influence future agent behavior beyond the current session?
- Does dynamic agent metadata persistence currently reload in production flows, given the on-demand loader code path is present but mostly commented?
- Which trace artifacts are canonical after summarization: raw tool response nodes, summarized events, session JSON, or graph memory entities?
- How should RL-generated model behavior be linked back to the traces, rewards, and benchmark versions that produced it?

## What to Watch

- Whether dynamic-agent metadata loading becomes active and reliable across sessions.
- Whether generated Skills gain provenance, tests, review status, or installation scopes.
- Whether Neo4j memory adds contradiction handling, source trace links, and retirement policies.
- Whether memory observer outputs are staged for review instead of written directly into long-term graph memory.
- Whether AReaL or SLIME training artifacts become first-class OpenSage artifacts with lineage back to rollout traces and reward functions.
- Whether `/mem/shared/knowledge.jsonl` evolves from lightweight shared notes into a typed knowledge store.

## Bottom Line

OpenSage is a rich example of runtime context engineering: it can create agents, generate tools, persist file and graph memory, record traces, summarize tool output, and feed rollouts into RL frameworks. Commonplace should borrow its separation of runtime surfaces and its willingness to make tools and agents explicit artifacts, but not its default authority boundary. Durable KB knowledge needs source-grounded lineage, validation, review, contradiction handling, and clear promotion from trace evidence to system definition.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: OpenSage spans raw trace retention, trace-to-graph memory, trace-to-generated tools/agents, and trace-to-external RL inputs.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: OpenSage needs separate substrate, form, lineage, and authority labels for files, graph nodes, agent configs, Skills, plugins, and RL samples.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: session traces, graph search results, and shared knowledge files advise later agents as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: dynamic agents, Skills, plugin callbacks, and RL adapters can instruct, route, configure, or train behavior.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - compares-with: OpenSage's `/mem`, topology, and message boards are closer to workshop state than durable library artifacts.
