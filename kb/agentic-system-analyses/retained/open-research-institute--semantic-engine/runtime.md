---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Semantic Engine runtime baseline: operator-driven ingestion, embedding, retrieval and alternate display/export paths at the frozen commit."
run-id: AAS-2026-10-17-semantic-engine-666c064cd8dc-01
reviewed-boundary: "7e2481671cad01f0b4c89f2a1877d6733d7e552c"
---

# Semantic Engine runtime report

## Runtime account

### Work and evidence

Semantic Engine ships an operator-orchestrated sequence of scripts, not a model choosing successive actions. The root README describes ingestion, embedding and visualization; the CLI README calls its tweet quickstart “RAG,” but the query implementation returns documents without generating an answer ([RT-CLM-pipeline-purpose](#rt-clm-pipeline-purpose), [RT-RTE-query-documents](#rt-rte-query-documents)). Code owns control flow and ranking; models supply dense embeddings. Human operators choose datasets, archives, feeds and query text. Corpus authors need not be the operators.

This account uses SRC-1 implementation and doctrine/design at the boundary's frozen commit. No target, tests or services were executed. All operation and benefit remain unobserved. The source inventory is the [boundary](boundary.md); this inspection adds no source or functional exclusion. Paths inspected here are the CLI README, manifest, environment template, database/configuration/vector files, seven scripts and chunker; canvas processor, PCA and browser consumer; Knowledge Gate page; root README and UI App. These are within the boundary's registered coverage. Dependency and provider internals remain uninspected.

### Ordinary invocation and state ownership

The documented ordinary sequence is dependency installation and schema push, archive download, archive load, embedding, then query (SRC-1, `apps/semantic-engine-cli/README.md`, `apps/semantic-engine-cli/package.json`). These are separate operator invocations; no shipped controller runs the entire sequence. The README's commands are operating guidance, not evidence of completed runs.

The download principal selects usernames, or all archives if omitted. The downloader lists Supabase storage objects, skips existing local files, and runs up to the configured number of downloads concurrently. Failures log and skip an item; existing files are not refreshed. Files are downloaded input, not yet database admission (SRC-1, `apps/semantic-engine-cli/scripts/download-archives.mts`). The archive loader then reads operator-supplied paths, filters retweets and replies to others, constructs threads in chronological order, assigns random document IDs, hashes content, splits text and inserts document batches followed by chunk batches. Missing parent threads are dropped. There is no outer transaction spanning the two insert phases in this driver. Thus starting this process is not per-document human approval or an atomic corpus replacement ([RT-RTE-ingest-documents](#rt-rte-ingest-documents)).

The dataset identity is an environment-derived SQLite filename. Root documents carry text and provenance; chunks carry parent IDs, text offsets and optional embeddings ([RT-OBJ-docs-chunks](#rt-obj-docs-chunks)). Neither a user identity nor a provider conversation ID is a runtime coordination primitive. A chunk's integer ID is the embedding pagination cursor. There are no agent turns in this sequence.

Embedding sends each selected chunk's content to LMStudio through the AI SDK. Its model is selected by environment, with no immutable weights identity. The script prefetches one next batch, awaits the current model request and writes results by chunk ID. It does not ask the model to approve content, modify the pipeline or select tools. A failed batch is skipped for that invocation, not retried before advancing. A later fresh invocation can select still-null rows ([RT-RTE-embed-chunks](#rt-rte-embed-chunks), [RT-CMP-lmstudio](#rt-cmp-lmstudio)).

A query invocation supplies one CLI argument. The script creates a query embedding, requests up to 50 embedded chunks for the CLI's final limit of ten, orders by cosine similarity, deduplicates parent document IDs, reloads full roots and sorts them by their best selected chunk score. The terminal output is source, creator, optional URL, full root content and score. Only query text is supplied to the embedding model; retrieved documents are not subsequently placed into a generative answer context. Selection is approximate at the document level because the initial chunk window can be dominated by a few roots. The code does not promise ten distinct documents or a relevance threshold ([RT-RTE-query-documents](#rt-rte-query-documents)).

### Controls and forcing cases

The capability surface is process-level local database/filesystem access and explicit network calls. Current grants are not inferable from code: local file permissions, provider credentials, Supabase policy, browser permissions and Nomic account access are external contracts. The code requests those effects as the invoking user or browser. This is not evidence of a deployed isolation envelope. The URL-key browser tool has a separate credential and provider path from local LMStudio ([RT-RTE-compare-texts](#rt-rte-compare-texts)). No claim that a single model-call wrapper enforces controls across both paths is warranted.

Three forcing cases bound the main account:

1. **Non-null selection is not embedding freshness or eventual success.** The embedding driver's SQL predicate excludes non-null embeddings; the explicit clearing script can null them again. A failed batch still advances the cursor. Changing the configured model does not itself invalidate previously stored vectors. Owner: embedding script. Enforcement: SQL null predicate at fetch time. Guarantee strength: protocol, limited to that driver's selection; implementation conclusion status: wired; operation conclusion status: uninspected. Required external contracts: database predicate semantics, provider output ordering/cardinality and compatible dimensions. Clearing, direct database edits and changed provider resolution fall outside a freshness guarantee. No cross-process reservation is shown ([RT-RTE-embed-chunks](#rt-rte-embed-chunks), [RT-RTE-clear-embeddings](#rt-rte-clear-embeddings)).
2. **A second ingestion route admits without archive filtering.** RSS converts HTML to Markdown and applies its own field checks, then inserts roots and chunks. The archive's retweet/thread rules do not protect this route. Both use fresh IDs; checksum storage does not become duplicate rejection because neither inspected loader queries it before insertion. RSS computes converted content before checking whether the encoded content exists, so its later skip check is not a guarantee against converter failures. Owner: each loader; enforcement: local conditional rules; guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. Parser/converter behavior and database success are external contracts. Neither route establishes semantic truth or retrieval quality ([RT-RTE-ingest-documents](#rt-rte-ingest-documents)).
3. **Persistence is not proof of working downstream integration.** Canvas assumes string/JSON embeddings, a fixed database location and a generated filename that differs from the browser request. The Nomic exporter uses an obsolete document-level embedding schema and an unbound database URL on its normal environment-present path. These are source-visible obstacles, not experimental failures and not reasons to remove shipped paths from scope ([RT-RTE-display-export](#rt-rte-display-export)).

Permissions, approval, shell execution and extension mechanisms matter here principally as external operator powers, not model powers. The inspected scripts contain fixed actions and explicit model embedding calls; they do not expose model-selected tools, shell commands, host callbacks, delegation or remote workers through those calls. Arbitrary operator changes to scripts/configuration are a different authority path ([RT-BAP-operator-config](#rt-bap-operator-config)). This bounded account does not establish what a surrounding deployment adds. The shipped UI App is a local counter scaffold, not another implemented query controller (SRC-1, `apps/semantic-engine-ui/src/App.tsx`).

### Change admission and recovery

Retained-knowledge admission is implemented by the two ingestion drivers; derived-vector admission by the embedding driver; removal by the clearing driver. Their route records separate human initiation from automatic per-item decisions. None of these writes constitutes model-parameter training. Product and production-machinery changes are available through ordinary source/configuration edits and operator-run schema push, not a traced evidence-responsive product revision loop. Schema configuration points `drizzle-kit push` at the selected dataset, but this account does not infer confirmation, migration safety or rollback guarantees from uninspected dependency internals (SRC-1, `apps/semantic-engine-cli/drizzle.config.ts`, `apps/semantic-engine-cli/package.json`). No formulated-theory revision is attributed to numerical embedding, scoring or PCA. Memory revision analysis is left to the memory member.

## Shared records

### Components

#### RT-CMP-lmstudio
Label: LMStudio embedding model

Source-native identity: `lmstudio.textEmbeddingModel`, using `LMSTUDIO_EMBEDDING_MODEL`. Distributed-parametric model behind an OpenAI-compatible HTTP endpoint; weights reside in external LMStudio-managed storage, not the repository or SQLite. Both embedding and query routes use `http://localhost:1234/v1`. Parameters changing during operation: uninspected provider internals; neither inspected caller requests training or parameter updates. Exact version pinned: no immutable model/weights digest; the environment template supplies a model name. Mutable endpoint can resolve to another model: yes, server/environment selection is outside the stored vectors and no model identity is recorded in the chunk schema. Cross-call compatibility is an external requirement, not enforced by the shared variable name (SRC-1, `apps/semantic-engine-cli/.env.template`, `apps/semantic-engine-cli/db/schema.ts`).

> const lmstudio = createOpenAICompatible({
>     name: 'lmstudio',
>     baseURL: 'http://localhost:1234/v1',
> });
> --- `apps/semantic-engine-cli/scripts/query-documents.mts`

#### RT-CMP-openai
Label: OpenAI text embedding model

Distributed-parametric `text-embedding-3-large`, remotely hosted by OpenAI; storage substrate and provider internals uninspected. Parameters changing during operation: caller does not request updates; provider-internal changes uninspected. Exact version pinned: no, a service model name rather than immutable weights/version. Mutable endpoint can resolve to another implementation: service-side resolution remains outside the frozen repository. Used only by the separate similarity page in this inspected account (SRC-1, `apps/knowledge-gate/index.html`).

> 'model': 'text-embedding-3-large',
> 'encoding_format': 'float'
> --- `apps/knowledge-gate/index.html`

### Operative objects

#### RT-OBJ-docs-chunks
Label: docs and chunks

Source-native identity: SQLite `docs` and `chunks` tables in `file:${process.env.DATASET_ID}.sqlite`. Natural-language document and chunk content is interpreted by people and embedding models. IDs, provenance fields, offsets and table relations are symbolic data consumed by fixed program rules. Dense embeddings are distributed-parametric numerical representations stored in a declared 768-dimensional vector column; they are derived values, not changes to embedding-model weights. These distinct parts have different consumers: query ranking reads chunk vectors, then reloads root content. Stored checksum has no rejection consumer in the inspected loaders. The Drizzle relation describes a parent lookup; this declaration does not infer a database-enforced foreign key from it (SRC-1, `apps/semantic-engine-cli/db/db.ts`, `apps/semantic-engine-cli/db/schema.ts`, `apps/semantic-engine-cli/db/types/vector.ts`).

> docId: text().notNull(),            // Reference to root document
> embedding: vector32({ dimensions: 768 }),
> content: text().notNull(),
> --- `apps/semantic-engine-cli/db/schema.ts`

### Routes

#### RT-RTE-ingest-documents
Label: Archive and RSS admission

Operator paths or feed URL → parsed external material → constructed roots → `splitText` chunks → separate database insertion batches. Owner/next-step policy: fixed loader code, not a model. Source authors propose content; the operator selects a source, not each admitted item. Archive filtering/thread reconstruction and RSS field checks decide admission automatically. Human veto is withholding an invocation or changing its inputs; no per-item approval screen is wired. Operating mode: open source ingestion, not a bounded experiment or improvement curriculum. Answer oracle: none used for admission; a stored hash is not an expected answer. Guidance is the fixed extraction/chunking code; source text and derived chunks persist, not a revised methodology. Recovery: archive missing files are skipped; RSS errors exit; insertion phases have no enclosing transaction or driver rollback. Fresh IDs and no checksum lookup mean reimport is not source-level deduplication. Split size is 512 JavaScript string units, not a model token-budget guarantee (SRC-1, `apps/semantic-engine-cli/scripts/load-archives.mts`, `apps/semantic-engine-cli/scripts/load-from-rss.mts`, `apps/semantic-engine-cli/lib/utils/split-text.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: database insertion effects and progress/totals on stdout; errors as described above.
- Later read-back: roots/chunks feed embedding and query invocations in the selected dataset.
- Delegated visibility: inapplicable — no agent delegation; external RSS fetch supplies input rather than delegated reasoning.
- Selection predicate: archive excludes text beginning RT and replies to other users; orphan reply chains are dropped; RSS requires encoded content and link/guid, subject to conversion occurring first.
- Invalidation or expiry: no automatic expiry or replacement keyed by external ID in either driver.
- Activation or effect: code inserts roots and chunks; exercised insertion and later influence remain unobserved.
- Evidence limits: provider/parser behavior, corpus provenance and successful atomic completion are not established.

> if (tweet.full_text.startsWith('RT')) return false
> --- `apps/semantic-engine-cli/scripts/load-archives.mts`

> const parentThread = threadMap[replyToId];
> if (!parentThread) return threadMap
> --- `apps/semantic-engine-cli/scripts/load-archives.mts`

> const contentToProcess = `# ${item.title}` + '\n\n' + turndownService.turndown(item["content:encoded"]) || '';
> --- `apps/semantic-engine-cli/scripts/load-from-rss.mts`

#### RT-RTE-embed-chunks
Label: Embed unembedded chunks

Chunk rows → AI SDK `embedMany` → SQL CASE update keyed by chunk ID. Operator initiates; loader state proposes null rows; code admits any nonempty returned embeddings array into its update construction without a human review or answer oracle. No explicit equality check between batch size and vector count is present. Operating mode: batch derivation, default 100, not adaptive experimentation. Guidance: unchanged driver and configured model; retained result is numerical embeddings. Rollback: no previous vector version retained here; failure logs and cursor progression are explicit. A fresh run starts the cursor anew and can revisit null rows (SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: per-batch update/logs and total processed count.
- Later read-back: stored embeddings are selected by query and intended display/export consumers.
- Delegated visibility: inapplicable — the provider is a numerical computation endpoint, not a delegated agent with tools.
- Selection predicate: embedding IS NULL, ascending ID and ID greater than cursor where supplied.
- Invalidation or expiry: non-null rows are not refreshed here; clearing can make them eligible again; no model-version invalidation.
- Activation or effect: code writes vectors to chunks; later ranking dependence is wired, not observed.
- Evidence limits: output ordering, count, dimensions, provider quality and successful writes are external/unobserved requirements.

> // We will still advance to the next prefetched batch even if this one failed.
> --- `apps/semantic-engine-cli/scripts/embed-documents.mts`

> model: lmstudio.textEmbeddingModel(process.env.LMSTUDIO_EMBEDDING_MODEL!),
> values: currentChunks.map(chunk => chunk.content),
> --- `apps/semantic-engine-cli/scripts/embed-documents.mts`

#### RT-RTE-query-documents
Label: Query root documents

CLI query → LMStudio embedding → cosine-ranked non-null chunks → unique root IDs → root row reload → sorted terminal output. Owner: deterministic script. Model supplies a vector, SQL supplies scores, code performs candidate selection; the human chooses the query and can disregard output, but no human veto occurs inside ranking. Operating mode: open query, no improvement trigger or reference-answer oracle. Similarity is a selector, not correctness adjudication (SRC-1, `apps/semantic-engine-cli/scripts/query-documents.mts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: up to ten full root documents and their best selected chunk scores printed to stdout; empty results message or propagated error otherwise.
- Later read-back: inapplicable — the query driver does not persist queries, ranked results or feedback.
- Delegated visibility: inapplicable — no downstream answer agent receives the selected text in this driver.
- Selection predicate: non-null embeddings, descending cosine score, initial limit five times requested roots, then unique parent IDs and database reload.
- Invalidation or expiry: current query vector/results are invocation-local; stored vectors have no freshness filter.
- Activation or effect: stored vectors affect implemented ranking and stored root text supplies displayed content; successful relevance and user benefit unobserved.
- Evidence limits: database/vector compatibility and provider behavior unobserved; a limited chunk window need not yield ten distinct roots or the globally best ten roots.

> const initialChunkLimit = limit * 5;
> --- `apps/semantic-engine-cli/scripts/query-documents.mts`

> similarity: sql<number>`1 - vector_distance_cos(${chunksTable.embedding}, vector32(${JSON.stringify(embedding)})) as similarity`,
> --- `apps/semantic-engine-cli/scripts/query-documents.mts`

#### RT-RTE-clear-embeddings
Label: Clear stored embeddings

Operator invocation → update non-null chunk embeddings to null → affected-row log. Admission/change roles: operator authorizes a dataset-wide removal; fixed SQL decides affected rows, with no model, per-row approval or answer oracle. Operating mode: manual maintenance; no evidence-driven improvement trigger. Proposed change is removal of derived vectors, not text or weights. Recovery requires recomputation or an external backup; this script retains no rollback copy (SRC-1, `apps/semantic-engine-cli/scripts/clear-all-embeddings.mts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: affected row count printed.
- Later read-back: query excludes the null rows; embedding invocation can select them for recomputation.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: embedding IS NOT NULL in the environment-selected dataset.
- Invalidation or expiry: explicit nulling; no timer or automatic model-change trigger.
- Activation or effect: removal is wired to vector eligibility; execution unobserved.
- Evidence limits: no confirmation or backup protocol is implemented in this file; deployment access rights remain external.

> embedding: null
> --- `apps/semantic-engine-cli/scripts/clear-all-embeddings.mts`

#### RT-RTE-display-export
Label: Canvas and Atlas consumers

Two distinct downstream consumer implementations are grouped here only as forcing alternatives to CLI retrieval, not as one functioning chain. Canvas owner is a fixed local processor and browser event handlers: hardcoded author → joined document/chunk rows → parsed vectors → centered/scaled PCA → GeoJSON → map points/labels and tweet links. Nomic owner is a Python driver: ORM document query → metadata/vector arrays → `atlas.map_data`. These transform/export existing content, not approve database content or improve models. No candidate oracle is used. Operating mode: operator-run projection/export, with no improvement trigger or revision loop (SRC-1, `apps/infinite-canvas-viewer/process-embeddings.mjs`, `apps/infinite-canvas-viewer/pca.js`, `apps/infinite-canvas-viewer/src/index.js`, `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py`, `apps/semantic-engine-cli/db/models.py`).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: intended GeoJSON file/map display or remote Atlas dataset; processor logs errors, exporter has catch-and-exit handling for errors inside its try block.
- Later read-back: browser requests a per-username GeoJSON file; Atlas later consumption is outside inspected implementation.
- Delegated visibility: Nomic receives supplied metadata, text and vectors if export reaches the service; no delegated agent protocol is shown.
- Selection predicate: canvas author equality with hardcoded DefenderOfBasic, no non-null vector filter; Atlas ORM requests non-null document-level embeddings in its own schema.
- Invalidation or expiry: GeoJSON write replaces its output filename; no synchronized regeneration or Atlas rollback protocol established.
- Activation or effect: plotting/export call sites exist, but schema, representation and path mismatches prevent asserting a connected shipped pipeline.
- Evidence limits: the runtime never tested these paths; external Atlas processing, generated files and PCA quality remain unobserved.

Canvas opens `../semantic-engine.sqlite` relative to its directory, rather than the CLI's working-directory/environment-selected file. Its `.substring` and `JSON.parse` assumptions do not decode the current declared F32_BLOB representation. It writes a `-test` filename while the browser requests one without that suffix. PCA fits the input corpus and rescales two components; this is a numerical projection, not embedding-model training. Joined `SELECT *` does not explicitly disambiguate both content columns for the displayed text (SRC-1, processor, PCA and schema paths above).

> fs.writeFileSync(`public/${username.toLowerCase()}-test.geojson`, JSON.stringify(geojson, null, 2));
> --- `apps/infinite-canvas-viewer/process-embeddings.mjs`

> const geojsonDataResponse = await fetch(`./${username}.geojson`)
> --- `apps/infinite-canvas-viewer/src/index.js`

In the exporter `db_url` is indented within the missing-environment branch after `sys.exit(1)`, leaving it unassigned on the ordinary environment-present path. The ORM also expects `docs.embedding`, `source` and `creatorId`, unlike the current TS schema's chunk embeddings, origin and author. These independent mismatches qualify the README's export instruction; they do not prove all conceivable legacy databases fail.

> session = get_session(db_url)
> --- `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py`

> embedding = Column(Vector32(dimensions=768))
> --- `apps/semantic-engine-cli/db/models.py`

#### RT-RTE-compare-texts
Label: Browser text comparison

Page load or debounced textarea input → two sequential OpenAI embedding requests → local cosine computation → DOM similarity display. Principal: browser user; next-step owner: fixed JavaScript. Key is read from URL query parameter `key`, not the CLI environment. This route bypasses the document store and LMStudio. It compares candidates numerically but makes no storage/admission decision. Operating mode: open pair comparison. Answer oracle: none; numerical similarity is the output, not a reference correctness outcome (SRC-1, `apps/knowledge-gate/index.html`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: displayed cosine similarity rounded to six decimals.
- Later read-back: inapplicable — no retained comparison result or corpus write in the page.
- Delegated visibility: both textarea contents are sent to OpenAI; no agent handoff.
- Selection predicate: current contents of the two textareas after 500ms debounce; initial contents compared on load.
- Invalidation or expiry: shared timeout cancels pending callbacks, not already-running requests; no result-version or cancellation check protects against overlapping completions.
- Activation or effect: code displays numerical comparison, not document acceptance; successful operation unobserved.
- Evidence limits: browser/network/provider grants and response success unobserved; code reads response data without an explicit status check or retry.

> const response = await fetch('https://api.openai.com/v1/embeddings', {
> --- `apps/knowledge-gate/index.html`

### Claims

#### RT-CLM-pipeline-purpose
Label: Modular semantic pipeline

Claimed operation: ingest, embed and visualize diverse documents and relationships. Source is doctrine/design, not a successful integration trace. Query implementation supplies retrieval without generative answering; display/export integration is qualified in its route record (SRC-1, `README.md`, `apps/semantic-engine-cli/README.md`).

> The ORI semantic engine is a modular pipeline for ingesting, embedding and visualizing diverse documents and their relationships to each-other
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-operator-config
Label: Operator-selected model and dataset

Consumer: CLI drivers, database connection and schema tool. Channel: environment variables, source files and operator-selected commands. Force: symbolic configuration chooses a database filename and model identifier; fixed source code determines transformations and SQL. Horizon: later invocations using that environment/source, without an implemented evidence-responsive self-edit loop. The environment template provides defaults, not evidence of current grants or model immutability. Operator-run schema push admits production-schema changes via external tooling; neither automated proposal generation nor a built-in rollback is established (SRC-1, `apps/semantic-engine-cli/.env.template`, `apps/semantic-engine-cli/db/db.ts`, `apps/semantic-engine-cli/drizzle.config.ts`, `apps/semantic-engine-cli/package.json`).

> export const db = drizzle(`file:${process.env.DATASET_ID}.sqlite`!);
> --- `apps/semantic-engine-cli/db/db.ts`

#### RT-BAP-vector-ranking
Label: Stored vectors shape retrieval

Consumer: query SQL and root-selection code. Channel: retained chunk embedding values, generated query vector and cosine-distance expression. Force: numerical scores order candidates and thereby select which root texts reach terminal output; they are not instructions or a truth warrant. Horizon: later query invocations until clearing, overwrite or database replacement. Numerical embeddings are durable behavior-shaping inputs to retrieval, but this establishes neither learning benefit nor an exercised self-improvement chain. The update consumer and downstream selection consumer are distinct (SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts`, `apps/semantic-engine-cli/scripts/query-documents.mts`).

> .orderBy(desc(sql`similarity`))
> .limit(initialChunkLimit);
> --- `apps/semantic-engine-cli/scripts/query-documents.mts`

## Annotations

none
