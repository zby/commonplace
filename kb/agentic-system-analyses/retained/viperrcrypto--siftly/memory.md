---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Siftly memory: retained bookmark content, derived metadata, selection state and independent search/export copies."
run-id: AAS-2026-10-18-siftly-b81c94cf0f77-01
source-identity: "https://github.com/ViperrCrypto/Siftly"
reviewed-boundary: b25daa45b858f4be096b5c368671c34db4407d8e
---

# Siftly memory report

## Boundary and evidence

This report covers Siftly's SQLite bookmark memory, model-derived metadata, category guidance, FTS index, request caches, browser/CLI consumption and exports at SRC-1, commit b25daa45b858f4be096b5c368671c34db4407d8e. The [boundary](boundary.md#source-register) supplies the source identity and evidence layers. Source reads below establish implementation; supplied runtime records establish the separately attributed ingress and configuration account. No observed database, provider response, runtime trace or experiment was supplied. Delivery wiring does not establish correct descriptions, model compliance or useful downstream agent behavior.

The external models and CLI runtimes are included only at Siftly's adapters. Their opaque weights, conversations, tool activity and retention policies are not inspected. The supplied [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch) and model-component records retain those limits. Actual X accounts, files selected by users and destination vaults were not supplied. These gaps prevent provenance verification of deployed content and conclusions about exercised downstream use, not inspection of shipped consumers.

### Coverage inventory

“Direct” means source inspection in this job; “supplied” means the runtime account, not a new source read. All source paths below belong to SRC-1. An available helper without a discovered caller is not treated as an activated route.

| Entry point or operation | Source path and inspection | Covering records or limit |
|---|---|---|
| File upload, bookmarklet, Twitter URL, live/sync and OAuth acquisition | Supplied: `app/api/import/route.ts`, `app/import/page.tsx`, `app/api/import/bookmarklet/route.ts`, `app/api/import/twitter/route.ts`, `lib/x-sync.ts`; OAuth fetch covered by supplied boundary | [RT-RTE-import-content](runtime.md#rt-rte-import-content); [MEM-OBJ-raw-json](#mem-obj-raw-json). OAuth response normalization not independently inspected here; no uniform payload-completeness claim. |
| Main pipeline, force, stop and incremental selection | Direct: `app/api/categorize/route.ts`, `lib/categorizer.ts`, `lib/vision-analyzer.ts`, `lib/rawjson-extractor.ts`, `lib/image-context.ts` | [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), its annotation and the five SQLite parts below. |
| Image-only HTTP processing | Direct: `app/api/analyze/images/route.ts`, `lib/vision-analyzer.ts` | [MEM-RTE-image-analysis](#mem-rte-image-analysis); same metadata store, different selector and no FTS refresh. |
| Exported processing helpers | Direct: `lib/categorizer.ts` (`categorizeAll`); `lib/vision-analyzer.ts` (`analyzeUntaggedImages`, `analyzeAllUntagged`, `enrichAllBookmarks`, `enrichBookmarkSemanticTags`) | Shared writers and parts below. Bounded caller search in `app/`, `lib/`, `cli/` found definitions but no callers for these helpers. They establish library capabilities, not additional deployed consumers; bulk and single-item semantic writes differ in ID handling. |
| Category suggestion, adoption, manual replacement and deletion | Direct: `lib/category-suggester.ts`, `app/api/bookmarks/[id]/categories/route.ts`, `app/api/categories/[slug]/route.ts`; supplied UI/API adoption account | [RT-RTE-category-admission](runtime.md#rt-rte-category-admission), [MEM-OBJ-category](#mem-obj-category), [MEM-OBJ-bookmark-category](#mem-obj-bookmark-category). |
| AI search, index maintenance and result caching | Direct: `app/api/search/ai/route.ts`, `lib/fts.ts`; caller search for `rebuildFts` | [RT-RTE-search-content](runtime.md#rt-rte-search-content), [MEM-OBJ-bookmark-fts](#mem-obj-bookmark-fts), [MEM-OBJ-search-cache](#mem-obj-search-cache). |
| CLI dispatch and retained-detail retrieval | Direct: `cli/siftly.ts` dispatch, search/list/show | [RT-RTE-cli-export](runtime.md#rt-rte-cli-export); commands are search, list, show, categories, stats, not a registered tool-execution loop. |
| Browser list and graph | Direct: `app/api/bookmarks/route.ts`, `app/api/mindmap/route.ts` category-node projection | [MEM-RTE-browse-memory](#mem-rte-browse-memory); graph display is not the underlying payload. |
| CSV, JSON, ZIP and Obsidian output | Direct: `app/api/export/route.ts`, `lib/exporter.ts`, `lib/obsidian-exporter.ts`; supplied Obsidian endpoint account | [RT-RTE-cli-export](runtime.md#rt-rte-cli-export), [MEM-OBJ-export-copy](#mem-obj-export-copy). External readers are afforded, not observed. |
| Clear collection | Direct: `app/api/bookmarks/route.ts` DELETE and dependent cache/index/export code | [MEM-RTE-clear-collection](#mem-rte-clear-collection). |
| Settings, credentials and import/progress metadata | Direct schema; supplied `lib/settings.ts`, `app/api/settings/route.ts`, main process-state account | [RT-RTE-settings-change](runtime.md#rt-rte-settings-change), [RT-OBJ-categorization-state](runtime.md#rt-obj-categorization-state), annotations below. Resolver internals not re-audited; no deployed secret-storage guarantee. |
| Evaluation, hooks and trace-fed revision search | Bounded source search in `app/`, `lib/`, `cli/`, `package.json`, `README.md`, `CLAUDE.md`, `__tests__/` for feedback/rating/evaluation, compaction, hooks/tool registration and helper callers | No additional feedback-to-content writer established by this inspection. Supplied boundary identifies mocked adapter tests, not retrieval evaluation. This is a search limit, not a system-wide absence record or proof about external CLI internals. |

## Core ideas

1. Siftly retains imported content and multiple derived views, not a conversation memory. `rawJson` can feed deterministic entity backfill; downloaded images feed model vision; text, entities and vision feed semantic tags; those tags feed classification and search. The raw input remains in SQLite while each consumer receives a projection. These are knowledge transformations, not demonstrated learning from Siftly's own success/failure outcomes ([MEM-OBJ-raw-json](#mem-obj-raw-json), [MEM-OBJ-entities](#mem-obj-entities), [MEM-OBJ-image-tags](#mem-obj-image-tags), [MEM-OBJ-semantic-tags](#mem-obj-semantic-tags)).
2. Retained processing markers govern future work independently of content quality. `{}`, `[]` and enrichedAt can prevent later attempts. Force resets only specific empty markers; category success can mark a bookmark processed even when semantic enrichment failed. Stop preserves committed rows and can leave the index unrefreshed ([RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), annotation below).
3. Generated metadata is promoted into evidence-like prompt context without a retained accuracy warrant. Categorization says to trust aiTags heavily; search calls them highly reliable. Those instructions establish intended authority, not verified reliability ([RT-CLM-category-policy](runtime.md#rt-clm-category-policy), [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search), [MEM-OBJ-search-cache](#mem-obj-search-cache)).
4. Withdrawal has several horizons. Deleting database content is not cache invalidation, FTS rebuilding or deletion of exported Markdown. Manual category replacement differs from the model's additive upsert; a later model pass can add back memberships ([MEM-RTE-clear-collection](#mem-rte-clear-collection), [MEM-OBJ-bookmark-category](#mem-obj-bookmark-category), [MEM-OBJ-export-copy](#mem-obj-export-copy)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw-json
Label: Bookmark rawJson and imported content
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite Bookmark.rawJson stores serialized imported tweet data alongside readable text, author, tweetId and source fields. The payload is source-native input, not a Siftly execution log. Natural-language tweet text is interpreted by models/humans; IDs and dates have fixed join/selection semantics; raw JSON's nested content is only partially interpreted by extraction. Import callers supply the material and parsers/software admit it; choosing an import is not human verification of its truth or approval of generated additions. Duplicate skipping preserves an earlier record rather than revising it. Scope and evidence: SRC-1, `prisma/schema.prisma`; supplied [RT-RTE-import-content](runtime.md#rt-rte-import-content).

> rawJson       String    // full JSON stored as string
> --- `prisma/schema.prisma`

Later entity extraction reloads rawJson, while ordinary classification/search use derived fields rather than the complete payload. CLI show also omits rawJson. Thus retaining the raw input affords re-extraction in the code, but does not mean each later consumer sees provenance or full evidence (SRC-1, `lib/rawjson-extractor.ts`, `cli/siftly.ts`, `app/api/search/ai/route.ts`).

#### MEM-OBJ-entities
Label: Bookmark entities
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite Bookmark.entities is JSON containing hashtags, URLs, mentions, detected tools, tweet type and media descriptors. Backfill selects entities=null and derives these fields from retained rawJson using fixed extraction rules; malformed input becomes the empty structure, which is nevertheless serialized and persisted. This is software admission without per-record human review or a model answer oracle. Hashtag/tool strings become natural-language signals in later prompts; fixed field tests and LIKE/FTS token matching give symbolic selection effects. Consumers include enrichment, categorization, category suggestions, AI search and CLI detail (SRC-1, `lib/rawjson-extractor.ts`, `lib/vision-analyzer.ts`, `lib/categorizer.ts`, `lib/category-suggester.ts`, `cli/siftly.ts`).

> const entities = extractEntities(b.rawJson)
>       await prisma.bookmark.update({
>         where: { id: b.id },
>         data: { entities: JSON.stringify(entities) },
>       })
> --- `lib/rawjson-extractor.ts`

This retains normalized facts, not extraction explanations or an independent source-veracity judgment. Null-only backfill means a previously persisted empty result is not automatically regenerated. Initialization through every alternate ingress was not independently inspected here; known subsequent backfill remains established.

#### MEM-OBJ-image-tags
Label: MediaItem imageTags
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite MediaItem.imageTags mixes two operative cases. Successful parseable JSON stores natural-language scene/action, OCR, tags and other model descriptions; `{}` is a symbolic attempted/failure marker. Both persist past the request, but only contentful results supply substantive visual context. SDK input is fetched image bytes; CLI input is an image URL in text, so equivalent image access is not established. The parser checks JSON parseability, not truth or full schema compliance. Software admits the model output without human verification. URL-level reuse selects another non-null result and can copy `{}` too (SRC-1, `lib/vision-analyzer.ts`).

> await prisma.mediaItem.update({ where: { id: item.id }, data: { imageTags: '{}' } })
> --- `lib/vision-analyzer.ts`

Lineage is media URL/thumbnail → provider output or another row's cached output → retained JSON → prompt summary/search/CLI/graph. No model-version or rationale history is stored in this field. The symbolic failure chain is attempted analysis → `{}` → later null-only selectors skip it, not improved image understanding. Force can reset this marker; successful results have no source/model-version expiry in the inspected pipeline. Storage of the result does not freeze the remote media bytes (SRC-1, `app/api/categorize/route.ts`, `app/api/analyze/images/route.ts`).

#### MEM-OBJ-semantic-tags
Label: Bookmark semanticTags and enrichmentMeta
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

These SQLite strings contain model-generated tag arrays and sentiment/people/companies metadata. The source is imported text plus compacted image context and selected entities, not task-performance feedback. The parser coerces strings and defaults fields; it does not independently validate tag correctness or calibrate sentiment. Automatic application admission differs from model authorship and physical database I/O. A trivial bookmark can instead receive `[]`, a software skip marker. Bulk helper failures leave null; the main pipeline also writes only nonempty returned tags. Existence of either helper does not establish its invocation (SRC-1, `lib/vision-analyzer.ts`, `app/api/categorize/route.ts`).

> tags: Array.isArray(item.tags) ? (item.tags as unknown[]).map(String).filter(Boolean) : [],
> --- `lib/vision-analyzer.ts`

Semantic strings receive natural-language interpretation in later categorization, suggestion and search. JSON array syntax is not a symbolic reasoning system. CLI show exposes enrichmentMeta; search's buildIndexEntry does not expose that whole metadata object. The retained fields contain results rather than derivation reasons. Main-pipeline and single-item-helper writes take results[0]; the bulk helper uses an ID map. Do not infer a common input-ID validation guarantee from the bulk implementation (SRC-1, `lib/vision-analyzer.ts`, `app/api/categorize/route.ts`, `app/api/search/ai/route.ts`, `cli/siftly.ts`).

#### MEM-OBJ-bookmark-category
Label: BookmarkCategory and enrichedAt
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite relational membership and confidence are symbolic selection state; category names become human/model-readable interpretation. enrichedAt is a persisted selection timestamp, not an audit of every stage's success. The model writer maps returned tweet IDs to existing rows and upserts assignments; omitted old memberships remain. Parser filtering and confidence clamping are computational admission; no reference-answer oracle or human veto intervenes. Current-batch membership is not checked, as supplied [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) establishes. Consumers use joins for browsing, graph, exports, search intent and later missing-work selection (SRC-1, `lib/categorizer.ts`, `prisma/schema.prisma`).

> data: { enrichedAt: now },
> --- `lib/categorizer.ts`

Manual PUT instead deletes old links and creates the submitted category IDs with confidence 1.0. That number means caller assignment, not calibrated certainty; generic HTTP input does not prove human authorship. Delete and create are separately awaited, not a transaction in this handler, so failed creation can leave assignments removed. A later categorization can re-add links; there is no retained exclusion veto or revision rationale in these rows (SRC-1, `app/api/bookmarks/[id]/categories/route.ts`).

> await prisma.bookmarkCategory.deleteMany({ where: { bookmarkId: id } })
> --- `app/api/bookmarks/[id]/categories/route.ts`

#### MEM-OBJ-category
Label: Category descriptions and identities
Part of: [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark)

SQLite Category.name/description contain natural-language classification guidance; slug/id are symbolic allowed identities and join keys. Shipped defaults are seeded and overwritten from code, while accepted suggestions derive descriptions from sampled retained bookmarks. Suggestion samples prefer non-null semanticTags/entities and recent imports, up to 100, with text bounded to 280 characters; fewer than ten blocks suggestion generation. Provenance is collection content, not measured categorization errors. Suggested examples/counts/confidence are response material; createCategoryFromSuggestion persists only name/slug/description/color/isAiGenerated, not those reasons/examples. Accepted guidance therefore outlives its displayed supporting examples without a stored explanatory history (SRC-1, `lib/category-suggester.ts`, `lib/categorizer.ts`).

> name: suggestion.name.slice(0, 50),
>       slug: suggestion.slug.slice(0, 50),
>       description: suggestion.description.slice(0, 500),
>       color: suggestion.color,
>       isAiGenerated: true,
> --- `lib/category-suggester.ts`

Admission, human selection affordance, rejection of duplicate names/slugs and lack of proof of UI approval are supplied by [RT-RTE-category-admission](runtime.md#rt-rte-category-admission). Subsequent prompt authority is already declared by [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance); this part does not duplicate that path. Deletion removes linked assignments via cascade, while a later seed can recreate a default category. Category guidance is classification policy here, not an established critic/reviser of explanatory theories (SRC-1, `app/api/categories/[slug]/route.ts`, `prisma/schema.prisma`, `lib/categorizer.ts`).

#### MEM-OBJ-bookmark-fts
Label: bookmark_fts search projection

Distinct from the Prisma row container [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark), this SQLite FTS5 virtual table copies bookmark IDs, text, semantic tags, entities and combined media tags. It is a derived lexical index, not embeddings or model weights. Natural-language payload becomes tokens under fixed FTS rules, with IDs returned in rank order, capped at 150. Rebuild automatically deletes all existing index rows then inserts batches of 200 from current bookmarks. No human content review or answer oracle participates. Main pipeline completion calls rebuild unless stopped; bounded `app/`/`lib/` caller search found no other rebuild caller (SRC-1, `lib/fts.ts`, `app/api/categorize/route.ts`).

> await prisma.$executeRawUnsafe(`DELETE FROM ${FTS_TABLE}`)
> --- `lib/fts.ts`

Later uncached AI search and CLI search use FTS IDs, with LIKE fallback on empty/error. A nonempty stale index is not detected as stale. Database hydration removes nonexistent IDs but can omit new or newly relevant rows; it also does not restore FTS rank explicitly. FTS is persistent but not maintained by an inspected automatic database trigger. A partial rebuild can remain visible because the whole delete/reinsert is not one transaction (SRC-1, `lib/fts.ts`, `app/api/search/ai/route.ts`, `cli/siftly.ts`; closest supplied route: [RT-RTE-search-content](runtime.md#rt-rte-search-content)).

#### MEM-OBJ-search-cache
Label: AI search response cache

Distinct from the persistent collection and [MEM-OBJ-bookmark-fts](#mem-obj-bookmark-fts), this module-local Map retains complete hydrated response objects, scores/reasons and explanation for five minutes. The selector key is lowercased trimmed query plus category, not a database or model revision. At size 100, insertion deletes the first key. A later equivalent request can consume a cached response before candidate selection or new model judgment. This is short-horizon read-back within a process; persistence across restarts is not established. Software admits responses, not a human relevance evaluator (SRC-1, `app/api/search/ai/route.ts`; closest supplied route: [RT-RTE-search-content](runtime.md#rt-rte-search-content)).

> if (cached) return NextResponse.json(cached)
> --- `app/api/search/ai/route.ts`

The response can outlive mutation/deletion of source rows until expiry/eviction/process loss; hydrated content is stored by value rather than rejoined on hit. The uncached prompt's trust claim is stronger than the admission warrant:

> 2. Check ALL fields — the ai_tags field contains pre-computed semantic context and is highly reliable
> --- `app/api/search/ai/route.ts`

That is natural-language guidance, not measured reliability. Cached reasons shape what the caller sees, but no inspected route feeds those reasons back into tags or category guidance.

#### MEM-OBJ-export-copy
Label: Exported bookmark copies

Distinct from the database container [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark), exports are derived output artifacts: response CSV/JSON/ZIP and filesystem Markdown notes/indexes. The closest supplied consumer route is [RT-RTE-cli-export](runtime.md#rt-rte-cli-export). Natural-language content and symbolic metadata coexist; no grant of agent instruction authority follows from Markdown. Code formats caller-selected exports without per-note approval. Obsidian notes preserve tweet text, source URL, author/date, category names, sanitized semantic tags and media links, not rawJson, complete image analysis or enrichment rationale. JSON export likewise selects fields and is not a complete lossless database backup (SRC-1, `lib/obsidian-exporter.ts`, `lib/exporter.ts`, `app/api/export/route.ts`).

> const lines: string[] = [frontmatter, '', bookmark.text || '']
> --- `lib/obsidian-exporter.ts`

Existing notes are skipped by default, whereas indexes are written on each export. Database withdrawal does not remove old notes or obsolete index files in this exporter. Category ZIP fetches current remote media and contains a manifest; all-bookmark ZIP instead wraps the selected-field JSON. Exporting a URL is not retaining its bytes, and even ZIP media downloads can fail. Persistence and reading of downloaded response files are caller-owned; external Obsidian reading is afforded but unobserved (SRC-1, `lib/exporter.ts`, `lib/obsidian-exporter.ts`).

### Routes

#### MEM-RTE-image-analysis
Label: Image-only analysis

This HTTP caller → handler → analyzeBatch → analyzeItem → MediaItem write path is distinct from the combined [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) route, although it shares [MEM-OBJ-image-tags](#mem-obj-image-tags). Code selects untagged photo/gif rows, default batch 20 with upper bound 50; it does not select videos here. Model proposes descriptions; parseability/cache reuse/failure marking admit them automatically. Caller can withhold invocation, not veto each generated result. No answer oracle; operating mode is requested batch processing. Recovery is later marker reset/reprocessing, not stored history rollback. Guidance is the shipped image-analysis prompt (SRC-1, `app/api/analyze/images/route.ts`, `lib/vision-analyzer.ts`).

- Immediate return: analyzed and remaining counts, or all-already-analyzed message; GET counts non-null tags, including failure markers.
- Later read-back: Retained imageTags feed later categorization/enrichment, live LIKE search, CLI detail and graph summaries; non-null markers also affect subsequent work selection.
- Delegated visibility: SDK receives fetched image bytes and analysis prompt; CLI alternative receives URL and prompt, not guaranteed image pixels.
- Selection predicate: imageTags=null and type in photo/gif, bounded requested batch.
- Invalidation or expiry: Writes persist without TTL; main pipeline force can reset `{}`. This endpoint does not refresh FTS or invalidate AI-search responses.
- Activation or effect: Metadata writes and downstream readers are wired; actual image understanding and benefit unobserved.
- Evidence limits: Counts do not establish descriptive correctness; deployment/authentication and provider outcomes not exercised.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const untagged = await prisma.mediaItem.findMany({
>     where: { imageTags: null, type: { in: ['photo', 'gif'] } },
> --- `app/api/analyze/images/route.ts`

#### MEM-RTE-browse-memory
Label: Browse retained projections

Distinct from model reranking [RT-RTE-search-content](runtime.md#rt-rte-search-content) and direct CLI/export [RT-RTE-cli-export](runtime.md#rt-rte-cli-export), GET bookmark and mindmap handlers select retained rows and format browser projections. Code owns selection and formatting; the caller supplies filters. These read-only operations perform no knowledge admission, ranking experiment or answer-oracle evaluation (SRC-1, `app/api/bookmarks/route.ts`, `app/api/mindmap/route.ts`).

- Immediate return: Paginated bookmark content/category/media links, or graph nodes and edges.
- Later read-back: Later requests reload retained content; the display projection itself is not persisted by these handlers.
- Delegated visibility: Human/browser gets the formatted response, not rawJson or full stored enrichment; category graph shows a short first-media visual summary.
- Selection predicate: List q searches text only, with source/category/media/uncategorized filters, default limit 24/max 100. Category graph chooses at most 66 memberships ordered by confidence and one media item per bookmark.
- Invalidation or expiry: Reads reflect database selection at request time; no response cache is implemented in these inspected handlers.
- Activation or effect: Display construction is wired; actual rendered understanding or subsequent user actions unobserved.
- Evidence limits: Graph truncation and list field omission prevent treating displayed summaries as full retained memory.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> visualSummary = [parsed.scene, parsed.action].filter(Boolean).join(' — ') || null
> --- `app/api/mindmap/route.ts`

#### MEM-RTE-clear-collection
Label: Clear retained collection

DELETE /api/bookmarks is a caller-requested destructive write, separate from import, model enrichment or single-category deletion. Caller decides whether to invoke; code executes a database transaction, with errors rejecting the operation. There is no model proposer, expected-answer oracle or per-row human approval. Operating mode is administrative clearing. No backup/revision-history rollback is implemented here; recovery would require separately retained input. The transaction removes memberships, media, bookmarks and categories, not ImportJob/Setting rows, FTS rows, module caches or exported files (SRC-1, `app/api/bookmarks/route.ts`, `lib/fts.ts`, `app/api/search/ai/route.ts`, `lib/obsidian-exporter.ts`). Closest supplied records concern storage [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark) and category deletion [RT-RTE-category-admission](runtime.md#rt-rte-category-admission), not this whole-collection operation.

- Immediate return: success Boolean or storage error.
- Later read-back: Direct database consumers see cleared content; cached AI-search responses can still deliver old hydrated content until expiry/eviction. Independent exported files remain outside this deletion.
- Delegated visibility: No model call; API caller receives status, not deleted data.
- Selection predicate: All rows of the four named Prisma models, without a per-bookmark filter.
- Invalidation or expiry: Database deletion is transactional; FTS/search-cache/export invalidation is not part of this handler. Default categories can later be seeded again.
- Activation or effect: Deletion and independent later consumers are source-wired; no exercised withdrawal trace supplied.
- Evidence limits: Does not establish secure erasure, remote-source deletion, exported-file removal or completeness across opaque provider state.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> prisma.bookmarkCategory.deleteMany({}),
>       prisma.mediaItem.deleteMany({}),
>       prisma.bookmark.deleteMany({}),
>       prisma.category.deleteMany({}),
> --- `app/api/bookmarks/route.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)

Working-context control is application-selected per-call framing, not demonstrated conversational compaction. Enrichment receives 500-character text, image summaries and selected entities; classification receives 400-character text, up to 20 semantic tags and ten hashtags. buildImageContext selects scene/action/style/OCR (200 characters)/15 visual tags/meme fields, excluding other successful-analysis fields. The original rows remain reachable through later database/CLI reads, but no automatic reload of omitted evidence occurs in these model calls. Only returned parsed results cross back into Siftly; host-internal contexts remain opaque (SRC-1, `lib/vision-analyzer.ts`, `lib/categorizer.ts`, `lib/image-context.ts`).

> if (parsed.style) parts.push(`Style: ${parsed.style}`)
> --- `lib/image-context.ts`

A material countercase to uniform structured image context: mapBookmarkForCategorization joins multiple image JSON strings with ` | ` before buildImageContext parses once. Multiple objects are not one JSON value; on that path the helper falls back to the first 300 raw characters rather than a structured summary of every image. Enrichment separately parses each image before joining summaries. Consequently “all image analysis reaches the classifier” is not supported (SRC-1, `lib/categorizer.ts`, `lib/vision-analyzer.ts`, `lib/image-context.ts`).

> return rawImageTags.slice(0, 300)
> --- `lib/image-context.ts`

Retained marker interactions also bound recovery: failed semantic enrichment can leave null, but successful categorization can still set enrichedAt. A later ordinary POST selects enrichedAt=null, so null semanticTags alone does not guarantee retry through the main endpoint. Explicit IDs/force can reselect it. The standalone enrichAllBookmarks helper selects semanticTags=null, but the caller search did not establish it as the normal endpoint driver. This qualifies, rather than negates, the source comment about retry on the next run (SRC-1, `app/api/categorize/route.ts`, `lib/categorizer.ts`, `lib/vision-analyzer.ts`).

#### On [RT-RTE-search-content](runtime.md#rt-rte-search-content)

The request-directed read chain is query/category → cached response or candidate selector → retained-field projection → reranking → hydration. There is no unsolicited push into an agent's context. The automatic selector acts only within this requested route: FTS up to 150 IDs plus up to 80 intent hits; fallback below twenty candidates caps the supplemented list at 150, not every merged list. Prompt projection gives text 350 characters, OCR 250, objects eight, visual tags 25, semantic tags 35, hashtags ten and mentions five. These are field/count bounds, not a global input-token budget. RawJson, full enrichmentMeta and derivation rationale are omitted (SRC-1, `app/api/search/ai/route.ts`; supplied route retains the main passages).

Delivery gives metadata relevance authority, not authority to issue tools or rewrite storage. Model scores/reasons enter response and [MEM-OBJ-search-cache](#mem-obj-search-cache), not a persisted correction of source tags. This frames a new model request rather than pruning an accumulated chat window. The database is reachable via subsequent independent queries, not by dereferencing a pointer in the model window.

#### On [RT-RTE-cli-export](runtime.md#rt-rte-cli-export)

CLI show reloads by database ID or tweetId and exposes parsed semanticTags/entities/enrichmentMeta/imageTags, but not rawJson; list/search expose a thinner projection. CLI search FTS fallback searches text/semanticTags/entities, unlike AI search's fallback which also includes imageTags. Thus even these two lexical entry points do not have identical recall surfaces. Dispatch confirms read commands only; it does not itself install an enclosing agent loop (SRC-1, `cli/siftly.ts`).

[MEM-OBJ-export-copy](#mem-obj-export-copy) describes the artifact loss and independent persistence horizons. No downstream agent or vault-consumption trace was supplied.

#### On [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)

[MEM-OBJ-category](#mem-obj-category) retains the sampling lineage and dropped supporting examples; [MEM-OBJ-bookmark-category](#mem-obj-bookmark-category) retains the distinct manual replacement semantics. Human category selection is a UI affordance, while the API's stored result does not prove that approval occurred. Rejection/deletion is a content-maintenance action, not evidence of a scored feedback loop or formulation of criticism. Retained descriptions enter the later consumer already declared in [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance).

#### On [RT-RTE-settings-change](runtime.md#rt-rte-settings-change)

Setting key/value rows are persistent symbolic configuration and sometimes credential/path content, not bookmark knowledge. Later resolver/cache reads confer configuration authority on dispatch and export location. Initial deployed values and actual operators are unknown; supplied runtime establishes allowlisted caller writes, software admission and cache invalidation, not model-authored proposals. Credential/API-key and category caches in search have independent one-/two-minute lifetimes, while result cache lasts five minutes (SRC-1, `prisma/schema.prisma`, `app/api/search/ai/route.ts`; remaining settings findings supplied by the cited route).

#### On [RT-OBJ-categorization-state](runtime.md#rt-obj-categorization-state)

Progress/status/abort flags and pending queue have process lifetime; SQLite rows have a different retention horizon. ImportJob status/counts/errorMessage in the schema are operational metadata, not a retained explanation for tags or a durable serialization of the current categorization queue. The supplied process-state evidence does not establish restart continuation at the exact interrupted step (SRC-1, `prisma/schema.prisma`, `app/api/categorize/route.ts`).

## Write side

The parts above separate acquisition, deterministic extraction, model transformation and selection metadata. The ordinary chain is imported content → rawJson/entities → vision descriptions → semantic metadata → category memberships/enrichedAt, with category descriptions entering as classification guidance. It is not strictly a single linear dependency: missing images or failed enrichment do not necessarily stop categorization. Software checks and model generation govern ordinary admission; starting the workflow is not human approval. Suggested categories offer selection before adoption, and manual assignments offer replacement, but generic API callers leave human control unresolved ([RT-RTE-import-content](runtime.md#rt-rte-import-content), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)).

Reasons have a narrower retention path than results. Vision/semantic fields retain descriptions, not the reasoning that warrants them. Category suggestion examples/confidence/counts are shown transiently but not stored with the admitted category. Search reasons persist only in response cache, with no inspected route using them to revise knowledge. Raw source retention permits some re-extraction, not reconstruction of omitted model reasoning. No inspected Siftly path compacts an execution conversation into a later behavioral manual; external CLI checkpoint forms and retained host context remain uninspected, not absent.

The implemented trace-fed changes are operational markers: failed image attempt → `{}` → skip; trivial-content rule → `[]` → skip; admitted category assignments → enrichedAt → incremental exclusion. Their provenance and later selectors are explicit above. They alter future processing without establishing content-level experience learning or improved capacity. Imported X posts can themselves describe experiences, but that does not make them traces of Siftly's operation. The bounded feedback/evaluation search did not establish a separate success/failure-to-category-policy writer. Mocked adapter tests are not an accuracy oracle. No benefit inference is drawn from repeated retention.

Maintenance includes force's partial marker reset, stop with partial retained writes, model upserts without removal, manual membership replacement, category deletion with cascade, whole-collection deletion, and FTS rebuilding. Rollback is not uniform: manual replacement can remove memberships before a later insert error; category defaults can be reseeded; caches/exports have independent horizons. Records above preserve those differences rather than calling all of them “curation.”

## Read-back

The actual later consumers are application models, direct query handlers, CLI callers and export formatting code. Database storage capability alone is not the consumer evidence: the supplied routes and direct handlers show the actual reload operations. Search, list, graph and CLI are request-directed. Pipeline selection can automatically reload newly retained tags into later batches, but runs under an explicit trigger and software predicates; no independent unsolicited delivery to an enclosing external agent was established.

At the model boundary, fixed code selects and bounds content; the model interprets natural-language material. Symbolic slugs/IDs gate admissibility and joins. Confidence controls some display/ordering and remains model/caller metadata rather than an external answer oracle. The existing [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance) and [RT-BAP-enrichment-search](runtime.md#rt-bap-enrichment-search) already declare the consequential authority paths; this report adds their retained parts and transformations, not duplicate authority records.

Separate model calls resemble isolated work frames only in the limited sense that selected inputs enter and parsed return values escape. Siftly does not own the external CLI's internal frame disposal, and no host compaction behavior is established. Retained SQLite content is reachable by another explicit query, not a live reference automatically followed from a truncated prompt. Search reasons, graph tooltips and exported tags must not be substituted for full source payloads.

## Integration issues

- **Recovery qualification:** [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) is compatible with partial retry, but “failed semantic tags retry next run” would require the selection qualification in its annotation. Null semanticTags plus non-null enrichedAt can escape the ordinary endpoint selector. Source: SRC-1, `app/api/categorize/route.ts`, `lib/categorizer.ts`, `lib/vision-analyzer.ts`. Consequence: retain separate per-stage and per-bookmark completion state rather than promise universal retry.
- **Image-context qualification:** the supplied runtime's “image-context summaries” description should retain the multi-image categorization fallback described above. Source: SRC-1, `lib/categorizer.ts`, `lib/image-context.ts`. Consequence: later classifier access is not necessarily a structured summary of all retained images; [MEM-OBJ-image-tags](#mem-obj-image-tags) remains richer than its delivered projection.
- **Withdrawal completeness:** [MEM-RTE-clear-collection](#mem-rte-clear-collection), [MEM-OBJ-bookmark-fts](#mem-obj-bookmark-fts), [MEM-OBJ-search-cache](#mem-obj-search-cache) and [MEM-OBJ-export-copy](#mem-obj-export-copy) add independent retention horizons absent from a simple database-clear account. Cached content can still be returned; stale FTS can omit content after later imports; files remain. Source: SRC-1, `app/api/bookmarks/route.ts`, `lib/fts.ts`, `app/api/search/ai/route.ts`, `lib/obsidian-exporter.ts`.
- **Record identity:** six SQLite part declarations explicitly belong to [RT-OBJ-bookmark](runtime.md#rt-obj-bookmark); that valid container need not be superseded. FTS/cache/export are distinct derived copies, not alternative names for it. The three new routes distinguish image-only writes, browser projection and whole-collection deletion from supplied routes. No possible replacement duplicate is identified after comparison; existing route/authority referents receive annotations.
- **Unresolved included alternatives:** external CLI context/checkpoint retention and exact resolved models are opaque; no conclusion about their compaction, learned parameters or actual tools is warranted. Source: supplied [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch). Alternate ingress payload completeness and deployed initial settings were not independently established here. Exported helper callers outside the bounded code search remain unspecified; those helpers establish capabilities, not extra activated routes.

## Limitations and checks

Source HEAD was rechecked as b25daa45b858f4be096b5c368671c34db4407d8e. This job used the supplied memory type, boundary/runtime types, collection contract, worker rules and shared record contract; it did not execute Siftly, its tests, providers or examples. No new source identity was introduced. Available source paths were read or searched as listed, with implementation and supplied evidence kept separate.

The countercase checks covered force versus full recomputation, category success versus semantic retry, multi-image retention versus delivered summaries, generated reliability claims versus admission checks, and deletion versus independent copies. Missing run evidence prevents claims about activation, retrieval quality, successful export or benefit. This report does not assess opaque provider training or external agent outcomes.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check passed. That establishes structural and quotation checks, not semantic acceptance or observed behavior.
