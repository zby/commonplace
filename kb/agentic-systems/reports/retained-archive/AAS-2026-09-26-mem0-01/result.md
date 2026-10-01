---
type: types/agentic-system-analysis-result.md
description: "Mem0 synchronous OSS memory: source-pinned extraction, retrieval, maintenance and evidence limits."
run-id: AAS-2026-09-26-mem0-01
system: "Mem0"
run-date: "2026-09-26"
result-disposition: complete
target-class: "memory/knowledge/context-engineering system"
boundary-kind: subsystem-only
reviewed-boundary: "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd"
analysis-cutoff: "2026-09-26"
evidence-tier: code-grounded
memory-comparison:
  scope: "Synchronous Python OSS Memory: inferred factual add, direct infer=False add, procedural add, get/get_all/search with rerank=False, explicit update/delete/delete_all/reset/history, saved message context, factual and procedural payloads, Qdrant dense and optional BM25 access structures, entity side collection and SQLite history; default OpenAI adapters and NLP available/failure paths. Excludes other stores, AsyncMemory, vision, managed client/cloud, server/auth, CLI, integrations and downstream application generation. Shipped prompts are method inputs, not accumulated memory."
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values: [sqlite, vector]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-7]
      note: "Logical stores are Qdrant collections and SQLite tables. Local database files are backing implementation, not independently consumed file memory; entity links are payloads, not a graph-store route."
    representational_form:
      assessment: known
      basis: wired
      values: [natural-language, parametric, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-7]
      note: "Text is interpreted; scope, expiry, IDs and links have parser/selector semantics; dense representations are distributed-parametric. Sparse BM25 indices are lexical access structures. No model-weight updating is implied."
    lineage:
      assessment: known
      basis: afforded
      values: [authored, imported, other-compiled, trace-extracted]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5, OBJ-7, RTE-2, RTE-5]
      note: "Caller-authored direct text and revisions are afforded; supplied raw messages are imported; extraction and summaries derive from conversations or execution traces; history, entity links and retrieval encodings are compiled derivatives."
    behavioral_authority:
      assessment: known
      basis: wired
      values: [knowledge, learning, ranking, routing]
      records: [BAP-1, OBJ-3, OBJ-5, OBJ-7, RTE-6, RTE-4]
      note: "Internal extraction consumes retained text as context and learning input; access structures rank or route retained parts. The summary label does not confer instruction authority, and return to a caller does not establish host activation."
    write_agency:
      assessment: known
      basis: afforded
      values: [automatic, manual]
      records: [RTE-1, RTE-2, RTE-3, RTE-5]
      note: "Automatic extraction, summarization and index maintenance are wired; direct caller-authored text and explicit edits afford manual authorship through APIs. An add call triggering extraction is still automatic acquisition."
    curation_operations:
      assessment: known
      basis: wired
      values: [decay, dedup, evolve, invalidate]
      records: [RTE-1, RTE-5, OBJ-3, OBJ-5]
      note: "Entity near-duplicate merging, explicit revisions, deletion with retained history, and rolling-message eviction/reset. Extraction itself and index generation do not establish consolidation or synthesis; transient retrieval boosting is ranking rather than retained promotion."
    read_back_direction:
      assessment: known
      basis: afforded
      values: [pull, push]
      records: [RTE-4, RTE-5, BAP-1, BAP-2, RTE-6]
      note: "Push is wired automatic extraction-context assembly. Pull is the SDK request/return route afforded to the documented application memory caller; actual downstream answer generation is excluded."
    read_back_signal:
      assessment: known
      basis: wired
      values: [identifier, inferred-embedding]
      records: [BAP-1, RTE-6]
      note: "Push matches saved messages to a scope key and retrieves scope-filtered nearest memories from the current messages' embedding. Count/recency limits are budgets; pull-time lexical/entity ranking is not an additional push signal."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-1, RTE-3, BAP-1, RTE-6]
      note: "Conversation-derived facts and execution-history summaries are automatically written durably and can enter later extraction context from the same collection. This is an implemented route, not observed improvement or model training."
    trace_source:
      assessment: known
      basis: afforded
      values: [session-logs, tool-traces, trajectories]
      records: [RTE-1, RTE-3]
      note: "Factual writes process conversation messages; procedural prompt explicitly accepts sequential agent execution history including exact action/tool outputs. Caller supply of those traces is afforded, not instrumented collection."
    learning_scope:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-1, RTE-3, RTE-6]
      note: "Default procedural intent is continuation of one task; factual retention can serve later conversations, but no task/project lifecycle bounds either API route or custom-prompt branch. Identity labels alone cannot establish a complete task-horizon union."
    learning_timing:
      assessment: not-determinable
      basis: null
      values: []
      records: [RTE-1, RTE-3]
      note: "Both writes run synchronously when called. Default procedural continuation and the README conversation example afford online use; the scoped library does not establish caller task timing or exclude offline/staged invocation."
    distilled_form:
      assessment: known
      basis: wired
      values: [natural-language, parametric, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-5, OBJ-7, RTE-1, RTE-3]
      note: "The qualifying write chains retain natural-language extracted facts/summaries together with compiled metadata/link records and dense retrieval representations used later. No learned weight change is claimed. Text-only distillation would be natural-language, but would omit operative outputs in this commissioned boundary."
    faithfulness_tested:
      assessment: known
      basis: wired
      values: ["no"]
      records: [ABS-1]
      note: "No retained execution evidence testing dependence on recalled content is supplied or produced in this frozen source-only analysis. This is a bounded evidence finding, not a claim that Mem0 has never been evaluated."
---

# Mem0 agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-mem0-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/mem0.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-mem0-01/memory-report.md`

**Memory analysis report SHA-256:** cffb2d220cafc9f4f9f69ae01faa3905db2136c58d2f9cc6c1cf21aca156c31f

## Boundary and evidence

Evidence basis: static source inspection at 94c3fe9f238f3dbf29c9ce98643bd71eb13077cd, resolved from reachable default branch main on 2026-09-26. No running product, benchmark or causal intervention was observed. The intended use is comparison of the synchronous open-source memory mechanism and its limits, not a product recommendation.

The target is a memory/knowledge/context-engineering system serving a calling application; it returns computation rather than owning the enclosing assistant loop. The subsystem boundary includes synchronous Python Memory factual inferred/raw and procedural writes, get/get_all/search with rerank=False, explicit maintenance and history, default Qdrant/OpenAI adapters, SQLite retained context, entity and dense/sparse access structures, and inspected NLP availability/failure branches. Custom text/prompts are included as input alternatives; their content and scheduling remain caller-owned.

Other vector/model providers, AsyncMemory parity, vision preprocessing, managed client/service internals, self-hosted server/auth, CLI, JavaScript SDK and integrations are excluded. Their exclusion prevents provider-independent, whole-product, concurrency-parity and deployed-isolation claims. The downstream assistant is excluded, preventing claims about answer activation or benefit. The managed service's proprietary optimizations and benchmarks are outside the OSS evidence horizon. External model, spaCy, FastEmbed and Qdrant implementation internals are not inspected; their call interfaces support wiring claims, not behavioral reliability or exact deployed package/weight identity. Optional reranking is inventoried as CMP-3 but excluded from all aggregate memory classifications.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | implementation, with embedded prompt doctrine identified separately | synchronous mem0/memory/main.py and helpers; storage.py; configs/prompts.py and defaults; llms/openai.py; embeddings/openai.py; vector_stores/qdrant.py; utils/entity_extraction.py, lemmatization.py, spacy_models.py and scoring.py | [Memory](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py), full paths on canonical records and attributed excerpts below | External providers/package internals and excluded implementations prevent observed or universal guarantees |
| SRC-2 | Git | `https://github.com/mem0ai/mem0` | `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd` | doctrine/design and attributed reported performance; no observed execution | README.md algorithm, managed-platform qualification, product claims and requesting application example | [README](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/README.md) | Benchmark traces, interventions and proprietary implementation unavailable within boundary; no OSS performance attribution |

Operational access root: `/home/zby/llm/commonplace/related-systems/mem0ai--mem0`. All Git evidence used commit-addressed reads; working tree and local HEAD were not evidence. No prior review or substantive prior audit supplied this analysis.

## Shared records

### Components

#### CMP-1 — extraction and procedural generator

Implementation conclusion status: wired. The configured OpenAI adapter defaults to `gpt-5-mini`, sends the constructed messages to chat completions and returns message content. RTE-1 asks for JSON; RTE-3 requests text. This is an external model dependency, not inspected generation behavior. Provider calls may fail. SRC-1 `mem0/llms/openai.py:39-53,81-83,106-150`.

Generator call — SRC-1 `mem0/llms/openai.py:136-142`.

>         if response_format:
>             params["response_format"] = response_format
>         if tools:  # TODO: Remove tools if no issues found with new memory addition logic
>             params["tools"] = tools
>             params["tool_choice"] = tool_choice
>         response = self.client.chat.completions.create(**params)
>         parsed_response = self._parse_response(response, tools)
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



Parameter mutation by this adapter: inapplicable to its inference-only responsibility; provider-side changes remain uninspected. Exact-version identity pinning: uninspected at the provider; configured model name and endpoint resolution are wired, with default gpt-5-mini and configurable OpenRouter/base URL. Provider weight changes remain uninspected. This conclusion does not assess memory learning.

>         if not self.config.model:
>             self.config.model = "gpt-5-mini"
> --- `mem0/llms/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

#### CMP-2 — memory and query embedder

Implementation conclusion status: wired. OpenAI defaults to `text-embedding-3-small` and 1536 dimensions; it obtains floating-point embeddings from the endpoint, with batch results sorted by response index and count-checked. Fixed model configuration and external weights are not memory changed through use. Dense outputs retained in OBJ-7 are. SRC-1 `mem0/embeddings/openai.py:15-19,37-81`.

Embedding output — SRC-1 `mem0/embeddings/openai.py:47-55`.

>         text = text.replace("\n", " ")
>         kwargs = {
>             "input": [text],
>             "model": self.config.model,
>             "encoding_format": "float",
>         }
>         if self._pass_dimensions_to_api:
>             kwargs["dimensions"] = self.config.embedding_dims
>         return self.client.embeddings.create(**kwargs).data[0].embedding
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



Parameter mutation by this adapter: inapplicable to its embedding-inference responsibility; retained vectors change, provider-side parameter changes remain uninspected. Exact-version pinning: uninspected at the provider; the default alias is not an immutable provider-weight identity.

>         self.config.model = self.config.model or "text-embedding-3-small"
>         # Only pass `dimensions` to the API when the user set embedding_dims; non-matryoshka
>         # OpenAI-compatible backends (vLLM, Voyage, etc.) reject the parameter
>         self._pass_dimensions_to_api = self.config.embedding_dims is not None
>         self.config.embedding_dims = self.config.embedding_dims or 1536
> --- `mem0/embeddings/openai.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

#### CMP-3 — optional reranker

Wired factory/configuration and conditional call at SRC-1 `mem0/memory/main.py:504-510,1514-1519`; provider behavior and parameter fixity uninspected. It can replace ordering when caller sets rerank and a component exists; exceptions retain original results. Excluded from the memory-comparison boundary, which fixes rerank=False.

#### CMP-4 — optional spaCy linguistic pipeline

Wired load of en_core_web_sm for entity extraction and lemmatization; distributed-parametric external NLP model used under symbolic filtering rules. The loader can download the named package when missing, so package/model identity is not pinned by this code. Runtime training inside the external package and its actual deployed weights are uninspected; the inspected code loads and invokes the package. Missing model returns no entity processing. SRC-1 `mem0/utils/spacy_models.py:20-91`; `mem0/utils/entity_extraction.py:751-772`. FastEmbed Qdrant/bm25 is treated as the lexical encoder feeding OBJ-7, not presumed learned weights from its class name.

> 
>     if not spacy.util.is_package("en_core_web_sm"):
>         logger.info("Downloading spaCy model en_core_web_sm...")
>         try:
>             from spacy.cli import download
> 
>             download("en_core_web_sm")
>             logger.info("spaCy model en_core_web_sm downloaded successfully")
> --- `mem0/utils/spacy_models.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`
### Operative objects

#### OBJ-1 — factual or raw memory payload

Implementation conclusion status: wired. Qdrant points retain `data`, MD5 of text, timestamps, lemmatized text, scope metadata, optional attribution/expiry and arbitrary caller metadata. RTE-1 produces extracted natural-language text; RTE-2 imports direct text; RTE-5 affords explicit authorship/revision. Fields used for scope/expiry/identity are symbolic operative parts; freeform returned metadata does not acquire an unknown host interpretation within this boundary. Dense and sparse access representations are split into OBJ-7. Consumer: BAP-1 receives `data` as extraction context; BAP-2 returns display text and metadata on request. No per-fact source-message IDs, extraction rationale, confidence, or model/prompt revision are constructed in the inferred payload. Attribution is an LLM output field, not verified provenance. SRC-1 `mem0/memory/main.py:1028-1041,1238-1267,1975-2005`.

Payload construction — SRC-1 `mem0/memory/main.py:1030-1041`.

>             memory_id = str(uuid.uuid4())
>             mem_metadata = deepcopy(metadata)
>             mem_metadata["data"] = text
>             mem_metadata["text_lemmatized"] = text_lemmatized
>             mem_metadata["hash"] = mem_hash
>             if "created_at" not in mem_metadata:
>                 mem_metadata["created_at"] = datetime.now(timezone.utc).isoformat()
>             mem_metadata["updated_at"] = mem_metadata["created_at"]
>             if mem.get("attributed_to"):
>                 mem_metadata["attributed_to"] = mem["attributed_to"]
> 
>             records.append((memory_id, text, embed_map[text], mem_metadata))
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### OBJ-2 — procedural memory text

Implementation conclusion status: wired. Same main vector collection and creation helper as OBJ-1, with `memory_type=procedural_memory`. RTE-3 produces a summary string from supplied messages, strips code fences and rejects empty output. The stored string may contain quoted tool outputs or structured fragments, but the included model consumer interprets it as text; no executable-procedure consumer is present. Its embeddings and structured metadata remain separate operative forms. No complete raw execution log or verification result is retained by this path. SRC-1 `mem0/memory/main.py:2007-2050`.

Procedural persistence — SRC-1 `mem0/memory/main.py:2043-2045`.

>         metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### OBJ-3 — rolling saved messages

Implementation conclusion status: wired. SQLite `messages` retains raw supplied role/content/name plus generated row ID, session scope and creation time. These are imported message traces, not summaries. RTE-1 saves them even when extraction yields no records; it does not do so if the LLM call raises before reaching persistence. RTE-2 and RTE-3 bypass this save route. The table retains the latest ten per exact scope, evicting older rows. RTE-6 selects them for later extraction. No durable summary replaces evicted messages. SRC-1 `mem0/memory/storage.py:128-148,257-324`; `mem0/memory/main.py:988-991,1043-1045,1206-1207`.

Rolling eviction — SRC-1 `mem0/memory/storage.py:282-291`.

>                 self.connection.execute(
>                     """
>                     DELETE FROM messages WHERE session_scope = ? AND id NOT IN (
>                         SELECT id FROM (
>                             SELECT id FROM messages WHERE session_scope = ? ORDER BY created_at DESC LIMIT 10
>                         )
>                     )
>                 """,
>                     (session_scope, session_scope),
>                 )
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### OBJ-4 — change history

Implementation conclusion status: wired. SQLite rows retain memory ID, old/new text, event, timestamps, deletion flag and optional actor/role. This is generated change evidence, not an extraction rationale or a fact-to-source-message dependency graph. `history(memory_id)` returns it to the requesting caller; the included extraction route does not read it. Deletion preserves previous text in history; reset drops history and messages. SRC-1 `mem0/memory/storage.py:102-119,227-255,326-335`; `mem0/memory/main.py:1960-1973,2114-2140`.

History payload — SRC-1 `mem0/memory/storage.py:108-118`.

>                     CREATE TABLE IF NOT EXISTS history (
>                         id           TEXT PRIMARY KEY,
>                         memory_id    TEXT,
>                         old_memory   TEXT,
>                         new_memory   TEXT,
>                         event        TEXT,
>                         created_at   DATETIME,
>                         updated_at   DATETIME,
>                         is_deleted   INTEGER,
>                         actor_id     TEXT,
>                         role         TEXT
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### OBJ-5 — entity side collection

Implementation conclusion status: wired. A lazily initialized second Qdrant collection stores entity text, type, linked memory IDs and scope, plus dense embeddings and optional sparse representations. It shares the Qdrant client. These are access metadata derived from memory text, not independently grounded facts or a graph database. NLP extraction feeds exact normalized lookup and semantic matching at 0.95; a match unions linked memory IDs into the existing entity. This is semantic deduplication of retained entity records. Search later uses similarity and link count to compute per-memory boosts. SRC-1 `mem0/memory/main.py:558-650,1100-1204,1747-1827`.

Entity merge — SRC-1 `mem0/memory/main.py:1166-1179`.

>                         semantic_match = matches[0] if matches and matches[0].score >= 0.95 else None
>                         match = exact_match or semantic_match
>                         if match:
>                             # Update existing entity
>                             payload = match.payload or {}
>                             linked = set(payload.get("linked_memory_ids", []))
>                             linked |= memory_ids
>                             payload["linked_memory_ids"] = sorted(linked)
>                             try:
>                                 self.entity_store.update(
>                                     vector_id=match.id,
>                                     vector=None,
>                                     payload=payload,
>                                 )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### OBJ-6 — static generation guidance, outside retained-through-use profile

Implementation conclusion status: wired. ADDITIVE_EXTRACTION_PROMPT and optional AGENT_CONTEXT_SUFFIX guide factual generation; caller `prompt` overrides configured custom instructions for that invocation. The procedural caller prompt replaces its default system prompt. These are method instructions, not learned memory. The extraction prompt demands input-grounded facts and role attribution; no corresponding truth checker runs before persistence. SRC-1 `mem0/memory/main.py:942-964,2018-2025`; `mem0/configs/prompts.py:677-689,918-942`.

Grounding instruction — SRC-1 `mem0/configs/prompts.py:679-681`.

> - **No Fabrication**: Every detail must trace to the inputs. If you can't point to where it came from, don't include it.
> - **No Implicit Attribute Inference**: Don't infer gender, age, ethnicity, etc. from names or context. Only record explicitly stated attributes.
> - **Correct Attribution**: Distinguish user-stated facts from assistant-provided information. Frame assistant content appropriately.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



> You are a Memory Extractor — a precise, evidence-bound processor responsible for extracting rich, contextual memories from conversations. Your sole operation is ADD: identify every piece of memorable information and produce self-contained, contextually rich factual statements.
> 
> You extract from BOTH user and assistant messages. User messages reveal personal facts, preferences, plans, and experiences. Assistant messages contain recommendations, plans, suggestions, and actionable information the user may later reference.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

#### OBJ-7 — retained retrieval encodings

Record kind: object. Implementation conclusion status: wired. Dense vectors from CMP-2 and optional BM25 sparse vectors accompany OBJ-1, OBJ-2 and OBJ-5 in Qdrant. Dense representations are distributed-parametric under Commonplace's definition, even though model weights are unchanged. Lemmatized tokens and sparse lexical coordinates are compiled retrieval data. Retained vectors affect nearest-neighbor selection; entity vectors affect link matching and retrieval boosts. Qdrant's existing-collection branch disables BM25 when no sparse slot exists; missing encoder or encoding failure also disables that signal. Those inspected alternatives keep semantic retrieval available. SRC-1 `mem0/vector_stores/qdrant.py:93-163,186-246,415-484`; `mem0/embeddings/openai.py:37-81`.

Dense and sparse point — SRC-1 `mem0/vector_stores/qdrant.py:239-246`.

>             # Build named vectors: dense + optional BM25 sparse (only if collection has the slot).
>             named_vectors = {"": vector}
>             if self._has_bm25_slot and bm25_sparse_vectors[idx] is not None:
>                 named_vectors["bm25"] = bm25_sparse_vectors[idx]
> 
>             points.append(PointStruct(id=point_id, vector=named_vectors, payload=payload))
> 
>         self.client.upsert(collection_name=self.collection_name, points=points)
> --- `mem0/vector_stores/qdrant.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### Routes

#### RTE-1 — inferred factual add

Implementation conclusion status: wired. Trigger: explicit `add(..., infer=True)` with a scope ID and text messages. Producer: CMP-1. Inputs: current parsed messages, top ten nearest stored memories under supplied identity filters, latest ten stored messages for the exact scope, and OBJ-6. The extractor creates candidate facts; code embeds, exact-hash checks against retrieved memories and this batch, appends UUID records, logs successful writes and updates entities. It never executes model-requested UPDATE or DELETE operations in this route. Model-generated `linked_memory_ids` are not copied into its constructed payload; OBJ-5 supplies a separate actual link mechanism. Source-side docstring at lines 790-791 is stale relative to this implementation. SRC-1 `mem0/memory/main.py:918-1220`.

Internal retrieval — SRC-1 `mem0/memory/main.py:920-933`.

>         # Phase 0: Context gathering
>         session_scope = _build_session_scope(filters)
>         last_messages = self.db.get_last_messages(session_scope, limit=10)
>         parsed_messages = parse_messages(messages)
> 
>         # Phase 1: Existing memory retrieval
>         search_filters = {k: v for k, v in filters.items() if k in ("user_id", "agent_id", "run_id") and v}
>         query_embedding = self.embedding_model.embed(parsed_messages, "search")
>         existing_results = self.vector_store.search(
>             query=parsed_messages,
>             vectors=query_embedding,
>             top_k=10,
>             filters=search_filters,
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Extractor input and delivery — SRC-1 `mem0/memory/main.py:950-964`.

>         user_prompt = generate_additive_extraction_prompt(
>             existing_memories=existing_memories,
>             new_messages=parsed_messages,
>             last_k_messages=last_messages,
>             custom_instructions=custom_instr,
>         )
> 
>         try:
>             response = self.llm.generate_response(
>                 messages=[
>                     {"role": "system", "content": system_prompt},
>                     {"role": "user", "content": user_prompt},
>                 ],
>                 response_format={"type": "json_object"},
>             )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Exact text rejection — SRC-1 `mem0/memory/main.py:1022-1026`.

>             mem_hash = hashlib.md5(text.encode()).hexdigest()
>             if mem_hash in existing_hashes or mem_hash in seen_hashes:
>                 logger.debug(f"Skipping duplicate memory (hash match): {text[:50]}")
>                 continue
>             seen_hashes.add(mem_hash)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



For RTE-1 performs automatic acquisition, not automatic revision of old factual memories. It first assembles retained context, makes one model request, parses JSON and batches embeddings. The implemented rejection checks are empty/missing text, embedding availability and identical text hashes among retrieved records and the current batch. The prompt asks for semantic duplicate avoidance, but that is model-mediated filtering, not a tested guarantee. A near duplicate outside the top-ten retrieval window need not be considered. Explicit UPDATE/DELETE remain RTE-5 operations. Neither a source label nor an old docstring changes this path.

Persistence has several failure boundaries. A failed extraction-model call raises LLMError; JSON parsing failure becomes no extracted records and still saves raw messages. The vector insert falls back from batch to individual writes; only successfully inserted records produce returned ADD entries and subsequent history/entity work. If all insertions fail, messages are saved and VectorStoreError is raised. History and entity failures after vector persistence can be logged without undoing the live memories. SQLite operations are transactional locally, but vector data, history, entities and saved messages do not share a transaction. SRC-1 `mem0/memory/main.py:957-991,1052-1098,1193-1207`.

Successful write tracking — SRC-1 `mem0/memory/main.py:1055-1068`.

>         persisted_records = []
>         try:
>             self.vector_store.insert(
>                 vectors=all_vectors,
>                 ids=all_ids,
>                 payloads=all_payloads,
>             )
>             persisted_records = records
>         except Exception:
>             # Fallback: insert one by one
>             for rec in records:
>                 try:
>                     self.vector_store.insert(vectors=[rec[2]], ids=[rec[0]], payloads=[rec[3]])
>                     persisted_records.append(rec)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


History failure handling — SRC-1 `mem0/memory/main.py:1090-1098`.

>         try:
>             self.db.batch_add_history(history_records)
>         except Exception:
>             # Fallback: add one by one
>             for hr in history_records:
>                 try:
>                     self.db.add_history(hr["memory_id"], None, hr["new_memory"], "ADD", created_at=hr.get("created_at"))
>                 except Exception as e:
>                     logger.error(f"Failed to add history for {hr['memory_id']}: {e}")
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


For OBJ-3's rolling message eviction is automatic forgetting. It is not a summary or consolidation checkpoint. RTE-2 stores each direct message as a separate memory; its role/name metadata and history differ from inferred facts, whose optional `attributed_to` field comes from CMP-1. RTE-3 produces a separate summary even when infer=False is passed with the procedural dispatch conditions. A procedural type without agent_id falls through to the ordinary add path; the label alone does not activate procedural creation (SRC-1 `mem0/memory/main.py:831-879`).

For trace learning, the factual chain is supplied conversation → CMP-1 extracted text → OBJ-1 plus encodings → RTE-6 → later CMP-1. The procedural chain is supplied execution/conversation history → CMP-1 summary → OBJ-2 plus encodings → RTE-6 → later CMP-1. The default procedural prompt also affords use by a continuing agent, but its host wiring is excluded. Both qualify on the internal chain; raw OBJ-3 retention alone does not.

Reasons are not first-class retained dependencies. Factual output asks for no reasoning/explanations, and the writer stores text/attribution rather than supporting message IDs or rationales. A reason explicitly present in a fact's text can be passed on, but there is no required reason field or dedicated later reader. Procedural guidance asks for task objective, exact results, challenges, and current context; those can preserve why a next step is sensible, yet the prompt does not require a justification for every prescription and no code verifies preservation. RTE-6 later reads the entire selected text, including any retained reason, without interpreting a separate reason slot. This supports optional contextual rationale, not guaranteed diagnostic traceability. SRC-1 `mem0/configs/prompts.py:327-359,918-936`; `mem0/memory/main.py:938-940,1030-1041,2043-2045`.

No reasoning field required — SRC-1 `mem0/configs/prompts.py:920-920`.

> Return ONLY valid JSON parsable by json.loads(). No text, reasoning, explanations, or wrappers.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Revision admission: input messages and OBJ-6 shape the model's candidate facts; code can reject missing/duplicate/unembeddable text, while the caller chooses invocation and later RTE-5 changes. No human approval stage is wired inside this call. The default prompt specifies extraction, attribution and duplicate avoidance, not an external expected-answer oracle. Raw source statements have unknown truth warrant. Persistent guidance is stored fact text and retrieval metadata, not a mandatory rationale or criticism object. For the shipped rule set, theory-builder conditions 1–4 are: localized method content wired; model consumption wired; content-directed criticism of those rules uninspected; iteration of criticism into revised rules uninspected. Separate addressability: prompt clauses are readable but not individually versioned/revised by this call. Learning attributable to criticism: uninspected. Stored facts are addressable by memory ID, but that is not evidence that they are explanatory theories or have survived criticism.

#### RTE-2 — direct add without inference

Implementation conclusion status: wired. Trigger: caller chooses `infer=False`, except that the earlier procedural dispatch takes precedence if its conditions hold. Each valid non-system message becomes a new text memory, with role and optional name mapped to actor ID. CMP-2 embeds it; `_create_memory` persists it and history. It neither checks duplicate text nor automatically links entities nor saves OBJ-3. This route affords caller-authored memory and import of existing text; it is not qualifying trace learning merely because raw messages are stored. SRC-1 `mem0/memory/main.py:855-864,881-916,1975-2005`.

Direct write — SRC-1 `mem0/memory/main.py:893-905`.

>                 if message_dict["role"] == "system":
>                     continue
> 
>                 per_msg_meta = deepcopy(metadata)
>                 per_msg_meta["role"] = message_dict["role"]
> 
>                 actor_name = message_dict.get("name")
>                 if actor_name:
>                     per_msg_meta["actor_id"] = actor_name
> 
>                 msg_content = message_dict["content"]
>                 msg_embeddings = self.embedding_model.embed(msg_content, "add")
>                 mem_id = self._create_memory(msg_content, {msg_content: msg_embeddings}, per_msg_meta)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



Revision admission: caller proposes direct text, and code performs structural filtering, embedding and insertion. Rejection ability is structural; semantic veto remains with the caller outside this boundary. Guidance is caller-provided content plus fixed import code, retained as input records and compiled indexes, not an evidenced theory-criticism process. Partial progress across messages can persist; no global rollback is established. Later consumer is RTE-6 or RTE-4; the call returns ADD entries.

#### RTE-3 — procedural summary creation

Implementation conclusion status: wired. Trigger: `agent_id` and `memory_type=procedural_memory` in `add`; no automatic checkpoint trigger is implemented. Producer: CMP-1 using supplied conversation/execution messages plus default or caller system prompt. The default describes a same-task continuation summary of sequential agent actions, exact tool/action outputs, errors, discoveries and current context. Generated text becomes OBJ-2 through `_create_memory`. Later BAP-1 can select it from the same collection without a memory-type exclusion; RTE-4 can return it to a caller. The continuation agent role is documented by the prompt, but no host continuation loop is inspected. SRC-1 `mem0/memory/main.py:853-864,2007-2050`; `mem0/configs/prompts.py:326-359`.

Procedural intended consumer — SRC-1 `mem0/configs/prompts.py:327-327`.

> You are a memory summarization system that records and preserves the complete interaction history between a human and an AI agent. You are provided with the agent’s execution history over the past N steps. Your task is to produce a comprehensive summary of the agent's output history that contains every detail necessary for the agent to continue the task without ambiguity. **Every output produced by the agent must be recorded verbatim as part of the summary.**
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Procedural action evidence intent — SRC-1 `mem0/configs/prompts.py:341-350`.

>   2. **Action Result (Mandatory, Unmodified)**:
>      - Immediately follow the agent action with its exact, unaltered output.
>      - Record all returned data, responses, HTML snippets, JSON content, or error messages exactly as received. This is critical for constructing the final output later.
> 
>   3. **Embedded Metadata**:
>      For the same numbered step, include additional context such as:
>      - **Key Findings**: Any important information discovered (e.g., URLs, data points, search results).
>      - **Navigation History**: For browser agents, detail which pages were visited, including their URLs and relevance.
>      - **Errors & Challenges**: Document any error messages, exceptions, or challenges encountered along with any attempted recovery or troubleshooting.
>      - **Current Context**: Describe the state after the action (e.g., "Agent is on the blog detail page" or "JSON data stored for further processing") and what the agent plans to do next.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Procedural input construction — SRC-1 `mem0/memory/main.py:2018-2029`.

>         parsed_messages = [
>             {"role": "system", "content": prompt or PROCEDURAL_MEMORY_SYSTEM_PROMPT},
>             *messages,
>             {
>                 "role": "user",
>                 "content": "Create procedural memory of the above conversation.",
>             },
>         ]
> 
>         try:
>             procedural_memory = self.llm.generate_response(messages=parsed_messages)
>             procedural_memory = remove_code_blocks(procedural_memory)
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



Revision admission: caller requests summary and supplies messages; CMP-1 proposes text under OBJ-6; code admits nonempty generated content. Empty/model-failed output is rejected, but no preservation oracle is supplied. Persistence is across subsequent library invocations subject to configured store lifetime, scope and RTE-5. Default guidance describes same-task continuation; custom guidance and caller scheduling prevent an exhaustive task horizon/timing classification. The summary is input/outcome context, not necessarily a theory. For any theory a supplied history contains, localized content, consumption as a theory, formulated criticism and retained iteration are uninspected; mere summarization establishes none of them. No observed improved capacity or criticism-driven learning is established.

#### RTE-4 — requested retrieval

Implementation conclusion status: wired. Consumer role: application code requesting memories for its assistant, documented in SRC-2 `README.md:209-222`; actual host generation is excluded. Search/get/get_all implement SDK returns (BAP-2). Search embeds and lemmatizes the query, extracts query entities, retrieves semantic and keyword pools of `max(top_k*4, 60)`, computes entity boosts and ranks semantic candidates. Default result budget is 20, default semantic threshold 0.1. Keywords and entity matches do not expand the candidate pool beyond semantic results. Up to the first eight query entities are considered before deduplication; each entity search requests 500 matches and ignores similarity below 0.5. Shared-entity boost falls with link count. `get` is by ID without expiry suppression; `get_all` is a limited listing, overfetches for expiry filtering and does not guarantee exhaustion. SRC-1 `mem0/memory/main.py:1222-1536,1642-1827`; `mem0/utils/scoring.py:94-139`; `mem0/vector_stores/qdrant.py:573-592`.

Application requesting role — SRC-2 `README.md:209-212`.

> def chat_with_memories(message: str, user_id: str = "default_user") -> str:
>     # Retrieve relevant memories
>     relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
>     memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Candidate gate — SRC-1 `mem0/memory/main.py:1680-1691`.

>         # Step 7: Build candidate set from semantic results
>         candidates = []
>         for mem in semantic_results:
>             payload = mem.payload if hasattr(mem, 'payload') else {}
>             if not show_expired and _payload_is_expired(payload):
>                 continue
>             mem_id = str(mem.id)
>             candidates.append({
>                 "id": mem_id,
>                 "score": mem.score,
>                 "payload": payload,
>             })
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Score gate and combination — SRC-1 `mem0/utils/scoring.py:110-119`.

>         semantic_score = result.get("score") or 0.0
>         if semantic_score < threshold:
>             continue
> 
>         mem_id_str = str(mem_id)
>         bm25_score = bm25_scores.get(mem_id_str, 0.0)
>         entity_boost = entity_boosts.get(mem_id_str, 0.0)
> 
>         raw_combined = semantic_score + bm25_score + entity_boost
>         combined = min(raw_combined / max_possible, 1.0)
> --- `mem0/utils/scoring.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### RTE-5 — explicit maintenance and history

Implementation conclusion status: wired. Caller supplies an ID for update/delete/history, scope IDs for delete_all, or reset for global clearing. Update re-embeds text, preserves creation time and records old/new text; identity metadata cannot be reassigned via update. Deletion removes the live point, preserves old text in history and attempts entity cleanup. Delete_all repeats batches with a repeated-batch guard. Reset drops SQLite tables and resets the main vector collection; it resets the entity collection only when initialized in that process. Entity cleanup likewise returns early if the entity store was not initialized and otherwise treats failures as non-fatal. Thus deletion is not a verified atomic purge of every derivative, and delete_all does not purge the saved-message table. SRC-1 `mem0/memory/main.py:1829-2180`; `mem0/memory/storage.py:326-335`.

Update history — SRC-1 `mem0/memory/main.py:2094-2103`.

>         self.db.add_history(
>             memory_id,
>             prev_value,
>             data,
>             "UPDATE",
>             created_at=new_metadata["created_at"],
>             updated_at=new_metadata["updated_at"],
>             actor_id=new_metadata.get("actor_id"),
>             role=new_metadata.get("role"),
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Delete and retained history — SRC-1 `mem0/memory/main.py:2125-2136`.

>         self.vector_store.delete(vector_id=memory_id)
>         self.db.add_history(
>             memory_id,
>             prev_value,
>             None,
>             "DELETE",
>             created_at=created_at,
>             updated_at=updated_at,
>             actor_id=existing_memory.payload.get("actor_id"),
>             role=existing_memory.payload.get("role"),
>             is_deleted=1,
>         )
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Entity cleanup boundary — SRC-1 `mem0/memory/main.py:660-666`.

>         No-op if the entity store has never been initialized in this process.
>         Errors on individual entities are swallowed at debug level; outer
>         failures are swallowed at warning level so the primary delete/update
>         path is never broken by entity cleanup.
>         """
>         if self._entity_store is None:
>             return
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



Revision admission and recovery: caller proposes text, expiry or deletion and decides whether to invoke; application or human identity is uninspected. Code checks shapes/existence and identity immutability, then effects stores. No epistemic evaluator, supplied answer oracle, automatic candidate comparison or successor-selection experiment is wired in these operations. Old/new history affords inspection, not automatic rollback. Methods and provider capabilities are changed by external deployment/configuration, outside this memory revision boundary. Guidance is fixed CRUD policy and caller text; operation is replacement/removal, with truth and theoretical status uninspected. No theory-builder or improved-capacity inference follows from the ability to edit.

#### RTE-6 — complete retained-context feedback route

Record kind: route. Implementation conclusion status: wired. RTE-1-generated OBJ-1 and RTE-3-generated OBJ-2 both reside in the main vector collection. On a later compatible inferred add, BAP-1 searches that collection using only identity filters and current-message embeddings; it supplies matching text to CMP-1, which may produce further OBJ-1. OBJ-3 also joins this route by exact scope key. There is no memory-type exclusion, expiry check or claim-rationale lookup in this internal retrieval. This establishes later-consumer wiring for both factual and procedural distillation without assuming host adoption. It does not guarantee any particular point is selected. Source evidence: RTE-1's retrieval and input quotations, OBJ-2's shared creation quotation; SRC-1 `mem0/memory/main.py:920-964,2043-2045`.


At CMP-1, BAP-1 is push: on add, code automatically supplies existing memory text and scoped recent messages. SQL equality on the escaped combination of supplied user/agent/run identifiers selects a message branch; recency then chooses up to ten. Embedding similarity selects up to ten main-collection points under identity filters. Previous-message content is truncated to 300 characters per message, while retrieved memory text and current messages have no local total token cap. The prompt builder exposes summary and recently-extracted sections, but RTE-1 does not populate them; they are not evidence of an additional durable profile-summary system. SRC-1 `mem0/memory/main.py:412-419,920-964`; `mem0/configs/prompts.py:965-1045`.

Character budget — SRC-1 `mem0/configs/prompts.py:965-972`.

> PAST_MESSAGE_TRUNCATION_LIMIT = 300
> 
> 
> def _truncate_content(text, limit=PAST_MESSAGE_TRUNCATION_LIMIT):
>     """Truncate text to limit characters, appending '...' when shortened."""
>     if len(text) <= limit:
>         return text
>     return text[:limit] + "..."
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


History formatting — SRC-1 `mem0/configs/prompts.py:987-991`.

>     for msg in messages:
>         role = msg.get("role", "")
>         content = msg.get("message") or msg.get("content", "")
>         if role and content:
>             result += f"{role}: {_truncate_content(content)}\n"
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


At the application caller, BAP-2 is pull. Search/get/get_all fulfill the caller's request; delivery back to that caller is not a second push. README documents an application role, so this is an afforded use route rather than an unspecified hypothetical API consumer. The example does not show a deployed application or justify host activation/benefit within this subsystem result. `chat` itself raises NotImplementedError. History is also requested rather than proactively inserted into a model prompt (SRC-1 `mem0/memory/main.py:1960-1973,2189-2190`).

Library chat boundary — SRC-1 `mem0/memory/main.py:2189-2190`.

>     def chat(self, query):
>         raise NotImplementedError("Chat function not implemented yet.")
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Entity linking supports ranking rather than broad candidate expansion. Search computes semantic, BM25 and entity scores in stages; final candidates come from semantic results only. The semantic threshold applies before score fusion, so a strong lexical/entity match below that threshold cannot rescue a point. `explain=True` adds numeric score components, not model reasoning or semantic provenance. Entity boost computation discounts widely shared entities. This bounds the source claim about multi-signal retrieval without assessing recall quality (RTE-4).

Expiration is a visibility rule for public search/get_all. The current date comparison considers dates strictly earlier than today's UTC date expired. show_expired can reveal them; get-by-ID and internal extraction retrieval do not apply this suppression. Expiry therefore does not establish global invalidation or forgetting, and an expired point can still be delivered through BAP-1. SRC-1 `mem0/memory/main.py:442-451,920-964,1232-1267,1367-1389,1680-1685`.

Expiry predicate evidence is retained on RTE-4.


Scope metadata routes selections but is not deployed authentication. Add requires an identity and strips identity fields from caller metadata; update keeps identity fields immutable through that metadata path. In contrast, get/update/delete accept a memory ID without principal authentication at this layer, and Qdrant wildcard filters skip that field. This prevents interpreting user/agent/run labels as verified tenant authorization. Server/auth is excluded, so this is not an assessment of server security. SRC-1 `mem0/memory/main.py:143-162,360-397,1222-1233,1829-1881,1883-1896`; `mem0/vector_stores/qdrant.py:280-289`.

Scope immutability helper — SRC-1 `mem0/memory/main.py:156-162`.

>     clean = {}
>     for key, value in metadata.items():
>         if key not in _IDENTITY_KEYS:
>             clean[key] = value
>         elif value != existing_payload.get(key):
>             logger.warning(f"{context}: ignoring metadata['{key}'] - identity fields cannot be set through metadata")
>     return clean
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Wildcard is not identity enforcement — SRC-1 `mem0/vector_stores/qdrant.py:280-284`.

>         if not isinstance(value, dict):
>             if value == "*":
>                 # Wildcard: match any value. Qdrant has no direct "field exists"
>                 # condition via FieldCondition, so we skip this filter (match all).
>                 return None
> --- `mem0/vector_stores/qdrant.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


NLP and sparse encoding have inspected degradation branches: missing spaCy returns no entities and leaves text unlemmatized; missing fastembed or BM25 slot disables keyword search. Entity cleanup and search can fail without aborting the primary route. These are conditional capabilities, not evidence that every installation uses all signals. No runtime was executed to determine a deployment's active branch. SRC-1 `mem0/utils/entity_extraction.py:751-772`; `mem0/utils/lemmatization.py:28-32`; `mem0/utils/spacy_models.py:44-91`; `mem0/vector_stores/qdrant.py:93-109,137-152,466-484`.

No NLP entity fallback — SRC-1 `mem0/utils/entity_extraction.py:755-758`.

>     nlp = get_nlp_full()
>     if nlp is None:
>         return []
>     return _extract_entities_from_doc(nlp(text))
> --- `mem0/utils/entity_extraction.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


No keyword fallback — SRC-1 `mem0/vector_stores/qdrant.py:466-470`.

>         if not self._has_bm25_slot:
>             return None
>         sparse_query = self._encode_bm25(query)
>         if sparse_query is None:
>             return None
> --- `mem0/vector_stores/qdrant.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

This record names the later-consumer composition of existing operations, not a separately scheduled loop. Owner is Memory.add; it terminates in that call's extraction prompt and return. Store scopes and retrieval predicates determine later visibility; no worker delegation is owned here. Material admitted after read-back is governed by RTE-1, so there is no second revision mechanism to count.
### Claims

#### CLM-1 — personalization and continuous learning

Claim conclusion status: claimed. README characterizes memory as adapting over time. RTE-1, RTE-3 and RTE-6 support durable trace-derived contextual reuse, not verified personalization benefit or changes to model weights. SRC-2 `README.md:71-79`.

Source learning claim — SRC-2 `README.md:73-73`.

> [Mem0](https://mem0.ai) ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. It remembers user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and autonomous systems.
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### CLM-2 — algorithm and performance claims

Claim conclusion status: claimed. The README explicitly assigns benchmark numbers to the managed platform, which is excluded. Its ADD-only claim is consistent with RTE-1. Its temporal-reasoning claim cannot be inherited wholesale by OSS: scoped methods reject explicit timestamp/reference_date, while expiry filtering and default prompt date text remain distinct mechanisms. SRC-2 `README.md:45-63`; SRC-1 `mem0/memory/main.py:817-829,1446-1447`; `mem0/configs/prompts.py:1007-1013,1033-1042`.

Performance boundary — SRC-2 `README.md:54-54`.

> All benchmarks run on the same production-representative model stack. Single-pass retrieval (one call, no agentic loops) at a top_200 retrieval budget. Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### Evidenced absences

#### ABS-1 — no retained recall-dependence execution evidence

Record kind: bounded absence. Conclusion status: absent. The commissioned evidence is frozen code and README, and no probe was run. None of the inspected implementation, prompt instructions, or README benchmark descriptions supplies a retained execution testing dependence on recalled content for these synchronous routes. This prevents `faithfulness_tested=yes`; it does not establish product-wide absence of tests or evaluation. The procedural preservation instruction and managed-platform benchmark qualification above are the relevant source anchors (SRC-1 `mem0/configs/prompts.py:327-359`; SRC-2 `README.md:45-63`).
Search boundary: source-register implementation and README paths at the full pin, plus this run's source/probe register. Procedure: inspected all supplied evidence layers for a retained execution with an intervention or dependence test; none is registered. No repository-wide text-search absence is asserted. Test files and uninspected benchmark repositories are outside this claim. The absence concerns available execution evidence only.
### Behavioral-authority paths

#### BAP-1 — retained context supplied to the extractor

Implementation conclusion status: wired. RTE-1 automatically selects OBJ-1/OBJ-2 text and OBJ-3 messages, then supplies them to CMP-1 as a user-message prompt. The extractor has not requested memory; the host's add call is the trigger for this push. Existing memories are meant to guide duplicate avoidance/linking, and recent messages resolve references. Scope matching and dense similarity are selectors. The count limits are budgets, not evidence of token-budget optimization. This is delivery into an extraction-model request, not observed dependence of its output. SRC-1 `mem0/memory/main.py:920-964`; `mem0/configs/prompts.py:506-521,965-997,1035-1045`.

Consumer use of retained facts — SRC-1 `mem0/configs/prompts.py:511-511`.

> Use these ONLY for deduplication and linking — do NOT extract new memories from Existing Memories. Your extractions must come exclusively from New Messages. If new information in New Messages is semantically equivalent to an Existing Memory with no meaningful new context, skip it.
> --- `mem0/configs/prompts.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Message identity match — SRC-1 `mem0/memory/storage.py:304-312`.

>                 SELECT role, content, name, created_at FROM (
>                     SELECT role, content, name, created_at
>                     FROM messages
>                     WHERE session_scope = ?
>                     ORDER BY created_at DESC
>                     LIMIT ?
>                 ) ORDER BY created_at ASC
>             """,
>                 (session_scope, limit),
> --- `mem0/memory/storage.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



#### BAP-2 — requested SDK return

Implementation conclusion status: wired. External consumer route conclusion status: afforded. The documented application caller requests relevant memories; the SDK returns data. Neither copying text to a return dictionary nor the mere existence of `get` establishes automatic host prompt insertion. README's application example affords a further route but is not treated as a deployed or scoped runtime component. SRC-1 `mem0/memory/main.py:1250-1267,1536-1536,1715-1745`; SRC-2 `README.md:209-222`.

Requested result — SRC-1 `mem0/memory/main.py:1536-1536`.

>         return {"results": original_memories}
> --- `mem0/memory/main.py` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



## Runtime account

An application principal constructs Memory with model, embedder, Qdrant and SQLite configuration. It supplies user/agent/run identifiers and conversation content. Synchronous code owns the progression through RTE-1, CMP-2, CMP-1 and storage; the model proposes text and the code decides structural admission. RTE-1 returns confirmed ADD records or errors. The application owns retry, next invocation, credentials, and use of results. No terminal assistant answer or delegated worker loop is produced by this subsystem. Configured provider/store credentials are the grant set; operating-system/network isolation and authenticated principals are uninspected.

| route | immediate return and next-step owner | later read-back and selector | delegated visibility | invalidation/expiry | activation/effect and recovery limits |
|---|---|---|---|---|---|
| RTE-1 | ADD entries; synchronous Memory code and caller | RTE-6 scope + nearest-memory context; RTE-4 requested reads | no owned delegate; configured services see supplied content | memory deletion via RTE-5; rolling messages evict; expiry not checked internally | vector/history/entity effects wired; model dependence unobserved; per-record fallback, partial stores possible |
| RTE-2 | per-message ADD entries; code then caller | same retained collection via RTE-6/RTE-4 | same external-service boundary | RTE-5/route-specific expiry | direct import, no extraction or initial entity/message-context write; partial progress possible |
| RTE-3 | summary ADD; model/code then caller | same collection permits RTE-6 selection and RTE-4 request | supplied history sent to model, no continuation worker | RTE-5/route-specific expiry | summary fidelity uninspected; empty output rejected; no cross-store rollback |
| RTE-4 | selected records to requesting caller | the route itself is requested read-back; identity, ID or semantic selector by method | external caller use uninspected | search/get_all suppress expiry unless overridden; get does not | ranking wired, host benefit uninspected; optional rerank excluded; NLP/sparse fallback may reduce signals |
| RTE-5 | success message, history rows, or reset completion; caller owns next action | later callers see revised/deleted points; history requested separately | no owned delegates | deletion preserves history/messages; reset entity cleanup depends on initialization | explicit effects wired; no global purge or transaction guarantee |
| RTE-6 | extraction-context assembly returns into RTE-1 | exact scoped latest messages plus top-ten nearest main points | CMP-1 receives selected text; no host inheritance asserted | no memory-type/expiry exclusion; rolling history count bound | delivery wired; causal output dependence unobserved; parent RTE-1 handles failures |

Four static forcing cases distinguish the guarantees. First, inferred add appends facts, while raw/procedural dispatch and explicit CRUD have different admission rules; ADD-only is a route property. Second, successful vector persistence can precede failed history/entity work; best-effort repair and fallbacks are not a distributed transaction. Third, expired text hidden from search can still enter get or extraction context; this policy is not universal withdrawal. Fourth, scope metadata constrains selected operations but ID-only APIs and wildcard filters prevent treating library scoping as authenticated tenant isolation. Each follows SRC-1 and the quoted routes, not a failed dynamic test.

Guarantee ownership is local: code enforces structural input checks, subset hash rejection and search predicates as invariants of covered methods, subject to external store/client contracts. Prompted fidelity and semantic duplicate avoidance are policies interpreted by CMP-1; no compliance guarantee is observed. Persistence across invocations requires the same configured durable stores and usable identifiers. No distributed transaction or deployment isolation guarantee is claimed.

Operation serves open caller requests. No bounded experiment/curriculum controller or answer oracle is supplied by these API paths. Current transcript content is source input, not a correct-answer reference. Model candidate generation and code admission are computational; caller scheduling, custom guidance, text edits and deployment changes may be computational or human and remain uninspected. Roles are described without assigning an autonomy grade.

Execution disposition: **no dynamic check planned**. Considered provider extraction fidelity, recalled-context dependence and cross-store fault injection. Static inspection establishes the claimed branches and wiring; runtime interventions would require model/service fixtures and a different evidence horizon. No target behavior was executed, so no probe evidence capsule or observed/causal result is asserted.

## Lens scoping

### Memory/context scope

Full depth. Trigger evidence SRC-1 RTE-1, RTE-3 and RTE-6 and SRC-2 CLM-1; retained OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-5 and OBJ-7 determine the system's work. The frozen specialist input fixed this synchronous OSS boundary, including all write alternatives and degraded NLP/sparse paths. OBJ-6 is static guidance, not memory accumulated through use. The specialist independently inspected the sources; source/identity checks do not certify semantics.

### Epistemic scope

Full depth at the same boundary, executed locally using analyse-external-system-epistemic-architecture.md. SRC-1 RTE-1, RTE-2, RTE-3 and RTE-5 produce or change truth-apt text; RTE-4 and RTE-6 govern exposure and reliance. CLM-1 makes learning relevant. Objects and components keep their canonical identities. Host answer warrant, managed-service acceptance/benchmarks, alternate providers and opaque model reasoning are unassessed; their exclusion prevents system-complete epistemic judgments.

## Lens outputs

### Memory/context lens

The specialist inventory is integrated in the canonical records and frontmatter. Both conversation-derived facts and procedural summaries have a complete internal retained-to-later-extractor route (RTE-1, RTE-3, RTE-6); an excluded host is not needed to establish wiring. Raw message storage alone is not trace learning. Read-back is automatic push to CMP-1 and afforded requested pull to the application. Push uses exact scope selection for OBJ-3 and inferred-embedding selection for main-collection text. Requested lexical/entity ranking is not another push signal.

The profile deliberately includes dense encodings and symbolic operative metadata, so representational and distilled forms include natural-language, parametric and symbolic. It does not imply model-weight training. Physical files behind Qdrant/SQLite do not become independently consumed file memories. Entity links support ranking; the library has no graph-store route in this boundary. Curation covers entity deduplication, explicit revisions/withdrawal, rolling eviction and reset; ordinary acquisition is not consolidation. Learning task horizon and timing remain not-determinable across generic/custom branches. No executed recalled-content faithfulness evidence supports yes (ABS-1).

Rationale may survive as text in a fact or procedural summary, but is neither required as a separate dependency nor checked. Delivery does not establish activation, faithful summarization, personalized answers, criticism-driven learning or the advertised managed-platform performance.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 and SRC-2, CLM-1 and CLM-2. Question: which inspected transformations, checks and admission routes license reliance on retained content? Assessed families are RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 and RTE-6; all excluded families and prevented conclusions are in Boundary and evidence. Implementation supplies architectural status, not observed candidate state.

#### 2. Epistemic-object inventory

| object | epistemic annotation; generic identity is canonical-owned | source/limit |
|---|---|---|
| OBJ-1 | raw text is acquired; generated facts may preserve, interpret or extend source meaning; truth-apt content concerns users/agents/conversation | RTE-1, RTE-2; source truth and semantic preservation uninspected |
| OBJ-2 | intended continuation summary can contain truth-apt action/results assertions and non-truth-apt plans | RTE-3; generative fidelity uninspected |
| OBJ-3 | acquired messages retain statements and instructions with unknown source warrant | RTE-6; truncation/eviction prevents full-history preservation |
| OBJ-4 | compiled mutation record concerns changes, not truth of old/new values | RTE-5; it is not criticism or endorsement |
| OBJ-5 | entity labels/link hypotheses organize retrieval; semantic match does not prove co-reference | RTE-1, RTE-4; selected-model and threshold warrant only |
| OBJ-6 | static policy instructs grounding and preservation; no candidate truth-apt output of its own | RTE-1, RTE-3; compliance unobserved |
| OBJ-7 | access encoding has no separately identified truth-apt proposition; ranking role | RTE-4, RTE-6; no behavioral probe |

#### 3. Authority-route ledger

All rows below have architectural status **implemented**, separate from conclusion status **wired**. No row asserts an observed candidate. Generic endpoint, owner and representations are in the cited canonical records.

| route/function | content/update relation and target | evaluator, activation and operative result | epistemic license | operational/behavioral authority and limit |
|---|---|---|---|---|
| RTE-1 content transformation | indeterminate truth-apt transformation of new messages into OBJ-1 | CMP-1 under OBJ-6 on inferred add; generates text | candidate interpretation only; grounding instruction is not validation | proposal enters admission; CLM-1 benefit unknown |
| RTE-1 check/evidence production | no content change; text shape/embedding/hash novelty | code on candidate batch; skip unavailable/duplicate text | structural eligibility, not truth or faithful entailment | blocks these entries; no independent answer oracle |
| RTE-1 disposition/acceptance | no content change; structural store admission | code and vector store; confirmed insert selected for result | operational acceptance only, not epistemic acceptance | retains/adds data; BAP-1 later advisory exposure |
| RTE-1 retention | no content change to admitted text; OBJ-1, OBJ-3, OBJ-4, OBJ-5 | stores after generation; history/entities best effort | persistence records no endorsement | enables RTE-6/RTE-4; no global atomicity |
| RTE-2 content transformation | acquisition/import of supplied OBJ-1 | caller selection, structural filtering | source warrant unknown | direct memory insertion; no semantic evaluator |
| RTE-2 retention | no content change | embedding/store helper on accepted message | no additional warrant | later RTE-6/RTE-4, history retained |
| RTE-3 content transformation | indeterminate truth-apt reshaping of supplied action history | CMP-1 under default/custom OBJ-6 | requested preservation, not checked preservation | proposal becomes OBJ-2; host continuation uninspected |
| RTE-3 disposition/acceptance | no content change; nonempty summary target | code checks nonempty output | structural acceptance only | allows durable write; no fidelity oracle |
| RTE-3 retention | no content change | common storage helper | no additional warrant | makes summary eligible for RTE-6, not verified lifecycle integration |
| RTE-4 operational admission/selection/consumption | no content change; candidate exposures | semantic threshold then combined rank on requested search; ID/list alternatives | relevance ordering, not truth | BAP-2 advisory data to requester, horizon one return |
| RTE-5 content transformation | imported caller revision or non-truth-apt expiry/deletion policy | caller supplies replacement; code applies existence/identity checks | caller warrant unknown | live payload replacement/removal; no learned-method claim |
| RTE-5 lineage/freshness/recovery | no endorsement; mutation histories and cleanup | store calls, explicit reset and history request | auditability of reported changes, not global rollback | old text survives deletion; scope/expiry not universal erasure |
| RTE-6 operational admission/selection/consumption | no content change apart from formatting/truncation | automatic scoped/semantic selectors on later add | contextual relevance only | BAP-1 user-channel knowledge/learning input to CMP-1, horizon current extraction |

No lifecycle-integration row is asserted: none of these data-retention transitions follows an evidenced epistemic acceptance of an ampliative candidate. Operational acceptance is kept separate.

#### 4. Per-object lifecycle disposition

For OBJ-1 via RTE-1: transformation indeterminate. Preservation, contextual interpretation and ampliative conjecture remain possible; source-role attribution is retained without a per-fact source-message lineage. Implemented checks test shape, embedding availability and hash novelty, not entailment. Resolving classification requires paired input/output instances and a semantic fidelity or entailment assessment. Raw RTE-2 and caller replacements RTE-5 are acquisition/import; discovery lifecycle not applicable to those acquisition edges, source truth unknown.

For OBJ-2 via RTE-3: transformation indeterminate between intended non-ampliative summary and unsupported additions/omissions. Explicit preservation instructions and empty-output admission are implemented; no candidate instance is observed. Testing actual preservation requires source histories and produced summaries. No premise warrant or accepted ampliative output is inferred.

For OBJ-3 via RTE-1/RTE-6: acquisition plus non-ampliative formatting/truncation; discovery lifecycle not applicable. Imported statements may be untrue; limited window and character budget lose content. OBJ-4 via RTE-5: compiled record of API effects, discovery lifecycle not applicable; completeness depends on non-atomic storage calls. OBJ-5 via RTE-1/RTE-4: entity grouping/co-reference classification is indeterminate where semantic matching merges entities; threshold is a retrieval heuristic, not a truth test. Candidate-linked execution evidence is needed to distinguish correct identity grouping from mistaken grouping.

No lifecycle record for OBJ-6: no candidate truth-apt output for this object; relevant update routes are static caller/deployment configuration outside learned memory. No lifecycle record for OBJ-7: no individuated candidate truth-apt output; RTE-4 and RTE-6 use access representations. Across all inspected generation, check, retention and use phases, observed candidate state is **no instance observed**. No ampliation is established well enough to fabricate a conjecture/test/acceptance lifecycle from static model calls.

#### 5. System-claim versus route comparison

| claim | doctrine/design support | implementation | observed/causal support | bounded result and unknown |
|---|---|---|---|---|
| CLM-1 | SRC-2 personalizing/continuous-learning description | RTE-1, RTE-3, RTE-6 retain and reuse derived context | none within boundary | contextual adaptation wiring supported; improved future capacity and faithful personalization uninspected |
| CLM-2 | SRC-2 ADD-only, multi-signal and managed performance claims | RTE-1 append path; RTE-4 conditional score fusion | no benchmark trace or intervention here | OSS wiring supported with semantic candidate restriction; platform scores cannot establish OSS benefit or component causality |

#### 6. Bounded conclusion

These routes acquire and reshape content, grant structural admission and retrieval exposure, and let old memory guide new extraction. They do not supply an independently warranted truth-acceptance transition. This is an intentional memory-service responsibility horizon, not a requirement that memory software become a general theory builder. Model interpretation, source truth and later host reliance remain separate unresolved questions.

## Reconciliation

The independent specialist's input, source pin, method hash, complete status and report digest match this run. The coordinator's runtime/epistemic baseline preceded the report and used pinned sources; agreement about ADD-only append, conditional retrieval, partial persistence and host boundary was independently reached. No source-only independence claim is made for conclusions learned from the specialist.

| specialist proposal | canonical registration | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-7 | accepted as retained dense/sparse encodings, separate from display text |
| MEM-RTE-1 | RTE-6 | accepted as composed later-extractor route, no independent scheduler or duplicate admission mechanism |
| MEM-ABS-1 | ABS-1 | accepted only for missing retained recall-dependence execution evidence in this analysis |

All other supplied canonical IDs retain their referents. Integration issues 4–10 are adopted: RTE-1 appends and does not retain model-proposed fact-to-fact links; RTE-2/RTE-3 initially skip saved messages/entity linking and procedural dispatch has priority; BAP-1 push and BAP-2 pull keep host activation excluded; expiry/deletion/reset remain distinct and non-atomic; RTE-4 uses semantic-only candidates with finite budgets and degraded branches; learning horizon/timing stay not-determinable; distilled_form includes actual operative compiled/vector outputs of qualifying chains. This broad form reading agrees with the registered representational-form definition and does not assert trained weights. No substantive conflict remains. The epistemic lens cites these records without rewriting memory classifications.

## Bounded synthesis

Mem0's inspected synchronous OSS library converts caller messages into appended factual memories, optionally generates execution-history summaries, and exposes retained material through requested retrieval and automatic context for later extraction. Its control loop ends at API results. The internal feedback route is concrete: future inferred adds select old text and scoped recent messages for CMP-1. It does not require assuming an enclosing agent actually adopts a returned result.

Three mechanisms determine its practical behavior. The inferred write path has one model extraction call followed by structural and bounded exact-text filtering; explicit edits and raw/procedural routes have different admission policies. Search ranks semantic candidates with optional lexical/entity contributions, so its multi-signal design is not a union of independent candidate pools. Persistence spans multiple stores, while expiry and deletion affect different readers and retained copies; neither success messages nor scope labels imply global erasure, atomicity or authenticated isolation.

The strongest supported learning contribution is automatic durable trace transformation with later contextual reuse (wired, under the comparison axis's narrow definition). Improved capacity attributable to criticism of a consumed theory remains uninspected. For the shipped method guidance, theory-builder condition 1 (localized rule content) and condition 2 (consumption) are wired; condition 3 (content-directed criticism) and condition 4 (iteration from criticism) are uninspected. Individual memories are addressable by ID, while assumptions inside prose are not independently governed parts. Persistence can cross API invocations with the same stores; task/project horizons are caller-defined and not fully determined.

Reflection is uninspected: an agent-labeled memory is not an evidenced two-way self-representation of this memory system. Autonomous theory-builder status is uninspected because the complete theory path is not established; computation does perform extraction and structural admission inside the selected boundary. Self-improvement is uninspected: mutable context and editable memory are wired, but no comparison shows an evidence-responsive change improving the system's capacity. These are separate properties, not a maturity grade.

For repeated conversations or task continuation, the architecture supplies durable selected context with finite selection budgets; adequacy and fidelity require execution evidence. A paired recall-dependence intervention could change the activation assessment. Source-linked generation checks and retained criticism with subsequent use could change the epistemic/theory-builder assessment. A broader service inspection would be needed to assess proprietary performance, authentication, temporal retrieval or other product surfaces.

## Limitations

| limitation | affected IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| Static-only evidence | SRC-1, ABS-1, RTE-1, RTE-3, RTE-6 | source paths and quoted calls | observed fidelity, activation or causal benefit | retained input/output runs and controlled dependence tests |
| Opaque component internals/versioning | CMP-1, CMP-2, CMP-4, OBJ-7 | adapters/loaders only | exact deployed weights, trained changes, reliable semantics | pinned component artifacts and probes |
| Excluded host and product branches | BAP-2, CLM-2, CMP-3 | synchronous OSS rerank=False | whole-product claims, hosted performance, host action effects | separately frozen service/host/branch implementation and run evidence |
| Caller-defined task/schedule/custom guidance | RTE-1, RTE-3, RTE-5 | generic open-request API | exhaustive learning scope/timing, human-versus-computational external role | concrete application/task lifecycle |
| Finite selectors and mixed retention | RTE-4, RTE-5, RTE-6, OBJ-3, OBJ-4, OBJ-5 | inspected default store paths | complete recall, transactional mutation or universal erasure | targeted failure/recall tests and full deployed store contracts |
| Source statements and model interpretations unverified | OBJ-1, OBJ-2, OBJ-5 | acquisition/extraction and structural admission | epistemic truth warrant, theory criticism and improvement | candidate-linked source support, formulated criticism and retained successor testing |

## Verification and blockers

### Semantic verification

Checked RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 and RTE-6 against the frozen scope and included alternatives. Both qualifying trace-fed writes carry their own factual/procedural source and default intent; generic/custom branches preserve not-determinable task horizon and timing. Distilled forms include operative outputs, not just display text, and opaque service internals remain excluded. Raw-message retention is not independently counted as trace learning.

Checked push consumer CMP-1, trigger add, exact message scope selector and current-message embedding selector; BAP-2 fulfills a caller request and adds no automatic push. Keyword/entity ranking is confined to requested retrieval. Checked identity and canonical remapping as exact tokens; generic records are unique and overlays refer to them. Every quote remains attached to its supporting canonical record, with no duplicate expiry passage. No observed/causal status is inferred from wiring, and no managed benchmark establishes OSS performance. The source pin, input, report and method hashes match. Known comparison sets and their weaker union bases remain consistent with the specialist report; its uncertainty is preserved. Canonical bounds and source occurrence checks support publication, without claiming automated semantic clearance.

### Deterministic validation

Target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-mem0-01/result.md`. Full deterministic validation passed; quote/source anchors are checked against frozen source by publication preparation. Markdown data changes require no pytest execution.

### Blockers

none
