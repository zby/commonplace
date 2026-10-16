---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "CORAL's agent orchestration, evaluation and shared-knowledge loop at commit 0123dfb939b35228cf2c1fde224cd0561e727408."
run-id: AAS-2026-10-15-coral-25e5fdab9dc4-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "0123dfb939b35228cf2c1fde224cd0561e727408"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/Human-Agent-Society/CORAL
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-coral/related-systems/Human-Agent-Society--CORAL
  revision: "0123dfb939b35228cf2c1fde224cd0561e727408"
  sha256: null
---

# CORAL boundary

## Boundary and evidence

This run examines CORAL as infrastructure for autonomous coding-agent experiments: task admission, agent launch and supervision, retained shared knowledge, evaluation, feedback and subsequent iteration. The intended use is to explain the shipped organization of that loop, including which responsibilities are executable and which depend on agents following prompts. It is not an evaluation of solution quality or proof that knowledge sharing improves outcomes.

The target class is **enclosing runtime**: CORAL owns the outer multi-agent run, while installed coding-agent harnesses own their inner model/tool turns. This does not attribute those harnesses' internal reasoning, compaction or tool policy to CORAL. The classification follows the shipped executable entry point and driver, not only the README. The package exposes `coral.cli:main`; the start command validates a task, creates an `AgentManager`, launches its agents and enters monitoring. The manager creates workspaces, starts supporting services and launches runtime adapters. For example, the Pi adapter constructs a `pi` command and launches it with `subprocess.Popen` (SRC-1, `pyproject.toml`, `coral/cli/start.py`, `coral/agent/manager.py`, `coral/agent/builtin/pi_agent.py`).

> description = "Orchestration system for autonomous coding agents"
> --- `pyproject.toml`

> manager = AgentManager(config, verbose=verbose, config_dir=config_path.parent)
> handles = manager.start_all()
> --- `coral/cli/start.py`

The **whole-system** functional boundary includes the CLI and its shipped callers, workspace and isolation setup, runtime adapters, gateway and sandbox integration, grader infrastructure, attempt records, single- and multi-island state, heartbeat and steering, warm-start and migration paths, generated instructions and seeded skills, and operator/dashboard consumption. The plugin is a shipped authoring/operation surface, not an excluded enclosing application. Example task configurations and graders are included as consumers of the same framework; they do not establish that every task or external benchmark has been reproduced.

The retained-state loop is material to this boundary. Project creation seeds bundled skills and subagent templates, preserves an existing agent role, and initializes a shared-state checkpoint repository. Worktree setup exposes notes, skills, roles, attempts and other island state through symlinks. Agent-facing instructions ask agents to read existing notes before implementation and update knowledge after evaluations. The consolidation prompt prescribes synthesis and role auditing. These are doctrine/design evidence, not evidence that an agent complied (SRC-1, `coral/workspace/project.py`, `coral/workspace/worktree.py`, `coral/template/coral.md.template`, `coral/hub/prompts/consolidate.md`).

> 7. Read notes: Start with `{shared_dir}/notes/index.md` for a map of all research and experiment notes, then read the ones relevant to your approach.
> --- `coral/template/coral.md.template`

> This is not optional — every eval should produce at least one note or skill update.
> --- `coral/template/coral.md.template`

The executable evaluation path connects that state to later decisions. `coral eval` calls `submit_eval`, which commits the candidate, checkpoints shared state and writes a pending attempt. The daemon grades an isolated checkout and writes a finalized attempt. The manager reads scored attempts to select heartbeat actions and construct feedback. Notes are reloaded from files by the hub, CLI and dashboard rather than being an unused library API (SRC-1, `coral/cli/eval.py`, `coral/hooks/post_commit.py`, `coral/hub/checkpoint.py`, `coral/grader/daemon.py`, `coral/agent/manager.py`, `coral/hub/notes.py`, `coral/cli/query.py`, `coral/web/api.py`).

> # Checkpoint shared state at submission time (captures agent's current notes/skills).
> shared_state_hash = checkpoint(str(coral_dir), agent_id, message, island_id=island_id)
> --- `coral/hooks/post_commit.py`

### Repository coverage

The tracked top-level tree was inventoried at the pinned commit. “Included” identifies the functional evidence boundary, not a claim that every file was read. Initial inspection below distinguishes traced paths from inventoried paths awaiting detailed analysis. There was no unavailable material shipped path at boundary establishment; uninspected files are not access gaps. All rows refer to SRC-1.

| Top-level tracked entry | Treatment and material paths | Initial inspection and limit |
|---|---|---|
| `coral/` | Included: `cli/` admission, start/resume, eval and queries; `agent/` manager, adapters, heartbeat, warm-start and migration; `workspace/` project, worktrees and isolation; `hooks/post_commit.py`; `grader/` daemon and grader loading; `hub/` attempts, notes, skills, checkpoints, islands and steering; `template/` prompts, roles, specialist agents and maintenance skills; `gateway/`, `sandbox/`; `web/` API and packaged UI. | Traced CLI start → manager → project/worktree → adapter, eval → submission/checkpoint → daemon → manager feedback, and note consumers. Read consolidation and agent-workflow instructions. Other adapters, maintenance scripts, gateway/sandbox internals, warm-start/migration details and bundled UI are available for subsequent inspection, not excluded. |
| `examples/` | Included: task YAML, seeds, packaged graders, evaluator support and task-specific prompts, including benchmark-agent seeds under terminal-bench and swebench-verified. | Tree inventoried; read circle-packing task and its complete grader as a concrete configuration/consumer path. Other tasks remain available, not presumed equivalent or independently validated. |
| `plugin/` | Included: per-harness manifests, `hooks/session-start.py`, quickstart/setup/task-authoring/experiment skills and author/doctor agent prompts. | Read complete `plugin/README.md`; inventoried implementation paths. Detailed hook and skill behavior remains to inspect. |
| `.agents/` | Included: `plugins/marketplace.json`, Codex plugin discovery. | Inventoried and identified through plugin README; manifest not yet read. |
| `.claude-plugin/` | Included: `marketplace.json`, Claude plugin discovery. | Inventoried and identified through plugin README; manifest not yet read. |
| `docker/` | Included: Claude, Codex and OpenCode Dockerfiles and entrypoints as shipped run wrappers. | Inventoried; inspected wrapper selection in CLI start, not each image/entrypoint. No isolation guarantee follows from inventory. |
| `litellm_config.yaml` | Included: shipped provider-routing configuration. | Inventoried, not yet read; no claim about a deployed provider configuration. |
| `install.sh` | Included: installation entry point. | README describes global tool installation; script not yet read. No installation-success claim. |
| `pyproject.toml` | Included: package, dependencies, console entry point and bundled-package boundary. | Read completely; examples are excluded from the wheel but remain repository-shipped consumers in this analysis. |
| `uv.lock` | Included: dependency-resolution evidence. | Inventoried, not read; no dependency reproducibility or supply-chain assurance. |
| `web/` | Included: frontend `src/pages/Knowledge.tsx`, `Overview.tsx`, `Dag.tsx`, `Logs.tsx`, components, hooks and API client; frontend build configuration. | Tree inventoried; backend notes/skills API read. Frontend rendering and control details remain to inspect. |
| `tests/` | Included: declared behavioral checks for manager, hub, checkpoints, grading, runtimes, isolation, steering and web consumers. | Test-file inventory only; no test execution or passing-suite claim. These may supply implementation-contract evidence, not observed run evidence merely by existing. |
| `docs/` | Included: source-native architecture, shared-state/eval-loop, API, CLI, runtime, plugin and tutorial documentation under `content/docs/`. | Tree inventoried; detailed documents not yet read. Site generator, historical plans and documentation tests are excluded from runtime-mechanism conclusions. |
| `README.md` | Included: source-native purpose, supported harnesses, entry workflow and stated architecture. | Read completely; marketing and reported capabilities do not establish observed performance. |
| `README_CN.md` | Included: alternate-language source-native documentation. | Inventoried, not yet read; no comparison of translation consistency. |
| `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` | Excluded from deployed run behavior: contributor guidance, distinct from generated agent instructions under `coral/template/`. | Inventoried, not read; cannot conclude anything about repository contribution practice. |
| `.claude/` | Excluded: repository-development/debug/extension/task-authoring and release-promotion skills. | Tree inventoried; no claims about contributor-agent operation. Shipped user plugin skills remain included separately. |
| `.github/` | Excluded: issue/PR templates, CI, release/promotion and blog-deployment automation. | Tree inventoried; no conclusions about release trust or CI effectiveness. |
| `.dockerignore`, `.gitignore`, `.pre-commit-config.yaml` | Excluded: repository/build filtering and development hygiene. | Inventoried, not read; no artifact-cleanliness or lint-enforcement conclusions. |
| `scripts/` | Excluded: `migrate_legacy_graders.py`, offline legacy-task migration. | Inventoried, not read; no legacy migration correctness claim. Current grader loading remains included. |
| `demos/` | Excluded: showcased solution dumps `kernel_builder_1103.py`, `solution_erdos.py`. | Inventoried, not read; no inference about achieved research results. |
| `assets/` | Excluded: diagrams, logos, screenshots and demo animation. | Inventoried; media are not execution traces used by this run. |
| `blog/` | Excluded: showcase site and comparison images. | Inventoried, not read; no benchmark or comparative-effectiveness conclusion. |
| `LICENSE` | Excluded from operational mechanism analysis. | Inventoried, not read; no independent licensing opinion. |

### Frozen evidence and external limits

The source is the acquired, read-only Git checkout at full commit **0123dfb939b35228cf2c1fde224cd0561e727408**. HEAD matched that revision and Git reported no working-tree changes. The applicability cutoff is **2026-10-15**, the supplied run date; it does not claim that the checkout represents all changes through that date. The overall tier is **code-grounded** because the classification and loop boundary are grounded in executable source. Documentation and prompts remain separately identified as doctrine/design evidence.

External coding-agent installations, model providers and credentials, host OS/process behavior, Git, Docker/tmux, installed Python dependencies and task-specific data/services are dependencies, not separately frozen sources. Only CORAL's shipped adapters, configurations and integration code are inside the evidence boundary. Consequently this run cannot establish those external implementations' internal policies, actual service behavior, effective security isolation in a deployment, or successful benchmark reproduction. External papers and linked live documentation are not added as evidence. No target code, tests or examples were executed, and no observed-run or causal-experiment evidence was established.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Human-Agent-Society/CORAL` | 0123dfb939b35228cf2c1fde224cd0561e727408 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-coral/related-systems/Human-Agent-Society--CORAL`. Implementation: complete `pyproject.toml`; bounded entry/consumer traces in `coral/cli/start.py`, `coral/cli/eval.py`, `coral/agent/manager.py`, `coral/agent/builtin/pi_agent.py`, `coral/workspace/project.py`, `coral/workspace/worktree.py`, `coral/hooks/post_commit.py`, `coral/hub/checkpoint.py`, `coral/hub/notes.py`, `coral/web/api.py`; symbol/search traces in CLI dispatch/query and heartbeat paths; complete circle-packing task and grader. Doctrine/design: complete README and plugin README, agent workflow/orientation/shared-state sections of `coral/template/coral.md.template`, complete `coral/hub/prompts/consolidate.md`. Full tracked-tree inventory; additional coverage status in table above. | Implementation: [package entry point](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/pyproject.toml), [manager](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/coral/agent/manager.py), [submission and checkpoint linkage](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/coral/hooks/post_commit.py), [grader daemon](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/coral/grader/daemon.py). Doctrine/design: [generated agent instructions](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/coral/template/coral.md.template), [consolidation prompt](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/coral/hub/prompts/consolidate.md), [plugin contract](https://github.com/Human-Agent-Society/CORAL/blob/0123dfb939b35228cf2c1fde224cd0561e727408/plugin/README.md). | No checkout access gap identified. Initial inspection is not an allowlist. External harness/provider internals and deployment evidence are not frozen; therefore no external-policy, observed-compliance, realized-performance or causal-benefit conclusions. |
