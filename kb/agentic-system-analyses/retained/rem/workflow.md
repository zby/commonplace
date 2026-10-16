---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "REM workflow account tracing the shipped LangChain before/after memory hooks, later read-back, rejection and recovery limits."
run-id: AAS-2026-10-14-rem-a81fdc774400-01
reviewed-boundary: "935e8be0a1fca5b23dbabfe16c48b562c1cd24cc"
---

# REM workflow report

## Workflow account

The representative workflow is the LangChain adapter's retrieve-before-response, save-after-response cycle, followed by another retrieval. It was selected because one shipped adapter explicitly connects both sides of an agent interaction; it does not require joining unrelated memory capabilities. The source establishes the hooks and attempted service handoffs, not a successfully executed agent conversation. Nonempty ordinary Go retrieval results fail SDK typed conversion before the adapter returns its memory variable; the selected cycle therefore does not establish delivered retained context. The external host still owns model invocation and final answer delivery. This account uses SRC-1 at the frozen boundary; no target code or services were executed. Detailed source inspection covered `sdk/python/rem_memory/integrations/langchain.py`, the complete `sdk/python/rem_memory/client.py`, `go-api/internal/api/handlers/episodes.go`, and both complete `go-api/internal/services/write_service.go` and `go-api/internal/services/retrieve_service.go`. Correction inspection additionally covered `sdk/python/rem_memory/types.py` and `go-api/internal/domain/episode.go`, and reread the complete SDK client and LangChain adapter to check the retrieval constructor and exception boundaries. These supply implementation evidence, not observed operation. The existing route identities remain those in [RT-RTE-host-integration](runtime.md#rt-rte-host-integration), [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve) and [RT-RTE-episode-write](runtime.md#rt-rte-episode-write).

### Request and context handoff

The host configures REMMemory with an API key and agent ID; the adapter defaults user ID to `default`, uses `REM_BASE_URL` or the hosted URL, and exposes `relevant_memories` by default. Its load hook selects the first nonempty `input`, `question` or `human_input`. Missing query or client returns an empty memory variable rather than initiating retrieval. Otherwise it calls the SDK with that query, configured agent ID, five episode results and semantic inclusion enabled. These are software-controlled handoffs, not delegation to an autonomous task-performing subagent (SRC-1, `sdk/python/rem_memory/integrations/langchain.py`).

Go owns retrieval progression after API admission. It obtains a query embedding, searches retained vectors, reloads episodes, expands temporal neighbors of up to three initial hits, and reranks episodes before formatting context. The embedding provider sees the query. Go constructs a string containing selected raw episode text and any semantic fact/confidence lines, available to a direct HTTP consumer; the selected SDK-mediated workflow must complete typed conversion before the host can receive that string. Selection does not verify truth. The five-episode limit is not a token budget, and semantic results have a separate selection path. See [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve); SRC-1, `go-api/internal/services/retrieve_service.go`.

Only after successful SDK conversion does the adapter hand back the injection string under its memory key:

> return {self.memory_key: result.injection_prompt}
> --- `sdk/python/rem_memory/integrations/langchain.py`

That mapping is the intended REM-side context-delivery boundary, not a reached handoff for nonempty ordinary Go episode or semantic results. Their required-timestamp constructor failures occur before RetrieveResult construction, so the existence of the server-built string does not establish adapter delivery. The source's usage example installs the adapter on a ConversationChain, but the inspected REM files do not establish actual framework startup, prompt placement or model compliance. The external host must incorporate the memory variable, invoke its model and deliver its answer. [RT-BAP-context-injection](runtime.md#rt-bap-context-injection) describes this advisory text channel, not an enforced instruction or grant of tool authority.

### Response retention and subsequent use

After a host response, the save hook selects the same human-input alternatives and the first nonempty `response`, `output` or `text` output. No human input means no write. Otherwise it constructs one episode description:

> content = f"Human: {human_input}\nAssistant: {ai_output}"
> --- `sdk/python/rem_memory/integrations/langchain.py`

It supplies that content, configured agent/user IDs and a fixed success label to the SDK. This does not transfer the host's full tool history or verified task outcome. Empty assistant text is not independently rejected by this hook. No reviewer approves the response before this write; neither the success label nor the host response is an independent answer oracle (SRC-1, `sdk/python/rem_memory/integrations/langchain.py`; [RT-RTE-host-integration](runtime.md#rt-rte-host-integration)).

The SDK submits the episode; Go validates it, creates its identity, requests best-effort parse metadata and requires an embedding before sequential PostgreSQL, Qdrant and Neo4j writes. Parser failure can leave defaults without rejecting the raw exchange. The parser interprets content; it does not certify that the assistant answered correctly. A successful service result carries `stored`, and the handler returns 201. The adapter itself discards the WriteResult and returns from saving. Thus answer delivery, episode storage acknowledgement and semantic consolidation completion are three different boundaries (SRC-1, `go-api/internal/services/write_service.go`, `go-api/internal/api/handlers/episodes.go`, `sdk/python/rem_memory/integrations/langchain.py`; [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)).

On a later host request, the same load hook requests retained exchanges under the configured agent ID. It does not replay the whole conversation: the Go string contains only selected episodes and semantic hits. Nonempty ordinary Go results fail SDK conversion before that string reaches the memory variable, so this later request is not evidence of completed adapter read-back. Actual selection of a particular newly stored exchange and any change to the host's next answer remain unobserved. The adapter's clear hook is explicitly a no-op, so clearing host memory through this interface does not remove retained REM episodes; see [RT-RTE-host-integration](runtime.md#rt-rte-host-integration).

### Rejection, failure and recovery ownership

A concrete rejection path is a short exchange. SDK write validation requires at least ten trimmed characters, while the Go handler requires a trimmed byte length strictly greater than 50 and less than 10000. An adapter-produced exchange can therefore pass SDK validation but receive HTTP 400 before the write service runs:

> if l := len(req.Content); l <= 50 || l >= 10000 {
> --- `go-api/internal/api/handlers/episodes.go`

The SDK converts 400 to ValidationError; the save hook has no catch or compensating fallback. The host owns recovery from that exception. This is structural rejection, not rejection of an incorrect answer. The inspected SDK retries connection errors and timeouts, not this validation response (SRC-1, `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/integrations/langchain.py`).

The SDK's default request loop allows three attempts. Connection failures back off; timeouts wait before retry. A timeout after a server-side episode write can cause another POST with a fresh server-generated episode identity. Sequential multi-store failures can also leave earlier writes behind. The workflow therefore provides neither transactional rollback nor exactly-once retention; caller recovery must not assume that an exception proves nothing was stored. These storage findings and their evidence are retained in [RT-RTE-episode-write](runtime.md#rt-rte-episode-write).

Retrieval has a different failure boundary. Search and graph errors can be logged while Go returns partial context; an embedding failure prevents retrieval completion. Even a Go success can fail before the adapter returns its memory variable. Go's untagged Episode fields serialize as PascalCase, including CreatedAt, while the SDK looks up created_at and passes None to EpisodeResult's required non-null datetime. Thus any nonempty ordinary Go episode results reject typed conversion rather than merely losing structured fields. Independently, Go's SemanticResult omits created_at, so nonempty semantic hits also pass None to a required datetime in SemanticMemory. Both constructors run before RetrieveResult construction and access to its injection_prompt; these failures apply even to a non-null semantic list. The supplied runtime retains the episode and semantic schema evidence in [RT-OBJ-episode](runtime.md#rt-obj-episode) and [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve). SRC-1: `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/types.py`, `go-api/internal/domain/episode.go`.

The SDK's return object is constructed only after both conversion loops:

> result = RetrieveResult(
>     episodes=flat_episodes,
>     semantic_memories=semantic,
>     injection_prompt=raw.get("injection_prompt", ""),
>     latency_ms=int(raw.get("latency_ms", 0)),
> )
> --- `sdk/python/rem_memory/client.py`

A null semantic list is a separate iteration failure: the SDK does not normalize it before looping. The adapter catches neither constructor nor iteration failures, and has no fallback returning the server's raw injection string. Transport retries do not handle these post-response conversion exceptions. Recovery belongs to the host; the inspected adapter does not implement it. A direct HTTP consumer can obtain Go's separately constructed string without these SDK constructors, but that alternate route does not repair the selected workflow. These source-derived findings establish neither an observed failure rate nor successful host recovery (SRC-1, `sdk/python/rem_memory/client.py`, `sdk/python/rem_memory/integrations/langchain.py`, `go-api/internal/services/retrieve_service.go`; [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve)).

Finally, successful retention is not a verified route to learned semantic context. Background publication is detached from episode acknowledgement; the supplied runtime establishes no shipped Redis-list-to-Celery bridge and no accepting semantic POST or consolidated-episode PATCH routes. Explicit task dispatch or direct candidate computation does not repair durable admission. Accordingly this workflow can trace episodic write attempts and server read selection, but cannot claim delivered nonempty SDK context or a completed automatic Write → Consolidate → Retrieve cycle. Its write account is conditional on an already running, prepared service and an existing agent row: the startup migration and agent foreign-key limits in [RT-RTE-episode-write](runtime.md#rt-rte-episode-write) prevent inferring fresh-install readiness or self-provisioning from the adapter. See [RT-ABS-worker-bridge](runtime.md#rt-abs-worker-bridge), [RT-ABS-writeback-routes](runtime.md#rt-abs-writeback-routes), [RT-RTE-worker-consolidation](runtime.md#rt-rte-worker-consolidation) and [RT-RTE-direct-consolidation](runtime.md#rt-rte-direct-consolidation). No operator-added repair or successful downstream task is inferred.

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

#### On [RT-RTE-host-integration](runtime.md#rt-rte-host-integration)

Workflow role: before/after hooks bracket a host-owned response, not a REM-owned task executor. The intended context handoff is selected text into a memory variable, but nonempty ordinary Go episode or semantic results fail required-timestamp SDK conversion before that return. The separate save handoff supplies the human/assistant exchange to episode admission. The host owns response delivery and recovery from uncaught hook exceptions. Save completion acknowledges only the retention call, not answer correctness or consolidation. Subsequent invocation requests selected retained content, but SDK constructor failures prevent ordinary nonempty results reaching this adapter's memory variable. Host use and effects on the answer remain unobserved.

#### On [RT-RTE-episode-write](runtime.md#rt-rte-episode-write)

Workflow verification boundary: handler checks can reject an exchange accepted by SDK length validation. Admission checks shape and dependency success, not correctness of the host's response. The adapter has no local failure handler; SDK transport retries can repeat admission after an uncertain response. No workflow-level repair closes partial multi-store writes.

#### On [RT-RTE-context-retrieve](runtime.md#rt-rte-context-retrieve)

Workflow delivery boundary: a successful API response is still upstream of SDK conversion and memory-variable return. Nonempty ordinary Go episodes pass None for the SDK's required created_at because Go emits CreatedAt; nonempty semantic hits independently lack that required timestamp. Both fail before RetrieveResult and memory-variable return, even with non-null lists. Null semantic lists separately interrupt iteration. Go can still construct partial context without a completeness gate, accessible to a direct HTTP consumer; this is not successful adapter delivery. Neither SDK conversion nor the adapter provides a fallback or recovery handler. Host prompt use and final answer acceptance remain outside REM's ownership and unobserved.
