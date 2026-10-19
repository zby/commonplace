---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Autogenesis's shipped multi-agent runtime, capability evolution, retained state and clients at commit 5b070d5cd497e951a188a01409138e8b530eaf4a."
run-id: AAS-2026-10-19-autogenesis-05936a4e4c3b-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "5b070d5cd497e951a188a01409138e8b530eaf4a"
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/DVampire/Autogenesis
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-autogenesis/related-systems/DVampire--Autogenesis
  revision: 5b070d5cd497e951a188a01409138e8b530eaf4a
  sha256: null
---

# Autogenesis boundary

## Boundary and evidence

This run analyses Autogenesis as an enclosing multi-agent runtime, including its capability-generation and improvement plane, memory and context assembly, workflow execution, durable project state, and shipped clients. The intended use is to establish how its components operate together, not to treat its memory API or evolution playbook as a standalone product. The boundary is whole-system at the registered repository revision. It includes both the Gateway path and directly bootstrapped Python example drivers; neither is an external host.

The frozen evidence is SRC-1 at `5b070d5cd497e951a188a01409138e8b530eaf4a`, with an applicability cutoff of 2026-10-19. HEAD matched that revision and the tracked working tree had no diff against it during boundary inspection. The overall tier is code-grounded: executable source supplies implementation evidence; bundled prompts, skills and module documentation supply doctrine/design evidence. No target code, tests or examples were executed. Test definitions are inspectable implementation evidence, not observed passing runs. This boundary establishes neither production reliability nor measured improvement from self-evolution.

### Classification and loop coverage

Autogenesis issues model calls and owns agent execution rather than merely returning a tool result to an excluded runtime. The installed console entry resolves to `autogenesis.cli:main` (SRC-1, `pyproject.toml`). That console starts or calls the Gateway, whose startup initializes capability managers, starts task workers and restores sessions (SRC-1, `autogenesis/cli.py`, `autogenesis/gateway/service.py`). The runtime itself owns spawned agent references and message handling (SRC-1, `autogenesis/runtime/server.py`).

> """One-shot: spawn + ask(TaskMessage) + stop.  Returns agent's result."""
> --- `autogenesis/runtime/server.py`

The agent's decision path streams a configured model with assembled messages and native capability schemas; source inspection is sufficient to classify the system as model-dependent, without assuming a successful provider call (SRC-1, `autogenesis/agent/types.py`).

> acc = await accumulate_stream(
>     model_manager.stream(
>         name=self.model_name,
>         input={"messages": messages, "tools": tools},
>         ctx=ctx,
>     )
> )
> --- `autogenesis/agent/types.py`

The functional boundary includes state producers, maintainers, admission paths and subsequent consumers. Lifecycle hooks emit events into primary memory and a file-system sink; tiered memory renders and persists session state; agent context assembly reads the selected memory for prompt injection. This traces a shipped producer-to-consumer path, but does not establish that persisted tiered memory is rehydrated after process restart (SRC-1, `autogenesis/hook/default/memory.py`, `autogenesis/memory/default/tiered.py`, `autogenesis/agent/types.py`). Conversation persistence and transcript replay are distinct retained-state paths, not evidence that every memory backend reloads (SRC-1, `autogenesis/conversation/server.py`, `autogenesis/gateway/service.py`, `frontend/src/App.tsx`).

> mem_text = await memory_info.instance.get(
>     session_id=session_id,
>     short_term_n=self.review_steps,
> )
> --- `autogenesis/agent/types.py`

Capability evolution is also inside the boundary: generators, optimizers, evaluators, their prompts and creator skills, registration hooks, staging/promotion, extension manifests, smoke checks, archived versions and rollback controls. An inspected skill registration path promotes a staged directory and registers it as evolvable; extension registration exposes a smoke-gate/revert path (SRC-1, `autogenesis/hook/default/skill_registration.py`, `autogenesis/hook/promotion.py`, `autogenesis/extension/server.py`). These mechanisms must be distinguished from the playbook's register-is-live claims. The playbook is design evidence, not proof that all contemporary admission paths lack staging or validation (SRC-1, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`).

> name = await extension_manager.add_component("skill", skill_dir, config={"enable_evolving": True})
> --- `autogenesis/hook/default/skill_registration.py`

Workflow and canvas callers remain included. The workflow runtime invokes the same capability managers and has checkpoint/resume paths; Gateway endpoints save, run and reopen canvas flows. Python examples likewise submit tasks through shipped task and agent managers rather than constituting excluded enclosing applications (SRC-1, `autogenesis/workflow/runtime.py`, `autogenesis/canvas/server.py`, `autogenesis/gateway/service.py`, `examples/run_general_agent.py`).

### Top-level coverage

Every top-level tracked entry is classified below. Included means part of the analysis's functional/evidence scope, not a claim that every file has already been read. “Not yet inspected” names available material, not an access gap. All path references in this table refer to SRC-1.

| Top-level entry | Status and material paths | Role, inspection extent and limit |
|---|---|---|
| `.dockerignore` | Included; not yet inspected | Packaging exclusions; no container-content claim established here. |
| `.gitignore` | Included; not yet inspected | Generated/local state exclusions; no inference that ignored artifacts were captured. |
| `LICENSE` | Included; not yet inspected | Distribution terms; not used to establish runtime behavior. |
| `PROJECT.md` | Included; not yet inspected | Project-authored design context; no claims drawn from it here. |
| `README.md` | Included; not yet inspected | User-facing intent and setup; implementation takes precedence for behavior. |
| `README_zh.md` | Included; not yet inspected | Additional project documentation; no independent operational corroboration assumed. |
| `autogenesis/` | Included: `cli.py`, `gateway/`, `runtime/`, `agent/`, `protocol/`, `task/`, `session/`, `conversation/`, `paths/`, `config/`, `registry.py`; `memory/`, `prompt/`, `hook/`, `extension/`, `version/`; `workflow/`, `canvas/`; `tool/`, `skill/`, `connector/`, `environment/`, `model/`, `permission/`, `constraint/`; `data/`, `process/`, `knowledge/`, `benchmark/`; sandbox/deployment, science/kernel, IDE, trace/trajectory, plugins and supporting modules | Primary implementation and resources. Initial inspection traced console/Gateway startup, runtime lifecycle, model decision and memory context assembly; lifecycle-memory hook and tiered get/persist; conversation save/read; skill registration and promotion; extension admission/rollback searches; workflow invocation/checkpoint and canvas facade searches; task persistence and knowledge API searches. Bundled meta-agent prompt, self-evolution skill, memory evaluator and module documentation were also inspected. Other handlers, provider adapters, domain skills and support modules remain available for later inspection, not excluded responsibilities. |
| `configs/` | Included: `base.py`, agent and tool configs, `memory/`, benchmark configs and top-level driver configs | Shipped capability wiring and model roles. `base.py` inspected; specific rosters and overrides not yet inspected. Their presence must not be inferred from an agent class alone. |
| `datasets/` | Included as evaluation inputs: AIME, ESG, GPQA, GSM8K and dataset gitlink declarations; contents not yet inspected | Evaluation task data, not run results. The Git-linked HLE and LeetCode repository contents are outside SRC-1; no dataset completeness or benchmark accuracy claim follows from their gitlink pins. |
| `docker/` | Included: `base/`, `chrome-vnc/`, `vscode/` Dockerfiles and entrypoints; not yet inspected | Shipped sandbox environments and launch support; no isolation or reproducibility conclusion established here. |
| `docs/` | Included: `canvas.md`, `workflows.md`, `capability-schemas.md`, site and assets; not yet inspected | Source-native design documentation; not separate evidence of deployed operation. |
| `examples/` | Included: `run_general_agent.py`, other actor/generator/optimizer/evaluator drivers, `run_hle.py`, `run_programbench.py`, task documents | `run_general_agent.py` inspected through setup, task submission, manager invocation and teardown. Other drivers/tasks remain available, not external hosts. No example execution outcome asserted. |
| `extension/` | Included: sample agents, memory backends, prompt, tools, maze environment and canvas documentation; not yet inspected | Shipped extension examples and potential state consumers; not actual generated artifacts from an observed run. |
| `frontend/` | Included: web `src/App.tsx`, controller, canvas/IDE/science/workspace views; terminal `src/cli/` and Gateway clients; proxy and build config | Package scripts inspected; bounded searches traced browser task submission and conversation reload, and terminal stdio backend launch. View internals remain available for later inspection. Both interfaces are shipped consumers, not excluded hosts. |
| `libs/` | Excluded: `AgentOS`, `EvoAgentX`, `browser-use`, `textgrad` gitlinks and `BinanceDatabase/` vendored material | Adjacent external libraries/experiments, not additional frozen repository sources. Tree and gitlink identities inspected, contents not analysed. Prevents conclusions about their internal execution, learning methods or guarantees; Autogenesis integration code remains included. |
| `pyproject.toml` | Included; inspected | Python entry point, dependencies and package-resource/config shipping. |
| `scripts/` | Included: install scripts, `run-in-sandbox.sh`, `serve-ui.sh`, supporting setup utilities; not yet inspected | Deployment and launch wiring; no installation success claim. |
| `tests/` | Included: runtime, Gateway, workflow, permissions, sandbox, capability and data-pipeline suites | Bounded searches inspected runtime lifecycle and Gateway persistence/replay assertions; other test bodies not yet inspected. Tests remain source evidence only; none were run. |
| `uv.lock` | Included; not yet inspected | Dependency resolution record, not a frozen installed environment or evidence of dependency behavior. |

### External dependencies and evidence limits

Provider implementations, network services, credentials, MCP server deployments, browser/container engines and installed dependency internals are not frozen by this run. Autogenesis's adapters, permission checks, configuration and launch code remain included. These external limits prevent conclusions about actual model quality, remote service availability, deployment security, tool success and reproducible end-to-end performance. Dependencies and optional browser/sandbox/benchmark integrations are declared in SRC-1, `pyproject.toml`; adapters and connectors are present in the tracked tree.

No execution traces or experimental results were separately supplied or frozen. The register therefore contains no observed-run or causal-experiment layer. A comparison probe prescribed by a skill or an evaluator class is not evidence that an intervention helped. Unread tracked files remain accessible within SRC-1; they are not missing evidence or permission to substitute another revision.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/DVampire/Autogenesis` | 5b070d5cd497e951a188a01409138e8b530eaf4a | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-autogenesis/related-systems/DVampire--Autogenesis`. Implementation: tracked tree and Git pin; `pyproject.toml`, `autogenesis/cli.py`, `autogenesis/runtime/server.py`, relevant ranges of `autogenesis/gateway/service.py` and `autogenesis/agent/types.py`, `examples/run_general_agent.py`, `autogenesis/conversation/server.py`, `autogenesis/hook/default/memory.py`, `autogenesis/memory/default/tiered.py`, `autogenesis/hook/default/skill_registration.py`, `autogenesis/hook/promotion.py`, `autogenesis/agent/evaluator/memory_evaluate_agent.py`, `configs/base.py`, `frontend/package.json`; bounded searches of extension, evolution tool, workflow, canvas, task, knowledge, version, frontend clients and runtime/Gateway tests. Doctrine/design: `autogenesis/README.md`, `autogenesis/memory/README.md`, `autogenesis/extension/README.md`, `autogenesis/workflow/README.md`, `autogenesis/prompt/default/meta_agent.html`, `autogenesis/skill/creator/self_evolving_skill/SKILL.md`. | Implementation: [console](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/cli.py), [agent loop](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/agent/types.py), [extension admission](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/extension/server.py). Doctrine/design: [meta-agent prompt](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/prompt/default/meta_agent.html), [evolution playbook](https://github.com/DVampire/Autogenesis/blob/5b070d5cd497e951a188a01409138e8b530eaf4a/autogenesis/skill/creator/self_evolving_skill/SKILL.md). | No access gap in the registered repository source. Separate gitlink contents, dependency/service internals and live runtime state are not frozen. No supplied execution or intervention evidence: prevents observed-reliability and causal-improvement conclusions. Partial initial inspection is distinguished from access failure in the coverage table. |
