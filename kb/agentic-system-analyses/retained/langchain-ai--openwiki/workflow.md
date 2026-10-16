---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "OpenWiki workflow: native repository planning, bounded page workers, rejection recovery and durable wiki delivery."
run-id: AAS-2026-10-14-openwiki-8f502f680f75-01
reviewed-boundary: "7c469e59584bfac3f97f5c32a67604de46805999"
---

# OpenWiki workflow report

## Workflow account

The representative workflow is native repository `init` or `update`: request → durable run → planner → assigned page workers → page admission → deterministic finalization → retained wiki. It was selected because the shipped runner connects these stages explicitly and supplies both corrective rejection and failure recovery. This is the existing [RT-RTE-native-generation](runtime.md#rt-rte-native-generation), not a new workflow assembled from unrelated tools. The [boundary](boundary.md) fixes SRC-1 and its evidence limits. This report describes implementation and prompt contracts, not an observed successful execution; no target, tests, examples or providers were run.

### 1. Request and durable control

The native repository branch is reached from repository-mode init/update requests. The CLI/agent dispatch is established by [RT-RTE-native-generation](runtime.md#rt-rte-native-generation). `runNativeRepositoryGeneration` calls the core begin/resume operation, returns immediately on a strict no-op, otherwise plans only when the retained phase is `planning`, runs pending pages, and finally invokes finish. OpenWiki code owns these transitions; a model cannot declare the run complete through narration. SRC-1, `src/agent/repository-runner.ts`.

The durable [RT-OBJ-repository-run-state](runtime.md#rt-obj-repository-run-state) holds the queue rather than the agents' conversations. Resume rejects conflicting mode or language requests. It resets skipped jobs to pending; a changed repository fingerprint removes the plan and restores planning. Thus resume can reuse accepted progress, but cannot blindly reuse a plan for changed source. These are fixed-rule lifecycle decisions, not semantic assessments of page truth. SRC-1, `src/generation/repository-run.ts`.

> if (sourceChanged) {
>     nextState.phase = "planning";
>     nextState.sourceFingerprint = currentSource.fingerprint;
> --- `src/generation/repository-run.ts`

### 2. Planner-to-core handoff

The runner creates a fresh planner with the configured model, read-only filesystem tools and `submit_plan`. Its prompt supplies mode, wiki goal, user/connector planning context, per-page update windows and Claim issues. It asks for repository-specific research and a small information architecture, not prose pages. Page jobs carry title, purpose, seed paths, related pages and page-specific instructions; planned deletions are a separate part of the plan. [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance) identifies the semantic part of this handoff. SRC-1, `src/agent/repository-runner.ts`, `src/agent/repository-prompts.ts`.

The planner chooses semantic scope. The core constructs and persists the canonical plan, then changes the phase to generating. A duplicate semantic plan is accepted; a different already-installed plan is rejected rather than silently replacing the queue. Invalid-input planning errors become corrective tool responses; exiting without a submitted plan throws and prevents page generation. Source establishes these gates, not that the model follows the requested research depth. SRC-1, `src/generation/repository-run.ts`, `src/agent/repository-runner.ts`; the missing-submission passage is retained in [RT-RTE-native-generation](runtime.md#rt-rte-native-generation).

### 3. Core-to-page-worker handoff

Delegation is performed by runner code, not by the planner launching subagents. For each pending job the runner creates a fresh page agent. The model is reused, but each attempt starts a fresh graph conversation without a repository-generation checkpointer. This does not exclude conversation-derived retention through the shared history backend. The worker receives the job's semantic guidance, output language, whether the page exists, the count of existing Claims and the stale/unresolved Claims requiring explicit decisions. The complete planned page map is included only for quickstart. Other pages do not automatically receive that map or predecessor conversations in their initial prompts. Source files and existing pages remain available through tools. Both planner and page agents also receive the shared `/conversation_history/` backend mount; possible access to retained predecessor material is separate from initial prompt transfer. SRC-1, `src/generation/repository-run.ts`, `src/agent/repository-prompts.ts`, `src/agent/repository-runner.ts`.

> claimsRequiringAttention: existingClaims.filter(({ issue }) => issue),
> --- `src/generation/repository-run.ts`

> job.path === "/openwiki/quickstart.md"
>     ? `The complete planned page map is:\n${JSON.stringify(
> --- `src/agent/repository-prompts.ts`

The native backend grants writes to the assigned page only; model-facing `task` delegation is removed. Those controls and their external dependency limits are established in [RT-CLM-native-confinement](runtime.md#rt-clm-native-confinement). Worker narration does not return to the parent as a synthesized report: the stream forwards bounded tool lifecycle events. The consequential return is an admitted page plus durable Claims and queue progress. Source therefore supports fresh initial working contexts and artifact-mediated lifecycle coordination, not complete conversation isolation. Both agents use `createAgentBackend`, which mounts durable history under the configured OpenWiki home, defaulting to `~/.openwiki/conversation_history`. Model-facing tool writes there are denied, but the source-native test distinguishes direct middleware backend writes and later backend reads. This is a possible conversation-derived retention channel outside page admission; actual offload, payload selection and cross-worker consumption are unobserved. It is not an inspected host compaction policy. SRC-1, `src/agent/repository-runner.ts`, `src/agent/agent-backend.ts`, `src/config/openwiki-home.ts`, `test/agent/conversation-history-offload.test.ts`; [MEM-OBJ-conversation-history](memory.md#mem-obj-conversation-history) and [MEM-RTE-history-offload](memory.md#mem-rte-history-offload) retain the load-bearing passages and limits.

When concurrency exceeds one, a process-local claimed-ID set and serialized acquisition avoid assigning the same job twice in that runner. Quickstart is held back until the first worker wave ends, then runs with one slot, so its navigation can use the other pages. This ordering is not proof that every other page was freshly generated: some may have been skipped. Nor is the claimed-ID set a cross-process reservation. SRC-1, `src/agent/repository-runner.ts`, `src/generation/repository-run.ts`.

> if (!pool.fatal && heldBack.size > 0) {
>     pool.size = 1;
>     await runWorkerLoops(run, model, onEvent, view, pool, new Set(), 0);
>   }
> --- `src/agent/repository-runner.ts`

### 4. Page admission and corrective rejection

The worker researches, writes its page and submits sparse Claim decisions: confirmations of rechecked issue Claims, revised/new propositions and retractions. It can request the complete current Claim set when intentionally changing otherwise-current content. The prompt requests canonical `repo://` evidence resources and says to correct errors and retry. Unchanged current Claims are retained automatically, so the handoff is not a demand to regenerate the full Claim set. SRC-1, `src/agent/repository-prompts.ts`, `src/agent/repository-runner.ts`; [RT-RTE-native-generation](runtime.md#rt-rte-native-generation).

The core checks generating phase and pending-job identity, requires readable Markdown, repairs/validates frontmatter, then serializes shared mutation. It reconciles Claims, finalizes their persisted state, proves page durability, records page completion in the manifest and writes the updated queue. The core supplies other pending pages as exclusions to Claim finalization. This excludes them from session persistence and eligibility entries, but does not establish complete pending-page noninterference: the verification projector receives no exclusion set and visits all discovered pages. An omitted active event can therefore remove an existing OpenWiki stamp on another pending page. No observed race, semantic corruption or failed delivery is established. SRC-1, `src/claims/brains/code/session.ts`, `src/claims/brains/code/runtime.ts`, `src/okf/claims-verification.ts`.

> for (const page of await store.discoverPages()) {
> --- `src/okf/claims-verification.ts`

> const active = verificationByPage.get(page);
>     const next = active ? [...retained, { ...active }] : retained;
> --- `src/okf/claims-verification.ts`

These projector passages bound the exclusion's effect; they do not overturn per-submission durability ordering or whole-run checks. [RT-CLM-page-durability](runtime.md#rt-clm-page-durability) supplies the retained ordering evidence. SRC-1, `src/generation/repository-run.ts`.

An `invalid_input` submission failure returns a tool rejection in the same attempt rather than completing the worker:

> "Correct the assigned page or sparse Claim decisions and call submit_page again.",
> --- `src/agent/repository-runner.ts`

A successful tool call sets the worker's submitted flag. If its stream subsequently throws, the runner still treats the page as submitted. Admission is therefore the delivery point for that worker, not a final conversational answer. A non-invalid-input submission failure is treated as fatal and escapes rather than being retried as an ordinary page attempt. The strongest gate verifies structural/state consistency and persistence; no independent semantic answer oracle or per-page human approval is wired into this sequence. Accepted prose can still be wrong. SRC-1, `src/agent/repository-runner.ts`, `src/generation/repository-run.ts`; [RT-RTE-native-generation](runtime.md#rt-rte-native-generation).

### 5. Failed attempt, retry and bounded recovery

Before the first attempt, code snapshots the page's Markdown and persisted Claims sidecar. An ordinary unsubmitted attempt gets at most one fresh retry. Between attempts, code restores those artifacts and constructs a fresh graph with a new initial prompt, rather than restoring the failed graph's conversation through a checkpointer. That restoration does not establish deletion or rollback of conversation-derived files in the shared history mount; later backend access remains possible, while actual reuse is unobserved. A rate-limit failure bypasses immediate retry. In a concurrent pool it reduces the live worker limit by one, never below one. The model does not choose these recovery decisions. SRC-1, `src/agent/repository-runner.ts`, `src/generation/repository-run.ts`.

> const PAGE_WORKER_ATTEMPT_LIMIT = 2;
> --- `src/agent/repository-runner.ts`

> await restoreRepositoryPage(run, snapshot);
> --- `src/agent/repository-runner.ts`

After unsuccessful attempts, skip restores the snapshot, rebuilds the Claims runtime from disk under the mutation lock, writes interrupted metadata and records the job as skipped. Successful neighboring pages remain durable. This is page-local restoration, not all-or-nothing rollback of the update. Fatal errors instead stop new work; in-flight workers can settle, and the runner rethrows before finish. The durable state supports later begin/resume, subject to source-drift replanning. Source shows recovery mechanics, not crash-proof filesystem transactions or successful recovery in a supplied trace. SRC-1, `src/agent/repository-runner.ts`, `src/generation/repository-run.ts`.

### 6. Whole-run delivery

Finish refuses a queue with pending jobs and requires matching original snapshots for skipped jobs. It applies deletions, finalizes wiki artifacts, restores skipped Markdown after that pass, finalizes/proves Claims durability and replaces the page manifest. Only pages actually regenerated in this run advance their source checkpoints; untouched pages keep their prior checkpoints. With skipped pages or source drift, update metadata remains interrupted even though finish can return complete. The resumable state file is removed last. SRC-1, `src/generation/repository-run.ts`; [RT-CLM-page-durability](runtime.md#rt-clm-page-durability).

> if (skippedPages.size > 0 || sourceChanged) {
> --- `src/generation/repository-run.ts`

The delivered result is the retained Markdown wiki and its Claims, navigation/provenance, manifest and update metadata, plus bounded CLI progress/status. Complete means lifecycle finalization succeeded, not exhaustive fresh coverage or semantic verification. A separate later consumer can search and read selected sections through [RT-RTE-wiki-retrieval](runtime.md#rt-rte-wiki-retrieval); this downstream availability is not evidence of actual use or benefit. The host-generation protocol and scheduled PR admission remain distinct alternatives in [RT-RTE-host-generation](runtime.md#rt-rte-host-generation) and [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission). Native page restoration is not attributed to raw external host writes or Git publication.

### Added inspection and limits

Within SRC-1, this member inspected the native begin/plan/worker/stream sequence, concurrent acquisition and quickstart ordering, attempt limits and fatal-error handling in `src/agent/repository-runner.ts`; complete prompt construction in `src/agent/repository-prompts.ts`; and resume, plan submission, job-context projection, snapshots, restoration, skip, page submission and finish portions of `src/generation/repository-run.ts`. For this correction, it additionally inspected planner/page backend construction and retry restoration in `src/agent/repository-runner.ts`, the history mount and tool permissions in `src/agent/agent-backend.ts`, home-directory resolution in `src/config/openwiki-home.ts`, and direct-write/edit/read-back and tool-denial contracts in `test/agent/conversation-history-offload.test.ts`. The tests were read, not executed. It also inspected pending exclusions and projection propagation in `src/generation/repository-run.ts`, `src/claims/brains/code/session.ts`, `src/claims/brains/code/runtime.ts`, and `src/okf/claims-verification.ts`. These provide implementation evidence and shipped prompt/test intent. They add workflow detail to the supplied runtime records, not independent observed-run evidence. Dependency internals, live provider behavior, semantic accuracy and end-to-end reliability remain uninspected; the trace is selective, not an exhaustive inventory of all OpenWiki workflows.

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

#### On [RT-RTE-native-generation](runtime.md#rt-rte-native-generation)

Workflow handoffs: planner admission installs the queue; page assignment projects only required Claim issues by default; page admission is the worker's completion event; finish supplies whole-wiki delivery. With concurrent workers, quickstart is deferred to a final single-slot pass. Invalid-input rejection permits same-attempt correction. Ordinary non-submission permits one fresh graph retry from restored page/Claim artifacts; restoration is not a rollback of the shared history mount, whose actual offload/reuse remains unobserved. Rate limiting skips immediate retry and can lower concurrency. Fatal submission failure prevents finish. These are workflow-specific details of the supplied route, not a distinct declaration.

#### On [RT-OBJ-page-guidance](runtime.md#rt-obj-page-guidance)

Workflow context boundary: every worker receives its page guidance and issue Claims; only quickstart receives the complete planned page map. Planner research and failed-attempt conversations are not automatically transferred in initial prompts or restored by a generation checkpointer. This is not a guarantee that conversation-derived material cannot cross stages: native workers share a durable history mount that affords middleware offload and later backend reads, with actual selection and cross-worker use unobserved. Page/Claim snapshot recovery does not establish history rollback. The source and page artifacts also remain tool-readable; fresh initial context does not imply loss of access.

#### On [RT-CLM-page-durability](runtime.md#rt-clm-page-durability)

Workflow delivery distinction: completion of a submitted job precedes whole-run finalization. Skipped-page snapshot restoration can coexist with a complete finish result and interrupted update metadata. Page-level admission and whole-run return therefore must not be interpreted as proof that all planned pages were regenerated or all source checkpoints advanced.
