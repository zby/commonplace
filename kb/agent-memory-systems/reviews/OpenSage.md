---
description: ADK-based agent framework where agents create subagents and tools at runtime, with Neo4j graph memory, Docker sandboxes, and RL training hooks — strongest reference for self-modifying agent topology
type: ../types/agent-memory-system-review.md
traits: [has-comparison, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-03-23"
---

# OpenSage

OpenSage (Open Self-programming Agent Generation Engine) is an open-source Python agent framework built on Google's ADK (Agent Development Kit). It was created by the opensage-agent organization and is oriented toward security analysis tasks — vulnerability detection, fuzzing, PoC generation, and code auditing. The framework's distinguishing pitch is "Agent Development 2.0": agents that dynamically create subagents, write their own tools, and manage their own memory at runtime, rather than executing fixed human-defined structures.

**Repository:** https://github.com/opensage-agent/OpenSage

## Core Ideas

**Agents can create subagents and tools at runtime.** The `DynamicAgentManager` lets the running agent call `create_subagent` to spawn new `OpenSageAgent` instances with specified tools, instructions, models, and skills. Created agents are persisted to disk as JSON metadata and can be reloaded across sessions. The `new_tool_creator` skill scaffolds new bash tool directories with `SKILL.md` frontmatter, so agents can also extend their own toolset. This is the core of the "self-programming" claim.

**Skills are filesystem-discovered bash/Python scripts described by SKILL.md.** Each skill lives in a directory under `bash_tools/` with a `SKILL.md` file containing YAML frontmatter (name, description, execution sandbox) and markdown documentation. The `ToolLoader` discovers skills at agent init time, parses their metadata, and generates a system prompt fragment listing available skills. Skills are executed inside Docker sandbox containers via `run_terminal_command`. The skill system is hierarchical: top-level groupings (coverage, fuzz, retrieval, static_analysis, neo4j) contain sub-skills.

**Two-tier memory: file-based and Neo4j graph-based.** File memory (`MemoryManagement.FILE`) gives each agent a `/mem/<agent_name>/` directory with `planning.md` (a living plan), per-session trajectory dumps, a cross-agent `topology.json`, and a shared `knowledge.jsonl` (JSONL key-value store for reusable knowledge). Graph memory (`MemoryManagement.DATABASE`) uses Neo4j with a domain-configurable schema: typed nodes (Function, Class, File, Question, Answer, Topic, Text), typed relationships, vector embeddings via Gemini, and multi-strategy search (embedding similarity, keyword, title browse). The `MemoryUpdateController` orchestrates entity extraction (LLM-driven), relationship discovery (embedding similarity), and graph persistence. The `MemoryObserverPlugin` watches tool results asynchronously and uses an LLM `StorageDecider` to determine what to store.

**Docker sandboxes provide execution isolation.** Each sandbox type (main, joern, codeql, neo4j, gdb_mcp, fuzz) runs as a Docker container with shared mount points (`/shared`, `/sandbox_scripts`, `/bash_tools`). Commands are non-persistent (each runs as a fresh `bash -c` process). The sandbox system handles container lifecycle, health checks, and resource cleanup per session.

**Agent ensemble enables parallel multi-agent exploration.** The `OpenSageEnsembleManager` discovers available agents (subagents, agent tools, dynamically created agents), manages thread-safety annotations per tool, and can run multiple agents in parallel on the same task. A message board (append-only JSONL with per-agent read cursors) provides inter-agent communication during ensemble runs.

**Plugin system bridges ADK plugins and Claude Code hooks.** Plugins intercept the tool execution lifecycle (before/after tool callbacks, model callbacks, event callbacks). Default plugins include a doom loop detector (blocks repeated identical tool calls), memory observer (async storage of tool results), tool response summarizer (LLM-compacts long tool outputs), build verifier, and read-before-edit enforcer. Claude Code hook JSON declarations are bridged into ADK plugin semantics with detailed mapping of which CC events have full, partial, or no ADK equivalents.

**Short-term memory records execution traces to Neo4j.** A monkey-patch on `BaseAgent.run_async` records `AgentRun` nodes, `Event` nodes (every streamed event), agent-to-agent call relationships, and session state. The `HistorySummarizerPlugin` compacts old events into summary nodes when history exceeds the context budget.

**RL training integration.** The `rl/` directory provides launch scripts for two RL frameworks: AReaL (ADK-based) and SLIME (Megatron-based), both active. This positions OpenSage as a framework that can close the loop between agent execution and weight updates — though the RL integration is scaffolding for external training pipelines, not an in-framework learning loop.

## Comparison with Our System

| Dimension | OpenSage | Commonplace |
|---|---|---|
| Primary purpose | Security analysis agent framework with runtime self-modification | Knowledge methodology for agent-operated knowledge bases |
| Storage substrate | Neo4j graph (long-term) + file-based `/mem` (planning/knowledge) + Neo4j traces (short-term) | Filesystem-first; markdown files under git |
| Agent model | Agents create/manage subagents and tools at runtime; parallel ensemble execution | Single-agent model; agent follows instructions and writes notes |
| Tool model | Filesystem-discovered skills (SKILL.md) + Python tools + MCP toolsets; agents can create new tools | Skills and instructions loaded from filesystem; no runtime tool creation |
| Memory write path | LLM-driven: StorageDecider evaluates tool results, EntityExtractor extracts entities, graph persistence | Human+agent writes markdown; git provides version history |
| Memory retrieval | Embedding similarity + keyword search + title browse; LLM selects strategy | `rg` keyword search + description scanning + link traversal |
| Validation | Doom loop detection, build verification plugins; no structural KB validation | Type system + `/validate` structural checks + semantic review |
| Knowledge structure | Flat nodes with type labels (Function, Question, Topic); relationships discovered by embedding similarity | Typed notes with templates, explicit link semantics, curated indexes |
| Linking | Implicit: embedding similarity discovers relationships; no explicit authored links | Explicit: markdown links with relationship semantics (extends, grounds, contradicts) |
| Learning model | RL training integration (AReaL, SLIME); file-based knowledge.jsonl accumulation; Neo4j trace mining | Manual curation; methodology-driven distillation |
| Execution isolation | Docker sandboxes per session with shared mount points | No isolation; agent reads/writes local filesystem |
| Inspectability | Neo4j requires API/UI to browse; file memory is readable | Fully inspectable — every note is a readable file |

**Where OpenSage is stronger.** Execution isolation via sandboxes is genuine infrastructure that commonplace lacks entirely. The dynamic subagent creation and ensemble coordination solve real multi-agent problems. The plugin system for intercepting tool execution (doom loop detection, response summarization, memory observation) is a mature lifecycle mechanism. RL training integration, even as scaffolding, opens a learning path we don't have.

**Where commonplace is stronger.** Knowledge structure. OpenSage's memory is flat typed nodes with embedding-discovered relationships — there are no curated indexes, no explicit link semantics, no progressive disclosure, no type templates. The knowledge.jsonl shared memory is a key-value store with no compositional structure. Our type system, link semantics, and curation methodology produce knowledge that can be traversed and reasoned about, not just retrieved. The validation and review pipeline (structural validation + semantic review) has no equivalent in OpenSage.

**The fundamental trade-off.** OpenSage invests in runtime self-modification (create agents, create tools, modify topology) and execution infrastructure (sandboxes, plugins, ensemble). Commonplace invests in knowledge quality (types, links, indexes, methodology, validation). OpenSage is a framework for building agents; commonplace is a framework for building knowledge. They solve different problems.

## Borrowable Ideas

**Plugin-based tool lifecycle hooks** — the pattern of intercepting before/after every tool call for doom loop detection, response summarization, memory observation, and build verification is immediately applicable. Our system could use a similar hook architecture for validation, link maintenance, or staleness detection triggered by tool use. *Ready to borrow as a pattern* — the specific implementation is ADK-dependent, but the architecture transfers.

**File-based planning.md as agent working memory** — each agent maintaining a `planning.md` file that it reads before work and updates after major steps is a simple, inspectable working memory pattern. This is close to our workshop layer concept but more operational. *Ready to borrow* — could be used as a session-scoped scratch file pattern within workshops.

**Doom loop detection** — short-circuiting when an agent makes the same tool call N times consecutively with identical arguments. Simple, effective, implementation-portable. *Ready to borrow now* — could be integrated into any tool-loop agent.

**SKILL.md as tool metadata** — using a markdown file with YAML frontmatter to describe each tool (name, description, execution sandbox, requirements, usage) is a clean convention for discoverable tools. The metadata is parsed at init time and injected into the system prompt. *Interesting but not directly borrowable* — our instructions/skills already serve this role with different conventions.

**Asynchronous memory observation** — the MemoryObserverPlugin's pattern of watching tool results in the background and using an LLM to decide what's worth storing is a plausible model for automated knowledge capture. *Needs a use case first* — the oracle quality for "what's worth storing" is unclear (the system uses a cheap LLM model for this decision).

## Curiosity Pass

**What property does "self-programming" claim to produce?** Autonomy — agents that can extend their own capabilities without human intervention. The mechanism is real: `create_subagent` creates actual running agents, and `new_tool_creator` scaffolds actual tool directories. But the quality of self-modification depends entirely on the LLM's judgment about what agents and tools to create. There is no validation gate on dynamically created agents — no equivalent of the application validators SAGE uses for memory writes. An agent can create a subagent with bad instructions and tools that don't work, and nothing structural prevents that. The self-modification mechanism exists; the self-modification oracle does not.

**Does the memory system transform data or just relocate it?** The graph memory pipeline does transform: the `EntityExtractor` uses an LLM to extract structured entities (functions, topics, questions) from unstructured tool results, and the `RelationshipDiscoverer` uses embedding similarity to find connections. This is genuine extraction, not just storage. However, the file memory system (`knowledge.jsonl`) is pure relocation: the agent writes key-value pairs, and they sit there unchanged. There is no consolidation, no synthesis, no lifecycle for file-memory entries.

**What's the simpler alternative for the Neo4j memory?** A vector database with typed metadata fields achieves nearly identical behavior to the graph memory's current usage. The graph structure (Neo4j) is justified by the entity-relationship model, but in practice the relationships are discovered by embedding similarity rather than explicit authoring. The graph edges add little that vector search with metadata filtering wouldn't provide. The graph would earn its complexity if relationships were used for multi-hop traversal during retrieval — but the search strategies (embedding search, keyword search, title browse) don't traverse relationships.

**What could the ensemble system actually achieve, even if it works perfectly?** Parallel exploration — multiple agents trying different approaches simultaneously. The message board provides inter-agent communication, and the ensemble manager does have LLM-driven result aggregation: after parallel runs complete, a summarization model synthesizes responses, identifies consensus/disagreement, and produces a merged answer. This is more than "pick the best result" but the aggregation is a single post-hoc LLM call, not structured consensus. There is no mechanism for agents to build on each other's intermediate findings during an ensemble run — the aggregation happens only after all agents complete.

**The "Agent Development 2.0" framing.** The introduction positions OpenSage as a paradigm shift from "agents executing predefined structures" to "agents autonomously building and managing structures." Reading the code, the actual capability is more modest: agents can create subagents with specified configurations and scaffold new tool directories. The agent topology is runtime-modifiable, but the modification decisions are still LLM judgment calls without structural guardrails. This is useful infrastructure, but calling it a paradigm shift overstates the mechanism relative to what it can achieve without better modification oracles.

**The security domain focus shapes the architecture.** OpenSage is built for vulnerability detection, fuzzing, and PoC generation. The sandbox system, the security-focused tool categories (Joern, CodeQL, GDB, AFL++), and the benchmark suite (CyberGym, SWE-bench Pro, SeCodePLT) all serve this domain. The general-purpose agent framework claims are real but the implementation is optimized for security workflows. The memory system stores code entities (Function, Class, File) and Q&A pairs, not general knowledge.

## What to Watch

- **Does the file memory evolve beyond key-value?** The `knowledge.jsonl` shared memory is the simplest possible artifact store. If OpenSage adds consolidation, schema enforcement, or lifecycle management for file memory, that would be a meaningful signal.
- **Does dynamic agent creation develop quality gates?** Currently any agent can create any subagent with no validation. If they add structural or behavioral validation for dynamically created agents, that addresses the missing oracle problem.
- **How does the RL integration develop?** The AReaL and SLIME scaffolding positions OpenSage to close the trace-to-weights loop. If the RL training produces measurably better agents on their security benchmarks, that's a concrete data point for weight-learning from agent traces.
- **Does the graph memory justify its complexity?** Currently the Neo4j graph is used primarily for embedding search with node types. If multi-hop graph traversal or relationship-based reasoning becomes a real retrieval strategy, the graph substrate earns its cost over simpler vector stores.

---

Relevant Notes:

- [bounded-context orchestration model](../../notes/bounded-context-orchestration-model.md) — extends: OpenSage's session-scoped sandbox management and ensemble coordination are a production implementation of bounded-context orchestration with real isolation
- [agent runtimes decompose into scheduler, context engine, and execution substrate](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — grounds: OpenSage's architecture maps cleanly to this decomposition: ADK runner as scheduler, system prompt injection + memory search as context engine, Docker sandboxes as execution substrate
- [claw learning loops must improve action capacity not just retrieval](../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) — extends: OpenSage addresses storage and retrieval but also opens a path to weight-learning via RL integration, making it one of the few reviewed systems that bridges artifact-learning and weight-learning
- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: OpenSage's Neo4j trace recording plus RL training integration is a concrete pipeline from execution traces to weight updates, placing it on the weight-learning end of the survey
- [inspectable substrate not supervision defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — contrasts: OpenSage's file memory is inspectable but its Neo4j graph memory is opaque without API mediation; the system trades inspectability for richer structure
- [skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — parallels: OpenSage's SKILL.md system is an independent convergence on filesystem-discovered, metadata-described callable procedures
- [ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — contrasts: OpenSage's memory observer plugin and knowledge.jsonl are explicit anti-ephemerality measures, though knowledge.jsonl has no consolidation lifecycle
