---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Semantic Engine epistemic routes: imported assertions, numerical selection, checks and downstream authority at the frozen revision."
run-id: AAS-2026-10-17-semantic-engine-666c064cd8dc-01
reviewed-boundary: "7e2481671cad01f0b4c89f2a1877d6733d7e552c"
---

# Semantic Engine epistemic report

## Source-and-claim boundary

The question is whether ingestion, embedding, comparison and visualization produce or warrant knowledge, rather than merely admit and select source material. Scope and exclusions are those of the [boundary and Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation. The public pipeline claim is [RT-CLM-pipeline-purpose](runtime.md#rt-clm-pipeline-purpose); the narrower RAG label is [EPI-CLM-rag-quickstart](#epi-clm-rag-quickstart). Neither claims universal factual correctness.

The assessed families are acquisition, text transformation, software admission, numerical comparison and selection, retention, withdrawal, projection/export, authored chunking checks, and the optional clustering helper. These are separate functions, not stages of one demonstrated acceptance loop. An imported text may contain factual assertions, questions, fiction or instructions. No supplied corpus lets this analysis individuate its actual propositions or warrant. The absence of a corpus prevents a judgment about acquired claim truth, not inspection of the routes.

Missing provider implementations and immutable weights prevent conclusions about embedding semantics, training history or internal learning. Missing execution traces prevent claims that these routes operated, that exports succeeded, or that results were useful. Missing reference relevance judgments, source verification and controlled interventions prevent retrieval-quality and causal-benefit conclusions. The excluded cluster-results sample is not used as a run trace. Dependency internals and raw OpenAPI remain outside inspected behavioral evidence; no provider or dependency guarantee is inferred.

| Entry point or operation | Source path in SRC-1 | Coverage and records |
| --- | --- | --- |
| Root/app dispatch, DB initialization, login | `package.json`; `apps/semantic-engine-cli/package.json`; `apps/infinite-canvas-viewer/package.json`; `apps/semantic-engine-ui/package.json` | Direct reads: empty root scripts, schema/login commands, Vite/build/lint surfaces; no registered model-selected tools or hook dispatcher found here. Operator configuration: see [RT-BAP-operator-config](runtime.md#rt-bap-operator-config). |
| Download archives | `apps/semantic-engine-cli/scripts/download-archives.mts` | Supplied runtime finding, not independently reread: see [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents) and runtime account. Download alone grants no claim warrant. |
| Archive/RSS loading | `apps/semantic-engine-cli/scripts/load-archives.mts`; `apps/semantic-engine-cli/scripts/load-from-rss.mts` | Direct reads: see [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents), [EPI-RTE-source-reshaping](#epi-rte-source-reshaping). |
| Chunking and authored tests | `apps/semantic-engine-cli/lib/utils/split-text.ts`; `apps/semantic-engine-cli/lib/utils/split-text.test.ts` | Direct reads: see [EPI-RTE-split-text](#epi-rte-split-text), [EPI-RTE-chunk-tests](#epi-rte-chunk-tests). |
| Storage, embedding and query | `apps/semantic-engine-cli/db/schema.ts`; `apps/semantic-engine-cli/scripts/embed-documents.mts`; `apps/semantic-engine-cli/scripts/query-documents.mts` | Direct reads: see [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks), [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks), [RT-RTE-query-documents](runtime.md#rt-rte-query-documents). Vector adapter and DB connection assessed through supplied runtime. |
| Clear embeddings | `apps/semantic-engine-cli/scripts/clear-all-embeddings.mts` | Supplied runtime finding: see [RT-RTE-clear-embeddings](runtime.md#rt-rte-clear-embeddings). |
| Canvas PCA/display | `apps/infinite-canvas-viewer/process-embeddings.mjs`; `apps/infinite-canvas-viewer/pca.js`; `apps/infinite-canvas-viewer/src/index.js` | Processor/PCA directly read; browser consumer supplied runtime finding: see [RT-RTE-display-export](runtime.md#rt-rte-display-export). |
| Optional clustering and SSE | `apps/infinite-canvas-viewer/cluster.js` | Direct read: see [EPI-RTE-cluster-items](#epi-rte-cluster-items). Not an active invocation in processor. |
| Atlas export/topic request | `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py`; `apps/semantic-engine-cli/db/models.py` | Exporter directly read, ORM through runtime: see [RT-RTE-display-export](runtime.md#rt-rte-display-export), [EPI-RTE-atlas-topics](#epi-rte-atlas-topics). Added inspection exposes topic-model request omitted from runtime's numerical-export summary. |
| Independent browser comparison | `apps/knowledge-gate/index.html` | Direct read, including numerical guards: see [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts), [EPI-RTE-cosine-guards](#epi-rte-cosine-guards). |
| UI scaffold | `apps/semantic-engine-ui/src/App.tsx` | Supplied runtime finding: counter, not corpus consumer; no additional epistemic route established. |

Search and reads deliberately included possible counterexamples to a mere-retrieval account: test assertions, numerical guards, metadata construction, clustering/SSE, and the Atlas topic request. They establish bounded checks and a requested opaque downstream operation, not factual acceptance. Supporting configuration/assets not behaviorally audited remain as distinguished in the boundary; this report does not claim an exhaustive negative over dependency, host or provider internals.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-docs-content](#epi-obj-docs-content) | Imported document assertions when present | see record | SRC-1, `apps/semantic-engine-cli/scripts/load-archives.mts` | Actual corpus and claim truth not determinable |
| [EPI-OBJ-chunks-content](#epi-obj-chunks-content) | Text fragments; not necessarily complete propositions | see record | SRC-1, `apps/semantic-engine-cli/lib/utils/split-text.ts` | Collection-level preservation does not give each fragment independent warrant |
| [EPI-OBJ-docs-metadata](#epi-obj-docs-metadata) | Provenance/date/author assertions and symbolic lookup fields | see record | SRC-1, `apps/semantic-engine-cli/scripts/load-from-rss.mts` | Fallback author/date are not verified original authorship/publication time |
| [EPI-OBJ-chunks-embedding](#epi-obj-chunks-embedding) | None individually identified; dense numerical state | see record | SRC-1, `apps/semantic-engine-cli/db/schema.ts` | Model semantics opaque; not a formulated claim or weight update |
| [RT-RTE-query-documents](runtime.md#rt-rte-query-documents) | Invocation-local numerical similarity and selected source text | see record | SRC-1, `apps/semantic-engine-cli/scripts/query-documents.mts` | Score is about supplied vectors, not truth of selected document |
| [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts) | Invocation-local cosine value for two supplied texts | see record | SRC-1, `apps/knowledge-gate/index.html` | No calibrated semantic-equivalence or factual-correctness criterion |
| [RT-RTE-display-export](runtime.md#rt-rte-display-export) | Derived plot coordinates plus copied text/IDs | see record | SRC-1, `apps/infinite-canvas-viewer/pca.js` | Synthetic coordinates are not geographic assertions or verified semantic relations |
| [EPI-RTE-atlas-topics](#epi-rte-atlas-topics) | Not determinable: provider topic output unavailable | see record | SRC-1, `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py` | Request only; no labels, propositions, evaluation or later local consumer supplied |
| [EPI-RTE-cluster-items](#epi-rte-cluster-items) | Grouped source text and numerical SSE; no formulated explanation | see record | SRC-1, `apps/infinite-canvas-viewer/cluster.js` | Optional helper, not demonstrated grouping or semantic validation |

## Authority-route ledger

Fields owned by supplied records are referred to rather than redeclared. Every implemented status below is source-level; no observed run is established.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents) | content transformation | implemented | [EPI-OBJ-docs-content](#epi-obj-docs-content) | truth-apt transformation: acquisition/import | External text enters roots | see route | see route | see route | see route | Source warrant unknown; no verification added | see route | see route | SRC-1, `apps/semantic-engine-cli/scripts/load-archives.mts` | [RT-CLM-pipeline-purpose](runtime.md#rt-clm-pipeline-purpose) | none | Conditional on truth-apt source content; acquisition is not production |
| [EPI-RTE-source-reshaping](#epi-rte-source-reshaping) | content transformation | implemented | [EPI-OBJ-docs-content](#epi-obj-docs-content), [EPI-OBJ-docs-metadata](#epi-obj-docs-metadata) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | No truth license from aggregation, conversion or fallback fields | see record | see record | SRC-1, `apps/semantic-engine-cli/scripts/load-from-rss.mts` | none | none | Text copying/grouping and metadata synthesis differ; see record |
| [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents) | disposition/acceptance | implemented | [EPI-OBJ-docs-content](#epi-obj-docs-content) | no content change | Operational admission, not epistemic acceptance | see route | see route | see route | see route | None beyond input-selection rules | see route | see route | SRC-1, `apps/semantic-engine-cli/scripts/load-archives.mts` | none | none | Excluding RT/replies or missing fields does not check a proposition |
| [EPI-RTE-split-text](#epi-rte-split-text) | content transformation | implemented | [EPI-OBJ-chunks-content](#epi-obj-chunks-content) | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Text preservation as ordered collection only | see record | see record | SRC-1, `apps/semantic-engine-cli/lib/utils/split-text.ts` | none | none | No assertion-level entailment for isolated fragments |
| [EPI-RTE-chunk-tests](#epi-rte-chunk-tests) | check/evidence production | implemented | [EPI-OBJ-chunks-content](#epi-obj-chunks-content) | no content change | Chunker behavior on authored fixtures | see record | see record | see record | see record | Fixture comparisons only; not source truth or retrieval relevance | see record | see record | SRC-1, `apps/semantic-engine-cli/lib/utils/split-text.test.ts` | none | none | No observed test run or admission consumer |
| [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents) | retention | implemented | [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks) | no content change | see route | see route | see route | see route | see route | Storage is not acceptance | see route | see route | SRC-1, `apps/semantic-engine-cli/db/schema.ts` | none | none | No evidence-consuming claim acceptance before storage |
| [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks) | content transformation | implemented | [EPI-OBJ-chunks-embedding](#epi-obj-chunks-embedding) | non-truth-apt policy/content update: dense vector encoding | see route | see route | see route | see route | see route | No individuated proposition licensed by vector generation | see route | see route | SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts` | [RT-CLM-pipeline-purpose](runtime.md#rt-clm-pipeline-purpose) | none | Semantic preservation not established; provider computation opaque |
| [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks) | operational admission/selection/consumption | implemented | [EPI-OBJ-chunks-embedding](#epi-obj-chunks-embedding) | no content change | Null-row selection and returned vector admission | see route | see route | see route | see route | Nonempty returned array is not quality validation | see route | see route | SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts` | none | none | No explicit count equality or model-version compatibility gate |
| [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks) | retention | implemented | [EPI-OBJ-chunks-embedding](#epi-obj-chunks-embedding) | no content change | see route | see route | see route | see route | see route | No acceptance inferred | see route | see [RT-BAP-vector-ranking](runtime.md#rt-bap-vector-ranking) | SRC-1, `apps/semantic-engine-cli/scripts/embed-documents.mts` | none | none | Retained derived values, not model training |
| [RT-RTE-query-documents](runtime.md#rt-rte-query-documents) | operational admission/selection/consumption | implemented | [EPI-OBJ-docs-content](#epi-obj-docs-content), [EPI-OBJ-chunks-embedding](#epi-obj-chunks-embedding) | no content change | Cosine rank then root selection | see route | see route | see route | ranking | No source-truth or complete-root relevance warrant | see route | see [RT-BAP-vector-ranking](runtime.md#rt-bap-vector-ranking) | SRC-1, `apps/semantic-engine-cli/scripts/query-documents.mts` | [EPI-CLM-rag-quickstart](#epi-clm-rag-quickstart) | Generation not implemented in this query route | Limited chunk window; no correctness threshold |
| [EPI-RTE-cosine-guards](#epi-rte-cosine-guards) | check/evidence production | implemented | [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts) | no content change | see record | see record | see record | see record | see record | Arithmetic preconditions only | see record | see record | SRC-1, `apps/knowledge-gate/index.html` | none | none | Does not validate text equivalence |
| [EPI-RTE-cosine-guards](#epi-rte-cosine-guards) | disposition/acceptance | implemented | [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts) | no content change | Reject unequal-length or zero-magnitude vectors | see record | see record | see record | enforcing | No epistemic claim acceptance | Throw prevents that calculation/display update | see record | SRC-1, `apps/knowledge-gate/index.html` | none | none | Guards are not exhaustive numeric validation |
| [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts) | content transformation | implemented | [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts) | truth-apt transformation: entailed derivation | Numeric cosine of returned vectors | Program arithmetic, nonzero equal-length finite vectors | see route | see route | advisory display | Conditional numeric result only; no warranted assertion about semantic identity | see route | see route | SRC-1, `apps/knowledge-gate/index.html` | none | none | Finite coordinates are assumed, not comprehensively checked |
| [RT-RTE-clear-embeddings](runtime.md#rt-rte-clear-embeddings) | lineage/freshness/recovery | implemented | [EPI-OBJ-chunks-embedding](#epi-obj-chunks-embedding) | non-truth-apt policy/content update: remove derived vectors | see route | see route | see route | see route | see route | No retraction of root assertions | see route | see route | SRC-1, `apps/semantic-engine-cli/scripts/clear-all-embeddings.mts` | none | none | Stops vector eligibility, not text retention or source endorsement |
| [RT-RTE-display-export](runtime.md#rt-rte-display-export) | content transformation | implemented | [RT-RTE-display-export](runtime.md#rt-rte-display-export) | non-truth-apt policy/content update: projection and plot encoding | see route | see route | see route | see route | display/export call sites | No verified semantic-neighborhood or geographic license | see route | see route | SRC-1, `apps/infinite-canvas-viewer/pca.js` | [RT-CLM-pipeline-purpose](runtime.md#rt-clm-pipeline-purpose) | Integration obstacles in record | Coordinates are corpus-dependent, with no quality threshold |
| [EPI-RTE-cluster-items](#epi-rte-cluster-items) | content transformation | implemented | [EPI-RTE-cluster-items](#epi-rte-cluster-items) | truth-apt transformation: non-ampliative reshaping | Group copied text by numeric cluster | see record | see record | see record | see record | Group membership not a tested conceptual theory | see record | see record | SRC-1, `apps/infinite-canvas-viewer/cluster.js` | none | none | Helper uninvoked by active processor |
| [EPI-RTE-cluster-items](#epi-rte-cluster-items) | check/evidence production | implemented | [EPI-RTE-cluster-items](#epi-rte-cluster-items) | no content change | SSE for k-means solutions | see record | see record | see record | diagnostic only | Within-vector squared distance, not truth or usefulness | No automatic winner/acceptance consumer found | see record | SRC-1, `apps/infinite-canvas-viewer/cluster.js` | none | none | Private exploration helper; no active call from exported cluster function |
| [EPI-RTE-atlas-topics](#epi-rte-atlas-topics) | content transformation | not determinable | [EPI-RTE-atlas-topics](#epi-rte-atlas-topics) | truth-apt transformation: indeterminate | see record | see record | see record | see record | external request only | None established | see record | see record | SRC-1, `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py` | none | Runtime summary needs qualification: requested topics also present | No output to classify as reshaping, entailed claim or conjecture |

No lifecycle-integration row is inferred from storage, ranking or topic-model configuration. The inspected admission and use paths give no evidence-consuming acceptance decision against a factual criterion for a named use/scope; the bounded negative is [EPI-ABS-claim-acceptance](#epi-abs-claim-acceptance).

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-pipeline-purpose](runtime.md#rt-clm-pipeline-purpose) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents), [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks), [RT-RTE-display-export](runtime.md#rt-rte-display-export) | None supplied | No intervention; independent schema/representation/path obstacles | Implemented acquisition, encoding and intended visualization responsibilities | Successful integrated pipeline and meaningful relationships unestablished; not an explicit truth guarantee |
| [EPI-CLM-rag-quickstart](#epi-clm-rag-quickstart) | see record | SRC-1, `apps/semantic-engine-cli/README.md`, doctrine/design | see record | [RT-RTE-query-documents](runtime.md#rt-rte-query-documents) | None supplied | No generation call after retrieval; no answer/relevance reference | Retrieval portion supported | If RAG denotes retrieval-augmented answer generation, generation is missing in the inspected CLI route; label alone is not a broader correctness claim |

## Bounded conclusion

Semantic Engine acquires external text and preserves source pointers, but its imported assertions carry unknown source warrant. Archive filtering, RSS field checks, hashing and storage do not add factual warrant. Source content, provenance metadata, fragments and vectors have different licenses: source text can express claims; metadata includes synthesized fallbacks; fragments can sever qualifying context; vectors drive ranking without stating inspectable propositions. See [EPI-OBJ-docs-content](#epi-obj-docs-content), [EPI-OBJ-docs-metadata](#epi-obj-docs-metadata), [EPI-RTE-split-text](#epi-rte-split-text) and [RT-BAP-vector-ranking](runtime.md#rt-bap-vector-ranking).

The numerical comparison route can derive a conditional arithmetic result about supplied vectors. Its guards enforce limited arithmetic preconditions; they do not evaluate whether either document is true or equivalent. Authored chunker tests compare outputs with expected fixture properties but are not wired into ingestion acceptance. SSE and PCA diagnostics also lack an operative factual-acceptance consumer. Thus checks exist, but their targets and force are narrower than knowledge validation: see [EPI-RTE-cosine-guards](#epi-rte-cosine-guards), [EPI-RTE-chunk-tests](#epi-rte-chunk-tests), [EPI-RTE-cluster-items](#epi-rte-cluster-items) and [RT-RTE-display-export](runtime.md#rt-rte-display-export).

Operational authority is concrete: automatically admitted text persists; stored chunk vectors order later query results; selected root text reaches terminal output; clearing removes vector eligibility until recomputation. These paths require no intervening truth check. Retention and use are therefore not evidence of accepted ampliative knowledge or post-acceptance lifecycle integration. No local route establishing those functions was found within the recorded search; the inaccessible provider route remains unresolved rather than negative ([EPI-ABS-claim-acceptance](#epi-abs-claim-acceptance), [EPI-RTE-atlas-topics](#epi-rte-atlas-topics)).

The Atlas topic request is a material qualification to the runtime's export summary, not grounds to attribute invented output. Its external semantics, claim production, checks and consumers are not determinable. The local CLI produces no generative answer, and projection/grouping supplies no formulated explanatory theory. Dense-state retention is distinct from provider-parameter change. The independently assessed model fixity limits remain those of [RT-CMP-lmstudio](runtime.md#rt-cmp-lmstudio) and [RT-CMP-openai](runtime.md#rt-cmp-openai). Nothing here establishes observed learning benefit, reflection, autonomous theory building or exercised self-improvement; these are separate properties, not consequences of similarity or persistence. No single epistemic score or system-wide verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-docs-content
Label: docs content

Part of: [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks)

Source-native identity: `docs.content`, natural-language material in SQLite. Imported archive text is copied/concatenated; RSS text is converted. People read root content after vector-based selection. This is the text part, not metadata or numerical embeddings. Actual truth-apt assertions and truth values are not determinable without corpus evidence. SRC-1 implementation, `apps/semantic-engine-cli/db/schema.ts`, `apps/semantic-engine-cli/scripts/load-archives.mts`; the supplied container records storage and downstream reload.

> content: thread.full_text,
> --- `apps/semantic-engine-cli/scripts/load-archives.mts`

#### EPI-OBJ-chunks-content
Label: chunks content

Part of: [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks)

Source-native identity: `chunks.content`, natural-language fragments stored in SQLite, consumed by embedding requests. Distinct from full roots because segmentation may isolate a qualifier or incomplete assertion; ranking then selects roots using these representations. SRC-1 implementation, `apps/semantic-engine-cli/lib/utils/split-text.ts`, `apps/semantic-engine-cli/scripts/embed-documents.mts`. See the supplied container for symbolic offsets and parent IDs.

> values: currentChunks.map(chunk => chunk.content),
> --- `apps/semantic-engine-cli/scripts/embed-documents.mts`

#### EPI-OBJ-docs-metadata
Label: docs provenance fields

Part of: [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks)

Source-native identity: root `origin`, `externalId`, `author`, `url`, `createdAt`, `checksum`, `metadata`. Symbolic SQLite fields become natural-language labels in output. IDs/checksums enable bookkeeping, not source authentication or duplicate rejection in inspected loaders. Author/time fields can assert provenance, but RSS falls back to feed title/Unknown Author and ingestion-time clock when publication date is unavailable. These are distinct from content because their production and consumer rules differ. SRC-1 implementation, `apps/semantic-engine-cli/db/schema.ts`, `apps/semantic-engine-cli/scripts/load-from-rss.mts`; query consumer in [RT-RTE-query-documents](runtime.md#rt-rte-query-documents).

> author: item.creator || feed.title || 'Unknown Author', // Use creator, feed title, or fallback
> --- `apps/semantic-engine-cli/scripts/load-from-rss.mts`

> const createdAtTimestamp = item.isoDate ? Math.floor(new Date(item.isoDate).getTime() / 1000) : Math.floor(Date.now() / 1000);
> --- `apps/semantic-engine-cli/scripts/load-from-rss.mts`

#### EPI-OBJ-chunks-embedding
Label: chunks embedding

Part of: [RT-OBJ-docs-chunks](runtime.md#rt-obj-docs-chunks)

Source-native identity: `chunks.embedding`, dense distributed-parametric representations in SQLite's declared vector column, not provider weights. The update consumer stores returned vectors; later SQL consumes them as ranking inputs. There is no explicit source-claim encoding individually inspectable here. Model provenance and mutable endpoint limits: see [RT-CMP-lmstudio](runtime.md#rt-cmp-lmstudio). SRC-1 implementation, `apps/semantic-engine-cli/db/schema.ts`; the supplied container and embedding/query routes provide the load-bearing vector/storage passages.

### Routes

#### EPI-RTE-source-reshaping
Label: Source reshaping and metadata

Part of: [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents)

Distinct transformation part of ingestion, not a new admission mechanism. Fixed loader code selects and concatenates surviving chronological tweets with blank lines, or constructs a title plus HTML-to-Markdown RSS body; it also creates provenance fields. Operator chooses archives/feed, source authors supply content, code decides per-item transformations, and withholding invocation is the operator's veto. No answer oracle or improvement trigger. Text concatenation adds no new sentence; whole-source semantic preservation is indeterminate because selection can omit context and converter behavior is external. RSS metadata fallback is not simple copying: an absent publication date becomes current time. No evidence that these transformations produce accepted ampliative assertions. Guidance is unchanged loader source; resulting roots and fields persist. SRC-1 implementation, `apps/semantic-engine-cli/scripts/load-archives.mts`, `apps/semantic-engine-cli/scripts/load-from-rss.mts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: constructed root text and metadata for automatic insertion.
- Later read-back: root text and labels reach query output after chunk/vector selection.
- Delegated visibility: inapplicable — external parsing/conversion is not agent delegation.
- Selection predicate: inherited archive/thread and RSS field rules; see parent route.
- Invalidation or expiry: no transformation-version tracking or automatic replacement; rerun creates fresh IDs.
- Activation or effect: constructed fields determine retained/displayed text if insertion succeeds; no observed activation.
- Evidence limits: converter implementation, source truth and actual inputs unavailable; no source-level rollback spanning both insert phases.

> full_text: parentThread.full_text + '\n\n' + tweet.full_text,
> --- `apps/semantic-engine-cli/scripts/load-archives.mts`

The parent route supplies the RSS conversion quotation; [EPI-OBJ-docs-metadata](#epi-obj-docs-metadata) supplies fallback passages.

#### EPI-RTE-split-text
Label: splitText transformation

Part of: [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents)

Fixed code transforms root text into ordered substring chunks and inclusive offsets before insertion. This part is distinct from root acquisition and per-item admission. SRC-1 implementation, `apps/semantic-engine-cli/lib/utils/split-text.ts`.

Concrete source deduction, not target execution: `splitText("Earth is not flat.", 10)` chooses space, yielding pieces `Earth`, ` is`, ` not`, ` flat.`. Buffer sizes make the result `Earth is` at positions 0–7 and ` not flat.` at positions 8–17. Concatenation reconstructs the input; the first chunk alone does not express the original qualified assertion. This falsifies any assumption that every chunk is independently truth-apt or retains whole-claim context. Production loaders use size 512; the same boundary mechanism remains, not an asserted corpus occurrence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: chunk content and start/end offsets, or error for nonpositive chunk size.
- Later read-back: inserted fragments feed embedding calls; roots, not reconstructed fragments, are printed by query.
- Delegated visibility: inapplicable — local deterministic function.
- Selection predicate: highest-priority present separator, recursive subdivision, buffer bounded by supplied size.
- Invalidation or expiry: no automatic rechunking/version invalidation in callers.
- Activation or effect: segmentation determines model inputs and therefore can affect ranking; no operation observed.
- Evidence limits: ordered collection reshaping, not a proof of semantic sufficiency of fragments or model token-budget compliance.

> splits = currentText.split(regex).filter(s => s !== ""); // Filter out potential empty strings from split
> --- `apps/semantic-engine-cli/lib/utils/split-text.ts`

> if (chunkBuffer.length + splitLen > chunkSize) {
> --- `apps/semantic-engine-cli/lib/utils/split-text.ts`

> currentPosition += splitLen;
> --- `apps/semantic-engine-cli/lib/utils/split-text.ts`

#### EPI-RTE-chunk-tests
Label: Chunker fixture checks

No supplied counterpart: this is authored evaluator code, not the ingestion route itself. `bun:test` runs `splitText` on fixtures and compares content/offsets, exceptions, size and reconstruction properties. Check target/domain: named finite input fixtures, not external truth or retrieval relevance. Human authors provide expected values; fixed assertions decide pass/fail. No model judge, adaptive curriculum or quality-improvement trigger; no test-driven write to retained content. SRC-1 implementation, `apps/semantic-engine-cli/lib/utils/split-text.test.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: assertion pass/failure to test runner when invoked.
- Later read-back: inapplicable — no retained test result or consumer in inspected code.
- Delegated visibility: inapplicable — local tests, no delegation.
- Selection predicate: statically authored test cases and assertions.
- Invalidation or expiry: inapplicable — no retained result or acceptance state.
- Activation or effect: failure can fail a test invocation; no ingestion/query gate is wired to that result in inspected scripts/manifests.
- Evidence limits: authored checks are not observed passes, universal correctness proof, relevance evaluation or evidence-consuming claim acceptance.

> const reconstructedText = result.map(chunk => chunk.content).join("");
>
>         // Assert that the reconstructed text is identical to the original
>         expect(reconstructedText).toBe(complexText);
> --- `apps/semantic-engine-cli/lib/utils/split-text.test.ts`

#### EPI-RTE-cosine-guards
Label: Cosine arithmetic guards

Part of: [RT-RTE-compare-texts](runtime.md#rt-rte-compare-texts)

The browser's numerical preconditions are a material check/disposition part of the supplied comparison route. Target/domain: returned vectors must have equal lengths and nonzero magnitudes for the implemented cosine formula. Fixed code evaluates and throws; provider proposes numerical outputs, user supplies texts and can stop use, but no human approval occurs between check and calculation. Open comparison, no answer oracle or improvement trigger. Guard results immediately enforce continuation; displayed score is advisory only. SRC-1 implementation, `apps/knowledge-gate/index.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: continuation to arithmetic, or thrown error preventing that score update.
- Later read-back: inapplicable — no persisted guards or comparisons.
- Delegated visibility: inapplicable — provider receives text as described by parent; guard is local code.
- Selection predicate: length inequality and either computed magnitude exactly zero.
- Invalidation or expiry: current invocation only; no result-version guard for overlapping requests.
- Activation or effect: throw enforces arithmetic rejection; score goes to DOM only on continuation.
- Evidence limits: no exhaustive finiteness/type validation, semantic-equivalence criterion or factual reference outcome. Arithmetic license is conditional on valid finite numeric inputs and normal floating-point limitations.

> if (vecA.length !== vecB.length) {
>                 throw new Error('Vectors must have the same length');
>             }
> --- `apps/knowledge-gate/index.html:178-181`

> if (magA === 0 || magB === 0) {
>                 throw new Error('Cannot calculate cosine similarity for zero vector');
>             }
> --- `apps/knowledge-gate/index.html`

> return dot / (magA * magB);
> --- `apps/knowledge-gate/index.html`

#### EPI-RTE-cluster-items
Label: Optional cluster grouping

No supplied counterpart: related to, but not part of the active projection/export behavior in [RT-RTE-display-export](runtime.md#rt-rte-display-export). Exported `cluster(items)` parses embeddings, calls k-means with 300 clusters, and groups copied `item.content`. Separate private `determineOptimalClusters` loops k=1..maxClusters, calculates squared-distance SSE and returns a list. Fixed numerical code proposes groups/metrics; no implemented selector chooses an optimal k or accepts a factual claim. The comment permits visual/programmatic choice but supplies neither. No answer oracle, adaptive improvement trigger or persisted policy. SRC-1 implementation, `apps/infinite-canvas-viewer/cluster.js`, `apps/infinite-canvas-viewer/process-embeddings.mjs`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: grouped content arrays if exported helper is called; private exploration helper would return SSE list.
- Later read-back: inapplicable — no active retained result or later consumer wired in processor.
- Delegated visibility: inapplicable — numerical library calls, not delegated reasoning.
- Selection predicate: numeric cluster labels map items to buckets; exploration checks each requested k.
- Invalidation or expiry: inapplicable — no retained state or replacement protocol implemented.
- Activation or effect: code can group text; processor's only cluster invocation is commented out. SSE is diagnostic with no automatic admission/selection consumer found.
- Evidence limits: library internals and actual assignments uninspected; no semantic interpretation, observed operation or causal quality evidence.

> const numberOfClusters = 300;
>     const clusteringResult = kmeans(vectors, numberOfClusters);
> --- `apps/infinite-canvas-viewer/cluster.js`

> clusterMap[label].push(item.content)
> --- `apps/infinite-canvas-viewer/cluster.js`

> return sseList; // Choose the optimal k visually or programmatically
> --- `apps/infinite-canvas-viewer/cluster.js`

> // const clusterResults = cluster(results)
> --- `apps/infinite-canvas-viewer/process-embeddings.mjs`

#### EPI-RTE-atlas-topics
Label: Atlas topic-model request

Part of: [RT-RTE-display-export](runtime.md#rt-rte-display-export)

This part qualifies the supplied container's characterization as transforming/exporting existing content: the Atlas request also asks for topic modeling, whose output cannot be classified from the caller alone. Fixed exporter code requests `topic_model` using content as label field. Local request implementation is inspected; external topic generation architecture, actual propositions, evaluation and acceptance are not determinable. Neither a label nor the request establishes ampliative conjecture. Operator starts export; fixed filters decide eligible rows; external service behavior and veto are uninspected. No local expected-answer oracle or evidence-responsive trigger. Guidance is static request configuration; potential remote persistence is not established. SRC-1 implementation, `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: intended Atlas mapping call; no actual service response supplied.
- Later read-back: uninspected — external dashboard/topic consumers and remote storage implementation unavailable.
- Delegated visibility: metadata, text and numerical embeddings are arguments if export reaches service; no agent protocol established.
- Selection predicate: inherited non-null/nonempty document-embedding checks; see parent route for schema and initialization obstacles.
- Invalidation or expiry: uninspected — no local topic revision or remote withdrawal protocol shown.
- Activation or effect: topic-model build requested at call site; no evidence request reached provider or changed later behavior.
- Evidence limits: unbound db_url and old schema qualify reachability in shipped exporter. No output, external source, provider implementation or execution evidence establishes topic truth, novelty, checking, acceptance or integration. No supersession is needed: the parent remains a valid container, but its prose must not be read as excluding the explicit topic request.

> topic_model={"build_topic_model": True, "topic_label_field": 'content'}
> --- `apps/semantic-engine-cli/scripts/push-to-nomic-atlas.py`

### Claims

#### EPI-CLM-rag-quickstart
Label: RAG on tweets

Distinct from the broader [RT-CLM-pipeline-purpose](runtime.md#rt-clm-pipeline-purpose): source-native quickstart label in SRC-1 doctrine/design, `apps/semantic-engine-cli/README.md`. The documented sequence leads to query output. Inspected query implementation embeds a query and prints root documents, without subsequent answer generation. This is a bounded label/implementation mismatch if RAG means retrieval-augmented generation, not evidence that the authors promised factual adjudication.

> ### Quickstart (RAG on tweets from community archive)
> --- `apps/semantic-engine-cli/README.md`

The supplied query record provides implementation evidence; this claim does not change that route's identity.

### Evidenced absences

#### EPI-ABS-claim-acceptance
Label: Local factual acceptance

- conclusion status: absent

No supplied counterpart: bounded absence of a local evidence-consuming decision accepting a claim against a factual criterion for an intended use/scope, not absence of all checks. Search boundary: SRC-1 at 7e2481671cad01f0b4c89f2a1877d6733d7e552c, CLI manifests, both loaders, chunker/tests, embedding/query, exporter, Knowledge Gate, canvas processor/PCA/clustering; clearing/display additionally covered by supplied runtime. Search terms included `accept`, `reject`, `valid`, `truth`, `test`, `embed`, `cluster`; full direct reads followed the material branches listed in coverage. The relevant decisions instead target source shape, null-vector eligibility, numeric comparison or fixed test properties. External Atlas/model/dependency internals are not covered by this negative.

Evidence: [RT-RTE-ingest-documents](runtime.md#rt-rte-ingest-documents), [RT-RTE-embed-chunks](runtime.md#rt-rte-embed-chunks), [RT-RTE-query-documents](runtime.md#rt-rte-query-documents), [EPI-RTE-cosine-guards](#epi-rte-cosine-guards), [EPI-RTE-chunk-tests](#epi-rte-chunk-tests), [EPI-RTE-cluster-items](#epi-rte-cluster-items), [EPI-RTE-atlas-topics](#epi-rte-atlas-topics). SRC-1 implementation, `apps/semantic-engine-cli/scripts/load-archives.mts`, `apps/semantic-engine-cli/scripts/load-from-rss.mts`, `apps/semantic-engine-cli/scripts/embed-documents.mts`, `apps/semantic-engine-cli/scripts/query-documents.mts`, `apps/knowledge-gate/index.html`. These records supply the load-bearing positive decision passages and opaque counterexample limit. Retention and ranking cannot establish accepted ampliative production or post-acceptance integration in these local routes. This does not assess the truth of uninspected source documents or undocumented human review.
