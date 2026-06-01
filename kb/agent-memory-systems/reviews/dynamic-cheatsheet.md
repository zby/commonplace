---
description: "Dynamic Cheatsheet review: test-time cheatsheet memory from solver traces, LLM curation, embedding retrieval, and automatic prompt read-back"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# Dynamic Cheatsheet

Dynamic Cheatsheet, from Mirac Suzgun's `dynamic-cheatsheet` repository, is a lightweight Python framework for test-time learning with black-box language models. It runs benchmark questions sequentially, keeps a reusable cheatsheet of strategies or examples across calls, and feeds that retained memory back into later prompts without modifying model weights.

**Repository:** https://github.com/suzgunmirac/dynamic-cheatsheet

**Reviewed commit:** [5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9](https://github.com/suzgunmirac/dynamic-cheatsheet/commit/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9)

**Last checked:** 2026-06-01

## Core Ideas

**Memory is an explicit prompt artifact, not a hidden model state.** The README presents Dynamic Cheatsheet as persistent inference-time memory for strategies, code snippets, and problem-solving techniques, and the public API shows the caller passing `final_cheatsheet` from one `advanced_generate` call into the next (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md). In code, the central retained artifact is just the `cheatsheet` string threaded through `LanguageModel.advanced_generate` and interpolated into `[[CHEATSHEET]]` in the generator prompt (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt).

**The cumulative path is trace-to-prose distillation.** `DynamicCheatsheet_Cumulative` first solves the current problem using the existing cheatsheet, then sends the current input, model answer, and previous cheatsheet to a curator prompt; only text inside `<cheatsheet>...</cheatsheet>` is retained, otherwise the old cheatsheet is kept (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/extractor.py). The curator prompt asks the model to preserve useful prior content, add generalizable strategies, remove redundancy, and keep usage counts (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt).

**Retrieval variants use similarity over prior inputs, then expose prior outputs as context.** `Dynamic_Retrieval` and `DynamicCheatsheet_RetrievalSynthesis` compare the current input embedding to embeddings of previous inputs with `cosine_similarity`, choose `retrieve_top_k` prior examples, and build a "previous solutions" section from prior inputs and prior generator outputs (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py). The benchmark runner loads precomputed task embeddings from CSV files under `embeddings/` and reorders them to match the shuffled dataset (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py, https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/embeddings).

**The hybrid path combines broad and local memory.** `DynamicCheatsheet_CumulativeRetrieval` sends the current cumulative cheatsheet plus a retrieved section of similar prior examples to the generator, then updates only the cumulative cheatsheet with the curator prompt after the answer (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py). This separates durable general strategy memory from per-query local precedent memory.

**Context efficiency is prompt-budgeted but not strongly governed.** The system avoids full-history replay in its main Dynamic Cheatsheet variants by asking the curator to compress lessons into a 2000-2500 word cheatsheet and, in retrieval modes, selecting only top-k examples (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py). There is no hard token budget, schema validation, semantic validation, provenance pruning, or deduplication outside the curator prompt. `FullHistoryAppending` is included as a baseline that explicitly appends all previous input-output pairs (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py).

**Execution feedback can enter the trace.** The generator prompt tells models to emit Python code followed by `EXECUTE CODE!`, and `generate` can recursively execute local Python snippets or use provider code-interpreter support before extracting the final answer (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/execute_code.py). That makes the raw answer trace richer than plain chat text, though the cheatsheet curator still receives only textual model output.

## Artifact analysis

**Cumulative cheatsheet.** The storage substrate is an in-memory string during `advanced_generate`, with durable snapshots in benchmark result JSONL records as `final_cheatsheet` and optional seed/resume paths through `--initialize_cheatsheet_path` and `--continue_from_last_run_path` (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py, https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/results). The representational form is prose with light XML-like tags, section headings, examples, and usage-count conventions. Lineage is trace-derived: current question, generator output, previous cheatsheet, and sometimes prior answers are transformed by an LLM curator into a replacement cheatsheet. Behavioral authority is system-definition artifact authority at read-back because the generator prompt instructs the solver to analyze and apply the cheatsheet; it is also a knowledge artifact because its entries act as evidence, examples, and advice rather than enforced rules.

**Retrieved previous-solution packet.** The storage substrate is the current Python process plus saved result JSONL files containing prior `final_output` values, with precomputed embedding CSVs under `embeddings/` for task inputs (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py, https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/embeddings). The representational form is mixed: distributed-vector similarity for selection, symbolic top-k ordering and similarity scores, then prose previous-input and previous-output blocks in the prompt. Lineage is assembled from benchmark dataset inputs, static embeddings, and prior solver traces. Behavioral authority is advisory knowledge-artifact context for the solver, with ranking influence from the similarity calculation.

**Curator prompt templates.** The storage substrate is authored prompt files in `prompts/` (https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts). The representational form is prose instruction plus placeholder symbols such as `[[PREVIOUS_CHEATSHEET]]`, `[[MODEL_ANSWER]]`, `[[PREVIOUS_INPUT_OUTPUT_PAIRS]]`, and `[[NEXT_INPUT]]`. Lineage is authored repository state. Behavioral authority is system-definition artifact authority: these prompts define what is eligible for promotion, how compression should happen, and the output wrapper required for extraction.

**Generator prompt template and answer trace.** The storage substrate is the authored generator prompt plus per-example result JSONL entries containing `generator_prompt`, `generator_output`, `generator_answer`, `current_cheatsheet`, `new_cheatsheet`, and final fields (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py). The representational form is prose prompt plus symbolic JSON result structure. Lineage is per-question execution trace. Behavioral authority is split: the prompt has instruction authority over the solver, while saved traces are knowledge artifacts for resumption, evaluation, retrieval, and later curation.

**Benchmark datasets, outputs, and evaluators.** The storage substrate is local Hugging Face datasets under `data/`, result JSONL under `results/`, and evaluation functions in `dynamic_cheatsheet/utils/evaluation.py` (https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/data, https://github.com/suzgunmirac/dynamic-cheatsheet/tree/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/results, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/evaluation.py). The representational form is mixed Arrow datasets, JSONL traces, and symbolic Python checks. Lineage is benchmark-run state; outputs are written after each example for crash recovery. Behavioral authority is evaluation authority for reported benchmark correctness, not a runtime gate on whether a cheatsheet entry is true before it is reused.

**Promotion path.** Dynamic Cheatsheet's promotion path is answer trace -> curator prompt -> prose cheatsheet -> automatic prompt read-back. Retrieval modes add answer trace -> top-k previous-solution packet -> optional curator synthesis -> prompt read-back. The path crosses lineage and authority, but it does not add a human review layer, validator, provenance-preserving citation model, or symbolic rule compiler.

## Comparison with Our System

| Dimension | Dynamic Cheatsheet | Commonplace |
|---|---|---|
| Primary purpose | Test-time benchmark learning for black-box LMs | Agent-operated methodology KB with durable typed artifacts |
| Main substrate | Python strings, prompt templates, result JSONL, embedding CSVs | Markdown collections, type specs, validation scripts, generated indexes, source snapshots |
| Retained unit | Cheatsheet text and previous input-output traces | Typed notes, reviews, instructions, sources, ADRs, reports |
| Learning path | LLM curator rewrites a prompt artifact from solver traces | Agents author or revise artifacts under collection/type contracts and review gates |
| Activation | Automatic prompt injection; top-k embedding-gated retrieval in retrieval modes | Mostly deliberate pull through search, indexes, skills, links, and review workflows |
| Governance | Minimal: prompt format extraction, benchmark evaluation, crash-resume records | Frontmatter schemas, validation, link contracts, review gates, git lifecycle |

Dynamic Cheatsheet is close to the smallest useful version of agent memory: retain a behavior-shaping prose artifact, update it after each attempt, and reinsert it into the next prompt. Commonplace is almost the opposite end of the same design space. It treats durable knowledge as a reviewed library with collection routing, type contracts, citations, validation, status, and links. Dynamic Cheatsheet treats memory as a mutable prompt support object optimized for immediate benchmark improvement.

The strongest alignment is the explicit separation between raw trace and distilled artifact. Dynamic Cheatsheet keeps prior generator outputs and result records, then asks a curator to compress them into a new cheatsheet. Commonplace uses workshop/review/source artifacts as evidence and promotes only selected material into durable notes or instructions. The difference is authority: Dynamic Cheatsheet lets the curator's prose immediately shape future solver behavior, while Commonplace normally requires more inspectable type and review boundaries before stronger system-definition authority is granted.

The main divergence is trust. The curator prompt asks the model to include "tested and proven" strategies, but the implementation does not pass correctness results into the curator as a hard oracle, does not attach source-level provenance to each cheatsheet item, and does not validate retained claims before reuse. The result can learn useful tactics quickly, but it can also preserve wrong or overfit strategies with high prompt authority.

Read-back: push, with unconditional cheatsheet injection in cumulative mode and engineered embedding-gated push in retrieval modes; no independent agent pull path is implemented.

### Borrowable Ideas

**Keep the retained memory as a first-class prompt artifact.** Commonplace could use explicit task-local cheatsheets for bounded workflows such as repeated benchmark review, source triage, or migration passes. Ready when the memory is intentionally temporary or workshop-scoped; too risky as a direct library-note mutation path.

**Separate cumulative strategy memory from retrieved precedent memory.** The hybrid approach is a useful shape: broad lessons stay in one compact artifact, while similar past cases are selected per query. Commonplace could use the same split for review runs: a stable review rubric plus top-k comparable prior reviews. Needs a retrieval surface that preserves source and review status.

**Expose failed compression as "keep old memory."** `extract_cheatsheet` falls back to the previous cheatsheet when the curator omits the wrapper. That is a small but useful failure mode for any generated artifact update. Ready now as a pattern for generated workshop artifacts.

**Do not borrow unreviewed automatic promotion into durable library artifacts.** Dynamic Cheatsheet's trace-to-instruction loop is effective for experiments, but Commonplace should keep a gate between trace-derived observations and permanent notes, instructions, or validators.

**Use result JSONL as an audit substrate for iterative memory experiments.** The benchmark runner records prompts, outputs, answers, cheatsheet states, targets, and correctness flow. Commonplace review bundles could borrow that lightweight, appendable run record for experimental workflows before deciding what belongs in the library.

## Trace-derived learning placement

**Trace source.** Dynamic Cheatsheet qualifies as trace-derived learning. The qualifying traces are sequential solver runs: current questions, generator prompts, generator outputs, extracted final answers, previous answers, current and new cheatsheets, and result JSONL rows written after each example (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py).

**Extraction.** Extraction is LLM-mediated for cheatsheets and deterministic for retrieval packets. The cumulative curator consumes the current input, model answer, and previous cheatsheet, then emits a replacement `<cheatsheet>` block; if parsing fails, the old cheatsheet remains. Retrieval modes use precomputed input embeddings and cosine similarity to select prior input-output traces, then either pass them directly to the solver or synthesize a task-local cheatsheet with a curator prompt (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_retrieval_synthesis.txt, https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py).

**Four fields.** Raw traces persist as result JSONL and in-process `generator_outputs_so_far`; distilled memory persists as `final_cheatsheet` strings and optional initialized/resumed cheatsheet files. The representational form moves from prose execution traces and JSON fields to prose cheatsheet entries; retrieval adds vector embeddings for selection but not as the final memory form. Lineage is per-benchmark and sequential, with result rows preserving enough state to resume the latest cheatsheet but not enough item-level provenance to invalidate a specific memory item cleanly. Behavioral authority moves from knowledge artifact evidence in raw traces to system-definition prompt authority when the cheatsheet is injected into the generator instructions.

**Scope and timing.** Scope is benchmark-run or manually supplied cheatsheet-file scope. Timing is online and sequential: the current example can update memory for the next example. Retrieval-synthesis is per-query and transient unless its synthesized packet is also stored in result rows.

**Survey placement.** Dynamic Cheatsheet belongs in the trace-to-prompt-artifact family. It strengthens the survey claim that test-time learning can be implemented without fine-tuning or a vector store as the durable memory: traces become an editable prose artifact that later changes prompt behavior. It also exposes the main risk in that family: authority rises faster than reviewability unless correctness, provenance, and invalidation are attached to the extracted memory items.

## Read-back placement

**Direction.** From the solver model's perspective, read-back is push. The runner and `advanced_generate` construct the prompt with whatever cheatsheet or retrieved examples the selected approach supplies; the solver does not call a memory tool or decide whether to retrieve (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py).

**Trigger and relevance signal.** Cumulative mode is unconditional carried-prompt push and would not by itself justify `push-activation`. Retrieval modes do justify it: on each query, the system compares the current input embedding against previous input embeddings, selects top-k by cosine similarity, and pushes only those examples or their synthesized summary into the prompt (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py).

**Timing relative to action.** Read-back happens before the solver answers. The selected cheatsheet or previous-solution packet is inside the generator prompt, so it can change the next answer rather than merely audit it afterward.

**Selection, scope, and complexity.** Selection is `retrieve_top_k` for retrieval examples and prompt-instructed compression for cumulative cheatsheets. Complexity is bounded only informally: the curator prompt asks for a 2000-2500 word cheatsheet, and the generator prompt receives the whole current cheatsheet plus any retrieved section in hybrid mode. There is no code-level token clipping for the cheatsheet content, despite `count_tokens` being available on the model wrapper (https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py).

**Authority at consumption.** The generator prompt makes the cheatsheet an advisory but behavior-shaping system-definition artifact: the model is told to analyze it, apply patterns, and document limitations. Retrieved previous solutions are lower-authority knowledge artifacts with an explicit warning not to blindly copy them.

**Faithfulness.** The benchmark results compare approaches and report correctness, but the code does not implement a per-memory WITH/WITHOUT ablation or faithfulness test proving that a fired cheatsheet item caused a specific answer improvement. Structural read-back is implemented; effective use is inferred from benchmark outcomes rather than verified at item level.

**Other consumers.** Humans can inspect result JSONL, notebooks, and generated cheatsheets. The implementation does not expose a separate governance consumer, reviewer queue, or memory approval workflow.

## Curiosity Pass

**The durable memory is ordinary prose, not a database.** The repository name sounds like a system, but most of the mechanism is a prompt string plus a loop that decides when to rewrite it.

**The curator is both compressor and trust boundary.** It decides what gets remembered, how much provenance survives, whether an answer was worth learning from, and which old material is preserved. The benchmark evaluator checks final answers, but the curator is not wired to a hard correctness oracle before promotion.

**The retrieval path is more engineered than the cumulative path.** Cumulative cheatsheet injection can dilute context as the artifact grows. Retrieval modes add an actual relevance signal, but the selected material is still previous model output and may contain mistakes.

**The code-execution loop can create high-value traces.** Python execution results may help solve tasks, and those outputs can be reflected in the generator answer that the curator sees. The system does not retain code-execution metadata as a separate typed artifact.

**The simplest baseline is intentionally revealing.** `FullHistoryAppending` shows what Dynamic Cheatsheet is trying to avoid: carrying all prior traces verbatim. The main contribution is the prompt-level distillation and retrieval boundary, not just persistence.

## What to Watch

- Whether future versions pass correctness results or evaluator feedback into the curator before cheatsheet promotion. That would make trace-derived memory less likely to preserve wrong strategies.
- Whether cheatsheet entries gain item-level provenance, confidence, or invalidation metadata. That is the main missing bridge from benchmark memory to a reviewable KB artifact.
- Whether embeddings are regenerated in-repo or remain precomputed CSV inputs. The current retrieval mechanism depends on external embedding lineage that is not represented by generation code in the repository.
- Whether token budgeting becomes a hard policy rather than a prompt instruction. That determines whether cumulative memory remains a compact context artifact as runs grow.
- Whether retrieval-synthesis keeps explicit links to selected examples after synthesis. Without that, the synthesized cheatsheet is harder to audit than the raw top-k packet.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Dynamic Cheatsheet turns sequential solver traces into prose prompt memory and top-k prior-example packets.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Dynamic Cheatsheet wires storage directly into prompt read-back for every later query in the selected approach.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: cheatsheets, prompt templates, embeddings, result traces, and evaluators differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: previous solutions and saved traces serve as examples, evidence, and audit material.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: prompt templates and injected cheatsheets instruct later solver behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: raw solver traces are distilled into a durable behavior-shaping cheatsheet.
