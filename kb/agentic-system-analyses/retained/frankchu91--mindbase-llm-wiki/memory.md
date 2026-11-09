---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MindBase memory: project context synthesis, source-aware question retrieval, hosted injection, chat retention and alternative cache/read paths."
run-id: AAS-2026-11-08-mindbase-llm-wiki-32a62759e2b9-01
source-identity: https://github.com/frankchu91/mindbase-llm-wiki
reviewed-boundary: c5273d2336c4d686df41c2a1495f14f085707f51
---

# MindBase memory report

## Boundary and evidence

The memory scope follows the retained-file producers and consumers in the supplied runtime, but includes alternative MCP, CLI, chat, manual-edit, synthesis-cache and embedding paths. The frozen boundary remains **complete artifact, partial loop**. SRC-1 is the repository at c5273d2336c4d686df41c2a1495f14f085707f51, not a deployed user's knowledge directory. Direct reads supply implementation evidence or, for agent instructions and prompts, doctrine/design evidence. There is no observed run or causal experiment. External host compaction, scheduling and provider internals are outside the implementation evidence; no claim of host compliance, useful knowledge or improved future capacity follows.

The table distinguishes directly inspected implementations from supplied runtime evidence and unresolved included mechanisms. Paths are SRC-1 anchors. Uninspected rows remain in the functional boundary, not silently excluded. Material captured by browser/mobile clients is not inspected user data.

| Entry or operation | Inspected paths and basis | Covering records or unresolved fact and prevented conclusion |
|---|---|---|
| Server contribute, build, research and ask auto-save | Supplied runtime: `apps/server/src/ops/runner.ts`, `apps/server/src/ops/executors.ts`, `apps/server/src/routes/ask.ts`; direct `apps/server/src/ops/gather.ts`, `apps/server/src/ops/recipes/build.ts`, `packages/core/src/qa/query.ts` | [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan), [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer); memory annotations below |
| Plugin builder, context snapshot and overflow | Direct `apps/plugin/agents/builder.md`, `apps/mcp/src/tools/gather-sources.ts`, `apps/mcp/src/tools/atomic-write-context.ts`, `apps/mcp/src/tools/load-project.ts` | [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build), [MEM-OBJ-context](#mem-obj-context) |
| Hook after startup, clear or compact | Direct `apps/plugin/hooks/hooks.json`, `apps/plugin/hooks/session-start` | [RT-BAP-session-context](runtime.md#rt-bap-session-context); reload exists, host compaction algorithm remains external |
| MCP capture, transcript retention and recall | Direct `apps/mcp/src/tools/contribute.ts`, `apps/mcp/src/tools/save-chat-excerpt.ts`, `apps/mcp/src/tools/recall-chat.ts`, `apps/server/src/routes/chats.ts` | [MEM-RTE-chat-retention](#mem-rte-chat-retention), [MEM-OBJ-sources](#mem-obj-sources) |
| MCP alternative read and answering paths | Direct `apps/mcp/src/tools/index.ts`, `apps/mcp/src/tools/search-wiki.ts`, `apps/mcp/src/tools/read-wiki-page.ts`, `apps/mcp/src/tools/semantic-search.ts`, `apps/mcp/src/tools/ask-wiki.ts`, `apps/mcp/src/tools/load-project.ts`, `apps/mcp/src/resources/index.ts` | [MEM-RTE-mcp-retrieval](#mem-rte-mcp-retrieval); registered tools do not all use core askQuestion |
| CLI dispatch and older compilation | Direct `apps/cli/src/index.ts`, `apps/cli/src/commands/ingest.ts`, `apps/cli/src/commands/query.ts`, `packages/core/src/compile/l1.ts`, `packages/core/src/compile/context.ts` | [MEM-RTE-cli-ingest](#mem-rte-cli-ingest); CLI query is index substring lookup, not a model answer |
| Search/graph and dense cache | Direct selected `apps/server/src/context.ts` reindex function, `apps/server/src/lib/embedding-indexer.ts`, `apps/server/src/lib/embedder.ts`, `packages/core/src/search/embedding-store.ts`, `packages/core/src/search/hybrid.ts` | [MEM-OBJ-access-metadata](#mem-obj-access-metadata), [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-CMP-bge-m3](#mem-cmp-bge-m3); cross-writer invalidation completeness unresolved |
| Cached synthesis and contradiction display | Direct `apps/server/src/lib/synthesis.ts`, `apps/server/src/lib/synthesis-cache.ts`, `apps/server/src/lib/synthesis-worker.ts`, `apps/server/src/routes/synthesize.ts`, `packages/core/src/synthesis/validate.ts`, `apps/mcp/src/tools/find-contradictions.ts` | [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache); MCP synthesis producer itself uninspected, so server equivalence not asserted |
| Lint diagnosis/dismissal | Supplied runtime `apps/server/src/ops/runner.ts` | [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings); no established automatic repair consumer |
| Manual edit, rename, deletion and restoration | Direct `apps/server/src/routes/tree/crud.ts`, `apps/server/src/lib/tree-paths.ts`, `apps/server/src/routes/trash.ts` | [MEM-RTE-tree-edit](#mem-rte-tree-edit); v2 unlink differs from trash-backed chat deletion |
| Other registered write, curation and review tools | Registration directly inspected in `apps/mcp/src/tools/index.ts`: ingest plan/execute, quick capture, ingest file/source, research save, append/update/tag/visibility, create note/template, SRS, health, migrate, rebuild index | Implementations not individually traced; no uniform human admission, reversibility, visibility filtering, provenance or review-to-knowledge conclusion |
| Capture/RSS/OCR, classification, brief/SRS, analysis workers; server compile/L2/file-back/schema routes | Available files enumerated under `apps/server/src/lib/`, `apps/server/src/routes/`, `packages/core/src/compile/`; startup evidence supplied by runtime | Individual transformation, admission and downstream consumption remain unresolved. Prevents complete trace-fed-learning or context-management inventory beyond the traced routes |
| Web/manual smoke evaluators, mobile/extensions and packaging | Available but not directly inspected; boundary inventory retained | No quality result, deployed approval behavior, corpus completeness or evaluator-to-revision linkage established |

## Core ideas

1. **Synthesized context is a retained document, not a transcript checkpoint.** Source/contributor files and research pages feed a rewrite of context.md, which feeds future builds and sessions. Server update_context rejects replacements over 400 lines and snapshots prior content; append_context_section checks the resulting line count without snapshotting. The same executor admits add_wikilinks targeting context.md without either check, so there is no executor-wide cap. MCP replacement separately relocates overflow. Selection by modification time is not a durable per-source synthesis ledger. See [MEM-OBJ-context](#mem-obj-context) and annotations on [RT-RTE-build-context](runtime.md#rt-rte-build-context).
2. **Delivery and trust depend on the consumer.** Core question answering labels source versus wiki material and boosts source hits. The session hook instead supplies whole selected-project files, calling context “curated truth”; that phrase does not establish truth. MCP ask has its own graph expansion and older wiki-path reads. See [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [RT-BAP-session-context](runtime.md#rt-bap-session-context), [MEM-RTE-mcp-retrieval](#mem-rte-mcp-retrieval).
3. **Content and access state are separate.** Markdown bodies carry knowledge through interpretation. Index rows, citation paths, timestamps, hashes and numeric retrieval ranks select or locate that content. Embeddings are dense representations, not readable summaries or learned provider-weight changes. See [MEM-OBJ-access-metadata](#mem-obj-access-metadata) and [MEM-OBJ-embeddings](#mem-obj-embeddings).
4. **Retention has multiple admission regimes.** Contribution checkboxes do not cover direct build/research, MCP replacement, transcript saving, caller-provided tree edits or auto-save. Cached contradiction reports can persist without revising the knowledge they criticize. No measured learning benefit follows from any of these writes. See [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes), [MEM-RTE-tree-edit](#mem-rte-tree-edit), [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache).

## Shared records

### Components

#### MEM-CMP-bge-m3
Label: BGE-M3 feature extractor

SRC-1, `apps/server/src/lib/embedder.ts`. Distributed-parametric encoder, distinct from the generative model in [RT-CMP-model](runtime.md#rt-cmp-model): it produces vectors for retrieval, not action proposals. Substrate is a lazily loaded Transformers pipeline and its externally supplied weights. No parameter-update operation appears in this wrapper; inference changes cached vectors, not those weights. Exact model revision is not pinned here: a model name without a revision does not identify immutable weights. Remote artifact resolution and provider internals remain uninspected. Local extraction takes only the first 8,000 characters and mean-pools/normalizes the result.

> extractor = (await pipeline('feature-extraction', 'Xenova/bge-m3')) as FeatureExtractionPipeline;
> --- `apps/server/src/lib/embedder.ts`

> const result = await fx(text.slice(0, 8000), { pooling: 'mean', normalize: true });
> --- `apps/server/src/lib/embedder.ts`

### Operative objects

#### MEM-OBJ-sources
Label: Contributor and raw source content

SRC-1, `apps/mcp/src/tools/contribute.ts`, `apps/server/src/ops/gather.ts`, `apps/server/src/context.ts`. Project filesystem Markdown holds contributor text and extracted raw text, distinct from the symbolic [RT-OBJ-actions](runtime.md#rt-obj-actions) envelope and from synthesized [MEM-OBJ-context](#mem-obj-context). Natural-language source bodies enter model/human interpretation; path labels and timestamps are access metadata. The MCP contribute implementation appends caller-supplied text with a daily/time/user header and optional mode marker. It does not itself invoke an LLM to select routing despite its description's “auto (LLM decides)” wording. Who originally authored arbitrary supplied text remains unresolved; a username or source type is not evidence of human provenance. Raw binaries/extraction provenance and other capture clients are not traced here.

> const entry = `\n## ${now}${tagBlock}\n\n${text.trim()}\n`;
> --- `apps/mcp/src/tools/contribute.ts`

> await appendFile(contributorFile, header + entry, 'utf-8');
> --- `apps/mcp/src/tools/contribute.ts`

Later consumers include server build, source-aware ask and lint statistics. Server build's gather selects contributors and research, not raw extraction files; source-aware indexing separately includes extracted raw text. Storage thus does not imply every synthesis path sees every source.

#### MEM-OBJ-context
Label: Context and research Markdown

SRC-1, `apps/server/src/ops/recipes/build.ts`, `apps/mcp/src/tools/atomic-write-context.ts`. These are persistent natural-language products in project context.md and sources/research/, distinct from [RT-OBJ-actions](runtime.md#rt-obj-actions). Authorship can be model synthesis under build/research/contribution recipes, saved answer text, hosted builder output or caller editing. The generative envelope's validity does not certify a body's truth. The build prompt requests dated decisions/learnings, preservation, contradiction flags and source citations for research pages. It does not require a separate retained rationale for every choice; the derived body is what later models receive, not a replay of the synthesis reasoning.

> preserve still-true
> content; flag contradictions between sources explicitly with ⚠️.
> --- `apps/server/src/ops/recipes/build.ts`

MCP overflow keeps a 395-line head and relocates the remaining lines into research with a pointer. The previous context is separately snapshotted by MCP replacement; neither snapshot nor overflow is itself proof of a later reload. Server update_context also snapshots, but append_context_section does not. Server add_wikilinks can append a See also line to context.md without a line-count check or snapshot, so these retained documents have no universal executor-enforced 400-line limit. The updated supplied [RT-RTE-build-context](runtime.md#rt-rte-build-context) documents this internal countercase (SRC-1, `apps/server/src/ops/executors.ts`, `apps/server/src/ops/types.ts`, directly read in this correction). The session hook reads current context, not old snapshots or overflow bodies. Subsequent source gathering can discover the research overflow page, and hosted Read or other explicit file reads can follow a pointer; automatic pointer following is not established.

> const head = lines.slice(0, MAX_LINES - 5);
> const overflow = lines.slice(MAX_LINES - 5);
> --- `apps/mcp/src/tools/atomic-write-context.ts`

#### MEM-OBJ-access-metadata
Label: Indexes and access metadata

SRC-1, `apps/server/src/context.ts`, `apps/server/src/ops/gather.ts`, `packages/core/src/qa/query.ts`, `packages/core/src/search/hybrid.ts`. Distinct from content [MEM-OBJ-sources](#mem-obj-sources) and [MEM-OBJ-context](#mem-obj-context); no supplied runtime object names these stores. MiniSearch access state and SQLite graph rows derive from filesystem bodies and metadata; navigation manifests and sidecars are readable but their path/type/date/link fields have symbolic consumers. Natural-language titles, one-liners and snippets supplied to a model are display/content parts, not proof that the underlying body entered context. Reindex adds research/context as concept and up to 400 contributor/raw extraction files as source; it persists the search index and calls graph reindex. Full invalidation of deletions across all writers is unresolved, not inferred from the name reindex.

> await walk('sources/contributors', (n) => n.endsWith('.md'));
> await walk('sources/raw', (n) => n.endsWith('.extracted.md'));
> --- `apps/server/src/context.ts`

The question consumer preferentially boosts hits classified source by 1.2 before taking candidates. This is a selection rule, not source authentication. Citation paths locate support, not entailment checks. Body truncation and incomplete sidecars can break provenance traversal without erasing the underlying content.

#### MEM-OBJ-embeddings
Label: Cached page embeddings

SRC-1, `packages/core/src/search/embedding-store.ts`, `apps/server/src/lib/embedding-indexer.ts`, `packages/core/src/search/hybrid.ts`. Dense numerical vectors are distributed-parametric representations; slug, content_hash, model and timestamp fields in the same JSON cache are symbolic access/provenance metadata, not a natural-language memory summary. Files live under embeddings/<slug>.json. The producer concatenates title and body, optionally including OCR sidecars, hashes the full supplied content and embeds it through [MEM-CMP-bge-m3](#mem-cmp-bge-m3). The encoder itself clips to 8,000 characters. This is derived indexing, not changing provider parameters or automatically extracting lessons from action outcomes. No supplied record identifies this cache.

> const vector = await embed(content);
> await this.store.set(slug, content, vector);
> --- `apps/server/src/lib/embedding-indexer.ts`

Hash matches suppress recomputation; indexAll runs at startup and indexOne affords individual updates. Hybrid search consumes retained vectors for cosine ranks, merges top-20 dense and BM25 lists by reciprocal rank, and optionally boosts backlink/recency/exact-title signals. The cache class exposes delete, but complete mutation-to-delete wiring is unresolved. Missing or mismatched source bodies can still affect rank before later text reads fail; hash existence is not a guarantee of freshness at each search.

#### MEM-OBJ-chats
Label: Saved chat transcripts

SRC-1, `apps/server/src/routes/chats.ts`, `apps/mcp/src/tools/recall-chat.ts`, `apps/mcp/src/resources/index.ts`. Distinct from [MEM-OBJ-sources](#mem-obj-sources): chats/<id>.json retains role/text and optional citation arrays as raw conversation records; natural-language messages are surrounded by symbolic session fields. Caller-supplied JSON becomes the retained record. GET, recall_chat and chat resources later return the record or selected previews. Deletion can move it to trash, independently of any excerpt note derived from it. No supplied runtime object identifies these transcript files.

> await ctx.store.writeJSON(`chats/${session.id}.json`, session);
> --- `apps/server/src/routes/chats.ts`

#### MEM-OBJ-chat-excerpts
Label: Filed chat excerpt notes

SRC-1, `apps/mcp/src/tools/save-chat-excerpt.ts`. Distinct from [MEM-OBJ-chats](#mem-obj-chats), and no supplied runtime object counterpart: excerpt saving produces wiki/notes/<slug>.md natural-language content plus symbolic sidecar fields and an index entry. It copies supplied content rather than summarizing it; only the title can be automatically generated. A source_chat_id can become a chat: reference, but no source-chat existence or extract-entailment check is shown. A saved excerpt need not be actual conversation text: caller identity/provenance is unresolved. Later wiki retrieval can consume the note independently of the originating transcript; deleting the transcript is not an established withdrawal of this separate note.

> await ctx.store.writeText(mdPath, `# ${title}\n\n${content}\n`);
> --- `apps/mcp/src/tools/save-chat-excerpt.ts`

### Routes

#### MEM-RTE-chat-retention
Label: Transcript save, recall and excerpt filing

SRC-1, `apps/server/src/routes/chats.ts`, `apps/mcp/src/tools/save-chat-excerpt.ts`, `apps/mcp/src/tools/recall-chat.ts`, `apps/mcp/src/resources/index.ts`. No counterpart in supplied routes: [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) saves marked answers, whereas this route saves caller transcripts or excerpts. Owner is server/MCP code; caller supplies record content. Trigger is PUT chat or save_chat_excerpt, not an automatic transcript-to-lesson process. Material is [MEM-OBJ-chats](#mem-obj-chats) and the separately retained [MEM-OBJ-chat-excerpts](#mem-obj-chat-excerpts).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Save acknowledgement or excerpt slug/title/path; recall returns sorted matching chat previews.
- Later read-back: recall_chat searches retained title/message substrings; MCP chat resources return full messages as Markdown, and GET chat returns the JSON. Excerpt notes are eligible for wiki retrieval.
- Delegated visibility: inapplicable — tools return to their requesting client; no child task is created here.
- Selection predicate: Lowercase substring query across titles/messages, newest updated first, default ten and maximum fifty previews; excerpt tool uses supplied title or first 1,000 content characters for title generation.
- Invalidation or expiry: Chat delete uses trash when FileStore affords it, otherwise remove; no TTL. Saving the same excerpt slug writes the same note path, without an explicit duplicate or version check here.
- Activation or effect: Stored transcript can be displayed/reloaded, excerpt content can become model-visible wiki material; behavioral activation and benefit unobserved.
- Evidence limits: Caller role and verbatim conversation origin unresolved; resource/tool availability establishes client affordance, not automatic injection into a later agent.

Admission: caller supplies/updates transcript or excerpt. The server casts the request body and validates chat ID; excerpt input is schema-checked, configuration is required, and title generation is conditional. No content-specific human approval or answer oracle. Human versus automated invocation is not resolved by MCP metadata. Physical writes are code's responsibility. Failure can leave partial note/metadata/index effects; no all-file rollback shown. Chat trash restoration is offered separately. Raw transcript retention alone is not trace-fed derivation; automatic titling does not establish acquired problem-solving capacity.

#### MEM-RTE-mcp-retrieval
Label: Alternative MCP retained-content delivery

SRC-1, `apps/mcp/src/tools/ask-wiki.ts`, `apps/mcp/src/tools/search-wiki.ts`, `apps/mcp/src/tools/read-wiki-page.ts`, `apps/mcp/src/tools/semantic-search.ts`, `apps/mcp/src/tools/load-project.ts`, `apps/mcp/src/resources/index.ts` (each named file directly inspected). Distinct from [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer): ask_wiki constructs its own prompt and never calls askQuestion. Registered handlers expose read-back to an external client role; deployed model use of raw tool/resource results is not established.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked snippets or dense/keyword results, full page/resource body, whole project core, or generated answer plus citation metadata.
- Later read-back: Explicit query/page/project requests select persistent wiki or project files; ask_wiki supplies selected retained bodies directly to its configured model.
- Delegated visibility: inapplicable — local retrieval and a completion, not a delegated agent frame.
- Selection predicate: ask_wiki unions explicit pages and top-five keyword seeds, expands incoming/outgoing one hop, takes first max_pages (default eight, max twenty), then reads wiki/notes bodies. search_wiki gives at most fifty snippets. load_project selects by explicit/current project and returns complete README/context/index.yaml without relevance filtering.
- Invalidation or expiry: inapplicable — these reads prescribe no retained-content expiry; underlying writer/index freshness is separate.
- Activation or effect: ask_wiki delivers full readable bodies through a user-role prompt with advisory citation instructions; tool/resources deliver to client. No semantic citation verification or observed influence established.
- Evidence limits: ask_wiki and read_wiki_page reconstruct wiki/notes paths; v2-shaped search hits do not establish successful v2 body reads through those handlers. No uniform all-layout retrieval claim.

> const body = await ctx.store.readText(`wiki/notes/${slug}.md`);
> --- `apps/mcp/src/tools/read-wiki-page.ts`

> const slugs = [...expanded].slice(0, max_pages);
> --- `apps/mcp/src/tools/ask-wiki.ts`

The semantic_search handler is a separate alternative: it lists wiki/notes, takes 1,000 body characters per page, remotely embeds query plus page texts using text-embedding-3-small at configured/default base URL, and cosine-ranks them. Errors fall back to keyword search. It does not use the persisted BGE cache described in [MEM-OBJ-embeddings](#mem-obj-embeddings). That remote model's parameters are not updated by this handler; exact weight revision and endpoint immutability are unresolved. This invocation creates transient dense representations, not a demonstrated durable memory update. Provider internals are uninspected.

> body: JSON.stringify({ model: 'text-embedding-3-small', input: texts }),
> --- `apps/mcp/src/tools/semantic-search.ts`

#### MEM-RTE-tree-edit
Label: Direct project file editing and withdrawal

SRC-1, `apps/server/src/routes/tree/crud.ts`, `apps/server/src/lib/tree-paths.ts`, `apps/server/src/routes/trash.ts`. Distinct from [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan): this caller-controlled surface writes file bodies without model proposals or a stored checkbox plan. Owner is HTTP route code, scoped by current project, known category and lexical path checks. The categories include README, context, soul, contributors, research, raw, logs and artifacts.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: File body/mtime, wroteBytes, rename acknowledgement or delete status/error.
- Later read-back: Updated README/context affect subsequent build/session consumers; retained source and research bodies can be loaded by explicit reads or later refreshed retrieval.
- Delegated visibility: inapplicable — direct HTTP file operations, no sub-agent.
- Selection predicate: Caller supplies category/path/body; single-file categories resolve to their designated project file.
- Invalidation or expiry: PUT replaces, rename moves, DELETE unlinks; no reindex or downstream cache invalidation call appears in these handlers. Trash routes separately expose restore/reindex and permanent deletion, not proof that tree unlink is restorable.
- Activation or effect: Content and instruction changes persist immediately without model or semantic checks. Session-start reads disk; immediate search consistency after edit/delete is not guaranteed by this route.
- Evidence limits: Caller identity does not establish human deliberation. Lexical path checking is not OS sandboxing; source/citation repair after rename is not established.

> await writeFile(abs, body, 'utf-8');
> --- `apps/server/src/routes/tree/crud.ts`

Admission: an open caller request supplies the new content; code validates category/layout/path and string body, not truth or 400-line context size. Humans can edit through a client, but server API identity leaves human control unresolved. No answer oracle. Invalid paths/layout/categories are rejected; no automatic prior-content snapshot/rollback shown here. This direct-tree countercase is additional to the executor's own add_wikilinks bypass. Server replacement and section-append checks, and MCP replacement overflow handling, remain branch-specific controls, not an executor-wide or all-writer cap; see [MEM-OBJ-context](#mem-obj-context) and [RT-RTE-build-context](runtime.md#rt-rte-build-context).

#### MEM-RTE-cli-ingest
Label: CLI plan/admit and graph-context compilation

SRC-1, `apps/cli/src/index.ts`, `apps/cli/src/commands/ingest.ts`, `apps/cli/src/commands/query.ts`, `packages/core/src/compile/l1.ts`, `packages/core/src/compile/context.ts` (directly inspected named files). Distinct from [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan): this is the shipped core compiler plan/execute path, not server ops JSON actions. CLI dispatch registers init, ingest, lint, query and rebuild-index; ingest is the retained-write branch traced here. Exact executor mutation semantics remain uninspected, so individual merge/review effects are not inferred from tool names.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed proposed tool actions, approval prompt unless --yes, per-action execution results or abort.
- Later read-back: Persisted wiki pages/index can feed subsequent compiler contexts; CLI query reads wiki/INDEX.md and returns at most twenty matching lines rather than answering with a model.
- Delegated visibility: inapplicable — local compilation/completion loop, no child agent.
- Selection predicate: CLI supplies an empty hybrid retriever. Core gather still has small-wiki concept survey, title-token overlap and recent-concept complements; the reusable gather also expands hybrid seeds one/two hops and ranks by score/backlinks. Self-source slug is excluded. Whole pages survive an approximate tokenBudget times four character budget; first over-budget candidate stops packing.
- Invalidation or expiry: Abort prevents plan application, not the earlier source ingest. Plan execution omits actions explicitly false; missing approvals mean approved. No universal rollback asserted for the underlying executor.
- Activation or effect: Model-requested tool calls are collected through dry-run executor, then real executor handles admitted actions without a fresh model call; no observed successful mutation or improved capacity.
- Evidence limits: A URL in this CLI path is stored via ingestPaste as URL text, not fetched article content. Executor, L2 and all non-CLI compiler callers not exhaustively traced.

> const hybridSearch = async (_q: string, _l: number) => [];   // v0 CLI: no hybrid search
> --- `apps/cli/src/commands/ingest.ts`

> const approved = approvals[action.id] !== false;
> --- `packages/core/src/compile/l1.ts`

Admission: model proposes under loaded schema sections and selected context; human confirms all or aborts, or --yes automatically licenses application. No expected-answer oracle. Structural/executor failure can reject actions, but the semantic checks within executor remain unresolved. The core also exposes direct compileL1, which gathers context, starts/completes an audit and executes model calls without this CLI confirmation. Its audit stores actions, context slugs and usage/status; its influence on later decisions was not established here. This is not evidence that audit traces become learned instructions. For working context, graph gathering excludes the source itself and clips by whole-page packing; the raw source plus scaffolding is outside that page budget. No persistent compaction summary is established by these functions.

#### MEM-RTE-synthesis-cache
Label: Cached synthesis, diagnosis and refresh

SRC-1, `apps/server/src/lib/synthesis.ts`, `apps/server/src/lib/synthesis-cache.ts`, `apps/server/src/lib/synthesis-worker.ts`, `apps/server/src/routes/synthesize.ts`, `packages/core/src/synthesis/validate.ts`, `apps/mcp/src/tools/find-contradictions.ts` (directly inspected named files). Distinct from [RT-RTE-research-page](runtime.md#rt-rte-research-page): this stores structured derived reports in synthesis/<topic-key>.json, not research Markdown actions. Distinct from [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings): different producer, validator, persistence and consumer. Mixed representation: natural-language summary/thread/contradiction/gap content, symbolic source slug/line ranges/hash/provenance fields. Stored reason/explanation text is readable in reports, not established as guidance to automatic knowledge repair.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Synthesis SSE meta/threads/gaps/contradictions/done, cached or newly generated; MCP find_contradictions returns only cached/generated contradiction array.
- Later read-back: Later synthesize requests stream retained report fields; find_contradictions can return a cached report subset. A worker reloads stale topic keys and replaces their retained reports.
- Delegated visibility: inapplicable — serial worker and local completion, no agent context frame.
- Selection predicate: Server synthesis hybrid-retrieves top twenty, reconstructs wiki/notes paths and skips unreadable bodies; schema/synthesis.md supplies optional preamble. Request cache key is normalized topic; force bypasses hit. Worker takes first stale key, one inflight.
- Invalidation or expiry: Reverse index maps source_hashes slugs to cached topic keys; markStaleFor queues dependent keys. Worker polls every five seconds and clears stale on success or error. Completeness of mutation-to-stale wiring is uninspected. HTTP cache hit does not check hashes or stale set before serving.
- Activation or effect: Validated structured reports persist and later display; critique-driven revision of the criticized wiki is not wired by this operation itself.
- Evidence limits: Source range existence checks are not entailment or contradiction proof; v2 path compatibility, MCP producer parity and external client response remain unresolved. No measured diagnosis quality or benefit.

Admission: open topic request or stale refresh; model authors the report, code validates and writes without per-content human approval. Source lines are citation-range reference material, not an expected-answer oracle. Threads without a valid citation are dropped. If inline markers appear, uncited sentences are pruned; otherwise a valid thread-level citation suffices to keep prose. Contradictions require a known with_slug and recognized confidence, not verified excerpt entailment. This is weaker than lint's quote-occurrence test. Failures can return empty results or clear a queued refresh; no automatic knowledge rollback or repair follows. Automatic refresh is content-derived maintenance, not outcome-trace learning.

> if (validCitations.length === 0) continue;
> --- `packages/core/src/synthesis/validate.ts`

> if (!c.with_slug || !sources.has(c.with_slug)) continue;
> if (c.confidence !== 'low' && c.confidence !== 'medium' && c.confidence !== 'high') continue;
> --- `packages/core/src/synthesis/validate.ts`

> console.warn(`[synthesis-worker] regen failed for ${key}:`, (e as Error).message);
> await this.ctx.synthesisCache.clearStale(key);
> --- `apps/server/src/lib/synthesis-worker.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-build-context](runtime.md#rt-rte-build-context)

SRC-1, `apps/server/src/ops/gather.ts`, `apps/server/src/ops/recipes/build.ts`. The write-side derivation is source/research excerpts plus existing context and README → model body → retained context/research → next build or hook. It is not a raw interaction trace automatically compacted into a lesson. It could incorporate contributed experience, but those contributors' original provenance is mixed/unknown. Prompt requests to preserve and flag contradictions establish curation intent, not realized semantic revision. A newer context mtime can exclude older files never selected because the thirty-file cap was reached; there is no per-source acknowledgement here. This is a supported risk from the selector, not an observed loss.

> const fresh = withM.filter((f) => f.mtime > contextMtime).sort((a, b) => b.mtime - a.mtime).slice(0, MAX_SOURCE_FILES);
> --- `apps/server/src/ops/gather.ts`

Context size control is branch-specific: update_context rejects over 400 lines and snapshots prior nonempty content; append_context_section rejects an over-limit result without snapshotting; add_wikilinks targeting context.md can append links without either control. Consequently even schema-valid actions within this build route do not enforce a universal context-line bound. This is a reachable source-level alternative, not an observed model choice or overflow (SRC-1, `apps/server/src/ops/types.ts`, `apps/server/src/ops/executors.ts`; direct implementation reads in this correction).

> const missing = action.links.filter((l) => !current.includes(`[[${l}]]`));
>       if (missing.length === 0) return action.path;
>       const seeAlso = `See also: ${missing.map((l) => `[[${l}]]`).join(', ')}`;
>       await writeFile(abs, `${current.replace(/\n*$/, '\n\n')}${seeAlso}\n`, 'utf-8');
> --- `apps/server/src/ops/executors.ts`

No total-token cap is established by thirty times 4,000 source characters: full README/current context and instruction scaffolding are additional. Source excerpts are prefix slices, not relevance-selected passages. MCP gather instead returns unbounded matching file metadata and delegates body reads to the host builder; it is not the server's thirty-file body selector.

#### On [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build)

SRC-1, `apps/plugin/agents/builder.md`, `apps/mcp/src/tools/gather-sources.ts`, `apps/mcp/src/tools/atomic-write-context.ts`. Working-context isolation is requested as a hosted sub-agent with projectId input and a one-line return. In the stack-frame lens, sources and instructions stay in the child and only a summary escapes; actual host inheritance/isolation is uninspected. The important additional persistent escape is context/research written to disk, which a later hook/model reloads. Window content is not a live reference to that disk state: only a new file read or injection obtains updates. No host context eviction or compaction algorithm is supplied by these instructions. The builder's declared deterministic rebuilding is not proof of deterministic model output.

#### On [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer)

SRC-1, `packages/core/src/qa/query.ts`. Later invocation consumption differs from merely holding a search hit. Only first three candidates' bodies enter the initial source blocks, clipped to at most 3,000 characters each, whereas the candidate list can describe six. Recent raw IDs are found over the supplied history, not just the final ten turns; at most two IDs are considered. Referenced raw retrieval uses sidecar sources and an older raw directory locator. Source preference and citation instructions are advisory; they neither authenticate original source authorship nor verify all claims.

> const noteTruncated = noteBody.slice(0, Math.min(3000, remaining));
> --- `packages/core/src/qa/query.ts`

Working context includes full hot cache and INDEX, candidate summaries, source blocks, last ten history messages and question; read_file can later restore complete requested content outside the initial source budget. The evicted history has no replacement summary in this function. Budget accounting covers source body slices, not these other inputs. Read_file results accumulate in the current call loop and are not independently a durable memory store. Optional answer filing creates a new retained synthesis, so a later question can encounter derived answers; a marker is not a quality gate. No activation or benefit inferred.

#### On [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings)

Supplied runtime evidence SRC-1, `apps/server/src/ops/runner.ts` establishes retained diagnostic findings and dismissal, not admitted wiki revisions. Dismissed state is a separate symbolic record from the criticized bodies. Same-day replacement limits history. A latest-artifact fetch is a display/read-back affordance, not proof that a later builder consumes the finding or its reasons. This prevents identifying this route alone as a closed trace-fed update to operational guidance.

#### On [RT-BAP-session-context](runtime.md#rt-bap-session-context)

SRC-1, `apps/plugin/hooks/hooks.json`, `apps/plugin/hooks/session-start`. This is unsolicited whole-project supply relative to the next question: the automatic trigger reads persisted currentProjectId and selects README/context/index.yaml, not a query. No truncation/relevance budget exists in the hook. It labels context as curated truth, but host acceptance and natural-language interpretation determine force; no semantic enforcement. The registration also matches clear/compact, affording post-compaction reload of these files, not arbitrary old transcript turns. What the host removed and whether it retained a summary remain external.

> "matcher": "startup|clear|compact",
> --- `apps/plugin/hooks/hooks.json`

## Write side

Admission and authorship must be kept apart. The supplied web contribution route lets model-generated actions await caller-selected indexes; it persists input before that checkpoint. Direct build/research and configured ask auto-save use software admission with no per-content human veto. Hosted build starts with a human command but MCP content replacement has no approval proof. Those distinctions are established in [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan), [RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-research-page](runtime.md#rt-rte-research-page), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer), [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build).

MCP contribute admits caller-supplied text after parsing and writes append-only entries; it does not authenticate human authorship or execute its described auto routing. Manual tree edits can replace derived content or operational README guidance directly, with content supplied by the caller and physical I/O performed by code. Transcript/excerpt writes similarly do not prove the caller is human. CLI ingest has explicit confirmation with an auto-approval flag. The cache admits model reports through structural/range checks, while embedding generation admits deterministic derived vectors on stale content hashes. These separate mechanisms are retained in [MEM-OBJ-sources](#mem-obj-sources), [MEM-RTE-tree-edit](#mem-rte-tree-edit), [MEM-RTE-chat-retention](#mem-rte-chat-retention), [MEM-RTE-cli-ingest](#mem-rte-cli-ingest), [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache), [MEM-OBJ-embeddings](#mem-obj-embeddings).

Rejection is route-local: expiry/deselection of a contribution proposal, parsing/line-cap or per-action execution error, discarded synthesis threads, user abort, or invalid direct-edit paths. A rejection log does not necessarily retract earlier captured input or partially applied actions. Withdrawal is also route-local: v2 tree DELETE unlinks directly; saved chats can be trashed; separate trash restore reindexes. Neither operation establishes removal of every derived mention, embedding, synthesis or snapshot. Context snapshots afford manual historical access, not automatic rollback or cascade deletion. See [MEM-RTE-tree-edit](#mem-rte-tree-edit), [MEM-RTE-chat-retention](#mem-rte-chat-retention), [RT-RTE-build-context](runtime.md#rt-rte-build-context).

No inspected mechanism establishes an automatic operation-outcome trace → durable revised method → later method-guided action chain. Raw chats, operation logs and compiler audits are not enough. Source-to-context synthesis and stale report refresh do establish derived-content maintenance, with partly unknown source provenance. They do not by themselves establish learned capacity, autonomous criticism, or exercised self-improvement. Untouched workers and executor branches prevent a whole-system negative.

## Read-back

Three delivery directions coexist. The session hook pushes selected-project files automatically, including after compact/clear. Core ask retrieves on a question and the model can request further files. Hosted builder requests file lists then reads bodies in a separate context. No shared global context budget covers these routes. Read-back details are attached to [RT-BAP-session-context](runtime.md#rt-bap-session-context), [RT-RTE-ask-answer](runtime.md#rt-rte-ask-answer) and [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build), not redeclared.

[MEM-RTE-mcp-retrieval](#mem-rte-mcp-retrieval) offers additional requested paths: snippets, full page resources, chat transcripts and full project core. Exposing a resource is an afforded external-client route, not evidence of automatic agent use. Its ask_wiki path, however, wires retained text into a completion. The CLI query consumes retained index text through fixed substring rules and prints matches; it is not question answering. Cached synthesis returns selected report fields and can omit its stored summary from the SSE output. A stored explanation can therefore be retained without governing revision or even reaching every consumer. See [MEM-RTE-cli-ingest](#mem-rte-cli-ingest), [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache).

Reasons survive only when present in copied bodies, contradiction explanations or audit action reasons; no universal rationale preservation contract was found in the traced routes. Context readers receive the current body, not the build's internal reasoning or snapshots. Lineage tags and citation metadata allow access but do not demonstrate warranted adoption or causal use.

## Integration issues

- **Cap inference corrected.** The previous memory report's server-rejection versus MCP-overflow comparison and endorsement of executor/MCP guarantees were too broad. Direct inspection of SRC-1 `apps/server/src/ops/types.ts` and `apps/server/src/ops/executors.ts` confirms an internal add_wikilinks bypass, not merely the external direct-tree exception. The supplied runtime now qualifies [RT-RTE-build-context](runtime.md#rt-rte-build-context) accordingly; no further supplied-record correction is requested. Core ideas, [MEM-OBJ-context](#mem-obj-context), the build annotation and [MEM-RTE-tree-edit](#mem-rte-tree-edit) now distinguish checked replacement/append, unchecked wikilink append and MCP overflow. Retained-context comparisons must not infer an executor-wide bound or snapshot guarantee.
- **No duplicate declarations identified.** New content/cache/metadata objects are not [RT-OBJ-actions](runtime.md#rt-obj-actions); new CLI/MCP/chat/tree/cache routes have different endpoints, admission or consumers than the closest cited runtime routes. Existing server/build/hook referents receive annotations rather than new IDs. [MEM-OBJ-chats](#mem-obj-chats) and [MEM-OBJ-chat-excerpts](#mem-obj-chat-excerpts) separately identify raw transcripts and filed notes because their retention and withdrawal are independent.
- **Layout compatibility unresolved.** [MEM-RTE-mcp-retrieval](#mem-rte-mcp-retrieval) and [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache) reconstruct wiki/notes paths; core ask handles v2-shaped paths separately. Do not extrapolate server source-aware retrieval to every registered tool. This limits end-to-end v2 recall and synthesis coverage, not existence of retained files.
- **Invalidation/withdrawal integration unresolved.** Reindex, stale queues, embedding hashes, tree unlink and trash restore have different controls. [MEM-OBJ-access-metadata](#mem-obj-access-metadata), [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-RTE-tree-edit](#mem-rte-tree-edit), [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache) do not establish complete downstream removal or freshness across all writers.
- **Timestamp selection can lose coverage.** [RT-RTE-build-context](runtime.md#rt-rte-build-context)'s annotation retains the cap-plus-context-mtime case; MCP gather differs. Prevents calling “unbuilt” a proof that every older source was incorporated.
- **Evaluation does not imply knowledge repair.** [RT-RTE-lint-findings](runtime.md#rt-rte-lint-findings) retains diagnostics/dismissal; [MEM-RTE-synthesis-cache](#mem-rte-synthesis-cache) retains different contradiction reports with weaker checks. No later automatic repair consumer established for either. Their reasons can remain display content.
- **Remaining included mechanisms remain unresolved, not absent.** The coverage table names capture/OCR/RSS, manual clients, L2/executor, other MCP writers, brief/SRS/classification/analysis, schema updates and evaluators. Their admission, lineage, actual later consumers and trace-fed transformations were not exhaustively inspected. This prevents uniform lifecycle, learning or context-management conclusions. No repository access gap was found; these are available-but-uninspected paths.

## Limitations and checks

Git HEAD was rechecked in this correction as c5273d2336c4d686df41c2a1495f14f085707f51. The previous inspection reported no working-tree changes. This correction directly reread the complete ops executor and action schema and otherwise preserves the previous report's bounded findings. Direct source reads stayed in SRC-1 at that checkout; the one attempted workers-directory enumeration returned an error because workers live under lib, which was subsequently enumerated. No target code, tests, fixtures, providers or external searches were executed. Source excerpts establish implementation or requested behavior, not observed compliance. The governing invocation, member types, collection, worker rules, complete record contract, boundary and both runtime ranges were read. No prior analyses were read. Uninspected providers/host behavior and the unresolved source paths above prevent benefit, exhaustive workflow coverage and cascade-retention conclusions.

Validation: the assigned role-specific commonplace-validate command passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”
