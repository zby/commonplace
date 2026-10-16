---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Semiont's annotation-to-resource workflow through context gathering, delegated generation, record admission and caller delivery."
run-id: AAS-2026-10-15-semiont-d516c7013d8f-01
reviewed-boundary: a920067ac4ea63a57b1855b7d263485fbd22bab4
---

# Semiont workflow report

## Workflow account

### Selected workflow and evidence limit

The selected workflow is the shipped MCP `yield_from_annotation` operation: gather knowledge around an existing annotation, delegate generation, persist the generated resource and report completion to the caller. It is representative because one handler explicitly joins retrieval to queued model work and a durable write; it is not a hypothetical composition of unrelated tools. The enclosing assistant that chooses this operation remains outside the analysis. The handoffs inside Semiont are predominantly fixed service orchestration, not agents autonomously choosing successive tools. SRC-1, `packages/mcp-server/src/handlers.ts`; [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather), [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation).

This account characterizes implementation at the frozen revision, not a successful execution. No supplied trace establishes that a request traversed these stages, that generated claims were correct or that a later consumer benefited. Direct source inspection for this member covers the MCP gather/yield handlers, Worker `run_job`/failure handling, `_yield`/citation entry and `process_generation_job`. These are implementation-layer extensions or rechecks under SRC-1, not new sources. Service wiring, queue admission, gathering transformations and record provenance checks also rely on the supplied runtime records. Browser/desktop review and deployment-specific supervision remain uninspected here.

### 1. The caller chooses the task; the handler gathers its input

The external MCP caller supplies the resource and annotation identifiers and may supply a title, destination storage URI, instruction and language settings. The handler first asks the Librarian for annotation context with `contextWindow: 2000`. It passes the returned context by value into generation. Source language defaults from gathered metadata unless the caller overrides it. No external assistant conversation is copied into this handoff. SRC-1, `packages/mcp-server/src/handlers.ts`.

> const ctx = gatheredContext(await semiont.gather.annotation(rId, aId, { contextWindow: 2000 }));
> --- `packages/mcp-server/src/handlers.ts`

The Librarian reads the annotation and source view, obtains selected surrounding text, graph relationships and semantic neighbors, and can invoke its own inference client for supplementary prose. Supplementary failures may yield degraded context rather than reject the whole request. Generation does not consume every gathered field: its prompt selects annotation text, hint, surrounding text, graph/relationship material and a bounded set of similar passages; linked-target content/summary is not separately rendered in the annotation prompt. Thus a successful gather is neither a completeness certificate nor proof that every retrieved source reached the generating model. SRC-1, `apps/librarian/src/semiont_librarian/annotation_gather.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`; [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather).

### 2. The platform delegates a job, not an unrestricted conversation

The handler calls `yield.delegate` with the gathered context and caller options. Gateway code supplies the authenticated principal; Dispatcher code validates and queues the request and matches eligible worker claims. Worker-role authorization and job filters govern who can claim; the Worker rechecks its accepted filters and generation parameters. The job input reaches the assigned worker, while the yield announcement omits context. These are different visibility surfaces, not a demonstrated tenant-isolation guarantee. SRC-1, `apps/gateway/src/routes/bus.rs`, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/handlers/src/handlers.rs`, `apps/worker/src/semiont_worker/held_job.py`; [RT-OBJ-job-params](runtime.md#rt-obj-job-params), [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation).

The client chooses the operation and supplies its instruction; Dispatcher owns scheduling; Worker code owns processor choice and prompt assembly; the configured model proposes document text. The Worker does not ask the model to schedule follow-up services. The context is a submitted snapshot, not automatically refreshed before generation or verified as a truthful representation of the current KB. Configuration selects the Worker provider/model; this is not a model-selected specialist roster. SRC-1, `apps/worker/src/semiont_worker/service.py`, `apps/worker/src/semiont_worker/generation/resource_generation.py`; [RT-CMP-worker-inference](runtime.md#rt-cmp-worker-inference), [RT-BAP-generation-prompt](runtime.md#rt-bap-generation-prompt).

### 3. Verification is structural; generated content is admitted automatically

This MCP wrapper does not forward an output format or `cite` option. The Worker processor defaults an unspecified format to Markdown. A PDF compilation/repair capability exists on other generation requests, but it is not an evidenced stage of this wrapper's ordinary workflow. Likewise, citation-capable generation does not establish that this handler requests source citation tokens. SRC-1, `packages/mcp-server/src/handlers.ts`, `apps/worker/src/semiont_worker/processors.py`; [RT-RTE-pdf-repair](runtime.md#rt-rte-pdf-repair), [RT-CLM-source-grounding](runtime.md#rt-clm-source-grounding).

The processor validates generatable media type and output budget, then produces an artifact. The Worker uploads bytes with source resource/annotation IDs, the instruction, generator identity and job ID. The authenticated content route and Archivist perform admission; worker-role creation must cite the job and match its recorded holder. Those checks establish attribution requirements, not a factual answer oracle. There is no inspected per-document human approval between the model response and this upload. Initiating the request is not approval of the generated content. SRC-1, `apps/worker/src/semiont_worker/processors.py`, `apps/worker/src/semiont_worker/held_job.py`, `apps/archivist/src/commands.rs`; [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission).

### 4. Storage, job completion and caller delivery are separate boundaries

The upload returns a new resource ID. For an annotation-focused request the upload itself requests the source binding; the Worker's separate whole-source linking branch applies only when no annotation ID is present. After upload, the Worker commits any generated citation annotations and completes the job with resource ID, name and truncation flag. Bytes do not travel through the progress bus. Source binding, content creation, annotation commits and terminal queue state are not one distributed transaction. SRC-1, `apps/worker/src/semiont_worker/held_job.py`; [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission).

> await job.complete(JobGenerationResult(resource_id=new_resource_id, resource_name=made.title, truncated=made.truncated))
> --- `apps/worker/src/semiont_worker/held_job.py`

The MCP wrapper waits for the delegated observable and accumulates progress strings. Its delivered result is a textual success notification plus progress, not the document, resource ID or truncation flag from the Worker completion payload. A later browse/gather can consume retained content, but this handler does not itself perform that read-back. A client receiving its success text has a narrower result than the queue completion record. SRC-1, `packages/mcp-server/src/handlers.ts`; [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation).

> return { content: [{ type: 'text', text: `Generation complete.\n${progressMessages.join('\n')}` }] };
> --- `packages/mcp-server/src/handlers.ts`

### Failure, rejection and recovery

A cancellation observed after the model answers can stop this workflow before upload: the processor returns `Cancelled`, and the Worker settles the job as cancelled without creating a resource in that branch. It does not interrupt the provider request immediately. Once upload has occurred, cancellation or a later failure does not imply rollback. The Archivist can also retain created content despite an automatic-link failure; resource existence alone therefore does not establish complete lineage or successful queue settlement. SRC-1, `apps/worker/src/semiont_worker/processors.py`, `apps/worker/src/semiont_worker/held_job.py`, `apps/archivist/src/commands.rs`; [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission).

> if isinstance(made, Cancelled):
>         # Cancelled by the time its model had answered: nothing is uploaded and nothing committed.
>         await reports.taken()
>         await job.cancel()
>         return "cancelled"
> --- `apps/worker/src/semiont_worker/held_job.py`

A generation exception is caught by `run_job` and reported as a classified failure with available checkpoint information. If failure reporting itself fails, the implementation leaves settlement to Dispatcher sweeping. Yield admission gives zero retries, unlike mark jobs; no automatic regenerated replacement should be inferred for this workflow. Dispatcher stale-job handling and supervisor restart are recovery responsibilities, not evidence of exactly-once effects or successful content repair. SRC-1, `apps/worker/src/semiont_worker/held_job.py`, `apps/dispatcher/handlers/src/admission.rs`, `apps/dispatcher/jetstream/src/lib.rs`; [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation), [RT-RTE-mark-detection](runtime.md#rt-rte-mark-detection).

> # The failure itself could not be said. The job is released, and the dispatcher's sweep concludes it.
> --- `apps/worker/src/semiont_worker/held_job.py`

The MCP generation `try` converts delegation-stream errors to an error response. The preceding gather is outside that local `try`, so this particular conversion does not cover gather failure; the surrounding MCP dispatch boundary is not characterized here. No failed-path execution was supplied. SRC-1, `packages/mcp-server/src/handlers.ts`.

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

#### On [RT-RTE-annotation-gather](runtime.md#rt-rte-annotation-gather)

Workflow role: prerequisite handoff from the MCP wrapper to generation. The wrapper waits for this result before delegating; gather failure therefore prevents creation of the generation job through this handler. The gather's local context snapshot can be degraded and is selectively rendered by the downstream Worker. It is not an independent verification verdict on the proposed document.

#### On [RT-RTE-yield-generation](runtime.md#rt-rte-yield-generation)

Workflow role: central delegated operation. Request ownership stays with the client; scheduling, model execution and record admission belong to different platform actors. Delivery has two levels: Worker completion carries the resource identity and truncation flag, while the selected MCP wrapper returns only success text and collected progress. In this wrapper, the caller is not handed the generated bytes or new resource ID.

#### On [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission)

Workflow role: durable-effect boundary before final job settlement. A successful content write can outlive failure of a subsequent annotation commit or completion report. Retrying the overall request is therefore not established as a rollback-safe recovery strategy. The assignment/holder checks are attribution controls, not content-quality acceptance.
