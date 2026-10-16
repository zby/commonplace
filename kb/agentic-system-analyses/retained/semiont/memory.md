---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Semiont memory: event-backed knowledge, derived graph/vector/text stores, explicit retrieval and generation context selection."
run-id: AAS-2026-10-15-semiont-d516c7013d8f-01
source-identity: https://github.com/The-AI-Alliance/semiont
reviewed-boundary: a920067ac4ea63a57b1855b7d263485fbd22bab4
---

# Semiont memory report

## Boundary and evidence

This account covers Semiont's retained knowledge and the routes that maintain it and return it to later clients or models. The frozen source is SRC-1 at a920067ac4ea63a57b1855b7d263485fbd22bab4; HEAD was rechecked. The [boundary](boundary.md#source-register) supplies source identity and evidence layers. All new evidence below is implementation or explicitly labelled doctrine/design, not observed operation. No target program, model, test or example was executed.

The memory scope includes resource bytes and events, materialized views, annotation prose and links/tags, graph projection, dense vectors and their readable payloads, extraction outcomes, negative extraction decisions, queue recovery state, explicit browse/search/gather, generated-resource read-back, and shipped composition instructions. It is not limited to the ordinary MCP generation path. Worker and Librarian model parameters remain externally served opaque state, not the same retained object as the knowledge they read. External assistant conversation compaction, provider-internal training/retention, actual deployment policy and external corpora are outside this inspection. These limits prevent conclusions about those hosts' memory behavior, factual quality or production outcomes.

The supplied runtime established generation, annotation detection, direct upload and request-local repair. I directly inspected the additional paths below and reread annotation gathering, generation prompt selection, content storage and Archivist commands. The boundary remains a complete artifact with a partial-loop account; listed but uninspected paths are not unavailable evidence.

| Entry point / memory operation | Source path under SRC-1 | Coverage and prevented conclusion |
|---|---|---|
| Upload; delegated yield; mark jobs; PDF repair | `apps/worker/src/semiont_worker/held_job.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`, `apps/archivist/src/commands.rs` | Supplied [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection), [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair); prompt and admission reread directly. Recovery details beyond supplied findings remain bounded. |
| Record append; boot replay; Git staging | `apps/archivist/src/archivist.rs`, `apps/archivist/src/main.rs`, `apps/archivist/record/src/record.rs`, `apps/archivist/record/src/log.rs`, `apps/archivist/record/src/view.rs`, `apps/archivist/staging/src/git.rs` | Direct: [MEM-RTE-record-replay](#mem-rte-record-replay). No automatic Git commit or remote durability follows from staging. |
| Clone, update, body edit, delete, archive, unarchive, vocabulary | `apps/archivist/src/commands.rs`, `apps/archivist/src/bus.rs`, `apps/archivist/src/content.rs` | Direct: [MEM-RTE-content-revision](#mem-rte-content-revision), [MEM-RTE-annotation-edit](#mem-rte-annotation-edit). Full gateway authorization for every command not audited. |
| Graph event following, catch-up, reconcile, rebuild | `apps/weaver/src/semiont_weaver/weaver.py`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/weaver/src/semiont_weaver/checkpoint.py` | Direct: [MEM-RTE-graph-maintenance](#mem-rte-graph-maintenance). Service wiring identified in `apps/weaver/src/semiont_weaver/service.py`; every backend's persistence/isolation not audited. |
| Vector/extraction update, declines, repair, index compatibility | `apps/smelter/src/semiont_smelter/smelter.py`, `apps/smelter/src/semiont_smelter/reconcile.py`, `apps/smelter/src/semiont_smelter/service.py`, `apps/smelter/src/semiont_smelter/index_stamp.py`, `apps/smelter/src/semiont_smelter/anchored_text_store.py` | Direct: [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance). Extractor/OCR algorithms and all store backend operations not exhaustively inspected; accuracy and distributed atomicity unestablished. |
| Extracted-text HTTP read and later gather | `apps/archivist/src/anchored.rs`, `apps/librarian/src/semiont_librarian/resource_text.py` | Direct: [MEM-OBJ-anchored-text](#mem-obj-anchored-text), [MEM-RTE-resource-gather](#mem-rte-resource-gather); PDF source maps are derived memory, not merely search metadata. |
| Resource gather and annotation gather | `apps/librarian/src/semiont_librarian/resource_gather.py`, `apps/librarian/src/semiont_librarian/annotation_gather.py` | Direct: [MEM-RTE-resource-gather](#mem-rte-resource-gather), annotation on [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather). Graph barrier internals not fully audited; response completeness not guaranteed. |
| Text and reference search | `apps/librarian/src/semiont_librarian/text_search.py`, `apps/librarian/src/semiont_librarian/reference_search.py` | Direct: [MEM-RTE-resource-search](#mem-rte-resource-search), [MEM-RTE-reference-search](#mem-rte-reference-search). Scoring formula details and ranking quality not evaluated. |
| MCP registered dispatch, browse, match, bind, direct upload and gather | `packages/mcp-server/src/tools.ts`, `packages/mcp-server/src/handlers.ts` | Direct tool roster/dispatch cross-check: [MEM-RTE-mcp-browse](#mem-rte-mcp-browse) and supplied runtime routes. Tool display text can omit the retrieved passage. |
| CLI dispatch and upload/gather | `apps/launcher/main.go`, `apps/launcher/internal/verbs/gather.go`, `apps/launcher/internal/verbs/yield.go` | Direct: CLI dispatch includes browse/gather/mark/match/frame/yield; gather exposes resource focus as well as annotation focus, and yield uploads local bytes. Remaining verb internals not traced: no CLI parity claim. |
| UI context hooks and review/composition surfaces | `packages/react-ui/src/components/modals/GatherContextStep.tsx`, `packages/react-ui/src/components/modals/ResourceGenerateModal.tsx` | Direct bounded UI reads show context display, hint and Search/Generate/Compose callbacks; model admission is not universally human-gated. Full Browser/desktop host and SDK state-unit lifecycle uninspected; prevents claims about all human edits, UI persistence and automatic refresh. |
| Shipped skills and watchers | `docs/builder/skills/semiont-aggregate/SKILL.md`, `docs/builder/skills/semiont-assess/SKILL.md`, `docs/builder/skills/semiont-session/SKILL.md` | Direct doctrine/design: [MEM-RTE-aggregate-writing](#mem-rte-aggregate-writing); session example affords event-driven annotation, not deployed autonomous ingestion. Ingest/wiki/other skills not fully read; no exhaustive instructional policy claim. |
| Evaluation | `tests/conformance/librarian/README.md`, source specification references in Smelter/Weaver modules | Direct evaluation-design read: scripted models and embedding stand-ins with real surrounding writers/stores. Harness assertions/results not inspected or run; prevents accuracy, efficacy and passing-suite claims. |

## Core ideas

1. **The record and the content file are different durable objects.** Events preserve changes and attribution; current views replay those events, while resource bytes live at a mutable storage URI. A record of an earlier checksum is not an immutable copy of those bytes. Git staging is not Git history. [MEM-OBJ-event-log](#mem-obj-event-log), [MEM-OBJ-content](#mem-obj-content), [MEM-RTE-record-replay](#mem-rte-record-replay).
2. **The graph, vectors and anchored text are different derivations with different repairs.** Graph repair replays recorded events. Vector repair compares live catalog, checksums, media types and entity types. Anchored text is cached by content checksum plus extraction stamp. A remembered decline also shapes later work: unchanged unreadable bytes are not repeatedly reprocessed at startup. [MEM-RTE-graph-maintenance](#mem-rte-graph-maintenance), [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance).
3. **Read-back is request-directed, then narrowed again at the consumer.** Resource/annotation gathers assemble selected retained knowledge; the Worker independently clips and selects the fields sent to its model. Summaries returned by a gather are request-local derivations unless a caller explicitly saves them. The MCP text-search wrapper returns names/IDs/types rather than the semantic passage its underlying service found. [MEM-RTE-resource-gather](#mem-rte-resource-gather), [MEM-RTE-mcp-browse](#mem-rte-mcp-browse), [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt).
4. **Provenance and quality have different controls.** An assigned worker can admit generated resource bytes and creation events without per-item human approval. Source binding/linking is separate from generated citations: the traced Worker's nonempty citation batch targets the new resource, whose log lacks the job assignment, so that batch is refused. Citation-token processing is not durable citation provenance. Caller-authored direct writes also exist. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation). Attribution, schema, checksum and compiler checks do not prove a factual claim. Assessment prose can subsequently enter a generation or reference-ranking prompt, but it is not automatically a veto or a revised system policy. [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [MEM-RTE-annotation-edit](#mem-rte-annotation-edit), [MEM-RTE-reference-search](#mem-rte-reference-search).

## Shared records

### Components

#### MEM-CMP-smelter-embedding
Label: Smelter embedding provider

Source-native identity: `provider` constructed by Smelter `boot` through `create_embedding_provider`. Unlike [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), whose referent is the Librarian query client, this client produces retained resource/annotation vectors. Same factory does not make the clients identical. Representational form: distributed-parametric embedding computation; substrate: external model weights, local access configuration, resulting vectors in a separately managed index. Parameters are not updated by the inspected document-embedding calls; provider-side changes are uninspected. Exact version is a configured provider/model name, not an immutable weights digest. Mutable endpoints may resolve differently; an index stamp records provider type/model and chunking, not remote weight identity. SRC-1, `apps/smelter/src/semiont_smelter/service.py`, `apps/smelter/src/semiont_smelter/index_stamp.py`; factory choices are also supplied in the runtime embedding record.

> provider = create_embedding_provider(config.embedding, api_key=embedding_key_of(config, environment))
> --- `apps/smelter/src/semiont_smelter/service.py`

#### MEM-CMP-matcher
Label: Librarian Matcher inference

Source-native identity: `started.matcher`, independently configured from `started.gatherer`. This differs from [RT-CMP-gatherer](runtime.md#rt-cmp-gatherer) and [RT-CMP-worker-inference](runtime.md#rt-cmp-worker-inference): its consumer task is candidate rescoring, not summarization or document generation. Representational form: external distributed-parametric inference with symbolic access configuration and natural-language ranking input. Storage: remote weights, local client configuration; returned scores are request state. No parameter update is requested by the inspected scoring route; provider internals remain uninspected. Exact model version is not universally pinned to immutable weights. Configured base URL/model may resolve to a different model. SRC-1, `apps/librarian/src/semiont_librarian/service.py`, `apps/librarian/src/semiont_librarian/reference_search.py`.

> model: LibrarianModelConfig = config.matcher if actor == "matcher" else config.gatherer
> --- `apps/librarian/src/semiont_librarian/service.py`

### Operative objects

#### MEM-OBJ-content
Label: Resource content file

Source-native identity: file addressed by a representation's `storageUri`; storage substrate: the KB working tree. Text/Markdown is natural-language knowledge at human/model readers; JSON or program text can be symbolic at format-specific consumers; PDF bytes are an encoded document, not themselves a readable prose summary. Their extracted text is separately [MEM-OBJ-anchored-text](#mem-obj-anchored-text). The content object's authority depends on the later route, not the filename. Lineage can be direct caller bytes, a local CLI file, a clone or Worker output. Originating human control is unresolved for a generic direct caller. Distinct from [RT-OBJ-job-params](runtime.md#rt-obj-job-params), the transient request that may cause its creation; produced through [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). SRC-1, `apps/archivist/src/content.rs`, `apps/launcher/internal/verbs/yield.go`.

> /// Put `bytes` at `uri`: to a file beside the target, renamed onto it.
> --- `apps/archivist/src/content.rs`

#### MEM-OBJ-event-log
Label: Record log and materialized views

Source-native identity: `Record.log`, `Record.views`, `Record.projections` and URI index; symbolic event envelopes and deterministic state projections. Resource streams are sharded JSONL under `.semiont/events`; views/projections are files in a service state directory. Events retain payloads, not independent semantic verification. Payload content is distinguished in [MEM-OBJ-annotation-text](#mem-obj-annotation-text), [MEM-OBJ-annotation-links](#mem-obj-annotation-links) and resource files. Log lineage is accepted commands plus recorded job lifecycle; current views are derived replay results, not raw traces. Later consumers include browse/gather and projection repair; event types/sequence numbers have fixed code authority there. No supplied object has this referent; [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission) describes one producing route, not the store. SRC-1, `apps/archivist/record/src/log.rs`, `apps/archivist/record/src/record.rs`, `apps/archivist/record/src/view.rs`, `apps/archivist/src/main.rs`.

> events_dir: root.join(".semiont").join("events"),
> --- `apps/archivist/record/src/log.rs`

> let Appended { event, changed } = self.log.append(&stream, event)?;
> --- `apps/archivist/record/src/record.rs`

#### MEM-OBJ-annotation-text
Label: Annotation comment and assessment prose

Source-native identity: `TextualBody.value` for commenting/assessing. Representational form: natural language; substrate: event payload and current annotation view, then graph body where projected. Human/manual or model detection can author it; attribution is derived by the record. Semantic correctness and initial human decision remain independent of transport identity. The text can retain an explanation of a flagged concern, unlike a scalar job count. Actual later consumers include the generation prompt's first textual body and reference scoring's first body with commenting/assessing purpose; neither consumes every body indiscriminately. Distinct retained output of [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection), not a duplicate of that route or its worker model. SRC-1, `apps/archivist/src/commands.rs`, `apps/worker/src/semiont_worker/generation/resource_generation.py`, `apps/librarian/src/semiont_librarian/reference_search.py`.

> parts.append(f"- {label}: {first.value}")
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

#### MEM-OBJ-annotation-links
Label: Annotation selectors, tags and bindings

Source-native identity: annotation target selectors, tagging body values and `SpecificResource` linking bodies. Symbolic IDs, positions, exact-quote anchors and vocabulary tags guide fixed source resolution, graph edges and filters; the quoted passage separately becomes natural-language model context. Storage: event payloads/current views and derived graph/index metadata. These are not the evaluative prose in [MEM-OBJ-annotation-text](#mem-obj-annotation-text): body operations can change a binding/type without re-embedding quoted text. Distinct output/control data associated with [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection) and [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), not either supplied referent. SRC-1, `apps/archivist/src/commands.rs`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/smelter/src/semiont_smelter/smelter.py`, `packages/mcp-server/src/handlers.ts`.

> await self._index.update_annotation_entity_types(annotation.id, types)
> --- `apps/smelter/src/semiont_smelter/smelter.py`

#### MEM-OBJ-graph
Label: Graph projection

Source-native identity: `GraphDatabase` passed to `Weaver`; symbolic resource nodes, annotation objects and relationships, with annotation prose values retained for separate interpretation. Substrate: configured graph store; exact deployment/backend correctness not supplied. Lineage: deterministic fold of recorded events, not independent discovery by a model. Consumers: Librarian graph traversal/listing, candidate selection and context derivation. Its descriptive authority is bounded by what the fold represents, not equivalence to every field of the record. No supplied store record has this identity; [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather) is a consumer. SRC-1, `apps/weaver/src/semiont_weaver/fold.py`, `apps/weaver/src/semiont_weaver/weaver.py`.

> if written(annotation) != written(intended_graph_annotation(recorded)):
>     return "annotation-content-mismatch"
> --- `apps/weaver/src/semiont_weaver/weaver.py`

#### MEM-OBJ-vector-points
Label: Resource and annotation vectors

Source-native identity: resource-chunk embeddings and annotation quote embeddings in `VectorStore`; distributed numerical representation, separately from provider weights. Substrate: configured vector database, with Qdrant implementation inspected at its declared collection boundary; actual live store not observed. Lineage: current decoded/extracted source text → chunking or quote extraction → [MEM-CMP-smelter-embedding](#mem-cmp-smelter-embedding) → points. Consumers compare vectors and return scores/passages, not human-readable reasons encoded in vector dimensions. No weight training is implied. Distinct from the query provider [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), and the retained data whose population the supplied gather route left open. SRC-1, `packages/vectors-python/src/semiont_vectors/store.py`, `packages/vectors-python/src/semiont_vectors/qdrant.py`, `apps/smelter/src/semiont_smelter/smelter.py`.

> embeddings = await self._provider.embed_documents(chunks)
> --- `apps/smelter/src/semiont_smelter/smelter.py`

#### MEM-OBJ-vector-payload
Label: Search passage and point metadata

Source-native identity: `EmbeddingChunk.text`, `AnnotationPayload`, `ResourceStamp`, `VectorSearchResult`. Stored alongside vectors: readable text passages are natural-language evidence at a later model/human consumer; IDs, checksums, media type, entity types, motivation and `machine_read` flags are symbolic access/lineage metadata. These parts differ from opaque numerical [MEM-OBJ-vector-points](#mem-obj-vector-points): the prompt receives the text and an OCR warning, not the vector. No supplied object duplicates this payload; [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather) returns selected parts. SRC-1, `packages/vectors-python/src/semiont_vectors/store.py`, `apps/smelter/src/semiont_smelter/smelter.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`.

> exact_text: str
> """The text the annotation quotes: what its vector was made of."""
> --- `packages/vectors-python/src/semiont_vectors/store.py`

> "treat their exact wording and numbers as uncertain, and say so if you rely on one."
> --- `apps/worker/src/semiont_worker/generation/resource_generation.py`

#### MEM-OBJ-anchored-text
Label: Anchored text extraction outcome

Source-native identity: `AnchoredTextStore` entries, extracted text/word geometry/derivation fields or an extraction decline. Substrate: sharded checksum-keyed JSON plus root `STAMP`; entry format version 3. Text is derived natural-language content, geometry/offsets/method/stamp and decline codes are symbolic control/provenance. Raw input is document bytes, not an assistant conversation trace. Smelter writes outcomes after extraction and reads them to avoid recomputation; Archivist reads under the writer's stamp; Librarian obtains text through anchored-text requests and later sends selected prose into gather/generation. Geometry supports anchoring rather than functioning as a model summary. An outcome retains extraction method and, where present, confidence/coverage information; this does not authenticate wording. No supplied operative object duplicates this cache; [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather) is a later consumer. SRC-1, `apps/smelter/src/semiont_smelter/anchored_text_store.py`, `apps/smelter/src/semiont_smelter/smelter.py`, `apps/archivist/src/anchored.rs`, `apps/librarian/src/semiont_librarian/resource_text.py`.

> held = await self._anchored.read(checksum)
> if held is not None:
>     return held
> --- `apps/smelter/src/semiont_smelter/smelter.py`

> return answer.text if isinstance(answer, ExtractedText) else None
> --- `apps/librarian/src/semiont_librarian/resource_text.py`

#### MEM-OBJ-declined
Label: Remembered resource decline

Source-native identity: `Declined(content_checksum, media_type, reason)` in vector-store decline state. Symbolic extraction outcome metadata, not a semantic embedding, prose criticism or raw log. Substrate: vector-store bookkeeping; Qdrant uses a separate non-search collection. Lineage: bytes read but no usable text → code decision → remembered checksum/type/reason. Later consumer: startup reconcile suppresses repeated extraction for unchanged declined bytes/type, while changed content/type becomes eligible again. Distinct from [RT-OBJ-job-params](runtime.md#rt-obj-job-params) and from transient job decline messages: this is durable maintenance control. SRC-1, `packages/vectors-python/src/semiont_vectors/store.py`, `packages/vectors-python/src/semiont_vectors/qdrant.py`, `apps/smelter/src/semiont_smelter/reconcile.py`.

> if remembered is None or (remembered.content_checksum, remembered.media_type) != (catalog.checksum, catalog.media_type):
> --- `apps/smelter/src/semiont_smelter/reconcile.py`

#### MEM-OBJ-weaver-checkpoint
Label: Weaver sequence marks

Source-native identity: `Checkpoint`, resource-ID → applied sequence number JSON file. Symbolic recovery metadata, not content, learned instructions or a compacted conversation. Written atomically via a sibling temporary file; missing/unreadable state gives an empty mapping. Later Weaver startup uses marks to select unprocessed events; a mark ahead of record history triggers rebuilding. Distinct from [RT-OBJ-job-params](runtime.md#rt-obj-job-params) and Worker unit/cursor checkpoints: different producer, substrate and consumer. SRC-1, `apps/weaver/src/semiont_weaver/checkpoint.py`, `apps/weaver/src/semiont_weaver/weaver.py`.

> self._marks.keep(await self._checkpoint.load())
> --- `apps/weaver/src/semiont_weaver/weaver.py`

### Routes

#### MEM-RTE-record-replay
Label: Record append and replay

Endpoints/progression: accepted Archivist command → JSONL append → deterministic view/projection/index updates → staging/fact publication; boot rebuild → later view consumers. Owner: Archivist/Record code. Distinct from [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), which covers one admission path, this spans retained event state and replay for multiple commands. SRC-1, `apps/archivist/src/archivist.rs`, `apps/archivist/record/src/record.rs`, `apps/archivist/src/main.rs`, `apps/archivist/staging/src/git.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stored event or command response; a downstream failure can occur after the log line was written.
- Later read-back: next view requests and boot replay receive accumulated accepted resource/annotation/job events; Weaver consumes event history for projection repair.
- Delegated visibility: published facts include current annotation for added/body-updated annotations; deployment audience is not audited here.
- Selection predicate: stream selected by resource ID or system stream; boot rebuild reads histories and rebuilds views, reaping views with no stream.
- Invalidation or expiry: views are replaceable projections; rebuild is skipped only when configured; historical event payloads are not removed by deleting a current annotation.
- Activation or effect: fixed event rules alter subsequent visible state; no model reliance or benefit observed.
- Evidence limits: no atomic transaction across file content, log, views, bus and remote stores; crash durability and remote backup unestablished.

Admission follows each command's local checks, not a new truth oracle at replay. Proposal author may be caller or Worker; code admits, can refuse before append, and later repairs from the log. Open-request operation; deterministic event history is the reconstruction reference, not an expected factual answer. Persisted material is the accepted payload and metadata, not a generalized improvement method.

> let recorded = record.append(event)?;
> for path in &recorded.changed {
>     self.staging.stage(path);
> }
> --- `apps/archivist/src/archivist.rs`

> //! the index is for people who commit by hand, so it must be current within
> --- `apps/archivist/staging/src/git.rs`

#### MEM-RTE-content-revision
Label: Content revision and clone

Endpoints/progression: `yield:update` registers an existing file and records checksum/size; clone-persist registers copied content under a fresh identity; token-based clone-create derives parent types and may archive the original. Owner: Archivist code; caller supplies bytes/metadata and chooses operation. This is an alternative to [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), not its generated-resource referent. SRC-1, `apps/archivist/src/commands.rs`, `apps/archivist/src/content.rs`, `apps/archivist/record/src/view.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resource ID or refusal, including missing/mismatched content or invalid/expired token.
- Later read-back: updated primary checksum/size or cloned descriptor is materialized for later browse/gather and Smelter reindexing.
- Delegated visibility: symbolic lineage is `parentResourceId`/`sourceResourceId` for clones; generation lineage is a separate path.
- Selection predicate: caller-named resource/storage URI; token path resolves a recorded source with a valid held token; direct clone-persist is a distinct exposed operation.
- Invalidation or expiry: token lifetime is fifteen minutes and successful clone-create consumes it; content updates supersede current checksum, not a saved copy of old bytes.
- Activation or effect: new/current resource state and optional original archive; downstream derived stores can lag.
- Evidence limits: no proof of universal graph handling of clone/update events; fold coverage differs from view/Smelter coverage. No universal content-version rollback established.

Admission is software checksum/identity/attribution control over caller-authored open requests; generic identity leaves human-versus-computation control unresolved. Code can refuse; there is no inspected semantic oracle or per-content approval step. The old content file need not survive overwrite; metadata history alone cannot restore it. SRC-1, `apps/archivist/src/content.rs`, `apps/archivist/src/commands.rs`.

> archivist.append(event(YieldUpdated::NAME, Some(resource_id), user, payload))?;
> --- `apps/archivist/src/commands.rs`

#### MEM-RTE-annotation-edit
Label: Annotation and vocabulary maintenance

Endpoints/progression: direct create/batch commit/body operations/delete/type registration/archive/unarchive → Archivist events/views → graph/vector followers → later reads. Owner: caller chooses proposal; Archivist applies local checks; followers project accepted results. Distinct from [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection): these are direct content/adoption/withdrawal surfaces, not the model detection job. SRC-1, `apps/archivist/src/commands.rs`, `apps/archivist/record/src/view.rs`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/smelter/src/semiont_smelter/smelter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: IDs/empty acknowledgment or refusal; batch commits skip already-present IDs.
- Later read-back: current bodies/selectors/types affect gather, filtering and reference search; deletion removes current annotation, not its historical event.
- Delegated visibility: creator/attribution is record-derived; worker-role batch commits must cite a matching assignment, while direct create remains a distinct route.
- Selection predicate: command-named resource/annotation and body operations; added resource types must be registered; body updates are not truth checks.
- Invalidation or expiry: delete removes current annotation and its graph/vector representation when followed; archive sets archived state and may remove the named file unless kept; unarchive with URI refuses a missing file.
- Activation or effect: binding edits change graph relationships, type edits change filters, and prose edits can alter later prompts. Archive removes resource and annotation vectors; it is not guaranteed erasure of all copies.
- Evidence limits: exact host authorization, UI confirmation and every body-operation validation path uninspected; factual evaluation/admission is not implied by `assessing` motivation.

Authorship and admission are separate: a human, script or model may author direct inputs; software derives attribution and records acceptable commands. Starting detection is not approval of each result. Existing prose can be replaced/removed and resources archived, but there is no all-store rollback transaction. Open-request mode; admission checks protocol and vocabulary, with no independent expected-answer oracle. Registered tag schemas/types persist as symbolic guidance for subsequent jobs; annotation concern text persists as content, not a compulsory policy. SRC-1, `apps/archivist/src/commands.rs`; [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection).

> archivist.append(event(MarkRemoved::NAME, Some(resource_id), user, payload))?;
> --- `apps/archivist/src/commands.rs`

#### MEM-RTE-graph-maintenance
Label: Graph following and repair

Endpoints/progression: recorded events → per-resource lanes → fold → graph → application marks/signals; startup checkpoint catch-up/reconcile or explicit rebuild replays history. Owner: Weaver symbolic code. Distinct from consumer [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather); no supplied record covers projection maintenance. SRC-1, `apps/weaver/src/semiont_weaver/weaver.py`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/weaver/src/semiont_weaver/checkpoint.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: projection signals, startup summaries or rebuild success/failure; following itself has no terminal answer.
- Later read-back: Librarian uses retained graph nodes/annotations; later Weaver boot reads saved marks and recorded history.
- Delegated visibility: graph holds codec-defined record fields; not every descriptor or annotation field is copied.
- Selection predicate: event type and per-resource sequence marks; reconcile checks node presence, archived/types, annotation membership and codec-projected annotation content.
- Invalidation or expiry: applied-event deduplication; rewind ahead of last event clears marks/rebuilds; divergent resource rebuild deletes graph resource and replays events; all-rebuild clears database.
- Activation or effect: retained symbolic knowledge becomes graph search/traversal input; repair rewrites projection, not the source assertion's truth.
- Evidence limits: caught failures can leave incomplete projection; inspected fold handles creation, archive/unarchive, annotation addition/removal/body and type changes, not every view event.

This is automatic maintenance using recorded state as reference outcome, not model diagnosis. Code decides rebuild and can report failure; no per-event human approval is in the follower. Triggers are startup, received events or commanded rebuild, not a content-improvement curriculum. Input history and checkpoints persist; logs explain divergence locally, while later replay depends on events/marks, not retained prose reasons. A rebuilt graph can improve consistency without demonstrating improved model capacity.

> await self._graph.delete_resource(resource_id)
> events = await self._history.events(resource_id)
> --- `apps/weaver/src/semiont_weaver/weaver.py`

#### MEM-RTE-vector-maintenance
Label: Index extraction and repair

Endpoints/progression: retained resource/annotation events or startup reconcile → read bytes/current catalog → decode/extract/cache → chunk/quote embed → point/payload writes; archive/delete removes points. Owner: Smelter code, embedding provider computes vectors. Distinct from [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider) and supplied gather routes: this produces the stored data they query. SRC-1, `apps/smelter/src/semiont_smelter/smelter.py`, `apps/smelter/src/semiont_smelter/reconcile.py`, `apps/smelter/src/semiont_smelter/index_stamp.py`, `apps/smelter/src/semiont_smelter/service.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `smelt:settled` indexed/skipped, reconcile health state or rebuild response; unread bytes produce no settled decision.
- Later read-back: resource/annotation search and gathers receive vectors' readable passages; startup consumes stamps/declines; later extraction reads cached text/decline.
- Delegated visibility: payload preserves resource/annotation IDs, quote/chunk, type/checksum/media metadata and OCR marker, not provider reasoning or source truth.
- Selection predicate: catalog live resources, media-type text capability, primary representation, current annotation quotes, configured chunk size/overlap; non-whitespace quotes only are embedded.
- Invalidation or expiry: archive removes resource and annotation vectors; removal unindexes annotation; body edits restamp types without re-embedding quote; startup checksum/media mismatch re-embeds, types mismatch restamps, missing map reanchors; provider/model/chunking stamp mismatch recreates index before reconcile.
- Activation or effect: changed or suppressed future indexing, search results and model-visible passages; no improved retrieval/model behavior observed.
- Evidence limits: all resource chunks are embedded before point submission, preserving prior points on embedding failure, but no atomicity across all stores is established; remote silent model drift can evade name-based stamp checking.

Admission and curation: software accepts extraction output according to media/extraction rules, not human review; provider computes embeddings, not accept/reject factual judgments. Bytes read with no text produce a retained decline and old vectors are removed/replaced by decline state; unread bytes preserve existing index because no decision is known. Startup declines suppress repeated work for matching checksum/type. This is an automatic outcome-fed update with a durable behavior-shaping result, unlike retaining raw log messages alone. Its original trace is the extraction result of source bytes, not a dialogue or general agent experience. The reason is retained and later reconcile consults checksum/type state; it does not interpret an explanatory prose rationale. Open-ended maintenance, not a bounded learning experiment; reference outcome is current catalog/extraction result, not an expected semantic answer. Recovery re-derives from source/cache, and can leave lag if reconcile fails. SRC-1, `apps/smelter/src/semiont_smelter/smelter.py`, `apps/smelter/src/semiont_smelter/reconcile.py`.

> await self._index.delete_annotation_vectors_for_resource(resource)
> --- `apps/smelter/src/semiont_smelter/smelter.py`

> declined = Declined(content_checksum=read.checksum, media_type=read.content_type, reason=read.reason)
> await self._index.decline_resource(resource, declined)
> --- `apps/smelter/src/semiont_smelter/smelter.py`

> await index.make_anew(stamp)
> --- `apps/smelter/src/semiont_smelter/index_stamp.py`

#### MEM-RTE-resource-gather
Label: Resource context gathering

Endpoints/progression: resource-focused request → current view/text → graph neighborhood/related text → optional summaries/suggestions → stored-vector similarity → `GatheredContext` → client and optionally delegated generation. Owner: Librarian code; caller sets inclusion/depth/budget; model generates optional prose. Distinct alternative focus to [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), sharing stores but not annotation/window selection. SRC-1, `apps/librarian/src/semiont_librarian/resource_gather.py`, `apps/librarian/src/semiont_librarian/resource_text.py`, `apps/launcher/internal/verbs/gather.go`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: gathered context or failure; auxiliary inference/vector timeout failures may degrade fields rather than fail all gathering.
- Later read-back: current retained resource, related documents, graph and vector passages reach a later request; generated summary is not persisted by this gather.
- Delegated visibility: focus content only when requested; summary/suggestions where requested and available; Worker then applies its own field/clipping selection.
- Selection predicate: requested resource ID; depth 1–3; nearest related graph resources capped at max-resources minus one; content/summary flags; vector resource-similarity limit max-resources, floor 0.5, optional excluded types.
- Invalidation or expiry: request-local snapshot; when no similarity hits and matching content is not indexed, bounded wait for matching checksum settlement and retry only when indexed; submitted job copies do not automatically refresh.
- Activation or effect: selected content is wired to optional subsequent generation; actual reliance/benefit unobserved.
- Evidence limits: summary may omit facts and matches may lack readable views; stored source text can be absent or stale relative to separate projections. No universal total prompt-token budget established.

Working-context control is per-request assembly, not compaction of an external assistant's turns. Code keeps unrelated resources outside the frame; returned context escapes. Resource content is subsequently capped at 4,000 code points each by Worker, semantic passages at three × 240. Originals remain reachable through new read/gather requests, but IDs in a prompt are not automatic dereference operations. SRC-1, `apps/worker/src/semiont_worker/generation/resource_generation.py`.

> peers = [node for node in around.nodes if isinstance(node, GraphResourceNode) and node.id != resource_id]
> --- `apps/librarian/src/semiont_librarian/resource_gather.py`

> limit=options.max_resources,
> score_threshold=LIKE_ENOUGH,
> --- `apps/librarian/src/semiont_librarian/resource_gather.py`

#### MEM-RTE-resource-search
Label: Resource text search

Endpoints/progression: text query → graph lexical listing → only empty first page permits query embedding/vector fallback → fold chunks by resource → hydrate graph/view → preview/service reply. Owner: Librarian code. Distinct from [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather): a search query, not selected annotation context. SRC-1, `apps/librarian/src/semiont_librarian/text_search.py`, `apps/librarian/src/semiont_librarian/resource_text.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resource page with lexical/semantic kind and content/preview; MCP display is narrower.
- Later read-back: retained graph metadata or stored vector text reaches a later query client; ranking results are not automatically retained as knowledge.
- Delegated visibility: semantic service result carries matched passage; lexical preview is first 200 code points only for byte-decoded text, not PDF extracted text.
- Selection predicate: trimmed search, entity/archive filters, offset and limit (default 50); graph result wins if it matched anything, offset is later, or archive-only; fallback requests four chunks per requested resource, merges by resource and applies configured semantic floor.
- Invalidation or expiry: fresh query and hydration; absent views/resources drop hits; projection lag remains possible.
- Activation or effect: code selects displayed candidates; no automatic knowledge edit and no measured usefulness.
- Evidence limits: graph failure raises; embedding/index failure normally becomes empty lexical result except absent collection raises. Empty result is not proof of no relevant knowledge.

> if lexical.total > 0 or offset > 0 or filters.archived is True:
> --- `apps/librarian/src/semiont_librarian/text_search.py`

#### MEM-RTE-reference-search
Label: Reference candidate selection

Endpoints/progression: reference plus gathered annotation context → name/type/neighborhood/vector candidate union → structural scores → optional Matcher scores of top twenty → ordered bounded reply; separate bind operation adopts a candidate. Owner: Librarian code selects and ranks; caller chooses whether to bind. Distinct from [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), which prepares context rather than chooses binding candidates. SRC-1, `apps/librarian/src/semiont_librarian/reference_search.py`, `packages/mcp-server/src/handlers.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: scored candidates with match reasons, not an accepted link.
- Later read-back: retained graph resources and vectors are reread; annotation comment/assessment body and gathered relationships enter candidate rescoring.
- Delegated visibility: Matcher receives selected passage, hint, motivation, first relevant body text, source/entity/context descriptors and candidate descriptions; not a full conversation or entire corpus.
- Selection predicate: name list up to 20, type list up to 50, context neighbors, vector hits up to 40 at 0.4 excluding source; deduplicate resources, score, model top 20 unless disabled, rerank and apply requested limit.
- Invalidation or expiry: per-request scores; model failure retains structural ordering; separate binding can persist chosen relationship via body update.
- Activation or effect: scores change returned order when parsed; later binding and downstream behavior are unobserved, not inferred from ranking.
- Evidence limits: model judgment is not an answer oracle; scoring formula quality and every external/UI consumer not assessed.

This is open-request candidate comparison, not automatic adoption. Code and model propose ordering; caller can reject all or submit a bind. Human role of a generic caller is unresolved. No immutable expected target is supplied. Guidance is context, hint and static scoring prompt; scores/reasons in reply do not themselves become a learned policy. Body editing/deletion supplies reversal of an adopted binding, not retroactive repair of all generated documents.

> shown = [resource for resource, _ in scored[:MOST_SHOWN]]
> --- `apps/librarian/src/semiont_librarian/reference_search.py`

#### MEM-RTE-mcp-browse
Label: MCP retained-knowledge display

Endpoints/progression: registered tool call → SDK fresh resource/annotation/search request → JSON or formatted text tool result → external MCP client. Owner: fixed handler code and caller choice of tool. Distinct from the generation/read-context routes supplied by runtime: display-only alternatives are material consumers. SRC-1, `packages/mcp-server/src/tools.ts`, `packages/mcp-server/src/handlers.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resource JSON; resource lists; quoted highlight lines; reference exact text and linked ID/stub; match names/IDs/types; gather JSON in its separate tool.
- Later read-back: stored descriptors and annotation quotes/bindings reach a later tool invocation; no new persisted memory from formatting alone.
- Delegated visibility: `match_resources` omits matched content/scores in its list display; browse-resource returns descriptor data, not a claim that raw bytes were fetched.
- Selection predicate: caller ID or search/filter; browse resources defaults archived false; local motivation filters select highlighting/linking annotations.
- Invalidation or expiry: `.fresh()` requests and local output formatting; host retention/eviction of tool results uninspected.
- Activation or effect: delivery to external client, with no evidence of external model compliance or automatic reload.
- Evidence limits: tool presence is implemented access, not an enclosing host's memory policy, context budget or proactive injection.

> return resources.map(d => `- ${d.name} (${d['@id']}) — ${d.entityTypes?.join(', ') || 'no types'}`).join('\n');
> --- `packages/mcp-server/src/handlers.ts`

#### MEM-RTE-aggregate-writing
Label: Aggregate composition procedure

Endpoints/progression: documented assistant/operator workflow → anchor/references or annotations → optional excerpts → compose Markdown with source links → direct resource upload → later browse by Aggregate type. Owner: external assistant/operator follows shipped skill; not a wired scheduled service. No supplied route has this referent; it uses [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). Evidence layer: doctrine/design and embedded example code, not an observed run. SRC-1, `docs/builder/skills/semiont-aggregate/SKILL.md`, `docs/builder/skills/semiont-assess/SKILL.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: procedure reports newly uploaded aggregate ID; actual script execution not supplied.
- Later read-back: explicit documented consumer is a person/tool reading a report; browse by Aggregate type lists retained compositions for later reading/comparison.
- Delegated visibility: selected references/source links and optional excerpts become authored report; not every original annotation or derivation reason must be copied.
- Selection predicate: named anchor and referring annotations, alternatively typed resource list and annotations; excerpt example uses 1,500-character context option.
- Invalidation or expiry: procedure asks for dated unique storage URI; rerun creates a new aggregate beside previous one, not automatic invalidation or replacement.
- Activation or effect: afforded retained synthesis of KB content; deployment, actual use and improved decision quality unobserved.
- Evidence limits: this is instructional guidance to a host, not proof of autonomously running aggregation, human approval or complete source coverage.

Admission is ordinary direct upload, separate from authorship. The assistant/operator composes; software accepts by upload protocol, no expected factual oracle established. Trigger is requested report, mode open requests. Guidance explicitly asks for what it was built from and when, with source links; those can retain derivation context. The later reading role is documented but no deployed caller is observed. No automatic withdrawal of earlier aggregates is stated.

> Running the skill again writes a new aggregate beside the last one. Put the date in the `storageUri` so successive runs can be compared.
> --- `docs/builder/skills/semiont-aggregate/SKILL.md`

### Claims

#### MEM-CLM-index-stamp
Label: Embedding compatibility stamp

Claimed operation: stamp documentation says an index made by another model or chunking is recreated; executable code compares configured provider type/model and chunk size/overlap. This is not an immutable model-weights or corpus-consistency guarantee. The documentation's assertion that changing serving location changes no vector is too strong for a mutable endpoint resolving different weights; retain the implemented nominal check and the limitation. Closest supplied record is [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), whose unresolved compatibility question this partly answers; it is not the same referent. SRC-1, `apps/smelter/src/semiont_smelter/index_stamp.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> embedding: dict[str, JsonValue] = {"type": config.embedding.type, "model": config.embedding.model}
> chunking: dict[str, JsonValue] = {"chunkSize": config.chunking.chunk_size, "overlap": config.chunking.overlap}
> --- `apps/smelter/src/semiont_smelter/index_stamp.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-projection-control
Label: Retained maintenance control

Consumer: Weaver startup/catch-up and Smelter startup/reconcile. Channel: retained sequence marks, catalog/event history, index/representation stamps and remembered declines. Force: fixed rules select replay, re-embedding, restamping, purging or skipping repeated declined bytes. Horizon: service restarts until retained state is removed/invalidated; no semantic improvement follows merely from persistence. Distinct from [RT-BAP-worker-config](runtime.md#rt-bap-worker-config): this is accumulated operational state, not only boot configuration. Evidence and minimum passages: [MEM-RTE-graph-maintenance](#mem-rte-graph-maintenance), [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance), [MEM-OBJ-declined](#mem-obj-declined). SRC-1, `apps/weaver/src/semiont_weaver/weaver.py`, `apps/smelter/src/semiont_smelter/reconcile.py`.

## Annotations

#### On [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather)

Memory consumers: request reads current view, source/linked text, graph and annotation vectors. Direct reread confirms window defaults to 1,000 code points per side, with admitted range 100–5,000; MCP explicitly requests 2,000 by default. Similarity operates on selected source text, not annotation assessment prose; up to ten annotations at 0.5, source resource excluded, with unreadable/unnamed resource views omitted. Gather returns target text clipped at twice the window and a generated summary, but Worker `_annotation_sections` does not separately render target-context fields. The returned summary is a request-local derivation, not a persistent knowledge revision. SRC-1, `apps/librarian/src/semiont_librarian/annotation_gather.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`. This qualifies delivery, not the supplied route progression.

#### On [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation)

Retained result: generated bytes, resource-creation event and attribution; annotation-focused upload attempts automatic source binding, while resource-focused generation commits a source-resource link. These effects precede the generated-citation commit and are not withdrawn by its refusal. The constructed nonempty citation batch is not durably retained in this traced Worker path: Dispatcher assigns the job on the source resource, Worker commits citations on the new resource, SDK includes the held job ID, and Archivist requires that assignment in the commit target's own log. It refuses before recording citations. An empty batch makes no commit request and can reach completion; a nonempty refused batch propagates failure after upload and any source linkage. The corrected supplied [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation) retains the mismatch passages; direct rereads of Worker, SDK, Dispatcher and Archivist confirm them. The generation prompt field contains `params.prompt`, not an established complete copy of the assembled prompt, all retrieved inputs or model reasoning. `generationPrompt` is carried into the creation event but not projected into the inspected current resource descriptor by `view::apply`; later normal gather consumes content/descriptor, not an established rationale reconstruction. Event history can retain the field without a model read-back route for it. Source-focused derivation requires both source resource and annotation to form the event's `generatedFrom`; do not generalize annotation-specific lineage to every resource-focused generation. SRC-1, `apps/worker/src/semiont_worker/held_job.py`, `apps/archivist/src/commands.rs`, `apps/archivist/record/src/view.rs`.

> generation_prompt=params.prompt,
> --- `apps/worker/src/semiont_worker/held_job.py`

#### On [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection)

Retained annotation content is distinct from queue recovery metadata. Supplied commit-before-checkpoint passage establishes cursor/completed-unit write and later attempt reuse. Unit completion and cursor mapping are symbolic resume controls, not a derived explanation of why an annotation is correct or an updated detection method. Already committed annotations can outlive cancellation and terminal queue pruning; later browse/gather consumes the annotation, not the pruned queue. Alternative checkpoints (whole completed unit versus partial unit cursor) affect how much is repeated; crash-between-commit/checkpoint behavior is not exactly-once proof. SRC-1, `apps/worker/src/semiont_worker/held_job.py`; supporting passage in the supplied route.

#### On [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt)

Retained material has natural-language influence only after selection: first comment/assessment body when textual, selected source context/hint, derived graph connections/relationship, or resource summary/content, then three best semantic snippets. Current source trust is a prompt request, not a fixed rule proving entailment. OCR payload flags become explicit wording/number uncertainty guidance. These fields can influence a subsequent generation without altering weights or the shipped prompt file. Request-frame isolation keeps other jobs and originating assistant turns out; only generated result/progress crosses back. This resembles a selected-input frame, not host conversation compaction: no verbatim turn tail or reload stub is produced here. SRC-1, `apps/worker/src/semiont_worker/generation/resource_generation.py`; [MEM-OBJ-vector-payload](#mem-obj-vector-payload).

## Write side

Acquisition has multiple admission paths. Direct MCP/CLI/SDK uploads accept caller bytes; the Worker uploads computed output. In the traced generation chain, upload and source binding/linking are separate from new-resource citation admission. A nonempty generated-citation batch is refused for lack of an assignment on the new resource; already admitted bytes/events and any source linkage remain. Empty batches bypass commit and can complete. This is an implemented admission mismatch, not merely an unobserved success or a general partial-failure possibility. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation). `yield:update` registers current bytes and records changed checksum/size; clones create separate identities and may archive the original. None of these establishes immutable content history, a human-reviewed corpus or factual truth. Software checks attribution/schema/checksum separately from the authorship of bytes. [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission), [MEM-RTE-content-revision](#mem-rte-content-revision).

Annotation curation is not only model extraction. Direct marks, body additions/removals/replacements, binding and type changes alter current knowledge. Model mark jobs commit incrementally after processor transformation; comments/assessments can retain reasons in prose. Prose and binding/type fields have different consumers and invalidation. Deleted annotations cease to be current, but their earlier events remain; archive withdrawal suppresses vector retrieval without erasing all history or cached extraction outcomes. [MEM-RTE-annotation-edit](#mem-rte-annotation-edit), [MEM-OBJ-annotation-text](#mem-obj-annotation-text), [MEM-OBJ-annotation-links](#mem-obj-annotation-links).

Automatic transformations are source/event → views/graph, bytes → extracted text → chunks/embeddings/payload, and extraction failure → retained decline → future skip decision. These routes retain derivation identifiers/checksums and some extraction reasons; they are not automatic consolidation of an agent's dialogue into procedural knowledge. Weaver checkpoints and Worker unit/cursor checkpoints are separate recovery forms, with different later consumers. Job lifecycle events are raw operational evidence, not proof of a learned strategy. Compiler diagnostics can guide within-job repair, but the supplied PDF route does not establish a durable repair-method store. [MEM-RTE-record-replay](#mem-rte-record-replay), [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance), [MEM-BAP-projection-control](#mem-bap-projection-control), [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair).

Evaluation has at least two distinct senses. Assessing annotations are retained evaluative content and can later be read into a prompt; they do not automatically reject or downgrade source assertions. Projection reconcile evaluates consistency against record/catalog and can actually remove/rebuild derived entries. The conformance suite describes scripted inference with real surrounding services, not a running production quality gate; this report did not run it. SRC-1, `docs/builder/skills/semiont-assess/SKILL.md`, `tests/conformance/librarian/README.md`; [MEM-RTE-reference-search](#mem-rte-reference-search), [MEM-RTE-graph-maintenance](#mem-rte-graph-maintenance).

## Read-back

The inspected knowledge path is explicit pull followed by code-selected delivery, not independently triggered unsolicited model-context injection. CLI resource gather adds a shipped alternative to annotation gather; SDK clients and MCP expose narrower or broader views, and UI controls show gathered evidence with hint and Generate/Compose choices. An SDK storage method alone would not establish this chain; the MCP gather-to-delegate caller and the Worker prompt builder do. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [MEM-RTE-resource-gather](#mem-rte-resource-gather), [MEM-RTE-mcp-browse](#mem-rte-mcp-browse). SRC-1, `apps/launcher/internal/verbs/gather.go`, `packages/react-ui/src/components/modals/GatherContextStep.tsx`, `packages/react-ui/src/components/modals/ResourceGenerateModal.tsx`.

Generated resources can later be browsed or gathered even when their job fails at the subsequent citation commit. Source bindings/links can be later-readable where successfully recorded; constructed citation annotations from the traced nonempty batch cannot be counted as retained provenance or gather input. Source-ID token handling alone establishes neither citation admission nor entailment. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).

Selectors use several inputs: explicit IDs for source resolution; graph proximity for related resources; selected annotation text for query embeddings; stored resource vectors for resource similarity; name/type/neighborhood/vector union for binding candidates. Those are not interchangeable. Character caps/window and candidate counts are local budgets, not proof of a universal end-to-end token bound. Content left out remains in source/cache for a fresh explicit request; a model-visible source ID is not a live pointer that automatically reloads it. [MEM-RTE-resource-gather](#mem-rte-resource-gather), [MEM-RTE-reference-search](#mem-rte-reference-search), [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather).

Proactive event following is present on the maintenance side: Weaver/Smelter automatically select event-targeted resources to update projections. The shipped session skill also documents a watcher that delegates detection when a resource is created, including warning that a watcher hears its own writes. That is an afforded external script and not evidence of a deployed autonomous memory loop. SRC-1, `docs/builder/skills/semiont-session/SKILL.md`; [MEM-RTE-graph-maintenance](#mem-rte-graph-maintenance), [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance).

## Integration issues

- **No direct correction of supplied runtime findings is required.** New projection and resource-focus inspection fills explicitly deferred areas. The distinct-client comparison for [MEM-CMP-smelter-embedding](#mem-cmp-smelter-embedding) versus [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider), and [MEM-CMP-matcher](#mem-cmp-matcher) versus [RT-CMP-gatherer](runtime.md#rt-cmp-gatherer), prevents collapsing producer/query/ranker models just because configurations can match. No candidate record is intended to replace a supplied referent; annotation headings carry overlapping memory details instead.
- **Generated citations are constructed but refused in the traced Worker path.** The former retained-result finding incorrectly grouped citations with accepted resource bytes and source links. The supplied runtime now independently records the source/new-resource assignment mismatch. This member's Core ideas, generation annotation, Write side and Read-back distinguish those effects; no successful retained generated-citation mechanism is claimed. The ordinary MCP route does not request citations, and empty batches can complete. Source linkage and resource read-back remain supported independently of citation refusal. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding). SRC-1, `apps/worker/src/semiont_worker/held_job.py`, `packages/sdk-python/src/semiont/claims.py`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/archivist/src/commands.rs`.
- **Lineage preservation is narrower than retaining full generation reasons.** `generationPrompt` is optional caller text retained in the event, not the whole assembled prompt. Resource-focus source lineage is not equivalent to the annotation-specific `generatedFrom` pair. This limits any later claim of reconstructible derivation/rationale. [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [MEM-OBJ-event-log](#mem-obj-event-log). SRC-1, `apps/worker/src/semiont_worker/held_job.py`, `apps/archivist/src/commands.rs`, `apps/archivist/record/src/view.rs`.
- **Projection coverage is unequal.** `view::apply` handles cloned/updated/moved/representation events; Smelter follows cloned/updated/representation-added, while the inspected Weaver fold's resource creation case is `yield:created`. Its default passes other types without changing graph. A universal all-event parity claim would be misleading. Whether additional producers/host repair close every affected route remains uninspected; this report asserts only listed fold/repair behavior. [MEM-RTE-content-revision](#mem-rte-content-revision), [MEM-RTE-graph-maintenance](#mem-rte-graph-maintenance), [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance). SRC-1, `apps/archivist/record/src/view.rs`, `apps/weaver/src/semiont_weaver/fold.py`, `apps/smelter/src/semiont_smelter/smelter.py`.
- **Nominal embedding compatibility is implemented; exact provider identity remains open.** Smelter stamp-based recreation qualifies the runtime's deferred index/model compatibility question without proving immutable weights or Librarian/Smelter deployment alignment. Exact deployed models/endpoints are not supplied. [MEM-CLM-index-stamp](#mem-clm-index-stamp), [MEM-CMP-smelter-embedding](#mem-cmp-smelter-embedding), [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider).
- **Withdrawal is not erasure or distributed rollback.** Annotation deletion/archive removes current projections when followed, but log history and checksum-keyed extraction caches differ; previous generated resources/aggregates are not automatically withdrawn. Consistency and content recovery after partial failure remain bounded. [MEM-RTE-annotation-edit](#mem-rte-annotation-edit), [MEM-RTE-vector-maintenance](#mem-rte-vector-maintenance), [MEM-RTE-aggregate-writing](#mem-rte-aggregate-writing).
- **Uninspected included surfaces remain explicit.** The supplied refusal identifies offline launcher import as restoration of content/event-log bytes rather than ordinary command resubmission (SRC-1, `apps/launcher/internal/launcher/importcmd.go`); this correction did not directly inspect it. Live command vocabulary/admission gates must not be generalized to that alternative acquisition path, and an exhaustive admission comparison or restart-parity claim remains prevented. Full Browser/desktop state/admission lifecycle, remaining launcher verb internals, extractor/OCR implementation quality, all graph/vector backends and detailed evaluator assertions are not exhausted. Evidence is available but not inspected, preventing whole-system policy, accuracy and recovery guarantees, not the positive routes established here. Coverage table and corresponding route evidence limits carry these gaps.

## Limitations and checks

The source boundary and source identity were rechecked against the supplied boundary and source checkout HEAD. New inspection stays inside SRC-1 at the frozen revision. Supplied method/type/records inputs were read completely, including the bounded runtime and records-contract continuations. No prior characterization, target execution, provider request or agent delegation was used. No observed operation, model compliance, retrieval accuracy, learned capacity or causal benefit is claimed. Structural validation checks form and quote occurrence, not semantic completeness or job acceptance.

Validation: the invocation-specific `commonplace-run validate-output` command passed: “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.” Its complete result was inspected.
