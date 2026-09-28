---
type: types/agentic-system-analysis-result.md
description: "Dynamic Cheatsheet workflow analysis at its pinned implementation and shipped example boundary"
run-id: AAS-2026-09-27-dynamic-cheatsheet-01
system: "Dynamic Cheatsheet"
run-date: "2026-09-27"
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
analysis-cutoff: "2026-09-27"
evidence-tier: code-grounded
memory-comparison:
  scope: "Accumulated cheatsheets, previous problem/solution traces, their CSV/array access metadata, JSONL persistence and continuation, local execution traces, and native interpreter state across all six LanguageModel approaches. Static templates are mechanism evidence, not accumulated memory; provider internals remain opaque within the native route."
  axes:
    storage_substrate:
      assessment: "partial"
      values: ["files", "in-memory", "service-object"]
      evidence: {"files": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "RTE-1"], "note": "JSONL checkpoints and CSV embeddings persist local memory."}, "in-memory": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-5"], "note": "Strings, lists and NumPy arrays hold operative memory during the loop."}, "service-object": {"basis": "wired", "records": ["OBJ-6", "RTE-7"], "note": "OpenAI container identity is created once and reused across benchmark questions."}}
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. No vector database is implemented; numeric vectors in CSV/arrays are not a separate vector store."
    representational_form:
      assessment: "partial"
      values: ["natural-language", "symbolic"]
      evidence: {"natural-language": {"basis": "wired", "records": ["OBJ-1", "OBJ-2"], "note": "Cheatsheet prose and solution text enter model prompts."}, "symbolic": {"basis": "wired", "records": ["OBJ-3", "OBJ-7", "RTE-7"], "note": "Numeric access arrays, retained code and tool output participate in ranking or execution routes."}}
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-6", "OBJ-7"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch."
    lineage:
      assessment: "partial"
      values: ["trace-extracted", "imported"]
      evidence: {"trace-extracted": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "Curators consume prior generator solutions and produce retained guidance."}, "imported": {"basis": "wired", "records": ["OBJ-3", "RTE-1"], "note": "Precomputed embeddings and optional seed cheatsheet are loaded from files."}}
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Seed provenance and embedding producer are unspecified; no authored lineage is inferred merely from file import."
    behavioral_authority:
      assessment: "partial"
      values: ["knowledge", "ranking"]
      evidence: {"knowledge": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-5", "RTE-6"], "note": "Reference solutions and cheatsheet advice are supplied to generator/curator, with instructions to verify applicability."}, "ranking": {"basis": "wired", "records": ["OBJ-3", "RTE-5"], "note": "Cosine similarities rank prior examples for selection."}}
      records: ["OBJ-1", "OBJ-2", "OBJ-3", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Static generator/curator instructions are outside accumulated memory; memory advice is not an enforcement or validation gate."
    write_agency:
      assessment: "partial"
      values: ["automatic"]
      evidence: {"automatic": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Runner records outputs and accepts extracted curator replacements without a human approval step."}}
      records: ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. A supplied seed file permits external editing but the repository does not establish who authored it; do not infer a manual memory-write route from import alone."
    curation_operations:
      assessment: "partial"
      values: ["evolve", "consolidate", "dedup", "synthesize", "promote"]
      evidence: {"evolve": {"basis": "wired", "records": ["RTE-2", "RTE-4"], "note": "Existing cheatsheet is included in curator input and replaced by extracted response."}, "consolidate": {"basis": "wired", "records": ["RTE-10"], "note": "Invoked curator instructions select useful material and discard trivial detail."}, "dedup": {"basis": "wired", "records": ["RTE-10"], "note": "Invoked curator instructions explicitly remove duplicate entries."}, "synthesize": {"basis": "wired", "records": ["RTE-10"], "note": "Invoked curator instructions introduce new meta-strategies from problem-solving experience."}, "promote": {"basis": "claimed", "records": ["RTE-10"], "note": "Prompt asks usage counts to prioritize frequently used strategies; no deterministic count update or salience selector verifies this."}}
      records: ["RTE-2", "RTE-3", "RTE-4", "RTE-10", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Prompt-directed operations are not guaranteed semantic outcomes. Overwrite/omission alone does not establish decay or explicit invalidation."
    read_back_direction:
      assessment: "partial"
      values: ["push"]
      evidence: {"push": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4", "RTE-5", "RTE-6"], "note": "Runner automatically assembles prior memory for generator and curator; neither model issues a retrieval request."}}
      records: ["RTE-2", "RTE-3", "RTE-4", "RTE-5", "RTE-6", "RTE-7"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Native code may request prior container resources, but payload use is not exposed sufficiently to classify pull."
    read_back_signal:
      assessment: "partial"
      values: ["coarse", "inferred-embedding"]
      evidence: {"coarse": {"basis": "wired", "records": ["RTE-2", "RTE-6"], "note": "Each question triggers delivery of the complete current cheatsheet or all prior solution pairs."}, "inferred-embedding": {"basis": "wired", "records": ["RTE-3", "RTE-4", "RTE-5"], "note": "Current question vector and prior vectors determine top-k previous pairs by cosine similarity."}}
      records: ["RTE-2", "RTE-3", "RTE-4", "RTE-5", "RTE-6", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Curator judgment transforms supplied memory; it is not a separate established memory-delivery selector. IDs and question references do not themselves select content."
    trace_learning:
      assessment: "known"
      values: ["yes"]
      evidence: {"yes": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Automatic solution-fed cheatsheet writes persist and are delivered to later problem-solving calls."}}
      records: ["RTE-1", "RTE-2", "RTE-3", "RTE-4"]
      note: "The positive boolean is established by local routes irrespective of opaque native alternatives; no improvement or parameter update is required."
    trace_source:
      assessment: "partial"
      values: ["trajectories", "tool-traces"]
      evidence: {"trajectories": {"basis": "wired", "records": ["OBJ-2", "RTE-2", "RTE-3", "RTE-4"], "note": "Previous questions and model solution sequences feed curator writes."}, "tool-traces": {"basis": "wired", "records": ["RTE-7", "RTE-2"], "note": "Local execution output is concatenated into generator output, which the curator consumes."}}
      records: ["OBJ-2", "RTE-2", "RTE-3", "RTE-4", "RTE-7"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Native responses expose text only, not complete tool traces."
    learning_scope:
      assessment: "partial"
      values: ["cross-task", "per-task"]
      evidence: {"cross-task": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Guidance generated from solved benchmark questions carries into later distinct questions."}, "per-task": {"basis": "wired", "records": ["RTE-2"], "note": "Configured cumulative refinement rounds reuse a newly derived cheatsheet on the same input."}}
      records: ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Benchmark task means dataset family; classification task means a problem-solving objective, not a session identifier."
    learning_timing:
      assessment: "partial"
      values: ["online"]
      evidence: {"online": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Curator calls run inside question processing before later generation; continuation reloads their outputs."}}
      records: ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Precomputed embedding acquisition is not trace learning and adds no offline value."
    distilled_form:
      assessment: "partial"
      values: ["natural-language", "symbolic"]
      evidence: {"natural-language": {"basis": "wired", "records": ["OBJ-1", "RTE-10"], "note": "Curator produces reusable explanations, strategies and reasons."}, "symbolic": {"basis": "wired", "records": ["OBJ-1", "RTE-10"], "note": "Curator produces reusable code snippets and mathematical formulas retained inside cheatsheet text."}}
      records: ["OBJ-1", "RTE-10", "OBJ-6"]
      note: "Native interpreter payloads and provider retention are opaque; the exposed positives do not exhaust that included branch. Mixed guidance remains mixed even though delivered through a text prompt."
    faithfulness_tested:
      assessment: "not-determinable"
      values: []
      evidence: {}
      records: ["CLM-5"]
      note: "Inspected runner/evaluation and shipped examples show accuracy reporting and apparent reuse, not a retained intervention isolating dependence on recalled content; sampled outputs cannot establish a repository-wide negative."
---

# Dynamic Cheatsheet agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/dynamic-cheatsheet.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-01/memory-report.md`
**Memory analysis report SHA-256:** aa49de3cde70ec6de5fb8f1607aef992160a03cab9b5d5496edc9bba4f3aef12

The source-only coordinator used the current analysis and epistemic instructions. The memory specialist received a frozen source/input boundary in a fresh context. No previous Commonplace review, audit, comparison or analysis result supplied evidence. Runtime model identity for the coordinator: unknown.

## Boundary and evidence

This analysis characterizes what the shipped Dynamic Cheatsheet workflow executes, how its retained material reaches later solving calls, and which checks warrant reliance. The whole-system boundary includes the benchmark runner, callable LanguageModel workflow, six approach branches, prompt templates, response extraction, JSONL recovery, local execution and native interpreter interfaces. It includes the notebook and selected JSONL artifacts as retained execution evidence, without claiming they were generated by this exact code revision.

The boundary excludes provider implementation/training and external dataset construction: no conclusions about provider weights, isolation guarantees, training contamination or dataset correctness follow. Provider-native state remains an included interface with opaque internals, not an excuse to classify its memory as known. Other utility-client entry points not reached by LanguageModel, including its independent chat/history and web-search conveniences, are outside the reviewed workflow; their general-purpose capabilities are not assigned to Dynamic Cheatsheet.

The evidence boundary is only `https://github.com/suzgunmirac/dynamic-cheatsheet` at `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, cutoff 2026-09-27. All Git evidence came from commit-addressed blobs through the verified checkout `/home/zby/llm/commonplace/related-systems/suzgunmirac--dynamic-cheatsheet`. No services, fetches or source mutations were performed. Code-grounded describes the implementation analysis; README performance claims remain attributed claims.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git repository | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Implementation: runner, model wrapper, extraction, execution, evaluator and relevant provider-client calls. Doctrine/design: README and three prompts. Observed artifact: notebook and explicitly selected result records; these layers remain distinct on records. | `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/utils/execute_code.py`, selected `dynamic_cheatsheet/utils/evaluation.py` and `text_generation/simple_unified_client.py` spans; prompts; `README.md`; `ExampleUsage.ipynb`; first two AIME 2024 Claude cumulative result records; specialist inspected first two GPT-4o AIME cumulative, retrieval-synthesis and retrieval records, evaluation notebook code, sampled CSV headers/rows, and native text extraction | Full paths and pinned quote attributions on canonical records | Provider internals, fresh live executions, exhaustive outcome corpus and historical runtime configuration are uninspected; prevents fresh benchmark reproduction and whole-corpus causal claims. |

## Shared records

### Components

### CMP-1 — Generator and curator LLM

The same LanguageModel instance sends generator and curator calls through UnifiedLLMClient. Distributed-parametric form; remote service execution, with provider/model selected by a string. Caller-side parameter adaptation is not implemented on these inference routes; provider-internal parameter changes are uninspected. Exact model identity is caller-selectable, not enforced: aliases and dated examples coexist. Parameter-fixity claim: claimed in README; inference-only call wiring: wired; exact provider weights: uninspected. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:76-113,411-431`, `README.md:13-20,125-135`.

> client_kwargs = {"provider": provider, "model": model_id, "max_retries": 3, "retry_delay": 10}
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CMP-2 — Unidentified embedding producer

The implementation consumes precomputed vectors but does not name their producer in the inspected runner, README, notebooks, or sampled CSV metadata. Evidence: SRC-1 `run_benchmark.py:201-220`; `embeddings/AIME_2024.csv:1`; `embeddings/GameOf24.csv:1`. The header is `input,tokens,embedding`; there is no model column. Keep this seed as unresolved producer identity, not an identified model. Shape alone would not identify its producer.

Producer parameter changes and version fixity are uninspected because producer identity itself is unresolved. The vectors are fixed input bytes at this analysis pin, which does not identify the weights that produced them.

### Operative objects

### OBJ-1 — Current and historical cheatsheet text

An in-memory string becomes `final_cheatsheet` in each JSONL row, with prior/current/new fields in cumulative steps. It contains natural-language advice plus code and formulas, derived from generator solutions and prior guidance; optional file import can initialize it. Later generator and curator calls receive it as reference knowledge. The generator template asks for applicability checks rather than blind execution. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:396-455`; `run_benchmark.py:170-189,274-280,308-315`; `prompts/generator_prompt.txt:9-21`.

> - Carefully analyze both the question and cheatsheet before starting
> - Search for and identify any applicable patterns, strategies, or examples within the cheatsheet
> - Create a structured approach to solving the problem at hand
> - Review and document any limitations in the provided reference materials
> --- `prompts/generator_prompt.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The loaded prompt treats the memory as advice to inspect. XML-like memory-item tags, source-question references and usage counters are not parsed as individual addressable records by this implementation. The new string wholly replaces current memory; historical rows remain available on disk.

### OBJ-2 — Prior inputs and generator outputs

The runner accumulates raw solution outputs in a Python list and checkpoints their surrounding question/answer/step records in JSONL. This raw corpus is distinct from derived cheatsheets. It may contain reasoning, generated Python and actual subprocess output. Retrieval and full-history paths reuse solution text, without filtering to correctly scored examples. Evidence: SRC-1 `run_benchmark.py:254-280,290-309`; `dynamic_cheatsheet/language_model.py:249-288,457-575`.

>         generator_outputs_so_far.append(output_dict["final_output"])
> 
>         outputs.append({
>             "input": current_input,
>             "target": original_target,
>             "raw_input": original_input,
>             **output_dict,
>         })
>         cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-3 — Precomputed input embeddings

CSV files hold input text, token metadata and numeric embedding arrays; pandas/NumPy load and reorder vectors against dataset inputs. They are imported access metadata, not a learned solution corpus or a vector database. Cosine similarities give them ranking authority over the retained examples selected for later context. Evidence: SRC-1 `run_benchmark.py:204-220`; `dynamic_cheatsheet/language_model.py:503-514`.

>             if len(prev_original_input_embeddings) > 0:
>                 similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
>                 top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
>                 top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
>                 top_k_similar_values = similarities[0][top_k_indices]
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-6 — Native interpreter service state and identity

Proposed operative object. The runner creates one interpreter session per benchmark run; OpenAI later calls reuse the container ID. This establishes a service-object interface and a run spanning multiple problem objectives. It does not reveal the files, variables, dependencies, retention rules, curation, or later memory read operations inside the container. Claude's sentinel is not evidence of cross-request retained state. Returned text is a readable projection, not the container payload itself. Evidence: SRC-1 `run_benchmark.py:115-118`; `dynamic_cheatsheet/language_model.py:157-172,212-234`; `text_generation/simple_unified_client.py:1128-1153,1191-1210`. Implementation conclusion status: wired for interface reuse; payload classification remains not determinable.

>         params: Dict[str, Any] = {
>             "model": self.model,
>             "input": messages,
>             "tools": [{"type": "code_interpreter", "container": container_id}],
>         }
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         def _call():
>             response = self.openai_client.responses.create(**params)
>             return response.output_text
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-7 — In-progress local execution history

Proposed operative object. Conversation message lists and accumulated output strings retain tool-produced stdout/error text and generated code through recursive generator calls. They are automatic raw trajectory/tool-trace retention; they become inputs to derived guidance only when a curator route is selected. They are retained in OBJ-2 and step outputs once the answer is checkpointed. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:249-288,422-445`; `dynamic_cheatsheet/utils/execute_code.py:48-59,81-101`. Implementation conclusion status: wired. The quotation on RTE-7 supplies the transition.

### OBJ-4 — Current answer and execution transcript

The generated problem solution is natural-language reasoning mixed with optional Python and observed tool text, held in strings and returned with an extracted final answer. It is a work product before becoming historical material in OBJ-2. SRC-1 `dynamic_cheatsheet/language_model.py:249-288,419-454`. The notebook retains particular expressions and executed solver output; this supports observed local operation, not a blanket truth guarantee.

### OBJ-5 — Static generator and curator templates

Files hold natural-language instructions with substitution slots. They are human-authored method texts, not accumulated read-back memory. They request analysis, correctness checking, reuse and curation; the caller chooses their paths. SRC-1 `run_benchmark.py:95-100`, `prompts/generator_prompt.txt:9-21`, `prompts/curator_prompt_for_dc_cumulative.txt:11-31`.

The supporting generator instruction is quoted on OBJ-1.

### Routes

### RTE-1 — Benchmark progression and continuation

Implementation conclusion status: wired. A human selects task, approach, model, prompts, code grant and optional prior run. Python owns sequential progression: load dataset, optionally shuffle with seed 10, initialize/read cheatsheet and prior outputs, call the selected approach, append answer, replace cheatsheet, evaluate, and rewrite JSONL after each example. The immediate return is a structured answer/steps/cheatsheet record; later read-back restores final_cheatsheet and final_output history. Selection is full prior output prefix, with task embeddings reordered to the current dataset. No expiry or per-entry invalidation occurs here. Delegated visibility is only the material chosen by the selected branch. SRC-1 `run_benchmark.py:124-225,253-315`.

> last_cheatsheet = outputs[-1].get("final_cheatsheet")
> if last_cheatsheet is not None:
>     cheatsheet = last_cheatsheet
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The recovery protocol compares selected arguments and writes a new continued output file, then skips previously completed examples. It depends on a matching dataset order and intact JSONL/parameter files. Its guarantee strength is protocol, not transactional durability: ordinary whole-file write and parameter subset checks do not prove crash-atomic recovery or exhaustive configuration equivalence. Changing prompts through caller-selected files is manual admission at startup, with filesystem replacement as recovery; no automated machinery revision is traced. Static templates guide problem solving and curation; their own criticism/revision remains uninspected. An explicit initial cheatsheet file is admitted by file read, not validated for correctness.

### RTE-2 — Cumulative generator/curator loop

Each round pushes the entire current cheatsheet to the generator, then supplies the question, generator output and previous cheatsheet to the curator. The extracted replacement feeds the next refinement round or next benchmark question and is checkpointed. This is automatic online trace learning, both within a problem when multiple rounds are configured and across distinct problems. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:386-455`; `run_benchmark.py:254-280,308-315`. Implementation conclusion status: wired.

>                 ## STEP 2: Run the cheatsheet extraction model with the generator output and the current cheatsheet
>                 cheatsheet_prompt = cheatsheet_template.replace("[[QUESTION]]", input_txt).replace("[[MODEL_ANSWER]]", generator_output).replace("[[PREVIOUS_CHEATSHEET]]", current_cheatsheet)
> 
>                 cheatsheet_history = [{"role": "user", "content": cheatsheet_prompt}]
>                 cheatsheet_output = self.generate(
>                     history=cheatsheet_history,
>                     temperature=temperature,
>                     max_tokens=2 * max_tokens,
>                     allow_code_execution=False,
>                 )
> 
>                 # Extract the new cheatsheet from the output (if present); otherwise, return the old cheatsheet
>                 new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
>                 cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

In the shipped AIME-2024 cumulative result, the first row's final cheatsheet is included verbatim in the second row's generator prompt. This supports reported delivery, not correctness or benefit. Evidence: SRC-1 `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:1-2`. Operation conclusion status: observed, limited to that shipped transcript.

### RTE-3 — Retrieval-synthesis

For each question, select top-k earlier examples using the current precomputed vector, supply the formatted examples, previous cheatsheet and next question to the curator, then give extracted guidance to the generator. The result returns the derived guidance as final_cheatsheet for checkpoint and next-question curator input. Failure to produce an opening cheatsheet marker falls back to the retrieved-example text, not the prior cheatsheet. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:503-575`. Implementation conclusion status: wired.

>             # For RetrievalSynthesis, run the curator to synthesize a better cheatsheet
>             previous_cheatsheet = cheatsheet
>             if approach_name == "DynamicCheatsheet_RetrievalSynthesis":
>                 cheatsheet_prompt = cheatsheet_template.replace("[[PREVIOUS_INPUT_OUTPUT_PAIRS]]", curated_cheatsheet)
>                 cheatsheet_prompt = cheatsheet_prompt.replace("[[NEXT_INPUT]]", input_txt)
>                 cheatsheet_prompt = cheatsheet_prompt.replace("[[PREVIOUS_CHEATSHEET]]", previous_cheatsheet)
>                 cheatsheet_history = [{"role": "user", "content": cheatsheet_prompt}]
>                 cheatsheet_output = self.generate(
>                     history=cheatsheet_history,
>                     temperature=temperature,
>                     max_tokens=2 * max_tokens,
>                     allow_code_execution=False,
>                 )
>                 new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=curated_cheatsheet)
>                 curated_cheatsheet = new_cheatsheet
> 
>             generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", curated_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

This branch does carry prior cheatsheet content to the curator, despite the shorthand description of a custom per-query cheatsheet. Its persisted `steps[0].new_cheatsheet` is None even when synthesis succeeds; `final_cheatsheet` is the operative checkpoint field. Sampled old result rows use differing formatting and a retrieval-text fallback; they cannot silently strengthen current-code conclusions.

### RTE-4 — Cumulative plus retrieval

Similarity-ranked old pairs are appended to the whole current cheatsheet for the generator. Afterwards, the curator sees the current problem, new generator output and prior cumulative cheatsheet, then returns a replacement. It does not receive the retrieved section separately; that section can influence the new solution which it reads. This branch performs one generator/curator pass and does not loop over max_num_rounds. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:577-662`. Implementation conclusion status: wired.

>             # --- Build combined cheatsheet for the generator ---
>             combined_cheatsheet = cheatsheet
>             if retrieved_section:
>                 combined_cheatsheet = f"{cheatsheet}\n{retrieved_section}"
> 
>             # --- Generator step ---
>             generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", combined_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>             # --- Curator step: update the cumulative cheatsheet ---
>             cheatsheet_prompt = cheatsheet_template.replace("[[QUESTION]]", input_txt).replace("[[MODEL_ANSWER]]", generator_output).replace("[[PREVIOUS_CHEATSHEET]]", current_cheatsheet)
> 
>             cheatsheet_history = [{"role": "user", "content": cheatsheet_prompt}]
>             cheatsheet_output = self.generate(
>                 history=cheatsheet_history,
>                 temperature=temperature,
>                 max_tokens=2 * max_tokens,
>                 allow_code_execution=False,
>             )
> 
>             new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### RTE-5 — Direct dynamic retrieval

The shared selection path computes similarities against earlier question vectors, takes top-k indices, then pushes their full question/solution texts into generator context. Most-similar pairs are placed last. There is no curator transformation in this branch, so raw retention/retrieval here does not itself establish trace learning. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:503-528,546-575`. Implementation conclusion status: wired. The quoted selection on OBJ-3 is the same shared branch.

### RTE-6 — Full-history appending

All previous input/output pairs are formatted in order and delivered to the generator. The field name curated_cheatsheet labels a formatted replay, not a semantic curation operation. No history pruning or token-window selection is implemented here. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:457-501`. Implementation conclusion status: wired.

>                 curated_cheatsheet = "### PREVIOUS SOLUTIONS (START)\n\n"
>                 for i, (previous_input_txt, previous_output_txt) in enumerate(zip(original_input_corpus, generator_outputs_so_far)):
>                     curated_cheatsheet += f"#### Previous Input #{i+1}:\n\n{previous_input_txt}\n\n#### Model Solution to Previous Input #{i+1}:\n\n{previous_output_txt}\n---\n---\n\n"
>                 curated_cheatsheet += "#### PREVIOUS SOLUTIONS (END)"
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### RTE-10 — Prompt-directed memory maintenance and reason retention

Proposed route specialized from RTE-2, RTE-3 and RTE-4. Supplied curator templates request selecting relevant material, removing duplicates, revising approaches and introducing general strategies; whole-text replacement admits the resulting change. This establishes an invoked model-mediated curation mechanism, not guaranteed semantic success for each operation. Usage counts and prioritization remain an explicit prompt claim without a separately inspected counter or selector. Evidence: SRC-1 `prompts/curator_prompt_for_dc_cumulative.txt:13-38,48-62,93-98,128-149`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:13-53,123-146`; `dynamic_cheatsheet/utils/extractor.py:76-86`.

> Selective Knowledge Retention:
> - Preserve only high-value strategies, code blocks, insights, and reusable patterns that significantly contribute to problem-solving.
> - Discard redundant, trivial, or highly problem-specific details that do not generalize well.
> - Ensure that previously effective solutions remain accessible while incorporating new, superior methods.
> 
> Continuous Refinement & Optimization:
> - Improve existing strategies by incorporating more efficient, elegant, or generalizable techniques.
> - Remove duplicate entries or rephrase unclear explanations for better readability.
> - Introduce new meta-strategies based on recent problem-solving experiences.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> 4. Implement a Usage Counter
>    - Each entry must include a usage count: Increase the count every time a strategy is successfully used in problem-solving.
>    - Use the count to prioritize frequently used solutions over rarely applied ones.
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>     response = response.strip()
>     # <cheatsheet> (content) </cheatsheet>
>     if "<cheatsheet>" in response:
>         try:
>             txt = response.split("<cheatsheet>")[1].strip()
>             txt = txt.split("</cheatsheet>")[0].strip()
>             return txt
>         except:
>             return old_cheatsheet
>     else:
>         return old_cheatsheet
> --- `dynamic_cheatsheet/utils/extractor.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Reason retention is possible and requested: explanations, assumptions and worked examples are part of the output format. The later generator and next curator read the entire retained text, including reasons if emitted. There is no separate rationale field, invariant requiring reasons to survive, or route that specifically uses them for diagnosis. The sampled cumulative row 2 explains its subset-counting formula in prose, demonstrating retained reasons in that shipped example. Evidence: SRC-1 `prompts/curator_prompt_for_dc_cumulative.txt:24-38,48-58`; `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:2`; `dynamic_cheatsheet/language_model.py:405-435`.

The admitting memory branches RTE-2, RTE-3 and RTE-4 share RTE-10's whole-text admission and recovery semantics. Trigger and next-step owner are the Python branch scheduler; producer and semantic selector are CMP-1 under OBJ-5. Immediate return is an answer plus derived/fallback guidance. Later consumers are the generator and/or curator through RTE-1. Their local selectors use coarse full-sheet supply or embedding-ranked prior pairs, with no explicit expiry. Only selected prompt content reaches the model; full local files are not automatically visible. Activation is demonstrated only at CLM-3's bounded artifact level, not for every admitted update. The raw replay branches RTE-5 and RTE-6 return their assembled historical material as final_cheatsheet but introduce no semantic curation. Recovery depends on RTE-1 and parser fallback; old JSONL entries are not automatically restored on a semantic failure.

Guidance on RTE-10 proposes reusable solving procedures and factual examples, with mixed preservation and new conjecture. Theory-builder conditions 1–4 at this route: localized content — observed; consumption — observed in CLM-3; content-directed criticism of retained strategy — uninspected; iteration of its criticism result — uninspected. Learning attributable to criticism — uninspected. Addressability is item/function-level in text while admission replaces the whole string. Persistence reaches later rounds, questions and checkpoint continuation. The [theory-builder definition](../../../../notes/definitions/theory-builder.md) supplies these condition labels. These properties and rationale limits are expanded in the epistemic overlay; a prompt's correctness request alone is not a completed criticism.

### RTE-7 — Local execution and native interpreter alternatives

Implementation conclusion status: wired. Generator model output selects a Python block and literal flag; the wrapper runs it and returns stdout/error text in the next model context. Python owns recursion, while the model chooses the next code/answer. Local temporary files are removed; transcript strings can subsequently enter OBJ-2 and curation. Selection uses the first Python block before the flag, not a permission approval. A three-second subprocess timeout limits one execution; code executes with the process's ambient filesystem/network grants. Deployed OS isolation is uninspected. The recursive continuation warning is policy: execution happens before the depth check, so the final warned call can execute another block. SRC-1 `dynamic_cheatsheet/language_model.py:249-284`, `dynamic_cheatsheet/utils/execute_code.py:28-59,75-99`.

> process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
> stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> executed_code = extract_and_run_python_code(output_prefix)
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Native interpreter selection disables local execution in advanced_generate. With a container/sentinel, generate calls provider tooling; OpenAI passes a reusable container ID, while Claude passes a code-execution tool. Immediate return is provider text. Native selection, retained payloads, expiry and execution isolation remain provider contracts, not repository-enforced guarantees. No interpreter container means the native branch is not entered. SRC-1 `dynamic_cheatsheet/language_model.py:157-172,212-234,347-349`, `text_generation/simple_unified_client.py:1128-1153,1191-1210`.

> tools=[code_execution_tool],
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Changes admitted here are model-proposed executable work, authorized by caller flags and marker parsing; there is no content-based veto before local execution. Error text can guide another attempt, but rollback of external code effects is not provided by deleting the script. Guidance is OBJ-5 plus selected memory; whether a particular generated repair criticizes a theory requires its trace. Tool text is not automatically an answer oracle. Provider calls retry exceptions three times with a fixed ten-second delay, then raise; retries do not certify idempotent effects. SRC-1 `text_generation/simple_unified_client.py:395-431`.

Additional memory detail: Local code output is appended to the conversation and accumulated final output. Subsequent generator continuation reads the result; curator branches later consume that same accumulated output. Temporary scripts run in new subprocesses and are removed, so this is retained text feedback, not a persistent Python variable namespace. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:249-288`; `dynamic_cheatsheet/utils/execute_code.py:75-101`. Implementation conclusion status: wired.

>                 current_output = f"{output_prefix}\n{code_execution_flag}\n\n{executed_code}"
>                 final_output = f"{final_output}\n\n{current_output}".strip()
> 
>                 # If we haven't exceeded the max depth, prompt the model to continue
>                 if current_depth <= max_depth_num_rounds:
>                     warning_txt = ""
>                     if current_depth == max_depth_num_rounds:
>                         warning_txt = " (This is the last round. No more code execution will be allowed. Please present your final solution now.)"
>                     new_messages = [
>                         {"role": "assistant", "content": current_output},
>                         {"role": "user", "content": f"Proceed with any additional steps required and provide the completed solution. If everything is already complete, type FINAL ANSWER and submit it in the expected format. If you are stuck, please try alternative methods to solve the problem and provide the final solution.{warning_txt}"}
>                     ]
>                     history += new_messages
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`



### RTE-8 — Default solving branch

Implementation conclusion status: wired. advanced_generate with approach default substitutes an empty cheatsheet, sends a user message to CMP-1, optionally follows RTE-7, extracts the answer and returns final_cheatsheet None. No accumulated cheatsheet selector, curation or later memory consumer is wired on this branch; the enclosing runner may still record raw output. Immediate answer return is the purpose. No expiry applies. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:351-384`.

> generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", "(empty)")
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### RTE-9 — Benchmark answer scoring

Implementation conclusion status: wired. After the generated answer and new cheatsheet already exist, Python evaluates the final answer. AIME exact matching and multiple choice consume dataset targets supplied by the dataset author; Game of 24 checks the numerical target 24 and supplied input-number usage; equation balancing compares the prescribed numbers/result. These are answer oracles for the bounded benchmark mode. They do not enter the generator/curator call arguments or gate retention. The result changes printed counters; it cannot veto a cheatsheet. No later score read-back, delegation, expiry or memory selector applies. SRC-1 `run_benchmark.py:253-309`, `dynamic_cheatsheet/utils/evaluation.py:47-81,102-112,151-170,173-240`.

> result = eval_for_exact_matching_with_no_punctuation(final_answer.lower(), original_target.lower())
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> if result:
>     correct_so_far += 1
> total_so_far += 1
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The scoring contract is a programmatic check within its encoded task/format, not proof of explanations or general strategies. In particular eval executes returned expressions; the local-code flag does not disable this evaluator path. The intended numeric check is not an isolation guarantee.

### Claims

### CLM-1 — Adaptive memory and performance claim

Conclusion status: claimed. README says inference-time memory improves performance without labels or human feedback and without modifying model parameters. Wiring supports the separate label-free curator path; benchmark evaluation does use targets. Quantitative performance and causal explanations remain README claims here because the selected trace does not reproduce the benchmark comparison. SRC-1 `README.md:13-28`.

> * **Zero-Shot Learning**: Improves performance without ground-truth labels or human feedback
> --- `README.md` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CLM-2 — Correctness-oriented curation

Conclusion status: claimed. The prompt requests assessing a solution before incorporating it and preserving tested useful methods. This is a model instruction with best-effort strength. The parser admits the returned text without independent correctness validation. SRC-1 `prompts/curator_prompt_for_dc_cumulative.txt:18-25`, `dynamic_cheatsheet/utils/extractor.py:76-86`.

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CLM-3 — Shipped repeated-puzzle trajectory

Conclusion status: observed. ExampleUsage runs the same 5, 6, 6, 8 puzzle with an initially empty sheet, then with the first and second retained sheets. The first displayed sheet states an invalid arithmetic example. The next call implements an enumerative Python solver, receives `6 - ((5 - 8) * 6)`, and saves the algorithm and corrected example; the third output states a plan to implement that algorithm and repeats the successful tool result. This is retained artifact evidence of reuse and a local answer improvement, with an explicit content-to-plan link. It is not a controlled intervention, general transfer result or proof that the correction arose from criticism of the old strategy. Notebook cell indices here are zero-based. SRC-1 `ExampleUsage.ipynb`, source cells 4, 6, 8, 10, 12 and output cells 5, 7, 9, 11, 14.

> Implement the algorithm from the cheatsheet to systematically test all permutations, operator combinations, and parenthesized groupings.
> --- `ExampleUsage.ipynb:466` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> (8 / (6 - 5)) * (6 + 6) = 24
> --- `ExampleUsage.ipynb:142` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> 6 - ((5 - 8) * 6)
> --- `ExampleUsage.ipynb:517` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CLM-4 — Retained content need not be correct

Conclusion status: observed. The second record of the shipped AIME 2024 Claude cumulative artifact contains a sheet asserting that 2024 equals 2^11. That is false by ordinary arithmetic. Its target is 55 and final answer 11. This one artifact establishes neither a system-wide error rate nor the absence of other successful criticism; it demonstrates that retention and a usage count are not correctness certification. SRC-1 `results/AIME_2024/claude-3-5-sonnet_DynamicCheatsheet_Cumulative.jsonl:2`.

> "new_cheatsheet": "Version: 2.0\n\nSOLUTIONS, IMPLEMENTATION PATTERNS, AND CODE SNIPPETS\n\n<memory_item>\n<description>\nGeometric Pattern Recognition in Regular Polygons (Reference: Q1)\nWhen dealing with regular polygons and counting geometric patterns:\n1. Identify symmetry properties (rotational, reflectional)\n2. Look for parallel and perpendicular relationships\n3. Use symmetry to reduce the problem size\n4. Multiply final count by symmetry factor\n</description>\n<example>\nFor regular dodecagon rectangle counting:\n- Identify basic constraints (sides must lie on edges/diagonals)\n- Use rotational symmetry (12-fold) to reduce counting\n- Look for parallel/perpendicular line pairs\n- Total = (unique configurations) \u00d7 (symmetry factor)\n</example>\n** Count: 1\n</memory_item>\n\n<memory_item>\n<description>\nPower-Based Set Counting (Reference: Q2)\nWhen counting sets with specific maximum element constraints:\n1. For each maximum element k, count possible subsets\n2. Use power of 2 properties for binary choices\n3. Look for patterns in powers that sum to target\n4. Consider binary representation of target number\n</description>\n<example>\nFor sets B with max element k from set A:\n- Each element < k: 2 choices (in/out)\n- k must be included\n- Total sets with max k = 2^(k-1)\n- Sum of 2^(k-1) across all k in A gives total count\nExample: If target = 2024 = 2^11, then A = {11}
> --- `results/AIME_2024/claude-3-5-sonnet_DynamicCheatsheet_Cumulative.jsonl:2` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### CLM-5 — Delivery and outcome evidence do not isolate recall dependence

Proposed bounded evidence claim. README performance claims, recorded benchmark outputs and notebook repeated-problem demonstrations concern outcomes. The inspected evaluation notebook scores final answers; it does not perturb recalled content while controlling other inputs. ExampleUsage repeats the same question with successive cheatsheets, and its third output describes following cheatsheet guidance, but that self-report does not isolate a causal memory effect. Evidence: SRC-1 `README.md:23-28`; `run_benchmark.py:290-309`; `ExampleUsage.ipynb`; `EvaluatingResults.ipynb`. Claim conclusion status: observed for the presence of these shipped demonstrations, not causally supported for faithfulness. Faithfulness classification remains not determinable because these samples do not establish a complete negative over every retained output.



### Evidenced absences

### ABS-1 — Benchmark score is not a memory-admission gate

Conclusion status: absent. Searched boundary: SRC-1 at the reviewed commit, full `run_benchmark.py` and `dynamic_cheatsheet/utils/extractor.py`, plus all advanced_generate branches in `dynamic_cheatsheet/language_model.py`. Query `target|result|eval_|curator|cheatsheet` on runner/extractor was followed through the call arguments, post-call score and parser return. No benchmark target or score reaches the curator or decides parsed-sheet adoption within this boundary. RTE-9 quotes anchor the ordering; RTE-2, RTE-3 and RTE-4 anchor admission. This does not exclude model reasoning or self-generated computational tests; it prevents calling benchmark correctness an enforced memory gate.

No additional evidenced absences are needed for the comparison profile; uncertain native state and faithfulness remain limitations.

### Behavioral-authority paths

### BAP-1 — Reference guidance to model consumers

Implementation conclusion status: wired. Consumers are generator and curator CMP-1; channel is user-message text assembled by RTE-2, RTE-3, RTE-4, RTE-5 and RTE-6. Force is advisory knowledge, with applicability checks requested by OBJ-5. Horizon is the next solving/curation call and subsequent calls receiving retained output. OBJ-1 and OBJ-2 carry operational influence but no general epistemic endorsement. Evidence and quotations: OBJ-1, OBJ-2, RTE-2, RTE-3, RTE-4 and RTE-6. CLM-3 supports observed reuse on the repeated puzzle; general activation remains uninspected.

### BAP-2 — Embeddings determine selection

Implementation conclusion status: wired. Consumer is the wrapper's top-k selector; channel is imported numeric arrays; force is ranking; horizon is each current question's selection from earlier examples. OBJ-3's cosine selection quotation establishes the path into RTE-3, RTE-4 and RTE-5. Ranking grants no epistemic warrant.

### BAP-3 — Execution feedback and action permission

Implementation conclusion status: wired. Caller flags and marker parsing permit model-generated execution through RTE-7. Tool stdout/errors reach the generator as conversation text and later the curator through OBJ-7 and OBJ-2; their force is evidence/advice within the next attempt, not truth certification. The local host grants actual execution authority; native permissions are external contracts. Persistence beyond the active trace follows RTE-1. Evidence and quotations: RTE-7 and OBJ-6.


## Runtime account

An operator launches RTE-1 or calls advanced_generate directly. The runner binds a task and model configuration, loads prompts, restores or initializes memory, and invokes one approach for each problem. CMP-1 proposes the answer and optional tool work; Python fixes the branch sequence. RTE-7 supplies execution feedback. The selected memory route prepares or replaces the sheet. RTE-9 scores the final answer after that update, and RTE-1 retains output for the next example. The terminal product is an answer plus inspectable prompts/steps and final memory, with JSONL/parameter files on the benchmark path. There is no sub-agent scheduler: generator and curator are sequential roles of the same configured wrapper.

All six approaches were inspected. The default branch is RTE-8; cumulative curation is RTE-2; retrieval synthesis is RTE-3; hybrid is RTE-4; raw retrieval is RTE-5; full historical context is RTE-6. Ordinary Python execution and the OpenAI/Claude native alternatives are distinguished on RTE-7. Public API calls can solve open requests, while the shipped runner processes bounded datasets; human callers can also repeat the same problem, as CLM-3 does. Only the benchmark scoring path has the supplied reference targets. A curator's own confidence does not imply an answer oracle.

Forcing cases were inspected statically: (1) an empty history selects empty context; (2) a missing cheatsheet marker preserves fallback content while a returned marker admits text; (3) a code block on the last warned recursive call still reaches execution before the recursion check; (4) a continuation restores the last sheet/output prefix subject to selected argument checks. No dynamic check planned. Live model calls were not authorized; static control flow suffices for these wiring findings. Local execution probes would not establish model criticism, provider behavior or causal learning. No source execution was attempted.

Role allocation is explicit: the human sets prompts/model/mode and may initialize or edit imported memory; the generator proposes solutions and executable actions; the curator proposes memory text and selects what to keep under natural-language guidance; the parser decides syntactic admission; Python owns scheduling and persistence; benchmark evaluators judge answer formats/outcomes but cannot veto curation. Blame assignment by a model is uninspected unless a retained trace states it. Automated source-code, prompt-policy, model or provider replacement by the workflow is uninspected, and not inferred from generated Python work products.

## Lens scoping

### Memory/context scope

Full depth, triggered by OBJ-1, OBJ-2, OBJ-3 and RTE-1 through the individually named branches RTE-2, RTE-3, RTE-4, RTE-5, RTE-6 and RTE-7. Scope is accumulated memory, derived sheets, access structures, continuation and native execution state. Static templates are separate. The independent specialist owns this analysis and comparison profile; source seeds did not include accepted classifications.

### Epistemic scope

Full depth. CLM-1 and CLM-2 make consequential learning/correctness claims, while OBJ-1 and OBJ-4 contain truth-apt statements and RTE-9 checks outcomes. Assess generator production, curator transformation, parser admission, retention, retrieval, execution feedback and answer scoring at the same frozen boundary. Provider reasoning and unobserved candidate-level criticism remain uninspected. The local epistemic procedure supplies a sparse overlay on the canonical register below.

## Lens outputs

### Memory/context lens

The specialist inventoried OBJ-1, OBJ-2, OBJ-3, OBJ-6 and OBJ-7 across RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7 and RTE-10. All fourteen profile axes above are adopted with their per-value bases and coverage notes. Cumulative, synthesis and hybrid branches automatically turn trajectories and optional tool traces into retained prose/code guidance: online trace learning in the comparison's defined sense. Configured cumulative rounds operate per problem; sequential benchmark questions establish cross-task scope. This does not establish capacity improvement.

Read-back is automatic push to named model consumers. Coarse whole-sheet/all-history supply differs from embedding selection of earlier problem/solution pairs. Curator judgment transforms supplied content; it is not separately evidenced as an inferred-judgment retrieval selector. File names, question labels, positional alignment and container IDs do not by themselves establish identifier-based push. The default branch supplies no accumulated sheet, but can still use RTE-7's in-progress history or opaque native state.

The local operative substrates are files and process memory, plus an exposed native service object. Forms are prose and symbolic code/access arrays. Provider-native payloads prevent exhaustive coverage, preserved as partial assessments. Embedding producer identity remains unknown. Seed loading supports imported lineage, not an inferred manual authoring route. Retained reference material is advisory knowledge; embeddings carry ranking authority. Static method instructions are excluded from accumulated-memory authority.

Whole-text evolution, consolidation, deduplication and synthesis are wired as model-mediated operations under invoked templates, without semantic guarantees. Usage-based promotion is only claimed; there is no verified counter/selector. Input context is not clipped locally: whole history grows with earlier outputs, cosine selection scans previous vectors, and top-k does not impose a selected-pair token budget. Curator output limits and requested word counts are not a context-window guarantee.

RTE-3 consumes a previous sheet and falls back to retrieved text; it is not stateless. RTE-4 performs one pass despite max_num_rounds. Checkpoint continuation restores text and output history, while native session initialization creates a fresh container; selected argument checks do not verify dataset/embedding identity. RTE-10 retains rationale when emitted and supplies it wholesale later, but has no separate rationale-survival invariant. CLM-5 preserves the faithfulness uncertainty. None of these findings depends on opening the local report.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1 and the frozen whole-workflow boundary. The question is what the workflow checks and what retained strategies are licensed to claim. Assessed families: solving, execution, curation, syntactic admission, historical retrieval, continuation and benchmark scoring. Unassessed families: provider internals and external dataset construction; these prevent attribution to particular weights, internal reasoning or ground-truth reliability. The claim targets are CLM-1 and CLM-2, with observed counterweight CLM-4 and local positive evidence CLM-3.

#### 2. Epistemic-object inventory

| object | truth-apt content and lineage | producer/consumer and warrant limit |
|---|---|---|
| The object OBJ-1 | Mixed advice, algorithms, examples and generalizations derived from prior model work; source-native identity/form/storage: see OBJ-1 | Curator to later generator/curator. Truth-apt algorithmic claims coexist with task policy; tag extraction does not warrant either. |
| The object OBJ-2 | Prior problem/solution statements and tool results; see OBJ-2 | Generator history becomes curator/generator input. Its provenance identifies earlier model work, not correctness. |
| The object OBJ-3 | Similarity access data; see OBJ-3 | Retrieval ranks historical material. Geometric similarity does not license answer validity. |
| The object OBJ-4 | Current candidate mathematical answer and reasoning; see OBJ-4 | Model proposes, local code or benchmark evaluator may test a limited consequence. Test scope differs from explanatory warrant. |
| The object OBJ-5 | Prescriptive solving/curation procedures; see OBJ-5 | Human-authored method guidance. No observed internal revision of these files. |

| The object OBJ-6 | Native service payload is opaque; identity/interface: see OBJ-6 | Provider tool operations can reuse a service object, but truth-apt content, update relation and warrant are not determinable. |
| The object OBJ-7 | In-progress generated code and execution output; see OBJ-7 | Generator consumes local feedback and curators later receive the accumulated text; execution does not warrant every narrated claim. |

#### 3. Authority-route ledger

All rows below have architectural status `implemented` unless stated otherwise. Generic endpoints and progression remain on the named route. Each row supplies one consequential function. Operational force means what can affect later behavior; epistemic force is narrower.

| route | function | content/update relation and target | evaluator/condition, timing and result | epistemic authority | operational/behavioral consequence and limit |
|---|---|---|---|---|---|
| The route RTE-2 | content transformation | Truth-apt transformation: indeterminate across arbitrary sheets; candidate generalization, reshaping and correction are all possible | CMP-1 receives old sheet/current question/generated work after solving; model returns proposed replacement under CLM-2 | Model judgment only; no independently checked premises or entailment | Proposed OBJ-1 may shape later solving through the memory authority paths; no enforced semantic fidelity |
| The route RTE-3 | content transformation | Truth-apt transformation: indeterminate; selected past work and current query guide a synthesized sheet | Curator runs before generator, conditioned on retrieval and prior sheet | Query relevance and requested quality are not verified truth | Candidate OBJ-1 delivered for this problem and retained for subsequent calls |
| The route RTE-4 | content transformation | Same qualified relation as RTE-2, with retrieved examples in solving context | Curator sees generated work and old sheet after answer | No outcome-score feedback | Candidate sheet replaces prior one under parser admission |
| The routes RTE-2, RTE-3, RTE-4 | disposition/acceptance | No content change: choose parsed text or fallback | Extractor accepts a marker-delimited substring; missing marker chooses fallback | Syntactic admission only; no recorded evidence-consuming acceptance of every strategy | Installs whole candidate as next sheet. No semantic veto or per-entry endorsement follows |
| The route RTE-1 | retention | No content change | Python stores final sheet/output and later restores them | Warrant preserved only at original strength | Retention supports continuity; it is not post-acceptance lifecycle integration |
| The routes RTE-5, RTE-6 | operational admission/selection/consumption | No content change apart from formatting | Cosine top-k or entire available history, before generator | No added warrant from relevance or availability | Selected OBJ-2 enters user context; model can adapt or ignore it |
| The route RTE-7 | check/evidence production | Candidate code/answer consequences; no automatic semantic relation for arbitrary code | Python or provider executes proposed work; output/error returned to generator | Execution text supports what that code returned in its environment, not correct problem encoding | Can trigger a revised attempt; no independent semantic approval of subsequent sheet |
| The route RTE-9 | check/evidence production | No content change: current final answer is scored | Task evaluator/target after memory update | Outcome fit under task/format contract only | Counter reporting; score cannot veto already-produced memory |
| The route RTE-8 | content transformation | Truth-apt transformation: indeterminate | Generator produces answer from task and static instructions | No added warrant without a check | Returns answer, with optional RTE-7 feedback; no curation |

#### 4. Per-object lifecycle disposition

For OBJ-1 the aggregate transformation is **indeterminate**. The sampled sheet contains both reusable strategy proposals and restatements. Neither all-preserving compaction nor all-ampliative conjecture is justified. Its implemented checks are model-instructed review and parser admission, followed by retention/use. CLM-3 supplies observed revision and later use, but no candidate-linked semantic acceptance record for the algorithm as a generally reliable method. A trace naming the precise proposed claim, criticism, resulting revision and acceptance criterion would resolve its lifecycle. No blanket discovery-lifecycle attribution is made from storage.

For OBJ-2: acquisition/import and non-ampliative formatting of prior work. Discovery lifecycle: not applicable to this copying route; source truth and any original derivation remain at their prior warrant. For OBJ-3: access metadata with no candidate truth-apt output in the reviewed retrieval operation. No lifecycle record for OBJ-3: no candidate truth-apt output for this object; relevant direct-adaptation or update routes are RTE-3, RTE-4 and RTE-5.

For OBJ-4: transformation is indeterminate across all answers. The notebook's candidate expression is directly tested by the displayed enumeration/returned result; architectural status `implemented`, observed candidate state `phase evidenced` for computation and answer production. That local arithmetic test does not establish a discovery lifecycle for the general solving method. The displayed final expression and later repeat are `phase evidenced` as outputs; acceptance of a general strategy remains `not determinable`. For OBJ-5, no candidate truth-apt output is produced by its static loading operation; relevant routes are RTE-1 and the model branches. Static method use is not method criticism.

For OBJ-6, transformation and candidate truth-apt content are **indeterminate**: the interface identifies service state but does not expose its operative parts. Architectural status is `implemented` for interface reuse and `not determinable` for internal checks/acceptance; observed candidate state is `not determinable` for any hidden candidate phase. Provider payload/trace evidence would be needed. For OBJ-7, local acquisition of executed code/output and transcript accumulation is non-ampliative retention; discovery lifecycle is not applicable to copying this feedback. A model's interpretation or later conjecture belongs to OBJ-4 or OBJ-1, not automatically to the transcript carrier.

#### 5. System-claim versus route comparison

CLM-1 has code support for inference-time retained context through the memory routes and one observed same-puzzle trajectory in CLM-3. Quantitative cross-task improvement and fine-grained causal attribution are uninspected here. CLM-2 is implemented as prompt guidance, not a correctness invariant. CLM-4 exhibits an admitted false statement, so a claim that all retained items are verified is not supported. This does not refute the narrower possibility of useful automatic curation or individual successful checks.

#### 6. Bounded conclusion

The workflow produces and reuses model-generated candidate strategies, and its callable execution and benchmark paths can check bounded answer consequences. Retrieval preserves previous provenance without upgrading warrant. The retained sheet has operational authority through model context but lacks universal epistemic endorsement. The generator may follow remembered algorithms, as CLM-3 shows; whether an arbitrary generalization was criticized or accepted remains a candidate-level question. The following property findings remain distinct from memory comparison axes.

**Theory-builder conditions 1–4:** (1) localized content — observed in the notebook's explicit strategy and code; (2) consumption — observed through the stated plan and matching executed implementation in CLM-3, beyond mere citation; (3) content-directed criticism of retained strategy — uninspected in the selected traces: prompt instructions request checking and actual arithmetic work is tested, but the transition from old strategy to new does not state a refutation of the old strategy; (4) criticism-result iteration — uninspected for that strategy path, despite observed replacement and later reuse. Consequently theory-builder membership is uninspected at the generalized memory-method boundary, not evidenced absent. Candidate-expression testing inside generated code must not silently substitute for criticism of the surrounding method.

Addressability is observed at prose-item and code-function granularity; assumptions and scope sometimes appear, but the runtime updates the whole sheet. Persistence is wired across problems and continued runs and observed across repeated notebook calls. Rationale is partially preserved in worked examples and explanations; the notebook's later plan consumes algorithmic content. Historical rationale for each curation decision is not required by the extractor and not established by those examples.

**Learning:** observed local answer improvement and subsequent correct repeated use in CLM-3 are the strongest retained contribution. Capacity improvement attributable to criticism of a consumed theory remains uninspected: the notebook lacks a controlled comparison and explicit criticism-to-revision trace. CLM-1's broader benchmark improvement remains claimed. A change of answer and retained code alone does not settle that stronger attribution.

**Reflection:** wired for the selected aspect of the workflow's own solving procedures: generator work updates the sheet, and the sheet informs later generator procedures. CLM-3 gives observed procedure reuse, while exact causal contribution remains limited by its observational design. This narrow self-representation does not establish reflection over the runner, model selection, critic standards or source machinery. Reflective theory-builder qualification remains uninspected because method-directed criticism and its iteration are unresolved.

**Autonomy:** proposal, transformation, syntactic admission, scheduling, code execution and persistence are computational after human configuration. A theory-builder autonomous qualifier is uninspected because the complete theory-builder route is unestablished, not because human-supplied problems would disqualify it. **Self-improvement:** a dispositional improvement-directed memory pathway is wired; the objective is improved later solving through useful retained strategies. CLM-3 supplies observed operative reuse after a useful local update. Strong occurrent causal attribution of the full evidence-responsive self-change chain remains uninspected at the declared workflow boundary; numerical benchmark success is not a substitute for that chain.

## Reconciliation

The specialist's exact frozen input identity, source identity/revision, complete status, method hash and final report hash were checked. Shared source verification returned 52 successful checks on its final bytes. Canonical seed identities remain unchanged.

Proposal mappings: MEM-OBJ-1 → OBJ-6; MEM-OBJ-2 → OBJ-7; MEM-RTE-1 → RTE-10; MEM-CLM-1 → CLM-5. Each mapped target is declared once and is distinct. The in-progress execution object OBJ-7 supplements current answer OBJ-4: the former is the recursion/history carrier, the latter is the returned task candidate. RTE-10 specializes admission/maintenance already used by the branch routes rather than inventing a second execution schedule.

All specialist issues are adopted: native payload uncertainty, unidentified embedding producer, prior-sheet input and retrieved-text fallback on RTE-3, single-pass RTE-4, text-only continuation versus new native container, weaker promotion evidence, and historical artifacts distinct from current execution. Shared RTE-1 and RTE-7 records retain their generic identity and incorporate specialist memory details. The specialist sampled GPT-4o AIME artifacts; the coordinator independently sampled Claude artifacts and the notebook. Their agreement on delivery and lack of a benchmark admission gate is independent convergence, not two copies of one report.

No substantive specialist conflict required reanalysis. No source endpoints, ranges, report prose or report bytes were changed by the coordinator. Exact-token mappings affect only this integrated result. Duplicate supporting quotations were retained once per canonical evidence passage. Faithfulness remains not determinable even though CLM-3 supports observed content-dependent procedure use: that observation does not isolate recall causally. No known profile value was strengthened during integration.

## Bounded synthesis

Dynamic Cheatsheet is a sequential generator/curator workflow with pluggable inference providers and optional executable work. The benchmark runner supplies accumulation, recovery and scoring; the callable wrapper supplies approach-specific context assembly and updates. These responsibilities explain why a returned cheatsheet becomes memory only when a later call consumes it.

The discriminating choice is between preserving all previous solutions, selecting them by embedding similarity, and rewriting a compact reference through another model call. The hybrid combines a cumulative reference and selected examples. Model curation can carry more transferable guidance than raw answers, but marker extraction and requested correctness leave substantial judgment to the model. Supplied benchmark targets affect scoring, not admission of the next sheet.

The strongest concrete positive result is the shipped notebook's transition to a tested algorithm and later reuse on the same puzzle. Its scope is that retained trajectory. Broad improvement, theory criticism, faithful recall and general transfer need their own evidence. The admitted false AIME sheet illustrates why no correctness guarantee follows from the curation vocabulary. Theory-builder conditions, learning, reflection, autonomy and self-improvement have separate dispositions in the epistemic lens; none is inferred from a positive trace-learning comparison value.

For sequential benchmark use, the implementation exposes useful records and restart inputs. For deployments requiring isolation, verified advice or provider-independent behavior, the boundary does not establish those guarantees: local execution inherits ambient permissions and native tools depend on opaque contracts. Fresh candidate-linked criticism traces, counterfactual memory-use comparisons, native-state inspection and an explicit semantic admission gate would materially change those assessments.

## Limitations

| limitation | affected records | inspected boundary | conclusion prevented | evidence that would resolve it |
|---|---|---|---|---|
| No new runtime execution | CMP-1, RTE-7 | Pinned static code and shipped artifacts | Current provider behavior and fresh causal reproduction | Authorized reproducible run with pinned configuration |
| Limited historical artifact sample | CLM-3, CLM-4 | Notebook and two AIME result rows | Whole-corpus error rates or generalization | Full experimental design and controlled comparisons |
| Hidden model processing | CMP-1, RTE-2, RTE-3, RTE-4 | Prompt inputs and retained outputs | Whether omitted criticism occurred or caused revision | Candidate-linked criticism/revision trace |
| Provider-native state opaque | RTE-7 | API call boundary | Complete memory profile and deployed isolation | Provider-state evidence and retained tool traces |
| Dataset/provider provenance excluded | RTE-9, CMP-1 | Repository-side usage | Ground-truth validity, model fixity and contamination | Pinned provider/dataset provenance |

## Verification and blockers

### Semantic verification

Checked profile scope against OBJ-1, OBJ-2, OBJ-3, OBJ-6 and OBJ-7 and all six branch routes. Opaque native payloads remain included and partial; the known positive trace-learning boolean is supported existentially by RTE-2, RTE-3 and RTE-4. Each qualifying trace-fed write is accounted for: cumulative per-task/cross-task, retrieval-synthesis cross-task, hybrid cross-task; all online, with trajectory/tool-trace inputs and prose/code outputs. Raw replay in RTE-5 and RTE-6 is not substituted for derivation. There is no additional inspected compaction route.

Checked every push claim: BAP-1's whole retained reference/all-history supply is coarse; BAP-2's current-vector top-k selection delivers identified prior problem/solution pairs by inferred embedding. Numeric corpus alignment and container identity are not additional identity-based push. CMP-2 remains unresolved. The profile preserves per-value evidence and every mapped record resolves. Model-mediated curation is distinguished from semantic success, and observation from causal attribution. Route ownership, answer-oracle timing, theory-builder conditions and learning are separately stated. The retained result includes specialist evidence and does not require its local report to interpret a finding.

### Deterministic validation

Validation targets are this exact result and its frozen-source anchors. `commonplace-validate --full` passed cleanly. Shared `commonplace-agentic-analysis-publication verify-sources` passed. Final-byte checks are repeated before publication. The specialist report passed both structural validation and shared verification (52 source checks), with identity/hash checks matching the frozen input and current memory instruction. Source occurrence checks do not certify semantic warrant.

### Blockers

none
