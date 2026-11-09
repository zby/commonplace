---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Kherad memory mechanisms: Git source and compiled knowledge, derived search state, session retention and later context selection."
run-id: AAS-2026-11-08-kherad-ac3e4da97ac6-01
source-identity: https://github.com/mohammadmaso/kherad
reviewed-boundary: "2a8d6992b87a33760688e1f956653c21a6292294"
---

# Kherad memory report

## Boundary and evidence

This report covers retained organizational content and task state in the shipped application at SRC-1, commit `2a8d6992b87a33760688e1f956653c21a6292294`. Memory includes source authoring, compilation, mirrored sources, publication, search projections, saved conversations, specialist snapshots/proposals/uploads and administrator-supplied skills. It includes context selection even when selection produces no new retained material. Current-process staging is distinguished from persistence. External model/provider state, MCP server contents and Docling internals remain opaque; they are not attributed local storage or learning mechanisms. No target program, test or example was executed.

The supplied runtime gives provisional admission and invocation findings. Direct reads added search refresh/chunking/embedding and agent search tools, source-mirror maintenance, indexer prompt and run setup, chat document tools, specialist research/edit tools, page mentions, session schema, compiled-document CRUD, raw deletion, search HTTP dispatch, embedding reindex configuration and version implementation. These are implementation and instruction-text evidence in the existing SRC-1, not observed operation. API registration was checked against these operations; the operative entry surface is HTTP routes and registered agent tools, not an assumed CLI or hook lifecycle. [SRC-1] `apps/api/src/index.ts`.

| Entry point or memory operation | Source scope and inspection | Covering records or limit |
|---|---|---|
| Raw save, import, ingestion and latest-draft selection | Supplied runtime; direct specialist research tools and raw delete range | [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring), [RT-RTE-ingest-document](runtime.md#rt-rte-ingest-document), [MEM-OBJ-source-pages](#mem-obj-source-pages) |
| Compile, delta, source mirrors, index/log | Direct `apps/api/src/agents/indexer/source-mirror.ts`, `prompt.ts`, `run.ts` setup/production ranges; supplied tool/admission findings | [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [MEM-OBJ-source-mirror](#mem-obj-source-mirror), [MEM-OBJ-compiled-docs](#mem-obj-compiled-docs) |
| MR approval, rejection/conflicts and remote synchronization | Supplied runtime, not independently re-audited | [RT-RTE-review-merge](runtime.md#rt-rte-review-merge), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull) |
| Manual compiled edit and draft reload | Direct `apps/api/src/routes/okf-docs.ts` | [MEM-RTE-compiled-edit](#mem-rte-compiled-edit) |
| Versions, restore, historical deletion | Direct `apps/api/src/routes/wiki-versions.ts`, `packages/core/src/git/versions.ts` creation/restore ranges | [MEM-RTE-version-restore](#mem-rte-version-restore) |
| Refresh, raw/OKF reconciliation and embedding maintenance | Direct `packages/core/src/search/refresh.ts`, `embedding.ts`, `chunking.ts`; embedding settings route | [MEM-OBJ-search-index](#mem-obj-search-index), [MEM-OBJ-chunk-content](#mem-obj-chunk-content), [MEM-OBJ-chunk-embedding](#mem-obj-chunk-embedding), [MEM-RTE-search-refresh](#mem-rte-search-refresh) |
| Chat reads and semantic/metadata tools; HTTP search | Direct chat/tools, shared search-tools and search route | [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat), [MEM-RTE-search-read](#mem-rte-search-read) |
| Conversation retention and replay | Direct schema, web `bundle-chat.tsx` history/transport range; supplied chat/session endpoints | [MEM-OBJ-message-parts](#mem-obj-message-parts), [MEM-RTE-history-replay](#mem-rte-history-replay) |
| Specialist draft, snapshot, proposals, upload reads and per-turn recap | Direct specialist tools and edit tools, schema; supplied session orchestration | [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session), [MEM-OBJ-session-content](#mem-obj-session-content) |
| Page attachments and excerpts | Direct `apps/api/src/agents/page-mentions.ts` | [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages) annotation |
| Skill/configuration admission and MCP | Supplied runtime findings only | [RT-RTE-admin-configuration](runtime.md#rt-rte-admin-configuration), [RT-BAP-session-skills](runtime.md#rt-bap-session-skills); remote payloads/effects unavailable, so no remote retention/cleanup guarantee |
| Wiki rendering, source conversion internals, remaining rename/folder UI details | Supplied boundary/runtime coverage where available; not independently audited here | No exhaustive UI or conversion correctness conclusion; these limits do not negate the identified later consumers |

## Core ideas

Kherad separates authored sources, derived knowledge and retrieval projections. Raw Markdown can be consumed from unmerged user branches; compilation produces a proposal, while ordinary MR approval controls default-branch publication. A programmatic source mirror is both readable knowledge and a compilation watermark. The watermark compares bytes, not the truth or adequacy of the derived concepts. [MEM-OBJ-source-pages](#mem-obj-source-pages), [MEM-OBJ-source-mirror](#mem-obj-source-mirror), [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile).

The later Q&A agent can navigate a retained index and read full documents, or request ranked snippets and metadata. Selection is model-requested retrieval, not independent unsolicited delivery. User-attached page context is assembled automatically after the user's attachment request. The statement that all chat knowledge is approved compiled content is too broad: attached raw pages and direct remote publication provide countercases already recorded by runtime. [RT-CLM-reviewed-chat](runtime.md#rt-clm-reviewed-chat), [MEM-RTE-search-read](#mem-rte-search-read), [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages).

Retention is not restricted to prose. Symbolic metadata controls filtering and recovery; dense vectors determine ranking; text chunks, not the numerical payload, become snippets. Saved conversations retain raw message parts. Session editing retains an immutable starting body and separately accepted replacements rather than repeatedly refreshing the live document. These mechanisms change what is available later, but no supplied trace establishes improved capacity, reliable model compliance or a causal benefit. [MEM-OBJ-chunk-embedding](#mem-obj-chunk-embedding), [MEM-OBJ-message-parts](#mem-obj-message-parts), [MEM-OBJ-session-content](#mem-obj-session-content).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-pages
Label: Authored source pages

Source-native identity: raw pages under `raw/<slug>` with legacy `wiki/<slug>` fallback, accompanied by `pages` database rows. Form: natural-language Markdown bodies, symbolic paths/IDs, deletion and redirect flags, titles and permissions. Storage: Git blobs/history/branches for content; Postgres for access and inventory metadata. Lineage can include human writing, imported model drafts, conversion/OCR/transcription and remote imports. Caller identity alone does not resolve per-content human authorship or approval. Closest supplied record [RT-OBJ-pending](runtime.md#rt-obj-pending) is a different, ephemeral map of compiled proposals; the source files are inputs to that map's producer, not its contents.

Consumers include specialist raw reads, page attachments, indexer source reads and human editors. Latest-source reads can select unmerged content; published source mirrors are distinct copies. Deletion sets database state and writes a deletion on the user's branch; this does not immediately erase historical Git content or every compiled derivative. [SRC-1] `apps/api/src/agents/specialist/tools.ts`, `apps/api/src/routes/pages.ts`; authoring and lineage passages are supplied by [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring), [RT-RTE-ingest-document](runtime.md#rt-rte-ingest-document), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull).

> const bytes = await git.getLatestSourcePageAtRef(bundle.defaultBranch, bundle.slug, path);
> --- `apps/api/src/agents/specialist/tools.ts`

> .set({ isDeleted: true })
> --- `apps/api/src/routes/pages.ts:368-419`

#### MEM-OBJ-compiled-docs
Label: Compiled documents and directory

Source-native identity: concept Markdown, root `index.md` and `log.md` under `okf/<slug>`. Storage: Git agent/user/default/version branches. Concept bodies and descriptions are natural-language knowledge; frontmatter type/tags/resource and paths also have symbolic consumers in validation, linking and search. The index is a model-readable directory; log entries describe updates, not verified reasons for correctness. Distinct from [RT-OBJ-pending](runtime.md#rt-obj-pending): persisted files are the post-transformation output, not the process-local proposal map. Source mirrors are separately declared below because their producer and byte-comparison consumer differ.

Indexer proposals, human edits and remote pulls can supply this content. Actual local publication consumers are the wiki and model document reads; later indexer runs read existing published files. Guidance requests preserving accurate content, citing primary and additional sources and retaining log history; it does not prove accurate compilation or preserved explanations. No mandatory rationale field establishes criticism or reasons for each assertion. [SRC-1] `apps/api/src/agents/indexer/prompt.ts`, `apps/api/src/agents/chat/tools.ts`, `apps/api/src/routes/okf-docs.ts`; admission exceptions in [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull).

> If a concept synthesizes several pages, set \`resource\` to the primary page and cite the others under a \`# Citations\` heading.
> --- `apps/api/src/agents/indexer/prompt.ts`

> const bytes = await git.getFileAtRef(bundle.defaultBranch, `${okfPrefix}/${validPath}`);
> --- `apps/api/src/agents/chat/tools.ts`

#### MEM-OBJ-source-mirror
Label: Published source mirror

Source-native identity: `okf/<slug>/source/<path>.md` and copied `_assets`. Storage: Git compiled tree; Markdown copy remains natural-language source content, while byte identity and path membership have symbolic watermark authority. It is distinct from raw sources and compiled concepts: code copies selected raw bytes rather than asking the model to summarize them. Closest supplied route [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile) produces it; no supplied object declares this retained copy.

The next compile compares current latest-source bytes against the published mirror, with missing index selecting full compilation and changes/deletions selecting delta work. Concept `resource` fields target source mirror URLs. Chat document reads and search can expose mirrors along with concepts, index and log. Thus source copies are not just hidden bookkeeping. They preserve originating content, not necessarily the model's derivation or justification. Assets are refreshed by copying enumerated files; this helper does not establish exhaustive removal of old assets. [SRC-1] `apps/api/src/agents/indexer/source-mirror.ts`, `packages/core/src/search/refresh.ts`, `apps/api/src/agents/chat/tools.ts`.

> } else if (!bytesEqual(live, mirroredBytes)) {
>       changed.push(page);
> --- `apps/api/src/agents/indexer/source-mirror.ts`

> path: okfDocGitPath(bundleSlug, `source/${page.path}.md`),
>       content: decoder.decode(bytes),
> --- `apps/api/src/agents/indexer/source-mirror.ts`

#### MEM-OBJ-search-index
Label: Search index projection

Source-native identity: `search_index`, joined to `pages`/`bundles`. Storage: Postgres. Distinct from [RT-OBJ-pending](runtime.md#rt-obj-pending), this is durable derived access state, not proposed content. Forms: symbolic tsvector/JSON metadata and natural-language plain-text projection. `indexPage` renders Markdown, prefixes title, strips NUL, caps displayed content at 50,000 characters but builds the tsvector from the uncapped indexed text, using English and simple token configurations. Raw metadata is null; compiled metadata is projected from frontmatter. A keyword match can therefore come from text beyond the retained snippet projection. [SRC-1] `packages/core/src/search/refresh.ts`, `packages/db/src/schema.ts`.

> const content = indexed.slice(0, CONTENT_CAP);
> --- `packages/core/src/search/refresh.ts`

> tsv: sql`to_tsvector('english', ${indexed}) || to_tsvector('simple', ${indexed})`,
> --- `packages/core/src/search/refresh.ts:53-53`

Consumers are HTTP keyword/hybrid search and model metadata filtering. Metadata is access structure, not evidence that the document's claims are correct. Its semantic force at the model arises only if selected results/content are delivered. [MEM-RTE-search-read](#mem-rte-search-read).

#### MEM-OBJ-chunk-content
Label: Embedding chunk text

Source-native identity: `page_embedding_chunks.content` and `chunkIndex`. Storage: Postgres text/integer columns. Form: natural-language title-prefixed rendered text plus symbolic ordinal. Lineage: heading-aware Markdown splitting, packing toward 1,400 characters, oversized-section splitting toward 2,000 with 200-character overlap, rendering and first-64-chunk cap. These are heuristic targets, not a proof that every returned chunk is at most 2,000 characters: a lone oversized first paragraph can remain intact through `splitOversized`. Empty input gets title-only content. Distinct from [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) and the vector part below: it is derived readable content, not a provider model or numerical representation. [SRC-1] `packages/core/src/search/chunking.ts`, `packages/db/src/schema.ts`.

> return texts.slice(0, MAX_CHUNKS);
> --- `packages/core/src/search/chunking.ts`

The selected best chunk supplies a 300-character semantic-search snippet; full original Markdown remains reachable through document tools. Coverage beyond the 64 chunks is not guaranteed by semantic retrieval. [SRC-1] `apps/api/src/agents/search-tools.ts`, `apps/api/src/routes/search.ts`.

#### MEM-OBJ-chunk-embedding
Label: Stored chunk embeddings

Source-native identity: `page_embedding_chunks.embedding` with `model`, `dim`, `updatedAt` and page/chunk identity. Storage: Postgres pgvector and symbolic metadata. Form: distributed-parametric dense numerical representation; no claim that these are model weights. Derived from chunk text by configured embedder, whose internal provenance and exact weights are unresolved in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model). This is a distinct retained output, not that component itself. Paired readable chunk content is [MEM-OBJ-chunk-content](#mem-obj-chunk-content).

Similarity consumers use cosine distance and require the current model string; stored vectors themselves are not delivered as prose to the answering model. Software replaces all page chunks after embedding succeeds and checks returned vector count. Embedding failures are caught by indexing, so updated keyword state need not imply updated vectors. A failure before deletion can leave old vectors, including old snippet text, under the same model name. No content-hash freshness gate is shown in the search consumer. A model-string change deletes other-model chunks; changing weights behind the same name or endpoint is not equivalent invalidation. [SRC-1] `packages/core/src/search/embedding.ts`, `packages/core/src/search/refresh.ts`, `apps/api/src/routes/embedding-settings.ts`, `apps/api/src/agents/search-tools.ts`.

> const vectors = await embedder.embed(chunks);
> --- `packages/core/src/search/embedding.ts`

> eq(schema.pageEmbeddingChunks.model, embedder.model),
> --- `apps/api/src/agents/search-tools.ts`

#### MEM-OBJ-session-content
Label: Specialist retained content

Source-native identity: `agentSessions` snapshot/draft, `agentSectionEdits` and `agentUploads`. Storage: Postgres Markdown/text and rendered HTML, with symbolic status/IDs/timestamps. Natural-language proposed content is distinguished from admission metadata: `proposed`, `accepted`, `rejected`, `superseded` decide which body is effective. HTML is a display rendering, not the authoritative replacement body. Closest supplied [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session) is the producing/consuming route, not an object declaration; this does not duplicate a supplied object.

Lineage: session-start target snapshot, model-written draft/replacement proposals, caller uploads. `read_page_section` uses latest accepted replacement or original snapshot; a new rejected proposal does not erase an earlier accepted replacement. The per-turn instruction recap communicates current statuses, not proposal bodies or a criticism rationale. User-facing views render pending previews or effective bodies separately. Accepted-override assembly produces saved Markdown; manual content is a separate save path. Reasons can remain conversational, but no required reason field or reason-consuming tool is shown in these edit records. [SRC-1] `packages/db/src/schema.ts`, `apps/api/src/agents/specialist/page-edit-tools.ts`, `apps/api/src/agents/specialist/tools.ts`; save admission in [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring).

> return latestAccepted(edits, section.id)?.proposedMarkdown ?? section.markdown;
> --- `apps/api/src/agents/specialist/page-edit-tools.ts`

> const status = sectionStatus(section, edits);
>     return `- ${section.id} ("${section.headingText}"): ${status}`;
> --- `apps/api/src/agents/specialist/page-edit-tools.ts`

`read_upload` selects a session-owned upload ID and returns its stored text; it does not automatically inject every upload. `propose_document` writes a draft without per-content approval; user import/save is a later gate. Session deletion cascades associated edits/uploads/messages in the schema. This retention is task work and model-output persistence, not demonstrated trace-fed method learning.

#### MEM-OBJ-message-parts
Label: Saved message parts

Source-native identity: `chat_messages.parts` and `agent_messages.parts`. Storage: Postgres JSONB with role/thread/session identity and timestamps. Form: mixed natural-language text and symbolic AI SDK parts (including attachment selectors and tool/display payloads); no numerical learning state is established. This is raw conversation retention, distinct from compiled knowledge and [RT-OBJ-pending](runtime.md#rt-obj-pending). Closest supplied routes [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat) and [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session) persist it but do not declare the object.

> // AI SDK UIMessage.parts stored verbatim so history replays losslessly into useChat.
>     parts: jsonb("parts").notNull(),
> --- `packages/db/src/schema.ts`

The schema comment expresses design intent; actual replay wiring is [MEM-RTE-history-replay](#mem-rte-history-replay). Persistence is not extraction of lessons, and thread storage alone is not the POST model-history source. Message parts can retain attachment identifiers whose target bodies are reloaded live, not a stable historical snapshot. Thread/session deletion cascades their message rows. External SDK transformations and provider-side retention remain uninspected.

### Routes

#### MEM-RTE-search-refresh
Label: Derived search refresh

Endpoints/progression: merge/remote/restore/admin reindex → raw diff refresh or full raw/OKF reconciliation → plain-text/metadata write → optional chunk embedding replacement. Owner: application rules and configured embedder, not a model deciding which content deserves admission. This adds the derivation route below the supplied publication routes rather than duplicating [RT-RTE-review-merge](runtime.md#rt-rte-review-merge) or [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull). Effects persist the three search objects above. [SRC-1] `packages/core/src/search/refresh.ts`, `packages/core/src/search/embedding.ts`, `apps/api/src/routes/embedding-settings.ts`.

- Immediate return: refresh resolves or errors; reindex endpoint returns progress state while processing asynchronously.
- Later read-back: keyword/metadata consumers read projected rows; semantic consumers use vectors and selected stored text.
- Delegated visibility: embedder receives title-prefixed chunk text; provider internals are uninspected.
- Selection predicate: raw merge paths or full live subtree enumeration; OKF includes every Markdown document, including index, log and source mirrors. Admin reindex selects unarchived bundles.
- Invalidation or expiry: raw missing files become soft-deleted with indexes/embeddings deleted; stale OKF page rows are hard-deleted with cascading search state; successful embedding replaces page chunks; model-string change removes incompatible chunks.
- Activation or effect: durable search access/ranking state changes; better retrieval or changed model answers unobserved.
- Evidence limits: embedding is best effort and Git/database operations are not established as a cross-store transaction; refresh does not certify semantic truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission control is software derivation from already selected content, not another human factual approval. Admin starts reindex but does not approve each derived chunk. Failures count/log; retry via reindex is afforded, not observed. No answer oracle or trace-scored curriculum is involved. Underlying content may be model-derived or human-authored; this is content indexing, not an automatic transformation of task-outcome traces into a learned operating method.

> // Hard-delete cascades to search_index + page_embedding_chunks via FK.
> --- `packages/core/src/search/refresh.ts`

#### MEM-RTE-search-read
Label: Retained content selection

Endpoints/progression: model tool arguments or HTTP query → scope/metadata/query embedding → ranked candidates → permission gating → snippets/metadata delivered to model or HTTP reader. Owner: model/user requests; code selects and filters. Distinct from the enclosing [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat) and [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session), which include generation and other tools. [SRC-1] `apps/api/src/agents/search-tools.ts`, `apps/api/src/routes/search.ts`.

- Immediate return: result metadata and optional snippets, not full source documents or numerical vectors.
- Later read-back: accumulated indexed knowledge reaches later model calls through tool results or human search responses; this is an implemented consumer route, not just a storage API.
- Delegated visibility: no child model context is created; external embedder receives the query; foreground model receives allowed results.
- Selection predicate: agent semantic search ranks pages by maximum chunk similarity, selects best-chunk first 300 characters, filters model string, live/unarchived state and optional bundle/type/tags. Agent metadata search uses JSON containment and title order, optional resource. Chat scope is bundle OKF; specialist user scope gates raw paths and OKF bundle visibility.
- Invalidation or expiry: current query reads persisted indexes; freshness depends on refresh success. Deletion/archive filters suppress candidates; model-string filter is not a content freshness check.
- Activation or effect: requested retained snippets become available to answer/draft generation; their actual influence and correctness are unobserved.
- Evidence limits: finite candidate pools before permission checks can underfill results; no evidence of exhaustive recall or relevance quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Agent semantic budget defaults to 8 results, maximum 15; metadata defaults 20, maximum 50, both fetch up to four times the requested limit before gating. HTTP search defaults to keyword, supports semantic and hybrid reciprocal-rank fusion with k=60, defaults 20/max 50 results and four-times candidate pools; hybrid falls back to keyword if embeddings are unavailable. A schema-valid query and returned scores are not an answer oracle. [SRC-1] `apps/api/src/agents/search-tools.ts`, `apps/api/src/routes/search.ts`.

> const similarity = sql<number>`max(1 - (${schema.pageEmbeddingChunks.embedding} <=> ${qvec}))`;
> --- `apps/api/src/agents/search-tools.ts`

> const results = await gateResults(db, user ?? null, isAdmin, candidates, limit);
> --- `apps/api/src/routes/search.ts`

#### MEM-RTE-history-replay
Label: Saved conversation replay

Endpoints/progression: authenticated thread open → GET stored messages → web `setMessages` → subsequent chat transport sends messages → model stream. Owner: user opens thread, web/API move state, model interprets submitted history. This fills in the later-consumer chain of [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat); not a second declaration of the complete answering route. [SRC-1] `apps/web/src/components/chat/bundle-chat.tsx`, `apps/api/src/routes/chat.ts`, `packages/db/src/schema.ts`.

- Immediate return: history populates UI; next turn produces the usual streamed answer.
- Later read-back: saved user/assistant parts reach subsequent calls via the client message array, rather than POST reconstructing history from thread ID.
- Delegated visibility: inapplicable — foreground conversation replay, not parent/child delegation.
- Selection predicate: user selects a thread; server ownership and bundle checks constrain GET; client chooses submitted message array.
- Invalidation or expiry: new chat clears local messages/thread; thread deletion cascades stored messages; persisted history does not guarantee old attachment bodies remain unchanged.
- Activation or effect: prior messages become model context; no evidence isolates their effect on an answer.
- Evidence limits: caller can supply a different array; storage comment about lossless parts is not proof of dependency-level byte-exact model input or successful persistence on every stream.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const { messages: rows } = await fetchChatThread(bundle.id, id);
>       setThreadId(id);
>       clearError();
>       setMessages(rows as unknown as UIMessage[]);
> --- `apps/web/src/components/chat/bundle-chat.tsx`

#### MEM-RTE-compiled-edit
Label: Manual compiled document editing

Endpoints/progression: permission-checked compiled content GET/PUT → validated body → user-branch Git write; ordinary publication remains MR-controlled. Owner: caller edits, code validates path/frontmatter/permission, Git persists. This is distinct from raw-specialist [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring), although both use user branches. [SRC-1] `apps/api/src/routes/okf-docs.ts`.

- Immediate return: content plus branch/editability on GET; commit OID, branch and timestamp on PUT.
- Later read-back: editor GET prefers caller's branch where file exists, else default; published chat reads default rather than this editor preference.
- Delegated visibility: inapplicable — editor HTTP operation, no delegated model.
- Selection predicate: llm_compiled mode, validated site path and per-site-path permissions; reserved read-only names cannot be PUT.
- Invalidation or expiry: successive edits replace branch content; publication and subsequent indexer rewrites can change later default content.
- Activation or effect: saved compiled proposal becomes editor-readable immediately, not automatically default-branch model knowledge.
- Evidence limits: generic caller does not establish human review of each assertion; no automatic preservation of manual edits against later recompilation is established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: caller proposes/replaces text; code can veto invalid input and read-only paths; MR reviewer controls ordinary later publication. Open editing, no expected-answer oracle. Recovery is later branch edit/history and review rejection, not automatic semantic rollback. Guidance and rationale for manual edits are unspecified; no reason is required in this body.

> [{ path: okfDocGitPath(bundle.slug, docPath), content }],
>       `Update OKF document: ${docPath}`,
> --- `apps/api/src/routes/okf-docs.ts`

#### MEM-RTE-version-restore
Label: Bundle snapshot and restore

Endpoints/progression: review-authorized version create/list/restore/delete → version Git branch or subtree graft → default-branch commit → raw/OKF reconciliation. Owner: authorized caller selects content snapshot; Git rules persist/graft it. Distinct from external remote admission [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull): retained local history supplies the replacement. [SRC-1] `apps/api/src/routes/wiki-versions.ts`, `packages/core/src/git/versions.ts`.

- Immediate return: version identity/OID or restored flag and raw reconciliation counts; errors for invalid/missing versions.
- Later read-back: version tree can be read by version viewers; restored default tree feeds ordinary wiki, compilation and model/search reads.
- Delegated visibility: inapplicable — history selection and Git operation, not a model worker.
- Selection predicate: named bundle/version or optional full commit for creation; scope includes raw, legacy wiki and compiled OKF prefixes, not other bundles.
- Invalidation or expiry: named branch can be deleted; restore clears each prefix absent from snapshot, preserves linear prior history, and skips identical trees.
- Activation or effect: historical content directly replaces default bundle subtrees and reconciles search, without a new MR in this route.
- Evidence limits: rollback of Git content is wired, not transactional rollback of every database/session object; latest user-branch source selection can still differ from restored default.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: review permission authorizes selecting the snapshot; no per-document approval or model critic is required. Mode is manual recovery/versioning, no reference-answer oracle. Rationale consists of commit/version identity and history, not required semantic criticism. Recovery can restore another version; deleting a branch is not proof of physical Git-object erasure. The route file's raw-only header comment is narrower than executable helper scope; the latter includes OKF.

> return [
>     bundleGitPathPrefix(bundleSlug),
>     legacyBundleGitPathPrefix(bundleSlug),
>     okfGitPathPrefix(bundleSlug),
>   ];
> --- `packages/core/src/git/versions.ts`

> await reconcileOkfSearchIndex(db, git, bundle, embedder);
> --- `apps/api/src/routes/wiki-versions.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile)

Memory-specific selection is a source-byte watermark and resource-link lookup, not score-based evaluation of prior answers. [MEM-OBJ-source-mirror](#mem-obj-source-mirror) determines full/delta/no-op; linked concept names are suggestions in kickoff, not a write allowlist. Existing default-branch documents remain available through tools, while all source bodies need not be preloaded. The retained result is content, references and update descriptions; no automatic conversation/outcome-to-skill extraction is established by this path. Raw source provenance can itself include prior model work, so neither purely human nor purely agent-trace origin is justified system-wide. [SRC-1] `apps/api/src/agents/indexer/source-mirror.ts`, `apps/api/src/agents/indexer/prompt.ts`, `apps/api/src/agents/indexer/run.ts`; raw admission in [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring).

#### On [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session)

Persistent task content is [MEM-OBJ-session-content](#mem-obj-session-content); stored dialogue is [MEM-OBJ-message-parts](#mem-obj-message-parts), not a derived policy. Per-turn section status is reconstructed from edit rows, while effective content uses accepted bodies or original snapshot. `read_upload` returns stored text only on an ID request. Section reads recommend fine granularity but do not enforce small bodies. These are selected task contexts, not agent-spawned stack frames: separate session state keeps unrelated work out, but there is no parent receiving only a child return or automatic frame-pop. Persisted session data remains reachable after a model call ends. [SRC-1] `apps/api/src/agents/specialist/tools.ts`, `apps/api/src/agents/specialist/page-edit-tools.ts`.

#### On [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages)

Each invocation extracts the latest eight distinct mentions across user messages, reloads viewable pages, and clips each body at 20,000 characters before appending instructions. That automatic assembly follows explicit user selectors, not an independent content-monitoring push. Older mentions and long-body tails are preferentially excluded from the generated block; the identifiers remain in replayable parts and full bodies remain in Git. Re-mentioning can change selection; new turns can reload changed bodies. The helper checks bundle/archive/access and bytes, but does not itself filter `pages.isDeleted`; a soft-delete row alone therefore does not prove that every old mention ceases to yield readable Git content. This qualifies withdrawal completeness, not the runtime's stated permission/branch rule. [SRC-1] `apps/api/src/agents/page-mentions.ts`.

> return [...seen.values()].slice(-MAX_MENTIONS);
> --- `apps/api/src/agents/page-mentions.ts`

Specialist selected quotations use only the latest user message, maximum six normalized excerpts at 2,000 characters each. These caps constrain the generated instruction blocks, not the complete conversation. No retained summary replaces removed attachment tails in this helper; original source and message parts supply the reload path.

> const text = q.text.replace(/\s+/g, " ").trim().slice(0, MAX_QUOTE_CHARS);
> --- `apps/api/src/agents/page-mentions.ts`

#### On [RT-BAP-session-skills](runtime.md#rt-bap-session-skills)

These are administrator-admitted natural-language methods retained in Postgres and selected by session attachments, then freshly loaded into instructions. They have stronger intended method authority than factual snippets, but compliance remains interpretive. Runtime's quoted directive and [RT-RTE-admin-configuration](runtime.md#rt-rte-admin-configuration) establish the actual channel and write agency. No trace-fed skill rewrite, required reason retention or versioned method criticism is established by those inspected routes. This is independent of the positive fact that models persist drafts and accepted content.

## Write side

Acquisition has several admission controls, not one review rule. Raw save/import and ingest commit require authorized caller action, with model/converter authorship separate from the caller's admission. Model specialist tools automatically persist draft/proposal rows before user import/save. Section decisions change symbolic status; latest accepted text controls effective reads and ordinary assembled saves, while manual-content save bypasses that assembly. Administrator edits admit methods/configuration separately. Remote pulls and version restores can replace default-branch content without an MR. [RT-RTE-ingest-document](runtime.md#rt-rte-ingest-document), [RT-RTE-source-authoring](runtime.md#rt-rte-source-authoring), [RT-RTE-admin-configuration](runtime.md#rt-rte-admin-configuration), [RT-RTE-remote-pull](runtime.md#rt-rte-remote-pull), [MEM-RTE-version-restore](#mem-rte-version-restore).

Compilation is automatic semantic transformation of admitted inputs under a static prompt, followed by structural tool checks, resource URL rewrite, byte-copy mirrors and proposal commit. Human review is a later publication decision, not the model's authorship or the programmatic mirror write. Rejection returns an MR to draft; conflicts and status rows retain recovery information. Neither structural validation nor successful merge means factual evaluation passed an answer oracle. [RT-RTE-indexer-compile](runtime.md#rt-rte-indexer-compile), [RT-RTE-review-merge](runtime.md#rt-rte-review-merge).

Withdrawal is staged and consumer-specific. Raw deletion immediately marks the page and commits branch deletion; raw inventory/search filters and later compile delta can remove it and associated mirrors/concepts through their respective paths. Existing default compiled material can remain until an admitted change, and historical trees/messages need not vanish. Search reconciliation deletes stale projections, but failed embedding replacement can leave earlier searchable chunks. Rejection of an edit prevents that proposed body becoming an accepted override; it does not erase an older accepted body. These mechanisms are not a universal retraction guarantee. [MEM-OBJ-source-pages](#mem-obj-source-pages), [MEM-OBJ-session-content](#mem-obj-session-content), [MEM-RTE-search-refresh](#mem-rte-search-refresh), [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages) annotation.

Raw dialogue retention is not a demonstrated raw-trace → lesson → later-method chain. The positive automatic derivations inspected are source → concepts/mirror → later reads, content → index/vectors → retrieval, and accepted edits/status → effective body/recap → later edit turn. They retain content and access/review state, not necessarily explanations for why the content is true or why a strategy worked. Initial corpus/skill authorship and remote provenance remain local unknowns; known transformations do not resolve them. No reliable trace-fed improvement or criticism-driven method revision is inferred.

## Read-back

The primary later consumers are human wiki/editor readers, indexer invocations, specialist invocations and bundle Q&A. Full-document paths deliver persisted Markdown; semantic paths deliver best-chunk snippets and access metadata, not opaque vectors. Model-selected index/document reads and section/upload tools keep external bodies outside the initial window until requested. A read acknowledgment alone does not establish activation, and retrieval availability does not establish learning. [MEM-RTE-search-read](#mem-rte-search-read), [MEM-OBJ-compiled-docs](#mem-obj-compiled-docs), [MEM-OBJ-session-content](#mem-obj-session-content).

Saved conversation read-back is client-mediated, not an automatic database thread injection. Mentions are replayed selectors that trigger fresh body fetches, whereas saved edit snapshots are fixed starting content with accepted overlays. Live skill reload similarly means a later turn can receive a changed method without a historical skill snapshot. These are different temporal semantics and cannot be grouped as a single stable checkpoint. [MEM-RTE-history-replay](#mem-rte-history-replay), [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages), [RT-BAP-session-skills](runtime.md#rt-bap-session-skills).

Working-context controls include delta inventories, on-demand document/section/upload reads, bounded attachment blocks and separate user-owned task sessions. They do not establish a general compaction service. The available code paths and supplied runtime show no retained summary replacing old dialogue here; dependency-level compaction remains uninspected rather than absent. The stack-frame analogy fits separation of selected task inputs only: these are not child invocations with a return-only escape, and persisted state survives. Source pointers are useful reload selectors but do not act like memory references with automatic liveness tracking. No inspected selector provides an overall token budget for complete submitted histories.

## Integration issues

1. **Additional admission route:** [MEM-RTE-version-restore](#mem-rte-version-restore) adds local historical default-branch replacement to runtime's remote-pull exception. Executable version scope includes compiled OKF despite the raw-only comment in the API route. No supplied runtime assertion is contradicted, but a synthesis must not enumerate only remote sync as the bypass. [SRC-1] `packages/core/src/git/versions.ts`, `apps/api/src/routes/wiki-versions.ts`.
2. **Withdrawal limit:** the [RT-BAP-attached-pages](runtime.md#rt-bap-attached-pages) annotation identifies no page-row deletion filter in attachment assembly. Database soft deletion and eventual Git publication differ. This prevents concluding immediate universal withdrawal across attachments, published concepts and historical messages. No observed stale disclosure is asserted.
3. **Freshness limit:** [MEM-OBJ-chunk-embedding](#mem-obj-chunk-embedding) and [MEM-RTE-search-refresh](#mem-rte-search-refresh) establish best-effort embedding replacement. Search model-string matching does not prove current content/version. Later evaluation must not equate refreshed keyword metadata with refreshed semantic payload.
4. **Potential record overlap:** [MEM-RTE-history-replay](#mem-rte-history-replay) expands the replay segment of [RT-RTE-bundle-chat](runtime.md#rt-rte-bundle-chat); [MEM-RTE-search-read](#mem-rte-search-read) spans search segments of chat/specialist, and [MEM-RTE-search-refresh](#mem-rte-search-refresh) expands post-publication maintenance. They are narrower/different chains, not replacement declarations of those full routes. New retained objects are distinct from ephemeral [RT-OBJ-pending](runtime.md#rt-obj-pending); no exact supplied-object duplicate was found.
5. **Unresolved external/operational facts:** actual corpus provenance, provider/MCP retention, runtime SDK message transformations, successful reindex/recovery and semantic compliance remain unobserved or externally opaque. This prevents quality, safe-retention and exercised-learning claims, not the source-level existence of the declared paths. Supplied [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-RTE-specialist-session](runtime.md#rt-rte-specialist-session) retain their limits.

## Limitations and checks

HEAD was rechecked against the exact reviewed commit before direct source inspection. All new anchors remain in SRC-1; no external source, prior analysis or unregistered execution evidence was used. Supplied member identity and source identity were retained exactly. Source passages establish implementation and prompt requests, not model obedience, observed use or causal benefit. No target code or tests were run. Available but uninspected UI/converter details and dependency internals remain limitations stated above, not evidenced absences. No theory-builder, reflection or self-improvement result is inferred from retention alone.

Validation: deterministic role/content validation passed for this candidate with the supplied artifact context; it checks form and quotation occurrence, not semantic acceptance.
