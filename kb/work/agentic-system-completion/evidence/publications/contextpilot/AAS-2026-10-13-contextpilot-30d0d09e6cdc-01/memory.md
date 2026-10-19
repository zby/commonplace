---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ContextPilot memory: per-task findings, relation-assisted read-back, context replacements and trace-derived policy updates."
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
source-identity: "https://github.com/Tencent/ContextPilot"
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot memory report

## Boundary and evidence

The memory scope includes the ordinary and FSM inference paths, training tools and trajectory renderer, document selection, structured memories, simple notes, context replacements, branch copies, recorded traces and policy/checkpoint consumers. It follows the whole-system boundary in [boundary](boundary.md). It excludes external service internals, unpublished weights and unavailable dataset payloads, not the shipped evaluation or training callers. Those exclusions prevent conclusions about actual service transformations, dataset coverage and reproduced performance.

All new evidence is SRC-1, implementation at the frozen revision; the shipped prompt is doctrine/design. Direct reads covered `infer/src/contextpilot.py` store, graph, embedding, retrieval, rendering, context-edit, token-window, cleanup and trajectory-save bodies; `infer/src/contextpilot_fsm.py` mandatory-review recovery; `infer/configs/fsm_plan_bm25_mc_prompt.txt`; `train/verl/tools/contextpilot_memory.py` normalization, signatures, embedding, graph and CRUD bodies; `train/verl/tools/statelm_tools.py` document lifecycle, memory/note tools and editing/compression bodies; `train/verl/experimental/agent_loop/statelm_agent_loop.py` rendering, branch checkpoint/reconstruction and generation passages; and the training launcher's tool-config selection. Tool-name inventories checked the inference JSON and training configurations; selected schema text was read in the launcher's optimized tool YAML. General CLI dispatch, evaluator scoring, automatic training reclamation, reward propagation, optimizer and durable checkpoint conclusions below are supplied runtime findings, not independently audited implementations.

| Entry point or operation | Source path | Coverage and conclusion limit |
| --- | --- | --- |
| Fresh sample; ordinary/FSM selection; resume and retry hints | `infer/src/hf_test_runner.py`, `infer/scripts/eval_task.sh` | Supplied [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference); symbol search confirms separate save/resume paths. No old store reload established. |
| Model `memorize`, `updateMemory`, `note`, `updateNote`; registered training equivalents | `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py` | Direct: [MEM-RTE-findings-write](#mem-rte-findings-write); structured content, symbolic access metadata and vectors separated below. |
| Automatic summary injection; keyed reads; graph expansion; FSM recovery read | `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py` | Direct: [MEM-RTE-findings-delivery](#mem-rte-findings-delivery); no measured incorporation or accuracy. |
| `mergeNotes` exposed library operation | `infer/src/contextpilot.py` | Direct: [MEM-RTE-memory-merge](#mem-rte-memory-merge); implemented but not default-granted. Loss of metadata differs from ordinary CRUD. |
| Document chunking, keyword search, sequential/explicit chunk reads; whole-document alternative | `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py` | Direct inference and training document lifecycle; [MEM-OBJ-document-index](#mem-obj-document-index). Training search/chunk implementation details remain supplied runtime findings; no exhaustive parity assertion. |
| Optional embeddings, semantic/hybrid retrieval and external reranking | `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py` | Direct selected implementations: [MEM-CMP-embedding-provider](#mem-cmp-embedding-provider), [MEM-CMP-reranker-endpoint](#mem-cmp-reranker-endpoint), vector objects below. Not in default inference grant; no observed endpoint identity. |
| Delete, truncate, summarize, compress; implemented restore; automatic eviction | `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py` | Direct explicit editing/rendering and inference token-window; supplied training automatic selection: annotations on [RT-OBJ-full-history](runtime.md#rt-obj-full-history), [RT-RTE-context-control](runtime.md#rt-rte-context-control), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout). |
| Tool grants and prompts | `infer/tools/context-shaper_tools.json`, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `train/examples/sglang_multiturn/config/tool_config/statelm_tool_optimized_config.yaml`, `train/verl/tools/configs/statelm_tools_config.yaml` | Names searched; selected optimized training schemas and full inference prompt read. Custom schemas/Python callers can change grants. Unread schema details prevent exhaustive argument-schema parity claims. |
| Serialized trajectories, answer predictions and evaluator feedback | `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py` | Direct trajectory-save and runner symbol search; supplied [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) for evaluator/caller chain. Raw records do not alone establish learned agent memory. |
| Branch copies, snapshots and reward-derived rows | `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/experimental/agent_loop/agent_loop.py` | Direct clone/reconstruction passages; supplied [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) for ranking, scoring, rejection and reward consumers. |
| Numerical policy updates, checkpoint save/load/retention and rollout consumption | `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`, `train/verl/workers/fsdp_workers.py` | Supplied [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-BAP-rollout-weights](runtime.md#rt-bap-rollout-weights). Saved contents and deployed inference adoption are not established beyond that account. |
| External policy, judge, compressor and embedding/reranker internals | Same adapters; external services not frozen | Opaque provider state: version/configuration can vary. Client wiring does not identify deployed weights, hidden retention or actual transformations. |

No target, test, example, benchmark or provider was executed. Newly inspected paths remain within SRC-1; no source was added. Available but unread code is an inspection limit, not an access gap or absence.

## Core ideas

1. **Two stores, not one external database.** Source-native `notes` holds structured memories; `simple_notes` holds shorter unstructured entries. Both are Python task state. Every later prompt receives all current keys and summaries; a keyed tool read supplies full content. The label `external_memory` means outside the current rendered history, not demonstrated cross-session durability ([MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-simple-notes](#mem-obj-simple-notes), [MEM-RTE-findings-delivery](#mem-rte-findings-delivery)).
2. **Graph retrieval combines a requested anchor with automatic neighbors.** Writes derive entity/time/facet/relation overlap and optional dense similarity. `loadMemory` returns the selected memory plus ranked neighbor summaries, episodes and reasons, not every neighbor's full content. Free-form entity/episode text can remain visible to the policy yet yield fewer parseable graph features ([MEM-OBJ-mem-edges](#mem-obj-mem-edges)).
3. **Cleanup replaces the view, not the underlying trace.** Derived summaries/compressions persist into later calls while originals remain in history. Explicit restoration exists in inference but is not default-granted. Automatic stubbing can exhaust candidates without fitting the window. Neither compactness nor successful edits warrant preservation of all relevant evidence ([RT-RTE-context-control](runtime.md#rt-rte-context-control), annotations below).
4. **Training has a different retained result.** Raw trajectories and branch outcomes feed numerical rewards, advantages and updated policy tensors. Updated rollout weights have a later consumer; human-readable error explanations are not the retained product of that path. This is separate from per-task fact retention and does not establish improved capacity ([RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

## Shared records

### Components

#### MEM-CMP-embedding-provider
Label: Configurable embedding provider

Source-native identity: `_embed_texts` / `_get_emb_client` in inference and `_get_embedding_client` / `_embed_memory_text` in training. Form: distributed-parametric external transformation; substrate: external model/service memory. The adapters do not update provider parameters. Exact weights are not pinned; inference configuration or `EMB_*` environment variables and training environment select model/address, default model name `text-embedding-3-small`. A mutable endpoint can resolve to other weights; internals and deployment are uninspected. Inference registers its embedding callback for memory writes when credentials exist, separately from optional chunk `buildEmbedding`. Training embeds memories when its environment provides a key. Exceptions disable the memory vector channel for the session; deterministic matching remains. Distinct from supplied policy, judge and compressor components, which produce actions, judgments and replacement text rather than retrieval vectors. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py`.

> self._emb_model = os.getenv("EMB_MODEL_ID", "text-embedding-3-small")
> --- `train/verl/tools/contextpilot_memory.py`

> self.state_manager.set_embedding_provider(
>     lambda texts: self._embed_texts(list(texts), is_query=False)
> )
> --- `infer/src/contextpilot.py`

#### MEM-CMP-reranker-endpoint
Label: Optional reranker endpoint

Source-native identity: `_rerank` and `_reranker_config`. Form: opaque external model computation returning symbolic index/score pairs; source describes a cross-encoder and Qwen3 prompt template, not frozen deployed parameters. Substrate: external service; client has no update path. Exact model version is unpinned, and mutable endpoint configuration can resolve to another model. `hybridSearch` sends query and candidate full texts, consumes sorted scores and constructs selected highlights. Distinct from the embedding provider and supplied policy/compactor components; no matching supplied component. SRC-1, `infer/src/contextpilot.py`.

> resp = requests.post(
>     url,
>     json={"query": formatted_query, "documents": formatted_docs},
>     headers=headers,
>     timeout=300,
> )
> --- `infer/src/contextpilot.py`

### Operative objects

#### MEM-OBJ-notes
Label: Structured memory content

Source-native identity: `StateManager.notes`; training `AgentData.memories` aliased as `notes`, operated by `ContextPilotMemoryState`. Substrate: per-agent/trajectory Python dictionaries, copied for branches. Form of the content part: natural-language `summary`, `full_content`/`content`, entity descriptions/evidence and episode/relation descriptions, even when encoded in JSON strings. Their consequences depend on policy interpretation after delivery. Key/source/time access metadata and graph consumers are separated in [MEM-OBJ-mem-edges](#mem-obj-mem-edges). The optional vectors are [MEM-OBJ-mem-embeddings](#mem-obj-mem-embeddings).

Lineage: foreground model writes under the evidence-saving prompt, generally after reading source passages. Software stringifies/normalizes supplied fields; it does not authenticate their truth. Reasons/evidence can be supplied in text, but are not required proof of correctness and need not survive overwrite/merge. `read_note`/`read_memory` copies the stored content; automatic injection uses only summaries. The policy can treat text as evidence/guidance, not as executable dispatch rules. Horizon established by wiring: later invocations within the task and branch copies, not demonstrated reuse on another problem. This is distinct from [RT-OBJ-full-history](runtime.md#rt-obj-full-history): store content is retained independently of old history visibility, not a part of that list. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py`, `train/verl/tools/statelm_tools.py`.

> "summary": self._safe_str(summary),
> "full_content": self._safe_str(content),
> "content": self._safe_str(content),
> --- `train/verl/tools/contextpilot_memory.py`

#### MEM-OBJ-simple-notes
Label: Simple note content

Source-native identity: `simple_notes`; inference `add_simple_note` and training `NoteTool`. Substrate: separate task-local dictionary; form: natural-language summary/full content, with symbolic keys used for addressing. Lineage: model-authored text admitted by software; training also retains a `content` alias. No structured relation-graph indexing is applied by the inspected simple-note write methods. Full entries reach the policy through `readNote`; summary lists reach every subsequent render. Distinct from [MEM-OBJ-notes](#mem-obj-notes), despite the confusing source-native name `notes` for the structured store, and distinct from supplied history. Reasons are optional content, not a dedicated validated rationale. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`.

> self.simple_notes[str(key)] = {"summary": str(summary), "full_content": str(content)}
> --- `infer/src/contextpilot.py`

#### MEM-OBJ-mem-edges
Label: Memory access metadata and relation graph

Source-native identity: structured entry `key`, `source`, timestamps; `_mem_signatures` and `_mem_edges`. Substrate: task-local dictionaries/sets; form: symbolic addressing, normalized term sets, adjacency scores and breakdowns. Lineage: caller-supplied provenance arrays normalized as lists, timestamps generated on writes, and signatures/edges recomputed from stored content. These are neither raw tool traces nor independent evidence validation. The actual graph selector consumes entity/time/facet/relation features and optional vector similarity; `source.chunk_ids` and `source.msg_ids` do not themselves establish evidence correctness or become a query-specific selector.

Weights are entity 3, connecting relation 3, shared time 2 and facet 1, with an optional thresholded similarity bonus. A keyed read ranks graph neighbors and returns `relation_reason`; this is a computational matching explanation, not an explanation of the remembered fact's truth. The policy receives neighbor key, summary, episodes, reason and score, not neighbor full content or all provenance. Deletion removes incident edges; overwrite/append recomputes them. Text normalization accepts strings, while feature extraction parses JSON or JSON lines: arbitrary prose can remain in storage without supplying the advertised structured features. Distinct from supplied history IDs and from content/embedding parts declared here. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py`.

> "relation_reason": copy.deepcopy(edge.get("breakdown", {})),
> "score": int(edge.get("score", 0)),
> --- `train/verl/tools/contextpilot_memory.py`

> for line in text.splitlines():
>     try:
>         parsed = json.loads(line.strip())
>     except Exception:
>         continue
> --- `train/verl/tools/contextpilot_memory.py`

#### MEM-OBJ-mem-embeddings
Label: Memory signature vectors

Source-native identity: `_mem_embeddings`. Form: distributed-parametric dense numerical representations; substrate: local NumPy arrays keyed by memory ID, not provider weights. Lineage: normalized embeddings of summary, entity/episode strings and the first 1500 content characters. They update on write/reindex and are removed on deletion or replacement; provider failure can leave the vector channel unavailable. Consumer: pair scorer's similarity bonus, then symbolic graph edges, then the neighbor selector. Vectors themselves are not rendered to the policy. Distinct from [RT-CMP-actor-module](runtime.md#rt-cmp-actor-module) policy tensors and document chunk vectors. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py`.

> self._safe_str(memory.get("full_content"))[:1500],
> --- `train/verl/tools/contextpilot_memory.py`

#### MEM-OBJ-document-index
Label: Attached document and chunk index

Source-native identity: `ToolLibrary.document`, `encoded_doc`, `index`, `_doc_id`; training `DocStateManager.document_content` and index. Substrate: local text/token offsets/chunk lists plus Elasticsearch rows filtered by document ID. Content form: natural-language source passages; access form: symbolic chunk IDs, token bounds, document IDs and section hints. These are source material and retrieval metadata, not already learned facts or trace-derived summaries. Input origin is the runner's dataset adapter or configured caller; human approval of individual documents is not established by a generic Python caller.

Inference `buildIndex` deterministically slices text using tokenizer offsets, chunk/overlap controls and optional boundary backtracking. `readChunk` supplies a full selected or next sequential chunk; multi-read supplies a bounded set. Keyword search delivers ranked IDs/highlights/section hints, capped by `_search_engine_max_results` (default 20), not the whole document. `loadDocument` is an implemented alternative that can return all text or retain head/tail or head-only tokens under configured limits; it is not in the default schema. Clearing a document deletes its ES material and resets the local index/vector fields; this is not deleting note stores or guaranteeing cleanup on every exception. Training document ownership separates branch-shared indexes from branch-owned replacements. No supplied object has this referent; it is input to, not part of, [RT-OBJ-full-history](runtime.md#rt-obj-full-history). SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`.

> chunk_content = self.document[char_start:char_end]
> --- `infer/src/contextpilot.py`

> query={"term": {"doc_id": self._doc_id}},
> --- `infer/src/contextpilot.py:973-1001`

#### MEM-OBJ-chunk-embeddings
Label: Optional document chunk vectors

Source-native identity: `_chunk_embeddings` and `_emb_dim`. Substrate: local NumPy matrix. Form: distributed-parametric document representations, produced by [MEM-CMP-embedding-provider](#mem-cmp-embedding-provider), not model weights or textual knowledge. Lineage: `buildEmbedding` embeds all indexed chunk contents; semantic search embeds the query with an instruction prefix, compares normalized vectors and returns bounded chunk previews. Hybrid retrieval reranks candidate vectors or uses the optional external reranker; if too few BM25 candidates exist it can use all chunks, and it can backfill low/filtered semantic results by BM25. A result label therefore does not prove every returned item exceeded the semantic threshold. Clearing the document resets this matrix; equivalence under arbitrary reindex/reconfiguration sequences was not audited. Distinct from memory-signature vectors and supplied actor tensors. SRC-1, `infer/src/contextpilot.py`.

> "backfilled_by_bm25": True,
> --- `infer/src/contextpilot.py`

### Routes

#### MEM-RTE-findings-write
Label: Model findings admission

Progression: model's `memorize`/`note`/update arguments → inference dispatcher or training registered tool → store normalization/mutation → graph reindex for structured memories → later summary or explicit read. Owner: foreground model proposes content; software admits it after tool availability, key/mode/content checks. The shipped prompt asks to preserve durable evidence and temporal/relational qualifiers. Operating mode: bounded document QA; there is no answer oracle or independent fact-validation veto at this write boundary. Humans select launch/configuration, not each saved fact in the inspected path. New writes to an existing key replace it; append, overwrite and delete are explicit update modes. Missing keys/invalid modes and missing required overwrite content can reject updates. Software provenance normalization is not source entailment checking. Recovery is subsequent rewriting, retained old trace or branch copy, not a transactional store revision log. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py`.

Distinct identity: a store-mutation subroute of inference and training invocation routes, spanning [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference) and [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), not a replacement for any one of them.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success/key/structured marker or error; training tool wrappers return zero local reward, separately from terminal scoring.
- Later read-back: Current summaries and keyed content reach later policy calls through [MEM-RTE-findings-delivery](#mem-rte-findings-delivery).
- Delegated visibility: Local tools see parsed arguments and task state; embedding service may see signature text. No helper-agent report is involved.
- Selection predicate: Available tool and dispatch/state checks; key addressing and update mode, with normalization of optional structures. Store methods themselves are also callable by trusted Python code.
- Invalidation or expiry: Delete removes entry and structured graph state; overwrite replaces content and reindexes; append mutates content/features. A fresh agent/trajectory creates fresh stores. Old rendered results or snapshots can retain superseded text.
- Activation or effect: Store changes and later delivery are wired. Correct facts, useful retention and semantic incorporation are unobserved.
- Evidence limits: No run evidence; model-authored provenance/evidence text is not independently verified. Training and inference differ in simple-note summary update semantics.

> self.notes[key] = self._build_memory(key, content, summary, entities, episodes, relations, source)
> self._reindex_memory(key, recompute_embedding=True)
> --- `train/verl/tools/contextpilot_memory.py`

#### MEM-RTE-findings-delivery
Label: Summary injection and keyed memory read

Progression: each payload rebuild selects all current store summaries; separately, a model reader call selects a key and structured graph neighbors; FSM API-failure recovery can select the last inserted key → text/JSON rendering → later policy invocation. Owner: renderer for automatic injection, foreground model for requested key, graph code for neighbors, FSM for recovery selection. Bounded QA mode; reads do not admit content changes and have no answer oracle. This is the retention-delivery subroute shared by [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), not a duplicate of their full invocations. SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `readNote` copies selected note; `loadMemory` returns selected structured entry plus directly related memories, or a missing-key error. Summary injection is part of prompt construction, not a separate tool return.
- Later read-back: Automatic lists go into the first user message; read results enter tool history and then subsequent model input, subject to edits/eviction. Full selected entry includes content and provenance; neighbor projections do not include full content.
- Delegated visibility: External policy sees rendered lists/results only; graph and stores remain in local state. Copying data does not expose dereferenceable host pointers.
- Selection predicate: Injection selects every key and current summary without query ranking or a separate summary token budget. Keyed reads use the requested exact key; neighbors sort precomputed scores and default to five. Training's wrapper converts zero `max_related` to five. FSM recovery after API failure chooses the latest dictionary key, not semantically most relevant content.
- Invalidation or expiry: Current store changes affect future lists; history edits can hide old read results. Previously serialized snapshots are not retroactively corrected. Fresh task state resets the stores.
- Activation or effect: Model-visible delivery is wired; summary presence or mandatory reader success does not prove reliance on the content or a correct final answer.
- Evidence limits: No observed provider invocation. Injected summary lists can themselves exceed context budget; neither key existence nor relation score warrants source truth or complete evidence coverage.

> text += (external_context_summary if idx == 0 else "")
> --- `infer/src/contextpilot.py`

> "memory": copy.deepcopy(memory),
> "directly_related_memories": self._related_memories(key, max_related=max_related),
> --- `train/verl/tools/contextpilot_memory.py`

> key = str(list(mandatory_store.keys())[-1])
> --- `infer/src/contextpilot_fsm.py`

#### MEM-RTE-memory-merge
Label: Optional structured memory merge

Progression: trusted/configured `mergeNotes` call → remove existing selected structured memories and their graph edges → concatenate summaries/content into a new entry → future summary injection or keyed read. Owner: caller proposes keys/new key/optional summary, code admits existing keys. The tool name is misleading: `merge_notes` operates on structured `notes`, not `simple_notes`. It is an exposed library capability, not a default-granted inference action or registered training counterpart in the inspected tool-name inventory. Invocation by an external configured caller is afforded; actual deployment is uninspected. Distinct from default write modes and closest to [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference), whose configured tool set could grant it. SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`, `train/examples/sglang_multiturn/config/tool_config/statelm_tool_optimized_config.yaml`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Success/new key/merged-from list, or error when no requested entries exist.
- Later read-back: New entry summary appears in subsequent renderings; `loadMemory` can copy the entry by key. No dedicated deployed caller is established beyond configurable dispatch/library access.
- Delegated visibility: Merge is local concatenation, not a summarizer model call. A caller-supplied summary can replace concatenated summaries.
- Selection predicate: Requested existing keys; missing keys are ignored. New key is supplied or joined from selected keys.
- Invalidation or expiry: Originals and incident graph state are removed. New entry has summary/full content only, dropping structured provenance/entities/episodes/relations and not immediately reindexing the merged entry. A new-key collision can replace existing content. No transactional rollback is implemented in this body.
- Activation or effect: A future list/keyed read can deliver merged text, but immediate graph coverage and semantic preservation are not guaranteed.
- Evidence limits: No default grant or execution. The implementation is a capability, not evidence that this transformation occurs in ordinary runs; omission of metadata is directly visible in the constructor below.

Admission: generic caller identity leaves per-content human control unresolved; the code does not request human approval. No answer oracle is used. Guidance for a hypothetical configured caller is uninspected; what persists is concatenated or supplied summary and content, not a criticism or validated synthesis. Recovery requires caller rewrite or other retained copies.

> self.notes[merged_key] = {"summary": str(existing_summary), "full_content": str(merged_content)}
> --- `infer/src/contextpilot.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-full-history](runtime.md#rt-obj-full-history)

Memory-specific parts: `summarized_msg_ids` holds model-supplied summaries and compressor-produced text; `truncated_msg_ids` holds selected spans with wrappers. Form: natural-language replacement content plus symbolic ID/precedence maps; substrate: task-local dictionaries alongside unchanged original history. These parts differ from the raw original tool messages. Render precedence is delete, summarize/compress, truncate, then original. A returned cleanup success or replacement length is not the replacement's warrant. Training has analogous maps. The later reader is the next policy invocation through the rendered message position; content can guide model interpretation, while IDs/sets control fixed visibility. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`.

Raw-to-derived chain: old tool/assistant message → foreground summary or selected span, or external compressor output → replacement map → later rendered model input. Compressor failure falls back to random word sampling, not a guaranteed semantic summary. Reasons for what was removed need not persist; originals remain host-reachable, and text may retain reasons only if supplied/selected. The clone path copies maps and history for branch continuation; exported trajectories include originals and edit maps as separate fields, not just final visible context.

> "full_history": self._sanitize_for_json(self.full_history),
> "deleted_msg_ids": sorted(self.deleted_msg_ids),
> "summarized_msg_ids": {str(k): v for k, v in self.summarized_msg_ids.items()},
> --- `infer/src/contextpilot.py`

#### On [RT-RTE-context-control](runtime.md#rt-rte-context-control)

Read-back/curation: a model selects message IDs and either a span or a manual summary; automatic compression delegates selected original text to [RT-CMP-llmlingua2](runtime.md#rt-cmp-llmlingua2). The percentage is a requested keep rate, not verified evidence coverage. Training's compression adapter has the same external-call/fallback distinction. Its local fallback is sampled words in original order; nonpositive keep rate can yield an empty body. Both inferred success and factual preservation therefore require separate evidence. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`.

> sampled_indices = sorted(random.sample(range(len(words)), keep_count))
> return " ".join(words[i] for i in sampled_indices)
> --- `train/verl/tools/statelm_tools.py`

Inference explicit delete/truncate/summary/compress admits by message existence/role and supplied arguments, records restore eligibility, and retains the original. `restoreContext` clears markers only for eligible IDs; default tool JSON does not grant it. Automatic token-window stubbing instead persistently hides earliest eligible assistant/tool pairs, preserving system/question/store summaries and old snapshots, but does not automatically confer restore eligibility. Host overflow recovery preferentially removes read context, as supplied runtime establishes. No human approval or semantic adequacy oracle gates these edits. This is shared-window view editing, not a separate sub-agent frame whose return value alone escapes. Values are copied into the window, so a key or stub is not a pointer the model can automatically follow.

> self.restorable_msg_ids.add(msg_id_int)
> result = {
>     "status": "success",
>     "msg_id": msg_id_int,
>     "compression_rate": compression_rate,
> --- `infer/src/contextpilot.py`

#### On [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)

The training renderer independently injects all memory/note summaries into the first user message and applies replacement maps to old history. Foreground edits use ID/role checks; automatic budget reclamation is the supplied runtime's token-measured selection of large read/search results, with termination on nonprogress/budget violation. Original history and store dictionaries remain separate from the rendered view. No explicit restore grant was found in the selected training tool inventory; this is a bounded grant finding, not an absence of host reconstruction capability. Per-trajectory state and branch-owned document cleanup bound lifetime, not proven cross-session memory. SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/tools/statelm_tools.py`, `train/examples/sglang_multiturn/config/tool_config/statelm_tool_optimized_config.yaml`.

> text = msg["content"] + external_context_summary
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

Training simple-note update differs from inference: omitted `new_summary` is stringified to empty and assigned, whereas inference retains the old summary when the argument is absent. Thus a content-only training edit can erase the automatically advertised summary without deleting full content. This narrows any inference-to-training parity assumption. SRC-1, `train/verl/tools/statelm_tools.py`, `infer/src/contextpilot.py`.

> new_summary = _safe_str(parameters.get("new_summary"))
> --- `train/verl/tools/statelm_tools.py`

> simple_notes[key]["summary"] = new_summary
> --- `train/verl/tools/statelm_tools.py`

#### On [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit)

Branches copy memories, simple notes, original history and editing maps, while document-index ownership can be shared. Parent reconstruction resets generation state and truncates history to the pre-generation checkpoint; inspected generation captures that checkpoint before proposing/executing the management action. This supports the supplied pre-action account, not the stronger assertion that a branch isolates the causal effect of one deletion. SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`.

> branch_data.memories = copy.deepcopy(agent_data.memories)
> branch_data.notes = branch_data.memories
> branch_data.simple_notes = copy.deepcopy(agent_data.simple_notes)
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

Trace-fed update has two consumers with different authority. Terminal outcomes and ancestry feed numeric snapshot rewards and training-row selection; branch history is raw evidence for that computation, not necessarily later policy input as prose. Then [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) consumes advantages to change parameters. Supplied runtime establishes terminal-ancestry rejection/drop and branch-failure exclusion, so retained snapshots cannot be assumed all admitted into training. No observed branch or reward was supplied.

#### On [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)

Trace origin is generated task actions/outcomes scored against dataset references, with model judge or symbolic correctness and penalties; it is not solely human-authored experience. Durable behavior-shaping result is numerical policy/checkpoint state, consumed by later rollout weight synchronization and configured training reload. Raw logs alone do not close this chain. Source and minimum passages are supplied in this record and [RT-BAP-rollout-weights](runtime.md#rt-bap-rollout-weights).

The parameter consumer receives gradients/advantages, not inspectable criticisms and reasons attached to each memory decision. Checkpoint reload and retention are distinct from note-store CRUD: older checkpoints may be removed, save contents are configured, and validation is not an inspected per-update promote-only-if-better gate. Deployed inference adoption remains uninspected. This wiring supports trace-responsive adaptation, not measured improved capacity or exercised beneficial self-change.

## Write side

Acquisition starts with caller-supplied document text; deterministic chunking preserves slices and access metadata, while search supplies selected highlights. These are not automatically curated memory. The foreground model chooses what to retain under the shipped prompt, then [MEM-RTE-findings-write](#mem-rte-findings-write) admits text without independent entailment validation. Software owns normalization, timestamping, graph reconstruction and optional signature embeddings. Human selection of a run does not establish human approval of its facts. Generic library initialization may supply arbitrary dictionaries, so original human/model provenance is unresolved for those callers, while subsequent transformations remain inspectable.

The retention prompt explicitly distinguishes saved facts from long assistant reasoning:

> - Keep reasoning before tool calls brief. Put durable facts into `memorize` / `updateMemory` or `note` / `updateNote` instead of long assistant prose.
> --- `infer/configs/fsm_plan_bm25_mc_prompt.txt`

Updates can append, replace or delete; graph edges are rebuilt or withdrawn with structured entry changes. Deleting a memory prevents later current-store lookup/injection, but does not purge earlier tool results, branch copies or serialized traces. The optional merge route removes originals and drops structured metadata; it is not a validated semantic synthesis. Reasons can survive in model text and relation evidence fields, but neither CRUD nor compaction enforces their retention. Full keyed reads can expose them; summary injection and neighbor projections expose only their selected fields ([MEM-RTE-findings-delivery](#mem-rte-findings-delivery)).

Context curation is separate: manual summary, selected verbatim span, external compression or random-word fallback replaces model-visible history. Software validates target/role, not factual sufficiency; automatic eviction selects by age or measured budget reduction. These can preserve a derived result for the next invocation even within one run. Original-history retention is a recovery affordance, not proof the policy can restore it under its current grant. See annotations on [RT-OBJ-full-history](runtime.md#rt-obj-full-history) and [RT-RTE-context-control](runtime.md#rt-rte-context-control).

Evaluation retains answers/trajectory artifacts and supplies scoring or retry hints through shipped callers. This is raw task evidence and a bounded feedback channel, not automatic recovery of the original memory store. Training is the separate raw-trace → scored terminal descendants → snapshot rewards/advantages → parameter update → rollout/checkpoint consumer chain. Computational filters can reject malformed/no-terminal rows or nonfinite-gradient steps; periodic validation is not an inspected mandatory quality veto. Parameter checkpoints and dataloader recovery differ from task memories and live branch copies ([RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

## Read-back

There are three materially different selection channels:

- **Automatic push of summaries:** every render selects all current keys and summaries, independent of a fresh memory request. It is not query-specific retrieval and has no separate list-size budget in the inspected renderer. It keeps entries discoverable after old writes/reads are hidden.
- **Requested full entries with automatic expansion:** `readNote` returns the keyed note; `loadMemory` returns the keyed structured memory and graph-ranked neighbor projections. The model selects the anchor using advertised keys; graph code chooses extra parts. FSM failure recovery can instead select the last key automatically. The neighbor cap is a count, not a total text-token budget. These are wired consumers, not hypothetical APIs alone ([MEM-RTE-findings-delivery](#mem-rte-findings-delivery)).
- **Derived context at its old position:** manual summary, compressed output, span or deletion stub replaces the original on every later render until superseded/restored/reset. Selection uses message IDs, not an independently retrieved knowledge index. Inference's optional restore can re-expose the original; training branch reconstruction copies/restores checkpoint-relative state rather than adding the inference restore grant.

Document search is a source-evidence path, not necessarily read-back of material learned through prior use. BM25 highlights, semantic previews and hybrid backfill have different completeness/trust limits. Whole-document and sequential-read alternatives can expose other material but do not establish that ordinary runs inspect it. Neither document passage delivery nor saved summaries give text symbolic authority to change the dispatcher. At the policy consumer their force is model-interpreted evidence/guidance; at graph/renderer consumers IDs, scores and markers have fixed computational effects.

Updated training weights have a fourth, nontextual channel: parameter synchronization determines later rollout token distributions. Saved checkpoints permit configured recovery; raw inference logs and predictions have evaluator/operator consumers, not an established fresh-task note reload. No path here is observed activation or demonstrated benefit.

## Integration issues

- No supported correction to the supplied runtime is required. The branch checkpoint timing was challenged against generation/reconstruction passages and supports its pre-action account. The read-back and context guarantees remain intentionally weaker than semantic incorporation.
- [MEM-RTE-findings-write](#mem-rte-findings-write) and [MEM-RTE-findings-delivery](#mem-rte-findings-delivery) refine common subroutes spanning the supplied inference/training invocations; they are not whole-record duplicates. [MEM-RTE-memory-merge](#mem-rte-memory-merge) is an optional exposed operation, not a default route. No newly declared object/component duplicates a supplied referent after comparison; history and policy records receive annotations instead.
- Inference and training are not identical stores: training simple-note updates can clear an omitted summary; arbitrary entity/episode prose can fail JSON feature extraction; merge can discard structured metadata. These findings concern [MEM-OBJ-simple-notes](#mem-obj-simple-notes), [MEM-OBJ-mem-edges](#mem-obj-mem-edges), [MEM-RTE-memory-merge](#mem-rte-memory-merge). Reconciliation should not generalize a schema label into uniform graph coverage or lossless curation.
- External embedding, reranker, judge, compressor and policy identities/hidden retention remain unresolved. Configuration names do not identify exact weights. Consequently actual retrieval quality, factual preservation, endpoint-side persistence and provider-specific authority remain unestablished ([MEM-CMP-embedding-provider](#mem-cmp-embedding-provider), [MEM-CMP-reranker-endpoint](#mem-cmp-reranker-endpoint), [RT-CMP-llmlingua2](runtime.md#rt-cmp-llmlingua2)).
- Caller initialization provenance, arbitrary reindex/configuration coherence and exact schema/implementation parity beyond the inspected grants remain open inspection questions, not absences. They prevent stronger universal provenance/cache/parity claims, not the directly traced write/read/render findings ([MEM-OBJ-document-index](#mem-obj-document-index), [MEM-OBJ-chunk-embeddings](#mem-obj-chunk-embeddings)). No execution evidence resolves durable cross-task store use, actual policy update exercise or beneficial learning ([RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

## Limitations and checks

Source identity recheck: checkout HEAD was `782cbb6611fb610c4cf6fafda6022b7e89cae191`; `git status --short` returned no changes at inspection. Frontmatter repeats the handed boundary/run identities exactly. The supplied invocation, governing types, worker rules, collection contract and shared records contract were read completely, recovering bounded reads. No peers beyond supplied boundary/runtime, prior analyses or engine-owned run metadata were inspected.

The evidence supports implementation wiring and exposed capabilities, not observed activation, successful cleanup/recovery, correct memories, complete document coverage, durable cross-session memory, learned improvement or causal benefit. Optional API operations are not promoted to deployed routes. The source's complete system boundary does not imply an exhaustive audit of every dependency or alternate configuration. Supplied runtime findings remain attributed where not directly re-inspected.

Validation: the invocation-specific `commonplace-run validate-output` check passed; it checks structure and quotation occurrence, not semantic support or final acceptance.
