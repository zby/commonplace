---
type: agentic-systems/types/agentic-system-runtime-report.md
description: "Runtime baseline of Dynamic Cheatsheet: benchmark invocation, state lifecycle, model and code execution routes"
run-id: AAS-2026-10-03-dynamic-cheatsheet-02
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet runtime report

## Runtime account

### Ordinary shipped invocation

The primary entry is `run_benchmark.py` (`SRC-1`, implementation). The caller parses task, approach, model, prompt, code-execution, resume and output options; reads generator and optional curator prompts; initializes `LanguageModel`; loads either the local task dataset or the named remote dataset; optionally reloads JSONL outputs and the last `final_cheatsheet`; and prepares input corpus and, for retrieval variants, checked-in embeddings. The default approach is `DynamicCheatsheet_Cumulative`, the default model name is `openai/gpt-4o-mini`, and the initial cheatsheet is `(empty)` unless a file or resumed run supplies it (`run_benchmark.py`). The runner shuffles with seed 10 unless disabled. Dataset ordering, prompts, embeddings and task targets are therefore caller-provided context, not state owned by the model client.

For each uncompleted example, the runner builds the task-specific question and calls `advanced_generate` with current cheatsheet, templates, previous generator outputs, input corpus and optional embeddings. In the cumulative route, the generator receives the current cheatsheet and question in a single user message. The client calls the selected provider, extracts an answer, then calls the model again with the question, raw generator output and prior cheatsheet to produce a replacement cheatsheet. The extractor returns prior text if no new cheatsheet is extracted. The runner appends the generator output to in-process history, adopts `final_cheatsheet`, evaluates the answer against the task target, appends an output object, and rewrites the JSONL output after each item. The output contains inputs, target, generator/answer fields, steps and final cheatsheet. The implementation explicitly assigns `cheatsheet = output_dict["final_cheatsheet"]`:

> cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py:280-280` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

On continuation, prior rows supply the generator output list and the last row's `final_cheatsheet`; iteration skips indices below the row count. A later run therefore consumes the accumulated text/history only through the runner. The core `LanguageModel` does not own durable memory. No supplied execution trace establishes that these paths were run in any particular deployment; implementation wiring is inspected, while operation, activation and benefit are unobserved. `run_benchmark.py` and `dynamic_cheatsheet/language_model.py` (`SRC-1`).

### Alternate and forcing paths

The approach switch materially changes what reaches the generator and what state is retained (`dynamic_cheatsheet/language_model.py`, `SRC-1`):

- `default` makes one generator call with `(empty)` and returns no cheatsheet.
- `FullHistoryAppending` constructs context from every prior input and generator output; there is no curation call, and that constructed context is returned as `final_cheatsheet` for the runner to persist.
- `Dynamic_Retrieval` selects top-k prior inputs and outputs by cosine similarity between the current and prior precomputed embeddings, places them in the generator prompt, and returns that context; the model does not create embeddings at runtime.
- `DynamicCheatsheet_RetrievalSynthesis` uses the same retrieved examples, calls a curator to synthesize context using the previous cheatsheet and next input, then calls the generator. The new synthesis is returned as the final cheatsheet.
- `DynamicCheatsheet_CumulativeRetrieval` appends retrieved examples to cumulative memory for generation, then uses the cumulative curator update route.
- `DynamicCheatsheet_Cumulative` can run multiple generator/curator rounds per question (`max_num_rounds`, at least one). Previous round answers can be added to the next generator context.

For all model paths, `model_name` chooses the provider prefix and model identifier. The adapter dispatches among OpenAI, Anthropic/Claude, Gemini and xAI, plus OpenAI-compatible Together, DeepSeek and Ollama endpoints (`dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py`). Provider calls and model internals are external. Parameters can vary by chosen model and endpoint; source does not pin an exact model revision or establish endpoint immutability.

Code execution is a separate forcing route. With `execute_python_code` enabled (default), ordinary generation output containing `EXECUTE CODE!` after a Python block triggers local extraction and execution through a `python3` subprocess. The process has a three-second timeout and no sandbox is implemented; the source itself has a TODO to improve sandboxing. It then appends execution output and asks the model to continue, up to the configured recursion depth. With `use_code_interpreter`, the runner creates a provider-side container or Claude native tool route, disables local subprocess execution, and sends generation through provider code execution. Cumulative curator calls explicitly disable local code execution. These are materially different effect boundaries; no guarantee about one route covers the other. The source states the subprocess path directly:

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
> --- `dynamic_cheatsheet/utils/execute_code.py:83-83` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The local subprocess is not isolated from the host by this code. The provider-side route delegates execution to the selected provider's service/container; its actual isolation contract is external and not inspected. Direct provider-native tools other than the wired code-interpreter path, arbitrary host callbacks, extension loading, remote worker orchestration, manual graph control and runtime delegation are not evidenced in the inspected target paths. This bounded inspection does not establish their general absence from dependencies or deployments.

### Memory changes and guarantees

The cumulative curator route admits changes to retained knowledge: each answered input triggers a model proposal based on the new input, generator output and prior cheatsheet; the extractor parses the proposal or falls back to the old text. The shipped curator prompt asks for verified and useful reusable content, preservation/refinement and deletion of redundancy, but that is model-facing guidance rather than a deterministic verifier. The generator answer is evaluated by task-specific code, but the evaluation result is not an input to curator admission. The runner replaces its current state with returned text and saves it in its result row; there is no separate approval, rollback or version history mechanism in the inspected loop. A prior output file can serve as a human-managed recovery copy, but no automatic rollback protocol is wired. `prompts/curator_prompt_for_dc_cumulative.txt`, `dynamic_cheatsheet/utils/extractor.py`, `run_benchmark.py` (`SRC-1` implementation; `SRC-2` design).

The retrieval synthesis route similarly admits an ephemeral, question-specific synthesized context from retrieved examples and prior memory; its result becomes the returned cheatsheet. Retrieved-only and full-history approaches construct context without curator acceptance. The material selection and admission behavior is described by implementation; no observed run proves what a provider returned or that delivered memory changed later behavior. The claimed success of prompt-directed checking does not establish correctness of retained entries. `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` and `dynamic_cheatsheet/language_model.py` (`SRC-1`, `SRC-2`).

No access-control, user approval, or deployment sandbox policy is imposed by the benchmark loop itself. Current grants, process permissions, environment and provider-side controls are deployment-dependent and unobserved. The inspected source establishes an affordance for local Python subprocess execution and an optional provider code-interpreter route, not the deployed isolation envelope. JSONL rewrite-after-each-example gives a recovery checkpoint in the ordinary loop, but interruption during file rewrite behavior and filesystem durability are not established as guarantees. Retry behavior belongs to the provider client and retries calls up to configured attempts; it does not establish successful or exactly-once model effects. `text_generation/simple_unified_client.py` and `run_benchmark.py` (`SRC-1`).

## Shared records

### Components

#### RT-CMP-1 — Selected inference model

- Source-native identity: model identifier selected by `model_name`, with provider dispatch by prefix through `LanguageModel` and `UnifiedLLMClient`.
- Representational form: distributed parametric model; opaque external provider implementation.
- Storage substrate: provider-controlled model parameters, inaccessible to this repository.
- Parameters change during operation: uninspected — provider-side update behavior is outside the boundary; the repository makes generation calls but does not inspect or update weights.
- Exact version pinned: no — configuration names a model identifier but code does not pin a provider revision or immutable artifact.
- Mutable endpoint can resolve to another model: yes/unknown — identifiers are sent to external provider endpoints and no immutable resolution is evidenced.
- Evidence: `dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py` (`SRC-1`).
- Identity comparison: no supplied records; distinct identity established by its external parametric-model role.

### Operative objects

#### RT-OBJ-1 — Cumulative cheatsheet text

- Source-native identity: `cheatsheet` / `final_cheatsheet`, a text string threaded by the benchmark runner.
- Representational form: explicit text.
- Storage substrate: process memory during a run; JSONL result file between runs.
- Evidence: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py` (`SRC-1`). The updater sets `cheatsheet = new_cheatsheet`:

> cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py:435-435` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

- Identity comparison: no supplied records; distinct identity established as the cumulative text state.

#### RT-OBJ-2 — Prior question/output corpus

- Source-native identity: `questions` / `original_input_corpus` paired in retrieval approaches with `generator_outputs_so_far`.
- Representational form: explicit input/output text plus supplied numeric embedding vectors.
- Storage substrate: benchmark process memory, initially reconstructed from datasets, checked-in CSV embeddings and previous JSONL outputs.
- Evidence: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py` (`SRC-1`).
- Identity comparison: no supplied records; distinct from RT-OBJ-1 because it is per-example history used for retrieval or full-history prompting.

### Routes

#### RT-RTE-1 — Cumulative generation, curation and persistence

- Endpoints and progression: question plus RT-OBJ-1 → generator model → answer extraction → curator model proposal → cheatsheet extraction/fallback → returned final state → runner JSONL write → later continuation read.
- Trigger and principal: each benchmark example; runner invokes the model client, which dispatches selected provider calls.
- Next-step owner and decision policy: Python orchestration determines call order and extracts/falls back to text; opaque model generation proposes answer and state. There is no independent approval decision.
- Context and state: current input, prompt templates, RT-OBJ-1; optional prior-round answers; curator receives raw generator output and previous cheatsheet.
- Action effects and boundary: provider inference; memory text replacement; runner filesystem write. Local code execution may be triggered during generator call only when enabled and marker protocol is met.
- Runtime-client controls: selected model, temperature, token limits, retry wrapper, max rounds, extraction and per-example file write. No deterministic correctness check gates memory admission.
- Persistence, coordination and return: runner holds state in process and stores returned row in JSONL; continuation reloads last `final_cheatsheet` and all prior `final_output` values.
- Recovery and terminal output: previous output file is a possible operator recovery source; automatic rollback is not wired. Returns answer, raw output, steps and updated cheatsheet; runner prints answer and running score.
- Admission fields: Trigger: completed generator result for each example. Proposed change: curator-generated full cheatsheet text. Admission: extractor accepts parsed new cheatsheet, otherwise retains old text; no human or deterministic content check. Rejection: parse fallback only; no explicit reject/approval action. Rollback/recovery: no route-level rollback; previous JSONL may be manually reused, while continuation reads the last row. Guidance: cumulative curator prompt instructs checking correctness, retaining useful prior content and refining/reducing redundancy; prompt persists as repository instruction, while accepted text persists in JSONL. `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `prompts/curator_prompt_for_dc_cumulative.txt` (`SRC-1`, `SRC-2`).
- Proposal and decision roles: the curator model proposes; Python extraction makes the effective acceptance decision; no human veto is wired. The task evaluator compares the final answer with a dataset target after the memory update, so that target is an answer oracle for scoring but not an oracle for memory admission. Operating mode is a bounded benchmark dataset run; improvement trigger is each processed example, not an observed improvement signal.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: no claimed guarantee
- Immediate return: answer, raw output, steps and final cheatsheet returned by `advanced_generate`; runner stores them in a JSONL row.
- Later read-back: last row's final cheatsheet and earlier final outputs are loaded by explicit continuation; no other reader is evidenced here.
- Delegated visibility: provider sees submitted prompt/context; the runner exposes prior state and answer to the curator; provider retention/visibility beyond request is uninspected.
- Selection predicate: every benchmark item is processed unless skipped by continuation index or stopped by sample limit; curator text parsing selects extracted content or old-state fallback.
- Invalidation or expiry: no TTL or automatic invalidation; a new curator replacement can omit prior material, and later resume reads the latest row only.
- Activation or effect: delivered in prompts by code; behavior change from retained text is unobserved.
- Evidence limits: source establishes wiring and prompt guidance only; provider responses, successful execution, memory correctness and benefit are unobserved.

#### RT-RTE-2 — Retrieved or full-history context construction

- Endpoints and progression: benchmark corpus/history and optional precomputed embeddings → selection/concatenation or synthesis → generator prompt → returned context (where applicable) → runner row.
- Trigger and principal: selected retrieval or full-history approach per item; deterministic Python constructs context, with opaque model synthesis only for retrieval-synthesis.
- Next-step owner and decision policy: cosine similarity and top-k ranking, or append-all ordering, choose examples; retrieval synthesis model proposes its textual context.
- Context and state: current question, earlier inputs and generator outputs; retrieval approaches additionally use repository-provided vectors.
- Action effects and boundary: prompt-context formation; retrieval-synthesis can return synthesized text as `final_cheatsheet`. No source in this repository generates embeddings during the loop.
- Runtime-client controls: `retrieve_top_k`, approach selection, and selected model; no answer validation controls retrieval inclusion.
- Persistence, coordination and return: runner keeps generator outputs and writes returned output rows; cumulative-retrieval also passes final cumulative text to RT-RTE-1 admission behavior.
- Recovery and terminal output: JSONL rows can be loaded through continuation; no separate retrieval-index update or rollback is wired.
- Admission fields (retrieval synthesis): Trigger: each item. Proposed change: synthesized context from selected prior examples, current question and prior cheatsheet. Admission: model output parsed by extractor, with fallback to prior context. Rejection: parse failure fallback only. Rollback/recovery: no rollback beyond reusing saved JSONL. Guidance: synthesis prompt asks for concise reusable strategy; prompt is shipped, while synthesis result is returned in the row. Other retrieval/full-history variants admit no model-curated knowledge revision beyond constructed context.
- Proposal and decision roles: similarity ranking / append ordering proposes selected examples computationally; no human confirmation or veto is wired. In synthesis mode, the model proposes text and Python extraction accepts it or falls back. The dataset target is used by the evaluator after generation as an answer oracle, not to select examples or accept memory. Operating mode is a bounded benchmark dataset run; each next item triggers selection, and synthesis mode additionally triggers curation.
- Evidence: `dynamic_cheatsheet/language_model.py`; `run_benchmark.py`; retrieval synthesis prompt (`SRC-1`, `SRC-2`).
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: no claimed guarantee
- Immediate return: selected example lists and generator output; synthesis variants also return synthesized context.
- Later read-back: generator outputs feed subsequent history; saved synthesis context is reused only when continuation loads its final cheatsheet.
- Delegated visibility: generator receives selected examples/context; retrieval curator sees selected pairs, next input and prior cheatsheet; external provider handling is uninspected.
- Selection predicate: top-k by cosine similarity among earlier precomputed vectors, or all prior pairs in full-history mode.
- Invalidation or expiry: examples expire from the current context when not selected; there is no corpus TTL. Synthesis text can replace its predecessor.
- Activation or effect: inclusion in generated prompt is wired; effect on answers is unobserved.
- Evidence limits: vectors are supplied artifacts and generation provenance is unavailable; no run trace supports ranking correctness or benefit.

#### RT-RTE-3 — Model-requested local subprocess execution

- Endpoints and progression: generator response containing Python fence and execution marker → extraction → temporary file → `python3` subprocess → captured output → appended conversation → further provider call.
- Trigger and principal: model output marker, gated by `allow_code_execution`; local extractor and Python process execute.
- Next-step owner and decision policy: model proposes code; literal marker plus code-block ending triggers execution; runner/client sets allow flag and recursion limit. No code approval step.
- Context and state: current generation conversation; code and stdout/stderr return to the model in the same call chain.
- Action effects and boundary: host subprocess with temporary script; timeout is three seconds. Source does not establish filesystem, network, privilege or process isolation.
- Runtime-client controls: enable flag, marker, timeout, recursion depth; these are not a sandbox.
- Persistence, coordination and return: output is appended to generation text and may be saved in benchmark JSONL; subprocess state is otherwise not retained by this code.
- Recovery and terminal output: timeout kills child; errors are returned as text; model may continue or final output returned.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: no claimed guarantee
- Immediate return: captured output, error, or timeout message is appended to model-visible text.
- Later read-back: result is available to later generation step in the same recursive call; no later benchmark invocation reads subprocess state.
- Delegated visibility: generated code executes locally; provider sees returned output on follow-up request.
- Selection predicate: exact marker and Python block trigger, when local execution is allowed.
- Invalidation or expiry: temporary file removed in `finally`; process ends after completion or timeout.
- Activation or effect: subprocess invocation is wired; actual execution and effects are unobserved.
- Evidence limits: implementation has no sandbox mechanism in inspected function and names security improvement as TODO; deployed OS controls and actual run are unobserved.
- Evidence: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py` (`SRC-1`).

#### RT-RTE-4 — Provider-side code interpreter

- Endpoints and progression: runner option → container creation for OpenAI or Claude native sentinel → provider request with code-execution tool → provider output returned to generator.
- Trigger and principal: explicit `use_code_interpreter`; provider client supplies tool configuration. `advanced_generate` disables local subprocess execution on this option.
- Next-step owner and decision policy: model/provider tool runtime controls tool calls; local code does not inspect code or intermediate execution beyond returned text.
- Context and state: request messages; OpenAI uses a persistent container ID for the benchmark run; Claude code execution is configured per request.
- Action effects and boundary: provider-side tool execution; provider isolation and persistence semantics are external and uninspected.
- Runtime-client controls: selected provider, container option, max output tokens and request parameters. OpenAI container path rejects non-OpenAI providers; Claude path uses native execution.
- Persistence, coordination and return: container identifier is held by client for current run; returned text enters output and can be saved in JSONL.
- Recovery and terminal output: provider request retry is wired; container rollback and recovery are uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Guarantee strength: no claimed guarantee
- Immediate return: provider-produced text is returned to generation; execution details may not be represented in text.
- Later read-back: provider execution context may persist within the run for OpenAI container; exact retained state and later visibility are uninspected.
- Delegated visibility: request messages and tool interaction are delegated to provider; service-side retention is uninspected.
- Selection predicate: explicit option and supported provider route; ordinary marker-based local execution is disabled.
- Invalidation or expiry: provider container lifecycle/expiry is uninspected; Claude tool is per-request by adapter design.
- Activation or effect: tool wiring is inspected; tool invocation and output effect are unobserved.
- Evidence limits: no service trace, execution artifact or provider isolation contract is supplied.
- Evidence: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py` (`SRC-1`).

### Claims

#### RT-CLM-1 — Curator quality guidance

- Claim: curator instructions direct inclusion of tested/proven strategies and correctness assessment; these are prompt claims, not verified runtime guarantees.
- Evidence: `prompts/curator_prompt_for_dc_cumulative.txt` (`SRC-2`).
- Identity comparison: no supplied records; distinct as declared prompt guidance.

> Only include solutions and strategies that have been tested and proven effective.
> --- `prompts/curator_prompt_for_dc_cumulative.txt:24-24` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-1 — Generated local Python process

- Consumer: local Python interpreter launched by `execute_code_with_timeout`.
- Channel: Python source extracted from model output that ends in the configured execution marker; temporary script passed to `python3`.
- Force: executable process instructions run with the benchmark process user's available OS permissions; code does not impose a sandbox.
- Horizon: one subprocess invocation, capped by the three-second timeout; any external side effects may outlast it.
- Evidence: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py` (`SRC-1`).

#### RT-BAP-2 — Provider code-interpreter tool

- Consumer: selected provider's code-execution service/tool.
- Channel: provider API tool configuration and model-directed tool execution.
- Force: provider-side computation under external service controls, not inspectable in this repository.
- Horizon: request or provider container lifecycle; exact retention and side-effect horizon uninspected.
- Evidence: `text_generation/simple_unified_client.py` (`SRC-1`).

## Annotations

none
