---
description: "Zikkaron review: Claude Code MCP memory server with SQLite, hooks, trace capture, hybrid retrieval, lifecycle compression, and generated instructions"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Zikkaron

Zikkaron, from amanhij, is a Python MCP memory server for Claude Code. It stores project and session memories in a local SQLite database, exposes memory operations as MCP tools, installs Claude Code hooks for automatic capture and context injection, and layers retrieval, consolidation, compression, staleness, rules, project seeding, and neuroscience-branded mechanisms over that substrate. The implementation is real enough to review as an agent memory system, but many of its named mechanisms are best read as local heuristics over database rows rather than as independent cognitive modules.

**Repository:** https://github.com/amanhij/Zikkaron

**Reviewed commit:** [dda34a5d903d04ecb5517af214d437873c833302](https://github.com/amanhij/Zikkaron/commit/dda34a5d903d04ecb5517af214d437873c833302)

**Last checked:** 2026-05-16

## Core Ideas

**The memory boundary is one local SQLite database.** The default `DB_PATH` is `~/.zikkaron/memory.db`, and the storage engine initializes ordinary tables, FTS5 virtual tables, `sqlite-vec` vector tables, profile/belief tables, rules, archives, checkpoints, and action logs ([zikkaron/config.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/config.py), [zikkaron/storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py)). The storage substrate is therefore not Markdown or a vector database service; it is a single local SQLite file with relational, lexical, vector, and lifecycle tables.

**Claude Code integration has both tool and hook surfaces.** The FastMCP server exposes explicit tools such as `remember`, `recall`, `get_project_context`, `checkpoint`, `restore`, `anchor`, `install_hooks`, `sync_instructions`, and `seed_project` ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py)). `install_hooks` writes Claude Code hook configuration and copies scripts for `PreCompact`, `SessionStart`, `PostToolUse`, and `UserPromptSubmit` ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/hooks/post-tool-capture.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/post-tool-capture.py), [zikkaron/hooks/session-start-context.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/session-start-context.py), [zikkaron/hooks/prompt-recall.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py)). The MCP tools are active agent-facing APIs; the hooks are higher-authority system-definition artifacts because they inject context and capture actions without the model choosing a tool call.

**Writes pass through filtering, curation, typing, and lifecycle metadata.** `remember` checks a predictive-coding write gate before storage, computes embeddings and thermodynamic scores, optionally merges or links similar memories through the curator, stamps CRDT provenance, classifies the row as episodic or semantic through the CLS module, records file hashes, captures content into the sensory buffer, assigns graph/HDC/engram metadata, and may create micro-checkpoints or protected decisions ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/predictive_coding.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/predictive_coding.py), [zikkaron/curation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/curation.py), [zikkaron/cls_store.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/cls_store.py)). A stored row is a mixed artifact: prose content plus symbolic tags, timestamps, scores, links, hashes, and optional distributed-parametric embeddings.

**Retrieval is a fused ranking pipeline, not simple vector search.** `recall` combines FTS5, vector search, personalized PageRank over an entity graph, spreading activation, fractal scores, Hopfield scores, HDC vectors, successor-representation navigation, temporal boosts, cross-encoder reranking, NLI scoring, multi-passage aggregation, profile/belief search, MMR diversity, adversarial confidence checks, rules, engram temporal links, and metacognitive context management where available ([zikkaron/retrieval.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/retrieval.py), [zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/rules_engine.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/rules_engine.py)). The memories themselves are knowledge artifacts when read as evidence or context; the retrieval code, weights, rules, embeddings, graph edges, and hook injectors are system-definition artifacts because they decide what reaches Claude.

**Lifecycle mechanisms are implemented as database transformations.** Consolidation applies decay, extracts entities from episodes, builds relationships, merges duplicates, runs causal discovery, runs domain consolidation, performs "memify" curation, promotes recurring episodic clusters into semantic memories, compresses old memories, and summarizes action logs ([zikkaron/consolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py), [zikkaron/cls_store.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/cls_store.py), [zikkaron/compression.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/compression.py)). Compression archives prior content and replaces the active memory with gist or tag-level content; reconsolidation can update a recalled memory or archive it and create a replacement ([zikkaron/compression.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/compression.py), [zikkaron/reconsolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/reconsolidation.py)).

**Project seeding imports codebase structure into the memory substrate.** `seed_project` scans a project directory for structure, manifests, documentation, CI, entry points, and component summaries, deletes prior `_seed` memories for that directory, and inserts fresh seeded memories with embeddings and heat scores ([zikkaron/seed.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/seed.py), [zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py)). These are knowledge artifacts derived from project files. Their lineage is directory-scoped and tag-based rather than source-file-citation based, but reseeding provides a regeneration path.

## Comparison with Our System

| Dimension | Zikkaron | Commonplace |
|---|---|---|
| Primary purpose | Personal/project memory for Claude Code sessions | Agent-operated methodology KB for durable knowledge, procedures, and reviews |
| Storage substrate | Local SQLite file with FTS5, sqlite-vec, JSON-ish fields, archives, checkpoints, action logs | Git-tracked Markdown, type specs, schemas, instructions, ADRs, generated indexes |
| Representational form | Mixed prose rows, symbolic tags/rules/relationships, embeddings, HDC vectors, graph/ranking scores | Mostly prose and frontmatter, with symbolic schemas, scripts, link vocabulary, and validation outputs |
| Lineage | Row timestamps, source episodes, file hashes, archives, vector clocks, seed replacement, checkpoint epochs | Source snapshots, reviewed commits, authored links, status lifecycle, replacement archives, validation and review outputs |
| Activation | MCP calls, startup hooks, prompt hooks, compaction hooks, fused retrieval, generated CLAUDE.md instructions | `rg`, curated indexes, authored links, skills, type contracts, validation, review gates |
| Behavioral authority | Context injection, ranking, write filtering, compression, rules, generated instructions | Advice, instruction, validation, routing, review, and methodology governance |

Zikkaron and commonplace share a pragmatic premise: memory matters only when it reaches the next agent before the next decision. Zikkaron solves this by moving into Claude Code's native runtime through MCP tools and hooks. Commonplace solves it by making the repository itself navigable and enforceable through typed artifacts, instructions, validation, and review procedures.

The major tradeoff is inspectability versus automation. Zikkaron has stronger automatic capture and retrieval: it can log tool calls, summarize action windows, inject hot memories on session start, and search through multiple ranking channels without a maintainer authoring links. Commonplace has stronger artifact contracts: a note, instruction, source, ADR, or review has a visible type, status, link vocabulary, lineage convention, and validation path.

The authority split is especially important. In Zikkaron, individual `memories` rows are usually knowledge artifacts: they advise, explain, or provide context. But `sync_instructions` output, hook configuration, retrieval weights, rules, write gates, compression policy, staleness policy, and prompt-injection hook scripts are system-definition artifacts because they instruct, filter, rank, mutate, or inject retained state ([zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py), [zikkaron/hooks/session-start-context.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/session-start-context.py), [zikkaron/hooks/prompt-recall.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/prompt-recall.py), [zikkaron/rules_engine.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/rules_engine.py)).

Zikkaron's lineage is useful but uneven. Raw rows carry timestamps, directory context, tags, file hashes, `source_episode_id`, archive links, and CRDT metadata where present ([zikkaron/storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py), [zikkaron/server.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/server.py)). Generated semantic memories from CLS do link back to episodic memories with derived links, but many derived artifacts depend on heuristic clustering or summarization rather than mandatory evidence citations ([zikkaron/cls_store.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/cls_store.py)). Commonplace would not accept that as durable library lineage without source fields and review state.

**Read-back:** both — agents can call MCP recall tools, and hooks inject context on session start and prompt submission.

## Trace-derived learning placement

**Trace source.** Zikkaron qualifies as trace-derived learning. The strongest implemented traces are Claude Code tool-call events captured by `PostToolUse`, session-start context, prompt text used for auto-recall, explicit `remember` calls, sensory-buffer episodes, checkpoints, and action logs ([zikkaron/hooks/post-tool-capture.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/hooks/post-tool-capture.py), [zikkaron/sensory_buffer.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/sensory_buffer.py), [zikkaron/restoration.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/restoration.py), [zikkaron/storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py)).

**Extraction.** Extraction is partly direct and partly delayed. The hot path writes concise action records to `action_log`; the consolidation path groups unprocessed actions by directory and 30-minute windows, then stores "Session activity" memories when a group has enough actions ([zikkaron/consolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py)). Separately, the sensory buffer stores episode text and consolidation extracts entities and relationships. The CLS store can promote recurring episodic clusters into semantic memories after consistency checks ([zikkaron/consolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/consolidation.py), [zikkaron/cls_store.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/cls_store.py)).

**Storage substrate.** Raw traces live in SQLite `action_log`, `episodes`, `checkpoints`, and memory rows. Distilled state lives in `memories`, `entities`, `relationships`, `memory_archives`, `memory_rules`, semantic memory rows, vector tables, FTS tables, and generated Claude Code files or hook settings when installed.

**Representational form.** Raw action logs are symbolic rows with short prose summaries. Memories and semantic schemas are prose plus symbolic tags and fields. Relationships, rules, checkpoints, heat values, staleness flags, compression levels, and vector clocks are symbolic. Embeddings, implicit embeddings, HDC vectors, cross-encoder scores, and ranking outputs are distributed-parametric or numeric retrieval state.

**Lineage.** Action-derived memories retain directory and time-window context but not a full replayable transcript of each tool call beyond the summarized action rows. Episode-derived graph state has `source_episode_id` lineage at the memory-row level. Compression and reconsolidation preserve older content in `memory_archives`; project seeding deletes and regenerates `_seed` rows for a directory ([zikkaron/storage.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/storage.py), [zikkaron/compression.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/compression.py), [zikkaron/reconsolidation.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/reconsolidation.py), [zikkaron/seed.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/seed.py)). The weak point is review lineage: promoted semantic memories do not require human approval, citations, or confidence-calibrated derivation records.

**Behavioral authority.** Raw trace rows have evidence authority. Ordinary memory rows advise or provide context. Semantic memories and seeded project memories become stronger knowledge artifacts because they are retrieved and injected across sessions. Hook scripts, generated CLAUDE.md instructions, write gates, rules, retrieval fusion, compression, staleness, and session-start injection have system-definition authority because they change what Claude sees, stores, filters, and preserves.

**Scope.** Most learning is per-user and per-project, keyed by directory context. Some rules and global memories can affect broader behavior, and `sync_instructions` writes global Claude instructions, but the implementation does not provide a review workflow for promoting project-local lessons into a durable cross-project library.

**Timing.** Capture is online through MCP calls and hooks. Consolidation, action-log processing, compression, CLS promotion, and graph construction run during idle or forced consolidation cycles. Compaction recovery is event-driven through `PreCompact` and `SessionStart` hooks.

**Survey placement.** Zikkaron sits on the trace-to-retrieval and trace-to-instruction edges of the trace-derived survey. It strengthens the survey split between raw trace storage and behavior-changing derived artifacts: a captured tool call is only evidence, while a summarized memory, semantic pattern, hook-injected context block, generated instruction section, or rule changes future behavior.

## Borrowable Ideas

**Treat hooks as first-class activation surfaces.** Useful for commonplace workshops, but not ready for the durable library without governance. Zikkaron shows that a memory system becomes more effective when it can inject context on session start and before prompts rather than waiting for the agent to remember a search command.

**Keep action traces cheap, then distill later.** Ready to borrow for active workspaces. The PostToolUse hook writes a lightweight row without loading ML models, while consolidation later groups action windows into memories. Commonplace could borrow this hot-path/cold-path split for workshop logs.

**Separate critical anchors from ordinary memories.** Ready conceptually. `anchor` creates protected, high-heat memories that restoration always includes ([zikkaron/restoration.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/restoration.py)). In commonplace, the analogous surface would be explicit workshop state or a short-lived instruction artifact, not an opaque database flag.

**Use reseeding as regeneration, not accumulation.** Ready now as a design rule. Zikkaron deletes old `_seed` memories for a directory before inserting new project-seed memories, which avoids stale project-bootstrap clutter ([zikkaron/seed.py](https://github.com/amanhij/Zikkaron/blob/dda34a5d903d04ecb5517af214d437873c833302/zikkaron/seed.py)).

**Do not borrow neuroscience names as authority.** The implementation has useful mechanisms, but the names can overstate what is happening. Commonplace should name the operational contract plainly: write gate, action-log summarizer, semantic pattern promotion, context injection, compression, and staleness.

## Takeaways

**Zikkaron is an agent-runtime memory layer, not a knowledge-base methodology library.** Its strength is that it sits directly in Claude Code's execution path through MCP tools and hooks.

**The storage substrate is centralized and opaque to git review.** SQLite makes automatic capture and ranking practical, but it weakens human inspectability, diffability, and review compared with typed Markdown artifacts.

**Representational form is deliberately mixed.** Prose memories, symbolic metadata, relational graph edges, rules, embeddings, HDC vectors, and reranker scores all shape behavior. Calling the SQLite row "the memory" hides the operative parts.

**Lineage exists but is not enough for durable claims.** Timestamps, file hashes, source episodes, archives, and vector clocks help, but generated semantic memories need stronger derivation metadata before they can become high-trust instructions.

**Trace-derived learning is real, but mostly heuristic.** Tool traces and episodes become durable memories and sometimes semantic patterns. There is no trained model update or human-reviewed promotion loop in the inspected implementation.

## Curiosity Pass

The most interesting design move is not any single retrieval algorithm. It is the combination of automatic capture, startup injection, prompt-time auto-recall, and compaction recovery. Zikkaron tries to make memory active before the model asks for it.

The largest review risk is over-crediting branded mechanisms. "Thermodynamics", "Hopfield", "astrocyte", "Hippocampal Replay", and "CLS" correspond to implemented code paths, but their practical effect is local scoring, grouping, ranking, compression, or hook behavior over SQLite rows.

The system-definition artifacts are scattered. Some live as Python code, some as generated `CLAUDE.md` text, some as `.claude/settings.json` hook config, and some as database rules. That makes authority powerful but hard to audit as one policy surface.

## Open Questions

- How often do automatically summarized action-window memories help compared with injecting the raw recent action log?
- Should semantic memories require explicit evidence links to source episodic memory IDs, scores, and timestamps in the active row?
- Can hook-injected context become stale or misleading without a visible review surface?
- How should protected anchors expire or be challenged when project assumptions change?
- Do the many retrieval signals improve robust recall, or do they mostly increase ranking complexity and tuning burden?
- What is the failure mode when generated global Claude instructions conflict with project-local instructions?

## What to Watch

- Whether Zikkaron adds human review, confidence, or source links for promoted semantic memories.
- Whether action-log summaries become richer than tool counts and short input snippets.
- Whether generated instructions and hooks gain versioned, inspectable policy state.
- Whether project seeding records stronger per-file lineage and invalidation.
- Whether retrieval evaluation separates storage quality, retriever quality, reader-model quality, and hook-injection quality.

## Bottom Line

Zikkaron is best read as a local Claude Code memory runtime: SQLite stores prose, symbolic metadata, vectors, action traces, checkpoints, archives, and generated patterns; MCP tools and hooks turn that state into future context. Its strongest lesson for commonplace is activation timing: memory should surface before an agent repeats work. Its weakest fit for commonplace is governance: high-authority ranking, injection, compression, and generated-instruction behavior lives outside a reviewable typed artifact system.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Zikkaron turns Claude Code tool/session traces into durable memories, semantic patterns, and injected context through hooks and consolidation.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Zikkaron requires separating SQLite rows, FTS/vector indexes, hooks, generated instructions, rules, and compression archives by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: ordinary memory rows and seeded project summaries advise future agents as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: hook configuration, retrieval ranking, write gates, rules, generated instructions, and compression policies carry instruction, ranking, filtering, or injection authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - illustrates: Zikkaron's main value comes from MCP calls, session hooks, prompt hooks, and compaction hooks that activate stored state.
