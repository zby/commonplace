---
type: types/agentic-system-analysis-result.md
description: "Mem0 Python memory subsystem: additive extraction, retained context and bounded warrant at the pinned revision"
run-id: AAS-2026-09-27-mem0-02
system: Mem0
run-date: "2026-09-27"
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: subsystem-only
reviewed-boundary: "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd"
analysis-cutoff: "2026-09-27"
evidence-tier: code-grounded

memory-comparison:
  scope: Python Memory/AsyncMemory retained facts, raw messages, procedural summaries, access indexes and history; shared
    API paths, default Qdrant adapter and optional LLM reranking inspected; other provider implementations included as unknown
    alternatives. External answering limited to README consumer wiring. Hosted platform, other integrations, model internals
    and deployment excluded.
  axes:
    storage_substrate:
      assessment: partial
      values:
      - vector
      - sqlite
      evidence:
        vector:
          basis: wired
          records:
          - OBJ-2
          - OBJ-3
          note: The default Qdrant adapter persists memory payloads and entity collections.
        sqlite:
          basis: wired
          records:
          - OBJ-4
          - OBJ-5
          note: SQLite retains recent messages and mutation history.
      records:
      - CMP-6
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      note: Non-Qdrant provider implementations remain uninspected; no complete substrate union is asserted.
    representational_form:
      assessment: partial
      values:
      - natural-language
      - symbolic
      evidence:
        natural-language:
          basis: wired
          records:
          - OBJ-2
          - OBJ-4
          - OBJ-6
          note: Text facts, messages and procedural summaries are retained and read.
        symbolic:
          basis: wired
          records:
          - OBJ-3
          - OBJ-5
          note: Vectors, sparse indexes, ID links and history fields have machine-consumed structure.
      records:
      - CMP-6
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-5
      - OBJ-6
      note: Includes access structures; embeddings are numeric data, not learned model weights. Alternative provider payloads
        remain uninspected.
    lineage:
      assessment: partial
      values:
      - trace-extracted
      - authored
      - imported
      - other-compiled
      evidence:
        trace-extracted:
          basis: wired
          records:
          - RTE-3
          - RTE-6
          - RTE-2
          note: Conversation facts and procedural summaries are automatically derived from supplied use traces.
        authored:
          basis: afforded
          records:
          - RTE-5
          note: Caller can author raw memory or replace text through explicit APIs.
        imported:
          basis: wired
          records:
          - OBJ-4
          - RTE-5
          note: Message retention and infer=False accept supplied content without factual extraction.
        other-compiled:
          basis: wired
          records:
          - RTE-7
          note: Embedding, lemmatization and entity-link production derive access structures from retained text.
      records:
      - CMP-6
      - RTE-3
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-2
      note: The API derivations are identified; provider-specific derived structures are not fully inventoried.
    behavioral_authority:
      assessment: partial
      values:
      - knowledge
      - ranking
      evidence:
        knowledge:
          basis: wired
          records:
          - RTE-3
          note: The extractor reads retained text as reference context; the external answering route is only afforded.
        ranking:
          basis: wired
          records:
          - RTE-7
          - RTE-4
          note: Retained indexes and entity-to-memory links change candidate scores.
      records:
      - CMP-6
      - RTE-3
      - RTE-4
      - RTE-6
      - RTE-7
      note: A system-role prompt does not by itself turn factual memory into a binding instruction. Custom prompts and alternative
        providers prevent a complete authority set.
    write_agency:
      assessment: known
      values:
      - automatic
      - manual
      evidence:
        automatic:
          basis: wired
          records:
          - RTE-3
          - RTE-6
          - RTE-7
          - RTE-2
          note: Caller-triggered extraction, summary production and indexing write automatically.
        manual:
          basis: afforded
          records:
          - RTE-5
          note: Explicit raw add/update/delete interfaces permit operator-directed changes.
      records:
      - RTE-3
      - RTE-5
      - RTE-6
      - RTE-7
      - RTE-2
      note: Both API-level agencies are supported; no human editing session was observed.
    curation_operations:
      assessment: partial
      values:
      - dedup
      - evolve
      - invalidate
      - decay
      evidence:
        dedup:
          basis: wired
          records:
          - RTE-7
          note: Entity index maintenance merges an existing exact or near-semantic entity with new linked memory IDs.
        evolve:
          basis: wired
          records:
          - RTE-5
          note: An explicit update replaces an existing memory and rebuilds its access metadata.
        invalidate:
          basis: wired
          records:
          - RTE-5
          note: Deletion removes the current item while recording prior text in history.
        decay:
          basis: wired
          records:
          - OBJ-4
          note: The recent-message store evicts older retained messages beyond ten per scope.
      records:
      - CMP-6
      - RTE-5
      - RTE-7
      - OBJ-4
      note: Dedup is supported by entity-index maintenance, not acquisition hash checks. Provider-internal maintenance is
        uninspected. No automatic fact consolidation or contradiction resolution is established.
    read_back_direction:
      assessment: known
      values:
      - pull
      - push
      evidence:
        pull:
          basis: afforded
          records:
          - RTE-4
          note: The documented chat application explicitly requests memories through search.
        push:
          basis: wired
          records:
          - RTE-3
          note: On add, code automatically supplies selected old memories and scoped recent messages to the extraction LLM.
      records:
      - RTE-3
      - RTE-4
      - RTE-6
      note: Directions are assigned at named consumer boundaries; the search return is not double-counted as push to its requesting
        application.
    read_back_signal:
      assessment: partial
      values:
      - identifier
      - inferred-embedding
      - inferred-lexical
      evidence:
        identifier:
          basis: wired
          records:
          - RTE-3
          - OBJ-4
          note: A composite user/agent/run identity selects the recent message history automatically supplied to extraction.
        inferred-embedding:
          basis: wired
          records:
          - RTE-3
          note: The new message embedding selects up to ten old memories supplied to the extraction LLM.
        inferred-lexical:
          basis: afforded
          records:
          - RTE-4
          note: The documented assistant context route uses hybrid search, whose BM25 scores can alter which memories are
            automatically supplied to the answering model.
      records:
      - CMP-6
      - RTE-3
      - RTE-4
      note: Lexical supply depends on optional BM25 availability. Alternative selectors/providers are not fully inspected.
        Requested identifier lookup alone is not identifier push.
    trace_learning:
      assessment: known
      values:
      - 'yes'
      evidence:
        'yes':
          basis: wired
          records:
          - RTE-3
          - RTE-6
          - RTE-7
          - RTE-2
          note: Automatic trace-fed facts, summaries and derived access structures persist and can affect later extraction
            or selection.
      records:
      - RTE-3
      - RTE-6
      - RTE-7
      - RTE-2
      note: Wired durable influence is established; observed improvement is not required and is not claimed.
    trace_source:
      assessment: partial
      values:
      - session-logs
      - trajectories
      - tool-traces
      evidence:
        session-logs:
          basis: wired
          records:
          - RTE-3
          - RTE-2
          note: The ordinary path derives memory from supplied user/assistant messages, including optional image descriptions.
        trajectories:
          basis: afforded
          records:
          - RTE-6
          note: The procedural producer accepts execution histories and is prompted to retain sequential actions and results.
        tool-traces:
          basis: afforded
          records:
          - RTE-6
          note: The procedural prompt explicitly accepts tool/API results as execution-history content; normal factual parsing
            omits tool-role messages.
      records:
      - RTE-3
      - RTE-6
      - RTE-7
      - RTE-2
      note: All identified learning routes inherit these trace sources. Custom prompts and unconstrained caller content leave
        the complete source union open.
    learning_scope:
      assessment: partial
      values:
      - cross-task
      - per-task
      evidence:
        cross-task:
          basis: afforded
          records:
          - RTE-3
          - RTE-4
          note: The user-scoped example reuses accumulated preferences across later requests without requiring a task ID.
        per-task:
          basis: claimed
          records:
          - RTE-6
          note: The default procedural prompt names continuation of the same unfinished task.
      records:
      - RTE-3
      - RTE-4
      - RTE-6
      - RTE-7
      - RTE-2
      note: 'Route-specific horizons: factual/image/index paths inherit caller identity and the cross-request example; procedural
        continuation is prompt intent. Arbitrary run_id values or custom prompts do not establish task/project horizons.'
    learning_timing:
      assessment: known
      values:
      - online
      evidence:
        online:
          basis: wired
          records:
          - RTE-3
          - RTE-6
          - RTE-7
          - RTE-2
          note: The API produces and persists derivatives during add, before returning; async methods await their writes.
      records:
      - RTE-3
      - RTE-6
      - RTE-7
      - RTE-2
      note: Online denotes immediate API processing, not proof that every caller invokes it during a live task. External batch
        schedules are outside this boundary.
    distilled_form:
      assessment: known
      values:
      - natural-language
      - symbolic
      evidence:
        natural-language:
          basis: wired
          records:
          - RTE-3
          - RTE-6
          - RTE-2
          note: Fact extraction, procedural summaries and image descriptions produce text.
        symbolic:
          basis: wired
          records:
          - RTE-7
          note: Trace-derived text produces retained vectors, lexical indexes and entity-ID associations used in ranking.
      records:
      - RTE-3
      - RTE-6
      - RTE-7
      - RTE-2
      note: Covers the identified qualifying learning routes. No trained parameter update is established; opaque remote model
        internals are outside scope.
    faithfulness_tested:
      assessment: not-determinable
      values: []
      evidence: {}
      records:
      - CLM-2
      note: No retained execution evidence testing dependence on recalled content was inspected. README managed-platform scores
        are neither OSS execution evidence nor a recall-dependence test.
---

# Mem0 Python memory subsystem analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/mem0.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-02/memory-report.md`

**Memory analysis report SHA-256:** `0ce564fddd6e8d5131cfc5d081ff01136d097d0439ceb8ea8ed5e660823d8ff2`

## Boundary and evidence

Evidence basis: static inspection of Python implementation and separately identified repository doctrine at commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`, inspected 2026-09-27. No system invocation or behavioral experiment was performed.

This analysis describes the open-source Python Memory and AsyncMemory subsystem for interpreting its runtime responsibilities, memory comparisons and epistemic claims. It includes ordinary inferred writes, raw and procedural writes, retained history, entity access structures, public retrieval, maintenance, configured model/provider dispatch and the README consumer example. The enclosing assistant runtime is outside the boundary: it supplies messages, identity values and credentials, selects calls, consumes returned memories and owns task effects. Hosted-platform internals, server authentication, CLI/plugin surfaces, TypeScript and other integrations are excluded; conclusions about their equivalence, deployment security and quality do not follow. External model and storage internals are inaccessible. Provider alternatives are inventoried at dispatch boundaries; selected default implementations and reranking alternatives are inspected, without a claim to exhaustive provider equivalence.

The source allowlist is only the repository at this commit. Origin and revision were verified before source inspection. All evidence reads used commit-addressed Git blobs; worktree state was not evidence. Primary-source links are limited to this frozen repository. No prior analysis was consulted.

## Source register

| Source ID | Kind | Identity/location | Revision | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | Implementation | Selected Python API, config, extraction, storage, scoring, factories, provider and utility paths named on records | Full paths on each record; pinned quote attributions | No deployed instances, provider internals or execution traces; prevents observed behavior, causal benefit and deployment guarantees |
| SRC-2 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | Doctrine/design; reported benchmark claims distinguished on CLM-2 | README introduction, April algorithm account, basic-use example; active prompt instructions | `README.md:45-80,196-235`, `mem0/configs/prompts.py:326-367,468-550,620-654,905-944,970-1062` | External benchmark framework and hosted optimizations excluded; no reproduced benchmark or quality attribution |

Operational access root: `/home/zby/llm/commonplace/related-systems/mem0ai--mem0`.

## Shared records

### Components

### CMP-1 — Memory and AsyncMemory orchestration

Conclusion status: wired. Symbolic Python objects own ordered memory operations, not an autonomous task loop. They instantiate LLM, embedder, vector store and SQLite history; AsyncMemory offloads synchronous calls through `asyncio.to_thread`. Source: SRC-1 `mem0/memory/main.py:487-512,2193-2220,2635-2661`.

> self.llm = LlmFactory.create(self.config.llm.provider, self.config.llm.config)
> self.db = SQLiteManager(self.config.history_db_path)
> self.collection_name = self.config.vector_store.config.collection_name
> --- `mem0/memory/main.py:488-505` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-2 — Configured extraction LLM

Invocation conclusion status: wired. Distributed-parametric service accessed through a symbolic adapter. The inspected OpenAI adapter defaults to the model name `gpt-5-mini`, accepts alternate base URLs and OpenRouter routing, and issues chat completions. Exact-version pinning conclusion status: uninspected; a model name and mutable endpoint do not identify weights. Parameter-change conclusion status: uninspected for provider internals; inspected adapter behavior is inference, not an evidenced training operation. Source: SRC-1 `mem0/llms/openai.py:15-54,106-148`, `mem0/utils/factory.py:35-139`. No parameter-learning conclusion follows.

> if not self.config.model:
>     self.config.model = "gpt-5-mini"
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> response = self.client.chat.completions.create(**params)
> parsed_response = self._parse_response(response, tools)
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-3 — Embedding model

Invocation conclusion status: wired. Distributed-parametric embedding service supplies memory, query and entity vectors. The OpenAI adapter resolves a configurable model name, defaulting to `text-embedding-3-small`; its vectors are derived access data, not changed model weights. Exact-weight identity and provider parameter changes: uninspected. Source: SRC-1 `mem0/embeddings/openai.py:11-80`.

> self.config.model = self.config.model or "text-embedding-3-small"
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> return self.client.embeddings.create(**kwargs).data[0].embedding
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-4 — Optional spaCy language pipeline

Invocation conclusion status: wired, conditional on availability. Distributed-parametric NER/tagging and symbolic filters support entity extraction and lemmatization. The loader can download `en_core_web_sm` if missing, loads by package name, and falls back to no model on failure. Exact-version identity: uninspected; no immutable weight pin is supplied at this call. Parameter changes within the inspected load/inference route: uninspected as a broad model claim; no training is established by these operations. Source: SRC-1 `mem0/utils/spacy_models.py:20-91`, `mem0/utils/entity_extraction.py:751-772`.

> _nlp_full = spacy.load("en_core_web_sm")
> logger.info("spaCy full model loaded")
> --- `mem0/utils/spacy_models.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-5 — Optional relevance reranker

Invocation conclusion status: wired when a reranker is configured and requested. Inspected alternatives include an LLM relevance scorer and a SentenceTransformer CrossEncoder. They produce relevance rankings, not truth judgments. Exact-weight pinning and operational parameter changes: uninspected; the inspected alternatives call prediction/completion APIs using configuration names. Other registered reranker implementations remain uninspected. Source: SRC-1 `mem0/memory/main.py:1498-1506`, `mem0/reranker/llm_reranker.py:40-98,121-150`, `mem0/reranker/sentence_transformer_reranker.py:46-89`.

> self.model = CrossEncoder(self.config.model, device=self.config.device)
> --- `mem0/reranker/sentence_transformer_reranker.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> "You are a relevance scoring assistant. "
> "Given a query and a document, score how relevant the document is to the query.\n\n"
> --- `mem0/reranker/llm_reranker.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-6 — Configurable storage and model boundary

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/configs/base.py:28-62`, `mem0/vector_stores/configs.py:6-65`, `mem0/configs/vector_stores/qdrant.py:7-25`, `mem0/memory/main.py:487-580`.

The default vector provider is Qdrant; history defaults to a SQLite database under the Mem0 directory. The Qdrant configuration defaults to `/tmp/qdrant`, with local path or remote/client alternatives. `on_disk=False` describes vector placement, not proof that the whole memory is ephemeral. No durability claim stronger than the inspected calls to storage is made.

> provider: str = Field(
>         description="Provider of the vector store (e.g., 'qdrant', 'chroma', 'upstash_vector')",
>         default="qdrant",
>     )
> --- `mem0/vector_stores/configs.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Evidence for SQLite initialization is retained on CMP-1.

The registered alternatives include SQL-backed, key/value, graph-branded, local and remote vector adapters. Their names alone do not establish their operative memory substrates or guarantees. Those implementations, model-provider adapters and non-LLM rerankers were not inspected. The supplied configuration has no graph-memory module; entity links inspected here are payload associations in a vector collection, not proof of a graph database. This is an implementation-scope limit, not absence across other product editions.

### Operative objects

### OBJ-1 — Shipped extraction guidance and caller instructions

Conclusion status: wired. Natural-language guidance in Python prompt constants, plus caller-supplied `prompt` or configured `custom_instructions`, shapes extraction and procedural summarization. This is shipped/caller guidance, not itself memory read-back. The additive prompt asks for self-contained factual statements from both conversational roles, semantic nonduplication and contextual precision. Procedural guidance instead prescribes a continuation summary with outputs preserved. Source: SRC-1 `mem0/memory/main.py:935-960,2007-2049`; SRC-2 `mem0/configs/prompts.py:326-367,468-550,905-944`.

> custom_instr = prompt or self.custom_instructions
> --- `mem0/memory/main.py:935-958` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> Use these ONLY for deduplication and linking — do NOT extract new memories from Existing Memories. Your extractions must come exclusively from New Messages. If new information in New Messages is semantically equivalent to an Existing Memory with no meaningful new context, skip it.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The guidance is addressable by sections and configuration fields. Theory-builder conditions 1–4 for the extraction policy are separately assessed: localized policy content, wired; consumption, wired; content-directed criticism of that policy, uninspected; kept criticism shaping a later policy round, uninspected. The checklist requests completeness checking of outputs but does not expose a formulated criticism record or demonstrate revision of the extraction policy. Its model-internal performance cannot be inferred from the prompt. Static policy retention across calls is not retained criticism. Learning: uninspected; no attributed capacity comparison is available. Reflective and autonomous theory-builder qualifications are uninspected because these missing links prevent membership establishment. This does not decide the weaker architectural reflection finding on the retained-memory context path.

### OBJ-2 — Memory text and metadata payload

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:1005-1052,1222-1268,1975-2005`. Ordinary facts are LLM-derived natural language. Raw additions import caller text, and explicit updates permit authored replacements. UUID, hash, timestamps, identity fields, expiration and optional attribution accompany the text. `data` is operative content; a returned `memory` field displays that same text, not a separate opaque learned payload. Embeddings are distinct access structures in the object OBJ-3.

> mem_metadata["data"] = text
>             mem_metadata["text_lemmatized"] = text_lemmatized
>             mem_metadata["hash"] = mem_hash
> --- [mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L1032-L1034)

Consumers are the extraction LLM through the route RTE-3 and the documented chat caller/model through the route RTE-4. Authority is contextual knowledge; no blanket instruction/enforcement authority follows from storage or prompt role. Rationale may occur inside text but is not a separate mandatory retained field.

### OBJ-3 — Dense/lexical indexes and entity associations

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/vector_stores/qdrant.py:93-165,186-245,415-485`, `mem0/memory/main.py:1100-1204,1642-1828`. Dense vectors and optional BM25 sparse vectors accompany memory records. Entity payloads contain entity text/type and `linked_memory_ids`, in a separate collection using the configured vector provider. They are compiled access metadata with symbolic structure; entity names remain readable text. Numeric embeddings are not updated model weights.

> named_vectors = {"": vector}
>             if self._has_bm25_slot and bm25_sparse_vectors[idx] is not None:
>                 named_vectors["bm25"] = bm25_sparse_vectors[idx]
> --- `mem0/vector_stores/qdrant.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> "linked_memory_ids": sorted(memory_ids),
> --- [mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L1189-L1189)

The later ranking consumer uses these links to boost matching memories. It does not send the link structure itself to the README answering model. BM25 may be disabled by missing dependencies or an older collection; entity extraction returns no candidates without its NLP model. These are conditional wired paths, not deployment observations.

### OBJ-4 — Recent-message ring in SQLite

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/storage.py:128-146,257-324`, `mem0/memory/main.py:407-420,918-956`, `mem0/configs/prompts.py:970-996,1016-1048`. Raw role/content/name/time rows are stored under a deterministic composite identity made from supplied user, agent and run IDs. This is a ten-message contextual window, not the full conversation archive. It contains natural-language content and symbolic scope/role metadata.

> SELECT id FROM messages WHERE session_scope = ? ORDER BY created_at DESC LIMIT 10
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> last_messages = self.db.get_last_messages(session_scope, limit=10)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The ring is automatically supplied to later extraction, with each displayed message truncated to 300 characters. Eviction is a concrete decay operation over retained content. Equal insertion timestamps provide no inspected deterministic secondary ordering. The scope key alone does not establish a task horizon.

### OBJ-5 — Mutation history in SQLite

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/storage.py:102-124`, `mem0/memory/main.py:1960-1973,2094-2138`. History retains old/new text, event, timestamps, deletion flag and optional actor/role. A caller can request it through `history(memory_id)`; the ordinary extraction/read-back pipeline does not load it. It is mutation evidence, not a record of why a fact was believed or changed.

> old_memory   TEXT,
>                         new_memory   TEXT,
>                         event        TEXT,
> --- [mem0/memory/storage.py](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/storage.py#L111-L113)

History failure can be logged after vector persistence in ordinary batch acquisition, so cross-store atomic audit completeness is not guaranteed.

### OBJ-6 — Procedural continuation summary

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:855-865,2007-2050,3708-3769`; SRC-2 `mem0/configs/prompts.py:326-359`. A generated natural-language summary is embedded and stored using the ordinary memory object format with `memory_type=procedural_memory`. It is not an executable procedure. The default prompt asks for the task objective, progress, ordered actions, exact outputs, errors, attempted recovery and current context. The stored object contains whatever the LLM actually returned; exact reproduction is not checked.

> metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Reasons and criticisms may survive as narrative findings/errors. No later dedicated reason evaluator is wired. The summary can be selected as ordinary retained text by later extraction/search; that is the implemented later consumer path. Agent continuation is an afforded/intended application, not an observed resume.

### OBJ-7 — Transient image description

Conclusion status: wired. Natural-language content returned by CMP-2 on RTE-2 becomes the current message text and may then enter OBJ-4 and the extracted-memory pipeline. It is not a separately retained original image or independent memory store. Candidate truth-apt content describes what the image depicts; preservation versus ampliation is indeterminate without image/output instances. Evidence and supporting quote: RTE-2, SRC-1 `mem0/memory/utils.py:161-231`.

### Routes

### RTE-1 — Caller configuration and provider admission

Conclusion status: wired. Trigger: caller creates or configures a Memory instance or registers an LLM provider. Caller proposes provider identity, endpoint, model and instructions; factory and configuration validation decide admissibility, then Python imports and instantiates the class. The guidance is caller configuration plus static dispatch rules, symbolic and natural-language, not an evidenced criticism-derived theory revision. Source: SRC-1 `mem0/utils/factory.py:30-34,68-139`, `mem0/memory/main.py:487-512`. The route changes the capabilities used by later calls. Rejection: unsupported names raise ValueError; runtime imports/configuration can fail. Recovery: caller supplies a valid configuration; rollback of arbitrary provider effects is uninspected. This is in-process extension authority, with the host owning credentials and isolation; no library-level sandbox guarantee is established.

Immediate return: instantiated component. Later read-back: configuration guides subsequent calls, but is not use-derived memory. Delegated visibility: inapplicable; provider invocation is an external service call, not an inspected subagent handoff. Selector: provider name/class registry. Expiry: inapplicable for static configuration. Effect: class construction and later calls; deployed effects uninspected. Required external contract: provider implementations respect their interfaces and storage success semantics. Guarantee strength: protocol at factory dispatch only.

> if provider_name not in cls.provider_to_class:
>     raise ValueError(f"Unsupported Llm provider: {provider_name}")
> --- `mem0/utils/factory.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> cls.provider_to_class[name] = (class_path, config_class)
> --- `mem0/utils/factory.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### RTE-2 — Optional image description preprocessing

Conclusion status: wired. Trigger: add receives image or multipart content and vision is enabled. Caller selects the mode; Python invokes CMP-2 to describe the image before the normal write route. The description is model-produced truth-apt input, with semantic preservation versus conjecture indeterminate. Without vision, multipart text is kept and image-only parts skipped. Source: SRC-1 `mem0/memory/utils.py:161-231`, `mem0/memory/main.py:865-870`. The model proposes the description; code admits it as message content. External image truth and model interpretation remain uninspected. No separate answer oracle or rejection based on image-description accuracy is established. Guidance asks for a high-level description; no rationale or criticism record is required. Recovery: image-description exceptions propagate. Immediate return: transformed messages to add; persistence and later read-back depend on the subsequent write. Selection is input type and configuration; delegated visibility inapplicable; no independent expiry. Guarantee strength: best effort semantic transformation, with only control-flow wiring established.

> description = get_image_description(msg, llm, vision_details)
> returned_messages.append({"role": role, "content": description})
> --- `mem0/memory/utils.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Specialist integration on RTE-2: image descriptions feed both the ordinary factual producer and recent-message retention, so they belong in the same trace-fed transformation chain. Timing and task horizon follow the caller-scoped factual route. No new storage form, visual-fidelity test or retained original image is established. Both passes independently identified this preprocessing boundary.

### RTE-3 — Additive extraction with automatic memory context

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:881-1219,2556-2901`; SRC-2 `mem0/configs/prompts.py:468-570,917-958,970-1062`. Trigger: caller invokes `add` with inference enabled (default). Producer: selected LLM, receiving new parsed messages, up to ten prior messages for the identity, and ten embedding-selected old memories. Output: added textual entries, embeddings, attribution if emitted, metadata, history, then entity associations and the recent-message ring. The immediate return is an ADD-result list (ID/text/event); the later consumer is a distinct subsequent extraction or search, not the return itself.

> existing_results = self.vector_store.search(
>             query=parsed_messages,
>             vectors=query_embedding,
>             top_k=10,
>             filters=search_filters,
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> user_prompt = generate_additive_extraction_prompt(
>             existing_memories=existing_memories,
>             new_messages=parsed_messages,
>             last_k_messages=last_messages,
>             custom_instructions=custom_instr,
>         )
> --- [mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L950-L955)

The extractor did not request these old entries: code selects and supplies them on `add`. This is wired push using identity for history and inferred embedding for old facts. The new fact can influence a later extraction's deduplication/reference resolution; the stored trace derivative therefore qualifies for trace learning independently of unobserved answering quality. Production is online within the API call. Identity can persist across requests; task/project semantics depend on the caller. The README supplies a cross-request application, while no arbitrary `run_id` is presumed to mean one task.

The LLM is asked to avoid semantic duplicates, but programmatic fact rejection uses equal text hashes from just the retrieved ten and the current batch. That acquisition check is not evidence of retained-fact consolidation. Missing text/embedding skips an output. LLM call errors propagate; malformed extraction responses can become empty extraction. Batch insert falls back to individual inserts; only confirmed successes are reported, and total failure raises. No active default automatic UPDATE/DELETE dispatcher appears in this path. Remaining old update prompts and stale `add` docstring wording do not establish one.

Trust boundary evidence: SRC-1 `mem0/memory/utils.py:61-76`. The normal parser includes system-role content in the serialized extraction input, even though the extraction instruction targets user and assistant facts. The sample answering route supplies recalled text inside a system message and later hands that conversation to `add`. This is an implementation path for recirculation; no observed erroneous extraction or protection guarantee follows.

> if role == "system":
>             response += f"system: {content}\n"
> --- `mem0/memory/utils.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The parse-failure and storage-success distinctions are implemented explicitly:

> except Exception as e:
>     logger.error(f"Error parsing extraction response: {e}")
>     extracted_memories = []
> --- `mem0/memory/main.py:970-989` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> if not persisted_records:
>     self.db.save_messages(messages, session_scope)
>     raise VectorStoreError(
>         f"Failed to insert any of the {len(records)} extracted memories into the vector store"
>     )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The extraction prompt requests memory-to-memory `linked_memory_ids`, but the inspected persistence loop copies text and optional attribution, not that generated field; the UUID-to-integer mapping is not used to persist those proposed links. The actual retained links are entity-to-memory associations produced separately by the route RTE-7.

### RTE-4 — Requested search and documented assistant delivery

Implementation conclusion status: wired. External consumer conclusion status: afforded. Evidence: SRC-1 `mem0/memory/main.py:1393-1536,1642-1828,3329-3420`, `mem0/utils/scoring.py:60-139`, `mem0/reranker/llm_reranker.py:112-173`; SRC-2 `README.md:209-222`.

The named requesting consumer is the README's `chat_with_memories` application. It calls `search`, using a user ID and current message. That request/return is pull. The application then automatically formats selected memory text into context for its answering LLM; this downstream consumer boundary is afforded push, conditional on the example being adopted. It is not an observation that the assistant relied on the memories.

> relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Selection requires at least one user/agent/run identity. The shared algorithm forms candidates from semantic results, filters expiration, gates the semantic score, and adds normalized BM25 and entity boosts before taking top-k. Keyword-only or entity-only hits outside the semantic candidate pool do not become candidates in this implementation. This narrows the README's broad multi-signal description.

> semantic_score = result.get("score") or 0.0
>         if semantic_score < threshold:
>             continue
> --- `mem0/utils/scoring.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> raw_combined = semantic_score + bm25_score + entity_boost
> --- `mem0/utils/scoring.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> if not show_expired and _payload_is_expired(payload):
>     continue
> --- `mem0/memory/main.py:1680-1687` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The optional reranker runs only with both configuration and `rerank=True`, after the initial top-k. The inspected LLM variant supplies query/document text (each truncated to 4,000 characters), parses a numerical relevance score, then sorts. Its judgment changes requested ranking; it does not alone establish inferred-judgment push to a demonstrated downstream assistant. `explain=True` exposes arithmetic score details, not a factual justification. No total assistant context token cap or successful recall-dependence test was inspected.

### RTE-5 — Raw authoring, editing and withdrawal

Implementation conclusion status: wired. Operator adoption conclusion status: afforded. Evidence: SRC-1 `mem0/memory/main.py:881-916,1222-1268,1340-1392,1829-1960,2052-2180,3507-3560,3770-3863`.

With `infer=False`, non-system message contents are embedded and stored directly with role/name metadata. This permits manual/imported memory; it is not itself automatic distillation. `update` changes text and metadata, preserves identity fields and records old/new content; changed text removes old entity links and builds new ones. `delete` removes a vector record, retains its text as deletion history, and removes its entity associations. These are explicit maintenance APIs, not decisions made by the default extraction LLM.

> self.vector_store.delete(vector_id=memory_id)
>         self.db.add_history(
>             memory_id,
>             prev_value,
>             None,
>             "DELETE",
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Thus update is evolve and delete is invalidate under the comparison vocabulary. Full reset clears history and recent messages as well as resetting stores. Scoped `delete_all` does not clear the raw message ring. Expiration hides items from default search/listing while direct `get` and the extraction's direct vector search lack the same expiry gate. Withdrawal is route-specific: a deleted fact's recent raw source can still enter the next extraction, and an expired fact can remain extractor context. Reintroduction is possible from these code paths, not demonstrated by execution. Automatic policy-based forgetting advertised as project `decay` is rejected in the OSS API; the actual bounded raw-message eviction is separately established.

### RTE-6 — Execution-history summary production and later reuse

Implementation conclusion status: wired. Continuation use conclusion status: afforded. Evidence: SRC-1 `mem0/memory/main.py:831-865,2007-2050,2507-2540,3708-3769`; SRC-2 `mem0/configs/prompts.py:326-359`.

Trigger: `add` with an agent ID and procedural memory type. Producer: selected LLM consumes the supplied messages and default/custom summary instruction. Storage is the object OBJ-6, immediately embedded and persisted; the immediate return contains its ID, summary text and ADD event. Empty output raises; no exact-output fidelity checker is present. Later ordinary vector search or additive extraction can select the stored summary. This is an automatic trace-fed write with an implemented later consumer, even though automatic task resumption is not established by these methods. The default same-task continuation horizon is explicit in its prompt; custom prompts leave the actual horizon undetermined.

> Your task is to produce a comprehensive summary of the agent's output history that contains every detail necessary for the agent to continue the task without ambiguity.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> - **Errors & Challenges**: Document any error messages, exceptions, or challenges encountered along with any attempted recovery or troubleshooting.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The source calls this procedural memory, but the operative result is descriptive execution context, not a validated reusable procedure. Trajectories and tool/API results are explicitly intended inputs; their use is afforded rather than observed. Errors/recovery are requested, so do not report wholesale absence of criticism retention. Neither retention fidelity nor later use of those reasons is verified. Async production awaits the same persistence; it is not a separate offline learning stage.

### RTE-7 — Automatic indexing and entity maintenance

Implementation conclusion status: wired. Evidence: SRC-1 `mem0/memory/main.py:991-1204,1747-1828,2105-2112,2778-2892`, `mem0/utils/entity_extraction.py:751-772`, `mem0/vector_stores/qdrant.py:186-245`.

After successful factual writes, text feeds embedding/lemmatization and entity extraction. Entity text is normalized and embedded. A matched existing entity (exact normalized text or similarity at least 0.95) receives the union of linked memory IDs; otherwise a new entity is inserted. This is near-duplicate merging of retained access metadata, supporting dedup. It is not proof that similar factual claims are merged. Missing NLP/dependencies, failed embeddings and entity-store errors can leave a valid fact without those extra retrieval signals.

> semantic_match = matches[0] if matches and matches[0].score >= 0.95 else None
>                         match = exact_match or semantic_match
> --- [mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L1166-L1167)

> linked = set(payload.get("linked_memory_ids", []))
>                             linked |= memory_ids
>                             payload["linked_memory_ids"] = sorted(linked)
> --- [mem0/memory/main.py](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py#L1171-L1173)

Later search embeds up to eight query entities, looks up up to 500 matches per entity, and boosts linked memory IDs subject to similarity and link-count weighting. This retained symbolic derivative changes ranking, and inherits its learning source/horizon from the factual input. Raw/procedural initial `_create_memory` calls generate dense/lexical access structures but do not invoke the ordinary batch entity-linking phase; later explicit text updates can create those links.

### Claims

### CLM-1 — Personalized assistants that learn over time

Conclusion status: claimed. The README attributes remembered preferences, adaptation and continuous learning to Mem0. Source: SRC-2 `README.md:74-80`. Retained-memory routes support persistent contextual adaptation; they do not alone establish improved capacity through criticism of consumed theories.

> It remembers user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and autonomous systems.
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CLM-2 — Managed benchmark improvements

Conclusion status: claimed. README numbers are reported operation of the managed platform, not observations or causal evidence for this Python subsystem. Source: SRC-2 `README.md:45-72`. The source itself excludes exact score transfer.

> Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Additional specialist constraint on CLM-2: the OSS API rejects add `timestamp` and search `reference_date`, while supporting expiration filtering. Source: SRC-1 `mem0/memory/main.py:817-818,1446-1447,461-484`. These surfaces cannot inherit hosted temporal or forgetting claims.

### CLM-3 — ADD-only extraction

Implementation conclusion status: wired. Doctrine conclusion status: claimed. This applies to the ordinary inferred write branch. Source: SRC-1 `mem0/memory/main.py:1030-1080`; SRC-2 `README.md:56-65`. Manual update/delete and the separate procedural branch limit this to automatic ordinary extraction; it is not a system-wide immutability guarantee.

> **Single-pass ADD-only extraction** -- one LLM call, no UPDATE/DELETE. Memories accumulate; nothing is overwritten.
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### Evidenced absences

### ABS-1 — No mandatory extraction rationale or evidence lineage

Conclusion status: absent. This bounded absence concerns the persisted default fact schema and active default acquisition/read paths, not all user metadata or custom prompts. Evidence: SRC-1 `mem0/memory/main.py:1012-1041,1079-1102,1680-1745`; SRC-2 `mem0/configs/prompts.py:917-945,608-619`.

> Return ONLY valid JSON parsable by json.loads(). No text, reasoning, explanations, or wrappers.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

The coordinator checked the same bounded absence at the pinned revision: case-insensitive query `rationale|evidence|source.?message|critici|reason` over `mem0/memory/main.py` ranges 1012-1041, 1079-1102, 1680-1745 and `mem0/configs/prompts.py` ranges 917-945, 608-619. The only lexical hit was the no-reasoning output instruction. The schema and assignments were also inspected semantically; the search alone is not the proof. The default output contract names text, attribution and optional links; the persisted fact does not require a rationale, evidence quote, source-message key or criticism record. The prompt nevertheless encourages context and reasons within text, including why a preference changed. Later text readers can consume such a reason if generated. No dedicated reason field, fidelity test, mandatory critique or explicit later diagnosis from retained reasons was found in these paths. This is weaker than claiming reasons are never retained.

Uninspected operation, provider internals and missing causal evidence remain limitations, not additional absence records.

### Behavioral-authority paths

### BAP-1 — Extraction guidance to the model

Conclusion status: wired. Consumer: CMP-2. Channel: system and user messages assembled from OBJ-1. Force: instruction, with best effort model compliance; no epistemic endorsement. Horizon: one extraction or procedural-summary call. Source: SRC-1 `mem0/memory/main.py:935-960,2019-2028`. The source quotes on OBJ-1 and the integrated write records provide the support. Host credentials permit model calls; downstream task-action authority remains with the excluded host.

### BAP-2 — Retained context to extraction

Conclusion status: wired. Consumer: CMP-2 on RTE-3. Channel: the user prompt includes selected OBJ-2 facts/OBJ-6 summaries and identity-selected OBJ-4 messages. Force: contextual knowledge under OBJ-1's deduplication/reference instructions; horizon: this extraction and consequent retained additions. Selector predicates and counts are on RTE-3. This is push; actual change in model behavior is unobserved. Evidence: SRC-1 and quotes on RTE-3 and OBJ-4.

### BAP-3 — Requested recall and external answering

Library implementation conclusion status: wired. External consumer conclusion status: afforded. Consumers: requesting chat application, then its answering model. Channels: search response, then text inside a system-role message in the README. Force: advisory knowledge, not automatic correctness or binding instruction adoption. Horizon: the current answer; future reuse depends on the caller. Pull and later automatic example supply are distinct operations. Evidence and quotes: RTE-4, SRC-1 and SRC-2.

### BAP-4 — Retained access structures to ranking

Conclusion status: wired. Consumer: search scorer on RTE-4. Channel: vectors, optional lexical scores and entity-to-memory associations OBJ-3. Force: ranking, bounded by semantic candidates and threshold before top-k. Horizon: one retrieval request; persisted indexes influence later requests. No epistemic warrant follows from a high score. Evidence and quotes: RTE-4 and RTE-7, SRC-1.

## Runtime account

An application constructs CMP-1 with model and storage configuration, supplies conversational messages and at least one user/agent/run identifier, then calls add. Identity values scope data; they are not authenticated principals inside this library. The code strips identity fields from arbitrary metadata and builds the effective scope from explicit parameters. The ordinary inferred path selects retained messages and nearby memories, assembles OBJ-1, calls CMP-2 once, parses its output, embeds accepted text with CMP-3, persists it, updates history and entity links, and returns IDs and ADD events. Return ends this invocation. The enclosing application owns further planning, tool use and user response. Source: SRC-1 `mem0/memory/main.py:150-171,362-401,760-1220`.

The material alternates are raw ingestion with `infer=False`, procedural summaries when agent ID and procedural type are supplied, optional image-description preprocessing RTE-2, direct update/delete/get/history operations, and AsyncMemory execution. The async procedural branch can use a caller-provided LangChain LLM; default async operations generally offload synchronous services, rather than delegating to autonomous workers. Direct provider registration RTE-1 changes implementation behavior inside the host process. Shell execution and server authorization are outside the selected library account; no claim about their presence elsewhere follows. Source: SRC-1 `mem0/memory/main.py:881-915,1829-1902,2455-2554,3708-3768`.

Read calls return selected memories to a caller; the README supplies a concrete assistant pattern: search top three user memories, insert their text into a system message, generate the assistant response, then retain the new exchange. That is inspectable example wiring, not evidence of a deployed conversation or changed answer. The built-in chat method raises NotImplementedError, so this subsystem should not inherit the enclosing assistant's reasoning or action authority. Source: SRC-2 `README.md:209-224`; SRC-1 `mem0/memory/main.py:2189-2190`.

Three static forcing cases bound the account:

1. **Provider failure versus parse failure.** In the ordinary inferred path, an LLM exception becomes LLMError for caller retry/fallback. An unparsable response instead yields an empty extraction, saves messages and returns no new memories. Thus an empty result is not a universal absence-of-facts signal. Source: SRC-1 `mem0/memory/main.py:951-989,2640-2675`.
2. **Partial vector insertion.** Failed batch insertion falls back to individual writes. Only records whose calls succeeded are returned and included in history. History and entity indexing have separate fallback or nonfatal error paths; this does not establish a transaction across all stores. The guarantee is an implementation protocol contingent on the backend honestly reporting insertion success, not an observed durability guarantee. Source: SRC-1 `mem0/memory/main.py:1053-1120,1192-1211,2730-2782`.
3. **Scope and expiry across entry paths.** Add requires identity scope and search validates filters, but get/update/delete take memory IDs directly. Search hides expired candidates by default; direct access and the internal extraction retrieval have different selectors. The host must own access grants and deletion policy. A filtered search is not proof of tenant isolation across every API. Source: SRC-1 `mem0/memory/main.py:362-401,921-931,1222-1235,1458-1463,1680-1686,1829-1902`.

**Decision roles and operating modes.** This is an open-request API. Callers supply messages, identity, configuration and optional custom instructions; computation selects context and proposes derived text; code decides structural admission and storage success. Callers can bypass extraction, override guidance, edit and delete entries. There is no operator confirmation step inside the inspected ordinary write path. A supplied conversation is a reference for preservation, not a ground-truth answer oracle for future user tasks. The active extraction policy requests checks of output completeness; inaccessible model reasoning prevents establishing what criticism it actually formulated. Reranker scores govern ranking, not acceptance of a proposition as true. Bounded experiments and curricula are not assessed modes; README hosted benchmark claims remain separate.

**Route audit and revision guidance.** The following completes the shared-route fields without duplicating their source-native progression. All routes return to their caller; none establishes autonomous worker delegation. No delegated visibility is applicable beyond named provider/service inputs. Actual behavioral activation is unobserved throughout.

| Route | Admission guidance and retained change | Rejection/recovery | Read-back, expiry and effect limits |
|---|---|---|---|
| RTE-2 | High-level image description prompt; candidate OBJ-7 feeds RTE-3 | Provider/image failures propagate; no truth check established | No direct persistence or expiry; later retention follows factual path |
| RTE-3 | OBJ-1 proposes contextual facts; model text, not a reasoning transcript, persists | Shape/text/embedding/hash guards; malformed output can yield no facts; insertion fallback and caller retry | Automatic identity/embedding selection; ten old memories and ten messages; internal vector retrieval lacks public expiry gate; BAP-2 |
| RTE-4 | Query, filters and configured scores select retained items; no content revision | Invalid parameters rejected; reranker failure falls back; no candidate truth acceptance | Requested pull and afforded external supply; public expiry filtering; BAP-3 and BAP-4 |
| RTE-5 | Caller-authored content or withdrawal decision; code preserves identity, records old/new state | Invalid/missing records rejected; store failures propagate; no coordinated rollback proven | Later search/extraction can see replacements; deletion history retained; scoped deletion does not clear raw history ring |
| RTE-6 | OBJ-1 continuation instruction or caller prompt creates descriptive history summary | Empty output/provider failure rejected; no verified verbatim-output test | Ordinary search/extraction may retrieve OBJ-6; no dedicated resume loop; caller can edit/delete |
| RTE-7 | Static normalization, embedding and similarity rules propose access associations | Failed NLP/embeddings/entities can omit extra signals; no factual validator | Retained OBJ-3 changes later ranking; update/delete clean links best effort; no independent relevance-expiry promise |

For the theory-builder conditions 1–4 on these admitting routes: guidance locality is wired on RTE-2, RTE-3, RTE-6 and RTE-7; its computational consumption is wired; formulated content-directed criticism is uninspected; criticism retained into a next round is uninspected. RTE-5 exposes authored replacement but the caller's theory, criticism and rationale are uninspected. These fields describe possible guidance-theory mappings, not a claim that every imported fact is a theory. Factual changes and summaries may preserve reasons, criticisms or input/outcome records in natural language, but their exact content and later critical uptake require instances. RTE-7 retains access metadata, not a formulated critique. Addressability is entry-level for text and associations, section-level for prompts; provider internals remain opaque. Guidance is applied, descriptive content is extracted or summarized, indexes are derived, and entries may be replaced; none of those verbs by itself establishes criticism. Learning from that criticism is uninspected for each route.

**Guarantees.** Identity metadata handling is a code invariant at that helper; isolation across arbitrary registered providers and direct-ID calls remains an external contract. ADD-only behavior is scoped to automatic ordinary extraction. Extraction faithfulness is prompt policy and best effort. Storage success reporting is protocol strength, with possible cross-store partial completion. No deployed isolation, model accuracy or end-to-end performance guarantee is established.

**Execution preflight:** no dynamic check planned. Considered a model-backed add/search conversation, an expiry case and a failed-store injection. Static inspection establishes their control paths; model/service setup or mocked responses would not establish real semantic accuracy or improved behavior. No probe reached the target, and no observed or causal result is claimed.

## Lens scoping

### Memory/context scope

Full depth. Trigger evidence: CLM-1 and the memory APIs in SRC-1. Included objects and routes are the integrated memory records below plus RTE-2 where preprocessing changes acquisition. Scope covers Python retained content, history, derived access data, ordinary/raw/procedural writes, retrieval and maintenance; configurable storage/provider internals are explicitly limited. Excludes other language implementations and hosted consumers. This is the system's principal work, so a brief lens would omit material branches.

### Epistemic scope

Full depth. Trigger evidence: CLM-1, CLM-3, OBJ-1 and truth-apt extraction outputs. The question is what warrants reliance on imported and derived memory, and whether its revision routes establish theory building or learning. Assessed families: content import/transformation, structural admission, retention, retrieval selection, manual revision, procedural summaries and optional vision. Hosted performance and unobserved model cognition are excluded; no system-complete knowledge-production judgment is licensed.

## Lens outputs

### Memory/context lens


Mem0 converts supplied conversations into durable textual entries, then builds access structures around them. The current default acquisition path is additive. Previously retained entries and recent messages are selected automatically to guide the next extraction. That internal consumer is already wired, independently of the README's external answering example. Evidence and quotes are retained on the object and route records below.

Context volume is controlled mostly by item counts: extraction reads ten prior messages and ten related memories; the prompt builder truncates each past message to 300 characters. Search overfetches `max(top_k * 4, 60)` semantic candidates and returns the requested count, default twenty. The README requests three. These are not an end-to-end token budget. New input and stored fact lengths have no enforcement corresponding to the prompt's requested 15–80 words in the inspected producer.

Content, access structures and audit history have different consumers. Text supports extraction and external answering; vectors, lexical representations and entity associations rank memories; recent messages resolve context during extraction; mutation history is exposed by an explicit API. A procedural summary is another stored text entry, despite its name. Its prompt asks for task continuation and errors, but no dedicated automatic resume loop is established by the inspected methods.

Trust is largely prompt-mediated. Scope identifiers constrain storage queries; they are not caller authentication. The producer retains attribution when emitted, but has no mandatory source-message identifier or independently checked reason for a fact. The prompt asks for factual extraction from user and assistant material. The implementation also serializes system messages into the extraction input. The README example places recalled material inside a system-role message and later supplies that conversation to `add`; this is a possible feedback path, not demonstrated contamination or demonstrated safety.


The qualifying chain is conversation messages → optional image description → extracted fact text → stored text/indexes → later extractor or retrieval selector, and, separately, execution messages → procedural summary → ordinary stored text/indexes → later extractor/search. The routes RTE-3, RTE-6, RTE-7 and RTE-2 cover these transformations. The raw message ring alone is not trace learning; the automatically derived facts and summaries are. There is no training of model weights in the inspected chain.

All these producers write within `add` or its awaited async equivalent. They are automatic despite the caller's initial choice to invoke them. Manual operations remain separately afforded by the route RTE-5. The default additive path can retain both an older fact and a later conflicting fact. The prompt asks the new text to capture the transition, but neither a truth check nor automatic withdrawal of the older record is established. Explicit mutation is available when a caller decides to correct or remove it.

Rationale/criticism retention is conditional content, not an enforced ledger: ordinary text may preserve reasons, and procedural prompts ask for errors/recovery. The objects OBJ-2, OBJ-5 and OBJ-6 and the absence record ABS-1 keep that distinction. Automatic record history documents mutations without their justifications. No demonstrated learning gain follows from these writes.


The most strongly established consumer is the extraction LLM. New `add` input triggers automatic identity/embedding selection and delivery of retained history/facts. Its requested operation is extraction, not a memory read, so that supply is push. Conversely, the documented chat application explicitly requests `search` results; its returned memories are pull. Its subsequent assembly of context for an answering model is a separate afforded push boundary. No unspecified hypothetical API caller is used as the sole basis of a pull classification.

Query identifiers, semantic candidates, optional lexical scores, entity links, expiration and optional reranking constrain what can arrive. The operative payload is stored text, not a latent summary of it. Search `explain` exposes score arithmetic. Explicit `get`, `get_all` and `history` establish storage/inspection capabilities, but no additional specific human/operator read workflow is assumed. The SDK's `chat` method raises `NotImplementedError`, reinforcing the boundary around external consumer wiring.


The fourteen frontmatter axes refer to the records above. Known write-agency/direction sets describe inspected shared API boundaries. Unknown provider internals prevent complete substrate/form/lineage/authority/curation unions. A positive wired witness is retained even when another branch remains afforded or uninspected.

The trace-learning axes cover the same qualifying transformations: factual extraction, procedural summarization, vision-to-text acquisition and derived access structures. Ordinary user memory has a documented cross-request use consistent with cross-task reuse; procedural continuation has an explicit per-task purpose at claim strength. Neither the bare name `run_id` nor `session_scope` decides a task horizon. Index and vision branches inherit the caller horizon; custom input/summary prompts can change it, so learning scope remains partial. All identified API transformations occur online, and produce natural-language and symbolic artifacts; raw input retention alone contributes no distilled-form claim.

Curation dedup relies on merging existing entity records and their linked IDs. Equal hashes that prevent duplicate acquisition alone would not support it. Evolve and invalidate rely on explicit mutation, not LLM autonomy. Decay relies on actual message eviction, despite the unavailable project decay feature. No synthesize/consolidate/promote value is inferred from the words intelligent, summary, extract or boost. Ranking boosts do not durably promote a tier.

Factual text remains knowledge even where a sample places it in a system message. No automatic enforcement, validation, instruction adoption or parametric learning is inferred. The recalled content's practical effect remains unobserved. Faithfulness tested is not determinable, rather than an unsupported global no.


### Epistemic lens

#### 1. Source-and-claim boundary

Mem0 at the reviewed commit; source register SRC-1 and SRC-2, boundary and exclusions as above. Analysis question: what transforms truth-apt conversational content, what licenses its retention/use, and what warrants learning claims? Assessed families are RTE-2, RTE-3, RTE-4, RTE-5, RTE-6 and RTE-7, with configuration RTE-1 classified as operational admission. CLM-1 and CLM-3 are the relevant work claims; CLM-2 is reported managed operation outside the implemented subsystem. Missing candidate instances prevent observed lifecycle and improvement conclusions.

#### 2. Epistemic-object inventory

| Object | Epistemic part and source | Candidate truth-apt content and limit |
|---|---|---|
| OBJ-1 | See canonical identity; active guidance | Normative extraction/continuation policy, with hypothesized contextual usefulness; no observed tested policy instance |
| OBJ-2 | See canonical identity and RTE-3, RTE-5 | Statements about users, agents, plans and events; source attribution is not truth verification |
| OBJ-3 | See canonical identity and RTE-7 | Access data and associations; naming/merging entities supports selection, not independently warranted identity claims |
| OBJ-4 | See canonical identity and RTE-3 | Retained utterances, including processed descriptions; acquisition preserves some message content but truncation/eviction limits later context |
| OBJ-5 | See canonical identity and RTE-5 | Structured mutation records; narrow evidence of requested changes, not their justification or cross-store completeness |
| OBJ-6 | See canonical identity and RTE-6 | Claimed execution history and task state; preservation is requested, exact fidelity untested |
| OBJ-7 | See canonical identity and RTE-2 | Image-description propositions; accuracy/ampliation cannot be determined without instances |

#### 3. Authority-route ledger

All rows have architectural status `implemented`; each is conditional on its route's trigger/configuration. Observed candidate state is `no instance observed` throughout. Canonical records carry progression and citations; functions are separated here. No row licenses source truth merely from operational success.

| Route/function | Target and content relation | Evaluator, timing and possible result | Epistemic authority; operational consequence; behavioral path |
|---|---|---|---|
| RTE-1 / operational admission/selection/consumption | Component/configuration; non-truth-apt update | Factory/configuration when instantiated; accept name or raise | Interface admissibility only; activates caller-selected implementation; caller/host authority |
| RTE-2 / content transformation | OBJ-7; indeterminate between preservation and ampliative interpretation | LLM on image input; description or failure | No independent image warrant; supplies candidate text to RTE-3; BAP-2 downstream |
| RTE-3 / content transformation | OBJ-2 from new messages plus context; indeterminate | LLM following OBJ-1 during add; candidate factual text | Intended extraction does not establish entailment; creates candidates; BAP-2 |
| RTE-3 / check/evidence production | Candidate shape, text, embeddings and equal hashes; no content change | Parser/guards before insertion; usable or skipped | Structural/storage eligibility only; no truth license; BAP-2 downstream |
| RTE-3 / disposition/acceptance | Candidate insertion eligibility; no content change | Code admits nonempty, embedded, nonduplicate candidates | Operational admission, not evidence-consuming epistemic acceptance; governs write |
| RTE-3 / retention | OBJ-2, OBJ-4 and OBJ-5; no content change | Vector/SQLite calls; success, partial auxiliary failure or error | Stored candidates become eligible for later reliance; not post-acceptance lifecycle integration |
| RTE-4 / operational admission/selection/consumption | OBJ-2, OBJ-6; no content change | Identity, expiry, semantic threshold, hybrid score and optional reranker on query | Relevance/selectability only; returns text and may supply external model; BAP-3 and BAP-4 |
| RTE-5 / content transformation | OBJ-2 raw import/replacement; acquisition/import or indeterminate replacement | Caller chooses text, ID and operation | Caller warrant unknown; explicit mutation allowed |
| RTE-5 / disposition/acceptance | Current entry; no content change | Code validates presence/arguments; update or remove | Mutation eligibility only; no epistemic criterion established |
| RTE-5 / retention | Replacement and OBJ-5 history; no content change | Storage/history API on mutation | Records content/event; rationale not required; later BAP-2 and BAP-3 |
| RTE-6 / content transformation | OBJ-6 execution summary; indeterminate | LLM under continuation prompt on supplied history | Intended preservation versus accidental/ampliative content unresolved |
| RTE-6 / disposition/acceptance | Summary content eligibility; no content change | Nonempty output check and embedding/store success | Operational admission only; no checked verbatim fidelity |
| RTE-6 / retention | OBJ-6 and history; no content change | Standard memory write after generation | Later ordinary retrieval; no demonstrated resumption or epistemic lifecycle integration |
| RTE-7 / content transformation | OBJ-3; non-truth-apt access update | Embedding, lexical/NLP extraction and association rules | Derived representation for selection, no factual acceptance |
| RTE-7 / check/evidence production | Entity match; no content change | Normalized equality or similarity threshold | Match evidence within index algorithm, not proof of real-world identity |
| RTE-7 / disposition/acceptance | Association merge/new entity; no content change | Code selects exact/semantic match and unions IDs | Operational index decision; changes BAP-4 ranking |
| RTE-7 / retention | OBJ-3; no content change | Best effort entity-store writes | Future scoring influence; auxiliary failure does not retract fact persistence |

These functions are supported by SRC-1 and their canonical quote blocks. OBJ-1 supplies policy-level purpose from SRC-2. The mismatch on CLM-1 is unresolved improvement attribution, not an assertion that retention fails. CLM-3 is implemented on RTE-3 only. CLM-2 has no observed OSS comparison in this evidence boundary.

#### 4. Per-object lifecycle disposition

For OBJ-2 on RTE-3 and RTE-5, transformation is `indeterminate`: source-based acquisition/reshaping and ampliative model interpretation remain possible. For raw imports, acquisition is wired and source warrant remains unknown. For model outputs, text, attribution and timestamps survive, but ABS-1 limits evidence lineage. Checks/admission/retention are implemented; no instance is observed. Candidate-linked messages and output comparisons would distinguish semantic preservation, entailment and novel claims. No accepted ampliative claim or post-acceptance integration is established.

For OBJ-6 on RTE-6, transformation is `indeterminate`: descriptive reshaping is intended, while loss or added interpretation cannot be ruled out from code. Structural checks and retention are implemented; observed candidate state is `no instance observed`. The default task-continuation purpose is not a test of its truth or fidelity. For OBJ-7 on RTE-2 the same observed state applies; image/output pairs are needed to decide the transformation and warrant.

For OBJ-4, acquisition/import and limited display reshaping apply; discovery lifecycle is not applicable to retained utterance copies. For OBJ-5, mutation recording is symbolic bookkeeping over operations; discovery lifecycle is not applicable, with cross-store completeness still limited. No lifecycle record for OBJ-1: no candidate truth-apt output for this guidance object; relevant updates are RTE-1 caller configuration. No lifecycle record for OBJ-3: no separately asserted truth-apt candidate output for access data; relevant update route is RTE-7. No global no-candidate claim is made, because OBJ-2, OBJ-6 and OBJ-7 can carry truth-apt content.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design support | Implemented routes | Observed and causal support | Supported conclusion and limit |
|---|---|---|---|---|
| CLM-1 | README personalized learning claim | RTE-3, RTE-4, RTE-5, RTE-6, RTE-7 | None inspected | Persistent contextual adaptation wired; improved capacity through criticism uninspected |
| CLM-2 | README managed scores with explicit proprietary caveat | No OSS score-transfer route | Managed results reported only; no inspected causal design | Hosted score claim retained at claimed strength; no OSS extrapolation |
| CLM-3 | README ADD-only account | RTE-3 | No instances observed | Ordinary automatic extraction is additive; RTE-5 explicit mutation is separate |

#### 6. Bounded conclusion

Mem0 retains and selects imported or generated content for later use. It performs operational selection and admission, with contextual model instructions and code-level shape/storage checks. Those functions do not supply independent epistemic warrant for user assertions, assistant claims or generated summaries. The extraction prompt's completeness check is an instruction to the model, not retained evidence that a specific criticism occurred. Revision history records change, not why that change was warranted. A narrowly wired reflection path over selected memory contents exists through BAP-2; a consumed, criticized and iterated theory of extraction, or demonstrated learning from such criticism, remains uninspected. No system-wide epistemic grade is assigned.


## Reconciliation

The specialist report was complete and matched the run, source, frozen input and method hashes. Its final bytes passed the shared source checker before integration. The coordinator retained all fourteen proposed axes and their per-value bases and coverage limits. No substantive classification was strengthened. The source report remains unchanged.

| Specialist proposal | Canonical record | Disposition |
|---|---|---|
| MEM-CMP-1 | CMP-6 | Registered and adopted |
| MEM-OBJ-1 | OBJ-2 | Registered and adopted |
| MEM-OBJ-2 | OBJ-3 | Registered and adopted |
| MEM-OBJ-3 | OBJ-4 | Registered and adopted |
| MEM-OBJ-4 | OBJ-5 | Registered and adopted |
| MEM-OBJ-5 | OBJ-6 | Registered and adopted |
| MEM-RTE-1 | RTE-3 | Registered and adopted |
| MEM-RTE-2 | RTE-4 | Registered and adopted |
| MEM-RTE-3 | RTE-5 | Registered and adopted |
| MEM-RTE-4 | RTE-6 | Registered and adopted |
| MEM-RTE-5 | RTE-7 | Registered and adopted |
| MEM-RTE-6 | RTE-2 | Merged same mechanism/claim; additional limits retained |
| MEM-ABS-1 | ABS-1 | Registered and adopted |
| MEM-CLM-1 | CLM-2 | Merged same mechanism/claim; additional limits retained |

All integration issues are disposed explicitly. RTE-3 is additive despite legacy update prompts and stale docstrings; RTE-5 owns explicit revisions. Generated memory-to-memory links are not conflated with OBJ-3 entity associations. Expiry and withdrawal remain entry-path-specific on RTE-4 and RTE-5; scoped deletion leaves OBJ-4 recent messages. RTE-6 remains a qualifying trace-fed summary route, with claimed per-task intent, possible errors/reasons retention and ordinary later retrieval. BAP-2 and BAP-3 keep internal push, caller pull and external example supply separate. CMP-6 and profile partial assessments preserve unknown provider alternatives and conditional NLP/BM25. CLM-2 confines managed scores and features to source claims; faithfulness remains not determinable.

Independent convergence is limited to the ordinary additive entry path, procedural alternate, optional image transformation, external consumer boundary and limits on hosted benchmark transfer: both coordinator and specialist inspected those before exchange. The specialist alone owns the normalized memory profile; integration is not independent semantic clearance. Its source-check repairs were completed before handoff; no coordinator report repair was needed. Overlapping quotations were retained once on canonical records. No unresolved anchored conflict remains.


## Bounded synthesis

At this pin, the Python subsystem is a returning memory computation. Its strongest supported contribution is a wired path from new conversational material through extraction and durable storage to later extraction context and application retrieval. It also offers raw writes, continuation summaries and caller-maintained edits. Learning in the separate sense of improved capacity attributable to criticism of a consumed theory is uninspected: no executed comparison or retained critical iteration establishes it. This does not negate the narrower memory-write contribution.

The ordinary route accumulates extracted statements rather than automatically overwriting them. That can preserve historical changes, but a later consumer still has to determine which statement applies. Hybrid relevance scoring and optional reranking decide what is delivered; they do not make supplied facts or model interpretations true. Structural admission and successful retention establish operational eligibility, not epistemic warrant.

For a caller using this API as scoped context storage, explicit identity filters, visible CRUD surfaces and recorded history distinguish the interface. For a caller needing verified knowledge, automatic conflict adjudication, authenticated direct-ID operations or proof of improved downstream answers, those conclusions are not established at this boundary. Model/provider choices, NLP availability, custom instructions and caller consumption can alter outcomes. The hosted benchmarks cannot close these gaps for the OSS code.

Theory-builder conditions 1–4 remain separate: localized guidance is wired; guidance consumption is wired; content-directed criticism of that guidance is uninspected; iteration that retains such criticism into a later policy round is uninspected. Membership is therefore uninspected. Memory revision alone cannot supply the missing links. Addressability is present in separately editable memory entries and named policy sections; persistence reaches later calls through stores, while exact operational horizons depend on scope and consumption. Reflection conclusion status: wired, narrowly for selected stored-memory contents. Add retrieves the current retained entries, represents them as an Existing Memories list, and uses that representation under a deduplication instruction to shape subsequent additions; later store changes can change the next representation. This is an architectural path, not observed successful self-correction. It does not establish reflection over extraction policy or a reflective theory builder. Agent-subject memories alone would not establish either claim. Computational execution of the selected pipeline is wired; autonomous theory-builder status is uninspected because membership is unresolved. Self-improvement has a wired retained-context contribution, with improvement in capacity and its attribution uninspected. No property is inferred from another.

Evidence that would change this assessment includes pinned executions demonstrating how recalled content changes later choices; retained comparisons isolating capacity gains; explicit content-directed criticism taken up by a subsequent round; source and candidate-linked evidence validating transformed claims; and deployment-specific enforcement for identities, backend failures and model endpoints.

The ontology mapping uses [theory builder](../../../../notes/definitions/theory-builder.md) and [reflective system](../../../../notes/definitions/reflective-system.md). These definitions organize the questions; they do not replace the source-native extraction and retrieval account.

## Limitations

| Limitation | Affected records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| No runtime experiment | SRC-1, CMP-1, CLM-1 | Static Python control paths | Activation, reliability, accuracy and attributed improvement | Candidate-linked runs and interventions |
| Mutable model/service resolution | CMP-2, CMP-3, CMP-4, CMP-5 | Inspected adapters/loaders | Exact weights, training/fixity across calls, provider semantic equivalence | Deployed version records and provider evidence |
| Host and managed product excluded | CLM-2, RTE-1 | Python subsystem | End-to-end security, hosted performance, autonomous task execution | Separately scoped host/platform analysis |
| Model-internal criticism opaque | OBJ-1, CMP-2 | Prompt and output contract | Formulated criticism, blame assignment, policy iteration and learning | Retained reasoning/candidate evidence with later uptake |
| Alternatives unevenly inspected | RTE-1, CMP-5 | Dispatch plus selected adapters | Complete backend and reranker behavior equivalence | Additional pinned branch inspections |

## Verification and blockers

### Semantic verification

Checked every source-dependent record against its pinned anchor and retained quotes; no prior analysis entered construction. Shared identity mappings resolve uniquely, and merged proposals keep their original referents. Inspected guarantees are scoped to their enforcement paths and external contracts. The static forcing cases do not claim observed outcomes.

Comparison scope matches OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-6 and RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7. Included unknown providers stay partial where they prevent a complete union; hosted and other language branches remain excluded. Known agency and direction values concern the shared API consumer boundaries, and known timing/form concern the identified API derivatives, not internal provider training. Trace-fed RTE-3 facts, RTE-6 continuation summaries, RTE-2 image preprocessing and RTE-7 derived indexes are all carried into source, horizon, timing and form assessments. Procedural per-task intent remains claimed; ordinary cross-task reuse remains afforded; identity names alone establish neither.

Push on RTE-3 names CMP-2, add trigger, identity/embedding selectors, OBJ-4 history and OBJ-2/OBJ-6 text; lexical push on RTE-4 belongs to the afforded README answering-model supply, not the requesting application's pull return. No identifier is classified as push merely because an API accepts an ID. Ranking and knowledge authority remain distinct; no fact enforcement or learned weights are inferred. Curation dedup is retained entity-index merging, not acquisition hash checks. The procedural summary is not omitted from trace learning. No observed faithfulness or improved-capacity conclusion is claimed. Epistemic architectural status and observed candidate state remain separate.

### Deterministic validation

Typed validation and frozen-source verification of this result passed. Guarded publication repeats the source and handoff checks against the final bytes. Citation anchors were checked against their supporting pinned passages; no source or analytical boundary changed.

### Blockers

none
