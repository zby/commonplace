---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Dynamic Cheatsheet's shipped inference-memory loop, benchmark drivers and evaluation at commit 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9."
run-id: AAS-2026-10-20-dynamic-cheatsheet-523b6948294d-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
analysis-cutoff: "2026-10-20"
evidence-tier: code-grounded
source:
  identity: https://github.com/suzgunmirac/dynamic-cheatsheet
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-523b6948294d/related-systems/suzgunmirac--dynamic-cheatsheet
  revision: 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9
  sha256: null
---

# Dynamic Cheatsheet boundary

## Boundary and evidence

This run examines how Dynamic Cheatsheet produces, curates, retains and reuses inference-time memory. It includes the shipped benchmark and notebook callers, not only the `LanguageModel` API. The target is a memory/knowledge/context-engineering system with a whole-system functional boundary: generator and curator calls, text extraction, cumulative and retrieval variants, code-execution continuations, caller-owned state, persistence and reload, and evaluation. This classification is grounded in SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`, `ExampleUsage.ipynb` and the three files under `prompts/`.

The wrapper returns updated memory; the shipped benchmark driver carries it into later queries and restores it on continuation. These are target responsibilities, not an excluded host's storage service (SRC-1, `run_benchmark.py`). The notebook also passes returned memory into subsequent calls (SRC-1, `ExampleUsage.ipynb`). Minimal implementation anchors establish the complete caller/API loop:

> cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py`

> last_cheatsheet = outputs[-1].get("final_cheatsheet")
> if last_cheatsheet is not None:
>     cheatsheet = last_cheatsheet
> --- `run_benchmark.py`

> write_jsonl(args.save_path_name, outputs)
> --- `run_benchmark.py:314-317`

The curator instructions are part of the mechanism, including the explicit replacement-loss warning; they are not evidence that the model reliably obeys it (SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`).

> N.B. Keep in mind that once the cheatsheet is updated, any previous content not directly included will be lost and cannot be retrieved. Therefore, make sure to explicitly copy any (or all) relevant information from the previous cheatsheet to the new cheatsheet!!!
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

The frozen evidence is SRC-1 at full commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`; the acquisition checkout's HEAD was verified against that pin. The applicability cutoff is 2026-10-20, not a claim that the checkout reflects later upstream changes. Overall evidence is code-grounded. No target code, tests, examples or provider requests were executed.

External dependencies include provider SDKs and model services, local Python and installed packages, filesystem storage, and Hugging Face dataset access for the Game of 24 benchmark. Their implementations and live availability are outside this source boundary. Consequently this run cannot establish current provider compatibility, model obedience, execution isolation supplied by hosted services, or reproducibility of remote dataset contents from source inspection alone (SRC-1, `README.md`, `run_benchmark.py`, `dynamic_cheatsheet/utils/execute_code.py`, `text_generation/simple_unified_client.py`). The linked paper is not separately acquired: statements reproduced in the README remain attributed claims, not independently inspected paper evidence.

### Top-level tracked coverage

“Included, pending” denotes available frozen evidence not yet inspected, not an access gap. The operational producer/maintenance/consumer paths were traced before choosing whole-system; pending corpus inspection does not remove those paths from the boundary.

| Top-level tracked path | Treatment and inspected material paths | Role and limits |
|---|---|---|
| `.gitignore` | Excluded; tree-listed only | Repository hygiene. No conclusions about ignored credentials or untracked deployment files. |
| `LICENSE` | Excluded; tree-listed only | Legal metadata; licensing assessment is not undertaken. |
| `README.md` | Included; inspected | Declared purpose, installation, API examples, approaches and reported performance. Performance prose is not an independently verified outcome. |
| `run_benchmark.py` | Included; inspected in full | CLI entry point, prompt/dataset loading, previous-output corpus and embedding alignment, generator invocation, memory handoff, initialization, JSONL persistence, continuation and scoring. |
| `ExampleUsage.ipynb` | Included; all cell source inspected | Shipped interactive caller reloads prompts and reuses returned cheatsheets on repeated inputs. Saved outputs not inspected; no notebook-success inference. |
| `EvaluatingResults.ipynb` | Included; all cell source inspected | Reloads JSONL results, extracts answers and dispatches task scorers. Saved outputs not inspected; no aggregate accuracy conclusion. |
| `dynamic_cheatsheet/` | Included; `language_model.py`, `utils/extractor.py`, `utils/execute_code.py`, `utils/evaluation.py` inspected in full; empty root `__init__.py` inspected | Generator/curator, retrieval and hybrid branches, full-history baseline, extraction/admission, local execution, and scoring. `utils/sonnet_eval.py` inspected only by function/import inventory; available auxiliary poetry scorer, not called by inspected benchmark/notebook paths. No poetry-evaluation correctness claim. Empty package initializers have no substantive loop role. Tracked `__pycache__/` and `.DS_Store` excluded as generated artifacts; bytecode/source parity not assessed. |
| `text_generation/` | Included; `__init__.py` and relevant `simple_unified_client.py` dispatch, retry, provider generation and code-interpreter methods inspected | Shipped provider adapter consumed by `LanguageModel`. Additional standalone chat/web-search conveniences are available but not fully inspected; no claim about those standalone APIs. Remote SDK/service internals excluded. |
| `prompts/` | Included; `generator_prompt.txt`, `curator_prompt_for_dc_cumulative.txt`, `curator_prompt_for_dc_retrieval_synthesis.txt` inspected in full | Memory consumption and maintenance doctrine, requested validation, formatting and retention. Instructions do not establish compliance. |
| `data/` | Included, pending content inspection; tree inventories AIME_2020_2024, AIME_2024, AIME_2025, GPQA_Diamond, MMLU_Pro_Engineering, MMLU_Pro_Physics and MathEquationBalancer Arrow datasets, metadata and state files | Frozen benchmark inputs and labels loaded by driver. No dataset-integrity or leakage conclusion from this boundary pass. `.DS_Store` excluded as generated metadata. |
| `embeddings/` | Included, pending content inspection; CSVs for those seven datasets plus GameOf24 identified | Precomputed retrieval input consumed by driver and API. No assertion about embedding generation, alignment correctness or vector quality beyond inspected caller logic. |
| `results/` | Included, pending content inspection; task directories and baseline/cumulative/retrieval-synthesis/retrieval/empty-cheatsheet JSONL files inventoried | Supplied historical result artifacts, available for later bounded run-evidence inspection. No observed-run or causal-experiment claim yet. `.DS_Store` excluded. |
| `figures/` | Excluded; `ClaudeSonnetRadarChart.png`, `Illustration.png`, `OverallPerformance.png` tree-listed | Expository diagrams/charts. Their graphical content supplies no independently inspected performance or mechanism evidence here. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/suzgunmirac/dynamic-cheatsheet` | 5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/dynamic-cheatsheet-523b6948294d/related-systems/suzgunmirac--dynamic-cheatsheet`. Implementation: full tracked-tree inventory, benchmark driver, language-model wrapper, extraction, local execution and task evaluation; notebook cell source; provider dispatch/retry/generation/code-interpreter methods. Doctrine/design: README and all shipped prompt templates. Reported operation: README performance prose only. Remaining available material is distinguished in coverage above. | Implementation: [driver](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/run_benchmark.py), [wrapper](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/dynamic_cheatsheet/language_model.py), [example caller](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/ExampleUsage.ipynb), [result consumer](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/EvaluatingResults.ipynb), [provider adapter](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/text_generation/simple_unified_client.py). Doctrine/design: [curator](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/prompts/curator_prompt_for_dc_cumulative.txt). Reported operation: [README](https://github.com/suzgunmirac/dynamic-cheatsheet/blob/5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9/README.md). | No repository access gap found. Remote providers, remote dataset snapshot and linked paper are not separately frozen, preventing claims about their internals or present operation. Result payloads and saved notebook outputs remain uninspected, not unavailable; no measured outcome or causal attribution is established by this member. |
