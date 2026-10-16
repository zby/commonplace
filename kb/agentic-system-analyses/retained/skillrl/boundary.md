---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "SkillRL's shipped skill-generation, skill-conditioned agent training and recursive skill-update paths at frozen commit 4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d."
run-id: AAS-2026-10-14-skillrl-0dba0e1c895e-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: whole-system
reviewed-boundary: "4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/aiming-lab/SkillRL
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/skillrl-0dba0e1c895e/related-systems/aiming-lab--SkillRL
  revision: 4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d
  sha256: null
---

# SkillRL boundary

## Boundary and evidence

SkillRL is in scope as a **builder or improvement plane**: software that generates reusable textual skills, conditions agent decisions on them, and changes both the skill bank and model policy during training. It also ships the agent-environment rollout machinery used by that improvement process. The intended use of this analysis is to characterize those shipped responsibilities, not to treat SkillRL as merely a skill-retrieval library or as a general-purpose deployed assistant. SRC-1, `README.md`, `verl/trainer/main_ppo.py`, `agent_system/multi_turn_rollout/rollout_loop.py` and `verl/trainer/ppo/ray_trainer.py` establish this classification.

The declared intent is:

> SkillRL is a framework that enables LLM agents to learn high-level, reusable behavioral patterns from past experiences. While traditional memory-based methods store redundant and noisy raw trajectories, SKILLRL abstracts these into a hierarchical skill library.
> --- `README.md`

The **whole-system** boundary covers SkillRL's functional loop across the repository: offline experience processing and skill generation; shipped bank artifacts and prompts; loading, selection and prompt consumption; model-driven environment interaction; training and validation; failure-driven skill admission and persistence; and the policy-training/checkpoint infrastructure those paths use. The repository's shipped training drivers and environment managers are included, not assigned to an imaginary external host. General-purpose inherited examples and independent benchmark baseline trainers are outside the functional target unless a SkillRL path calls them. This is whole-system coverage of SkillRL, not a claim to have audited every feature of its bundled verl training framework.

### Entry points and state-loop coverage

The inspected ALFWorld driver invokes `verl.trainer.main_ppo` with a bank path and dynamic updates enabled (SRC-1, `examples/grpo_trainer/run_alfworld_skills.sh`). Scoped searches also found the WebShop and Search skill drivers invoking that same entry point with their respective environment and bank settings (SRC-1, `examples/grpo_trainer/run_webshop_skills.sh`, `examples/grpo_trainer/run_search_skills.sh`). `TaskRunner.run` constructs training and validation environments, workers, a trajectory collector and the trainer, then initializes workers and calls `fit` (SRC-1, `verl/trainer/main_ppo.py`). These callers are part of the target.

>         from agent_system.environments import make_envs
>         envs, val_envs = make_envs(config)
> --- `verl/trainer/main_ppo.py`

>         trainer.init_workers()
>         trainer.fit()
> --- `verl/trainer/main_ppo.py`

The source trace reaches production and later consumption of state, rather than stopping at an API. The offline generator reads memory records and writes a skill JSON; the SFT pipeline parses supplied rollout dumps, generates memories, aggregates a bank, distills reasoning with that bank and emits training pairs (SRC-1, `skill_generation/alfworld.py`, `examples/sft_data_generation/run_alfworld.sh`). The SFT documentation explicitly places its initial rollout dump outside that particular pipeline:

> The rollout step is **not** included — run your own model on the target
> environment, dump trajectories to disk, then run the pipeline here.
> --- `examples/sft_data_generation/README.md`

`SkillsOnlyMemory` reloads a configured JSON bank. The ALFWorld environment manager retrieves skills on reset and formats retained selections into later observations; its shipped prompt contains a retrieved-experience slot. The rollout collector calls policy generation and feeds decoded actions back into the environment (SRC-1, `agent_system/memory/skills_only_memory.py`, `agent_system/environments/env_manager.py`, `agent_system/environments/prompts/alfworld.py`, `agent_system/multi_turn_rollout/rollout_loop.py`).

>         with open(skills_json_path, 'r') as f:
>             self.skills = json.load(f)
> --- `agent_system/memory/skills_only_memory.py`

>             next_obs, rewards, dones, infos = envs.step(text_actions)
> --- `agent_system/multi_turn_rollout/rollout_loop.py`

The trainer's validation and training update branches call `SkillUpdater`, admit returned skills to training memory and save step-labelled banks. Those paths and their validation input collection remain inside the boundary. Inspection of the validation branch shows its write target is the training bank, not the validation bank; this is an implementation boundary, not evidence that validation cannot influence training (SRC-1, `verl/trainer/ppo/ray_trainer.py`).

>             self.envs.retrieval_memory.add_skills(new_skills, category='general')
> --- `verl/trainer/ppo/ray_trainer.py`

>             save_path = os.path.join(save_dir, f'updated_skills_step{self.global_steps}.json')
>             self.envs.retrieval_memory.save_skills(save_path)
> --- `verl/trainer/ppo/ray_trainer.py`

### Repository coverage

The tracked tree was enumerated at the frozen revision. “Included” means part of the functional analysis boundary; the inspection column distinguishes source traced now from available material still to be inspected by later jobs. Uninspected files are not access gaps. All rows refer to SRC-1; paths are commit-relative.

| Top-level tracked entry | Included or excluded; material paths and role | Initial inspection and limits |
|---|---|---|
| `README.md` | Included: target intent, setup, bank format, training drivers and reported benefits. | Read completely. Benefits remain attributed declarations, not measured outcomes. |
| `agent_system/` | Included: `memory/skills_only_memory.py`, `memory/skill_updater.py`, `memory/retrieval_memory.py`, `memory/memory.py`, `memory/base.py`; `environments/env_manager.py`, `environments/base.py`, `environments/prompts/`, `environments/env_package/`; `multi_turn_rollout/rollout_loop.py` and `utils.py`; `reward_manager/episode.py`. These cover retained skills, episode history, prompts, interaction, action projection and feedback. | Traced bank load/admission/save, updater model call, ALFWorld reset/consumption and model/environment loop; searched Search and WebShop manager paths; read ALFWorld prompt. Remaining retrieval internals, other prompts, rewards and environment implementations are available, not yet inspected in detail. Vendored independent baseline agents and benchmark-generation utilities are excluded as independent applications; no conclusions about their training or correctness follow. Environment code actually consumed by SkillRL remains included. Tracked bytecode is not a separate behavioral authority. |
| `examples/` | Included: `grpo_trainer/run_*skills*.sh`, `data_preprocess/prepare.py`, `sft_data_generation/` including `preprocess/`, `skill_memory/`, `distillation/`, `postprocess/` and three shell drivers; `search/retriever/` and `env_server/` when serving included environments; task-agent and alternative training examples as comparison or caller evidence where relevant. | Read ALFWorld skill driver, SFT README and ALFWorld SFT driver; searched WebShop/Search skill drivers, aggregation, distillation and prompt-agent entry points. Other pipeline stages, task drivers and service internals remain available for detailed tracing. Independent generic generation, SFT, Ray tutorial and split-placement examples are deliberately excluded unless consumed by included paths; this prevents general coverage claims about every example. |
| `memory_data/` | Included: `alfworld/claude_style_skills.json`, `search/claude_style_skills_search.json`, `webshop/claude_style_skills.json`, corresponding `generated_memories*.json`, and `prompt/prompt.txt`. Bank artifacts, experience inputs and generation instructions. | Read initial ALFWorld bank entries; generator and training driver establish its producer/consumer paths. Other bank contents, raw memory records and generation prompt are available, not yet inspected. Shipped content is not a trace of the present analysis executing the system. |
| `skill_generation/` | Included: `alfworld.py`, `search.py`, `webshop.py`; offline model-assisted conversion from memories to persistent skill banks. | Traced ALFWorld main through input, categorization, model-client initialization and JSON output. Search/WebShop generation details remain available for inspection; equivalence across them is not yet established. |
| `verl/` | Included: `trainer/main_ppo.py`, `trainer/ppo/ray_trainer.py`, `trainer/ppo/core_algos.py`, `trainer/config/ppo_trainer.yaml`; connected `workers/`, `single_controller/`, `protocol.py`, `utils/dataset/`, `utils/checkpoint/`, model and rollout adapters. These implement policy training, validation, transport, generation and checkpoints for the included loop. | Read main orchestration and both skill-update branches; searched validation, rollout calls and checkpoint entry points. Worker/optimizer/checkpoint details remain available, not yet audited. Unrelated framework-only tools, model support and standalone generation/evaluation commands are excluded unless the included loop reaches them; no framework-wide compatibility or correctness verdict follows. |
| `gigpo/` | Included as alternative training infrastructure: `core_gigpo.py`. | Tree inspected; algorithm implementation not yet inspected. No claim of SkillRL-specific effects or algorithm equivalence is established. |
| `tests/` | Included as potential test-contract evidence for included infrastructure: `trainer/ppo/`, `workers/rollout/`, `utils/`, `e2e/` and related distributed/controller tests. | Tree inspected only; tests not run. Generic framework tests are not presumed to evaluate recursive skill quality. Independent test fixtures outside included paths are excluded; no full test-suite assessment is supported. |
| `docs/` | Included where explaining used training/worker/checkpoint infrastructure: `api/trainer.rst`, `workers/`, `advance/checkpoint.rst`, `examples/config.rst`; remaining generic framework documentation is contextual only. | Tree inspected; content not yet inspected. Independent framework tutorials are deliberately excluded from claims about SkillRL's mechanism; general documentation accuracy is not assessed. |
| `scripts/` | Included where used for setup or checkpoint export: `install_vllm_sglang_mcore.sh`, `model_merger.py`, `converter_hf_to_mcore.py`, `diagnose.py`. | Tree inspected; script implementations not yet inspected. No deployment or checkpoint-export success is established. |
| `docker/` | Excluded: container recipes for backend/platform deployment. | Tree inspected only. Exclusion prevents claims about image reproducibility or backend/platform deployment support, not source-level skill-loop tracing. |
| `recipe/` | Excluded: independent DAPO, PRIME, R1, SPIN and SPPO recipes. | Tree inspected only. No conclusions about these separate algorithms or workflows; a subsequently discovered direct dependency must be traced rather than attributed from recipe names. |
| `figs/` | Included as declared-design material: `pipeline.png`. | Tree inspected; diagram not yet read. It supplies no implementation or experiment evidence by itself. |
| `pyproject.toml` | Included: build/dependency metadata. | Available, not yet inspected; installation reproducibility remains unestablished. |
| `requirements.txt` | Included: dependency declarations. | Available, not yet inspected; dependency-resolution success remains unestablished. |
| `setup.py` | Included: package and backend dependency declarations. | Read completely; declares a verl package and optional generation backends. No installation was performed. |
| `LICENSE` | Excluded: legal terms, not a skill-loop mechanism. | Tree inspected only; no legal-use assessment. |
| `Notice.txt` | Excluded: notices/attribution. | Tree inspected only; no attribution-completeness assessment. |

### Frozen evidence and dependencies

The applicability cutoff is **2026-10-14**. The sole frozen evidence identity is `https://github.com/aiming-lab/SkillRL` at commit `4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d`; checkout HEAD matched that pin during inspection. No later branch state, linked paper, external repository, live model listing or downloaded dataset supplies evidence. The overall tier is **code-grounded**, with documentation separately treated as declared intent or reported claims.

External dependencies include model weights, generation backends, Ray/PyTorch infrastructure, embedding models for embedding retrieval, environment data/services, and OpenAI/Azure model services. The updater's actual model invocation is inspected in SRC-1, `agent_system/memory/skill_updater.py`:

>             response = self.client.chat.completions.create(
>                 model=self.model,
>                 messages=[{"role": "user", "content": prompt}],
>                 max_completion_tokens=self.max_completion_tokens,
>             )
> --- `agent_system/memory/skill_updater.py`

The root documentation assigns the SFT training stage to LLaMA-Factory, while the included SFT-data pipeline emits its inputs (SRC-1, `README.md`, `examples/sft_data_generation/README.md`). That external trainer's implementation is not frozen here; this prevents conclusions about its actual fitting behavior or reproducibility. Externally supplied rollout dumps likewise prevent reconstructing the provenance of every initial experience from this source set alone. Neither limit excludes SkillRL's shipped RL collector or its offline processors.

No target code, tests, examples, services or model calls were executed. There are no supplied execution traces or controlled comparisons. Consequently this boundary supports source-level operation and attributed design, not observed end-to-end success, performance, quality of generated skills, causal gains or external-service availability. All tracked source paths remain available within SRC-1 for subsequent inspection; no material shipped path is known to be inaccessible.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/aiming-lab/SkillRL` | 4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/skillrl-0dba0e1c895e/related-systems/aiming-lab--SkillRL`. Implementation: tracked tree; `verl/trainer/main_ppo.py` orchestration, `verl/trainer/ppo/ray_trainer.py` update branches and scoped caller/checkpoint search; `agent_system/memory/skills_only_memory.py` load/mutation/save; `agent_system/memory/skill_updater.py` client and analysis call; `agent_system/environments/env_manager.py` ALFWorld consumption and Search/WebShop scoped searches; `agent_system/multi_turn_rollout/rollout_loop.py` reset/model/action loop; skill/SFT drivers, ALFWorld generation main, aggregation/distillation scoped searches; initial ALFWorld bank; `setup.py`. Doctrine/design: complete root and SFT READMEs and ALFWorld prompt. Reported operation: root README benefit claims only. | Implementation: [training entry](https://github.com/aiming-lab/SkillRL/blob/4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d/verl/trainer/main_ppo.py), [trainer](https://github.com/aiming-lab/SkillRL/blob/4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d/verl/trainer/ppo/ray_trainer.py), [bank](https://github.com/aiming-lab/SkillRL/blob/4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d/agent_system/memory/skills_only_memory.py), [SFT driver](https://github.com/aiming-lab/SkillRL/blob/4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d/examples/sft_data_generation/run_alfworld.sh). Doctrine/design and reported claims: [README](https://github.com/aiming-lab/SkillRL/blob/4d984d455b9b02f0bad283cbe9ab3d66a7e5b89d/README.md). Other local anchors above resolve at this same revision. | No known checkout access gap. External weights, services, rollout provenance and SFT trainer are not frozen; no observed run or causal experiment is supplied. Prevents reproducing model/service behavior, validating provenance or inferring measured gains from implementation and documentation alone. Initial inspected paths are not an evidence allowlist; later jobs may inspect other included paths at this commit. |
