---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "xMemory workflow: shipped LoCoMo adaptive memory-assisted question answering through result delivery and offline scoring."
run-id: AAS-2026-10-15-xmemory-b9a2b9f58eda-01
reviewed-boundary: "1a4f9dd8abd7f2da86bfe6afe4293a1ea1c63608"
---

# xMemory workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped LoCoMo adaptive reader: an operator requests answers over previously constructed conversation memory; software selects and hydrates context, calls a model, and saves a QA artifact for separate scoring. This is selected because it connects retained memory to a delivered model result, rather than stopping at a library search return. It is a multi-step model-dependent QA workflow, not a team of autonomous agents. The README invocation explicitly selects `adaptive_hier`; the CLI default is baseline, as qualified in [RT-CLM-retrieval-purpose](runtime.md#rt-clm-retrieval-purpose).

All source findings use SRC-1 at the frozen revision in [boundary](boundary.md#boundary-and-evidence). Evidence is implementation and shipped prompt/design text, not observed execution. This member additionally inspected `process_single_conversation` in `evaluation/locomo/add.py` and the reader's adaptive entry, answer, hydration, search dispatch, worker coordination, save and main-call sequence in `evaluation/locomo/xMemory_search_framework.py`. No model/provider calls or target execution were performed. Successful completion, answer accuracy and recovery effectiveness remain unobserved.

### Request, prerequisites and handoffs

1. **Prepare retained state in a separate invocation.** The construction driver supplies conversation messages under a speaker/index namespace. Episode creation and background semantic generation precede driver-owned theme and graph maintenance. These are the existing [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission), [RT-RTE-semantic-admission](runtime.md#rt-rte-semantic-admission) and [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission) routes, not a reader-controlled rebuild. Their handoff is retained files, not a live conversation-agent context. The driver waits, snapshots incremental batches, updates themes and graph, and clears batches. Its final file-existence check does not certify a complete hierarchy or all background work. The runtime records retain the relevant passages and non-atomicity limits (SRC-1, `evaluation/locomo/add.py`, `src/core/memory_system.py`).
2. **Dispatch the request.** Reader `main` loads configuration, answer model and dataset, applies optional conversation/QA limits and constructs `LocomoSearcher`. `process` submits one software worker per conversation. Construction of each memory object is serialized by `_memory_build_lock`; questions within one conversation run sequentially, while conversations can run concurrently. The worker derives the namespace from speaker and dataset index. It supplies the question and memory handle to search, not the expected answer. These are executor tasks, not independently prompted subordinate agents (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).
3. **Select context.** [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader) supplies the existing route identity and its selection evidence. Reloaded hierarchy and a query embedding support semantic/theme representatives and episode candidates. Code owns inclusion, stopping and fallback; the model supplies generated-token scores. Missing embedding client, empty hierarchy or no semantic pool routes to baseline search. Numerical thresholds and a first-episode fallback are admission policies for this question's context, not correctness verification. The score does not establish that admitted episodes improve the final answer (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).
4. **Hydrate and answer.** The worker passes selected results to episode hydration, then semantic timestamp hydration, then `answer`. Episode hydration follows expansion flags and the configured positive cap; missing IDs/repository objects or lookup errors can leave summaries without originals. The answer model receives freshly rendered episodic and semantic text plus the question. It does not inherit scoring generations, and returned themes are not rendered in the final answer prompt. Thus delegation supplies selected text by value, not unrestricted access to the store or an accumulating agent transcript. The existing route and [RT-BAP-memory-reader](runtime.md#rt-bap-memory-reader) retain the prompt evidence and authority limit (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).
5. **Collect and deliver.** After answering, the worker flattens retrieved context and appends a record containing response, question, dataset answer/evidence/category and token counts. Expected answers are recorded for downstream comparison; they are not a retrieval oracle or an answer-acceptance gate. Main calls `save` only after `process` returns. That writes results JSON and then token-statistics JSON; model identity is saved earlier in startup. Delivery here means the configured result file is written, not that an end user approved an answer or that metrics passed (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).

The worker's concrete handoff order is:

> memories = self.search(memory, user_id, question)
> self._hydrate_episode_results(memory, user_id, memories.get("episodic", []))
> self._hydrate_semantic_results(memories.get("semantic", []))
> response = self.answer(question, memories)
> flattened = flatten_results(memories, self.include_original_messages_top_k)
> --- `evaluation/locomo/xMemory_search_framework.py`

The CLI's completion boundary is:

> try:
>     searcher.process(dataset, max_workers=args.max_workers)
>     searcher.save()
> finally:
>     searcher.close()
> --- `evaluation/locomo/xMemory_search_framework.py`

### Verification, rejection and recovery

**Construction rejection is not whole-conversation recovery.** The construction worker rejects empty input before creating memory. Initialization, message chunks and flush have bounded retries. After repeated `None` flush returns, it marks failure and exits before theme/graph updates, even though earlier message processing may already have created episodes. Chunk retries are exception-driven: a returned processing dictionary is not inspected for success. Therefore the retry machinery is not proof of idempotent replay or preservation of every message. The supplied conversation route already identifies buffer-clear-before-save risk (SRC-1, `evaluation/locomo/add.py`; [RT-RTE-conversation-admission](runtime.md#rt-rte-conversation-admission)).

> memory.add_messages(user_id, chunk)
> messages_processed += len(chunk)
> if pbar:
>     pbar.update(len(chunk))
> break
> --- `evaluation/locomo/add.py`

> if episode_info is None:
>     result["error"] = "Failed to create episode (flush returned None after retries)"
>     result["stage"] = "flush_failed"
>     with tracker_lock:
>         tracker[user_id] = result
>     memory.close()
>     return
> --- `evaluation/locomo/add.py`

**Reader failure has two different delivery outcomes.** An answer-generation exception is logged and converted into an empty response. The worker then follows its normal record-append path, with no nonempty-answer gate or answer retry in the inspected worker. This can deliver a structurally valid result entry without an answer. Conversely, an exception escaping a worker is re-raised by the coordinator's future check. Under the inspected main sequence, that skips `save`; `finally` still closes the searcher. Worker `finally` also closes its memory object after failures inside its processing block. This is cleanup and failure propagation, not automatic repair, checkpointed partial delivery or all-files rollback (SRC-1, `evaluation/locomo/xMemory_search_framework.py`).

> except Exception as e:
>     logger.warning(f"LLM answer failed: {e}")
>     return ""
> --- `evaluation/locomo/xMemory_search_framework.py`

> for fut in as_completed(futures):
>     # 这里只是确保异常会被抛出来，不再 update 进度
>     fut.result()
> --- `evaluation/locomo/xMemory_search_framework.py`

**Scoring is post-delivery assessment.** [RT-RTE-offline-evaluation](runtime.md#rt-rte-offline-evaluation) supplies the separate response/reference comparison route and its quote. The operator must invoke it over saved output. The inspected scoring loop computes lexical metrics, skips category 5 and does not execute the commented model judge. It neither vetoes the earlier write nor automatically sends failures back into construction or reader policy. No source-supported critic/reviser/retest cycle is established by this workflow. No supplied run proves that the workflow completes, that retries recover, or that selected context improves answers (SRC-1, `evaluation/locomo/evals.py`).

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-adaptive-reader](runtime.md#rt-rte-adaptive-reader)

Workflow delegation: conversation-level executor workers own the sequential search → hydration → answer → record sequence. The coordinator waits on futures, then main saves the collected result. No agent-to-agent goal delegation is established by this executor usage.

Workflow acceptance and recovery: context-admission thresholds do not validate final answers. Generation exceptions can become empty saved responses; escaping worker errors prevent the normal save call. Cleanup does not retry the failed question or guarantee partial-result delivery. Delivery is the results-file write after successful `process` return, separate from later scoring and not atomic with sidecar writes. Supporting source passages are retained in the workflow account above.

#### On [RT-RTE-hierarchy-admission](runtime.md#rt-rte-hierarchy-admission)

Workflow prerequisite gate: exhausted flush attempts returning `None` terminate this construction worker before its hierarchy-maintenance sequence. This does not establish that earlier episode writes are absent or rolled back. The failure branch is retained above; no additional route identity is declared.

#### On [RT-RTE-offline-evaluation](runtime.md#rt-rte-offline-evaluation)

Workflow verification placement: scoring consumes the delivered QA artifact in a separate operator invocation. Its result is assessment, not a pre-delivery acceptance gate or an automatic recovery handoff to memory construction.
