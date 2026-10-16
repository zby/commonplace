---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Exo epistemic routes: imported evidence, authoritative memory, skill admission, task checks and self-change limits."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
---

# Exo epistemic report

## Source-and-claim boundary

The question is which shipped routes acquire or produce truth-apt content, test it, grant reliance and affect later behavior. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identities and layers are see [Source register](boundary.md#source-register). All new findings use SRC-1, implementation unless explicitly labelled doctrine/design. No target code, tests, examples or providers were executed. No observed-run or causal-experiment source was supplied.

Runtime is a provisional baseline, not an inspection boundary. Direct reads below extend it with memory admission/withdrawal, skills, web acquisition/extraction, todo claims, development hooks and the Harbor caller. Supplied runtime findings cover queue/recovery, Basic/Responses/native/RLM and tool/guardian activation; those implementations were not all independently reread. No supplied runtime fact requires supersession; details below qualify broader interpretations, not those records' bounded findings.

| Entry point or operation | Source path / read basis | Covering record or unassessed consequence |
|---|---|---|
| CLI dispatch, run, serve, agent/config, conversation send/events, sandbox/resources | SRC-1 `crates/cli/src/main.rs`, direct dispatch search and completion/send bodies; baseline for other branches | [RT-RTE-definition-admission](runtime.md#rt-rte-definition-admission); [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn). Resource CRUD is operational state, not claim acceptance. Full fork/delete lineage not retraced; no universal lineage guarantee. |
| Responses, Basic, native bridges, RLM and dynamic tool admission | Supplied runtime, source paths owned there | [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop); [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn); [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge); [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery); [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) |
| Exo profile registrations and instruction assembly | Direct SRC-1 `exo/profiles/practical.ts`, `exo/harness.ts` | [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions); new routes below. Scheduler, adapters, introspection, snapshots also registered; no inference that every tool returns checked knowledge. |
| Remember / forget / memory instruction | Direct SRC-1 `exo/tools/memory-tools.ts` | [EPI-RTE-memory-write](#epi-rte-memory-write); [EPI-RTE-memory-read](#epi-rte-memory-read); [EPI-RTE-memory-forget](#epi-rte-memory-forget) |
| Install/list/use/read/uninstall skill | Direct complete SRC-1 `exoharness/typescript/harness/skill-tools.ts` | [EPI-RTE-skills-install](#epi-rte-skills-install); [EPI-RTE-skills-read](#epi-rte-skills-read) |
| Search/fetch, caches, extraction, access checks | Direct complete SRC-1 `exo/tools/web-tools.ts` | [EPI-RTE-web-access](#epi-rte-web-access) |
| Todowrite / plan injection | Direct complete SRC-1 `exo/tools/todo-tools.ts` | [EPI-RTE-todo-state](#epi-rte-todo-state) |
| Pre-commit / pre-push / CI checks | Direct SRC-1 `scripts/precommit.mjs`, `package.json`; scoped searches `.githooks/`, `.github/workflows/ci.yml` | [EPI-RTE-development-checks](#epi-rte-development-checks); assertion coverage and actual results unassessed. |
| Harbor caller / sequential shared state | Direct SRC-1 `eval/harbor/src/exo_harbor/agent.py`, `eval/harbor/src/exo_harbor/plugin.py` | [EPI-RTE-harbor-task](#epi-rte-harbor-task) |
| Scheduler/adapters/Cloudflare recovery and guardian | Supplied runtime; direct CLI complete-rebuild branch and guardian build search | [RT-RTE-background-wakeup](runtime.md#rt-rte-background-wakeup); [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) |
| Self-improvement and learning declarations | Direct SRC-1 `docs/RSI.md`, `eval/harbor/src/exo_harbor/plugin.py`; harness guidance | [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement); [EPI-CLM-shared-trials](#epi-clm-shared-trials) |
| Remaining opaque or uninspected alternatives | Provider/native SDK internals outside source; full Claude/Cursor routes, adapter payload transformations, all HTTP paths, sandbox snapshots/fork semantics, introspection tool outputs and all example/test assertions not fully assessed | Cannot conclude system-complete absence of checks, provenance or accepted claims; cannot generalize inspected approval/check semantics to all alternatives. |

Missing execution evidence prevents claims of actual fact retention, checker activation, model compliance, useful knowledge, learning or exercised self-improvement. No persisted candidate instance or original source truth was supplied. Missing provider weights/version history prevents assessing distributed-parametric learning; see [RT-CMP-model-binding](runtime.md#rt-cmp-model-binding). No external Harbor grading implementation/result is captured; this prevents judging its oracle domain or grade-driven improvement. Unread available source is an inspection limit, not an access gap.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-entry](#epi-obj-memory-entry) | see [EPI-OBJ-memory-entry](#epi-obj-memory-entry) | MemoryEntry | SRC-1 `exo/tools/memory-tools.ts` | Content/check/consumer fields see record; no observed candidate. |
| [EPI-OBJ-skill-record](#epi-obj-skill-record) | see [EPI-OBJ-skill-record](#epi-obj-skill-record) | SkillRecord | SRC-1 `exoharness/typescript/harness/skill-tools.ts` | Content/check/consumer fields see record; no observed candidate. |
| [EPI-OBJ-web-result](#epi-obj-web-result) | see [EPI-OBJ-web-result](#epi-obj-web-result) | WebSearchResult | SRC-1 `exo/tools/web-tools.ts` | Content/check/consumer fields see record; no observed candidate. |
| [EPI-OBJ-todo](#epi-obj-todo) | see [EPI-OBJ-todo](#epi-obj-todo) | Todo | SRC-1 `exo/tools/todo-tools.ts` | Content/check/consumer fields see record; no observed candidate. |
| [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry) | Executable policy/capability, not inherently a truth-apt claim | see [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry) | SRC-1 `exoharness/typescript/harness/tool-registry.ts` | Structural admission is not correctness. |
| [RT-OBJ-guardian-update](runtime.md#rt-obj-guardian-update) | Status/exit code asserts pipeline outcome; reason is proposer text | see [RT-OBJ-guardian-update](runtime.md#rt-obj-guardian-update) | SRC-1 `exo/tools/guardian-tools.ts` | No observed outcome. |
| [RT-CMP-model-binding](runtime.md#rt-cmp-model-binding) | Individual encoded propositions not determinable | see [RT-CMP-model-binding](runtime.md#rt-cmp-model-binding) | SRC-1 `exoharness/typescript/model-runtime/shared.ts` | External parameters opaque; no weight-change finding. |

## Authority-route ledger

All rows describe architecture, not observed operation. A check is separated from its disposition; a storage or publication disposition is not epistemic acceptance. Generic route fields owned by a shared record say see. For model-generated answers, the content/update relation is indeterminate: acquisition, reshaping, entailment and non-entailment depend on unsupplied instances. A model call alone does not prove ampliative conjecture.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | content transformation | implemented | none individuated | truth-apt transformation: indeterminate | Task/history → answer or action | Configured model; open task domain | see [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | Candidate text/tool call | Model selection, not truth certification | No general answer warrant | Answer returned; calls enter authorization | see [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | SRC-1 `crates/executor/src/basic.rs` | none | none | see [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) |
| [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | disposition/acceptance | implemented | none individuated | no content change | Tool execution permission | Runtime policy / approval responder | see [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | Allow/deny; final completion when no further tools | Enforcing capability gate | No claim acceptance; terminal status is not task correctness | Dispatch or block action before next model round | see [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | SRC-1 `crates/executor/src/permissions.rs` | none | none | see [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) |
| [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop) | retention | implemented | none individuated | no content change | Messages/tool results → event history | Software journal and materialization | see [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop) | Stored events available later | Persist/reload | Preserves available content, not truth | Later model sees materialized history | see [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop) | SRC-1 `exoharness/typescript/model-runtime/turn-loop.ts` | none | none | see [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop) |
| [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery) | content transformation | implemented | none individuated | truth-apt transformation: indeterminate | Selected text → subquery answer | Separate configured-model request, no tools | see [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery) | Answer preview / optional JS value | Value-return guidance | No independently checked derivation | Root can consume answer, not full subquery state | see [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery) | SRC-1 `crates/executor/src/native/rlm.rs` | none | none | see [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery) |
| [EPI-RTE-web-access](#epi-rte-web-access) | content transformation | implemented | [EPI-OBJ-web-result](#epi-obj-web-result) | truth-apt transformation: acquisition/import | Remote text/search → tool result | Host HTTP/provider/extraction code; source warrant unknown | see [EPI-RTE-web-access](#epi-rte-web-access) | Normalized/selected/truncated content | Informational import | No endorsement of page propositions | Later model may use external evidence | see [EPI-RTE-web-access](#epi-rte-web-access) | SRC-1 `exo/tools/web-tools.ts` | none | none | see [EPI-RTE-web-access](#epi-rte-web-access) |
| [EPI-RTE-web-access](#epi-rte-web-access) | check/evidence production | implemented | [EPI-OBJ-web-result](#epi-obj-web-result) | no content change | Fetch destination, response status and format | Address/content/status rules, not source truth | see [EPI-RTE-web-access](#epi-rte-web-access) | Allowed response or structured error | Access filter | Transport/property checks only | Fetch/return or refuse | see [EPI-RTE-web-access](#epi-rte-web-access) | SRC-1 `exo/tools/web-tools.ts` | none | none | see [EPI-RTE-web-access](#epi-rte-web-access) |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | check/evidence production | implemented | [EPI-OBJ-memory-entry](#epi-obj-memory-entry) | no content change | Text length and stored JSON shape | Deterministic structural rules | see [EPI-RTE-memory-write](#epi-rte-memory-write) | Valid input or error | Validation | Storage eligibility only | Invalid write rejected | see [EPI-RTE-memory-write](#epi-rte-memory-write) | SRC-1 `exo/tools/memory-tools.ts` | none | none | see [EPI-RTE-memory-write](#epi-rte-memory-write) |
| [EPI-RTE-memory-write](#epi-rte-memory-write) | retention | implemented | [EPI-OBJ-memory-entry](#epi-obj-memory-entry) | no content change | Trimmed proposed text → durable entry | Writer and cap policy | see [EPI-RTE-memory-write](#epi-rte-memory-write) | New entry; oldest evicted if needed | Persistent state | No evidence-consuming acceptance | Available across agent conversations | see [EPI-RTE-memory-write](#epi-rte-memory-write) | SRC-1 `exo/tools/memory-tools.ts` | none | none | see [EPI-RTE-memory-write](#epi-rte-memory-write) |
| [EPI-RTE-memory-read](#epi-rte-memory-read) | operational admission/selection/consumption | implemented | [EPI-OBJ-memory-entry](#epi-obj-memory-entry) | no content change | Latest memory → developer instructions | All current entries if schema readable | see [EPI-RTE-memory-read](#epi-rte-memory-read) | Authoritative-context message or warning | Advisory/model-interpreted | Authority label exceeds available factual warrant | Guide subsequent model decisions | see [EPI-RTE-memory-read](#epi-rte-memory-read) | SRC-1 `exo/tools/memory-tools.ts` | none | Authoritative does not mean verified | see [EPI-RTE-memory-read](#epi-rte-memory-read) |
| [EPI-RTE-memory-forget](#epi-rte-memory-forget) | disposition/acceptance | implemented | [EPI-OBJ-memory-entry](#epi-obj-memory-entry) | no content change | Entry withdrawal | Proposer selects ID; code exact-match removal | see [EPI-RTE-memory-forget](#epi-rte-memory-forget) | Removed count / updated store | Enforcing omission at future injection | No independent falsity judgment | Stops supplying that entry through memory channel | see [EPI-RTE-memory-forget](#epi-rte-memory-forget) | SRC-1 `exo/tools/memory-tools.ts` | none | none | see [EPI-RTE-memory-forget](#epi-rte-memory-forget) |
| [EPI-RTE-skills-install](#epi-rte-skills-install) | check/evidence production | implemented | [EPI-OBJ-skill-record](#epi-obj-skill-record) | no content change | Skill syntax/name/path/size/index readability | Program structural validators | see [EPI-RTE-skills-install](#epi-rte-skills-install) | Pass/error | Validation | No semantic/procedural reliability license | Blocks malformed installation | see [EPI-RTE-skills-install](#epi-rte-skills-install) | SRC-1 `exoharness/typescript/harness/skill-tools.ts` | none | none | see [EPI-RTE-skills-install](#epi-rte-skills-install) |
| [EPI-RTE-skills-install](#epi-rte-skills-install) | retention | implemented | [EPI-OBJ-skill-record](#epi-obj-skill-record) | non-truth-apt policy/content update: install or replace instruction package | Valid record → artifact and catalog | Software publication after structural checks | see [EPI-RTE-skills-install](#epi-rte-skills-install) | Stored skill and updated index | Persistent publication | Not acceptance of factual rationale | Makes procedure discoverable | see [EPI-RTE-skills-install](#epi-rte-skills-install) | SRC-1 `exoharness/typescript/harness/skill-tools.ts` | none | none | see [EPI-RTE-skills-install](#epi-rte-skills-install) |
| [EPI-RTE-skills-read](#epi-rte-skills-read) | operational admission/selection/consumption | implemented | [EPI-OBJ-skill-record](#epi-obj-skill-record) | no content change | Catalog / selected skill / file → model | Model name/path selection; code retrieval | see [EPI-RTE-skills-read](#epi-rte-skills-read) | Body or file content | Advisory instructions | No checked claim warrant | Follow procedure requested on matching task | see [EPI-RTE-skills-read](#epi-rte-skills-read) | SRC-1 `exoharness/typescript/harness/skill-tools.ts` | none | none | see [EPI-RTE-skills-read](#epi-rte-skills-read) |
| [EPI-RTE-skills-read](#epi-rte-skills-read) | disposition/acceptance | implemented | [EPI-OBJ-skill-record](#epi-obj-skill-record) | no content change | Uninstall → index removal | Exact-name filtering | see [EPI-RTE-skills-read](#epi-rte-skills-read) | No catalog entry; artifacts remain | Enforcing unlisting, not full erasure | No epistemic rejection record | use_skill stops; direct file read can still succeed | see [EPI-RTE-skills-read](#epi-rte-skills-read) | SRC-1 `exoharness/typescript/harness/skill-tools.ts` | none | Unlisting is not complete withdrawal | see [EPI-RTE-skills-read](#epi-rte-skills-read) |
| [EPI-RTE-todo-state](#epi-rte-todo-state) | check/evidence production | implemented | [EPI-OBJ-todo](#epi-obj-todo) | no content change | Todo shape/status/size | Program enum and cap checks, not task evidence | see [EPI-RTE-todo-state](#epi-rte-todo-state) | Pass/error | Validation | No warranted completion assertion | Permits list write | see [EPI-RTE-todo-state](#epi-rte-todo-state) | SRC-1 `exo/tools/todo-tools.ts` | none | none | see [EPI-RTE-todo-state](#epi-rte-todo-state) |
| [EPI-RTE-todo-state](#epi-rte-todo-state) | retention | implemented | [EPI-OBJ-todo](#epi-obj-todo) | non-truth-apt policy/content update: full plan replacement | Validated list → artifact | Model/caller chooses labels; code persists | see [EPI-RTE-todo-state](#epi-rte-todo-state) | New current list | Persistent state | Completed remains proposer assertion | Plan available to later rounds | see [EPI-RTE-todo-state](#epi-rte-todo-state) | SRC-1 `exo/tools/todo-tools.ts` | none | none | see [EPI-RTE-todo-state](#epi-rte-todo-state) |
| [EPI-RTE-todo-state](#epi-rte-todo-state) | operational admission/selection/consumption | implemented | [EPI-OBJ-todo](#epi-obj-todo) | no content change | Plan → developer prompt when open items exist | Software pending/in_progress predicate | see [EPI-RTE-todo-state](#epi-rte-todo-state) | Whole list or no message | Advisory instructions | Remaining count entailed from status fields only | Model asked to maintain/verify plan | see [EPI-RTE-todo-state](#epi-rte-todo-state) | SRC-1 `exo/tools/todo-tools.ts` | none | none | see [EPI-RTE-todo-state](#epi-rte-todo-state) |
| [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | check/evidence production | implemented | [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry) | no content change | Tool structure/schema/conflicts | Host loader/validator, executes imports | see [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | Structural validation or error | Validation with possible pre-admission effects | No semantic safety/correctness license | Precedes registry commit and later tool selection | see [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | SRC-1 `exoharness/typescript/harness/tool-modules.ts` | none | none | see [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) |
| [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | operational admission/selection/consumption | implemented | [RT-OBJ-tool-registry](runtime.md#rt-obj-tool-registry) | non-truth-apt policy/content update: executable capability installation | Committed tool → next registry | Software install/register; model later selects call | see [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | Executable module/handler | Executable authority | Capability admission, not knowledge acceptance | Host import/handler and later rounds can change behavior | see [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) | SRC-1 `exoharness/typescript/harness/tool-registry.ts` | none | none | see [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission) |
| [EPI-RTE-development-checks](#epi-rte-development-checks) | check/evidence production | implemented | none individuated | no content change | Staged source/types/suite assertions | Format/lint/typecheck/tests within configured domains | see [EPI-RTE-development-checks](#epi-rte-development-checks) | Diagnostics or failure | Check production | At most named program properties and tested assertions | May fix/restage source; return exit failure | see [EPI-RTE-development-checks](#epi-rte-development-checks) | SRC-1 `scripts/precommit.mjs` | none | none | see [EPI-RTE-development-checks](#epi-rte-development-checks) |
| [EPI-RTE-development-checks](#epi-rte-development-checks) | disposition/acceptance | implemented | none individuated | no content change | Commit path continuation | Installed hook process success | see [EPI-RTE-development-checks](#epi-rte-development-checks) | Continue or abort hook | Conditional enforcing local gate | No general product correctness or improvement | Commit path can proceed if invocation succeeds | see [EPI-RTE-development-checks](#epi-rte-development-checks) | SRC-1 `scripts/precommit.mjs` | none | none | see [EPI-RTE-development-checks](#epi-rte-development-checks) |
| [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) | behavior/policy adaptation | implemented | [RT-OBJ-guardian-update](runtime.md#rt-obj-guardian-update) | non-truth-apt policy/content update: rebuilt own source and services | Source changes → build/restart | Host fixed build commands, exit status | see [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) | Queued then succeeded/failed pipeline status | Executable activation | Build success is not improvement | Future services consume changed binaries/modules | see [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) | SRC-1 `exo/scripts/exo-service-guardian` | [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement) | Benefit and evidence-responsive update not established | see [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) |
| [EPI-RTE-harbor-task](#epi-rte-harbor-task) | operational admission/selection/consumption | implemented | none individuated | no content change | Trial instruction → shared agent / trajectory export | Plugin/driver; grading external and uninspected | see [EPI-RTE-harbor-task](#epi-rte-harbor-task) | Task execution/export attempt | Operational task delivery | No captured grade/warrant transfer | Sequential trials reuse agent; failure still exports | see [EPI-RTE-harbor-task](#epi-rte-harbor-task) | SRC-1 `eval/harbor/src/exo_harbor/agent.py` | [EPI-CLM-shared-trials](#epi-clm-shared-trials) | Reuse does not establish learning | see [EPI-RTE-harbor-task](#epi-rte-harbor-task) |

No lifecycle integration following epistemic acceptance is established by these inspected writers: they store text, publish procedures or update execution state without a decision consuming factual evidence against a named truth criterion, intended use and scope. This is bounded to these routes, not a system-complete absence: arbitrary tools/native harnesses can implement additional checks.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-recursive-improvement](#epi-clm-recursive-improvement) | see record | SRC-1 `docs/RSI.md`, doctrine/design | see record | [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update); [RT-BAP-rebuilt-services](runtime.md#rt-bap-rebuilt-services) | None supplied | No independent objective, actual evidence-driven update or downstream comparative outcome | Own-source change/build/restart capacity is wired, conditional on grants | Recursive improvement is not demonstrated; code access alone is insufficient |
| [EPI-CLM-memory-authority](#epi-clm-memory-authority) | see record | SRC-1 `exo/tools/memory-tools.ts`, implementation of model-facing guidance | see record | [EPI-RTE-memory-write](#epi-rte-memory-write); [EPI-RTE-memory-read](#epi-rte-memory-read) | None supplied | Shape checks admit the same false and true text; original evidence not required | Persistent model-interpreted reliance path | Operational authority instruction, not warranted fact acceptance |
| [EPI-CLM-shared-trials](#epi-clm-shared-trials) | see record | SRC-1 `eval/harbor/src/exo_harbor/plugin.py`, doctrine/design plus validation implementation | see record | [EPI-RTE-harbor-task](#epi-rte-harbor-task) | None supplied | Sequential shared state without grade-driven update comparison | Reduces simultaneous self-edit races by rejecting concurrent Exo trials | Learning and component effect not established |
| [RT-CLM-recovery-scope](runtime.md#rt-clm-recovery-scope) | see record | SRC-1 `crates/executor/src/basic.rs`, implementation | see record | [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) | None supplied | Unresolved-tool guard is counterexample to universal safe replay | Durable lineage can preserve requests/results; not arbitrary exactly-once effects | Correct preserved events need not be correct propositions |

## Bounded conclusion

Exo exposes several independent authority paths. Basic/Responses and native/RLM alternatives generate answers without a general expected-answer oracle; their novel content remains candidate content, with entailment versus conjecture not determinable without instances. External model parameters are opaque; there is no source basis for a claim about weight training or parametric knowledge change. See [RT-CMP-model-binding](runtime.md#rt-cmp-model-binding); [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn); [RT-RTE-native-bridge](runtime.md#rt-rte-native-bridge); [RT-RTE-rlm-subquery](runtime.md#rt-rte-rlm-subquery).

Web tools acquire external assertions with URL/provider/extractor metadata. Source warrant is unknown; reader-mode filtering and truncation can remove context, so transport success cannot license the page propositions. A concrete implementation deduction, not a target execution: with fallback input `<p>Count: 2 &amp; 3</p><aside>Not verified</aside>`, extractReadableText removes the aside, converts closing paragraph to newline, strips tags, decodes amp and trims, returning text `Count: 2 & 3` and null title. This is non-ampliative reshaping of the retained fragment, but not preservation of the page's qualification. Whether reader mode chooses a different fragment depends on uninspected dependency execution. Code passage and transformation scope are see [EPI-RTE-web-access](#epi-rte-web-access). It creates no new empirical warrant.

Memory is retained across agent conversations and labelled authoritative in developer messages after shape checks. Forget and cap eviction alter future supply, not truth, earlier mentions or effects. Corruption instead produces an explicit unavailability warning and blocks writes. These are separate checking, retention, operational reliance and withdrawal functions, not lifecycle integration of an accepted claim. See [EPI-RTE-memory-write](#epi-rte-memory-write); [EPI-RTE-memory-read](#epi-rte-memory-read); [EPI-RTE-memory-forget](#epi-rte-memory-forget).

Skills admit durable instructions after structural validation. Catalog disclosure, selected body retrieval and supporting-file retrieval have different authority paths; uninstallation removes catalog membership but does not revoke all direct supporting-file access. A skill may contain factual theory, but this code does not individuate one or establish content-directed criticism. Todos similarly retain plans/status assertions: the remaining count follows from declared statuses, while completed is not evidence of completed work. See [EPI-RTE-skills-install](#epi-rte-skills-install); [EPI-RTE-skills-read](#epi-rte-skills-read); [EPI-RTE-todo-state](#epi-rte-todo-state).

Development hooks and CI provide bounded code evaluators. They are counterexamples to an unqualified claim that Exo has no checking: local hook failure can block that commit path, and tests can check their specified assertions. They are not mandatory gates on every source edit or guardian restart and no passing result was supplied. Guardian build exit status checks pipeline execution, not semantic correctness or benefit. Reusable tool admission can execute host code before later handler selection. These direct policy/capability/machinery changes need no truth-apt acceptance phase. See [EPI-RTE-development-checks](#epi-rte-development-checks); [RT-RTE-tool-admission](runtime.md#rt-rte-tool-admission); [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update).

The self-change boundary is Exo source/runner/services over rebuild to subsequent service turns. No independent improvement objective, objective-bearing evidence determining an actual update (link 1), or later behavior causally depending on it (link 4) is supplied; links 2–3 are architectural possibilities, not observed events. Thus useful learning, exercised self-improvement and causal benefit are independently unestablished, not disproven. Sequential Harbor trials share state but do not close these gaps. See [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update); [EPI-RTE-harbor-task](#epi-rte-harbor-task). Self-referential source guidance establishes inspectability and modification requests, not a complete reflective loop; autonomous task continuation is distinct from an autonomous theory builder. No supplied formulated-theory instance with content-directed criticism and retained criticism shaping a next round establishes theory-builder conditions 1–4; additional model/skill content could supply such instances, so this is an instance/evidence limit rather than system-wide impossibility. No single epistemic verdict follows across these heterogeneous routes.

## Shared records

### Operative objects

#### EPI-OBJ-memory-entry
Label: MemoryEntry

Source-native identity, representational form and storage substrate: Agent-scoped entries in memory/exo-memory.json; natural-language text plus symbolic id and createdAt; versioned agent artifact. Text may assert user preferences or facts about the agent; no fact instance or its original evidence is supplied.

Evidence: SRC-1 `exo/tools/memory-tools.ts`, implementation. Closest supplied record [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions) covers the enclosing instruction/turn channel, not this retained content part; no supplied object counterpart. Distinct identity from tool registry and turn envelope.

#### EPI-OBJ-skill-record
Label: SkillRecord

Source-native identity, representational form and storage substrate: Agent-scoped skills/<name>.json and skills/index.json. Natural-language skillMd/description and bundled text, with symbolic names, paths and timestamps. Procedures need not be truth-apt; any factual rationale is not individuated in this source-only run.

Evidence: SRC-1 `exoharness/typescript/harness/skill-tools.ts`, implementation. Closest supplied record [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions) covers the enclosing instruction/turn channel, not this retained content part; no supplied object counterpart. Distinct identity from tool registry and turn envelope.

#### EPI-OBJ-web-result
Label: WebSearchResult

Source-native identity, representational form and storage substrate: Natural-language title/snippet/page text with symbolic provider, URL, status, extractor and truncation metadata. Search cache is process-local; tool results enter conversation storage through the Responses loop. Imported assertions are truth-apt only within their source scopes; truth is not checked.

Evidence: SRC-1 `exo/tools/web-tools.ts`, implementation. Closest supplied record [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop) covers the enclosing instruction/turn channel, not this retained content part; no supplied object counterpart. Distinct identity from tool registry and turn envelope.

#### EPI-OBJ-todo
Label: Todo

Source-native identity, representational form and storage substrate: Conversation-scoped todos/exo-todos.json; natural-language imperatives and symbolic status enum. The status completed asserts completion, but the code does not check work evidence.

Evidence: SRC-1 `exo/tools/todo-tools.ts`, implementation. Closest supplied record [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions) covers the enclosing instruction/turn channel, not this retained content part; no supplied object counterpart. Distinct identity from tool registry and turn envelope.

### Routes

#### EPI-RTE-memory-write
Label: Remember admission and write

Model/caller text → remember handler → agent memory artifact. Handler trims text, rejects empty or overlong text, reads a schema-valid store, appends a UUID/time entry and retains the newest 200. The handler owns structural decisions; the foreground model chooses the proposed fact. Open requests, no expected-answer oracle, human content authorship unresolved. Tool invocation is subject to the registry permission route, not mandatory per-fact human approval. Instructions request standalone durable facts. No evidence or truth criterion is consumed. Corrupt stores reject writes; concurrent read-modify-write can lose an update.

Closest supplied record: [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exo/tools/memory-tools.ts`, implementation.

- Immediate return: An error, or ok/id/total/dropped after artifact write.
- Later read-back: Latest artifact is consumed by memoryInstruction on subsequent model rounds and conversations for this agent.
- Delegated visibility: The writer receives text, not mandatory provenance, confidence, criterion or intended-use evidence.
- Selection predicate: Remember call and nonempty text of at most 600 characters; readMemory selects latest matching artifact version.
- Invalidation or expiry: Oldest entries drop beyond 200; forget removes selected IDs; no freshness expiry or compare-and-swap.
- Activation or effect: Wired retention and later instruction supply; no observed change of model behavior.
- Evidence limits: Shape/length admission licenses storage only, not acceptance of a proposition. No actual saved fact or run supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (text.length > MAX_TEXT_CHARS) {
>           return {
>             ok: false,
>             error: `text exceeds ${MAX_TEXT_CHARS} characters; summarize it first`,
>           };
>         }
> --- `exo/tools/memory-tools.ts`

#### EPI-RTE-memory-read
Label: Memory authority and corruption

Latest schema-valid memory artifact → memoryInstruction → developer message via exoInstructions. Software selects all current entries and labels them authoritative. On corrupt read it supplies an unavailability warning instead of the entries. This is operational reliance instruction, not evidence-consuming acceptance. It is a distinct dynamic-memory supply part, not a redeclaration of the generic instruction channel.

Closest supplied record: [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exo/tools/memory-tools.ts`, implementation.

- Immediate return: Developer message, null for empty store, or corruption warning.
- Later read-back: Latest store is reread during later Responses instruction materialization; across this agent’s conversations.
- Delegated visibility: Model receives entry IDs/text, not createdAt, original source evidence or a validation record.
- Selection predicate: All entries in latest matching artifact; no query relevance or factual ranking.
- Invalidation or expiry: Next read reflects forget, cap eviction or replacement; corruption blocks normal injection, not artifact deletion.
- Activation or effect: Natural-language direction to rely in model decisions; compliance and downstream decisions unobserved.
- Evidence limits: Authoritative is an instruction label. Schema-valid false text takes the same path as true text.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> content: `Durable memory you saved earlier with the remember tool. Treat these as authoritative context. Add new facts with remember and drop stale ones with forget(id).\n\n${lines.join("\n")}`,
> --- `exo/tools/memory-tools.ts`

#### EPI-RTE-memory-forget
Label: Forget withdrawal

Model/caller ID → forget → filtered agent store → future memory injection. Model/caller proposes removal; exact-ID software decides whether anything matches. Guidance asks the model to drop stale entries, but no stale-fact evaluator is implemented here. No oracle or per-item human approval is established. Removal changes future reliance supply, not the truth of the removed claim.

Closest supplied record: [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exo/tools/memory-tools.ts`, implementation.

- Immediate return: ok/id/removed; artifact written only when an entry was removed.
- Later read-back: Future memoryInstruction sees the filtered latest store; old artifact versions are not rewritten by this handler.
- Delegated visibility: Future prompt omits deleted entries, but existing conversation mentions are not retracted.
- Selection predicate: Exact equality of requested ID; nonempty ID required.
- Invalidation or expiry: Remember can add a new entry; no automatic falsity detection or historical retraction.
- Activation or effect: Wired withdrawal from this memory channel only; no observed use.
- Evidence limits: Removal does not erase prior tool events, undo actions or establish epistemic rejection.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> store.entries = store.entries.filter((entry) => entry.id !== id);
> --- `exo/tools/memory-tools.ts`

#### EPI-RTE-skills-install
Label: Skill installation and publication

Model/caller skillMd and files → syntax/name/path/size checks → skill artifact → index publication. Software rejects malformed inputs and corrupt indexes; model/caller supplies all instruction content. Open installation requests, no answer oracle or skill-performance evaluation. Existing name updates the record. Guidance requests reusable procedures; persisted source includes full text and files. No factual evidence, semantic safety or usefulness gate is required.

Closest supplied record: [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exoharness/typescript/harness/skill-tools.ts`, implementation.

- Immediate return: ok/name/updated/files or structural validation error.
- Later read-back: Catalog feeds skillsInstruction; use_skill loads named body and read_skill_file loads exact bundled path.
- Delegated visibility: Catalog supplies names/descriptions only; selected body and file paths return through tools; requested file contents separately.
- Selection predicate: Parsed name/description and bounded files; same name replaces content. Latest artifact version selected.
- Invalidation or expiry: Uninstall removes index membership; previous artifact versions remain. No automatic rollback of bad instructions.
- Activation or effect: Wired publication and later model-directed selection, not demonstrated skill acquisition or improved capacity.
- Evidence limits: Index/content writes lack compare-and-swap; import provenance and factual rationale are not required.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Write content first, then publish in the index: a listed skill must
>         // always have readable content.
>         await handle.writeArtifactJson({
>           path: skillArtifactPath(name),
>           value: record as unknown as JsonValue,
>         });
> --- `exoharness/typescript/harness/skill-tools.ts`

#### EPI-RTE-skills-read
Label: Skill use and withdrawal

Index → developer catalog → model-selected use_skill → raw skillMd and paths → optional read_skill_file. Uninstall filters index entries. Model/caller chooses name and removal; code checks membership for use_skill and retrieves exact requested paths. This is task guidance, not enforced skill compliance. No truth/utility oracle. read_skill_file reads the stored record without testing catalog membership, so uninstallation is not complete withdrawal of stored supporting content by known name/path.

Closest supplied record: [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exoharness/typescript/harness/skill-tools.ts`, implementation.

- Immediate return: Catalog developer message or warning/null; use_skill returns body/file paths or error; file read returns contents; uninstall returns removed count.
- Later read-back: Later requests receive updated catalog. Named content is read from latest retained artifacts; prior tool-result messages can remain.
- Delegated visibility: Names/descriptions precede full selected body; only selected bundled files return.
- Selection predicate: All indexed catalog entries; model chooses skill name; exact bundled path selects file. use_skill requires index membership.
- Invalidation or expiry: Uninstall unlists only; read_skill_file can still find a retained record. Corrupt catalog emits unavailability instruction.
- Activation or effect: Advisory instruction authority for later model decisions; selection/obedience unobserved.
- Evidence limits: Not an evidence-consuming acceptance or historical retraction mechanism; retained instruction content may be false or unsafe.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const record = await readSkill(skillsHandle(execution.context), name);
>         if (record === null) {
>           return { ok: false, error: `skill not installed: ${name}` };
>         }
> --- `exoharness/typescript/harness/skill-tools.ts`

#### EPI-RTE-web-access
Label: Search and page acquisition

Model query/URL → host search/fetch → normalized source text/metadata → tool result → subsequent model context. Host code chooses configured provider, applies fetch address/content/HTTP checks and extracts reader-mode or fallback text. These evaluate access/transport/format, not page propositions. Search API ranking is imported, not independent endorsement. No answer oracle; source truth and human authorship unresolved. Search cache can reuse results for 15 minutes.

Closest supplied record: [RT-RTE-responses-loop](runtime.md#rt-rte-responses-loop). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exo/tools/web-tools.ts`, implementation.

- Immediate return: Search title/url/snippet list with provider/cache metadata, or fetch text/title/URL/status/extractor/truncated; bounded error results.
- Later read-back: Search process cache reuses normalized result; conversation tool events may reach subsequent model requests through Responses materialization.
- Delegated visibility: Model gets normalized/selected and possibly truncated text, not a guaranteed full original page or browser execution.
- Selection predicate: Model query/count or URL/maxChars; provider config selects Brave versus DuckDuckGo; extractor and length rules select page portions.
- Invalidation or expiry: Cache expires after 15 minutes or eviction; no claim-level withdrawal on source correction. A later fetch can differ.
- Activation or effect: Wired import into model context, including host access independent of sandbox networking. Not observed operation.
- Evidence limits: Imported source warrant is unknown; extraction may degrade context and traceability of qualifications. Dependencies and remote sources not inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> text: truncated ? text.slice(0, maxChars) : text,
>           truncated,
> --- `exo/tools/web-tools.ts`

The deterministic fallback deduction in the conclusion uses these inspected rules, not an execution trace:

> .replace(/<(nav|footer|aside)\b[\s\S]*?<\/\1>/gi, " ")
> --- `exo/tools/web-tools.ts`

> .replace(/<[^>]*>/g, " ");
>   text = decodeEntities(text)
>     .split("\n")
>     .map((line) => line.replace(/[ \t]+/g, " ").trim())
>     .join("\n")
>     .replace(/\n{3,}/g, "\n\n")
>     .trim();
>   return { title, text };
> --- `exo/tools/web-tools.ts`

#### EPI-RTE-todo-state
Label: Todo checking and state

Model full list → structural/cap checks → conversation artifact → developer instruction if any item is open. Model proposes completion labels; software validates enum/length, not actual completion evidence. Open task planning, no answer oracle. Instructions say completed only after verification, but no implementation enforces such verification or exactly one in_progress. Empty list clears current plan. Corrupt reads are treated as empty, unlike memory.

Closest supplied record: [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `exo/tools/todo-tools.ts`, implementation.

- Immediate return: Error or ok/total/remaining, derived by counting pending/in_progress statuses.
- Later read-back: Latest conversation artifact is injected on later rounds while any item remains open.
- Delegated visibility: Model receives entire list when open work exists; all-terminal list yields no developer message.
- Selection predicate: Latest matching artifact version; todo status membership and size constraints; open predicate gates injection.
- Invalidation or expiry: Full replacement or empty write clears current plan; corrupt list also suppresses injection.
- Activation or effect: Wired model-interpreted plan guidance; no observed task behavior.
- Evidence limits: Counts are entailed from validated status fields only; completed status is not independently warranted task success.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const remaining = todos.filter(
>           (todo) => todo.status === "pending" || todo.status === "in_progress",
>         ).length;
> --- `exo/tools/todo-tools.ts`

#### EPI-RTE-development-checks
Label: Development validation hooks

Staged files → formatting/lint fixes and restaging → pnpm check. pre-commit invokes this script; pre-push invokes cargo clippy. pnpm check chains lint/typecheck/Vitest; CI separately configures format, Rust tests and Worker checks. Programs judge code shape/types and suite-specific assertions, not unrestricted semantic correctness. execFileSync failure aborts the script, making hook success a permissive commit-path condition where hooks are installed/invoked. Ordinary guardian builds do not call this validation script. No actual change, test result, hook installation or commit is supplied.

Closest supplied record: [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `scripts/precommit.mjs`, implementation.

- Immediate return: Inherited diagnostics and success, or thrown command failure; format/lint may modify and restage files.
- Later read-back: inapplicable — this route establishes no retained evaluation result reaching a later invocation; source edits can persist but test output retention is not shown here.
- Delegated visibility: Each checker sees selected staged files or its configured suite, not a universal truth specification.
- Selection predicate: Nondeleted staged files excluding website/docs-src; extension selects formatter/linter; empty list exits without pnpm check.
- Invalidation or expiry: Rerun after edits; local hook bypass and alternate build routes prevent universal enforcement.
- Activation or effect: Wired local hook check; CI declared executable workflow, no run supplied. Not an empirical improvement gate on every rebuild.
- Evidence limits: Passing finite tests licenses tested assertions under their setups only; test coverage and actual results not assessed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> run("pnpm", ["check"]);
> --- `scripts/precommit.mjs`

Additional evidence: SRC-1 `.githooks/pre-commit`, `.githooks/pre-push`, `package.json`, `.github/workflows/ci.yml`. CI configuration is implementation of job requests, not observed passing operation.

> cargo clippy --workspace --all-targets -- -D warnings
> --- `.githooks/pre-push`

> "check": "pnpm lint && pnpm typecheck && pnpm test",
> --- `package.json`

#### EPI-RTE-harbor-task
Label: Harbor trial and export

Harbor instruction → Exo conversation attached to Harbor-owned container → send → finally export trajectory. Plugin shares one agent across trials and requires sequential trials for the Exo harness. Exo model proposes task actions; external Harbor owns grading/container lifecycle. The driver does not consume a grade into a mandatory update/acceptance decision. No expected answer or grader implementation is captured in these inspected integration files. This is a distinct shipped caller, not another model-loop implementation.

Closest supplied record: [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn). Distinct identity: this is the specialized writer, reader, withdrawal, evaluator or caller described above, not the enclosing generic turn or instruction route; no supplied record declares this operation at this granularity. Evidence: SRC-1 `eval/harbor/src/exo_harbor/agent.py`, implementation.

- Immediate return: run returns after send or raises; metadata and trajectory export attempted even after timeout/failure.
- Later read-back: Shared agent state can span sequential trials; a feedback-to-update path from external grades is not established by these files.
- Delegated visibility: Exo receives instruction and attached environment; trajectory consumer receives exported activity, not proof of task correctness.
- Selection predicate: Per-trial context ID selects conversation; plugin requires Docker, one agent and sequential Exo trials.
- Invalidation or expiry: Per-trial container is Harbor-owned; export failure logged. Resume unsupported by this driver.
- Activation or effect: Wired trial execution/export integration; no benchmark outcomes or benefit observed.
- Evidence limits: Sequential reuse enables persistence, not learning evidence or causal attribution to self-editing.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> # A timed-out trial still has a partial trajectory worth keeping.
> --- `eval/harbor/src/exo_harbor/agent.py`

### Claims

#### EPI-CLM-recursive-improvement
Label: Recursive improvement support

Claimed operation: Exo supports incremental recursive improvement through own-code modification, clone, rebuild/restart and rewind. Source: SRC-1 `docs/RSI.md`, doctrine/design. Closest supplied [RT-RTE-guardian-update](runtime.md#rt-rte-guardian-update) establishes one implementation pathway, not this public rationale; no supplied claim counterpart. This claim does not assert underlying model improvement; that scope is explicitly excluded by the source.

> That's the whole design. Exo supports recursive improvement by allowing the
> model to modify any aspect of itself, clone itself, rebuild and restart itself,
> and rewind itself, and to do all this incrementally and somewhat safely, with
> minimal scaffolding.
> --- `docs/RSI.md`

#### EPI-CLM-memory-authority
Label: Authoritative saved memory

Claimed operation/warrant instruction: saved memory should be treated as authoritative context. SRC-1 `exo/tools/memory-tools.ts`, implementation of model-facing doctrine; see [EPI-RTE-memory-read](#epi-rte-memory-read) for the exact passage. Closest supplied [RT-BAP-harness-instructions](runtime.md#rt-bap-harness-instructions) describes general instruction supply, not this content-specific authority instruction. This is requested reliance, not an assertion by the analyst that memory is warranted.

#### EPI-CLM-shared-trials
Label: Shared trials enable learning

Claimed operation: sequential trials avoid races and enable learning from one trial to the next in a shared self-evolving agent. SRC-1 `eval/harbor/src/exo_harbor/plugin.py`, doctrine/design; sequential rejection condition is implementation. Closest supplied [RT-RTE-managed-turn](runtime.md#rt-rte-managed-turn) is runtime execution, not this trial/learning rationale; no supplied claim counterpart.

> # Exo self-edits, so to avoid races and enable learning from one
>             # trial to the next, we require sequential trials.
> --- `eval/harbor/src/exo_harbor/plugin.py`

### Components

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; each specialized consumer/channel/force/horizon is recorded in its route and ledger; generic instruction, installed-code and rebuilt-service paths remain owned by runtime.
