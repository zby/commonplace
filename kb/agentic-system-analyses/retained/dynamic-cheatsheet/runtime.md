---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of Dynamic Cheatsheet: benchmark invocation, provider calls, state carry-forward, retrieval, execution and checkpoints"
run-id: AAS-2026-10-04-dynamic-cheatsheet-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet runtime report

## Runtime account

### Ordinary benchmark invocation

`run_benchmark.py` is the shipped entry point. It loads the configured prompt, constructs one `LanguageModel` from the requested provider/model name and optional reasoning-effort parameter, loads a supported task dataset, and iterates examples. The shipped defaults select `DynamicCheatsheet_Cumulative`, `openai/gpt-4o-mini`, one round, temperature zero, and local Python execution enabled. The API credentials, provider service and live model are external dependencies. The runner calls `advanced_generate` once per unseen example; it passes the current cheatsheet, prompts, dataset prefix, prior full outputs, optional precomputed embedding prefix, execution settings and approach-specific top-k. It appends returned `final_output`, stores the result object, and makes `final_cheatsheet` the next loop's state. The evaluator then checks the extracted answer for the task. [SRC-1: `run_benchmark.py`]

The cumulative route makes one generator call followed by a curator call per round. The generator receives the current cheatsheet and question as one user message. On later rounds it may also receive earlier answers from the same question. The curator receives the question, raw generator output and prior cheatsheet, and is asked by the shipped template to assess correctness and retain/refine reusable content. The extractor accepts text inside `<cheatsheet>`; missing tags return the previous sheet. `max_num_rounds` repeats generation and curation, with a minimum of one round, and the last generator answer and latest extracted sheet are returned. The implementation does not itself check answer correctness before curation. The template's direction to retain tested and proven material is model guidance, not a code-enforced admission test. [SRC-1: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `prompts/curator_prompt_for_dc_cumulative.txt`]

> cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py`

`DynamicCheatsheet_RetrievalSynthesis` creates a prompt from the current input embedding and prior embeddings, ranks cosine similarities, selects up to `retrieve_top_k` prior input/output pairs, and asks the curator to synthesize them with the previous cheatsheet. It then sends the result and current question to the generator. `Dynamic_Retrieval` uses the same selected examples without a curator synthesis call. `DynamicCheatsheet_CumulativeRetrieval` combines retrieved examples with the cumulative sheet for generation, then updates the cumulative sheet with a curator call. `FullHistoryAppending` places all previous inputs and full outputs into the prompt without curation. The default route sends an empty cheatsheet and performs a single generation. These are materially distinct context-selection paths; retrieval uses committed precomputed vectors paired to dataset inputs, not an embedding call shown in the inspected route. [SRC-1: `dynamic_cheatsheet/language_model.py`; `run_benchmark.py`]

> if original_input_embeddings is not None and len(original_input_embeddings) > 1:
> --- `dynamic_cheatsheet/language_model.py`

The runner writes the accumulated JSONL after each evaluated example and once more at completion. A continuation loads prior rows, takes the most recent `final_cheatsheet` when present, reconstructs previous outputs, skips indices below the prior output count, and writes to a `_continued.jsonl` path. Its consistency check compares only generator prompt path, temperature, Python-execution flag, task, model name, approach and round count. This is file-based recovery and caller-controlled carry-forward; no shared service or autonomous background updater is shown. The example notebook separately demonstrates caller-managed repeated calls. The later evaluator notebook reads saved JSONL as a consumer. [SRC-1: `run_benchmark.py`; `ExampleUsage.ipynb`; `EvaluatingResults.ipynb`]

> # Save the outputs to a file after each example (for crash recovery)
> --- `run_benchmark.py`

### Execution, control and limits

The selected provider is inferred from a configurable model-name prefix or explicit provider/model string. The `LanguageModel` constructs a `UnifiedLLMClient` and forwards prompts through provider-specific clients. One model selector is used for generator and curator calls; the source does not pin a provider-side immutable model revision. Model parameters do not change in the inspected code, but a mutable provider model alias may resolve to changed weights. The actual provider, model resolution, output, retry behavior during any particular run, and effects of the prompts are unobserved. [SRC-1: `dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py`]

Local code execution is a materially different path. When enabled, the model output must contain the configured execution flag after a closing code fence; the code block is written to a temporary file and launched with `python3`, with captured stdout/stderr and a three-second timeout. The host process is not shown to run in a sandbox. Recursion permits further model/code rounds up to the configured depth. When provider code interpreter mode is requested, local execution is disabled and generation uses a provider-native code-interpreter call; OpenAI setup creates a remote container, while Claude returns a native-tool sentinel. These execution environments and their isolation are outside the registered source boundary, so the deployed isolation envelope cannot be established. [SRC-1: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py`]

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
> --- `dynamic_cheatsheet/utils/execute_code.py`

The capability surface includes provider inference, optional Python execution, provider code-interpreter selection, benchmark file writes, and selection among six approaches. The runner's current grant set depends on its command-line arguments, environment credentials, host permissions and chosen provider; the source alone does not establish actual grants or approval controls. Code emitted by the model can invoke the local Python interpreter when the flag protocol matches. No separate human approval gate is visible in that path. The wrapper's timeout limits elapsed execution time but does not establish filesystem, network or process isolation. Provider-native tool permissions and isolation depend on external provider contracts not frozen here. [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py`]

No supplied execution traces or experiments were available. Therefore the member establishes implementation wiring and declared prompt guidance, not successful invocation, actual state retention, answer quality, activation, improvement, reliability or safety in operation. The source register excludes historical `results/`, so its results are not assessed. Dataset contents and embedding provenance were not analyzed; retrieval relevance and correctness are consequently unestablished. Inspected additional coverage beyond the boundary's initial anchors: `dynamic_cheatsheet/__init__.py`, `dynamic_cheatsheet/utils/__init__.py`, `dynamic_cheatsheet/utils/sonnet_eval.py`, `text_generation/__init__.py`, and all three prompt templates. The additional files are at the registered commit. [SRC-1]

## Shared records

### Components

#### RT-CMP-configured-model — Configured provider model

- Source-native identity: `LanguageModel` creates one configured model client and uses it for generation and curation calls.
- Representational form: distributed-parametric (provider model weights); prompt messages are natural-language inputs, not a separate parametric component.
- Storage substrate: provider-managed model service, outside the frozen repository boundary; exact provider-side storage and internals are uninspected.
- Parameters change during operation: no weight update is wired in the inspected implementation; this does not establish provider internals.
- Exact version pinned: no. The configurable model identifier, including the default `gpt-4o-mini`, is passed to the provider client without a frozen provider revision.
- Mutable endpoint may resolve to another model: yes or unknown by provider contract; actual resolution is unobserved.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py`; `run_benchmark.py`]

### Operative objects

#### RT-OBJ-cheatsheet — Caller-carried cheatsheet

- Source-native identity: `cheatsheet` / `final_cheatsheet`, plain text returned by the approach implementation and supplied to later calls.
- Representational form: natural-language text, interpreted by the model when inserted into a prompt.
- Storage substrate: Python string during the process; optionally serialized inside benchmark JSONL on the host filesystem.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `run_benchmark.py`]

#### RT-OBJ-retrieval-vectors — Precomputed retrieval vectors

- Source-native identity: per-task `embeddings/<task>.csv` rows loaded and reordered against the dataset inputs.
- Representational form: distributed-parametric dense vectors consumed numerically by cosine similarity; model provenance and generation process are not established by this boundary.
- Storage substrate: committed CSV vectors and in-memory NumPy arrays.
- Evidence: [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`]

### Routes

#### RT-RTE-benchmark-invocation — Benchmark question invocation

- Endpoints and progression: CLI arguments and task rows → runner → `LanguageModel.advanced_generate` → provider client → extractor/evaluator → JSONL output.
- Owner: benchmark runner owns iteration and evaluation; model owns generated content; host/provider execute calls.
- Context/state/action effects: task prompt plus current state and prior outputs form model messages; effects are returned answer/sheet and output-file writes.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: approach result includes generator output, extracted answer, steps and final cheatsheet.
- Later read-back: subsequent benchmark iterations receive the returned sheet and prior outputs; a resumed run reloads the last saved sheet when present.
- Delegated visibility: provider receives prompt messages and configured model parameters; host evaluator sees extracted answer and task target.
- Selection predicate: CLI-selected approach and current task index; each approach has its own context selection described above.
- Invalidation or expiry: no automatic expiry; state lasts in process and, when saved, until files are changed or a new run starts.
- Activation or effect: prompts place the sheet/examples in model context; behavioral effect is unobserved.
- Evidence limits: source code only; no provider trace, output or evaluated run supplied.
- Decision roles: runner selects route by `approach_name`; model generates answer and curator output; evaluator compares extracted answer with task target. No separate human route decision occurs within the loop.
- Operating mode: open-ended configured benchmark task sequence, with optional bounded `max_n_samples`; not evidence of an improvement experiment.
- Answer oracle: evaluator uses the dataset target and task-specific evaluator in the shipped benchmark; this is an evaluation reference, not an oracle supplied to model generation. [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/utils/evaluation.py`]
- Evidence: [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`]

#### RT-RTE-cumulative-update — Cumulative generation and curation

- Endpoints and progression: prior cheatsheet + current question → generator → raw output → curator prompt with prior sheet → tagged sheet extraction → caller state.
- Owner: code constructs prompts and extracts tagged text; provider model proposes both output and update; runner carries the result forward.
- Context/state/action effects: generator reads question and sheet; curator reads question, model answer and old sheet; extracted replacement updates the Python state.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: final answer and last extracted sheet; absent `<cheatsheet>` returns the prior sheet.
- Later read-back: runner supplies returned sheet on the next example, or from checkpoint on resume.
- Delegated visibility: provider sees current generator or curator message; curator's proposed sheet is consumed only if the expected tags parse.
- Selection predicate: cumulative approach is selected; all old content is subject to model output, and extraction takes the first `<cheatsheet>` block following the opening tag.
- Invalidation or expiry: no automatic expiry; curator may omit old content and replace it, while missing tags preserve it.
- Activation or effect: newly extracted text is supplied in later model prompts; changed behavior is unobserved.
- Evidence limits: no verification of curator correctness or successful future use in supplied traces.
- Trigger, proposed change, admission, rejection and recovery: each curator response proposes a text replacement; code admits any parseable tagged block without a correctness check or human veto; malformed/missing tags retain the old text; a parseable harmful change has no in-route rollback beyond restoring an earlier saved file or caller-supplied initial sheet.
- Guidance and persistence: cumulative curator prompt instructs accuracy checks, usefulness filtering, preservation, refinement and usage counts; this guidance is natural-language prompt text, not enforced policy. The resulting text persists through runner carry-forward/checkpoint or caller retention.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `prompts/curator_prompt_for_dc_cumulative.txt`; `run_benchmark.py`]

#### RT-RTE-retrieval-context — Retrieval context selection

- Endpoints and progression: current and prior precomputed vectors → cosine similarity ranking → selected prior input/output pairs → optional synthesis curator → generator context.
- Owner: Python code computes ranking and selects top-k; generator interprets selected text; synthesis model proposes a condensed sheet when that approach is chosen.
- Context/state/action effects: vector comparisons determine which prior examples are inserted; retrieval alone does not write the cumulative sheet, while retrieval-synthesis returns a synthesized prompt context.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: selected examples are exposed in result metadata; retrieval-synthesis returns its curated prompt context as `final_cheatsheet`.
- Later read-back: runner appends the current full output for later example retrieval; cumulative-retrieval separately returns a sheet that is passed forward.
- Delegated visibility: provider sees selected example text; it does not receive the numerical vector ranking inputs through the prompt.
- Selection predicate: descending cosine similarity of current vector against prior vectors, truncated to `retrieve_top_k`.
- Invalidation or expiry: selected examples are recomputed per question; no vector refresh or expiry mechanism is shown.
- Activation or effect: selected text is delivered in generation context; effect on answer is unobserved.
- Evidence limits: embeddings are precomputed and their provenance/content quality was not analyzed; no run traces show actual retrieval outcomes.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `run_benchmark.py`]

#### RT-RTE-full-history — Full history context assembly

- Endpoints and progression: prior dataset inputs and full generator outputs → Python concatenation → current generator prompt.
- Owner: runner accumulates outputs; approach formats all prior pairs; provider model consumes prompt.
- Context/state/action effects: prior input/output strings are appended as context; this approach does not curate or alter a separate cheatsheet.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: current answer/output and concatenated history as `final_cheatsheet`.
- Later read-back: next invocation reconstructs context from prior corpus and outputs; these outputs are also saved in JSONL.
- Delegated visibility: provider sees every included prior pair.
- Selection predicate: all entries in the prior corpus and generator output list are concatenated in input order; no similarity filtering.
- Invalidation or expiry: no per-example expiry; context grows with prior examples for the run.
- Activation or effect: history text is delivered; effect is unobserved.
- Evidence limits: no execution traces or token-limit outcomes supplied.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `run_benchmark.py`]

#### RT-RTE-local-code — Local model-triggered Python execution

- Endpoints and progression: model response containing code block plus execution flag → temporary `.py` file → host `python3` process → captured output appended to conversation → optional next model call.
- Owner: model proposes code; wrapper checks string/fence trigger and launches it; host process executes it; provider model receives captured text.
- Context/state/action effects: code can exercise the host process's available capabilities; stdout/stderr or timeout text is returned into model context.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: execution output is appended to the conversation; recursive generation continues within configured code rounds.
- Later read-back: execution output is available to the current invocation's subsequent model step; no separate persistent memory is wired by this executor.
- Delegated visibility: model sees captured result; code runs with host process permissions, whose deployment envelope is unknown.
- Selection predicate: `allow_code_execution` and exact flag occurrence with a response prefix ending in a code fence; extractor requires a Python fence.
- Invalidation or expiry: temporary script is removed after process completion or timeout; external side effects are not rolled back by this code.
- Activation or effect: the process is launched when predicate matches; no execution observed in this analysis.
- Evidence limits: host OS permissions, network access, subprocess descendants and effects are deployment-dependent; source comments identify sandboxing as an unresolved security concern.
- Trigger, proposed change, admission, rejection and recovery: model output proposes executable code; wrapper admits it on string/fence match without a human approval step; exceptions become text, timeouts kill the child, and script file is removed, but other side effects have no recovery path shown.
- Guidance and persistence: generator template requires Python-fenced code followed by `EXECUTE CODE!` and asks for validation; this instruction persists in the shipped prompt. Code and execution results persist only in the current interaction unless copied into a returned answer or cheatsheet.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py`; `prompts/generator_prompt.txt`]

#### RT-RTE-provider-interpreter — Provider code interpreter

- Endpoints and progression: caller requests interpreter mode → provider-specific session/tool route → provider execution and response → current invocation output.
- Owner: wrapper creates OpenAI container or enables Claude native code execution; external provider owns execution service and isolation.
- Context/state/action effects: provider receives messages and performs tool execution under external service behavior; local subprocess execution is disabled when this mode is selected.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: provider response is returned as generation output.
- Later read-back: tool result is present only in the current response/conversation; no separate durable code state is shown by DC.
- Delegated visibility: provider receives prompt and tool instructions; exact execution environment and logs are external.
- Selection predicate: `use_code_interpreter` plus a created/session sentinel container ID.
- Invalidation or expiry: remote session lifetime and tool-state cleanup are external and unspecified in the inspected target.
- Activation or effect: provider-native tool call is wired; its actual invocation and effect are unobserved.
- Evidence limits: provider implementation, isolation, approval and retention contracts are outside the frozen boundary.
- Trigger, proposed change, admission, rejection and recovery: model may request provider tool execution; DC wrapper selects provider path but does not implement an independent approval or rollback mechanism; external provider behavior is uninspected.
- Guidance and persistence: generator prompt supplies the code execution instruction; it remains a shipped template. Provider-side execution persistence cannot be established.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py`; `prompts/generator_prompt.txt`]

#### RT-RTE-checkpoint-resume — Checkpoint and resume

- Endpoints and progression: in-memory outputs/sheet → JSONL host file after each evaluated example → optional reload and continuation into a new output file.
- Owner: benchmark runner and host filesystem.
- Context/state/action effects: result rows and returned sheet are serialized; continuation restores sheet and previous outputs and skips already-counted dataset indices.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: write operation returns no analysis result; runner continues or ends with result file.
- Later read-back: continuation reads the last available `final_cheatsheet` and all saved outputs.
- Delegated visibility: host filesystem users/processes with applicable permissions can access saved prompts, outputs and state; actual permissions are unknown.
- Selection predicate: continuation path supplied and exists; resume compatibility checks selected argument subset.
- Invalidation or expiry: no automatic expiry or integrity check; user may choose another initial sheet or output path.
- Activation or effect: loaded sheet is supplied to later model calls; effect is unobserved.
- Evidence limits: no actual files from a run are supplied; runner code only establishes intended write/read flow.
- Trigger, proposed change, admission, rejection and recovery: each completed example is written for crash recovery; resumption admits prior JSONL state if its path/parameter checks pass. No content validation or rollback is implemented; recovery can use another prior file or explicit initialized sheet.
- Guidance and persistence: runner's checkpoint/resume code governs serialization and reload; no curator guidance is added here. Retention lasts as long as host files remain.
- Evidence: [SRC-1: `run_benchmark.py`]

#### RT-RTE-prompt-configuration — Prompt and run configuration

- Endpoints and progression: CLI arguments and prompt paths/environment → runner loads text and settings → model client and approach calls.
- Owner: operator supplies run configuration; runner loads and forwards it; model provider consumes the prompt.
- Context/state/action effects: configuration changes model selector, prompts, approach, execution mode, retrieval and run boundaries.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: settings determine invocation behavior and are serialized to a parameter JSON file.
- Later read-back: continuation reloads prior result state; supplied prompt paths/settings are not comprehensively restored from the params file by the inspected code.
- Delegated visibility: provider sees prompt content, model identifier and forwarded API parameters; host environment provides credentials.
- Selection predicate: parsed command-line values and file paths; approach must match supported approach list.
- Invalidation or expiry: applies to a run; new invocation can select different prompts, provider, capabilities or approach.
- Activation or effect: loaded prompt/config is used in model calls; effects are unobserved.
- Evidence limits: operator identity, approval process, file permissions and environment values are outside the source boundary.
- Trigger, proposed change, admission, rejection and recovery: operator proposes changes through argument values or prompt files; runner checks supported approach and provider prefix but performs no human approval; invalid values raise errors. Recovery is a new invocation with changed values or a prior saved state.
- Guidance and persistence: shipped generator and curator templates shape model proposals; configured values persist in the run parameter JSON, while prompt content is referenced by path rather than shown as copied into that file.
- Evidence: [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`; `prompts/generator_prompt.txt`; `prompts/curator_prompt_for_dc_cumulative.txt`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`]

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-local-python — Model-triggered host Python

- Consumer: model-generated code emitted during a generator call.
- Channel: output string containing execution flag and Python fenced code; wrapper launches a host subprocess.
- Force: code executes under the subprocess's inherited OS permissions; source does not show an approval gate or sandbox.
- Horizon: execution result returns to the current model conversation; external side effects may outlive the call.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py`]

#### RT-BAP-provider-tool — Provider-managed interpreter

- Consumer: provider model request routed through native code interpreter support.
- Channel: provider API tool/container mechanism.
- Force: provider service executes under its external tool contract; DC exposes no independent approval or isolation policy in inspected code.
- Horizon: response returns to current call; provider-side session retention is uninspected.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `text_generation/simple_unified_client.py`]

## Annotations

none
