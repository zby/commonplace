---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Agno epistemic routes: tool acquisition, answer rewriting, scoped evaluators, soft learning admission and scored training-data export."
run-id: AAS-2026-10-13-agno-60e6e09dd4a6-01
reviewed-boundary: "00497422d4a386d93ab3b45c1a11faf42fcc932f"
---

# Agno epistemic report

## Source-and-claim boundary

Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Source identity, frozen revision and evidence layers: see [Source register](boundary.md#source-register). The question is how the SDK/AgentOS subsystem acquires truth-apt content, evaluates it, grants reliance and lets it affect later behavior. This is not a whole-product or whole-repository epistemic audit. The terminal operations package, infrastructure and hosted UI remain excluded; external service/model internals are not inspected.

All new findings use SRC-1 at the frozen revision: implementation source text, and explicitly marked doctrine/design. Supplied runtime findings order the investigation but do not limit it. No target execution, model call, tests, trace or experiment was performed or supplied. Consequently no candidate's actual truth, activated recall, successful approval, model weight change, empirical improvement or causal process attribution is established. A source-native knowledge label is not a warrant certificate.

Coverage distinguishes direct source inspection from supplied records. Available uninspected operations prevent a system-complete negative about checking, accepted knowledge, autonomous learning or self-improvement.

| Entry point or operation | Source path | Coverage and records, or remaining limit |
|---|---|---|
| Agent run, Team delegation, Workflow Step | `libs/agno/agno/agent/_run.py`; `libs/agno/agno/team/_default_tools.py`; `libs/agno/agno/workflow/step.py` | Supplied runtime records for whole route; direct read of returning Agent post-hooks/error cleanup. See [RT-RTE-agent-run](runtime.md#rt-rte-agent-run), [RT-RTE-team-delegation](runtime.md#rt-rte-team-delegation), [RT-RTE-workflow-step](runtime.md#rt-rte-workflow-step). Complete async/stream/graph scheduling not audited. |
| SDK interactive CLI | `libs/agno/agno/agent/_cli.py` | Direct read: cli_app forwards initial/user messages to agent_print_response; exit words stop input loop. Same configured Agent path, not the excluded agnoctl operations CLI. No independent factual check shown in this wrapper; print utility internals uninspected. |
| Registered financial tool | `libs/agno/agno/tools/yfinance.py` | Direct read current-price entrypoint and registration search; [EPI-RTE-finance-import](#epi-rte-finance-import). Other financial/data tool integrations not exhaustively traced. |
| Output/parser stages | `libs/agno/agno/agent/_response.py`; `libs/agno/agno/agent/_messages.py`; `libs/agno/agno/agent/_run.py` | Direct read synchronous stage inputs, ordered substitutions and RunOutput update; [EPI-RTE-output-generation](#epi-rte-output-generation), [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting), within [EPI-RTE-output-replacement](#epi-rte-output-replacement). Reasoning, follow-up model and complete structured conversion paths unassessed, preventing complete generation/derivation account. |
| Pre/post hooks and guardrails | `libs/agno/agno/agent/_hooks.py`; `libs/agno/agno/guardrails/pii.py` | Direct post-hook and PII reads; [EPI-RTE-pii-input](#epi-rte-pii-input), [EPI-RTE-output-hooks](#epi-rte-output-hooks). Prompt-injection/moderation guardrails and arbitrary custom evaluators unassessed; prevents universal safety/factual gate verdict. |
| Accuracy, criteria judge, tool reliability | `libs/agno/agno/eval/accuracy.py`; `libs/agno/agno/eval/agent_as_judge.py`; `libs/agno/agno/eval/reliability.py` | Direct evaluator/consequence reads; corresponding EPI routes. Full eval-suite dispatch, performance checks, logs/reloads unassessed; no full evaluation inventory or reliability measurement. |
| Learned knowledge extract/save/search/delete | `libs/agno/agno/learn/stores/learned_knowledge.py`; `libs/agno/agno/agent/_messages.py` | Direct read selected synchronous methods and prompt/context wiring; EPI learning routes. Other learning stores, memory manager and complete LearningMachine mode orchestration unassessed here, preventing universal learning/criticism/admission verdict. |
| Generic knowledge search/write tools | `libs/agno/agno/agent/_default_tools.py` | Direct simple search/write wrappers; [EPI-RTE-learning-save](#epi-rte-learning-save). Readers, chunking, embeddings, reranking, namespace adapters and backend validation not traced; full ingestion lineage/warrant unknown. |
| Profile curator | `libs/agno/agno/learn/curate.py` | Full direct file read; [EPI-RTE-profile-curation](#epi-rte-profile-curation). User-profile schema/reload/render and material applicability unassessed. |
| Environment score and SFT export | `libs/agno/agno/environments/_engine.py`; `libs/agno/agno/scorer/judge.py`; `libs/agno/agno/environments/exporters/sft.py` | Direct scoring seam, JudgeScorer conversion, full exporter; [EPI-RTE-sft-selection](#epi-rte-sft-selection). CodeScorer/ToolCallScorer, runner clone/fingerprints and exporters/_validate only searched or uninspected; no complete training or experiment claim. |
| History filtering, compaction | `libs/agno/agno/agent/_messages.py`; `libs/agno/agno/compaction/compaction.py` | Supplied [RT-RTE-context-window](runtime.md#rt-rte-context-window); compression manager/model seams searched, not assessed end-to-end. Offload/read-back, archive tools, skills/context providers and full summary-memory lifecycle unassessed; prevents semantic-fidelity or complete lineage conclusions. |
| AgentOS HTTP, queue, config, local confirmation | `libs/agno/agno/os/routers/agents/router.py`; `libs/agno/agno/os/job_queue.py`; `libs/agno/agno/os/routers/components/components.py`; `libs/agno/agno/agent/_tools.py` | Supplied [RT-RTE-queue-dispatch](runtime.md#rt-rte-queue-dispatch), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission), [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation). Approval-service expiry, schedulers, interfaces/remote dispatch and additional published operation handlers unassessed; no universal withdrawal/rollback claim. |

Consequential source claims: see [RT-CLM-market-brief](runtime.md#rt-clm-market-brief), [EPI-CLM-learning-loop](#epi-clm-learning-loop), and [EPI-CLM-propose-approval](#epi-clm-propose-approval). No supplied fact requires supersession. The valid output-replacement container is retained with separately declared output-generation and parser-rewriting parts. Manual LearningMachine.capture as a post-hook remains unassessed here, preventing a complete automatic-versus-manual capture timing comparison. The shipped export loader at `cookbook/environments/_12_trainer_loader/basic.py` remains uninspected here, preventing a complete downstream dataset-consumer inventory; export alone establishes no training-loop closure. Specialist refinements below concern material parts and evaluator consumers the provisional runtime explicitly left open.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-price-result](#epi-obj-price-result) | Provider-reported price for requested symbol, or error text. | see [EPI-OBJ-price-result](#epi-obj-price-result) | SRC-1, `libs/agno/agno/tools/yfinance.py` | see [EPI-OBJ-price-result](#epi-obj-price-result) |
| [EPI-OBJ-model-response](#epi-obj-model-response) | Task-dependent factual assertions, if present; no actual candidate supplied. | see [EPI-OBJ-model-response](#epi-obj-model-response) | SRC-1, `libs/agno/agno/agent/_response.py` | see [EPI-OBJ-model-response](#epi-obj-model-response) |
| [EPI-OBJ-output-content](#epi-obj-output-content) | Task-dependent assertions, if present; no actual candidate. | see [EPI-OBJ-output-content](#epi-obj-output-content) | SRC-1, `libs/agno/agno/agent/_response.py` | see [EPI-OBJ-output-content](#epi-obj-output-content) |
| [EPI-OBJ-parser-content](#epi-obj-parser-content) | Task-dependent structured assertions, if present; no actual candidate. | see [EPI-OBJ-parser-content](#epi-obj-parser-content) | SRC-1, `libs/agno/agno/agent/_response.py` | see [EPI-OBJ-parser-content](#epi-obj-parser-content) |
| [EPI-OBJ-learning](#epi-obj-learning) | Insights may be truth-apt; organizational goals/policies are non-truth-apt guidance. | see [EPI-OBJ-learning](#epi-obj-learning) | SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py` | see [EPI-OBJ-learning](#epi-obj-learning) |
| [EPI-OBJ-profile-memories](#epi-obj-profile-memories) | Possibly truth-apt user assertions; actual instance not supplied. | see [EPI-OBJ-profile-memories](#epi-obj-profile-memories) | SRC-1, `libs/agno/agno/learn/curate.py` | see [EPI-OBJ-profile-memories](#epi-obj-profile-memories) |
| [EPI-OBJ-judge-evaluation](#epi-obj-judge-evaluation) | Claim that an answer meets caller criteria; criteria need not concern truth. | see [EPI-OBJ-judge-evaluation](#epi-obj-judge-evaluation) | SRC-1, `libs/agno/agno/eval/agent_as_judge.py` | see [EPI-OBJ-judge-evaluation](#epi-obj-judge-evaluation) |
| [EPI-OBJ-accuracy-evaluation](#epi-obj-accuracy-evaluation) | Assessment of closeness/completeness relative to reference. | see [EPI-OBJ-accuracy-evaluation](#epi-obj-accuracy-evaluation) | SRC-1, `libs/agno/agno/eval/accuracy.py` | see [EPI-OBJ-accuracy-evaluation](#epi-obj-accuracy-evaluation) |
| [EPI-OBJ-reliability-result](#epi-obj-reliability-result) | Whether recorded tool executions meet configured name/argument expectations. | see [EPI-OBJ-reliability-result](#epi-obj-reliability-result) | SRC-1, `libs/agno/agno/eval/reliability.py` | see [EPI-OBJ-reliability-result](#epi-obj-reliability-result) |
| [EPI-OBJ-sft-conversations](#epi-obj-sft-conversations) | Assistant assertions preserved from selected text-only attempts. | see [EPI-OBJ-sft-conversations](#epi-obj-sft-conversations) | SRC-1, `libs/agno/agno/environments/exporters/sft.py` | see [EPI-OBJ-sft-conversations](#epi-obj-sft-conversations) |
| [EPI-OBJ-run-input](#epi-obj-run-input) | Input may contain factual assertions; masked strings remove information. | see [EPI-OBJ-run-input](#epi-obj-run-input) | SRC-1, `libs/agno/agno/guardrails/pii.py` | see [EPI-OBJ-run-input](#epi-obj-run-input) |

Provider models, tool capabilities, execution identities and published configurations retain their supplied identities: see [RT-CMP-gemini](runtime.md#rt-cmp-gemini), [RT-CMP-fallback-model](runtime.md#rt-cmp-fallback-model), [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model), [RT-OBJ-function](runtime.md#rt-obj-function), [RT-OBJ-run-context](runtime.md#rt-obj-run-context), and [RT-OBJ-component-config](runtime.md#rt-obj-component-config). No source establishes a served immutable model version or online weight update. Extra inference roles used here have the separate component record below.

## Authority-route ledger

Route ID: [EPI-RTE-finance-import](#epi-rte-finance-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-price-result](#epi-obj-price-result)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Evaluator/condition and domain: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Activation and timing: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Possible or observed result: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Implemented force: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Epistemic authority and scope: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-finance-import](#epi-rte-finance-import)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/tools/yfinance.py`; see [EPI-RTE-finance-import](#epi-rte-finance-import)
Claim IDs or none: [RT-CLM-market-brief](runtime.md#rt-clm-market-brief)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-finance-import](#epi-rte-finance-import)

Route ID: [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-model-response](#epi-obj-model-response)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Evaluator/condition and domain: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Activation and timing: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Possible or observed result: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Implemented force: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Epistemic authority and scope: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/agent/_response.py`; see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)

Route ID: [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-model-response](#epi-obj-model-response)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Evaluator/condition and domain: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Activation and timing: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Possible or observed result: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Implemented force: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Epistemic authority and scope: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/agent/_response.py`; see [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-output-replacement](#epi-rte-output-replacement)

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-output-generation](#epi-rte-output-generation) | content transformation | implemented | [EPI-OBJ-output-content](#epi-obj-output-content) | truth-apt transformation: indeterminate | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | SRC-1, `libs/agno/agno/agent/_response.py` | none | none | see [EPI-RTE-output-generation](#epi-rte-output-generation) |
| [EPI-RTE-output-generation](#epi-rte-output-generation) | operational admission/selection/consumption | implemented | [EPI-OBJ-output-content](#epi-obj-output-content) | no content change | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | see [EPI-RTE-output-generation](#epi-rte-output-generation) | SRC-1, `libs/agno/agno/agent/_response.py` | none | none | see [EPI-RTE-output-generation](#epi-rte-output-generation) |
| [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | content transformation | implemented | [EPI-OBJ-parser-content](#epi-obj-parser-content) | truth-apt transformation: indeterminate | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | SRC-1, `libs/agno/agno/agent/_response.py` | none | none | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) |
| [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | operational admission/selection/consumption | implemented | [EPI-OBJ-parser-content](#epi-obj-parser-content) | no content change | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) | SRC-1, `libs/agno/agno/agent/_response.py` | none | none | see [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting) |

Route ID: [EPI-RTE-pii-input](#epi-rte-pii-input)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-input](#epi-obj-run-input)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Evaluator/condition and domain: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Activation and timing: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Possible or observed result: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Implemented force: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Epistemic authority and scope: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/guardrails/pii.py`; see [EPI-RTE-pii-input](#epi-rte-pii-input)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-pii-input](#epi-rte-pii-input)

Route ID: [EPI-RTE-pii-input](#epi-rte-pii-input)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-input](#epi-obj-run-input)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Evaluator/condition and domain: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Activation and timing: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Possible or observed result: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Implemented force: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Epistemic authority and scope: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/guardrails/pii.py`; see [EPI-RTE-pii-input](#epi-rte-pii-input)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-pii-input](#epi-rte-pii-input)

Route ID: [EPI-RTE-pii-input](#epi-rte-pii-input)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-run-input](#epi-obj-run-input)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Evaluator/condition and domain: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Activation and timing: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Possible or observed result: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Implemented force: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Epistemic authority and scope: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-pii-input](#epi-rte-pii-input)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/guardrails/pii.py`; see [EPI-RTE-pii-input](#epi-rte-pii-input)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-pii-input](#epi-rte-pii-input)

Route ID: [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-model-response](#epi-obj-model-response)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Evaluator/condition and domain: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Activation and timing: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Possible or observed result: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Implemented force: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Epistemic authority and scope: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/agent/_hooks.py`; see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)

Route ID: [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-model-response](#epi-obj-model-response)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Evaluator/condition and domain: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Activation and timing: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Possible or observed result: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Implemented force: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Epistemic authority and scope: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/agent/_hooks.py`; see [EPI-RTE-output-hooks](#epi-rte-output-hooks)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-output-hooks](#epi-rte-output-hooks)

Route ID: [EPI-RTE-judge-check](#epi-rte-judge-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judge-evaluation](#epi-obj-judge-evaluation)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Evaluator/condition and domain: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Activation and timing: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Possible or observed result: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Implemented force: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Epistemic authority and scope: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/eval/agent_as_judge.py`; see [EPI-RTE-judge-check](#epi-rte-judge-check)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-judge-check](#epi-rte-judge-check)

Route ID: [EPI-RTE-judge-check](#epi-rte-judge-check)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judge-evaluation](#epi-obj-judge-evaluation)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Evaluator/condition and domain: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Activation and timing: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Possible or observed result: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Implemented force: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Epistemic authority and scope: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/eval/agent_as_judge.py`; see [EPI-RTE-judge-check](#epi-rte-judge-check)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-judge-check](#epi-rte-judge-check)

Route ID: [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-accuracy-evaluation](#epi-obj-accuracy-evaluation)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Evaluator/condition and domain: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Activation and timing: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Possible or observed result: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Implemented force: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Epistemic authority and scope: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/eval/accuracy.py`; see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-accuracy-check](#epi-rte-accuracy-check)

Route ID: [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-reliability-result](#epi-obj-reliability-result)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Evaluator/condition and domain: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Activation and timing: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Possible or observed result: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Implemented force: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Epistemic authority and scope: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/eval/reliability.py`; see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)

Route ID: [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-reliability-result](#epi-obj-reliability-result)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Evaluator/condition and domain: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Activation and timing: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Possible or observed result: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Implemented force: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Epistemic authority and scope: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/eval/reliability.py`; see [EPI-RTE-reliability-check](#epi-rte-reliability-check)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-reliability-check](#epi-rte-reliability-check)

Route ID: [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learning](#epi-obj-learning)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Evaluator/condition and domain: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Activation and timing: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Possible or observed result: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Implemented force: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Epistemic authority and scope: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py`; see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-learning-extraction](#epi-rte-learning-extraction)

Route ID: [EPI-RTE-learning-save](#epi-rte-learning-save)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learning](#epi-obj-learning)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Evaluator/condition and domain: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Activation and timing: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Possible or observed result: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Implemented force: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Epistemic authority and scope: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py`; see [EPI-RTE-learning-save](#epi-rte-learning-save)
Claim IDs or none: none
Mismatch marker or none: PROPOSE approval request is not a writer-level enforcing gate
Gap/limit: see [EPI-RTE-learning-save](#epi-rte-learning-save)

Route ID: [EPI-RTE-learning-save](#epi-rte-learning-save)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learning](#epi-obj-learning)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Evaluator/condition and domain: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Activation and timing: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Possible or observed result: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Implemented force: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Epistemic authority and scope: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-learning-save](#epi-rte-learning-save)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py`; see [EPI-RTE-learning-save](#epi-rte-learning-save)
Claim IDs or none: none
Mismatch marker or none: PROPOSE approval request is not a writer-level enforcing gate
Gap/limit: see [EPI-RTE-learning-save](#epi-rte-learning-save)

Route ID: [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learning](#epi-obj-learning)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Evaluator/condition and domain: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Activation and timing: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Possible or observed result: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Implemented force: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Epistemic authority and scope: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py`; see [EPI-RTE-learning-recall](#epi-rte-learning-recall)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-learning-recall](#epi-rte-learning-recall)

Route ID: [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-profile-memories](#epi-obj-profile-memories)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Evaluator/condition and domain: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Activation and timing: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Possible or observed result: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Implemented force: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Epistemic authority and scope: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/learn/curate.py`; see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)

Route ID: [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-profile-memories](#epi-obj-profile-memories)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Evaluator/condition and domain: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Activation and timing: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Possible or observed result: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Implemented force: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Epistemic authority and scope: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/learn/curate.py`; see [EPI-RTE-profile-curation](#epi-rte-profile-curation)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-profile-curation](#epi-rte-profile-curation)

Route ID: [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sft-conversations](#epi-obj-sft-conversations)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Evaluator/condition and domain: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Activation and timing: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Possible or observed result: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Implemented force: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Epistemic authority and scope: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/environments/exporters/sft.py`; see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Claim IDs or none: [EPI-CLM-learning-loop](#epi-clm-learning-loop)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)

Route ID: [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-sft-conversations](#epi-obj-sft-conversations)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Evaluator/condition and domain: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Activation and timing: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Possible or observed result: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Implemented force: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Epistemic authority and scope: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Evidence source ID and local anchor: SRC-1, `libs/agno/agno/environments/exporters/sft.py`; see [EPI-RTE-sft-selection](#epi-rte-sft-selection)
Claim IDs or none: [EPI-CLM-learning-loop](#epi-clm-learning-loop)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-sft-selection](#epi-rte-sft-selection)

Route ID: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-run-context](runtime.md#rt-obj-run-context)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Evaluator/condition and domain: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Activation and timing: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Possible or observed result: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Implemented force: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Epistemic authority and scope: Generic generation has no supplied concrete factual candidate; no inference of conjecture merely from failure to prove entailment.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Evidence source ID and local anchor: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)

Route ID: [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-run-context](runtime.md#rt-obj-run-context)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Evaluator/condition and domain: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Activation and timing: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Possible or observed result: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Implemented force: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Epistemic authority and scope: Model summary is not proven truth-preserving; original history/archive reachability differs from delivery.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Evidence source ID and local anchor: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [RT-RTE-context-window](runtime.md#rt-rte-context-window)

Route ID: [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [RT-OBJ-function](runtime.md#rt-obj-function)
Content/update relation: no content change
Transition or check target: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Evaluator/condition and domain: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Activation and timing: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Possible or observed result: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Implemented force: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Epistemic authority and scope: Approval permits an effect, not a factual assertion; alternate effect paths remain.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Evidence source ID and local anchor: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation)

Route ID: [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-component-config](runtime.md#rt-obj-component-config)
Content/update relation: non-truth-apt policy/content update: caller-supplied runtime configuration
Transition or check target: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Evaluator/condition and domain: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Activation and timing: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Possible or observed result: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Implemented force: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Epistemic authority and scope: Published/current constraints are operational admission, not an evidence-fed truth criterion or universal human review.
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Evidence source ID and local anchor: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [RT-RTE-config-admission](runtime.md#rt-rte-config-admission)

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-market-brief](runtime.md#rt-clm-market-brief) | see record | see record | see record | [RT-RTE-agent-run](runtime.md#rt-rte-agent-run), [EPI-RTE-finance-import](#epi-rte-finance-import) | None supplied | Provider/source truth and final brief accuracy untested | Tool-backed brief generation wired, not verified finance truth | Live/current wording has no independent timestamp or final-answer oracle here |
| [EPI-CLM-learning-loop](#epi-clm-learning-loop) | see record | see record | see record | [EPI-RTE-learning-extraction](#epi-rte-learning-extraction), [EPI-RTE-learning-save](#epi-rte-learning-save), [EPI-RTE-learning-recall](#epi-rte-learning-recall), [EPI-RTE-sft-selection](#epi-rte-sft-selection), [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) | None supplied | Retained guidance and selected datasets do not demonstrate better capacity or a causally effective deployed revision | Several building blocks for a caller-operated learning loop exist | Simulations/training/integration and improvement not demonstrated; not a claim that no other pathway exists |
| [EPI-CLM-propose-approval](#epi-clm-propose-approval) | see record | see record | see record | [EPI-RTE-learning-save](#epi-rte-learning-save) | None supplied | Mode prompt asks approval; underlying save method/tool accepts no approval artifact | Instruction-level proposal/approval policy, not enforcing writer gate | Distinct from local Function confirmation protocol |

## Bounded conclusion

Agno imports external tool data and returns or retains model-produced content. The inspected price wrapper selects and formats a provider datum; it does not verify source truth. Generic knowledge and learned-knowledge tools retain caller/model text and later deliver selected results through tool strings or system instructions. Selection, storage and fluent rewriting do not supply missing warrant. See [EPI-RTE-finance-import](#epi-rte-finance-import), [EPI-RTE-learning-save](#epi-rte-learning-save), [EPI-RTE-learning-recall](#epi-rte-learning-recall).

Checks are heterogeneous. Criteria judges offer model opinion plus threshold/binary pass; an on_fail callback can give that opinion caller-defined operational consequences, but the judge post-hook does not automatically reject failed output. AccuracyEval compares against an assumed-correct reference. ReliabilityEval deterministically tests provided execution evidence against tool-name/argument expectations, with an optional assertion gate; its license is evidence-relative and does not extend to final-answer truth or service effects. Regex PII checks enforce input masking/rejection within lexical domains. None is a universal answer oracle. See [EPI-RTE-judge-check](#epi-rte-judge-check), [EPI-RTE-accuracy-check](#epi-rte-accuracy-check), [EPI-RTE-reliability-check](#epi-rte-reliability-check), [EPI-RTE-pii-input](#epi-rte-pii-input).

Rejection and withdrawal are different. Check exceptions can mark an Agent run error and still preserve generated content in cleanup/storage. Local confirmation prevents a marked Function effect before execution; it is not evidence of factual acceptance or rollback of prior effects. Learning deletion changes later available content subject to backend support; Curator changes survivors by age/count/normalized-string collision, not factual criticism. The concrete normalization counterexamples prevent calling its deduplication a warranted semantic equivalence transformation. See [EPI-RTE-output-hooks](#epi-rte-output-hooks), [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation), [EPI-RTE-learning-save](#epi-rte-learning-save), [EPI-RTE-profile-curation](#epi-rte-profile-curation).

Learning extraction requests reusable generalizations and organizational policies. The former are unverified candidates without a supplied instance showing entailment or non-entailment; the latter may directly shape policy without being truth-apt. PROPOSE requests user approval in text, while the shared writer has no approval-token check. Recall provides a live advisory channel for retained guidance, but no observed consumer dependence or improved capacity. This supports a retained-guidance capacity, not an exercised or beneficial self-improvement claim. No accepted ampliative claim or post-acceptance lifecycle integration is established in these inspected routes. This is a bounded finding, not an absence across unassessed stores or arbitrary user hooks. See [EPI-RTE-learning-extraction](#epi-rte-learning-extraction), [EPI-RTE-learning-save](#epi-rte-learning-save), [EPI-RTE-learning-recall](#epi-rte-learning-recall).

Scored rollout export is a consequential evaluator consumer: default pass-only and trace/schema filters admit text-only examples for conversational SFT, with provenance sidecar and explicit counters. Its material criterion is selected scorer pass plus exportability, intended use a dataset, and scope the retained completed scored attempts. Caller can export failed scored attempts by disabling only_passed. This is operational dataset acceptance, not independent factual warrant, training success, parameter update or live-policy installation. See [EPI-RTE-sft-selection](#epi-rte-sft-selection). It is a counterexample to treating all evaluations as inert reports.

Optional output generation consumes the run-message list after its last entry is popped and any configured system prompt is substituted. Parser rewriting instead consumes the resulting content under its own schema-oriented prompt and may replace content/parsed while appending its assistant message. Output substitution precedes parser substitution: neither has unconditional independent finality, and RunOutput content selection distinguishes parsed output from text. Persisted payloads and filtered messages are different replay surfaces; later history selection remains unresolved. See [EPI-RTE-output-generation](#epi-rte-output-generation), [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting). These stages and supplied compaction have operational replacement force but unestablished semantic fidelity. No warranted novel derivation or actual conjecture can be identified without inputs/outputs and premise warrant. Parameters, exact served versions and mutable provider endpoints remain separately unresolved; inference/deepcopy is not training. Missing execution and comparison evidence also prevents activated learning, causal benefit or fine-grained mechanism attribution. Reflection, autonomy, theory-building and self-improvement are not bundled into a system-wide negative: they require independent evidence, and relevant stores/callers remain unassessed. See [EPI-RTE-output-replacement](#epi-rte-output-replacement), [RT-RTE-context-window](runtime.md#rt-rte-context-window), [EPI-CMP-auxiliary-models](#epi-cmp-auxiliary-models).

## Shared records

### Components

#### EPI-CMP-auxiliary-models
Label: Auxiliary inference roles

Source-native identities: Agent.output_model and Agent.parser_model; LearnedKnowledgeStore.model copied for extraction; AgentAsJudgeEval configured evaluator/model (default OpenAIChat gpt-5-mini); AccuracyEval default OpenAIChat o4-mini or supplied evaluator; JudgeScorer explicit Model. Each role consumes separately prepared content and has a distinct authority described by its route. Representational form: distributed-parametric provider inference, separate from symbolic configuration and natural-language criteria. Storage substrate: provider-managed weights, not local persisted learnings or Score objects. Parameters changing during operation: uninspected provider internals; inspected calls perform response inference and extraction deepcopy, not a weight update. Exact version pinned: no immutable weight/version digest for any of these roles. Mutable endpoint resolving to another model: provider alias behavior unresolved for each; caller can substitute configured models. None was observed to run.

Distinct identity from [RT-CMP-gemini](runtime.md#rt-cmp-gemini), [RT-CMP-fallback-model](runtime.md#rt-cmp-fallback-model), [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model): these are separately configured inference consumers, not a second declaration of those supplied model roles. A caller may intentionally reuse one Model; physical equality is configuration-dependent, not established by role names.

SRC-1, `libs/agno/agno/agent/_response.py`, `libs/agno/agno/learn/stores/learned_knowledge.py`, `libs/agno/agno/eval/agent_as_judge.py`, `libs/agno/agno/eval/accuracy.py`, `libs/agno/agno/scorer/judge.py` (implementation); see route passages for actual calls.

### Operative objects

#### EPI-OBJ-price-result
Label: Current stock price result

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
This is the finance Function's tool-result payload within that route, not a final model answer. Its source is provider data rather than model generation; it has a separate producer and consumer stage from [EPI-OBJ-model-response](#epi-obj-model-response).

Source-native identity: get_current_stock_price result, a four-decimal string for a requested symbol or fetch/error text. Representational form: textual numerical datum or natural-language error, interpreted by the foreground model; request symbol/tool name are symbolic selectors. Storage substrate: current tool-result string and enclosing run messages, with persistence only under enclosing run configuration. Evidence: SRC-1, `libs/agno/agno/tools/yfinance.py` (implementation); see [EPI-RTE-finance-import](#epi-rte-finance-import) for minimum passage. Source price truth and timestamp remain unknown; the returned scalar alone supplies neither an evidence certificate nor final-answer validation.

#### EPI-OBJ-model-response
Label: ModelResponse content

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
This is the answer payload within that route, not another declaration of the whole execution route. The parent is a route rather than an object because no supplied answer object is declared.

Source-native identity: The content and parsed fields replaced by output/parser model stages of Agent execution.
Representational form: Natural-language answer content; parsed Pydantic output has symbolic shape, but its factual fields still require interpretation.
Storage substrate: Current-run ModelResponse/RunOutput and configured run storage.
Evidence: SRC-1, `libs/agno/agno/agent/_response.py` (implementation). No run supplies propositions to individuate, entailment or factual correctness.

#### EPI-OBJ-output-content
Label: Output-model content

Part of: [EPI-OBJ-model-response](#epi-obj-model-response)
Source-native identity: output_model_response.content copied into ModelResponse.content. Representational form: task-dependent natural-language text; truth-apt assertions cannot be individuated without a candidate. Storage substrate: current ModelResponse and conditional later RunOutput storage. Producer is output_model; consumers are parser preparation and downstream RunOutput update, not necessarily final return unchanged. Distinct from parser content by producer, input lineage and overwritten fields. SRC-1, `libs/agno/agno/agent/_response.py` (implementation); minimum passages in [EPI-RTE-output-generation](#epi-rte-output-generation).

#### EPI-OBJ-parser-content
Label: Parser-model content and parsed output

Part of: [EPI-OBJ-model-response](#epi-obj-model-response)
Source-native identity: parser_model_response.content and parsed, plus appended parser assistant message. Representational form: natural-language content and symbolic structured shape; factual fields still need interpretation. Storage substrate: ModelResponse, run_messages and conditional RunOutput persistence. Distinct from output content by separate schema-oriented inference, assistant-message admission and parsed-field substitution. No actual instance supplies truth or fidelity evidence. SRC-1, `libs/agno/agno/agent/_response.py` (implementation); minimum passages in [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting).

#### EPI-OBJ-learning
Label: LearnedKnowledgeStore learning

No counterpart after comparison with supplied RunContext and component config: this is stored knowledge content, not execution identities or configuration.

Source-native identity: Learning schema with title, learning, context, tags, namespace, creator metadata and created_at.
Representational form: Natural-language insight, directives and scope; symbolic metadata and namespace selectors.
Storage substrate: Knowledge insertion plus configured vector/content backends.
Evidence: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py` (implementation). No retained instance or evidence links demonstrate a true generalization. Embedding provenance and backend fidelity are uninspected.

#### EPI-OBJ-profile-memories
Label: User profile memories

No counterpart after comparison with supplied runtime objects; this is a distinct retained profile part, not component configuration.

Source-native identity: The profile.memories list operated on by Curator, with content and optional created_at.
Representational form: Natural-language content plus symbolic dictionaries/timestamps.
Storage substrate: Loaded profile and store.save persistence.
Evidence: SRC-1, `libs/agno/agno/learn/curate.py` (implementation). Curator supports only this store and only profiles exposing memories; actual schema/configuration applicability is unobserved.

#### EPI-OBJ-judge-evaluation
Label: AgentAsJudgeEvaluation

No counterpart after comparison with supplied runtime records: these are criteria judgments, not run completion states.

Source-native identity: Criteria, input/output, numeric score or binary passed, and reason.
Representational form: Natural-language criteria/reason and assessed answer; symbolic score/pass fields.
Storage substrate: Current result and optional evaluation DB/file output.
Evidence: SRC-1, `libs/agno/agno/eval/agent_as_judge.py` (implementation). No observed calibration or independent evidence about judge accuracy.

#### EPI-OBJ-accuracy-evaluation
Label: AccuracyEvaluation

Distinct from supplied runtime records and from criteria-only judgment: a supplied reference is assumed correct.

Source-native identity: Expected_output, output, score and reason returned by evaluate_answer.
Representational form: Natural-language reference/answer/reason; symbolic score.
Storage substrate: Evaluation result and optional configured logs.
Evidence: SRC-1, `libs/agno/agno/eval/accuracy.py` (implementation). Reference truth is not checked by the default evaluator.

#### EPI-OBJ-reliability-result
Label: ReliabilityResult

No counterpart after comparison with supplied runtime records: tool-dispatch capability and actual execution-evidence judgment are different referents.

Source-native identity: PASSED/FAILED plus missing, failed, passed and additional tool calls and argument checks.
Representational form: Symbolic execution-evidence comparison; strings identify failures.
Storage substrate: Current result; callers can log or assert it.
Evidence: SRC-1, `libs/agno/agno/eval/reliability.py` (implementation). Recorded clean status is not independent evidence of external side-effect success or final-answer truth.

#### EPI-OBJ-sft-conversations
Label: Conversational-SFT JSONL

Distinct from supplied context-window storage: a selected external training artifact, not foreground history.

Source-native identity: Exported role/content conversations and provenance meta.json.
Representational form: Natural-language messages with symbolic roles and provenance indices/scores.
Storage substrate: Caller-selected JSONL file and sidecar.
Evidence: SRC-1, `libs/agno/agno/environments/exporters/sft.py` (implementation). No trainer, actual training, updated weights or improved behavior is established by export.

#### EPI-OBJ-run-input
Label: PII-checked RunInput

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
This is its material input payload, not another complete execution route.

Source-native identity: RunInput.input_content changed by PIIDetectionGuardrail.
Representational form: Natural-language input converted to text; symbolic regex matching and error flags.
Storage substrate: Current-run input; retention policy follows enclosing run configuration.
Evidence: SRC-1, `libs/agno/agno/guardrails/pii.py` (implementation). PII-pattern matches do not establish that text actually identifies a person.

### Routes

#### EPI-RTE-finance-import
Label: Yahoo price acquisition

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
This is one granted local Function implementation, not the entire model/tool loop.

Caller grants YFinanceTools; model selects symbol and call; host entrypoint imports yf.Ticker.info, chooses regularMarketPrice with currentPrice fallback and formats four decimals. Tool response enters the ordinary tool-result channel. In source terms this is live-data acquisition, not production of financial knowledge. Host formats an external value without independently validating it.

Evidence: SRC-1, `libs/agno/agno/tools/yfinance.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Price string, could-not-fetch string or exception string.
- Later read-back: inapplicable — this entrypoint itself writes no retained state; enclosing run storage may retain tool output.
- Delegated visibility: Foreground tool-result messages; team/workflow transfer is governed by supplied routes.
- Selection predicate: Granted tool and chosen symbol.
- Invalidation or expiry: inapplicable — no retained price is maintained by this entrypoint.
- Activation or effect: Returns imported/formatted value to current model invocation; actual service response and use unobserved.
- Evidence limits: Provider truth, timestamps and freshness unverified; successful return is not a final-brief check.

Check target and evaluator domain: No independent evaluator; field selection and formatting are host rules on an external numeric datum.
Epistemic authority and scope: Source warrant unknown: an attributed provider field is returned without a measurement or independent factual check.
Operational authority and behavioral-authority path: Foreground model receives tool data, advisory information for current answer; local Function dispatch has enforcing executable force but no factual license.

> current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))
> return f"{current_price:.4f}" if current_price else f"Could not fetch current price for {symbol}"
> --- `libs/agno/agno/tools/yfinance.py`

#### EPI-RTE-output-replacement
Label: Output and parser response replacement

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
These are optional answer-replacement stages within the supplied execution route.

Host calls optional output model with prepared messages and replaces model_response.content. Optional parser model requires output_schema, calls response with response_format and copies content/parsed when an assistant message exists. The stages differ in target: output generation versus schema-oriented rewriting. Output generation substitutes content before parser rewriting; a successful parser branch substitutes both content and parsed fields afterward. Neither stage checks semantic fidelity. Stage-owned input, admission and downstream-consumer findings are declared in [EPI-RTE-output-generation](#epi-rte-output-generation) and [EPI-RTE-parser-rewriting](#epi-rte-parser-rewriting); this record remains their valid container, not evidence of independent finality. No actual answer establishes preservation, entailment or non-entailment.

Evidence: SRC-1, `libs/agno/agno/agent/_response.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Replaced ModelResponse content; parser may also replace parsed.
- Later read-back: Configured RunOutput persistence can store post-stage output and filtered messages; stage-specific message lineage is declared in the two part records. Exact future replay selection remains uninspected here.
- Delegated visibility: Subsequent stages and RunOutput consumers receive stage-dependent content; the output-model stage is not independently final when the parser substitutes afterward.
- Selection predicate: Non-null output_model; parser_model plus output_schema; assistant-message presence for parser copy.
- Invalidation or expiry: inapplicable — these stages own no independent retained version/rollback store.
- Activation or effect: Replaces the answer used by later conversion, post-hooks and return.
- Evidence limits: Model compliance and semantic preservation unobserved; schema conversion is not factual acceptance.

Check target and evaluator domain: Output/parser inference consumes prepared text; host checks configuration/assistant-message presence and format, not truth.
Epistemic authority and scope: No new factual warrant from replacement or output shape. Acquisition, reshaping, derivation and conjecture cannot be distinguished for unseen model outputs.
Operational authority and behavioral-authority path: Ordered host substitutions affect ModelResponse before RunOutput update, conversion and post-hooks. Current-run payload force is implemented; later replay depends on persistence, filtered message retention and history selection, not independently final output from each stage.

> model_response.content = output_model_response.content
> --- `libs/agno/agno/agent/_response.py:605-605`

> run_messages.messages.append(parser_model_response_message)
> model_response.parsed = parser_model_response.parsed
> model_response.content = parser_model_response.content
> --- `libs/agno/agno/agent/_response.py`

#### EPI-RTE-output-generation
Label: Output-model generation and substitution

Part of: [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Distinct material stage within that container: output-model inference, not parser inference. In the inspected returning sync route, host passes the actual run-message list to get_messages_for_output_model. A configured output_model_prompt replaces the first system message or inserts one; the helper unconditionally pops the last entry (comment identifies it as assistant) and returns the list. Thus this stage does not simply rewrite the preceding answer as a user payload. Model.response consumes that modified context and host copies only its content into the existing ModelResponse; the helper mutates the list later used for message retention. SRC-1, `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/agent/_response.py`, `libs/agno/agno/agent/_run.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Helper returns None after substituting ModelResponse.content; existing parsed and other response fields are not copied from output_model_response by this helper.
- Later read-back: Conditional persistence can retain downstream RunOutput content and add_to_agent_memory-filtered messages; future replay selection remains uninspected. This helper has no explicit append of an output assistant message; provider response message mutation is not independently audited here.
- Delegated visibility: Output model gets modified run messages, not the removed final entry; next parser gets the substituted content, not the full run-message list.
- Selection predicate: Non-null output_model; optional output_model_prompt selects system replacement/insertion. Successful response return selects unconditional content copy; no factual veto here.
- Invalidation or expiry: inapplicable — no independent stage version, expiry or rollback store; subsequent parser may overwrite this content.
- Activation or effect: Enforcing content substitution before parser and RunOutput update; also mutates message context. Actual activation and consumer dependence unobserved.
- Evidence limits: Returning sync route inspected; no exhaustive stream/async equivalence, provider mutation audit, fidelity or factual acceptance. Preexisting parsed content may govern downstream output instead of this text.

Check target and evaluator domain: Host tests configuration; model generates under modified instructions/context, not an evidence-consuming truth criterion. Caller configures/proposes guidance; model proposes content; host copies it. No answer oracle or mandatory human per-content approval; open task mode. Disabling the model withholds this stage; later parser/hooks may change or reject output, not restore its prior content automatically.
Epistemic authority and scope: No new factual warrant. Relation indeterminate among preservation, derivation and conjecture without actual inputs/outputs and warranted premises.
Operational authority and behavioral-authority path: Host assigns content; optional parser receives it as user text; update_run_response subsequently selects parsed versus content under schema rules, then conversion/post-hooks/return. Force enforcing current payload substitution, with conditional persisted horizon, not independently final output or guaranteed replay.

> if message.role == "system":
>     system_message_exists = True
>     message.content = agent.output_model_prompt
>     break
> --- `libs/agno/agno/agent/_messages.py`

> # Remove the last assistant message from the messages list
> messages.pop(-1)
>
> return messages
> --- `libs/agno/agno/agent/_messages.py`

> messages_for_output_model = get_messages_for_output_model(agent, run_messages.messages)
> output_model_response: ModelResponse = agent.output_model.response(messages=messages_for_output_model)
> --- `libs/agno/agno/agent/_response.py`

Content-copy evidence: see [EPI-RTE-output-replacement](#epi-rte-output-replacement).

#### EPI-RTE-parser-rewriting
Label: Parser-model rewriting and substitution

Part of: [EPI-RTE-output-replacement](#epi-rte-output-replacement)
Distinct material stage: schema-oriented inference after output generation, not a second declaration of output generation. Host prepares a separate two-message list: parser-specific/default system guidance and current ModelResponse.content as user content. JSON-object mode adds schema guidance when output_schema exists. Parser.response receives response_format. process_parser_response searches backward for an assistant message; only that branch appends the assistant to run_messages and copies both parsed and content. No assistant leaves previous fields unchanged and warns. SRC-1, `libs/agno/agno/agent/_messages.py`, `libs/agno/agno/agent/_response.py`, `libs/agno/agno/agent/_run.py` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Helper returns None; successful assistant branch replaces content/parsed and appends that assistant; otherwise warns without these substitutions.
- Later read-back: Appended assistant can enter RunOutput.messages only under add_to_agent_memory filtering and configured persistence; later history replay selection remains uninspected. Persisted RunOutput content is separately selected by parsed/schema rules.
- Delegated visibility: Parser receives resulting answer content and its own prompt/schema, not the whole original evidence context. Downstream RunOutput update sees copied fields and message list.
- Selection predicate: parser_model configured and run_context.output_schema non-null; assistant-message presence selects substitution. Caller controls prompt/schema; model proposes structured output; host decides structural copy, not truth.
- Invalidation or expiry: inapplicable — no separate parser version/rollback store; absent assistant preserves preceding fields rather than revoking them.
- Activation or effect: Enforcing content/parsed substitution after output stage and assistant-message append before RunOutput update. Actual execution and replay effects unobserved.
- Evidence limits: Format request and assistant presence do not verify semantic fidelity or source truth. Returning sync route inspected; no universal finality or stream/async equivalence established.

Check target and evaluator domain: Schema-oriented model generation plus host assistant-presence check; no independent factual evaluator or answer oracle. Open task mode; caller can disable stage/change prompt/schema, human authorship or approval unresolved. No rollback of preceding effects; later hooks may reject status without erasing content.
Epistemic authority and scope: No factual acceptance from structured shape. Semantic relation indeterminate for unseen candidates; prompt requests rewriting, not proof it preserved meaning.
Operational authority and behavioral-authority path: Parser content/parsed → host ModelResponse assignment → RunOutput update chooses parsed under structured-output conditions, otherwise content where its branch applies → conversion/post-hooks/return/storage. Appended message separately reaches filtered retained messages. Enforcing current substitution and conditional later history availability; not guaranteed replay or unchanged final return.

> return [
>     Message(role="system", content=system_content),
>     Message(role="user", content=model_response.content),
> ]
> --- `libs/agno/agno/agent/_messages.py:2449-2472`

> if parser_model_response_message is not None:
>     run_messages.messages.append(parser_model_response_message)
>     model_response.parsed = parser_model_response.parsed
>     model_response.content = parser_model_response.content
> else:
>     log_warning("Unable to parse response with parser model")
> --- `libs/agno/agno/agent/_response.py`

> # If an output model is provided, generate output using the output model
> generate_response_with_output_model(agent, model_response, run_messages, run_response=run_response)
>
> # If a parser model is provided, structure the response separately
> parse_response_with_parser_model(
>     agent, model_response, run_messages, run_context=run_context, run_response=run_response
> )
> --- `libs/agno/agno/agent/_run.py:581-587`

> if output_schema is not None and model_response.parsed is not None:
>     # We get native structured outputs from the model
>     if model_should_return_structured_output(agent, run_context=run_context):
>         # Update the run_response content with the structured output
>         run_response.content = model_response.parsed
> --- `libs/agno/agno/agent/_response.py`

> messages_for_run_response = [m for m in run_messages.messages if m.add_to_agent_memory]
> # Update the RunOutput messages
> run_response.messages = messages_for_run_response
> --- `libs/agno/agno/agent/_response.py:1018-1021`

#### EPI-RTE-pii-input
Label: PII input detection and masking

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
An optional pre-hook guardrail rather than a second Agent dispatcher.

Regex search judges input_content_string against enabled SSN/card/email/phone/custom patterns. With mask_pii the hook substitutes equal-length asterisks and overwrites input_content; otherwise it raises InputCheckError. Example deduction from inspected code: with email-only checking, input "Contact a@b.com" becomes "Contact *******" in masking mode; rejection mode raises instead. This deliberately removes a fact-bearing value and cannot license semantic equivalence. The evaluator domain is lexical pattern membership, not real-world sensitivity or truth.

Evidence: SRC-1, `libs/agno/agno/guardrails/pii.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: No return payload; mutated input or InputCheckError.
- Later read-back: inapplicable — no independent guardrail memory; mutated input may be retained by enclosing run.
- Delegated visibility: Subsequent message preparation receives masked input when configured; no delivery of hidden text through this hook.
- Selection predicate: Configured hook, enabled patterns and at least one match.
- Invalidation or expiry: inapplicable — no retained guardrail result store in this implementation.
- Activation or effect: Masks or interrupts current run before model use on the hook path.
- Evidence limits: False positives/negatives outside regex membership remain possible. No universal content or effect safety gate is established.

Check target and evaluator domain: Deterministic regex evaluator on text; caller chooses mask/reject and pattern set. No answer oracle; human authorship of request/configuration unresolved.
Epistemic authority and scope: Establishes syntactic match only. Transformation removes information; cannot establish a truth-preserving rewrite.
Operational authority and behavioral-authority path: Pre-hook consumer uses InputCheckError as enforcing stop or RunInput mutation as enforcing substitution; horizon current request.

> content = self.pii_patterns[pii_type].sub(mask_match, content)
> run_input.input_content = content
> return
> --- `libs/agno/agno/guardrails/pii.py:56-78`

#### EPI-RTE-output-hooks
Label: Post-hook rejection and cleanup

Part of: [RT-RTE-agent-run](runtime.md#rt-rte-agent-run)
This declares the exception-consuming post-output stage, not a duplicate of the whole run.

Host sequentially invokes configured hooks after output generation. InputCheckError/OutputCheckError propagates; ordinary exceptions are logged. Sync run skips async hooks. Background scheduling is separate: global background mode runs identified guardrails synchronously, schedules other hooks on copied arguments. The Agent returning path catches check exceptions, marks RunStatus.error and persists cleanup; it keeps preexisting content rather than erasing it. Thus rejection can change return status without withdrawing all generated content, prior storage or tool effects. Streaming already-emitted text is not retracted by the shown returning-path code.

Evidence: SRC-1, `libs/agno/agno/agent/_hooks.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Hook events or raised check exception; Agent catches it and returns error RunOutput.
- Later read-back: Error output can be persisted by cleanup_and_store; no universal replay exclusion is established.
- Delegated visibility: Hooks receive filtered run_output/agent/session/context arguments; background hooks receive copied args.
- Selection predicate: Configured post_hooks and hook identity/background settings.
- Invalidation or expiry: inapplicable — exception handling does not implement retained-claim revocation or effect rollback.
- Activation or effect: Check exceptions enforce non-completed run status; ordinary hook failures may leave continuation intact.
- Evidence limits: Exact evaluator/criterion belongs to each caller hook. Cannot infer a truth oracle from generic hook capability. Async/stream equivalence not exhaustively inspected.

Check target and evaluator domain: Caller hooks propose/judge/veto; computational host consumes specific error classes. Open task mode; oracle and human participation caller-dependent/unresolved.
Epistemic authority and scope: A hook rejection is only as warranted as its named criterion; generic machinery grants no truth license.
Operational authority and behavioral-authority path: Hook exception → Agent error handler → returned/persisted status, enforcing current run non-completion; no automatic rollback of prior external effects.

> except (InputCheckError, OutputCheckError) as e:
>     raise e
> except Exception:
>     log_exception(f"Post-hook #{i + 1} execution failed")
> --- `libs/agno/agno/agent/_hooks.py:354-357`

> if run_response.content is None:
>     run_response.content = str(e)
> 
> log_error(f"Validation failed: {str(e)} | Check trigger: {e.check_trigger}")
> --- `libs/agno/agno/agent/_run.py:697-700`

#### EPI-RTE-judge-check
Label: Criteria judgment and callback

No counterpart after comparison with supplied runtime records; generic post-hooks are the containing seam, but this independent evaluator also has standalone entry points.

Caller supplies criteria, strategy, threshold, evaluator/model and optional on_fail. Evaluator inference judges answer against criteria, returns typed reason and score/pass. Host threshold converts numeric score to passed; binary mode uses model passed. A failed judgment invokes on_fail if configured; callback errors are logged. post_check evaluates and optionally logs, but does not itself raise OutputCheckError for a failed judgment. The callback may implement a veto; its actual effects are not supplied. Evaluation failure returns None rather than a valid acceptance. This positive witness defeats a system-wide claim that Agno has no output evaluators; it does not make all model outputs accepted knowledge.

Evidence: SRC-1, `libs/agno/agno/eval/agent_as_judge.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AgentAsJudgeEvaluation or None; callback may act on failed judgment.
- Later read-back: Optional DB/file evaluation logging; later policy consumers of stored judgments uninspected.
- Delegated visibility: Judge receives formatted input/output and criteria; callback receives evaluation.
- Selection predicate: Explicit evaluation or configured post-hook; numeric threshold or binary model passed; on_fail only when failed.
- Invalidation or expiry: uninspected — no judgment expiry or revision policy established by these reads.
- Activation or effect: Judgment recorded/returned; failed result conditionally invokes callback; post_check logging alone does not reject run.
- Evidence limits: No observed judge calibration, accepted factual candidate or causal outcome; arbitrary callback force is caller-dependent.

Check target and evaluator domain: Judge model evaluates input/output under caller criteria; host threshold decides pass. Caller can select/veto configuration; programmatic calls need not involve a human. Open or caller-bounded cases; no independent answer oracle by default.
Epistemic authority and scope: A criteria-relative model opinion, not independent factual verification. No universal intended factual use/scope follows from caller criteria.
Operational authority and behavioral-authority path: Standalone result is advisory; threshold is enforcing classification; on_fail channel permits caller-defined action; post_check logs at current-run horizon without built-in fail-to-error enforcement.

> score = judge_response.score
> passed = score >= self.threshold
> --- `libs/agno/agno/eval/agent_as_judge.py:301-357`

> self.on_fail(evaluation)
> --- `libs/agno/agno/eval/agent_as_judge.py:301-357`

#### EPI-RTE-accuracy-check
Label: Reference-relative accuracy evaluation

No counterpart after comparison with supplied runtime records or criteria-only judge; this evaluator explicitly imports a reference outcome.

Default evaluator is instructed to assume user-provided expected_output correct and compare answer only to it. Agent output is scored for closeness and completeness, yielding typed AccuracyEvaluation. Invalid model result or evaluator exception returns None. Target is answer-reference agreement, not reference truth. Callable references are caller-controlled. No automatic product/configuration successor selection or factual admission consumer is established by the inspected evaluate_answer method.

Evidence: SRC-1, `libs/agno/agno/eval/accuracy.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AccuracyEvaluation with score/reason or None.
- Later read-back: uninspected — storage/export consumers outside the inspected evaluate_answer method not traced.
- Delegated visibility: Evaluator receives constructed evaluation text including answer/reference; no child-policy update established.
- Selection predicate: Explicit accuracy evaluation using configured/default evaluator.
- Invalidation or expiry: uninspected — no reference invalidation policy inspected.
- Activation or effect: Produces reference-relative evidence for caller; no inspected automatic rejection or revision.
- Evidence limits: Score does not certify oracle accuracy, producing mechanism or transfer. Custom evaluator may differ from default instructions.

Check target and evaluator domain: Default LLM comparator; expected answer supplied by caller/string or callable. Reference is an answer oracle by role, with correctness assumed rather than established; human origin unresolved.
Epistemic authority and scope: At most model-assessed agreement with an assumed-correct reference, not warrant for that reference.
Operational authority and behavioral-authority path: Caller consumes returned score/reason advisory for this evaluation; no inspected automatic production gate.

> 2. Do not judge the correctness of the expected_output itself. Your role is only to compare the two outputs, the user provided expected_output is correct.
> --- `libs/agno/agno/eval/accuracy.py`

> score=accuracy_agent_response.accuracy_score,
> reason=accuracy_agent_response.accuracy_reason,
> --- `libs/agno/agno/eval/accuracy.py:293-325`

#### EPI-RTE-reliability-check
Label: Recorded tool execution expectations

Distinct from [RT-RTE-agent-run](runtime.md#rt-rte-agent-run) and [RT-BAP-function-dispatch](runtime.md#rt-bap-function-dispatch): those execute calls; this evaluates evidence of calls already made.

Host gathers Agent tools or nested Team member evidence; excludes from_history requests. Expected names require clean, nonpaused ToolExecution; unexpected attempts can fail strict mode even when refused. Argument specs require equal expected key-values in at least one clean call. Missing/failed/argument mismatches determine PASSED/FAILED. assert_passed is an explicit caller gate. Deduction: an expected "lookup" with only a paused ToolExecution cannot enter clean_names, so is missing and fails even if an assistant requested it. Conversely tool_call_error=None counts clean, limiting inference about rehydrated evidence.

Evidence: SRC-1, `libs/agno/agno/eval/reliability.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ReliabilityResult; assert_passed raises assertion for FAILED when assertions enabled.
- Later read-back: uninspected — evaluation DB logs/reload and their later consumers not fully traced.
- Delegated visibility: Team evidence unions nested members; no parent-wide truth evaluation.
- Selection predicate: Caller supplies response and expected names/arguments/strictness.
- Invalidation or expiry: inapplicable — evaluator does not revise or invalidate stored tool effects.
- Activation or effect: Produces deterministic evidence-relative status and optional explicit assertion gate.
- Evidence limits: Not final-answer accuracy or exactly-once effects. Empty expectations may be vacuous; Python assertion force depends on normal assertion-enabled execution.

Check target and evaluator domain: Program compares recorded evidence with caller expectations, including failed/paused distinctions; caller chooses expected outcome and optional veto/assertion. Bounded test or open caller evaluation; reference supplied by caller, human authorship unresolved.
Epistemic authority and scope: Deterministically derived claim about provided execution records within configured tool-name/argument domain; source record trust is a premise, not checked external service success.
Operational authority and behavioral-authority path: Returned status advisory; explicit assert_passed enforces caller test continuation at current evaluation horizon.

> clean_executions = [t for t in executions if t.tool_name and not t.tool_call_error and not t.is_paused]
> --- `libs/agno/agno/eval/reliability.py`

> assert self.eval_status == "PASSED", f"ReliabilityEval failed: {self}"
> --- `libs/agno/agno/eval/reliability.py`

#### EPI-RTE-learning-extraction
Label: Conversation learning extraction

No counterpart after comparison with supplied runtime records; a separate model/tool extraction route, not foreground answer production.

extract_and_save converts messages to conversation text, searches first 500 characters for existing learnings (limit 5), provides existing summary plus extraction guidance, deep-copies configured model and calls it with save tools and max_updates_per_run. Guidance asks for investigated, reusable, durable insights and explicit organizational directives, not uncertain conclusions. The save tool commits candidate text directly through save; no separate truth test is shown. Semantic relation remains indeterminate: imported directives, paraphrases, and generalizations are all requested, with no candidate instance to distinguish them. Model request is not observed criticism or warranted induction.

Evidence: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: No returned candidate batch; optional save-tool effects and learning_saved flag.
- Later read-back: Saved text may be retrieved later through [EPI-RTE-learning-recall](#epi-rte-learning-recall); flag alone is not proof of a successful insert because tool_executions presence sets it.
- Delegated visibility: Extractor receives conversation text and limited existing-summary context, not all saved learnings.
- Selection predicate: Model and knowledge must exist; mode/programmatic caller selects extraction; max_updates_per_run limits requested updates.
- Invalidation or expiry: inapplicable — extraction implements no candidate expiry or independent supersession.
- Activation or effect: Model can invoke save tool during extraction; actual extraction/save and downstream effect unobserved.
- Evidence limits: No source evidence acceptance record; backend, actual candidates, semantic fidelity and improvement remain unresolved.

Check target and evaluator domain: Model chooses whether/what to save under guidance; code bounds calls and exposes save. Open conversational extraction; no independent oracle or mandatory human approval.
Epistemic authority and scope: Requested reusable insights are candidates; no separate evidence-consuming acceptance against truth criteria is established. Organizational directives instead have policy authority.
Operational authority and behavioral-authority path: Extractor model receives selection guidance via system text, advisory; symbolic save-tool calls carry enforcing insertion capability for configured store, later scope caller/backend-dependent.

> existing = self.search(query=conversation_text[:500], limit=5)
> existing_summary = self._summarize_existing(learnings=existing)
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:1100-1151`

> model_copy = deepcopy(self.model)
> response = model_copy.response(
>     messages=extraction_messages,
>     tools=functions,
>     tool_call_limit=self.config.max_updates_per_run,
> )
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:1100-1151`

#### EPI-RTE-learning-save
Label: Learning and knowledge insertion

No counterpart after comparison with supplied RunContext/config records; this writes knowledge text rather than versioned runtime configuration.

save strips fields, validates schema and user namespace identity, builds metadata, and calls Knowledge.insert(skip_if_exists=True). Agent save_learning calls it directly; PROPOSE guidance asks user approval, but save signature/entrypoint does not test an approval token or preceding search. get_agent_tools grants save by agent_can_save. Direct callers and extractor tool use the same writer. Generic add_to_knowledge separately sanitizes document name, JSON-encodes query/result and inserts after capability/owner checks; it also has no factual test in that inspected wrapper. Thus these paths have software write admission, not universal human/factual acceptance. delete(title) delegates deletion if supported, without withdrawing already-delivered text.

Evidence: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Success/failure bool or tool confirmation; generic knowledge wrapper returns status string.
- Later read-back: Stored text reaches later query/context through [EPI-RTE-learning-recall](#epi-rte-learning-recall); generic knowledge search entrypoint retrieves documents.
- Delegated visibility: Namespace/user/creator metadata constrain store selection; save tool return is status, not evidence certificate.
- Selection predicate: Knowledge configured; user namespace requires user_id; schema validation; agent_can_save grants tool.
- Invalidation or expiry: Supported delete_content(name=title) can remove a learning; backend duplicate/replace/delete completeness uninspected.
- Activation or effect: Candidate retained without an independent truth judgment; explicit deletion changes future available content, not already-produced effects.
- Evidence limits: No persisted actual claim/approval evidence. Backend skip_if_exists semantics, transactionality and arbitrary knowledge adapters remain uninspected.

Check target and evaluator domain: Caller/model proposes text; schema/namespace/adapter capability admits write, exceptions reject. Human approval requested in PROPOSE prompt but not checked by this writer. Open-request maintenance; no answer oracle. Recovery via supported deletion, not automatic rollback.
Epistemic authority and scope: Insertion establishes retained candidate or instruction, not epistemic acceptance. PROPOSE is soft instruction-level approval on this path, distinct from [RT-RTE-tool-confirmation](runtime.md#rt-rte-tool-confirmation).
Operational authority and behavioral-authority path: Host insertion is enforcing write permission into configured knowledge backend; foreground/extractor caller supplies text; later retrieval delivers advisory information/policy. Horizon retained store until deletion/backend policy.

> self.knowledge.insert(
>     name=learning_data["title"],
>     text_content=text_content,
>     reader=TextReader(),
>     skip_if_exists=True,
>     metadata=filter_metadata,  # Pass metadata for filtering
> )
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:881-964`

> Call `save_learning` ONLY after the user says "yes" to your proposal.
> --- `libs/agno/agno/learn/stores/learned_knowledge.py`

> document_content = json.dumps({"query": query, "result": result}, ensure_ascii=False)
> --- `libs/agno/agno/agent/_default_tools.py`

#### EPI-RTE-learning-recall
Label: Learning search and context reliance

Distinct from [RT-RTE-context-window](runtime.md#rt-rte-context-window): query-selected learned knowledge is supplied, rather than compacted conversation history.

recall selects query or current message, requires user_id for user namespace, and searches configured Knowledge. search passes namespace filters where available, parses returned results, post-filters namespace and applies limit. search_learnings formats matching learning objects into a tool string. Mode context appends relevant learnings with "Apply these naturally if relevant"; Agent _messages requests LearningMachine.build_context and appends guidance/data to system message when add_learnings_to_context. These are information/guidance channels, not proof that a consumer followed them. Query similarity and namespace are not correctness criteria.

Evidence: SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Learning objects or None/empty; formatted tool/context text.
- Later read-back: Later invocations can select saved learnings; actual retained-instance lineage and behavioral dependence unobserved.
- Delegated visibility: Foreground model receives formatted selected results, not entire KB or external evidence supporting them.
- Selection predicate: Query/message, configured namespace, user identity, result limit; tool grant or add_learnings_to_context.
- Invalidation or expiry: Deleted/unreturned material not selected; backend index freshness/cache behavior uninspected.
- Activation or effect: Delivers selected prior content through tool result or system context; operational compliance and benefit unobserved.
- Evidence limits: Semantic search scoring, embedding provenance and generic knowledge ingestion/re-ranking uninspected; similarity does not warrant truth.

Check target and evaluator domain: Code query/namespace/limit selects; backend semantic ranking domain is relevance, not truth; model decides how to use delivered text. No oracle, human per-read decision not required.
Epistemic authority and scope: Retained assertions are delivered with unknown source warrant; policy text is guidance. No acceptance or post-acceptance lifecycle integration is demonstrated by recall.
Operational authority and behavioral-authority path: Foreground model; formatted tool strings or system-message learning_block; advisory natural-language authority; current inference and subsequent configured recall horizon.

> results = self.knowledge.search(query=query, max_results=limit, filters=filters)
> --- `libs/agno/agno/learn/stores/learned_knowledge.py:747-795`

> system_message_content += learning_block + "\n"
> --- `libs/agno/agno/agent/_messages.py:1164-1164`

#### EPI-RTE-profile-curation
Label: Profile pruning and string deduplication

No counterpart after comparison with supplied runtime records; distinct user-profile cleanup, not general knowledge verification.

Curator loads only user_profile, drops old timestamped memories or keeps newest count and saves changed profile. Missing/unparseable timestamps survive age pruning. Deduplication normalizes content to lowercase, strips punctuation and collapses whitespace; first normalized-key occurrence survives and others are removed. Concrete deduction: "US policy" and "us policy" share "us policy" and the latter is dropped if second, although acronym-versus-pronoun meaning can differ. Likewise "x=1" and "x!=1" normalize to "x1"; contradictory content can collide. These are implementation deductions, not executions. Cleanup therefore does not establish semantic equivalence or factual refutation. Age and count are storage policies, not withdrawal of epistemic endorsement.

Evidence: SRC-1, `libs/agno/agno/learn/curate.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Number removed, or zero when store/profile/memories missing.
- Later read-back: Changed profile is passed to store.save; exact user-profile reload/render path uninspected here.
- Delegated visibility: Store receives survivor list; dropped content not included in this saved list.
- Selection predicate: Explicit prune/deduplicate, user_id; age/count controls; normalized content keys.
- Invalidation or expiry: Removals replace profile.memories; no archive/undo in inspected Curator.
- Activation or effect: Enforcing deletion from saved list; no truth test or learned-policy improvement shown.
- Evidence limits: Actual profile schema may lack memories; only guarded capacity established. No universal deduplication or semantic preservation conclusion.

Check target and evaluator domain: Program assesses age/count and normalized-string equivalence; caller chooses controls, no human per-content review or answer oracle. Recovery uninspected; no rollback exposed by Curator.
Epistemic authority and scope: No equivalence license for normalization collisions and no truth license from recency. Remaining content is not accepted by being kept.
Operational authority and behavioral-authority path: Curator program → store.save survivor list, enforcing maintenance; later profile consumers receive reduced availability, exact read-back authority uninspected.

> text = text.lower().strip()
> text = re.sub(r"[^\w\s]", "", text)
> text = re.sub(r"\s+", " ", text)
> return text
> --- `libs/agno/agno/learn/curate.py`

> profile.memories = unique_memories
> store.save(user_id=user_id, profile=profile)
> --- `libs/agno/agno/learn/curate.py`

#### EPI-RTE-sft-selection
Label: Scored rollout export selection

No counterpart after comparison with supplied runtime records; this is an external training-artifact consumer of evaluated runs, not a deployed configuration update.

Environment engine scores only completed runs and keeps scorer failure unscored. JudgeScorer can classify via explicit model/criteria and numeric threshold or binary response. Exporter first excludes unscored; default only_passed rejects failed. It then drops tool-limit-hit runs, tool-bearing runs and nonexportable text. Role/content export excludes from_history and keeps system/user/assistant through final assistant with actual raw text, not str(run.content). JSONL plus sidecar keeps indices/scores/fingerprints; caps drop tail candidates. This is evidence-consuming operational dataset admission for conversational SFT within caller criteria and text-only schema. It is not independent factual acceptance or proof of successful training. only_passed=False is a material alternate permitting scored failures. No training API is called by this exporter.

Evidence: SRC-1, `libs/agno/agno/environments/exporters/sft.py` (implementation unless expressly marked doctrine/design).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ExportReport counters; JSONL and .meta.json files.
- Later read-back: External trainer can read files; no later trainer execution or parameter change supplied/inspected.
- Delegated visibility: Export omits tool traces by rejecting tool-bearing attempts; history excluded; sidecar has score/indices rather than full warrant.
- Selection predicate: Scored attempts; only_passed defaults true; textual conversation, no tool/limit-hit, count/byte caps.
- Invalidation or expiry: Caller-selected file overwritten by export; automatic dataset revocation/backend training rollback uninspected.
- Activation or effect: Enforcing candidate-to-dataset selection and file write; no automatic policy/weight installation.
- Evidence limits: Score inherits chosen scorer assumptions; rollout cloning/fingerprints/export validation and external consumers not exhaustively traced. No observed run or causal improvement.

Check target and evaluator domain: Caller-selected scorer judges completed attempt; exporter decides inclusion and caller can override only_passed. JudgeScorer model/criteria, CodeScorer custom rules and ToolCallScorer expectations are separate evaluator domains; only judge conversion and export consumer directly read here. Expected outcomes caller-dependent; no universal oracle.
Epistemic authority and scope: Dataset suitability under selected scorer and text-only export criteria; no source-truth, causal mechanism or transfer license. This is not produced accepted ampliative knowledge merely because the score passed.
Operational authority and behavioral-authority path: Exporter consumes Score.passed and trace flags, enforcing file admission for external SFT horizon; external training and live organization effects unestablished.

> if attempt.score is None:
>     return None  # not a candidate: unscored attempts never reach the exporter
> if only_passed and not attempt.score.passed:
>     report.n_skipped_failed += 1
>     return None
> --- `libs/agno/agno/environments/exporters/sft.py`

> state.score = await scorer.ascore(run, expected_value)
> --- `libs/agno/agno/environments/_engine.py`

> passed=content.score >= self.threshold,
> --- `libs/agno/agno/scorer/judge.py`

### Claims

#### EPI-CLM-learning-loop
Label: Learning loop with simulations and usage data

Claimed operation: own the stack/data/memory/security and turn the agent platform into a learning loop with simulations and usage data. Claim conclusion status: claimed. Distinct from [RT-CLM-market-brief](runtime.md#rt-clm-market-brief): this concerns platform learning rather than financial output. SRC-1, `README.md` (doctrine/design). It is framed as something the platform enables, not evidence that a shipped deployment improved.

> Agno allows you to own your agent stack. Maintain control of your data, memory, and security posture (JWT-based RBAC), and turn your agent platform into a learning loop with simulations and usage data.
> --- `README.md`

#### EPI-CLM-propose-approval
Label: PROPOSE learning approval policy

Claimed operation: PROPOSE mode saving requires user approval, with save_learning only after explicit yes. Claim conclusion status: claimed. No counterpart after comparison with supplied claims; this is the learned-knowledge mode policy, not local tool confirmation. SRC-1, `libs/agno/agno/learn/stores/learned_knowledge.py` (doctrine/design in model instructions; implementation provides the prompt and shared writer). The writer supplies a counterexample to interpreting this request as universal enforced admission.

> You have a knowledge base of reusable learnings. In PROPOSE mode, saving requires user approval.
> --- `libs/agno/agno/learn/stores/learned_knowledge.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

The route declarations carry their distinct consumers, channels, forces and horizons; supplied [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions) and [RT-BAP-function-dispatch](runtime.md#rt-bap-function-dispatch) retain the enclosing text-policy and executable-dispatch paths.
