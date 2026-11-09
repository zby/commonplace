---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "BRAN workflow account: grounded connected evidence request through host delegation, rejection, bounded retry and local result delivery."
run-id: AAS-2026-11-08-bran-2be75f1c9e69-01
reviewed-boundary: "7bc428b2ccdfad38e05caa0c0cba2bb19041993a"
---

# BRAN workflow report

## Workflow account

### Selection and evidence boundary

This account selects the production connected `bran -p` workflow. It joins repository evidence selection, external-host delegation, answer admission and retained-result delivery in one shipped call chain. It therefore exposes consequential handoffs and a specific recovery path without inventing a general coding-agent loop. The referent is already [RT-RTE-connected-request](runtime.md#rt-rte-connected-request); this member adds workflow interpretation rather than declaring it again. The ordinary offline evidence-selection route remains [RT-RTE-query-packet](runtime.md#rt-rte-query-packet).

The evidence is SRC-1 at the revision fixed by [the boundary](boundary.md#boundary-and-evidence). Source code establishes wiring, not a successful connected invocation. No observed host run, successful recovery or outer-task completion is supplied. BRAN returns evidence; the enclosing agent retains task decisions and implementation, as specified by [RT-CLM-evidence-location](runtime.md#rt-clm-evidence-location).

### 1. Caller requests evidence; BRAN admits the invocation

The caller supplies a prompt and invocation options. Production setup requires connected project settings and explicit trust of the current root, then resolves the configured agent descriptor, profile and ports. Offline is a distinct early branch, not a connected host attempt. Rust code, not a model planner, owns progression. Setup can stop before delegation for missing settings, absent trust or invalid configuration. The runtime additionally gates profile, tool and model authority; the production mutation grant is false. The broader custom-port API is not substituted for this production envelope. These roles and limits are established in [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) and [RT-RTE-runtime-port](runtime.md#rt-rte-runtime-port), SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`.

### 2. BRAN constructs the delegated context

The grounded-request builder scans the current root, constructs graph input, ranks sources against the original prompt, compiles a view, expands dependencies and assembles a bounded packet. Empty views or packets fail grounding rather than producing an ungrounded connected fallback. Only packet items become admitted evidence in the grounding contract; the host is not simply given the whole scanner snapshot. Each admitted locator is paired with a digest of its source bytes. The prompt contains a preamble, the task and the packet. Task segments, source locators and source digests also become preservation anchors. SRC-1, implementation, `crates/bran-cli/src/main.rs`.

> let prompt = prompt_prefix + &packet.payload;
> --- `crates/bran-cli/src/main.rs`

> let grounding_contract = GroundingContract::with_evidence(root, admitted_evidence, anchors)
>     .map_err(|_| ConnectedSetupFailure::GroundingFailed)?;
> --- `crates/bran-cli/src/main.rs`

The builder reserves space for the prompt prefix and requested output before packet assembly; bounded evidence is therefore selected before the model call. This is working-context construction, not removal of older conversation turns. Omitted source material remains on disk for an explicit later request. The packet and accounting have separate consumers, as distinguished by [RT-OBJ-context-packet](runtime.md#rt-obj-context-packet) and [RT-OBJ-packet-receipt](runtime.md#rt-obj-packet-receipt). Source selection is software-controlled; it does not establish that all task-relevant evidence reached the host.

### 3. Runtime delegates; the host proposes an answer

The runtime compresses input under the selected SQZ policy and invokes the configured external executable through the provider port. The host receives the grounded prompt and execution settings, including model/tool/session/budget fields and an account reference. Preflight and result checks compare protocol identities and budget information. The provider-host implementation, model/tool loop and actual confinement are external responsibilities, not BRAN mechanisms inferred from a receipt. [RT-RTE-connected-request](runtime.md#rt-rte-connected-request) and [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) supply the evidence and limits, SRC-1, `crates/bran-core/src/adapters/provider/mod.rs`.

This is a bounded request/response delegation per attempt. The host proposes answer text, citations and claims; BRAN code decides whether that result qualifies for completion. There is no evidenced multi-agent author/reviewer handoff in this selected call chain. Actual host-internal coordination remains uninspected, not absent.

### 4. Verification can reject, but does not certify task success

Runtime acceptance checks the returned execution fields, output surfaces, grounding, exact supported material claims and optional token-budget attestation. A grounded answer must reconstruct from admitted claims, and claim text must equal support. Source support is checked against reopened current files and packet digests. Output compression cannot alter the grounded answer. These completion gates and their minimum source passages are retained in [RT-RTE-connected-request](runtime.md#rt-rte-connected-request), SRC-1, `crates/bran-core/src/agent/coordinator.rs`, `crates/bran-core/src/agent/delegate.rs`.

Thus the local reference is admitted source bytes, not an expected solution to the caller's task. Rejection can establish unsupported output under this contract; acceptance does not establish source truth, adequate coverage or useful task reasoning. Software provides the veto. The caller may disregard accepted evidence; no required human approval of each returned claim is established.

### 5. A specific input-fidelity failure can trigger recovery

The CLI owns retry, not the host. `next_sqz_fidelity_source_limit` requires an incomplete grounding failure, an input SQZ receipt with missing fidelity anchors, a nonempty missing-anchor list and only `source-`-prefixed missing anchors. It refuses this retry when the current source limit is already one. For the qualifying failure it halves the limit, bounded below by one. `next_changed_grounded_request` rebuilds from the original request and retries only when the resulting prompt differs. A smaller requested limit that leaves the prompt unchanged is not itself a new host attempt. SRC-1, implementation, `crates/bran-cli/src/main.rs`.

> if input.failure_reason != Some(SqzFailureReason::MissingFidelityAnchors)
>     || input.missing_fidelity_anchor_ids.is_empty()
>     || input
>         .missing_fidelity_anchor_ids
>         .iter()
>         .any(|anchor| !anchor.starts_with("source-"))
> {
>     return None;
> }
> Some((current_limit / 2).max(1))
> --- `crates/bran-cli/src/main.rs`

> if next_grounded_request.prompt() != grounded_request.prompt() {
>     return Ok(Some((next_controls, next_grounded_request)));
> }
> --- `crates/bran-cli/src/main.rs`

This recovery trades evidence breadth for a smaller compression input. It is not a general critic revising rejected answers or an automatic retry for every unsupported claim, timeout or provider error. When no qualifying changed request remains, the routine returns the receipt; grounding/setup errors can instead terminate with a typed setup failure. This is inspectable recovery capacity, not evidence that shrinking sources preserves answer quality or has succeeded in operation.

### 6. Storage, command delivery and outer delivery are different terminals

After runtime acceptance, successful local result publication is required for runtime completion. The caller receives a delegation receipt containing the inline result and result references. `get` later opens the local result store, retrieves checked content, decodes the canonical inline result and emits answer, citations and claims. Invalid IDs, unavailable stores, missing entries and invalid content have explicit failure returns. Storage and read-back are already part of [RT-RTE-connected-request](runtime.md#rt-rte-connected-request); no automatic reuse as a future prompt follows from them. SRC-1, `crates/bran-cli/src/main.rs`, `crates/bran-core/src/agent/coordinator.rs`.

The CLI applies one further delivery decision: a completed receipt whose citation count exceeds the requested response-source limit becomes an error envelope. Otherwise complete maps to `p`/`ok`, and incomplete maps to `p`/`error`. SRC-1, implementation, `crates/bran-cli/src/main.rs`.

> InvocationOutcome::Complete { .. } => {
>     CliResult::success(make_envelope("p", "ok", &data, &[], &[], "{}", &metrics))
> }
> --- `crates/bran-cli/src/main.rs`

Consequently runtime completion and local retention may precede a CLI delivery error; the error does not prove that no result was saved. Likewise `--no-session` requests host session behavior but does not suppress this local publication, as distinguished by [RT-CLM-session-retention](runtime.md#rt-clm-session-retention). Even a successful CLI envelope delivers evidence rather than an implemented outer-task product. That last decision and change boundary remains with the caller.

### Added inspection coverage

This member independently read the production setup/retry/get and receipt-envelope functions, plus the full grounded-request builder in SRC-1, `crates/bran-cli/src/main.rs`. These are additional implementation inspection of an already included path, not a new source or observed execution layer. Runtime citations supply the coordinator/provider validation evidence. External host execution, actual caller reliance and recovery effectiveness remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-connected-request](runtime.md#rt-rte-connected-request)

Workflow role: selected request-to-delivery chain. Caller initiates and controls the outer task; CLI constructs bounded evidence and owns the narrow source-anchor retry; the external host proposes output; runtime gates completion and publication; CLI maps the receipt to a delivery envelope and can still reject a response-source-count excess. No independent reviewer or expected-task-answer oracle is established by these stages. Runtime completion, command success and successful outer-task implementation are separate outcomes. Retry and delivery are wired in implementation; their exercise and benefit remain uninspected.
