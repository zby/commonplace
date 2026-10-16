---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "browzy.ai runtime baseline: terminal and library answering, source compilation and retained-change admission at the frozen Git boundary."
run-id: AAS-2026-10-15-browzy-ai-0a823a13a7b6-01
reviewed-boundary: "56c253042041ee2f483a5e9b824174d746891cf4"
---

# browzy.ai runtime report

## Runtime account

### Work, entry and ordinary invocation

browzy ingests selected material, compiles local wiki articles and answers questions using retrieved articles. The shipped executable is `dist/cli/entry.js`; no-argument launch renders the Ink application, whereas arguments dispatch Commander init, ingest, compile, query, lint, status and search commands. The library entry is `dist/index.js`. These are different callers of the same engine, not one uniform conversational agent loop (SRC-1, `package.json`, `src/cli/entry.tsx`, `src/cli/commands/query.ts`).

> "bin": {
>     "browzy": "dist/cli/entry.js"
>   },
> --- `package.json`

The ordinary terminal invocation is a user question against a populated knowledge directory. `handleQuery` requires a provider, records the user message, creates a new QueryEngine, calls `prepare`, independently builds bounded conversation history, and streams through the configured provider. Retrieval searches SQLite, reloads Markdown, supplements sparse search from the index, ranks candidates and assembles context. No model decides the next tool or graph node: application code owns this progression; the model supplies answer text. The final answer is added to the session with the selected article slugs. Failure of streaming invokes a new non-streaming call, not continuation from a checkpoint. The library/one-shot CLI instead calls `query`, including its process-local result cache and optional output-file save. See [RT-RTE-answer-question](#rt-rte-answer-question) and [RT-RTE-library-query](#rt-rte-library-query).

The runtime receives question text, article text, schema preferences and, in the terminal, selected prior turns. The principal is the local user or library caller. Provider credentials authorize service calls, while local filesystem access uses the process's OS permissions. Slugs/source IDs label knowledge; session IDs label saved conversations. Neither is an authentication boundary. Models are remote or local inference components, not delegated workers with independent tools; their numerical internals are outside the source boundary ([RT-CMP-llm-provider](#rt-cmp-llm-provider)). Sources: SRC-1, `src/cli/app.tsx`, `src/core/query/engine.ts`, `src/core/llm/provider.ts`, `src/cli/hooks/useSession.ts`.

### Material forcing routes and limits

Three forcing comparisons qualify the ordinary account:

1. **Terminal versus library.** Terminal history reaches the provider only after `prepare` has calculated its budget without that history or the actual configured model ID. A new engine per question also discards its used-slug set. Library callers can request follow-up exclusions, but that is not the terminal's observed call shape. The terminal bypasses the answer cache. On streaming failure, the fallback omits the appended conversation-context system instruction, although it retains selected messages (SRC-1, `src/cli/app.tsx`, `src/core/query/engine.ts`).
2. **Short versus model-compiled sources.** Content shorter than 2,000 characters becomes a template article without model curation or schema/guidance interpretation. Longer content is truncated to 15,000 characters for the compiler call. Only the first 30 existing article names/titles are supplied, not their full bodies. A prompt asking to merge/preserve old material therefore does not establish that preservation. The compiled-source membership predicate can skip re-ingested sources retaining their ID; `/refresh` and `/rebuild` call the same incremental compiler, not a force-update implementation (SRC-1, `src/core/compile/compiler.ts`, `src/core/ingest/index.ts`, `src/cli/app.tsx`). See [RT-RTE-source-compilation](#rt-rte-source-compilation).
3. **Answer-derived draft versus session-derived wiki write.** The crystallizer writes only to drafts after model novelty judgment and parser gates; the digest path separately attempts a direct wiki write without those gates. Thus neither “all interaction-derived text becomes searchable knowledge” nor “all retained model text requires human approval” describes these paths (SRC-1, `src/core/query/crystallizer.ts`, `src/cli/app.tsx`). See [RT-RTE-insight-draft](#rt-rte-insight-draft) and [RT-RTE-session-digest](#rt-rte-session-digest).

This inspection additionally covers provider request bodies (Claude, OpenAI, OpenRouter and Ollama; chat and stream), direct image-provider admission through the ingest dispatcher, and the library-supplied provider interface. The inspected provider bodies contain text/multimodal requests, not a provider-native tool dispatcher. A custom library implementation of `LLMProvider` remains an external host contract, not proof of a permission policy. A scoped search of `src/` for `exec`, `spawn`, `tools:`, `tool_choice`, and `drafts` located clipboard/editor subprocesses and the draft writer. Those host subprocesses are not model-selected tool executions: the app invokes fixed clipboard commands and an editor executable. This bounds the account, not a complete security audit or proof that dependency/service code cannot execute actions (SRC-1, `src/core/llm/provider.ts`, `src/core/ingest/index.ts`, `src/cli/app.tsx`, `src/core/discovery/clipboard.ts`).

### Guarantees and enforcement coverage

| Guarantee and owner | Enforcement, strength and covered paths | Alternate path / external contract | Separate conclusions |
|---|---|---|---|
| Relevant context fits its budget; ContextBuilder/QueryEngine | Estimated-token checks in assembly; **best effort**, not a hard model-window invariant. | Assembly permits at least two articles before enforcing total budget; intro sections can exceed the per-article target. Terminal adds history after prepare. Requires actual tokenizer/model-window and provider acceptance contracts. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Article/output paths stay under the chosen base; FilesystemStorage | `safePath` lexical resolution, relative-path rejection and null-byte checks; **invariant** for those checks at that API boundary. | Drafts, session files and schema use separate joins/writes. No realpath/symlink isolation follows from the lexical guard; requires trustworthy directory layout and OS permissions. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Ollama endpoint is local; OllamaProvider | Constructor URL hostname allowlist covers both chat and stream; **invariant** for accepted hostname strings. | Other providers intentionally send remotely; injected providers bypass this constructor. Local hostname validation is not a guarantee of service privacy, redirect handling or sandbox isolation. Requires trustworthy local service/network stack. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Source instructions are not obeyed; compiler prompt owner | Untrusted-content delimiter/instruction; **policy**, not executable isolation. | Short sources bypass model compilation and retain source content directly. Query prompts later treat wiki content as primary truth. Requires model compliance; parser accepts article structure, not truth or instruction safety. | implementation conclusion status: wired; operation conclusion status: uninspected |

Sources: SRC-1, `src/core/retrieval/contextBuilder.ts`, `src/core/query/engine.ts`, `src/cli/app.tsx`, `src/core/storage/filesystem.ts`, `src/core/utils.ts`, `src/core/llm/provider.ts`, `src/core/compile/compiler.ts`, `src/core/prompts.ts`.

> if (totalTokens + blockTokens > budget && used.length >= MIN_ARTICLES) {
>         break; // Budget exceeded
>       }
> --- `src/core/retrieval/contextBuilder.ts`

> if (rel.startsWith('..') || rel.startsWith('..' + sep) || isAbsolute(rel)) {
>     throw new Error(`Path traversal blocked: ${filename}`);
>   }
> --- `src/core/utils.ts`

> if (parsed.hostname !== 'localhost' && parsed.hostname !== '127.0.0.1' && parsed.hostname !== '[::1]') {
>         throw new Error('Ollama baseUrl must be localhost. Remote Ollama endpoints are not supported.');
>       }
> --- `src/core/llm/provider.ts`

The capability surface is source fetching/parsing, provider calls and host-managed local writes/subprocesses. The current grant set is unavailable: no real credentials, knowledge directory or runtime configuration was supplied. The deployed isolation envelope is also unavailable; the code-level path and endpoint controls do not establish an OS sandbox. No inspected route admits arbitrary generated executable code into the shipped product or production machinery. This last statement concerns the described admission routes, not a repository-wide absence claim. Human schema editing is an instruction-change path ([RT-RTE-schema-change](#rt-rte-schema-change)); content compilation and digesting are separate knowledge-change paths. No test or target was executed, so activation, correctness, successful persistence, reliability and benefit remain unobserved.

### Evidence coverage added

All new inspection remains SRC-1 implementation at the boundary pin, with prompt text as doctrine/design. In addition to boundary-listed material, the runtime read the complete query history manager, query cache, query CLI command, provider adapter, digest and crystallizer; read material app ranges for query, digest, refresh, schema and rebuild; and inspected lexical path controls in utilities. Ranking internals, document processors, discovery implementations, linter repair behavior, demo consumers and dependency internals were not independently traced end to end here. Their detailed quality/security behavior remains uninspected, not absent. The boundary member supplies their inclusion and initial coverage; this member does not replace the specialists' retention/revision account.

## Shared records

### Components

#### RT-CMP-llm-provider
Label: LLMProvider inference services

Source-native identity: the `LLMProvider` chat/stream interface and its Claude, OpenAI, OpenRouter and Ollama implementations. Representational form: distributed-parametric model state behind service APIs; request/response transport is symbolic JSON containing natural-language content. Storage substrate: external provider or local Ollama model storage, not repository-owned weights. Parameters changing during operation: no update/training operation in inspected adapters; provider-side change remains uninspected. Exact version pinned: no immutable weight/version contract; dated Claude default is an API model name, while other defaults include `gpt-4o`, `anthropic/claude-sonnet-4`, and `llama3.2`. Mutable endpoint resolving to another model: possible through configuration/model switching or service alias resolution; actual service resolution is uninspected. SRC-1, `src/core/llm/provider.ts`, `src/cli/app.tsx`.

> model: this.config.model || 'gpt-4o',
> --- `src/core/llm/provider.ts:250-260`

### Operative objects

#### RT-OBJ-browzy-schema
Label: browzy.schema.md

Source-native identity: `browzy.schema.md` in the data directory. Representational form: natural-language preferences interpreted by the model; file existence and length gates are symbolic code rules. Storage substrate: local Markdown file, reloaded for compilation/query system-prompt assembly. This object changes instruction supply, not model parameters. SRC-1, `src/core/schema.ts`, `src/core/prompts.ts`.

> return content.slice(0, MAX_SCHEMA_CHARS);
> --- `src/core/schema.ts`

### Routes

#### RT-RTE-answer-question
Label: Terminal question answering

User question → application `handleQuery` → QueryEngine.prepare/ContextBuilder → provider.stream → session assistant message. Owner/next-step selector: application code; content synthesis: model. Context is wiki article blocks, user question, schema-bearing system prompt and filtered/truncated history. State includes current session, UI stream snapshot and freshly created engine; effects are service requests, answer display, session accumulation and conditional downstream draft generation. Operating mode: open user requests, not a bounded experiment. No expected-answer oracle. Retrieval ranking/confidence is code-scored coverage, not model correctness evaluation. SRC-1, `src/cli/app.tsx`, `src/core/query/engine.ts`, `src/core/retrieval/contextBuilder.ts`, `src/core/query/historyManager.ts`.

- Immediate return: streamed snapshots, then a final assistant message with selected source slugs; source list establishes context delivery, not actual citation use.
- Later read-back: bounded prior user/assistant messages reach later terminal calls; session files separately feed digest generation, not automatic restoration of full prior chat here.
- Delegated visibility: provider receives assembled context and history; no worker delegation in this route.
- Selection predicate: FTS top 20 candidates, index fallback if fewer than five loadable articles, ranking up to 15; history retains up to ten user/assistant turns with per-message and aggregate character targets.
- Invalidation or expiry: engine used-slug state lasts only this handler; history removes system messages and older/truncated text from provider input, leaving full session state reachable to host saving.
- Activation or effect: model answer is displayed; changed behavior due to selected articles/history remains unobserved.
- Evidence limits: source wiring only; no execution, token-window measurements or answer-grounding observations.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const prepared = engine.prepare(question, { format: outputFormatRef.current }); // #11: use ref
> --- `src/cli/app.tsx`

> const systemPrompt = prepared.systemPrompt + '\n\n' + CONVERSATION_CONTEXT_PROMPT;
> --- `src/cli/app.tsx`

The code-controlled context reduction discards older/long text rather than generating a retained compact summary. Original turns remain in host session memory/files, but the provider has no pointer-following tool to reload omitted text. This differs from a sub-agent frame: no isolated task agent returns a computed result. Streaming failure starts chat with the same messages but only `prepared.systemPrompt`; provider chat methods implement bounded retry for selected errors. Neither fallback nor retry proves successful recovery (SRC-1, `src/cli/app.tsx`, `src/core/query/historyManager.ts`, `src/core/llm/provider.ts`).

#### RT-RTE-library-query
Label: Library and one-shot query

Caller/Commander query → QueryEngine.query → optional cache return, otherwise retrieval → provider.chat → result/cache and optional output file. Code owns progression; model owns answer text. Context/state and selection largely share terminal preparation, but conversationHistory is used in budget calculation and is not actually sent as messages by `query`. `followUp` excludes previously used slugs only while an engine instance survives. Operating mode: open caller request; answer oracle: none. SRC-1, `src/core/query/engine.ts`, `src/cli/commands/query.ts`, `src/core/retrieval/queryCache.ts`.

- Immediate return: answer, source slugs, coverage confidence/gaps, token metadata and optional saved-output path; cache hit returns earlier result before schema loading or save handling.
- Later read-back: process-local cached answer reaches an identical keyed request; optional saved output is a file, with no automatic reinjection established in this route.
- Delegated visibility: provider receives only the newly assembled user prompt/system prompt on a cache miss; external library provider implementations are caller-controlled.
- Selection predicate: cache key is question, format and model string; misses use ContextBuilder; follow-ups skip cache and exclude used articles.
- Invalidation or expiry: cache has 30-minute TTL, 50-entry LRU limit and ingest-generation invalidation; key does not include dataDir, schema or conversation history.
- Activation or effect: cached result bypasses inference; cache misses request synthesis and optionally write output; grounded answer quality unobserved.
- Evidence limits: no run confirms cache isolation, output saves or benefit; shared singleton and omitted key inputs prevent assuming per-KB correctness.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const cached = queryCache.get(question, format, model);
>       if (cached) return cached as QueryResult;
> --- `src/core/query/engine.ts`

#### RT-RTE-source-compilation
Label: Source ingestion and compilation

Caller-selected URL/file → ingest processor → raw content/manifest and source database → incremental WikiCompiler → model or template → article files/database/backlinks/index. Human initiates source selection and may supply per-source guidance; processor/code admits raw material. Model proposes long-source articles; parser and slug handling decide structural acceptance; compiler writes without per-article human approval. Operating mode: open source admission in batches, not an improvement experiment. Answer oracle: none; source text is evidence input, not a reference correct answer. Guidance requests wiki synthesis, source citations, merging and contradiction handling; schema adds user preferences. Raw source, generated article text and derived indexes persist. SRC-1, `src/core/ingest/index.ts`, `src/core/compile/compiler.ts`.

- Immediate return: raw-source metadata from ingest; compile returns created/updated slug lists and concept-slug proposals, with progress callbacks.
- Later read-back: future compilation reads source manifest and existing articles; query reloads selected article files via SQLite/index candidates.
- Delegated visibility: compiler sends at most 15,000 raw characters, up to 30 existing slug/title entries, schema and optional guidance to provider; not full existing article bodies.
- Selection predicate: raw sources whose IDs are absent from existing article sources, first batchSize (default 20); fewer than 2,000 characters takes non-model template branch; longer sources run in groups of three.
- Invalidation or expiry: ingest invalidates answer cache; compiler membership skips already represented IDs. No rollback/version transaction spans file and DB writes; failures can leave partial state.
- Activation or effect: parser-accepted articles become local wiki files and FTS records; semantic correctness, preservation and later model reliance unobserved.
- Evidence limits: source wiring; neither schema compliance nor successful semantic merge follows from prompt instructions.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const newSources = sources.filter(s => !compiledSourceIds.has(s.id));
> --- `src/core/compile/compiler.ts`

> if (rawContent.length < 2000) {
>               const articles = this.createTemplateArticle(source, rawContent);
>               return { source, articles };
>             }
> --- `src/core/compile/compiler.ts`

> this.fs.writeArticle(article.slug, article.frontmatter, article.content);
> --- `src/core/compile/compiler.ts:123-123`

Rejection/recovery: malformed article blocks lacking slug/title or empty sanitized slug are skipped; Promise.allSettled allows other sources to proceed. Failed pre-index entries are removed regardless of success. There is no content-truth gate or human veto between parsing and persistence in this function. Used-slug collision handling renames a proposal before the existing-article check; therefore the prompt's UPDATE instruction is not an overwrite guarantee. `/refresh` re-ingests stale sources and calls this compiler; preserving IDs can defeat intended recompilation. `/rebuild` also supplies no force flag. Knowledge revision details remain for memory analysis (SRC-1, `src/core/compile/compiler.ts`, `src/core/ingest/index.ts`, `src/cli/app.tsx`).

#### RT-RTE-insight-draft
Label: Insight crystallization to drafts

Terminal answer using at least two articles → host reloads up to five sources → crystallize model call → NONE or parsed article → drafts file. Host controls trigger and parser gates; model proposes and judges novelty against truncated source content. User does not approve each draft. Operating mode: automatic post-answer proposal within an open session; no expected-answer oracle. Novelty prompt is guidance, not independent validation. Proposal persists as derived Markdown with question/source slugs; model reasoning/criticisms are not separately retained by this function. SRC-1, `src/cli/app.tsx`, `src/core/query/crystallizer.ts`, `src/core/prompts.ts`.

- Immediate return: saved flag with optional slug/title; terminal reports insight drafted asynchronously.
- Later read-back: uninspected — draft file persists, but no automatic draft-to-query consumer was found in the scoped source search; retrieval inspected here reads wiki files.
- Delegated visibility: question, first 3,000 answer characters, up to five source articles with 2,000 characters each reach the provider.
- Selection predicate: at least two source IDs and two loadable source contents; session ref suppresses additional successful drafts; NONE, malformed markers, missing metadata or body under 50 characters reject.
- Invalidation or expiry: unsuccessful/error paths reset session gate for retry; successful draft suppresses further session drafts. No rollback/expiry protocol in crystallize.
- Activation or effect: file write to drafts only, not wiki/index admission or demonstrated later behavior change.
- Evidence limits: model novelty judgment is not a reference oracle; truncated comparisons cannot establish corpus-wide novelty or truth.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Write to drafts/ directory (NOT wiki/)
>   const draftsDir = join(dataDir, 'drafts');
> --- `src/core/query/crystallizer.ts`

#### RT-RTE-session-digest
Label: Prior-session digest admission

App startup/provider availability → load latest saved session and matching metadata → model summarizes → digest text/meta write and optional wiki article. Host owns eligibility and persistence; model authors the summary. No per-digest human admission/veto or reference-answer oracle. Mode: automatic background summary, not experiment. Guidance requests topics, insights and unresolved work, at most 100 words; provider max output 200 tokens. It retains a summary, not a demonstrated correction of a system method. SRC-1, `src/cli/app.tsx`, `src/cli/hooks/useSession.ts`, `src/core/query/digest.ts`, `src/core/prompts.ts`.

- Immediate return: background completion writes digest and updates metadata; startup is not blocked.
- Later read-back: startup loads digest path for banner display; optional wiki write has no SQLite/index update here, so immediate query retrieval of it is not established by this writer alone.
- Delegated visibility: prior non-system messages, full user questions and assistant answers cut to 200 characters, reach digest provider; user-visible system notices are omitted.
- Selection predicate: matching latest-session ID, no existing digest, provider available and at least three user messages.
- Invalidation or expiry: saved session JSON retention prunes to newest 50 by mtime; digest text has no matching pruning in inspected hook. Daily session article slug can overwrite on another write; errors are swallowed and wiki write is optional.
- Activation or effect: retained digest/display and attempted wiki insertion; successful read-back and impact on answers unobserved.
- Evidence limits: no observed session corpus; ESM dynamic require in the callback is source text, not demonstrated successful runtime module resolution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const userMessages = lastSession.messages.filter(m => m.role === 'user');
>         if (userMessages.length >= 3) {
> --- `src/cli/app.tsx`

#### RT-RTE-schema-change
Label: Owner schema instruction change

Owner edits the schema file (CLI provides path/default/reset) → readSchema → compiler/query system-prompt builders. Human proposes and admits text by filesystem edit; code checks existence, at least one non-comment nonblank line and truncates to 4,000 characters. No semantic approval gate, experiment or answer oracle. Recovery: edit/replace file or `/schema reset`; not a revision history. Compiles read once per pass; uncached queries reload. Short-source template compilation does not consume schema, and library cached answers can return before reloading it. SRC-1, `src/core/schema.ts`, `src/core/prompts.ts`, `src/core/query/engine.ts`, `src/core/compile/compiler.ts`, `src/cli/app.tsx`.

- Immediate return: CLI shows path/current text or reset notification; subsequent prompt construction includes admitted text.
- Later read-back: later uncached query and model compilation calls reload schema and prepend it to system instructions.
- Delegated visibility: provider receives schema as system instruction content; owner editing does not grant model tools.
- Selection predicate: existing readable file with some non-comment content; whole prefix is returned, not only filtered user lines.
- Invalidation or expiry: owner reset/replacement, file-read failure or prefix limit; no answer-cache invalidation on schema edit in this route.
- Activation or effect: changes model instruction supply; model compliance or improved domain behavior not observed.
- Evidence limits: code establishes instruction delivery and owner editing affordance, not successful customization or self-directed method revision.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return `# User Schema\n\nThe knowledge base owner has defined these preferences. Follow them when answering:\n\n${schema}\n\n---\n\n${QUERY_SYSTEM_PROMPT}`;
> --- `src/core/prompts.ts`

### Claims

#### RT-CLM-wiki-grounding
Label: Wiki-grounded answer policy

Claimed operation: query prompt directs articles to be primary truth, factual provenance to be explicit and unsupported training knowledge to be distinguished. This is natural-language doctrine/design delivered through the answer routes, not an enforced grounding oracle. SRC-1, `src/core/prompts.ts`.

> - **Trace provenance.** Every factual claim should be traceable to either a specific wiki article or clearly flagged as your own knowledge. Never blend them silently.`
> --- `src/core/prompts.ts`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-schema-instruction
Label: Owner preferences to model instructions

Consumer: compiler/query inference model. Channel: schema text prepended to system prompt. Force: requested behavioral preference interpreted by model, not executable validation or tool authorization. Horizon: later invocations across sessions while the file remains; compiler reads once per pass; library cache can bypass fresh consumption. Evidence: [RT-OBJ-browzy-schema](#rt-obj-browzy-schema), [RT-RTE-schema-change](#rt-rte-schema-change); SRC-1, `src/core/schema.ts`, `src/core/prompts.ts`, `src/core/query/engine.ts`.

#### RT-BAP-wiki-context
Label: Wiki text to answer context

Consumer: answer model, and then the human reader of the answer. Channel: retrieved Markdown serialized into user-prompt article blocks. Force: knowledge/context under a system policy treating articles as primary truth, not code execution or a hard correctness constraint. Horizon: future requests selecting those articles; subset selection, budget omissions and cached-answer bypass qualify reach. Evidence: [RT-RTE-answer-question](#rt-rte-answer-question), [RT-RTE-library-query](#rt-rte-library-query), [RT-CLM-wiki-grounding](#rt-clm-wiki-grounding); SRC-1, `src/core/retrieval/contextBuilder.ts`, `src/core/query/engine.ts`, `src/core/prompts.ts`.

## Annotations

none
