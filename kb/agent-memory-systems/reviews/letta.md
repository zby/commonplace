---
description: "Letta review: stateful agent server with prompt-rendered core memory, searchable recall/archives, compaction, sleeptime agents, and git memory"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# Letta

Letta, formerly MemGPT, is Letta AI's open-source stateful-agent server and SDK substrate. At the reviewed commit it persists agents, messages, core memory blocks, archival passages, sources/files, tool rules, runs, traces, and optional git-backed memory; it then reconstructs prompt context from those retained artifacts before agent steps, while exposing separate search and edit tools for longer-term memory.

**Repository:** https://github.com/letta-ai/letta

**Reviewed commit:** [1131535716e8a31c9a437f8695e25ac98f203a24](https://github.com/letta-ai/letta/commit/1131535716e8a31c9a437f8695e25ac98f203a24)

**Last checked:** 2026-06-02

## Core Ideas

**Core memory is rendered into the system prompt.** `Memory` stores labeled `Block` objects and compiles them into XML-like `<memory_blocks>` sections, including descriptions, read-only flags, current character counts, and character limits ([memory schema](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/memory.py)). `PromptGenerator` inserts that compiled memory into the protected `{CORE_MEMORY}` variable and appends it if the system prompt omitted the variable, so current core memory is pre-action context rather than a tool the agent must remember to call ([prompt generator](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/prompt_generator.py)).

**Memory changes trigger prompt rebuilds.** `BlockManager.update_block_async()` treats description, label, limit, read-only, and value changes as prompt-affecting and rebuilds system prompts for connected agents; `AgentManager.rebuild_system_prompt_async()` recompiles memory, counts recall and archival memory, and swaps the persisted system message when the compiled memory differs ([block manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/block_manager.py), [agent manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/agent_manager.py)). That makes retained blocks behavior-shaping system-definition inputs, not passive database rows.

**Archival and recall memory are pull surfaces with metadata hints.** Messages persist in the `messages` table with role, content, tool calls, run/step ids, group ids, conversation ids, and sequence indexes ([message ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/message.py)). Archival memory persists as `ArchivalPassage` rows with text, embeddings, metadata, tags, archive ids, and vector/text-index support ([passage ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/passage.py), [passage manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/passage_manager.py)). The prompt includes counts and archive tags, but actual retrieval comes through tools such as `conversation_search` and `archival_memory_search` ([base tools](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/functions/function_sets/base.py)).

**Context efficiency is layered, not one mechanism.** Core blocks have per-block character limits and render only their current values; git-enabled agents render only `system/` blocks into direct prompt memory, list non-system memory as an external projection, and render skills as a tree rather than loading every skill file ([memory schema](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/memory.py), [memory tests](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/tests/test_memory.py)). Attached source files use open/closed file blocks, `max_files_open`, and per-file view limits instead of dumping whole sources into the prompt. Archival and conversation retrieval use limits, tags, date filters, and embeddings.

**Agents can edit their own memory, but the mutation path is tool-mediated.** Core memory tools append, replace, insert, rethink, and patch memory blocks through the agent state; archival insert/search tools create and retrieve long-term memories ([base tools](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/functions/function_sets/base.py)). Tool execution is routed through `ToolExecutionManager` from the agent loop, so memory writes happen as explicit tool effects rather than invisible model-side state changes ([Letta agent](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/agents/letta_agent.py)).

**Sleeptime agents are background memory maintainers.** When sleeptime is enabled, the foreground agent's response is followed by background participant runs that receive a transcript of recent foreground messages and an instruction to review the conversation and update relevant memory blocks ([sleeptime group](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/groups/sleeptime_multi_agent_v4.py)). Integration tests verify shared blocks, sleeptime-specific memory edit tools, run creation, and a skipped redundancy-collapse test that describes the intended consolidation behavior ([sleeptime tests](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/tests/integration_test_sleeptime_agent.py)).

**Compaction turns message history into retained summary messages.** The v3 agent triggers compaction when the context estimate crosses thresholds or a context-window error occurs, then `compact_messages()` summarizes in-context messages using configured compaction settings and persists a summary message that can replace compacted history ([Letta agent v3](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/agents/letta_agent_v3.py), [compact service](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/summarizer/compact.py)). This is context-pressure adaptation from trace material, not just retrieval.

**Git-backed memory makes blocks inspectable and versioned.** With the `git-memory-enabled` tag, `GitEnabledBlockManager` writes blocks to a git memory repository first and treats PostgreSQL as a cache; blocks serialize to Markdown with YAML frontmatter and path-like labels map to markdown files ([git block manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/block_manager_git.py), [git operations](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/git_operations.py), [block markdown](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/block_markdown.py), [path mapping](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/path_mapping.py)). This is closer to Commonplace's auditability than ordinary service memory, though still mediated by server code.

## Artifact analysis

- **Storage substrate:** `rdbms` — `block` table rows, agent/block pivot rows, optional block tags and history pointers, and optionally git-backed Markdown files when git memory is enabled
- **Representational form:** `mixed` — Prose values plus symbolic labels, descriptions, limits, read-only flags, metadata, tags, and path-like labels

**Core memory blocks.** Storage substrate: `block` table rows, agent/block pivot rows, optional block tags and history pointers, and optionally git-backed Markdown files when git memory is enabled. Representational form: prose values plus symbolic labels, descriptions, limits, read-only flags, metadata, tags, and path-like labels. Lineage: authored at agent creation, edited through API/tool calls, or trace-derived through sleeptime/background agents; git mode can preserve commit history, while ordinary database mode preserves less diff-oriented lineage. Behavioral authority: system-definition artifact when compiled into the system prompt, because block content and metadata directly shape the next model call; knowledge artifact when shown to users or edited as remembered facts.

**Compiled system prompt / in-context message list.** Storage substrate: persisted system `Message` plus the agent's `message_ids` context window. Representational form: assembled prose and XML-like symbolic prompt sections. Lineage: derived from the system prompt, current memory blocks, tool rules, source/file state, previous message count, archival memory count, archive tags, and timestamps. Behavioral authority: high-authority system instruction and pre-action context for the receiving model; regenerated when core memory or system prompt changes.

**Recall messages.** Storage substrate: `messages` table, sequence indexes, run/step ids, group ids, conversation ids, and optional vector backends for message search. Representational form: structured conversation/tool traces with prose content and symbolic metadata. Lineage: raw interaction trace from agent/user/tool execution. Behavioral authority: knowledge artifact when listed or searched; ranking and filtering state has system-definition authority for retrieval.

**Archival passages and archives.** Storage substrate: `archives`, `archives_agents`, `archival_passages`, passage tags, embeddings, and optional Turbopuffer/Pinecone/Postgres vector storage. Representational form: prose passages plus symbolic tags, metadata, timestamps, embeddings, and archive relationships. Lineage: inserted through archival tools, APIs, files, or background agents; embeddings and indexes are derived views over passage text. Behavioral authority: knowledge artifact when searched into context; embeddings, tags, and date filters provide ranking and routing authority.

**Source/file blocks and source passages.** Storage substrate: source/file metadata, source passages, file-agent associations, and `FileBlock` views. Representational form: file text slices plus symbolic source ids, file ids, open/closed state, line windows, and per-file limits. Lineage: imported file content processed into passages and visible file windows; file changes or processor settings invalidate the derived passages and visible snippets. Behavioral authority: advisory context when opened into directories; routing authority when file open state and limits decide which material is visible.

**Sleeptime and compaction outputs.** Storage substrate: shared blocks, summary messages, runs, group state, and message traces. Representational form: distilled prose summaries or rewritten block contents plus symbolic run/status metadata. Lineage: trace-derived from foreground conversations, response messages, or compacted context windows; LLM prompts and compaction settings are part of the derivation policy. Behavioral authority: sleeptime block edits become system-definition artifacts on later prompt rebuilds; summary messages become knowledge/context artifacts that preserve continuity after compaction.

**Tool rules, memory tools, and git-memory configuration.** Storage substrate: repository code, tool rows, agent-tool pivots, tool rules, agent tags, memory repo object storage, and hook-like server paths. Representational form: symbolic schemas/configuration plus prose tool descriptions. Lineage: authored system-definition artifacts, with runtime tool state attached per agent. Behavioral authority: instruction, routing, enforcement, and mutation authority over what the agent can change and how memory operations are validated.

Promotion path: Letta has a direct authority ladder. Raw messages enter as recall traces; agents or sleeptime agents can distill them into core block edits or archival passages; prompt rebuild promotes core block content into the next system prompt; compaction promotes long trace windows into summary messages; git-backed mode can additionally promote database block state into inspectable versioned files. The weak point is governance: promotion is operational and model-mediated, not review-gated by default.

## Comparison with Our System

| Dimension | Letta | Commonplace |
|---|---|---|
| Primary purpose | Runtime stateful agents with persistent memory and tool-mediated self-editing | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifacts | Blocks, messages, archives/passages, sources/files, tool rules, runs, git memory repos | Typed Markdown notes, instructions, reviews, ADRs, source snapshots, indexes, reports |
| Storage substrate | Database tables, vector stores, object-storage git repos, API/server state | Repository files plus generated indexes and validation/review reports |
| Read-back | Core blocks and open files push into prompt; recall/archives pull through tools | Mostly deliberate pull via `rg`, indexes, links, skills, and explicit instructions |
| Learning loop | Agent/sleeptime tool edits, compaction summaries, archival inserts from traces | Human/agent-authored promotion through source snapshots, notes, reviews, validation, and gates |
| Governance | Runtime validators, tool rules, tests, optional git history | Git diffs, collection contracts, schemas, validation, semantic gates, replacement archives |

Letta is much stronger than Commonplace as an online agent runtime. It owns agent creation, message execution, tool dispatch, memory mutation, background memory maintenance, compaction, API surfaces, and vector-backed retrieval. Commonplace is stronger as an inspectable knowledge library: changes are reviewable as ordinary files, type contracts are explicit, source citations are stable, and validation/reporting is built around artifact governance rather than conversation continuity.

The closest overlap is git-backed memory. Letta's memory repo path acknowledges the same design pressure as Commonplace: durable behavior-shaping prose should be inspectable, versioned, and recoverable. The difference is that Letta still treats git as a backing store behind server APIs, whereas Commonplace treats the repo itself as the operating surface.

**Read-back:** `both` — Core memory blocks and selected source/file windows are pushed into the receiving model's system context before action; archival and conversation memory content is pull through tools the agent or host must call explicitly

### Borrowable Ideas

**Separate core memory from archival memory in the prompt contract.** Ready now as a vocabulary refinement. Commonplace should keep distinguishing always-available operative instructions from searchable background evidence, and it should name the read-back path explicitly when writing skills.

**Expose memory availability metadata without dumping memory content.** Ready for retrieval tooling. Letta's memory metadata block tells the agent how much recall and archival memory exists and which tags are available. A Commonplace analogue would be compact generated hints for large source collections, not automatic loading.

**Use background memory-maintenance agents only inside workshops.** Needs a controlled use case. Sleeptime is attractive for trace distillation, but Commonplace should run it against bounded workshop traces and require review before promoting edits to library notes or instructions.

**Borrow git-backed memory as an adoption bridge, not as hidden infrastructure.** Ready conceptually. Letta's Markdown block serialization and git commit history are useful, but Commonplace should keep the repo as the primary source of truth rather than a cache behind an API.

**Treat compaction summaries as retained artifacts with lineage.** Ready now. Commonplace already receives context-compaction summaries from agents; the Letta design reinforces that summaries should record trigger, source window, prompt/model policy, and whether they are advisory or authoritative.

**Do not borrow automatic core-memory authority promotion wholesale.** Letta can let an agent or sleeptime agent rewrite behavior-shaping blocks from traces. Commonplace should preserve a review gate before trace-derived prose becomes instruction, validator, or navigation policy.

## Trace-derived learning placement

**Trace source.** Letta qualifies as trace-derived. The raw signals include persisted conversation messages, tool calls/returns, run and step records, foreground response messages handed to sleeptime agents, and message windows compacted under context pressure.

**Extraction.** Extraction is mostly LLM/tool mediated rather than a fixed classifier. Foreground agents can call memory tools to edit core blocks or insert archival passages. Sleeptime agents receive conversation transcripts with an explicit memory-management instruction and can use memory edit tools to update shared blocks. Compaction passes in-context messages through summarizer prompts and model settings to produce summary messages.

**Four fields.** The raw stage is message/run/tool trace state in database tables: structured traces plus prose content, knowledge-artifact authority as evidence, and retrieval/ranking authority when searched. The distilled stages are block edits, archival passages, and summary messages: mixed prose/symbolic artifacts with lineage from traces and compaction/sleeptime prompts. Core block edits gain system-definition authority when prompt rebuild injects them into the next system prompt; archival passages and summaries remain mostly advisory unless a host or agent reads them back.

**Scope and timing.** Scope is per agent, conversation, group, archive, source, organization, and sometimes project. Timing is mixed: foreground memory tools run during an agent step; sleeptime agents run asynchronously after foreground turns according to group frequency; compaction runs when context pressure crosses thresholds or errors occur; archival search and conversation search are on-demand.

**Survey placement.** Letta belongs in the trace-to-core-memory and trace-to-summary families. It strengthens the survey claim that behavior change usually occurs after a distillation boundary: raw messages are not themselves high-authority memory until an agent, sleeptime agent, compactor, or tool path converts them into prompt-rendered blocks, summaries, or retrieved passages.

## Read-back placement

**Direction.** Letta is both push and pull. Core memory blocks and selected file/source views are pushed into the model context through system prompt compilation. Conversation and archival memory are pull through tools such as `conversation_search` and `archival_memory_search`; the prompt-rendered counts and archive tags are availability metadata, not a push of archival memory content.

**Targeting and signal.** The pushed memory path is instance-targeted, with an `identifier` signal. Core blocks are selected by the receiving agent's attached memory blocks and block labels; git-enabled rendering narrows direct prompt memory to `system/` labels. File/source views are selected by agent-file/source associations, open-file state, file ids/names, and configured line/window limits. This is not semantic top-k selection for core blocks; archival semantic search remains pull.

**Timing relative to action.** Core blocks and file windows are present before the next LLM call and can change the next action. Sleeptime and compaction run after turns or under context pressure, so their outputs affect later turns after persistence and prompt rebuild. Archival/recall searches affect the current turn only when the model or host calls the tool.

**Selection, scope, and complexity.** Context volume is controlled by block character limits, git `system/` rendering, open/closed file state, `max_files_open`, per-file view windows, retrieval limits, tags, date filters, and compaction thresholds. Context complexity is still high: the prompt can combine system text, core blocks, metadata, source directories, file snippets, tool rules, skills, summaries, and messages.

**Authority at consumption.** Core memory is advisory content inside a system prompt, with stronger force than a retrieved fact but weaker than a hard validator. Tool rules and read-only metadata can constrain tool choices or editing rights. Archival and recall results are knowledge artifacts unless the agent's system prompt or host gives them stronger instruction force.

**Faithfulness.** The code and tests verify rendering, prompt recompilation, sleeptime wiring, and compaction behavior, but I did not find a with/without ablation proving that pushed core memory changes model behavior. Effective authority is therefore structurally implemented, not behaviorally measured in the source.

**Other consumers.** Humans and operators consume the same memory through REST/SDK APIs, block/file endpoints, tests, git-backed repositories, run records, and context-window inspection. Git-backed memory also makes a subset of blocks inspectable outside the live service.

## Curiosity Pass

**Letta's "memory" spans several authority levels.** A block rendered into the system prompt, an archival passage searched by a tool, a source passage, and a summary message are all called memory-like things, but they do not have the same activation path or authority.

**The most Commonplace-like feature is not the vector store.** The git-backed block repository is the interesting bridge: it turns memory blocks into Markdown files with version history while leaving server APIs in charge of synchronization.

**Sleeptime shifts trust to another agent.** Background maintenance is powerful, but its edits inherit the same LLM judgment risks as any summarizer. The tests verify wiring and some behavior, not general edit quality.

**The prompt-rendered metadata is valuable even when content is not loaded.** Counts and tags give the agent a map of available out-of-context memory. That is a lower-risk affordance than pushing arbitrary retrieved memories into every turn.

**Compaction summaries are memory, not just cleanup.** Once persisted in the conversation stream, they become the retained representation of evicted trace windows and deserve lineage and quality treatment.

## What to Watch

- Whether git-backed memory becomes the default memory substrate or remains a tagged mode; that decides whether Letta moves closer to reviewable file-native memory.
- Whether sleeptime memory edits gain stronger provenance, review queues, or diff approval before updating prompt-rendered blocks.
- Whether core-memory prompt injection gains semantic selection or priority budgets beyond block attachment and labels.
- Whether compaction stores prompt/model/source-window metadata sufficient to regenerate or audit summary messages.
- Whether archival/recall search becomes automatically invoked before actions in a host integration; that would extend push activation beyond core blocks.
- Whether tests evolve from structural wiring checks to memory faithfulness checks that measure behavior with and without pushed memory.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Letta derives block edits, archival memories, and compaction summaries from conversation/tool traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Letta's core blocks are activated by prompt compilation, while archival storage requires search.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Letta requires separating blocks, messages, passages, summaries, files, tool rules, and git memory by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: archived passages, recall messages, source passages, and summary messages usually advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt-rendered core blocks, tool rules, memory renderers, and git-memory sync rules configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Letta turns conversational traces into durable memory edits and summaries through agents and compaction.
