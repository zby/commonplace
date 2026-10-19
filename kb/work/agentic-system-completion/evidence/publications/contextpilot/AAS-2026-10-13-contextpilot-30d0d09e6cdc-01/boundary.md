---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ContextPilot's shipped inference and reinforcement-learning context-management paths at commit 782cbb6611fb610c4cf6fafda6022b7e89cae191."
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
analysis-cutoff: "2026-10-13"
evidence-tier: code-grounded
source:
  identity: https://github.com/Tencent/ContextPilot
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/contextpilot-30d0d09e6cdc/related-systems/Tencent--ContextPilot
  revision: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
  sha256: null
---

# ContextPilot boundary

## Boundary and evidence

This run covers ContextPilot as a context-engineering system for model-driven long-context document question answering, including its shipped inference driver, context and memory tools, prompts, evaluation callers, and reinforcement-learning improvement plane. It is not limited to the memory API. The target qualifies because model calls select operations on the working context and retained findings, and subsequent calls consume the resulting state. The repository also ships the training loop that improves those decisions (SRC-1, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/sh/run_qwen3-8b_longbenchv2.sh`).

The intended use is to characterize these source-native responsibilities and their boundaries, not to establish benchmark superiority or production reliability. The target class is `memory/knowledge/context-engineering system`; its included agent loops and training infrastructure are responsibilities of this system, not evidence of a general-purpose enclosing application runtime.

The boundary is `whole-system`: it includes the material shipped paths that ingest documents, construct searchable chunks, admit and update memories and notes, edit context, render saved content into later model inputs, terminate with an answer, save trajectories and predictions, score them, and train and checkpoint the policy. Inference's ordinary and FSM implementations are both included; the supplied task launcher selects the FSM variant. The training driver and evaluation harness are included callers, not excluded hosts (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/hf_test_runner.py`, `train/verl/tools/statelm_tools.py`, `train/verl/trainer/ppo/ray_trainer.py`).

Minimum boundary evidence:

> You are an AI assistant specialized in long-context document QA. Use the currently available tools to find evidence in the attached document, save useful findings, keep the context compact, and submit the final answer through `finish`.
> --- `infer/configs/fsm_plan_bm25_mc_prompt.txt`

This is shipped doctrine, not an instruction to this analysis worker (SRC-1). The default inference caller selects the FSM and creates a new agent for each sample, runs it, and writes answer and trajectory artifacts (SRC-1, `infer/scripts/eval_task.sh`, `infer/src/hf_test_runner.py`). The FSM's declared gating is backed by its state-driven loop:

> FSM-aware run loop.  At each turn only the tools allowed by the
> current FSM state are presented to the model.  tool_choice is set
> to "required" in states where the model MUST call a tool.
> --- `infer/src/contextpilot_fsm.py`

Saved memory is consumed within subsequent prompt construction; its existence must not be equated with proven cross-session persistence (SRC-1, `infer/src/contextpilot.py`):

> external_context_summary = external_memory_summary + external_note_summary
> --- `infer/src/contextpilot.py`

The training side includes memory-store tools and an explicit agent state loop, with branch trajectories subsequently consumed by the reward worker and advantage estimator. Policy and dataloader checkpoint save/load paths are included, separately from the task's memory objects (SRC-1, `train/verl/tools/statelm_tools.py`, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/ppo/ray_trainer.py`). Its estimator declares the division of responsibility:

> Partial rollouts and subtree-mean reward assignment happen in the agent-loop
> worker before this estimator runs.  Consequently, each input row already
> represents one snapshot whose reward is the mean terminal reward of its
> descendant continuations.
> --- `train/verl/trainer/contextpilot/adv.py`

### Tracked top-level coverage

The table accounts for every top-level tracked file or directory. Included means within the functional boundary, not that every contained implementation has been audited. The inspected material paths below establish the boundary's main loops; additional files at this same revision remain eligible evidence under SRC-1.

| Top-level path | Classification and material paths | Inspection and role; conclusion prevented by exclusion or gap |
| --- | --- | --- |
| `.env.example` | Included configuration contract | Inspected: judge endpoint/model credentials and optional download/logging credentials. Actual secrets and deployed endpoint configuration are unavailable; deployment-specific judge behavior cannot be established. |
| `.gitignore` | Excluded repository housekeeping | Tree inventoried; contents not inspected. No claim about ignored-file policy or completeness of a developer's local working environment. |
| `LICENSE` | Excluded legal metadata | Tree inventoried; contents not inspected. No licensing analysis. |
| `README.md` | Included doctrine/design and attributed performance report | Inspected: intended context-management and RL mechanisms, setup, evaluation/training entry points, model/data dependencies. Performance claims remain attributed reports, not measured results. |
| `assets/` | Excluded presentation asset: `assets/contextpilot_overview.png` | Tree inventoried; diagram not inspected. No mechanism conclusion rests on the diagram. |
| `infer/` | Included operational and evaluation path | Inspected `infer/README.md`; full `infer/scripts/run_full_pipeline.sh` and `infer/scripts/eval_task.sh`; caller ranges in `infer/src/hf_test_runner.py`; state, memory rendering, model-call and ordinary-loop ranges in `infer/src/contextpilot.py`; FSM loop and repository-wide symbol tracing in `infer/src/contextpilot_fsm.py`; full `infer/configs/fsm_plan_bm25_mc_prompt.txt`; LongMemEval scorer range and scoring entry-point search in `infer/src/hf_score_fns.py`; full `infer/.gitattributes` and the LongMemEval LFS pointer. These cover document supply, per-sample instantiation, read/write/re-consumption of findings, answer/trajectory persistence and score consumption. `infer/src/hf_process_fns.py`, `infer/tools/context-shaper_tools.json`, endpoint JSONs, other scripts and remaining scorer/core bodies are included but not yet inspected in detail; no exhaustive tool/schema or evaluator-correctness conclusion is made here. Benchmark payload availability is limited below. |
| `train/` | Included ContextPilot training and its supporting verl implementation; unrelated bundled recipes are deliberately excluded | Inspected full `train/README.md`, `train/configs/contextpilot_system_prompt.txt`, `train/verl/trainer/contextpilot/adv.py`; launch range in `train/sh/run_qwen3-8b_longbenchv2.sh`; main entry range in `train/verl/trainer/main_ppo.py`; state-loop and cleanup ranges plus branch/rendering symbol search in `train/verl/experimental/agent_loop/statelm_agent_loop.py`; subtree reward assignment and branch-budget search in `train/verl/experimental/agent_loop/agent_loop.py`; document lifecycle and memory/context-tool ranges in `train/verl/tools/statelm_tools.py`; memory implementation symbol search in `train/verl/tools/contextpilot_memory.py`; trainer checkpoint save/load ranges and generation/update search in `train/verl/trainer/ppo/ray_trainer.py`; document/Parquet data-path search in `train/verl/utils/dataset/rl_dataset.py`. Included but not yet deeply inspected: 14B launcher, tool/agent YAML configurations, reward scorer `train/verl/utils/reward_score/statelm_qa.py`, actor/rollout/checkpoint workers and model-merger support, plus `train/tests/experimental/agent_loop/test_contextpilot_partial_rollout.py`. Their inclusion preserves the training, reload and validation responsibilities; tests are source contracts, not observed passes. Generic `train/recipe/`, unrelated `train/examples/`, and generic documentation/docker variants outside this ContextPilot path are deliberately excluded from independent characterization; no claim covers all bundled verl algorithms, examples or hardware backends. |

### Frozen revision, dependencies and limits

The applicability cutoff is 2026-10-13, the supplied run date. The frozen boundary is commit `782cbb6611fb610c4cf6fafda6022b7e89cae191` of `https://github.com/Tencent/ContextPilot`, accessed read-only at the absolute checkout in `source.path`. HEAD matched that pin and the checkout reported no tracked modifications. The overall tier is `code-grounded`; reading source establishes implementation and declared contracts, not successful operation.

External dependencies include OpenAI-compatible inference and judge services, model/tokenizer weights, Elasticsearch, and the vLLM/verl training and serving stack. ContextPilot's shipped adapters, launchers and modified verl code are inside the boundary; separately installed dependency internals, deployed services and downloaded weights are not frozen evidence. Accordingly this run cannot establish provider execution semantics, model quality, service reliability, hardware performance or the exact behavior of an unpinned deployed dependency (SRC-1, `infer/scripts/run_full_pipeline.sh`, `infer/scripts/eval_task.sh`, `train/README.md`, `.env.example`).

Benchmark code and references are included, but actual task content is not uniformly available. `infer/data/LongMemEval/longmemeval_s_cleaned.json` is an LFS pointer in this checkout, and the inspected BrowseComp+ shard is likewise a pointer; `infer/.gitattributes` declares both data families as LFS. Their payloads were not fetched. NovelQA's prepared copyrighted bundle and externally downloaded InfBench and transformed LongBench-v2 training data are not supplied frozen inputs. These gaps prevent inspection of those complete datasets, reconstruction of the paper's exact evaluation inputs and independent benchmark verification, not characterization of the shipped data-loading and evaluation mechanism (SRC-1, `infer/.gitattributes`, `infer/data/LongMemEval/longmemeval_s_cleaned.json`, `infer/data/BrowseCompPlus/data/test-00000-of-00006.parquet`, `infer/scripts/eval_task.sh`, `train/README.md`).

No target code, example, training job or benchmark was executed. No observed run or causal experiment is registered. The linked paper, live demo, external StateLM repository and model collection were not acquired and are excluded as independent evidence; their contents cannot support conclusions in this run. Source-native documentation may report outcomes, but such reports do not establish reproduced gains, action-level causal effects, cross-session memory durability, or robustness under real deployment (SRC-1, `README.md`). Available files not yet inspected are not access gaps.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/Tencent/ContextPilot` | 782cbb6611fb610c4cf6fafda6022b7e89cae191 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/contextpilot-30d0d09e6cdc/related-systems/Tencent--ContextPilot`. Implementation: tracked-tree inventory; inference launch/caller, ordinary/FSM loops, state summaries, model calls, output and scoring paths; training entry, document/memory/context tools, state/branch/reward worker, advantage estimator, dataset and checkpoint paths identified in the coverage table. Doctrine/design: `README.md`, `infer/README.md`, `train/README.md`, both shipped system prompt files and `.env.example`. Reported operation: root README's attributed experimental claim; no run artifacts inspected. | Implementation: [inference caller](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/hf_test_runner.py), [FSM](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/contextpilot_fsm.py), [state and model client](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/contextpilot.py), [training loop](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/verl/experimental/agent_loop/statelm_agent_loop.py), [reward worker](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/verl/experimental/agent_loop/agent_loop.py), [checkpoint owner](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/verl/trainer/ppo/ray_trainer.py). Doctrine: [inference prompt](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/configs/fsm_plan_bm25_mc_prompt.txt), [training guide](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/README.md). Reported operation: [README](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/README.md). | LFS dataset payloads and external/private datasets and model weights are unavailable as frozen content; no dataset-completeness or reproduced-quality conclusion. Dependency deployments, paper/demo contents and execution evidence are outside the frozen source; no observed-operation or causal-effect conclusion. Deliberate generic verl/presentation/legal exclusions and uninspected included files are distinguished above. |
