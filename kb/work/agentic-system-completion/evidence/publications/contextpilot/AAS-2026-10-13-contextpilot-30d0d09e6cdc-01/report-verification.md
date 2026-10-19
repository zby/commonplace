---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of ContextPilot's inference, memory, evaluation and training account at the frozen revision."
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot report verification

## Verification

### Judgment and evidence

The current reports support a bounded source-grounded account. The three previous blockers are resolved. I read the complete boundary, five reports, correction answers, structural check and previous verification. The structural check says `none`, so there is no structural failure to route. I assessed every declared record, its source anchors, evidence status and consumer claims, the three explicit `Part of:` relations, the three supersessions and the reconciliation's disagreement dispositions. There are no declared evidenced-absence records. The epistemic ledger's local no-integration finding does not assert system-complete absence.

Independent inspection used only SRC-1 within the [Source register](boundary.md#source-register). Checkout HEAD matched the frozen revision and tracked status was clean. Source reads and searches establish implementation or shipped doctrine, not observed execution. No target code, tests, examples, providers or benchmarks were executed. External weights, dataset payloads and deployment internals remain outside the inspected evidence.

### Corrections and reconciliation

I independently traced the changed prediction handoff through SRC-1, `infer/src/hf_test_runner.py`, and both extraction implementations in `infer/src/contextpilot.py`. The runner obtains its prediction from `logger.save_final_result`; reverse tool-history scanning selects a truthy `content.final_answer` without testing the tool name, otherwise returning the failure placeholder. `_extract_final_answer` instead supplies the trajectory snapshot and can fall back to assistant prose. The revised invocation account, [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference), [EPI-OBJ-answer-content](epistemic.md#epi-obj-answer-content) and dependent offline-evaluation conclusion now preserve this distinction. The correction answers agree with source, rather than serving as evidence for it. The [workflow delivery account](workflow.md#what-counts-as-delivered) remains supported: recording a selected answer or placeholder need not establish successful protocol completion. Both previous prediction-lineage blockers are discharged.

I reread the merge mutation, wrapper, rendering and read methods in SRC-1, `infer/src/contextpilot.py`, and searched inference grants and training configurations/callers. [EPI-RTE-memory-merge](epistemic.md#epi-rte-memory-merge) now gives implementation conclusion `afforded`, matching [MEM-RTE-memory-merge](memory.md#mem-rte-memory-merge). Its ledger's separate architectural status `implemented` describes inspected code, explicitly not established invocation wiring. Both preserve destructive concatenation, metadata loss, subsequent availability and the missing shipped caller connection. The previous merge-status blocker is discharged; neither supported implementation nor its limitations were erased.

The [reconciliation](reconciliation.md#reconciliation) accurately disposes both former disagreements without overriding an analyst's fields. Its document/index, simple-note and merge supersessions have same-referent evidence. The broader epistemic structured-memory object and findings-retention route remain valid containers beside memory's more detailed parts; no split supersession is necessary. Context-replacement content is part of history, its transformation is part of context control, and terminal answer reward is part of branch credit. All three containment relations are supported. No unresolved current conflict requires correction.

### Runtime, memory and workflow

Source tracing of SRC-1, `infer/src/contextpilot_fsm.py`, `infer/src/contextpilot.py` and `infer/src/hf_test_runner.py` supports the ordinary/FSM distinction, state-local allowed-tool enforcement, count-based evidence readiness, cleanup/review handoffs and deterministic latest-key recovery. The allowed-tool full-set fallback and ordinary global-membership dispatch qualify [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating). Successful reader return is not independent fact checking, exhaustive review or demonstrated incorporation. This preserves the [workflow account](workflow.md#workflow-account), not a universal completion guarantee. The shipped prompt supports the requested behavior in [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) and [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance), not reliable semantic compliance.

CRUD, neighbor projection and renderer reads in SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py` and the training wrappers support [MEM-RTE-findings-write](memory.md#mem-rte-findings-write), [MEM-RTE-findings-delivery](memory.md#mem-rte-findings-delivery) and [EPI-RTE-findings-retention](epistemic.md#epi-rte-findings-retention). Content, simple notes, symbolic metadata/edges and dense vectors have distinct consumers; source IDs and graph scores do not authenticate remembered propositions. All current summaries are advertised without query ranking or an independent summary-list budget. Keyed reads return a full selected entry and bounded neighbor projections. Deletion does not purge old history or branch copies. Training's omitted-summary erasure is a genuine implementation difference, not uniform store parity.

I checked history replacement, explicit restoration and the token-window stopping branch in SRC-1, `infer/src/contextpilot.py`. They support [RT-OBJ-full-history](runtime.md#rt-obj-full-history), [RT-RTE-context-control](runtime.md#rt-rte-context-control) and their memory annotations. Originals remain separate from rendered replacements; default grants do not provide the implemented restore action; eviction can exhaust candidates while still oversized. The substring operations support the denial-removal deduction in [EPI-RTE-context-replacement](epistemic.md#epi-rte-context-replacement). It is a source-derived counterexample, not an observed false answer. Random-word fallback likewise warrants no semantic-preservation guarantee.

The policy, actor, judge, compressor, embedding and reranker component records distinguish local adapters from provider parameters. Source configuration and update paths support their different roles and mutability accounts. No exact deployed version follows from a model name. Document/index and chunk-vector findings concern source selection, not learned policy tensors. The adapter transformations in SRC-1, `infer/src/hf_process_fns.py`, support [EPI-RTE-document-selection](epistemic.md#epi-rte-document-selection): LongMemEval removes answer-location fields; BrowseComp+ flattens shuffled document text. These transformations retain bounded lineage, not independently established source warrant.

### Evaluation and training

I checked parser/aggregation passages in SRC-1, `infer/src/hf_score_fns.py`, and the complete training scorer in `train/verl/utils/reward_score/statelm_qa.py`. [EPI-RTE-offline-evaluation](epistemic.md#epi-rte-offline-evaluation) correctly separates post-output labels from a pre-emission veto. LongMemEval's default-false parsing and BrowseComp+'s exclusion of parse-error judgments have different denominator consequences. [EPI-RTE-answer-reward](epistemic.md#epi-rte-answer-reward) correctly separates letter matching, model reference comparison and format penalties; client initialization precedes the judge retry fallback. These mechanisms assess reference agreement and protocol shape, not the truth of every saved finding.

Independent reads of pre-generation capture, branch reconstruction and tool-processing order in SRC-1, `train/verl/experimental/agent_loop/statelm_agent_loop.py`, support the pre-action account in [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit). Cloning copies retained stores and edit maps; it is not an independently varied single-action causal experiment. Reward assignment in `train/verl/experimental/agent_loop/agent_loop.py` drops snapshots lacking terminal descendants and averages descendant rewards. The estimator in `train/verl/trainer/contextpilot/adv.py` normalizes within query identity. Finite-gradient admission in `train/verl/workers/actor/dp_actor.py`, weight transfer in `train/verl/workers/fsdp_workers.py` and save/load in `train/verl/trainer/ppo/ray_trainer.py` support [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) and [RT-BAP-rollout-weights](runtime.md#rt-bap-rollout-weights).

Thus training has an implemented trace-to-parameter-to-later-consumer path, unlike raw log retention alone. No supplied evidence establishes exercised update-dependent behavior, improved future capacity or causal benefit. The reports appropriately keep these questions separate from theory criticism and reflection. The prompt and README support [EPI-CLM-grounded-answer](epistemic.md#epi-clm-grounded-answer), [EPI-CLM-branch-credit](epistemic.md#epi-clm-branch-credit) and [EPI-CLM-performance-gains](epistemic.md#epi-clm-performance-gains) at their respective doctrine and attributed-report layers, not reproduced superiority.

### Consequential omission search and stopping decision

I selected omission questions from the frozen top-level tree, alternate inference dispatch, task-state producers/consumers and launcher-selected training paths. The material questions were whether resume reloads old findings; whether prediction recording follows the trajectory helper; whether another grant/caller establishes optional merge or restore wiring; and whether branch reconstruction or checkpoint consumers invalidate the bounded adaptation account.

Runner reads resolve resume as sample skipping and retry hints as fresh-agent feedback, not store reload. Logger/helper reads resolve the output-lineage question and confirm the corrections above. Searches covered inference scripts/source/grants, training launchers, tool implementations and both selected and non-selected StateLM configuration surfaces. Names in an alternative configuration do not alone establish executable caller wiring. The reports already withhold exhaustive schema parity and universal grant claims; the optional capability findings remain valid. Branch timing, terminal reward consumers and configured reload paths support the reported training chain without supplying its missing execution or benefit evidence.

Further optional search stopped because these questions have supported dispositions and no identified material challenge remains unresolved. Generic verl backends, arbitrary configuration sequences and provider internals were not exhaustively audited. The reports do not emit complete-coverage, universal coherence or deployed-reliability findings requiring that audit. Their scoped uncertainties already prevent stronger comparisons; they are not new publication limits or evidenced absences.

## Blockers

none

## Limits

none
