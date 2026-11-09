---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "LLM Repo Wiki runtime: repository synchronization, model drafting, revision admission and retained-content consumers at the frozen commit."
run-id: AAS-2026-11-09-llm-repo-wiki-55aae7f87b1b-01
reviewed-boundary: "38a439cd649105c0cd90b687fc1f8d8dd1d0986c"
---

# LLM Repo Wiki runtime report

## Runtime account

### Work and evidence basis

The shipped system turns GitHub repository snapshots into a searchable local index and model-written wiki proposals. A separate review surface admits proposals; chat can also write directly through a narrower approval protocol. Retained pages, source chunks and conversation summaries subsequently reach models or external MCP clients. This is a database-backed production and consumption pipeline, not one autonomous agent controlling every step (SRC-1, `src/worker.ts`, `src/agent/author.ts`, `src/agent/chat.ts`, `src/wiki/store.ts`).

All implementation findings below concern SRC-1 at the boundary's commit. No application, test, model call or benchmark was executed, and no execution trace was supplied. Wiring is inspectable; actual activation, model compliance, deployment isolation and benefit remain unobserved. Added substantive inspection beyond the boundary's initial coverage includes `src/agent/chat-store.ts`, `src/agent/server.ts`, `src/agent/tool-names.ts`, `src/agent/models.ts`, `src/agent/retrieved.ts`, `src/agent/explain-answer.ts`, `src/ingest/prepare.ts`, `src/ingest/repos.ts`, `src/ingest/poll.ts`, `src/ingest/webhook.ts`, `src/ingest/embedder.ts`, `src/jobs/queue.ts`, `src/mcp/handlers.ts`, `src/search/explain.ts`, `src/search/rerank.ts`, `src/lib/env.ts`, `src/lib/openrouter-privacy.ts`, `src/project/actions.ts` and `SECURITY.md`. These supply implementation or declared-design evidence, not observed runs. Supporting files named elsewhere in this member were also inspected at SRC-1.

### Ordinary invocation, from acquisition to later use

1. A local operator adds an `owner/name` repository through the shipped repository surface. `addRepo` validates the name, checks wiki ownership, resolves the default branch and head with GitHub, persists a queued repo row and enqueues synchronization. Manual sync, scheduled polling and signed push webhooks converge on `desiredSha` plus the same queue. The web process enqueues; the separately started worker consumes. See [RT-RTE-repo-sync](#rt-rte-repo-sync) (SRC-1, `package.json`, `src/worker.ts`, `src/ingest/repos.ts`, `src/ingest/poll.ts`, `src/ingest/webhook.ts`).
2. Code, not a model, chooses full reconciliation versus incremental comparison, downloads a commit tarball, filters and secret-scans files, chunks surviving content and embeds it. Per-file transactions replace changed chunks. Changes mark citing pages stale and enqueue an author run. A file failure can leave earlier file transactions committed while preventing `syncedSha` advancement; retry uses hashes and diff-derived change reporting. This is recoverable incremental work, not an atomic snapshot swap (SRC-1, `src/ingest/sync.ts`, `src/ingest/prepare.ts`).
3. The author job resolves the repo's wiki, current indexed SHA, project context, schema and existing tree. Initially a model proposes an outline; code validates paths and page/token budgets, retrieves source evidence for each selected page, and calls the author model with a structured page schema. Code strips unsupported source links and requires at least one surviving citation before writing a proposal. Incremental runs update stale/affected pages and ask a model where uncovered changed files belong. See [RT-RTE-author-pages](#rt-rte-author-pages), [RT-CMP-author-model](#rt-cmp-author-model) (SRC-1, `src/agent/author.ts`, `src/agent/jobs.ts`).
4. Human-facing actions accept or reject revisions, edit directly, or restore accepted bodies. Acceptance compares the proposed parent revision to the current revision under a wiki write lock; it does not silently rebase prose. Accepted changes enqueue asynchronous wiki-section indexing. The store catches enqueue failure, so accepted persistence does not guarantee immediate searchable content. See [RT-RTE-revision-admission](#rt-rte-revision-admission) (SRC-1, `src/app/w/[wiki]/actions.ts`, `src/wiki/store.ts`, `src/ingest/index-page.ts`).
5. Later chat turns load server-side conversation state, build instructions from schema, project, tree and optional summary, and let a model choose tool calls or a final answer within eight steps. Search supplies bounded excerpts; tools read/write the scoped store. The UI stream and messages persist sources and intermediate steps. Alternatively an MCP host requests search/page content, or the export CLI writes accepted Markdown. These consumers do not share all admission and grounding controls. See [RT-RTE-chat-turn](#rt-rte-chat-turn), [RT-RTE-context-fold](#rt-rte-context-fold), [RT-RTE-external-consumption](#rt-rte-external-consumption) (SRC-1, `src/agent/chat.ts`, `src/agent/context.ts`, `src/mcp/server.ts`, `src/export/export.ts`).

### Material challenges to broad guarantees

Four forcing cases distinguish enforcement from intent:

- **A model creates rather than overwrites a page in chat.** Background author writes are always proposals, but chat constructs tools with `mode: "apply"`. Approval policy covers update, move and delete, not create. `createPage` forwards that mode to the store, which creates an accepted revision and schedules indexing. Thus “all agent writes are reviewed proposals” would be false. This is a supported shipped caller, not merely a theoretical store API bypass. Human decisions gate selected tool calls, not every new retained statement. See [RT-RTE-chat-turn](#rt-rte-chat-turn).
- **A draft cites an old source or a range outside the delivered prefix.** New author citations must fall within retrieved chunk metadata, but updates also admit exact pre-existing citation keys. Evidence text truncates hit content to 6,000 characters while grounding compares the full hit's line bounds. This establishes provenance/range filtering, not proof that every cited line was shown, that every claim is cited, or that citations entail the prose. Chat does not apply this filter; the explainer does. See [RT-RTE-author-pages](#rt-rte-author-pages), [RT-RTE-explain-answer](#rt-rte-explain-answer).
- **A page has only an unaccepted proposal.** Store `getPage` exposes an empty body when no current revision exists. MCP `read_page` instead deliberately retrieves the newest proposal and labels it unreviewed. Export omits unpublished pages and their unreachable subtrees. Consequently “unreviewed content never reaches a consumer” is false, even though it is not the normal indexed accepted-page body. See [RT-RTE-external-consumption](#rt-rte-external-consumption).
- **A guarded privacy option is disabled or an alternate caller is used.** Production chat/author and embedding wiring request provider ZDR by default, not locally enforce remote retention. Turning `OPENROUTER_ZDR` off yields no provider restriction. The explainer rejects reranking when ZDR is on; the retrieval evaluation directly calls reranking with provider preferences instead of that UI gate. It may fail remotely rather than being locally excluded. This is a shipped alternate path, not evidence of actual disclosure. See [RT-CLM-provider-routing](#rt-clm-provider-routing), [RT-RTE-retrieval-eval](#rt-rte-retrieval-eval).

### Control ownership, grant and isolation

The chat model's capability surface is search, tree/page reads and page create/update/move/delete. Its current grant is the store and search bound to one wiki plus a fixed author/run identity and apply mode. There is no model shell, arbitrary network executor or token-reading tool in this factory. The executor is application TypeScript and database transactions; arbitrary repository text is not executed as source code. The background writer has no tools at all: code retrieves and writes proposals (SRC-1, `src/agent/tools.ts`, `src/agent/chat.ts`, `src/agent/author.ts`). These findings describe the inspected tool surface, not a sandbox around the Node process or external provider.

Store locks, scoped SQL and optimistic revision checks are implementation invariants within the store paths, dependent on PostgreSQL transaction/advisory-lock behavior. They are not user authentication. Local-only operation is a deployment requirement: `SECURITY.md` explicitly says there is no login, while the shipped dev/start commands bind to loopback. This does not establish a live install's network exposure or per-human authorization (SRC-1, `SECURITY.md`, `package.json`, `src/wiki/store.ts`).

The approval owner is the chat host/AI SDK protocol, configured with a server-derived secret and an allowlist of approval-requiring tools. Server message merging accepts only decisions on stored pending approvals, not client-rewritten tool arguments. Store functions themselves do not demand a human token: human actions, background proposals, chat tools and injected library callers are distinct paths. Guarantee strength is **protocol** for the selected chat-tool approvals, not a store-wide invariant; implementation conclusion status: wired; operation conclusion status: uninspected. SDK signature verification and approval execution internals are an external contract, not independently inspected here (SRC-1, `src/agent/models.ts`, `src/agent/chat-store.ts`, `src/agent/chat.ts`, `src/agent/tool-names.ts`).

Retrieved-tag escaping and “data, not instructions” text constrain encoding and request model behavior; they cannot establish universal prompt-injection resistance. Freshness flags and last-seen-head messages likewise expose state rather than verify that a page remains semantically correct (SRC-1, `src/agent/retrieved.ts`, `src/agent/prompts.ts`, `src/mcp/handlers.ts`).

### Changes, recovery and measurement

Knowledge admission is split between automatic ingestion, software-screened author proposals, explicit revision review, and chat's selectively approved direct writes. Operator-edited schema instructions are reread each call; changing the file changes subsequent instructions without a restart. Project-context changes enter through a validated server action. These are distinct authority paths; no per-content human admission is implied for ingestion or chat-created pages (SRC-1, `src/agent/prompts.ts`, `src/project/actions.ts`, `src/agent/author.ts`, `src/agent/tools.ts`). See [RT-BAP-schema-instructions](#rt-bap-schema-instructions).

pg-boss owns retry scheduling. Queue configuration supplies five retries, backoff and longer sync/author expiry. Author calls have 120-second timeouts, page drafts may be dropped individually, and systemic auth/credit/rate-limit errors fail the run for retry. Total tokens are checked between calls/pages, not a hard pre-call maximum. Chat records steps, tokens, sources and outcomes, persists responses per step, keeps consuming after the browser disconnects, and uses a per-chat abort controller for explicit Stop. These are wired recovery/observability paths, not measured reliability or latency (SRC-1, `src/jobs/queue.ts`, `src/agent/author.ts`, `src/agent/chat.ts`).

The deterministic daily lint job reports findings, not autonomous model revision. The retrieval evaluator compares fixed strategy variants against expected file paths and reports recall, reciprocal rank, latency and reranking cost. It does not automatically install a winning search policy. Package scripts also expose author/chat/MCP benchmarks and citation evaluation; their detailed evaluator semantics were not inspected here, so no result or oracle claim is made for those drivers. They remain included available evidence, not an access gap (SRC-1, `src/wiki/jobs.ts`, `eval/run.ts`, `package.json`). Direct product-code or production-machinery self-modification is not established by these inspected paths; no exhaustive absence claim is made. Detailed retained-memory transformations and epistemic quality judgments are left to the specialist members.

## Shared records

### Components

#### RT-CMP-chat-model
Label: Chat model

Distributed-parametric remote language model selected by `CHAT_MODEL`, default `anthropic/claude-haiku-5.5`; application stores model identity and usage, not weights. It decides tool calls and answers in chat, and is available to the answer explainer through production model wiring. No inspected call trains or updates its parameters. Provider-side parameter changes are uninspected; exact weights/version are not pinned by the configured identifier, and the mutable remote endpoint may resolve differently. Model output is interpreted as natural-language answers or symbolic tool calls (SRC-1, `src/agent/models.ts`, `src/lib/env.ts`, `src/agent/chat.ts`).

> return openrouter().chat(env().CHAT_MODEL, { ...accounting, ...providerPrivacy() });
> --- `src/agent/models.ts`

#### RT-CMP-author-model
Label: Author and summary model

Distributed-parametric remote model selected by `AUTHOR_MODEL`, default `anthropic/claude-haiku-5.5`. Used for outline/page generation and for conversation folding; summary wiring uses `authorModel()`, not a separately configured cheap model. Provider storage holds parameters; Postgres holds resulting proposals, summaries and accounting. No local parameter update is wired. Exact weights are unpinned and mutable endpoint resolution remains possible; provider internals are uninspected (SRC-1, `src/agent/models.ts`, `src/agent/server.ts`, `src/agent/author.ts`, `src/agent/context.ts`, `src/lib/env.ts`).

> summaryModel: authorModel(),
> --- `src/agent/server.ts`

#### RT-CMP-embedding-model
Label: Embedding model

Distributed-parametric remote embedding model selected by `EMBEDDING_MODEL`, default `openai/text-embedding-3-small`. Produces dense vectors stored with model IDs on source/wiki chunks; query embeddings feed cosine retrieval. No inspected parameter update during operation; new vectors are derived data, not weight training. Exact provider weight version is unpinned; endpoint substitution is possible and internals uninspected. The adapter checks dimensions, not semantic model equivalence (SRC-1, `src/ingest/embedder.ts`, `src/search/index.ts`, `src/lib/env.ts`).

> const model = provider.textEmbeddingModel(opts.model, opts.provider ? { provider: opts.provider } : undefined);
> --- `src/ingest/embedder.ts`

#### RT-CMP-rerank-model
Label: Optional rerank model

Remote distributed-parametric cross-encoder reached through OpenRouter `/rerank`, with configurable explainer model default `cohere/rerank-4-pro` and fixed strategy names in the retrieval evaluation. It returns symbolic indices and relevance scores. Parameters live remotely, no local parameter mutation is wired, exact weights are unpinned, and mutable endpoint resolution remains possible. Provider internals remain uninspected. Chat's ordinary hybrid search does not invoke it (SRC-1, `src/search/rerank.ts`, `src/search/explain.ts`, `src/search/index.ts`, `eval/run.ts`).

> const documents = hits.map((h) => `${h.kind === "source" ? h.path : h.pagePath}\n${h.content}`.slice(0, 4_000));
> --- `src/search/rerank.ts`

### Operative objects

#### RT-OBJ-wiki-schema
Label: Wiki schema instruction text

Natural-language Markdown in repository-root `WIKI_SCHEMA.md`; read from the process working directory and incorporated in author/chat instruction strings. It is static shipped guidance until an operator changes the file, not generated retained experience. Its reload path is per-call file reading; rollback is ordinary file replacement, with no schema-review gate in this loader. Detailed page-content objects are left for memory analysis (SRC-1, `src/agent/prompts.ts`, `WIKI_SCHEMA.md`).

> /** Read per call (not cached) so editing WIKI_SCHEMA.md changes the next answer without a restart. */
> --- `src/agent/prompts.ts`

### Routes

#### RT-RTE-repo-sync
Label: Repository synchronization and refresh

Owner: application ingestion code and separate worker. Trigger/principal: operator add/sync, polling schedule, or valid default-branch push. Repo UUID, wiki UUID, desired/synced commit hashes and source paths govern progression. Code decides full versus incremental work; GitHub supplies bytes, chunker/embedder produce chunks/vectors, Postgres persists source state. Models do not choose these steps. This is automatic source-state admission after the operator admits a repository, not per-file human approval. Filtering can reject files; removing the repository is a separate explicit destructive path. Recovery uses per-file transactions, hashes, recorded errors, queue retries and another sync; there is no all-files rollback. No answer oracle applies to normal ingestion (SRC-1, `src/ingest/repos.ts`, `src/ingest/sync.ts`, `src/ingest/jobs.ts`, `src/ingest/prepare.ts`, `src/ingest/poll.ts`, `src/ingest/webhook.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: admission/sync requests return queued status; the worker returns sync statistics or missing/locked/up-to-date states.
- Later read-back: retained source chunks feed author evidence, application search and MCP search; changed paths trigger wiki maintenance.
- Delegated visibility: the background worker receives repo IDs and rereads database state; embedding endpoints receive surviving chunk text, not an agent conversation.
- Selection predicate: registered repo/default branch and desired commit; full reconciliation on initial/too-large comparison, otherwise diff paths; path/content/secret filters precede chunking.
- Invalidation or expiry: changed/deleted files reconcile chunk rows; citations mark pages stale; changed desired SHA can requeue work. No wall-clock semantic expiry is enforced.
- Activation or effect: wired replacement of source chunks, SHA/status updates and author scheduling; actual downstream model behavior unobserved.
- Evidence limits: secret detection is a scanner decision, not proof all secrets are detectable; partial file commits and failed stale marking prevent a universal atomic-freshness guarantee.

> // Modified into something we refuse (a secret, a size blow-up): it must leave the index.
> --- `src/ingest/sync.ts`

> if (findings.length) {
> --- `src/ingest/prepare.ts`

The scanner branch is shared by full and incremental preparation. In the latter, a changed file no longer accepted is removed if previously indexed. Claims about secret exclusion cover detected files on these paths, not human wiki prose or chat input.

#### RT-RTE-author-pages
Label: Model page proposal production

Owner: author worker code. Open maintenance request over a registered repository, not a bounded learning curriculum. Models propose outlines, query terms and page prose; code chooses evidence, applies budgets and validates outputs; a human may later veto proposals through review. Guidance is schema plus project/repo/SHA instructions. Output is natural-language Markdown with symbolic citation metadata in proposed revisions. No reference-answer oracle is used. A dropped page, retry or human rejection is not evidence of content-directed theory criticism. Source-change repair is requested, but model compliance and semantic improvement are unobserved (SRC-1, `src/agent/author.ts`, `src/agent/prompts.ts`, `src/agent/jobs.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposed, skipped and dropped paths plus mode/status, with progress/accounting logs.
- Later read-back: existing page prose/citations/tree affect subsequent author runs; accepted/indexed results reach chat and search; proposal bodies also reach explicit review/MCP reads.
- Delegated visibility: separate outline and draft calls receive selected context; drafts receive bounded retrieved excerpts rather than the complete repository or conversation.
- Selection predicate: initial/no-citing-pages versus incremental; affected stale/citing pages first, then uncovered changed paths; up to five nonblank queries, six hits per query, sixteen deduplicated source hits.
- Invalidation or expiry: latest indexed SHA is used; idempotency checks skip existing same-SHA proposals; old citation keys may survive updates; outdated proposals require rejection/reproposal at admission.
- Activation or effect: creates proposed revisions only; downstream behavioral activation unobserved.
- Evidence limits: citation checks constrain references, not entailment, complete claim coverage or receipt of every line in a truncated hit; token checks occur between calls and do not cap each run exactly.

> const ok = (c: Citation) => isGrounded(c, hits) || keptKeys.has(citationKey(c));
> --- `src/agent/author.ts`

> if (citations.length === 0) return drop(path, "the draft cited no retrieved source");
> --- `src/agent/author.ts`

> * Every write is a proposal; this job has no delete or move tool at all.
> --- `src/agent/author.ts`

Guarantee owner: author job. Enforcement point: grounding plus proposal-mode store calls. Guarantee strength: invariant for proposal mode in this job; best effort for factual grounding. Covered paths: initial creation, cross-repo extension and incremental update. Alternate chat/human store writes do not use this author filter. External contracts: search hit metadata, model structured output and database persistence. Implementation conclusion status: wired; operation conclusion status: uninspected.

#### RT-RTE-revision-admission
Label: Human revision decisions and direct editing

Owner: local UI/server actions plus wiki store. Proposer: author model or human editor; decision/veto: human-facing accept/reject/edit actions, mechanically checked by the store. Normal operating mode is open review/editing, not an experiment; there is no software answer oracle. Software permits acceptance based on revision status, scope and unchanged parent, not semantic truth. Direct human edits apply immediately; revert copies body/citations of an accepted revision into another applied revision. Guidance for what to accept is not enforced here. Accepted Markdown, citations, revision history and logs persist (SRC-1, `src/app/w/[wiki]/actions.ts`, `src/wiki/store.ts`, `src/ingest/index-page.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: action success/error with refreshed UI; bulk action delegates ordered decisions and per-item handling.
- Later read-back: current accepted revision reaches page reads/export; asynchronously indexed sections reach search; history enables body/citation restoration.
- Delegated visibility: index worker gets page/revision IDs and rereads the accepted body for embedding.
- Selection predicate: wiki-scoped page/revision IDs; accept requires proposed status and matching parent/current revision; revert requires accepted status.
- Invalidation or expiry: subsequent current revision makes pending proposals outdated; rejecting the last proposal may remove a never-accepted childless page.
- Activation or effect: accepted/current pointers and stale flags change in transactions; index is eventually scheduled, not atomically committed with acceptance.
- Evidence limits: actor label human is assigned by local server actions, not authenticated identity; no supplied run establishes a person actually reviewed content.

> if (rev.parentRevisionId !== page.currentRevisionId) {
> --- `src/wiki/store.ts`

> console.error("[wiki] enqueue index-page failed", { pageId, revisionId }, err);
> --- `src/wiki/store.ts`

Guarantee owner: store; enforcement point: locked transaction and parent comparison. Guarantee strength: invariant for stale-parent rejection on store acceptance, dependent on PostgreSQL. Index worker checks current revision before embedding, but the inspected code does not repeat that check inside its replacement transaction after the remote embedding call. Thus even its stale-job check does not establish strict synchronization under all interleavings. Search hydration does not compare indexed revision against the page's current revision (SRC-1, `src/ingest/index-page.ts`, `src/search/index.ts`).

#### RT-RTE-chat-turn
Label: Persistent chat with selectively approved writes

Owner: application chat host/AI SDK loop. User supplies newest turn; model decides search/read/write/answer steps from natural-language instructions and tool schemas. Stored chat UUID and wiki scope select authoritative history; page paths resolve server-side. A server-generated agent-run identity attributes writes. `createWikiTools` is instantiated in apply mode. Create can run immediately; update/move/delete wait on the approval protocol. Human can veto those calls; merging a new user message denies pending approvals. No expected-answer oracle is used. This is an open interactive task, not an automatic improvement experiment (SRC-1, `src/agent/chat.ts`, `src/agent/chat-store.ts`, `src/agent/tools.ts`, `src/agent/tool-names.ts`, `src/agent/models.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: streamed text, tool activity and sources; response messages saved per step and completion.
- Later read-back: server messages and optional summary feed later turns; applied page writes reach normal wiki consumers.
- Delegated visibility: model sees active messages, schema, project, tree, summary and bounded tool outputs; no shell/subagent executor is supplied by this tool factory.
- Selection predicate: chat must belong to requested wiki; incoming user text or decisions on the latest stored assistant approval only; model chooses tools, with search capped at eight hits of 6,000 characters each.
- Invalidation or expiry: regenerate truncates later messages; Stop aborts the active controller; loop ends at eight steps or ordinary model completion/approval boundary. No guaranteed answer correctness follows.
- Activation or effect: tools execute scoped store effects; browser disconnect alone does not stop execution; precise influence of retained prose on model behavior unobserved.
- Evidence limits: search-before-answer and cite-every-claim are instructions, not a code-enforced retrieval predicate; chat does not strip invented citations; SDK approval internals are outside frozen evidence.

> const tools = createWikiTools({ store, wikiSlug: deps.wikiSlug, search: deps.search, author: { kind: "agent", agentRunId: run.id }, mode: "apply" });
> --- `src/agent/chat.ts`

> export const WIKI_TOOL_APPROVAL = {
>   updatePage: "user-approval",
>   movePage: "user-approval",
>   deletePage: "user-approval",
> } as const;
> --- `src/agent/tool-names.ts`

These implemented routes support a narrower conclusion than a universal human-review gate. Chat-created page content is admitted by the model/software tool call. For overwrites, approval of a particular tool call is the human contribution; optimistic base-revision checks separately reject conflicts. Rollback is a later accepted-revision restore, not automatic repair of model mistakes; move/delete do not provide an equivalent restore in this factory.

#### RT-RTE-context-fold
Label: Conversation folding for later turns

Owner: deterministic context code selects the fold boundary; author model writes the compressed summary. Trigger: estimated active history exceeds budget, normally 60,000 tokens using JSON length divided by four. It retains recent whole user-turn groups, normally about 20,000 tokens, and keeps the newest user turn even if over budget. The model receives prior summary plus a transcript of old turns; tool input/output is clipped before summarization. The fold removes old turns from model-visible active context, not from database history. This is a separate model invocation/frame whose summary escapes; it is not a delegated agent with arbitrary tool access (SRC-1, `src/agent/context.ts`, `src/agent/chat-store.ts`, `src/agent/prompts.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: summary, remaining active messages and folded flag to the chat caller.
- Later read-back: persisted summary and summarized-through message ID determine subsequent chat context.
- Delegated visibility: summarizer sees prior summary and transformed old transcript, not the complete future chat/tool state; foreground receives only summary plus recent tail.
- Selection predicate: active messages after the stored fold marker; code selects oldest prefix ending before a retained user boundary.
- Invalidation or expiry: later folds replace the summary; if the marker is missing from messages, activeMessages returns all supplied messages. Regeneration's interaction with an existing summary is not repaired in the inspected truncateAfter routine.
- Activation or effect: summary replaces old turns in next model instructions; exact behavioral influence and summary accuracy unobserved.
- Evidence limits: budget is an estimate of messages, not total instructions or a hard context-window guarantee; fold can be skipped when no removable older user boundary exists.

> await setSummary(input.db, input.chatId, summary, toFold.at(-1)!.id);
> return { summary, active: active.slice(boundary), folded: true };
> --- `src/agent/context.ts`

Admission here is software/model-controlled: no per-summary human approval or answer oracle. Failed generation throws and fails the request rather than silently claiming a completed fold. Guidance asks to retain goals, decisions, page paths and cited facts. Persistence is within the chat across later turns; detailed memory interpretation belongs to the memory member.

#### RT-RTE-external-consumption
Label: MCP and Markdown export consumers

Owner: requesting external MCP host or local export operator; server/export code determines delivered content. MCP resolves one wiki at startup and registers search/read/list/status/sync, not wiki-write tools. Search ranks in scoped SQL, then compact profile deduplicates per file/page and clips to 500 characters, default five hits; full profile defaults to eight at 1,500 characters. Explicit limit can change hit count. It rewrites internal links, strips invisible Unicode and marks freshness relative to latest seen head. MCP read selects accepted body, or latest proposal for a never-accepted page. Export loads accepted current revisions and emits deterministic linked Markdown, refusing a nonempty output directory without force (SRC-1, `src/mcp/server.ts`, `src/mcp/handlers.ts`, `src/export/export.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: MCP text tool result/error; export file count and on-disk Markdown.
- Later read-back: external host may consume results or exported files, but its retention and reasoning are outside boundary; sync requests can refresh retained source state.
- Delegated visibility: host gets transformed snippets, explicit page reads, citations and status, not application credentials or database access through these tools.
- Selection predicate: scoped hybrid search plus profile clipping/deduplication; read by page path; export accepted reachable tree only.
- Invalidation or expiry: no automatic invalidation of already-delivered host text/exported files; status labels expose staleness; subsequent sync/export can refresh.
- Activation or effect: supplied material is available to host interpretation; host compliance/behavior unobserved; sync tool queues rather than performs indexing inline.
- Evidence limits: MCP annotations are hints, not host isolation; a proposal-only read deliberately exposes unreviewed prose, unlike export.

> const body = accepted ? page.bodyMd : (proposal?.bodyMd ?? "");
> --- `src/mcp/handlers.ts`

> if (!file) continue; // unreachable: an ancestor is unpublished
> --- `src/export/export.ts`

#### RT-RTE-explain-answer
Label: Optional retrieval explainer and grounded answer

Owner: operator selection plus explainer code. Search can display vector, FTS and fused rankings and optionally invoke a reranker; a separate answer request takes selected chunk keys, rereads them within the wiki and calls the chat model. It does not trust client-supplied text. Output citation filtering reuses author grounding; wiki hits lack source-kind grounding support, so this filter is not a general wiki-answer warrant. Models propose relevance ordering or answer text; code maps valid indices and strips unsupported source links. Human selects inputs, but there is no expected-answer oracle or automatic durable wiki admission (SRC-1, `src/search/explain.ts`, `src/search/rerank.ts`, `src/agent/explain-answer.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ranking explanation or answer Markdown, surviving/stripped citations, tokens and cost.
- Later read-back: inapplicable — this answer route does not install wiki revisions or a retained instruction update.
- Delegated visibility: reranker receives query plus path/content prefixes; answer model receives selected rehydrated hits through bounded evidenceText.
- Selection predicate: wiki-scoped keys and rank lists; optional rerank is rejected locally when ZDR is enabled.
- Invalidation or expiry: missing chunk keys disappear on hydration; if all are gone answer generation fails and asks for another search.
- Activation or effect: produces diagnostic/answer output, not an automatic policy or knowledge change.
- Evidence limits: rerank scores and citation occurrence do not establish correct answers; no supplied execution shows successful ranking or benefit.

> * explainer can show which citations survive. Chat itself does not strip citations.
> --- `src/agent/explain-answer.ts`

#### RT-RTE-retrieval-eval
Label: Retrieval strategy evaluation driver

Owner: operator starts fixed strategy comparison; code computes metrics. `eval/golden.json` provides pinned repo/SHA, questions and expected paths. Expected paths are the answer oracle for file retrieval, not factual answer content. Models provide embeddings/reranking; fixed code computes first matching path rank, recall@5 and MRR@10, time and cost. No winner is automatically admitted to production. The evaluator may reuse an existing repository's wiki, move its desired commit to the golden SHA and call sync with maintenance callbacks disabled; it is therefore not necessarily a side-effect-free read-only measurement (SRC-1, `eval/run.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: metric table and optional JSON to stdout, or process failure.
- Later read-back: synchronized source index persists; printed scores have no implemented production-policy read-back in this driver.
- Delegated visibility: remote embedding/reranking receives evaluation text; no worker delegation or per-strategy human judgment is needed.
- Selection predicate: fixed strategies, optionally substring-filtered by CLI argument; oracle matches expected file paths within top ten.
- Invalidation or expiry: golden SHA pins evaluated source input; provider identifiers do not pin weights; no automatic restoration of the pre-eval desired SHA is implemented here.
- Activation or effect: changes source index if needed and measures strategy outputs; no causal benefit or deployed winner inferred.
- Evidence limits: not executed; fixed path labels do not validate semantic answer quality, model citation correctness or general performance.

> const rank = hits.slice(0, K_MRR).findIndex((h) => h.kind === "source" && expected.includes(h.path));
> --- `eval/run.ts`

> if (st.rerank) {
> --- `eval/run.ts`

The direct rerank branch forwards providerPrivacy preferences but does not use the explainer's local ZDR exclusion. Exact remote rejection/retention behavior remains an external contract.

### Claims

#### RT-CLM-provider-routing
Label: Provider privacy requests and their limits

Claimed operation: default calls route to endpoints with zero retention and denied data collection. Source-native helper implements request preferences; chat/author models, embedding wiring and rerank caller wiring use it. `OPENROUTER_ZDR=false` returns an empty object. This is request-level policy dependent on SDK forwarding and provider enforcement, not evidence of actual provider deletion. The explainer additionally blocks reranking locally when enabled; the evaluation uses direct reranking with the preferences (SRC-1, `src/lib/openrouter-privacy.ts`, `src/lib/env.ts`, `src/agent/models.ts`, `src/search/index.ts`, `src/search/explain.ts`, `src/ingest/embedder.ts`, `eval/run.ts`).

> return env().OPENROUTER_ZDR ? { provider: { zdr: true, data_collection: "deny" } } : {};
> --- `src/lib/openrouter-privacy.ts`

Guarantee owner: application sets request policy; provider must fulfill it. Enforcement point: model/embedding/rerank options, plus explainer's local guard. Guarantee strength: policy. Implementation conclusion status: wired; operation conclusion status: uninspected. Injected library models/embedders and benchmark-specific internals were not exhaustively traced; no universal all-calls or deployed-retention conclusion is warranted.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-schema-instructions
Label: Editable schema to model instructions

Consumer: author and chat models. Channel: per-call Markdown file loading followed by instruction-string composition. Force: requested model behavior, not deterministic validation of all schema prose. Horizon: next author/chat invocations after file editing, across sessions while the file remains. Operator can propose/admit/replace the file through filesystem editing; the loader provides no review, rejection or rollback mechanism beyond read failure and file replacement. The guidance shapes outlines, page prose and chat editing; generated proposals do not rewrite the schema on the inspected routes. This is a live instruction-change affordance, not demonstrated self-improvement or a theory-building loop (SRC-1, `src/agent/prompts.ts`, `src/agent/author.ts`, `src/agent/chat.ts`).

> return readFile(path.join(root, "WIKI_SCHEMA.md"), "utf8");
> --- `src/agent/prompts.ts`

The exact instruction object's identity is [RT-OBJ-wiki-schema](#rt-obj-wiki-schema). The account does not infer learning or criticism from configurable guidance alone.

## Annotations

none
