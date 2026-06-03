---
description: "OpenSage review: dynamic subagents, sandbox/file memory, generated Skills, Neo4j history/memory, plugins, and RL adapters"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# OpenSage

OpenSage, by opensage-agent/OpenSage, is a Python agent framework on top of Google ADK for software-engineering agents that can create subagents, use sandboxed tools, scaffold new bash-tool Skills, persist session and sandbox state, log execution traces, and optionally extract long-term memory into Neo4j. Its memory design is not one substrate: it combines ADK session history, sandbox files under `/mem`, dynamic-agent metadata, generated `SKILL.md` tool packages, Neo4j history and memory databases, plugin-produced summaries and guards, benchmark output traces, and RL rollout adapters.

**Repository:** https://github.com/opensage-agent/OpenSage

**Reviewed commit:** [481b4344f3d07de42082f367ecda4381f81c22c8](https://github.com/opensage-agent/OpenSage/commit/481b4344f3d07de42082f367ecda4381f81c22c8)

**Last checked:** 2026-06-02

## Core Ideas

**Agents can create other agents with retained metadata.** The `create_subagent` tool validates a requested model, Python tools/toolsets, baseline tools, and `enabled_skills`, then asks the session's `DynamicAgentManager` to create and persist an `AgentMetadata` JSON record under the configured storage path, defaulting to `~/.local/opensage/dynamic_agents` ([dynamic_subagent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/toolbox/general/dynamic_subagent.py), [opensage_dynamic_agent_manager.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_dynamic_agent_manager.py)). The restore path is not as strong as the persistence story sounds: `_load_persisted_agents_on_demand` currently returns after setup and has its file-loading loop commented out, so persistent metadata is implemented, but reliable cross-session resurrection is limited in the inspected code.

**Skills are prompt-visible tool packages, and agents can scaffold new ones.** `ToolLoader` reads `SKILL.md` frontmatter and markdown from `src/opensage/bash_tools` and user-local tool roots, filters by `enabled_skills`, and appends a generated tool list plus a tool-usage policy to the agent instruction ([opensage_agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/agents/opensage_agent.py)). The built-in `new_tool_creator` Skill scaffolds new Skills only under `bash_tools/new_tools/`, generating `SKILL.md` plus a script template ([init_skill.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/bash_tools/new_tool_creator/init_skill.py), [create_new_tool.sh](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/bash_tools/new_tool_creator/scripts/create_new_tool.sh)). This is behavior-shaping memory in the form of executable/prose tool packages, not graph memory.

**Sandbox file memory is an instructed workspace convention.** When required sandboxes exist, OpenSage injects a `/mem` layout into the prompt: `/mem/<agent_name>/planning.md`, per-session JSON dumps, `/mem/topology.json`, and shared `/mem/shared/knowledge.jsonl` with a small schema. The same prompt tells the agent to read/update planning files and curate shared knowledge ([opensage_agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/agents/opensage_agent.py)). The Neo4j logging patch independently creates those memory folders and writes `session_<session_id>.json` and topology records in the main sandbox ([neo4j_logging.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/patches/neo4j_logging.py)).

**Neo4j is split into history, analysis, and long-term memory roles.** The Neo4j client manager maps `history`, `analysis`, and `memory` client types to separate database names ([opensage_neo4j_client_manager.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_neo4j_client_manager.py)). History logging records `AgentRun`, `Event`, `RawToolResponse`, summary relations, session state, and agent-call relations ([neo4j_history_management.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/utils/neo4j_history_management.py)). Long-term memory is separate: `memory_observer_plugin` observes tool outputs, asks `StorageDecider` whether to store them, then `MemoryUpdateController` extracts entities/relationships and writes them to the `memory` database with embeddings and indexes ([memory_observer_plugin.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/plugins/default/adk_plugins/memory_observer_plugin.py), [storage_decider.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/storage_decider.py), [update_controller.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/update/update_controller.py)).

**Context efficiency is handled by compaction, output summarization, and delegation, not by one retrieval budget.** The history summarizer plugin triggers when the folded event view exceeds the configured character budget, creates a compaction event, and can record a history-summary node in Neo4j ([summarization.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/features/summarization.py)). Tool-response summarization saves long outputs to sandbox files and replaces the returned result with a summary and file pointer. Dynamic subagents offer context isolation by running a child ADK runner with its own temporary session, while explicit `search_memory` uses strategy selection and top-k limits for long-term memory pull ([search_tool.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search_tool.py), [search_controller.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search/search_controller.py)).

**Evaluation and RL adapters turn trajectories into training/evaluation payloads.** Evaluation collects sandbox outputs, exports the Neo4j history database, and writes `session_trace.json` plus metadata per task ([base.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/base.py)). The AReaL adapter runs an OpenSage evaluation with an ADK-compatible RL model and returns reward-bearing results; the SLIME adapter injects `SlimeLlm`, tracks tokens/loss masks, computes rewards, and updates the framework sample ([areal.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/areal.py), [slime.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/slime.py), [slime_llm.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/slime_llm.py)).

## Artifact analysis

- **Storage substrate:** `in-memory` — JSON files under `agent_storage_path`, defaulting to `~/.local/opensage/dynamic_agents`, plus in-memory `_agents` and `_metadata` maps during a session
- **Representational form:** `symbolic` — Symbolic JSON metadata for name, status, creator, model string, tool names, `enabled_skills`, parent/children ids, and timestamps

**Dynamic subagent metadata.** Storage substrate: JSON files under `agent_storage_path`, defaulting to `~/.local/opensage/dynamic_agents`, plus in-memory `_agents` and `_metadata` maps during a session. Representational form: symbolic JSON metadata for name, status, creator, model string, tool names, `enabled_skills`, parent/children ids, and timestamps. Lineage: created by `create_subagent` from the caller agent's tool context and model/tool selections. Behavioral authority: system-definition artifact authority while loaded, because metadata configures a future runnable agent; effective cross-session authority is weaker because automatic reload is not fully active in the inspected code.

**Generated and built-in Skills.** Storage substrate: `src/opensage/bash_tools/`, `~/.local/opensage/bash_tools/`, and sandbox-mounted `/bash_tools`, with generated tools constrained to `bash_tools/new_tools/`. Representational form: mixed prose and symbolic metadata in `SKILL.md`, plus executable scripts and optional reference/assets. Lineage: built-in authored tool packages or agent/user-scaffolded packages from `new_tool_creator`; generated templates start with TODO placeholders and require later completion. Behavioral authority: system-definition artifacts. They define available operations, dependency sandboxes, execution location, and prompt-visible usage policy.

**Sandbox file memory.** Storage substrate: sandbox filesystem paths under `/mem/<agent_name>/`, `/mem/shared/`, `/mem/topology.json`, and saved long-output files under locations such as `/workspace/.tool_outputs` or `/workspace/.memory_observer_outputs`. Representational form: prose Markdown plans, JSON/JSONL session and shared-knowledge records, topology JSON, and raw text output files. Lineage: a mix of prompt-instructed agent maintenance, runtime session dumps from the patched ADK run loop, topology capture, and output-saving utilities. Behavioral authority: mostly advisory knowledge artifact authority when an agent reads files back; the prompt text that tells agents to consult and update `/mem` has instruction authority, but the file contents themselves are not enforced.

**ADK web-session snapshots.** Storage substrate: local saved-session directories under `~/.local/opensage/sessions`, containing `adk_session.json`, `resolved_config.toml`, and `metadata.json`. Representational form: symbolic JSON/TOML. Lineage: created on web shutdown from the live ADK session, resolved config, and sandbox runtime metadata; resume reloads the ADK session into the in-memory session service and reattaches to existing sandboxes where metadata allows. Behavioral authority: continuity and restore authority over the next web run, not general knowledge authority.

**Neo4j history database.** Storage substrate: Neo4j database selected as `history`, exported by evaluation as a tar archive when available. Representational form: symbolic graph nodes and relationships, with JSON strings for events, raw tool responses, summaries, session state, and agent-call edges. Lineage: trace-derived from ADK events, agent starts/ends, tool responses, compaction summaries, and subagent calls. Behavioral authority: audit, debugging, history navigation, and summarization support. It is mostly a knowledge artifact for later inspection; some query tools over history can make it operational context when explicitly called.

**Neo4j long-term memory database.** Storage substrate: Neo4j database selected as `memory`, with regular, vector, and full-text indexes over labels such as `Question`, `Answer`, `Text`, `Topic`, `Function`, `Class`, and `File`. Representational form: mixed symbolic graph properties and distributed-vector embeddings. Lineage: durable distilled state from tool-output traces when `memory_observer_plugin` is enabled and `[memory] enabled = true`; an LLM decider may summarize/select content, and entity extraction may use LLM and embeddings. Behavioral authority: knowledge artifact when `search_memory` returns matches; ranking and retrieval strategy have system-definition authority because they select what the agent sees.

**Plugin callback state and outputs.** Storage substrate: ADK session state, tool response dictionaries, sandbox output files, optional Neo4j nodes, and plugin source/config. Representational form: symbolic Python callbacks plus prose warnings/summaries. Lineage: authored plugins consume tool calls/results at before/after callback points. Behavioral authority: system-definition artifact authority for hooks that mutate or block tool flow, such as duplicate-call detection, read-before-edit warnings, build verification, tool-response summarization, and memory observation.

**Evaluation and RL artifacts.** Storage substrate: per-task output directories, exported sandbox directories, `session_trace.json`, `metadata.json`, Neo4j history exports, RL framework samples, token/loss-mask arrays, rewards, and patch/prediction files. Representational form: symbolic JSON, graph archives, text patches, token arrays, scalar rewards, and framework-specific distributed-parametric training inputs. Lineage: trace-derived from benchmark rollouts and task execution. Behavioral authority: evaluation, ranking, and learning authority outside the ordinary agent loop; RL adapters can turn rollouts into training data, but the inspected repo provides adapters and launch scripts rather than trained weights.

The promotion path is broad but uneven: tool results can become sandbox files, Neo4j history, summarized compaction events, long-term memory graph entities, evaluation traces, or RL training samples. OpenSage has many paths from trace to artifact, but only some paths include curation or validation beyond LLM selection and schema/index constraints.

## Comparison with Our System

| Dimension | OpenSage | Commonplace |
|---|---|---|
| Primary purpose | Agent framework for software-engineering agents, sandboxes, subagents, plugins, evaluation, and RL | Methodology KB framework with typed retained artifacts, validation, reviews, and source workflows |
| Main substrates | ADK sessions, sandbox files, Skill directories, dynamic-agent metadata, Neo4j databases, local snapshots, benchmark outputs | Git-tracked Markdown collections, type specs, source snapshots, generated indexes, review reports, and instructions |
| Memory creation | Agent writes files/Skills, runtime patches dump traces, plugins observe tool outputs, evaluation exports traces, RL adapters convert rollouts | Agents author/revise typed artifacts under collection contracts; snapshots and reviews preserve source lineage |
| Retrieval/read-back | Explicit `search_memory`, history tools, file reads, session resume, prompt-injected Skill/file-memory guidance | Pull through `rg`, indexes, links, type contracts, skills, validation, and review reports |
| Governance | Plugin order, config, sandbox constraints, Neo4j indexes, tool summaries, benchmarks, reward functions | Frontmatter schemas, collection contracts, link vocabulary, validation, semantic review, git lifecycle |
| Context control | History compaction, tool-response summaries, file pointers, subagent isolation, top-k memory search | Navigation indexes, descriptions, lexical search, type-local contracts, scoped skills, validation/review loops |

The strongest alignment is that both systems treat retained artifacts as operational surfaces rather than as one generic "memory" bucket. OpenSage's Skills resemble Commonplace skills in spirit: a package of prose instructions, metadata, scripts, and supporting files that changes future agent behavior. The major difference is governance. Commonplace keeps durable methodology claims in typed, reviewed, citation-bearing Markdown. OpenSage lets behavior-shaping state accumulate across runtime surfaces: prompt appendices, sandbox files, Neo4j nodes, generated Skills, plugin side effects, and RL/evaluation outputs.

OpenSage is stronger where the memory must sit inside an active agent framework. It has before/after tool callbacks, child-agent sessions, sandbox mounts, web-session resume, output compaction, and training adapters. Commonplace is stronger where durable knowledge must be inspectable, source-grounded, validated, and comparable across time. OpenSage's trace-derived graph memory can be useful, but the default lineage from a tool result to an extracted entity is weaker than Commonplace's source-pinned review/snapshot practice.

### Borrowable Ideas

**Treat generated Skills as a promotion target.** Ready with governance. Commonplace could make "write a reusable command/skill" an explicit promotion path from repeated workflow notes, but only with type checks, review, and clear provenance before the Skill gains instruction authority.

**Keep runtime traces separate from durable claims.** Ready now as a design reminder. OpenSage's separate history database, memory database, sandbox files, and RL outputs make it easier to distinguish audit traces from behavior-shaping artifacts. Commonplace should preserve that separation when adding trace capture.

**Session snapshots with resolved config.** Worth borrowing for agent-operated KB sessions if we add resumable workspaces. Persisting the ADK session together with resolved config and sandbox metadata is a clean continuity pattern; in Commonplace it would need a work-layer lifecycle and expiration policy.

**Tool-response summary plus full-output file pointer.** Ready for bounded-context tooling. Commonplace review commands could summarize large command outputs while retaining a file path for exact inspection, but the summary should be labeled as derived and should not replace validation evidence.

**Do not borrow LLM-decided memory as trust.** OpenSage's `StorageDecider` can decide what is "valuable" to store, but that is not the same as source trust, review status, or semantic correctness. Commonplace should keep LLM-derived candidates below reviewed artifacts in authority.

**Use plugin callbacks as guard surfaces.** Needs concrete use cases. A read-before-edit warning or build-verifier callback is a useful system-definition artifact, but Commonplace should encode stable rules as validation or review gates rather than silent runtime nudges where possible.

## Trace-derived learning placement

**Trace source.** OpenSage consumes several trace classes: ADK session events, tool calls/responses, subagent calls, sandbox command outputs, web-session state, benchmark task outputs, Neo4j history exports, and RL rollout interactions. The most direct durable learning path is `memory_observer_plugin`, which fires after tool execution and treats the tool result as candidate memory. Evaluation and RL adapters use task rollouts as training/evaluation payloads rather than as ordinary agent memory.

**Extraction.** Extraction is layered. `StorageDecider` optionally asks an LLM whether a tool result should be stored and may summarize it. `MemoryUpdateController` then extracts entities, discovers relationships, writes graph nodes/edges, and creates indexes/embeddings. Separately, history summarization creates compaction events from bounded windows of session events, and RL adapters convert trajectories into reward-bearing samples, token arrays, loss masks, and framework metadata.

**Scope and timing.** Memory observation is online and after-tool: it cannot change the tool action that just happened, but it can affect later explicit `search_memory` calls. History compaction is online after tool callbacks when the folded history exceeds budget. Evaluation export is per-task and offline after a benchmark run. RL adapters run per rollout and pass trace-derived training data to external frameworks.

**Survey placement.** OpenSage sits in a mixed trace-to-graph and trace-to-training branch of the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey's distinction between raw trace retention and distilled behavior-shaping artifacts: Neo4j history preserves traces for audit, Neo4j memory extracts searchable entities/relationships, and RL adapters produce training samples without making the resulting model artifact part of the repository.

## Read-back placement

**Read-back:** `both` — Long-term Neo4j memory is explicit pull through `search_memory` or the memory-management agent, while configured Skills, history/session summaries, and ensemble message-board diffs can arrive without the receiving agent making a memory lookup.

The strongest memory push is the ensemble message-board path. `message_board_diff_plugin` runs after a tool call, resolves the receiving agent instance id and current board id, reads unread JSONL records with a per-agent cursor, and appends the diff into the tool result. Targeting is `instance`; the signal is `identifier`, because selection keys on `board_id` plus the receiving `agent_id`/instance id rather than semantic similarity. It is after-tool rather than pre-action, so it can shape the next model turn rather than the tool call that just completed; scope is capped by `read_diff(max_bytes=32000)`. Precision, context dilution, and effective authority are not verified from code.

Other push-like surfaces are weaker or outside memory read-back. History compaction automatically appends a session-summary event when the folded history exceeds budget, which is a coarse session-memory push rather than an instance-relevance signal. Built-in Skill descriptions and the `/mem` layout instructions are shipped baseline prompt surfaces, not read-back; user-local or plugin Skill metadata can be retained memory when selected by `enabled_skills`, but full `SKILL.md` content is normally pulled through `list_available_scripts`. Long-term Neo4j memory remains pull-only: `search_memory` requires an explicit query and then uses LLM strategy selection, embedding search, keyword search, or title browsing.

## Curiosity Pass

The system's most interesting memory design is also its main risk: OpenSage has many retained surfaces with different authority levels, and the code does not force them into one audited promotion ladder. A generated Skill, a `/mem/shared/knowledge.jsonl` line, a memory graph entity, and an RL sample all change future behavior differently.

Dynamic-agent persistence is weaker than the README-level story might imply. Metadata writing is implemented and tested, but the on-demand loading loop is commented out in the inspected manager. A reader should not assume dynamic subagents automatically become reliable reusable agents across sessions.

The file-memory prompt is strong operationally but not selective. It tells agents to read and update `/mem` structures, including shared knowledge, but the system does not itself prove that the agent consulted the right file or that shared knowledge is correct.

The plugin system is a powerful place for memory policy because callbacks sit directly before or after tool use. That same position makes provenance and observability important: plugin order and side effects can decide what the agent sees, what gets stored, and what gets summarized.

The RL adapters are best read as behavior-learning infrastructure, not as an implemented memory store. They make OpenSage rollouts trainable in AReaL or SLIME, but the learned weights and training framework state live outside the reviewed repo.

## What to Watch

- Whether dynamic-agent reload is re-enabled and governed, because that would turn persisted metadata into a stronger reusable-agent memory surface.
- Whether Neo4j memory gains source/provenance views that connect extracted entities back to exact tool outputs, session events, and storage-decider rationales.
- Whether `/mem/shared/knowledge.jsonl` gets validation, deduplication, or review workflow before agents treat it as stable shared knowledge.
- Whether generated Skills move from templates with TODOs to a reviewed promotion workflow with tests and sandbox dependency checks.
- Whether plugin callbacks add faithfulness checks showing that retrieved or stored memories actually change downstream behavior.
- Whether RL integrations produce retained model artifacts or only rollout/training handoff data in future revisions.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places OpenSage's tool-output memory observer, history traces, and RL adapters on the trace-derived learning landscape.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: OpenSage's Skills, sandbox files, Neo4j graphs, session snapshots, plugin outputs, and RL samples split cleanly by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: OpenSage stores long-term graph memory, but ordinary read-back is still explicit search or unconditional instruction rather than relevance-gated push.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: session traces, history records, file memory, and search results mostly advise or evidence future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: Skills, plugin callbacks, generated prompts, search strategies, RL adapters, and validation-like guards carry stronger behavioral authority.
