---
description: "OpenSage review: ADK agent framework with dynamic subagents, Skills, sandbox memory, Neo4j history/memory, plugins, and RL adapters"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# OpenSage

OpenSage, by opensage-agent, is a Python agent framework built around Google ADK for software-engineering agents. At the reviewed commit it implements dynamic subagent creation, prompt-visible bash-tool Skills, sandbox file memory under `/mem`, Neo4j-backed execution history and long-term memory, plugin callbacks for summarization and memory observation, and evaluation/RL adapters. Its memory system is not one store: retained state is split across local files, sandbox files, ADK session state, Neo4j history/memory graphs, message-board JSONL, generated Skill packages, benchmark outputs, and RL rollout payloads.

**Repository:** https://github.com/opensage-agent/OpenSage

**Reviewed commit:** [481b4344f3d07de42082f367ecda4381f81c22c8](https://github.com/opensage-agent/OpenSage/commit/481b4344f3d07de42082f367ecda4381f81c22c8)

**Last checked:** 2026-06-04

## Core Ideas

**Dynamic subagents are retained as metadata-backed runnable configurations.** The `create_subagent` tool validates model/tool choices, injects baseline tools, appends a bash-Skill tooling policy, and asks the session's `DynamicAgentManager` to create and persist `AgentMetadata` JSON records under the configured storage path, defaulting to `~/.local/opensage/dynamic_agents` ([dynamic_subagent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/toolbox/general/dynamic_subagent.py), [opensage_dynamic_agent_manager.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_dynamic_agent_manager.py)). The persistence story is not full cross-session resurrection at this commit: `_load_persisted_agents_on_demand` returns after guard checks and the file-loading loop is commented out.

**Skills are prompt-visible tool packages.** `ToolLoader` reads `SKILL.md` frontmatter and markdown from built-in and user-local roots, filters by `enabled_skills`, parses sandbox requirements, and appends a generated tool list plus usage policy to the agent instruction ([opensage_agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/agents/opensage_agent.py)). The `new_tool_creator` Skill scaffolds new Skill directories and scripts, so a workflow can be promoted into a behavior-shaping package rather than remaining only a transcript ([SKILL.md](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/bash_tools/new_tool_creator/SKILL.md), [init_skill.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/bash_tools/new_tool_creator/init_skill.py)).

**Sandbox file memory is an instructed workspace convention.** When required sandboxes exist, OpenSage injects a `/mem` layout into the prompt: per-agent `planning.md`, session JSON dumps, `/mem/topology.json`, and shared `/mem/shared/knowledge.jsonl`. The instruction tells the agent to read plans before work, update them after major steps, and curate shared knowledge ([opensage_agent.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/agents/opensage_agent.py)). The Neo4j logging patch also creates the `/mem` folders, persists session JSON, and records topology around agent starts, ends, and calls ([neo4j_logging.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/patches/neo4j_logging.py)).

**Neo4j separates history, analysis, and memory roles.** The session client manager maps `history`, `analysis`, and `memory` to distinct database names ([opensage_neo4j_client_manager.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/opensage_neo4j_client_manager.py)). History logging records agent runs, events, tool responses, session state, and agent-call relations ([neo4j_history_management.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/utils/neo4j_history_management.py)). Long-term memory is separate: `MemoryObserverPlugin` watches tool results, asks `StorageDecider` whether they are valuable, and sends accepted content to `MemoryUpdateController`, which extracts entities, discovers relationships, and writes graph records with indexes/embeddings ([memory_observer_plugin.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/plugins/default/adk_plugins/memory_observer_plugin.py), [update_controller.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/update/update_controller.py)).

**Context efficiency comes from compaction, summarization, and delegation rather than one global retrieval budget.** Tool-response summarization saves long outputs to sandbox files and replaces the in-context response with a model summary and file pointer. History summarization compacts older event windows into ADK compaction events and optional Neo4j summary nodes. Dynamic subagents isolate work into child sessions, while explicit long-term memory lookup uses top-k limits plus LLM/heuristic strategy selection over embedding, keyword, and title-browse search ([summarization.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/features/summarization.py), [search_tool.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search_tool.py), [search_controller.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search/search_controller.py)).

**Evaluation and RL adapters turn trajectories into learning payloads.** Evaluation exports session traces, task metadata, sandbox outputs, and optional Neo4j database archives ([base.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/base.py)). The AReaL adapter runs OpenSage evaluation with an ADK-compatible RL model and computes rewards; the SLIME adapter routes calls through `SlimeLlm`, tracks prompt/assistant/environment tokens and loss masks, and fills the training sample ([areal.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/areal.py), [slime.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/adapters/slime.py), [slime_llm.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/evaluation/rl_adapters/slime_llm.py)).

## Artifact analysis

- **Storage substrate:** `files` `graph` `in-memory` — Retained surfaces persist as dynamic-agent JSON, Skill files, sandbox `/mem` files, saved web sessions, message-board JSONL, per-task evaluation outputs, Neo4j history/memory graphs, and runtime ADK/session manager state.
- **Representational form:** `prose` `symbolic` `parametric` — Plans, summaries, Skill guidance, and memory values are prose; metadata, config, session/event JSON, graph nodes/edges, plugin code, indexes, and tool schemas are symbolic; embeddings, token arrays, loss masks, rewards, and external RL model interfaces add parametric learning surfaces.
- **Lineage:** `authored` `trace-extracted` — Built-in Skills, plugins, configs, and agent instructions are authored; history nodes, session dumps, compaction summaries, memory graph entities, message-board records, evaluation traces, and RL samples derive from agent/session/tool/rollout traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Files, graph records, summaries, and search results advise; Skills and prompt appendices instruct; plugins can mutate/block tool flow; managers route subagents and sandboxes; schemas/indexes/config checks validate structure; search scores/strategies rank recall; RL adapters feed learning.

**Dynamic subagent metadata.** Storage substrate: JSON files under `agent_storage_path` plus in-memory `_agents` and `_metadata` maps. Representational form: symbolic config for name, status, model, tools, `enabled_skills`, parent/children ids, and timestamps. Lineage: created from a caller agent's tool context and requested configuration. Behavioral authority: system-definition authority while loaded because it configures a runnable future agent; cross-session authority is weaker until restore loading is implemented again.

**Skill packages and generated tools.** Storage substrate: `src/opensage/bash_tools/`, `~/.local/opensage/bash_tools/`, and sandbox-mounted `/bash_tools`, with generated tools under the new-tool path. Representational form: prose `SKILL.md`, symbolic YAML metadata, scripts, and optional dependencies. Lineage: built-in authored packages or agent/user-scaffolded packages. Behavioral authority: instruction and routing, because loaded Skills shape prompt-visible tool choices and sandbox execution locations.

**Sandbox memory files.** Storage substrate: `/mem/<agent_name>/`, `/mem/shared/knowledge.jsonl`, `/mem/topology.json`, saved session JSON, and long-output files such as `/workspace/.tool_outputs` or `/workspace/.memory_observer_outputs`. Representational form: Markdown/prose, JSON/JSONL, and raw text. Lineage: prompt-instructed agent maintenance plus runtime session/topology/output capture. Behavioral authority: mostly knowledge when read back, with instruction authority in the prompt rule that tells agents to consult and update the files.

**Neo4j history and memory graphs.** Storage substrate: Neo4j `agent-history` and `memory` databases. Representational form: symbolic graph nodes/relationships, JSON strings, full-text/vector indexes, and embeddings. Lineage: history is trace-extracted from ADK events and tool responses; long-term memory is distilled from tool outputs by an LLM/heuristic storage decision, entity extraction, relationship discovery, and graph writes. Behavioral authority: history is audit/navigation context; memory is knowledge when `search_memory` returns matches, while strategies, indexes, and scores provide routing/ranking authority.

**Plugin callback state and outputs.** Storage substrate: plugin source/config, ADK session state, mutated tool responses, sandbox output files, optional Neo4j nodes, and message-board JSONL/cursors. Representational form: symbolic callbacks plus prose warnings, summaries, quota notes, and board diffs. Lineage: authored plugin logic consumes live tool-call and tool-result traces. Behavioral authority: system-definition authority when callbacks summarize, warn, block, append board diffs, observe memory, or verify builds.

**Evaluation and RL artifacts.** Storage substrate: per-task output directories, exported sandbox directories, `session_trace.json`, `metadata.json`, Neo4j archives, framework samples, token/loss-mask arrays, rewards, patches, and prediction files. Representational form: symbolic JSON/archives, prose/text outputs, token arrays, scalar rewards, and external training-framework state. Lineage: trace-extracted from benchmark rollouts. Behavioral authority: evaluation, ranking, and learning outside the ordinary agent loop; the inspected repo provides adapters and launch scripts, not retained trained weights.

Promotion path: OpenSage can move a trace into several stronger forms: a raw event becomes Neo4j history, a long output becomes a file-backed summary, a selected tool result becomes a memory-graph entity, repeated workflow knowledge can become a generated Skill, and rollout trajectories can become RL training samples. The path is broad but uneven; not every promotion has review, provenance, or faithfulness checks.

## Comparison with Our System

| Dimension | OpenSage | Commonplace |
|---|---|---|
| Primary purpose | Runtime framework for software-engineering agents, sandboxes, subagents, plugins, evaluation, and RL | Methodology KB framework with typed retained artifacts, source workflows, validation, and review |
| Main substrates | ADK sessions, sandbox files, Skill directories, dynamic-agent metadata, Neo4j graphs, message boards, benchmark outputs | Git-tracked Markdown collections, type specs, source snapshots, generated indexes, review reports, and instructions |
| Memory creation | Agent file writes, plugin observation, history compaction, graph extraction, generated Skills, rollout export | Authored notes/reviews, source snapshots, type-governed revisions, validation, semantic review |
| Read-back | Explicit memory/history/file pulls plus pushed summaries and message-board diffs in configured runs | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | Plugin order/config, sandbox constraints, schema/index creation, benchmark rewards, tool summaries | Frontmatter schemas, collection contracts, link vocabulary, deterministic validation, semantic review, git lifecycle |

The strongest alignment is that both systems treat retained artifacts as behavior-shaping surfaces, not as a single generic memory bucket. OpenSage's Skills resemble Commonplace skills: a package of prose, metadata, scripts, and dependencies that can change future agent behavior.

The major divergence is governance. Commonplace makes durable claims source-grounded, typed, reviewed, and diffable in a Git repository. OpenSage lets behavior-shaping state accumulate across runtime surfaces: prompt appendices, sandbox files, graph nodes, generated tools, plugin mutations, message-board records, and RL/evaluation outputs. That is stronger for active agent operations and weaker for long-lived epistemic trust.

### Borrowable Ideas

**Generated Skills as a promotion target.** Ready with governance. Commonplace could make "promote repeated workflow into a reusable skill" an explicit path, but the promoted Skill should gain instruction authority only after type checks, tests, and source/provenance review.

**Separate history from memory.** Ready now as an architectural principle. OpenSage's distinction between execution history and long-term memory helps prevent raw traces from being treated as reviewed knowledge.

**Tool-output summary with full-output pointer.** Ready for bounded-context tooling. Commonplace commands could summarize huge outputs while retaining an exact file for inspection, as long as the summary is labeled as derived.

**Plugin callbacks as guard surfaces.** Needs concrete use cases. Read-before-edit and build-verifier hooks show where runtime guards can live, but Commonplace should encode stable rules as validators or review gates when possible.

**Do not borrow LLM-selected memory as trust.** OpenSage's storage decider can choose what seems worth retaining, but that is not a correctness, source, or review signal. Commonplace should keep LLM-derived candidates below reviewed artifacts in authority.

## Write side

**Write agency:** `manual` `automatic` — Humans/agents can author Skills and sandbox memory files, while plugins, history logging, compaction, memory observation, message boards, evaluation export, and RL adapters automatically write retained surfaces from execution traces.

**Curation operations:** `consolidate` `synthesize` `promote` — History and tool-response summarizers consolidate large trace windows/outputs; memory extraction and generated Skills can synthesize new retained artifacts from traces or workflows; selected outputs are promoted into memory graphs, summaries, Skill packages, evaluation artifacts, or RL samples.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — OpenSage consumes ADK session events, tool calls/responses, plugin callback streams, message-board records, benchmark outputs, and RL rollouts.

**Learning scope:** `per-task` `per-project` `cross-task` — Evaluation/RL artifacts are per task or rollout, sandbox and message-board memory are session/project scoped, and Neo4j memory can be reused across later work.

**Learning timing:** `online` `offline` `staged` — Tool-result observation, history compaction, message-board append/read, and file memory happen during runs; evaluation export and RL handoff happen after benchmark or rollout execution; generated Skills are staged promotions.

**Distilled form:** `prose` `symbolic` `parametric` — Distillation produces summaries, warnings, plans, graph entities/relationships, indexes, Skill packages, embeddings, token/loss-mask arrays, rewards, and training-framework samples.

**Trace source.** OpenSage qualifies as trace-derived because multiple durable artifacts derive from live agent traces: ADK events are logged to Neo4j, tool responses can become summaries or memory graph content, sandbox sessions are dumped to `/mem`, message-board JSONL is appended during ensemble work, benchmark runs export `session_trace.json`, and RL adapters convert rollouts into training payloads.

**Extraction.** Extraction is layered. The memory observer uses length/exclusion filters plus an optional LLM `StorageDecider`; `MemoryUpdateController` then extracts entities, discovers relationships, and writes graph records. Summarization prompts produce prose summaries from tool responses or event windows. RL adapters use benchmark reward functions and tokenizer/model traces rather than a KB-style semantic review.

**Scope and timing.** Online writes mostly occur after a tool call or when a history budget is exceeded, so they cannot change the action that just produced the trace but can affect later turns. Evaluation/RL artifacts are downstream of a benchmark run. Generated Skills are an explicit promotion path from repeated operational knowledge to reusable instruction/tool packages.

**Survey fit.** OpenSage sits in the trace-to-graph, trace-to-summary, and trace-to-training branches of the trace-derived learning landscape. It strengthens the distinction between raw trace retention and distilled behavior-shaping artifacts: Neo4j history preserves raw-ish event records, Neo4j memory extracts searchable graph knowledge, and RL adapters produce training payloads without making learned weights part of the repo.

## Read-back

**Read-back:** `both` — Long-term memory, history, files, and subagents are usually explicit pull surfaces, while configured history summaries and message-board diffs can be inserted into the agent's next context without the receiving agent making a memory lookup.

**Read-back signal:** `coarse` `identifier` — History compaction pushes coarse session summaries when budget thresholds fire, and the message-board diff plugin targets unread board records by board id plus receiving agent id.

**Faithfulness tested:** `no` — The inspected tests and integrations check mechanics such as dynamic subagent calls, Neo4j logging, summarization, and tool flows, but I did not find an ablation or post-action audit proving that pushed summaries, board diffs, or searched memory change downstream behavior faithfully.

The clearest targeted push is `MessageBoardDiffPlugin`: after a tool call, it resolves the current board id and receiving agent instance id, reads unread JSONL records with a per-agent cursor, and appends the diff into the tool result ([message_board_diff_plugin.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/plugins/default/adk_plugins/message_board_diff_plugin.py), [message_board.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/session/message_board.py)). The signal is `identifier`, not semantic relevance: selection keys on `board_id` and `agent_id`, with `max_bytes=32000`.

History compaction is coarse push. The callback checks the folded event-history budget, summarizes an older event window, appends an ADK compaction event, and can record the summary in Neo4j ([summarization.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/features/summarization.py)). That summary can affect later model calls as part of the session context, but it is selected by budget/window policy rather than instance relevance.

The long-term Neo4j memory search path remains pull. `search_memory` requires an explicit query and then uses LLM-selected or heuristic strategies over embedding search, keyword search, and title browsing with top-k and score controls ([search_tool.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search_tool.py), [search_controller.py](https://github.com/opensage-agent/OpenSage/blob/481b4344f3d07de42082f367ecda4381f81c22c8/src/opensage/memory/search/search_controller.py)). Sandbox `/mem` files are also pull unless an agent follows prompt instructions to read them; the prompt rule itself is static instruction, not a proof that file contents are automatically injected.

At consumption, retrieved graph memory and file contents are advisory knowledge; Skills, plugin policies, and prompt appendices carry stronger instruction/routing authority. Effective precision, context dilution, and behavioral obedience are not verified from code.

## Curiosity Pass

OpenSage's most important memory characteristic is heterogeneity. A generated Skill, a `/mem/shared/knowledge.jsonl` line, a Neo4j entity, a message-board diff, a compaction event, and an RL sample all count as retained behavior-shaping state, but they carry different authority and reviewability.

The dynamic-subagent persistence story is a useful caution. Metadata writing is implemented, but on-demand metadata loading is commented out, so a reader should not infer reliable cross-session reusable agents from the existence of metadata files alone.

The message board is a small but real push mechanism. It is easy to overlook because it piggybacks on tool results after a tool call, but from the receiving agent's perspective unread retained records arrive without an explicit memory lookup.

The RL adapters are behavior-learning infrastructure, not ordinary memory storage. They make OpenSage rollouts trainable in AReaL or SLIME, but the resulting trained weights and framework state live outside the reviewed repository.

## What to Watch

- Whether dynamic-agent reload is re-enabled and governed, because that would turn persisted metadata into stronger reusable-agent memory.
- Whether Neo4j memory gains source/provenance views connecting extracted entities back to exact tool outputs, session events, and storage-decider rationales.
- Whether `/mem/shared/knowledge.jsonl` gains validation, deduplication, or review before agents treat it as stable shared knowledge.
- Whether generated Skills move from scaffolds/templates into a tested promotion workflow with provenance and sandbox dependency checks.
- Whether plugin callbacks add with/without-memory or post-action faithfulness checks for pushed summaries, board diffs, and searched memory.
- Whether RL integrations produce retained model artifacts in or near the project, rather than only rollout/training handoff data.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places OpenSage's tool-output memory observer, history traces, summaries, message board, and RL adapters on the trace-derived learning landscape.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: OpenSage stores long-term memory and also has configured push paths through compaction and message-board diffs.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: OpenSage's Skills, sandbox files, Neo4j graphs, plugin outputs, message boards, and RL samples split by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: session traces, history records, graph search results, and file memory mostly advise future work.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: Skills, plugin callbacks, prompt policies, search strategies, and RL adapters carry stronger behavioral authority.
