---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "RightMemory epistemic routes: evidence reconciliation, structural admission, correction guidance and shared-view reliance."
run-id: AAS-2026-11-08-rightmemory-cbec05309c2b-01
reviewed-boundary: "62534bd82c58718f31c99692fed4c5d159e218ec"
---

# RightMemory epistemic report

## Source-and-claim boundary

This report asks how submitted evidence becomes reusable context or guidance, what checks license reliance, and what later consumers can do with it. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); sources are see [Source register](boundary.md#source-register). SRC-1 supplies implementation, doctrine/design and reported operation, not observed runs or causal experiments. Provider weights, actual host behavior, private memory roots and private benchmark traces remain unavailable. This prevents conclusions about exercised acceptance, factual accuracy, causal task benefit and improved capacity.

Runtime findings are provisional supplied evidence, not an inspection ceiling. Direct reads added the module admission rules, all four Update/Retrieve/Pruner/Insight prompts, builder prompt, guidance capture/review, shared-view builder/approval/question operations, structural validation body, entry dispatch and MCP registration. All are SRC-1 at the frozen commit. The countercase search deliberately included manual curation, sync, imports and live provider questions: an ordinary Update gate cannot characterize all admission, and internal source rendering cannot characterize every answer route.

Consequential design claims are [EPI-CLM-memory-admission](#epi-clm-memory-admission), [EPI-CLM-correction-cases](#epi-clm-correction-cases) and [EPI-CLM-retrieval-coverage](#epi-clm-retrieval-coverage); publication's narrower claim is see [RT-CLM-native-publication](runtime.md#rt-clm-native-publication). No claim of a universal factual oracle is inferred from these.

| Entry point or operation | Source path, SRC-1 | Coverage and records / conclusion prevented |
| --- | --- | --- |
| Installed dispatch, validation, MCP | `rightmemory/entrypoint.py`, `rightmemory/mcp.py` | Direct dispatch and three registered MCP tools inspected; Retrieve/submit route findings see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update); capture adds [EPI-RTE-guidance-capture](#epi-rte-guidance-capture). |
| Native assistant prepare/submit/complete | `rightmemory/assistant.py`, `rightmemory/assistant_context.py`, `rightmemory/assistant_write.py` | Supplied findings see [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant); no independent host trace. |
| Agent and embedding retrieval | `rightmemory/retrieve_selection.py`, `rightmemory/embedding_retrieval.py` | Supplied implementation findings see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval); direct Retrieve prompt read. No exhaustive renderer audit added. |
| Update and structural gate | `rightmemory/prompts/update.md`, `rightmemory/reference/MEMORY_RULES.md`, `rightmemory/tools.py` | Direct semantic criteria and validation body; supplied publication details see [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update). |
| Pruner, Insight, Historian | `rightmemory/prompts/pruner.md`, `rightmemory/prompts/insight.md`, `rightmemory/runtime.py` | Direct first two prompts; supplied scheduler/executor/history findings see [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles). Historical completeness not independently assessed. |
| Maintenance and Pursuit editor | `skills/maintain-rightmemory/SKILL.md`, `rightmemory/pursuit_store.py` | Supplied findings see [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor); no inference of universal user approval. |
| Guidance inbox and reviewed curation | `rightmemory/guidance.py`, `skills/review-agent-guidance-inbox/SKILL.md` | Direct capture and approval procedure; [EPI-RTE-guidance-capture](#epi-rte-guidance-capture), [EPI-RTE-guidance-review](#epi-rte-guidance-review). |
| Edit feedback | `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md` | Direct rules and Update's late-check request; [EPI-OBJ-corrections](#epi-obj-corrections). Actual user correction artifacts unavailable. |
| Sync and shared-file imports | `rightmemory/sync.py`, `rightmemory/shared_view_files.py` | Supplied findings see [RT-RTE-sync-admission](runtime.md#rt-rte-sync-admission), [RT-RTE-file-import](runtime.md#rt-rte-file-import); all Git transport, repair and revocation combinations not independently audited. Prevents complete withdrawal guarantee. |
| Shared-view creation/refresh/approval | `rightmemory/shared_view_builder.py`, `rightmemory/shared_view_files.py`, `rightmemory/prompts/shared-view-builder.md` | Direct relevant build, refresh, extractive render and approval bodies; [EPI-RTE-view-build](#epi-rte-view-build), [EPI-RTE-view-approval](#epi-rte-view-approval). |
| Live provider questions | `rightmemory/shared_view_questions.py` | Direct request, provider execution, timeout/error and answer wrapping; [EPI-RTE-provider-question](#epi-rte-provider-question). External providers remain opaque. |
| Retrieval evaluators | `experiments/README.md` | Direct full report read, attributed operation only; [EPI-CLM-retrieval-coverage](#epi-clm-retrieval-coverage). Harness implementation not independently audited; raw labels/traces unavailable. |
| Agent-file collection | `rightmemory/agent_files.py` | Direct catalog discovery/hash grouping inspected. No traced later semantic consumer here; catalog availability does not establish authority. Remaining CLI/storage operations unassessed. |
| Other installation/hooks, manager/onboarding, hub and web frontend paths | `rightmemory/install_core.py`, `skills/`, `rightmemory/hub/`, `rightmemory/web/` | Boundary inventory or supplied runtime coverage only; detailed independent hook, host prompt and authorization audits not performed. Prevents system-complete negative about additional evaluators or behavioral routes. |

Available but uninspected branches are not access gaps or evidenced absences. This is a sparse epistemic assessment of named paths, not an exhaustive absence proof.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-memory](#epi-obj-memory) | Facts, interpretations, scoped decisions and rules; questions are not assertions | see [EPI-CLM-memory-admission](#epi-clm-memory-admission) | SRC-1 `rightmemory/reference/MEMORY_RULES.md` | No actual stored claim or initial warrant supplied. |
| [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | Prior attempt/redirection/outcome contrast and applicability | see [EPI-CLM-correction-cases](#epi-clm-correction-cases) | SRC-1 `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md` | A contrast is not a causal test of a generalized lesson. |
| [EPI-OBJ-corrections](#epi-obj-corrections) | Exact candidate and rejected/accepted edit contrast | Operational curation feedback | SRC-1 `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md` | No independent semantic adjudicator or executed correction supplied. |
| [EPI-OBJ-guidance-inbox](#epi-obj-guidance-inbox) | User redirection or direct-guidance evidence | Pending, not formal guidance | SRC-1 `rightmemory/guidance.py` | Caller interpretation and completeness unknown. |
| [EPI-OBJ-view-document](#epi-obj-view-document) | Selected or rewritten provider memory | Shareable context | SRC-1 `rightmemory/shared_view_files.py` | Extractive and generative lineage differ; approval is permission, not truth. |
| [EPI-OBJ-retriever-policy](#epi-obj-retriever-policy) | Mostly policy; factual assumptions may be embedded | Provider-side question instructions | SRC-1 `rightmemory/shared_view_questions.py` | Native policy text is not independently checked for semantic fidelity. |
| [EPI-OBJ-view-permission](#epi-obj-view-permission) | No truth-apt content update from approval metadata | Permission to distribute or answer | SRC-1 `rightmemory/shared_view_files.py` | A flag is not a factual acceptance decision. |
| [EPI-OBJ-question-answer](#epi-obj-question-answer) | Provider response, potentially truth-apt | Answered/unavailable result | SRC-1 `rightmemory/shared_view_questions.py` | Concrete proposition not determinable without response; status does not establish correctness. |
| [EPI-OBJ-insight-logs](#epi-obj-insight-logs) | Patterns, tensions and possible recommendations | Reflection for future work | SRC-1 `rightmemory/prompts/insight.md` | No produced instance or acceptance decision supplied. |
| [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions) | Mostly policy rather than assertions about a user's world | see [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions) | SRC-1 `rightmemory/prompt.py` | Model interpretation not compliance. |
| [RT-OBJ-runtime-config](runtime.md#rt-obj-runtime-config), [RT-OBJ-semantic-operation](runtime.md#rt-obj-semantic-operation) | No world-claim change from dispatch/phase state alone | see cited records | SRC-1 `rightmemory/config.py`, `rightmemory/runtime.py` | State labels do not grant semantic warrant. |
| [RT-CMP-role-model](runtime.md#rt-cmp-role-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-reranker-model](runtime.md#rt-cmp-reranker-model) | Distributed-parametric inference/ranking, not individually recoverable propositions | see cited records | SRC-1 `rightmemory/runtime.py`, `rightmemory/embedding_models.py` | No accessible weights, training evidence or exact deployed identity; no operational parameter update established in inspected callers. |

## Authority-route ledger

Each row is a separate consequential function; repeated route citations identify different phases of the same declared referent, not new declarations. Record-owned endpoints, activation, recovery and evidence fields are see the cited record. Here “unknown warrant” means the source claim's factual warrant has not been established; faithful text transport does not improve it.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-guidance-capture](#epi-rte-guidance-capture) | retention | implemented | [EPI-OBJ-guidance-inbox](#epi-obj-guidance-inbox) | truth-apt transformation: acquisition/import | Incoming evidence text | Nonempty session/evidence and inbox parser; syntactic domain | see [EPI-RTE-guidance-capture](#epi-rte-guidance-capture) | Pending inbox entry | Enforcing write transaction | Unknown source warrant; no formal guidance acceptance | Save evidence for later review | Review host; inbox text; advisory evidence; later explicit review | SRC-1 `rightmemory/guidance.py` | none | none | No observed run.  |
| [EPI-RTE-guidance-review](#epi-rte-guidance-review) | disposition/acceptance | doctrine only | [EPI-OBJ-guidance-inbox](#epi-obj-guidance-inbox) | no content change | Proposed meaning, scope and destination | Human explicitly approves host proposal against module rules; intended use is future behavior guidance | see [EPI-RTE-guidance-review](#epi-rte-guidance-review) | Approve, reject, already covered, defer | Procedural human veto | Approval licenses requested guidance within approved scope; factual truth not independently checked | Authorize only approved semantic changes | Host editor; explicit approval; permissive; current curation | SRC-1 `skills/review-agent-guidance-inbox/SKILL.md` | none | none | Protocol, not enforced per-write gate. |
| [EPI-RTE-guidance-review](#epi-rte-guidance-review) | lifecycle integration | doctrine only | [EPI-OBJ-memory](#epi-obj-memory); [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | truth-apt transformation: indeterminate | Approved semantic proposal → scoped canonical guidance and inbox removal | Host applies approved meaning and validates in clean worktree | see [EPI-RTE-guidance-review](#epi-rte-guidance-review) | Merged/replaced guidance and evidence disposition | Skill protocol | Conditional on prior approval; new generalized wording needs separate warrant | Land exact validated change; preserve deferred evidence | Future retrieval then host; source text; advisory; cross-session | SRC-1 `skills/review-agent-guidance-inbox/SKILL.md` | none | none | Semantic preservation versus new generalization depends on unavailable proposal/output. |
| [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | check/evidence production | implemented | [EPI-OBJ-memory](#epi-obj-memory); [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | no content change | Durability, usefulness, clear scope, overlap, evidence clarity and stale claims | Role model under module rules and late corrections check; semantic relevance to future work | see [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | Keep/merge/skip/edit judgment, question or uncertain state | Natural-language criteria requested | Fallible evidence-informed candidate assessment, not independent corroboration | Shape proposal; model can reject all candidates | Update model; prompt plus candidates/current state; advisory instructions; current operation | SRC-1 `rightmemory/prompts/update.md` | [EPI-CLM-memory-admission](#epi-clm-memory-admission) | none | No observed run.  |
| [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | content transformation | implemented | [EPI-OBJ-memory](#epi-obj-memory); [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | truth-apt transformation: indeterminate | Candidates/current state → revised wording | Role model; no supplied input/output pair | see [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | Revision, compression, new scoped inference or no change | Model edits in candidate tree | No concrete entailed or ampliative claim established without instances | Produce candidate commit | Supervisor; candidate files; proposed state; current operation | SRC-1 `rightmemory/prompts/update.md` | none | none | Reshaping, entailment and conjecture remain possible; non-entailment not evidenced. |
| [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | check/evidence production | implemented | [EPI-OBJ-memory](#epi-obj-memory); [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | no content change | Committed paths, file modes, semantic base and graph/correction structure | Supervisor and MemoryTools.validate_memory; structural domain | see [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | Validation pass/failure | Enforcing validation at publication | Structure only; no factual oracle; correction capacity exception is see record | Report eligibility or reject candidate | Supervisor; commit/validation result; enforcing; publication attempt | SRC-1 `rightmemory/isolated_write.py` | none | none | No observed run.  |
| [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory](#epi-obj-memory); [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | no content change | Validated proposed state → active root | Supervisor, applicable validation and base fencing | see [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | Landed/no-change/rejected/prepared | Enforcing publication checks | Operational admission is not evidence of accepted ampliative knowledge | Allow state to reach later retrieval | Active root and retriever; Git files; permissive admission then advisory delivery; later invocations | SRC-1 `rightmemory/isolated_write.py` | none | none | No observed run.  |
| [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory](#epi-obj-memory) | no content change | Native prepared edits → completion receipt | Host semantic judgment, program validates completion; same structural/factual distinction | see [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant) | Receipt, reject, retry | Program enforces inspected completion checks | Receipt attests publication, not correctness | Make committed content available; native retrieval independently host-selected | Native host; live files/handoff; advisory context; current and later tasks | SRC-1 `rightmemory/assistant_write.py` | [RT-CLM-native-publication](runtime.md#rt-clm-native-publication) | none | No observed run.  |
| [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | content transformation | implemented | [EPI-OBJ-memory](#epi-obj-memory); [EPI-OBJ-agent-corrections](#epi-obj-agent-corrections) | truth-apt transformation: non-ampliative reshaping | Selected IDs/ranges → source-derived return | Model relevance judgment; symbolic source resolver and output-size constraint | see [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) | Rendered content or failed selector | Selection plus structural enforcement | Preserves selected source wording, unknown initial warrant; relevance not proven | Supply context rather than synthesize an answer | Host; retrieval return; advisory; current task and repeat retrieval | SRC-1 `rightmemory/retrieve_selection.py` | none | none | No observed run.  |
| [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory](#epi-obj-memory) | no content change | Ranked source entries → returned set | Embedding similarity then reranker/count limits; ranking domain | see [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval) | Top entries even without stored answer | Ranking | Neither similarity nor answered-need guarantee is truth warrant | Prioritize source context | Host; selected original text; ranking/advisory; query | SRC-1 `rightmemory/embedding_retrieval.py` | [EPI-CLM-retrieval-coverage](#epi-clm-retrieval-coverage) | none | No observed run.  |
| [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory](#epi-obj-memory) | no content change | Prune stale active surface | Due code then model comparison of boundary/current meaning, active patterns, Pursuit references and grace | see [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles) | Remove or preserve; checkpoint ledger | Deletion admission plus procedural semantic judgment | Unchanged text is not false text; age is not refutation | Withdraw active retrieval availability; keep grace/history route | Future retriever; remaining files and historian; enforcing active-set change; generations | SRC-1 `rightmemory/prompts/pruner.md` | none | none | No observed run.  |
| [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles) | content transformation | implemented | [EPI-OBJ-insight-logs](#epi-obj-insight-logs) | truth-apt transformation: indeterminate | Memory/prior logs → possible reflection | Insight model judges meaningfulness; source limited to memory root | see [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles) | New log or no-op | Role request and scoped publication | Possible conjecture; no evidenced accepted ampliative claim | Retain separate logs, not promote to active Memory | Later Insight model; prior logs; advisory; later cycles | SRC-1 `rightmemory/prompts/insight.md` | none | none | No content-directed criticism/revision trace or concrete new proposition supplied. |
| [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-memory](#epi-obj-memory) | truth-apt transformation: indeterminate | Explicit requested maintenance edits | Host/user-scoped judgment plus instructed validation and base fences | see [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) | Changed canonical files or stop | Skill protocol | Requested edit authorization not universal truth acceptance | Afford direct state revision outside Update | Host then retriever; worktree/files; permissive then advisory; later sessions | SRC-1 `skills/maintain-rightmemory/SKILL.md` | none | none | Supplied findings only; host compliance unobserved. |
| [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor) | behavior/policy adaptation | implemented | Pursuit state — see [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor) | non-truth-apt policy/content update: human direction-map changes | User direction operations → canonical Pursuit map | Allowed symbolic operations, revision fence and graph validator; not a factual evaluator | see [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor) | New intended directions and opening context | Enforcing allowed map changes | User authority over intent, not world truth | Change direction supplied to later agent work | Host; opening-context/Pursuit text; advisory; future tasks | SRC-1 `rightmemory/pursuit_store.py` | none | none | No observed host adoption. |
| [RT-RTE-sync-admission](runtime.md#rt-rte-sync-admission) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory](#epi-obj-memory) | truth-apt transformation: acquisition/import | Upstream state → validated active candidate | Allowlist/graph validation and possible reconciler; structural domain | see [RT-RTE-sync-admission](runtime.md#rt-rte-sync-admission) | Admitted state or repair/rejection | Enforcing structural admission | Imported warrant unknown; local Update semantic judgment not required | Change sources available to retrieval | Retriever/host; synchronized files; permissive then advisory; later calls | SRC-1 `rightmemory/sync.py` | none | none | No observed run.  |
| [RT-RTE-file-import](runtime.md#rt-rte-file-import) | lineage/freshness/recovery | implemented | [EPI-OBJ-shared-view](#epi-obj-shared-view) | truth-apt transformation: acquisition/import | External package → persistent local import | Expected identity/namespace/package validation; failed refresh may keep old valid import | see [RT-RTE-file-import](runtime.md#rt-rte-file-import) | Fresh/stale/unavailable | Enforcing package checks, freshness status | Provider attribution, unknown factual warrant; stale does not imply false | Continue serving valid stale source or replace | Readers/host; imported files and status; advisory; until refresh | SRC-1 `rightmemory/shared_view_files.py` | none | none | No observed run.  |
| [EPI-RTE-view-build](#epi-rte-view-build) | content transformation | implemented | [EPI-OBJ-shared-view](#epi-obj-shared-view) | truth-apt transformation: non-ampliative reshaping | Extractive selected blocks → view distribution | Symbolic block selector, renderer and structural validator | see [EPI-RTE-view-build](#epi-rte-view-build) | Source lines selected with ancestry and exclusions | Enforcing deterministic extraction | Selected text preserved; omitted context can limit interpretation; no new fact derived | Construct shareable subset | Package consumers; dist Markdown; advisory context; after publication/import | SRC-1 `rightmemory/shared_view_files.py` | none | none | No observed run.  |
| [EPI-RTE-view-build](#epi-rte-view-build) | content transformation | implemented | [EPI-OBJ-shared-view](#epi-obj-shared-view) | truth-apt transformation: indeterminate | Generative rewrite of mixed private/shareable memory | Builder model plus schema-valid compiler; not semantic equivalence check | see [EPI-RTE-view-build](#epi-rte-view-build) | Rewritten dist or tool failure | Model generation and structural admission | No demonstrated faithful meaning, new entailment or accepted novelty | Prepare shareable candidate; refresh can retain approval | External retrievers; generated Markdown; advisory; subsequent publication | SRC-1 `rightmemory/prompts/shared-view-builder.md` | none | none | No concrete output pair; missing semantic checks cannot itself prove non-entailment. |
| [EPI-RTE-view-approval](#epi-rte-view-approval) | operational admission/selection/consumption | implemented | [EPI-OBJ-shared-view](#epi-obj-shared-view) | non-truth-apt policy/content update: approved flag | Structurally valid view → publication permission | Caller invokes approval; code validates then sets approved; no per-proposition evidence decision | see [EPI-RTE-view-approval](#epi-rte-view-approval) | Approved or structural error | Permissive metadata with code checks | Distribution authorization only | Enable sharing and later approved refresh publication | Publishers; recipe approved flag; permissive; until changed; refresh preserves old approval | SRC-1 `rightmemory/shared_view_files.py` | none | none | No observed run.  |
| [EPI-RTE-provider-question](#epi-rte-provider-question) | operational admission/selection/consumption | implemented | [EPI-OBJ-question-answer](#epi-obj-question-answer) | truth-apt transformation: acquisition/import | Provider response → consumer-visible answer | Approved configuration, token gate at token verification, started/answer timeouts and status parsing; availability domain | see [EPI-RTE-provider-question](#epi-rte-provider-question) | Answered/unavailable | Availability enforcement; no factual acceptance gate | Answered means completed provider response, not verified truth | Return response for caller interpretation | Requesting caller; formatted answer/status; advisory; current question | SRC-1 `rightmemory/shared_view_questions.py` | none | none | Provider role may reshape or select; content relation inside provider is indeterminate. |

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-memory-admission](#epi-clm-memory-admission) | see claim | SRC-1 `rightmemory/reference/MEMORY_RULES.md`, doctrine/design | see claim | [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) | None supplied | No causal comparison; model interprets all semantic criteria | Program requests scoped evidence-grounded context and preserves useful uncertainty | Policy is not proof that every stored assertion passes a truth test. |
| [EPI-CLM-correction-cases](#epi-clm-correction-cases) | see claim | SRC-1 `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`, doctrine/design | see claim | [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update), [EPI-RTE-guidance-review](#epi-rte-guidance-review) | None supplied | User contrast and recurrence judgment do not identify causal transfer | Concrete cases and generalized behavior rules have distinct admission criteria | No measured improvement or automatic guarantee of recurrence. |
| [EPI-CLM-retrieval-coverage](#epi-clm-retrieval-coverage) | see claim | SRC-1 `experiments/README.md`, reported operation | see claim | [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval) | No inspectable raw trace registered | Private, agent-labelled small corpus; model/count/render/interface comparisons differ; component effects not independently identified by this analysis | Attributed required-ID coverage and latency, not independent factual-answer accuracy | Fixed-count selection still returns results on no-answer cases; source explicitly acknowledges this. |
| [RT-CLM-native-publication](runtime.md#rt-clm-native-publication) | see claim | SRC-1 `skills/rightmemory-assistant/SKILL.md`, doctrine/design | see claim | [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant) | None supplied | Publication receipt not semantic accuracy or exercised host honesty | Prepared work and landed state differ | No warrant for content truth follows from completion. |

## Bounded conclusion

RightMemory has several distinct checks, not one epistemic evaluator. Update requests an evidence-consuming semantic judgment against durability, future usefulness, scope, duplication and evidence clarity. Its model may skip, revise, retain uncertainty or preserve questions. A separate deterministic gate checks publishable structure and scope. Neither a structural pass nor a landed commit establishes the factual correctness of a stored claim. No concrete produced accepted ampliative claim is evidenced by these source instructions alone. See [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update), [EPI-CLM-memory-admission](#epi-clm-memory-admission) and [EPI-CLM-correction-cases](#epi-clm-correction-cases).

The ordinary agent path returns resolved stored text, not free-form model answers. Embedding/reranking selects source entries but supplies no answer-absence or truth oracle. Those paths preserve selected wording without creating initial warrant; missing source provenance stays unknown. Native retrieval has a different host-authored result path, and provider questions explicitly return live provider results with answered/unavailable labels. Thus “retrieval never synthesizes anything” is too broad for the whole shipped system. See [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval), [RT-RTE-embedding-retrieval](runtime.md#rt-rte-embedding-retrieval), [RT-RTE-native-assistant](runtime.md#rt-rte-native-assistant) and [EPI-RTE-provider-question](#epi-rte-provider-question).

Correction cases, generalized behavioral Memory and edit feedback differ. The first preserves a scoped user-redirection contrast; the second prescribes future behavior; the third preserves rejected-versus-accepted curation examples for a late check by future Update work. Guidance capture alone retains unsettled evidence. Explicit inbox review adds a user approval criterion for meaning/scope and then connects approved changes to canonical guidance. That is a conditional procedural acceptance/integration route, not evidence it operated or that ordinary automatic Update requires human approval. See [EPI-OBJ-corrections](#epi-obj-corrections), [EPI-RTE-guidance-capture](#epi-rte-guidance-capture) and [EPI-RTE-guidance-review](#epi-rte-guidance-review).

Pruner withdraws active availability using unchanged meaning, active use and grace criteria, not a test that an assertion is false. Insight can propose patterns in a separate retained log; later Insight reads are wired, but this does not establish acceptance or active-Memory promotion. Sync, imported views, direct maintenance and the Pursuit editor have separate authority. No inspected universal withdrawal propagation or rollback guarantee covers every external consumer. See [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles), [RT-RTE-sync-admission](runtime.md#rt-rte-sync-admission), [RT-RTE-file-import](runtime.md#rt-rte-file-import), [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance) and [RT-RTE-pursuit-editor](runtime.md#rt-rte-pursuit-editor).

Extractive views mechanically reshape selected source text. Generative views request rewritten shareable text; their semantic preservation is indeterminate without actual inputs and outputs. Approval licenses distribution, and refresh preserves prior approval rather than requiring a new per-output human decision. This is operational authority, not evidence-consuming acceptance of every generated proposition. See [EPI-RTE-view-build](#epi-rte-view-build) and [EPI-RTE-view-approval](#epi-rte-view-approval).

Retained guidance can change later action through model interpretation, but actual activation and improved capacity are unobserved. No supplied trace establishes content-directed criticism iterating on a formulated explanation, successful reflection, autonomous theory building or exercised self-improvement. These conclusions remain independent: persistent trace-fed correction capacity is supported at the instruction/update boundary; factual warrant, learned benefit and causal self-change do not follow. Model-weight changes are not established in inspected callers; provider internals remain uninspected. See [RT-CMP-role-model](runtime.md#rt-cmp-role-model), [RT-BAP-role-policy](runtime.md#rt-bap-role-policy) and [RT-BAP-host-context](runtime.md#rt-bap-host-context). The coverage limits above prevent an unqualified system-wide negative.

## Shared records

### Operative objects

#### EPI-OBJ-memory
Label: Memory

Natural-language facts, preferences, interpretations, scoped rules and unresolved questions in Git-backed MEMORY.md, MEMORY_*.md and linked Markdown/skill assets. This is semantic state, distinct from runtime configuration, operation metadata and package policy in [RT-OBJ-runtime-config](runtime.md#rt-obj-runtime-config), [RT-OBJ-semantic-operation](runtime.md#rt-obj-semantic-operation) and [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions). No supplied operative-object record names this same retained semantic state. SRC-1: `rightmemory/reference/MEMORY_RULES.md`.

> A Memory item should express one reusable fact, preference, rule, decision, conclusion, or unresolved question at the smallest scope that remains independently meaningful.
> --- `rightmemory/reference/MEMORY_RULES.md`

#### EPI-OBJ-agent-corrections
Label: Agent Corrections

Natural-language scoped cases stored in the two fixed Git-backed correction Markdown collections. Distinct from the generic update route [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) and package instructions [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions): this record names its semantic products, not execution or policy. SRC-1: `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`.

> A stored Agent Correction is not the same thing as a user redirection in conversation. A redirection is evidence; Update or an explicit review workflow decides whether that evidence deserves a reusable entry.
> --- `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`

#### EPI-OBJ-corrections
Label: RightMemory Edit Feedback

Natural-language Candidate/Proposed edit/Accepted edit sections in optional root corrections.md, stored in the memory repository. Distinct from Agent Corrections and the supplied role-instructions object; Update reads this operational feedback after tentative planning. Its exact-evidence requirement supports lineage within the example, not generalized truth. SRC-1: `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md`.

> Keep evidence exact. Do not derive general behavior lessons inside this collection.
> --- `rightmemory/reference/RIGHTMEMORY_EDIT_CORRECTION_RULES.md`

#### EPI-OBJ-guidance-inbox
Label: Pending Agent Guidance

Natural-language evidence bodies with symbolic entry/session/time fields in Git-backed AGENT_GUIDANCE_INBOX.md. No counterpart object in supplied runtime: [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) processes a different submission route; the inbox explicitly uses user-reviewed direct curation. SRC-1: `rightmemory/guidance.py`.

> GUIDANCE_INBOX_PATH = "AGENT_GUIDANCE_INBOX.md"
> --- `rightmemory/guidance.py`

#### EPI-OBJ-shared-view
Label: Shared-view artifacts

Container whose operative parts are split below by consumption: dist Markdown is natural-language provider content; retriever.md is natural-language provider policy; recipe.toml/question.toml contain symbolic selection, approval and endpoint metadata. Stored under shared_views/<view-id>/ and imported runtime directories. This names provider-produced artifacts; [RT-RTE-file-import](runtime.md#rt-rte-file-import) instead names acquisition of file packages. SRC-1: `rightmemory/prompts/shared-view-builder.md`.

> Build only provider-owned shared-view artifacts under `shared_views/<view-id>/`.
> --- `rightmemory/prompts/shared-view-builder.md`

#### EPI-OBJ-view-document
Label: Shared Memory document

Part of: [EPI-OBJ-shared-view](#epi-obj-shared-view)

Natural-language dist/MEMORY.md and extractively copied backing documents, stored in provider distribution files and consumer imports. The part is source content, not recipe permission or question instructions. Extractive selection preserves surviving text; generative compiler accepts a complete document subject to structure checks. Compared with [RT-RTE-file-import](runtime.md#rt-rte-file-import), this object names what is transported, not its acquisition route. SRC-1: `rightmemory/shared_view_files.py`.

> _write_text(dist / "MEMORY.md", memory_document.strip() + "\n")
> --- `rightmemory/shared_view_files.py`

#### EPI-OBJ-retriever-policy
Label: Provider retriever instructions

Part of: [EPI-OBJ-shared-view](#epi-obj-shared-view)

Natural-language retriever.md in a provider view directory. The builder supplies policy text; answer_question_view concatenates it with the current question before invoking the configured provider role. This policy has behavioral authority at that model invocation, separate from consumer-facing dist content and from package role policy [RT-OBJ-role-instructions](runtime.md#rt-obj-role-instructions). No meaning-equivalence validator for generated instructions is established by the inspected wrapper. SRC-1: `rightmemory/shared_view_questions.py`.

> retriever.read_text(encoding="utf-8").strip(),
> --- `rightmemory/shared_view_questions.py`

#### EPI-OBJ-view-permission
Label: Shared-view approval metadata

Part of: [EPI-OBJ-shared-view](#epi-obj-shared-view)

Symbolic approved fields in recipe.toml and question.toml, stored in provider files. File approval validates then writes a flag; question answering refuses an unapproved config. Their scope is distribution or execution permission, not semantic acceptance. The narrower file-view change is [EPI-RTE-view-approval](#epi-rte-view-approval); question control is [EPI-RTE-provider-question](#epi-rte-provider-question). Distinct from [RT-OBJ-runtime-config](runtime.md#rt-obj-runtime-config): view-level content permission, not executor/backend settings. SRC-1: `rightmemory/shared_view_files.py`, `rightmemory/shared_view_questions.py`.

> if not config.approved:
>     return _format_unavailable(clean_view_id, "question view is not approved")
> --- `rightmemory/shared_view_questions.py`

#### EPI-OBJ-question-answer
Label: Shared question answer

Natural-language provider result with symbolic status interpreted by wrappers, transient in the returned string/HTTP payload. Distinct from [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval): a separately exposed live provider question path, not ordinary terminal-selection retrieval. SRC-1: `rightmemory/shared_view_questions.py`.

> return f"Shared question: {clean_view_id}\nStatus: answered\nAnswer:\n{answer.strip()}\n"
> --- `rightmemory/shared_view_questions.py`

#### EPI-OBJ-insight-logs
Label: Insight logs

Natural-language reflections in timestamped Git-backed insight_logs/*.md. Distinct product of the Insight part of [RT-RTE-maintenance-cycles](runtime.md#rt-rte-maintenance-cycles), not a replacement for that execution container. Prior logs are explicitly sources for later cycles; no automatic Memory promotion found in inspected prompt. SRC-1: `rightmemory/prompts/insight.md`.

> Do not append to existing logs.
> --- `rightmemory/prompts/insight.md`


### Routes

#### EPI-RTE-guidance-capture
Label: Guidance evidence capture

Caller/session evidence → submit_guidance → parsed/rendered inbox entry → committed temporary worktree → base-fenced fast-forward. Owner is capture code, not Update. Nonempty text and parse validity decide retention; caller supplies content, and code vetoes malformed evidence. No expected-answer oracle, per-entry human approval or semantic admission is imposed. This extends coverage beyond [RT-RTE-isolated-update](runtime.md#rt-rte-isolated-update) with a distinct durable pending object. Operating mode is open capture, not an improvement experiment. SRC-1: `rightmemory/guidance.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New pending entry identity; MCP caller ordinarily receives only warning state.
- Later read-back: Explicit review host reads inbox and proposes formal guidance; pending evidence is not automatically promoted.
- Delegated visibility: CLI/MCP capture caller and review host; inspected tools do not grant this inbox to ordinary RightMemory role reads.
- Selection predicate: Nonempty evidence/session and valid inbox structure; no semantic truth test.
- Invalidation or expiry: Explicit review may remove approved/rejected entries; deferred entries stay; HEAD conflict aborts fast-forward.
- Activation or effect: Durably retains unresolved evidence; later behavioral change requires approved curation and retrieval.
- Evidence limits: No real captured entry or review run supplied.

> _git(root, "merge", "--ff-only", _git(worktree, "rev-parse", "HEAD"))
> --- `rightmemory/guidance.py`

#### EPI-RTE-guidance-review
Label: User-reviewed guidance curation

Pending inbox → host proposal naming evidence, intended meaning/scope/destination → explicit user approval → host worktree edits and inbox removals → instructed validation and exact landing. Owner is host/human under the skill. Human can veto or defer individual proposals; host drafts meaning, not exact final wording before approval. Criterion is approved scoped guidance under module admission rules, intended for future behavior or reusable cases; approval does not independently corroborate factual claims. Operating mode is explicit user-reviewed curation; no answer oracle. Recovery: stop on dirty/changed active base; leave deferred entries; no universal rollback after protocol violation. Compared with [RT-RTE-manual-maintenance](runtime.md#rt-rte-manual-maintenance), this is a distinct inbox-specific proposal/approval/removal workflow, not general direct maintenance. SRC-1: `skills/review-agent-guidance-inbox/SKILL.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Applied proposals, remaining inbox, validation/commit report or no commit.
- Later read-back: Canonical guidance becomes available to later retrieval; inbox removal disposes reviewed evidence.
- Delegated visibility: Host/user see proposal evidence and scope; later agents receive admitted guidance rather than necessarily all original evidence.
- Selection predicate: Explicitly approved proposals only; reject/already-covered/defer dispositions are available.
- Invalidation or expiry: Deferred/unreviewed entries unchanged; module rules allow future narrowing/removal; active-base change blocks landing.
- Activation or effect: Approval can authorize semantic changes; skill affords lifecycle integration after that approval, with no observed execution.
- Evidence limits: Natural-language procedure, not mandatory program gate; no factual oracle or benefit trace.

> Do not present exact final wording, graph ids, or a patch before approval. Apply only explicitly approved proposals.
> --- `skills/review-agent-guidance-inbox/SKILL.md`

#### EPI-RTE-view-build
Label: Shared-view build and refresh

Caller intent/current active memory → shared-view-builder model → extractive selection or generative complete Memory document → compiler artifacts → applicable schema/dist checks. Owner is builder wrapper and role model. Model proposes mode/selection/refined intent, tools can fail and request correction; no per-content human acceptance in build itself. Operating mode is open sharing request or due/forced refresh. No expected-answer oracle checks meaning. File build/refresh backs up view directory and restores it on failure; refresh records time/active commit, preserves old approval and can publish when configured. Distinct from [RT-RTE-file-import](runtime.md#rt-rte-file-import): this is provider construction, not consumer acquisition. The provider model follows the fixity limits of [RT-CMP-role-model](runtime.md#rt-cmp-role-model). SRC-1: `rightmemory/shared_view_builder.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Builder summary or failure; refresh can report not due.
- Later read-back: Recipe/dist/retriever policy persist for later publication, import or question invocation.
- Delegated visibility: Builder sees provider active memory; consumers get selected/rewritten distribution, not all private source context.
- Selection predicate: Model's shareability/clarity judgment; extractive recipes select/exclude IDs/files; generative compiler checks schema, not semantic equivalence.
- Invalidation or expiry: Refresh due requires changed active commit and configured elapsed interval unless forced; failed file build/refresh restores view directory.
- Activation or effect: Prepares context and question policy; later publication/import supplies them to consumers; no exercised benefit supplied.
- Evidence limits: No actual generative output pair; no proof of privacy-preserving semantics or factual completeness; all repair/publication branches not exhaustively audited. Generated question instructions become [EPI-OBJ-retriever-policy](#epi-obj-retriever-policy), consumed as provider policy, whereas dist text becomes [EPI-OBJ-view-document](#epi-obj-view-document).

> approved=old_recipe.approved,
> --- `rightmemory/shared_view_builder.py`

#### EPI-RTE-view-approval
Label: File-view approval permission

Caller → validate recipe → render or validate generated output → validate dist → persist approved flag. Code owns this API's gate. Caller requests approval; code can reject structure. Caller identity alone does not establish human review or an evidence-consuming per-claim acceptance decision. No answer oracle. Operating mode is explicit view permission, distinct from [RT-RTE-file-import](runtime.md#rt-rte-file-import) and [EPI-RTE-view-build](#epi-rte-view-build). Publication consumes approval, including configured refresh retaining it; approval is not a truth evaluation. SRC-1: `rightmemory/shared_view_files.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Approved-view status or validation exception.
- Later read-back: Persisted recipe flag licenses later publish paths; dist becomes external context after publication/import.
- Delegated visibility: Publisher consumes flag; later readers consume distribution, not this permission as factual evidence.
- Selection predicate: Valid recipe/selection and generated-or-extractive dist checks before approved=True.
- Invalidation or expiry: Recipe revisions can alter permission; automatic refresh deliberately preserves old approval; universal remote revocation is uninspected.
- Activation or effect: Permission changes publication eligibility, not confidence in source propositions.
- Evidence limits: No supplied reviewer identity, inspected per-proposition evidence decision or external consumer withdrawal trace.

> _write_text(_view_dir(root, recipe.view_id) / "recipe.toml", _render_recipe_toml(_replace_recipe(recipe, approved=True)))
> --- `rightmemory/shared_view_files.py`

#### EPI-RTE-provider-question
Label: Live provider question response

Consumer ask_question_view → configured HTTP target → provider answer_question_view → approved view/retriever prompt plus question → configured runtime role → wrapped answer or unavailable. Provider code owns availability checks and caller code parses/relabels results. Model/provider determines content under generated retriever policy; no answer oracle, independent semantic rejection or accepted-claim record is added here. Operating mode is open question answering. Token verification checks authorization and approval, not truth. Timeouts/errors withhold an answer status; successful return permits consumer reliance without another truth check. Compared with [RT-RTE-agent-retrieval](runtime.md#rt-rte-agent-retrieval) and [RT-RTE-file-import](runtime.md#rt-rte-file-import), this is a distinct live question endpoint. Configured runtime model fixity is see [RT-CMP-role-model](runtime.md#rt-cmp-role-model). SRC-1: `rightmemory/shared_view_questions.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Formatted answered/unavailable response; provider error/start/answer timeout becomes unavailable.
- Later read-back: uninspected — wrapper does not itself persist the answer for future retrieval; configured runtime role/session may retain its own history.
- Delegated visibility: Provider sees retriever policy and question; consumer receives wrapped response, not full internal work.
- Selection predicate: Configured question connection, approved provider view, retriever file, authentication where token verifier is used, successful provider completion.
- Invalidation or expiry: Request timing bounds availability; token verifier rejects unapproved configuration; no general recall/withdrawal of already returned content is shown.
- Activation or effect: Answered status changes availability and delivers provider content, not factual endorsement.
- Evidence limits: No deployed provider prompt/output or inspected provider trace; internal transformation may select, rewrite or infer and is indeterminate.

> if not config.approved:
>         return _format_unavailable(clean_view_id, "question view is not approved")
> --- `rightmemory/shared_view_questions.py`

Implementation deduction for [EPI-RTE-view-build](#epi-rte-view-build): in the inspected extractive renderer, suppose a selected full block has node line `- [x] latency is 20 ms` and its sibling is excluded. Given a parsed node and full inclusion, `_render_block` returns that exact line; the excluded sibling returns the empty string. The parent joins included pieces; `render` strips managed examples and adds a terminal newline before dist validation/promotion. The surviving proposition is unchanged, but nothing checks whether 20 ms is true or whether omitted surrounding material was necessary warrant. This is a code-based hypothetical trace, not target execution or an observed stored assertion. SRC-1: `rightmemory/shared_view_files.py`.

> if block.kind == "node":
>     return block.line if full or key in self.exact_nodes else ""
> --- `rightmemory/shared_view_files.py`

> if self._is_excluded(key):
>     return ""
> --- `rightmemory/shared_view_files.py`

> text = _strip_managed_examples(text).strip()
> --- `rightmemory/shared_view_files.py`

### Claims

#### EPI-CLM-memory-admission
Label: Durable context with scoped evidence

Memory rules claim a future-use admission policy, not storage of everything. Module policy treats useful uncertainty explicitly and forbids converting speculation into fact. Update asks revalidation of possibly stale claims. This is a design claim about intended handling, distinct from the publication receipt claim [RT-CLM-native-publication](runtime.md#rt-clm-native-publication). SRC-1: `rightmemory/reference/MEMORY_RULES.md`, `rightmemory/prompts/update.md`.

> Useful unsettled context may be stored as `Uncertain:` when the uncertainty itself affects future work. Do not convert speculation into declarative fact.
> --- `rightmemory/reference/MEMORY_RULES.md`

> Revalidate claims that may have become stale instead of copying candidates as fact.
> --- `rightmemory/prompts/update.md`

#### EPI-CLM-correction-cases
Label: Reusable user-redirection cases

Agent Corrections claims to preserve scoped contrast that generalized rules would weaken. Its six admission conditions require identifiable attempt, clear redirection/outcome, recurrence or cost, distinct value and clear applicability. A different result alone is explicitly insufficient. Distinct from the supplied publication claim: this is a semantic content/admission claim. SRC-1: `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`.

> Agent Corrections is RightMemory's bounded library of reusable cases in which a user redirected prior agent work. It preserves concrete contrast that would be weakened or lost if reduced to a generalized preference or rule.
> --- `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`

> A different result alone is insufficient.
> --- `rightmemory/reference/AGENT_CORRECTION_MEMORY_RULES.md`

#### EPI-CLM-retrieval-coverage
Label: Reported labelled retrieval coverage

The repository reports 28/28 positive required-ID cases retained across three integrated-backend passes, under the documented small frozen benchmark and environment. This is attributed reported operation, not observed-run evidence in this analysis. Unlike [RT-CLM-native-publication](runtime.md#rt-clm-native-publication), the claim concerns retrieval measurements, not publication. It supplies no independent end-to-end answer judgment or causal component attribution. SRC-1: `experiments/README.md`.

> This is still a small, agent-labelled coverage test, not independent answer-quality evaluation.
> --- `experiments/README.md`

> The four no-answer queries also receive ten candidates; deciding their usefulness belongs to the caller.
> --- `experiments/README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; downstream host interpretation and package role policy are see [RT-BAP-host-context](runtime.md#rt-bap-host-context) and [RT-BAP-role-policy](runtime.md#rt-bap-role-policy). New-route-specific channels, force and horizons are stated in their declarations and ledger rows.
