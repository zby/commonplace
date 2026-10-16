---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "A-MEM memory mechanisms: instance-local notes, derived semantic metadata, split read representations and model-directed neighbor edits."
run-id: AAS-2026-10-16-a-mem-sys-eff95cd80440-01
source-identity: https://github.com/WujiangXu/A-mem-sys
reviewed-boundary: f303dfc71e07bdc787f4bc135d4cea328ae30e99
---

# A-MEM memory report

## Boundary and evidence

This report covers the shipped memory library, embedded prompts, README callers and memory tests at the boundary's frozen commit. It covers admission, metadata derivation, relationship edits, consolidation, all memory-system read helpers, direct CRUD and exposed retriever operations. It does not treat A-MEM as an enclosing task agent. Direct inspection covered complete `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`, `agentic_memory/llm_controller.py`, `tests/test_memory_system.py`, `README.md` and `pyproject.toml` under SRC-1. These provide implementation and doctrine/design evidence, not observed execution. The supplied runtime supplies the initial route decomposition; all memory mechanisms below were checked against source.

Excluded external model services, Chroma internals, model artifacts, images and separate paper reproduction remain as stated in `boundary.md`. There was no source access failure. No target execution was attempted. Actual model choices, synchronization success, provider-side retention, cross-session recovery and task benefit remain unobserved. The constructor starts an empty map and attempts a Chroma client reset, so "persistent memory storage" in the README is not evidence of a shipped restoration route (SRC-1, `README.md`, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`; [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)).

### Coverage inventory

All paths in this table are direct reads in SRC-1. Supplied records are linked, not treated as additional sources.

| Entry point or operative part | Source path | Record coverage and limits |
|---|---|---|
| Constructor, notes and initialization/reset | `agentic_memory/memory_system.py` | [MEM-OBJ-memory-content](#mem-obj-memory-content), [MEM-OBJ-semantic-metadata](#mem-obj-semantic-metadata), [MEM-OBJ-note-links](#mem-obj-note-links), [MEM-OBJ-usage-fields](#mem-obj-usage-fields); no save/load route established |
| `add_note`, `analyze_content`, `process_memory` | `agentic_memory/memory_system.py` | [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), annotations below; no source-quality or human approval gate |
| `consolidate_memories`, automatic threshold and explicit call | `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py` | [MEM-RTE-index-consolidation](#mem-rte-index-consolidation); successful replacement of existing IDs unresolved |
| `read`, `update`, `delete`, mutable objects | `agentic_memory/memory_system.py` | [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation); live reference edits are an alternative unsynchronized write path |
| `search`, `search_agentic`, `find_related_memories`, `find_related_memories_raw`, `_search_raw`, `_search` | `agentic_memory/memory_system.py` | [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval), read-back section; `_search`'s second dictionary iteration prevents assuming a working hybrid route |
| `ChromaRetriever.add_document`, `delete_document`, `search` | `agentic_memory/retrievers.py` | [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot); direct library operations afford storage/query without a demonstrated general external consumer |
| Four inference adapters, empty-response fallbacks | `agentic_memory/llm_controller.py` | [RT-CMP-openai](runtime.md#rt-cmp-openai), [RT-CMP-ollama](runtime.md#rt-cmp-ollama), [RT-CMP-sglang](runtime.md#rt-cmp-sglang), [RT-CMP-open-router](runtime.md#rt-cmp-open-router); provider payload/weight retention opaque |
| Embedding selector | `agentic_memory/retrievers.py` | [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer), [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot); dense vectors are not readable note summaries |
| Usage examples, periodic review guidance | `README.md` | Write-side account; advice is not an automatic maintenance hook |
| CRUD, relationships, evolution and consolidation checks | `tests/test_memory_system.py` | [MEM-ABS-usage-feedback](#mem-abs-usage-feedback), limitations; checks do not feed production admission |
| Dispatch, hooks and registered tools | `pyproject.toml`, both package implementation modules above and `agentic_memory/llm_controller.py` | Library entry points only in inspected packaging/code; no CLI script declaration, hook registry or model-tool registration was found. This bounds shipped dispatch, not arbitrary host integrations |

## Core ideas

1. **Content and its retrieval representation differ.** The caller's text is retained alongside generated or caller-supplied keywords, context and tags. Chroma embeds an enhanced concatenation of those fields, not just the original experience. Derived labels can therefore affect which notes later enter evolution's context. They are not independent corroboration of the original content ([MEM-OBJ-memory-content](#mem-obj-memory-content), [MEM-OBJ-semantic-metadata](#mem-obj-semantic-metadata), [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot)).
2. **Evolution edits metadata, not a recorded rationale.** New-note ingestion selects five neighbors and asks a model for a fixed set of relationship/tag/context edits. The retained results can influence later calls, but a model decision and its reasons are not retained as an evolution trace. The history field's name does not establish automatic history recording ([RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), [MEM-ABS-usage-feedback](#mem-abs-usage-feedback)).
3. **There is no single authoritative read representation.** Some consumers read live objects; others read Chroma snapshots. Neighbor evolution edits only the former immediately. The consolidation name does not establish fresh metadata on every later read ([MEM-RTE-index-consolidation](#mem-rte-index-consolidation), [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)).
4. **Automatic context supply is triggered by a write.** Code, not an autonomous search agent, chooses retained neighbors when a note is added. Ordinary searches are caller requests. The internal automatic route gives retained natural language model-interpreted influence over further edits, whereas outward retrieval returns data without a shipped task-answer consumer ([RT-BAP-neighbor-context](runtime.md#rt-bap-neighbor-context), [RT-BAP-caller-results](runtime.md#rt-bap-caller-results)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-memory-content
Label: MemoryNote content

Source-native identity: `MemoryNote.content`, held on notes in `AgenticMemorySystem.memories`, with a content copy in Chroma metadata. Form: natural-language content when interpreted by the metadata/evolution model or reader; Python stores the supplied string without establishing that it is a raw execution trace. Lineage starts at caller input; whether it is human writing, a transcript, model output or other material is unresolved per note. Constructor and direct update preserve/replace it; automatic evolution does not rewrite it. The full text, rather than an opaque reference or only a display summary, is retained. No source identifier, evidence grade or authorship authentication is added automatically. Consumers: direct reads, search callers, the analysis model and later neighbor prompts. Authority is input data/model context, not executable host instructions. Horizon: initialized instance; caller copies may outlive it but that is not a shipped restoration route. Evidence: SRC-1, `agentic_memory/memory_system.py`.

No counterpart object is declared in the supplied runtime. This object is distinct from the routes that admit and deliver it, notably [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) and [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval).

> # Core content and ID
> self.content = content
> self.id = id or str(uuid.uuid4())
> --- `agentic_memory/memory_system.py`

#### MEM-OBJ-semantic-metadata
Label: MemoryNote semantic metadata

Source-native identity: `keywords`, `context`, `tags` and caller/default `category` on `MemoryNote`. Substrate: live Python fields plus serialized Chroma copies. Context is natural-language summary; keywords/tags/category are strings interpreted semantically by models and embedding generation. Their containers/field names are symbolic; no inspected tag ontology enforces their meanings. Category is not generated by the analysis schema or updated by evolution. Lineage: caller values, defaults, conditional model analysis of content, later neighbor-context/tag replacement, or direct caller edits. The system retains raw content alongside these derived fields; it does not retain an explanation of why a label was chosen. Consumers: enhanced embedding generation, caller display, and evolution's formatted neighbor input (which omits category). Authority: influence on similarity selection and model-interpreted context; not a source trust certification. Evidence: SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`.

No counterpart object is declared in runtime; admission/evolution routes are distinct from this retained field group ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution)).

> self.keywords = keywords or []
> self.links = links or []
> self.context = context or "General"
> self.category = category or "Uncategorized"
> self.tags = tags or []
> --- `agentic_memory/memory_system.py`

#### MEM-OBJ-note-links
Label: MemoryNote links

Source-native identity: `MemoryNote.links`, a live Python list by default, serialized into Chroma metadata. Representational form: symbolic identifiers interpreted by membership lookup and ordered iteration, not a semantic guarantee of a valid relationship. Lineage: caller-supplied links, `strengthen` output appended to the new note, or direct edits; automatic strengthening does not create reciprocal links. Model-suggested connection IDs are extended without a local existence/deduplication check. Later link-expansion consumers do check map membership and skip unresolved targets. Authority: select additional notes for formatted raw output or `search_agentic` candidates; direct hits may exhaust the latter's final budget. Deleted targets can leave dangling links in surviving notes; deletion does not scan/rewrite their lists. Consumers and truncation differ from semantic metadata's embedding path. Evidence: SRC-1, `agentic_memory/memory_system.py`; [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval) are related routes, not counterpart objects.

> suggest_connections = response_json["suggested_connections"]
> new_tags = response_json["tags_to_update"]
> note.links.extend(suggest_connections)
> note.tags = new_tags
> --- `agentic_memory/memory_system.py`

#### MEM-OBJ-usage-fields
Label: MemoryNote usage and history fields

Source-native identity: `timestamp`, `last_accessed`, `retrieval_count`, `evolution_history` on notes. Substrate: Python attributes and serialized Chroma copies. Form: symbolic timestamp/counter fields; `evolution_history` is an unconstrained caller-supplied list whose payload meanings and origin are unresolved. Default timestamps use current minute, retrieval count defaults to zero and history to empty. These are not automatically generated operational traces after initialization. The full source inspection found no read-count increment, access-time refresh or append of evolution decisions ([MEM-ABS-usage-feedback](#mem-abs-usage-feedback)). Caller history values can exist, so this is not a claim that history can never be stored. Consumers: live-object readers can inspect all fields; formatted neighbor text carries timestamp, not retrieval count or history; `search_agentic` exposes timestamp but not history/count/access time. No inspected selector ranks by these fields. Consequently the automatic edit path does not retain or consume its reasons merely because a history slot exists. Evidence: SRC-1, `agentic_memory/memory_system.py`, `tests/test_memory_system.py`. No runtime object counterpart; [RT-RTE-note-admission](runtime.md#rt-rte-note-admission) covers their initial storage, not a distinct audit mechanism.

> self.last_accessed = last_accessed or current_time
> 
> # Usage and evolution data
> self.retrieval_count = retrieval_count or 0
> self.evolution_history = evolution_history or []
> --- `agentic_memory/memory_system.py`

#### MEM-OBJ-chroma-snapshot
Label: Chroma enhanced document and metadata snapshot

Source-native identity: `ChromaRetriever.collection` entries created by `add_document`, using collection name `memories` in the system. Storage substrate: Chroma dependency via `chromadb.Client(Settings(allow_reset=True))`; dependency-level durability and internal storage are uninspected. Material parts: original content plus semantic metadata form an enhanced natural-language embedding input; metadata field containers and JSON serialization are symbolic access representations; emitted/indexed dense vectors are distributed-parametric representations, not readable summaries. The readable `enhanced_content` metadata string is not the vector payload. Vector derivation uses [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer); exact numerical values and provider artifact provenance are uninspected, with no local parameter-training path.

Lineage: live note → enhanced text and serialized metadata → collection add/embedding; search decodes list/dict-looking strings and numeric-looking strings. This heuristic can change the types of text-like metadata (e.g. numeric timestamps); it is not an exact typed-object reconstruction. New neighbor mutations do not immediately update the entry. Consumers: Chroma similarity query, neighbor-text formatting and direct `search_agentic` results. `search` uses collection-selected IDs but live values. Authority: numerical selection plus model-interpreted/caller-returned text; no demonstrated reliability or benefit. Direct retriever insertion/deletion bypasses the note map and model decisions, so it affords storage operations, not a guaranteed coherent alternate full-system admission route. Evidence: SRC-1, `agentic_memory/retrievers.py`, `agentic_memory/memory_system.py`.

No supplied object counterpart. The embedding component and [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval) describe a producer/consumer, not this retained representation.

> # Store enhanced document content for better embedding
> processed_metadata['enhanced_content'] = enhanced_document
> 
> # Use enhanced document content for embedding generation
> self.collection.add(
>     documents=[enhanced_document],
>     metadatas=[processed_metadata],
>     ids=[doc_id]
> )
> --- `agentic_memory/retrievers.py`

### Routes

#### MEM-RTE-index-consolidation
Label: Re-add live notes to retriever

Endpoints/progression: explicit caller `consolidate_memories()` or a threshold multiple of positive add-time evolution decisions → new `ChromaRetriever` wrapper → iteration of all live notes → metadata construction and `add_document`. Owner: Python routine; no model performs summarization, deduplication, conflict resolution or note merging in this route. It proposes no semantic change: it republishes the live representation to storage. Admission is software-controlled on the automatic trigger; an explicit caller may trigger the same bulk write, without establishing human inspection/approval of each note. Answer oracle: inapplicable to this index-maintenance operation. Operating mode: open API maintenance; trigger is the decision counter, not measured task success or read feedback. Caller edits and evolution provide the values; the routine admits them without a separate approval gate. Exceptions can interrupt iteration; no local rollback, checkpoint or rejected-entry queue is maintained. What persists is requested collection entries, not consolidation reasoning. Evidence: SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`.

Part of: [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution)

This route isolates the maintenance continuation already described inside the supplied add/evolution route because its trigger, representation refresh and failure limit differ from semantic evolution. The explicit public call additionally reaches the same routine without a new note. It is not a replacement declaration for the whole evolution route.

- Immediate return: implicit `None` on completion; downstream exceptions can escape.
- Later read-back: requested refreshed snapshots would feed later similarity queries, `search_agentic` direct results and evolution neighbor text; replacement of existing IDs is not established by this source.
- Delegated visibility: all live notes and their metadata are passed to Chroma/embedding dependencies; no LLM call is made by consolidation itself.
- Selection predicate: all `self.memories.values()`; automatic call when positive-evolution count is divisible by `evo_threshold`, or direct caller invocation.
- Invalidation or expiry: no explicit collection reset, deletion or upsert is issued here; successful refresh depends on dependency behavior. New system construction separately attempts client reset.
- Activation or effect: constructs a retriever and calls add for every live note; no observed synchronization or retrieval improvement is established.
- Evidence limits: `get_or_create_collection` plus `collection.add` does not establish replacing prior IDs. No dependency execution or consistency experiment was supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> def consolidate_memories(self):
>     """Consolidate memories: update retriever with new documents"""
>     # Reset ChromaDB collection
>     self.retriever = ChromaRetriever(collection_name="memories",model_name=self.model_name)
> --- `agentic_memory/memory_system.py`

The comment is not the operation: initialization uses get-or-create, and the write is add, as quoted in [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot).

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-usage-feedback
Label: No automatic usage-history feedback in shipped memory paths

- implementation conclusion status: absent

Searched boundary: complete `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`, `agentic_memory/llm_controller.py`, `tests/test_memory_system.py`, plus scoped search for `retrieval_count`, `last_accessed`, `evolution_history`, save/load and consolidation at SRC-1 revision f303dfc71e07bdc787f4bc135d4cea328ae30e99. The memory code initializes/copies these fields but its read/search/evolution methods do not increment retrieval count, refresh access time or append a model decision/reason. Test history values are supplied by the test caller. This absence is bounded to automatic production paths; direct caller writes can populate or replace fields. Supported conclusion: no automatic trace-fed usage/rationale update to these fields, no count/recency-based selector, and no retained automatic criticism history established here. It does not rule out caller-provided experiences or opaque model processing. Evidence: SRC-1, `agentic_memory/memory_system.py`, `tests/test_memory_system.py`; [MEM-OBJ-usage-fields](#mem-obj-usage-fields) supplies the initialization passage. No counterpart absence is declared in runtime; [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution) already notes nonretention of rationale, a consistent narrower finding rather than a duplicate referent.

> evolution_history = ["evolution1", "evolution2"]
> --- `tests/test_memory_system.py`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

Memory lineage: caller content → conditional analysis → only missing/default semantic fields filled → evolution → live object and enhanced Chroma entry. Complete caller metadata bypasses the analysis call but not populated-store evolution. Authorship is unresolved; software applies the returned values without per-content human approval. Direct metadata completion is a transformation, not evidence of learning or trusted factual verification. Model errors may yield empty schema values or the outer `General` fallback, and add can continue with those values. Evidence: SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/llm_controller.py`; supplied route carries the field-assignment passage. Stored representations are separated in [MEM-OBJ-memory-content](#mem-obj-memory-content), [MEM-OBJ-semantic-metadata](#mem-obj-semantic-metadata) and [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot).

#### On [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution)

Automatic read-back trigger: a new note in a populated system. Selector input: new note content; selected retained parts: up to five Chroma neighbors' content, context, keywords, tags, IDs and timestamps. Code formats and delivers those parts in the evolution prompt. Budget: five neighbors, with no local character/token truncation; current note/context/keywords and static guidance remain visible, while unselected notes remain in stores and reachable by later search/ID reads. The current note's tags, links, category and usage/history fields are not interpolated into this prompt. There is no accumulating chat context to compact, no sub-agent frame and no checkpoint summary alternative in these paths. Provider-internal window handling remains opaque. Evidence: SRC-1, `agentic_memory/memory_system.py`; the supplied route and [RT-BAP-neighbor-context](runtime.md#rt-bap-neighbor-context) supply the prompt/dispatch passages.

Curation is fixed-action metadata/relationship editing, not whole-note rewriting. Neighbor contexts/tags change in live objects immediately; selected context snapshots and embedding vectors can lag. Generated labels have update authority through Python dispatch, whereas their later authority is selection/model context. No retained proposal rationale is read by a later automatic route. Input may be a caller-provided trace, but this library does not itself establish its origin or measure a task outcome. This permits experience-derived organization when such content is supplied, without establishing an automatic execution-trace learning loop. Evidence: SRC-1, `agentic_memory/memory_system.py`; [MEM-ABS-usage-feedback](#mem-abs-usage-feedback).

#### On [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation)

Material adoption/edit surface: direct `update` accepts any existing attribute name; direct `read` returns the object itself. The caller can supply edits, but human authorship or approval remains unresolved. Content edits do not automatically regenerate metadata; old metadata can shape a newly embedded changed document. `delete` withdraws the target from the retriever before deleting its map entry and does not clean surviving links or invalidate already returned references. Neither method maintains old-value recovery material. Changing an `id` attribute through update can diverge from its map key and future consolidation ID. Evidence: SRC-1, `agentic_memory/memory_system.py`; supplied record contains the `hasattr` and delete/add passages. No universal semantic quality admission gate can be inferred from the model-mediated add path.

#### On [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)

Read representations and budgets: exact-ID `read` selects a live object. `search` uses Chroma-selected IDs/distances then returns live content/context/keywords/tags. `search_agentic` direct hits carry Chroma metadata, while appended links use live notes; its output omits links/history/count/access time. It discovers links from live objects because its constructed direct-result dictionaries omit the links field. It appends up to `k` unseen neighbors globally then returns only the first `k` total items. `find_related_memories` supplies Chroma metadata text and IDs to evolution; `find_related_memories_raw` formats up to `k` direct hits and up to `k` valid live links per hit, without the same global truncation or deduplication. `_search_raw` returns IDs/distances only; `_search`'s second call returns a dictionary but its loop expects result objects. These helper APIs do not establish additional deployed agent consumers. Evidence: SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`.

> return memories[:k]
> --- `agentic_memory/memory_system.py:620`

The final truncation can exclude every appended neighbor when direct hits fill the budget. The quote's checked source line identifies the `search_agentic` occurrence; other methods use the same text.

## Write side

**Acquisition and admission.** Callers choose what is admitted through `add_note`; no shipped host harvests raw conversation/tool traces. Automatic analysis requests salient keywords, a one-sentence context and categorical tags. Supplied complete metadata can prevent that generation, but code/model evolution can still modify new tags and prior neighbors. These are distinct controls: caller-authored fields, software missing-field admission and model-directed fixed-action edits. The same caller need not be human. Source trust is not established by origin labels, similarity or a model's output. See [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution) and their annotations (SRC-1, `agentic_memory/memory_system.py`).

**Maintenance.** Consolidation re-adds live representations rather than producing an abstract or merged memory. README guidance asks users to review metadata periodically, but no scheduler or approval workflow implements that advice in the inspected code. Direct update/read mutation are operative editing/adoption surfaces. Direct retriever writes provide a lower-level alternative that need not update the map; no hypothetical host using them is promoted to an established consumer route. See [MEM-RTE-index-consolidation](#mem-rte-index-consolidation), [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation), [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot) (SRC-1, `README.md`, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

> - Review LLM-generated metadata periodically for accuracy
> --- `README.md`

**Rejection and withdrawal.** The evolution boolean can withhold automatic edits, and unknown actions are ignored. Malformed outputs are handled by fallback/exception paths, but a false return is not proof of rollback after partial mutation. There is no retained rejected-proposal ledger. CRUD offers caller overwrite/deletion, not automatic evidence-based retraction or cascading removal of links. New construction resets the map and attempts client reset; there is no TTL or save/load checkpoint route in the inspected system. These differences prevent equating retention with durable recovery or deletion with total erasure of previously delivered values ([RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation); SRC-1, `agentic_memory/memory_system.py`).

**Evaluation and traces.** Memory tests check metadata equality, presence and search results, not measured task performance or source truth. Their assertions do not gate production changes or feed retained automatic edits. A test named metadata persistence constructs and queries the same system; it does not restore across sessions. The evolution test's non-None assertions do not establish useful semantic revision. Caller history payloads remain possible, but no raw-to-derived automatic execution-trace transformation is established beyond caller input → generated semantic metadata → later embedding/model context. No compaction-derived summary, checkpoint or retained model reasoning is produced by these modules ([MEM-ABS-usage-feedback](#mem-abs-usage-feedback); SRC-1, `tests/test_memory_system.py`, `agentic_memory/memory_system.py`).

> self.assertIsNotNone(memory.tags)
> self.assertIsNotNone(memory.context)
> self.assertIsNotNone(memory.keywords)
> --- `tests/test_memory_system.py`

## Read-back

The implemented later internal consumer is evolution on a subsequent add. Its source is the Chroma snapshot, not necessarily the newest live neighbor fields. Trigger and selection belong to Python; the model does not formulate a retrieval query or independently request memory. This is automatic delivery within an ingestion request, not unsolicited scheduled maintenance. The model sees retained text in the same prompt as guidance; local schema/action dispatch constrains the output vocabulary, not semantic trust in that text. The source establishes delivery wiring, not actual compliance, activation or benefit ([RT-BAP-neighbor-context](runtime.md#rt-bap-neighbor-context), [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution); SRC-1, `agentic_memory/memory_system.py`).

Outward read-back is caller-requested ID/similarity/link retrieval. The exact representations and budgets are retained in the retrieval annotation rather than collapsed into one "agentic search" claim. README callers print content/metadata; tests inspect returned fields. Neither supplies a shipped task-answer LLM consuming the results. The externally intended agent role therefore remains an integration affordance, while the observed-in-source caller role is Python consumption/display. APIs returning history-capable objects or raw collection results are capabilities; without a defined later consumer they do not establish another behavior-changing route ([RT-BAP-caller-results](runtime.md#rt-bap-caller-results), [MEM-OBJ-usage-fields](#mem-obj-usage-fields), [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot); SRC-1, `README.md`, `tests/test_memory_system.py`).

## Integration issues

- **Corrections to supplied facts:** none required after direct source comparison. This report retains the runtime's qualifications about partial mutations, stale metadata, limited linked delivery, broad direct mutation and unproven consolidation replacement. Source-native README wording that updates automatically evolve is not supported by `update`; this is a documentation/implementation difference, not a correction to the supplied runtime ([RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation); SRC-1, `README.md`, `agentic_memory/memory_system.py`).
- **Record overlap:** [MEM-RTE-index-consolidation](#mem-rte-index-consolidation) isolates a maintenance continuation of [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), with an additional explicit public trigger. The part relation preserves the original route. Objects have no supplied object counterparts. [MEM-ABS-usage-feedback](#mem-abs-usage-feedback) extends the runtime's rationale nonretention finding to inspected usage/history fields, not a duplicate route. No other possible duplicate was found against supplied records.
- **Unresolved refresh behavior:** [MEM-RTE-index-consolidation](#mem-rte-index-consolidation), [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot), [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval). The local code invokes add, not upsert/reset. Dependency behavior is unfrozen/unexecuted, preventing a guarantee that consolidation repairs stale snapshots; the call itself remains wired.
- **Unresolved input provenance and human control:** [MEM-OBJ-memory-content](#mem-obj-memory-content), [MEM-OBJ-usage-fields](#mem-obj-usage-fields), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-RTE-direct-mutation](runtime.md#rt-rte-direct-mutation). Generic Python callers do not establish a human editor or a captured agent trace. This prevents system-wide claims about trace origin or per-content human approval; subsequent transformations remain inspectable.
- **Unresolved provider/storage internals and external use:** [MEM-OBJ-chroma-snapshot](#mem-obj-chroma-snapshot), [RT-BAP-caller-results](runtime.md#rt-bap-caller-results), [RT-CMP-sglang](runtime.md#rt-cmp-sglang). No frozen service/dependency internals or downstream agent execution is supplied. Provider retention, exact model resolution, cross-session reconstruction and task benefit cannot be concluded. These are evidence limits, not missing local source files.

## Limitations and checks

HEAD and clean source status were checked against f303dfc71e07bdc787f4bc135d4cea328ae30e99 before source inspection. No source, registered identity, write scope or method input was changed. The complete supplied invocation, member/peer types, collection, worker rules and records contract were read; ranged inputs were recovered through EOF. Analysis challenged persistence, consolidation, history tracking, linked retrieval and automatic-on-update claims with their alternate paths rather than accepting source labels.

Evidence is implementation/design only. No tests, examples, models, services or dependency runtime were executed. Form validation cannot establish semantic quality or actual activation. Deterministic validation: the supplied `commonplace-run validate-output` command passed with exit status 0: "Member content check passes; invocation residue not checked. This is not job acceptance or claim support."
