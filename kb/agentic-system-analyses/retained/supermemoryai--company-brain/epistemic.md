---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Company Brain's truth-apt acquisition, memory admission, reply checks and later behavioral authority at the frozen revision."
run-id: AAS-2026-10-14-company-brain-30a9e8cfaeca-01
reviewed-boundary: ef8a45ef3aed97b32599c7d8007edefab6d14e9a
---

# Company Brain epistemic report

## Source-and-claim boundary

Question: which acquired or generated statements are checked, admitted, retained and consumed, and what reliance do those transitions warrant? Scope follows [boundary](boundary.md#boundary-and-evidence); evidence identities/layers follow its [Source register](boundary.md#source-register), not a new register. All direct findings below use SRC-1 implementation or explicitly labelled doctrine/design at the frozen commit. No target execution, observed run or causal experiment is supplied.

External memory extraction, embeddings, deduplication, supersession, model internals and remote tool semantics remain uninspected: their actual correctness, lineage preservation and effect cannot be established. Distributed-parametric providers have the separate mutability limits of [RT-CMP-brain-main](runtime.md#rt-cmp-brain-main), [RT-CMP-triage-model](runtime.md#rt-cmp-triage-model), and [RT-CMP-research-model](runtime.md#rt-cmp-research-model). Client inference is not weight training evidence.

| Entry point/operation | Source path | Coverage and prevented conclusion |
|---|---|---|
| Worker/HTTP and Slack dispatch | `src/worker.ts`, `src/routes/index.ts`, `src/routes/slack/index.ts` | Supplied boundary/runtime: [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn). No CLI dispatch is claimed; shipped worker is the entry. |
| Tool registry, brain search and entity lookup | `src/brain/turn/tools.ts`, `src/brain/memory/search-brain.ts`, `src/brain/search-brain-format.ts` | Direct search registration/read/format reads; entity route supplied [RT-RTE-entity-web](runtime.md#rt-rte-entity-web). |
| Interactive writeback and delayed channel curation | `src/brain/memory/writeback.ts`, `src/brain/memory/index.ts`, `src/brain/slack/channel-observe.ts` | Direct complete writeback/index reads and channel prompt/distill/write/cursor ranges; runtime caller supplied [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff). Full observer retry scheduler uninspected; no complete reliability claim. |
| Hosted adapter and cleanup | `src/compat/routes/memories/handler-effect.ts`, `src/brain/memory/cleanup.ts`, `src/brain/turn/agent.impl.ts` | Direct adapter, cleanup and reset-registry reads. Actual service deletion/extraction uninspected. |
| Topic split | `src/brain/memory/split.ts` | Direct complete read; grouping and failure behavior assessed separately from factual acceptance. |
| Style observer and consumer | `src/brain/turn/interaction-observe.ts`, `src/brain/memory/interaction-style.ts` | Direct complete reads; compute consumption supplied by runtime. Bucket production opaque. |
| Final reply check/selection | `src/brain/observability/reply-quality.ts`, `src/brain/turn/finalization/output.ts` | Direct complete reads; delivery host supplied runtime. Shape gate is not semantic truth evaluation. |
| Research planning, flags, send and administrative feedback | `src/brain/auto-research/plan.ts`, `src/brain/auto-research/draft.ts`, `src/brain/auto-research/send.ts`, `src/brain/auto-research/outcome.ts`, `src/brain/admin/chat.ts`, `src/brain/turn/agent.ts`, `src/brain/turn/agent.impl.ts` | Direct plan/send/outcome reads; bounded draft shaping/flags ranges. Correction directly read complete outcome/admin chat implementations and agent exposure/export passages: [EPI-RTE-outcome-acquisition](#epi-rte-outcome-acquisition), [EPI-RTE-outcome-frame](#epi-rte-outcome-frame), [EPI-RTE-admin-consumption](#epi-rte-admin-consumption). Administrative interpretation consumes feedback; automatic planner inputs contain prior bodies and operator steer, not this outcome reader. No automatic engagement-driven adaptation or benefit inferred. |
| App classification, approval and shell | `src/brain/tools/mcp/policy.ts`, `src/brain/tools/mcp/tool-policy.ts`, `src/brain/tools/sandbox/guards.ts` | Supplied [RT-RTE-app-code](runtime.md#rt-rte-app-code), [RT-RTE-direct-mcp](runtime.md#rt-rte-direct-mcp), [RT-RTE-sandbox-work](runtime.md#rt-rte-sandbox-work); no direct audit repeated. |
| Skills, standing configuration, scheduled calls and compaction | `src/brain/skills/tools.ts`, `src/brain/tools/scheduling.ts`, `src/brain/turn/context.ts` | Supplied [RT-RTE-instruction-admission](runtime.md#rt-rte-instruction-admission), [RT-RTE-scheduled-task](runtime.md#rt-rte-scheduled-task), [RT-RTE-context-boundary](runtime.md#rt-rte-context-boundary). |
| Signup research/profile maintenance/admin memory views/tests | `src/brain/turn/research.ts`, `src/brain/memory/profile-sync.ts`, `src/routes/memories.ts` | Boundary/runtime initial findings only; leaf transformations/evaluators and UI review criteria not directly assessed here. Prevents system-complete negative about factual acceptance, correction or criticism. Authored tests do not supply passed results. |

Public warrant claims assessed: [EPI-CLM-team-answers](#epi-clm-team-answers), [EPI-CLM-current-memory](#epi-clm-current-memory), and model self-check doctrine [EPI-CLM-evidence-check](#epi-clm-evidence-check). Approval claims are operational, not truth claims: [RT-CLM-write-approval](runtime.md#rt-clm-write-approval).

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-doc](#epi-obj-memory-doc) | Decisions, ownership, dated facts or stable inferences | Durable company input | SRC-1 `src/brain/memory/writeback.ts` | sources may be empty; human statements and model prose do not establish truth |
| [EPI-OBJ-channel-clusters](#epi-obj-channel-clusters) | Curated human statements | Faithful clusters for downstream extraction | SRC-1 `src/brain/slack/channel-observe.ts` | preservation requested, not demonstrated |
| [EPI-OBJ-brain-results](#epi-obj-brain-results) | Service memories/chunks | Retrieved evidence | SRC-1 `src/brain/search-brain-format.ts` | ranking and optional provenance, not endorsement |
| [EPI-OBJ-reply](#epi-obj-reply) | Answer propositions or nonfactual chat | Slack reply | SRC-1 `src/brain/turn/finalization/output.ts` | supplied record/claim trace not host-validated |
| [EPI-OBJ-style-note](#epi-obj-style-note) | Attributed team preferences; also behavioral guidance | Agent persona notes | SRC-1 `src/brain/turn/interaction-observe.ts` | selected model output unobserved; guidance is not itself necessarily truth-apt |
| [EPI-OBJ-research-draft](#epi-obj-research-draft) | Research conclusions and advice | Reviewable outbound note | SRC-1 `src/brain/auto-research/draft.ts` | tool trace flags do not compare claims to evidence |
| [EPI-OBJ-topic-partition](#epi-obj-topic-partition) | Existing fact texts grouped by topic; symbolic ID assignments | Readable child topics | SRC-1 `src/brain/memory/split.ts` | model taxonomy interpretation not independently validated |
| [EPI-OBJ-draft-outcome](#epi-obj-draft-outcome) | Reactions, reply excerpts and attribution to a sent research post | Operator-facing evidence about reception | SRC-1 `src/brain/auto-research/outcome.ts`, `src/brain/admin/chat.ts` | bounded excerpts; uncertainty flag has a partial-failure countercase; engagement does not establish factual correctness |
| [RT-OBJ-brain-skill](runtime.md#rt-obj-brain-skill), [RT-OBJ-workspace-prompt](runtime.md#rt-obj-workspace-prompt) | Instructions; factual parts not individuated here | Standing guidance | see supplied records | human approval supplies permission, not factual warrant |

## Authority-route ledger

Route ID: [EPI-RTE-outcome-acquisition](#epi-rte-outcome-acquisition)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-draft-outcome](#epi-obj-draft-outcome)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Sent-post reception data, not factual correctness of research claims
Evaluator/condition and domain: see cited route; program eligibility/scope, Slack responses; no truth evaluator
Activation and timing: Non-refinement administrative request after sends; operation unobserved
Possible or observed result: Bounded outcomes or missing/partial data; possible
Implemented force: Supplies acquired evidence to framing
Epistemic authority and scope: Imported reception only; lineage degraded by clipping, source accuracy unknown; engagement does not license claim truth
Operational authority: Permits selected outcome evidence to enter administrative context
Behavioral-authority path: see cited route; administrative formatter, transient outcome objects, permissive, current query
Evidence source ID and local anchor: SRC-1 `src/brain/auto-research/outcome.ts`; see cited route
Claim IDs or none: none
Mismatch marker or none: Failed thread read can be classified as known engagement with empty replies
Gap/limit: see cited route

Route ID: [EPI-RTE-outcome-frame](#epi-rte-outcome-frame)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-draft-outcome](#epi-obj-draft-outcome)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Outcome fields to administrative evidence text
Evaluator/condition and domain: see cited route; deterministic renderer, not correctness check
Activation and timing: Before fresh administrative turn; operation unobserved
Possible or observed result: Reception block or empty string; possible
Implemented force: Controls evidence representation shown to model
Epistemic authority and scope: Bounded reception descriptions; no endorsement; user IDs and draft IDs omitted
Operational authority: Supplies unknown/truncation language and reception matching guidance
Behavioral-authority path: see cited route; model question frame, text, advisory, current administrative inquiry
Evidence source ID and local anchor: SRC-1 `src/brain/admin/chat.ts`; see cited route
Claim IDs or none: none
Mismatch marker or none: Unknown handling inherits reader's partial-failure countercase
Gap/limit: see cited route

Route ID: [EPI-RTE-admin-consumption](#epi-rte-admin-consumption)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-draft-outcome](#epi-obj-draft-outcome)
Content/update relation: no content change
Transition or check target: Scoped feedback admitted to fresh administrative model context
Evaluator/condition and domain: see cited route; host validates scope/completion, model interprets reception; no oracle
Activation and timing: Operator administrative query, excluding refinement; operation unobserved
Possible or observed result: Operator-only answer or error; possible
Implemented force: Context selection enforcing locally; interpretation advisory to operator
Epistemic authority and scope: Reception evidence available for interpretation; generated answer truth/compliance not established
Operational authority: Allows operator inquiry using feedback; does not itself update research plan or persist an accepted criticism
Behavioral-authority path: see cited route; computeTurn/model then operator, question frame and returned reply, advisory, current inquiry and optional supplied history
Evidence source ID and local anchor: SRC-1 `src/brain/admin/chat.ts`; see cited route
Claim IDs or none: none
Mismatch marker or none: Consumer exists; operator interpretation is not automatic planning/adaptation
Gap/limit: see cited route; no supplied episode of criticism or later feedback-shaped behavior

Route ID: [EPI-RTE-channel-distillation](#epi-rte-channel-distillation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-channel-clusters](#epi-obj-channel-clusters)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Slack human statements to curated clusters
Evaluator/condition and domain: Fast model with structured schema; requested faithful wording and dates, not an independent truth oracle
Activation and timing: Delayed observation of bounded new messages; operation unobserved.
Possible or observed result: Candidate clusters or empty list; possible, not observed.
Implemented force: Persisted batch feeds memory writer
Epistemic authority and scope: Acquired statements are not established as true; semantic preservation unverified
Operational authority: Selects what enters durable memory
Behavioral-authority path: Memory writer; SQL batch; permissive; later recall
Evidence source ID and local anchor: SRC-1 `src/brain/slack/channel-observe.ts`; see [EPI-RTE-channel-distillation](#epi-rte-channel-distillation) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Channel prompt requests non-ampliative grouping; implementation does not establish faithful output. Novel added inference versus reshaping remains unresolved.
Gap/limit: see [EPI-RTE-channel-distillation](#epi-rte-channel-distillation).

Route ID: [EPI-RTE-memory-admission](#epi-rte-memory-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-doc](#epi-obj-memory-doc)
Content/update relation: no content change
Transition or check target: Document eligibility for hosted ingest
Evaluator/condition and domain: Program checks nonempty content, tags, current reset epoch and service status; domain is write eligibility
Activation and timing: Each writeMemory call, before and after hosted add; operation unobserved.
Possible or observed result: written true/false; stale successful document deleted; possible, not observed.
Implemented force: Enforcing local write gate
Epistemic authority and scope: Operational admission only; queued/done is not evidence-consuming acceptance of factual truth
Operational authority: Permits mapping/registering eligible document; blocks stale/invalid write
Behavioral-authority path: writeMemory; return status and epoch; enforcing; current generation
Evidence source ID and local anchor: SRC-1 `src/brain/memory/index.ts`; see [EPI-RTE-memory-admission](#epi-rte-memory-admission) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: No per-document human judgment in this path; adapter status is a storage outcome, not factual endorsement.
Gap/limit: see [EPI-RTE-memory-admission](#epi-rte-memory-admission).

Route ID: [EPI-RTE-document-retention](#epi-rte-document-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-doc](#epi-obj-memory-doc)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Application document and metadata enter Supermemory
Evaluator/condition and domain: Hosted documents.add; internals uninspected
Activation and timing: After local write admission; operation unobserved.
Possible or observed result: Document ID and status defaulting to queued; possible, not observed.
Implemented force: Permissive retained input for later retrieval
Epistemic authority and scope: Source warrant unknown after hosted extraction; sources metadata is not verification
Operational authority: Makes content available to hosted memory service
Behavioral-authority path: Hosted service and later recall; document API; permissive; later invocations
Evidence source ID and local anchor: SRC-1 `src/compat/routes/memories/handler-effect.ts`; see [EPI-RTE-document-retention](#epi-rte-document-retention) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Imported human/model content is acquired. Server-side transformations cannot be classified here. Arrays of links are comma-joined; no retained raw evidence guarantee.
Gap/limit: see [EPI-RTE-document-retention](#epi-rte-document-retention).

Route ID: [EPI-RTE-brain-selection](#epi-rte-brain-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-brain-results](#epi-obj-brain-results)
Content/update relation: no content change
Transition or check target: Returned chunks/memories for query relevance
Evaluator/condition and domain: Opaque service similarity plus local dedup/sort/top40 and score threshold 0.3; domain is retrieval relevance
Activation and timing: search_company_brain request; operation unobserved.
Possible or observed result: Formatted relevant text or none found; possible, not observed.
Implemented force: Ranking and local filtering
Epistemic authority and scope: Relevance score does not license truth or completeness; source warrant unknown
Operational authority: Selects which retained statements the foreground model sees
Behavioral-authority path: Foreground model; tool-result text; ranking/advisory; current turn
Evidence source ID and local anchor: SRC-1 `src/brain/memory/search-brain.ts`; see [EPI-RTE-brain-selection](#epi-rte-brain-selection) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Undefined similarity passes local formatting filter. Formatting retains optional IDs/filepaths but not complete document provenance.
Gap/limit: see [EPI-RTE-brain-selection](#epi-rte-brain-selection).

Route ID: [EPI-RTE-reply-check](#epi-rte-reply-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-reply](#epi-obj-reply)
Content/update relation: no content change
Transition or check target: Sanitized reply string publishability
Evaluator/condition and domain: Regex/parse-based program; domain is selected malformed shapes, not semantic truth
Activation and timing: Final reply selection; operation unobserved.
Possible or observed result: Boolean publishable; possible, not observed.
Implemented force: See disposition route; boolean is consumed there
Epistemic authority and scope: Only heuristic display-shape license
Operational authority: Supplies gate decision; does not itself publish
Behavioral-authority path: selectTurnReply; Boolean; enforcing via linked disposition; current reply
Evidence source ID and local anchor: SRC-1 `src/brain/observability/reply-quality.ts`; see [EPI-RTE-reply-check](#epi-rte-reply-check) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: CJK plus Latin letters fails even when bilingual text is valid. Falsehood in ordinary English can pass.
Gap/limit: see [EPI-RTE-reply-check](#epi-rte-reply-check).

Route ID: [EPI-RTE-reply-selection](#epi-rte-reply-selection)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-reply](#epi-obj-reply)
Content/update relation: no content change
Transition or check target: Which candidate string may become final reply
Evaluator/condition and domain: Program consumes publishability Boolean and orders sources: terminal, text, longest acceptable transcript text
Activation and timing: At settlement before caller delivery; operation unobserved.
Possible or observed result: Selected reply/source or empty; possible, not observed.
Implemented force: Enforcing selection
Epistemic authority and scope: Permission to deliver is not epistemic acceptance
Operational authority: Suppresses failing candidates; may select older assistant draft as recovery
Behavioral-authority path: Slack caller; selected reply; permissive; current turn
Evidence source ID and local anchor: SRC-1 `src/brain/turn/finalization/output.ts`; see [EPI-RTE-reply-selection](#epi-rte-reply-selection) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Longest transcript draft need not be the most current or best supported. Caller owns empty fallback.
Gap/limit: see [EPI-RTE-reply-selection](#epi-rte-reply-selection).

Route ID: [EPI-RTE-style-generation](#epi-rte-style-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-style-note](#epi-obj-style-note)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Human reactions to generalized team preference and operating note
Evaluator/condition and domain: Fast model prompted to verify direct HUMAN evidence; remaining program only recognizes non-note phrases
Activation and timing: Delayed public-thread observation; excludes DMs/private channels; operation unobserved.
Possible or observed result: Short note or empty/non-note; possible, not observed.
Implemented force: Candidate note feeds style admission
Epistemic authority and scope: Requested human-grounded generalization; whether particular note is entailed or ampliative is not determinable without output
Operational authority: Proposes later style guidance
Behavioral-authority path: Style writer; generated text; permissive; future sessions
Evidence source ID and local anchor: SRC-1 `src/brain/turn/interaction-observe.ts`; see [EPI-RTE-style-generation](#epi-rte-style-generation) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Speaker labels bound intended evidence, but prompt compliance is not enforced by semantic comparison. Preference attribution is truth-apt; resulting guidance also changes non-truth-apt policy.
Gap/limit: see [EPI-RTE-style-generation](#epi-rte-style-generation).

Route ID: [EPI-RTE-style-admission](#epi-rte-style-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-style-note](#epi-obj-style-note)
Content/update relation: no content change
Transition or check target: Non-note filtering and current-generation style write eligibility
Evaluator/condition and domain: Program uses phrase filter, public surface and workspace/generation checks, service queued/done status
Activation and timing: After style generation and hosted write; operation unobserved.
Possible or observed result: Skip, retry, stale, complete/continue; possible, not observed.
Implemented force: Enforcing operational eligibility
Epistemic authority and scope: Not acceptance that every preference has direct human support
Operational authority: Admits agent-self note and advances carried cursor only after successful status
Behavioral-authority path: Future observer/style context; hosted note and cursor; permissive/advisory; later sessions
Evidence source ID and local anchor: SRC-1 `src/brain/turn/interaction-observe.ts`; see [EPI-RTE-style-admission](#epi-rte-style-admission) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Human evidence verification is model-requested, not a separately consumed evidence judgment.
Gap/limit: see [EPI-RTE-style-admission](#epi-rte-style-admission).

Route ID: [EPI-RTE-draft-check](#epi-rte-draft-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-draft](#epi-obj-research-draft)
Content/update relation: no content change
Transition or check target: Draft length and presence of evidence-producing tool names
Evaluator/condition and domain: Program counts words and classifies tool names in trace; not evidence entailment or source truth
Activation and timing: Completed nonempty ephemeral draft; operation unobserved.
Possible or observed result: Over-length/no-tool-evidence flags; possible, not observed.
Implemented force: Advisory to reviewer, not rejection
Epistemic authority and scope: Tool presence establishes neither claim support nor tool result quality
Operational authority: Allows flagged real draft to remain reviewable
Behavioral-authority path: Reviewer; stored flags; advisory; draft review
Evidence source ID and local anchor: SRC-1 `src/brain/auto-research/draft.ts`; see [EPI-RTE-draft-check](#epi-rte-draft-check) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Runtime baseline mentioned flags but did not individuate evaluator domain. A tool-name witness can coexist with unsupported claims.
Gap/limit: see [EPI-RTE-draft-check](#epi-rte-draft-check).

Route ID: [EPI-RTE-draft-send](#epi-rte-draft-send)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-research-draft](#epi-obj-research-draft)
Content/update relation: no content change
Transition or check target: Stored draft permission for Slack delivery
Evaluator/condition and domain: Reviewer chooses ID; program checks draft status, entitlement, workspace and target
Activation and timing: Separate explicit send after draft retention; operation unobserved.
Possible or observed result: Posted/sent status or error; possible, not observed.
Implemented force: Permissive send with local enforcing operational checks
Epistemic authority and scope: Send records use permission; no named factual criterion or evidence-consuming review contract
Operational authority: Delivers stored body; successful target earns watchlist slot
Behavioral-authority path: Slack recipient and watchlist; message/API; permissive; current send and future rounds
Evidence source ID and local anchor: SRC-1 `src/brain/auto-research/send.ts`; see [EPI-RTE-draft-send](#epi-rte-draft-send) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Human selection is not automatically evidence-consuming epistemic acceptance. Body is sent without flags forcing a refusal.
Gap/limit: see [EPI-RTE-draft-send](#epi-rte-draft-send).

Route ID: [EPI-RTE-topic-partition](#epi-rte-topic-partition)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-topic-partition](#epi-obj-topic-partition)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Index grouping of existing document IDs into child topics
Evaluator/condition and domain: Fast model proposes children; program normalizes keys/indexes, excludes other, later-child-wins, moves after metadata success
Activation and timing: 125 live members; sample capped at 160; operation unobserved.
Possible or observed result: Child mapping/tag changes or skipped failed update; possible, not observed.
Implemented force: Changes organization and later selection
Epistemic authority and scope: Grouping establishes no new factual warrant; not lifecycle integration after epistemic acceptance
Operational authority: Moves retrieval organization without changing existing memory statements
Behavioral-authority path: Topic tree/metadata consumers; tags and IDs; ranking/selection; later recall
Evidence source ID and local anchor: SRC-1 `src/brain/memory/split.ts`; see [EPI-RTE-topic-partition](#epi-rte-topic-partition) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: Requested coherent subthemes are not validated semantically. Descriptive labels are model interpretations, not proven taxonomy truth.
Gap/limit: see [EPI-RTE-topic-partition](#epi-rte-topic-partition).

Route ID: [EPI-RTE-reset-withdrawal](#epi-rte-reset-withdrawal)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-doc](#epi-obj-memory-doc)
Content/update relation: no content change
Transition or check target: Eligibility of old-generation memory and observation state
Evaluator/condition and domain: Program advances epoch, clears observer/cursor/registry/research state, cancels schedules; writers delete stale late document
Activation and timing: Operator reset registry and late-write checks; operation unobserved.
Possible or observed result: Old writes blocked/deleted; local state cleared; possible, not observed.
Implemented force: Enforcing generation eligibility
Epistemic authority and scope: Freshness/withdrawal from operational use, not refutation of content
Operational authority: Prevents deleted carried style from regenerating and stale writes mapping into new registry
Behavioral-authority path: Observers/writers/later recall; epoch and cleared SQL; enforcing; subsequent generation
Evidence source ID and local anchor: SRC-1 `src/brain/turn/agent.impl.ts`; see [EPI-RTE-reset-withdrawal](#epi-rte-reset-withdrawal) for evidence passages and route fields.
Claim IDs or none: see comparison below for public claims; none specific to this function unless linked there.
Mismatch marker or none: resetMemoryRegistry is local reset component, not proof all remotely retained content was deleted. Cascade comment is an external-service assertion.
Gap/limit: see [EPI-RTE-reset-withdrawal](#epi-rte-reset-withdrawal).

Route ID: [RT-RTE-entity-web](runtime.md#rt-rte-entity-web)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: canonical entity JSON; see cited route.
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: real-world entity identification versus JSON/canonical nonempty validation.
Evaluator/condition and domain: see cited route; parse validity is not identification accuracy.
Activation and timing: unresolved reference; see cited route.
Possible or observed result: entity or null; see cited route.
Implemented force: canonical identification can guide later app lookup; optional cache persists it.
Epistemic authority and scope: no independently checked identification warrant established.
Operational authority: see cited route.
Behavioral-authority path: see cited route; lookup input and future cache consumers, permissive, current/later references.
Evidence source ID and local anchor: SRC-1 `src/brain/memory/entities.ts`; see cited record.
Claim IDs or none: none.
Mismatch marker or none: successful parse is operational adoption, not truth acceptance.
Gap/limit: provider native search and generated outputs unobserved.

Route ID: [RT-RTE-app-code](runtime.md#rt-rte-app-code)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: proposed Code Mode native method effect and grant; see cited record.
Content/update relation: no content change
Transition or check target: method's read/write effect in remote tool domain.
Evaluator/condition and domain: see cited record; contract override, annotation, deterministic verb or triage model classifier.
Activation and timing: before native callback execution; see cited record.
Possible or observed result: allow/deny/pause; possible, operation unobserved.
Implemented force: local enforcement through connector policy and approval protocol.
Epistemic authority and scope: effect classification only; no license for answer truth or successful remote action.
Operational authority: see cited record; reads allowed, non-read denied for read-only grants or paused for requester approval.
Behavioral-authority path: see [RT-BAP-tool-policy](runtime.md#rt-bap-tool-policy); connector native executor, effect-policy decision, enforcing, current invocation/resume.
Evidence source ID and local anchor: SRC-1 `src/brain/tools/mcp/policy.ts`; supplied record.
Claim IDs or none: [RT-CLM-write-approval](runtime.md#rt-clm-write-approval).
Mismatch marker or none: classification can differ from actual remote effects; no global write mediation follows.
Gap/limit: remote semantics and SDK compliance uninspected; human approval is permission, not correctness evaluation.

Route ID: [RT-RTE-direct-mcp](runtime.md#rt-rte-direct-mcp)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: proposed direct MCP tool effect and grant; see cited record.
Content/update relation: no content change
Transition or check target: tool-name/annotation effect class and permitted grant mode.
Evaluator/condition and domain: see cited record; deterministic name tokens and annotations, with separate approval predicate and lease checks.
Activation and timing: direct fallback assembly and provider call; see cited record.
Possible or observed result: filtered availability, denied execution, approval request or call; possible, operation unobserved.
Implemented force: local availability/filtering, lease validation and SDK needsApproval predicate.
Epistemic authority and scope: local permission classification only; does not establish actual effect or answer truth.
Operational authority: see cited record; positively read tools for shared/read-only grants; personal unknown names can lack an approval trigger.
Behavioral-authority path: see [RT-BAP-tool-policy](runtime.md#rt-bap-tool-policy); direct tool executor, filtering and needsApproval, enforcing/permissive at named checks, current call/continuation.
Evidence source ID and local anchor: SRC-1 `src/brain/tools/mcp/tool-policy.ts`; supplied record.
Claim IDs or none: [RT-CLM-write-approval](runtime.md#rt-clm-write-approval).
Mismatch marker or none: this shipped fallback is not equivalent to Code Mode's non-read pause policy.
Gap/limit: actual remote method effects and SDK compliance uninspected; no deployment violation is inferred.

## System-claim versus route comparison

| Claim ID | Claimed operation/warrant | Source/anchor and layer | Doctrine/design support | Implemented routes | Observed run | Causal support/limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-team-answers](#epi-clm-team-answers) | Not internet/guesswork; own conversations/tools | SRC-1 `README.md`; doctrine/design | System prompt requests evidence-linked answers | [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn), [RT-RTE-entity-web](runtime.md#rt-rte-entity-web), [EPI-RTE-brain-selection](#epi-rte-brain-selection) | none supplied | No source attribution/accuracy experiment | Internal evidence available and selected | Absolute source restriction not supported: native entity web search exists; draft with no tool evidence can survive |
| [EPI-CLM-current-memory](#epi-clm-current-memory) | Memories kept current as people talk | SRC-1 `README.md`; doctrine/design | Channel prompt assigns dedup/supersession to downstream extractor | [EPI-RTE-channel-distillation](#epi-rte-channel-distillation), [EPI-RTE-document-retention](#epi-rte-document-retention), [EPI-RTE-reset-withdrawal](#epi-rte-reset-withdrawal) | none supplied | Service internals excluded | Implements continuous capture and local generation invalidation | Reset freshness is not factual supersession; downstream currentness unknown |
| [EPI-CLM-evidence-check](#epi-clm-evidence-check) | Check every answer claim against seen evidence | SRC-1 `src/brain/prompt/system.ts`; doctrine/design | Model instruction is explicit | [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn), [EPI-RTE-reply-check](#epi-rte-reply-check), [EPI-RTE-reply-selection](#epi-rte-reply-selection) | none supplied | No concrete answer/check result or causal comparison | Self-check requested; display gate implemented | Model compliance unknown; deterministic gate does not consume claim evidence |
| [RT-CLM-write-approval](runtime.md#rt-clm-write-approval) | Automatic approval for writes | see supplied claim | see supplied claim | [RT-RTE-app-code](runtime.md#rt-rte-app-code), [RT-RTE-direct-mcp](runtime.md#rt-rte-direct-mcp), [RT-RTE-sandbox-work](runtime.md#rt-rte-sandbox-work) | none supplied | see supplied claim | Local classified Code Mode effect admission | Permission scope does not imply factual evaluation or global mediation |

## Bounded conclusion

Company Brain acquires human statements and tool/service evidence, requests durable curation, retains documents, and supplies selected memory to later model calls. The source warrant of imported statements is not created by import; hosted extraction/lineage remains unknown. Local date anchors, source links, generation IDs and tags preserve some context, but not a checked chain of evidence supporting every extracted statement. Service status grants storage eligibility, not factual acceptance.

Directly inspected text code establishes grouping/formatting transformations, not accepted ampliative knowledge. For example, `buildSlackMemoryWriteRequest` given content `Owner is Ada`, eventDate `2026-10-01`, and now `2026-10-14` emits `DOCUMENT_DATE: 2026-10-14
Owner is Ada (as of 2026-10-01)`: a date/metadata reshaping of supplied premises, not a discovered ownership fact. `sanitizeSlackReply` given `{"reply":"Owner is Ada","memory":null}` extracts `Owner is Ada`; the shape check accepts ordinary text without testing Ada's ownership. These deductions use inspected implementation, not target execution. A false ownership assertion would follow the same successful shape path. Topic partition changes organization, not the warranted truth of member facts. No checked entailment of a new real-world claim is established by these transformations.

Generated summaries, generalized style notes, entity identifications and research conclusions can contain truth-apt propositions. Without concrete outputs and premises, semantic preservation versus entailed or non-entailed additions is indeterminate, not automatically ampliative. Prompts constrain proposals but do not supply observed compliance. The foreground policy requests an evidence check; the host's operative reply check instead licenses selected display shape. Evidence-free research is flagged and retained for review rather than universally rejected. Human send selection supplies a consequential permission, but the source names no factual criterion, intended evidential scope or required evidence-consuming decision. Retention, watchlist registration and topic repointing therefore do not establish lifecycle integration after epistemic acceptance.

Style observation is an implemented trace-fed behavior-shaping path: public human reactions can generate retained persona notes, carried observer context, and service-bucketed facets for later foreground context. It separately requests human-only warrant and imposes eligibility/failure controls. This is neither evidence of provider weight change nor improved future capacity. Later behavior actually depending on those notes, criticism-driven method revision and successful self-improvement remain unobserved/unestablished; no global negative about learning, reflection or theory construction follows. Standing skills and prompts have separate human admission and advisory authority, per runtime records.

The assessment supports distinct local routes and their limits, not one epistemic score. Uninspected signup/profile/other admin/evaluation leaves prevent a system-complete absence claim about acceptance or criticism. Research feedback does have an implemented consumer: the administrative chat acquires recent sent-post reactions and bounded replies, renders them with uncertainty/truncation language, and supplies that frame to a fresh model turn. Its reply reaches the operator, not the workspace. This supports operator-facing interpretation of reception, not automatic research-plan adaptation or evidence-consuming factual acceptance. The automatic planner separately consumes prior bodies and operator steering; an operator could use feedback to steer later work, but no supplied trace establishes that chain. The outcome reader's uncertainty handling is imperfect: a failed thread read becomes null, yet with a successful reactions read `thread?.ok !== false` remains true, allowing 'no replies' without known reply evidence. Formatting also drops reply-user IDs and bounds textual provenance. These limits constrain reception claims, not the existence of feedback consumption.

The same admin implementation can propose replacement draft wording in a distinct refinement mode; that mode skips the outcome block and requires the operator to apply the proposal. In the inspected feedback route, no structured content-directed criticism naming a challenged theory, result and placement of blame is required or retained as a revision decision. This does not establish that a model or operator cannot criticize a post in a concrete conversation. Operator-held history can enter subsequent admin turns, but no observed episode establishes criticism-driven iteration, later behavior depending on feedback, improved capacity or causal benefit. Absence of supplied runs prevents exercised-route, accuracy and causal-benefit conclusions, not source-level implementation findings.

## Shared records

### Operative objects

#### EPI-OBJ-memory-doc
Label: MemoryDoc

Source-native identity: MemoryDoc/MemoryDocInput content, optional eventDate, sources and tags. Representational form: Natural-language statement content; symbolic links/dates/tag IDs control metadata. Storage substrate: Model messages then hosted document service. Evidence: SRC-1 `src/brain/memory/writeback.ts`; supporting passages in associated routes below. Distinct object within writeback progression of [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), not its full runtime route.

#### EPI-OBJ-channel-clusters
Label: PersistedChannelBatch clusters

Source-native identity: PersistedChannelBatch.clusters. Representational form: Natural-language curated content plus symbolic batch timestamps/custom IDs. Storage substrate: Durable Object SQL clusters_json, then hosted document. Evidence: SRC-1 `src/brain/slack/channel-observe.ts`; supporting passages in associated routes below. Distinct intermediate, not final extracted memories; closest supplied [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff).

#### EPI-OBJ-brain-results
Label: Brain search results

Source-native identity: searchBrain results and formatBrainResults string. Representational form: Natural-language memory/chunk content; symbolic IDs/scores/filepaths. Storage substrate: Hosted response, current tool context. Evidence: SRC-1 `src/brain/search-brain-format.ts`; supporting passages in associated routes below. Distinct retrieved content from retained input document; closest supplied [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff).

#### EPI-OBJ-reply
Label: Selected turn reply

Source-native identity: TurnTerminalProposal.reply and fallback assistant text. Representational form: Natural-language interpreted by recipient; source enum symbolic. Storage substrate: Current model output and Slack delivery. Evidence: SRC-1 `src/brain/turn/finalization/output.ts`; supporting passages in associated routes below. Distinct answer content within [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn), not [RT-OBJ-turn-state](runtime.md#rt-obj-turn-state).

#### EPI-OBJ-style-note
Label: Observed persona note

Source-native identity: note, carriedState and InteractionStyleProfile text facets. Representational form: Natural-language preference descriptions and guidance; cursor/buckets symbolic. Storage substrate: Hosted agent-self documents and Durable Object cursor SQL. Evidence: SRC-1 `src/brain/turn/interaction-observe.ts`; supporting passages in associated routes below. Distinct behavior-shaping content, not company factual document or skill; closest supplied [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff).

#### EPI-OBJ-research-draft
Label: AutoResearchDraft

Source-native identity: NewAutoResearchDraft body, sources and flags. Representational form: Natural-language conclusions/flags plus symbolic trace/status/destination. Storage substrate: Local SQL draft state; Slack on send. Evidence: SRC-1 `src/brain/auto-research/draft.ts`; supporting passages in associated routes below. Distinct material draft object within [RT-RTE-research-draft](runtime.md#rt-rte-research-draft).

#### EPI-OBJ-topic-partition
Label: PartitionSchema children

Source-native identity: PartitionSchema children memoryIndexes and normalized child paths. Representational form: Symbolic index/document assignments; natural-language descriptions model-interpreted. Storage substrate: Generation response then remote metadata and Durable Object mappings. Evidence: SRC-1 `src/brain/memory/split.ts`; supporting passages in associated routes below. No runtime counterpart after comparison; topic split was explicitly deferred.

#### EPI-OBJ-draft-outcome
Label: DraftOutcome reception evidence

Source-native identity: DraftOutcome reactions, replies, opening, targetLabel, destination, sentAt, engagementKnown and repliesTruncated; sentBlock renders a model-visible text view. Representational form: Natural-language reply excerpts/opening; symbolic reaction names/counts, user IDs and uncertainty flags. Storage substrate: Existing SQL sent-draft identity and live Slack responses, then current administrative model context; no dedicated outcome persistence in these implementations. Evidence: SRC-1 `src/brain/auto-research/outcome.ts`, `src/brain/admin/chat.ts`. Distinct from [EPI-OBJ-research-draft](#epi-obj-research-draft): reception after send, not proposed body/flags. Closest supplied [RT-RTE-research-draft](runtime.md#rt-rte-research-draft) does not establish this administrative feedback object or consumer. Source passages retained in the associated routes below.

### Routes

#### EPI-RTE-outcome-acquisition
Label: Sent research reception acquisition

Distinct identity: acquires reception after [EPI-RTE-draft-send](#epi-rte-draft-send), not draft generation/send in [RT-RTE-research-draft](runtime.md#rt-rte-research-draft). This route spans sent-store and administrative access rather than a material part of exactly one supplied runtime record.

Endpoints/progression: Selected sent drafts with Slack timestamps → organization-bound workspace/token and channel lookup → parallel Slack reactions/thread reads → bounded DraftOutcome objects. Owner: host scope/filter/read code; Slack supplies reaction/reply data. Context/state/action effects: transient reception evidence becomes available for administrative framing. This is acquisition, not a correctness evaluator for research claims. Program selects sent posts by supplied scope (channel sends and selected DM recipient IDs; default five posts), not by an expected-answer oracle. Open operator query, not a controlled experiment. Invalid identity/workspace/channel returns null; Slack failures are caught. No per-outcome human approval or automatic policy update is admitted here.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: DraftOutcome or null; recentDraftOutcomes returns non-null selected outcomes
- Later read-back: inapplicable — this reader does not persist newly acquired outcomes; later requests reread Slack using retained sent-draft references
- Delegated visibility: Sent message timestamp/channel and bot credential reach Slack; selected response data stays in host until framing
- Selection predicate: Sent status and Slack timestamp; matching workspace organization/channel; listSentDraftsForScope with selected channel/DM scope and default limit five
- Invalidation or expiry: Missing/rebound workspace or absent channel excludes outcome; Slack failure yields partial or unknown evidence, not retraction of a sent claim
- Activation or effect: Acquires reception evidence for the administrative consumer; actual calls and reception unobserved
- Evidence limits: Thread fetch caps at 20 messages, reply text at 600 characters and opening at 120; engagement is not truth evaluation. A null failed thread read with non-null reactions passes engagementKnown, so the intended unknown distinction is not fully implemented

Evidence: SRC-1 `src/brain/auto-research/outcome.ts`, implementation. Concrete countercase deduction: reactions resolves to an array while getSlackThreadHistory rejects; its catch yields null, replies becomes empty, and `thread?.ok !== false` is true. No target execution is needed for this deduction.

> const [reactions, thread] = await Promise.all([
> 		getSlackMessageReactions(botToken, channelId, draft.slackTs).catch(
> 			() => null,
> 		),
> 		getSlackThreadHistory(botToken, channelId, draft.slackTs, {
> 			maxMessages: 20,
> 		}).catch(() => null),
> 	])
> --- `src/brain/auto-research/outcome.ts`

> const replies = (thread?.messages ?? [])
> 		.filter((m) => m.ts !== draft.slackTs)
> 		.map((m) => ({
> 			user: m.user ?? null,
> 			text: (m.text ?? "").slice(0, 600),
> 		}))
> 		.filter((m) => m.text.trim().length > 0)
> --- `src/brain/auto-research/outcome.ts`

> engagementKnown: reactions !== null && thread?.ok !== false,
> 		repliesTruncated: thread?.complete === false,
> --- `src/brain/auto-research/outcome.ts`

> const sent = listSentDraftsForScope(agent, scope, limit)
> 	if (!sent.length) return []
> 	const outcomes = await Promise.all(sent.map((d) => readOutcome(agent, d)))
> 	return outcomes.filter((o): o is DraftOutcome => o !== null)
> --- `src/brain/auto-research/outcome.ts`

#### EPI-RTE-outcome-frame
Label: Reception evidence framing

Distinct identity: deterministic transformation between [EPI-RTE-outcome-acquisition](#epi-rte-outcome-acquisition) and [EPI-RTE-admin-consumption](#epi-rte-admin-consumption); no counterpart among supplied runtime records. Owner: sentBlock code. Endpoints/progression: DraftOutcome array → text descriptions of destination/time/subject/opening and reaction counts/quoted reply text → question frame. Context/state/action effects: changes the evidence visible to the administrative model; no durable update. Program formatting is not an oracle or evidence-consuming acceptance. Non-ampliative presentation of available fields, but lineage is degraded: reply-user IDs and draft IDs are omitted, text is already truncated, and source uncertainty depends on the acquisition flag. Guidance tells the model to match subject/opening and distinguish unknown from no engagement; compliance remains unobserved.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Empty string or sent-post reception block
- Later read-back: inapplicable — formatter does not persist content; operator-supplied admin history is a separate continuation channel
- Delegated visibility: Rendered opening, destination, time, subject, reactions and reply excerpts reach model via frame; reply-user and draft IDs do not
- Selection predicate: All supplied outcomes rendered; engagementKnown chooses unknown versus reactions/replies text; repliesTruncated adds a warning
- Invalidation or expiry: inapplicable — transient formatting with no retained endorsement state
- Activation or effect: Selects model-visible representation and embeds instructions for interpreting reception
- Evidence limits: Unknown flag countercase can produce misleading 'no replies'; known absence within a bounded fetch is not comprehensive absence, nor engagement factual warrant

Evidence: SRC-1 `src/brain/admin/chat.ts`, implementation (embedded instructions are doctrine/design). A concrete deterministic input with engagementKnown true, empty reactions/replies and repliesTruncated false renders 'no reactions; no replies', regardless of why those arrays are empty.

> const engagement = !o.engagementKnown
> 			? "engagement unknown, Slack could not be read"
> --- `src/brain/admin/chat.ts`

> o.replies.length
> 						? o.replies
> 								.map((r) => `"${r.text.replace(/\s+/g, " ")}"`)
> 								.join(" | ")
> 						: "no replies",
> 					o.repliesTruncated ? "(more replies not fetched)" : "",
> --- `src/brain/admin/chat.ts`

> return `\n\nPosts this workspace's proactive research has actually sent, and how they landed. This is the only record of them, so use it when asked how something we sent was received and do not go looking in memory. Match a question to a post by its subject or opening, and never read "engagement unknown" as no engagement:\n${lines.join("\n")}`
> --- `src/brain/admin/chat.ts`

#### EPI-RTE-admin-consumption
Label: Administrative reception interpretation

Distinct identity: operator-facing fresh computeTurn consuming research outcomes, not the automatic planner or ephemeral outbound draft route [RT-RTE-research-draft](runtime.md#rt-rte-research-draft). Shares the model loop with [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn), but returns to an operator instead of Slack. Owner: operator supplies question/surfaces/history; host validates surfaces and supplies context; foreground model proposes interpretation; host returns only completed output. Operating mode: open administrative inquiry, no answer oracle. Trigger: non-refinement admin chat request. Guidance requests investigation, no invented activity, and correct unknown handling. Computational admission selects a valid surface set and actor, not an epistemic criterion for reception or draft correctness. Noncompleted turn rejected. No automatic research-policy write or accepted factual update is performed by this path. Model output may criticize a draft, but the architecture neither requires a challenged theory/blame/revision record nor establishes one without an episode.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Operator-facing reply, actual scope/surfaces and bounded tool-input trail, or error
- Later read-back: Console-held input.history (last 20 turns) can reach later admin invocations; this function writes no outcome/criticism into research planning or workspace threads
- Delegated visibility: Scoped memory/tools, question, sentBlock/pendingBlock and bounded supplied history reach computeTurn/model; returned reply reaches only operator by stated contract
- Selection predicate: Valid requested/shared surfaces; selected DM recipients govern outcome inclusion; refinement mode skips outcomes and pending blocks; completed output required
- Invalidation or expiry: Unknown surface/draft and noncompleted computation fail; failed recent outcome call falls back to an empty block; no retained acceptance decision to expire
- Activation or effect: Feedback enters a fresh model context through an implemented consumer; actual interpretive behavior and benefit unobserved. readOnly actor, scheduledRun and ephemeral flags request scoped tooling/continuation posture, not a global effect-containment guarantee
- Evidence limits: No feedback episode or causal improvement supplied; operator interpretation/possible later steering is not automatic planner adaptation. Refinement separately proposes wording for operator application and does not consume these outcomes

Evidence: SRC-1 `src/brain/admin/chat.ts`, `src/brain/turn/agent.ts`, `src/brain/turn/agent.impl.ts`, implementation. Broader HTTP/UI authorization equivalence is not assessed by these agent exposure passages.

> const outcomes = refining
> 		? []
> 		: await recentDraftOutcomes(agent, {
> 				// Shared surface covers channel sends; a person's DM replies need that
> 				// person's surface to have been selected.
> 				channel: wanted.some((s) => s.kind === "shared"),
> 				recipientUserIds: wanted.flatMap((s) =>
> 					s.kind === "dm" && s.userId ? [s.userId] : [],
> 				),
> 			}).catch(() => [])
> --- `src/brain/admin/chat.ts`

> const out = await computeTurn({
> 		agent,
> 		org,
> 		userId: person?.userId ?? slack?.installedByUserId ?? org.id,
> 		actor,
> --- `src/brain/admin/chat.ts`

> : frame(
> 					question,
> 					person?.name ?? null,
> 					wanted.map((s) => s.label),
> 					sentBlock(outcomes),
> 					pendingBlock(pending),
> 				),
> --- `src/brain/admin/chat.ts`

> // Same posture as an automation: read-only, no scheduling, no approvals.
> 		scheduledRun: true,
> 		skipBilling: true,
> 		// Borrowed context: leave nothing behind in the workspace's own threads.
> 		ephemeral: true,
> --- `src/brain/admin/chat.ts`

> async runAdminChat(input: AdminChatInput): Promise<AdminChatResult> {
> 		return (await this.loadImpl()).runAdminChat(this, input)
> 	}
> --- `src/brain/turn/agent.ts`

> export { runAdminChat } from "../admin/chat"
> --- `src/brain/turn/agent.impl.ts`

The separately inspected automatic planner's input type contains steer, prior sent/drafted bodies, roster and cost ledger, not acquired outcomes. Its prompt can follow operator steering; no `recentDraftOutcomes` caller occurs in that planner. This bounds automatic-adaptation conclusions without denying the administrative consumer.

> export type DerivePlanInput = {
> 	steer?: string
> 	sentBodies: string[]
> 	/** Awaiting review. Unsent, so the sent list won't stop us redrafting them. */
> 	draftedBodies: string[]
> 	roster: DraftRecipient[]
> 	costLedger?: BrainCostLedger
> }
> --- `src/brain/auto-research/plan.ts`

#### EPI-RTE-channel-distillation
Label: Channel durable clusters

Distinct identity: this channel-batch producer shares the downstream memory writer with [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff), but that supplied record describes interactive writeback and delayed style observation rather than this channel-batch producer.

Endpoints/progression: Slack human statements to curated clusters → Candidate clusters or empty list → Selects what enters durable memory. Owner: Fast model with structured schema; requested faithful wording and dates, not an independent truth oracle. Context/state/action effects: Requests curation and writes clusters to SQL; actual model behavior unobserved. Guidance and admission: Owned schedule and current generation; schema and durable-selection model; Channel prompt requests non-ampliative grouping; implementation does not establish faithful output. Novel added inference versus reshaping remains unresolved. Rejection/recovery: Ownership loss/reset stops work; failed batch writes retry. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: clusters in persisted batch
- Later read-back: Later writeMemories and then search/ambient consumers
- Delegated visibility: Bounded channel messages, roster and policy reach fast model
- Selection predicate: Owned schedule and current generation; schema and durable-selection model
- Invalidation or expiry: Ownership loss/reset stops work; failed batch writes retry
- Activation or effect: Requests curation and writes clusters to SQL; actual model behavior unobserved
- Evidence limits: Prompt compliance and hosted extraction are not independently checked

Evidence: SRC-1 `src/brain/slack/channel-observe.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> Lines labeled ${BOT_AUTHOR_LABEL} (bots, apps, and the brain's own prior replies) are context only: read them to make human messages make sense, but never extract a memory from them and never record the brain's own statements as facts. Capture a fact only when a HUMAN states it.
> --- `src/brain/slack/channel-observe.ts`

#### EPI-RTE-memory-admission
Label: Memory write admission

Part of: [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff)

Endpoints/progression: Document eligibility for hosted ingest → written true/false; stale successful document deleted → Permits mapping/registering eligible document; blocks stale/invalid write. Owner: Program checks nonempty content, tags, current reset epoch and service status; domain is write eligibility. Context/state/action effects: Eligible write initiates node registration and splitting. Guidance and admission: Model proposes content; program decides eligibility; no answer oracle; open work/observation; No per-document human judgment in this path; adapter status is a storage outcome, not factual endorsement. Rejection/recovery: Reset invalidates; failures return false; stale success triggers deletion. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: written boolean
- Later read-back: Caller can retry; successful document is eligible for later consumers
- Delegated visibility: Document and metadata go to hosted service
- Selection predicate: Model proposes content; program decides eligibility; no answer oracle; open work/observation
- Invalidation or expiry: Reset invalidates; failures return false; stale success triggers deletion
- Activation or effect: Eligible write initiates node registration and splitting
- Evidence limits: Deletion cascade is external; document accuracy is not tested

Evidence: SRC-1 `src/brain/memory/index.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> function isSuccessfulMemoryWrite(result: BatchItemResult): boolean {
> 	return result.status === "queued" || result.status === "done"
> }
> --- `src/brain/memory/index.ts`

#### EPI-RTE-document-retention
Label: Hosted document retention request

Part of: [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff)

Endpoints/progression: Application document and metadata enter Supermemory → Document ID and status defaulting to queued → Makes content available to hosted memory service. Owner: Hosted documents.add; internals uninspected. Context/state/action effects: Requests retention; successful end-to-end recall unobserved. Guidance and admission: Nonempty content; service response; no human approval or answer oracle; Imported human/model content is acquired. Server-side transformations cannot be classified here. Arrays of links are comma-joined; no retained raw evidence guarantee. Rejection/recovery: Client errors become upsert errors; epoch cleanup belongs to memory admission. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ID/status
- Later read-back: Hosted derived memories/chunks can reach search and ambient consumers
- Delegated visibility: Content, customId, tags and flattened metadata reach service
- Selection predicate: Nonempty content; service response; no human approval or answer oracle
- Invalidation or expiry: Client errors become upsert errors; epoch cleanup belongs to memory admission
- Activation or effect: Requests retention; successful end-to-end recall unobserved
- Evidence limits: isFullReplace and dreaming options are declared but not passed by this adapter

Evidence: SRC-1 `src/compat/routes/memories/handler-effect.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> const result = await client.documents.add({
> 					content: requestParams.content,
> --- `src/compat/routes/memories/handler-effect.ts`

#### EPI-RTE-brain-selection
Label: Brain relevance selection

Distinct part of runtime knowledge handoff: request-driven selection, not content writeback.

Endpoints/progression: Returned chunks/memories for query relevance → Formatted relevant text or none found → Selects which retained statements the foreground model sees. Owner: Opaque service similarity plus local dedup/sort/top40 and score threshold 0.3; domain is retrieval relevance. Context/state/action effects: Changes evidence visible to model; belief/action effect unobserved. Guidance and admission: Scope resolution, optional focus tags, service results and local relevance rules; Undefined similarity passes local formatting filter. Formatting retains optional IDs/filepaths but not complete document provenance. Rejection/recovery: Current scopes resolved per call; no endorsement invalidation mechanism established. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: formatted search text
- Later read-back: inapplicable — selector does not write accumulated state; enclosing checkpoint may retain results
- Delegated visibility: Query and scopes reach hosted service; selected text reaches main model
- Selection predicate: Scope resolution, optional focus tags, service results and local relevance rules
- Invalidation or expiry: Current scopes resolved per call; no endorsement invalidation mechanism established
- Activation or effect: Changes evidence visible to model; belief/action effect unobserved
- Evidence limits: No evidence that relevance implies correctness; absence is only bounded search absence

Evidence: SRC-1 `src/brain/memory/search-brain.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> export const BRAIN_RELEVANCE_THRESHOLD = 0.3
> --- `src/brain/search-brain-format.ts`

#### EPI-RTE-reply-check
Label: Reply shape check

Part of: [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn)

Endpoints/progression: Sanitized reply string publishability → Boolean publishable → Supplies gate decision; does not itself publish. Owner: Regex/parse-based program; domain is selected malformed shapes, not semantic truth. Context/state/action effects: Returns predicate used by selectTurnReply. Guidance and admission: Program applies listed malformed-reply patterns; no oracle; CJK plus Latin letters fails even when bilingual text is valid. Falsehood in ordinary English can pass. Rejection/recovery: inapplicable — no retained result. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: publishable Boolean
- Later read-back: inapplicable — check does not retain a result for a later invocation
- Delegated visibility: inapplicable — deterministic local program makes no delegation
- Selection predicate: Program applies listed malformed-reply patterns; no oracle
- Invalidation or expiry: inapplicable — no retained result
- Activation or effect: Returns predicate used by selectTurnReply
- Evidence limits: Not a factual evaluator and not a comprehensive language/format validator

Evidence: SRC-1 `src/brain/observability/reply-quality.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> // A malformed reply must never reach Slack. Semantic quality is observed in
> // PostHog and does not affect runtime delivery.
> --- `src/brain/observability/reply-quality.ts`

#### EPI-RTE-reply-selection
Label: Reply selection gate

Part of: [RT-RTE-slack-turn](runtime.md#rt-rte-slack-turn)

Endpoints/progression: Which candidate string may become final reply → Selected reply/source or empty → Suppresses failing candidates; may select older assistant draft as recovery. Owner: Program consumes publishability Boolean and orders sources: terminal, text, longest acceptable transcript text. Context/state/action effects: Chooses text for delivery rather than judging factual support. Guidance and admission: Host decides; malformed predicate can veto; no reference-answer oracle; open task; Longest transcript draft need not be the most current or best supported. Caller owns empty fallback. Rejection/recovery: inapplicable — no retained gate state. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reply and source
- Later read-back: inapplicable — selector does not persist evidence; enclosing memory writeback is separate
- Delegated visibility: inapplicable — no additional model call
- Selection predicate: Host decides; malformed predicate can veto; no reference-answer oracle; open task
- Invalidation or expiry: inapplicable — no retained gate state
- Activation or effect: Chooses text for delivery rather than judging factual support
- Evidence limits: No evidence-consuming semantic acceptance criterion

Evidence: SRC-1 `src/brain/turn/finalization/output.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> function publishable(text: string): string {
> 	const reply = sanitizeSlackReply(text)
> 	return isPublishableSlackReply(reply) ? reply : ""
> }
> --- `src/brain/turn/finalization/output.ts`

#### EPI-RTE-style-generation
Label: Human-evidence style notes

Part of: [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff)

Endpoints/progression: Human reactions to generalized team preference and operating note → Short note or empty/non-note → Proposes later style guidance. Owner: Fast model prompted to verify direct HUMAN evidence; remaining program only recognizes non-note phrases. Context/state/action effects: Generates behavior-shaping candidate from interaction trace. Guidance and admission: Model proposes; HUMAN-only policy and isNonNote filter; no answer oracle; Speaker labels bound intended evidence, but prompt compliance is not enforced by semantic comparison. Preference attribution is truth-apt; resulting guidance also changes non-truth-apt policy. Rejection/recovery: Reset/ownership guards; retry without cursor advance on write failure. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: note text
- Later read-back: Carried last-eight-line/1200-character context reaches next observation; hosted notes reach style loader
- Delegated visibility: Bounded labeled messages plus prior carried state reach fast model
- Selection predicate: Model proposes; HUMAN-only policy and isNonNote filter; no answer oracle
- Invalidation or expiry: Reset/ownership guards; retry without cursor advance on write failure
- Activation or effect: Generates behavior-shaping candidate from interaction trace
- Evidence limits: No concrete generated note or independent evidence comparison supplied

Evidence: SRC-1 `src/brain/turn/interaction-observe.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> Before writing a note, verify that every claimed preference has direct HUMAN evidence in these messages. If the evidence exists only in AGENT_OR_BOT text, output nothing. For example, if only the agent says "no cap," do not infer that the team wants slang. If a human says "I like when you say no cap," you may generalize that explicit reaction into a durable style preference.
> --- `src/brain/turn/interaction-observe.ts`

#### EPI-RTE-style-admission
Label: Style note admission

Part of: [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff)

Endpoints/progression: Non-note filtering and current-generation style write eligibility → Skip, retry, stale, complete/continue → Admits agent-self note and advances carried cursor only after successful status. Owner: Program uses phrase filter, public surface and workspace/generation checks, service queued/done status. Context/state/action effects: Admits durable style guidance, not provider parameter updates. Guidance and admission: Model proposes; software decides; humans can react but do not approve each note; open observation; Human evidence verification is model-requested, not a separately consumed evidence judgment. Rejection/recovery: Reset clears cursor and registry; stale late documents deleted; errors retry. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: status and carried cursor
- Later read-back: loadInteractionStyleProfile filters person scope and recognized service buckets, renderInteractionStyle supplies context; runtime compute consumes it
- Delegated visibility: Note to hosted service; selected facets later reach foreground model
- Selection predicate: Model proposes; software decides; humans can react but do not approve each note; open observation
- Invalidation or expiry: Reset clears cursor and registry; stale late documents deleted; errors retry
- Activation or effect: Admits durable style guidance, not provider parameter updates
- Evidence limits: Hosted bucket assignment is opaque; later behavior change and improved capacity unobserved

Evidence: SRC-1 `src/brain/turn/interaction-observe.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> if (result.status !== "queued" && result.status !== "done") {
> 			return "retry"
> 		}
> --- `src/brain/turn/interaction-observe.ts`

#### EPI-RTE-draft-check
Label: Research draft quality flags

Part of: [RT-RTE-research-draft](runtime.md#rt-rte-research-draft)

Endpoints/progression: Draft length and presence of evidence-producing tool names → Over-length/no-tool-evidence flags → Allows flagged real draft to remain reviewable. Owner: Program counts words and classifies tool names in trace; not evidence entailment or source truth. Context/state/action effects: Annotates rather than blocks a nonempty draft. Guidance and admission: Program assesses; reviewer may withhold send; no correctness oracle; open drafting; Runtime baseline mentioned flags but did not individuate evaluator domain. A tool-name witness can coexist with unsupported claims. Rejection/recovery: Reset/ownership stops insertion; noncompleted/empty drafts dropped. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: draft including flags and collected sources
- Later read-back: Stored draft/flags can be reviewed; prior body guides next planning
- Delegated visibility: Selected trace and body cross isolated draft-turn boundary
- Selection predicate: Program assesses; reviewer may withhold send; no correctness oracle; open drafting
- Invalidation or expiry: Reset/ownership stops insertion; noncompleted/empty drafts dropped
- Activation or effect: Annotates rather than blocks a nonempty draft
- Evidence limits: No observed review or source-consuming factual acceptance decision

Evidence: SRC-1 `src/brain/auto-research/draft.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> // Over budget and unevidenced are quality problems, not reasons to bin a real
> 	// draft: the reviewer can read it and decide. Only an empty or absent note goes.
> --- `src/brain/auto-research/draft.ts`

#### EPI-RTE-draft-send
Label: Reviewed draft send permission

Part of: [RT-RTE-research-draft](runtime.md#rt-rte-research-draft)

Endpoints/progression: Stored draft permission for Slack delivery → Posted/sent status or error → Delivers stored body; successful target earns watchlist slot. Owner: Reviewer chooses ID; program checks draft status, entitlement, workspace and target. Context/state/action effects: May post body and update watchlist; actual successful delivery unobserved. Guidance and admission: Human selects; program admits/claims; entitlement/workspace can veto; no oracle; Human selection is not automatically evidence-consuming epistemic acceptance. Body is sent without flags forcing a refusal. Rejection/recovery: Failure releases send claim; sent status prevents another local claim. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: send result
- Later read-back: Sent body enters later planning; watch target persists; sent-draft references also select reception evidence for the administrative consumer [EPI-RTE-admin-consumption](#epi-rte-admin-consumption)
- Delegated visibility: Stored body goes to Slack
- Selection predicate: Human selects; program admits/claims; entitlement/workspace can veto; no oracle
- Invalidation or expiry: Failure releases send claim; sent status prevents another local claim
- Activation or effect: May post body and update watchlist; actual successful delivery unobserved
- Evidence limits: No measured quality or causal improvement

Evidence: SRC-1 `src/brain/auto-research/send.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> const res = await postSlackMessageIdempotent(
> 		botToken,
> 		channelId,
> 		draft.body,
> 		draft.id,
> 	)
> --- `src/brain/auto-research/send.ts`

#### EPI-RTE-topic-partition
Label: Topic partition reshaping

No runtime counterpart after comparison: runtime explicitly left splitting to specialists.

Endpoints/progression: Index grouping of existing document IDs into child topics → Child mapping/tag changes or skipped failed update → Moves retrieval organization without changing existing memory statements. Owner: Fast model proposes children; program normalizes keys/indexes, excludes other, later-child-wins, moves after metadata success. Context/state/action effects: Repoints documents and registers child tags. Guidance and admission: Model proposes partition; code chooses valid indexes and winning update; no oracle; Requested coherent subthemes are not validated semantically. Descriptive labels are model interpretations, not proven taxonomy truth. Rejection/recovery: Epoch check and per-node lock; metadata failure leaves that child at parent. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: inapplicable — background function returns void
- Later read-back: Updated paths and tags guide subsequent tree/retrieval access
- Delegated visibility: Sample texts reach fast model; metadata requests reach service
- Selection predicate: Model proposes partition; code chooses valid indexes and winning update; no oracle
- Invalidation or expiry: Epoch check and per-node lock; metadata failure leaves that child at parent
- Activation or effect: Repoints documents and registers child tags
- Evidence limits: No acceptance-before-integration finding; hosted metadata effects unobserved

Evidence: SRC-1 `src/brain/memory/split.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> const SPLIT_THRESHOLD = 125
> const SPLIT_SAMPLE_CAP = 160
> --- `src/brain/memory/split.ts`

#### EPI-RTE-reset-withdrawal
Label: Generation withdrawal and cleanup

Distinct identity: reset withdrawal spans the writeback/style state of [RT-RTE-knowledge-handoff](runtime.md#rt-rte-knowledge-handoff) and research state of [RT-RTE-research-draft](runtime.md#rt-rte-research-draft); it is not a material part of exactly one supplied route.

Endpoints/progression: Eligibility of old-generation memory and observation state → Old writes blocked/deleted; local state cleared → Prevents deleted carried style from regenerating and stale writes mapping into new registry. Owner: Program advances epoch, clears observer/cursor/registry/research state, cancels schedules; writers delete stale late document. Context/state/action effects: Withdraws old state from local eligibility. Guidance and admission: Program generation predicate; not truth judgment or answer oracle; resetMemoryRegistry is local reset component, not proof all remotely retained content was deleted. Cascade comment is an external-service assertion. Rejection/recovery: Clears cursors and registry; cancellation failures swallowed; hosted deletion contract external. Operating mode: open task, continuous observation or operator-directed research as described above, not a controlled experiment. Answer oracle: none supplied; model judgment and service status are not reference outcomes.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: reset completion; cleanup may throw
- Later read-back: Fresh generation affects subsequent observers/writers
- Delegated visibility: Stale deletion document ID reaches hosted service
- Selection predicate: Program generation predicate; not truth judgment or answer oracle
- Invalidation or expiry: Clears cursors and registry; cancellation failures swallowed; hosted deletion contract external
- Activation or effect: Withdraws old state from local eligibility
- Evidence limits: Complete remote purge and end-to-end stale-read prevention not established

Evidence: SRC-1 `src/brain/turn/agent.impl.ts`, implementation. Requested model behavior within quoted prompts is doctrine/design, not proof of semantic compliance.

> clearInteractionObserveState(agent)
> 	clearBrainProfileSync(agent)
> 	clearBrainMemoryRegistry(agent)
> --- `src/brain/turn/agent.impl.ts`

Additional load-bearing implementation passages for the concrete deductions and consumer bounds:

> const withEvent =
> 		eventDate && !base.includes(eventDate)
> 			? `${base} (as of ${eventDate})`
> 			: base
> --- `src/brain/memory/writeback.ts`

> const content = withEvent.startsWith("DOCUMENT_DATE:")
> 		? withEvent
> 		: `DOCUMENT_DATE: ${utcDateString(now)}\n${withEvent}`
> --- `src/brain/memory/writeback.ts`

> if (looksLikeTurnOutput(whole) && typeof whole.reply === "string") {
> 		out = whole.reply.replace(ZERO_WIDTH_CHARS, "").trim()
> 	}
> --- `src/brain/observability/reply-quality.ts`

> r.similarity === undefined || r.similarity >= BRAIN_RELEVANCE_THRESHOLD
> --- `src/brain/search-brain-format.ts`

> for (const bucket of row.buckets ?? []) {
> 			const facet = BUCKET_TO_FACET[bucket]
> 			if (!facet) continue
> --- `src/brain/memory/interaction-style.ts`

> if (!trace.some((entry) => toolProducesEvidence(entry.tool)))
> 		flags.push("no tool evidence behind this, it may be riffing from memory")
> --- `src/brain/auto-research/draft.ts`

> if (looksLikeTurnOutput(whole) && typeof whole.reply === "string") {
> 		out = whole.reply.replace(ZERO_WIDTH_CHARS, "").trim()
> 	}
> --- `src/brain/observability/reply-quality.ts`

### Claims

#### EPI-CLM-team-answers
Label: Answers from team evidence

Claimed operation: answers use conversations and connected tools rather than internet or guesswork. Source: SRC-1 `README.md`, doctrine/design. Closest supplied claim [RT-CLM-write-approval](runtime.md#rt-clm-write-approval) concerns effect permission, not this distinct warrant claim.

> 💬 **Answers from your team** | Not from the internet, not from guesswork: from your own conversations and connected tools.
> --- `README.md`

#### EPI-CLM-current-memory
Label: Memory kept current

Claimed operation: remembers decisions/context and keeps them current as people talk. Source: SRC-1 `README.md`, doctrine/design. No counterpart among supplied runtime claims.

> 🧠 **Remembers** | Decisions, projects, owners and context from the channels it's in, kept current as people talk. No one has to write anything down.
> --- `README.md`

#### EPI-CLM-evidence-check
Label: Pre-send evidence check

Claimed operation: model must trace claims to seen records or label inference, state absence coverage, and fix failing answers. Source: SRC-1 `src/brain/prompt/system.ts`, doctrine/design. Distinct from supplied delivery-fencing and approval claims; those enforce coordination/permission, not answer warrant.

> Before sending, check the answer against the evidence: every claim traces to a record you actually saw or is labeled as inference, and an absence claim states what was covered. If the check fails, fix the answer, not the phrasing.
> --- `src/brain/prompt/system.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; each route retains its consumer, channel, force and horizon in the ledger rather than allocating duplicate identities.
