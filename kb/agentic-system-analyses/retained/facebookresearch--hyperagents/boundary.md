---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Hyperagents' shipped improvement loop, task agents and evaluation integrations at commit 59a68f672dfb92c74aeb7e61535d776fb36e172d."
run-id: AAS-2026-10-14-hyperagents-dd9d501b160c-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/facebookresearch/Hyperagents
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/hyperagents-dd9d501b160c/related-systems/facebookresearch--Hyperagents
  revision: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
  sha256: null
---

# Hyperagents boundary

## Boundary and evidence

This run analyses how Hyperagents produces and evaluates code-modified agents, retains their lineage and results, and consumes that retained state for further improvement. The target is the shipped framework, not only `MetaAgent` or its model-call library. Its primary class is **builder or improvement plane**: an outer generation driver invokes a model-dependent code-editing agent and evaluates the resulting task agents. The task agents and their shipped callers remain inside the target. The boundary is **whole-system**, covering the framework's generation, retention, admission, replay, evaluation and selection paths, including optional ensemble and editable-parent-selection paths. This classification concerns responsibilities, not demonstrated improvement (SRC-1, `generate_loop.py`, `meta_agent.py`, `task_agent.py`, `utils/gl_utils.py`).

The repository declares the main entry point:

> - `generate_loop.py` entry point for running the algorithm
> --- `README.md`

The initial meta agent delegates code editing to a model/tool loop:

> instruction = f"Modify any part of the codebase at `{repo_path}`."
>
> new_msg_history = chat_with_agent(instruction, model=self.model, msg_history=[], logging=self.log, tools_available='all')
> --- `meta_agent.py`

The generated README describes the intended recursive improvement mechanism. This is design evidence, not evidence that the mechanism improves performance:

> This system is designed to automatically produce agents for solving downstream tasks. The system iteratively improves the generated agents through code editing. To enable continuous improvement, the system should look at its code repository and the provided path to previously generated agents and their evaluation results, and then edit and enhance its own mechanisms for generating agents. This process creates a recursive loop of self-improvement.
> --- `utils/gl_utils.py`

Initial tracing follows `setup_initial.sh` into domain harnesses and reports, then `generate_loop.py` into root-repository preparation, Docker execution, lineage-patch replay, `run_meta_agent.py`, evaluation, saved metadata and parent selection. It also follows resume loading, archive consumers, the optional ensemble wrapper and the optional selection wrapper. The archive is not itself a successful-agent-only collection: the generation driver appends generations, while separate metadata and score checks govern candidate eligibility (SRC-1, `setup_initial.sh`, `generate_loop.py`, `utils/gl_utils.py`, `select_next_parent.py`). In particular, the admission metadata is written as:

> metadata["valid_parent"] = metadata["run_eval"] and (eval_successful or meta_patch_files is not None)
> --- `generate_loop.py`

Persistence and later consumption belong to this framework. `run_meta_agent.py` saves a Git diff; `utils/gl_utils.py` saves and reloads archive and lineage metadata; `generate_loop.py` applies parent patches and copies previous evaluation outputs into the next container. Domain harnesses save task predictions or episode artifacts, reports produce scores, and selection and ensembling read retained results. The default ensemble implementation selects a scored agent's saved prediction rather than launching a fresh task-agent call (SRC-1, `run_meta_agent.py`, `utils/gl_utils.py`, `generate_loop.py`, `domains/harness.py`, `domains/report.py`, `ensemble.py`). Its durable archive append includes:

> archive_file = os.path.join(output_dir, "archive.jsonl")
> with open(archive_file, "a") as f:
> --- `utils/gl_utils.py`

### Tracked-path coverage

All rows refer to SRC-1 at the reviewed commit. “Included” establishes functional scope, not exhaustive inspection of every file. Initial inspection consists of full-file reads, bounded source reads and scoped searches. Deeper implementation not yet inspected remains available under SRC-1; it is neither excluded nor an access gap.

| Top-level tracked path | Scope and material paths | Initial inspection and role; exclusion limit |
|---|---|---|
| `.gitignore` | Excluded | Repository housekeeping; no conclusions about ignore-policy completeness. |
| `CODE_OF_CONDUCT.md` | Excluded | Community governance; no conclusions about contributor conduct controls. |
| `CONTRIBUTING.md` | Excluded | Contribution process; no conclusions about development-process assurance. |
| `Dockerfile` | Included | Read; execution image, dependencies and GPU setup. |
| `LICENSE.md` | Excluded | Licensing; no legal or redistribution assessment. |
| `README.md` | Included | Read; setup, primary entry point, file roles, declared safety warning and external-log pointer. |
| `agent/` | Included: `base_agent.py`, `llm.py`, `llm_withtools.py`, `tools/__init__.py`, `tools/bash.py`, `tools/edit.py` | Model dispatch and tool-turn loop read; tool implementations searched. Base-class and detailed tool behavior remain to inspect. Produces model responses and code-editing actions. |
| `analysis/` | Included: `plot_progress.py`, `visualize_archive.py`, `transfer_utils.py`; other plotting/statistical scripts remain available | Driver imports and archive-reader searches inspected. Shipped post-generation state consumers, visualizations and transfer-evaluation command construction. Detailed plotting and statistical behavior not yet inspected. |
| `baselines/` | Included: `dgm/coding_agent.py`, `dgm/utils.py`; excluded independent comparators: `ai_reviewer/`, `genesis_go2walking/`, `imo_grading/`, `imo_proof/`, `sft_openai/` | DGM branch traced from root preparation and driver, and its model-dependent editor/diagnosis paths searched. Other comparator internals not inspected; exclusion prevents comparative implementation or performance conclusions, not analysis of the Hyperagents loop. |
| `domains/` | Included: `harness.py`, `report.py`, `run_eval.py`, and shipped adapters under `paper_review/`, `search_arena/`, `imo/`, `balrog/`, `genesis/`, `polyglot/` | Harness/report dispatch and independent replay-evaluation entry point read. Human-preference/IMO input-formatters searched. BALROG and Genesis harnesses read and evaluator task-call/artifact paths inspected; summary-output paths searched. Polyglot per-instance runner inspected through task invocation, generated patch, test execution and result persistence. Domain configs, environment implementations, dataset curation, proof-grader setup, RL trainer/evaluator and remaining benchmark helpers remain available for deeper inspection. These shipped callers and evaluators are not treated as an external host. |
| `ensemble.py` | Included | Read; archive-score selection and saved-prediction consumption. |
| `generate_loop.py` | Included | Main generation body and lifecycle read, including resume, lineage replay, evaluation staging, metadata, optional wrappers and archive consumers. CLI definitions remain to inspect in detail. |
| `meta_agent.py` | Included | Read; initial model/tool-driven code editor. |
| `requirements.txt` | Included | Read; runtime and environment dependencies. |
| `requirements_dev.txt` | Included | Read; plotting/statistics dependencies. |
| `run_meta_agent.py` | Included | Read; editor invocation, domain-change reset and persisted diff. |
| `run_task_agent.py` | Included | Read and consumer traced in Polyglot; task invocation and code-diff output. |
| `select_next_parent.py` | Included | Read; metadata/score-based candidate filtering and random selection. |
| `setup_initial.sh` | Included | Read; initial evaluation production, domain preparation and external setup recipes. |
| `task_agent.py` | Included | Read; initial task-model call and response extraction, consumed by harnesses. |
| `utils/` | Included: `gl_utils.py`, `docker_utils.py`, `git_utils.py`, `domain_utils.py`, `common.py`, `constants.py`, `run_ensemble.py`, `run_select_next_parent.py`, `thread_logger.py` | Generation/state utilities and domain policy read; Docker image-build/GPU-setup entry inspected; optional wrappers read. Git diff/reset imports traced through their callers. Remaining transport, Git and logging internals not yet inspected. Supplies preparation, replay, persistence, scoring, selection and execution support. |

### Frozen evidence and limits

The evidence is the repository at **59a68f672dfb92c74aeb7e61535d776fb36e172d**, with applicability cutoff **2026-10-14**, the supplied run date. The checkout's HEAD matches the acquired pin and its working tree reports no changes. No additional repository, paper, live page, execution trace or downloaded experiment log is frozen by this boundary. Overall evidence tier is **code-grounded**; declared goals and setup instructions remain separately labelled doctrine/design.

External dependencies include model-provider APIs through LiteLLM, credentials, Python packages, Git, Docker-compatible execution and host networking, and domain-specific datasets, environments and GPU/RL facilities. Requirements reference additional environment repositories; setup also obtains SWE-bench and a proof-grader installation. These dependency implementations and downloaded data are not registered evidence. They cannot establish provider behavior, benchmark validity, external grader correctness, full dependency reproducibility or effective containment. Shipped integration code remains included (SRC-1, `agent/llm.py`, `requirements.txt`, `Dockerfile`, `utils/docker_utils.py`, `setup_initial.sh`, `domains/report.py`).

The README points to externally downloadable experiment logs, but those logs are not captured here. The arXiv paper and linked blog are likewise not part of SRC-1. This prevents claims grounded in those results or documents. Source inspection alone establishes neither successful execution nor causal improvement, quantitative performance, long-run stability or security against generated code. No target code, tests, examples, models or services were executed for this boundary. Available files left for deeper inspection are inspection limits, not inaccessible evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/facebookresearch/Hyperagents` | 59a68f672dfb92c74aeb7e61535d776fb36e172d | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/hyperagents-dd9d501b160c/related-systems/facebookresearch--Hyperagents`. Implementation: tracked tree; generation lifecycle in `generate_loop.py`; `meta_agent.py`, `task_agent.py`, both root run-agent scripts; `agent/llm.py`, `agent/llm_withtools.py`; `utils/gl_utils.py`, `utils/domain_utils.py`, optional ensemble/selection wrappers; `ensemble.py`, `select_next_parent.py`; `domains/harness.py`, `domains/report.py`, `domains/run_eval.py`; BALROG/Genesis harnesses and bounded evaluator reads; Polyglot per-instance harness; scoped tool, baseline, summary-output and analysis-consumer searches. Doctrine/design: `README.md`, generated README text in `utils/gl_utils.py`, `setup_initial.sh`, `Dockerfile`, requirements and in-source contracts. Coverage table distinguishes initial reads from available deeper material. | Implementation: [generation driver](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [state utilities](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py), [task harness](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/harness.py); doctrine/design: [README](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/README.md). Other anchors are the commit-relative paths named in this member at this same revision. | No established access gap within the tracked checkout. External dependencies, paper/blog and externally hosted experiment logs are not frozen; their behavior, assertions and results cannot supply evidence. No observed-run or causal-experiment layer is registered. |
