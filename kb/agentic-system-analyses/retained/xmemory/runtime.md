---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "xMemory runtime baseline: shipped construction, hierarchy maintenance, retrieval, answer consumption and evaluation at the frozen Git revision."
run-id: AAS-2026-10-15-xmemory-b9a2b9f58eda-01
reviewed-boundary: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
---

# xMemory runtime report

## Runtime account

### Work and evidence basis

xMemory's shipped work is conversation-memory construction followed by memory-assisted question answering, not autonomous tool execution. The public facade delegates ingestion, flush, semantic-task waiting and search. The LoCoMo construction driver additionally coordinates theme updates and graph updates; the reader driver reloads retained files, selects context and calls an answer model. These drivers belong to the target, as established in [boundary](boundary.md#boundary-and-evidence). SRC-1 supplies implementation and declared design, not an observed run. All implementation findings below refer to that source at the frozen commit. Operation, model compliance and benefit remain unobserved; no target code was executed.

The ordinary README path is construction through `evaluation/locomo/add.py`, then `evaluation/locomo/xMemory_search_framework.py --search-strategy adaptive_hier`, then offline scoring. The reader's CLI default is instead `baseline`; invoking the command without the strategy argument does not select hierarchical retrieval (SRC-1, `README.md`, `evaluation/locomo/xMemory_search_framework.py`). The claim and its qualifications are retained in [RT-CLM-retrieval-purpose](#rt-clm-retrieval-purpose).

### Ordinary invocation, ownership and return

1. **Construction principal and identity.** An operator invokes the dataset driver with configuration, dataset path, model name, conversation/session limits and worker settings. Code turns a conversation into role/content/timestamp/metadata dictionaries, incorporating image captions and search-query text. It creates a caller-chosen namespace `speaker_a` plus conversation index, not an authenticated subject. A shared injected HF client serves conversation workers, each of which creates an xMemory instance. The model CLI argument supplies the injected model; changing only the configuration is not equivalent because the driver passes its own `args.llm_model` to `LLMClient` (SRC-1, `evaluation/locomo/add.py`). [RT-RTE-conversation-admission](#rt-rte-conversation-admission) owns the runtime admission path.
2. **Buffer and episode loop.** `MemorySystem.add_messages` takes an instance-local per-owner reentrant lock, converts messages and appends them one at a time. For a nonempty buffer with smart detection enabled, a model receives conversation history and the arriving message; above the exclusion threshold it sees a temporary history omitting the last buffered message. Its `should_end` field decides segmentation. Code copies and clears a completed buffer before generating episodes. The arriving message starts the next buffer. Episode generation requests title/content/time, keeps original messages, saves to the repository, then updates indexes and incremental episode state. Batch creation and semantic generation are software-owned thread work, not independent agents with delegated goals (SRC-1, `src/core/memory_system.py`, `src/core/boundary_detector.py`, `src/generation/episode_generator.py`).
3. **Semantic continuation.** Successful episode creation publishes an `episode_created` event. The handler checks semantic-memory enablement and submits a tracked background task identified by owner and episode ID. The task reloads episodes and existing statements, obtains embeddings, invokes semantic generation, skips duplicates, saves accepted statements and attempts indexing. The completion callback accumulates newly saved statements for maintenance. Initial `add_messages` returns buffer/episode/scheduling information before this continuation necessarily finishes. Forced flush shares episode creation but explicitly initiates the event only when semantic memory is enabled. [RT-RTE-semantic-admission](#rt-rte-semantic-admission) describes the decision roles and modes; memory revision semantics are left to the memory member (SRC-1, `src/core/memory_system.py`, `src/generation/semantic_generator.py`).
4. **Maintenance and terminal construction result.** The driver flushes remaining messages, calls the semantic wait method, fetches the incremental episode and statement batches, updates themes, updates the hierarchy graph and finally clears the incremental batches. Theme maintenance uses numerical similarity and clustering plus model-generated summaries; graph update passes no new message nodes. It persists artifacts for a later reader. The driver's success predicate is existence of the episode JSONL file, not verification of all semantic/theme/graph content. Its terminal output is a tracker summary on stdout. `finally` closes the memory instance and waits for the semantic executor (SRC-1, `evaluation/locomo/add.py`, `src/core/memory_system.py`, `src/core/memory_hierarchy.py`). See [RT-RTE-hierarchy-admission](#rt-rte-hierarchy-admission).
5. **Read, decide, answer and save.** The reader constructs a memory instance per conversation worker, obtains an embedding client from it, and addresses the same speaker/index namespace. With adaptive search it loads episode, semantic, theme and semantic-kNN files, loads stored theme vectors and recomputes semantic/episode embeddings. Query similarity, graph representatives and model-generated token scores choose semantic and episode context. Code hydrates originals only for episodes marked for expansion, subject to the configured limit. The final answer model receives semantic and episodic text, timestamps and any hydrated originals, but not the returned theme list. Its response, retrieved material, dataset answer/evidence/category and token counters enter a JSON result; separate files record model identity and aggregate token counts. The dataset reference answer is recorded after answering and is not passed into retrieval or the answer call. Offline scoring then compares saved response and reference answer (SRC-1, `evaluation/locomo/xMemory_search_framework.py`, `evaluation/locomo/evals.py`). See [RT-RTE-adaptive-reader](#rt-rte-adaptive-reader) and [RT-RTE-offline-evaluation](#rt-rte-offline-evaluation).

### Forcing cases and guarantee limits

Three source-level forcing cases materially qualify the ordinary account. These are inspected branches, not runtime experiments.

**Segmentation is not a hard configured context cap.** With smart detection enabled and a nonempty buffer, the maximum-size branch is an `elif`, so it is not a second unconditional check. The detector explicitly ignores the confidence threshold and returns no boundary on errors. A model that repeatedly returns false can therefore keep growing the buffer along this inspected path. The temporary exclusion removes one message from the detector's view, not from retained originals or the full episode-generation input. Forced flush bypasses model segmentation. Owner: `MemorySystem` plus `BoundaryDetector`; enforcement point: branch selection and model response; guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. There is no established invariant bounding model-visible input by `buffer_size_max` across these paths. Required external contract for semantic segmentation is correct model judgment, not merely valid JSON (SRC-1, `src/core/memory_system.py`, `src/core/boundary_detector.py`).

> # Check buffer size limit
> elif buffer.size() >= self.config.buffer_size_max:
>     should_create_episode = True
>     boundary_reason = "Buffer reached maximum size"
> --- `src/core/memory_system.py`

> # ⚠️ Note: Confidence threshold check removed - only use should_end from LLM
> # This matches the behavior of the old system which ignores confidence
> --- `src/core/boundary_detector.py`

**Task completion is not successful, durable hierarchy completion.** The wait loop returns true when there are no active tasks, while completion callbacks also remove failed tasks. Timeout attempts cancellation and removes task records, but cannot guarantee termination of already running Python futures. The construction driver ignores the wait return value before taking its incremental snapshot. Closing later waits for the executor, but does not rerun the earlier maintenance snapshot. Episode creation also clears buffers before save/index completion, and indexing failure can occur after repository save. These facts prevent interpreting a successful driver summary as an atomic all-layers commit. Owner: task tracker and construction driver; enforcement points: polling and file-existence predicate; guarantee strength: best effort; implementation conclusion status: wired; operation conclusion status: uninspected. Required external contracts include successful model/provider calls and filesystem/index writes. Instance-local locks do not establish multi-process exclusion (SRC-1, `src/core/memory_system.py`, `evaluation/locomo/add.py`, `src/storage/episode_storage.py`).

> # If there are no active tasks, we're done
> if active_tasks == 0:
>     logger.debug(f"All semantic generation tasks completed for user {owner_id}")
>     return True
> --- `src/core/memory_system.py`

> if file_path.exists():
>     result["success"] = True
>     result["stage"] = "completed"
> --- `evaluation/locomo/add.py`

The filesystem episode backend describes immediate persistence but rewrites the user's JSONL directly under its own `RLock`; this is a concrete write mechanism, not a crash-safe transactional guarantee. The wider admission path saves episodes before indexes and does not undo the save if a later index operation fails (SRC-1, `src/storage/episode_storage.py`, `src/core/memory_system.py`).

> with open(file_path, 'w', encoding='utf-8') as f:
>     for episode in episodes:
>         json.dump(episode.to_dict(), f, ensure_ascii=False)
>         f.write('\n')
> --- `src/storage/episode_storage.py`

**Adaptive expansion is a surrogate decision, not verified information improvement.** The implementation's quantity named entropy is mean negative log probability of generated tokens, not a correctness oracle or full predictive entropy. It compares a fixed semantic-only baseline with one episode at a time, not the marginal effect of each episode after all previously selected episodes. Thresholds include negative values; fallback selects a first candidate even if none passes. Expansion marks raw-message hydration after testing episode summary/content, without testing originals in this route. A generation/cache failure can return the constant 5.0. Theme text affects the scoring prompt but is omitted from the final answer prompt. Therefore a selected episode is not evidence of reduced final-reader uncertainty or better answers. Owner: `LocomoSearcher`; enforcement points: score thresholds, fallback and hydration flags; guarantee strength: policy; implementation conclusion status: wired; operation conclusion status: uninspected. It requires compatible model logits and a relationship between this surrogate and answer utility that supplied evidence does not establish (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).

> nlls = [-float(lp) for lp in logprobs]
> entropy = float(sum(nlls) / len(nlls))
> --- `evaluation/locomo/xMemory_search_framework.py:908-925`

> if not selected_episode_ids and E_probe_ids:
>     selected_episode_ids = [E_probe_ids[0]]
> --- `evaluation/locomo/xMemory_search_framework.py`

### Alternate surfaces and isolation envelope

The facade's synchronous search, async executor wrapper, direct `MemorySystem` operations, baseline hybrid/vector/BM25/NOR-LIFT dispatch, explicit flush, manually ordered theme/graph operations and direct lightweight vector reader are material alternate routes. The facade does not automatically perform the driver's theme/graph sequence. The lightweight reader directly reloads JSONL and a vector index without taking the episode-storage locks or constructing a generation client. Baseline search can honor zero top-k independently for either result type; the adaptive strategy uses its own semantic cap and defaults a nonpositive episode count to ten. Thus facade top-k behavior is not a universal control over the adaptive route (SRC-1, `src/api/facade.py`, `src/core/memory_system.py`, `src/core/lightweight_search_system.py`, `evaluation/locomo/xMemory_search_framework.py`). See [RT-RTE-baseline-search](#rt-rte-baseline-search).

Capability surface differs from current grants. Constructors accept injected memory systems, models, generators, repositories, indexes and metrics reporters. These Python objects run as host code; they are not constrained by the default prompt/parse policy. The selected local adapter also loads tokenizer/model code with `trust_remote_code=True`. Its model name is not an immutable weight revision. [RT-RTE-provider-admission](#rt-rte-provider-admission) and [RT-CMP-llm-client](#rt-cmp-llm-client) retain those boundaries. The unused-by-default OpenAI-style adapter file exists, but default exports select the HF adapter; inspection does not establish deployments using the alternative (SRC-1, `src/utils/__init__.py`, `src/utils/llm_client_openllm.py`, `src/api/facade.py`, `src/services/providers.py`, `src/core/memory_system.py`).

The inspected drivers grant local storage/model loading and credentialed embedding-service requests; optional injected host implementations can enlarge that surface. User IDs select files, caches and collections, rather than proving user authorization. No deployed container, OS permission set or network policy was supplied. No general model-to-shell/tool dispatcher was found in the bounded search described in [RT-ABS-action-dispatch](#rt-abs-action-dispatch); this does not sandbox injected Python or remotely loaded model code. Approval for a workflow or a model choice is not per-statement human approval. [RT-BAP-memory-reader](#rt-bap-memory-reader) describes the soft behavioral force of retained text.

Working-context controls are explicit input assembly, not a chat agent's accumulating window. Detector history can omit a trailing message; episode generation condenses a whole segment while preserving originals outside later prompts. Adaptive selection keeps most stored material out of each model call, admits selected summaries and conditionally reloads originals. Scoring uses per-thread prefix-KV state keyed by exact prefix text, with cache and non-cache model-call alternatives. It preserves a shared scoring prefix, not cross-session learned parameters. The final answer is a fresh prompt with its own smaller selected inputs. This resembles selected-input call frames, but the retained store is read by value rather than providing model-dereferenceable pointers. Returning an ID does not itself make the source text reachable in the model window (SRC-1, `src/core/memory_system.py`, `src/generation/episode_generator.py`, `evaluation/locomo/xMemory_search_framework.py`).

### Additional coverage and unobserved portions

Beyond boundary inspection, this member inspected the facade; construction driver; memory-system initialization, buffer loop, search dispatch, save/scheduling/completion/wait/close and hierarchy adapters; boundary detector; episode generation; semantic dispatch and prediction/comparison conversion; provider factory; HF adapter construction, chat generation and JSON fallback; embedding construction/request/retry; lightweight preload/search; episode-write implementation; hierarchy orchestration; reader reload, answer, hydration, entropy, adaptive selection, processing and persistence; evaluation scoring; and README. All are SRC-1 implementation except README and embedded prompt intent, which are doctrine/design. No new source identity is introduced.

Detailed split/merge objective internals, every backend's consistency/rebuild behavior, full direct-model logprob/cache internals, every lexical/vector ranking variant and metric internals remain incompletely inspected here. They prevent exhaustive correctness, isolation and numerical-equivalence conclusions, not the positive source-wiring findings above. No runtime activation, token-saving magnitude, model quality, benchmark result, crash recovery or isolation envelope was observed. No product-source self-edit loop or production release approval process is established by the inspected routes; source modification is not inferred from retained-memory updates.

## Shared records

### Components

#### RT-CMP-llm-client
Label: HF LLMClient

Source-native identity: `LLMClient` exported from `src/utils/llm_client_openllm.py` through `src/utils/__init__.py`. Representational form: distributed-parametric language model, consumed through natural-language prompts and token generation. Storage substrate: external HF model/tokenizer artifacts loaded into host tensor memory. Parameters change during operation: no optimizer/update step in the inspected inference paths; calls use `torch.no_grad()`. Exact version pinned: no, construction gives a model name without a `revision`. Mutable resolution: a later load of that name can resolve different artifacts; injected clients can differ. No provider-internal training or external artifact behavior was inspected. This component supplies segmentation, episode/statement/theme generation, adaptive scoring and answers; it does not itself decide all code branches (SRC-1, `src/utils/llm_client_openllm.py`, `src/utils/__init__.py`, `src/services/providers.py`, `evaluation/locomo/xMemory_search_framework.py`).

> self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
> self.model = AutoModelForCausalLM.from_pretrained(
>     self.model_name,
>     device_map=device_map,
>     torch_dtype=dtype,
>     trust_remote_code=True,
>     attn_implementation=attn_impl or "sdpa",
> )
> --- `src/utils/llm_client_openllm.py`

#### RT-CMP-embedding-client
Label: EmbeddingClient

Source-native identity: `EmbeddingClient`. Representational form: distributed-parametric embedding computation whose numerical vectors are consumed by similarity and graph algorithms. Storage substrate: opaque remote provider model, plus returned vectors in host memory/indexes/files. Parameters change during operation: client sends embedding requests, with no parameter update API on the inspected path; provider-internal mutation is uninspected. Exact model version pinned: no immutable model artifact is captured. Mutable endpoint resolution: yes, model/deployment name plus OpenAI base URL or environment-selected Azure endpoint can resolve provider-controlled implementations. The endpoint and API version do not pin weights. Text is cleaned, batched and retried up to three times; exhaustion raises. These requests transmit text outside local storage (SRC-1, `src/utils/embedding_client.py`, `src/config.py`).

> response = self.client.embeddings.create(
>     model=self.model,   # ✅ Azure: deployment name；OpenAI: model name
>     input=batch,
>     timeout=self.timeout
> )
> --- `src/utils/embedding_client.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-conversation-admission
Label: Conversation and episode admission

Endpoints/progression: caller messages → owner buffer → model segment decision or force-flush → episode generator → repository and indexes → event/scheduling result. Owner: `MemorySystem` and calling construction driver. Context: role/content/timestamp dictionaries, current buffer, generation prompts and per-owner lock. Action effects: clears completed buffers, saves episodes including originals, updates indexes and incremental batches. The generator supplies prose; code checks essential fields, normalizes time/content and can create a fallback episode. Runtime controls include buffer settings, smart-boundary toggle, injected generator, explicit flush and episode minimum size (SRC-1, `src/core/memory_system.py`, `src/generation/episode_generator.py`, `evaluation/locomo/add.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: processing dictionary with episodes, buffer sizes and scheduling flags, or an error dictionary; forced flush returns episode information or None.
- Later read-back: saved episodes and original messages feed semantic generation and later query/answer invocations.
- Delegated visibility: episode-generation calls see the selected full segment; semantic workers receive the created episode, not the calling worker's entire state.
- Selection predicate: smart detector's should_end, or non-smart maximum-size branch, or explicit caller flush; generation requires minimum message count.
- Invalidation or expiry: buffer is cleared at segment dispatch/flush; repository retention is separate and has no TTL on this inspected path.
- Activation or effect: save/index calls are wired; reliable segmentation, persistence and downstream answer changes are not observed.
- Evidence limits: errors can become return values; buffer clearance precedes successful save, so retrying is not proven lossless or idempotent.

Admission: caller proposes input; model proposes segmentation and episode text; code decides when to save. Starting the driver is human initiation, not human review of each admitted episode. Veto: code can reject too-short inputs or invalid generation; fallback generation can still be admitted. Operating mode: dataset construction or open caller messages. Answer oracle: none for truth checking; source messages guide generation but are not an independent expected-answer test. Trigger/proposed change: arriving conversation creates retained episode content. Guidance: static generation and boundary prompts; what persists is episode content and originals, not revised method text. Recovery: generation fallback and driver retries; no transaction spanning clear, save and index.

> original_messages=[msg.to_dict(clean_metadata=True) for msg in messages],
> message_count=len(messages),
> boundary_reason=boundary_reason,
> timestamp=episode_timestamp
> --- `src/generation/episode_generator.py`

#### RT-RTE-semantic-admission
Label: Background semantic admission

Endpoints/progression: episode-created event → tracked executor task → prior episodes/statements → selected generator mode → embedding/duplicate check → semantic repository → attempted search index → incremental callback. Owner: `MemorySystem`, with `SemanticGenerator` and `PredictionCorrectionEngine`. Software chooses mode; the model proposes statements. In prediction-correction mode, existing statements guide a predicted episode and the model compares prediction against original messages; empty existing knowledge takes a cold-start extraction path. When that engine is disabled, configured per-episode extraction is the alternate; if neither mode is enabled the generator returns no statements. This is a knowledge-admission loop, not evidence of source-code or parameter revision (SRC-1, `src/core/memory_system.py`, `src/generation/semantic_generator.py`, `src/generation/prediction_correction_engine.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: event scheduling does not return completed statements to the caller; task returns saved-memory dictionaries, possibly an empty list after error.
- Later read-back: saved statements guide later prediction/extraction and retrieval; callback batches feed themes and graph.
- Delegated visibility: worker sees new episode, existing episode/semantic data and embeddings; each model invocation gets its constructed prompt.
- Selection predicate: enablement/event checks, prediction-correction versus per-episode configuration, model statement output and embedding-based duplicate rejection.
- Invalidation or expiry: completion removes task records; timeout removes tracker entries without ensuring running writes stop; retained semantic lifetime is separate.
- Activation or effect: statement repository writes and later-consumer wiring are implemented; no observed update or demonstrated improved capacity is supplied.
- Evidence limits: duplicate checking and model extraction do not establish factual correctness; saved statements can survive index failure, and completion does not prove success.

Admission roles: model proposes statement content; code filters empties and duplicates and decides save. Human per-content veto is not present in this inspected route; generic caller provenance does not establish who authored original conversations. Answer oracle: original messages are the comparison target, not a held-out expected-answer oracle. Operating mode: automatic incremental extraction; trigger is new episode, not failed benchmark score. Guidance: shipped prediction/comparison prompts direct extraction of missing/misrepresented knowledge. Persistence: statement text, source episode ID, generic knowledge type and metadata. Rejection/recovery: filtered statements can be dropped; exceptions return empty results; no inspected rollback of already saved statements. Detailed revision/theory classification belongs to the specialists; this record establishes the admission mechanism, not a theory-builder or learning conclusion.

> new_statements = self._extract_knowledge_from_comparison(
>     original_messages=new_episode.original_messages,
>     predicted_episode=predicted_episode
> )
> --- `src/generation/prediction_correction_engine.py`

#### RT-RTE-hierarchy-admission
Label: Driver-coordinated hierarchy admission

Endpoints/progression: wait call → fetch incremental batches → `update_themes` → `ThemeManager.assimilate_and_accommodate` → graph update → mark batches consumed. Owner/next-step policy: construction driver chooses order; numerical attachment/split/merge code chooses structure; model proposes theme summary. Representational forms: symbolic IDs/membership/edges, numerical vectors, and natural-language summaries. Effects reach per-owner theme JSONL/vector artifacts and graph persistence (SRC-1, `evaluation/locomo/add.py`, `src/core/memory_system.py`, `src/core/memory_hierarchy.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: theme and graph statistics, followed by driver tracking and stdout summary.
- Later read-back: reader loads themes, semantic relationships and vectors; graph exports are available for diagnostics, while adaptive reader uses the separate files rather than loading the exported graph here.
- Delegated visibility: summarizer receives statement strings; graph manager receives new episodes/statements, current theme dictionary and an empty message list.
- Selection predicate: new semantic batch plus numerical attachment, size/heterogeneity split and similarity merge/coalescence policies.
- Invalidation or expiry: successful driver sequence clears incremental batches; themes are rewritten and reader caches can remain stale within the reader instance.
- Activation or effect: persisted hierarchy feeds later adaptive selection; no evidence that a selected theme or restructuring improved a final answer.
- Evidence limits: a false/timeout wait result is ignored; maintenance snapshots may omit later-finishing tasks; not an atomic multi-file transaction.

Admission: code decides structural change, model supplies summaries, caller can manually choose when/with which batches maintenance runs. Trigger/proposed change: new statements attach, create, split or merge themes and update graph. Veto: numerical tests determine structural admissibility; no per-change human approval or answer oracle. Mode: incremental maintenance, not benchmark-directed improvement. Guidance: fixed summary instruction asks for a stable high-level theme capturing recurring facts. Retains summaries/membership/vectors/edges, not a revised summary policy. Recovery: caller can retry or retain files externally; automatic consistent rollback across theme, vector, graph and consumption steps is not established.

> memory.mark_incremental_consumed(user_id)
> 
> # Verify file creation
> result["stage"] = "verifying_files"
> --- `evaluation/locomo/add.py`

#### RT-RTE-baseline-search
Label: Baseline and direct vector search

Endpoints/progression: facade search/asearch → `MemorySystem.search_all` → method-specific loading → parallel episodic/semantic searches → categorized results. Separate lightweight route directly loads JSONL and vector indexes and returns the same two categories. Owner: deterministic Python search dispatch; context/state: caller namespace/query/counts plus stored episodes/statements/indexes. Runtime-client controls include method, top-k and dependency injection, not authorization (SRC-1, `src/api/facade.py`, `src/core/memory_system.py`, `src/core/lightweight_search_system.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: episodic/semantic result lists; broad errors in search_all or lightweight search return empty categories.
- Later read-back: retrieves accumulated episode and semantic content; baseline reader then constructs a fresh answer prompt.
- Delegated visibility: parallel search workers receive user ID, query, top-k and selected backend access; asearch merely runs synchronous search in an executor.
- Selection predicate: hybrid, BM25, vector or NOR-LIFT dispatch; zero top-k short-circuits each baseline category. Lightweight route uses vector search only.
- Invalidation or expiry: standard caches/index-loading rules apply; lightweight preloaded dictionaries persist in the instance without a refresh trigger in its inspected search path.
- Activation or effect: delivers content to caller; no answer is produced by the facade search alone, and result delivery establishes no compliance or benefit.
- Evidence limits: backend ranking variants are not exhaustively traced; empty output can mean error rather than absence of stored knowledge.

> # Handle top_k=0 case: return empty list
> if top_k == 0:
>     return []
> --- `src/core/memory_system.py:899-915`

#### RT-RTE-adaptive-reader
Label: Adaptive hierarchy selection and answer

Endpoints/progression: question → hierarchy reload/cache and query embedding → semantic pool → theme/semantic graph representatives → episode candidates → per-candidate generation score → hydration → answer prompt → saved response. Owner: `LocomoSearcher`; numerical rules propose/rank candidate context, local model supplies generated-token scores, code admits/falls back, answer model supplies final text. State: per-user hierarchy cache, per-thread prefix-KV cache/token counters, result map. Runtime controls: strategy, counts, original-message cap, model and worker settings. The final answer call is fresh, not a continuation of scoring generations (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: theme/episode/semantic results from retrieval; answer method returns stripped text or an empty string after generation failure.
- Later read-back: saved hierarchy text is read into scoring and answer calls; original messages are reloaded for flagged episodes. Saved QA results are later consumed by offline evaluation, not automatically by admission.
- Delegated visibility: scoring sees themes, selected semantics and each probed episode; final answering receives only rendered semantics and episodes, including originals when hydrated.
- Selection predicate: top-40 semantic similarity pool, up to five theme and twenty semantic representatives, induced plus vector episode candidates, up to ten probes, fixed NLL-difference thresholds and early stops; first-candidate fallback if no episode passes.
- Invalidation or expiry: hierarchy cache is keyed only by user within the instance; prefix cache is rebuilt when exact prefix text changes; no file-change invalidation is wired in the inspected hierarchy loader.
- Activation or effect: context selection and final model invocation are wired; changed behavior, truthfulness and uncertainty reduction remain unobserved.
- Evidence limits: the score is a surrogate with constant fallback; final prompt differs from scoring context; original hydration is gated by summary-level scores, not measured raw-message improvement.

Decision roles/answer oracle: deterministic code decides inclusion and fallback from model scores; no ground-truth answer enters that decision. Dataset references are merely saved alongside the resulting response. Mode: bounded per-question context search, not online product optimization. Missing embedding client, empty hierarchy or no semantic candidates fall back to baseline. Admission here changes current invocation context, not retained knowledge. No human candidate approval appears in this route.

> episodic = format_memory_lines(
>     memories.get("episodic", []),
>     include_original_limit=self.include_original_messages_top_k,
> )
> semantic = format_memory_lines(
>     memories.get("semantic", []),
>     include_original_limit=0,
> )
> --- `evaluation/locomo/xMemory_search_framework.py`

#### RT-RTE-offline-evaluation
Label: Offline answer evaluation

Endpoints/progression: saved result JSON → response/reference conversion → lexical metrics → metrics JSON. Owner: evaluation script and operator who invokes it. Context/state: saved question, answer, response and category; no live memory mutation. It skips category 5 and computes F1 and BLEU; imported model judging is commented out in the inspected scoring loop (SRC-1, `evaluation/locomo/evals.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: persisted per-item scores and output-path message.
- Later read-back: reads prior QA artifacts, not retained memory into an agent; no automated score-to-memory/product revision link is established here.
- Delegated visibility: evaluation threads receive result groups, including expected answers.
- Selection predicate: all saved entries except category 5; scores compare reference answer and predicted response.
- Invalidation or expiry: inapplicable — no automatic expiry policy in this offline input/output path; operator chooses paths/reruns.
- Activation or effect: score computation is wired, not a runtime admission gate or demonstrated benchmark outcome.
- Evidence limits: metric internals and completed result artifacts are not established here; this code does not verify research claims by its presence.

Answer oracle: dataset `answer`, supplied through the QA result artifact; use is offline lexical scoring. Proposer: answer model in the reader; evaluator: scoring software; veto over later production/admission: none established. Operating mode: fixed dataset evaluation. A separate judge's import is not proof of its execution.

> #llm_score = evaluate_llm_judge(question, gt_answer, pred_answer)
> llm_score = None
> --- `evaluation/locomo/evals.py`

#### RT-RTE-provider-admission
Label: Host-selected implementation and model admission

Endpoints/progression: caller configuration/injected Python objects or CLI model → default factory/constructor selection → provider/model initialization → subsequent memory/QA calls. Owner: host caller and Python loader. Representational forms: symbolic configuration and executable Python, plus external distributed-parametric artifacts. Effects can include arbitrary host implementation behavior through injected code or trusted remote model code; these are not limited to emitted prose (SRC-1, `src/api/facade.py`, `src/core/memory_system.py`, `src/services/providers.py`, `src/utils/llm_client_openllm.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: constructed object or initialization exception.
- Later read-back: inapplicable — this route installs chosen implementations/artifacts for use, rather than reading content accumulated through operation.
- Delegated visibility: selected clients/generators/repositories receive their supplied input data with host process capabilities.
- Selection predicate: constructor arguments, truthy injected object versus default, configuration backend strings, CLI model name and embedding environment variables.
- Invalidation or expiry: caller can reconstruct with different objects/models; no automatic migration or rollback protocol is established.
- Activation or effect: chosen components are wired into later calls; actual remote code, model version and deployed grants are not supplied.
- Evidence limits: capability surface is not a report of installed extensions, exact weights, current host permissions or exercised code loading.

Admission roles: caller supplies/selects; factory and loader admit. No dynamic model-authored extension proposal is established. Human participation is unresolved for generic callers and explicit at operator CLI choice; neither proves per-artifact code review. Answer oracle: none. Mode: startup/configuration, not experimental improvement. Trigger/proposed change: configuration or host-code replacement can alter provider, storage or generator behavior. Guidance: constructor/factory contracts, not retained operational criticisms. Rejection/recovery: initialization errors can reject loading; replacement/restart is caller-owned, not an automatic production rollout or rollback.

> self._episode_repository = episode_repository or providers_episode_repo
> self._semantic_repository = semantic_repository or providers_semantic_repo
> self._vector_index = vector_index or providers_vector_index
> self._lexical_index = lexical_index or providers_lexical_index
> self._boundary_detector = boundary_detector or providers_boundary
> self._episode_generator = episode_generator or providers_episode_gen
> self._semantic_generator = semantic_generator or providers_semantic_gen
> --- `src/core/memory_system.py`

### Claims

#### RT-CLM-retrieval-purpose
Label: Claimed uncertainty-guided expansion

Claimed operation: README attributes compact/diverse retrieval and expansion to episodes/raw messages only when reader uncertainty falls, with answer-quality and efficiency gains. Source: SRC-1, `README.md`, doctrine/design and reported operation. Implementation is more qualified: optional strategy; NLL surrogate; threshold/fallback inclusion; raw-message flag inferred from episode score; theme omission at final answering. [RT-RTE-adaptive-reader](#rt-rte-adaptive-reader) establishes the narrower wiring. No supplied observed run or causal experiment verifies benefit.

> At inference, xMemory retrieves top-down, selecting a compact, diverse set of themes and semantics for multi-fact queries, and expanding to episodes and raw messages only when it reduces the reader’s uncertainty.
> --- `README.md`

### Evidenced absences

#### RT-ABS-action-dispatch
Label: No general model action dispatcher in inspected shipped paths

- implementation conclusion status: absent

Searched boundary: SRC-1 at `1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608`, roots `src/`, `evaluation/`, `xMemory/`; query terms `subprocess`, `exec(`, `eval(`, `tool_calls`, `approve`, `permission`, `trust_remote_code`, `from_pretrained`, plus direct inspection of selected facade, providers, model adapter, construction and reader calls. The search's executable-loading witness is HF `trust_remote_code=True`; inspected model calls return text/JSON/logprob statistics, not commands dispatched as model actions (SRC-1, `src/utils/llm_client_openllm.py`, `src/api/facade.py`, `evaluation/locomo/add.py`, `evaluation/locomo/xMemory_search_framework.py`).

Supported conclusion: there is no general model-to-shell/provider-tool dispatcher on these inspected default conversation-memory/QA routes. Prevented conclusion: this does not prove process sandboxing, absence of arbitrary host/remote-loader code, or all deployments lacking action capabilities. The constructor injection and trusted-loader route is an explicit alternative capability, not covered by a prompt-only safety claim. Evidence passage: the checked `chat_completion` continuation in SRC-1, `src/utils/llm_client_openllm.py`, returns decoded content rather than executing it:

> content = self.tokenizer.decode(new_ids[idx:], skip_special_tokens=True).strip()
> --- `src/utils/llm_client_openllm.py`

### Behavioral-authority paths

#### RT-BAP-memory-reader
Label: Retained text to model decisions

Consumer: prediction/comparison generator, theme summarizer, adaptive scoring model and final answer model. Channel: stored statements, episode text and selected original messages rendered into natural-language prompts. Force: advisory/model-interpreted context, with symbolic code deciding inclusion and numerical ranking; not an execution privilege or proven instruction compliance. Horizon: later episode-processing and question invocations across storage reloads. Static prompts frame the intended use; persisted text does not rewrite those prompt templates on the inspected path (SRC-1, `src/generation/prediction_correction_engine.py`, `src/core/memory_system.py`, `evaluation/locomo/xMemory_search_framework.py`). [RT-RTE-semantic-admission](#rt-rte-semantic-admission) establishes update consumption; [RT-RTE-adaptive-reader](#rt-rte-adaptive-reader) establishes answer consumption. The selected memory can influence later behavior by model interpretation, but successful influence or beneficial change is unobserved.

> prompt = ANSWER_PROMPT.render(
>     question=question,
>     episodic=episodic,
>     semantic=semantic,
> )
> --- `evaluation/locomo/xMemory_search_framework.py`

## Annotations

none
