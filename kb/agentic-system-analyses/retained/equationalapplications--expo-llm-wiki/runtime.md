---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "expo-llm-wiki runtime baseline: local memory admission, retrieval, shipped callers and remote integration at the frozen revision."
run-id: AAS-2026-11-08-expo-llm-wiki-54f1fc1a0310-01
reviewed-boundary: "09c90258560a6b1664038d642b5d25d9de0c4d3d"
---

# expo-llm-wiki runtime report

## Runtime account

### What runs, and who owns the next step

The target is a memory engine with shipped consumers, not a general agent host. The [boundary](boundary.md) fixes SRC-1 and the whole-repository scope. Its claimed work is turning conversations and documents into reusable facts, tasks and graph relations. The core `WikiMemory` constructor composes SQLite repositories, ingestion, retrieval, maintenance, temporal and graph services. Expo's factory adapts an Expo SQLite connection; React's provider exposes an already-created instance. Setup must precede other operations. Neither wrapper supplies an autonomous enclosing agent. SRC-1, `packages/core/src/WikiMemory.ts`, `packages/expo/src/factory.ts`, `packages/react/src/WikiContext.tsx`.

> return new WikiMemory(createExpoAdapter(db), options);
> --- `packages/expo/src/factory.ts`

An ordinary local invocation begins when a host creates the adapter and provider, calls `setup()`, and submits an entity-scoped event. `write()` validates and clips the event, assigns an ID and timestamp, and persists it. In default auto mode it checks event/checkpoint differences, normally against 20 events, with an optional character-derived token threshold. It schedules a librarian promise after committing, rather than awaiting the completed extraction before returning. The librarian dispatch defaults to `legacy`; it reads 50 recent events and 100 recent facts, builds the prompt, asks the host text model for JSON, validates facts/tasks, deduplicates qualifying inferred titles, writes accepted rows in a transaction, then updates search and embeddings. Later `read()` returns a selected bundle, not an answer. The host decides whether and how to insert it into another model's context. These steps have distinct owners and failure boundaries: code schedules and admits, the model proposes content, SQLite executes storage, and the host owns persistence lifecycle and downstream inference. See [RT-RTE-event-librarian](#rt-rte-event-librarian), [RT-RTE-memory-read](#rt-rte-memory-read), [RT-BAP-memory-context](#rt-bap-memory-context).

> const strategy = deps.options.config?.librarian?.strategy ?? 'legacy';
> --- `packages/core/src/services/librarian/index.ts`

The chosen forcing cases are: deferred event writing versus auto work; direct mutable-fact writing versus model extraction; ingestion with failed chunks versus full replacement; and a valid zero-token retrieval budget versus a strict context cap. ScopeLab's advertisement/dispatch split is an additional effect-boundary check. These are source traces, not experiments. No target code was executed. All operation and behavioral benefit remain unobserved here. Newly inspected implementation coverage beyond the boundary's initial excerpts includes the full legacy librarian and strategy dispatcher, the ops orchestration, direct remember, bounded-call helper, core LLM-call wrapper, retrieval entry/packing/fallback/return paths, ingestion admission branches, ScopeLab dispatch and executor, tool injector/scopes, MCP search/server/client, outbox worker, native engine assembly, and benchmark answer/judge call sequence. Each remains SRC-1 at the frozen commit; no source identity was added.

### Controls are local, not an isolation envelope

The capability surface includes caller-supplied SQLite adapters, text/embedding providers, optional classifier and vector-ranker callbacks, configurable prompt templates, deterministic writes/imports, and a separate remote HTTP integration. Current grants differ by consumer. Core takes the caller's entity IDs and adapter; it does not identify an authenticated user in the inspected API entry. ScopeLab uses a fixed `scopelab-user` entity and a supplied enabled-scope list. MCP forwards a bearer credential to SynapseTree. These are not interchangeable security boundaries. No production sandbox, provider isolation or external authorization behavior is established. SRC-1, `packages/core/src/WikiMemory.ts`, `packages/core/src/types.ts`, `apps/scopelab/src/lib/memory/wiki-service.ts`, `packages/mcp-server/src/client.ts`.

Core transaction serialization wraps the instance's adapter. JobManager holds JavaScript maps/sets for maintenance and ingest coordination; these are not a distributed lease service. The `upsertGraph` route deliberately accepts a host-owned transaction and does no commit, rollback or post-commit embedding. Its host must propagate failures and later synchronize search. This alternate path prevents promoting the instance's internal transaction wrapper into an all-writers or all-processes guarantee. SRC-1, `packages/core/src/WikiMemory.ts`, `packages/core/src/services/JobManager.ts`; [RT-RTE-direct-admission](#rt-rte-direct-admission).

> this.db = withSerializedTransactions(db);
> --- `packages/core/src/WikiMemory.ts`

> This method neither commits nor rolls back the caller's transaction.
> --- `packages/core/src/WikiMemory.ts`

Load-bearing guarantee assessment:

| Proposed guarantee | Owner/enforcement and strength | Covered paths, alternatives and external contract | Separate conclusions |
|---|---|---|---|
| Deferred writes do not launch automatic librarian/heal work | WriteService's early return; invariant of that branch | `write()` with `config.maintenance === 'deferred'`; explicit maintenance, ingestion and direct writes remain callable. SQLite adapter must implement its write contract. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Read token budget strictly bounds the entire model context | No such enforcement; best effort fact packing only | Valid zero budget still retains the top fact's title/tags after trimming body; tasks/events are assembled separately; host history and formatting are external to packing. | implementation conclusion status: wired; operation conclusion status: uninspected |
| ScopeLab executes only advertised, scope-eligible function calls | `chatWithMemory` membership and scope checks before `executeTool`; policy enforced in that dispatch | First returned function call only; direct exported executor calls are outside this check, and provider-native built-ins are advertised by a different injector branch. Provider compliance with instructions is not code enforcement. | implementation conclusion status: wired; operation conclusion status: uninspected |
| All knowledge changes require human review | Not a universal shipped gate; no claimed guarantee across these paths | Model extraction and `remember()` persist without per-content human approval. `promoteDraft()` checks a live draft and nonempty reviewer string, not identity authentication. Host may add approval externally. | implementation conclusion status: wired; operation conclusion status: uninspected |

The budget row describes the implemented approximation and its counterexample, not a demonstrated runtime overrun. Source input validation admits finite budgets greater than or equal to zero; the consumer always initializes its kept list with the top item. A supported public call can therefore reach that branch whenever retrieval yields a fact. Missing fixture execution does not make this architecture indeterminate. See [RT-RTE-memory-read](#rt-rte-memory-read).

### Other material loops and limits

The opt-in ops librarian extracts from events after a watermark without existing facts in the extraction prompt, gates candidates against neighbors, asks a resolver only for ambiguous ones, applies results transactionally, and refreshes indexes/vectors. This is a second admission policy, not merely another name for legacy extraction. A budget stop before application discards diagnostics and returns without admission. [RT-RTE-ops-librarian](#rt-rte-ops-librarian) records the inspected orchestration; detailed resolver validity and semantic revision quality remain for specialist inspection.

Knowledge/instruction changes can also arrive through deterministic graph writes, imports, temporal replacement, draft promotion and ontology-manifest updates. Configured prompts and per-call overrides alter the guidance supplied to extraction/maintenance; they do not modify model parameters. A manual librarian override does not persist into subsequent auto runs. There is no inspected production code-change proposal/installation loop in these runtime paths; this does not assert repository-wide absence of development machinery. Memory revision semantics, heal's detailed criticisms, and any theory-builder classification are left to specialist evidence rather than inferred from method names. SRC-1, `packages/core/src/WikiMemory.ts`; [RT-RTE-direct-admission](#rt-rte-direct-admission), [RT-RTE-import-admission](#rt-rte-import-admission).

`runPendingMaintenance()` is the explicit host scheduling entry. Its source constructs a usage meter/deadline and awaits librarian/heal/reembed work. Its token budget meters generation only, not embedding; a deadline is checked between units, not a provider cancellation guarantee. Bounded batching handles parse/truncation-shaped failures through splitting, and can escalate singleton truncation failures to prompts with reduced context. It may skip terminal failures or return unattempted work after budget exhaustion. It is not a guarantee of eventual successful model output. SRC-1, `packages/core/src/services/MaintenanceScheduler.ts`, `packages/core/src/services/BoundedLlmCall.ts`, `packages/core/src/utils/llmCall.ts`.

> The token budget meters `generateText` calls
>    * only; embeddings are never metered.
> --- `packages/core/src/services/MaintenanceScheduler.ts`

ScopeLab completes a shipped model-consumption loop, but its memory constructor passes only config, omitting the required provider supplied by WikiDemo. Its `persist()` looks for `.adapter`, whereas inspected `WikiMemory` stores `.db`. These mismatches prevent treating ScopeLab as demonstrated end-to-end persistent operation. WikiDemo supplies an actual Anthropic or OpenAI-compatible provider before setup; its UI thresholds are 5/20 rather than core defaults. Neither is supplied execution evidence. SRC-1, `apps/scopelab/src/lib/memory/wiki-service.ts`, `packages/core/src/WikiMemory.ts`, `apps/wiki-demo/src/App.tsx`; [RT-RTE-scopelab-chat](#rt-rte-scopelab-chat).

The benchmark reopens the ingestion database, retrieves a bundle, excludes events/tasks from formatted answer context, calls an answer provider and a separate judge, and records a parsed verdict. It is a bounded evaluation mode, not the deployed app's answer oracle. No stored-result aggregate is adopted as empirical support here. [RT-RTE-benchmark-answer](#rt-rte-benchmark-answer).

The MCP integration owns tool parsing and HTTP request construction, not local-core execution. Outbox synchronization delegates effects to a caller's `mapEvent` inside Prisma transactions, then acknowledges local rows, allowing replay after a crash between external commit and local acknowledgement. Native GraphRAG is a separate returning computation with connection-owned and transaction-owned entry paths, not a second LLM orchestrator. [RT-RTE-remote-tools](#rt-rte-remote-tools), [RT-RTE-outbox-sync](#rt-rte-outbox-sync), [RT-RTE-native-traversal](#rt-rte-native-traversal).

## Shared records

### Components

#### RT-CMP-llm-provider
Label: Core text-generation provider

Source-native identity: `LLMProvider.generateText` or preferred optional `generateTextWithUsage`. Representational form: distributed-parametric model behind a symbolic callback interface; weights and provider state reside outside core SQLite. Exact model/version is not pinned by the interface. No inspected core call updates parameters; provider internals and changes during operation remain uninspected. A host callback or mutable endpoint can resolve to another model. Used for extraction/maintenance, not automatically for answering user questions. SRC-1, `packages/core/src/types.ts`, `packages/core/src/utils/llmCall.ts`.

> if (typeof provider.generateTextWithUsage === 'function') {
> --- `packages/core/src/utils/llmCall.ts`

#### RT-CMP-embed-provider
Label: Optional embedding provider

Source-native identity: `LLMProvider.embed`. Representational form: distributed-parametric encoder producing dense numerical arrays; external parameter storage, with derived vectors in local fact storage. Exact encoder version is not fixed by the callback contract. Inspected calls request embeddings rather than weight updates; internal parameter mutation is uninspected. A mutable host/provider endpoint can substitute an encoder; the interface requests stable dimensions, which is not an immutable model identity. SRC-1, `packages/core/src/types.ts`, `packages/core/src/services/RememberService.ts`.

> embed?: (text: string) => Promise<number[]>;
> --- `packages/core/src/types.ts`

#### RT-CMP-gemini-flash
Label: ScopeLab conversational model

Source-native identity: `gemini-2.0-flash:generateContent` URL. Representational form: distributed-parametric remote model; parameter storage external. Alias is explicit but not an immutable weights revision. No weight-changing request appears in the inspected caller; remote mutation is uninspected and the endpoint may resolve differently over time. It chooses text or a function call and supplies a follow-up answer. SRC-1, `apps/scopelab/src/lib/llm/function-caller.ts`.

> 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
> --- `apps/scopelab/src/lib/llm/function-caller.ts`

#### RT-CMP-answer-provider
Label: Benchmark answer model

Source-native identity: `ctx.answerProvider`. Representational form: distributed-parametric generation behind an instrumented provider; remote weight storage. Configured endpoint/model identity is recorded by the driver, not an exact immutable model revision. Calls do not request training; internal changes are uninspected and mutable endpoint substitution remains possible. Distinct role from the ingestion and judge providers even when deployments choose the same model. SRC-1, `packages/benchmarks/src/longmemeval/run.ts`.

> const answerText = await ctx.answerProvider.generateText(answerPrompt);
> --- `packages/benchmarks/src/longmemeval/run.ts`

#### RT-CMP-judge-provider
Label: Benchmark judge model

Source-native identity: `ctx.judgeProvider`. Representational form: distributed-parametric remote generation; storage outside the repository. Exact weights unpinned; no parameter update requested in inspected calls; internal mutation uninspected; a mutable endpoint can change the resolved model. Provides a verdict string, which code parses, not an independent guarantee of correctness. SRC-1, `packages/benchmarks/src/longmemeval/run.ts`.

> const judgeOutput = await ctx.judgeProvider.generateText(judgePrompt);
> --- `packages/benchmarks/src/longmemeval/run.ts`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-event-librarian
Label: Event write to legacy librarian admission

Owner/endpoints: host invokes `WikiMemory.write(entityId,event)`; WriteService persists an event and code schedules maintenance; legacy model proposes facts/tasks; code validates, deduplicates and commits. Event IDs and generated fact/task IDs differ; entity ID scopes the work. State includes event log, checkpoint, recent facts and post-commit search/embedding state. Guidance is the configured/per-call librarian prompt and ontology context. Open conversational accumulation is the operating mode; no expected-answer oracle is supplied. Human contribution is initial content/configuration, not a demonstrated per-fact decision or veto. Software can reject malformed candidates; DB errors roll back the transaction. Later forget/supersede APIs afford recovery, not an automatic semantic rollback.

- Immediate return: `write()` resolves after persistence and launching background work, not after completed model admission; `drain()` awaits tracked jobs with all-settled handling.
- Later read-back: committed inferred facts and tasks can enter later reads; recent facts also enter a subsequent legacy librarian prompt.
- Delegated visibility: provider receives constructed prompts, not the whole database; embeddings are stripped from prompt facts.
- Selection predicate: auto event/checkpoint threshold or optional summary-character token estimate; legacy reads 50 events and 100 facts and rejects fuzzy-title duplicates among inferred facts.
- Invalidation or expiry: failures restore the auto checkpoint for retry; explicit retention/deletion APIs exist; the selected legacy pass is not itself a universal expiry mechanism.
- Activation or effect: validated rows are admitted without mandatory human review, followed by index sync, embeddings and cache eviction. Changed downstream behavior is unobserved.
- Evidence limits: implementation trace only; legacy's bounded recent window does not establish full-event-log coverage or correct extraction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/WriteService.ts`, `packages/core/src/services/librarian/legacy.ts`, `packages/core/src/services/MaintenanceService.ts`.

> if (deferred) {
>       await this.eventRepo.add(newEvent);
>       return;
>     }
> --- `packages/core/src/services/WriteService.ts`

> const events = await deps.eventRepo.getRecent(entityId, 50);
>     const currentFactsRows = await deps.entryRepo.findRecentByEntityId(entityId, 100);
> --- `packages/core/src/services/librarian/legacy.ts`

> const valid = validateFact(raw);
> --- `packages/core/src/services/librarian/legacy.ts`

#### RT-RTE-ops-librarian
Label: Opt-in gated operation admission

Owner/endpoints: configured `ops` strategy receives entity, trigger, prompt override and optional meter. It selects events, calls extraction, gates candidates, resolves ambiguous candidates, and applies operations in a transaction. Code decides which candidates reach the resolver; model-generated operations and code application jointly govern admission. The inspected orchestrator passes rejected/failed sets to application; detailed veto rules in those helpers are not established here. No per-content human approval or expected-answer oracle appears in this orchestration. Mode is ongoing maintenance over event batches, not a fixed evaluation curriculum. Guidance and proposed operations shape retained facts/tasks/ontology; rollback depends on the application transaction, and future memory APIs afford recovery.

- Immediate return: result with processed-through cursor and facts-written count, or early empty/budget-stop result.
- Later read-back: admitted facts enter retrieval and later neighbor searches; watermark determines subsequent event batches.
- Delegated visibility: extraction gets the selected event batch; only ambiguous gated candidates are passed to resolution.
- Selection predicate: `config.librarian.strategy` selects ops; watermark batch selection and neighbor gate precede resolution.
- Invalidation or expiry: budget-stop returns before application; successful pass returns newest batch event cursor for watermark advancement. Detailed expiry remains outside this orchestration inspection.
- Activation or effect: applyOps writes changes, then syncs search, stores/recomputes vectors and evicts cache; semantic correctness and behavioral activation unobserved.
- Evidence limits: ops orchestration inspected, not a complete audit of gate, resolver and application internals; operation labels alone do not establish sound revision or formulated criticism.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/librarian/index.ts`, `packages/core/src/services/librarian/ops/index.ts`, `packages/core/src/services/MaintenanceService.ts`.

> const res = await runResolve(deps, ctx, gated.filter((g) => g.decision.kind === 'ambiguous'));
> --- `packages/core/src/services/librarian/ops/index.ts`

#### RT-RTE-document-ingest
Label: Document extraction with partial admission

Owner/endpoints: caller supplies entity, sourceRef/hash and document text; code normalizes identifiers, locks hash/sourceRef, chunks, calls provider per chunk, parses and validates candidates, then admits. Mode is open document ingestion; caller controls content and guidance overrides, model proposes facts, code validates/adopts; no external expected-answer oracle or mandatory human veto is in the inspected route. Complete success replaces source-derived content transactionally; partial success appends deduplicated successful facts without source ownership update or supersession. Thus partial success must not be interpreted as complete replacement. Total chunk failure throws before persistence. Restoring/retrying source ingestion is host-controlled recovery; post-commit embedding failure is a separate boundary from DB admission.

- Immediate return: chunk counts, truncation flag and optional parse failures, or typed total-failure/duplicate exceptions; duplicate skip may return before model work.
- Later read-back: successful full or partial facts are indexed/embedded for later retrieval; source state tracks completed ingestion differently from partial append.
- Delegated visibility: each extraction sees its constructed chunk prompt and ontology context; concurrency is bounded by the sanitized configured chunk count.
- Selection predicate: caller-specified document and chunking; valid facts survive parsing/validation; duplicate-hash options control precheck behavior.
- Invalidation or expiry: full success supersedes prior source facts; partial success preserves them. Caller can retry failures or invoke deletion.
- Activation or effect: SQLite admission followed by diagnostics, index refresh, embedding and cache eviction; no downstream answer benefit established.
- Evidence limits: inspected full/partial branches and early returns; fact-level truth and chunk coverage under real providers unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/IngestionService.ts`.

> if (failedChunks === chunks.length) {
>         throw new WikiIngestEmptyError({
>           parseFailures: failures,
>           sourceRef,
>           chunks: chunks.length,
>         });
>       }
> --- `packages/core/src/services/IngestionService.ts`

> return await this.appendPartialFacts(entityId, sourceRef, flat, tx, diagBuffer, factLedger);
> --- `packages/core/src/services/IngestionService.ts`

#### RT-RTE-direct-admission
Label: Caller-directed knowledge and guidance admission

Owner/endpoints: host invokes `remember`, `upsertGraph`, manifest setters or metadata/draft APIs. Proposed content originates with that caller, whose human/software identity is unresolved by the API. Code checks input and applicable ontology/ownership conditions; it does not require a text-model proposal. In open API mode the caller decides changes; software can reject invalid inputs. There is no expected-answer oracle or universal per-content human review. Retained outputs are facts/graph/manifest or lifecycle/trust metadata, not revised model weights. Configured prompt strings and per-call overrides supply runtime guidance; persistent configuration belongs to the host. Recovery is explicit forget/supersede/import or transaction rollback, not a universal undo command.

- Immediate return: remember returns the stored row; graph upsert returns counts; manifest batch returns written/skipped entities; other APIs have their own void/status results.
- Later read-back: retained knowledge can reach reads; manifests guide later normalization/prompt context. Per-call prompt overrides do not become persistent auto-run instructions.
- Delegated visibility: remember invokes embedding when configured, not text extraction; graph writes leave embeddings to later maintenance.
- Selection predicate: caller-supplied entity/content; remember normalizes input and validates nonnull ontology type; manifest batches validate invariants before transaction.
- Invalidation or expiry: manifest updates invalidate cache; temporal replacement preserves explicit history; graph writes require host post-commit search synchronization.
- Activation or effect: deterministic admission bypasses extraction without bypassing every data constraint. Draft promotion requires a live draft and nonempty reviewer string, not proof of a human identity.
- Evidence limits: remember body and public graph/manifest/promotion implementations inspected; full ownership/ontology helper internals are not audited here. No all-path authorization or strict ontology guarantee is inferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/RememberService.ts`, `packages/core/src/WikiMemory.ts`.

> await this.entryRepo.upsert(fact, tx);
> --- `packages/core/src/services/RememberService.ts`

> if (typeof by !== 'string' || by.trim().length === 0) {
>       throw new TypeError('promoteDraft requires reviewer.by to be a non-empty string.');
>     }
> --- `packages/core/src/WikiMemory.ts`

#### RT-RTE-import-admission
Label: Dump replacement or merge admission

Owner/endpoints: caller supplies a MemoryDump to importDump; code locks affected entities and invokes a transaction per entity. Caller proposes/adopts the dump; software enforces import rules. Human identity and any upstream review are unresolved; no answer oracle. Default mode is replacement, optional merge changes behavior. Guidance here is symbolic API flags and imported content, not a model instruction. Imports can restore backups, but multi-entity import is not shown as one global atomic transaction.

- Immediate return: void completion or rejection; locks released in finally.
- Later read-back: imported facts, tasks, edges and optional summary remain for later API consumption.
- Delegated visibility: inapplicable — inspected entry does not delegate import selection to a model.
- Selection predicate: dump entity keys and merge flag, default false.
- Invalidation or expiry: replacement soft-deletes live facts/tasks, removes edges and clears checkpoints within each entity transaction; imported summary replaces or clears the previous one according to merge.
- Activation or effect: caller-controlled replacement/merge, with downstream behavior depending on later consumers.
- Evidence limits: import entry and replacement transaction prelude inspected; detailed per-field conversion and postprocessing remain uninspected, preventing a universal import-validation claim.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/ImportExportService.ts`.

> for (const [entityId, bundle] of Object.entries(dump.entities)) {
>         await this.doImportEntity(entityId, bundle, merge);
>       }
> --- `packages/core/src/services/ImportExportService.ts`

#### RT-RTE-memory-read
Label: Selected memory bundle return

Owner/endpoints: host calls read for one or multiple entity IDs and a query; code selects facts via semantic/hybrid/keyword or empty-query recency paths, applies optional fact budget, then appends tasks/events. Optional ranker callbacks are another selection executor, not an authorization principal. Code owns admission into the returned bundle; host owns insertion into model context.

- Immediate return: facts, pending tasks, recent events, empty edges array and conditional metadata/scores.
- Later read-back: this is the read-back of retained material; access tracking also updates fact metadata on nonempty-query reads with results.
- Delegated visibility: configured embed callback receives query text; host ranker support exists, with detailed custom-ranker behavior not fully audited here.
- Selection predicate: entity list, query, result limit, draft/temporal filtering options, ranking options, and optional budget. Empty query uses recency; zero maxResults skips fact work but still fetches tasks/events.
- Invalidation or expiry: read-time liveness and optional draft filtering affect selection; these do not delete stored content. Retained data may later be forgotten or superseded through other APIs.
- Activation or effect: delivers a bundle, not a model answer or proof of reliance. Fact packing preferentially keeps top-ranked text and greedily packs others; it can truncate body while retaining title/tags.
- Evidence limits: entry, packing, keyword fallback and final assembly inspected; detailed native/custom ranker branches not exhaustively audited. Token estimate is not actual model tokenization and not a hard total-context ceiling.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/core/src/services/RetrievalService.ts`, `packages/core/src/utils/budget.ts`.

> if (tokenBudget !== undefined && !(typeof tokenBudget === 'number' && Number.isFinite(tokenBudget) && tokenBudget >= 0)) {
> --- `packages/core/src/services/RetrievalService.ts`

> const kept: Array<{ rank: number; item: T }> = [{ rank: 0, item: top }];
> --- `packages/core/src/utils/budget.ts`

> const bundle: MemoryBundle = { facts, tasks, events: events.reverse(), edges: [] };
> --- `packages/core/src/services/RetrievalService.ts`

#### RT-RTE-scopelab-chat
Label: ScopeLab memory-to-tool conversation

Owner/endpoints: user message enters chatWithMemory; wrapper writes it as an event, retrieves up to five facts, formats title/body/tags, injects memory plus history into Gemini, optionally dispatches one function call and asks for a final answer. Principal grants are supplied enabledScopes plus always-on core. The model proposes a tool call; code decides executability; the registered executor only implements search_memory. This is open conversation, without an expected-answer oracle. No additional per-call human approval is implemented in the inspected branch.

- Immediate return: response text, with optional executed tool call/arguments/result.
- Later read-back: user message, assistant text or abbreviated tool-result event is written for future extraction/retrieval; actual durability is unresolved in this wrapper.
- Delegated visibility: Gemini gets formatted selected memory, supplied history and user message; follow-up gets function response and original messages. This is not a separate subagent context.
- Selection predicate: authorizedTools filters advertisement; dispatcher also requires matching advertised name, truthy scope, and always-on or enabled scope. Only first response part/function call is handled.
- Invalidation or expiry: inapplicable — chat caller implements no context trimming, expiry or reload policy beyond memory retrieval; supplied history is forwarded.
- Activation or effect: a recognized authorized search_memory call reaches the injected wiki context reader; unknown handlers throw. Memory directives are discouraged by text, not cryptographically or semantically excluded.
- Evidence limits: wrapper omits core llmProvider and persist looks for an unavailable adapter property; successful extraction/persistence is not established. Direct executeTool callers are not guarded by chatWithMemory; provider-native built-ins have separate provider execution semantics.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `apps/scopelab/src/lib/llm/function-caller.ts`, `apps/scopelab/src/lib/memory/wiki-service.ts`, `apps/scopelab/src/lib/llm/tool-executor.ts`, `packages/core-llm-tools/src/injector.ts`, `packages/core-llm-tools/src/scopes.ts`.

> if (!advertisedNames.has(t.name)) return false
>       if (!t.scope) return false
>       return isAuthorizedScope(t.scope) || enabledScopes.includes(t.scope)
> --- `apps/scopelab/src/lib/llm/function-caller.ts`

> const adapter = (this.wiki as any).adapter
> --- `apps/scopelab/src/lib/memory/wiki-service.ts`

#### RT-RTE-benchmark-answer
Label: Reopened memory answer and judge pipeline

Owner/endpoints: benchmark driver ingests a question's evidence, opens the resulting DB file, sets up WikiMemory with embed and a no-op text generator, reads question context, asks an answer model, then asks a judge and records parsed correctness. This is a bounded question-evaluation mode. The supplied question object and buildJudgePrompt supply reference context for judging; exact expected-answer content and verdict prompt wording are not established by the inspected call sequence. Judge model proposes verdict; parseVerdict makes the recorded decision. Human per-answer veto is not present in this sequence. No product/knowledge changes are admitted by the verdict itself.

- Immediate return: question ID/type, correctness, context-token estimate, timings, cache flag, judge text and answer.
- Later read-back: reopened ingest database supplies facts; result record retention/aggregation is separate from core knowledge admission.
- Delegated visibility: answer provider sees formatted memory and question prompt; judge sees its separately built question/answer prompt, not automatically the answer model's full context.
- Selection predicate: question and read options, with formatted context explicitly excluding tasks/events.
- Invalidation or expiry: database handle closes in finally; cache validity and ingestion reuse are not audited here.
- Activation or effect: source wires retained memory to model input and parsed verdict; no causal attribution to a memory mechanism or measured accuracy adopted here.
- Evidence limits: driver implementation only; oracle prompt internals and stored results not inspected; no target evaluation executed.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/benchmarks/src/longmemeval/run.ts`.

> const context = formatContext(bundle, { maxEvents: 0, maxTasks: 0 });
> --- `packages/benchmarks/src/longmemeval/run.ts`

#### RT-RTE-remote-tools
Label: MCP tool to SynapseTree HTTP operation

Owner/endpoints: MCP caller invokes registered tool; server validates Zod input, handler selects namespace and HTTP operation, client constructs authenticated request; remote SynapseTree owns execution/persistence. Search forwards query, namespace, limit and optional draft/asOf controls, returning remote data. Other registered tools share server wrapping; this record does not infer local-core behavior for their remote consumers.

- Immediate return: JSON text content, or isError text on caught exception.
- Later read-back: uninspected — remote retained-state consumer is outside frozen source; search response alone does not reveal remote write/admission internals.
- Delegated visibility: HTTP service receives request body and bearer authorization for authenticated operations.
- Selection predicate: tool registration and Zod schema; search limit 1–100 and query maximum 4096; namespace resolution before request.
- Invalidation or expiry: timeout abort, bounded retries and per-operation idempotency-key support govern requests, not remote data expiry.
- Activation or effect: remote requests, not local SQLite calls; retries reuse the generated request key within one call when operation supports it.
- Evidence limits: source wires transport; remote authorization, model use, isolation and persistence remain uninspected. Registration/auth-token minting are deliberately single-attempt alternatives, not universally retried.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/mcp-server/src/server.ts`, `packages/mcp-server/src/tools/memory-search.ts`, `packages/mcp-server/src/client.ts`.

> if (authenticated && this.apiKey) headers.Authorization = `Bearer ${this.apiKey}`;
> --- `packages/mcp-server/src/client.ts`

#### RT-RTE-outbox-sync
Label: Local outbox to Prisma effects

Owner/endpoints: timer or explicit caller triggers syncBatch; worker reads pending rows, calls mapEvent inside Prisma transaction, then acknowledges processed IDs in WikiMemory. Caller-supplied mapping owns external effects. No LLM decision is in this worker.

- Immediate return: void completion; already-running calls return without another batch.
- Later read-back: unacknowledged rows are fetched again; mapped external state may be consumed elsewhere, outside this worker's inspected evidence.
- Delegated visibility: mapEvent receives each event and external transaction handle.
- Selection predicate: oldest pending events, bounded batch; error callback can skip/acknowledge a failed event, otherwise halts preserving remaining order.
- Invalidation or expiry: processed rows are acknowledged after external transactions; crash gap can replay, so exactly-once effects require external idempotence.
- Activation or effect: external Prisma mutation determined by host callback, then local acknowledgement; no atomic cross-database commit established.
- Evidence limits: worker body inspected, not a deployed mapEvent or Prisma implementation; cross-worker concurrency/isolation not guaranteed by this instance's running flag.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `packages/prisma-outbox/src/PrismaOutboxWorker.ts`, `packages/core/src/WikiMemory.ts`.

> await this.config.prisma.$transaction(tx => this.config.mapEvent(event, tx));
>           processedIds.push(event.id);
> --- `packages/prisma-outbox/src/PrismaOutboxWorker.ts`

#### RT-RTE-native-traversal
Label: Native graph neighborhood computation

Owner/endpoints: host passes connection or existing transaction, traversal request and now_ms to GraphRagEngine. Symbolic Rust rules validate schema/request, walk, fetch induced edges, hydrate facts and remove edges whose endpoints did not hydrate. State is host SQLite; output is typed nodes/edges, not generated language.

- Immediate return: GraphNeighborhood or typed error.
- Later read-back: inapplicable — this computation reads existing graph state and does not itself accumulate new retained knowledge.
- Delegated visibility: inapplicable — inspected engine pipeline has no model delegation.
- Selection predicate: validated traversal request, entity/source IDs, graph walk and hydrated node membership.
- Invalidation or expiry: hydration drops soft-deleted nodes; connection entry ends its snapshot, while transaction entry leaves host transaction ownership unchanged.
- Activation or effect: returns selected graph DTO; downstream context construction and behavior outside this pipeline remain unobserved.
- Evidence limits: engine assembly inspected, not full walk/hydration/schema validation internals or runtime parity tests; no TypeScript/native semantic parity guarantee inferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `crates/graphrag-core/src/engine.rs`.

> self.run(tx, req, now_ms)
> --- `crates/graphrag-core/src/engine.rs:88-88`

### Claims

#### RT-CLM-longterm-memory
Label: Conversation and document memory claim

Claimed operation: SQLite-backed cross-platform long-term memory with fact extraction, semantic search and pruning. This is source doctrine/design; the inspected routes support implemented mechanisms, not demonstrated longevity, benefit or cross-platform reliability. SRC-1, `README.md`.

> Core LLM Wiki is a family of cross-platform TypeScript packages for long-term LLM memory, built on SQLite.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-memory-context
Label: Retrieved facts into ScopeLab model input

Consumer: Gemini conversation model. Channel: selected fact title/body/tags formatted as natural-language memory in a marked region of the first message; original system-role messages are mapped to user role in the request. Force: advisory contextual data with an explicit instruction not to follow embedded directives; not an enforced semantic exclusion. Horizon: later invocations can consume retained extracted facts, conditional on wrapper/provider/persistence issues being resolved. Escaping wrapper delimiters prevents the literal closing-marker route but cannot establish that a model ignores instructions in natural language. Delivery and compliance are distinct. SRC-1, `apps/scopelab/src/lib/llm/function-caller.ts`, `apps/scopelab/src/lib/memory/wiki-service.ts`; [RT-RTE-scopelab-chat](#rt-rte-scopelab-chat).

> .replaceAll('</retrieved_memory>', '<\\/retrieved_memory>')
> --- `apps/scopelab/src/lib/llm/function-caller.ts`

#### RT-BAP-prompt-guidance
Label: Host prompt configuration into maintenance

Consumer: core text provider. Channel: natural-language system/user prompts built from templates, overrides and selected state. Force: requested extraction/maintenance behavior, followed by symbolic candidate parsing and validation, not guaranteed model compliance. Horizon: construction-time config applies to later runs on the instance; manual promptOverride applies only to its call. Stored instructions are not shown rewriting their own templates. SRC-1, `packages/core/src/WikiMemory.ts`, `packages/core/src/services/librarian/legacy.ts`, `packages/core/src/utils/llmCall.ts`.

> const params = { systemPrompt: prompts.systemPrompt, userPrompt: prompts.userPrompt };
> --- `packages/core/src/utils/llmCall.ts`

## Annotations

none
