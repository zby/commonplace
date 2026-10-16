---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "ByteRover CLI epistemic routes: structural admission, caller judgment, lossy delivery, post-write review and bounded evaluation claims."
run-id: AAS-2026-10-15-byterover-cli-71610aaf716b-01
reviewed-boundary: "1052ac1a5dd0fde4da8693d4712064f7876c269c"
---

# ByteRover CLI epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on the project knowledge ByteRover stores and supplies, rather than whether the files exist. Scope, dependencies, frozen source and exclusions: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register), SRC-1. The boundary is a complete repository artifact but a partial knowledge loop: external authoring/consuming agents, providers, Cloud, shared UI and transport internals are excluded. Their absence prevents end-to-end judgments about authorship, factual checking, actual reliance and deployed behavior. No execution or causal-experiment source is registered.

Public claims assessed are [RT-CLM-project-memory](runtime.md#rt-clm-project-memory), [EPI-CLM-agent-native](#epi-clm-agent-native), [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) and [EPI-CLM-query-answer](#epi-clm-query-answer). None is treated as evidence of current-route operation. Runtime findings are provisional: counterpaths already supplied there defeat a universal curate gateway, mandatory pre-write human approval and internal-model authorship of all knowledge. Direct inspection below further separates a recorded review decision from evidence-consuming factual acceptance, and a maturity label from factual validation.

### Coverage

“Supplied” means reliance on a named runtime record, not a direct reread. “Direct” means additional SRC-1 source inspection in this member. All paths are commit-relative at the reviewed revision.

| Entry point or operation | Source path | Coverage and records, or remaining limit |
|---|---|---|
| CLI dispatch and lifecycle hooks | `package.json`; `bin/run.js`; `src/oclif/hooks/` | Direct package registration; supplied launcher account in [RT-RTE-curate-session](runtime.md#rt-rte-curate-session). Init/update/config/error hooks are enumerated, not traced through all bodies. Product-update admission remains unassessed. |
| CLI/MCP curate | `src/oclif/lib/curate-session.ts`; `src/server/infra/mcp/tools/brv-curate-tool.ts`; `src/server/infra/mcp/tools/index.ts` | Supplied [RT-RTE-curate-session](runtime.md#rt-rte-curate-session), [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission); direct MCP export inventory. |
| Writer and factual attribute validation | `src/server/infra/render/writer/html-writer.ts`; `src/server/infra/render/elements/make-validator.ts`; `src/server/infra/render/elements/bv-fact/schema.ts`; `src/server/infra/render/elements/bv-fact/validator.ts` | Direct; [EPI-RTE-fact-validation](#epi-rte-fact-validation). |
| Query, selection and cache | `src/server/infra/executor/query-executor.ts`; `src/oclif/lib/query-retrieval.ts` | Supplied [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval). Cache confidence/freshness is not endorsement. |
| Rendered versus raw read | `src/oclif/commands/read.ts`; `src/oclif/lib/read-topic.ts`; `src/server/infra/render/reader/html-renderer.ts`; `src/server/infra/render/reader/html-parser.ts` | Direct; [EPI-RTE-render-content](#epi-rte-render-content), [EPI-RTE-read-topic](#epi-rte-read-topic). Raw read is a counterexample to universal renderer loss. |
| Search | `src/oclif/commands/search.ts` | Direct command description and request setup; [EPI-CLM-query-answer](#epi-clm-query-answer). Search result formatting/excerpt completeness not independently traced; no equivalence to a complete topic asserted. |
| Internal curate, context compaction | `src/server/infra/executor/curate-executor.ts`; `src/agent/infra/llm/agent-llm-service.ts` | Supplied [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation), [RT-RTE-context-control](runtime.md#rt-rte-context-control), [RT-CMP-content-generator](runtime.md#rt-cmp-content-generator). Semantic entailment of generated outputs remains unresolved. |
| Registered tools | `src/agent/infra/tools/tool-registry.ts` | Direct factory inventory includes map, code execution, curate, expand, file discovery/read/write, ingest, search, map and swarm operations. Supplied internal-control account covers dispatch controls, not every worker. Ingest extraction, map/swarm judgments and their semantic admissions remain uninspected; prevents a system-complete negative about inference or checking. |
| Review and withdrawal | `src/server/infra/transport/handlers/review-handler.ts`; `src/server/infra/process/curate-html-log.ts`; `src/server/infra/transport/handlers/push-handler.ts` | Direct review handler; supplied pending-selection and push consumers in [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync); [EPI-RTE-review-decision](#epi-rte-review-decision). |
| Direct edit, hub, Cloud | `src/server/infra/transport/handlers/context-tree-handler.ts`; `src/server/infra/hub/hub-install-service.ts`; `src/server/infra/transport/handlers/pull-handler.ts` | Supplied [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit), [RT-RTE-hub-install](runtime.md#rt-rte-hub-install), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync). Imported bytes have unknown source warrant; no semantic audit inferred. |
| Dream scan, finalize, undo | `src/server/infra/dream/tool-mode/dream-session.ts`; `src/server/infra/dream/tool-mode/prune-candidates.ts`; `src/server/infra/dream/tool-mode/merge-candidates.ts`; `src/server/infra/dream/dream-undo.ts`; `src/oclif/commands/dream/undo.ts` | Direct selected algorithms, archive and undo; [EPI-RTE-prune-candidates](#epi-rte-prune-candidates), [EPI-RTE-dream-undo](#epi-rte-dream-undo), supplied [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance). Link and synthesis generator internals not independently assessed; orchestration does not establish semantic synthesis. |
| Hook and maintenance instructions | `src/oclif/commands/hook-prompt-submit.ts`; `src/server/templates/sections/brv-instructions.md`; `src/server/templates/skill/dream.md` | Direct; [EPI-RTE-hook-instructions](#epi-rte-hook-instructions). Shipped instructions request future behavior, not observed compliance. |
| Versioning, sources, worktrees, migration, reset, connector installation | `src/oclif/commands/vc/`; `src/server/infra/transport/handlers/vc-handler.ts`; `src/server/infra/transport/handlers/source-handler.ts`; `src/server/infra/transport/handlers/worktree-handler.ts`; `src/server/infra/transport/handlers/migrate-handler.ts`; `src/server/infra/transport/handlers/reset-handler.ts`; `src/oclif/commands/connectors/` | Available, not deeply inspected here; supplied runtime explicitly leaves these incomplete. They can alter retained content, scope or instruction delivery. Prevents complete lineage, rollback and admission judgments, not the positive route findings below. |
| Public evaluation | `README.md`; `paper/README.md`; `paper/main.tex` | Direct reported claims, metrics and ablation sections; [EPI-CLM-benchmark-results](#epi-clm-benchmark-results). No question-level outputs, executed harness or intervention records supplied; prevents independent accuracy verification and causal attribution. Tests remain available but uninspected evaluators of implementation, not factual topic acceptance. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-topic-statements](#epi-obj-topic-statements) | Project/personal assertions, reasons and explanations, scoped by authored text | Typed facts and retained knowledge | SRC-1, `src/server/infra/render/elements/bv-fact/schema.ts` | A type label does not supply evidence or identify an actual true proposition in a supplied run. |
| [EPI-OBJ-topic-rules](#epi-obj-topic-rules) | Prescriptive rules are not inherently truth-apt; any accompanying descriptive premises are assessed separately | Behavior guidance | see [EPI-OBJ-topic-rules](#epi-obj-topic-rules) | Host interpretation determines compliance; renderer severity is not enforcement. |
| [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | Mixed container, not one proposition | see [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | Container identity remains valid; semantic parts above need no supersession. |
| [EPI-OBJ-runtime-signals](#epi-obj-runtime-signals) | Counters/timestamps support bounded arithmetic statements; importance/maturity are policy labels | Ranking and cleanup inputs | SRC-1, `src/server/core/domain/knowledge/runtime-signals-schema.ts` | `validated` is not a recorded factual acceptance criterion. |
| [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | HTML errors, write success, pending status and backup are symbolic operational objects, not factual verdicts | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | Selection and recovery refer to changes, not claim truth. |
| [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | Matched topic text and cache payload carry candidate assertions; scores select rather than verify them | see [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | Shared/unreadable hits may be omitted; rendered content may lose evidence links. |
| [RT-RTE-context-control](runtime.md#rt-rte-context-control) | Model summaries may contain truth-apt task claims; deterministic checkpoint metadata describes task state | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | No concrete supplied summary permits entailment or factual acceptance assessment. |
| [RT-CMP-content-generator](runtime.md#rt-cmp-content-generator) | Distributed parameters are not individually accessible propositions here | see [RT-CMP-content-generator](runtime.md#rt-cmp-content-generator) | Parameter mutation, exact weights and endpoint contents remain opaque; no parametric-learning inference. |
| [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | Bundles may contain assertions; skills may contain prescriptions | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | Imported content provenance is publisher-based, not locally warranted. |

## Authority-route ledger

Each row is a distinct consequential function. Generic route fields owned by the cited declaration are referenced with `see`; epistemic classifications here apply only to the named edge, not every possible output of its enclosing route. Architectural status denotes inspection support, not operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-curate-session](runtime.md#rt-rte-curate-session) | content transformation | implemented | [EPI-OBJ-topic-statements](#epi-obj-topic-statements) | truth-apt transformation: acquisition/import | Caller HTML enters target | Caller authors; semantic checking external | see [RT-RTE-curate-session](runtime.md#rt-rte-curate-session) | see [RT-RTE-curate-session](runtime.md#rt-rte-curate-session) | Authoring prompt advisory; envelope enforcing | Source warrant unknown | Caller can submit candidate for writing | Caller → continuation HTML → writer; permissive, session | SRC-1, `src/oclif/lib/curate-session.ts` | [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | none | No attribution of caller reasoning to ByteRover |
| [EPI-RTE-fact-validation](#epi-rte-fact-validation) | check/evidence production | implemented | [EPI-OBJ-topic-statements](#epi-obj-topic-statements) | no content change | Topic structure and fact attributes | Registry/Zod; markup domain only | Before writer I/O | Schema success or errors | Enforcing input to writer | License only for checked syntactic predicates | Writer may proceed or return correction | Validator → writer result → caller, enforcing, one submission | SRC-1, `src/server/infra/render/writer/html-writer.ts` | none | none | Not a factual oracle |
| [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | disposition/acceptance | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Structural success and overwrite policy | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | Enforcing within this writer | Operational admission, not evidence-consuming acceptance of truth | Allows write or rejects candidate | Writer/caller, structured error/success, enforcing, submission | SRC-1, `src/server/infra/render/writer/html-writer.ts` | none | none | Direct edit and imports are counterpaths |
| [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | retention | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Persist admitted topic | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | see [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) | Makes bytes available | No new semantic warrant from persistence | Later retrieval eligible before review | Tree → query/read, permissive, until changed | SRC-1, `src/server/infra/render/writer/html-writer.ts` | [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | none | Not lifecycle integration after factual acceptance |
| [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation) | content transformation | implemented | [EPI-OBJ-topic-statements](#epi-obj-topic-statements) | truth-apt transformation: indeterminate | Model extraction/grouping/final HTML | see [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation) | see [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation) | see [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation) | Prompt guidance then writer enforcement | No checked source-to-output entailment | Can author and replace retained guidance | Model output → writer → future readers, permissive, persistent | SRC-1, `src/server/infra/executor/curate-executor.ts` | [EPI-CLM-agent-native](#epi-clm-agent-native) | none | Reshaping, derivation and conjecture unresolved without concrete input/output |
| [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | operational admission/selection/consumption | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Relevance and deliverability | see [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | see [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | see [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | Ranking/filtering | Similarity licenses selection, not truth | Chooses what caller can use | see [RT-BAP-topic-guidance](runtime.md#rt-bap-topic-guidance) | SRC-1, `src/server/infra/executor/query-executor.ts` | [EPI-CLM-query-answer](#epi-clm-query-answer) | Query answer label exceeds target synthesis on this route | No recall or actual reliance evidence |
| [EPI-RTE-render-content](#epi-rte-render-content) | content transformation | implemented | [EPI-OBJ-topic-statements](#epi-obj-topic-statements) | truth-apt transformation: non-ampliative reshaping | HTML assertions to text | Deterministic rendering; selected typed elements | During query/read | Selected text survives; href may not | Advisory delivery | Proposition text can survive while evidence lineage degrades | Caller receives incomplete source representation | Rendered markdown → caller, advisory, invocation | SRC-1, `src/server/infra/render/reader/html-renderer.ts` | [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | none | Not lossless or a truth check |
| [EPI-RTE-read-topic](#epi-rte-read-topic) | operational admission/selection/consumption | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Explicit requested path | Path checks and readable file, not relevance scoring | Each read request | Raw or rendered content/error | Permissive delivery | Raw bytes preserve available source representation, not source truth | Supports inspection before rewrite | CLI content → caller, advisory, invocation | SRC-1, `src/oclif/lib/read-topic.ts` | [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | none | No proof caller inspects evidence |
| [EPI-RTE-review-decision](#epi-rte-review-decision) | disposition/acceptance | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Pending operations by task/path | Requesting reviewer; no encoded factual criterion or oracle | Conditional post-write | Approved/rejected statuses | Enforcing status changes | Recorded choice, not established evidence-consuming factual acceptance | Approval keeps current state; rejection requests reversion | Request → handler/log → push filtering, enforcing, until later change | SRC-1, `src/server/infra/transport/handlers/review-handler.ts` | none | none | Human identity and evidence use not established |
| [EPI-RTE-review-decision](#epi-rte-review-decision) | lineage/freshness/recovery | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Rejected file change | Backup presence and I/O success | After reject request | Restore old bytes or unlink | Physical rollback, best effort extras | Withdrawal of current bytes is not refutation | Changes later available guidance | Backup → tree → later readers, enforcing file effect, persistent | SRC-1, `src/server/infra/transport/handlers/review-handler.ts` | none | none | Missing backup may delete; cache/index retraction not established |
| [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | operational admission/selection/consumption | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Pending/rejected push paths | see [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | see [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | see [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | Push exclusion policy | Approval status licenses export, not truth | Blocks selected legacy Cloud submissions | Handler → Cloud request, enforcing, push | SRC-1, `src/server/infra/transport/handlers/push-handler.ts` | [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | none | Does not gate local query or establish Git VC policy |
| [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit) | retention | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | truth-apt transformation: acquisition/import | Client-supplied replacement bytes | see [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit) | see [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit) | see [RT-RTE-direct-edit](runtime.md#rt-rte-direct-edit) | Direct persistent mutation | Source warrant unknown | Bypasses curate structural/review gateway | Client → file → readers, permissive, persistent | SRC-1, `src/server/infra/transport/handlers/context-tree-handler.ts` | none | none | Semantic content depends on request |
| [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | retention | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | truth-apt transformation: acquisition/import | Publisher bundle bytes | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | Persistent file admission | Source warrant unknown | Bundle becomes eligible knowledge | Publisher → installer → tree, permissive, persistent | SRC-1, `src/server/infra/hub/hub-install-service.ts` | none | none | Skill branch is policy admission, separately below |
| [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | behavior/policy adaptation | implemented | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | non-truth-apt policy/content update: install agent skill | External host instruction surface | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | see [RT-RTE-hub-install](runtime.md#rt-rte-hub-install) | Installation permissive; host force unresolved | No epistemic license from install | Makes skill available to host | Connector files → excluded host loader, permissive, installed lifetime | SRC-1, `src/server/infra/hub/hub-install-service.ts` | none | none | Not observed activation or self-improvement |
| [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | retention | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | truth-apt transformation: acquisition/import | Cloud snapshot | see [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | see [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | see [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | Local snapshot admission | Source warrant unknown | Replaces eligible local state after divergence guard | Cloud → pull → tree, permissive, snapshot lifetime | SRC-1, `src/server/infra/transport/handlers/pull-handler.ts` | [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | none | Remote correctness/access controls excluded |
| [EPI-RTE-prune-candidates](#epi-rte-prune-candidates) | check/evidence production | implemented | [EPI-OBJ-runtime-signals](#epi-obj-runtime-signals) | truth-apt transformation: entailed derivation | Low-importance/stale predicates | Arithmetic and symbolic tier rules | Scan | Predicate reason and age | Advisory candidate ranking | Entailed only relative to input fields and clock | Offers candidates, does not archive them | Scan envelope → caller, advisory, scan | SRC-1, `src/server/infra/dream/tool-mode/prune-candidates.ts` | none | none | Does not establish stale knowledge or semantic redundancy |
| [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance) | disposition/acceptance | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Caller archive list | see [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance) | see [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance) | see [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance) | Enforcing removal from active tree | Caller choice not factual refutation | Archives paths without proving survivor preserved facts | Caller → finalize → active tree, enforcing, until undo | SRC-1, `src/server/infra/dream/tool-mode/dream-session.ts` | none | none | Stateless session does not certify scan membership or semantic merge |
| [EPI-RTE-dream-undo](#epi-rte-dream-undo) | lineage/freshness/recovery | implemented | [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) | no content change | Last dream state | Log preconditions and saved data | Explicit undo | Restored files/signals or collected errors | Physical recovery | Restores prior state, not prior warrant | Can re-expose archived guidance and prune predicates | Log → files/signals → readers/scans, enforcing, persistent | SRC-1, `src/server/infra/dream/dream-undo.ts` | none | none | Not all historical operations reversible; errors can coexist with undone status |
| [RT-RTE-context-control](runtime.md#rt-rte-context-control) | content transformation | implemented | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | truth-apt transformation: indeterminate | Model summary replaces working history | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | see [RT-RTE-context-control](runtime.md#rt-rte-context-control) | Changes subsequent model input | Summary fidelity unchecked here | Continues with reduced input | Summary boundary → next model call, permissive, task | SRC-1, `src/agent/infra/llm/agent-llm-service.ts` | none | none | Deterministic checkpoint branch differs; no factual acceptance implied |
| [EPI-RTE-hook-instructions](#epi-rte-hook-instructions) | operational admission/selection/consumption | implemented | Static workflow text, not acquired experience | non-truth-apt policy/content update: supply workflow instructions | Host pre-prompt context | Template loader; host activation excluded | Hook invocation | Workflow text or silent production failure | Advisory request; host placement unresolved | No factual warrant | Requests query-before-work and curate-after-work | Stdout → host context → caller, advisory here, prompt | SRC-1, `src/oclif/commands/hook-prompt-submit.ts` | none | none | “MANDATORY” is not local enforcement |

No accepted-claim lifecycle-integration route is established by the writer, review handler or dream paths inspected here. This is a bounded conclusion about those mechanisms, not a system-complete absence record: uninspected tool workers and excluded caller judgment prevent that wider negative. Topic links and synthesis can change organization before any factual acceptance is evidenced.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | see [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) | SRC-1, `README.md`, doctrine/design | see claim | [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission), [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) | None supplied | No demonstrated improvement or teammate consumption | Persistent availability and local delivery are wired | Knowledge label does not establish acceptance or factual warrant |
| [EPI-CLM-agent-native](#epi-clm-agent-native) | see [EPI-CLM-agent-native](#epi-clm-agent-native) | SRC-1, `paper/README.md`, doctrine/design | see claim | [RT-RTE-agent-curation](runtime.md#rt-rte-agent-curation), [RT-RTE-curate-session](runtime.md#rt-rte-curate-session), [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | None supplied | No author/consumer traces | Internal model route exists; public tool mode delegates authorship and synthesis | LLM retrieval is not the current deterministic public query path; zero-infrastructure wording is not a provider-independence proof |
| [EPI-CLM-query-answer](#epi-clm-query-answer) | see [EPI-CLM-query-answer](#epi-clm-query-answer) | SRC-1, `src/oclif/commands/search.ts`, doctrine/design | see claim | [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | None supplied | No host synthesis trace | Query supplies context from which caller may synthesize | Description overstates target-side synthesis on tool-mode route |
| [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | see [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) | SRC-1, `paper/README.md`; `paper/main.tex`, reported operation/design | see claim | No implemented benchmark acceptance consumer traced; public retrieval is [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) | None supplied; scores are attributed reporting | Full-versus-no-tier contrast also removes separate justifier; curated tree fixed; write-path components explicitly not ablated; mixed published comparisons use different models/judges | Reported answer-scoring protocol names domain, reference and evaluator | Does not warrant all retained statements, present-route accuracy, mechanism transfer or isolated write-path effect |

## Bounded conclusion

ByteRover has implemented routes for acquiring candidate statements from callers and publishers, retaining them, selecting them for later use, and requesting behavior through retained rules and static host instructions. Source warrant of imports is unknown, not conferred by storage. The relevant paths are [RT-RTE-curate-session](runtime.md#rt-rte-curate-session), [RT-RTE-hub-install](runtime.md#rt-rte-hub-install), [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync) and [RT-BAP-topic-guidance](runtime.md#rt-bap-topic-guidance). Direct edits independently admit content. The boundary does not establish actual later compliance or benefit.

Structural checking is consequential but narrowly licensed. [EPI-RTE-fact-validation](#epi-rte-fact-validation) checks attributes and topic structure for writer admission; it does not test the statement against project evidence. [EPI-RTE-review-decision](#epi-rte-review-decision) records a reviewer-supplied choice and can revert bytes. Neither branch requires a named factual criterion, intended factual use and scope, or records the evidence consumed. Pending content is already eligible locally; legacy push filtering confers operational export authority only. Therefore these statuses do not establish accepted ampliative knowledge or post-acceptance lifecycle integration.

The deterministic renderer demonstrably reshapes rather than verifies content; [EPI-RTE-render-content](#epi-rte-render-content) shows one preserved assertion with a lost source URL. [EPI-RTE-read-topic](#epi-rte-read-topic) supplies a raw alternative, so loss is route-specific. [EPI-RTE-prune-candidates](#epi-rte-prune-candidates) derives valid conditional arithmetic results from supplied state, not the truth or obsolescence of topic contents. No warranted source premises for broader project claims are supplied. Maturity, similarity and freshness must not be substituted for endorsement.

The internal model can author topics and compact task history, but accessible evidence does not individuate a produced claim and its premises well enough to decide reshaping, entailment or non-entailment; both generated-topic and summary relations remain indeterminate. The configured generator's parameter changes, exact version and endpoint behavior remain as bounded in [RT-CMP-content-generator](runtime.md#rt-cmp-content-generator). This does not negate nonparametric retention. Dream maintenance offers structural candidates and caller-controlled removal, while [EPI-RTE-dream-undo](#epi-rte-dream-undo) restores selected prior state without revalidating truth.

The benchmark evaluator has a named answer/reference domain, but its labels score answers, not each retained claim or its causal explanation. [EPI-CLM-benchmark-results](#epi-clm-benchmark-results) supports attributed outcomes and bounded comparison designs, not independently observed effectiveness of the frozen tool-mode route. No general learning, reflection, autonomous-theory-builder or self-improvement verdict follows: guidance delivery does not establish semantic criticism, iterative retention of criticism, or exercised evidence-responsive improvement. These are separate unestablished properties, not one inferred failure. Uninspected workers and excluded agents leave additional routes unresolved.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-topic-statements
Label: Topic statements

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

Source-native identity: textual statements in `bv-fact` and descriptive topic bodies; natural-language representational form, local HTML-file substrate. This is the semantic part of the supplied mixed container, not a replacement for it. Scope and truth depend on authored content; no particular persisted candidate instance was supplied. SRC-1 implementation/design, `src/server/infra/render/elements/bv-fact/schema.ts`:

> The element's text content is the canonical statement; attributes are
>  * the structured extraction.
> --- `src/server/infra/render/elements/bv-fact/schema.ts`

#### EPI-OBJ-topic-rules
Label: Topic rules

Part of: [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree)

Source-native identity: `bv-rule` bodies and their severity/ID signals, persisted in topic HTML. Natural-language normative consumption is distinct from the symbolic rendering of attributes and from descriptive statements. Storage substrate: local files; later reader receives advisory text. SRC-1 implementation, `src/server/infra/render/reader/html-renderer.ts`; minimum rendering passage and actual authority boundary: see [RT-BAP-topic-guidance](runtime.md#rt-bap-topic-guidance) and [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval). The normative part differs from the statement part by its consumer function; neither a severity string nor a “Rule” label implements host enforcement.

#### EPI-OBJ-runtime-signals
Label: Runtime signals

Source-native identity: `RuntimeSignals` sidecar fields, symbolic numerical/tier state stored per machine rather than shared topic bodies. Distinct from [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree); overlaps [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance) as its input, not its route identity. SRC-1 implementation, `src/server/core/domain/knowledge/runtime-signals-schema.ts`:

> export const MaturityTierSchema = z.enum(['core', 'draft', 'validated'])
> --- `src/server/core/domain/knowledge/runtime-signals-schema.ts`

> export const DEFAULT_IMPORTANCE = 50
> export const DEFAULT_RECENCY = 1
> export const DEFAULT_MATURITY = 'draft' as const
> export const DEFAULT_ACCESS_COUNT = 0
> export const DEFAULT_UPDATE_COUNT = 0
> --- `src/server/core/domain/knowledge/runtime-signals-schema.ts`

The checked schema constrains values, not their semantic warrant. The prune consumer below uses maturity as policy input; this source alone establishes no factual evaluation behind `validated`.

### Routes

#### EPI-RTE-fact-validation
Label: Fact attribute validation

Part of: [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission)

Endpoints/progression: writer `validateHtmlTopic` walks parsed elements, calls the fact validator through the element registry, receives Zod attribute results, then returns errors or a valid topic to writer disposition. Owner: deterministic writer/validator. Context/state: submitted markup; no project evidence enters the fact attribute evaluator. This check is a material subroute, not a duplicate admission mechanism.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Attribute-validation errors or syntactic success.
- Later read-back: inapplicable — this pure check retains no result by itself; enclosing writer determines topic persistence.
- Delegated visibility: Caller can receive structured errors through the enclosing admission path.
- Selection predicate: Registered `bv-*` elements select corresponding attribute validators; exactly one topic and a safe nonempty path are also required.
- Invalidation or expiry: inapplicable — each call reevaluates current submitted markup.
- Activation or effect: Errors block this writer's write; success permits the remaining overwrite/write checks.
- Evidence limits: Supports structure/attribute correctness only; no semantic truth test or execution observed.

The proposer is the caller or internal model, the program can veto schema failure, and human contribution is unresolved. This is open-request admission, with schema as reference criterion, not an expected factual-answer oracle. Correction prompts can shape resubmission; enclosing route owns retries and recovery. SRC-1 implementation, `src/server/infra/render/writer/html-writer.ts`, `src/server/infra/render/elements/bv-fact/validator.ts`, `src/server/infra/render/elements/bv-fact/schema.ts`, `src/server/infra/render/elements/make-validator.ts`:

> export const validateBvFact = makeAttributeValidator('bv-fact', BvFactAttributesSchema)
> --- `src/server/infra/render/elements/bv-fact/validator.ts`

> const parsed = schema.safeParse(node.attributes)
> --- `src/server/infra/render/elements/make-validator.ts`

> const result = ELEMENT_REGISTRY[el.tagName].validator(el)
> --- `src/server/infra/render/writer/html-writer.ts`

Because the checked fact schema uses optional strings/category enumeration and the generic validator parses attributes, changing a fact body's factual assertion alone does not cause this fact evaluator to test the new assertion's truth. This deduction is narrower than a claim about all tools or external reviewers.

#### EPI-RTE-render-content
Label: Render topic content

Part of: [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval)

Endpoints/progression: raw topic → `parseHtml` normalized tree → selected topic children → semantic-prefix renderer → caller-facing markdown. Owner: renderer code. The same implementation is reused by the independent single-topic read route below. This is a transformation part of the supplied query route, not a new retrieval selector.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Markdown-like text, including selected header attributes, typed labels and collapsed inner text.
- Later read-back: Rendered envelopes can be cached by the enclosing query route and delivered later; renderer itself does not persist.
- Delegated visibility: Text descendants and selected metadata survive; ordinary link hrefs and unrecognized non-bv top-level elements need not survive.
- Selection predicate: First `bv-topic`; element children; type-specific rendering and nonempty inner text.
- Invalidation or expiry: inapplicable — renderer is a pure current-input transformation; cache invalidation belongs to enclosing query.
- Activation or effect: Alters content available to caller interpretation, with no new truth test or mandatory compliance.
- Evidence limits: Deduction below is implementation evidence, not a target execution; raw reads provide a lossless-byte alternative.

SRC-1 implementation, `src/server/infra/render/reader/html-parser.ts`, `src/server/infra/render/reader/html-renderer.ts`:

> if (node.type === 'text') return node.text
>   if (node.type === 'element') {
>     if (node.tagName === 'img') return renderImgMarkdown(node.attributes)
>     return node.children.map((c) => getInlineMarkdownRaw(c)).join(' ')
>   }
> --- `src/server/infra/render/reader/html-renderer.ts`

Concrete input deduction, not execution: `<bv-topic path="config/timeout" title="Timeout"><bv-fact>Timeout is 30 s. <a href="evidence.txt">Source</a></bv-fact></bv-topic>` is parsed into the topic, fact, text and link nodes. Header extraction yields `# Timeout`; fact recursion joins its text descendants, yielding `Timeout is 30 s. Source`. The fact branch adds `- **Fact**: `, so the result is `# Timeout\n\n- **Fact**: Timeout is 30 s. Source` (escape sequences denote newlines). The proposition is reshaped non-ampliatively, but the evidence URL is discarded. Thus preserving a statement's words does not preserve its available source linkage or warrant. This deduction assumes the imported parser contract used by the inspected wrapper, not a verified dependency implementation.

#### EPI-RTE-read-topic
Label: Read topic path

Endpoints/progression: CLI `read` → `readTopic` → checked project-local path → UTF-8 file → raw or rendered result. Owner: helper and invoking caller. Distinct from [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval): explicit path selection, no query ranking/cache, optional raw bytes. It reuses [EPI-RTE-render-content](#epi-rte-render-content) only in its default HTML branch.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Content/path/format or unsafe-path, not-found or read-failed error.
- Later read-back: Previously retained topic reaches a later read invocation; raw mode preserves available source bytes.
- Delegated visibility: Entire UTF-8 source string with raw flag; otherwise HTML renderer output or unchanged non-HTML text.
- Selection predicate: Caller-chosen relative path; lexical/resolved-root safety and file readability, not relevance or truth.
- Invalidation or expiry: Each read opens current file; no helper cache. File replacement/deletion changes subsequent results.
- Activation or effect: Supplies existing content for inspection or merge authorship; actual interpretation unobserved.
- Evidence limits: No target execution; lexical checks are not a proved physical symlink-containment guarantee.

Selection is an open caller request, code can veto unsafe/unreadable paths, human identity unresolved, no factual answer oracle. SRC-1 implementation, `src/oclif/commands/read.ts`, `src/oclif/lib/read-topic.ts`:

> const format = relPath.toLowerCase().endsWith('.html') ? 'html' : 'markdown'
>   const content = format === 'html' && !options.raw ? renderHtmlTopicForLlm(raw) : raw
> --- `src/oclif/lib/read-topic.ts`

#### EPI-RTE-review-decision
Label: Review task decision

Endpoints/progression: `ReviewEvents.DECIDE_TASK` request → pending operations grouped by task/file → optional file filter → reject restores/unlinks, approve leaves current bytes → successful operations' log status changes → backup deletion/notification. Owner: requesting reviewer for choice; handler for effects. Distinct endpoint and consumer chain spanning the post-write review support in [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) and export selection in [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync); not a duplicate writer admission.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Processed paths, reverted flags and operation count.
- Later read-back: Updated log statuses can affect export selection; restored/deleted topic bytes affect later reads subject to other freshness mechanisms.
- Delegated visibility: Pending/list endpoints expose operation metadata; decision request carries choice, task ID and optional paths, not a factual proof.
- Selection predicate: Matching task ID, pending status, project-relative file path and optional caller file filter.
- Invalidation or expiry: Decision clears applicable backups; failed file processing remains pending. Later changes can replace topic bytes and statuses.
- Activation or effect: Reject changes filesystem content; approval/rejection changes processed operation statuses; notification best effort.
- Evidence limits: No encoded evidence-consuming factual criterion; reviewer human identity and evidence use unresolved; rejection does not demonstrate instantaneous cache/index retraction.

The requesting principal proposes the decision; software selects applicable pending operations and I/O failure can prevent completion. Operating mode is requested review, not an experiment. No expected-answer oracle is implemented. Optional review metadata shaped which changes were offered, not a mandatory semantic trial. Rollback depends on backups and is not guaranteed for every admission path. SRC-1 implementation, `src/server/infra/transport/handlers/review-handler.ts`; supplied backup failure and pending-selection passages: [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission).

> if (decision === 'rejected') {
>           const absolutePath = join(contextTreeDir, relPath)
>           const backupContent = await backupStore.read(relPath)
> --- `src/server/infra/transport/handlers/review-handler.ts`

> batch.push({operationIndex, reviewStatus: decision})
> --- `src/server/infra/transport/handlers/review-handler.ts`

Approval records a choice but cannot on these fields establish acceptance against a named factual criterion for an intended scope. Conversely, rejection has real physical force; it is not merely a cosmetic label. The export consumer's separate scope is retained in [RT-RTE-cloud-sync](runtime.md#rt-rte-cloud-sync).

#### EPI-RTE-prune-candidates
Label: Prune candidate predicates

Part of: [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance)

Endpoints/progression: loaded topic mtimes and sidecar signals → scope/core filtering → age and importance predicates → reason labels → oldest-first limit → scan envelope. Owner: deterministic candidate generator; caller owns archive/keep/merge judgment. This is a check subroute, not the encompassing semantic maintenance workflow. SRC-1 implementation, `src/server/infra/dream/tool-mode/prune-candidates.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate HTML/path/signals plus computed age and low-importance/stale/both reason.
- Later read-back: inapplicable — generator retains no candidate decisions; later scans recompute from persisted files/signals.
- Delegated visibility: Caller receives original topic HTML and signals alongside reasons, not a factual obsolescence verdict.
- Selection predicate: Optional prefix; exclude core; importance below 35 or draft age at least 60 days/validated age at least 120; sort by age and limit by default 20.
- Invalidation or expiry: Changed signals, mtime, clock or scope change next result; no candidate lifetime certificate.
- Activation or effect: Advisory candidate selection only; enclosing finalize requires caller archive request.
- Evidence limits: Correctness is conditional on supplied clock/mtime/signals; no semantic freshness or actual maintenance benefit established.

> const daysSinceModified = Math.max(0, (now - t.mtimeMs) / DAY_MS)
>     const lowImportance = t.signals.importance < importanceThreshold
>     const staleMtime = isStaleForMaturity(t.signals.maturity, daysSinceModified, draftDays, validatedDays)
> --- `src/server/infra/dream/tool-mode/prune-candidates.ts`

> case 'draft': {
>       return daysSinceModified >= draftDays
>     }
> --- `src/server/infra/dream/tool-mode/prune-candidates.ts`

Concrete deduction: a non-core draft topic with importance 50 and mtime exactly 60 days before the supplied clock is selected as `stale-mtime` under defaults, even if its project assertion remains true. The implementation's boundary is inclusive (`>=`), whereas the dream skill abbreviates it as `>60d`; implementation governs this calculation. The entailed proposition is about fields and clock, not whether content is outdated. Code proposes, caller decides and can ignore the candidate; no human step or factual oracle is required. Scan is open requested maintenance; thresholds guide selection, not content acceptance. The merge generator separately delegates to BM25 pair discovery with threshold 0.85 (`src/server/infra/dream/tool-mode/merge-candidates.ts`); that parameter does not license semantic equivalence.

#### EPI-RTE-dream-undo
Label: Dream undo recovery

Endpoints/progression: explicit CLI undo → last dream ID and log preconditions → reverse logged operations → restore/delete and signal/mtime recovery → review cleanup → manifest rebuild → log `undone` and dream-state rewind. Owner: CLI helper. Distinct recovery route, not the archive endpoint in [RT-RTE-dream-maintenance](runtime.md#rt-rte-dream-maintenance); restores the state that can feed its next scan.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Restored/deleted/archive-restored paths and errors, or failed precondition.
- Later read-back: Restored topic bytes can reach reads; restored mtimes/signals can make a topic qualify again for pruning.
- Delegated visibility: Caller receives errors alongside successes; no evidence of a factual reacceptance decision is returned.
- Selection predicate: Last logged dream, completed or partial, not already undone; reverse each logged operation.
- Invalidation or expiry: Only latest dream, not a history stack; operation data limits restoration; subsequent file changes are not compared against a content revision before restore.
- Activation or effect: Writes prior text, restores selected metadata, deletes created outputs; cleanup can alter review statuses. Marks undone even when collected per-operation errors remain.
- Evidence limits: Not transactional recovery. Legacy synthesis UPDATE explicitly lacks saved previous text; restoration of sidecar is best effort; no executed rollback supplied.

Caller requests rollback; log state and implementation can veto; there is no factual answer oracle or new semantic approval. Recovery guidance is fixed switch logic over saved operations, not model judgment. Phase-two independent curate writes are not part of this undo; CLI documentation states that boundary. SRC-1 implementation, `src/oclif/commands/dream/undo.ts`, `src/server/infra/dream/dream-undo.ts`:

> if (op.action === 'UPDATE') {
>     throw new Error(`Cannot undo SYNTHESIZE/UPDATE: previousTexts not captured for ${op.outputFile}`)
>   }
> --- `src/server/infra/dream/dream-undo.ts`

> await writeFile(fullPath, content, 'utf8')
>
>           // Restore original mtime so stale-mtime prune candidates
>           // re-qualify. `writeFile` stamps mtime=now; `utimes` overwrites.
>           const savedMtimeMs = op.previousMtimes?.[filePath]
> --- `src/server/infra/dream/dream-undo.ts`

#### EPI-RTE-hook-instructions
Label: Hook workflow instructions

Endpoints/progression: hidden pre-prompt command → template loader `brv-instructions` → stdout → excluded host's context placement. Owner: command for delivery, host for actual invocation/placement, calling agent for compliance. Distinct from retained-topic guidance [RT-BAP-topic-guidance](runtime.md#rt-bap-topic-guidance): static workflow instructions rather than retrieval of accumulated experience.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Template text on stdout; production load failures do not interrupt the agent.
- Later read-back: inapplicable — static shipped instructions are not accumulated-through-use read-back.
- Delegated visibility: Host receives workflow text asking query first, curate after code changes, and inspect curate logs.
- Selection predicate: Command invocation loads the named static section; external connector/host activation not established here.
- Invalidation or expiry: Instruction bytes follow installed package/template version; no content-derived policy update implemented by this command.
- Activation or effect: Supplies an advisory instruction channel; no local enforcement of the requested query/curate order.
- Evidence limits: No host execution trace, binding system-context placement or compliance observed; source comment describes host wrapping, not an inspected host implementation.

SRC-1 implementation, `src/oclif/commands/hook-prompt-submit.ts`:

> const instructions = await templateLoader.loadSection('brv-instructions')
>
>       // Output to stdout (agent wraps in system context)
>       this.log(instructions)
> --- `src/oclif/commands/hook-prompt-submit.ts`

SRC-1 doctrine/design, `src/server/templates/sections/brv-instructions.md`:

> Code task received → brv query FIRST → Work → brv curate → Done
> --- `src/server/templates/sections/brv-instructions.md`

### Claims

#### EPI-CLM-agent-native
Label: Agent native memory

Claimed operation: LLM curation, structuring and retrieval through a hierarchical context tree with zero external infrastructure. Distinct from the general persistent-memory purpose in [RT-CLM-project-memory](runtime.md#rt-clm-project-memory); this claim assigns the processing to the LLM. SRC-1 doctrine/design, `paper/README.md`:

> Research paper for [ByteRover](https://www.byterover.dev/) - an agent-native memory architecture where the LLM itself curates, structures, and retrieves knowledge through a hierarchical Context Tree, requiring zero external infrastructure.
> --- `paper/README.md`

Current public tool mode supplies a countercase: caller authoring plus deterministic retrieval. Internal model curation exists independently. Neither source route proves every instance of the broader architectural account or zero model-service dependence.

#### EPI-CLM-query-answer
Label: Query synthesized answer

Claimed operation: query provides a synthesized answer, contrasted with ranked search. No distinct supplied claim record; closest [RT-CLM-project-memory](runtime.md#rt-clm-project-memory) does not make this synthesis assignment. SRC-1 doctrine/design, `src/oclif/commands/search.ts`:

> Use this for structured results with file paths.
> Use "brv query" when you need a synthesized answer.
> --- `src/oclif/commands/search.ts`

The implemented tool-mode retrieval in [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) leaves synthesis to the caller. The description may describe the overall caller workflow but does not establish target-side answer generation on that route.

#### EPI-CLM-benchmark-results
Label: Benchmark answer accuracy

Claimed operation: production-codebase memory evaluation with reported LoCoMo 96.1% and LongMemEval-S 92.8% LLM-judge answer accuracy. Distinct evaluation claim from [RT-CLM-project-memory](runtime.md#rt-clm-project-memory); no supplied record declares its protocol. SRC-1 reported operation, `paper/README.md`:

> **LoCoMo** - 96.1% overall accuracy (1,982 questions, 272 docs).
>
> **LongMemEval-S** - 92.8% overall accuracy (500 questions, 23,867 docs).
>
> All metrics are LLM-as-Judge accuracy (%).
> --- `paper/README.md`

SRC-1 reported operation/design, `paper/main.tex`:

> where a judge model evaluates each generated answer against the ground truth
> and returns a binary correctness label.
> For our own evaluations, we use Gemini~3 Flash as the judge
> with a separate justifier model (Gemini~3.1 Pro) that synthesizes
> an answer from retrieved context before scoring.
> --- `paper/main.tex`

Target/domain: answers on the named conversational benchmarks. Reference: benchmark ground truth. Evaluator: stated Gemini judge, distinct justifier. Result consumer evidenced here is reported comparative scoring, not an implemented admission gate for stored topics or a live policy update. No supplied question-level run artifact establishes those judgments actually occurred under the frozen tool-mode implementation.

The paper reports selective query-time ablations, a stronger design claim than an uncontrolled comparison but not registered causal-experiment evidence. Its tier-removal contrast changes both retrieval routing and the separate justifier, so attribution is no finer than that treatment bundle. Other LongMemEval published comparisons use differing backbone/judge configurations. The write-path limitation is explicit:

> Since the curated \contexttree{} is held constant across all ablation conditions,
> their contribution cannot be isolated through query-time ablation on a static benchmark.
> --- `paper/main.tex`

> All queries are routed to the full agentic loop (Tier~4),
> bypassing Tiers~0--3 and the separate justifier model
> --- `paper/main.tex`

Thus attributed answer accuracy does not independently establish factual reliability of each retained claim, replay safety, a causal curation/lifecycle improvement, or current-route transfer.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
