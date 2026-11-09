---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Dynamic Cheatsheet cumulative benchmark workflow from question delegation through local execution, curation, scoring, checkpoint delivery and continuation."
run-id: AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet workflow report

## Workflow account

### Selected workflow and evidence

This report traces one cumulative benchmark question through answer generation, optional local Python continuation, reference replacement, scoring and checkpoint delivery, then follows the reference into a later question or resumed run. This is representative because cumulative curation is the driver's default approach and includes both the memory producer and its shipped persistence/reload consumer. The selected configuration supplies the shipped cumulative curator prompt and uses local execution rather than provider-native tools. The CLI default alone does not supply that curator prompt: without its path, the driver substitutes `(empty)`. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`; [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation).

The account establishes implementation at the frozen revision, not a successful run. It does not join retrieval or native execution into this selected path. Those alternatives change handoff order or execution ownership and remain characterized by [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) and [RT-RTE-native-execution](runtime.md#rt-rte-native-execution). No benchmark, provider request or target example was executed. No retained result payload was inspected for workflow success.

### Request, principals and handoffs

The caller chooses task, model, prompt files, initial or resumed reference and execution settings. The driver loads the task, optionally shuffles it with seed 10, constructs the numbered problem and answer-format instructions, and calls `advanced_generate`. It keeps the dataset target outside this request. Python owns scheduling; the configured model supplies answer and reference content. The generator and curator are sequential roles of one configured backend, not independent workers that select their own delegates. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`; [RT-CMP-language-model](runtime.md#rt-cmp-language-model).

| Handoff | Supplied material | Recipient responsibility and return |
|---|---|---|
| Driver → wrapper | Current question, live cheatsheet, templates, generation/round/execution settings | Schedule at least one generator–curator round and return a result dictionary. |
| Wrapper → generator | One user message containing question and cheatsheet; later refinement rounds can also include previous extracted answers | Produce solution text and optionally request local code execution. |
| Wrapper → local executor → generator | First Python fence selected from eligible flagged text; execution output inserted into assistant text, followed by a user continuation request | Executor returns output/error text; model is asked to complete or try alternatives. |
| Wrapper → curator | Question, full generator output and previous cheatsheet; twice the generator token limit, local execution disabled | Propose replacement reference under the curation template, without target or score. |
| Wrapper → driver | Round steps, previous answers, final answer, final output and final cheatsheet | Carry state forward, score the answer and write JSONL. |

These handoffs are implemented in SRC-1, `dynamic_cheatsheet/language_model.py` and `run_benchmark.py`; their minimum source passages are retained in [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) and [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict). There is no parallel join in this inspected sequence. The wrapper returns the last round's answer/output and successor reference, while its steps preserve earlier round prompts, outputs and old/new references. It does not include the curator's full response in those step records. SRC-1, `dynamic_cheatsheet/language_model.py`.

### Verification and rejection are separate decisions

The curator prompt asks the model to assess correctness, preserve useful material and refine reusable strategies. This is requested model judgment, not an independently supplied answer oracle. The extractor decides which reference text becomes live, using delimiters rather than correctness. Missing the opening cheatsheet tag preserves the previous reference; an opening tag without a closing tag can still admit the remaining text. Omitted old content is not automatically merged back. SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`, `dynamic_cheatsheet/utils/extractor.py`; [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation).

Answer extraction is likewise not a delivery gate for curation. If the generator has no recognized final-answer marker, extraction can return a failure string, but the wrapper still supplies the full generator output to the curator. There is no conditional retry or admission veto on that failure string in the selected cumulative branch. SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`; see the workflow annotation below.

The driver scores only after the wrapper has returned the successor reference and the driver has assigned it. Its task scorer uses the dataset target or task validity rules, but a false score neither rejects the new cheatsheet nor restarts curation. Thus task correctness reporting and memory admission do not form a verification loop. The next question can consume a reference derived from an incorrect answer. SRC-1, `run_benchmark.py`; [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring), [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context). This is a wired possibility, not evidence that a particular wrong strategy was retained or used.

### Failure ownership and recovery

On the optional local execution path, the executor reports a timeout or execution error as text. The wrapper places that text in the continuation conversation and asks the generator to complete the answer or try alternatives. This delegates recovery reasoning to the model; it does not establish that recovery succeeds. The subprocess has a three-second timeout and direct-child kill, not demonstrated isolation or rollback of filesystem effects. The depth check occurs after execution, so the final warning is not a hard three-execution gate. SRC-1, `dynamic_cheatsheet/utils/execute_code.py`, `dynamic_cheatsheet/language_model.py`; [RT-RTE-local-execution](runtime.md#rt-rte-local-execution).

An unparseable curator response takes the extractor fallback without a new curator attempt. A parseable but poor replacement has no automatic semantic rollback. Previous reference versions in round steps/checkpoints can assist external manual recovery; they are not an automatic recovery controller. SRC-1, `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/language_model.py`; [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation).

### Delivery and continuation

Library delivery is the returned dictionary, not disk persistence. Driver delivery adds the original target/raw input to that dictionary, updates its in-memory histories and reference, prints and scores the result, and rewrites the accumulated JSONL after each example. The loop ends at the dataset boundary or configured sample limit; it writes again and prints accuracy for processed examples. Neither a correct answer nor successful curation is required to reach the save call. An exception before that call can prevent the current example from being checkpointed. SRC-1, `run_benchmark.py`; [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict), [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation).

A later invocation explicitly requested by the caller reloads JSONL and companion parameters, rejects mismatches in selected arguments, recovers the last final cheatsheet and full-output history, and skips a number of examples equal to the loaded row count. It writes to a continued filename. This is positional continuation, not exact replay: prompt bytes, several settings and provider identity resolution are not completely checked, and writes are truncating rather than atomic. Bad/empty checkpoint contents can prevent recovery. SRC-1, `run_benchmark.py`; [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation). The driver owns this recovery protocol; no autonomous worker repairs a checkpoint.

The terminal result therefore has two distinct consumers: the evaluator reads the answer/target, while later generation reads the returned or restored reference. Retention and delivery to that later model are wired; reliance, correctness preservation and improvement remain unobserved. SRC-1, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`; [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context).

### Inspection coverage

This member checked the complete benchmark driver and extractor, the complete local executor and cumulative curator prompt, and the `generate` and cumulative `advanced_generate` implementation ranges in SRC-1, `dynamic_cheatsheet/language_model.py`. These are implementation or doctrine/design evidence already inside the boundary. It also inspected the provider retry helper in SRC-1, `text_generation/simple_unified_client.py`; that helper alone is not an end-to-end recovery guarantee. No new source or observed-run evidence is added. External service behavior and result payloads remain outside the conclusions reached here.

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

#### On [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation)

Workflow verification boundary: the wrapper extracts an answer but does not make successful extraction a prerequisite for the curator handoff. SRC-1, `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/language_model.py`.

> if not("FINAL ANSWER" in response):
>     return "No final answer found"
> --- `dynamic_cheatsheet/utils/extractor.py`

> # Extract the output from the generator model
> generator_answer = extract_answer(generator_output)
>
> ## STEP 2: Run the cheatsheet extraction model with the generator output and the current cheatsheet
> cheatsheet_prompt = cheatsheet_template.replace("[[QUESTION]]", input_txt).replace("[[MODEL_ANSWER]]", generator_output).replace("[[PREVIOUS_CHEATSHEET]]", current_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py`

The curator receives full output even when the answer string signals extraction failure. This source branch establishes scheduling, not an observed failed-answer episode or successful correction. No new referent is declared: this is a workflow-specific acceptance limit on the supplied cumulative route.
