---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AgentFly's judgment-labelled case banks, query-driven example delivery, retriever checkpoints and tool-local retained files."
run-id: AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01
source-identity: "https://github.com/Agent-on-the-Fly/AgentFly"
reviewed-boundary: "42fbbcac63dd58ed6856c0761357345a58e4f032"
---

# AgentFly memory report

## Boundary and evidence

AgentFly retains question/plan/outcome cases in two shipped benchmark drivers. It also retains training pairs, retriever weights, result traces and tool-local files. This report uses SRC-1 at the frozen commit in [boundary](boundary.md). Direct inspection covered both CBR drivers and all three memory Python modules completely; first records of the three JSONL corpora; source searches across client, memory and server registrations, persistence, cache, deletion and entry points; and material workspace, document and video persistence/read ranges. Supplied runtime findings cover ordinary/local execution, tool extraction and interpreter cleanup. All direct findings are implementation or source-data evidence, not observed execution.

Excluded external provider state, transformer assets and dependency/service internals remain opaque. They prevent claims about provider-side retention, exact trained parameters or operational reliability. Corpus samples do not authenticate generation or establish corpus-wide quality. Static prompts and current-query messages are context surfaces, not automatically durable memory. No new source identity is introduced.

| Entry point or operation | SRC-1 path and inspection basis | Coverage and conclusion limit |
|---|---|---|
| Nonparametric driver initialization, append/reload, query selection | Direct: `client/no_parametric_cbr.py`, `memory/np_memory.py` | [MEM-OBJ-dummy-memo](#mem-obj-dummy-memo), [MEM-RTE-embedding-examples](#mem-rte-embedding-examples); configurable schema fallback and malformed-line handling included. |
| Parametric driver initialization, append/reload, query selection | Direct: `client/parametric_memory_cbr.py`, `memory/parametric_memory.py` | [MEM-OBJ-memory](#mem-obj-memory), [MEM-RTE-classifier-examples](#mem-rte-classifier-examples); missing checkpoint and malformed pool can disable retrieval. |
| Judgment, results and restart suppression | Direct: both CBR drivers | [MEM-OBJ-query-record](#mem-obj-query-record), annotation on [RT-RTE-case-admission](runtime.md#rt-rte-case-admission); result persistence has a recovery consumer even when later memory writes fail. |
| Pair writes and trainer admission/evaluation | Direct: parametric driver, `memory/train_memory_retriever.py` | [MEM-OBJ-training-data](#mem-obj-training-data), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), annotation on [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training); no supplied trained checkpoint or generation trace. |
| Standalone scoring CLI and exposed library alternatives | Direct: `memory/parametric_memory.py`, `memory/train_memory_retriever.py`, `memory/np_memory.py` | [MEM-RTE-retrieval-display](#mem-rte-retrieval-display); `topk_select` is a separate callable helper, not the driver selector. Unspecified callers establish capabilities only. |
| Ordinary/local message reset and executor trimming | Supplied runtime plus direct CBR reads; `client/agent.py`, `client/agent_local_server.py` searched | [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history); no durable compaction route established by these resets/trims. |
| Workspace write, read, execution and logs | Direct material ranges: `server/code_agent.py`; supplied interpreter findings | [MEM-OBJ-workspace-files](#mem-obj-workspace-files), [MEM-RTE-workspace-read](#mem-rte-workspace-read), [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution); display is not full storage, task-cache directory is caller-selected. |
| Document/media side files and later file consumers | Direct material ranges: `server/documents_tool.py`, `server/video_tool.py`; server persistence/registration searches | [MEM-OBJ-tool-files](#mem-obj-tool-files); binary payloads and external extraction fidelity not inspected. No automatic case-bank admission of these files established. |
| Returning crawl/search/image/math/spreadsheet tools | Server registration/persistence search; supplied [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction) | Returning transformations can feed current tool history. No inspected driver route makes those full outputs case content; whole dependency caching remains uninspected. |
| Provider/model opaque state | Supplied [RT-CMP-openai-backend](runtime.md#rt-cmp-openai-backend), [RT-CMP-direct-model-backend](runtime.md#rt-cmp-direct-model-backend), [RT-CMP-tool-judge-models](runtime.md#rt-cmp-tool-judge-models) | External retention, provider training and hidden processing unresolved; no system-wide absence inferred. |

## Core ideas

1. **Outcome labels govern interpretation, not admission.** Both drivers retain unsuccessful as well as successful plans. Their answer judge labels the final answer against dataset references; the retained plan is the latest parsed plan, not necessarily the full successful procedure. Thus a positive case is not a validated planning rule. The raw result preserves more evidence than the example sent to a later model ([RT-RTE-case-admission](runtime.md#rt-rte-case-admission), [MEM-OBJ-query-record](#mem-obj-query-record)).
2. **Two different selectors feed similar guidance.** Embedding retrieval ranks question similarity; classifier retrieval scores query/case-plan pairs. Only after ranking do labels partition examples into imitate/avoid groups. Neither route filters the bank to successful cases, and unknown parametric labels disappear from example sections ([MEM-RTE-embedding-examples](#mem-rte-embedding-examples), [MEM-RTE-classifier-examples](#mem-rte-classifier-examples)).
3. **Text memory and trained memory have different refresh horizons.** Driver writes reload cases for following questions. Retriever weights change only through separately started training and later initialization. Reloading cases does not load a new checkpoint ([RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)).
4. **Delivery is narrower than storage.** Case prompts omit tool traces and judge reasons. Workspace reads can truncate non-code text or return only binary metadata. Neither a retained payload nor its display label establishes that the next model receives its complete contents ([MEM-RTE-workspace-read](#mem-rte-workspace-read)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-dummy-memo
Label: dummy_memo JSONL cases

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

This is the nonparametric driver's distinct persisted case output, not the parametric bank or a new name for the admission route. Its default file is `memory/dummy_memo.jsonl`; environment configuration can replace it. JSON framing and numeric reward are symbolic access/interpretation metadata. Question and plan descriptions are natural-language content inside serialized plan JSON; later models interpret descriptions rather than execute the retained plan schema directly. File substrate is UTF-8 JSONL; loaded objects/pairs are process memory. Producer lineage is dataset question plus latest planner JSON plus whole-answer judge reward. Initialization provenance of the committed sample is unverified. Software appends without content approval; no author trust check or deduplication gate appears in the inspected writer (SRC-1, `client/no_parametric_cbr.py`, `memory/dummy_memo.jsonl`).

> mem_entry = {
>     "question": q,
>     "plan": rec.plan_json or "",
>     "reward": reward
> }
> --- `client/no_parametric_cbr.py`

The positive/negative distinction guides later planners and executors through [MEM-RTE-embedding-examples](#mem-rte-embedding-examples). Physical append admits both rewards. The default extractor requires configured question/plan fields; its two-key fallback treats the first key as question and second as value, potentially admitting other two-field data. Malformed JSON lines are skipped, missing fields otherwise ignored. These are parsing controls, not semantic curation (SRC-1, `memory/np_memory.py`).

#### MEM-OBJ-memory
Label: memory JSONL labelled cases

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

The parametric driver's distinct bank defaults to `memory/memory.jsonl`. It stores symbolic `case_label` and JSON envelopes, natural-language question and plan descriptions, and sometimes raw malformed plan text. Local JSONL persists across questions/processes; `_memory_pool` and metadata are derived process-memory views. The driver automatically writes current question/latest plan/positive-or-negative label, not judge rationale, answer evidence or the full trace. Committed case provenance is unresolved. The physical writer and content admission are software-controlled; starting the benchmark is not per-case human approval. Initial external edits are possible through the file surface, but no shipped editor or independent content review is established (SRC-1, `client/parametric_memory_cbr.py`, `memory/parametric_memory.py`, `memory/memory.jsonl`).

> memory_entry = {
>     "case": query,
>     "plan": plan,
>     "case_label": case_label
> }
> --- `client/parametric_memory_cbr.py`

`load_pool` requires a case and nonempty pool; malformed JSON fails the load. Plan parsing/pretty-printing creates text used by the scorer; case labels remain metadata until prompt grouping. The later consumer path is [MEM-RTE-classifier-examples](#mem-rte-classifier-examples), not direct execution of plan JSON.

#### MEM-OBJ-query-record
Label: QueryRecord result traces and judgments

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

This is the route's distinct rich result artifact. Each driver serializes `QueryRecord` plus question, plan, reference, prediction, judgment and rationale to local result JSONL. Natural-language planner inputs/outputs, task summaries, tool result strings and judge rationale mix with symbolic tool arguments, task IDs and record structure. Parametric records additionally carry retrieved cases and scores. These are raw-ish invocation records plus derived answer judgment, not just the reduced case bank. They are automatic driver outputs with no per-record human gate; committed corpus samples do not verify their generation. On restart, `main` reads only query/question fields to skip completed questions. The inspected memory selectors do not read these result traces or reasons (SRC-1, both `client/no_parametric_cbr.py` and `client/parametric_memory_cbr.py`).

> finished_task.append(record.get('query') or record.get('question'))
> --- `client/parametric_memory_cbr.py`

> rec_dict.update({
>     "question": q,
>     "plan": rec.plan_json,
>     "ground_truth": gt,
>     "pred_answer": pred_answer,
>     "judgement": judge_res["judgement"],
>     "rationale": judge_res["rationale"],
> })
> --- `client/parametric_memory_cbr.py`

Persistence changes scheduling through duplicate-query suppression, not example guidance. Result append precedes case/pair append; partial writes can therefore suppress a retry without completing memory admission, as already bounded in [RT-RTE-case-admission](runtime.md#rt-rte-case-admission).

#### MEM-OBJ-training-data
Label: training_data retrieved-case pairs

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

This distinct output defaults to `memory/training_data.jsonl`. Each retrieved case gets current query, retained case/plan/case label, and the same final-answer `truth_label`. Text is natural-language pair content; JSON fields and Boolean label are symbolic training controls. Local JSONL persists; dataset conversion builds process-memory samples. Lineage mixes previous cases and current benchmark outcome, not isolated evidence of each case's contribution. Software admits one row per retrieved case automatically when retrieval is nonempty; there is no per-case causal test or human veto. Sample provenance before this driver remains unverified (SRC-1, `client/parametric_memory_cbr.py`, `memory/training_data.jsonl`).

> training_entry = {
>     "query": query,
>     "case": case.get("case", ""),
>     "case_label": case.get("case_label", "unknown"),
>     "plan": case.get("plan", ""),
>     "truth_label": is_correct
> }
> --- `client/parametric_memory_cbr.py`

The trainer consumes `truth_label`, not `case_label`, so a positive source case can receive a false target on a failed current query. Unknown-label cases omitted from example sections can still receive pair rows, because pair writing iterates all retrieved cases. Later consumer is [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training), not the planner. Parser requirements are query/case/label presence; labels normalize to binary. Text formatting and truncation are transformations, not source validation (SRC-1, `memory/train_memory_retriever.py`).

#### MEM-OBJ-checkpoint
Label: Retriever state_dict checkpoints

Part of: [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)

This is the route's distinct numerical output, not another component declaration for [RT-CMP-case-retriever](runtime.md#rt-cmp-case-retriever). Distributed-parametric backbone/head state persists in local `best.pt` and `last.pt` files and becomes in-memory classifier weights on later initialization. Gradients derive it from pair text/labels; optional best selection uses validation AUC or F1, while final weights always save. Neither filename includes source reasons, raw traces or an optimization-history rationale. Software updates/saves; operator chooses inputs, hyperparameters, output paths and which checkpoint path a later process loads. There is no shown per-update human approval, automatic scheduling, atomic deployment or rollback gate. Numerical contents and exact deployed versions are unavailable because no checkpoint is tracked (SRC-1, `memory/train_memory_retriever.py`, `memory/parametric_memory.py`; supplied [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) supplies optimization and save passages).

#### MEM-OBJ-workspace-files
Label: Workspace files and execution logs

Part of: [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution)

Distinct retained parts of the terminal/workspace route: caller-selected `task_cache_dir/workspace` files and parent `execution.log`, plus process logging to `code_tool.log`. Files can be natural-language notes, symbolic executable scripts/configuration or opaque binary outputs; no one form covers them all. Write tool stores caller content, while terminal commands can derive files from execution. Software performs writes without default per-content approval; generic external callers do not establish human authorship. File overwrite has no built-in version history. JSONL execution logs retain operation/timestamp/workspace/details metadata, not necessarily full payloads or reasons; no automatic model consumer of those logs is established. The read surface and executable consumer differ ([MEM-RTE-workspace-read](#mem-rte-workspace-read), [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution); SRC-1, `server/code_agent.py`).

> log_file = Path(workspace_dir).parent / "execution.log"
> with open(log_file, "a", encoding="utf-8") as f:
>     f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
> --- `server/code_agent.py`

#### MEM-OBJ-tool-files
Label: Document and video retained side files

No counterpart for these distinct file outputs after comparison with supplied [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction) and [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution). Document processing writes converted DOCX/Chunkr Markdown or JSON, PPTX image side files and unzip contents under a cache directory. Video download writes bytes to caller-selected or temporary directories; audio extraction writes a sibling MP3. Local binary payloads remain opaque in this inspection; derived Markdown/text can be natural language, JSON framing symbolic. External documents/media and extraction services supply mixed provenance. Software writes under caller-triggered tool operations, not an independent human semantic approval gate (SRC-1, `server/documents_tool.py`, `server/video_tool.py`).

> out_path = f"{os.path.basename(path)}.{ 'json' if output_format=='json' else 'md' }"
> (result.json if output_format == "json" else result.markdown)(out_path)
> return open(out_path, encoding="utf‑8").read()
> --- `server/documents_tool.py`

> with yt_dlp.YoutubeDL(opts) as ydl:
>     info = ydl.extract_info(url, download=True)
>     return ydl.prepare_filename(info)
> --- `server/video_tool.py`

Converted-document read in the same call is immediate return, not later memory read-back. Exposed `get_video_bytes(video_path)` supplies a later read capability; shipped video/image/document tools can receive saved paths on subsequent executor calls. That is caller-requested file reuse, not automatic experience selection or case-bank ingestion. Actual reuse, expiration policy and external service retention are uninspected. These payloads are not evidence of multimodal case memory.

### Routes

#### MEM-RTE-embedding-examples
Label: Embedding-selected case examples

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

This is its nonparametric read-back subroute. At query start Python retrieves against loaded question/plan pairs, recomputing question and query embeddings; normalized vector dot products determine top-k. Query-driven selection is a request within the shipped driver, followed by automatic supply into user-role history, not an independent unsolicited push. The model does not request individual examples. Labels then partition examples by source row reward; missing reward becomes negative. Both successful and unsuccessful examples can reach later planner/executor invocations. No human selects individual examples or vetoes this delivery (SRC-1, `memory/np_memory.py`, `client/no_parametric_cbr.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted positive/negative example text, or none when retrieval fails or the pool is empty.
- Later read-back: Reloaded JSONL cases reach the next query's planner as user history and executors through shared history.
- Delegated visibility: Question/plan and group label reach models; similarity scores and full outcome/tool rationale do not appear in example text.
- Selection predicate: Current query versus retained question embeddings, top-k (default 8), then reward and per-sign display caps (default 8 each).
- Invalidation or expiry: Append/reload changes the bank; no automatic case expiry in this route. Shared history resets per query and is capped at 50 entries.
- Activation or effect: Guidance requests positive imitation and negative avoidance; behavior dependence and benefit are unobserved.
- Evidence limits: Embedding assets are not exact-version pinned; CUDA model initialization precedes the optional import handler and can fail before fallback. Device selection does not establish operational compatibility.

> sims = (query_vec @ key_vecs.T).squeeze(0)
> k = min(top_k, len(pairs))
> topk_scores, topk_idx = torch.topk(sims, k)
> --- `memory/np_memory.py`

Selector token budget defaults to 256 per question/query; delivery has count caps but no memory-specific token bound. Positive plan JSON becomes numbered descriptions when parseable; negative plan remains raw. Executor trimming is a separate approximate 175000-content-token budget and can remove older examples; planner history lacks that trimming. Dropping older entries/messages is not semantic summary generation (SRC-1, `client/no_parametric_cbr.py`, `memory/np_memory.py`).

#### MEM-RTE-classifier-examples
Label: Classifier-selected case examples

Part of: [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

This is its parametric read-back subroute. Query completion appends then reloads the bank; subsequent query intake asks the fixed initialized retriever to score current query against loaded case/plan text. Driver sorts descending and slices top-k. Labels group the selected set after scoring. Only positive/negative cases get example sections; unknowns can be scored, retained in result records and training pairs without being shown as examples. Python owns selection/delivery; model-generated plans and judge labels supply content but humans do not approve individual reads (SRC-1, `client/parametric_memory_cbr.py`, `memory/parametric_memory.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked case dictionaries followed by formatted example prompt, or empty retrieval on failure.
- Later read-back: Current process's reloaded bank supplies user-role examples to later benchmark planners and, via shared history, executors; later starts can load the persisted bank and configured checkpoint.
- Delegated visibility: Displayed case/plan and positive/negative section labels reach models, not classifier probabilities, raw result traces or judge rationale.
- Selection predicate: Classifier class-1 probability for current query and retained case/plan; driver top-k defaults to 8, then per-sign example caps.
- Invalidation or expiry: Appends reload text, not weights; parse failure clears the pool. If the file disappears the `_load_memory` guard does not clear an already loaded pool, so external deletion is not guaranteed immediate withdrawal.
- Activation or effect: Selected text is wired into later model input; numerical weights govern scoring, but exercised behavioral change or improved outcomes are unobserved.
- Evidence limits: Missing checkpoint disables retriever on startup; all-pool scoring can fail and return no cases. No trained state or runtime trace verifies meaningful ranking.

> results = retriever.retrieve(query, self._memory_pool, self._memory_metadata)
> results.sort(key=lambda x: x["score"], reverse=True)
> return results[:MEMORY_TOP_K]
> --- `client/parametric_memory_cbr.py`

> if retriever and load_pool and os.path.exists(MEMORY_JSONL_PATH):
> --- `client/parametric_memory_cbr.py`

Inference tokenizers truncate using their configured defaults without an explicit `max_length` in `_score_batch`; trainer defaults to 256. Prompt delivery has count caps, not a dedicated token guarantee. Model semantic guidance is a policy, not enforcement. Source labels are trusted as file metadata; the reader does not recompute correctness. Parsed positive plans drop extra plan fields from display; negative plans stay raw, and positive parse exceptions fall back to raw text (SRC-1, `memory/parametric_memory.py`, `client/parametric_memory_cbr.py`).

#### MEM-RTE-retrieval-display
Label: Standalone retrieval display

This distinct CLI route is not contained in the query driver: `memory/parametric_memory.py` main loads operator-supplied checkpoint/pool/query, scores every case, sorts and prints examples. Closest supplied [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) produces weights rather than displaying cases; [RT-RTE-case-admission](runtime.md#rt-rte-case-admission) runs/judges questions rather than returning this display. The CLI accepts externally supplied files without semantic approval or outcome oracle; it is an open retrieval request (SRC-1, `memory/parametric_memory.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed score, index, label and built case/plan text.
- Later read-back: Persisted pool/checkpoint are selected on a later standalone invocation; no wired planner consumer follows the print operation.
- Delegated visibility: CLI reader receives selected formatted pool text and scores, not training history or original tool evidence.
- Selection predicate: Current CLI query versus all pool text, descending score; default topk 5, but nonpositive or at-least-pool-size values return all.
- Invalidation or expiry: Each invocation reloads configured files; external replacement affects a subsequent invocation.
- Activation or effect: Ranking and printing are wired; subsequent human adoption or agent use is uninspected.
- Evidence limits: This exposure is not automatic checkpoint deployment or a documented complete external agent integration.

> topk = ranked[:args.topk] if 0 < args.topk < len(ranked) else ranked
> --- `memory/parametric_memory.py`

`np_memory.retrieve` exposes embedding lookup, and trainer `topk_select` exposes batched classifier lookup with explicit max-length 256. No inspected shipped caller consumes `topk_select` output. Those callable capabilities do not establish additional later-agent routes (SRC-1, `memory/np_memory.py`, `memory/train_memory_retriever.py`).

#### MEM-RTE-workspace-read
Label: Requested workspace file read

Part of: [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution)

This distinct read operation completes the workspace route's material text-consumption surface. Later executor-selected MCP calls can ask `read_workspace_file` for previously written content. Caller supplies directory and filename; the tool reads filesystem content and returns a display. It does not choose a relevant file autonomously or make a semantic adoption decision (SRC-1, `server/code_agent.py`; surrounding executor dispatch established by [RT-RTE-query-execution](runtime.md#rt-rte-query-execution)).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: File text with name, workspace, size and optional truncation notice; missing-file/error or binary metadata instead of content when applicable.
- Later read-back: Prior workspace writes can reach subsequent executor invocations via MCP result text; scripts can alternatively be consumed by terminal execution without this display.
- Delegated visibility: Executor receives the returned display; planner normally receives only final executor summary. Binary bytes are not decoded by this reader.
- Selection predicate: Caller filename and task_cache_dir identify the file; non-code text is truncated to first/last portions using a rough 1000-token/4000-character budget, code extensions bypass it.
- Invalidation or expiry: Overwrite replaces content; persistent files remain until external removal, while supplied interpreter findings cover temporary script cleanup separately.
- Activation or effect: Read and subsequent context delivery are wired; later model reliance on returned content is unobserved.
- Evidence limits: Path naming is not relevance selection or isolation; listing/info/structure tools expose metadata rather than full payloads.

> display_content = _truncate_text(content, max_tokens=1000, filename=filename)
> --- `server/code_agent.py`

> if file_ext in code_extensions:
>     return text
> --- `server/code_agent.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history)

The nonparametric driver limits shared history to 50 entries in addition to resetting it; executor content trimming preserves system plus a recent suffix, not a derived summary. The parametric driver clears on normal return, not at query start; an exception before clear can leave previous-query material for the next query in `main`'s continuing loop. This is accidental process-state carryover, not a durable authored memory artifact. It limits the supplied current-query characterization on exceptional paths (SRC-1, `client/no_parametric_cbr.py`, `client/parametric_memory_cbr.py`).

> if len(self.shared_history) > MAX_TURNS_MEMORY:
>     self.shared_history.pop(0)
> --- `client/no_parametric_cbr.py`

The clear-on-normal-return and exception continuation passages appear directly in the parametric driver; no exception cleanup restores pristine context before the next call. No provider conversation-state retention follows from client lists.

#### On [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)

Trace-to-memory lineage has three outputs with different consumers: rich result records feed restart suppression, reduced latest-plan cases feed model examples, and retrieved-case/outcome pairs feed classifier training. Raw tool traces and judge reasons are retained only in rich results, not transmitted as case reasons. Both signs are admitted automatically; judge failure becomes incorrect rather than a rejected write. Negative examples request avoidance without identifying which plan step caused failure. Starting the benchmark is not human approval of labels or plans. Direct inspection confirms the supplied route's persistence and partial-write limits (SRC-1, both CBR driver files; [MEM-OBJ-query-record](#mem-obj-query-record), [MEM-OBJ-training-data](#mem-obj-training-data)).

#### On [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)

Pair dataset construction ignores `case_label` and normalizes `truth_label`; training's CLI `--use_plan` defaults false, but README's explicit training command supplies it. Thus the supplied mismatch warning is a possible configuration divergence, not evidence that the documented training recipe omits plans. Tokenization further limits what the update consumer receives. Random pair-row train/validation splitting does not enforce query-level grouping, so multiple pairs from one question need not remain in the same partition. Metrics measure pair-label prediction, not independently varied case contribution or later task improvement (SRC-1, `memory/train_memory_retriever.py`, `README.md`).

> parser.add_argument("--use_plan", action="store_true")
> --- `memory/train_memory_retriever.py`

> python train_memory_retriever.py \
>   --train training_data.jsonl \
>   --output_dir ./ckpts/retriever \
>   --use_plan \
>   --val_ratio 0.1 \
>   --batch_size 32 \
>   --lr 2e-5 \
>   --epochs 10 \
>   --save_best
> --- `README.md`

#### On [RT-BAP-case-guidance](runtime.md#rt-bap-case-guidance)

Stored case text enters a user message, not the system instruction channel. Positive plans may be prettified to numbered task descriptions; negative plans remain raw; rationale and tool evidence do not accompany either. The classifier consumes numerical weights and tokenized text, while planners/executors receive the formatted examples, so authority at the update/ranking consumer differs from interpretive guidance at downstream agents. Delivery does not establish compliance or learning benefit (SRC-1, both CBR drivers and `memory/parametric_memory.py`; [MEM-RTE-embedding-examples](#mem-rte-embedding-examples), [MEM-RTE-classifier-examples](#mem-rte-classifier-examples)).

## Write side

Acquisition begins with benchmark question/reference files, initial JSONL banks and externally resolved embedding/checkpoint assets. Initial case authorship and training-data generation are not authenticated. Known subsequent transformations remain inspectable despite that provenance gap. Models author plans and final answers; the judge derives whole-answer labels; software reduces completed query records to question/latest-plan/label cases and retrieved-case/outcome pairs. Human choices configure datasets, paths, models and training, not individual content admission ([RT-RTE-case-admission](runtime.md#rt-rte-case-admission), [MEM-OBJ-dummy-memo](#mem-obj-dummy-memo), [MEM-OBJ-memory](#mem-obj-memory)).

Admission is completion-dependent append, not success-only filtering. Parsing failures before a query record returns can prevent a write; judge failure instead admits a negative case. Empty latest plans are possible when no parsed plan preceded an answer/error. Case loading and prompt formatting are separate filters: nonparametric malformed lines skip; parametric malformed pools fail wholesale; unknown labels can be selected yet omitted from display. No automatic semantic correction of historical labels is shown. External file edits can replace content, but configured reload behavior matters: deleting the parametric bank does not necessarily withdraw its already loaded view ([MEM-RTE-classifier-examples](#mem-rte-classifier-examples)).

Result → training pairs → case → reload are ordered, not transactional. A result can survive while later writes fail; restart suppression then prevents the missing admission from being retried. This differs from rolling back memory. Cases append without expiry/deduplication in the inspected writers. The README lists memory pruning/compression as future work, not a shipped mechanism (SRC-1, `README.md`, both CBR drivers; [RT-RTE-case-admission](runtime.md#rt-rte-case-admission)).

The trace-fed numerical chain is retrieved text/current outcome → pair labels → dataset formatting/truncation → gradient updates → best/final checkpoint → later inference initialization → ranking → examples. Whole-answer truth copied to all retrieved cases is not a retained reason that each case helped. Checkpoint selection retains parameters, not formulated criticisms, and no inspected inference route reconstructs reasons from result logs. These source-level pathways establish automatic trace-fed behavior-shaping material, not improved future capacity or exercised self-improvement ([MEM-OBJ-training-data](#mem-obj-training-data), [MEM-OBJ-checkpoint](#mem-obj-checkpoint), [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training)).

Tool files have separate admission: caller/model text writes or commanded computations persist payloads; overwrite is replacement without versioning; read display may omit the middle or binary contents. Temporary interpreter cleanup is not corpus cleanup. Document/media side files derive from external sources and services rather than benchmark trace reduction; they are not folded into the case bank by the inspected drivers ([MEM-OBJ-workspace-files](#mem-obj-workspace-files), [MEM-OBJ-tool-files](#mem-obj-tool-files)).

## Read-back

The two benchmark selectors request retained material using the current question, choose examples, and supply them automatically to planner history. That supply is downstream of a query-triggered selection operation; it is not a free-running push system. Planner receives examples before producing a plan; executor inherits them until message/entry budgets omit them. Counts bound selected/displayed examples but not exact delivered token length. Fixed shipped system prompts govern how to interpret examples; source-provided label metadata has no independent trust gate ([MEM-RTE-embedding-examples](#mem-rte-embedding-examples), [MEM-RTE-classifier-examples](#mem-rte-classifier-examples)).

Other later consumers have distinct roles: result readers suppress repeated benchmark work; separately launched trainers consume pair data; later retriever initialization consumes checkpoints; standalone CLI consumers receive retrieval displays; executor-requested file tools read stored payloads or execute scripts. A bare library helper with no caller establishes only capability. Raw reason retention in result JSONL does not establish reason read-back to planning. Neither immediate extraction text nor static prompts count as accumulation through use without a retained/later-consumed result ([MEM-OBJ-query-record](#mem-obj-query-record), [MEM-RTE-retrieval-display](#mem-rte-retrieval-display), [MEM-RTE-workspace-read](#mem-rte-workspace-read), [RT-RTE-crawl-extraction](runtime.md#rt-rte-crawl-extraction)).

## Integration issues

- **Exceptional history carryover qualifies supplied runtime.** [RT-OBJ-shared-history](runtime.md#rt-obj-shared-history) correctly says the parametric normal return clears history, but that does not cover error continuation. A failure before clear can carry prior context into another question. Preserve this qualification when classifying temporary-state horizons; it does not establish durable case memory (SRC-1, `client/parametric_memory_cbr.py`; annotation above).
- **Documented training recipe mitigates default divergence.** [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training) identifies a real CLI/inference default mismatch. README explicitly opts into plans; retain the warning as configuration-sensitive, not an assertion about that recipe (SRC-1, `README.md`, `memory/train_memory_retriever.py`).
- **External withdrawal has stale-view behavior.** [MEM-RTE-classifier-examples](#mem-rte-classifier-examples) adds missing-file reload semantics not stated by [RT-RTE-case-admission](runtime.md#rt-rte-case-admission): the existing in-memory bank can survive deletion. This prevents equating physical file withdrawal with immediate operational withdrawal (SRC-1, `client/parametric_memory_cbr.py`).
- **Record identity.** The six case/result/pair/read-back declarations explicitly contained in [RT-RTE-case-admission](runtime.md#rt-rte-case-admission), the checkpoint part of [RT-RTE-retriever-training](runtime.md#rt-rte-retriever-training), and workspace object/read parts of [RT-RTE-terminal-execution](runtime.md#rt-rte-terminal-execution) refine rather than replace their containers. No possible duplicate referent is proposed. Existing retriever components, history and behavioral-authority paths receive annotations/citations rather than duplicate declarations. Standalone retrieval display and document/media side files have no supplied counterpart.
- **Remaining source uncertainties.** Initial corpus provenance, trained checkpoint contents, exact external model versions, actual reuse of tool files and service/provider retention remain unresolved. The named objects/routes retain these limits; no deployment, corpus-wide correctness, activated model reliance or successful learning conclusion is supported. Available unsampled corpus rows are uninspected, not inaccessible.

## Limitations and checks

HEAD was rechecked as `42fbbcac63dd58ed6856c0761357345a58e4f032`; Git status was clean before source inspection. The target was neither executed nor modified. Source paths and quotations were checked against SRC-1; source-native JSONL samples were read only as data artifacts. Method scope followed the supplied memory type, job, worker rules and records contract; no prior analyses, peer attempts or external sources were consulted.

No supplied run trace or causal comparison supports activation, learning gains, autonomous deployed retraining, or exercised self-improvement. Hidden model processing cannot establish inspectable retained criticism. Available code supports the transformations and consumer wiring described here; missing execution is not used to erase that capacity. Validation: passed by the invocation-specific `commonplace-run validate-output` check; this establishes structural/quotation validity, not semantic acceptance.
