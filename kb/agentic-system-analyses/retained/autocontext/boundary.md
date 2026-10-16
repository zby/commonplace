---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Autocontext's shipped improvement, retained-context and operator surfaces at commit f72c154152397f54d55407508b153d28861888a5."
run-id: AAS-2026-10-15-autocontext-b7f59f8405c4-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: f72c154152397f54d55407508b153d28861888a5
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/greyhaven-ai/autocontext
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autocontext/related-systems/greyhaven-ai--autocontext
  revision: f72c154152397f54d55407508b153d28861888a5
  sha256: null
---

# Autocontext boundary

## Boundary and evidence

This run examines how Autocontext produces, evaluates, retains, admits and later consumes improvements to agent behavior. The target is the shipped repository system, not just its knowledge API, one MCP tool, or the Pi extension. Its primary class is **builder or improvement plane**: it coordinates model-backed attempts and evaluation and retains artifacts for subsequent attempts. It also contains runtime adapters, session orchestration and a memory/context subsystem. Those responsibilities remain included rather than being assigned to an imaginary external caller.

The classification is supported by SRC-1, `README.md`, and by the CLI-to-runner and retained-context paths below. The source describes its intended product as follows:

> autocontext is a harness for agent improvement. Give it a goal, it runs the task against evaluation, keeps the useful lessons, discards dead ends, and leaves traces, reports, playbooks, datasets, and optional local-model training artifacts for the next run.
> --- `README.md`

### Functional boundary and initial loop trace

The whole-system boundary includes the Python `autocontext`, TypeScript `autoctx`, and `pi-autocontext` shipping surfaces. These are the active packages according to SRC-1, `packages/README.md`; the repository's deferred package split is not a separate deployed system.

Initial implementation inspection establishes these connected paths:

- **Entry and execution:** Python's `autoctx` entry point is declared in SRC-1, `autocontext/pyproject.toml`. `autocontext/src/autocontext/cli.py` dispatches saved scenarios to `GenerationRunner` and agent tasks to an improvement loop. `autocontext/src/autocontext/cli_solve.py` and `autocontext/src/autocontext/knowledge/solver.py` supply the plain-language solve route. The SDK delegates to the shared tool implementations rather than constituting an excluded application (`autocontext/src/autocontext/sdk.py`).
- **Retained context into later attempts:** SRC-1, `autocontext/src/autocontext/loop/stages.py`, loads the active context bundle, playbook, tools, skills, prior analysis, trajectory, hints and reports. The generation pipeline connects knowledge setup, agent generation, evaluation, review and persistence (`autocontext/src/autocontext/loop/generation_pipeline.py`). Role orchestration and model/runtime selection are inside the target (`autocontext/src/autocontext/agents/orchestrator.py`).
- **Persistence and admission:** SRC-1, `autocontext/src/autocontext/loop/stages.py`, writes matches and generation metadata to SQLite and persists analysis, coach and architect artifacts. Context-candidate evaluation and activation are a separate live boundary (`autocontext/src/autocontext/loop/context_bundle_evaluation.py`, `autocontext/src/autocontext/context_bundles/promotion.py`). Skill/lesson persistence, lifecycle and package movement also belong to this boundary (`autocontext/src/autocontext/storage/artifact_skill_lessons.py`, `autocontext/src/autocontext/knowledge/lifecycle.py`, `autocontext/src/autocontext/knowledge/package.py`).
- **TypeScript caller and consumer:** SRC-1, `ts/package.json`, declares the npm CLI and public exports. `ts/src/cli/run-command-workflow.ts` creates storage and a runner with knowledge and run roots, then calls it. `ts/src/loop/generation-runner.ts` reloads the scenario playbook and reports for competitor prompts, runs support roles, stores their output, and writes or stages playbook changes. `ts/src/loop/generation-prompts.ts` supplies the shipped prompt construction. These paths must not be treated as merely external consumers of a narrower library.
- **Operator and host surfaces:** SRC-1, `autocontext/src/autocontext/server/run_manager.py`, `autocontext/src/autocontext/mcp/server.py`, `ts/src/server/run-start-workflow.ts`, and `ts/src/mcp/solve-tools.ts` expose or drive the same system. `pi/src/index.ts` registers tools and dynamically imports `autoctx`; `pi/src/runtime-snapshot.ts` is part of its readback surface. The extension is included, while the enclosing Pi application's implementation is not frozen here.
- **Additional improvement and maintenance routes:** SRC-1 includes bounded task revision (`autocontext/src/autocontext/execution/improvement_loop.py`), mission steps (`autocontext/src/autocontext/mission/executor.py`), ambient stages (`autocontext/src/autocontext/ambient/daemon.py`, `autocontext/src/autocontext/ambient/stage_factory.py`), training (`autocontext/src/autocontext/training/runner.py`), kernel evolution (`autocontext/src/autocontext/kernel_evolution/runner.py`), and TypeScript promotion and session-memory mechanisms (`ts/src/control-plane/promotion/decide.ts`, `ts/src/session/memory-consolidation.ts`). These are included shipped responsibilities, not exclusions from the learning loop.

Two minimum passages retain the basis for including both the retained-state reader and its shipped writer. Python's knowledge setup reads stored context (SRC-1):

> playbook = "" if ablation else artifacts.read_playbook(ctx.scenario_name)
> tool_context = "" if ablation else artifacts.read_tool_context(ctx.scenario_name)
> --- `autocontext/src/autocontext/loop/stages.py`

TypeScript's support-role path submits an accepted playbook to the storage admission surface (SRC-1):

> const playbookResult = this.#artifactStore.writeOrStagePlaybook(
>   this.#scenarioName,
>   nextPlaybook,
>   {
>     requireApproval: this.#requirePlaybookApproval,
>     sourceRunId: runId,
>     generation: gen,
>     curatorDecision: "advance",
>   },
> );
> --- `ts/src/loop/generation-runner.ts`

These passages establish responsibilities, not equivalent admission guarantees across languages. In particular, the Python matched-context-candidate path and the TypeScript playbook path require separate analysis; sharing a product name does not establish parity.

### Repository coverage

The tracked root tree was enumerated at the frozen commit. Every top-level tracked file or directory is classified below. “Included” defines eligible functional evidence, not a claim that every descendant has already been read. Initial inspection traced the principal shipped producers, admission points and consumers above; detailed algorithms, ancillary commands, individual tests and archived results remain for later source inspection at this same pin. No material shipped path was inaccessible, and no material runtime directory is deliberately excluded.

All paths in this table refer to SRC-1.

| Top-level entry | Boundary status | Material paths and role; inspection or exclusion limit |
| --- | --- | --- |
| `autocontext/` | Included | `pyproject.toml`; `src/autocontext/cli*.py`, `sdk.py`, `agents/`, `loop/`, `prompts/`, `storage/`, `knowledge/`, `context_bundles/`: Python entry, production, persistence, admission and reload. `execution/`, `scenarios/`, `harness/`, `providers/`, `runtimes/`: task execution and evaluation. `server/`, `mcp/`, `session/`, `mission/`, `ambient/`, `training/`, `kernel_evolution/`, `hermes/`, `openclaw/`, `sharing/`, `integrations/`: alternative callers, maintenance, export and host bridges. Initial reads/searches cover the paths named above, storage/lesson and lifecycle surfaces, and the ambient stage factory. `tests/`, `benchmarks/`, `docs/`, `skills/`, `scripts/`, `migrations/` remain included as contracts, evaluators, drivers and operational instructions. Individual benchmark result artifacts have not been inspected here. |
| `ts/` | Included | `package.json`, `src/cli/`, `src/loop/`, `src/prompts/`, `src/knowledge/`, `src/storage/`: npm entry, generation, retained-state writer/reader. `src/control-plane/`, `src/training/`, `src/traces/`, `src/production-traces/`: registry/promotion, dataset and trace processing. `src/server/`, `src/mcp/`, `src/session/`, `src/runtimes/`, `src/agent-runtime/`, `src/tui/`, `src/scenarios/`, `src/judge/`, `src/integrations/`: shipped callers, host adapters, sessions and evaluators. Initial inspection includes the run caller, generation reader/writer/prompts, server start route, MCP solve route, promotion decision and memory consolidation. `tests/`, `examples/`, `migrations/`, build scripts and public exports remain eligible; listing them is not evidence of passing tests or Python parity. |
| `pi/` | Included | `package.json`, `src/index.ts`, `src/runtime-snapshot.ts`, `skills/autocontext/SKILL.md`, `prompts/autoctx-{improve,judge,status}.md`, and `tests/`: extension entry, tool use, readback and host-facing instructions. Entry code and skill metadata inspected; full prompt and test contents not yet inspected. No claims about the enclosing Pi runtime follow. |
| `skills/` | Included | `autocontext-consumer/SKILL.md` explicitly supplies later file consumption and package movement; `autocontext-creator/SKILL.md` supplies knowledge production; `autocontext/SKILL.md` and `references/` supply Hermes/CLI/MCP/training workflows. Consumer skill read; creator and Hermes skill/reference passages searched. These are target-authored instructions, not instructions to this analyst. |
| `examples/` | Included | `README.md`, `executable_skills/run.py`, `policy_candidates/run.py`, `kernel_evolution/run.py`, `kernel_evolution/kernelbench_h100/`, `kernel_evolution/multi_workload/`, `agent-runtime/.autoctx/agents/support.ts`, `workspace_benchmark.py`: shipped drivers, evaluation and host usage. Driver overview and selected runner/evaluator wiring inspected. Real-hardware result contents and other examples are not yet inspected; no hardware-performance conclusion is established. |
| `docs/` | Included | Root design/contracts, `internal/`, schemas and parity fixtures cover context bundles, evaluator epochs, release surfaces, runtime composition, trace boundaries and admission. Tree inspected and README declarations consulted; detailed contracts not yet read. Design documents must not be substituted for implementation or execution evidence. |
| `fixtures/` | Included | `context-bundles/`, `harness-optimization/`, `cross-runtime/` and parity JSON: evaluation and contract inputs. Tree inspected only; no fixture content or real-world efficacy claim established. |
| `protocol/` | Included | `autocontext-protocol.json`: shared protocol evidence. Tree inspected only; protocol behavior requires tracing implementations. |
| `infra/` | Included | `docker/`, `fly/`, `modal/validate_sft_serving.py`, `scripts/bootstrap.sh`: shipped deployment, serving-validation and setup paths. Tree inspected only; no successful deployment, isolation or GPU-serving claim established. |
| `scripts/` | Included | Release/dependency checks, `generate_protocol.py`, synchronization scripts and `escalation-sweep/`: development checks plus evaluation driver/summary tooling. Tree inspected only; no execution or validation results established. |
| `packages/` | Included | `README.md` read: identifies the actual shipping packages and deferred split. No additional package implementation is inferred. |
| `knowledge/` | Included | Tracked `.gitkeep` only. The knowledge store is implemented elsewhere and included above; this root supplies no learned corpus to evaluate. |
| `runs/` | Included | Tracked `.gitkeep` only. This is not evidence of an executed run. Source-native benchmark/results under other included directories remain available but uninspected. |
| `README.md` | Included | Product intent, entry surfaces, artifact layout and feature-scope declarations read. Attributed design evidence, not proof of production improvement. |
| `.env.example` | Included | Shipped configuration surface identified from the tree and README; values not yet inspected. No credential/configuration-default audit established. |
| `CHANGELOG.md` | Included | Version-history evidence available but not read; release-history assertions beyond inspected declarations are not established. |
| `.github/` | Excluded | CI, issue templates and publishing automation, identified by tree. Exclusion prevents conclusions about CI enforcement, release provenance or automation correctness; it excludes no target improvement responsibility. |
| `.dockerignore`, `.gitignore`, `.prettierrc.json` | Excluded | Development/build-context and formatting configuration. No packaging-completeness or formatting-policy audit. Runtime deployment files under `infra/` remain included. |
| `AGENTS.md`, `CLAUDE.md` | Excluded | Repository contributor/agent guidance, not loaded as binding instructions or used as evidence. No claim about contributor-agent governance. Shipped product skills and prompts remain included. |
| `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE`, `SECURITY.md`, `SUPPORT.md` | Excluded | Community, contribution, legal, reporting and support policies. No legal compliance, support commitment or security-policy audit; executable security mechanisms remain included. |

### Frozen evidence, dependencies and limits

The source identity is exactly `https://github.com/greyhaven-ai/autocontext`. The acquired read-only checkout resolves to commit `f72c154152397f54d55407508b153d28861888a5`; its status was clean at inspection. That full revision is the reviewed boundary. The applicability cutoff is **2026-10-15**, the opening's run date: claims apply to this frozen revision, not to the latest branch, current website, package registries or future releases. No additional repository, fetched documentation, or non-Git capture is admitted.

The overall evidence tier is **code-grounded**. Implementation and shipped design/instruction text were inspected. No target commands, tests, examples, services or model calls were executed. Test definitions and synthetic fixtures may establish intended checks but not successful runs. The target's archived benchmarks are eligible source-native evidence at this pin, but this boundary has not inspected their run records and registers no observed-run or causal-experiment finding.

External dependencies include model providers/endpoints, agent CLI/RPC runtimes, the enclosing Pi/MCP client, operating-system/process facilities, databases and optional Docker/remote/GPU/training infrastructure. Their adapters and configurations shipped here are included; their independent implementations and live behavior are not frozen. Consequently, this run cannot establish provider reliability, enclosing-host authority enforcement, sandbox security, hardware performance or deployment success solely from these adapters. SRC-1, `README.md`, `autocontext/src/autocontext/agents/orchestrator.py`, `pi/src/index.ts`, and `examples/kernel_evolution/run.py` identify those seams.

There is no source-access blocker. Uninspected available files are inspection limits, not access gaps or permission to infer their behavior. Later jobs may inspect additional paths within SRC-1 at this same commit. Missing live or independent execution evidence limits operational and causal conclusions without narrowing away the shipped state-producing or state-consuming paths.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/greyhaven-ai/autocontext` | f72c154152397f54d55407508b153d28861888a5 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-autocontext/related-systems/greyhaven-ai--autocontext`. Implementation: tracked tree and package entry declarations; Python CLI/solve/SDK, generation runner/pipeline/stages, role orchestration, context evaluation/promotion, storage/lessons/lifecycle/package surfaces, server/MCP, ambient, task revision, mission, training and kernel-runner passages; TypeScript run caller, generation reader/writer/prompts, server/MCP, promotion and session-memory passages; Pi entry; selected example evaluator/driver wiring. Doctrine/design: `README.md`, `packages/README.md`, consumer skill, creator/Hermes/Pi skill passages and source-native skill-reuse study descriptions. Coverage table distinguishes tree-only from content inspection. | Implementation: [Python entry](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/autocontext/pyproject.toml), [knowledge setup/persistence](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/autocontext/src/autocontext/loop/stages.py), [live candidate admission](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/autocontext/src/autocontext/loop/context_bundle_evaluation.py), [npm run caller](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/ts/src/cli/run-command-workflow.ts), [npm generation reader/writer](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/ts/src/loop/generation-runner.ts), [Pi entry](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/pi/src/index.ts). Doctrine/design: [product declaration](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/README.md), [later consumer instructions](https://github.com/greyhaven-ai/autocontext/blob/f72c154152397f54d55407508b153d28861888a5/skills/autocontext-consumer/SKILL.md). Other commit-relative paths named above are anchors within this same registered source. | No access gap in the acquired repository. Implementation inspection is static and selective, not execution or an exhaustive correctness audit. Design claims remain attributed intent. External dependency implementations and live services are outside the frozen set, preventing independent host/provider/security/deployment conclusions. Archived result contents have not yet been inspected, preventing observed-performance or causal-improvement conclusions at this stage. |
