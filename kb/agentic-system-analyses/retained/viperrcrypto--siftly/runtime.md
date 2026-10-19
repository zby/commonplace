---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Siftly runtime baseline: import, model enrichment, category admission and retained-content consumption at the frozen Git revision."
run-id: AAS-2026-10-18-siftly-b81c94cf0f77-01
reviewed-boundary: b25daa45b858f4be096b5c368671c34db4407d8e
---

# Siftly runtime report

## Runtime account

### Scope, work and evidence

Siftly's consequential work is to turn imported X content into a browsable and searchable bookmark collection. The enclosing application, not a model, owns progression through extraction, vision, semantic enrichment, categorization and later retrieval. Models supply descriptions, tags, category judgments and relevance judgments. The shipped agent-facing CLI is a database consumer, not an autonomous agent scheduler. Entry points are Next.js HTTP handlers and pages plus `npm run siftly -- ...` (SRC-1, `package.json`, `app/import/page.tsx`, `app/api/categorize/route.ts`, `cli/siftly.ts`). The declared product purpose is retained in [RT-CLM-bookmark-work](#rt-clm-bookmark-work).

All findings below use SRC-1 at the boundary's revision. They are implementation or explicitly identified doctrine/design evidence. No execution evidence was supplied; authentication success, exercised model behavior, correct enrichment, retrieval quality, throughput and downstream agent benefit remain unobserved. This account extends the boundary's initial inspection with the concrete category suggestion/admission handlers, model settings branches, bookmarklet ingress and CLI bridges cited below. These are additional paths in the same registered repository, not new sources.

### One ordinary invocation, end to end

A user uploads JSON in the import page. The HTTP import handler parses it, creates an ImportJob, skips existing tweet IDs, and writes Bookmark and MediaItem rows. Its response contains counts, not enriched knowledge. The browser's categorization step then attaches to a running pipeline or POSTs a fresh one if importedCount is nonzero; direct triggers use -1. Uploading through the API alone does not cause this UI step. See [RT-RTE-import-content](#rt-rte-import-content).

> const res = await fetch('/api/categorize', {
>       method: 'POST',
>       headers: { 'Content-Type': 'application/json' },
>       body: JSON.stringify(force ? { force: true } : {}),
>     })
> --- `app/import/page.tsx`

The server responds `started` while an unawaited async task operates. Database IDs and tweet IDs have distinct roles: pipeline selection uses Bookmark.id; categorization input and output use tweetId; writes translate model-returned tweet IDs back into existing bookmarks. A process-global progress object coordinates GET polling and DELETE stop requests. The normal selector is enrichedAt=null, explicit IDs override it, and force selects all. Entity backfill precedes per-bookmark work and is not restricted by that selected ID list. Five workers process selected bookmarks; each analyzes untagged media, enriches bookmarks lacking semanticTags, then pushes IDs into a shared categorization queue drained in batches of 25. Each flush reloads retained media tags and text, builds the categorization prompt and admits model results into SQLite. The task rebuilds FTS unless stopped and finally sets progress idle. This is resumable-by-reselection work, not a durable job executor: progress and pending queues are process memory while row-level effects persist (SRC-1, `app/api/categorize/route.ts`; [RT-RTE-enrich-categorize](#rt-rte-enrich-categorize)).

> const PIPELINE_WORKERS = 5
> const CAT_BATCH_SIZE = 25
> --- `app/api/categorize/route.ts`

> const tasks = bookmarkIdsToProcess.map((id) => () => processBookmark(id))
>           try {
>             await runWithConcurrency(tasks, PIPELINE_WORKERS)
>           } finally {
>             // Always drain remaining items even if some workers threw
>             await drainCategorizeQueue(true)
>           }
> --- `app/api/categorize/route.ts`

A later search loads the retained collection, selects candidates using keywords and inferred category intent, formats bounded text/metadata context, asks a model for matches, and returns hydrated bookmark records. Search judgments do not update category assignments. A separate CLI path searches FTS/LIKE directly and emits JSON; `show` includes parsed retained enrichment. Export writes notes and category/author indexes into a configured vault. These consumers differ in model use and effects ([RT-RTE-search-content](#rt-rte-search-content), [RT-RTE-cli-export](#rt-rte-cli-export)).

### Material alternate and forcing routes

1. **Direct import and alternate ingress.** File and bookmarklet imports persist without themselves invoking the pipeline. Cookie-based live sync paginates X, writes imports and maintains a sync timestamp; its timer is process-local. The Twitter URL import optionally makes a background HTTP request to categorize when AUTO_CATEGORIZE_AFTER_IMPORT=true. That request sends Content-Type but no Basic Authorization; with configured Basic Auth it cannot be assumed to start the protected pipeline. The browser is therefore a material workflow owner, not merely presentation (SRC-1, `app/api/import/route.ts`, `app/api/import/bookmarklet/route.ts`, `lib/x-sync.ts`, `app/api/import/twitter/route.ts`, `middleware.ts`). The OAuth fetch and live-import routes are additional shipped import surfaces in the boundary; successful X access remains unobserved.
2. **SDK versus external CLI.** Categorization and semantic enrichment prefer Codex when provider=openai, otherwise Claude if available, then SDK fallback. This means a configured MiniMax provider can use Claude for these stages. Search instead uses Claude CLI only for provider=anthropic, so MiniMax search proceeds through its SDK. Vision uses SDK when a client exists; only client absence takes the URL-in-text CLI route. Failed SDK vision does not automatically switch to CLI. A provider name consequently does not identify every actual execution backend (SRC-1, `lib/categorizer.ts`, `lib/vision-analyzer.ts`, `app/api/search/ai/route.ts`; [RT-RTE-model-dispatch](#rt-rte-model-dispatch)).
3. **Failure markers, force and stop.** Failed vision writes `{}` and a later ordinary pass skips any non-null imageTags. force resets `{}` and semanticTags=`[]`, but does not clear all successful enrichment; force is not universal recomputation. URL-level cached image analysis can be copied before the guarded model call, including an existing `{}` marker. DELETE only requests cooperative stop: in-flight calls and the final categorization drain can still write. Stopping skips the final FTS rebuild. Per-item and batch exceptions are often logged while progress advances; idle/done counters do not prove every result succeeded (SRC-1, `lib/vision-analyzer.ts`, `app/api/categorize/route.ts`).
4. **Prompt constraints versus hard output checks.** Category slug filtering and confidence clamping are executable checks, but the 1–3 assignment count is requested, not enforced by the parser. Returned tweet IDs are checked for database existence, not membership in the current input batch. Search hydration rejects IDs outside the candidate map, yet its requested maximum 15, minimum score .30 and unique IDs are not enforced by the final sort/map/filter. These differences bound the output guarantees; they are not demonstrations that any model emitted a violating result (SRC-1, `lib/categorizer.ts`, `app/api/search/ai/route.ts`).

### Controls and guarantee envelope

The application has database, network and filesystem capabilities: imports write SQLite, SDKs call endpoints, vision fetches media, CLI bridges spawn executables, and Obsidian export writes files. Actual configured credentials, process filesystem permissions, CLI tool grants and deployment isolation were not supplied. HTTP Basic Auth does not guard direct local database CLI access. SDK adapters submit messages without a Siftly tool-dispatch loop; external CLIs can have their own runtime behavior, which the frozen repository does not establish. Do not transfer a presumed provider or CLI sandbox guarantee to Siftly (SRC-1, `lib/ai-client.ts`, `lib/claude-cli.ts`, `lib/codex-cli.ts`, `cli/siftly.ts`, `middleware.ts`).

| Guarantee or control | Owner, enforcement and strength | Coverage, countercase and required external contract | Status |
|---|---|---|---|
| Configured HTTP authentication | Middleware compares Basic credentials; conditional invariant | Only matched HTTP routes when both credentials are nonempty. Bookmarklet is deliberately exempt; direct CLI is outside middleware. TLS, secret provision and network exposure are deployment responsibilities. | implementation conclusion status: wired; operation conclusion status: uninspected |
| One running categorization pipeline | POST checks process-global running/stopping state; best effort | Same-process gate, not a database lock or multi-instance invariant; handler awaits occur before setting running. Host lifetime and request scheduling matter. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Stop processing | Abort flag checked at stage/item boundaries; best effort | Does not cancel a running provider call or roll back committed rows; final queue draining still runs. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Category integrity | Parser filters known slugs; writer maps database identities and transactionally upserts; invariant at those points | CLI and SDK results converge on parser, but prompt assignment limits and current-batch identity are not enforced. Requires database transaction/constraint semantics; manual writes are a different path. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Search results refer to candidates | Hydration map rejects unknown IDs; invariant at this point | Cached results bypass new candidate selection until expiry. Score/count/duplicate instructions remain model policy rather than output invariants. | implementation conclusion status: wired; operation conclusion status: uninspected |

For authentication's consequential exception, the consumer path was inspected through writes, not just the middleware branch:

> if (!username || !password) return NextResponse.next()
> --- `middleware.ts`

> if (request.nextUrl.pathname === '/api/import/bookmarklet') {
>     return NextResponse.next()
>   }
> --- `middleware.ts`

> const tweets = body.tweets ?? []
>   if (!Array.isArray(tweets) || tweets.length === 0) {
>     return NextResponse.json({ error: 'No tweets provided' }, { status: 400, headers: cors })
>   }
> --- `app/api/import/bookmarklet/route.ts`

The bookmarklet POST then checks rest_id, skips existing IDs, and calls prisma.bookmark.create. CORS response headers select permitted browser origins but the handler has no Origin rejection. A suitably shaped HTTP request thus reaches the persistence branch without Basic Auth; this is a source-reachable exception, not a penetration-test result (SRC-1, `app/api/import/bookmarklet/route.ts`).

### Admission and change boundaries

Ordinary enrichment is software/model admission: starting the pipeline is not human approval of each generated tag or category. Category suggestions instead have a UI selection step before POST; all suggestions initially selected can be deselected. The API accepts caller-supplied suggestion content, so it does not independently prove a human approved it. Persisted category descriptions become subsequent categorization guidance. Default category seeding also overwrites default names/colors/descriptions from shipped code on pipeline start. Model/provider settings are another behavior-changing write route, not a model-parameter update. These mechanisms are specified in [RT-RTE-category-admission](#rt-rte-category-admission) and [RT-RTE-settings-change](#rt-rte-settings-change).

Product and production machinery changes visible here are operator/developer actions: package scripts launch Next.js and the CLI; `start.sh` installs dependencies if needed, generates Prisma client and applies migrations or initial db-push fallback; the Docker entrypoint migrates before next start. Optional tunnel setup changes exposure. These are shell/code-defined operational changes, not model-proposed deployments. No exercised product self-modification is established by the inspected enrichment, suggestion, settings and launcher paths; that bounded statement does not infer anything about opaque external CLI internals (SRC-1, `package.json`, `start.sh`, `docker/docker-entrypoint.sh`, `scripts/setup-tunnel.sh`).

## Shared records

### Components

#### RT-CMP-anthropic
Label: Anthropic model execution

Distributed-parametric model consumed through AnthropicAIClient or external Claude CLI. Remote/CLI-owned weights are not stored in SQLite. Siftly passes model strings to SDK; Claude CLI receives haiku/sonnet/opus aliases, collapsing full identifiers. Parameter changes during operation are uninspected in provider internals; no training request occurs in the inspected adapter calls. Exact deployed weights are not pinned by this revision. Alias and configurable/proxy endpoints can resolve to a different model; CLI resolution is opaque (SRC-1, `lib/ai-client.ts`, `lib/claude-cli.ts`, `lib/claude-cli-auth.ts`, `lib/settings.ts`).

> if (fullModelName.includes('opus')) return 'opus'
>   if (fullModelName.includes('haiku')) return 'haiku'
>   return 'sonnet'
> --- `lib/claude-cli.ts`

#### RT-CMP-openai
Label: OpenAI model execution

Distributed-parametric model accessed by OpenAIAIClient or Codex CLI; weights and any provider state remain external. No parameter-update operation is implemented in the inspected requests; internal mutability is uninspected. SDK default is gpt-4.1-mini, configurable via settings and endpoint environment. Exact weights are not pinned; endpoint routing may change the resolved model. Inspected Codex callers do not pass the supported model option, so selected OpenAI settings do not establish the CLI's actual model (SRC-1, `lib/settings.ts`, `lib/ai-client.ts`, `lib/openai-auth.ts`, `lib/codex-cli.ts`, `lib/categorizer.ts`).

> const args = ['exec', '--output-last-message', outFile]
>   if (model) args.push('--model', model)
>   args.push(prompt)
> --- `lib/codex-cli.ts`

#### RT-CMP-minimax
Label: MiniMax model execution

Distributed-parametric model accessed through an OpenAI-compatible SDK, default MiniMax-M2.7. External numerical parameters are not present in the repository or database. Siftly does not update them through the inspected adapter; provider-side changes remain uninspected. The exact weights are not pinned; configurable MINIMAX_BASE_URL and mutable provider resolution can change the model behind the endpoint. This record denotes MiniMax SDK execution, not Claude calls selected by non-openai branches (SRC-1, `lib/minimax-auth.ts`, `lib/settings.ts`, `lib/ai-client.ts`).

> const baseURL = options.baseURL ?? process.env.MINIMAX_BASE_URL ?? 'https://api.minimax.io/v1'
> --- `lib/minimax-auth.ts`

### Operative objects

#### RT-OBJ-bookmark
Label: Bookmark collection runtime state

Source-native Bookmark, MediaItem, Category and BookmarkCategory rows in SQLite through Prisma. Natural-language text, model descriptions and tags are interpreted by models/humans; symbolic IDs, timestamps, confidence numbers and relational memberships control selection and joins. JSON strings are containers, not proof that their semantic contents are symbolic rules. Raw JSON and enrichment are retained beyond the request; this is a runtime container description, leaving individual memory transformations to the memory analyst. Source: SRC-1, `prisma/schema.prisma`, `lib/categorizer.ts`, `app/api/search/ai/route.ts`.

> semanticTags    String?   // JSON array of AI-generated searchable tags
>   entities        String?   // JSON: {hashtags[], urls[], mentions[], tools[], tweetType}
>   enrichedAt      DateTime? // when AI enrichment last ran — drives incremental processing
>   enrichmentMeta  String?   // JSON: {sentiment, people[], companies[]} from batch enrichment
> --- `prisma/schema.prisma`

#### RT-OBJ-categorization-state
Label: Categorization process state

Symbolic status/stage/counters/errors and abort Boolean in globalThis; pending IDs and queue-drain flags in the async task's closure. GET delivers a shallow progress snapshot; no durable queue serialization is shown in this handler. Database effects and this process state have different restart horizons (SRC-1, `app/api/categorize/route.ts`).

> // In-memory state for progress tracking across requests
> const globalState = globalThis as unknown as {
>   categorizationState: CategorizationState
>   categorizationAbort: boolean
> }
> --- `app/api/categorize/route.ts`

### Routes

#### RT-RTE-import-content
Label: Import content and initiate processing

User/browser or HTTP caller supplies JSON; parser and import handler decide admissible content and software writes rows. No expected-answer oracle is used. Operating mode is open user import, not an evaluation curriculum. Duplicates are skipped by tweetId; parse failures produce error status; row errors can leave partial imports. Human supplies the file, not approval of later AI annotations. Proposed retained additions are guided by input parsing and source normalization; persisted content includes original rawJson. Recovery is retry/reimport with duplicate skipping, not transactional rollback of the whole import (SRC-1, `app/api/import/route.ts`, `app/import/page.tsx`).

- Immediate return: Job ID and imported/skipped/parsed counts, or parse/input error.
- Later read-back: Stored rows feed pipeline, browser, search, CLI and exports on later requests.
- Delegated visibility: Import response does not delegate an agent; subsequent pipeline calls expose selected content to model providers.
- Selection predicate: Parsed file records; existing tweet IDs skipped; source resolves to like or bookmark.
- Invalidation or expiry: No import TTL; retry does not overwrite existing tweet records in this handler.
- Activation or effect: Executable write and later selection paths are wired; successful ingestion was not observed.
- Evidence limits: File-import UI and direct endpoint differ in triggering categorization; X account operation unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (existing) {
>         skippedCount++
>         continue
>       }
> --- `app/api/import/route.ts`

Alternate ingress is source-grounded by SRC-1, `app/api/import/bookmarklet/route.ts`, `app/api/import/twitter/route.ts`, `lib/x-sync.ts`: browser bookmarklet POST writes directly; scheduled sync repeatedly imports at configured intervals, capped at 50 pages per sync. Timer and syncing flag coordinate one module instance, not multiple workers. These paths do not imply per-item human review.

#### RT-RTE-enrich-categorize
Label: Enrichment and category assignment

POST principal is an HTTP caller; server code owns next steps. SQL state and progress flags are symbolic; prompts and descriptions are natural-language guidance; model components supply judgments. Vision retains parseable object text or failure marker, enrichment normalizes fields, categorization filters slugs/clamps confidence, then a transaction upserts memberships and enrichedAt. Computational admission is automatic after these checks, without an answer oracle or per-result human veto. Operating mode is open processing of selected bookmarks; force/manual reprocessing and missing enrichment trigger additional work, not scored improvement experiments. Caller can request stop; recovery is partial-state retry, not global rollback (SRC-1, `app/api/categorize/route.ts`, `lib/vision-analyzer.ts`, `lib/categorizer.ts`).

- Immediate return: POST returns started/total before async work completes; GET returns process progress; DELETE requests stopping.
- Later read-back: Retained media/semantic tags and assignments feed later categorization/search/export/CLI; enrichedAt drives subsequent selection.
- Delegated visibility: SDK receives selected text/image blocks; CLI receives composed text, including image URL on CLI vision path.
- Selection predicate: Explicit IDs, else all when force, else enrichedAt=null; media only if imageTags=null; enrichment only if semanticTags falsy. Entity backfill precedes and is broader than the ID list.
- Invalidation or expiry: force clears only specified failure/empty markers; successful tags lack a version-based expiry here. Default category descriptions are reseeded.
- Activation or effect: Row writes and later prompt construction are wired; truthful content and behavioral improvement unobserved.
- Evidence limits: Progress counts include attempts and caught failures; stop is cooperative and restart loses queue state.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .filter((a) => validSlugs.has(a.category))
> --- `lib/categorizer.ts`

> where: { tweetId: { in: tweetIds } },
> --- `lib/categorizer.ts`

The writer's tweetIds come from returned results, not a retained copy of current batch IDs. This bounds its integrity guarantee. Existing assignments not returned are not deleted by writeCategoryResults. The model's confidence is normalized, not independently calibrated. No content-directed theory criticism or learned parameter update follows merely from these metadata writes.

#### RT-RTE-model-dispatch
Label: Model backend dispatch

Application code chooses external executor; availability checks and provider settings determine CLI/SDK selection. Calls to [RT-CMP-anthropic](#rt-cmp-anthropic), [RT-CMP-openai](#rt-cmp-openai) and [RT-CMP-minimax](#rt-cmp-minimax) do not grant Siftly ownership of provider runtime internals. SDK requests carry messages/model/token limit; local executable invocations use execFile argument arrays, not shell interpolation. Claude defaults maxTurns=1; Codex wrapper has no corresponding turn option. Timeouts and output capture bound the local call, not the remote runtime's entire effects. Codex can accept a nonempty final-message file even after process failure (SRC-1, `lib/ai-client.ts`, `lib/claude-cli.ts`, `lib/codex-cli.ts`, `lib/vision-analyzer.ts`, `lib/categorizer.ts`).

- Immediate return: Text-only AIResponse or CLI success/data/error wrapper; caller parses structured results.
- Later read-back: inapplicable — wrapper itself does not retain conversation for future Siftly invocations; downstream callers separately persist selected outputs.
- Delegated visibility: Current composed prompt; SDK vision sends base64 media, CLI vision sends an HTTP(S) URL in text. External runtime context/tools remain uninspected.
- Selection predicate: Stage-specific provider/availability branches; vision prefers SDK if client exists while text stages prefer CLI.
- Invalidation or expiry: Availability caches expire after one minute; settings caches after five minutes or explicit invalidation; Codex output temp file is normally removed.
- Activation or effect: External call wiring exists; actual provider resolution, CLI tool grants and image URL understanding unobserved.
- Evidence limits: No installed CLI configuration, deployed endpoint contracts or invocation traces supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const { model, maxTurns = 1, timeoutMs = 120_000 } = options
> --- `lib/claude-cli.ts`

> if (!client) {
>     return attempt === 0 ? analyzeImageViaCli(url) : ''
>   }
> --- `lib/vision-analyzer.ts`

Working-context control is code selection, not an observed conversational compaction loop: categorization truncates text to 400 characters and tags/hashtags to bounded subsets; enrichment uses 500-character text and image-context summaries; search builds a selected candidate index with 350-character text, selected OCR and tag fields. Each model call receives that frame rather than all database content. Raw records remain accessible via later queries/CLI show, but omitted context is not automatically reloaded by these calls. Only parsed outputs escape into callers; no Siftly sub-agent continuation is implemented in these wrappers (SRC-1, `lib/categorizer.ts`, `lib/vision-analyzer.ts`, `app/api/search/ai/route.ts`, `cli/siftly.ts`).

#### RT-RTE-search-content
Label: Search and model reranking

Caller query/category is interpreted by code for keyword and intent selection, then by model for relevance. Code merges keyword candidates with up to 80 intent hits; when fewer than 20 remain, recent fallback augments and caps at 150. Without fallback the merged set can exceed 150. FTS order is not explicitly restored after Prisma id-in lookup. Model decides proposed matches/reasons, hydration decides admissible IDs, and no human or expected-answer oracle scores relevance before returning. Operating mode is an open search request, not a benchmark (SRC-1, `app/api/search/ai/route.ts`, `lib/fts.ts`).

- Immediate return: Hydrated bookmarks with aiScore/aiReason and explanation, empty result, or error.
- Later read-back: Query result cache may return the same response for later equivalent query/category for five minutes; collection metadata is read anew on uncached selection.
- Delegated visibility: Formatted candidate index and query reach selected model; full rawJson is not part of buildIndexEntry.
- Selection predicate: Cache key is lowercased trimmed query plus category; uncached FTS/LIKE and intent/fallback rules choose candidates; hydration retains only candidate IDs.
- Invalidation or expiry: TTL five minutes, cache size limited to 100 entries; key lacks database/model revision, so changes can temporarily leave stale responses.
- Activation or effect: Model output is sorted/hydrated into returned results; response correctness and useful downstream behavior unobserved.
- Evidence limits: Prompt promises are not all runtime validations; model/proxy behavior and search quality lack run evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const b = bookmarkById.get(match.id)
>       if (!b) return null
> --- `app/api/search/ai/route.ts`

> const matchMap = new Map(aiResponse.matches.map((m) => [m.id, m]))
> --- `app/api/search/ai/route.ts`

The map does not deduplicate the subsequent iteration over aiResponse.matches. The prompt's uniqueness rule remains a request. FTS rebuild deletes then inserts in batches; the full rebuild is not one transaction. Only the categorization handler called rebuildFts in the inspected `app`/`lib` caller search. Thus direct imports and image-only analysis cannot be assumed to refresh a nonempty index immediately; FTS-empty/error fallback does not detect every stale nonempty index (SRC-1, `lib/fts.ts`, `app/api/categorize/route.ts`, `app/api/analyze/images/route.ts`).

#### RT-RTE-category-admission
Label: Suggested and manual categories

GET samples up to 100 bookmarks, preferring rows with semanticTags/entities, then uses a model to propose topic clusters. Parser derives sanitized unique-per-response slugs, length-bounds name/description and clamps confidence; example IDs are matched against samples. Browser selects proposals (initially all); POST can admit arbitrary submitted suggestions without proof of that UI step. Code rejects invalid slugs/existing name or slug and persists accepted category descriptions. No expected-answer oracle judges category quality; operating mode is user-requested collection organization. Recovery includes category deletion, not stored proposal-history rollback. Default category seeding can replace default descriptions on subsequent pipeline start (SRC-1, `lib/category-suggester.ts`, `app/api/categories/suggest/route.ts`, `app/categories/page.tsx`, `app/api/categories/[slug]/route.ts`, `lib/categorizer.ts`).

- Immediate return: GET returns suggestions; POST returns created/failed/errors, allowing partial success.
- Later read-back: Persisted category descriptions/slugs enter subsequent categorization prompts; sample metadata influences future suggestions.
- Delegated visibility: Model sees sanitized/truncated sample texts and tags; browser sees examples/counts/confidence.
- Selection predicate: At least 10 samples required; UI selected slug set chooses POST payload, while direct API callers choose it themselves.
- Invalidation or expiry: No category TTL; duplicate names/slugs rejected; deletion is available. No retained version history here.
- Activation or effect: Descriptions are wired into future prompts and slugs into assignment filtering; actual changed model decisions unobserved.
- Evidence limits: UI offers human veto, HTTP handler does not establish human approval; model confidence is not a reference answer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> description: suggestion.description.slice(0, 500),
>       color: suggestion.color,
>       isAiGenerated: true,
> --- `lib/category-suggester.ts`

Manual assignment is a separate admission mechanism: PUT bookmark categories deletes existing assignments then creates the caller's selection with confidence 1.0; it is not the model upsert-only writer (SRC-1, `app/api/bookmarks/[id]/categories/route.ts`). Browser manual selection affords human editing; generic API callers do not establish its human origin. This distinction matters for interpreting confidence and retained authorial control.

#### RT-RTE-settings-change
Label: Provider and model settings changes

HTTP caller proposes settings; code allowlists provider/model identifiers, upserts one selected branch and invalidates settings caches. Human Settings UI use is possible, but endpoint principal alone does not establish who chose the content. Guidance is shipped allowlists/defaults, not model-proposed executable capabilities. Veto is validation failure or caller withholding change; rollback is a later setting overwrite, without revision history or an outcome oracle. Operating mode is operator configuration, not an improvement experiment (SRC-1, `app/api/settings/route.ts`, `lib/settings.ts`).

- Immediate return: saved or validation/storage error; early-return branches mean a combined request does not necessarily save every field.
- Later read-back: Subsequent provider/model resolution reads retained Setting rows or cached values; external CLI model resolution differs as above.
- Delegated visibility: Future model calls use the resolved client and identifier; credentials are passed to adapters, not included in content prompts by this route.
- Selection predicate: Ordered provider, Anthropic model, OpenAI model, MiniMax model, credential and other setting branches.
- Invalidation or expiry: Explicit settings-cache invalidation plus five-minute resolver TTL; search's separate result/key caches have their own expiry.
- Activation or effect: Configuration affects future dispatch; actual backend/model changes unobserved.
- Evidence limits: Allowlisted model names do not pin weights or deployed endpoint; actual deployment settings absent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!(ALLOWED_OPENAI_MODELS as readonly string[]).includes(openaiModel)) {
>       return NextResponse.json({ error: 'Invalid OpenAI model' }, { status: 400 })
>     }
> --- `app/api/settings/route.ts`

#### RT-RTE-cli-export
Label: Direct CLI and export consumption

Local principal runs search/list/show/categories/stats; code reads the same database, and stdout returns JSON. No reranking model is called in CLI search. HTTP export callers can also write retained content into Obsidian Markdown; code validates vault placement, sanitizes subfolder, filters optional category and writes notes/indexes. Export is a derived knowledge-artifact write, not a proposed product update: caller chooses export/overwrite and software formats output without per-note approval or answer oracle. Operating mode is open consumption/export; filesystem access and actual vault use are external contracts (SRC-1, `cli/siftly.ts`, `lib/obsidian-exporter.ts`, `app/api/export/obsidian/route.ts`).

- Immediate return: CLI JSON or error; export counts/skips/errors and index count.
- Later read-back: CLI reloads retained DB on later invocations; Markdown can persist in vault, but downstream consumption was not observed.
- Delegated visibility: External caller receives JSON; CLI show includes semanticTags/entities/enrichmentMeta/imageTags. Export target receives formatted notes and indexes, not an executable agent instruction grant.
- Selection predicate: CLI query, ID/tweetId or list flags; export optional category filter.
- Invalidation or expiry: No CLI response cache here; export default skips existing notes, overwrite changes them, while indexes are written regardless of note overwrite.
- Activation or effect: Direct reads/stdout and filesystem writes are wired; no downstream agent action or Obsidian interpretation demonstrated.
- Evidence limits: Local database permissions bypass HTTP auth; configured path validation does not establish deployed OS isolation or successful export.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> semanticTags: safeParse(bookmark.semanticTags),
>     entities: safeParse(bookmark.entities),
>     enrichmentMeta: safeParse(bookmark.enrichmentMeta),
> --- `cli/siftly.ts`

> if (!overwrite) {
>       try { await fs.access(filePath); result.skipped++; continue } catch {}
>     }
> --- `lib/obsidian-exporter.ts`

### Claims

#### RT-CLM-bookmark-work
Label: Claimed bookmark knowledge-base work

Doctrine/design claim, SRC-1, `package.json`:

> "description": "Self-hosted Twitter/X bookmark manager with AI-powered categorization",
> --- `package.json`

Import, categorization and consumption wiring support the capacity; no supplied run supports accuracy or useful agent outcomes.

#### RT-CLM-category-policy
Label: Claimed categorization policy

Natural-language categorization guidance asks the model to weight retained AI metadata heavily. This is a model instruction, not an independently established truth about metadata quality (SRC-1, `lib/categorizer.ts`).

> - aiTags field is pre-computed context — trust it heavily for category signals
> --- `lib/categorizer.ts`

This establishes a behavior-shaping consumption path, not successful compliance or epistemic warrant. Category descriptions are classification guidance; this report does not equate generating category clusters with content-directed criticism of explanatory theories.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-category-guidance
Label: Category descriptions guide assignments

Consumer: buildCategorizationPrompt and the chosen model. Channel: SQLite Category.description/name inserted as AVAILABLE CATEGORIES; allSlugs also controls executable result filtering. Force: semantic guidance through model interpretation for descriptions, symbolic membership restriction for slugs. Horizon: later pipeline invocations until overwrite/deletion, including reseeding defaults. [RT-RTE-category-admission](#rt-rte-category-admission) admits custom descriptions; [RT-RTE-enrich-categorize](#rt-rte-enrich-categorize) consumes them. Delivery is wired; actual influence on emitted judgments unobserved (SRC-1, `lib/categorizer.ts`, `app/api/categorize/route.ts`).

> const categoriesList = allSlugs.map(
>     (slug) => `- ${slug}: ${categoryDescriptions[slug] ?? slug.replace(/-/g, ' ')}`,
>   ).join('\n')
> --- `lib/categorizer.ts`

#### RT-BAP-enrichment-search
Label: Enrichment guides later search

Consumer: candidate selection and reranking model. Channel: retained semanticTags/entities/imageTags through FTS/LIKE predicates and buildIndexEntry text. Force: fixed selection rules determine eligibility; natural-language metadata influences model relevance judgment. Horizon: later uncached queries until mutation/deletion or index/cache refresh. [RT-RTE-search-content](#rt-rte-search-content) identifies stale-index/cache limits. This is supplied knowledge and selection influence, not evidence that source content is authorized to issue general tool instructions (SRC-1, `lib/fts.ts`, `app/api/search/ai/route.ts`).

> if (tags.length) lines.push(`ai_tags: ${tags.slice(0, 35).join(', ')}`)
> --- `app/api/search/ai/route.ts`

## Annotations

none
