---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Smriti MCP workflow account: caller-led trace review, consolidated memory admission and subsequent retrieval."
run-id: AAS-2026-10-14-smriti-mcp-14f6928f9817-01
reviewed-boundary: "8264bf9103477d9521e57b27c81dcc2e943a3230"
---

# Smriti MCP workflow report

## Workflow account

The representative workflow is **record observations → request consolidation suggestions → supply a durable memory → retrieve it later**. It was selected because the shipped tool descriptions explicitly connect trace review to consolidated writes, and the store implements both that chain and later consumption. It is a supported caller-led workflow, not a supplied execution trace or an internal autonomous agent loop. The external caller determines when to advance and what the final memory says; Smriti executes individual requests and returns control after each. The host's model prompting and completed task delivery are outside the [boundary](boundary.md).

The account reuses [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation), [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) and [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), rather than declaring duplicate routes. Additional inspection concerns implementation and shipped guidance in SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`, and test intent in `tests/test_smriti_store.py`, all at the frozen revision. No additional source or observed-run evidence is introduced. The tests were read, not executed.

### 1. The caller records an observation

A host agent, human or application supplies content, optional agent identity, scope, memory ID, salience and metadata to `record_trace`. The server delegates the operation to its captured store, not to another agent. The store supplies timestamp and a hash-derived event ID, appends a JSON event to a dated agent-named NDJSON file, and returns ID, relative path and the event. This is raw persistence, not verification of the observation. Agent labels are caller-supplied, not authenticated worker identities. The caller owns any next request (SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`; [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)).

### 2. The caller requests review material

`suggest_consolidation` reloads persisted events with optional scope, time and agent filters. Its loader skips blank lines and JSON decoding failures; the agent filter checks the filename stem. This does not establish complete ingestion of every trace file or validation of every event schema (SRC-1, `src/smriti_mcp/store.py`).

> try:
>     event = json.loads(line)
> except json.JSONDecodeError:
>     continue
> --- `src/smriti_mcp/store.py`

The store groups events by their first three normalized content terms. It searches for related memories using up to eight normalized terms from the group's combined content and returns metadata rather than full bodies. A related-memory hit produces `update_existing`; otherwise repeated events or an event with salience at least 0.7 produce `create_memory`; other groups retain `review`. Groups are ordered by event count and maximum salience, then limited. The returned handoff therefore contains selected raw events, a heuristic recommendation and related-memory metadata, not a synthesized or verified memory. The caller must request full existing content separately if needed for its judgment (SRC-1, `src/smriti_mcp/store.py`; [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)).

> if group["related_memories"]:
>     group["recommendation"] = "update_existing"
> elif len(group["traces"]) > 1 or any((t.get("salience") or 0) >= 0.7 for t in group["traces"]):
>     group["recommendation"] = "create_memory"
> --- `src/smriti_mcp/store.py`

These are candidate-selection rules, not an answer oracle. They neither verify factual support nor compel an update. The tool's explicit division of labor is retained in [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation): Smriti does not summarize the events; the agent decides final memory content.

### 3. The caller decides and submits consolidated prose

The caller can decline all recommendations, gather more information, or invoke `consolidate_memory` with final Markdown, metadata, optional target ID, selected trace IDs and a mode. There is no inspected continuation that automatically invokes consolidation after suggestions. This is semantic work reserved for the external caller, not agent delegation owned by Smriti. Generic caller identity leaves human versus model judgment unresolved (SRC-1, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`).

> "Create, append, or update a durable memory from agent-supplied consolidated content. "
> "Use after reviewing traces; Smriti records provenance but does not summarize content itself."
> --- `src/smriti_mcp/server.py`

The server serializes the metadata input and calls the store. The store prepares `sources` strings from supplied trace IDs. Create/update apply the prepared metadata; append forwards only ID and content, so newly prepared provenance and other metadata are not applied to the existing note. The evidence for that distinction is retained in [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation). Trace IDs do not require a preceding suggestion call and are not checked against loaded events here. Thus recording provenance strings does not establish that the new prose faithfully summarizes them (SRC-1, `src/smriti_mcp/store.py`).

### 4. Code admits a file change, not a semantic verdict

Selected ordinary write methods check metadata/path/target conditions and persist the note. Create returns ID/path; append or update returns ID/status. After the note operation, consolidation appends a new `consolidated` event containing the note ID, supplied trace IDs and mode, then returns the note operation's result. Its success response is not the final memory body or a support report (SRC-1, `src/smriti_mcp/store.py`; [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)).

> self.record_trace(
>     content=f"Consolidated traces into {result['id']}.",
>     type="consolidated",
>     agent=clean_meta.get("source_agent"),
>     memory_id=result["id"],
>     metadata={"trace_ids": trace_ids or [], "mode": mode},
> )
> return result
> --- `src/smriti_mcp/store.py`

**Rejection and recovery.** Append/update without an ID reject before the note operation; append's exact guard is retained in [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation). Creating at an existing target rejects rather than overwriting it:

> with self._lock:
>     if path.exists():
>         raise FileExistsError(memory_id)
> --- `src/smriti_mcp/store.py`

These checks reject malformed or conflicting operations, not unsupported knowledge. The caller must select a different target or deliberately use append/update and resubmit. No recovery agent or automatic retry is implemented in this chain. A later trace-write exception can occur after a note has already been saved; the code has no encompassing rollback. Blindly retrying create can then encounter the existing-target rejection, while repeating append can add the text again. Those are source-level failure consequences, not observed incidents. Recovery requires the caller to inspect retained state, for example with `get_memory`, before choosing another mutation. Per-note atomic replacement does not make note-plus-trace transactional ([RT-CLM-file-controls](runtime.md#rt-clm-file-controls); SRC-1, `src/smriti_mcp/store.py`).

### 5. A later caller requests the retained result

`get_memory` reloads full Markdown by ID. Alternatively, a later `recall_context` request rescans current files, applies filters and lexical/affinity ranking, optionally expands one-hop links, and returns selected formatted context. The consolidation result has no automatic recall continuation. Recall's returned representation contains title/ID, optional short description and lifecycle/confidence/source fields, plus at most two selected snippets per note; it is not complete delivery of the consolidated body (SRC-1, `src/smriti_mcp/store.py`).

> for snippet in snippets[:2]:
>     lines.append(f"  {snippet}")
> return "\n".join(lines)
> --- `src/smriti_mcp/store.py`

[RT-RTE-context-recall](runtime.md#rt-rte-context-recall) retains the ranking, approximate budget, archived/superseded defaults and optional access reinforcement. Recall returns context and selected metadata to the caller, not to an owned model invocation. Access reinforcement may update the note before return; these writes, too, are not an enclosing workflow transaction. A successful file write and a returned recall bundle establish separate implementation-level delivery boundaries. Neither establishes host prompt inclusion, model reliance, an improved answer or completed external work (SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`).

### What the evidence establishes

The source supports a multi-request memory workflow with explicit handoffs, deterministic candidate suggestions, caller-authored content, structural write rejection and later file-backed retrieval. The shipped `test_record_trace_and_suggest_consolidation` inspects trace storage/grouping intent; `test_consolidate_and_supersede_memory` constructs an observation, supplies replacement prose and checks supersession through read-back. Neither supplies a model's semantic review or a successful end-to-end trace-consolidation-recall run. Their assertions are test intent, not observed operation (SRC-1, `tests/test_smriti_store.py`).

The deliverable inside Smriti is a saved memory and returned operation result, followed only on request by full Markdown or compact recall context. Semantic verification, autonomous scheduling, cross-agent coordination and acceptance of an enclosing task result cannot be inferred from this chain. No claim of successful execution or improved future task performance follows from the inspected implementation.

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

#### On [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

Workflow role: review-to-write handoff. The external caller advances between independently invoked tools and supplies the semantic decision; the recommendation is advisory. Structural rejection terminates the current operation, leaving recovery to the caller. A returned success follows both the note operation and the attempted consolidation-event append; an exception is not proof that the earlier note effect was undone. Later recall is another caller-selected invocation, not an automatic successor.

#### On [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Workflow role: requested later delivery. A compact recall result may omit most consolidated prose; ID-based full retrieval remains available. Delivery ends at the tool/library caller. No inspected host continuation establishes acceptance or use in a completed agent task.
