# Batch 23 ContextPilot exact-publication audit

## Disposition

**Hold.** The new publication again omits the training-loop dispatch prerequisite. It describes ContextPilot-specific rollouts and actor-update wiring without explaining that dataset `agent_name` or a configuration override must select `statelm_tool_agent`; the inherited default is the generic `single_turn_agent`. The transformed training dataset is outside the frozen evidence. General no-execution and missing-data qualifications do not disclose this architectural alternative.

Unblock through a separately authorized correction route: qualify the runtime training route and public synthesis with the selector, fallback and unresolved dataset selection; align the boundary narrative and dependent assessments, then independently reverify. Alternatively establish selection from frozen evidence. This does not require executing training or acquiring data merely to state the condition. This report authorizes no repair or recovery. Historical holds remain evidence; this new hold is independently established against the exact fresh bytes.

## Identity and method

- `run-id`: `AAS-2026-10-19-contextpilot-0826e2df5b2f-01`.
- `method-commit`: `3e2491c83a4613d410511af8c3cfde30f4b67689`.
- `source-revision`: `782cbb6611fb610c4cf6fafda6022b7e89cae191`.
- Source identity: `https://github.com/Tencent/ContextPilot`.
- **W**: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-23-contextpilot`.
- **S**: `W/related-systems/Tencent--ContextPilot`.
- **P**: `W/kb/agentic-system-analyses/retained/tencent--contextpilot`.
- **R**: `W/kb/agentic-system-analyses/state/AAS-2026-10-19-contextpilot-0826e2df5b2f-01`.
- **L**: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/batch-23/contextpilot.output`.
- Preparation: sibling `batch-23-contextpilot.preparation.json`; ready, command prefix `W/.venv/bin`.
- Auditor: independent Pi session `01a15553-6993-7087-8139-123237c86bac`; observed `PI_PROVIDER=openai`, `PI_MODEL=gpt-6.1-sol`, `PI_REASONING_LEVEL=medium`. No delegation.

Followed the commission and audit procedure. Read the workshop README, workshop/text contracts, analysis collection and applicable set/runtime/synthesis contracts. Read the overview, synthesis and three verification members completely; selected boundary/runtime passages and direct frozen-source dispatch/configuration bodies for the consequential discrepancy. This is a bounded audit, not a second analysis or full memory-profile reassessment.

### Current identity checks

Independently recomputed all intake-listed hashes: **1,020 source files, 13 publication files and 170 run files matched**, as did preparation, publication effect and external log. P contains exactly its 13 expected members. The completed `R/effects/publish.json` names this run, source and destination; its `new` map equals the intake publication map, with expected incumbent `absent`. `000037-publish` and the installed verification version were inspected. W HEAD equals the method commit; S HEAD equals the source revision and source Git status is empty. W status shows only its untracked publication directory. Preparation commit/path-prefix and overview identities agree.

| Exact binding | SHA-256 |
|---|---|
| Preparation | `a15274b3df8ddf93dd17654bde2b1c03954ab2e76c24d1b8245ad7fdec8db788` |
| Publication effect | `9dc671cc82fd96840b4ef8e2fe5f059c96143ff7ad8ed23dc8d6dcb0cd79c4aa` |
| External log L | `6eb8f5c7fee38dbd3f20666bc5f6e672510f24158b4561aa1e16840f0486bb80` |
| P/ARTIFACT.yaml | `a3d9788df8357a625bcb105c2045219fb9a39c8a7232a7957a9082cbf2e50c8c` |
| P/runtime.md | `eaef3cdd36b6afc2bf401963a65bea5aa146a6356a85c37994207b041b5fca69` |
| P/synthesis.md | `78823bc3c69910b2fb3260ea2a5164c430b80dc3bfa8870bce0dc3e8476dfb8e` |

The complete maps and exact paths remain in [intake cases.contextpilot](../batch-23-audit-intake.json). These checks bind publication, not integration readiness or every worker obligation.

## Consequential source finding

The historical accounts supplied the question, not its answer. Direct inspection established this chain at S:

1. `train/verl/experimental/agent_loop/agent_loop.py:1006–1008` fills missing batch `agent_name` with `config.agent.default_agent_loop`. At `1080–1121`, the worker selects that registry entry, instantiates it and calls its `run`.
2. `train/verl/experimental/agent_loop/statelm_agent_loop.py:451–452` registers the ContextPilot loop as `statelm_tool_agent`.
3. `train/verl/trainer/config/rollout/rollout.yaml:207–208` sets the default to `single_turn_agent`. `ppo_trainer.yaml:8–36` imports that rollout configuration. The complete launcher-selected `train/examples/sglang_multiturn/config/statelm_tool_agent_grpo.yaml` inherits `ppo_trainer` without overriding the selector.
4. The complete `train/sh/run_qwen3-8b_longbenchv2.sh` supplies tools, ContextPilot/partial-rollout flags and the estimator, but no default-loop override. It consumes external transformed Parquet files. P/boundary.md explicitly retains the separately downloaded training-data gap.
5. `train/verl/experimental/agent_loop/single_turn_agent_loop.py:26–64` registers the fallback and performs single-turn generation, not the ContextPilot tool/context-management loop.

This establishes a condition, **not** that actual training selected the wrong loop, that the dataset lacks its selector, or that the ContextPilot learning implementation is absent. ContextPilot and partial-rollout flags do not themselves establish the class selection.

Affected exact publication:

- `P/runtime.md:43–45` connects the training launcher to context-management snapshots and updates without the prerequisite. `RT-RTE-training-rollout` at `187–202` names the StateLM owner and lists ContextPilot/partial-rollout configuration as selection, but omits loop dispatch.
- `P/synthesis.md`, “From rollout experience to a changed actor,” carries the branch/snapshot/update account without the selector or generic alternative. Its limitations withhold execution, exact models, data reproduction and downstream deployment, not this entry condition.
- `P/boundary.md:35–47` includes training snapshot consumers and says the recipe was traced through reward/update recovery without identifying conditional dispatch.
- `P/report-verification.md` accepts the runtime/training chain and declares no blockers; its omission search addresses synthetic cleanup and alternate inference callers, not this training selector. Synthesis verification accepts the dependent public account. Neither acceptance supplies the missing evidence.

A search across every published Markdown member found no `agent_name`, `default_agent_loop`, `single_turn_agent` or `statelm_tool_agent`. The missing qualification therefore cannot be recovered elsewhere in this set. The synthesis contract requires preserving conditions that change whether a mechanism operates; an audit-only qualification cannot repair its absence.

## Historical coverage and retained public limits

Read both intake-listed audits and the [archived review linked by systems.md](../../../agentic-systems/reviews-archive/contextpilot.md). All address the same source revision; a newer cutoff does not explain loss of its explicit dispatch condition. Their older traces, reset lineage and conclusions were not freshly certified here. The archived detailed result and depth investigations were not reopened.

The new public account preserves useful distinctions: per-sample stores rather than established cross-task autobiographical reuse; full-tool fallback and alternate base inference; mechanical review versus relevant semantic checking; original-history retention versus restoration availability; sampled-word compression and best-effort token windows; optional merge rather than default execution; descendant reward versus individual-action merit; conditional trainable synthetic cleanup; and wired updates versus exercised behavior or benefit. It additionally carries its verifier's selective recovery inventory, including automatic highest-ranked-chunk delivery, in public limitations. These are favorable coverage observations, not independent source certification of every statement.

Historical numerical-gradient/checkpoint details, reflection interpretations and all memory axes were not exhaustively compared. No disposition on those unsettled differences is needed to decide this hold. Further reconstruction stops at the established dispatch defect.

## Bounded operational evidence

Parsed settled outer `message_end` subagent results in L, not repeated stream snapshots. There are 13 analytical worker results plus the diagnostic; all report exit zero. Sampled boundary, runtime and report-verification nested messages. Calls below were paired with results by exact ID **inside the same worker**; message indices are zero-based:

| L line / worker | Nested messages and exact call ID | Established action |
|---|---|---|
| 765 / `000003-boundary` | 14→15, `call_pRR3JZVrTMsIuPg4KFfCYevA\|fc_0515a0a65cb57ba6016ad619fad61487d2a587ff20d540472c` | Read S/README.md; result `isError: false`. |
| 1151 / `000005-runtime` | 21→22, `call_4dn8R5m7QhIdNiL4DYbyazIR\|fc_0687e270c4ecda2f016ad61adfc52887d2ad9b6e60726be3b2` | Read S/infer/src/contextpilot_fsm.py, offset 1, limit 175; result `isError: false`. |
| 2844 / `000022-report-verification` | 50→51, `call_OJqajN9ZVTw5hniLBgmkX4Av\|fc_0f8f1bd538f955a7016ad61f02d60887d2a59697afaddc2eca` | Read S/infer/src/contextpilot.py, offset 580, limit 210; result `isError: false`. |
| 2844 / same verifier | 95→96, `call_fyStK0VkoVHx2UvLWkIgKvIX\|fc_0f8f1bd538f955a7016ad61f62c11087d2b7136cd2e86ca6f2` | Successful write to its handout `outputs/verification.md`; later 99→100 successfully edits that same output. |

The last row is evidence of actual output mutation, not an unexecuted suggestion. The submitted verification hash is the installed report-verification version. Source-read samples establish some independent inspection, not inspection of the missing dispatch condition. No new operational violation was established by these bounded samples. Complete invocation recovery, all executed shell effects, every write's authorization, indirect legacy exposure, unsampled worker compliance and current writer idleness were **not certified**. Publication success and zero worker exits do not discharge those obligations or clear historical incidents.

## Validation and limits

From W with `PATH=W/.venv/bin:$PATH`, ran only read-only validation, not a run/engine command:

```text
commonplace-validate kb/agentic-system-analyses/retained/tencent--contextpilot
VALIDATION SUCCESS
Target: kb/agentic-system-analyses/retained/tencent--contextpilot
Scope: kb/agentic-system-analyses/retained/tencent--contextpilot
Files analysed: 1
Text files: 0
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

The count denotes one directory artifact, not twelve separately counted documents. From the same prepared environment, report validation returned:

```text
commonplace-validate /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch-23-contextpilot.md
VALIDATION SUCCESS
Target: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch-23-contextpilot.md
Scope: /home/zby/llm/commonplace/kb/work/agentic-system-reruns/audits/batch-23-contextpilot.md
Files analysed: 1
Text files: 1
Diagnostics: 0 failures across 0 subjects; 0 warnings across 0 subjects
```

Deterministic success does not resolve the semantic hold.

Only this assigned report was authored. No analysis/source/state changes, delegation, commits, run effects, integration, acquisition, target execution, cleanup, termination or push occurred. No analyst feedback was sent. Other reports and unpublished timeout cases were outside scope. Actual dataset selection and target benefit remain unknown; no missing source prevents stating the established condition.
