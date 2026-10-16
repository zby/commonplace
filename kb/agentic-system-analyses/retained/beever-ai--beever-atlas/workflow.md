---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Beever Atlas workflow: background message extraction through parallel agents, admission, retry and retained-memory delivery."
run-id: AAS-2026-10-15-beever-atlas-10a3512c094c-01
reviewed-boundary: "7d791af27ef4aa19644cb385c7ca24619bc4f848"
---

# Beever Atlas workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is background extraction of queued channel messages into retained memory, followed by notification of downstream maintenance. It is selected because it exposes coordinated model work, deterministic admission, checkpoint recovery and a concrete delivery boundary in one connected shipped path. It is not an invented sequence of independent QA tools. Its canonical container is [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion); this member adds workflow details rather than declaring that route again.

The evidence is implementation in SRC-1 at the revision fixed by [the boundary](boundary.md). Added inspection covers `src/beever_atlas/agents/ingestion/pipeline.py`, the session/retry portion of `src/beever_atlas/services/batch_processor.py`, the per-channel completion/failure portion of `src/beever_atlas/services/extraction_worker.py`, and fact admission/recovery in `src/beever_atlas/agents/callbacks/quality_gates.py`. These are source-level mechanisms, not observed successful execution. No target code, tests, examples or model providers were run.

### Request, scheduling and delegation

The initiating input is a pending message, not a conversational instruction to a supervising agent. Platform synchronization or the signed push endpoint persists messages; push acceptance explicitly means extraction is queued, not that knowledge or a wiki page has been delivered. A later worker claims pending rows, groups them by channel and passes normalized messages plus channel identity and a generated worker job identity to `BatchProcessor`. The worker, rather than a model, owns this handoff and its queue status. These entry and claim mechanisms are established in [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion) (SRC-1: `src/beever_atlas/api/sources.py`, `src/beever_atlas/services/extraction_worker.py`).

The processor supplies each batch with a system-owned working session. Alongside messages, its state includes channel/name, batch/job identifiers, known entities, embedding-similarity candidates, language and policy overrides for quality and extraction/graph skipping. It reloads selected checkpoint keys when available. This is selected context and shared output state, not delegation of authority to reschedule the pipeline or access every stored channel. The supplied [RT-OBJ-session-state](runtime.md#rt-obj-session-state) describes the session substrate; the retry handoff is further characterized in Annotations below (SRC-1: `src/beever_atlas/services/batch_processor.py`).

The constructor fixes the sequence: preprocessing fans out to fact and entity extractors; their outputs meet at `join_extract`; embedding and deterministic cross-batch validation run in parallel; `join_enrich` gates persistence. Fact and entity models propose content, but neither chooses the next worker or the graph topology. The two joins matter because simply connecting multiple predecessors is not the same as one combined downstream invocation. The source documents that distinction and inserts actual `JoinNode` instances. The guarantee remains conditional on dependency semantics, as the runtime report states; it does not deduplicate independent batch retries (SRC-1: `src/beever_atlas/agents/ingestion/pipeline.py`; [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)).

### Verification, rejection and recovery

Verification here means admission of extracted representations, not proof of factual truth. Shipped extraction guidance asks models for structured facts/entities. The fact callback then filters returned candidates against a configured quality threshold and bridges the admitted list into the embedder's input. The score itself comes from extracted output; testing it is not an independent expected-answer oracle. Neither starting ingestion nor authenticating a push constitutes human approval of individual derived facts. The separately recorded admission step below makes this distinction explicit.

Malformed fact output need not abort the batch. The callback attempts JSON recovery, sends recovered facts through the same gate, and otherwise replaces the output with an empty list carrying an extraction-failure reason. Thus an extraction stage can advance with no admitted facts. An empty output is not evidence that the channel contained no knowledge. This is a concrete source-supported failure branch, not a reliability claim (SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py`; [WF-RTE-fact-admission](#wf-rte-fact-admission)).

Failures that escape the pipeline are handled at another level. `BatchProcessor` has fresh-session checkpoint-aware retries. The worker then owns durable row finalization: an exception from processing marks the normalized batch failed; a result with sub-batch errors separates successful and failed keys where breakdown provenance exists. When breakdown keys are unavailable it falls back to failing the batch. Failed rows receive a next-attempt timestamp based on their attempt count. These are recovery opportunities, not transactional rollback of any already completed store effects (SRC-1: `src/beever_atlas/services/batch_processor.py`, `src/beever_atlas/services/extraction_worker.py`; annotation on [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)).

### What counts as delivery

On the worker's success branch, it marks valid message keys done and then emits extraction completion with channel and fact IDs. With partial success, it notifies for succeeding sub-batches while scheduling failed keys separately. Subscribers may receive an empty fact-ID list and route by channel or rescan. The delivered handoff is therefore retained-memory output plus a completion signal, not the full extraction session or a verified answer to a person (SRC-1: `src/beever_atlas/services/extraction_worker.py`).

Even this terminal must be interpreted narrowly. Persistence is not an atomic vector-and-graph commit: graph failure alone does not prevent intent completion, as [RT-CLM-write-completion](runtime.md#rt-clm-write-completion) establishes. Completion/status messages cannot establish all-store consistency, truth or eventual recovery. Downstream wiki maintenance is a separately scheduled consumer with its own model, parser and curation gates, described by [RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance); a worker completion does not prove that a page was refreshed. QA is a later request, not a mandatory final stage of each extraction. No supplied trace establishes that this sequence ran, that every subscriber was active or that later answers improved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-fact-admission
Label: Fact output admission

Part of: [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)

This is the callback-level admission part of the supplied ingestion container, not an alternative ingestion route. Endpoints/progression: fact extractor state output → `fact_extraction_with_recovery` → `fact_quality_gate_callback` → filtered `extracted_facts` and `classified_facts` for enrichment. The model proposes fact content and quality scores; callback code decides retention using per-channel state threshold or the global setting, after attempting narration filtering. No per-fact human approval or reference-answer oracle is established. Operating mode is automatic processing of incoming messages, not a bounded experiment. The guidance remains shipped extraction policy; the callback changes candidate facts, not the extraction instructions. SRC-1: `src/beever_atlas/agents/callbacks/quality_gates.py`; the extraction component and instruction attachment are established by [RT-CMP-fact-extractor](runtime.md#rt-cmp-fact-extractor).

- Immediate return: callback returns control after modifying session state, including an empty-facts fallback when recovery fails.
- Later read-back: inapplicable — this callback writes working state; persistence and subsequent consumption are owned by the enclosing ingestion route.
- Delegated visibility: enrichment receives the filtered dictionary through `classified_facts`, not necessarily every original model candidate.
- Selection predicate: candidate `quality_score` must meet the resolved threshold; recoverable string output is parsed before the normal gate.
- Invalidation or expiry: callback overwrites the current fact-state keys; durable invalidation is outside this part.
- Activation or effect: changes which candidates are made available to downstream enrichment; actual retention and downstream use were not observed.
- Evidence limits: threshold admission is not independent truth verification; narration-filter exceptions continue with unfiltered facts, and recovery may yield partial or empty output.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Rejection/recovery: low-scoring candidates are removed. String output gets a recovery attempt; recovered facts re-enter the normal gate. If recovery fails, the fallback replaces rather than restores the original candidate set. This is automatic admission with loss-tolerant continuation, not a human veto or semantic rollback.

> filtered = [f for f in facts_dicts if f.get("quality_score", 0.0) >= threshold]
> --- `src/beever_atlas/agents/callbacks/quality_gates.py`

> callback_context.state["extracted_facts"] = {"facts": [], "skip_reason": "extraction_failed"}
> --- `src/beever_atlas/agents/callbacks/quality_gates.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-message-ingestion](runtime.md#rt-rte-message-ingestion)

Workflow recovery ownership: processor retries reconstruct a fresh system session and reconsult the checkpoint store before retrying. This discards the previous mutable frame while restoring selected completed-stage outputs, rather than giving a new model the whole failed interaction. The restored snapshot can affect the next attempt; raw conversation continuity is not the recovery contract. The inspected implementation does not establish whether a later worker tick, with a new generated job identity, can reuse a prior tick's checkpoint (SRC-1: `src/beever_atlas/services/batch_processor.py`, `src/beever_atlas/services/extraction_worker.py`).

> _retry_checkpoint = await stores.mongodb.load_pipeline_checkpoint(
>     sync_job_id=sync_job_id,
>     batch_num=batch_index,
> )
> --- `src/beever_atlas/services/batch_processor.py`

Worker completion/rejection ownership: successful and failed sub-batch keys are finalized separately where provenance exists. For failures, the worker schedules per-attempt backoff, rather than assuming a processor retry has fixed the batch. Completion signals are downstream work requests, not verification of subscriber delivery or all-store correctness (SRC-1: `src/beever_atlas/services/extraction_worker.py`).

> await stores.mongodb.finalize_extraction_status_bulk(
>     keys=keys,
>     new_status="failed",
>     last_error=error[:500],
>     next_attempt_at=now + timedelta(seconds=offset),
> )
> --- `src/beever_atlas/services/extraction_worker.py`
