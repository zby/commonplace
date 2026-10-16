---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Meta-n's shipped recursive improvement framework and drivers at commit b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8."
run-id: AAS-2026-10-14-meta-n-18c23b6f8bb4-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/MinnesotaNLP/Meta-n
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/meta-n-18c23b6f8bb4/related-systems/MinnesotaNLP--Meta-n
  revision: b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8
  sha256: null
---

# Meta-n boundary

## Boundary and evidence

This run analyses the shipped Meta-n framework for model-generated improvements to task-solving agents. Its primary target class is **builder or improvement plane**: the framework selects evaluated candidate chains, asks a model to generate additional improvement code, and evaluates the resulting solver. Native solving and external-agent orchestration are included constituent responsibilities, not excluded hosts. The intended use is to explain the implementation's improvement loop, retained state, injection channels and evaluation boundaries; this is not a verification of the paper's performance claims.

The boundary is **whole-system** at Git commit `b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8`, with applicability cutoff **2026-10-14**. The acquired checkout's HEAD matches that commit and its tracked working tree is clean. The overall tier is **code-grounded**. Documentation supplies declared design, and executable source supplies implementation evidence. No target code, test, benchmark or model call was executed. Tests and fixtures are source-level contracts, not newly observed runs.

The shipped caller belongs to this target. The installed `meta-n` entry point maps to `meta_n.main:main`; the CLI constructs the improvement engine, executor and orchestrator, invokes the search with resume state, and saves its results (SRC-1, `pyproject.toml`, `meta_n/main.py`). The classification is grounded by the model-generation and admission path, not just the repository's title (SRC-1, `meta_n/core/evolutionary_orchestrator.py`):

> injected, omega_tokens = await self.omega.generate(
>     traces=parent.traces,
>     context_stack=parent.injected_codes,
>     tasks=tasks,
>     depth=child_depth,
>     temperature=temperature,
> --- `meta_n/core/evolutionary_orchestrator.py`

> if self.config.verified_code:
>     barred = self._nonadopting_verified_tasks(
>         child, injected, sandbox_verified_names
>     )
>     self.archive.add(child, bar_from_best=barred)
> else:
>     self.archive.add(child)
> --- `meta_n/core/evolutionary_orchestrator.py`

Functional inclusion covers task/configuration loading; native and external base solvers; fixed prompts and prompt rendering; generated preprocessing and helper libraries; candidate selection, gates and optional repair paths; execution/scoring adapters; archive and checkpoint writing/rebuilding; later reuse of traces and code; budget/concurrency guards; telemetry; and shipped post-run analysis tools. Feature existence does not imply activation in every configuration. In particular the bundled configuration and explicit CLI choices are part of the same boundary (SRC-1, `meta_n/configs/benchmark_features.yaml`, `meta_n/main.py`).

Persistence and subsequent consumption are inside the boundary. Candidate traces and complete injected chains are written by `RunPersistence`, reconstructed by `Archive.rebuild_from_disk`, and used by resumed search. Archive traces and prior injections also enter subsequent Ω calls; `MetaLayer` consumes generated context and libraries when invoking its inner solver. Analysis tools read the saved run summaries (SRC-1, `meta_n/core/run_persistence.py`, `meta_n/core/archive.py`, `meta_n/core/meta_layer.py`, `meta_n/analysis/best_of_k.py`). Minimum implementation anchors for the write/reload/consume chain are:

> for i, ic in enumerate(candidate.injected_codes):
>     with open(cand_dir / f"injected_code_d{i+2}.json", "w") as f:
>         json.dump(
>             ic.model_dump(exclude={"raw_omega_prompt", "raw_omega_response"}),
>             f, indent=2,
>         )
> --- `meta_n/core/run_persistence.py`

> self._orch.archive = Archive.rebuild_from_disk(
>     archive_dir,
>     barred_from_best=checkpoint.get("barred_from_best"),
>     **self._orch._archive_kwargs(),
> )
> --- `meta_n/core/run_persistence.py`

> script, reasoning, tokens = await self.inner_solver.solve(task, context)
> script = self._prepend_library(self._maybe_deploy_verified_helper(script))
> return script, reasoning, tokens, context, False
> --- `meta_n/core/meta_layer.py`

### Repository coverage

Every top-level tracked file or directory is classified below. Included paths remain available for deeper inspection at this same commit; this table records initial boundary inspection, not an exhaustive audit or an evidence allowlist.

| Top-level path | Included or excluded | Role and initial inspected scope | Limit or conclusion prevented |
|---|---|---|---|
| `.github/` | Included | Read `.github/workflows/test.yml`: CI dependency installation and test selection. | No CI run evidence inspected; cannot claim CI passed. |
| `.gitignore` | Included | Read ignore rules for experiments, dataset caches, external environments and local baselines. | Ignore rules alone do not establish that an experiment occurred. |
| `LICENSE` | Excluded deliberately | Legal licensing text; README identifies MIT licensing. | No independent legal/licensing assessment. |
| `README.md` | Included | Read all documentation: architecture, entry points, dependencies, invocation, artifact layout and prototype status. | Design and reported operation only; paper and reported gains are not verified. |
| `constraints/` | Included | Tree identifies `openhands-1.31.0.lock.txt` and `terminal-bench.lock.txt`; dependency-lock role traced through `pyproject.toml` and README. Lock contents not yet inspected. | No exact transitive dependency-tree or installation-reproducibility conclusion yet. |
| `data/` | Included | Read `data/README.md`: external dataset and evaluator acquisition responsibilities. No tracked datasets in the tree. | Dataset contents and upstream evaluator correctness are unavailable here. |
| `docs/` | Excluded deliberately | `docs/figures/build_step.png`, `run_step.png`, `paper_at_glance.png`, `meta_improv_concept_diffs.png`: explanatory figures referenced by README; images not inspected. | No claims from figure-specific examples or visual results. No executable path excluded. |
| `examples/` | Included | Read `examples/toy_tasks.json`: shipped custom-task input and verification scripts. | Not executed; no success evidence. |
| `meta_n/` | Included | Traced `main.py` to `core/evolutionary_orchestrator.py`, `omega.py`, `meta_layer.py`, `archive.py`, `run_persistence.py`; read prompt and bundled-config excerpts. Located native `solver.py`/`agentic_solver.py`, `base_executor.py`, `verified_code.py` and context/safety support. Traced `integrations/benchmark.py` evaluation-to-trace wrapper; located benchmark-specific evaluation entry points in `co_bench.py`, `text_classification.py`, `openevolve.py`, `arc_agi.py`, `swe_bench.py` and `terminal_bench/`. Read `core/external_agents/solver.py` lifecycle and searched backend runner seams. Located all `analysis/` tools and read `analysis/best_of_k.py` summary consumption. | Initial material responsibility tracing, not full function-by-function inspection. Detailed adapter algorithms, guard guarantees, repair behavior and every analysis metric remain for later inspection. These are not access gaps or exclusions. |
| `pyproject.toml` | Included | Read all package metadata, dependencies/extras, console entry point, package-data and test settings. | Does not prove an installed distribution works. |
| `scripts/` | Included | Read `run_agentic_stage2_cobench.sh`; searched shipped `run_agentic_stage*.sh`, `run_agentic_smoke_openevolve.sh`, `run_tb2_*.sh`, `oh_runner.py`, `t2_runner.py`, `oh_tb_runner.py`, `builtin_tb_runner.py`, `_runner_common.py` for CLI and SDK consumers. Tree identifies setup/install/prepull/reap scripts, `generate_synthetic_sr.py`, and `oh_sandbox/` build inputs. Subprocess runners are included even where comments call them external bridges. | Detailed runner internals, setup/reaping scripts and sandbox build inputs not yet fully inspected. No SDK operation, container isolation or environmental readiness established. |
| `tests/` | Included | Enumerated unit, integration and external-agent tests plus fixtures/goldens. Read `test_persistence_compat.py` excerpt covering summary-schema and archive-rebuild contracts. Located `tests/golden/`, `fixtures/legacy_archive/`, `fixtures/stage1_golden/`, `external_agents/` and subsystem tests as available contract evidence. | Tests were not run; fixtures are not evidence of live provider behavior or campaign results. Remaining tests are available, not an access gap. |

### Dependencies and unavailable evidence

External dependencies include model providers/OpenAI-compatible endpoints, optional OpenHands and Terminus 2/terminal-bench SDKs, Harbor, Docker, benchmark datasets and upstream evaluator packages. Meta-n's wrappers, subprocess drivers, environment provisioning and result parsing are included; upstream implementations and live services are not independently frozen sources in this run (SRC-1, `pyproject.toml`, `README.md`, `data/README.md`, `meta_n/core/external_agents/solver.py`, `scripts/t2_runner.py`). This prevents attributing upstream internals to Meta-n or establishing end-to-end operation from wrapper text alone.

The source tree supplies no complete frozen empirical campaign or model-provider execution trace for this boundary. The README's paper link is not a registered source and was not followed. These limits prevent conclusions about measured improvement, emergent roles in actual runs, causal benefit of depth, external-backend parity in operation, or safety under real generated code. They do not block a source-grounded account of the shipped design and implementation.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/MinnesotaNLP/Meta-n` | b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/meta-n-18c23b6f8bb4/related-systems/MinnesotaNLP--Meta-n`. Implementation: CLI/search/generation/admission; layer consumption; candidate writing and rebuilding; adapter execution; external-agent lifecycle; summary analysis; driver and backend searches as recorded in the coverage table. Doctrine/design: complete README, data README, package metadata, CI and ignore rules; prompt/config and persistence-test excerpts. | Implementation: [CLI](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/main.py), [search](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/evolutionary_orchestrator.py), [persistence](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/run_persistence.py), [layer](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/meta_layer.py). Doctrine/design: [README](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/README.md), [data](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/data/README.md), [prompts](https://github.com/MinnesotaNLP/Meta-n/blob/b7081843d3c7b0e0f418ca10aaf2ccbff856e7f8/meta_n/core/prompts.py). | No checkout access gap identified. Upstream datasets/SDK internals, paper contents, live services and empirical campaign traces are outside the frozen evidence; no end-to-end, performance or causal conclusions from this register. Initial inspected scopes are not an allowlist. |
