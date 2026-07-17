---
description: "Dynamic Cheatsheet review: trace-learning test-time prompt memory with LLM cheatsheet curation, embedding retrieval, and automatic solver read-back"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# Dynamic Cheatsheet

Dynamic Cheatsheet, from Mirac Suzgun's `suzgunmirac/dynamic-cheatsheet` repository, is a Python framework for test-time learning with black-box language models. It runs benchmark examples sequentially, keeps an evolving cheatsheet of strategies, snippets, and examples, and injects that retained memory into later solver prompts without changing model weights.

**Repository:** https://github.com/suzgunmirac/dynamic-cheatsheet

**Reviewed commit:** [5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9](https://github.com/suzgunmirac/dynamic-cheatsheet/commit/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9)

**Source directory:** `related-systems/dynamic-cheatsheet`

## Core Ideas

**The memory is a prompt artifact, not a model update.** The README describes a persistent, evolving inference-time memory for strategies, code snippets, and problem-solving techniques, and the implementation threads a `cheatsheet` string through `LanguageModel.advanced_generate()` rather than training or modifying a model ([README.md](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md), [dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py)). The generator prompt receives that string through `[[CHEATSHEET]]` and tells the solver to inspect, apply, and qualify the provided reference material ([prompts/generator_prompt.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt)).

**The cumulative path distills solver traces into prose memory.** In `DynamicCheatsheet_Cumulative`, the solver first answers with the current cheatsheet, then a curator prompt receives the current question, solver output, and previous cheatsheet; only text inside `<cheatsheet>...</cheatsheet>` becomes the new retained memory, otherwise the old cheatsheet survives ([dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [dynamic_cheatsheet/utils/extractor.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/extractor.py)). The cumulative curator asks for concise reusable entries, examples, usage counts, redundancy removal, and preservation of useful old content ([prompts/curator_prompt_for_dc_cumulative.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt)).

**Retrieval variants separate local precedent from broad strategy.** `Dynamic_Retrieval` and `DynamicCheatsheet_RetrievalSynthesis` compare the current input embedding against previous input embeddings with cosine similarity, select top-k prior examples, and pass previous inputs plus previous model outputs into the solver or a synthesis curator ([dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py)). `DynamicCheatsheet_CumulativeRetrieval` combines both: the solver receives the cumulative cheatsheet plus retrieved similar examples, while the post-answer curator updates only the cumulative cheatsheet.

**Context efficiency is prompt-governed rather than enforced.** The system avoids full-history replay in its main variants by either compressing traces into a 2000-2500 word cheatsheet requested by the curator prompt or selecting `retrieve_top_k` similar examples ([prompts/curator_prompt_for_dc_cumulative.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt), [run_benchmark.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py)). There is no hard token clipping for cheatsheet size, no schema validator for individual memory items, and no source-level provenance attached to a retained entry; `FullHistoryAppending` remains as the explicit uncompressed baseline.

**Execution feedback can enrich the trace without becoming a separate memory type.** The generator prompt asks for Python code followed by `EXECUTE CODE!`, and `generate()` can execute local code blocks recursively or use provider code-interpreter support before extracting the final answer ([prompts/generator_prompt.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/generator_prompt.txt), [dynamic_cheatsheet/language_model.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [dynamic_cheatsheet/utils/execute_code.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/execute_code.py)). The curator sees the textual solver output, so code results can influence the cheatsheet indirectly, but the implementation does not retain code-execution metadata as a typed artifact.

## Artifact analysis

- **Storage substrate:** `in-memory` — The active behavior-shaping memory is the Python `cheatsheet` string and per-run `generator_outputs_so_far` list; benchmark JSONL files, initialized cheatsheet files, result directories, and embedding CSVs provide durable snapshots and inputs, but runtime prompt assembly reads the in-process values.
- **Representational form:** `prose` `symbolic` `parametric` — Cheatsheets, prior solutions, and prompt templates are prose; XML-like wrappers, JSONL fields, approach names, top-k ordering, CLI arguments, and extraction rules are symbolic; precomputed input embeddings and cosine similarities provide parametric retrieval state.
- **Lineage:** `authored` `imported` `trace-extracted` — Prompt templates and runner code are authored, benchmark datasets and embedding CSVs are imported, and the retained cheatsheet plus previous-solution packets are derived from sequential solver traces.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — Cheatsheet entries and previous solutions advise the solver as knowledge artifacts; generator and curator prompts instruct how memory is used and updated; embedding similarity ranks prior examples; curator calls turn traces into later prompt memory.

**Cumulative cheatsheet.** The central artifact is a replacement prose cheatsheet carried from one `advanced_generate()` call to the next, saved in result rows as `final_cheatsheet`, and optionally seeded or resumed from files through `--initialize_cheatsheet_path` and `--continue_from_last_run_path` ([run_benchmark.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py)). Its lineage is trace-extracted: current input, solver output, and prior cheatsheet are transformed by a curator prompt into a new prompt artifact. Its authority is soft but direct, because the next solver prompt tells the model to analyze and apply the cheatsheet.

**Retrieved previous-solution packets.** Retrieval modes assemble prompt sections from earlier input-output traces selected by similarity over precomputed input embeddings. These packets are transient context rather than durable distilled memory, except that their source traces are also written into JSONL result rows. Their authority is knowledge and ranking: they are examples to inspect critically, while cosine similarity decides which traces become visible.

**Curator prompt templates.** `curator_prompt_for_dc_cumulative.txt` and `curator_prompt_for_dc_retrieval_synthesis.txt` are authored system-definition artifacts. They define what counts as useful memory, how much prior material must be preserved, how duplicates should be removed, how usage counts should appear, and which `<cheatsheet>` wrapper is required for extraction ([prompts/curator_prompt_for_dc_cumulative.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt), [prompts/curator_prompt_for_dc_retrieval_synthesis.txt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_retrieval_synthesis.txt)).

**Benchmark traces and evaluators.** Each example writes prompt state, solver output, final answer, current/new cheatsheet, target, and raw input into JSONL output, with task-specific evaluation functions checking final answers after the solver run ([run_benchmark.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py), [dynamic_cheatsheet/utils/evaluation.py](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/evaluation.py)). Evaluation affects reported benchmark performance, but the inspected code does not feed correctness as a hard acceptance gate into the curator before a memory item is reused.

The promotion path is trace -> curator prompt -> prose cheatsheet -> automatic prompt injection. Retrieval adds trace -> embedding-ranked example packet -> optional synthesis -> prompt injection. The path increases behavioral authority quickly, but it does not add item-level provenance, human review, contradiction handling, or symbolic validation before reuse.

## Comparison with Our System

| Dimension | Dynamic Cheatsheet | Commonplace |
|---|---|---|
| Primary purpose | Test-time benchmark learning for black-box LMs | Agent-operated methodology KB with durable typed artifacts |
| Main retained unit | Cheatsheet text and prior solver traces | Typed notes, reviews, instructions, sources, ADRs, reports, and generated indexes |
| Write behavior | Automatic LLM curation after each example | Authored or revised artifacts under collection/type contracts and review gates |
| Read-back | Automatic prompt injection, optionally embedding-targeted | Mostly deliberate search, indexes, links, skills, and workflow context |
| Governance | Wrapper extraction, result logging, task evaluation | Frontmatter schemas, validation, source snapshots, reviews, links, and git history |

Dynamic Cheatsheet is close to the minimum viable test-time memory loop: remember a compact prose artifact, update it from the last attempt, and put it in the next prompt. Commonplace makes the opposite tradeoff. It keeps memory as a governed library of typed artifacts whose claims can be cited, validated, reviewed, replaced, and connected before they acquire stronger authority.

The useful alignment is the raw-to-distilled split. Dynamic Cheatsheet keeps solver traces and result rows, then asks a curator to produce a smaller behavior-shaping artifact. Commonplace has the same broad shape when sources, workshop drafts, or review reports produce durable notes and instructions. The difference is trust: Dynamic Cheatsheet lets an LLM curator immediately rewrite operational memory, while Commonplace usually separates evidence, draft, and current library artifact.

The major divergence is provenance. The curator prompt asks for tested and proven strategies, but the code does not pass evaluation outcome into the curator as a strict oracle, does not preserve source pointers per memory item, and does not provide invalidation metadata. That is acceptable for a benchmark experiment where fast adaptation matters; it is too weak for durable Commonplace artifacts.

### Borrowable Ideas

**Use task-local cheatsheets as workshop artifacts.** Commonplace could keep an explicit temporary cheatsheet during repeated review, migration, or source-triage loops. Ready for workshop-scoped work; not ready as an automatic path into library notes.

**Separate cumulative lessons from similar precedents.** The hybrid variant is a useful structure: broad strategy memory stays compact, while similar past cases are selected per instance. Commonplace could apply this to review bundles by combining a stable rubric with a few comparable prior reviews. Needs retrieval that preserves source and review status.

**Fallback to the incumbent artifact when generation fails format checks.** `extract_cheatsheet()` keeps the old cheatsheet if the curator omits the wrapper. Commonplace can borrow that failure mode for generated workshop drafts or derived summaries. Ready now.

**Keep automatic promotion away from durable authority.** Dynamic Cheatsheet's trace-to-instruction loop is effective for experiments, but Commonplace should keep generated observations as suggestions until validation or review accepts them.

**Retain appendable run records for memory experiments.** The JSONL output records prompts, outputs, cheatsheet states, targets, answers, and correctness flow. Commonplace review and revision experiments could use similarly lightweight run logs before deciding what deserves a durable artifact.

## Write side

**Write agency:** `automatic` `manual` — The main memory loop is automatic: solver traces are passed to curator prompts and the returned `<cheatsheet>` replaces the old cheatsheet for the next call. Manual agency exists only at the edges, where a user chooses prompts, selects an approach, seeds an initial cheatsheet file, resumes a prior run, or edits prompt/templates outside the runtime loop.

**Curation operations:** `consolidate` `dedup` `evolve` `promote` — The curator is instructed to compress old and new material into a compact cheatsheet, remove redundancy, refine existing entries, and use usage counts to prioritize frequently useful strategies. These operations are prompt-mediated rather than independently validated by code.

### Trace-learning

**Trace source:** `session-logs` `trajectories` — Sequential benchmark runs produce ordered examples with prompts, solver outputs, extracted answers, current/new cheatsheets, targets, correctness checks, and prior output lists.

**Extraction.** For cumulative memory, the oracle is an LLM curator prompted with the current input, solver output, and previous cheatsheet; wrapper extraction decides whether the proposed memory replaces the incumbent. For retrieval memory, deterministic embedding similarity selects prior input-output traces, and `DynamicCheatsheet_RetrievalSynthesis` can ask a curator to synthesize those selected traces into a temporary cheatsheet.

**Learning scope:** `per-task` `cross-task` — Runs are normally organized by benchmark task, but an initialized cheatsheet can be carried into another run manually.

**Learning timing:** `online` — Each processed example can update memory for the next example in the same sequential run.

**Distilled form:** `prose` — The durable learned artifact is cheatsheet prose; embeddings rank traces for retrieval but are not the final distilled memory.

Dynamic Cheatsheet is a clear trace-learning system because retained behavior-shaping prose is generated from prior solver trajectories. It demonstrates a low-infrastructure path to test-time learning, while also showing the trust problem: trace-derived authority can outrun provenance and validation.

## Read-back

**Read-back:** `push` — From the solver model's perspective, retained memory is injected by `advanced_generate()` into the generator prompt; the solver does not call a memory tool or decide whether to retrieve.

**Read-back signal:** `coarse` `inferred / embedding` — Cumulative mode pushes the whole current cheatsheet on each example, while retrieval modes use input-embedding similarity to push top-k prior examples or a synthesized cheatsheet for the current instance.

**Faithfulness tested:** `no` — The repository reports benchmark outcomes and writes traces, but it does not implement per-memory with/without ablations, perturbation tests, or post-answer audits proving that a fired memory item changed solver behavior faithfully.

Cumulative read-back is coarse: whatever cheatsheet is current is inserted into `[[CHEATSHEET]]` before the next answer. Retrieval read-back is instance-targeted by inferred embedding similarity: the current input embedding is compared with previous input embeddings, top-k examples are assembled into a prompt section, and the solver is warned to verify rather than blindly copy them. In the hybrid variant, both the cumulative cheatsheet and the retrieved section enter the same pre-invocation solver prompt.

Selection is controlled by `retrieve_top_k` for retrieval paths and by the curator prompt's requested 2000-2500 word cheatsheet length for cumulative memory. Actual token pressure is not enforced by `count_tokens()` or a clipping policy in the reviewed path, and effective precision, recall, or context dilution cannot be verified from code alone.

At consumption time, the cheatsheet has instruction-like force because the generator prompt tells the solver to analyze it and apply applicable patterns. Retrieved previous solutions have weaker advisory authority: they are explicitly framed as potentially useful but fallible examples.

## Curiosity Pass

**The core memory is simpler than the name suggests.** Most of the system is a string, prompt templates, a wrapper extractor, and a loop. The interesting part is not storage sophistication; it is the decision to let the prompt artifact evolve online.

**The curator is the trust boundary.** It decides what to preserve, what to discard, how to generalize a trace, and whether previous content survives. Evaluation happens after solving, but the curator is not wired to a hard correctness signal before promotion.

**Retrieval is better governed than cumulative memory, but only on selection.** Embedding top-k at least controls which past traces are visible for a given input. Once visible, those traces are still unverified model outputs.

**The code-execution loop creates richer evidence than the curator explicitly models.** Solver outputs may include executed Python and follow-up reasoning, but the retained memory does not separate code, execution result, failure, and final answer as distinct provenance-bearing units.

**`FullHistoryAppending` is a useful baseline because it names the failure mode.** Dynamic Cheatsheet's main contribution is avoiding full trace replay by compression or retrieval; it is not merely that previous text is stored.

## What to Watch

- Whether correctness results become curator inputs or acceptance gates. That would materially improve trace-derived memory quality.
- Whether cheatsheet entries gain item-level provenance, confidence, or invalidation metadata. That is the missing bridge from benchmark memory to reviewable knowledge artifacts.
- Whether embedding generation becomes part of the repository workflow rather than precomputed CSV input. That would clarify retrieval lineage.
- Whether prompt-level length requests become hard token budgets. That determines whether cumulative memory stays compact as runs grow.
- Whether retrieval-synthesis preserves links back to selected examples after synthesis. Without those links, the synthesized cheatsheet is harder to audit than the raw top-k packet.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places: Dynamic Cheatsheet turns sequential solver traces into prose prompt memory and embedding-selected prior-example packets.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Dynamic Cheatsheet stores traces and cheatsheets, then wires them into prompt read-back automatically.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: cheatsheets, prompt templates, embeddings, result traces, and evaluators differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: previous solutions and saved result traces are examples, evidence, and audit material.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generator and curator prompts define how retained memory changes and how it influences later solver behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: raw solver trajectories are distilled into a durable behavior-shaping cheatsheet.
