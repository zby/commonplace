---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Dynamic Cheatsheet runtime baseline: benchmark state handoff, generator/curator calls, retrieval and local/provider execution at the frozen revision."
run-id: AAS-2026-10-20-dynamic-cheatsheet-523b6948294d-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet runtime report

## Runtime account

Dynamic Cheatsheet is a sequential inference-memory workflow, not an enclosing autonomous runtime. Python chooses the approach, supplies context, calls a generator and sometimes a curator, extracts text, and returns a result dictionary. The caller owns cross-query state. The claimed work is accumulating useful strategies without changing model parameters; that intent is recorded in [RT-CLM-adaptive-memory](#rt-clm-adaptive-memory). This account uses SRC-1 implementation and doctrine/design, under [the boundary](boundary.md#boundary-and-evidence). No target execution was performed. Historical JSONL results remain uninspected. A notebook-output search incidentally exposed saved second/third-round answers and cheatsheets, but this report uses notebook cell source only; it does not authenticate those outputs or establish causal improvement.

### Ordinary invocation and ownership

The README's cumulative benchmark command supplies both prompt paths. `run_benchmark.py` parses arguments, loads `config.env`, validates the approach, reads templates, constructs `LanguageModel`, loads a dataset, optionally shuffles with seed 10, and initializes or restores the cheatsheet. Its CLI defaults do **not** select the cumulative curator file: absent `cheatsheet_prompt_path`, the curator template is literally `(empty)`. Consequently a bare default invocation does not request the shipped curation instructions (SRC-1, `run_benchmark.py`, `README.md`).

For each example, Python forms the numbered question and passes it, the current cheatsheet, templates, settings and any prior-output/embedding slices to `advanced_generate`. Under cumulative mode, the generator receives one user message containing the template-expanded question and cheatsheet. It may enter a local execution continuation. The curator then receives a **separate** one-message context with the question, full generator output and previous cheatsheet. It is the same model/client, not a separately configured critic. Python extracts the new sheet, returns answer/output/steps, and the driver carries `final_cheatsheet` and `final_output` forward. Dataset targets are added to the saved envelope and used for scoring **after** generation/curation; they are not arguments to those calls. See [RT-RTE-cumulative-update](#rt-rte-cumulative-update) and [RT-RTE-benchmark-cycle](#rt-rte-benchmark-cycle).

There is no inter-agent scheduler here: Python owns the next step; models choose answer text, code requests and proposed retained content. Each query's generator/curator contexts are fresh rather than an ever-growing chat. Curator isolation keeps its analysis out of the next generator except for the extracted sheet. Cumulative repeated rounds additionally supply prior extracted answers when enabled; `max(1, max_num_rounds)` bounds those rounds. The hybrid branch performs just one generator/curator pair and does not implement that repeated-round loop (SRC-1, `dynamic_cheatsheet/language_model.py`).

The notebook repeats the same question three times, passing each returned sheet to the next call. The README example instead supplies a second question. Both are caller-owned read-back, not hidden persistence inside `LanguageModel` (SRC-1, `ExampleUsage.ipynb`, `README.md`).

### Material alternate routes and forcing cases

[RT-RTE-context-selection](#rt-rte-context-selection) covers all six shipped approaches. Retrieval selects previous examples by cosine similarity; synthesis adds a curator **before** generation; cumulative/hybrid update **after** generation. Full history copies all previous pairs; default replaces the sheet with `(empty)`. These differ in what enters the model, not merely in a display label.

Three forcing cases bound consequential controls:

1. **Execution disabled versus provider execution.** `advanced_generate(use_code_interpreter=True)` sets local execution false; a truthy container ID sends generator calls directly to provider tools. Direct `generate(allow_code_execution=False, use_code_interpreter=True)` still reaches that native branch. `allow_code_execution` is therefore a local-subprocess control, not a general no-execution grant. With no container ID, native selection falls through to ordinary generation. Through `advanced_generate` that fallback remains locally disabled; a direct `generate` call can retain its independently supplied local permission. See [RT-RTE-provider-execution](#rt-rte-provider-execution).
2. **Round limit versus local side effect.** The local code executes before the depth comparison. Default depth 1/limit 3 permits execution at depths 1, 2, 3 and 4 if every response qualifies; the last warning is not an enforced prohibition on depth-4 execution. The terminal branch also appends `current_output` again after adding it to `final_output`. This bounds the recursion, not the advertised number of executions. See [RT-RTE-local-execution](#rt-rte-local-execution).
3. **Curator correctness request versus admission.** A response containing `<cheatsheet>` is accepted by string extraction; a missing closing tag still returns the remainder. A missing opening tag falls back to the previous sheet for cumulative/hybrid, but to retrieved raw pairs for retrieval-synthesis. Dataset scoring cannot veto this admission because it occurs later. See [RT-RTE-cumulative-update](#rt-rte-cumulative-update).

### Guarantees, grants and evidence limits

The local execution switch is a code invariant **only over the guarded subprocess path in `generate`**, owned by `LanguageModel`. Native execution is an alternate path. OpenAI and Claude adapter calls also forward additional keyword parameters: OpenAI updates request parameters and Claude does `params.update(kwargs)`, whereas Gemini and xAI use narrower allowlists. Thus an API caller's `extra_api_params` can deliver provider tool configurations on ordinary OpenAI/Claude calls even when the wrapper's local flag is false; actual tool acceptance/execution depends on the external provider. The benchmark supplies only optional reasoning effort through this channel. No universal provider-tool exclusion follows (SRC-1, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`).

- Local-switch guarantee strength: invariant.
- Local-switch implementation conclusion status: wired
- Local-switch operation conclusion status: uninspected

The capability surface includes unrestricted local Python, provider-native execution when enabled, and provider-specific request extensions. The benchmark's current grant set defaults to local execution enabled, native disabled; runtime grants can differ per API invocation. The inspected local executor launches `python3` with the process's ambient environment and working directory. It supplies a three-second `communicate` timeout, not filesystem/network/credential isolation or a subprocess-tree termination guarantee. The provider branch requests hosted tools; service isolation is an external contract, not verified here. Furthermore GameOf24 scoring evaluates generated answer text in the benchmark process independently of `execute_python_code`; this prevents interpreting that flag as an isolation envelope for the entire benchmark (SRC-1, `dynamic_cheatsheet/utils/execute_code.py`, `dynamic_cheatsheet/utils/evaluation.py`).

Crash recovery is best effort, owned by the driver: it rewrites all output rows after each scored example and supports continuation into a new file. Writes use `open(..., "w")`, not atomic replacement. Evaluation or write failure can lose the newest in-memory update, and an interrupted rewrite can damage the file. Resume restores previous output text and the last sheet, skips the saved count, and checks selected arguments, not dataset identity, all settings or prompt content. New native sessions are created before restoration; provider container state is not restored. No exact replay guarantee is established (SRC-1, `run_benchmark.py`).

- Recovery guarantee strength: best effort.
- Recovery implementation conclusion status: wired
- Recovery operation conclusion status: uninspected

Provider exceptions receive up to three attempts with ten-second delays; exhaustion raises `RuntimeError`. This does not make tool effects idempotent. Empty responses become `(No response generated)`, which may reach extraction/curation. Output token limits and prompt word-count advice do not implement a memory-size or context-fit guarantee (SRC-1, `text_generation/simple_unified_client.py`, `dynamic_cheatsheet/language_model.py`, `prompts/curator_prompt_for_dc_cumulative.txt`).

Inspection added no source identity: all anchors remain SRC-1 at the frozen commit. Beyond boundary coverage, this member inspected the full provider request assembly for ordinary OpenAI/Claude/Gemini/xAI generation and both native execution methods, complete extraction/local-execution/evaluation files, README, all prompt templates, driver and notebook cell sources. Precomputed vector contents, dataset payload integrity, historical result corpora and provider internals remain uninspected. This prevents retrieval-quality, leakage, live-compatibility and measured-benefit conclusions. Semantic memory/theory revision findings are left to the specialist rather than inferred from function names.

## Shared records

### Components

#### RT-CMP-language-model
Label: LanguageModel provider-backed model

Source-native identity: `LanguageModel.client`, a `UnifiedLLMClient` configured from provider/model text. Generator and curator use this same endpoint. Representational form: distributed-parametric model, remotely served or Ollama-accessed; parameter storage is outside the checkout. No inspected code updates weights during operation. Exact model version is not universally pinned: callers choose a string, including aliases such as `claude-3-5-sonnet-latest`; a mutable endpoint can resolve differently. Even a dated identifier depends on provider version guarantees. Provider internals and training state are uninspected. SRC-1, `dynamic_cheatsheet/language_model.py`, `README.md`.

> self.client = UnifiedLLMClient(**client_kwargs)
> --- `dynamic_cheatsheet/language_model.py`

### Operative objects

#### RT-OBJ-output-dict
Label: advanced_generate result envelope

Source-native identity: returned dictionary with `steps`, `final_answer`, `final_output`, `final_cheatsheet` and branch-specific retrieval/previous-answer fields. Representational form: symbolic Python keys and lists, serialized by the driver as JSONL; text values remain model-interpreted natural language or code when later consumed. Storage: current Python process, then driver-selected filesystem path. This record identifies the envelope, not the retained sheet's semantic parts. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`.

> generator_outputs_so_far.append(output_dict["final_output"])
> --- `run_benchmark.py`

### Routes

#### RT-RTE-benchmark-cycle
Label: Benchmark generation persistence and evaluation

The CLI/operator chooses a task, approach, model, templates and initialization/resume files. Python owns dataset order, per-question invocation, state handoff, scoring and disk writes. The bounded benchmark mode has expected answers from dataset `target`; GameOf24 additionally uses arithmetic/rule checks. These are evaluation oracles, not curator admission gates. Computation performs the loop; human per-content approval is not wired. The API also permits open caller-supplied questions outside this benchmark mode. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/utils/evaluation.py`, `README.md`.

- Immediate return: answer, full output, updated sheet and steps in [RT-OBJ-output-dict](#rt-obj-output-dict); CLI prints answers, targets and counts.
- Later read-back: next example receives the last sheet and prior output list; continuation reloads saved rows and last sheet.
- Delegated visibility: provider receives selected prompt messages, not the saved target field through this call path.
- Selection predicate: dataset iteration after optional seed-10 shuffle; resume skips indices below saved-row count.
- Invalidation or expiry: caller initialization/restart or replacement of saved state; no semantic expiry rule in this driver.
- Activation or effect: wired filesystem persistence and subsequent input supply; behavior changes from those inputs remain unobserved here.
- Evidence limits: result corpora and dataset payloads not evaluated; restored correctness counters start at zero and count newly processed examples only.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py`

> with open(file_path, "w") as file:
>     for line in data:
>         file.write(json.dumps(line) + "\n")
> --- `run_benchmark.py`

#### RT-RTE-cumulative-update
Label: Cumulative generator curator admission

Trigger: each cumulative round, or one hybrid answer. Generator proposes a solution; curator proposes replacement reference text after seeing current question, full output and old sheet. Python decides admission by extraction rather than correctness; human veto is not required. The curator prompt asks for validation, useful strategies, retained examples and counters; the persisted product is extracted text, not curator analysis or a software-validated usage counter. Recovery on missing opening tag is the old sheet; driver logs retain prior steps but no automatic semantic rollback is implemented. Operating mode is caller questions or benchmark sequence; update is unconditional after an answer, not triggered by an oracle failure. No answer oracle is passed to this admission route. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `prompts/curator_prompt_for_dc_cumulative.txt`.

- Immediate return: last generated answer and extracted new sheet with steps; previous round answers are additionally returned in cumulative mode.
- Later read-back: updated sheet becomes the next round's input and, through driver/notebook handoff, later questions' input.
- Delegated visibility: curator sees generator output including local execution transcript, not an independent reference answer; generator does not receive curator analysis.
- Selection predicate: cumulative approach and at least one round; hybrid invokes its own one-pair update.
- Invalidation or expiry: entire sheet replaced on accepted extraction; omitted old contents disappear from live sheet, although earlier logged versions can remain on disk.
- Activation or effect: Python replaces the carried text; reliable validation, selective preservation and improved solving are not established by that write.
- Evidence limits: prompt requests are not compliance evidence; semantic theory criticism and capacity change are not assessed by this runtime record.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

> txt = response.split("<cheatsheet>")[1].strip()
> txt = txt.split("</cheatsheet>")[0].strip()
> return txt
> --- `dynamic_cheatsheet/utils/extractor.py`

#### RT-RTE-context-selection
Label: Approach-specific context construction

Python selects context by approach name, then generator/curator models interpret its text. Default injects `(empty)`. FullHistoryAppending formats all prior input/output pairs without curator selection. Dynamic_Retrieval computes cosine similarities between the last embedding and preceding embeddings, sorts descending, takes top-k, then inserts pairs in reverse order so the most similar appears last. RetrievalSynthesis first sends selected pairs, previous sheet and next question to a curator, extracts a custom sheet, then solves; hybrid appends selected examples to a cumulative sheet, solves, then updates only the cumulative sheet. Synthesis is model-proposed context replacement admitted by the same opening-tag extractor; no human approval or expected-answer oracle enters it. Guidance asks for reusable strategies and correctness review, not a mechanically verified selection. SRC-1, `dynamic_cheatsheet/language_model.py`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`.

- Immediate return: generator result, supplied custom/reference sheet, and selected original inputs/outputs on retrieval routes.
- Later read-back: caller carries final sheet and generator outputs; raw prior outputs stay available for future retrieval even if omitted by a synthesis.
- Delegated visibility: generator sees selected pairs or synthesized text, not the complete corpus in retrieval modes; curator receives current next question as well as selected pairs and prior sheet.
- Selection predicate: top-k cosine ranking of input vectors, not answer correctness; no earlier examples yields `(empty)` pairs. Hybrid permits missing embeddings and still uses its cumulative sheet.
- Invalidation or expiry: per-query context rebuilt; no corpus eviction rule in these branches. Synthesis missing-tag fallback is selected raw pairs, not the prior synthesized sheet.
- Activation or effect: changes model-visible context composition; actual adherence or benefit is unobserved.
- Evidence limits: driver aligns CSV vectors by exact input lookup; API assumes compatible corpus/vector/output lengths. Embedding provenance and retrieval quality remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
> top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
> --- `dynamic_cheatsheet/language_model.py`

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=curated_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py`

#### RT-RTE-local-execution
Label: Model-requested local Python continuation

The generator proposes Python text and an execution flag. `generate` owns dispatch when permission is true, the flag is present and pre-flag text ends in a closing fence. The extractor takes the first Python block and may rewrite its last line as a print expression. A temporary file is run with local `python3`; stdout or an error/timeout message is returned to the model along with a continuation request. Python controls recursion, not the model's compliance with the last-round warning. No human approval occurs between code proposal and execution. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py`.

- Immediate return: concatenated generation and code-result transcript, then subsequent model answer; terminal depth branch duplicates its last current-output segment.
- Later read-back: full output can enter curator input and driver-retained prior outputs; generated local program variables do not survive into the next subprocess by this mechanism.
- Delegated visibility: continuation sees the same history plus assistant code/result text and a user request to finish or try alternatives.
- Selection predicate: allowed flag plus closing fence before execution marker; extractor additionally requires a Python opening fence.
- Invalidation or expiry: temporary source file removed; no automatic rollback of filesystem or network effects; child process killed on timeout.
- Activation or effect: local process execution with ambient privileges, not a sandboxed capability grant.
- Evidence limits: no process-tree cleanup guarantee or observed execution asserted; round bound checks follow execution rather than precede it.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
> stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py`

> executed_code = extract_and_run_python_code(output_prefix)
> --- `dynamic_cheatsheet/language_model.py`

> if current_depth <= max_depth_num_rounds:
> --- `dynamic_cheatsheet/language_model.py`

#### RT-RTE-provider-execution
Label: Provider-native execution and direct-call alternatives

Caller selects native execution and creates or supplies a session identifier. Claude creation returns a sentinel; OpenAI creation requests a container. With a truthy identifier `generate` calls native execution before ordinary generation/local execution checks. OpenAI sends Responses API tools and returns `output_text`; Claude sends a native code-execution tool and concatenates returned text blocks. Provider service owns any internal tool progression. Advanced generation disables local execution whenever native mode is requested; curators omit native mode and set local execution false, though API-supplied provider kwargs can still affect ordinary requests. This is not a host callback or remote-worker scheduler implemented by Dynamic Cheatsheet. SRC-1, `dynamic_cheatsheet/language_model.py`, `text_generation/simple_unified_client.py`.

- Immediate return: provider text only, not a complete structured tool-event record.
- Later read-back: output text reaches normal extraction/curation; OpenAI container ID is reused within the benchmark run, but not saved/restored as durable continuation state.
- Delegated visibility: hosted service receives message history, model identifier, requested tool and optional API parameters.
- Selection predicate: native flag and truthy container ID; missing ID falls through. Provider family determines Claude native versus OpenAI-compatible method.
- Invalidation or expiry: provider session lifecycle is external and uninspected; no source-owned container rollback or deletion shown in these methods.
- Activation or effect: requests provider-side execution; provider acceptance and isolation are external contracts.
- Evidence limits: live service behavior is unobserved; enabling local switch false does not suppress this route or provider-native tools passed by an API caller.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if use_code_interpreter and self.container_id:
> --- `dynamic_cheatsheet/language_model.py`

> "tools": [{"type": "code_interpreter", "container": container_id}],
> --- `text_generation/simple_unified_client.py`

> code_execution_tool = {"type": "code_execution_20250825", "name": "code_execution"}
> --- `text_generation/simple_unified_client.py`

#### RT-RTE-score-answer
Label: Post-generation answer scoring

The benchmark and evaluation notebook dispatch task scorers. Expected outcomes come from dataset/saved targets; GameOf24 computes arithmetic and digit-multiset checks. AIME compares normalized text, multiple choice accepts supported letter/text matches, and equation balancing checks number-string shape then numerical equality. These scoring operations classify an already generated answer, not curator candidates. The notebook independently extracts the first answer tag from the last step and applies additional AIME boxed-answer processing, whereas runtime extraction prefers the last opening answer tag. Counts therefore depend on the consumer path. SRC-1, `run_benchmark.py`, `EvaluatingResults.ipynb`, `dynamic_cheatsheet/utils/evaluation.py`, `dynamic_cheatsheet/utils/extractor.py`.

- Immediate return: Boolean scoring result and printed cumulative/file totals.
- Later read-back: inapplicable — driver does not pass score outcomes into later generator/curator calls.
- Delegated visibility: inapplicable — inspected scorers are local Python functions, not model judges.
- Selection predicate: task name selects scorer after extracting answer text.
- Invalidation or expiry: inapplicable — transient counters do not revise retained reference text.
- Activation or effect: local evaluation; GameOf24 invokes Python eval on cleaned model text before checking its numbers, outside the generation execution flag.
- Evidence limits: no aggregate accuracy computed here; scoring correctness and safety are not guaranteed by the existence of a scorer.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> value = eval(clean_output)
> --- `dynamic_cheatsheet/utils/evaluation.py`

### Claims

#### RT-CLM-adaptive-memory
Label: Parameter-preserving adaptive memory claim

The README claims accumulated reusable strategies and performance gains without changing model parameters. The wiring above supports text retention and later supply, not those gains by itself. SRC-1, `README.md` (doctrine/design and reported operation).

> Dynamic Cheatsheet (DC) endows black-box language models with the ability to store and reuse insights across queries. Rather than repeatedly re-discovering solutions or making the same mistakes, DC enables models to accumulate and leverage strategies, code snippets, and problem-solving techniques without modifying the underlying model parameters.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-reference-context
Label: Retained reference to generator context

Consumer: generator model. Channel: natural-language cheatsheet and/or previous solution text substituted into a user-message template. Force: requested reference and strategy guidance, not an enforced algorithm or validated instruction grant. Horizon: next round/query and resumed benchmark through caller handoff. This is live input wiring, not proof of changed behavior. SRC-1, `dynamic_cheatsheet/language_model.py`, `prompts/generator_prompt.txt`, `run_benchmark.py`.

> - Carefully analyze both the question and cheatsheet before starting
> - Search for and identify any applicable patterns, strategies, or examples within the cheatsheet
> --- `prompts/generator_prompt.txt`

## Annotations

none
