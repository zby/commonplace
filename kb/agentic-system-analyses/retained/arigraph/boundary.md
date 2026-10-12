---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "AriGraph's memory architecture and shipped game and QA consumers at commit e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2."
run-id: AAS-2026-10-12-arigraph-fd0f6f1c1383-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/AIRI-Institute/AriGraph
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/arigraph-fd0f6f1c1383/related-systems/AIRI-Institute--AriGraph
  revision: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
  sha256: null
---

# AriGraph boundary

## Boundary and evidence

This run analyses AriGraph as a model-dependent memory system, including its shipped consumers rather than only its graph API. Its intended use is to retain semantic facts and episodic observations for later game decisions and question answering. The repository also ships the Ariadne game loop, alternative memory baselines, a human-play driver and evaluation code. They belong to this whole-system boundary because they establish how memory is produced, maintained and consumed (SRC-1, `README.md`, `pipeline_arigraph.py`, `musique_test_big.py`). The primary target class remains memory/knowledge/context-engineering system; including its consumers does not imply that the graph library itself owns their planning or environment execution.

The game path covers observation processing, model-selected retrieval entities, model extraction and replacement of facts, semantic and episodic retention, retrieval, planning, action selection, navigation and environment feedback. The QA path builds memory from task paragraphs, retrieves facts and texts, and passes both to an answer model. These are shipped callers, not excluded host applications (SRC-1, `pipeline_arigraph.py`, `graphs/contriever_graph.py`, `agents/parent_agent.py`, `musique_test_big.py`). Minimum evidence for the model-dependent maintenance path:

> prompt = prompt_extraction_current.format(observation = observation, example = example)
> response, _ = self.generate(prompt, t = 0.001)
> new_triplets_raw = process_triplets(response)
> --- `graphs/contriever_graph.py:28-30`

> prompt = prompt_refining_items.format(ex_triplets = associated_subgraph, new_triplets = new_triplets)
> response, _ = self.generate(prompt, t = 0.001)
> predicted_outdated = parse_triplets_removing(response)
> self.delete_triplets(predicted_outdated, locations)
> --- `graphs/contriever_graph.py`

A later consumer uses retrieved memory to construct the QA request (SRC-1, `musique_test_big.py`):

> Relevant facts from your memory: {subgraph}
>
> Relevant texts from your memory: {episodic}
> --- `musique_test_big.py`

The boundary includes the graph's attempt-local retention and reset lifecycle, and the drivers' file logging. Retention here must not be assumed to mean restart-persistent graph storage. The inspected game driver constructs a graph per attempt, the QA driver clears it per task, and `Logger` writes textual logs or JSON objects; these are distinct responsibilities (SRC-1, `pipeline_arigraph.py`, `musique_test_big.py`, `graphs/contriever_graph.py`, `utils/utils.py`). The boundary permits later examination of any tracked file at the same revision; initial inspection is not a source allowlist.

### Repository coverage

The tree was enumerated at the pinned commit and all root driver scripts were read. “Included” means within the functional evidence boundary, not that every data item has been examined. The table distinguishes full source reads, bounded searches, sampled artifacts and deliberately excluded packaging residue. No material shipped memory producer, maintenance path or consumer identified in the entry-point trace was inaccessible.

| Top-level tracked path | Coverage | Material paths, role and inspection status | Limit or conclusion prevented |
|---|---|---|---|
| `.gitignore` | Excluded | Repository housekeeping; tree-listed only. | No conclusions about repository ignore policy. |
| `LICENSE` | Excluded | Licensing; tree-listed only. | No legal or licensing assessment. |
| `README.md` | Included | Fully read: declared architecture, results, setup and repository map. | Performance tables remain attributed reports, not independently replicated results. |
| `__pycache__/` | Excluded | Tracked compiled residue, including bytecode for modules absent as Python source. | No reconstruction of historical implementations or bytecode-only variants. |
| `agents/` | Included source; excluded bytecode | Fully read `agents/parent_agent.py` and `agents/llama_agent.py`: API calls, retrieval-entity prompts and local-generation adapter. `agents/__pycache__/` is residue. | No claims about bytecode-only agents or actual provider behavior. |
| `envs/` | Included task fixtures and generators | `utils/envs_cfg.py` and `utils/textworld_adapter.py` trace configured `.z8` games to the runtime. Bounded source search inspected imports in `envs/hunt/hunt.py`, `envs/hunt_hard/hunt_hard.py` and `envs/clean_3x3/walkthrough.py`. Cooking directories, cleaning JSON/Inform sources, hunt assets and `envs/jericho-game-suite/` were tree-listed; full task contents not yet inspected. | No exhaustive task-rule, solvability or fixture-fidelity conclusions from initial inspection. These files remain available, not an access gap. |
| `graphs/` | Included source; excluded bytecode | Fully read `graphs/parent_graph.py`, `graphs/contriever_graph.py`, `graphs/hypergraph.py`, `graphs/lazy_graph.py`: graph state, updates, deletion, retrieval, navigation, alternative representation and evaluation adapter. `graphs/__pycache__/` excluded. | Hypergraph implementation is available, but the inspected root drivers do not establish a shipped consumer for it; no execution or deployment claim for that variant. |
| `img/` | Included design assets | `img/Architecture.png` and `img/Architecture.pdf` referenced by README and tree-listed, not yet visually inspected. | No diagram-derived architectural claims at this stage. |
| `interactive_human_games.py` | Included | Fully read: human-input game driver, environment stepping and logging; also defines model helper functions. | Presence of helpers does not prove they run in the human loop. |
| `logs/` | Included retained run artifacts | All filenames enumerated. Read initial 65 lines of `logs/hunt_arigraph.txt` and 35 lines of `logs/musique_gpt.txt`: recorded observation, extraction, retrieval, plans/actions or QA answers and metrics. Other game, ablation and QA logs not yet inspected. | Samples do not establish aggregate scores, causal ablation effects or correspondence to this checkout's exact configuration. |
| `musique_test_big.py` | Included | Fully read: paragraph admission, per-task reset, retrieval, answer consumption, dataset loading, model setup and metric calculation. | Source establishes intended code paths, not successful execution of every task/model branch. |
| `pipeline_arigraph.py` | Included | Fully read: observation-to-memory-to-plan/action loop, bounded recent history, navigation, rewards and logging. | No live operational success inferred. |
| `pipeline_fullhist.py` | Included | Fully read: full-history memory baseline and its game decision consumers. | No baseline performance replication. |
| `pipeline_graph_evaluation.py` | Included | Fully read: intended fact-replacement evaluation against environment facts and walkthrough actions. | Evaluator source alone does not establish a functioning evaluation or trustworthy reported metrics. |
| `pipeline_smartrag.py` | Included | Fully read: embedding/recency/model-importance retrieval baseline and decision consumers. | No comparative effectiveness inference from code alone. |
| `pipeline_summary.py` | Included | Fully read: model-maintained summary baseline, recent history and plan/action consumption. | No comparative effectiveness inference from code alone. |
| `prompts/` | Included authored prompts; excluded bytecode | Fully read `prompts/prompts.py` and `prompts/system_prompts.py`: extraction, conservative replacement, hypergraph, reflexion, planning, exploration, action and summary instructions. `prompts/qa_prompts.py` is empty by line count. `prompts/__pycache__/` excluded, including its incidental human-game log. | Prompt intent is not evidence of model compliance; bytecode/incidental-log history is not reconstructed. |
| `qa_data/` | Included task data | `qa_data/musique_ans_v1.0_dev.jsonl` and `qa_data/hotpot_dev_distractor_v1.json` are tree-listed and their loading consumer fully read; dataset contents not yet inspected. | No independent dataset integrity, coverage or answer-quality assessment. |
| `requirements.txt` | Included | Full file read; dependency manifest is encoded with NUL-separated display in the reader. Dependencies are also traced through imports. | No installation or compatibility certification. |
| `src/` | Included source; excluded bytecode | Fully read `src/contriever.py`: embedding forward pass and retriever loading. Bounded import/function/load/save searches in `src/utils.py` and `src/dist_utils.py`: supporting model-checkpoint and distributed utilities; full bodies not yet inspected. `src/__pycache__/` excluded. | Model-checkpoint helpers are not evidence of serialized AriGraph memory; no claims about unused training/distributed paths from initial search. |
| `utils/` | Included source; excluded bytecode | Fully read `utils/contriever.py`, `utils/retriever_search_drafts.py`, `utils/utils.py`, `utils/textworld_adapter.py`, `utils/envs_cfg.py`, `utils/win_cond.py`, `utils/observedgpaph.py`: embedding retrieval, graph search, episodic ranking, parsing, logging, environment interface/configuration, cleaning rewards and auxiliary observed graph. `utils/__pycache__/` excluded. | Auxiliary observed-graph source is not evidence that the main driver uses it. |

### External dependencies and evidence limits

External dependencies include OpenAI chat completions, Hugging Face model/tokenizer loading, `facebook/mcontriever`, an optional LLaMA generation pipeline, PyTorch/Transformers, TextWorld and NetworkX. Their integration code is included; external implementation, weights, service responses and runtime environments are not frozen here (SRC-1, `agents/parent_agent.py`, `agents/llama_agent.py`, `graphs/parent_graph.py`, `utils/contriever.py`, `src/contriever.py`, `utils/textworld_adapter.py`). This prevents conclusions about actual response quality, service reliability, embedding checkpoint reproducibility or execution compatibility. The README's linked paper and hosted game site are deliberately outside this single-repository evidence set; claims requiring their contents cannot be established (SRC-1, `README.md`).

The immutable boundary is commit `e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2`, with applicability cutoff **2026-10-12**, the supplied run date. HEAD matches the acquired revision and the checkout reports no tracked modifications. Overall evidence is **code-grounded**: source reading supports implementation analysis, prompts and README support declared intent, and committed logs can support bounded recorded-operation findings. No target execution, dependency installation, provider call or fresh causal experiment was performed. Logs are repository-supplied artifacts, not newly observed runs or proof that the current scripts reproduce the reported comparisons.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/AIRI-Institute/AriGraph` | e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2 | implementation; doctrine/design; reported operation; observed run | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/arigraph-fd0f6f1c1383/related-systems/AIRI-Institute--AriGraph`. Implementation: all root Python drivers, both agent sources, four graph sources, seven utility sources and `src/contriever.py` fully read; bounded support/generator searches as listed above. Doctrine/design: README and both nonempty prompt modules fully read. Reported operation: README performance tables. Observed run: bounded initial samples of `logs/hunt_arigraph.txt` and `logs/musique_gpt.txt`, as retained attributed execution records, not independent observations. | Implementation: [game loop](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/pipeline_arigraph.py), [memory](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/graphs/contriever_graph.py), [QA](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/musique_test_big.py), [logging/ranking](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/utils/utils.py). Doctrine/design: [prompts](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/prompts/prompts.py), [README](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/README.md). Recorded operation: [game log](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/logs/hunt_arigraph.txt), [QA log](https://github.com/AIRI-Institute/AriGraph/blob/e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2/logs/musique_gpt.txt). | No source-checkout access gap. External services, weights and the linked paper/site are not frozen. Initial uninspected assets/data are identified in coverage, not unavailable. Reported tables and supplied logs do not establish independent reproducibility or causal effectiveness; no causal-experiment layer is claimed. |
