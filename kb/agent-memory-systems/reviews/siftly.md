---
description: "Siftly review: local X bookmark knowledge base with SQLite storage, AI enrichment, FTS5 search, Claude reranking, and Obsidian export"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# Siftly

Siftly, from viperrcrypto's `viperrcrypto/Siftly` repository, is a self-hosted Next.js application for turning Twitter/X bookmarks into a local searchable knowledge base. It imports bookmark JSON, stores tweet text and raw tweet payloads in SQLite, enriches bookmarks with deterministic entity extraction plus AI-generated visual and semantic metadata, uses FTS5 and LLM reranking for natural-language search, and can export the collection as markdown notes and index files.

**Repository:** https://github.com/viperrcrypto/Siftly

**Reviewed commit:** [b25daa45b858f4be096b5c368671c34db4407d8e](https://github.com/viperrcrypto/Siftly/commit/b25daa45b858f4be096b5c368671c34db4407d8e)

**Last checked:** 2026-06-02

## Core Ideas

**The durable memory is a local bookmark database.** The Prisma schema stores each bookmark's tweet id, text, author, imported date, raw JSON payload, semantic tags, extracted entities, enrichment metadata, media rows, category assignments, import jobs, and settings in SQLite (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/prisma/schema.prisma). Import creates `Bookmark` and `MediaItem` rows from uploaded JSON, skips duplicate tweet ids, and preserves the full source JSON as a string rather than only storing normalized fields (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/route.ts).

**The enrichment pipeline separates cheap extraction from model calls.** `backfillEntities` deterministically mines hashtags, URLs, mentions, known tool domains, tweet type, and media presence from stored raw tweet JSON with no AI call (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/rawjson-extractor.ts). The categorization route then runs a bounded concurrent pipeline: analyze untagged media, generate semantic tags and enrichment metadata, queue category assignment, and rebuild FTS after the run (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categorize/route.ts).

**AI outputs become searchable retained metadata, not just transient answers.** Vision analysis writes JSON `imageTags` onto media rows, semantic enrichment writes `semanticTags` and `enrichmentMeta` onto bookmarks, and categorization writes confidence-scored `BookmarkCategory` edges (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/vision-analyzer.ts, https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/categorizer.ts). Those retained fields later affect search, browsing, filtering, mindmap organization, and Obsidian export.

**Search is pull-time candidate selection plus LLM reranking.** `bookmark_fts` indexes bookmark text, semantic tags, entities, and image tags; `ftsSearch` returns up to 150 ranked bookmark ids and falls back gracefully if the virtual table is unavailable (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/fts.ts). The AI search route extracts keywords, detects category intent, merges FTS and intent candidates, caps the candidate set at 150, builds compact per-bookmark entries, and asks Codex, Claude CLI, or an SDK-backed model to return scored matches and short reasons (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/search/ai/route.ts).

**Context efficiency is handled by preprocessing and hard candidate caps.** The system does not push an unbounded bookmark corpus into a model. It precomputes entities, visual tags, semantic tags, and categories; indexes them in FTS5; slices tweet text, OCR, object lists, visual tags, hashtags, mentions, and categories into compact search entries; and limits reranking to a merged candidate set. This controls volume, though the LLM prompt still contains many bookmark summaries and has no tokenizer-aware budget beyond fixed truncation and candidate counts.

**Adoption is local-first but model-dependent.** The README emphasizes local SQLite storage and no cloud account requirement, while AI calls go to the configured provider or CLI session (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/README.md). That is a practical fit for personal knowledge capture: the source data and derived metadata stay inspectable in a local database, but enrichment quality and search reranking depend on external or CLI-mediated model behavior.

**Obsidian export turns bookmarks into a markdown vault surface.** `exportToObsidian` validates an absolute vault path, writes one markdown note per bookmark with tweet metadata, tags, categories, media links, and source URL, then writes category and author index files with wikilinks (https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/obsidian-exporter.ts). Exported notes can become ordinary knowledge artifacts for another agent or human, but export is a deliberate operation rather than automatic agent memory activation.

## Artifact analysis

- **Storage substrate:** `sqlite` — The local SQLite database configured by Prisma, with `Bookmark`, `MediaItem`, `BookmarkCategory`, `Category`, `Setting`, and `ImportJob` tables
- **Representational form:** `mixed` — Mixed symbolic/prose: tweet ids, authors, timestamps, source labels, category links, settings, and media URLs are symbolic fields, while tweet text and raw JSON carry prose and platform payloads

**Bookmark and media rows.** The storage substrate is the local SQLite database configured by Prisma, with `Bookmark`, `MediaItem`, `BookmarkCategory`, `Category`, `Setting`, and `ImportJob` tables. The representational form is mixed symbolic/prose: tweet ids, authors, timestamps, source labels, category links, settings, and media URLs are symbolic fields, while tweet text and raw JSON carry prose and platform payloads. Lineage comes from uploaded X bookmark JSON and import-time parsing; duplicate tweet ids are skipped rather than merged. Behavioral authority is knowledge artifact authority: rows provide evidence, reference material, and retrievable context for user-facing views and tools.

**Deterministic entity extraction.** The storage substrate is the bookmark `entities` JSON field. The representational form is symbolic JSON with hashtags, URLs, mentions, detected tool names, tweet type, and media flags. Lineage is derived from stored `rawJson` by authored TypeScript rules and the `KNOWN_TOOL_DOMAINS` table; changes to either raw JSON or those rules invalidate the extraction. Behavioral authority is search and categorization influence: entities are used as signals in enrichment prompts, category prompts, FTS rows, and AI-search entries.

**AI image and semantic enrichment.** The storage substrate is `MediaItem.imageTags`, `Bookmark.semanticTags`, and `Bookmark.enrichmentMeta`. The representational form is prose-in-symbolic-JSON: OCR text, people, objects, scene, action, mood, visual tags, semantic tags, sentiment, people, and companies. Lineage is model-derived from tweet text, image URLs or fetched image bytes, deterministic entities, and prompt templates. Behavioral authority is ranking and selection influence for future search and categorization. Effective quality is not verifiable from code; the code validates JSON shape and retries some calls, but it does not run a grounded accuracy check against the original media or tweet.

**Categories and category assignments.** The storage substrate is the `Category` and `BookmarkCategory` tables. The representational form is mixed prose/symbolic: category names, slugs, colors, descriptions, confidence scores, and AI-generated flags. Lineage is split between authored default category descriptions, user-created categories, and model-assigned bookmark-category edges. Behavioral authority is routing and filtering authority in the application: categories drive browse filters, mindmap grouping, search intent expansion, export tags, and prompt labels for later categorization.

**FTS5 index and search cache.** The storage substrate is the runtime SQLite virtual table `bookmark_fts` plus a short-lived in-memory `searchCache` in the AI search route. The representational form is symbolic/indexed text over tweet text, semantic tags, entities, and image tags. Lineage is derived by `rebuildFts` from all current bookmark and media rows after enrichment; cache entries derive from query/category pairs and expire after five minutes. Behavioral authority is ranking and candidate-selection authority: the index determines which bookmarks enter the LLM reranking prompt, while cache results can bypass fresh reranking for repeated queries.

**AI search prompt and CLI/API integration.** The storage substrate is repository code and runtime settings/API credentials. The representational form is mixed symbolic/prose: TypeScript handlers, provider selection, JSON response contracts, and prompt text. Lineage is authored code plus user settings and CLI session state. Behavioral authority is system-definition artifact authority for search behavior because it instructs the reranker how to interpret bookmark fields, scoring, result caps, and response format.

**Obsidian export notes and indexes.** The storage substrate is a user-selected filesystem vault outside Siftly's database. The representational form is markdown prose with YAML frontmatter, tags, embedded media links, source links, and wikilink indexes. Lineage is derived from current SQLite rows at export time; later database changes do not automatically update exported files unless export runs again. Behavioral authority is knowledge artifact authority for downstream humans or agents that read the vault. It can gain stronger authority only if another system treats the exported notes or indexes as instructions, routing rules, or validation inputs.

The promotion path is bookmark JSON -> local rows -> deterministic entities and model-derived metadata -> FTS/search/category views -> optional markdown export. Siftly does not promote observations into executable validators, agent instructions, or model weights.

## Comparison with Our System

| Dimension | Siftly | Commonplace |
|---|---|---|
| Primary purpose | Personal X bookmark capture, enrichment, search, visualization, and export | Agent-operated methodology KB with typed markdown artifacts, validation, reviews, and source workflows |
| Canonical substrate | Local SQLite database plus optional exported markdown | Git-tracked `kb/` collections, type specs, source snapshots, generated indexes, and review reports |
| Retained artifacts | Raw tweet JSON, tweet text, media URLs, entities, AI tags, categories, FTS rows | Notes, instructions, type specs, reviews, indexes, links, validation outputs |
| Retrieval | FTS5, category-intent heuristics, LLM reranking, browse filters, mindmap, CLI search | `rg`, curated/generated indexes, authored links, collection routing, skills, review bundles |
| Context efficiency | Precomputed enrichment, compact search entries, candidate caps, fixed truncation | Descriptions, collection contracts, type schemas, generated indexes, scoped skills, review gates |
| Governance | Local storage, import deduplication, path validation for export, JSON parse checks | Type validation, semantic review, link contracts, source citation rules, git lifecycle |

Siftly and Commonplace both treat accumulation as insufficient. Siftly makes bookmarks useful by extracting entities, enriching media, assigning categories, and indexing derived fields before search. Commonplace makes methodology artifacts useful by adding type contracts, frontmatter, links, validation, source snapshots, and review workflows before agents depend on them.

The main difference is authority. Siftly's retained artifacts mostly shape user-facing retrieval and organization. They can help a human or external agent find a remembered tweet, but they do not themselves instruct the next agent action. Commonplace's retained artifacts are often system-definition artifacts: collection contracts, type specs, instructions, validators, and gates are intended to constrain future agent behavior directly.

Siftly is stronger as an ergonomic capture and enrichment front end. It has import tools, media understanding, semantic tags, category confidence, mindmap exploration, and export. Commonplace is stronger as a governed knowledge substrate: it keeps artifact form, lineage, validation, review state, and behavior-shaping authority explicit.

**Read-back:** `pull` — Users or external agents deliberately search, browse, inspect, run CLI commands, or read exported markdown; the code does not implement relevance-gated pre-action injection into a receiving agent's context

### Borrowable Ideas

**Precompute cheap signals before model calls.** Commonplace could extract deterministic entities, links, dates, artifact types, and source hints before invoking semantic review or search. Ready now for source snapshots and review candidate triage.

**Use compact rich entries for reranking.** Siftly's AI search prompt does not send full records; it sends bounded entries with text, visual context, tags, entities, and categories. Commonplace could use the same pattern for optional semantic search over reviews and sources, provided citations remain pinned to source artifacts.

**Make derived metadata visible enough to export.** Siftly's Obsidian export preserves categories, tags, author, tweet id, media, and source link. Commonplace should keep generated summaries and indexes similarly inspectable when they become context surfaces, rather than hiding them in opaque caches.

**Keep personal capture separate from governed authority.** Siftly is useful precisely because import and enrichment are low-friction. Commonplace can borrow the capture ergonomics, but promotion into instructions, validators, or durable claims still needs review and validation.

**Candidate caps are a useful but incomplete budget.** Siftly's fixed top-150 candidate cap and field truncation are practical. Commonplace can borrow the simplicity for early search layers, while adding tokenizer-aware budgets where generated context is fed directly to agents.

## Curiosity Pass

**This is a knowledge base more than an agent memory system.** Siftly can support agent memory if an agent queries it or reads exported notes, but the inspected repository is a bookmark manager and search app. Its behavior-shaping path is retrieval and organization, not autonomous future-agent activation.

**The deepest retained artifact is AI-derived metadata, not the mindmap.** The graph visualization is useful, but the more consequential memory layer is the stored semantic tags, image tags, entities, categories, and FTS rows that determine what can be found later.

**The README's "semantic search" is implemented as LLM reranking over lexical and category candidates.** There is no vector database at this commit. That keeps the system local and simple, but recall depends on FTS keywords, intent heuristics, and fallback sampling before the LLM sees candidates.

**Export is one-way and deliberate.** Obsidian export can create a more agent-readable markdown surface, but the code does not keep the vault synchronized with database updates or read vault edits back into Siftly.

**Quality controls stop at parsing and shape checks.** The enrichment and search routes parse JSON, retry some failures, and constrain output format. They do not test whether OCR, tags, categories, or reranked matches are faithful to the source tweet and media.

## What to Watch

- Whether Siftly adds embedding or hybrid retrieval beyond FTS5 and LLM reranking, because that would change the retained ranking substrate.
- Whether exported markdown becomes bidirectional sync with provenance and conflict handling, because that would move Siftly closer to a durable agent-readable vault.
- Whether category and tag assignments gain user correction loops or evaluation records, because that would create auditable learning from operator feedback.
- Whether AI search adds tokenizer-aware prompt budgeting or provenance snippets, because current candidate caps manage volume but not full context cost or citation quality.
- Whether the app exposes MCP or other agent-facing APIs; that would change read-back from user-pull through the web/CLI toward tool-pull by agents.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Siftly stores and enriches bookmark knowledge, but memory enters context only through explicit search, browse, CLI, or export reads.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw bookmark rows, entity JSON, AI metadata, categories, FTS rows, prompts, and exported notes differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: tweets, raw JSON, media analysis, search results, and exported notes mostly provide evidence, reference, and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: search prompts, FTS candidate selection, category descriptions, import rules, and export validators route or constrain behavior.
- [Storage substrate](../../notes/definitions/storage-substrate.md) - relates: Siftly separates local SQLite state from optional exported markdown and external model/provider state.
