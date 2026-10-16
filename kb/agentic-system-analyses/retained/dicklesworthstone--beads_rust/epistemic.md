---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "beads_rust epistemic routes: issue assertions, scoped gate reports, policy admission and downstream reliance."
run-id: AAS-2026-10-16-beads-rust-e82d5506d2ff-01
reviewed-boundary: 53f7a3d30aca8cab3c3e4abdefeade459e8a3089
---

# beads_rust epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on retained issue assertions and derived workflow results. Scope and exclusions are those of [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not execution evidence. The tracker admits external assertions and makes deterministic workflow decisions. Neither storing an assertion nor calling an issue closed establishes its truth.

Coverage below distinguishes direct source inspection in this job from supplied runtime evidence. The whole-system functional boundary is unchanged, but this is a bounded material-route assessment, not an exhaustive negative about every shipped operation. No source access gap was encountered. Uninspected available implementations remain possible additional routes.

| Entry point or operation | SRC-1 source path | Coverage and records, or limit and conclusion prevented |
|---|---|---|
| CLI dispatch and write classification | `src/main.rs` | Direct dispatch/classification search; create, update, close, ready, import and instruction paths supported by supplied runtime records below. |
| Create, update/claim, close, JSONL import | `src/cli/commands/create.rs`, `src/cli/commands/update.rs`, `src/cli/commands/close.rs`, `src/sync/mod.rs` | Supplied [RT-RTE-create-issue](runtime.md#rt-rte-create-issue), [RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue), [RT-RTE-close-issue](runtime.md#rt-rte-close-issue), [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import). Not re-audited here. |
| Gate report and storage transition checks | `src/cli/commands/gate.rs`, `src/storage/sqlite.rs`, `src/close_policy.rs` | Direct report, effective-history query, evaluator and enforcing consumer reads; [EPI-RTE-gate-report](#epi-rte-gate-report), [EPI-RTE-gate-check](#epi-rte-gate-check), [EPI-RTE-gate-admission](#epi-rte-gate-admission). Material addition to runtime's selected routes. |
| Lint | `src/cli/commands/lint.rs` | Direct parser, classification and output reads; [EPI-RTE-lint-check](#epi-rte-lint-check). |
| Delete | `src/cli/commands/delete.rs` | Direct selected deletion loop and flush read; [EPI-RTE-delete-state](#epi-rte-delete-state). Full cascade and purge internals uninspected; prevents complete withdrawal/recovery guarantee. |
| Ready | `src/cli/commands/ready.rs` | Supplied [RT-RTE-ready-query](runtime.md#rt-rte-ready-query); snapshot policy result, not task-value evaluation. |
| MCP registrations and mutation wrapper | `src/mcp/mod.rs` | Direct registration search confirms seven tools, twelve resources, four prompts; wrapper supported by [RT-RTE-mcp-request](runtime.md#rt-rte-mcp-request). Registration is not an exhaustive handler audit. |
| MCP triage | `src/mcp/prompts.rs` | Supplied [RT-RTE-triage-prompt](runtime.md#rt-rte-triage-prompt) and [RT-BAP-triage-guidance](runtime.md#rt-bap-triage-guidance). |
| MCP status report, plan-next-work, polish-backlog; graph health/bottlenecks | `src/mcp/prompts.rs`, `src/mcp/resources.rs` | Registered alternatives identified. Polish instruction construction directly read, but upstream completeness/dependency analysis and other prompt/resource computations uninspected. Prevents complete classification of derived propositions and advisory judgments. |
| Agents update and binary upgrade | `src/cli/commands/agents.rs`, `src/cli/commands/upgrade.rs` | Supplied [RT-RTE-agents-update](runtime.md#rt-rte-agents-update), [RT-RTE-upgrade-binary](runtime.md#rt-rte-upgrade-binary). Version/checksum admission is not semantic verification. |
| Gate-independent close checks | `src/close_policy.rs` | Direct acceptance-checkbox evaluator read; consequences and bypass limits supplied by [RT-RTE-close-issue](runtime.md#rt-rte-close-issue). Checks recorded markup, not fulfillment. |
| Remaining CLI/library operations | `src/main.rs`, `src/cli/commands/`, `src/storage/`, `src/sync/` | Dispatch exposes comments, dependencies, epic closure, scheduler, audit, capacity, history restore/prune, doctor/repair, merge/reconcile, query/config and diagnostics. Bodies not fully inspected. These prevent system-complete negatives about evaluators, cleanup, recovery, adaptation or derivation. |
| Instructions, hooks and evaluators | `src/main.rs`, `.claude/skills/br/SKILL.md`, `scripts/`, `tests/`, `docs/` | Runtime supplies startup auto-import/flush and shipped instruction evidence. Development Git hooks excluded by boundary; no additional executable runtime-hook survey completed. Scripts/tests and maintenance qualifications not audited here; no test-pass, deployment-activation or causal-benefit conclusion. |

Knowledge/warrant claims assessed are [EPI-CLM-issue-tracking](#epi-clm-issue-tracking), [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle), and the narrower sync claim [RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync). No claim that br autonomously discovers true project facts is established by these passages. That is a statement about the cited claims, not a repository-wide absence.

Missing evidence matters separately: no supplied host/model trace establishes recommendations, compliance or learning; no source-linked execution establishes exercised gate acceptance; no intervention/comparison establishes productivity, correctness improvement or component effects. External evaluator methods behind provider strings are unspecified, preventing a task-correctness license from their pass reports. Distributed-parametric state belongs to an external host, not the inspected symbolic component [RT-CMP-beads-rust](runtime.md#rt-cmp-beads-rust); its weights, endpoint identity and mutability are not determinable here.

## Epistemic-object inventory

| object ID | candidate truth-apt content or none | claimed role | evidence source ID and local anchor | gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-issue-text](#epi-obj-issue-text) | Caller assertions about defects, requirements, implementation and completion; some text is imperative rather than truth-apt | Issue body and rationale | SRC-1 `src/close_policy.rs`; see record | Actual propositions and their external truth are not determinable without particular authored content and project evidence. |
| [EPI-OBJ-issue-state](#epi-obj-issue-state) | Assignment, status and dependency assertions over tracker state | Workflow state and readiness inputs | SRC-1 `src/storage/sqlite.rs`; see record | A stored status is authoritative tracker state, not proof of corresponding real-world work. |
| [EPI-OBJ-gate-result](#epi-obj-gate-result) | Provider's pass/fail assertion for an issue transition attempt | External evaluation report | SRC-1 `src/cli/commands/gate.rs`, `src/storage/sqlite.rs`; see record | Gate-specific external criterion, evaluator identity and assessment method unknown. |
| [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb) | Workflow prescriptions; no independent task-truth verdict | Installed instructions | See record | See [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions). |
| [EPI-RTE-lint-check](#epi-rte-lint-check) output | Missing-template-section propositions under a fixed parser | Diagnostic warning | SRC-1 `src/cli/commands/lint.rs` | Output is transient; semantics limited to parser predicate. |
| [RT-RTE-triage-prompt](runtime.md#rt-rte-triage-prompt) output | Selected backlog fields plus requests for judgment | Model-visible context | See record | Selection omits issues/fields; no resulting model judgments supplied. |

## Authority-route ledger

Rows are separate consequential functions, including linked rows for checks and their dispositions. Repeated record references reuse the declaring record rather than duplicate it. All observed-operation fields below remain uninspected; possible results are source deductions.

| route ID | route function | architectural status | object/candidate ID | content/update relation | transition or check target | evaluator/condition and domain | activation and timing | possible or observed result | implemented force | epistemic authority and scope | operational authority: behavior permitted, blocked, or changed | behavioral-authority path: consumer, channel, force, horizon | evidence source ID and local anchor | claim IDs or none | mismatch marker or none | gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-create-issue](runtime.md#rt-rte-create-issue), [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import) | content transformation | implemented | [EPI-OBJ-issue-text](#epi-obj-issue-text) | truth-apt transformation: acquisition/import | External issue content enters tracker | Caller authorship; structural/workflow admission, not truth evaluator | Request or configured import | Stored candidate or rejection | Admits fields | Source warrant unknown; no independent task truth license | Later queries can expose admitted assertions | Storage to CLI/MCP readers; informational, later invocations | See records | [EPI-CLM-issue-tracking](#epi-clm-issue-tracking) | none | Imported state bypasses some interactive checks. |
| [RT-RTE-create-issue](runtime.md#rt-rte-create-issue), [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import) | retention | implemented | [EPI-OBJ-issue-text](#epi-obj-issue-text), [EPI-OBJ-issue-state](#epi-obj-issue-state) | no content change | Admitted fields retained | Storage transaction/import writer | After admission | SQLite state; separate JSONL export lifecycle | Persistence | Retention alone licenses no semantic endorsement | Makes fields available to later readers | Persistent store to query/import consumers; informational and workflow inputs, across invocations | See records | [EPI-CLM-issue-tracking](#epi-clm-issue-tracking) | none | Export need not be committed with mutation. |
| [RT-RTE-ready-query](runtime.md#rt-rte-ready-query) | operational admission/selection/consumption | implemented | [EPI-OBJ-issue-state](#epi-obj-issue-state) | truth-apt transformation: entailed derivation | Eligibility under stored statuses, blockers, filters | Deterministic policy over current tracker inputs | Query snapshot | Eligible projected work list | Selection/ranking | Conditional readiness in represented graph, not objective priority or successful work | Offers candidates; reserves none | CLI/MCP result to caller, advisory selection, current snapshot | See record | [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle) | none | No warranted external dependency truth or future lease. |
| [EPI-RTE-gate-report](#epi-rte-gate-report) | retention | implemented | [EPI-OBJ-gate-result](#epi-obj-gate-result) | truth-apt transformation: acquisition/import | Caller-supplied verdict for scoped transition | Caller supplies status/provider; storage validates scope | Report request before transition | Append history and mirror latest verdict | Stores report | Source warrant unknown; records a report, not an independently established pass | Makes report eligible for gate checking | Scoped history to transition evaluator, permissive input, same attempt/revision | SRC-1 `src/cli/commands/gate.rs`, `src/storage/sqlite.rs` | none | none | Provider string does not establish authenticated independent reviewer. |
| [EPI-RTE-gate-check](#epi-rte-gate-check) | check/evidence production | implemented | [EPI-OBJ-gate-result](#epi-obj-gate-result) | truth-apt transformation: entailed derivation | Required gate/report predicate for transition | Fixed named-gate or reviewer-count rule over effective scoped results | During guarded transition preflight | Violations or no violations | Supplies policy verdict | Report-set sufficiency only | No mutation force until disposition consumer | Evaluator vector to storage preflight, enforcing input, current attempted update | SRC-1 `src/close_policy.rs`, `src/storage/sqlite.rs` | none | none | Named pass can coexist with another provider's fail; no universal veto. |
| [EPI-RTE-gate-admission](#epi-rte-gate-admission) | disposition/acceptance | implemented | [EPI-OBJ-issue-state](#epi-obj-issue-state) | no content change | Status transition against configured workflow | Storage consumes violations; see record | Non-bypass guarded update | Reject or permit continuation | Enforcing, conditional on path/policy | Acceptance of report sufficiency for transition; not acceptance of task explanation or code correctness | Blocks update with violations; otherwise permits downstream write checks | PolicyViolation or continuation within storage transaction, current mutation | SRC-1 `src/storage/sqlite.rs` | none | none | Other checks can still reject; bypass/import limits in runtime. |
| [EPI-RTE-gate-check](#epi-rte-gate-check) | lineage/freshness/recovery | implemented | [EPI-OBJ-gate-result](#epi-obj-gate-result) | truth-apt transformation: non-ampliative reshaping | Effective report set | Scope/revision selection; last report per case-folded gate/provider | On subsequent transition attempt | Old revision excluded; later same-provider fail replaces pass in effective set | Withdraws report's eligibility | Scope freshness, not refreshed external truth | Can prevent reuse of prior passing result | History query to gate evaluator, enforcing selection, current status revision | SRC-1 `src/storage/sqlite.rs` | none | none | Not a content-hash binding to all task evidence. |
| [RT-RTE-close-issue](runtime.md#rt-rte-close-issue) | check/evidence production | implemented | [EPI-OBJ-issue-text](#epi-obj-issue-text) | truth-apt transformation: entailed derivation | Supplied closure evidence and configured gates | Markup/reason/field checks; checkbox evaluator scans body fields | Close request | Violations or no violations | Supplies admission input | Syntactic/represented completion only | See record for close consumer | CLI/MCP gate result to close admission, enforcing except allowed bypass, request horizon | SRC-1 `src/close_policy.rs`; see runtime record | [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle) | none | Checked box is not verification of fulfilled criterion. |
| [RT-RTE-close-issue](runtime.md#rt-rte-close-issue) | disposition/acceptance | implemented | [EPI-OBJ-issue-state](#epi-obj-issue-state) | non-truth-apt policy/content update: closes workflow item | Closure admission | See record | Caller request and policy/bypass conditions | Closed/skipped/error | Workflow enforcement with explicit exceptions | Close is operational acceptance, not necessarily evidence-consuming acceptance of an ampliative claim | Removes item from ordinary active-work flow | Stored status to later queries, enforcing selection, until reopened/edited | See record | [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle) | none | Auxiliary metadata may fail after close. |
| [EPI-RTE-lint-check](#epi-rte-lint-check) | check/evidence production | implemented | [EPI-OBJ-issue-text](#epi-obj-issue-text) | truth-apt transformation: entailed derivation | Template-section presence | Fixed issue-type/Markdown predicate | Lint request | Missing sections and hints | Advisory output; human/quiet nonzero exit with warnings | Template presence only | Changes CLI diagnostic status, not issue state | Renderer to caller, advisory text/status, invocation | SRC-1 `src/cli/commands/lint.rs` | none | none | JSON/TOON return diagnostic data without warning exit; content correctness unchecked. |
| [RT-RTE-triage-prompt](runtime.md#rt-rte-triage-prompt) | content transformation | implemented | [EPI-OBJ-issue-text](#epi-obj-issue-text), [EPI-OBJ-issue-state](#epi-obj-issue-state) | truth-apt transformation: non-ampliative reshaping | Selected context plus static guidance | Focus filters/projections/caps | Host prompt request | Two user-role messages | Advisory | No new warrant from delivery | Requests review/recommendation, not automatic edits | See [RT-BAP-triage-guidance](runtime.md#rt-bap-triage-guidance) | See record | none | none | Any later conjecture/check/acceptance by host not determinable. |
| [EPI-RTE-delete-state](#epi-rte-delete-state) | retention | implemented | [EPI-OBJ-issue-state](#epi-obj-issue-state), [EPI-OBJ-issue-text](#epi-obj-issue-text) | non-truth-apt policy/content update: remove retained issue/dependency state | Caller-selected deletion set | Delete command dispatches tombstone or purge | Admitted delete operation | Removed links; tombstone or physical deletion | Alters retained state | Deletion is not epistemic refutation | Changes later graph/retrieval inputs | Store and export to later readers, enforcing retention change, subsequent invocations | SRC-1 `src/cli/commands/delete.rs` | none | none | Cascade policy and storage internals not fully inspected. |
| [RT-RTE-agents-update](runtime.md#rt-rte-agents-update), [RT-RTE-upgrade-binary](runtime.md#rt-rte-upgrade-binary) | behavior/policy adaptation | implemented | [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb), [RT-CMP-beads-rust](runtime.md#rt-cmp-beads-rust) | non-truth-apt policy/content update: replace shipped instructions or executable | Version/checksum/confirmation predicates | See records | Explicit maintenance request | Replacement, abort or error | Installation | Compatibility/integrity checks, not improvement warrant | Changes future instructions/machinery | See records and [RT-BAP-agent-instructions](runtime.md#rt-bap-agent-instructions) | See records | [RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync) | sync wording conflict, not an update-quality judgment | No task-evidence-driven revision or exercised improvement established. |

Lifecycle integration of accepted ampliative knowledge is not established by the inspected admission/retention paths. No separate lifecycle-integration route is inferred from retention, close status or later retrieval. Broader uninspected routes in the coverage table prevent a system-complete absence conclusion.

## System-claim versus route comparison

| claim ID | claimed operation or warrant | claim source ID/anchor and evidence layer | doctrine/design support | implemented route IDs | observed-run support | causal support and design limits | supported conclusion | mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-issue-tracking](#epi-clm-issue-tracking) | Local-first, dependency-aware issue tracking and agent-friendly workflows | SRC-1 `README.md`, doctrine/design | See record and boundary | [RT-RTE-create-issue](runtime.md#rt-rte-create-issue), [RT-RTE-ready-query](runtime.md#rt-rte-ready-query), [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import) | None supplied | No outcome comparison | Mechanisms support retained work state and conditional graph-based selection | Agent friendliness and workflow benefit not measured; no truth-oracle claim follows. |
| [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle) | Retrieve, claim, work, close, sync | See record, doctrine/design | Shipped instructions | [RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue), [RT-RTE-close-issue](runtime.md#rt-rte-close-issue), [EPI-RTE-gate-admission](#epi-rte-gate-admission) | None supplied | No compliance or success experiment | Work/status coordination exists; external work remains external | Ordinary status change is weaker than exclusive claim; closure not independent verification. |
| [RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync) | Sync never automatic | See record, doctrine/design | Official skill wording | [RT-RTE-create-issue](runtime.md#rt-rte-create-issue), [RT-RTE-mcp-request](runtime.md#rt-rte-mcp-request) | None supplied | Source-level counterexample, not causal evidence | Explicit sync remains useful operator advice | Universal wording contradicted by implemented automatic export. |

## Bounded conclusion

The inspected tracker acquires caller-authored assertions and workflow state, persists them, retrieves selected projections and computes conditional workflow predicates. External source warrant is unknown: structural validation, import consistency and a status field do not establish project truth. Ready results derive from represented state under policy; their deduction is conditional on those inputs, not independent proof that work is valuable or actually unblocked in the world.

A material evaluator omitted from the runtime's selected account is transition-scoped gate reporting. It retains externally supplied verdicts, derives report sufficiency and uses that result to permit or reject guarded status updates. Its criterion is named-gate pass or configured reviewer-count sufficiency; intended use and scope are a particular issue's current source-status revision and target transition. The storage consumer has enforcing force on non-bypass guarded updates. This operational acceptance must not be promoted to acceptance of the report's underlying correctness claim. A provider name and Boolean do not reveal the provider's test, authenticate independence or demonstrate evidence-consuming semantic acceptance.

Withdrawal is concrete but bounded: later same-provider reports replace earlier effective verdicts within scope, old status revisions cannot authorize a new attempt, and caller deletion removes issue/dependency state or leaves a tombstone. A different provider's fail does not universally cancel a named gate's pass. These countercases constrain claims about universal rejection, stale-pass safety and independent review. Imports and explicit policy bypass are separate admission routes. No universal evidence-enforcing gate is inferred.

Lint derives template-presence warnings; closure checks can detect unchecked criteria. Both assess recorded structure rather than whether implementation satisfies the criteria. Prompt delivery requests triage and revision but supplies neither exercised conjecture generation nor successful semantic checking. Particular host-produced propositions, their non-entailment and their acceptance are not determinable without host evidence. The report therefore does not classify unseen judgments as ampliative conjectures merely because reasoning was requested.

Instruction/executable replacement supplies direct future-behavior change without demonstrated truth-apt learning. The inspected evidence does not establish improved capacity, an evidence-responsive self-improvement cycle, exercised reflection, autonomy of external work or iterative content-directed theory criticism. Those are independent unestablished properties of the assessed routes, not one negative system verdict. Available but uninspected maintenance, diagnostic and prompt implementations prevent stronger completeness claims. No supplied execution or comparison establishes benefit or causal attribution.

## Shared records

### Operative objects

#### EPI-OBJ-issue-text
Label: Issue body fields

Source-native identity: issue `description`, `design`, `notes`, `acceptance_criteria`. Natural-language assertions and prescriptions; SQLite fields and JSONL serialization are substrates, not their representational form. Evidence: SRC-1 `src/close_policy.rs`; storage/admission supplied by [RT-RTE-create-issue](runtime.md#rt-rte-create-issue) and [RT-RTE-jsonl-import](runtime.md#rt-rte-jsonl-import). No counterpart object is declared in runtime: its issue routes operate on this material, while [RT-OBJ-agent-blurb](runtime.md#rt-obj-agent-blurb) is different installed guidance. This is not a part of that blurb.

>     let candidates = [
>         evidence.acceptance_criteria,
>         evidence.description,
>         evidence.design,
>         evidence.notes,
>     ];
> --- `src/close_policy.rs`

#### EPI-OBJ-issue-state
Label: Issue workflow state

Source-native identity: issue status, assignment and dependency state. Symbolic fields consumed by fixed query/transition rules, retained in SQLite and exported JSONL. Distinct from [EPI-OBJ-issue-text](#epi-obj-issue-text): different consumers and authority. Closest supplied records are [RT-RTE-claim-issue](runtime.md#rt-rte-claim-issue), [RT-RTE-ready-query](runtime.md#rt-rte-ready-query) and [RT-RTE-close-issue](runtime.md#rt-rte-close-issue), which describe operations rather than declare this object. SRC-1 `src/storage/sqlite.rs`; their passages support persistence and consumers.

>             workflow.validate_transition(Some(from), to, Some(prospective_type.as_str()))?;
> --- `src/storage/sqlite.rs`

#### EPI-OBJ-gate-result
Label: Scoped gate result

Source-native identity: `gate_result_history` records and effective `GateResult` verdict fields; the `gate_results` mirror is a separate current-state view, not the enforcing source. Symbolic scope/verdict/provider fields plus optional natural-language note, stored in SQLite. Notes accompany reports but the inspected sufficiency evaluator consumes names and Booleans rather than interpreting note truth. SRC-1 `src/storage/sqlite.rs`, `src/close_policy.rs`. No counterpart object in runtime; closest [RT-RTE-close-issue](runtime.md#rt-rte-close-issue) covers closure, not this reusable transition-scoped auxiliary store. Its persistence and authority are supported by the following route passages.

### Routes

#### EPI-RTE-gate-report
Label: Scoped gate reporting

Caller gate-report arguments → issue/status revision resolution → scope-checked history append and current-view mirror. Caller proposes and decides the external verdict; code can veto malformed names, missing issue, ambiguous target or changed scope. Human authorship/approval is unresolved. Operating mode is an open report request, not an experiment. No external answer oracle is specified by the provider string. SRC-1 `src/cli/commands/gate.rs`, `src/storage/sqlite.rs`. Distinct addition to [RT-RTE-close-issue](runtime.md#rt-rte-close-issue): reporting precedes and can serve non-close transitions; not a part of exactly that route.

- Immediate return: Serialized or human report confirmation, or error.
- Later read-back: History is read by transition checks and gate listing; latest mirror is available for current-state queries.
- Delegated visibility: No worker launched; caller receives reported scope and verdict.
- Selection predicate: Resolved issue, source status/revision, target, gate/provider and caller pass/fail.
- Invalidation or expiry: Later reports supersede effective same-provider verdicts; status revision changes exclude earlier scope.
- Activation or effect: Writes auxiliary report state, not the issue transition itself.
- Evidence limits: External assessment method and veracity uninspected; no observed invocation.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The proposed change is a report with optional note. Scope mismatch rejects before insertion; successful reports persist history rather than rolling back earlier reports. Later reports can change reliance. Mirror failure belongs to the same connection transaction; no general filesystem recovery guarantee is inferred.

>     let passed = matches!(args.status, GateStatus::Pass);
> --- `src/cli/commands/gate.rs`

>                 "INSERT INTO gate_result_history (
>                     issue_id, from_status, to_status, status_revision, gate,
>                     provider, passed, note, recorded_by, recorded_at
>                 ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)",
> --- `src/storage/sqlite.rs`

>             // enforcement never reads this table (it consults the scoped
>             // history above); the mirror keeps the documented current-state
>             // view populated for external queries. Runs after the
> --- `src/storage/sqlite.rs`

#### EPI-RTE-gate-check
Label: Effective gate checking

Scoped history → effective latest report set → required gate evaluation → violation vector. Code owns selection and fixed rule evaluation. Its target is report sufficiency for the requested issue transition, not the work product. SRC-1 `src/storage/sqlite.rs`, `src/close_policy.rs`. Distinct from [RT-RTE-close-issue](runtime.md#rt-rte-close-issue), which covers close as a whole rather than this arbitrary-edge check; paired with [EPI-RTE-gate-admission](#epi-rte-gate-admission), its separate consumer.

- Immediate return: Policy violation vector or empty vector to storage preflight.
- Later read-back: Reads accumulated gate history; no separate retained check result established here.
- Delegated visibility: Violations can propagate to caller; no delegation.
- Selection predicate: Same issue/from/to/status revision; ordered history folded by case-insensitive gate/provider; requirements depend on edge, labels and priority.
- Invalidation or expiry: Different status revision excludes prior reports; later reports replace effective earlier same-key verdicts.
- Activation or effect: Produces sufficiency and stale-revision diagnostics consumed by admission.
- Evidence limits: Validity of supplied report content remains unknown; no runtime trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller proposes a transition; policy selects requirements and code judges report-set compliance. No human veto or independent oracle is demonstrated inside the evaluator. Recovery is fresh reporting/retry, not an automatic external retest.

Concrete deduction, not target execution: for a named gate `tests`, same scoped provider `ci` reports pass then fail. The ascending-ID fold replaces the pass with fail, so that provider no longer supplies a satisfying pass. Add another provider's pass for `tests` in the same scope: the named-gate `any` predicate succeeds despite `ci`'s fail. Move both reports to an older status revision: neither enters the selected effective set for the current attempt. This demonstrates implemented conditional derivation and limits rejection semantics without asserting that tests actually ran or passed.

>                AND status_revision = ?
>              ORDER BY id ASC",
> --- `src/storage/sqlite.rs`

>             effective.insert(
>                 (gate.to_ascii_lowercase(), provider.to_ascii_lowercase()),
>                 result,
>             );
> --- `src/storage/sqlite.rs`

>         GateSpec::Named(name) => results
>             .iter()
>             .any(|result| result.gate.eq_ignore_ascii_case(name) && result.passed),
> --- `src/close_policy.rs`

#### EPI-RTE-gate-admission
Label: Guarded transition admission

Status update → configured gate check → violation rejection or continuation toward storage write. Storage owns disposition. SRC-1 `src/storage/sqlite.rs`. Closest supplied [RT-RTE-close-issue](runtime.md#rt-rte-close-issue) describes closure and bypasses; this route spans configured status edges rather than being identical to close. It consumes [EPI-RTE-gate-check](#epi-rte-gate-check), whose result alone has no mutation effect.

- Immediate return: PolicyViolation error or continuation of storage preflight; success here is not final mutation success.
- Later read-back: Admitted downstream mutation persists issue status; this admission branch alone retains no separate knowledge decision.
- Delegated visibility: Caller sees error or later update result; no worker launch.
- Selection predicate: Non-bypass update, gates enforced, matching transition rule and prospective labels/priority.
- Invalidation or expiry: Each attempted guarded transition checks current scope again; future edits or reopen change workflow state.
- Activation or effect: Nonempty violations reject update; empty gate violations permit further checks/write progression.
- Evidence limits: Bypass and import routes do not inherit a universal gate guarantee; no observed transition.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller proposes; installed workflow and storage decide; explicit bypass may override ordinary rejection as supplied by runtime. Intended use is workflow admission, criterion is required-report sufficiency, scope is current transition attempt. This is not a semantic task acceptance oracle. Recovery is reporting missing/fresh results or changing request/policy; rollback of later external work is not part of admission.

>             if workflow.gates_enforced() && workflow.gate_rule_for(from, to).is_some() {
> --- `src/storage/sqlite.rs`

>                 return Err(BeadsError::PolicyViolation {
>                     issue_id: id.clone(),
>                     summary,
>                     violations,
>                 });
> --- `src/storage/sqlite.rs:7630-7649`

#### EPI-RTE-lint-check
Label: Issue template lint

Selected issues → type-specific required sections → missing-section suggestions → output and diagnostic exit handling. Code owns the parser/evaluator, caller chooses query. SRC-1 `src/cli/commands/lint.rs`. No counterpart after comparison with supplied [RT-RTE-ready-query](runtime.md#rt-rte-ready-query): lint diagnoses template presence rather than eligibility.

- Immediate return: Missing section warnings/hints or no warnings, rendered as structured or human output.
- Later read-back: Reads retained issue fields; no persistent lint judgment written by inspected evaluator/output code.
- Delegated visibility: Output may reach an external host; no worker launched.
- Selection predicate: Caller IDs/filters, issue type, nonblank acceptance field or recognized named section with body.
- Invalidation or expiry: Subsequent issue edits require a fresh lint invocation.
- Activation or effect: Human/quiet warnings record nonzero diagnostic exit; JSON/TOON branches emit data and return before warning status handling.
- Evidence limits: No observed invocation; no claim about external automation's response to output.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Target: template completeness under the parser, not truth or adequacy. No answer oracle for task success. Concrete deduction: a Task with no description and nonblank acceptance text `do something` has its sole required section satisfied by `field_present`; the evaluator returns no lint warning even though no project evidence accompanies the text. An empty acceptance field and missing description yields the missing Acceptance Criteria section. This is an implementation deduction, not evidence of good criteria. Parser recognition also excludes a bare prose mention from standing in for a Markdown heading.

>     let missing = missing_sections(issue, required);
>     if missing.is_empty() {
>         return None;
>     }
> --- `src/cli/commands/lint.rs`

>                     .is_some_and(|criteria| !criteria.trim().is_empty());
>             !field_present
>                 && !description_has_section(description, strip_heading_prefix(section.heading))
> --- `src/cli/commands/lint.rs`

>         ctx.json_pretty(&output);
>         return;
> --- `src/cli/commands/lint.rs:168-176`

#### EPI-RTE-delete-state
Label: Delete retained state

Admitted deletion set → remove dependencies → tombstone or hard-purge dispatch → flush handling. Caller requests deletion and chooses flags; command/storage perform changes. SRC-1 `src/cli/commands/delete.rs`. Distinct from [RT-RTE-close-issue](runtime.md#rt-rte-close-issue): deletion/purge changes retained content and links, not merely completion status.

- Immediate return: Deletion result or error; selected code accumulates affected IDs and removed-link counts.
- Later read-back: Later queries and exports consume changed issue/dependency state; hard deletion is intended to prune JSONL.
- Delegated visibility: Cooperating readers can observe state after persistence/export; no worker launched.
- Selection predicate: Final deletion set produced by earlier command logic, then hard versus ordinary deletion flag.
- Invalidation or expiry: Tombstones or physical removal change future retention; complete merge/resurrection behavior uninspected.
- Activation or effect: Removes dependency links and invokes delete_issue or purge_issue; flush handling follows.
- Evidence limits: Earlier confirmation/cascade logic and lower-level purge implementation not fully inspected; no batch atomicity or permanent-erasure guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

This is operational withdrawal, not evidence-consuming rejection of a false claim. Human versus programmatic initiation is unresolved. No truth oracle; operating mode is an explicit maintenance request. Dry-run, refusal, undo and recovery guarantees cannot be established from this selected loop; no universal rollback inferred.

>         // Delete each issue (create tombstone, then purge if --hard)
> --- `src/cli/commands/delete.rs`

>                     |storage| storage.purge_issue(id, &actor),
> --- `src/cli/commands/delete.rs:310-319`

>                     |storage| storage.delete_issue(id, &actor, &args.reason, None),
> --- `src/cli/commands/delete.rs:320-328`

### Claims

#### EPI-CLM-issue-tracking
Label: Local-first issue tracking

Claimed operation: local-first persisted issue tracking with dependency-aware selection, machine-readable output, recovery and agent workflows. SRC-1 `README.md`, doctrine/design. Distinct from [RT-CLM-work-cycle](runtime.md#rt-clm-work-cycle), a specific prescribed lifecycle, and [RT-CLM-explicit-sync](runtime.md#rt-clm-explicit-sync), a narrower synchronization assertion. The claim does not by itself promise autonomous knowledge production.

> **br** is a local-first issue tracker that stores issues in SQLite with JSONL export for git-friendly collaboration. It provides dependency-aware issue tracking, machine-readable output, sync/recovery tooling, and agent-friendly workflows without leaving your repository.
> --- `README.md`
