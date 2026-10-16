---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Agent Workflow Memory's shipped Mind2Web and WebArena memory loops at commit 8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1."
run-id: AAS-2026-10-12-agent-workflow-memory-cb2da079273e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/zorazrw/agent-workflow-memory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/agent-workflow-memory-cb2da079273e/related-systems/zorazrw--agent-workflow-memory
  revision: "8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1"
  sha256: null
---

# Agent Workflow Memory boundary

## Boundary and evidence

This run examines how Agent Workflow Memory (AWM) produces, selects, persists and supplies reusable web-task workflows to model-driven agents. The target is a **memory/knowledge/context-engineering system**, not a standalone browser runtime. Its declared purpose is inducing and using task subroutines through agent memory (SRC-1, `README.md`):

> Agent Workflow Memory (AWM) proposes to induce, integrate, and utilize workflows via an agent memory.
> A workflow is usually a common sub-routine in solving tasks, with example-specific contexts being abstracted out.
> --- `README.md`

The **whole-system** boundary includes both shipped benchmark implementations, their command-line drivers, agent consumers, induction alternatives, prompts, retained examples, task configurations and evaluators. These callers belong to AWM: the root quickstart sends users to both pipeline scripts, and those scripts arrange production and subsequent consumption of workflow files (SRC-1, `README.md`, `mind2web/pipeline.py`, `webarena/pipeline.py`). Whole-system describes functional coverage of the repository's shipped responsibilities, not proof that its pipelines run successfully.

### Shipped loop coverage

- **Mind2Web:** `pipeline.py` coordinates offline training-example induction or interleaved inference and online induction. `offline_induction.py` and `online_induction.py` read task examples or saved model conversations, invoke a model with shipped induction prompts, filter its output and write workflow text. `run_mind2web.py` calls `memory.py`, which reloads that text and concrete exemplars, assembles model messages, scores predictions against annotated steps and persists conversations and metrics. `results/calc_score.py` aggregates those metrics. The separate `workflow/retrieve.py` CLI selects workflow text or concrete examples and writes a consumer-ready text file; it is included as a shipped alternative, not presumed to run inside the default pipeline (SRC-1, `mind2web/pipeline.py`, `mind2web/offline_induction.py`, `mind2web/online_induction.py`, `mind2web/run_mind2web.py`, `mind2web/memory.py`, `mind2web/results/calc_score.py`, `mind2web/workflow/retrieve.py`). The consumer's file read is explicit:

> workflow_text = open(args.workflow_path, 'r').read().strip()
> if len(workflow_text):
>     memory = [[{"role": "user", "content": workflow_text}]]
> --- `mind2web/memory.py`

- **WebArena:** `pipeline.py` sequences agent inference, trajectory evaluation and neural induction. `run.py` constructs the shipped legacy agent and delegates experiment execution and trace storage to BrowserGym. The agent reloads workflow text into its system message. `autoeval/evaluate_trajectory.py` and `autoeval/evaluator.py` generate model-based admission signals; `induce_prompt.py` selects trajectories using those signals or ground-truth rewards and writes model-induced workflow text. `induce_rule.py` supplies a rule-based selection alternative with optional manual admission. The retained website text files are also included. The separate basic agent demo is covered as an auxiliary caller, not attributed a workflow-memory integration (SRC-1, `webarena/pipeline.py`, `webarena/run.py`, `webarena/agents/legacy/agent.py`, `webarena/autoeval/evaluate_trajectory.py`, `webarena/autoeval/evaluator.py`, `webarena/induce_prompt.py`, `webarena/induce_rule.py`, `webarena/agents/basic/agent.py`). The memory-consumption hook is explicit:

> if self.flags.workflow_path is not None:
>     sys_msg += '\n\n' + open(self.flags.workflow_path).read()
> --- `webarena/agents/legacy/agent.py`

Induction instructions are part of the mechanism, not merely explanatory documentation. For example, the WebArena instruction requests abstraction while retaining invariant elements (SRC-1, `webarena/prompt/instruction.txt`):

> Keep the values of invariant elements, e.g., id of "Search" or "Customers", as they will share and stay invariant across tasks.
> --- `webarena/prompt/instruction.txt`

### Top-level tracked coverage

The frozen tree has six top-level entries. All material shipped state-loop paths are included. Initial inspection is complete for the listed drivers and core loop files; auxiliary modules and large static datasets have only bounded inspection as stated below. Those limits are not access gaps and do not exclude those paths from later inspection at this commit.

| Top-level entry | Classification | Material paths and role | Initial inspection and conclusion limit |
|---|---|---|---|
| `.gitignore` | Included | Excludes generated results, configuration outputs and evaluation logs from ordinary tracking. | Read; tracking policy is not evidence of saved executions (SRC-1, `.gitignore`). |
| `LICENSE` | Excluded deliberately | Legal metadata; no state-loop responsibility. | Not inspected; no license or redistribution conclusion. |
| `README.md` | Included | Purpose, quickstarts and reported benchmark results. | Read; reported success rates are attributed claims, not independently observed runs (SRC-1, `README.md`). |
| `assets/` | Excluded deliberately | `teaser.jpg`, `online-offline.jpg`, `mind2web-results.jpg`, `webarena-leaderboard.jpg`: explanatory and benchmark illustrations linked from the README. | Images not inspected; no figure-specific numerical, architectural or experimental conclusion. The executable loops and written doctrine remain included (SRC-1, `README.md`). |
| `mind2web/` | Included | `README.md`; `pipeline.py`, `run_mind2web.py`; `offline_induction.py`, `online_induction.py`; `memory.py`; both `instruction_*.txt` and `one_shot_*.txt` pairs under `prompt/`; `data/memory/exemplars.json`; `workflow/retrieve.py`; `utils/data.py`, `utils/env.py`, `utils/llm.py`; `results/calc_score.py`; `requirements.txt`. | Drivers, induction, consumer, data formatting, retrieval, prompts, score aggregation and dependency declarations read. Exemplars sampled at the beginning; environment/LLM helper definitions searched, not exhaustively audited. No exhaustive dataset-quality or helper-correctness conclusion (SRC-1, `mind2web/README.md`, `mind2web/memory.py`, `mind2web/workflow/retrieve.py`). |
| `webarena/` | Included | `README.md`; `pipeline.py`, `run.py`; `induce_prompt.py`, `induce_rule.py`; `agents/legacy/agent.py`, `dynamic_prompting.py`, `utils/` and package initializers; `agents/basic/agent.py`; `autoeval/evaluate_trajectory.py`, `evaluator.py`, `clients.py`, `prompts.py`, `requirements.txt`; `prompt/instruction.txt`, `one_shot.txt`; all five website files under `workflow/`; `config_files/generate_test_data.py`, `test.raw.json`, `test.json`; root `requirements.txt`. | Drivers, both induction paths, both agents, evaluator and induction prompts read. Dynamic prompting and provider helpers searched; workflow text and task configurations sampled at their beginnings; config generation read. No exhaustive prompt-helper audit, per-task correctness or retained-workflow provenance conclusion (SRC-1, `webarena/README.md`, `webarena/run.py`, `webarena/induce_prompt.py`, `webarena/config_files/generate_test_data.py`). |

### External dependencies and evidence limits

BrowserGym, its WebArena integration, Playwright/browser execution, website servers, authentication state, model-provider services and third-party library implementations are external dependencies. Their setup is documented, but their code and live services are not frozen here. Consequently, this run can establish how AWM configures, calls and consumes them, not their internal execution, environment fidelity or provider behavior. In particular, BrowserGym's experiment loop and trace persistence must not be attributed to AWM's own implementation (SRC-1, `webarena/README.md`, `webarena/run.py`, `webarena/requirements.txt`).

Mind2Web benchmark splits and candidate-ranking scores are requested as downloads and are not present among the tracked source files. The shipped exemplar JSON is available, but it does not replace those inputs. This prevents reproducing benchmark scoring or checking the full training/test input boundary from this checkout alone (SRC-1, `mind2web/README.md`, `mind2web/utils/data.py`). Generated WebArena per-task configurations, runtime results, screenshots and evaluation logs are not supplied as run evidence; tracked template/configuration data and workflow examples are design inputs or retained content, not proof of the induction history that produced them (SRC-1, `webarena/config_files/generate_test_data.py`, `.gitignore`, `webarena/autoeval/evaluate_trajectory.py`).

The evidence tier is **code-grounded**: shipped source supports static mechanism tracing, and documentation supplies declared intent and reported results. No target code, tests or examples were executed, and no model services were called. There is no registered observed run or causal experiment, so successful end-to-end operation, measured performance and causal improvement remain unestablished. The applicability cutoff is **2026-10-12**, supplied by the run opening; evidence is limited to commit **8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1**, not repository changes or dependency revisions after it. The acquired checkout's HEAD was verified against that pin without modifying it.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/zorazrw/agent-workflow-memory` | 8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/agent-workflow-memory-cb2da079273e/related-systems/zorazrw--agent-workflow-memory`. Implementation: both benchmark pipelines, induction alternatives, consumers, evaluation and configuration-generation paths listed above; scoped helper searches and static-data samples. Doctrine/design: root and benchmark READMEs, induction instructions and one-shot prompts. Reported operation: root README benchmark claims only. | Implementation: [Mind2Web pipeline](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/pipeline.py), [Mind2Web consumer](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [WebArena pipeline](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py), [WebArena consumer](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/agent.py), [neural induction](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py). Doctrine/design: [induction instruction](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/prompt/instruction.txt). Doctrine/design and reported operation: [README](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/README.md). | Frozen shipped source is available. External dependency implementations, downloaded benchmark inputs and runtime artifacts are not registered; prevents host-internal, reproduced-performance and causal-effect conclusions. Auxiliary files not fully inspected remain available for later work; illustration and license exclusions prevent only their specific conclusions. No observed-run or causal-experiment layer. |
