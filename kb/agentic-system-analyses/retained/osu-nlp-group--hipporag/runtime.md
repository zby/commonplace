---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "HippoRAG runtime baseline: retained document indexing, graph/dense retrieval, QA, iterative retrieval and MCP entry paths at the frozen revision."
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
---

# HippoRAG runtime report

## Runtime account

### Scope and evidence

HippoRAG is a document-memory computation with shipped Python and MCP callers, not the enclosing agent that chooses arbitrary tools. This account uses SRC-1 implementation and doctrine/design at the boundary's frozen commit. No target code was executed. The integration lifecycle is an executable specification, not an observed trace. Operation, actual prompt compliance, answer benefit and deployment isolation remain uninspected. All declarations below are new runtime referents; no peer runtime, memory, epistemic or workflow records were supplied for comparison.

Added inspection beyond the boundary's initial scope includes `src/hipporag/utils/state_utils.py`, `src/hipporag/utils/qa_utils.py`, `src/hipporag/llm/__init__.py`, `src/hipporag/llm/openai_gpt.py`, `src/hipporag/llm/vllm_offline.py`, `src/hipporag/llm/transformers_offline.py`, `src/hipporag/embedding_model/OpenAI.py`, `src/hipporag/embedding_model/NVEmbedV2.py`, and both offline OpenIE implementations. These supply implementation evidence, not additional sources or execution evidence. Other provider adapters, remote vector-store implementations, bulk fixtures and dataset contents remain uninspected in this member; conclusions below do not require their equivalence to the default paths.

### Ordinary invocation and work ownership

The shipped `main.py` driver supplies the principal and initial decisions: a dataset name, method, provider/model configuration and rebuild flags. It reads corpus and question JSON, constructs title-plus-text documents, extracts gold answers/supporting documents, constructs `BaseConfig`, opens the selected RAG object, indexes, and invokes `rag_qa`. The library owns progression after these calls; there is no model-selected general action dispatcher in this inspected flow. SRC-1: `main.py`.

> with rag_class(global_config=config) as rag:
>     rag.index(docs)
>     rag.rag_qa(queries=queries, gold_docs=gold_docs, gold_answers=gold_answers)
> --- `main.py`

Initialization selects or accepts injected extraction, QA, embedding and preprocessing components, makes a model-labelled working directory, opens stores and graph state, and checks the manifest. Default preprocessing keeps one chunk per document. Document strings receive content-hash identities; optional `source_id` is metadata, not the passage primary key. Extraction supplies NER then relation triples. Code normalizes triples, embeds passages/entities/facts, creates source-aware graph edges and synonym edges, and saves graph state. The index call returns no substantive result; MCP wraps it with counts. [RT-RTE-index-state](#rt-rte-index-state) owns this admission route; [RT-OBJ-index-manifest](#rt-obj-index-manifest) separates symbolic compatibility policy from the retained content. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/preprocessing.py`, `src/hipporag/embedding_store.py`.

On a normal string question, `rag_qa` invokes retrieval. Preparation checks graph/store identity and OpenIE coverage and materializes arrays and reverse mappings. Query embeddings score facts; a model-backed filter selects among top candidate triples. With selected facts, code weights subject/object nodes and dense passage seeds, then runs personalized PageRank on an undirected projection. Without selected facts, code uses dense passage results. The selected original passage texts and metadata become `QuerySolution` values. QA receives only the first `qa_top_k` passages, the question and shipped examples/instructions; it does not receive the full graph or all facts. It returns model text, metadata and the mutated query solutions. Answer extraction splits at `Answer:` and otherwise uses the raw response. [RT-RTE-retrieve-answer](#rt-rte-retrieve-answer) records the decisions and oracle boundary. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/rerank.py`.

> retrieved_passages = query_solution.docs[:self.global_config.qa_top_k]
> --- `src/hipporag/HippoRAG.py`

The benchmark mode compares selected passages with gold supporting documents and answers with supplied aliases using recall, exact match and F1. These are external references supplied by the driver, not a model's judgment of its own correctness and not an admission gate on indexed knowledge. In open library/MCP requests, those references need not exist. The driver logs scores rather than using them to revise the pipeline. SRC-1: `main.py`, `src/hipporag/HippoRAG.py`.

### Four forcing cases and alternate paths

1. **Fact-filter failure or bypass.** Retrieval is not unconditionally graph-based and is not unconditionally free of generative-model calls. The normal graph route invokes the extraction LLM for filtering. An exception, no facts, or nonpositive `linking_top_k` produces an empty selection and dense fallback. The filter maps generated triples to candidate strings using nearest matching with cutoff zero; it constrains the returned items to candidates but does not prove their relevance. Direct DPR methods and the StandardRAG driver bypass this filter. A supplied `QuerySolution` bypasses retrieval altogether. These cases refute a universal graph or recognition guarantee, while leaving the normal implementation intact. SRC-1: `src/hipporag/rerank.py`, `src/hipporag/HippoRAG.py`, `src/hipporag/StandardRAG.py`; [RT-RTE-retrieve-answer](#rt-rte-retrieve-answer), [RT-RTE-standard-rag](#rt-rte-standard-rag).

2. **Extraction error and offline staging.** Online extraction has separate NER and triple calls and raises at the batch boundary when either stage records errors. It is not simply one model call per new passage, despite skill guidance. The vLLM `offline` mode saves extraction state and deliberately raises to require a later online indexing phase; it is not ordinary end-to-end QA. `Transformers-offline` instead participates in the indexing flow. Both offline parsers can log parse errors and emit empty results without the online error metadata. Therefore online fail-fast behavior cannot be extended to all modes. SRC-1: `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/information_extraction/openie_vllm_offline.py`, `src/hipporag/information_extraction/openie_transformers_offline.py`, `src/hipporag/HippoRAG.py`; [RT-RTE-offline-extraction](#rt-rte-offline-extraction).

3. **Compatibility versus partial writes.** The manifest rejects incompatible recorded configuration and retrieval preparation checks graph IDs and passage/OpenIE coverage. But indexing first writes passage embeddings and metadata, then extracts and writes OpenIE, then derives other stores and graph. These checks do not make the complete operation transactional. An extraction failure can occur after passage persistence. Recovery is explicit reuse/retry or authorized rebuild/fresh directory, not a demonstrated whole-index rollback. The special offline-to-online producer transition is allowed; identical model names/endpoints also do not pin the remote weights. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/state_utils.py`; [RT-CLM-state-compatibility](#rt-clm-state-compatibility).

4. **MCP read-only and concurrency scope.** `--read_only` omits index/delete registration in that server. It does not disable the library's mutation APIs, prevent response-cache writes, impose per-content approval, or establish a read-only filesystem. A single worker serializes operations on one service instance; separate server processes and direct library users do not acquire that queue. Stdio and HTTP are shipped paths, with an explicit warning about unauthenticated nonlocal writable HTTP. Host callbacks and plugin instructions are outside that code-level enforcement point. SRC-1: `src/hipporag/mcp_server.py`, `src/hipporag/llm/openai_gpt.py`; [RT-RTE-mcp-tools](#rt-rte-mcp-tools).

IRCoT is an additional bounded retrieval/reasoning loop, not a separate autonomous executor. Code alternates retrieval and a QA-model thought, stops on a literal marker or step limit, and merges passages by maximum score before final QA. Previous thoughts and selected passages are passed by value into each thought prompt. No sub-agent frame or host-context compaction is implemented by this loop. [RT-RTE-ircot-retrieval](#rt-rte-ircot-retrieval) identifies its state and termination. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/qa_utils.py`.

### Effects, grants, controls and guarantees

The Python capability surface includes local persistence, configured model/embedding network calls, optional remote vector stores, injected Python components and provider-specific local engines. Injection is arbitrary caller-supplied Python, not a model-authorized tool grant. Default online calls request text completions; the inspected orchestration consumes text and does not dispatch provider tool calls. This observation does not bound arbitrary injected implementations. The plugin's `uvx` launcher installs from an unpinned Git reference; that is a host installation mechanism, not an internal improvement loop. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/llm/openai_gpt.py`, `src/hipporag/utils/state_utils.py`, `plugins/hipporag/.claude-plugin/plugin.json`.

The actual grant set is unknown: credentials, endpoint permissions, filesystem rights and host tool approvals are deployment choices. Local NVEmbed loading sets `trust_remote_code`; this further prevents interpreting model choice as an isolation boundary. No deployed sandbox or authenticating proxy was supplied. [RT-CMP-extraction-llm](#rt-cmp-extraction-llm), [RT-CMP-qa-llm](#rt-cmp-qa-llm) and [RT-CMP-embedding-model](#rt-cmp-embedding-model) separate model inference from retained-state change. SRC-1: `src/hipporag/embedding_model/NVEmbedV2.py`, `src/hipporag/mcp_server.py`.

| Guarantee | Owner and enforcement point | Strength and covered paths | Alternate paths / required external contract | Separate statuses |
| --- | --- | --- | --- | --- |
| Recorded index configuration is compatible | HippoRAG initialization and manifest helper; retrieval preparation checks identities | invariant over the checked fields and checked API path, not content truth | Offline staging has different initialization; direct file mutation and endpoint drift are not detected as weight changes. Requires honest producer identity, store APIs and filesystem semantics. | implementation conclusion status: wired; operation conclusion status: uninspected |
| One service operation at a time | `HippoRAGService` single-worker executor | invariant within one service queue | Direct library calls, other processes and external stores require their own coordination. Internal extraction still uses multiple workers. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Writable tools not exposed under read-only | `create_server` conditional registration | invariant over index/delete registration in that server | Direct APIs, local caches and host filesystem actions are outside it; requires MCP to expose registered tools as specified. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Cost/deletion confirmation | Plugin skill interpreted by the enclosing agent | policy, not a server authorization check | Python and MCP callers can submit writes directly; requires host adherence and user interaction. | guidance conclusion status: claimed; operation conclusion status: uninspected |
| Grounded, useful answer | Selected-passage QA prompt and model | best effort, no semantic correctness gate | Caller-supplied solutions can bypass retrieval; model compliance, passage quality and external inference behavior remain required. | implementation conclusion status: wired; benefit conclusion status: uninspected |

Recovery and observability are local, not universal reliability guarantees. Online extraction reports error metadata and fails batches; reranking instead catches errors and falls back. QA parsing tolerates missing answer delimiters. OpenAI adapters enforce text/usage response shape, use configured retries/timeouts, and retain response/usage metadata and cached results. MCP converts operation exceptions to tool errors and logs them; failed warm-up can be retried on the first call because instance construction remains lazy. Timers and token counters supply instrumentation, not measured performance here. SRC-1: `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/rerank.py`, `src/hipporag/llm/openai_gpt.py`, `src/hipporag/embedding_model/OpenAI.py`, `src/hipporag/mcp_server.py`.

Changes to retained knowledge are admitted by the index/delete route. Configuration and injected producers change behavior on caller construction; prompt files and a configured DSPy prompt JSON supply static guidance, not runtime prompt optimization. The plugin prescribes refresh by delete then index. No inspected route uses benchmark outcomes to automatically revise product code, capabilities or production machinery. That last statement is limited to the traced driver, core lifecycle, filter and MCP/skill paths, not a repository-wide absence finding. Memory revision details remain for the memory analyst. SRC-1: `main.py`, `src/hipporag/HippoRAG.py`, `src/hipporag/rerank.py`, `plugins/hipporag/skills/hipporag-memory/SKILL.md`.

## Shared records

### Components

#### RT-CMP-extraction-llm
Label: Extraction LLM

Source-native identity: `extraction_llm`; default aliases `llm_model`, also used by `DSPyFilter`. Representational form: distributed-parametric model accessed through text inference; storage substrate: remote provider or local engine, with response caches separate from weights. Online routing selects OpenAI-compatible, gateway, Bedrock or Transformers adapters by configuration; injection can replace this implementation. Parameters are not updated by the inspected extraction/filter orchestration. Exact weights are not pinned by model name, endpoint or explicit index identity; mutable remote endpoints can resolve to another model. Provider internal mutability is uninspected; injected implementations remain caller-defined. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/llm/__init__.py`, `src/hipporag/llm/openai_gpt.py`, `src/hipporag/rerank.py`.

> self.llm_infer_fn = hipporag.extraction_llm.infer
> --- `src/hipporag/rerank.py`

#### RT-CMP-qa-llm
Label: QA LLM

Source-native identity: `qa_llm`, defaults to the shared model but may be separately injected. This is a distinct operative role, not necessarily a distinct weight set. Representational form: distributed-parametric; substrate: external service or local model. It produces answer text and optional IRCoT thoughts. No parameter update is wired by these callers; exact weight version is not enforced, and a remote deployment can change resolution. Arbitrary injected model behavior and inaccessible provider internals remain uninspected. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/qa_utils.py`, `src/hipporag/llm/openai_gpt.py`.

> self.qa_llm: BaseLLM = qa_llm or self.llm_model
> --- `src/hipporag/HippoRAG.py`

#### RT-CMP-embedding-model
Label: Embedding model

Source-native identity: `embedding_model`; distributed-parametric encoder producing dense arrays. Substrate: configured local model or remote inference service; output vectors persist separately in stores. Parameters are not changed by inspected encoding/index/retrieval callers. Exact versions are not pinned by the inspected OpenAI or NVEmbed loaders; a remote model/deployment can resolve to new weights, and local model names do not supply immutable revisions. NVEmbed enables remote model code. The driver defaults to NVEmbed; the plugin defaults to OpenAI embeddings. Other adapters are available but their internal fixity is uninspected here. SRC-1: `main.py`, `plugins/hipporag/.claude-plugin/plugin.json`, `src/hipporag/embedding_model/OpenAI.py`, `src/hipporag/embedding_model/NVEmbedV2.py`.

> response = self.client.embeddings.create(input=texts, model=self.request_model_name, encoding_format="float")
> --- `src/hipporag/embedding_model/OpenAI.py`

#### RT-CMP-vllm-offline
Label: vLLM offline extraction model

Source-native identity: `VLLMOffline.client`, a local vLLM `LLM` instance. Representational form: distributed-parametric; substrate: local loaded model/GPU resources managed by vLLM. The inspected wrapper generates text and contains no parameter-update operation. Its loader passes a model name without an immutable revision, so exact weights are not pinned; this route does not use a mutable inference endpoint, although model-name resolution at loading can change. vLLM internals and any spawned engine workers remain external. The loader enables remote code and configures tensor/pipeline parallelism; neither is an isolation guarantee. SRC-1: `src/hipporag/llm/vllm_offline.py`.

> max_model_len=max_model_len, quantization=kwargs.get('quantization', None), load_format=kwargs.get('load_format', 'auto'), trust_remote_code=True)
> --- `src/hipporag/llm/vllm_offline.py`

#### RT-CMP-transformers-offline
Label: Transformers offline extraction model

Source-native identity: `TransformersOffline.model`; may share an already loaded extraction model. Representational form: distributed-parametric; substrate: local loaded model, normally GPU-backed. The wrapper uses generation, not parameter updates. Exact weights are not pinned: `from_pretrained` receives a name without a revision. No mutable inference endpoint is used here; reloading a name or supplying a different shared model can change the resolved model. Third-party generation internals remain uninspected. SRC-1: `src/hipporag/llm/transformers_offline.py`, `src/hipporag/information_extraction/openie_transformers_offline.py`.

> self.model = kwargs.get("model") or AutoModelForCausalLM.from_pretrained(model_name, device_map='auto', torch_dtype=torch.bfloat16)
> --- `src/hipporag/llm/transformers_offline.py`

### Operative objects

#### RT-OBJ-index-manifest
Label: Index manifest

Source-native identity: `index_manifest.json` in the model-labelled working directory. Representational form: symbolic JSON fields compared by equality; substrate: local file with a file lock and temporary-file replacement. It records schema, embedding identity, producer classes/explicit identity, OpenIE provenance and graph construction configuration. It is not a content-correctness certificate or a model-weight digest. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/state_utils.py`.

> if stored_manifest != manifest and not (allow_empty_rewrite and not has_derived_state):
>     raise StateConsistencyError(f"Index schema/config mismatch in {manifest_path}. Use a fresh save_dir for a full rebuild.")
> --- `src/hipporag/utils/state_utils.py`

#### RT-OBJ-query-solution
Label: Query solution

Source-native identity: `QuerySolution` instances returned by retrieval and modified by QA. This record concerns the per-call result container, not the retained index. It holds natural-language question, passages, thoughts and answer; symbolic score/metadata/seed fields direct code consumption. Substrate: process memory and return payloads, with no general durable write in these methods. Passing it to `rag_qa` bypasses fresh retrieval; no proof of provenance is required there. SRC-1: `src/hipporag/HippoRAG.py`.

> if queries and not isinstance(queries[0], QuerySolution):
> --- `src/hipporag/HippoRAG.py:934-934`

### Routes

#### RT-RTE-index-state
Label: Index and delete retained state

Caller supplies documents or exact texts for deletion; HippoRAG code owns preprocessing, persistence and graph construction. Endpoint progression is caller → chunk store/metadata → model extraction → normalized entity/fact stores → graph/OpenIE state → later retrieval. Content hashes identify chunks; source metadata identifies caller provenance. Extraction prompts propose relations; code controls structural admission, identity checks and graph derivation. No per-relation human approval or truth oracle is required. Open requests and benchmark corpus ingestion use the same mechanism; missing/changed input or explicit rebuild flags trigger work, not a performance-driven improvement policy. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/embedding_store.py`, `src/hipporag/preprocessing.py`.

- Immediate return: `index`/`delete` return implicitly; MCP separately reports count changes.
- Later read-back: persisted passages, OpenIE, vectors, graph and metadata are opened by later instances and selected for retrieval; the shipped integration caller explicitly reopens before QA.
- Delegated visibility: extraction receives each passage, then its entity list; embedding providers receive texts. These are service calls, not independent agents granted write authority.
- Selection predicate: only missing passage hashes require new embeddings/extraction; derived entities/facts come from processed triples; deletion matches existing exact text and retains shared references.
- Invalidation or expiry: index/delete clear retrieval readiness; deletion removes source contributions and unreferenced objects; no time-based expiry is established in this route.
- Activation or effect: wired writes change later searchable state; actual later behavior change and improved capacity are unobserved.
- Evidence limits: source-level lifecycle and shipped reload caller only; no crash-recovery experiment, semantic validation or actual user-approval evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/rejection/recovery: the caller chooses documents and can request delete/rebuild. The extraction model proposes NER/triples; online error metadata causes batch rejection, while manifest/schema/provenance checks can veto incompatible construction. Passage/metadata writes precede extraction, so rejection need not restore the prior state. Re-extraction is blocked once derived entity/fact/graph state exists; a fresh directory or explicit graph rebuild is prescribed. Deletion requires provenance and preserves still-referenced triples/entities; no automatic rollback is shown. Guidance persists as shipped prompts, while passages and extracted structures persist as knowledge state. The transformation is not established as a theory-revision or learning mechanism. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/information_extraction/openie_openai.py`.

> self.chunk_embedding_store.insert_strings(chunk_texts)
> --- `src/hipporag/HippoRAG.py`

> failed_ner_chunk_ids = [result.chunk_id for result in ner_results_list if result.metadata.get("error")]
> if failed_ner_chunk_ids:
>     raise RuntimeError(f"NER failed for {len(failed_ner_chunk_ids)} chunk(s): {failed_ner_chunk_ids}")
> --- `src/hipporag/information_extraction/openie_openai.py`

> with HippoRAG(**kwargs) as reloaded_rag:
>     print(reloaded_rag.rag_qa(queries=QUERIES, gold_docs=GOLD_DOCS, gold_answers=ANSWERS)[-2:])
> --- `tests/integration/_shared.py`

#### RT-RTE-retrieve-answer
Label: Retrieve and answer

Endpoint progression: question → query vectors → scored candidate facts → model filter → PPR or dense ranking → selected original passages → QA text/result. Library code owns the next step. The filter model proposes candidate selection, nearest-string matching constrains returned triples to candidate items, and code selects fallback on empty output. QA-model text supplies the answer, not an authoritative acceptance decision. Plain requests have no expected-answer oracle. Benchmark mode uses caller-supplied gold passages/answers after generation; it does not feed these references into candidate admission or automatically revise the index. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/rerank.py`, `main.py`.

- Immediate return: passage solutions for retrieval; QA adds answer, raw response and metadata, and optionally aggregate evaluation scores.
- Later read-back: retrieves retained passages/derived structures admitted earlier; the OpenAI adapter can reuse persisted responses on matching requests. The route does not itself retain an answer as a document.
- Delegated visibility: encoder sees query; filter sees question and candidate facts; QA sees top passages, question and static template examples, not the entire retained corpus.
- Selection predicate: embedding similarity proposes top `linking_top_k` facts; model filter selects; code combines entity and dense passage weights for PPR, or uses DPR if no facts survive; QA slices to `qa_top_k`.
- Invalidation or expiry: mutation invalidates retrieval preparation; per-instance query caches are initialized in preparation; persistent response-cache identity depends on request parameters, not a verified provider-weight revision.
- Activation or effect: wired delivery affects the model input and selected results; model compliance, realized grounding and causal answer benefit are unobserved.
- Evidence limits: no successful run or experiment; direct `QuerySolution`, `qa`, `retrieve_dpr` and `rag_qa_dpr` are alternate paths that do not share normal fact selection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Working-context control is deterministic selection before each model call: full stored corpus stays out, only candidate triples reach filtering, and only a passage prefix reaches QA. This is external-material retrieval by value, not a pointer dereference or host turn compaction. Static prompt examples are not accumulated experience. Filter exceptions are caught and cause dense fallback; provider or QA failures are not universally converted into usable answers. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/rerank.py`.

> if len(top_k_facts) == 0:
>     logger.info('No facts found after reranking, return DPR results')
>     sorted_doc_ids, sorted_doc_scores = self.dense_passage_retrieval(query)
> --- `src/hipporag/HippoRAG.py`

> closest_matched_fact = difflib.get_close_matches(str(generated_fact), [str(i) for i in candidate_items], n=1, cutoff=0.0)[0]
> --- `src/hipporag/rerank.py`

#### RT-RTE-ircot-retrieval
Label: IRCoT iterative retrieval

Caller chooses `max_qa_steps`; library code owns iteration. Starting from ordinary retrieval, it sends ranked passages plus original question and previous thoughts to `qa_llm`, then uses the next thought as a new retrieval query. It merges duplicate passages by maximum score, stopping on the literal answer marker or the step budget. `answer_with_ircot` then invokes ordinary QA; final QA uses the query and passages rather than directly passing the thought list. This is bounded inference-time search, not admission of a revised method. Optional gold labels supply evaluation references only. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/utils/qa_utils.py`.

- Immediate return: merged passage solutions with thought lists, or final QA and optional evaluation results.
- Later read-back: reads the retained index each retrieval step; thoughts/merged scores are current-call state, with no durable thought admission in this loop.
- Delegated visibility: QA-model reasoning receives selected ranked passages, accumulated thoughts and original question; no independent worker identity or tool authority is created.
- Selection predicate: thoughts direct subsequent retrieval; code ranks merged documents by maximum observed retrieval score and selects the prompt prefix.
- Invalidation or expiry: current thoughts/merged maps end with the call; configured step limit and literal marker terminate the loop, not evidence of correctness.
- Activation or effect: model output is wired as the next query and can alter selection; actual activation and benefit have no execution evidence.
- Evidence limits: template availability is checked for multistep use; actual reasoning quality, marker reliability and comparative gain remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> thoughts.append(thought)
> if 'So the answer is:' in thought:
>     break
> --- `src/hipporag/HippoRAG.py`

> step_result = self.retrieve([thought], num_to_retrieve=num_to_retrieve)[0]
> --- `src/hipporag/HippoRAG.py`

#### RT-RTE-mcp-tools
Label: MCP service tools

MCP client triggers typed retrieve, QA, index, delete or statistics requests. `HippoRAGService` owns one lazily initialized instance and queues every operation on one thread. The enclosing host chooses tools; the server does not choose a next tool autonomously. Index/delete wrap [RT-RTE-index-state](#rt-rte-index-state); retrieval and QA wrap [RT-RTE-retrieve-answer](#rt-rte-retrieve-answer). The CLI fixes save directory, provider configuration, transport and read-only exposure at launch. SRC-1: `src/hipporag/mcp_server.py`.

- Immediate return: typed passages, QA answer/passages, index/delete counts or statistics; operation failures become `ToolError`.
- Later read-back: the service reuses its instance and configured retained index across calls; process restart can reopen the same saved index.
- Delegated visibility: the client receives selected texts, scores and metadata, not arbitrary server filesystem access through these tools; external inference services receive the underlying library requests.
- Selection predicate: host/client selects tool and arguments; read-only registration omits index/delete; retrieve `top_k` has a schema bound and empty indexes raise tool errors.
- Invalidation or expiry: shutdown closes the instance and waits for the executor; no cross-process queue or whole-store snapshot is established.
- Activation or effect: tool requests are wired to corresponding library operations; registration hints do not enforce content approval or filesystem isolation.
- Evidence limits: host approvals, actual transport deployment, authentication proxies and cross-process store behavior are unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is direct client submission followed by library checks. Any human approval is external or skill-guided, not an enforced server vote; the server can reject invalid/empty inputs and library errors. No answer oracle is used by these wrappers. Writable service mode admits knowledge changes; read-only mode withholds those tools but still initializes models/stores and can use response caches. Errors are reported rather than an automatic rollback. SRC-1: `src/hipporag/mcp_server.py`, `src/hipporag/llm/openai_gpt.py`.

> self._executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="hipporag")
> --- `src/hipporag/mcp_server.py`

> if not read_only:
>     @server.tool(
>         title="Index documents",
> --- `src/hipporag/mcp_server.py`

#### RT-RTE-offline-extraction
Label: Offline extraction modes

Configuration selects a local vLLM or Transformers extractor, using [RT-CMP-vllm-offline](#rt-cmp-vllm-offline) or [RT-CMP-transformers-offline](#rt-cmp-transformers-offline). Code owns batch NER then triple generation. In `offline` mode it writes OpenIE state and deliberately terminates with an instruction to run online indexing afterward; the provenance check explicitly allows that producer-mode transition. `Transformers-offline` is not this staging branch: it supplies extraction during normal indexing. These modes have different parsers/error handling, so they cannot inherit online batch rejection guarantees. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/information_extraction/openie_vllm_offline.py`, `src/hipporag/information_extraction/openie_transformers_offline.py`.

- Immediate return: offline staging raises after saving extraction state; Transformers-offline returns NER/triple dictionaries into indexing.
- Later read-back: persisted offline OpenIE can be consumed by a subsequent online index build after identity/provenance validation.
- Delegated visibility: local generation engines receive batch passages, extraction templates and generated entity lists; engine internals remain outside this inspection.
- Selection predicate: missing chunk keys choose extraction inputs; configuration chooses producer; parsing selects named-entity/triple fields.
- Invalidation or expiry: force flags and provenance identity govern reuse; explicit full re-extraction requires compatible empty/fresh derived state.
- Activation or effect: extraction state is wired into subsequent graph construction; actual successful phase transition and output accuracy remain unobserved.
- Evidence limits: inspected wrappers show parse failures becoming empty lists; local engine execution, exact weights and resource isolation were not observed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/recovery: models propose structures; wrappers parse and return them, while downstream code controls saved state and compatibility. No per-triple human veto or expected-answer oracle is present in these wrappers. The operator/caller must perform the online successor invocation for staged mode. Guidance is the same shipped extraction templates, not self-revised instructions. Persisted material is extracted knowledge with producer identity, not a method improvement. SRC-1: `src/hipporag/HippoRAG.py`, `src/hipporag/information_extraction/openie_vllm_offline.py`.

> raise RuntimeError("Offline OpenIE completed. Run indexing again with openie_mode='online' to build the graph.")
> --- `src/hipporag/HippoRAG.py`

> except Exception as e:
>     triples = []
>     logger.warning(f"Could not parse response from OpenIE: {e}")
> --- `src/hipporag/information_extraction/openie_vllm_offline.py`

#### RT-RTE-standard-rag
Label: StandardRAG dense baseline

`main.py --rag_type standard` chooses a separate shipped dense baseline, not the graph runtime under a different label. Caller submits documents; code embeds missing texts, invalidates retrieval objects and later ranks dense passage scores. The traced index/retrieve methods do not perform OpenIE or model fact filtering. QA/evaluation are exposed by the same driver interface. SRC-1: `main.py`, `src/hipporag/StandardRAG.py`.

- Immediate return: index/delete return implicitly; retrieval returns passage solutions and optional recall metrics; driver calls QA afterward.
- Later read-back: retained chunk embeddings/texts reopen for later dense retrieval; no graph/OpenIE write is required by the inspected index method.
- Delegated visibility: embedding provider receives documents/queries; generative QA is a later stage, not the dense retrieval selector.
- Selection predicate: text hashes skip existing documents; descending dense scores select the requested passage prefix.
- Invalidation or expiry: index/delete invalidate retrieval objects; delete removes requested existing text hashes.
- Activation or effect: wired change to searchable corpus and dense ranking, without observed outcome or superiority evidence.
- Evidence limits: baseline implementation is not an empirical comparison; alternate provider/backend internals and crash recovery remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission/recovery: caller supplies or deletes document texts, software admits embeddings, with no per-item human approval or truth oracle in these methods. Gold references belong to benchmark evaluation, not corpus admission. Reindex/delete are available; no atomic multi-operation undo is demonstrated. This route prevents extending graph-specific guarantees to the entire shipped method surface. SRC-1: `src/hipporag/StandardRAG.py`, `main.py`.

> self._invalidate_retrieval_objects()
> logger.info(f"Indexing Documents")
>
> self.chunk_embedding_store.insert_strings(docs)
> --- `src/hipporag/StandardRAG.py`

### Claims

#### RT-CLM-state-compatibility
Label: Recorded state compatibility

Claimed operation: initialization binds persisted index components to a producing configuration, and retrieval preparation rejects inconsistent graph/store/OpenIE identities. This is wired for inspected normal HippoRAG paths, not proof of semantic correctness, immutable provider weights or transactional knowledge admission. Owner: manifest helper and HippoRAG preparation. Enforcement: equality/provenance/ID checks; strength: invariant over checked fields at these call sites. Required external contracts: trustworthy producer identity and store/filesystem behavior. Offline staging and manually modified state need separate interpretation; one service queue does not make the entire persisted lifecycle atomic. SRC-1: `src/hipporag/utils/state_utils.py`, `src/hipporag/HippoRAG.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected

> if set(igraph_name_to_idx) != expected_node_ids:
>     raise StateConsistencyError("Graph vertex IDs do not match embedding store IDs.")
> --- `src/hipporag/HippoRAG.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-extraction-prompt
Label: Extraction prompt authority

Consumer: extraction model. Channel: shipped system/user/example messages plus passage/entity text. Force: natural-language instruction requesting RDF triples and pronoun resolution; code separately enforces parsing/structure and downstream identity. Horizon: each extraction invocation; derived triples persist for later search. The prompt is static guidance, not an automatically revised method. Actual compliance is unobserved. SRC-1: `src/hipporag/prompts/templates/triple_extraction.py`, `src/hipporag/information_extraction/openie_openai.py`.

> - Each triple should contain at least one, but preferably two, of the named entities in the list for each passage.
> - Clearly resolve pronouns to their specific names to maintain clarity.
> --- `src/hipporag/prompts/templates/triple_extraction.py`

#### RT-BAP-plugin-skills
Label: Plugin maintenance guidance

Consumer: enclosing Claude Code agent, not the server's index method. Channel: natural-language shipped skills. Force: host-interpreted policy to split documents, preserve provenance, confirm costly batches/deletions and refresh changed sources with delete then index. Horizon: host use across sessions against the persistent index. Host adherence, current permissions and whether skill content enters an actual model invocation are unobserved. This guidance admits knowledge changes via host tool choices; it is not enforced per-content approval in MCP. SRC-1: `plugins/hipporag/skills/hipporag-memory/SKILL.md`, `plugins/hipporag/skills/index-folder/SKILL.md`, `src/hipporag/mcp_server.py`.

> - To **update** a changed source, first `delete` its `source_id`, then `index` the new passages. Otherwise the stale passages remain.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`

The same skill says retrieve makes no LLM call and new passages cost one extraction call. Those are doctrine claims qualified by the inspected online NER/triple/filter implementation, not performance facts adopted here. The plugin launcher supplies a separate host-admitted installation channel, `uvx` from mutable Git, with no runtime revision/approval loop established in HippoRAG. SRC-1: `plugins/hipporag/.claude-plugin/plugin.json`, `src/hipporag/information_extraction/openie_openai.py`, `src/hipporag/rerank.py`.

## Annotations

none
