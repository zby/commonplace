# ContextPilot current-batch audit

## Disposition

**Hold.** The publication omits a consequential training-loop selection condition that the historical account retained. The implemented ContextPilot training route is useful and its operation/benefit qualifications are sound, but the public account does not explain when the launcher actually selects that route rather than the generic single-turn loop. A qualification in this audit cannot repair the publication.

Unblock through a coordinator/operator-authorized correction route: retain the dataset/configuration selector and generic fallback in the runtime account and public synthesis, qualify the ContextPilot-specific wiring accordingly, and reverify dependent claims. Alternatively, provide frozen-boundary evidence that establishes selection independently of the unavailable dataset. Do not require new acquisition or target execution merely to state the existing condition. This audit does not authorize mutation of accepted outputs.

## Identity and inspection method

- Target: the exact ContextPilot batch-02 inventory row, not an older origin copy.
- Run: `AAS-2026-10-13-contextpilot-30d0d09e6cdc-01`.
- Prepared worktree: `/home/zby/llm/commonplace/.commonplace/worktrees/contextpilot-30d0d09e6cdc` (abbreviated **W** below).
- Publication: `W/kb/agentic-system-analyses/retained/contextpilot/` (**P**).
- Run evidence: `W/kb/agentic-system-analyses/state/AAS-2026-10-13-contextpilot-30d0d09e6cdc-01/` (**R**).
- Preparation record: sibling `contextpilot-30d0d09e6cdc.preparation.json`; status `ready`, command prefix `W/.venv/bin`.
- Method commit: `4266dabc470929df0ff753e57fee0c55d7b87fc6`, matching preparation, overview inputs and observed worktree HEAD.
- Source: `https://github.com/Tencent/ContextPilot`, at `782cbb6611fb610c4cf6fafda6022b7e89cae191`; the boundary, retained overview and observed source HEAD agree. Source Git status was empty.
- Frozen source root: `W/related-systems/Tencent--ContextPilot` (**S**). All source inspection stayed within this boundary. Cutoff: `2026-10-13`; code-grounded, whole-system functional scope, not exhaustive file coverage.
- Auditor runtime confirmed through environment: Pi, `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`; session `01a138ef-a849-7220-90a5-05912d1ee006`. No delegation.

Method: bounded legacy-regression comparison, public-qualification review, targeted source tracing for the lost activation condition, exact publication hash checking and a stored-attempt/nested-trace screen. Read the overview, synthesis, boundary and all three current verification reports completely. Selected runtime passages and source/configuration sections according to the consequential difference. Stopped after establishing one actionable publication defect; this is not a second analysis.

## Historical comparison

The workshop's `systems.md` row links [the archived ContextPilot review](../../../agentic-systems/reviews-archive/contextpilot.md), run `AAS-2026-09-25-contextpilot-01`. A case-insensitive search of `kb/agent-memory-systems/` found no matching ContextPilot coverage. The comparison therefore uses the moved retained review in `kb/agentic-systems/reviews-archive/`, not an invented legacy report. Its linked detailed result was not independently audited here.

The historical review and current publication inspect the **same source commit**. The later cutoff does not explain this coverage loss. Historical assertions were leads, not truth or material supplied to the source-first workers.

The current synthesis retains the historical review's important distinctions: task-local stores versus cross-question service; protocol tool admission versus semantic sufficiency; full-set fallback and alternate base route; deterministic review recovery; original retention versus faithful replacement and granted restoration; random-word compression fallback; oversized-payload possibility; outcome credit versus individual-action merit; and implemented own-parameter changes versus observed improvement. It also makes benchmark prediction provenance, conditional synthetic cleanup and destructive merge's library-only status more explicit. These are favorable coverage observations, not independent source certification of each claim.

The historical review explicitly said training activation depends on dataset `agent_name` or configuration, the generic fallback is `single_turn_agent`, and the transformed external dataset was uninspected. The current public account loses this particular prerequisite. Its broader warnings about unfrozen datasets and unobserved execution do not identify the alternative architectural route.

## Consequential finding: training dispatch is conditional

The following inspected source chain establishes the missing qualification:

1. `S/train/verl/experimental/agent_loop/agent_loop.py:1006–1008` supplies `config.agent.default_agent_loop` when the batch lacks `agent_name`.
2. The same file at `1080–1121` indexes `_agent_loop_registry[agent_name]`, instantiates that entry and calls its `run`. Naming a tool configuration or enabling partial rollout is not itself this class selector.
3. `S/train/verl/experimental/agent_loop/statelm_agent_loop.py:451–452` registers `StatelmToolAgentLoop` as `statelm_tool_agent`.
4. `S/train/verl/trainer/config/rollout/rollout.yaml:207–208` sets the default to `single_turn_agent`. `ppo_trainer.yaml:8–36` imports that rollout configuration; the complete `examples/sglang_multiturn/config/statelm_tool_agent_grpo.yaml` inherits `ppo_trainer` and does not change the default.
5. The complete `S/train/sh/run_qwen3-8b_longbenchv2.sh` selects that configuration and enables ContextPilot/tool/partial-rollout settings, but does not override `agent.default_agent_loop`. It takes external transformed train/validation parquet files. The boundary explicitly says those training payloads are not frozen.
6. `S/train/verl/experimental/agent_loop/single_turn_agent_loop.py:26–64` registers the generic fallback and performs a single generation. It is not the inspected ContextPilot tool/context-management loop.

This does **not** establish that the actual transformed dataset lacks the correct selector, that training is broken, or that the ContextPilot-specific update pathway is absent. It establishes a prerequisite whose fulfillment is not evidenced here.

Affected publication passages: `P/boundary.md`, “Entry points and state consumers,” says the worker instantiates the registered loop without exposing the selector; `P/runtime.md`, “Model improvement and change admission” and `RT-RTE-rollout-training`, describe launcher → manager/worker → `StatelmToolAgentLoop` as the selected pathway without this condition; `P/synthesis.md`, “From rollout experience to later policy,” describes ContextPilot branches and downstream consumers without the fallback. Searches of these three members found neither `agent_name` nor `single_turn_agent`. The report verification's broad acceptance of the training chain does not resolve this omitted entry condition.

The necessary correction is narrow: distinguish an implemented route conditional on selecting `statelm_tool_agent` from proof that the shipped launcher plus unavailable dataset activates it. Carry that distinction into the public synthesis and affected dependent records. The existing missing-run/benefit qualifications should remain.

## Publication and operational evidence

`R/effects/publish.json` records completed publication to P for this run/source, with 13 exact hashes: the manifest and twelve members. Independently recomputed SHA-256 values matched all 13 files. `R/state/attempts/000050-publish.json` is completed and pins the same accepted member versions and manifest. Thus there is positive file-identity and publication evidence, not merely an overview's existence.

Stored attempts show semantic correction cycles before publication: report verification at attempt 22, runtime/epistemic revisions at 24/26, re-verification at 35; profile verification at 39, revised profile at 41, re-verification at 43; synthesis and its verification at 45/47. The current verifications declare no blockers or additional limits. Their claims do not settle the new selector omission.

The preserved `kb/work/agentic-system-reruns/outputs/contextpilot.output` contains nested worker results for all 17 model attempts, plus a separate launch diagnostic. A streaming inspection paired assistant tool calls with tool-result identifiers within each worker: all 17 results report exit zero and include executed tool evidence. Initial source analysts and both report-verification workers have source-locator calls; reconciliation/profile/synthesis workers have none in this locator screen. No literal historical-review or retained-publication locator was found in the screened executed arguments. This is a screen, not proof against indirect reads or complete compliance.

For the final report verifier (`000035-report-verification`), paired executed reads include `infer/src/contextpilot.py` at offsets 460 and 2110, and `infer/src/hf_test_runner.py` at offset 290. One exact locator is `call_udTkAnnw7IYmay6qnE99rgMC|fc_0b4e2d9bc47f7f93016acec2000bd487d2b3d1b6fdfd2a84dc`, paired with its tool result inside that worker. This is positive evidence of source inspection rather than an unexecuted proposal. No missing worker trace was established for these attempts. Complete invocation-read recovery, every write's authorization and every worker obligation were not certified by this bounded screen. Engine acceptance, worker exit, architectural wiring and demonstrated target benefit remain different claims.

## Validation and coverage limits

From W, used its prepared command environment:

```text
.venv/bin/commonplace-validate kb/agentic-system-analyses/retained/contextpilot
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/contextpilot
Scope: kb/agentic-system-analyses/retained/contextpilot
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

The displayed count is one directory artifact, not a claim of twelve separately counted documents. This is deterministic validation, not resolution of the semantic blocker.

From W, report validation also succeeded:

```text
.venv/bin/commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-contextpilot.md
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-contextpilot.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/bash-current-contextpilot.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

No target execution, tests, acquisition, engine advancement, integration, commit or shared bookkeeping change was performed. The audit does not independently settle all memory axes, optional acquisition paths, branch-credit arithmetic or historical numerical-gradient/checkpoint details. Current source/runtime/benefit limits are already visible in the synthesis. The outstanding blocker is the missing dispatch qualification, not a demand to prove operation or benefit.
