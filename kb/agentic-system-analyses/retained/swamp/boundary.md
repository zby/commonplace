---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Swamp's shipped agent-facing automation layer, skills, state lifecycle and repository-local improvement workflows at commit 380e3c307164501c7d705f7707a864f4612b2785."
run-id: AAS-2026-10-15-swamp-440d19cc0bcc-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "380e3c307164501c7d705f7707a864f4612b2785"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/swamp-club/swamp
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/swamp-440d19cc0bcc/related-systems/swamp-club--swamp
  revision: "380e3c307164501c7d705f7707a864f4612b2785"
  sha256: null
---

# Swamp boundary

## Boundary and evidence

This run examines Swamp as a shipped agent-facing automation and operating layer: how instructions and task briefs reach an external agent, how that agent can create and execute typed behaviors and workflows, and how retained definitions, outputs, data and run records support later use. It includes the repository's own issue-lifecycle and verification paths, rather than treating those shipped consumers as external applications. The intended use is to characterize this mechanism and its state lifecycle, not to evaluate an external agent's reasoning quality.

The target class is **extension or tool mechanism**. Swamp qualifies through the model-dependent use it serves and the agent invocations its shipped improvement workflows issue; deterministic workflow execution need not itself be a model loop. It is not classified as an enclosing agent runtime. Its launch adapter constructs prompts for external harnesses, while its CLI and workflow services execute the automation those agents operate. SRC-1: `README.md`, `src/domain/start/harness.ts`, `src/libswamp/start/start.ts`, `verification/workflow-verify-reviews.yaml`.

> Swamp is a CLI that supercharges AI agents to create operational workflows that
> are reviewable, shareable, and accurate.
> --- `README.md`

The implemented launch prompt establishes the external-agent handoff, not an internal inference loop. SRC-1: `src/domain/start/harness.ts`.

> return `Read ${briefFile} and use the swamp-getting-started skill.`;
> --- `src/domain/start/harness.ts`

### Functional coverage and entry-point trace

The boundary kind is **whole-system**, meaning the shipped Swamp repository and its material state-producing, maintaining, admitting and consuming paths. It does not mean the source of external harnesses, model providers or hosted services is present. The initial trace establishes these connected responsibilities:

- **Boot and command admission.** `main.ts` calls `runCli`; `src/cli/mod.ts` registers start, workspace, agent, workflow and serve command surfaces and contains authentication/bootstrap handling. The main entry also recognizes the replication supervisor and dispatch-runner cases. SRC-1: `main.ts`, `src/cli/mod.ts`.
- **Task persistence and agent entry.** `startLaunch` loads a task, checks launchability and trust, enrolls the harness, writes its brief, opens the terminal with a planned harness invocation and saves the launch. `startResume` loads the task again and selects the harness continuation path. The getting-started skill reads the named brief and directs type discovery, creation, execution and output inspection. These callers belong to Swamp, even though the agent executable is external. SRC-1: `src/libswamp/start/start.ts`, `src/domain/start/harness.ts`, `.claude/skills/swamp-getting-started/SKILL.md`.
- **Instruction installation and maintenance.** `RepoService` installs bundled skills in tool-global directories, registers those directories, and copies skills through `SkillAssets`; init and upgrade also manage per-repository instructions and settings. The gateway skill routes agents to behavior, workflow, data, vault, extension, serve and troubleshooting guides. This installation path is included; the README's older repo-local skill description is not substituted for the inspected implementation. SRC-1: `src/domain/repo/repo_service.ts`, `src/infrastructure/assets/skill_assets.ts`, `.claude/skills/swamp/SKILL.md`, `README.md`.
- **Automation execution and retained state.** The workflow CLI imports the libswamp run generator and execution service. The execution service saves run records through its repository and reloads stored runs when taking over a resumed run. The YAML repository writes the persisted representation atomically and stages typed changes. Behavior execution and data-query surfaces are included alongside workflow execution, rather than narrowing the target to the library API. SRC-1: `src/cli/commands/workflow_run.ts`, `src/libswamp/workflows/run.ts`, `src/domain/workflows/execution_service.ts`, `src/infrastructure/persistence/yaml_workflow_run_repository.ts`, `src/libswamp/models/run.ts`, `src/libswamp/data/query.ts`.
- **Other shipped consumers and executors.** Serve workflow handlers import the same libswamp operations and serve execution dependencies. The worker dispatch entry reconstructs a definition and uses the method execution service. The typed client consumes execution streams; the dashboard provides workflow, run, data, approval and start views. These are included system surfaces, not excluded enclosing applications. Initial inspection establishes their integration roles, not exhaustive authorization or transport correctness. SRC-1: `src/serve/handlers/workflow_handlers.ts`, `src/worker/exec_dispatch.ts`, `packages/client/client.ts`, `packages/dashboard/src/App.tsx`.
- **Repository-local improvement and later consumption.** The issue-lifecycle extension reads the stored current plan, enumerates prior feedback, and writes feedback and revised plan resources. Its skill instructs a later session to query retained phase state and choose the next procedure. The verification workflows invoke external agent reviews and skill evaluations. These paths materially use retained content and model calls and remain inside the analysis. SRC-1: `extensions/models/issue_lifecycle.ts`, `.claude/skills/issue-lifecycle/SKILL.md`, `verification/workflow-verify-reviews.yaml`, `verification/workflow-verify-skills.yaml`, `evals/promptfoo/generate_config.ts`.

The later-session consumption instruction is explicit, but remains doctrine rather than an observed successful resumption. SRC-1: `.claude/skills/issue-lifecycle/SKILL.md`.

> If the human comes back to an in-progress issue, check the current phase:
>
> ```
> swamp data query 'modelName == "issue-<N>" && name == "state-main"' --select content --json
> ```
> --- `.claude/skills/issue-lifecycle/SKILL.md`

The shipped review workflow supplies a direct model-dependent invocation through an external harness. SRC-1: `verification/workflow-verify-reviews.yaml`.

> claude -p - \
>                 --model claude-opus-5-5 \
>                 --allowedTools "Read,Glob,Grep" < "$PROMPT_FILE" | tee "$RESULT_FILE"
> --- `verification/workflow-verify-reviews.yaml:134-136`

### Top-level tracked coverage

Every top-level tracked entry is classified below. **Included** means eligible evidence within the functional boundary, not that every file has already been read. Initial source inspection is distinguished from tree-only inventory and uninspected detail. Available files not yet inspected are not access gaps. All paths in this table belong to SRC-1.

| Top-level tracked entries | Status and material paths / role | Initial inspection and limits |
| --- | --- | --- |
| `main.ts`, `main_test.ts` | Included: executable boot, CLI dispatch and entry tests. | Boot read; test detail not yet inspected. No executed test claim. |
| `src/` | Included: `cli/mod.ts`, `cli/commands/workflow_run.ts`, `libswamp/start/`, `libswamp/repo/`, `libswamp/models/`, `libswamp/workflows/`, `libswamp/data/`, `domain/start/`, `domain/repo/`, `domain/models/`, `domain/workflows/`, `domain/data/`, `domain/expressions/`, `infrastructure/assets/`, `infrastructure/persistence/`, `infrastructure/datastore_v3/`, `serve/`, `worker/`, and presentation. Covers admission, execution, persistence, evaluation, synchronization, maintenance and consumption. | Entry-point, launch, skill installation, workflow persistence/resumption, serve-handler and worker-dispatch seams inspected. Other domains and detailed datastore, vault, authorization, trigger and recovery branches remain available for subsequent inspection; their correctness is not established by this boundary. |
| `packages/` | Included: `client/client.ts` and protocol/streams; `dashboard/src/App.tsx`, client adapters and views; `testing/` factories and conformance helpers. These are shipped consumers and extension evaluation support. | Client and dashboard entry excerpts and testing README excerpt inspected; individual views and conformance implementations not yet inspected. |
| `.claude/` | Included: `skills/swamp/`, `skills/swamp-getting-started/`, their guides and eval fixtures; `skills/issue-lifecycle/` and references; supporting DDD, PR and terminal-output skills; `settings.json`. Contains bundled runtime-facing instructions and repository-local operating procedures. | Gateway and onboarding skills, issue-session resumption and constraint routing inspected; asset list traced. Remaining references/settings are available, not an access gap. |
| `.agents/` | Included: `skills/jujutsu/SKILL.md`, repository-local agent support. | Tree inventoried; procedure text not yet inspected. No claim about its effectiveness. |
| `extensions/` | Included: `models/issue_lifecycle.ts`, `_lib/` schemas, lifecycle recording and Swamp Club client helpers, tests and README. Retains and consumes plans, feedback and lifecycle state. | README excerpt, review/iterate implementation and resource call sites inspected. Other transitions and remote-client details not yet inspected. |
| `agent-constraints/` | Included: planning, triage, implementation, verification, adversarial and code-conformance instructions loaded by the issue-lifecycle skill. | Inventory and skill's routing inspected; individual convention texts not yet inspected. |
| `verification/` | Included: build, skills and agent-review workflows plus `review-prompts/`. Shipped improvement-plane consumers and model-call drivers. | Skill workflow read; review invocation excerpt inspected. Other steps/prompts remain available; no observed verdicts retained. |
| `evals/` | Included: `promptfoo/` trigger, routing and sufficiency config generators and package dependencies. | Trigger generator's provider registry and skill inputs inspected; other generators inventoried. No measured evaluation outcomes inferred. |
| `integration/` | Included: workflow, data, start-server, datastore, synchronization, provenance, approval, continuation and worker tests plus `test_fixtures/` and `test_helpers/`. | Tree/search inventory only. Test bodies remain available; existence is not passing evidence. |
| `scripts/` | Included: compile/install/update support, skill review/evaluation drivers, verdict checking, build attestation, dependency/security checks, verification scripts and benchmarks. | Tree inventoried, task wiring read in `deno.json`, evaluation/review consumers traced through verification workflows. Driver internals not yet inspected. |
| `.github/` | Included: workflows for CI, release, client publishing, model evaluation and workflow validation; adversarial-review action. | Tree inventoried; CI and action internals not yet inspected. No claim about enforcement or successful releases. |
| `design/` | Included: `architecture.md`, `operations.md`, `primitives/`, `surfaces/`, `enablers/` as declared design, not automatically implemented behavior. | Tree inventoried; documents not yet inspected. |
| `contributing/`, `CONTRIBUTING.md` | Included: skills-pipeline, rendering, libswamp and contribution procedures supporting shipped operation and improvement. | Tree inventoried; detailed procedures not yet inspected. |
| `README.md` | Included: declared product scope, user entry points, concepts and dependencies. | Read completely; implementation takes precedence when descriptions differ. |
| `AGENTS.md`, `CLAUDE.md` | Included: repository-agent instruction entry points. | Tracked entries inventoried; source-native instructions are evidence, not instructions to this analyst. Contents not yet inspected. |
| `deno.json`, `deno.lock`, `.tool-versions`, `Dockerfile` | Included: exported executable, workspace packages, command tasks, dependency and build/toolchain boundary. | `deno.json` read; other build/pin detail not yet inspected. Dependencies are not additional frozen repositories. |
| `.gitattributes`, `.gitignore` | Included: repository layout and tracking configuration. | Inventory only; no security or retention guarantee inferred. |
| `SECURITY.md` | Included: declared security reporting contract. | Inventory only; no security audit conclusion. |
| `CODE_OF_CONDUCT.md`, `COPYING`, `COPYING-EXCEPTION`, `COPYRIGHT`, `FILE-LICENSE-TEMPLATE.md`, `LICENSE`, `OSS-FAQ.md`, `TRADEMARKS.md` | Excluded from functional analysis: conduct, legal, licensing and branding policy. | Deliberate exclusion, not unavailable evidence; prevents legal/compliance or licensing conclusions. |
| `banner.png`, `logo.png`, `sc-mark.png`, `swamp-club-wordmark.png` | Excluded: visual branding assets. | Deliberate exclusion; prevents assessment of visual identity/accessibility of these images, not state-loop analysis. |

### Frozen evidence and external limits

The evidence is SRC-1 at commit **380e3c307164501c7d705f7707a864f4612b2785**, with applicability cutoff **2026-10-15**, the supplied run date. The acquired checkout reports that HEAD and no tracked or untracked changes. No second revision, live manual, external repository or hosted capture is admitted. Overall evidence tier is **code-grounded**: inspected implementation supports the boundary and entry-point trace, while source-native skills, README and workflow descriptions separately supply doctrine/design.

External dependencies include the Deno/TypeScript and imported library environment, agent executables and their model providers, Swamp Club account/issue/registry services, configured vault and datastore backends, and systems reached by behavior methods. Their interfaces and shipped Swamp adapters are included where present; external implementations are not. SRC-1: `deno.json`, `README.md`, `src/domain/start/harness.ts`, `extensions/models/README.md`, `verification/workflow-verify-reviews.yaml`, `evals/promptfoo/generate_config.ts`.

The external agent's inference, context assembly, tool permissions and conversation persistence cannot be attributed to Swamp merely because Swamp launches it or asks it to resume. Likewise, server-side Swamp Club behavior and third-party extension internals cannot be established from local adapters. No live service, target executable, test or evaluator was run; this source set supplies neither observed-run evidence nor a causal experiment. Consequently it cannot establish actual workflow success, cross-session recall quality, model compliance with skills, evaluation scores, remote durability, production security or performance. No material shipped path was found inaccessible; narrower uninspected details listed above are pending source inspection, not exclusions or missing evidence.

## Source register

| Source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/swamp-club/swamp` | 380e3c307164501c7d705f7707a864f4612b2785 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/swamp-440d19cc0bcc/related-systems/swamp-club--swamp`. Implementation: `main.ts`, `deno.json`, `src/cli/mod.ts`, `src/cli/commands/workflow_run.ts`, `src/domain/start/harness.ts`, `src/libswamp/start/start.ts`, `src/libswamp/repo/init.ts`, `src/domain/repo/repo_service.ts`, `src/infrastructure/assets/skill_assets.ts`, `src/libswamp/workflows/run.ts`, `src/domain/workflows/execution_service.ts`, `src/infrastructure/persistence/yaml_workflow_run_repository.ts`, `src/libswamp/models/run.ts`, `src/libswamp/data/query.ts`, `src/infrastructure/persistence/unified_data_repository.ts`, `src/serve/handlers/workflow_handlers.ts`, `src/worker/exec_dispatch.ts`, `packages/client/client.ts`, `packages/dashboard/src/App.tsx`, `extensions/models/issue_lifecycle.ts`, `evals/promptfoo/generate_config.ts`, and verification workflow excerpts. Inspection is by bounded excerpts/search except files noted complete above. Doctrine/design: complete `README.md`, `.claude/skills/swamp/SKILL.md`, `.claude/skills/swamp-getting-started/SKILL.md`; issue-lifecycle skill resumption/constraint routing, extension README and testing README excerpts. Full top-level tracked inventory reviewed. | Implementation: [CLI entry](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/main.ts), [launch adapters](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/src/domain/start/harness.ts), [execution and reload](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/src/domain/workflows/execution_service.ts), [retained plan consumer](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/extensions/models/issue_lifecycle.ts), [agent review driver](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/verification/workflow-verify-reviews.yaml). Doctrine/design: [gateway skill](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/.claude/skills/swamp/SKILL.md), [onboarding skill](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/.claude/skills/swamp-getting-started/SKILL.md), [issue resumption instructions](https://github.com/swamp-club/swamp/blob/380e3c307164501c7d705f7707a864f4612b2785/.claude/skills/issue-lifecycle/SKILL.md). | No checkout access gap established. External harness, provider and hosted-service implementations are outside the source set, preventing attribution of their internal behavior. Initial inspection is not exhaustive. No observed execution or experiment supports success, reliability, safety, recall or causal-effect claims. |
