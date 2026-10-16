---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SkillLift's shipped skill-improvement framework at commit 599358b4d4c4a27c0e004df8228ab93026600653, with benchmark and host execution outside the available evidence."
run-id: AAS-2026-10-14-skilllift-0f350bf64418-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: "599358b4d4c4a27c0e004df8228ab93026600653"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/walter-mitty-pro/SkillLift
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/skilllift-0f350bf64418/related-systems/walter-mitty-pro--SkillLift
  revision: "599358b4d4c4a27c0e004df8228ab93026600653"
  sha256: null
---

# SkillLift boundary

## Boundary and evidence

This run analyses SkillLift as a model-dependent **builder or improvement plane**: software that generates and revises agent skill packages and their scoring rubrics, rather than the enclosing agent that executes the benchmark task. The intended use is to characterize the shipped improvement mechanism, retained state, admission checks and paths that consume that state. It is not to establish benchmark superiority or observed deployment reliability.

The target is in scope because its shipped runners create model clients for rubric planning, skill editing and verification, then connect them to a portfolio evolution coordinator. This is not merely a deterministic patch library. SRC-1, `skilllift_eval/runners/skilllift_wildclaw.py` and `skilllift_eval/runners/skilllift_skillsbench_tasks.py` supply implementation evidence for that classification. The coordinator declares its responsibilities as follows:

> Extends the task-portfolio state machine with the SkillLift protocol:
> Mode A refines candidate branches with a rubric verifier (zero oracle calls),
> Mode B aligns the verifier ranking with the oracle ranking and revises the
> receipt. Benchmark differences stay in the injected adapter/planner/generator.
> --- `skilllift/skilllift/coordinator/modes.py`

The model-dependent edit path is explicit in SRC-1, `skilllift_eval/runners/bounded_edits_skill_generator.py`:

> raw = self.client.call_text(
>             system,
>             user,
>             temperature=0.0,
>             response_format=_response_format_for(
>                 self.client,
>                 response_format(contract),
>             ),
>             max_completion_tokens=self.max_completion_tokens,
>         )
> --- `skilllift_eval/runners/bounded_edits_skill_generator.py`

The functional boundary includes the algorithm core; prompts and model-call plumbing; portfolio representation, patch validation and persistence; seed loaders; benchmark adapters; shipped CLI and batch drivers; recovery, audit, budget and token-accounting code; baseline implementations; and evaluation/test contracts. Callers and drivers in this repository are part of the target, not excluded applications. In particular, the domain-level tau2 training, fusion and held-out consumption path is included even though the root README foregrounds two other benchmarks. Its shipped driver imports training, rubric revision, fusion and held-out evaluation functions (SRC-1, `scripts/skilllift_tau2_run_domain.py`); the runner validates and reloads retained MASTER_SKILL content (SRC-1, `skilllift_eval/runners/skilllift_tau2.py`). Available but not initially inspected code remains eligible evidence at this same commit.

Initial tracing establishes these shipped paths:

| Path | Responsibilities traced | Evidence |
|---|---|---|
| WildClawBench task improvement | CLI selects the SkillLift runner; runner creates clients, adapter and store; coordinator loads public task and seed, initializes or reloads state, evolves, freezes the final portfolio and requests final trials; adapter submits the portfolio to the shipped WildClaw runner. | SRC-1: `skilllift_eval/cli.py`, `skilllift_eval/runners/skilllift_wildclaw.py`, `skilllift/skilllift/coordinator/task.py`, `skilllift/skilllift/coordinator/modes.py`, `skilllift/skilllift/adapters/wildclawbench.py`; repository searches also identify the local `skilllift_eval/runners/wildclaw_engine/run_batch.py` consumer. |
| SkillsBench task improvement | Task runner creates model clients and the same portfolio coordinator; adapter reads task.md and native seed skills, deploys the candidate, invokes the benchmark command and checks deployment/loading receipts before committing reward. | SRC-1: `skilllift_eval/runners/skilllift_skillsbench_tasks.py`, `skilllift_eval/runners/skillsbench_portfolio_adapter.py`, `skilllift_eval/runners/skillsbench_adapter.py`. |
| SkillsBench category training/testing | A separate CLI path and runner expose category training, round markers, final-skill output and later testing; not assumed identical to the task-portfolio path. | SRC-1: `skilllift_eval/skillsbench_cli.py`, `skilllift_eval/runners/skilllift_skillsbench.py` (initial function/call-site search, not full behavioral inspection). |
| Retained portfolio reuse | Store initialization checks seed/configuration fingerprints; accepted patches reconstruct the parent on re-entry; final portfolios are frozen and hash-checked. | SRC-1: `skilllift/skilllift/portfolio/store.py`. |
| tau2 domain skills | Shipped driver supplies training/fusion/test functions; training runner evaluates clusters and writes artifacts; held-out loader checks the retained master skill against its bundle and hash. | SRC-1: `scripts/skilllift_tau2_run_domain.py`, `skilllift_eval/runners/skilllift_tau2.py` (selected implementation ranges). |

Retained content is not only an output file: the store reconstructs an accepted parent from previously recorded candidates. SRC-1, `skilllift/skilllift/portfolio/store.py`:

> for index, accepted in enumerate(state.get("accepted_candidates", [])):
>             record = self.load_candidate(task_id, int(accepted["round_index"]), accepted["candidate_id"])
>             if record is None:
>                 raise PersistenceError(f"accepted candidate record is missing: {accepted}")
>             current = self.materialize_candidate(current, record, workspace / f"accepted-{index:03d}")
> --- `skilllift/skilllift/portfolio/store.py`

The boundary kind is **complete artifact, partial loop**, not whole-system. The frozen evidence is the main repository artifact at the acquired commit; its two benchmark gitlinks are present, but their working directories have no source files. Their referenced commits are metadata, not additional registered sources. No submodule was fetched. The main repository's wrappers, local WildClaw execution engine and injection patch remain in scope; they must not be mistaken for evidence of the unavailable benchmark tasks, graders or host implementations. The target itself explains why these missing components matter (SRC-1, `README.md`):

> The benchmark submodules are lightly patched forks of their upstreams (skill-injection hooks,
> seed-skill declarations, harness hardening) required to run skill evolution end-to-end; see each
> fork's git log for the exact deltas.
> --- `README.md`

External dependencies include model endpoints, Docker/container images, benchmark data and host runtimes such as OpenClaw and OpenHands. The tau2 driver also expects a sibling tau2-bench installation that is not part of the tracked artifact. These gaps prevent end-to-end conclusions about actual seed/task contents, host skill loading, grader correctness, environment isolation and execution outcomes. Host scheduling, tool execution and host memory behavior are not attributed to SkillLift. No target program, tests or model services were executed. Absent execution traces prevent claims of observed operation or causal validation. README result claims and checked-in figure data can support attributed reported results, not independently reproduced performance.

### Repository coverage and inspection status

This table accounts for every top-level tracked entry. “Included; not yet inspected” is neither an exclusion nor an access gap. Rows describe the functional coverage intended for later jobs, not an assertion that every file was read for this boundary.

| Top-level entry | Boundary status and material paths | Role / limit |
|---|---|---|
| `.env.example` | Included; not yet inspected | Endpoint/environment setup; no inference about live secrets or configured services. |
| `.gitignore` | Excluded; deliberate | Version-control housekeeping; no conclusions about ignored run artifacts. |
| `.gitmodules` | Included; inspected | Benchmark dependency declarations; gitlink metadata does not provide benchmark source. |
| `CITATION.cff` | Excluded; deliberate | Citation metadata; no authorship or publication-history analysis. |
| `LICENSE` | Excluded; deliberate | Legal text; no licensing assessment. |
| `README.md` | Included; inspected | Declared mechanism, launch paths, dependencies and reported evaluation; performance is attributed, not observed. |
| `WildClawBench` | Unavailable source behind tracked gitlink | Tasks, native skills, assets and benchmark grading; prevents verification of these responsibilities at referenced submodule commit. |
| `skillsbench` | Unavailable source behind tracked gitlink | Tasks, native skills, benchmark harness and deterministic verifiers; prevents verification of these responsibilities at referenced submodule commit. |
| `assets` | Included; not yet inspected: `figures/*` | Method/result illustrations; images alone cannot establish execution or causality. |
| `configs` | Included; not yet inspected: `skillsbench/tasks.yaml`, `skillsbench/domains/*.yaml` | Task/domain launch controls. |
| `packages` | Included: `bounded-edits/src/bounded_edits/{contract,documents,engine,diff,transport}.py`, adapters, tests, packaging and README | Supporting edit-validation mechanism; README and consuming generator initially inspected, package implementation/tests not yet inspected. |
| `scripts` | Included: benchmark batch/launch drivers, `oh_skill_patch.py`, `lib/run_retention.sh`, tau2 train/evolve/domain drivers, figure generator and prewarm code | Shipped callers, injection, maintenance and reporting. Initially inspected `run_skilllift.sh` and selected `skilllift_tau2_run_domain.py` ranges; other paths not yet inspected. The script named run_skilllift.sh actually launches coevoskills, so filenames are not method identity evidence. SRC-1, `scripts/run_skilllift.sh`. |
| `skilllift` | Included: `skilllift/coordinator/`, `portfolio/`, `adapters/`, rubricator, verifier, oracle, persistence, prompts, model clients/configuration, schemas, baselines; `coevoskills/`; packaging, eval shim, scripts and tests | Core improvement and retained-state machinery, comparison methods and compatibility/entry paths. Initial implementation inspection covers selected coordinator, store and WildClaw adapter ranges; README and pyproject inspected. Other material remains in scope and not yet inspected. |
| `skilllift_eval` | Included: CLI, runners, local `runners/wildclaw_engine/`, benchmark public/feedback views, skill loaders, resume, metrics, schemas, budgets, algorithm profiles and human skills | Produces and consumes state, calls benchmark environments and records evaluation. Initial inspection covers selected CLI, SkillLift runners/adapters and generator ranges; other material, including local engine internals, audit and human-skill contents, not yet inspected. |
| `tests` | Included; not yet inspected: `skilllift_eval/test_*.py`, fixtures | Shipped evaluator/runner/retention contracts; unexecuted tests are implementation/design evidence, not passing-run evidence. |

The frozen revision and applicability cutoff are respectively `599358b4d4c4a27c0e004df8228ab93026600653` and **2026-10-14**. The cutoff is the supplied run date, not a claim that later changes were reviewed. The overall tier is **code-grounded** because executable entry-point, model-call, retention and consumption paths were inspected; individual documentation and result claims retain their weaker evidence layer.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/walter-mitty-pro/SkillLift` | 599358b4d4c4a27c0e004df8228ab93026600653 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/skilllift-0f350bf64418/related-systems/walter-mitty-pro--SkillLift`. Implementation: tracked tree and gitlinks; selected ranges in CLI, WildClaw runner/adapter, task and mode coordinators, portfolio store, bounded-edit generator, SkillsBench task runner/portfolio adapter/command builder, tau2 driver and training/master-skill loader. Function/call-site searches additionally trace category SkillsBench runner and local WildClaw engine dispatch. Doctrine/design: root README, skilllift README, skilllift pyproject, gitmodules, selected bounded-edits README. Reported operation: root README's attributed result narrative only. Listed paths record initial inspection, not an allowlist. | Implementation: [CLI](https://github.com/walter-mitty-pro/SkillLift/blob/599358b4d4c4a27c0e004df8228ab93026600653/skilllift_eval/cli.py), [mode coordinator](https://github.com/walter-mitty-pro/SkillLift/blob/599358b4d4c4a27c0e004df8228ab93026600653/skilllift/skilllift/coordinator/modes.py), [store](https://github.com/walter-mitty-pro/SkillLift/blob/599358b4d4c4a27c0e004df8228ab93026600653/skilllift/skilllift/portfolio/store.py), [SkillsBench task runner](https://github.com/walter-mitty-pro/SkillLift/blob/599358b4d4c4a27c0e004df8228ab93026600653/skilllift_eval/runners/skilllift_skillsbench_tasks.py), [tau2 runner](https://github.com/walter-mitty-pro/SkillLift/blob/599358b4d4c4a27c0e004df8228ab93026600653/skilllift_eval/runners/skilllift_tau2.py). Doctrine/design and reported operation: [README](https://github.com/walter-mitty-pro/SkillLift/blob/599358b4d4c4a27c0e004df8228ab93026600653/README.md). | Implementation: unpopulated benchmark submodules and unregistered tau2/host/container/provider implementations prevent end-to-end source verification beyond the main repository adapters. Doctrine/design: declared behavior does not prove implementation equivalence. Reported operation: no supplied execution artifacts or controlled interventions establish reproduced results or causal effects. |
