---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Autogenesis's shipped multi-agent runtime and capability-improvement paths at frozen commit 5b070d5cd497e951a188a01409138e8b530eaf4a."
run-id: AAS-2026-10-15-autogenesis-9bcfa57fd7c1-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/DVampire/Autogenesis
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autogenesis/related-systems/DVampire--Autogenesis
  revision: 5b070d5cd497e951a188a01409138e8b530eaf4a
  sha256: null
---

# Autogenesis boundary

## Boundary and evidence

Autogenesis is in scope as an **enclosing runtime**: it owns agent execution, issues model calls, dispatches capabilities, and serves user tasks through shipped drivers and interfaces. Its intended use is task completion through a MetaAgent and other actors, with generator, optimizer and evaluator agents for changing the capability ecosystem. The improvement plane is part of this target, not a separate external application. This is a **whole-system** functional boundary over the shipped Autogenesis implementation at the reviewed commit, including its direct example drivers, Gateway, browser/terminal clients, retained state and extension lifecycle. It is not a boundary around only the `runtime` Python module or only the MetaAgent API. SRC-1: `README.md`, `pyproject.toml`, `autogenesis/cli.py`, `examples/run_meta_agent.py`, `autogenesis/agent/types.py`, `autogenesis/extension/server.py`.

The classification rests on executable ownership, not the project description alone. Runtime spawning creates and registers an agent pump (SRC-1: `autogenesis/runtime/server.py`):

> ref = AgentRef(name=ref_name, agent_name=agent_name, status=AgentStatus.RUNNING)
> ref._pump_task = asyncio.create_task(_pump(agent, ref), name=f"pump-{ref_name}")
>
> self._refs[ref_name] = ref
> --- `autogenesis/runtime/server.py`

The agent decision path streams a model with messages and callable capabilities (SRC-1: `autogenesis/agent/types.py`):

> model_manager.stream(
>     name=self.model_name,
>     input={"messages": messages, "tools": tools},
>     ctx=ctx,
> )
> --- `autogenesis/agent/types.py`

### Entry points and state-loop coverage

The installed console entry is `autogenesis.cli:main`. Its command and terminal modes create an in-process Gateway; serve mode exposes the Gateway through stdio or WebSocket transport. Gateway startup initializes capability managers, extensions, task workers and restored sessions. The direct MetaAgent example instead bootstraps managers itself, binds session roots, installs a TaskManager handler and invokes `agent_manager`. That shipped caller is included even though it bypasses the Gateway. SRC-1: `pyproject.toml`, `autogenesis/cli.py`, `autogenesis/gateway/service.py`, `examples/run_meta_agent.py`.

The inspected state loop includes creation and consumption of per-session memory, persisted conversations and sessions, workflow checkpoint recovery, persisted knowledge corpora, and reusable extension admission. These are distinct stores; writing a memory report does not by itself establish that a restarted agent reloads it. The inspected tiered-memory `get` reads an in-process session registry, whereas Gateway session recovery reads manifests and knowledge retrieval rereads corpus JSONL. Later analysis must distinguish those paths rather than generalize persistence into universal restart recovery. SRC-1: `autogenesis/memory/default/tiered.py`, `autogenesis/agent/types.py`, `autogenesis/gateway/service.py`, `autogenesis/knowledge/server.py`, `autogenesis/workflow/runtime.py`.

The extension consumer is inside the target. Startup reloads the active extension manifest, and the Gateway promotion handler registers promoted components through `add_component`. The inspected implementation archives versions, writes the manifest and can revert after a failed smoke probe. Shipped evolution instructions and prompt text are also included as declared policy; they are not assumed to be identical to enforcement. In particular, the self-evolution playbook describes register-is-live behavior, while the MetaAgent prompt also describes session staging and user-approved promotion. This boundary retains both surfaces so later jobs can trace their respective callers rather than silently choose one description. SRC-1: `autogenesis/extension/server.py`, `autogenesis/gateway/service.py`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`, `autogenesis/prompt/default/meta_agent.html`.

The reusable-state reload responsibility is explicit in the extension implementation:

> await self._load_component(comp.module, abspath, comp.name, version=comp.version, config=None)
> self._ensure_archived(comp.module, comp.name, abspath, comp.version)
> loaded.append(comp)
> --- `autogenesis/extension/server.py`

Evaluation is included on three different surfaces: model-driven evaluator agents, benchmark adapters and smoke-probe admission checks, plus repository regression tests as executable specifications. None of these source files is an observed successful run. The default smoke probe calls a general-purpose agent on a synthetic completion task; its presence does not establish that an evolved capability is actually exercised or improves task quality. SRC-1: `autogenesis/agent/evaluator/agent_evaluate_agent.py`, `autogenesis/benchmark/server.py`, `autogenesis/extension/smoke_gate.py`, `tests/test_runtime.py`.

### Repository coverage

The tracked root tree was enumerated at the pinned commit. “Included” below specifies analytical responsibility, not a claim that every implementation file was read during boundary declaration. Initial inspection traced the material entry, state production, admission, reload and consumption paths above. Uninspected leaf implementations remain available within SRC-1; they are not access gaps and cannot support detailed conclusions until inspected.

| Top-level tracked entry | Treatment | Material paths and role | Inspection status and limits |
|---|---|---|---|
| `.dockerignore` | Included, packaging context | Container build-context filtering. | Enumerated; contents not yet inspected. No conclusion about exact image exclusions. |
| `.gitignore` | Included, repository context | Generated-state tracking exclusions. | Enumerated; contents not yet inspected. No conclusion about completeness of committed run evidence from ignore rules. |
| `LICENSE` | Included, distribution context | Project licensing declaration. | Enumerated; not used to assess runtime behavior or third-party license compliance. |
| `PROJECT.md` | Included, project doctrine | Repository-local development and project instructions. | Enumerated, not yet inspected; not treated as executed behavior. |
| `README.md` | Included | Installation, MetaAgent driver, UI entry and output/extension layout. | Read; doctrine/design only. |
| `README_zh.md` | Included | Alternative-language project documentation. | Enumerated, not yet inspected; no claim of agreement with the English document. |
| `autogenesis/` | Included, core implementation and bundled doctrine | `cli.py`; `gateway/service.py`; `agent/server.py`, `agent/types.py`, actor/generator/optimizer/evaluator classes; `runtime/server.py` and `pump.py`; `protocol/`, `task/`, `workflow/`, `canvas/`; `prompt/default/`, `prompt/module/`, `skill/creator/`; `hook/default/memory.py`, registration hooks and `hook/promotion.py`; `memory/default/tiered.py`, memory renderers, `knowledge/server.py`; `extension/server.py`, `extension/smoke_gate.py`, `version/`; `model/`, `tool/`, `connector/`, `plugins/`, `environment/`, `sandbox/`, `session/`, `paths/`, `conversation/`, `trace/`, `trajectory/`, `permission/`, `constraint/`; deployment, IDE, kernel and science services. | Executable entry/model/runtime, memory consumption/persistence, Gateway restoration/promotion, extension reload/admission, workflow resume and knowledge ingest/retrieve inspected. Tree and bounded symbol searches identify supporting managers. MetaAgent prompt and self-evolution playbook inspected as doctrine; other bundled prompts, skills, provider integrations and service internals await mechanism-specific inspection. |
| `configs/` | Included, shipped assembly | `base.py`, `meta_agent.py`, `agents/meta_agent.py`, actor/evaluator/generator/optimizer configurations, `memory/`, `tools/`, `benchmarks/`. | Tree inspected; `agents/meta_agent.py` read, establishing a configured memory/model/prompt consumer. Other assemblies remain available, not assumed equivalent. |
| `datasets/` | Included for shipped evaluator inputs and metadata; nested Git repositories excluded | AIME, GPQA, GSM8K and ESG fixtures; `hle` and `leetcode` are Gitlinks. | Tree inspected, payloads not read. No benchmark-quality or score conclusions. Gitlink contents are not frozen blobs of this source; no conclusions about their dataset construction or full contents. |
| `docker/` | Included, shipped execution environment | `base/Dockerfile`, `base/entrypoint.sh`, `chrome-vnc/`, `vscode/`. | Base Dockerfile inspected through framework-install context; remaining image and entrypoint details await inspection. Build text does not establish a deployed image or isolation strength. |
| `docs/` | Included, design/user documentation | `canvas.md`, `workflows.md`, `capability-schemas.md`, `index.html`, architecture assets. | Tree inspected; contents not yet used as evidence. No claim that diagrams match implementation. |
| `examples/` | Included, shipped callers and evaluator drivers | `run_meta_agent.py`; actor/generate/optimize/evaluate drivers; `run_hle.py`, `run_programbench.py`; `tasks/` inputs. | MetaAgent driver read; evaluator driver searched to its agent invocation and TaskManager handler. Other drivers/inputs await detailed inspection. Their runtime/state responsibilities are not excluded as external hosts. |
| `extension/` | Included, shipped reusable components | `agent/gaia_answer_agent.py`, `prompt/gaia_answer_agent.html`, `memory/file_system_memory.py`, `memory/constraint_memory.py`, `environment/grid_maze_environment/`, `tool/`, `canvas/README.md`. | Tree inspected and file-system memory renderer inspected. Startup consumption traced through ExtensionManager. No assertion that bundled extension examples were successfully loaded in a live run. |
| `frontend/` | Included, shipped state consumers and task clients | `src/controllers/gateway.ts`, `src/cli/`, `src/science/Conversation.tsx`, `src/canvas/index.tsx`, workspace, IDE and VNC views; package/build files and container proxy. | README read; bounded searches traced session-event replay, task submission and canvas list/save/get/run requests. Full rendering, client-side state and transport implementation not yet inspected. |
| `libs/` | Excluded third-party/reference implementations | Gitlinks `AgentOS`, `EvoAgentX`, `browser-use`, `textgrad`; tracked `BinanceDatabase/` utilities and tests. | Tree/Gitlink entries inspected. Bounded search of Python/shell/build files under `autogenesis`, `configs`, `examples`, `scripts` and `pyproject.toml` found no references to `libs`, `BinanceDatabase`, `AgentOS`, `EvoAgentX` or `textgrad`. This is not proof of universal non-use. No internals or performance claims about those projects; shipped adapters remain included. A material runtime dependency discovered here must be surfaced rather than silently expanding the source. |
| `pyproject.toml` | Included | Package boundary, Python console entry, dependencies, package resources, bundled configs and test configuration. | Read. Dependency declarations establish requirements, not installed versions or service availability. |
| `scripts/` | Included, shipped launch/install integration | `run-in-sandbox.sh`, `serve-ui.sh`, install scripts, plugin/icon helpers. | `serve-ui.sh` read, tracing Gateway and Vite startup. Other scripts enumerated; no claim of successful installation or sandbox launch. |
| `tests/` | Included, executable contracts | Runtime, Gateway, permissions, project sandbox/promotion, workflow, prompt, capability, science and robustness tests. | Tree inspected; representative runtime tests read. Not executed; assertions are not observed outcomes or complete coverage evidence. |
| `uv.lock` | Included, dependency-lock context | Dependency resolution metadata. | Enumerated, not yet inspected. No inference of the actual deployed environment. |

### Frozen evidence and external dependencies

The sole frozen evidence source is SRC-1 at full commit `5b070d5cd497e951a188a01409138e8b530eaf4a`. The supplied checkout's HEAD matched that pin and its short status was empty. The source object above is unchanged from acquisition. The analysis cutoff is **2026-10-15**, the supplied run date; it does not assert repository completeness after the reviewed commit. No branch tip, live website, second repository, historical analysis or newly executed target output is evidence for this run.

Overall evidence tier is **code-grounded**. Inspected Python, shell and client call sites supply implementation evidence; target READMEs, prompt text and skill instructions supply doctrine/design. No observed-run or causal-experiment source is registered. The target was not executed, installed or tested. Consequently this boundary supports source-level responsibility and mechanism analysis, not claims of real-world success rates, reliable self-improvement, measured retrieval quality, operational security or causal benefit.

External dependencies include model-provider APIs/SDKs, MCP connector services and plugin-backed services, Docker/container and browser infrastructure, Vault or environment-supplied credentials, package dependencies and optional benchmark data. Their shipped adapters, configuration and launch contracts are included; remote internals, credentials, live service responses and separately versioned dependency implementations are excluded. These exclusions prevent conclusions about provider behavior, connector service correctness, actual deployed isolation, credential configuration and dataset availability. Nested Gitlinks do not authorize inspecting another repository under SRC-1. SRC-1: `pyproject.toml`, `README.md`, `autogenesis/gateway/service.py`, `docker/base/Dockerfile`, `scripts/serve-ui.sh`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/DVampire/Autogenesis` | 5b070d5cd497e951a188a01409138e8b530eaf4a | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autogenesis/related-systems/DVampire--Autogenesis`. Implementation: root tracked tree; `pyproject.toml`, `autogenesis/cli.py`, `autogenesis/runtime/server.py`, selected agent decision/context methods in `autogenesis/agent/types.py`; startup, manifests, restore and extension-promotion portions of `autogenesis/gateway/service.py`; extension startup/add/revert in `autogenesis/extension/server.py`; `autogenesis/extension/smoke_gate.py`; event ingestion, prompt retrieval, compaction and persistence portions of `autogenesis/memory/default/tiered.py`; `extension/memory/file_system_memory.py` renderer; knowledge corpus ingest/retrieve; workflow checkpoint resume; `examples/run_meta_agent.py`; `configs/agents/meta_agent.py`; agent evaluator; `scripts/serve-ui.sh`; base Dockerfile context; representative runtime tests. Bounded call-site/symbol searches: agent manager, memory hook, promotion helper, evaluator example, benchmark manager, frontend replay/task/canvas requests and possible `libs` references. Doctrine/design: `README.md`, `frontend/README.md`, `autogenesis/runtime/README.md`, MetaAgent prompt input/project/routing rules and `autogenesis/skill/creator/self_evolving_skill/SKILL.md`. Listed paths describe initial inspection, not an allowlist. | Implementation: [console entry](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/cli.py), [runtime ownership](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/runtime/server.py), [agent context and model calls](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/agent/types.py), [Gateway/state consumers](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/gateway/service.py), [extension lifecycle](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/extension/server.py), [direct driver](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/examples/run_meta_agent.py). Doctrine/design: [project intent](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/README.md), [evolution playbook](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/skill/creator/self_evolving_skill/SKILL.md). | No access gap in the inspected tracked blobs. Nested Gitlink contents, remote dependencies and operational environment are outside this source; they cannot establish implementation internals or successful deployment. No registered execution trace or experiment: no operational-effectiveness or causal-improvement conclusion. Available but uninspected files are identified in coverage, not mislabeled as unavailable evidence. |
