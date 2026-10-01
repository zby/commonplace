---
type: types/note.md
description: "Dynamic Cheatsheet's accumulated guidance, retrieval selection, format-only admission and separate benchmark scoring at a fixed revision."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-27-dynamic-cheatsheet-04
source-identity: https://github.com/suzgunmirac/dynamic-cheatsheet
reviewed-revision: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
analysis-result: kb/agentic-systems/reports/retained-archive/AAS-2026-09-27-dynamic-cheatsheet-04/result.md
analysis-result-sha256: 18a90d3619d9357c200ad80b41ade5b654875d9a7ca0b7b1c5203581a17ef5a4
---

# Dynamic Cheatsheet

Evidence basis: Python source, shipped prompts and two historical result rows at commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`, inspected on 2026-09-27. No fresh benchmark or provider call was run. Historical rows do not identify their producing revision.

Dynamic Cheatsheet maintains guidance between model calls. Its benchmark supplies each problem, invokes a generator and sometimes a curator, saves outputs, and carries the current cheatsheet into later work. The strongest supported contribution is automatic retention and delivery of derived guidance. Improved performance caused by that guidance, or by criticism of its content, remains unestablished in this analysis. The [exact result](../reports/retained-archive/AAS-2026-09-27-dynamic-cheatsheet-04/result.md) retains the route records and evidence distinctions.

## Runtime and memory

The Python benchmark owns sequencing, dataset access, persistence and resume; the selected model supplies solutions and proposed cheatsheet text. Cumulative mode can update a sheet across rounds on one problem and across later problems. Full history sends all prior solutions. Raw retrieval ranks earlier questions by cosine similarity and sends top-k solution pairs. Retrieval synthesis adds a curator before answering and retains the resulting sheet for the next curator. Hybrid combines cumulative guidance and retrieved examples, then performs one answer/update pair. The default branch supplies no cheatsheet. Direct library callers own persistence and repeated invocation. [Implementation](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [benchmark](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py).

Memory is stored in process strings/lists/arrays and JSONL/CSV files. It includes prose, formulas and possible code; precomputed embeddings are numeric ranking data, not evidence of an internal vector database or parameter updates. Whole-sheet and full-history delivery use coarse selection; retrieval uses question embeddings; retrieval synthesis adds model selection and rewriting conditioned on the upcoming question. All these supply context automatically to generators or curators. Top-k limits item count, while the curator's requested sheet length is not an enforced input-token budget. Source records OBJ-1, OBJ-2, OBJ-3 and OBJ-6 distinguish content from access data.

Cumulative, hybrid and retrieval-synthesis writes qualify as wired trace learning under the comparison contract: prior solutions, sometimes including local execution output, become retained guidance for a later model call. Raw transcript retention alone does not. This classification asserts a write/read-back mechanism, not demonstrated improvement. Semantic synthesis, deduplication and usage-count promotion are requested in prompts; only whole-sheet replacement is established as a wired curation operation at its controlled meaning. [Curator instructions](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_retrieval_synthesis.txt).

## Admission and evidence

The curator is asked to assess correctness and preserve useful strategies. The program admits its output by extracting text after an opening cheatsheet tag. Missing tags select a fallback; there is no independent semantic admission gate on these inspected paths. Cumulative fallback keeps the old sheet, whereas retrieval synthesis falls back to retrieved-pair text. The exact result records this bounded finding as ABS-1. [Extractor](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/extractor.py).

A historical first-row sheet says a rectangle count is 15 while its saved target is 315. The second row carries that sheet into the next generator prompt. This establishes retained, delivered, target-inconsistent guidance; it does not show that the next answer depended on it or independently establish the target's truth. [Historical artifact](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/results/AIME_2024/gpt-4o_DynamicCheatsheet_Cumulative.jsonl#L1-L2).

Benchmark answer evaluation happens after the new sheet has been admitted into process state. Task-specific predicates or dataset targets decide whether an answer counts correct; the result updates printed counters and does not veto the cheatsheet or remove previous solutions from retrieval. Consequently, an answer score licenses only the selected benchmark criterion, not its explanation or future applicability. The code keeps memory construction free of target labels while evaluation separately uses them. [Evaluation](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/evaluation.py), [loop](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py).

## Control and limits

Optional local Python execution runs model-produced code under the caller's OS permissions. Its timeout is not an isolation boundary. The continuation-depth check follows execution, and disabling generator code execution does not disable Python eval in arithmetic scoring. Provider-native execution is a separate dispatch path with provider-owned limits and opaque internal state. Resume restores previous sheets and solutions but checks only selected arguments; compatible dataset ordering remains an external requirement. [Local executor](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/utils/execute_code.py), [provider dispatch](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/text_generation/simple_unified_client.py).

Explicit guidance satisfies the localized-content condition of a [theory builder](../../notes/definitions/theory-builder.md) in the historical artifact. Dependence on what a particular theory says is uninspected; content-directed criticism is requested; retained criticism shaping the next round is unestablished. A complete theory-builder classification therefore does not follow. Configured solving, replacement and retention are computationally operated, but autonomous theory-building and [reflection](../../notes/definitions/reflective-system.md) remain separate unresolved claims. README performance gains remain attributed reports without reconstructed causal comparisons.

Provider weights, hidden reasoning, server-side isolation and embedding-model provenance are outside the established evidence. Candidate-linked criticism and acceptance records would change the epistemic assessment; controlled interventions on recalled content with pinned models would change the learning assessment.
