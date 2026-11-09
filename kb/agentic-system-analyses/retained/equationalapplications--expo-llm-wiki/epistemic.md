---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "expo-llm-wiki epistemic routes: extraction, grounding, reconciliation, withdrawal and benchmark reliance at the frozen revision."
run-id: AAS-2026-11-08-expo-llm-wiki-54f1fc1a0310-01
reviewed-boundary: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
---

# expo-llm-wiki epistemic report

## Source-and-claim boundary

The question is how conversation/document content becomes retained assertions, what checks license reliance, and how results affect later consumers. Scope, exclusions and SRC-1 are fixed by the [boundary and Source register](boundary.md#source-register). This overlay uses supplied runtime findings as provisional evidence and directly reads additional SRC-1 implementation. It does not execute the target. External provider internals and SynapseTree service behavior remain unavailable; they prevent conclusions about external semantic checking, mutable weights and production operation. Runtime model fixity limits remain in [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider), [RT-CMP-embed-provider](runtime.md#rt-cmp-embed-provider), [RT-CMP-answer-provider](runtime.md#rt-cmp-answer-provider) and [RT-CMP-judge-provider](runtime.md#rt-cmp-judge-provider), not inferred from memory changes.

The public memory claim is [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory); the configured grounding promise is [EPI-CLM-grounding-draft](#epi-clm-grounding-draft). Assessment separates import, candidate transformation, checking, disposition, retention and later consumption. No stored benchmark result is adopted here as an observed run or causal comparison.

| Entry point or operation | SRC-1 source path | Coverage and record |
|---|---|---|
| write / legacy librarian / document ingest | `packages/core/src/services/librarian/legacy.ts`; `packages/core/src/services/IngestionService.ts` | Supplied [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); direct prompt/shape/grounding utility inspection supplements, not an exhaustive branch audit. |
| ops extraction, gate, resolve, apply | `packages/core/src/services/librarian/ops/extract.ts`; `packages/core/src/services/librarian/ops/gate.ts`; `packages/core/src/services/librarian/ops/resolve.ts`; `packages/core/src/services/librarian/ops/apply.ts`; `packages/core/src/services/librarian/ops/text.ts` | Direct complete reads; [EPI-RTE-ops-classify](#epi-rte-ops-classify), [EPI-RTE-ops-disposition](#epi-rte-ops-disposition); refines [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian). |
| optional grounding | `packages/core/src/utils/grounding.ts`; `packages/core/src/prompts.ts` | Direct complete reads; [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-grounding-status](#epi-rte-grounding-status). |
| heal, pruning and forget | `packages/core/src/services/MaintenanceService.ts` | Direct heal orchestration/application excerpts; [EPI-RTE-heal-assess](#epi-rte-heal-assess), [EPI-RTE-heal-dispose](#epi-rte-heal-dispose). Prune/forget only searched signatures and supplied runtime recovery affordance: full retention-policy and deletion-hook implementations unassessed; prevents all-cleanup guarantees. |
| supersede/history, remember, trust/promotion | `packages/core/src/services/TemporalService.ts`; `packages/core/src/services/RememberService.ts`; `packages/core/src/WikiMemory.ts`; `packages/core/src/db/okf-trust-writes.ts` | Direct full TemporalService/RememberService, public trust/promotion and fact trust DAO excerpts; supplied [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission); metadata can be caller-written, no authenticated truth-review gate established. |
| read, packing, graph and import | `packages/core/src/services/RetrievalService.ts`; `packages/core/src/utils/budget.ts`; `crates/graphrag-core/src/engine.rs`; `packages/core/src/services/ImportExportService.ts` | Supplied [RT-RTE-memory-read](runtime.md#rt-rte-memory-read), [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal), [RT-RTE-import-admission](runtime.md#rt-rte-import-admission); direct read-options excerpt confirms opt-in draft exclusion. Import conversion/native internals not directly audited; no global preservation or parity conclusion. |
| lint, ontology/classifier backfill | `packages/core/src/services/LintService.ts`; `packages/core/src/services/MaintenanceService.ts`; `packages/core/src/prompts.ts` | Full lint and backfill prompt directly read; lint returns health/manifest counts read-only, with no inspected disposition consumer. Backfill implementation unassessed; prevents complete classification/graph-warrant conclusion. |
| ScopeLab / WikiDemo / hooks / outbox | `apps/scopelab/src/lib/llm/function-caller.ts`; `apps/wiki-demo/src/App.tsx`; `packages/prisma-outbox/src/PrismaOutboxWorker.ts` | Supplied [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat), [RT-BAP-memory-context](runtime.md#rt-bap-memory-context), [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync); direct heal excerpt traces embedding-persisted notification with caught hook errors. Hook implementations belong to host callbacks; no exactly-once or semantic-veto guarantee. React/UI paths otherwise rely on supplied findings, not exhaustive direct inspection. |
| benchmark answer/judge | `packages/benchmarks/src/longmemeval/run.ts`; `packages/benchmarks/src/longmemeval/judge.ts` | Supplied [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer); direct full judge source, [EPI-RTE-judge-check](#epi-rte-judge-check), [EPI-RTE-judge-record](#epi-rte-judge-record). Result aggregates, calibration artifacts, integration evaluators remain unassessed; no accuracy or causal benefit claim. |
| MCP CLI / registered operations | `packages/mcp-server/src/cli.ts`; `packages/mcp-server/src/commands.ts`; `packages/mcp-server/src/tools/index.ts`; `packages/mcp-server/src/tools/memory-remember.ts`; `packages/mcp-server/src/tools/memory-supersede.ts` | Direct full dispatch and tool enumeration plus remember/supersede: serve/auth/status/config/help/version, and eight registered tools including search/remember/supersede/ingest/log-event/graph/namespaces/whoami. Supplied [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools) covers server/client/search. Direct writes forward sourceType user_stated even when caller identity is unresolved; remote semantics uninspected. Other handlers not directly audited. |

Relevant unassessed operations above prevent a system-complete negative about acceptance, theory-building, evaluation or cleanup. They are available but uninspected, not access gaps or evidenced absences. The positive routes below stand independently. No supplied runtime fact needs supersession: its ops/oracle internals were explicitly left open.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-fact-text](#epi-obj-fact-text) | see [EPI-OBJ-fact-text](#epi-obj-fact-text) | Fact title and body | SRC-1, `packages/core/src/utils/pure.ts` | see [EPI-OBJ-fact-text](#epi-obj-fact-text) |
| [EPI-OBJ-task-description](#epi-obj-task-description) | see [EPI-OBJ-task-description](#epi-obj-task-description) | Task description | SRC-1, `packages/core/src/utils/pure.ts` | see [EPI-OBJ-task-description](#epi-obj-task-description) |
| [EPI-OBJ-grounding-trust](#epi-obj-grounding-trust) | see [EPI-OBJ-grounding-trust](#epi-obj-grounding-trust) | Grounding and lifecycle metadata | SRC-1, `packages/core/src/utils/grounding.ts` | see [EPI-OBJ-grounding-trust](#epi-obj-grounding-trust) |
| [EPI-OBJ-judge-verdict](#epi-obj-judge-verdict) | see [EPI-OBJ-judge-verdict](#epi-obj-judge-verdict) | Judge reply and correctness | SRC-1, `packages/benchmarks/src/longmemeval/judge.ts` | see [EPI-OBJ-judge-verdict](#epi-obj-judge-verdict) |

Events and document chunks are imported evidence inputs, not newly warranted truths: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian) and [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest). Graph edges and ontology classifications can express truth-apt relations or non-truth-apt organizational choices depending on content; exact content and full checking are not determinable from supplied traversal/container findings alone. Imported dumps preserve supplied candidates, not demonstrated acceptance: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission). Numerical embeddings and distributed provider state are distinct from text; see [RT-CMP-embed-provider](runtime.md#rt-cmp-embed-provider) and [RT-CMP-llm-provider](runtime.md#rt-cmp-llm-provider). Their model-internal truth-apt content is not determinable from these interfaces. These opaque/unassessed parts are not merged into the four assessed operative objects.

## Authority-route ledger

Route ID: [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact-text](#epi-obj-fact-text)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Evaluator/condition and domain: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Activation and timing: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Possible or observed result: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Implemented force: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Epistemic authority and scope: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)
Evidence source ID and local anchor: SRC-1, `packages/core/src/utils/grounding.ts`
Claim IDs or none: [EPI-CLM-grounding-draft](#epi-clm-grounding-draft)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-grounding-check](#epi-rte-grounding-check)

Route ID: [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-grounding-trust](#epi-obj-grounding-trust)
Content/update relation: non-truth-apt policy/content update: lifecycle and verification metadata
Transition or check target: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Evaluator/condition and domain: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Activation and timing: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Possible or observed result: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Implemented force: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Epistemic authority and scope: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)
Evidence source ID and local anchor: SRC-1, `packages/core/src/utils/grounding.ts`
Claim IDs or none: [EPI-CLM-grounding-draft](#epi-clm-grounding-draft)
Mismatch marker or none: draft status is not default retrieval exclusion
Gap/limit: see [EPI-RTE-grounding-status](#epi-rte-grounding-status)

Route ID: [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact-text](#epi-obj-fact-text)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Evaluator/condition and domain: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Activation and timing: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Possible or observed result: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Implemented force: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Epistemic authority and scope: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)
Evidence source ID and local anchor: SRC-1, `packages/core/src/services/librarian/ops/gate.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-ops-classify](#epi-rte-ops-classify)

Route ID: [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact-text](#epi-obj-fact-text)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Evaluator/condition and domain: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Activation and timing: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Possible or observed result: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Implemented force: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Epistemic authority and scope: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)
Evidence source ID and local anchor: SRC-1, `packages/core/src/services/librarian/ops/apply.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-ops-disposition](#epi-rte-ops-disposition)

Route ID: [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact-text](#epi-obj-fact-text)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Evaluator/condition and domain: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Activation and timing: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Possible or observed result: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Implemented force: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Epistemic authority and scope: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)
Evidence source ID and local anchor: SRC-1, `packages/core/src/prompts.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-heal-assess](#epi-rte-heal-assess)

Route ID: [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact-text](#epi-obj-fact-text)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Evaluator/condition and domain: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Activation and timing: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Possible or observed result: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Implemented force: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Epistemic authority and scope: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)
Evidence source ID and local anchor: SRC-1, `packages/core/src/services/MaintenanceService.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-heal-dispose](#epi-rte-heal-dispose)

Route ID: [EPI-RTE-judge-check](#epi-rte-judge-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judge-verdict](#epi-obj-judge-verdict)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Evaluator/condition and domain: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Activation and timing: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Possible or observed result: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Implemented force: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Epistemic authority and scope: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-judge-check](#epi-rte-judge-check)
Evidence source ID and local anchor: SRC-1, `packages/benchmarks/src/longmemeval/judge.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-judge-check](#epi-rte-judge-check)

Route ID: [EPI-RTE-judge-record](#epi-rte-judge-record)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judge-verdict](#epi-obj-judge-verdict)
Content/update relation: non-truth-apt policy/content update: benchmark correctness Boolean
Transition or check target: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Evaluator/condition and domain: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Activation and timing: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Possible or observed result: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Implemented force: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Epistemic authority and scope: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-judge-record](#epi-rte-judge-record)
Evidence source ID and local anchor: SRC-1, `packages/benchmarks/src/longmemeval/judge.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-judge-record](#epi-rte-judge-record)

Route ID: [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Route function: content transformation
Architectural status: implemented
Content/update relation: truth-apt transformation: indeterminate
Object/candidate ID: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Transition or check target: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Evaluator/condition and domain: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Activation and timing: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Possible or observed result: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Implemented force: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Epistemic authority and scope: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Evidence source ID and local anchor: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: content transformation
Architectural status: implemented
Content/update relation: truth-apt transformation: indeterminate
Object/candidate ID: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Transition or check target: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Evaluator/condition and domain: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Implemented force: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Epistemic authority and scope: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)

Route ID: [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Route function: content transformation
Architectural status: implemented
Content/update relation: truth-apt transformation: acquisition/import
Object/candidate ID: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Transition or check target: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Evaluator/condition and domain: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Activation and timing: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Possible or observed result: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Implemented force: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Epistemic authority and scope: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Evidence source ID and local anchor: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission)

Route ID: [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Route function: retention
Architectural status: implemented
Content/update relation: truth-apt transformation: acquisition/import
Object/candidate ID: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Transition or check target: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Evaluator/condition and domain: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Activation and timing: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Possible or observed result: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Implemented force: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Epistemic authority and scope: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Evidence source ID and local anchor: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-import-admission](runtime.md#rt-rte-import-admission)

Route ID: [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Route function: retention
Architectural status: implemented
Content/update relation: no content change
Object/candidate ID: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Transition or check target: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Evaluator/condition and domain: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Activation and timing: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Possible or observed result: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Implemented force: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Epistemic authority and scope: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Evidence source ID and local anchor: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian)

Route ID: [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Route function: retention
Architectural status: implemented
Content/update relation: no content change
Object/candidate ID: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Transition or check target: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Evaluator/condition and domain: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Activation and timing: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Possible or observed result: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Implemented force: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Epistemic authority and scope: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Evidence source ID and local anchor: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)

Route ID: [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Route function: operational admission/selection/consumption
Architectural status: implemented
Content/update relation: truth-apt transformation: non-ampliative reshaping
Object/candidate ID: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Transition or check target: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Evaluator/condition and domain: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Activation and timing: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Possible or observed result: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Implemented force: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Epistemic authority and scope: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Evidence source ID and local anchor: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read)

Route ID: [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Route function: operational admission/selection/consumption
Architectural status: implemented
Content/update relation: no content change
Object/candidate ID: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Transition or check target: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Evaluator/condition and domain: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Activation and timing: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Possible or observed result: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Implemented force: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Epistemic authority and scope: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Evidence source ID and local anchor: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-scopelab-chat](runtime.md#rt-rte-scopelab-chat)

Route ID: [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Route function: operational admission/selection/consumption
Architectural status: implemented
Content/update relation: truth-apt transformation: non-ampliative reshaping
Object/candidate ID: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Transition or check target: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Evaluator/condition and domain: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Activation and timing: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Possible or observed result: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Implemented force: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Epistemic authority and scope: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Evidence source ID and local anchor: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-native-traversal](runtime.md#rt-rte-native-traversal)

Route ID: [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Route function: other — remote API delegation
Architectural status: implemented
Content/update relation: truth-apt transformation: acquisition/import
Object/candidate ID: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Transition or check target: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Evaluator/condition and domain: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Activation and timing: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Possible or observed result: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Implemented force: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Epistemic authority and scope: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Evidence source ID and local anchor: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools)

Route ID: [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Route function: lineage/freshness/recovery
Architectural status: implemented
Content/update relation: no content change
Object/candidate ID: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Transition or check target: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Evaluator/condition and domain: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Activation and timing: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Possible or observed result: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Implemented force: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Epistemic authority and scope: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Operational authority: behavior permitted, blocked, or changed: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Behavioral-authority path: consumer, channel, force, horizon: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Evidence source ID and local anchor: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)
Claim IDs or none: [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory)
Mismatch marker or none: none
Gap/limit: see [RT-RTE-outbox-sync](runtime.md#rt-rte-outbox-sync)

The acquisition/import rows preserve caller-provided content only to the limits of the cited conversion/transport route; source warrant is unknown. Generated extraction text is indeterminate between faithful reshaping, derivation and conjecture: instructions and valid JSON do not establish semantic preservation or non-entailment. Read/graph selection reshapes which assertions are delivered, not their external truth. No lifecycle-integration row is asserted: these inspected routes establish retention and operational use, not semantic acceptance followed by evidence-linked integration.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory) | see cited record | SRC-1, `README.md`, doctrine/design | see cited record | [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-memory-read](runtime.md#rt-rte-memory-read), [EPI-RTE-heal-dispose](#epi-rte-heal-dispose) | Uninspected; no adopted trace | No comparison adopted | Mechanisms for extraction, persistence, retrieval and pruning; not a truth guarantee | Long-term reliability and answer improvement unestablished |
| [EPI-CLM-grounding-draft](#epi-clm-grounding-draft) | see cited record | SRC-1, `packages/core/src/prompts.ts`, doctrine/design | see cited record | [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-grounding-status](#epi-rte-grounding-status) | Uninspected | Deterministic implementation deduction only | Quote occurrence controls insert metadata when configured | Does not check claim entailment; draft reads are included by default; ops UPDATE bypasses insert check |

## Bounded conclusion

- **Acquisition and retention are implemented, but source truth is not inherited automatically.** [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission) and [RT-RTE-import-admission](runtime.md#rt-rte-import-admission) admit caller content with unknown upstream warrant. [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) can retain partial success without replacing the old source state. [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian) retains model-produced text after shape checks. Calling these rows facts, certain, or user_stated is not an external truth criterion.
- **Checks have different licenses.** [EPI-RTE-grounding-check](#epi-rte-grounding-check) establishes normalized source occurrence, not quotation relevance or entailment. [EPI-RTE-ops-classify](#epi-rte-ops-classify) establishes routing and local alias scope, not correctness of a change in the world. [EPI-RTE-judge-check](#epi-rte-judge-check) compares a generated answer to a supplied reference/rubric with type-specific tolerances; [EPI-RTE-judge-record](#epi-rte-judge-record) makes that judgment consequential only for benchmark correctness.
- **Disposition is consequential without semantic acceptance.** [EPI-RTE-ops-disposition](#epi-rte-ops-disposition) can admit the candidate after rejecting its operation and can retain a new row after rejected supersession linkage. [EPI-RTE-heal-dispose](#epi-rte-heal-dispose) can downgrade/withdraw existing content and insert new candidates. These are operational changes, not merely advisory reports. Their later consumers are search, retrieval and maintenance via persisted rows and indexes. [EPI-RTE-grounding-status](#epi-rte-grounding-status) is a genuine criterion-based status decision for textual grounding, with optional future draft filtering, not acceptance of produced ampliative knowledge.
- **Metadata review and source correction are host-controlled.** [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission) and the directly read SRC-1 `packages/core/src/WikiMemory.ts` promotion/trust methods afford lifecycle/trust changes. A nonempty reviewer string and a live draft suffice for promotion; no supplied evidence shows a content-review decision, authenticated human identity or independently named truth criterion. The fact trust DAO does not push an outbox event, so external sync does not learn new verification through this metadata-only path. See [EPI-OBJ-grounding-trust](#epi-obj-grounding-trust).
- **Later use is wired, not demonstrated compliance or benefit.** [RT-RTE-memory-read](runtime.md#rt-rte-memory-read) selects/reshapes retained text; [RT-BAP-memory-context](runtime.md#rt-bap-memory-context) supplies advisory natural-language context to ScopeLab, subject to its provider/persistence limits. [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer) gives an independent answer consumer with a reference judge, not a production acceptance gate. [RT-RTE-remote-tools](runtime.md#rt-rte-remote-tools) delegates authority to unavailable remote implementation; local-engine checking cannot be attributed to it.
- **Generation, learning and adaptation remain separate.** Candidate assertions and model reconciliation are wired; no particular output establishes warranted entailed derivation, a non-entailed conjecture followed by semantic acceptance, or lifecycle integration after such acceptance. Heal's schema need not retain content-directed criticism/blame, so a theory-builder iteration is not established by the word heal. Retained updates can shape later input, but no supplied causal comparison establishes improved future capacity or exercised self-improvement. The unassessed paths listed above prevent converting these local limits into system-wide absences. Provider-internal reflection/learning is uninspected independently of the positive local retention/withdrawal capacities.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-fact-text
Label: Fact title and body

Natural-language truth-apt assertions, stored as SQLite text with symbolic confidence/source/lifecycle metadata. Candidate output and persisted text differ when clipping or resolver overrides occur. Distinct from tasks, numerical vectors and trust metadata; no runtime object counterpart is declared. Producers and consumers: see [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian), [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest), [RT-RTE-direct-admission](runtime.md#rt-rte-direct-admission). Source warrant is unknown, not established by source_type or confidence.

SRC-1, `packages/core/src/utils/pure.ts` (implementation).

> if (typeof fact?.title !== 'string' || typeof fact?.body !== 'string') return null;
> --- `packages/core/src/utils/pure.ts`

#### EPI-OBJ-task-description
Label: Task description

Natural-language prospective instruction stored in SQLite with symbolic priority/status. A task can embed factual premises, but its action request is not itself a truth assertion. Distinct operative part of the bundles written by [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian) and [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest); no supplied object counterpart. Later consumers: see [RT-RTE-memory-read](runtime.md#rt-rte-memory-read).

SRC-1, `packages/core/src/utils/pure.ts` (implementation).

> priority = Math.max(0, Math.min(10, Math.round(priority)));
> --- `packages/core/src/utils/pure.ts`

#### EPI-OBJ-grounding-trust
Label: Grounding and lifecycle metadata

Symbolic SQLite lifecycle_status, verification actor/time and verification JSON; not the fact's truth. Distinct from fact text and numerical model state; no runtime object counterpart. Grounding maps matching evidence to stable status, failed/missing evidence to draft. Generic metadata writes and promotion can also change it; source attribution is caller-writable.

SRC-1, `packages/core/src/utils/grounding.ts` (implementation).

> trust: { lifecycle_status: 'draft' },
> --- `packages/core/src/utils/grounding.ts`

#### EPI-OBJ-judge-verdict
Label: Judge reply and correctness

Natural-language judge response converted to a symbolic Boolean in the benchmark result object. It assesses an answer, not individual stored facts. Distinct from core fact admission and from [RT-CMP-judge-provider](runtime.md#rt-cmp-judge-provider) (producer component); no supplied object counterpart.

SRC-1, `packages/benchmarks/src/longmemeval/judge.ts` (implementation).

> return text.trim().toLowerCase().startsWith('yes');
> --- `packages/benchmarks/src/longmemeval/judge.ts`

For [EPI-OBJ-grounding-trust](#epi-obj-grounding-trust), additional implementation evidence: SRC-1, `packages/core/src/WikiMemory.ts` and `packages/core/src/db/okf-trust-writes.ts`. The trust DAO's metadata-only writes do not enqueue content sync; exact human authenticity and actual review remain unresolved.

> await this.okfTrustWrites.setLifecycleStatus(entryId, entityId, 'stable', tx);
> --- `packages/core/src/WikiMemory.ts`

> * Deliberately does NOT push an outbox event, unlike `EntryRepository.upsert`
> --- `packages/core/src/db/okf-trust-writes.ts`

### Routes

#### EPI-RTE-grounding-check
Label: Evidence substring check

Distinct check inside the writing routes [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and [RT-RTE-event-librarian](runtime.md#rt-rte-event-librarian); overlaps heal below, not a replacement for their container identities.

Check target / transition: Evidence strings against the normalized source corpus shown to the writer; not proposition truth or entailment.

Owner: deterministic checkGrounding. When mode is draft and the writer is enabled (default writers: ingest), NFKC/whitespace-normalized quotes of qualifying length must each occur inside one corpus part. Empty/short evidence is missing; excessive count or an unmatched qualifying quote fails. It never compares a fact's title/body meaning to its quotes. Concrete implementation deduction: with minEvidenceChars=20, evidence ['The user lives in Paris.'] and corpus ['The user lives in Paris.'], a candidate body 'The user lives in Rome.' still gets grounded: body is not an input to checkGrounding. This is not target execution or an observed mistake. License: normalized textual occurrence only.

- Immediate return: Grounded/missing/failed verdict plus retained quote strings.
- Later read-back: inapplicable — the checker returns a current-call verdict; its disposition is a separate route.
- Delegated visibility: inapplicable — program check, no model delegation.
- Selection predicate: Configured writer and evidence length/count/substring predicates.
- Invalidation or expiry: inapplicable — verdict applies to that input/corpus, not a standing endorsement.
- Activation or effect: Verdict consumed by groundingOutcome during inserts; no changed model behavior observed.
- Evidence limits: Implementation deduction only; source truth, quotation relevance, and semantic entailment remain unchecked.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/utils/grounding.ts` (implementation).

> if (qualifying.some((q) => !normalizedCorpus.some((part) => part.includes(q)))) {
> --- `packages/core/src/utils/grounding.ts`

#### EPI-RTE-grounding-status
Label: Grounding lifecycle disposition

Distinct identity and comparison: no supplied route separately individuates this function; related supplied admission routes remain valid containers.

Check target / transition: Insert-time stable/draft status for configured generated facts.

Owner: groundingOutcome and writer insert code. A grounded verdict sets stable and process:grounding-check verification; missing/failed evidence sets draft and emits a diagnostic. This is an evidence-consuming acceptance decision for textual-grounding status, not acceptance of an ampliative assertion as true. Operational force: writers retain even failing candidates as drafts; RetrievalService defaults excludeDrafts to false, so draft status alone is not a quarantine. Consumer/channel/horizon: SQLite metadata consumed by later reads' optional draft filter and exposed trust fields. Ops failed-resolution and immutable-document contradiction branches can override grounded status to draft. Distinct disposition from the preceding check; spans the ingest/legacy/ops/heal insert paths, rather than replacing a runtime container.

- Immediate return: Trust fields and optional diagnostic, then insert persistence.
- Later read-back: Lifecycle/trust fields on retained rows reach later read/filter and draft-list consumers.
- Delegated visibility: inapplicable — metadata disposition uses code, not another provider call.
- Selection predicate: Configured writer plus grounding verdict, with ops draft overrides.
- Invalidation or expiry: Host lifecycle/trust writes or promoteDraft can change metadata; not automatic semantic revocation.
- Activation or effect: Stable or draft row; exclusion requires an explicit read/config flag.
- Evidence limits: Grounded metadata is no proof of proposition truth. UPDATE of an existing librarian row in ops does not run insert's check again.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/utils/grounding.ts` (implementation).

> last_verified_by: GROUNDING_VERIFIER,
> --- `packages/core/src/utils/grounding.ts`

#### EPI-RTE-ops-classify
Label: Ops neighbor classification

Part of: [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian)

Distinct identity and comparison: this is a material function within the cited runtime container; checking and disposition have different results and consumers.

Check target / transition: Candidate redundancy/novelty relative to selected live neighbors, not external factual truth.

Owner: classifyCandidate and optional resolver model. Exact normalized equality produces noop; absent neighbors add; vector similarity plus qualifying title overlap can noop, low similarity adds, otherwise ambiguous; keyword neighbors are always ambiguous. Only ambiguous items reach the resolver, whose prompt requests ADD/UPDATE/SUPERSEDE/NOOP. validateOp checks operation schema and per-candidate aliases, not whether a proposed supersession is true. Guidance: OPS_RESOLVE_SYSTEM_PROMPT. Computational proposals/decisions dominate; no human veto or expected-answer oracle in this maintenance mode. Natural-language neighbor bodies are limited to 400 characters. Similarity and constrained aliases license routing/local target scope only. Countercase to universal model reconciliation: no-neighbor and exact-duplicate candidates bypass resolution.

- Immediate return: Gate decisions; validated resolver operations or rejected/failed candidates.
- Later read-back: inapplicable — current-pass decisions go directly to applyOps; retained effects are separate.
- Delegated visibility: Resolver sees candidate text and clipped selected neighbors, not full history.
- Selection predicate: Live top-k vector or keyword neighbors; ambiguous only for model call.
- Invalidation or expiry: Pass can abort on transient resolver call errors; budget stop avoids application.
- Activation or effect: ApplyOps consumes gate and resolve outcomes to choose mutations.
- Evidence limits: No observed semantic classification accuracy; calibration comments are reported design rationale, not adopted run evidence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/librarian/ops/gate.ts` (implementation).

> if (same) return { kind: 'noop', target: same.id };
> --- `packages/core/src/services/librarian/ops/gate.ts`

#### EPI-RTE-ops-disposition
Label: Ops mutation disposition

Part of: [RT-RTE-ops-librarian](runtime.md#rt-rte-ops-librarian)

Distinct identity and comparison: this is a material function within the cited runtime container; checking and disposition have different results and consumers.

Check target / transition: Insert/update/noop/supersession choice and retention eligibility of extracted candidates.

Owner: applyOps. Noop writes nothing; add inserts; failed resolution inserts a draft; rejected/missing op inserts a non-forced-draft candidate with diagnostic. Thus rejection of the operation is not rejection of the fact. UPDATE on librarian_inferred rewrites existing text; other UPDATEs become supersession. Immutable-document targets cause a new draft rather than source replacement. SUPERSEDE inserts the new row then calls temporal validation; WikiSupersedeError is caught with diagnostic, so the new candidate may remain even without successful linkage. DB/non-supersession errors abort transaction. TemporalService checks entity, live replacement, immutability and cycles; these do not check truth. Guidance: model reconciliation instructions plus symbolic branch policy. Mode: ongoing event maintenance; no expected-answer oracle or mandatory human content veto. Consumer/channel/force/horizon: database mutation changes later retrieval and neighbor inputs, enforcing current-state choice. Recovery: explicit forget/supersede/history APIs. No source-supported particular output establishes entailment or non-entailment; remaining possibilities include preserved extraction, derived content and conjecture.

- Immediate return: Written/updated IDs and diagnostics after transaction.
- Later read-back: Mutated facts enter later retrieval/neighbor queries; temporal linkage can withdraw old current-state visibility.
- Delegated visibility: inapplicable — disposition runs code over gate/resolver results.
- Selection predicate: Gate decision, failed/rejected sets, validated op, target source_type and temporal constraints.
- Invalidation or expiry: Explicit later replacement/deletion; transaction rollback on uncaught failure.
- Activation or effect: Operational admission/revision without an external truth acceptance criterion.
- Evidence limits: UPDATE rewrites text without insert-time grounding, and sourceLabel from extraction can be null; not a fully grounded per-event lineage guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/librarian/ops/apply.ts` (implementation).

> if (rejected.has(g) || !op) {
>         await insert(g, false, vf);
> --- `packages/core/src/services/librarian/ops/apply.ts`

#### EPI-RTE-heal-assess
Label: Heal model assessment

Distinct identity and comparison: no supplied route separately individuates this function; related supplied admission routes remain valid containers.

Check target / transition: Contradictions, stale/obsolete mutable fact candidates relative to supplied recent events/document anchors.

Owner: supplied core provider. MaintenanceService batches eligible facts, constructs bounded prompts with recent events, tasks and selected document anchors, and parses downgraded/deleted/newFacts arrays. Doctrine requests contradiction resolution and staleness review, not a reference-answer test. Mutability is limited per producing batch before application. This is distinct from runtime librarian routes: manual/auto heal has a different evaluator target and deletion force. Context truncation, batch splitting and skipped calls bound the evidence available; no detailed rationale/blame placement is required in the response schema. NewFacts are candidate generation, with semantic relation indeterminate absent outputs.

- Immediate return: Parsed batch response and optional corpus, or skipped/unattempted work.
- Later read-back: inapplicable — assessment results feed same-pass mutations; retained facts are the next route.
- Delegated visibility: Only selected bounded prompt state, not guaranteed full database despite prompt's 'full dump' wording.
- Selection predicate: Eligible heal batch/cooldown, keyword availability, selected anchors and bounded-call ladder.
- Invalidation or expiry: Transient failures and budget-unattempted candidates are not cooldown-stamped; other attempted candidates may be deferred.
- Activation or effect: Responses feed scoped deletion/downgrade and new-fact admission.
- Evidence limits: Prompt request establishes criticism intent; no observed content-directed criticism with resulting reasoned revision is supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/prompts.ts` (implementation; quoted prompt supplies doctrine/design).

> You are a memory grooming agent. Your job is to review a full dump of facts and recent events to resolve contradictions, downgrade stale claims, and flag obsolete facts for deletion.
> --- `packages/core/src/prompts.ts`

#### EPI-RTE-heal-dispose
Label: Heal withdrawal and retention

Distinct identity and comparison: no supplied route separately individuates this function; related supplied admission routes remain valid containers.

Check target / transition: Fact confidence/liveness and newly synthesized candidates.

Owner: MaintenanceService. Before model work, deterministic orphan/stale policies can already mutate rows. Model downgraded/deleted IDs are intersected with that response's batch; new facts pass validateFact and inferred-title deduplication, then optional grounding. Code downgrades and soft-deletes before dedupe/insert, allowing delete-plus-restate. No mandatory human veto or answer oracle; computational model proposes and program scopes/applies. Guidance: heal prompt and host configuration; operating mode: periodic/manual ongoing maintenance. Consumer/channel/force/horizon: SQLite confidence/liveness/content affects future searches, with touched-ID index sync, embedding notification/removal and cache eviction. Hook failures can be reported after data mutation, not restore truth. Recovery is host-directed history/backup/replacement; no semantic undo guarantee. Distinct from check above and runtime admission containers; neither inferred-title similarity nor staleness establishes falsehood.

- Immediate return: Heal counts, remaining/deferred/skipped/degraded information and persisted effects.
- Later read-back: Surviving/new facts are available to later retrieval and maintenance; deleted facts leave live selection.
- Delegated visibility: Embedding hook/provider receives touched facts/IDs after mutation, not an independent content approval.
- Selection predicate: Per-batch mutable IDs, shape validation, fuzzy inferred-title dedupe and optional grounding.
- Invalidation or expiry: Explicit deletion/replacement; cooldown stamps include created facts but exclude transient failures/unattempted budget work.
- Activation or effect: Withdrawal/reduced confidence and retained replacement candidates; not demonstrated better answers.
- Evidence limits: No evidence-consuming semantic acceptance criterion beyond model judgment and structural/grounding policy; transformation cannot be classified as entailed or ampliative from interface alone.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/MaintenanceService.ts` (implementation).

> await this.entryRepo.downgradeByIds(safeDowngraded, entityId, tx);
>       await this.entryRepo.softDeleteByIds(safeDeleted, entityId, tx);
> --- `packages/core/src/services/MaintenanceService.ts`

#### EPI-RTE-judge-check
Label: Reference answer judgment

Part of: [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

Distinct identity and comparison: this is a material function within the cited runtime container; checking and disposition have different results and consumers.

Check target / transition: Generated answer versus dataset answer/rubric for one LongMemEval question type.

Owner: judge provider, requested yes/no. Reference oracle is q.answer, not the retrieval corpus; q.question and answer-model response also enter the judge prompt. Criterion allows equivalent answers and intermediate steps, rejects incomplete answers, tolerates temporal off-by-one differences and old information alongside a required updated answer; preference mode uses a personalization rubric. Intended use/scope: benchmark correctness scoring, not accepting core facts. No reference provenance or judge calibration established by the prompt. Human activity supplies dataset/design externally; no per-verdict human veto in inspected driver. Distinct check inside runtime benchmark container, refining its explicitly uninspected oracle-prompt field, not contradicting it.

- Immediate return: Judge response text.
- Later read-back: inapplicable — current-call reply goes to parseVerdict, not memory admission.
- Delegated visibility: Judge gets question/reference/response, not necessarily memory evidence.
- Selection predicate: Question type selects template; literal one-pass placeholder substitution.
- Invalidation or expiry: inapplicable — one benchmark judgment, no standing knowledge endorsement.
- Activation or effect: Reply consumed by parseVerdict for recorded score.
- Evidence limits: No observed-run or causal result adopted; judge agreement is bounded answer/reference fit, not mechanism validation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/benchmarks/src/longmemeval/judge.ts` (implementation).

> const values: Record<string, string> = { question: q.question, answer: q.answer, response };
> --- `packages/benchmarks/src/longmemeval/judge.ts`

#### EPI-RTE-judge-record
Label: Judge verdict recording

Part of: [RT-RTE-benchmark-answer](runtime.md#rt-rte-benchmark-answer)

Distinct identity and comparison: this is a material function within the cited runtime container; checking and disposition have different results and consumers.

Check target / transition: Judge reply interpreted as result.correct.

Owner: parseVerdict plus benchmark driver. A trimmed lowercase prefix yes yields true; all other replies false. Concrete deterministic deduction: 'yesterday' passes the prefix test although not the requested yes/no; no execution is needed. Operational force: permissive scoring parser changes the recorded result, not fact admission. Consumer/channel/horizon: result object correctness used for benchmark reporting; exact aggregation/promotion beyond runtime result record remains uninspected. Computational judge proposes, program decides; no human veto. No product/knowledge/capability change is installed by this verdict. Distinct disposition from reference check.

- Immediate return: Boolean correctness in question result.
- Later read-back: uninspected — stored-result aggregation not inspected; this is not core memory read-back.
- Delegated visibility: inapplicable — deterministic parser.
- Selection predicate: trim().toLowerCase().startsWith('yes').
- Invalidation or expiry: inapplicable — no implemented retraction of this Boolean in inspected parser.
- Activation or effect: Recorded answer-evaluation decision only.
- Evidence limits: No evidence of successful evaluation runs, causal memory benefit, or promotion into production policy.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/benchmarks/src/longmemeval/judge.ts` (implementation).

> return text.trim().toLowerCase().startsWith('yes');
> --- `packages/benchmarks/src/longmemeval/judge.ts`

The draft-consumption countercase and ops grounding exception are directly inspected SRC-1 implementation, not inferred from status names:

> const excludeDrafts = (options?.excludeDrafts ?? config?.excludeDrafts ?? false) === true;
> --- `packages/core/src/services/RetrievalService.ts`

> if (op.op === 'UPDATE' && target.source_type === 'librarian_inferred') {
> --- `packages/core/src/services/librarian/ops/apply.ts`

> await deps.entryRepo.upsert({
>             ...existing,
>             title: newTitle,
>             body: op.body ?? g.candidate.fact.body,
>             updated_at: now,
>           }, tx);
> --- `packages/core/src/services/librarian/ops/apply.ts`

Source-event labels are requested but not mandatory for ops admission; fallback chronology is not source authentication:

> const sourceLabel = typeof r.source_event === 'string' && byLabel.has(r.source_event) ? r.source_event : null;
> --- `packages/core/src/services/librarian/ops/extract.ts`

### Claims

#### EPI-CLM-grounding-draft
Label: Ungrounded candidate draft promise

Claimed operation: configured writer prompts promise to retain facts with unmatched source quotes as unreviewed drafts. This is a prompt-level doctrine claim, not proof that all writes are checked. Distinct from the general memory claim [RT-CLM-longterm-memory](runtime.md#rt-clm-longterm-memory). Configuration and implementation limits: see [EPI-RTE-grounding-check](#epi-rte-grounding-check) and [EPI-RTE-grounding-status](#epi-rte-grounding-status). SRC-1, `packages/core/src/prompts.ts` (doctrine/design).

> A fact whose quotes cannot be found in the SOURCE section is stored as an unreviewed draft.
> --- `packages/core/src/prompts.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; new route records carry their distinct consumer/channel/force/horizon, while [RT-BAP-memory-context](runtime.md#rt-bap-memory-context) and [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) remain the supplied context/guidance paths.
