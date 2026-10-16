---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "browzy.ai memory: raw-to-wiki compilation, split search/content stores, bounded chat context and interaction-derived retention."
run-id: AAS-2026-10-15-browzy-ai-0a823a13a7b6-01
source-identity: "https://github.com/VihariKanukollu/browzy.ai"
reviewed-boundary: "56c253042041ee2f483a5e9b824174d746891cf4"
---

# browzy.ai memory report

## Boundary and evidence

This account covers the terminal application, one-shot commands and exported storage/query/compiler operations at the boundary's frozen commit. It includes source acquisition, compilation, article and access metadata, schema instructions, session history, digest and draft production, caches, maintenance, demo admission and evaluation. It excludes external service implementations, dependency internals and unspecified consuming applications as established in [boundary](boundary.md#boundary-and-evidence). No real knowledge directory, session corpus or execution trace was supplied. All new evidence is SRC-1 implementation; model instructions are doctrine/design, not observed compliance.

Direct inspection checked the executable dispatch and root exports against the provisional runtime routes. The registered commands are init, ingest, compile, query, lint, status and search; the app also owns interactive admission and background session work. No model-selected tool registration is established by these surfaces. Storage APIs with unspecified callers are capabilities, not inferred later-consumer routes. The runtime's provider analysis remains supplied evidence, not a new provider audit here (SRC-1, `src/cli/entry.tsx`, `src/index.ts`; [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider)).

### Coverage inventory

“Direct” denotes source reads in this attempt. “Supplied” denotes the handed boundary/runtime account. Uninspected material is available source, not an access gap.

| Operation or retained part | Source paths and inspection | Covering records / limit |
|---|---|---|
| CLI dispatch and library operations | Direct: `src/cli/entry.tsx`, `src/index.ts`, `src/core/wiki/wiki.ts`, `src/cli/commands/search.ts`; other command dispatches searched; supplied command tracing | [MEM-RTE-search-display](#mem-rte-search-display), [RT-RTE-library-query](runtime.md#rt-rte-library-query). Init/config details and command error handling not independently audited. |
| Raw admission, duplicates and image/PDF/text/web conversion | Direct: `src/core/ingest/index.ts`, `src/core/ingest/text.ts`, `src/core/ingest/pdf.ts`, `src/core/ingest/image.ts`, web ingest body, `src/core/retrieval/deduplicator.ts` | [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-images](#mem-obj-images), [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation). Network/private-address helpers and third-party parsing quality not audited. |
| Interactive previews, skip/guidance, bulk and topic admission | Direct: material `src/cli/app.tsx` ranges for pendingCompile and pendingDive; supplied ordinary ingest/bulk flow | [MEM-RTE-interactive-compile](#mem-rte-interactive-compile). Preview generation internals uninspected; this prevents a preview-fidelity conclusion, not tracing its admission effect. |
| Opt-in clipboard capture | Direct app polling body and text processor; clipboard helper searched | [MEM-RTE-clipboard-capture](#mem-rte-clipboard-capture). Helper filtering internals uninspected; no claim that arbitrary clipboard text is successfully retained. |
| Compilation and derived metadata | Direct complete `src/core/compile/compiler.ts`, `src/core/storage/filesystem.ts`, `src/core/storage/sqlite.ts`, `src/core/storage/migrations.ts` | [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-articles-fts](#mem-obj-articles-fts), [MEM-OBJ-wiki-index](#mem-obj-wiki-index); annotation on source compilation. |
| Request-driven retrieval, budget and history | Direct complete `src/core/retrieval/contextBuilder.ts`, token counter, query engine/history manager; ranking through scoring and selected sections | [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), [RT-RTE-library-query](runtime.md#rt-rte-library-query), annotations below. Ranking match-display helper tail uninspected; no effect on inspected assembly chain. |
| Compaction alternative | Direct complete `src/core/retrieval/compactor.ts` and its app call site | [MEM-RTE-conversation-compaction](#mem-rte-conversation-compaction). Returned summary is discarded by the app, despite its comment. |
| Session save/reload/export and digest | Direct complete `src/cli/hooks/useSession.ts`, `src/core/query/digest.ts`, app startup/digest ranges | [MEM-OBJ-sessions](#mem-obj-sessions), [MEM-OBJ-session-digest](#mem-obj-session-digest), [RT-RTE-session-digest](runtime.md#rt-rte-session-digest). Module-resolution success remains unobserved. |
| Answer-derived drafts | Direct complete `src/core/query/crystallizer.ts` and app trigger; scoped drafts search across `src/` | [MEM-OBJ-drafts](#mem-obj-drafts), [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft). No automatic draft promotion consumer established. |
| Instruction changes | Direct complete `src/core/schema.ts`; prompt-delivery evidence supplied by runtime | [RT-OBJ-browzy-schema](runtime.md#rt-obj-browzy-schema), [RT-RTE-schema-change](runtime.md#rt-rte-schema-change). Prompt compliance unobserved. |
| Answer and HTML caches | Direct complete `src/core/retrieval/queryCache.ts`, `src/core/retrieval/webCache.ts`, their query/ingest call sites | [MEM-OBJ-query-cache](#mem-obj-query-cache), [MEM-OBJ-web-cache](#mem-obj-web-cache). Process lifetime only; no persisted cache inferred. |
| Health, refresh/rebuild, deletion and migration | Direct complete linter, app command ranges, storage deletion/migration bodies | [MEM-RTE-health-review](#mem-rte-health-review), compilation annotation. Freshness selector helper only searched; exact stale-source criteria remain uninspected. Deletion APIs alone establish no coordinated withdrawal workflow. |
| Demo initialization | Direct complete `src/core/demo/seed.ts`; app call located, boundary supplies caller role | [MEM-RTE-demo-seeding](#mem-rte-demo-seeding). Bundled article claims not independently assessed. |
| Logs, saved outputs and interaction metadata | Direct complete `src/core/activityLog.ts`, query output writer, session hook | [MEM-OBJ-activity-log](#mem-obj-activity-log), query/session annotations. Profile/streak/history/autocomplete and cost-tracker internals not read; their UI personalization/feedback effects remain unresolved, not inferred knowledge learning. |
| Retrieval/security evaluators | Direct first 100 lines and scoped assertion search in `tests/e2e/retrieval-quality.test.ts`; supplied security-test inspection | [MEM-RTE-health-review](#mem-rte-health-review) distinguishes production health from tests. Fixture indexing and expected retrieval slugs are visible; remaining assertions, fixture bodies and full security coverage uninspected. No tests run, hence no measured result or production feedback link. |

## Core ideas

1. **Search state and knowledge text are separate.** SQLite chooses candidate slugs; query context then reloads Markdown files. JSON index fallback is another candidate path. Raw pre-index entries can be searchable without a corresponding wiki file, so searchability does not establish model-context delivery ([MEM-OBJ-articles-fts](#mem-obj-articles-fts), [MEM-OBJ-wiki-index](#mem-obj-wiki-index)).
2. **Admission is automatic after source initiation, but not uniform.** Short material is retained through a template; longer material undergoes model synthesis and structural parsing. Interactive “skip” is not passed as an exclusion to the compiler. Source selection, article authorship, structural admission and physical writing are different controls ([RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation), [MEM-RTE-interactive-compile](#mem-rte-interactive-compile)).
3. **Later authority depends on the actual destination.** Wiki text reaches answer prompts under a primary-truth policy; schema reaches system instructions; drafts have no established automatic read-back; session digests have a human banner route and only an incomplete direct-wiki admission route. None establishes accurate answers or improvement ([RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context), [RT-BAP-schema-instruction](runtime.md#rt-bap-schema-instruction), [MEM-OBJ-drafts](#mem-obj-drafts), [MEM-OBJ-session-digest](#mem-obj-session-digest)).
4. **Implemented compaction is not integrated compacted memory.** A summarizer returns a summary plus recent messages, but the app awaits and discards that result. Actual terminal history control is filtering and truncation, not summary replacement ([MEM-RTE-conversation-compaction](#mem-rte-conversation-compaction)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-raw
Label: raw source content and manifest

Source-native identity: data-directory `raw` Markdown/text and `_manifest.json`, with source records in SQLite `sources`. Natural-language source text is distinct from symbolic manifest fields (ID, origin, path, hash and ingestion times). The manifest controls incremental compilation; source text supplies the compiler, not direct query context. User/caller selects input; software performs conversion, persistence and metadata admission. Web HTML becomes sanitized Markdown, PDF becomes extracted text, text files are copied with metadata, and images can contribute model descriptions. Thus “raw” does not always mean original bytes or human-authored content. Initial external content provenance is not authenticated here. Sources: SRC-1, `src/core/ingest/index.ts`, `src/core/ingest/text.ts`, `src/core/ingest/pdf.ts`, `src/core/ingest/image.ts`, `src/core/ingest/web.ts`, `src/core/storage/filesystem.ts`.

Closest supplied record is [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation): this is its retained input object, not a duplicate route. Duplicate checking identifies normalized URL, path or content-hash matches but does not veto re-fetching. Re-ingest preserves a matched ID, while manifest replacement uses exact origin; normalized matches need not collapse to one origin row. Existing raw files can remain outside manifest selection. No later consumer of those orphaned files is established.

> source.id = existingSource.id;
> --- `src/core/ingest/index.ts`

> const existing = manifest.findIndex(s => s.origin === source.origin);
> --- `src/core/ingest/index.ts`

#### MEM-OBJ-images
Label: raw images and textual descriptions

Source-native identity: binary files under `raw/images`, plus description/link text in raw Markdown. These are separate operative parts: binary image encoding is not classified as model weights or a textual theory; description is natural language interpreted by compiler/answer model after article admission; image paths are symbolic references. Local image ingestion copies original bytes and optionally asks a provider to describe base64 image input. Failure retains a placeholder. Web ingestion downloads some image bytes, but the inspected compiler reads raw Markdown, not those binary payloads. Consequently readable descriptions do not establish later visual consumption. Sources: SRC-1, `src/core/ingest/image.ts`, `src/core/ingest/web.ts`, `src/core/compile/compiler.ts`. Distinct from [MEM-OBJ-raw](#mem-obj-raw) by substrate and consumers; closest supplied route is [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation).

> description = `![${title}](images/${imgFilename})\n\n## Description\n\n${sanitizeUnicode(response.content)}`;
> --- `src/core/ingest/image.ts`

#### MEM-OBJ-wiki
Label: wiki articles

Source-native identity: data-directory `wiki/<slug>.md`, read through FilesystemStorage. Article body/title/summary are natural language; source IDs, tags, backlinks, slugs and timestamps have symbolic selection/linking roles. Metadata strings can also be displayed to a model. Local filesystem is the substrate; SQLite is a separate copy used for search. Articles derive from template copies, model compilation, demo articles and attempted digest insertion. Source IDs retain a lineage pointer, not a preserved reasoning transcript or independently checked warrant. In parser output the source list is reset to the current source ID, not merged from emitted provenance. Compiler proposals therefore do not establish preservation of all old sources. Sources: SRC-1, `src/core/storage/filesystem.ts`, `src/core/compile/compiler.ts`, `src/core/demo/seed.ts`, `src/cli/app.tsx`.

Closest supplied record is [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation); this object spans other producers as well, rather than being a part of exactly that one route. Later answer authority is [RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context). Backlinks affect ranking numerically, not truth validation. No provider tool follows source IDs to fetch omitted raw evidence.

> sources: [sourceId],
> --- `src/core/compile/compiler.ts`

#### MEM-OBJ-articles-fts
Label: SQLite articles and articles_fts

Source-native identity: `.browzy/browzy.db` article rows and FTS5 virtual table. These are symbolic lexical access structures holding copies of natural-language title/summary/content and tag strings, not embeddings. `indexArticle` atomically updates article and FTS rows, but does not transact the Markdown write. Search uses quoted terms joined with OR, Porter tokenization and weighted BM25. Its metadata/snippet return goes to human search; its slugs go to Markdown reloading for answers. Sources: SRC-1, `src/core/storage/sqlite.ts`, `src/core/storage/migrations.ts`, `src/core/retrieval/contextBuilder.ts`.

Closest supplied records are [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) and [RT-RTE-answer-question](runtime.md#rt-rte-answer-question): this is the shared search object, not either route. Compilation temporarily indexes raw sources under synthetic slugs, then removes those rows regardless of success. No wiki file is written for that synthetic slug by this pre-index branch. A human search can display its snippet; the answer route requires `readArticle` to succeed. This is a counterexample to equating FTS availability with usable answer memory.

> slug: `raw-${source.id}`,
> --- `src/core/compile/compiler.ts`

> const article = this.fs.readArticle(r.slug);
>           if (article) articles.push(article);
> --- `src/core/retrieval/contextBuilder.ts`

#### MEM-OBJ-wiki-index
Label: wiki _index.json and backlinks

Source-native identity: wiki `_index.json`, concept-to-article mappings and article backlink arrays. Symbolic JSON/frontmatter on local disk carries access metadata plus natural-language titles/summaries. Compiler rebuilds index from listed Markdown, groups tags as concepts, and updates backlinks from literal wikilinks. This is index/link derivation, not model-authored concept articles: `extractConcepts` returns slug proposals from the pre-pass existing article list, while `updateIndex` uses tags. Closest supplied record: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation); distinct retained metadata object. Sources: SRC-1, `src/core/compile/compiler.ts`, `src/core/storage/filesystem.ts`, `src/core/retrieval/contextBuilder.ts`.

Index entries supplement fewer than five loadable FTS results, up to 20 candidates, then reload the associated files. It is not full reindexing of SQLite. Backlink maintenance only writes when a backlink set exists; no branch clears a stale array when all incoming links disappear. Thus removal of links need not remove their ranking-authority signal. This is bounded to this implementation, not a claim about external editors.

> const backlinks = linkMap.get(article.slug);
>       if (backlinks) {
> --- `src/core/compile/compiler.ts`

#### MEM-OBJ-sessions
Label: saved sessions and last-session metadata

Source-native identity: `~/.browzy/sessions/<id>.json` and `last-session-meta.json`, separate from configured dataDir. JSON stores symbolic roles/IDs/timestamps/source-slug lists and raw natural-language messages, including system notices. Human user messages, generated assistant answers and host notices are mixed-origin traces, not derived knowledge. Hook state starts empty; saved-session loading serves digest generation, not automatic full-chat restoration. Saved metadata supplies last-session identity, counts and digest path for startup display and eligibility. Source: SRC-1, `src/cli/hooks/useSession.ts`, `src/cli/app.tsx`; closest supplied records [RT-RTE-answer-question](runtime.md#rt-rte-answer-question) and [RT-RTE-session-digest](runtime.md#rt-rte-session-digest), distinct raw-input object.

Saving is host-initiated, not per-message human approval. JSON is directly written and pruned to 50 sessions by mtime; export separately writes Markdown, redacting patterns in assistant/system text but not user text. No exported-file automatic reload route is established. The global session root is not keyed by knowledge directory, so no per-KB provenance isolation follows from these paths.

> const SESSIONS_DIR = join(homedir(), '.browzy', 'sessions');
> --- `src/cli/hooks/useSession.ts`

> const [messages, setMessages] = useState<MessageData[]>([]);
> --- `src/cli/hooks/useSession.ts`

#### MEM-OBJ-session-digest
Label: session digest text and attempted wiki article

Source-native identity: `<session-id>-digest.txt`, metadata digestPath and optional daily `wiki/session-<date>.md`. Natural-language summary on disk derives from saved conversation: user messages remain full, assistant text is cut to 200 characters and system messages are omitted. Symbolic metadata points startup display to the file. The model returns a short digest; host admits it without a human review gate, writes the file/meta and attempts a wiki article. No separate criticism, causal explanation or model rationale is retained by this function. Sources: SRC-1, `src/core/query/digest.ts`, `src/cli/app.tsx`; distinct output object of [RT-RTE-session-digest](runtime.md#rt-rte-session-digest).

Human banner display is the wired intended later consumer, qualified by caught dynamic-require failures. The optional wiki writer omits SQLite/index updates and normal created/updated/backlinks fields. A subsequent compiler pass can rebuild the JSON index, but linter/backlink code also assumes fields that this writer omits. Therefore do not generalize this into a complete automatic query-admission loop. Daily slug reuse may replace a prior digest article. Session JSON pruning does not prune digest text in the inspected hook.

> fs.writeArticle(`session-${date}`, {
>                 title: `Session Digest — ${date}`,
>                 tags: ['session-digest'],
>                 summary: digestText.slice(0, 120),
>                 sources: [],
>               }, digestText);
> --- `src/cli/app.tsx`

#### MEM-OBJ-drafts
Label: crystallizer drafts

Source-native identity: data-directory `drafts/<slug>.md`. Natural-language derived insight plus symbolic derived flag, source slugs, date and truncated originating question; retained on local disk. Model authors the proposed insight and makes a novelty judgment from truncated answer/source contents; software checks structure/body length and writes automatically. Reasons for acceptance/rejection and full source evidence are not separately persisted. The fixed tags describe origin, not epistemic validation. Closest supplied route is [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft), whose quote establishes the destination. Sources: SRC-1, `src/core/query/crystallizer.ts`, `src/cli/app.tsx`.

This object differs from wiki by admission destination and established consumers. The scoped `drafts` search across `src/` located the writer, not an automatic promotion/retrieval consumer. The file is human-readable, but unspecified manual editing is not a wired route. No later behavior-shaping trace update can be attributed solely to this draft write.

#### MEM-OBJ-query-cache
Label: process-local queryCache

Source-native identity: singleton Map in queryCache; volatile process memory, with symbolic hashed keys, timestamp/generation/LRU controls and a stored QueryResult containing natural-language answer and symbolic source/coverage metadata. Automatic cache admission follows library query inference; later identical-key non-follow-up queries directly return the old result. TTL is 30 minutes and capacity 50 entries. Ingest increments generation. Neither compile nor schema edit invalidation is established at their inspected call sites. No dataDir/schema/history component appears in its key. Sources: SRC-1, `src/core/retrieval/queryCache.ts`, `src/core/query/engine.ts`, `src/core/ingest/index.ts`; closest supplied record [RT-RTE-library-query](runtime.md#rt-rte-library-query), distinct retained result object.

The consumer receives an answer rather than wiki evidence; no new model invocation occurs on a hit. Output saving occurs after cache insertion and mutates the same result object. A hit precedes save handling, so a later request for saving can return without producing a new file. Saved outputs under `output/` are natural-language Markdown or formatted JSON; no automatic reinjection is wired in QueryEngine.

> .update(`${query}\0${format}\0${model}`)
> --- `src/core/retrieval/queryCache.ts`

#### MEM-OBJ-web-cache
Label: process-local webCache

Source-native identity: URL-keyed Map of HTML, fetchedAt and byte count. Volatile local process memory; HTML source text is retained under symbolic URL/time/size selection. Automatic software admission follows a successful fetch; later ingest of the exact URL within 15 minutes reuses HTML before cleaning/conversion. Size cap is 50 MB; set evicts oldest insertion entries. Despite the LRU label, get does not promote entries. This is source-acquisition reuse, not answer/context memory itself. Sources: SRC-1, `src/core/retrieval/webCache.ts`, `src/core/ingest/web.ts`; no supplied object counterpart; related [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation).

> const cachedHtml = webCache.get(url);
> --- `src/core/ingest/web.ts`

#### MEM-OBJ-activity-log
Label: log.md activity records

Source-native identity: data-directory `log.md` and rotated timestamped files. Local natural-language event lines with symbolic tags/counts; software authors records of ingest, compile, query and health operations. It retains truncated question/source context or aggregate counts, not full criticism or a corrective theory. `/log` reads recent lines into system-role display messages; history filtering excludes them from future provider history, and digest excludes system messages. No automatic proposal/update consumer of the log is established in these inspected paths. Sources: SRC-1, `src/core/activityLog.ts`, `src/cli/app.tsx`, `src/core/query/historyManager.ts`, `src/core/query/digest.ts`. Closest supplied routes source compilation/library query produce events, but this is a distinct retained trace object.

> session.addMessage('system', log.readRecent(count));
> --- `src/cli/app.tsx`

### Routes

#### MEM-RTE-interactive-compile
Label: Interactive source deferral and guidance
Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

This is the terminal's preview/admission branch of the supplied ingestion/compilation route, not a second general compiler. Human can enter guidance, accept defaults or type skip after raw ingestion. App code maintains pending-source/skipped state, then invokes the compiler. Model authors long-source articles, code admits parsed output; user does not approve each generated article. Open source admission, not experiment; no answer oracle. Guidance may shape long-source synthesis but not short templates. Recovery is later compilation, not rollback. Sources: SRC-1, `src/cli/app.tsx`, `src/core/compile/compiler.ts`.

- Immediate return: system display says deferred, guidance noted, all deferred, or compilation results.
- Later read-back: raw sources stay in the manifest; compiler selects new sources from that entire manifest, and accepted articles enter normal wiki read-back.
- Delegated visibility: model receives per-source guidance where provided and the bounded compiler inputs in the parent route; skip state is not delivered.
- Selection predicate: toCompile filters pending sources for display/control; if nonempty, compile is called with batchSize, extractConcepts, guidance and progress, not a source allowlist or skipped-ID exclusion.
- Invalidation or expiry: pending state clears after review; skipping all postpones this call but leaves raw admission intact; future rebuild can select them. Skipping only some does not enforce exclusion.
- Activation or effect: source-level deferral intent is not a per-source veto at the compiler; generated articles can be admitted without further review.
- Evidence limits: branch wiring only; no observed skipped-source compilation or measured user impact.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const toCompile = pendingCompile.sources.filter(s => !pendingCompile.skipped.has(s.id));
> --- `src/cli/app.tsx`

> const result = await compiler.compile({
>             batchSize: config.compile.batchSize,
>             extractConcepts: config.compile.extractConcepts,
>             guidance,
>             onProgress: (cur, tot, title) => setLoadingLabel(`Compiling (${cur}/${tot}): ${title.slice(0, 40)}...`),
>           });
> --- `src/cli/app.tsx`

#### MEM-RTE-clipboard-capture
Label: Opt-in clipboard capture attempt
Part of: [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

This alternative acquisition branch belongs to the supplied source-admission route. User enables clipboard watching globally, not per captured content. App polls every five seconds, checks a helper-returned string and sensitive-pattern guard, then invokes ingest as text. Software proposes/adopts the raw-input attempt without content-by-content confirmation; no model oracle, experiment or article approval. Processor rejects nonexistent paths. Sources: SRC-1, `src/cli/app.tsx`, `src/core/ingest/index.ts`, `src/core/ingest/text.ts`.

- Immediate return: captured status on success; errors swallowed.
- Later read-back: conditional on successful text ingestion, normal manifest/compiler routes apply; arbitrary clipboard strings are not directly written as raw text by this call.
- Delegated visibility: inapplicable — the inspected text processor makes no model call.
- Selection predicate: watcher enabled, changed eligible content, provider present and single-line sensitive-pattern test passed; exact helper content filtering remains uninspected.
- Invalidation or expiry: interval disposed on effect cleanup; file-not-found rejection leaves no admitted source from that attempt.
- Activation or effect: `newContent` is passed as a file path to ingestText, which requires a file to exist. General clipboard-text capture is not established; a string naming an existing file is a different case.
- Evidence limits: direct call/processor mismatch, not an observed failure rate; helper internals and OS clipboard behavior uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await ingest(newContent, config.dataDir, { llm: llmRef.current, type: 'text' });
> --- `src/cli/app.tsx`

> if (!existsSync(filePath)) {
>     throw new Error(`File not found: ${filePath}`);
>   }
> --- `src/core/ingest/text.ts`

#### MEM-RTE-conversation-compaction
Label: Conversation compaction result handling

App after answering, when session.messages exceeds 20, calls compactConversation with keepRecentCount 6. Code selects older messages; model summarizes them according to topic/findings/corrections/pending-thread guidance; helper returns a synthetic system summary plus six recent messages. It retries up to three times and returns original messages on failure. This is a distinct transformation from [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), which actually uses buildLLMHistory. Open-session maintenance, no reference-answer oracle or human admission of summary. Sources: SRC-1, `src/core/retrieval/compactor.ts`, `src/cli/app.tsx`, `src/core/query/historyManager.ts`.

- Immediate return: helper returns summary and keptMessages; app awaits without assigning or persisting them.
- Later read-back: uninspected — no later summary consumer is wired in this app call; future questions still build history from unchanged session.messages. Exported internal helper capability does not supply an external consumer.
- Delegated visibility: summarizer receives older messages including system notices, each cut at 3,000 characters; output budget 4,096 tokens. This is a separate inference request, not a tool-using delegated agent.
- Selection predicate: app length threshold, not calculateBudget.needsCompaction; helper splits by recent-count and returns unchanged input if insufficient length.
- Invalidation or expiry: app discards derived summary immediately; raw displayed/session messages remain. Failure returns original messages after bounded retry/backoff.
- Activation or effect: summarization request is wired, replacement context is not integrated. No retained compacted memory or restored correction guidance follows from this caller.
- Evidence limits: source code contradicts the nearby claim that the result is used internally; model summary fidelity and service execution are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> await compactConversation(
>             session.messages.map(m => ({ role: m.role, content: m.content })),
>             currentLlm,
>             6,
>           );
> --- `src/cli/app.tsx`

> { role: 'system', content: `[Previous conversation summary]\n\n${summary}` },
> --- `src/core/retrieval/compactor.ts`

Even passing that synthetic message unchanged into buildLLMHistory would filter its system role out. That is a counterexample to assuming a future integration could simply substitute keptMessages at the existing history call. The app currently does neither substitution nor persistence (SRC-1, `src/core/query/historyManager.ts`).

#### MEM-RTE-health-review
Label: Wiki health review and retained feedback

CLI lint or terminal /health → WikiLinter loads all Markdown → broken-link/orphan/missing-field checks plus model consistency review → issue list/display and terminal aggregate log. Code owns checks/validation, model proposes consistency issues; user can act separately, but this route admits no article edits. Mode is open diagnostic request, no expected-answer oracle; model judgment is not ground truth. Closest supplied route is [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation), a different writer; health is not a compilation gate. Sources: SRC-1, `src/core/lint/linter.ts`, `src/cli/app.tsx`, `src/cli/commands/lint.ts` (command registration searched; full body not independently read).

- Immediate return: issue records with severity/article/message/suggestion; terminal displays messages and reward counts.
- Later read-back: terminal aggregate counts enter log.md; issue messages enter saved session as system notices, excluded from inspected digest/history inputs. No automatic correction/adoption consumer is established by these bodies.
- Delegated visibility: model sees slug/title/summary list, not article bodies; output max 2,048 tokens. Structural checks inspect body links and frontmatter directly.
- Selection predicate: all listed wiki files; model check requires at least two articles. JSON-array parsing validates severity/article/message types and permitted severity values; malformed model output returns no issues.
- Invalidation or expiry: diagnostics recomputed on invocation; log rotation retains counts in older files, not an active revision queue. No rollback applicable because this route does not edit articles.
- Activation or effect: human-visible review/aggregate retention; no implemented semantic repair or knowledge withdrawal here.
- Evidence limits: summary-only review cannot substantiate body-level contradiction detection. Missing backlinks arrays, including optional digest output, can fail orphan checking; no execution supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .map(a => `- ${a.slug}: ${a.frontmatter.title} — ${a.frontmatter.summary || '(no summary)'}`)
> --- `src/core/lint/linter.ts`

> .filter(a => !linked.has(a.slug) && a.frontmatter.backlinks.length === 0)
> --- `src/core/lint/linter.ts`

The shipped retrieval tests instead index ten fixture articles and compare returned slugs against explicit expected slugs; these are developer-supplied retrieval expectations, not production answer oracles or a feedback-fed article updater. Source only, tests not executed (SRC-1, `tests/e2e/retrieval-quality.test.ts`).

> expect(results.some(r => r.slug === 'attention-mechanism')).toBe(true);
> --- `tests/e2e/retrieval-quality.test.ts`

#### MEM-RTE-search-display
Label: Retained content search display

User CLI search or app /search → Wiki.search → SQLite.search → result snippets displayed to user. Code selects and formats; no model call or new knowledge admission. Distinct from [RT-RTE-answer-question](runtime.md#rt-rte-answer-question): it consumes the SQLite copy directly rather than requiring Markdown reloading. Sources: SRC-1, `src/cli/commands/search.ts`, `src/core/wiki/wiki.ts`, `src/core/storage/sqlite.ts`; app search call located by source search.

- Immediate return: slug, title, BM25-derived score and snippet, not full article context.
- Later read-back: request-driven search exposes previously retained article-copy text, including temporary raw rows if still present. Wiki.getArticle/listArticles/getIndex are additional exported storage reads, with unspecified external callers rather than inferred automatic routes.
- Delegated visibility: inapplicable — human display path, no inference delegation.
- Selection predicate: sanitized OR query with FTS ranking; one-shot limit clamped 1–100, default 10; symbolic slug is return metadata, not an independently targeted user file choice.
- Invalidation or expiry: underlying row removal/reindex affects search; absence of coordinated Markdown/index deletion can leave stores divergent.
- Activation or effect: delivers snippets to human interpretation; changed beliefs/actions unobserved.
- Evidence limits: no search run supplied; source demonstrates route and selection, not relevant-result quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const results = wiki.search(query, clampInt(opts.limit, 1, 100, 10));
> --- `src/cli/commands/search.ts`

#### MEM-RTE-demo-seeding
Label: Demo knowledge seeding

App initialization calls seedDemoKB → absent marker and available bundled articles → SQLite indexing → Markdown/index writes → marker. Host software admits shipped content without per-article approval. Authorship/truth of demo articles is not determined by seeding; no model synthesis, answer oracle or experiment in this path. This is a distinct initialization producer from [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation), sharing its downstream wiki/search stores. Sources: SRC-1, `src/core/demo/seed.ts`, `src/cli/app.tsx`.

- Immediate return: Boolean seeded/skipped; app can display demo welcome state.
- Later read-back: normal search and article-reload consumers use seeded entries, not a demo-only memory format.
- Delegated visibility: inapplicable — seeding makes no provider request.
- Selection predicate: marker absence and bundle availability, not absence of existing wiki articles despite function documentation. Existing same-slug files/index can be overwritten when marker is absent.
- Invalidation or expiry: marker suppresses future seeding; per-row SQLite atomicity is not an all-files transaction. No coordinated rollback is implemented across seeding stages.
- Activation or effect: wired admission to wiki/SQLite/index, not evidence users queried them or benefited.
- Evidence limits: bundled bodies not independently reviewed; shipping examples does not validate system quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (existsSync(markerFile)) return false;
> --- `src/core/demo/seed.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation)

Storage/lineage: [MEM-OBJ-raw](#mem-obj-raw) → template or model-produced [MEM-OBJ-wiki](#mem-obj-wiki) plus separate [MEM-OBJ-articles-fts](#mem-obj-articles-fts) and [MEM-OBJ-wiki-index](#mem-obj-wiki-index). Sources, generated content, index metadata and concept-slug proposals are not interchangeable products. User workflow initiation is not per-article approval. Short-source branch copies content, bypassing model curation/schema/guidance; long branch sends 15,000 characters and up to 30 old slug/title entries. Parser requires slug/title but can accept an empty body; it does not preserve emitted full provenance or model reasoning. Collision renaming and represented-ID selection limit revision, as the supplied route already notes. Direct recheck: SRC-1, `src/core/compile/compiler.ts`.

Read-back/authority: compiler first reads the entire existing corpus for membership/title inventory; query later reloads selected bodies under the wiki-primary-truth prompt. A malformed model article can be dropped while other sources proceed. All raw synthetic rows are cleaned after each chunk, including failed source processing. That cleanup withdraws temporary search exposure, not the raw manifest input, so future retry remains possible if no article source ID represents it. Writes are not a corpus-wide transaction or version history. Human editing via exported writeArticle/deleteArticle remains an afforded storage capability with no unspecified caller inferred.

#### On [RT-RTE-answer-question](runtime.md#rt-rte-answer-question)

Read-back selection: FTS top 20 then sparse-result JSON-index supplementation; candidate files reloaded, excluded slugs filtered, ranking up to 15, then budget assembly. Ranking uses lexical content/title/tag matches, up to five points of recency and backlink count, not an evidence-quality oracle. Raw SQL content is not directly delivered in article context. Direct recheck: SRC-1, `src/core/retrieval/contextBuilder.ts`, `src/core/retrieval/relevanceRanker.ts`, `src/core/query/engine.ts`.

The advertised relevant-section branch has a consequential code condition: `allSections` is assigned matchedSections whenever matchedSections is nonempty, so the ensuing less-than comparison cannot select that branch. Small articles therefore normally retain full bodies rather than only matched sections; oversized articles do enter the separate section-budget branch. That branch always admits the intro even if it alone exceeds 8,000 estimated tokens. Total assembly permits two articles before enforcing the overall budget. These qualify delivery completeness and budget safety, not proof of model-window failure (SRC-1, `src/core/retrieval/contextBuilder.ts`).

> const allSections = scored.matchedSections.length > 0 ? scored.matchedSections : extractSections(article.content);
>       if (scored.matchedSections.length > 0 && scored.matchedSections.length < allSections.length) {
> --- `src/core/retrieval/contextBuilder.ts`

Working context: buildLLMHistory filters system messages, takes at most ten user/assistant messages and processes newest first. Default older cap 1,000 characters, last-two cap 2,000 each, aggregate target 4,000 with at least two retained. It removes old text by value, not by a reloadable reference. Raw session state remains available to host saving/export/digest, but omitted text is not reloadable by an answer-model tool. Model-side weights stay outside inspection as in [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider). This is context eviction rather than an isolated sub-agent frame. New compaction findings are in [MEM-RTE-conversation-compaction](#mem-rte-conversation-compaction), not evidence of retained summaries.

> const relevant = messages.filter(
>     (m): m is HistoryMessage & { role: 'user' | 'assistant' } =>
>       m.role === 'user' || m.role === 'assistant'
>   );
> --- `src/core/query/historyManager.ts`

#### On [RT-RTE-library-query](runtime.md#rt-rte-library-query)

Memory consumers: same article selection as terminal on misses; [MEM-OBJ-query-cache](#mem-obj-query-cache) can instead return prior answer without schema reload/retrieval. QueryEngine options.conversationHistory affects estimated article budget but not provider message delivery in query. Per-instance usedSlugs supports request-driven follow-up exclusion, not targeted novelty evaluation or automatic unsolicited recall. Reset clears exclusions. Optional output files have no established reinjection. Direct recheck: SRC-1, `src/core/query/engine.ts`, `src/core/retrieval/queryCache.ts`, `src/core/retrieval/tokenCounter.ts`.

Budget is estimated through model-name-prefix windows and heuristic text counts. QueryEngine defaults to a Claude-family budget unless passed a model option; terminal prepare passes only format and app later appends history. Thus the articleBudget is not a bound on actual total input. Changing a model can change effective window without changing the source's prefix table; no real tokenizer/provider measurements are supplied.

#### On [RT-RTE-session-digest](runtime.md#rt-rte-session-digest)

Raw-to-derived lineage and storage are [MEM-OBJ-sessions](#mem-obj-sessions) → [MEM-OBJ-session-digest](#mem-obj-session-digest). Trigger is startup/provider availability and missing digest with matching saved session and at least three user messages, not a quality failure. Automatic selector supplies all non-system turns, user text full and assistant text cut to 200 characters; model output max 200 tokens. The retained summary may express insights/pending work but does not separately preserve reasons for what was omitted or validate them. Startup banner is a human-consumption channel; no direct automatic summary-to-answer history route is wired. Optional wiki article requires additional discovery/indexing to reach ordinary retrieval. Global session location also permits different configured data directories to share the same last-session source; no KB identity guard is present in this selection. Direct recheck: SRC-1, `src/cli/hooks/useSession.ts`, `src/core/query/digest.ts`, `src/cli/app.tsx`.

#### On [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft)

Automatic trace-fed write consumes mixed user question/model answer/wiki article content. Model novelty judgment against only five 2,000-character article prefixes plus 3,000 answer characters is not independent corpus-wide validation. Structural gates, body minimum and session-success suppression are code rules. The result is [MEM-OBJ-drafts](#mem-obj-drafts), not an adopted rule or directly indexed wiki article. Reasons for model novelty judgment are not separately retained/read later. A model rejection produces no durable rejection record here. Direct recheck: SRC-1, `src/core/query/crystallizer.ts`, `src/cli/app.tsx`.

#### On [RT-OBJ-browzy-schema](runtime.md#rt-obj-browzy-schema)

Storage is local Markdown; natural-language preferences have later system-instruction authority through [RT-BAP-schema-instruction](runtime.md#rt-bap-schema-instruction). Write agency is human editing or software default/reset; neither changes model parameters. ReadSchema uses non-comment content only as an eligibility test, then returns a prefix of the original whole file, including comments. Owner instructions are not inferred from a comment-only default. Compiler reads once per pass, query on cache miss/prepare; cache hits and short templates bypass fresh schema consumption. This is static/user-edited instruction retention, not trace-fed self-revision. Direct recheck: SRC-1, `src/core/schema.ts`, `src/core/query/engine.ts`, `src/core/compile/compiler.ts`; instruction-delivery quotes supplied by runtime.

## Write side

Acquisition retains transformed source material and symbolic lineage, with separate binary images. Human source choice is the ordinary initiation mechanism, while topic diving lets the host search and admit up to three found URLs after topic confirmation, not per-URL human approval. Clipboard capture is a distinct opt-in attempt with an input-type mismatch. These distinctions prevent attributing one uniform human/software admission policy ([MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-images](#mem-obj-images), [MEM-RTE-clipboard-capture](#mem-rte-clipboard-capture); SRC-1, `src/cli/app.tsx`).

Compilation curation ranges from template copying to instructed model synthesis. Structural parsing admits articles, not their truth, preservation, contradiction resolution or safety. Guidance and schema shape long-source proposals but are not admission vetoes. Partial skip state does not constrain compiler source selection. The source-ID membership predicate can suppress updates after re-ingest; `/refresh` and `/rebuild` reuse it. Collision handling favors renamed proposals rather than assured replacement. These are implemented revision limits, not merely missing execution evidence ([RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation), [MEM-RTE-interactive-compile](#mem-rte-interactive-compile)).

Metadata maintenance includes FTS/row transactions, JSON-index rebuilding, conditional backlink updates and schema migrations. Migration version 2 recreates FTS with Porter tokenization from stored article rows; it backs up the main DB path before migration. The code provides transaction failure reporting but no automatic restore route or evidence that the copied file is a complete live-WAL backup. Markdown, JSON index and DB do not share one atomic admission/rollback boundary. Backlink removal is incomplete at the empty-set case. Exported deleteArticle unlinks only Markdown; removeArticle deletes only SQL rows. Neither alone coordinates index/backlink/cache withdrawal, and no combined withdrawal caller was established in the inspected entry/search paths (SRC-1, `src/core/storage/migrations.ts`, `src/core/storage/sqlite.ts`, `src/core/storage/filesystem.ts`, `src/core/compile/compiler.ts`; [MEM-OBJ-wiki-index](#mem-obj-wiki-index)).

Health review yields displayable issues and retained counts, not automatic accepted corrections. Developer retrieval tests use expected fixture slugs, but no production admission depends on those tests in this inspected loop. Demo seeding is an independent software-admitted producer and can replace same-slug content when its marker is absent ([MEM-RTE-health-review](#mem-rte-health-review), [MEM-RTE-demo-seeding](#mem-rte-demo-seeding)).

Trace-fed retention has three distinct results: raw session JSON, a model digest with banner/optional-wiki destination, and answer-derived drafts. Only the digest has a wired later human-display selection; draft-to-answer consumption is not established. Compaction supplies a fourth derived form but the app discards it. Retained summaries/articles do not contain a separately preserved chain of model criticism/reasons, although their prose can include explanatory content. These facts establish trace processing and retention capacity, not improved capacity, reflection, autonomous theory building or exercised self-improvement ([MEM-OBJ-sessions](#mem-obj-sessions), [MEM-OBJ-session-digest](#mem-obj-session-digest), [MEM-OBJ-drafts](#mem-obj-drafts), [MEM-RTE-conversation-compaction](#mem-rte-conversation-compaction)).

## Read-back

Request-driven knowledge read-back is question → lexical candidate search → file reload → code ranking/exclusion → budgeted article blocks → answer model. The actual authority is natural-language knowledge under the supplied primary-truth policy, not executable control or validated truth. Source IDs/tags are serialized metadata, not full original evidence. The human search route consumes SQLite snippets directly. Caches are separate directions of reuse: requested identical answers bypass synthesis, requested URLs reuse HTML for ingestion ([RT-BAP-wiki-context](runtime.md#rt-bap-wiki-context), [MEM-RTE-search-display](#mem-rte-search-display), [MEM-OBJ-query-cache](#mem-obj-query-cache), [MEM-OBJ-web-cache](#mem-obj-web-cache)).

Automatic supply has a narrower scope than automatic retrieval of everything retained. The terminal automatically adds selected recent user/assistant turns when a new question is asked. Startup automatically selects latest-session metadata/digest for human display and may launch digest generation. Compiler reads raw sources and existing article metadata when compilation is requested. Crystallizer automatically selects answer-used source prefixes after qualifying answers, but persists only a proposal. Schema is reloaded for applicable prompt assembly. No route here independently pushes drafts or old full sessions into the answer model ([RT-RTE-answer-question](runtime.md#rt-rte-answer-question), [RT-RTE-session-digest](runtime.md#rt-rte-session-digest), [RT-RTE-insight-draft](runtime.md#rt-rte-insight-draft), [RT-RTE-schema-change](runtime.md#rt-rte-schema-change)).

Working-context control removes old/system turns and truncates messages; article selection removes irrelevant/unaffordable material by code policy. Files remain available to host retrieval, not reachable through pointer-following by the provider. Compaction's separate inference request returns a summary but crosses no retained summary back into future answering. This resembles a bounded helper computation, not a delegated-agent stack frame whose summary is adopted. Neither a stored slug nor a source list grants model tool access. Context budgets and displayed confidence describe estimates/coverage, not answer correctness or activated benefit.

## Integration issues

1. **Compaction integration correction/extension.** The source comment claims future-context use, but the returned summary is discarded. Runtime already describes history trimming rather than retained summaries; its compaction coverage should explicitly retain this missing consumer and distinguish helper capacity from integrated replacement. Evidence and consequence: [MEM-RTE-conversation-compaction](#mem-rte-conversation-compaction), [RT-RTE-answer-question](runtime.md#rt-rte-answer-question); SRC-1, `src/cli/app.tsx`, `src/core/retrieval/compactor.ts`. Do not count this as a retained compacted-memory route.
2. **Interactive veto qualification.** Source preview offers skip, but only all-skipped avoids this invocation; partial skip is not passed to the compiler. Extend [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) with the branch [MEM-RTE-interactive-compile](#mem-rte-interactive-compile). This affects attribution of human admission control, not the known general parser/writer route (SRC-1, `src/cli/app.tsx`, `src/core/compile/compiler.ts`).
3. **Clipboard capture correction to broad boundary wording.** Boundary names optional capture as a shipped responsibility, correctly, but generic successful text capture is not supported by the caller/processor pair. [MEM-RTE-clipboard-capture](#mem-rte-clipboard-capture) traces the mismatch; [RT-RTE-source-compilation](runtime.md#rt-rte-source-compilation) must not imply every input label supplies valid content. Helper filtering and actual OS behavior remain uninspected (SRC-1, `src/cli/app.tsx`, `src/core/ingest/text.ts`).
4. **Selection/budget qualification.** The nominal relevant-section branch is ineffective for nonempty matchedSections; a distinct oversized-article branch does perform selection. Add the direct source qualification in the annotation on [RT-RTE-answer-question](runtime.md#rt-rte-answer-question), without withdrawing the genuine ranking/budget controls or the runtime's already-qualified window guarantee (SRC-1, `src/core/retrieval/contextBuilder.ts`).
5. **Retained stores are not interchangeable.** [MEM-OBJ-articles-fts](#mem-obj-articles-fts), [MEM-OBJ-wiki](#mem-obj-wiki), [MEM-OBJ-wiki-index](#mem-obj-wiki-index) separate synthetic raw search exposure, live Markdown context and fallback metadata. [MEM-OBJ-session-digest](#mem-obj-session-digest) has no immediate index admission, and missing frontmatter can disrupt later linter/backlink consumers. This strengthens, rather than contradicts, the limitation in [RT-RTE-session-digest](runtime.md#rt-rte-session-digest). Successful later adoption remains unresolved (SRC-1, compiler/storage/context builder/app/linter paths cited in those records).
6. **No duplicate referents declared.** New objects are retained inputs/results/access structures of the supplied routes, not replacement route identities. Interactive and clipboard routes explicitly identify their parent. Compaction, health, search and demo seeding have distinct progression/consumers from the supplied routes. Schema/provider and the two established authority paths are annotated/cited, not redeclared. Draft and digest objects must not be superseded by each other simply because both derive from conversations.
7. **Local unknowns retained.** No supplied deployed corpus confirms digest/draft creation, schema consumption, cache coherence, source merge quality or any downstream behavior change. Global sessions are not keyed by dataDir, so cross-KB session lineage remains uncontrolled by this selector. Profile/streak/history/autocomplete/cost-tracker internals, full freshness criteria, preview fidelity and remaining evaluation assertions are available but uninspected; their contribution to personalization/feedback cannot be classified from this member. These limits do not erase known article/history/schema routes (SRC-1, paths and prevented conclusions in coverage inventory).

## Limitations and checks

The frozen checkout HEAD was rechecked as `56c253042041ee2f483a5e9b824174d746891cf4`, with clean status. Source identity matches the handed boundary and run. Only source text/search and Commonplace content validation were used; target, providers, examples and tests were not executed. Supplied runtime findings were treated as provisional, with direct counterchecks for storage/selection/admission and new distinctions recorded above. Governing job, member types, collection, worker rules and records contract were read completely. No new source identity or prior analysis was consulted.

No source passage establishes observed activation, successful persistence or answer benefit. Provider state remains opaque and no repository-owned parameter update was added to the runtime's component account. Natural-language retained content is not automatically a formulated-theory improvement loop: source admission, derived summaries and novelty judgments do not independently establish criticism-driven method revision or learning. The source register and coverage inventory delimit both inspected implementation and uninspected alternatives.

Deterministic validation: the required validate-output command passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” A pass checks structure/quotation occurrence, not semantic support or job acceptance.
