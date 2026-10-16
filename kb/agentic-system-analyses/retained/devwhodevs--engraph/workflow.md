---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Engraph workflow account: an agent-requested meeting note through MCP creation, filing, indexing, delivery and failure recovery."
run-id: AAS-2026-10-14-engraph-0cd4f00695b0-01
reviewed-boundary: f9a95bc96accc792c02ee384d9e6bf768a88c8c8
---

# Engraph workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped example **“Create a meeting note for today's standup”**: an external Claude Code client supplies a note to MCP `create`; Engraph transforms, files and indexes it, then returns identifying metadata. This is selected because one wired call traverses the production-to-retention path, including consequential software decisions and a rejection/recovery branch. It is not an invented search→draft→review chain. The example declares the external handoff, not an observed agent execution (SRC-1, `examples/claude-code-setup.md`):

> Claude will call `create` with content, tags, and type hint. engraph resolves tags against your registry, discovers wikilinks in the content, and places the note in the best folder.
> --- `examples/claude-code-setup.md`

The request-to-agent step is declared design; the MCP handler and writer progression are inspected implementation. No conversation, user vault, model weights, executed tests or failure trace was supplied. Thus this account establishes coordination and delivery machinery, not actual agent compliance, correct meeting content, appropriate filing or successful recovery. The frozen boundary is [boundary](boundary.md#boundary-and-evidence); the existing referents are [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), [RT-CLM-write-consistency](runtime.md#rt-clm-write-consistency) and [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh).

This inspection adds focused implementation coverage of `create_note`, its chunk preparation, temporary-file cleanup and orphan removal in `src/writer.rs`; the create/read handlers and result/error conversion in `src/serve.rs`; `place_note` strategy progression in `src/placement.rs`; and disk consumption in `context_read` in `src/context.rs`. The complete setup example was read as doctrine/design. All are SRC-1 at the frozen commit. These reads extend selected coverage, not the evidence boundary.

### Handoffs and decision ownership

1. **Client setup and request.** The setup example supplies an index command and an MCP server configuration launching `engraph serve`. At startup the service opens Store, loads configuration and the embedder, and requires the stored vault path. The example expects Claude Code to turn the user's meeting-note request into content, tags and a type hint; it does not specify how Claude obtains meeting facts, verifies them or decides that drafting is complete. Those responsibilities remain external (SRC-1, `examples/claude-code-setup.md`, `src/serve.rs`).
2. **MCP admission.** The `create` handler first checks read-only, then locks Store and embedder. It forwards content, optional filename/type/folder/auto-link settings and tags, defaulting absent tags to an empty list. It supplies `created_by: "claude-code"` itself and passes the already loaded vault profile. That label is not authenticated authorship. Code, not a model or delegated worker, owns all subsequent steps (SRC-1, `src/serve.rs`; [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)).
3. **Text and target preparation.** The writer derives or accepts a title, generates an `.md` filename, resolves supplied tags and discovers links. Exact-name and alias matches are auto-applied; fuzzy matches require confidence of at least 920 basis points; first-name matches remain suggestions. Disabling auto-link sends all discovered links to suggestions. Applied links alter the body before placement. The caller's explicit folder bypasses automatic placement; otherwise code tries type rules, semantic centroid placement and inbox fallback in order. An uncertain semantic destination can survive as suggested-folder metadata rather than the actual destination. User frontmatter is merged with generated metadata before writing (SRC-1, `src/writer.rs`, `src/placement.rs`). These are software transformations, not per-content human approvals. The natural-language meeting body, symbolic metadata/rules and numerical embeddings have different consumers; numerical similarity is not an answer oracle.

The placement dispatcher makes the fallback an operational branch rather than a promise to always find the best folder:

> // Strategy A: Type-based rules
> if let Some(result) = try_type_rules(content, hints, profile) {
>     return Ok(result);
> }
> --- `src/placement.rs`

> reason: "No confident placement".to_string(),
> suggestion: semantic_suggestion,
> --- `src/placement.rs`

4. **Persistence and indexing.** The writer checks whether the final path already exists, then chunks and embeds the assembled content before opening its database transaction. It writes a temporary file, begins the transaction and inserts the file record, chunks, vectors, full-text entries, graph edges and registered tags. Commit precedes renaming the temporary file to its final path. It then updates stored mtime and attempts an incremental folder-centroid update. The centroid update's error is ignored; completion does not certify that every derived update succeeded (SRC-1, `src/writer.rs`). The ordering and its consistency limit are retained in [RT-CLM-write-consistency](runtime.md#rt-clm-write-consistency). The in-process locks do not make external editors or other CLI processes part of this transaction.
5. **Delivery.** The writer returns path, docid, resolved tags, added/suggested links, folder, confidence and strategy. MCP serializes that result as a successful text tool response. The response supplies identifiers and transformation summaries, not the final note body, a semantic review verdict or proof of later retrieval. Completion here means successful writer return and response serialization; the external agent still owns any conversational acknowledgement to the user (SRC-1, `src/writer.rs`, `src/serve.rs`).

> Ok(CallToolResult::success(vec![Content::text(json)]))
> --- `src/serve.rs`

### Verification, rejection and recovery

The implemented checks are operational admission checks. Read-only rejects the MCP request before writer dispatch; an existing destination found by the writer rejects create before chunk embedding and temporary-file creation. Neither check assesses whether the meeting record is true. The caller can abstain, supply an explicit folder or disable auto-linking, but initiating creation is not evidence that a human inspected the transformed note. The example supplies no mandatory critique/approval handoff (SRC-1, `examples/claude-code-setup.md`, `src/serve.rs`, `src/writer.rs`; [RT-CLM-server-readonly](runtime.md#rt-clm-server-readonly)).

For errors inside the database insertion closure, the writer attempts rollback and temporary-file removal, then returns the original error. Those cleanup errors are ignored, so this is attempted recovery rather than an invariant:

> Err(e) => {
>     let _ = store.rollback();
>     let _ = std::fs::remove_file(&temp_path);
>     return Err(e);
> }
> --- `src/writer.rs:698-702`

Commit and rename use error propagation in the successful-closure branch, not that cleanup branch. A post-commit rename failure can therefore yield an error despite admitted database state and a remaining temporary file. Even after rename, an mtime-record update or response serialization error can prevent successful delivery after persistent effects. There is no inspected internal retry of the user's create request; errors are mapped to MCP errors and the client must decide what to do next (SRC-1, `src/writer.rs`, `src/serve.rs`). Retrying blindly is not established as safe: if the final file now exists, the ordinary collision check rejects it.

Server restart provides a different recovery owner: startup code removes incomplete temporary files, removes database entries whose final files are missing, and starts the watcher's reconciliation route. Orphan removal deletes vectors, full-text entries, edges and file records. This repairs retained search state rather than completing or replaying the requested meeting note. In particular, cleanup can discard the temporary copy after a failed rename; it does not preserve every intended write (SRC-1, `src/serve.rs`, `src/writer.rs`; [RT-RTE-index-refresh](runtime.md#rt-rte-index-refresh)).

> std::fs::remove_file(path)?;
> cleaned += 1;
> --- `src/writer.rs`

### Later consumption, not a required completion gate

Create immediately populates derived retrieval entries; later search can select the retained note through [RT-RTE-query-search](runtime.md#rt-rte-query-search). Independently, MCP `read` forwards a caller-supplied file identifier to `context_read`, which resolves the indexed record and reads the current disk file, adding indexed graph metadata. That is a supported reload route, not an automatic post-create inspection. The create handler does not call it. A missing/unreadable disk file can return empty content and an explanatory body rather than validating the original write (SRC-1, `src/serve.rs`, `src/context.rs`):

> let msg = "[File not found on disk. Re-run 'engraph index' to update.]".to_string();
> (String::new(), msg, String::new())
> --- `src/context.rs`

The workflow has a concrete retained result and later consumers, but no supplied evidence that an agent read it, accepted its suggestions or benefited from it. Engraph's internal model involvement here is embedding/semantic placement, not model-native tool execution, worker delegation or autonomous meeting-note authorship. External context-window management and agent scheduling remain outside this trace.

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

#### On [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

Workflow selection: the shipped standup-note example uses the create branch. External Claude Code supplies the proposed note; MCP forwards selected inputs and adapter authorship metadata; writer code owns transformation, persistence and return. Operational checks can reject the request, but there is no inspected semantic acceptance gate in this branch. Delivery is the serialized WriteResult, not a user-facing answer or a mandatory read-back. Other note mutation variants are not steps in this selected workflow.

#### On [RT-CLM-write-consistency](runtime.md#rt-clm-write-consistency)

Workflow recovery boundary: rollback/temp deletion covers insertion-closure failure, not every propagated error after temporary-file creation. Startup repair removes incomplete state rather than replaying the request. A failed response therefore cannot be treated as proof that nothing persisted, and a successful create response cannot be treated as a cross-resource crash-safety guarantee.
