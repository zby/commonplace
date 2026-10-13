---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Atomic workflow account tracing manual report dispatch through research, structural verification, finding admission and recovery."
run-id: AAS-2026-10-12-atomic-f98683232831-01
reviewed-boundary: "983bea6baf449d060514c94b3b15b5f85f77ba9b"
---

# Atomic workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **run an existing report now and retrieve its finding**. It joins a shipped HTTP request, durable work claim, model-directed research, a separate prose-generation call, storage admission and a published read endpoint. It was selected because these steps form one explicit lifecycle, including rejection and retry, rather than a constructed combination of independent capabilities. Its existing referent is [RT-RTE-report-finding](runtime.md#rt-rte-report-finding); the workflow-specific findings below annotate that route rather than redeclare it.

All source evidence is SRC-1 implementation at the revision in [boundary](boundary.md#source-register). Additional inspection covers `crates/atomic-server/src/routes/reports.rs`, `crates/atomic-core/src/reports/scope.rs`, `crates/atomic-core/src/scheduler/ledger.rs` and `crates/atomic-core/src/providers/structured.rs`, plus selected report assembly and runner regions in `crates/atomic-core/src/reports/agentic.rs`, `crates/atomic-core/src/reports/runner.rs` and `crates/atomic-core/src/lib.rs`. No execution evidence establishes that a run succeeded, that the model used its tools correctly, or that the delivered prose improved a user's knowledge.

### 1. Request, dispatch and claim

The caller posts a report ID to `/api/reports/{id}/run`. The REST handler checks that the report exists, rejecting an unknown ID before dispatch. It clones the core and event channel into a spawned Rust task. The immediate HTTP result is **202 dispatched**, not completed research. It contains the findings URL for later retrieval. The core reloads the report and calls the shared runner with a Manual trigger. SRC-1: `crates/atomic-server/src/routes/reports.rs`, `crates/atomic-core/src/lib.rs`.

> HttpResponse::Accepted().json(RunNowResponse {
>     report_id: id.clone(),
>     status: "dispatched",
>     findings_url: format!("/api/reports/{id}/findings"),
> })
> --- `crates/atomic-server/src/routes/reports.rs`

The runner asks the ledger for a claim under `report::{id}`, with a default three-attempt budget. No claim returns Skipped: dispatch can therefore succeed without starting a new research episode. The task handle supplies the run identity used in eventual finding provenance. Coordination is software-owned; this is not delegation to a second autonomous agent. The model later chooses research actions, but does not allocate or claim durable report work. SRC-1: `crates/atomic-core/src/reports/runner.rs`; see the lifecycle already retained in [RT-RTE-report-finding](runtime.md#rt-rte-report-finding).

### 2. Resolve what reaches research

The runner resolves the source batch before invoking the model. Source tag scope, configured kinds, time window and atom cap go into storage queries. A content-token budget then trims the returned batch, keeping at least its first atom even if that atom alone exceeds the budget. Consequently this budget is not a strict maximum on delivered prompt tokens. Empty source selection terminates without a model call. SRC-1: `crates/atomic-core/src/reports/scope.rs`, `crates/atomic-core/src/reports/runner.rs`.

> if out.is_empty() {
>     used += tokens;
>     out.push(a);
>     continue;
> }
> --- `crates/atomic-core/src/reports/scope.rs`

The initial model handoff contains the stock system scaffold, report-specific research prompt, numbered source titles/snippets/IDs and citation-policy instructions. It is not full source content: `read_atom` supplies line windows on demand. The runtime constructs only `read_atom`, `semantic_search` and `done` tools for this workflow. Source numbering seeds the citation ledger. SourceOnly disallows new citation identities; SourceAndContext permits search to register them. These ledger rules are already evidenced by [RT-RTE-report-finding](runtime.md#rt-rte-report-finding). SRC-1: `crates/atomic-core/src/reports/agentic.rs`.

Context search uses configured tag/time/kind predicates and excludes the selected sources and this report's prior findings. These predicates filter semantic-search results after retrieval. They do **not** govern every reader: `read_atom` calls `core.get_atom(atom_id)` directly, with no context-filter check in that handler. Therefore source/context scope limits source selection and search delivery, not all atom content potentially delivered to research. This resolves the baseline's explicitly uninspected read-atom isolation question without changing its route identity. Citation eligibility also does not establish which text the model could have read. SRC-1: `crates/atomic-core/src/reports/scope.rs`, `crates/atomic-core/src/reports/agentic.rs`.

> let atom = match self.core.get_atom(atom_id).await {
>     Ok(Some(a)) => a,
>     Ok(None) => return ToolResult::failed(format!("no atom found with id {}", atom_id)),
>     Err(e) => return failed_verbatim(format!("Error fetching atom {}: {}", atom_id, e)),
> };
> --- `crates/atomic-core/src/reports/agentic.rs`

### 3. Research hands its transcript to synthesis

AgentRun owns iteration and local tool execution; the configured model proposes queries, atom IDs and stopping. The report sets a configurable round count, sentinel termination through `done`, no cancellation handle, no event callback, no context-length trimming and no salvage-on-cap. Its transcript proceeds to synthesis even when the research budget is exhausted. This is a bounded research loop followed by another inference call, not independent reviewer approval. SRC-1: `crates/atomic-core/src/reports/agentic.rs`; shared executor ownership is described in [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn).

The synthesis handoff takes `outcome.messages` and appends an instruction to write markdown with citation markers and not call tools. It does not publish the research loop's intermediate text. The configured provider/model performs the separate final pass. Rust remains the executor and admission owner. SRC-1: `crates/atomic-core/src/reports/agentic.rs`.

> let mut messages = outcome.messages;
> messages.push(Message::user(
>     "Now write the final report as markdown prose with [N] citation \
>      markers. Do not call tools."
>         .to_string(),
> ));
> --- `crates/atomic-core/src/reports/agentic.rs`

### 4. Structural verification, not truth verification

The final call uses the long-form markdown contract. Its parser requires a `CITATIONS_USED:` trailer, rejects content after the trailer, parses citation numbers and rejects an empty body. Early-ended generations and retryable provider failures can retry; a malformed trailer receives at most one corrective nudge within the available retry budget. Exhaustion returns an error to the runner. This accepts a usable response shape, not a correct answer: there is no expected-answer oracle or independent factual reviewer in this inspected admission path. SRC-1: `crates/atomic-core/src/providers/structured.rs`, `crates/atomic-core/src/reports/agentic.rs`.

> if nudged || attempt >= max_retries {
>     return Err(StructuredCallError::Other(format!(
>         "long-form parse failed: {parse_err}"
>     )));
> }
> --- `crates/atomic-core/src/providers/structured.rs`

The report adapter uses the returned **body** and resolves citations with `ledger.cited_in(&content)`; the trailer's parsed citation list is not the finding's citation authority. The runner additionally rejects whitespace-only content. Passing these checks automatically admits model prose without per-finding human approval. Neither marker resolution nor structural completeness verifies that each cited atom supports each claim. SRC-1: `crates/atomic-core/src/reports/agentic.rs`, `crates/atomic-core/src/reports/runner.rs`; citation admission and the nonempty guard are retained in [RT-RTE-report-finding](runtime.md#rt-rte-report-finding).

### 5. Delivery and later consumption

The runner assigns a finding atom UUID, retains report/run provenance, maps resolved citations and applies configured output tags. It calls a transactional finding-write helper for atom, provenance and citations. It then updates the report cache and completes the ledger with the finding ID. These latter operations are separate awaits after the write; storage-helper internals were not inspected here. A returned Succeeded outcome identifies the retained product, but no end-to-end exactly-once guarantee follows. SRC-1: `crates/atomic-core/src/reports/runner.rs`; see [RT-RTE-report-finding](runtime.md#rt-rte-report-finding).

The REST background task reloads a successful atom and broadcasts AtomCreated when possible. A client can poll the supplied findings endpoint to retrieve persisted results. Event delivery is not required for persistence and does not prove client receipt. Thus the delivery boundary is a stored, retrievable finding, with a best-effort notification—not the initial 202 response or intermediate transcript. SRC-1: `crates/atomic-server/src/routes/reports.rs`.

### 6. Failure, rejection and recovery ownership

A research/provider/final-parser/write error from the runner's execute stage records last_error without advancing last_run_at and calls the ledger's failure method. Software, not the model or a reviewer, decides recovery. Installed failure policy can defer an environmental failure without consuming retry budget; otherwise attempts below the maximum schedule backoff and exhausted attempts abandon. Subsequent dispatch/claim supplies another attempt. This is work-lifecycle recovery, not retained content-directed criticism of the research method. SRC-1: `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-core/src/scheduler/ledger.rs`.

> if let FailureDisposition::DeferUntil(until) = self.core.failure_disposition(&error) {
>     return self.defer_until(until, error).await;
> }
> --- `crates/atomic-core/src/scheduler/ledger.rs`

Empty source or empty output takes a different branch: complete with no result and advance the resolution-time watermark. It is not retried as a failure. Using resolution time rather than completion time leaves atoms captured during research eligible for the next SinceLastRun batch. A capped batch can still omit older eligible atoms; advancing the watermark does not prove complete coverage. SRC-1: `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-core/src/reports/scope.rs`.

Recovery is bounded further: cache-update or ledger-completion errors in the success branches propagate rather than entering the execute-error failure arm. A finding can already exist when these bookkeeping steps fail. The code ignores the boolean returned by completion/failure, so the outcome alone does not prove the lease-fenced transition took effect. No automatic rollback of a successfully written but incorrect finding is established by this trace. SRC-1: `crates/atomic-core/src/reports/runner.rs`, `crates/atomic-core/src/scheduler/ledger.rs`.

> let _ = handle.complete(Some(atom_id.clone())).await?;
> --- `crates/atomic-core/src/reports/runner.rs`

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

#### On [RT-RTE-report-finding](runtime.md#rt-rte-report-finding)

Workflow selection: manual REST report invocation, joining dispatch, claim, research, separate synthesis, structural admission, retained finding and polling. The Workflow account supplies the additional SRC-1 inspection and minimum passages for these refinements.

Handoff boundary: the caller receives 202 before work completes; the background task reloads report configuration; the provider receives source snippets and optional tool-read content; synthesis receives the research message history plus a final-writing instruction. No separate autonomous worker or human content approval is inserted between synthesis and finding write.

Verification boundary: the final-call trailer/parser can reject malformed or prematurely ended output, but is not an answer oracle. Persisted citations derive from body markers resolved against the ledger, not the trailer's declared list. Search filtering does not constrain direct read_atom by ID.

Recovery boundary: execute-stage errors enter ledger fail/defer/backoff/abandon; success-branch cache/complete errors propagate separately after possible durable admission. Lease-transition booleans are discarded. Empty results advance the watermark without a finding. These distinctions prevent interpreting Succeeded/EmptyScope or a dispatched response as proof of complete semantic coverage or end-to-end exactly-once delivery.
