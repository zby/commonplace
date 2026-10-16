---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Link epistemic routes: source acquisition, memory review, wiki checks and downstream reliance at the frozen revision."
run-id: AAS-2026-10-14-link-595f6f9cba36-01
reviewed-boundary: cc92f3632121b04063b24eaaf3a8c5429eaf2b57
---

# Link epistemic report

## Source-and-claim boundary

The question is whether Link's retained context is acquired, transformed, checked and licensed for later reliance. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity and layers are see [Source register](boundary.md#source-register), SRC-1. This is source inspection at the frozen commit, not target execution. The supplied runtime is a provisional route map. Direct inspection below adds checks, dispositions and transformations; it does not supersede the valid runtime containers.

External human judgments, host model behavior, provider weights and the separately reported QA benchmark workspace are not supplied. Missing judgments prevent establishing evidence-consuming acceptance of particular claims. Missing host traces prevent establishing actual reliance, compliance or changed answers. Unpinned and inaccessible provider state prevents independently assessing the truth content, if any, in distributed-parametric components. Missing QA artifacts prevent independently licensing reported answer-quality results or causal attribution. Available source files left unread are inspection limits, not access gaps.

| Entry point or operation | Source path, SRC-1 | Coverage and evidence basis | Limit and prevented conclusion |
|---|---|---|---|
| CLI dispatch | `link.py` | Direct read of `main`, review-all and selected lifecycle handlers; supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | Parser internals and demo/proof bodies not audited; no all-command approval invariant |
| MCP slim/full registration and review/admin dispatch | `mcp_package/link_mcp/server.py` | Direct registration/dispatch search and recall/review/admin body reads; supplied [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) and [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery) | Full tool bodies not all reread; host tool compliance unobserved |
| HTTP and LinkBar callers | `serve.py`; `apps/LinkBar/Sources/LinkBar/LinkStore.swift` | Supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install) | Caller wiring assessed from runtime, not an independent UI/security audit |
| Session hooks, handoffs and capture cleanup | `link.py`; `mcp_package/link_core/capture.py`; `mcp_package/link_core/handoff.py` | Supplied [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery); direct proposal normalization read, [EPI-RTE-proposal-normalization](#epi-rte-proposal-normalization) | Capture dedup/redaction bodies not independently traced here; no universal lineage-preservation conclusion |
| Write, review, update, archive and restore | `mcp_package/link_core/memory.py` | Direct reads of shared implementations; [EPI-RTE-memory-check](#epi-rte-memory-check), [EPI-RTE-memory-disposition](#epi-rte-memory-disposition), [EPI-RTE-review-marking](#epi-rte-review-marking), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | Forget and visibility details supplied only; no all-path quarantine |
| Structured ingest and validation | `mcp_package/link_core/structured_ingest.py`; `mcp_package/link_core/validation.py` | Direct complete validator and renderer/apply reads; [EPI-RTE-export-rendering](#epi-rte-export-rendering), [EPI-RTE-wiki-validation](#epi-rte-wiki-validation), [EPI-RTE-staged-disposition](#epi-rte-staged-disposition) | Input loader and plan ownership details supplied by [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest); export source truth unknown |
| Arbitrary-source ingest, query filing, research and lint | `LINK.md` | Direct operation instructions; supplied [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) | External authored candidates and critic decisions unavailable; instruction is not compliance |
| Project seed, Obsidian/imported instruction sources | `mcp_package/link_core/project_seed.py`; `mcp_package/link_core/obsidian.py`; `mcp_package/link_core/importers.py` | Supplied [RT-RTE-project-seed](runtime.md#rt-rte-project-seed), [RT-RTE-source-import](runtime.md#rt-rte-source-import), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | No independent semantic fidelity audit of seed/import |
| Generic wiki search/context, including archived memories | `mcp_package/link_core/wiki.py`; `mcp_package/link_core/search.py`; `mcp_package/link_core/query.py` | Correction-round direct reads of enumeration, complete search selector, topic-context assembly and combined-query construction; supplied [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read) and [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) | Generic page delivery does not apply focused-memory lifecycle/project gates or carry memory-specific review/lifecycle warnings; ranking determines actual delivery, which is unobserved |
| Query compaction, ranking, warnings and abstention | `mcp_package/link_core/query.py`; `mcp_package/link_core/memory.py`; `mcp_package/link_mcp/server.py` | Direct body reads; [EPI-RTE-recall-assessment](#epi-rte-recall-assessment); supplied [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) | Only focused recall emits the inspected first-class abstention result; combined query emits separate guidance |
| Stale repository references | `mcp_package/link_core/staleness.py`; `mcp_package/link_core/query.py` | Direct checker and consumer reads; [EPI-RTE-path-staleness](#epi-rte-path-staleness) | Bounded path lookup is not general semantic drift detection |
| Consolidate, digest and retrieval history | `mcp_package/link_core/consolidate.py`; `mcp_package/link_core/usage.py` | Direct plan and usage bodies; [EPI-RTE-consolidation-plan](#epi-rte-consolidation-plan) | Similarity helper/digest bodies not fully inspected; experimental usage boost is not automatic production learning |
| Sync, team import and recovery | `mcp_package/link_core/sync.py`; `mcp_package/link_core/backup.py`; `mcp_package/link_core/operations.py` | Supplied [RT-RTE-workspace-sync](runtime.md#rt-rte-workspace-sync), [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery); direct sync claim search | Byte/history restoration is not truth endorsement; outgoing secret checks do not judge incoming truth |
| Offline recall evaluator | `scripts/eval_recall_quality.py` | Supplied rank scoring plus direct `main` read; [RT-RTE-recall-evaluation](runtime.md#rt-rte-recall-evaluation) | Regression exit status can block an invoking job, not automatically alter production |
| Other evaluators, tests, doctor, benchmark, share/snapshot/export | `scripts/`; `tests/`; `mcp_package/link_core/doctor.py`; `mcp_package/link_core/share.py`; `link.py` | Entry-point/search coverage only, or runtime summaries | Hygiene, poisoning, salience, staleness, token and LoCoMo evaluator bodies, complete health/benchmark and export consumers unassessed; prevents system-complete negative about evaluators and operational adaptation |
| Runtime setup and model provisioning | `mcp_package/link_core/semantic.py`; `integrations/` | Supplied [RT-RTE-runtime-install](runtime.md#rt-rte-runtime-install), [RT-CMP-model2vec](runtime.md#rt-cmp-model2vec), [RT-CMP-fastembed](runtime.md#rt-cmp-fastembed), [RT-CMP-reranker](runtime.md#rt-cmp-reranker) | Exact provider internals/weights and installed configuration unavailable |

Consequential claims are [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory), [EPI-CLM-source-backed](#epi-clm-source-backed), [EPI-CLM-confidence-tags](#epi-clm-confidence-tags) and [EPI-CLM-review-accuracy](#epi-clm-review-accuracy). These concern distinct approval, lineage, inference and review licenses; none is an observed success guarantee.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-page](#epi-obj-memory-page) | User/project facts and preferences; procedures include both claims and directives | see record | SRC-1, `mcp_package/link_core/memory.py` | Caller source label does not authenticate origin or approval |
| [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | Imported documentation and agent-authored claims, comparisons, answers and hypotheses | see record | SRC-1, `LINK.md` | Empty scaffold supplies no accepted claim instance |
| [EPI-OBJ-capture-proposal](#epi-obj-capture-proposal) | Proposed user/project claims extracted from notes; original text may mix speakers | see record | SRC-1, `mcp_package/link_core/memory.py` | User-only hook selection differs from manual/import inputs |
| [RT-OBJ-link-instructions](runtime.md#rt-obj-link-instructions) | Mostly policy; doctrine includes claims about grounding and review | see record | SRC-1, `LINK.md` | Static shipped method, not evaluated use-derived learning |
| [RT-OBJ-operation-journal](runtime.md#rt-obj-operation-journal) | Symbolic propositions about write/recovery state, not factual wiki knowledge | see record | SRC-1, `mcp_package/link_core/operations.py` | Restoring bytes preserves an earlier state, not its truth |
| [RT-CMP-model2vec](runtime.md#rt-cmp-model2vec), [RT-CMP-fastembed](runtime.md#rt-cmp-fastembed), [RT-CMP-reranker](runtime.md#rt-cmp-reranker) | not determinable: numerical representation/scores do not individuate their encoded truth-apt content | see records | SRC-1, `mcp_package/link_core/semantic.py` | Separate unpinned models; no inspected parameter-update step; external internals opaque |

Handoff text, raw imports, manifests and numerical indexes remain contextual parts of their supplied route records, not new inferred knowledge objects. A handoff gives task priority and possibly claims about past work; no particular handoff instance is supplied. Retrieval events report selected identities, not evidence that an answer used or benefited from them.

## Authority-route ledger

The ledger separates checking from its consumer and retention from integration. `see` delegates only fields owned by the cited records; the content/update assessments and architectural statuses here are this report's judgments. Implementation status establishes capacity, never activation. No accepted ampliative claim instance is evidenced.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-source-import](runtime.md#rt-rte-source-import) | content transformation | implemented | Raw source; see record | truth-apt transformation: acquisition/import | External Markdown to raw copies | see record | Explicit import | see record | Copy permitted by checks | Original attribution can survive; source truth unknown | Makes raw available to later ingest | Raw reader; filesystem; permissive; later ingest | SRC-1, `mcp_package/link_core/obsidian.py` | none | none | Import does not itself create recalled knowledge; source warrant unknown. |
| [RT-RTE-project-seed](runtime.md#rt-rte-project-seed) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: acquisition/import | Project files/history to source page | see record | Explicit seed; steering permits bootstrap | see record | Bounded copying/rendering | Source lineage available; no truth oracle | Generated page eligible for query | Query/agent; wiki excerpt; advisory; later calls | SRC-1, `mcp_package/link_core/project_seed.py` | none | none | Exact semantic preservation unassessed; source warrant unknown. |
| [EPI-RTE-proposal-normalization](#epi-rte-proposal-normalization) | content transformation | implemented | [EPI-OBJ-capture-proposal](#epi-obj-capture-proposal) | truth-apt transformation: indeterminate | First-person or decision text to candidate claim | see record | Proposal mining before capture/acceptance | see record | Candidate only | No general semantic-preservation license | Makes rewritten proposal available for caller selection | Capture/review caller; candidate text; advisory; until accepted/dismissed | SRC-1, `mcp_package/link_core/memory.py` | none | none | Speaker and temporal qualifier can change; warranted reshaping only under extra assumptions. |
| [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) | retention | implemented | [EPI-OBJ-capture-proposal](#epi-obj-capture-proposal) | no content change | Retain proposal/raw review context | see record | Session end or manual capture | see record | Proposal-only persistence | No approval from capture | Inbox and review supply enabled | Review caller; raw/inbox; advisory; later sessions | SRC-1, `link.py` | none | none | Automatic user-only extraction does not cover manual/import origin; downstream acceptance separate. |
| [EPI-RTE-memory-check](#epi-rte-memory-check) | check/evidence production | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | no content change | Secret-shaped, duplicate and conflicting candidates | see record | Before write; conflicts before update | see record | Computes heuristic findings | Only detected similarity/revision/secret patterns | Supplies inputs to separate disposition | Writer; candidate lists; enforcing only at disposition; current mutation | SRC-1, `mcp_package/link_core/memory.py` | [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory) | none | No general contradiction or truth proof; optional model state opaque; update is not the new-write secret gate. |
| [EPI-RTE-memory-disposition](#epi-rte-memory-disposition) | disposition/acceptance | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | no content change | Whether shared new-memory write proceeds | see record | After candidate checks | see record | Overrideable rejection or permissive write | Operational admission, not evidence-consuming truth acceptance | Refuses or admits pending active page | Writer; return/override arguments; enforcing; current call | SRC-1, `mcp_package/link_core/memory.py` | [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory) | Approval contract is not authenticated | Direct files and sync bypass this gate. |
| [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | retention | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | truth-apt transformation: acquisition/import | Caller claim to durable memory | see record | After write admission | see record | Durable pending active page | Acquires supplied claim; source warrant unknown | Eligible for later recall before review | Recall; Markdown; permissive; later sessions | SRC-1, `mcp_package/link_core/memory.py` | [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory) | none | Retention/use before acceptance is not lifecycle integration. |
| [EPI-RTE-memory-update](#epi-rte-memory-update) | content transformation | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | truth-apt transformation: acquisition/import | Caller detail appended to retained memory | see record | Explicit update after conflict gate | see record | Journaled append and review reset | Acquires supplied detail with source label; source warrant unknown | Changes future claim/body context and makes review pending | Recall/agent; body and metadata; permissive/advisory; later calls | SRC-1, `mcp_package/link_core/memory.py` | [EPI-CLM-review-accuracy](#epi-clm-review-accuracy) | Update does not inherit new-write secret screen | Append does not resolve every old/new contradiction or prove accuracy. |
| [EPI-RTE-review-marking](#epi-rte-review-marking) | disposition/acceptance | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | non-truth-apt policy/content update: review metadata and due date | Caller assertion of accuracy to reviewed marker | see record | Explicit review; optional bulk confirm | see record | Sets reviewed, re-arms window | Protocol criterion: human confirms accuracy for future context; evidence not checked by code | Review metadata/rank/warnings change | Recall and agent; review fields; ranking/advisory; typed review interval | SRC-1, `mcp_package/link_core/memory.py` | [EPI-CLM-review-accuracy](#epi-clm-review-accuracy) | Marker is not proof of acceptance | No authenticated judgment trace or mandatory evidence/note; no claim-instance acceptance established. |
| [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | non-truth-apt policy/content update: archive/restore status | Focused-memory default eligibility, including combined query's memory branch | see record | Caller archive/restore | see record | Focused active filter enforces status | Withdrawal from focused-memory default selection only, not refutation or all-query withdrawal | Archive suppresses focused active selection; restore re-enables; generic wiki delivery remains possible | Focused-memory selector; lifecycle fields; enforcing for that branch; until changed | SRC-1, `mcp_package/link_core/memory.py` | none | Generic wiki delivery bypasses focused lifecycle filtering | Ordinary combined query can still deliver the retained archived page through [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read), without memory-specific review/lifecycle warnings. include_archived/as_of, file reads and prior host text also remain possible. |
| [EPI-RTE-export-rendering](#epi-rte-export-rendering) | content transformation | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: non-ampliative reshaping | Export page bodies to grouped source pages | see record | Structured plan/render | see record | Deterministic rendering | Body lineage retained with explicit byte modifications; source truth unknown | Creates candidate outputs for staging | Adapter; output strings; permissive; planned apply | SRC-1, `mcp_package/link_core/structured_ingest.py` | [EPI-CLM-source-backed](#epi-clm-source-backed) | Verbatim has documented escape exception | Generated counts derive within supplied export domain, not upstream factual validation; high confidence is preset. |
| [EPI-RTE-wiki-validation](#epi-rte-wiki-validation) | check/evidence production | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Wiki structure, links, dates, secret patterns | see record | Staged pre-copy or explicit/post-write check | see record | Produces passed/findings | Shape/link consistency and detected secret patterns only | Inputs to stage rejection or operator completion decision | Adapter/agent; validator result; enforcing/advisory respectively; current apply/completion | SRC-1, `mcp_package/link_core/validation.py` | [EPI-CLM-source-backed](#epi-clm-source-backed) | none | Cannot establish faithful grounding or source truth; source links need not entail authored prose. |
| [EPI-RTE-staged-disposition](#epi-rte-staged-disposition) | disposition/acceptance | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Apply staged structured output | see record | After conflicts and staged validation | see record | Code veto on failure, copy on pass | Acceptance of structural/ownership admissibility only; not truth acceptance | Blocks or permits live replacement | Adapter; validation/plan; enforcing; current apply | SRC-1, `mcp_package/link_core/structured_ingest.py` | none | none | Caught copy failure rollback is not crash/concurrency proof. |
| [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest) | retention | implemented | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Generated wiki plus provenance manifest | see record | Successful structured apply | see record | Filesystem persistence | Hash lineage, not endorsement | Later query and later managed update available | Query/adapter; Markdown/hash manifest; permissive; later calls | SRC-1, `mcp_package/link_core/structured_ingest.py` | none | none | No epistemic lifecycle integration established merely by rebuilding links/index. |
| [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) | content transformation | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Arbitrary source/answer to claims and hypotheses | see record | Agent follows ingest/query/research instructions | see record | Natural-language request | Explicit source statements, reasonable inferences and speculation distinguished by authored tags | Requests source-linked pages, contradiction notes and human-selected repairs | External agent; LINK.md; advisory; ingest/lint/future queries | SRC-1, `LINK.md` | [EPI-CLM-confidence-tags](#epi-clm-confidence-tags) | none | Actual transformation may acquire, reshape, derive or conjecture; no produced candidate or checked entailment/non-entailment trace. |
| [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) | lifecycle integration | doctrine only | [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Accepted content connected to sources and existing pages | see record | After human confirms memory or selects filing/fixes; arbitrary-source ingest has workflow authority | see record | Requested links, Open Questions, organization changes | Integration request; no accepted claim instance or reliable compliance established | Asks agent to organize reusable content | Agent; LINK.md and wiki; advisory; later queries | SRC-1, `LINK.md` | none | none | Source linking during ordinary ingest may precede acceptance; not all graph rebuilding is lifecycle integration. |
| [EPI-RTE-recall-assessment](#epi-rte-recall-assessment) | check/evidence production | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | no content change | Query-memory match strength, not claim truth | see record | Focused recall after selection | see record | Returns confidence/abstention | Lexical coverage or capped semantic similarity only | Supplies cautious-use advice | MCP/agent; JSON confidence/abstention; advisory; answer turn | SRC-1, `mcp_package/link_core/memory.py` | none | none | Strong match is compatible with false claim; weak result remains returned. |
| [EPI-RTE-context-compaction](#epi-rte-context-compaction) | content transformation | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page); [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: indeterminate | Selected body to bounded packet excerpt | see record | Packet construction after selection | see record | Fixed character clipping | Provenance remains, full semantic scope need not remain | Limits initial host context; follow-up can return fuller pages | Agent; compact text/ellipsis; advisory; query turn | SRC-1, `mcp_package/link_core/query.py` | [EPI-CLM-source-backed](#epi-clm-source-backed) | Excerpt is not full source warrant | Qualifiers outside excerpt require source reload. |
| [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page); [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | no content change | Select retained context; compaction assessed separately | see record | Recall request | see record | Ranking, filters and budgets | Selected excerpts/provenance, not new warrant | Chooses what reaches initial host context through separately gated memory and ungated generic wiki branches | Agent; packets/capsules; ranking/advisory; present and later calls | SRC-1, `mcp_package/link_core/query.py` | [EPI-CLM-source-backed](#epi-clm-source-backed) | Archive is not an all-packet withdrawal gate | Generic delivery of retained archived/expired/project-scoped memory pages is see [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read); page compaction omits memory-specific review/lifecycle warnings. Clipping can omit qualifiers; fuller-source follow-up remains. No answer oracle. |
| [RT-RTE-session-delivery](runtime.md#rt-rte-session-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page); handoff text | no content change | Unsolicited startup/first-response supply | see record | Hook or first suitable MCP response | see record | Delivery plus priority instruction | No epistemic acceptance from freshness or delivery | Requests resume/verify and supplies remembered context | External agent; hook/stdout/tool JSON; advisory; next session | SRC-1, `link.py` | none | none | Process flag is not proof of session identity; receiving behavior unobserved. |
| [EPI-RTE-path-staleness](#epi-rte-path-staleness) | check/evidence production | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page) | no content change | Missing formerly tracked path references | see record | Combined query, when repository available | see record | Findings carried with verify guidance | Limited missing/renamed-path evidence only | Requests review before relying on affected memory | Agent; stale_paths/guidance; advisory; query turn | SRC-1, `mcp_package/link_core/staleness.py` | none | none | Path existence is not claim correctness; no automatic archive or content replacement. |
| [EPI-RTE-consolidation-plan](#epi-rte-consolidation-plan) | check/evidence production | implemented | [EPI-OBJ-capture-proposal](#epi-obj-capture-proposal); [EPI-OBJ-memory-page](#epi-obj-memory-page) | truth-apt transformation: indeterminate | Backlog counts, duplicate/theme/merge proposals | see record | Explicit consolidate or backlog nudge | see record | Read-only candidate action plan | Counts under supplied payload; similarity groups not proven equivalence | Offers follow-up mutation commands, no automatic merge | Human/agent; plan; advisory; subsequent explicit actions | SRC-1, `mcp_package/link_core/consolidate.py` | none | none | Grouping internals not fully audited; merge correctness remains a human/content-review question. |
| [RT-RTE-workspace-sync](runtime.md#rt-rte-workspace-sync) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-page](#epi-obj-memory-page); [EPI-OBJ-wiki-page](#epi-obj-wiki-page) | truth-apt transformation: acquisition/import | Incoming/merged workspace content | see record | Explicit sync/team sync | see record | File/Git reconciliation | Lineage may survive; incoming truth/approval unknown | Imports content into local retrieval independently of memory writer | Recall; merged/imported files; permissive; later calls | SRC-1, `mcp_package/link_core/sync.py` | none | none | Outgoing secret gate does not establish incoming endorsement; conflict sibling keeps both versions. |
| [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery) | lineage/freshness/recovery | implemented | [RT-OBJ-operation-journal](runtime.md#rt-obj-operation-journal) | no content change | Restore snapshot/archive state | see record | Mutation failure or confirmed recovery | see record | Restore bytes; report integrity/errors | State lineage only | Restored context can replace newer context for later recall | Recovery/recall; snapshots/files; enforcing at replacement; later calls | SRC-1, `mcp_package/link_core/operations.py` | none | none | Does not recheck truth or automatically withdraw already supplied host text. |
| [RT-RTE-recall-evaluation](runtime.md#rt-rte-recall-evaluation) | check/evidence production | implemented | Authored target identities | no content change | Top-five retrieval rank | see record | Offline maintainer invocation | see record | Metrics and regression exit status | Retrieval rank on authored/variant suite, not answer truth | Nonzero exit on compared metric regression; no automatic production update | Invoker; report/exit code; enforcing for process, downstream uninspected; invocation | SRC-1, `scripts/eval_recall_quality.py` | none | none | QA reported results are not this evaluator; no run or component-causal evidence supplied. |


## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory) | see record | SRC-1, `LINK.md`, doctrine/design | see record | [EPI-RTE-memory-check](#epi-rte-memory-check), [EPI-RTE-memory-disposition](#epi-rte-memory-disposition), [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | None supplied | No human-approval credential; caller overrides and sync/file alternatives | Approval is a shipped protocol with heuristic admission, not authenticated all-path approval | Pending active memories can reach recall |
| [EPI-CLM-source-backed](#epi-clm-source-backed) | see record | SRC-1, `mcp_package/link_core/query.py`, doctrine/design | see record | [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), [EPI-RTE-export-rendering](#epi-rte-export-rendering), [EPI-RTE-wiki-validation](#epi-rte-wiki-validation) | None supplied | Lineage and shape checks do not establish source truth, encoding fidelity or final-answer grounding | Packets expose provenance and source-related excerpts; supported export bodies preserve documented lineage | Arbitrary authored prose/source entailment and qualifier-preserving clipping unresolved |
| [EPI-CLM-confidence-tags](#epi-clm-confidence-tags) | see record | SRC-1, `LINK.md`, doctrine/design | see record | [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) is a requested route; [EPI-RTE-export-rendering](#epi-rte-export-rendering) presets high | None supplied | Source-count maturity and explicitness are not independent truth evidence; retrieval confidence has a different target | Tags distinguish authored statement/inference/speculation intentions | No observed tagging judgment, calibration or inference acceptance |
| [EPI-CLM-review-accuracy](#epi-clm-review-accuracy) | see record | SRC-1, `LINK.md`, doctrine/design | see record | [EPI-RTE-review-marking](#epi-rte-review-marking), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | None supplied | Optional note; same caller can mark/re-arm; bulk confirm is a Boolean | Human accuracy confirmation is requested, reviewed state has consequential recall effects | Recorded reviewed status alone does not establish evidence-consuming acceptance |

## Bounded conclusion

Link acquires supplied user/project claims and external documents, retains them locally, and later selects compact excerpts for agents. The assessed source/import routes retain paths, revision strings or hashes but do not verify source truth; their epistemic source warrant is unknown. Structured export rendering is deterministic reshaping with explicit bracket escaping, not unrestricted verbatim preservation. Derived page counts and validation counts are warranted only as computations over the supplied records and inspected rules, not as external-world facts. First-person normalization has a concrete semantic counterexample, so the general route remains indeterminate rather than automatically non-ampliative.

The new-write gates evaluate detected secrets, similarity and revision/conflict patterns. Their separate disposition consumer can reject or admit a pending active page and supports caller overrides. These are operational safeguards, not truth acceptance. Pending review is not quarantine. Update appends supplied detail and resets review; it should not inherit the new-write secret-screening claim. Sync/file imports and direct edits are distinct admission paths. Archive withdraws a page from default focused-memory active selection, including the combined query's memory branch. It does not withdraw future operational availability across ordinary combined recall: the independent generic wiki branch can still rank and deliver the retained archived page, without memory-specific review/lifecycle warnings. This supported alternate consumer is see [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read), SRC-1, `mcp_package/link_core/wiki.py`, `mcp_package/link_core/search.py` and `mcp_package/link_core/query.py`. Historical/include_archived focused recall, direct file access and text already in a host window are additional exceptions. Actual generic delivery depends on query, corpus and ranking; no disclosure or reliance was observed.

The review protocol has a criterion, intended use and scope: the human confirms that a memory is accurate for future personal/project context. The implemented marker changes review warnings, ranking and the typed review horizon. The code does not consume mandatory evidence of that confirmation or a named factual test. No supplied claim-instance judgment therefore establishes acceptance, and index/backlink rebuild or retention cannot be called post-acceptance lifecycle integration. Arbitrary-source ingest requests source links, contradiction notes, confidence labels and coherent revision; the external agent's actual acquisition, entailment or ampliative conjecture is unobserved. The available templates afford localized theories; they do not supply a formulated candidate or exercised criticism/iteration. The runtime's independent theory-builder limits remain see [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki).

Wiki validation licenses structural admissibility and link/index consistency under its finite checks. Structured apply enforces its result before copying; agent-authored completion uses a post-write protocol. Neither verifies propositions against the source. Recall confidence targets query match, not truth. Focused abstention and stale-path warnings ask an external agent to verify or refrain; they do not remove the returned weak/stale candidate or enforce its final answer. Content delivery and operational ranking are implemented; actual host reliance and benefit remain unobserved. Startup supply and handoff instructions can affect a later session without an explicit recall, but supply does not establish acceptance or compliance.

The offline recall evaluator checks authored target ranks and can fail its own process on a hybrid regression. It does not automatically select a new product policy or accept a factual answer. Other accessible evaluator and maintenance bodies remain unassessed as named in coverage, so no system-complete absence of evidence-responsive behavior or knowledge testing follows. In the inspected usage module, retrieval recording supports observability; the popularity boost is explicitly retained as not adopted, and the inspected combined query does not pass salience. Retrieval counts cannot demonstrate learning or improvement. Independent learning, reflection, autonomy and self-improvement conclusions require their own behavioral and attribution evidence; no exercised benefit is established here. The embedding and cross-encoder routes remain separate, with unpinned external weights and no inspected parameter-update operation, not a system-wide verdict about learning.

## Shared records

### Operative objects

#### EPI-OBJ-memory-page
Label: Memory page

Source-native identity: Markdown pages under `wiki/memories/` rendered and reloaded by the memory core. Representational form: natural-language claim/body/procedure text and symbolic lifecycle/provenance fields, assessed separately by the ledger. Storage substrate: local Markdown. Closest supplied record is [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission); distinct identity is its durable output, not the admission progression. The title/TLDR can truncate; claim text is retained in the body. SRC-1, `mcp_package/link_core/memory.py`, implementation.

> ## Memory
>
> {clean_text}
> --- `mcp_package/link_core/memory.py`

#### EPI-OBJ-wiki-page
Label: Wiki page

Source-native identity: source/concept/entity/comparison/exploration pages addressed by Link's wiki categories. Representational form: natural-language sourced prose/code plus symbolic frontmatter and graph links; substrate: local Markdown. Closest supplied records are [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) and [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest); distinct identity is their shared output family, not either route. Checks and authorship differ and are not assigned one acceptance status. SRC-1, `LINK.md`, doctrine/design; `mcp_package/link_core/structured_ingest.py`, implementation.

> 3. Create a source page in `wiki/sources/` following the template
> 4. For each significant concept, entity, or claim in the source:
>    - If a wiki page exists: UPDATE it with new information, add the source to its Sources section, update `date_updated` and `source_count`
>    - If no wiki page exists: CREATE one following the appropriate template, set `maturity: seed`
> --- `LINK.md`

#### EPI-OBJ-capture-proposal
Label: Capture proposal

Source-native identity: candidate memory strings produced from note segments and retained in session captures. Representational form: natural-language candidate text with symbolic type/confidence/action metadata; substrate: raw Markdown captures and returned objects. Closest supplied record is [RT-RTE-session-capture](runtime.md#rt-rte-session-capture); distinct identity is the candidate content, not the capture route. Source-user identity is conditional on input provenance. SRC-1, `mcp_package/link_core/memory.py`, implementation. Normalization passage is retained in [EPI-RTE-proposal-normalization](#epi-rte-proposal-normalization); supplied capture record retains the automatic user-turn selection evidence.

### Routes

#### EPI-RTE-proposal-normalization
Label: Proposal normalization

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Material transformation part of the supplied capture route, not a duplicate capture operation. Endpoints/progression: segmented notes → `normalize_proposed_memory` → candidate memory → proposal selection/capture. Owner: deterministic regex code; state: text and classified memory type. No internal model judge or answer oracle; open proposal requests, not an evaluated improvement loop. Caller/human decides subsequent approval and shared writer can veto; no write is admitted by normalization itself. Guidance is the shipped replacement list; rollback means discard candidate or later edit/delete capture. SRC-1, `mcp_package/link_core/memory.py`, implementation.

Concrete deduction, not execution: `I prefer short replies` with preference type becomes `User prefers short replies.` after capitalization/replacement and final punctuation. This is referent-preserving only if the first-person speaker is the user. The manual path permits mixed notes; `assistant: I prefer short replies` loses its speaker prefix in segmentation and can become the same user-preference candidate. `From now on I only push to develop` loses its temporal lead-in. Neither universal semantic preservation nor non-entailment of every output is established; the route is indeterminate with speaker/time assumptions needed. Automatic user-only hook extraction is a source-supported limiting case that reduces, but does not erase, this general ambiguity.

- Immediate return: Normalized candidate string.
- Later read-back: Captured candidate can be re-mined/selected at later acceptance.
- Delegated visibility: Local review callers receive candidate; external further delegation uninspected.
- Selection predicate: Replacement patterns, classified type and bounded segments.
- Invalidation or expiry: Source/candidate change or dismissal changes later proposal; no claim-specific expiry here.
- Activation or effect: Candidate transformation wired; changed future behavior unobserved.
- Evidence limits: No executed candidate or identity/temporal-fidelity test.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> line = re.sub(r"^(?:user|human|me|assistant|codex|agent)\s*:\s*", "", line, flags=re.IGNORECASE)
> --- `mcp_package/link_core/memory.py`

> value = re.sub(r"^(?:from now on|going forward|starting now|starting today)[,\s]+", "", value, flags=re.IGNORECASE)
> --- `mcp_package/link_core/memory.py`

> (r"^i prefer\b", "User prefers"),
> --- `mcp_package/link_core/memory.py`

#### EPI-RTE-memory-check
Label: Memory candidate checking

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Checking part of the supplied admission route; its findings are distinct from the disposition below. Endpoints/progression: proposed text/title plus active record list → secret scanner, duplicate matcher, conflict matcher → findings to writer. Owner: deterministic core, optional numerical embedder for conflict revision similarity. State: type/scope/project, active claims, caller exclusions; effects: finding lists, not proof of truth. Check target is secret-shaped text or potential duplication/revision/conflict within eligible active memory types, not all logical contradictions. Lexical conflict branches use negation/overlap, options and reversed preference cues; semantic tier requires revision cue and threshold. Human/caller proposes and resolves actual meaning; code selects candidates, disposition can veto. Open requests; no expected-answer oracle, no product successor. New-write secret gate can be bypassed by explicit argument; update checks conflicts but its inspected body does not perform that new-write secret screen. SRC-1, `mcp_package/link_core/memory.py`, implementation.

- Immediate return: Secret labels or duplicate/conflict candidates.
- Later read-back: inapplicable — checking alone does not persist a judgment; admitted content is separate.
- Delegated visibility: Mutation caller receives candidates for review.
- Selection predicate: Type/project/active filters and heuristic threshold rules.
- Invalidation or expiry: Recomputed from current records; model/cache changes can change semantic candidates.
- Activation or effect: Findings feed rejection at separate disposition, not independent acceptance.
- Evidence limits: False positives/negatives and numerical-provider internals unassessed; no observed check results.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if new_negated != has_negation(record_text) and len(overlap) >= 1 and overlap_ratio >= 0.45:
>             score = max(score, 92)
>             reasons.append("opposite_negation")
> --- `mcp_package/link_core/memory.py`

#### EPI-RTE-memory-disposition
Label: Memory write disposition

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Disposition part, separate from checks and persisted output. Endpoints/progression: checker findings plus override/supersedes arguments → reject or continue shared new-memory writer → created/refusal result. Owner: software gate; caller proposes and can override detected secrets, duplicates and conflicts. Protocol human may veto by withholding approval; no authenticated human result is consumed. State/actions: pending active page and optional archival lineage after admission, or no creation on rejection. Trigger: explicit remember/accepted capture request; proposed change: supplied durable context. Guidance is approved-memory contract and refusal messages. Open requests; answer oracle inapplicable, no expected truth. Journal rollback/recovery belongs to [RT-RTE-local-recovery](runtime.md#rt-rte-local-recovery), not a truth-check rollback. SRC-1, `mcp_package/link_core/memory.py`, implementation; protocol see [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory).

- Immediate return: Created identity or created=False and findings.
- Later read-back: Admitted page is subsequently read by recall; refusal itself has no durable acceptance record.
- Delegated visibility: Caller/workspace readers; no delegated worker.
- Selection predicate: Gate predicates and caller override arguments; superseded item excluded from candidate blocking.
- Invalidation or expiry: Later updates/archive/supersession and file mutations can change eligibility.
- Activation or effect: Reject/permit operation wired; no human assent or later behavioral activation evidenced.
- Evidence limits: Other admission paths bypass this mechanism; source strings and success do not authenticate approval.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if duplicate_candidates and not allow_duplicate:
>         return {
>             "created": False,
>             "duplicate": True,
> --- `mcp_package/link_core/memory.py`

#### EPI-RTE-memory-update
Label: Memory detail update

Closest supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) explicitly leaves detailed updates to later analysis. Distinct referent is an existing-page detail append, not new-page creation. Endpoints/progression: identifier/text/source → active-page resolution and conflicts against other records → refusal or appended update → pending review metadata → later recall. Owner: caller supplies new detail; software checks a bounded conflict domain and writes. State/effects: old body plus update, update count/source/time, removal of reviewed fields. Trigger/proposed change: explicit update to active context. Guidance requests review again with the human; caller can decline or override conflicts, software rejects empty/unresolved/inactive targets. Open update requests; no factual expected-answer oracle. Journaled recovery applies, but the inspected implementation does not run the new-write secret screen. Appending preserves older body text rather than proving that all previous claims have been semantically reconciled. SRC-1, `mcp_package/link_core/memory.py`, implementation; `LINK.md`, doctrine/design.

- Immediate return: Updated identity/remaining issues or conflict refusal.
- Later read-back: Appended body, pending review state and update provenance reach later reload/recall.
- Delegated visibility: Workspace readers and calling hosts receive updated selected content; no inner worker.
- Selection predicate: Resolved active identifier, nonempty supplied detail, other-record conflicts and allow_conflict.
- Invalidation or expiry: Removes reviewed_at/review_note and sets pending; later human review re-arms metadata, archive suppresses default focused-memory selection but not generic wiki delivery of the retained page.
- Activation or effect: Durable detail acquisition and review reset wired; changed host behavior unobserved.
- Evidence limits: Caller source label is not authenticated evidence; no universal conflict resolution, secret safety or truth acceptance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> updated_body = append_memory_update(body, clean_text, timestamp, clean_source)
> --- `mcp_package/link_core/memory.py`

> updated_text = update_frontmatter_fields(original, updates, remove={"reviewed_at", "review_note"})
> --- `mcp_package/link_core/memory.py`

#### EPI-RTE-review-marking
Label: Memory review marking

Closest supplied record [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) explicitly leaves detailed review to later analysis; distinct referent is the subsequent callable reviewed-state mutation, not new-page admission. Endpoints/progression: identifier/optional note → resolve page → reviewed metadata/re-armed due date → later recall review state and rank. Owner: caller asserts review; code writes marker/date. State: existing page and typed review window. Trigger/proposed change: explicit review or CLI bulk review with confirm; caller can withhold the call, code can reject unresolved identifier, journal supports recovery. Guidance asks human accuracy confirmation, intended use future personal/project context; source evidence consumption is not mandatory. Proposer/decider is caller/human under protocol, software does not independently judge claim accuracy. Open requests; no answer oracle or live improvement trigger. Bulk confirm strengthens interaction friction, not authenticated per-content evidence. SRC-1, `mcp_package/link_core/memory.py` and `link.py`, implementation; criterion doctrine in [EPI-CLM-review-accuracy](#epi-clm-review-accuracy).

- Immediate return: Reviewed state and remaining issues.
- Later read-back: Later recall reloads reviewed metadata and its due date.
- Delegated visibility: Workspace hosts receive review state/warnings in selected packets.
- Selection predicate: Resolved identifier; bulk mode active pending/due list and caller confirm.
- Invalidation or expiry: Update resets pending/removes review evidence fields; typed window becomes due and can be re-armed.
- Activation or effect: Changes future warning/ranking capacity; actual approval or changed host reliance unobserved.
- Evidence limits: Optional note and caller-written marker do not establish evidence-consuming acceptance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> clean_note = note.strip() if note else ""
>     updates = {
>         "review_status": "reviewed",
>         "reviewed_at": f'"{timestamp}"',
>     }
> --- `mcp_package/link_core/memory.py`

> "review_status": "pending",
> --- `mcp_package/link_core/memory.py:1657-1663`

The downstream selector consumes reviewed status as a ranking input, independently of whether the marker corresponds to an actual accuracy judgment:

> if str(record.get("review_status") or "").lower() == "reviewed":
>     boost += 3
> --- `mcp_package/link_core/memory.py`

#### EPI-RTE-memory-withdrawal
Label: Memory archive withdrawal

Closest supplied record [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) mentions archive/restore as recovery; distinct referent is subsequent focused-memory eligibility withdrawal and restoration. Endpoints/progression: caller identifier/status/reason → journaled lifecycle fields → future focused-memory recall's active filter, including the combined query's memory branch. Owner: caller chooses archival/reinstatement, core enforces requested state and focused-memory selector excludes inactive unless explicit alternatives. The independent generic wiki consumer is see [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read): ordinary combined query and explicit search/context can still deliver the retained archived page. This is not a duplicate archive route; it is the alternate consumer that bounds archive's force. Guidance: archive stale/wrong memory rather than permanent deletion. Human can veto by not requesting; unresolved page/unsupported status rejects. Open lifecycle requests, no truth oracle: archive reason may contain criticism but code does not evaluate it. State replacement is journal-recoverable; no current host-context eviction. SRC-1, `mcp_package/link_core/memory.py`, implementation; `LINK.md`, doctrine/design.

- Immediate return: Status-change result.
- Later read-back: Changed status reaches later focused-memory selection; retained body remains independently available through generic wiki search/context and ordinary combined-query page delivery.
- Delegated visibility: Local and connected host consumers receive selected memory packets or generic page excerpts; generic page compaction omits memory-specific review/lifecycle warnings.
- Selection predicate: Resolved page; focused-memory default active filter, optional historical/include_archived exceptions. Generic wiki selection instead ranks all nonhidden Markdown and graph neighbors without the focused lifecycle/project gates.
- Invalidation or expiry: Restore reverses archive fields; supersession and expiry independently change focused-memory eligibility. Archive does not delete or exclude the page from generic wiki enumeration.
- Activation or effect: Focused-memory operational withdrawal/restoration wired; generic delivery remains implemented and possible, not observed; no actual reliance/refutation trace.
- Evidence limits: No all-query withdrawal or erasure of prior host text; archive is not proof the proposition is false. Actual generic delivery depends on query/corpus/ranking.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> elif not include_archived and not is_active_memory(record):
>             continue
> --- `mcp_package/link_core/memory.py`

Correction inspection directly checked SRC-1, `mcp_package/link_core/wiki.py` enumeration and complete `context_for_topic`, `mcp_package/link_core/search.py` complete `search_pages`, and `mcp_package/link_core/query.py` branch assembly and `_compact_page`, implementation layer. Enumeration includes retained memory Markdown; search and context use page matches and graph neighbors without the focused-memory gate. Combined query compacts those pages separately from its filtered memory results. Minimum passages and the distinct consumer's findings are see [MEM-RTE-wiki-read](memory.md#mem-rte-wiki-read) and [RT-RTE-context-recall](runtime.md#rt-rte-context-recall).

#### EPI-RTE-export-rendering
Label: Structured export rendering

Part of: [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest)

Transformation part of supplied structured ingest container. Endpoints/progression: loaded export pages/relationships → group/sort/count/render → candidate source-page strings. Owner: deterministic adapter. State: export manifest, navigation, page bodies and relationship records; effects: grouped Markdown, provenance fields, calculated connection counts. Caller chooses exclusions/apply/adoption; software rejects colliding groups; later stage gate can veto. Open supported-export requests, no expected-answer oracle. Guidance is fixed renderer and schema; source hash/revision and adapter details persist on apply, rollback/discard is stage or copy recovery. Source truths are acquired, body reshaping is non-ampliative under the documented encoding change; generated count claims are derivations over supplied records. `confidence: high` is preset, not a check result.

Concrete deduction: input body `Use [[name]]` has no trailing newline to strip, triggers replacement and becomes `Use [\[name]]` inside a fenced Markdown block. A note records the escape and raw retains exact bytes. Therefore the rendered character string is not universally byte-verbatim despite its TLDR wording. This establishes an explicit encoding exception, not falsity of upstream documentation. SRC-1, `mcp_package/link_core/structured_ingest.py`, implementation.

- Immediate return: Output page strings and render statistics.
- Later read-back: Applied source bodies/manifest feed future query and plan ownership checks.
- Delegated visibility: Local wiki consumers, no internal model delegation.
- Selection predicate: Navigation groups/exclusions, sorted page inputs and supported relationships.
- Invalidation or expiry: Source hash/output ownership and explicit pruning govern later regeneration.
- Activation or effect: Rendering wired; staged/admitted persistence separate.
- Evidence limits: Export truth/source authenticity unknown; count domain limited to supplied records, escaped code not exact bytes.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> body = str(page.get("markdown") or "").rstrip("\n")
>             escaped = "[[" in body
>             if escaped:
>                 body = body.replace("[[", "[\\[")
>                 escaped_pages.append(str(page.get("canonical_url") or ""))
> --- `mcp_package/link_core/structured_ingest.py`

#### EPI-RTE-wiki-validation
Label: Wiki validation checking

Part of: [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest)

Finite checking part of the staged route, also exposed as standalone CLI/MCP/HTTP check. The containing staged route remains valid; reuse by other consumers does not make this another apply operation. Endpoints/progression: wiki files → shape/section/date/link/backlink/secret checks → findings and passed Boolean. Owner/evaluator: deterministic validator. Context/state: wiki roots, parsed frontmatter/body, expected backlink map; target/domain: file admissibility and structural consistency, not proposition truth or source entailment. Caller chooses strictness; warning-only findings pass by default. Validator proposes findings, separate consumers decide action. Open validation requests, no semantic expected-answer oracle; no product change is selected. SRC-1, `mcp_package/link_core/validation.py`, implementation. Complete function inspected; no source-content comparison or confidence-calibration check in that function.

- Immediate return: passed, counts and typed findings.
- Later read-back: inapplicable — validator does not persist acceptance; changed wiki belongs to its consumers.
- Delegated visibility: Calling agent/operator receives result; no worker delegation.
- Selection predicate: All nonhidden Markdown plus required paths; finite fields/sections/link rules.
- Invalidation or expiry: Recomputed on next invocation; strict flag changes warning disposition.
- Activation or effect: Feeds staged rejection or post-write completion protocol, distinct force by consumer.
- Evidence limits: Structural success does not license factual claims or guarantee every sensitive value is detected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> error_count = sum(1 for finding in findings if finding["severity"] == "error")
>     warning_count = sum(1 for finding in findings if finding["severity"] == "warning")
>     passed = error_count == 0 and (warning_count == 0 if strict else True)
> --- `mcp_package/link_core/validation.py`

#### EPI-RTE-staged-disposition
Label: Staged wiki disposition

Part of: [RT-RTE-structured-ingest](runtime.md#rt-rte-structured-ingest)

Separate disposition part. Endpoints/progression: caller-authorized plan → reject conflicts → stage generated outputs/log/index/backlinks → validator → reject failure or copy live files and ownership manifest. Owner: adapter enforces finite gate, caller chooses apply/options and can veto invocation. Proposed change: rendered wiki files. Guidance: plan ownership and shape validation; current hashes/manifests persist. Mode: open supported exports, no factual expected-answer oracle, no live adaptive curriculum. Caught copy exceptions restore original bytes; direct agent/file writes are different paths. SRC-1, `mcp_package/link_core/structured_ingest.py`, implementation. Acceptance here is structural/ownership admission, not evidence-consuming acceptance of a truth-apt claim.

- Immediate return: Applied count and validation or raised conflict/validation error.
- Later read-back: Admitted wiki and manifest reach later query/adapter invocations.
- Delegated visibility: Ordinary workspace consumers; no internal model worker.
- Selection predicate: No plan conflicts and staged passed result; explicit apply/options.
- Invalidation or expiry: Later source/output change and explicit prune; copy failure can restore originals.
- Activation or effect: Code veto before live copy wired; successful operation unobserved.
- Evidence limits: No universal pre-write wiki gate, truth oracle or crash/concurrent isolation guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> validation = validate_wiki(stage_wiki)
>         if not validation.get("passed"):
>             raise StructuredIngestError(f"staged wiki failed validation: {validation.get('findings')}")
> --- `mcp_package/link_core/structured_ingest.py`

#### EPI-RTE-context-compaction
Label: Context excerpt compaction

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Material transformation part of supplied retrieval, distinct from its selector and match evaluator. Endpoints/progression: selected memory summary/steps or page content → compact objects and character-limited excerpts → packet/capsule → external agent; follow-up reload remains available. Owner: deterministic budget/character rules. State: selected content, budget and provenance metadata; effect: excerpt rather than full source in initial host context. No approval or expected-answer oracle; open query requests. The host interprets the excerpt and chooses further reads. SRC-1, `mcp_package/link_core/query.py`, implementation.

Concrete deduction, not execution: `_trim_text("Safe only locally", 10)` returns `Safe on...` because the retained prefix is seven characters. In general a qualifier placed after the cutoff does not reach the excerpt, even though the ellipsis signals incompleteness. The inspected `_compact_page` passes page content and its primary/neighbor character limit to this function. Semantic preservation therefore depends on source content and cutoff; the relation is indeterminate at the whole-route level, not a warranted transformation of every claim. The example tests the helper's rules, not a claimed deployed budget or actual user page.

- Immediate return: Bounded excerpt/object with provenance and follow-up fields.
- Later read-back: inapplicable — this constructor does not retain a new content version; later source reload uses the underlying retained wiki.
- Delegated visibility: Calling host receives excerpts by value; fuller content stays outside initial context but locally reachable.
- Selection predicate: Budget-specific primary/neighbor limits and selected summaries/steps; no semantic qualifier detector.
- Invalidation or expiry: New query/budget/source yields a new packet; old host-window text is not automatically evicted.
- Activation or effect: Context exclusion and on-demand restoration capacity wired; actual host reliance unobserved.
- Evidence limits: Ellipsis/provenance do not preserve omitted qualifications; no observed fidelity or answer-benefit test.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> def _trim_text(value: object, max_chars: int) -> str:
>     text = str(value or "").strip()
>     if len(text) <= max_chars:
>         return text
>     return text[: max(0, max_chars - 3)].rstrip() + "..."
> --- `mcp_package/link_core/query.py`

#### EPI-RTE-recall-assessment
Label: Recall match assessment

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Checking part of supplied context route. Endpoints/progression: query and retrieved memory metadata/body → match confidence → top-result abstention recommendation → focused MCP JSON and external-agent guidance. Owner: lexical rule/optional semantic cap; agent decides final reliance. Target/domain: lexical query coverage or numerical closeness, not factual truth; strong result can be an exact match to a false claim. State: ranked results, confidence labels; no candidate truth mutation or acceptance. Open recall requests; no expected-answer oracle. Shared combined query is a countercase to universal first-class abstention: it uses compact review/weak-match guidance, while focused memory mode carries `abstention`. SRC-1, `mcp_package/link_core/memory.py`, `mcp_package/link_mcp/server.py`, `mcp_package/link_core/query.py`, implementation.

- Immediate return: Confidence label and recommended abstention/reason/guidance.
- Later read-back: inapplicable — result is current-turn advice, not persisted acceptance or revised policy.
- Delegated visibility: Calling host receives both advice and matching memory content.
- Selection predicate: Query token coverage and top result confidence; focused branch condition.
- Invalidation or expiry: Fresh query/record/model selection recomputes result.
- Activation or effect: Advisory cautious-use instruction; neither weak candidate removal nor final-answer enforcement.
- Evidence limits: No observed compliance or calibration; match score and review endorsement are distinct.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if q and (q in title or q in tldr):
>         return "strong"
> --- `mcp_package/link_core/memory.py`

> "abstention": _core_recall_abstention(memories),
> --- `mcp_package/link_mcp/server.py:1414-1426`

> "Treat matches as hints only; say the memory has nothing "
> "reliable on this rather than asserting from a weak match."
> --- `mcp_package/link_core/memory.py`

#### EPI-RTE-path-staleness
Label: Repository path staleness

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Checking/warning part of context recall newly traced beyond runtime's selection summary. Endpoints/progression: selected full memory body/context → bounded referenced-path checks and Git history/rename lookup → stale_paths on compact memory → verify/review instruction. Owner: deterministic checker and packet builder. Target/domain: a named path formerly tracked but missing now, optionally a known successor; not whether the claim remains correct. Activation condition: provided repo_root with `.git`, selected memories and bounded path references. Caller/agent decides review/update; code does not rewrite/archive content. Open query/check operation, no truth oracle. SRC-1, `mcp_package/link_core/staleness.py`, `mcp_package/link_core/query.py`, implementation.

- Immediate return: Removed/renamed-path findings attached to selected memories.
- Later read-back: inapplicable — findings are current-query annotations, not stored acceptance/revision.
- Delegated visibility: Agent gets stale_paths plus guidance to verify before relying.
- Selection predicate: Selected memory identities; parsed path candidates up to lookup limit; missing and formerly known paths only.
- Invalidation or expiry: Current filesystem/history/selected records change later findings.
- Activation or effect: Advisory verify/update request, not automatic rejection or withdrawal.
- Evidence limits: No general staleness conclusion from no findings; Git/history/parse limits and unobserved behavior.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (self.root / candidate).exists():
>                 continue
>             if not self._was_known(candidate):
>                 continue  # never in the repository: prose, not a stale reference
> --- `mcp_package/link_core/staleness.py`

> "A recalled memory names a repository file git no longer has "
> "(see its stale_paths); verify the memory against the current code "
> "before relying on it, and suggest the user review or update it.",
> --- `mcp_package/link_core/query.py`

#### EPI-RTE-consolidation-plan
Label: Memory consolidation planning

Closest supplied [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) supplies capture backlog and [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) supplies durable context; distinct identity is read-only planning, not either write operation. Endpoints/progression: capture/review payloads and optional merge candidates → counts, duplicate/theme groups and action commands → human/agent chooses subsequent explicit mutation. Owner: code generates plan, human chooses and may veto every action. State: payload counts, similarity helpers, survivor/absorbed claims; effect: report, no content merge. Count propositions are entailed under the payload's count/list interpretation; duplicate/theme/merge correctness is heuristic, unassessed in the unread helper bodies. Open maintenance requests/backlog prompts; no factual expected-answer oracle or automatic product successor. Guidance is review/approval safety text; rollback inapplicable for read-only planner, later writes have separate gates. SRC-1, `mcp_package/link_core/consolidate.py`, `mcp_package/link_mcp/server.py`, implementation.

- Immediate return: Read-only counts, groups, review queue and mutation commands.
- Later read-back: inapplicable — this planner writes no durable content or policy; subsequent chosen writes are separate.
- Delegated visibility: Caller/human sees proposals through terminal or MCP JSON.
- Selection predicate: Provided capture/review payloads, helper groups and optional merge candidates.
- Invalidation or expiry: Recomputed on new backlog; no plan expiry or automatic application.
- Activation or effect: Advisory plan; human-approved commands may later change context.
- Evidence limits: No observed semantic merge correctness, criticism-led iteration or improvement; grouping helpers not fully read.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "safety": (
>             "Read-only plan. Nothing was merged, deleted, or saved. "
>             "Run the listed commands only after the user approves each action."
>         ),
> --- `mcp_package/link_core/consolidate.py`

### Claims

#### EPI-CLM-source-backed
Label: Source-backed context packet

Claimed operation: query returns compact, source-backed context for a later agent answer, rather than answering directly. Closest supplied [RT-RTE-context-recall](runtime.md#rt-rte-context-recall) is implementation progression, not a claim declaration; [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory) concerns approval rather than source warrant. No supplied claim counterpart after comparison. SRC-1, `mcp_package/link_core/query.py`, doctrine/design, quoted via supplied runtime record. Its operative instruction is:

> "Prefer recall-ready reviewed memories for personalization and source-backed wiki pages for factual claims.",
> --- `mcp_package/link_core/query.py`

#### EPI-CLM-confidence-tags
Label: Claim confidence tags

Claimed operation: source-derived claim confidence denotes explicit statement, reasonable inference or speculation; maturity also rises with source count. These are authored labels and source-count policy, not calibrated factual probabilities. Closest supplied [RT-RTE-agent-wiki](runtime.md#rt-rte-agent-wiki) describes requested authoring; distinct identity is the doctrine's claim-classification convention. No supplied claim counterpart after comparison. SRC-1, `LINK.md`, doctrine/design.

> - Tag confidence on claims: `high` (explicitly stated), `medium` (reasonable inference), `low` (speculative)
> --- `LINK.md`

> - Update the `maturity` field: seed (1 source) → growing (2-3 sources) → mature (4-6 sources) → established (7+ sources)
> --- `LINK.md`

#### EPI-CLM-review-accuracy
Label: Human memory accuracy review

Claimed operation: the human confirms accuracy before a memory is marked reviewed, after which the typed trust window is re-armed; stale/wrong memories should be archived. Closest supplied [RT-CLM-approved-memory](runtime.md#rt-clm-approved-memory) governs initial save approval, not subsequent accuracy review; distinct decision and horizon. SRC-1, `LINK.md`, doctrine/design.

> - After the human confirms a memory is accurate, run `python3 link.py review-memory "<name-or-title>" .`. Reviewing re-arms the memory's trust window (`review_after`): project context stays trusted for 3 months, preferences/notes/procedures for 6, decisions and stable facts for 12.
> --- `LINK.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; external-agent delivery channels are see [RT-BAP-agent-steering](runtime.md#rt-bap-agent-steering) and [RT-BAP-context-packet](runtime.md#rt-bap-context-packet), with per-function force bounded in the ledger above.

### Supplementary evidence limits

The offline evaluator's operative result is a regression exit code, not live content acceptance:

> if hybrid_groups[group][metric] < baseline[metric]:
>     print(f"REGRESSION: hybrid {group} {metric} below lexical baseline", file=sys.stderr)
>     return 1
> --- `scripts/eval_recall_quality.py`

Retrieval event recording stores selected names rather than queries, outcomes or factual judgments. The usage-aware alternative is explicitly not adopted; this prevents inferring that current retrieval counts automatically adapt production query ranking. SRC-1, `mcp_package/link_core/usage.py`, implementation and attributed design history; `mcp_package/link_core/query.py`, inspected combined-query call has no salience argument. This is not an all-call-site absence assertion.

> # MEASURED AND NOT ADOPTED. Ranking is not usage-aware, and this is the
> # function that was tried. scripts/eval_salience.py splits queries by whether
> # the answer is a memory with retrieval history, and at every ceiling from 1
> # to 4 the cold half got harder to find: at ceiling 1 the hot half gained
> # nothing and cold still fell. The average improves, which is exactly how this
> # kind of change gets shipped without anyone noticing what it cost.
> --- `mcp_package/link_core/usage.py`

This comment is attributed measurement history, not a reproduced experiment. The unread salience evaluator prevents independent assessment of that comparison. No exercised self-improvement or component effect follows.
