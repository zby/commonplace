---
type: types/agentic-system-analysis-result.md
description: "Dynamic Cheatsheet at the frozen September 2026 code boundary: local adaptive memory, execution paths, and limits of improvement evidence"
run-id: AAS-2026-09-26-dynamic-cheatsheet-01
system: Dynamic Cheatsheet
run-date: "2026-09-26"
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9
analysis-cutoff: "2026-09-26"
evidence-tier: code-grounded
memory-comparison:
  scope: "Local accumulated cumulative and query-conditioned cheatsheets, prior input/output traces, imported access embeddings, initialization and benchmark checkpoint restoration across all five memory approaches and cumulative within-question refinement. Excludes static templates, pretrained model weights, remote code-interpreter payloads and unwired general chat conveniences; their consequences are stated in the report."
  axes:
    storage_substrate:
      assessment: known
      basis: wired
      values: [files, in-memory]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-8, RTE-6]
      note: "Python strings/lists/arrays are operative in memory; CSV, initialization text, JSONL and parameter JSON supply file persistence. Numeric vectors do not establish a vector database."
    representational_form:
      assessment: known
      basis: wired
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-8, CLM-3]
      note: "Readable explanations coexist with code snippets, numeric vectors and structured checkpoints. No inspected local learned weights; remote opaque payloads are expressly excluded."
    lineage:
      assessment: known
      basis: afforded
      values: [authored, imported, trace-extracted, other-compiled]
      records: [OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-8, RTE-2, RTE-4, RTE-5, RTE-6]
      note: "Human-provided initialization is afforded; embeddings and seed sheets are imported; curators extract from generated solution traces; history/retrieval formatting and checkpoint serialization compile retained content without semantic learning."
    behavioral_authority:
      assessment: known
      basis: wired
      values: [knowledge, ranking]
      records: [BAP-1, BAP-2, OBJ-3, RTE-3]
      note: "Sheets and examples are reference guidance, even when phrased imperatively; vector similarity ranks examples. Static binding prompts and execution of newly generated code are outside the memory authority profile."
    write_agency:
      assessment: known
      basis: afforded
      values: [automatic, manual]
      records: [RTE-2, RTE-4, RTE-6]
      note: "Curator replacement and checkpoint writing are automatic; caller-provided strings and initialization files afford manual seed/adoption. No dedicated memory editor is shipped."
    curation_operations:
      assessment: known
      basis: claimed
      values: [consolidate, decay, dedup, evolve, promote, synthesize]
      records: [RTE-2, RTE-4, CLM-4]
      note: "Shipped curator instructions request reduction, forgetting selected trivial details, duplicate removal, revision, usage-based prioritization and new general strategies. This is the requested operation set, not guaranteed successful execution; no explicit invalidation protocol is found."
    read_back_direction:
      assessment: known
      basis: wired
      values: [push]
      records: [RTE-1, RTE-3, RTE-4, RTE-5, RTE-6]
      note: "Controller/curator selection supplies context to generator and curator without their requesting memory. Initialization and resume are upstream operator choices feeding this push route; file I/O is not a separate model-requested recall interface."
    read_back_signal:
      assessment: known
      basis: wired
      values: [coarse, inferred-embedding, inferred-judgment]
      records: [RTE-1, RTE-3, RTE-4, RTE-5, RTE-6]
      note: "Whole current sheets/history and restored latest sheet use coarse selection; cosine similarity targets examples; query-conditioned curator judgment selects the synthesized material delivered to the generator."
    trace_learning:
      assessment: known
      basis: wired
      values: ["yes"]
      records: [RTE-2, RTE-4, RTE-6]
      note: "Automatic solution-trace transformation produces sheets retained for later generator/curator consumers. Raw retention alternatives alone do not qualify."
    trace_source:
      assessment: known
      basis: wired
      values: [trajectories, tool-traces]
      records: [OBJ-2, RTE-2, RTE-4, RTE-7]
      note: "Problem-solution trajectories include model reasoning and optionally appended local Python execution output; remote tool internals are not included."
    learning_scope:
      assessment: known
      basis: wired
      values: [per-task, cross-task]
      records: [RTE-1, RTE-2, RTE-4, RTE-6]
      note: "A task means an individual problem to solve: cumulative rounds revise within that task; benchmark sequencing transfers sheets between distinct problems in one dataset. No autonomous transfer across benchmark families or projects is established."
    learning_timing:
      assessment: known
      basis: wired
      values: [online]
      records: [RTE-2, RTE-4, RTE-6]
      note: "Curators run in the live problem sequence, after the cumulative answer or before the retrieval-synthesis answer. Saving/restoring is not a separate offline learning stage."
    distilled_form:
      assessment: known
      basis: wired
      values: [natural-language, symbolic]
      records: [OBJ-1, OBJ-4, RTE-2, RTE-4, CLM-3]
      note: "Qualifying curator routes retain explanatory prose and may retain Python code; symbolic does not mean parametric learning."
    faithfulness_tested:
      assessment: not-determinable
      basis: null
      values: []
      records: [CLM-3, CLM-2]
      note: "Inspected paired checkpoint rows establish delivery and answer errors, not recalled-content dependence. README outcomes and the evaluation notebook do not identify a controlled candidate-linked intervention. Broader results are not exhaustively assessed."
---

# Dynamic Cheatsheet agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-01/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/dynamic-cheatsheet.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-01/memory-report.md`

**Memory analysis report SHA-256:** c0a67a97dd56d0b79c84eaa018c16f19ac89f1100f500ced51c06454efba97a0

Run opened on 2026-09-26. Repository default branch `main` resolved to the reviewed full commit. Destination inspection returned expected incumbent `absent`. This document declares completed analysis content; the run state declares publication. No prior system analysis, legacy review or comparison classification supplied these findings.

## Boundary and evidence

**Evidence basis:** pinned implementation and prompts, source-reported performance, and four sampled retained output rows, inspected on 2026-09-26. No live model or benchmark execution was performed.

Dynamic Cheatsheet is an inference-time memory mechanism and sequential benchmark workflow. The selected boundary includes `LanguageModel`, all six approach branches, shipped prompts, answer extraction, local Python execution, provider call paths reached by this wrapper, and benchmark sequencing, scoring and checkpoint recovery. It is a complete repository artifact with a partial external loop: hosted model inference and remote tool environments remain externally owned. Direct Python invocation and the CLI benchmark are both included. Operator-chosen alternative prompts are an extension surface whose content is not supplied; conclusions about prompt semantics apply to shipped templates.

The local memory comparison includes cumulative and query-conditioned sheets, prior input/output traces, imported access vectors, manual seed adoption and checkpoint restoration. Static instructions and pretrained weights are not accumulated local memory. Remote interpreter state is explicitly excluded from the comparison while retained as OBJ-9 and RTE-9 in the runtime account. Therefore the known local substrate values do not describe all possible remote persistence.

Excluded provider implementation prevents claims about exact weights, tool isolation or complete remote traces. Excluded embedding generation prevents identifying its model or training. External live paper and uninspected experiment configurations prevent reproducing reported performance or attributing it to individual mechanisms. General chat/history and web-search conveniences in the provider client, outside the wrapper's ordinary call path, are excluded; no assertion about their memory behavior follows. Source notebooks contribute specialist-read documentation, not experiment outputs. Binary datasets and the wider result corpus were not exhaustively inspected.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git implementation | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Implementation | Wrapper 1–668; runner 1–327; extractor 1–115; execution utility 1–101; evaluation 1–225; provider message dispatch 534–583 and native tools 1077–1210 | `dynamic_cheatsheet/language_model.py:1-668`; `run_benchmark.py:1-327`; `dynamic_cheatsheet/utils/extractor.py:1-115`; `dynamic_cheatsheet/utils/execute_code.py:1-101`; `dynamic_cheatsheet/utils/evaluation.py:1-225`; `text_generation/simple_unified_client.py:534-583,1077-1210` | Provider and embedding internals unavailable; no live behavior or parameter identity established |
| SRC-2 | Git documentation/prompts | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Doctrine/design: prompts and usage. Reported operation: README performance paragraph only | README 1–180; three prompt files; specialist selected notebook code cells as documentation | `README.md:1-180`; `prompts/generator_prompt.txt:1-80`; `prompts/curator_prompt_for_dc_cumulative.txt:1-149`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:1-146`; `ExampleUsage.ipynb`; `EvaluatingResults.ipynb` | External paper not inspected; reported gains are not audited causal evidence |
| SRC-3 | Git retained outputs | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Observed run artifacts, with generating execution provenance unverified | First two JSONL rows each of cumulative and RetrievalSynthesis AIME 2024 GPT-4o outputs; selected fields decoded for inspection | `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:1-2`; `results/AIME_2024/gpt-4o_DynamicCheatsheet_RetrievalSynthesis.jsonl:1-2` | Four rows establish artifact contents and recorded delivery only; generating revision, credentials, exact models, full conditions and intervention design unverified |

Operational source root is `/home/zby/llm/commonplace/related-systems/suzgunmirac--dynamic-cheatsheet`. All evidence came from full-commit Git blobs, never the worktree. Source snippets below are quoted once on their supporting records. Decoding retained JSON fields is inspection of existing evidence, not execution of Dynamic Cheatsheet or a new behavioral probe.

## Shared records

### Components

CMP-1 — Python `LanguageModel` controller and benchmark loop. Symbolic program, stored as repository files and executed in a Python process; strings, lists and arrays carry active state. Implementation conclusion status: wired. The benchmark owns sequencing, task identities, local persistence and evaluation; the wrapper owns prompt assembly and calls. SRC-1, `dynamic_cheatsheet/language_model.py:290-668`; `run_benchmark.py:81-327`.

CMP-2 — Selected generator/curator language model. Distributed-parametric computation accessed through the same provider/model client for both roles. Model-name selection conclusion status: wired; exact parameter-version identity conclusion status: uninspected. Configurable strings such as aliases do not pin immutable weights. Parameter mutation inside local operation conclusion status: absent within ABS-2; external provider parameter changes conclusion status: uninspected. SRC-1, `dynamic_cheatsheet/language_model.py:76-113,411-431`; SRC-2, `README.md:125-141`.

>         client_kwargs = {"provider": provider, "model": model_id, "max_retries": 3, "retry_delay": 10}
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

CMP-3 — Precomputed question embeddings and symbolic cosine ranker. The numeric array is OBJ-3; the distributed-parametric component that produced it has identity and parameter-fixity conclusion status: uninspected. Loading/reordering and ranking conclusion status: wired. No embedding model is called in these runtime paths. SRC-1, `run_benchmark.py:204-220`; `dynamic_cheatsheet/language_model.py:503-514`.

CMP-4 — Local Python subprocess and optional remote code interpreter. Symbolic execution locally; provider-owned remote machinery uninspected. Execution grant is configured by operator flags and model-produced requests. Local timeout is process control, not a deployment isolation guarantee. RTE-7 and RTE-9 separate the routes. SRC-1, `dynamic_cheatsheet/utils/execute_code.py:62-101`; `text_generation/simple_unified_client.py:1077-1210`.

### Operative objects

OBJ-1 — Cumulative cheatsheet string, also used by the hybrid branch. Natural-language strategies, mathematical expressions and code snippets; in-memory during operation and checkpointed in files. RTE-2 extracts it from generated trajectories plus the previous sheet; RTE-6 can import an operator seed. BAP-1 and BAP-2 consume it as reference. Whole-string replacement is wired, item-level schema enforcement is absent within ABS-1. SRC-1, `dynamic_cheatsheet/language_model.py:396-455,610-661`. Truth-apt content and executable examples are distinguished as OBJ-10 and OBJ-11.

OBJ-2 — Accumulated original problem inputs and generator `final_output` trajectories. Mixed natural-language/symbolic strings can include reasoning, Python and execution output. In-memory positional pairs, persisted in OBJ-8; original inputs are reloaded from the dataset on resume. Generation does not certify truth. SRC-1, `run_benchmark.py:179-225,253-280`; `dynamic_cheatsheet/language_model.py:249-288`.

OBJ-3 — Imported numeric access vectors aligned by exact input-string lookup. Symbolic array and CSV data, used for ranking rather than learned in this loop. Stored vector values are not model weights or evidence of a vector database. SRC-1, `run_benchmark.py:204-220`.

>         df = pd.read_csv(embeddings_path)
>         questions = df["input"].tolist()
>         embeddings = df["embedding"].apply(ast.literal_eval)
>         embeddings = np.array(embeddings.tolist())  # (N, embedding_dim)
> 
>         # Re-order the embeddings based on the order of the dataset inputs
>         dataset_inputs = [example["input"] for example in dataset]
>         indices = [questions.index(inp) for inp in dataset_inputs]
>         embeddings = embeddings[indices]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

OBJ-4 — Query-conditioned RetrievalSynthesis sheet. Normal branch is curator-derived mixed prose/code; parse fallback is the current formatted raw retrieval block, not the old synthesis sheet. Stored/returned as a string and later fed to the next curator. A first call with no previous examples can generate guidance from the question alone and is not by itself trace extraction. SRC-1, `dynamic_cheatsheet/language_model.py:516-575`.

OBJ-5 — Current generated solution and extracted answer envelope, with independently consumed parts OBJ-14 and OBJ-15. Mixed prose/code output supplies later trace-based memory; answer alone supplies scoring. SRC-1, `dynamic_cheatsheet/language_model.py:419-445`; `run_benchmark.py:272-297`.

OBJ-6 — Superseded composite seed for benchmark target and score. Split into OBJ-12 and OBJ-13 because reference authority and computed verdict have different producers and consumers. No ID is reassigned.

OBJ-7 — Static generator/curator templates, natural-language instructions in files or caller strings. User-message instructions govern the task, while the embedded sheet is reference material. They are not operationally revised memory in this boundary. SRC-2, `prompts/generator_prompt.txt:1-80`; both curator prompts.

OBJ-8 — JSONL per-example checkpoints and parameter JSON. Symbolic envelopes retain mixed prose/code content, targets, steps, sheets and full outputs. RTE-6 restores selected fields; archival presence is not selection for every later consumer. Files preserve earlier sheet versions but no item-level rollback procedure is wired. SRC-1, `run_benchmark.py:69-78,133-189,272-309`.

OBJ-9 — Opaque remote execution environment addressed by OpenAI container ID. Possible state across problems; internal retained parts, representation and reuse are uninspected. Explicitly excluded from the local profile. Claude's native tool branch does not thread this identifier. SRC-1, `run_benchmark.py:115-118`; `text_generation/simple_unified_client.py:1077-1210`.

OBJ-10 — Truth-apt strategy propositions and worked mathematical claims carried inside OBJ-1 and OBJ-4. In the cumulative sample, the sheet generalizes a rectangle-counting method and states its dodecagon result as 15; stored target is 315. This is localized content, not a certified theorem. Observed content conclusion status: observed; general validity conclusion status: uninspected. CLM-3 retains evidence. Source provenance and creation phase are weaker than inspection of the stored claim itself. SRC-3, `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:1-2`.

OBJ-11 — Python snippets embedded in sheet examples. Symbolic code is present in sampled RetrievalSynthesis output; it remains advisory until a generator emits executable code through RTE-7 or RTE-9. Stored snippets are not executed directly. SRC-3, `results/AIME_2024/gpt-4o_DynamicCheatsheet_RetrievalSynthesis.jsonl:1`; SRC-1, `dynamic_cheatsheet/language_model.py:249-255`.

> pairs = n // 2  # Number of opposite pairs
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_RetrievalSynthesis.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

OBJ-12 — Dataset-supplied reference answers and task constraints, imported rather than produced by the memory system. Their epistemic authority is the benchmark's answer oracle, bounded to its task/encoding. Independent reference correctness is uninspected. SRC-1, `run_benchmark.py:232-244,290-297`.

OBJ-13 — Computed task verdict/count. Symbolic boolean and numeric state from matching or task predicates; affects printed scores, not curator acceptance. Check validity is bounded by the evaluator and input interpretation. SRC-1, `dynamic_cheatsheet/utils/evaluation.py:47-81,102-112,151-225`; `run_benchmark.py:290-309`.

OBJ-14 — Generated solution body inside OBJ-5 and later OBJ-2, containing problem-specific propositions, reasoning, optional code and reported execution output. Preservation into trace memory does not validate its premises or derivation. SRC-1, `dynamic_cheatsheet/language_model.py:249-288,419-445`; SRC-3, cumulative row 2 contains a purported arithmetic verification accompanying answer 54 against stored target 55.

OBJ-15 — Extracted final answer inside OBJ-5. A proposed result checked by RTE-8 against OBJ-12; text extraction supplies neither logical validity nor task correctness. SRC-1, `dynamic_cheatsheet/utils/extractor.py:12-59`; `run_benchmark.py:281-297`.

### Routes

RTE-1 — Cumulative/hybrid generation. Trigger: new problem or next cumulative refinement round; principal: caller/benchmark. CMP-1 owns the next step under symbolic branch/loop policy. It selects the whole current OBJ-1, optionally adds previous extracted answers for later cumulative rounds, and substitutes question plus sheet into OBJ-7. CMP-2 receives a user message and returns OBJ-5. BAP-1 gives the sheet advisory reference force for that solution; activation of a particular recalled proposition is uninspected. Returned solution is retained via RTE-6. Model/API failure can prevent completion; empty output becomes a placeholder in `generate`. Hybrid has one generation/update sequence despite the shared rounds argument. SRC-1, `dynamic_cheatsheet/language_model.py:244-247,396-455,610-661`.

>                 generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", generator_cheatsheet_content)
>                 current_cheatsheet = cheatsheet
> 
>                 # Prepare the message history for the generator model
>                 generator_history = [{"role": "user", "content": generator_prompt}]
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

RTE-2 — Post-answer cumulative/hybrid revision. Trigger: produced solution; proposer and substantive selector: CMP-2 under curator instructions. Inputs: question, OBJ-14 and previous OBJ-1; no target or score. CMP-1 asks for twice generator output-token allowance, disables local code execution for this call, then admits the first tagged sheet through extraction. Missing opening tag keeps old sheet; presence of tag does not require a closing tag, soundness, item structure or provenance. Replacement becomes the next returned sheet, then RTE-6 carries it forward. Model can decline to change content; code can reject only through extraction fallback. Operator can supply a seed on a later invocation, but automatic rollback to an earlier version is not implemented here. SRC-1, `dynamic_cheatsheet/language_model.py:422-455,630-661`; `dynamic_cheatsheet/utils/extractor.py:62-86`.

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

Guidance asks to assess solution correctness, preserve useful strategies, explain assumptions and improve generalized methods. It can retain theory text and reasons but is not obliged by extraction to do so; later generator and curator receive any reasons retained in the whole sheet. Correctness checking is model judgment, with no independent target oracle. Requested criticism can blame a solution or strategy; no fixed blame assignment or recorded criticism field is required. SRC-2, cumulative curator prompt 18–35; CLM-4 gives maintenance semantics.

> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Theory-builder conditions 1–4 for RTE-2 are separate: condition 1, localized proposed solutions, conclusion status: observed for OBJ-10 in CLM-3. Condition 2, deciding through what those solutions say, conclusion status: afforded by BAP-1 and BAP-2; stored prompt delivery is observed, but actual use of a specific rule is uninspected. Condition 3, formulated content-directed criticism and resulting revision or changed reliance, conclusion status: afforded by requested correctness assessment and output replacement; the sampled records do not expose an identified criticism of an existing strategy followed by its disposition. Condition 4, retained criticism result shaping the next round, conclusion status: uninspected; recurrence of revised strings is wired but does not identify a criticism-bearing change. Persistence of sheet text across rounds/problems and restart is wired; persistence of a particular criticism result is uninspected. Addressability: text items, descriptions, examples and stated conditions are inspectable; item structure/editing is best effort, with whole-sheet replacement as the implemented unit. Learning attributable to criticism conclusion status: uninspected; CLM-2 reports broader benefit without that attribution.

RTE-3 — Similarity retrieval for raw retrieval, synthesis and hybrid. CMP-1 compares current question vector against all prior OBJ-3 rows, sorts cosine scores, takes top-k and pairs positional OBJ-2 outputs. It reverses selected display order so the highest-ranked example is last. Trigger: next query; selection input: its precomputed vector; selected retained part: full prior input/output pairs. Direct generator delivery for raw/hybrid; curator delivery for synthesis. This is push with inferred-embedding signal and ranking authority, not an identifier-based memory request. No age or validity filter; excerpt length is not input-token-budgeted. Recovery from missing embeddings at benchmark entry is error, not a fallback to another memory approach. SRC-1, `dynamic_cheatsheet/language_model.py:503-528,588-608`; `run_benchmark.py:204-220`.

>             if len(prev_original_input_embeddings) > 0:
>                 similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
>                 top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
>                 top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
>                 top_k_similar_values = similarities[0][top_k_indices]
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

RTE-4 — RetrievalSynthesis revision before current answer. CMP-1 supplies selected pairs, previous OBJ-4 and next question to CMP-2, whose query-conditioned judgment proposes/transforms a sheet. Same parser admits it; fallback is the newly assembled raw retrieval block. Immediate consumer is current generator; returned text is later curator input via RTE-6. This is both selection by judgment and possible synthesis, not necessarily faithful compression. First-call invention is not sufficient evidence of trace learning; later trace-fed writes qualify. Guidance requests improvements and replacement of worse methods, but extraction supplies no semantic veto, acceptance warrant or audited rationale. SRC-1, `dynamic_cheatsheet/language_model.py:530-575`; SRC-2, synthesis curator prompt 13–53.

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

For this route, theory-builder condition 1 conclusion status: observed for localized sampled sheet content; condition 2 conclusion status: afforded through generator/curator reference use; condition 3 conclusion status: afforded through explicit effectiveness and rival-method questions; condition 4 conclusion status: uninspected for actual retained criticism results. The source wires repeated replacement and cross-problem reuse, not a guaranteed successful critique. Rationale and addressability have RTE-2's same best-effort limits. Learning attributable to that criticism conclusion status: uninspected. Whole replacement and context-derived guidance can change later capacity without weight training, but this evidence does not measure that change.

RTE-5 — FullHistoryAppending. Trigger: next query. CMP-1 formats every previous OBJ-2 pair into a reference block; no semantic curation or targeted selector. It immediately supplies this block to the generator, returns the formatted text, and reconstructs it from the complete prior corpus on the next call. Coarse push, no explicit expiry or invalidation. Its raw retention alone does not qualify as trace learning. SRC-1, `dynamic_cheatsheet/language_model.py:457-500`.

>                 curated_cheatsheet = "### PREVIOUS SOLUTIONS (START)\n\n"
>                 for i, (previous_input_txt, previous_output_txt) in enumerate(zip(original_input_corpus, generator_outputs_so_far)):
>                     curated_cheatsheet += f"#### Previous Input #{i+1}:\n\n{previous_input_txt}\n\n#### Model Solution to Previous Input #{i+1}:\n\n{previous_output_txt}\n---\n---\n\n"
>                 curated_cheatsheet += "#### PREVIOUS SOLUTIONS (END)"
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

RTE-6 — Local retention, seed import and resume. CMP-1 appends full output, assigns final sheet, then scores and rewrites JSONL after each problem. Parameters are saved separately. Operator can supply arbitrary initial text or a prior run path; resume checks selected argument values, restores last sheet and full outputs, reloads/reorders dataset inputs and skips completed rows. This is partial consistency checking, not verified reproducibility. Admission of seed/checkpoint contents trusts files; no substantive veto. Normal recovery uses latest sheet, with prior versions retained but not automatically replayed. File persistence is explicit; read-back selects current/latest sheet coarsely, not by provenance identifier. SRC-1, `run_benchmark.py:69-78,133-225,246-309`.

>     # Initialize the cheatsheet
>     cheatsheet = "(empty)"
>     if args.initialize_cheatsheet_path is not None:
>         with open(args.initialize_cheatsheet_path, "r") as file:
>             cheatsheet = file.read()
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         # Load the previous cheatsheet from the last output (if available)
>         last_cheatsheet = outputs[-1].get("final_cheatsheet")
>         if last_cheatsheet is not None:
>             cheatsheet = last_cheatsheet
> 
>         generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         cheatsheet = output_dict["final_cheatsheet"]
>         final_answer = output_dict["final_answer"]
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         # Save the outputs to a file after each example (for crash recovery)
>         write_jsonl(args.save_path_name, outputs)
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

RTE-7 — Generated code execution umbrella, with local and remote branches; RTE-9 details the materially distinct remote branch without changing this seed's referent. Locally, CMP-1 checks the execution flag and preceding fence, extracts the first Python block, adjusts a final expression for printing and starts a fresh Python subprocess. It captures stdout/errors, enforces a three-second wait, kills on timeout, deletes the temporary script and appends textual output to the solution. A continuation prompt can produce more code. Recovery is error text/model continuation, not rollback of effects. Code executes under inherited process authority; no deployed isolation envelope is established. Directly executing stored sheet snippets is not wired. SRC-1, `dynamic_cheatsheet/language_model.py:249-288`; `dynamic_cheatsheet/utils/execute_code.py:15-101`.

>         process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
>         stdout, stderr = process.communicate(timeout=timeout)
> --- `dynamic_cheatsheet/utils/execute_code.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>                 current_output = f"{output_prefix}\n{code_execution_flag}\n\n{executed_code}"
>                 final_output = f"{final_output}\n\n{current_output}".strip()
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The recursion depth check follows execution. At the nominal last continuation, prose tells the model no more execution is allowed, but the next invocation can still execute before stopping. Thus the prompt warning is policy, not a strict execution-count invariant. Execution result can test a computed consequence, but does not validate problem encoding, assumptions or general strategy. A model chooses the program and interprets its result; no answer oracle is thereby supplied. SRC-1, `dynamic_cheatsheet/language_model.py:249-284`.

>                 # If we haven't exceeded the max depth, prompt the model to continue
>                 if current_depth <= max_depth_num_rounds:
>                     warning_txt = ""
>                     if current_depth == max_depth_num_rounds:
>                         warning_txt = " (This is the last round. No more code execution will be allowed. Please present your final solution now.)"
>                     new_messages = [
>                         {"role": "assistant", "content": current_output},
>                         {"role": "user", "content": f"Proceed with any additional steps required and provide the completed solution. If everything is already complete, type FINAL ANSWER and submit it in the expected format. If you are stuck, please try alternative methods to solve the problem and provide the final solution.{warning_txt}"}
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

RTE-8 — Benchmark final-answer check. After memory assignment, CMP-1 calls the task evaluator, using OBJ-12 or a task predicate, and updates displayed correct/total counters (OBJ-13). GameOf24 evaluates expression and operand use; exact-match covers AIME; multiple-choice pattern matching and equation evaluation cover other loaded tasks. The oracle is supplied by dataset author/task specification, external to curator judgment. Result affects reported score; it cannot reject or repair already admitted memory. Expression evaluators call Python `eval`, so generator `allow_code_execution=False` is not a process-wide no-execution guarantee. SRC-1, `run_benchmark.py:280-309`; `dynamic_cheatsheet/utils/evaluation.py:47-81,102-112,151-225`.

>         if args.task == "GameOf24":
>             result = eval_for_GameOf24(original_input, final_answer)
>         elif args.task in ["AIME_2025", "AIME_2024", "AIME_2020_2024"]:
>             result = eval_for_exact_matching_with_no_punctuation(final_answer.lower(), original_target.lower())
>         elif args.task in ["GPQA_Diamond", "MMLU_Pro_Engineering", "MMLU_Pro_Physics"]:
>             result = eval_for_multiple_choice(current_input, final_answer, original_target)
>         elif args.task == "MathEquationBalancer":
>             result = eval_equation_balancer(None, final_answer, original_target)
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         value = eval(clean_output)
>         if not (abs(value - 24) < 1e-3):
>             return False
> --- `dynamic_cheatsheet/utils/evaluation.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

RTE-9 — Provider-native execution subordinate to RTE-7. Operator requests code interpreter; benchmark creates one OpenAI container for its run or a Claude sentinel. Wrapper disables local execution and passes requests to the remote tool route. OpenAI sends the same container identifier and retains only response text locally; Claude sends its native execution tool without equivalent container threading. Provider owns scheduling, state lifetime, isolation and tool recovery; these are uninspected external contracts, not inherited local guarantees. Immediate return is text; potential later environment read-back is opaque and outside the local comparison. SRC-1, `dynamic_cheatsheet/language_model.py:157-172,212-234,347-349`; `text_generation/simple_unified_client.py:1077-1210`.

>         params: Dict[str, Any] = {
>             "model": self.model,
>             "input": messages,
>             "tools": [{"type": "code_interpreter", "container": container_id}],
>         }
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>         def _call():
>             return self._generate_claude(
>                 messages=messages,
>                 stream=False,
>                 system_message=system_message,
>                 temperature=final_temperature,
>                 max_completion_tokens=final_max_tokens,
>                 use_native_web_search=False,
>                 tools=[code_execution_tool],
>                 **kwargs,
>             )
> --- `text_generation/simple_unified_client.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### Claims

CLM-1 — Source claims accumulating and reusing insights across queries without changing model parameters. Claim conclusion status: claimed. Local recurrence is wired and stored delivery narrowly observed; external weights remain uninspected. SRC-2, `README.md:13`.

> Dynamic Cheatsheet (DC) endows black-box language models with the ability to store and reuse insights across queries. Rather than repeatedly re-discovering solutions or making the same mistakes, DC enables models to accumulate and leverage strategies, code snippets, and problem-solving techniques without modifying the underlying model parameters.
> --- `README.md` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

CLM-2 — Source reports task accuracy gains without ground-truth labels or human feedback. Claim conclusion status: claimed. The memory-update inputs indeed exclude target labels (ABS-1); benchmark scoring separately has targets. Reported aggregate benefit cannot establish criticism-led learning, particular recalled-content activation, current provider performance or component causality. SRC-2, `README.md:20-28`.

> * **Zero-Shot Learning**: Improves performance without ground-truth labels or human feedback
> * **Experience-Driven Learning**: Bridges the gap between isolated inference events and cumulative learning
> 
> ### Performance Improvements
> 
> * **Mathematics**: Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams by retaining algebraic insights
> * **Puzzles**: GPT-4o's success rate on Game of 24 increased from approximately 10% to 99% after discovering and reusing Python-based solutions
> * **Arithmetic**: Near-perfect accuracy on tasks like balancing equations (compared to baseline ~50%)
> * **Knowledge-Intensive Tasks**: 9% improvement on GPQA-Diamond and 8% boost on MMLU-Pro Engineering and Physics problems
> --- `README.md` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

CLM-3 — Retained sample evidence, operation conclusion status: observed, limited to artifact contents. Cumulative row 1 records target 315, final answer 15 and a sheet with that erroneous answer-derived rectangle claim. Row 2 generator prompt contains the entire prior sheet, verified by exact string containment. This establishes recorded delivery, not behavioral dependence of the later answer. Row 2 has a different problem, target 55 and answer 54; it does not trace either error causally to recalled content. In the RetrievalSynthesis sample, first sheet has Python despite no retrieved pairs; second has a raw retrieval header. That is consistent with fallback but cannot prove fallback occurred without curator output. SRC-3, both sampled JSONL files 1–2.

> "target": "315"
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> "final_answer": "15"
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> Thus, the total number of rectangles is 15.
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> This formula excludes the edges of the polygon and self-connections.
> --- `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

CLM-4 — Source requests semantic memory maintenance, claim conclusion status: claimed. Preserving useful material and removing redundant/trivial details map to consolidation, forgetting and deduplication; revising entries maps to evolve; new strategies to synthesize; usage-based priority to promote. `decay` here means selective forgetting, not time-based expiry. These are instructions to a model inside a wired rewrite route, not implemented reliable item operations. SRC-2, synthesis curator prompt 13–53 and cumulative curator prompt 13–62.

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
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### Evidenced absences

ABS-1 — Target-driven memory rejection and semantic admission enforcement are absent within the inspected update/feedback boundary. Conclusion status: absent. Boundary: SRC-1 full `dynamic_cheatsheet/language_model.py:290-668`, `dynamic_cheatsheet/utils/extractor.py:62-86`, `run_benchmark.py:253-309` at the pin. Search/read question: which arguments deliver `target` or `result` to curator and which predicate accepts/rejects `new_cheatsheet`? Exhaustive route reads find generated-output/previous-sheet arguments, tag extraction/fallback, then benchmark scoring outside revision. RTE-2, RTE-4 and RTE-8 quotes show the positive wiring. This excludes hidden model criticism and arbitrary caller code from the negative claim; neither is proven absent.

ABS-2 — Local operational weight training is absent within wrapper/runner invocation. Conclusion status: absent. Boundary: SRC-1 full wrapper and runner at the pin; query/read question: are model parameters or optimizer/training state mutated between calls? Their full invocation paths select provider/model, pass prompts and update text/arrays, with no training step. This supports local parameter-fixity only; remote provider internals remain uninspected. CMP-2's model/client quote anchors the actual alternative operation.

### Behavioral-authority paths

BAP-1 — Generator consumes sheets/prior solutions through user-message reference context. Force: advisory knowledge, horizon: current solution and possible later trace-fed reuse. Static template tells it to inspect and adapt material; content delivery is wired and narrowly observed, activation of specific memory is uninspected. SRC-2, generator prompt 3–14; SRC-1, wrapper 405–418, 546–555, 616–627.

> - Carefully analyze both the question and cheatsheet before starting
> - Search for and identify any applicable patterns, strategies, or examples within the cheatsheet
> - Create a structured approach to solving the problem at hand
> - Review and document any limitations in the provided reference materials
> --- `prompts/generator_prompt.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

BAP-2 — Curator consumes old sheets and generated solutions in the user-message prompt. Force: advisory input to model judgment; surrounding static instructions direct revision. Horizon: proposed whole-sheet replacement and later generator/curator calls. No additional epistemic authority follows from retention. SRC-1, wrapper 423–435 and 533–544; SRC-2, curator prompts.

BAP-3 — Generated code request reaches local subprocess or remote tool. Force: execution grant; horizon: current program and any environment effects. Advisory memory may influence generated code but no direct stored-snippet execution is wired. SRC-1, RTE-7 and RTE-9 anchors.

BAP-4 — Evaluator verdict changes counters/output reporting. Force: validation for benchmark answer scoring; horizon: that task answer and aggregate display. No veto over memory. SRC-1, runner 290–309. This is outside the memory comparison's authority set.

BAP-5 — Imported embedding values influence cosine ranking of prior examples. Consumer: CMP-1 selector; channel: numeric array; force: ranking; horizon: current top-k selection. SRC-1, wrapper 509–514 and 593–601. They do not warrant selected answers.

## Runtime account

Ordinary cumulative benchmark invocation is a bounded experiment over a selected task dataset. Human principal chooses configuration, model, prompt paths and optional seed/restart. CMP-1 loads environment configuration, instantiates CMP-2, obtains dataset, shuffles at seed 10 by default, and aligns CSV question embeddings for retrieval variants. Each problem's identity is its position plus original input; saved output relationships are positional rather than cryptographically verified. RTE-1 solves, RTE-7 optionally executes generated Python, RTE-2 proposes memory, RTE-6 retains it, and RTE-8 scores before the checkpoint write. The terminal product is output JSONL and printed correctness; the latest sheet can be carried into more problems. Direct API callers receive the result dictionary and own subsequent persistence/sequence. This is not an enclosing autonomous agent service or delegation runtime.

Material alternatives are default generation with empty sheet, raw history RTE-5, raw retrieval RTE-3, pre-answer synthesis RTE-4, and hybrid RTE-1/RTE-2 plus retrieval. Native tools RTE-9 replace local execution, with external state uncertainty. Cumulative can repeat rounds on a single question; hybrid does one sequence. Empty model output becomes a placeholder. Extraction failure retains old cumulative text but falls back to raw selected pairs for synthesis. Missing embeddings stop benchmark retrieval setup; there is no silent change of approach. Resume uses selected argument equality and latest saved sheet, so changing dataset order or unverified prompt contents can alter resumed behavior.

Decision roles are explicit. Humans choose experiment/initial material and can change configuration between invocations. Model computation proposes solutions, code and memory, judges usefulness/correctness and selects replacement content; symbolic extraction can veto malformed sheet output, but no truth check veto exists. The model may attribute errors to a solution, strategy or assumptions; actual blame is uninspected without formulated criticism. Controller decides branch, sample order and successor invocation. No in-loop route edits static templates or production machinery. Reference targets are supplied to benchmark evaluators only; model judgment does not secretly provide an answer oracle. Direct API use affords open user problems, while shipped CLI mode is a bounded dataset sequence. Each mode's result depends on the caller's subsequent state handoff.

| Static forcing case | Inspected consequence | Evidence and limit |
|---|---|---|
| Missing sheet opening tag | Cumulative preserves current sheet; synthesis uses current retrieved block | RTE-2, RTE-4; parser behavior wired, no live model reliability claim |
| First retrieval query / no prior pairs | Raw route supplies empty context; synthesis still calls curator with question and previous sheet | RTE-3, RTE-4; first output alone cannot prove trace-fed learning |
| Code-execution limit and disabling local code | Local depth check follows execution; native provider path has own limits; task evaluators can still `eval` text | RTE-7, RTE-8, RTE-9; no process-wide execution prohibition inferred |
| Wrong answer / checkpoint resume | Memory is assigned before scoring and can retain wrong strategies; resume chooses latest sheet under partial consistency checks | CLM-3, ABS-1, RTE-6; sample shows retention/delivery, not later error causation |

No dynamic check planned. Live benchmark reproduction was considered but needs model credentials, external services and dataset/provider conditions beyond this static assessment; a new uncontrolled run would not identify historical causal claims. A synthetic parser test would duplicate unambiguous inspected branch logic without resolving a material uncertainty. No execution-preflight for a selected dynamic test is therefore required, and no `not run` attempt is treated as negative behavior evidence.

| Guarantee or control | Owner and enforcement point | Strength | Coverage, alternate path and external contract |
|---|---|---|---|
| Curator keeps correct useful material | Model under prompt; parser only checks opening tag | Policy | Shipped prompts only; arbitrary templates can differ; no truth invariant |
| Latest local text can be restored | Runner JSONL/parameter read | Best effort | Last completed checkpoint and compatible data/order; write rewrites file and is not atomic; remote environment not restored by local JSONL |
| Local code times out | Python parent `communicate(timeout=3)` and kill | Protocol | Direct child process wait; no demonstrated sandbox, descendant/resource or rollback guarantee; remote tool path externally owned |
| Context remains bounded | Generation token parameters and prompt word request | Best effort | Generated output bounded by provider parameters; prior raw histories/selected solutions have no enforced input-token budget |

Every route was checked for retained read-back and authority. RTE-1, RTE-2, RTE-3, RTE-4 and RTE-5 deliver retained parts as described; selection is coarse, embedding-based or model judgment. RTE-6 is restoration into those paths. RTE-7's local output returns immediately and can persist inside trajectories; remote read-back remains uninspected under RTE-9. RTE-8 score has no memory consumer. No sub-agent delegation occurs in inspected invocation paths, so delegated visibility is inapplicable. Explicit expiry is absent within these particular local assembly routes; prompt-directed forgetting belongs to CLM-4. Actual behavioral activation and benefit remain distinct from all delivered context.

## Lens scoping

### Memory/context scope

Trigger evidence: CLM-1, CLM-2 and SRC-1 recurrence/retrieval. Depth: full. Boundary: OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-8 and their routes RTE-1 through RTE-6, with optional trace-producing RTE-7. Remote OBJ-9/RTE-9 is inventoried but excluded from local normalized values. Five memory variants and cumulative repeated rounds must be covered because they differ in selection, write timing and retention. Fresh specialist input and report hashes match this run; no second coordinator-drafted profile replaces the specialist's classifications.

### Epistemic scope

Trigger evidence: CLM-2 improvement claim, CLM-4 curation instructions, generated theories OBJ-10, tool checks and task scoring. Depth: full. Boundary: RTE-1 through RTE-9; all operative objects, with truth-apt parts separated. Question: what is proposed, checked, admitted, retained and relied upon, and which criticism/learning claims does that support? Provider internals and full experimental designs remain excluded. Both lenses use the same canonical register; epistemic output is the local sparse overlay required by the invoked procedure.

## Lens outputs

### Memory/context lens

The integrated specialist inventory covers cumulative sheets, query-conditioned synthesis, raw history, raw retrieval and hybrid, plus seed import and resume. The memory unit is a replaceable string, not a store of enforced item records. Retrieval ranks prior question vectors and returns full paired solutions; it does not search sheet entries. The generator and curator are named later consumers. Coarse whole-sheet/history push, embedding-based example push and judgment-based synthesis push are distinct selections. Q references and displayed counts do not create identifier-based push.

RTE-2 and RTE-4 automatically distill trajectories, including optional local tool output, into retained guidance. This supports the profile's narrow `trace_learning: yes` meaning without establishing improvement or theory-builder membership. Cumulative rounds cover the same problem; subsequent benchmark problems cover cross-task use, where task means an individual problem, not a dataset label. Both occur online. Raw RTE-3/RTE-5 retention alone does not satisfy trace learning, and a first synthesis sheet made without past examples does not either.

The profile includes files/in-memory, mixed natural language/symbolic content and complete local lineage paths. Manual/authored seed adoption is afforded, lowering union basis accordingly. Curation values remain claimed because they are semantic instructions, while whole replacement is wired. Generated reasoning can survive inside sheets/history and be delivered later, but truth and rationale retention are not enforced. Faithfulness testing is not determinable from the inspected sample and reported gains; no recalled-content intervention has been established. CLM-3 shows why observation of delivery must not be relabelled success.

### Epistemic lens

#### 1. Source-and-claim boundary

See SRC-1, SRC-2 and SRC-3 for the frozen boundary. Assessed families are model content production, curation, retrieval/history, code evidence, answer scoring and checkpoint reuse. Unassessed families are provider internals, embedding creation and exhaustive experiment provenance; they prevent whole-system truth or causality claims. CLM-1 and CLM-2 are claims under test, not adopted warrants. The question and exclusions are those in Epistemic scope.

#### 2. Epistemic-object inventory

| Object/part | Candidate content and lineage | Claimed role and gap |
|---|---|---|
| OBJ-1, OBJ-4 | See canonical identities; candidate truth-apt strategy parts are OBJ-10, code parts OBJ-11 | Reference/revision material; whole-sheet retention not epistemic acceptance |
| OBJ-2 | Prior input/output content acquired and preserved | Evidence about prior model activity; its assertions inherit no new truth warrant |
| OBJ-3 | No candidate truth-apt output identified in numeric access metadata | Ranks examples; similarity not answer validity |
| OBJ-5 | See solution propositions OBJ-14 and proposed answer OBJ-15 | Composite output, not one undifferentiated warrant target |
| OBJ-6 | Superseded; see OBJ-12 and OBJ-13 | Split reference from verdict |
| OBJ-7 | Static task/method instructions | Not a newly produced candidate in the inspected operation |
| OBJ-8 | Serialization envelope; substantive parts covered separately | Records lineage, not truth |
| OBJ-9 | Internal payload uninspected | Cannot determine candidate content or lifecycle |
| OBJ-10 | General strategies and mathematical claims | Minimum localized theory content observed; creation and criticism provenance limited |
| OBJ-11 | Procedural code examples | No independent truth-apt claim of program correctness isolated; related strategy assertions belong to OBJ-10 |
| OBJ-12 | Imported expected answer/task condition | Source oracle is external; independent accuracy uninspected |
| OBJ-13 | Computed match/predicate verdict | Bounded evaluator domain; does not validate entire solution or memory |
| OBJ-14, OBJ-15 | Model solution propositions and final answer | Candidate production without automatic proof or acceptance |

#### 3. Authority-route ledger

All implemented rows have architectural status **implemented** based on SRC-1. Their observed candidate state is separately addressed below. Generic endpoints and force channels remain in canonical RTE/BAP records.

| Route | Function | Content/update relation | Target, evaluator, timing and result | Epistemic authority | Operational force and limit |
|---|---|---|---|---|---|
| RTE-1 | Content transformation | Indeterminate: derivation or conjecture depending on candidate | Model proposes OBJ-14/OBJ-15 while solving | No automatic warrant for truth | Returns answer, may trigger RTE-7; BAP-1 guidance does not certify use |
| RTE-1 | Operational admission/selection/consumption | No content change to delivered sheet | Whole OBJ-1 supplied at solve start | Advisory prior content only | BAP-1, current solution; recorded delivery in CLM-3 |
| RTE-2, RTE-4 | Content transformation | Indeterminate overall; generalized OBJ-10 may be ampliative conjecture | Curator assesses usefulness/correctness, proposes revised sheet | Model judgment; no independent oracle | Produces replacement candidate; instruction asks criticism, actual formulation uninspected |
| RTE-2, RTE-4 | Disposition/acceptance | No content change at parser | Opening-tag extraction admits text or uses fallback | Formatting license only, no epistemic acceptance of claims | Permits memory replacement; ABS-1; prior-sheet and raw-block fallbacks differ |
| RTE-3, RTE-5 | Operational admission/selection/consumption | Non-ampliative formatting of preserved trajectories | Cosine rank or full history selected before generation | Relevance/presence does not warrant correctness | BAP-1/BAP-2, BAP-5; no truth predicate |
| RTE-6 | Retention | No substantive content change in serialization | Controller saves after generation/scoring | Preserves source lineage, not endorsement | Keeps future context available |
| RTE-6 | Lineage/freshness/recovery | Acquisition/import and restoration | Selected parameter checks and last-record read | Limited configuration consistency | Resumes local text; no complete replay guarantee |
| RTE-7, RTE-9 | Check/evidence production | Generated program may compute an entailed result; interpretation remains unchecked | Python/provider environment evaluates submitted program | Bounded evidence about that execution only | Returns observations for model continuation; cannot warrant encoding/strategy generalization |
| RTE-8 | Check/evidence production | Entailed derivation within implemented predicate | Checks OBJ-15 against OBJ-12 after memory update | Task answer match under given predicate | Produces OBJ-13, BAP-4 |
| RTE-8 | Disposition/acceptance | No content change | True/false adjusts correct count | Acceptance only for benchmark scoring, not memory or whole reasoning | Printed aggregate; no later memory veto |

No post-acceptance lifecycle integration route for a generalized strategy is established within ABS-1's boundary. RTE-6 retention and RTE-1 use precede or lack epistemic acceptance and are labelled accordingly. Predicate success on a final answer cannot transfer warrant to its explanation, reusable rule or recalled-memory contribution. Architecturally missing strategy acceptance has status **no route found within boundary**, not a system-wide negative about all model thought.

#### 4. Per-object lifecycle disposition

OBJ-10 is the material ampliative candidate part: a worked problem result is extended into reusable general strategy. The stored sheet supports that content classification; it does not identify every creation step. Relevant routes are RTE-2, RTE-4, RTE-1 and RTE-6. Observation/anomaly route architecture is implemented through question/solution delivery; observed candidate state: not determinable for an actual error noticed by a critic. Conjecture architecture is implemented through curator proposal; observed candidate state: not determinable for the generating process, although the candidate artifact exists. Derived consequence architecture is implemented in optional solution/code paths; observed candidate state: not determinable for a consequence test of this retained rule. Test/evidence architecture is implemented for optional code and bounded answer scoring; observed candidate state: not determinable for a rule-directed criticism. Acceptance architecture for generalized rule truth: no route found within boundary; observed candidate state: not reached within the recorded parser/retention sequence. Intended operational use is future reference, but extraction is not evidence-consuming epistemic acceptance. Lifecycle integration architecture: no route found within boundary; observed candidate state: not reached in that sequence. The sheet was retained and delivered without such acceptance. Missing evidence is a candidate-linked formulated criticism, disposition and later use of its result. CLM-3 establishes stored candidate/delivery, not those phases.

OBJ-2 has non-ampliative acquisition/preservation through RTE-5/RTE-6; discovery lifecycle not applicable to that preserving operation. Original generated assertions are separately OBJ-14/OBJ-15. OBJ-12 has acquisition/import; discovery lifecycle not applicable; source oracle warrant is assumed by the benchmark, not independently tested. OBJ-13 has entailed derivation within scoring code; discovery lifecycle not applicable; its license is only the predicate actually applied. OBJ-14 and OBJ-15 have indeterminate transformations: generation may derive from premises, guess, or generalize. Sample explanations alone do not certify entailment. Preserved lineage is source problem plus prompt and generated output; checks are optional program execution and task scoring. To classify production more finely requires candidate-specific warranted premises, derivation or identified conjecture and execution-linked checks.

No lifecycle record for OBJ-1: envelope contents are analysed as OBJ-10 and OBJ-11; relevant update routes RTE-2 and RTE-6.
No lifecycle record for OBJ-3: no candidate truth-apt output for this access object; relevant direct selection route RTE-3.
No lifecycle record for OBJ-4: envelope contents are analysed as OBJ-10 and OBJ-11; relevant update routes RTE-4 and RTE-6.
No lifecycle record for OBJ-5: output parts are OBJ-14 and OBJ-15; relevant route RTE-1.
No lifecycle record for OBJ-6: superseded composite, now OBJ-12 and OBJ-13.
No lifecycle record for OBJ-7: no candidate truth-apt output for this static instruction object; relevant consumption routes RTE-1, RTE-2 and RTE-4.
No lifecycle record for OBJ-8: no independent candidate truth-apt output for this envelope; relevant route RTE-6.
OBJ-9 lifecycle disposition: not determinable because its contents are uninspected; RTE-9 supplies only request/return wiring.
No lifecycle record for OBJ-11: no separately isolated candidate truth-apt output for this procedural part; relevant routes RTE-2, RTE-4 and optionally RTE-7.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design and implementation | Observed-run support | Causal support and conclusion |
|---|---|---|---|
| CLM-1 | Prompts and RTE-1/RTE-2/RTE-4/RTE-6 support cross-query reuse; ABS-2 bounds local weight fixity | CLM-3 records prior-sheet delivery | No independent causal contrast; reuse established at narrower interface/artifact level |
| CLM-2 | Source reports improvement; ABS-1 supports label-free curation, while RTE-8 uses labels for scoring | Selected artifacts have answers/sheets, not a complete improvement comparison | No verified intervention isolates memory, criticism, code execution or retrieval; retain performance as reported |
| CLM-4 | Maintenance operations requested in prompts; replacement routes implemented | Sample shows retained text, not reliable completion of all requested operations | No faithful-maintenance or validity guarantee |

#### 6. Bounded conclusion

Dynamic Cheatsheet retains model-generated solutions, constructs reference strategies, and provides them to later model calls. Curator prompts request criticism and generalization, and code can preserve resulting text. The admission route does not distinguish a checked generalized claim from an unchecked one. Optional execution provides bounded computational evidence; benchmark targets assess final answers after memory admission. These routes support adaptive memory and an available criticism/revision architecture, but sampled delivery and reported aggregate gains do not establish that criticism of a consumed theory improved future capacity.

## Reconciliation

Fresh specialist input hash `062c4748323404f7c963bccd5636b804e2e3980158082422e53f2f6e91cdd2cc`, method hash `d424c68a5638393f1c3fa838e87d662ce662349e33aef6d7d0523abc021a8606`, report run/source/boundary/status and exact report hash were checked. Specialist model identity is unknown as reported. The typed report is substantive provenance, not independent semantic clearance of this result.

| Specialist proposal | Canonical disposition |
|---|---|
| MEM-OBJ-1 | OBJ-9, opaque remote environment; explicitly excluded from local profile |
| MEM-RTE-1 | RTE-9, detailed remote branch under existing RTE-7 umbrella; no ID reassignment |
| MEM-CLM-1 | CLM-3, narrow observed artifact contents and delivery |
| MEM-CLM-2 | CLM-4, requested semantic maintenance at claimed basis |

All seven issues are resolved explicitly: remote state stays outside local known-value aggregation; artifact observation and prompt claim retain distinct strengths; OBJ-4/RTE-4 use current raw retrieval fallback rather than assumed old-sheet preservation; OBJ-8 distinguishes archived targets from fields actually restored, and checkpoint write follows scoring; per-task and cross-task refer respectively to one problem and distinct problems, with hybrid single-pass; retained reasons are optional and delivered without truth guarantee; `decay` adopts the report's documented selective-forgetting mapping at claimed basis. No substantive specialist disagreement remains, so no correction pass was necessary.

The coordinator independently traced evaluation-after-admission and provider/local execution; the specialist independently confirmed these overlapping routes. Other memory classifications are integrated specialist findings, not claimed independent convergence. Local epistemic analysis added truth-apt/content parts OBJ-10 through OBJ-15, superseding composite OBJ-6, and ranking authority BAP-5. No profile reference depends on superseded OBJ-6. All accepted IDs resolve and retain their original referents.

## Bounded synthesis

The strongest supported contribution is a wired route that automatically converts generated problem-solving experience into text/code guidance and carries it across later problems without local model training. The source reports substantial performance gains. The available sample establishes retained strategies and subsequent delivery, including delivery of a wrong answer-derived rule; it does not identify improved capacity caused by criticism of a consumed theory.

Operationally, cumulative mode revises after solving, RetrievalSynthesis revises before solving from selected prior cases and an old sheet, and hybrid supplies both general and similar-case context. Raw alternatives reveal that memory retention, selective delivery and semantic curation are different mechanisms. The same model performs solution and curation; a tag parser controls text replacement while truth checking remains prompt-directed. Task targets are evaluation oracles only after memory update. For sequential experiments this separates adaptation from benchmark feedback: label-free curation is supported, verified memory is not.

Theory-builder membership conclusion status: uninspected as a completed process in this evidence boundary. Condition 1 is observed for localized strategies; condition 2 is afforded through instructed semantic use, condition 3 afforded through correctness/rival-method judgment, and condition 4 uninspected for actual retained criticism shaping a subsequent round. Wired recurrence alone does not fill those gaps. Learning conclusion status: claimed for source-reported broad performance gains; attribution to holding and criticizing theories conclusion status: uninspected. No `trace_learning` axis value upgrades that result.

Reflection conclusion status: afforded for strategy self-representation: outputs from the system's solving activity can update its retained strategy description, and subsequent solves are instructed to use it. A realized two-way behavioral effect is uninspected, so this is not an observed reflective process. Reflective theory-builder qualifier conclusion status: uninspected; shipped method templates/controller are not revised through their own criticism in these routes. Computational operation/autonomy conclusion status: wired for proposing, judging and admitting text within the configured loop; the stronger autonomous theory-builder qualifier remains uninspected with membership. Humans set the problems, model/templates and initial state, outside those automatic rounds.

Self-improvement conclusion status: claimed at the source's reported task-performance level. The concrete partial mechanism is wired replacement and reuse of problem-solving strategies; independently verified improved future capacity, and its causal dependence on that replacement or criticism, remain uninspected. Exact candidate-linked criticism and successor use would establish missing theory-route links; controlled memory-content or mechanism interventions with pinned models/configurations would change the improvement assessment. Remote environment persistence must be accounted for in any such contrast.

## Limitations

| Limitation | Affected source/records | Inspected boundary | Conclusion prevented | Resolving evidence |
|---|---|---|---|---|
| Model/provider internals opaque | SRC-1, CMP-2, OBJ-9, RTE-9 | Request/return code only | Exact weights, deployed isolation, remote state form/lifetime | Version-pinned provider/runtime evidence and traces |
| Generated embedding origin uninspected | CMP-3, OBJ-3 | CSV load/alignment/ranking | Embedding model identity/training/freshness | Source generation record and version |
| Four output rows, generating conditions unknown | SRC-3, CLM-3 | Selected AIME 2024 artifacts | Full benchmark replication or general outcome rates | Immutable configurations, complete traces and executable experiment protocol |
| No recalled-content intervention | CLM-2, CLM-3, RTE-1 | Reported gains plus delivery sample | Faithfulness, activation and memory/criticism causal contribution | Controlled counterfactual memory inputs with comparable runs |
| Criticism content/result not retained explicitly | RTE-2, RTE-4, OBJ-10 | Curator prompts, sheets, sampled steps | Observed theory-builder conditions 2–4 and criticism-led learning | Candidate-linked criticism, blame/disposition, next-round semantic use |
| Arbitrary caller templates and notebook modes not exhaustive | OBJ-7, SRC-2 | Shipped wrapper/default semantics; notebooks as documentation | Claims over every external integration | Declared integration configuration and bounded new inspection |
| Partial checkpoint consistency and overwrite writes | RTE-6, OBJ-8 | Runner resume/write code | Verified deterministic replay or crash-atomic persistence | Complete data/prompt/model pins and atomic checkpoint protocol |
| Predicate-bound checks | RTE-7, RTE-8 | Execution and scoring implementations | General strategy validity from answer/code success | Checked premises/encoding and scoped strategy tests |

## Verification and blockers

### Semantic verification

Checked all scoped alternatives and included opaque-state exclusion against the profile. Local files/in-memory union covers sheets, traces, vectors and checkpoints; mixed prose/code/vector/serialization explains representational form. Manual/imported seed lineage remains afforded, and requested curation remains claimed. RTE-2 and RTE-4 are the qualifying trace-fed write routes; both feed later consumers, with optional RTE-7 tool traces. Cumulative same-problem rounds and later distinct problems account for per-task/cross-task; timing is online for both. First-query invention and raw history do not independently qualify.

For every push signal, consumer/trigger/selector/part was checked: whole-sheet generator and previous-sheet curator delivery on each call is coarse; whole-history delivery is coarse; cosine current-question ranking selects prior paired solutions; query-conditioned curator judgment selects/transforms delivered synthesis. Operator file selection is upstream of these deliveries, not an additional model-requested pull. Q references/input alignment do not create identifier push. Remote OBJ-9 remains excluded rather than silently counted as known local storage.

Canonical ID mapping, superseded composite disposition, source/status boundaries and all seven integration issues were checked. Theory-builder conditions, learning, reflection and autonomy remain separately bounded. Observed output contents do not prove generating revision or causality. Every blockquote is checked against the complete pinned blob during prepare/publish; load-bearing quote meaning was checked independently of occurrence. Source/native authority limits and method-overlay fields are preserved.

### Deterministic validation

Validation target: `kb/reports/state/agentic-system-analysis/AAS-2026-09-26-dynamic-cheatsheet-01/result.md` with `commonplace-validate --full`. PASS (clean), with no warnings or failures. The final bytes were revalidated after recording this outcome.

### Blockers

None.
