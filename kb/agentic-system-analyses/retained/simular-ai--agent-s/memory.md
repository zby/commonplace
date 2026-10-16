---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Agent S memory: historical experience and query caches, current worker context and coding returns, and offline rollout evidence."
run-id: AAS-2026-10-16-agent-s-db6fee212353-01
source-identity: https://github.com/simular-ai/Agent-S
reviewed-boundary: "15776a8dc659658b1963816ea006f7af1978e595"
---

# Agent S memory report

## Boundary and evidence

This report covers the shipped S1, S2, S2.5 and S3 memory/context paths at the revision in [boundary](boundary.md). Persistent historical experience, exact-task query/search caches, embedding access metadata, ACI notes, current-run reflection and context eviction, coding-frame returns, and offline trajectory-to-caption-to-selection paths are included. The installed command selects S3, not the historical experience architecture. SRC-1: `setup.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s1/core/AgentS.py`.

Evidence is implementation and shipped prompt/design text, not execution. Direct reads extended the supplied runtime account through historical KnowledgeBase implementations, manager/worker consumers, alternative S2 save APIs, S1 history editing, S3 coding-summary construction and offline file consumers. No target code or tests were run. External KB release contents, actual result directories, model weights/provider storage and desktop environments remain unavailable; their provenance, correctness, exercised authority and benefits cannot be established. These limits do not erase the inspectable later-consumer wiring. Hosted products and external OpenClaw orchestration remain excluded as in boundary.

### Coverage inventory

Rows distinguish direct source inspection from dependence on supplied runtime records. Paths are SRC-1 commit-relative anchors; records give the detailed evidence and limits.

| Entry point / operation | Source paths and inspection | Coverage / unresolved fact and prevented conclusion |
|---|---|---|
| Installed CLI / SDK / OpenClaw dispatch | `setup.py`; `gui_agents/s3/cli_app.py`; `integrations/openclaw/agent_s_wrapper.py` — supplied runtime; S3 agent reset directly read | [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop), [RT-RTE-openclaw-bridge](runtime.md#rt-rte-openclaw-bridge); no wrapper knowledge-store reload established |
| Historical CLI trace admission | `gui_agents/s2/cli_app.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s1/core/AgentS.py` — direct reads; S1 CLI call sites searched | [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience), [MEM-RTE-s1-experience](#mem-rte-s1-experience); terminal/wait branches do not equal complete trace capture |
| Bootstrap and initial content | `gui_agents/utils.py`, S1/S2 agent constructors — direct | [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap), annotation below; external archive lineage/content opaque, later transformations known |
| Task and subtask stores / retrieval | `gui_agents/s1/core/Knowledge.py`, `gui_agents/s2/core/knowledge.py`, S1/S2 manager/worker paths — direct | [MEM-OBJ-narrative-memory](#mem-obj-narrative-memory), [MEM-OBJ-episodic-memory](#mem-obj-episodic-memory), [MEM-RTE-experience-retrieval](#mem-rte-experience-retrieval) |
| Query formulation / search / fusion | Same KnowledgeBase files; `gui_agents/s2/agents/manager.py` — direct | [MEM-OBJ-formulate-query](#mem-obj-formulate-query), [MEM-OBJ-rag-knowledge](#mem-obj-rag-knowledge), [MEM-RTE-query-cache](#mem-rte-query-cache); Perplexica response provenance remains external |
| Alternate save/finalize API | `gui_agents/s2/core/knowledge.py`; caller search across `gui_agents/`, `osworld_setup/`, `integrations/` | [MEM-RTE-knowledge-save](#mem-rte-knowledge-save); no shipped caller of the alternative lifecycle methods found, so automatic deployment of this path is not established |
| Embedding generation and serialization | S1/S2 KnowledgeBase files and `gui_agents/s2/utils/common_utils.py` — direct; provider clients supplied | [MEM-OBJ-embeddings](#mem-obj-embeddings), [RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine); existing vector/model provenance not encoded by string-key cache |
| Advertised save-to-knowledge action / notes | `gui_agents/s3/agents/grounding.py`, S3 worker directly; historical ACI/worker searches and S1/S2/S2.5 worker reads | [MEM-OBJ-notes](#mem-obj-notes), [MEM-RTE-notes-delivery](#mem-rte-notes-delivery); a RAM list is not evidence of a cross-process bank |
| Procedural instructions, reflection, eviction, worker resets | `gui_agents/s1/core/Worker.py`, `gui_agents/s2/agents/worker.py`, `gui_agents/s2_5/agents/worker.py`, `gui_agents/s3/agents/worker.py`, S3 agent — direct | [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory), [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop), annotations and working-context account below |
| Formatting and grounding contexts | Supplied `gui_agents/s3/utils/formatters.py`, `gui_agents/s3/utils/common_utils.py`; grounding reset call sites searched | [RT-RTE-action-check](runtime.md#rt-rte-action-check); retries can mutate notes; grounding's per-request reset is not experience consolidation |
| Coding frame / return / summary | `gui_agents/s3/agents/code_agent.py`, S3 worker — direct; ACI/controller route supplied | [MEM-OBJ-code-result](#mem-obj-code-result), [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation); raw result feedback does not reach the summary constructor |
| OSWorld logs and evaluation | `osworld_setup/s3/lib_run_single.py` — direct; historical helpers searched for memory updater calls | [MEM-OBJ-traj](#mem-obj-traj), [RT-RTE-osworld-driver](runtime.md#rt-rte-osworld-driver); external evaluator semantics unavailable, benchmark logging alone does not imply historical KB admission |
| Caption admission / later judge / resume and scoring | `osworld_setup/s3/bbon/generate_facts.py`, `osworld_setup/s3/bbon/utils.py`, `osworld_setup/s3/bbon/run_judge.py`, `gui_agents/s3/bbon/behavior_narrator.py`, `gui_agents/s3/bbon/comparative_judge.py` — direct relevant ranges | [MEM-OBJ-fact-captions](#mem-obj-fact-captions), [MEM-OBJ-judge-results](#mem-obj-judge-results), [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection); actual captions, judgments and benefits unobserved |
| Provider-side retained state | Provider boundaries supplied in runtime | [RT-CMP-lmm-agent](runtime.md#rt-cmp-lmm-agent), [RT-CMP-grounding-model](runtime.md#rt-cmp-grounding-model); no frozen service state, so server retention, hidden compaction and training cannot be classified |

## Core ideas

1. **Historical experience has content and access state with different roles.** Natural-language task/subtask summaries survive in JSON. Dense vectors of their keys survive separately in pickle and rank candidates; vectors are not the advice supplied to the planner. Query formulation and search responses are additional persistent stores, not merely a front end to episodic recall. [MEM-RTE-experience-retrieval](#mem-rte-experience-retrieval), [MEM-RTE-query-cache](#mem-rte-query-cache).
2. **Admission is mostly automatic and preservation is mostly key-based.** Historical CLI summaries are admitted without per-summary human approval or an independent truth gate. Existing keys suppress revision; retrieval even skips an identical top key. That combination is not an evidence-responsive repair policy. Prompts request correct-step extraction and failure explanations, but successful curation is not observed. [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience), [MEM-OBJ-narrative-memory](#mem-obj-narrative-memory), [MEM-OBJ-episodic-memory](#mem-obj-episodic-memory).
3. **Current S3 separates retained returns from context housekeeping.** A coding summary and action history cross into a later worker invocation; older screenshots are simply removed from model messages. ACI notes are repeatedly inserted in full. Neither image removal nor the name “long-term knowledge bank” establishes persistent experience consolidation. [MEM-OBJ-code-result](#mem-obj-code-result), [MEM-RTE-notes-delivery](#mem-rte-notes-delivery), [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop).
4. **Offline captions change a later judgment, not the live worker policy.** Raw rollout evidence is transformed into model-produced captions. The judge receives caption answers and endpoint images, not retained narrator thoughts or all intermediate evidence. A persisted choice later affects resume/scoring. This is a separate consumer chain, not an inferred online learning loop. [MEM-OBJ-fact-captions](#mem-obj-fact-captions), [MEM-OBJ-judge-results](#mem-obj-judge-results).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-narrative-memory
Label: Historical narrative_memory task summaries

Source-native identity: platform-specific `narrative_memory.json` in S1/S2 local KB roots. JSON key lookup is symbolic; values are natural-language plans or failure explanations, interpreted by the manager/fusion model. Filesystem JSON persists beyond worker/task resets. Initial entries may come from external bundles or caller-supplied local files, with unknown per-entry origin; subsequent CLI writes derive from task instruction plus accumulated plan/reflection text. This is content, not an embedding index. It complements the route [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience), not a duplicate route/object; S1 is also included here. SRC-1: `gui_agents/s1/core/AgentS.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/core/knowledge.py`.

Admission preserves an existing search-query key. New summaries are model-authored under a prompt that requests successful plans or reasons/suggestions for failure. Those reasons may survive in the value and are passed to later consumers with the value; no structured criticism lineage or guarantee that reasons are present survives independently. The text's authority is optional guidance in a later planning system prompt, not an executable rule or verified fact. Consumers and exact-key skipping are in [MEM-RTE-experience-retrieval](#mem-rte-experience-retrieval).

> 1. If the task is successfully executed, you should summarize the successful plan based on the whole trajectory to finish the task.
> 2. Otherwise, provide the reasons why the task is failed and potential suggestions that may avoid this failure.
> --- `gui_agents/s2/memory/procedural_memory.py`

#### MEM-OBJ-episodic-memory
Label: Historical episodic_memory subtask summaries

Source-native identity: platform-specific `episodic_memory.json` in S1/S2. Symbolic task/subtask/instruction string keys select natural-language action recipes, including rendered grounded-action strings. Stored recipes are delivered as model guidance, not directly replayed by the loader. Local filesystem persistence is distinct from transient raw subtask trajectory strings. This is a content part adjacent to [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience), not another declaration of that route; S1 shares the design. SRC-1: `gui_agents/s1/core/AgentS.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/agents/worker.py`.

New-key admission invokes the summarizer; existing content wins. The updater appends “Subtask Completed” at a Start/Done boundary, not after an independent success oracle. Terminal CLI branching can bypass that boundary's updater. The prompt asks to remove repeated/incorrect steps and substitute element descriptions; the saved value need not retain the rejected steps or their reasons. S2 read-side regex substitutions additionally replace numeric action arguments and `_id` substrings, so stored and delivered recipes can differ. No separate rationale reader is established. Initial bundle provenance is unresolved locally, without obscuring these known transformations.

> You will summarize the correct plan and grounded actions based on the whole trajectory of a subtask, ensuring the summarized plan contains only correct and necessary steps.
> --- `gui_agents/s2/memory/procedural_memory.py`

> retrieved_subtask_experience = retrieved_subtask_experience.replace(
>                     "_id", "_description"
>                 )
> --- `gui_agents/s2/agents/worker.py`

#### MEM-OBJ-formulate-query
Label: Historical formulate_query cache

Source-native identity: S1/S2 platform `formulate_query.json`, symbolic exact instruction keys and natural-language search-query values. It is a local JSON file. A model derives a query from task and current observation on cache miss; a later task with the same instruction returns the saved query without checking the new observation. S1 formulation includes accessibility-tree text and optionally image; S2 uses a screenshot. This object has no supplied object counterpart; it is an additional path alongside [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience). SRC-1: `gui_agents/s1/core/Knowledge.py`, `gui_agents/s2/core/knowledge.py`.

> if instruction in formulate_query:
>             return formulate_query[instruction]
> --- `gui_agents/s2/core/knowledge.py`

The later manager retains the query as task search identity and passes it to workers; search/fusion use is described in [MEM-RTE-query-cache](#mem-rte-query-cache). Content has planning/search authority through those consumers, not a global instruction-install operation.

#### MEM-OBJ-rag-knowledge
Label: Historical search-engine rag_knowledge cache

Source-native identity: S1/S2 `{search_engine}_rag_knowledge.json`. Local JSON has symbolic exact instruction keys and natural-language search-result values. On miss the producer is either an LLM's response or external Perplexica output; the latter's source selection and correctness are not frozen. This is distinct from task-trace summaries and has no supplied object counterpart. SRC-1: `gui_agents/s1/core/Knowledge.py`, `gui_agents/s2/core/knowledge.py`.

> if instruction in exist_search_results:
>             return exist_search_results[instruction]
> --- `gui_agents/s2/core/knowledge.py`

S2 returns `(search_query, search_results)` from `retrieve_knowledge`; manager passes that return as `web_knowledge` into a string-formatted fusion message. The actual fusion input can therefore contain a rendered tuple rather than only search-result prose. Model fusion produces an ephemeral numbered list that is installed as optional planning guidance. Neither a cached result nor the label “web search result” authenticates the content. [MEM-RTE-query-cache](#mem-rte-query-cache) traces this consumer path.

#### MEM-OBJ-embeddings
Label: Historical embeddings access cache

Source-native identity: S1/S2 `embeddings.pkl`, a pickle dictionary mapping symbolic text keys to dense numerical vectors. The dense part is distributed-parametric representation, not natural-language knowledge; storage is the local filesystem, not model weights. Known miss-path lineage is the task/subtask query or memory-entry key passed to an external embedding engine. Existing pickle contents can originate in a downloaded bundle or prior local use; no per-vector model/version lineage is checked by these retrieval functions. Model mutability belongs to [RT-CMP-embedding-engine](runtime.md#rt-cmp-embedding-engine); this cache is a distinct operative object, not that component. SRC-1: `gui_agents/s1/core/Knowledge.py`, `gui_agents/s2/core/knowledge.py`, `gui_agents/s2/utils/common_utils.py`.

> with open(embeddings_path, "rb") as f:
>             return pickle.load(f)
> --- `gui_agents/s2/utils/common_utils.py`

The symbolic consumer uses cosine similarity and sorts key vectors. Cache writes are automatic miss filling, not parameter training or demonstrated trace learning. Retrieval controls which summary gets model-visible authority, but vectors themselves are not appended as advice. Deleting or changing summary keys changes candidates; stale unused vectors can remain. No encoder-version invalidation is present in the inspected lookup. Loading pickle is deserialization, not a semantic content/trust gate.

#### MEM-OBJ-notes
Label: ACI notes text buffer

Source-native identity: `notes`, a Python list owned by ACI instances, across historical ACI implementations and S2/S2.5/S3 grounding agents. Strings are natural-language content; list membership/order is symbolic state in process RAM. Model-selected `save_to_knowledge` calls append supplied strings. This is distinct from [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory), a static shipped instruction object, and from the persistent historical JSON stores. SRC-1: `gui_agents/s3/agents/grounding.py`, `gui_agents/s2/agents/grounding.py`, `gui_agents/s2_5/agents/grounding.py`, `gui_agents/s1/aci/LinuxOSACI.py`.

> def save_to_knowledge(self, text: List[str]):
>         """Save facts, elements, texts, etc. to a long-term knowledge bank for reuse during this task. Can be used for copy-pasting text, saving elements, etc.
>         Args:
>             text:List[str] the text to save to the knowledge
>         """
>         self.notes.extend(text)
>         return """WAIT"""
> --- `gui_agents/s3/agents/grounding.py`

The description's “long-term” is bounded by the instance, not evidence of disk persistence. Worker resets do not necessarily replace ACI; in S3 `AgentS3.reset` passes the same grounding object to a new Worker. Notes can therefore survive a task reset in a reused process. Full content enters user-message text, giving advisory authority and exposure to later model decisions. [MEM-RTE-notes-delivery](#mem-rte-notes-delivery).

#### MEM-OBJ-code-result
Label: S3 code-agent retained result

Part of: [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation)

This object is the route's material return, not a replacement route. Source-native identity: `last_code_agent_result`, including summary and `execution_history`, in ACI RAM. Symbolic dictionary fields hold natural-language summary/thoughts and code/action text. Code has a symbolic execution role inside the coding frame, but its later outer-worker display is model-interpreted evidence, not automatic replay. Source lineage is CodeAgent model actions/thoughts; controller output feeds subsequent coding rounds but is omitted from `execution_history`. The summary uses that reduced history. SRC-1: `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/grounding.py`.

> execution_history.append(
>                 {"step": step_count + 1, "action": action, "thoughts": thoughts}
>             )
> --- `gui_agents/s3/agents/code_agent.py`

> summary = self._generate_summary(execution_history, task_instruction)
> --- `gui_agents/s3/agents/code_agent.py`

Task identity, completion reason, budget, summary and formatted actions reach the next worker user message. The worker does not render the retained per-step `thoughts` field there. The summary may incorporate those thoughts, but the full raw controller-result dialogue does not cross back. The summary prompt requests fewer than 150 words; this is a request, not a token-enforced bound. No factual acceptance gate precedes delivery. Summary failure becomes an explanatory string. The cached object clears after delivery; message text can remain until reset/eviction. This is within-task retained read-back, unlike plain turn accumulation.

#### MEM-OBJ-traj
Label: OSWorld raw trajectory evidence

Part of: [RT-RTE-osworld-driver](runtime.md#rt-rte-osworld-driver)

The object is the driver's persistent evidence output. Source-native identity: task directory `traj.jsonl`, `step_*.png`, `instruction.txt`, `result.txt` and runtime log. These require separate interpretation: JSON fields/timestamps/action strings and numeric score are symbolic; model plans/reflections are natural-language trace content; screenshots are encoded raster observations interpreted visually, not dense learned weights. Filesystem records mix agent-produced intentions with externally returned observations/reward/evaluation. They are not already curated lessons. SRC-1: `osworld_setup/s3/lib_run_single.py`.

> with open(
>                 os.path.join(example_result_dir, "traj.jsonl"), "a", encoding="utf-8"
>             ) as f:
>                 f.write(json.dumps(response, ensure_ascii=False))
>                 f.write("\n")
> --- `osworld_setup/s3/lib_run_single.py`

Later captioning reads screenshots plus `exec_code`; variance filtering/scoring reads scores. `instruction.txt` is recorded, but run_judge instead loads the task instruction from external example configuration. No automatic GUI-worker reload of these files is established by this driver. S1/S2 OSWorld helpers were searched for historical updater calls; the CLI experience-writing behavior must not be projected onto benchmark recording.

#### MEM-OBJ-fact-captions
Label: S3 fact_captions derived descriptions

Part of: [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection)

This is the selection route's retained intermediate object. Source-native identity: `fact_captions.jsonl`, local JSONL storing natural-language `fact_answer`, `fact_thoughts` and symbolic screenshot number. Narrator derivation uses adjacent sorted screenshots and matching trajectory-line `exec_code`, with marked/zoomed image transformations. Terminal actions have special fixed descriptions; nonterminal captions are model interpretations, not independently certified facts. Exceptions are omitted and only successful results written. Existing filename presence causes main to skip the directory, including a potentially incomplete prior file. SRC-1: `osworld_setup/s3/bbon/generate_facts.py`, `gui_agents/s3/bbon/behavior_narrator.py`.

> result = {
>             "fact_thoughts": fact_thoughts,
>             "fact_answer": f"Fact Caption from Screenshot {screenshot_num}: {fact_answer}",
>         }
> --- `gui_agents/s3/bbon/behavior_narrator.py`

> if "fact_answer" in data:
>                     fact_captions.append(data["fact_answer"])
> --- `osworld_setup/s3/bbon/utils.py`

The latter is the actual later selection: caption answers alone reach ComparativeJudge. Stored narrator reasons are not read by this route. Judge input additionally includes initial/final image pairs when both can be loaded; it is neither caption-only nor full-trajectory review. Content has evidential influence on model comparison. No explicit caption token budget, truth veto, content expiry or automatic invalidation after trajectory changes is shown in the inspected generator/loader. Human workflow launch is not approval of each caption.

#### MEM-OBJ-judge-results
Label: Persisted comparative judgment and resume state

Part of: [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection)

Source-native identity: output JSON files such as `BoN{i}.json` created by run_judge. Natural-language model answer/thoughts coexist with symbolic task keys and selected directory strings; later resume and scoring consume the latter mechanically. Filesystem persistence permits another invocation to skip recorded tasks and evaluate chosen rollout scores. This is not an installed next-action policy. Model judgment is admitted after parsing/range handling; invalid answers can persist with no selected trajectory. SRC-1: `osworld_setup/s3/bbon/run_judge.py`, `gui_agents/s3/bbon/comparative_judge.py`, `osworld_setup/s3/bbon/utils.py`.

> record = {
>         "selected_trajectory": selected_trajectory,
>         "answer": answer,
>         "thoughts": thoughts,
>     }
> --- `osworld_setup/s3/bbon/run_judge.py`

> if str(task) in data:
>             print(f"⚠️ Task {task} already exists in results — skipping.")
>             continue
> --- `osworld_setup/s3/bbon/run_judge.py`

Thoughts survive but scoring only needs the selected directory and task. Later reruns preserve choices by task-key presence rather than reassessing their reasons, model version or changed candidates. Output corruption can reset the loaded dictionary; no versioned rollback is shown. External evaluator scores filter the comparison workload and score choices retrospectively, not enter the comparative model as expected answers.

### Routes

#### MEM-RTE-s1-experience
Label: S1 CLI experience admission

Distinct identity: S1 generation's CLI/updater route, compared with the S2 referent [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience). The two share JSON filenames and updater structure but use separate generation modules and configurable roots. Owner/progression: S1 CLI executes ordinary actions, accumulates plan/reflection text, calls episodic updater, and invokes narrative updater on done/fail. Manager summarizers propose text; software key tests admit it. No per-summary human veto or independent answer oracle appears. Mode is ordinary task execution with retrospective summarization, not a bounded improvement experiment. SRC-1: `gui_agents/s1/cli_app.py`, `gui_agents/s1/core/AgentS.py`, `gui_agents/s1/core/Manager.py`.

- Immediate return: episodic updater returns an updated raw trajectory string; narrative updater writes JSON or logs failure.
- Later read-back: later S1 manager/worker initialization retrieves stored summaries through the KnowledgeBase similarity functions.
- Delegated visibility: summarizers receive accumulated textual trajectories; later agents receive selected summaries, not an assured full raw trace.
- Selection predicate: new task-search or subtask key admits a new model summary; old keys are retained. Start/Done episodic boundaries finalize a preceding nonempty trajectory.
- Invalidation or expiry: no per-entry expiry or correction branch in these updater methods; disk deletion/replacement can remove content, reset alone does not.
- Activation or effect: stores become eligible for later prompt advice; actual reliance and improved task ability are unobserved.
- Evidence limits: release entries and real CLI runs unavailable; a completion label in accumulated text is not an outcome oracle, and final pending subtask admission is not guaranteed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if self.search_query not in reflections:
>                 reflection = self.planner.summarize_narrative(trajectory)
>                 reflections[self.search_query] = reflection
> --- `gui_agents/s1/core/AgentS.py`

Guidance requests trajectory summarization, not machinery replacement. No automatic content rollback is implemented in these updater branches. Existing-key preservation can reject a proposed overwrite before a summarizer is called; it does not reject a bad first summary on its meaning.

#### MEM-RTE-experience-retrieval
Label: Historical key-similarity experience delivery

Distinct identity: read/selection operation across S1/S2, not a replacement for the enclosing S2 execution/admission route [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience). It crosses generations, so it is not wholly a part of that one S2 route. Trigger/owner: first manager planning step or first subtask worker turn requests experience; code builds query embeddings and ranks stored key embeddings, then injects one selected value. SRC-1: `gui_agents/s1/core/Knowledge.py`, `gui_agents/s1/core/Manager.py`, `gui_agents/s1/core/Worker.py`, `gui_agents/s2/core/knowledge.py`, `gui_agents/s2/agents/manager.py`, `gui_agents/s2/agents/worker.py`.

- Immediate return: selected `(key, value)` pair; empty store returns literal strings `"None", "None"`.
- Later read-back: manager uses narrative value or model-fused knowledge in its first system prompt; enabled worker uses episodic key/value in its first system prompt, after S2 read-side substitutions.
- Delegated visibility: fusion sees retrieved experience, search return and screenshot/current state; worker sees task/subtask/future/completed labels and one recipe, not all candidates or embedding scores.
- Selection predicate: cosine similarity over embedded keys; task instruction for narrative, composite task-search/subtask/instruction string for episodic; skip the top candidate if its key exactly equals the query. Budget is one entry, with no inspected token cap or similarity threshold.
- Invalidation or expiry: JSON is loaded on retrieval; access vectors are reused by text key. Worker reset discards prior prompt frame but can retrieve again; no content-age or encoder-version invalidation here.
- Activation or effect: selected prose reaches action/planning guidance with optional-use language; numeric ranking determines delivery, not truth or demonstrated compliance.
- Evidence limits: empty-store sentinel can itself be inserted as advice; a singleton identical key makes the second-ranked access out of range. Successful retrieval and useful advice are not universal guarantees.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> keys = list(knowledge_base.keys())
>         idx = 1 if keys[sorted_indices[0]] == instruction else 0
>         return keys[sorted_indices[idx]], knowledge_base[keys[sorted_indices[idx]]]
> --- `gui_agents/s2/core/knowledge.py:194-196`

This source witness qualifies the broad “retrieve most similar” label. Software selects a candidate; optional fusion model can omit content it judges unhelpful, not certify it. No human content choice or external reference answer is supplied to this read/comparison. Operating mode is task assistance. Request-driven retrieval is not independent unsolicited supply: code automatically requests it at the first planning/subtask invocation, then delivers the selected text.

#### MEM-RTE-query-cache
Label: Historical query and search cache reuse

No supplied route directly describes this cache-miss/admission/read chain; it complements [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience). Owner/progression: initial manager planning calls formulation, cache lookup or model generation, optional search-engine cache lookup or LLM/Perplexica call, optional fusion with experience, and planning prompt installation. SRC-1: `gui_agents/s1/core/Knowledge.py`, `gui_agents/s1/core/Manager.py`, `gui_agents/s2/core/knowledge.py`, `gui_agents/s2/agents/manager.py`.

- Immediate return: cached/generated query; if search enabled, query/result pair and model-fused guidance.
- Later read-back: a later invocation with the same instruction reuses the saved query and selected engine's saved result; manager prompt consumes fusion output or retrieved experience fallback.
- Delegated visibility: S1 formulation/fusion receives accessibility tree and optional image, S2 screenshot; cache hits bypass recomputation from changed observation. Fusion receives search return and selected experience, not an authenticated corpus.
- Selection predicate: exact instruction lookup, plus chosen search-engine filename; not semantic ranking of search-result values. No explicit retained-text budget in these methods.
- Invalidation or expiry: malformed/missing JSON is treated as empty; cache misses rewrite the dictionary; no freshness, observation-change or model-version expiry in the inspected methods.
- Activation or effect: saved query steers subsequent search and task identity; saved result can become planning advice through model fusion. Actual action change is unobserved.
- Evidence limits: Perplexica internals and actual cached text unavailable; LLM search is a model answer, not proof of external web retrieval. File-write success is environment-dependent.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> exist_search_results[instruction] = search_results.strip()
> --- `gui_agents/s2/core/knowledge.py`

Model or external search proposes content; software automatically admits it on a miss. Human task entry is not per-result approval. Unsupported engines raise; I/O/provider failures can prevent completion. No semantic rejection, rollback or validation oracle appears in this cache path. RAG prompt guides UI-automation information; fusion requests a useful numbered list. Persisted results are raw search/model response text, not a guaranteed curation of trace experience. S2 resets query/search/fusion contexts before miss processing; S1's corresponding methods do not reset those agents there, so long-lived instances may carry earlier context.

#### MEM-RTE-notes-delivery
Label: ACI notes admission and delivery

No supplied record declares this specific retained list/consumer chain; it intersects [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop) and [RT-RTE-action-check](runtime.md#rt-rte-action-check) without duplicating either. Owner/progression: model emits save-to-knowledge call, ACI extends notes, later worker generation inserts the full joined list as current text buffer. SRC-1: `gui_agents/s3/agents/grounding.py`, `gui_agents/s3/agents/worker.py`; analogous consumption in `gui_agents/s2/agents/worker.py`, `gui_agents/s2_5/agents/worker.py`, `gui_agents/s1/core/Worker.py`.

- Immediate return: WAIT marker from S3 append method; the list is already mutated during method evaluation.
- Later read-back: subsequent worker invocation automatically supplies all notes in user-message text, including across Worker replacement if ACI is reused.
- Delegated visibility: worker sees note strings, not separately stored source observations, author identities or confidence; no independent provenance travels with each note.
- Selection predicate: foreground model selects supplied text through the advertised action; code pushes the entire notes list on each worker call. No query matching or explicit size budget.
- Invalidation or expiry: RAM instance lifetime; no delete/revise/expiry operation in the inspected save method. S3 agent reset recreates Worker, not ACI, so task reset is not a clearing guarantee.
- Activation or effect: notes become advisory user-context material. Trial action checking may append before the selected outer action executes and may repeat the append.
- Evidence limits: no durable disk bank or observed note use established; arbitrary code can mutate files/state outside the designed notes operation but does not establish a managed curation route.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> generator_message += (
>             f"\nCurrent Text Buffer = [{','.join(self.grounding_agent.notes)}]\n"
>         )
> --- `gui_agents/s3/agents/worker.py`

Admission is software append of model-selected strings, not human approval or a facts checker. No answer oracle or improvement curriculum is present; the task and observation guide the open-request choice. Existing notes are neither deduplicated nor source-validated by this append/read chain. Formatter retry effects in the supplied runtime are a counterexample to assuming that only the final chosen action admits notes.

#### MEM-RTE-knowledge-save
Label: Alternative S2 KnowledgeBase save lifecycle

Distinct identity: exposed `KnowledgeBase.save_episodic_memory`, `save_narrative_memory`, trajectory helpers and `finalize_task`, rather than the AgentS2 updater methods in [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience). They write the same S2 stores, so object identity overlaps, but admission control and caller evidence differ. SRC-1: `gui_agents/s2/core/knowledge.py`. Search for these method names across `gui_agents/`, `osworld_setup/`, `integrations/` found internal helper calls/definitions, not a shipped external lifecycle caller.

- Immediate return: save methods return existing/new summary if enabled, or nothing when `save_knowledge` is false; lifecycle helpers accumulate/finalize/reset text state.
- Later read-back: storage capability only for this exposed write API — no wired caller was found; if called, the shared JSON stores are eligible for the separately wired historical retrieval route.
- Delegated visibility: helper summarizers see text trajectories supplied to the object; finalize can mark a pending subtask completed without an external outcome check.
- Selection predicate: caller invocation, `save_knowledge` flag and missing key; helper finalize writes narrative only with both task trajectory and current search query.
- Invalidation or expiry: existing keys preserved; finalize clears transient tracking strings, not saved content. No versioned rollback or semantic invalidation in these methods.
- Activation or effect: automatic model summary admission and JSON creation are afforded; deployment of this alternative lifecycle and resulting behavioral activation are not established.
- Evidence limits: cannot attribute these methods' save flag/directory creation/finalization guarantees to the distinct CLI AgentS2 updater path.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

> if not self.save_knowledge:
>             return
>
>         try:
>             kb = load_knowledge_base(self.episodic_memory_path)
> --- `gui_agents/s2/core/knowledge.py`

The generic library caller's human identity is unresolved; human per-content admission cannot be inferred. Model proposes summary text under shipped task/subtask prompts and software admits it on a new key, without a truth/success veto or reference answer. The save flag can suppress these writes, but query/search cache writes are not guarded by it. This alternative preserves the known transformation capability without inventing a deployed consumer of the API itself.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-procedural-memory](runtime.md#rt-obj-procedural-memory)

Shipped source literals are developer-authored static guidance, not use-accumulated memory. Worker construction renders available action signatures/docstrings and substitutes task/OS. Source edits would change later construction, but no automatic source-edit/adoption/redeployment route follows from this object. API visibility is not capability revocation. The runtime record's retained verification instruction supports the requested policy; it does not establish compliance. SRC-1: `gui_agents/s3/memory/procedural_memory.py`, `gui_agents/s3/agents/worker.py`.

#### On [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop)

Working-context control is code-owned, post-turn housekeeping: engine type selects image-only pruning for anthropic/openai/gemini, or oldest generator user/assistant pair and oldest reflector user turn removal otherwise. Budget is an image/turn count, not a token bound; retained text can grow in the image-only branch. Old screenshot bytes remain separately in `screenshot_inputs` and model responses in `worker_history`, but the flush function does not re-inject removed images or summarize them. System prompt remains. Source-read support extends the runtime's existing quote:

> if img_count > max_images:
>                                 del agent.messages[i]["content"][j]
> --- `gui_agents/s3/agents/worker.py`

S2.5 directly inspected worker uses the same engine-dependent policy; S2 worker instead keeps at most its configured trajectory-tail shape by deleting oldest full turns, with local maximum eight. S1 has a flush helper but the action-generation call is commented out. It actively removes accessibility IDs from old user text before adding the current tree; original history IDs are not recoverable through that rewritten message. This matters for context correctness rather than persistent learning. SRC-1: `gui_agents/s2_5/agents/worker.py`, `gui_agents/s2/agents/worker.py`, `gui_agents/s1/core/Worker.py`.

> # Clear older messages - we keep full context. if you want to keep only the last n messages, you can use the flush_messages function
>         # self.flush_messages(3) # flushes generator messages
> --- `gui_agents/s1/core/Worker.py`

> result = result.replace("id\t", "")
>
>                         # replace message content
>                         content["text"] = result
> --- `gui_agents/s1/core/Worker.py`

S3 reflection is a separate model context fed task, previous worker response and new screenshot. Its reply is injected as optional advice in the worker's current user message. It is not a replacement summary that preserves evicted screenshots; the raw history feeding reflection is not thereby the same as model-visible worker context. Worker reset drops histories/reflections; ACI notes have a separate lifetime. Historical subtask reset similarly discards a worker frame and reconstructs task/subtask/future/completed labels plus retrieved advice, rather than importing the entire prior worker dialogue. SRC-1: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/agent_s.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/s2/agents/worker.py`, `gui_agents/s1/core/AgentS.py`.

#### On [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience)

The CLI's raw task trajectory is text built from reflections and executor plans after ordinary action execution. Done/fail invokes narrative update before adding that turn; wait/next branches continue before trajectory accumulation. Episodic updater runs after ordinary executed actions, not on every predict result. Thus the summary producer does not receive every observation, result or terminal reflection simply because the source prompt says “Whole Trajectory.” Existing-key preservation also means later experience does not revise earlier summaries. SRC-1: `gui_agents/s2/cli_app.py`, `gui_agents/s2/agents/agent_s.py`.

> agent.update_narrative_memory(traj)
>             break
> --- `gui_agents/s2/cli_app.py`

> subtask_traj = agent.update_episodic_memory(info, subtask_traj)
> --- `gui_agents/s2/cli_app.py`

No guaranteed final pending episodic flush is present in this CLI terminal branch. Alternative KnowledgeBase finalization is a different API, not evidence that the CLI closes this gap. [MEM-RTE-knowledge-save](#mem-rte-knowledge-save) records the distinction. Task and subtask stores, their rationale limits and selection consumers are declared separately above.

#### On [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap)

Initial text/vector provenance and human review are unresolved because archive bytes are outside the freeze. HTTP/ZIP admission is software admission of caller-selected asset identity, not per-entry approval. S2 optional bootstrap tests a missing platform subdirectory; S1 automatically downloads if the whole KB root is absent, without the same opt-in flag. Both call the shared extractor. This qualifies applying the supplied historical-bootstrap trigger uniformly to S1. SRC-1: `gui_agents/s1/core/AgentS.py`, `gui_agents/s2/agents/agent_s.py`, `gui_agents/utils.py`.

> if not os.path.exists(self.local_kb_path):
>             download_kb_data(
>                 version="s1",
> --- `gui_agents/s1/core/AgentS.py`

Deleting the root to re-download is documented recovery, not selective rejection or rollback of one entry. Known later query, summary and embedding transformations remain separately established despite unknown initialization.

#### On [RT-RTE-code-delegation](runtime.md#rt-rte-code-delegation)

Coding execution resets its LMMAgent per call and passes selected task/subtask plus screenshot, excluding the outer worker dialogue. During that frame, actual controller status/output/error is formatted and fed into the next coding model invocation. Later return is a lossy extraction: actions/thoughts and summary, not that full result feedback. [MEM-OBJ-code-result](#mem-obj-code-result) supplies the material evidence. Execution budget is twenty by default; summary's requested size is under 150 words. The outer worker receives summary and rendered actions once, then cached return clears; accumulated worker text can retain delivery. SRC-1: `gui_agents/s3/agents/code_agent.py`, `gui_agents/s3/agents/worker.py`.

> result_context = format_result(result, step_count)
>             self.agent.add_message(result_context, role="user")
> --- `gui_agents/s3/agents/code_agent.py`

This resembles an isolated task frame with selected inputs/return. It is not a pure frame: executed code mutates shared environment state, and the retained return can omit the evidence needed to verify it. No pointer in the summary automatically reloads the omitted dialogue. Controller errors can shape within-frame revisions, but omitted feedback prevents attributing complete result-grounded rationale to the summary consumer.

#### On [RT-RTE-rollout-selection](runtime.md#rt-rte-rollout-selection)

Raw traces, answer/thought caption fields and selected-directory records have different consumers and authority, recorded separately above. Task selection uses score variance; step selection is every adjacent sorted screenshot pair with corresponding trajectory-line action. Failed captions are skipped; filename existence, not completeness validation, suppresses regeneration. Later loader discards `fact_thoughts`. ComparativeJudge uses its own final-screenshot helper choosing the largest parsed step, not the separately defined utility that verifies image validity and falls back to older valid images. Missing endpoint image pairs can be omitted while captions remain. SRC-1: `osworld_setup/s3/bbon/generate_facts.py`, `osworld_setup/s3/bbon/utils.py`, `gui_agents/s3/bbon/comparative_judge.py`.

> if (
>                 initial_screenshot_message is not None
>                 and final_screenshot_message is not None
>             ):
>                 messages.append(initial_screenshot_message)
>                 messages.append(final_screenshot_message)
> --- `gui_agents/s3/bbon/comparative_judge.py`

This limits any claim that the judgment always has complete visual evidence. Captions labelled facts can be unverified model interpretations; endpoint images are a partial independent display, not an outcome oracle. Persisted thoughts do not become a later revision process merely because they are stored.

## Write side

### Acquisition, curation and admission

Historical initialization admits a release bundle by HTTP/ZIP success or uses existing local stores; local-file authorship and external bundle lineage are unknown. S1 automatic versus S2 opt-in bootstrap is retained in the annotation on [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap). This unknown initial control does not hide subsequent known writes.

The CLI trace-fed chain is task/plan/reflection strings → model summary under shipped extraction prompts → missing-key JSON admission → later manager/worker guidance. Summarizers are the computational authors; key tests are admission, and JSON writing is physical I/O. Human task choice is not summary approval. Task prompts allow failure reasons; subtask prompts instead request only correct necessary recipes. The admitted summary is not assured to preserve reasons or source observations. Episodic summary generation also retains preceding trajectory/summary messages as exemplars in the summarizer instance; this is additional context across summarization calls, not a separately persisted cross-process store. SRC-1: `gui_agents/s2/agents/manager.py`, `gui_agents/s1/core/Manager.py`; [MEM-OBJ-narrative-memory](#mem-obj-narrative-memory), [MEM-OBJ-episodic-memory](#mem-obj-episodic-memory), [MEM-RTE-s1-experience](#mem-rte-s1-experience), [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience).

The S2 exposed KnowledgeBase lifecycle is an alternative checkpoint form: internally accumulated task/current-subtask text can be finalized and cleared, with save control and directory creation. It must not be substituted for the actual CLI's externally threaded strings and missing terminal episodic flush. Its caller remains unestablished. [MEM-RTE-knowledge-save](#mem-rte-knowledge-save).

Query and search miss responses persist independently of trace summaries. Software caches them automatically, without an expected answer; fusion may transform their meaning before planning but does not replace the cache with the fused list. Embedding miss filling changes access metadata, not content or weights. [MEM-RTE-query-cache](#mem-rte-query-cache), [MEM-OBJ-embeddings](#mem-obj-embeddings).

Foreground save-to-knowledge appends model-selected text with no curation beyond supplied strings. Formatting trial execution is an alternate admission point and can duplicate append effects. This is not per-action human approval. [MEM-RTE-notes-delivery](#mem-rte-notes-delivery), [RT-RTE-action-check](runtime.md#rt-rte-action-check).

Coding produces a summary from model action/thought history, while controller feedback stays in the coding conversation. Summary failures are rendered as text rather than rejected wholesale. The outer model gets the reduced return and is instructed to verify through GUI, but verification is a policy request. [MEM-OBJ-code-result](#mem-obj-code-result), [RT-CLM-gui-verification](runtime.md#rt-clm-gui-verification).

Offline trace-fed derivation is screenshots/action → narrator → answer/thought JSONL → answer-only loader plus endpoint images → comparative judge → persisted directory choice. A later score reader consumes the choice; a rerun uses task-key presence to avoid rejudging. This is retained behavior-shaping content for the selection/scoring workflow, not only raw logging, but no live worker update or improved capacity is demonstrated. [MEM-OBJ-traj](#mem-obj-traj), [MEM-OBJ-fact-captions](#mem-obj-fact-captions), [MEM-OBJ-judge-results](#mem-obj-judge-results).

### Rejection, withdrawal and cleanup

In the inspected historical updater/cache paths, existing keys suppress replacement, malformed loads can be treated as empty, and file/provider errors can stop or log failure. Those are control/error conditions, not truth review. Source deletion/replacement can withdraw file content; no semantic withdrawal graph or per-entry expiration is established in these methods. A stale vector is only access metadata and does not preserve a removed JSON entry as a candidate. The alternative save flag controls only its API path. [MEM-RTE-experience-retrieval](#mem-rte-experience-retrieval), [MEM-RTE-query-cache](#mem-rte-query-cache), [MEM-RTE-knowledge-save](#mem-rte-knowledge-save).

Offline caption exceptions omit steps, and file presence can freeze that partial set. Judge parsing can yield no selection, which may still persist and suppress retry. Neither is evidence-responsive correction of earlier content. Worker message/image eviction and reset are context cleanup, not withdrawal of disk experience. Notes survive Worker reset when ACI is retained. These distinct lifetimes prevent a single system-wide “memory reset” conclusion. [MEM-OBJ-fact-captions](#mem-obj-fact-captions), [MEM-OBJ-judge-results](#mem-obj-judge-results), [MEM-RTE-notes-delivery](#mem-rte-notes-delivery), annotation on [RT-RTE-desktop-loop](runtime.md#rt-rte-desktop-loop).

## Read-back

| Retained input | Trigger / selector / budget | Actual consumer, channel and force | Horizon and limits |
|---|---|---|---|
| Narrative summary | First manager plan; instruction embedding ranks keys; one result, exact-top skip | Manager system prompt, directly or through model fusion; optional planning guidance | Across tasks/processes if file retained; content use and benefit unobserved |
| Episodic summary | First enabled subtask worker turn; composite query embedding; one result | Worker system prompt, after S2 text substitutions; advisory recipe | Across resets/tasks; not automatic action replay, singleton exact-match failure possible |
| Query/result cache | Same instruction exact lookup, optional chosen search engine; whole value | Query identity/search, then fusion and manager guidance | Cross-invocation local JSON; changed observation not a cache-invalidating input |
| Dense vectors | Historical retrieval miss/hit by string key | Cosine-ranking code; fixed numerical selection behavior | Persisted metadata, no model-visible textual lesson in the vector itself |
| Notes | Every worker call, full-list push; no explicit size cap | Worker user message, task-context content | ACI lifetime, potentially across task resets in reused instance; no disk store established |
| Code result | First outer-worker call after delegation; full rendered actions plus summary; requested summary under 150 words | Worker user message; advisory evidence, then cached field cleared | Within task; retained message text may remain, raw controller dialogue omitted |
| Caption answers / endpoint images | Offline task-variance selection, all loaded answers plus available image pair per rollout | ComparativeJudge model user messages under comparison policy | Across saved runs; narrator thoughts excluded, not full trajectory evidence |
| Saved rollout choice | Rerun task-key test and scoring invocation | Software skip and selected result-file lookup | Persisted workflow authority; no installed GUI-worker policy |

All rows are supported by the records above; vector reads, static prompt construction and ordinary reflection histories are not relabelled as independent experience routes. Context eviction removes older material without a summary/checkpoint reload mechanism in the inspected flush functions. Coding and historical subtask isolation keep whole dialogues out; selected inputs and reduced outputs cross frames. Shared desktop/file effects and ACI notes break a pure stack-frame interpretation because they survive frame replacement. Provider-side retention remains opaque, rather than inferred from local histories. SRC-1: `gui_agents/s3/agents/worker.py`, `gui_agents/s3/agents/code_agent.py`, `gui_agents/s2/agents/agent_s.py`; [RT-CMP-lmm-agent](runtime.md#rt-cmp-lmm-agent).

## Integration issues

- **Bootstrap generation qualification.** [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap) describes the S2 opt-in/missing-platform trigger. S1 instead tests the KB root and downloads automatically when absent. Source and minimum passage are in the annotation. Consequence: do not generalize S2 initial-admission control to all historical versions.
- **Coverage additions, not replacement identities.** [MEM-RTE-s1-experience](#mem-rte-s1-experience) is the S1 generation path, distinct from supplied S2 route. [MEM-RTE-experience-retrieval](#mem-rte-experience-retrieval) spans the two generations' read operations and overlaps the read portion of [RT-RTE-historical-experience](runtime.md#rt-rte-historical-experience), but does not replace that execution/admission container. Reconciliation should connect them, not count two S2 memories. The four Part-of objects explicitly identify their runtime-route containers; a route contains a retained object, despite the different record kinds. Other store objects include both S1 and S2 instances and therefore are not wholly parts of the one S2 route.
- **Alternative save API must remain separate.** [MEM-RTE-knowledge-save](#mem-rte-knowledge-save) writes the same JSON referents as the CLI, but search found no shipped lifecycle caller. Its save flag and finalization cannot repair the CLI's pending-episode gap. Consequence: preserve afforded implementation separately from wired CLI operation and from wired downstream JSON retrieval.
- **Retrieval is qualified rather than universally successful.** [MEM-RTE-experience-retrieval](#mem-rte-experience-retrieval) retains exact-top skipping and its singleton failure case, plus empty-string-sentinel delivery. These qualify, rather than contradict, the runtime's selection account. No actual store was available to determine whether those cases occurred.
- **Opaque initialization and service state.** External release entries/vector lineage and provider-side retained state remain unresolved. Consequence: initial human review, original trace mixture, vector-version consistency and hidden service learning cannot be classified. Local transformations and later consumer wiring remain supported. [MEM-OBJ-embeddings](#mem-obj-embeddings), [MEM-OBJ-narrative-memory](#mem-obj-narrative-memory), [RT-RTE-kb-bootstrap](runtime.md#rt-rte-kb-bootstrap), [RT-CMP-lmm-agent](runtime.md#rt-cmp-lmm-agent).
- **No retained reasons guarantee at reduced consumers.** Code summary omits raw controller outputs, caption loader omits narrator thoughts, episodic extraction need not keep rejected-step reasons, and scoring reads selected-directory fields rather than judge rationale. Consequence: do not infer reason-preserving criticism or demonstrated learning from these labels. [MEM-OBJ-code-result](#mem-obj-code-result), [MEM-OBJ-fact-captions](#mem-obj-fact-captions), [MEM-OBJ-episodic-memory](#mem-obj-episodic-memory), [MEM-OBJ-judge-results](#mem-obj-judge-results).

No additional correction to supplied runtime facts or possible replacement duplicate is proposed. Actual use, correctness, capacity improvement and causal benefit remain unresolved for every retained chain because no observed run or experiment was supplied. These are evidence limits, not claims that wiring is absent.

## Limitations and checks

The frozen checkout HEAD was rechecked as `15776a8dc659658b1963816ea006f7af1978e595`; `git status --short` returned no changes. Supplied run/source identities and member/worker/record contracts were read, including the complete bounded runtime and records-contract inputs. New direct reads stayed within SRC-1 and the included functional scope. Bounded source searches checked memory-operation callers across `gui_agents/`, `osworld_setup/` and `integrations/`, note initialization/appends across generations, and historical versus current worker context controls. No broader negative about every possible external caller, arbitrary code effect or hidden service operation is warranted.

No execution, model-provider request, external release download or benchmark reconstruction was performed. Correct-step extraction, fact narration, model-guidance compliance and learning benefit are not observed. Text/raster/numerical encodings and local persistence do not establish source trust, theory criticism or exercised self-improvement. The report's source claims use the implementation/design layers only.

Deterministic validation: the required `commonplace-run validate-output` check passed for this invocation. This establishes form, identity/reference checks and quotation occurrence, not semantic acceptance or operational benefit.
