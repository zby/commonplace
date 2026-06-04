---
description: "Letta review: stateful agent server with core memory blocks, archival and recall tools, compaction, sleeptime memory agents, and optional git-backed memory"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
status: current
last-checked: "2026-06-04"
---

# Letta

Letta, from `letta-ai/letta`, is the open-source server behind Letta agents and the successor to MemGPT. At the reviewed commit it stores stateful agents, messages, memory blocks, passages, files, tools, and groups in a database-backed service; renders selected core memory into the model's system prompt; exposes explicit recall and archival-memory tools; and includes compaction plus background "sleeptime" agents that can update memory from conversation or document traces.

**Repository:** https://github.com/letta-ai/letta

**Reviewed commit:** [1131535716e8a31c9a437f8695e25ac98f203a24](https://github.com/letta-ai/letta/commit/1131535716e8a31c9a437f8695e25ac98f203a24)

**Last checked:** 2026-06-04

## Core Ideas

**Core memory is rendered into the prompt, not retrieved on demand.** `Memory.compile()` renders memory blocks as `<memory_blocks>` for ordinary agents, line-numbered blocks for selected Anthropic-backed agent types, and a structured git-memory view for git-enabled agents; `PromptGenerator` injects that compiled memory and a `<memory_metadata>` count block into the system prompt, appending the memory placeholder if the base prompt omits it ([memory.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/schemas/memory.py), [prompt_generator.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/prompt_generator.py)). This is a push path for core memory: the agent sees the blocks before each model call.

**External memory stays behind explicit tools.** Recall memory is prior messages searched by `conversation_search`; archival memory is long-term passages inserted and searched by `archival_memory_insert` / `archival_memory_search` with semantic search when the agent has an embedding config, plus tag and date filters ([base.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/functions/function_sets/base.py), [core_tool_executor.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/tool_executor/core_tool_executor.py), [agent_manager.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/agent_manager.py)). The prompt metadata tells the agent those stores exist, but the content is not automatically spliced into the prompt.

**Context efficiency is a three-layer policy.** Small, high-salience core blocks are always visible; larger recall and archival stores are pulled by tools with limits; overflowing active context is compacted into summary messages and a shorter in-context message list ([agent.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/agent.py), [compact.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/summarizer/compact.py), [summarizer.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/summarizer/summarizer.py)). The tradeoff is visible: core memory can dilute every call if bloated, while archival/recall require the agent to choose to search.

**Memory writes are ordinary tool/API mutations plus optional background memory work.** Foreground agents can append or replace core blocks and insert archival passages through built-in tools; server APIs and managers can create/update blocks, tools, messages, files, and archives. When `enable_sleeptime` is set, a separate sleeptime agent receives the foreground conversation transcript after a turn or at a configured frequency and is instructed to edit shared memory blocks until they are organized, readable, and current ([sleeptime_multi_agent_v4.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/groups/sleeptime_multi_agent_v4.py), [sleeptime_v2.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/system_prompts/sleeptime_v2.py), [server.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/server/server.py)).

**The optional git memory path adds versioned files without replacing the DB cache.** Agents tagged `git-memory-enabled` write memory blocks to a git-backed repository first, then sync PostgreSQL as a cache; local self-hosted storage lives under `~/.letta/memfs`, and block files are Markdown with YAML frontmatter for description/read-only/metadata ([block_manager_git.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/block_manager_git.py), [memfs_client_base.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/memfs_client_base.py), [block_markdown.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/memory_repo/block_markdown.py)).

**Tool state is also behavior-shaping memory.** Letta stores tool definitions, rules, schemas, execution settings, MCP metadata, and optional Turbopuffer embeddings; updates can regenerate schemas, redeploy Modal apps, and refresh tool embeddings ([tool_manager.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/tool_manager.py)). This is not the same as autobiographical memory, but it is durable state that changes what future agents can do.

## Artifact analysis

- **Storage substrate:** `rdbms` — The central live store is SQL-backed agent, block, message, passage, tool, file, group, run, and history state; embeddings may live in SQL vector columns or Turbopuffer, and git-backed memory is an optional versioned source for blocks rather than the default active substrate.
- **Representational form:** `prose` `symbolic` `parametric` — Memory blocks, prompts, messages, summaries, archival passages, and tool source are prose; schemas, metadata, tags, tool rules, IDs, groups, run state, and git frontmatter are symbolic; message/passage/tool embeddings are parametric retrieval structures.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author blocks, tools, archives, and prompts; source/file passages can be imported; messages, compaction summaries, sleeptime edits, voice-sleeptime stores, and provider traces derive from conversations, tool calls, and execution events.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Blocks and recalled passages advise as knowledge; core memory and system prompts instruct; read-only flags, tool rules, schemas, permissions, and context limits enforce or validate; tags, IDs, groups, archives, and source attachments route; embeddings and full-text search rank; compaction and sleeptime implement learning from traces.

**Core memory blocks.** Blocks are SQL rows with labels, descriptions, values, char limits, read-only flags, hidden flags, metadata, version counters, and agent/group/identity links ([block.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/block.py)). Their value and description are prose; labels, limits, permissions, and links are symbolic; their authority becomes instruction-like when rendered into the system prompt.

**Archival passages and source passages.** Passages store text, metadata, tags, embedding configuration, and optional embeddings, with separate archive/source identity ([passage.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/orm/passage.py)). Archival passages are agent-created long-term knowledge; source passages are imported document knowledge; both become ranking inputs when embedding or text search is used.

**Recall messages and summary messages.** Messages are durable conversation traces; compaction creates summary messages from older in-context messages and replaces the active context list with system + summary + retained recent messages ([agent.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/agent.py), [compact.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/services/summarizer/compact.py)). Raw messages are trace-extracted knowledge/audit artifacts; summaries are trace-extracted distilled prose that changes later context.

**Sleeptime and document-sleeptime agents.** Sleeptime agents are separate agents linked to the foreground agent's shared blocks. They receive completed conversation transcripts or source-ingest tasks and use memory editing tools to update blocks ([sleeptime_multi_agent_v4.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/groups/sleeptime_multi_agent_v4.py), [sleeptime_doc_ingest.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/system_prompts/sleeptime_doc_ingest.py)). The durable outputs are block edits; the operative policy is authored prompt/tool instruction plus trace-derived block content.

**Tools and tool rules.** Tools are durable system-definition artifacts: source code, schemas, names, types, requirements, metadata, execution settings, and optional embeddings decide what actions and search surfaces future agents can access. Tool updates are ordinary authored/API mutations unless a host workflow uses conversation evidence to generate or edit them.

Promotion path: Letta promotes raw traces into summary messages and, through sleeptime agents, into edited core memory blocks. It can also promote memory blocks into git-versioned Markdown for agents with the git-memory tag. It does not show a Commonplace-style promotion path from candidate memory to independently reviewed note, instruction, or validator; authority mainly comes from being injected into prompt context or becoming an available tool/rule.

## Comparison with Our System

| Dimension | Letta | Commonplace |
|---|---|---|
| Primary purpose | Runtime stateful-agent server with memory, tools, files, groups, and APIs | Git-native methodology KB for agents and maintainers |
| Canonical retained artifact | SQL agent state: core blocks, messages, passages, tools, groups, summaries | Typed Markdown notes, reviews, instructions, sources, indexes, validation reports |
| Read-back | Core blocks push into system prompt; archival/recall are explicit tools | Mostly explicit pull through search, indexes, links, and loaded instructions |
| Write path | Agent tools, API writes, compaction, sleeptime background agents, optional git block commits | Human/agent-authored repo artifacts, snapshots, validation, semantic review |
| Governance | Tool schemas/rules, read-only blocks, context limits, DB permissions, git history for selected agents | Collection contracts, type specs, deterministic validation, review gates, git diffs |

Letta is stronger as an application runtime: it owns agent execution, message storage, tool execution, file/source ingestion, streaming, compaction, and multi-agent background memory maintenance. Commonplace is stronger as an inspectable knowledge system: most behavior-shaping state is directly visible in Markdown, validated against type contracts, and reviewable through ordinary git history.

The key design difference is read-back. Letta's core memory is designed to act without a search step; Commonplace usually makes the agent decide what to load. That gives Letta better continuity for agent applications, but it also makes prompt-bloat and unreviewed memory authority central risks. Commonplace's slower pull model keeps authority more explicit.

### Borrowable Ideas

**Separate always-visible core from searched archives.** Ready now as vocabulary. Commonplace could distinguish "session core" from "library/archive" when designing workshop memory, while keeping automatic core insertion small and scoped.

**Use memory metadata as affordance, not evidence.** Letta's prompt metadata tells the agent how many recall/archival items exist and which tags are available. Commonplace could expose index/report counts to guide search without pretending the content has been loaded.

**Borrow background memory agents only inside workshops.** Sleeptime is useful for after-action cleanup, but Commonplace should first route this into temporary workshop artifacts or review candidates, not directly into durable library notes.

**Git-backed memory blocks are a useful convergence point.** Letta's optional Markdown/frontmatter block repository points toward a runtime memory surface that agents can edit and humans can diff. Commonplace could borrow the cache/source-of-truth split only where a service runtime is actually needed.

**Do not borrow silent core-memory authority.** Letta's core blocks become prompt instructions by default. For Commonplace, unreviewed extracted memories should remain advisory until promoted through collection/type validation.

## Write side

**Write agency:** `manual` `automatic` — Foreground agents, users, API clients, and operators can create/update/delete blocks, passages, messages, tools, files, and git memory files; automatic paths compact message traces and run sleeptime agents that update shared memory blocks after foreground conversations or document-ingest events.

**Curation operations:** `consolidate` `evolve` — Compaction summarizes older in-context messages into one retained summary message; sleeptime and document-sleeptime agents rewrite existing memory blocks from new conversation/source evidence. Index/embedding refreshes and ordinary passage/tool inserts are access upkeep or acquisition, not curation operations.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Letta stores conversation messages, tool calls/returns, steps, runs, provider traces, compaction events, and foreground-response transcripts used by sleeptime agents.

**Learning scope:** `per-task` `per-project` `cross-task` — Raw runs are per conversation/task; retained blocks, passages, summaries, and tools are agent/project scoped and can affect later tasks with the same agent.

**Learning timing:** `online` `staged` — Foreground tool writes and compaction happen during or around agent steps; sleeptime agents run after turns or at configured frequency; document-sleeptime ingestion is triggered after source/file events.

**Distilled form:** `prose` `symbolic` `parametric` — Distilled outputs include prose block edits, summary messages, archival passages, source-derived memory blocks, symbolic tags/metadata/run records, and embeddings used for later retrieval.

**Extraction.** Compaction uses configured summarizer modes to turn old in-context messages into a packed summary message with optional compaction stats. Sleeptime uses a background agent prompt as the oracle: it reads a transcript, decides whether memory edits are warranted, and applies precise or broad memory editing tools. Voice sleeptime similarly stores older dialogue and rewrites the human memory block under a required tool-call sequence ([voice_sleeptime.py](https://github.com/letta-ai/letta/blob/1131535716e8a31c9a437f8695e25ac98f203a24/letta/prompts/system_prompts/voice_sleeptime.py)).

**Scope and timing.** The strongest trace-derived loop is not archival insertion; that can be ordinary authored memory. The qualifying loops are compaction and sleeptime because they derive durable summaries or block edits from messages that have already occurred. Tool edits are durable and behavior-shaping, but in the inspected code they are ordinary API/tool-manager updates unless a separate workflow supplies a trace-derived generation step.

**Survey fit.** Letta belongs in the trace-to-core-memory family: raw conversational traces are distilled into prompt-visible blocks or summaries, and those artifacts can affect later actions without another retrieval call. It also illustrates the need to distinguish trace-derived write paths from ordinary memory editing tools that the foreground agent calls intentionally.

## Read-back

**Read-back:** `both` — Core memory blocks, file blocks, tool rules, source directories, and memory metadata are pushed into the system prompt; recall and archival contents are pull-only through explicit conversation and archival search tools.

**Read-back signal:** `coarse` `identifier` — Core memory is coarse always-load; metadata and block/file selection are narrowed by agent/source/file identifiers. Recall and archival searches use query text, tags, date filters, and optional embedding search only after the agent invokes a pull tool, so those retrieval signals do not classify the push path.

**Faithfulness tested:** `no` — The repo has unit/integration tests for prompt rendering, cache invalidation, compaction, search, and sleeptime mechanics, but I did not find a with/without memory ablation proving that pushed core memory or summaries changed downstream behavior faithfully.

**Direction edge cases.** The external-memory metadata block is push, but it pushes availability/counts/tags rather than memory contents. Core blocks and open files are memory read-back because they are retained agent state rendered before the LLM call. Archival and recall search tools are pull even when their results are semantic or hybrid, because the agent must call the tool.

**Targeting and signal.** Core push is mostly coarse within the agent: all renderable blocks are included for standard agents, while git-enabled agents render `system/*` blocks and a structured memory/external file tree. Pull retrieval is instance-targeted through agent IDs, archive/source IDs, tags, roles, dates, and query text; semantic archival search uses embeddings when available.

**Injection point.** Read-back happens during system prompt assembly and LLM request construction. Compaction and sleeptime work after a turn or around overflow handling, so they are write-side maintenance; their outputs affect later reads when the updated summary/block is rendered or searched.

**Selection, scope, and complexity.** Core memory has character limits and optional line-number rendering, but no retrieval ranking because it is always included. Archival and recall paths use limits, tag/date filters, text search, and embedding search; source/file rendering uses open-file and max-file controls. Actual context dilution from large blocks or many files is not proven by code.

**Authority at consumption.** Core memory has strong prompt-context authority because it sits in the system message. Archival/recall results are advisory tool results. Tool rules and schemas can constrain action selection, while read-only flags and execution validators enforce selected boundaries.

**Other consumers.** Humans and operators consume memory through REST APIs, SDKs, the admin/developer surface, git memory repositories, source/file endpoints, run records, and tests. Background agents, compaction routines, search managers, and tool executors consume the same retained state operationally.

## Curiosity Pass

**Letta's memory story is not one store.** Core blocks, recall messages, archival passages, source passages, summary messages, files, tools, and optional git repos all shape later behavior differently.

**The clearest push is the least searchable memory.** Core memory is reliable because it is always rendered, but it depends on the block remaining compact and current. The richer recall/archive stores need explicit tool use.

**Sleeptime is a high-authority trace learner.** It edits the same blocks the foreground agent later sees as prompt context. That is more consequential than storing an archival passage that must later be searched.

**Git-backed memory is an adoption bridge, not the whole product.** It gives diffable block history for selected agents, but much of Letta's active state remains database/service state: messages, passages, tools, runs, groups, and embeddings.

**Tool memory deserves separate review.** Durable tool definitions and rules can change future behavior as much as autobiographical facts, but their lineage and review surface differ from user-memory blocks.

## What to Watch

- Whether git-backed memory expands from core blocks to messages, archival passages, tools, and summaries; that would shift Letta toward auditable repo memory rather than DB-first state.
- Whether sleeptime outputs gain per-edit provenance linking block changes back to exact source messages, run IDs, prompts, and model settings.
- Whether evaluations add behavioral ablations for pushed core memory, compaction summaries, and sleeptime edits rather than only structural prompt/search tests.
- Whether tool-generation or tool-edit workflows become trace-derived and automated in the open-source server; that would raise tool definitions from authored system state to learned system-definition artifacts.
- Whether archival search gets stronger freshness, contradiction, and expiry semantics; current passages are persistent knowledge unless a caller edits or deletes them.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Letta derives summaries and sleeptime memory edits from conversation/session traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Letta's core blocks are pushed into context, while archival and recall stores require explicit search tools.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Letta's blocks, messages, passages, tools, embeddings, and git files differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: archival passages, recall search results, source passages, and summaries mostly advise as context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: system prompts, core-memory rendering, tool rules, schemas, read-only flags, and background memory policies.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Letta's compaction and sleeptime loops turn traces into durable behavior-shaping memory.
