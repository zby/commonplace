---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Kompl workflow account: staged source compilation through layered drafting, page admission, flush recovery and wiki delivery."
run-id: AAS-2026-10-14-kompl-9cffb1e5eb86-01
reviewed-boundary: "17970c969b0c2576bf722840e0e2db3c6416a7aa"
---

# Kompl workflow report

## Workflow account

### Selection and evidence limit

This account follows one included-source session from onboarding finalization to retained wiki pages. It selects this workflow because the shipped trigger and compile driver connect source admission, model computation, page review, persistence and later reading in one explicit path. It is not a constructed sequence of unrelated API capabilities. The representative success branch has readable sources, some successful extraction, eligible drafts, successful file flushes and either an existing schema or successful schema bootstrap. Manual review and flush failure are branches of that same path, not separate agent runtimes. [RT-RTE-session-compile](runtime.md#rt-rte-session-compile), [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

The evidence is SRC-1 implementation and shipped instructions at the revision in [the boundary](boundary.md#boundary-and-evidence). No target code, tests, services or providers were executed for this account. Consequently, the account establishes wiring and decision ownership, not a successful session, faithful model output or recovery observed under a crash. Historical provider reports do not supply a trace of this complete workflow at the reviewed revision.

### 1. The caller selects material; the application admits a session

The input is an existing staging session whose caller has included particular files, URLs or text. Finalization requires included pending or legacy-ingested rows. It checks the application's active-session state, declines another active session with 409, and handles a same-session replay without another trigger. It creates queued progress before contacting n8n and stamps the configured compile model name. This is authorization to start processing the selected sources, not approval of each generated page. The API's caller identity does not prove a human made either decision. SRC-1: `app/src/app/api/onboarding/finalize/route.ts`; [RT-RTE-session-compile](runtime.md#rt-rte-session-compile).

The first consequential handoff carries only `session_id` through the n8n webhook to the application's compile/run endpoint. The workflow's webhook responds on receipt with 202; the app separately returns `started` while a background promise runs. Neither acknowledgement means a wiki page has been delivered. n8n's error branch logs failure to start the app request; later background-step failures belong to the app, not to that already-returned HTTP request. SRC-1: `n8n/workflows/session-compile.json`, `app/src/app/api/compile/run/route.ts`.

> runCompilePipeline(session_id).catch((err: unknown) => {
> --- `app/src/app/api/compile/run/route.ts`

This is delegated computation under a fixed coordinator, not a parent agent assigning open-ended work to autonomous agents. The app chooses the next step and persists its progress. n8n provides the asynchronous trigger; Python endpoints and model providers receive task-specific work. [RT-RTE-session-compile](runtime.md#rt-rte-session-compile).

### 2. The driver turns sources into page proposals

The driver first health-checks required services and ingests staged files, then URLs, then text-like inputs. It checks cancellation between these steps. It then loads source rows and skips extraction for sources already represented in the extraction table. Missing extractions enter a worker queue with configured concurrency, default four. Each failed extraction logs its source and cause; zero successful extractions fails the session, while partial extraction success permits progression. A cancellation stops new extraction calls but does not abort calls already in flight. The executable worker loop, rather than the file header's older sequential description, establishes this behavior. SRC-1: `app/src/app/api/compile/run/route.ts`.

> if (extractSucceeded === 0) {
> --- `app/src/app/api/compile/run/route.ts`

Resolution returns canonical entities and concepts. Matching receives the session and canonical entities; planning receives those entities, concepts and match decisions. The app owns these handoffs, their HTTP error checks and timeouts. Models contribute extraction and ambiguous identity/update judgments; code controls the candidate limits and page-planning rules. The detailed candidate and promotion mechanisms are in [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), with its retained source passage for the top-three TF-IDF selection. These judgments have no expected-answer oracle in the production path; a model's decision is not verification against an independently supplied correct answer. SRC-1: `app/src/app/api/compile/run/route.ts`.

Plans become durable control state in [RT-OBJ-page-plans](runtime.md#rt-obj-page-plans), rather than a model-maintained agenda. Existing plans normally prevent destructive replanning. A newly extracted source not referenced by any existing plan forces planning again; committed plans remain preserved, while uncommitted plans may be rebuilt. Thus retry can preserve completed work but need not preserve every uncommitted draft. SRC-1: `app/src/app/api/compile/run/route.ts`.

### 3. Layered drafting supplies bounded contexts, not shared agent memory

The app drafts original-source, source-summary, entity, concept, comparison and overview layers in that order, with at most ten tasks running concurrently within a layer. Original-source pages copy raw prose into a generated frontmatter envelope without a drafting-model call. Other tasks receive readable sources, a selected extraction dossier, related earlier-draft summaries, optional existing page prose, optional saved schema, known titles and categories. The earlier-layer output is explicitly read from SQLite and reduced to title/type/summary context. It does not transfer a worker's hidden reasoning or whole model conversation. SRC-1: `app/src/app/api/compile/draft/route.ts`; [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft).

> const LAYER_ORDER = ['original-source', 'source-summary', 'entity', 'concept', 'comparison', 'overview'] as const;
> --- `app/src/app/api/compile/draft/route.ts`

The app caps known titles at 200, ranks/caps dossiers except for comparisons, and selects related summaries. Python subsequently prefix-truncates the assembled prompt at its configured character limit. The supplied runtime record retains the truncation passage. Therefore the HTTP request's full source list does not establish that all raw content reaches the generating model. Each page call is a temporary task context: selected inputs enter, returned markdown persists, and later calls explicitly reload selected artifacts. Provider-internal context handling remains uninspected. The saved schema requests conventions from the model; it does not choose the application's next step. [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft), [RT-BAP-schema-drafting](runtime.md#rt-bap-schema-drafting).

A drafting task with no readable sources throws. Other per-task failures are recorded against their plan, while successful siblings remain drafted. The draft endpoint reports counts, and the orchestrator continues to cross-reference and commit even when the reported draft-failure count is positive. This makes the workflow tolerant of partial production, not a verification that every planned page exists. SRC-1: `app/src/app/api/compile/draft/route.ts`, `app/src/app/api/compile/run/route.ts`.

### 4. Verification can reject structure or admission, not certify truth

The shipped cross-reference step deterministically injects title/alias wikilinks into drafted prose and advances it to crossreffed state. It excludes the page's own title from targets. It returns `contradictions_found: 0` as a fixed field; that zero is not a clean semantic review. The inspected handler does not call the model-backed contradiction detector described by older pipeline comments. SRC-1: `app/src/app/api/compile/crossref/route.ts`; [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft).

Commit then applies distinct gates:

- Any non-provenance-only crossreffed plan lacking draft content blocks that commit request with 422.
- A configured minimum-body-length check marks undersized generated pages `draft_too_thin` and skips them. It strips frontmatter first and exempts original-source pages.
- With auto-approval disabled, otherwise eligible content plans become pending approval. Provenance-only plans still commit without a content review.
- With auto-approval enabled, eligible content is installed by software, without waiting for per-page human approval.

SRC-1: `app/src/app/api/compile/commit/route.ts`; [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

> error: 'commit_blocked_null_drafts',
> --- `app/src/app/api/compile/commit/route.ts`

> if (bodyLength < minDraftChars) {
> --- `app/src/app/api/compile/commit/route.ts`

These checks test state, presence and size, not source fidelity or truth. Drafting models propose prose; fixed application predicates and configured mode decide ordinary admission. In manual mode an approval/rejection caller can veto installation. A pending draft's rejection changes its status to rejected and retains the row for audit; this is not rollback of an already committed page. The rejection API accepts only pending-approval state. SRC-1: `app/src/app/api/drafts/[plan_id]/reject/route.ts`.

> updatePlanStatus(plan_id, 'rejected');
> --- `app/src/app/api/drafts/[plan_id]/reject/route.ts`

Explicit approval runs the shared single-plan committer, requiring pending state and nonempty prose. It does not rerun the compile thin-body predicate. In both modes, review must be distinguished from successful file installation: single-plan approval can report success after a database commit even if its later file flush failed. Human review at the API boundary and semantic quality remain unestablished. SRC-1: `app/src/lib/approve-plan.ts`; [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

### 5. Admission, delivery and session completion are different events

For each ordinarily admitted content plan, one SQLite transaction writes page metadata, pending markdown, provenance, FTS content, activity and committed-plan status. Only afterwards does the app ask Python storage to install the compressed page file. Successful flush clears pending content and records the previous path; failures retain the outbox. Link synchronization and vector updates have separate error/retry policies, so this is not one atomic database/files/index transaction. SRC-1: `app/src/app/api/compile/commit/route.ts`; [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

After commit, the driver runs schema bootstrap and then marks session progress completed. An existing schema permits a skip; otherwise committed-plan metadata supplies a model-generated schema file for future drafting. This is retained guidance, not a retrospective validation of page accuracy. The bootstrap mechanism and its independently limited theory assessment are in [RT-RTE-schema-bootstrap](runtime.md#rt-rte-schema-bootstrap).

A first-session manual-review branch exposes a consequential distinction: drafts can be pending review while there are no committed plans and no schema. The schema handler then returns `no_committed_pages`, causing the driver to fail rather than complete. The pending drafts are not thereby erased. Approving drafts and retrying can supply committed plans to a later bootstrap attempt; a successful such recovery was not observed. SRC-1: `app/src/app/api/compile/schema/route.ts`, `app/src/app/api/compile/run/route.ts`, `app/src/lib/approve-plan.ts`.

For this workflow, a page is delivered as retained knowledge when the admitted content is available to wiki consumers, not when n8n acknowledges a request or a draft appears. The wiki data endpoint looks up page metadata, reads markdown and returns it with provenance sources. MCP exposes that read to an external agent, but Kompl does not control the agent's subsequent prompt inclusion or answer. The read endpoint can return empty content when its reader yields nothing; response success alone is not proof of complete prose delivery. SRC-1: `app/src/app/api/wiki/[page_id]/data/route.ts`; [RT-RTE-mcp-read](runtime.md#rt-rte-mcp-read).

The session completion flag is narrower still: the driver rejects reported pending flush failures, but it does not require every extraction, draft or secondary vector update to have succeeded. A zero-source branch can mark all downstream steps skipped and complete without new compiled pages. Therefore completion means the selected driver branch reached its end under its gates, not universal source coverage or a verified answer. SRC-1: `app/src/app/api/compile/run/route.ts`; [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion).

### Checked recovery path: database commit succeeds, file flush fails

This failure occurs after the plan is already committed in SQLite. The commit endpoint retries pending page flushes after the page loop and, on later invocations, even when no crossreffed plans remain. If failures remain, the driver marks commit failed and throws before schema/completion. The app's background catch records session failure. n8n cannot infer that later outcome from its earlier successful start request. SRC-1: `app/src/app/api/compile/commit/route.ts`, `app/src/app/api/compile/run/route.ts`; [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion).

The caller can invoke the retry endpoint. It checks competing sessions, resets retryable progress and re-triggers n8n. On re-entry, the driver uses extraction/plan state to avoid blindly repeating expensive successful model work; commit reconciliation can flush the retained outbox despite zero new plans to commit. The recovery owner is application code plus a caller initiating retry, with startup reconciliation as a separately wired fallback. It is not an agent improvising repairs. SRC-1: `app/src/app/api/compile/retry/route.ts`, `app/src/app/api/compile/run/route.ts`, `app/src/app/api/compile/commit/route.ts`; [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

> resetForRetry(session_id);
> --- `app/src/app/api/compile/retry/route.ts`

This is completion recovery by finishing an outstanding write, not full rollback. Previous-file archival and pending markdown aid recovery; they do not undo every metadata, index or semantic change. Explicit approval uses a weaker success condition than the session driver. An old file can remain preferred over pending prose by some readers, and chat's file-only read can miss an unflushed new page. These consumer differences prevent treating database commitment as uniformly current delivery. [RT-CLM-durable-completion](runtime.md#rt-clm-durable-completion), [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval).

### Inspection coverage

Direct inspection for this account covered SRC-1 `app/src/app/api/onboarding/finalize/route.ts`, `n8n/workflows/session-compile.json`, the full compile driver, drafting's layer/context/result-handling section, commit's gates/transactions/flush/reconciliation, deterministic crossref, schema bootstrap, retry, draft rejection, the single-plan approval helper and the wiki data endpoint. The retry handler adds source coverage beyond the supplied runtime's named reads. These are implementation evidence; comments were checked against executable branches where consequential. Extraction/resolution/matching/planning internals, Python prompt truncation, startup reconciliation and MCP formatting use the supplied runtime records rather than a second full inspection. No claim of exhaustive caller coverage, live concurrency exclusion, semantic correctness or crash-tested delivery follows.

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

#### On [RT-RTE-session-compile](runtime.md#rt-rte-session-compile)

Workflow role: primary request-to-retained-page path selected above. The decisive coordination boundary is early trigger acknowledgement versus later app-owned progress and failure. Handoff acceptance establishes that background work was requested, not that its products passed admission or reached readers. Retry responsibility remains with the application and retry caller; no model owns rescheduling.

#### On [RT-RTE-plan-draft](runtime.md#rt-rte-plan-draft)

Workflow role: layered proposal production. Source-summary and later page layers exchange persisted selected summaries/categories rather than full worker contexts. Partial drafting failure can coexist with downstream admission of successful siblings. This handoff structure explains why reaching commit is not an all-proposals-success verdict.

#### On [RT-RTE-draft-approval](runtime.md#rt-rte-draft-approval)

Workflow role: branch between generated prose and retained knowledge. Manual rejection vetoes a pending proposal without erasing its audit row; it does not reverse prior committed content. The session driver and single-plan approver expose different success boundaries, so a workflow consumer must distinguish pending review, database commitment, readable file delivery and session completion.
