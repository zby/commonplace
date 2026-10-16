---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Stash workflow account: caller-directed session memory, episode-to-fact consolidation, rejection recovery and later MCP recall."
run-id: AAS-2026-10-15-stash-7ac5612837a0-01
reviewed-boundary: d34ed430c4348ef741ef95146b488aea8616f4fb
---

# Stash workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **retain a session observation, consolidate it into a fact, and retrieve relevant memory in a later session**. It is selected because the shipped session protocol explicitly connects these operations, and implementation connects the persisted episode to consolidation and subsequent fact recall. This is not a reconstructed general-purpose task-solving loop. Stash coordinates storage and model-dependent maintenance; the external agent coordinates session timing and decides what to do with returned memory. The account establishes a source-supported workflow contract and its implementation, not an observed successful session. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`, `internal/brain/episode.go`, `internal/brain/consolidate.go`, `internal/brain/recall.go`]

> 1. remember a summary of what was accomplished (2-3 sentences, self-contained)
> 2. consolidate IF significant new knowledge was added this session
> --- `cmd/cli/mcp_prompts.tmpl`

The inspected SRC-1 ranges add focused workflow coverage of `cmd/cli/mcp_prompts.tmpl` (server description and initialization/namespace guidance), `cmd/cli/mcp.go` (initialization, remember, recall and consolidation handlers), `internal/brain/episode.go` (Remember), `internal/brain/consolidate.go` (orchestration, stage-one admission, clustering and deduplication), `internal/reasoner/openai.go` (ReasonStructured), and `internal/brain/recall.go` (complete retrieval function). These supply implementation and doctrine/design evidence at the frozen revision. Secondary maintenance stages are traced only as orchestration handoffs here, not as independent correctness audits. No target code, provider, test or service was executed. No supplied execution trace establishes agent compliance, successful synthesis or downstream answer improvement.

### 1. The external agent chooses the request and memory inputs

The MCP description asks the agent to initialize, inspect namespaces, recall relevant history before answering, store durable observations during work, and retain a self-contained session summary before closing. Initialization creates the `/self` namespace scaffold; it does not itself create every project namespace. The protocol asks the agent to choose a specific existing namespace or create one when missing. These are natural-language instructions delivered through [RT-OBJ-server-description](runtime.md#rt-obj-server-description) and [RT-BAP-agent-protocol](runtime.md#rt-bap-agent-protocol), not a Go-enforced session state machine. The remember handler can be called without a prior initialization check. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`]

The agent supplies the observation or session summary and exact namespace to MCP `remember`. Stash neither observes the original task directly nor verifies that the text accurately reports it. Generic tool-caller identity does not establish whether a human selected or approved the content. The shipped instruction to prefer durable signal shapes the proposed input, but storage admission uses Brain validation and database/provider success rather than a semantic quality judge. This is [RT-RTE-remember-write](runtime.md#rt-rte-remember-write). [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`, `internal/brain/episode.go`]

### 2. The write handoff persists an episode, not a completed task

The MCP handler passes content and namespace to `Brain.Remember`. Brain validates them, resolves the exact namespace, requests an embedding, and inserts the episode with the embedding model label and occurrence time into PostgreSQL. Successful return is an episode ID serialized as MCP text. A missing namespace, embedding failure or failed insert returns an error rather than that acknowledgment. The text is natural language, its vector is a separate dense representation, and the namespace/ID/timestamps are symbolic metadata. The acknowledgment establishes the write endpoint in code; it is not verification of the original task or of later recall usefulness. [RT-RTE-remember-write](runtime.md#rt-rte-remember-write); [SRC-1: `cmd/cli/mcp.go`, `internal/brain/episode.go`]

### 3. Consolidation transfers semantic work to the reasoner

For the selected foreground path, the agent calls MCP `consolidate` with namespaces. The handler resolves namespace IDs and invokes `ConsolidateByID` sequentially for each. Brain loads progress and owns the next maintenance stage. This does not launch a sub-agent with independent tools: it calls a reasoner adapter for a bounded semantic transformation, then resumes Go-controlled admission. Background/manual alternatives are already covered by [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run); they do not require the foreground agent to follow this session sequence. [SRC-1: `cmd/cli/mcp.go`, `internal/brain/consolidate.go`, `internal/reasoner/openai.go`]

Stage one fetches a namespace's checkpointed episode batch and clusters episodes by vector similarity. The handoff to `ReasonStructured` supplies each cluster's episode texts, not the enclosing agent's whole session or its complete conversation. The adapter sends static system guidance plus an event-list synthesis request to the configured chat-completions model. The requested return is JSON with entity, property, value and summary. The model proposes semantic content; Go owns decoding, checking, later embedding and insertion. This is maintenance over retained batches, not an experiment with a reference-answer oracle. [RT-CMP-openai-reasoner](runtime.md#rt-cmp-openai-reasoner), [RT-BAP-extraction-policy](runtime.md#rt-bap-extraction-policy); [SRC-1: `internal/brain/consolidate.go`, `internal/reasoner/openai.go`]

> sf, err := b.reasoner.ReasonStructured(ctx, texts)
> llmCalls++
> if err != nil {
> errs = append(errs, fmt.Sprintf("reason structured: %v", err))
> continue
> }
> --- `internal/brain/consolidate.go`

### 4. Verification is bounded admission, not a truth certificate

The adapter extracts and decodes JSON, then calls the grounding validator. Parse or grounding failure can trigger one further application-level model attempt with an appended warning. Provider-call failure or an empty response instead returns immediately from this function. The retry sends the existing event request and warning; it does not append the rejected response as a separate candidate artifact. The supplied runtime record retains the anti-copy predicate and its limit: a novel fabrication can satisfy those lexical checks. The protocol's labels such as "consolidated truths" therefore cannot establish factual verification. [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), [RT-BAP-extraction-policy](runtime.md#rt-bap-extraction-policy); [SRC-1: `internal/reasoner/openai.go`, `cmd/cli/mcp_prompts.tmpl`]

> if err := json.Unmarshal([]byte(raw), &jf); err != nil {
> valErr = fmt.Errorf("parse json: %w", err)
> msgs = append(msgs, openai.SystemMessage(retryWarning))
> continue
> }
> --- `internal/reasoner/openai.go`

Brain treats an empty summary as processed without adding a fact. For a nonempty summary it requests a vector, checks for a sufficiently similar existing fact, and either counts a duplicate or inserts a new fact with computed confidence and structured fields. No human content-veto step or independent answer oracle is wired into this witness. Fact-source associations are attempted after insertion; their errors are ignored. Inline contradiction detection is invoked after insertion, but its returned error is also discarded here. Thus a created-fact counter is not a certificate of complete provenance or successful contradiction checking. [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run); [SRC-1: `internal/brain/consolidate.go`]

### 5. Failure recovery can replay a partially committed batch

A concrete rejection path is two malformed structured responses: the adapter exhausts its attempts and returns the parse error; stage one records it and continues to other clusters. Its checkpoint advances only if its collected errors are empty. Facts inserted for other clusters remain persisted, so a later maintenance invocation can replay the batch and use deduplication to avoid some repeated facts. This is retryable partial progress, not atomic rollback or exactly-once processing. The supplied runtime record contains the checkpoint predicate and the no-rollback finding. [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run); [SRC-1: `internal/reasoner/openai.go`, `internal/brain/consolidate.go`]

The eight-stage orchestrator accumulates stage errors and proceeds to later stages while the context remains active. It attempts to save progress even after cancellation, using a background context then. It returns a result with counters and errors and ordinarily a nil top-level error. The MCP handler includes the embedded errors in its per-namespace summary; a top-level namespace failure gets a separate error entry. Consequently receiving a consolidation tool result does not mean every stage succeeded. The caller must inspect the result, and a later caller or ticker must actually trigger another run for replay to occur. [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run); [SRC-1: `cmd/cli/mcp.go`, `internal/brain/consolidate.go`]

The separate caller-recovery protocol asks the external agent to retry a failed tool call once, disclose memory unavailability, and avoid pretending to remember. This is instruction-level recovery, not server-enforced behavior; it also does not guarantee that an agent treats embedded consolidation errors as a failed tool call. [RT-BAP-agent-protocol](runtime.md#rt-bap-agent-protocol); [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`]

> - Retry the call once before giving up
> - Do NOT pretend to remember things you cannot verify from a successful tool call
> --- `cmd/cli/mcp_prompts.tmpl`

### 6. Later recall delivers selected text, not the whole derivation

A later agent supplies a query and namespace selection to MCP `recall`. Brain embeds the query, resolves namespace subtrees, selects facts first and episodes only for remaining slots, then sorts the selected results by score. It does not jointly rank all episodes and facts before filling the limit. The MCP response is serialized selected content with IDs, namespace IDs, scores, types and available metadata. The inspected result structure does not supply the fact-source association chain or rejected synthesis attempts. Delivery therefore does not give the downstream agent the entire admission history. [RT-RTE-recall-read](runtime.md#rt-rte-recall-read); [SRC-1: `internal/brain/recall.go`, `cmd/cli/mcp.go`]

For Stash, the delivered result is memory tool text returned to the requesting client. The external agent owns interpretation, any answer composition, and any user-facing delivery. No evidence here closes that last step or demonstrates that retained content changed the answer. Recall brings external retained material into a caller-selected invocation; Stash does not decide which old caller messages to evict. Optional working-focus handoffs are a separate route, [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff), and are not necessary to this durable-memory workflow. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`, `internal/brain/recall.go`]

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

#### On [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

Workflow verification boundary: an application-level structured-response retry is local to the reasoner adapter; a later replay of a batch is owned by a caller or maintenance driver invoking consolidation again. Embedded stage errors survive into the MCP summary even when the top-level method returns nil. Neither return alone establishes all-stage acceptance. The workflow account above retains the checked parse-retry passage; the supplied record retains the checkpoint passage. [SRC-1: `internal/reasoner/openai.go`, `internal/brain/consolidate.go`, `cmd/cli/mcp.go`]

#### On [RT-BAP-agent-protocol](runtime.md#rt-bap-agent-protocol)

Workflow recovery guidance: the server description directs the external agent to disclose memory failure and retry once, but it leaves execution and interpretation with that agent. In particular, no automatic bridge from embedded consolidation errors to this disclosure is established by the inspected handler. The workflow account retains the recovery instruction verbatim. [SRC-1: `cmd/cli/mcp_prompts.tmpl`, `cmd/cli/mcp.go`]
