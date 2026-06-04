---
description: "sage-wiki review: LLM-compiled personal wiki with SQLite FTS/vector/ontology state, MCP pull read-back, output trust, and session-trace scribing"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-03"
tags: [trace-derived]
---

# sage-wiki

sage-wiki, from `xoai/sage-wiki`, is a Go implementation of an LLM-compiled personal knowledge base inspired by Karpathy's "LLM-compiled wiki" idea. At the reviewed commit, it turns raw documents and captured text into Markdown summaries, concept articles, ontology entities, search indexes, chunk embeddings, query answers, and agent-facing MCP tools. It is not only an Obsidian-style file wiki: the visible wiki files are backed by `.sage/wiki.db` tables for FTS5, vectors, chunks, ontology, compile tiers, learned entries, and output-trust state.

**Repository:** https://github.com/xoai/sage-wiki

**Reviewed commit:** [c8761cbec4effa6c8db21cc392ab9f1bfaa8e498](https://github.com/xoai/sage-wiki/commit/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498)

**Last checked:** 2026-06-03

## Core Ideas

**The retained wiki is compiled from sources, not merely searched in place.** Greenfield initialization creates `raw/`, `wiki/summaries/`, `wiki/concepts/`, `wiki/connections/`, `wiki/outputs/`, `wiki/images/`, `wiki/archive/`, `.sage/`, `config.yaml`, `.manifest.json`, and a SQLite database; vault-overlay mode writes into an existing vault with an alternate output directory ([internal/wiki/init.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/wiki/init.go)). The compiler diffs source files against the manifest, summarizes sources, extracts concepts, deduplicates concepts, writes concept articles, updates the manifest, and indexes outputs into search and ontology stores ([internal/compiler/pipeline.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/compiler/pipeline.go), [internal/compiler/fullpipeline.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/compiler/fullpipeline.go), [internal/manifest/manifest.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/manifest/manifest.go)).

**SQLite is the operational memory substrate.** The storage layer creates FTS5 tables, vector tables, entity/relation tables, chunk metadata and chunk FTS/vector tables, compile-item tier state, learned entries, and pending-output trust tables under `.sage/wiki.db` ([internal/storage/db.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/storage/db.go)). Markdown remains the human-readable output surface, but many behavior-shaping decisions - ranking, graph traversal, tier promotion, output inclusion, and trust state - happen through database records.

**Context efficiency is tiered on write and budgeted on read.** For large vaults, sources can stop at Tier 0 full-text indexing, Tier 1 indexing plus embeddings, Tier 2 code parsing, or Tier 3 full LLM compilation; `.wikitier`, frontmatter, config defaults, query-hit counts, and stale-time signals control promotion and demotion ([internal/compiler/tiers.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/compiler/tiers.go), [internal/compiler/ondemand.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/compiler/ondemand.go), [docs/guides/large-vault-performance.md](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/docs/guides/large-vault-performance.md)). At read time, query context is assembled through chunk search, graph expansion, article truncation, and a configurable token budget rather than by loading the whole wiki ([internal/query/query.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/query/query.go)).

**Retrieval combines lexical, vector, LLM, and graph signals.** Basic hybrid search fuses FTS5 BM25 and vector results with reciprocal-rank fusion, tag boosts, and recency boosts ([internal/hybrid/search.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/hybrid/search.go)). Enhanced query search splits articles into chunks, optionally expands the query through an LLM into lexical/vector/HyDE variants, runs BM25 and vector search across chunks, deduplicates to documents, optionally reranks with an LLM, and then adds ontology-neighbor context ([internal/search/pipeline.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/search/pipeline.go), [internal/search/expand.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/search/expand.go), [internal/query/query.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/query/query.go)).

**MCP exposes the wiki as an agent-operated memory layer.** The server registers read tools (`wiki_search`, `wiki_read`, `wiki_status`, `wiki_ontology_query`, `wiki_list`, `wiki_provenance`), write tools (`wiki_add_source`, `wiki_write_summary`, `wiki_write_article`, `wiki_add_ontology`, `wiki_learn`, `wiki_capture`, `wiki_compile_topic`), and compound compile/lint tools ([internal/mcp/server.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/server.go), [internal/mcp/tools_write.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/tools_write.go), [internal/mcp/tools_compound.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/tools_compound.go)). The generated skill files are static host instructions telling agents when to search, read, capture, learn, compile a topic, and query ontology relationships ([internal/skill/packs/base.md.tmpl](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/skill/packs/base.md.tmpl), [internal/skill/writer.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/skill/writer.go), [docs/guides/agent-memory-layer.md](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/docs/guides/agent-memory-layer.md)).

**The trust layer treats generated answers as quarantined claims.** When trust mode is not legacy `true`, query answers go to `wiki/under_review/` and `pending_outputs` instead of being immediately indexed. Repeated similar questions can confirm or conflict with pending outputs, `verify` computes grounding scores against source passages, and promotion moves files to `wiki/outputs/` before indexing them into FTS, vector, ontology, and chunk stores ([internal/query/query.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/query/query.go), [internal/trust/hooks.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/trust/hooks.go), [internal/trust/verify.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/trust/verify.go), [internal/trust/promote.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/trust/promote.go), [docs/guides/output-trust.md](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/docs/guides/output-trust.md)).

## Artifact analysis

- **Storage substrate:** `sqlite` - The central behavior-shaping state lives in `.sage/wiki.db`: FTS5 entries, vector blobs, chunk tables, ontology entities/relations, compile tiers, learned entries, and output trust state. Files remain important as source and presentation artifacts, but search, graph traversal, tiering, and trust decisions are database-mediated.
- **Representational form:** `prose` `symbolic` `parametric` - Source and generated wiki content are prose Markdown; configuration, manifests, compile tiers, ontology records, trust records, MCP schemas, and indexes are symbolic; embeddings are distributed-parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` - Sources and learnings can be authored or imported through user/agent write paths, while session-scribe ontology records are trace-extracted from Claude Code session JSONL.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` - Wiki content and outputs serve as knowledge; generated skills instruct agents; trust gates enforce output promotion; manifests, tiers, indexes, ontology, and search state route, validate, rank, and learn behavior-shaping records.

**Raw sources and captures.** Storage substrate: project files under configured source paths, plus `raw/captures/*.md` for CLI/MCP capture ([cmd/sage-wiki/capture.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/cmd/sage-wiki/capture.go), [internal/mcp/tools_write.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/tools_write.go)). Representational form: prose or mixed document formats, normalized to extracted text for compilation. Lineage: authored/imported by users, copied in by `ingest`/`add-source`, or extracted from captured conversation/text. Behavioral authority: source knowledge artifacts until the compiler or scribe derives summaries, concepts, ontology, or learnings.

**Manifest and compile items.** Storage substrate: `.manifest.json` plus `compile_items` in SQLite ([internal/manifest/manifest.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/manifest/manifest.go), [internal/storage/db.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/storage/db.go)). Representational form: symbolic JSON and relational rows. Lineage: derived from source hashes, file types, compile pass completion, query hits, and tier signals. Behavioral authority: routing and scheduling system-definition artifacts because they decide what must be summarized, embedded, written, promoted, demoted, or skipped.

**Generated summaries and concept articles.** Storage substrate: Markdown files under `wiki/summaries/`, `wiki/concepts/`, or a vault overlay output directory. Representational form: prose Markdown with generated frontmatter and wikilinks. Lineage: LLM-derived from source text through summarize, extract, dedup, and article-writing passes; regenerated when sources change or tiers promote. Behavioral authority: knowledge artifacts when read by humans or agents; weak system-definition artifacts only when a host treats a generated article as instruction.

**Search, chunk, vector, and ontology indexes.** Storage substrate: SQLite FTS5 tables, vector tables, `chunks_meta`, `chunks_fts`, `vec_chunks`, `entities`, and `relations` ([internal/storage/db.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/storage/db.go), [internal/memory/entries.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/memory/entries.go), [internal/memory/chunks.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/memory/chunks.go)). Representational form: mixed symbolic rows, prose snippets, lexical indexes, graph edges, and embedding vectors. Lineage: derived from summaries, articles, outputs, chunking, embedding calls, ontology extraction, and manual/MCP additions. Behavioral authority: ranking, retrieval, graph-expansion, and routing system-definition artifacts; they decide what memory reaches later query contexts.

**Learning entries.** Storage substrate: the SQLite `learnings` table, written by CLI/MCP `learn` ([cmd/sage-wiki/learn.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/cmd/sage-wiki/learn.go), [internal/mcp/tools_write.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/tools_write.go), [internal/storage/db.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/storage/db.go)). Representational form: symbolic row fields plus prose content. Lineage: authored by a human or agent as explicit gotcha, correction, convention, error-fix, decision, or similar entry. Behavioral authority: intended self-learning knowledge artifacts; the inspected code stores them, but their future read-back path is weaker than the wiki article/search path unless a linter pass or operator consumes them.

**Session-scribe ontology records.** Storage substrate: Claude Code JSONL session files as raw traces, then ontology entities/relations in SQLite ([cmd/sage-wiki/main.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/cmd/sage-wiki/main.go), [internal/scribe/session.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/scribe/session.go)). Representational form: raw symbolic JSONL plus prose messages, distilled to symbolic entity/relation records with prose definitions. Lineage: trace-extracted by a deterministic compression pass and an LLM entity extraction pass, then filtered by kebab-case specificity and existing-entity comparison. Behavioral authority: graph/routing system-definition artifacts once inserted, because extracted entities and relations affect ontology queries and graph expansion.

**Query outputs and trust records.** Storage substrate: Markdown files under `wiki/under_review/` or `wiki/outputs/`, plus `pending_outputs`, `confirmation_sources`, and `pending_questions_vec` in SQLite ([internal/trust/hooks.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/trust/hooks.go), [internal/trust/store.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/trust/store.go), [internal/trust/promote.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/trust/promote.go)). Representational form: prose answers plus symbolic state, hashes, confirmation counts, grounding scores, source lists, chunk lists, and question embeddings. Lineage: LLM-synthesized from wiki context, then verified by consensus and grounding checks before promotion. Behavioral authority: pending outputs are quarantined knowledge artifacts; promoted outputs become searchable knowledge artifacts and ontology artifacts. The trust tables have system-definition authority over whether generated answers can re-enter future search context.

**MCP tools and generated skill files.** Storage substrate: Go tool definitions and generated host files such as `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `.windsurfrules`, `GEMINI.md`, or a generic skill file ([internal/mcp/server.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/server.go), [internal/skill/skill.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/skill/skill.go), [internal/skill/packs/base.md.tmpl](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/skill/packs/base.md.tmpl)). Representational form: symbolic API/tool schemas plus prose behavioral instructions. Lineage: authored package code/templates, parameterized by project config. Behavioral authority: system-definition interface and instruction artifacts; they expose memory operations and tell host agents when to use them, but the retained wiki content still enters via agent-initiated tool calls.

**Promotion path.** sage-wiki has several authority jumps: raw source -> summary -> concept article -> search/ontology index; source/index -> LLM answer -> pending output -> confirmed output -> searchable output; session trace -> extracted entity/relation -> ontology graph. The strongest design move is the trust system, because it prevents LLM answers from becoming future evidence until they pass consensus/grounding or manual promotion.

## Comparison with Our System

| Dimension | sage-wiki | Commonplace |
|---|---|---|
| Primary purpose | Compile personal/project documents into a searchable wiki for humans and agents | Maintain a typed methodology KB with validation, review, and source-grounded artifact lifecycle |
| Main substrate | Markdown wiki files plus SQLite FTS/vector/chunk/ontology/trust state | Git-tracked Markdown collections, type specs, generated indexes, sources, reports, and validation scripts |
| Context strategy | Tiered compilation, hybrid search, chunk budgets, graph expansion, compile-on-demand | Lexical search, curated/generated indexes, collection contracts, links, skills, validation, review bundles |
| Agent surface | MCP read/write/compile tools plus generated host skill files | Shell commands, skills, collection conventions, review workflows, and repo-native artifacts |
| Learning loop | Captures text, stores explicit learnings, extracts ontology from session JSONL, and promotes query outputs through trust gates | Deliberate note/source/review writing, semantic QA, deterministic validation, and workshop-to-library promotion |
| Governance | Config, manifest, tier state, linting, output trust, grounding, consensus, source-change demotion | Frontmatter schemas, type specs, collection contracts, validation, semantic review, git diffs, archive/replacement workflow |

sage-wiki is closer to Commonplace than a normal RAG stack because it treats compiled artifacts, provenance, ontology, and trust state as first-class. The main difference is which substrate carries authority. Commonplace keeps most durable authority in readable Git-tracked Markdown and validation rules. sage-wiki keeps much of its operational authority in SQLite: a reviewer can inspect generated articles, but ranking, vector state, compile tiers, and trust decisions require database-level inspection.

The strongest alignment is the distinction between raw evidence and promoted behavior-shaping artifacts. sage-wiki's output trust system is a concrete answer to a problem Commonplace also has: generated outputs should not silently become future evidence. The difference is that sage-wiki automates promotion with consensus and grounding thresholds, while Commonplace usually relies on explicit review and validation.

The biggest divergence is context activation. sage-wiki can make a large wiki searchable and can tell a host agent when to look, but the implemented memory read-back remains tool-mediated. The generated skill file is a static instruction surface; it does not itself push retained wiki content into the next action. This keeps the system understandable, but it leaves effectiveness dependent on the agent following the instruction to search.

**Read-back:** `pull` - Retained memory reaches the agent through explicit CLI/MCP/search/query/read/ontology calls. Generated skill files provide static guidance for when to pull; they do not automatically select and inject retained wiki content before an action.

### Borrowable Ideas

**Quarantine generated answers before indexing them.** Commonplace could borrow the pending/confirmed/stale/conflict lifecycle for any generated synthesis that might later appear as evidence. Ready as a workflow idea, but it needs a narrow artifact type and validation story before automation.

**Track source independence for repeated confirmations.** The trust system's use of chunk-set independence is more discriminating than simply asking the same question several times. Commonplace could use this in review gates where repeated claims only count if they depend on different sources. Needs a concrete review bundle use case.

**Expose compile-on-demand as a search hint.** `wiki_search` can tell the agent that uncompiled matching sources exist and suggest `wiki_compile_topic`. A Commonplace analogue would let search/index tools surface "you found a seed, run this focused expansion" instead of making agents infer the next command. Ready for command-output design.

**Separate source files from operational indexes without hiding the contract.** sage-wiki accepts that large-scale retrieval needs an operational database. Commonplace should not reject that category, but any future index layer should preserve plain-file source of truth and make invalidation/regeneration auditable.

**Borrow trust demotion on source change.** Confirmed sage-wiki outputs can become stale when cited source hashes change. Commonplace's source-grounded reviews and syntheses could use a similar invalidation signal when upstream snapshots or reviewed commits change. Ready as a design note or report, not a broad implementation yet.

**Do not borrow database-only authority for core methodology claims.** A methodology KB needs reviewable, diffable arguments. SQLite is useful for retrieval and staging, but durable claims and high-authority instructions should remain visible in typed files.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` - `sage-wiki scribe <session-file>` consumes Claude Code session JSONL after filtering non-message records.

**Learning scope:** `per-project` `cross-task` - Scribed entities and relations land in the project wiki's durable ontology and can affect later ontology queries and graph-expanded retrieval.

**Learning timing:** `offline` - The inspected trigger is an explicit `scribe <session-file>` command or explicit capture call, not an automatic online hook.

**Distilled form:** `symbolic` `prose` - The scribe distills compressed session text into ontology entity/relation records with prose definitions.

**Trace source.** sage-wiki qualifies as trace-derived because `sage-wiki scribe <session-file>` consumes Claude Code session JSONL. The compression path keeps user/assistant text, strips thinking tags, skips tool-use/tool-result/thinking records, and caps entity extraction to reduce noise ([internal/scribe/session.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/scribe/session.go)). `wiki_capture` can also consume conversation excerpts or text and write extracted items to `raw/captures/`, but that path depends on the caller supplying the excerpt rather than automatically mining a session log ([internal/mcp/tools_write.go](https://github.com/xoai/sage-wiki/blob/c8761cbec4effa6c8db21cc392ab9f1bfaa8e498/internal/mcp/tools_write.go)).

**Extraction.** Session scribing uses a two-stage extraction loop: deterministic compression first, then an LLM prompt that emits JSON entity candidates with IDs, names, types, definitions, and optional relations. The oracle is LLM judgment filtered by local gates: valid entity types from config, kebab-case specificity, duplicate lookup against the ontology store, and update-only behavior when a definition changes.

**Scope and timing.** The scope is per project wiki, and timing is manual: the inspected CLI exposes `scribe <session-file>`, not an automatic session-end hook. Captures are likewise explicit CLI/MCP calls. Once written, the distilled entities and relations become durable ontology state that can affect later ontology queries and graph-expanded retrieval.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), sage-wiki sits between session-to-knowledge capture and graph-building. It strengthens the survey's raw/durable split: raw session text is compressed and discarded from the immediate operation, while distilled ontology records persist as graph/routing state. It is weaker than systems with automatic trace harvesting because the trigger is manual.

## Curiosity Pass

**The product language says "wiki," but the architecture is an operational memory database plus wiki files.** The readable Markdown surface is valuable, yet retrieval and governance are mostly mediated by SQLite tables.

**The generated skill files solve intention, not activation.** They tell an agent when to use memory, which is an adoption affordance, but they do not prove the agent will actually search before acting.

**The trust system is stronger for generated answers than for generated articles.** Query outputs can be quarantined and promoted through consensus/grounding, while concept articles are part of the compile pipeline and receive quality scores/linting rather than the same pending-output lifecycle.

**Session scribing writes directly into ontology authority.** Extracted entities and relations can affect traversal and graph-expanded context, but they do not carry per-entity citations back to exact transcript turns in the inspected code.

**Compile-on-demand blurs retrieval and writing.** A failed or incomplete search can trigger source promotion and article generation. That is powerful, but it means a read path can mutate the wiki when an agent accepts the compile hint.

## What to Watch

- Whether scribe gains automatic hooks for Claude Code session end. That would move trace-derived learning from manual import to continuous adaptation.
- Whether session-scribed entities get transcript-span evidence or source files. That would make graph authority more auditable.
- Whether output trust extends to concept articles and captured knowledge items. That would unify governance across all LLM-derived artifacts.
- Whether generated skill instructions are paired with telemetry or faithfulness checks. That would show whether "search before acting" changes agent behavior.
- Whether SQLite state gains export/rebuild guarantees strong enough for long-lived Git workflows. That would reduce the risk of opaque operational authority.

## Bottom Line

sage-wiki is a serious compiled-memory system: it does source ingestion, LLM distillation, hybrid retrieval, ontology, MCP tools, output trust, trace scribing, and agent skill generation in one binary. Its most borrowable ideas for Commonplace are output quarantine, source-change demotion, and search hints that trigger focused compilation. Its main caution is that once ranking, trust, and graph state live in SQLite, reviewability depends on explicit export and rebuild discipline rather than on the repo diff alone.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: sage-wiki can extract ontology entities and relations from Claude Code session traces.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: sage-wiki stores and retrieves memory through strong tools, but retained memory is still pull-read by the agent.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: sage-wiki separates raw sources, generated articles, indexes, ontology, trust records, and skill files by substrate, form, lineage, and authority.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: output trust and provenance aim to preserve evidence while loading compiled context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: compile tiers, search indexes, ontology records, trust state, MCP schemas, and skill files configure future behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, generated summaries/articles, and confirmed outputs primarily inform future work as evidence or context.
