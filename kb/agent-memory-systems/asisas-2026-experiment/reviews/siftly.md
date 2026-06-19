---
description: "Siftly review: local SQLite Twitter/X bookmark knowledge base with AI enrichment, category routing, FTS5 search, LLM reranking, mindmap, exports, and JSON CLI"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# Siftly

Siftly, from `viperrcrypto/Siftly`, is a self-hosted Next.js application for turning Twitter/X bookmarks and likes into a local searchable bookmark knowledge base. At the reviewed commit it stores imported tweet JSON, media rows, categories, AI-derived image/semantic metadata, settings, and import jobs in SQLite through Prisma; then serves browse, category, mindmap, export, web search, AI search, and a JSON CLI over that store.

**Repository:** https://github.com/viperrcrypto/Siftly

**Reviewed commit:** [b25daa45b858f4be096b5c368671c34db4407d8e](https://github.com/viperrcrypto/Siftly/commit/b25daa45b858f4be096b5c368671c34db4407d8e)

**Source directory:** `related-systems/viperrcrypto--Siftly`

## Core Ideas

**A personal bookmark corpus becomes the memory substrate.** Siftly's central retained objects are not agent episodes or notes; they are imported X/Twitter bookmarks and likes, with raw tweet JSON preserved beside normalized text, author, media, source, category, entity, semantic-tag, enrichment, and timestamp fields ([prisma/schema.prisma](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/prisma/schema.prisma), [app/api/import/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/route.ts)). The app treats social bookmarks as reusable knowledge items for later browsing, search, graph exploration, and export.

**The write pipeline enriches imported records in place.** Import creates bookmark/media rows and skips duplicate tweet ids; the categorization API then runs entity extraction, media vision analysis, semantic tag generation, category assignment, and FTS rebuild as a stateful background job ([app/api/import/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/route.ts), [app/api/categorize/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categorize/route.ts), [lib/rawjson-extractor.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/rawjson-extractor.ts), [lib/vision-analyzer.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/vision-analyzer.ts), [lib/categorizer.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/categorizer.ts)). Failed or trivial enrichments are marked so the pipeline can continue rather than loop forever.

**Categories are both user-facing labels and prompt policy.** Default category descriptions live in code and are seeded into SQLite; custom or suggested categories also carry descriptions. Categorization prompts pass those descriptions directly to the LLM, so category prose becomes an instruction surface for future label assignment, not just UI copy ([lib/categorizer.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/categorizer.ts), [lib/category-suggester.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/category-suggester.ts), [app/api/categories/suggest/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categories/suggest/route.ts)).

**Context efficiency is two-stage retrieval, not full-corpus loading.** AI search first narrows candidates with extracted keywords, SQLite FTS5, category-intent regexes, filters, deduplication, and a recent fallback capped around 150 candidates. It then serializes a compact per-bookmark index entry with text, media summaries, semantic tags, entities, and categories for LLM reranking, instead of sending every stored bookmark to the model ([lib/fts.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/fts.ts), [lib/search-utils.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/search-utils.ts), [app/api/search/ai/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/search/ai/route.ts)). The tradeoff is that hard misses in lexical/category candidate selection can prevent semantic reranking from seeing a relevant bookmark.

**Adoption is local-first and agent-readable.** The main UI is a local Next app, but the repository also ships `cli/siftly.ts` with JSON commands for `stats`, `categories`, `search`, `list`, and `show`, so an agent can pull structured bookmark memory without scraping the web UI ([cli/siftly.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/cli/siftly.ts), [CLAUDE.md](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/CLAUDE.md)). AI provider auth is pragmatic: Anthropic/OpenAI/MiniMax SDK clients, Claude/Codex CLI fallbacks, DB-saved settings, env vars, and local proxy paths are all wired ([lib/ai-client.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/ai-client.ts), [lib/claude-cli-auth.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/claude-cli-auth.ts), [lib/settings.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/settings.ts)).

**Trust is local and inspectable, but not source-faithful.** The system preserves raw JSON, media URLs, confidence scores, import jobs, and derived metadata, and it can export CSV/JSON/ZIP or Obsidian markdown notes/indexes ([lib/exporter.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/exporter.ts), [lib/obsidian-exporter.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/obsidian-exporter.ts)). I did not find a claim-level provenance model tying each semantic tag, image tag, category, or search explanation back to exact source spans or verification tests.

## Artifact analysis

- **Storage substrate:** `sqlite` `files` — The active memory store is SQLite via Prisma models for bookmarks, media, categories, category joins, settings, and import jobs; the FTS5 virtual table is also SQLite-managed at runtime. File outputs exist as import JSON, media/export archives, and optional Obsidian markdown exports, but they are not the primary live read path ([prisma/schema.prisma](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/prisma/schema.prisma), [lib/db.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/db.ts), [lib/fts.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/fts.ts), [lib/obsidian-exporter.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/obsidian-exporter.ts)).
- **Representational form:** `prose` `symbolic` — Tweet text, category descriptions, visual summaries, semantic tags, search reasons, and exported markdown are prose. Tweet ids, JSON blobs, Prisma rows, FTS rows, category slugs, confidence scores, API routes, CLI commands, and parser outputs are symbolic. I found no durable embedding index, learned ranker, adapter, or model-weight artifact in the repo.
- **Lineage:** `authored` `imported` — Default categories, prompts, parser code, AI provider settings, API routes, and CLI behavior are authored. Bookmark rows, raw tweet JSON, media URLs, entities, OCR/vision summaries, semantic tags, category assignments, FTS rows, search explanations, and exports are imported from user-provided X data or derived from that imported corpus. I found no durable artifact derived from agent session logs, tool traces, trajectories, or transcripts, so this review is not tagged `trace-derived`.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Bookmark records and exports are knowledge artifacts for humans and agents; category descriptions and AI prompts instruct categorization/search models; slugs, source/media filters, FTS ids, intent categories, and mindmap graph edges route navigation; parsers, duplicate checks, path validation, response parsing, confidence clamping, and route guards validate; FTS rank, category confidence, candidate selection, LLM scores, and cache order rank; enrichment and category-suggestion paths learn reusable metadata/categories from the imported corpus.

**Bookmark rows.** The operative retained object is the bookmark plus its derived fields: raw JSON is evidence, normalized text/media make it browsable, entities and semantic tags make it searchable, category joins make it routable, and `enrichedAt` drives incremental processing. The row is not merely a saved tweet; it is a compact record of how future search and category views should treat that tweet.

**Categories and category descriptions.** Categories bundle user-facing organization with model-facing policy. A category name and slug route browse/mindmap/search filters, while the description is inserted into categorization prompts as the semantic boundary for later assignments. That makes category edits high-authority compared with ordinary bookmark edits.

**FTS5 table and AI-search prompt entries.** `bookmark_fts` is a derived access structure over text, semantic tags, entities, and image tags. AI search then builds query-specific prompt entries from selected rows. This is a pointer stack: fixed stored metadata narrows candidates, and query-time LLM ranking decides the final answer.

**Obsidian export.** The export path promotes selected bookmark rows into markdown notes and category/author indexes under a user-chosen vault folder. This improves portability and human review, but the exported notes are snapshots; the live app does not read them back as the canonical store.

**Promotion path.** Siftly promotes raw bookmarks into enriched knowledge records: imported tweet JSON becomes entities, image tags, semantic tags, category assignments, FTS rows, mindmap nodes, and optional markdown notes. The promotion crosses from raw imported evidence toward symbolic/prose navigation surfaces, but it does not create enforced rules, validators, or agent instructions from usage traces.

## Comparison with Our System

Siftly and Commonplace both rely on local inspectable artifacts, but their center of gravity differs. Siftly optimizes a personal social-bookmark corpus for interactive retrieval: capture is easy, enrichment is automatic, and search uses pragmatic candidate narrowing plus LLM reranking. Commonplace optimizes methodology artifacts for agent operation: source grounding, type contracts, validation, review gates, and authored links matter more than one-click import.

The strongest alignment is the layered-context pattern. Siftly avoids full-corpus prompt stuffing by building derived metadata and query-specific candidate sets before model reranking. Commonplace uses descriptions, indexes, links, `rg`, source snapshots, and review bundles for a similar reason, but keeps most of those pointers in git-tracked markdown rather than SQLite rows.

The main divergence is authority. Siftly's AI-derived tags/categories can silently shape future search and categorization, but they lack per-claim lineage or review state. Commonplace is slower because derived artifacts must satisfy collection/type contracts and validation, yet that friction is what lets its notes act as durable methodology rather than convenient personal search metadata.

### Borrowable Ideas

**Corpus-specific semantic tags as query-time pointers.** Commonplace could generate non-authoritative search tags for source snapshots or reviews, stored separately from canonical note text. Ready for experimental search support, but not as a replacement for descriptions or authored links.

**Category descriptions as prompt policy.** Siftly's category descriptions are concise, editable routing rules. Commonplace already has collection contracts; a lighter category-description layer could help temporary workshops or review reruns route artifacts before a durable taxonomy exists. Needs a concrete workflow before promotion.

**JSON CLI over the memory store.** `cli/siftly.ts` is a clean adoption affordance for agents. Commonplace's command family already serves this role, but Siftly is a reminder that every UI knowledge store should expose a small, stable, JSON-emitting pull surface.

**Export as adoption bridge, not canonicalization.** Siftly's Obsidian export is useful because it acknowledges where users may already review and reuse knowledge. Commonplace could borrow this for outbound reports, while keeping canonical artifacts under the existing type and validation regime.

## Write side

**Write agency:** `manual` `automatic` — Users manually import files, create/edit categories, configure settings, run exports, delete bookmarks, and accept generated category suggestions. Automatic paths parse imported tweet data, skip duplicate tweet ids, extract entities, analyze images, generate semantic tags, assign categories, update `enrichedAt`, rebuild FTS, cache search results, and write export files when invoked.

**Curation operations:** `evolve` — The implemented automatic memory curation is in-place evolution of existing bookmark/media/category state after acquisition: rows receive entities, image tags, semantic tags, category assignments, enrichment metadata, confidence scores, and rebuilt access structures. Import-time duplicate skipping and image-analysis reuse reduce repeated work, but they do not merge stored memories; FTS rebuilds and search caches are access-structure upkeep, not content curation. Category suggestions can synthesize possible new categories from a corpus sample, but they become stored categories only through the user-facing acceptance route, so I would not classify that as autonomous curation.

Siftly is not trace-derived under the current review contract. Its durable learned artifacts come from imported X/Twitter bookmark content and media, not from agent session logs, transcripts, tool/action traces, trajectories, or rollout history.

## Read-back

**Read-back:** `pull` — Stored memory re-enters action only when a human or agent explicitly opens a page, filters a view, calls an API route, runs the JSON CLI, exports notes, or submits a search query. The repo does not implement unsolicited memory injection into an agent prompt, hook, scheduler, or task context.

The read-back surfaces are broad but pull-only: browse/filter uses structured DB queries; mindmap pulls category/bookmark graph data; CLI `search/list/show/stats/categories` returns JSON; AI search pulls candidates with FTS/filters and asks an LLM to rerank a bounded prompt entry set ([app/api/bookmarks/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/bookmarks/route.ts), [app/api/mindmap/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/mindmap/route.ts), [cli/siftly.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/cli/siftly.ts), [app/api/search/ai/route.ts](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/search/ai/route.ts)). Precision, recall, and whether an external agent would faithfully use CLI results are not verified by code.

## Curiosity Pass

**The app is closer to a personal RAG corpus than an agent memory system.** Its memory value is real: saved social posts become searchable, categorized, visual, exportable context. But the system does not retain agent experience or update agent instructions from use.

**The strongest behavior-shaping prose is category description text.** A category description looks like metadata, but it is injected into prompts and can steer every later categorization. That makes category editing closer to prompt engineering than ordinary labeling.

**The search path is semantic only after candidate selection.** AI search can reason over rich prompt entries, but it first depends on keyword/FTS/category-intent selection plus recent fallback. That is a reasonable local-cost tradeoff, not a full semantic index.

**Obsidian export improves reviewability but creates a second surface.** Exported notes and indexes are useful for humans and agents outside Siftly, yet they can drift immediately because the app continues to treat SQLite as the live store.

**Local-first privacy is partial.** Storage is local, but vision, enrichment, categorization, and AI search send selected tweet/media context to the configured model provider or CLI-backed service. The README states this clearly; the code matches that architecture.

## What to Watch

- Whether Siftly adds embeddings or a durable vector index. That would change the representational form and make candidate selection less dependent on lexical FTS.
- Whether exported Obsidian notes become a bidirectional sync surface. That would turn files from snapshots into a competing or shared storage substrate.
- Whether category suggestions gain an autonomous acceptance policy. That would move the write-side classification from human-approved suggestions toward automatic synthesis over stored bookmarks.
- Whether the CLI grows AI search and export commands, not only FTS/list/show. That would make Siftly more directly useful as an agent pull-memory service.
- Whether derived tags/categories gain source-span provenance or review states. That would make AI enrichment safer to reuse as durable knowledge rather than search metadata.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Siftly stores rich bookmark memory but serves it by explicit browse/search/API/CLI/export pulls.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: SQLite rows, FTS rows, category descriptions, prompts, and exports carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: bookmarks, raw tweet JSON, visual summaries, semantic tags, and exported notes mostly provide evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: category descriptions, prompts, parsers, FTS construction, candidate selection, route guards, and CLI/API contracts shape later behavior.
- [Context efficiency is the central design concern in agent systems](../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - grounds: Siftly's candidate narrowing and compact prompt entries are context-efficiency machinery.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - contrasts: Siftly relies on available symbols such as ids, slugs, FTS terms, categories, entities, and tags before LLM reranking can help.
