---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ModularRSI's released harness improvement and evaluation paths at commit b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9."
run-id: AAS-2026-10-18-modularrsi-4218ceff5530-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/IQuestLab/ModularRSI
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-21-fresh-modularrsi/related-systems/IQuestLab--ModularRSI
  revision: b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9
  sha256: null
---

# ModularRSI boundary

## Boundary and evidence

This run analyses the released ModularRSI improvement system, including the modular solver it changes and the shipped drivers that produce, admit, retain and consume its changes. Its primary class is **builder or improvement plane**: the product of the improvement loop is an executable module library, not a new foundation model. The solver is an included execution runtime, not an excluded host. The intended use is to explain the released architecture and its evidence limits, not to reproduce the paper's experiments or independently establish its reported gains.

The boundary is **whole-system** for that functional target. It includes both public launchers, Phase0 orchestration, support-task execution, trajectory investigation, findings and proposals, editor instructions, isolated candidate construction, admission gates, generation/archive maintenance, later module selection, solver execution and evaluation. Generic Harbor facilities used by those paths are included as supporting implementation. Unrelated Harbor product surfaces are not treated as ModularRSI mechanisms merely because this repository ships them.

SRC-1, `README.md`, describes the target's intervention and output:

> Program checks, diff
> review, and execution validation filter proposed changes. Cross-module integration
> then resolves interactions among the evolved modules, and the resulting function
> library is frozen for downstream evaluation.
> --- `README.md`

The classification is also implementation-grounded. `scripts/evolve.sh` invokes `harbor.agents.terminus_2_modular.self_evo.phase0`; Phase0 calls `run_online_evo` with the selected support tasks, module lock and workload. That driver initializes or resumes a generation, launches solver task groups using that generation, accumulates summaries and invokes reflection. After promotion it updates `current_gen`, which subsequent task launches use. These shipped callers are part of the target, not external applications (SRC-1, `scripts/evolve.sh`, `src/harbor/agents/terminus_2_modular/self_evo/phase0.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`). The generation transition is explicit:

> current_gen = outcome.promoted_gen
> n_promotions += _promotion_count(outcome)
> --- `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`

The retained-state loop includes more than Python module files. Candidate lanes consume persisted findings and proposals; promotion moves a candidate into a new generation and attempts archive synchronization. Resume reads `progress.json`; archive status and bundle pins affect later composition. Editor memory records change outcomes and exposes a compact history for editor use. These paths remain included even where persistence is best-effort; inclusion does not assert transactionality or gate effectiveness (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/dual_implement.py`, `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`, `src/harbor/agents/terminus_2_modular/self_evo/online_evo.py`, `src/harbor/agents/terminus_2_modular/self_evo/editor_memory.py`, `src/harbor/agents/terminus_2_modular/composer/llm_dynamic.py`).

> promoted = _staging.atomic_promote(tree, target)
> --- `src/harbor/agents/terminus_2_modular/self_evo/two_lane.py`

The consumption side is shipped too. `scripts/evaluate.sh` supplies `generations/merged_active/gen_0/modules` by default to the `terminus-2-modular` agent through Harbor. The agent shim calls installed orchestration, which loads the selected library, chooses a bundle, instantiates the five strategy modules, executes the agent loop and dumps its trajectory. Evolution's task runner invokes this same agent through `harbor run` and reads trial-level verifier rewards. Thus Harbor's agent factory, trial lifecycle, verifier, model access and environment interface are supporting parts of the in-repository loop rather than responsibilities attributed to an unspecified external host (SRC-1, `scripts/evaluate.sh`, `src/harbor/agents/terminus_2_modular/agent.py`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py`, `src/harbor/agents/factory.py`, `src/harbor/trial/trial.py`).

> library = build_default_library(modules_root=params.get("modules_root"))
> --- `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`

Shipped prompt contracts are included as design evidence, not instructions to this analyst. They distinguish fixed infrastructure from the module-edit surface. A stale or broader comment in another file does not by itself establish what the release permits; later mechanism analysis must resolve such discrepancies against callers and enforcing code (SRC-1, `src/harbor/agents/terminus_2_modular/self_evo/editor_skills/kernel-boundaries/SKILL.md`, `src/harbor/agents/terminus_2_modular/kernel/orchestration.py`).

> The codebase you're editing is split into **Kernel** (fixed plumbing) and
> **Modules** (evolvable strategy). You MAY only modify modules.
> --- `src/harbor/agents/terminus_2_modular/self_evo/editor_skills/kernel-boundaries/SKILL.md`

### Frozen evidence and limits

The sole source is the acquired repository at **b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9**. HEAD was checked against the acquisition pin, and the checkout was inspected read-only. The applicability cutoff is **2026-10-18**, the opening run date; it is not an assertion about when every bundled artifact was produced. No other repository, live website, linked paper or dataset is frozen by this run.

Overall evidence is **code-grounded**. README performance numbers and the trajectory README's descriptions are source-reported operation, not this analyst's measurements. The repository includes sanitized held-out evaluation trajectories, configuration and results; those can support bounded observed-run findings after their contents are inspected. This initial boundary inspected their README and tracked layout, not individual trial contents, and establishes no aggregate empirical finding (SRC-1, `README.md`, `trajectories/mergefinal/README.md`).

External dependencies include the chosen model/provider endpoint and credentials, Docker or E2B infrastructure, support-task datasets, and evaluation tasks resolved locally or through Harbor's registry. Their calling interfaces are included; external service implementations, model weights and remotely supplied task contents are not. This prevents conclusions about provider-side reasoning, sandbox security and the quality or contamination status of unfrozen dataset contents. The public launchers and Phase0 show these dependencies directly (SRC-1, `scripts/evolve.sh`, `scripts/evaluate.sh`, `src/harbor/agents/terminus_2_modular/self_evo/phase0.py`, `src/harbor/agents/terminus_2_modular/self_evo/task_runner.py`).

The released generation is a sanitized library and archive, not an inspectable full training history. The evaluation artifacts omit terminal recordings, per-episode requests and verifier logs. These are evidence limitations, not missing in-repository callers. They prevent reconstructing the complete evolution lineage, independently attributing reported gains to individual changes, or auditing omitted verifier executions. No target code, tests, examples or provider calls were executed (SRC-1, `generations/merged_active/README.md`, `trajectories/mergefinal/README.md`).

### Top-level coverage

The tracked tree was inventoried at the pinned commit. “Included” fixes functional scope; it does not mean every file was read in full in this boundary job. Initial inspection traced the public entry points through improvement and consumption; detailed mechanism inspection remains for later jobs. Uninspected available files are not access gaps. All source-dependent entries below refer to SRC-1 and the named commit-relative paths.

| Top-level tracked path | Treatment and material paths | Role and conclusion limit |
|---|---|---|
| `README.md` | Included; read | Target intent, launcher directions and attributed research claims; not independent performance evidence. |
| `scripts/` | Included; `scripts/evolve.sh`, `scripts/evaluate.sh` read completely | Public evolution and evaluation drivers, including environment and dataset configuration. |
| `src/` | Included for ModularRSI and its supporting Harbor execution paths | `src/harbor/agents/terminus_2_modular/agent.py`, `kernel/orchestration.py`, `composer/llm_dynamic.py`, `self_evo/phase0.py`, `online_evo.py`, `task_runner.py`, `two_lane.py`, `dual_implement.py`, `editor_memory.py` and `editor_skills/kernel-boundaries/SKILL.md` initially inspected in full or bounded sections; factory/trial wiring searched. Scope also includes the remaining modular modules, composer/library/archive/protocol/service code, all self-evolution state, prompts, gates and maintenance, plus CLI/job/trial/verifier/LLM/environment paths they use. Generic authoring, publishing, sharing, authentication administration and unrelated installed agents are deliberately excluded as independent product features; no completeness claim about Harbor as a separate product follows. |
| `generations/` | Included; `generations/merged_active/README.md` and tracked layout initially inspected | Released `archive.json`, `PROVENANCE.json`, and `gen_0/modules/` are retained state consumed by evaluation; individual variant efficacy not established here. |
| `trajectories/` | Included; `trajectories/mergefinal/README.md` and tracked layout initially inspected | Bundled run/task configs, results and ATIF trajectories are admissible evaluation evidence after inspection; not training feedback or a complete training trace. |
| `tests/` | Included as implementation contracts; tree inventoried, not run | Modular archive, composer pin, staging, editor admission, evidence, routing, promotion, rollback and resume tests, plus Harbor execution tests. Assertions are not observed test passes. |
| `pyproject.toml` | Included; entry-point metadata searched | `harbor = "harbor.cli.main:app"` connects task-runner subprocesses to shipped CLI; build/dependency context. |
| `uv.lock` | Included as dependency context; inventoried only | Available dependency pin, not evidence that dependencies were installed or exercised. |
| `.env.example` | Included as public configuration surface; inventoried only | Complements launcher credential/environment inputs; no inference about actual deployed credentials. |
| `.python-version` | Included as interpreter configuration; inventoried only | No runtime-compatibility result claimed. |
| `adapters/` | Deliberately excluded as independent benchmark-conversion workflows | Templates, conversion scripts and parity artifacts do not establish ModularRSI's improvement mechanism; prevents an exhaustive benchmark-adapter/parity assessment. Local/registry task consumption remains included through the driver. |
| `apps/` | Deliberately excluded; `apps/viewer/` UI | Prevents conclusions about browser presentation and viewer behavior, not about solver/evolution state consumption. |
| `assets/` | Deliberately excluded as illustrations and figure data | Prevents treating diagrams, GIFs or plotted data as independently verified execution evidence. |
| `docs/` | Deliberately excluded as the generic Harbor documentation/site | Prevents a complete Harbor documentation or website assessment; target README and in-code/editor contracts remain included. |
| `examples/` | Deliberately excluded as generic Harbor demonstration workloads and agents | Prevents claims that example tasks/configurations work or represent ModularRSI training; public ModularRSI launchers remain included. |
| `packages/` | Deliberately excluded; `packages/rewardkit/` | Prevents a standalone RewardKit implementation assessment; the included task verifier interface does not imply inspection of every optional judging package. |
| `registry.json` | Included as available task-resolution configuration; inventoried only | Registry use is visible in task runner; no assertion about availability or contents of remote task payloads. |
| `rfcs/` | Deliberately excluded; trajectory-format proposal and sample formats | Prevents a historical trajectory-standard design assessment; executable recording and released ATIF files remain included. |
| `skills/` | Deliberately excluded; generic adapter/task/publishing/RewardKit skills | Prevents claims about generic Harbor authoring workflows. ModularRSI's editor skills under `src/` remain included. |
| `skills-lock.json` | Deliberately excluded with generic authoring skills | No skill-installation provenance assessment. |
| `.github/` | Deliberately excluded; CI, labeling and documentation-deployment workflows | No CI success, release automation or hosted-documentation claim. |
| `.gitignore` | Deliberately excluded as repository hygiene | No ignored-file or secret-cleanliness audit. |
| `CHANGELOG.md` | Deliberately excluded as historical release narrative | No version-history assessment outside the pinned implementation. |
| `CITATION.cff` | Deliberately excluded as citation metadata | No independent authorship or publication-metadata verification. |
| `LICENSE`, `LICENSE-MODULARRSI.md` | Deliberately excluded from technical analysis | No legal interpretation or license-compliance conclusion. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/IQuestLab/ModularRSI` | b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-21-fresh-modularrsi/related-systems/IQuestLab--ModularRSI`. Implementation: public launchers, full Phase0 and agent shim, full orchestration, bounded online driver initialization/reflection/gates, candidate brief construction, two-lane selection/promotion, editor memory, dynamic composer selection; factory/trial/entry-point and related evolution files searched. Doctrine/design: root README, released generation README, evaluation-trajectory README and kernel-boundaries editor skill. Reported operation: README research results and release descriptions only. Top-level coverage table distinguishes inventories and exclusions. | [launchers](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/scripts/evolve.sh); [Phase0](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/src/harbor/agents/terminus_2_modular/self_evo/phase0.py); [online evolution](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/src/harbor/agents/terminus_2_modular/self_evo/online_evo.py); [orchestration](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/src/harbor/agents/terminus_2_modular/kernel/orchestration.py); [generation contract](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/generations/merged_active/README.md); [evaluation artifact limits](https://github.com/IQuestLab/ModularRSI/blob/b5c72c36b0d08ff93f00ee202a8fbdebe849dfb9/trajectories/mergefinal/README.md). Other initial anchors are the exact paths in the body and table. | No access failure in the inspected checkout. External model/services, unfrozen datasets/paper and omitted training/verification artifacts prevent provider-internal, full-reproduction and causal-gain conclusions. Available but initially unread source and bundled individual trials are not access gaps. No observed-run or causal-experiment finding is established by this boundary; later inspection of bundled traces may establish bounded observed-run evidence under this same source ID. |
