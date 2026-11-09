---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MindBase workflow account: hosted builder delegation, structural rejection, context replacement and completion reporting at c5273d2."
run-id: AAS-2026-11-08-mindbase-llm-wiki-32a62759e2b9-01
reviewed-boundary: c5273d2336c4d686df41c2a1495f14f085707f51
---

# MindBase workflow report

## Workflow account

### Selected workflow and evidence boundary

This account follows `/mb:build`: a foreground agent delegates a project-context rebuild to a restricted builder, which reads retained sources and writes a new context through MCP tools. It is representative of MindBase's hosted knowledge-maintenance workflow because it connects source selection, synthesis, persistence, index refresh and caller-visible completion in one prescribed sequence. It is not representative of every MindBase admission mechanism: the direct server build and the contribution checkbox plan have different owners and controls ([RT-RTE-build-context](runtime.md#rt-rte-build-context), [RT-RTE-contribute-plan](runtime.md#rt-rte-contribute-plan)).

The supplied [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build) already identifies this route; this report extends its workflow account without allocating a duplicate record. All evidence is SRC-1 at the boundary's frozen commit. The command and agent files supply doctrine/design evidence, while the MCP handlers supply implementation evidence. Neither establishes that a host dispatched the builder, that the prescribed sequence ran, or that synthesis preserved correct knowledge. No execution evidence or causal comparison is registered.

Additional implementation inspection beyond the supplied members covers `apps/mcp/src/tools/validate-structure.ts`, `apps/mcp/src/tools/load-project.ts`, `apps/mcp/src/tools/gather-sources.ts`, `apps/mcp/src/tools/rebuild-index.ts`, and `apps/mcp/src/tools/append-log.ts`. The command, builder definition and atomic-write handler were also read in full. These are included paths at the same revision, not new sources or a whole-system coverage claim.

### Request and delegation

The human supplies a build request. The foreground agent is instructed to resolve the target from an explicit project flag, positional argument, or current-project configuration, then dispatch a builder Task. The handoff names the project, not a complete copied corpus (SRC-1, `apps/plugin/commands/build.md`):

> **Dispatch the builder sub-agent** via the Task tool with `subagent_type: "builder"` and prompt:
> ```
> Rebuild context.md for project ${resolvedProjectId}.
> ```
> --- `apps/plugin/commands/build.md`

The command instructs the builder to thread that projectId through every MCP call. Loading the explicit project is read-only by default; it does not switch the persisted active project. In `apps/mcp/src/tools/load-project.ts`, successful loading returns the project root plus the entire README, context and index.yaml bodies, and writes configuration only when `persist` is true. Thus the builder obtains project instructions and retained knowledge after dispatch, rather than receiving them in the Task prompt.

The builder definition permits Read and the named MCP tools, not Edit, Write or Bash (SRC-1, `apps/plugin/agents/builder.md`). This is a host-enforced tool grant if honored, not an MCP-wide authorization boundary. The foreground agent and other clients are not thereby restricted. The separate child Task keeps detailed source-reading work out of the foreground workflow by prescription; only a one-line summary is requested back. Actual host context inheritance, disposal and isolation remain uninspected. No claim is made that source bodies cannot reach the foreground through host behavior.

### Validation and source selection

The first prescribed step is a rejection checkpoint (SRC-1, `apps/plugin/agents/builder.md`):

> 1. **Validate** via `mindbase_validate_structure({ projectId })`. Halt + return error if invalid.
> --- `apps/plugin/agents/builder.md`

The implementation checks whether README, context and index are files, and contributor, research and log roots are directories. It returns validity and missing-path diagnostics (SRC-1, `apps/mcp/src/tools/validate-structure.ts`):

> return textResult({ projectId, valid: missing.length === 0, missing });
> --- `apps/mcp/src/tools/validate-structure.ts`

This is a structural oracle, not a reference answer for synthesized knowledge. The model/host owns obeying the halt instruction: the subsequent write handler does not require a successful validation token. In particular, `valid: false` is returned as structured text rather than itself enforcing a prohibition on later tool calls. No semantic acceptance test for truth, completeness or contradiction handling is established by this check.

After loading project files, the builder gathers sources and is instructed to Read each listed file. Gathering recursively lists Markdown under the contributor and research roots. Unless an explicit `since` is supplied, context.md's modification time is the cutoff (SRC-1, `apps/mcp/src/tools/gather-sources.ts`):

> const cutoff = since ? new Date(since).getTime() : await lastBuildTime(root, p.context);
> --- `apps/mcp/src/tools/gather-sources.ts`

> const unbuilt = all.filter((f) => f.mtimeMs > cutoff).map((f) => ({
> --- `apps/mcp/src/tools/gather-sources.ts`

The return contains relative paths, sizes and mtimes, not file bodies or proof of successful incorporation. Read supplies the bodies in a separate step. “Unbuilt” therefore means newer than the cutoff, not individually tracked as unprocessed. Directory/stat failures can skip entries in this implementation. A context write advances the default selection boundary even though no per-source synthesis receipt is recorded here. These facts prevent treating a successful write or empty subsequent gather as evidence that every relevant source was incorporated.

### Synthesis and admission

The builder model proposes a complete replacement body, under the loaded README's build rules and the builder instruction. The instruction asks it to preserve prior context, add new information, and flag rather than settle contradictions (SRC-1, `apps/plugin/agents/builder.md`):

> **Merge, never replace** — keep prior context, add new info alongside. **Flag contradictions** as `> Warning: Conflicting information about X`. Never resolve them yourself; reviewer decides.
> --- `apps/plugin/agents/builder.md`

This is natural-language guidance. The write tool physically replaces the whole context; it does not check whether the new body retains prior claims, supports new ones, or includes the requested warning. “Reviewer decides” names intended later human judgment, but this eight-step workflow has no required reviewer approval call before persistence. Starting the build is not per-content approval. These limits agree with the baseline's qualification of [RT-CLM-approved-changes](runtime.md#rt-clm-approved-changes).

The atomic-write handler accepts nonempty content and a resolved project. Its software admission controls are input validation, project resolution and the line-cap transformation, not semantic comparison with an expected synthesis. The human can choose whether to initiate the command; the builder determines the proposed content; the tool admits it without a content-specific approval parameter. There is no inspected expected-answer oracle or quality-based candidate competition in this path.

### Persistence, failure and delivery

The replacement handler first attempts a snapshot, then spills overflow if needed, writes a temporary context and renames it, then appends its own build log. The baseline retains the rename evidence in [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build). Snapshotting is weaker than a guaranteed backup: the handler catches any failure in reading or writing the prior snapshot and proceeds (SRC-1, `apps/mcp/src/tools/atomic-write-context.ts`):

> } catch { /* no prior context; first build */ }
> --- `apps/mcp/src/tools/atomic-write-context.ts`

Above 400 input lines it retains the first 395 lines and replaces the tail with a pointer to a research overflow file. The returned `lines` is the input line count, not the resulting context's length. The tool returns projectId, snapshot path and optional overflow path. This establishes the available acknowledgment fields, not the existence of a successful historical run. The minute-resolution snapshot and temporary names do not provide an unqualified unique build history ([RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build)).

Atomic rename concerns context replacement only. Overflow writing happens earlier; log appending happens later; index rebuild and final logging are separate agent steps. A post-rename logging error can therefore occur after the context changed. No all-step transaction or automatic snapshot restore appears in this handler. Snapshot availability affords manual recovery, but the command's “rollback available” message is not evidence that rollback was executed or that snapshot creation succeeded in every case.

The builder is next instructed to rebuild index.yaml and append a final summary log. The index handler scans contributor/research Markdown, computes contributor counts and context mtime, and overwrites index.yaml. It does not verify the synthesized claims. The log handler appends the supplied operation/topic/details, rather than independently verifying the source count or contradiction count (SRC-1, `apps/mcp/src/tools/rebuild-index.ts`, `apps/mcp/src/tools/append-log.ts`).

> await writeFile(join(root, p.indexYaml), yaml, 'utf-8');
> --- `apps/mcp/src/tools/rebuild-index.ts`

> const { operation, topic, details } = parsed.data;
> --- `apps/mcp/src/tools/append-log.ts`

The final delivery criterion is prescribed rather than machine-certified: after these steps the builder returns its one-line source/line/contradiction/overflow summary; the foreground reports Build complete and a snapshot-path template. On an error it is instructed to surface the error verbatim and suggest validation or migration (SRC-1, `apps/plugin/commands/build.md`). No automatic retry, resume ledger or restore sequence is prescribed in that command. A structural rejection should halt before synthesis, but a failure after context replacement can leave changed context and incomplete index/log steps. The foreground completion text alone cannot certify that all steps or semantic checks occurred.

The persistent product is context.md, possibly an overflow research page, snapshot, regenerated index and logs. Later loading can supply context to another builder; session-start consumption is separately established by [RT-BAP-session-context](runtime.md#rt-bap-session-context). This closes the designed persistence-to-consumer path, not an observed improvement loop. Successful merge, reliable contradiction detection, future behavioral dependence and benefit remain unobserved.

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

#### On [RT-RTE-plugin-build](runtime.md#rt-rte-plugin-build)

Workflow-specific verification: structural validation returns a validity report; the builder must interpret it and halt. It is not a write-tool precondition token or semantic synthesis oracle. Index refresh and final log are subsequent child-agent obligations, not part of the atomic rename. Caller-visible completion depends on the child's summary rather than an independent end-to-end receipt.

Workflow-specific recovery: invalid structure is prescribed to stop the child and return an error for verbatim reporting. Partial post-write failure has no automatic restore sequence in the inspected command/handler chain. Snapshot creation is attempted but errors are swallowed; the snapshot-path acknowledgment is not proof of successful backup. The evidence and affected step boundaries are retained in the account above.
