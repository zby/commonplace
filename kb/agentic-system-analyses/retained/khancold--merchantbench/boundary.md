---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MerchantBench's shipped benchmark workflow, simulator, agent clients and evaluators at the frozen public Git revision."
run-id: AAS-2026-10-15-merchantbench-d2f4d78dbe37-01
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: d9e5bd7519ab100193c21778aecfb59e30f24651
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/khancold/MerchantBench
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/merchantbench-d2f4d78dbe37/related-systems/khancold--MerchantBench
  revision: d9e5bd7519ab100193c21778aecfb59e30f24651
  sha256: null
---

# MerchantBench boundary

## Boundary and evidence

MerchantBench is in scope as a model-dependent benchmark **workflow**. The target is the complete shipped public artifact, not just its HTTP SDK or simulator. Its intended use is long-horizon evaluation of agents operating a simulated store. The artifact includes its own ReAct agent loop, simulator, launchers, persistence, tools, human interface and evaluator. Deterministic baselines are included as alternate consumers of the same protocol, not classified as model-calling agents themselves (SRC-1, `README.md`, `agent/submission_template/my_agent.py`, `agent/baselines/react_160k_compact_30k.py`).

> This repository contains the simulator, agent SDK and reference baselines,
> evaluation harness, batch runner, and test suite. Credentials, local run
> records, private source-system connectors, and non-redistributable datasets are
> intentionally excluded.
> --- `README.md`

The whole-system boundary follows the shipped loop: `env/run.py` builds the Flask application; `env/web/app.py` installs agent and dashboard routes around the run registry; `env/web/run_worker.py` advances the simulation; observations and scenario-derived briefs reach the agent through `env/web/routes_agent.py` and the SDK. The ReAct baseline builds a model request from its history and environment tool schemas, then sends returned actions through the SDK. The agent route dispatches tools, records messages and usage, and releases the simulation hook. These are in-repository callers and consumers, not excluded applications (SRC-1, the named paths and `agent/baselines/react_160k_compact_30k.py`).

The model-calling path is executable source, rather than an SDK-only proposal:

> return self.openai.chat.completions.create(**request)
> --- `agent/baselines/react_160k_compact_30k.py`

State coverage includes simulator listings/orders/cash, SQLite-backed rehydration, delta snapshots and checkpoints, agent traces/costs, the run-local Markdown memory tools and their write history, and the ReAct history-compaction branch. Scenario configuration and composed prompts are part of the boundary because they determine what the model receives and which tools it can call. The evaluator and batch launcher are included because they create runs and consume terminal state (SRC-1, `env/core/simulator.py`, `env/web/runner.py`, `env/tools/tools.py`, `env/tools/observation.py`, `env/scenarios/default.yaml`, `eval/run_eval.py`, `eval/scoring.py`, `scripts/run_batch.py`).

Documentation and executable defaults must be distinguished. Although `agent/README.md` says the default scenario denies memory tools, the frozen `env/scenarios/default.yaml` comments out those denylist entries. Thus this boundary includes memory tools and their configured availability; it does not adopt the documentation's default-denial assertion (SRC-1, those two paths).

> tool_denylist:                 # null = 全部工具可用；例: [search_products] → 禁用 search_products
>     - market_brief
>     - hot_search_terms
>     # - read_memory_doc
>     # - write_memory_doc
> --- `env/scenarios/default.yaml`

### Frozen evidence and limits

The sole frozen evidence source is SRC-1 at full commit `d9e5bd7519ab100193c21778aecfb59e30f24651`; its checkout HEAD was verified against the acquisition pin. The applicability cutoff is 2026-10-15, the supplied run date, not a claim about later repository state. Overall evidence is code-grounded, supplemented by source-native design documentation. No target, tests, examples, model endpoints or container evaluation were executed. Test source establishes intended assertions, not passing tests; no observed run or causal experiment is registered.

External dependencies include Python libraries, an OpenAI-compatible model provider for ReAct, Docker for hosted evaluation, and optionally a separately installed Hermes adapter/runtime. MerchantBench's Hermes discovery, profile preparation and subprocess-launch code are included; the external Hermes runtime and its skills/session implementation are not frozen here. This prevents conclusions about Hermes-internal memory, skill evolution or actual isolation behavior beyond the MerchantBench-side setup (SRC-1, `env/web/runner.py`, `README.md`).

Private business catalogs, opportunity-report datasets, credentials, historical local runs, arbitrary submitter images and source-system connectors are not available in this public source set. Their absence prevents reproduction claims about private-data research results or submitted agents' actual performance. The synthetic-data path and private-data loader interfaces remain inside the artifact boundary. The paper, project website, news links and external Hermes repository were not acquired and cannot supply evidence. Their exclusion prevents verification of their claims, not inspection of the shipped public workflow (SRC-1, `README.md`, `env/README.md`).

### Top-level tracked coverage

Included means within this analysis target, not that every file has already been inspected. Initial inspection traced the material loop above. Remaining source files at this commit may be inspected by later analysts; they are not access gaps.

| Top-level tracked entry | Classification and material paths | Initial inspection / exclusion consequence |
| --- | --- | --- |
| `.env.example` | Included: credential and provider configuration template. | Tree inventoried; contents not yet inspected. No credential validity established. |
| `.gitignore` | Included: generated/local artifact exclusions. | Tree inventoried; contents not yet inspected. No repository-hygiene audit claimed. |
| `LICENSE` | Included: distribution terms. | Tree inventoried; contents not yet inspected. No legal assessment claimed. |
| `README.md` | Included: public purpose, artifact paths, deployment and external integration declarations. | Read in full; doctrine/design evidence. |
| `agent/` | Included: `sdk/merchantbench_tool_client.py`, compatibility SDK, `baselines/react_160k_compact_30k.py`, `baselines/rule_based.py`, `baselines/auto_seed.py`, submission stub/Dockerfile and requirements. | Read agent README, SDK observation/action contract, ReAct prompt/model/action and compaction paths, submission stub; searched deterministic baseline entry points. Container recipe and remaining baseline internals await detailed inspection. |
| `assets/` | Excluded: architecture illustration, logos and badges. | Images not inspected as behavioral evidence; prevents conclusions based on diagram details or branding, not the executable loop. |
| `env/` | Included: `run.py`; `web/app.py`, `runner.py`, `run_worker.py`, agent/dashboard routes and templates/auth; `core/` simulation, orders, supplier events and ratings; `tools/` schemas/dispatch/observations/memory; `storage/` database, traces, snapshots/replay; `data/` loaders/generator; `scenarios/` defaults and Hermes overlay; requirements/compatibility modules. | Traced app entry, worker, observation/action dispatch, simulator hook persistence, rehydration, memory read/write, brief construction and default configuration. Searched storage replay and dispatch. Detailed domain equations, dashboard/template rendering, loader internals and overlay contents remain for later inspection; no unavailable shipped path identified. |
| `eval/` | Included: `run_eval.py`, `scoring.py`, `env_image/Dockerfile`, requirements and operator documentation. | Read operator manual, container/run/terminal-metric flow and scoring. Build recipe not yet inspected; no container-build or benchmark-result claim. |
| `requirements.txt` | Included: artifact dependency aggregation. | Tree inventoried; contents not yet inspected. No dependency/version audit claimed. |
| `scripts/` | Included: `run_batch.py`, `batch_queue.yaml` experiment driver/configuration. | Read run creation and finish polling; searched queue/job entry points. Queue contents and scheduler internals remain for later inspection. |
| `tests/` | Included: synthetic protocol, state, memory, ReAct, scoring and launcher contracts. | Read memory-tool schema/round-trip/history test source; other tests inventoried, not executed or fully inspected. No test-pass or experimental efficacy claim. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/khancold/MerchantBench` | d9e5bd7519ab100193c21778aecfb59e30f24651 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/merchantbench-d2f4d78dbe37/related-systems/khancold--MerchantBench`. Implementation: shipped tree and entry-point tracing through ReAct, SDK, app/registry/worker, observation/action dispatch, simulator finalization, memory tools, default scenario, batch creation and evaluator/scoring; memory-tool test source. Doctrine/design: root, agent and env READMEs and evaluator operator manual. These are initial inspected paths, not a restriction on other files at this commit. | Implementation: [ReAct](https://github.com/khancold/MerchantBench/blob/d9e5bd7519ab100193c21778aecfb59e30f24651/agent/baselines/react_160k_compact_30k.py), [agent routes](https://github.com/khancold/MerchantBench/blob/d9e5bd7519ab100193c21778aecfb59e30f24651/env/web/routes_agent.py), [simulator](https://github.com/khancold/MerchantBench/blob/d9e5bd7519ab100193c21778aecfb59e30f24651/env/core/simulator.py), [registry](https://github.com/khancold/MerchantBench/blob/d9e5bd7519ab100193c21778aecfb59e30f24651/env/web/runner.py), [scoring](https://github.com/khancold/MerchantBench/blob/d9e5bd7519ab100193c21778aecfb59e30f24651/eval/scoring.py). Doctrine/design: [README](https://github.com/khancold/MerchantBench/blob/d9e5bd7519ab100193c21778aecfb59e30f24651/README.md), `agent/README.md`, `env/README.md`, `eval/OPERATOR.md`. Additional inspected anchors are named in the coverage account above. | No unavailable public code identified. External Hermes code, private datasets/connectors, model service behavior and local historical runs are outside this frozen source; no conclusions about their internal operation or empirical performance. No observed-run or causal-experiment evidence. |
