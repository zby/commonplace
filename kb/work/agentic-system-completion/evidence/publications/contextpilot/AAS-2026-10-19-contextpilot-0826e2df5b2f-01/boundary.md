---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ContextPilot's shipped context-management inference and RL training system at commit 782cbb6611fb610c4cf6fafda6022b7e89cae191."
run-id: AAS-2026-10-19-contextpilot-0826e2df5b2f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/Tencent/ContextPilot
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-contextpilot/related-systems/Tencent--ContextPilot
  revision: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
  sha256: null
---

# ContextPilot boundary

## Boundary and evidence

This run analyses ContextPilot as a **memory/knowledge/context-engineering system**, including its shipped model-driven QA loop, context and memory tools, finite-state inference controller, benchmark drivers and RL improvement pipeline. Its intended use is document-grounded long-context QA and search with a compact working context. It is not just a memory library embedded in an excluded caller: the repository ships the callers, prompts, tool-admission controller, result writers and training consumers. The boundary kind is **whole-system** for those ContextPilot responsibilities, not a review of every capability of the bundled verl framework (SRC-1, `README.md`, `infer/scripts/eval_task.sh`, `train/sh/run_qwen3-8b_longbenchv2.sh`).

The target depends directly on model calls. The inference driver constructs a fresh agent for each sample, supplies the document and question, calls its run method, and writes final results and inference traces. The payload builder exposes saved memory/note summaries to subsequent turns; the FSM restricts which tools may be offered, including memory review before completion. These shipped callers and consumers are included, rather than treated as external hosts (SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`, `infer/src/contextpilot_fsm.py`). A minimum implementation passage establishing the caller is:

> last_payload = agent.run(question, max_turns_to_fail=max_turns_to_fail)
> --- `infer/src/hf_test_runner.py`

The prompt supplies maintenance instructions as part of the system, not merely explanatory documentation (SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, `train/configs/contextpilot_system_prompt.txt`):

> 7. Before finishing, if `readNote` or `loadMemory` is available, review relevant saved entries using only keys listed in the current Available Notes/Memories sections.
> --- `infer/configs/fsm_plan_bm25_mc_prompt.txt`

The training plane is included because it creates and consumes intermediate context-editing snapshots, not just final answers. Its agent-loop worker assigns descendant terminal rewards to snapshots, and the dedicated estimator consumes these rewards. Checkpoint save/load and validation paths are also within scope (SRC-1, `train/verl/experimental/agent_loop/agent_loop.py`, `train/verl/trainer/contextpilot/adv.py`, `train/verl/trainer/ppo/ray_trainer.py`). The estimator states the division of responsibility:

> Partial rollouts and subtree-mean reward assignment happen in the agent-loop
> worker before this estimator runs.  Consequently, each input row already
> represents one snapshot whose reward is the mean terminal reward of its
> descendant continuations.
> --- `train/verl/trainer/contextpilot/adv.py`

The frozen evidence is solely SRC-1 at the full commit above, with applicability cutoff **2026-10-19**, the supplied run date. Overall evidence is **code-grounded**: source text and shipped instructions were inspected, but no target code, tests, examples, model calls or services were executed. Source inspection establishes implementation and intended contracts, not successful deployment, measured quality or causal benefit. The README's performance claims remain attributed claims, not observed results (SRC-1, `README.md`).

### Repository coverage

Every top-level tracked entry is classified below. Included paths remain available to later source inspection at the same commit; “not yet inspected” does not mean unavailable. Initial inspection traced the inference caller through state consumption and result writing, and the training recipe through tools, snapshot reward assignment, advantage computation and checkpoint recovery.

| Top-level entry | Classification and material paths | Initial inspection and limits |
|---|---|---|
| `.env.example` | Included: judge endpoint configuration surface. | Role established through `train/README.md` and `train/sh/run_qwen3-8b_longbenchv2.sh`; template contents not yet inspected. No conclusion about secret handling. |
| `.gitignore` | Excluded: repository housekeeping. | No conclusion about completeness of ignored local artifacts or operational retention policy. |
| `LICENSE` | Excluded: legal terms. | No licensing assessment. |
| `README.md` | Included: system purpose, inference/training entry points, benchmark availability and declared results. | Inspected in full as doctrine/design and attributed reported operation, not execution evidence. |
| `assets/` | Excluded: `contextpilot_overview.png`, presentation diagram. | No conclusion relies on visual architecture or diagram-only details. |
| `infer/` | Included: `README.md`; `scripts/run_full_pipeline.sh`, `scripts/eval_task.sh` and per-task/service/setup/data-preparation launchers; `src/contextpilot.py`, `src/contextpilot_fsm.py`, `src/hf_test_runner.py`, `src/hf_process_fns.py`, `src/hf_score_fns.py`; `configs/`, `tools/context-shaper_tools.json`, requirements and benchmark data declarations. | Inspected guide, full pipeline/task launchers, full maintenance prompt, runner's per-sample creation/run/output path, payload builder, FSM state/tool admission and choice scoring. State/memory/context tool entry points and remaining runner/scorer functions were located by search. Other implementation bodies, endpoint/tool schemas, dataset adapters, service launchers and data preparation remain available but not yet inspected. Benchmark payload limits are stated below. |
| `train/` | Included: `README.md`, `sh/run_qwen3-{8b,14b}_longbenchv2.sh`, `configs/contextpilot_system_prompt.txt`; ContextPilot configuration under `examples/sglang_multiturn/config/`; `verl/experimental/agent_loop/{agent_loop,statelm_agent_loop}.py`, `verl/tools/{statelm_tools,contextpilot_memory}.py`, `verl/trainer/contextpilot/`, `verl/utils/reward_score/statelm_qa.py`, PPO trainer, checkpoint/worker/rollout machinery, model export, and relevant tests including `tests/experimental/agent_loop/test_contextpilot_partial_rollout.py`. | Inspected guide, full 8B launcher and prompt, document-state setup/cleanup, memory write/read/update tools, structured memory mutation/read methods, subtree reward assignment, full advantage estimator, terminal QA scoring, and PPO checkpoint save/load. Agent-loop branch/state/snapshot paths were located by search. The 14B recipe, relevant test bodies, configuration bodies, detailed rollout scheduling, lower-level worker/optimizer/checkpoint/export internals remain available but not yet inspected. They are not excluded responsibilities. Generic verl examples, unrelated recipes, hardware tutorials, docs infrastructure and container variants are deliberately excluded as independent framework breadth; this prevents claims of comprehensive verl or hardware-platform coverage, not analysis of ContextPilot's shipped training loop. |

All source-dependent entries above refer to SRC-1; paths are commit-relative. Coverage does not assert exhaustive inspection of every included function.

### External dependencies and evidence limits

- **Model services and weights:** inference launches vLLM and uses model/tokenizer paths; training requires a supplied SFT checkpoint and GPU environment. OpenAI-compatible judges score selected tasks and open-ended training answers. Optional embedding/reranking paths are present in the inference caller. These external implementations, model weights and live endpoint behavior are not frozen here, preventing conclusions about actual model behavior, service reliability, achieved accuracy or runtime cost (SRC-1, `infer/scripts/run_full_pipeline.sh`, `infer/src/hf_test_runner.py`, `train/README.md`, `train/verl/utils/reward_score/statelm_qa.py`).
- **Retrieval:** Elasticsearch is an external service; the included tool code owns document indexing and cleanup, but the Elasticsearch implementation and deployed index contents are outside this source. This prevents claims about production retrieval performance and isolation beyond inspected request construction (SRC-1, `train/verl/tools/statelm_tools.py`, `infer/README.md`).
- **Benchmark content:** LongMemEval's checked-out file is an LFS pointer rather than benchmark records; root documentation also identifies BrowseComp+ as LFS-tracked. NovelQA's private answer/book bundle is explicitly not distributed, InfBench is loaded from Hugging Face, and training data is downloaded separately. No fetch or LFS materialization was performed. Benchmark adapters and scoring/launch code remain included, but unavailable external payloads prevent dataset-content audits and reproduction of benchmark or training outcomes (SRC-1, `infer/data/LongMemEval/longmemeval_s_cleaned.json`, `README.md`, `infer/scripts/eval_task.sh`, `train/README.md`). BrowseComp+ shard contents were not inspected; their materialization is not asserted.
- **Durability and reuse:** this boundary includes within-trajectory memory read/write and subsequent payload consumption, inference artifact persistence/resume bookkeeping, and training checkpoint save/reload. It does not infer cross-task autobiographical memory from the word “memory,” nor assume that inference trajectory JSON is reloaded as a later agent's knowledge store. Those conclusions require further tracing, not an exclusion of the shipped driver (SRC-1, `infer/src/hf_test_runner.py`, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`, `train/verl/trainer/ppo/ray_trainer.py`).
- **Evidence outside this checkout:** the linked paper, live demo, upstream StateLM/verl repositories and remote model/dataset pages were not acquired and cannot supply evidence for this run. No implementation claim or experimental conclusion may rely on them (SRC-1, `README.md`).

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Tencent/ContextPilot` | 782cbb6611fb610c4cf6fafda6022b7e89cae191 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-contextpilot/related-systems/Tencent--ContextPilot`. Implementation: tracked tree; inference pipeline/task launchers, per-sample caller and artifact writing in `infer/src/hf_test_runner.py`, payload building in `infer/src/contextpilot.py`, state/tool admission in `infer/src/contextpilot_fsm.py`, choice evaluator in `infer/src/hf_score_fns.py`; training launcher, document and memory tools, memory-state mutations, subtree reward assignment, advantage estimator, terminal scoring, PPO checkpoint save/load. Doctrine/design: root/inference/training READMEs and both shipped maintenance prompts. Reported operation: root README's performance assertions only. | Implementation: [inference caller](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/hf_test_runner.py), [context/payload implementation](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/contextpilot.py), [FSM](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/src/contextpilot_fsm.py), [training loop](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/verl/experimental/agent_loop/agent_loop.py), [checkpoint consumer](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/verl/trainer/ppo/ray_trainer.py). Doctrine/design: [prompt](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/infer/configs/fsm_plan_bm25_mc_prompt.txt), [training guide](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/train/README.md). Reported operation: [README](https://github.com/Tencent/ContextPilot/blob/782cbb6611fb610c4cf6fafda6022b7e89cae191/README.md). | Implementation limits: no target execution; unavailable model/service implementations and external dataset payloads; verified LongMemEval LFS pointer. These prevent runtime/performance and dataset-content conclusions. Available but uninspected bodies are identified in coverage, not called access gaps. Doctrine/design supports intent, not compliance. Reported operation has no inspected run artifacts or intervention/comparison evidence and supports no independently verified accuracy or causal claim. |
