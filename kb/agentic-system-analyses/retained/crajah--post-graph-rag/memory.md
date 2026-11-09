---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "post-graph-rag memory: persisted passages, derived graph and reports, lifecycle metadata and retrieval-fed demotion."
run-id: AAS-2026-11-08-post-graph-rag-448d75e4222d-01
source-identity: https://github.com/crajah/post-graph-rag
reviewed-boundary: "bce4146a7dc4684e9b66806915c29b0eed57ba23"
---

# post-graph-rag memory report

## Boundary and evidence

This report covers the retained knowledge and working-context surfaces within the supplied whole-system boundary. SRC-1 is the repository at the registered commit, not its dependencies or a live database. Direct reads covered the store's document, entity, relation, community, telemetry, inspection and retrieval methods; engine indexing, community hierarchy, query and maintenance methods; reporting, retention and delta modules; packaging; the LongMemEval conversational caller; ECT-QA replay; and the incremental example. These supply implementation and embedded doctrine, not observed execution. The supplied runtime supplies extraction branches, model mutability and additional shipped-caller findings. No tests, examples, target code or services were executed.

Memory scope follows [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-community-build](runtime.md#rt-rte-community-build) and [RT-RTE-retention-control](runtime.md#rt-rte-retention-control). It includes direct store access, caller-supplied extraction, raw context return, change polling, document drill-down, evaluation retention and cleanup. Static shipped prompts are guidance, not accumulated memory. Caller history is not an engine-managed conversation archive. Provider training, dependency storage internals, live grants and downloaded datasets remain outside the frozen evidence; their behavior cannot be inferred from this source.

| Entry point / operation | SRC-1 source paths and inspection | Covering records / limits |
| --- | --- | --- |
| `index_text`, `index_document`, `index_documents` | Direct: `post_graph_rag/engine.py`, store writers in `post_graph_rag/graph_store.py`; supplied extractor trace | [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), [MEM-OBJ-documents](#mem-obj-documents), [MEM-OBJ-entities](#mem-obj-entities), [MEM-OBJ-relations](#mem-obj-relations), [MEM-OBJ-embeddings](#mem-obj-embeddings) |
| External extraction and injected services | Supplied `post_graph_rag/extractor.py`, `post_graph_rag/engine.py` | [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension); callback provenance/extra storage unresolved, prevents universal admission/trust claims |
| Replacement, deletion, sweep and revival | Direct: `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py` | [MEM-RTE-document-withdrawal](#mem-rte-document-withdrawal), [MEM-OBJ-relation-metadata](#mem-obj-relation-metadata) |
| Supersession and contradiction selection | Direct store and engine; supplied model selector | [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), [MEM-OBJ-relation-metadata](#mem-obj-relation-metadata); no retained model justification established |
| Community build, parent summaries and rebuild | Direct: `post_graph_rag/engine.py`, `post_graph_rag/reporting.py`, store | [RT-RTE-community-build](runtime.md#rt-rte-community-build), [MEM-OBJ-community-text](#mem-obj-community-text), [MEM-OBJ-community-metadata](#mem-obj-community-metadata) |
| Query modes, relation vector/lexical channels, mention expansion, raw-context API, bypass/stream | Direct engine/store; supplied model wrapper | [RT-RTE-question-answer](runtime.md#rt-rte-question-answer), [RT-RTE-direct-answer](runtime.md#rt-rte-direct-answer); no retained answer cache established by these routes |
| Coverage, dark entities, retention, restoration and event purge | Direct: engine/store and `post_graph_rag/retention.py` | [RT-RTE-retention-control](runtime.md#rt-rte-retention-control), [MEM-OBJ-retrieval-events](#mem-obj-retrieval-events); coverage is exposure, not correctness |
| Watermark and delta polling | Direct: `post_graph_rag/deltas.py`, engine, `examples/05_incremental_and_deltas.py` | [MEM-RTE-change-polling](#mem-rte-change-polling); no complete deletion journal or exactly-once proof |
| `document_graph`, document statistics, community tree/children | Direct engine interfaces and store drill-down; detailed statistics SQL not assessed | [MEM-RTE-corpus-inspection](#mem-rte-corpus-inspection); storage-inspection capability, not evidence of a deployed exploration agent |
| Shipped persistent corpus writer/reader and replay | Supplied boundary traces of `evaluation/index_corpus.py`, `evaluation/analyse_graph.py`; direct replay dispatch in `evaluation/ectqa/replay.py`; bounded call-site search of corpus scripts | [MEM-RTE-evaluation-memory](#mem-rte-evaluation-memory); baseline file is replay input, not an answer-memory store |
| Conversational benchmark ingestion, grading and cleanup | Direct: `evaluation/longmemeval/run.py` | [MEM-RTE-evaluation-memory](#mem-rte-evaluation-memory); conversational source is a supplied dataset, not observed own-agent experience |
| Other evaluation consumers | Call-site search: `evaluation/temporal_eval.py`, `evaluation/tempo/run.py`; supplied boundary inventory of ECT-QA, comparisons, judges and build scripts | Underlying index/query routes covered above. Detailed scoring, result bodies, ablation and comparison feedback remain uninspected; prevents benchmark-validity, benefit or automatic improvement conclusions |
| CLI, hooks, registered tools | Direct complete `pyproject.toml`, engine public-method inventory; supplied public exports | Packaging declares no console-script dispatch. Shipped Python example/evaluator drivers and exposed methods are included above. No claim about an external host's hooks/tools |

## Core ideas

1. Passages and derived views coexist. A failed structural extraction can still leave a searchable passage. Entity descriptions and reports compress source meaning; relations retain symbolic provenance and lifecycle controls separately from their prose. Passage-first recovery is bounded by the actual failure and replacement routes, not an atomic corpus invariant: [RT-CLM-passage-priority](runtime.md#rt-clm-passage-priority).
2. Curation is layered, not one truth gate. Model extraction, optional external validation, alias merging, deduplication, confidence maxima, supersession and report generation change different retained parts. Authorship, admission and physical database writes are distinct. None of these mechanisms proves the retained claims true.
3. Retrieval is request-led. The caller asks a question; code and auxiliary model outputs choose stored passages, entity descriptions, relations and reports. Automatic selection supplies context in that request, not an independent unsolicited push. Vectors select material; prose then influences the synthesis model through interpretation: [RT-BAP-answer-context](runtime.md#rt-bap-answer-context).
4. There is one explicit retrieval-trace-to-policy-state chain: selected entity IDs become telemetry, telemetry contributes to archival scoring, and archive flags affect later seed selection and builds. This is retention of use-dependent access state, not model training, a correctness evaluator or demonstrated improved capacity: [RT-RTE-retention-control](runtime.md#rt-rte-retention-control).
5. Withdrawal is not universal forgetting. Raw documents can be deleted, graph assertions can become dormant, superseded assertions remain addressable, and old reports can survive until a rebuild. Later channels have different exclusion rules: [MEM-RTE-document-withdrawal](#mem-rte-document-withdrawal).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-documents
Label: Document passage text

Source-native `documents.payload.text` is natural-language content in PostgreSQL graph vertices, with its vector assessed separately in [MEM-OBJ-embeddings](#mem-obj-embeddings). Lineage: caller document or chunk, including rendered conversational sessions; chunking changes boundaries, not a proven semantic summary. This is source material retained for later requests, not necessarily a raw runtime trace. Consumers: document similarity retrieval and mention expansion, then raw-context caller or synthesis model. Authority at synthesis is evidence-like prose, not a code-enforced fact. Generic API identity leaves human authorship and per-content human approval unresolved. Distinct from the process-local request in [RT-OBJ-query-param](runtime.md#rt-obj-query-param); produced by [RT-RTE-document-admission](runtime.md#rt-rte-document-admission). SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`.

> payload = {"text": text, **meta_dict}
> --- `post_graph_rag/graph_store.py`

Document identity, content hashes, paragraph and source metadata are symbolic access/lineage fields of the same stored vertex, not its prose. They control whole-document replacement, unchanged skipping and references. Deleted passage text has no reconstruction route shown here; re-indexing requires the caller's source again.

#### MEM-OBJ-entities
Label: Entity descriptions

Source-native entity names, types and descriptions are extracted natural-language labels and descriptions stored in `entities` payloads. Default lineage is model extraction; missing endpoints become `Concept` stubs. External extraction can change that provenance. Store merge chooses the longer canonical name and description and avoids replacing specific types with `Concept`; it is not a conflict-explaining synthesis. Consumers: selected entity passages, community reporter, and relation endpoint display. These are derived knowledge, not the original extraction transcript or a retained explanation of the merge decision. Distinct retained product of [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), not another runtime component. SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`.

> merged_desc = prev.get("description") or description or ""
> if description and len(description) > len(merged_desc):
>     merged_desc = description
> --- `post_graph_rag/graph_store.py`

#### MEM-OBJ-entity-metadata
Label: Entity identity and access metadata

Symbolic aliases, vertex identity, mention edges and dormant/archive timestamps reside in database rows/JSON payloads. Alias strings also have a natural-language display role; equality lookup consumes them symbolically to merge vertices. These fields differ from [MEM-OBJ-entities](#mem-obj-entities) by consumer and invalidation: alias resolution controls future writes; mention existence controls dormancy; archive/dormant fields control seed and snapshot admission. Entity vector search always requests null `archived_at`, and conditionally null `dormant_since`. Raw endpoint hydration does not apply those same tests. These are durable products/control state of [RT-RTE-document-admission](runtime.md#rt-rte-document-admission) and [RT-RTE-retention-control](runtime.md#rt-rte-retention-control), not copies of either route. SRC-1, `post_graph_rag/graph_store.py`.

> where = [("archived_at", "is_null", None)]
> if self.config.exclude_dormant_entities:
>     where.append(("dormant_since", "is_null", None))
> --- `post_graph_rag/graph_store.py`

#### MEM-OBJ-relations
Label: Relation assertion text

Source-native predicate and description express the relation between entity endpoints. Natural-language consumption occurs in rendered graph triples, contradiction prompts and community reports; PostgreSQL full-text search separately consumes predicate/description through fixed symbolic lexical rules. This is extracted assertion content, not model reasoning or a retained verdict explanation. Predicate aliases may normalize labels on validated extraction paths. Distinct from the control/provenance part in [MEM-OBJ-relation-metadata](#mem-obj-relation-metadata), and a product rather than a duplicate of [RT-RTE-document-admission](runtime.md#rt-rte-document-admission). SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`.

> "description": description or prev.get("description", ""),
> --- `post_graph_rag/graph_store.py`

Query synthesis renders names/endpoints, predicate, negation, weight and description; optional validity rendering adds dates. The formatted return's friendly triple strings omit some metadata, so that display alone is not the full retained assertion.

#### MEM-OBJ-relation-metadata
Label: Relation provenance and lifecycle fields

Source-native relation endpoint IDs, `sources`, `weight`, `confidence`, `negated`, validity and belief timestamps, supersession pointer and dormancy/revival stamps are symbolic database content. Source chunk IDs record contribution, not independent corroboration. With provenance, weight counts distinct chunks; direct writes without a source increment observation count instead. Merge keeps maximum confidence, combines negation with logical AND, preserves old validity if incoming values are empty, and retains first creation time. Those are admission/update rules, not evidence calibration. Consumers: traversal filters, query filtering/ranking/rendering, withdrawal, contradiction selection, document drill-down and deltas. Distinct part of retained graph state, not a duplicate of [RT-RTE-document-admission](runtime.md#rt-rte-document-admission). SRC-1, `post_graph_rag/graph_store.py`.

> sources = sorted(prior_sources | {source_chunk})
> weight = max(1, len(sources))
> --- `post_graph_rag/graph_store.py`

> "negated": bool(prev.get("negated", False)) and negated,
> "confidence": max(float(prev.get("confidence", 0.0)), float(confidence)),
> --- `post_graph_rag/graph_store.py`

Supersession records replacement ID and expiration time, not a textual reason from the model. Withdrawing provenance removes deleted source IDs; the surviving dormant assertion is an audit residue, not preservation of the deleted passage or an immutable event history.

#### MEM-OBJ-embeddings
Label: Stored embeddings

Source-native document, entity, optional relation and community `embedding` values are dense numerical representations stored in database vector columns. They are separate operative parts from readable text and symbolic metadata: nearest-neighbor consumers use their geometry, not their readable meaning. Lineage is configured embedding service over passage or derived text. Remote training provenance is unresolved; local/hash alternatives and model fixity are already established in [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model) and [RT-CMP-local-embedding](runtime.md#rt-cmp-local-embedding). This object is the retained output, not a duplicate of the producer components. SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`.

> text = report_to_text(report)
> embedding = await self.llm.get_embedding(text)
> --- `post_graph_rag/engine.py`

Dense vectors are distributed numerical encodings, not model-weight updates. New embeddings on merged entity content do not establish that the embedding text equals every surviving longer description; model/geometry consistency is not enforced merely by dimensional checks, as bounded in the supplied runtime.

#### MEM-OBJ-community-text
Label: Community report prose

Source-native report title, summary and findings are generated natural-language memory in `communities` vertices. Lineage: graph snapshot → deterministic/configured clustering → clipped member descriptions/internal relations → reporter; parents consume child reports through a new projection. The renderer takes at most 60 entities and 80 relations, each rendered line capped at 400 characters. Report prose is embedded and later supplied in global/hybrid answer context. Findings retain explanatory prose about subjects, not an extraction/build transcript or a proof of grounding. Distinct product of [RT-RTE-community-build](runtime.md#rt-rte-community-build); report metadata is separately assessed below. SRC-1, `post_graph_rag/reporting.py`, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`.

> pseudo_entities = [{"name": c.title, "type": "Community",
>                    "description": c.summary} for c in children]
> --- `post_graph_rag/reporting.py`

> parts = [report.title, report.summary]
> parts.extend(f"{f.summary}: {f.explanation}" for f in report.findings)
> --- `post_graph_rag/reporting.py`

Parents do not re-read original documents. Lossy projection can compound across levels. Build strips relation validity and supersession metadata before the reporter; the reporter cannot enforce those omitted distinctions from that input.

#### MEM-OBJ-community-metadata
Label: Community ranking and links

Source-native key, level, size, rating, `built_at`, membership and child links are symbolic database material. Model-generated rating has direct ranking authority: code clamps it to 0–10, divides by ten and combines it with similarity and size. Parent rating is overwritten by the maximum child rating. Build time supports warnings, not automatic expiry. Membership/child links support coverage joins and drill-down. Distinct from [MEM-OBJ-community-text](#mem-obj-community-text) by encoding, consumer and authority; produced by [RT-RTE-community-build](runtime.md#rt-rte-community-build). SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`.

> importance = min(max(c["rating"], 0.0), 10.0) / 10.0
> --- `post_graph_rag/engine.py`

#### MEM-OBJ-retrieval-events
Label: Retrieval events

Source-native `retrieval_events` vertices retain timestamp, mode, query SHA-256, selected entity IDs and community IDs. These are symbolic access traces, not full questions, answers, tool transcripts, correctness labels or embeddings. Engine records seed entities and selected communities before synthesis; it does not count every endpoint reached by relation channels. Hashes cannot reconstruct question text. Later consumers aggregate hits/last-hit for coverage and retention scoring; the raw event is not directly delivered as answer evidence. Distinct retained input of [RT-RTE-retention-control](runtime.md#rt-rte-retention-control), not a duplicate of that route. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`.

> "query_sha256": hashlib.sha256(query_text.encode()).hexdigest(),
> "entity_ids": [str(i) for i in entity_ids],
> "community_ids": [str(i) for i in community_ids],
> --- `post_graph_rag/graph_store.py`

### Routes

#### MEM-RTE-document-withdrawal
Label: Document withdrawal and graph revival

Caller deletion, or changed `index_text` replacement → remove chunks and mentions → withdraw provenance → refresh entity dormancy → mark/revive orphan relations. Store code owns progression. This is a distinct lifecycle operation downstream of, and sometimes invoked inside, [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), not an alternative name for ingestion. SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts of deleted chunks/mentions, dormant entities, withdrawn and orphaned relations; sweep returns marked count.
- Later read-back: New query/build invocations apply dormant relation and entity-seed rules; new documented relation assertions can revive withdrawn relations.
- Delegated visibility: inapplicable — database maintenance, not another model or agent invocation.
- Selection predicate: Caller doc_key and space select chunks; remaining mentions decide entity dormancy; no sources or both dormant endpoints can retire relations.
- Invalidation or expiry: Raw chunks are deleted; graph rows remain with dormancy reasons. Orphaned-endpoint revival requires either endpoint live; source-withdrawal revival requires a new source-backed relation assertion.
- Activation or effect: Dormant relations are withheld by default lexical/vector/walk/snapshot consumers; reports already built are not invalidated by deletion itself.
- Evidence limits: No crash-atomic multi-operation transaction or comprehensive forgetting proof; direct include_dormant reads remain possible and entity description content is not reconstructed after source withdrawal.

Admission: a caller chooses deletion/re-index/sweep, but code selects affected rows; no per-row human approval or answer oracle. New mentions and assertions trigger automatic revival. Rejection/recovery: underlying write failures may interrupt maintenance; later re-index/sweep can repair selected state, not restore deleted source text without caller input. The rules are fixed code; no revised method or criticism is retained.

> withdrawn = await self._withdraw_relation_sources(chunk_ids, space=target_space)
> --- `post_graph_rag/graph_store.py`

> if source_chunk and prev.get("dormant_since") is not None:
>     payload.pop("dormant_since", None)
>     payload.pop("dormant_reason", None)
>     payload["revived_at"] = _utc_now()
> --- `post_graph_rag/graph_store.py`

The source-withdrawal update sets `dormant_since`/reason, not `t_expired`; relation-delta consumers filtering expiration time therefore do not receive a complete withdrawal event stream. Supersession and source withdrawal are separate state changes.

#### MEM-RTE-change-polling
Label: Corpus change polling

Caller watermark/changes_since → DeltaReader → timestamp predicates and counts/detail rows → caller. This is distinct from the answer-return route [RT-RTE-question-answer](runtime.md#rt-rte-question-answer): the consumer receives corpus-change metadata and rows, not synthesized answer context. The shipped incremental example prints summary and detail. SRC-1, `post_graph_rag/deltas.py`, `post_graph_rag/engine.py`, `examples/05_incremental_and_deltas.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CorpusDelta with since/as_of, selected counts and optional detail lists, and community-staleness flag.
- Later read-back: Reads retained relation creation/expiration fields, entity transitions and document row clocks from prior operations; external pollers are afforded re-exploration inputs.
- Delegated visibility: inapplicable — no automatic agent dispatch; caller decides what to do with deltas.
- Selection predicate: Caller since, space, include categories, summary flag and limit; engine defaults summary=True and limit=500.
- Invalidation or expiry: inapplicable — result is returned rather than persisted by this route; underlying records change through lifecycle routes.
- Activation or effect: Exposes changed records; does not itself rebuild reports or revise an answer.
- Evidence limits: No upper-bound predicate using as_of, complete deletion journal or durable cursor acknowledgement is shown; limits and mutable timestamps prevent an exactly-once completeness conclusion.

> as_of = await self._db_now()
> delta = CorpusDelta(since=since, as_of=as_of)
> --- `post_graph_rag/deltas.py`

> new_w = [("t_created", ">", since)]
> sup_w = [("t_expired", ">", since)]
> --- `post_graph_rag/deltas.py`

The database clock reduces caller clock skew but does not by itself guarantee a complete poll chain. Missing legacy belief stamps prevent relation inclusion; deletion removes document rows rather than supplying tombstones. The example's exactly-once/idempotence prose exceeds the inspected implementation, including its use of direct `index_document` rather than replacement-aware `index_text`.

#### MEM-RTE-corpus-inspection
Label: Corpus inspection interfaces

Caller → document graph/statistics or community tree/children/coverage interfaces → stored projections → caller display or application. Owner: Python API caller and fixed SQL/projection code. This is distinct from [RT-RTE-question-answer](runtime.md#rt-rte-question-answer); it inspects selected structures without model synthesis. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Capped document subgraph with explicit truncation flags, document statistics or community hierarchy/coverage projections.
- Later read-back: Stored mentions/provenance and community links reach a documented drill-down consumer role; an external exploration agent using them is not established.
- Delegated visibility: inapplicable — no agent call is created by these interfaces.
- Selection predicate: Document key/space and entity/relation caps; hierarchy uses levels and child IDs; coverage sorts hit counts.
- Invalidation or expiry: Underlying graph changes and rebuilds alter subsequent views; no independent display cache is implemented here.
- Activation or effect: Supports inspection, not automatic admission or semantic correction of retained content.
- Evidence limits: Document drill-down cannot enumerate contributions lacking recorded sources; detailed statistics SQL and deployed UI behavior uninspected.

> "entities_truncated": ent_trunc,
> "relations_truncated": rel_trunc,
> --- `post_graph_rag/graph_store.py`

#### MEM-RTE-evaluation-memory
Label: Shipped evaluation memory consumers

Shipped callers map datasets or corpus chunks into normal ingestion and query APIs, then grade/retain outputs. This route groups caller-side orchestration, not another declaration of engine admission or retrieval: [RT-RTE-document-admission](runtime.md#rt-rte-document-admission), [RT-RTE-question-answer](runtime.md#rt-rte-question-answer). Supplied boundary traces establish the persistent named-realm corpus reader; direct inspection adds conversational mapping and replay input. SRC-1, `evaluation/longmemeval/run.py`, `evaluation/ectqa/replay.py`, `evaluation/index_corpus.py`, `evaluation/analyse_graph.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answers, grading records, timing/degraded-run records and output JSON; corpus reader can return structured retrieval.
- Later read-back: Named corpus realms can be queried in later invocations; replay reloads baseline questions/spaces/golds while reading an existing realm; conversational session facts reach later questions within a benchmark instance.
- Delegated visibility: Extraction/synthesis receive source or selected context; judges receive question/reference/answer rather than authority to revise the graph.
- Selection predicate: Caller dataset/realm/configuration, replay baseline records and per-instance sessions; LongMemEval sorts sessions chronologically and queries mix/top_k=32.
- Invalidation or expiry: LongMemEval drops each instance schema in finally; corpus writer has reset/append options; replay does not reconstruct a frozen historical graph merely by loading baseline questions.
- Activation or effect: Session text is transformed to graph state and later answer context; grade records persist to output files but no automatic grade-to-graph or grade-to-instruction update is shown in inspected consumers.
- Evidence limits: No inspected result bodies or execution traces; evaluation correctness, causal gains and completeness of every alternate benchmark scoring path remain uninspected.

Admission: dataset choice and prompt/configuration are caller-controlled; code and extraction gates admit individual records without per-fact human review. The conversational prompt requests user facts and excludes unadopted assistant suggestions. Failure recovery temporarily substitutes the default document prompt; the engine's nonempty result dictionary alone is not a semantic completeness check. Judges use dataset reference answers as an oracle for scoring, not runtime truth admission. There is no automatic proposal-selection loop from those scores in the inspected caller.

> return header + "\n".join(f"{t['role']}: {t['content']}" for t in turns)
> --- `evaluation/longmemeval/run.py`

> DO NOT extract:
> - Assistant suggestions the user did not adopt.
> --- `evaluation/longmemeval/run.py`

> old = base["results"]
> --- `evaluation/ectqa/replay.py`

> await rag.store.client._execute(f'DROP SCHEMA IF EXISTS "{realm}" CASCADE;')
> --- `evaluation/longmemeval/run.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-access-state
Label: Access-state authority

Consumer: entity seed selector, graph snapshot builder and report ranker. Channel: stored archive/dormant flags and report rating. Force: fixed symbolic exclusion/ranking, unlike the interpretive force of prose at [RT-BAP-answer-context](runtime.md#rt-bap-answer-context). Horizon: later queries/builds until state is cleared or reports rebuilt. This path is distinct from the extraction-guidance and answer-context paths in runtime. It is not a guarantee that excluded seeds' facts cannot arrive through documents, existing reports or other relation channels. SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`; see [MEM-OBJ-entity-metadata](#mem-obj-entity-metadata), [MEM-OBJ-community-metadata](#mem-obj-community-metadata).

> if p.get("archived_at"):
>     continue
> --- `post_graph_rag/graph_store.py`

## Annotations

#### On [RT-RTE-document-admission](runtime.md#rt-rte-document-admission)

Retained input/output lineage is split across passage prose, entity prose, relation assertion/provenance and vectors above. Default software/model admission is not human per-content approval. Direct store writes additionally admit caller-supplied graph content without going through GraphExtractor. Read-back is request-triggered in later queries/builds, not unsolicited supply. `index_text` creates a fresh DocumentContext, snapshots known names for each batch, and trims the name list after writes; it does not reload the entire database into extraction context. Adjacent batch mates cannot see each other's extracted names. These are working-context controls, not a persisted summary replacing a conversation. SRC-1, `post_graph_rag/engine.py`; the supplied runtime establishes the first-40-name rendering limit in `post_graph_rag/extractor.py`.

> del context.known_entities[: max(0, len(context.known_entities) - self.config.context_entity_limit)]
> --- `post_graph_rag/engine.py`

#### On [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension)

External callback output can enter the same retained graph without default semantic validation. Initial authorship/trace origin of that output remains unresolved; known downstream merges and lifecycle operations still apply. Starting ingestion is not evidence that a human approves every output. Custom/injected implementations prevent a system-wide claim that all graph content is LLM-authored or all admission has the default confidence/name gates. Evidence and minimum passage are supplied by this runtime record, SRC-1, `post_graph_rag/extractor.py`.

#### On [RT-RTE-community-build](runtime.md#rt-rte-community-build)

Derived report prose and symbolic report rating have different later consumers. Rebuild is caller-triggered, then code/model controlled: cluster size/cap, parsed report and nonempty summary gates admit content without semantic verification. The engine drops validity and supersession fields in member relation projections. Earlier reports are cleared before new reports finish; report failures do not restore the old set. New builds filter dormant relations, but already persisted reports survive later withdrawal until rebuild. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py`, `post_graph_rag/reporting.py`; see the community objects above.

> "predicate": r["predicate"], "description": r["description"],
> "weight": r["weight"], "negated": r["negated"],
> --- `post_graph_rag/engine.py`

#### On [RT-RTE-retention-control](runtime.md#rt-rte-retention-control)

Raw retrieval events → hit/recency aggregates plus degree and age → fixed score → archive timestamps → later entity seeds/snapshots. The input trace is system retrieval exposure, not user acceptance, answer quality or original document provenance. The durable behavior-shaping result is access state. It keeps no per-entity textual rationale or historical score in archive fields; RetentionReport is returned to the caller. Dry-run previews by default; non-dry execution admits selected changes algorithmically. Restore removes archive fields; purge deletes telemetry and changes the evidence for subsequent scoring. SRC-1, `post_graph_rag/retention.py`, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`. No improved future capacity is established by this wiring.

> return (self.W_RECENCY * recency + self.W_FREQ * frequency +
>         self.W_CENTRALITY * centrality + self.W_AGE * age)
> --- `post_graph_rag/retention.py`

#### On [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)

Selector inputs are question vectors, keyword lists, optional subqueries, mode, temporal controls, space and top-k. Selected retained parts travel through multiple channels: document vectors and mentions; entity vectors plus outward walk; relation vectors; lexical predicate/description search; global report search and ranker. RRF combines ranks; quota omits lexical results. The raw-context endpoint returns retrieved parts before text-budget rendering, so it is a distinct delivery contract within the same route. Query is pull-requested selection, not unsolicited memory injection. Automatic keyword/decomposition calls are selectors, not retained knowledge updates. SRC-1, `post_graph_rag/engine.py`, `post_graph_rag/graph_store.py` and supplied runtime evidence.

Synthesis clipping is a best-effort character-based budget, not compaction with a persisted summary: only the selected rendered prefix enters the current answer call, while original stored material remains reachable by a future query. There is no stack of agent task frames here. Batch concurrency creates no autonomous child context or return-only memory boundary. Caller history is appended verbatim without those retrieval budgets, as established by [RT-OBJ-query-param](runtime.md#rt-obj-query-param). Metadata omitted from prose cannot be assumed available to the synthesis model.

> messages.append({"role": "user", "content": prompt})
> --- `post_graph_rag/engine.py`

## Write side

Acquisition is explicit caller ingestion. [RT-RTE-document-admission](runtime.md#rt-rte-document-admission) and [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension) distinguish default model authorship, external proposal shapes, admission gates and database I/O. The document can survive empty or degraded structure; structural errors are counted. [MEM-OBJ-entities](#mem-obj-entities) and [MEM-OBJ-relation-metadata](#mem-obj-relation-metadata) show deterministic merges that preserve some old fields and replace others. Those transformations operate even when upstream provenance is unresolved.

Maintenance comprises caller-triggered document replacement/withdrawal/sweep, configurable supersession, community rebuild and retention. Supersession admits newer order or model-selected candidate IDs, not a reference-validated truth verdict. It retains pointer/time, not criticism text. Withdrawal has its own revival rules and can remove provenance. Community generation keeps subject-matter findings but no build-time criticism record. Retention is the qualifying automatic trace-fed update chain, conditional on caller invocation and non-dry execution; raw events alone would not establish it. Its result changes selectors, not model weights or the extraction method. These mechanisms have no demonstrated benefit in the inspected evidence.

The conversational harness is an alternative input route, not proof of an always-on conversational memory agent. Rendered dataset turns mix user and assistant text; a custom prompt requests user-centered extraction. Later queries consume that derived graph and source excerpts, while final schema cleanup limits persistence to the instance. Evaluation JSON records are retained outside the graph; replay consumes prior question/space/gold records, not prior answers as authoritative facts: [MEM-RTE-evaluation-memory](#mem-rte-evaluation-memory).

## Read-back

Ordinary read-back uses a later caller question. Code selects stored parts, renders text and requests synthesis; the model's compliance is unobserved. Bypass is explicitly outside corpus read-back. Raw-context consumers can bypass synthesis entirely. Context clipping does not delete stored material or learn a compressed substitute. Extraction name-tail control is local to an indexing run and reloads no lost source automatically. These distinctions and budget limits are attached to [RT-RTE-question-answer](runtime.md#rt-rte-question-answer) above.

Reports introduce a second lossy path: corpus → extracted graph → clipped subgraph → report → parent report → selected/clipped synthesis context. Neither original source passages nor lifecycle metadata are automatically reloaded by the report model. Stored report rating has fixed selector force; stored findings have interpretive evidence force. A stale report remains eligible after a warning. Relation filtering alone therefore cannot establish historically faithful full context.

Change polling and corpus inspection are separate consumer surfaces, not proof that an autonomous explorer exists. Polling returns retained transition fields under requested categories; inspection returns bounded projections. Their consumer and completeness limits are in [MEM-RTE-change-polling](#mem-rte-change-polling) and [MEM-RTE-corpus-inspection](#mem-rte-corpus-inspection). Telemetry read-back goes into a maintenance selector, not the answer prompt.

## Integration issues

- No correction to the supplied runtime's bounded admission, temporal or budget findings is required. New lifecycle details qualify broad source-native promises, not those supplied findings. No new record is intended to duplicate a supplied record: retained products and access-state authority are distinct from runtime producer routes/components; new routes cover withdrawal, polling, inspection and shipped caller orchestration.
- Source-native example claims need qualification: `examples/05_incremental_and_deltas.py` labels repeated direct `index_document` calls idempotent, but that API does not perform `index_text` hash/replace checks. Its exactly-once poll claim is not established by a database timestamp. Consequence: do not infer whole-document replacement or lossless deltas from this example. Records: [MEM-RTE-change-polling](#mem-rte-change-polling), [RT-RTE-document-admission](runtime.md#rt-rte-document-admission).
- Withdrawal and historical state remain partial: source IDs are removed, raw passages deleted, entity descriptions are not recomputed from surviving mentions, dormant source-withdrawal does not set relation expiration, and old reports can remain queryable. Consequence: audit residue and current filtering are not complete event sourcing, forgetting or historical-answer reconstruction. Records: [MEM-RTE-document-withdrawal](#mem-rte-document-withdrawal), [MEM-OBJ-relation-metadata](#mem-obj-relation-metadata), [MEM-OBJ-community-text](#mem-obj-community-text).
- Retention's source description suggests general withholding, but archived endpoint facts may arrive through relation/document/report channels. Coverage and dark-entity outputs count selected-ID exposure rather than every supplied fact; `dark_entities` checks dormancy but not archive state. Consequence: neither exposure nor archival means comprehensive relevance, exploration or erasure. Records: [MEM-OBJ-retrieval-events](#mem-obj-retrieval-events), [MEM-BAP-access-state](#mem-bap-access-state), [RT-RTE-retention-control](runtime.md#rt-rte-retention-control). Evidence: SRC-1, `post_graph_rag/graph_store.py`, `post_graph_rag/engine.py`.
- External extraction provenance, provider state/version and dependency payload/transaction semantics remain unresolved. This prevents universal admission/lineage and crash-atomicity conclusions, not descriptions of inspected downstream transformations. Records: [RT-RTE-extractor-extension](runtime.md#rt-rte-extractor-extension), [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-RTE-document-withdrawal](#mem-rte-document-withdrawal).
- Other evaluator internals and tracked outputs remain unassessed as identified in coverage. No result-validity or benefit inference should be integrated from their mere presence. The LongMemEval guard tests truthiness of the engine return, not counts of healthy graph writes; its comments overstate that check's semantic protection. Records: [MEM-RTE-evaluation-memory](#mem-rte-evaluation-memory), [RT-RTE-document-admission](runtime.md#rt-rte-document-admission).

## Limitations and checks

The frozen checkout HEAD was rechecked as bce4146a7dc4684e9b66806915c29b0eed57ba23. Supplied run identity, source identity and reviewed boundary were preserved. Mandatory input reads were completed, including continuation checks after bounded final ranges. Analysis used only SRC-1 and the supplied boundary/runtime; no prior analyses, external services, target execution or experimental results were used. Direct source evidence establishes implementation and requested behavior, not observed activation or causal benefit. Initial provider/embedding provenance, external callback behavior and detailed uninspected evaluator paths remain local limits above. Deterministic validation result: the required role-memory artifact check passed (exit status 0): “Member content check passes; invocation residue not checked. This is not job acceptance or claim support.”
