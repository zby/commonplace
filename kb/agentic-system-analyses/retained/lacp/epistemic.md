---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LACP's candidate retention, evaluator domains and consequential reliance routes at the frozen revision."
run-id: AAS-2026-10-14-lacp-91efd16f7a35-01
reviewed-boundary: e31f134b689afd6a71d94b0420682d1f528d6fa1
---

# LACP epistemic report

## Source-and-claim boundary

This overlay asks which LACP routes create or acquire truth-apt candidates, which checks license reliance, and which results actually govern continuation or later use. The scope is the shipped operating layer, including native generation, host hooks, memory maintenance and improvement machinery. The frozen source and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register), SRC-1. No source or execution evidence is added.

Runtime records are provisional supplied findings, not direct inspection by this analyst. Direct additional reads below supply implementation evidence; source docstrings and CLI help supply doctrine/design. No target execution occurred. No observed run or causal experiment is supplied. External host/model internals, installed vault/index contents and deployed schedules remain unresolved. They prevent conclusions about actual candidate truth, effective host enforcement, retrieval benefit, exact weights and exercised improvement.

Coverage is selective within the whole-system boundary. Relevant available but uninspected routes remain named below; this report does not establish a system-complete absence of acceptance, theory criticism or knowledge production. A candidate's retention or changed filename is not an evidence-consuming acceptance decision. Formal or deterministic checks have only their named domain.

| Entry point or operation | Source path | Coverage and records / prevented conclusion |
|---|---|---|
| No-argument CLI, provider turns, keyed memory and session restore | `bin/lacp`, `tui/repl.py`, `tui/tools.py`, `tui/providers.py`, `tui/sessions.py` | Supplied runtime: [RT-RTE-native-turn](runtime.md#rt-rte-native-turn), [RT-OBJ-messages](runtime.md#rt-obj-messages). Dispatch searched directly; memory handlers and provider internals not independently reread here. No exhaustive semantic classification of generated content. |
| Host launch, bypass, delegation, MCP and skill supply | `bin/lacp-stream`, `tui/mcp.py`, `tui/tools.py` | Supplied [RT-RTE-host-launch](runtime.md#rt-rte-host-launch), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). Host-internal evidence consumption is outside the frozen source. |
| Sandbox, swarm, workflow and harness | `bin/lacp-sandbox-run`, `bin/lacp-workflow-run`, `bin/lacp-harness-run` | Supplied [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch), [RT-RTE-orchestrated-run](runtime.md#rt-rte-orchestrated-run), [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance), [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt). Configured task references and verifier independence unresolved. |
| Stop checks and self-model update/context | `hooks/stop_quality_gate.py`, `hooks/self_memory_system.py` | Direct score parsing, evaluator and final consumer reads; direct SMS update/context reads. [RT-RTE-host-hook](runtime.md#rt-rte-host-hook), [EPI-RTE-self-model-update](#epi-rte-self-model-update). Episode writer/caller wiring supplied by boundary/runtime; no run. |
| PostToolUse Write validation | `hooks/write_validate.py` | Entire file directly inspected: [EPI-RTE-note-validation](#epi-rte-note-validation). Installed host matching not supplied; plugin copy not independently inspected. |
| Shared daily extraction and optional auto promotion | `automation/scripts/extract_shared_memory.py`, `automation/scripts/suggest_memory_promotions.py`, `automation/scripts/run_memory_pipeline.sh` | Direct cleaning/lesson selection and rendering, complete suggestion helper and driver: [EPI-RTE-memory-promotions](#epi-rte-memory-promotions). History reader internals not fully inspected; original histories absent. |
| CLI curate / brain expansion title stage | `bin/lacp-curate`, `automation/scripts/curate_titles.py` | CLI dispatch/help searched; entire Python implementation directly read: [EPI-RTE-title-renaming](#epi-rte-title-renaming). Other expansion stages not inferred equivalent. |
| RAG query and retrieval probes/benchmark | `automation/scripts/query_memory_rag.py`, `automation/scripts/active_recall_probes.py`, `automation/scripts/benchmark_memory_retrieval.py` | Direct query_index, saved-index loading, probe_item and benchmark reference/path metric reads: [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking), [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy). Index construction/embedding provenance and full benchmark gate variants not traced. |
| Consolidation conflict/prune/cleanup | `automation/scripts/memory_consolidation.py` | Direct detect_conflicts through run_consolidation and main: [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy). Imported scoring, graph and registry helper internals uninspected; downstream interpretation of supersedes unestablished. |
| Learn eval, promote, rollback | `bin/lacp-learn-eval`, `bin/lacp-learn-promote`, `bin/lacp-learn-rollback` | Entire eval directly read: [EPI-RTE-learning-metrics](#epi-rte-learning-metrics); promotion/rollback supplied [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion). No downstream enforce-mode consumer established. |
| Idle improvement | `tui/idle_agent.py`, `tui/autoresearch_metrics.py` | Supplied [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment), [RT-BAP-autoresearch-code](runtime.md#rt-bap-autoresearch-code). No independent experimental outcome. |
| Other ingestion, synchronization, research promotion and maintenance | `automation/scripts/brain-ingest.sh`, `automation/scripts/sync_research_knowledge.py`, `automation/scripts/suggest_research_promotions.py`, `automation/scripts/consolidate_research.py`, `automation/scripts/compile_wiki.py`, `automation/scripts/generate_review_queue.py`, `automation/scripts/detect_knowledge_gaps.py`, `bin/lacp-brain-expand` | Included and available, not traced here. Prevents complete claims about imported warrant preservation, all generated summaries, all lifecycle integration and all semantic acceptance routes. |
| Other evaluator and learning consumers | `autoresearch/evaluate.py`, `autoresearch/evaluate_memory.py`, `autoresearch/optimize.py`, `bin/lacp-learn-retrieve`, `hooks/session_start.py`, `plugin/hooks/scripts/session_start.py` | Included but not directly traced here beyond supplied boundary/runtime descriptions. Prevents all-evaluator completeness, learning advisory consumer equivalence and plugin session-context parity. External skill-factory internals remain outside SRC-1. |

Consequential claims found: [RT-CLM-control-scope](runtime.md#rt-clm-control-scope), [RT-CLM-idle-improvement](runtime.md#rt-clm-idle-improvement), [EPI-CLM-title-normalization](#epi-clm-title-normalization), [EPI-CLM-learning-report](#epi-clm-learning-report). These are operation/proxy claims, not a discovered universal truth oracle. Unread documentation prevents a system-wide claim inventory.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-messages](runtime.md#rt-obj-messages) | see record; user/tool/assistant text can carry scoped claims, but no supplied instance individuates them | see record | SRC-1, `tui/repl.py` | Generation route does not establish candidate truth or accepted ampliation. |
| [EPI-OBJ-promotion-text](#epi-obj-promotion-text) | see record | see record | SRC-1, `automation/scripts/suggest_memory_promotions.py` | Original factual warrant unknown; requests/commands are not necessarily propositions. |
| [EPI-OBJ-vault-title](#epi-obj-vault-title) | see record | see record | SRC-1, `automation/scripts/curate_titles.py` | Shape classifier is not semantic truth check. |
| [EPI-OBJ-self-model](#epi-obj-self-model) | see record | see record | SRC-1, `hooks/self_memory_system.py` | Pattern labels and confidence can outrun available session evidence. |
| [EPI-OBJ-retrieval-result](#epi-obj-retrieval-result) | see record | see record | SRC-1, `automation/scripts/query_memory_rag.py` | Retrieved text warrant unchanged/unknown; rank is not endorsement. |
| [EPI-OBJ-learning-report](#epi-obj-learning-report) | see record | see record | SRC-1, `bin/lacp-learn-eval` | Metrics are about supplied labels and token overlap, not independently measured task truth. |
| [RT-OBJ-autoresearch-program](runtime.md#rt-obj-autoresearch-program) | see record; operational method, not an expected task answer | see record | SRC-1, `config/autoresearch-program.md` | Score-selected source change does not warrant transfer or benefit. |

## Authority-route ledger

Each ledger entry separates functions even where one declaring route owns the linked chain. All non-status fields below refer to the record that owns their findings; its evidence is not duplicated. “Implemented” means inspected code or the supplied code-grounded runtime finding, never observed activation.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | content transformation | implemented | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | SRC-1, `tui/repl.py` | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) |
| [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | retention | implemented | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | SRC-1, `tui/sessions.py` | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) |
| [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | operational admission/selection/consumption | implemented | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | SRC-1, `tui/tools.py` | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | see [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) |
| [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | content transformation | implemented | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | SRC-1, `tui/providers.py` | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) | see [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) |
| [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | operational admission/selection/consumption | implemented | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | SRC-1, `tui/mcp.py` | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | see [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) |
| [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | check/evidence production | implemented | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | SRC-1, `bin/lacp-sandbox-run` | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) |
| [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | operational admission/selection/consumption | implemented | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | SRC-1, `bin/lacp-sandbox-run` | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) | see [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch) |
| [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | disposition/acceptance | implemented | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | SRC-1, `bin/lacp-workflow-run` | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) | see [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) |
| [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | check/evidence production | implemented | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | SRC-1, `bin/lacp-harness-run` | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) |
| [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | disposition/acceptance | implemented | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | SRC-1, `bin/lacp-harness-run` | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) | see [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt) |
| [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | check/evidence production | implemented | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | SRC-1, `hooks/stop_quality_gate.py` | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) |
| [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | operational admission/selection/consumption | implemented | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | SRC-1, `hooks/stop_quality_gate.py` | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) | see [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) |
| [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | content transformation | implemented | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | SRC-1, `automation/scripts/suggest_memory_promotions.py` | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) |
| [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | check/evidence production | implemented | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | SRC-1, `automation/scripts/suggest_memory_promotions.py` | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) |
| [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | retention | implemented | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | SRC-1, `automation/scripts/suggest_memory_promotions.py` | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) | see [EPI-RTE-memory-promotions](#epi-rte-memory-promotions) |
| [EPI-RTE-title-renaming](#epi-rte-title-renaming) | check/evidence production | implemented | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | SRC-1, `automation/scripts/curate_titles.py` | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) |
| [EPI-RTE-title-renaming](#epi-rte-title-renaming) | content transformation | implemented | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | SRC-1, `automation/scripts/curate_titles.py` | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) | see [EPI-RTE-title-renaming](#epi-rte-title-renaming) |
| [EPI-RTE-self-model-update](#epi-rte-self-model-update) | content transformation | implemented | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | SRC-1, `hooks/self_memory_system.py` | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) |
| [EPI-RTE-self-model-update](#epi-rte-self-model-update) | retention | implemented | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | SRC-1, `hooks/self_memory_system.py` | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) |
| [EPI-RTE-self-model-update](#epi-rte-self-model-update) | operational admission/selection/consumption | implemented | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | SRC-1, `hooks/self_memory_system.py` | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) | see [EPI-RTE-self-model-update](#epi-rte-self-model-update) |
| [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | operational admission/selection/consumption | implemented | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | SRC-1, `automation/scripts/query_memory_rag.py` | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) | see [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking) |
| [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | check/evidence production | implemented | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | SRC-1, `automation/scripts/memory_consolidation.py` | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) |
| [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | operational admission/selection/consumption | implemented | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | SRC-1, `automation/scripts/memory_consolidation.py` | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) |
| [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | lineage/freshness/recovery | implemented | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | SRC-1, `automation/scripts/memory_consolidation.py` | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) | see [EPI-RTE-consolidation-policy](#epi-rte-consolidation-policy) |
| [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | check/evidence production | implemented | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | SRC-1, `bin/lacp-learn-eval` | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) | see [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) |
| [EPI-RTE-note-validation](#epi-rte-note-validation) | check/evidence production | implemented | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | SRC-1, `hooks/write_validate.py` | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) |
| [EPI-RTE-note-validation](#epi-rte-note-validation) | operational admission/selection/consumption | implemented | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | SRC-1, `hooks/write_validate.py` | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) | see [EPI-RTE-note-validation](#epi-rte-note-validation) |
| [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | disposition/acceptance | implemented | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | SRC-1, `bin/lacp-learn-promote` | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) |
| [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | lineage/freshness/recovery | implemented | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | SRC-1, `bin/lacp-learn-rollback` | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | see [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) |
| [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | check/evidence production | implemented | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | SRC-1, `tui/autoresearch_metrics.py` | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) |
| [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | disposition/acceptance | implemented | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | SRC-1, `tui/idle_agent.py` | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) |
| [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | behavior/policy adaptation | implemented | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | SRC-1, `tui/idle_agent.py` | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | see [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) |

### Epistemic assessment of supplied runtime chains

For [RT-RTE-native-turn](runtime.md#rt-rte-native-turn), imported user/tool text is acquisition with source warrant unknown. Model output's relation is **truth-apt transformation: indeterminate**: no particular claim/input pair is supplied to prove preservation, entailment or non-entailment. Persistence of messages is retention, not acceptance or lifecycle integration. Tool status is bounded execution evidence; no answer oracle is supplied. Executable file changes are non-truth-apt organization updates unless a particular content proposition is individuated. The registry executor admits edits immediately; the later consumer is file execution/import or model interpretation, not a truth gate. Tool-result truncation and delegated last-user-only supply in [RT-RTE-host-launch](runtime.md#rt-rte-host-launch) degrade available context lineage, not prove falsehood. Skills and MCP definitions in [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) acquire external instructions/capabilities of unknown provenance, not accepted knowledge.

For [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch), target/criterion are launch-contract inputs, declared risk, budget and approval state. Results have prelaunch permissive/enforcing force at the shell gate only; epistemic license is limited to those predicates, not task correctness. There is no content change. Caller-supplied trust/confirmation and the documented budget-branch counterexample qualify [RT-CLM-control-scope](runtime.md#rt-clm-control-scope). [RT-RTE-workflow-advance](runtime.md#rt-rte-workflow-advance) records supplied decisions after protocol checks; it does not evidence-consume task results or authenticate approvers. “Acceptance” in that ledger row is operational disposition, not epistemic acceptance.

For [RT-RTE-harness-attempt](runtime.md#rt-rte-harness-attempt), tests and configured references can evidence-consume a particular work product against their conditions. Software accepts **task-success** for that use when both execution and verification succeed; license remains the checked task/profile domain. Hashes and tails support identity and partial auditability, not source truth, independent causal attribution or complete replay safety. Rejection can cause retries without undoing product effects. The verifier and runner may share mistakes; no inspected expected-answer corpus authenticates generalized correctness.

For [RT-RTE-host-hook](runtime.md#rt-rte-host-hook), tests target repository behavior under selected commands, whereas Ollama judges the last assistant-message tail against quality criteria. Those are separate evaluator domains. Direct inspection of SRC-1, `hooks/stop_quality_gate.py` confirms message truncation to the last 2000 characters, JSON score parsing and threshold comparison, followed by a consumer emitting block/allow. This does not independently verify honesty or claimed completeness. SMS retention happens before these checks. Heuristic fast exits skip testing/scoring; evaluator unavailability permits continuation; Ralph cooperation can alter a block. Hence “allow” can mean **no evaluator result**, not endorsement, and accepted task termination neither accepts nor withdraws retained SMS content. External host honoring the hook protocol is required. No content change occurs in score selection itself.

> # Ollama approved or unavailable — allow
> --- `hooks/stop_quality_gate.py`

For [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion), aggregated gates accept a mode transition for operational learning-policy use, not each learning-event claim. Distinct caller names and nonempty evidence are admission predicates; their truth/authorship remain unverified. Rollback withdraws active enforce state, not retained event content. This combines with [EPI-RTE-learning-metrics](#epi-rte-learning-metrics); downstream enforce consumers are uninspected, so permissive state writing is not demonstrated enforcement or lifecycle integration.

For [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment), health score is the check target, and the evaluator covers import/tools/startup/tests/CSS/lint proxies, not arbitrary functional task outcomes. Numeric keep/discard is operational source admission; content/update relation is non-truth-apt organization update. Later code import gives enforcing executable authority, while the program gives interpretive guidance. The zero-score failure comparison is a counterexample to “kept implies improvement.” Conditions, recovery defects and independent reflection/theory-builder/self-improvement limits remain as declared in that record; none is promoted to causal support.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-control-scope](runtime.md#rt-clm-control-scope) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-sandbox-launch](runtime.md#rt-rte-sandbox-launch), [RT-RTE-host-hook](runtime.md#rt-rte-host-hook), [RT-RTE-native-turn](runtime.md#rt-rte-native-turn) | none supplied | see records | Path-specific launch checks and selective feedback, not universal epistemic/operational mediation | Native and bypass routes contradict universal reading. |
| [RT-CLM-idle-improvement](runtime.md#rt-clm-idle-improvement) | see record | SRC-1, `tui/idle_agent.py`; doctrine/design | see record | [RT-RTE-idle-experiment](runtime.md#rt-rte-idle-experiment) | none supplied | see record | Implemented improvement-directed experiment organization | Successful improvement and criticism-fed method revision unestablished. |
| [EPI-CLM-title-normalization](#epi-clm-title-normalization) | see record | SRC-1, `automation/scripts/curate_titles.py`; doctrine/design | see record | [EPI-RTE-title-renaming](#epi-rte-title-renaming) | none supplied | see record | H1-derived renaming with lexical screening | “ok” titles also qualify; shape/rename does not create or warrant a new claim. |
| [EPI-CLM-learning-report](#epi-clm-learning-report) | see record | SRC-1, `bin/lacp-learn-eval`; doctrine/design | see record | [EPI-RTE-learning-metrics](#epi-rte-learning-metrics), [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion) | none supplied | see record | Deterministic label/overlap metrics support policy comparisons | Chronological halves do not identify an advisory treatment effect. |

## Bounded conclusion

LACP implements several consequential routes, not one warrant authority. Native messages and external content are acquired/retained with unknown source warrant; generated claims remain semantically indeterminate without an individuated input/output instance. RAG reloads retained index chunks, ranks them and returns text/path metadata; ranking does not supply new factual warrant. Learning evaluation likewise reads captured events from the retained store before deriving metrics. These are implemented later-consumer paths even though neither selector nor evaluator persists new output; operation and benefit remain unobserved. Title normalization relocates an existing H1 into a filename; it neither derives nor accepts a new truth claim.

Memory auto promotion is a positive counterexample to reading “Promote Manually” as a universal human gate. Keyword-scored candidates can be appended to durable memory by an explicit apply operation. Report provenance survives in the suggestion report but is omitted from appended memory text. Retention precedes any demonstrated evidence-consuming factual acceptance. The shipped pipeline invokes suggestions without apply; capability and automatic activation are distinct.

SMS implements a truth-apt conjecture route: it can infer “tests pass” from absence of recorded test failures and infer a test-first preference from separated keywords. Neither follows from those signals. Confidence increases by update count, and after the threshold, selected self-model fields can enter future host context. This is operative interpretive authority without an inspected semantic acceptance gate. It is not evidence of improved capacity or reliable reflection; the update and downstream injection remain architecture, not observed behavior.

Tests, schema predicates, retrieval path references, model quality judgments, token-overlap learning metrics and health scores have different targets. A structural PASS licenses only the parser's required-field predicates. A recall hit licenses only matching-path/text retrievability under the query. A success-label uplift licenses arithmetic on the stored labels. Gate-selected termination, promotion mode and kept code are operational decisions; they do not prove a generalized mechanism or transfer.

Consolidation can archive source files and protect important recall gaps. Its similarity/time conflict recommendations do not check contradiction or source truth. The inspected function mutates supersedes only in local loaded state and reports a count; no registry write occurs in that function/main. No durable withdrawal or downstream reliance consumer is thereby established for that marker. Archival is an operational availability change, not epistemic rejection.

The inspected routes do not establish accepted ampliative knowledge followed by lifecycle integration. That is a bounded non-establishment, not a whole-system negative: research ingestion/synthesis/promotions, other evaluators and installed memory consumers remain unassessed. No supplied run/experiment establishes activated benefit, independent component effect, parameter learning or exercised self-improvement. Runtime's independent theory-builder, reflection and autonomy limits remain independent of these positive memory/evaluator pathways.

## Shared records

### Components

none declared in this member. Remote provider/classifier mutability limits are supplied by [RT-CMP-anthropic-provider](runtime.md#rt-cmp-anthropic-provider), [RT-CMP-openai-provider](runtime.md#rt-cmp-openai-provider) and [RT-CMP-ollama-classifier](runtime.md#rt-cmp-ollama-classifier). Dense query embedding is an additional external numerical representation in [EPI-RTE-retrieval-ranking](#epi-rte-retrieval-ranking); parameter updates, exact weight version and endpoint identity are uninspected, with no inspected training call and a configurable, unpinned model name. No claim about fixed deployed weights follows.

### Operative objects

#### EPI-OBJ-promotion-text
Label: Memory promotion text

Natural-language prompt/lesson candidates plus symbolic score, source_file and source_section fields in Suggestion objects and Markdown promotion reports; optional natural-language append into MEMORY.md, active-tasks.md, lessons.md and TOOLS.md. These destinations have different subject matter but one append admission mechanism. Source text can assert facts/preferences, request tasks or name commands; truth-aptness must be individuated rather than inferred from the lessons label. Distinct from [RT-OBJ-messages](runtime.md#rt-obj-messages): extracts from external host histories/daily captures, not the native saved message list. SRC-1, `automation/scripts/extract_shared_memory.py`, `automation/scripts/suggest_memory_promotions.py`.

> Suggestion(text=text, score=score, source_file=daily_file.name, source_section="Candidate Lessons")
> --- `automation/scripts/suggest_memory_promotions.py`

#### EPI-OBJ-vault-title
Label: Vault filename and H1

Natural-language existing note H1 and file stem, interpreted by lexical regex rules as claim/category/timestamp/ok; symbolic path/wikilink identifiers on local vault filesystem. Truth-apt where a sentence claims something, but no concrete deployed note supplied. Filename shape and body truth are separate. No counterpart in supplied runtime objects: this is vault maintenance, not conversation storage or autoresearch instructions. SRC-1, `automation/scripts/curate_titles.py`.

> if n.h1 and classify_title(n.h1) in ("claim", "ok") and n.h1.lower() != n.stem.lower():
>     suggestion = n.h1
> --- `automation/scripts/curate_titles.py`

#### EPI-OBJ-self-model
Label: SelfModel

Natural-language preference/failure/success labels plus symbolic confidence and update counter in a dataclass, persisted as self-model.json at SMS_ROOT. Selected preferences/failures become natural-language host context; success_patterns are retained but not emitted by the inspected build_session_context. Distinct from [RT-OBJ-messages](runtime.md#rt-obj-messages), with different producer, storage and consumer. SRC-1, `hooks/self_memory_system.py`.

> model.confidence_in_self_model = min(0.9, 0.3 + (model.update_count * 0.05))
> _self_model_file().write_text(json.dumps(asdict(model), indent=2))
> --- `hooks/self_memory_system.py`

#### EPI-OBJ-retrieval-result
Label: RAG ranked chunks

Natural-language chunk text/headings and symbolic paths/rank scores in JSON index payload and returned dictionaries. Dense numerical vectors can influence selection; they are not individually truth-evaluable source claims. Query code carries chunk text/path/heading to output, not endorsement or evidence validation. No supplied runtime counterpart: external RAG selection is not native tool-message storage. SRC-1, `automation/scripts/query_memory_rag.py`.

> return ranked[:top_k], {"weights": weights, "dense_warning": dense_warning, "dense_enabled": dense_enabled, "fusion_mode": fusion_mode}
> --- `automation/scripts/query_memory_rag.py`

#### EPI-OBJ-learning-report
Label: Learning metrics report

Symbolic JSON report computed in memory from local learning events.jsonl; fields total_events, split_at, success rates, hit_rate, mrr and uplift_pct assert deterministic properties of parsed events under the code's definitions. Input task summaries are natural language and labels are caller-supplied symbolic values. Distinct from [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion): this is its metric input, not promotion state or evidence file. SRC-1, `bin/lacp-learn-eval`.

> uplift = round((treat_sr - base_sr) * 100.0, 4)
> --- `bin/lacp-learn-eval`

### Routes

#### EPI-RTE-memory-promotions
Label: Memory suggestion and append

No counterpart among supplied runtime routes; extraction/suggestion/append is separate from native conversation persistence and enforce-state promotion.

Endpoints: cleaned daily prompt/lesson bullets → keyword score and focus/dedup selection → report → optional target-file append. Owner: Python code; caller selects apply/targets/thresholds, not necessarily a human per candidate. Imported historical assertions have unknown source warrant; clean_text redaction/truncation degrades original context. Prefix removal/dedup is non-ampliative reshaping of retained text, not novel explanatory content. Check target: relevance/lexical shape, secrecy/noise hints and duplicate lines. Score is a deterministic heuristic, not calibrated factual confidence or expected-answer oracle. Retention function accepts an append operation for selected memory use, not evidence-consuming truth acceptance or lifecycle integration. Consumer: local target-file readers, whose actual downstream model delivery is uninspected; channel Markdown gives at most potential interpretive guidance across later sessions. Report stores source file/section, but apply stores only text, losing that local provenance at the target. Reject/skip ability: focus/score/noise/dedup and absence of apply; no implemented per-claim verifier or automatic rollback in this helper. Guidance is the source keyword rules; persistent outputs are suggestions and optional memory text. No formulated explanatory theory is individuated.

Concrete deterministic deduction: a daily Candidate Lessons bullet `- [codex] root cause and regression fix` becomes `root cause and regression fix`; lesson hints add 0.8 (length does not add 0.1 here), passing default 0.75. With apply and no exact existing duplicate, that same string is appended to lessons.md. The source note/section is not appended. This proves lexical selection/retention, not a newly inferred lesson or its truth. Pipeline uses min-score 0.90 without apply, so this default-helper witness does not prove pipeline admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON summary and timestamped suggestion report, with optional append counts.
- Later read-back: Reports and target files persist; actual later task-agent reading of these targets is uninspected.
- Delegated visibility: inapplicable — no model delegation in this deterministic helper.
- Selection predicate: Lookback daily files, focus/score threshold, dedup, apply flag and selected targets.
- Invalidation or expiry: No semantic expiry or rollback; existing exact normalized lines are skipped.
- Activation or effect: Writes report and, under apply, durable memory/task/lesson/command text; changed behavior unobserved.
- Evidence limits: Private daily files absent; original provenance/warrant and later consumption unresolved; pipeline does not enable apply.

Evidence: SRC-1, `automation/scripts/suggest_memory_promotions.py`; implementation.

> lesson_lines = [s.text for s in suggestions["lessons"] if normalize_line(s.text) not in lesson_existing]
> added["lessons"] = append_under_heading(LESSONS_FILE, f"## Auto Promoted ({timestamp})", lesson_lines)
> --- `automation/scripts/suggest_memory_promotions.py`

#### EPI-RTE-title-renaming
Label: H1 title normalization

No counterpart in supplied runtime routes; vault filename maintenance is distinct from product edits and extension admission.

Endpoints: vault note path/body → lexical title classifier and first-H1 parser → rename proposal → optional filesystem rename/wikilink rewrite. Owner/evaluator: code; caller enables apply; no per-proposal human judgment required. Check target/domain: title shape, protected directories/date naming, H1 length/template filters and destination collision, not the proposition's truth. Content relation: truth-apt transformation: non-ampliative reshaping for a claim-shaped H1 when sanitization leaves its wording intact; otherwise identifier update for non-truth-apt titles, or truth-apt transformation: indeterminate where punctuation removal may alter claim meaning. It transfers existing H1 wording, strips some punctuation for filename safety, and does not derive a claim from evidence. Semantic preservation of every admissible title is not guaranteed. Operational force: rename map and filesystem operations enforce naming changes; later filename retrieval may rank differently, but benefit is unobserved. No evidence-consuming acceptance/integration.

Concrete static deduction: unprotected `Research Notes.md` with H1 `# memory graphs beat giant memory files` is category-shaped, its H1 is claim-shaped, and apply selects `memory graphs beat giant memory files.md` if absent. The wording already existed. Counterexample to exclusive claim-shape: H1 `# Context Engineering Playbook` is `ok` and can also become the filename. Existing new path vetoes apply; absent suggestion skips it. Caller-triggered apply, protected-dir checks and collision skips are admission/rejection; there is no automatic rename rollback. Guidance is lexical rules, not an independently checked theory. In apply_renames, notes retain original rel paths; a just-renamed note's old path no longer exists and is skipped in link rewriting. Thus “vault-wide” link correction is not unconditional, particularly for links inside renamed files.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Proposals/report or applied rename list.
- Later read-back: Renamed paths and edited links persist for future vault/index readers; their behavioral dependency is unobserved.
- Delegated visibility: inapplicable — no model invocation.
- Selection predicate: Timestamp/category or needs_curation, usable distinct H1, apply, no collision, unprotected location.
- Invalidation or expiry: No transaction/revert; collision/empty suggestion prevents rename; next scans use changed files.
- Activation or effect: Filesystem rename and selected extant-file wikilink writes; no truth endorsement.
- Evidence limits: No deployed vault or retrieval comparison; unsafe punctuation transformations remain semantically unclassified.

Evidence: SRC-1, `automation/scripts/curate_titles.py`; implementation.

> old_path.rename(new_path)
> rename_map[old_path.stem] = new_stem
> applied.append((p["note"], new_stem))
> --- `automation/scripts/curate_titles.py`

#### EPI-RTE-self-model-update
Label: SMS inferred self-model

Part of: [RT-RTE-host-hook](runtime.md#rt-rte-host-hook)
This is the hook chain's durable self-description part, not the check/termination feedback part.

Endpoints: session-summary/outcome signals → inferred labels/preferences → self-model.json → selected future session context. Code owns update and threshold; host/model interprets injected context. Objects: EPI-OBJ-self-model. Content relation: truth-apt transformation: ampliative conjecture for pattern/preference assertions. Check target: flags, keyword occurrences and update count; evaluator domain is recorded signal predicates, not actual session success or agent preference. No independent answer oracle, evidence-consuming acceptance or lifecycle integration is implemented by these inspected functions.

Concrete counterexample deduction: files_changed=16 with had_test_failures=False produces `large successful changes (15+ files, tests pass)` even if no tests ran; absence of a failure flag does not entail passing tests. Summary `test failed first; use a different approach` contains test and first and can add `test-first`, without expressing that preference. Three writes raise confidence from base 0.3 to 0.45 irrespective of correctness; >0.4 enables selected preference/failure context. Confidence is admission by count, not corroboration. Labels can therefore influence later prompts without factual acceptance. Preferred approaches and failure patterns reach context; success labels do not directly reach this particular consumer. Retention and operational consumption are separate functions; no semantic evaluator revises/withdraws stale labels. Code admits new labels with bounded failure/success lists; caller supplies signals, human contribution unresolved. Retained guidance is self-description, and actual improvement/activation is unobserved.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: No explicit return value from update; build_session_context returns selected text.
- Later read-back: self-model.json reloads; after count-derived threshold, selected fields enter context builder and root session hook delivery as supplied by boundary.
- Delegated visibility: inapplicable — update function performs no model call; downstream host receives selected contextual text.
- Selection predicate: Signal/keyword predicates and confidence >0.4; source update wiring is supplied by runtime/boundary.
- Invalidation or expiry: Failure/success arrays capped at last ten; no semantic withdrawal/expiry for preferences in inspected update.
- Activation or effect: Durable self-description and future interpretive context; compliance and benefit unobserved.
- Evidence limits: Session signals and host operation absent; not all retained fields are emitted; plugin context parity not established.

Evidence: SRC-1, `hooks/self_memory_system.py`; implementation.

> if files_changed > 15 and not had_test_failures:
>     pattern = "large successful changes (15+ files, tests pass)"
> --- `hooks/self_memory_system.py`

> if "test" in lower and "first" in lower:
>     pref = "test-first"
> --- `hooks/self_memory_system.py`

> if sm and sm.confidence_in_self_model > 0.4:
>     if sm.preferred_approaches:
>         parts.append(f"Preferred approaches: {', '.join(sm.preferred_approaches[:3])}")
> --- `hooks/self_memory_system.py`

#### EPI-RTE-retrieval-ranking
Label: Hybrid RAG candidate selection

No supplied runtime counterpart; this is external retained chunk ranking, not tool-name dispatch or extension discovery.

Endpoints: saved index → CLI reload of retained payload with caller query → sparse/lexical/optional dense scores → RRF candidate selection and final rescoring → top-k dictionaries. Owner: deterministic ranking code and external embedding service. Content relation: truth-apt transformation: non-ampliative reshaping for existing chunk text; returned paths/text preserve the indexed payload fields but original-source fidelity/warrant is uninspected. Check/selection target: textual similarity to query, not truth. Force: ranking through returned query results for CLI/probe/benchmark callers; model-facing use beyond supplied boundary descriptions uninspected. No acceptance, semantic rollback or lifecycle integration. Consumer receives selected text, heading, path and numeric scores, not omitted chunks. Dense exception can remove dense signal and reweight sparse/lexical when fallback permitted; this changes selection domain without validating content. Optional embedding name defaults to nomic-embed-text:latest or payload/override model; no exact weights pinned, parameter mutation/service internals uninspected, mutable endpoint configurable. Ranking can be implemented while deployed index provenance remains unknown.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Top-k ranked chunk dictionaries and weights/dense-warning metadata.
- Later read-back: CLI loads the saved index payload and passes retained chunks into query_index; selected text, heading, path and scores reach CLI/probe/benchmark callers. This is incoming retained-material consumption, not persistence of new selector output. Later task-model consumption and behavioral dependence are uninspected.
- Delegated visibility: Embedding service gets query text when dense enabled; receives no evidence claims for truth judgment.
- Selection predicate: Scores, positive-signal ranked lists, top_k*4 RRF candidates, final mixed score and top-k cut.
- Invalidation or expiry: No semantic expiry; externally rebuilt index changes results; fallback can disable dense weights.
- Activation or effect: Ranks/delivers retained text to callers; epistemic license is none beyond selection arithmetic.
- Evidence limits: Index construction and service internals uninspected; no observed retrieval or factual endorsement.

Evidence: SRC-1, `automation/scripts/query_memory_rag.py`; implementation.

> payload = json.loads(index_path.read_text())
> --- `automation/scripts/query_memory_rag.py`

> "rrf_score": round(rrf_score, 6),
> "sparse_score": round(scores["sparse"], 6),
> "dense_score": round(scores["dense"], 6),
> "lexical_score": round(scores["lexical"], 6),
> "path": chunk.get("path", ""),
> "heading": chunk.get("heading", ""),
> "text": chunk.get("text", ""),
> --- `automation/scripts/query_memory_rag.py`

#### EPI-RTE-consolidation-policy
Label: Similarity conflict and forgetting policy

No counterpart among supplied runtime routes; registry/pruning policy differs from workflow role checks and enforce-mode rollback.

Endpoints: registry/related scores and latest recall probes → conflict/prune recommendations → optional local supersedes mutation and file archival/state history. Owner/evaluator: code with imported graph/scoring helpers (not independently inspected). Truth-apt content relation: no content change to retained assertion text; metadata/retrieval policy update is non-truth-apt. Conflict target: related-pair similarity above threshold; winner: later event string, then confidence, then first encountered. Unlike the docstring's intent, different source/time is not a required filter; identical-time equal-confidence similar items also yield a winner/loser. Similarity does not check contradiction. Recommendations license only this heuristic policy, not truth or warranted supersession.

Concrete static deduction: two similar, same-time, equal-confidence items yield tie_keep_first; no opposing proposition is required. Apply sets loser.supersedes=winner in loaded items and reports superseded count. Entire run_consolidation/main read shows no registry serialization, so this marker has no established durable downstream force. Pruning differs: selected weak/low-connected items can move from graph files to archive; prune history persists. Latest probe CRITICAL_RETRIEVAL_GAP with importance >=0.4 protects a candidate. probe_item counts expected item/category filename stems or >=0.5 token overlap as hits; those checks can succeed without recovering the precise proposition. Reference oracle is identity/overlap, not factual truth. Benchmark expected_paths similarly define a path-reference domain, including prefix matches, not independent source accuracy.

Operational consumers: policy protects/orders archival candidates and shutil.move enforces availability change; history supports audit, not semantic rejection. Archival state does not roll back claims or establish integration of an accepted winner. Caller enables apply; software selects; human per-item approval unresolved. Imported scoring and graph safeguards constrain admission; no automatic archival rollback in inspected function. Guidance is operational heuristics and probe results, not formulated explanatory criticism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary/preview, optional moves, saved prune-history and local-only marker count.
- Later read-back: Prune history/file location changes persist; durable supersedes marker/use not established by inspected function/main.
- Delegated visibility: inapplicable — policy function invokes no model; helpers/probes use stored ranking results.
- Selection predicate: Similarity/time/confidence policy; storage/retrieval strengths, edge checks, probe importance, max-prune and bridge/frontier safeguards.
- Invalidation or expiry: Archival changes file availability; marker has no inspected registry save; no explicit claim expiry or restore.
- Activation or effect: Protects/prioritizes/archives candidates; no semantic truth rejection/acceptance.
- Evidence limits: Imported graph/strength/registry internals and archive indexing consumers uninspected; no evidence of persistent supersession.

Evidence: SRC-1, `automation/scripts/memory_consolidation.py`; implementation.

> if apply and conflicts:
>     for conflict in conflicts:
>         loser_id = conflict["loser"]
>         if loser_id in items:
>             items[loser_id]["supersedes"] = conflict["winner"]
>             superseded_ids.append(loser_id)
> --- `automation/scripts/memory_consolidation.py`

> shutil.move(str(source), str(dest))
> --- `automation/scripts/memory_consolidation.py`

> if result_stem in expected_stems:
>     hit_rank = rank
>     break
> --- `automation/scripts/active_recall_probes.py`

> if candidate.startswith(expected_norm):
>     return True
> --- `automation/scripts/benchmark_memory_retrieval.py`

#### EPI-RTE-learning-metrics
Label: Chronological learning-store metrics

Distinct checking route feeding [RT-RTE-learning-promotion](runtime.md#rt-rte-learning-promotion); that record owns admission/state writing, while this referent computes the metric evidence. It is not a duplicate promotion decision.

Endpoints: retained events.jsonl → evaluator reload of captured events → parsed capture-order halves → label success rates and overlap rankings → report → threshold gate JSON → promotion caller. Owner/evaluator: embedded Python plus shell; symbolic report is EPI-OBJ-learning-report. Content relation: truth-apt transformation: entailed derivation **only** for the code-defined arithmetic predicates conditional on faithfully parsed event labels; premises are not independently warranted descriptions of task outcomes. Invalid JSON lines are skipped. It does not derive actual learning or causal improvement.

Target/domain: label frequencies, token coverage and quality-order matches in chronological halves; reference outcomes are captured outcome.status/score, not independent expected task answers. Gate compares min_events, uplift, hit-rate and MRR thresholds. Counterexample deduction: two first-half failures and two second-half successes yield 100 percentage-point uplift even when no advisory was used and tasks differ. Capture order alone is no controlled treatment. A token match's quality >= treatment quality and coverage >=0.5 can count as help without evidence the later agent saw it. Human/computational contributions: event label supplier unresolved; code proposes report and decides thresholds; caller chooses promotion and can refuse. Immediate report is read-only; consequential force exists through the supplied promotion consumer, bounded to mode admission, not each fact. No content rewrite, automatic learning-policy adaptation or factual acceptance occurs here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Deterministic metrics or metrics_pass plus threshold checks/manual gate requirements.
- Later read-back: Evaluator opens the retained events.jsonl store and parses captured events into the metric computation; aggregate report/gate JSON reaches the promotion caller. This is incoming retained-material consumption, with no new persistent evaluator output. Promotion-state read-back is a separate supplied runtime route; operation and behavioral benefit remain uninspected.
- Delegated visibility: inapplicable — no model delegated; promotion caller receives aggregate JSON.
- Selection predicate: Capture-order split (caller override for report), status/score quality and token-overlap ranking; gate policy thresholds.
- Invalidation or expiry: Changes to store/policy change results; no timestamp/semantic expiry built into report.
- Activation or effect: Produces label/overlap evidence consumed by enforce-state admission; does not itself mutate state.
- Evidence limits: Outcome labels unverified, task mix/time confounds and advisory exposure absent; no causal learning license.

Evidence: SRC-1, `bin/lacp-learn-eval`; implementation.

> with open(store) as f:                 # read-only
>     for line in f:
> --- `bin/lacp-learn-eval`

> baseline = events[:split]
> treatment = events[split:]
> --- `bin/lacp-learn-eval`

#### EPI-RTE-note-validation
Label: Post-write knowledge-note schema check

Distinct from [RT-RTE-host-hook](runtime.md#rt-rte-host-hook) pre-tool/Stop route: this separately shipped PostToolUse Write check evaluates note schema after the write, not task quality before termination.

Endpoints: written-file path → markdown/path predicate → simple frontmatter parser → required-field/category checks → PASS/WARN/FAIL/SKIP JSON and exit status. Owner/evaluator: Python code; host owns subsequent treatment of exit 2. Target/domain: textual presence/nonempty title/category, recommended created/tags and optional taxonomy membership. Truth-apt content relation: no content change. PASS licenses only these parser predicates, not YAML validity in general or body factual truth. Unknown category is WARN; missing taxonomy yields no category judgment. Concrete deduction: a note with title: False claim and category: made-up can avoid FAIL when required strings are nonempty, even if the category is invalid (WARN) or taxonomy unavailable. Original write already occurred, so failure is post-write feedback, not rejection-before-retention or rollback. Admission/diagnosis: code decides schema result, caller/host controls activation; author/principal unresolved. No answer oracle for factual content; current-run hook mode with no automated theory revision. Consumer/channel: host receives JSON/exit 2, intended blocking feedback with external host-contract force, current event horizon; direct invocation only prints/returns status. Implementation cannot establish host honoring feedback.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Structured status/issues/file and FAIL exit 2; otherwise exit 0.
- Later read-back: inapplicable — checker stores no new content; original file persists independently of result.
- Delegated visibility: inapplicable — no model; host receives JSON and exit status.
- Selection predicate: Configured path-prefix test, .md suffix, delivered file path, parser-required fields.
- Invalidation or expiry: No automatic removal/revert or semantic expiry; later writes can be checked anew.
- Activation or effect: Emits post-write failure feedback for missing fields, warnings for recommendations/category; no truth endorsement.
- Evidence limits: Installed matching and host response unobserved; path prefix/simple parser weaker than general schema/security boundary.

Evidence: SRC-1, `hooks/write_validate.py`; implementation.

> if result["status"] == "FAIL":
>     sys.exit(2)
> sys.exit(0)
> --- `hooks/write_validate.py`

### Claims

#### EPI-CLM-title-normalization
Label: Claim-shaped title normalization

No counterpart in supplied runtime claims. Source declares H1-based claim-shaped renaming to repair filename-driven retrieval. Supported operation and counterexamples are [EPI-RTE-title-renaming](#epi-rte-title-renaming). SRC-1, `automation/scripts/curate_titles.py`; doctrine/design; benefit unobserved and causal effect untested.

> script detects those and proposes claim-shaped rewrites from each note's own H1.
> --- `automation/scripts/curate_titles.py`

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

#### EPI-CLM-learning-report
Label: Deterministic baseline treatment report

Distinct from [RT-CLM-idle-improvement](runtime.md#rt-clm-idle-improvement): this concerns cross-CLI captured-event metrics, not TUI experiments. Source declares deterministic baseline-vs-treatment reporting and proxy advisory hit-rate. [EPI-RTE-learning-metrics](#epi-rte-learning-metrics) supports deterministic arithmetic, not identified treatment/learning benefit. SRC-1, `bin/lacp-learn-eval`; doctrine/design.

> The store is split chronologically (capture order) into a baseline half and a
> treatment half.
> --- `bin/lacp-learn-eval`

- doctrine conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

### Evidenced absences

none declared in this member. Missing evidence and available uninspected route families are limits, not absences.

### Behavioral-authority paths

none declared in this member. Each new route states its own consumer, channel, force and horizon; supplied runtime paths remain distinct. No EPI record supersedes a supplied referent.
