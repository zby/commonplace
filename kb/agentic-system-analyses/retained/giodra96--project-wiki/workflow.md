---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Project Wiki workflow account: inbox document update through source review, conditional human decision, canonical integration and delivery."
run-id: AAS-2026-11-08-project-wiki-b055e5c71dc7-01
reviewed-boundary: "3af1e28d0a3ed3daeb9f923102cd5cefb51b0f41"
---

# Project Wiki workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is an explicit `update` with a processable inbox document, from preflight through canonical integration. It is selected because the shipped instructions join these steps explicitly and expose both deterministic rejection and conditional human review. This is the same route as [RT-RTE-source-intake](runtime.md#rt-rte-source-intake), not a newly declared workflow. Short pasted notes and ordinary coding-task updates are separate routes; they are not assumed to pass through the document ledger.

All findings use SRC-1 at the frozen commit in [the boundary](boundary.md). The workflow is primarily doctrine/design in `references/source-inbox.md` and `references/document-ingestion.md`; local review-helper checks are implementation evidence in `scripts/review_progress.py`. No target code was executed and no consuming-project trace was supplied. The account establishes prescribed coordination and implemented local checks, not a successfully completed integration.

### 1. Request, source decision and extraction handoff

A user requests `update`. The foreground host agent follows the skill's intake procedure and checks the inbox even if chat notes accompany the request. The agent delegates discovery, byte hashing, duplicate-history validation and action selection to `check_inbox.py`; it must inspect the returned action rather than independently reproduce duplicate reasoning. A `new-unique` process result authorizes creation of a pending source registry entry with a stable source ID and reported hash. Retry results name the existing registry entry to reuse. These handoffs carry filesystem paths, source IDs, action/reason fields and hashes, not a semantic answer from another model (SRC-1, `references/source-inbox.md`; [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)).

> The checker derives `process`, `skip`, and `review` actions from the source workflow contract in `schema/project-wiki.yml`; apply the returned action rather than reproducing that mapping in agent reasoning.
> --- `references/source-inbox.md`

The foreground agent then invokes extraction with a local path and the preflight hash as `--expected-sha256`. The extraction helper returns a generated intake directory and compact report, with immutable source provenance, a chunk manifest, chunk text and mutable review progress. Snapshot/hash checking and publication cleanup are implemented local controls, not a transaction over later canonical edits. Direct explicit file ingestion is an alternate supported path where the expected hash is optional; the inbox protocol is the reason it is required here ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake); SRC-1, `references/document-ingestion.md`).

Successful extraction is not canonical integration. For an inbox file, the instructions already tell the agent to archive the original under `sources/processed/YYYY-MM/` and mark its source record processed after ingestion. That lifecycle means extraction/archive success, not completion of the subsequent semantic review. The agent must preserve the matching archived bytes, registry hash and intake provenance (SRC-1, `references/source-inbox.md`).

### 2. Review inputs and semantic comparison

The same host agent reads the compact report, calls `review_progress.py inspect`, and obtains source content through `view`. Reliable source sections may be loaded separately, including unsectioned content; absent or ambiguous structure requires `view --all`. This selects what enters the current host context without delegating semantic review to another agent. The source explicitly refuses using chunk selection as a substitute for whole-source coverage:

> Use `--chunks CH-012 CH-019` only for targeted rereading after complete source review.
> --- `references/document-ingestion.md`

The host owns chunk classification and comparison with the root index, registry, requirements, changes, technical and implementation documents, and traceability. It reconciles existing open questions before proposing new ones. When requirements are involved, it must plan atomic topics before canonical authoring. The helper's hints are metadata, not semantic decisions or a filter permitting source exclusion (SRC-1, `references/document-ingestion.md`).

The agent returns JSON dispositions to `review_progress.py apply`. Pending and interim reviewed entries need final classified or skipped dispositions; classified entries require classifications and skipped entries require reasons. One chunk may support multiple classes and target IDs. The helper validates updates and atomically writes ledger state, but does not establish that the agent read the content or that its classifications are true ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake); SRC-1, `scripts/review_progress.py`). The ledger is a resumable checkpoint, not an independent semantic reviewer. Current-context eviction and host token budgets remain uninspected; section views do not establish a separate context frame or compaction mechanism.

### 3. Canonical admission or a narrowly scoped human decision

An explicit update normally proceeds directly to conservative canonical integration. The host proposes and admits source-backed records while preserving nonblocking uncertainty through questions, alerts, confidence, blocked records or alternatives. Requesting an update is not human approval of each generated claim. No expected-answer oracle is supplied; source and existing wiki state are comparison evidence, not a reference answer ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake); SRC-1, `references/document-ingestion.md`).

A blocking human decision is a conditional handoff, not a universal review stage. It applies when no conservative representation can proceed without resolving source authority/scope, incompatible baselines, unauthorized changes to confirmed intent, a binding choice, or an explicit review-only request. The host writes `review.md` with the exact question, evidence, options, affected scope and consequences. The human supplies that decision, and the host resumes the same integration rather than creating another gate for the same choice:

> Do not duplicate the full source or create a second approval after the user resolves the blocking decision.
> --- `references/document-ingestion.md`

Document size, cross-section impact or security subject matter alone do not justify blocking. A pending review or its unapproved choice is not canonical knowledge. Direct integration writes appropriate records and exact requirement-to-chunk edges in `traceability/requirement-evidence.yml`; unresolved requirement decomposition prevents the intake from becoming integrated (SRC-1, `references/document-ingestion.md`). The user can withhold the consequential decision; this does not turn the deterministic helpers into semantic approvers.

### 4. Verification, final mutation and delivered result

Before `reviewed` or `integrated` status, the host must rerun inspection, require complete review, run the ledger audit, retain its summary and SHA-256, and then check that digest immediately before terminal status mutation. Changed ledger bytes invalidate that checkpoint. The implementation supports this specific rejection:

> if expected_digest != ledger_sha256:
>     raise ReviewProgressError("ledger changed since the reviewed audit snapshot; rerun audit")
> --- `scripts/review_progress.py`

An audit return code alone is insufficient: its result can report `review-incomplete` while the command returns zero. The host must inspect `audit_status`. The helper audits ledger structure/state and identity, not canonical truth; it does not commit the final intake status. This leaves a procedural interval between audit and host mutation, not a lock covering all subsequent edits ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake); SRC-1, `scripts/review_progress.py`).

The host reconciles counts and runs `validate_wiki.py`. Deterministic errors block completion; audit candidates do not. For integrated requirement findings, registered atomic requirement targets and ledger/sidecar edges must agree bidirectionally. These checks can reject malformed or incomplete integration, but cannot prove source entailment or semantic adequacy ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake); SRC-1, `references/document-ingestion.md`, `scripts/validate_wiki.py`).

Delivery therefore means canonical content merged with traceability, required audit evidence logged, intake lifecycle updated and the host reporting integration or the exact blocker. It does not mean merely publishing extraction output or receiving exit zero from audit. The direct path logs integration once; a blocking path logs the pending review and separately logs its final integration, rejection or postponement. Terminal intake remains provenance-only during normal coding work; later tasks should reach integrated knowledge through the ordinary wiki routes, not reread every source ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake), [RT-RTE-coding-cycle](runtime.md#rt-rte-coding-cycle); SRC-1, `references/document-ingestion.md`). Actual later consumption and benefit remain unobserved.

### Failure and recovery ownership

The selected workflow has several distinct recovery boundaries. Preflight errors stop inbox processing; duplicate skips suppress ingestion and may quarantine redundant files. Historical-path changes and ambiguous processable history require reconciliation rather than heuristic record choice. A changed source hash requires fresh preflight, not overriding the old decision. If extraction fails, helper cleanup covers newly generated output while the agent marks the source failed and leaves it in the inbox for retry. These are local recovery responsibilities, not an atomic rollback of a complete wiki update ([RT-RTE-source-intake](runtime.md#rt-rte-source-intake); SRC-1, `references/source-inbox.md`, `references/document-ingestion.md`).

Materially bad extraction before integration must be rejected or superseded and regenerated:

> If extraction is materially wrong before integration, mark the intake `rejected` or `superseded`, append a wiki audit log entry, and rerun ingestion instead of preserving known-bad extraction as a correction note.
> --- `references/document-ingestion.md`

After integration, the prescribed recovery changes affected canonical records and appends an audit entry rather than silently rewriting immutable extraction provenance. A ledger correction requires a new audit; structural validation errors require repair before completion. In each case the foreground host retains scheduling and continuation responsibility. The supplied source provides neither an observed recovery trace nor a guarantee that a host follows these policies (SRC-1, `references/document-ingestion.md`).

### Added inspection coverage

Beyond the supplied runtime baseline, this member read `references/document-ingestion.md` and `references/source-inbox.md` completely for doctrine/design, and inspected `scripts/review_progress.py` main dispatch, audit-result construction and update validation/completion computation for implementation. This adds depth at the same registered SRC-1 revision, not a new source or observed-run layer.

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

#### On [RT-RTE-source-intake](runtime.md#rt-rte-source-intake)

Workflow role: the selected end-to-end path. Coordination alternates foreground semantic work with local deterministic helper calls; only a blocking, auditable decision transfers judgment to a human. No separate model reviewer or worker context is specified in this procedure. Verification separates hash/history checks, ledger coverage and canonical-link structure from semantic fidelity. The host owns recovery after helper errors and the final lifecycle mutation. A processed source is not yet an integrated intake, and an audit checkpoint is not a semantic acceptance verdict. Delivery is bounded by completion of the prescribed canonical integration and audit procedure, with actual execution unobserved.
