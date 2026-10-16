---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "HippoRAG folder-indexing workflow: host preparation, confirmation, refresh, queued persistence and delivery of an indexing report."
run-id: AAS-2026-10-16-hipporag-2b37edfc7ade-01
reviewed-boundary: d5c8329422e0a0b834a15874545cb6a74b4f9b26
---

# HippoRAG workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is the shipped `index-folder` skill, from a folder request to a report of indexed and skipped passages. It is selected because it explicitly connects agent-side file preparation, a user checkpoint, destructive refresh, several MCP calls and a terminal report. These are connected steps in one shipped procedure, not a workflow inferred from unrelated API capabilities. The encompassing route is [WF-RTE-folder-indexing](#wf-rte-folder-indexing).

The evidence is SRC-1 doctrine/design for the two plugin skills and implementation for the server wrappers. Focused inspection covered both complete skills and `src/hipporag/mcp_server.py` through its tool registration and configuration resource. This revisits material included in the boundary and adds detailed inspection of result schemas, document conversion, delete resolution and count reporting. Library internals are supported by the supplied runtime records, not independently re-audited here. No target code, providers or examples were executed. In particular, the supplied source does not show an enclosing agent actually loading the skill, receiving approval, executing all steps or delivering a report.

### Request, preparation and user checkpoint

The host agent receives a folder and optional glob. The skill prescribes asking for a missing folder; otherwise its default glob covers Markdown, text and reStructuredText. It tells the agent to exclude hidden directories, dependency/build output, binaries and files over about 1 MB, and resolve absolute paths. The agent, not the MCP server, reads files and makes self-contained passages of roughly 100–400 words, carrying headings where needed. This is natural-language guidance interpreted by the host, not server-enforced file selection or chunking. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`; [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills).

The agent next calls `index_stats` and presents file/passage counts and model information before proceeding. Above approximately 50 passages the skill requires confirmation. User refusal or a request to change the plan can therefore stop the prescribed process before indexing, but the actual host interaction is unobserved. Neither the server's `index` wrapper nor its registration requires an approval token. The confirmation is a policy checkpoint, not a capability gate. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`, `src/hipporag/mcp_server.py`; [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools).

The cost guidance is not an exact implementation estimate: the skill says one extraction call per new passage, whereas [RT-RTE-index-state](runtime.md#rt-rte-index-state) establishes separate online NER and triple stages. Do not use the prescribed user message as evidence of actual call counts or cost. This discrepancy limits the accuracy of the planned estimate without preventing the workflow account.

### Refresh and the service handoff

For previously indexed files, the agent asks whether to refresh and, if requested, deletes by `source_id` before adding replacements. The general memory skill also requires confirmation before deleting content the user did not explicitly name. The server resolves source IDs against retained chunk metadata, gathers matching texts and delegates deletion to the library. It returns `passages_deleted`, unmatched requests and the remaining total. The server does not determine whether a file changed or ask the user; those decisions stay with the host. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`, `plugins/hipporag/skills/hipporag-memory/SKILL.md`, `src/hipporag/mcp_server.py`.

The agent then submits batches of about 20–30 objects. Each supplies passage text, an absolute file path as `source_id`, and chunk position/relative path metadata. All passages from one file share the source ID. Thus the handoff gives the service already prepared content and caller-asserted provenance, not authority to scan the folder or verify that the provenance matches a real file. `_to_chunk` copies these fields into a `Chunk`; indexing enters [RT-RTE-index-state](runtime.md#rt-rte-index-state). Extraction and embedding services receive their assigned content through that route; they are not delegated agents with authority to choose more files or commit arbitrary state. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`, `src/hipporag/mcp_server.py`.

The service serializes each operation on one worker. It owns library progression within a call, while the host owns whether to issue another batch, stop or report failure. The queue does not make the entire folder workflow exclusive: it is not a transaction spanning separate delete/index calls and does not coordinate independent processes. Read-only registration withholds the two mutating tools, so a read-only deployment cannot carry out this workflow through these wrappers. SRC-1: `src/hipporag/mcp_server.py`; [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools).

### Verification, rejection and recovery

Checks operate at different levels. Host preparation excludes unsuitable files and boilerplate according to the skill. Server input conversion rejects blank documents. Library compatibility and online extraction checks can reject construction, but do not establish content truth. These are structural checks, not an independent reviewer approving extracted facts. There is no supplied expected passage count or gold knowledge content against which this open folder-ingestion procedure verifies its result. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`, `src/hipporag/mcp_server.py`; [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility), [RT-RTE-index-state](runtime.md#rt-rte-index-state).

One concrete rejection path is a nonempty document list containing whitespace-only text. Conversion raises `ToolError` before that wrapper calls `rag.index`; the service propagates the tool error. Other library exceptions are logged and converted to tool errors, rather than silently counted as successful batches. This establishes error delivery, not automatic remediation. SRC-1: `src/hipporag/mcp_server.py`.

Recovery is divided between host/user and library. The memory skill tells the agent to ask the user to correct plugin settings and restart after an authentication or connection error, and to report a disconnected server rather than guess. The service can retry construction on a later call if warm-up failed because initialization remains lazy. Neither mechanism guarantees recovery from a partially written index. [RT-RTE-index-state](runtime.md#rt-rte-index-state) and [RT-CLM-state-compatibility](runtime.md#rt-clm-state-compatibility) establish that passage writes can precede extraction failure and that no whole-index rollback is demonstrated. Consequently, refreshing a file by successful deletion followed by failed re-indexing can leave its old content unavailable without installing the complete replacement. The skill supplies no transactional restoration step. SRC-1: `plugins/hipporag/skills/hipporag-memory/SKILL.md`, `src/hipporag/mcp_server.py`.

### Delivery and later consumption

A successful index wrapper returns documents received, the change in passage-store count and the total passage count. The terminal skill step tells the host to summarize files indexed, added passages, duplicates skipped and final total, and list skipped files with reasons. These tool results support count reconciliation, not semantic validation of extracted knowledge. Duplicate reporting requires host accounting: `IndexResult` has no separate duplicate or per-file success field. The host must combine its submitted batches and skip decisions with the returned counts rather than treating the tool response as a complete file-level audit. SRC-1: `src/hipporag/mcp_server.py`, `plugins/hipporag/skills/index-folder/SKILL.md`.

The intended delivery has two surfaces: retained searchable state and the host's user-facing summary. A server return completes one batch, not the folder workflow or proof of a delivered host message. Persisted passages can later feed retrieval and QA through [RT-RTE-retrieve-answer](runtime.md#rt-rte-retrieve-answer); that later use is not required by this skill and is not asserted to have occurred. There is no basis here for a successful-execution, answer-quality or reliability claim. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`, `src/hipporag/mcp_server.py`.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-folder-indexing
Label: Folder indexing workflow

This is the host-directed, multi-call procedure from a folder request through preparation, approval, optional refresh, batched indexing and a final report. Its identity differs from the instruction channel [RT-BAP-plugin-skills](runtime.md#rt-bap-plugin-skills), from the individual service operations in [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools), and from the library lifecycle in [RT-RTE-index-state](runtime.md#rt-rte-index-state). It spans these supplied records rather than being a material part of exactly one. It does not declare another copy of their components or state objects.

The enclosing host agent owns sequencing, file selection, passage preparation and reporting; the user can refuse prescribed confirmation or refresh. The service owns queued execution, and the library owns knowledge-state admission after submission. Operating mode is an open user ingestion request, not a benchmark or improvement experiment. New or changed files trigger additions/replacements. The agent proposes their content; software/model stages admit derived state subject to structural and compatibility rejection. There is no per-triple human vote or expected-answer oracle. The instructions shape document preparation and refresh; passages, provenance and derived index state persist, not a revised indexing method. A failed batch is returned as an error; already completed deletes/batches and partial library writes are not covered by a workflow rollback. SRC-1: `plugins/hipporag/skills/index-folder/SKILL.md`, `plugins/hipporag/skills/hipporag-memory/SKILL.md`, `src/hipporag/mcp_server.py`; library rejection and partial-write evidence: [RT-RTE-index-state](runtime.md#rt-rte-index-state).

- Immediate return: Each tool returns typed statistics or mutation counts; the host is instructed to deliver a final file/passage summary and skipped-file reasons.
- Later read-back: Indexed passages and derived structures persist for later retrieval, including across instance restarts as established by the runtime lifecycle. The workflow itself does not require a subsequent retrieval or retain its final summary as indexed knowledge.
- Delegated visibility: The host reads selected local files; the server receives prepared passage objects with source IDs and metadata, not the folder contents by reference. The host receives counts/errors, not extraction traces or a per-file audit from the index wrapper.
- Selection predicate: Skill-guided glob/exclusion rules and host passage splitting determine submissions; confirmation and refresh choices determine progression. Library content identity skips previously indexed passage content.
- Invalidation or expiry: Optional refresh deletes matching source contributions before replacement; no expiry timer is prescribed. Index/delete invalidate library retrieval preparation. There is no whole-folder atomic replace or undo established.
- Activation or effect: Tool wiring changes retained searchable state when calls succeed; source instructions prescribe host decisions and reporting. Actual host compliance, completed ingestion and later behavior change remain unobserved.
- Evidence limits: Skills supply doctrine/design and server code supplies implementation. No observed host session, execution trace or causal experiment establishes end-to-end success, cost, file completeness or knowledge correctness.
- guidance conclusion status: claimed
- implementation conclusion status: wired
- operation conclusion status: uninspected

The source explicitly joins refresh, provenance-bearing batches and final reporting:

> 4. **Refresh changed files.** Ask whether files already in the index should be refreshed. If so, `delete` them by `source_id` first, so edited files don't leave stale passages behind. Skip this step on a first-time index.
> --- `plugins/hipporag/skills/index-folder/SKILL.md`

> 5. **Index.** Call `index` in batches of about 20–30 passages. Each document is `{"text": <passage>, "source_id": <absolute file path>, "metadata": {"chunk": <index within file>, "path": <path relative to the folder>}}`. Every passage of a file uses the same `source_id`.
> --- `plugins/hipporag/skills/index-folder/SKILL.md`

> 6. **Report.** Summarize the files indexed, `passages_added`, passages skipped as duplicates, and the final `total_passages`. List any files you skipped and why.
> --- `plugins/hipporag/skills/index-folder/SKILL.md`

The skill prescribes a conditional user checkpoint; its cost statement is qualified in the account above:

> 3. **Confirm the cost.** Call `index_stats` to see the current size and model. Then tell the user how many files and passages you are about to index, and that each new passage costs one LLM extraction call with the configured model (passages already indexed are skipped). Wait for confirmation if there are more than ~50 passages.
> --- `plugins/hipporag/skills/index-folder/SKILL.md`

The wrapper returns store-count differences only after the library call returns:

> before = _num_passages(rag)
> rag.index(chunks)
> after = _num_passages(rag)
> return IndexResult(documents_received=len(chunks), passages_added=after - before, total_passages=after)
> --- `src/hipporag/mcp_server.py`

Blank object input is rejected before indexing:

> if not document.text.strip():
>     raise ToolError("Documents must not be empty.")
> return Chunk(content=document.text, source_id=document.source_id, metadata=dict(document.metadata))
> --- `src/hipporag/mcp_server.py`

Service failures become tool errors rather than successful result objects:

> except ToolError:
>     raise
> except Exception as exc:
>     logger.exception("HippoRAG operation failed")
>     raise ToolError(f"{type(exc).__name__}: {exc}") from exc
> --- `src/hipporag/mcp_server.py`

The prescribed configuration recovery belongs to the user and host:

> - If a tool reports an authentication or connection error, the plugin's API key or base URL option is probably unset or wrong. Ask the user to fix it in the plugin settings (`/plugin` → hipporag → configure) and restart the session.
> --- `plugins/hipporag/skills/hipporag-memory/SKILL.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-mcp-tools](runtime.md#rt-rte-mcp-tools)

Workflow role: one queued tool call is an execution handoff, not delegation of the remaining folder task. The host regains sequencing responsibility after each result or error. A final summary is outside the server return boundary; registration in read-only mode prevents the mutating portion of the selected workflow. The source evidence for these existing mechanisms remains in the supplied record; the folder-level consequences are established in [WF-RTE-folder-indexing](#wf-rte-folder-indexing).

#### On [RT-RTE-index-state](runtime.md#rt-rte-index-state)

Workflow recovery consequence: a host-guided refresh comprises deletion followed by later indexing, so rejection of a replacement does not imply retention of the old file. Library partial-write and compatibility checks must not be presented as a whole-folder rollback or as successful semantic verification. The prescribed procedure and server handoff are established in [WF-RTE-folder-indexing](#wf-rte-folder-indexing); the library mechanism and evidence remain in the supplied record.
