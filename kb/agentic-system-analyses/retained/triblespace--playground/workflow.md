---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Playground workflow: caller-directed long-running shell work, admission, polling, cancellation and bounded result delivery."
run-id: AAS-2026-10-14-playground-88ee8a292f9b-01
reviewed-boundary: de28ac8fdda30c7a5c2ee099de089e65a685195f
---

# Playground workflow report

## Workflow account

The representative workflow is a client opening a tenant sandbox, starting a long-running shell command, polling its result and releasing the sandbox handle. It was selected because the shipped tools explicitly connect these steps through session IDs, job IDs and output cursors. This is the provider-side portion of an agent workflow, not a demonstrated autonomous agent task: the enclosing client supplies the purpose, shell commands, interpretation and continuation. No source-supported task-level plan, model-to-model delegation or completed agent deliverable is established within this boundary. The code establishes a callable sequence, not evidence that a client executed it. SRC-1: `src/mcp.rs`, `src/jobs.rs`; [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec), [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs).

**Admission and opening.** Assume the operator has already provisioned the tenant and an authenticated sandbox HTTP service; provisioning is a separate administrative prerequisite, not a per-command approval. HTTP binds calls to the authenticated tenant and checks ownership before dispatch. The stdio alternative lacks that HTTP admission layer. Opening returns the tenant's stable backend session ID and increments a shared handle count. It does not create a fresh independent workspace for every client. The provider rechecks session registration under a per-tenant lifecycle lock before starting execution, preventing a start from slipping through last-handle detach. SRC-1: `src/mcp.rs`, `src/mcp_http.rs`; [RT-RTE-tenant-provision](runtime.md#rt-rte-tenant-provision), [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec).

**Delegation and execution.** The client submits `job_exec` with the open session, shell command and optional execution parameters. The provider constructs an `ExecRequest`; the job manager admits it and hands it to a host thread calling the configured backend. This delegates execution, not agent reasoning. The backend gets the session, request and cancellation/output control; it does not get an independently assembled model conversation. Retained execution is rejected unless the backend advertises proven background-job cancellation. Thus this workflow applies to the capable root-local FreeBSD path, not indiscriminately to Lima or SSH. The synchronous `exec` route is the advertised fallback, not an automatic replay. SRC-1: `src/mcp.rs`, `src/jobs.rs`; [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs).

**Return and delivery.** Start returns a job ID, an initial cursor and a running label, not the completed command result. The client owns subsequent `job_poll` requests and must advance through pages. Polling returns chunks, next cursor, gap/dropped-byte information and any terminal result. Output is bounded, so a terminal state alone cannot establish a complete transcript. Sealing the output sink before terminal publication prevents later chunks from arriving after a final page. These are transport/execution checks, not verification that the command accomplished the client's task. SRC-1: `src/mcp.rs`, `src/jobs.rs`; [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs).

The consequential delivery limit is that producing the terminal final page marks the handle observed on the server, before any network acknowledgement. A later submission may recycle it. The client must therefore retain returned pages before requesting more work; the provider does not establish client receipt or model consumption. SRC-1: `src/jobs.rs`.

> // owns the last page. This records server-side observation, not a
> // network delivery acknowledgement: callers must retain returned
> // pages before submitting work that may recycle a completed id.
> --- `src/jobs.rs`

**Rejection and recovery.** When retained slots are occupied by live or unread terminal jobs, admission refuses additional work rather than silently discarding those outcomes for capacity. The error directs the client to poll terminal output; observed terminal handles can then yield capacity. Terminal TTL remains a separate expiry exception, and daemon restart loses handles. Tool-level failures return MCP `isError` content. The provider does not generate a revised command or retry side effects on the client's behalf. SRC-1: `src/jobs.rs`, `src/mcp.rs`; [RT-CMP-job-manager](runtime.md#rt-cmp-job-manager), [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs).

> "job table is full ({MAX_RETAINED_JOBS_GLOBAL} live/unobserved jobs); poll terminal output before submitting more"
> --- `src/jobs.rs`

If the client elects cancellation, `job_cancel` requests it and reports the current state. A cancelling state is not completion: the backend must return before the job becomes terminal. Normal completion, cancellation and backend failure become distinct terminal outcomes. Loss of execution control on a capable backend closes admission and triggers the fatal handler rather than promising safe reuse. Recovery of task intent and inspection of any partial filesystem effects remain client/operator responsibilities; cancellation does not establish rollback. SRC-1: `src/jobs.rs`; [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs).

**Closing.** After collecting results, the client releases its sandbox handle. Last-handle close detaches without permanent workspace deletion. A failed backend close leaves the registry entry available for a retry; permanent destruction is operator-only. Persistent files can support a later task, but the transient job ledger is not a durable delivery receipt. SRC-1: `src/mcp.rs`; [RT-CLM-persistent-sandbox](runtime.md#rt-clm-persistent-sandbox), [RT-CMP-job-manager](runtime.md#rt-cmp-job-manager).

> // ssh/limactl). We remove the entry only after the close succeeds so
> // a failed close leaves the session known (and retryable).
> --- `src/mcp.rs`

Additional SRC-1 implementation inspection covered provider lifecycle/start logic, tool dispatch and job-tool response construction in `src/mcp.rs`, and cancellation, terminal publication, final-page observation, retention admission and thread dispatch in `src/jobs.rs`. No target or tests were executed. The native-worker gateway is a separate route, not a stage spliced into this workflow; its downstream native tool workflow remains outside the frozen implementation. SRC-1: `src/mcp.rs`, `src/jobs.rs`; [RT-RTE-worker-forward](runtime.md#rt-rte-worker-forward).

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

#### On [RT-RTE-retained-jobs](runtime.md#rt-rte-retained-jobs)

Workflow responsibility: the client sequences start, poll and optional cancel, retains returned pages and judges task adequacy. The provider delegates shell execution, not a separate model subtask. Admission can reject unsupported background execution or exhausted capacity; it cannot certify semantic success. The workflow's delivery boundary is result construction, not acknowledged client receipt. Recovery after ordinary rejection belongs to the client; control-loss fail-stop requires operator attention. No automatic command revision or rollback is established by this route.

#### On [RT-RTE-sandbox-exec](runtime.md#rt-rte-sandbox-exec)

Workflow sequencing: open precedes job start, while handle release follows the caller's result collection. The lifecycle lock protects registration/start/detach ordering, not the semantic ordering of concurrently submitted commands. A failed last-handle detach remains retryable. Persistent workspace availability and completed job delivery have different lifetimes and must not be treated as one completion guarantee.
