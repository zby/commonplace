---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Dynamic Cheatsheet's shipped memory-generation, retrieval, persistence and evaluation paths at commit 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9."
run-id: AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/suzgunmirac/dynamic-cheatsheet
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-workflow-ca0a0b29d273/related-systems/suzgunmirac--dynamic-cheatsheet
  revision: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
  sha256: null
---

# Dynamic Cheatsheet boundary

## Boundary and evidence

This run analyses how Dynamic Cheatsheet creates, carries forward, retrieves and consumes inference-time memory. The target is the shipped repository system, not just the `LanguageModel` API. It is an in-scope **memory/knowledge/context-engineering system**: model-generated answers supply material for model-based curation, and retained text or previous input-output pairs become context for later model calls. The README declares this intended use (SRC-1, `README.md`):

> A lightweight framework that gives language models (LMs) a persistent, evolving memory during inference time.
> --- `README.md`

The **whole-system** boundary includes the benchmark driver and interactive example as well as the library, its shipped prompts, provider client and evaluation consumers. The driver owns cross-example state, disk persistence and continuation; these responsibilities are not assigned to an excluded host. Initial inspection traced all six supported approaches in `advanced_generate`: default generation, cumulative curation, retrieval with synthesis, cumulative plus retrieval, full-history appending and direct retrieval. It also traced the generator's local-code continuation and provider-native code-execution branches (SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`, `text_generation/simple_unified_client.py`).

Cumulative curation passes the question, generated response and previous cheatsheet into a curator call, then admits the extractor's returned text as the next cheatsheet (SRC-1, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`). This is an executable memory-update path, not solely a claim in documentation:

> # Extract the new cheatsheet from the output (if present); otherwise, return the old cheatsheet
> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
> cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py`

The shipped curator prompts are part of the system's maintenance contract. They request retention, refinement, usage counts and explicit copying of useful previous content. Their instructions to verify correctness are model-facing intent, not evidence of an independently enforced correctness gate (SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`). The generator prompt supplies the consumption contract and answer/code-execution formatting (SRC-1, `prompts/generator_prompt.txt`).

The benchmark driver initializes memory, optionally reloads the last cheatsheet and previous outputs from JSONL, passes earlier state to the library, carries the returned cheatsheet into the next example and rewrites the output checkpoint after each example. The standalone example notebook also feeds returned cheatsheets into subsequent calls (SRC-1, `run_benchmark.py`, `ExampleUsage.ipynb`). The continuation path is explicit:

> # Load the previous cheatsheet from the last output (if available)
> last_cheatsheet = outputs[-1].get("final_cheatsheet")
> if last_cheatsheet is not None:
>     cheatsheet = last_cheatsheet
>
> generator_outputs_so_far = [output["final_output"] for output in outputs]
> --- `run_benchmark.py`

The evaluation boundary includes online scoring in the benchmark driver and later scoring of retained JSONL in the evaluation notebook. This prevents treating the repository as only a stateless API or omitting its shipped persistence/reload/evaluation loop (SRC-1, `run_benchmark.py`, `EvaluatingResults.ipynb`, `dynamic_cheatsheet/utils/evaluation.py`).

### Tracked top-level coverage

All rows refer to SRC-1 at the reviewed commit. “Not yet inspected” describes available evidence, not an access gap. Artifact contents remain available to later jobs at the same revision.

| Top-level tracked path | Inclusion and material paths | Inspection and role; exclusions or remaining limits |
|---|---|---|
| `.gitignore` | Included as repository configuration. | Inspected; ignores environment files and several generated paths. Does not establish runtime retention guarantees. |
| `LICENSE` | Deliberately excluded from operational analysis. | Legal text; no licensing conclusion is reached. |
| `README.md` | Included: overview, approaches, API usage, CLI, continuation, dependencies and reported performance. | Fully inspected. Design and reported-operation evidence only; advertised improvements are not independently reproduced. |
| `run_benchmark.py` | Included: argument entry point, task loading, prompt loading, initialization, continuation, embedding alignment, sequential generation, state carry-forward, scoring and JSONL writes. | Fully inspected; shipped producer, persister, reloader and consumer of memory. |
| `ExampleUsage.ipynb` | Included: all source cells loading prompts, calling cumulative generation and passing returned cheatsheets into later calls. | Source cells inspected through JSON extraction; saved outputs not yet inspected. No observed-success claim is drawn from notebook comments. |
| `EvaluatingResults.ipynb` | Included: JSONL loader, retained-output answer extraction and task-specific scoring loop. | Fully inspected as source; no new evaluation executed. |
| `dynamic_cheatsheet/` | Included: `language_model.py`; `utils/extractor.py`, `utils/execute_code.py`, `utils/evaluation.py`; package initializers and auxiliary `utils/sonnet_eval.py`. | Core model/memory paths and three active utilities fully inspected. Initializers and sonnet evaluator received tree/signature-level inspection; `evaluation.py` comments out the sonnet import. Auxiliary sonnet scoring internals are not yet inspected, so no sonnet-evaluator correctness conclusion is reached. `.DS_Store` and tracked `__pycache__/` files are deliberately excluded as metadata/compiled artifacts; no equivalence between bytecode and source is claimed. |
| `text_generation/` | Included: `__init__.py` exports and `simple_unified_client.py` provider initialization, message-based dispatch, retries, provider response handling and native code execution. | Active routes used by `LanguageModel` inspected. Additional client web-search helpers, citation logging and standalone chat/history convenience methods are not yet fully inspected; no claim about their full behavior or compatibility. They are not an excluded host. |
| `prompts/` | Included: `generator_prompt.txt`, `curator_prompt_for_dc_cumulative.txt`, `curator_prompt_for_dc_retrieval_synthesis.txt`. | All three fully inspected; state-consumption and maintenance instructions. |
| `data/` | Included: AIME 2020–2024, AIME 2024, AIME 2025, GPQA Diamond, MMLU-Pro Engineering/Physics and MathEquationBalancer task bundles; each bundle's `dataset_info.json`, `state.json` and Arrow data/cache files. | Metadata inspected for all seven bundles and driver loading traced. Arrow payloads not yet inspected; no item-level quality, provenance or leakage conclusion. `.DS_Store` deliberately excluded; no operational conclusion depends on it. |
| `embeddings/` | Included: eight task CSVs, including `GameOf24.csv`, and their retrieval consumption in the driver. | All CSV headers and first-row structure inspected; input-to-vector alignment path traced. Full vectors and their generation provenance not yet inspected; no embedding-quality or reproducibility conclusion. |
| `results/` | Included: task JSONL bundles for baseline, empty-cheatsheet, direct-retrieval, cumulative and retrieval-synthesis configurations. | Tracked inventory, one AIME cumulative record's keys/step keys and both scoring/persistence consumers inspected. Full trace payloads not yet inspected; no accuracy, causal improvement or equivalence to current code claim. `.DS_Store` deliberately excluded. |
| `figures/` | Deliberately excluded: `Illustration.png`, `OverallPerformance.png`, `ClaudeSonnetRadarChart.png`. | Presentation images, not executable paths; no graph-derived measurement or performance conclusion. |

### Frozen evidence and dependencies

The sole frozen source is SRC-1, repository `https://github.com/suzgunmirac/dynamic-cheatsheet` at full commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. The acquired checkout's HEAD matches that commit and its status was clean at inspection. The applicability cutoff is **2026-10-12**; later repository revisions and live services are outside this evidence. Overall evidence is **code-grounded**. No target execution, provider call or benchmark reproduction was performed.

External dependencies include the selected provider's SDK/service, OpenAI-compatible endpoints, Python and the local subprocess environment, NumPy/scikit-learn for retrieval, tiktoken, pandas, datasets, dotenv and typed argument parsing. The driver loads Game of 24 through the external `turingmachine/meta-prompting` dataset rather than a shipped local task bundle. These interfaces are visible in SRC-1, `README.md`, `run_benchmark.py`, `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/execute_code.py` and `text_generation/simple_unified_client.py`; their external implementations and moving service/data versions are not frozen here. This prevents conclusions about present provider compatibility, remote execution isolation, exact external dataset bytes or complete environment reproducibility. Local execution source remains included; remote sandbox claims do not establish local sandboxing.

The linked paper is not captured or registered and is deliberately excluded. Paper-only experimental conditions and causal explanations cannot support this run. Repository result files remain eligible frozen evidence, but their presence or schema alone does not establish an observed memory benefit. No required shipped state-producing, updating, admitting, persisting, reloading or consuming source path was unavailable; the uninspected artifact payloads and auxiliary facilities above limit claims rather than turning the core loop into a partial boundary.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/suzgunmirac/dynamic-cheatsheet` | 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-workflow-ca0a0b29d273/related-systems/suzgunmirac--dynamic-cheatsheet`. Implementation: complete benchmark driver, model wrapper, extractor, local executor and active evaluation utility; notebook source cells; exported client and its active provider/message/retry/code-execution routes; task metadata, CSV headers and one result-record schema. Doctrine/design: README and all three shipped prompts. Reported operation: README performance statements, not independently validated. Coverage table distinguishes auxiliary and payload inspection limits. | Implementation: [driver](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py), [memory wrapper](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [evaluation consumer](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/EvaluatingResults.ipynb), [provider client](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/text_generation/simple_unified_client.py). Doctrine/design: [cumulative prompt](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt). Doctrine/design and reported operation: [README](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md). | No unavailable required repository source. External providers, SDK implementations, remote dataset revision and linked paper are not frozen; prevents current-service, full reproducibility and paper-only conclusions. Available but uninspected notebook outputs, full results, Arrow payloads and embedding provenance do not yet support observed-run or causal-experiment findings. |
