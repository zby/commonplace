---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Eva-brain workflow account: source ingestion through delegated editing, structural admission, human review, recovery and desktop delivery."
run-id: AAS-2026-11-09-eva-brain-de4240cd9e79-01
reviewed-boundary: "706fb91f4ee851cc355785f4e7c6eab37146938f"
---

# Eva-brain workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **ingesting a source into the retained wiki**, including the held-review and rejection branches. It was selected because it connects the system's defining responsibilities: acquiring source material, asking an external agent to integrate it with existing knowledge, admitting or rejecting edits, and displaying the retained result. This is one shipped path, not a workflow assembled from independent tools. Its existing declaration is [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); its staging object is [RT-OBJ-ingest-worktree](runtime.md#rt-obj-ingest-worktree).

The account traces inspected implementation in SRC-1, `apps/desktop/src-tauri/src/ingest.rs` and `apps/desktop/src/main.ts`, at the boundary's frozen commit. It adds closer inspection of `ingest_enqueue`, `drive_codex_agent`, `drive_agent`, `run_job`, `verify_agent_write_boundary`, `gate_agent_changes`, `worker`, `ingest_decide`, `cleanup`, frontend ingest event handlers and `openVault`. These supply implementation evidence, including a model-directed prompt; they supply no observed run or causal experiment. The external runtime's internal tool loop is outside the frozen evidence. No target code or tests were executed. Successful integration, semantic correctness, model compliance and effective recovery in an actual run remain unobserved.

### Request, queue and delegated task

1. **A person supplies sources; Rust determines eligibility.** `ingest_enqueue` validates the brain and runtime and checks Node/tools before copying. It copies selected files into `raw/` only when the destination does not already exist, also discovers non-hidden files already there, excludes source names occurring anywhere in `log.md`, sorts the remaining names, and suppresses names already queued/current. Raw changes are committed before jobs are enqueued. The return is a count, not a completed wiki. This is filename/log-text eligibility, not content-change detection ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest); SRC-1, `apps/desktop/src-tauri/src/ingest.rs`).

2. **Rust serializes work and creates the edit boundary.** The worker pops one job, marks it running and calls `run_job`. Each job identifies its source, vault and numeric job ID. `run_job` reads the vault's runtime/model configuration and profile, captures HEAD and baseline lint issues, and creates a branch plus temporary worktree. The baseline commit anchors both protected-path verification and deletion comparison. The worktree provides the proposed patch; the model's textual reply does not stand in for that patch ([RT-OBJ-ingest-worktree](runtime.md#rt-obj-ingest-worktree)).

3. **Eva delegates integration, not admission.** `drive_agent` dispatches to Codex, Claude or OpenCode. For the inspected Codex handoff, the current directory is the worktree and the prompt names `raw/{source}`, asks the agent to read the vault contract first, and supplies the brain profile and profile guidance. It requests search-before-edit, merging rather than duplication, links, frontmatter, provenance and index reachability. It prohibits changes to raw/infrastructure, Git use and network access, and asks for a one-paragraph summary. These are requests to an external runtime, not evidence of compliance. Codex receives `workspace-write`; the alternate adapters and their requested controls are distinguished in [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest). The retained guidance path is [RT-BAP-vault-contract](runtime.md#rt-bap-vault-contract).

SRC-1, `apps/desktop/src-tauri/src/ingest.rs` supplies the integration instruction and return contract:

> 3. Search the existing Markdown pages with rg and read the relevant pages before editing. Prefer merging new information into existing pages; create a page only for a distinct entity or concept worth linking from elsewhere.
> --- `apps/desktop/src-tauri/src/ingest.rs`

> When finished, reply with one paragraph describing the pages you created or updated.
> --- `apps/desktop/src-tauri/src/ingest.rs:2632-2632`

The model owns the next read/edit decisions within that delegated task. Eva owns progression after the subprocess returns. The parent receives a summary and filesystem state, not an independently verified reasoning history. Task isolation here means a separate subprocess and worktree, not a demonstrated isolated model history or a whole-machine containment guarantee.

### Verification and admission

On successful agent return, `gate_agent_changes` first checks protected paths in both uncommitted status and base-to-HEAD changes. Thus an agent-created commit cannot bypass that check merely by leaving clean status. Protected edits fail before the branch can be offered for human acceptance. This is an admission rejection rule, not prevention of every external tool effect. The source explicitly distinguishes instruction from enforcement:

> /// Prompts are instructions, not an access boundary. Verify the immutable
> /// source collection and Eva's own instructions before an agent branch can
> /// ever be committed or shown for review.
> --- `apps/desktop/src-tauri/src/ingest.rs`

The gate then requires uncommitted changes, commits the agent edits, appends an Eva-owned operation log entry and commits that separately. Consequently an agent that commits all its otherwise permissible edits can still fail the no-changes check. The gate computes deleted paths with rename detection disabled, then compares post-edit lint issue strings against the baseline. A rename counts as deletion plus addition; inherited lint debt alone does not require review. These mechanisms and their limits belong to [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-CLM-structural-gate](runtime.md#rt-clm-structural-gate).

If there is neither deletion nor new issue, Rust merges automatically. Otherwise it produces a held result containing branch/worktree, diff, deletion list, new issues and summary. Lint is the structural comparator, not a semantic expected-answer oracle. Human acceptance can merge a branch with the displayed issues. The person need not approve every clean proposal; software performs that admission. The inspected path is an open ingestion task, not an experiment with reference answers.

### Human handoff and delivery

The worker stores held metadata and emits `ingest:review`. The frontend presents the patch, issues and deletions. The worker then stops, leaving queued sources awaiting a decision rather than proceeding past the held proposal. SRC-1, `apps/desktop/src-tauri/src/ingest.rs` makes this sequencing explicit:

> // Serial discipline: nothing else runs until the human decides.
>                 pause = true;
> --- `apps/desktop/src-tauri/src/ingest.rs`

`ingest_decide` locates the held item by job ID. Acceptance merges that branch, cleans up its worktree/branch, obtains the page count and emits `ingest:merged`. There is no second semantic gate in this command. The command accepts an `accept` boolean; the shipped frontend supplies the human decision, but this is not authentication of a human principal for every possible command caller.

Delivery has two linked boundaries: retained wiki state is delivered by a successful Git merge; desktop presentation follows the merge event. The frontend reloads the current brain:

> void listen('ingest:merged', async (event) => {
>   clearAgentActive();
>   forwardDev('merged', event.payload);
>   if (currentVault) await openVault(currentVault);
> });
> --- `apps/desktop/src/main.ts`

`openVault` rereads Markdown, builds the vault and graph, runs lint and renders the views (SRC-1, `apps/desktop/src/main.ts`). Therefore the agent's summary is not the only delivered product: retained page edits become desktop-visible wiki content. They can later be consumed by [RT-RTE-vault-query](runtime.md#rt-rte-vault-query), but a query is not required to finish ingestion. Event wiring establishes the intended delivery chain, not observed rendering success or downstream reliance.

### Rejection, failure and recovery limits

**Rejection is a terminal decision on the proposal, not a request for another model attempt.** `ingest_decide` removes the branch/worktree, writes a rejection entry to the real vault's log, commits it, emits `ingest:rejected`, marks the job rejected and resumes the pending queue. The frontend reloads to show the log entry. The retained log affects future eligibility: the rejected filename is suppressed on subsequent enqueue. The decisive retained text is:

> "Rejected in review; branch discarded.",
> --- `apps/desktop/src-tauri/src/ingest.rs`

This makes rejection consequential beyond discarding current edits. The inspected route does not automatically repair and resubmit the source; changing the filename/log state is outside this traced decision path ([RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)).

**Agent/gate errors take a different path.** In `run_job`, a failed agent call or a failed gate invokes cleanup and returns an error. The worker marks that job failed, emits `ingest:failed` and continues its loop rather than pausing for review. The UI displays the source and error. A hold pauses the queue; a failure does not itself schedule a retry. Cleanup requests forced worktree/branch removal but discards their errors, so a cleanup call is not proof that all residue was removed (SRC-1, `apps/desktop/src-tauri/src/ingest.rs`):

> let _ = git(vault, &["branch", "-D", branch]);
> --- `apps/desktop/src-tauri/src/ingest.rs`

Recovery is not transactional across the entire workflow. For example, automatic admission merges before linting the merged vault for its page count; a later error can report failure after the merge has already changed retained state. Held acceptance removes the item from in-memory held state before attempting its merge; a merge error returns without reinstalling that item or reaching queue resumption. Queue/review metadata is process-held while raw commits, branches and accepted pages are filesystem/Git state. These orderings prevent treating an error event as proof of rollback, or local Git staging as a durable recovery protocol. This agrees with the recovery limits of [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest), without claiming a demonstrated crash or failed merge.

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

#### On [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest)

Workflow-specific sequencing: the review handoff stops the worker; a completed accept/reject decision resumes queued work. Rejection discards the proposal but retains a log entry that suppresses future enqueue by filename. Agent/gate failure instead records a failed job and allows the worker loop to advance, without an automatic retry. Delivery is merge followed by a frontend Markdown reload, not merely the subprocess summary. The inspected ordering of merge, subsequent lint and held-state removal limits rollback and recoverability claims. The workflow account above supplies the source anchors and minimum passages for these sequencing details; no distinct route identity is introduced.
