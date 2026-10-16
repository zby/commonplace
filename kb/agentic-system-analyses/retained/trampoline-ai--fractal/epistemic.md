---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Fractal epistemic routes: task-result reliance, retained trajectory, operational checks and the limits of context and verification claims."
run-id: AAS-2026-10-14-fractal-ee03010af4c2-01
reviewed-boundary: "6a226e7d539e229b5c7cc9ffa3b05ab1c8f00385"
---

# Fractal epistemic report

## Source-and-claim boundary

Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identity and layers: see the [Source register](boundary.md#source-register). The question is which truth-apt content Fractal acquires, transforms, checks and licenses for later reliance, rather than whether a terminal turn returns normally. SRC-1 supplies implementation and doctrine/design only. No target invocation, tests, provider requests or examples were executed.

Assessed families are task-result conversion and status, retained trajectory consumption, root instruction import, registered runtime observations, provider diagnostics and configuration admission, version notifications, and development evaluators. PredictRLM's internal content generation, recursive aggregation, verification and context rewriting remain external and uninspected. User projects, model weights, actual execution traces and comparison experiments are missing. These respectively prevent specific task-claim truth judgments, parameter-learning judgments, exercised acceptance/reliance judgments, and causal benefit judgments. The illustrated README trace explicitly calls itself a pseudo trace; it is not supplied execution evidence.

The consequential capability/warrant claims are [EPI-CLM-context-rot](#epi-clm-context-rot), [EPI-CLM-readable-trace](#epi-clm-readable-trace), and [EPI-CLM-trustworthy-usage](#epi-clm-trustworthy-usage). The requested verification policy is distinguished from implemented answer grading below. This is not a system-complete negative about all possible epistemic work: arbitrary workspace code and external tools can contain additional evaluators.

| Entry point or operation | Source path | Coverage and conclusion limit |
| --- | --- | --- |
| CLI dispatch; headless and TUI task turns; direct Python API | SRC-1, `src/fractal/cli.py`, `src/fractal/agent/service.py`, `src/fractal/runtime.py`, `src/fractal/tui/app.py` | Directly read dispatch, adapter and runtime submit; TUI details supplied by [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent), [RT-RTE-interactive-interrupt](runtime.md#rt-rte-interactive-interrupt). |
| Signature, root guidance, filesystem and document skills | SRC-1, `src/fractal/agent/signature.py`, `src/fractal/agent/skills.py`, `src/fractal/agent/service.py` | Signature and service read directly; filesystem search/read/write guidance inspected. [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance). External document skill implementation uninspected: no semantic extraction guarantee. |
| Save/load/resume, summary and bounded history, fallback | SRC-1, `src/fractal/session.py`, `src/fractal/runtime.py` | Direct source reads; [EPI-RTE-summary-render](#epi-rte-summary-render), [RT-OBJ-session-state](runtime.md#rt-obj-session-state), [RT-RTE-budget-exhaustion](runtime.md#rt-rte-budget-exhaustion). |
| Hook registration, reduction and observer callbacks | SRC-1, `src/fractal/events.py`, `src/fractal/runtime.py`, `src/fractal/agent/service.py` | Direct reads across target lists, tracker dispatch, compound suppression, file reducer and callback handling; [EPI-RTE-event-projection](#epi-rte-event-projection). |
| Config show/get/status/setup/set/unset/reset | SRC-1, `src/fractal/config_commands.py`, `src/fractal/connectivity.py` | Direct dispatch, status/setup/set/connectivity reads; [EPI-RTE-provider-check](#epi-rte-provider-check). Other config mutation/read routes supplied by [RT-RTE-config-change](runtime.md#rt-rte-config-change); no claim of exhaustive credential security. |
| Startup version notification | SRC-1, `src/fractal/version_check.py`, `src/fractal/cli.py` | Entire notifier and CLI dispatch read directly; [EPI-RTE-version-notice](#epi-rte-version-notice). |
| CI tests and package release | SRC-1, `.github/workflows/tests.yml`, `tests/test_session.py`, `.github/workflows/release.yml` | Test workflow and round-trip evaluator directly read; [EPI-RTE-contract-tests](#epi-rte-contract-tests). Release coverage supplied by [RT-RTE-package-release](runtime.md#rt-rte-package-release). Remaining test bodies uninspected, preventing exhaustive evaluator coverage. |
| Bundled host calling recipes | SRC-1, `.agents/skills/fractal/RECIPES.md` | Delegation/resume, CI gate, structured-output and independent-diff guidance directly read. Doctrine only, not a host execution trace. |
| Provider internals, context-meter heuristics, installation/setup details | SRC-1, `src/fractal/providers.py`, `src/fractal/context_meter.py`, `src/fractal/onboarding.py`, `install.sh` | Supplied runtime coverage or available but not exhaustively inspected. No full operational/security audit or complete negative about auxiliary diagnostics follows. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-agent-turn](#epi-obj-agent-turn) | Response may assert edits, diagnoses or task answers; particular propositions not determinable without an instance | see cited record | SRC-1, `src/fractal/session.py` | Structural success is not answer acceptance. |
| [EPI-OBJ-session-summary](#epi-obj-session-summary) | User requests, prior responses, status and operation counts | see cited record | SRC-1, `src/fractal/session.py` | Requests/policies need not be truth-apt; trace-derived and model-derived parts keep different warrant. |
| [RT-OBJ-session-state](runtime.md#rt-obj-session-state) | Detailed history includes file/command names and opaque trace contents | see cited record | SRC-1, `src/fractal/session.py` | Last 20 history turns, not complete exact recall across an arbitrarily long session. |
| [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace) | Static instructions are policies; imported root guidance may mix claims and policies | see cited record | SRC-1, `src/fractal/agent/signature.py` | User origin is not endorsement of factual content; compliance unobserved. |
| [EPI-OBJ-runtime-event](#epi-obj-runtime-event) | A hook target/phase/argument was reported; reduced file/command observations | see cited record | SRC-1, `src/fractal/events.py` | No complete diff or semantic task test; before-phase commands are not evidence of completion. |
| [EPI-OBJ-version-cache](#epi-obj-version-cache) | Website reports a latest release identifier; installed package version | see cited record | SRC-1, `src/fractal/version_check.py` | Provider assertion, not authenticated package availability or quality. |
| [RT-CMP-main-lm](runtime.md#rt-cmp-main-lm), [RT-CMP-sub-lm](runtime.md#rt-cmp-sub-lm) | Internal representations not individuable from these sources | see cited records | SRC-1, `src/fractal/agent/service.py` | Weights and internal updates uninspected; adapter replacement is not training. |

## Authority-route ledger

The following entries are a sparse overlay. Fields owned by declaring records say `see`; assessments of warrant and architectural status are local. No observed-run result is asserted.

Route ID: [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-RTE-direct-agent](runtime.md#rt-rte-direct-agent)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-agent-turn](#epi-obj-agent-turn)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Task input/workspace to response and edits; particular claims not determinable.
Evaluator/condition and domain: Model generation delegated to PredictRLM; no entailment or non-entailment test of a concrete response in Fractal.
Activation and timing: see cited routes.
Possible or observed result: see cited routes; possible string response and mutable file effects.
Implemented force: Delegation and direct editing, not semantic verification.
Epistemic authority and scope: Candidate task answer; no checked source truth or general mechanism warrant established by the adapter.
Operational authority: behavior permitted, blocked, or changed: Execution is permitted under task instructions before result conversion.
Behavioral-authority path: consumer, channel, force, horizon: Workspace executor through delegated code; permissive invocation scope. Later response consumption is separated below.
Evidence source ID and local anchor: SRC-1, `src/fractal/agent/service.py`; see cited routes for passages.
Claim IDs or none: [EPI-CLM-readable-trace](#epi-clm-readable-trace)
Mismatch marker or none: Inner generation and verification implementation uninspected.
Gap/limit: Imported workspace claims may be acquired; entailment, conjecture and acceptance cannot be assigned to opaque generated content solely because it is model output.

Route ID: [RT-CLM-result-contract](runtime.md#rt-clm-result-contract), [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-agent-turn](#epi-obj-agent-turn)
Content/update relation: no content change
Transition or check target: Returned response string, list of changed-file strings and optional RunTrace type.
Evaluator/condition and domain: Python isinstance checks; adapter structure only.
Activation and timing: After predictor return, before FractalResult construction.
Possible or observed result: Valid shape or TypeError; see cited records.
Implemented force: Structural failure prevents adapter return.
Epistemic authority and scope: The fields have the expected Python types, not that edits occurred or the answer is true.
Operational authority: behavior permitted, blocked, or changed: Invalid shape enters outer failure handling; valid shape proceeds to classification/output.
Behavioral-authority path: consumer, channel, force, horizon: Adapter caller, exception/typed result, enforcing current return; does not undo earlier direct edits.
Evidence source ID and local anchor: SRC-1, `src/fractal/agent/service.py`; see cited claim's passages.
Claim IDs or none: [RT-CLM-result-contract](runtime.md#rt-clm-result-contract)
Mismatch marker or none: none
Gap/limit: The signature's request to verify important edits is policy, not this check's criterion.

Route ID: [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-RTE-budget-exhaustion](runtime.md#rt-rte-budget-exhaustion), [RT-RTE-interactive-interrupt](runtime.md#rt-rte-interactive-interrupt)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-agent-turn](#epi-obj-agent-turn)
Content/update relation: no content change
Transition or check target: Outer turn completion state, not truth of task answer.
Evaluator/condition and domain: Runtime branch on exceptions, interruption predicate and trace.status == max_iterations.
Activation and timing: see cited routes.
Possible or observed result: succeeded, failed, interrupted or max_iterations; see cited routes.
Implemented force: Determines saved state and public status/exit behavior; budget fallback remains retained.
Epistemic authority and scope: Operational classification only. It is not an evidence-consuming acceptance of an ampliative claim against a task criterion.
Operational authority: behavior permitted, blocked, or changed: Caller sees normal or incomplete/error termination and can continue; no workspace rollback.
Behavioral-authority path: consumer, channel, force, horizon: CLI/TUI and later session model, status/error and exit channel; enforcing current exit, advisory future context. Headless and TUI cancellation differ as cited.
Evidence source ID and local anchor: SRC-1, `src/fractal/runtime.py`, `src/fractal/cli.py`; see cited passages.
Claim IDs or none: none
Mismatch marker or none: succeeded does not mean verified task completion.
Gap/limit: Host interpretation of exit codes is external; the bundled CI recipe branches on exit, but is not observed operation.

Route ID: [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [RT-OBJ-session-state](runtime.md#rt-obj-session-state)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-agent-turn](#epi-obj-agent-turn), [EPI-OBJ-session-summary](#epi-obj-session-summary)
Content/update relation: no content change
Transition or check target: Returned response and failure/budget/interruption metadata into checkpoint.
Evaluator/condition and domain: Automatic host persistence, not epistemic acceptance.
Activation and timing: see cited route.
Possible or observed result: Stored candidate and outcome metadata; see cited records.
Implemented force: Retains successful and unsuccessful turn context alike.
Epistemic authority and scope: Source distinctions remain model response versus host status/accounting; persistence adds no truth warrant.
Operational authority: behavior permitted, blocked, or changed: Resume and later submit can use retained content.
Behavioral-authority path: consumer, channel, force, horizon: Session loader to later model invocation; delivery only until consumption described below.
Evidence source ID and local anchor: SRC-1, `src/fractal/session.py`, `src/fractal/runtime.py`; see cited records and summary-render record.
Claim IDs or none: [EPI-CLM-trustworthy-usage](#epi-clm-trustworthy-usage)
Mismatch marker or none: Retention is not lifecycle integration after acceptance.
Gap/limit: No evidence-linked claim admission demonstrated by this checkpoint writer; other workspace evaluators remain possible.

Route ID: [EPI-RTE-summary-render](#epi-rte-summary-render)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-session-summary](#epi-obj-session-summary)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Stored user/agent fields to prompt text and counts.
Evaluator/condition and domain: Deterministic renderer and list lengths; see cited record's concrete deduction.
Activation and timing: see cited record.
Possible or observed result: see cited record.
Implemented force: Produces always-visible session text; reduces detailed observations to counts without validating their contents.
Epistemic authority and scope: Preserves response text and status attribution at the field level, not semantic verification or original filesystem evidence.
Operational authority: behavior permitted, blocked, or changed: Later model can rely on earlier response and status even when detailed history has expired.
Behavioral-authority path: consumer, channel, force, horizon: Per-turn signature, instruction text, advisory model context over the retained session; no compliance trace.
Evidence source ID and local anchor: SRC-1, `src/fractal/session.py`, `src/fractal/agent/signature.py`.
Claim IDs or none: [EPI-CLM-context-rot](#epi-clm-context-rot)
Mismatch marker or none: Summary is not a semantic condensation of response prose in the inspected Fractal renderer.
Gap/limit: Removing path/command details degrades exact-evidence access when the bounded history tail drops them; all summary turns remain rendered.

Route ID: [RT-BAP-workspace-guidance](runtime.md#rt-bap-workspace-guidance)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-edit-workspace](runtime.md#rt-obj-edit-workspace)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Root AGENTS.md into per-turn instructions, where it may carry truth-apt claims or policies.
Evaluator/condition and domain: Read/decode/length handling; see cited record.
Activation and timing: see cited record.
Possible or observed result: Imported text, omission or truncated prefix; see cited record.
Implemented force: User-message-precedence instruction policy.
Epistemic authority and scope: External source warrant unknown; truncation can remove qualifications. No factual endorsement check.
Operational authority: behavior permitted, blocked, or changed: Model is asked to follow retained workspace guidance; current user_message takes precedence.
Behavioral-authority path: consumer, channel, force, horizon: see cited record.
Evidence source ID and local anchor: SRC-1, `src/fractal/agent/service.py`, `src/fractal/agent/signature.py`.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Arbitrary guidance content is not supplied; policy compliance and self-modification remain unobserved.

Route ID: [EPI-RTE-event-projection](#epi-rte-event-projection)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-runtime-event](#epi-obj-runtime-event)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Scoped hook events to unique paths, command strings and operation counts.
Evaluator/condition and domain: Symbolic phase/target/argument reducer; event report domain, not complete host effects.
Activation and timing: see cited record.
Possible or observed result: see cited record.
Implemented force: Accounting/display only, no edit veto.
Epistemic authority and scope: Counts derive from lists under event availability assumptions. A before command establishes admission of an attempted call, not completion; file after events establish reported operations, not semantic edits.
Operational authority: behavior permitted, blocked, or changed: Accumulated observations become summary/history and live display.
Behavioral-authority path: consumer, channel, force, horizon: Runtime session writer and CLI/TUI; accounting channel advisory, current turn and later session context.
Evidence source ID and local anchor: SRC-1, `src/fractal/events.py`, `src/fractal/runtime.py`, `src/fractal/session.py`.
Claim IDs or none: [EPI-CLM-trustworthy-usage](#epi-clm-trustworthy-usage), [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting)
Mismatch marker or none: Host-derived does not mean exhaustive or independent of external trace correctness.
Gap/limit: Runtime persists result.changed_files, not the tracker's files_modified list, on normal return. Failed/interrupted branches omit changed-file input. Therefore persisted changed-file counts are not a hook-certified diff.

Route ID: [EPI-RTE-provider-check](#epi-rte-provider-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: none; transient provider diagnostic
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Configured provider endpoint's response to a cheap authenticated GET.
Evaluator/condition and domain: HTTP/error classification; endpoint/credential connectivity at request time, not generation ability or sub-model performance.
Activation and timing: see cited record.
Possible or observed result: True, False for unsupported check, or connectivity error.
Implemented force: Diagnostic result handed to status/setup; disposition is separate below.
Epistemic authority and scope: Only tested endpoint behavior; response below 400 is not task-quality evidence.
Operational authority: behavior permitted, blocked, or changed: None directly beyond returned diagnostic.
Behavioral-authority path: consumer, channel, force, horizon: config_status/config_setup through result/exception channel, immediate decision input.
Evidence source ID and local anchor: SRC-1, `src/fractal/connectivity.py`.
Claim IDs or none: none
Mismatch marker or none: No unsupported-provider check is silently treated as verification.
Gap/limit: Requests/services unobserved; supplied opener could alter semantics; status checks connectivity only for main selection.

Route ID: [EPI-RTE-provider-check](#epi-rte-provider-check), [RT-RTE-config-change](runtime.md#rt-rte-config-change)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: none; provider configuration and diagnostic status
Content/update relation: non-truth-apt policy/content update: provider selection and diagnostic disposition
Transition or check target: Whether to report config status success, and whether setup remains saved.
Evaluator/condition and domain: config_status fails on connectivity error; setup warns after write; offline skips connectivity. Schema/catalog/readiness checks have separately bounded input domains.
Activation and timing: see cited records.
Possible or observed result: Status return 1 or 0; setup may return 0 despite connectivity failure or missing credential warning.
Implemented force: Status exit code enforces command result, not general task admission; setup connectivity result advisory only.
Epistemic authority and scope: Named connectivity diagnostic, not model-answer correctness or proof of model availability for every selected model.
Operational authority: behavior permitted, blocked, or changed: Persisted config can select later adapters without a successful network check; operator repairs/replaces it.
Behavioral-authority path: consumer, channel, force, horizon: Operator through status/warnings; future runtime through TOML/provider selection; no automatic performance-adaptive update.
Evidence source ID and local anchor: SRC-1, `src/fractal/config_commands.py`; see cited records.
Claim IDs or none: none
Mismatch marker or none: Network failure is not setup rollback.
Gap/limit: CLI explicit LM and direct caller alternatives prevent treating this diagnostic as a universal launch gate.

Route ID: [EPI-RTE-version-notice](#epi-rte-version-notice)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-version-cache](#epi-obj-version-cache)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Website latest string into local cache.
Evaluator/condition and domain: JSON/string shape; source warrant unknown.
Activation and timing: see cited record.
Possible or observed result: Fresh imported identifier or fallback cached identifier.
Implemented force: Cache write and possible notification input, no installation.
Epistemic authority and scope: Website-reported version only, not release safety or provenance validation.
Operational authority: behavior permitted, blocked, or changed: Future failed requests can use cached latest for at most the accepted cache age.
Behavioral-authority path: consumer, channel, force, horizon: Notice formatter, cache/website channel advisory, startup and one-day fallback.
Evidence source ID and local anchor: SRC-1, `src/fractal/version_check.py`.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Cache timestamp is freshness, not endorsement.

Route ID: [EPI-RTE-version-notice](#epi-rte-version-notice)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-version-cache](#epi-obj-version-cache)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Latest identifier compares greater than installed package identifier under packaging.version.Version.
Evaluator/condition and domain: Version ordering only; invalid versions or missing dependency return False.
Activation and timing: see cited record.
Possible or observed result: Greater-than result, then notice or omission.
Implemented force: Advisory upgrade notice; no successor installation or rollback.
Epistemic authority and scope: Ordering follows warranted parser inputs; does not prove the website's latest assertion.
Operational authority: behavior permitted, blocked, or changed: User may choose to run the displayed upgrade command.
Behavioral-authority path: consumer, channel, force, horizon: Terminal user, banner, advisory one startup; future cache reuse is distinct from acceptance.
Evidence source ID and local anchor: SRC-1, `src/fractal/version_check.py`.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: CLI comment says PyPI update check, implementation contacts Fractal website; use implementation identity, not comment as service provenance.

Route ID: [EPI-RTE-contract-tests](#epi-rte-contract-tests), [RT-RTE-package-release](runtime.md#rt-rte-package-release)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)
Content/update relation: no content change
Transition or check target: Synthetic session serialization contract; CI unit-test and lint contract.
Evaluator/condition and domain: Pytest assertions against constructed expected values, not model-answer oracle.
Activation and timing: see cited records.
Possible or observed result: Test pass/fail; no result supplied.
Implemented force: Failing assertion fails test job; coverage upload is not correctness acceptance. Release workflow has no test-job dependency as supplied.
Epistemic authority and scope: A successful run would support tested fixture properties only, not end-to-end capability or context-rot prevention.
Operational authority: behavior permitted, blocked, or changed: CI exposes failed checks to repository operators; merge protection not established.
Behavioral-authority path: consumer, channel, force, horizon: CI job and maintainer, job status, enforcing job completion/advisory repository decision.
Evidence source ID and local anchor: SRC-1, `tests/test_session.py`, `.github/workflows/tests.yml`; release limit see cited route.
Claim IDs or none: [EPI-CLM-context-rot](#epi-clm-context-rot)
Mismatch marker or none: Development evaluator is not a task-turn gate.
Gap/limit: Other test bodies not exhaustively read; no execution or causal comparison supplied.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-context-rot](#epi-clm-context-rot) | see cited record | SRC-1, `README.md`, doctrine/design | Programmatic context and sub-model account | [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), [EPI-RTE-summary-render](#epi-rte-summary-render) | none supplied | No intervention/comparison; inner summarization external | Fractal delegates a model/code computation and supplies structured trajectory plus bounded detailed history | No-context-rot and model-scaled benefit unestablished; all summary responses can accumulate. |
| [EPI-CLM-readable-trace](#epi-clm-readable-trace) | see cited record | SRC-1, `README.md`, doctrine/design | Readable recursion/verification claim; pseudo trace | [RT-OBJ-session-state](runtime.md#rt-obj-session-state), [EPI-RTE-event-projection](#epi-rte-event-projection) | none supplied | No verified task run; hooks best effort, trace schema external | Available trace can be retained and offered for recall | Completeness and actual verification unestablished; old detailed turns expire. |
| [EPI-CLM-trustworthy-usage](#epi-clm-trustworthy-usage) | see cited record | SRC-1, `src/fractal/session.py`, doctrine/design in docstring and implementation | Host derives usage from trace rather than response | [EPI-RTE-event-projection](#epi-rte-event-projection), [RT-OBJ-session-state](runtime.md#rt-obj-session-state) | none supplied | Provider trace truth and successful persistence not independently tested here | Deterministic sums of supplied trace accounting avoid trusting response prose for usage | Scoped trace dependency, not unconditional trustworthy audit or correctness warrant. |

## Bounded conclusion

Fractal implements candidate delivery and operational reliance, not a universal truth-checking boundary. The adapter checks structure; runtime status records return/failure/budget/interruption. Neither criterion accepts the answer as true or validates the changed-file list against actual edits. Direct file effects precede those outer checks. The requested verification of important edits is a real policy, but its exercise and evaluator depend on the delegated computation and workspace. No particular accepted ampliative claim can be established from source-only generation wiring.

The session checkpoint keeps responses together with host status, counts and available traces, including budget fallback and unsuccessful turns. The renderer copies response prose, rather than checking or semantically condensing it, into later signature context. Counts and labels are deterministic reshaping/derivation in their narrow input domains. Exact history retention is bounded; summary-turn rendering is not. Read-back supplies a live model-facing path but does not demonstrate compliance, evidence-consuming acceptance or integration after acceptance.

Root guidance and release identifiers are imports with unknown source warrant; truncation/fallback has local limits. Runtime hooks derive scoped observations, not complete effect auditing. Provider connectivity has a concrete endpoint/time domain: config status can fail, while setup preserves written configuration and warns. Version comparison licenses an advisory ordering notice, not automatic installation. Development tests have expected synthetic values and job-level consequences, not an online answer oracle.

Main and sub-model parameters, mutable endpoint resolution and version fixity remain bounded as in [RT-CMP-main-lm](runtime.md#rt-cmp-main-lm) and [RT-CMP-sub-lm](runtime.md#rt-cmp-sub-lm). Adapter configuration change is distinct from model learning. Later context consumption establishes an implemented avenue for experience to influence work, not improved capacity, content-directed method criticism, autonomous theory building, or exercised self-improvement. Those properties do not imply one another and are not resolved by a single system score. The advertised context and trace benefits remain unsupported at observed-run and causal layers in this evidence set.

## Shared records

### Operative objects

#### EPI-OBJ-agent-turn
Label: AgentTurn response and status

Part of: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)
Source-native identity: `AgentTurn` in each SummaryTurn. Representational form: natural-language response/error plus symbolic status/count/usage fields. Storage substrate: Pydantic model and saved session JSON. Distinct material part: this carries the task answer and outer outcome; the supplied checkpoint record is the containing state, not semantic answer acceptance. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/runtime.py`.

> class AgentTurn(BaseModel):
>     status: Literal["succeeded", "failed", "max_iterations", "interrupted"]
>     response: str = ""
> --- `src/fractal/session.py`

#### EPI-OBJ-session-summary
Label: SessionSummary prompt projection

Part of: [RT-OBJ-session-state](runtime.md#rt-obj-session-state)
Source-native identity: `SessionSummary.turns`; includes user text and AgentTurn records, overlapping the contained [EPI-OBJ-agent-turn](#epi-obj-agent-turn) rather than redefining it. Representational form: structured symbolic container of natural-language content, rendered into instruction text. Storage substrate: JSON/Pydantic state and per-turn signature docstring. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/agent/signature.py`.

> class SessionSummary(BaseModel):
>     turns: list[SummaryTurn] = Field(default_factory=list)
> --- `src/fractal/session.py`

#### EPI-OBJ-runtime-event
Label: RuntimeHookSnapshot observation

Source-native identity: `RuntimeHookSnapshot` and reducer-visible fields. Representational form: symbolic target/phase/argument/result fields, with interpreted path/command strings. Storage substrate: transient Python dataclass; reduced observations enter history and summary counts. Distinct from [RT-OBJ-session-state](runtime.md#rt-obj-session-state): this is event input before checkpoint writing. Closest supplied claim is [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting), not another event-object declaration. Evidence: SRC-1, `src/fractal/events.py`.

> class RuntimeHookSnapshot:
>     """Fractal's normalized view of a PredictRLM runtime hook event."""
>
>     target: str
>     phase: str
>     args: list[Any] = field(default_factory=list)
> --- `src/fractal/events.py`

#### EPI-OBJ-version-cache
Label: Version check cache

Source-native identity: `version_check.json` latest/fetched_at/install_id payload. Representational form: symbolic JSON keys and version strings. Storage substrate: config-directory JSON file and notifier fields. No counterpart in supplied runtime after comparison: not session memory or provider config selection; this holds a website assertion for startup notices. Evidence: SRC-1, `src/fractal/version_check.py`.

> def _write_cached_latest(latest: str) -> None:
>     payload = _read_cache()
>     payload["latest"] = latest
>     payload["fetched_at"] = time.time()
>     _write_cache(payload)
> --- `src/fractal/version_check.py`

### Routes

#### EPI-RTE-summary-render
Label: Session summary rendering

Source-native progression: summary fields → deterministic text → dynamic signature → later PredictRLM invocation. Owner: Fractal session/signature code; state effect is projection, action effect is later model context. Distinct material transformation within the broad [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn), not a second declaration of the whole turn. Evidence: SRC-1, `src/fractal/session.py`, `src/fractal/agent/signature.py`, `src/fractal/runtime.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rendered summary string; empty summary gives No prior Fractal session context.
- Later read-back: Saved user/response/status/count/error fields are rendered on later submission, including after explicit resume.
- Delegated visibility: Signature docstring always-visible text; detailed history separately supplied for Python inspection.
- Selection predicate: Every summary turn is enumerated; response/error emitted only when nonempty; history separately takes its last 20 turns.
- Invalidation or expiry: Summary projection has no inspected turn cap; detailed history cap can remove underlying exact event/trace data.
- Activation or effect: Instruction delivery wired; changed model decisions unobserved.
- Evidence limits: Deterministic field preservation does not establish truth of preserved prose or bounded total prompt size; inner summarization external.

Concrete input deduction, not execution: a SummaryTurn with user message `inspect x`, response `x has a bug`, status `succeeded`, and two changed-file strings produces `User: inspect x`, `Agent status: succeeded`, `Agent response: x has a bug`, and `files_changed_count: 2`. File names are absent from this summary projection; the response is not semantically shortened. This follows from the inspected field assignments and renderer, with no assumption that the response or changed-file assertions are true.

> summary_turn.agent = AgentTurn(
>     status=status,
>     response=response,
>     files_read_count=len(files_read_list),
>     files_changed_count=len(files_modified_list),
>     commands_run_count=len(commands_run_list),
> --- `src/fractal/session.py`

> lines.append(f"User: {turn.user.message}")
> if turn.agent is None:
>     lines.append("Agent status: pending")
>     continue
> lines.append(f"Agent status: {turn.agent.status}")
> if turn.agent.response:
>     lines.append(f"Agent response: {turn.agent.response}")
> lines.append(f"files_read_count: {turn.agent.files_read_count}")
> lines.append(f"files_changed_count: {turn.agent.files_changed_count}")
> lines.append(f"commands_run_count: {turn.agent.commands_run_count}")
> --- `src/fractal/session.py`

> class EditWorkspaceWithSession(dspy.Signature):
>     __doc__ = instructions
> --- `src/fractal/agent/signature.py`

The static guidance is policy, not a verified disposition:

> Keep changes focused on the current user request. Inspect files before modifying
> them, preserve unrelated content, and verify important edits. Return only a
> concise user-facing response and a list of changed file paths, relative to the
> primary workspace when possible.
> --- `src/fractal/agent/signature.py`

#### EPI-RTE-event-projection
Label: Runtime event projection

Endpoints: dependency hook event → snapshot → RuntimeEventTracker lists/display event → runtime checkpoint → later summary/history. Owner: Fractal reducer and writer. Distinct from [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting), a claim about accounting: this record isolates the phase/target projection and its consumer semantics. It overlaps [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn) at checkpoint writing, not whole-route identity. Evidence: SRC-1, `src/fractal/events.py`, `src/fractal/runtime.py`, `src/fractal/session.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized display event or None; unique file/command lists updated under phase and nesting rules.
- Later read-back: Files-read/commands and trace-derived usage reach saved history/counts; successful changed_files comes from result, not tracker.files_modified.
- Delegated visibility: Later session summary/history supply accounting; live callbacks are display observations, not approval requests.
- Selection predicate: Registered file/subprocess target sets, phase checks, compound suppression and available path/command arguments.
- Invalidation or expiry: Tracker is turn-local; detailed history expires beyond 20 turns; summary counts persist with the session.
- Activation or effect: Checkpoint and display inputs wired, no check of semantic edit correctness and no hook-enforced veto.
- Evidence limits: Missing hook import or suppressed callback errors can remove observations; external hook correctness and trace accounting unknown.

A reported `subprocess.run` before event adds the command even if an error follows. An after `pathlib.Path.write_text` event with a known path can add a modified-file fact to the tracker. That fact is not necessarily the changed-file list persisted on return. Concrete deductions are implementation-level, not observed command execution.

> if phase == "before":
>     _append_unique(self.commands_run, command)
> --- `src/fractal/events.py`

> if path and phase == "after":
>     if mode in {"read", "read_write"}:
>         _append_unique(self.files_read, path)
>     if mode in {"write", "read_write"}:
>         _append_unique(self.files_modified, path)
> --- `src/fractal/events.py`

> else:
>     self.session.add_agent_turn(
>         status="succeeded",
>         response=result.response,
>         changed_files=result.changed_files,
>         files_read=runtime_events.files_read,
>         commands_run=runtime_events.commands_run,
>         trace=result.trace,
>         turn_id=turn_id,
>     )
> --- `src/fractal/runtime.py`

#### EPI-RTE-provider-check
Label: Provider connectivity diagnostic

Endpoints: status/setup selection → cheap HTTP GET classification → status exit or setup warning. Owner: Fractal connectivity/config command code. Distinct material evaluator/disposition pair supplementing [RT-RTE-config-change](runtime.md#rt-rte-config-change), which describes adapter/config mutation. Context is selected main endpoint/credentials; no task answer or workspace evaluator. Evidence: SRC-1, `src/fractal/connectivity.py`, `src/fractal/config_commands.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: True for responding supported endpoint below 400, False when no endpoint check, or error; status/setup print different consequences.
- Later read-back: inapplicable — diagnostic result is not retained as a future task acceptance record; setup config is separately retained.
- Delegated visibility: inapplicable — check is ordinary HTTP/code without a model call.
- Selection predicate: config status/setup unless offline; status main connectivity only, local readiness may check both selections.
- Invalidation or expiry: No durable diagnostic license; a later call repeats current checks.
- Activation or effect: Status failure returns 1; setup connectivity failure only warns after config write.
- Evidence limits: No supplied service response; a cheap endpoint GET does not test inference or task-answer quality.

Operator supplies configuration and can correct it; schema/readiness checks propose no learned update. Config set can reject schema/catalog mismatch. Setup can save with missing-credential warning; network errors do not roll it back. No answer oracle or improvement curriculum. This is operational setup, not knowledge-claim acceptance.

> if status >= 400:
>     raise ProviderConnectivityError(
>         f"provider {definition.id!r} connectivity check failed "
>         f"(HTTP {status} from {endpoint.url})."
>     )
> return True
> --- `src/fractal/connectivity.py`

> if not offline:
>     try:
>         if check_provider_connectivity(selection):
>             print("Provider connectivity verified.", file=stdout)
>     except ProviderConnectivityError as exc:
>         print(f"warning: {exc}", file=stderr)
>         print(
>             "The config was written. Fix the credential or network, then "
>             "run `fractal config status` to verify.",
>             file=stderr,
>         )
> return 0
> --- `src/fractal/config_commands.py`

> except ProviderConnectivityError as exc:
>     print("Fractal config status: unreachable", file=stdout)
>     print(render_config(result.config, path=result.path), file=stdout)
>     print(f"connectivity check failed: {exc}", file=stderr)
>     print(
>         "Fix the credential or network, or re-run with `--offline`.",
>         file=stderr,
>     )
>     return 1
> --- `src/fractal/config_commands.py`

#### EPI-RTE-version-notice
Label: Startup version notice

Endpoints: website JSON/cache → latest identifier → installed-version comparison → terminal notice. Owner: Fractal notifier; cache carries website report across startups. No counterpart after comparison with [RT-RTE-package-release](runtime.md#rt-rte-package-release): notification advises an operator, not production package admission. Evidence: SRC-1, `src/fractal/version_check.py`, `src/fractal/cli.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Latest string or cache fallback; notice only when installed version exists and ordering says newer.
- Later read-back: Saved latest/fetched_at is fallback input to later startup, accepted within 24-hour TTL.
- Delegated visibility: inapplicable — ordinary network/version code, no model call.
- Selection predicate: Non-JSON CLI startup; config command dispatch returns before notifier; version ordering controls banner.
- Invalidation or expiry: One-day fallback cache; fresh response overwrites latest; errors are swallowed.
- Activation or effect: Advisory banner with upgrade command, not automatic installation.
- Evidence limits: Website truth, package existence, installed upgrade behavior and observed requests unknown.

The website supplies the assertion; code decides shape/order, user can ignore it. No expected task answer, candidate-performance comparison or self-improvement trigger. No rollback is needed for an uninstalled advisory candidate; installed update recovery is outside this route.

> latest = payload.get("latest")
> return latest if isinstance(latest, str) else None
> --- `src/fractal/version_check.py`

> try:
>     return Version(latest) > Version(current)
> except InvalidVersion:
>     return False
> --- `src/fractal/version_check.py`

> if _is_newer(latest, current):
>     return format_notice(current, latest)
> return None
> --- `src/fractal/version_check.py`

#### EPI-RTE-contract-tests
Label: Development contract tests

Endpoints: push/PR CI → pytest fixture/assertions and lint → job result. Owner: GitHub Actions configured by repository; developers author fixture/reference values. Distinct from [RT-RTE-package-release](runtime.md#rt-rte-package-release): development checking, not release publication. Context is source contracts, including synthetic sessions, not user task claims. Evidence: SRC-1, `.github/workflows/tests.yml`, `tests/test_session.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Assertion/job success or failure if run; no run result supplied.
- Later read-back: inapplicable — no model-facing experience update is wired by this test workflow.
- Delegated visibility: inapplicable — test job is not a task-model call.
- Selection predicate: Push/PR against main, Python 3.11/3.12/3.13 matrix; pytest tests/ and ruff src/tests.
- Invalidation or expiry: Each job checks its checkout; no durable epistemic license for later changed code.
- Activation or effect: Failed assertion prevents successful test job; repository merge policy and release gating not established.
- Evidence limits: Inspected test source establishes evaluator design, not passing execution; fixture expectations do not grade open-ended model answers.

Proposer is repository contributor; evaluator is assertion code with developer-supplied reference values; maintainer veto and branch protection unknown. Operating mode is bounded synthetic contract testing, not online improvement. No automatic package rollback or learned revision is configured by this workflow.

> - name: Run unit tests
>   run: uv run pytest tests/ -q --cov=fractal --cov-report=xml
> --- `.github/workflows/tests.yml`

> assert loaded.history[-1].files_read == ["src/app.py"]
> assert loaded.history[-1].files_modified == ["README.md"]
> assert loaded.history[-1].commands_run == ["uv run pytest"]
> assert loaded.history[-1].trace == trace
> --- `tests/test_session.py`

### Claims

#### EPI-CLM-context-rot
Label: Programmatic context without context rot

Claimed operation: model-managed programmatic context scales capability with model instead of harness engineering and avoids context rot. Source: SRC-1, `README.md`, doctrine/design. No counterpart in supplied runtime's result/accounting claims; broad product benefit, not adapter structure. [RT-RTE-headless-turn](runtime.md#rt-rte-headless-turn) supplies delegation, not causal support.

> The model writes and runs its
> own code, calls a sub-model when it needs to, and manages its own context as it
> works — so capability scales with the underlying model instead of with harness
> engineering, and
> [without context rot](https://github.com/Trampoline-AI/predict-rlm). (It's an
> implementation of the
> --- `README.md`

#### EPI-CLM-readable-trace
Label: Fully readable verification trace

Claimed operation: every peek/chunk/sub-call/verification step is readable in trace. Source: SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting), which covers best-effort file/command accounting, not all dependency steps. Illustrated trace is explicitly pseudo, not observed run.

> And every
> peek, chunk, sub-call, and verification step is fully readable in the trace.
> --- `README.md`

> This is a pseudo trace, to help you understand what goes on inside the RLM.
> --- `README.md`

#### EPI-CLM-trustworthy-usage
Label: Host-recorded trustworthy usage

Claimed operation: usage derived from trace rather than model output stays trustworthy across failed/interrupted turns. Source: SRC-1, `src/fractal/session.py`, doctrine/design docstring plus inspected arithmetic implementation. Distinct accounting part from [RT-CLM-hook-accounting](runtime.md#rt-clm-hook-accounting): token/cost/iteration trace input rather than filesystem/subprocess hook lists.

> Derived from the PredictRLM RunTrace, not from model output, so it stays
> trustworthy across failed and interrupted turns.
> --- `src/fractal/session.py`

> return TurnUsage(
>     input_tokens=trace.usage.main.input_tokens + trace.usage.sub.input_tokens,
>     output_tokens=trace.usage.main.output_tokens + trace.usage.sub.output_tokens,
>     cost=trace.usage.main.cost + trace.usage.sub.cost,
>     duration_ms=trace.duration_ms,
>     iterations=trace.iterations,
>     context_tokens=context_tokens,
> )
> --- `src/fractal/session.py`
