---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Dynamic Cheatsheet runtime baseline tracing generation, curation, retrieval, execution and benchmark continuation at the frozen source revision."
run-id: AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet runtime report

## Runtime account

Dynamic Cheatsheet performs sequential problem solving with model-interpreted reference text. Its consequential change mechanism is replacement of that reference text, not an inspected weight-training loop. The generator and curator are two invocations of the same configured `LanguageModel`, not separately configured agents. Python decides their order, substitutes templates, extracts outputs and carries state; the remote model interprets the problem and proposes reference content. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py` and `prompts/generator_prompt.txt`; see [RT-CMP-language-model](#rt-cmp-language-model), [RT-RTE-cumulative-curation](#rt-rte-cumulative-curation) and [RT-BAP-cheatsheet-context](#rt-bap-cheatsheet-context).

### Ordinary shipped invocation

The shipped CLI parses `Arguments`, checks the approach name, reads caller-selected generator and curator files, loads credentials from the environment/config file, initializes the provider wrapper and loads a task. Default settings select cumulative curation, `openai/gpt-4o-mini`, one refinement round and local Python execution. A meaningful cumulative invocation must supply the curator prompt path: the CLI otherwise passes the literal `(empty)` as its curator template, so passing the approach check alone does not establish an operative curation instruction. The README's benchmark example supplies both shipped prompt files. The interactive `ExampleUsage.ipynb` likewise loads both files and passes each returned cheatsheet into a subsequent call on the same puzzle. SRC-1, `run_benchmark.py`, `README.md`, `ExampleUsage.ipynb`.

For a fresh cumulative benchmark, the driver starts with `(empty)` or an initialization file, shuffles the dataset with seed 10 unless disabled, adds task-specific question/answer-format instructions and calls `advanced_generate`. Each round constructs one user message with the current question and cheatsheet. The generator requests a provider response, optionally executes code and asks the model to continue, then extracts an answer. The curator receives the question, full generated response and previous cheatsheet, but not the dataset target or subsequent score. It proposes an entire replacement cheatsheet. Extraction admits the proposal immediately; the next round or next question can receive it. Additional cumulative rounds can append the previous extracted answers to generator context. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`; [RT-RTE-cumulative-curation](#rt-rte-cumulative-curation).

The library returns a dictionary containing steps, answer, full output and final cheatsheet. It does not itself persist that dictionary to disk. The driver appends the output and target to its list, appends full generated output to the retrieval/history corpus, assigns the returned cheatsheet, prints state and scores the answer. Only then does it rewrite JSONL. After the loop it writes once more and prints accuracy over newly processed examples. The driver is the next-step owner and disk persister; there is no parallel worker coordination in this loop. The terminal product is both the answer/checkpoint and the evolving reference state. SRC-1, `run_benchmark.py`; [RT-RTE-checkpoint-continuation](#rt-rte-checkpoint-continuation), [RT-RTE-answer-scoring](#rt-rte-answer-scoring).

### Material alternate approaches

The six branches change the delivered context and timing of admission, not just the name of the same operation (SRC-1, `dynamic_cheatsheet/language_model.py`):

| Approach | Context and next-step policy | Returned reference state |
|---|---|---|
| `default` | One generator invocation with `(empty)` reference; optional execution continuation still applies. | `None`; no curator. |
| `DynamicCheatsheet_Cumulative` | Generator then curator, repeated `max(1, max_num_rounds)` times. | Extracted replacement or previous cheatsheet. |
| `Dynamic_Retrieval` | Cosine top-k previous question vectors; corresponding previous full responses delivered directly. | Assembled selected examples. |
| `DynamicCheatsheet_RetrievalSynthesis` | Retrieve first; curator receives selected pairs, prior cheatsheet and next question before generator. | Synthesized reference, or retrieved text on extraction fallback. |
| `DynamicCheatsheet_CumulativeRetrieval` | Combine cumulative text with retrieved examples; generator then cumulative curator. This branch does not iterate `max_num_rounds`. | Replacement cumulative text, not the combined retrieval section. |
| `FullHistoryAppending` | All available earlier question/output pairs, zipped in corpus order; no embeddings or curator. | Assembled history text. |

Retrieval selects on original question embeddings, not correctness or generated-answer similarity. The driver aligns CSV vectors to dataset input strings and supplies prefixes ending with the current question; the library treats the last vector as current and earlier vectors as candidates. Prior full responses can include code and local execution output. Thus retrieval is not restricted to validated final answers. The hybrid curator receives its generated response and old cumulative text, not a separate retrieved-example placeholder. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`; [RT-CMP-input-embeddings](#rt-cmp-input-embeddings), [RT-RTE-context-selection](#rt-rte-context-selection).

### Forcing cases and guarantee scope

Four source-inspected cases challenge tempting system-wide guarantees. These are branch traces, not target executions.

1. **No closing cheatsheet tag.** `extract_cheatsheet` checks for the opening tag, then splits at the closing tag without requiring it. A response with an opening tag but no closing tag can replace the old reference with its remaining text. Missing an opening tag returns the old reference. This is a delimiter policy, not validation of correctness, item structure or preservation. [RT-RTE-cumulative-curation](#rt-rte-cumulative-curation).
2. **Last permitted local round still requests execution.** Local code is executed before the depth test. With default initial depth 1 and maximum 3, a flagged output at depth 4 can still execute; the stopping branch also appends the current output again after it has already entered `final_output`. The last-round warning is model guidance, not enforcement of three executions. [RT-RTE-local-execution](#rt-rte-local-execution).
3. **Native execution enabled while local execution is disabled.** The native branch is tested before the local flag, and uses provider tools when `use_code_interpreter` and a container/sentinel are present. Consequently `allow_code_execution=False` is not a universal execution veto. Conversely, `advanced_generate(use_code_interpreter=True)` disables local execution even without a container, in which case ordinary generation occurs without the requested native branch. [RT-RTE-native-execution](#rt-rte-native-execution).
4. **Scoring still evaluates Python after generation tools are disabled.** Game of 24 scoring invokes Python `eval` on normalized model answer text before digit validation. The generator execution flag does not cover this host evaluation route. This matters even though scoring is not an improvement/admission oracle. [RT-RTE-answer-scoring](#rt-rte-answer-scoring).

Guarantee owners and enforcement differ. The wrapper's disabling of local execution in native mode is an **invariant** of `advanced_generate`'s parameter assignment, covered on that entry path only; direct `generate` and evaluation are alternate paths. The local executor's three-second `communicate` timeout and direct-child kill are **best effort**, not process-tree containment or an isolation envelope. The native client installs a provider tool declaration, a **protocol** whose execution/isolation semantics require external provider contracts not frozen here. The driver's continuation argument comparisons and positional restart are a **protocol**, not exact replay or atomic crash recovery. These guarantees have implementation conclusion status: wired, operation conclusion status: uninspected. Accuracy and preservation instructions have guarantee strength: policy, implementation conclusion status: claimed, operation conclusion status: uninspected. Their owner is the prompt author and enforcement is requested model compliance, not a separate executable gate. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`, `text_generation/simple_unified_client.py`, `run_benchmark.py`, `prompts/curator_prompt_for_dc_cumulative.txt`.

Capability, grant and deployment must remain separate. The local capability is model-written Python under the process user's inherited environment, not merely arithmetic. The shipped CLI grants that capability by default; actual deployed credentials, filesystem permissions, networking and enclosing isolation are uninspected. The inspected source uses a temporary script and ordinary `Popen`, with no approval request on this path. Provider-native tools are separately requested and have opaque remote effects. OpenAI/Claude additional API parameters can also supply or override provider parameters: inspected parameter merges do not make the local flag a provider-tool allowlist. `generate_from_messages` disables its explicit web-search switch, but a search-preview model can search natively, and direct client convenience APIs are another capability surface not exercised by the benchmark account. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`, `text_generation/simple_unified_client.py`.

### Evidence and coverage limits

All account findings use SRC-1 at the frozen revision. This member additionally inspected notebook source cells, the provider's initialization, xAI message dispatch, OpenAI sampling/parameter handling and native-tool methods, plus all active scoring implementations. These add implementation coverage, not new sources. No saved notebook output, complete result trace, benchmark run or causal experiment was inspected here. Source comments announcing correct answers in `ExampleUsage.ipynb` are not independent outcome evidence. Present provider compatibility, execution benefit, model compliance and learned improvement remain unobserved. CSV generation provenance and exact model weights remain uninspected. Auxiliary sonnet scoring and direct client chat/search convenience loops are not characterized beyond their relationship to the active message entry point. SRC-1, `ExampleUsage.ipynb`, `EvaluatingResults.ipynb`, `text_generation/simple_unified_client.py`; boundary evidence limits remain in force.

## Shared records

### Components

#### RT-CMP-language-model
Label: LanguageModel generator and curator backend

Source-native identity: `LanguageModel.client`, configured once and called for generator and curator roles. Representational form: distributed-parametric model computation, fed natural-language messages. Storage substrate: provider-managed weights/runtime or an OpenAI-compatible endpoint; the local wrapper stores model/provider strings and client configuration. SRC-1, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

> self.extra_api_params = extra_api_params or {}
> self.container_id = container_id
> self.client = UnifiedLLMClient(**client_kwargs)
> --- `dynamic_cheatsheet/language_model.py`

Parameters changing during operation: no weight update is issued by the inspected wrapper/driver routes; provider internal mutation is uninspected. Exact version pinned: not enforced; callers may choose dated names or mutable aliases, and CLI defaults use an alias. Mutable endpoint can resolve to another model: yes, the source delegates identity resolution to the selected provider/compatible endpoint without checking weight identity. No conclusion about remote training or actual alias changes follows. Generator and curator share the same configured component, while their context and maximum tokens differ.

#### RT-CMP-input-embeddings
Label: Precomputed original input embeddings

Source-native identity: `original_input_embeddings`, from task CSV `embedding` cells. Representational form: distributed-parametric dense numerical vectors consumed by cosine similarity. Storage substrate: CSV on disk, parsed into a NumPy array and reordered in memory. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`.

> embeddings = df["embedding"].apply(ast.literal_eval)
> embeddings = np.array(embeddings.tolist())  # (N, embedding_dim)
> --- `run_benchmark.py`

Parameters changing during operation: the inspected driver reorders and slices vectors but does not train or recompute them. Exact producing model version pinned: uninspected; this path does not identify it. Mutable endpoint can resolve to another model: inapplicable to the loaded vectors themselves; their original production endpoint is uninspected. No embedding quality or input-provenance conclusion is reached.

### Operative objects

#### RT-OBJ-generator-prompt
Label: Generator template

Source-native identity: `prompts/generator_prompt.txt`, with a caller-selectable path in the driver. Representational form: natural-language problem-solving, reference-use, execution and final-answer instructions; literal placeholders are substituted symbolically before interpretation. Storage substrate: tracked text file, in-memory string and returned step prompt. Consumer: generator model as one user message, not privileged system policy. SRC-1, `prompts/generator_prompt.txt`, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`.

> - Carefully analyze both the question and cheatsheet before starting
> - Search for and identify any applicable patterns, strategies, or examples within the cheatsheet
> --- `prompts/generator_prompt.txt`

This establishes requested reference use, not activation. Curator prompts are guidance for admission discussed in the route records, not aliases for this generator object.

#### RT-OBJ-output-dict
Label: Advanced generation result and driver checkpoint

Source-native identity: `output_dict` returned by `advanced_generate`, expanded into the driver's `outputs` list. Representational form: symbolic dictionary/JSON envelope with separately interpreted natural-language prompts, outputs and reference strings. Storage substrate: Python list/dictionaries and JSONL disk file. It contains diagnostic steps as well as later-consumed final outputs and cheatsheets; persistence alone does not establish learning. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

> outputs.append({
>     "input": current_input,
>     "target": original_target,
>     "raw_input": original_input,
>     **output_dict,
> })
> --- `run_benchmark.py`

The target is checkpoint/evaluator material. It is not passed as a curator oracle by this driver.

### Routes

#### RT-RTE-cumulative-curation
Label: Cumulative generation and reference replacement

Endpoints and progression: caller question/current cheatsheet → generator → answer extraction → curator → cheatsheet extraction → next round/caller. Owner: Python wrapper schedules; model supplies answer and candidate replacement. Context/state/action effects: curator sees full generated output including any execution continuation, question and old cheatsheet. Admission installs extracted text as reference state. Same mechanism serves cumulative and the hybrid post-answer update, but only cumulative iterates refinement rounds. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `prompts/curator_prompt_for_dc_cumulative.txt`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer, full output, step records, previous answers and final replacement reference; hybrid also returns retrieved examples.
- Later read-back: Next cumulative round receives the replacement; the driver or notebook passes returned reference into a later question/invocation.
- Delegated visibility: Generator gets question/reference; curator gets question/full response/previous reference. Dataset target and score are not supplied to curator.
- Selection predicate: Whole prior reference is supplied; prompt requests relevant reusable content and preservation, with model selection rather than an item-level software selector.
- Invalidation or expiry: Whole extracted replacement supersedes previous live text; omitted material is not automatically recovered from the prior version.
- Activation or effect: Replacement and subsequent delivery are wired; content-dependent change to model behavior is uninspected.
- Evidence limits: No trace demonstrating preservation, criticism, correctness or improvement was inspected; opening-tag extraction does not enforce closing tags or semantic validity.

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
> cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py`

> txt = response.split("<cheatsheet>")[1].strip()
> txt = txt.split("</cheatsheet>")[0].strip()
> return txt
> --- `dynamic_cheatsheet/utils/extractor.py`

Admission roles/mode: bounded benchmark sequence or caller-supplied open problems. The model proposes the replacement; delimiter extraction decides admission. There is no per-content human approval on this route. Caller can supply/edit the initial reference or prompt files and choose future invocations; actual human authorship of a supplied file is unresolved. Rejection ability: missing opening tag or extraction exception preserves the old reference, but no accuracy veto is wired. Recovery: old reference remains in step records/checkpoints, permitting external manual recovery, not automatic rollback of a bad extracted replacement. Trigger/objective: after an answer, consolidate reusable strategies for future problem solving. Guidance requests correctness assessment, preservation, refinement, examples and usage counts; only extracted reference text persists as live guidance, not necessarily the curator's entire rationale.

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

Answer oracle: none supplied to this admission route; model judgment is not a reference answer. Improvement trigger is every generated answer, not a low score.

Theory scope: the prompt requests reusable strategies, including rules and scope/limitations, which could formulate theories. No particular generated theory or criticism was inspected. Applied guidance is the static curator method and existing reference; the model is asked to refine the latter, not rewrite the curation method itself. Theory-builder conditions 1–4: condition 1 conclusion status: claimed (localized strategies requested); condition 2 conclusion status: claimed (use requested, dependence unobserved); condition 3 conclusion status: uninspected (specific challenged claim, blame and consequent revision unobserved); condition 4 conclusion status: uninspected (reference iteration wired, but preservation and later use of a criticism result unobserved). Addressability: entire text is replaceable and visible to the model; prompt tags request finer items but the extractor enforces no item structure. Persistence: library rounds and caller-driven later problems; driver checkpoints can extend across resumed runs. Learning: improved future capacity is claimed by README, not established here. Reflection: prior answer/reference can shape a successor reference that is delivered to future solving; actual representation-mediated behavioral effects are unobserved. Reflective theory builder: method-text criticism is uninspected. Autonomous theory builder: computational scheduling/proposal/admission are wired, but performance of every theory-builder operation is not established.

#### RT-RTE-context-selection
Label: Retrieval, synthesis and full-history context construction

Endpoints and progression: caller-supplied previous inputs/outputs and vectors → deterministic selection/assembly → optional curator synthesis → generator. Owner: wrapper for ordering and cosine ranking; model for synthesis. Direct retrieval bypasses curator; full-history uses zipped earlier pairs without ranking; hybrid appends selected examples to cumulative reference then follows cumulative admission. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Generated answer/output, selected input/output lists and assembled or synthesized final reference.
- Later read-back: Driver accumulates previous full outputs for later selection; synthesis also receives the prior final reference through the driver's carry-forward.
- Delegated visibility: Direct generator sees selected pairs; synthesis curator sees selected pairs, prior reference and next question; generator sees extracted synthesis rather than necessarily all retrieved pairs.
- Selection predicate: Descending cosine similarity between current and prior question vectors, sliced by retrieve_top_k; full-history instead includes the supplied zipped prefix.
- Invalidation or expiry: New per-query assembled/synthesized context replaces prior live selection; no time-based expiry in these inspected branches.
- Activation or effect: Ranking/assembly/template delivery wired; successful use or benefit uninspected.
- Evidence limits: Vector provenance, payload quality, caller alignment outside the driver and content-dependent model behavior remain uninspected; correctness is not a selector input.

> similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
> top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
> --- `dynamic_cheatsheet/language_model.py`

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=curated_cheatsheet)
> curated_cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py`

Admission roles/mode: synthesis model proposes reference suited to next question; extraction admits it without human content approval or expected-answer oracle. Software decides retrieved candidates by score, not the model. This is a bounded benchmark/caller problem sequence, not a candidate-performance experiment. Trigger: incoming question; proposed change: a customized reference; rejection/recovery: extraction fallback returns assembled retrieved pairs rather than necessarily the previous cheatsheet. Guidance asks for useful, generalized strategies and replacement of inferior methods. It persists only insofar as the extracted text survives later synthesis/carry-forward.

> - If a better approach than a previously recorded one is found, replace the old version.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`

Theory-builder conditions 1–4 for synthesis: condition 1 conclusion status: claimed (localized heuristics requested); condition 2 conclusion status: claimed (intended solving use); condition 3 conclusion status: uninspected (no specific content-directed criticism observed); condition 4 conclusion status: uninspected (no criticism-result iteration observed). Addressability: whole reference replaceable, finer item structure requested not checked. Persistence: selected/synthesized reference lives through return and driver carry-forward; previous input/output corpus reaches later benchmark questions and resumed runs. Learning and reflection: delivery and update capacity do not establish improved capacity or actual behavioral dependence. Reflective and autonomous theory-builder operation remain uninspected. Direct retrieval and full-history assembly formulate no new theory in software; whatever theories their text contains are uninspected.

#### RT-RTE-local-execution
Label: Flag-triggered local Python continuation

Endpoints/progression: provider response → execution-flag and fence check → first Python fence extraction/last-line print adjustment → temporary script → `python3` subprocess → output appended as assistant content plus user continuation request → another provider call. Owner: wrapper controls continuation; model chooses code and whether to request it. Effect boundary: host-process permissions/environment, not an inspected sandbox. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted stdout/error/timeout text incorporated into accumulated generated output.
- Later read-back: Driver can later retrieve or curate full output including executed code/results; temporary script is removed rather than retained as a tool artifact.
- Delegated visibility: Subsequent model call sees augmented conversation; curator can receive full generated response, not a separately typed execution result.
- Selection predicate: Local allow flag, execution marker in output, pre-marker text ending with a fence; extraction chooses the first Python fence, not necessarily the last block before the marker.
- Invalidation or expiry: Temporary file removed in finally; conversation retained for recursive continuation and output accumulation.
- Activation or effect: Host subprocess dispatch wired; actual code effects, descendant behavior and successful continuation uninspected.
- Evidence limits: Timeout is direct-child control only; no demonstrated isolation or process-tree cleanup. Depth warning does not prevent execution before the depth check.

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
> stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py`

> except TimeoutExpired:
>     process.kill()
>     captured_output = "Execution took too long, aborting..."
> --- `dynamic_cheatsheet/utils/execute_code.py`

> if current_depth <= max_depth_num_rounds:
> --- `dynamic_cheatsheet/language_model.py`

The marker grants local execution, not a reviewed capability installation. The formatting and self-contained-code constraints are model-facing policy; the executor performs no content approval. Failure text is fed back for model recovery. There is no automatic rollback of host side effects. Curator calls set local execution false, but that does not constrain generation/scoring elsewhere.

#### RT-RTE-native-execution
Label: Provider-native code interpreter dispatch

Endpoints/progression: caller/driver enables native mode → OpenAI container creation or Claude `native` sentinel → native generation method → provider service execution → returned text. Owner: wrapper grants/request dispatch, provider owns inner execution and next steps. SRC-1, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: OpenAI output_text or concatenated Claude text blocks; not a complete independently structured execution trace.
- Later read-back: Returned full text may enter driver corpus and curator; OpenAI container ID is reused within the benchmark, but not saved as resume state by the driver.
- Delegated visibility: Provider receives conversation/tool request; remote filesystem, tool internals and nontext response details are uninspected or omitted from returned text.
- Selection predicate: generate uses native path only when both use_code_interpreter and container_id are truthy; Claude/Anthropic prefixes select Claude tool path, others select guarded OpenAI method.
- Invalidation or expiry: No explicit container deletion/expiry enforcement in inspected wrapper/driver; external lifecycle uninspected. Restart creates a new session rather than restoring saved container state.
- Activation or effect: Tool declaration wired; actual provider execution and isolation uninspected. Local execution is disabled by advanced_generate in native mode.
- Evidence limits: Remote services/SDK versions not frozen; local depth/timeout controls do not cover this branch, and caller extra parameters can affect provider request fields.

> if use_code_interpreter:
>     allow_code_execution = False
> --- `dynamic_cheatsheet/language_model.py`

> "tools": [{"type": "code_interpreter", "container": container_id}],
> --- `text_generation/simple_unified_client.py`

> code_execution_tool = {"type": "code_execution_20250825", "name": "code_execution"}
> --- `text_generation/simple_unified_client.py`

The wrapper's native early return bypasses local code parsing entirely. OpenAI Responses and Claude messages requests use client retries; on failure a request can be repeated, with external idempotency/side-effect semantics uninspected. No source-level human approval is inserted on this active route. This is an execution grant rather than admission of retained reference content.

#### RT-RTE-checkpoint-continuation
Label: Benchmark checkpoint write and positional restart

Endpoints/progression: generated dictionary → driver lists/live cheatsheet → scoring → JSONL rewrite; later driver invocation loads JSONL and companion parameters → checks selected argument equality → restores last cheatsheet and output history → skips first len(outputs) examples. Owner: driver; symbolic JSON parsing and index count choose restart position. SRC-1, `run_benchmark.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full outputs list written to disk and printed progress/summary; no separate durable transaction result.
- Later read-back: Last final_cheatsheet and every final_output are reloaded for subsequent generation/retrieval/history calls.
- Delegated visibility: New provider invocation gets rebuilt prompt context, not the complete checkpoint or its stored targets by default.
- Selection predicate: Resume path supplied by caller; final reference from last loaded row; start index equals row count.
- Invalidation or expiry: Writes truncate/rewrite the selected output file; continued run uses a new continued filename. No artifact expiry enforcement inspected.
- Activation or effect: Disk write and reconstructed context delivery wired; exact reproducibility and successful crash recovery uninspected.
- Evidence limits: Save is after scoring and is not atomic; truncated/empty JSONL, changed dataset order/content and unchecked prompt/model-service changes can defeat recovery assumptions.

> with open(file_path, "w") as file:
>     for line in data:
>         file.write(json.dumps(line) + "\n")
> --- `run_benchmark.py`

> args_keys = ["generator_prompt_path", "temperature", "execute_python_code", "task", "model_name", "approach_name", "max_num_rounds"]
> --- `run_benchmark.py`

> generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py`

Those equality checks omit, among other inputs, curator path/content, no_shuffle, retrieval k, max_tokens and native-mode configuration. They compare a generator path, not its bytes. Fixed shuffle seed supports repeatable ordering only under unchanged data/shuffle settings. Caller chooses initialization/restart files; that path selection is not per-entry human approval. No semantic rejection or automatic rollback of an admitted cheatsheet occurs on save/reload. Retained steps can assist manual inspection, not guaranteed restoration.

#### RT-RTE-answer-scoring
Label: Online and retained-output answer evaluation

Endpoints/progression: extracted final answer and dataset target/raw input → task-specific scorer → boolean/count/print; notebook separately reads retained step output and performs its own answer normalization before scoring. Owner: driver/notebook and deterministic utility functions. Mode: bounded task benchmark; dataset expected answers are an oracle for scoring, not reference admission. SRC-1, `run_benchmark.py`, `EvaluatingResults.ipynb`, `dynamic_cheatsheet/utils/evaluation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Task boolean and aggregate counters/printed accuracy; driver JSONL preserves target and output but does not append the score as a decision field.
- Later read-back: Notebook reads saved output/target for post-hoc scoring; scoring result is not fed to next curator invocation.
- Delegated visibility: Evaluator sees reference targets; generator/curator do not receive them through this scoring path.
- Selection predicate: Task name dispatch; online answer comes from extract_answer, notebook from final step text with different tag/boxed-answer handling.
- Invalidation or expiry: Counters restart on continuation and summarize newly processed examples; retained files can be rescored under notebook normalization.
- Activation or effect: Scoring/printing wired; Game of 24 and equation evaluation invoke host eval, independent of generator tool flags.
- Evidence limits: No run reproduced; online/offline normalization differences prevent assuming identical measured accuracy. Evaluator acceptance is not proof of safe execution or semantically valid curation.

> value = eval(clean_output)
> --- `dynamic_cheatsheet/utils/evaluation.py`

> output_value = eval(output)
> if abs(output_value - eval(target_val)) < 1e-6:
> --- `dynamic_cheatsheet/utils/evaluation.py`

Game of 24 evaluates normalized model expression before checking number use, exposing a separate host effect boundary without the subprocess timeout. Equation scoring performs a string-number-format check first, then evaluates output and target value. Multiple-choice and exact-match paths use normalization/string tests. Scorers determine reported correctness, not whether reference updates survive: admission and live reference assignment have already happened. No score-driven improvement trigger or veto is wired in this driver.

### Claims

#### RT-CLM-adaptive-memory
Label: Adaptive memory without parameter modification

Claimed operation: reusable strategies improve future problem solving through inference-time memory rather than weight changes. SRC-1, `README.md` supplies doctrine/design and reported performance, not an independently reproduced causal result.

> Dynamic Cheatsheet (DC) endows black-box language models with the ability to store and reuse insights across queries. Rather than repeatedly re-discovering solutions or making the same mistakes, DC enables models to accumulate and leverage strategies, code snippets, and problem-solving techniques without modifying the underlying model parameters.
> --- `README.md`

Implementation supports reference replacement/carry-forward and avoids explicit training in the inspected routes. Exercised learning and benefit remain uninspected. For the claimed improvement-directed self-change pathway, boundary is the generator/curator/driver reference loop; horizon is later benchmark questions or resumed runs; objective is independently specified task correctness. Answer-derived material can shape a reference update, reference replacement changes later model context, and the reference has a wired model-authority channel. Causal links from objective-bearing evidence to a particular update and from later behavior to that update are unestablished here. This supports an improvement-directed standing mechanism, not exercised self-improvement or successful improvement attribution. Dataset scores do not close those links because they are not admission feedback.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-cheatsheet-context
Label: Reference text reaches generator decisions

Consumer: generator model. Channel: natural-language reference inserted into the CHEATSHEET region of a user-message template. Force: requested use/verification/adaptation, not compulsory correctness or privileged system policy. Horizon: subsequent cumulative rounds, later questions, and restart if driver reloads the reference. SRC-1, `dynamic_cheatsheet/language_model.py`, `prompts/generator_prompt.txt`, `run_benchmark.py`.

> generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", generator_cheatsheet_content)
> --- `dynamic_cheatsheet/language_model.py`

[RT-RTE-cumulative-curation](#rt-rte-cumulative-curation) installs successor text; [RT-RTE-context-selection](#rt-rte-context-selection) supplies alternative examples/synthesis. Delivery is implemented; model reliance and causal change in answers are uninspected.

#### RT-BAP-curator-guidance
Label: Prior reference and generated response shape curator proposal

Consumer: curator invocation of the configured model. Channel: natural-language template with prior reference, problem and generated response, or synthesis template with selected prior pairs and next problem. Force: instructions to evaluate/refine/preserve useful strategies; extraction grants returned text live reference status without semantic veto. Horizon: immediate update and successors reached through generator context and driver carry-forward. SRC-1, `dynamic_cheatsheet/language_model.py`, `prompts/curator_prompt_for_dc_cumulative.txt`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`.

> ## STEP 2: Run the cheatsheet extraction model with the generator output and the current cheatsheet
> cheatsheet_prompt = cheatsheet_template.replace("[[QUESTION]]", input_txt).replace("[[MODEL_ANSWER]]", generator_output).replace("[[PREVIOUS_CHEATSHEET]]", current_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py`

This is update-consumer authority distinct from subsequent solving authority. It establishes wired delivery and admission, not correct criticism, parameter learning or demonstrated benefit.

## Annotations

none
