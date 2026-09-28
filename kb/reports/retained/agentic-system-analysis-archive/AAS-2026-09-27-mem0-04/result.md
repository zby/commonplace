---
type: types/agentic-system-analysis-result.md
description: "Mem0 synchronous OSS memory pipeline: additive extraction, retrieval, and the limits of knowledge and improvement claims"
run-id: AAS-2026-09-27-mem0-04
system: Mem0
run-date: "2026-09-27"
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: subsystem-only
reviewed-boundary: "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd"
analysis-cutoff: "2026-09-27"
evidence-tier: code-grounded
memory-comparison:
  scope: 'Synchronous Python OSS Memory: accumulated raw/extracted/procedural payloads,
    recent messages, edit history, entity and vector/lexical access structures; add,
    search, manual maintenance and documented caller consumption. Default Qdrant/SQLite
    inspected; optional providers, reranking and vision included as explicit partial
    limits. AsyncMemory and hosted/platform/JS/server/CLI/external runtime implementations
    excluded.'
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
          - OBJ-8
          - OBJ-7
          - OBJ-4
          - CMP-5
          note: Qdrant dense/sparse vectors and payloads store content and entity
            links.
        sqlite:
          basis: wired
          records:
          - OBJ-2
          - OBJ-5
          note: SQLite retains recent messages and edit history.
      records:
      - OBJ-8
      - OBJ-7
      - OBJ-4
      - CMP-5
      - OBJ-2
      - OBJ-5
      note: Default stores are inspected. Configurable non-Qdrant providers and their
        internal persistence are uninspected; their additional substrate values are
        not a complete set.
    representational_form:
      assessment: partial
      values:
      - natural-language
      - symbolic
      evidence:
        natural-language:
          basis: wired
          records:
          - OBJ-8
          - OBJ-7
          - OBJ-2
          - OBJ-3
          note: Text facts, conversation messages and procedural summaries are retained
            and read.
        symbolic:
          basis: wired
          records:
          - OBJ-4
          - OBJ-6
          - OBJ-5
          note: Identity links, numeric vector arrays, hashes and typed history fields
            drive access and maintenance.
      records:
      - OBJ-8
      - OBJ-7
      - OBJ-2
      - OBJ-3
      - OBJ-4
      - OBJ-6
      - OBJ-5
      note: Inspected payloads and access structures are covered; alternate provider
        internals remain opaque. Vector arrays are stored numeric data, not evidence
        that model weights learn.
    lineage:
      assessment: partial
      values:
      - trace-extracted
      - imported
      - authored
      - other-compiled
      evidence:
        trace-extracted:
          basis: wired
          records:
          - RTE-1
          - RTE-3
          note: Conversational facts and procedural summaries are automatically derived
            from supplied traces.
        imported:
          basis: wired
          records:
          - RTE-4
          - OBJ-2
          note: Caller messages are retained as supplied after normalization, including
            raw writes.
        authored:
          basis: afforded
          records:
          - RTE-4
          - RTE-6
          note: Callers can supply authored text and replacements; human use is not
            observed.
        other-compiled:
          basis: wired
          records:
          - RTE-5
          - OBJ-6
          note: Entity links, hashes, lemmas and vector access representations are
            derived from content.
      records:
      - RTE-1
      - RTE-3
      - RTE-4
      - OBJ-2
      - RTE-6
      - RTE-5
      - OBJ-6
      note: Source-to-store paths are inspected; optional provider-side transformations
        are uninspected.
    behavioral_authority:
      assessment: partial
      values:
      - knowledge
      - ranking
      evidence:
        knowledge:
          basis: wired
          records:
          - RTE-1
          - OBJ-8
          - OBJ-7
          - OBJ-2
          note: The extraction LLM receives prior factual text and recent utterances
            as context.
        ranking:
          basis: wired
          records:
          - OBJ-4
          - OBJ-6
          - RTE-2
          note: Entity linkage and vector/lexical representations alter computed retrieval
            order.
      records:
      - RTE-1
      - OBJ-8
      - OBJ-7
      - OBJ-2
      - OBJ-4
      - OBJ-6
      - RTE-2
      note: The documented answer consumer uses recalled facts as knowledge. Optional
        consumers, custom prompt meanings and reranker internals prevent a complete
        authority set; system-role delivery alone does not make facts instructions.
    write_agency:
      assessment: known
      values:
      - automatic
      - manual
      evidence:
        automatic:
          basis: wired
          records:
          - RTE-1
          - RTE-3
          - RTE-5
          note: Triggered APIs automatically extract, embed, index and retain derived
            content.
        manual:
          basis: afforded
          records:
          - RTE-4
          - RTE-6
          note: Raw text insertion and explicit update/delete permit caller-authored
            curation.
      records:
      - RTE-1
      - RTE-3
      - RTE-5
      - RTE-4
      - RTE-6
      note: Both API-driven automatic transformation and manual text/maintenance affordances
        are accounted for; no deployed human activity is claimed.
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
          - RTE-5
          note: Semantic entity matching merges links into an existing retained entity.
        evolve:
          basis: wired
          records:
          - RTE-6
          note: Explicit update replaces an existing payload and logs prior text.
        invalidate:
          basis: wired
          records:
          - RTE-6
          note: Delete removes live payload while retaining a DELETE history record;
            expiry hides selected reads.
        decay:
          basis: wired
          records:
          - OBJ-2
          - RTE-6
          note: SQLite evicts recent-message rows beyond ten and explicit removal
            forgets live content.
      records:
      - RTE-5
      - RTE-6
      - OBJ-2
      note: Automatic primary memory ingestion is ADD-only. Whether model transformations
        synthesize new claims is instance-dependent; optional provider maintenance
        is uninspected. Index construction and exact acquisition duplicate checks
        alone are not counted as dedup.
    read_back_direction:
      assessment: known
      values:
      - pull
      - push
      evidence:
        pull:
          basis: afforded
          records:
          - RTE-2
          - RTE-7
          note: Named caller interfaces and the documented chat consumer request retained
            facts/history.
        push:
          basis: wired
          records:
          - RTE-1
          note: add automatically assembles existing memories and recent messages
            for an extraction LLM that has not requested them.
      records:
      - RTE-2
      - RTE-7
      - RTE-1
      note: API pull and internal extraction-context push are distinct operations.
        README answer assembly is an afforded external route, not an observed deployment.
    read_back_signal:
      assessment: partial
      values:
      - identifier
      - inferred-embedding
      evidence:
        identifier:
          basis: wired
          records:
          - RTE-1
          - OBJ-2
          note: Current scope identifiers select exact recent-message history automatically.
        inferred-embedding:
          basis: wired
          records:
          - RTE-1
          - OBJ-6
          note: Current conversation embedding selects ten prior vector payloads for
            the extraction prompt.
      records:
      - RTE-1
      - OBJ-2
      - OBJ-6
      note: The automatic default extraction selector is covered. Alternate vector-provider
        selection internals remain uninspected; public hybrid retrieval is caller
        pull and adds no push signal by itself.
    trace_learning:
      assessment: known
      values:
      - 'yes'
      evidence:
        'yes':
          basis: wired
          records:
          - RTE-1
          - RTE-3
          - RTE-5
          note: Conversation traces produce durable facts and derived access structures
            consumed by later extraction/retrieval; summaries share the later extraction
            route.
      records:
      - RTE-1
      - RTE-3
      - RTE-5
      note: At least one automatic durable trace-to-later-consumer chain is wired.
        This structural classification asserts no observed improvement or weight training.
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
          - RTE-1
          - RTE-3
          note: Supplied conversation messages feed facts and continuation summaries.
        trajectories:
          basis: afforded
          records:
          - RTE-3
          - OBJ-3
          note: The procedural prompt explicitly expects execution history across
            past steps, including actions and results.
        tool-traces:
          basis: afforded
          records:
          - RTE-3
          - OBJ-3
          note: Procedural guidance explicitly preserves API outputs, errors and browser
            action results when included in caller messages.
      records:
      - RTE-1
      - RTE-3
      - OBJ-3
      note: No actual trace instance is available; optional vision inputs and caller-supplied
        message meanings prevent a complete source taxonomy.
    learning_scope:
      assessment: partial
      values:
      - per-task
      - cross-task
      evidence:
        per-task:
          basis: afforded
          records:
          - RTE-3
          - OBJ-3
          note: Procedural summary guidance names continuation of the current task.
        cross-task:
          basis: afforded
          records:
          - RTE-7
          - CLM-1
          note: User-scoped personalization and the documented repeated-question chat
            retain preferences beyond a single question.
      records:
      - RTE-3
      - OBJ-3
      - RTE-7
      - CLM-1
      note: Durability and IDs alone do not determine task horizons. Generic add calls,
        derived indexes and custom procedural prompts inherit caller task boundaries,
        which are not fixed in this code.
    learning_timing:
      assessment: partial
      values:
      - online
      evidence:
        online:
          basis: wired
          records:
          - RTE-1
          - RTE-3
          - RTE-5
          note: Facts, summaries and indexes are produced in the triggering add call
            for subsequent calls.
      records:
      - RTE-1
      - RTE-3
      - RTE-5
      note: Default transformations execute synchronously in use. Offline submission
        of historical traces and alternate provider processing remain possible but
        unestablished; no complete timing set is claimed.
    distilled_form:
      assessment: partial
      values:
      - natural-language
      - symbolic
      evidence:
        natural-language:
          basis: wired
          records:
          - RTE-1
          - RTE-3
          note: LLM outputs retained facts and procedural text.
        symbolic:
          basis: wired
          records:
          - RTE-5
          - OBJ-6
          note: Automatic trace-derived content is compiled into numeric access vectors
            and entity-to-memory links used by later selection/ranking.
      records:
      - RTE-1
      - RTE-3
      - RTE-5
      - OBJ-6
      note: No inspected weight-update path; opaque providers prevent exhaustive form
        claims. Natural-language summaries are themselves retained content, not displays
        of opaque checkpoints.
    faithfulness_tested:
      assessment: not-determinable
      values: []
      evidence: {}
      records:
      - CLM-1
      - RTE-7
      note: Only source code and doctrine were commissioned; no retained execution
        intervention demonstrates dependence on recalled content. Test code or benchmark
        claims cannot establish yes.
---

# Mem0 agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-04/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/mem0.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-04/memory-report.md`
**Memory analysis report SHA-256:** 6812d1e3a042bb36a6fa21bb1f6eb23d29448866f3d65e6ae432d4231a55172c

Run AAS-2026-09-27-mem0-04 opened 2026-09-27. The fresh specialist read frozen input SHA-256 `b424fa9ae42b1cb926de17d64f0987d0bb0d17c56235fd721cc4c73ba95d5b15`.

## Boundary and evidence

This analysis explains what the synchronous Python OSS `Memory` API retains, how that material reaches later consumers, and what its extraction and admission checks establish. It is a subsystem-only, code-grounded analysis of Mem0 at commit `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`, with applicability cutoff 2026-09-27. It includes inferred and raw additions, procedural summaries, history, entity access structures, hybrid search, optional reranking, and manual maintenance. It distinguishes the documented external chat consumer from the internal extraction consumer.

The managed platform, self-hosted server authentication/dashboard, CLI, JS SDK, and third-party enclosing agents are excluded. Their exclusion prevents conclusions about production platform performance, deployed access isolation, or all integrations. AsyncMemory is identified as a separate execution path, not assumed equivalent. Alternate provider internals and deployed installations are uninspected; the default OpenAI adapter and optional spaCy loader establish call and version boundaries, not actual model behavior. External dependencies are the configured LLM/embedding endpoints, vector-store backend, SQLite, optional NLP package/models and reranker. No dynamic system execution, credentials, environment deployment or candidate-linked trace was used. No prior analysis supplied evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git | `https://github.com/mem0ai/mem0` | 94c3fe9f238f3dbf29c9ce98643bd71eb13077cd | implementation | Synchronous Memory, supporting storage/configuration, default adapters, scoring and entity access; specialist scopes below | `mem0/memory/main.py`, `mem0/memory/storage.py`, `mem0/configs/base.py`, `mem0/llms/openai.py`, `mem0/embeddings/openai.py`, `mem0/utils/scoring.py`, `mem0/utils/entity_extraction.py`, `mem0/utils/spacy_models.py`, `mem0/utils/factory.py`, `mem0/vector_stores/qdrant.py`, `mem0/vector_stores/configs.py`, `mem0/configs/vector_stores/qdrant.py`, `mem0/memory/utils.py` | External model and store internals; no deployment or causal evidence |
| SRC-2 | Git | `https://github.com/mem0ai/mem0` | 94c3fe9f238f3dbf29c9ce98643bd71eb13077cd | doctrine/design | README claims and example consumer; additive and procedural prompts; API descriptions | `README.md`, `mem0/configs/prompts.py`, `mem0/memory/main.py` | Documentation does not establish successful operation or semantic fidelity |

| SRC-3 | Git | `https://github.com/mem0ai/mem0` | 94c3fe9f238f3dbf29c9ce98643bd71eb13077cd | reported operation | README managed-platform benchmark report | `README.md` | Reported scores lack inspected execution or causal design within this boundary |

Operational access root: `/home/zby/llm/commonplace/related-systems/mem0ai--mem0`; origin and full commit were verified. All evidence reads used commit-addressed blobs. Quotations below were generated by `commonplace-quote` against the running state. Local source paths refer to this revision; the source repository and full commit supply durable identity. Source-reading and validation commands are workflow checks, not executions of Mem0.

## Shared records

### Components

### CMP-1 — Configured extraction LLM

Source-native identity: `self.llm`, created by LlmFactory for extraction and procedural summarization. Representational form: distributed-parametric model behind a symbolic Python adapter; storage substrate: external service or configured provider, weights inaccessible here. SRC-1 `mem0/memory/main.py`, `mem0/llms/configs.py`, `mem0/llms/openai.py`. Implementation conclusion status: wired. Parameter changes during operation: uninspected at provider boundary; the inspected adapter issues inference requests, which does not establish provider weight fixity. Exact-version pinning: uninspected for actual deployment; code resolves configurable model names and endpoints, including OpenRouter routing. The default model name is mutable rather than a retained weight digest. Inference requests can carry an optional response callback; its external effects are uninspected. Neither callback nor provider behavior is an isolation guarantee.

> if not self.config.model:
>             self.config.model = "gpt-5-mini"
> --- `mem0/llms/openai.py:39-40` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`
> response = self.client.chat.completions.create(**params)
>         parsed_response = self._parse_response(response, tools)
> --- `mem0/llms/openai.py:141-142` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-2 — Configured embedding model

Source-native identity: `self.embedding_model`; symbolic adapter calls a distributed-parametric embedding endpoint. Storage substrate: provider service; returned vectors are retained access structures, not the model weights. SRC-1 `mem0/embeddings/configs.py`, `mem0/embeddings/openai.py`. Implementation conclusion status: wired. Parameter changes during operation: uninspected inside provider. Exact-version pinning: uninspected in deployment; default name and configurable endpoint do not identify exact weights. It supports candidate selection and text indexing; semantic similarity is not a truth evaluator.

> self.config.model = self.config.model or "text-embedding-3-small"
> --- `mem0/embeddings/openai.py:15-15` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-3 — Optional spaCy model

Source-native identity: `en_core_web_sm`, loaded through `get_nlp_full` and `get_nlp_lemma`. Mixed symbolic extraction and distributed-parametric NLP; storage substrate: installed package/local model files. SRC-1 `mem0/utils/spacy_models.py`, `mem0/utils/entity_extraction.py`, `mem0/utils/lemmatization.py`. Implementation conclusion status: wired, conditional on availability. Loader can download the named model if missing and caches failure; entity extraction returns no entities and lemmatization returns the input text when unavailable. Parameter changes during operation: uninspected within loaded model; the inspected loader exposes load/inference, not training. Exact-version pinning: uninspected for installed package; the name-only download does not supply a fixed model digest. These fallbacks limit claims that every deployment uses all retrieval signals.

> _nlp_full = spacy.load("en_core_web_sm")
> --- `mem0/utils/spacy_models.py:60-60` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`
> download("en_core_web_sm")
> --- `mem0/utils/spacy_models.py:35-35` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-4 — Optional configured reranker

Source-native identity: `self.reranker`, factory-created when configured and called only when `rerank` is true and results exist. Representational form and storage substrate: uninspected provider internals, potentially distributed-parametric; symbolic invocation is wired. SRC-1 `mem0/memory/main.py`, `mem0/utils/factory.py`. Parameter changes and exact-version pinning: uninspected, preventing uniform fixity claims over optional rerankers. Failure retains original ranked results, so reranking is a conditional best-effort enhancement.

> if rerank and self.reranker and original_memories:
>             try:
>                 reranked_memories = self.reranker.rerank(query, original_memories, limit)
>                 original_memories = reranked_memories
>             except Exception as e:
>                 logger.warning(f"Reranking failed, using original results: {e}")
> --- `mem0/memory/main.py:1514-1519` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CMP-5 — Configured memory persistence and model dependencies

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Source-native identity: `Memory.vector_store`, `Memory.db`, `Memory.llm`, `Memory.embedding_model`, optional `Memory.reranker`. Implementation conclusion status: wired. Default vector provider is Qdrant; default history is `~/.mem0/history.db` unless `MEM0_DIR` or configuration changes it. Qdrant configuration uses collection `mem0` and local path `/tmp/qdrant` by default, with supplied client/host/url alternatives. Memory and entity collections use the same configured provider. The storage classification counts the vector and SQLite interfaces; it does not separately count implementation files as a memory file system. Remote deployment and non-Qdrant internals are uninspected.

Default LLM and embedder providers are OpenAI, but hosted model parameter internals, immutable endpoint versions and parameter changes are uninspected. An embedding output is a stored numeric representation; it is not evidence that the embedding model learns from use. Optional reranker behavior is bounded by the wrapper in RTE-2.

Evidence: SRC-1, `Memory.__init__`, `Memory.entity_store`, provider configs, and the Qdrant constructor.

> class VectorStoreConfig(BaseModel):
>     provider: str = Field(
>         description="Provider of the vector store (e.g., 'qdrant', 'chroma', 'upstash_vector')",
>         default="qdrant",
>     )
>     config: Optional[Dict] = Field(description="Configuration for the specific vector store", default=None)
> 
>     _provider_configs: Dict[str, str] = {
>         "qdrant": "QdrantConfig",
>         "chroma": "ChromaDbConfig",
>         "pgvector": "PGVectorConfig",
>         "pinecone": "PineconeConfig",
>         "mongodb": "MongoDBConfig",
> --- `mem0/vector_stores/configs.py:6-18` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> history_db_path: str = Field(
>         description="Path to the history database",
>         default=os.path.join(mem0_dir, "history.db"),
>     )
>     reranker: Optional[RerankerConfig] = Field(
>         description="Configuration for the reranker",
>         default=None,
>     )
> --- `mem0/configs/base.py:42-49` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Assembly relation: model constituents are CMP-1, CMP-2 and CMP-4, not additional independently counted models. This record supplies the configured persistence interfaces. Representation is mixed symbolic adapter/configuration and constituent distributed-parametric dependencies; storage is the configured vector provider and SQLite. Exact model pinning and parameter-change limits remain on the constituent records.


### Operative objects

### OBJ-1 — Superseded raw/extracted memory aggregate

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Parent referent preserved as a superseded aggregate: all raw or extracted general-memory text payloads in the configured vector store. This record originally combined automatic extraction and direct supplied text. The replacement operative records are OBJ-8 (extracted text) and OBJ-7 (raw supplied text), whose producers, guidance, admission and semantic warrant differ. The aggregate's identity is retained for reconciliation, not reused for either part. Procedural subtype OBJ-3 remains separately described. Supporting source mechanisms are RTE-1 and RTE-4; maintenance and reads cover both parts.


### OBJ-2 — Bounded recent-message rows

Evidence anchor: SRC-1, `mem0/memory/storage.py`.

Parent referent preserved: SQLite `messages` rows selected by `session_scope`. Retained fields are id, scope, role, content, name and creation time; natural-language utterances in symbolic rows. Lineage: imported conversation after input/vision normalization, not automatically distilled memory. Source-native selector: escaped, sorted concatenation of supplied user/agent/run identifiers. The producer RTE-1 saves messages after normal completion, empty extraction, no accepted records, and failed-all-insert handling. An early LLM failure raises before save. Raw and procedural branches return without this save route.

Later consumer is RTE-1's extraction LLM: the SQLite selector requests at most ten rows for the exact scope and returns them chronologically. Automatic delivery is identifier-targeted push, not a hypothetical caller. Save evicts all but the most recent ten rows in that scope; no stable tie breaker for equal timestamps is specified in the inspected SQL. Scope IDs do not prove a task boundary. Authority: contextual knowledge for reference resolution. Reasons are not separate from the retained utterances, and full source history does not persist here. Evidence: SRC-1, `storage.py` and `_build_session_scope`.

> ),
>                     )
>                 # Evict old messages beyond the most recent 10 for this scope.
>                 # Wrapped in a derived table to force SQLite to materialize the
>                 # ORDER BY before the outer NOT IN evaluates it.
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
>                 self.connection.execute("COMMIT")
>             except Exception as e:
>                 self.connection.execute("ROLLBACK")
>                 logger.error(f"Failed to save messages: {e}")
>                 raise
> 
>     def get_last_messages(self, session_scope: str, limit: int = 10) -> List[Dict[str, Any]]:
>         with self._lock:
>             # Subquery picks the latest N rows (DESC + LIMIT), outer query
>             # re-sorts them chronologically (ASC) for the caller.
>             cur = self.connection.execute(
>                 """
>                 SELECT role, content, name, created_at FROM (
>                     SELECT role, content, name, created_at
>                     FROM messages
>                     WHERE session_scope = ?
>                     ORDER BY created_at DESC
>                     LIMIT ?
>                 ) ORDER BY created_at ASC
>             """,
>                 (session_scope, limit),
>             )
>             rows = cur.fetchall()
> --- `mem0/memory/storage.py:277-314` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-3 — Procedural continuation text

Evidence anchor: SRC-2, `mem0/configs/prompts.py`.

Object, source-native `procedural_memory`, with payload `memory_type: procedural_memory`. Storage is the same configured vector collection via `_create_memory`. Form: natural-language summary plus symbolic metadata/access structures; lineage: automatically trace-extracted. Producer RTE-3 takes caller-supplied conversation/execution history and returns a new UUID and ADD event. The prompt asks for task objective, progress, sequential actions, exact action results, findings, errors and next context. It describes continuation of the current task, not necessarily reusable skill induction.

Its guidance asks to preserve reasons/context in prose where supplied, but no separate durable raw trace, structured rationale, proof of verbatim preservation or adequacy check is wired by RTE-3. Later RTE-1 can select this object as ordinary prior text; RTE-2 can return it to a caller, including by metadata filters. The former knowledge channel is wired; a continuation agent is only afforded. No continuation-specific automatic checkpoint restoration or instruction activation is established. Custom prompts can change the summary's semantics and horizon.

Evidence: SRC-2, procedural prompt; implementation retained on RTE-3.

> PROCEDURAL_MEMORY_SYSTEM_PROMPT = """
> You are a memory summarization system that records and preserves the complete interaction history between a human and an AI agent. You are provided with the agent’s execution history over the past N steps. Your task is to produce a comprehensive summary of the agent's output history that contains every detail necessary for the agent to continue the task without ambiguity. **Every output produced by the agent must be recorded verbatim as part of the summary.**
> --- `mem0/configs/prompts.py:326-327` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> 1. **Agent Action**:
>      - Precisely describe what the agent did (e.g., "Clicked on the 'Blog' link", "Called API to fetch content", "Scraped page data").
>      - Include all parameters, target elements, or methods involved.
> 
>   2. **Action Result (Mandatory, Unmodified)**:
>      - Immediately follow the agent action with its exact, unaltered output.
>      - Record all returned data, responses, HTML snippets, JSON content, or error messages exactly as received. This is critical for constructing the final output later.
> --- `mem0/configs/prompts.py:337-343` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-4 — Entity rows and linked-memory index

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Object, source-native entity collection (`<collection>_entities` for Qdrant), payload `data`, `entity_type`, `linked_memory_ids` and scope IDs, with embedding vector. Form: natural-language entity text plus symbolic types/IDs/vectors; lineage: other-compiled from memory content, ultimately trace-derived on inferred ingestion. This is an access index, not evidence of a separate graph database or truth-apt relations between world entities.

The producer RTE-5 extracts entities from successfully persisted facts and merges identical/near entity descriptions. Consumer RTE-2 uses linked IDs to boost candidate memory scores after semantic matching against query entities. Authority: ranking, not factual validation. Rows can survive across calls with the collection; cleanup is best-effort and process-initialization dependent. Reasons for an entity merge are not retained as criticism or later read-back evidence. Evidence: SRC-1, entity collection property and linking/boost code.

> payload = match.payload if hasattr(match, 'payload') else {}
>                         linked_memory_ids = payload.get("linked_memory_ids", [])
>                         if not isinstance(linked_memory_ids, list):
>                             continue
> 
>                         num_linked = max(len(linked_memory_ids), 1)
>                         memory_count_weight = 1.0 / (1.0 + 0.001 * ((num_linked - 1) ** 2))
>                         boost = similarity * ENTITY_BOOST_WEIGHT * memory_count_weight
> 
>                         for memory_id in linked_memory_ids:
>                             if memory_id:
>                                 memory_key = str(memory_id)
>                                 memory_boosts[memory_key] = max(memory_boosts.get(memory_key, 0.0), boost)
> --- `mem0/memory/main.py:1810-1822` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-5 — Memory edit-history rows

Evidence anchor: SRC-1, `mem0/memory/storage.py`.

Object, source-native SQLite `history`, retains memory ID, old/new text, event, timestamps, deletion flag and optional actor/role. Form: natural-language before/after text in symbolic event rows; lineage: imported retained operation records. Producers RTE-1, RTE-4, RTE-3 and RTE-6 record ADD/UPDATE/DELETE. Later `history(memory_id)` provides caller pull; no automatic extraction of this edit history is established in the inspected synchronous routes.

The object supports inspection of past text but is not a transaction journal that automatically rolls back the vector store. History failure can follow a successful vector mutation; add has best-effort history fallbacks. No criterion, factual reason or critical judgment is required. Retention extends until database reset or external removal; deletion of a live vector retains its old text here. Evidence: SRC-1, `SQLiteManager` history schema, `Memory.history`, and the history write quoted under RTE-6.


### OBJ-6 — Dense/lexical access representations and metadata

Evidence anchor: SRC-1, `mem0/vector_stores/qdrant.py`.

Operative object separating access representations from the readable content of OBJ-8 and OBJ-7: dense embeddings; Qdrant optional named sparse `bm25` vectors; `text_lemmatized`; content hashes; IDs, scopes and expiry dates. Form: symbolic numeric arrays, token text and fields; lineage: other-compiled. No learned parameter artifact is demonstrated. Producer: every content write computes embeddings, hash and lemmas; Qdrant insert/update conditionally computes sparse vectors. Consumer: RTE-1 and RTE-2 search selectors plus duplicate and expiry checks.

Authority: ranking/selection at retrieval, with hash used for exact duplicate admission. Raw/procedural entries get these fields even though they bypass batch entity linking. BM25 requires a compatible collection slot and available encoder; failures disable the sparse signal. Lemmatization falls back to original text when spaCy is unavailable. Embedding model semantics and alternate provider encodings remain uninspected. Evidence: SRC-1, `_create_memory`, Qdrant insert, lemmatization and scoring.

> payload = payloads[idx] if payloads else {}
>             point_id = idx if ids is None else ids[idx]
> 
>             # Build named vectors: dense + optional BM25 sparse (only if collection has the slot).
>             named_vectors = {"": vector}
>             if self._has_bm25_slot and bm25_sparse_vectors[idx] is not None:
>                 named_vectors["bm25"] = bm25_sparse_vectors[idx]
> 
>             points.append(PointStruct(id=point_id, vector=named_vectors, payload=payload))
> 
>         self.client.upsert(collection_name=self.collection_name, points=points)
> --- `mem0/vector_stores/qdrant.py:236-246` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-7 — Raw supplied message payloads

Evidence anchor: SRC-1, `mem0/memory/main.py` and `mem0/memory/utils.py`.

Operative object replacing the raw portion of superseded OBJ-1. Source-native identity: payload `data` with role, optional actor_id, UUID, hash, timestamps and caller identity/metadata. Form: supplied natural-language text with symbolic metadata; access structures remain OBJ-6. Storage: same configured vector collection. Lineage: imported, or authored where caller composes the text; trace-derived semantic extraction is not performed by this branch. Producer RTE-4 checks message shape, skips system messages, embeds and writes each accepted body. It has no fact-extraction guidance, truth test, automatic deduplication or entity linking. Optional RTE-8 preprocessing means raw refers to bypassing fact inference, not guaranteed preservation of original multimodal bytes.

Later consumers: ordinary RTE-1 context selection and RTE-2 caller retrieval, with RTE-7 an afforded answer consumer. Authority is advisory knowledge in the inspected extraction channel; arbitrary caller-authored semantics are not assigned universal instruction authority. Persistence can cross calls/sessions; no task horizon is fixed by a scope ID. Individually addressable text and ADD history persist; original source warrant and reasons are unknown. Raw retention alone is not a qualifying automatic distillation route, although compiled vectors can later affect access. Replacements and withdrawal follow RTE-6. No observed raw payload instance or response dependence is available. Source quotations supporting its admission/write route remain once on RTE-4.


### OBJ-8 — Automatically extracted factual payloads

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Operative object replacing the extracted portion of superseded OBJ-1. Source-native identity: payload `data` with UUID, hash, timestamps, scope IDs, optional `attributed_to` and expiration/caller metadata. Form: natural-language generated facts with symbolic metadata; access structures remain OBJ-6. Storage: configured vector-store payloads. Lineage: trace-extracted from supplied conversational messages by RTE-1. The ADDITIVE_EXTRACTION_PROMPT requests contextual factual statements and source attribution; admission checks nonempty text, available embeddings, hashes and persistence rather than truth or entailment. Consequently preservation versus ampliation is indeterminate without generated instances.

Later consumers: RTE-1's extraction LLM as contextual knowledge, RTE-2's requesting caller, and RTE-7's documented answer generator at afforded status. Persistence can cross calls/sessions under surviving store configuration; task horizon follows caller scope. Individual text is addressable/editable by UUID. Retained derivation is limited to source attribution/metadata and ADD history, not full generating prompt, trace or criticism. No observed payload instance or behavior activation is present. Explicit replacements thereafter follow RTE-6; their warrant is separately instance-dependent.

> memory_id = str(uuid.uuid4())
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
> 
>         if not records:
>             self.db.save_messages(messages, session_scope)
>             return []
> 
>         # Phase 6: Batch persist
>         all_vectors = [r[2] for r in records]
>         all_ids = [r[0] for r in records]
>         all_payloads = [r[3] for r in records]
> --- `mem0/memory/main.py:1030-1050` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### OBJ-9 — Transient vision description

Source-native identity: description text returned by `get_image_description`, then substituted into normalized message content in RTE-8. Natural-language content in transient Python memory; generated from caller multimodal input. It is not a separate accumulated memory substrate. It can later become a raw payload, extraction input or recent-message text through RTE-4 or RTE-1. SRC-1 `mem0/memory/utils.py`; the supporting generated quotation is on RTE-8. Description grounding and provider semantics are uninspected. This object separates the epistemic content edge without changing the specialist's memory scope or classifications.



### Routes

### RTE-1 — Automatic conversational extraction and internal read-back

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Parent referent preserved: `Memory.add(infer=True)` to `_add_to_vector_store`. Owner: synchronous Memory. Trigger: caller supplies messages and at least one user/agent/run identifier. Producer: configured LLM, embedding model, CPU payload processing and vector store. Normalization precedes extraction; optional vision behavior is RTE-8. Exact scope selects OBJ-2, current parsed conversation embedding selects up to ten payloads from OBJ-8, OBJ-7 and OBJ-3 under identity filters. Only id/text from existing payloads and recent message content enter the generated user prompt; the caller need not request that read-back. Integer aliases replace UUIDs for the extraction input. There is no token-length budget in this route beyond record counts.

Guidance: ADDITIVE_EXTRACTION_PROMPT, optional agent suffix when agent_id exists without user_id, and `prompt or custom_instructions`. Existing text is instructed to serve deduplication/linking, not as a source for new extraction. The static prompt advertises summary/recently-extracted inputs, but this call does not populate those arguments. It uses ten last messages although prompt prose discusses twenty. These prompts are applied, not revised by the route.

Admission: parse generated JSON `memory` list; retain nonempty texts with embeddings; skip exact content hashes among retrieved memories and the current batch. No semantic truth, contradiction or preservation check follows. LLM failure raises; parse failure becomes empty extraction; batch embedding/insertion has per-item fallback. Only confirmed inserts are returned and indexed. Immediate result is ADD IDs/text, not generated assistant behavior. Persistence: OBJ-8, OBJ-5, OBJ-2 and optional entity index. Later read-back: subsequent RTE-1 and RTE-2. Delegated visibility: selected context goes to configured providers; downstream provider internals are uninspected. No separate worker delegation is implemented here.

Content/update relation: truth-apt transformation, indeterminate between faithful extraction/non-ampliative reshaping and unsupported ampliation in particular model outputs. Guidance demands source attribution but no observed instance proves it. The route does not operationally UPDATE/DELETE old facts; new shifted preferences can coexist. The guidance requests `linked_memory_ids`, but the persisted fact payload code does not copy that output field. Entity linking is a different implemented mechanism.

Revision/accountability: admission changes retained knowledge automatically; rejection is structural, embedding/store failure or duplicate detection, not acceptance against a truth criterion. Recovery uses retry/fallback for stores and caller-invoked maintenance, not an atomic rollback across stores. Candidate text is individually addressable by UUID and editable, but its assumptions/reasons are not separately structured. Theory-builder conditions 1–4: (1) localized factual content wired; applicability as formulated theory is instance-dependent; (2) content-sensitive context/dedup guidance wired, actual generated dependence unobserved; (3) content-directed criticism leading to revised theory or reliance uninspected, with no such evaluator identified in the inspected ADD-only route; (4) retained facts feed later rounds, but iteration from criticism is uninspected. Repeated context use alone does not establish conditions 3–4.

Implementation conclusion status: wired. Activation conclusion status: uninspected. Benefit conclusion status: uninspected. Expiration caveat: existing-memory retrieval calls vector search directly and does not apply the public expiry filter. Evidence: SRC-1, synchronous extraction; SRC-2, additive prompt.

> # Phase 0: Context gathering
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
> 
>         # Map UUIDs to integers (anti-hallucination)
>         existing_memories = []
>         uuid_mapping = {}
>         for idx, mem in enumerate(existing_results):
>             uuid_mapping[str(idx)] = mem.id
>             existing_memories.append({"id": str(idx), "text": mem.payload.get("data", "")})
> 
>         # Phase 2: LLM extraction (single call)
>         is_agent_scoped = bool(filters.get("agent_id")) and not filters.get("user_id")
>         system_prompt = ADDITIVE_EXTRACTION_PROMPT
>         if is_agent_scoped:
>             system_prompt += AGENT_CONTEXT_SUFFIX
> 
>         custom_instr = prompt or self.custom_instructions
> 
>         user_prompt = generate_additive_extraction_prompt(
>             existing_memories=existing_memories,
>             new_messages=parsed_messages,
>             last_k_messages=last_messages,
>             custom_instructions=custom_instr,
>         )
> --- `mem0/memory/main.py:920-955` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> Use these ONLY for deduplication and linking — do NOT extract new memories from Existing Memories. Your extractions must come exclusively from New Messages. If new information in New Messages is semantically equivalent to an Existing Memory with no meaningful new context, skip it.
> 
> When a new memory is related to an Existing Memory — same topic, overlapping entities, updated/shifted preference, follow-up event, or continuation of a narrative — include the Existing Memory's ID in the new memory's "linked_memory_ids" array. Your ADD output IDs remain sequential ("0", "1", ...) but linked_memory_ids uses the UUIDs from this list.
> --- `mem0/configs/prompts.py:511-513` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> if not text or text not in embed_map:
>                 continue
> 
>             mem_hash = hashlib.md5(text.encode()).hexdigest()
>             if mem_hash in existing_hashes or mem_hash in seen_hashes:
>                 logger.debug(f"Skipping duplicate memory (hash match): {text[:50]}")
>                 continue
>             seen_hashes.add(mem_hash)
> --- `mem0/memory/main.py:1019-1026` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Coordinator runtime evidence for distinct failure paths:

> logger.error(f"LLM extraction failed: {e}")
>             raise LLMError(f"LLM extraction failed: {e}") from e
> --- `mem0/memory/main.py:970-971` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`
> except Exception as e:
>             logger.error(f"Error parsing extraction response: {e}")
>             extracted_memories = []
> --- `mem0/memory/main.py:984-986` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`
> if not persisted_records:
>             self.db.save_messages(messages, session_scope)
>             raise VectorStoreError(
>                 f"Failed to insert any of the {len(records)} extracted memories into the vector store"
>             )
> --- `mem0/memory/main.py:1072-1076` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

Decision roles and operating mode: open caller requests; caller selects input/configuration and can withhold invocation; computation performs the described proposal/selection and structural admission. Human factual review is uninspected, not required by the inspected route. Answer-oracle access: uninspected beyond the stated inputs; no supplied expected-answer evaluator is evidenced. Learning conclusion status: uninspected for improved future capacity; no measured improvement or attribution. Reflection conclusion status: uninspected; retained user/task content does not by itself establish a two-way self-representation of Mem0 machinery. Autonomous execution of the described code steps: wired; autonomous theory-builder qualification: uninspected because criticism and criticism-driven iteration are unestablished.

### RTE-2 — Caller-requested hybrid memory retrieval

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Parent referent preserved: `Memory.search`, with immediate return `results`. Trigger/consumer: a caller requests query plus identity filters. Selection embeds query and fetches `max(top_k * 4, 60)` semantic candidates; keyword search supplies scores, not additional candidate rows. spaCy entity extraction on the query feeds up to eight query entities into scoped entity searches, up to 500 rows per entity, similarity gate 0.5. Linked IDs receive bounded boosts, diminished as entity fanout grows. Public defaults: top_k 20, semantic threshold 0.1, rerank false, expired rows hidden.

The scorer excludes candidates below the semantic threshold, then combines semantic, normalized BM25 and entity boosts; final normalization depends on active score dictionaries. Keyword-only matches cannot rescue a memory omitted by semantic overfetch. Optional configured reranker runs only when requested and catches failures to retain original results; its internal selection semantics are uninspected. `explain` can expose numerical score details. Invalid query/filter/top_k/threshold and unsupported reference_date are rejected before execution.

Storage mutation: none. Delivery: caller result dictionary containing text and selected metadata, not automatic model continuation. Implemented retrieval conclusion status: wired. Consumer-role direction conclusion status: afforded, established by documented calling interface and RTE-7. Behavioral force: ranking for access structures, advisory knowledge for documented answer generation. Delegated visibility: query/selected results may reach configured embedding/reranker providers; no execution observed. Expiry does not withdraw all other channels. No theory revision or acceptance occurs; recovery is reranker fallback. Evidence: SRC-1, search, `_search_vector_store`, `_compute_entity_boosts`, `score_and_rank`.

> for result in semantic_results:
>         mem_id = result.get("id")
>         if mem_id is None:
>             continue
> 
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
> 
>         scored_result = {
>             "id": mem_id_str,
>             "score": combined,
>             "payload": result.get("payload"),
>         }
>         if explain:
> --- `mem0/utils/scoring.py:105-126` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> # Step 7: Build candidate set from semantic results
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
> 
>         # Step 8: Score and rank
>         scored_results = score_and_rank(
>             semantic_results=candidates,
>             bm25_scores=bm25_scores,
>             entity_boosts=entity_boosts,
>             threshold=threshold,
> --- `mem0/memory/main.py:1680-1698` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### RTE-3 — Automatic procedural-summary creation

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Parent referent preserved: `_create_procedural_memory`, selected by `agent_id is not None` plus `memory_type == procedural_memory`, before normal infer/vision handling. Thus infer=False does not bypass this selected branch. Owner: synchronous Memory. Input: caller messages, metadata, optional prompt. Producer: LLM with default procedural system guidance or caller replacement. Admission: generated text has code fences removed and must be nonempty; metadata must exist; embedding and insertion must succeed. No content adequacy, execution-success or verbatim-preservation check is implemented. Immediate result: newly created summary ID/text with ADD event.

Persistence: OBJ-3 plus OBJ-6 and ADD history OBJ-5. The route does not save OBJ-2 recent messages or build OBJ-4 entity links. Later-consumer chain: raw execution/conversation → automatic summary → vector payload → either automatic existing-memory selection in RTE-1 or requested RTE-2 return. Continuation use is an afforded caller role from the prompt, not a wired checkpoint loader. Default horizon is per-task by the prompt's explicit continuation objective; custom prompts and caller-scoped retrieval need not respect that horizon. Timing: transformation occurs in the current add call, not a scheduled batch. Form: natural-language distilled text.

Addressability: summary is one inspectable/editable unit with proposed internal headings; those headings are guidance rather than enforced fields. Persistence can cross calls/sessions, but rationale fidelity and actual later activation are uninspected. Relation is truth-apt transformation: indeterminate, intended as non-ampliative preservation of supplied execution history. Policy/next-step content can also be retained if present. No observed output establishes preservation versus invented content.

Theory-builder conditions 1–4: (1) localized summary content wired, whether it states a theory depends on supplied/generated text; (2) advisory consumption through RTE-1 wired, continuation dependence uninspected; (3) content-directed criticism with resulting revision uninspected, no summary critic identified; (4) criticism-driven iteration uninspected. New summaries are ADDs rather than automated revisions of prior summaries. Rejection is empty content/provider failure; rollback or recovery is caller maintenance, with no cross-store transaction. Implementation conclusion status: wired. Continuation-role conclusion status: afforded. Activation and benefit conclusion statuses: uninspected. Evidence: SRC-1, procedural creator; SRC-2, prompt on OBJ-3.

> parsed_messages = [
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
>         except Exception as e:
>             logger.error(f"Error generating procedural memory summary: {e}")
>             raise
> 
>         if not procedural_memory:
>             raise ValueError(
>                 "The LLM returned no content for the procedural memory summary. "
>                 "The model may have declined the request or returned an empty response."
>             )
> 
>         if metadata is None:
>             raise ValueError("Metadata cannot be done for procedural memory.")
> 
>         metadata = {**metadata, "memory_type": MemoryType.PROCEDURAL.value}
>         embeddings = self.embedding_model.embed(procedural_memory, memory_action="add")
>         memory_id = self._create_memory(procedural_memory, {procedural_memory: embeddings}, metadata=metadata)
> --- `mem0/memory/main.py:2018-2045` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Decision roles and operating mode: open caller requests; caller selects input/configuration and can withhold invocation; computation performs the described proposal/selection and structural admission. Human factual review is uninspected, not required by the inspected route. Answer-oracle access: uninspected beyond the stated inputs; no supplied expected-answer evaluator is evidenced. Learning conclusion status: uninspected for improved future capacity; no measured improvement or attribution. Reflection conclusion status: uninspected; retained user/task content does not by itself establish a two-way self-representation of Mem0 machinery. Autonomous execution of the described code steps: wired; autonomous theory-builder qualification: uninspected because criticism and criticism-driven iteration are unestablished.

### RTE-4 — Raw message retention

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Route: `_add_to_vector_store(infer=False)`. Trigger: caller chooses raw mode unless procedural branch was selected first. Producer: input normalization then `_create_memory` per message. Valid dict messages need role/content; system messages are skipped. Embedding, hash and lemma generation are automatic, but caller supplies the semantic text. Actor name and role are retained. Immediate result: ADD event per accepted message. Persistence: OBJ-7, OBJ-6, OBJ-5; no recent-message save or entity extraction in this branch. Later consumers: RTE-1, RTE-2. Authority: knowledge where supplied as facts; no claim that arbitrary caller text has a uniform semantic authority.

Admission is structural and store success; no LLM extraction, factual review or dedup of raw entries. Recovery/withdrawal: RTE-6. Guidance is API shape and preprocessing, not a learned theory. Theory-builder conditions 1–4: caller text can be localized content (afforded); context delivery is wired, content dependence unobserved; criticism and criticism-driven iteration uninspected. This is acquisition/import, with original warrant unknown; arbitrary message body content is preserved after applicable normalization. Implementation conclusion status: wired; manual-authoring conclusion status: afforded. Evidence: SRC-1, raw branch and `_create_memory`.

> per_msg_meta = deepcopy(metadata)
>                 per_msg_meta["role"] = message_dict["role"]
> 
>                 actor_name = message_dict.get("name")
>                 if actor_name:
>                     per_msg_meta["actor_id"] = actor_name
> 
>                 msg_content = message_dict["content"]
>                 msg_embeddings = self.embedding_model.embed(msg_content, "add")
>                 mem_id = self._create_memory(msg_content, {msg_content: msg_embeddings}, per_msg_meta)
> 
>                 returned_memories.append(
>                     {
>                         "id": mem_id,
>                         "memory": msg_content,
> --- `mem0/memory/main.py:896-910` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Decision roles and operating mode: open caller requests; caller selects input/configuration and can withhold invocation; computation performs the described proposal/selection and structural admission. Human factual review is uninspected, not required by the inspected route. Answer-oracle access: uninspected beyond the stated inputs; no supplied expected-answer evaluator is evidenced. Learning conclusion status: uninspected for improved future capacity; no measured improvement or attribution. Reflection conclusion status: uninspected; retained user/task content does not by itself establish a two-way self-representation of Mem0 machinery. Autonomous execution of the described code steps: wired; autonomous theory-builder qualification: uninspected because criticism and criticism-driven iteration are unestablished.

Read-back audit: selection for later extraction/search is inherited from RTE-1/RTE-2; expiry/deletion is bounded by RTE-6. Configured embedder/store receive content; no worker delegation. Activation is uninspected.

### RTE-5 — Automatic entity/access derivation and maintenance

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Route: successful inferred inserts → `extract_entities_batch` → normalize/deduplicate descriptions → embed and match retained entities → update links or insert entity. Exact normalized text match is preferred; otherwise top-one semantic match at least 0.95 merges linked IDs into that entity. This is genuine curation over retained entity access memory, not just input hash checking. Batches reuse scope IDs; exact listing examines up to 10,000 rows. spaCy unavailable means no entities; errors are logged without rejecting primary memory insertion.

Producer: extraction heuristics and embedding/store APIs, not an LLM critic. Persisted changes are entity associations; full merge rationale and extraction provenance are not retained. `_update_memory` re-extracts entities on changed text, removing prior links best-effort first. `_remove_memory_from_entity_store` does nothing when that process has not initialized the entity store; failed cleanup need not invalidate the main write. Later consumer RTE-2 reads links for ranking; index contents are not user-facing factual graph assertions. Immediate return is internal; subsequent caller return belongs to RTE-2. No special instruction or knowledge acceptance criterion is present.

Transformation: non-truth-apt access-policy/content update, with possible entity identity errors; not a truth-validated entity theory. Theory-builder conditions 1–4: localized heuristic rules wired as shipped code, their application wired, criticism/revision of those rules uninspected, criticism-driven iteration uninspected. The rules are not learned during these mutations. Natural-language entity labels and symbolic associations can persist across tasks when the caller reuses scope; the task horizon is otherwise unspecified. Automatic generation is online in add/update; no result instances or benefit observed. Evidence: SRC-1, entity linking/upsert and entity extraction entry points.

> entity_embedding = self.embedding_model.embed(entity_text, "add")
>             search_filters = {k: v for k, v in filters.items() if k in ("user_id", "agent_id", "run_id") and v}
>             exact_match = self._existing_entities_by_text(search_filters).get(self._normalize_entity_text(entity_text))
> 
>             existing = []
>             if exact_match is None:
>                 existing = self.entity_store.search(
>                     query=entity_text,
>                     vectors=entity_embedding,
>                     top_k=1,
>                     filters=search_filters,
>                 )
> 
>             semantic_match = existing[0] if existing and existing[0].score >= 0.95 else None
>             match = exact_match or semantic_match
>             if match:
>                 # Update existing entity's linked_memory_ids
>                 payload = match.payload or {}
>                 linked_ids = payload.get("linked_memory_ids", [])
>                 if memory_id not in linked_ids:
>                     linked_ids.append(memory_id)
>                     payload["linked_memory_ids"] = linked_ids
> --- `mem0/memory/main.py:608-629` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Decision roles and operating mode: open caller requests; caller selects input/configuration and can withhold invocation; computation performs the described proposal/selection and structural admission. Human factual review is uninspected, not required by the inspected route. Answer-oracle access: uninspected beyond the stated inputs; no supplied expected-answer evaluator is evidenced. Learning conclusion status: uninspected for improved future capacity; no measured improvement or attribution. Reflection conclusion status: uninspected; retained user/task content does not by itself establish a two-way self-representation of Mem0 machinery. Autonomous execution of the described code steps: wired; autonomous theory-builder qualification: uninspected because criticism and criticism-driven iteration are unestablished.

Read-back audit: immediate output is an internal index mutation; later reader is RTE-2 under query entity selection and similarity/linked-ID predicates. Provider visibility is the embedded entity text; no worker delegation. Invalidation follows best-effort cleanup in RTE-6; actual activation/benefit remains uninspected. Rejection may skip entities or catch linking failures without reverting primary text. Recovery has no demonstrated cross-store rollback.

### RTE-6 — Explicit update, deletion, expiration and reset

Evidence anchor: SRC-1, `mem0/memory/main.py`.

Maintenance family, owner synchronous Memory. Trigger: caller invokes update/delete/delete_all/reset or supplies expiration_date; automatic read filters evaluate expiry. Update can replace text, metadata or expiration; identity fields are immutable after creation. It reads the current payload, preserves original creation time, writes new text/hash/lemmas/vector and updated timestamp, logs before/after text and repairs entities best-effort. Admission rejects missing memory, invalid/nontext content, malformed dates or no requested change. No factual critique or required justification is imposed. Immediate return is success text after route completion; retained mutations affect RTE-1 and RTE-2 later.

Delete removes live vector and retains a DELETE history row with old text, then attempts entity cleanup. Scoped delete_all repeatedly lists/deletes batches and stops on an empty or repeated batch; it does not delete the messages table. Reset drops SQLite history/messages and resets main vectors, with entity reset only if initialized. Failure can leave partial state: operations span stores without a shared transaction or automatic replay from history. `history` affords manual inspection, not automated recovery.

Expiry stores an ISO date; dates strictly earlier than current UTC date count expired. Public search/get_all hide them unless show_expired; direct get and automatic extraction vector search do not apply that filter. Therefore expiry is bounded withdrawal from selected public results, not universal forgetting. Expiry can be cleared or moved by update. Manual deletion is stronger for live vectors but leaves history and potentially recent messages/index residue.

Semantic update relation: arbitrary caller replacement is indeterminate without an actual instance; metadata/date changes are non-truth-apt access updates. Guidance is caller text plus structural/identity rules. What persists: replacement text and old/new history, not stated criticism or acceptance reasons. Addressability is individual payload plus metadata. Theory-builder conditions 1–4: localized replacement content afforded; later context use wired; content-directed criticism is not required and remains uninspected; criticism-driven iteration remains uninspected. Implementation conclusion status: wired. Human curation conclusion status: afforded. Activation/benefit conclusion status: uninspected. Evidence: SRC-1, update/delete/reset/expiry helpers and synchronous filters.

> self.vector_store.update(
>             vector_id=memory_id,
>             vector=embeddings,
>             payload=new_metadata,
>         )
>         logger.info(f"Updating memory with ID {memory_id=} with {data=}")
> 
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
> 
>         # Entity-store cleanup: strip this memory's id from old-text entities,
>         # then re-extract entities from the new text and link them back.
>         session_filters = {k: new_metadata[k] for k in ("user_id", "agent_id", "run_id") if new_metadata.get(k)}
>         if text_changed:
>             self._remove_memory_from_entity_store(memory_id, session_filters)
>             self._link_entities_for_memory(memory_id, data, session_filters)
> --- `mem0/memory/main.py:2087-2110` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> session_filters = {k: payload[k] for k in ("user_id", "agent_id", "run_id") if payload.get(k)}
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
> 
>         # Entity-store cleanup: strip this memory's id from any entity records
>         # that linked to it. Non-fatal — the helper swallows errors.
>         self._remove_memory_from_entity_store(memory_id, session_filters)
> --- `mem0/memory/main.py:2124-2140` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> def _payload_is_expired(payload: Optional[Dict[str, Any]]) -> bool:
>     if not payload:
>         return False
>     expiration_date = payload.get("expiration_date")
>     if not expiration_date:
>         return False
>     try:
>         return date.fromisoformat(str(expiration_date)) < datetime.now(timezone.utc).date()
>     except ValueError:
>         return False
> --- `mem0/memory/main.py:442-451` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Decision roles and operating mode: open caller requests; caller selects input/configuration and can withhold invocation; computation performs the described proposal/selection and structural admission. Human factual review is uninspected, not required by the inspected route. Answer-oracle access: uninspected beyond the stated inputs; no supplied expected-answer evaluator is evidenced. Learning conclusion status: uninspected for improved future capacity; no measured improvement or attribution. Reflection conclusion status: uninspected; retained user/task content does not by itself establish a two-way self-representation of Mem0 machinery. Autonomous execution of the described code steps: wired; autonomous theory-builder qualification: uninspected because criticism and criticism-driven iteration are unestablished.

Read-back audit: subsequent RTE-1/RTE-2 and caller history reads consume effects; inherited identity/query selection chooses surviving material. Configured embedding/store calls see edited content, and no worker delegation is evidenced. Invalidation is the operation itself, with the stated expiry and residual-history limits.

### RTE-7 — Documented caller answer assembly and inspection reads

Evidence anchor: SRC-2, `README.md`.

Documented caller-consumer route in the README: `chat_with_memories` requests top-three memories for a user, joins their `memory` text, builds a system message asking the answer model to use query and memories, generates an answer, appends that assistant message, then calls Memory.add. The shell loop accepts successive questions. This establishes an afforded consumer with query-derived targeting and count budget, not deployed wiring or faithful response dependence. Content is advisory knowledge even in a system message; the surrounding static instruction directs answer generation. The example retains the old user scope across questions, giving a cross-question/cross-task affordance alongside the README personalization claim.

The read is pull from the caller to Memory; automatic model input assembly by this documented caller is only afforded. It is not counted as a second wired push in the Memory subsystem. Direct get/get_all/history also expose inspection reads by UUID/scope; their final consumer semantics beyond the caller are unspecified. `Memory.chat` itself raises NotImplementedError. The example supplies system-role memory context back to add; parse_messages includes system content in parsed input, although extraction guidance distinguishes user/assistant facts. This is potential input recycling, not a demonstrated failure.

Immediate output: answer string in example, structured memory/history in inspection APIs. Later retention: example feeds messages through RTE-1. No library-owned action execution or continuation is demonstrated. Admission/withdrawal follow the selected memory interfaces; answer generation does not add a truth test. Theory revision uninspected. Evidence: SRC-2, README example; SRC-1, `get`, `get_all`, `history`, `parse_messages`, `chat`.

> def chat_with_memories(message: str, user_id: str = "default_user") -> str:
>     # Retrieve relevant memories
>     relevant_memories = memory.search(query=message, filters={"user_id": user_id}, top_k=3)
>     memories_str = "\n".join(f"- {entry['memory']}" for entry in relevant_memories["results"])
> 
>     # Generate Assistant response
>     system_prompt = f"You are a helpful AI. Answer the question based on query and memories.\nUser Memories:\n{memories_str}"
>     messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": message}]
>     response = openai_client.chat.completions.create(model="gpt-5-mini", messages=messages)
>     assistant_response = response.choices[0].message.content
> 
>     # Create new memories from the conversation
>     messages.append({"role": "assistant", "content": assistant_response})
>     memory.add(messages, user_id=user_id)
> --- `README.md:209-222` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

> def chat(self, query):
>         raise NotImplementedError("Chat function not implemented yet.")
> --- `mem0/memory/main.py:2189-2190` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Read-back audit: requested query/identity or ID selects retained parts; immediate answer delivery belongs to an external documented consumer, while inspection methods return data. Host/provider visibility follows caller prompt assembly and is afforded, not deployed. Invalidations are inherited from the chosen library read; actual answer activation is uninspected.

### RTE-8 — Optional vision normalization before general writes

Evidence anchor: SRC-1, `mem0/memory/utils.py`.

Alternate route: when enable_vision is configured, list/image message content can be converted to an LLM description before general raw/inferred handling. Without it, list content retains textual parts and image-only input can be skipped. System messages pass through. This branch precedes `_add_to_vector_store`, so infer=False is not necessarily a byte-preserving path for original multimodal input. Procedural mode is selected earlier and bypasses this helper.

Producer: `parse_vision_messages` and configured LLM description helper. Persistence: resulting descriptions can feed OBJ-8, OBJ-7 and OBJ-2; original images are not demonstrated as retained memory objects here. Form visible at Memory boundary: natural-language text; provider vision internals are uninspected. Admission/rejection: malformed image URL raises; missing content or absent text can be skipped; provider failure propagates. Transformation warrant is indeterminate; no semantic verification of descriptions inspected. Guidance and full provider behavior are uninspected, preventing exhaustive lineage/trace-source claims. Later consumers are the same as RTE-1/RTE-4. Wrapper implementation conclusion status: wired; image-grounding fidelity, theory-builder conditions 1–4 and benefit conclusion statuses: uninspected. Evidence: SRC-1, add and vision parsing.

> # Handle message content
>         if isinstance(content, list):
>             if llm is None:
>                 text_parts = [
>                     part["text"] for part in msg["content"]
>                     if isinstance(part, dict) and part.get("type") == "text"
>                 ]
>                 if not text_parts:
>                     continue
>                 returned_messages.append({"role": role, "content": " ".join(text_parts)})
>             else:
>                 description = get_image_description(msg, llm, vision_details)
>                 returned_messages.append({"role": role, "content": description})
>         elif isinstance(content, dict) and content.get("type") == "image_url":
>             if llm is None:
>                 continue
>             image_url_obj = content.get("image_url")
>             image_url = image_url_obj.get("url") if isinstance(image_url_obj, dict) else None
> --- `mem0/memory/utils.py:203-220` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


Decision roles and operating mode: open caller requests; caller selects input/configuration and can withhold invocation; computation performs the described proposal/selection and structural admission. Human factual review is uninspected, not required by the inspected route. Answer-oracle access: uninspected beyond the stated inputs; no supplied expected-answer evaluator is evidenced. Learning conclusion status: uninspected for improved future capacity; no measured improvement or attribution. Reflection conclusion status: uninspected; retained user/task content does not by itself establish a two-way self-representation of Mem0 machinery. Autonomous execution of the described code steps: wired; autonomous theory-builder qualification: uninspected because criticism and criticism-driven iteration are unestablished.

Read-back audit: immediate return is normalized text for RTE-1/RTE-4; no accumulated memory is selected by this preprocessing operation. Later read-back and expiry follow those downstream records. Image/message content is visible to the configured provider; no separate worker delegation is evidenced. No persistent image checkpoint or automatic rollback is established.


### Claims

### CLM-1 — Personalized memory and continuous learning claim

Evidence anchor: SRC-2, `README.md`.

Source-native claim: the README describes remembering preferences, adapting to needs and continuous learning. Claim conclusion status: claimed. Implementation support: RTE-1, RTE-3 and RTE-5 create durable trace-derived content/access structures, then RTE-1/RTE-2 consume them. The README example supplies an afforded answer consumer. That supports the structural trace-learning classification, not improved accuracy, effective adaptation or parameter training. No inspectable execution intervention or benefit comparison is in this commissioned evidence. Faithfulness tested therefore remains not-determinable rather than no or yes.

Evidence: SRC-2, README overview.

> [Mem0](https://mem0.ai) ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. It remembers user preferences, adapts to individual needs, and continuously learns over time—ideal for customer support chatbots, AI assistants, and autonomous systems.
> --- `README.md:73-73` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`


### CLM-2 — Managed-platform benchmark gains

Claimed operation: higher benchmark scores with a new algorithm. Conclusion status: claimed. Source: SRC-3 `README.md`. The source explicitly locates the numbers on the managed platform, which is excluded. No raw benchmark trace or causal comparison entered this source boundary. The claim is not silently transferred to the OSS pipeline.

> All benchmarks run on the same production-representative model stack. Single-pass retrieval (one call, no agentic loops) at a top_200 retrieval budget. Scores reflect Mem0's managed platform, which includes proprietary optimizations not available in the open-source SDK; open-source users should expect directionally similar gains but not identical numbers.
> --- `README.md:54-54` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`

### CLM-3 — Add docstring describes automatic update/delete

Claimed operation: `infer=True` decides whether to add, update or delete. Conclusion status: claimed. Source: SRC-2 `mem0/memory/main.py`. The inspected implementation in RTE-1 is additive, while explicit maintenance APIs are separate routes. This claim is stale relative to the inspected branch and cannot characterize its admission policy.

> infer (bool, optional): If True (default), an LLM is used to extract key facts from
>                 'messages' and decide whether to add, update, or delete related memories.
>                 If False, 'messages' are added as raw memories directly.
> --- `mem0/memory/main.py:790-792` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`



### Evidenced absences

### ABS-1 — No update/delete dispatch in the inferred additive branch

Conclusion status: absent. Searched boundary: the complete synchronous `_add_to_vector_store` body in `mem0/memory/main.py` at the reviewed commit, selected from its definition to the following `get` definition; dispatch question: whether this branch calls existing-memory update/delete rather than constructing new ADD records. The complete body was read in bounded ranges. Evidence: SRC-1; generated selection/payload/admission/persistence quotes on RTE-1 and OBJ-8. No such dispatch occurs in that routine; RTE-6 contains explicit maintenance outside it. This supports only the bounded correction to CLM-3, not absence of deletion elsewhere or opaque-provider effects.


### Behavioral-authority paths

### BAP-1 — Extraction context

Consumer: configured extraction model. Channel: generated prompt's existing-memory and recent-message sections. Force: advisory knowledge. Horizon: each future inferred add where identity/embedding selectors choose the records. Route RTE-1; SRC-1 `mem0/memory/main.py`, SRC-2 `mem0/configs/prompts.py`. Delivery is wired; content-dependent effect and benefit are uninspected.

### BAP-2 — Retrieval ordering

Consumer: synchronous search scorer and requesting caller. Channel: dense/lexical scores, entity-to-memory links and result dictionary. Force: ranking and bounded availability. Horizon: the current requested search. Route RTE-2, RTE-5; SRC-1 `mem0/utils/scoring.py`, `mem0/memory/main.py`. Computed scoring is wired; empirical relevance benefit is uninspected.

### BAP-3 — Documented external answer context

Consumer: answer model in README chat example. Channel: system message containing queried memory text. Force: advisory knowledge under the caller's answer instruction. Horizon: current answer, with subsequent add retaining the conversation. Route RTE-7; SRC-2 `README.md`. Consumer-role status: afforded. Deployed wiring, activation and correctness are uninspected.


## Runtime account

The ordinary invocation starts with application code constructing `Memory`, supplying user/agent/run identity and messages, then calling `add`. Python owns progression: input normalization, optional vision preprocessing, recent-message and existing-memory selection, a configured LLM extraction call, JSON parsing, embedding, hash filtering, vector insertion, history/entity maintenance and return. The application chooses the input and configuration; the LLM proposes text; Python admission decides which returned items reach storage. The terminal output is memory IDs, text and ADD events, or a raised provider/store error. It is a returning memory computation, not an enclosing action agent.

The loop's context is the new messages, selected retained context and prompt instructions; state lives in vector collections and SQLite. Providers execute inference and vector operations. Durable retention reaches later add/search calls; no scheduler automatically initiates those calls. The host remains responsible for an enclosing task loop, granting credentials, and deciding how retrieved text enters its own prompts. The README chat example is an afforded integration, not observed operation. Internal extraction supplies retained material without a model-originated retrieval request; external search fulfils the caller's request.

The runtime-client controls are source messages and identities, `infer`, procedural memory type, caller prompt/custom instructions, provider configuration, search filters/top_k/threshold/expiration visibility and optional reranking. There is no inspected deployed grant set. Scope identifiers restrict selection but do not prove caller authentication or deployed isolation. ID-based get/update/delete differ from filtered search, so search validation cannot be generalized to every access path. Configured provider extensions, optional LLM callbacks and host Python code have effects outside the selected enforcement points.

Material alternatives are raw `infer=False` insertion, procedural summary generation, manual update/delete/expiration, ID-based reads and history, optional vision parsing, optional NLP/keyword/reranker paths, and asynchronous execution. `AsyncMemory.add` has a distinct async API and additional LLM argument; parity and scheduling/recovery guarantees were not established. Platform/JS/server/CLI alternatives remain outside scope. Raw writes bypass fact extraction; procedural summaries bypass conversational extraction policy. The scope of a guarantee is therefore its named route, not Mem0 as a whole.

Forcing cases were inspected statically:

| case | owner and enforcement point | route and outcome | guarantee strength | conclusion status | limits |
|---|---|---|---|---|---|
| LLM call fails versus extraction JSON is malformed | Memory._add_to_vector_store | RTE-1 propagates provider failures as LLMError; parse failure produces no extracted memories and saves messages | protocol | wired | Different failure classes have different external visibility; no runtime execution established frequency |
| Batch persistence fails or partially succeeds | Memory._add_to_vector_store | RTE-1 retries individual inserts; only acknowledged inserts become results/history/entities; zero persisted raises VectorStoreError after message save | best effort | wired | Relies on backend acknowledgement and insert semantics; no cross-store transaction or rollback established |
| Missing search scope and explicit expired visibility | Memory.search and _search_vector_store | RTE-2 checks for scope keys; normal search excludes expired payloads, show_expired can include them | protocol | wired | Not authentication; internal extraction/direct ID paths have separate behavior |
| Optional reranker fails | Memory.search | RTE-2 returns original results after logging | best effort | wired | No full-signal ranking guarantee and no observed relevance result |

Evidence for these cases: SRC-1 `mem0/memory/main.py`. The first two are directly quoted on RTE-1. Scope validation is:

{
  "occurrences": [
    {
      "occurrence": 1,
      "start_line": 1317,
      "end_line": 1321,
      "start_offset": 56184,
      "end_offset": 56447,
      "citation": "> if not any(key in effective_filters for key in (\"user_id\", \"agent_id\", \"run_id\")):\n>             raise ValueError(\n>                 \"filters must contain at least one of: user_id, agent_id, run_id. \"\n>                 \"Example: filters={'user_id': 'u1'}\"\n>             )\n> --- `mem0/memory/main.py:1317-1321` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`\n"
    },
    {
      "occurrence": 2,
      "start_line": 1471,
      "end_line": 1475,
      "start_offset": 63187,
      "end_offset": 63450,
      "citation": "> if not any(key in effective_filters for key in (\"user_id\", \"agent_id\", \"run_id\")):\n>             raise ValueError(\n>                 \"filters must contain at least one of: user_id, agent_id, run_id. \"\n>                 \"Example: filters={'user_id': 'u1'}\"\n>             )\n> --- `mem0/memory/main.py:1471-1475` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`\n"
    },
    {
      "occurrence": 3,
      "start_line": 2998,
      "end_line": 3002,
      "start_offset": 130434,
      "end_offset": 130697,
      "citation": "> if not any(key in effective_filters for key in (\"user_id\", \"agent_id\", \"run_id\")):\n>             raise ValueError(\n>                 \"filters must contain at least one of: user_id, agent_id, run_id. \"\n>                 \"Example: filters={'user_id': 'u1'}\"\n>             )\n> --- `mem0/memory/main.py:2998-3002` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`\n"
    },
    {
      "occurrence": 4,
      "start_line": 3156,
      "end_line": 3160,
      "start_offset": 137610,
      "end_offset": 137873,
      "citation": "> if not any(key in effective_filters for key in (\"user_id\", \"agent_id\", \"run_id\")):\n>             raise ValueError(\n>                 \"filters must contain at least one of: user_id, agent_id, run_id. \"\n>                 \"Example: filters={'user_id': 'u1'}\"\n>             )\n> --- `mem0/memory/main.py:3156-3160` @ `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`\n"
    }
  ]
}

No dynamic check planned. Provider-failure injection, partial-store failures, expired-memory retrieval, and output-fidelity probes were considered. Static branches establish the wired control distinction sought here; live or mocked execution would add a different evidence layer and cannot establish real semantic fidelity without a candidate-linked evaluation. No credentials, packages or services were assumed available or used.

Decision roles and operating mode: open caller requests drive the pipeline, not an inspected experiment curriculum. Users/application code propose source messages or explicit edits and can withhold calls; the configured model proposes extracted/summary text; code admits nonempty embedded records and handles persistence failures. Model judgment is not an answer oracle. No expected-answer input or reference evaluator is supplied by the inspected production extraction call. Few-shot instructions express policy rather than a held-out answer oracle. The exact revision-admission guidance and persistence are recorded on each admitting route. Host review, deployment approval and provider-side decisions are uninspected.

## Lens scoping

### Memory/context scope

Depth: full. Trigger evidence: SRC-1 durable entries, history read-back and procedural branch; SRC-2 personalization claim CLM-1. Boundary: synchronous OSS Memory retained objects and access structures, their writes/maintenance and later consumers; RTE-1, RTE-2 and RTE-3 plus specialist extensions. Omitted external surfaces match Boundary and evidence. The specialist's exact profile scope and per-value uncertainties govern comparisons.

### Epistemic scope

Depth: full. Trigger evidence: SRC-2 CLM-1 and the extraction policy; SRC-1 RTE-1 and RTE-3 produce truth-apt text while RTE-2 selects it for reuse. Question: does extraction, storage or retrieval provide a checked basis for truth or improved later action? Assess message acquisition, fact/summary transformation, structural admission, retention, retrieval and explicit maintenance. Exclude managed-platform evaluation, opaque model reasoning and external agent outcomes, preventing production efficacy or full knowledge-production conclusions. Both lenses use the same source pin and canonical records.

## Lens outputs

### Memory/context lens

#### Core ideas

Mem0's default write route adds new factual text while automatically supplying earlier retained facts and the last ten messages to its extraction LLM. That makes internal memory delivery wired even though answer generation normally requires a caller to request memories. The route RTE-1 is ADD-only at this commit; the `add` docstring still describes add/update/delete decisions. No automatic replacement of contradictory facts follows from that wording.

The same vector store holds raw messages, extracted facts and procedural summaries. The procedural branch is a task-continuation summary generator, guided to retain action outputs and current context. It is an automatic trace-fed retained artifact, and it can enter subsequent extraction through the ordinary existing-memory selector. Its continuation role is afforded by the prompt and retrieval interface; an agent actually resuming from it is not observed. The record RTE-3 keeps these two consumer claims separate.

Memory includes access structures, not only readable text. Entity rows link normalized entity descriptions to memory IDs; dense vectors, optional sparse BM25 vectors and lemmatized fields affect ranking. These derived structures support automatic trace learning under the comparison definition, without implying model-weight updates or improved performance. The records OBJ-4 and OBJ-6 distinguish these operative representations from their readable fields.

Content trust is limited. Extraction guidance requests factual attribution and deduplication, but persisted payloads omit the generating prompt, full source trace, criticism and semantic-verification results. Recent messages are evicted; edit history records text changes rather than their justification. Delivered knowledge therefore has a traceable implementation route but no established factual acceptance criterion or observed faithfulness result.

#### Write side

The routes RTE-1 and RTE-3 automatically transform caller traces; RTE-4 acquires supplied text without normal fact inference, while RTE-8 can transform multimodal input first. Only RTE-1 saves the bounded recent-message context. The derived-to-later-consumer chains are factual conversation → payload → later extraction/context retrieval; execution history → procedural summary → the same selectors or afforded task continuation; and retained content → entity/vector/lexical structures → later retrieval ranking. Raw log retention OBJ-2 alone is not counted as trace learning.

Every automatic derived artifact was considered: fact text and procedural summaries have natural-language form and online generation; entity/embedding/lexical access structures have symbolic form and online generation. General fact/index horizons inherit caller scopes rather than proving per-task or cross-task. Default procedural guidance specifically affords per-task continuation; documented personal preference memory affords cross-task use. Optional image descriptions inherit the downstream route with uninspected provider semantics. No alternate checkpoint form, parameter-learning path or deferred consolidation job is established in this boundary.

The automatic main write is additive. LLM-guided non-repetition and an exact hash guard limit duplicate acquisition, while entity merging is curation over already retained material. Explicit replacement, deletion and expiry supply evolution/withdrawal. SQLite recent-message eviction supplies automatic forgetting. There is no requirement that stored generated content retain an argument, nor any separate retained criticism that a later round consumes. Structural admission must not be labeled factual acceptance; sampled model outputs would be needed to decide preservation, entailment or ampliation for specific text.

#### Read-back

The strongest internal consumer witness is RTE-1. On a new infer=True call it supplies the extraction model with ten exact-scope message rows and ten vector-selected prior text payloads. Trigger and selector input are current call identities/messages; chosen retained parts are utterance fields and prior id/text; delivery is generated prompt context. Count budgets do not bound tokens. This is wired identifier/embedding push even when the outer add call is human-triggered.

The requested read in RTE-2 is caller pull. Semantic overfetch controls the candidate pool; optional BM25/entity scoring and reranking alter its order. Entity and vector access structures are operative at those selectors, not merely available storage. The route RTE-7 gives a named answer consumer and top-three budget at afforded status. RTE-3's continuation consumer is not upgraded from afforded because its prompt says “continue”; its ordinary later extraction route is independently wired. Direct get/history have caller inspection roles without proof of subsequent model behavior.

Availability, delivery and activation remain separate. The code can persist content and pass it to later consumers; no retained execution here shows that a particular recalled claim caused an answer, that summarization preserved every output, or that ranking improved retrieval quality. Expiry filters do not cover automatic extraction or direct get, and entity cleanup can be skipped, so withdrawal is route-specific.

#### Comparison rationale

All fourteen axes are proposed in frontmatter with per-value witnesses. Partial assessments preserve supported positive values while refusing to turn default Qdrant behavior into an all-provider profile. Profile storage covers actual memory interfaces; “entity linking” alone does not justify graph storage. Numeric embeddings/sparse arrays are operative symbolic access data, not a claim that parameters were learned. Model parameters belong to uninspected dependencies.

The trace-learning yes is wired because automatic fact production persists and affects a later extraction/context selector, with additional derived ranking artifacts. It does not depend solely on the README benefit claim. Procedural summaries are explicitly included even though their intended transformation is preservation and their continuation benefit is unobserved. Ordinary conversation and supplied execution history warrant separate source values; actual task horizons remain partial. Online means produced within the synchronous use call; no evidence is manufactured for offline/staged alternatives.

Knowledge is supported by the extraction consumer, ranking by the access structures. The documented system-message placement does not independently justify instruction authority for factual content. Likewise hybrid requested search does not justify lexical push. Dedup is based on actual entity merging, not solely MD5 input collision checks. Explicit update gives evolve; delete/history and public expiry give bounded invalidate; evicted messages/deletions give decay. No verified semantic synthesis or consolidation is inferred from an LLM label. Faithfulness is not-determinable because no retained execution test is in scope, not because source code proves universal absence of such testing.

### Epistemic lens

#### 1. Source-and-claim boundary

The assessed routes acquire messages, extract factual text, summarize execution history, normalize optional images, build access structures, admit writes and select retained content. Their question and exclusions are the Epistemic scope above; see SRC-1, SRC-2 and SRC-3. The knowledge/personalization claim is CLM-1; CLM-2 reports results outside the runtime boundary; CLM-3 conflicts with the inspected additive branch. Provider reasoning, deployed candidate instances and evaluation traces are missing, preventing semantic fidelity, observed acceptance and improved-capacity conclusions. The analysis does not infer that inaccessible reasoning contains no criticism.

#### 2. Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| OBJ-7 | Caller-supplied message propositions | Retained raw knowledge | SRC-1 `mem0/memory/main.py`; see RTE-4 | Source truth unknown; prior vision transformation separately bounded |
| OBJ-8 | Generated factual statements | Personal memory for future context | SRC-1 `mem0/memory/main.py`; see RTE-1 | No candidate instance establishes preservation, entailment or ampliation |
| OBJ-2 | Earlier normalized utterances | Reference-resolution context | SRC-1 `mem0/memory/storage.py`; see RTE-1 | Conversation retention does not verify its propositions |
| OBJ-3 | Summary of actions, outputs, progress and context | Task continuation | SRC-2 `mem0/configs/prompts.py`; see RTE-3 | Prompted preservation is not checked fidelity |
| OBJ-4 | None as an asserted world relation; entity labels and links index memory records | Access ranking | SRC-1 `mem0/memory/main.py`; see RTE-5 | Similarity-based association is not entity-truth validation |
| OBJ-5 | Recorded old/new text and mutation events | Inspection history | SRC-1 `mem0/memory/storage.py`; see RTE-6 | Event retention supplies no factual reason or cross-store atomicity |
| OBJ-6 | None as a candidate proposition; access representations and metadata | Ranking and selection | SRC-1 `mem0/vector_stores/qdrant.py`; see RTE-2 | Model representation semantics and optional providers remain uninspected |
| OBJ-9 | Generated image descriptions | Text input for later memory writes | SRC-1 `mem0/memory/utils.py`; see RTE-8 | No grounded image/output instance or adequacy check |

#### 3. Authority-route ledger

Each row separates function from architecture; generic progression stays on the canonical route. All implementation rows are static, with no observed candidate outcome. Behavioral paths below identify consumer, channel, force and horizon directly.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTE-4 | content transformation | implemented | OBJ-7 | truth-apt transformation: acquisition/import | Normalized caller text | Structural message eligibility | Raw add, after optional preprocessing | Text accepted or skipped | Permits embedding/storage | Warrant of source propositions unknown | Creates durable payload | Later extraction; context text; advisory; later calls | SRC-1 `mem0/memory/main.py` | none | none | Imports claims without validating them |
| RTE-1 | content transformation | implemented | OBJ-8 | truth-apt transformation: indeterminate | Statements about conversation | Configured model under additive prompt | Inferred add | Generated text or empty/invalid response | Proposes storage candidates | No verified entailment or source fidelity | Supplies candidate list to admission | Extraction model; prior-text prompt; advisory; current/additional calls | SRC-1 `mem0/memory/main.py` | CLM-1, CLM-3 | Additive branch contradicts CLM-3 | Faithful reshaping, entailed derivation and ampliation remain possible |
| RTE-1 | check/evidence production | implemented | OBJ-8 | no content change | JSON shape, nonempty text, embeddings and exact hashes | Parser, embedding availability and MD5 comparisons; structural domain | Before persistence | Eligible or filtered records | Structural gate | Only parseability, embedding availability and bounded exact duplicate checks | Blocks malformed/unembeddable/duplicate candidates | Writer; code conditions; enforcing; this write | SRC-1 `mem0/memory/main.py` | CLM-1 | Structural checks do not warrant factual truth | Model hallucination and contradiction unchecked by these conditions |
| RTE-1 | disposition/acceptance | implemented | OBJ-8 | no content change | Storage admission | CPU record construction and successful store calls | After preceding checks | Acknowledged records survive | Operational admission | No epistemic acceptance established | Commits eligible text for later use | Writer; accepted record batch; permissive; later calls | SRC-1 `mem0/memory/main.py` | CLM-1 | Storage admission is not discovery-lifecycle acceptance | Backend acknowledgements are external contract |
| RTE-1 | retention | implemented | OBJ-8, OBJ-2, OBJ-5 | no content change | Accepted payload and recent messages/history | Store operations, bounded SQLite retention | During add | Stored data or partial failures | Durable availability and context replacement | Retention adds no truth warrant | Allows later context and inspection | Future selectors; persisted rows; permissive; across calls | SRC-1 `mem0/memory/main.py` | CLM-1 | No acceptance-to-integration inference | No shared cross-store transaction established |
| RTE-3 | content transformation | implemented | OBJ-3 | truth-apt transformation: indeterminate | Execution-history summary | Model under procedural/custom prompt | Procedural add | Nonempty summary or error | Proposes continuation content | Preservation intended, not verified | Candidate summary reaches write gate | Summarizer; message history; advisory; current generation | SRC-1 `mem0/memory/main.py` | CLM-1 | Summary label does not establish fidelity | No input/output pair to classify semantic relation |
| RTE-3 | check/evidence production | implemented | OBJ-3 | no content change | Nonempty response and metadata | Python conditions; structural domain | After generation | Valid shape or exception | Blocks empty summary | No check of completeness or verbatimness | Permits embedding and insert | Writer; response validation; enforcing; this write | SRC-1 `mem0/memory/main.py` | none | none | Does not assess task adequacy |
| RTE-3 | retention | implemented | OBJ-3, OBJ-5 | no content change | Generated summary | _create_memory and backing stores | After structural admission | New payload/history | Availability for later reads | No epistemic acceptance established | Enables ordinary later retrieval | Extraction/caller; vector payload; advisory; later calls | SRC-1 `mem0/memory/main.py` | CLM-1 | Retention not lifecycle integration | Actual continuation unobserved |
| RTE-8 | content transformation | implemented | OBJ-9 | truth-apt transformation: indeterminate | Image/list-message meaning | Configured model when vision enabled | Before general raw/inferred add | Description or exception; text-only fallback when disabled | Replaces input presented downstream | Grounding unknown | Changes later source text | Memory writer; normalized text; advisory; this and later retained calls | SRC-1 `mem0/memory/utils.py` | none | none | Description fidelity and provider internals uninspected |
| RTE-5 | behavior/policy adaptation | implemented | OBJ-4, OBJ-6 | non-truth-apt policy/content update: access associations | Entity identity/link selection | Normalization, embedding similarity, exact/threshold matching | After successful writes or changed-text update | Merge/update/insert associations | Changes future ranking | Similarity only, no world-truth license | Changes boost eligibility | Search scorer; linked IDs/vectors; ranking; subsequent search | SRC-1 `mem0/memory/main.py` | CLM-1 | No truth-validated graph inference | Index errors/cleanup failures possible |
| RTE-6 | disposition/acceptance | implemented | OBJ-7, OBJ-8, OBJ-3, OBJ-6 | truth-apt transformation: indeterminate | Caller replacement or withdrawal | Caller chooses; code checks shape, identity and date | Explicit maintenance | Changed/deleted text or visibility | Mutates live reliance | Caller rationale and truth criterion unknown | Allows replacement/removal from selected channels | Future selectors; payload/metadata; permissive; later calls | SRC-1 `mem0/memory/main.py` | none | Manual edit is not evidence-consuming factual acceptance | Expiration does not cover every read-back |
| RTE-6 | lineage/freshness/recovery | implemented | OBJ-5 | truth-apt transformation: acquisition/import | Old/new text and event | Mutation history writes | After operations | Historical event rows | Supports caller inspection | Records mutation, not its truth or justification | Enables history reads; no automatic rollback | Inspector; history API; advisory; until reset | SRC-1 `mem0/memory/storage.py` | none | History is not a transaction guarantee | Partial cross-store outcomes possible |
| RTE-2 | operational admission/selection/consumption | implemented | OBJ-7, OBJ-8, OBJ-3, OBJ-4, OBJ-6 | no content change | Search candidate relevance/visibility | Semantic threshold, scoring, optional reranker and expiry | Requested search | Ranked payloads | Selection/ranking, not verification | Relevance score licenses no factual truth | Allows selected facts to reach caller | Requesting caller; result dictionary; ranking/advisory; this response | SRC-1 `mem0/utils/scoring.py` | CLM-1 | Retrieval not epistemic acceptance | Caller/model dependence unobserved |
| RTE-7 | operational admission/selection/consumption | doctrine only | OBJ-7, OBJ-8, OBJ-3 | no content change | Answer context | Documented top-three caller search and prompt assembly | External example chat loop | Answer intended | Afforded knowledge delivery | No correctness criterion checked | Can influence external answer generation | Answer model; system-message memory text; advisory; current answer | SRC-2 `README.md` | CLM-1 | Consumer affordance not deployment observation | Enclosing runtime excluded |
| RTE-7 | operational admission/selection/consumption | implemented | OBJ-7, OBJ-8, OBJ-3, OBJ-5 | no content change | Requested ID/scope/history inspection | API selection by ID or scope; no factual evaluator | Caller inspection call | Stored payload/history or missing result | Makes selected data available | No new truth warrant | Returns data to requesting inspector | Caller; get/get_all/history response; advisory; this request | SRC-1 `mem0/memory/main.py` | none | Inspection route distinguished from documented external answer assembly | Subsequent caller reliance uninspected |

The maintenance row covers text-changing edits; its expiry/identity metadata changes are separately non-truth-apt access updates under RTE-6. The history row acquires operation records rather than establishing their content as true. None of these operational gates supplies an expected-answer oracle.

#### 4. Per-object lifecycle disposition

| candidate object ID | relevant route IDs | transformation/disposition | applicable route and warrant or remaining possibilities | missing evidence/limit |
|---|---|---|---|---|
| OBJ-7 | RTE-4, RTE-8 | acquisition/import after any upstream normalization; discovery lifecycle: not applicable to imported text | Retains caller assertions with unknown source warrant | Vision-generated portions inherit OBJ-9 indeterminacy |
| OBJ-8 | RTE-1 | indeterminate | Non-ampliative reshaping, entailed derivation or ampliative conjecture remain possible; trace lineage is implementation-level, not a retained justification; structural gates and retention are implemented | Need candidate-linked inputs/outputs and meaning checks to decide relation; no epistemic acceptance established |
| OBJ-2 | RTE-1, RTE-8 | acquisition/import of normalized messages; discovery lifecycle: not applicable to copied rows | Keeps recent utterances as context with unknown original warrant | Earlier generated descriptions retain OBJ-9 limits; eviction loses full history |
| OBJ-3 | RTE-3 | indeterminate | Intended non-ampliative preservation; semantic rewriting, entailed derivation or ampliation possible in model output; structural check/retention implemented | Need actual trace/summary comparison and adequacy test; no accepted scope established |
| OBJ-5 | RTE-6 | acquisition/import of operation history; discovery lifecycle: not applicable | Preserves before/after text and events, not their reasons | No candidate-linked audit of multi-store effect |
| OBJ-9 | RTE-8 | indeterminate | Faithful description, entailed interpretation or unsupported ampliation remain possible; forwarded to raw/inferred writers | Need image/output and grounding assessment; no preserved epistemic warrant established |

No lifecycle record for OBJ-4: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-5.

No lifecycle record for OBJ-6: no candidate truth-apt output for this object; relevant direct-adaptation or update routes: RTE-5, RTE-6.

The object OBJ-1 is the superseded aggregate; its operative parts are OBJ-7 and OBJ-8. No observed candidate instance was supplied for any generated object. Since ampliation is not established for a specific output, the six-phase ampliative lifecycle is not assigned. This is indeterminacy about transformation, not evidence that ampliative candidates are absent. Retention and operational use are recorded separately; no post-acceptance integration is established.

#### 5. System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| CLM-1 | Personalized memory and continuous learning | SRC-2 `README.md`, doctrine/design | Memory and continuation objectives; external chat example | RTE-1, RTE-2, RTE-3, RTE-5 | None retained | None; no controlled comparison | Durable trace-derived content and internal read-back are wired; personalization consumer afforded | Improved capacity, factual accuracy and attributable benefit unestablished |
| CLM-2 | Benchmark improvements | SRC-3 `README.md`, reported operation | Report explicitly scoped to managed platform | No included route establishes measured result | No inspected run trace | No inspected design; platform excluded | Attributed platform report only | Cannot transfer numbers or gain expectation to OSS |
| CLM-3 | infer=True decides add/update/delete | SRC-2 `mem0/memory/main.py`, doctrine/design | API docstring | RTE-1 is additive; RTE-6 is explicit maintenance | None retained | None | Separate add and manual maintenance mechanisms | Docstring does not describe current inferred branch |

#### 6. Bounded conclusion

The scoped routes acquire caller content, generate fact and continuation text, retain that text and derived access structures, and supply later extraction or requesting callers. JSON, hash, expiry and relevance checks govern operation in their own narrow domains. They neither validate extracted propositions nor establish that a summary preserves an execution history. Explicit edits and history make revision inspectable, but do not require a stated criticism or evidence-consuming factual acceptance.

The strongest retained loop is automatic trace-derived memory with later internal contextual use. Its implementation supports the comparison's trace-learning classification. Actual semantic dependence, improved capacity for future action and any causal benefit remain uninspected. The route evidence supplies no accepted ampliative claim or post-acceptance lifecycle integration to report, and no conclusion about opaque provider reasoning. These limits belong to the assessed routes, not a system-wide epistemic grade.

## Reconciliation

The fresh specialist report's run/source/boundary, complete status, input hash and instruction hash were checked against the frozen commission. Exact report bytes are bound in Run identity. No prior analysis was read. The specialist reports worker-model unknown because its precise runtime model was not exposed; the launch identity was /root/mem0/memory, requested gpt-6-astra with medium reasoning and no conversation fork.

Mappings: MEM-CMP-1 → CMP-5; MEM-OBJ-1 → OBJ-3; MEM-OBJ-2 → OBJ-4; MEM-OBJ-3 → OBJ-5; MEM-OBJ-4 → OBJ-6; MEM-OBJ-5 → OBJ-8; MEM-OBJ-6 → OBJ-7; MEM-RTE-1 → RTE-4; MEM-RTE-2 → RTE-5; MEM-RTE-3 → RTE-6; MEM-RTE-4 → RTE-7; MEM-RTE-5 → RTE-8; MEM-CLM-1 merged into CLM-1. Exact identifier tokens were mapped; every target has one declaration. Local labels appear here only as mapping provenance.

Amendment attached to OBJ-1: its original raw/extracted aggregate is superseded by OBJ-7 and OBJ-8, which preserve separate producers, checks and semantic relations. The specialist made this split and revised profile references before final hashing. No earlier canonical ID changed referent. Procedural text OBJ-3 and transient vision description OBJ-9 remain distinct. The latter makes the report's existing RTE-8 content edge explicit for the epistemic inventory; it adds no accumulated-memory classification.

The ADD-only finding corrects CLM-3; the procedural finding preserves continuation as an afforded role and internal extraction read-back as wired. CMP-5's assembly includes models already inventoried as CMP-1, CMP-2 and CMP-4, and is not a second model inventory. The memory profile is the specialist's profile with canonical token mapping only. Its partial coverage, per-value bases, rationale and faithfulness uncertainty were preserved. Source quotations remain unchanged, once on their supporting canonical records. No citation repair was necessary.

Runtime evidence and sparse epistemic overlays annotate these same routes. Structural admission, output retention and epistemic acceptance remain distinct. There are no unresolved substantive conflicts. Agreement on additive ingestion and unobserved benefit arose from separate coordinator/source and specialist/source inspection; this convergence does not upgrade the evidence tier or certify the integrated artifact.

## Bounded synthesis

Evidence basis: source code and source-native prompts/documentation at the pinned revision, inspected 2026-09-27; no system run or causal experiment. Mem0's synchronous OSS subsystem is a caller-driven memory computation. Its strongest supported contribution is a wired durable trace-to-context loop: automatic facts, procedural summaries and access structures can affect later extraction and retrieval. Whether that loop improves future capacity remains uninspected.

A caller submits messages and scope. General inferred ingestion assembles retained context, generates candidate facts, rejects structurally ineligible/duplicate/unpersisted items, then appends new payloads. Raw and procedural modes change the producer and bypass portions of that pipeline. This is why a generic claim that add revises outdated knowledge is too broad: explicit maintenance is a separate route, and retained shifted preferences can coexist. The epistemic result is candidate generation and operational admission, with transformation fidelity undetermined.

On a later call, scoped recent messages and embedding-selected prior text can be supplied automatically to extraction. Requested search instead returns a semantic candidate pool whose order can incorporate lexical and entity signals. Procedural summaries share ordinary retrieval and internal context routes; their prompt affords task continuation without proving a resumed agent actually uses them. Count limits, optional dependencies and partial provider coverage bound both context and comparison claims.

Maintenance exposes individually addressable replacement and removal, with old/new text retained in history. Expiration only hides selected public reads; it does not withdraw internal extraction context or direct get. Partial multi-store effects and best-effort entity cleanup prevent a universal forgetting or rollback claim. For a developer needing remembered conversational context, these are operative distinctions. For one requiring verified factual revision, full withdrawal or proven answer improvement, the inspected evidence is insufficient.

Under the [theory-builder definition](../../../../notes/definitions/theory-builder.md), localized content and shipped guidance are present (condition 1: wired at that minimum, with actual theory content instance-dependent); guidance delivery and content-sensitive selector application are wired, while model-generated semantic dependence remains uninspected (condition 2 is not generalized beyond those mechanisms). Content-directed criticism of retained theories is uninspected (condition 3), and criticism-driven iteration is uninspected (condition 4). Thus the selected boundary does not establish full theory-builder membership. Addressability reaches individual payloads and metadata; persistence reaches subsequent calls under surviving stores. Neither establishes criticism by itself.

Learning as improved capacity: uninspected, despite the narrower wired trace-learning comparison value. Reflection: uninspected; stored user/task descriptions do not establish a causally connected self-representation of Mem0's own operation. Autonomous execution of selected generation/admission steps: wired; autonomous theory-builder qualification: uninspected. Self-improvement as operative evidence-responsive improvement: uninspected. These are separate findings, not grades. The broad continuous-learning claim is supported only to the narrower extent of retained trace-derived material and later use afforded or wired here.

Candidate-linked input/output checks would resolve semantic fidelity; controlled recall interventions would test dependence and benefit; deployed provider identities would resolve component fixity; a complete consumer-by-consumer withdrawal audit would establish stronger expiration guarantees. Managed-platform performance requires its own pinned evidence rather than transfer from the README report.

## Limitations

| limitation | affected source, record, or route IDs | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| Static implementation only | SRC-1, RTE-1, RTE-2, RTE-3 | Pinned synchronous API and helpers | Successful activation, fidelity, benefit and causal attribution | Retained candidate-linked execution and controlled intervention |
| Managed platform excluded | SRC-3, CLM-2 | README qualification only | OSS benchmark performance or managed architecture | Separately pinned platform/evaluation evidence |
| Configured providers and optional ranking | CMP-1, CMP-2, CMP-3, CMP-4 | Default adapters, loader and call boundaries | Exact deployed weights, full-signal availability or provider equivalence | Deployment/model identity and provider-specific analysis |
| Enclosing consumer and security boundary excluded | RTE-2 | Caller API and README example | Actual host prompt authority, authentication or task success | Pinned integration and deployed grant/isolation evidence |
| Opaque model semantics | RTE-1, RTE-3 | Prompts and calls | Entailment, criticism, epistemic acceptance or learned capability | Candidate input/output pairs and retained evaluation records |
| Scope and withdrawal limits | RTE-1, RTE-3, RTE-6, RTE-8 | Synchronous memory alternatives | Universal expiration, full history, continuation fidelity or all-provider classifications | Provider-specific routes and retained executions; preservation tests and full-consumer withdrawal audit |

## Verification and blockers

### Semantic verification

Checked the integrated records, not only the specialist report. OBJ-1 remains a superseded aggregate; OBJ-7 and OBJ-8 separate raw and extracted propositions. OBJ-2, OBJ-3, OBJ-4, OBJ-5 and OBJ-6 retain distinct content/access/history roles; OBJ-9 is transient preprocessing and is not counted as another durable storage substrate.

Checked every scoped trace-fed write: RTE-1 facts, RTE-3 procedural summaries, RTE-5 entity/access structures, and RTE-8 descriptions feeding downstream writes. The profile retains natural-language and symbolic distilled forms, online positive evidence, partial source/horizon coverage, and wired trace-learning without upgrading it to benefit. RTE-4 raw retention and OBJ-2 raw history alone do not supply automatic distillation. No qualifying procedural route was omitted merely because its purpose is preservation.

Checked push signals at their actual consumer: RTE-1 automatically selects exact-scope recent messages and embedding-matched prior payloads for the extraction LLM. Identifier and inferred-embedding values have wired witnesses. RTE-2's hybrid search is caller pull; it adds no lexical push signal. RTE-7's external answer use remains afforded. All scoped API read/write alternatives and conditional reranking/vision paths carry explicit limits; optional providers prevent complete value sets on affected axes.

Checked every route's immediate return, later consumer, selection, provider/delegated visibility, expiry/invalidation and activation limits. Compared admission and check functions separately from truth warrant. Each epistemic object has an indeterminate, acquisition or no-candidate disposition; no implementation row was upgraded to observed candidate acceptance. The ADD-only correction is bounded by ABS-1, not projected to all maintenance. Model-component fixity, decision roles, answer-oracle limits, guidance and theory conditions remain separate from profile trace learning.

Checked canonical mappings for uniqueness and source paths for pinned attribution. The source and input identities agree; the report digest is exact. Quoted passages are retained on canonical records, with generated source locations unchanged. No prior analysis, live deployment, external benchmark or inferred test result supports a conclusion.

### Deterministic validation

`commonplace-validate --full kb/reports/state/agentic-system-analysis/AAS-2026-09-27-mem0-04/result.md` passed cleanly, with no warnings or failures. The final exact bytes are validated again before candidate generation; publication independently validates the complete source-bound bundle.

### Blockers

none
