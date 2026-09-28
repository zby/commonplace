---
type: types/agentic-system-analysis-result.md
description: "Dynamic Cheatsheet: pinned workflow analysis of inference-time memory, code execution, and the separation between curation and answer grading"
run-id: AAS-2026-09-27-dynamic-cheatsheet-02
system: "Dynamic Cheatsheet"
run-date: "2026-09-27"
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
analysis-cutoff: "2026-09-27"
evidence-tier: code-grounded
memory-comparison: {"scope": "Local accumulated cheatsheet text, raw input/output histories, their embedding access structures, initialization, curation, later generator/curator consumption and checkpoint/resume in all six advanced_generate alternatives. Includes source-native retained artifacts as bounded operational evidence. Excludes static prompt instructions as memory objects, provider-internal container contents, model weights, and unspecified external API consumers. Temporary local code-execution recursion is current-episode context and does not independently count as accumulated memory or read-back.", "axes": {"storage_substrate": {"assessment": "known", "values": ["files", "in-memory", "vector"], "evidence": {"files": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "RTE-1", "RTE-3"], "note": "Benchmark checkpoints memory in JSONL and loads seed text and embedding CSV files."}, "in-memory": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "RTE-1", "RTE-3"], "note": "The benchmark passes the current cheatsheet and growing output list between calls."}, "vector": {"basis": "wired", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "RTE-1", "RTE-3"], "note": "OBJ-3 supplies numeric vectors used directly by cosine similarity; no vector database is implied."}}, "records": ["OBJ-1", "OBJ-2", "OBJ-3", "RTE-1", "RTE-3"], "note": "Local strings, arrays and JSONL/CSV persistence cover every inspected cheatsheet/history alternative; provider-internal container contents are outside this classification."}, "representational_form": {"assessment": "known", "values": ["natural-language", "symbolic"], "evidence": {"natural-language": {"basis": "observed", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "CLM-3"], "note": "The inspected cumulative run retains prose descriptions and sends the preceding sheet to the next generator prompt."}, "symbolic": {"basis": "observed", "records": ["OBJ-1", "OBJ-2", "OBJ-3", "CLM-3"], "note": "The same retained sheet contains Python function definitions; OBJ-3 also wires numeric selection structures."}}, "records": ["OBJ-1", "OBJ-2", "OBJ-3", "CLM-3"], "note": "Content includes prose and executable Python examples; access structures include numeric vectors and structured JSON. Embeddings are symbolic access data, not learned model parameters."}, "lineage": {"assessment": "known", "values": ["authored", "imported", "other-compiled", "trace-extracted"], "evidence": {"authored": {"basis": "afforded", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "RTE-8"], "note": "A caller can compose seed cheatsheet text for the documented cheatsheet argument or initialization file; no human edit is evidenced."}, "imported": {"basis": "wired", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "RTE-8"], "note": "Benchmark initialization/resume and CSV loading import retained text/history and access vectors."}, "other-compiled": {"basis": "wired", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "RTE-8"], "note": "Raw prior input/output pairs are deterministically formatted into reference blocks for retrieval and full history."}, "trace-extracted": {"basis": "wired", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "RTE-8"], "note": "Curators consume prior generator solutions and produce later-consumed cheatsheet text."}}, "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "RTE-8"], "note": "Caller-authored seed text is an affordance; checkpoint/CSV import, deterministic history formatting, and trace-fed curation are implemented."}, "behavioral_authority": {"assessment": "known", "values": ["knowledge", "instruction", "ranking"], "evidence": {"knowledge": {"basis": "wired", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "CLM-3"], "note": "Retrieved examples and sheets enter generator prompts as reference material whose correctness the model is asked to check."}, "instruction": {"basis": "observed", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "CLM-3"], "note": "Retained sheets contain ordered solving steps and code; the usage notebook generator explicitly rehearses cheatsheet steps in its solution."}, "ranking": {"basis": "wired", "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "CLM-3"], "note": "Cosine similarity over retained input embeddings determines which prior outputs enter the prompt."}}, "records": ["OBJ-1", "OBJ-3", "RTE-2", "RTE-3", "CLM-3"], "note": "Memory prose supplies advice and prescriptive strategies to generators and curators; vectors rank past examples. No memory-grounded enforcement or validation route is shown."}, "write_agency": {"assessment": "known", "values": ["automatic", "manual"], "evidence": {"automatic": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-8"], "note": "Model curation, output accumulation and after-example JSONL writes run without individual memory-item approval."}, "manual": {"basis": "afforded", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-8"], "note": "The caller can author or edit an initial cheatsheet before supplying it; provenance is not checked."}}, "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-8"], "note": "Automatic production/checkpointing is wired; manual initial content is afforded through supplied strings/files, with no built-in editor."}, "curation_operations": {"assessment": "known", "values": ["consolidate", "dedup", "evolve", "promote", "synthesize"], "evidence": {"consolidate": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "The delivered curator prompt asks for concise entries and removal of trivial information while carrying old material forward."}, "dedup": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "The delivered retrieval-synthesis prompt explicitly instructs removal of duplicate entries."}, "evolve": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "New extracted text replaces the current cheatsheet and is passed to later calls."}, "promote": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "The delivered curator prompts ask for usage counts and prioritization of frequently used solutions; salience is model-mediated, not enforced metadata."}, "synthesize": {"basis": "wired", "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "The delivered curator prompts request new meta-strategies and generalizations from earlier problem solutions."}}, "records": ["RTE-2", "RTE-3", "RTE-4"], "note": "Model-mediated consolidation, deduplication, salience promotion and synthesis are instructed by the supplied curator prompts; whole-sheet evolution is wired. This classifies requested operations, not their reliable success. No separate invalidation/history-retaining withdrawal or decay schedule is implemented."}, "read_back_direction": {"assessment": "known", "values": ["push"], "evidence": {"push": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-5"], "note": "The generator and curator receive automatically assembled retained content on each solve/update. Neither requests a memory search. Returning a result dictionary to the orchestrator is not a second memory-consumer pull route."}}, "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-5"], "note": "The generator and curator receive automatically assembled retained content on each solve/update. Neither requests a memory search. Returning a result dictionary to the orchestrator is not a second memory-consumer pull route."}, "read_back_signal": {"assessment": "known", "values": ["coarse", "inferred-embedding", "inferred-judgment"], "evidence": {"coarse": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-5"], "note": "Each cumulative call receives the whole current sheet; full-history appending delivers all accumulated pairs; resume restores the last sheet."}, "inferred-embedding": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-5"], "note": "The current query vector selects top-k earlier query/output pairs automatically."}, "inferred-judgment": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-5"], "note": "Curator calls select and rewrite portions of old sheets and traces before their output is supplied to later generators."}}, "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4", "RTE-5"], "note": "Whole-sheet and accumulated prior-task history delivery are coarse; retrieval uses cosine similarity; curators decide retained content for subsequent delivery. Temporary code-execution recursion is current-episode context and does not supply a memory read-back classification."}, "trace_learning": {"assessment": "known", "values": ["yes"], "evidence": {"yes": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Automatic trace-fed cheatsheet writes persist through checkpointing and reach later generators. Improvement is not required for this implemented route."}}, "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Automatic trace-fed cheatsheet writes persist through checkpointing and reach later generators. Improvement is not required for this implemented route."}, "trace_source": {"assessment": "known", "values": ["trajectories", "tool-traces"], "evidence": {"trajectories": {"basis": "wired", "records": ["OBJ-2", "OBJ-4", "RTE-2", "RTE-3", "RTE-4", "RTE-6"], "note": "Curators receive problem-solving trajectories, including local code and its returned output when local execution is used. Raw retention alone in retrieval/full-history branches does not establish learning."}, "tool-traces": {"basis": "wired", "records": ["OBJ-2", "OBJ-4", "RTE-2", "RTE-3", "RTE-4", "RTE-6"], "note": "Curators receive problem-solving trajectories, including local code and its returned output when local execution is used. Raw retention alone in retrieval/full-history branches does not establish learning."}}, "records": ["OBJ-2", "OBJ-4", "RTE-2", "RTE-3", "RTE-4", "RTE-6"], "note": "Curators receive problem-solving trajectories, including local code and its returned output when local execution is used. Raw retention alone in retrieval/full-history branches does not establish learning."}, "learning_scope": {"assessment": "known", "values": ["cross-task", "per-task"], "evidence": {"cross-task": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Separate benchmark questions establish cross-task reuse, even though the runner calls a whole dataset a task; repeated cumulative rounds establish per-task reuse. No cross-project sharing service is shown."}, "per-task": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Separate benchmark questions establish cross-task reuse, even though the runner calls a whole dataset a task; repeated cumulative rounds establish per-task reuse. No cross-project sharing service is shown."}}, "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Separate benchmark questions establish cross-task reuse, even though the runner calls a whole dataset a task; repeated cumulative rounds establish per-task reuse. No cross-project sharing service is shown."}, "learning_timing": {"assessment": "known", "values": ["online"], "evidence": {"online": {"basis": "wired", "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Cumulative and hybrid curation run after solving; retrieval-synthesis runs before the next solve within the active sequence. Resume/import does not create an additional offline learning process."}}, "records": ["RTE-1", "RTE-2", "RTE-3", "RTE-4"], "note": "Cumulative and hybrid curation run after solving; retrieval-synthesis runs before the next solve within the active sequence. Resume/import does not create an additional offline learning process."}, "distilled_form": {"assessment": "known", "values": ["natural-language", "symbolic"], "evidence": {"natural-language": {"basis": "observed", "records": ["OBJ-1", "RTE-2", "CLM-3"], "note": "The sampled cumulative run retained problem descriptions and solving strategies in its final sheet and next prompt."}, "symbolic": {"basis": "observed", "records": ["OBJ-1", "RTE-2", "CLM-3"], "note": "That sheet also retained Python code, including is_valid_coloring, alongside explanatory text."}}, "records": ["OBJ-1", "RTE-2", "CLM-3"], "note": "The same trace-fed cheatsheet retains prose and Python procedures consumed on later queries."}, "faithfulness_tested": {"assessment": "not-determinable", "values": [], "evidence": {}, "records": ["CLM-3", "RTE-7"], "note": "Inspected notebook and JSONL samples show delivery and expressed use; answer-scoring code and sequential reruns do not isolate dependence on recalled content. Uninspected experimental rows prevent a corpus-wide negative."}}}
---

# Dynamic Cheatsheet agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-02/run-state.md`

**Generated review:** `kb/agentic-systems/reviews/dynamic-cheatsheet.md`

**Memory analysis report:** `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-02/memory-report.md`
**Memory analysis report SHA-256:** b5bb6019e509596e7746d0e588bfe72783ebdc7daa2d836083022ecbd487e603

The result records complete analysis content; the run state alone declares successful publication. Coordinator: CODEX_THREAD_ID `01a0e315-4fce-7b71-8c14-09e9af772ceb`. The specialist received a source-only frozen input, not an earlier review.

## Boundary and evidence

Evidence basis: implementation, shipped prompts and documentation, and selected retained notebook/JSONL artifacts at Git commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, inspected on 2026-09-27. No target code was executed.

The intended use is to explain how this experimental workflow carries solutions between model invocations and what its checks warrant. The whole-system boundary is the Dynamic Cheatsheet workflow: `LanguageModel.advanced_generate`, its generator/curator variants, the code and provider calls they reach, benchmark orchestration, checkpoint/resume, and selected example outputs. This is a sequential model-calling workflow, not a general delegated-agent scheduler. Both open caller requests through the Python API and bounded benchmark sequences are included.

External model services, hosted code-interpreter internals, and the origin of shipped embedding vectors are excluded; the client cannot establish their model weights, service persistence guarantees, isolation, or embedding-training provenance. General-purpose client chat/web-search APIs not reached by the inspected workflow are excluded; this prevents claims about every independent use of the bundled client. Provider selection and arbitrary extra API parameters remain included as extension boundaries whose effects depend on the provider. Dataset truth and the full research study are not independently audited; README metrics remain reported claims. Notebook outputs are inspected historical artifacts, not execution of the current commit. No legacy Commonplace reviews, prior analysis results, audits, workshop records or comparison rows supplied analytical input.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | Git repository | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Implementation: Python modules. Doctrine/design: README and prompts, separately attributed below. | `run_benchmark.py`; `dynamic_cheatsheet/language_model.py`; extractor and execution utilities; shipped task evaluators; client dispatch, retry, and native code paths; three prompt files; README; evaluation notebook code cells. | Full paths and ranges on records below; all read with commit-addressed Git. | Remote service internals and embedding producer uninspected; no deployment or parameter-fixity guarantee. |
| SRC-2 | Retained source-native run artifacts | `https://github.com/suzgunmirac/dynamic-cheatsheet` | `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` | Observed run artifacts, without causal experiment or authenticated executing-code provenance. | `ExampleUsage.ipynb` cells 0–15, selected output fields; `results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl` first two rows and one targeted keyword inspection in row 9; first two rows of AIME 2025 GPT-4o cumulative and retrieval-synthesis JSONL. | Notebook raw JSON lines and JSONL row anchors on records. | No reconstruction of complete study design; historical outputs do not prove operation of later provider/client changes. |

Access root: `/home/zby/llm/commonplace/related-systems/suzgunmirac--dynamic-cheatsheet`. Origin and full commit were verified. Worktree contents were not evidence. Truncated preliminary reads were replaced with bounded commit reads before supporting findings.

## Shared records

### Components

### CMP-1 — Generator and curator language model

Source-native component: one `LanguageModel` client used for generator and curator calls; distributed-parametric model behind a caller-selected provider/model name. Implementation conclusion status: wired. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:76-113,405-435` and `text_generation/simple_unified_client.py:534-583`. Model calls return text, and client code performs no weight update. Local parameter-update conclusion status: absent within these dispatch/update functions; remote parameter changes conclusion status: uninspected. Identity-pinning conclusion status: wired for forwarding the supplied model string, not for proving immutable weights. The benchmark default is `openai/gpt-4o-mini`; aliases and version-shaped strings are both permitted, while the notebook names `openai/gpt-4o-2024-11-20`. Provider resolution and actual weights remain uninspected. This does not limit learning through retained text.

>         client_kwargs = {"provider": provider, "model": model_id, "max_retries": 3, "retry_delay": 10}
> --- [Pinned source](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py#L91-L91)

### CMP-2 — Unidentified embedding producer

Source-native component: external producer of the precomputed query embeddings, distinct from the cosine selector. Representational form: distributed-parametric producer, if used, is not identified by the inspected runtime; stored vectors are numerical data. Producer identity, parameter change, and exact-version pinning conclusion status: uninspected. Evidence: SRC-1 `run_benchmark.py:201-220` consumes a CSV `embedding` column and never invokes an embedding model. The source boundary establishes selector wiring, not the method that produced these vectors.

### Operative objects

### OBJ-1 — Cheatsheet text

Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:386-455,530-575,630-662`; `prompts/curator_prompt_for_dc_cumulative.txt:18-41,60-78,98-128`; `dynamic_cheatsheet/utils/extractor.py:62-86`. Implementation conclusion status: wired. It is an in-memory string with JSONL persistence through RTE-1, optionally initialized by RTE-8. It contains natural-language strategies and may contain executable symbolic examples. The generator and curator consume it as reference knowledge and prescriptive guidance, without a structural authority boundary separating examples from instructions. Curation derives it from solution traces and the previous sheet. Question references and usage counts are embedded display text, not independently maintained access metadata. The parser extracts the first opening-tag segment and accepts content even without a closing tag; absence of an opening tag falls back to the supplied old value. No semantic acceptance check runs.

>     if "<cheatsheet>" in response:
>         try:
>             txt = response.split("<cheatsheet>")[1].strip()
>             txt = txt.split("</cheatsheet>")[0].strip()
>             return txt
>         except:
>             return old_cheatsheet
>     else:
>         return old_cheatsheet
>
> --- `dynamic_cheatsheet/utils/extractor.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>    - Clearly state any assumptions, limitations, or dependencies (e.g., specific Python libraries or solution hacks).
>
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>    - Focus on key insights or strategies that make solutions correct and effective.
>
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

These prompt lines request conditions and reasons; later whole-sheet delivery makes retained explanations available. The acceptance code does not require them.

### OBJ-2 — Accumulated prior input/output history

Evidence: SRC-1 `run_benchmark.py:176-189,201-225,253-280`; `dynamic_cheatsheet/language_model.py:457-575`. Implementation conclusion status: wired. Inputs come from the dataset ordering; outputs are full returned generator strings, not merely extracted answers. They remain lists in memory and fields in JSONL checkpoints. Retrieval and full-history format them into reference text. This is raw trace retention, not itself trace learning. Checkpoints additionally retain step prompts, old/new sheets and targets; those diagnostic fields are not all replayed after resume. Only final outputs and the last sheet are restored into the continuing memory route.

>         # Load the previous cheatsheet from the last output (if available)
>         last_cheatsheet = outputs[-1].get("final_cheatsheet")
>         if last_cheatsheet is not None:
>             cheatsheet = last_cheatsheet
> 
>         generator_outputs_so_far = [output["final_output"] for output in outputs]
>
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-3 — Precomputed query embeddings

Evidence: SRC-1 `run_benchmark.py:201-220`; `dynamic_cheatsheet/language_model.py:503-525,588-608`. Implementation conclusion status: wired. CSV input strings and numeric vectors are imported and reordered against dataset inputs by exact string lookup, then sliced to the current prefix. They are access metadata, not distilled experiences: vectors rank prior questions, whose corresponding generated answers are fetched by list index. The code does not construct or update these embeddings as outputs accumulate. This is a vector substrate implemented by arrays and cosine similarity, without a vector database. Generation model weights are outside this mechanism.

>         df = pd.read_csv(embeddings_path)
>         questions = df["input"].tolist()
>         embeddings = df["embedding"].apply(ast.literal_eval)
>         embeddings = np.array(embeddings.tolist())  # (N, embedding_dim)
> 
>         # Re-order the embeddings based on the order of the dataset inputs
>         dataset_inputs = [example["input"] for example in dataset]
>         indices = [questions.index(inp) for inp in dataset_inputs]
>         embeddings = embeddings[indices]
>         questions = dataset_inputs
>
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

### OBJ-4 — Generator response and extracted answer

The response contains natural-language reasoning, optional Python code, tool output and an extracted final-answer string. It is a compound work product: the answer part is checked by RTE-7; the full response feeds the curator and later history through RTE-1. Implementation conclusion status: wired; operation conclusion status: observed for the selected SRC-2 examples. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:419-454`; `dynamic_cheatsheet/utils/extractor.py:12-59`. The answer extractor locates tags or a final-answer header and returns a sentinel on failure; extraction grants format-level operational use, not truth. SRC-2 `ExampleUsage.ipynb` cells 5, 9, 13 show a first missing final answer followed by two identical valid arithmetic expressions, `6 - ((5 - 8) * 6)`, on the same input. This comparison shows successful later solutions, not an isolated effect of criticism or memory.

>       "1. Implement the algorithm from the cheatsheet to systematically test all permutations, operator combinations, and parenthesized groupings.\n",
>       "2. Evaluate each expression to check if it equals 24.\n",
>       "3. Return the first valid expression found.\n",
> --- [Pinned source](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/ExampleUsage.ipynb#L466-L468)

### OBJ-5 — Dataset-target and evaluation-result envelope

This canonical seed is superseded by OBJ-8 and OBJ-9 because supplied targets and computed verdicts have different producers, consumers and authority. Its identity is preserved as the original compound envelope; it supplies no independent finding.

### OBJ-6 — Shipped generator and curator instructions

Static natural-language files loaded from the operator's paths, not accumulated memory. Implementation conclusion status: wired at SRC-1 `run_benchmark.py:97-104`; guidance content at `prompts/generator_prompt.txt:9-40`, `prompts/curator_prompt_for_dc_cumulative.txt:3-41`, and `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:13-53`. The generator is told to examine reference limitations and verify assumptions; the curator is told to assess correctness, retain useful strategies, remove repetition and improve generality. These instructions formulate a procedure and an improvement objective. Their presence establishes an invoked request for model judgment, not successful checking of every memory entry. No inspected update rewrites these static prompt files.

The quoted correctness instruction is retained on RTE-2, the route that invokes it.

### OBJ-7 — Provider code-interpreter state

The OpenAI path retains a provider container identifier on the wrapper for reuse during the benchmark; Claude uses a sentinel that enables a per-request native tool. Storage substrate: service-object for the hosted container interface. Payload form, content retention and lifetime: uninspected provider internals. Interface conclusion status: wired. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:153-172,212-234`; `run_benchmark.py:120-123`; `text_generation/simple_unified_client.py:1077-1153,1182-1210`. This state must not be treated as inspected cheatsheet storage or as proof of cross-request artifact reuse.

### OBJ-8 — Supplied benchmark targets

Structured dataset fields, loaded from local datasets or the configured Game of 24 dataset service. Implementation conclusion status: wired. Evidence: SRC-1 `run_benchmark.py:131-137,232-244,274-297`. The benchmark evaluator is given the expected target for AIME, multiple-choice and equation tasks. The curator receives the generated answer, not this target. The target supplies answer authority only inside the corresponding benchmark check; dataset correctness and provenance are not established by loading it.

### OBJ-9 — Computed answer score

Boolean result and aggregate counters produced by RTE-7, held in process and printed. Symbolic computation over the answer/target or problem constraints. Implementation conclusion status: wired. Evidence: SRC-1 `run_benchmark.py:290-309`. Its force is reporting benchmark correctness; it neither accepts nor rolls back OBJ-1. It is separate from claims inside generated explanations and cheatsheets.

### Routes

### RTE-1 — Benchmark orchestration and checkpoint/resume

Evidence: SRC-1 `run_benchmark.py:69-78,133-189,197-225,246-280,308-315`. Implementation conclusion status: wired. Each dataset example triggers a generation call; final output is appended and final_cheatsheet becomes the next current sheet. JSONL is rewritten with the full output list after evaluation and once again at the end. Resume imports all rows, restores the last final_cheatsheet if non-null, restores every final_output, and skips len(outputs) examples. This supplies cross-question continuity and crash recovery only at completed checkpoints. The writer is a plain overwrite, not atomic replacement. Resume checks seven named arguments but not dataset identity/content, shuffle choice, embedding contents, seed content or all prompt/settings fields; pairing resumed outputs with reconstructed input order therefore depends on operator consistency. A fresh native container is created before resume when requested; its ID/state is not restored from the JSONL.

>     with open(file_path, "w") as file:
>         for line in data:
>             file.write(json.dumps(line) + "\n")
>
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>             original_input_corpus=questions[:idx+1],
>             original_input_embeddings=embeddings[:idx+1] if args.approach_name in RETRIEVAL_APPROACHES else None,
>             generator_outputs_so_far=generator_outputs_so_far,
>             retrieve_top_k=args.retrieve_top_k,
>             use_code_interpreter=args.use_code_interpreter,
>         )
> 
>         generator_outputs_so_far.append(output_dict["final_output"])
>
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Runtime audit: principal is the CLI operator; owner is the benchmark loop, whose symbolic policy sequences examples and writes checkpoints. Immediate return is a saved result list and printed summary; later consumers receive last-sheet and output-list state through the selected generation branch. Selection is positional prefix plus the chosen task ordering; delegated visibility is only the contexts supplied to model calls. No TTL or invalidation applies; retained snapshots persist until external file changes. Effect boundary is local files and called provider routes. Recovery is reload/skip at completed checkpoints, with no atomic-write guarantee. No new theory is proposed by unchanged serialization. Imported seeds and restored content are admitted by RTE-8, not revalidated here.

### RTE-2 — Cumulative generator/curator loop

Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:386-455`; `prompts/curator_prompt_for_dc_cumulative.txt:13-41,60-78,98-149`. Implementation conclusion status: wired. Each round supplies the whole current sheet to the generator, then sends input, full solution and old sheet to the curator. The extracted replacement is used next round and returned for the next question. With max_num_rounds greater than one, same-question answers are also appended as unverified annotations. Curator code execution is disabled. The initial caller may choose a template lacking the expected slots; benchmark default curator text is `(empty)` if no path was supplied, so selecting a cumulative branch alone does not guarantee the intended curation prompt is loaded.

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
>
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>    - Refine and update content: Continuously update and improve the content of the cheatsheet by incorporating new insights and solutions, removing repetitions or trivial information, and adding efficient solutions.
>    - Ensure practicality and comprehensiveness: Provide critical and informative examples, as well as efficient code snippets and actionable guidelines. 
> 
> Before updating the cheatsheet, however, you should first assess the correctness of the provided solution and strategically incorporate code blocks, insights, and solutions into the new cheatsheet. Always aim to preserve and keep correct, useful, and illustrative solutions and strategies for future cheatsheets.
>
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> 4. Implement a Usage Counter
>    - Each entry must include a usage count: Increase the count every time a strategy is successfully used in problem-solving.
>    - Use the count to prioritize frequently used solutions over rarely applied ones.
>
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> N.B. Keep in mind that once the cheatsheet is updated, any previous content not directly included will be lost and cannot be retrieved. Therefore, make sure to explicitly copy any (or all) relevant information from the previous cheatsheet to the new cheatsheet!!!
>
> --- `prompts/curator_prompt_for_dc_cumulative.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The usage-count instruction is an implemented model-mediated salience request. Counts are neither measured nor validated by Python; they should not be described as a reliable success-frequency tracker. Replacement can lose un-copied content even though old step snapshots remain in the checkpoint. That is whole-sheet evolution with possible omission, not an explicit decay or history-preserving invalidation mechanism.

Runtime audit: each problem/round triggers Python-owned generator then curator calls. The generator sees the whole current sheet; curator sees that sheet, question and full response. Immediate return is answer, steps and successor sheet; RTE-1 or an explicit API consumer supplies it later. Curator model proposes, judges and selects semantic content; the parser can only refuse an unextractable replacement. Human input is initial configuration, with no in-loop veto. No independent answer oracle is available. No expiry is applied; omitted text is lost to ordinary next-round delivery. Old checkpoint steps permit manual recovery but are not automatically replayed. Provider sees its supplied messages. The model's guidance force is advisory/prescriptive, not guaranteed activation. Guidance and revision classification: OBJ-6 shapes the proposed sheet by requesting useful, correct, reusable strategies and examples. The content may state tentative solutions in prose/code; retained explanations are visible to later generators when kept inside the sheet. Theory-builder conditions 1–4: localized-content conclusion status: wired; content-consuming route conclusion status: wired; content-directed criticism with resulting revision conclusion status: uninspected; iteration of a criticism result conclusion status: uninspected. The last two findings concern inaccessible model judgment, not missing rationale alone. Ordinary sheet replacement and later delivery do not fill that gap. Learning attributable to criticism conclusion status: uninspected. Addressability is textual strategy/example units inside a whole-string replacement; persistence is the branch's returned sheet and RTE-1 checkpoint, reaching later problems, with same-problem rounds additionally supported only by RTE-2.

### RTE-3 — Retrieval and retrieval-synthesis variants

Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:503-575`; `prompts/curator_prompt_for_dc_retrieval_synthesis.txt:13-29,35-53,123-146`. Implementation conclusion status: wired. On each query the automatic selector compares its final supplied embedding with the prefix of prior embeddings, chooses top-k, retrieves aligned prior inputs/outputs, and formats them in reverse similarity order so the most similar example is closest to the question. Pure retrieval delivers this block directly and ignores the incoming sheet. Retrieval-synthesis instead gives the block, next input and previous sheet to a curator; extracted text is delivered immediately to the generator and returned for subsequent questions. Malformed curator output falls back to the retrieved block, not to the previous synthesized sheet. The code records the resulting sheet as current_cheatsheet with new_cheatsheet null; that null does not mean synthesis was absent.

>                 similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
>                 top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
>                 top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
>                 top_k_similar_values = similarities[0][top_k_indices]
>
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

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
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> Continuous Refinement & Optimization:
> - Improve existing strategies by incorporating more efficient, elegant, or generalizable techniques.
> - Remove duplicate entries or rephrase unclear explanations for better readability.
> - Introduce new meta-strategies based on recent problem-solving experiences.
>
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The curation operations consolidate, dedup, evolve and synthesize are supplied as instructions to an automatic model transform. New claims may be produced; they are not externally verified. The generator sees retained reasons only insofar as the transform kept them. Empty history remains a supported case; zero or negative retrieve_top_k values are not guarded in this branch and follow Python slicing semantics.

Runtime audit: each query triggers Python cosine selection from the prior prefix using the current query vector; the generator does not request retrieval. Similarity ranking selects raw examples; on synthesis, curator judgment additionally selects/rewrites retained material from those examples and the whole old sheet. Immediate return is answer and current synthesized/formatted sheet. RTE-1 retains outputs and sheet; pure retrieval later rebuilds from raw history. No expiry or semantic rejection applies; malformed synthesis falls back to selected raw history. No human veto or external answer oracle participates. Provider receives only the constructed contexts; embedding alignment and available context capacity are required external/input contracts. Guidance and revision classification: OBJ-6 shapes the proposed sheet by requesting useful, correct, reusable strategies and examples. The content may state tentative solutions in prose/code; retained explanations are visible to later generators when kept inside the sheet. Theory-builder conditions 1–4: localized-content conclusion status: wired; content-consuming route conclusion status: wired; content-directed criticism with resulting revision conclusion status: uninspected; iteration of a criticism result conclusion status: uninspected. The last two findings concern inaccessible model judgment, not missing rationale alone. Ordinary sheet replacement and later delivery do not fill that gap. Learning attributable to criticism conclusion status: uninspected. Addressability is textual strategy/example units inside a whole-string replacement; persistence is the branch's returned sheet and RTE-1 checkpoint, reaching later problems, with same-problem rounds additionally supported only by RTE-2.

### RTE-4 — Hybrid cumulative/retrieval variant

Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:577-662`. Implementation conclusion status: wired. It retrieves similar prior examples when embeddings are present, combines them with the whole cumulative sheet for a single generator call, then curates from the current problem, generator solution and old cumulative sheet. The retrieved block is not a direct curator argument, although its influence can enter via the generated solution. The replacement cumulative sheet is returned; raw retrieved examples remain in diagnostic fields. max_num_rounds is not used in this branch. The standard cumulative curator prompt provides the same rationale and curation requests as RTE-2, without guaranteeing their preservation.

>             # --- Build combined cheatsheet for the generator ---
>             combined_cheatsheet = cheatsheet
>             if retrieved_section:
>                 combined_cheatsheet = f"{cheatsheet}\n{retrieved_section}"
> 
>             # --- Generator step ---
>             generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", combined_cheatsheet)
>
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

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
>
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Runtime audit: one call triggers Python retrieval and context combination, then generator and curator model decisions. Selection uses current-vector top-k plus the whole cumulative sheet; curator chooses a successor using old sheet and generated response. Immediate return is answer, diagnostics and replacement cumulative sheet; RTE-1 carries it forward. A tag failure keeps old cumulative text; no truth-based veto or expiry exists. Reusing saved old steps is manual recovery. Human role is configuration; no answer oracle is sent to the curator. Both provider calls receive constructed user messages, with raw retrieval influencing curation indirectly via the response. Guidance and revision classification: OBJ-6 shapes the proposed sheet by requesting useful, correct, reusable strategies and examples. The content may state tentative solutions in prose/code; retained explanations are visible to later generators when kept inside the sheet. Theory-builder conditions 1–4: localized-content conclusion status: wired; content-consuming route conclusion status: wired; content-directed criticism with resulting revision conclusion status: uninspected; iteration of a criticism result conclusion status: uninspected. The last two findings concern inaccessible model judgment, not missing rationale alone. Ordinary sheet replacement and later delivery do not fill that gap. Learning attributable to criticism conclusion status: uninspected. Addressability is textual strategy/example units inside a whole-string replacement; persistence is the branch's returned sheet and RTE-1 checkpoint, reaching later problems, with same-problem rounds additionally supported only by RTE-2.

### RTE-5 — Full-history and default branches

Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:351-384,457-501`. Implementation conclusion status: wired. Full history automatically supplies all zipped prior input/output pairs with no curation or input-token budget. The returned final_cheatsheet is that formatted history, but the next full-history call rebuilds from the accumulated raw lists rather than consuming that string. Default substitutes `(empty)` and returns no sheet, even if the caller supplied one. Neither branch performs trace learning by itself. Full-history content is raw replay; a formatted string named cheatsheet is not necessarily a derived memory theory.

>         if approach_name == "default":
>             generator_prompt = generator_template.replace("[[QUESTION]]", input_txt).replace("[[CHEATSHEET]]", "(empty)")
>             generator_history = [
>                 {"role": "user", "content": generator_prompt},
>
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

>                 curated_cheatsheet = "### PREVIOUS SOLUTIONS (START)\n\n"
>                 for i, (previous_input_txt, previous_output_txt) in enumerate(zip(original_input_corpus, generator_outputs_so_far)):
>                     curated_cheatsheet += f"#### Previous Input #{i+1}:\n\n{previous_input_txt}\n\n#### Model Solution to Previous Input #{i+1}:\n\n{previous_output_txt}\n---\n---\n\n"
>                 curated_cheatsheet += "#### PREVIOUS SOLUTIONS (END)"
>
> --- `dynamic_cheatsheet/language_model.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Runtime audit: Python selects the branch per caller setting; default uses empty reference and full-history uses all zipped prior pairs without a model request. Immediate return is answer plus null or formatted raw history; later full-history calls read the growing raw lists from RTE-1, not the returned formatted string. No history curation, expiry, semantic admission or truth-based rollback occurs. The provider receives the assembled message; missing/misaligned caller lists can fail or truncate by zip semantics. The branch derives no new memory theory. Provider retry and output extraction follow RTE-6.

### RTE-8 — Caller initialization and adoption surface

Evidence: SRC-1 `run_benchmark.py:170-189`; `README.md:100-120`; `dynamic_cheatsheet/language_model.py:290-306`. Implementation conclusion status: wired. A benchmark operator chooses a text file whose entire content becomes the initial sheet; a non-null resumed last sheet overrides it. The documented API caller supplies a string and can pass the returned sheet into the next query. Authoring or editing that supplied text is afforded, not observed. There is no dedicated editor, approval queue, item identity check or provenance gate. Initial text can thus supply authored advice or imported prior memory, but arbitrary external consumers of the return dictionary are outside scope.

>     # Initialize the cheatsheet
>     cheatsheet = "(empty)"
>     if args.initialize_cheatsheet_path is not None:
>         with open(args.initialize_cheatsheet_path, "r") as file:
>             cheatsheet = file.read()
>
> --- `run_benchmark.py` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

> # Pass the updated cheatsheet to the next query to accumulate knowledge
> next_results = model.advanced_generate(
>     approach_name="DynamicCheatsheet_Cumulative",
>     input_txt="Question #2: 1 3 8 9",
>     cheatsheet=results['final_cheatsheet'],  # Reuse the cheatsheet
>     generator_template=generator_prompt,
>     cheatsheet_template=curator_prompt,
>
> --- `README.md` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Runtime audit: caller/operator owns initial choice and can reject/edit before invocation; file reading and argument passing admit the whole supplied string without semantic checks. Immediate outcome is initialized OBJ-1, then normal branch-specific consumption. Selection is the explicit input path/string, not identifier-based push of memory parts. The later generator/curator gets selected content automatically through its ordinary branch. Rollback is supplying a different seed or checkpoint. Retained seed content, reasons, criticism and theory quality are uninspected until supplied; this interface alone establishes neither a theory-building process nor learning. Persistence is the caller object or seed file and subsequent RTE-1 checkpoints; no invalidation/expiry is supplied. Interface use is wired; human authorship is afforded, not observed.

### RTE-6 — Model dispatch and optional code execution

Trigger: generator or curator call. Owner: `LanguageModel.generate`; model selects generated content, Python chooses the dispatch branch. Context: explicit message list plus current tool outputs; no automatic client chat history in `generate_from_messages`. State: accumulated local recursion text, or OBJ-7 container reference. Immediate return: model text; later read-back occurs when RTE-1 stores it and memory routes consume it. Delegated visibility: remote provider receives supplied messages; a local Python subprocess receives generated code. No independently scheduled sub-agent is involved.

Admission: by default a response containing the execution flag immediately after a code block causes local execution. The caller can disable this branch; curator calls disable it. Guidance: OBJ-6 requests verification and self-contained Python. Generated code is a proposed solution with symbolic semantics; its execution produces output that is returned as feedback, and the next model invocation may revise the answer. The code path has no supplied expected-answer oracle: model reasoning and Python output are evidence, with independent benchmark targets available only in RTE-7. Model chooses what to propose and how to respond to errors; Python admits flagged code; there is no intervening human veto in the running loop. The product revision is an answer/code revision, not automatically a revision to the system's own organization.

Local execution writes a temporary file and launches `python3` with the host process's access. A three-second subprocess timeout and deletion of the temporary file provide bounded recovery, not sandbox isolation. The recursion test occurs after execution; its default depth setting does not cap execution at three invocations because the depth-four call can execute before returning. Provider-hosted execution is selected separately and disables the local branch. A missing container with that flag falls back to ordinary generation with local execution disabled. Native provider limits, approval and isolation remain uninspected; local timeout does not govern them. The direct task evaluators also use Python `eval`, so disabling generator code does not remove every evaluation effect path.

Provider retries cover dispatch exceptions for three configured attempts with a fixed delay; exhausted calls raise. No transaction or idempotency guarantee covers remote effects retried after uncertain failures. Empty responses become a sentinel. Parameters and provider names determine the current grant; arbitrary extra parameters expand the interface, while actual deployment credentials and operating-system restrictions are uninspected. Expiry/invalidation: local temporary code deleted, recursion abandoned at return; provider state expiry uninspected. Terminal output is text returned to the enclosing variant.

Implementation conclusion status: wired. Guarantee strength: protocol for branch selection and bounded retries; no claimed isolation guarantee. Evidence: SRC-1 `dynamic_cheatsheet/language_model.py:174-288,347-349`; `dynamic_cheatsheet/utils/execute_code.py:45-101`; `text_generation/simple_unified_client.py:395-431,534-583,1077-1210`; `dynamic_cheatsheet/utils/evaluation.py:47-81,151-170`.

>     try:
>         # In case alias python=python3 is not set, use python3 instead of python
>         process = Popen(["python3", temp_file.name], stdout=PIPE, stderr=PIPE)
>         stdout, stderr = process.communicate(timeout=timeout)
> --- [Pinned source](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/execute_code.py#L81-L84)

### RTE-7 — Task-specific answer evaluation

Trigger: each benchmark answer after curation. Owner: deterministic benchmark code. Input: OBJ-4 answer part plus OBJ-8 target or the Game of 24 numbers. Evaluator: exact-match normalization for AIME, permissive option/text matching for multiple choice, arithmetic-expression and number checks for Game of 24 and equation balancing. The arithmetic evaluators execute Python expressions; successful computation does not validate the model's explanation or general strategy. Immediate return: OBJ-9 boolean, then counters/printed summary. Selection: task-name branch, not memory retrieval. Later read-back and delegated consumption of the score: inapplicable in this loop; score is not supplied to the next generator or curator. No score-based veto, candidate replacement or rollback occurs. Persistence of the answer/target is in RTE-1; the runtime score itself is reporting state. Recovery: evaluator-specific exception handling returns false for some arithmetic failures; the enclosing process can still fail on other malformed inputs. Terminal output: aggregate summary. Implementation conclusion status: wired. Guarantee strength: invariant of the inspected call order that curation precedes grading, not a correctness guarantee for graders.

Evidence: SRC-1 `run_benchmark.py:253-309`; `dynamic_cheatsheet/utils/evaluation.py:47-112,151-266`. Answer oracle: dataset target for AIME, multiple-choice and equation tasks; explicit target value 24 plus number-use constraints for Game of 24. Authority is limited to this encoded answer domain. It cannot warrant memorized rules, transfer or the producing process.

>         if args.task == "GameOf24":
>             result = eval_for_GameOf24(original_input, final_answer)
>         elif args.task in ["AIME_2025", "AIME_2024", "AIME_2020_2024"]:
>             result = eval_for_exact_matching_with_no_punctuation(final_answer.lower(), original_target.lower())
>         elif args.task in ["GPQA_Diamond", "MMLU_Pro_Engineering", "MMLU_Pro_Physics"]:
>             result = eval_for_multiple_choice(current_input, final_answer, original_target)
>         elif args.task == "MathEquationBalancer":
>             result = eval_equation_balancer(None, final_answer, original_target)
>         else:
>             raise ValueError(f"Task {args.task} not supported.")
> 
>         if result:
>             correct_so_far += 1
>         total_so_far += 1
> --- [Pinned source](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py#L290-L303)

### Claims

### CLM-1 — Accumulate and reuse insights without parameter updates

Claim conclusion status: claimed. SRC-1 `README.md:9-20` says the framework gives black-box models evolving inference-time memory and reusable strategies. RTE-1, RTE-2, RTE-3 and RTE-4 wire that text-retention account; RTE-5 supplies uncured alternatives. SRC-2 gives selected retained instances and later consumption. The statement about model parameters is bounded by CMP-1: client code does not train, but remote internals are not inspected.

> Dynamic Cheatsheet (DC) endows black-box language models with the ability to store and reuse insights across queries. Rather than repeatedly re-discovering solutions or making the same mistakes, DC enables models to accumulate and leverage strategies, code snippets, and problem-solving techniques without modifying the underlying model parameters.
> --- [Pinned source](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md#L13-L13)

### CLM-3 — Retained samples show delivery, reasons, code and imperfect curation

Evidence: SRC-2 `results/AIME_2025/gpt-4o_DynamicCheatsheet_Cumulative.jsonl:1-2`, `results/AIME_2025/gpt-4o_DynamicCheatsheet_RetrievalSynthesis.jsonl:1-2`, and selected retained output cells 7, 11 and 14 of `ExampleUsage.ipynb:142,255,446`. Operation conclusion status: observed. Decoding the first two cumulative rows shows a 3642-character first sheet containing a grid-solving description, Python functions and reasons/constraints; that complete first sheet occurs in the next row generator_prompt. The second final sheet is unchanged in this sample. This proves retained delivery and mixed content, not successful revision after each problem or a measured performance gain. The first solution includes code output and a final answer of 16; no ground-truth acceptance precedes curation in the wired path.

> "final_cheatsheet": "Version: 1.0\n\nSOLUTIONS, IMPLEMENTATION PATTERNS, AND CODE SNIPPETS\n\n<memory_item>\n<description>\nCounting valid configurations in a constrained combinatorial grid problem. This approach is useful for problems involving grids, shared edges, and specific constraints on substructures (e.g., coloring, tiling, or partitioning problems). (Reference: Q1)\n</description>\n<example>\nProblem: Count the number of valid colorings of a \\(2 \\times 2\\) grid where each square has exactly 2 red and 2 blue edges, and shared edges between adjacent squares must be consistently colored.\n\nSolution:\n1. Represent the grid as a set of edges.\n2. Define constraints for each square and shared edges.\n3. Enumerate all possible configurations and filter valid ones.\n\nPython Code:\n```python\nfrom itertools import product\n\ndef is_valid_coloring(grid):
>
> --- [Cumulative sample, row 1](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/results/AIME_2025/gpt-4o_DynamicCheatsheet_Cumulative.jsonl#L1)

The retrieval-synthesis sample has a 37-character first final sheet consisting of `(empty)` and a previous-solutions end marker. Its second final sheet contains generalized combinatorial strategies. The old first sheet is not literally present in the next generator prompt. This is compatible with a transform rather than literal replay, but saved prompts/outputs do not prove which revision produced it. In particular, the sampled empty-history marker differs from current code formatting. Keep historical operation evidence separate from current implementation evidence.

The example notebook saves an invalid initial proposed 24-game solution, then a revised valid solution and Python search code. Its later generator output explicitly lists cheatsheet insights and plans. These are observed expressions of use, not controlled dependence tests. The initial proposed expression evaluates to 96, not 24, and uses three sixes although the input has two. This concrete retained counterexample limits the curator prompt claim that only tested/proven solutions enter memory.

>       "Example Solution: \\((8 / (6 - 5)) * (6 + 6) = 24\\)\n",
>
> --- [Saved initial cheatsheet](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/ExampleUsage.ipynb#L142)

>       "### Cheatsheet Insights:\n",
>
> --- [Saved generator output](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/ExampleUsage.ipynb#L446)

### CLM-2 — Improvement without ground-truth feedback

Claim conclusion status: claimed. SRC-1 `README.md:21-35` reports AIME, Game of 24, arithmetic and knowledge-task improvements. The strongest inspected local contribution is the notebook's successful later solution and explicit reuse of a retained algorithm on the same puzzle, after an unsuccessful first response. This is observed recurrence and task success, not a controlled memory intervention. The README's broader metrics remain claims; the evidence inspected here does not isolate criticism of a theory as the cause of improvement. Ground-truth-free *curation* is consistent with the code, while the benchmark still uses answer oracles for scoring.

> * **Mathematics**: Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams by retaining algebraic insights
> * **Puzzles**: GPT-4o's success rate on Game of 24 increased from approximately 10% to 99% after discovering and reusing Python-based solutions
> * **Arithmetic**: Near-perfect accuracy on tasks like balancing equations (compared to baseline ~50%)
> * **Knowledge-Intensive Tasks**: 9% improvement on GPQA-Diamond and 8% boost on MMLU-Pro Engineering and Physics problems
> 
> --- [Pinned source](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md#L25-L30)

### Evidenced absences

### ABS-1 — No semantic memory admission gate in the inspected Python path

Conclusion status: absent. Boundary: SRC-1 full `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py` and `run_benchmark.py` at the pinned commit. Search query: `target|eval_|extract_cheatsheet|result`, followed through every matched update and grading call. The curator receives question, model output and prior memory; a tagged result replaces memory before answer grading, and grading changes counters only. The extraction code checks tag presence, not truth, provenance or rationale. This establishes no supplied-target, semantic or score-based memory gate on RTE-2, RTE-3, RTE-4 through RTE-1. It does not establish absence of criticism formulated inside model reasoning, a separate human experiment, or an external API caller's own gate. Supporting quoted update and grading passages are retained on their routes.

### Behavioral-authority paths

### BAP-1 — Accumulated reference material to generator and curator

Consumer: later generator and curator model invocations. Channels: user-message templates filled by RTE-2, RTE-3, RTE-4 and RTE-5; checkpoints restored through RTE-1 and seed input through RTE-8. Force: advisory knowledge and prescriptive strategy text; embeddings rank which old examples enter the channel. Horizon: same-problem cumulative rounds and subsequent problems; checkpoint restoration permits cross-process continuation. Delivery conclusion status: wired; expressed strategy consumption conclusion status: observed in CLM-3 and OBJ-4, without causal dependence or success guarantees. SRC-1 `dynamic_cheatsheet/language_model.py:396-455,457-575,588-661`; SRC-2 evidence on CLM-3. Current-run code recursion is outside this memory path until its trace is retained and curated. No trust partition separates an old example's assertions from its instructions.

### BAP-2 — Generated code to local execution

Consumer: host Python interpreter; channel: extracted code written to a temporary file; force: execution admitted by RTE-6's flag and caller setting; horizon: one subprocess and its host-visible effects. Conclusion status: wired. SRC-1 `dynamic_cheatsheet/language_model.py:249-284`; `dynamic_cheatsheet/utils/execute_code.py:75-99`. Output is feedback to the next model call, not epistemic endorsement of its source.

### BAP-3 — Benchmark verdict to reported score

Consumer: benchmark counter/reporting code; channel: boolean return; force: reporting only, no veto over memory; horizon: current benchmark run. Conclusion status: wired. SRC-1 `run_benchmark.py:290-309`. Epistemic license concerns encoded final-answer correctness; no memory acceptance authority follows.

## Runtime account

The ordinary CLI invocation loads operator-selected prompts and a provider/model, initializes memory and output history, optionally resumes a prior JSONL, and walks a dataset in fixed-seed shuffled or original order. RTE-1 owns sequence and checkpoints. RTE-2 solves one problem with the current cheatsheet, calls the same model as curator, extracts a successor, and returns both work product and memory. RTE-6 provides optional code feedback while solving. RTE-7 grades only after that successor is already adopted. Checkpoints preserve inputs, targets, reasoning/answers, steps and cheatsheets; resume reconstructs memory and history and skips the saved count of examples. There is no parallel scheduler or agent handoff in this path. Direct Python callers receive the returned dictionary and must carry memory themselves; the README shows that wiring but cannot establish arbitrary host behavior.

The materially different variants are RTE-3 (similarity selection, optionally pre-answer synthesis), RTE-4 (combined cumulative and retrieved context, post-answer update), and RTE-5 (raw full history or empty reference baseline). A missing/failed curator extraction preserves prior memory or the retrieved fallback, depending on the branch. Prompt replacement and tag parsing are protocol boundaries; no semantic admission test proves that a successor preserves useful content. Checkpoint writes overwrite the output file rather than creating atomic transactional snapshots; resume checks selected argument equality, not every artifact hash. This bounds the crash-recovery promise.

The forcing cases inspected statically were: malformed curator output; a wrong benchmark answer retained before scoring; resume versus fresh initialization; and local execution disabled versus provider-hosted execution enabled. Relevant paths are RTE-1, RTE-2, RTE-3, RTE-4, RTE-6 and RTE-7. These cases expose the actual admission and recovery points without requiring live model behavior.

Execution-preflight disposition: **no dynamic check planned**. Considered model reruns, code-execution timeout probes, malformed-tag probes and checkpoint crash probes. Static branches suffice for the bounded wiring claims, while a live model rerun would require provider access and would not by itself isolate memory or criticism effects. No target execution was attempted; no probe or causal status is claimed. Reading/decoding historical artifacts is source inspection, not a new benchmark run.

Actors and operating modes: humans select prompts, model, task, seeds and any initial memory, and can stop the process. During the included loop, models propose answers and memory, make prompt-requested correctness/usefulness judgments, and decide what to retain semantically; code selects contexts, admits tagged text, executes flagged code and persists results. No in-loop human approval is wired. The benchmark is a bounded experiment sequence; the API also serves arbitrary requests. Improvement is triggered after each answer in cumulative/hybrid mode and before each answer from retrieved history in synthesis mode, not only after a failed grade. Answer-oracle use belongs to the benchmark evaluation mode. Whether model criticism genuinely assigns blame to a retained strategy remains a separate evidence question.

## Lens scoping

### Memory/context scope

Depth: full. Trigger evidence: CLM-1, OBJ-1, OBJ-2, OBJ-3 and RTE-1 through their source anchors. Boundary: all six local generation alternatives, RTE-8 initialization, RTE-1 checkpoint/resume, and RTE-2, RTE-3, RTE-4 curation/read-back. RTE-5's raw-history/default branches are explicitly included; their lack of curation does not remove them from storage and retrieval coverage. RTE-6 is an upstream tool-trace producer. Temporary recursion, static prompts, provider-internal contents/weights and unspecified external consumers are excluded from memory classifications. A full lens is warranted because whole-sheet rewriting, selected history, hybrid context and resume impose different retention and consumption contracts. Frozen input SHA-256: `8978ab2a363888701ac0f50361b0f25515abd64724357d07352230b74612f8d6`.

### Epistemic scope

Depth: full. Trigger evidence: CLM-1, CLM-2 and OBJ-6's correctness and improvement instructions. Boundary: the frozen workflow and selected SRC-2 artifacts. Canonical targets: OBJ-1, OBJ-2, OBJ-3, OBJ-4, OBJ-6, OBJ-7, OBJ-8, OBJ-9; routes RTE-1, RTE-2, RTE-3, RTE-4, RTE-5, RTE-6, RTE-7. The question is whether producing, grading and retaining a solution supplies warrant for the strategies later consumed. All material workflow route families are assessed; provider-internal checking and unused independent client APIs are not. This warrants a full lens because checking and operational adoption have different owners and timing.

## Lens outputs

### Memory/context lens

The persistent unit is caller-carried text, not state hidden inside LanguageModel. The benchmark keeps a current sheet and previous generator outputs, passes them into the next call, and writes a JSONL checkpoint after each completed example. Cumulative curation rewrites the whole sheet after solving; retrieval-synthesis rewrites before solving from the previous sheet, selected old solutions and the next question. Hybrid adds retrieved examples to a cumulative sheet but retains only the newly curated cumulative sheet as its next persistent value. Raw retrieval and full-history variants replay earlier solutions without producing learned summaries. The default branch discards the supplied sheet. Evidence and minimal retained passages are on RTE-1, RTE-2, RTE-3, RTE-4 and RTE-5 below.

Memory can carry reasons: curator instructions request contextual descriptions, assumptions, worked examples and explanation of what makes a strategy effective. These fields remain ordinary text. Later generators and curators receive the entire retained sheet, including any reasons preserved inside it. There is no separate rationale store or reason-specific retrieval. SRC-2 demonstrates some explanatory content, but neither the parser nor checkpoint writer requires it. This supports a rationale-bearing route, not guaranteed rationale preservation.

Context selection trades completeness for size. Cumulative state has a prompt-level 2000–2500-word suggestion and a curator completion-token limit of twice the generator limit; no code enforces a retained-input token budget. Full history grows with every solution. Retrieval scores every earlier vector and fully sorts the similarities, then takes top-k (default three); it does not bound the token lengths of those examples. Retrieval-synthesis still supplies the complete previous sheet to its curator. Model-based selection is automatic but may preserve errors; verification and usage counts are prose obligations, not checked fields.

#### Write side

Acquisition has three distinct sources. RTE-8 admits supplied text; RTE-1 imports an existing output checkpoint; OBJ-3 imports precomputed access vectors. Generation automatically appends new raw solution traces to OBJ-2. Curator transformations in RTE-2 and RTE-4 consume the just-generated trace after a solve; RTE-3 consumes selected earlier traces before the next solve. All three carry prior derived memory too. The chain is therefore raw solution, model-produced sheet, extracted accepted string, caller/checkpoint retention, later generator or curator prompt. There is no asynchronous training step, weight update, background consolidation job or separate compaction subsystem in the inspected branches.

Cumulative max_num_rounds makes that chain operate within one problem as well as across subsequent questions. Retrieval-synthesis and hybrid have one generator pass per advanced_generate call. The benchmark calls its dataset selection a task, but each question is a separate problem; this establishes cross-task learning under the comparison definition. Offline restore is persistence, not offline learning. Local code observations participate in the same online route through the full generator output; native-provider tool internals cannot be assumed to survive the text projection.

Rejection is narrow: missing required arguments raise errors in cumulative/hybrid; absence of cheatsheet tags retains an old value, except retrieval-synthesis uses the raw retrieved block as its fallback. Curator output outside the extracted block is discarded, including any explanation left there. Within-block reasons and code are carried forward and read whole; no required field prevents a later rewrite from dropping them. Maintenance is model-mediated whole-sheet replacement with requested refinement, duplicate removal, generalization and salience changes. Withdrawal has no stable item tombstones or separate invalidation operation. Old sheets survive only in saved step records and can be manually reimported; normal generation does not retrieve omitted old sheet sections from those records.

#### Read-back

| Route | Automatic selection and later consumer | Delivery and bound |
|---|---|---|
| RTE-2 | Current whole sheet to generator; old sheet plus current solution to curator | User-message template; optional previous answers after first round; no input-token cap |
| RTE-3 retrieval | Current vector ranks prior vectors; corresponding raw solutions to generator | Top-k block, closest example last; count limit only |
| RTE-3 synthesis | Same retrieved block plus old sheet and next question to curator; curator output to generator | Whole extracted sheet; curator limit twice generator max_tokens |
| RTE-4 | Current sheet and ranked examples to generator; sheet/current trace to curator | One generator/curator pair; same top-k and completion limits |
| RTE-5 history | All prior input/output pairs to generator | Entire formatted block; no curation or token budget |
| RTE-5 default | No accumulated sheet selected | Empty placeholder |
| RTE-1 recovery | Last non-null sheet and all saved final outputs to resumed orchestrator | Reconstructed lists subsequently follow chosen branch |

The memory-delivering rows above are push routes from the consuming model roles: selection and context insertion occur without generator-initiated memory requests. The caller requests a solve, not a memory search on behalf of an identified separate consumer. Exact input matching reorders embedding metadata; it does not itself select recalled content for generator delivery, so no identifier signal is assigned. Embedding rank and curator judgment are distinct targeted selectors. Whole current-sheet and history supply are coarse selectors. Model delivery is implemented; a model visibly mentioning an insight in an old sample is observed expressed use, while benefit and causal dependence remain unestablished.

RTE-6 local recursion supplies code and returned observations to a continuing generator within the current episode. That temporary context is outside accumulated-memory read-back. Durable later delivery is established when RTE-1 retains completed responses/sheets and RTE-2, RTE-3 or RTE-4 consumes and curates them; raw prior-task replay through RTE-3 or RTE-5 is separately supported. The push and coarse classifications rely on those retained-material routes, not recursion alone.

#### Comparison rationale

The profile covers all six local alternatives and their shared persistence routes. Shipped static templates define the interpreter of accumulated memory but are not counted as authored memory themselves. Authored lineage and manual agency come only from the caller text surface, at afforded strength. Automatic lineage, curation and push delivery have wired witnesses. Numeric vectors are a symbolic access representation and a vector substrate; they do not establish parametric learning. Files describes CSV/checkpoints, not every repository file. Server-native execution supplies a reused container reference, but its opaque internal contents are excluded rather than inferred to add a known store or learning route.

The curation profile separates requested model work from guaranteed success. The supplied curator prompt is part of a wired transform, so its explicit operations count as wired model-mediated operations. No claim is made that every output performs each operation. Evolution also has direct assignment and later-consumption evidence; CLM-3 observes a correction across example notebook outputs, but unchanged sampled sheets caution against universalizing it. Usage-based priority qualifies as a request to promote salience; no ranking index reads its count. Omission under replacement does not by itself establish a decay policy, and retaining a snapshot of an old sheet does not establish explicit invalidation semantics.

Trace-learning scope, timing and form all describe the same qualifying curator routes: online generation of retained prose/code from trajectories and local tool traces, used in later same-problem rounds or separate benchmark questions. Raw retrieval and full-history replay remain memory routes but add no trace-learning classifications. Faithfulness is not determinable: retained examples demonstrate content delivery and expressed use, while the inspected scoring procedure measures answer correctness. No controlled claim that recalled content caused the output is supported by the reviewed samples.

### Epistemic lens

#### 1. Source-and-claim boundary

Uses SRC-1 implementation and separately marked doctrine/design, plus SRC-2 historical outputs at the reviewed commit. Claims: CLM-1 and CLM-2. Scope, exclusions and prevented conclusions are those above; the overlay does not redefine records. The six blocks implement `kb/instructions/analyse-external-system-epistemic-architecture.md` locally, with the frozen boundary and canonical register.

#### 2. Epistemic-object inventory

| Object | Truth-apt content and lineage | Warrant and gap |
|---|---|---|
| OBJ-1 | Strategies, examples and code claims derived from model solutions; some proposals generalize beyond the observed problem. | Model-curated guidance, not certified knowledge; examples may preserve incorrect answers. |
| OBJ-2 | Imported prior questions, generated reasoning and answers. | Preserves what was generated, not independent truth. Retrieval does not improve source warrant. |
| OBJ-3 | Numerical access structure, not an individually stated candidate proposition. | Similarity licenses selection, not truth or applicability. |
| OBJ-4 | Reasoning, program and answer parts; truth-apt solution claims. | Tool outputs can check particular computations; answer grading checks only final-answer domain. |
| OBJ-6 | Authored method proposals about solving and curating. | Static guidance; tests of these method texts as theories are uninspected. |
| OBJ-7 | Opaque provider state. | Candidate content and epistemic lifecycle not determinable from the client interface. |
| OBJ-8 | Supplied expected answer. | Imported benchmark oracle; underlying warrant not audited. |
| OBJ-9 | Evaluator verdict under encoded conditions. | Derived from answer and target/constraints; does not warrant broader model explanation. |

#### 3. Authority-route ledger

Architectural status for all following implementation rows: **implemented**. Each row is one consequential function. Record-specific anchors remain on the canonical routes. No row converts this architectural status into a conclusion status.

| Route | Function and content/update relation | Target, condition, timing and result | Authority, force and limit |
|---|---|---|---|
| RTE-1 | retention; no content change | After each example, save outputs and next memory; on resume, load previous memory/history. | Preserves candidates for use, grants no epistemic license. BAP-1 governs later model delivery. |
| RTE-2 | content transformation; indeterminate, potentially ampliative conjecture | Model transforms prior sheet and new response after answering. | Prompt requests correctness/usefulness review; new reusable generalizations can exceed evidence. No independent oracle. |
| RTE-2 | disposition/acceptance | Tag parser admits successor text or keeps fallback. | Operational admission only; format is not an evidence-consuming acceptance criterion for memory truth. |
| RTE-3 | operational admission/selection/consumption; no content change | Cosine top-k selects past examples for current input. | Ranking/selective delivery through BAP-1, not validation of selected content. |
| RTE-3 | content transformation; indeterminate | Synthesis model sees selected pairs, next input and previous sheet before answering. | May reshape or conjecture; supplied prompt does not establish preservation or entailment. |
| RTE-3 | disposition/acceptance | Tagged synthesis becomes current context, otherwise retrieved fallback. | Operational use precedes any independent check; no accepted-memory status. |
| RTE-4 | content transformation; indeterminate | Hybrid consumes both history and current sheet, then curates after response. | Same model admission limit as RTE-2, with different evidence context. |
| RTE-4 | disposition/acceptance | Tagged successor or previous cumulative sheet. | Model chooses content; parser controls only extraction. |
| RTE-5 | operational admission/selection/consumption; non-ampliative reshaping for full history, no content change for default | Full-history formatting supplies all previous pairs; default supplies empty reference. | Raw context is advisory; no epistemic promotion. |
| RTE-6 | content transformation; indeterminate | Model produces an answer/program from problem and context. | Candidate generation; particular arithmetic expressions may be derived, broader explanations are not validated by fluency. |
| RTE-6 | check/evidence production; no content change | Execute model-chosen program, return stdout/error to model. | Computation checks encoded consequences only. The model's chosen test can omit the actual task constraint; BAP-2 admits code without a correctness gate. |
| RTE-6 | behavior/policy adaptation | Model may revise its answer after tool output. | Product-level correction; truth-apt revision or mere formatting depends on the particular trace. |
| RTE-7 | check/evidence production; entailed derivation within implemented evaluator semantics | Task-selected final-answer evaluator produces OBJ-9. | Benchmark license only; see BAP-3. Dataset truth, encoding fidelity and all memory claims remain outside this license. |
| RTE-7 | disposition/acceptance; no content change | True increments reported correctness counter, false does not. | Accepts answer for scoring under a named criterion; does not accept or reject the cheatsheet. |

No memory lifecycle-integration row is claimed merely from retention or injection. ABS-1 records the missing benchmark-feedback admission connection. Mismatch: CLM-2's correctness/improvement language is broader than tag admission and similarity selection; code still supports its narrower inference-time update mechanism.

#### 4. Per-object lifecycle disposition

For OBJ-1, content transformation is **indeterminate** across arbitrary model outputs: reshaping, derivation and ampliative conjecture remain possible. The source-native retained strategies make localized content visible, but do not establish that every retained rule follows from its inputs. Conjectural generalization is evidenced where the notebook turns a single puzzle solution into reusable combinatorial strategy; its observation/conjecture architecture is implemented through RTE-2, its observed candidate state is **phase evidenced** for retained text. A separately derived, later-tested prediction about that general strategy is **not determinable** in those artifacts. Memory-wide test and evidence-consuming acceptance architecture: **no route found within boundary** for the supplied-target gate searched in ABS-1, while prompt-directed model judgment is implemented and its particular decisions are **not determinable**. Lifecycle integration observed candidate state: **not reached** for these retained candidates, because no acceptance transition for their truth was established; their operational retention/use is separately observed. A hidden model argument could improve this account but cannot be inferred from the replacement text.

For OBJ-4, the inspected notebook produces and executes a candidate program and then supplies a concrete correct expression. RTE-6's answer generation and tool-feedback phases are implemented; observed candidate state: **phase evidenced**. Its correct arithmetic result licenses that example, not the general completeness or transfer of its search strategy. In the benchmark, RTE-7's acceptance-for-scoring is implemented. For the selected JSONL rows, observed candidate state of the evaluator phase is **not determinable** because answers/targets are retained but evaluator execution is not linked by those records. The first two answer strings disagree with their supplied targets. Operational persistence is observed; epistemic lifecycle integration remains **not reached** for unchecked retained strategy claims.

For OBJ-2 and OBJ-8, transformation: acquisition/import. Discovery lifecycle: not applicable; lineage preserves prior output and supplied target respectively, while their upstream truth warrant is unknown. OBJ-9 is an entailed evaluator output within program semantics; discovery lifecycle: not applicable, with encoding and dataset limits. OBJ-6 is authored static method content: its own discovery lifecycle is uninspected. No lifecycle record for OBJ-3: no candidate truth-apt output for this object; relevant access route RTE-3. For OBJ-7, payload opacity makes the content classification and lifecycle **not determinable**; this is not a finding of no candidate content.

#### 5. System-claim versus route comparison

| Claim | Doctrine/design | Implementation | Observed support | Causal support and bounded conclusion |
|---|---|---|---|---|
| CLM-1 | README describes accumulated insights and unchanged model parameters. | RTE-1, RTE-2, RTE-3, RTE-4 retain and supply text; CMP-1 dispatches without local training. | Notebook shows revised sheets and later algorithm use; selected JSONL rows carry one sheet into the next prompt. | No intervention isolates the effect; remote weights uninspected. Text-memory mechanism is supported. |
| CLM-2 | README reports substantial benchmark gains and curator prompt requests verified solutions. | RTE-6 allows computational feedback; RTE-7 scores answers after memory adoption. | Notebook later solves the same puzzle successfully and explicitly follows its retained algorithm; selected AIME rows retain target-disagreeing answers. | No controlled component contrast inspected. Successful reuse is supported; general gains and learning attributable to criticism remain unestablished here. |

#### 6. Bounded conclusion

The workflow produces, reshapes and reuses candidate solutions and strategies. Automatic curation and selection have operational force. Final-answer evaluators have narrower epistemic authority, and their scores do not decide memory retention. Tool feedback can support content-directed correction, but the current evidence does not establish the full route from criticism of a retained theory to a revised theory that improves later capacity. Retained examples document useful later solving and error retention together; neither fact warrants a system-wide epistemic grade.

## Reconciliation

Specialist report run, source identity, reviewed boundary, complete status, input digest and method digest were checked against the commissioned bytes. Final report SHA-256 is bound in Run identity. The parent's independent runtime/epistemic inspection and the specialist independently converged on the distinction between late answer grading and earlier memory admission; neither used earlier Commonplace analyses.

Proposal mappings: `MEM-RTE-1` → RTE-8 (caller initialization/adoption); `MEM-CLM-1` → CLM-3 (bounded retained examples); `MEM-ABS-1` → ABS-1 (merged into the bounded memory-admission absence). Every profile token was mapped exactly to a declared canonical ID; generic identities were not reassigned.

Issue dispositions: (1) caller text route registered with authored/manual affordances kept below wired human operation; (2) historical samples retained separately as SRC-2, including the current-code/empty-history formatting difference; (3) semantic admission absence integrated with ABS-1 while preserving possible internal model criticism; (4) original compound OBJ-5 marked superseded and split into OBJ-8 targets and OBJ-9 local scores, with no ID reused; (5) retrieval-synthesis, hybrid and full-history fallback/persistence differences retained on their respective routes; (6) checkpoint consistency and provider-state recovery limitations retained on RTE-1 and OBJ-7. (7) The specialist was asked to separate temporary execution recursion from accumulated memory. Its corrected report removes RTE-6 as a direct direction/signal witness and retains it only as upstream tool-trace production. The aggregate scope and notes now explicitly exclude temporary context. The input bytes did not change; the specialist revalidated the corrected report. No substantive conflict remains.

Profile values, evidence strengths, coverage and rationale were adopted from the specialist without an independent replacement memory analysis. The coordinator verified integration and added whole-runtime owner/effect/return fields. Shared-route ownership remains canonical: generic dispatch/evaluation on RTE-6 and RTE-7, memory semantics on RTE-1, RTE-2, RTE-3, RTE-4, RTE-5 and RTE-8. The epistemic overlay cites these records instead of creating duplicate generic routes. No mechanical citation edit to the specialist report was needed.

## Bounded synthesis

Dynamic Cheatsheet makes earlier model work available during subsequent inference, using cumulative rewritten guidance, similar prior examples, or both. The notebook provides a concrete successful reuse case: later invocations solve the same puzzle and explicitly apply the retained algorithm. That is stronger than an unused storage interface. Its limits are equally concrete: the workflow admits curator text by tags, stores it before benchmark grading, and has source-native examples of incorrect answers becoming reference material. Benchmark score cannot be read as a trust mark on the memory.

At this workflow boundary, **theory-builder conditions 1–4** remain separate. Condition 1, localized content: **observed** in named strategies and code in OBJ-1. Condition 2, consumption: **observed** in the notebook's explicit plan to implement the retained algorithm and corresponding program; its causal necessity is not established. Condition 3, content-directed criticism and resulting revision or changed reliance: **uninspected** at the model-judgment boundary; the invoked prompts request checking, and tool feedback is wired, but the inspected retained sequence does not formulate an error in the prior strategy and link that criticism to its replacement. Condition 4, iteration of the result of criticism: **uninspected** for that same missing relation, even though successor-sheet read-back is wired and recurrent consumption observed. All four are therefore not established together. Missing curator rationale alone would not establish absent criticism.

Addressability: strategy descriptions, examples, assumptions requested by the prompt and code snippets are inspectable units; whole-sheet replacement is the actual commit operation. Persistence: text passes across rounds and problems and can be restored across process runs through JSONL; persistence of a formulated criticism is unestablished. **Learning**: the strongest observed contribution is a successful later solution using retained guidance on one puzzle. Improved capacity attributable specifically to criticizing a consumed theory is **uninspected**; neither later success nor the README metrics resolve that attribution. No causal claim exceeds the inspected comparison.

**Reflection:** a pathway that feeds its own generated solutions and current strategy text to a curator and then back to the generator is **wired** for those represented aspects. Actual model dependence on the representation is evidenced locally by explicit later use, while a causal intervention was not inspected. **Reflective theory-builder qualifier:** **uninspected**, because criticism and revision of the builder's method texts as theories are not established. **Autonomous theory-builder qualifier:** **uninspected** as a membership claim; role allocation is wired computationally for proposal, selection, admission and reuse, but missing criticism evidence cannot be filled by that allocation. Humans configure and initiate the workflow, and the notebook's retries are human-authored cell choices.

**Self-improvement:** a standing improvement-directed memory-update pathway is **wired**, with more useful later problem solving as its prompt-stated objective. The notebook supplies **observed** recurrence and a later successful answer. Occurrent causal dependence of that success on evidence-responsive changes to the workflow's own organization remains **uninspected**. This is a positive architectural contribution with an unresolved causal link, not a claim that memory rewriting guarantees improvement. The local code path and remote provider path must be assessed separately for effect control.

For sequential problem solving, the design offers automatic access to reusable strategies without retraining. For trust-sensitive reuse, its decisive limitation is that semantic checking is delegated to the same model and memory admission does not consume the independent score. A retained curator critique tied to an identified rule, its revised successor, later content-dependent use, and a controlled comparison would change the theory-building and learning assessment. A gate that checked a candidate sheet before adoption would change its memory-warrant architecture. Provider evidence would be needed to strengthen hosted-state and isolation claims.

## Limitations

| Limitation | Affected IDs | Inspected boundary | Conclusion prevented | Evidence that would resolve it |
|---|---|---|---|---|
| Remote model resolution and execution opaque | CMP-1, OBJ-7, RTE-6 | Client requests only | Exact weights, fixity, hosted isolation and retained service payload | Provider-version and execution evidence |
| Embedding provenance unknown | CMP-2, OBJ-3, RTE-3 | CSV consumer and similarity selector | Producer identity and semantic quality of vector representation | Generation provenance and pinned model |
| Historical outputs lack current-code execution provenance | SRC-2, OBJ-4 | Selected notebook and JSONL | Observed operation of every current provider/variant | New pinned runtime trace |
| Retained criticism not established | RTE-2, RTE-3, RTE-4 | Prompts, updater and selected artifacts | Theory-builder conditions 3 and 4, reflective builder status, learning attribution | Candidate-linked criticism and successor use |
| No controlled memory intervention inspected | CLM-2, BAP-1 | Same-puzzle recurrence and README claims | Causal memory benefit, faithfulness and cross-task improvement | Matched ablation with retained outputs and design |
| Task evaluator and dataset warrant limited | OBJ-8, OBJ-9, RTE-7 | Encoded evaluator and supplied targets | Truth of all labels, explanations and retained strategies | Dataset audit and strategy-specific tests |
| Independent bundled client interfaces excluded | RTE-6 | Workflow-reached dispatch only | Complete characterization of standalone chat/web-search clients | Separately scoped interface analysis |
| Semantic curator success is not enforced | OBJ-1, RTE-2, RTE-3, RTE-4 | Supplied prompts and parser | Reliable counts, rationale preservation, semantic deduplication and complete context fit | Candidate-specific traces and tests of preservation/use |

## Verification and blockers

### Semantic verification

Integrated comparison scope and canonical records checked together: OBJ-1, OBJ-2 and OBJ-3 cover local sheets/history/access data; all six branch alternatives and RTE-8 input are accounted for, while OBJ-7's opaque service state is explicitly excluded. RTE-2, RTE-3 synthesis and RTE-4 are the qualifying trace-fed writes. Each receives trajectories and, when present in the returned text, local tool traces; each produces retained prose/code online. RTE-2 additionally reaches later same-task rounds; RTE-1 carries successors across distinct problems and restores checkpoints. RTE-3 pure retrieval and RTE-5 replay/default add no distilled-learning witness. No separate compaction route was found among these inspected transformations; curator consolidation already belongs to these routes.

Push was checked from the consuming model's perspective: no memory request precedes the automatic context insertion. Whole-sheet/history availability is coarse; current query embeddings select prior pairs; curator judgments select and rewrite retained parts for generator delivery. Exact matching only aligns the embedding table and is not a delivered-part identifier selector. Temporary RTE-6 recursion was removed as a direct memory witness after specialist correction. Requested API return is not counted as a second pull path. Prompt-wired curation operations remain distinct from guaranteed successful curation. Manual/authored values retain afforded evidence. Faithfulness stays not-determinable; no negative corpus-wide claim or observed causal benefit is inferred. Every mapped profile record resolves and each value's supporting status remains unchanged.

Source layers remain distinct. Every runtime route records owner, return, read-back, selection, visibility, persistence and recovery. Round limits and two execution locations were not merged into one guarantee. Answer-oracle availability is attached to benchmark scoring and not inferred for curation. Component parameter fixity is distinguished from forwarding a model name. The epistemic overlay cites canonical IDs, distinguishes transformation, checks, operational admission and retention, and does not translate `implemented` into a conclusion status. All learning and self-improvement claims lead with supported reuse and preserve causal limits. No legacy analysis supplied evidence.

### Deterministic validation

Validation target: this exact result at `kb/reports/state/agentic-system-analysis/AAS-2026-09-27-dynamic-cheatsheet-02/result.md`, with `commonplace-agentic-analysis-publication verify-sources` against the sibling running state. Source anchors, quotes, identifiers and handoff identity are checked before publication. Final status: passed. Structural and source verification completed with no unresolved failure; final exact bytes are rechecked before publication.

### Blockers

none
