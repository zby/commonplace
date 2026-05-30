---
description: "Self-hosted X bookmark ingestion system that stores raw tweet/media evidence in SQLite, derives AI tags/categories, and serves hybrid search plus mindmap exploration"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-05-16"
---

# Siftly

Siftly is viperrcrypto's self-hosted Twitter/X bookmark manager. It imports bookmarks and likes into a local SQLite database, preserves raw tweet JSON, extracts deterministic entities, calls configured LLM/vision providers to enrich media and bookmark text, categorizes bookmarks into configurable category rows, and exposes browse, AI search, export, and mindmap UI surfaces. It is relevant to agent memory as a personal ingestion and enrichment system: the retained bookmark corpus is a knowledge artifact for later search and review, while the category descriptions, prompts, provider settings, and pipeline code are system-definition artifacts with classification and ranking authority.

**Repository:** https://github.com/viperrcrypto/Siftly

**Reviewed commit:** [b25daa45b858f4be096b5c368671c34db4407d8e](https://github.com/viperrcrypto/Siftly/commit/b25daa45b858f4be096b5c368671c34db4407d8e)

## Core Ideas

**SQLite is the storage substrate for both raw and derived bookmark state.** The Prisma schema keeps `Bookmark` rows with stable tweet IDs, text, author fields, source type, timestamps, and `rawJson`, then hangs `MediaItem`, `BookmarkCategory`, `Category`, `ImportJob`, and `Setting` rows off that local database ([schema](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/prisma/schema.prisma)). Raw tweet JSON and media URLs are the source evidence. `semanticTags`, `entities`, `enrichmentMeta`, `imageTags`, category joins, settings, and the runtime FTS5 table are derived or behavior-shaping state rather than independent source material.

**Import accepts several bookmark/media source formats but normalizes them into one bookmark model.** `parseBookmarksJson()` accepts raw Twitter-like tweet arrays, flat exporter rows, Siftly re-export rows, and the app's console/bookmarklet `{ bookmarks: [...] }` shape, then normalizes IDs, text, author, hashtags, URLs, media, and raw JSON ([parser](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/parser.ts)). The upload endpoint deduplicates on `tweetId`, creates `Bookmark` rows, stores media rows, records an `ImportJob`, and distinguishes `source: "bookmark"` from `source: "like"` ([import API](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/route.ts)). The client-side import page also ships a bookmarklet and console script that intercept X/Twitter API responses while the user scrolls, then emits JSON for upload ([import UI](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/import/page.tsx)).

**Live X import is implemented as an optional second source path.** Besides file/bookmarklet import, Siftly has X OAuth 2.0 PKCE routes that store verifier/state, exchange tokens, refresh access tokens, and fetch `/2/users/me/bookmarks` pages with media/user expansions into the same `Bookmark` and `MediaItem` tables ([authorize route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/x-oauth/authorize/route.ts), [callback route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/x-oauth/callback/route.ts), [fetch route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/import/x-oauth/fetch/route.ts)). A separate cookie/session-token sync path uses X internal GraphQL pagination and a scheduler setting for recurring sync ([twitter API helper](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/twitter-api.ts), [sync scheduler](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/x-sync.ts)).

**Deterministic extraction is a cheap derived layer before LLM calls.** `extractEntities()` parses stored `rawJson` and mines hashtags, URLs, mentions, tweet type, media types, and known tool/product names from a curated domain map without an AI call ([raw JSON extractor](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/rawjson-extractor.ts)). This output is a derived knowledge artifact when shown or indexed, but the curated domain table and extraction rules are symbolic system-definition artifacts because they decide what counts as a tool, URL, reply, quote, or thread.

**LLM enrichment is multi-stage and field-oriented.** Vision analysis prompts an AI model for JSON containing people, OCR text, objects, scene, action, mood, style, meme template, and tags, then stores the JSON in `MediaItem.imageTags` ([vision analyzer](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/vision-analyzer.ts)). Semantic enrichment combines text, image context, entities, hashtags, tools, and mentions to generate `semanticTags` plus sentiment, people, and company metadata. Categorization then combines tweet text, image context, AI tags, hashtags, and tools with the live `Category.description` values to assign 1-3 categories and confidence scores ([categorizer](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/categorizer.ts)). The derived tags and assignments advise search and browsing; the prompts and category descriptions instruct future enrichment.

**Stage markers make the pipeline resumable, but the orchestration state is in-memory.** Pipeline status, stage counters, abort flag, and current stage live in `globalThis` for API polling, while durable progress is inferred from database markers: `entities: null`, `imageTags: null` or `{}`, `semanticTags: null` or `[]`, and `enrichedAt` ([categorize route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categorize/route.ts), [vision analyzer](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/vision-analyzer.ts)). A forced run clears some failure sentinels and reprocesses all bookmarks. This is practical resumability for local enrichment, not an audited lineage graph: each derived field records little about prompt version, model version, or source-field version beyond its current value.

**Concurrency and retry policy are local and bounded.** Vision uses 12 concurrent media tasks, retries retryable SDK failures with fixed delays, skips large images, caches duplicate URL analysis, and writes `{}` after failed media attempts to avoid infinite loops ([vision analyzer](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/vision-analyzer.ts)). Bulk semantic enrichment uses batches of five with two concurrent batches. The current categorize API also runs bookmark workers with a five-worker pool and drains a shared categorization queue in 25-item batches ([categorize route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categorize/route.ts)). Failed semantic enrichments remain null for retry; failed categorization batches are logged and not promoted into a durable error artifact.

**Search is hybrid retrieval plus LLM reranking.** `bookmark_fts` is a runtime SQLite FTS5 virtual table over bookmark text, semantic tags, entities, and image tags, rebuilt after enrichment ([FTS helper](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/fts.ts)). The AI search route extracts keywords, detects likely category intent from regexes and category metadata, retrieves FTS/category/recent candidates, builds rich per-bookmark index entries, and asks the configured LLM or CLI to return scored matches and short reasons ([AI search route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/search/ai/route.ts), [keyword utility](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/search-utils.ts)). FTS rows and LLM rerank output have ranking authority over search results, but they do not update the underlying corpus or category definitions.

**Categories are both labels and prompt controls.** Default categories are seeded from code, custom categories are stored in SQLite with name, slug, color, and prose description, and category descriptions are passed directly into categorization prompts ([categorizer](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/categorizer.ts)). The category-suggestion feature samples bookmarks and asks an LLM for 3-8 topic clusters, then creates selected suggestions as `Category` rows marked `isAiGenerated` ([category suggester](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/category-suggester.ts), [suggest route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categories/suggest/route.ts)). A category assignment is a derived knowledge artifact; a category description is a prose system-definition artifact because it instructs later classification.

**Export and visualization are derived consumer surfaces.** CSV, JSON, ZIP, and Obsidian export read from the database and emit downstream files, including media downloads and Obsidian notes with category/author indexes ([exporter](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/exporter.ts), [Obsidian exporter](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/obsidian-exporter.ts)). The mindmap API serves root, category, and tweet nodes with confidence and visual summaries, while the mindmap page can start categorization when the map is empty ([mindmap API](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/mindmap/route.ts), [mindmap page](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/mindmap/page.tsx)). These surfaces make the retained artifacts navigable, but they are views over the database rather than reviewed canonical notes.

**Auth and model settings are operational authority.** Siftly resolves providers across Anthropic, OpenAI, and MiniMax SDK wrappers, with CLI fallback through Claude Code or Codex when available ([AI client](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/ai-client.ts), [settings](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/lib/settings.ts)). The settings API stores API keys, provider selection, allowed model IDs, X OAuth credentials, and Obsidian vault path in the `Setting` table ([settings route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/settings/route.ts)). These rows are system-definition artifacts with configuration authority over future enrichment, search, import, and export behavior.

## Comparison with Our System

| Dimension | Siftly | Commonplace |
|---|---|---|
| Primary substrate | Local SQLite through Prisma, plus runtime FTS5 | Git-tracked typed markdown, generated indexes, validation reports |
| Source evidence | Raw tweet JSON, normalized bookmark fields, media URLs, imported source type | Source snapshots, reviewed notes, references, ADRs, instructions |
| Derived knowledge artifacts | Entities, image tags, semantic tags, enrichment metadata, category assignments, search explanations | Indexes, connect reports, review outputs, source-linked notes |
| System-definition artifacts | Pipeline code, prompts, category descriptions, known-tool domain table, model/provider settings | Type specs, collection contracts, AGENTS.md, skills, validation/review commands |
| Lineage | Mostly row-level source/derived fields and null/sentinel stage markers | File paths, frontmatter, links, git history, source snapshots, review records |
| Retrieval surface | FTS5 candidate search, regex category intent, LLM reranking, browse filters, command palette, mindmap | `rg`, descriptions, authored links, curated indexes, connect reports, review gates |
| Promotion path | Import -> enrich -> categorize -> search/export/view | Workshop/source -> note/reference/instruction -> validation/review -> generated views |

Siftly is stronger as a turnkey personal ingestion app. It has concrete import affordances for a high-friction source, local database storage, media-aware enrichment, configurable providers, search UI, mindmap exploration, and export. Commonplace is stronger where retained artifacts need reviewable authority: Siftly stores useful annotations and categories, but it does not make explicit claims, review status, source confidence, retirement state, or promotion boundaries for turning a bookmark insight into an instruction, test, skill, or maintained note.

The most important artifact split is that Siftly stores source material and derived metadata in the same database row family. That is fine for a bookmark manager, but it makes source-of-truth status implicit. Raw `rawJson`, tweet text, media URLs, and source fields are evidence. AI tags, image JSON, enrichment metadata, category joins, FTS rows, and AI search reasons are derived views. Category descriptions, prompts, known-tool rules, provider/model settings, OAuth credentials, and export paths are behavior-shaping system-definition artifacts.

Siftly does not learn from traces in the agent-memory sense. It persists import/sync state and derived annotations from bookmarks, and it can create AI-suggested categories from the bookmark corpus. I did not find code that mines prior search sessions, user corrections, pipeline failures, or repeated task traces into durable behavior-changing rules, prompts, rankers, validators, or model weights. User-created categories and settings shape later behavior, but they are direct operator configuration rather than trace-derived learning.

**Read-back:** pull — users or agents deliberately search, browse, filter, export, or inspect the mindmap to consume enriched bookmark context.

## Borrowable Ideas

**Keep raw source payloads next to normalized fields.** Ready to borrow for high-variance web sources. Siftly keeps `rawJson` while also normalizing common fields, which lets later extractors recover more structure without re-importing.

**Use null and sentinel fields for local resumability.** Ready as a pragmatic pattern for batch enrichment jobs. `imageTags: null` means unattempted, `{}` means attempted but failed, and `enrichedAt` marks categorization completion. Commonplace would need stronger lineage if the derived output gained library authority.

**Treat category descriptions as prompt-time controls.** Useful when categories are local and operator-owned. In commonplace, the closest equivalent is collection/type prose with stronger review expectations; for workshop-local clustering, Siftly's lightweight category descriptions are enough.

**Build search from cheap candidates plus expensive reranking.** Ready to borrow for future interactive search. FTS and intent regexes reduce the candidate set, while the LLM only reranks rich summaries. Commonplace should keep canonical files and use such indexes as derived projections.

**Offer visual and export views without making them canonical.** The mindmap, CSV/JSON/ZIP, and Obsidian export are useful consumer surfaces. Commonplace could borrow the "views are rebuildable/exportable" stance while preserving typed notes as source of truth.

## Curiosity Pass

**The pipeline is more resumable than auditable.** It can restart from missing fields and avoid infinite loops on failed media, but it does not preserve prompt versions, model versions, raw AI responses, or invalidation rules when category descriptions and prompts change.

**The README's "4-stage" description is directionally right, but the current route runs a parallel per-bookmark pipeline after entity extraction.** The API exposes `entities` and `parallel` as durable status stages, and old `vision`, `enrichment`, and `categorize` labels still appear in the UI types for display compatibility ([categorize route](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/api/categorize/route.ts), [categorize page](https://github.com/viperrcrypto/Siftly/blob/b25daa45b858f4be096b5c368671c34db4407d8e/app/categorize/page.tsx)).

**Category suggestion is corpus-derived but not trace-derived learning.** It samples enriched bookmarks and asks the model for clusters, then lets the operator create category rows. That changes future categorization if accepted, but the source signal is the bookmark corpus, not operational traces or user corrections.

**The FTS table is a compiled view with ranking influence.** It is intentionally outside Prisma's schema and rebuilt at runtime. That keeps it operationally simple, but if Siftly begins relying on search explanations for high-stakes recall, it will need stronger synchronization and audit reporting.

**Security and privacy claims depend on local deployment discipline.** Bookmark data stays in SQLite and API keys/settings are local rows, but enrichment sends tweet text and image data or image URLs to the configured provider/CLI path. OAuth and X session credentials are also stored in the local settings table.

## What to Watch

- Whether Siftly starts recording prompt/model versions or derivation metadata for `imageTags`, `semanticTags`, `enrichmentMeta`, and category assignments.
- Whether user corrections to categories become training data, prompt amendments, category-description edits, or ranking signals. That would change the trace-derived classification if mined from durable correction traces.
- Whether FTS rebuilds become incremental and tied to schema/version markers rather than full rebuilds after pipeline completion.
- Whether AI-suggested categories gain review status, merge/split lifecycle, or evidence links before receiving future categorization authority.
- Whether Obsidian export grows from one-way export into a round-trip knowledge workflow with stable IDs and invalidation rules.

---

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: Siftly makes bookmarks searchable, but downstream search and prompt assembly still decide activation.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, category descriptions, provider settings, domain maps, and pipeline code shape later behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw bookmarks, media context, tags, category assignments, and exports advise later users or agents.
- [Lineage](../../notes/definitions/lineage.md) - clarifies: Siftly has raw payload retention and stage markers, but limited derivation/version lineage for AI outputs.
- [Files beat a database for agent-operated knowledge bases](../../notes/files-not-database.md) - contrasts: Siftly appropriately uses SQLite for an application corpus, while commonplace keeps reviewed knowledge in files.
