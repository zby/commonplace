---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "AgentFly's planner–executor invocation, MCP effect paths, case-admission drivers and separate retriever training at the frozen commit."
run-id: AAS-2026-10-12-agentfly-bbfc9fb2d5c7-01
reviewed-boundary: "42fbbcac63dd58ed6856c0761357345a58e4f032"
---

# AgentFly runtime report

## Runtime account

This account uses SRC-1 implementation and source prompts within [the boundary](boundary.md). It establishes wiring, not successful operation, model compliance or learning benefit. No target execution or experimental results were supplied or produced. Additional inspection covered local backend adaptation, subprocess execution, file-name normalization, media provider calls and trainer checkpoint selection at the same frozen commit.

### Ordinary invocation

The shipped `client/agent.py` CLI accepts a question, optional file path, planner/executor model names and server script paths. With no question it prompts interactively; each query receives a UUID. The client loads environment configuration, launches Python or Node servers over stdio, initializes MCP sessions, and registers returned tool names. A duplicate name raises an error. These server scripts are executable extensions selected by the operator; tool discovery does not establish trustworthiness or restrict their host effects (SRC-1, `client/agent.py`).

[RT-RTE-query-execution](#rt-rte-query-execution) traces the query. The client resets shared history, supplies question/task ID/file path as user text, and asks the planner model for a JSON plan or a `FINAL ANSWER:` prefix. Python parses the plan; the plan's IDs and descriptions construct task requests. Tasks execute serially. Each executor receives its own system prompt, shared query/plan/prior task results and the task description. The executor either returns nonempty text, ending the task, or selects MCP function calls. Calls are decoded, dispatched to the registered session and their stringified content added to that task's executor conversation. Raw tool results are not independently copied into planner history: the planner sees the executor's final task result. After the tasks the planner owns the next plan or terminal answer. Three planner cycles are allowed; exhaustion returns the last planner text, which need not be an answer (SRC-1, `client/agent.py`).

There is no distributed scheduler in this path: the Python coroutine owns serial progression and both model backends. Session identities are keyed by tool name; tool call IDs correlate replies; task IDs are model-visible text, not enforced access-control identities. Shared history is temporary, and the next interactive query resets it. The CLI prints the returned string under a final-answer label even for a planner error or exhausted plan. Provider calls retry up to three times with exponential waits; malformed plan parsing returns an error string. Tool argument parsing, unknown tool lookup and MCP call errors are not caught by the ordinary task loop. Cleanup closes acquired sessions in the main query block's `finally`, but server connection occurs before that block (SRC-1, `client/agent.py`).

### Controls and forcing cases

The strongest inspected client invariant is the outer planner-cycle bound, owned and enforced by `range(self.MAX_CYCLES)` in each shipped client. It covers planner iterations, not task count or the executor's `while True`. A backend returning neither text nor calls can keep that inner loop running. Nonempty text wins over calls in the ordinary OpenAI path; the direct streaming backend deliberately suppresses text when calls exist. Thus neither termination nor execution of every emitted call is guaranteed. Implementation conclusion status: wired. Operation conclusion status: uninspected. Guarantee strength: invariant, scoped only to outer cycle count. External completion and MCP responsiveness remain necessary for progress (SRC-1, `client/agent.py`, `client/agent_local_server.py`, `client/no_parametric_cbr.py`, `client/parametric_memory_cbr.py`).

Executor trimming is best effort, not an exact context guarantee: it counts content and role overhead, preserves the first system message and recent suffix, and does not count the supplied tool schemas or function-call argument structure. Planner messages are not trimmed on the ordinary route. The planner/tool division is implemented by supplying tools only to the executor call, while prompt language requests the division. This does not mean only the executor model exists: tools and the benchmark judge make separate model calls (SRC-1, `client/agent.py`, `server/ai_crawl.py`, `client/parametric_memory_cbr.py`).

Four forcing cases were inspected without executing them:

1. **Mixed text and calls or empty replies:** the ordinary executor's content-first branch can omit calls, and its unbounded inner loop defeats a system-wide three-step termination claim. See [RT-RTE-query-execution](#rt-rte-query-execution).
2. **Local model adaptation:** [RT-RTE-local-execution](#rt-rte-local-execution) chooses a direct OpenAI-compatible streaming executor for Qwen3 names, aggregates calls, supplies a fallback search schema, resolves aliases/substrings and translates arguments. A schema supplied to the model is not proof of a corresponding registered tool. Resolution failures become tool-result text; malformed JSON and actual MCP call failure still escape that handler.
3. **Shell and workspace effects:** [RT-RTE-terminal-execution](#rt-rte-terminal-execution) reaches Bash through the subprocess interpreter without the separate Python import-whitelist check. A working directory is not a filesystem isolation boundary. The shipped terminal tool selects subprocess execution and default confirmation is false. Alternative Docker/E2B/Jupyter wrapper branches exist, but their deployed isolation and credentials are not established by this inspection.
4. **Memory unavailable or partial completion:** [RT-RTE-case-admission](#rt-rte-case-admission) can continue without the parametric retriever when import/checkpoint loading fails. It writes results before training examples and case entries; later failures are not transactionally rolled back. Restart skipping reads the result file, so a recorded question can be skipped even if subsequent memory admission failed.

The capability surface includes operator-selected server code, model-selected tools, network services and shell/file operations. The actual current grant set depends on the selected scripts, advertised names and provider/environment configuration; no live grant inventory was supplied. The isolation envelope depends on OS/service deployment, not on MCP transport, task ID text or workspace naming. The normal client dispatch supplies no per-call human approval gate. A lower-level interpreter can request confirmation, but that is not the terminal tool's default grant. No universal permission or sandbox guarantee is claimed here (SRC-1, `client/agent.py`, `server/code_agent.py`, `server/interpreters/subprocess_interpreter.py`).

### Change and model boundaries

The two benchmark drivers are shipped entry paths, not excluded callers. They read questions and reference answers from `data/deepresearcher.jsonl`, run the planner/executor loop, judge final answers, append results and retain plans for later queries. The parametric driver also labels retrieved cases for training. These automatic writes have no per-content human approval; starting the driver is not approval of each plan or label. Their admission and answer-oracle roles are recorded in [RT-RTE-case-admission](#rt-rte-case-admission). Detailed case-memory transformations belong to the memory analysis.

[RT-RTE-retriever-training](#rt-rte-retriever-training) is a separate operator-started training program, not a call scheduled by the query driver. It changes the numerical retriever, saves final weights and optionally chooses best validation weights. The inference driver loads a configured checkpoint on module initialization; its per-query `_load_memory()` reloads cases, not weights. A new checkpoint requires a later initialization or external integration. Product/provider/server configuration can also be changed externally through arguments, environment or source editing, but this source does not establish automated runtime admission of such product revisions (SRC-1, `client/parametric_memory_cbr.py`, `memory/train_memory_retriever.py`).

The inspected models are separately accounted for below. Endpoint model names, including dated names, do not pin exact provider parameters. Tool-local extraction is a separate returning model computation, not another executor permission channel. Its output is a transformed page representation; source prompt demands grounding, but the runtime performs no independent check of extracted quotations (SRC-1, `server/ai_crawl.py`).

## Shared records

### Components

#### RT-CMP-openai-backend
Label: Planner and executor OpenAIBackend

Source-native instances `meta_llm` and `exec_llm` use distributed-parametric remote models, while Python backend code and payloads are symbolic. Weights reside with the provider; current messages reside in client memory. No weight update is issued in inspected query paths; provider internal mutation is uninspected. Exact weight versions are not pinned, and configurable OpenAI/Azure-compatible endpoints can resolve model names to other implementations. Ordinary defaults are planner `gpt-4.1` and executor `o3-2025-04-16`; benchmark defaults differ (SRC-1, `client/agent.py`, `client/parametric_memory_cbr.py`).

> self.meta_llm = OpenAIBackend(meta_model, is_azure)
> self.exec_llm = OpenAIBackend(exec_model, is_azure)
> --- `client/agent.py`

#### RT-CMP-direct-model-backend
Label: DirectModelBackend

The local client's Qwen3 executor is distributed-parametric model inference behind a configurable OpenAI-compatible endpoint; buffers and call reconstruction are symbolic client state. The repository does not supply exact weights or revisions. No client-side parameter update is issued; endpoint mutability permits a different model and server-internal changes remain uninspected (SRC-1, `client/agent_local_server.py`).

> if exec_model.lower().startswith("qwen3"):
>     self.exec_llm = DirectModelBackend(model=exec_model)
> else:
>     self.exec_llm = OpenAIBackend(exec_model, is_azure)
> --- `client/agent_local_server.py`

#### RT-CMP-case-retriever
Label: CaseRetriever and nonparametric embedding model

These are distinct distributed-parametric alternatives. `CaseRetriever` uses a RoBERTa backbone and learned two-class head, loaded from a local checkpoint into CPU/GPU memory. Inference uses eval/inference mode and does not update weights; the separate training program updates backbone/head. Its exact checkpoint is configurable, absent from tracked source and not digest-pinned. Hugging Face asset names are not revision-pinned. The nonparametric driver instead loads `princeton-nlp/sup-simcse-bert-base-uncased` onto CUDA and uses normalized embeddings with dot-product ranking; no fine-tuning occurs in that query path. Local files or remotely resolved assets can change across starts; exact deployed parameters are uninspected (SRC-1, `memory/parametric_memory.py`, `memory/np_memory.py`, `client/no_parametric_cbr.py`, `memory/train_memory_retriever.py`).

> self.model.load_state_dict(torch.load(model_path, map_location=self.device))
> self.model.eval()
> --- `memory/parametric_memory.py`

> memo_tokenizer = AutoTokenizer.from_pretrained("princeton-nlp/sup-simcse-bert-base-uncased")
> memo_model = AutoModel.from_pretrained("princeton-nlp/sup-simcse-bert-base-uncased").to('cuda')
> --- `client/no_parametric_cbr.py`

#### RT-CMP-tool-judge-models
Label: Tool-local models and answer judge

Separate remote distributed-parametric calls serve page extraction (`gpt-4.1`), image/video question answering (`gemini-2.5-pro-preview-05-06`), video transcription (`whisper-1`) and benchmark judging (`gpt-4o-mini`). Storage and parameter maintenance are external; inspected callers issue inference, not weight updates. Exact parameter versions are not pinned; environment-configured endpoints can map identifiers differently. Internal state and provider learning are uninspected. These are separate consumers, not one shared model invocation (SRC-1, `server/ai_crawl.py`, `server/image_tool.py`, `server/video_tool.py`, `client/parametric_memory_cbr.py`).

> response = await openai_client.chat.completions.create(
>     model="gemini-2.5-pro-preview-05-06",
>     messages=messages,
> )
> --- `server/image_tool.py`

> JUDGE_MODEL = "gpt-4o-mini"
> --- `client/parametric_memory_cbr.py`

### Operative objects

#### RT-OBJ-shared-history
Label: shared_history and task-local exec_msgs

Python lists hold current conversation in process memory. Natural-language question, instructions, plan descriptions and results receive consequences through model interpretation; symbolic role/tool-call envelopes and JSON plan structure receive fixed Python/API consumption. Task-local raw tool outputs reach the executor, whereas shared history carries final task summaries to the planner. This is ordinary current-query state, not evidence of durable retained memory. Baseline resets it at query start; parametric normal return clears it (SRC-1, `client/agent.py`, `client/parametric_memory_cbr.py`).

> self.shared_history = []
> self.shared_history.append({"role": "user", "content": f"{query}\ntask_id: {task_id}\nfile_path: {file}\n"})
> --- `client/agent.py`

### Routes

#### RT-RTE-query-execution
Label: Ordinary planner–executor query

User/CLI → planner → parsed tasks → executor → MCP sessions → executor task results → planner → returned string. Python owns sequence and stopping; models propose plans, calls and textual completion. Natural-language policy guides generation; symbolic parsing/prefix checks decide progression. Open-request operating mode has no reference-answer oracle or human per-step veto. Task IDs do not constrain tool effects. Provider retries and final cleanup are recovery mechanisms, not rollback of completed effects (SRC-1, `client/agent.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stripped final answer, planner-error text or last planner output after three cycles.
- Later read-back: inapplicable — the ordinary query route does not persist its history for later queries.
- Delegated visibility: Executor receives shared history; planner receives final task result text rather than the full tool conversation; MCP server receives named call arguments.
- Selection predicate: Parsed plan order, nonempty executor content, model-emitted function names and planner prefix determine branches.
- Invalidation or expiry: Query start resets shared history; task-local messages are discarded after task completion.
- Activation or effect: Calls are wired to MCP dispatch and textual results to subsequent model inputs; exercised effects or behavior dependence are unobserved.
- Evidence limits: No traces; provider behavior, tool responsiveness and eventual inner-loop termination are unestablished.

> if exec_reply["content"]:
>     result_text = str(exec_reply["content"])
>     self.shared_history.append({"role": "assistant", "content": f"Task {task['id']} result: {result_text}"})
>     break
> --- `client/agent.py`

> session = self.sessions[t_name]
> result_msg = await session.call_tool(t_name, t_args)
> result_text = str(result_msg.content)
> --- `client/agent.py`

#### RT-RTE-local-execution
Label: Local streaming executor and tool adaptation

The local client's executor backend differs from the ordinary route, while the planner remains OpenAIBackend. Streaming fragments become function-call buffers; Python aliases/substrings resolve tool names and patches search arguments. Client code owns dispatch, not the model server. Open-request mode has no reference oracle; model proposes calls and Python rejects unresolved names by returning error text. Operator selects models/scripts, not individual calls (SRC-1, `client/agent_local_server.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Executor content or reconstructed calls; the surrounding client returns query output.
- Later read-back: inapplicable — buffers and conversation are current-query state, not retained updates.
- Delegated visibility: Endpoint receives message history/tools; MCP server receives resolved name and patched arguments.
- Selection predicate: Qwen3 model-name prefix selects direct backend; exact name, search alias then substring match select session.
- Invalidation or expiry: Stream buffers expire per call; shared history resets per query.
- Activation or effect: Function calls are wired through compatibility translation into MCP execution; compliance is unobserved.
- Evidence limits: Backend advertises fallback search even without supplied tools; successful resolution and service compatibility are not established.

> content = None if tool_calls else (aggregated_text or None)
> return {"content": content, "tool_calls": tool_calls}
> --- `client/agent_local_server.py`

#### RT-RTE-terminal-execution
Label: Workspace write and terminal execution

Executor/MCP caller → `write_workspace_file` and `execute_terminal_command` → task workspace and subprocess interpreter. Model/caller proposes file content and commands; software writes or executes without default human approval. File writes normalize the filename to a basename, but `task_cache_dir` is caller supplied. Terminal execution uses Bash scripts, host environment and workspace cwd; shell code is symbolic executable content, arbitrary file content may be natural-language or symbolic. This admits task capabilities/scripts and potentially host-visible changes, not a demonstrated product-improvement cycle. Source guidance recommends write-then-execute; files persist until externally removed. No automatic prior-version rollback is shown in this path (SRC-1, `server/code_agent.py`, `server/interpreters/subprocess_interpreter.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: File-write status or subprocess stdout/stderr encoded as a string.
- Later read-back: Workspace files can be read by file tools or executed by later terminal calls using that workspace.
- Delegated visibility: Interpreter inherits host environment and receives generated code; executor receives returned text, not an independently validated execution certificate.
- Selection predicate: Model-selected tool/arguments and caller workspace identify the effect destination; terminal tool selects subprocess backend.
- Invalidation or expiry: File overwrite replaces content; subprocess temp scripts are cleaned up; persistent workspace expiry is externally determined.
- Activation or effect: Direct filesystem writes and process execution are wired; no deployed containment or successful command execution was observed.
- Evidence limits: Python import validation belongs to a separate execute_code method, not this shell route; OS permissions and external backend isolation remain uninspected.

> sandbox_instance = _get_or_create_sandbox(workspace_dir, "subprocess", verbose, False)
> --- `server/code_agent.py`

> result = self.interpreter.run(command, code_type="bash")
> --- `server/code_agent.py`

> env = os.environ.copy()
> --- `server/interpreters/subprocess_interpreter.py`

> require_confirm: bool = False,
> --- `server/code_agent.py`

The subprocess `shell=False` flag concerns how the interpreter launches Bash/Python; it does not prevent Bash script shell operations. Timeout handling kills the launched process and returns diagnostic text. The wrapper marks any string result as successfully executed, even though the interpreter can encode failures within that string. Treat this as a reporting limitation, not success evidence (SRC-1, `server/code_agent.py`, `server/interpreters/subprocess_interpreter.py`).

> elif isinstance(result, str):
>     return f"✅ Command executed.\n\nOutput:\n{result}"
> --- `server/code_agent.py`

#### RT-RTE-crawl-extraction
Label: Tool-local crawl and model extraction

MCP caller → crawler Markdown → extraction model → string result. Python owns rate admission and provider retry; the extraction model interprets the page/query under source grounding instructions. No answer oracle or independent quote validator is supplied by this route. This open request returns transformed external content, not the complete page (SRC-1, `server/ai_crawl.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Query-relevant extraction model text returned as MCP tool result.
- Later read-back: inapplicable — this implementation does not durably retain extracted pages or update a knowledge corpus.
- Delegated visibility: Model receives full crawler Markdown and query; calling executor receives only extraction text.
- Selection predicate: Caller supplies URL/query; model selects content; limiter admits at most configured recent call count per server instance.
- Invalidation or expiry: Rate timestamps expire over the configured interval; page/model messages are temporary.
- Activation or effect: Returning extraction is wired; truthful grounded answers and downstream reliance are unobserved.
- Evidence limits: Network/crawler/model behavior is external; prompt instructions establish requested extraction, not verified fidelity.

> "Given a user query and a webpage in Markdown, do NOT summarize the whole page. "
> "Instead, extract ONLY the content that directly answers or is highly relevant to the query. "
> --- `server/ai_crawl.py`

#### RT-RTE-case-admission
Label: Benchmark judgment and retained-case admission

Dataset question/reference → query record → LLM judge → results, case JSONL and (parametric driver) retrieved-case training pairs → reload for subsequent questions. Planner proposes the latest plan; judge decides answer correctness under semantic-match guidance; software assigns reward or positive/negative labels and writes both successful and unsuccessful plans. Dataset `ground_truth` supplies the expected-answer oracle, not the judge model alone. Mode is bounded benchmark evaluation with reference outcomes. Humans select inputs/configuration but do not approve each retained item. Missing/malformed judge output falls back to incorrect, not abstention. A failed retriever initializes to none; the runtime continues without retrieved examples. Case details are left to the memory member (SRC-1, `client/no_parametric_cbr.py`, `client/parametric_memory_cbr.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: QueryRecord plus logged/appended prediction, judge rationale and judgment.
- Later read-back: Reloaded case data are selected and delivered as user-role planning examples for later benchmark queries; training pairs may feed a separately launched trainer.
- Delegated visibility: Judge receives question, normalized reference-answer list and prediction, not the whole tool trace; planner/executor receive selected example text, not all retained cases.
- Selection predicate: Judge string correct determines label; every completed query can append a case; query matching in existing result records skips work at startup.
- Invalidation or expiry: Cases append without automatic expiry; files are externally editable; no transaction or automatic rollback joins result, training and case writes.
- Activation or effect: Durable case append, reload and prompt delivery are wired; activation of examples and improved capacity are unobserved.
- Evidence limits: Training labels copy whole-answer correctness to each retrieved case, not an identified causal contribution of that case; committed records are not verified generation traces.

> case_label = "positive" if is_correct else "negative"
> save_memory_entry(q, rec.plan_json or "", case_label)
>
> client._load_memory()
> --- `client/parametric_memory_cbr.py`

> "Focus on the positive examples and avoid the patterns shown in negative examples.\n\nYour plan:"
> --- `client/parametric_memory_cbr.py`

The improvement trigger is completion plus model judgment, not content-directed criticism of a particular planning rule. What persists is question/latest plan/label and retrieved-case pairs with outcome labels, rather than a codified explanation of why a plan failed. Model hidden processing cannot supply inspectable theory criticism. No theory-builder or successful self-improvement conclusion follows from this write route alone.

#### RT-RTE-retriever-training
Label: Standalone retriever parameter update and checkpoint selection

Operator-selected JSONL → dataset/tokenization → classifier optimization → validation metrics → local checkpoint → later CaseRetriever initialization. Computation proposes weight updates through gradients and chooses optional best checkpoint by AUC, falling back to F1; the caller chooses data, options and installation path. This is a bounded training/validation mode with supplied truth_label targets, whose driver provenance is answer-judge outcomes. CLI default plan inclusion is false (`--use_plan`), whereas inference pool construction includes a supplied plan; configuration alignment is therefore not guaranteed. The training objective is prediction of pair labels, not an independently identified marginal retrieval benefit. There is no automated query-driver scheduling or per-content human approval in the inspected program (SRC-1, `memory/train_memory_retriever.py`, `memory/parametric_memory.py`, `client/parametric_memory_cbr.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Saved last.pt and optionally best.pt, plus printed validation metrics.
- Later read-back: A later inference initialization loads configured weights; the query driver's case reload does not refresh the retriever checkpoint.
- Delegated visibility: Trainer receives pair text/labels, not original tool histories; inference receives numerical weights and case text.
- Selection predicate: Gradients optimize cross-entropy; save_best and strictly improved AUC/F1 select best checkpoint; final checkpoint always saves.
- Invalidation or expiry: Checkpoint files overwrite at output paths; no automatic rollback or atomic deployment gate is established.
- Activation or effect: Parameter-update and checkpoint-load mechanisms are wired; later live use and causal behavioral change are unobserved.
- Evidence limits: No tracked trained checkpoint or execution comparison; changed numerical parameters do not establish successful learning or exercised self-improvement.

> scaler.scale(loss).backward()
> --- `memory/train_memory_retriever.py`

> if args.save_best and score > best_metric:
>     best_metric = score
>     torch.save(model.state_dict(), best_path)
> --- `memory/train_memory_retriever.py:306-308`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-task-guidance
Label: Planner and executor guidance

Consumer: planner/executor models. Channel: system prompts, shared conversation and task request. Force: natural-language generation guidance, supplemented by symbolic client parsing, prefix checks and registered-session dispatch. Horizon: current query/task. Requested minimal plans and correct answers are not enforced semantic guarantees (SRC-1, `client/agent.py`; [RT-RTE-query-execution](#rt-rte-query-execution)).

> "When done, output a concise result. Do NOT output FINAL ANSWER."
> --- `client/agent.py`

#### RT-BAP-case-guidance
Label: Retained examples and retriever weights

Consumers: planner/executor and case-selection classifier respectively. Channels: selected case text in user-role history, and local checkpoint loading into numerical scoring. Force: examples request adoption/avoidance through model interpretation; weights determine ranking scores through numerical computation. Horizon: later benchmark questions and, for separately installed weights, later process starts. These are distinct authority channels; neither proves improved outcomes or that supplied examples changed a live decision (SRC-1, `client/parametric_memory_cbr.py`, `memory/parametric_memory.py`; [RT-RTE-case-admission](#rt-rte-case-admission), [RT-RTE-retriever-training](#rt-rte-retriever-training)).

> mem_prompt = build_prompt_from_cases(query, retrieved_cases) if retrieved_cases else ""
>
> if mem_prompt:
>     self._add_to_history("user", mem_prompt)
> --- `client/parametric_memory_cbr.py`

## Annotations

none
