---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Citadel workflow account: scheduled seat-to-Central promotion through model triage, review, write acceptance and later context delivery."
run-id: AAS-2026-11-09-citadel-de4383eefa4e-01
reviewed-boundary: "749a24014a6cef59499dbe13b6fb4c348f8044a4"
---

# Citadel workflow report

## Workflow account

### Selected workflow and evidence

This account selects scheduled promotion of personal-seat material into shared Central, including the new-project review branch. It is representative of Citadel's multi-step memory work: code selects candidates, delegates bounded judgments to a model, admits or withholds shared content, and hands accepted source to separate indexing and retrieval consumers. It is not a multi-agent implementation of an engineering task. The enclosing coding agent remains outside Citadel's control. The baseline identity is [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review); the steps below add workflow detail rather than declare the same route again.

All source findings use SRC-1 at the revision fixed in [boundary](boundary.md). Additional inspected implementation coverage comprises `kb/promotion.py`, `kb/promotion_refs.py`, `kb/promotion_queue.py`, `kb/improvement_policy.py`, promotion endpoints and queue redaction in `kb/server.py`, the promotion stage in `scripts/run_railway.py`, preview shaping in `kb/llm_enrichment.py`, and the decision handler in `web/src/pages/app/review.tsx`. No target code or tests were executed. There is no supplied observed run of this workflow; wiring does not establish classification accuracy, successful recovery, actual reviewer judgment or improved tasks.

### 1. Scheduled trigger, not an interactive promotion request

The scheduled driver constructs a service, checks promotion enablement and a Central evaluation receipt, then collects seat datasets from access-store principals. It shares one engine across seats and calls `engine.run` sequentially with the configured dry-run flag. Each seat failure is counted without aborting the remaining seats; any counted failure makes the stage return failure. SRC-1: `scripts/run_railway.py`.

> if not automation_evaluation_passed(config):
>     logger.info("Promotion stage skipped: Central evaluation gate has not passed")
>     return 0
> --- `scripts/run_railway.py`

The receipt predicate checks Central scope, passed status, a nonempty run identifier, valid evaluation/expiry timestamps, and true values for five named checks: projection chain, seat isolation, cited graph retrieval, rollback and free-model budget. This is a software gate over receipt fields, not independently inspected evidence that these checks passed in a deployment. SRC-1: `kb/improvement_policy.py`.

An interactive caller cannot substitute `/api/promote/run` for the scheduled engine: after access and dataset checks the endpoint returns HTTP 409 with `LLM_SCHEDULED_ONLY`. This limits that HTTP entry, not every direct Python invocation of the engine. SRC-1: `kb/server.py`.

> "message": "Promotion runs only during scheduled self-evolution.",
> --- `kb/server.py`

### 2. Candidate selection and model handoff

Enumeration searches the seat using two broad seed queries, extracts the first nonempty text-like result field, normalizes tags, deduplicates by lowercased text and caps the candidate list. A selected candidate can therefore be a returned summary or title rather than the complete original source. This is best-effort retrieval, not a full-seat audit. If every attempted seed query fails, enumeration raises rather than reporting an empty successful sweep. SRC-1: `kb/promotion.py`.

The engine first blocks personal capture roots and secret-scan failures. It then assesses organizational reference using repository hints, local GitHub-sync state and Central searches. With no repository hint, any Central hit can establish the source-native `known_org_work` status; without a hit the status is `no_reference_signal`. Unmatched repository hints without Central hits yield `new_org_project`. Search errors become empty hit lists, so these statuses are operational heuristics, not verified organizational membership. SRC-1: `kb/promotion.py`, `kb/promotion_refs.py`.

Model delegation supplies at most 6,000 characters of candidate text. The typed decision path gets relevance/sensitivity questions; if it yields no usable verdict, chat fallback gets the classifier system prompt and capped candidate as user content. A usable negative typed verdict is retained rather than retried until favorable. The model receives neither an entire seat corpus nor a separate tool-using agent workspace. The blocking classification call is dispatched through `asyncio.to_thread`; this is execution isolation from the event loop, not an autonomous reasoning worker. SRC-1: `kb/promotion.py`; model identities and mutability are covered by [RT-CMP-promotion-decision](runtime.md#rt-cmp-promotion-decision) and [RT-CMP-openrouter-chat](runtime.md#rt-cmp-openrouter-chat).

> verdict = await asyncio.to_thread(self.classify, candidate.text)
> --- `kb/promotion.py`

> "both relevant AND safe to promote. Never include the original text or any "
> "secret in the reason."
> --- `kb/promotion.py`

The output parser checks shape and value types; engine code requires relevance, nonsensitivity and a score at least the configured threshold. It also checks prior rejection by seat and content hash. None of these supplies an answer oracle or a proof of factual correctness. The operating mode is a bounded maintenance sweep. Model judgment proposes suitability; fixed rules control which action is permitted. SRC-1: `kb/promotion.py`; [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review).

### 3. Automatic admission or review handoff

Qualifying known work can be promoted automatically, subject to capture-root tagging rules. Qualifying new-project material becomes pending review. A dry run returns proposals without executing either queue insertion or promotion writes. Thus a proposal is not yet delivered content. SRC-1: `kb/promotion.py`.

For a pending proposal the engine stores candidate text, its hash, a redacted preview, seat identity, model verdict and reference status, plus a scan result when scanning succeeds. The queue builder can store repository hints, but this enqueue call reconstructs a reference assessment using only status and reason, so original matched-repository/search details do not cross this handoff. SRC-1: `kb/promotion.py`, `kb/promotion_queue.py`.

The review-list endpoint further removes the candidate body. Reviewers receive preview and metadata, not the complete stored candidate through this endpoint. Preview shaping collapses whitespace, truncates and redacts secrets. Legacy items without a scan are scanned during the read without persisting that result. These transformations limit what the reviewer can verify from the list alone. SRC-1: `kb/server.py`, `kb/llm_enrichment.py`.

> text = redacted.pop("candidate_text", None)
> --- `kb/server.py`

The inspected Next review handler asks for browser confirmation, then POSTs the item ID to approve or reject. It does not send edited candidate content. Both server endpoints require admin role and `sources:sync` before item lookup; a seat writer's apparent ownership is not enough. Credentials do not establish that a biological human made the decision. The browser confirmation supplies a human-facing opportunity, while authenticated software clients can use the same endpoints. SRC-1: `web/src/pages/app/review.tsx`, `kb/server.py`.

> # Approving commits a candidate into Central, so it requires admin — a
> # seat-writer is rejected with 403 BEFORE the item lookup, closing the gap
> # where a seat could self-promote its own pending item into Central (#48).
> identity = require_access(request, "admin", "sources:sync")
> --- `kb/server.py`

### 4. What approval delivers, and what it does not

Approval reloads the stored full candidate and reconstructs a promotion proposal. It does not repeat the model triage at this point. `_promote` uses a synthetic service-account admin/env identity whose default dataset is the seat, resolves the seat-light/Central-full dual-write targets, and supplies the approving actor as attestation. Downstream learning re-runs content guards. Promotion tags and actor/time metadata accompany the text; the model itself has no direct write capability. SRC-1: `kb/promotion.py`.

The engine checks the returned Central ingestion outcome before reporting promotion. A rejected write is not counted as delivered merely because the write call returned. This distinction is load-bearing:

> if not primary.ingest.accepted:
>     write_reason = primary.ingest.reason or "not_accepted"
> --- `kb/promotion.py`

At this workflow's terminal write boundary, `promoted` means accepted Central content plus an audit event, not completed indexing or demonstrated use. [RT-OBJ-ingest-result](runtime.md#rt-obj-ingest-result) and [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) establish the acceptance semantics. In lifecycle mode [RT-RTE-source-projection](runtime.md#rt-rte-source-projection) separately leases retained-source work and checks relational/vector/optional graph projections. Lexical retrieval can reach retained source without finished vector/graph work. Later permitted search selects shared material and [RT-RTE-task-search](runtime.md#rt-rte-task-search) delivers bounded untrusted context to a host; [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) does not force reliance. These are connected downstream consumers, not evidence that a particular promoted item reached an actual model invocation.

### 5. Rejection and recovery limits

Three rejection points differ. Before queueing, personal/secret content, unavailable or malformed verdicts, unfavorable scores and missing references settle as skips. A reviewer can reject a pending item, recording a rejection checked by later seat/content-hash decisions. During writing, secret or general write exceptions settle as `write_blocked`; non-exception ingestion refusals retain their own reason. Repeated accepted or duplicate-in-process Central text is tracked in an engine-local hash set to avoid redundant known-work classification. This set is not a durable cross-restart delivery ledger. SRC-1: `kb/promotion.py`.

Approval marks the pending item approved even when the attempted Central write fails; its return separates `promoted` and `write_reason`. The same item is consequently not a guaranteed retry handle: approve/reject both require it still be pending. The inspected code establishes neither transactional rollback across seat/Central writes nor an automatic re-open of failed approvals. Later projection recovery is owned by the lifecycle worker, not the reviewer, and cannot repair every pre-acceptance failure. SRC-1: `kb/promotion.py`; [RT-RTE-source-projection](runtime.md#rt-rte-source-projection).

> # The item is consumed either way, so the caller needs the server's
> # reason to tell "the write failed" from "this content is already
> # in Central" (an approval of the second of two identical pending
> # items is the ordinary way to hit the latter).
> "write_reason": None if promoted else outcome,
> --- `kb/promotion.py`

The Next review handler awaits the API call then reloads the list; it does not inspect the returned `promoted` field in that handler. Therefore its successful request path alone cannot certify accepted Central delivery. The backend response and audit are the more precise boundary. No browser execution or production recovery trace is supplied. SRC-1: `web/src/pages/app/review.tsx`, `kb/promotion.py`.

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

#### On [RT-RTE-promotion-review](runtime.md#rt-rte-promotion-review)

Workflow-specific handoffs: the scheduled stage owns seat iteration; a capped candidate supplies model triage; a pending item retains full text but the review-list consumer receives only preview/metadata; approval reloads full text for guarded dual writes. The admin decision is a veto for queued new-project work, not for every known-work promotion. Acceptance, indexing and host reliance are separate delivery milestones. A failed approval consumes the queue item and returns a write reason rather than guaranteeing retry. These details and their minimum source passages are retained in the Workflow account above; they refine the supplied route without changing its identity or evidence status.
