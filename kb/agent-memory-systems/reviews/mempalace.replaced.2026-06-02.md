---
description: "MemPalace review: local Chroma drawer memory with conversation mining, hooks, MCP tools, diaries, temporal SQLite KG, and retrieval-first activation"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# MemPalace

> Replaced 2026-06-02. See [mempalace](./mempalace.md) for the current review.

MemPalace is a local-first Python memory system by milla-jovovich for filing project files, conversations, agent diaries, and facts into a searchable "palace." The reviewed implementation uses ChromaDB as the primary drawer store, SQLite for a temporal knowledge graph, a fixed MCP server tool surface, Claude/Codex hooks for automatic capture, and a retrieval protocol that asks agents to check memory before answering about people, projects, or past events. Its strongest design claim is retrieval-first: preserve verbatim source chunks, build lightweight indexes and routing metadata around them, and let wake-up/search/tool protocols do most of the behavior-shaping work.

**Repository:** https://github.com/milla-jovovich/mempalace

**Reviewed commit:** [d0163a7bec5ee6faa5e86169ed407a7bf41d5582](https://github.com/milla-jovovich/mempalace/commit/d0163a7bec5ee6faa5e86169ed407a7bf41d5582)

**Last checked:** 2026-05-16

## Core Ideas

**The canonical memory object is a Chroma drawer, usually verbatim.** The project README says MemPalace stores conversation history as verbatim text rather than summaries, with people/projects as wings, topics as rooms, and original content as drawers ([README.md](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/README.md)). The code mostly implements that: project mining chunks readable files into 800-character drawers with overlap, conversation mining chunks by exchange or paragraph, message sweeping writes one drawer per user/assistant message, and MCP writes use deterministic drawer ids over wing/room/content ([miner.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/miner.py), [convo_miner.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/convo_miner.py), [sweeper.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/sweeper.py), [mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/mcp_server.py)). Storage substrate is local Chroma under `~/.mempalace/palace` by default, with collection name configurable and Chroma wrapped behind a backend abstraction ([config.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/config.py), [backends/chroma.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/backends/chroma.py)).

**Closets are a derived retrieval layer, not the source of truth.** `build_closet_lines()` extracts topics, repeated entities, quotes, and drawer references into compact pointer lines, then `upsert_closet_lines()` packs them into `mempalace_closets` documents without splitting a topic line ([palace.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/palace.py)). Search always queries drawers directly; closet hits add rank-based boost and neighbor expansion, but the drawer query remains the floor ([searcher.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/searcher.py)). The representational form therefore splits cleanly: drawers are prose/mixed evidence, closets are symbolic/prose pointer indexes, and Chroma embeddings are distributed-parametric retrieval indexes.

**Source and conversation mining preserve raw material but still add heuristics.** `mempalace init` samples source files for corpus-origin detection, optionally refines persona/platform fields with an LLM, writes `origin.json`, discovers entities, writes per-project `entities.json`, updates `known_entities.json`, detects rooms, and can auto-mine afterward ([cli.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/cli.py)). Project mining respects `.gitignore`, skips generated directories and risky files, loads `mempalace.yaml` when present, routes files to rooms, and writes closets beside drawers. Conversation mining treats large transcript files as valid inputs, normalizes content, chunks exchanges, writes registry sentinels for empty files, and can apply a general extraction mode ([convo_miner.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/convo_miner.py)). The README's "does not summarize, extract, or paraphrase" is true of the headline raw retrieval path, but not of the whole system: origin detection, entity extraction, closet generation, AAAK, diaries, and KG tools are extraction or compression layers around the verbatim drawers.

**Stop and precompact hooks turn traces into capture triggers.** The shell hooks auto-mine the active transcript into the palace and can block the agent with a reason message before stopping or compacting, with loop-prevention state under `~/.mempalace/hook_state` ([hooks/README.md](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/hooks/README.md), [mempal_save_hook.sh](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/hooks/mempal_save_hook.sh), [mempal_precompact_hook.sh](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/hooks/mempal_precompact_hook.sh)). The hook design gives raw traces knowledge-artifact status as evidence, while the hook configuration and blocking decisions are system-definition artifacts: they schedule capture and can force the agent to record material before context disappears.

**Wake-up is a layered context surface over the same drawer store.** `MemoryStack` renders L0 identity from `~/.mempalace/identity.txt`, L1 "essential story" from high-weight/recent drawers, L2 filtered wing/room retrieval, and L3 deep semantic search ([layers.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/layers.py)). This is not a separate memory store; it is a context scheduler and prompt-construction view over retained drawers. The behavioral authority comes from activation timing: wake-up text and MCP protocol reminders shape what the agent sees before it decides whether to search.

**The MCP server is the main behavior-shaping interface.** The server exposes 29 named tools across status, taxonomy, AAAK spec, KG query/add/invalidate/timeline/stats, graph tunnels, search, duplicate checks, drawer CRUD, sync, diaries, hook settings, checkpoint acknowledgement, and reconnect ([mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/mcp_server.py)). It also embeds the MemPalace protocol in status responses: on wake-up call status, before answering about people/projects/past events query memory first, write a diary after each session, and invalidate old facts before adding changed facts. That protocol is a prose system-definition artifact; drawers and KG facts advise, but MCP tool schemas, query sanitization, validation, WAL logging, and the protocol create routing and instruction force.

**The temporal KG is real but sidecar, not the primary retrieval substrate.** `KnowledgeGraph` stores entities and triples in SQLite with `valid_from`, `valid_to`, confidence, source closet/file/drawer provenance fields, UTC/date validation, and invalidation/timeline queries ([knowledge_graph.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/knowledge_graph.py)). The MCP server uses `~/.mempalace/knowledge_graph.sqlite3` by default, or `<palace>/knowledge_graph.sqlite3` when `--palace` is passed. The checked-in `docs/schema.sql` still says `knowledge_graph.db` and omits newer provenance columns such as `source_drawer_id` and `adapter_name`, so the code is the more current source for KG behavior ([docs/schema.sql](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/docs/schema.sql)).

**Maintenance is practical and defensive.** The Chroma backend sets cosine/HNSW metadata, pins HNSW threads, guards against link-list bloat, quarantines unsafe HNSW segments, and can route to SQLite/BM25 fallback when vector capacity diverges ([backends/chroma.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/backends/chroma.py), [mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/mcp_server.py)). `repair.py` extracts drawers and closets from SQLite, rebuilds temporary collections, verifies counts, and swaps live collections; `dedup.py` removes near-duplicate drawers within a source group; `sync.py` prunes drawers whose source files are gitignored, missing, or out of scope, while preserving registry rows ([repair.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/repair.py), [dedup.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/dedup.py), [sync.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/sync.py)).

## Comparison with Our System

| Lens axis | MemPalace | Commonplace |
|---|---|---|
| Primary substrate | ChromaDB drawer collection plus closet collection, SQLite KG, local config/state files | Git-tracked typed markdown, generated indexes, source snapshots, review reports, validators |
| Raw traces/sources | Project files, transcript files, message JSONL, diary markdown, MCP writes | Sources, workshop artifacts, review traces, note drafts, validation reports |
| Retained artifacts | Drawers, closets, diaries, KG triples, tunnels, origin/entity files, WAL entries | Notes, source snapshots, instructions, type specs, indexes, reports, review decisions |
| Runtime/index/tool surfaces | CLI, MCP tools, Chroma vector search, BM25 fallback, closet boosts, wake-up layers, hooks | `rg`, authored indexes, `commonplace-*` commands, skills, validation and review workflows |
| Behavior-shaping artifacts | MCP protocol, hook settings, tool schemas, query sanitizer, KG invalidation protocol, wake-up context | AGENTS instructions, type specs, collection contracts, validators, commands, skills |
| Lineage model | Source file/session metadata, source drawer/closet references, WAL for writes, sync/repair state | Git history, frontmatter, backlinks, source snapshots, review archives, generated-index provenance |
| Trust posture | Capture first, retrieve locally, repair/dedup/sync operationally | Curate before promotion, validate structure, review semantics, keep authority explicit |

MemPalace is stronger than commonplace at live local capture. It has concrete capture paths for Claude Code/Codex transcript directories, stop/precompact hooks, MCP direct writes, daily summaries, and message-level sweeping. Commonplace has stronger artifact contracts: a retained object is typed, linked, validated, reviewed, and promoted through explicit library/workshop boundaries.

The deepest design difference is source-of-truth placement. In commonplace, the human-readable file is usually canonical and indexes are generated views. In MemPalace, Chroma/SQLite are canonical for runtime memory, while CLI/MCP outputs and docs are projections over database state. That buys fast retrieval and tool ergonomics, but makes code-level repair, WAL, and HNSW health checks part of the memory architecture rather than ancillary operations.

MemPalace also makes behavioral authority more automatic. The protocol tells agents to query before answering, diary after sessions, and invalidate changed facts. Hooks can force capture before compaction. Those are useful system-definition artifacts, but they also raise the trust bar for noisy drawers and extracted KG facts: a weak or stale fact can influence behavior earlier than it would in commonplace, where notes usually advise until promoted into instructions, schemas, or code.

**Read-back:** both — agents search drawers and KG through tools, while wake-up layers and hooks can inject memory context or force capture.

## Borrowable Ideas

**Hook-triggered trace capture before context loss.** Ready to borrow as a workshop pattern. Commonplace should not copy MemPalace's database substrate wholesale, but the stop/precompact trigger boundary is exactly where agents lose behavior-relevant evidence. A workshop-level trace capture command could preserve raw evidence before asking for curated note promotion.

**Separate verbatim drawers from compact pointer indexes.** Borrowable if commonplace grows a high-volume trace/source layer. MemPalace's drawers/closets split is a practical reminder that raw evidence and derived navigation aids should be different retained artifacts with different lineage and authority.

**Query sanitization for agent-supplied retrieval.** Ready as a small tool rule. MemPalace handles system-prompt contamination by extracting the likely user query before embedding ([query_sanitizer.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/query_sanitizer.py)). Commonplace's `rg`-first workflow avoids embeddings, but any future semantic search layer should defend against prompt-stuffed queries.

**Operational repair as part of the memory contract.** Worth borrowing conceptually. MemPalace treats corruption, duplicate rows, gitignored sources, stale indexes, and post-write cache reconnects as first-class commands. Commonplace already validates note structure; a future trace/index substrate should similarly ship repair and sync commands with clear dry-run/apply boundaries.

**Temporal KG as a sidecar, not a replacement.** Needs a clearer use case before borrowing. MemPalace's SQLite KG is useful for facts with validity windows, but it sits beside drawers and depends on agent/tool discipline for fact quality. Commonplace should adopt temporal triples only where questions genuinely require as-of reasoning, and should require source citations and review state before strong activation.

**AAAK as a compressed diary dialect.** Mostly a caution. The dialect is implemented as a parser/compressor and exposed through MCP docs, but `tool_diary_write` stores raw diary text and includes a TODO that compressed AAAK may hurt embedding quality ([dialect.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/dialect.py), [mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/d0163a7bec5ee6faa5e86169ed407a7bf41d5582/mempalace/mcp_server.py)). Commonplace should prefer ordinary typed prose unless a dialect has measured retrieval or context-budget benefits.

## Trace-derived learning placement

**Trace source.** MemPalace qualifies as trace-derived learning. It consumes project files, Claude Code/Codex conversation JSONL, ChatGPT/Slack/plain transcript exports, per-message user/assistant records, hook-fired active session transcripts, and agent-written diary entries. The most trace-specific inputs are `mempalace mine --mode convos`, `mempalace sweep`, Stop/PreCompact hooks, and MCP diary writes.

**Extraction.** There are several extraction paths. Project mining chunks files and adds wing/room/entity metadata. Conversation mining normalizes transcripts and chunks exchange pairs or paragraphs. Sweeping flattens Claude Code JSONL message blocks, including tool calls/results, into deterministic message drawers. Closet generation extracts topics, repeated entities, quotes, and drawer references. Init performs corpus-origin and entity detection, optionally with LLM refinement. KG facts are added through MCP tools rather than a fully automatic extractor in the reviewed runtime path. Diaries are agent-authored, often encouraged in AAAK format, not inferred automatically.

**Storage substrate.** Raw and semi-raw retained state primarily lives in ChromaDB drawer rows under the configured palace path. Derived closet rows live in a second Chroma collection. KG triples live in SQLite. Write-ahead logs live in `~/.mempalace/wal/write_log.jsonl` with content redaction. Hook state lives under `~/.mempalace/hook_state`; diary-ingest state lives under `~/.mempalace/state`; identity and config live as local files. Chroma's own SQLite and HNSW segment files are operational substrate for vector retrieval.

**Representational form.** Drawers and diaries are prose or mixed trace/prose artifacts. Closet lines, wing/room metadata, tunnels, and KG triples are symbolic. Embeddings and HNSW indexes are distributed-parametric retrieval surfaces, not learned agent policy. AAAK is symbolic/prose compression. Hook scripts, tool schemas, query sanitizer logic, validation/sanitization functions, and repair/sync commands are symbolic system definitions.

**Lineage.** Drawer metadata preserves `source_file`, chunk index, filed time, session id/message uuid/timestamp for sweeper writes, and source drawer/closet fields for KG tools when supplied. Closets point back to drawer ids and are purged/rebuilt by source file. Sync classifies drawers from source-file paths and gitignore rules. WAL records write operations with sensitive content redacted. The weak point is semantic lineage: a drawer may be trace-derived, but extracted KG facts, diary judgments, and AAAK summaries do not have a universal review state or enforced source-quotation contract.

**Behavioral authority.** Raw traces, drawers, source files, and WAL entries are knowledge artifacts when used as evidence. Search results and wake-up layers are context artifacts with ranking and activation influence. KG facts become stronger when the MCP protocol tells agents to query before answering and to invalidate changed facts. Hooks, tool schemas, sanitizer rules, HNSW fallback routing, and the MemPalace protocol are system-definition artifacts because they instruct, route, validate, schedule, or constrain future behavior.

**Scope.** Scope is local and per-palace, with wings dividing projects, people, agents, and topics. Agent diaries can be per-agent or project-wing scoped. The system does not train a cross-task policy or maintain a globally reviewed lesson library; reuse happens through local retrieval and protocol compliance.

**Timing.** Capture can be online during agent sessions through hooks and MCP writes, staged through `mine` and `sweep`, or offline through backfill of historical transcript directories. Retrieval is online at wake-up and tool-call time. Repair, sync, dedup, and migration are explicit maintenance cycles.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), MemPalace belongs in the live session-mining and local retrieval cluster, closest to ClawVault, SignetAI, Synapptic, and GBrain rather than benchmark trajectory-to-rule systems like ExpeL. It strengthens the survey claim that trace-derived systems need a raw/derived/authority split: MemPalace stores raw traces well, builds derived indexes and fact surfaces, and uses hooks/protocols for activation, but leaves trust and promotion mostly to agent discipline and operational repair.

## Curiosity Pass

MemPalace's best mechanism is not the palace metaphor; it is the practical separation between raw drawers, closet hints, KG facts, wake-up layers, and MCP protocols. That split lets raw retrieval outperform heavier extraction stories while still giving agents enough structure to navigate.

The README's "verbatim only" positioning understates the amount of symbolic machinery in the code. The product can run raw semantic retrieval with no API calls, but the implemented system also contains extraction, compression, routing, query repair, fact invalidation, and hook-level instructions. The more precise claim is: verbatim drawers remain canonical for the main retrieval path.

The KG is useful but not yet a reviewed knowledge base. It can represent temporal facts and invalidate old ones, yet fact quality depends on who calls `mempalace_kg_add` and what provenance they pass. Without source quotation and review status, KG facts should be treated as operational recall, not authoritative truth.

The write-ahead log is a strong governance clue. It does not make writes trustworthy, because content is redacted and rollback is not a first-class reviewed workflow, but it acknowledges that MCP write access is a poisoning surface and needs an audit trail.

The Chroma/HNSW repair code is unusually central for an "agent memory" project. In a database-first system, index health is memory health. That is the opposite of commonplace's file-first stance, where index failures usually degrade retrieval but do not threaten the canonical artifact.

## What to Watch

- Whether source adapters from RFC 002 become first-class and start writing KG triples with consistent `source_drawer_id` and `adapter_name` provenance.
- Whether KG facts gain review state, source quotations, confidence policy, and invalidation/regeneration rules before being used with strong protocol authority.
- Whether AAAK remains a diary convention or becomes a measured compression layer with retrieval benchmarks and expansion rules.
- Whether hooks move from capture reminders into fully silent durable writes, and how that changes user/agent awareness of memory mutation.
- Whether the public docs converge on the code's current KG path/schema and on the distinction between raw retrieval claims and extraction layers.

## Bottom Line

MemPalace is a serious local memory runtime, not just a vector-store wrapper. Its retained system splits into raw sources/traces, Chroma drawers and diaries, derived closet pointers, SQLite temporal triples, MCP/CLI/search/wake-up surfaces, and system-definition artifacts such as hooks, tool schemas, query sanitation, repair routines, and the memory protocol. The design is strongest where it keeps raw evidence canonical and retrieval cheap; it is weakest where extracted facts or compressed diary conventions can gain behavioral authority without the review contracts that commonplace relies on.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: MemPalace is live trace/session mining into local retrieval artifacts, not weight learning.
- [ClawVault](./clawvault.md) - compares-with: both use hooks, session capture, and local memory activation, but MemPalace centers Chroma drawers while ClawVault centers a markdown vault plus `.clawvault` state.
- [SignetAI](./signetai.md) - compares-with: both are cross-harness local memory daemons with transcript capture, MCP tools, and database-backed recall.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: drawers, traces, WAL entries, and reports advise as evidence before being promoted into stronger surfaces.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: hooks, MCP protocol text, tool schemas, and validators carry instruction, routing, validation, or scheduling force.
- [Behavioral authority](../../notes/definitions/behavioral-authority.md) - defined-in: MemPalace shows why raw memory, retrieval ranking, protocol instructions, and hook enforcement should not be collapsed into one "memory" label.
