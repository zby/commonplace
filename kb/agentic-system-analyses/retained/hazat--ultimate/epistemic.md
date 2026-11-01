---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Ultimate epistemic routes: project-memory warrant, relevance selection, content review and operational change authority."
run-id: AAS-2026-11-01-ultimate-f5179584de71-01
reviewed-boundary: "e2b9fa61962f6aecd394dea1c670688fac3ec432"
---

# Ultimate epistemic report

## Source-and-claim boundary

The question is how Ultimate's project facts, lessons, summaries and assessments become consequential guidance, and which checks license truth rather than operational continuation. The whole-system functional scope, external dependency exclusions and frozen SRC-1 identity are those of [the boundary and Source register](boundary.md#source-register). This report directly inspects additional paths within that source; it does not add sources or execution evidence. Implementation establishes available routes, not operation, model compliance or benefit. No target execution was performed.

The supplied runtime is provisional, not an inspection limit. Its local-control qualifications survive the inspected countercases: automatic landing memorization can write without a user choosing each memory; explicit remember's standing-agent check is not a restriction on internal extension APIs; hands-off goals replace normal user-choice policy; codemode bypasses nested hooks. A single truth gate or per-content human approval claim would therefore be false. No supplied fact requires supersession: new declarations below identify material parts or distinct routes, not replacement identities.

| Entry point or operation | SRC-1 source path | Coverage and basis |
|---|---|---|
| CLI/server/browser admission, durable conversation | `bin/ultimate.ts`, `server/api.ts`, `server/harness.ts` | Supplied [RT-RTE-browser-input](runtime.md#rt-rte-browser-input); this member does not independently inspect every dispatch branch. Structural admission is not truth checking. |
| Root branch and named children | `extensions/lineage/server.ts`, `extensions/subagents/server.ts` | Direct memory-tool/reaction slices plus supplied [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch), [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start). |
| Explicit remember, memory read, internal remember API, landing event reaction | `extensions/lineage/server.ts`, `extensions/lineage/memory.ts` | Direct reads; [EPI-RTE-memory-checks](#epi-rte-memory-checks), [EPI-RTE-memory-retention](#epi-rte-memory-retention), [EPI-RTE-memory-consumption](#epi-rte-memory-consumption), [EPI-RTE-landing-candidates](#epi-rte-landing-candidates). |
| Landing normalization, parse/refusal/retry/deletion | `extensions/lineage/memory.ts` | Direct complete file; [EPI-RTE-memory-normalization](#epi-rte-memory-normalization), [EPI-RTE-memory-checks](#epi-rte-memory-checks). |
| Recall hook and classifier endpoint | `extensions/recall/server.ts`, `extensions/classify/server.ts`, `extensions/recall/README.md` | Direct complete files; [EPI-RTE-recall-selection](#epi-rte-recall-selection), [EPI-RTE-recall-injection](#epi-rte-recall-injection). |
| Review/onboarding/dream procedure | `agents/ultimate.md`, `extensions/lineage/README.md`, `extensions/dream/DREAM.md` | Direct agent/dream instructions and bounded memory-review documentation; [EPI-RTE-memory-review](#epi-rte-memory-review). Generic executable tools afford enactment, not reliable semantic review. |
| Seed/cross-chapter carry and user-only transition | `extensions/dream/seed.ts`, `extensions/dream/server.ts` | Direct buildSeed/applySeed slices; supplied transition account [RT-BAP-extension-code](runtime.md#rt-bap-extension-code); [EPI-RTE-chapter-carry](#epi-rte-chapter-carry). |
| Web search/fetch and local shape validation | `extensions/parallel/server.ts` | Direct tool executors and validateResponse; [EPI-RTE-web-acquisition](#epi-rte-web-acquisition). Remote extractor and truncation helper internals uninspected: full fidelity not established. |
| Hands-off criteria and decision authority | `extensions/goal/server.ts`, `agents/ultimate.md` | Direct act/end/note and agent instructions; [EPI-RTE-goal-authority](#epi-rte-goal-authority). |
| Human code-review steering | `extensions/review/server.ts` | Direct send action: validated review text is submitted with whenBusy steer, not a semantic verdict gate; covered as imported caller input by [RT-RTE-browser-input](runtime.md#rt-rte-browser-input), a distinct entry surface, not HTTP enforcement. Review validation helper uninspected prevents assessing its full contract. |
| Phase classifier | `extensions/phase/server.ts` | Direct classify task: current-run entries feed choice; current row/run plus confidence >= .6 or no prior phase admits label. Downstream phase consumers not traced; no claim that this evaluates correctness or changes work policy. |
| Automation and codemode dispatch | `extensions/automations/scheduler.ts`, `extensions/codemode/server.ts` | Supplied [RT-RTE-automation-run](runtime.md#rt-rte-automation-run), [RT-RTE-codemode-tools](runtime.md#rt-rte-codemode-tools). Script repair/supervisor evaluator details uninspected, preventing complete adaptation account. |
| Summary, sketch, compaction and side-chat returns | `extensions/conversations/summary.ts`, `extensions/sketch/server.ts`, `extensions/side-chat/server.ts` | Supplied [RT-RTE-auxiliary-model](runtime.md#rt-rte-auxiliary-model), [RT-RTE-context-return](runtime.md#rt-rte-context-return); truth/fidelity cannot follow from schema validity or nonempty output. |
| Workspace checks, swap, extension admission | `extensions/workspaces/lander.ts`, `server/extensions.ts`, `bin/ultimate.ts` | Supplied [RT-RTE-change-admission](runtime.md#rt-rte-change-admission), [RT-BAP-extension-code](runtime.md#rt-bap-extension-code). Checks cover configured outcomes and type/shape, not general semantic truth. |
| Other exposed operations and tests | `extensions/voice-live/server.ts`, `extensions/watchdog/server.ts`, `extensions/mcp/server.ts`, `test/recall.test.ts`, `skills/verify-ui/SKILL.md` | Tool/hook names searched; MCP uncertainty supplied by runtime. Voice transformations, watchdog diagnosis/retry, full UI evaluation procedures and test bodies not independently traced here. These available but unassessed routes prevent a system-complete negative about evaluation or adaptation. |

Missing execution traces prevent identifying actual memory candidate states, actual evidence-consuming acceptances, compliant criticism, activation or successful change. Missing provider implementation prevents inferring internal learning or theorem-like entailment. No comparative experiment is supplied: claimed precision/recall is reported operation, not independently inspected evaluation data or a component-effect estimate. The initial source register does not supply an observed-run layer for it.

Consequential claims examined: [RT-CLM-coding-work](runtime.md#rt-clm-coding-work), [EPI-CLM-project-memory](#epi-clm-project-memory), [EPI-CLM-recall-tuning](#epi-clm-recall-tuning), [EPI-CLM-dream-learning](#epi-clm-dream-learning). This is not a claim to enumerate every public assertion in the repository.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc) | User/model/tool assertions and symbolic execution state, split by content | see record | SRC-1, see record | No supplied run identifies actual propositions. |
| [EPI-OBJ-memory](#epi-obj-memory) | Facts about project, lessons, reasons for decisions; policy parts need not be truth-apt | Project memory | SRC-1 `extensions/lineage/memory.ts` | Kind label does not prove truth; no actual memory corpus. |
| [EPI-OBJ-memory-ops](#epi-obj-memory-ops) | Proposed bodies/lines plus symbolic add/update/delete operations | Update candidates | SRC-1 `extensions/lineage/memory.ts` | Model semantic relation cannot be fixed from prompt alone. |
| [EPI-OBJ-web-results](#epi-obj-web-results) | Imported page propositions over remote page scope | External evidence candidates | SRC-1 `extensions/parallel/server.ts` | Excerpts/extraction are opaque and output bounded. |
| [EPI-OBJ-goal](#epi-obj-goal) | Criteria/met markers and reasons; mixed with non-truth-apt delegation policy | Goal decisions | SRC-1 `extensions/goal/server.ts` | Marker is not independently checked outcome. |
| [RT-OBJ-agent-instructions](runtime.md#rt-obj-agent-instructions) | Requested review criteria, process rules, self-change guidance | see record | SRC-1 `agents/ultimate.md`, `extensions/dream/DREAM.md` | Requested practice, not evidence it happened. |
| [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models) | Exact distributed representation not determinable | see record | SRC-1, see record; classifier separately scoped in [EPI-RTE-recall-selection](#epi-rte-recall-selection) | No accessible weight/provenance/parameter-update evidence. |
| [RT-RTE-auxiliary-model](runtime.md#rt-rte-auxiliary-model), [RT-RTE-context-return](runtime.md#rt-rte-context-return) | Summary assertions/render specs | see records | SRC-1, see records | Different parts/checks remain separate there; no output trace here. |

## Authority-route ledger

Each compact entry is an overlay. Fields owned by the declaring record say “see” rather than re-declaring it. Status here is architectural status, not the shared conclusion-status vocabulary. No observed candidate instance is supplied.

Route ID: [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-ops](#epi-obj-memory-ops)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Evaluator/condition and domain: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Activation and timing: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Possible or observed result: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Implemented force: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Epistemic authority and scope: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/memory.ts`
Claim IDs or none: [EPI-CLM-project-memory](#epi-clm-project-memory)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-landing-candidates](#epi-rte-landing-candidates)

Route ID: [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-ops](#epi-obj-memory-ops)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Evaluator/condition and domain: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Activation and timing: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Possible or observed result: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Implemented force: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Epistemic authority and scope: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/memory.ts`
Claim IDs or none: [EPI-CLM-project-memory](#epi-clm-project-memory)
Mismatch marker or none: Clipping is not proven semantic preservation.
Gap/limit: see [EPI-RTE-memory-normalization](#epi-rte-memory-normalization)

Route ID: [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-ops](#epi-obj-memory-ops)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Evaluator/condition and domain: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Activation and timing: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Possible or observed result: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Implemented force: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Epistemic authority and scope: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/memory.ts`
Claim IDs or none: [EPI-CLM-project-memory](#epi-clm-project-memory)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-memory-checks](#epi-rte-memory-checks)

Route ID: [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Evaluator/condition and domain: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Activation and timing: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Possible or observed result: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Implemented force: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Epistemic authority and scope: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/memory.ts`
Claim IDs or none: [EPI-CLM-project-memory](#epi-clm-project-memory)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-memory-retention](#epi-rte-memory-retention)

Route ID: [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Evaluator/condition and domain: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Activation and timing: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Possible or observed result: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Implemented force: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Epistemic authority and scope: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/memory.ts`
Claim IDs or none: [EPI-CLM-project-memory](#epi-clm-project-memory)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-memory-consumption](#epi-rte-memory-consumption)

Route ID: [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Evaluator/condition and domain: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Activation and timing: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Possible or observed result: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Implemented force: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Epistemic authority and scope: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Evidence source ID and local anchor: SRC-1 `extensions/recall/server.ts`
Claim IDs or none: [EPI-CLM-recall-tuning](#epi-clm-recall-tuning)
Mismatch marker or none: Relevance is not truth.
Gap/limit: see [EPI-RTE-recall-selection](#epi-rte-recall-selection)

Route ID: [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Evaluator/condition and domain: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Activation and timing: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Possible or observed result: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Implemented force: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Epistemic authority and scope: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)
Evidence source ID and local anchor: SRC-1 `extensions/recall/server.ts`
Claim IDs or none: [EPI-CLM-recall-tuning](#epi-clm-recall-tuning)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-recall-injection](#epi-rte-recall-injection)

Route ID: [EPI-RTE-memory-review](#epi-rte-memory-review)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Evaluator/condition and domain: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Activation and timing: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Possible or observed result: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Implemented force: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Epistemic authority and scope: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/README.md`
Claim IDs or none: [EPI-CLM-dream-learning](#epi-clm-dream-learning)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-memory-review](#epi-rte-memory-review)

Route ID: [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Evaluator/condition and domain: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Activation and timing: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Possible or observed result: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Implemented force: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Epistemic authority and scope: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)
Evidence source ID and local anchor: SRC-1 `extensions/dream/seed.ts`
Claim IDs or none: [EPI-CLM-dream-learning](#epi-clm-dream-learning)
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)

Route ID: [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-web-results](#epi-obj-web-results)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Evaluator/condition and domain: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Activation and timing: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Possible or observed result: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Implemented force: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Epistemic authority and scope: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)
Evidence source ID and local anchor: SRC-1 `extensions/parallel/server.ts`
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: see [EPI-RTE-web-acquisition](#epi-rte-web-acquisition)

Route ID: [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal](#epi-obj-goal)
Content/update relation: non-truth-apt policy/content update: goal delegation and status records
Transition or check target: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Evaluator/condition and domain: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Activation and timing: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Possible or observed result: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Implemented force: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Epistemic authority and scope: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)
Evidence source ID and local anchor: SRC-1 `extensions/goal/server.ts`
Claim IDs or none: none
Mismatch marker or none: Bookkeeping is not outcome verification.
Gap/limit: see [EPI-RTE-goal-authority](#epi-rte-goal-authority)

Route ID: [EPI-RTE-memory-review](#epi-rte-memory-review)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-memory-ops](#epi-obj-memory-ops)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Evaluator/condition and domain: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Activation and timing: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Possible or observed result: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Implemented force: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Epistemic authority and scope: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Operational authority: behavior permitted, blocked, or changed: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Behavioral-authority path: consumer, channel, force, horizon: see [EPI-RTE-memory-review](#epi-rte-memory-review)
Evidence source ID and local anchor: SRC-1 `extensions/lineage/README.md`
Claim IDs or none: [EPI-CLM-dream-learning](#epi-clm-dream-learning)
Mismatch marker or none: Enactment of an evidence-consuming acceptance is not supplied.
Gap/limit: Generic tools implement possible effects, not this semantic decision criterion.

Route ID: [RT-RTE-auxiliary-model](runtime.md#rt-rte-auxiliary-model), [RT-RTE-context-return](runtime.md#rt-rte-context-return)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see cited records
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see cited records
Evaluator/condition and domain: see cited records
Activation and timing: see cited records
Possible or observed result: see cited records
Implemented force: see cited records
Epistemic authority and scope: Summary and render validity do not independently establish factual fidelity; further scope see cited records.
Operational authority: behavior permitted, blocked, or changed: see cited records
Behavioral-authority path: consumer, channel, force, horizon: see cited records
Evidence source ID and local anchor: SRC-1, see cited records
Claim IDs or none: [RT-CLM-coding-work](runtime.md#rt-clm-coding-work)
Mismatch marker or none: Nonempty text/schema success is not truth checking.
Gap/limit: No supplied outputs distinguish copying, reshaping, derivation and conjecture.

Route ID: [RT-RTE-change-admission](runtime.md#rt-rte-change-admission)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: see cited record
Content/update relation: no content change
Transition or check target: Candidate merged commit versus configured check process success; supervisor candidate versus type checker; extension export versus shape.
Evaluator/condition and domain: see cited record
Activation and timing: see cited record
Possible or observed result: see cited record
Implemented force: see cited record
Epistemic authority and scope: At most the selected program/type/shape criteria in their checked domain, not overall correctness or safe deployment.
Operational authority: behavior permitted, blocked, or changed: see cited record
Behavioral-authority path: consumer, channel, force, horizon: see cited record
Evidence source ID and local anchor: SRC-1, see cited record
Claim IDs or none: [RT-CLM-coding-work](runtime.md#rt-clm-coding-work)
Mismatch marker or none: Configured checks may be empty; retry success is permitted.
Gap/limit: Test outcomes and causal component effects not supplied.

Route ID: [RT-RTE-change-admission](runtime.md#rt-rte-change-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: see cited record
Content/update relation: no content change
Transition or check target: Landing/swap/registry admission after path-specific results; these are product/capability decisions.
Evaluator/condition and domain: see cited record
Activation and timing: see cited record
Possible or observed result: see cited record
Implemented force: see cited record
Epistemic authority and scope: Operational acceptance against configured criteria; not acceptance of an ampliative factual explanation.
Operational authority: behavior permitted, blocked, or changed: see cited record
Behavioral-authority path: consumer, channel, force, horizon: see cited record
Evidence source ID and local anchor: SRC-1, see cited record
Claim IDs or none: [RT-CLM-coding-work](runtime.md#rt-clm-coding-work)
Mismatch marker or none: Direct shell/live load alternatives prevent a system-wide check gate.
Gap/limit: Rejection and recovery are path-local, not global rollback.

Lifecycle integration of accepted factual claims is not established by these inspected memory/recall/seed routes. They demonstrably retain/select/deliver candidates; adding an invented acceptance or integration row would conflate storage with warrant. Review doctrine describes a possible evidence-consuming decision, not an observed one.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-project-memory](#epi-clm-project-memory) | see record | SRC-1 `extensions/lineage/memory.ts`, doctrine/design | see record | [EPI-RTE-landing-candidates](#epi-rte-landing-candidates), [EPI-RTE-memory-retention](#epi-rte-memory-retention), [EPI-RTE-memory-consumption](#epi-rte-memory-consumption) | none supplied | No memory outcomes/comparison | Durable guidance plumbing and model request exist | “Fact/lesson” does not establish truth; clipping and incomplete citations limit warrant. |
| [EPI-CLM-recall-tuning](#epi-clm-recall-tuning) | see record | SRC-1 `extensions/recall/README.md`, doctrine/design with reported metrics | see record | [EPI-RTE-recall-selection](#epi-rte-recall-selection), [EPI-RTE-recall-injection](#epi-rte-recall-injection) | No underlying dataset/trace supplied | Reported threshold tuning, not independent component variation or truth assessment | Relevance selector and advisory delivery implemented | Metrics are scoped to labelled messages, not factual correctness or broad benefit. |
| [EPI-CLM-dream-learning](#epi-clm-dream-learning) | see record | SRC-1 `extensions/dream/DREAM.md`, doctrine/design | see record | [EPI-RTE-memory-review](#epi-rte-memory-review), [EPI-RTE-chapter-carry](#epi-rte-chapter-carry), [RT-RTE-change-admission](runtime.md#rt-rte-change-admission) | none supplied | No exercised update-to-later-behavior chain | Evidence-review/self-change procedure with executable means to carry/adopt changes | Neither successful learning nor exercised self-improvement follows. |
| [RT-CLM-coding-work](runtime.md#rt-clm-coding-work) | see record | SRC-1 `extensions/prompt/server.ts`, doctrine/design, supplied record | see record | [RT-RTE-browser-input](runtime.md#rt-rte-browser-input), [RT-RTE-change-admission](runtime.md#rt-rte-change-admission) | none supplied | Check success is not a complete product oracle | Available coding and bounded admission routes | Actual reliable verification unestablished. |

## Bounded conclusion

**Project memory can acquire operational authority without acquiring factual warrant.** [EPI-RTE-landing-candidates](#epi-rte-landing-candidates) produces candidates from a landing/abstract and existing memory; [EPI-RTE-memory-checks](#epi-rte-memory-checks) checks form, caller and applicability, while [EPI-RTE-memory-retention](#epi-rte-memory-retention) commits candidates for later use. There is no inspected evidence-consuming truth-acceptance criterion on those automatic or direct write paths. This is a path-specific finding, not a claim that Ultimate cannot check facts through ordinary work.

**Provenance and meaning are not preserved equally on every edge.** Web acquisition retains URL labels but relies on opaque extraction. Automated memory source replacement identifies the landing, not each original premise. Clipping can remove content; no checked entailment connects the resulting proposition to warranted premises. Briefs expose line/kind/date but not body/source. Recall exposes line/body but omits source/date. Full memory lookup can restore the stored breadcrumb. None of those metadata operations independently validates the claim ([EPI-RTE-web-acquisition](#epi-rte-web-acquisition), [EPI-RTE-memory-normalization](#epi-rte-memory-normalization), [EPI-RTE-memory-consumption](#epi-rte-memory-consumption), [EPI-RTE-recall-injection](#epi-rte-recall-injection)).

**Relevance and continuity have consequential but bounded force.** Recall probabilities rank estimated applicability, not truth, and advisory failure leaves work running. The current and later model receive selected text, not an enforcement result requiring obedience. Chapter carry selects one same-slug version by timestamp and brings it into a fresh chapter, without contradiction adjudication. Old chapters remain readable, but already-delivered false or obsolete content is not universally withdrawn by an update/delete ([EPI-RTE-recall-selection](#epi-rte-recall-selection), [EPI-RTE-recall-injection](#epi-rte-recall-injection), [EPI-RTE-chapter-carry](#epi-rte-chapter-carry)).

**There are distinct evaluators, not one oracle.** Memory schema/map checks evaluate structural applicability. Lander check commands evaluate configured executable outcomes for a candidate commit; type checker and module-shape checks cover narrower domains and consumers. Review/dream instructions ask model and user to judge evidence and usefulness for future project work, then adopt chosen operations; this semantic procedure is doctrine, not a supplied accepted-claim instance. Hands-off goals delegate those choices and record criteria/reasons; met markers are self-report rather than independent outcome measurement ([EPI-RTE-memory-review](#epi-rte-memory-review), [EPI-RTE-goal-authority](#epi-rte-goal-authority), [RT-RTE-change-admission](runtime.md#rt-rte-change-admission)).

**Self-directed change is a capacity, not an evidenced improvement result.** Dream explicitly represents Ultimate's failures/tools/methods and asks evidence-linked proposals. Those localized natural-language rules satisfy the formulation side of a theory account at least at whole-procedure granularity, but implemented requests do not establish model consumption, content-directed criticism or iterative use of criticism. Conditions 2–4 are unobserved in the supplied evidence; this does not establish their absence. [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) and [RT-BAP-extension-code](runtime.md#rt-bap-extension-code) supply live behavioral-authority channels for adopted instructions/code; [EPI-RTE-memory-review](#epi-rte-memory-review) supplies the requested criticism. Reflection is afforded by reading own-operation records and proposing changes, but both exercised causal directions are unestablished. Human proposal decisions are the normal protocol, with goal-mode computational substitution, so blanket autonomous-theory-building is not established. For improvement of project-specific future behavior across chapters/sessions, the first unclosed exercised self-improvement link is objective-bearing evidence actually shaping an update; no actual update, later activation or causal dependence is supplied either. Successful learning, exercised self-improvement and causal benefit remain separately unestablished, not a combined negative about adaptive capacity.

No checked entailed derivation or individuated non-entailed conjecture is established from candidate-free source text alone. The semantic relations of model summaries/lessons therefore remain indeterminate, rather than calling every output novel knowledge. Untested outcomes and unassessed operations named above prevent a system-complete verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memory
Label: Project memory
Part of: [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc)

Distinct material part of the supplied conversation/document-state container: root-scoped Memory map, not the generic AgentDoc configuration. It mixes natural-language line/body guidance with symbolic slug/kind/source/updated metadata. Durable conversation document substrate is active-chapter SQLite via Pi Durable; source declares history latest and fork initial. “fact” is a label, not an epistemic status. SRC-1 `extensions/lineage/memory.ts`; parts have different readers as [EPI-RTE-memory-consumption](#epi-rte-memory-consumption) and [EPI-RTE-recall-injection](#epi-rte-recall-injection) establish.

> /** A root's project memory. A fork starts empty: memories live on roots only. */
> --- `extensions/lineage/memory.ts`

#### EPI-OBJ-memory-ops
Label: Memory operations

Distinct candidate/update payload, not the stored map or generic conversation entries in [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc). Symbolic op/slug/field rules carry natural-language proposed bodies/lines; generated as summary-model text, parsed as JSON, memoized in durable task receipts/checkpoints before possible map mutation. SRC-1 `extensions/lineage/memory.ts`.

> {"op":"delete","slug":"existing-slug"}
> --- `extensions/lineage/memory.ts`

#### EPI-OBJ-web-results
Label: Parallel results

Distinct imported payload with no counterpart after comparison to [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc); eventual conversation entry is only a container. Natural-language excerpts/full_content plus symbolic URL/date/id/status fields, transient HTTP response/tool output and host details. Full remote page/source state is not captured. SRC-1 `extensions/parallel/server.ts`.

> const content = page.full_content || page.excerpts.join('\n\n')
> --- `extensions/parallel/server.ts`

#### EPI-OBJ-goal
Label: Goal ledger

Distinct goal-document part from the generic conversation/configuration state of [RT-OBJ-agent-doc](runtime.md#rt-obj-agent-doc); not a second declaration of its whole. Goals document stores natural-language criteria and decision reasons with symbolic status/tries/ending data, consumed as later goal note and report. Durable document substrate through harness; exact external persistence semantics remain contractual. SRC-1 `extensions/goal/server.ts`.

> goal.decisions.push(decision)
> --- `extensions/goal/server.ts`

### Routes

#### EPI-RTE-landing-candidates
Label: Landing memory candidates

A SubmissionLanded reaction schedules one memorization task per submission/root. The summary model receives the landing note, frozen or open submitter abstract and current full memories. It proposes add/update/delete operations; default is an empty batch. This is model synthesis, not checked entailment. A body could copy an imported fact, compress it, or infer a lesson; no supplied candidate/run lets those cases be individuated.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/lineage/memory.ts` (implementation). 

Check target / transition: Landing/abstract/current-memory → proposed operations; durable project guidance for future branches.
Evaluator and domain: Summary model interprets MEMORIZE_SYSTEM; this is generation, not an independent truth evaluator or reference-answer oracle.
Activation and timing: On new eligible landing events, from now; absent summary model ends without change.
Possible result: JSON text, empty ops, malformed or interrupted answer; provider failure writes nothing.
Implemented force: Candidate supply only; proposal is subject to separate format checks.
Epistemic authority and scope: No new factual warrant; input warrant unknown and semantic preservation unestablished.
Operational authority: Permits later software admission, not direct model compliance.
Behavioral-authority path: Memorize task, response receipt then parser; candidate channel, current task.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: JSON text, empty ops, malformed or interrupted answer; provider failure writes nothing.
- Later read-back: Memoized input/model/response retained for task resume; not yet project-memory read-back.
- Delegated visibility: Summary model gets selected landing, abstract and memories, not full original evidence.
- Selection predicate: Tree landing with a receipt not yet allocated; root itself is excluded.
- Invalidation or expiry: At most one repair request; refusal after retry or provider error leaves memory unchanged.
- Activation or effect: Proposed operations can reach the write path; no observed output.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> - Record only durable facts, decisions and lessons a future branch needs; never progress reports, changelogs or what a commit message already says.
> --- `extensions/lineage/memory.ts`

#### EPI-RTE-memory-normalization
Label: Automated memory normalization

Automated operations alone pass normalizeMemoryOp before parsing/admission. Slugs are kebab-cased; line whitespace collapses; overlong line/body are clipped with an ellipsis. A deterministic text operation need not preserve the claim. Deduction from inspected code: {op:'add',slug:'BAD SLUG',kind:'fact',line:'A\nB',body:' Keep this. '} becomes the same op with slug 'bad-slug', line 'A B', body 'Keep this.'. For a body exceeding 2000 characters the suffix is removed at a word boundary past the midpoint or a hard boundary and replaced with …; that can remove a necessary condition. No target execution was used.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/lineage/memory.ts` (implementation). 

Check target / transition: Proposed textual fields → bounded textual fields.
Evaluator and domain: Fixed regex, lengths and clip implementation; domain is formatting, not truth or contradiction.
Activation and timing: Only automated landing batch before applyMemoryOps; remember remains strict.
Possible result: Normalized or clipped strings; other fields left for parser.
Implemented force: Enforcing alteration before admission.
Epistemic authority and scope: No truth license; exact textual lineage can degrade under clipping.
Operational authority: Allows some otherwise over-limit batches to proceed.
Behavioral-authority path: applyMemoryOps, transformed operations, enforcing, current admission and subsequent memory lifetime.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Normalized or clipped strings; other fields left for parser.
- Later read-back: No separate retained original-to-normalized mapping in the memory item; task response receipt is separate.
- Delegated visibility: inapplicable — no delegation performed by normalization.
- Selection predicate: Every automated op object; only string fields are normalized.
- Invalidation or expiry: Output can later be updated/deleted; normalization has no semantic rollback.
- Activation or effect: Input strings change deterministically; semantic fidelity unestablished.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ...(typeof body === 'string' ? { body: clip(body.trim(), BODY_CHARS) } : {}),
> --- `extensions/lineage/memory.ts`

#### EPI-RTE-memory-checks
Label: Memory batch checks

Parser/check code assesses syntax, field types, slug uniqueness/existence, text lengths and final root capacity. Automatic inference also requires stopReason 'stop'; length or other stop reasons cause refusal and one retry with the reason. Direct remember checks caller against Standing. None of these checks consults cited conversation content, tests a factual claim or detects contradiction.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/lineage/memory.ts` (implementation). 

Check target / transition: Batch well-formedness and applicability to listed-root state; automatic response completion; caller identity on remember.
Evaluator and domain: Software parser, map simulation, constants and stop reason; domain is transactional/schema fitness. Summary model proposes; software can veto. No per-content human acceptance is required on automatic landings.
Activation and timing: Before writing anything; both remember and automated landing path, with normalization only on the latter.
Possible result: Parsed ops or error string; automated refusal can feed one repair.
Implemented force: Enforcing veto upstream of storage.
Epistemic authority and scope: Only structural admissibility, not evidence-consuming acceptance for truth.
Operational authority: Blocks invalid batches; retry permits generation of a repaired batch.
Behavioral-authority path: Memorize retry/disposition and remember executor; error/success channel; enforcing within batch.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Parsed ops or error string; automated refusal can feed one repair.
- Later read-back: Automatic response/error may persist in task checkpoint; no accepted factual assertion follows.
- Delegated visibility: Repair model sees previous answer and refusal reason.
- Selection predicate: All submitted ops and final simulated state.
- Invalidation or expiry: New attempt may pass; no staleness/contradiction invalidation of admitted content.
- Activation or effect: Checks gate memory writes, not provider-level truth.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const parsed = ops.map(parseOp)
> --- `extensions/lineage/memory.ts`

#### EPI-RTE-memory-retention
Label: Project memory mutation

After structural checks, applyMemoryOps changes the root Memory document atomically: add, overwrite selected fields or delete. It timestamps changed items. Automatic non-delete operations have their source overwritten with the landing's #from/at regardless of the model's proposed source. That is attribution to the landing, not proof that the landing warrants every body. Explicit remember can omit source; a source string is shape-checked, not dereferenced. This route retains candidates operationally, not epistemic lifecycle integration after an established acceptance decision.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/lineage/memory.ts` (implementation). 

Check target / transition: Checked operations → root memory map.
Evaluator and domain: Software commits the simulated map; foreground model proposes explicit remember, auxiliary model proposes automated ops. Standing identity gates only the tool, not internal LineageApi.remember or landing task.
Activation and timing: On successful applyMemoryOps inside caller transaction.
Possible result: Updated/deleted memory and short change summary; empty automatic batch yields no write.
Implemented force: Enforcing storage update.
Epistemic authority and scope: Retained as decision/fact/lesson labels; no independently established truth or justified acceptance.
Operational authority: Makes new guidance available to branches, memory tool, recall and chapter carry.
Behavioral-authority path: Memory document → later model contexts through separate read routes; storage then advisory language, future invocations.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Updated/deleted memory and short change summary; empty automatic batch yields no write.
- Later read-back: Root-scoped lineage.memory durable doc, history latest, fork initial; later consumers receive index/body as separately selected.
- Delegated visibility: Branches do not receive the whole memory map automatically; index or selected body is delivered.
- Selection predicate: Listed root and validated operation slug; automatic source replaced by landing location.
- Invalidation or expiry: Explicit update/delete, user forget or later automated delete; no mandatory validity expiry.
- Activation or effect: Operational memory can change without per-content human approval; live use unobserved.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> next.set(op.slug, { ...current, ...fields, updated: now })
> --- `extensions/lineage/memory.ts`

> ? { ...op, source: `#${from}/${at}` }
> --- `extensions/lineage/memory.ts`

The tool-only caller guard is SRC-1 `extensions/lineage/server.ts`; the same file also exposes an internal extension API without that tool identity check:

> remember: (root, ops, ctx, now) =>
>       host.harness().commit((tx) => applyMemoryOps(tx, root, ops, now), ctx),
> --- `extensions/lineage/server.ts`

Admission/recovery scope: a request or landing triggers the proposed content change; model instructions shape the proposal and software can reject malformed batches. The direct tool does not demand a human-approved content receipt. Whole-batch validation precedes writes, and automated refusal permits one repair; later update/delete can replace retained guidance but does not undo earlier model or host effects.

#### EPI-RTE-memory-consumption
Label: Memory brief and read

memoryIndex sorts slugs and presents kind, line and update date; memoryText adds optional source and body. memoryBrief supplies the index plus ten recent landings and history/full-memory pointers. The existing branch record supplies the reset consumer. The memory tool returns index or one exact requested slug. These are different visibility levels: a branch initially sees neither the full body nor the source field. Lookup can restore them; date and source are not endorsements.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/lineage/memory.ts` (implementation). 

Check target / transition: Retained memory → selected text for model context.
Evaluator and domain: Code formatting/root lookup/exact slug; model interprets relevance after delivery.
Activation and timing: Root branch with nonempty memory; explicit memory calls; brief also used around compaction.
Possible result: Index/brief/full selected body, missing-slug error.
Implemented force: Enforcing selection of visible content; advisory language at model consumer.
Epistemic authority and scope: Preserves displayed fields; omission of body/source in index restricts context, not a factual acceptance.
Operational authority: Supplies guidance the receiving model can use in work/decisions.
Behavioral-authority path: Branch reset and foreground/child tool results; natural-language context; advisory; later invocations while retained.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Index/brief/full selected body, missing-slug error.
- Later read-back: Reads retained map at later invocation; root tally remains separately searchable.
- Delegated visibility: Branch receives index and history pointer; exact tool call can fetch full body.
- Selection predicate: Requested root or resolved tree/only root; sorted index or Object.hasOwn exact slug.
- Invalidation or expiry: Updates/deletes change later reads; stale already-injected text is not retracted by this route.
- Activation or effect: Delivered content may shape decisions, but activation/compliance not observed.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> ...(item.source ? [`Source: ${item.source}`] : []),
> --- `extensions/lineage/memory.ts`

#### EPI-RTE-recall-selection
Label: Recall relevance selection

A beforeRequest hook asks external ClassifyApi which stored memory line is specifically triggered by the user's or branch's message (first 4000 text characters). The target is likely behavioral relevance to this situation, not the truth of the stored body. Classify requests jev-1.14.0 at a configured/default Typesafe endpoint; response shape checks do not validate probability calibration or source truth. The provider internals and weights are unavailable; no local weight-update path is inspected, exact remote weights are not pinned and configurable endpoint identity can vary.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/recall/server.ts` (implementation). Also SRC-1 `extensions/classify/server.ts` (implementation), `extensions/recall/README.md` (doctrine/design and reported metrics).

Check target / transition: Message intent and memory-line relevance, over available root memories plus none.
Evaluator and domain: External typed model judgment, choice probabilities; no expected factual answer oracle.
Activation and timing: Standing Ultimate only, once per eligible input, context at least 20% full and usage tokens/memories present; 3-second timeout.
Possible result: Probabilities or advisory failure; no relevance result on unsupported inputs.
Implemented force: Evidence for a downstream rank/threshold, not truth veto.
Epistemic authority and scope: At most estimated applicability; no warrant for the memory's proposition.
Operational authority: Controls which memories will be considered for injection.
Behavioral-authority path: Recall selector consumes probabilities; ranking; current input.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Probabilities or advisory failure; no relevance result on unsupported inputs.
- Later read-back: Last/pending state records progress; selected recall entry persists separately.
- Delegated visibility: Classifier sees sender/message prefix and all memory lines, not bodies or cited evidence.
- Selection predicate: User pi.user or branch board.message as latest input; classifier must be available.
- Invalidation or expiry: Failure/timeout leaves run unchanged; stopped run clears pending and propagates abort.
- Activation or effect: Potential selection input; no observed probability trace.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (answer.type === 'choice') probabilities = answer.probabilities
> --- `extensions/recall/server.ts`

#### EPI-RTE-recall-injection
Label: Recall delivery

Software chooses known slugs with p >= .25, excluding recalls within the last 30% of the context window, sorts descending and takes three. It appends each line and body as user-role text, both durably and to the current request. It omits memoryText's source field and updated date. Confidence is stored rounded in entry data, not offered as a truth probability in model text. Restart logic can reappend a placed recall to an older request cutoff.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/recall/server.ts` (implementation). Also SRC-1 `extensions/classify/server.ts` (implementation), `extensions/recall/README.md` (doctrine/design and reported metrics).

Check target / transition: Relevance probabilities and stored memories → foreground guidance.
Evaluator and domain: Fixed threshold/top-three/recent-context rule, followed by natural-language interpretation.
Activation and timing: After relevance call; empty picks produce no recall.
Possible result: recall.memories entry and request messages or unchanged request.
Implemented force: Ranking/enforcing delivery, advisory guidance to model.
Epistemic authority and scope: No epistemic acceptance; source warrant remains unknown and source breadcrumb is omitted from recalled text.
Operational authority: Requests action on each applicable memory and a one-line notice when it changes behavior.
Behavioral-authority path: Standing Ultimate through user-role request/conversation entry; advisory; current and later requests until context removal.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: recall.memories entry and request messages or unchanged request.
- Later read-back: Entry stored in conversation; later requests read it, restart cutoff can receive same message again.
- Delegated visibility: inapplicable — recall is injected into standing Ultimate, not a child.
- Selection predicate: Known slug, probability threshold, not recently recalled, descending top three.
- Invalidation or expiry: Compaction removes recalls from live view, allowing future recall; no automatic withdrawal of old false claims from past context.
- Activation or effect: Delivery wired; requested action and causal benefit unobserved.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> .filter(
>               ([slug, p]) => Object.hasOwn(memories, slug) && p >= THRESHOLD && !recent.has(slug),
>             )
> --- `extensions/recall/server.ts`

The delivered text selects line/body rather than the stored source field:

> ...picked.map(({ slug, item }) =>
>       [`${slug} [${item.kind}] — ${item.line}`, item.body].join('\n'),
>     ),
> --- `extensions/recall/server.ts`

#### EPI-RTE-memory-review
Label: Memory review and dream criticism

Memory review instructs a coordinator to fact-check against later decisions, code, history and conversations, return reasoned add/update/delete proposals and ask the user after Ultimate weighs in. Dream expands this into six passes, checks the handoff against transcripts and asks the coordinator to drop unsupported reports. Checking content and deciding which ops to adopt are distinct requested functions, not implemented semantic evaluators. Existing generic branch/message/tool paths afford enactment; no run trace establishes an actual evidence-consuming acceptance.

Closest supplied records: [RT-RTE-subagent-start](runtime.md#rt-rte-subagent-start). Distinct identity: requested semantic review/decision procedure, not generic child creation.
Source: SRC-1 `extensions/lineage/README.md` (doctrine/design). 

Check target / transition: Memory continued truth/relevance; dream proposals about failures, repeated work and future process changes.
Evaluator and domain: Requested model evidence review and user choice, except hands-off goals delegate choices to Ultimate. Intended criterion: durable useful guidance with supported evidence; scope: this project and future work, not general scientific truth.
Activation and timing: On requested review/dream; instructions require approved proposals before ordinary change branches/remember.
Possible result: Requested journal, evidence-linked criticisms, change set, user decisions; none supplied.
Implemented force: Natural-language protocol only, backed by generic branch and remember affordances.
Epistemic authority and scope: Could support bounded evidence-consuming acceptance if carried out; not established by procedure text.
Operational authority: Requests adoption/rejection, ordinary implementation branches and retirement of codified memories after landing.
Behavioral-authority path: Review/dream coordinator → Ultimate/user → remember or normal code branch; advisory/human decision; future project operation.
Owner and progression: Model/user under instructed procedure; generic tools afford later effects.
- Immediate return: Requested journal, evidence-linked criticisms, change set, user decisions; none supplied.
- Later read-back: Requested journal/change proposal and chosen memory or installed code; actual trace not supplied.
- Delegated visibility: Dream requests six dream-pass children with handoff, transcripts and evidence; actual launches unobserved.
- Selection predicate: Review request; dream memory/failure/tool/correction/codify/project passes; source-based criticism requested.
- Invalidation or expiry: Reject unsupported proposals; postpone memory retirement until code lands; user can skip proposals.
- Activation or effect: Criticism/revision/iteration are requested, not observed or software-enforced.
- Evidence limits: No observed run or causal experiment; semantic review/decision enactment unobserved.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> It fact-checks each memory: still true, outdated (with evidence), or contradicted by a later decision; and
> --- `extensions/lineage/README.md`

Theory account: the localized review/dream guidance states how to seek evidence, criticize memories and propose revised instructions or code. It requests retaining a journal, proposal reasons and chosen updates; ordinary memory or installed instructions/code would persist across later work. A proposal/journal itself is not proof of acceptance or use. Model and user contributions remain separate; ordinary review is open-ended project work, not a bounded experimental curriculum. The user normally decides and may skip; hands-off-goal instructions instead delegate proposal decisions to Ultimate. The chapter-switch action remains user-only.

Theory-builder conditions 1–4:
- condition 1 conclusion status: claimed
  The whole procedural unit is localized and inspectable; treating its prescriptive evidence rules as a methodological theory is a limited mapping, not a claim of a retained explanatory theory instance.
- condition 2 conclusion status: uninspected
  Instructions are deliverable through the supplied runtime, but no decision trace establishes dependence on what this procedure says.
- condition 3 conclusion status: claimed
  The procedure requests checking challenged memory content and placing blame using later decisions/evidence, then changing or rejecting it. No enacted criticism or changed reliance is supplied.
- condition 4 conclusion status: claimed
  Chosen memory/code revisions are intended to shape later work; no trace establishes criticism-fed iteration.

Addressability: whole files, named passes, memory slugs and operation fields are inspectable and separately revisable; no demonstrated theory-assumption decomposition is supplied. Persistence: requested journal and adopted memory/code can survive sessions/chapters; actual retention and consumption of a particular criticism are unobserved. Learning: improved future project capacity is intended, not demonstrated; no controlled outcome or component attribution is supplied. Reflection: own traces/failures/methods are the requested evidence and change targets, affording a feedback route without establishing both exercised causal directions. Reflective theory building is requested but not established as operated. Autonomous theory building is not established: human proposal decisions normally participate, and goal-mode substitution alone proves neither all internal operations nor compliance.

Self-improvement scope: project-specialized Ultimate's own behavior-determining instructions, tools and memory, across later project sessions/chapters; objective is fewer evidenced failures and less repeated manual work, not merely making a change. Dormant routes can install behavior-shaping outputs through the supplied runtime. Exercised attribution lacks link 1 (evidence actually shaping the chosen update), link 2 (an actual own-organization update), link 3 for that specific update (its live consumer), and link 4 (later operation causally depending on it). Static means and requests establish neither exercised membership nor successful improvement.

#### EPI-RTE-chapter-carry
Label: Chapter seed carry

buildSeed unions listed-root memories by slug, preferring the greater updated timestamp on collisions, with first encountered retained on equal timestamps. This is deterministic recency selection, not contradiction resolution. applySeed copies memories into the new chapter, delivers learned lines and handoff as chapter input and marks the seed applied. Old chapter remains reachable by chapter-qualified reads. User-only sleep/switch is established by runtime; seed construction does not establish that dream proposals were semantically accepted.

Closest supplied records: [RT-BAP-extension-code](runtime.md#rt-bap-extension-code). Distinct identity: data-seed construction/application, not the host facet/transition authority.
Source: SRC-1 `extensions/dream/seed.ts` (implementation). 

Check target / transition: Existing memory and prepared handoff → next-chapter context.
Evaluator and domain: Timestamp, about-slug-presence guard, receipt/compatibility checks; domain continuity, not truth.
Activation and timing: Prepared user chapter transition, then applySeed on next chapter open.
Possible result: seed.json, copied memories, chapter input and carry/recreate work items.
Implemented force: Enforcing recency selection/copy and input delivery.
Epistemic authority and scope: Preserves selected memory fields, not all competing versions; no new factual warrant.
Operational authority: New Ultimate can continue work from carried memory and handoff rather than replaying old context.
Behavioral-authority path: New chapter Memory doc and standing Ultimate input; stored then advisory text; cross-chapter invocations.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: seed.json, copied memories, chapter input and carry/recreate work items.
- Later read-back: Seed and new chapter docs retain selected content; old chapter accessible separately.
- Delegated visibility: New standing agent receives handoff/learned text and memory through ordinary routes, not every prior transcript.
- Selection predicate: Listed roots; latest timestamp per slug, open todos/questions and eligible automations.
- Invalidation or expiry: Applied receipt prevents repeated initial seed; incompatible old seed is refused with switch-back notice.
- Activation or effect: Continuation route wired; faithful handoff and actual use unobserved.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (!memories[slug] || memory.updated > memories[slug].updated) memories[slug] = memory
> --- `extensions/dream/seed.ts`

#### EPI-RTE-web-acquisition
Label: Web acquisition

web_search and web_fetch call Parallel Search/Extract with an objective and 40000-character aggregate request limit. Response shape is checked, then URLs/titles/dates and excerpts or full_content are formatted and tool output truncated. Details can retain a bounded per-page content slice. This imports externally extracted content; target does not create source warrant by labeling transport success. Local URL breadcrumbs survive formatting, but original-page fidelity and completeness remain unknown.

Closest supplied records: [RT-RTE-browser-input](runtime.md#rt-rte-browser-input). Distinct identity: external retrieval adapter, not user HTTP input admission.
Source: SRC-1 `extensions/parallel/server.ts` (implementation). 

Check target / transition: Public page/search content → model-visible tool result.
Evaluator and domain: Remote retrieval/extraction opaque; local validateResponse tests types/arrays, not factual correctness.
Activation and timing: Model requests tool and usable secret/extension present.
Possible result: Ranked pages/content, partial extraction/errors or failure output.
Implemented force: Enforcing output selection/format limits; advisory facts to model.
Epistemic authority and scope: Source warrant unknown; URL attribution preserved, completeness can degrade under selection/truncation.
Operational authority: Model may answer, investigate or make changes using imported material.
Behavioral-authority path: Foreground/child model or codemode nested consumer; tool text or emitted subset; advisory; current context and retained conversation.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Ranked pages/content, partial extraction/errors or failure output.
- Later read-back: Conversation tool result/details via host; codemode can omit nested output as runtime records.
- Delegated visibility: Only caller's selected/emitted content reaches later recipients; no implicit full-page delivery.
- Selection predicate: Query, objective, URL list, provider ranking/extraction, result cap and output truncation.
- Invalidation or expiry: No truth withdrawal mechanism in inspected adapter; repeat read may change remote content.
- Activation or effect: Acquisition capacity wired; no actual fetched source supplied.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> validateResponse(response, false)
> --- `extensions/parallel/server.ts`

#### EPI-RTE-goal-authority
Label: Hands-off goal authority

A live goal note tells Ultimate to decide instead of asking the user, against self-written checkable criteria, and record reasons. met sets a status; failed increments tries and blocks at three. finish accepts outcome met/blocked and records a report without independently verifying all criteria. This can record truth-apt claims about task success, but symbolic marking is not an evidence-consuming factual evaluator. Ending the goal restores ask-as-usual guidance.

Closest supplied records: [RT-RTE-lineage-branch](runtime.md#rt-rte-lineage-branch). Distinct identity: the named memory or goal operation, not branch creation; source and consumer differ.
Source: SRC-1 `extensions/goal/server.ts` (implementation). 

Check target / transition: Open user goal, criteria/status and decision records → permitted decision policy.
Evaluator and domain: Model judges criteria and choices; code validates status/indices/counters. No expected-answer oracle or per-decision human veto is wired here.
Activation and timing: Open goal supplies note; decisions/criteria/met/failed/pause/resume/finish tools update state.
Possible result: Recorded rationale, status, pause or ended report; criterion may be blocked after three failures.
Implemented force: Symbolic state/counters enforce bookkeeping; natural-language policy delegates decisions.
Epistemic authority and scope: A met marker licenses no externally verified success claim; reasons may carry candidate assessments.
Operational authority: Changes who is asked; during goal, Ultimate is instructed to choose approvals itself, including UI and dream proposals, while secrets/force pushes remain user matters in agent instructions.
Behavioral-authority path: Standing Ultimate per-run goal note and report; advisory instruction with fixed-state triggers; goal lifetime.
Owner and progression: Ultimate extension code owns the stated transition; model interpretation remains external where described.
- Immediate return: Recorded rationale, status, pause or ended report; criterion may be blocked after three failures.
- Later read-back: Goals/decisions persist in document and later notes/report; subsequent goal invocation can see current state.
- Delegated visibility: Branch receives decisions via normal messages; goal ledger does not supply all underlying evidence.
- Selection predicate: Currently open goal; requested valid criterion index for met/failed.
- Invalidation or expiry: Pause stops reminder; end removes active-goal grant; status updates do not undo prior host effects.
- Activation or effect: Decision-policy adaptation wired, compliance and successful goal attainment unobserved.
- Evidence limits: No observed run or causal experiment; implementation supports this local route, not successful model use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (args.action === 'met') {
>     criterion().status = 'met'
> --- `extensions/goal/server.ts`

### Claims

#### EPI-CLM-project-memory
Label: Durable facts and lessons

The code's introductory design description calls the stored material durable decisions, facts and lessons and says future branches start from an index brief. Distinct from [RT-CLM-coding-work](runtime.md#rt-clm-coding-work): this claim concerns retained project guidance, not the whole coding role. Source: SRC-1 `extensions/lineage/memory.ts`, doctrine/design. It does not explicitly promise infallibility.

> Project memory: each root keeps durable decisions, facts and lessons by slug. Branches from a root with memories start
> * from a brief of its index and recent landings; each landing distils memory operations with the summary model.
> --- `extensions/lineage/memory.ts`

#### EPI-CLM-recall-tuning
Label: Recall tuning metrics

No counterpart in supplied claims: this concerns relevance-selection quality on a named local sample, not factual memory correctness. SRC-1 `extensions/recall/README.md` is a doctrine/design document reporting operation, not a supplied observed trace/dataset or causal experiment. Metrics cannot be silently promoted to an observed-run source layer.

> The question and threshold were tuned once against 55 labelled messages from three chapters (the user's prompts, branch reports, casual lines such as "Good night!") and the project's live memories: precision 0.77, recall 0.62, quiet on 16 of 18 messages that called for no memory.
> --- `extensions/recall/README.md`

#### EPI-CLM-dream-learning
Label: Dream learning and change

Distinct from [RT-CLM-coding-work](runtime.md#rt-clm-coding-work): this claim concerns review of own operating records and proposed changes. SRC-1 `extensions/dream/DREAM.md`, doctrine/design. “Learned” is attributed language; successful capacity improvement requires separate evidence.

> Like people, agents need time to process what they learned. A dream is a working session: Ultimate reads back over
> the project's conversations, memory, failures and tools, writes a journal of what it learned, and proposes changes:
> to itself, and to how it works in this particular project (what it keeps doing by hand here, and what to build for it).
> --- `extensions/dream/DREAM.md`

> Nothing changes code, memory or storage by
> itself.
> --- `extensions/dream/DREAM.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
