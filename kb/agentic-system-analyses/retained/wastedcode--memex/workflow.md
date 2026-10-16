---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Memex workflow account tracing source upload, delegated wiki integration, result delivery and conditional maintenance at the frozen commit."
run-id: AAS-2026-10-14-memex-42ecde52cc05-01
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
---

# Memex workflow report

## Workflow account

### Selection and evidence boundary

The selected workflow is an ordinary blocking `memex ingest <wiki> <files...>` into an existing wiki, followed by the maintenance job that the queue can schedule after its ingest counter reaches the threshold. This is representative because it connects source admission, persistent wiki production, model-dependent decisions and a shipped maintenance handoff. Maintenance is a conditional continuation, not a prerequisite for delivering the ingest result. This is not a fabricated ingest–query pipeline: later questions are separate requests.

The account uses SRC-1 at the [frozen boundary](boundary.md), with implementation evidence from `src/cli/commands/ingest.ts`, `src/cli/client.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts` and `src/daemon/namespace.ts`, and doctrine/design evidence from `src/lib/prompts/ingest.ts` and `src/lib/prompts/lint.ts`. These paths were inspected for the consequential handoffs below within the registered commit; no additional source identity is introduced. No target code was executed. There is no supplied run, completed wiki or before/after comparison, so successful integration, actual verification and recovery remain unobserved.

### Request to delegated work

1. **The caller supplies a wiki and local files.** The CLI checks that every path exists before beginning uploads. It then uploads files sequentially. `MemexClient.uploadFile` reads bytes and sends basename plus base64 content; the daemon checks wiki ownership and the presence/type of upload fields. The scaffold writes the bytes under the wiki's `wiki/raw/` directory and returns a timestamp-prefixed stored name. The handoff carries stored filenames, not the caller's original filesystem paths. The caller can be a human or automation; source selection is not per-edit approval. See [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) (SRC-1, `src/cli/commands/ingest.ts`, `src/cli/client.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`).

2. **The daemon accepts a job, not a verified integration.** Only after uploads succeed does the CLI submit `{ files: storedFiles }`. The route checks ownership and job type, persists the payload and notifies the queue. It does not establish that these names identify readable source files or validate a typed ingest payload. A direct API caller can skip the CLI's upload sequence. The queue claims pending jobs in ascending ID order and awaits each runner for that wiki; this coordinates queued jobs, not raw uploads or external filesystem writers. The durable handoff is [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs), not a retained model conversation (SRC-1, `src/daemon/routes.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`).

3. **The runner delegates content decisions to a fresh Claude Code process.** It rebuilds the task from the stored payload, resolves current credentials/model/tools, appends wiki policy and wraps the invocation in a per-job mount namespace. It supplies the task via `-p`, not stdin, and passes tool grants as both available and pre-approved tools. The wiki filesystem is reachable for model-directed reads, but its contents are not automatically inlined into the prompt. No conversation-resume identifier carries an earlier model frame forward. The external process owns source interpretation, related-page selection and edits; the daemon owns scheduling and result recording. External tool enforcement is not established by inspecting the arguments (SRC-1, `src/daemon/runner.ts`; [RT-BAP-wiki-instructions](runtime.md#rt-bap-wiki-instructions), [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model)).

4. **The task describes a multi-step editorial procedure, not a series of daemon checkpoints.** Claude is instructed to read the sources, schema and index, search related pages, extract information, update/create pages, repair bidirectional links, update the index and log, then reconsider schema conventions. This is one delegated job whose internal step completion is not reported to a controlling coordinator. The prompt requests a final JSON summary and operations with reasons only after file operations. The supplied runtime record retains the relevant editorial and schema passages; no new record duplicates that route (SRC-1, `src/lib/prompts/ingest.ts`; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job), [RT-OBJ-wiki-prompts](runtime.md#rt-obj-wiki-prompts)).

The path inconsistency identified in the runtime applies at this handoff: the wrapper changes directory to `/workspace`, while scaffolded schema/index/raw content is under `/workspace/wiki/`. The prompt says `raw/`, `_schema.md` and `_index.md`. Literal relative-path use therefore does not reach the scaffolded files. A model might discover the layout, but no evidence demonstrates that compensation. This prevents claiming that the described editorial procedure successfully operates on the intended files (SRC-1, `src/daemon/namespace.ts`, `src/daemon/scaffold.ts`, `src/lib/prompts/ingest.ts`; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)).

### Verification and delivery

There are three distinct acceptance boundaries. Request admission checks identity and outer request validity. The model is asked to resolve or flag source contradictions and maintain structural consistency. Terminal job admission checks process exit status. None is an independent semantic oracle for the completed wiki. No expected answer or curated reference outcome is supplied; this is open source integration rather than a bounded experiment (SRC-1, `src/daemon/routes.ts`, `src/lib/prompts/ingest.ts`, `src/daemon/runner.ts`; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)).

The runner attempts to parse Claude's output envelope, then the enclosed result text, but parsing failure falls back to text instead of rejecting the job. The runtime's retained `success: code === 0` passage establishes that exit status, not output format or verified edits, determines success. Queue completion stores the returned result object and an audit entry. The blocking CLI polls for `completed` or `failed`, prints “Ingest complete.” on completion and prints the stored `output` when present. Thus result delivery means a persisted terminal row consumed by the client; it does not mean all promised file operations were checked. `--async` delivers a job ID instead of waiting for this terminal result (SRC-1, `src/daemon/runner.ts`, `src/daemon/queue.ts`, `src/daemon/db.ts`, `src/cli/client.ts`, `src/cli/commands/ingest.ts`; [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)).

### Conditional maintenance handoff

Successful ingest increments an in-memory per-wiki counter. At the default ten-ingest threshold the queue resets that counter and creates a lint job unless one is already pending. It does so after recording ingest completion, so the CLI can finish without waiting for lint. The lint job receives an empty payload, not the prior ingest's operations or a critic's findings; its prompt supplies the current date and requests inspection of wiki files. It uses the same runner in a new process. The retained files, rather than a model-to-model conversation, connect the two jobs (SRC-1, `src/daemon/queue.ts`, `src/lib/prompts/lint.ts`; [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)).

> this.db.createJob(wikiId, 'lint', {});
> --- `src/daemon/queue.ts`

Lint asks Claude to check contradictions, stale claims, orphans, missing/duplicate pages, cross-references, index accuracy and schema drift. It requests direct confident structural fixes but report-only handling for contradictions, merges and stale facts. The runtime retains the exact human-judgment instruction. This is model self-review against the wiki and schema, not independent verification against an answer oracle. The tool grant does not enforce the report-only partition. The markdown report becomes that lint job's result; the automatic branch does not synchronously return it to the original ingest caller or implement a review-approval callback. Pending-lint suppression avoids stacking pending maintenance requests, not repeated semantic defects. Restart resets the counter because it is not durable (SRC-1, `src/daemon/queue.ts`, `src/daemon/runner.ts`, `src/lib/prompts/lint.ts`; [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)).

### Rejection, failure and recovery

An upload failure ends the CLI invocation before job submission. Earlier successful uploads have already written raw files; the CLI has no compensating deletion in this path. Similarly, unauthorized requests are rejected by the daemon before their protected operation, but this is not rollback of earlier accepted uploads (SRC-1, `src/cli/commands/ingest.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`).

> if (!resp.ok) {
>         console.error(` failed: ${resp.error}`);
>         process.exit(1);
>       }
> --- `src/cli/commands/ingest.ts`

If a delegated job returns failure, the queue records `failed` and an audit entry. A thrown runner error is also caught and recorded as failed. The drain loop can continue to later jobs; there is no automatic semantic repair attempt for that failed row. The CLI reports failure and exits. Neither branch restores wiki files already changed by Claude, and lint is not scheduled from a failed ingest. These findings follow the inspected queue/CLI branches, not a supplied failure trace (SRC-1, `src/daemon/queue.ts`, `src/cli/commands/ingest.ts`, `src/daemon/db.ts`).

> } catch (err) {
>           const msg = err instanceof Error ? err.message : String(err);
>           this.db.failJob(job.id, msg);
> --- `src/daemon/queue.ts`

Restart recovery is different: stale `running` rows become `pending` with an increased retry count and can be replayed from the retained payload. Existing file effects are not reverted and the previous model frame is not restored. Consequently, replay is not exactly-once editing. Timeout and shutdown attempt to signal tracked children, but successful termination and descendant cleanup are unobserved; the runtime records the `child.killed` escalation limitation. The recovery owner is daemon code, not a critic or human approval stage (SRC-1, `src/daemon/db.ts`, `src/daemon/runner.ts`, `src/daemon/queue.ts`; [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)).

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

#### On [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job)

Workflow role: the selected request-to-delivery route. Caller-to-daemon handoff carries stored upload names; daemon-to-Claude handoff carries a rebuilt task and filesystem access. Internal editorial ordering is prompt guidance, not host-enforced checkpoints. The CLI's terminal success is distinct from verified integration and from completion of later maintenance.

#### On [RT-RTE-lint-job](runtime.md#rt-rte-lint-job)

Workflow role: conditional post-ingest continuation, not an ingest acceptance gate. The automatic handoff carries no predecessor operations/result, only access to the retained wiki and a fresh maintenance task. Human review is requested in report text; no approval/resumption protocol makes a flagged issue an enforced workflow stop.

#### On [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery)

Workflow role: scheduler-level replay after interruption, rather than semantic rejection repair. Reusing the job payload with surviving file changes does not reconstruct a clean editorial starting state or prove successful recovery.
