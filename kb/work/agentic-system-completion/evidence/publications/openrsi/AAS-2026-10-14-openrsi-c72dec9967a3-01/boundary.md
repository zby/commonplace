---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenRSI's shipped OpenMLE task-building, training and search stack at commit 71ae803a035d5e3b78c19fa49ed9f67d0550cbaa."
run-id: AAS-2026-10-14-openrsi-c72dec9967a3-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/FrontisAI/OpenRSI
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/openrsi-c72dec9967a3/related-systems/FrontisAI--OpenRSI
  revision: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
  sha256: null
---

# OpenRSI boundary

## Boundary and evidence

This run examines the OpenMLE implementation shipped by OpenRSI: construction of executable machine-learning tasks, production and selection of training experience, operator training, and test-time program search and evaluation. Its intended use is to establish the stack's source-native control and retained-state mechanisms, not to reproduce its benchmark scores or establish general recursive self-improvement.

The target is a **builder or improvement plane**. Model-dependent program generation is central rather than incidental: the search solver constructs separate model clients for Draft, Improve, Debug, Crossover and Analyze, then binds them to operators. The boundary is **whole-system** at the source-release level, covering the separately runnable stages and their shipped drivers, vendored runtimes, prompts, evaluators, persistence and consumers. It is not a claim that one autonomous process closes the entire task-building-to-model-training-to-search cycle. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `README.md`.

> OpenRSI contains several independently runnable stages rather than one synthetic top-level command.
> --- `README.md`

> draft_llm = GenericLLM(self.cfg.operators["draft"])
> improve_llm = GenericLLM(self.cfg.operators["improve"])
> debug_llm = GenericLLM(self.cfg.operators["debug"])
> crossover_llm = GenericLLM(self.cfg.operators["crossover"])
> analyze_llm = GenericLLM(self.cfg.operators["analyze"])
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

### Frozen evidence and coverage

The sole frozen source is SRC-1 at full commit `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`; the checkout HEAD was checked against the supplied acquisition object. The applicability cutoff is **2026-10-14**, not a claim about subsequent revisions or live services. Overall evidence is **code-grounded**. Repository documentation supplies declared design and attributed operational claims; reading it does not establish observed execution or causal experiments.

Every top-level tracked entry is classified below. Included directories remain available for later analysts to inspect at this same commit. Initial inspection traced representative shipped entry points and state transitions; it is not a line-by-line audit. Available but unread files are not access gaps.

| Top-level tracked entry | Treatment | Material paths and responsibility | Initial inspection and limit |
| --- | --- | --- | --- |
| `LICENSE` | Excluded from operational analysis | Release licensing | Tree identified; text not inspected. No legal-permission conclusion. |
| `NOTICE` | Included as provenance context | Third-party attribution | Tree identified; text not yet inspected. No dependency-license assessment. |
| `README.md` | Included | Release identity, stage relationships, entry points and external-artifact map | Read completely; doctrine/design and reported results only. |
| `OpenMLE-Gym/` | Included | `openmle_gym/cli.py`, `build.py`, `task_worker.py`; `builder_core/main.py`, `design.py`, `utils/` and prompts; `metadata_pipeline/`; task preparation, local metric validation/evaluation, examples and tests; `openmle-sandbox/` controller, router, dispatcher and scoring worker | CLI dispatch traced into process worker and graph construction. Graph includes download, perception/tools, description, preparation and metric stages. Sandbox architecture, dispatcher lifecycle symbols and worker metric loading inspected. Metadata tools, graph node internals, router/API internals and complete example artifacts remain available, not fully inspected. No observed production-service reliability conclusion. SRC-1, `OpenMLE-Gym/openmle_gym/cli.py`, `OpenMLE-Gym/openmle_gym/build.py`, `OpenMLE-Gym/openmle_gym/task_worker.py`, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/openmle-sandbox/README.md`, `OpenMLE-Gym/openmle-sandbox/node_workers/read_and_metric.py`. |
| `OpenMLE-ERL/` | Included | `SFT/scripts/` collection and selection drivers; `SFT/tts_search/` generation, persistence and data production; `SFT/third_party/aira-evo/`; `SFT/slime_scripts/` and vendored `SFT/slime/`; `RL/scripts/`, training wrappers, generation/reward hooks, Program Database, prompts, async rollout and configuration | SFT rollout launcher, selection pipeline, trainer arguments and vendored training loop inspected. RL synchronous launcher hook wiring, wrapper and reward-side database admission/snapshot code inspected. Async implementations and detailed selection/prompt/database internals remain available for analyst inspection. RL's upstream SLIME runtime is an external dependency, not automatically identical to the vendored SFT copy. SRC-1, `OpenMLE-ERL/SFT/scripts/run_evolutionary_rollout.sh`, `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`, `OpenMLE-ERL/SFT/slime/train.py`, `OpenMLE-ERL/RL/README.md`, `OpenMLE-ERL/RL/train_with_patch.py`, `OpenMLE-ERL/RL/generate_mle.py`. |
| `OpenMLE-Evo/` | Included | `scripts/` MLE-Bench, NatureBench and local drivers; `tts_search/` guidance, adapters and configs; `third_party/aira-evo/examples/` task builders and runners; `third_party/aira-evo/src/dojo/` search, operators, prompts, journals, experience, interpreters and evaluation; `skills/`, benchmarks and tests | Both benchmark adapter entry points traced to shipped task builders and runner. Runner resume checks, solver model binding, journal save/reload and selection of related memory nodes inspected; one experience-aware improvement prompt inspected. Local runner, all skills, async scheduler details, task/evaluator internals and test assertions are included but not yet fully inspected. These are shipped consumers, not excluded hosts. SRC-1, `OpenMLE-Evo/scripts/evaluate_airaevo.py`, `OpenMLE-Evo/scripts/evaluate_naturebench.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml`. |
| `assets/` | Excluded | Figures, logos and branding | Tree inspected only. No inference from visual results charts or diagrams beyond inspected textual evidence. No executable responsibility identified in the tracked tree. |
| `docs/` | Included for textual evidence; audiovisual assets excluded | `release.md`, `training.md`, `results.md`, `index.html`; images/video/favicon are presentation material | `release.md` read completely; other textual pages available but not yet inspected. No conclusions from uninspected tables or video demonstrations. SRC-1, `docs/release.md`. |

### State-loop inclusions

The Gym CLI is not merely an API wrapper outside the target: it invokes task building, metadata overview, metric checks and evaluation. Its worker dispatches those operations and writes machine-readable results. The graph and generated task packages are therefore inside the boundary, as are the sandbox's scoring and lifecycle mechanisms. SRC-1, `OpenMLE-Gym/openmle_gym/cli.py`, `OpenMLE-Gym/openmle_gym/task_worker.py`, `OpenMLE-Gym/builder_core/design.py`.

Experience production and its training consumers are also included. The SFT pipeline collects scored rows, applies token and validation/test-gap filters, selects per-task examples and writes an alignment dataset. Its training launcher consumes prompt data through an SFT rollout function. The RL generation/reward module conditionally admits programs into its database and exposes database snapshots. These source paths authorize analysis of the mechanisms, not a claim that the released corpora or checkpoints were regenerated here. SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`, `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`, `OpenMLE-ERL/RL/generate_mle.py`.

The inference side includes persistence and later use, not just operator APIs. The solver saves and reconstructs its journal, gathers related memory nodes and ensures their summaries before operator use. Shipped prompt templates explicitly consume this memory. Both benchmark adapters write configurations and launch a shipped runner; that runner checks retained outputs for resume. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/runner.py`.

> self.journal = Journal.from_export_data({"nodes": journal_export})
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> Use horizontal sibling memory to avoid repeating nearby failed alternatives and to borrow useful details.
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/configs/solver/operators/mlebench/aira_operators/improve_experience.yaml`

### External dependencies and prevented conclusions

Model serving and weights, full training corpora and historical checkpoints, the separate OpenMLE Tasks release, upstream benchmark environments and datasets, credentials, and deployment-specific infrastructure are outside this frozen source. Repository-bundled smoke packages, evaluation tools and source-native example reports remain in scope; they do not stand in for the full external releases. The pinned RL SLIME dependency documented by the project has not been acquired into this evidence set. No second repository, model card, paper, web page or live endpoint is registered. SRC-1, `docs/release.md`, `OpenMLE-ERL/RL/README.md`.

> Training corpora, model weights, checkpoints, service credentials, private infrastructure configuration, generated outputs, and deployment-specific endpoints are deliberately kept outside this code repository.
> --- `docs/release.md`

Those gaps prevent verification of historical training lineage, exact numerical reproduction, full task-release coverage and deployed service behavior. A source-level whole-system boundary does not establish that external dependencies work together in any particular deployment. The target, tests and examples were not executed; no fresh observed-run or causal-experiment evidence is claimed. Source-native reports of runs can be examined later as attributed evidence under their actual retained conditions.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/FrontisAI/OpenRSI` | 71ae803a035d5e3b78c19fa49ed9f67d0550cbaa | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/openrsi-c72dec9967a3/related-systems/FrontisAI--OpenRSI`. Implementation: Gym CLI/build/worker/graph, sandbox dispatcher symbol trace and metric worker; SFT launcher, data-production pipeline and vendored training loop; RL launcher, wrapper and generation/reward storage; Evo benchmark drivers, runner resume logic, solver initialization/journal/memory preparation and experience prompt. Doctrine/design: root README, release map, SFT/RL READMEs, sandbox architecture and inspected prompt. Reported operation: root README benchmark claims and RL README validation status, not independently verified. | Implementation: [Gym CLI](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Gym/openmle_gym/cli.py), [SFT pipeline](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py), [RL generation/reward](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-ERL/RL/generate_mle.py), [Evo solver](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py). Doctrine/design: [release boundary](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/docs/release.md). Reported operation: [README](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/README.md), [RL status](https://github.com/FrontisAI/OpenRSI/blob/71ae803a035d5e3b78c19fa49ed9f67d0550cbaa/OpenMLE-ERL/RL/README.md). Additional initially inspected paths are recorded in the coverage table and prose above. | Frozen Git source available read-only. External weights, full datasets/corpora, upstream RL framework, benchmark installations and historical/deployed infrastructure are not captured: no exact reproduction, historical provenance verification or deployment validation. No target execution undertaken; reported operation is not observed operation or causal attribution. |
