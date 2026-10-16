---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Continuity's memory, narrative, research and Threads routes: what their checks license and what later consumers receive."
run-id: AAS-2026-10-14-continuity-3e490e1d39f0-01
reviewed-boundary: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
---

# Continuity epistemic report

## Source-and-claim boundary

The question is whether conversation, imported content, synthesis and plugin evaluation become warranted knowledge or only operationally admitted candidates. The [boundary and Source register](boundary.md#source-register) fix SRC-1 and the whole-system functional scope. This report examines separate routes, not a system-wide knowledge-production score. No source, target code, test or service was executed. Implementation deductions below are not observed operation.

Direct inspection adds the files named below to the boundary's initial inspection. Supplied runtime records supply their own passages and are provisional wherever direct inspection refines a container into parts. No supersession is needed: the runtime's broad containers remain valid. The memory and workflow members were not supplied; comparisons are with the runtime only. Independent parametric components remain as assessed in [RT-CMP-ai-client](runtime.md#rt-cmp-ai-client) and [RT-CMP-ai-evaluator](runtime.md#rt-cmp-ai-evaluator): remote weights and endpoint identity are opaque, and no local training follows from retained text.

| Entry point / operation | SRC-1 source path | Inspection basis and coverage / limit |
|---|---|---|
| Desktop send and saved output | `providers/chat-provider.tsx` | Supplied [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat); direct narrative prompt construction read. Canvas/journal/artifact factual admission semantics are not independently audited; prevents a complete negative about all workspace content. |
| Desktop remember / recall / forget | `lib/ai/memory-tools.ts`, `lib/db/memories.ts`, `lib/db/memory-db.ts` | Direct normalization, CRUD, schema/default and active-read inspection; [EPI-RTE-key-reshaping](#epi-rte-key-reshaping), [EPI-RTE-memory-retention](#epi-rte-memory-retention), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal). |
| MCP CLI and tool registrations | `server/bin/cli.mjs`, `server/dist/server.mjs`, `server/tools/memory-tools.ts`, `server/tools/narrative-tools.ts`, `server/tools/lifecycle-tools.ts`, `server/tools/relationship-tools.ts` | Direct CLI import, bundle footer/registered names, source schemas and callbacks. Footer registers six modules and declares 17 tools, including learning/narrative/link/history paths. Targeted bundle inspection is not whole-bundle parity. Project/search modules inspected by scoped registration search and supplied boundary, not a full semantic audit; prevents complete MCP negative. |
| MCP database mutations and relations | `server/db/memories.ts`, `server/db/learnings.ts`, `server/db/relationships.ts` | Direct write/update/archive/import, observation insert and link/active-linked-read inspection; [EPI-RTE-signal-retention](#epi-rte-signal-retention), [EPI-RTE-relation-retention](#epi-rte-relation-retention). |
| Scheduled / manual narrative synthesis | `lib/ai/narrative-synthesis.ts`, `providers/memories-provider.tsx` | Direct input construction, parse fallback, save/absorption, scheduler, read-back and UI launch/manual caller inspection; narrative parts below. |
| Research launch, findings, gap check and completion | `lib/ai/research-engine.ts`, `providers/chat-provider.tsx` | Direct analyzer, fallback, gap and synthesizer construction; supplied [RT-RTE-deep-research](runtime.md#rt-rte-deep-research) supplies launch/completion persistence. |
| Vault scan index and incremental update | `lib/vault/memory.ts` | Direct formatter, ranking and update inspection; [EPI-RTE-vault-projection](#epi-rte-vault-projection). Scanner truth/fidelity and write callers not independently audited; cannot certify the index against actual files. |
| Plugin RPC and foreground delivery | `plugin-host/src/index.ts`, `lib/plugins/manager.ts` | Supplied [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission) and [RT-CLM-plugin-controls](runtime.md#rt-clm-plugin-controls); not re-audited here. Host registration is not demonstrated foreground prompt/tool delivery. |
| Threads cron, registered tools and review endpoints | `plugins/continuity-threads-engagement/src/ai-evaluator.ts`, `plugins/continuity-threads-engagement/src/cron.ts`, `plugins/continuity-threads-engagement/src/index.ts`, `plugins/continuity-threads-engagement/src/ui-server.ts` | Direct relevance/draft inference, threshold, ad-hoc search/draft handlers, regeneration/status/edit/select/approve paths. Scheduled and ad-hoc consumers differ. |
| Org event subscriptions, search and synchronization | `plugins/continuity-org-memory-sync/src/index.ts`, `plugins/continuity-org-memory-sync/src/sync-engine.ts`, `org-server/src/routes/memories-push.ts` | Scoped event/tool search and supplied [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion). Schema/auth/time guards do not check memory truth; intended local pull target remains mismatched. Full event production and search semantics uninspected. |
| Developer-agent maintenance | `CLAUDE.md`, `claude_docs/` | Boundary's supplied doctrine inspection only. Separate development procedure, not in-app synthesis. No exercised criticism/revision conclusion. |
| Other model/web/vault/MCP tools, briefings and UI edits | `lib/ai/`, `lib/services/briefing-service.ts`, `components/` | Runtime dispatch/boundary coverage only. Detailed evaluators and arbitrary external tool semantics unassessed; prevents a system-complete negative or inventory of every factual claim. |

Excluded external provider internals, MCP clients/tools, live vaults and Threads API behavior prevent judgments of input truth, actual compliance, provider quality and live effects. Deliberately excluded historical plugin databases cannot supply route provenance. Missing registered observed runs prevents claims of exercised acceptance, reliable synthesis or benefit; missing interventions/comparisons prevents causal learning or improvement attribution. No retained candidate instance is treated as evidence that a particular route produced it.

Consequential warrant/design claims are [EPI-CLM-conversation-understanding](#epi-clm-conversation-understanding), [EPI-CLM-source-groundtruth](#epi-clm-source-groundtruth) and [EPI-CLM-research-quality](#epi-clm-research-quality). These are source declarations, not accepted conclusions.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID / local anchor | Gap / limit |
|---|---|---|---|---|
| [RT-OBJ-current-messages](runtime.md#rt-obj-current-messages) | see record | Desktop working context | SRC-1 `providers/chat-provider.tsx` | see record; no output truth oracle |
| [EPI-OBJ-memories](#epi-obj-memories) | see record | Persistent remembered statements | SRC-1 `lib/db/memories.ts` | Actual truth and authorship unobserved |
| [EPI-OBJ-memory-source](#epi-obj-memory-source) | see record | Source label affecting synthesis reliance | SRC-1 `server/tools/memory-tools.ts` | Caller label is not authenticated provenance |
| [EPI-OBJ-learnings](#epi-obj-learnings) | see record | Observation signals | SRC-1 `server/db/learnings.ts` | Correction label does not establish a tested correction |
| [EPI-OBJ-memory-links](#epi-obj-memory-links) | see record | Relationship assertions | SRC-1 `server/db/relationships.ts` | Existence check is not relation validation |
| [EPI-OBJ-narratives](#epi-obj-narratives) | see record | Understanding briefing | SRC-1 `lib/ai/narrative-synthesis.ts` | Semantic change and confidence calibration undetermined |
| [EPI-OBJ-research-findings](#epi-obj-research-findings) | see record | Findings/report candidates | SRC-1 `lib/ai/research-engine.ts` | Full source linkage is not passed to final synthesizer |
| [EPI-OBJ-relevance-result](#epi-obj-relevance-result) | see record | Relevance assessment | SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` | Persona-fit judgment, not post truth |
| [EPI-OBJ-draft-result](#epi-obj-draft-result) | see record | Proposed replies | SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` | May contain claims, questions or non-truth-apt speech; no instance supplied |
| [EPI-OBJ-vault-memory](#epi-obj-vault-memory) | see record | Vault overview | SRC-1 `lib/vault/memory.ts` | Selected excerpt, not whole vault or endorsed knowledge |
| [RT-OBJ-plugin-session](runtime.md#rt-obj-plugin-session) | see record | Session authority/registered prompts | SRC-1 `plugin-host/src/server.ts` | see record; foreground delivery unresolved |

## Authority-route ledger

Route ID: [EPI-RTE-key-reshaping](#epi-rte-key-reshaping)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memories](#epi-obj-memories)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Caller key/value before setMemory
Evaluator/condition and domain: TypeScript lowercase/trim/whitespace replacement; string domain
Activation and timing: see [EPI-RTE-key-reshaping](#epi-rte-key-reshaping); operation unobserved
Possible or observed result: Normalized key and trimmed content
Implemented force: see [EPI-RTE-key-reshaping](#epi-rte-key-reshaping)
Epistemic authority and scope: No new factual warrant; value is retained as caller/model proposal
Operational authority: Normalized identifier selects the global storage target
Behavioral-authority path: see [EPI-RTE-key-reshaping](#epi-rte-key-reshaping); horizon: Current call; durable consequences through memory writes
Evidence source ID and local anchor: SRC-1 `lib/ai/memory-tools.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-key-reshaping](#epi-rte-key-reshaping)
Gap/limit: see [EPI-RTE-key-reshaping](#epi-rte-key-reshaping)

Route ID: [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memories](#epi-obj-memories), [EPI-OBJ-memory-source](#epi-obj-memory-source)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Proposed memory statement and source metadata
Evaluator/condition and domain: Desktop string checks; MCP schema/enums and DB CRUD; storage domain
Activation and timing: see [EPI-RTE-memory-retention](#epi-rte-memory-retention); operation unobserved
Possible or observed result: Created/updated/versioned row; import transaction or error
Implemented force: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Epistemic authority and scope: Imported source warrant unknown; versioning is not acceptance
Operational authority: Makes candidate eligible for later active retrieval
Behavioral-authority path: see [EPI-RTE-memory-retention](#epi-rte-memory-retention); horizon: Across later sends/MCP requests until archive or replacement
Evidence source ID and local anchor: SRC-1 `server/db/memories.ts` (implementation)
Claim IDs: [EPI-CLM-source-groundtruth](#epi-clm-source-groundtruth)
Mismatch marker: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Gap/limit: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)

Route ID: [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memories](#epi-obj-memories)
Content/update relation: no content change
Transition or check target: Eligibility of a stored memory for active reads
Evaluator/condition and domain: Caller/model forget request and archival SQL; active-row domain
Activation and timing: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal); operation unobserved
Possible or observed result: Archived row excluded from inspected active memory reads
Implemented force: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)
Epistemic authority and scope: No judgment that content is false; withholding active use only
Operational authority: Stops direct active recall/context selection, not every derivative
Behavioral-authority path: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal); horizon: Later active reads; old narratives/history can outlive archival
Evidence source ID and local anchor: SRC-1 `lib/db/memories.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)
Gap/limit: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)

Route ID: [EPI-RTE-signal-retention](#epi-rte-signal-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-learnings](#epi-obj-learnings)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller observation about user/preferences/patterns
Evaluator/condition and domain: MCP enum/range schema then SQL insert; record-shape domain
Activation and timing: see [EPI-RTE-signal-retention](#epi-rte-signal-retention); operation unobserved
Possible or observed result: Pending learning row with optional source ids and confidence
Implemented force: see [EPI-RTE-signal-retention](#epi-rte-signal-retention)
Epistemic authority and scope: Imported observation warrant unknown; label correction is not criticism evidence
Operational authority: Pending signals can trigger and supply later synthesis
Behavioral-authority path: see [EPI-RTE-signal-retention](#epi-rte-signal-retention); horizon: Until absorbed; observations persist for list/display
Evidence source ID and local anchor: SRC-1 `server/db/learnings.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-signal-retention](#epi-rte-signal-retention)
Gap/limit: see [EPI-RTE-signal-retention](#epi-rte-signal-retention)

Route ID: [EPI-RTE-relation-retention](#epi-rte-relation-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-links](#epi-obj-memory-links)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller claim that two memories contradict/supersede/depend on one another
Evaluator/condition and domain: Endpoint-existence SQL and uniqueness constraint; identifier domain
Activation and timing: see [EPI-RTE-relation-retention](#epi-rte-relation-retention); operation unobserved
Possible or observed result: Stored typed edge or error
Implemented force: see [EPI-RTE-relation-retention](#epi-rte-relation-retention)
Epistemic authority and scope: Only endpoints/existing edge constraints checked; relation truth unknown
Operational authority: Linked-memory query exposes edge and active counterpart
Behavioral-authority path: see [EPI-RTE-relation-retention](#epi-rte-relation-retention); horizon: Later MCP/UI link reads
Evidence source ID and local anchor: SRC-1 `server/db/relationships.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-relation-retention](#epi-rte-relation-retention)
Gap/limit: see [EPI-RTE-relation-retention](#epi-rte-relation-retention)

Route ID: [EPI-RTE-narrative-generation](#epi-rte-narrative-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-narratives](#epi-obj-narratives)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Memories, pending signals and prior narrative to new briefing
Evaluator/condition and domain: Configured AIClient under synthesis instructions; user-model domain
Activation and timing: see [EPI-RTE-narrative-generation](#epi-rte-narrative-generation); operation unobserved
Possible or observed result: Candidate JSON/text narrative and self-assigned confidence
Implemented force: see [EPI-RTE-narrative-generation](#epi-rte-narrative-generation)
Epistemic authority and scope: No added warrant merely from model synthesis; inherited warrant unknown
Operational authority: Proposes future system-message context
Behavioral-authority path: see [EPI-RTE-narrative-generation](#epi-rte-narrative-generation); horizon: Current synthesis; candidate may persist across sessions
Evidence source ID and local anchor: SRC-1 `lib/ai/narrative-synthesis.ts` (implementation)
Claim IDs: [EPI-CLM-source-groundtruth](#epi-clm-source-groundtruth)
Mismatch marker: see [EPI-RTE-narrative-generation](#epi-rte-narrative-generation)
Gap/limit: see [EPI-RTE-narrative-generation](#epi-rte-narrative-generation)

Route ID: [EPI-RTE-narrative-format](#epi-rte-narrative-format)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-narratives](#epi-obj-narratives)
Content/update relation: no content change
Transition or check target: Response syntax as JSON, not propositions about user
Evaluator/condition and domain: JSON.parse after optional fence stripping; syntax domain
Activation and timing: see [EPI-RTE-narrative-format](#epi-rte-narrative-format); operation unobserved
Possible or observed result: Parsed value or exception, followed by raw-text fallback
Implemented force: see [EPI-RTE-narrative-format](#epi-rte-narrative-format)
Epistemic authority and scope: Syntactic parse license only; neither structure assertion nor factual acceptance
Operational authority: Parse failure does not block all narrative admission
Behavioral-authority path: see [EPI-RTE-narrative-format](#epi-rte-narrative-format); horizon: Current synthesis
Evidence source ID and local anchor: SRC-1 `lib/ai/narrative-synthesis.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-narrative-format](#epi-rte-narrative-format)
Gap/limit: see [EPI-RTE-narrative-format](#epi-rte-narrative-format)

Route ID: [EPI-RTE-narrative-retention](#epi-rte-narrative-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-narratives](#epi-obj-narratives), [EPI-OBJ-learnings](#epi-obj-learnings)
Content/update relation: no content change
Transition or check target: Generated/parsed/fallback content to narrative row
Evaluator/condition and domain: App SQL save after model call; no evidenced factual acceptance criterion
Activation and timing: see [EPI-RTE-narrative-retention](#epi-rte-narrative-retention); operation unobserved
Possible or observed result: Versioned current briefing saved; pending learning flags set absorbed
Implemented force: see [EPI-RTE-narrative-retention](#epi-rte-narrative-retention)
Epistemic authority and scope: Retention grants no epistemic acceptance; confidence is generated/capped
Operational authority: Makes current content available for later prompt and next synthesis
Behavioral-authority path: see [EPI-RTE-narrative-retention](#epi-rte-narrative-retention); horizon: Across sessions until subsequent update
Evidence source ID and local anchor: SRC-1 `lib/ai/narrative-synthesis.ts` (implementation)
Claim IDs: [EPI-CLM-source-groundtruth](#epi-clm-source-groundtruth)
Mismatch marker: see [EPI-RTE-narrative-retention](#epi-rte-narrative-retention)
Gap/limit: see [EPI-RTE-narrative-retention](#epi-rte-narrative-retention)

Route ID: [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-narratives](#epi-obj-narratives)
Content/update relation: no content change
Transition or check target: Current narrative content and confidence metadata
Evaluator/condition and domain: App read/prompt construction; presence predicate, not truth evaluation
Activation and timing: see [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption); operation unobserved
Possible or observed result: What I Know About You section in system message, or omission on failure
Implemented force: see [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption)
Epistemic authority and scope: Operational context, not certified knowledge; confidence label is not measured accuracy
Operational authority: May guide model response/tool proposals before another check
Behavioral-authority path: see [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption); horizon: Current send and repeated later sends
Evidence source ID and local anchor: SRC-1 `providers/chat-provider.tsx` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption)
Gap/limit: see [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption)

Route ID: [EPI-RTE-research-findings](#epi-rte-research-findings)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-findings](#epi-obj-research-findings)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Search/source findings to final report/summary
Evaluator/condition and domain: External search/provider plus configured AIClient; open research domain
Activation and timing: see [EPI-RTE-research-findings](#epi-rte-research-findings); operation unobserved
Possible or observed result: Findings, report and summary, including fallback excerpts
Implemented force: see [EPI-RTE-research-findings](#epi-rte-research-findings)
Epistemic authority and scope: Acquired source warrant unknown; model-generated claim warrant unestablished
Operational authority: Completion can persist report/summary without per-content review
Behavioral-authority path: see [EPI-RTE-research-findings](#epi-rte-research-findings); horizon: Current pipeline; retained report/summary later available
Evidence source ID and local anchor: SRC-1 `lib/ai/research-engine.ts` (implementation)
Claim IDs: [EPI-CLM-research-quality](#epi-clm-research-quality)
Mismatch marker: see [EPI-RTE-research-findings](#epi-rte-research-findings)
Gap/limit: see [EPI-RTE-research-findings](#epi-rte-research-findings)

Route ID: [EPI-RTE-research-gap](#epi-rte-research-gap)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-findings](#epi-obj-research-findings)
Content/update relation: no content change
Transition or check target: Coverage of current question by findings so far
Evaluator/condition and domain: AIClient with question, 200-character finding prefixes and investigated-question statuses; adequacy domain
Activation and timing: see [EPI-RTE-research-gap](#epi-rte-research-gap); operation unobserved
Possible or observed result: shouldContinue and optional follow-up questions or parse failure
Implemented force: see [EPI-RTE-research-gap](#epi-rte-research-gap)
Epistemic authority and scope: Candidate adequacy judgment only; not factual verification of findings
Operational authority: Supplies continuation selector, not acceptance certificate
Behavioral-authority path: see [EPI-RTE-research-gap](#epi-rte-research-gap); horizon: Current research round
Evidence source ID and local anchor: SRC-1 `lib/ai/research-engine.ts` (implementation)
Claim IDs: [EPI-CLM-research-quality](#epi-clm-research-quality)
Mismatch marker: see [EPI-RTE-research-gap](#epi-rte-research-gap)
Gap/limit: see [EPI-RTE-research-gap](#epi-rte-research-gap)

Route ID: [EPI-RTE-research-continuation](#epi-rte-research-continuation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-findings](#epi-obj-research-findings)
Content/update relation: no content change
Transition or check target: Next research round versus synthesis
Evaluator/condition and domain: Code consumes shouldContinue, follow-up presence and bounds; continuation domain
Activation and timing: see [EPI-RTE-research-continuation](#epi-rte-research-continuation); operation unobserved
Possible or observed result: Up to three follow-ups or exit to synthesis; failed gap check also exits
Implemented force: see [EPI-RTE-research-continuation](#epi-rte-research-continuation)
Epistemic authority and scope: Permission to proceed, not acceptance of report claims
Operational authority: Schedules more source work or permits synthesis without successful review
Behavioral-authority path: see [EPI-RTE-research-continuation](#epi-rte-research-continuation); horizon: Current pipeline rounds
Evidence source ID and local anchor: SRC-1 `lib/ai/research-engine.ts` (implementation)
Claim IDs: [EPI-CLM-research-quality](#epi-clm-research-quality)
Mismatch marker: see [EPI-RTE-research-continuation](#epi-rte-research-continuation)
Gap/limit: see [EPI-RTE-research-continuation](#epi-rte-research-continuation)

Route ID: [EPI-RTE-threads-relevance](#epi-rte-threads-relevance)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-relevance-result](#epi-obj-relevance-result)
Content/update relation: no content change
Transition or check target: Relevance/authentic engagement opportunity of supplied posts for persona/topics
Evaluator/condition and domain: AIEvaluator remote model then JSON.parse; persona-fit domain
Activation and timing: see [EPI-RTE-threads-relevance](#epi-rte-threads-relevance); operation unobserved
Possible or observed result: Post-id score/reason array; parse exception returns []
Implemented force: see [EPI-RTE-threads-relevance](#epi-rte-threads-relevance)
Epistemic authority and scope: Judgment of fit only, not factual correctness, mechanism or transfer
Operational authority: Scores feed cron threshold; ad-hoc search returns scores as advice
Behavioral-authority path: see [EPI-RTE-threads-relevance](#epi-rte-threads-relevance); horizon: Current scan or ad-hoc request
Evidence source ID and local anchor: SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-threads-relevance](#epi-rte-threads-relevance)
Gap/limit: see [EPI-RTE-threads-relevance](#epi-rte-threads-relevance)

Route ID: [EPI-RTE-threads-selection](#epi-rte-threads-selection)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-relevance-result](#epi-obj-relevance-result)
Content/update relation: no content change
Transition or check target: Which new posts enter stored review/draft work queue
Evaluator/condition and domain: Code scoreMap lookup and configured threshold; selection domain
Activation and timing: see [EPI-RTE-threads-selection](#epi-rte-threads-selection); operation unobserved
Possible or observed result: Qualifying stored posts; others not admitted this scan
Implemented force: see [EPI-RTE-threads-selection](#epi-rte-threads-selection)
Epistemic authority and scope: Operational relevance admission, not acceptance of factual claims
Operational authority: Permits draft generation for above-threshold posts
Behavioral-authority path: see [EPI-RTE-threads-selection](#epi-rte-threads-selection); horizon: Current scan with persisted qualifying results
Evidence source ID and local anchor: SRC-1 `plugins/continuity-threads-engagement/src/cron.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-threads-selection](#epi-rte-threads-selection)
Gap/limit: see [EPI-RTE-threads-selection](#epi-rte-threads-selection)

Route ID: [EPI-RTE-threads-drafting](#epi-rte-threads-drafting)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-draft-result](#epi-obj-draft-result)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Post/persona to candidate reply text
Evaluator/condition and domain: AIEvaluator under concise/authentic/value instructions; reply-content domain
Activation and timing: see [EPI-RTE-threads-drafting](#epi-rte-threads-drafting); operation unobserved
Possible or observed result: Two parsed options or []; ad-hoc single raw reply
Implemented force: see [EPI-RTE-threads-drafting](#epi-rte-threads-drafting)
Epistemic authority and scope: Questions/policies may be non-truth-apt; factual reply claims remain unwarranted candidates
Operational authority: Supplies text for review or ad-hoc tool return
Behavioral-authority path: see [EPI-RTE-threads-drafting](#epi-rte-threads-drafting); horizon: Current call; cron candidates may persist
Evidence source ID and local anchor: SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-threads-drafting](#epi-rte-threads-drafting)
Gap/limit: see [EPI-RTE-threads-drafting](#epi-rte-threads-drafting)

Route ID: [EPI-RTE-threads-retention](#epi-rte-threads-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-draft-result](#epi-obj-draft-result)
Content/update relation: no content change
Transition or check target: Generated reply text to plugin-local draft rows
Evaluator/condition and domain: Code insertion after draft generation; storage domain
Activation and timing: see [EPI-RTE-threads-retention](#epi-rte-threads-retention); operation unobserved
Possible or observed result: Stored drafts and drafted status
Implemented force: see [EPI-RTE-threads-retention](#epi-rte-threads-retention)
Epistemic authority and scope: Candidate storage, not epistemic acceptance
Operational authority: Makes draft selectable/editable/postable later
Behavioral-authority path: see [EPI-RTE-threads-retention](#epi-rte-threads-retention); horizon: Across review requests until regeneration/deletion
Evidence source ID and local anchor: SRC-1 `plugins/continuity-threads-engagement/src/cron.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-threads-retention](#epi-rte-threads-retention)
Gap/limit: see [EPI-RTE-threads-retention](#epi-rte-threads-retention)

Route ID: [EPI-RTE-threads-publication](#epi-rte-threads-publication)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-draft-result](#epi-obj-draft-result)
Content/update relation: no content change
Transition or check target: Selected/first draft for remote posting
Evaluator/condition and domain: HTTP caller plus post/draft/config availability checks; publication domain
Activation and timing: see [EPI-RTE-threads-publication](#epi-rte-threads-publication); operation unobserved
Possible or observed result: Remote reply id/posted record or failed engagement
Implemented force: see [EPI-RTE-threads-publication](#epi-rte-threads-publication)
Epistemic authority and scope: Permission to publish only; endpoint result does not certify truth or authenticated human acceptance
Operational authority: Calls Threads API; records replied on success
Behavioral-authority path: see [EPI-RTE-threads-publication](#epi-rte-threads-publication); horizon: Current request and durable external/local effects
Evidence source ID and local anchor: SRC-1 `plugins/continuity-threads-engagement/src/ui-server.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-threads-publication](#epi-rte-threads-publication)
Gap/limit: see [EPI-RTE-threads-publication](#epi-rte-threads-publication)

Route ID: [EPI-RTE-vault-projection](#epi-rte-vault-projection)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-vault-memory](#epi-obj-vault-memory)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Scanner metadata/excerpts to stored vault overview
Evaluator/condition and domain: Code formatter/heuristic ranker; scan-summary domain
Activation and timing: see [EPI-RTE-vault-projection](#epi-rte-vault-projection); operation unobserved
Possible or observed result: Subset of folders/files with truncated excerpts and counts
Implemented force: see [EPI-RTE-vault-projection](#epi-rte-vault-projection)
Epistemic authority and scope: Warrant no stronger than supplied scan; importance heuristic not truth test
Operational authority: Provides high-level memory context and replaces index after scan/update
Behavioral-authority path: see [EPI-RTE-vault-projection](#epi-rte-vault-projection); horizon: Retained until rescan or incremental write
Evidence source ID and local anchor: SRC-1 `lib/vault/memory.ts` (implementation)
Claim IDs: none
Mismatch marker: see [EPI-RTE-vault-projection](#epi-rte-vault-projection)
Gap/limit: see [EPI-RTE-vault-projection](#epi-rte-vault-projection)

Route ID: [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-findings](#epi-obj-research-findings)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: external Perplexity answer to findings
Evaluator/condition and domain: see [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Activation and timing: see [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Possible or observed result: see [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Implemented force: see [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Epistemic authority and scope: imported source warrant unknown; fixed high label adds no warrant
Operational authority: see [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Behavioral-authority path: see [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition)
Evidence source ID and local anchor: SRC-1 `lib/ai/research-engine.ts`
Claim IDs: [EPI-CLM-research-quality](#epi-clm-research-quality)
Mismatch marker: high confidence assigned without a local factual evaluator
Gap/limit: external answer correctness and actual returned answer unobserved

Route ID: [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-findings](#epi-obj-research-findings)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: read-source prefix to findings after analyzer failure
Evaluator/condition and domain: see [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Activation and timing: see [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Possible or observed result: see [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Implemented force: see [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Epistemic authority and scope: acquired excerpt retains only unknown external-source warrant; truncation can degrade interpretability
Operational authority: see [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Behavioral-authority path: see [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback)
Evidence source ID and local anchor: SRC-1 `lib/ai/research-engine.ts`
Claim IDs: [EPI-CLM-research-quality](#epi-clm-research-quality)
Mismatch marker: low confidence fallback still enters findings pipeline
Gap/limit: no guarantee that a character prefix preserves qualifications or a whole claim

The remaining supplied material routes are not recast as new declarations:

Route ID: [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: schema/auth/timestamp admission, not memory truth
Evaluator/condition and domain: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Activation and timing: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Possible or observed result: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Implemented force: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Epistemic authority and scope: imported source warrant unknown
Operational authority: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Behavioral-authority path: see [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion)
Evidence source ID and local anchor: SRC-1 `org-server/src/routes/memories-push.ts`
Claim IDs: none
Mismatch marker: intended memory.db pull versus SDK default app target; see record
Gap/limit: no observed roundtrip; incomplete event/search inspection

Route ID: [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-plugin-session](runtime.md#rt-obj-plugin-session)
Content/update relation: non-truth-apt policy/content update: capability/session registration
Transition or check target: process/session access, not prompt truth
Evaluator/condition and domain: see [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission)
Activation and timing: see [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission)
Possible or observed result: see [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission)
Implemented force: see [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission)
Epistemic authority and scope: no factual license from token/capability admission
Operational authority: see [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission)
Behavioral-authority path: see [RT-BAP-plugin-capabilities](runtime.md#rt-bap-plugin-capabilities)
Evidence source ID and local anchor: SRC-1 `plugin-host/src/index.ts`
Claim IDs: [RT-CLM-plugin-controls](runtime.md#rt-clm-plugin-controls)
Mismatch marker: foreground delivery not established by host registration
Gap/limit: enabled process and installed bundle operation unobserved

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant | Source ID/anchor and layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-conversation-understanding](#epi-clm-conversation-understanding) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat), [EPI-RTE-narrative-generation](#epi-rte-narrative-generation), [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption) | None registered | No interventions or criterion-based truth/understanding evaluation | Model-mediated structure/context production is implemented | Understanding and dependable automatic extraction are not established by these routes |
| [EPI-CLM-source-groundtruth](#epi-clm-source-groundtruth) | see record | SRC-1 `lib/ai/narrative-synthesis.ts`; doctrine/design | see record | [EPI-RTE-memory-retention](#epi-rte-memory-retention), [EPI-RTE-narrative-generation](#epi-rte-narrative-generation), [EPI-RTE-narrative-retention](#epi-rte-narrative-retention) | None registered | No source authenticity/claim verification; parse fallback can lose preserved learning sections | Instructions distinguish user-set claims and AI hypotheses | Caller-set/inherited source labels cannot establish ground truth; contradiction rule is requested, not enforced |
| [EPI-CLM-research-quality](#epi-clm-research-quality) | see record | SRC-1 `lib/ai/research-engine.ts`; doctrine/design | see record | [EPI-RTE-research-findings](#epi-rte-research-findings), [EPI-RTE-research-gap](#epi-rte-research-gap), [EPI-RTE-research-continuation](#epi-rte-research-continuation) | None registered | No reference answers, factual audit or comparative outcome; lossy evidence delivery | Adequacy review and follow-up work selection are wired | Adequacy judgment and citation-form instructions do not license factual accuracy or citation fidelity |

## Bounded conclusion

Continuity implements several consequential candidate routes. [EPI-RTE-memory-retention](#epi-rte-memory-retention), [EPI-RTE-signal-retention](#epi-rte-signal-retention) and [EPI-RTE-relation-retention](#epi-rte-relation-retention) acquire caller/model statements with unknown source warrant. String/schema/id checks license storage and retrieval, not truth. Archival [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) removes direct active selection but does not establish derivative withdrawal from narrative/history. Relationship labels organize assertions; they are not validated criticism or accepted-claim integration.

[EPI-RTE-key-reshaping](#epi-rte-key-reshaping) and the scan formatter in [EPI-RTE-vault-projection](#epi-rte-vault-projection) deterministically reshape content under inspected rules. They add no empirical warrant. There is no established entailed factual derivation from warranted premises in these assessed routes. Narrative/research/reply model transformations remain separately indeterminate without actual premises/output traces: inference guidance is not evidence of produced ampliative claims, and retained candidates do not establish acceptance.

[EPI-RTE-narrative-format](#epi-rte-narrative-format) checks syntax only. [EPI-RTE-narrative-retention](#epi-rte-narrative-retention) admits even fallback text and marks signals absorbed; [EPI-RTE-narrative-consumption](#epi-rte-narrative-consumption) then supplies narrative content and self-assigned confidence in the next system message. This is a wired, advisory/model-interpreted behavioral-authority path across sessions, without a demonstrated evidence-consuming acceptance criterion. It is not lifecycle integration after established acceptance. Prior-content preservation and source-groundtruth claims remain unsupported at their enforcement points.

[EPI-RTE-research-gap](#epi-rte-research-gap) judges coverage over abbreviated findings. [EPI-RTE-research-continuation](#epi-rte-research-continuation) consumes that result to schedule work or proceed to synthesis, including after failed review. Its authority is pipeline continuation, not fact certification. [EPI-RTE-threads-relevance](#epi-rte-threads-relevance) assesses persona fit; [EPI-RTE-threads-selection](#epi-rte-threads-selection) enforces a score threshold for an engagement queue. Neither result checks reply/post truth. [EPI-RTE-threads-publication](#epi-rte-threads-publication) licenses external posting via endpoint availability, not authenticated human factual acceptance; status rejection does not enforce a veto in that endpoint. These are different targets, domains and forces, not one evaluator.

Plugin capability admission and org timestamp conflict resolution are direct symbolic policy changes/selection without a truth-apt acceptance route. They can govern access or overwrite eligibility, but cannot upgrade content warrant. The org pull database target and plugin foreground-delivery gaps bound claimed later consumption independently of content quality.

No exercised learning, reflective criticism, autonomous theory-building or self-improvement follows from the named writes alone. The inspected prompts represent the user/research subject, not demonstrated criticism of Continuity's own method against operation records. Possible behavior-shaping narrative adaptation is retained and deliverable, but no operation trace establishes activation or improved capacity. This is a local limit on these evidence paths, not a negative about opaque model processes or all shipped operations. Unassessed available paths prevent a system-complete negative about knowledge production or acceptance. No global epistemic score follows.

## Shared records

### Components

none declared in this member; the distributed-parametric components are [RT-CMP-ai-client](runtime.md#rt-cmp-ai-client) and [RT-CMP-ai-evaluator](runtime.md#rt-cmp-ai-evaluator).

### Operative objects

#### EPI-OBJ-memories
Label: Memory statement content

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Natural-language memory content is stored in SQLite memory.db rows and consumed by recall/context/synthesis. Candidate truth-apt content includes user preferences, project facts, patterns and constraints over the stated user/project scope; actual truth cannot be determined without instances/evidence. This object is the content-bearing part of the supplied admission route (different kind because the route owns production/persistence, not content identity). SRC-1 `lib/db/memories.ts` (implementation).

> [generateId(), id, content, "continuity-app", now]
> --- `lib/db/memories.ts`

#### EPI-OBJ-memory-source
Label: Memory source authority label

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Symbolic source enum in a SQLite row; caller-provided/default/inherited label is converted to natural-language source framing in synthesis. This is distinct from memory text because its consumer assigns epistemic treatment. It asserts provenance category, not verified authorship. It is the metadata part admitted by the supplied runtime route. SRC-1 `server/tools/memory-tools.ts` (implementation).

> source: MemorySourceEnum.optional().describe("Who wrote this: 'user' (explicit preference), 'ai' (inferred), 'system' (automated)"),
> --- `server/tools/memory-tools.ts`

#### EPI-OBJ-learnings
Label: Learning observations and absorption state

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Natural-language observation and symbolic signal_type/confidence/optional source ids/absorption flag reside in memory.db. Observation is truth-apt about preferences/patterns; flags control selection, not truth. Separate operative parts are described here: text supplies synthesis content; flag/count supplies scheduling and pending eligibility. This is the learning input part of the supplied admission container. SRC-1 `server/db/learnings.ts` (implementation).

> source_thread_id = null,
>     source_message_id = null,
> --- `server/db/learnings.ts`

#### EPI-OBJ-memory-links
Label: Memory relationship assertions

Symbolic typed edges and endpoint identifiers reside in SQLite memory_links; caller relation can assert truth-apt contradiction, dependence or supersession over the endpoint claims. Fixed query rules expose edges and active counterparts; relation names are not automatically interpreted as warrants. No counterpart in supplied runtime declarations: distinct from content persistence, although endpoints refer to its memories. SRC-1 `server/db/relationships.ts` (implementation).

> const { memory_id_a, memory_id_b, relationship_type = "related" } = params;
> --- `server/db/relationships.ts`

#### EPI-OBJ-narratives
Label: Narrative briefing and structured learning sections

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Natural-language user briefing/insights in SQLite narratives.content and JSON sections; symbolic version/confidence/hash accompany it. Briefing and structured learnings have different readers: foreground gets content plus metadata, subsequent synthesis gets prior content plus prior learning sections. They can differ after fallback. Truth-apt candidate claims concern user/work/projects; no concrete candidate trace is supplied. This is the saved-output part of runtime admission. SRC-1 `lib/ai/narrative-synthesis.ts` (implementation).

> Math.min(result.confidence, 0.95),
> --- `lib/ai/narrative-synthesis.ts:274-274`

#### EPI-OBJ-research-findings
Label: Research findings and report candidates

Part of: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

Natural-language findings/report/summary and symbolic sourceUrl/confidence/subquestion ids reside in JS working structures; canvas/message persistence belongs to the runtime callback. Different consumers receive 200-character findings for gap review and 300-character findings for synthesis, plus separate source metadata. Findings may assert truth-apt claims about researched subject; external or generated provenance differs by branch. This is the work-product part of the supplied pipeline. SRC-1 `lib/ai/research-engine.ts` (implementation).

> confidence: "high",
> --- `lib/ai/research-engine.ts`

#### EPI-OBJ-relevance-result
Label: RelevanceResult score and rationale

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

Symbolic postId/score plus natural-language reason in JS parsed array; qualifying results are stored in plugin SQLite posts. Fit-to-persona/topic is the assessment target, not post truth. Rationale may express truth-apt relevance judgments but no verified reference labels are supplied. This is the assessment-result part of the runtime Threads route; model identity stays in RT-CMP-ai-evaluator. SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` (implementation).

> export interface RelevanceResult {
>   postId: string;
>   score: number;
>   reason: string;
> }
> --- `plugins/continuity-threads-engagement/src/ai-evaluator.ts`

#### EPI-OBJ-draft-result
Label: DraftResult reply text

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

Natural-language reply options reside in JS strings, then plugin-local SQLite drafts for scheduled/regenerated candidates. Ad-hoc single-reply path returns directly. No supplied instance individuates factual claims; questions and non-truth-apt speech are possible. This is a different content part than scoring because its later consumer can publish text. SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` (implementation).

> export interface DraftResult {
>   drafts: string[];
> }
> --- `plugins/continuity-threads-engagement/src/ai-evaluator.ts`

#### EPI-OBJ-vault-memory
Label: VaultMemory formatted overview

Natural-language overview with symbolic paths/count/date metadata is stored as a global memory string at obsidian_vault_index. Counts/paths/excerpts are truth-apt about the supplied scan, with unverified scan-to-files fidelity. Projection and incremental updater own its changes. Distinct identity compared with runtime desktop/memory routes: producer is vault scan/write logic rather than conversation or MCP caller, although downstream delivery overlaps. SRC-1 `lib/vault/memory.ts` (implementation).

> const VAULT_MEMORY_KEY = "obsidian_vault_index";
> --- `lib/vault/memory.ts`

### Routes

#### EPI-RTE-key-reshaping
Label: Desktop key and value normalization

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

For concrete input key "  Work Style  " and value "  Prefers short answers  ", inspected code passes work_style and Prefers short answers to setMemory. This is an implementation deduction, not a run. Distinct keys differing only in case/spacing can collapse; value trimming does not entail truth. Nonempty checks concern strings, not preferences. Model proposes via tool choice; code decides validity; there is no reference answer or per-content human veto. SRC-1 `lib/ai/memory-tools.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized remembered text after persistence
- Later read-back: Via stored content, not the transient normalization result
- Delegated visibility: Executor receives key/value, not full user history
- Selection predicate: Nonempty trimmed key/value; default type context
- Invalidation or expiry: Per-call input expires; canonical key may overwrite existing slot
- Activation or effect: Canonical storage address/content passed to setMemory
- Evidence limits: No run; semantic truth/identifier intent is not checked

Behavioral-authority path: consumer: setMemory; channel: normalized string arguments; force: enforcing storage-address selection, not enforcing truth; horizon: this write and later reads of the canonical slot. Epistemic license: No new factual warrant; value is retained as caller/model proposal.

> // Normalize the key (lowercase, underscores for spaces)
> const normalizedKey = args.key
>     .toLowerCase()
>     .trim()
>     .replace(/\s+/g, "_");
> --- `lib/ai/memory-tools.ts`

#### EPI-RTE-memory-retention
Label: Desktop and MCP candidate persistence

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Desktop model or MCP caller proposes; code admits. MCP source is caller supplied, defaults ai; desktop insertion omits source and inherits ai, while update retains existing source. Therefore a desktop model update of a preexisting user-labeled row leaves that label attached to changed content. This is a counterexample to treating source=user as guaranteed human authorship. MCP write can unarchive an existing matching row. Version history offers inspection, not an automatic truth rollback. No answer oracle or content approval criterion is present in these inspected mutations. SRC-1 `server/db/memories.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stored row/JSON or tool error
- Later read-back: Active records reach recall/system context; MCP readers return requested rows
- Delegated visibility: Database executor receives content and metadata
- Selection predicate: Desktop canonical key/global scope; MCP key+scope+project upsert
- Invalidation or expiry: Replacement/version bump; MCP upsert clears archived_at
- Activation or effect: Candidate retention and later delivery are wired, activation unobserved
- Evidence limits: No source truth verification or live shared-database proof

Behavioral-authority path: consumers: active memory queries, recall executor and configured model via rebuilt system context; channel: memory.db row to tool result or prompt; force: permissive retrieval eligibility and advisory natural-language context; horizon: later requests/sends until archive or replacement. Epistemic license: Imported source warrant unknown; versioning is not acceptance.

> source = "ai",
> --- `server/db/memories.ts`

#### EPI-RTE-memory-withdrawal
Label: Memory archival changes active selection

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Caller or model requests withdrawal; code archives, rather than erases. No evidence-consuming rejection criterion is supplied. Counterexample to complete forgetting: narrative gathering excludes archived rows but feeds previous narrative and asks to preserve all previous learnings. Scheduler also requires active memories and does not necessarily run just because an item was archived. Thus archiving does not establish withdrawal of the same claim from already generated narrative or saved chat. MCP write can revive an archived slot; desktop getMemory only finds active slots. SRC-1 `lib/db/memories.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Archived acknowledgment or missing-key response
- Later read-back: Active recall excludes row; version history remains independently readable
- Delegated visibility: Executor receives identifier only
- Selection predicate: Existing active desktop key or MCP id
- Invalidation or expiry: Archival changes eligibility; later writes may reintroduce content
- Activation or effect: Direct active memory exclusion is wired; derivative removal is not established
- Evidence limits: No universal erasure or epistemic falsification follows

Behavioral-authority path: consumers: getMemory/getAllMemories/searchMemories and synthesis memory selection; channel: archived_at SQL predicates; force: enforcing exclusion from these active reads; horizon: later active requests, not already generated narrative/history. Epistemic license: No judgment that content is false; withholding active use only.

> `UPDATE memories SET archived_at = $1 WHERE key = $2 AND scope = $3 AND project_id IS NULL`,
> --- `lib/db/memories.ts`

#### EPI-RTE-signal-retention
Label: MCP learning observation admission

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

MCP caller proposes observation, signal_type and optional provenance. Code stores with default confidence 0.5; no check dereferences thread/message evidence or adjudicates observation truth in the inspected insert. Starting or requesting the call is not per-content human approval. No answer oracle; open input recording. Absorption is bookkeeping, not accepted knowledge or improved capacity. SRC-1 `server/db/learnings.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Learning row and pending count
- Later read-back: Unabsorbed rows enter synthesis; list returns retained observations
- Delegated visibility: Insert sees observation/labels and optional source identifiers
- Selection predicate: Scope/project and pending predicate select synthesis inputs
- Invalidation or expiry: Absorption flag removes from next pending set, not deletion
- Activation or effect: Observation persistence can affect next narrative construction
- Evidence limits: No evidence of actual conversational extraction or calibrated confidence

Behavioral-authority path: consumers: checkAndSynthesize and synthesizeNarrative; channel: pending count and observation rows; force: permissive scheduling and advisory model input; horizon: future synthesis until absorption, with retained observations still listable. Epistemic license: Imported observation warrant unknown; label correction is not criticism evidence.

> confidence = 0.5,
> --- `server/db/learnings.ts`

#### EPI-RTE-relation-retention
Label: MCP relationship assertions retained

No counterpart after comparison with supplied runtime records: this is caller-selected relationship persistence, not a model evaluation or automatic withdrawal route. Caller supplies relation; code checks existence, not the asserted logical relation. A supersedes or contradicts enum does not archive either endpoint. getMemoryLinks filters the linked row by archived_at but does not interpret relation type as a reliability policy. This is organization before demonstrated acceptance, not lifecycle integration of accepted knowledge. No human-content veto/reference oracle is established. SRC-1 `server/db/relationships.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Edge JSON or error
- Later read-back: MCP and memory-browser linked-record reads expose retained edge
- Delegated visibility: Executor sees endpoint ids and relation enum
- Selection predicate: Existing endpoints; unique edge; active counterpart on read
- Invalidation or expiry: Archival hides linked counterpart; edge semantics do not invalidate claims
- Activation or effect: Inspectable organization, not automatic relation-dependent reliance
- Evidence limits: No validated entailment/contradiction/supersession or integrated acceptance

Behavioral-authority path: consumers: memory_links_get callback and getLinkedMemories UI query; channel: memory_links join results; force: advisory relationship display, not enforcing contradiction/supersession; horizon: later linked-record requests. Epistemic license: Only endpoints/existing edge constraints checked; relation truth unknown.

> if (!a) throw new Error(`Memory not found: ${memory_id_a}`);
> --- `server/db/relationships.ts`

#### EPI-RTE-narrative-generation
Label: Model synthesis of user understanding

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Prompt asks to infer patterns and evolving understanding, preserve prior learnings and adjust confidence for contradiction. Available evidence cannot establish semantic preservation, entailment or actual non-entailment of a particular output: no instance with premises/result was supplied. Remaining possibilities are reshaping, entailed derivation or ampliative conjecture; a grounded input/output trace is needed to distinguish them. Memory SQL selects all active scopes even for project synthesis, while signals/previous narrative are scoped. This is not demonstrated project-only evidence. Invocation owner is app synthesis code; model proposes text under natural-language rules, not a truth oracle. SRC-1 `lib/ai/narrative-synthesis.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: AI response, then save path
- Later read-back: Input candidate can become saved narrative; prior narrative is fed into next synthesis
- Delegated visibility: Model receives labeled memory text, observations and previous briefing/learnings; not full source threads
- Selection predicate: All active memories; scoped unabsorbed signals and latest scoped narrative
- Invalidation or expiry: Snapshot comparison may suppress invocation; generated candidate replaces prior content if saved
- Activation or effect: User model construction requested; actual content/quality unobserved
- Evidence limits: No candidate trace, provenance verification or empirical contradiction resolution

Behavioral-authority path: consumers: response parser/save code, then next synthesis and foreground model if persisted; channel: AI response to narrative row to prompt; force: permissive automatic admission, then advisory/model-interpreted context; horizon: current synthesis and later sessions. Epistemic license: No added warrant merely from model synthesis; inherited warrant unknown.

> - If a new learning contradicts an old one, keep both but adjust confidence
> --- `lib/ai/narrative-synthesis.ts`

#### EPI-RTE-narrative-format
Label: Narrative JSON parsing and fallback

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Program checks parseability; type assertion is not runtime schema validation. Concrete malformed response "not-json" throws in JSON.parse; inspected catch constructs content "not-json", empty learning array and confidence 0.3, then proceeds to save. A low fallback confidence is not a rejection gate. This defeats the possible claim that invalid JSON necessarily prevents operational reliance. No target execution was needed for this deduction. SRC-1 `lib/ai/narrative-synthesis.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed result or caught exception
- Later read-back: inapplicable — parse event itself is not retained for later consumer
- Delegated visibility: Parser sees response text only
- Selection predicate: Optional fence removal then JSON parse
- Invalidation or expiry: Per-call result; catch generates replacement container
- Activation or effect: Branches to parsed output or fallback, not a semantic truth decision
- Evidence limits: No semantic schema/evidence check established by parsing

Behavioral-authority path: consumer: synthesizeNarrative catch/save branch; channel: JSON.parse result or exception; force: enforcing branch selection, not enforcing semantic acceptance; horizon: current synthesis. Epistemic license: Syntactic parse license only; neither structure assertion nor factual acceptance.

> result = JSON.parse(text);
> --- `lib/ai/narrative-synthesis.ts`

#### EPI-RTE-narrative-retention
Label: Narrative replacement and signal absorption

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Code admits generated or fallback text automatically, then marks input signals absorbed one by one. Confidence Math.min cap limits maximum display value, not calibration or a semantic gate. Existing row is updated rather than a full narrative-version archive in this function. No transactional all-or-nothing envelope is shown around narrative write and all absorption writes. Preserve-all instruction is countered by parse fallback with learnings: [], so preservation is requested, not enforced. Manual user launch is not content approval. Exceptions/scheduler catch provide failure return, not established restoration of prior narrative. SRC-1 `lib/ai/narrative-synthesis.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean true after SQL steps, or thrown/caught failure
- Later read-back: Latest narrative read and prior narrative supplied to next synthesis
- Delegated visibility: DB receives content, serialized sections, version/confidence/hash
- Selection predicate: Successful persistence; no minimum confidence predicate
- Invalidation or expiry: Current row content replaced; pending flags changed
- Activation or effect: Future model-visible candidate and scheduling state change
- Evidence limits: No accepted claim, semantic preservation or atomic multi-step guarantee

Behavioral-authority path: consumers: getNarrativeForPrompt, subsequent synthesizeNarrative, and pending-learning scheduling queries; channel: narratives row and absorbed_into_narrative flags; force: permissive candidate supply and enforcing pending-set exclusion; horizon: across sessions until later update. Epistemic license: Retention grants no epistemic acceptance; confidence is generated/capped.

> "UPDATE learnings SET absorbed_into_narrative = 1 WHERE id = $1",
> --- `lib/ai/narrative-synthesis.ts`

#### EPI-RTE-narrative-consumption
Label: Saved narrative to foreground system message

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Material part of runtime memory admission; its downstream authority agrees with RT-BAP-system-guidance. getNarrativeForPrompt selects nonempty content without a minimum confidence or per-claim support check. Only content/confidence/version/date, not structured sections or source thread/message evidence, are included here. The channel upgrades presentation to system context while retaining candidate warrant, not automatically epistemic authority. Delivery is wired; compliance and benefit remain unobserved. SRC-1 `providers/chat-provider.tsx` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Constructed system prompt
- Later read-back: Retained briefing supplied across sends when available
- Delegated visibility: Foreground model receives narrative content and display metadata, not source trace
- Selection predicate: Tauri context; nonempty latest scoped narrative; best-effort read
- Invalidation or expiry: Per-send rebuild; latest saved content replaces earlier selection
- Activation or effect: Natural-language advisory/contextual influence on answer/tool choice
- Evidence limits: No observed activation; failure can omit context silently

Behavioral-authority path: consumer: configured foreground model; channel: What I Know About You section in rebuilt system message; force: advisory/model-interpreted context, not deterministic compliance; horizon: current and repeated later sends. Epistemic license: Operational context, not certified knowledge; confidence label is not measured accuracy.

> "## What I Know About You",
> --- `providers/chat-provider.tsx`

#### EPI-RTE-research-findings
Label: Research import and candidate report construction

Part of: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

This route concerns the analyzer and final synthesizer's model-generated content. The adjacent imported-answer and excerpt-fallback branches are separately declared in [EPI-RTE-provider-acquisition](#epi-rte-provider-acquisition) and [EPI-RTE-excerpt-fallback](#epi-rte-excerpt-fallback); they do not inherit the model-transformation classification. Model inference remains indeterminate without concrete premises/output. Analyst sees up to 2000 characters per selected source; fallback uses 500. Final synthesizer sees findings sliced to 300 plus a title/URL source list, without each finding sourceUrl/confidence. It cannot be assumed to verify every citation from original excerpts. This is a counterexample to equating source presence with complete evidence delivery. Planner/generator owns proposals; callback admission is automatic; no reference answer. SRC-1 `lib/ai/research-engine.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pipeline findings then report/summary result
- Later read-back: Completion callback stores report canvas and chat summary, per RT-RTE-deep-research
- Delegated visibility: Analyst sees selected source excerpts; synthesizer sees shortened findings and source titles/URLs
- Selection predicate: Source-order caps/read success; parsed model fields; Perplexity-answer and fallback branches
- Invalidation or expiry: Cooperative cancellation and partial-result fallback; current windows discarded
- Activation or effect: Candidate work product available through callback persistence
- Evidence limits: Input/output trace needed to distinguish model reshaping/derivation/conjecture; external source truth unknown

Behavioral-authority path: consumers: gap reviewer, final synthesizer and desktop onComplete callback; channel: shortened finding text, final report/summary and callback result; force: advisory model evidence context and permissive automatic work-product persistence; horizon: current pipeline and later canvas/history reads. Epistemic license: Acquired source warrant unknown; model-generated claim warrant unestablished.

> // Fall back to using raw source content as findings
> --- `lib/ai/research-engine.ts`

#### EPI-RTE-research-gap
Label: Model judgment of research sufficiency

Part of: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

Model judges gaps under instructions, without original source text in this invocation or a reference outcome. It is a production evaluator, not a causal experiment or known-answer benchmark. reasoning is requested but inspected consumer uses shouldContinue/followUpQuestions; unconsumed rationale is not evidence of implemented criticism-directed revision. SRC-1 `lib/ai/research-engine.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed adequacy judgment or exception
- Later read-back: inapplicable — check output is used for current continuation, not saved as an independent critic record
- Delegated visibility: Reviewer receives abbreviated findings and statuses, not original source pages
- Selection predicate: Reached gap phase before round/read/cancellation cap
- Invalidation or expiry: Current check expires after continuation choice
- Activation or effect: Judgment can change further research selection
- Evidence limits: No oracle, demonstrated truth checking or content-directed blame attribution

Behavioral-authority path: consumer: runResearch gap-result branch; channel: parsed shouldContinue/followUpQuestions; force: permissive continuation advice subject to code bounds; horizon: current round. Epistemic license: Candidate adequacy judgment only; not factual verification of findings.

> const gapResponse = await aiClient.chat(gapMessages);
> --- `lib/ai/research-engine.ts`

#### EPI-RTE-research-continuation
Label: Gap judgment to follow-ups or synthesis

Part of: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

Model proposes follow-ups; code caps and decides progression. A false/missing shouldContinue, missing questions, reached budgets or parse exception can end gap checking. Catch explicitly proceeds to synthesis, so this is not enforcing mandatory successful epistemic review. No content veto or answer oracle. It may improve coverage but no learning or benefit is established. SRC-1 `lib/ai/research-engine.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New subquestions or break
- Later read-back: inapplicable — transient continuation decisions do not independently persist; report persists by separate callback
- Delegated visibility: Worker rounds receive selected questions/search queries
- Selection predicate: shouldContinue plus follow-ups, max rounds/read budget/cancellation
- Invalidation or expiry: End/cancellation discards round state; report may outlive it
- Activation or effect: Code-selected work continuation affects current pipeline
- Evidence limits: Stopping is not evidence-consuming acceptance of claims

Behavioral-authority path: consumers: next source-worker round or final synthesizer; channel: questionsToInvestigate or loop break; force: enforcing work selection/continuation; horizon: current pipeline rounds. Epistemic license: Permission to proceed, not acceptance of report claims.

> // Gap check failed — proceed to synthesis with what we have
> --- `lib/ai/research-engine.ts`

#### EPI-RTE-threads-relevance
Label: Model persona-fit scoring

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

Separate consumers: cron score admission is enforcing, registered search tool formats all returned posts with scores and reasons and is advisory. The inspected parser uses a type assertion, not range/identity validation; scoring scale in prompt is not runtime calibration. The evaluator does not assess truth of post or drafted reply. Provider computation remains RT-CMP-ai-evaluator. No answer oracle or validated reference relevance label. SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Scores/reasons or empty array on parse failure
- Later read-back: Scores/reasons persisted with qualifying cron posts; ad-hoc result retention depends on caller
- Delegated visibility: Scorer sees post text/usernames plus persona/keywords
- Selection predicate: Input post array; model-generated scores; parser success
- Invalidation or expiry: Per-call scores; retained qualifying post metadata lasts separately
- Activation or effect: Score data supplied to selection or advisory tool result
- Evidence limits: No calibrated accuracy, score-range enforcement or actual tool delivery proved

Behavioral-authority path: consumers: CronScheduler scoreMap threshold and search_threads_posts formatting handler; channel: RelevanceResult array; force: ranking input to enforcing cron threshold versus advisory ad-hoc text; horizon: scan/current request, with qualifying metadata later persisted. Epistemic license: Judgment of fit only, not factual correctness, mechanism or transfer.

> const parsed = JSON.parse(response) as RelevanceResult[];
> --- `plugins/continuity-threads-engagement/src/ai-evaluator.ts`

#### EPI-RTE-threads-selection
Label: Cron score threshold admission

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

Model proposes relevance; code admits based on score >= threshold after prior search/dedup budgets. Empty score array leads no matches. Threshold is a criterion for intended engagement queue use only; not an evidence-consuming truth acceptance rule. User supplies persona/settings rather than reviewing each threshold decision. Rejected/unscored posts are not thereby false. SRC-1 `plugins/continuity-threads-engagement/src/cron.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Qualifying-post list and stored post rows
- Later read-back: Persisted posts and metadata reach review UI/later actions
- Delegated visibility: Drafter receives qualifying post and persona
- Selection predicate: Id-matched score at or above configured threshold
- Invalidation or expiry: Later status edits change workflow metadata; not guaranteed external veto
- Activation or effect: Conditional queue admission and draft-generation permission
- Evidence limits: Model fit judgment cannot warrant post truth or reply safety

Behavioral-authority path: consumers: insertPost and AIEvaluator.draftReplies; channel: qualifyingPosts list; force: enforcing score-threshold queue admission; horizon: scan and later review of stored qualifying posts. Epistemic license: Operational relevance admission, not acceptance of factual claims.

> if (score && score.score >= this.relevanceThreshold) {
> --- `plugins/continuity-threads-engagement/src/cron.ts`

#### EPI-RTE-threads-drafting
Label: Model reply candidate generation

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

No reply instance allows individuation of a proposition or proof of non-entailment. If a reply is a question it need not be truth-apt; if it asserts experience or insight, preservation/derivation/conjecture require input/output evidence. Model proposes; parse maps text fields, does not assess factual accuracy. Regenerate endpoint deletes old drafts before replacement generation; failure can therefore leave no old candidates. Direct draft tool returns one reply without this scheduled persistence/threshold. SRC-1 `plugins/continuity-threads-engagement/src/ai-evaluator.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reply options/empty list or direct single reply
- Later read-back: Cron/regeneration store candidates; ad-hoc reply goes to invoking caller
- Delegated visibility: Model receives post/persona and optional tone, not user experience evidence
- Selection predicate: Qualifying cron post or endpoint/tool request
- Invalidation or expiry: Regeneration deletes old draft rows; per-call inference context expires
- Activation or effect: Produces candidate reply content
- Evidence limits: No observed content, factual check or guaranteed two valid options

Behavioral-authority path: consumers: cron/regenerate draft inserter or draft_threads_reply caller; channel: returned draft strings; force: permissive candidate supply, advisory until separately selected/posted; horizon: current call and later persisted review where stored. Epistemic license: Questions/policies may be non-truth-apt; factual reply claims remain unwarranted candidates.

> return { drafts: parsed.map((d) => d.text) };
> --- `plugins/continuity-threads-engagement/src/ai-evaluator.ts`

#### EPI-RTE-threads-retention
Label: Draft candidates retained for review

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

Cron automatically inserts every returned draft and sets drafted status. The UI permits string edits and selected-draft choice. These operations can alter proposed content, but no observed human evidence-consuming factual acceptance is supplied. Status drafted can be set even when drafts array is empty. External post success remains separate. SRC-1 `plugins/continuity-threads-engagement/src/cron.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Draft rows/status and eventual scan count
- Later read-back: Review/read/approve endpoints fetch retained drafts
- Delegated visibility: Persistence sees generated draft strings; later HTTP client sees candidates
- Selection predicate: All returned options, no separate semantic criterion
- Invalidation or expiry: Regeneration deletes old drafts; edits replace text
- Activation or effect: Candidate availability for later review/posting
- Evidence limits: Local persistence is source-defined; no retained database instances inspected

Behavioral-authority path: consumers: review GET/edit/select/approve handlers; channel: plugin-local drafts rows; force: permissive availability for editing/selection/publication, not factual endorsement; horizon: later review requests until regeneration/deletion. Epistemic license: Candidate storage, not epistemic acceptance.

> insertDraft(post.id, result.drafts[i], i + 1);
> --- `plugins/continuity-threads-engagement/src/cron.ts`

#### EPI-RTE-threads-publication
Label: Review actions and endpoint-triggered publication

Part of: [RT-RTE-threads-engagement](runtime.md#rt-rte-threads-engagement)

UI intends human review, but any caller reaching endpoint with configuration/post/draft can initiate. Existing rejected/skipped status is not checked here, so status rejection is not an enforcing publication veto. Draft selection defaults first option. API result is an operative outcome for posted/failed bookkeeping, not evidence for factual claim acceptance, process reliability or causal model benefit. No rollback of successful remote post or checked replay safety is established. Editing/selecting/status changes are separate from posting and do not require an evidence criterion. SRC-1 `plugins/continuity-threads-engagement/src/ui-server.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP reply id or error with engagement status
- Later read-back: Local engagement/post status consumed by review and summary tools
- Delegated visibility: Threads API receives chosen draft text; not scoring evidence/reviewer rationale
- Selection predicate: Existing post, draft (selected or first), configured API
- Invalidation or expiry: Status changes do not undo remote reply; failed record does not prove no remote effect
- Activation or effect: Endpoint permits external publishing and local outcome bookkeeping
- Evidence limits: No authenticated human reviewer, factual acceptance, idempotency or actual successful posting

Behavioral-authority path: consumers: ThreadsAPI.postReply and local outcome bookkeeping; channel: selected/first draft text and remote reply result; force: permissive publication, then enforcing posted/failed state update; horizon: current request plus durable remote/local effects. Epistemic license: Permission to publish only; endpoint result does not certify truth or authenticated human acceptance.

> const replyId = await deps.threadsApi.postReply(post.id, draft.draft_text);
> --- `plugins/continuity-threads-engagement/src/ui-server.ts`

#### EPI-RTE-vault-projection
Label: Deterministic vault overview and incremental edits

No counterpart after runtime comparison: scanner projection has its own producer and selection, although desktop chat consumes it. Code takes at most 15 root subfolders and 30 scored files; file score depends on frontmatter/depth/name/size, not evidence correctness. Excerpt first line strips heading and truncates to 60. Concrete input excerpt "# Alpha\nBeta" becomes Alpha, losing Beta by design. updateVaultMemoryFile uses substring matching for path replacement and can replace lines mentioning another longer path containing that string; fidelity of incremental update is therefore not guaranteed. The relation here describes the projection intent/ordinary formatter, not a guarantee for all incremental inputs. No acceptance step. SRC-1 `lib/vault/memory.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: setMemory completion; stored overview text
- Later read-back: Vault memory getter returns retained string for later context
- Delegated visibility: Formatter sees supplied scan data; consumer sees selected overview rather than all files
- Selection predicate: Heuristic ranking/top-N, root-folder cap and excerpt prefix
- Invalidation or expiry: Rescan replaces entry; incremental update replaces substring-matching lines or appends
- Activation or effect: Retained summarized vault awareness; actual scan validity unobserved
- Evidence limits: No scanner/content truth audit; lossy and potentially destructive incremental mapping

Behavioral-authority path: consumers: setMemory and later vault-context/model readers; channel: stored overview at obsidian_vault_index; force: enforcing overview selection/overwrite and advisory model context; horizon: retained until rescan/incremental write. Epistemic license: Warrant no stronger than supplied scan; importance heuristic not truth test.

> return scored.slice(0, MAX_KEY_FILES).map((s) => s.file);
> --- `lib/vault/memory.ts`

#### EPI-RTE-provider-acquisition
Label: Perplexity answer imported as finding

Part of: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

This is the external-answer import branch of the supplied research pipeline, distinct from local analyzer generation. runSubAgent copies each Perplexity answer into findings and assigns confidence high without an evidence-consuming factual decision. Imported truth-apt content is acquired, not produced by this local transformation. There is no local oracle or human content veto; external source warrant remains unknown. SRC-1 `lib/ai/research-engine.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer-bearing finding with subquestion id and high label
- Later read-back: Finding enters gap/synthesis contexts; final report/summary can persist through the runtime callback
- Delegated visibility: Downstream reviewer/synthesizer sees abbreviated finding text, not the external provider's internal evidence process
- Selection predicate: Nonempty perplexityAnswers branch
- Invalidation or expiry: Working findings last for pipeline; persisted output lasts separately
- Activation or effect: External candidate becomes eligible for report construction without local verification
- Evidence limits: No supplied answer instance, provider evidence trace, observed use or validated confidence

Behavioral-authority path: consumers: gap reviewer and final synthesizer; channel: finding content prefixes; force: advisory evidence context with an uncalibrated label; horizon: this research pipeline and later callback output. No factual acceptance follows.

> for (const answer of perplexityAnswers) {
>       findings.push({
>         content: answer,
>         subQuestionId: subQuestion.id,
>         confidence: "high",
>       });
> --- `lib/ai/research-engine.ts`

#### EPI-RTE-excerpt-fallback
Label: Failed analyzer returns source prefixes

Part of: [RT-RTE-deep-research](runtime.md#rt-rte-deep-research)

This is the source-excerpt fallback part of the supplied research pipeline, not a successful analyzer judgment. The catch truncates read-source content to 500 characters, associates URL/subquestion and marks low confidence. For concrete source text of 500 copies of A followed by " except in winter", the retained prefix excludes the qualification. This implementation deduction demonstrates lossy reshaping; it neither establishes source truth nor produces an accepted inference. Code owns fallback selection; no human approval, answer oracle or per-claim rejection criterion is present. SRC-1 `lib/ai/research-engine.ts` (implementation).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Source-prefix findings with URL and low confidence
- Later read-back: Prefixes feed current gap/synthesizer invocations; report/summary can later persist through runtime callback
- Delegated visibility: Downstream consumers get prefixes, not original read-source text or failed analyzer reasoning
- Selection predicate: Analyzer try/catch failure and available readSources
- Invalidation or expiry: Working findings disappear at pipeline end; outputs may survive
- Activation or effect: Failure does not exclude source-prefix material from report construction
- Evidence limits: Truncation need not preserve a complete proposition or qualification; source warrant unknown; no run

Behavioral-authority path: consumers: gap reviewer/final synthesizer; channel: abbreviated fallback findings; force: permissive pipeline supply and advisory model context; horizon: current pipeline, with outputs independently persisted.

> content: source.fullContent!.slice(0, 500),
>           sourceUrl: source.url,
>           subQuestionId: subQuestion.id,
>           confidence: "low",
> --- `lib/ai/research-engine.ts`

### Claims

#### EPI-CLM-conversation-understanding
Label: Conversation becomes understood structure

No counterpart among supplied runtime claims: this is the product's consequential understanding/extraction declaration, not the plugin-control guarantee. SRC-1 `README.md` (doctrine/design) asserts background understanding and extraction from conversation. Implementation overlap is with desktop tools and synthesis, not evidence of exercised understanding.

> You just talk. Have a conversation about your project, your research, your plans. The system listens, understands, and quietly builds structure in the background — tasks, notes, timelines, decisions — all extracted from your natural conversation.
> --- `README.md`

#### EPI-CLM-source-groundtruth
Label: Source labels license synthesis reliance

No counterpart among supplied runtime claims: the synthesis instruction licenses direct reliance on user-labeled content and hypothesis framing for AI-labeled content. It further requests preservation and contradiction-confidence adjustment. SRC-1 `lib/ai/narrative-synthesis.ts` (doctrine/design). Source label authenticity and semantic enforcement are not implemented by this instruction alone.

> - User-set memories (source: "user") are ground truth — state them directly
> - AI-inferred memories (source: "ai") are hypotheses — frame appropriately
> - Preserve ALL existing learnings from the previous narrative
> --- `lib/ai/narrative-synthesis.ts`

#### EPI-CLM-research-quality
Label: Research adequacy and factual report guidance

No counterpart among supplied runtime claims: source-native instructions ask the reviewer to judge sufficient coverage and the synthesizer to produce a factual balanced cited report. SRC-1 `lib/ai/research-engine.ts` (doctrine/design). Implemented model calls request the behavior; they do not establish accurate execution or accepted report propositions.

> - Set shouldContinue to false if findings adequately cover the topic
> --- `lib/ai/research-engine.ts`

> - Cite sources inline using [Source N] format
> - Be factual and balanced — note disagreements between sources
> --- `lib/ai/research-engine.ts`

### Evidenced absences

none declared in this member. Uninspected operations and missing runs bound conclusions rather than establish system-wide absences.

### Behavioral-authority paths

none declared in this member. The generic narrative/model-guidance path is already [RT-BAP-system-guidance](runtime.md#rt-bap-system-guidance). Each new route above records its distinct consumer, channel, force and horizon without duplicating that referent.
