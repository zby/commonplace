---
description: "Test-time learning benchmark that carries a curator-rewritten cheatsheet across ordered problem attempts and can retrieve prior examples by embedding similarity"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Dynamic Cheatsheet

Dynamic Cheatsheet is Mirac Suzgun's research implementation of test-time learning with adaptive memory. It wraps a black-box language model with prompt-level retained state: an evolving cheatsheet string, optional retrieval over previous examples, optional Python/code-interpreter execution during solving, and benchmark JSONL logs that preserve ordered attempts across math, puzzle, and multiple-choice datasets.

**Repository:** https://github.com/suzgunmirac/dynamic-cheatsheet

**Reviewed commit:** [5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9](https://github.com/suzgunmirac/dynamic-cheatsheet/commit/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9)

## Core Ideas

**The durable memory is prompt text, not a database.** The README frames Dynamic Cheatsheet as persistent, evolving memory, and the implemented carrier is the `cheatsheet` string passed into `LanguageModel.advanced_generate(...)` and then into the generator prompt's `[[CHEATSHEET]]` slot ([README.md](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md), [dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [prompts/generator_prompt.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt)). Within one run, the value is held in process memory and written into every result row as `current_cheatsheet`, `new_cheatsheet`, or `final_cheatsheet`; resuming a run reloads the last row's `final_cheatsheet` ([run_benchmark.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py)).

**Cumulative mode is a two-call trace-to-cheatsheet loop.** `DynamicCheatsheet_Cumulative` first asks the generator to solve the current input using the current cheatsheet. It then asks a curator model to rewrite the cheatsheet from `[[QUESTION]]`, `[[MODEL_ANSWER]]`, and `[[PREVIOUS_CHEATSHEET]]`, extracting only a `<cheatsheet>...</cheatsheet>` block and otherwise keeping the old version ([dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [dynamic_cheatsheet/utils/extractor.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/extractor.py), [prompts/curator_prompt_for_dc_cumulative.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt)). The curator prompt asks for usage counters, preserved old content, reusable snippets, assumptions, and general strategies; the code does not pass the benchmark target or correctness result into that curator call.

**Retrieval variants retain examples separately from the cheatsheet.** `Dynamic_Retrieval` and `DynamicCheatsheet_RetrievalSynthesis` load precomputed CSV embeddings from `embeddings/{task}.csv`, align them to the shuffled dataset order, compute cosine similarity against previous input embeddings, and pass the top-k previous input/output pairs to the generator or to a synthesis prompt ([run_benchmark.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py), [dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [embeddings/](https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/embeddings)). `DynamicCheatsheet_RetrievalSynthesis` turns retrieved examples into a per-query cheatsheet using a separate curator prompt, while `DynamicCheatsheet_CumulativeRetrieval` injects both the cumulative cheatsheet and a retrieved-example section before updating the cumulative cheatsheet ([prompts/curator_prompt_for_dc_retrieval_synthesis.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_retrieval_synthesis.txt)).

**Code execution is part of the attempt trace.** The generator prompt instructs models to emit Python code blocks followed by `EXECUTE CODE!`. `LanguageModel.generate(...)` detects that flag, runs local Python through `extract_and_run_python_code(...)`, appends the captured output to the conversation, and asks the model to continue; an optional provider code-interpreter path creates a persistent OpenAI container or uses Claude native code execution ([prompts/generator_prompt.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt), [dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [dynamic_cheatsheet/utils/execute_code.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/execute_code.py)). Those execution outputs are stored inside `generator_output` and `final_output`, not as separate typed artifacts.

**Benchmark artifacts preserve raw attempts and derived state together.** `run_benchmark.py` writes JSONL after every example for crash recovery, with `input`, `target`, `raw_input`, `steps`, `final_answer`, `final_output`, and `final_cheatsheet`; it also writes a sibling params JSON for newly run experiments ([run_benchmark.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py)). The repository includes checked-in `results/` JSONL files for multiple tasks and model/approach combinations, local Hugging Face dataset caches under `data/`, precomputed embedding CSVs under `embeddings/`, and notebooks/figures for example usage and evaluation ([results/](https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/results), [data/](https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/data), [ExampleUsage.ipynb](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/ExampleUsage.ipynb), [EvaluatingResults.ipynb](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/EvaluatingResults.ipynb)).

## Comparison with Our System

| Dimension | Dynamic Cheatsheet | Commonplace |
|---|---|---|
| Primary loop | Ordered benchmark attempts update a carried prompt artifact | Agents and maintainers revise typed KB artifacts over git |
| Raw trace substrate | JSONL rows with prompts, generated answers, code outputs, targets, and old/new cheatsheets | Markdown notes, review reports, generated indexes, command outputs, git history |
| Distilled artifact | Prose cheatsheet string; sometimes retrieval-synthesized prompt context | Notes, instructions, ADRs, skills, validators, indexes |
| Activation | Inject cheatsheet or retrieved examples into the next generator prompt | Search/load artifacts and follow instructions/skills before acting |
| Oracle | Mostly model self-curation; benchmark targets score runs after generation | Human review, schemas, validators, review gates, source citations |
| Lifecycle | Carry forward, initialize from file, resume from JSONL; no status, supersession, retirement, or provenance graph | Frontmatter status, links, indexes, validation, archival/replacement workflows |

Dynamic Cheatsheet is useful precisely because it is minimal: no vector database service, no fine-tuning step, no custom agent runtime. Its retained artifact can be inspected as a knowledge artifact when a human or later agent reads the results JSONL, but it becomes a system-definition artifact when the generator prompt injects it as advice/policy for the next answer. That authority shift is the system's main memory move.

The implementation also shows why commonplace separates artifact contracts. Dynamic Cheatsheet stores raw ordered attempts, generated answer traces, code-execution output, old cheatsheet text, new cheatsheet text, retrieval examples, benchmark targets, and result files in one JSONL row family. That is economical for an experiment, but it blurs lineage: a wrong answer can still be summarized into the cheatsheet because the curator does not receive the evaluation result, and a later row's `final_cheatsheet` does not record which entries came from which successful or failed attempts except whatever references the curator chose to preserve.

Compared with commonplace, Dynamic Cheatsheet is better at zero-friction online adaptation inside a benchmark. Commonplace is better when the retained state must be governed, cited, reviewed, retired, or promoted into stronger artifacts. Dynamic Cheatsheet's representational form is almost entirely prose, with symbolic JSON wrappers and embedding-based retrieval. Commonplace's comparable promotion path would not stop at a growing prompt note; it would split reusable lessons into reviewed notes, instructions, tests, or skills when evidence justifies stronger behavioral authority.

## Borrowable Ideas

**Treat a carried prompt as a compiled view with weak authority.** Ready as vocabulary. A commonplace run could carry a temporary cheatsheet for a workshop or review batch, but it should be labeled as a derived view, not a canonical source.

**Keep old and new retained text in the trace row.** Ready for review tooling. Dynamic Cheatsheet's `current_cheatsheet` and `new_cheatsheet` fields make each update diffable after the fact. A commonplace analogue would preserve before/after generated context packs or review summaries beside the source action that produced them.

**Use retrieval examples as evidence, not as memory itself.** Ready as a caution. The retrieved `top_k_original_inputs` and outputs are useful local evidence, but they should not silently gain instruction authority. Commonplace should keep retrieved examples marked as examples until a reviewed artifact promotes a generalized lesson.

**Separate curator prompts by update mode.** Borrowable if commonplace adds temporary compiled memories. The cumulative and retrieval-synthesis prompts have different jobs: one preserves and rewrites a standing artifact, the other synthesizes query-local context from similar examples.

**Do not let benchmark success imply governance.** Ready now as a review principle. The repository can show accuracy improvements while still lacking validation of individual cheatsheet entries, source-level lineage, or retirement rules. Those are different claims.

## Trace-derived learning placement

**Trace source.** Dynamic Cheatsheet consumes ordered problem attempts during benchmark or notebook execution. A raw attempt includes the current input, prompt-expanded cheatsheet, generator output, optional Python/code-interpreter output, extracted final answer, target, prior generated outputs, old cheatsheet, and new/final cheatsheet. Retrieval modes also consume the ordered corpus of previous inputs and outputs plus precomputed input embeddings.

**Extraction.** Extraction differs by variant. In cumulative mode, an LLM curator rewrites the old cheatsheet from the current question and model answer. In retrieval mode, cosine similarity selects prior input/output pairs. In retrieval-synthesis mode, a curator rewrites selected examples into a query-local cheatsheet. In cumulative-retrieval mode, retrieved examples are injected beside the cumulative cheatsheet, then a curator updates the cumulative artifact. The benchmark evaluator checks final answers after generation, but that correctness signal is not fed into the cumulative curator call in the inspected implementation.

**Storage substrate.** Raw and distilled state live primarily in JSONL files under `results/{task}/...jsonl` when using the benchmark runner. Dataset caches live under `data/`; embeddings live as CSV files under `embeddings/`; prompt templates live under `prompts/`; figures and notebooks summarize experiments. During a live run, the active cheatsheet is an in-memory string, optionally initialized from a file and carried forward from one output row to the next.

**Representational form.** Raw attempts are mixed artifacts: symbolic JSON fields containing prose prompts, prose answers, code blocks, execution output, targets, and extracted answer strings. The cheatsheet's operative part is prose, usually structured with XML-like `<memory_item>` blocks and usage counts. Retrieval examples are prose traces selected by symbolic numeric similarity. Embedding CSVs are distributed-vector representations used for ranking, but they are precomputed retrieval support rather than the learned retained behavior.

**Lineage.** The lineage chain is benchmark dataset row -> generated solution trace -> optional code-execution transcript -> curator rewrite or retrieval selection -> next prompt injection -> result JSONL row. The row preserves enough material to inspect many updates locally, but the cheatsheet entries are not separately addressable, do not carry stable source IDs, do not record an evaluation-backed acceptance decision, and are overwritten unless the previous content is copied into the new cheatsheet.

**Behavioral authority.** Raw result rows, prior answers, benchmark targets, and generated code outputs are knowledge artifacts when inspected as evidence. Retrieved examples are knowledge artifacts when shown as analogous cases. The cheatsheet becomes a system-definition artifact at the generator interface because the prompt tells the solver to analyze and use it when producing the next answer. The curator prompt is also a system-definition artifact: it defines what retained material should be preserved, discarded, counted, and rewritten.

**Scope and timing.** Scope is per benchmark run, per task, or per initialized cheatsheet file. Timing is online/staged during inference: solve one problem, update or select memory, solve the next problem. The checked-in result logs provide offline evidence about those runs, but the memory mechanism itself is prompt-time adaptation rather than parameter learning.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Dynamic Cheatsheet is a trace-to-prose-system-definition system with optional retrieval over previous attempts. It strengthens the survey claim that a trace-derived system can have multiple retained artifacts with different authority: raw attempts and retrieved examples are evidence, the curator prompt is update policy, and the cheatsheet is behavior-shaping advice once injected. It also adds a caution: self-curated trace distillation can improve benchmark performance without preserving enough correctness lineage to make each retained item trustworthy.

## Curiosity Pass

**The "verified" language is stronger than the implementation.** The curator prompt asks for tested and proven strategies, but `run_benchmark.py` evaluates correctness after the curator has already rewritten the cumulative cheatsheet. That means the system can carry forward an appealing but wrong technique unless the model self-diagnoses it in the answer text.

**The result row is doing several jobs at once.** It is a raw trace log, a crash-recovery checkpoint, an evaluation artifact, a source of examples for retrieval, and the persistence layer for the latest cheatsheet. That compactness is good for a research release, but it makes artifact authority hard to review.

**Retrieval-synthesis and cumulative memory solve different problems.** Retrieval-synthesis constructs a context pack from similar previous cases; cumulative mode tries to compress experience into reusable policy. Treating both as "cheatsheet" hides the difference between local analogy and cross-case distillation.

**Code execution is an implicit teacher.** Python output can correct or complete a model's solution before the curator sees the final answer. The execution transcript is not a separate lesson artifact, but it is part of the trace that can influence what the curator keeps.

**Usage counters are model-maintained, not event-derived.** The prompt requests counts, but the code does not compute them from successful reuse events. They are prose state maintained by the curator model.

## What to Watch

- Whether future versions feed evaluator results or verifier judgements into curator updates before a lesson can enter the cumulative cheatsheet.
- Whether cheatsheet entries gain source links back to result rows, question IDs, correctness outcomes, and supersession history.
- Whether retrieval support shifts from precomputed benchmark CSVs to live embedding of new tasks and generated outputs.
- Whether code-execution transcripts become first-class artifacts rather than being embedded inside `final_output` strings.
- Whether users apply Dynamic Cheatsheet outside ordered benchmarks, where dataset order, task homogeneity, and repeated examples are less controlled.

---

Relevant Notes:

- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: result rows, retrieved examples, targets, and code outputs when inspected as evidence
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: cheatsheet and curator prompts when injected as behavior-shaping policy
- [behavioral authority](../../notes/definitions/behavioral-authority.md) - sharpens: the same cheatsheet text changes authority depending on whether it is read or injected
- [representational form](../../notes/definitions/representational-form.md) - sharpens: Dynamic Cheatsheet mixes prose cheatsheets, symbolic JSON rows, and vector retrieval support
- [lineage](../../notes/definitions/lineage.md) - cautions: generated memory entries need source and acceptance lineage before gaining stronger authority
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Dynamic Cheatsheet is online trace-to-prose prompt memory with optional retrieval over previous attempts
