---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "CrewAI's shipped agent orchestration, memory, knowledge and Flow paths at commit 3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8."
run-id: AAS-2026-10-15-crewai-62e53db969a7-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/crewAIInc/crewAI
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-crewai-memory/related-systems/crewAIInc--crewAI
  revision: "3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8"
  sha256: null
---

# CrewAI boundary

## Boundary and evidence

This run examines the shipped CrewAI framework, including its memory and knowledge mechanisms in their actual callers. Its intended use is to establish how the framework produces, retains, maintains and later consumes agent context, without reducing the target to the standalone `Memory` API. CrewAI is an **enclosing runtime**: it dispatches crew tasks and owns agent model/tool execution, while also exposing standalone agents, memory and programmable Flows. The boundary is **whole-system** for the open-source framework at the frozen commit, not for CrewAI's separately operated hosted platform. The applicability cutoff is **2026-10-15**. The overall evidence tier is **code-grounded**; no target execution, provider calls or tests were performed.

The source checkout's HEAD matched the acquired full commit, and its Git status was clean on inspection. All source evidence is restricted to SRC-1 at that commit. Later releases, live documentation and external repositories are not evidence for this run.

### Entry points and retained-state loop

The distribution exposes the CLI through `crewai_cli.cli:crewai` (SRC-1, `lib/crewai/pyproject.toml`). The public Python exports include Agent, Crew, Task, Flow, Knowledge and a lazy Memory export (SRC-1, `lib/crewai/src/crewai/__init__.py`). CLI dispatch is not an excluded host: `run_crew` routes declarative crews, declarative Flows and classic Python projects, while the shipped crew template calls kickoff, training, replay and evaluation APIs (SRC-1, `lib/cli/src/crewai_cli/run_crew.py`, `lib/cli/src/crewai_cli/templates/crew/main.py`). These drivers belong inside the boundary.

Crew kickoff dispatches the configured process, and its task loop supplies prior outputs as context to task execution (SRC-1, `lib/crewai/src/crewai/crew.py`). The executor selects native tool calling or the ReAct loop and invokes the configured LLM (SRC-1, `lib/crewai/src/crewai/agents/crew_agent_executor.py`). These responsibilities support the runtime classification rather than a classification as a returning computation or runtime client.

> if self.process == Process.sequential:
>     result = self._run_sequential_process()
> elif self.process == Process.hierarchical:
>     result = self._run_hierarchical_process()
> --- `lib/crewai/src/crewai/crew.py`

> if use_native_tools:
>     return self._invoke_loop_native_tools()
>
> return self._invoke_loop_react()
> --- `lib/crewai/src/crewai/agents/crew_agent_executor.py`

Memory coverage includes both production and later consumption. Task execution recalls against the task description and appends formatted results to the task prompt. The executor extracts memories from the task, agent, expected result and output, then submits extracted statements for retention (SRC-1, `lib/crewai/src/crewai/agent/core.py`, `lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py`). Standalone Agent kickoff has its own recall and output-save paths in `lib/crewai/src/crewai/agent/core.py`; it is not treated as an external application.

> query = task.description
> matches = unified_memory.recall(query, limit=5)
> --- `lib/crewai/src/crewai/agent/core.py`

The retention boundary includes encoding, consolidation, storage reopening, retrieval, scoped access, explicit memory tools and reset paths. `Memory.remember` enters the serialized save pipeline; encoding can delete, update and insert records; recall waits for pending saves and selects shallow search or RecallFlow. LanceDB storage opens an existing table when available. Agents also receive Search memory and Save to memory tools. These are shipped maintenance and consumption paths, not merely examples (SRC-1, `lib/crewai/src/crewai/memory/unified_memory.py`, `lib/crewai/src/crewai/memory/encoding_flow.py`, `lib/crewai/src/crewai/memory/storage/lancedb_storage.py`, `lib/crewai/src/crewai/tools/memory_tools.py`).

> # Read barrier: wait for any pending background saves to finish
> # so that the search sees all persisted records.
> self.drain_writes()
> --- `lib/crewai/src/crewai/memory/unified_memory.py`

The boundary also includes knowledge-source ingestion and search, training artifacts consumed by later prompts, Flow state persistence and reload, and human-feedback lessons. These are distinct retained-state paths, not all interchangeable with unified memory. Knowledge assigns storage to its sources and queries that storage. Crew training saves evaluated suggestions, while agent prompt preparation applies training data. Flow runtime reloads persisted state by UUID; SQLite persistence saves and retrieves state snapshots. Human-feedback handling distills lessons into memory and recalls them to revise later outputs (SRC-1, `lib/crewai/src/crewai/knowledge/knowledge.py`, `lib/crewai/src/crewai/crew.py`, `lib/crewai/src/crewai/agent/utils.py`, `lib/crewai/src/crewai/flow/runtime/__init__.py`, `lib/crewai/src/crewai/flow/persistence/sqlite.py`, `lib/crewai/src/crewai/flow/human_feedback.py`).

Shipped prompts are included as operational evidence: the English translations contain memory extraction, query, save, consolidation and human-feedback prompts, plus the prompt slice used when recalled memories enter task context. Skill loading is also included because it admits instructions into agent context. These files are evidence of the target's contracts, not instructions to the analyst (SRC-1, `lib/crewai/src/crewai/translations/en.json`, `lib/crewai/src/crewai/skills/loader.py`).

### Repository coverage

The table accounts for every top-level tracked entry. “Included” denotes the functional evidence boundary, not a claim that every file has already been read. Initial inspection traced the material entry points and state loops above; deeper implementation inspection remains available throughout SRC-1. Uninspected files are not access gaps. Tests and evaluators are included as source evidence, not as observed successful runs.

| Top-level entry / material paths | Classification and role | Initial coverage or exclusion limit |
|---|---|---|
| `lib/crewai/` | Included: runtime, agent execution, tools, model adapters, memory, knowledge, Flow, checkpoints, hooks, events and telemetry; tests and compatibility entry surfaces. | Traced public exports, Crew kickoff/task execution/train/test/reset, Agent task and standalone memory use, executor/save path, memory encoding/recall/storage, knowledge ingestion/search, Flow reload/persistence and feedback learning. Inspected memory tests and task evaluator source. Anchors are the paths cited above and SRC-1 `lib/crewai/tests/memory/test_unified_memory.py`, `lib/crewai/src/crewai/utilities/evaluators/task_evaluator.py`, `lib/crewai/src/crewai/utilities/reset_memories.py`. |
| `lib/cli/` | Included: user entry point, project selection, templates, supplied prompts/instructions, replay/training/evaluation/reset drivers. | Inspected CLI command definitions, run routing, reset wrapper and crew template main. Includes generated-application scaffolds rather than excluding them as callers. SRC-1 `lib/cli/src/crewai_cli/cli.py`, `lib/cli/src/crewai_cli/run_crew.py`, `lib/cli/src/crewai_cli/reset_memories_command.py`, `lib/cli/src/crewai_cli/templates/crew/main.py`. |
| `lib/crewai-core/` | Included: shared storage-path, locking, settings, auth and platform-client support. | Inspected storage-path resolution used by memory. SRC-1 `lib/crewai-core/src/crewai_core/paths.py`. Other helpers remain available for consumer tracing; their external services are not supplied implementations. |
| `lib/crewai-files/` | Included: file inputs, resolution, formatting, upload/cache and cleanup surfaces supporting task context. | Inspected public exports and the shipped PDF runner's imports/use; not an exclusion of file-mediated context. SRC-1 `lib/crewai-files/src/crewai_files/__init__.py`, `scripts/age90_file_input_runner.py`. |
| `lib/crewai-tools/` | Included: shipped retrieval, file, database, service and agent/tool adapters and their tests. | Inspected exported tool inventory; specific adapter internals remain to be inspected where consequential. SRC-1 `lib/crewai-tools/src/crewai_tools/__init__.py`. Inclusion covers local adapters, not the remote databases or services they call. |
| `lib/devtools/` | Excluded: package release/versioning plane, not the runtime's agent-state loop. | Inspected SRC-1 `lib/devtools/README.md` to distinguish release tooling from agent improvement. Prevents conclusions about release automation, generated release notes and external enterprise-release behavior. |
| `docs/` | Included: source-native doctrine, examples, usage and evaluation guidance; Edge and frozen-version documentation remain distinguishable. | Initially inspected SRC-1 `docs/edge/en/concepts/memory.mdx`; do not project its claims onto every archived version or language. Other documentation is available but not yet inspected. No live hosted documentation is registered. |
| `scripts/` | Included for shipped runtime callers and manual evaluators; excluded for documentation-freezing/catalog-generation maintenance. | Inspected SRC-1 `scripts/age90_file_input_runner.py` and `scripts/wharf_runner.py`: file-input and standalone-agent/Flow/MCP/tracing drivers. `scripts/docs/` and `scripts/update_litellm_catalog.py` are maintenance, not evidence of agent-run outcomes; exclusion prevents claims about documentation publication and catalog-generation correctness. |
| `README.md` | Included: framework introduction and shipped usage documentation. | Present in tracked tree; not initially read. No claim here relies on it. |
| `pyproject.toml`, `uv.lock`, `.python-version` | Included: workspace, package/dependency and interpreter boundary. | Inspected workspace/package metadata; lockfile and interpreter file not initially read. Dependency implementations are not thereby frozen as source. SRC-1 `pyproject.toml`, `lib/crewai/pyproject.toml`. |
| `conftest.py`, `.env.test` | Included: repository test setup, not runtime success evidence. | Not initially read; test-environment details cannot yet support a finding. SRC-1 `conftest.py`, `.env.test`. |
| `.github/` | Excluded: CI, issue/review and security-administration configuration. | Tracked workflow/template inventory inspected, not workflow bodies. Prevents conclusions about CI success, security scanning results and publishing operation. |
| `AGENTS.md`, `DOCS_TRANSLATIONS.md` | Excluded: repository contributor and translation procedures. | Not initially read. Prevents conclusions about contributor-agent or translation workflows; does not exclude runtime prompts or template instructions under `lib/`. |
| `.editorconfig`, `.gitignore`, `.pre-commit-config.yaml` | Excluded: editor, source-control and contributor checks. | Prevents conclusions about contributor-check enforcement, ignored local artifacts and development formatting behavior. |
| `LICENSE` | Excluded from mechanism analysis: legal terms. | Prevents licensing conclusions. |

### External dependencies and evidence limits

The package metadata declares model SDKs, embedding/vector-storage libraries, MCP support and optional provider integrations (SRC-1, `lib/crewai/pyproject.toml`). Their implementations and hosted behavior are not frozen by this repository pin. The framework's adapters, delegation boundaries and error handling remain in scope; remote model quality, service availability and provider-side storage/security guarantees do not. User-authored downstream crews, datasets, deployed services and proprietary CrewAI platform implementations are excluded. This prevents attributing host policy, application success or hosted persistence guarantees to the open-source runtime.

There is no supplied observed-run or causal-experiment evidence. Test source, evaluators and manual runners can establish intended checks and executable paths, but not passing results, reliable recall, improved task quality, latency, cost or effects of an intervention. No inspected material path was inaccessible; the principal access limit is implementation outside SRC-1. Initial sampling is not a license to describe uninspected mechanisms as established behavior.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/crewAIInc/crewAI` | 3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-crewai-memory/related-systems/crewAIInc--crewAI`. Implementation: package/export surfaces; CLI routing/template callers; Crew and Agent execution, memory production/consumption; memory API, encoding and LanceDB reopening; knowledge API; Flow state reload/SQLite persistence and feedback learning; memory tools, skill loader, reset utilities, training/evaluation source and memory tests. Doctrine/design: Edge English memory guide, runtime translation prompts, devtools release-tool description, runner descriptions. The coverage table records exact initial paths; the registered source is the entire repository at this commit, not that initial subset. | Implementation: [package and CLI entry](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/lib/crewai/pyproject.toml), [Crew runtime](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/lib/crewai/src/crewai/crew.py), [Agent consumers](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/lib/crewai/src/crewai/agent/core.py), [Memory](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/lib/crewai/src/crewai/memory/unified_memory.py), [Flow runtime](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/lib/crewai/src/crewai/flow/runtime/__init__.py). Doctrine/design: [memory guide](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/docs/edge/en/concepts/memory.mdx), [shipped prompts](https://github.com/crewAIInc/crewAI/blob/3da2d4e9932b5f2fa9aa73ea9245e0f8b5c154f8/lib/crewai/src/crewai/translations/en.json). Additional local anchors appear above. | No observed run or causal experiment supplied; test and runner source does not establish successful operation or improvement. External model/embedding/storage dependencies and hosted/proprietary services lack frozen implementation evidence; their correctness, availability, deployment policy and empirical effects cannot be concluded. Documentation supplies declared contracts, not verified outcomes. |
