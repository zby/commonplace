---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Siftly workflow account: browser-driven JSON import through model enrichment, category admission and delivery of retained results."
run-id: AAS-2026-10-18-siftly-b81c94cf0f77-01
reviewed-boundary: b25daa45b858f4be096b5c368671c34db4407d8e
---

# Siftly workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is a browser JSON import followed by enrichment and categorization, ending with persisted annotations and a browser completion indication. It is selected because it connects the shipped input driver, model calls, executable admission checks and retained output. A later retrieval request illustrates consumption, not an automatic continuation of the import. This is an application-controlled model workflow, not evidence of an autonomous multi-agent conversation. The browser and server own progression; model executors return judgments rather than choosing the next application stage. See [RT-RTE-import-content](runtime.md#rt-rte-import-content), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize) and [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch).

Evidence is implementation in SRC-1 at the reviewed revision. Inspection checked the pipeline, browser categorization driver, categorization parser/writer and vision failure handling: `app/api/categorize/route.ts`, `app/import/page.tsx`, `lib/categorizer.ts`, `lib/vision-analyzer.ts`. These are paths already within the boundary, not additional sources. No execution trace or experiment establishes that this workflow completed, that model judgments were correct, or that a later agent benefited.

### Request and first handoff

The user supplies the JSON file. The import handler parses it, creates an ImportJob, skips duplicate tweet IDs and persists bookmarks and media. It returns counts and a job ID. The file endpoint does not itself launch enrichment. On mounting the categorization step, the browser uses importedCount to decide whether there is work: zero returns without starting; a nonzero value checks server progress and either attaches to an existing pipeline or starts one. This distinguishes file admission from delegation of model work. The ordinary start request supplies an empty object, not the newly imported IDs, so the server can select all bookmarks with enrichedAt=null, including older unfinished work. Explicit IDs and force are alternate selectors, not the normal upload handoff (SRC-1, `app/import/page.tsx`, `app/api/categorize/route.ts`; [RT-RTE-import-content](runtime.md#rt-rte-import-content), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

The server returns started/total before its asynchronous task finishes. Its process-global status, counters and abort flag support polling and stop requests; they are not the ImportJob or a durable queue. POST rejects an already-running/stopping state with 409, and the browser treats 409 as a reason to poll rather than a fatal start failure. This coordinates the inspected process, not multiple deployment instances (SRC-1, `app/api/categorize/route.ts`, `app/import/page.tsx`; [RT-OBJ-categorization-state](runtime.md#rt-obj-categorization-state)).

### Server delegation and model context

The task resolves an optional SDK client, seeds default categories, optionally clears selected failure markers, and backfills entities before the selected bookmark workers begin. Entity backfill is broader than the requested bookmark-ID list. Five workers process bookmarks; each analyzes untagged media, enriches missing semantic tags and places its bookmark ID in a shared category queue. A flush takes up to 25 IDs, reloads database content and composes a category prompt. Consequently the categorizer receives retained text and metadata after earlier writes, not an uninterrupted conversation with the vision executor (SRC-1, `app/api/categorize/route.ts`; [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

The handoffs cross distinct identities: workers use database Bookmark.id; categorization prompts and responses use tweetId; the writer maps returned tweet IDs to database rows. Category descriptions/slugs are loaded once for the run and guide prompts and filtering. Models receive stage-selected context: media or image URL for vision, text/entities/image summaries for semantic enrichment, and bounded text/metadata plus available categories for categorization. Only returned structured content passes back into the application. The runtime baseline documents truncation and dispatch differences; omitted source content is not automatically reloaded into the model call (SRC-1, `lib/categorizer.ts`, `lib/vision-analyzer.ts`; [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch), [RT-BAP-category-guidance](runtime.md#rt-bap-category-guidance)).

These are requests to external executors, not delegation of Siftly scheduling authority. Text stages prefer Codex for OpenAI or Claude on the other provider branch when available, with SDK fallback. Vision prefers an available SDK client and takes its CLI path only without one. External CLI tools, internal turns and permissions remain outside the inspected implementation boundary; provider settings alone do not identify every actual backend (SRC-1, `lib/categorizer.ts`, `lib/vision-analyzer.ts`; [RT-RTE-model-dispatch](runtime.md#rt-rte-model-dispatch)).

### Verification and admission

The server, not a reviewing agent or human, admits ordinary enrichment. Categorization parses a JSON array, normalizes assignments, clamps numeric confidence and filters unknown slugs. The writer skips empty assignments and missing database identities, then transactionally upserts memberships and updates enrichedAt. Existing memberships omitted by a new response are not removed. A successful transaction is acceptance of structurally admissible annotations, not verification of their semantic truth (SRC-1, `lib/categorizer.ts`; [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

No expected-answer oracle or per-result human veto occurs on this path. The requested assignment count is prompt policy, not an enforced parser bound. Returned tweet IDs are checked against the database, not against the current batch: the checks do not establish current-batch confinement. Starting the workflow therefore cannot be read as human approval of each model-generated category. This admission mechanism differs from the separate category-suggestion UI selection and manual category editing (SRC-1, `lib/categorizer.ts`; [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize), [RT-RTE-category-admission](runtime.md#rt-rte-category-admission)).

### Failure, recovery and stopping

A concrete rejection path is malformed categorization output. CLI parse failure falls through to SDK; without a client the call throws. The queue flush catches a categorization exception, logs it and proceeds. There is no semantic critic that asks for a revised category judgment in this branch. Empty accepted results can also produce no writes while the flush still increments its categorized count by the number of queued IDs. Thus attempts, admitted rows and correct annotations are distinct quantities (SRC-1, `lib/categorizer.ts`, `app/api/categorize/route.ts`; [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

Vision retries selected transient errors, but terminal failure writes imageTags=`{}`. A normal pass skips non-null imageTags. Force clears that marker and semanticTags=`[]`, while keeping other successful metadata; it is not universal recomputation. A URL cache can also reuse another row's failure marker. Recovery belongs to application retry rules and caller reprocessing, not an agent recovering a suspended plan (SRC-1, `lib/vision-analyzer.ts`, `app/api/categorize/route.ts`; [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

DELETE requests cooperative stop rather than cancelling provider calls or rolling back writes. Worker completion always attempts the final queue drain, so queued categories can still be written after a stop request; the abort flag suppresses the final FTS rebuild. Process loss discards queue/progress state but not already committed rows. Ordinary re-selection can revisit rows lacking enrichedAt, without reconstructing the lost queue or resetting every previously written stage result (SRC-1, `app/api/categorize/route.ts`; [RT-OBJ-categorization-state](runtime.md#rt-obj-categorization-state), [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

### Delivery and its limits

The task attempts FTS rebuilding unless aborted, then returns progress to idle; caught item, batch or rebuild failures need not prevent idle. Persisted bookmark/media metadata and memberships are the work product. The browser's completion indication is a separate delivery signal driven by polling, not a proof that every selected row was enriched or correctly categorized. The completion and lost-connection rules are annotated below (SRC-1, `app/api/categorize/route.ts`, `app/import/page.tsx`; [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)).

Later consumers independently request this retained product. AI search selects candidates and supplies retained metadata to a reranking model; the local CLI reads the database and emits JSON without AI reranking. These are wired delivery paths to a browser/API caller or external agent, not evidence of downstream successful use. A skipped/failed rebuild or stale cache/index can separate successful row persistence from fresh search visibility (SRC-1, `app/api/search/ai/route.ts`, `cli/siftly.ts`, `lib/fts.ts`; [RT-RTE-search-content](runtime.md#rt-rte-search-content), [RT-RTE-cli-export](runtime.md#rt-rte-cli-export)).

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

#### On [RT-RTE-import-content](runtime.md#rt-rte-import-content)

Workflow handoff: the categorization step does not pass the import job's ID or a list of newly imported bookmarks. It passes force or an empty body. This makes the ordinary processing scope the server's unfinished collection rather than exactly the latest import (SRC-1, `app/import/page.tsx`). The baseline retains the start-request passage.

#### On [RT-RTE-enrich-categorize](runtime.md#rt-rte-enrich-categorize)

Delivery signal: browser polling runs every second and marks done on idle, including idle reached after a stop. Five consecutive polling exceptions terminate local polling with a refresh instruction; this does not stop the server task. Refresh can attach to running/stopping progress through the mount check. This is connection recovery, not durable job recovery (SRC-1, `app/import/page.tsx`).

> if (data.status === 'idle') {
>           if (pollRef.current) clearInterval(pollRef.current)
>           pollRef.current = null
>           setDone(true)
>           setRunning(false)
>           setStopping(false)
>         }
> --- `app/import/page.tsx`

> setError('Lost connection to the server. The pipeline may still be running — refresh to check.')
> --- `app/import/page.tsx`

Verification limit: the category count advances by attempted queue membership after a nonthrowing writer return, even if the model returned no writable assignments. The UI counters cannot serve as a per-record acceptance oracle (SRC-1, `app/api/categorize/route.ts`, `lib/categorizer.ts`).

> await writeCategoryResults(results)
>                   counts.categorized += ids.length
> --- `app/api/categorize/route.ts`

> if (results.length === 0) return
> --- `lib/categorizer.ts`

> if (!result.tweetId || result.assignments.length === 0) continue
> --- `lib/categorizer.ts`
