---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "ContextPilot memory: keyed evidence stores, lossy context views, related-entry expansion and trace-fed training snapshots."
run-id: AAS-2026-10-19-contextpilot-0826e2df5b2f-01
source-identity: "https://github.com/Tencent/ContextPilot"
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot memory report

## Boundary and evidence

This report covers ContextPilot's within-sample memory and working-context controls, their training counterparts, saved traces and reward-fed actor state. The frozen source is SRC-1 at commit `782cbb6611fb610c4cf6fafda6022b7e89cae191`, as registered in [boundary](boundary.md). Direct inspection supplies implementation evidence and shipped-prompt doctrine, not observed execution. The supplied [runtime report](runtime.md) supplies the broader invocation, reward, checkpoint and recovery traces. No target code, tests, model calls or services were executed.

The scope follows both inference callers and the training tool registry, rather than equating memory with one dictionary. External model internals, live Elasticsearch state, unavailable benchmark payloads and the linked paper remain outside the acquired evidence. They prevent conclusions about actual retrieval quality, semantic fidelity, exercised learning and deployment durability. Static prompts are guidance, not learned read-back. Document indexes are included as working-context acquisition substrates, not automatically classified as accumulated experiential memory (SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`; [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)).

### Coverage inventory

“Direct” means source text read or a scoped dispatch/schema search in this attempt; “supplied” identifies reliance on runtime findings. Available but uninspected details are not access gaps.

| Entry point or operation | Source path and evidence basis | Covering records or bounded limit |
|---|---|---|
| Evaluation CLI, per-sample creation, FSM/base dispatch, resume and result writers | Direct: `infer/scripts/eval_task.sh`, `infer/src/hf_test_runner.py`; supplied runtime progression | [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-RTE-base-inference](runtime.md#rt-rte-base-inference), [RT-OBJ-full-history](runtime.md#rt-obj-full-history). Fresh sample state and skip-based resume do not establish cross-task memory reload. |
| Registered memory/note tools; keyed admission, revision and reads | Direct: `infer/tools/context-shaper_tools.json`, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py` | [MEM-RTE-inference-stores](#mem-rte-inference-stores), [MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-simple-notes](#mem-obj-simple-notes). FSM read-key correction and mandatory recovery qualify model-only selection. |
| Automatic summary inventories and related-entry expansion | Direct: `infer/src/contextpilot.py` | [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes), [MEM-RTE-inference-stores](#mem-rte-inference-stores). Full primary entry differs from neighboring summaries/episodes. |
| Exposed merge and restore operations | Direct: `infer/src/contextpilot.py`, schema-name inventory in `infer/tools/context-shaper_tools.json`, state filters in `infer/src/contextpilot_fsm.py` | Merge capability is described in [MEM-OBJ-notes](#mem-obj-notes); no merge consumer route is established. Restore is implemented but not listed in the inspected default inference schema. Configuration-dependent execution must not be promoted to ordinary availability. |
| Explicit cleanup, token-window pruning, overflow hooks and compression | Direct handlers in `infer/src/contextpilot.py`; supplied detailed overflow/token-window/FSM traces | [RT-RTE-context-edit](runtime.md#rt-rte-context-edit), [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks), [RT-CMP-compression-model](runtime.md#rt-cmp-compression-model). Original history differs from the model-visible view. |
| Document indexing, optional retrieval services and cleanup | Direct cleanup in `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`; supplied retrieval paths | [RT-RTE-document-qa](runtime.md#rt-rte-document-qa), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider). Detailed chunk/reranker ranking bodies not inspected here; no completeness or isolation claim. |
| Training registry and memory tools | Direct: `train/examples/sglang_multiturn/config/tool_config/statelm_tool_optimized_config.yaml`, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py` | [MEM-RTE-training-stores](#mem-rte-training-stores), [MEM-OBJ-memories](#mem-obj-memories), [MEM-OBJ-training-notes](#mem-obj-training-notes), [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes). Different admission details are retained separately from inference. |
| Training render, explicit edits, proactive cleanup and length checkpoints | Direct: `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/tools/statelm_tools.py`, launcher configuration search | [MEM-RTE-training-context](#mem-rte-training-context), [MEM-OBJ-trajectory-snapshots](#mem-obj-trajectory-snapshots). Includes code-authored trainable cleanup actions, not just sampled actions. |
| Branch clone, snapshot scoring, actor update, save/load and validation | Direct branch-field/snapshot paths; supplied worker/reward/estimator/PPO inspection | [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), [RT-RTE-actor-update](runtime.md#rt-rte-actor-update), [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor). Optimizer internals, export and production adoption remain untraced. |
| Maintenance instructions and source trust | Direct: `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `train/configs/contextpilot_system_prompt.txt` | [MEM-RTE-inference-stores](#mem-rte-inference-stores), [MEM-RTE-training-stores](#mem-rte-training-stores). They request evidence preservation and review; admission does not authenticate claims or source IDs. |

All paths in this table are SRC-1 commit-relative anchors. The inventory covers the material memory routes found in the frozen CLI, tool registries, local dispatch and cleanup hooks. It does not claim exhaustive auditing of generic verl extension machinery.

## Core ideas

1. **A compact inventory is pushed; full entries are pulled.** Payload construction automatically appends all current keys and summaries to the original question. The model can request one exact key; `loadMemory` additionally expands to ranked neighbors. This expansion is driven by the selected memory, not by a new question-to-store search. Full neighboring content is not delivered by that expansion ([MEM-RTE-inference-stores](#mem-rte-inference-stores), [MEM-RTE-training-stores](#mem-rte-training-stores)).
2. **Saved content and context eviction have different lifecycles.** Deleting a bulky message changes its rendered view, not the underlying history or a separately saved entry. Overwriting a store entry changes later inventories and reads, but does not retract copies already delivered in old tool results. Restoration and store revision are therefore different operations ([RT-OBJ-context-masks](runtime.md#rt-obj-context-masks), [MEM-RTE-inference-stores](#mem-rte-inference-stores)).
3. **Structured memory is model-authored evidence, not validated fact.** Entities, episodes, relations and source IDs accompany text, but their normalization and ranking do not verify the document claim. Optional embeddings contribute selection metadata; they are not the readable entry. Prompts request preservation of attribution and temporal qualifiers without guaranteeing it ([MEM-OBJ-notes](#mem-obj-notes), [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes)).
4. **Training retains more than sampled behavior.** In addition to model edits and retrieval snapshots, proactive recovery can create a synthetic `deleteContext` action with trainable token masks. When it cannot isolate a valid suffix, the same cleanup is conditioning only. Both variants alter subsequent context; only the trainable variant supplies that synthetic action to snapshot credit and actor training ([MEM-RTE-training-context](#mem-rte-training-context), [RT-RTE-actor-update](runtime.md#rt-rte-actor-update)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Inference structured memories in StateManager.notes

Source-native `StateManager.notes` is a per-agent Python dictionary. Its `summary`, `full_content`/`content`, entity and episode strings contain natural-language material interpreted by the policy. Keys, source ID lists, timestamps and relation envelopes have symbolic access/normalization roles; entity/relation values also feed fixed feature extraction. They are not independently authenticated propositions. Text originates in model tool arguments, normally after document search/read, but the writer accepts content without proving that lineage. `source.chunk_ids` and `source.msg_ids` preserve only supplied lists, not a verified derivation or mandatory reason for a claim (SRC-1, `infer/src/contextpilot.py`).

The full entry is consumed by `loadMemory`; its summary is consumed on subsequent payload builds. Scope is the agent/sample lifetime. This is distinct from the history and mask containers in [RT-OBJ-full-history](runtime.md#rt-obj-full-history) and [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks): a store entry survives masking its original write/read messages, while those objects hold traces or view controls. No supplied record declares this dictionary separately.

> "relations": self._normalize_relations(relations),
> "source": self._normalize_source(source),
> "created_at": datetime.utcnow().isoformat() + "Z",
> "updated_at": datetime.utcnow().isoformat() + "Z",
> --- `infer/src/contextpilot.py`

The exposed `merge_notes`/`mergeNotes` capability deletes found input entries, concatenates summaries/content and constructs an entry containing only `summary` and `full_content`. It does not retain their structured fields or immediately reindex the merged entry; missing inputs are skipped. Thus “merge” is not semantic reconciliation, and its graph readiness differs from ordinary add/update. The inspected default schema lists neither `mergeNotes` nor `restoreContext`; the existence of a method alone supplies no later merge caller (SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`).

> self.notes[merged_key] = {"summary": str(existing_summary), "full_content": str(merged_content)}
> --- `infer/src/contextpilot.py`

#### MEM-OBJ-simple-notes
Label: Inference simple notes

`StateManager.simple_notes` is a separate per-agent Python dictionary keyed by strings, holding natural-language `summary` and `full_content`. Its symbolic key selects a value; the policy interprets that value. It has no structured-memory graph fields or required provenance. Model arguments supply the text; the summary inventory and `readNote` deliver it later. It is distinct from [MEM-OBJ-notes](#mem-obj-notes), whose `notes` name actually denotes the richer memory store, and from [RT-OBJ-full-history](runtime.md#rt-obj-full-history), which records messages rather than this current keyed state (SRC-1, `infer/src/contextpilot.py`).

> def add_simple_note(self, key, content, summary):
>     self.simple_notes[str(key)] = {"summary": str(summary), "full_content": str(content)}
>     return {"status": "success", "key": key}
> --- `infer/src/contextpilot.py`

#### MEM-OBJ-memories
Label: Training AgentData.memories

Training `AgentData.memories`, aliased by `notes`, is a mutable dictionary interpreted through `ContextPilotMemoryState`. It stores the richer text/structured fields, source ID lists and timestamps in the training process. Natural-language content reaches descendant policy invocations; symbolic keys/metadata drive reads, rendering, source-list merging and relation indexing. It is not a parameter checkpoint. Branch cloning deep-copies it; a branch gets a current store, not a live shared textual memory (SRC-1, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

It is a distinct operative object from inference [MEM-OBJ-notes](#mem-obj-notes): different state owner and admission wrappers, with branch consumers. The closest supplied record is [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), a route rather than a declaration of this store. Its supplied clone quotation establishes branch lineage.

> def _get_memory_state(agent_data) -> ContextPilotMemoryState:
>     memories, _ = _ensure_memory_stores(agent_data)
>     state = getattr(agent_data, "_contextpilot_memory_state", None)
>     if not isinstance(state, ContextPilotMemoryState) or state.notes is not memories:
>         state = ContextPilotMemoryState(memories)
>         agent_data._contextpilot_memory_state = state
>     return state
> --- `train/verl/tools/statelm_tools.py`

#### MEM-OBJ-training-notes
Label: Training AgentData.simple_notes

`AgentData.simple_notes` contains natural-language summary/full-content strings plus a `content` alias in a symbolic keyed dictionary. It is local to the training trajectory and deep-copied into branches. The summary enters rendered inventories; `ReadNoteTool` returns a copy of the selected value. The model supplies content without mandatory evidence IDs. This is separate from [MEM-OBJ-memories](#mem-obj-memories), including its graph, and from inference [MEM-OBJ-simple-notes](#mem-obj-simple-notes), whose update checks differ. The closest supplied record is again the containing training route [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout), not a duplicate object (SRC-1, `train/verl/tools/statelm_tools.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

> simple_notes[str(key)] = {"summary": _safe_str(parameters.get("summary")), "full_content": _safe_str(parameters.get("content")), "content": _safe_str(parameters.get("content"))}
> --- `train/verl/tools/statelm_tools.py`

#### MEM-OBJ-memory-indexes
Label: Memory signatures, embeddings and relation edges

Inference `StateManager` and training `ContextPilotMemoryState` each maintain three separate in-process caches. `_mem_signatures` contains symbolic feature sets and a text signature derived from entry summaries, entities, episodes and the first 1500 full-content characters. `_mem_edges` contains fixed-rule scores, feature-overlap/relation breakdowns and optional vector similarity. `_mem_embeddings` contains normalized numerical vectors, a distributed representation derived through the embedding provider. These are access metadata, not another authored memory body. Their distinct roles matter: the selector uses numerical/symbolic data while the policy receives neighbor keys, summaries, episodes, score and a readable breakdown; the actual dense vectors and stored `vector_sim` are not returned in those neighbor dictionaries (SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py`).

This is distinct from the provider component [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider): that record describes the producing service, not these derived cached values. Provider parameter/version limits remain as stated there. Training also takes embedding credentials/model IDs from its environment, performs no provider training in the inspected methods, and does not pin exact provider weights; a configured mutable endpoint can resolve differently. Failure disables its vector channel while fixed-rule relation scoring continues. No vector quality or operational use is observed (SRC-1, `train/verl/tools/contextpilot_memory.py`).

> if not os.getenv("EMB_OPENAI_API_KEY") or self._embedding_disabled:
>     return None
> --- `train/verl/tools/contextpilot_memory.py`

> related.append({
>     "key": other_key,
>     "summary": other.get("summary", ""),
>     "episodes": deepcopy(other.get("episodes", [])),
>     "relation_reason": deepcopy(edge.get("breakdown", {})),
>     "score": int(edge.get("score", 0)),
> })
> --- `infer/src/contextpilot.py`

Add/append/overwrite recompute incident edges; deletion removes the key and incident caches. The merge capability is an exception to immediate reconstruction, as noted in [MEM-OBJ-notes](#mem-obj-notes). Retained scoring reasons explain the fixed selector's overlap basis, not the truth or original rationale of the selected factual claim.

#### MEM-OBJ-trajectory-snapshots
Label: Training trajectory snapshots and length boundaries

Training `trajectory_snapshots` holds symbolic token IDs, response masks/log-probabilities, turn counts and node/prefix metadata in Python structures returned to the worker. Decoded text represents prompts/actions; numerical log-probabilities and mask fields govern learning rather than conveying a claim to the QA model. Ordinary context-edit/memory-write/retrieval boundaries retain prompt/response arrays; alternative length boundaries can retain an empty response-ID suffix when the current prompt no longer ends in the accumulated response IDs. They also mark themselves non-branchable. This distinguishes the serialized training checkpoint form from a simple full raw transcript (SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

The closest supplied object [RT-OBJ-full-history](runtime.md#rt-obj-full-history) covers inference histories/payload snapshots and JSON logging; these training arrays have separate producers, reward lineage and actor-update consumers. They are not duplicate declarations. The broader flow is [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout) into [RT-RTE-actor-update](runtime.md#rt-rte-actor-update).

> current_response_ids = copy.deepcopy(agent_data.response_ids)
> if current_response_ids and agent_data.prompt_ids[-len(current_response_ids) :] != current_response_ids:
>     current_response_ids = []
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

> "contextpilot_length_boundary": True,
> "contextpilot_branchable": False,
> "contextpilot_length_boundary_reason": reason,
> "contextpilot_auto_delete_context": auto_delete_context,
> "contextpilot_forced_action": forced_action,
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

### Routes

#### MEM-RTE-inference-stores
Label: Inference store admission and read-back
Part of: [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)

This is the keyed-store subroute inside the FSM invocation, not a replacement for the containing QA route. The same base handlers and payload builder are also used by [RT-RTE-base-inference](runtime.md#rt-rte-base-inference); that alternate caller does not inherit FSM ordering. Endpoints: model memory/note arguments to current keyed state to inventories and explicit tool results to later policy invocations. Owner: Python StateManager/ToolLibrary and payload builder; foreground policy proposes content and requested keys. Key/role/state checks admit operations, not semantic truth. Humans choose document, model, prompt and schema; launching evaluation is not per-entry approval. No reference-answer oracle participates in these store writes; ordinary QA and retry modes retain the distinction in the parent record (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Add/update/delete success or error; a read returns the full selected memory plus bounded neighbor displays, or the full simple note.
- Later read-back: On subsequent payload builds, all current keys/summaries are appended to the first user question. Requested read results deliver full selected entries as tool text to later policy calls; neighboring displays contain summaries/episodes, not full neighbor bodies.
- Delegated visibility: The policy endpoint sees rendered inventories and selected tool results; optional embedding service receives signature text. No independent reviewer receives or approves the stored claim.
- Selection predicate: Policy supplies a key from the advertised store; FSM validates it and can autocorrect to the newest insertion in mandatory states or to a sole available key. Related neighbors are automatically sorted by positive fixed-rule/optional-vector scores for that key, with default max_related 5. Inventory construction iterates all entries without a relevance selector or local token budget.
- Invalidation or expiry: Delete removes current entry and graph edges; overwrite replaces it; append changes content and optionally summary. Already recorded tool-result copies remain in history until separately masked. Per-sample recreation bounds ordinary store lifetime; no inspected driver reload extends it across samples.
- Activation or effect: Subsequent payload delivery is wired. Relevant semantic review, factual correctness, behavioral dependence and answer benefit are unobserved.
- Evidence limits: FSM schema fallback, emergency reads and base dispatch qualify mandatory-review claims. Default schema omits merge/restore operations despite exposed implementations. No deployed model/store was inspected.

Guidance requests saving useful findings, preserving relation direction/qualifiers and reviewing before finish. On add, a reused key replaces the old value without content comparison. Update rejects absent keys/invalid modes; structured overwrite requires new content, while simple-note append/overwrite requires new content and preserves the old summary if none is supplied. Software has no per-content human veto, source authentication or semantic rollback. Model-directed delete/overwrite is the available store revision mechanism; prior versions are not kept in this dictionary. Graph metadata updates automatically, separately from authorship (SRC-1, `infer/src/contextpilot.py`, `infer/configs/fsm_plan_bm25_mc_prompt.txt`).

> self.notes[k] = self._build_memory(key, content, summary, entities, episodes, relations, source)
> --- `infer/src/contextpilot.py`

> related.sort(key=lambda item: item["score"], reverse=True)
> return related[:max(0, int(max_related or 0))]
> --- `infer/src/contextpilot.py`

The summary push is independent of an explicit memory-read request, whereas the primary-entry read is policy-requested. Neighbor supply is automatic expansion within that requested read. Neither key IDs nor source IDs are automatically dereferenced evidence pointers. These distinctions prevent describing all memory delivery as semantic search (SRC-1, `infer/src/contextpilot.py`; [MEM-OBJ-memory-indexes](#mem-obj-memory-indexes)).

#### MEM-RTE-training-stores
Label: Training store admission and read-back
Part of: [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)

Endpoints: model calls through registered training tools to AgentData stores, rendered prompt and descendant generations. Owner: StateLM tool wrappers, ContextPilotMemoryState and renderer. Proposer: policy model; admission: nonempty-key/available-state checks followed by keyed mutation. This is a different implementation from inference, not a new label for [MEM-RTE-inference-stores](#mem-rte-inference-stores). Operating mode is the parent's bounded training/validation curriculum. Reference answers influence terminal scoring and actor updates, not a factual approval of each memory entry. Humans supply curriculum/checkpoint/configuration without approving individual retained contents (SRC-1, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON ToolResponse reporting mutation success/error or selected entry and related-memory displays; wrappers return tool reward 0.0 for the inspected memory operations, not a truth score.
- Later read-back: Rendered histories append all current keys/summaries to the first user message; memory-write boundaries rebuild prompt tokens. Reads return selected entry text; deep-copied stores support descendant branch rendering. Snapshot rows can later receive terminal-based learning credit independently of the text's truth.
- Delegated visibility: Policy/branch endpoints receive their rendered contexts; optional embedding endpoint receives signature text. Reward/actor consumers later receive selected trajectory arrays through the parent training route, not an independently curated factual database.
- Selection predicate: Policy chooses exact key; read wrappers require a nonempty key and the state rejects missing entries. Related selection uses fixed features/optional vector scores, returning bounded summaries/episodes; the wrapper converts max_related 0 to default 5. Summary inventory includes every current key rather than question-ranked retrieval.
- Invalidation or expiry: Delete removes the current entry/cache; overwrite replaces it; append revises fields. Simple-note update always assigns the normalized new summary, so omission clears it to an empty string. Branches copy state rather than receiving later sibling revisions; trajectory/process lifetime bounds stores.
- Activation or effect: Memory/tool results and revised prompt tokens are wired to descendant generations; operational activation and semantic benefit remain uninspected.
- Evidence limits: Training is not the inference FSM and carries no inherited mandatory-review guarantee. Initial content supplied through arbitrary library callers is not established; the inspected shipped tools show known subsequent transformations and branch inheritance.

Guidance is the shipped training maintenance prompt. New keys overwrite on repeated admission. Rich-memory update rejects missing keys, invalid modes and overwrite without content. Simple-note update permits normalized empty content/summary and rejects invalid mode/missing key. It therefore cannot be summarized by inference's “new content required” rule. Content has no human veto or semantic review; deletion/overwrite are model-controlled recovery, not an automatically triggered correction based on reward (SRC-1, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py`, `train/configs/contextpilot_system_prompt.txt`).

> new_content = _safe_str(parameters.get("new_content"))
> new_summary = _safe_str(parameters.get("new_summary"))
> --- `train/verl/tools/statelm_tools.py`

> simple_notes[key]["summary"] = new_summary
> --- `train/verl/tools/statelm_tools.py`

#### MEM-RTE-training-context
Label: Training context edits and synthetic recovery
Part of: [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)

Endpoints: policy context-edit tools or token-pressure rule to masks/replacement text, rendered tokens, length snapshots and subsequent generation/training. Owner: StateLM tools and asynchronous loop. This is the training context subroute, distinct from inference [RT-RTE-context-edit](runtime.md#rt-rte-context-edit). Both use backing histories and edited views, but training adds synthetic-action credit and non-branchable length checkpoints. Operating mode is bounded training/validation. The policy proposes explicit edits; code independently selects proactive cleanup and admits its own synthetic action. No per-edit human veto or answer oracle controls this selection. Terminal scoring uses the parent's reference-answer oracle only downstream (SRC-1, `train/verl/tools/statelm_tools.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Explicit tool success/error and editor metadata; automatic cleanup returns whether a change was made, records synthetic assistant/tool history and rebuilds prompt IDs. Length boundaries retain training arrays and reset the training segment.
- Later read-back: Later policy calls receive stubs, selected spans, model summaries or compressor output in place of original messages. Snapshots, including qualifying forced-action snapshots, feed descendant reward assignment and actor updates through [RT-RTE-actor-update](runtime.md#rt-rte-actor-update). Emergency-conditioning-only cleanup supplies no trainable synthetic suffix.
- Delegated visibility: Compressor receives selected raw message text; branch policies receive cloned histories/masks and rendered contexts. Worker/actor consumers receive token/mask/metadata artifacts, not a reviewer-approved explanation of the edit.
- Selection predicate: Policy selects message ID, summary/span/rate for explicit edits. Token-pressure code considers undeleted read/search tool results, ranks up to eight large candidates plus a provisionally protected newest read, simulates rendered lengths, and selects the smallest reducing result, falling back to the protected read only when needed. Proactive configured limits and length boundaries trigger this code without a model decision.
- Invalidation or expiry: Original history is retained; masks determine rendering precedence: delete, summary, then truncation. Branches deep-copy those fields. The inspected training tool registry offers no restoreContext operation; original retention alone establishes no policy-visible reload tool. New context reconstruction, task termination and process lifetime bound these views.
- Activation or effect: Altered prompt delivery and potential trainable forced-action masks are wired; actual generation dependence, preserved meaning and learning benefit are unobserved.
- Evidence limits: Cleanup is best effort: no reducing candidate can stop reclamation above its target; failure to fit the model window can flag a length violation. Provider compression behavior is external, and random sampling fallback is not guaranteed semantic summarization.

Explicit admission checks IDs/roles and span presence, not semantic fidelity. User messages cannot be deleted by the handler. Summaries are model-supplied; compression calls an external generation endpoint, falling back on ordered randomly sampled words after an exception. Software stores the result without semantic acceptance testing. Static instructions shape requested cleanup, while masks and replacement strings persist into subsequent contexts. This is a trace-to-derived-view-to-policy chain even within a single trajectory (SRC-1, `train/verl/tools/statelm_tools.py`, `train/configs/contextpilot_system_prompt.txt`).

The automatic producer is materially different. After adding a synthetic assistant delete call, it attempts to isolate the action's token suffix. If successful, it assigns response mask 1 and zero old log-probabilities, then emits a forced-action, non-branchable snapshot. Otherwise it applies cleanup as emergency conditioning only. Raw trace provenance is therefore mixed: document-derived observations, policy calls, and code-authored actions. A synthetic action is not evidence that the sampled policy chose it (SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`).

> agent_data.response_ids = list(action_token_ids)
> agent_data.response_mask += [1] * len(action_token_ids)
> agent_data.response_logprobs += [0.0] * len(action_token_ids)
> await self._emit_length_boundary(
>     agent_data,
>     reason="auto_deleteContext",
>     tool_names=["deleteContext"],
>     auto_delete_context=True,
>     forced_action=True,
> )
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

> "deleteContext action; applying it as emergency conditioning only."
> --- `train/verl/experimental/agent_loop/statelm_agent_loop.py`

Downstream reward assignment averages descendant terminal outcomes, drops snapshots without terminal descendants and supplies normalized masked training signals. That establishes a trace-fed parameter-update path, not retention of a formulated reason why each cleanup was appropriate. The metadata retains boundary reasons and action provenance, but the supplied actor-update route does not establish that the optimizer consumes those explanatory strings. No exercised learning or self-improvement claim is made ([RT-RTE-actor-update](runtime.md#rt-rte-actor-update), [RT-BAP-reward-actor](runtime.md#rt-bap-reward-actor)).

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-full-history](runtime.md#rt-obj-full-history)

Memory distinction: raw messages remain backing state; payload snapshots are derived views. The inference JSON writer stores history, edit maps, summaries and snapshots, not a complete explicit dump of both keyed stores. Some store content may survive in tool arguments/results, but that is not a verified lossless database backup. The shipped driver writes final/inference result artifacts and resume uses completed sample IDs; neither establishes reloading trace content as later task knowledge. Artifact durability therefore exceeds the demonstrated semantic reuse horizon (SRC-1, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`).

> "session_notes_summary": self.state_manager.get_notes_summary(),
> "api_call_count": self.api_call_counter,
> "final_answer": self._extract_final_answer(),
> "correct_answer": correct_answer,
> "full_history": self._sanitize_for_json(self.full_history),
> --- `infer/src/contextpilot.py`

#### On [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks)

Replacement text is retained derived memory when later policy calls receive it; a deletion set itself is symbolic view control rather than a factual summary. The explicit inference restore handler clears delete/truncate/summary/compression masks only for marked restorable IDs, revealing backing history again. It does not restore an overwritten store entry. Its default schema availability remains a separate limit. The memory analogy is a filtered backing store: stubs and IDs are not automatically followed references, and masking is not destruction of the original frame (SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`).

> if msg_id_int in self.truncated_msg_ids:
>     self.truncated_msg_ids.pop(msg_id_int, None)
>     restored_from.append("truncateContext")
> --- `infer/src/contextpilot.py`

#### On [RT-BAP-context-policy](runtime.md#rt-bap-context-policy)

Summary inventories are unsolicited supply during payload rebuilding; explicit read tools request stored bodies. Neighbor expansion supplies only selected displays. Their authority is natural-language evidence/guidance to the policy, not execution rights or proven belief. Store keys and source fields do not grant special instruction priority. The same content can affect future calls through multiple copies: current inventory, surviving raw write/read messages and derived replacement text (SRC-1, `infer/src/contextpilot.py`).

> text += (external_context_summary if idx == 0 else "")
> messages.append({"role": "user", "content": text})
> --- `infer/src/contextpilot.py`

#### On [RT-RTE-actor-update](runtime.md#rt-rte-actor-update)

Memory lineage includes code-authored recovery snapshots as well as sampled actions. Forced-action metadata and response masks originate in [MEM-RTE-training-context](#mem-rte-training-context). The immediate update consumer receives scored/masked trajectories; its retained result is actor parameter state, not an adopted textual memory entry. Checkpoint save/load supplies a longer numerical recovery horizon than the per-sample dictionaries. Validation metrics do not themselves retract or rewrite a wrong memory; absent descendant rewards reject a training row rather than deleting its textual source (SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`; the supplied record supplies the reward/estimator/checkpoint passages).

## Write side

Acquisition starts with the supplied document, question and chunk/search observations. Indexing/search expose selected source text; the policy authors summaries, saved facts and explicit context replacements. Source strings and optional evidence IDs retain only what the proposer supplies. A static instruction asks preservation of subject/object/speaker/time and independent counting/chronology checks. It supplies a reason to preserve qualifiers, not evidence that any particular derived summary did so (SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `train/configs/contextpilot_system_prompt.txt`; [MEM-RTE-inference-stores](#mem-rte-inference-stores), [MEM-RTE-training-stores](#mem-rte-training-stores)).

Admission is separately visible at each write: keyed dictionary assignment admits model text; update mode/content checks reject malformed revisions; graph reconstruction admits automatic access metadata; role/span checks admit explicit view edits; provider failure admits sampling fallback; token-pressure code admits synthetic deletion and sometimes a trainable action. None of these is a per-content human approval. A caller directly initializing a library dictionary has unresolved human/computational authorship, which does not erase the known subsequent model and code transformations ([MEM-OBJ-memory-indexes](#mem-obj-memory-indexes), [RT-RTE-context-edit](runtime.md#rt-rte-context-edit), [MEM-RTE-training-context](#mem-rte-training-context)).

Withdrawal has different effects. Store deletion removes an entry from future current-state inventories and graph reads; it does not invalidate prior copied tool results. Context deletion masks only the selected message; it does not remove separately saved facts. Document cleanup deletes indexed document material and clears local retrieval state, not necessarily memories derived from that material. Inference cleanup can delete a whole configured index or matching document ID; training clears only owned/orphan document IDs, respecting branch nonownership. Interrupted/failed external deletion is not successful erasure (SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`; [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)).

Training's automatic trace-fed chain is raw/edited history plus policy and synthetic actions → token/mask snapshots → descendant terminal score → query-relative training signal → actor update → checkpoint/reload. Alternative length boundaries and conditioning-only recovery are retained in [MEM-OBJ-trajectory-snapshots](#mem-obj-trajectory-snapshots) and [MEM-RTE-training-context](#mem-rte-training-context). Raw logging alone is not this learning path. The actor route provides the independent answer objective, row rejection and numerical persistence; it provides no observed improvement. Natural-language reasons for saved facts are optional content, and no inspected path requires a durable criticism/rationale for each parameter change ([RT-RTE-actor-update](runtime.md#rt-rte-actor-update)).

## Read-back

The inference payload builder and training renderer automatically select **all current summaries**, with keys, for the first user message. The selection input is current store membership, not the question. This push survives cleanup of the original evidence message but can itself consume substantial context: there is no per-inventory top-k or token-budget step in the inspected builders. Overall token-window handling remains best effort and can fail to fit. For full contents, the policy chooses a key and receives a copied entry. The FSM may substitute a latest/sole key or perform a mandatory recovery read; this is delivery, not demonstrated relevant review ([MEM-RTE-inference-stores](#mem-rte-inference-stores), [MEM-RTE-training-stores](#mem-rte-training-stores), [RT-CLM-fsm-controls](runtime.md#rt-clm-fsm-controls)).

`loadMemory` selects neighbors using retained pairwise metadata from the chosen entry. It returns bounded key/summary/episode displays plus relation breakdown/score. A neighbor key affords a later explicit full read; it does not cause the neighbor's complete payload to enter this invocation. Optional vectors can alter the selection, but their exact producing model and semantic relevance remain unestablished. Simple notes have no equivalent graph expansion ([MEM-OBJ-memory-indexes](#mem-obj-memory-indexes)).

Working-context control is not limited to these stores. Explicit model edits remove chosen assistant/tool material or replace it with spans/summaries/compression. Inference token-window and API recovery select older/reclaimable material without a fresh model choice; the newest evidence is not universally protected. Training's proactive selector provisionally protects the latest read but can delete it when no alternative reduces context. Original question/system guidance and backing history remain distinct from edited message views. Branches isolate local mutable copies, returning scored trajectories rather than free-form findings to a foreground policy; shared document backend IDs qualify isolation. This fits a separate-context copying mechanism, not a heap with automatically dereferenced IDs ([RT-RTE-context-edit](runtime.md#rt-rte-context-edit), [MEM-RTE-training-context](#mem-rte-training-context), [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout)).

Numerical checkpoint loading is a separate later consumer from model prompt read-back. It restores training state for later optimization, while output resume skips completed sample IDs. Neither establishes that saved inference traces become a new task's autobiographical store or that a trained checkpoint was deployed to the inference service ([RT-RTE-actor-update](runtime.md#rt-rte-actor-update), [RT-RTE-document-qa](runtime.md#rt-rte-document-qa)).

## Integration issues

1. **Training trace-origin addition.** [MEM-RTE-training-context](#mem-rte-training-context) and [MEM-OBJ-trajectory-snapshots](#mem-obj-trajectory-snapshots) add a forcing case not detailed in [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout) or [RT-RTE-actor-update](runtime.md#rt-rte-actor-update): code-authored synthetic cleanup may be a masked trainable snapshot, or conditioning only. Evidence is the forced-action suffix and length-boundary code in SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`. This qualifies any inference that all credited actions originated in sampled policy output; it does not contradict the supplied reward-assignment account.
2. **Configuration-dependent restore and uncalled merge.** The base handlers implement restore and merge, but the inspected default inference schema names neither. Merge also discards rich fields and does not immediately reindex its new entry. Evidence is SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`. [RT-OBJ-context-masks](runtime.md#rt-obj-context-masks) and [RT-RTE-context-edit](runtime.md#rt-rte-context-edit) should retain “where authorized/configured” rather than imply default callable restoration; [MEM-OBJ-notes](#mem-obj-notes) establishes only a merge capability, not an ordinary consumer route.
3. **Store-container versus trace identity.** [MEM-OBJ-trajectory-snapshots](#mem-obj-trajectory-snapshots) resembles the word “snapshots” in [RT-OBJ-full-history](runtime.md#rt-obj-full-history), but its training token/mask/node state has a distinct producer and consumer. The four store-object declarations likewise are not redeclarations of raw history or masks. No proposed duplicate referent remains after this comparison. The inference store route is explicitly a subroute of the supplied FSM QA route and also applies to base-handler reuse, not a supersession.
4. **Known admission difference, not a generic update rule.** [MEM-RTE-training-stores](#mem-rte-training-stores) retains training simple-note summary clearing/empty-content acceptance; [MEM-RTE-inference-stores](#mem-rte-inference-stores) retains inference's content requirement and optional summary preservation. SRC-1, `train/verl/tools/statelm_tools.py`, `infer/src/contextpilot.py`. Any reconciled store description must preserve these route-specific checks rather than universalize the runtime's within-trajectory write summary.
5. **Unresolved downstream horizons.** Exact provider state, successful semantic review/compression, actual checkpoint-driven future behavior, lower-level optimizer/export/deployment wiring, and cross-task semantic trace reuse are not established. Relevant evidence/limits are [RT-CMP-actor-model](runtime.md#rt-cmp-actor-model), [RT-CMP-compression-model](runtime.md#rt-cmp-compression-model), [RT-RTE-actor-update](runtime.md#rt-rte-actor-update), and the annotation on [RT-OBJ-full-history](runtime.md#rt-obj-full-history). Available export/lower-level source was not inspected, while external service weights and executions are outside the acquired evidence. These limits prevent claims of deployed or beneficial long-horizon memory, not the positive within-trajectory wiring findings.

## Limitations and checks

Git HEAD was rechecked as `782cbb6611fb610c4cf6fafda6022b7e89cae191`; source checkout status was clean. Source identity and report boundary match the supplied boundary/run. The complete invocation, member/input types, boundary, runtime, collection, worker rules and record contract were read, including the supplied bounded ranges. Scope and method followed source-only inspection; no outside sources or prior analyses were used.

Load-bearing additions retain verbatim source passages or cite supplied records containing them. Negative statements are scoped to inspected builders, schemas and callers; no system-wide evidenced-absence record is declared. No execution, activation, benchmark reproduction or causal experiment was available. Validation checks structure and quotation occurrence, not whether the analysis is correct.

Deterministic validation: the invocation's validate-output command passed after report construction.
