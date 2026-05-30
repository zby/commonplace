---
description: "Letta review: agent-self-managed memory with core blocks, archival passages, recall search, compaction summaries, sleeptime editing, and git-backed block history"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-30"
---

# Letta

Letta, from Letta AI, is a stateful agent platform descended from MemGPT. The code retains the familiar three-tier memory interface: core memory blocks are rendered into the system prompt, recall memory is stored conversation history searchable by tool, and archival memory is a persistent passage store the agent can explicitly write and search. Around that base interface, current Letta layers compaction summaries, file/git-backed block storage, source blocks, and optional background "sleeptime" agents. Its most distinctive design choice is the agency boundary: ordinary Letta agents receive memory tools and are instructed to manage memory themselves, while the framework handles storage, message persistence, prompt rebuilds, compaction, and optional background memory maintenance.

**Repository:** https://github.com/letta-ai/letta

**Reviewed commit:** [1131535716e8a31c9a437f8695e25ac98f203a24](https://github.com/letta-ai/letta/commit/1131535716e8a31c9a437f8695e25ac98f203a24)

**Last checked:** 2026-05-30

## Core Ideas

**Core memory is prompt-resident block state, not just a prompt string.** `AgentState` stores a `Memory` object and a list of `Block` objects, while the ORM maps blocks through `blocks_agents` as an agent's `core_memory` relationship ([agent schema](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/agent.py), [agent ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/agent.py)). A block has `label`, `description`, `value`, `limit`, `read_only`, metadata, tags, and history/version fields; the block ORM calls it a section of LLM context ([block schema](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/block.py), [block ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/block.py)). `Memory.compile()` renders these blocks as XML-like `<memory_blocks>` with descriptions, current size, limits, read-only markers, and values; git-enabled agents render `system/*` labels as a structured `<self>` plus `<memory>` projection instead ([memory renderer](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/memory.py)).

**The agent is explicitly taught the memory hierarchy.** The classic MemGPT prompt tells the model that recall memory is searchable conversation history, core memory is always in context and editable with `core_memory_append`/`core_memory_replace`, and archival memory is outside immediate context and accessible through `archival_memory_insert`/`archival_memory_search` ([MemGPT prompt](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/system_prompts/memgpt_chat.py)). The newer v2 prompt generalizes this to memory blocks, retrieval tools, and external memories without hard-coding every tool name in the prompt body ([v2 prompt](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/system_prompts/memgpt_v2_chat.py)). The memory metadata block injected into the system prompt also tells the agent how many previous messages are in recall memory, how many archival memories exist, and which archive tags are available ([prompt generator](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/prompt_generator.py)).

**Core memory editing is agent-invoked but framework-persisted.** The base tool definitions expose `core_memory_append`, `core_memory_replace`, precise string replacement/insertion, full-block rethink, and a multi-block patch-style `memory_apply_patch` contract ([base function set](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/functions/function_sets/base.py)). At runtime, `LettaCoreToolExecutor` maps those function names to direct implementations that mutate `agent_state.memory`, enforce read-only blocks and line-number guardrails, then call `update_memory_if_changed_async()` or rebuild the system prompt ([core tool executor](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/tool_executor/core_tool_executor.py)). The agent chooses the edit; the framework validates, persists, and recompiles.

**Archival memory is a passage/archive store with optional vector backend.** An archive is a named collection shared through `archives_agents`; the current relationship has a uniqueness constraint that leaves one archive per agent for now ([archive ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/archive.py), [archives-agents mapping](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/archives_agents.py)). Archival passages store text, embedding config, tags, metadata, archive id, and optional vector embeddings in SQL or pgvector-like storage ([passage ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/passage.py)). `archival_memory_insert` calls `passage_manager.insert_passage()`, which creates the default archive, embeds text when embedding config exists, writes SQL first, and dual-writes to Turbopuffer for archives configured with that vector provider ([passage manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/passage_manager.py), [core tool executor](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/tool_executor/core_tool_executor.py)).

**Recall memory is ordinary message history plus search indexes.** Messages persist as rows with roles, content parts, model, tool calls, tool returns, run/step ids, conversation ids, approvals, and sequence ids ([message ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/message.py)). In-context membership is tracked separately in `conversation_messages`, including position and `in_context` state ([conversation message ORM](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/conversation_messages.py)). `conversation_search` is a base tool whose executor searches messages by hybrid mode when Turbopuffer is enabled and falls back to SQL text search otherwise, filtering recursive search/tool artifacts before returning structured results ([message manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/message_manager.py), [core tool executor](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/tool_executor/core_tool_executor.py)).

**The framework creates the available memory tools.** Base tools are declared centrally: `conversation_search`, archival insert/search, core block tools, and newer `memory`/patch-style tools ([constants](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/constants.py)). Agent creation attaches different tool sets depending on agent type and `enable_sleeptime`; normal agents get search plus memory-edit tools, whereas sleeptime-enabled foreground agents keep chat/search tools and offload editing to the background memory agent ([agent creation](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/agent_manager.py), [base tool calculation](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/helpers/agent_manager_helper.py)).

**Git-backed memory is implemented as a source-of-truth option for blocks.** `GitEnabledBlockManager` activates when an agent has the `git-memory-enabled` tag. Writes go to git first, then PostgreSQL is updated as cache; reads still come from PostgreSQL for performance ([git block manager](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/block_manager_git.py)). The open-source `MemfsClient` stores each block as `{label}.md` with YAML frontmatter for description/read-only/metadata, keeps local git repos under `~/.letta/memfs`, and exposes history and block reads by commit ref ([memfs client](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/memfs_client_base.py), [block markdown](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/block_markdown.py), [local storage](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/storage/local.py)). `GitOperations` shells out to git, uses a Redis lock around commits, uploads `.git` object data to the configured storage backend, and records `MemoryCommit` metadata ([git operations](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/git_operations.py), [memory repo schema](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/memory_repo.py)).

**Compaction and sleeptime are distinct framework-driven loops around the agent-owned memory tools.** Compaction is trace distillation for context management: when context overflows or post-step checks trip the threshold, Letta compacts messages, creates a summary message, checkpoints it, and refreshes the system prompt ([agent v3 compaction path](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/agents/letta_agent_v3.py), [compact service](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/summarizer/compact.py)). Sleeptime is background memory maintenance: `enable_sleeptime` creates a paired `sleeptime_agent` sharing the main agent's blocks, and the sleeptime loop periodically reviews foreground conversation messages and asks the background agent to update relevant memory blocks ([server sleeptime creation](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/server/server.py), [sleeptime loop](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/groups/sleeptime_multi_agent_v4.py), [sleeptime prompt](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/system_prompts/sleeptime_v2.py)).

## Comparison with Our System

| Dimension | Letta | Commonplace |
|---|---|---|
| Primary artifact | Agent state: blocks, messages, archives, passages, tools, prompts, runs, optional git memory repos | Git-tracked Markdown notes, instructions, reviews, sources, ADRs, schemas, generated reports |
| Storage substrate | PostgreSQL/SQLite rows, optional pgvector/Turbopuffer/Pinecone-style vector backends, optional git-backed block repositories | Filesystem and git as primary substrate |
| Representational form | Prose blocks and passages, symbolic tool schemas and DB rows, vector embeddings, prompt templates, git commits | Mostly prose with frontmatter, typed links, schemas, scripts, validation and review reports |
| Lineage | Message/run/step ids, block history/version, compaction stats, git commits for enabled memory repos | Source snapshots, commit-pinned reviews, authored links, git history, archive/replacement lifecycle |
| Agency model | Acting agent or sleeptime agent invokes memory tools; framework persists, searches, compacts, rebuilds prompts | Human/agent collaboration writes durable artifacts; instructions and validators constrain edits |
| Authority | Prompted memory policy, tool rules, read-only flags, tool executor checks, compaction thresholds, vector ranking | Collection contracts, type specs, AGENTS.md, skills, deterministic validation, semantic review |

Letta is the clearest code-grounded example of agent-self-managed memory in this review set. The acting model is told that memory editing is part of its identity and is given tools that directly mutate retained state. The framework does not decide which user fact belongs in the human block or archival memory during ordinary operation; it exposes the machinery and depends on model judgment.

That agency claim has two important qualifications. First, the framework owns persistence and activation mechanics: it stores every message, maintains recall indexes, injects memory metadata, recompiles the system prompt when blocks change, compacts overflowing context, and enforces tool/read-only errors. Second, with `enable_sleeptime`, memory management shifts from the foreground agent to a background agent. The memory decision is still made by an LLM agent, but no longer by the same agent that just answered the user.

Compared with commonplace, Letta is stronger as a live stateful-agent runtime. It has an API, SDK-facing state model, typed tools, run metrics, multiple model providers, message search, archival vector retrieval, multi-agent groups, approvals, and background processing. Commonplace is stronger as a reviewable knowledge system: notes and instructions are durable files with explicit type contracts, link semantics, validation, and human-readable lineage. Letta's git-backed blocks move in the same direction, but they cover memory blocks, not the whole system of sources, claims, indexes, procedures, and review gates.

Read-back direction verdict: Letta is both push and pull from the agent's perspective. Core memory blocks, memory metadata, and compaction summaries are pushed into context by prompt construction or compaction; archival memory and recall memory are pull surfaces the agent must explicitly search. Because the main activation path is unconditional core-memory load plus agent-initiated search, not relevance-gated unsolicited memory selection, this review does not add the `push-activation` tag.

## Borrowable Ideas

**Treat the agency boundary as a first-class design axis.** Ready to borrow. Letta makes "who decides what to remember" concrete: foreground agent, background memory agent, or framework. Commonplace should use the same distinction when comparing skills, review loops, and automated note promotion.

**Expose memory counts and paths as prompt metadata.** Worth borrowing in small form. Letta's `<memory_metadata>` does not retrieve content, but it tells the agent that recall and archival stores exist and how large they are. Commonplace could give agents compact inventory signals for reports, notes, or pending reviews without loading the artifacts themselves.

**Use read-only flags on prompt-resident memory.** Ready as an implementation pattern if commonplace ever adds editable prompt-resident state. Letta's block-level `read_only` flag is enforced by the executor, not only by prompt instruction.

**Separate foreground work from background memory maintenance.** Useful but needs a real workflow. The sleeptime split prevents every user-facing turn from doing memory cleanup inline. A commonplace analogue would be a background review/promote job that proposes updates, not a hidden process that silently rewrites canonical notes.

**Git-backed memory blocks are strong convergence evidence.** Letta started from database-backed blocks and now has an implemented file-and-git source-of-truth option for blocks. The borrowable idea is not its storage-object dance; it is the recognition that memory history, diffs, and inspectable text matter even inside a hosted agent platform.

**Do not borrow self-edited memory without review gates for high-authority artifacts.** Letta's model works for adaptive user/persona memory, but commonplace methodology notes and instructions have stronger downstream authority. Agent-only edits should remain candidates until reviewed, validated, or promoted through explicit contracts.

## Trace-derived learning placement

Letta qualifies as trace-derived learning, with several distinct outputs rather than one memory artifact.

**Trace source.** The primary trace is live conversation and tool activity stored as messages with roles, tool calls, tool returns, run ids, step ids, conversation ids, approvals, and sequence ids. The acting agent sees a bounded in-context slice, while recall keeps the larger conversation history searchable. The sleeptime path consumes foreground response messages and, when configured, messages since the last processed id.

**Extraction.** There are three extraction oracles. In ordinary operation, the foreground agent itself decides whether to call `core_memory_append`, `core_memory_replace`, `memory_*`, or `archival_memory_insert`. Under context pressure, the framework asks a summarizer model or the agent's own model to summarize messages into a compact summary message. With sleeptime enabled, a separate background agent reviews prior conversation text and uses memory editing tools to update shared blocks.

**Storage substrate.** Raw traces persist in the messages tables and optional Turbopuffer message index. Core-memory distillates persist as block rows, or as Markdown files plus git history when git memory is enabled. Archival distillates persist as archival passages in SQL with optional vector storage. Compaction summaries persist as summary/user-style messages that are inserted back into the in-context sequence and saved with the rest of message state.

**Representational form.** Raw messages are structured symbolic rows wrapping prose content and tool payloads. Core blocks, archival passages, and compaction summaries are prose. Tool schemas, tool rules, read-only flags, block labels, archive ids, tags, and compaction thresholds are symbolic. Embeddings and vector indexes are distributed-parametric retrieval state. Git commit metadata is symbolic lineage around prose memory files.

**Lineage.** The strongest lineage is operational: message ids, run/step ids, sequence ids, compaction stats, block history/version fields, and git commits. The weakest lineage is semantic: a core-memory statement or archival passage does not necessarily point back to the exact conversation turns that justified it unless the agent wrote that provenance into the prose. Git-backed blocks improve edit history but do not by themselves prove that the edit was faithful to the source trace.

**Behavioral authority.** Raw messages and archival passages are knowledge artifacts when searched as evidence or context. Core blocks are stronger: they are prompt-resident knowledge artifacts with persistent advisory force on every future step. Tool rules, prompt templates, read-only flags, executor validations, compaction thresholds, vector ranking, and git/SQL sync policy are system-definition artifacts because they configure, route, constrain, or rank behavior. Sleeptime outputs become high-authority memory when written into shared blocks.

**Scope and timing.** Scope is per agent, per conversation, per archive, per organization, and sometimes per shared block or group. Timing is online during deployment: the acting agent can edit memory in the middle of a turn, compaction runs when context management requires it, and sleeptime agents run after foreground turns at configured intervals.

**Survey placement.** Letta strengthens the survey's agent-self-managed trace-to-memory lane. It splits the trace-derived family into foreground self-editing, framework compaction, and background-agent memory maintenance. It does not strengthen the claim that traces should automatically promote into reviewed instructions, tests, or skills; Letta's durable outputs remain memory blocks, passages, summaries, and git-backed block histories.

## Curiosity Pass

**Letta is less "the framework remembers" than "the framework gives agents a memory operating system."** The code keeps the memory policy mostly in prompt/tool use, while the platform handles the machinery around it.

**The current three-tier story is now mixed with newer file and sleeptime abstractions.** Core/recall/archival remains real, but current code also has source/file blocks, memory filesystem rendering, client skills, compaction summaries, background memory agents, and git-backed block repos.

**Git memory is implemented, but it is not yet a full files-first KB.** Blocks become Markdown files with commit history, but tags remain Postgres-only metadata, PostgreSQL remains the read cache, and archives/recall still live in service storage.

**Self-managed memory is model-capability dependent.** The tool executor can reject malformed edits and enforce read-only blocks, but it cannot know whether a chosen memory edit is worth keeping. That policy remains in the LLM or the sleeptime LLM.

**Compaction is trace distillation, not necessarily durable knowledge.** A summary message helps preserve continuity as context is trimmed, but it is not the same as a reviewed fact, rule, or instruction.

## What to Watch

- Whether git-backed memory expands from core blocks to archival passages, sources, skills, and agent configuration.
- Whether block edits gain semantic provenance from source message ids or compaction runs.
- Whether sleeptime agents get stronger review, approval, or rollback workflows before edits affect foreground behavior.
- Whether archival memory deletion, contradiction handling, and consolidation become as explicit as insertion/search.
- Whether Letta adds evaluation that tests memory usefulness by downstream behavior rather than by successful storage and retrieval.
- Whether hosted and local deployments keep the same memory semantics as storage backends diverge.

---

Relevant Notes:

- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - analogizes: Letta's self-managed memory depends on model judgment about what should be saved, edited, or ignored, though it does not use AgeMem's RL oracle.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: Letta separates always-loaded core memory from pull-only archival and recall search.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: Letta's memory hierarchy exists because context is scarce and must be managed.
- [Files not database](../../notes/files-not-database.md) - extends: Letta's git-backed memory blocks are convergence evidence from a database-first agent platform toward inspectable files.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: messages, archival passages, summaries, and memory blocks advise future agent behavior when read back.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: tools, tool rules, prompt rendering, read-only flags, compaction thresholds, and retrieval rankings configure or constrain behavior.
