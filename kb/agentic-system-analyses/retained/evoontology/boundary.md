---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "EvoOntology's shipped ontology lifecycle, host plugins and benchmark consumers at commit c94389b764394379086ff25e50d0e0f4396167b4."
run-id: AAS-2026-10-13-evoontology-f2d0c7992c6e-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: c94389b764394379086ff25e50d0e0f4396167b4
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/ruc-datalab/EvoOntology
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/evoontology-f2d0c7992c6e/related-systems/ruc-datalab--EvoOntology
  revision: c94389b764394379086ff25e50d0e0f4396167b4
  sha256: null
---

# EvoOntology boundary

## Boundary and evidence

This run analyses EvoOntology as a versioned knowledge layer for data agents. Its intended use is to retain grounded semantic objects, serve relevant objects during later analysis, and revise the retained layer from task evidence. The target class is **memory/knowledge/context-engineering system**, not an autonomous enclosing agent runtime. Its deterministic core serves model-dependent work through MCP; shipped host-agent skills supply construction and evolution instructions. The classification includes those instructions rather than treating the Python library alone as the system (SRC-1, `docs/architecture.md`, `plugins/evoontology-codex/AGENTS.md`, `evoontology/runtime/mcp_server.py`).

> The core package provides deterministic capabilities only. Build and Evolve intelligence remains in the skills; Python implements the runtime, minimal deterministic validation, and the evolution lifecycle state machine.
> --- `docs/architecture.md`

The boundary is **whole-system** for the material shipped lifecycle: workload preparation; construction and semantic evidence commitment; version persistence and selection; manifest and semantic-tool consumption; task recording; reminders; candidate diagnosis and patch instructions; evaluation adapters and admission; publication and subsequent reload; and outcome presentation. Both plugin bundles and all three benchmark environments are included. The benchmark drivers are shipped consumers and evaluators, not excluded hosts. Whole-system here denotes responsibility coverage, not a claim that every helper, translated document or test assertion has been inspected (SRC-1, `evoontology/workflow.py`, `evoontology/ontology/store.py`, `evoontology/evolution/session.py`, `benchmarks/registry.py`).

### Entry-point and consumer trace

- Marketplace manifests select the Claude Code and Codex plugin directories. Each plugin's `.mcp.json` selects a launcher that runs its bundled `evoontology/runtime/mcp_server.py`. The server dispatches semantic retrieval to `SemanticLayer` and lifecycle operations to `ops`; those operations reach `ProjectWorkflow`, version storage and `EvolutionSession`. These are included shipped paths, even though an external host decides when to call them (SRC-1, `.agents/plugins/marketplace.json`, `.claude-plugin/marketplace.json`, `plugins/claude-code/.mcp.json`, `plugins/claude-code/scripts/launch-evoontology`, `plugins/evoontology-codex/.mcp.json`, `plugins/evoontology-codex/scripts/launch_evo_semantic_mcp`, `evoontology/runtime/mcp_server.py`, `evoontology/runtime/ops.py`).
- Build/Evolve skills and their referenced interaction, workload and data-boundary instructions govern the model's production and maintenance of semantic state. Codex's `AGENTS.md` also directs later semantic consumption and explicit task recording. Claude Code's SessionStart hook reaches `EvolutionTrigger` through `check-reminder.py`; the trigger reminds rather than launches evolution (SRC-1, `plugins/evoontology-codex/skills/build-ontology/SKILL.md`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`, `plugins/claude-code/skills/evolve-ontology/SKILL.md`, `plugins/evoontology-codex/AGENTS.md`, `plugins/claude-code/hooks/hooks.json`, `plugins/claude-code/scripts/check-reminder.py`, `evoontology/trigger/trigger.py`).
- Version files are persisted under the resolved workspace and later loaded either through the active selector or an explicit version. The server reloads the selected semantic layer on semantic calls. `ProjectWorkflow` pins a task's version, records observations and appends completed task records to `TrajectoryStore`. This connects retained state to subsequent use rather than ending the boundary at a returning API (SRC-1, `evoontology/ontology/store.py`, `evoontology/runtime/mcp_server.py`, `evoontology/workflow.py`, `evoontology/trajectory/trajectory.py`).

> SemanticStore.publish(self.workspace, candidate, target)
> EvolutionTrigger(str(self.workspace)).advance_checkpoint()
> run["status"] = ACCEPTED
> --- `evoontology/evolution/session.py`

- BIRD's adapter invokes `run_evaluation.py`, which selects semantic versions, builds a manifest, connects MCP tools, runs the shipped data agent, scores SQL and optionally calls its trajectory recorder. DDR's adapter invokes `run_agent.py` and `run_evaluation.py`; the data agent loads a semantic version, passes its manifest into the agent and persists a normalized message trace. InsightBench's adapter invokes `main.py run`; its agent constructs the semantic layer and `ToolCallingChat`, while its runner scores and optionally retains task artifacts. These consumer and evaluator paths remain in scope, including their local ontology bindings and prompts (SRC-1, `benchmarks/bird/evolution_adapter.py`, `benchmarks/bird/run_evaluation.py`, `benchmarks/bird/trajectory_recorder.py`, `benchmarks/bird/agent/prompt_manager.py`, `benchmarks/ddr_10k/evolution_adapter.py`, `benchmarks/ddr_10k/agent/data_agent.py`, `benchmarks/insightbench/evolution_adapter.py`, `benchmarks/insightbench/insightbench/agents.py`, `benchmarks/insightbench/insightbench/runner.py`).

> Task execution and scoring live inside each benchmark's runner and evaluator
> entry points, which the adapter drives as subprocesses. The adapter normalizes
> their results for the evolution lifecycle.
> --- `benchmarks/registry.py`

- The explorer reloads available versions and combines them with retained workload and terminal-run summaries through `build_experience`. It is a later consumer of retained content, not just README media (SRC-1, `plugins/evoontology-codex/skills/explore-ontology/SKILL.md`, `evoontology/visualization/renderer.py`, `evoontology/workflow.py`).

### Top-level tracked coverage

All rows refer to SRC-1 at the frozen revision. “Included” declares functional scope. Initial inspection is narrower where stated; uninspected available files are not access gaps and remain available to later jobs.

| Top-level file or directory | Status and material paths | Role, initial inspection and limits |
| --- | --- | --- |
| `.agents/` | Included: `plugins/marketplace.json` | Inspected Codex plugin discovery and local bundle selection. |
| `.claude-plugin/` | Included: `marketplace.json` | Inspected Claude Code plugin discovery and local bundle selection. |
| `LICENSE` | Excluded deliberately | Legal terms, not lifecycle behavior; no licensing analysis. |
| `README.md` | Included; inspected | System intent, lifecycle and reported benchmark scores. Scores are attributed reports, not reproduced results. |
| `README.zh-CN.md` | Excluded deliberately | Translated overview; no claim about translation fidelity or additional Chinese-language assertions. |
| `USAGE.md` | Included, not yet inspected | Available operational guide; initial trace uses implementation and plugin instructions, not this guide's detailed claims. |
| `USAGE.zh-CN.md` | Excluded deliberately | Translated usage guide; no translation-fidelity conclusion. |
| `assets/` | Excluded deliberately: demo video, framework/overview figures, ontology-layer screenshots, logo and contact image | Presentation media; no conclusion about demonstrated execution or visual UI behavior from these assets. Executable explorer code is included separately. |
| `benchmarks/` | Included: registry/CLI; BIRD adapter, agent/manifest, SQL evaluation, trajectory recorder, local `tceo`, MCP servers and configs; DDR adapter, batch runners, agent/providers/prompts, local `tceo`, MCP servers and evaluators; InsightBench adapter, `main.py`, agents, runner, prompts, local `tceo`, tools and metrics | Inspected registry, all three adapter implementations and the consumption/recording ranges identified above; searched local stores, evaluator paths and prompt connections. Remaining helpers/configuration details are available but not yet inspected. Dataset downloads, loaders and construction scripts remain in scope as setup paths; actual external datasets and benchmark execution are not frozen here. |
| `docs/` | Included: `architecture.md`, documentation indexes and `guide/new-benchmark.md`; translated counterparts excluded deliberately | Inspected architecture and integration responsibilities. Remaining English guidance is not yet inspected. Exclusion prevents translation assessment, not tracing the shipped loop. |
| `evoontology/` | Included: `workspace.py`, `workflow.py`, `ontology/`, `runtime/`, `trajectory/`, `trigger/`, `evaluation/`, `evolution/`, `validate.py`, `visualization/` and package entry points | Inspected project workflow, store save/load/publish, semantic loading/manifest, MCP dispatch and operations, trajectory persistence, trigger, evaluation aggregation, candidate publication gate, validation entry and explorer version loading. Other model/schema, retrieval, preview and rendering internals remain available for later inspection. |
| `plugins/` | Included: both marketplace plugin manifests, MCP configurations, launchers, bundled cores, Build/Evolve/Explore skills and references; Codex `AGENTS.md`; Claude Code hook and evaluation/trajectory/versioning docs | Inspected launchers/configuration, Codex host instructions and three skills, Claude evolution skill and reminder hook, and Codex workload/interaction/data-boundary references. Read-only byte comparison found all 28 root core files identical to each bundled core; this supports using root implementation anchors for those copies, not assumed prompt parity. Remaining manifests, support references, platform launcher and plugin-specific docs are not yet inspected. Plugin images are excluded as presentation media; no visual-asset assessment. |
| `pyproject.toml` | Included; inspected | Package boundary, optional dependencies and `evoontology-validate` console entry point. |
| `scripts/` | Included: `sync_plugin_core.py`; inspected | Root-to-plugin packaging maintenance. Read source only; did not run synchronization. |
| `tests/` | Included: storage, runtime/MCP, trajectories, trigger, evaluation, evolution, workflow, workspace, plugin/skill parity, visualization and validation tests | Inspected plugin-sync test source and searched workflow/MCP/evolution test declarations. Remaining assertions are not yet inspected. Tests are design/check evidence only; none were executed, so no passing-test claim. |

### Frozen evidence and external limits

The sole frozen source is the acquired Git checkout at **c94389b764394379086ff25e50d0e0f4396167b4**. HEAD matches that pin, and the working tree status was clean when inspected. The applicability cutoff is **2026-10-13**, the supplied run date; it does not imply observation of deployments through that date. No other repository, live page, paper, dataset, execution trace or experimental capture is admitted.

The evidence tier is **code-grounded**. Executable source establishes inspectable behavior; shipped skills and documentation establish declared responsibilities. README performance figures supply **reported operation** only. The run has no observed target execution or causal experiment.

External dependencies are the Claude Code/Codex hosts, user-project data and native tools, model-provider services, benchmark datasets, optional benchmark Python dependencies, and the browser or desktop panel used for presentation. Their implementations and live behavior are excluded. This prevents conclusions about host compliance with skills, actual service reliability, data-grounding correctness, end-to-end task success and browser delivery. Shipped benchmark agents, provider wrappers, evaluators and plugin launchers are included, but the external services they call are not (SRC-1, `plugins/evoontology-codex/AGENTS.md`, `pyproject.toml`, `benchmarks/bird/evolution_adapter.py`, `benchmarks/ddr_10k/evolution_adapter.py`, `benchmarks/insightbench/evolution_adapter.py`).

The core's aggregation and publication checks do not by themselves establish that supplied evaluation observations are authentic or independent. The model-facing instructions require independent validation, while the inspected publication code consumes recorded gate inputs. This boundary supports later analysis of that division of responsibility, not a claim that prompt requirements were obeyed in a real run (SRC-1, `evoontology/evolution/session.py`, `evoontology/evaluation/evaluation.py`, `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`).

> Use the frozen independent
> validation protocol; generated numbers or public training replays are not valid
> evaluation evidence. Historical runs are not silently granted a passing gate.
> --- `plugins/evoontology-codex/skills/evolve-ontology/SKILL.md`

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/ruc-datalab/EvoOntology` | c94389b764394379086ff25e50d0e0f4396167b4 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/evoontology-f2d0c7992c6e/related-systems/ruc-datalab--EvoOntology`. Implementation: tracked tree, packaging, plugin launch/dispatch, root core persistence/consumption/admission, all benchmark adapters and selected agent/evaluation/recording paths; root/plugin core byte comparison. Doctrine/design: `README.md`, `docs/architecture.md`, Codex host instructions and Build/Evolve/Explore skills, Claude Evolve skill, Codex interaction/workload/data-boundary references and plugin-sync test source. Reported operation: README benchmark table and its stated analysis-subset conditions. | Implementation: [MCP server](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/evoontology/runtime/mcp_server.py), [project workflow](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/evoontology/workflow.py), [evolution session](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/evoontology/evolution/session.py), [benchmark registry](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/benchmarks/registry.py). Doctrine/design: [architecture](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/docs/architecture.md), [Codex instructions](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/plugins/evoontology-codex/AGENTS.md), [evolution skill](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/plugins/evoontology-codex/skills/evolve-ontology/SKILL.md). Reported operation: [README performance section](https://github.com/ruc-datalab/EvoOntology/blob/c94389b764394379086ff25e50d0e0f4396167b4/README.md). | No access gap in the frozen tracked checkout was encountered. External hosts, datasets, services and paper are outside this source. No frozen run artifacts or intervention comparisons were supplied; reported performance cannot establish reproduced operation or causal improvement. Uninspected available files are identified in coverage, not classified as inaccessible. |
