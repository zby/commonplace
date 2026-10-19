---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ContextPilot epistemic routes: document evidence, saved findings, context replacement, answer evaluation and reward-driven policy authority."
run-id: AAS-2026-10-13-contextpilot-30d0d09e6cdc-01
reviewed-boundary: "782cbb6611fb610c4cf6fafda6022b7e89cae191"
---

# ContextPilot epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on ContextPilot's document-QA findings and answers, and what its evaluators actually change. Scope, exclusions, frozen source and external dependencies are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All new source inspection below is SRC-1 at that same commit. No target code, tests, model requests or benchmarks were executed. Code deductions below are implementation evidence, not observed operation.

The assessed families are document acquisition and selection; model-authored findings and answers; memory admission, revision, withdrawal and read-back; context replacement and restoration; FSM protocol checks; offline answer grading; and training's answer reward, branch-credit disposition and parameter-update consumer. The consequential claims are [EPI-CLM-grounded-answer](#epi-clm-grounded-answer), [EPI-CLM-branch-credit](#epi-clm-branch-credit), [EPI-CLM-performance-gains](#epi-clm-performance-gains), and the narrower supplied [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating).

| Entry point or operation | Source path, SRC-1 | Coverage and records |
| --- | --- | --- |
| Task launcher and ordinary/FSM runner selection, retry hint, prediction saving | `infer/scripts/eval_task.sh`; `infer/src/hf_test_runner.py` | Direct reads of full task launcher and runner sample loop; supplied [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference). Retry hint supplies attributed negative feedback, not a revalidated fact or old-store reload. |
| Dataset adapters, indexing, keyword search, chunk reads | `infer/src/hf_process_fns.py`; `infer/src/contextpilot.py` | Direct adapter file and analyze/index/search/read bodies; [EPI-RTE-document-selection](#epi-rte-document-selection). |
| All 18 default tool grants and training registrations | `infer/tools/context-shaper_tools.json`; `train/examples/sglang_multiturn/config/tool_config/statelm_tool_optimized_config.yaml` | Direct full schema/config reads. The latter is the ContextPilot launcher-selected configuration, not unrelated generic examples. Supplied training loop wiring: [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout). No separate hook layer is identified by these dispatch paths; this is not an audit of arbitrary installed plugins. |
| memorize/updateMemory/note/updateNote, readNote/loadMemory, related-memory ranking | `infer/src/contextpilot.py`; `train/verl/tools/statelm_tools.py`; `train/verl/tools/contextpilot_memory.py` | Direct inference write/read/update/graph bodies and training wrappers/write/update bodies; [EPI-RTE-findings-retention](#epi-rte-findings-retention). Training graph internals were not fully read; no claim of identical graph scoring across implementations. |
| delete/truncate/summarize/compress; explicit restore; loadDocument; mergeNotes; budget/stat tools | `infer/src/contextpilot.py`; `train/verl/tools/statelm_tools.py` | Direct edit, rendering, merge, loadDocument and training context-tool bodies. [EPI-RTE-context-replacement](#epi-rte-context-replacement), [EPI-RTE-memory-merge](#epi-rte-memory-merge); supplied [RT-RTE-context-control](runtime.md#rt-rte-context-control). Restore, loadDocument and mergeNotes are exposed implementation alternatives, not default JSON grants. Budget/count results control capacity, not document truth. |
| Optional buildEmbedding/semanticSearch/hybridSearch/reranker | `infer/src/contextpilot.py` | Direct selection and reranker request/response bodies; [EPI-RTE-document-selection](#epi-rte-document-selection). Provider internals and embedding provenance are uninspected; relevance is not factual validation. |
| plan, FSM review/finish and fallback progression | `infer/src/contextpilot.py`; `infer/src/contextpilot_fsm.py`; `infer/configs/fsm_plan_bm25_mc_prompt.txt` | Direct plan validator, full prompt and transition body; supplied normal/forcing paths in [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference). No exhaustive independent reread of the 1,500-line FSM run loop; hard-stop and API-failure findings use runtime evidence. |
| Offline scoring CLI and result consumers | `infer/src/hf_score_fns.py`; `infer/scripts/eval_task.sh` | Direct all four CLI mappings, correctness helpers, judge requests/parsers, annotators and aggregates; [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation). |
| Training reward and subtree rejection/assignment | `train/verl/utils/reward_score/statelm_qa.py`; `train/verl/experimental/agent_loop/agent_loop.py` | Direct full scorer and terminal-penalty/subtree-assignment bodies; [EPI-RTE-answer-reward](#epi-rte-answer-reward), supplied [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit). Branch scheduling/entropy and later actor/checkpoint consumers use supplied runtime, not a fresh full-source audit. |
| Training advantage, optimizer, weight transfer, checkpoint/resume | `train/verl/trainer/contextpilot/adv.py`; `train/verl/trainer/ppo/ray_trainer.py`; `train/verl/workers/actor/dp_actor.py`; `train/verl/workers/fsdp_workers.py` | Supplied [RT-RTE-policy-update](runtime.md#rt-rte-policy-update), [RT-BAP-rollout-weights](runtime.md#rt-bap-rollout-weights), [RT-CMP-actor-module](runtime.md#rt-cmp-actor-module); not independently reread. |

Missing frozen dataset payloads prevent verification of source/reference truth and exact benchmark reconstruction. Missing weights and deployed endpoint internals prevent individuating the policies' internal propositions or checking their factual transformations. Missing run traces prevent asserting that any candidate was actually generated, accepted, used or improved. Missing controlled comparisons prevent attribution of gains or one edit's causal contribution. Optional routes and partly supplied training/FSM coverage remain individually bounded; this report makes no system-complete negative about all possible acceptance or theory routes.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-document-index](#epi-obj-document-index) | see [EPI-OBJ-document-index](#epi-obj-document-index) | see [EPI-OBJ-document-index](#epi-obj-document-index) | SRC-1, `infer/src/hf_process_fns.py` | Document truth is not independently authenticated. |
| [EPI-OBJ-memory-content](#epi-obj-memory-content) | see [EPI-OBJ-memory-content](#epi-obj-memory-content) | see [EPI-OBJ-memory-content](#epi-obj-memory-content) | SRC-1, `infer/src/contextpilot.py` | Semantic preservation is not established by normalized structure. |
| [EPI-OBJ-simple-notes](#epi-obj-simple-notes) | see [EPI-OBJ-simple-notes](#epi-obj-simple-notes) | see [EPI-OBJ-simple-notes](#epi-obj-simple-notes) | SRC-1, `train/verl/tools/statelm_tools.py` | No model-written entry instances supplied. |
| [EPI-OBJ-context-replacements](#epi-obj-context-replacements) | see [EPI-OBJ-context-replacements](#epi-obj-context-replacements) | see [EPI-OBJ-context-replacements](#epi-obj-context-replacements) | SRC-1, `infer/src/contextpilot.py` | Meaning can change despite success status. |
| [EPI-OBJ-answer-content](#epi-obj-answer-content) | see [EPI-OBJ-answer-content](#epi-obj-answer-content) | see [EPI-OBJ-answer-content](#epi-obj-answer-content) | SRC-1, `infer/src/contextpilot.py` | Entailment from document uninspected at instance level. |
| [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | see [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | see [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | SRC-1, `infer/src/hf_score_fns.py` | Criterion-relative judgments, not source authentication. |
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | see [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | see [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt` | Guidance is not enforced semantic criticism. |
| [RT-OBJ-full-history](runtime.md#rt-obj-full-history) | see [RT-OBJ-full-history](runtime.md#rt-obj-full-history) | see [RT-OBJ-full-history](runtime.md#rt-obj-full-history) | SRC-1, `infer/src/contextpilot.py` | Plan prose and IDs have different consumers; see supplied split. |
| [RT-CMP-vllm-client](runtime.md#rt-cmp-vllm-client), [RT-CMP-actor-module](runtime.md#rt-cmp-actor-module), [RT-CMP-judge-answer](runtime.md#rt-cmp-judge-answer), [RT-CMP-llmlingua2](runtime.md#rt-cmp-llmlingua2) | not determinable for internal distributed-parametric truth-apt contents | see cited components | SRC-1, `infer/src/contextpilot.py`; `train/verl/utils/reward_score/statelm_qa.py` | Fixity, mutability and weight/version limits remain component-specific; tensor change does not individuate a proposition. |

## Authority-route ledger

The ledger separates checking, disposition, retention and use even where one declared implementation spans several functions. A `see` cell delegates the field to its declaring record, not to an inferred global property. All implemented rows have unobserved activation; possible results are not run results.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-document-selection](#epi-rte-document-selection) | content transformation | implemented | [EPI-OBJ-document-index](#epi-obj-document-index) | truth-apt transformation: acquisition/import | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | none | none | Source warrant unknown; transformed presentations retain only bounded lineage. |
| [EPI-RTE-document-selection](#epi-rte-document-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-document-index](#epi-obj-document-index) | no content change | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | see [EPI-RTE-document-selection](#epi-rte-document-selection) | none | none | Relevance selects evidence exposure; not truth. |
| [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | content transformation | implemented | [EPI-OBJ-answer-content](#epi-obj-answer-content) | truth-apt transformation: indeterminate | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | none | Without candidate/input pairs, copying, derivation and conjecture remain distinguishable alternatives. |
| [EPI-RTE-findings-retention](#epi-rte-findings-retention) | retention | implemented | [EPI-OBJ-memory-content](#epi-obj-memory-content) | truth-apt transformation: indeterminate | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | none | Model-written payload may copy or change meaning; stored status is not acceptance. |
| [EPI-RTE-findings-retention](#epi-rte-findings-retention) | operational admission/selection/consumption | implemented | [EPI-OBJ-simple-notes](#epi-obj-simple-notes) | no content change | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | none | none | Summaries delivered automatically; full entries by key. Delivery is not demonstrated reliance. |
| [EPI-RTE-memory-merge](#epi-rte-memory-merge) | content transformation | implemented | [EPI-OBJ-memory-content](#epi-obj-memory-content) | truth-apt transformation: non-ampliative reshaping | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | see [EPI-RTE-memory-merge](#epi-rte-memory-merge) | none | none | Afforded capability, no shipped caller established. Default concatenation only; supplied new summary has indeterminate semantics. |
| [EPI-RTE-context-replacement](#epi-rte-context-replacement) | content transformation | implemented | [EPI-OBJ-context-replacements](#epi-obj-context-replacements) | truth-apt transformation: indeterminate | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | see [EPI-RTE-context-replacement](#epi-rte-context-replacement) | [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | semantic-preservation limit | Exact substring extraction can change a proposition; see concrete code deduction. |
| [RT-RTE-context-control](runtime.md#rt-rte-context-control) | lineage/freshness/recovery | implemented | [RT-OBJ-full-history](runtime.md#rt-obj-full-history) | no content change | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | none | none | Restoration changes visibility, not source endorsement; default grant lacks restoreContext. |
| [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | check/evidence production | implemented | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating) | none | Successful reader call satisfies review flag; not an answer-evidence acceptance test. |
| [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | disposition/acceptance | implemented | [EPI-OBJ-answer-content](#epi-obj-answer-content) | no content change | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | see [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | operational, not epistemic acceptance | finish permits termination and saving; empty-search/budget forcing permits best effort. |
| [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | check/evidence production | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | truth-apt transformation: indeterminate | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | [EPI-CLM-performance-gains](#epi-clm-performance-gains) | none | Judgment of reference agreement; symbolic score is determinate given parsed labels, reference truth is not established. |
| [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | operational admission/selection/consumption | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | no content change | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | see [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation) | [EPI-CLM-performance-gains](#epi-clm-performance-gains) | none | Writes labels and aggregates after prediction; no pre-emission veto. |
| [EPI-RTE-answer-reward](#epi-rte-answer-reward) | check/evidence production | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | truth-apt transformation: indeterminate | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | see [EPI-RTE-answer-reward](#epi-rte-answer-reward) | [EPI-CLM-branch-credit](#epi-clm-branch-credit) | none | MC syntax/letter branch and external semantic judge have separate domains and failure behavior. |
| [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | disposition/acceptance | implemented | [EPI-OBJ-evaluation-results](#epi-obj-evaluation-results) | no content change | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | see [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) | [EPI-CLM-branch-credit](#epi-clm-branch-credit) | none | Training-row ancestry/terminal-evidence admission; no admission of memory claims as true. |
| [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | behavior/policy adaptation | implemented | [RT-CMP-actor-module](runtime.md#rt-cmp-actor-module) | non-truth-apt policy/content update: gradient-based numerical policy change | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | see [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | [EPI-CLM-performance-gains](#epi-clm-performance-gains) | none | Finite gradients gate steps, not demonstrated better quality; later rollout parameters have operative force. |
| [EPI-RTE-findings-retention](#epi-rte-findings-retention) | lifecycle integration | no route found within boundary | [EPI-OBJ-memory-content](#epi-obj-memory-content) | no content change | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | see [EPI-RTE-findings-retention](#epi-rte-findings-retention) | none | bounded absence | Inspected stores connect and expose candidates before any evidenced claim-acceptance decision; not a system-wide absence. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | see [EPI-CLM-grounded-answer](#epi-clm-grounded-answer) | SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, doctrine/design | see claim | [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [EPI-RTE-findings-retention](#epi-rte-findings-retention), [EPI-RTE-context-replacement](#epi-rte-context-replacement) | none supplied | no comparisons; exact semantic checking remains model guidance | Evidence acquisition and review opportunities are wired, not guaranteed entailment or completeness | Count/chronology rules and role checks are requested, not independent validators; best-effort exit and lossy replacements qualify warrant. |
| [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating) | see [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating) | SRC-1, `infer/src/contextpilot_fsm.py`, implementation/design | see claim | [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) | none supplied | no causal evidence; state-local and configuration-dependent | Protocol constraints, not fact acceptance | Ordinary/training/direct and fallback routes prevent universalization. |
| [EPI-CLM-branch-credit](#epi-clm-branch-credit) | see [EPI-CLM-branch-credit](#epi-clm-branch-credit) | SRC-1, `README.md`, doctrine/design | see claim | [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit), [EPI-RTE-answer-reward](#epi-rte-answer-reward), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | none supplied | Reward ancestry averages do not independently vary one edit | Implemented answer-outcome credit and numerical adaptation | Action-specific causal efficacy and correct mechanism attribution not established. |
| [EPI-CLM-performance-gains](#epi-clm-performance-gains) | see [EPI-CLM-performance-gains](#epi-clm-performance-gains) | SRC-1, `README.md`, reported operation | see claim | [EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) | none supplied | No controlled results registered; datasets/weights not frozen | Attributed performance report; implemented measurement machinery | Not reproduced superiority, smaller-context benefit or transfer. |

## Bounded conclusion

ContextPilot acquires document text and selects passages through indexed retrieval; it does not authenticate the document or reference answer. Adapters and chunk IDs provide partial lineage, but flattening documents and later editing can remove contextual qualifiers. Keyword/vector/reranker scores authorize exposure to the policy, not endorsement of a proposition ([EPI-RTE-document-selection](#epi-rte-document-selection)).

Model-written memory, simple notes, summaries, plans and answers are candidate content. Their copying, warranted derivation or non-entailed inference cannot be classified instance-wise without inputs and outputs. Structural checks license storage and tool continuation. Later summary injection, keyed reads and related-entry ranking license operational availability within a task; they do not establish an evidence-consuming acceptance decision. Deletion and overwrite withdraw future availability, not a recorded judgment that the former proposition was false. The inspected store and graph paths therefore establish candidate retention and organization, not post-acceptance lifecycle integration; the optional merge is an afforded capability without an established shipped caller ([EPI-RTE-findings-retention](#epi-rte-findings-retention), [EPI-RTE-memory-merge](#epi-rte-memory-merge)).

Exact extraction is not automatically a truth-preserving derivation: the concrete substring countercase in [EPI-RTE-context-replacement](#epi-rte-context-replacement) removes a denial while retaining its embedded proposition. The compressor fallback can also remove arbitrary words, including qualifications. No universal semantic-preservation guarantee follows from successful editing. Original-history access and optional restore can recover bytes, not establish which version deserves belief ([RT-RTE-context-control](runtime.md#rt-rte-context-control)).

FSM checking constrains action legality and review timing; successful read-back marks review satisfied, and `finish` operationally terminates. It does not consume independent evidence against an answer-truth criterion before release. The source prompt asks the policy to check counts, chronology and relation direction, but reliable semantic compliance is unobserved ([RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [EPI-CLM-grounded-answer](#epi-clm-grounded-answer)).

Offline graders judge benchmark reference agreement after output, under task-specific criteria: permissive letter parsing, rubric or semantic equivalence, temporal tolerance, updated-answer allowance and abstention. Their target is the runner's logger-selected prediction, including its failure placeholder, not the separate trajectory helper's assistant-prose fallback. Their force is recording labels and aggregates; no inspected automatic truth-store admission or pre-answer veto follows. Parse failures have different denominator effects across LongMemEval and BrowseComp+, so reported scores cannot be interpreted as a uniform oracle ([EPI-RTE-offline-evaluation](#epi-rte-offline-evaluation)).

Training evaluation has a separate consequential consumer. Reference-letter or model-judge decisions, format penalties and tool/budget flags feed subtree rewards and query-relative advantages, then actor updates and rollout weight transfer. This is implemented evidence-responsive adaptation with a numerical behavioral-authority path, not acceptance of a formulated explanation or a guarantee that each saved finding is true. Finite-gradient and terminal-lineage gates are operational admission criteria, not promote-only-if-better validation. Exact judge/actor versions and internal proposition content remain uninspected ([EPI-RTE-answer-reward](#epi-rte-answer-reward), [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit), [RT-RTE-policy-update](runtime.md#rt-rte-policy-update)).

No produced accepted ampliative claim is established by this evidence. That is an evidentiary limit, not proof that a model never conjectures or derives. Improved future capacity, exercised self-improvement, reflection and theory-building remain independent questions: the supplied runtime establishes the adaptation wiring and its missing later update-dependent execution link, not beneficial learning or content-directed criticism. The public performance report remains attributed, without observed or causal support in this run ([EPI-CLM-performance-gains](#epi-clm-performance-gains)).

## Shared records

### Operative objects

#### EPI-OBJ-document-index
Label: Document text and chunk index

Source-native identity: `document`, `encoded_doc`, `index`, dataset context adapters. Natural-language document propositions coexist with symbolic chunk IDs, token offsets and heuristic section hints; the latter locate content, not verify it. Substrate: per-agent Python strings/lists and a document-filtered Elasticsearch index. Distinct from [RT-OBJ-full-history](runtime.md#rt-obj-full-history): this is the source/index supplying selected history entries, not history itself. SRC-1, `infer/src/hf_process_fns.py`, `infer/src/contextpilot.py`. Imported document/reference warrant is unknown; no independent source verification is evidenced by these adapters.

> chunk_content = self.document[char_start:char_end]
> --- `infer/src/contextpilot.py`

#### EPI-OBJ-memory-content
Label: Structured memory entries

Source-native identity: inference `notes` and training `memories`, with full content, summary, entities, episodes, relations and source IDs. Natural-language propositions receive model interpretation; symbolic keys, source-ID arrays, graph caches and scores govern storage/selection. Substrate: per-task Python dictionaries, separate from full history. Closest supplied [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) describes their junction but declares no store object. These entries are not a second declaration of history. Content and provenance are model-supplied, not checked warrants. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/contextpilot_memory.py`; passages in [EPI-RTE-findings-retention](#epi-rte-findings-retention).

#### EPI-OBJ-simple-notes
Label: Simple note entries

Source-native identity: `simple_notes` entries, summary/full_content (and training content alias). Natural-language findings and summaries; symbolic key membership selects entries. Substrate: separate per-agent/per-trajectory Python dictionary. Distinct from structured memory because it lacks the structured source/relations fields and related-memory graph, and has its own read/update path. Closest supplied [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout) mentions the renderer without declaring this object. SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`.

> self.simple_notes[str(key)] = {"summary": str(summary), "full_content": str(content)}
> --- `infer/src/contextpilot.py`

#### EPI-OBJ-context-replacements
Label: Edited history replacements

Part of: [RT-OBJ-full-history](runtime.md#rt-obj-full-history)

Source-native identity: `summarized_msg_ids`, `truncated_msg_ids`, `compressed_msg_ids` and deletion stubs. Natural-language replacement content is interpreted by the next model; symbolic message-ID membership controls rendering precedence. Substrate: process-local maps/sets accompanying originals. Candidate truth-apt summaries and excerpts differ from non-truth-apt deletion notices. Split from the history container because edit admission is not a factual check, and replaced evidence has a different visibility path. SRC-1, `infer/src/contextpilot.py`; evidence in [EPI-RTE-context-replacement](#epi-rte-context-replacement).

#### EPI-OBJ-answer-content
Label: Submitted answer text

Source-native identity: `finish` argument `answer`, result `final_answer`, and runner's logger-selected prediction. Natural-language answer or symbolic MC option; substrate: tool-call/history objects, output JSONL and result files. Distinct from the history container because the runner records a selected answer field or failure placeholder, and from evaluation labels because that saved prediction is their target. `save_final_result` scans tool messages in reverse for a truthy `content.final_answer`, without checking the tool name, and otherwise selects `"No final answer found."`. The runner uses its returned value in the inference result and prediction JSONL. `_extract_final_answer` instead prefers a finish result and otherwise the latest undeleted assistant text; it populates `save_trajectory`'s snapshot, not the benchmark prediction. Closest supplied [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) owns the completion and logger handoff behavior. SRC-1, `infer/src/contextpilot.py`, `infer/src/hf_test_runner.py`.

> if not final_answer:
>     final_answer = "No final answer found."
> --- `infer/src/contextpilot.py`

> res_file, final_answer = logger.save_final_result(agent, question, correct_ans, meta_info)
> --- `infer/src/hf_test_runner.py`

> "final_answer": self._extract_final_answer(),
> --- `infer/src/contextpilot.py`

> return {"final_answer": params.get("answer", "No final answer provided.")}
> --- `infer/src/contextpilot.py`

#### EPI-OBJ-evaluation-results
Label: Answer judgments and rewards

Source-native identity: `correct_list`, `autoeval_label`, `autoeval_judge`, terminal `score` and subtree reward metadata. Symbolic booleans/scalars have fixed aggregation/optimization consumers; judge reasoning and matched spans are natural-language supporting fields, not independently verified proofs. Substrate: output JSONL/text files or training trajectory metadata/tensors. Distinct from [RT-CMP-judge-answer](runtime.md#rt-cmp-judge-answer), a producing service, and from [RT-CMP-actor-module](runtime.md#rt-cmp-actor-module), the update consumer. SRC-1, `infer/src/hf_score_fns.py`, `train/verl/utils/reward_score/statelm_qa.py`, `train/verl/experimental/agent_loop/agent_loop.py`; passages in the evaluation routes below.

### Routes

#### EPI-RTE-document-selection
Label: Document acquisition and relevance selection

This material function spans both [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) and [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference), rather than duplicating either complete invocation. Endpoints: dataset context → adapter string → indexed chunks → keyword/vector/hybrid rank → preview or full read → policy context. Owner: adapters/tool library; model proposes queries/IDs; code validates IDs and selection limits. Target/domain: requested document passages for query relevance, not proposition truth. Keyword rank comes from Elasticsearch; cosine rank from external embeddings; optional reranker judges query/document relevance. Results rank and expose content; they confer no independent epistemic authority. Operational consumer: policy through tool results, ranking force for this task's subsequent calls.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search IDs, scores, highlights/previews and section hints; reads return indexed passages or errors.
- Later read-back: inapplicable — source index is ordinary current-task input state; separately saved findings have their own route.
- Delegated visibility: Search/embedding/reranker services receive queries and indexed or selected document text; policy receives selected previews/passages, not necessarily the full source.
- Selection predicate: Document-ID filter, keyword match, top-k cosine/reranker ordering, read ID/range limits. Hybrid may bypass insufficient BM25 recall, then semantically filter and backfill by BM25.
- Invalidation or expiry: Index rebuild/document cleanup and fresh task; no source-truth expiry check established.
- Activation or effect: Implemented exposure and rank; actual query quality, complete coverage and faithful answer use unobserved.
- Evidence limits: External model/service implementation and source/reference truth uninspected; optional relevance models receive no weight updates in inspected selection bodies, exact weights are not pinned, configurable endpoints may change models.

Acquisition/import preserves literal selected text in the inspected chunk slice, but source warrant remains unknown. Adapters also change lineage: LongMemEval removes `has_answer` and adds session/date headings; BrowseComp+ shuffles and concatenates evidence and negative document text without carrying their document IDs into that string. Metadata records some IDs separately, not a positional citation map. A concrete deterministic deduction: `_clean_longmemeval_session([{"content":"Mara arrived", "has_answer":true}])` yields a turn with `content` and no `has_answer`; `longmemevals_i2c` then JSON-serializes that cleaned turn under the session heading. This removes answer-location leakage, not an epistemic evaluation. SRC-1, `infer/src/hf_process_fns.py`, `infer/src/contextpilot.py`.

> {key: value for key, value in turn.items() if key != "has_answer"}
> --- `infer/src/hf_process_fns.py`

> return "\n\n".join(all_docs_text)
> --- `infer/src/hf_process_fns.py`

> return {"retrieved_chunk": [self.index[chunk_id]], "chunk_id": chunk_id}
> --- `infer/src/contextpilot.py`

> kept = [it for it in items if it["semantic_score"] >= SEM_THRESHOLD]
> --- `infer/src/contextpilot.py`

#### EPI-RTE-findings-retention
Label: Findings retention and operational reliance

Distinct material mechanism shared by [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference), [RT-RTE-ordinary-inference](runtime.md#rt-rte-ordinary-inference) and [RT-RTE-training-rollout](runtime.md#rt-rte-training-rollout): candidate tool arguments → store admission/update → summaries or keyed read → later policy call. It is not a second complete inference loop. Owner: foreground model proposes content under the shipped evidence-saving prompt; software admits by key/mode/content requirements, not per-content human approval. Target/domain of checks: key existence and operation shape. No independent comparison of each finding to document evidence in these write bodies. Truth-apt input/output relation is indeterminate: a call could copy a passage, reshape it, derive or conjecture; no instance supplied decides which. Store success grants operational availability, not epistemic acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Write/update/delete status or missing-key/invalid-mode error; readers return copies of entries and, for structured memory, ranked related summaries/episodes.
- Later read-back: Current memory/note summaries injected into first user-message rendering; explicit readNote/loadMemory results deliver selected full content into later calls. Training renderer delivery is supplied by the runtime route.
- Delegated visibility: Policy endpoint receives rendered summaries/results; local store keeps full entries. Source-ID arrays are not dereferenced into factual validation during admission.
- Selection predicate: Model key choice and store membership; inference graph scores shared entities, connecting relations, times/facets and optional embedding similarity, then returns top-related entries.
- Invalidation or expiry: Append/overwrite/delete under model proposal; structured updates reindex graph, deletion removes incident edges. Simple summaries can be separately changed; inference append without a new summary leaves the old one. Fresh task/trajectory resets the store.
- Activation or effect: Retention, organization and prompt delivery wired; no demonstrated semantic reliance or improved answer. A changed summary may influence later generation without any accepted claim.
- Evidence limits: Read-back is within task, not proven cross-session reuse. No candidate instances or independent truth acceptance supplied. Training graph scoring internals not fully inspected, so inference graph details are not projected to training.

There is no per-write oracle in this bounded QA route. Humans choose task/configuration; the model decides proposed facts and revisions, and software can veto malformed/missing-key operations. Overwrite/delete permit withdrawal; they do not retain a criticism explaining falsity or a transactional content-version rollback. The accepted input criterion is operational shape, intended use is later QA prompting, scope is the current task. Operational consumer is the policy via natural-language summary/reader channels, advisory semantic force for future turns. Graph ranking is an organization/use operation on unaccepted candidates, not post-acceptance lifecycle integration.

SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`, `train/verl/tools/contextpilot_memory.py`.

> self.notes[k] = self._build_memory(key, content, summary, entities, episodes, relations, source)
> --- `infer/src/contextpilot.py`

> self._reindex_memory(k, recompute_embedding=True)
> return {"status": "success", "key": key, "structured": True}
> --- `infer/src/contextpilot.py`

> external_context_summary = external_memory_summary + external_note_summary
> --- `infer/src/contextpilot.py`

> return related[:max(0, int(max_related or 0))]
> --- `infer/src/contextpilot.py`

> del self.notes[key]
> self._remove_from_graph(key)
> --- `train/verl/tools/contextpilot_memory.py`

#### EPI-RTE-context-replacement
Label: Semantic limits of context replacement

Part of: [RT-RTE-context-control](runtime.md#rt-rte-context-control)

This part assesses transformation of selected message text, not the whole history-recovery route. Endpoints: chosen original message → literal span/model-supplied summary/external compressor or random fallback → replacement map → later rendered model message. Owner: model selects edit and supplied summary; code validates message/role/boundaries; compressor proposes compressed text. Target/domain: message/role/span existence and requested size, not factual equivalence. Operational force: replacement bytes are enforced by renderer; the policy interprets the changed natural-language evidence on subsequent task calls. Epistemic license: no checked preservation of original propositions. General relation is indeterminate, not automatically non-ampliative merely because text becomes shorter.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success/length/fallback metadata, or invalid role/ID/span errors; not a semantic-preservation verdict.
- Later read-back: Replacement text persists in maps and reaches later payloads instead of originals; deletion supplies a stub. Memory summaries remain separately supplied.
- Delegated visibility: External compressor receives selected original message text; foreground model later receives replacement with a compression/summary/truncation notice.
- Selection predicate: Model-selected ID and endpoints; `find` chooses the first start and first later stop. Compression percentage is clamped; fallback samples words in original index order.
- Invalidation or expiry: Originals remain in history; explicit restore can clear edit maps when granted and eligible. Fresh agent clears maps. Delete rendering takes precedence over summary, then truncation.
- Activation or effect: Changed next-input text is wired, not observed successful evidence preservation or benefit.
- Evidence limits: Compressor output/weights uninspected; default JSON grants editing but not restore. Training edit bodies show analogous replacement, but no universal inference restore guarantee is inferred there.

Concrete deterministic deduction, not target execution: for an eligible assistant text `It is false that Mara arrived. Mara stayed home.`, choose start `Mara arrived.` and stop `Mara stayed home.`. The inspected `find`/slice yields `Mara arrived. Mara stayed home.` under the truncation notice. The embedded affirmative clause is no longer under `It is false that`; the output assertion that Mara arrived does not follow from the original denial. String fidelity inside the selected span therefore does not establish proposition preservation. This witness is a non-entailed semantic assertion caused by deterministic extraction, not evidence of model creativity or an observed false answer. The general route stays indeterminate because other selections are harmless.

SRC-1, `infer/src/contextpilot.py`, `train/verl/tools/statelm_tools.py`. Countercase search also inspected compression's failure branch: it returns sampled whitespace words and success metadata, so successful compression likewise cannot guarantee preservation of negation or attribution.

> start_idx = text.find(start_sentence)
> --- `infer/src/contextpilot.py`

> search_from = start_idx + len(start_sentence)
> stop_idx = text.find(stop_sentence, search_from)
> --- `infer/src/contextpilot.py`

> truncated = text[start_idx:stop_idx + len(stop_sentence)]
> --- `infer/src/contextpilot.py`

> sampled_indices = sorted(random.sample(range(len(words)), keep_count))
> return " ".join(words[i] for i in sampled_indices)
> --- `infer/src/contextpilot.py`

> self.summarized_msg_ids[msg_id_int] = compressed
> self.compressed_msg_ids.add(msg_id_int)
> self.restorable_msg_ids.add(msg_id_int)
> --- `infer/src/contextpilot.py`

#### EPI-RTE-memory-merge
Label: Optional structured-memory merge

Distinct from the context editor in [RT-RTE-context-control](runtime.md#rt-rte-context-control): this mutates the structured store, not a history rendering. Exposed `mergeNotes` dispatches `merge_notes` on structured `notes`, despite its name; default tool JSON does not grant it. Endpoints: existing structured entries → remove originals/edges → concatenate contents and default summaries → reduced-schema new entry. Owner: caller/model proposes keys and optional replacement summary; software selects existing entries, skips missing ones and rejects when none exist. Criterion is existence, not factual agreement. Default content concatenation is non-ampliative reshaping; optional authored summary's relation is indeterminate. Operational license is subsequent summary/read availability, not acceptance of merged claims. Provenance is degraded: the new entry contains summary/full_content, without original source/relations/entities fields or a rebuilt edge for the merged key in this body.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Success with merged_from/new_key, or no-notes-found error.
- Later read-back: If invoked, new entry summary is listed in memory rendering and its content is available by read_note/loadMemory; former keys no longer resolve. No shipped caller connection is established.
- Delegated visibility: Local store transformation; later policy receives merged summary/content, not the discarded structured provenance through this entry.
- Selection predicate: Existing keys among caller's supplied list; default key joins old keys, default summary joins summaries, content joins with newline.
- Invalidation or expiry: Destructive removal of selected originals and their graph edges; no per-merge version rollback shown; fresh task resets store.
- Activation or effect: Implemented optional store reorganization; no default-grant activation or observed quality benefit.
- Evidence limits: Direct/configured use is afforded, not established shipped wiring or default FSM behavior; concatenation does not resolve contradiction or qualify as accepted-claim integration. The full default inference JSON and selected training YAML grant no merge operation.

This is the same operation as the supplied peer fragment [MEM-RTE-memory-merge](memory.md#mem-rte-memory-merge), not a separately wired route. Its implemented mutation and renderer/read methods establish capability only; configured external invocation remains hypothetical. The ledger's architectural status `implemented` describes that inspected implementation, not a shipped caller connection. Generic caller identity leaves per-content human control unresolved; no answer oracle or human approval gate is used by this body. A hypothetical caller's proposal guidance is uninspected; recovery requires rewriting or another retained copy.

SRC-1, `infer/src/contextpilot.py`, `infer/tools/context-shaper_tools.json`, `train/examples/sglang_multiturn/config/tool_config/statelm_tool_optimized_config.yaml`.

> self.notes[merged_key] = {"summary": str(existing_summary), "full_content": str(merged_content)}
> --- `infer/src/contextpilot.py`

> merged_content = "\n".join([note[2] for note in notes_to_merge])
> --- `infer/src/contextpilot.py`

#### EPI-RTE-offline-evaluation
Label: Offline reference-answer evaluation

No supplied counterpart after comparison: [RT-RTE-fsm-inference](runtime.md#rt-rte-fsm-inference) ends in output recording, while [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) concerns training. This is the separately shipped post-output inference scoring CLI. Endpoints: prediction file/reference → letter heuristic or external judge → parsed label → annotated JSONL and aggregate score. Owner: evaluation script and scorer; humans configure reference datasets/endpoint, not each label. Expected answers are benchmark annotations, not discovered by the policy. Operating mode: bounded benchmark QA. No inspected evidence independently checks that reference answers are true.

Check targets and domains: InfBench/NovelQA option correctness under `_choice_correct`; LongMemEval answer/rubric agreement under question-type criteria; BrowseComp+ semantic answer equivalence. Offline judge parameters are not updated by these functions, exact version is unpinned, endpoint configuration may resolve to another model, provider internals uninspected. Epistemic authority is criterion-relative benchmark correctness only. Operational consumer/channel/force/horizon: file annotators and aggregators consume symbolic labels, enforcing recorded counts/score after each evaluation call, not vetoing already emitted answers or admitting a fact to memory.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed label/diagnostics; CLI writes annotations and score text, prints aggregate counts.
- Later read-back: inapplicable — scored files are report products; no inspected automatic later QA-store or policy consumer of these annotations.
- Delegated visibility: Judge receives question, candidate and supplied reference/rubric, not the full producing document/search/edit trace.
- Selection predicate: Choice heuristic parses answer text; judge annotators select prediction IDs present in references. LongMemEval task/abstention selects rubric; BrowseComp+ requires parseable correct verdict for score denominator.
- Invalidation or expiry: Re-running overwrites designated outputs; no automated answer withdrawal or benchmark-driven rollback in these bodies.
- Activation or effect: Files/aggregates wired; labels do not enforce pre-emission correctness. Optional `DEFER_JUDGE` bypasses model judging and writes a deferred score marker.
- Evidence limits: No executed judgments/results; no calibration, reference validation, model reliability or benchmark superiority established. Missing-reference predictions are skipped, limiting denominator interpretation.

Criteria differ materially. Choice parsing accepts a last standalone A–D match before other permissive fallbacks; a string with several letters can score despite ambiguity. LongMemEval temporal tasks allow off-by-one dates/counts; knowledge-update tolerates older information if the required update is present; preference uses a rubric and abstention checks recognition of unanswerability. Its parser can fall back to the last yes/no/true/false token, and unparseable empty text defaults false with parse_error, counted as false. A JSON verdict key with an uncoercible value can also return default false without parse_error. BrowseComp+ asks semantic equivalence, permits small numeric error and requires extra details to be correct; missing correct verdict sets parse_error and is excluded from the aggregate denominator. These are evidence-consuming decisions for benchmark marking, not scope-independent truth checks. Neither reconstructed reasoning nor matched_span is independently checked against the underlying source.

SRC-1, `infer/src/hf_score_fns.py`, `infer/scripts/eval_task.sh`.

> match = re.search(r"\b[A-D]\b(?!.*\b[A-D]\b)", prediction)
> if match and match.group(0) in label:
>     return True
> --- `infer/src/hf_score_fns.py`

> matches = re.findall(r"\b(yes|no|true|false)\b", text.lower())
> if matches:
>     result["label"] = matches[-1] in {"yes", "true"}
>     return result
> --- `infer/src/hf_score_fns.py`

> counts[reference["question_type"]].append(int(label))
> --- `infer/src/hf_score_fns.py`

> valid = [row["autoeval_judge"] for row in scored_rows if not row["autoeval_judge"]["parse_error"]]
> correct = sum(bool(row["correct"]) for row in valid)
> score = correct / len(valid) if valid else 0.0
> --- `infer/src/hf_score_fns.py`

#### EPI-RTE-answer-reward
Label: Training answer correctness and penalties

Part of: [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit)

This part is terminal evaluation, distinct from branch selection, snapshot disposition and parameter admission. Endpoints: decoded policy solution and dataset reward reference → last-assistant/finish extraction → MC letter or model judgment → outcome plus format score → tool/budget penalty in agent-loop worker → subtree-credit consumer. Owner: scorer and worker. Policy proposes answer, dataset supplies oracle reference, configured external judge decides open-ended correctness, code decides syntax/letter and flags. No per-answer human approval. Operating mode: bounded training QA curriculum. Target/domain: answer agreement with reference and tool-call/trajectory conformance, not truth of each stored memory or validity of the producing explanation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Numeric outcome plus format score; worker may add tool/budget penalty before reward ancestry propagation.
- Later read-back: Scalar rewards feed later training updates via supplied branch-credit/parameter routes; no direct read-back of a judge explanation into the QA context.
- Delegated visibility: Judge receives question/reference/prediction, not full document or action-level causal contrast. Worker receives trajectory flags and prefix ancestry.
- Selection predicate: `finish` with answer extracted from last assistant portion; MC references are a single A–D, accepted prediction exact letter or letter followed by period; otherwise configured external model must return boxed True. Exceptions inside judge retries use normalized equality, while client setup occurs outside that retry try-block.
- Invalidation or expiry: Missing valid finish denies correctness; format violation subtracts 0.5; tool failure or budget exceeded can subtract another 0.5. Missing terminal ancestry can drop snapshots downstream; no fact-level rollback follows.
- Activation or effect: Reward-consumer path to numerical policy adaptation is wired; scorer alone does not accept a theory or prove causal credit for one edit.
- Evidence limits: No executed reward/gradient trace. External judge/reference correctness unvalidated; broader exception paths may fail rather than yield a fallback score. Comparison of whole continuations does not isolate a component mechanism.

Epistemic license: in MC mode a deterministic decision under encoded letter criterion; in open mode a model decision under reference-answer comparison, not warranted source entailment. Check success has ranking/update force through rewards/advantages, while downstream admission checks terminal ancestry and finite gradients rather than epistemic truth. Actor weight authority and checkpoint horizon are owned by [RT-RTE-policy-update](runtime.md#rt-rte-policy-update) and [RT-BAP-rollout-weights](runtime.md#rt-bap-rollout-weights). These preserve the independent parameter-learning conclusion; a numerical policy change is not a newly accepted truth-apt claim.

SRC-1, `train/verl/utils/reward_score/statelm_qa.py`, `train/verl/experimental/agent_loop/agent_loop.py`.

> (predicted.strip() == ground_truth) or (predicted.strip().startswith(f"{ground_truth}."))
> --- `train/verl/utils/reward_score/statelm_qa.py`

> is_correct = has_valid_finish_tool_call and llm_judge_answer(predicted, ground_truth, question)
> --- `train/verl/utils/reward_score/statelm_qa.py`

> r_out = 1.0 if is_correct else 0.0
> r_fmt = -0.5 if had_format_violation else 0.0
> score = r_out + r_fmt
> --- `train/verl/utils/reward_score/statelm_qa.py`

> had_failure = self._as_bool(output.extra_fields.get("had_tool_failure", False))
> exceeded_budget = self._as_bool(output.extra_fields.get("context_len_or_turn_exceeded", False))
> if had_failure or exceeded_budget:
>     r_pen = -0.5
>     result["reward_score"] = float(result["reward_score"]) + r_pen
> --- `train/verl/experimental/agent_loop/agent_loop.py`

### Claims

#### EPI-CLM-grounded-answer
Label: Evidence-sufficient grounded answer

Claimed operation: continue evidence search/reading/saving/review until sufficient, then submit a concise document-grounded answer. This is shipped desired behavior, not an assertion of infallible QA. Closest supplied [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating) concerns protocol, not semantic sufficiency, so identities differ. SRC-1, `infer/configs/fsm_plan_bm25_mc_prompt.txt`, doctrine/design. Implemented review tests successful reader return, not evidence entailment; this qualification does not require superseding the valid runtime protocol account.

> 8. Continue searching, reading, memorizing, cleaning, and reviewing until the evidence is sufficient; then call `finish` with a concise answer grounded in the document.
> --- `infer/configs/fsm_plan_bm25_mc_prompt.txt`

> elif old == FSMState.S6_REQUIRE_READ_NOTE:
>     if tool_name == "readNote" and "error" not in result:
>         self._note_review_satisfied = True
> --- `infer/src/contextpilot_fsm.py`

#### EPI-CLM-branch-credit
Label: Downstream-outcome snapshot credit

Claimed operation: exploration focuses on sensitive context decisions, training intermediate snapshots using descendant outcomes. Doctrine/design, SRC-1, `README.md`. Distinct from [RT-CLM-fsm-gating](runtime.md#rt-clm-fsm-gating); closest operational counterpart [RT-RTE-branch-credit](runtime.md#rt-rte-branch-credit) is a route, not this public claim. Implemented sensitivity selection/ancestry means support the stated computation; they do not establish action-specific causal explanation or observed benefit.

> Its context-aware partial rollout focuses exploration
> on sensitive context-editing decisions, while fine-grained credit assignment
> trains intermediate snapshots using the outcomes of their downstream
> branches.
> --- `README.md`

#### EPI-CLM-performance-gains
Label: Better QA with compact context

Claimed operation/outcome: stronger long-context QA/deep-search performance with a more compact working context, surpassing baselines across models/benchmarks. SRC-1, `README.md`, reported operation. No counterpart after comparison with runtime's protocol claim; training implementation is not experimental evidence for this outcome. No frozen observed runs or controlled comparisons are registered; gains and attribution remain unverified.

> Experiments on long-context QA and deep search tasks show that ContextPilot
> achieves stronger performance with a more compact working context,
> outperforming existing baselines across various base models and benchmarks.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
