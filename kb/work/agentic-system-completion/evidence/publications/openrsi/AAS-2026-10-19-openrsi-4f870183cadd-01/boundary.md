---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenRSI's shipped OpenMLE improvement stack at commit 71ae803a035d5e3b78c19fa49ed9f67d0550cbaa, with external training and deployment artifacts outside the evidence boundary."
run-id: AAS-2026-10-19-openrsi-4f870183cadd-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/FrontisAI/OpenRSI
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-openrsi/related-systems/FrontisAI--OpenRSI
  revision: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
  sha256: null
---

# OpenRSI boundary

## Boundary and evidence

This run analyses OpenRSI's shipped OpenMLE implementation: task construction and evaluation, supervised trajectory production and training, execution-grounded reinforcement learning, and test-time program evolution. Its intended use is to explain how these components produce, retain and consume executable research experience, and where their handoffs depend on external systems. It is not an analysis of all future routes proposed by the OpenRSI initiative or a verification of general recursive self-improvement.

**Classification: builder or improvement plane.** OpenRSI qualifies as an agentic target because the release constructs model-driven task-building and program-evolution workflows and supplies training paths for the operators used by those workflows. It is not merely a dataset or a returning scoring function. The target's own description bounds its ambition (SRC-1, `README.md`):

> OpenRSI begins with Meta-Evolution—training the improver itself in bounded, executable domains—without claiming that general recursive self-improvement has been solved.
> --- `README.md`

The classification includes the shipped drivers, not just the APIs they invoke. In Gym, `openmle-task` dispatches to task construction and evaluation; the construction worker compiles and invokes the LangGraph builder. In Evo, the evaluation driver writes task/runner configuration and launches the vendored AIRA task builder and runner. The per-task runner constructs the evolutionary solver and restores its state. These are responsibilities of the target, not excluded enclosing applications (SRC-1, `OpenMLE-Gym/pyproject.toml`, `OpenMLE-Gym/openmle_gym/cli.py`, `OpenMLE-Gym/openmle_gym/build.py`, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Evo/scripts/evaluate_airaevo.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`). Representative executable anchors establish both orchestration and model-operator construction:

> result = await app.ainvoke(agent)
> --- `OpenMLE-Gym/openmle_gym/build.py`

> solver = Evolutionary(solver_cfg, task_info=task_info)
> solver.load_checkpoint()
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

> draft_llm = GenericLLM(self.cfg.operators["draft"])
> improve_llm = GenericLLM(self.cfg.operators["improve"])
> debug_llm = GenericLLM(self.cfg.operators["debug"])
> crossover_llm = GenericLLM(self.cfg.operators["crossover"])
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

The solver's checkpoint methods serialize and restore its journal; retained search state is therefore within scope, not treated as an external memory service (SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`). Shipped prompts, skill guidance, experience maintenance, configuration, evaluators, sandbox controller/router/worker code, training launchers and vendored implementations are also within the functional target, even where not yet inspected below.

**Boundary kind: complete artifact, partial loop.** The frozen artifact is the repository at the full commit above; HEAD was checked against the acquisition pin. This is not a narrowed Evo-only or library-only analysis. However, initial inspection does not establish complete coverage of every material path, and external inputs and the separately supplied RL training dependency prevent treating the artifact as a self-contained, fully inspected improvement loop. The RL README prescribes an external SLIME checkout, while SFT has its own vendored SLIME. Those must not be silently equated (SRC-1, `OpenMLE-ERL/RL/README.md`, `OpenMLE-ERL/SFT/README.md`, `OpenMLE-ERL/RL/train_with_patch.py`):

> git clone https://github.com/THUDM/slime.git
> cd slime
> git checkout 680824dd5e01a2e83750bf87fc366ec6fa98766c
> --- `OpenMLE-ERL/RL/README.md`

That external revision is a declared dependency, not a second registered or inspected source. The shipped RL wrapper applies patches and executes the surrounding SLIME `train.py`; the SFT launcher passes dataset, loss and checkpoint arguments to its training environment (SRC-1, `OpenMLE-ERL/RL/train_with_patch.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`). These entry points establish integration scope, not the correctness of external optimizer or serving behavior.

### Initial inspection and remaining coverage

The complete tracked tree was enumerated. The table distinguishes initial inspection from material still to trace; it does not exclude uninspected code from SRC-1 or claim whole-system coverage.

| Tracked area | Included role and initial inspection | Remaining coverage or exclusion limit |
| --- | --- | --- |
| `README.md` | Inspected release architecture, operator vocabulary, independent component entry points and dependency declarations. | Intent and reported results are not execution evidence. |
| `OpenMLE-Gym/` | Inspected `pyproject.toml`, `openmle_gym/cli.py` dispatch, `openmle_gym/build.py` worker and `builder_core/design.py` graph. Includes builder nodes/tools/prompts, metadata pipeline, input preparation, local evaluation, example packages and distributed sandbox. | Node internals, metadata/evaluator internals, example data and `openmle-sandbox/` services are available but not yet inspected. No sandbox isolation or task-quality conclusion is established here. |
| `OpenMLE-Evo/` | Inspected `README.md`, `scripts/evaluate_airaevo.py` orchestration, vendored `examples/mle_bench/runner.py` scheduling, `single_task_runner.py` construction/restoration and `src/dojo/solvers/evo/evo.py` checkpoint/operator setup under `third_party/aira-evo/`. Includes `tts_search/`, `skills/`, benchmark adapters, execution profiles and tests. | NatureBench adapters, full standard/async search, experience admission, prompt assembly, skill content, final selection and tests remain to trace. Their presence is not proof of equivalent semantics or reliable operation. |
| `OpenMLE-ERL/` | Inspected component README files, `SFT/scripts/run_evolutionary_rollout.sh`, SFT training argument assembly in `SFT/slime_scripts/common/run_slime_sft.sh`, and `RL/train_with_patch.py`. Includes rollout collection/selection/persistence, vendored SFT runtimes, RL database/reward/rollout logic, configurations and launch modes. | Dataset gates, full training consumers, async wrapper and RL update/restore behavior remain to inspect. External RL SLIME and production checkpoints are not in this evidence set. |
| `docs/` | Inspected `release.md` for artifact and dependency scope; project page, training and results documents are included as target-authored documentation. | Other document bodies and embedded media not yet inspected; no independent result verification follows. |
| `assets/` | Available release figures and branding, not initially inspected. | Deliberately excluded from executable-mechanism evidence; visual or figure-only claims cannot be established from this initial inspection. |
| `LICENSE`, `NOTICE` | Available legal/provenance material, not initially inspected. | Deliberately excluded from functional analysis; no license-compliance or complete dependency-provenance conclusion. |

### Time, dependencies and evidence limits

The applicability cutoff is **2026-10-19**, confined to commit **71ae803a035d5e3b78c19fa49ed9f67d0550cbaa**. No later repository changes, live project pages, linked papers, external repositories or model/dataset releases supply evidence in this run. Listed source paths are initial inspection, not a source allowlist.

Overall evidence is **code-grounded**: inspected executable integration and state-handling code supplies implementation evidence. Target documentation supplies doctrine/design and attributed reported operation. No target execution, reproduction or causal experiment was performed. In particular, the RL README's reported validation and root README benchmark improvements remain author-reported, not observed runs registered by this analysis (SRC-1, `OpenMLE-ERL/RL/README.md`, `README.md`).

External requirements include model weights and serving endpoints, training corpora, task data/packages, benchmark environments, leaderboard/evaluation assets, credentials, cluster/container configuration and deployed sandbox services. The repository includes sandbox implementation, so absence of a deployment is not absence of sandbox source. The excluded external artifacts prevent conclusions about exact training lineage, paper-score reproduction, deployed isolation, operational availability and measured improvement. The release itself states this separation (SRC-1, `docs/release.md`):

> Training corpora, model weights, checkpoints, service credentials, private infrastructure configuration, generated outputs, and deployment-specific endpoints are deliberately kept outside this code repository.
> --- `docs/release.md`

These are evidence limits, not a blocked disposition: the shipped improvement mechanisms can still be analysed from the frozen code. Available-but-uninspected files are coverage work, not access gaps.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/FrontisAI/OpenRSI` | 71ae803a035d5e3b78c19fa49ed9f67d0550cbaa | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-openrsi/related-systems/FrontisAI--OpenRSI`. Implementation: Gym CLI/build worker/graph; Evo evaluation driver, vendored MLE runner, per-task solver construction/restoration and evolutionary checkpoint/operator setup; SFT rollout launcher and training argument assembly; RL synchronous patch wrapper. Doctrine/design: root, Evo, ERL, SFT and RL README files and release scope. Reported operation: root benchmark claims and RL README validation statement, without underlying execution artifacts inspected. Initial coverage is detailed above. | Implementation: [Gym dispatch](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Gym/openmle_gym/cli.py), [builder graph](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Gym/builder_core/design.py), [Evo driver](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Evo/scripts/evaluate_airaevo.py), [solver](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py), [RL wrapper](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-ERL/RL/train_with_patch.py). Doctrine/design: [release boundary](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/docs/release.md). Reported operation: [root README](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/README.md), [RL README](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-ERL/RL/README.md). | Frozen checkout accessible; no repository access gap found. External RL SLIME, weights, corpora, complete task releases and deployed services are outside the registered source; their absence prevents complete optimizer/serving tracing, historical lineage and end-to-end reproduction claims. Uninspected shipped files are not access gaps. Reported-operation passages alone establish neither observed performance nor causal attribution. |
