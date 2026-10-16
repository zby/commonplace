---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "jaz-evals evaluation and improvement workflows at commit 2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72, with external runtime and benchmark internals unavailable."
run-id: AAS-2026-10-15-jaz-evals-17ab95f93794-01
result-disposition: complete
target-class: workflow
boundary-kind: complete artifact, partial loop
reviewed-boundary: "2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/jaz-lang/jaz-evals
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/jaz-evals-17ab95f93794/related-systems/jaz-lang--jaz-evals
  revision: 2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72
  sha256: null
---

# jaz-evals boundary

## Boundary and evidence

The target is the jaz-evals reproduction package, not the separately distributed JAZ runtime. Its intended use is to configure and run agent-method/benchmark pairings, grade attempts, retain traces and metrics, and rebuild comparative results. It is in scope as a model-dependent **workflow**: shipped harnesses invoke agents, and the package includes instructions and code for carrying improved context between tasks. The README calls JAZ “the agent framework under test,” rather than identifying this package as that framework (SRC-1, `README.md`).

The frozen boundary is commit `2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72`, with an applicability cutoff of 2026-10-15. The evidence tier is **code-grounded** for the shipped orchestration and adapter code. Source text was inspected read-only; no target, tests, examples, containers or provider calls were executed. Documentation about published runs is attributed reporting, not an observed run or a causal experiment in this evidence set.

The boundary kind is **complete artifact, partial loop**. All parent-repository paths at this commit remain eligible evidence, including shipped callers, prompts, evaluators, patches and reporting consumers. However, the benchmark submodules are uninitialized, and the installed JAZ, Letta and smolagents implementations are not part of the frozen source. These are material parts of execution, state maintenance and grading. This boundary therefore does not claim whole-system coverage merely because the parent repository is frozen. Submodule gitlinks pin other repositories but do not supply their contents as registered evidence.

### Shipped entry points and responsibilities

The installed `jaz-evals` entry point calls `cli.main`, which loads a configuration and calls `run_evaluation`. The runner builds the environment and selected harness, supplies an `AgentEnv`, grades after the harness returns, writes attempt records, and aggregates results. These are responsibilities of this target, not an excluded enclosing application (SRC-1, `pyproject.toml`, `src/jaz_evals/cli.py`, `src/jaz_evals/eval_harness.py`, `src/jaz_evals/registry.py`). The inspected implementation includes:

> report = harness.run_task(AgentEnv(env))
> --- `src/jaz_evals/eval_harness.py`

The registered methods are JAZ, JAZ-per-task, ACE, Letta and smolagents. Their shipped adapters respectively call JAZ, drive fresh task sessions, evolve an ACE playbook, create and message a Letta agent, or build and run a smolagents chain. These are not passive dataset utilities (SRC-1, `src/jaz_evals/harnesses/__init__.py`, `src/jaz_evals/harnesses/jaz_harness.py`, `src/jaz_evals/harnesses/jaz_per_task.py`, `src/jaz_evals/harnesses/ace.py`, `src/jaz_evals/harnesses/letta_harness.py`, `src/jaz_evals/harnesses/smolagents_harness.py`). For example, the JAZ adapter issues:

> jaz.invoke(*self._root_overrides(), *self._build_root_hooks(), *root_guard, **inputs)
> --- `src/jaz_evals/harnesses/jaz_harness.py`

The AppWorld JAZ configuration selects a shipped improvement prompt. Its declared loop is relevant evidence about intended context production and later consumption, but not proof that a model followed it (SRC-1, `configs/appworld_jaz.yaml`, `prompts/ttsi/jaz.md`):

> Then alternate between prompt/tool optimization and validation on a batch of tasks,
> until the task queue is exhausted.
> --- `prompts/ttsi/jaz.md`

The ACE implementation independently supplies an explicit task queue and adaptation path, including loading initial playbook state, passing it to sessions, adapting after task completion and writing snapshots (SRC-1, `src/jaz_evals/harnesses/ace.py`). No general-purpose durable knowledge system is inferred from this evaluation-local state.

Post-run consumers are also inside the artifact boundary. `jaz-evals-analyze` discovers retained attempt artifacts and computes diagnostics; the two log-viewer entry points render method-specific traces. The shipped official-AppWorld shell driver launches external AppWorld runs and is included as this package's driver, even though it bypasses `run_evaluation`. Its downstream runtime and grader remain unavailable dependencies, not responsibilities attributed to jaz-evals (SRC-1, `pyproject.toml`, `src/jaz_evals/analyze_cli.py`, `scripts/run_appworld_official_react.sh`).

### Coverage and limits

This inventory distinguishes initial inspection from the eligible source boundary. A file not yet inspected is not an access gap.

| Top-level path | Treatment and initial coverage | Limit or conclusion prevented |
| --- | --- | --- |
| `README.md` | Included; read in full for target identity, usage, dependencies and reproduction limits. | Published-operation claims remain attributed. |
| `pyproject.toml` | Included; read in full for installed entry points, runtime pins and dependency boundaries. | Pins do not expose dependency implementation. |
| `src/` | Included: `jaz_evals/cli.py`, `eval_harness.py` and `registry.py` read in full; entry/consumer ranges inspected in `analyze_cli.py`, `harnesses/__init__.py`, `jaz_harness.py`, `jaz_per_task.py`, `ace.py`, `letta_harness.py` and `smolagents_harness.py`. Tree and symbol searches located environment setup/grading, isolation, provenance and configuration. Remaining material includes `env.py`, `envs/stulife.py`, `envs/appworld.py`, `hooks.py`, ACE playbook/dedup helpers, trace writers/viewers, analysis, pricing and Letta container patches. | Remaining included code is not yet fully inspected; no claim of complete adapter, grader, patch or state-lifecycle coverage. |
| `configs/` | Included; tree enumerated and `appworld_jaz.yaml` read to trace configuration into shipped improvement guidance. Other arms remain available for later inspection. | One configuration does not establish identical behavior across arms. |
| `prompts/` | Included; tree enumerated; `ttsi/jaz.md` read in full. Long-horizon and other TTSI prompts remain included but not yet fully inspected. | Instructions establish intended behavior, not adherence. |
| `scripts/` | Included: artifact-generation documentation inspected, plus official-baseline launch/wait/integrity-check code. Material includes `run_appworld_official_react.sh`, `_artifacts.py`, `_curves.py`, table/plot generators, run manifests and `release_traces.py`. | Generator and release implementations are not yet fully inspected. Archived run directories are not supplied, preventing independent reconstruction of reported scores. |
| `tables/` | Included as shipped result artifacts; tree enumerated, numerical/PDF contents not inspected. | No numerical comparison or verification is established here. |
| `third_party/` | Gitlink metadata inspected; `ELL-StuLife` at `1a5dd05d97a2f197ab0763ae33b61f2523602731` and `appworld` at `6830ac0e5a36b00e5691f5d3d9360c9dfc6a5045` are uninitialized. Contents unavailable within this source set. | Prevents tracing benchmark state transitions, data repairs, native grading and the official baseline end to end. |
| `.gitmodules` | Included; read in full for benchmark fork identities. | Metadata does not supply those repositories as evidence. |
| `uv.lock` | Included dependency-resolution artifact; not inspected. | No lock-wide dependency audit. |
| `.gitignore` | Included administrative artifact; not inspected. | No exhaustive ignored-file policy claim. |
| `LICENSE` | Deliberately excluded from behavioral analysis. | No legal/licensing conclusion. |

External execution dependencies include JAZ (`jaz-lang==0.2.0a4` in the local group), smolagents, a Letta server/client with optional Turbopuffer-backed search, OpenAI model services, benchmark forks and task data, and ACE's sentence-transformer encoder. Their declarations and adapter seams are evidence; their internals and live behavior are not. This prevents conclusions about actual context compaction/retrieval semantics inside those runtimes, provider stability, full benchmark validity or reproducibility of historical numbers. The README also distinguishes the installable JAZ release from the development checkouts used for historical runs (SRC-1, `pyproject.toml`, `README.md`). No linked paper, package, external trace archive or dependency repository is added to the frozen source set.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/jaz-lang/jaz-evals` | 2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/jaz-evals-17ab95f93794/related-systems/jaz-lang--jaz-evals`. Implementation: CLI, central runner, registration, bounded adapter/analysis/official-driver ranges named above. Doctrine/design: README, dependency declarations, AppWorld JAZ configuration, TTSI JAZ prompt, artifact-generation documentation and submodule metadata. Reported operation: README's reproduction and historical-run accounts. The tracked tree and relevant symbols were enumerated; initial inspected paths are not an allowlist. | Implementation: [runner](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/src/jaz_evals/eval_harness.py), [method registration](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/src/jaz_evals/harnesses/__init__.py), [ACE](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/src/jaz_evals/harnesses/ace.py), [official driver](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/scripts/run_appworld_official_react.sh). Doctrine/design: [TTSI prompt](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/prompts/ttsi/jaz.md), [metadata](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/pyproject.toml). Reported operation: [README](https://github.com/jaz-lang/jaz-evals/blob/2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72/README.md). | Uninitialized submodules, unregistered dependency implementations, unavailable task/runtime data and historical run artifacts prevent whole-loop and historical-result verification. Included but uninspected files are identified above, not classified as inaccessible. No observed-run or causal-experiment layer is established. |
