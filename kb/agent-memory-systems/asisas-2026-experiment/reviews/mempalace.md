---
description: "MemPalace review: local-first ChromaDB/SQLite memory palace with transcript mining, MCP tools, hooks, and explicit wake-up/search read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-04"
tags: [trace-derived]
---

# MemPalace

MemPalace, by milla-jovovich, is a local-first Python memory system for developer agents. At the reviewed commit it mines project files, documents, and AI conversation transcripts into verbatim ChromaDB drawers; builds searchable closet pointers, room/wing navigation, and SQLite temporal facts; exposes read/write operations through a CLI and MCP server; and ships Claude/Codex plugin hooks that save session material around stop and pre-compaction events.

**Repository:** https://github.com/milla-jovovich/mempalace

**Reviewed commit:** [db1fbe888b59514a66c43e745f095d762b9bf276](https://github.com/milla-jovovich/mempalace/commit/db1fbe888b59514a66c43e745f095d762b9bf276)

**Source directory:** `related-systems/mempalace`

## Core Ideas

**Verbatim drawers are the canonical memory unit.** Project mining and conversation mining chunk source text, preserve the chunk content as stored documents, and attach wing, room, source file, chunk index, ingest mode, and normalization metadata. The README explicitly frames this as not summarizing or paraphrasing, and the code implements that by upserting raw chunk text into the palace collection ([README.md](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/README.md), [mempalace/miner.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/miner.py), [mempalace/convo_miner.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/convo_miner.py)).

**The store is local and split across retrieval substrates.** The main palace lives in a ChromaDB-backed collection, closet pointers live in a second ChromaDB collection, temporal entity facts live in SQLite, and explicit room-to-room tunnels are JSON records under the local palace configuration path ([mempalace/backends/base.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/backends/base.py), [mempalace/backends/chroma.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/backends/chroma.py), [mempalace/knowledge_graph.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/knowledge_graph.py), [mempalace/palace_graph.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/palace_graph.py)).

**Context efficiency is layered retrieval, not whole-store loading.** `wake-up` renders identity plus a capped L1 "essential story"; L2 gets bounded wing/room drawers; L3 performs semantic search. The MCP search path over-fetches candidates, combines vector distance, BM25, closet boosts, and optional SQLite BM25 fallback, then returns a bounded result set with local snippets rather than loading the entire palace ([mempalace/layers.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/layers.py), [mempalace/searcher.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/searcher.py), [mempalace/mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/mcp_server.py)).

**Agent integration is operational, not only a library API.** The package exposes CLI commands, an MCP server, Claude and Codex plugin metadata, skill wrappers, and hooks. The hook implementation can silently write diary checkpoints and spawn transcript mining; the plugin hook manifests wire session-start, stop, and pre-compact hooks into Codex/Claude host lifecycles ([pyproject.toml](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/pyproject.toml), [mempalace/cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/cli.py), [mempalace/mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/mcp_server.py), [.codex-plugin/hooks.json](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/.codex-plugin/hooks.json), [.claude-plugin/plugin.json](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/.claude-plugin/plugin.json)).

**Trust comes from locality, provenance metadata, and repair tests more than review state.** The system records source paths, chunk indexes, timestamps, ingestion modes, temporal validity windows, and write-ahead log entries for MCP writes. It also has tests and repair paths for Chroma/HNSW failure modes, but I did not find a review gate that approves mined drawers or extracted closet pointers before they influence retrieval ([mempalace/mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/mcp_server.py), [mempalace/repair.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/repair.py), [tests/test_mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/tests/test_mcp_server.py)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` `vector` `graph` — The retained state spans local ChromaDB files for drawer and closet collections, SQLite for the temporal knowledge graph, JSON/config/plugin files, transcript source files, and graph-like tunnel and hallway records derived from palace metadata.
- **Representational form:** `prose` `symbolic` `parametric` — Drawers, diary entries, identity text, and hook messages are prose; wing/room metadata, drawer ids, closet pointers, KG triples, tunnel records, plugin manifests, and tool schemas are symbolic; Chroma embeddings and vector distances are parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — MCP drawer writes, KG facts, plugin files, configs, and identity text are authored; project files and document corpora are imported; Claude/Codex transcripts, per-message sweeps, and hook diary checkpoints are trace-extracted from agent sessions.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Retrieved drawers and KG facts advise future work as knowledge; MCP protocol text, skills, hooks, and plugin manifests instruct agent behavior; wings, rooms, closets, graph tunnels, and tool schemas route retrieval; sanitizers, temporal interval checks, HNSW health probes, and tests validate state; embeddings, BM25, closet boosts, graph dynamics, and top-k limits rank read-back; trace-derived transcript mining and diary checkpoints create later-consumed memory.

**Drawers and closets.** Drawers are the primary retained knowledge artifacts: verbatim chunks plus metadata in the palace collection. Closets are compact pointer lines built from source content and drawer ids; they are a ranking and navigation layer, not the canonical content source ([mempalace/palace.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/palace.py), [mempalace/searcher.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/searcher.py)).

**Temporal facts.** `KnowledgeGraph` stores entities and triples with `valid_from`, `valid_to`, confidence, and provenance columns. The MCP tools expose add, query, invalidate, timeline, and stats operations; validity windows shape what facts are read back for a given time ([mempalace/knowledge_graph.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/knowledge_graph.py), [mempalace/mcp_server.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/mcp_server.py)).

**Hooks and plugin manifests.** The Codex and Claude plugin surfaces are system-definition artifacts: they bind host lifecycle events to MemPalace hook commands and expose skills that tell the agent how to call the CLI. Their authority is instruction and write-triggering, while the actual transcript content they capture becomes knowledge in drawers or diary entries ([.codex-plugin/hooks.json](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/.codex-plugin/hooks.json), [.codex-plugin/skills/search/SKILL.md](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/.codex-plugin/skills/search/SKILL.md), [.claude-plugin/skills/mempalace/SKILL.md](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/.claude-plugin/skills/mempalace/SKILL.md), [mempalace/hooks_cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/hooks_cli.py)).

**Promotion path.** MemPalace promotes raw traces and files into indexed drawers, closet pointer lines, embeddings, rooms, wings, tunnels, and sometimes temporal KG facts. This is a retrieval promotion path rather than a governance promotion path: the system can strengthen access and salience, but mined text does not become an approved claim record with review status.

## Comparison with Our System

| Dimension | MemPalace | Commonplace |
|---|---|---|
| Primary purpose | Local memory palace for AI sessions, projects, and conversations | Typed methodology KB for agent-operated knowledge bases |
| Canonical artifact | ChromaDB drawers plus metadata, closets, KG triples, tunnels | Git-tracked Markdown notes, reviews, ADRs, instructions, sources, and indexes |
| Write path | CLI/MCP writes, project/document mining, transcript hooks, sweeper, KG APIs | Authored Markdown under collection contracts, validation, source discipline, review gates |
| Read-back | Explicit search, KG query, wake-up summaries, status/protocol, graph navigation | Explicit pull through `rg`, indexes, links, skills, snapshots, and generated reports |
| Governance | Locality, provenance metadata, sanitizers, tests, repair, temporal validity | Type schemas, collection routing, validation, semantic review, git history, replacement lifecycle |

MemPalace is much stronger than Commonplace at preserving raw agent-session material automatically. Its hooks and sweeper attack a real operational failure mode: terminal-agent transcripts expire or compact before the user has a chance to distill them. Commonplace is stronger when retained material needs durable semantic authority, because its artifacts are human-readable, typed, validated, and reviewable in git rather than primarily embedded in a local vector store.

The main design divergence is that MemPalace keeps raw memory cheap to capture and cheap to search, then lets agents decide what to do with it at read time. Commonplace pushes more work into the write/review path so later agents consume fewer ambiguous artifacts. The systems are complementary: MemPalace is a capture and recall layer; Commonplace is a library and governance layer.

### Borrowable Ideas

**Hook-driven transcript capture.** Ready as a Commonplace workshop tool if scoped carefully. A Commonplace hook could snapshot terminal-agent transcripts into `kb/work/` or `kb/sources/` before compaction without automatically promoting them into notes.

**Separate raw drawers from compact pointer indexes.** Ready as a retrieval-layer idea. Commonplace could keep source snapshots authoritative while generating cheap closet-like pointers for search and navigation, as long as generated pointers remain advisory.

**Per-message sweeper with deterministic ids.** Ready for trace ingestion. The cursor plus deterministic message id pattern would make transcript backfills idempotent and resume-safe.

**Temporal invalidation for facts.** Needs a concrete Commonplace use case. The KG `valid_from`/`valid_to` model is useful for personal-memory facts, but Commonplace methodology claims usually need source-linked supersession and review state rather than bare temporal windows.

**Do not borrow vector store authority as-is.** Commonplace should not let an embedding-backed hit become authoritative simply because it was retrieved. It can borrow recall mechanics while keeping typed Markdown and validation as the source of authority.

## Write side

**Write agency:** `manual` `automatic` — Humans or agents can add drawers, update drawers, add/invalidate KG triples, create tunnels, and mine sources manually through CLI/MCP calls; the system also automatically chunks, normalizes, embeds, builds closets, mines transcripts from hooks, writes hook diary checkpoints, sweeps per-message JSONL records, and maintains retrieval structures.

**Curation operations:** `dedup` `invalidate` `decay` `promote` — The standalone deduplicator detects near-duplicate drawers within source groups and deletes weaker duplicates; KG invalidation sets `valid_to` for stale facts; connection dynamics decay tunnel/hall strength over time; potentiation increases connection strength and stability on co-access. These are implemented operations over retained state, though not all are always-on background jobs ([mempalace/dedup.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/dedup.py), [mempalace/knowledge_graph.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/knowledge_graph.py), [mempalace/dynamics.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/dynamics.py)).

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — Conversation mining accepts Claude Code, ChatGPT, Slack, Codex, and other transcript formats; the sweeper parses Claude JSONL user/assistant records and preserves tool-use/tool-result blocks in flattened message content; stop and precompact hooks locate the active transcript and mine it into the palace ([mempalace/convo_miner.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/convo_miner.py), [mempalace/sweeper.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/sweeper.py), [mempalace/hooks_cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/hooks_cli.py)).

**Extraction.** The default conversation path normalizes transcripts, chunks them by exchange pairs or paragraphs, detects coarse rooms by keyword scoring, and stores verbatim drawers. The `general` extraction mode classifies chunks into decision, preference, milestone, problem, and emotional memory types. The sweeper stores one deterministic drawer per user/assistant message with session id, message uuid, timestamp, role, and source metadata. The hook silent-save path also extracts recent user-message themes into a compressed diary checkpoint.

**Learning scope:** `per-project` `cross-task` — Hook transcript wings derive from the JSONL working directory when possible, while one-time backfills can mine broad AI-tool session directories into shared wings.

**Learning timing:** `online` `staged` — Stop hooks trigger every configured message interval, precompact hooks fire just before context compaction, and backfills/sweeps run as explicit staged maintenance.

**Distilled form:** `prose` `symbolic` `parametric` — Raw session text and diary checkpoints are prose; metadata, wings, rooms, roles, timestamps, session ids, and memory-type labels are symbolic; Chroma embeddings make the trace-derived drawers retrievable through parametric similarity.

On the survey axes, MemPalace is a strong example of trace capture plus retrieval promotion rather than trace-to-rule learning. It turns session traces into future recall artifacts, but I did not find code that automatically distills traces into new validators, policies, executable tools, or model weights.

## Read-back

**Read-back:** `pull` — Agents or users explicitly call CLI search, MCP search, KG query, drawer lookup, graph traversal, diary read, status/protocol, or `mempalace wake-up`. The inspected session-start hook is operational pass-through/logging rather than retained-memory injection, and stop/precompact hooks save memory instead of retrieving stored memory into the next task context.

The pull read path is rich. `mempalace_search` sanitizes the query, queries ChromaDB, applies vector/BM25/closet ranking, and can fall back to SQLite BM25 when the HNSW vector segment is unsafe. KG reads are entity-first and can filter facts by `as_of` temporal validity. Graph traversal follows rooms, tunnels, and hallway structures. `wake-up` renders L0 identity plus L1 essential-story context from retained drawers, but it is still an explicit command whose output must be loaded by the operator or host workflow. These reads have advisory authority: they return context the agent may use, not hard enforcement.

The stop and precompact hooks should be read as write-side maintenance, not read-back. They mine transcripts and may emit a small system message saying memories were saved; they do not retrieve stored memory into the agent's next task context ([mempalace/hooks_cli.py](https://github.com/milla-jovovich/mempalace/blob/db1fbe888b59514a66c43e745f095d762b9bf276/mempalace/hooks_cli.py)).

## Curiosity Pass

**The strongest mechanism is capture, not synthesis.** MemPalace is compelling because it makes transcript preservation operationally hard to forget. Its code does not prove that agents will turn those traces into better decisions without explicit retrieval or wake-up injection.

**"Verbatim always" simplifies provenance and complicates context.** Keeping original chunks avoids summary drift, but it pushes burden onto retrieval ranking, chunk boundaries, and agent judgment at read time.

**Closets are useful but weakly governed.** They provide compact routing hints and source pointers, but they are generated access structures rather than reviewed claims.

**Temporal KG invalidation is more precise than drawer invalidation.** Facts can expire; drawers mostly persist or are deleted. Long-lived use will need clear rules for when stale transcript-derived drawers should remain evidence versus pollute search.

**The plugin surface is broader than the read-back automation.** Codex/Claude hooks are wired for save events, but the inspected session-start hook does not automatically load memories. That keeps startup cheap, but it means users still need an explicit wake-up/search habit.

## What to Watch

- Whether the session-start hook begins injecting wake-up memory automatically; that would strengthen the push side and make read-back quality tests more important.
- Whether generated closet pointers gain confidence, source-span, or review metadata; that would clarify when a pointer can be trusted beyond ranking.
- Whether trace-derived general extraction starts writing KG facts or durable rules automatically; that would move MemPalace from trace recall toward trace-derived system-definition learning.
- Whether dedup, decay, and potentiation become scheduled maintenance rather than callable utilities; that would change the write-side agency and curation picture.
- Whether benchmark results expand from retrieval recall to downstream agent behavior with and without MemPalace context; that would test whether retrieved memory is actually used.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - applies: MemPalace has substantial storage, but most read-back remains explicit pull unless wake-up context is injected.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: drawers, closets, KG facts, hooks, and embeddings have different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: drawers, diary entries, transcript chunks, and retrieved facts primarily advise as evidence/context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: hooks, plugin manifests, MCP tool schemas, protocol text, and validation/repair checks configure future behavior.
- [Context engineering](../../../notes/definitions/context-engineering.md) - frames: MemPalace is mainly a local capture and selective read-back system for bounded agent context.
