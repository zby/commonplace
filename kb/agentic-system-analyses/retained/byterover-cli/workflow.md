---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "ByteRover CLI workflow: caller-authored curate, bounded correction, daemon delivery and later retrieval at the frozen repository boundary."
run-id: AAS-2026-10-15-byterover-cli-71610aaf716b-01
reviewed-boundary: "1052ac1a5dd0fde4da8693d4712064f7876c269c"
---

# ByteRover CLI workflow report

## Workflow account

### Selection and evidence boundary

This account selects the public CLI curate workflow: a caller requests retention of knowledge, receives authoring instructions, supplies HTML, corrects rejected submissions and receives a stored-topic result. It then distinguishes that delivery from later query consumption. This is representative because the shipped coding-agent workflow expressly requires completing curate before dependent work, and the CLI implements the handoffs rather than merely advertising them. It is not an account of the separate internal model curator.

The evidence is SRC-1 implementation and doctrine/design at the revision in [the boundary](boundary.md), not an executed transcript. Direct inspection covers `src/oclif/lib/curate-session.ts` kickoff, continuation and task dispatch, `src/oclif/commands/curate/index.ts` command routing, continuation checks, output and response-file cleanup, and `src/server/templates/sections/workflow.md`. These are additional scoped implementation/design inspections within the registered source, not new sources. The daemon writer and later retrieval findings use the supplied runtime records and their retained passages. No source-supported claim here establishes successful external-agent authorship, downstream compliance or benefit.

### Request and authoring handoff

The invoking user or coding agent supplies knowledge intent to `brv curate`. The CLI kickoff saves intent, attempt count and step under a UUID session, then returns a schema-derived prompt and `needs-llm-step` envelope. This is a request to perform the next step, not a stored-knowledge result. The caller owns HTML generation; ByteRover's own provider is not invoked by this CLI path. The external caller's model, reasoning and authority to approve content are outside the frozen implementation boundary. See [RT-RTE-curate-session](runtime.md#rt-rte-curate-session) and SRC-1, `src/oclif/lib/curate-session.ts`, `src/oclif/commands/curate/index.ts`.

The handoff supplies user intent and authoring/output guidance. The UUID allows a later CLI invocation to reload protocol state; it is not a sub-agent identity or evidence of human approval. The caller returns a JSON `{html, meta?}` envelope with that session ID, inline or through a response file. These are process-separated protocol steps, not evidence that ByteRover launches a worker or transfers the caller's full conversation. The implementation leaves the intervening generation to the caller; the source does not establish that the caller follows the prompt.

### Continuation, verification and correction

The continuation first checks flag combinations, nonempty input, envelope shape and local session existence. Local failure returns a structured error without daemon dispatch. Empty or malformed input leaves the session available; a `failed` envelope therefore does not always mean the workflow state has been destroyed. The authoritative continuation reparses and reloads state before dispatch. See [RT-RTE-curate-session](runtime.md#rt-rte-curate-session); SRC-1, `src/oclif/commands/curate/index.ts`, `src/oclif/lib/curate-session.ts`.

For accepted envelope shape, the CLI creates a separate task UUID, sends explicit project path, HTML, optional metadata, overwrite choice and original intent to the daemon, then waits for a correlated completion. The daemon owns topic admission and physical writes, not content generation on this branch. Its checks can reject invalid HTML structure, unsafe path segments or an existing target without overwrite consent. These checks establish a structural acceptance criterion, not a factual answer oracle. No per-content human judgment is necessary on this route; a generic CLI caller does not resolve human authorship or approval. See [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission), including its writer passage; SRC-1, `src/oclif/lib/curate-session.ts`, `src/server/infra/render/writer/html-writer.ts`.

After a writer rejection, the CLI increments the attempt count, saves the previous response and returns a correction prompt, errors and the same session ID. Conflict feedback can include readable existing content for a caller-directed merge. The caller, not the validator, chooses a semantic revision or supplies overwrite consent. Four unsuccessful writer responses terminate the session; malformed envelopes do not consume that writer-response budget. A successful writer response instead clears session state and returns `done` with the file path. The retry cap belongs to this CLI protocol, not every route into the writer. See [RT-RTE-curate-session](runtime.md#rt-rte-curate-session); SRC-1, `src/oclif/lib/curate-session.ts`.

### Transport failure and artifact recovery

The command wraps continuation dispatch in daemon retry and maps an eventual thrown error to `daemon-error`. When the caller used a response file, a throwing dispatch leaves that file intact. This preserves the authored proposal for recovery but does not establish transactional rollback or prove that no daemon write occurred before a transport failure. SRC-1 implementation, `src/oclif/commands/curate/index.ts`:

> } catch (error) {
>       this.emitToolModeEnvelope(
>         {
>           errors: [{kind: 'daemon-error', message: formatConnectionError(error)}],
>           ok: false,
>           status: 'failed',
>         },
>         format,
>       )
>       return
>     }
> --- `src/oclif/commands/curate/index.ts`

Optional `--delete-response-file` cleanup runs after a nonthrowing dispatch, including a returned correction or failure result; retaining the original file is not guaranteed after a structured rejection. Cleanup failure appends an error without replacing the dispatched result's success/status. Thus `done` can coexist with a cleanup error, and that companion error alone is not grounds to repeat the knowledge write. SRC-1 implementation, `src/oclif/commands/curate/index.ts`:

> ...dispatchEnvelope,
>               errors: [
>                 ...(dispatchEnvelope.errors ?? []),
>                 {kind: error.kind, message: error.message},
>               ],
> --- `src/oclif/commands/curate/index.ts`

These are response-artifact recovery semantics, separate from restoring overwritten knowledge. For topic recovery, the supplied [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission) establishes conditional post-write review and best-effort backups. A review rejection can restore a backup or remove an addition, but missing backup content can make rejection delete rather than restore. Pending review is not pre-write approval and does not prevent local retrieval.

### Delivery and later use

For this protocol, delivered means the daemon reports a successful topic write and the CLI emits the completion envelope with its file path. The durable output is the context-tree topic, not the discarded session. Review logs, sidecar updates and deferred index regeneration are separate effects; the completion is not an atomic guarantee covering all of them. See [RT-OBJ-context-tree](runtime.md#rt-obj-context-tree) and [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission).

The shipped workflow makes that completion a dependency barrier before subsequent work. This is instruction-level coordination, not enforcement over the external caller. SRC-1 doctrine/design, `src/server/templates/sections/workflow.md`:

> Any follow-up step (query, search, read, or a later curate that builds on this one) needs the just-curated topic live in the context tree — finish the continuation before moving on.
> --- `src/server/templates/sections/workflow.md`

A later query starts a separate retrieval task. Code selects local results, excludes shared-origin or unreadable files, renders topic HTML into markdown-like content and applies the requested limit; it may return cached content. The caller owns synthesis and subsequent action. Consequently, persistence does not guarantee immediate selection, byte-complete delivery, freshness or reliance. [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval) establishes this implemented read-back edge, and [RT-BAP-topic-guidance](runtime.md#rt-bap-topic-guidance) bounds its behavioral authority. The traced workflow supports a concrete retain-and-retrieve protocol with structural correction, not a demonstrated coding-task outcome or an end-to-end reliability claim.

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

#### On [RT-RTE-curate-session](runtime.md#rt-rte-curate-session)

Workflow-specific delivery distinction: kickoff delegates generation; only successful continuation reports the stored topic. The authoring caller owns correction decisions, the CLI owns bounded protocol retry and the daemon owns admission/write. The command's response-file recovery preserves the proposal on a throwing dispatch, but optional cleanup also follows structured writer rejection. A cleanup error can accompany successful delivery without reversing it. The Workflow account retains the added command implementation evidence and quotations.

#### On [RT-RTE-topic-admission](runtime.md#rt-rte-topic-admission)

Workflow-specific acceptance boundary: a structurally accepted topic is the continuation's deliverable. Optional review is a later rejection/recovery mechanism, not a required authorization handoff before the local write. Deferred indexing and best-effort companion effects prevent treating this completion as a transaction over every derivative artifact.

#### On [RT-RTE-query-retrieval](runtime.md#rt-rte-query-retrieval)

Workflow-specific dependency: shipped instructions tell the caller to finish curate before dependent query or other follow-up work. The query is a fresh task rather than session continuation. Its selected/rendered return crosses back to the external caller; the target implementation does not establish synthesis or successful downstream action.
