---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM Repo Wiki workflow from repository-change maintenance through model proposals, human revision decisions and indexed delivery."
run-id: AAS-2026-11-09-llm-repo-wiki-55aae7f87b1b-01
reviewed-boundary: "38a439cd649105c0cd90b687fc1f8d8dd1d0986c"
---

# LLM Repo Wiki workflow report

## Workflow account

### Selected workflow and evidence boundary

The representative workflow is incremental wiki maintenance after repository changes: synchronize source evidence, draft updates to affected pages, review proposals, and index accepted prose for later consumption. It was selected because it connects the shipped acquisition, model-production, human-admission and retrieval paths without inventing a supervising agent. The initial-outline branch explains how the same author job bootstraps pages, but is not a second independent workflow. The canonical routes are [RT-RTE-repo-sync](runtime.md#rt-rte-repo-sync), [RT-RTE-author-pages](runtime.md#rt-rte-author-pages) and [RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission).

All source inspection is SRC-1 at the frozen commit. The workflow is implementation wiring, not an observed successful run. Additional substantive coverage includes the complete author job and bulk-review helper, job registration and queue configuration, acceptance/rejection/index scheduling in the store, the synchronization-to-author handoff, review actions and the complete page-index worker (SRC-1, `src/agent/author.ts`, `src/wiki/review.ts`, `src/agent/jobs.ts`, `src/jobs/queue.ts`, `src/wiki/store.ts`, `src/ingest/sync.ts`, `src/ingest/jobs.ts`, `src/app/w/[wiki]/actions.ts`, `src/ingest/index-page.ts`). These passages supply implementation evidence; comments explain intent but do not authenticate their reported incidents. No target code or tests were executed.

### 1. Code hands repository changes to an author worker

An operator sync, poll or webhook enters the synchronization route. Its code performs ingestion rather than asking a model to select download or indexing actions; source-chunk persistence and its partial-failure limits are established by [RT-RTE-repo-sync](runtime.md#rt-rte-repo-sync). After file processing succeeds, nonempty changed paths cause a stale-marking attempt and author enqueue. The job payload supplies repository ID, previous SHA, target SHA and changed paths. A stale-marking failure is logged without preventing the enqueue (SRC-1, `src/ingest/sync.ts`):

> await deps.enqueueAuthor({ repoId, fromSha, toSha, changedPaths });
> --- `src/ingest/sync.ts`

The ingestion registration supplies a repository-keyed queue handoff; author registration supplies database access, wiki-scoped store/search factories, an author model and the configured token budget. The receiver rereads repository state to resolve wiki scope and uses the indexed SHA when available rather than blindly trusting an older coalesced payload. The enqueue precedes the sync transaction advancing `syncedSha`; this ordering does not establish an atomic source-snapshot/author-start barrier (SRC-1, `src/ingest/sync.ts`, `src/ingest/jobs.ts`, `src/agent/jobs.ts`, `src/agent/author.ts`).

### 2. The author worker selects work and delegates bounded writing calls

The worker builds instructions from schema, repository/SHA and project context, then reads the existing tree and page citations. For ordinary incremental work it selects pages that cite this repository and are stale or cite changed paths. It processes at most the page budget, checking accumulated token spend between pages. After those updates it considers up to forty changed paths not already cited and asks a model to place relevant material in existing or new pages. The model may return no additions. On an initial sync or when no existing page cites the repository, an outline call instead receives a bounded file list, README excerpts and the wiki tree (SRC-1, `src/agent/author.ts`; [RT-RTE-author-pages](runtime.md#rt-rte-author-pages)).

This is delegation from deterministic job code to separate model calls, not a model delegating tasks to tool-using subagents. Query strings come from page titles, changed citation paths and model outline items. Code executes source-only search across the wiki's repositories, deduplicates hits and caps their count. An update call receives the current accepted body plus selected evidence prefixes, not the full repository or the entire preceding workflow state. Only the structured draft and accounting escape the writing call. The model cannot itself choose a shell command, delete a page or move it on this route (SRC-1, `src/agent/author.ts`; [RT-RTE-author-pages](runtime.md#rt-rte-author-pages)).

### 3. Mechanical screening produces proposals, not verified facts

The worker validates paths and parent availability, drops pages with no evidence, requests structured Markdown and citation strings, and filters citations. A new page needs at least one surviving source citation; an update may retain exact old citation keys. The proposal store call supplies page identity, current base revision, Markdown, citations, author-run identity and a reason containing the SHA. These controls screen provenance and revision compatibility, not entailment or every factual claim. Evidence text is clipped while grounding uses chunk metadata, so surviving citations do not prove every referenced line reached the writer ([RT-RTE-author-pages](runtime.md#rt-rte-author-pages), SRC-1, `src/agent/author.ts`).

Proposal persistence is the author's delivered result. It is not publication. A run returns proposed, skipped and dropped paths with status; a successful run can therefore have partial output. The human review phase is a separate action, not an automatic continuation of the model loop. Its decision can veto the proposed knowledge change; software supplies no expected-answer oracle ([RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission)).

### 4. Review chooses whether a proposal becomes current

Wiki-scoped server actions accept/reject one revision or call the bulk decision helper. Acceptance checks proposed status and compares parent revision against current revision under a store transaction/lock. An intervening edit causes a conflict rather than silent prose rebasing. Direct editor saves are a different apply-mode path; this account does not generalize the proposal requirement to all application writes (SRC-1, `src/app/w/[wiki]/actions.ts`, `src/wiki/store.ts`; [RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission), [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn)).

Bulk review orders parent pages first for acceptance and children first for rejection. This matters because an accepted child beneath an unpublished parent can remain hidden, while removing emptied new parents requires removing children first. Expected per-item `WikiError` failures are collected; other exceptions escape. Bulk delivery is thus a count plus explicit failed items, not all-or-nothing acceptance (SRC-1, `src/wiki/review.ts`):

> await (accept ? store.acceptRevision(p.id) : store.rejectRevision(p.id));
> result.done++;
> --- `src/wiki/review.ts`

### 5. Accepted persistence and searchable delivery are separate endpoints

Acceptance sets the revision to accepted, points the page at it and clears stale status. Only after commit does the store request indexing. The page-index worker rereads the named revision and skips missing, unaccepted or no-longer-current revisions. Otherwise it splits Markdown, obtains embeddings and transactionally replaces page chunks. This is a second asynchronous delivery boundary, not part of the acceptance transaction (SRC-1, `src/wiki/store.ts`, `src/ingest/index-page.ts`; [RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission)).

A current accepted revision is available to page reads and export; indexed sections become available to search and hence later model queries. These endpoints are not identical: enqueue failure is caught after acceptance, and the current-revision check occurs before remote embedding, not again inside the chunk-replacement transaction. The wiring therefore does not guarantee immediate or strictly synchronized search delivery. Later chat/MCP interpretation and exported-file use are bounded separately by [RT-RTE-chat-turn](runtime.md#rt-rte-chat-turn) and [RT-RTE-external-consumption](runtime.md#rt-rte-external-consumption). No inspected execution establishes actual use or benefit.

### Failure and rejection paths

A malformed or timed-out individual draft is dropped while remaining pages can proceed. Auth, credit and rate-limit errors are rethrown; if all attempted drafts fail and nothing is proposed, the author also fails the run. The job records failure and throws to queue machinery. Queue configuration requests five retries with backoff and a two-hour author expiry. Those are requested scheduling controls dependent on pg-boss, not a guarantee that a timed-out handler is cancelled (SRC-1, `src/agent/author.ts`, `src/jobs/queue.ts`).

> if (isSystemicError(err)) throw err;
> draftFailures++;
> --- `src/agent/author.ts`

Retries are not whole-run rollback. Already persisted proposals remain; updates skip an existing same-SHA proposal, and initial processing skips paths already citing the repository. A human rejection changes proposal status, and rejecting the last proposal of a never-accepted childless page removes the page. An outdated proposal instead fails acceptance with an explicit instruction to reject and re-propose; no automatic model repair is invoked by that error (SRC-1, `src/agent/author.ts`, `src/wiki/store.ts`):

> throw new WikiError("conflict", "This proposal is outdated: the page changed after it was written. Reject it and re-propose.");
> --- `src/wiki/store.ts`

The operator owns that recovery decision. A later author run can propose again after rejection, but the reviewed paths do not establish an immediate rejection-triggered reauthoring loop. Reverting an accepted revision restores prior body/citations through another applied revision rather than undoing the full sync/author/index workflow ([RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission)). Neither per-page dropping nor human veto alone establishes content-directed criticism or improved future writing.

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

#### On [RT-RTE-author-pages](runtime.md#rt-rte-author-pages)

Workflow role: bounded producer between source synchronization and separate human review. The author result ends at proposal persistence; there is no worker-owned acceptance step. Partial draft failure can coexist with a succeeded run and delivered proposals. Recovery preserves earlier writes and uses existing-page/same-SHA skips rather than rolling back the run. The account's draft-error quotation supplies the workflow-specific failure branch (SRC-1, `src/agent/author.ts`).

#### On [RT-RTE-revision-admission](runtime.md#rt-rte-revision-admission)

Workflow coordination: bulk decisions sort by path depth in opposite directions for accept/reject and retain expected item failures while continuing. This adds ordering and partial-result semantics to the existing admission route, not a separate admission authority. Accepted persistence is its delivery endpoint; indexed retrieval is downstream and asynchronous. The account retains the bulk-call and stale-parent rejection passages (SRC-1, `src/wiki/review.ts`, `src/wiki/store.ts`, `src/ingest/index-page.ts`).
