---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Wuphf epistemic routes: cited answers, fact synthesis, contradiction disposal and verified-task reliance."
run-id: AAS-2026-10-15-wuphf-b246722f99c0-01
reviewed-boundary: "88023d4dac7491b6e71dbc1e86d274c435b9cb2c"
---

# Wuphf epistemic report

## Source-and-claim boundary

The question is how Wuphf (called gawkbot in the frozen source) turns inputs and execution results into content for later reliance, and what its checks license. Scope, exclusions, dependencies and evidence identity are those of the [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). This remains a complete artifact, partial loop, not a system-complete assessment. All new inspection below is SRC-1 implementation at the frozen revision; attributed tool/product descriptions are doctrine/design. No target code, models, tests, examples or services were run. No deployment trace, result dataset or causal comparison was supplied.

Material operations include model-produced factual text, provenance shaping, software checks and admission, truth-claim disposal, and behavior-changing reuse. Ordinary transport is included only where it changes warrant or force. The public claims examined are [EPI-CLM-cited-knowledge](#epi-clm-cited-knowledge), [EPI-CLM-verified-lookup](#epi-clm-verified-lookup), and the runtime's [RT-CLM-external-approval](runtime.md#rt-clm-external-approval). They have different scopes; an approval gate is not a truth test.

| Entry point or operation | Source path | Coverage and records, or uninspected responsibility and conclusion prevented |
|---|---|---|
| CLI dispatch and memory migrate | `cmd/wuphf/main.go`, `cmd/wuphf/memory.go` | Direct dispatch searches and migrate orchestration read; migration adapter/conversion not traced, so imported content fidelity is unassessed. |
| Office providers, planning and app publication | `internal/team/headless_codex.go`, `internal/team/broker_apps.go` | Supplied runtime findings, not independently reread: [RT-RTE-office-turn](runtime.md#rt-rte-office-turn), [RT-RTE-compatible-turn](runtime.md#rt-rte-compatible-turn), [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval), [RT-RTE-app-publication](runtime.md#rt-rte-app-publication). Alternate native CLI contexts remain opaque. |
| Sidecar authoring, replay, saved calls, routines | `agent/src/service.ts`, `agent/src/capabilities.ts` | Supplied [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring), [RT-RTE-saved-call](runtime.md#rt-rte-saved-call), [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay), [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool); direct realAI read adds [EPI-RTE-ai-results](#epi-rte-ai-results). |
| Registered memory, entity, learning, playbook, lookup and lint tools | `internal/teammcp/server.go`, `internal/teammcp/learning_tools.go`, `internal/teammcp/server_wiki_tools.go` | Direct registration read and handler searches; [EPI-RTE-lint-disposal](#epi-rte-lint-disposal), [EPI-RTE-query-answer](#epi-rte-query-answer). Notebook promotion, canonical-write delegation and legacy GBrain handlers remain untraced; no universal acceptance conclusion. |
| Artifact extraction hook | `internal/team/broker_wiki_lifecycle.go`, `internal/team/wiki_extractor.go` | Direct hook search and extraction/application read: [EPI-RTE-extract-facts](#epi-rte-extract-facts). Worker hook timing, immutable capture, full entity resolution and DLQ replay implementation not inspected; no complete lineage/recovery guarantee. |
| Entity synthesis and cleanup | `internal/team/entity_synthesizer.go` | Direct synthesis and stripper read: [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief), [EPI-RTE-related-cleanup](#epi-rte-related-cleanup). Initial FactLog provenance and every graph update uninspected. |
| Contradiction check and withdrawal | `internal/team/wiki_lint.go`, `internal/team/broker_lint.go` | Direct judge, resolution and HTTP handler reads: [EPI-RTE-lint-judge](#epi-rte-lint-judge), [EPI-RTE-lint-disposal](#epi-rte-lint-disposal). Full index invalidation/retrieval filtering after expiry uninspected; no universal withdrawal guarantee. |
| Task completion checks and trace-fed memory | `internal/team/task_verification.go`, `internal/team/task_distill.go`, `internal/team/broker_tasks_mutation_service.go` | Direct checks, gate, distillation read and caller searches: [EPI-RTE-task-check](#epi-rte-task-check), [EPI-RTE-task-admission](#epi-rte-task-admission), [EPI-RTE-task-distill](#epi-rte-task-distill). Artifact-delta gates and every task mutation path not fully traced. |
| Learning admission and context use | `internal/team/learnings.go`, `internal/team/context_assembler.go` | Direct validator, append, search and task packet reads: [EPI-RTE-learning-write](#epi-rte-learning-write), [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet). Full confidence decay/dedup semantics and all packet wiring not independently traced. |
| Playbook draft and compile | `internal/team/playbook_draft.go`, `internal/team/playbook_compiler.go`, `internal/team/wiki_worker.go` | Direct draft contract, eligibility, emitted draft marker, compiler and registration searches: [EPI-RTE-playbook-compile](#epi-rte-playbook-compile). Full draft transformation, policy compiler, v2 synthesis and actual skill invocation uninspected; no reliable procedural transfer claim. |
| Prompt evaluation | `evals/README.md`, `cmd/eval-prompts/runner.go` | Direct harness documentation and runCase read: [EPI-RTE-prompt-eval](#epi-rte-prompt-eval). Main exit/report consumers, matcher internals, benchmarks, office-eval jobs and app evaluators not traced; no quality certification or deployment-gate finding. |
| Other included consumers and maintainers | `web/src/`, `internal/team/memory_workflow_reconciler.go`, `internal/team/broker_apps_knowledge.go`, `internal/team/broker_wiki_obsidian.go` | Available, unassessed: frontend inline citation rendering, memory workflow reconciliation, app knowledge and external-editor admission. Prevents system-complete negatives about acceptance, criticism, policy adaptation or knowledge production. |

Model components are described by [RT-CMP-office-model](runtime.md#rt-cmp-office-model), [RT-CMP-author-model](runtime.md#rt-cmp-author-model), and [RT-CMP-runtime-ai](runtime.md#rt-cmp-runtime-ai). These calls do not inspect provider weights or pin parameter versions. Source-visible inference and configurable endpoints do not establish parameter learning or its absence inside providers.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-typed-fact](#epi-obj-typed-fact) | see record | TypedFact | SRC-1 `internal/team/wiki_extractor.go` | see record |
| [EPI-OBJ-entity-brief](#epi-obj-entity-brief) | see record | entity brief | SRC-1 `internal/team/entity_synthesizer.go` | see record |
| [EPI-OBJ-query-answer](#epi-obj-query-answer) | see record | QueryAnswer | SRC-1 `internal/team/wiki_query.go` | see record |
| [EPI-OBJ-learning-record](#epi-obj-learning-record) | see record | LearningRecord | SRC-1 `internal/team/learnings.go` | see record |
| [EPI-OBJ-verification-result](#epi-obj-verification-result) | see record | TaskVerificationResult | SRC-1 `internal/team/task_verification.go` | see record |
| [RT-OBJ-stored-tool](runtime.md#rt-obj-stored-tool) | see record | StoredTool | SRC-1 `agent/src/store.ts` | see record |
| [RT-OBJ-tool-schema](runtime.md#rt-obj-tool-schema) | see record | TOOL_SCHEMA_PROMPT | SRC-1 `agent/src/tools.ts` | see record |

## Authority-route ledger

Each entry below owns its architectural status and function. Other fields are owned by its cited declaration, including target/domain, content relation, activation, result, license, consumer, channel, force, horizon and limits. Split entries for a single declaration distinguish functions, not new identities. Implementation establishes possible force, not exercised reliance.

Route ID: [EPI-RTE-extract-facts](#epi-rte-extract-facts)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Content/update relation: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Transition or check target: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Evaluator/condition and domain: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Activation and timing: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Possible or observed result: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Implemented force: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Epistemic authority and scope: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Evidence source ID and local anchor: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Claim IDs or none: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Mismatch marker or none: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Gap/limit: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).

Route ID: [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Content/update relation: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Transition or check target: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Evaluator/condition and domain: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Activation and timing: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Possible or observed result: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Implemented force: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Epistemic authority and scope: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Evidence source ID and local anchor: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Claim IDs or none: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Mismatch marker or none: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Gap/limit: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).

Route ID: [EPI-RTE-related-cleanup](#epi-rte-related-cleanup)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Content/update relation: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Transition or check target: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Evaluator/condition and domain: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Activation and timing: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Possible or observed result: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Implemented force: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Epistemic authority and scope: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Evidence source ID and local anchor: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Claim IDs or none: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Mismatch marker or none: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).
Gap/limit: see [EPI-RTE-related-cleanup](#epi-rte-related-cleanup).

Route ID: [EPI-RTE-query-answer](#epi-rte-query-answer)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Content/update relation: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Transition or check target: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Evaluator/condition and domain: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Activation and timing: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Possible or observed result: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Implemented force: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Epistemic authority and scope: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Evidence source ID and local anchor: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Claim IDs or none: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Mismatch marker or none: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Gap/limit: see [EPI-RTE-query-answer](#epi-rte-query-answer).

Route ID: [EPI-RTE-lint-judge](#epi-rte-lint-judge)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Content/update relation: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Transition or check target: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Evaluator/condition and domain: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Activation and timing: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Possible or observed result: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Implemented force: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Epistemic authority and scope: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Evidence source ID and local anchor: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Claim IDs or none: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Mismatch marker or none: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).
Gap/limit: see [EPI-RTE-lint-judge](#epi-rte-lint-judge).

Route ID: [EPI-RTE-lint-disposal](#epi-rte-lint-disposal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Content/update relation: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Transition or check target: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Evaluator/condition and domain: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Activation and timing: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Possible or observed result: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Implemented force: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Epistemic authority and scope: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Evidence source ID and local anchor: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Claim IDs or none: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Mismatch marker or none: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Gap/limit: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).

Route ID: [EPI-RTE-task-check](#epi-rte-task-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-task-check](#epi-rte-task-check).
Content/update relation: see [EPI-RTE-task-check](#epi-rte-task-check).
Transition or check target: see [EPI-RTE-task-check](#epi-rte-task-check).
Evaluator/condition and domain: see [EPI-RTE-task-check](#epi-rte-task-check).
Activation and timing: see [EPI-RTE-task-check](#epi-rte-task-check).
Possible or observed result: see [EPI-RTE-task-check](#epi-rte-task-check).
Implemented force: see [EPI-RTE-task-check](#epi-rte-task-check).
Epistemic authority and scope: see [EPI-RTE-task-check](#epi-rte-task-check).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-task-check](#epi-rte-task-check).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-task-check](#epi-rte-task-check).
Evidence source ID and local anchor: see [EPI-RTE-task-check](#epi-rte-task-check).
Claim IDs or none: see [EPI-RTE-task-check](#epi-rte-task-check).
Mismatch marker or none: see [EPI-RTE-task-check](#epi-rte-task-check).
Gap/limit: see [EPI-RTE-task-check](#epi-rte-task-check).

Route ID: [EPI-RTE-task-admission](#epi-rte-task-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Content/update relation: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Transition or check target: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Evaluator/condition and domain: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Activation and timing: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Possible or observed result: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Implemented force: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Epistemic authority and scope: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Evidence source ID and local anchor: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Claim IDs or none: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Mismatch marker or none: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Gap/limit: see [EPI-RTE-task-admission](#epi-rte-task-admission).

Route ID: [EPI-RTE-task-distill](#epi-rte-task-distill)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Content/update relation: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Transition or check target: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Evaluator/condition and domain: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Activation and timing: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Possible or observed result: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Implemented force: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Epistemic authority and scope: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Evidence source ID and local anchor: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Claim IDs or none: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Mismatch marker or none: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Gap/limit: see [EPI-RTE-task-distill](#epi-rte-task-distill).

Route ID: [EPI-RTE-learning-write](#epi-rte-learning-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Content/update relation: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Transition or check target: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Evaluator/condition and domain: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Activation and timing: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Possible or observed result: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Implemented force: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Epistemic authority and scope: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Evidence source ID and local anchor: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Claim IDs or none: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Mismatch marker or none: see [EPI-RTE-learning-write](#epi-rte-learning-write).
Gap/limit: see [EPI-RTE-learning-write](#epi-rte-learning-write).

Route ID: [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Content/update relation: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Transition or check target: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Evaluator/condition and domain: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Activation and timing: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Possible or observed result: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Implemented force: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Epistemic authority and scope: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Evidence source ID and local anchor: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Claim IDs or none: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Mismatch marker or none: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).
Gap/limit: see [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).

Route ID: [EPI-RTE-playbook-compile](#epi-rte-playbook-compile)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Content/update relation: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Transition or check target: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Evaluator/condition and domain: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Activation and timing: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Possible or observed result: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Implemented force: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Epistemic authority and scope: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Evidence source ID and local anchor: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Claim IDs or none: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Mismatch marker or none: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).
Gap/limit: see [EPI-RTE-playbook-compile](#epi-rte-playbook-compile).

Route ID: [EPI-RTE-ai-results](#epi-rte-ai-results)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Content/update relation: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Transition or check target: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Evaluator/condition and domain: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Activation and timing: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Possible or observed result: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Implemented force: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Epistemic authority and scope: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Evidence source ID and local anchor: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Claim IDs or none: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Mismatch marker or none: see [EPI-RTE-ai-results](#epi-rte-ai-results).
Gap/limit: see [EPI-RTE-ai-results](#epi-rte-ai-results).

Route ID: [EPI-RTE-prompt-eval](#epi-rte-prompt-eval)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Content/update relation: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Transition or check target: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Evaluator/condition and domain: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Activation and timing: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Possible or observed result: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Implemented force: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Epistemic authority and scope: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Evidence source ID and local anchor: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Claim IDs or none: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Mismatch marker or none: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).
Gap/limit: see [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).

Route ID: [EPI-RTE-extract-facts](#epi-rte-extract-facts)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Content/update relation: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Transition or check target: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Evaluator/condition and domain: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Activation and timing: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Possible or observed result: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Implemented force: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Epistemic authority and scope: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Evidence source ID and local anchor: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Claim IDs or none: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Mismatch marker or none: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Gap/limit: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-extract-facts](#epi-rte-extract-facts)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Content/update relation: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Transition or check target: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Evaluator/condition and domain: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Activation and timing: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Possible or observed result: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Implemented force: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Epistemic authority and scope: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Evidence source ID and local anchor: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Claim IDs or none: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Mismatch marker or none: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
Gap/limit: see [EPI-RTE-extract-facts](#epi-rte-extract-facts).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Content/update relation: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Transition or check target: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Evaluator/condition and domain: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Activation and timing: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Possible or observed result: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Implemented force: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Epistemic authority and scope: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Evidence source ID and local anchor: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Claim IDs or none: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Mismatch marker or none: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Gap/limit: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Content/update relation: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Transition or check target: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Evaluator/condition and domain: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Activation and timing: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Possible or observed result: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Implemented force: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Epistemic authority and scope: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Evidence source ID and local anchor: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Claim IDs or none: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Mismatch marker or none: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
Gap/limit: see [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-query-answer](#epi-rte-query-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Content/update relation: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Transition or check target: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Evaluator/condition and domain: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Activation and timing: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Possible or observed result: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Implemented force: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Epistemic authority and scope: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Evidence source ID and local anchor: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Claim IDs or none: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Mismatch marker or none: see [EPI-RTE-query-answer](#epi-rte-query-answer).
Gap/limit: see [EPI-RTE-query-answer](#epi-rte-query-answer).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-lint-disposal](#epi-rte-lint-disposal)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Content/update relation: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Transition or check target: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Evaluator/condition and domain: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Activation and timing: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Possible or observed result: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Implemented force: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Epistemic authority and scope: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Evidence source ID and local anchor: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Claim IDs or none: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Mismatch marker or none: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
Gap/limit: see [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-task-admission](#epi-rte-task-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Content/update relation: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Transition or check target: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Evaluator/condition and domain: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Activation and timing: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Possible or observed result: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Implemented force: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Epistemic authority and scope: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Evidence source ID and local anchor: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Claim IDs or none: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Mismatch marker or none: see [EPI-RTE-task-admission](#epi-rte-task-admission).
Gap/limit: see [EPI-RTE-task-admission](#epi-rte-task-admission).
This entry isolates the named function from the linked implementation.

Route ID: [EPI-RTE-task-distill](#epi-rte-task-distill)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Content/update relation: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Transition or check target: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Evaluator/condition and domain: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Activation and timing: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Possible or observed result: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Implemented force: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Epistemic authority and scope: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Evidence source ID and local anchor: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Claim IDs or none: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Mismatch marker or none: see [EPI-RTE-task-distill](#epi-rte-task-distill).
Gap/limit: see [EPI-RTE-task-distill](#epi-rte-task-distill).
This entry isolates the named function from the linked implementation.

Route ID: [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Content/update relation: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Transition or check target: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Evaluator/condition and domain: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Activation and timing: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Possible or observed result: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Implemented force: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Epistemic authority and scope: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Evidence source ID and local anchor: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Claim IDs or none: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Mismatch marker or none: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Gap/limit: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

Route ID: [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Content/update relation: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Transition or check target: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Evaluator/condition and domain: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Activation and timing: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Possible or observed result: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Implemented force: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Epistemic authority and scope: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Evidence source ID and local anchor: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Claim IDs or none: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Mismatch marker or none: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Gap/limit: see [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

Route ID: [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Content/update relation: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Transition or check target: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Evaluator/condition and domain: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Activation and timing: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Possible or observed result: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Implemented force: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Epistemic authority and scope: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Evidence source ID and local anchor: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Claim IDs or none: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Mismatch marker or none: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Gap/limit: see [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

Route ID: [RT-RTE-saved-call](runtime.md#rt-rte-saved-call)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Content/update relation: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Transition or check target: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Evaluator/condition and domain: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Activation and timing: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Possible or observed result: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Implemented force: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Epistemic authority and scope: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Evidence source ID and local anchor: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Claim IDs or none: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Mismatch marker or none: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Gap/limit: see [RT-RTE-saved-call](runtime.md#rt-rte-saved-call).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

Route ID: [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Content/update relation: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Transition or check target: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Evaluator/condition and domain: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Activation and timing: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Possible or observed result: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Implemented force: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Epistemic authority and scope: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Evidence source ID and local anchor: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Claim IDs or none: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Mismatch marker or none: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Gap/limit: see [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

Route ID: [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Content/update relation: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Transition or check target: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Evaluator/condition and domain: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Activation and timing: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Possible or observed result: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Implemented force: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Epistemic authority and scope: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Evidence source ID and local anchor: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Claim IDs or none: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Mismatch marker or none: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Gap/limit: see [RT-RTE-plan-approval](runtime.md#rt-rte-plan-approval).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

Route ID: [RT-RTE-app-publication](runtime.md#rt-rte-app-publication)
Route function: retention
Architectural status: implemented
Object/candidate ID: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Content/update relation: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Transition or check target: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Evaluator/condition and domain: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Activation and timing: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Possible or observed result: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Implemented force: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Epistemic authority and scope: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Evidence source ID and local anchor: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Claim IDs or none: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Mismatch marker or none: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Gap/limit: see [RT-RTE-app-publication](runtime.md#rt-rte-app-publication).
Epistemic limit: authorization/software results are not semantic business-answer oracles or evidence of accepted ampliative content.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-verified-lookup](#epi-clm-verified-lookup) | see record | SRC-1 `internal/teammcp/server.go`, doctrine/design | see record | [EPI-RTE-query-answer](#epi-rte-query-answer) | none supplied | see record | see record | see record |
| [EPI-CLM-cited-knowledge](#epi-clm-cited-knowledge) | see record | SRC-1 `README.md`, doctrine/design | see record | [EPI-RTE-query-answer](#epi-rte-query-answer), [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet) | none supplied | see record | see record | see record |
| [RT-CLM-external-approval](runtime.md#rt-clm-external-approval) | see record | SRC-1 `README.md`, doctrine/design | see record | [RT-RTE-saved-call](runtime.md#rt-rte-saved-call), [RT-RTE-spec-replay](runtime.md#rt-rte-spec-replay), [RT-RTE-office-turn](runtime.md#rt-rte-office-turn) | none supplied | see record | see record | see record |

## Bounded conclusion

**Knowledge text can become consequential without semantic acceptance.** Artifact extraction, brief synthesis and learning append support candidate production/import and retention. Their software checks establish format, limited safety or bookkeeping, not source truth. The fact-to-brief and source-to-answer relations remain indeterminate without actual content and semantic checks. This neither proves hallucination nor warrants describing the transformations as accepted ampliative knowledge. Retention and use are not lifecycle integration after acceptance. See [EPI-RTE-extract-facts](#epi-rte-extract-facts), [EPI-RTE-synthesize-brief](#epi-rte-synthesize-brief), [EPI-RTE-learning-write](#epi-rte-learning-write).

**There are operative evaluators with distinct domains.** Task checks can block completion and produce a trusted learning, but file existence, command exit and HTTP status license only their named conditions. Copying a task title/details into a Verified outcome record does not make those narrative claims true, explain the successful process or validate its transfer. The task trace feeds a durable future-context path; no subsequent activation, capacity improvement or causal benefit is observed. See [EPI-RTE-task-check](#epi-rte-task-check), [EPI-RTE-task-admission](#epi-rte-task-admission), [EPI-RTE-task-distill](#epi-rte-task-distill), [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).

**Contradiction criticism has a consequential disposal route, not an oracle.** Model consistency judgments can lead callers to expire one fact or acknowledge both. The judgment does not authenticate either proposition. Acknowledgment suppresses later checks; expiry propagation into all retrieval, existing briefs and future prompts is not established. This positive criticism/disposition mechanism must not be erased by the lack of observed runs, nor inflated into evidence of a complete theory-builder. See [EPI-RTE-lint-judge](#epi-rte-lint-judge), [EPI-RTE-lint-disposal](#epi-rte-lint-disposal).

**Citation and cleanup guarantees are narrower than their labels.** Bounds filtering leaves answer prose unchanged even after dropped citations; Related cleanup leaves a prose-containing Related section intact. Source IDs and backlinks afford traceability, but do not check support. Packet clipping and omission of trust/evidence metadata can further reduce what the recipient can assess. See [EPI-RTE-query-answer](#epi-rte-query-answer), [EPI-RTE-related-cleanup](#epi-rte-related-cleanup), [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet).

**Procedural reuse and simulated checks have operational force without a truth verdict.** Compiled playbooks advise later agent behavior; saved tool code has executable force as described by [RT-BAP-tool-execution](runtime.md#rt-bap-tool-execution). Smoke testing checks selected failures in simulated capabilities, not correct business behavior, and routine persistence can admit fallback tools. AI score fallback can return a successful hash-derived value without model inference. Prompt golden cases supply a narrow reference comparison; no case results or production-enforcement consumer were supplied. See [EPI-RTE-playbook-compile](#epi-rte-playbook-compile), [RT-RTE-tool-authoring](runtime.md#rt-rte-tool-authoring), [RT-RTE-scheduled-tool](runtime.md#rt-rte-scheduled-tool), [EPI-RTE-ai-results](#epi-rte-ai-results), [EPI-RTE-prompt-eval](#epi-rte-prompt-eval).

These are independent route/property conclusions, not a single score. Provider parameter change remains uninspected. Autonomous execution, reflection, learning, theory-building and exercised self-improvement do not follow from storage or a retry. The inspected routes establish selected architecture and standing future-behavior paths, not successful improvement. Unassessed notebook review, app knowledge, alternate maintenance/evaluation paths and frontend consumers prevent system-wide negatives about acceptance or knowledge production. No supplied content establishes an accepted novel ampliative claim; this is a limit of the evidenced routes and instances, not proof that the whole shipped system cannot produce one.

## Shared records

### Operative objects

#### EPI-OBJ-typed-fact
Label: TypedFact

Source-native identity: artifact-derived Text/triplet, confidence, source path/excerpt, validity and relation metadata. Representational form and storage substrate: Natural-language assertions plus symbolic identity/provenance/validity fields; in-memory WikiIndex and persisted JSONL/ghost-brief substrate. Evidence: SRC-1 `internal/team/wiki_extractor.go`, implementation. Artifact claim fidelity is unchecked in the inspected extractor; initial source warrant unknown.

> Text:            f.Text,
> --- `internal/team/wiki_extractor.go`

#### EPI-OBJ-entity-brief
Label: Entity brief

Source-native identity: prior brief and model-updated entity narrative. Representational form and storage substrate: Natural-language Markdown body plus symbolic frontmatter/sentinels in wiki files under Git. Evidence: SRC-1 `internal/team/entity_synthesizer.go`, implementation. Claims can be truth-apt; no particular actual brief was supplied. No supplied runtime counterpart.

> newBody := applySynthesisFrontmatter(rewritten, headSHA, now, factCount, existingBrief)
> --- `internal/team/entity_synthesizer.go`

#### EPI-OBJ-query-answer
Label: QueryAnswer

Source-native identity: answer prose, source list, citation indices, confidence/coverage. Representational form and storage substrate: Natural-language answer plus symbolic JSON fields returned to caller; no retained-answer substrate established here. Evidence: SRC-1 `internal/team/wiki_query.go`, implementation. Reference index validity does not establish semantic support. No supplied runtime counterpart.

> Confidence:     parsed.Confidence,
> --- `internal/team/wiki_query.go`

#### EPI-OBJ-learning-record
Label: LearningRecord

Source-native identity: insight and source/confidence/trust/scope/evidence references. Representational form and storage substrate: Natural-language insight plus symbolic fields in wiki JSONL and regenerated Markdown index. Evidence: SRC-1 `internal/team/learnings.go`, implementation. Observation/policy distinction depends on actual insight. No supplied runtime counterpart; source labels alone do not establish lineage truth.

> rec.Trusted = trusted
> --- `internal/team/learnings.go`

#### EPI-OBJ-verification-result
Label: TaskVerificationResult

Source-native identity: Pass, Detail, kind and checked-at result. Representational form and storage substrate: Symbolic pass/kind/time with textual output detail, persisted in task state by broker. Evidence: SRC-1 `internal/team/task_verification.go`, implementation. Truth apt only over selected command/file/HTTP criterion. No supplied runtime counterpart; distinct from plan authorization.

> task.VerificationResult = &resCopy
> --- `internal/team/task_verification.go`

### Routes

#### EPI-RTE-extract-facts
Label: Artifact extraction to TypedFact

No counterpart after comparison with supplied runtime routes: this is the broker's artifact extraction path, not sidecar tool authoring. Endpoints: committed artifact path → provider prompt → JSON parse and sanitizer → entity/ID resolution → index submission and fact-log/ghost-brief persistence. Owner: Extractor and WikiWorker; model proposes fact text, triplets, confidence and excerpts. Code overwrites artifact SHA from the path, skips nil triplets and preserves prior supersede/contradiction arrays on reinforcement. Source warrant is unknown: lineage metadata is useful, but no inspected semantic comparison verifies that each extracted claim follows from its artifact. Extraction could be faithful reshaping, entailed derivation or unsupported addition; model use alone does not distinguish these.

Check target/domain: JSON shape and known unsafe strings in candidate fact text/triplets, not truth over the artifact's domain. Admission is software/model, with parse/sanitizer/index errors able to reject; no human per-fact veto is shown here. Trigger is the worker extractor hook, registered in SRC-1 `internal/team/broker_wiki_lifecycle.go`. Its exact firing schedule is not established by the registration search. Immediate index availability precedes successful disk persistence; persistence failure can enter DLQ without failing the already-committed artifact. This is retention/use without demonstrated evidence-consuming epistemic acceptance, not lifecycle integration after acceptance.

Content/update relation: truth-apt transformation: indeterminate. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/wiki_extractor.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Index submission, persistence attempts or validation/provider error.
- Later read-back: Fact logs/ghost briefs support reconstruction; query and synthesis paths consume retained knowledge, but full index reload is uninspected.
- Delegated visibility: Provider receives artifact body plus index context through the extraction prompt; full template not inspected.
- Selection predicate: ArtifactKind permits path; parsed sanitized rows with resolved subject and triplet proceed.
- Invalidation or expiry: Reinforcement preserves selected history; expiry/replay details uninspected.
- Activation or effect: Wired index/JSONL changes; actual claims and downstream use unobserved.
- Evidence limits: No source-to-claim entailment check established; exact artifact capture integrity and resolution logic remain unassessed.

> parsed.ArtifactSHA = sha
> --- `internal/team/wiki_extractor.go`

> return e.apply(ctx, parsed, artifactPath, kind)
> --- `internal/team/wiki_extractor.go`

> e.persistFactLogs(ctx, out.ArtifactSHA, factsToWrite)
> --- `internal/team/wiki_extractor.go`

> worker.SetExtractor(extractor)
> --- `internal/team/broker_wiki_lifecycle.go`

#### EPI-RTE-synthesize-brief
Label: Entity brief proposal and retention

No counterpart after comparison with runtime: this worker updates entity briefs, not executable tools. Endpoints: FactLog plus prior brief → model → trim/size/leakage checks → related cleanup/graph appendix → human-edit sentinel handling → WikiWorker replace under archivist. Owner: EntitySynthesizer, with model prose proposal and software admission. Target/domain of implemented checks: nonempty output, byte ceiling and two prompt-echo strings. These can reject malformed output but do not establish factual fidelity, contradiction completeness or source truth. Guidance explicitly forbids invented facts and requests contradiction callouts; that is natural-language guidance, not a semantic oracle. Count-based new-fact selection and stamped HEAD support bookkeeping, not endorsement. Manual or automatic synthesis modes and queue coalescing are declared in this file; only selected synthesis execution code was traced.

Content relation is indeterminate: intended aggregation may preserve claims, but inspected code cannot prove preservation or non-entailment of arbitrary returned prose. Source warrant is unknown. Result force is permissive admission to retained canonical prose; the retained prior brief also shapes later synthesis. The human-edit branch preserves the existing body and inserts learned content instead of replacing all of it. No acceptance decision naming evidence, intended use and criterion is established by these checks; this ledger keeps retention separate from lifecycle integration.

Content/update relation: truth-apt transformation: indeterminate. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/entity_synthesizer.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Enqueued rewritten brief and synthesized event, or size/empty/provider/write error.
- Later read-back: A subsequent synthesis reads the retained brief; downstream article consumption is only partly covered.
- Delegated visibility: Model gets escaped prior body and selected new facts, not raw full artifact history.
- Selection predicate: Fact count relative to prior synthesis selects newest facts; zero-new-fact conditions skip.
- Invalidation or expiry: Replacement/sentinel insertion and fact-count stamps; no automatic epistemic expiry established.
- Activation or effect: Can change canonical prose for later interpretation; no observed factual update or benefit.
- Evidence limits: Never-invent and contradiction guidance do not establish compliance; FactLog initial warrant and graph correctness are uninspected.

> output, llmErr := llm(callCtx, SynthesisPromptSystem, userPrompt)
> --- `internal/team/entity_synthesizer.go`

> Hard rules: Never invent facts. Mark contradictions explicitly with **Contradiction:** inline callouts rather than resolving them. Do not restate fact counts, file paths, or internal IDs as if they were content. Do not write a "## Related" section — that block is managed automatically from the cross-entity graph. Output ONLY the updated markdown, no explanation.`
> --- `internal/team/entity_synthesizer.go`

> if output == "" {
> 		return fmt.Errorf("llm output is empty")
> 	}
> --- `internal/team/entity_synthesizer.go`

> sha, _, werr := s.worker.Enqueue(ctx, ArchivistAuthor, relBrief, newBody, "replace", commitMsg)
> --- `internal/team/entity_synthesizer.go`

#### EPI-RTE-related-cleanup
Label: Related-section cleanup

No supplied runtime counterpart; this is a distinct deterministic suboperation of brief synthesis. Target/domain: recognizable managed Related blocks, not all prose under a Related heading. Owner/evaluator: stripRelatedSection's literal sentinel and Markdown-shape rules. A concrete deduction from implementation, without execution: input `Body\n\n## Related\n- Alice` has Related as last level-two heading and only bullet content after it; the function returns `Body`. In contrast, `Body\n\n## Related\nAlice is CEO.` has prose after the heading and returns unchanged. Thus the synthesis comment saying it strips any model-generated Related block is too broad. This is a local design-comment/implementation mismatch, not a needed runtime supersession. Cleanup deletes selected existing content, adds no truth proposition and certifies none; graph appending afterward is a separate acquisition path whose warrant remains unassessed. The surviving prose counterexample prevents claiming graph-only authority over every Related statement.

Content/update relation: truth-apt transformation: non-ampliative reshaping. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/entity_synthesizer.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned body or unchanged input.
- Later read-back: Output passes to synthesis retention; cleanup itself has no independent store.
- Delegated visibility: inapplicable — literal program processes body, not a delegated evaluator.
- Selection predicate: Sentinel pair, else last unfenced level-two Related heading followed only by bullet/blank lines.
- Invalidation or expiry: Only the current candidate body is modified.
- Activation or effect: Enforces deletion of matched segments before retained brief construction.
- Evidence limits: Concrete deduction covers specified inputs only; no claim of semantic validation or graph truth.

> if !(strings.HasPrefix(trimmed, "- ") || strings.HasPrefix(trimmed, "* ") || strings.HasPrefix(trimmed, "+ ")) {
> 			return body
> 		}
> --- `internal/team/entity_synthesizer.go`

#### EPI-RTE-query-answer
Label: Cited answer production and citation bounds

No supplied runtime counterpart. Endpoints: selected QuerySources → escaped prompt → provider response → parse → citation-index filter → QueryAnswer return. Owner: QueryHandler; model proposes answer, confidence, coverage and citation indices; code decides JSON acceptance and filters indices. Truth-apt object: factual answer over retrieved source scope. Its relation to those sources remains indeterminate, and source warrant is unknown. Check target/domain: integer membership in 1..len(sources), not whether a source entails the linked sentence. Empty citations are explicitly allowed. Concrete deduction: filterValidCitations([0, 1, 3], 2) returns clean [1], dropped [0, 3]; parsed AnswerMarkdown is still returned unchanged and Notes records the dropped indices. No target execution was needed.

The implemented force is field cleanup and return, not answer rejection when citations fail. Provider/parse errors instead produce a zero-confidence no-coverage response with sources. The claimed verified lookup is stronger than this check: no expected answer oracle or source-truth evaluator was found in this inspected synthesis path. This is not a system-wide finding about every wiki path.

Content/update relation: truth-apt transformation: indeterminate. Claim IDs: EPI-CLM-verified-lookup; EPI-CLM-cited-knowledge. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/wiki_query.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AnswerMarkdown, filtered SourcesCited, sources and model-reported confidence/coverage, or error explanation.
- Later read-back: inapplicable — inspected handler constructs a response and does not persist it.
- Delegated visibility: Provider gets escaped query and source excerpts, not independently authenticated facts.
- Selection predicate: Previously selected sources and valid JSON response; cited indices retained only within range.
- Invalidation or expiry: Request timeout; no persistent answer expiry in inspected segment.
- Activation or effect: Caller receives answer even if some citations were dropped; no semantic acceptance force.
- Evidence limits: Full retrieval and renderer paths uninspected; valid indices do not license source entailment.

> AnswerMarkdown: parsed.AnswerMarkdown,
> 		SourcesCited:   cleanCites,
> --- `internal/team/wiki_query.go`

> if c >= 1 && c <= sourceCount {
> 			clean = append(clean, c)
> 		} else {
> 			dropped = append(dropped, c)
> 		}
> --- `internal/team/wiki_query.go`

#### EPI-RTE-lint-judge
Label: Cluster contradiction judgment

No supplied runtime counterpart. Endpoints: indexed facts grouped by exact subject/predicate → provider judge → parsed contradicts/reason → critical finding with fact IDs and A/B/Both actions. Owner: Lint; model proposes semantic verdict; code selects clusters and admits JSON. Target/domain: currently-valid mutually-exclusive statements in a cluster, explicitly excluding paraphrase, specificity and temporal succession. Verdict is a truth-apt judgment about consistency, not proof that either statement is true. No independent oracle or observed accuracy is supplied. Acknowledged clusters are skipped when every member has any contradicts_with entry; code does not require each pair to be mutually acknowledged. Provider errors are logged and skipped, so no finding does not establish consistency. The finding advises resolution; it does not itself expire a fact.

Content/update relation: truth-apt transformation: indeterminate. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/wiki_lint.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Critical finding and action labels, or no finding/error skip.
- Later read-back: Findings feed resolution; full report persistence/UI path not independently traced.
- Delegated visibility: Judge receives cluster text, validity and source path, not underlying sources themselves.
- Selection predicate: At least two triplet facts sharing subject/predicate, unless all have contradiction metadata.
- Invalidation or expiry: Next lint can reevaluate; acknowledgment suppresses future cluster checks.
- Activation or effect: Advisory critical finding, no automatic truth selection.
- Evidence limits: Model consistency judgment has no supplied calibration; membership grouping misses other formulations.

> if allAcknowledged(cluster) {
> 				continue
> 			}
> --- `internal/team/wiki_lint.go`

> systemPrompt := "You are the WUPHF lint judge. Given a cluster of facts sharing (subject, predicate), determine if there is a real semantic contradiction. Read docs/specs/WIKI-SCHEMA.md §10.4 rules: temporal validity, specificity, and paraphrase are NOT contradictions. Real contradictions are currently-valid, mutually-exclusive claims."
> --- `internal/team/wiki_lint.go`

#### EPI-RTE-lint-disposal
Label: Contradiction disposal and expiry

No supplied runtime counterpart. Endpoints: resolve_contradiction tool/HTTP request → client-supplied contradiction finding and winner → fact-file mutation via WikiWorker. Owner: caller selects A, B or Both; broker validates operation shape; Lint mutates metadata. Domain: first two IDs of the supplied finding. The human-like identity is attribution, not evidence of independent human judgment: the registered MCP write tool can invoke this path, and the HTTP handler falls back to a synthetic human identity. No inspected check requires the supplied finding to equal a prior retained report.

A/B appends loser ID to winner Supersedes and stamps loser ValidUntil if nil. Both appends mutual ContradictsWith, leaving both valid. This is operational disposition of prior propositions, not an evidence-consuming acceptance against a truth criterion. The record changes warrant/validity metadata, not fact text. Force: enforcing metadata mutation, plus advisory acknowledgment semantics to the next lint. Scope of withdrawal is bounded: full index refresh, every query's expiry handling and already-written briefs were not traced, so it does not establish retraction everywhere. Sequential writes may partly succeed; no rollback was established.

Content/update relation: no content change. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/wiki_lint.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Queued fact metadata updates, success response/HEAD or error.
- Later read-back: Fact files retain metadata; lint uses acknowledgment fields, but complete reload/filter propagation is uninspected.
- Delegated visibility: Caller supplies finding IDs/type and choice; handler does not pass evidence to a fresh truth judge.
- Selection predicate: A/B/Both, contradictions type, two or more IDs and report date; first two IDs used.
- Invalidation or expiry: A/B marks expiry; Both marks acknowledgment; reversal/rollback uninspected.
- Activation or effect: Changes retained dispositions and can suppress lint checks; global withdrawal not established.
- Evidence limits: No observed human decision, source review or universal retrieval exclusion established.

> case "Both":
> 		return l.resolveBoth(ctx, finding.EntitySlug, idA, idB, identity)
> --- `internal/team/wiki_lint.go`

> f.Supersedes = append(f.Supersedes, loseID)
> --- `internal/team/wiki_lint.go`

> if f.ValidUntil == nil {
> 			t, _ := time.Parse(time.RFC3339, now)
> 			f.ValidUntil = &t
> 		}
> --- `internal/team/wiki_lint.go`

> Findings: []LintFinding{*req.Finding},
> --- `internal/team/broker_lint.go`

#### EPI-RTE-task-check
Label: Machine task checks

No supplied runtime counterpart: runtime's task durability mention is not this definition-of-done evaluator. Endpoints: TaskVerification kind/spec and task work directory → shell/filesystem/HTTP → Pass/Detail. Owner: runTaskVerification. Three independent targets/domains: command exit under a five-minute deadline; existence of a nonempty nondirectory file matching a glob; HTTP GET status in 2xx under a 15-second client timeout. Within their implementation/environment contracts, results report those narrow conditions. Warrant does not extend to semantic correctness of a file, substantive correctness of a web service or all requirements of the task. A command may contain a stronger test, but the command and its premises must be inspected separately. No actual verification spec or run outcome is supplied.

Possible counterexamples to broad success are direct from code: arbitrary nonempty wrong bytes meet the artifact criterion, and a 200 error page meets the URL criterion. These preserve the positive existence of operative testing while bounding its epistemic license. No expected business answer is built into these generic checks; external authors choose specs. Test selection authority/provenance for every task is uninspected.

Content/update relation: truth-apt transformation: entailed derivation. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/task_verification.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pass plus Detail and timestamp, including failure output or timeout.
- Later read-back: Result is stamped by task-admission route; later distillation consumes Pass.
- Delegated visibility: Shell sees spec and work directory; artifact probe sees matches; HTTP sees configured URL.
- Selection predicate: Kind selects evaluator; unsupported kind fails closed.
- Invalidation or expiry: Result describes check time, not future artifact content or service health.
- Activation or effect: Produces bounded environment evidence; actual operation unobserved.
- Evidence limits: Checked domain cannot certify title/details or process explanation; command test quality unassessed.

> if info, statErr := os.Stat(m); statErr == nil && !info.IsDir() && info.Size() > 0 {
> 				found = append(found, m)
> 			}
> --- `internal/team/task_verification.go`

> if resp.StatusCode < 200 || resp.StatusCode >= 300 {
> 			res.Detail = fmt.Sprintf("GET %s: HTTP %d", v.Spec, resp.StatusCode)
> 			return res
> 		}
> --- `internal/team/task_verification.go`

#### EPI-RTE-task-admission
Label: Task completion admission

No supplied runtime counterpart: distinct from plan-first authorization. Endpoints: completion/approval mutation → configured verification → persisted result → required-failure refusal or continued mutation. Owner: broker; checker computation provides result; spec author determines criterion, whose identity is uninspected. SRC-1 `internal/team/broker_tasks_mutation_service.go` calls the gate before mutation. No spec means this gate permits continuation; pre-execution approval is a start, not completion and bypasses the done check. Task worktree or owner scratch directory is used. A changed kind/spec on stamping refuses the stale result.

Acceptance scope is configured definition-of-done criterion for the task transition. Required false allows continuation on a failed check; required true blocks it. This licenses operational completion, not all narrative claims attached to the task. Evidence is consumed for a named operational criterion, but does not establish an accepted ampliative business claim or general mechanism. Rejection directs fixing the work and retrying. Persisted result is not a rollback of prior effects. Human approval in other task phases has separate authorization force.

Content/update relation: no content change. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/task_verification.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored verification result, refusal on required failure or continuation.
- Later read-back: Task record persists result; distillation subsequently tests Pass.
- Delegated visibility: Checker receives copied spec and resolved work directory; stale-spec test occurs at stamp.
- Selection predicate: Complete/approve with configured check and relevant lifecycle; Required determines refusal.
- Invalidation or expiry: New attempts replace result; exact freshness under concurrent artifact mutation unestablished.
- Activation or effect: Can block selected done transitions; no-spec/optional-check paths differ.
- Evidence limits: Other gates and every alternate mutation path uninspected; no universal task-success claim.

> if !res.Pass && v.Required {
> 		return taskMutationError(
> --- `internal/team/task_verification.go`

> if task == nil || task.Verification == nil {
> 		b.mu.Unlock()
> 		return nil
> 	}
> --- `internal/team/task_verification.go`

> if err := b.gateTaskCompletionVerification(body); err != nil {
> --- `internal/team/broker_tasks_mutation_service.go`

#### EPI-RTE-task-distill
Label: Verified task to trusted learning

No supplied runtime counterpart. Endpoints: non-system done task → entity facts/article regeneration → Pass gate → deterministic insight → AppendVerified → optional playbook draft. Owner: broker goroutine; software chooses capture and trust, without per-record human approval. Guidance is hardcoded string assembly and eligibility; no model interpretation is needed for the insight. Task title, a clipped details tail and clipped proof detail become natural-language content in JSONL, with task ID, Source execution, confidence 7 and Trusted true. Idempotency uses an in-flight task set and prior TaskID search. No theory of why the task succeeded or transferable rule is derived by this string formatting.

Crucial scope mismatch: the generated prefix Verified outcome labels the title, and unverified details are copied, although Pass may mean only nonempty artifact or HTTP 2xx. Retaining those claims does not expand the check's warrant. This transformation is classified as reshaping of supplied task text/result rather than a newly warranted generalization; added verification framing is only justified over the narrow check domain. Entity facts and article generation run before the Pass gate, so unverified done tasks can still produce retained factual content. Those subroutes remain unassessed beyond this call ordering. Successful learning admission can trigger a draft playbook; the full draft transformation is not established here. This is retention and downstream operational use, not evidence-consuming acceptance of every copied statement or lifecycle integration of an accepted general theory.

Content/update relation: truth-apt transformation: non-ampliative reshaping. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/task_distill.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Trusted learning append or skip/error; optional draft trigger after successful append.
- Later read-back: Learning search and context packet can supply the retained record on later tasks.
- Delegated visibility: No model in inspected insight assembly; input is copied task and result.
- Selection predicate: Non-system done task with Pass, active log and no existing matching TaskID.
- Invalidation or expiry: New task records accumulate; same-task dedup is not ongoing truth revalidation.
- Activation or effect: Software grants trusted metadata to recorded task text and enables downstream reuse.
- Evidence limits: Outcome does not certify narrative truth, causal explanation, repeatability or transfer. No activated learning/benefit evidence.

> insight := fmt.Sprintf("Verified outcome: %s.", strings.TrimSpace(task.Title))
> --- `internal/team/task_distill.go`

> res := task.VerificationResult
> 	if res == nil || !res.Pass {
> --- `internal/team/task_distill.go`

> if _, err := llog.AppendVerified(ctx, rec); err != nil {
> --- `internal/team/task_distill.go`

#### EPI-RTE-learning-write
Label: Learning admission and retention

No supplied runtime counterpart. Endpoints: caller LearningRecord → normalization and validation → UUID/time → JSONL plus human index via WikiWorker. Owner: LearningLog; external author supplies insight/source/confidence, software admits. Truth-apt observations and policy-like preferences are both allowed; classify each actual insight by content, not learning label. Source warrant is unknown. Target/domain: registered type/source values, key/scope/author/path shapes, length, confidence 1..10 and instruction-like text screening. No evidence-consuming truth check is implemented in the inspected append function. Ordinary Append sets trust from Source user-stated; it does not independently authenticate that the content was human-stated. AppendVerified grants trust to the separate broker capture route. The code's special trusted execution route is a counterexample to describing all trust as author assertion, but still does not validate arbitrary insight meaning.

Writes can reject invalid records or fail enqueue; the caller can propose another record. The persisted human index is regenerated from records; retention and readability are not epistemic acceptance or lifecycle integration. Search supports trust/source/scope filters and confidence/time sorting; full dedup/decay and supersession semantics remain uninspected.

Content/update relation: truth-apt transformation: acquisition/import. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/learnings.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Admitted record with generated ID/time, or validation/write error.
- Later read-back: Search reloads records and returns filtered/ranked results, including effective confidence.
- Delegated visibility: Record author supplies content and source label; software validates fields.
- Selection predicate: Valid enum/shape/safety/range and available worker.
- Invalidation or expiry: Supersedes metadata exists; complete dedup/expiry semantics uninspected.
- Activation or effect: Makes retained insight available to future search and packet interpretation.
- Evidence limits: Trust is not verified truth; author identity and source authenticity are not resolved by field validity.

> func (l *LearningLog) Append(ctx context.Context, rec LearningRecord) (LearningRecord, error) {
> 	return l.append(ctx, rec, rec.Source == LearningSourceUserStated)
> }
> --- `internal/team/learnings.go`

> if err := ValidateLearningInput(rec); err != nil {
> 		return LearningRecord{}, fmt.Errorf("%w: %w", ErrInvalidLearning, err)
> 	}
> --- `internal/team/learnings.go`

#### EPI-RTE-knowledge-packet
Label: Retrieved knowledge to task prompt

No supplied runtime record with this exact referent: RT-RTE-office-turn is a broader provider-execution container that mentions delivery; this record isolates the knowledge packet builder and its warrant-relevant omissions, not a duplicate turn. Endpoints: task title/details → configured search seams → selected learning insight/wiki snippets → packet and manifest. Owner: notificationContextBuilder and search implementations. Target/domain: matching knowledge to task; this builder is not a truth evaluator. It preserves learning ID and effective confidence in text, but omits the full source/trust/evidence fields of the learning result; wiki snippets are truncated to 400 characters with entity/fact reference. Thus the delivered packet is not complete provenance. Source warrant may be degraded by this omission and clipping even when the store holds more context.

Consumer path: office runner/model through work packet; force advisory natural-language apply-it/cite-it instruction, not guaranteed adherence; horizon current task invocation, with retained content reselectable for later tasks. Selection is query-dependent and externally supplied by search seams; searchWiki has a three-second deadline. Runtime supplies broader delivery wiring, not evidence of uptake. This is working-context selection rather than plain accumulation, with bounded entries and persistent store reachable through other tools; no window-reference/liveness guarantee is implied.

Content/update relation: truth-apt transformation: non-ampliative reshaping. Claim IDs: EPI-CLM-cited-knowledge. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/context_assembler.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Knowledge packet and ID manifest or empty packet.
- Later read-back: Later tasks can reselect retained knowledge; builder itself writes no memory.
- Delegated visibility: Model-visible text carries insight/snippet and ID, not full evidence/trust/source record.
- Selection predicate: Nonempty task query, configured search functions, nonempty snippets and route-specific limits.
- Invalidation or expiry: Each task gets a fresh packet; expiry depends on uninspected backing search semantics.
- Activation or effect: Can advise model reliance; actual behavioral uptake not observed.
- Evidence limits: No comprehensive provenance preservation or enforcement of citation compliance; wiring beyond runtime account uninspected.

> line := fmt.Sprintf("- [learning:%s confidence=%d] %s", rec.ID, rec.EffectiveConfidence, strings.TrimSpace(rec.Insight))
> --- `internal/team/context_assembler.go`

> header := "RELEVANT TEAM KNOWLEDGE (matched to this task — apply it; cite the learning/wiki id when you do):"
> --- `internal/team/context_assembler.go`

#### EPI-RTE-playbook-compile
Label: Playbook to invokable skill

No supplied runtime counterpart: this compiler emits natural-language guidance for future model/tool behavior, not a StoredTool JavaScript executable. Endpoints: wiki playbook source → deterministic skill wrapper → file/commit → skill registration. Owner: compiler and WikiWorker. Trigger: explicit queued compilation/current source; source edits can lead to recompile. The compiler validates repo/path/read/write, not task suitability or procedural correctness, and does not gate on draft frontmatter. A task-derived draft may therefore be compiled without human curation. Proposer of content may be human or software draft; code admission has no per-content human veto in this inspected segment. Recovery: errors propagate; previous compiled-byte rollback/revision consumers uninspected.

Consumer receives title/description and instructions to load canonical body, execute its steps, record outcome and optionally retain a compact lesson. This is advisory procedural authority through model interpretation, not symbolic enforcement that the model will follow each instruction. Source backlink is preserved, but converting a task example into a reusable procedure does not establish its general applicability. Skill registry registration is found in WikiWorker; actual later invocation and policy compilation are not traced. Claims that the complete core-loop learns, reflects or improves require independent evidence; this standing guidance path alone proves none of those outcomes.

Content/update relation: non-truth-apt policy/content update: generate procedural skill wrapper. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `internal/team/playbook_compiler.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Skill bytes/path, commit or I/O error.
- Later read-back: WikiWorker registers compiled bytes for later skill selection; actual selection/invocation unobserved.
- Delegated visibility: Later model receives wrapper and is instructed to fetch canonical source; full body not embedded.
- Selection predicate: Valid playbook path, readable source, successful write; no draft-status veto in inspected compiler.
- Invalidation or expiry: Source recompile replaces derived wrapper; stale invocation/registry invalidation uninspected.
- Activation or effect: Can change future agent guidance; no exercised behavior or improvement shown.
- Evidence limits: Full draft/generalization, policies and registration-to-invocation path not traced.

> source := string(sourceBytes)
> 
> 	skill := renderCompiledSkill(slug, wikiPath, source)
> --- `internal/team/playbook_compiler.go`

> b.WriteString("1. Call `team_wiki_read` with `article_path=\"" + sourcePath + "\"` to load the canonical playbook body.\n")
> --- `internal/team/playbook_compiler.go`

> reg.RegisterCompiledPlaybookSkill(slug, sourcePath, skillBytes)
> --- `internal/team/wiki_worker.go`

#### EPI-RTE-ai-results
Label: Runtime model capability results

Part of: [RT-RTE-saved-call](runtime.md#rt-rte-saved-call)

This is the material AI-result-producing subroute of saved capability dispatch, not another declaration of that whole executor. Same component: [RT-CMP-runtime-ai](runtime.md#rt-cmp-runtime-ai). Endpoints: subject/items/kind/context → fresh model request → score/summary/draft or deterministic fallback → generated tool caller. Owner: realAI and configured provider; model supplies text. Score criterion is caller rubric or fit over a business subject, normalized to integer 0..100; numerical parsing/clamping checks range, not empirical validity. Summary/draft can contain truth-apt assertions, but no particular actual input/output is supplied, so semantic relation is indeterminate, not automatically conjecture. Parameters/version and mutable resolution remain as runtime records report.

On model error, score returns hashScore without a provenance flag; summary/write return simulated text. Therefore successful capability return does not prove inference happened or the score measures the rubric. The generated tool may rank, display or write that result; exact consumer force depends on its unprovided code, so no specific downstream factual acceptance is established. The host does not perform evidence-consuming semantic acceptance here. Guidance is one fresh system/user context per call, not accumulated prior conversation.

Content/update relation: truth-apt transformation: indeterminate. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `agent/src/capabilities.ts`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Score, summary or draft; fallback can return ordinary successful value.
- Later read-back: inapplicable — this capability does not itself persist; calling tool may write/display result.
- Delegated visibility: Model gets a bounded subject/context and instructions; prior call conversation is not supplied.
- Selection predicate: Configured realAI overlay; score parse failure or provider exception selects fallback.
- Invalidation or expiry: Per-call/run signal and deadline; returned values have no implemented factual expiry.
- Activation or effect: Permits caller continuation with value, including hash fallback; particular ranking/writes not determinable without caller tool.
- Evidence limits: No observed results, rubric validation or consumer-specific trust policy.

> if (Number.isNaN(n)) throw new Error("non-numeric score");
> 				return Math.max(0, Math.min(100, n));
> 			} catch {
> 				return hashScore(subject);
> 			}
> --- `agent/src/capabilities.ts`

#### EPI-RTE-prompt-eval
Label: Golden prompt-case grading

No supplied runtime counterpart. Endpoints: case file/template vars/expected block → provider response → fence strip/parse → expected matchers → case result. Owner: runCase and case authors. Check target/domain: one response against the case's specified output properties, not arbitrary truth or operational task success. Human-authored expected block is a limited reference oracle; matcher's internal correctness was not inspected. Evaluator compares output strings/parsed shape to reference conditions; final pass is defined by empty failures under that implementation. The deduction licenses only that formal per-case condition, conditional on matcher/parser behavior, not source truth or general model quality. Trigger: developer harness invocation, not automatic admission of each production claim. Main reporting/exit integration uninspected; no production deployment gate or automatic policy update is established by runCase. No output or executed case results supplied.

Content/update relation: truth-apt transformation: entailed derivation. Claim IDs: none. Mismatch marker: see assessment above; none otherwise. Epistemic authority is limited to the expressly named target/domain; no additional license follows from operational continuation. Evidence: SRC-1 `cmd/eval-prompts/runner.go`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Per-case pass/fail, failures, elapsed time or setup/provider error.
- Later read-back: uninspected — report persistence and later consumers lie in untraced main/CI machinery.
- Delegated visibility: Provider gets rendered case prompt; matcher sees expected block and returned output.
- Selection predicate: Selected case/template and configured provider.
- Invalidation or expiry: One response per case; no longitudinal model-version guarantee.
- Activation or effect: Evidence-producing grading result; production-enforcement consumer not established.
- Evidence limits: No target execution, score dataset, matcher audit, generalization or causal component effect.

> mr := assertExpected(cleaned, parsed, ec.Expected)
> 	failures = append(failures, mr.failures...)
> --- `cmd/eval-prompts/runner.go`

> pass:     len(failures) == 0,
> --- `cmd/eval-prompts/runner.go`

### Claims

#### EPI-CLM-verified-lookup
Label: Verified sourced lookup

Claimed operation: wuphf_wiki_lookup supplies a verified, sourced answer with inline citations. No supplied runtime claim has this referent; [RT-CLM-external-approval](runtime.md#rt-clm-external-approval) concerns authorization instead. Evidence: SRC-1 `internal/teammcp/server.go`, doctrine/design.

> "Cited-answer lookup against the team wiki. Returns a structured JSON answer with sources and inline citations. Use when you need a verified, sourced answer rather than a raw search.",
> --- `internal/teammcp/server.go`

- claim conclusion status: claimed

Supported conclusion and mismatch: [EPI-RTE-query-answer](#epi-rte-query-answer) supplies source-bearing answers and filters out-of-range citation indices. It does not verify entailment, require nonempty citations or reject the answer text when invalid indices are dropped. The stronger semantic reading of verified is unsupported by this inspected path. Full lookup handler-to-renderer behavior remains uninspected, so this is not an assertion that no other check exists. No observed-run or causal support supplied.

#### EPI-CLM-cited-knowledge
Label: Every knowledge claim cited

Claimed operation: every knowledge claim carries a citation, within the README's Honest by default product promise. No supplied runtime counterpart; approval of external effects is a different claim. Evidence: SRC-1 `README.md`, doctrine/design.

> | **Honest by default** | No connected data → the app says "simulated" in plain text. Missing integration → it asks before building. Every knowledge claim carries a citation. |
> --- `README.md`

- claim conclusion status: claimed

Supported conclusion and mismatch: [EPI-RTE-query-answer](#epi-rte-query-answer) and [EPI-RTE-knowledge-packet](#epi-rte-knowledge-packet) implement source lists/IDs and citation guidance. An empty citation list is permitted by the bounds filter; it does not require every answer sentence to be cited. Packet delivery requests citations rather than enforcing them. Thus inspected architecture supports citation affordances, not the universal promise. Source-grounded task/playbook drafting offers additional attribution, but does not establish universal coverage or claim truth. Frontend/rendering and every producer remain unassessed; no observed uncited user-facing claim or causal reliability result is asserted.
