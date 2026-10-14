---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "EchoWiki's source acquisition, candidate synthesis, structural checks and later wiki reliance at the frozen revision."
run-id: AAS-2026-10-14-echowiki-8d428f79523e-01
reviewed-boundary: "11446997423e88177dba62d6a3d5c1e8b4886c62"
---

# EchoWiki epistemic report

## Source-and-claim boundary

The question is whether EchoWiki's knowledge compilation acquires, produces, checks and accepts truth-apt content, and what licenses later reliance. Scope and dependencies are see [boundary](boundary.md#boundary-and-evidence); evidence identities are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design only. No target execution occurred. A prompt request establishes a requested behavior, not faithful generation or acceptance.

The whole shipped compilation loop is assessed: Obsidian commands/events, CLI/API, voice transcription, model planning/generation, parser and link cleanup, persistent writes, later brief/body consumption, instruction loading, exposed file helpers and connection probes. External provider weights, Obsidian internals and private vaults remain unassessed. Missing audio/text pairs prevent judging transcription fidelity; missing source/output pairs prevent deciding actual preservation, entailment or novelty; missing evaluation decisions prevent attributing accepted knowledge to actual runs; missing execution and contrasts prevent benefit or causal attribution. Accessible code still establishes the architecture independently of these missing observations.

| Entry point or operation | Source path (SRC-1) | Coverage and records | Inspection basis / limit |
|---|---|---|---|
| Four commands, ribbon, watcher and pending review | `obsidian-plugin/src/main.ts`, `obsidian-plugin/src/raw-watcher.ts`, `obsidian-plugin/src/approval-modal.ts` | [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval), [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest), [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) | Direct reads corroborate supplied runtime; source admission is not page acceptance. |
| CLI dispatch and public API | `package.json`, `src/cli/compile.ts`, `src/compiler-api.ts` | [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) | Direct reads; no additional CLI quality gate or model-tool registration. |
| Summary, plan, concept/entity creation/update, summary rewrite | `src/wiki/compiler.ts`, `src/wiki/prompts.ts`, `src/wiki/llm.ts`, `src/llm/client.ts` | Epistemic routes below | Direct complete reads; actual outputs unavailable. |
| Link checking/cleanup | `src/wiki/wikilink.ts`, `src/wiki/compiler.ts` | [EPI-RTE-link-check](#epi-rte-link-check), [EPI-RTE-link-reshape](#epi-rte-link-reshape) | Direct reads and concrete source deduction; no target execution. |
| Writes, provenance metadata, related links, backlinks, index/log | `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`, `src/wiki/compiler.ts` | [EPI-RTE-page-retain](#epi-rte-page-retain), [EPI-RTE-source-lineage](#epi-rte-source-lineage) | Direct complete reads; storage enforcement details remain supplied runtime findings. |
| Retained context | `src/wiki/briefs.ts`, `src/wiki/compiler.ts` | [EPI-RTE-page-consume](#epi-rte-page-consume), [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages) | Direct reads; model compliance and benefit unobserved. |
| Editable instructions/settings | `src/wiki/schema.ts`, `templates/wiki/AGENTS.md`, `obsidian-plugin/src/settings-tab.ts` | [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings), [RT-OBJ-agents](runtime.md#rt-obj-agents) | Template and probe UI directly read; schema/configuration loading supplied runtime. Not automatic method revision. |
| STT and connection tests | `obsidian-plugin/src/stt-client.ts`, `src/llm/client.ts`, `obsidian-plugin/src/settings-tab.ts` | [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest), [EPI-RTE-probe-check](#epi-rte-probe-check), [EPI-RTE-probe-notice](#epi-rte-probe-notice) | Direct reads; response availability is not truth evaluation. |
| Exported filesystem/page/image helpers | `src/wiki/tools.ts` | [EPI-RTE-helper-access](#epi-rte-helper-access) | Direct complete read; no compiler registration or shipped query consumer found in inspected dispatch/callers. |
| Release and documented manual checks | `README.md`, `package.json`, `.github/workflows/release.yml` | [RT-RTE-release-build](runtime.md#rt-rte-release-build), [EPI-ABS-quality-gate](#epi-abs-quality-gate) | README/package direct reads; release route supplied runtime. No recorded test or release operation. |

Consequential knowledge claims are [EPI-CLM-knowledge-compiler](#epi-clm-knowledge-compiler), [EPI-CLM-cross-synthesis](#epi-clm-cross-synthesis), [EPI-CLM-summary-preservation](#epi-clm-summary-preservation) and see [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy). No general infallibility claim is inferred from the term knowledge compiler.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-content](#epi-obj-source-content) | Statements in input notes/transcripts; actual instances unavailable | Source context | SRC-1 `src/wiki/compiler.ts`, `obsidian-plugin/src/main.ts` | Imported content, not established source truth; STT fidelity unknown. |
| [EPI-OBJ-summary](#epi-obj-summary) | Requested document findings, ideas and description | Summary | SRC-1 `src/wiki/prompts.ts` | Generation and rewrite may preserve or alter claims; no concrete outputs. |
| [EPI-OBJ-concept-page](#epi-obj-concept-page) | Requested explanations of concepts across documents | Cross-document synthesis | SRC-1 `src/wiki/prompts.ts`, `src/wiki/page-writer.ts` | No evidence-consuming truth acceptance. |
| [EPI-OBJ-entity-page](#epi-obj-entity-page) | Requested identity and facts about named entities | Entity page | SRC-1 `src/wiki/prompts.ts`, `src/wiki/page-writer.ts` | Type membership checks constrain labels, not entity facts. |
| [EPI-OBJ-plan](#epi-obj-plan) | None required: symbolic create/update/related actions | Model-directed task selection | SRC-1 `src/wiki/llm.ts`, `src/wiki/compiler.ts` | Selection decisions do not establish selected claims' truth. |
| [EPI-OBJ-source-metadata](#epi-obj-source-metadata) | Associations with summary/full-text paths and source counts | Provenance and contextual selection cues | SRC-1 `src/wiki/page-writer.ts`, `src/wiki/briefs.ts` | Path associations are not claim-level support or verified source availability. |
| [RT-OBJ-agents](runtime.md#rt-obj-agents) | None required: compilation policy prose | See record | SRC-1 `templates/wiki/AGENTS.md` | Requested preservation/conflict behavior, not checked obedience. |
| [RT-OBJ-pending-queue](runtime.md#rt-obj-pending-queue) | None: paths/timestamps | See record | SRC-1 `obsidian-plugin/src/main.ts` | No snapshot, candidate diff or acceptance criterion. |
| [RT-CMP-llm-model](runtime.md#rt-cmp-llm-model), [RT-CMP-stt-model](runtime.md#rt-cmp-stt-model) | Not determinable in opaque numerical state | See records | SRC-1 `src/llm/client.ts`, `obsidian-plugin/src/stt-client.ts` | Exact weights, parameter updates and internal truth representations uninspected; not inferred from returned prose. |

## Authority-route ledger

Fields owned by declaring records use `see`; architectural status is this report's judgment. The table covers implemented epistemic functions, not observed episodes. Checking and disposition are separate even where one function implements both. Retention and contextual use are not lifecycle integration after acceptance.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-summary-generate](#epi-rte-summary-generate) | content transformation | implemented | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) | [EPI-CLM-knowledge-compiler](#epi-clm-knowledge-compiler) | none | see [EPI-RTE-summary-generate](#epi-rte-summary-generate) |
| [EPI-RTE-page-generate](#epi-rte-page-generate) | content transformation | implemented | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | see [EPI-RTE-page-generate](#epi-rte-page-generate) | [EPI-CLM-cross-synthesis](#epi-clm-cross-synthesis) | none | see [EPI-RTE-page-generate](#epi-rte-page-generate) |
| [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | content transformation | implemented | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) | [EPI-CLM-summary-preservation](#epi-clm-summary-preservation) | Consistency request exceeds consumer input: final concept/entity bodies are not passed to rewrite. | see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite) |
| [EPI-RTE-plan-check](#epi-rte-plan-check) | check/evidence production | implemented | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | see [EPI-RTE-plan-check](#epi-rte-plan-check) | none | none | see [EPI-RTE-plan-check](#epi-rte-plan-check) |
| [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | disposition/acceptance | implemented | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) | none | none | see [EPI-RTE-plan-dispose](#epi-rte-plan-dispose) |
| [EPI-RTE-link-check](#epi-rte-link-check) | check/evidence production | implemented | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | see [EPI-RTE-link-check](#epi-rte-link-check) | none | none | see [EPI-RTE-link-check](#epi-rte-link-check) |
| [EPI-RTE-link-reshape](#epi-rte-link-reshape) | content transformation | implemented | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) | none | none | see [EPI-RTE-link-reshape](#epi-rte-link-reshape) |
| [EPI-RTE-page-retain](#epi-rte-page-retain) | retention | implemented | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | see [EPI-RTE-page-retain](#epi-rte-page-retain) | [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy) | No implemented manual-edit conflict veto; concept create can overwrite an existing path without update preservation branch. | see [EPI-RTE-page-retain](#epi-rte-page-retain) |
| [EPI-RTE-page-consume](#epi-rte-page-consume) | operational admission/selection/consumption | implemented | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | see [EPI-RTE-page-consume](#epi-rte-page-consume) | none | none | see [EPI-RTE-page-consume](#epi-rte-page-consume) |
| [EPI-RTE-source-lineage](#epi-rte-source-lineage) | lineage/freshness/recovery | implemented | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) | none | none | see [EPI-RTE-source-lineage](#epi-rte-source-lineage) |
| [EPI-RTE-probe-check](#epi-rte-probe-check) | check/evidence production | implemented | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | see [EPI-RTE-probe-check](#epi-rte-probe-check) | none | none | see [EPI-RTE-probe-check](#epi-rte-probe-check) |
| [EPI-RTE-probe-notice](#epi-rte-probe-notice) | other — describe | implemented | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) | none | none | see [EPI-RTE-probe-notice](#epi-rte-probe-notice) |
| [EPI-RTE-helper-access](#epi-rte-helper-access) | operational admission/selection/consumption | implemented | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | see [EPI-RTE-helper-access](#epi-rte-helper-access) | none | none | see [EPI-RTE-helper-access](#epi-rte-helper-access) |
| [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | content transformation | implemented | [EPI-OBJ-source-content](#epi-obj-source-content) | truth-apt transformation: acquisition/import | Audio to externally supplied transcript; source warrant unknown | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | Candidate text supply, not verified transcription | No fidelity license | Supplies raw text for later compilation | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | none | none | No audio/transcript comparison supplied. |
| [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | check/evidence production | implemented | [EPI-OBJ-source-content](#epi-obj-source-content) | no content change | HTTP success and nonempty transcript | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest); HTTP predicate also directly read in SRC-1 `obsidian-plugin/src/stt-client.ts` | After transcription response | Return trimmed text or throw | Consumed by transcript write/error branch | Only transport success and nonemptiness | Prevents empty/error transcript persistence, not audio persistence | Plugin caller, returned promise/error, enforcing force, this voice operation | SRC-1 `obsidian-plugin/src/stt-client.ts`; passage see [EPI-RTE-probe-check](#epi-rte-probe-check) | none | none | No transcript correctness check. |
| [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | retention | implemented | [EPI-OBJ-source-content](#epi-obj-source-content) | no content change | Returned text to raw Markdown | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | Persistence without transcript confirmation | Retention before factual acceptance | Eligible input for watcher/manual compilation | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | See [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) | none | none | Accuracy and actual later operation unobserved. |
| [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) | disposition/acceptance | implemented | [RT-OBJ-pending-queue](runtime.md#rt-obj-pending-queue) | no content change | Source-path admission, not generated proposition | See [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) | See [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) | See [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) | Enforcing watcher-path permission only | No recorded evidence-consuming factual acceptance | Compile current path or remove pending entry | See [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) | See [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval) | none | none | Manual/CLI bypass; no frozen preview or output diff. |
| [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings) | operational admission/selection/consumption | implemented | [RT-OBJ-agents](runtime.md#rt-obj-agents) | non-truth-apt policy/content update: operator instructions and configuration | Operator edits to subsequent prompt/config inputs | See [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings) | See [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings) | See [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings) | Prompt policy request and endpoint selection | No automatic method warrant or improvement evaluation | Changes later model requests/configuration | See [RT-BAP-compiler-instructions](runtime.md#rt-bap-compiler-instructions) | See [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings) | none | none | No compiler-generated instruction revision or verified obedience. |

Input acquisition and watcher disposition are see [RT-RTE-voice-ingest](runtime.md#rt-rte-voice-ingest) and [RT-RTE-watcher-approval](runtime.md#rt-rte-watcher-approval): architectural status **implemented**. Notes enter as imports with unknown source warrant. STT turns audio into candidate text with unknown fidelity, not a verified derivation. Nonempty returned transcripts persist without correction confirmation. Human watcher approval grants compilation permission for the current path; it does not accept a proposition. Reject removes only the queue item. Manual and CLI paths bypass this gate. Settings/instruction policy supply is see [RT-RTE-instruction-settings](runtime.md#rt-rte-instruction-settings): architectural status **implemented**, non-truth-apt policy/content update through operator edits; no automatic evidence-fed method revision established.

Lifecycle integration after epistemic acceptance: **no route found within boundary**; see [EPI-ABS-quality-gate](#epi-abs-quality-gate). Related links, indexing and later context delivery are operative before any evidenced truth acceptance; they are not renamed into integration. Claim withdrawal/changed reliance after factual refutation: **no route found within boundary** in the same searched compiler/writer/caller scope. Overwrite and queue rejection are different functions, not epistemic withdrawal.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-knowledge-compiler](#epi-clm-knowledge-compiler) | See record | SRC-1 `README.md`; doctrine/design | Source-to-structured-linked-wiki intent | [EPI-RTE-summary-generate](#epi-rte-summary-generate), [EPI-RTE-page-retain](#epi-rte-page-retain), [EPI-RTE-link-reshape](#epi-rte-link-reshape) | None supplied | No measured quality or intervention | Implemented candidate compiler and navigation, not established accepted knowledge production | Knowledge label supplies no truth criterion. |
| [EPI-CLM-cross-synthesis](#epi-clm-cross-synthesis) | See record | SRC-1 `templates/wiki/AGENTS.md`; doctrine/design | Cross-document synthesis and existing-page context requested | [EPI-RTE-page-generate](#epi-rte-page-generate), [EPI-RTE-page-consume](#epi-rte-page-consume) | None supplied | Old bodies only for selected updates; all briefs for planning | Architecture can use retained candidates while rewriting | Actual novelty, faithfulness and acceptance unresolved. |
| [EPI-CLM-summary-preservation](#epi-clm-summary-preservation) | See record | SRC-1 `src/wiki/prompts.ts`; doctrine/design | Preserve all facts and consistency with concept pages | [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite), [EPI-RTE-link-check](#epi-rte-link-check) | None supplied | Only target names, not final generated bodies, reach rewrite; no factual comparator | Preservation request plus link-domain cleanup | No warrant for factual invariance or semantic consistency. |
| [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy) | See record | SRC-1 `templates/wiki/AGENTS.md`; doctrine/design | Manual-edit conflict instruction | [EPI-RTE-page-retain](#epi-rte-page-retain), [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) | None supplied | Full replacements; no conflict check or per-page human gate | Prompt-only preservation policy | No enforced human-edit veto. |

## Bounded conclusion

EchoWiki acquires external notes and STT text, requests summaries, concept explanations and entity facts, and retains structurally usable candidates. Imported source warrant is unknown; audio transcription fidelity is not checked. Generation and rewriting are semantically indeterminate without actual source/output propositions. Neither a checked entailed derivation from warranted premises nor a produced accepted ampliative claim is established. This does not deny that individual runs could generate true or novel statements.

Implemented evaluators license narrower conclusions: JSON/name/type/nonempty tests license task eligibility; related existence checks license current path existence; wikilink checks license membership in a whitelist that includes planned targets. Cleanup, metadata, backlinks and indexing organize candidate material without evaluating truth. Source paths/counts do not establish evidential support, and full_text references are emitted without a shipped full-text copying step. This limits recoverable source lineage even though raw notes remain in the plugin's vault.

The material acceptance criterion found is operational usability, not factual acceptance: models propose; code filters/schedules/keeps nonempty outputs and writes them; a watcher user may approve the incoming path. These decisions permit storage and later use before another check. Prior descriptions/previews enter subsequent planning, and selected old bodies enter update generation. Their force is contextual, not a truth certificate. No evidence establishes downstream model obedience, content improvement or causally beneficial synthesis. Failed generation can still yield success/log entries; neither continuation nor freshness endorses the remaining claims.

No separate evidence-consuming factual acceptance, post-acceptance lifecycle integration, or refutation-driven withdrawal was found in the inspected material paths. There is no whole-system epistemic score. Probe responses affect notices only; they do not establish factual accuracy or adapt policy. Operator instruction edits change future prompt input, independently of any automatic improvement route. Provider weight changes and numerical knowledge remain uninspected. Retained pages can shape later model context, but learning as improved capacity, formulated content-directed criticism with retained iteration, reflection about the compiler's own operation and exercised self-improvement are not established by these paths or by mere persistence. Model-internal reasoning is not inferred to lack these properties; its evidence is unavailable.

## Shared records

### Operative objects

#### EPI-OBJ-source-content
Label: Source content

Input sourceContent string from vault/CLI/API, including text returned by STT. Natural-language claims; current-call memory plus caller-owned raw text/audio files. Distinct from pending path queue: the queue does not hold a frozen body. No supplied operative-object counterpart; closest route is [RT-RTE-document-compile](runtime.md#rt-rte-document-compile). SRC-1 `src/wiki/compiler.ts`, `obsidian-plugin/src/main.ts`, `src/cli/compile.ts`.

> Full text:
> {content}
> --- `src/wiki/prompts.ts`

#### EPI-OBJ-summary
Label: Summary

Draft summary plus description, then summaries/{docName}.md. Natural-language body/description interpreted by model and human; symbolic path/frontmatter consumed by code. Current-call strings and later WikiStorage Markdown. Distinct operative part of the compilation route, not its full task sequence. SRC-1 `src/wiki/prompts.ts`, `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`.



#### EPI-OBJ-concept-page
Label: Concept page

concepts/{sanitized-name}.md: natural-language explanation and description; symbolic sources/type/path fields. WikiStorage Markdown; descriptions or previews later enter planning, selected bodies enter update calls. No supplied object counterpart; material output of [RT-RTE-document-compile](runtime.md#rt-rte-document-compile). Distinct from entity pages by requested content and writer metadata. SRC-1 `src/wiki/prompts.ts`, `src/wiki/page-writer.ts`.

> 3. Create or **update** concept pages — cross-document synthesis, not one-off notes.
> --- `templates/wiki/AGENTS.md`

#### EPI-OBJ-entity-page
Label: Entity page

entities/{sanitized-name}.md: natural-language identity/facts/description; symbolic configured entity type and source list. WikiStorage Markdown; later briefs include type/source count. Distinct from concept pages, not a duplicate of the model component. Closest supplied route is [RT-RTE-document-compile](runtime.md#rt-rte-document-compile). SRC-1 `src/wiki/prompts.ts`, `src/wiki/page-writer.ts`.

> - "content": The full entity page in Markdown — what this entity is, the key facts about it from this document, and [[wikilinks]] to related concepts, other [[entities/...]], and [[summaries/{doc_name}]] — subject to the whitelist rules from the message above.
> --- `src/wiki/prompts.ts`

#### EPI-OBJ-plan
Label: Concepts plan

concepts/entities create/update/related JSON interpreted by fixed parser/code rules. Symbolic action selections in local call memory, not a retained truth theory or output approval. Material part of [RT-RTE-document-compile](runtime.md#rt-rte-document-compile) with no supplied object counterpart. SRC-1 `src/wiki/llm.ts`, `src/wiki/compiler.ts`.

> create: filterConceptItems(group.create, 'create'),
>     update: filterConceptItems(group.update, 'update'),
>     related: filterRelatedSlugs(group.related),
> --- `src/wiki/llm.ts`

#### EPI-OBJ-source-metadata
Label: Source metadata

Summary full_text and concept/entity sources fields, source counts and related path links. Symbolic path associations in Markdown/frontmatter; source-count text interpreted by planning model. Separate from natural-language page facts. No supplied object counterpart; output of [RT-RTE-document-compile](runtime.md#rt-rte-document-compile). Evidence and minimum passages are see [EPI-RTE-source-lineage](#epi-rte-source-lineage). SRC-1 `src/wiki/page-writer.ts`, `src/wiki/briefs.ts`.



### Routes

#### EPI-RTE-summary-generate
Label: Summary candidate generation

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Source text to description and summary Markdown. Configured chat model; requested coverage of source findings, no implemented fidelity evaluator. Every compilation, before planning. Result and action/state effect: Requested summary or raw-response fallback.

Route function: content transformation

Object/candidate ID: [EPI-OBJ-summary](#epi-obj-summary)

Content/update relation: truth-apt transformation: indeterminate

Transition or check target: Source text to description and summary Markdown

Evaluator/condition and domain: Configured chat model; requested coverage of source findings, no implemented fidelity evaluator

Activation and timing: Every compilation, before planning

Possible or observed result: Requested summary or raw-response fallback

Implemented force: Candidate generation only

Epistemic authority and scope: No verified license for factual reliance; source warrant unknown

Operational authority: Supplies draft to plan and page-generation calls

Behavioral-authority path: Compiler passes draft through assistant-role message; contextual force; current compilation

Evidence source ID and local anchor: SRC-1 `src/wiki/compiler.ts`, `src/wiki/prompts.ts`

Claim IDs or none: [EPI-CLM-knowledge-compiler](#epi-clm-knowledge-compiler)

Mismatch marker or none: none

Gap/limit: Without paired content, acquisition, non-ampliative reshaping, entailed derivation and ampliative conjecture remain unresolved. Failure to prove entailment is not proof of novelty.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: Without paired content, acquisition, non-ampliative reshaping, entailed derivation and ampliative conjecture remain unresolved. Failure to prove entailment is not proof of novelty.

> - "content": The full summary in Markdown. Include key concepts, findings, ideas, and [[wikilinks]] to concepts that could become cross-document concept pages
> --- `src/wiki/prompts.ts`

#### EPI-RTE-page-generate
Label: Concept and entity candidate generation

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Source/draft/selected prior body to explanation or entity facts. Configured chat model; requested synthesis and preservation, no factual comparison evaluator. After model plan; selected create/update tasks. Result and action/state effect: New page bodies/descriptions and optional entity type.

Route function: content transformation

Object/candidate ID: [EPI-OBJ-concept-page](#epi-obj-concept-page), [EPI-OBJ-entity-page](#epi-obj-entity-page)

Content/update relation: truth-apt transformation: indeterminate

Transition or check target: Source/draft/selected prior body to explanation or entity facts

Evaluator/condition and domain: Configured chat model; requested synthesis and preservation, no factual comparison evaluator

Activation and timing: After model plan; selected create/update tasks

Possible or observed result: New page bodies/descriptions and optional entity type

Implemented force: Candidate generation; no acceptance force

Epistemic authority and scope: No entailed derivation established; no accepted ampliative claim established

Operational authority: Creates candidates for structurally admitted writes

Behavioral-authority path: Compiler task arrays to model user/assistant messages; contextual force; this invocation

Evidence source ID and local anchor: SRC-1 `src/wiki/compiler.ts`, `src/wiki/prompts.ts`

Claim IDs or none: [EPI-CLM-cross-synthesis](#epi-clm-cross-synthesis)

Mismatch marker or none: none

Gap/limit: Novel cross-document synthesis is requested but non-entailment of an actual proposition is not evidenced. Prior body reaches only update tasks; other pages reach planning as briefs.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: Novel cross-document synthesis is requested but non-entailment of an actual proposition is not evidenced. Prior body reaches only update tasks; other pages reach planning as briefs.

> Integrate the new facts about this entity from document "{doc_name}" (summarized above). Rewrite the full page — do not just append. Preserve the existing structure and intent. Follow the whitelist rules from the message above for all [[wikilinks]].
> --- `src/wiki/prompts.ts`

#### EPI-RTE-summary-rewrite
Label: Summary rewrite candidate generation

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Draft summary to final candidate. Chat model asked to preserve every fact; no implementation compares facts. After generation results, before concept writes when rewriteSummary enabled. Result and action/state effect: Nonempty cleaned rewrite replaces draft; empty/error falls back.

Route function: content transformation

Object/candidate ID: [EPI-OBJ-summary](#epi-obj-summary)

Content/update relation: truth-apt transformation: indeterminate

Transition or check target: Draft summary to final candidate

Evaluator/condition and domain: Chat model asked to preserve every fact; no implementation compares facts

Activation and timing: After generation results, before concept writes when rewriteSummary enabled

Possible or observed result: Nonempty cleaned rewrite replaces draft; empty/error falls back

Implemented force: Model request plus permissive nonempty fallback

Epistemic authority and scope: Factual preservation not verified; remaining relation classifications unresolved

Operational authority: Changes persisted summary text without a semantic check

Behavioral-authority path: Compiler consumes candidate through nonempty predicate; permissive force; persisted page and later browsing

Evidence source ID and local anchor: SRC-1 `src/wiki/compiler.ts`, `src/wiki/prompts.ts`

Claim IDs or none: [EPI-CLM-summary-preservation](#epi-clm-summary-preservation)

Mismatch marker or none: Consistency request exceeds consumer input: final concept/entity bodies are not passed to rewrite.

Gap/limit: No supplied run establishes exercised behavior or benefit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: No supplied run establishes exercised behavior or benefit.

Trigger: rewriteSummary. Model proposes; code chooses nonempty cleaned rewrite or draft. No human per-output veto, expected-answer oracle or bounded experiment; open document compilation. Recovery is fallback, not factual rollback.

> - Preserve every factual claim, finding, and detail from your draft. Do NOT add or remove technical content, examples, or claims.
> --- `src/wiki/prompts.ts`

> [systemMsg, docMsg, summaryMsg, knownTargetsMsg, { role: 'user', content: SUMMARY_REWRITE_USER }],
> --- `src/wiki/compiler.ts`

#### EPI-RTE-plan-check
Label: Plan and page structural checks

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: JSON parseability; plan name/type shapes; related-page existence; nonempty page body. Deterministic parser/string/type/storage predicates; JSON and configured label/path domains only. Plan parsing and task-result construction. Result and action/state effect: Parse success/failure, filtered entries, nonempty result or Error.

Route function: check/evidence production

Object/candidate ID: [EPI-OBJ-plan](#epi-obj-plan), page candidates

Content/update relation: no content change

Transition or check target: JSON parseability; plan name/type shapes; related-page existence; nonempty page body

Evaluator/condition and domain: Deterministic parser/string/type/storage predicates; JSON and configured label/path domains only

Activation and timing: Plan parsing and task-result construction

Possible or observed result: Parse success/failure, filtered entries, nonempty result or Error

Implemented force: Check outcomes consumed by plan/task disposition

Epistemic authority and scope: License only for tested structure, not factual validity, duplicate semantics or source support

Operational authority: Enables downstream filtering/fallback/skip

Behavioral-authority path: Compiler consumes parsed values/errors; enforcing structural gate; current invocation

Evidence source ID and local anchor: SRC-1 `src/wiki/llm.ts`, `src/wiki/compiler.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: Counterexample to universal strict JSON admission: malformed page JSON falls back to raw text; nonempty raw prose can pass.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: Counterexample to universal strict JSON admission: malformed page JSON falls back to raw text; nonempty raw prose can pass.

> if (!content.trim()) {
>       throw new Error(`Empty content for concept ${name}`);
>     }
> --- `src/wiki/compiler.ts:201-220`

> return { brief: '', content: raw, obj: null };
> --- `src/wiki/llm.ts`

#### EPI-RTE-plan-dispose
Label: Plan and page operational disposition

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Whether to schedule tasks, retain a page candidate, skip a failure or use fallback. Compiler consumes structural outcomes; models propose tasks, code admits shapes; domain is task eligibility. After checks and task results. Result and action/state effect: Filtered task sets; failed pages skipped; fallback summary/index for empty/unparseable plan.

Route function: disposition/acceptance

Object/candidate ID: [EPI-OBJ-plan](#epi-obj-plan), page candidates

Content/update relation: non-truth-apt policy/content update: create/update/related task selection

Transition or check target: Whether to schedule tasks, retain a page candidate, skip a failure or use fallback

Evaluator/condition and domain: Compiler consumes structural outcomes; models propose tasks, code admits shapes; domain is task eligibility

Activation and timing: After checks and task results

Possible or observed result: Filtered task sets; failed pages skipped; fallback summary/index for empty/unparseable plan

Implemented force: Enforcing operational admission, not epistemic acceptance

Epistemic authority and scope: No evidence-consuming decision against a truth criterion, intended claim use and scope

Operational authority: Schedules writes, removes failed candidates, permits terminal completion despite failures

Behavioral-authority path: Compiler branching/result loops; enforcing/permissive force; current invocation and downstream storage

Evidence source ID and local anchor: SRC-1 `src/wiki/compiler.ts`, `src/wiki/llm.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: No supplied run establishes exercised behavior or benefit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: No supplied run establishes exercised behavior or benefit.

Trigger: compile input. Model proposes selections/bodies; code decides structurally; watcher user may veto input only. No answer oracle; open requests. Guidance is source, instructions, briefs and selected old body. Rejection filters and skips; recovery fallback/re-run, no whole-ingest rollback.

> if (result instanceof Error) {
>       console.warn(`  Entity generation failed: ${result.message}`);
>       continue;
>     }
> --- `src/wiki/compiler.ts`

#### EPI-RTE-link-check
Label: Wikilink membership checking

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Target membership/canonicalization in supplied knownTargets. Set membership and normalized lookup; domain is passed whitelist, not eventual filesystem existence or meaning. Before generated body writes. Result and action/state effect: Exact/canonical recognized target or ghost target.

Route function: check/evidence production

Object/candidate ID: Generated page and summary links

Content/update relation: no content change

Transition or check target: Target membership/canonicalization in supplied knownTargets

Evaluator/condition and domain: Set membership and normalized lookup; domain is passed whitelist, not eventual filesystem existence or meaning

Activation and timing: Before generated body writes

Possible or observed result: Exact/canonical recognized target or ghost target

Implemented force: Classification consumed immediately by replacement

Epistemic authority and scope: Only whitelist-relative admissibility

Operational authority: Determines links kept/canonicalized/removed

Behavioral-authority path: stripGhostWikilinks replacement callback; enforcing force; current body

Evidence source ID and local anchor: SRC-1 `src/wiki/wikilink.ts`, `src/wiki/compiler.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: Whitelist includes planned pages before success. Failure of a planned task can leave an admitted link without an actual target.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: Whitelist includes planned pages before success. Failure of a planned task can leave an admitted link without an actual target.

> if (knownTargets.has(targetPart)) {
>       return match;
>     }
> --- `src/wiki/wikilink.ts`

> const canonical = index.get(normalizeTarget(targetPart));
> --- `src/wiki/wikilink.ts`

#### EPI-RTE-link-reshape
Label: Wikilink cleanup transformation

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Recognized/unknown link markup to canonical link/plain text. Deterministic replacement; classification from link-check, not a semantic evaluator. During stripGhostWikilinks, before persistence. Result and action/state effect: Body with unknown links rendered as alias or normalized stem.

Route function: content transformation

Object/candidate ID: Generated page and summary links

Content/update relation: truth-apt transformation: non-ampliative reshaping

Transition or check target: Recognized/unknown link markup to canonical link/plain text

Evaluator/condition and domain: Deterministic replacement; classification from link-check, not a semantic evaluator

Activation and timing: During stripGhostWikilinks, before persistence

Possible or observed result: Body with unknown links rendered as alias or normalized stem

Implemented force: Enforcing output formatting; ghosts array not used as a quality decision

Epistemic authority and scope: No truth license from link markup cleanup; no new explanatory proposition required by this code

Operational authority: Replaces bad markup without rejecting candidate body

Behavioral-authority path: Compiler consumes returned content; enforcing textual force; persisted body

Evidence source ID and local anchor: SRC-1 `src/wiki/wikilink.ts`, `src/wiki/compiler.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: Concrete deduction: with knownTargets={concepts/alpha}, input See [[concepts/missing-topic]] becomes See missing topic; ghosts contains concepts/missing-topic. No target execution. Alias/normalization can change reference identity; this licenses no universal semantic-preservation claim.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: Concrete deduction: with knownTargets={concepts/alpha}, input See [[concepts/missing-topic]] becomes See missing topic; ghosts contains concepts/missing-topic. No target execution. Alias/normalization can change reference identity; this licenses no universal semantic-preservation claim.

> ghosts.push(targetPart);
>     if (aliasPart) {
>       return aliasPart;
>     }
>     const stem = targetPart.split('/').pop() ?? targetPart;
>     return stem.replace(/[-_]/g, ' ');
> --- `src/wiki/wikilink.ts`

#### EPI-RTE-page-retain
Label: Candidate page retention and overwrite

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Current admitted body to stored summary/concept/entity Markdown. Writers and storage; file/frontmatter domains, not semantic acceptance. After cleanup; entities, summary, concepts then backlink/index/log work. Result and action/state effect: Persistent candidates; old body replaced.

Route function: retention

Object/candidate ID: [EPI-OBJ-summary](#epi-obj-summary), [EPI-OBJ-concept-page](#epi-obj-concept-page), [EPI-OBJ-entity-page](#epi-obj-entity-page)

Content/update relation: no content change

Transition or check target: Current admitted body to stored summary/concept/entity Markdown

Evaluator/condition and domain: Writers and storage; file/frontmatter domains, not semantic acceptance

Activation and timing: After cleanup; entities, summary, concepts then backlink/index/log work

Possible or observed result: Persistent candidates; old body replaced

Implemented force: Physical write enforcing persistence; no knowledge-quality gate

Epistemic authority and scope: Retention does not license claim truth or preservation

Operational authority: Makes content browseable and available to future model context

Behavioral-authority path: WikiStorage writes; enforcing storage force; across compilations until replacement

Evidence source ID and local anchor: SRC-1 `src/wiki/compiler.ts`, `src/wiki/page-writer.ts`

Claim IDs or none: [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy)

Mismatch marker or none: No implemented manual-edit conflict veto; concept create can overwrite an existing path without update preservation branch.

Gap/limit: No supplied run establishes exercised behavior or benefit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: Stored descriptions feed planning; selected previous bodies feed update-generation calls via page-consume.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: Replacement by later compilation or external host edits; no compiler expiry/version rollback.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: No supplied run establishes exercised behavior or benefit.

Code admits generation results and writes; human input choice/approval is not output review. No truth oracle. Source/instructions guide candidates. Failed tasks skipped; later write errors may leave earlier writes. Entity writer chooses isUpdate by current existence even for a create task; this preserves metadata, not necessarily prior body semantics.

> const isUpdate = await storage.exists(entityPath(safe));
>     await writeEntity(storage, item.name, content, sourceFile, isUpdate, item.brief, item.type);
> --- `src/wiki/compiler.ts`

#### EPI-RTE-page-consume
Label: Retained page selection and consumption

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: All retained descriptions/previews to planning; model-selected body to update. Code enumerates briefs; planning model selects update entries; code loads sanitized paths. Each later document compilation. Result and action/state effect: Brief strings and selected old bodies become model inputs.

Route function: operational admission/selection/consumption

Object/candidate ID: [EPI-OBJ-concept-page](#epi-obj-concept-page), [EPI-OBJ-entity-page](#epi-obj-entity-page)

Content/update relation: truth-apt transformation: non-ampliative reshaping

Transition or check target: All retained descriptions/previews to planning; model-selected body to update

Evaluator/condition and domain: Code enumerates briefs; planning model selects update entries; code loads sanitized paths

Activation and timing: Each later document compilation

Possible or observed result: Brief strings and selected old bodies become model inputs

Implemented force: Contextual/permissive reliance; no authority ranking by evidence quality

Epistemic authority and scope: Source warrant unknown; source count is association count, not corroboration

Operational authority: Prior candidates can influence task selection and replacement prose

Behavioral-authority path: Planning/update model via user messages; contextual force; subsequent compilations

Evidence source ID and local anchor: SRC-1 `src/wiki/briefs.ts`, `src/wiki/compiler.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: No supplied run establishes exercised behavior or benefit.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: Descriptions or flattened 150-character previews from prior pages; selected update bodies with frontmatter removed.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: All concept/entity Markdown briefs enumerated; model plan chooses update names; old body loaded only for those tasks.
- Invalidation or expiry: Current page version read afresh; no explicit stale/accepted/withdrawn status filter.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: No supplied run establishes exercised behavior or benefit.

Model proposes names; code filters shapes, not evidential quality. No answer oracle, quality-triggered experiment or semantic veto. Open compilation. Prior body is guidance, not a checked premise. Context is per-task, not accumulated conversation.

> const brief = resolveDescription(fm) || bodyPreview(text);
>     if (brief) {
>       lines.push(`- ${file.slice(0, -3)}: ${brief}`);
>     }
> --- `src/wiki/briefs.ts`

> existingContent = parts ? parts.body.trim() : rawText;
> --- `src/wiki/compiler.ts:221-253`

#### EPI-RTE-source-lineage
Label: Source associations and navigation maintenance

Part of: [RT-RTE-document-compile](runtime.md#rt-rte-document-compile)

This function is a material part of the supplied compilation container, not a replacement for its valid combined account.

Endpoints/progression and owner: Bodies and document/page identities to source paths, related links, index descriptions and operation log. Code adds path associations and copied descriptions; no support verification. During writes and related/backlink/index/log maintenance. Result and action/state effect: Summary full_text, page sources, reciprocal links, refreshed index and ingest log.

Route function: lineage/freshness/recovery

Object/candidate ID: [EPI-OBJ-source-metadata](#epi-obj-source-metadata)

Content/update relation: truth-apt transformation: non-ampliative reshaping

Transition or check target: Bodies and document/page identities to source paths, related links, index descriptions and operation log

Evaluator/condition and domain: Code adds path associations and copied descriptions; no support verification

Activation and timing: During writes and related/backlink/index/log maintenance

Possible or observed result: Summary full_text, page sources, reciprocal links, refreshed index and ingest log

Implemented force: Stored navigation/provenance cues, no acceptance or support-check result

Epistemic authority and scope: Association only: no claim-to-evidence mapping, no independent endorsement from source count

Operational authority: Enables navigation and source-count cues on subsequent planning

Behavioral-authority path: Human browser and planning model via Markdown/frontmatter/briefs; contextual force; later compilations/browsing

Evidence source ID and local anchor: SRC-1 `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`, `src/wiki/briefs.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: full_text points at sources/{docName}.md but inspected callers/compiler never copy sourceContent there. Folder creation is not source preservation. External prepopulation possible; actual resolvability unknown. Related-only linking can add a source association without body synthesis.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: Entity briefs include sources.length; descriptions feed planning; index/log are not read by compiler as factual evaluators.
- Delegated visibility: Model/provider receives only the explicit inputs named for this function.
- Selection predicate: Compiler code selects this function in its finite compilation sequence.
- Invalidation or expiry: Associations retained/merged on update; creation may reset metadata; no claim withdrawal/version lineage.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: full_text points at sources/{docName}.md but inspected callers/compiler never copy sourceContent there. Folder creation is not source preservation. External prepopulation possible; actual resolvability unknown. Related-only linking can add a source association without body synthesis.

> fmLines.push(frontmatter.kvLine('full_text', `sources/${docName}.${ext}`));
> --- `src/wiki/page-writer.ts`

> const sourceFile = `summaries/${docName}.md`;
> --- `src/wiki/compiler.ts`

> const sources = Array.isArray(fm.sources) ? fm.sources : [];
> --- `src/wiki/briefs.ts`

#### EPI-RTE-probe-check
Label: Connection probe response checks

Distinct from [RT-RTE-document-compile](runtime.md#rt-rte-document-compile): this exported or UI-triggered operation is not an internal compiler stage. Closest supplied findings mention this surface but do not declare this function separately; no supplied route counterpart after comparison.

Endpoints/progression and owner: LLM response completion; STT HTTP success and nonempty transcription. Provider response plus code predicates; domain is configured service request, not factual correctness. User presses a connection-test button; outside compilation. Result and action/state effect: LLM text or exception; STT trimmed nonempty text or exception.

Route function: check/evidence production

Object/candidate ID: Probe requests/results (no retained truth claim)

Content/update relation: no content change

Transition or check target: LLM response completion; STT HTTP success and nonempty transcription

Evaluator/condition and domain: Provider response plus code predicates; domain is configured service request, not factual correctness

Activation and timing: User presses a connection-test button; outside compilation

Possible or observed result: LLM text or exception; STT trimmed nonempty text or exception

Implemented force: Consumed by UI notice, not by compiler admission

Epistemic authority and scope: At most a completed request under tested settings; LLM OK compliance not compared, STT accuracy not compared

Operational authority: Supplies success/failure branch for notice only

Behavioral-authority path: Settings UI awaits result; informational force; single probe

Evidence source ID and local anchor: SRC-1 `src/llm/client.ts`, `obsidian-plugin/src/stt-client.ts`, `obsidian-plugin/src/settings-tab.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: LLM expected token OK is prompt text, not a used answer oracle. STT has no transcript reference; nonempty requirement can reject an empty silence transcript while accepting spurious words.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Configured LLM receives Reply with exactly: OK; STT receives a generated one-second silent WAV and model.
- Selection predicate: Explicit human test button selects endpoint from current settings.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: LLM expected token OK is prompt text, not a used answer oracle. STT has no transcript reference; nonempty requirement can reject an empty silence transcript while accepting spurious words.

> return client.generate([{ role: 'user', content: 'Reply with exactly: OK' }], 'connection-test');
> --- `src/llm/client.ts`

> if (!payload.text?.trim()) {
>     throw new Error('STT returned empty transcript');
>   }
> --- `obsidian-plugin/src/stt-client.ts`

#### EPI-RTE-probe-notice
Label: Connection probe result presentation

Distinct from [RT-RTE-document-compile](runtime.md#rt-rte-document-compile): this exported or UI-triggered operation is not an internal compiler stage. Closest supplied findings mention this surface but do not declare this function separately; no supplied route counterpart after comparison.

Endpoints/progression and owner: Probe return/error to UI success/failure message. Settings UI try/catch; return versus exception, not result truth. Immediately after explicit test. Result and action/state effect: LLM OK/STT OK notice with first 80 characters, or failure notice.

Route function: other — describe

Object/candidate ID: Probe requests/results

Content/update relation: no content change

Transition or check target: Probe return/error to UI success/failure message

Evaluator/condition and domain: Settings UI try/catch; return versus exception, not result truth

Activation and timing: Immediately after explicit test

Possible or observed result: LLM OK/STT OK notice with first 80 characters, or failure notice

Implemented force: Advisory only; no settings rollback or compilation permission gate

Epistemic authority and scope: Notice does not establish exact OK response, transcription accuracy or future reliability

Operational authority: Informs operator; does not block/enable later compile in code

Behavioral-authority path: Human through Obsidian Notice; advisory force; immediate session

Evidence source ID and local anchor: SRC-1 `obsidian-plugin/src/settings-tab.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: No downstream automatic consumer changes trust, policy or model parameters.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: inapplicable — current-call material is not itself retained by this function.
- Delegated visibility: Human sees response prefix or error message.
- Selection predicate: Try/catch branches on returned promise or exception.
- Invalidation or expiry: inapplicable — this function owns no independent retained version.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: No downstream automatic consumer changes trust, policy or model parameters.

> const text = await testLlmConnection(this.plugin.settings);
>             new Notice(`LLM OK: ${text.slice(0, 80)}`);
> --- `obsidian-plugin/src/settings-tab.ts`

#### EPI-RTE-helper-access
Label: Exported file helper access

Distinct from [RT-RTE-document-compile](runtime.md#rt-rte-document-compile): this exported or UI-triggered operation is not an internal compiler stage. Closest supplied findings mention this surface but do not declare this function separately; no supplied route counterpart after comparison.

Endpoints/progression and owner: Requested paths to read content or caller-supplied writes. Lexical root checks and subdirectory allowlists; domain path access, not source truth. Only if an external caller invokes exported helpers; not wired to shipped compiler model tools. Result and action/state effect: File/page/image return, denial/missing messages or write acknowledgment.

Route function: operational admission/selection/consumption

Object/candidate ID: Caller-supplied file/page/image content

Content/update relation: truth-apt transformation: acquisition/import

Transition or check target: Requested paths to read content or caller-supplied writes

Evaluator/condition and domain: Lexical root checks and subdirectory allowlists; domain path access, not source truth

Activation and timing: Only if an external caller invokes exported helpers; not wired to shipped compiler model tools

Possible or observed result: File/page/image return, denial/missing messages or write acknowledgment

Implemented force: Enforcing lexical path rules; no semantic evaluator

Epistemic authority and scope: Imported source warrant unknown; write acknowledgment licenses no factual reliance

Operational authority: Direct file access/write within function rules; no inspected query-agent activation

Behavioral-authority path: External API caller through return strings/image union; access force; invocation and writes retained

Evidence source ID and local anchor: SRC-1 `src/wiki/tools.ts`, `src/llm/client.ts`

Claim IDs or none: none

Mismatch marker or none: none

Gap/limit: Lexical checks do not prove realpath confinement against symlinks. Helper existence cannot establish an actual later consumer or knowledge evaluator.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current-call result or continuation as described above.
- Later read-back: Files can be reread by helper caller; shipped compiler may later see helper-written concept/entity pages if put in its wiki root. Actual caller and accumulated state uninspected.
- Delegated visibility: Returns selected JSON page content/images or full requested text to caller; no model-tools registration in inspected client.
- Selection predicate: Caller path/page selector; getWikiPageContent filters entries by requested page number; writeKbFile limits wiki/explorations or output.
- Invalidation or expiry: Writes overwrite; no semantic approval or built-in version rollback.
- Activation or effect: Implemented delivery, selection or transformation as stated above; changed behavior and benefit unobserved.
- Evidence limits: Lexical checks do not prove realpath confinement against symlinks. Helper existence cannot establish an actual later consumer or knowledge evaluator.

Caller proposes content; code permits lexically confined writeWikiFile or allowlisted writeKbFile. No answer oracle, per-content human check or improvement experiment. Reads do not establish an implemented query runtime.

> fs.writeFileSync(fullPath, content, 'utf-8');
>   return `Written: ${relativePath}`;
> --- `src/wiki/tools.ts:49-57`

### Claims

#### EPI-CLM-knowledge-compiler
Label: Knowledge compiler

Claimed operation: local-first source-to-structured/interlinked-wiki compilation. No supplied duplicate claim; broader than [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy), which concerns manual edits. SRC-1 `README.md`, doctrine/design.

> Local-first LLM knowledge compiler for Obsidian. Drop notes or record voice into `raw/`; the wiki compiler turns them into a structured, interlinked wiki under `wiki/`.
> --- `README.md`

#### EPI-CLM-cross-synthesis
Label: Cross-document synthesis

Claimed operation: concept pages synthesize across documents, using prior concept/entity context. No supplied duplicate claim; the compilation route describes its implementation but is not a claim record. SRC-1 `templates/wiki/AGENTS.md`, doctrine/design; minimum passage see [EPI-OBJ-concept-page](#epi-obj-concept-page).

#### EPI-CLM-summary-preservation
Label: Summary preservation

Claimed operation: preserve every draft claim/detail while rewriting consistently with concept pages. This is a prompt-level requested behavior, distinct from [RT-CLM-conflict-policy](runtime.md#rt-clm-conflict-policy)'s manual-edit conflict promise. SRC-1 `src/wiki/prompts.ts`, doctrine/design; preservation quote see [EPI-RTE-summary-rewrite](#epi-rte-summary-rewrite).

> Task: Rewrite the summary you wrote above into a final version that is consistent with the concept pages now in the wiki (per the whitelist message above).
> --- `src/wiki/prompts.ts`

### Evidenced absences

#### EPI-ABS-quality-gate
Label: Factual quality gate

- implementation conclusion status: absent

Searched boundary: SRC-1 at 11446997423e88177dba62d6a3d5c1e8b4886c62; complete direct reads of `src/wiki/compiler.ts`, `src/wiki/llm.ts`, `src/wiki/prompts.ts`, `src/wiki/page-writer.ts`, `src/wiki/index-writer.ts`, `src/wiki/briefs.ts`, `src/wiki/wikilink.ts`, `src/wiki/tools.ts`, `src/compiler-api.ts`, `src/cli/compile.ts`, `src/llm/client.ts`, plugin command/watcher/approval/STT paths and `package.json`. Scoped search of `src/wiki`, `src/cli`, `src/llm`, plugin `src`, README and template for check, valid, test, reject, accept, conflict, truth, accur, knowledge, export and command, followed by dispatch and consumer tracing. Supplied release route adds a build-only path, not a factual evaluator. No supplied absence counterpart.

These paths expose structural/path/nonempty checks, upstream path approval, prompt preservation policy, writes, later context reuse and advisory service probes. None implements an evidence-consuming acceptance decision naming a factual criterion, intended claim use and scope; none implements refutation-directed changed reliance/withdrawal or lifecycle integration after such acceptance. This bounded absence does not deny possible human evaluation in external Obsidian use or opaque model processing. It prevents identifying accepted knowledge production or epistemic lifecycle integration from the shipped loop. Positive implementation witnesses and countercases are retained in the route records rather than interpreting a search miss as proof.

> "test": "echo \"Error: no test specified\" && exit 1",
> --- `package.json`

### Behavioral-authority paths

none declared in this member. The route records specify their consumer, channel, force and horizon; supplied [RT-BAP-retained-pages](runtime.md#rt-bap-retained-pages) and [RT-BAP-compiler-instructions](runtime.md#rt-bap-compiler-instructions) retain their identities. No separate numerical-parameter authority route is inferred from opaque providers.
