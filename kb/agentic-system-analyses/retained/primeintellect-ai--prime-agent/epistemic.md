---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Prime Agent's content, refinement, review and shell-gate authority routes at the frozen commit."
run-id: AAS-2026-10-14-prime-agent-8ec59ae12476-01
reviewed-boundary: "33da15a2c15c4e903c372f69ae8e1156d77d53da"
---

# Prime Agent epistemic report

## Source-and-claim boundary

The question is how Prime Agent obtains truth-apt material, checks it and lets it influence current or later work. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. External providers, search results, MCP servers, user workloads and linked papers are not frozen. Their absence prevents judgments about source truth, exercised review, task outcomes and improvement. Provider parameters are see [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model): endpoint selection is inspectable, exact weights and provider adaptation are not.

The consequential public claim is [EPI-CLM-harness-improve](#epi-clm-harness-improve). The risk disclosure is see [RT-CLM-user-permissions](runtime.md#rt-clm-user-permissions). This report does not infer a system-wide lack of evaluation from open-ended tool execution: the shipped autonomous shell gates and PR-manager review loop are positive counterexamples. They add detail to, rather than supersede, the supplied runtime's continuation and factory containers.

| Entry point or operation | Source path | Coverage and records / prevented conclusion |
|---|---|---|
| Print/JSON, interactive, daemon, ACP, RPC dispatch | SRC-1: `crates/pa-cli/src/print_runtime.rs` | Direct dispatch read; invocation semantics supplied by [RT-RTE-print-prompt](runtime.md#rt-rte-print-prompt), [RT-RTE-daemon-session](runtime.md#rt-rte-daemon-session). Mode parity not established. |
| Registered Python tool and shell/MCP/host effects | SRC-1: `crates/pa-core/src/session_engine/runtime_wiring.rs` | Registration search; execution findings supplied by [RT-RTE-python-effects](runtime.md#rt-rte-python-effects). Individual MCP/third-party evaluators uninspected, preventing a complete negative about reachable checking. |
| Natural-turn-end hook and headless shell gates | SRC-1: `crates/pa-cli/src/print_autonomous.rs`, `crates/pa-cli/src/headless_autonomous.rs`, `crates/pa-core/src/autonomous/gates.rs`, `crates/pa-core/src/autonomous/driver.rs` | Direct reads of hook, driver and check/admission policy: [EPI-RTE-shell-check](#epi-rte-shell-check), [EPI-RTE-gate-disposition](#epi-rte-gate-disposition). Full daemon scheduling/recovery uninspected. |
| Manual/queued/automatic refine; reject, delete and rollback | SRC-1: `crates/pa-core/src/refinement/executor.rs`, `crates/pa-core/src/refinement/planner.rs`, `crates/pa-core/src/session_engine/refine.rs` | Direct planner/request reads and outcome/rollback searches, plus supplied [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine). No measured validation of improvement. |
| Direct harness writes and later digest | SRC-1: `prime-agent-runtime/src/rlm/harness.py`, `crates/pa-core/src/session_engine/harness_digest.rs`, `crates/pa-core/src/refinement/ranking.rs` | Supplied write/consumer account plus direct ranking read: [RT-RTE-python-effects](runtime.md#rt-rte-python-effects), [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest). Exact full-store delivery is not claimed. |
| Child spawn/collect, factory launch, capture and guards | SRC-1: `prime-agent-runtime/src/rlm/factory.py` | Direct capture/guard/transition reads supplement [RT-RTE-child-spawn](runtime.md#rt-rte-child-spawn), [RT-RTE-factory-run](runtime.md#rt-rte-factory-run), [EPI-RTE-port-capture](#epi-rte-port-capture), [EPI-RTE-factory-guard](#epi-rte-factory-guard). Other failure-policy branches not exhaustively traced. |
| Built-in builder, review-sweep and PR-manager | SRC-1: `prime-agent-runtime/src/rlm/machines/builder/MACHINE.md`, `prime-agent-runtime/src/rlm/machines/review-sweep/MACHINE.md`, `prime-agent-runtime/src/rlm/machines/pr-manager/MACHINE.md` | Direct complete template reads. [EPI-RTE-pr-review](#epi-rte-pr-review) establishes requested assessment and operational selection, not exercised review. Builder/report aggregation has no independently checked semantic fidelity. |
| Search import and formatting | SRC-1: `skills/websearch/src/websearch/websearch.py` | Direct complete read: [EPI-RTE-web-search](#epi-rte-web-search). Live Serper contents excluded. |
| Compaction, skill installation, release activation | SRC-1: `crates/pa-core/src/session_engine/compaction.rs`, `skills/skill-creator/SKILL.md`, `crates/pa-cli/src/update_flow/update_command.rs` | Supplied [RT-RTE-context-compact](runtime.md#rt-rte-context-compact), [RT-RTE-skill-install](runtime.md#rt-rte-skill-install), [RT-RTE-release-update](runtime.md#rt-rte-release-update); direct summarization-prompt search. No semantic equivalence, skill-content approval or complete release trust assessment. |
| Headless evaluator tests and other evaluation support | SRC-1: `crates/pa-cli/tests/eval_composition_e2e.rs`, `scripts/`, `.github/` | Test-name/assertion search confirms gate composition tests exist, not that they passed. Other evaluation scripts/workflows uninspected: no system-complete evaluation or causal-benefit conclusion. |

All added reads remain at SRC-1's frozen revision. Available uninspected evaluator variants, release coordinator internals and arbitrary executable tools prevent a system-complete negative. There is no supplied candidate instance whose provenance can establish actual production or acceptance.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-session-context](runtime.md#rt-obj-session-context) | Caller assertions, assistant answers, tool reports and compaction summaries; factual content depends on instance | see record | see record | Message envelopes do not authenticate embedded claims. Summary fidelity is not checked by the cited replacement code. |
| [EPI-OBJ-harness-memory](#epi-obj-harness-memory) | Facts, decisions, failures and outcome claims | see record | see record | No supplied contents or acquired-source warrant. |
| [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | Behavioral instructions are non-truth-apt; explanations embedded in them can be truth-apt | see record | see record | Effect by delivery is not compliance; installed-call references do not prove callable efficacy. |
| [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine) | Control graph itself is policy; child task/results can carry claims | see record | see record | Validation of graph syntax and references does not validate child claims. |
| [EPI-OBJ-verdict](#epi-obj-verdict) | PR has no merge-blocking defect; particular fixes landed; findings about defects | see record | see record | Model-produced boolean is not an external truth oracle. |
| [EPI-OBJ-gate-result](#epi-obj-gate-result) | Configured command exited successfully or failed under this run's conditions | see record | see record | License is bounded by command semantics and environment, not universal correctness. |
| [EPI-OBJ-search-results](#epi-obj-search-results) | Imported snippets, knowledge-graph assertions and suggested answers | see record | see record | Unknown upstream warrant; selected and potentially truncated text. |
| [RT-CMP-provider-model](runtime.md#rt-cmp-provider-model) | not determinable as individuated retained propositions | see record | see record | Opaque distributed-parametric state; no provider training or weight-update conclusion. |

## Authority-route ledger

Owned identity, timing, outcomes, consumers and evidence fields say `see` where the declaring record supplies them. Separate rows distinguish functions of valid route containers; a repeated route citation does not assert another referent.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-print-prompt](runtime.md#rt-rte-print-prompt) | content transformation | implemented | [RT-OBJ-session-context](runtime.md#rt-obj-session-context) | truth-apt transformation: indeterminate | Open task response | Model; no fixed answer oracle | see record | see record | see record | Candidate answer only; instances needed to distinguish reshaping, derivation and conjecture | see record | see record | see record | none | none | Generation is not acceptance; non-entailment not established from generic inference. |
| [EPI-RTE-web-search](#epi-rte-web-search) | content transformation | implemented | [EPI-OBJ-search-results](#epi-obj-search-results) | truth-apt transformation: acquisition/import | External search response | see record | see record | see record | see record | Acquired selected assertions, upstream warrant unknown | see record | see record | see record | none | none | URL attribution is not corroboration. |
| [RT-RTE-context-compact](runtime.md#rt-rte-context-compact) | content transformation | implemented | [RT-OBJ-session-context](runtime.md#rt-obj-session-context) | truth-apt transformation: indeterminate | Historical messages to summary | Model under fidelity instructions | see record | see record | see record | Requested compression; semantic preservation unestablished | see record | see record | see record | none | none | Source-supported faithful intent does not prove non-ampliative output. |
| [RT-RTE-context-compact](runtime.md#rt-rte-context-compact) | retention | implemented | [RT-OBJ-session-context](runtime.md#rt-obj-session-context) | no content change | Summary to later context | Successful compaction commit | see record | see record | see record | No added semantic warrant from persistence | see record | see record | see record | none | none | Separate from lifecycle integration after acceptance. |
| [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) | content transformation | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | truth-apt transformation: indeterminate | Trajectory/state/history to proposed facts; policy edits may instead be non-truth-apt | Model instructed to use evidence and rationale | see record | see record | see record | Evidence-directed candidate production is requested; generic edits cannot establish entailment or ampliation | see record | see record | see record | [EPI-CLM-harness-improve](#epi-clm-harness-improve) | none | No observed compliance or objective-level benefit. |
| [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) | check/evidence production | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | no content change | Proposal syntax, entry shape, reserved ID, baseline conflict, factory opt-in | Parser/validator under scoped store contract | see record | see record | see record | Admissibility, not factual truth or predicted improvement | see record | see record | see record | [EPI-CLM-harness-improve](#epi-clm-harness-improve) | none | Automatic model review asks whether to refine, not whether an applied edit improved capacity. |
| [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) | disposition/acceptance | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | no content change | Individually admissible edit to apply/reject | Software apply checks; no obligatory per-edit human veto | see record | see record | see record | Operational admission only; not evidence-consuming acceptance of fact truth | see record | see record | see record | [EPI-CLM-harness-improve](#epi-clm-harness-improve) | none | Reserved-base and stale-edit protections are route-scoped. |
| [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) | retention | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | no content change | Applied entry/history to store | see record | see record | see record | see record | Ledger retention before epistemic acceptance; no license from expectedOutcome | see record | see [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest) | see record | [EPI-CLM-harness-improve](#epi-clm-harness-improve) | none | State/history/session rows do not form one atomic transaction. |
| [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) | lineage/freshness/recovery | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | no content change | Faulty edit to rollback/update/delete | Caller-selected history; model may recommend replacement | see record | see record | see record | Withdrawal changes later availability, not retrospective truth | see record | see [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest) | see record | [EPI-CLM-harness-improve](#epi-clm-harness-improve) | none | Snapshot restoration is not proof external effects or previous reliance were undone. |
| [RT-RTE-python-effects](runtime.md#rt-rte-python-effects) | disposition/acceptance | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | no content change | Supplied entry to direct upsert | Helper shape checks; caller/model proposes | see record | see record | see record | No factual endorsement from locked saving | see record | see [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest) | see record | none | none | Alternate write path bypasses refiner diagnosis; direct filesystem writes can bypass helpers. |
| [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest) | operational admission/selection/consumption | implemented | [EPI-OBJ-harness-memory](#epi-obj-harness-memory), [EPI-OBJ-harness-policy](#epi-obj-harness-policy) | truth-apt transformation: non-ampliative reshaping | Merged entries to selected digest | Lexical relevance/limits; see record | see record | see record | see record | Selection and rendering establish no endorsement | see record | see record | see record | [EPI-CLM-harness-improve](#epi-clm-harness-improve) | none | Downstream gets a rendering, not guaranteed complete source content. |
| [EPI-RTE-shell-check](#epi-rte-shell-check) | check/evidence production | implemented | [EPI-OBJ-gate-result](#epi-obj-gate-result) | truth-apt transformation: entailed derivation | Process outcome to pass/fail classification | see record | see record | see record | see record | Predicate over process status/error/timeout; no wider claim about task truth | see record | see record | see record | none | none | Correctness of gate program and coverage of task criteria remain uninspected. |
| [EPI-RTE-gate-disposition](#epi-rte-gate-disposition) | disposition/acceptance | implemented | [EPI-OBJ-gate-result](#epi-obj-gate-result) | no content change | Gate result to continuation/stop | see record | see record | see record | see record | Evidence-consuming operational completion under configured command criterion, not explanation acceptance | see record | see record | see record | none | none | Cached failure is not a new measurement; external state can change independently of workspace snapshot. |
| [EPI-RTE-port-capture](#epi-rte-port-capture) | content transformation | implemented | [EPI-OBJ-verdict](#epi-obj-verdict) | truth-apt transformation: non-ampliative reshaping | Child answer to named output | see record | see record | see record | see record | Exact selected field extraction, not semantic endorsement | see record | see record | see record | none | none | Trailing-block precedence, capture caps and provisional exits affect lineage. |
| [EPI-RTE-pr-review](#epi-rte-pr-review) | check/evidence production | implemented | [EPI-OBJ-verdict](#epi-obj-verdict) | truth-apt transformation: indeterminate | PR diff/fix report against merge-blocking criteria | see record | see record | see record | see record | Scoped model judgment requested; an actual evidence-consuming approval remains unobserved | see record | see record | see record | none | none | A response schema alone cannot establish review fidelity. |
| [EPI-RTE-factory-guard](#epi-rte-factory-guard) | operational admission/selection/consumption | implemented | [EPI-OBJ-verdict](#epi-obj-verdict) | no content change | Parsed verdict to fixer/watcher state | see record | see record | see record | see record | Encoded boolean match only; does not corroborate approval | see record | see record | see record | none | none | Kernel-resident bounded loop; not automatic merge or durable acceptance archive. |
| [RT-RTE-skill-install](runtime.md#rt-rte-skill-install) | operational admission/selection/consumption | implemented | Skill body/package; see record | non-truth-apt policy/content update: instructions and executable capability | Discovered resources to later model/kernel | see record | see record | see record | see record | No content approval from discovery | see record | see record | see record | none | none | Full loader/rejection branches uninspected. |
| [RT-RTE-release-update](runtime.md#rt-rte-release-update) | check/evidence production | implemented | Candidate binary; see record | no content change | Candidate checksum/version against expected release | see record | see record | see record | see record | Integrity/version under trusted expected values, not improved task behavior | see record | see record | see record | none | none | Coordinator activation and independent origin trust uninspected. |

No lifecycle integration after accepted truth claims is established in these inspected harness routes. This is a bounded finding about their checks, not a negative about all possible tools or tasks. The PR-manager template supplies a review-and-revision protocol; neither its exercised approvals nor their subsequent epistemic integration are observed.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-harness-improve](#epi-clm-harness-improve) | see record | see record | Evidence-backed edits, constrained base prompt and rollback are requested | [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine), [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest) | None supplied | No variation/comparison or measured future capacity; direct writes/custom prompts remain alternate paths | Implemented trajectory-fed supplemental editing and later model delivery; requested evidence grounding | “Can improve” is improvement-directed capacity, not demonstrated benefit. “Never rewrites” holds for reserved-entry refinement, not every filesystem/API path. |
| [RT-CLM-user-permissions](runtime.md#rt-clm-user-permissions) | see record | see record | Explicit no-sandbox disclosure | [RT-RTE-python-effects](runtime.md#rt-rte-python-effects) | None supplied | Deployment isolation external | Broad execution permits task-specific evidence collection but supplies no universal truth gate | Actual deployed grant set unknown. |

No other consequential public knowledge-production warrant was established by this reading boundary. Built-in reviewer instructions are operational contracts, not independent claims of measured correctness.

## Bounded conclusion

Prime Agent acquires caller/tool/search assertions, generates model responses and retains histories, summaries and editable harness entries. Search formatting preserves selected URLs/snippets but omits other response material and can truncate the return. Upstream search warrant is unknown. Summaries and generic refinement edits remain semantically indeterminate without instances: requested faithful compression is not proof of preservation, and an opaque model call is not sufficient evidence of non-entailment. See [EPI-RTE-web-search](#epi-rte-web-search), [RT-RTE-context-compact](runtime.md#rt-rte-context-compact), [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine).

The refiner implements trace-fed candidate planning, scope/shape/conflict admission, persisted edits/history and withdrawal by delete/rollback. These checks license a store transition, not fact truth or predicted improvement. Direct upsert is a materially different admission path. Later digest delivery has model-interpreted advisory force across the entry's local/global horizon; relevance and clipping can reduce what the consumer receives. Policy edits can directly change behavioral guidance without producing a truth-apt claim. No obligatory content-level human veto is established by these routes. See [RT-RTE-python-effects](runtime.md#rt-rte-python-effects), [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest).

Evaluation is heterogeneous. Shell gates derive a bounded process-outcome predicate, then enforce continuation/stop and headless failure exit; their operational completion criterion is configured command success with no error or timeout. This is neither a general answer oracle nor a proof of the producer's explanation. PR-manager instead requests model assessment of diff correctness, regressions and test gaps, encodes approval, sends false to fixing and true to a watcher, and feeds a fix report back into the next review. This is an implemented candidate-check-revision protocol with separate symbolic control; observed evidence use, reliable criticism and acceptance remain unestablished. See [EPI-RTE-shell-check](#epi-rte-shell-check), [EPI-RTE-gate-disposition](#epi-rte-gate-disposition), [EPI-RTE-pr-review](#epi-rte-pr-review), [EPI-RTE-factory-guard](#epi-rte-factory-guard).

These results independently support retained adaptation and improvement-directed self-change affordances. They do not establish improved capacity, exercised self-improvement or a reflective/autonomous theory builder. For the harness claim, an independently specifiable objective is future task effectiveness, but no metric, workload or comparison is supplied. Planning from trajectory, organization mutation and a later guidance channel are wired; subsequent operation causally depending on the change and successful improvement are unobserved. Method-directed critique is requested, not evidenced as exercised. Remote parametric learning remains independently uninspected. No system-wide epistemic score or absence verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-harness-memory
Label: Harness memory entries

Source-native identity: `memory` kind of HarnessEntry. Representational form: natural-language facts, decisions and outcomes in symbolic keyed entries. Storage substrate: local/global harness JSON. Distinct from [RT-OBJ-session-context](runtime.md#rt-obj-session-context): curated editable entries, not historical message envelopes. Also overlaps the state endpoints of [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine), not its invocation identity. SRC-1: `crates/pa-core/src/refinement/executor.rs`, `crates/pa-core/src/refinement/planner.rs`; the planner enumerates the content kinds, while the supplied route establishes write/read-back.

> "Requested refinement scope: local. Prefer local continual harness edits for current task progress, temporary blockers, current-run coordination, and project facts that are not clearly reusable across Prime Agent sessions. Global entries in the overview are read-only context: do not propose update or delete edits for them; create a local entry instead if an override is needed."
> --- `crates/pa-core/src/refinement/executor.rs`

#### EPI-OBJ-harness-policy
Label: Harness behavioral entries

Source-native identity: supplemental `prompt`, `skill` and `subagent` entries (factory control is separately [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine)). Representational form: natural-language guidance with symbolic callable/reference/argument selectors. Storage substrate: local/global harness JSON; installed Python packages remain separate executable material. Distinct from [EPI-OBJ-harness-memory](#epi-obj-harness-memory) by policy/call consumption, and from [RT-OBJ-session-context](runtime.md#rt-obj-session-context) by editable store identity. Evidence is SRC-1: `crates/pa-core/src/refinement/planner.rs`, supplied [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) and [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest). No different check is inferred merely from an entry's name.

#### EPI-OBJ-verdict
Label: PR-manager verdict port

Part of: [RT-OBJ-factory-machine](runtime.md#rt-obj-factory-machine)

The parent includes the machine's model-interpreted tasks and typed output protocol. Source-native identity: `reviewing.verdict`, with `approved` and `findings`. Representational form: symbolic JSON claims produced from natural-language model assessment. Storage substrate: captured child answer and kernel factory entry outputs, not a durable truth-certified store. Evidence: SRC-1: `prime-agent-runtime/src/rlm/machines/pr-manager/MACHINE.md`, `prime-agent-runtime/src/rlm/factory.py`; passages under the review and capture routes.

#### EPI-OBJ-gate-result
Label: Autonomous gate result

Source-native identity: ChildProcessResult and AutonomousGateResult, plus last_gate_failure. Representational form: symbolic status/error/timeout fields and natural-language output. Storage substrate: runtime state, with headless continuation/status rows where surfaced. No counterpart after comparison with supplied [RT-OBJ-session-context](runtime.md#rt-obj-session-context): this is the evaluated process outcome before message rendering. SRC-1: `crates/pa-core/src/autonomous/gates.rs`; passages under shell check and disposition.

#### EPI-OBJ-search-results
Label: Websearch result text

Source-native identity: `websearch.run` return string. Representational form: natural-language snippets with symbolic URLs/labels in text. Storage substrate: Python return/tool result; no dedicated search archive in inspected implementation. Distinct from [RT-OBJ-session-context](runtime.md#rt-obj-session-context): import-side result before admission to conversation. SRC-1: `skills/websearch/src/websearch/websearch.py`; passage under web-search route.

### Routes

#### EPI-RTE-web-search
Label: Serper search import

Material part of the broad execution surface [RT-RTE-python-effects](runtime.md#rt-rte-python-effects), but distinct operation with a named source endpoint and formatter, not another eval invocation. Endpoints: query/API key to Serper HTTP response, selected text to Python caller and possibly the model via output. Owner: skill code for request/formatting; foreground model/caller for query and consumption. Formats knowledge graph, top organic results and selected questions, then caps return length. HTTP/parse failures become diagnostic output; missing credentials return setup guidance. Source warrant is unknown, and omission/truncation degrades completeness.

- Immediate return: Formatted search text or setup/error diagnostic.
- Later read-back: inapplicable — no separate retained-search store; later history use belongs to the session route if the caller emits this text.
- Delegated visibility: inapplicable — no child context is constructed here.
- Selection predicate: Caller query, num_results, max_output and source result ordering.
- Invalidation or expiry: New calls fetch anew; previously emitted results have no truth-expiry check here.
- Activation or effect: Import and delivery wired; reliance on returned assertions unobserved.
- Evidence limits: Live service/source truth excluded; only request, formatter and return inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Behavioral-authority path: Python caller receives data; foreground model only receives what the cell exposes, advisory force, current turn/history horizon. No evidence-consuming acceptance decision is performed by this formatter. SRC-1 implementation: `skills/websearch/src/websearch/websearch.py`.

> for i, result in enumerate((data.get("organic") or [])[:num_results]):
>     title = (result.get("title") or "").strip() or "Untitled"
>     lines = [f"Result {i}: {title}"]
>     link = (result.get("link") or "").strip()
>     if link:
>         lines.append(f"URL: {link}")
>     snippet = (result.get("snippet") or "").strip()
>     if snippet:
>         lines.append(snippet)
>     sections.append("\n".join(lines))
> --- `skills/websearch/src/websearch/websearch.py`

#### EPI-RTE-shell-check
Label: Autonomous shell checking

Part of: [RT-RTE-print-prompt](runtime.md#rt-rte-print-prompt)

Distinct check phase of the print invocation; broad runtime continuation account remains valid. Endpoints: configured gate command in session cwd to ChildProcessResult and pass/fail predicate. Owner: ShellGateRunner and quality-gate code. Target/domain: successful completion of configured commands under current environment, assessed by status zero with no error/timeout. Command-defined tests may assess task properties, but their scope and correctness cannot be inferred from exit status alone. Human/operator configures commands; model performs task changes; software evaluates. Operating mode: optional quality gates during open autonomous tasks, not a fixed benchmark oracle. No expected answer is inherent in this generic runner.

- Immediate return: Gate pass, failure or retry-exhaustion result to driver.
- Later read-back: Last failure/snapshot can suppress another measurement; continued task receives rendered failure output via disposition.
- Delegated visibility: inapplicable — shell child is not a delegated model context.
- Selection predicate: Autonomous enabled and commands configured; configured order, first failure wins.
- Invalidation or expiry: Changed workspace or absent snapshot permits rerun; failure state resets after successful commands.
- Activation or effect: Bounded check outcome wired; not observed on any actual task.
- Evidence limits: No target execution; configured gate bodies and external environment not supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The derivation is implementation-grounded: a returned status 0, error None and timed_out false enters the success branch. These are warranted hypothetical inputs for a formal predicate deduction, not observed process facts. SRC-1: `crates/pa-core/src/autonomous/gates.rs`.

> if result.status == Some(0) && result.error.is_none() && !result.timed_out {
>     state.gate_attempts.insert(command.clone(), 0);
> --- `crates/pa-core/src/autonomous/gates.rs`

#### EPI-RTE-gate-disposition
Label: Gate-controlled continuation

Part of: [RT-RTE-print-prompt](runtime.md#rt-rte-print-prompt)

Distinct from [EPI-RTE-shell-check](#epi-rte-shell-check): consumes check outcomes instead of measuring. Endpoints: gate result/limits to driver Continue/Stop, model continuation or headless exit. Owner: AutonomousDriver and HeadlessAutonomous. Pass stops; failure continues within retry/budget bounds, otherwise stops and headless failure contract produces nonzero exit. Caller selects gate policy, software can veto continuation, model is prompted to repair. A failed same-workspace consult increments attempts without rerunning the command. This is operational admission against configured checks, not general epistemic endorsement.

- Immediate return: Continue text or Stop reason/status; enclosing print caller reports failure exit when appropriate.
- Later read-back: Failure feedback enters following model turn; status/continuation records can enter retained session history.
- Delegated visibility: Inline-child unsettled work defers continuation; goal arm can take priority.
- Selection predicate: Enabled mode, normal settled turn, gate result and continuation/token/time/retry limits.
- Invalidation or expiry: Gate success clears failure; limits terminate continuation; no rollback of task effects is implied.
- Activation or effect: Stop/continue enforcing in driver; repair text advisory to model; exercised repair unobserved.
- Evidence limits: Print/core policy inspected, not complete transport or scheduler parity; workspace equality does not cover live external state.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Behavioral-authority path: code driver via result enum, enforcing for next-turn permission; foreground model via failure continuation, advisory repair guidance; headless caller via exit contract, reporting force. Horizon: current autonomous invocation. SRC-1: `crates/pa-core/src/autonomous/driver.rs`, `crates/pa-core/src/autonomous/gates.rs`, `crates/pa-cli/src/headless_autonomous.rs`, `crates/pa-cli/src/print_autonomous.rs`.

> AutonomousDecisionReason::NotNeeded => {
>     // Gates evaluated and passed (mode/stop-reason cases were
>     // handled above).
>     AutonomousFollowUp::Stop {
>         reason: AutonomousStopReason::GatePassed,
>         status: Box::new(autonomous_status(state)),
>     }
> }
> --- `crates/pa-core/src/autonomous/driver.rs`

> failure.exit_text =
>     "not rerun: workspace unchanged since previous failed gate".to_string();
> --- `crates/pa-core/src/autonomous/gates.rs`

#### EPI-RTE-port-capture
Label: Factory output capture

Part of: [RT-RTE-factory-run](runtime.md#rt-rte-factory-run)

Endpoints: settled child answer to declared text/JSON ports and capture errors. Owner: FactoryExecutor. Text retains captured answer; JSON scans trailing fences first for a named field, then whole answer. Capture is capped and may fall back to preview. Failed/cancelled exits can preserve provisional text, not count as done; real settlement supersedes provisional capture. Missing ports trigger one recollection and record failure; input binding fails on recorded capture errors, and guards fail when a value is missing. This is operational lineage/recovery, not truth adjudication.

- Immediate return: Outputs/error map and capture events in kernel state.
- Later read-back: inapplicable — ordinary kernel-resident run state, not accumulated memory across invocations; child collect may reread retained child result during recovery.
- Delegated visibility: Selected port values feed downstream child inputs; no full-transcript inheritance.
- Selection predicate: Declared output name/type, successful settle, trailing matching JSON block precedence.
- Invalidation or expiry: Retry can replace incomplete capture; genuine settlement clears provisional marker; kernel loss ends run registry.
- Activation or effect: Port binding and deterministic failures wired; actual machine execution unobserved.
- Evidence limits: No claim that selected answer is true, complete or independent; caps can discard material.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deterministic trace, without target execution: answer `{"verdict":{"approved":true,"findings":[]}}` has no fenced candidate, parses as a dict containing `verdict`, and yields exactly the nested object. With guard output `verdict`, path `approved`, op `eq`, value true, dictionary traversal finds true and JSON-strict comparison succeeds. It would fail if the actual field were numeric 1. The transition consumer then admits the watcher, subject to run bounds. This proves the code's selection predicate, not the PR's acceptability. SRC-1 implementation: `prime-agent-runtime/src/rlm/factory.py`.

> if isinstance(parsed, dict) and output_name in parsed:
>     return parsed[output_name], None
> --- `prime-agent-runtime/src/rlm/factory.py`

> if isinstance(actual, bool) or isinstance(expected, bool):
>     return isinstance(actual, bool) and isinstance(expected, bool) and actual is expected
> --- `prime-agent-runtime/src/rlm/factory.py`

> if child_reason is not None:
>     # The exit capture (the M4 class): an exited child's last
>     # assistant text — whatever the exit envelope carried — is a
>     # PROVISIONAL answer. The child may have finished its work and
>     # died without reporting; the answer is preserved on the
>     # instance and the state reads needs-verify instead of silently
>     # counting the exit as settled work.
> --- `prime-agent-runtime/src/rlm/factory.py`

#### EPI-RTE-pr-review
Label: PR-manager model review

Part of: [RT-RTE-factory-run](runtime.md#rt-rte-factory-run)

Endpoints: bound PR URL and optional fix report to reviewer child, diff assessment and verdict. Owner: template supplies task, child model judges, factory handles output and progression. Target/domain: merge-blocking correctness defects, regressions and test gaps in a named PR; when fix report exists, whether stated fixes landed. No external reference-answer oracle is specified. Human/caller starts/enables factory; no mandatory per-verdict human veto is present in the template. Model proposes findings; encoded approval is later consumed by the guard. Criterion/intended use/scope are stated, but actual evidence consumption and acceptance decision are not observed.

- Immediate return: Child answer intended to contain verdict.approved and findings.
- Later read-back: Optional fix_report from latest fixing settlement is supplied to next reviewer re-entry; live run state only, not a durable review archive.
- Delegated visibility: Reviewer gets PR URL and selected fix report; fixer gets verdict; watcher gets PR URL.
- Selection predicate: PR-manager reviewing state entered from entry or fixing; explicit diff/fix-review task.
- Invalidation or expiry: Next review can replace prior verdict for later transitions; max_entries/budget bound rounds.
- Activation or effect: Review instruction and guarded feedback path implemented; exercised assessment or successful fixes unobserved.
- Evidence limits: Template plus shared factory implementation, not a PR trace; prompt compliance and quality cannot be established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Guidance persists as static machine template, with verdict/fix_report as current-run products. The fixer is asked to make targeted changes and run relevant tests; fixing is an external work-product update, not by itself Prime Agent self-improvement. Behavioral-authority path: child model via task text, advisory interpreted guidance; downstream factory through encoded verdict, enforcing state choice within one run. SRC-1: `prime-agent-runtime/src/rlm/machines/pr-manager/MACHINE.md`.

> "prompt": "Review the pull request at {pr_url} for merge-blocking defects. Fetch the diff with `gh pr diff` and judge correctness, regressions, and test gaps. When a fix report is bound below, verify the described fixes landed instead. Return a fenced json block of the form {\\\"verdict\\\": {\\\"approved\\\": <true|false>, \\\"findings\\\": [\\\"one sentence per finding\\\"]}}. Output only the json block.",
> --- `prime-agent-runtime/src/rlm/machines/pr-manager/MACHINE.md`

#### EPI-RTE-factory-guard
Label: Factory verdict selection

Part of: [RT-RTE-factory-run](runtime.md#rt-rte-factory-run)

Endpoints: captured output map to outgoing transition match and next-state admission. Owner: FactoryExecutor. Target/domain: declared field/operator comparison, not truth of reviewer assessment. Distinct from model review and port capture; implements the symbolic force summarized by [RT-BAP-machine-guards](runtime.md#rt-bap-machine-guards). In PR-manager false goes to fixing, true to monitoring; fixing returns to review. No automatic PR merge is declared by this template. Code vetoes malformed/unbound comparisons and run bounds; caller can resume a paused run, but this is not approval of claim truth.

- Immediate return: Transition fires, skips, blocks or pauses with event/state change.
- Later read-back: inapplicable — one kernel-resident run's progression; stored machine reuse is separately described by the runtime.
- Delegated visibility: Entered states receive selected bound inputs, not complete upstream context.
- Selection predicate: Queued settle, matching guard, target max_entries and run max_transitions.
- Invalidation or expiry: Consumed settle not re-evaluated; pause preserves resume position; new settlement supplies a new comparison.
- Activation or effect: Enforcing state selection wired; truth-correlated selection unobserved.
- Evidence limits: No independent reviewer warrant, merge action or durable replay established.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Behavioral-authority path: FactoryExecutor via parsed boolean/output map and transition table, enforcing next-state eligibility, one kernel-resident run. Content/update relation is no content change. SRC-1: `prime-agent-runtime/src/rlm/factory.py`, `prime-agent-runtime/src/rlm/machines/pr-manager/MACHINE.md`.

> when = transition.get("when")
> if when is not None and not _guard_passes(when, outputs):
>     continue
> --- `prime-agent-runtime/src/rlm/factory.py`

### Claims

#### EPI-CLM-harness-improve
Label: Harness improvement claim

Claimed operation: useful context/reusable patterns outlive a window; refine reviews trajectory and can apply small evidence-backed supplemental updates, preserves base prompt and supports rollback. Distinct from supplied [RT-CLM-user-permissions](runtime.md#rt-clm-user-permissions), which discloses execution risk rather than warrant. SRC-1 doctrine/design: `README.md`. The relevant implementation/limits are supplied by [RT-RTE-harness-refine](runtime.md#rt-rte-harness-refine) and [RT-BAP-harness-digest](runtime.md#rt-bap-harness-digest).

> - **The harness can improve:** `/refine` reviews the current trajectory and can apply small, evidence-backed updates to supplemental harness state. It never rewrites the immutable base system prompt, and recorded snapshots support rollback.
> --- `README.md`
