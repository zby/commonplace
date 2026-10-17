---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Semantic Engine workflow account: operator-driven Community Archive ingestion through embedded-chunk retrieval and terminal delivery."
run-id: AAS-2026-10-17-semantic-engine-666c064cd8dc-01
reviewed-boundary: "7e2481671cad01f0b4c89f2a1877d6733d7e552c"
---

# Semantic Engine workflow report

## Workflow account

### Selected workflow and evidence limit

The representative workflow is the CLI quickstart: an operator selects a Community Archive corpus, downloads and loads it, embeds its chunks, and submits a query that returns root documents. It is selected because the shipped README explicitly connects these steps, and the implementation supplies the persistent handoffs. It is a multi-step computation involving embedding models, not an established multi-agent workflow. The scripts, rather than a reasoning agent, decide the next actions. No agent delegation, reviewer-agent acceptance, or generated answer is established within this chain ([RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents), [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks), [RT-RTE-query-documents](runtime.md#rt-rte-query-documents)).

The operating instructions explicitly separate embedding from querying:

> bun scripts/embed-documents.mts
> --- `apps/semantic-engine-cli/README.md`

> bun scripts/query-documents.mts "query: what is the meaning of memetics?"
> --- `apps/semantic-engine-cli/README.md`

Evidence is SRC-1 implementation and doctrine/design at the frozen commit in [boundary](boundary.md). This member inspected the CLI README, download, archive-load, embedding and query scripts, and `apps/semantic-engine-cli/lib/utils/split-text.ts`, all within the registered coverage. No added source or functional exclusion is needed. No target code, tests, providers or services were executed. The account establishes source-level wiring, not successful completion or retrieval effectiveness.

### Request, acquisition and admission

The human supplies the workflow's initial purpose and chooses usernames, archive paths, dataset configuration and ultimately query text. The README requires dependency installation, database initialization and an LMStudio server/model setup. These are operator responsibilities, not work automatically assigned to another agent. Dataset configuration determines which SQLite file later invocations share ([RT-BAP-operator-config](runtime.md#rt-bap-operator-config); SRC-1, `apps/semantic-engine-cli/README.md`).

The first concrete handoff is from the download script to local archive files. It lowercases requested usernames, lists Supabase storage objects, filters by username when provided, and downloads with bounded concurrency. Existing local files are skipped, so acquisition does not ensure refresh. A download error is caught for that item and the loop continues; therefore its final completion message is not an all-items-success certificate (SRC-1, `apps/semantic-engine-cli/scripts/download-archives.mts`).

> console.error('error downloading', filename, '. Skipping...')
> --- `apps/semantic-engine-cli/scripts/download-archives.mts`

The operator invokes the loader with explicit archive paths. There is no direct downloader-to-loader scheduler: filesystem output and the next human command connect them. The loader skips missing files, parses available JSON, filters retweets and replies to other users, sorts by time, and builds threads. A reply with no retained parent is dropped. These fixed rules can reject input; they do not verify its factual accuracy, and initiating the loader is not per-document human approval ([RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents); SRC-1, `apps/semantic-engine-cli/scripts/load-archives.mts`).

For admitted threads, the loader creates fresh root IDs, stores source attribution and content hashes, inserts root documents, and then inserts chunks linked by root ID. The chunker uses a 512-JavaScript-string-unit size with prioritized separators, not a model-token accounting policy. Thus the embedding model receives portions of reconstructed thread text, not the raw archive or every original tweet field. Query delivery later reloads the root text rather than reconstructing it from those chunks (SRC-1, `apps/semantic-engine-cli/scripts/load-archives.mts`, `apps/semantic-engine-cli/lib/utils/split-text.ts`; [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks)).

Root and chunk inserts are separate batches without a driver-level transaction spanning both phases. A failure can interrupt this handoff after some writes. Re-running is not an implemented repair protocol: fresh IDs and the lack of checksum lookup permit duplicate roots rather than proving idempotent recovery ([RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents)).

### Embedding handoff, acceptance and recovery

A new operator invocation reads null-embedding chunks in ascending ID order. The embedding script sends an ordered content array to LMStudio and uses returned vector positions to construct updates keyed by chunk ID. The provider supplies numerical embeddings, not instructions for the next step or delegated reasoning with tools. The script owns pagination, prefetch, update construction and continuation ([RT-CMP-lmstudio](runtime.md#rt-cmp-lmstudio), [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks)).

The admission check is only a nonempty embeddings array before building the update. No explicit equality check confirms that every selected chunk has a corresponding vector, and no human or reference-answer oracle accepts embedding quality. Provider ordering, cardinality and compatible dimensions remain external requirements, not validated workflow guarantees ([RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks); SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts`).

The failure branch preserves forward progress at the cost of completeness: embedding or update errors inside the batch try block are logged, then processing advances to the prefetched next batch. It does not retry that failed batch in the same invocation. The existing runtime record supplies the verbatim continuation rule. A fresh invocation starts without a cursor and can revisit rows still null. Prefetch/initial-fetch errors outside that batch try block instead reach the top-level failure handler. Consequently “No more chunks to embed” describes reaching the end of this cursor traversal; after skipped failures it does not prove that no null rows remain (SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts`; [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks)).

Non-null stored vectors make chunks eligible for later query selection. They do not carry a pinned model identity or automatic freshness check. An operator changing the configured model must not infer compatible old vectors merely from a shared environment-variable name. The separate clearing route can null vectors for recomputation; it retains no rollback copy ([RT-CMP-lmstudio](runtime.md#rt-cmp-lmstudio), [RT-RTE-clear-embeddings](runtime.md#rt-rte-clear-embeddings)).

### Query selection and delivered result

The final handoff is database read-back in a separate query invocation. The human supplies one query string. Only that string goes to LMStudio for a query embedding. SQL scores non-null chunk vectors by cosine similarity and returns at most 50 candidates for the CLI's ten-root limit. Code deduplicates parent IDs, reloads roots and sorts by selected chunk scores. The model neither chooses tools nor reviews the selected documents ([RT-RTE-query-documents](runtime.md#rt-rte-query-documents), [RT-BAP-vector-ranking](runtime.md#rt-bap-vector-ranking)).

The reload preserves full root content for delivery:

> const displayContent = doc.content;
> --- `apps/semantic-engine-cli/scripts/query-documents.mts`

Ranking is selection, not verification. No correctness oracle, minimum relevance threshold, reviewer decision or user-feedback loop intervenes between candidate scores and display. The finite chunk window can contain many chunks from the same root, so the implementation does not guarantee ten distinct results or the globally best ten roots. There is no subsequent generative answer step ([RT-RTE-query-documents](runtime.md#rt-rte-query-documents)).

Delivery in this workflow means printing ranked root content, similarity, origin, author and optional URL to the invoking terminal. It does not mean a reviewer accepted the answer or a downstream agent consumed it. Missing query input exits with an error; an empty candidate set produces “No results found”; provider/database failures are logged and propagated to the top-level exit handler. Query results and feedback are not retained for later improvement (SRC-1, `apps/semantic-engine-cli/scripts/query-documents.mts`; [RT-RTE-query-documents](runtime.md#rt-rte-query-documents)).

The operator therefore owns cross-command continuation and recovery. File existence, database writes and terminal output are the concrete handoff artifacts; there is no inspected end-to-end success gate. The separate Atlas/canvas paths are not needed to complete this selected terminal-retrieval workflow and are not silently joined to it; their integration obstacles remain in [RT-RTE-display-export](runtime.md#rt-rte-display-export). Source wiring establishes neither that an operator completed this sequence nor that its results were useful.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents)

Workflow handoff: the selected archive branch starts only after a separate download command or an already available archive file. Its database writes supply the next command's work, not a delegated-agent response. Operator intervention is required to proceed to embedding. Partial insertion and duplicate-producing reimport limit recovery, so loader completion is not a corpus-replacement guarantee.

#### On [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks)

Workflow checkpoint: reaching the cursor's end is weaker than complete embedding coverage because failed batches are skipped. The next query can consume the successfully retained subset without an intervening coverage gate. A fresh embedding invocation, not the current batch loop, owns the available revisit path for still-null rows.

#### On [RT-RTE-query-documents](runtime.md#rt-rte-query-documents)

Workflow delivery criterion: terminal emission of source documents completes the selected retrieval command; it is not answer acceptance. The root reload is the consequential expansion from selected chunk evidence to delivered full text. There is no delivered agent work product beyond this document listing in the inspected CLI chain.
