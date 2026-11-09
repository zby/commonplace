---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "expo-llm-wiki memory: retained events, derived facts, graph and trust state, maintenance and later model consumers."
run-id: AAS-2026-11-08-expo-llm-wiki-54f1fc1a0310-01
source-identity: "https://github.com/equationalapplications/expo-llm-wiki"
reviewed-boundary: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
---

# expo-llm-wiki memory report

## Boundary and evidence

The subject is the repository's memory engine and shipped integrations, not an enclosing agent runtime. The frozen boundary and SRC-1 are declared in [boundary](boundary.md). Included memory surfaces are event retention, extraction and direct admission, document ingestion, fact/task/graph storage, embeddings and search, ontology, trust and temporal metadata, import/export, maintenance, React and tool access, the shipped conversational consumer and benchmark consumer. Provider internals, deployed SQLite lifecycle, remote SynapseTree storage and independent consuming applications remain outside the source boundary. They prevent conclusions about deployed persistence, remote admission policy and behavioral benefit.

I directly inspected the paths listed below, at SRC-1's frozen commit. These reads supply implementation evidence; comments and tool descriptions supply doctrine/design only. The supplied runtime account supplies the ordinary invocation and several alternate paths, and is distinguished below from direct inspection. No target execution or stored-result aggregate is used as observed or causal evidence. Available but uninspected branches are named rather than treated as absent.

| Entry or memory operation | Source paths, relative to SRC-1 | Coverage and remaining limit |
|---|---|---|
| Event write, automatic maintenance | `packages/core/src/services/WriteService.ts` | Direct full read; [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [MEM-OBJ-events](#mem-obj-events). Event summaries are clipped host input, not necessarily complete transcripts. |
| Default legacy extraction | `packages/core/src/services/librarian/legacy.ts` | Supplied runtime findings and quotations, not an independent full source read; recent-window limits retained in [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian). |
| Ops extraction, neighbor gate, resolution and application | `packages/core/src/services/librarian/ops/extract.ts`, `packages/core/src/services/librarian/ops/gate.ts`, `packages/core/src/services/librarian/ops/resolve.ts`, `packages/core/src/services/librarian/ops/apply.ts` | Direct full reads; annotations on [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian). Distinct admission outcomes must not be flattened into rejection. |
| Document ingestion and caller graph upsert | `packages/core/src/services/IngestionService.ts`, `packages/core/src/WikiMemory.ts` | Supplied runtime findings for full/partial ingest and public graph transaction contract; detailed chunk transformation and graph ownership helpers remain uninspected. No universal provenance or validation guarantee: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission). |
| Deterministic remember | `packages/core/src/services/RememberService.ts` | Direct full read; [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission). Caller identity does not resolve human approval. |
| Fact/task/event/edge and control storage | `packages/core/src/db/schema.ts`; selected `packages/core/src/repositories/EntryRepository.ts` methods | Direct schema and focused repository reads; operative records below. Individual task/edge repository internals not fully audited, preventing exhaustive cross-path consistency claims. |
| Query retrieval, ranking and packing | `packages/core/src/services/RetrievalService.ts` entry and fallback/final assembly; `packages/core/src/utils/temporal.ts` | Direct reads; [RT-RTE-memory-read](runtime.md#rt-rte-memory-read). Detailed native/custom ranking and cache internals retain runtime's inspection limits. |
| Embedding generation/recovery | `packages/core/src/services/EmbeddingService.ts` generation and dimension reconciliation; schema | Direct reads; [MEM-OBJ-entry-vectors](#mem-obj-entry-vectors). Remaining storage-hook internals and reembed sweep details rely on supplied runtime, not a full independent audit. |
| Heal, context degradation, anchor selection | `packages/core/src/services/MaintenanceService.ts` heal and anchor methods; `packages/core/src/services/PromptService.ts` heal selection/degradation excerpt | Direct reads; [MEM-RTE-heal-memory](#mem-rte-heal-memory). Bounded provider contexts cannot establish exhaustive contradiction detection. |
| Ontology backfill including classifier alternative | `packages/core/src/services/MaintenanceService.ts` backfill, classifier and apply methods | Direct reads; [MEM-RTE-ontology-backfill](#mem-rte-ontology-backfill). OntologyService helper internals remain uninspected; no global soundness claim. |
| Grounding and draft handling | `packages/core/src/utils/grounding.ts`; ops/heal writers; `packages/core/src/WikiMemory.ts` public API search | Direct grounding/writer reads; promotion contract supplied by runtime; [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata). Quote occurrence does not establish truth or semantic entailment. |
| Supersede and historical read | `packages/core/src/services/TemporalService.ts`, `packages/core/src/utils/temporal.ts` | Direct full reads; [MEM-RTE-temporal-history](#mem-rte-temporal-history). Valid time with current knowledge, not reconstruction of past knowledge state. |
| Forget and prune | `packages/core/src/services/MaintenanceService.ts` full forget and prune methods | Direct reads; [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). No all-substrate erasure guarantee. |
| Import/export, summary and full-bundle read | `packages/core/src/services/ImportExportService.ts` full-bundle and import transaction prelude; `packages/core/src/WikiMemory.ts` API inventory | Direct excerpts plus supplied runtime; [MEM-OBJ-entity-summary](#mem-obj-entity-summary), [RT-RTE-import-admission](runtime.md#rt-rte-import-admission). Full per-field conversion remains uninspected. |
| Presentation into later contexts | `packages/core/src/utils/formatContext.ts`, `packages/core/src/utils/formatGraphContext.ts` | Direct full reads; [MEM-RTE-graph-context](#mem-rte-graph-context) and annotations on read/benchmark routes. Display is not a complete serialization of stored knowledge. |
| ScopeLab conversation and tool-result feedback | `apps/scopelab/src/lib/llm/function-caller.ts` | Direct full read; wrapper storage issues supplied by [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat). No demonstrated operational persistence. |
| React and demo access | `packages/react/src/useMemoryRead.ts`, `useWikiMaintenance.ts`; `apps/wiki-demo/src/App.tsx` | First two direct full reads; demo setup from runtime. Hooks request reads and manual maintenance; UI subpanels and remaining hook implementations not independently inspected, so no exhaustive UI admission-policy conclusion. |
| Tool declarations, instruction exposure and MCP CLI | `packages/core-llm-tools/src/manifests/core.ts`, `packages/core-llm-tools/src/manifests/graph.ts`, `packages/core-llm-tools/src/manifests/instructions.ts`; `packages/core/src/WikiMemory.ts` getInstructions; `packages/mcp-server/src/commands.ts`, `packages/mcp-server/src/server.ts`, `packages/mcp-server/src/tools/index.ts` | Direct reads. MCP registers search/remember/supersede/ingest/log-event/traverse/namespaces/whoami and serves over stdio; remote behavior remains [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools). Schema-only local manifests are not deployed dispatch. |
| Outbox and native graph computation | `packages/prisma-outbox/src/PrismaOutboxWorker.ts`, `crates/graphrag-core/src/engine.rs` | Supplied runtime, not direct rereads; [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync), [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal). External mapEvent consumers and native/TS parity unresolved. |
| Evaluation consumption | `packages/benchmarks/src/longmemeval/judge.ts`; runtime's `run.ts` read/answer/judge sequence | Judge direct full read; driver supplied. [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer). Stored benchmark results and integration evaluators not inspected for measured benefit; no accuracy or causal conclusion. |

## Core ideas

1. The event log and the knowledge store are different memory layers. Host summaries are retained first; the librarian produces separately identified facts and tasks. Later retrieval can return both derived facts and recent raw summaries. Fact admission can also bypass the event log through remember, documents, graph upsert or import. A system-wide description as only conversational extraction would miss these alternatives. See [MEM-OBJ-events](#mem-obj-events), [MEM-OBJ-entry-text](#mem-obj-entry-text) and [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission).
2. Read-back is requested, with automatic selection inside the request, not unsolicited model-context injection by the library. Query/entity selection, ranking, optional fact packing and presentation intervene before model consumption. Background maintenance independently requests retained material for its own model calls. Its push-like scheduling is not evidence of pushing memories into an unrelated foreground model. See [RT-RTE-memory-read](runtime.md#rt-rte-memory-read), [MEM-RTE-heal-memory](#mem-rte-heal-memory), [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat).
3. Trust and historical status are separate from readable assertions. A grounded insertion can receive a machine-check marker; a failed check produces a draft, not necessarily rejection or exclusion from read-back. Default retrieval admits drafts. Document immutability limits some update routes but not caller deletion or replacement through all APIs. See [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata), [MEM-RTE-temporal-history](#mem-rte-temporal-history), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal).
4. Retention does not imply faithful later delivery. Ordinary formatting omits provenance/trust/history fields; graph formatting omits even fact bodies. Heal can omit tasks/events and truncate candidate bodies to recover from bounded-output failures. These are material context transformations, not merely storage choices. See [MEM-RTE-graph-context](#mem-rte-graph-context), [MEM-RTE-heal-memory](#mem-rte-heal-memory) and the read annotations.

## Shared records

### Components

#### MEM-CMP-classify-provider
Label: Optional ontology classifier

Source-native identity: `LLMProvider.classify`, consumed only when backfill chooses `auto` and an eligible manifest has 1–255 node types. The interface is symbolic question/choice/confidence data; the implementation behind the callback is opaque and may be model-based. Parameter substrate, exact model version, parameter changes during operation and endpoint mutability are uninspected; the callback does not pin a model. No weight update is requested by this call. Distinct from [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider) and [RT-CMP-embed-provider](runtime.md#rt-cmp-embed-provider): different operation and answer contract even if a host implements all roles in one provider. SRC-1, `packages/core/src/services/MaintenanceService.ts`.

> response = await provider.classify!({ state: classifierStateForFact(fact), questions: { okf_type: question } });
> --- `packages/core/src/services/MaintenanceService.ts`

### Operative objects

The runtime declares no operative objects. The following objects have no supplied object counterpart; associated runtime routes are consumers or producers, not alternative identities for the objects.

#### MEM-OBJ-events
Label: Events

Identity/substrate: entity-scoped rows in SQLite `events`. Natural-language `summary` is distinct from symbolic event type, IDs and created/occurred timestamps. WriteService clips host summaries to 4000 characters, coerces unsupported event types to observation and checks related-entry visibility. These are retained input records, not necessarily verbatim conversation logs: their upstream authorship may be human, application, assistant or tool-derived. In ScopeLab the caller writes the user message, abbreviated assistant text or a tool-call/result rendering; the event type label alone does not authenticate that origin. Later consumers are librarian extraction, heal context and read bundles. No stable event-to-fact source reference is written by the inspected ops insertion; its source label is used to choose valid time. See [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat). SRC-1, `packages/core/src/services/WriteService.ts`, `packages/core/src/services/librarian/ops/extract.ts`, `packages/core/src/services/librarian/ops/apply.ts`, `apps/scopelab/src/lib/llm/function-caller.ts`.

> const summary = clip(event.summary, 4000);
> --- `packages/core/src/services/WriteService.ts`

> await wiki.remember(`Assistant: ${text.slice(0, 500)}`, { type: 'assistant_response' })
> --- `apps/scopelab/src/lib/llm/function-caller.ts`

#### MEM-OBJ-entry-text
Label: Entry assertions

Identity/substrate: SQLite `entries` title/body/tags, separate from the numerical and metadata parts below. Representational form is natural-language assertions and labels, interpreted by models or humans; IDs and field structure are symbolic. Lineage can be extracted conversation summaries, document chunks, host-authored direct facts or imported facts. Source type is not proof of authorship or truth. Ops/heal inserts mark derived rows `librarian_inferred` and leave source_ref/hash null; document linkage is carried on the document route. Facts can be updated, superseded, deduplicated, softened to tentative or soft-deleted. Later consumers are retrieval, legacy prompt context, ops neighbor resolution, heal and ontology classification. Downstream answer models receive selected renderings, not necessarily every stored field. See [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission), [MEM-RTE-heal-memory](#mem-rte-heal-memory). SRC-1, `packages/core/src/db/schema.ts`, `packages/core/src/services/librarian/ops/apply.ts`, `packages/core/src/services/MaintenanceService.ts`.

> id, entity_id: entityId, title, body, tags: fact.tags, confidence: fact.confidence,
>         source_type: 'librarian_inferred', source_hash: null, source_ref: null,
> --- `packages/core/src/services/librarian/ops/apply.ts`

#### MEM-OBJ-entry-vectors
Label: Entry embeddings

Identity/substrate: `entries.embedding_blob` numerical Float32 representation, with legacy `embedding` text storage and dimension metadata. Encoding is distributed numerical representation of text, not the encoder's weights and not a natural-language summary. The embedding input concatenates title/body/tags and clips to configured bounds. Vectors affect similarity selection in query retrieval and ops gating, not directly model instructions. The provider's exact provenance/version is not retained by a dimension check; equal dimensions cannot establish semantic compatibility. Imported blobs are an alternative lineage, whose upstream encoder can be unresolved. Reembed/dimension reconciliation and failure markers support later repair. This is distinct from [RT-CMP-embed-provider](runtime.md#rt-cmp-embed-provider), which produces vectors rather than storing these per-fact results. SRC-1, `packages/core/src/services/EmbeddingService.ts`, `packages/core/src/services/ImportExportService.ts`, `packages/core/src/services/librarian/ops/gate.ts`.

> const text = clip(`${fact.title} ${fact.body} ${tagsStr}`.trim(), maxEmbedChars);
> --- `packages/core/src/services/EmbeddingService.ts`

> const vector = await this.options.llmProvider.embed(text);
> --- `packages/core/src/services/EmbeddingService.ts`

#### MEM-OBJ-entry-metadata
Label: Entry access, trust and validity metadata

Identity/substrate: symbolic SQLite entry fields: access counts/times, confidence, source reference/type/hash, lifecycle, verification/source JSON, stale-after, valid-from/to and supersession links, plus maintenance/failure timestamps. These parts differ from assertion content. Access is operational use metadata, not evidence of correctness; nonempty-query read tracks access, empty-query recency does not. Access_count affects formatted ordering and orphan survival. Confidence is model/caller data with code-defined weighting. Temporal fields govern liveness. Grounding in configured draft mode checks normalized quotes against individual shown corpus parts and stamps stable/machine-confirmed or draft status; `retained` quote strings returned by checkGrounding are not part of GroundingTrust, and the inspected ops/heal insert objects save trust fields rather than evidence text. Thus no retained explanation chain or quote-bearing later answer is established by those checks. SRC-1, `packages/core/src/utils/grounding.ts`, `packages/core/src/services/RetrievalService.ts`, `packages/core/src/services/librarian/ops/apply.ts`, `packages/core/src/services/MaintenanceService.ts`.

> trust: {
>         lifecycle_status: 'stable',
>         okf_verified: [{ by: GROUNDING_VERIFIER, at: new Date(now).toISOString() }],
>         last_verified_at: now,
>         last_verified_by: GROUNDING_VERIFIER,
>       },
> --- `packages/core/src/utils/grounding.ts`

> const excludeDrafts = (options?.excludeDrafts ?? config?.excludeDrafts ?? false) === true;
> --- `packages/core/src/services/RetrievalService.ts`

Draft promotion's nonempty reviewer string and host-editable trust/source APIs are supplied by [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission); they do not establish human authentication. Read-time default draft inclusion is a counterexample to treating failed grounding as universal quarantine.

#### MEM-OBJ-tasks
Label: Tasks

Identity/substrate: SQLite tasks with natural-language descriptions, symbolic status/priority/IDs and optional lifecycle/trust metadata. Models propose extracted tasks; code validates and inserts pending rows. Import is another lineage. Later ordinary reads return pending tasks separately from ranked facts; default formatContext renders prioritized tasks unless explicitly excluded. No inferred fact-level rationale accompanies the inspected ops task insert. The benchmark explicitly excludes this part from answer context. SRC-1, `packages/core/src/db/schema.ts`, `packages/core/src/services/librarian/ops/apply.ts`, `packages/core/src/services/RetrievalService.ts`, `packages/core/src/utils/formatContext.ts`; [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer).

> id: generateId('task_'), entity_id: entityId, description: task.description, status: 'pending', priority: task.priority,
> --- `packages/core/src/services/librarian/ops/apply.ts`

#### MEM-OBJ-edges
Label: Graph edges

Identity/substrate: SQLite edges linking source/target IDs under an entity and edge-type string. The operative links are symbolic adjacency consumed by traversal rules; type descriptions and rendered titles add natural-language interpretation. Edges can arrive from extracted facts, ontology backfill, caller graph upsert and imports. Ops/backfill normalize and resolve title targets before persistence; a proposed edge is not automatically a stored edge. Graph consumers differ from ordinary read, whose bundle has an empty edges array. Native traversal is separately covered by [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal); no parity is inferred. SRC-1, `packages/core/src/db/schema.ts`, `packages/core/src/services/librarian/ops/apply.ts`, `packages/core/src/services/MaintenanceService.ts`, `packages/core/src/services/GraphTraversalService.ts`.

> const bundle: MemoryBundle = { facts, tasks, events: events.reverse(), edges: [] };
> --- `packages/core/src/services/RetrievalService.ts`

#### MEM-OBJ-entity-manifests
Label: Entity manifests

Identity/substrate: SQLite entity_manifests mode and JSON node/edge definitions. Symbolic type vocabulary and edge constraints are consumed by normalizers; natural-language type descriptions enter writer/classifier prompts. Host setter calls and emergent model proposals are distinct admission origins. The backfill apply transaction rechecks mode; emergent mode can merge ontology updates before validating types. These are retained interpretation constraints for later writers, not model-parameter updates. Instructions_get can expose them as reference data alongside configured templates. Distinct from static ontology package data: effective-manifest initialization and merge helper details remain uninspected here, so exhaustive inheritance/provenance is unresolved. SRC-1, `packages/core/src/db/schema.ts`, `packages/core/src/services/MaintenanceService.ts`, `packages/core-llm-tools/src/manifests/instructions.ts`; [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission).

> if (txMode === 'emergent' && ontologyUpdates) {
>         manifest = await ontologyService.mergeEmergentUpdates(entityId, ontologyUpdates, tx);
>       }
> --- `packages/core/src/services/MaintenanceService.ts`

#### MEM-OBJ-checkpoints
Label: Checkpoints and maintenance state

Identity/substrate: symbolic SQLite checkpoints, meta keys, source_ref_index and row-level cooldown/failure fields. These retain scheduling/access state, not conversational knowledge. Counts/watermark govern whether events are retried and can be pruned; source-ref/hash ownership supports ingestion idempotence; cooldowns and embedding failure markers shape later maintenance eligibility. In-memory JobManager locks are separately scoped and are not durable memory. See [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal). SRC-1, `packages/core/src/db/schema.ts`, `packages/core/src/services/WriteService.ts`, `packages/core/src/services/MaintenanceService.ts`.

> librarian_watermark_at INTEGER,
>       librarian_watermark_id TEXT
> --- `packages/core/src/db/schema.ts`

#### MEM-OBJ-entity-summary
Label: Imported entity summary

Identity/substrate: natural-language entity summary persisted in SQLite meta by import, returned through full-bundle export and exposed by getEntitySummary. Upstream authorship and derivation are unresolved: an imported field called summary does not establish transcript compaction or automatic synthesis. Replacement import without a summary clears it; merge without one preserves it. Ordinary RetrievalService bundle construction and formatContext do not carry/render this field. Thus its inspected route is storage/API exposure, not an established later model consumer. Closest supplied record is [RT-RTE-import-admission](runtime.md#rt-rte-import-admission), a producer route rather than this object. SRC-1, `packages/core/src/services/ImportExportService.ts`, `packages/core/src/WikiMemory.ts`, `packages/core/src/services/RetrievalService.ts`, `packages/core/src/utils/formatContext.ts`.

> if (bundle.summary !== undefined) {
>         await this.metadataRepo.setMeta(entitySummaryMetaKey(entityId), bundle.summary, tx);
>       } else if (!merge) {
>         await this.metadataRepo.deleteMeta(entitySummaryMetaKey(entityId), tx);
>       }
> --- `packages/core/src/services/ImportExportService.ts`

#### MEM-OBJ-outbox
Label: Change outbox

Identity/substrate: symbolic SQLite outbox rows with operation/table/record/entity identifiers and JSON payloads; payloads can contain natural-language entry changes. These are change-delivery records, not necessarily complete source traces or derived knowledge. Entry deletion/downgrade methods emit changes; embedding lifecycle fields explicitly remain local. Later mapEvent consumers are host-defined through [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync); local retention enables retry but does not establish exactly-once external effect or a later model prompt. SRC-1, `packages/core/src/db/schema.ts`, `packages/core/src/repositories/EntryRepository.ts`.

> payload: { id: row.id, entity_id: entityId, deleted_at: now },
> --- `packages/core/src/repositories/EntryRepository.ts:873-873`

### Routes

#### MEM-RTE-heal-memory
Label: Heal retained memory

Closest supplied route: [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian) can trigger heal but does not describe this maintenance operation; heal is a distinct pass over retained facts. Owner: host manual call, scheduler or automatic event-count scheduling starts code selection; text provider proposes downgrades/deletions/new facts; software bounds eligible IDs and persists. No per-content human veto or expected-answer oracle is required. Mode is ongoing maintenance, not benchmark answer evaluation. Guidance is host override/global/default heal template. Proposed knowledge changes can be invalidated/deduplicated; transaction failure rolls back that transaction, but earlier SQL aging changes are separate. Later explicit remember/import/supersede can repair content; no automatic semantic undo.

- Immediate return: scanned/downgraded/deleted/new-fact counts, skipped/degraded records, remaining/deferred counts and possible budget/search status.
- Later read-back: retained assertions and access metadata shape this pass; new/downgraded/deleted rows affect later retrieval and maintenance. New facts are stamped checked to prevent immediate self-feeding eligibility.
- Delegated visibility: selected mutable facts, keyword-selected immutable-document anchors, bounded tasks and 20 recent events; embeddings omitted. Grounding-enabled heal changes trust-field visibility and anchor-body/corpus handling.
- Selection predicate: repository selects nondeleted non-immutable current facts ordered oldest update first with recheck cooldown and batch limit. Anchor query concatenates candidate titles, overfetches keywords, filters to immutable-document rows, caps at min(50, four per candidate). The prompt degradation ladder drops tasks at L1, events at L2 and truncates candidate bodies at L3.
- Invalidation or expiry: pre-model SQL can delete old unaccessed non-document rows and downgrade stale inferred confidence. Model deletion/downgrade IDs are guarded per producing batch. Transient-error and unattempted candidates avoid cooldown stamps; other skipped candidates can be stamped.
- Activation or effect: accepted new facts and safe ID changes commit, then search sync/embedding/cache updates run. Context degradation is temporary; stored candidate bodies are not truncated merely because their prompt copy was. Successful semantic revision or answer improvement is unobserved.
- Evidence limits: source implementation only. Keyword/title anchor selection can miss contradictions sharing no query vocabulary; default anchors carry id/title/source_ref rather than full document bodies. A model request for cleanup is not evidence that content-directed criticism occurred or that reasons persist.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/MaintenanceService.ts`, `packages/core/src/services/PromptService.ts`, `packages/core/src/repositories/EntryRepository.ts`.

> const effectiveTasks = attemptLevel >= 1 ? [] : allTasks;
>     const effectiveEvents = attemptLevel >= 2 ? [] : recentEvents;
> --- `packages/core/src/services/PromptService.ts`

> for (const id of batchResult.deleted) if (mutableIds.has(id)) safeDeletedSet.add(id);
> --- `packages/core/src/services/MaintenanceService.ts`

> const columns = opts?.withBody ? 'id, title, source_ref, body, lifecycle_status' : 'id, title, source_ref';
> --- `packages/core/src/repositories/EntryRepository.ts`

#### MEM-RTE-ontology-backfill
Label: Backfill ontology metadata

No supplied route counterpart: this is distinct from extraction and caller manifest admission in [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian) and [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission). Host selects entity/options; code chooses untyped facts and text-model versus optional classify branch. Provider proposes type and, in text mode, edges/ontology updates; code normalizes against the effective manifest and can reject. In classifier auto mode, 1–255 types are required, answer schema is checked, and default minimum confidence is 0.5. No edges are proposed on that branch. Caller human identity is unresolved; no per-result human approval or reference-answer oracle. This is maintenance of knowledge structure under manifest guidance, not evidence of improved reasoning. Mode changes and transaction rollback reject/abort applicable batches; already committed earlier batches survive. Explicit host metadata/manifest APIs afford correction, not universal undo.

- Immediate return: scanned/typed/failed-validation/edges-added/skipped/remaining/deferred counts.
- Later read-back: type fields and edges reach graph/API consumers and later writers; emergent manifest changes guide subsequent normalization and prompts.
- Delegated visibility: selected id/title/body/tags plus ontology context for text generation; classifier receives per-fact state and manifest choices/descriptions.
- Selection predicate: eligible untyped facts with cooldown and batch limit; ontology off skips work; auto plus callable classifier and eligible type count selects the non-text alternative, otherwise text generation.
- Invalidation or expiry: transaction rechecks ontology mode and aborts when off; existing concurrently typed facts are not overwritten. Nontransient skips receive cooldown; thrown classifier calls do not.
- Activation or effect: normalized type/edge changes are persisted; emergent updates may change manifest. No evidence establishes correct typing, learning or downstream behavioral activation.
- Evidence limits: application and both dispatch branches inspected, helper ontology semantics and opaque classifier internals not fully audited. No claim that ontology labels are formulated explanations.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/MaintenanceService.ts`.

> if (classifierMode === 'auto' && typeof classify === 'function') {
>       const slugs = effectiveManifest.node_types.map((n) => n.type);
>       if (slugs.length > 0 && slugs.length <= 255) {
>         return this._runClassifierBackfill(entityId, candidates, effectiveManifest, now, recheckCutoff);
>       }
>     }
> --- `packages/core/src/services/MaintenanceService.ts`

#### MEM-RTE-temporal-history
Label: Supersession and historical access

Part of: [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)

This is its material temporal-replacement operation, with a distinct history consumer and invalidation rules. Caller supplies replacement ID/content and effective time; code validates entity, liveness, immutability and cycles before linking. Caller decides admission in open API mode; human control unresolved. No model, expected-answer oracle or mandatory human review. Guidance is symbolic validation and valid-time options, not a retained criticism. A transaction rolls back invalid replacement/link changes; history affords inspection, not a universal rollback operation.

- Immediate return: newId from supersede; history returns predecessor/start/successor facts sorted by valid-from or creation time, capped chain depth 100.
- Later read-back: current/asOf query liveness uses retained validity fields; explicit history accesses the chain of retained nondeleted facts.
- Delegated visibility: inapplicable — TemporalService does not call a text model to select or criticize replacements.
- Selection predicate: entity and fact IDs; explicit epoch time or now; replacement must exist/be created and pass temporal constraints. History is an ID request, not query-targeted semantic recall.
- Invalidation or expiry: supersede sets old valid_to/link/timestamp and initializes replacement valid_from when absent. Immutable document targets are rejected; pruning/deletion can remove historical availability later.
- Activation or effect: changes which assertions qualify at a selected valid time; search refresh and optional new-fact embedding follow. No evidence of a later answer changing because of this update.
- Evidence limits: source-only; asOf is valid time using current knowledge, not transaction-time reconstruction or retained explanation of why the change was correct.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/TemporalService.ts`, `packages/core/src/utils/temporal.ts`.

> if (old.source_type === 'immutable_document') throw new WikiSupersedeError('immutable_target');
> --- `packages/core/src/services/TemporalService.ts`

> await this.entryRepo.setTemporal(oldId, entityId, { valid_to: t, superseded_by: newId, superseded_at: now }, tx);
> --- `packages/core/src/services/TemporalService.ts`

#### MEM-RTE-memory-withdrawal
Label: Forget and prune memory

No supplied route counterpart. Closest overlaps are [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)'s mention of explicit forget recovery and [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)'s replacement behavior; neither declares this deletion route. Host invokes forget selectors/dry-run or prune retention parameters; code owns scope checks, locking and retention policy. No text model or expected-answer oracle. Caller human/software identity unresolved; content-specific human approval is not required. These are withdrawal decisions under host selectors and configured age policies; malformed/exclusive selectors reject, DB transactions recover their own changes, but hard deletion has no built-in undo. A separately retained dump might restore content without guaranteeing original state.

- Immediate return: deletion counts and optional metadataReset; dry-run previews without writes; prune can throw partial-failure details after successful prior hook/DB work.
- Later read-back: soft-deleted facts stop normal live hydration; pruned rows and events are physically removed. Outbox consumers can receive deletion changes; external ANN cleanup is delegated to hooks.
- Delegated visibility: deletion hook receives entity/fact identifiers and null vector; no model receives a withdrawal prompt.
- Selection predicate: forget entry/task or normalized sourceRef/sourceHash or clearAll; prune ages soft-deleted rows/events, optionally expired temporal history. Deferred/ops event pruning is bounded by librarian watermark.
- Invalidation or expiry: forget clearAll soft-deletes facts/tasks, resets memory/heal counts and deletes entity summary, but inspected branch does not erase event log or all control/index state. Default prune retention is seven days for soft deletes and thirty for events; temporal-history aging is off by default.
- Activation or effect: DB changes precede index sync and forget hook notification; hook failure can therefore report failure after local deletion committed. Prune notifies deletions first and hard-deletes only successful entry IDs before reporting a hook partial failure. No universal remote/backup erasure follows.
- Evidence limits: inspected method bodies establish local withdrawal mechanics, not external deletion correctness or prevention of re-deriving facts from retained events/documents. SourceRef clearAll comments contain a TODO; code must not be represented as complete source-index cleanup.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/MaintenanceService.ts`.

> const guarded = this.options.config?.maintenance === 'deferred' || this.options.config?.librarian?.strategy === 'ops';
> --- `packages/core/src/services/MaintenanceService.ts`

> deletedEvents = (await this.eventRepo.pruneThrough(entityId, cutoff, wm)).changes;
> --- `packages/core/src/services/MaintenanceService.ts`

> await this.metadataRepo.updateCheckpoint(entityId, { memory: 0, heal: 0 }, tx);
>           await this.metadataRepo.deleteMeta(entitySummaryMetaKey(entityId), tx);
> --- `packages/core/src/services/MaintenanceService.ts`

#### MEM-RTE-graph-context
Label: Graph traversal and presentation

Distinct from [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal): this is the TypeScript graph service and exported presenter, not the native engine entry. Host chooses anchor/options, service selects neighborhood through EdgeRepository and hydrates facts; the optional presenter converts that result to text. A manifest describes external host dispatch but does not establish a deployed answer-model caller.

- Immediate return: nodes/edges or dense graph text if caller invokes formatGraphContext; no generated answer.
- Later read-back: traverses retained links/facts on a later request. Actual delivery to a model is afforded by tool description/presenter, not established for all consumers.
- Delegated visibility: inapplicable — these service/presenter functions do not delegate selection to a model.
- Selection predicate: entity/anchor, depth 1–3, direction/edge types/confidence/source exclusions/draft flag, node cap default 20 and optional valid time/budget. Nonlive anchor can return alone. Budget keeps packed anchor and greedily admits further nodes, then filters edges to kept endpoints.
- Invalidation or expiry: deleted/unhydrated endpoints lose edges; liveness filters affect walks. Retained graph persists until writes/deletion change it.
- Activation or effect: presenter emits type/title/ID and relation/type/title lines, not fact bodies, trust metadata or retained derivation reasons. Delivered content therefore differs substantially from raw nodes.
- Evidence limits: EdgeRepository walk implementation not fully inspected; no parity, complete neighborhood, total token ceiling or deployed model-compliance guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/GraphTraversalService.ts`, `packages/core/src/utils/formatGraphContext.ts`, `packages/core-llm-tools/src/manifests/graph.ts`.

> lines.push(`[${node.okf_type ?? 'fact'}] ${node.title} (ID: ${node.id})`);
> --- `packages/core/src/utils/formatGraphContext.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-manifest-guidance
Label: Retained ontology into writer guidance

Consumer: text-generation writer/backfill or optional classifier and symbolic ontology normalizer. Channel: effective manifest context in prompts, classification choices/descriptions and validation rules. Force: model guidance is advisory; normalized permitted type/edge checks are software admission constraints within their inspected call sites. Horizon: later maintenance/writer calls on the persisted entity. This is a retained-data-derived instruction/constraint surface, not an edit to provider weights. It overlaps [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) at prompt delivery but is distinct in tracing the persisted manifest to both language and code consumers. A generic prompt-guidance path does not describe the classifier choice contract. SRC-1, `packages/core/src/services/MaintenanceService.ts`, `packages/core-llm-tools/src/manifests/instructions.ts`.

> instructions:
>         'Choose the ontology node type that best describes this fact.\n' +
>         manifest.node_types.map((n) => `- ${n.type}: ${n.description}`).join('\n'),
> --- `packages/core/src/services/MaintenanceService.ts`

## Annotations

#### On [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)

Memory lineage is retained summary → model extraction → separate assertions/tasks → later retrieval or maintenance. It is an automatic trace-fed transformation when configured/scheduled over conversational events, not a parameter-training route. Original event content may mix user/assistant/tool renderings; generic core write input alone does not determine origin. Admission combines model proposal and software validation, not per-fact human approval. Deferred mode preserves raw records without starting extraction; explicit maintenance is still available. Legacy's recent 50-event/100-fact window is supplied runtime evidence, not an exhaustive processed-event guarantee. Behavioral benefit is unobserved. SRC-1, `packages/core/src/services/WriteService.ts`; supplied record quotations establish the legacy window.

#### On [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian)

Read-back selector uses retained watermark, at most 50 later events and a 24000 summary-character bound; a budget can shrink the batch. Extract sees the selected summaries, not existing facts; gate then retrieves candidate-text neighbors by vectors or keywords. Resolver sees only ambiguous candidates and neighbor title/body copies, bodies clipped to the configured constant. Per-candidate aliases constrain its targets. Text equivalence can suppress a candidate before model resolution. These are separate consumers of retained text and vectors. SRC-1, `packages/core/src/services/librarian/ops/extract.ts`, `gate.ts`, `resolve.ts`.

> const events: WikiEvent[] = await deps.eventRepo.getAfter(entityId, wm, OPS_MAX_EVENTS_PER_PASS);
> --- `packages/core/src/services/librarian/ops/extract.ts`

> body: safeSlice(n.body, 0, OPS_NEIGHBOUR_BODY_CHARS),
> --- `packages/core/src/services/librarian/ops/resolve.ts`

Application gives rejection several different meanings: malformed/missing op falls back to stable insertion, failed parsing can insert a draft, NOOP retains existing content, UPDATE mutates inferred title/body in place, and UPDATE against non-inferred mutable targets becomes supersession. Immutable-document targets produce draft alternatives rather than being overwritten. A supersession validation failure can leave the already-inserted alternative fact admitted with a diagnostic. These are supported refinements to runtime's unresolved application details, not a contradiction of its bounded orchestration claim. No stored resolver rationale is in the inspected op schema or insertion. SRC-1, `packages/core/src/services/librarian/ops/apply.ts`, `resolve.ts`.

> if (rejected.has(g) || !op) {
>         await insert(g, false, vf);
> --- `packages/core/src/services/librarian/ops/apply.ts`

> if (target.source_type === 'immutable_document') {
>         const id = await insert(g, true, supersedeFrom, overrides);
> --- `packages/core/src/services/librarian/ops/apply.ts`

#### On [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)

Direction is request → automatic selection → returned bundle. Entity list scopes candidates; query and options target ranking; empty query uses global recency, not query relevance. Multi-entity tier weights/floors change selection and can suppress zero-weight entities from scored retrieval without making them authorization boundaries. The optional budget packs only facts. Tasks and recent events are fetched separately. Nonempty-query results update access metadata, which subsequently influences orphan/stale policies and formatting order; this is trace-fed metadata feedback, not new explanatory knowledge. SRC-1, `packages/core/src/services/RetrievalService.ts`.

> await this.entryRepo.trackAccess(ids, now);
> --- `packages/core/src/services/RetrievalService.ts`

A second transformation can reorder/limit the selected facts. formatContext preserves retrieval order when factScores exists; otherwise it sorts by confidence, log access count and exponential recency, then defaults to ten facts. It displays assertion body/title plus optional confidence/tags/entity/scores, tasks and events, not complete provenance/validity/verification/reasons. Thus delivery of rows does not establish delivery of their warrant. SRC-1, `packages/core/src/utils/formatContext.ts`.

> const sortedFacts = bundle.factScores
>     ? [...bundle.facts].slice(0, opts.maxFacts)
> --- `packages/core/src/utils/formatContext.ts`

#### On [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)

Imported material can include natural-language entity summary and numerical embedding blobs as well as assertions/tasks/edges. Upstream origin, review and encoder identity are not established by import acceptance. Full-bundle export strips the legacy embedding field, conditionally copies blobs and returns retained summary. Physical import I/O is code; deciding which dump to adopt remains with the caller, whose human/software identity is unresolved. This alternative lineage prevents treating every fact/vector/summary as local model extraction. SRC-1, `packages/core/src/services/ImportExportService.ts`.

> const safeBlobCopy =
>         opts?.includeBlobs && embedding_blob
> --- `packages/core/src/services/ImportExportService.ts`

#### On [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)

Direct caller read confirms requested context → marked memory text → first Gemini request and possible follow-up with original messages. Supplied history is forwarded, with no separate subagent frame or compaction in this caller. After tool execution it retains a rendering of call arguments and at most 200 result characters; otherwise it retains at most 500 assistant characters. These are application-created summaries and can lose evidence. A follow-up answer in the tool branch is returned without the same assistant-response event write. Later extraction/read-back is conditional on the supplied wrapper/provider/storage issues. SRC-1, `apps/scopelab/src/lib/llm/function-caller.ts`.

> await wiki.remember(`Tool call: ${functionCall.name}(${JSON.stringify(functionCall.args)}) → ${JSON.stringify(result).slice(0, 200)}`, {
> --- `apps/scopelab/src/lib/llm/function-caller.ts`

#### On [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

Downstream selection is narrower than stored bundle: tasks/events are excluded by supplied driver evidence, and formatContext defaults to ten facts. Answer system prompt asks use of memory and admission of ignorance when absent; judge receives question, dataset reference answer/rubric and model response. This resolves runtime's oracle-content uncertainty: the reference outcome is `q.answer`, not an additional store-truth check. Verdict does not admit revised knowledge and no feedback from this verdict into facts is established. SRC-1, `packages/benchmarks/src/longmemeval/judge.ts`, `packages/core/src/utils/formatContext.ts`.

> const values: Record<string, string> = { question: q.question, answer: q.answer, response };
> --- `packages/benchmarks/src/longmemeval/judge.ts`

> return text.trim().toLowerCase().startsWith('yes');
> --- `packages/benchmarks/src/longmemeval/judge.ts`

## Write side

The admission mechanisms must be kept apart from their physical storage executors:

| Mechanism | Authorship/proposal | Admission control and retained result | Later consumer |
|---|---|---|---|
| Event write | Caller supplies summary; ScopeLab explicitly supplies mixed conversation/tool-origin renderings | Code validates/clips and stores without extraction in deferred mode; calling the workflow is not per-derived-fact human review | Librarian/heal/read: [MEM-OBJ-events](#mem-obj-events) |
| Legacy/ops extraction | Provider derives assertions/tasks under host templates | Symbolic parsing, validity/dedupe/neighbor/operation rules; no universal human approval. Ops failed/rejected resolution can still retain content | Retrieval, subsequent maintenance: [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian) |
| Document extraction | Caller document, model-derived assertions | Runtime supplies full-replace versus partial-append distinction; partial success does not transfer complete source ownership | Later retrieval: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) |
| Remember/graph/import | Caller content/dump; upstream author unresolved | Code/DB constraints, caller-controlled adoption; model extraction not required. Transaction ownership differs for graph upsert | Read/graph/export: [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission), [RT-RTE-import-admission](runtime.md#rt-rte-import-admission) |
| Grounding/draft/trust | Model quote proposal, code occurrence test, optional caller reviewer metadata | Trust status insertion, not a truth oracle; draft can still be read by default | Ordinary retrieval and host views: [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata) |
| Heal | SQL aging plus provider revisions of retained knowledge | Per-batch ID guards, fact validation/dedupe, transactions; reasons not retained in the inspected output schema | Subsequent reads/heals: [MEM-RTE-heal-memory](#mem-rte-heal-memory) |
| Backfill/manifest | Caller or emergent provider vocabulary; model/classifier classifications | Software validates; classifier confidence gate; off-mode recheck; no mandatory human veto | Writer constraints and graph presentation: [MEM-RTE-ontology-backfill](#mem-rte-ontology-backfill) |
| Supersede/forget/prune | Caller change or configured age policy | Symbolic veto/retention rules; local transaction and post-commit hook boundaries | Current/history reads, outbox, external hooks: [MEM-RTE-temporal-history](#mem-rte-temporal-history), [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) |

Trace-fed knowledge here is event summary → extraction → retained assertions/tasks → later retrieval or maintenance. It is not merely logging. ScopeLab gives a specific mixed-origin witness, with abbreviation limits. Heal additionally transforms prior derived memory and operational access metadata. None of these paths alone establishes improved capacity. Embeddings transform text for selection; access counters transform use into retention/ranking influence, not explanatory claims. The imported entity summary is not evidence of compaction; no automatic raw-transcript → entity-summary → later-model chain is established. SRC-1 paths and source passages are retained in the linked records.

Rejection and withdrawal are not uniform. Dropping invalid fact syntax can prevent insertion; rejecting an ops resolution can still ADD; failed grounding can keep a draft; forget can commit locally before an ANN hook fails; prune can partially succeed. These distinctions determine what a later consumer can still retrieve. Version links retain old assertion text where not pruned, but do not preserve a criticism explaining its replacement. No route here is classified as a theory builder merely because it revises text; formulation, content-directed criticism, retained reasons and benefit require separate evidence not supplied by labels such as heal or knowledge-update.

## Read-back

Established request chains are ordinary read to a host bundle, ScopeLab selected text to Gemini, and benchmark reopened DB to answer prompt. Maintenance also re-reads retained material on automatic/manual schedules. Graph text and instructions_get provide documented external consumer affordances, but schema-only declarations are not proof of deployment wiring. MCP's eight registered tools address a remote service; transport-level search/remember/supersede/ingest names do not establish local-core retention semantics. The CLI's auth/config/status branches retain credentials/settings, not derived task knowledge; serve constructs the remote client and registers the tool server. SRC-1, `packages/mcp-server/src/commands.ts`, `packages/mcp-server/src/server.ts`, `packages/mcp-server/src/tools/index.ts`; [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools).

Working-context controls are primarily selection by value. Library code builds bounded maintenance prompts, drops lower-priority sections on retry and exposes selected returns to hosts. Removed prompt material remains in SQLite and can be selected by later reads; L3 truncation does not replace the stored fact with a summary. No inspected ScopeLab caller creates a separate subagent context or automatic history compaction. This is a bounded statement about that caller, not repository-wide absence of host compaction. The stack-frame analogy fits separate maintenance model requests only weakly: their input copies and parsed return escape, but they are service calls, not nested conversational agent frames. SQLite IDs remain reload handles only when a host calls an API; the model window contains text by value rather than automatically followable heap references. See [MEM-RTE-heal-memory](#mem-rte-heal-memory), [MEM-RTE-graph-context](#mem-rte-graph-context), [RT-RTE-memory-read](runtime.md#rt-rte-memory-read).

Source trust at actual consumption is narrower than stored trust state. ScopeLab renders title/body/tags under an advisory data wrapper; the benchmark formats assertions/confidence but does not render the full verification/source fields. Graph text drops bodies. Machine-confirmed grounding metadata therefore must not be treated as an automatically delivered reason or an enforced behavioral policy. The symbolic selector can exclude drafts when requested, but default read inclusion and graph-anchor exceptions prevent a universal quarantine guarantee. See [RT-BAP-memory-context](runtime.md#rt-bap-memory-context), [MEM-OBJ-entry-metadata](#mem-obj-entry-metadata), [MEM-RTE-graph-context](#mem-rte-graph-context).

## Integration issues

- **Ops rejection refinement:** runtime deliberately left helper veto rules unresolved. Direct source inspection now establishes stable ADD on rejected/missing op, draft on failed resolution, and draft alternatives for immutable targets. Preserve this distinction when reconciling [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian); treating rejected ops as discarded knowledge would be false. Supporting passages are in its annotation.
- **Oracle uncertainty resolved:** [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) leaves reference content unresolved. `judge.ts` supplies dataset `q.answer` or rubric, and prefix-yes parsing. This is additional source-supported detail, not measured correctness or a knowledge-admission oracle.
- **Potential overlap:** [MEM-BAP-manifest-guidance](#mem-bap-manifest-guidance) intersects [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) at writer prompt delivery but adds persisted manifest and classifier/code consumers; keep those parts distinguishable. [MEM-RTE-graph-context](#mem-rte-graph-context) and [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal) concern parallel TS/native implementations, not proven identical routes. [MEM-RTE-temporal-history](#mem-rte-temporal-history) explicitly declares containment in direct admission rather than competing identity. No other possible duplicates identified after comparison.
- **Upstream and remote lineage:** [MEM-OBJ-entity-summary](#mem-obj-entity-summary) and imported [MEM-OBJ-entry-vectors](#mem-obj-entry-vectors) have unresolved upstream authors/encoders; [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools) has opaque remote retention. These prevent assigning one origin, admission policy or model-update property to the entire system. Storage exposure is not a known later-model route for the summary.
- **Ontology initialization/helpers:** [MEM-OBJ-entity-manifests](#mem-obj-entity-manifests) records known host/emergent changes while leaving effective-state inheritance and helper enforcement details uninspected. [MEM-RTE-ontology-backfill](#mem-rte-ontology-backfill) does not establish globally sound types/relations. The supplied runtime's graph/ingest ownership and normalization helper limits also remain.
- **Withdrawal limits:** [MEM-RTE-memory-withdrawal](#mem-rte-memory-withdrawal) retains the sourceRef clearAll TODO and event survival. Do not translate metadataReset or deletion counts into complete source erasure, guaranteed source-index reset or prevention of reconstitution. External hooks/outbox consumers have independent success boundaries.
- **Consumer and evaluation limits:** ScopeLab's provider/storage mismatches from [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat) remain unresolved. Remaining UI hooks/subpanels, custom/native ranker branches and stored/integration evaluation results were not independently traced here. These prevent exhaustive UI policy, parity and measured-benefit conclusions, not the positive local storage/transformation findings above.

## Limitations and checks

Source identity was rechecked with git HEAD: `09c90258560a6b1664038d642b5d25d9de0c4d3d`; source checkout status was clean. Method identity is the supplied job, member type, worker rules and record contract read completely for this invocation; no alternate method revision was substituted. All evidence remains SRC-1. No target, test, example, provider, benchmark or remote tool was executed. A failed search for a guessed benchmark prompts path was corrected by reading the imported `judge.ts`; it was not treated as source absence.

The report establishes implemented transformations and wired/advisory consumers, not observed operation, reliable model compliance, truth, improved capacity or causal benefit. Only the listed paths/ranges were inspected directly; supplied runtime findings carry their own limits. Deterministic content validation is recorded below after the required check.

Validation: the required member content check passed after replacing the pending-status line and anchoring the repeated deletion-payload quote to the inspected orphan-deletion occurrence. An intervening invocation used an incorrect artifact path and failed before checking content; the subsequent check used the supplied path and passed. Validator result: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”
