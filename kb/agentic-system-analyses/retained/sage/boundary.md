---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SAGE's shipped training, skill-library agent, evaluation and SFT patches at commit 3c9244e82244abb1adc5467ee601a03ba0f433a0."
run-id: AAS-2026-10-15-sage-d0de15ae5730-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "3c9244e82244abb1adc5467ee601a03ba0f433a0"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/amazon-science/SAGE
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-amazon-science-sage/related-systems/amazon-science--SAGE
  revision: 3c9244e82244abb1adc5467ee601a03ba0f433a0
  sha256: null
---

# SAGE boundary

## Boundary and evidence

SAGE is in scope as a **builder or improvement plane**: it trains a model through skill-augmented agent rollouts and ships the corresponding task-solving agent and data-generation paths. The intended analysis covers how reusable Python functions are produced, admitted, retained and consumed during training and evaluation, alongside how rollout rewards feed model updates. This is a whole-system boundary over the shipped SAGE repository, not merely its skill-extraction API. AppWorld callers, prompts, evaluators and SFT patches supplied in this repository are included even though installation overlays some of them onto external repositories (SRC-1, `README.md`, `sage/run_sage_2nodes.sh`, `patches/appworld/experiments/code/skill_library_agent/agent.py`).

The source declares its identity and training mechanism:

> This repository contains the official implementation of **SAGE (Skill Augmented GRPO for self-Evolution)**, introduced in our paper [Reinforcement Learning for Self-Improving Agent with Skill Library](https://arxiv.org/pdf/2512.17102).
> --- `README.md`

The shipped RL launcher calls `verl.trainer.main_ppo`; that entry point constructs `RayPPOTrainer`, initializes its workers and calls `fit`. The trainer imports the AppWorld generation manager, feeds generated rewards into advantage computation and calls the actor update. This establishes model-dependent operation, rather than a passive function store (SRC-1, `sage/run_sage_2nodes.sh`, `sage/verl/trainer/main_ppo.py`, `sage/verl/trainer/ppo/ray_trainer.py`).

> actor_output = self.actor_rollout_wg.update_actor(batch)
> --- `sage/verl/trainer/ppo/ray_trainer.py`

The training loop and evaluation loop are both included, but their retention mechanisms must not be conflated. Training initializes skill dictionaries for a rollout and passes them across two subtask iterations. The batch environment extracts functions from non-failing execution output on the first subtask, then executes and supplies retained functions in the second subtask's prompt. Evaluation instead keeps an agent-level function list, appends function records to JSONL, optionally saves embeddings, and can load a separately located predefined library on construction. The analysis must distinguish in-process reuse, output persistence and predefined-library loading; these paths alone do not establish automatic restart recovery from evaluation output (SRC-1, `sage/llm_agent/appworld_generation.py`, `sage/llm_agent/app_world/app_world_env.py`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`).

> skill_libraries = [{} for _ in range(len(gen_batch["task_ids"])//2)]
> skill_counts = [0 for _ in range(len(gen_batch["task_ids"])//2)]
> for subtask_iter in range(2):
> --- `sage/llm_agent/appworld_generation.py`

> if os.path.exists("./predefined_skill_library/skill_library_functions.jsonl"):
> --- `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`

The evaluation config selects the skill-library agent. Its shipped runner constructs one agent and calls `solve_tasks`; the base agent executes generated code, evaluates tasks and invokes skill extraction when configured. Expert generation adds scenario rollouts, verification and dataset extraction, with SFT configuration consuming the resulting dataset. These are included state producers and consumers, not excluded applications (SRC-1, `patches/appworld/experiments/configs/sage_test_normal.jsonnet`, `patches/appworld/experiments/code/skill_library_agent/run.py`, `patches/appworld/experiments/code/skill_library_agent/agent.py`, `patches/appworld/extract_expert_dataset.py`, `patches/LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml`).

Prompts are part of the mechanism, not independent evidence that every requested property is enforced:

> (3) If no suitable function exists in the skill library, you should define a new function first and then call it to complete the step.
> --- `patches/appworld/experiments/prompts/skill_library_agent.txt`

### Shipped-path coverage

The tracked tree was enumerated at the frozen commit. Included directories below remain within the evidence boundary in full; named paths document the material responsibilities initially traced, not an allowlist. “Not yet inspected” is not an access gap.

| Top-level tracked path | Classification and material paths | Role and coverage limit |
|---|---|---|
| `README.md` | Included; inspected | Declared algorithm, installation, training, evaluation and SFT entry points. Supports intent, not successful execution. |
| `sage/` | Included; inspected `run_sage_2nodes.sh`, `verl/trainer/main_ppo.py`, selected generation/update portions of `verl/trainer/ppo/ray_trainer.py`, rollout coordination in `llm_agent/appworld_generation.py`, and the full `llm_agent/app_world/app_world_env.py` | RL launch, model orchestration, function production/admission, cross-subtask consumption and environment reward interface. Tree/search also located `run_sage_4nodes.sh`, trainer configs, checkpoint save/load methods, model workers, datasets and vendored execution infrastructure. These remain included but implementation details not yet read cannot support detailed backend, checkpoint-correctness or alternate-launch claims. |
| `patches/` | Included; inspected `appworld/src/appworld/cli.py` run/evaluate dispatch, `appworld/experiments/configs/sage_test_normal.jsonnet`, `appworld/experiments/code/skill_library_agent/run.py`, `agent.py`, and skill loading/retrieval/generation/save portions of `skill_library_agent.py`; full `appworld/experiments/prompts/skill_library_agent.txt`; `appworld/expert_dataset_generation_claude.sh`, `appworld/extract_expert_dataset.py`; `LLaMA-Factory/run_sft.sh` and `LLaMA-Factory/examples/train_full/qwen2_5_32B_appworld.yaml` | Evaluation and expert-generation callers, skill persistence and later consumption, prompt-level function rules, output-to-SFT dataset conversion and SFT launch. Tree/search located rollout-specific agent/prompt/config, scenario lists, API prediction/reflexion helpers, logging/model adapters, SFT supervised processor and data arguments. These remain included; unread details require later inspection before claims about those branches. |
| `algorithm_preview.png` | Included as declared design illustration; not yet inspected | No independent visual or algorithmic claim is drawn from the image; the README's description is not a substitute for inspecting it. |
| `CODE_OF_CONDUCT.md` | Deliberately excluded | Community governance; no conclusion about conduct obligations or enforcement. |
| `CONTRIBUTING.md` | Deliberately excluded | Contribution/security-reporting policy; no conclusion about security review or vulnerability handling. |
| `LICENSE` | Deliberately excluded | Legal terms; no licensing or permitted-use conclusion. |
| `THIRD-PARTY-NOTICES` | Deliberately excluded | Attribution/legal notices; no dependency-license completeness conclusion. |

### Dependencies and evidence limits

The frozen revision is `3c9244e82244abb1adc5467ee601a03ba0f433a0`; the applicability cutoff is 2026-10-15, taken from the supplied run date, not a claim about when this commit was authored. The acquired checkout's HEAD matches the pin and its working tree reports no changes. Overall evidence is **code-grounded**, with README and prompts supplying doctrine/design. No target execution was performed; no observed-run or causal-experiment layer is established.

Upstream AppWorld and LLaMA-Factory implementations are external dependencies, not additional frozen sources. The README identifies upstream checkout revisions, but those references do not register their contents here. AppWorld supplies the environment, task data and underlying evaluator; SAGE supplies the inspected orchestration and patches. Missing upstream implementation evidence prevents conclusions about sandbox isolation, benchmark-test adequacy and full patched-install compatibility. SFT's upstream training machinery is likewise not attributable to SAGE's patches (SRC-1, `README.md`, `patches/appworld/src/appworld/cli.py`, `patches/LLaMA-Factory/run_sft.sh`).

Model weights, downloaded AppWorld data, predefined skill-library files, hosted model responses and generated experiment outputs are not frozen in this source set. Their absence prevents conclusions about actual learned competence, library quality, empirical reuse benefits, achieved evaluation scores or reproducibility on particular hardware. The shipped code is evidence for what the implementation attempts, not for successful training or causal improvement. Ray, PyTorch, vLLM, model-provider adapters and retrieval models are runtime dependencies; only their shipped integration code falls within SRC-1. The linked paper and linked external repositories have not been acquired and supply no separate evidence in this run (SRC-1, `README.md`, `sage/run_sage_2nodes.sh`, `patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/amazon-science/SAGE` | 3c9244e82244abb1adc5467ee601a03ba0f433a0 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-amazon-science-sage/related-systems/amazon-science--SAGE`. Implementation: launcher, PPO entry point and selected trainer paths, AppWorld rollout coordination and batch environment; evaluation CLI dispatch, runner, base agent, skill-library agent loading/retrieval/save paths; expert-generation launcher and dataset extraction; SFT launcher/config. Doctrine/design: README and full evaluation/training skill-library prompt. Unread included branches are identified in coverage above. | Implementation: [RL launcher](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/run_sage_2nodes.sh), [trainer](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/verl/trainer/ppo/ray_trainer.py), [batch environment](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/sage/llm_agent/app_world/app_world_env.py), [evaluation agent](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/code/skill_library_agent/skill_library_agent.py), [expert extraction](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/extract_expert_dataset.py). Doctrine/design: [README](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/README.md), [prompt](https://github.com/amazon-science/SAGE/blob/3c9244e82244abb1adc5467ee601a03ba0f433a0/patches/appworld/experiments/prompts/skill_library_agent.txt). | No access gap in the registered checkout was encountered. Upstream dependency contents, model/data artifacts and actual runs are outside the frozen source set: no independent environment/evaluator audit, compatibility demonstration, achieved-performance claim or causal-benefit conclusion. |
