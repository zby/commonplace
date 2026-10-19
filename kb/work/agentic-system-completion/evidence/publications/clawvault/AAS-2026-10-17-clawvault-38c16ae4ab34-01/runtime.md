---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "ClawVault runtime baseline: vault writes, host recall, observation, maintenance and change admission at the frozen revision."
run-id: AAS-2026-10-17-clawvault-38c16ae4ab34-01
reviewed-boundary: bd702e9cce436bc3065827714cd576e8be20c375
---

# ClawVault runtime report

## Runtime account

ClawVault supplies persistent memory and host-facing context, not the enclosing agent's action-selection loop. This account uses SRC-1's implementation and doctrine/design layers at the boundary revision. No target code, tests, benchmarks or services were executed. All operation, model compliance, activation in a host answer and user benefit remain unobserved. The [boundary](boundary.md) supplies the frozen source and external-contract limits.

### Shipped paths and an ordinary invocation

The Node package declares `bin/clawvault.js`, ESM/CommonJS library entry points and an OpenClaw extension. The plugin has two materially different registrations: a host API registers tools and hooks with a `ClawVaultMemoryManager`; a registry-like object installs the simpler memory slot. Neither registration is evidence that a deployed OpenClaw delivered an event (SRC-1, `package.json`, `src/openclaw-plugin.ts`, `src/plugin/slot.ts`).

An ordinary library/slot invocation is store followed by search, then prompt delivery:

1. A caller supplies content, type/category, optional title and metadata to the memory slot. Explicit path, plugin configuration and agent identity select the vault. Code derives the default category and title, loads the vault, and calls `vault.store`; the caller, not a ClawVault model, supplies this content. See [RT-RTE-slot-store](#rt-rte-slot-store).
2. Loading reads `.clawvault.json`, configures search, reindexes Markdown and synchronizes graph/index state. Storage slugifies the title, rejects an existing filename unless overwrite was requested, serializes frontmatter/body, writes synchronously, reloads the document and updates indexes. Optional qmd updates are separate effects. The returned document is not a proof of all downstream consumers succeeding (SRC-1, `src/lib/vault.ts`).
3. A later query loads a vault and delegates `find` to search. In-process search chunks title/body, uses BM25, optionally combines available stored vectors with a query embedding, optionally reranks candidates, applies recency/score selection and returns document snippets. The search wrapper can prefer or fall back to qmd. Thus “in process” does not mean “no external calls” (SRC-1, `src/lib/search.ts`, `src/lib/in-process-search.ts`).
4. On a host `before_prompt_build` event, the plugin independently sanitizes the foreground prompt, resolves the agent vault and retrieves up to four memories by default, with minimum score 0.2 and temporal boosting. In parallel it fetches up to six recent recap entries. It formats titles, relative paths, ages and shortened snippets into a system-context addition. The result is bounded context, not the full stored document. A recall mandate and communication appendix are also added when their switches are enabled. The host owns the subsequent model invocation and answer. See [RT-RTE-prompt-recall](#rt-rte-prompt-recall) and [RT-BAP-system-context](#rt-bap-system-context).

This ordinary path crosses independent callers; ClawVault does not enforce that every store is followed by recall or that every answer consults memory. The simple slot returns search results or a recall string; the actual plugin also supplies unsolicited prompt context and foreground tools. The memory analyst can refine retained-object lineage and revision semantics without treating these consumers as equivalent.

### Selected forcing cases and guarantees

Three source-level forcing cases materially narrow the guarantees. They were inspected as branches, not executed as tests.

| Case | Enforcement owner and point | Covered paths and strength | Counterpath / external contract | Conclusions |
|---|---|---|---|---|
| Capture quality versus direct storage | `LiveCaptureService.captureTurn` invokes `evaluateCandidateQuality` before candidate persistence. | Local code invariant: candidates accepted through this route pass its configured confidence, junk, similarity and score tests. This is not a truth or completeness guarantee. | Slot `store`, core `store`, Python `store`, maintenance writes and peer pulls do not traverse this gate. Human approval per accepted candidate is not required here. See [RT-RTE-capture-turn](#rt-rte-capture-turn). | implementation conclusion status: wired; operation conclusion status: uninspected. |
| Search versus `memory_get` | Memory manager `toSafeFilePath` rejects `..` and permits only `MEMORY.md` or `memory/*`; search loads the broader indexed vault. | Protocol-level lexical path restriction on this read method, not a vault-wide access boundary. | Search can return category paths outside that allowlist, so an advertised detail lookup may reject a search hit. Filesystem symlink isolation and host shell policy are not established. See [RT-RTE-tool-recall](#rt-rte-tool-recall). | implementation conclusion status: wired; operation conclusion status: uninspected. |
| Plugin execution opt-in versus direct work | `runClawvault` and `runObserverCron` test `allowClawvaultExec`, resolve/check the executable and sanitize arguments; process creation uses `shell: false`. | Local invariant for these launch helpers; synchronous helper has a timeout, asynchronous observation only returns launch acceptance. | In-process retrieval, checkpoint, fact extraction and reflection are separately wired. Standalone CLI, scheduled scripts, maintenance and a host's own shell access are not mediated by this flag. Requires trusted executable/dependencies and host event delivery. | implementation conclusion status: wired; operation conclusion status: uninspected. |

The execution guard is literal:

> output: "ClawVault CLI execution is disabled. Set allowClawvaultExec=true to enable.",
> --- `src/plugin/clawvault-cli.ts`

These are distinct from the recall mandate's **policy** strength. The plugin owns its text insertion, not model compliance. The outbound-message handler adds a second, code-mediated control point, but only for messages routed through that hook and with the filter enabled. It rewrites content and can request cancellation when a question remains after memory evidence is substituted; this is not universal prevention of all unnecessary questions. See [RT-RTE-outbound-filter](#rt-rte-outbound-filter).

The capability surface includes local file reads/writes, optional model/embedding/rerank requests, qmd and CLI subprocesses, graph/dashboard serving and remote sync. The actual grant set depends on configuration, credentials, host tool registration and OS permissions; none was supplied. No deployed isolation envelope is established. There is no warrant to project a local helper's guard onto arbitrary host callbacks, provider-native tools, host shell access or extension code. These enclosing mechanisms remain external/unobserved rather than proven absent (SRC-1, `src/openclaw-plugin.ts`, `src/plugin/clawvault-cli.ts`, `src/lib/search.ts`, `src/lib/tailscale.ts`).

### Other material loops and change surfaces

Observation consumes transcript-derived strings, preserves raw capture by default, buffers until an estimated-token threshold or explicit flush, compresses against existing observations, writes daily observation Markdown and routes it to categories. Host heartbeat/reset/compaction launch paths and scheduled scripts can trigger it; the launch is not completion. Before compaction can also invoke independent rule-based fact extraction, which saves facts and a graph without launching the observation CLI. Host compaction itself, including what it evicts or preserves, is not implemented by these hooks (SRC-1, `src/plugin/hooks/observation.ts`, `src/plugin/hooks/session-lifecycle.ts`, `src/plugin/fact-extractor.ts`, `scripts/observe-active-sessions.sh`, `scripts/observe-stale-sessions.sh`). See [RT-RTE-observe-session](#rt-rte-observe-session).

Session handoff/recovery is a separate durable path: `sleep` records caller-supplied work and next steps; `wake` reloads handoffs, checkpoint/recovery state and selected recent observations. `sleep` catches observation/reflection errors after the handoff, so successful handoff does not guarantee those secondary products. The host plugin also keeps transient session recap/recovery-notice state, marks some recap text injected once, and clears session cache on session end. It does not thereby delete the durable transcript or vault (SRC-1, `src/commands/sleep.ts`, `src/commands/wake.ts`, `src/plugin/hooks/session-lifecycle.ts`). See [RT-RTE-session-handoff](#rt-rte-session-handoff).

Maintenance workers are sequential named computations, not evidence of independent agent contexts. The curator chooses categories using model JSON or heuristics; distiller extracts statements; janitor archives duplicates/stale captures and emits a report; surveyor emits graph-health suggestions. Their model calls receive selected samples/metrics rather than the foreground context. Only outputs escape these calls; there is no demonstrated general subagent stack or host-window trimming mechanism. The prompt injector is selective reload by value: files remain reachable through later retrieval, but the injected text is not a live pointer. See [RT-RTE-maintain-inbox](#rt-rte-maintain-inbox) and [RT-RTE-reflect-week](#rt-rte-reflect-week).

Peer sync directly admits external file content with direction/category/dry-run controls and timestamp-based conflict handling. Its trust and recovery assumptions differ from capture admission. The Python SDK independently stores/reloads Markdown, searches with BM25 and optional semantic merging, and builds a wake string. The dashboard watches Markdown and distributes rebuilt graph updates over HTTP/WebSocket; it is a visualization consumer, not evidence that the agent used those memories (SRC-1, `src/lib/tailscale.ts`, `python/src/clawvault/vault.py`, `dashboard/server.js`). See [RT-RTE-peer-sync](#rt-rte-peer-sync) and [RT-RTE-python-vault](#rt-rte-python-vault).

Product changes have a separate development-plane loop. `autoresearch/program.md` asks an agent to hypothesize, edit, commit, benchmark and keep/discard. The runner explicitly leaves edits to an external agent; the experiment script builds, runs a subset of tests, benchmarks and compares scores. There is no inspected automatic deployment from the kept branch into a production host. See [RT-RTE-autoresearch-change](#rt-rte-autoresearch-change). This path cannot be collapsed into ordinary memory updates.

Added SRC-1 inspection beyond the boundary's initial scope includes `src/capture/quality.ts`, the memory manager's search/read implementation, the plugin CLI helpers, `src/lib/search.ts`, `src/lib/in-process-search.ts`, hosted embedding/rerank configuration and requests, maintenance client/parsers/worker branches, `src/observer/reflection-service.ts`, `autoresearch/experiment.sh` and benchmark runner. These supply implementation evidence; `autoresearch/program.md` supplies doctrine/design. Source scans of wake/sleep, Python, dashboard and the scripts supplement the traces above. Detailed task/project mutation APIs, WebDAV authorization, entity synthesis internals, fact conflict resolution, observer router internals, dashboard parser, the separate evaluation adapter and dependency internals remain uninspected here. No guarantee of uniform validation, authorization, quality or parity across these included alternatives is asserted. In particular the separate evaluation loop cannot establish the plugin's end-to-end utility without tracing its adapter and consumers. These are inspection limits, not missing repository access or evidenced absences.

## Shared records

### Components

#### RT-CMP-compressor
Label: Observer Compressor

Source-native `Compressor` is TypeScript orchestration on disk with symbolic preprocessing/merging and natural-language prompt construction; the optional inference backend is distributed-parametric. Observer configuration selects provider, model and base URL. Default aliases include `claude-3-5-haiku-latest`, `gpt-4o-mini`, `gemini-2.0-flash`, `grok-2-latest` and `llama3.2`. Exact weights are not pinned. Mutable provider endpoints/model aliases can resolve to changed models. No parameter-update request is present in the inspected compression path; provider-side parameter changes remain uninspected. Retained observations can change independently of weights. SRC-1, `src/observer/compressor.ts`, `src/observer/observer.ts`.

> const fallback = this.fallbackCompression(cleanedMessages);
> return this.mergeObservations(existingObservations, fallback);
> --- `src/observer/compressor.ts`

The fallback makes availability of a model neither a necessary condition for a write nor proof of which backend produced a stored observation.

#### RT-CMP-worker-llm
Label: Maintenance and reflection LLM client

`createWorkerLlmClient` wraps symbolic TypeScript selection and HTTP completion calls to distributed-parametric providers. Provider weights live outside the repository. `CLAWVAULT_NO_LLM` disables maintenance inference; vault `observe` configuration and provider resolution select the backend, with per-call tier/model overrides. The inspected routes request inference, not weight changes. Exact versions are not pinned by immutable weight identities; OpenClaw gateway/custom provider routing is mutable. Provider internals and actual resolved versions are uninspected. Reflection uses the shared completion mechanism directly rather than this wrapper. SRC-1, `src/lib/maintenance/llm.ts`, `src/lib/llm-provider.ts`, `src/observer/reflection-service.ts`.

> model: options.model ?? configuredModel ?? undefined,
> tier: options.tier ?? 'default',
> --- `src/lib/maintenance/llm.ts`

#### RT-CMP-hosted-embeddings
Label: Hosted embeddings

`resolveEmbeddingConfig` and `embedText` select OpenAI, Gemini or Ollama numerical embedding inference; defaults include `text-embedding-3-small`, `text-embedding-004` and `nomic-embed-text`. Distributed-parametric model state is external; resulting dense vectors are numerical retained representations rather than model parameters. Configuration/HTTP requests are symbolic code. Exact model revisions are not pinned, configurable URLs and aliases can resolve differently, and the inspected client does not train/update model weights. Provider changes remain opaque. SRC-1, `src/lib/hosted-embeddings.ts`, `src/lib/in-process-search.ts`.

> model: searchConfig?.embeddings?.model?.trim() || DEFAULT_OPENAI_MODEL,
> --- `src/lib/hosted-embeddings.ts`

The inspected query path requires compatible available stored vectors; it does not prove document embeddings are fresh or correctly derived.

#### RT-CMP-hosted-rerank
Label: Hosted cross-encoder rerank

Configured Jina, Voyage, SiliconFlow or Pinecone requests consume query and candidate title/snippet strings and return numerical scores. Distributed-parametric models and weights reside at provider endpoints, while parsing/weighting is symbolic TypeScript. Runtime requests do not update weights; provider internals remain uninspected. Model names and endpoints are configurable, not immutable weight pins, so endpoint resolution may change. SRC-1, `src/lib/hosted-rerank.ts`, `src/lib/in-process-search.ts`.

> const endpoint = (searchConfig?.rerank?.endpoint?.trim() || DEFAULT_ENDPOINTS[provider]).replace(/\/+$/, '');
> const model = searchConfig?.rerank?.model?.trim() || DEFAULT_MODELS[provider];
> --- `src/lib/hosted-rerank.ts`

### Operative objects

#### RT-OBJ-vault-documents
Label: Vault Markdown documents

Core `Document` identity includes category-relative ID, absolute path, title, body, frontmatter, links/tags and modification time. Markdown body is natural-language material for later model/human use. Parsed frontmatter and IDs are symbolic selectors for code. The substrate is ordinary files with derived local search/graph state. These operative parts differ in consumers: category/status/date fields can determine inclusion without the reader interpreting prose. No claim that all YAML is enforced or that every file passed capture admission follows. SRC-1, `src/lib/vault.ts`, `src/plugin/slot.ts`.

> const filename = this.slugify(title) + '.md';
> const relativePath = path.join(category, filename);
> const fullPath = path.join(this.config.path, relativePath);
> --- `src/lib/vault.ts`

#### RT-OBJ-recall-mandate
Label: Memory recall mandate

`MEMORY_RECALL_MANDATE` is static natural-language policy encoded as a source string, consumed through the host system-context channel. It is shipped guidance, not memory accumulated through use. Feature flags and joining/insertion code are symbolic controls, distinct from semantic compliance. SRC-1, `src/plugin/hooks/before-prompt-build.ts`.

> "- Before answering anything about prior work, people, decisions, preferences, todos, or historical context, call memory_search first.",
> --- `src/plugin/hooks/before-prompt-build.ts`

### Routes

#### RT-RTE-slot-store
Label: Direct slot storage and reload

Caller → memory slot `store` → loaded `ClawVault.store` → Markdown and local indexes → returned document. Owner is the caller for content/category choice and code for naming, serialization, collision rejection and indexing. Open API mode; no expected-answer oracle or per-content human veto is wired. The caller may be human-directed or computational; generic identity does not settle that. Proposed change is a new memory, admitted by the direct API rather than the capture quality gate. Existing-file rejection can be overridden at the core API; no transactional multi-index rollback is established. SRC-1, `src/plugin/slot.ts`, `src/lib/vault.ts`.

- Immediate return: Document or thrown error after the core write/index sequence.
- Later read-back: Markdown reload/reindex and subsequent find, recall, wake or host injection.
- Delegated visibility: The same filesystem vault can be consumed by independent clients; no delegated agent launch occurs in this route.
- Selection predicate: Explicit path/configuration/agent selects vault; supplied category/type and slugified title select destination.
- Invalidation or expiry: File replacement/deletion and subsequent reindex change availability; no time-to-live is set by this store route.
- Activation or effect: Writes retained content and updates derived search state; influence on a host answer is unobserved.
- Evidence limits: No execution trace; disk write followed by index updates does not establish atomicity or cross-client consistency.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return vault.store({
> category,
> title,
> content,
> frontmatter
> });
> --- `src/plugin/slot.ts`

#### RT-RTE-capture-turn
Label: Assistant-response capture admission

Caller messages → normalization/assistant-role filter → extractor candidates → quality gate against existing and staged contents → persisted documents → optional entity synthesis. Code owns admission and can reject; originating assistant text supplies candidate content, with no per-candidate human approval. Open turn-capture mode, default cap eight accepted candidates; no answer oracle validates truth. Confidence/plausibility, secret/noise patterns and dedup are admission proxies, not criticism of the truth of a claim. Persisted metadata includes source, confidence and capture time. Collision recovery retries a timestamp-suffixed title; entity synthesis and partial multi-document failure recovery are not traced. SRC-1, `src/capture/service.ts`, `src/capture/quality.ts`.

- Immediate return: Counts, IDs, accepted candidates and rejection reasons; processing stops when accepted cap is reached, so rejected count need not describe every remaining candidate.
- Later read-back: Stored category documents enter later vault loading/search/injection.
- Delegated visibility: Accepted files are visible to other vault clients; entity mentions trigger another synthesis computation, not a host-agent delegation.
- Selection predicate: Assistant messages with extracted candidates; configured/default confidence, quality, similarity and junk checks.
- Invalidation or expiry: No expiry in capture; collision retry does not revise an old document.
- Activation or effect: Code admits new retained memories; later behavioral reliance is unobserved.
- Evidence limits: Extractor and synthesis internals are not fully inspected; proxy thresholds establish neither factual accuracy nor global protection of the vault.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const minConfidence = options.minConfidence ?? 0.4;
> const minQualityScore = options.minQualityScore ?? 0.4;
> const dedupThreshold = options.dedupThreshold ?? 0.82;
> --- `src/capture/quality.ts`

#### RT-RTE-prompt-recall
Label: Proactive prompt context injection

Host `before_prompt_build` event → hook → concurrent recap and memory fetch → formatted prepend/append strings → host. Code owns selection; the host owns subsequent invocation. Natural-language retained snippets and recap text pass through sanitization/truncation, while scores, limits and feature flags are symbolic rules. The default query limit is four, clamped 1–20, prompt length 500 and memory snippet length 220; recap defaults to six messages. Ordinary open-request mode, not a candidate-improvement experiment; no answer oracle is consulted. SRC-1, `src/openclaw-plugin.ts`, `src/plugin/hooks/before-prompt-build.ts`, `src/plugin/vault-context-injector.ts`, `src/plugin/clawvault-cli.ts`.

- Immediate return: `prependSystemContext` and `appendSystemContext`, or no hook result when no sections apply.
- Later read-back: Retrieved Markdown and prior conversation recap reach a later host prompt; startup notice/session recap cache may also be consumed.
- Delegated visibility: Host receives formatted strings, not the whole vault or raw provider context.
- Selection predicate: Feature flags; sanitized current prompt; resolved agent vault; score/recency/limit; nonempty snippets; session-key recap lookup.
- Invalidation or expiry: Retrieval runs anew; cached session recap is marked injected once and cleared on session end. Durable files remain separately reachable.
- Activation or effect: Adds proposed system-context content; host incorporation, model compliance and answer changes are unobserved.
- Evidence limits: Fetch failures become empty entries. A supplied contextProfile is not applied by the inspected memory-fetch branch; no profile-specific selection guarantee is established here.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const matches = await vault.find(prompt, {
> limit: maxResults,
> minScore: DEFAULT_MIN_SCORE,
> temporalBoost: true
> });
> --- `src/plugin/vault-context-injector.ts`

#### RT-RTE-tool-recall
Label: Foreground memory search and detail lookup

Host-registered `memory_search`/`memory_get` tools → manager → vault search or direct allowed-file read → tool result. The foreground agent chooses whether/what to call; code enforces query/limit/path rules. Search can derive agent identity from a supplied session key; detail read resolves the manager's default vault. This difference prevents assuming all identities share the same read destination. SRC-1, `src/openclaw-plugin.ts`, `src/plugin/memory-manager.ts`.

- Immediate return: Search snippets with score, path and estimated line citations; detail read returns raw or sliced file text, empty text for missing file, or error for disallowed path.
- Later read-back: Explicit requested retrieval of retained files; unlike proactive injection, it is selected by foreground query/tool action.
- Delegated visibility: Host/tool consumer receives results; no remote worker is launched.
- Selection predicate: Sanitized query, score and result limit for search; only `MEMORY.md` or `memory/*`, without `..`, for detail read.
- Invalidation or expiry: Repeated calls reload files; caller-held snippets can become stale after independent writes.
- Activation or effect: Makes selected text available to the host model; actual grounding is unobserved.
- Evidence limits: Search citations are estimated, not verified semantic evidence; lexical path checking is not a symlink/OS sandbox. Search-category hits need not be admissible to memory_get.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (mapped !== "MEMORY.md" && !mapped.startsWith("memory/")) {
> throw new Error("memory_get only allows MEMORY.md or memory/* paths");
> }
> --- `src/plugin/memory-manager.ts`

#### RT-RTE-outbound-filter
Label: Outbound communication filtering

Host message hook → deterministic rewrite → optional memory search for question-like content → evidence rewrite → content override/cancellation request. Code, not a separate model, owns the final hook decision. The host must honor it. Open outbound-message mode; a memory hit is not an expected-answer oracle. SRC-1, `src/plugin/hooks/message-sending.ts`.

- Immediate return: No override, replacement content, or `{ cancel: true }`.
- Later read-back: Question text queries retained memories, with at most two hits and default minimum score 0.35.
- Delegated visibility: Search evidence is passed to the rewrite helper; only the returned hook result reaches the host sending path.
- Selection predicate: Enabled filter; question detection; nonempty qualifying memory hits; question remaining after evidence rewrite.
- Invalidation or expiry: Recomputed per message; no durable filter decision is stored by this handler.
- Activation or effect: Can request suppression or replacement on this host channel; delivered outbound behavior remains unobserved.
- Evidence limits: Rewrite-helper semantics and host cancellation implementation are not audited; other delivery paths are not covered by this hook.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (shouldCancel) {
> return { cancel: true };
> }
> --- `src/plugin/hooks/message-sending.ts`

#### RT-RTE-observe-session
Label: Transcript observation and admission

Host observation hooks or standalone/scheduled CLI callers → observation computation → compressor → daily Markdown and router. Owner is invoking driver for timing, code/model for filtering and proposed summary, code for persistence. `Observer` defaults to raw capture and 30,000 estimated tokens, using approximately characters/4; flush bypasses this threshold. Pending messages are reset after a successful compression call and before subsequent writes/routing, so full atomic recovery across those effects is not established. New natural-language observations are software/model-admitted without per-item human veto. No expected-answer oracle is used in ordinary observation; compressor guidance asks for durable observations, not execution of arbitrary retained instructions. SRC-1, `src/observer/observer.ts`, `src/observer/compressor.ts`, `src/plugin/hooks/observation.ts`, `src/plugin/clawvault-cli.ts`.

- Immediate return: processMessages returns void; flush returns current observations and routing summary; detached host cron helper returns launch acceptance only.
- Later read-back: Existing daily observations condition a later compression; persisted observations can enter wake/reflection and category retrieval.
- Delegated visibility: Provider sees sanitized messages and existing observations; router receives compressed text and route context, not foreground host control.
- Selection predicate: Driver configuration/opt-ins, byte-growth scheduling and threshold/flush; compressor sanitization and deterministic fallback; dedup before persistence.
- Invalidation or expiry: Daily output can replace prior daily text; archive/reflection is a separate path. Raw capture persistence does not itself prove later behavioral use.
- Activation or effect: Writes durable observations and invokes category routing; host behavior changes are unobserved.
- Evidence limits: Full scheduler/parser/cursor/router logic is not traced. Detached process launch cannot guarantee completion before host compaction/reset. Independent fact extraction has a different store and admission path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> this.writeObservationFile(todayPath, compressed);
> this.observationsCache = compressed;
> --- `src/observer/observer.ts:184-185`

#### RT-RTE-session-handoff
Label: Sleep handoff and wake recovery

Caller-supplied work/next steps → sleep → createHandoff and dirty-flag clear → optional qmd/git/observation/reflection effects; later wake → recovery/checkpoint state, loaded vault, recap and selected recent observations → Markdown/string result. The caller owns handoff meaning; optional interactive questions allow a human to supply content. Noninteractive caller identity remains unresolved. No answer oracle judges handoff adequacy. The optional Git commit path is separate, requires interactive confirmation and a message, and is skipped noninteractively. SRC-1, `src/commands/sleep.ts`, `src/commands/wake.ts`.

- Immediate return: Sleep returns handoff/document/Git result and optional routing summary; wake returns recovery, recap, recapMarkdown, summary and observations.
- Later read-back: Handoffs/checkpoints and recent observation files reach a subsequent wake; host must deliver the result to an agent for further use.
- Delegated visibility: Optional compressor receives transcript strings; wake can request an executive summary. This does not delegate foreground task execution.
- Selection predicate: Nonempty working-on summary; supplied or interactively requested next/blocked fields; wake handoff limit and importance/recency selection; optional noSummary.
- Invalidation or expiry: Dirty flags are cleared; durable documents remain until another operation changes them. Clearing a flag is not deleting history.
- Activation or effect: Creates handoff, updates recovery state and returns context; actual restored task performance is unobserved.
- Evidence limits: Secondary observation/reflection exceptions are swallowed to preserve handoff completion; recovery completeness and Git success are not established. Optional wake-summary provider version is unpinned and its weights/update behavior are external; no training operation is requested by the inspected path.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // Observational memory should never block session handoff completion.
> --- `src/commands/sleep.ts`

#### RT-RTE-maintain-inbox
Label: Background inbox maintenance

CLI maintain → state/log/client load → curator, janitor, distiller, surveyor sequential dispatch → writes/reports/archive → state save and run summary. Models propose category/insights/recommendations; parsers, heuristics and worker code decide actual effects. Curator JSON categories must be in an allowlist; missing/invalid routes fall back to heuristics. Janitor actions are not all contingent on the model recommendations. Dry-run guards content helpers, but dispatcher still writes maintenance state; therefore dry-run is not a universal no-write guarantee. Guidance is shipped worker prompts; retained outputs include categorized copies, extracted statements, reports and processed hashes. Open maintenance mode, item limits and processed hashes trigger selection; no factual answer oracle or per-item human approval. Archive offers retained prior files, not demonstrated automatic rollback of every write. SRC-1, `src/commands/maintain.ts`, `src/lib/maintenance/curator-worker.ts`, `src/lib/maintenance/janitor-worker.ts`, `src/lib/maintenance/distiller-worker.ts`, `src/lib/maintenance/surveyor-worker.ts`, `src/lib/maintenance/worker-utils.ts`.

- Immediate return: Worker counts/actions/degraded-mode flags, run timestamps and log path.
- Later read-back: Processed hashes affect future pending selection; generated Markdown can be reindexed and retrieved. Reports' later agent use is unobserved.
- Delegated visibility: Curator sees at most 300-character item samples; distiller sees up to 1,800 characters; other workers pass selected metrics/prompts. No autonomous host-agent grant is created.
- Selection predicate: Chosen worker or all four, optional maxItems, pending hashes, long-form eligibility and worker-specific heuristics.
- Invalidation or expiry: Changed hashes can make content eligible again; janitor archive/move changes retrieval availability. Full reversal semantics are uninspected.
- Activation or effect: Changes retained knowledge organization/content and future worker selection, not model weights.
- Evidence limits: Not all heuristic thresholds or archive readers are audited; an LLM fallback/degraded flag does not establish equivalent semantic quality.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> writeMaintenanceState(vaultPath, state);
> --- `src/commands/maintain.ts`

#### RT-RTE-reflect-week
Label: Weekly observation reflection

Explicit reflection, sleep option or opt-in weekly lifecycle trigger → date-window observations → parsed/promoted records → prior-reflection-key exclusion → merged draft → optional LLM rewrite → header checks/fallback → reflection Markdown and archive. Computation proposes/adopts output; no human per-content approval or truth oracle is wired. Guidance requests the fixed section structure and preserved bullets. Model text is accepted if nonempty and required headings occur; this is a structural gate, not verification of preservation. Dry-run suppresses reflection/archive writes. Prior text/keys condition later drafts; archived originals support inspection but full automatic rollback is not established. SRC-1, `src/observer/reflection-service.ts`, `src/plugin/hooks/session-lifecycle.ts`, `src/commands/sleep.ts`.

- Immediate return: Processed/written week counts, paths, dry-run and archive result.
- Later read-back: Existing reflections and prior keys affect later reflection generation; generic vault indexing can expose written Markdown, without proving subsequent agent use.
- Delegated visibility: LLM receives a rendered weekly draft, not the complete foreground conversation; deterministic rendering is the fallback.
- Selection predicate: Date window, nonarchived/legacy observation enumeration, promotion rules and unseen keys. Weekly host trigger additionally requires Sunday 00:00 UTC and an unmarked week.
- Invalidation or expiry: Rewrites a weekly file and archives observations older than fourteen days when not dry-run; retention is not the same as direct availability to ordinary search.
- Activation or effect: Persists consolidated observations and changes future consolidation inputs; improved capacity remains unestablished.
- Evidence limits: The source-native name reflection does not itself establish reflective theory criticism; factual consistency after model rewriting and operational scheduling remain unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const markdown = llmMarkdown ?? renderReflectionMarkdown(weekKey, mergedSections);
> --- `src/observer/reflection-service.ts`

#### RT-RTE-peer-sync
Label: Peer file synchronization

Caller peer/direction configuration → local/remote manifests → comparison/filtering → network push/pull → direct file writes or optional orphan deletion → result/error lists. Software admits remote contents by manifest decisions, not capture quality tests; caller configuration is not human approval of each file. Ordinary synchronization mode, no answer oracle. Timestamp/hash comparison and direction govern acceptance; per-file failures are collected. No inspected content-level rollback or semantic validation protects an overwritten local file. SRC-1, `src/lib/tailscale.ts`.

- Immediate return: Pushed/pulled/deleted/unchanged paths, errors and transfer statistics.
- Later read-back: Subsequent vault loads consume pulled Markdown as local documents.
- Delegated visibility: Remote peer receives pushed file text or serves requested files. Actual peer trust/isolation is external.
- Selection predicate: Manifest comparison, direction, categories, dryRun; equal timestamps with differing content produce conflicts; orphan deletion requires pull mode and deleteOrphans.
- Invalidation or expiry: Overwrite and optional deletion alter retained content immediately; local search refresh is not shown in this transfer loop.
- Activation or effect: Admits externally supplied files capable of reaching later search/injection.
- Evidence limits: Server/WebDAV authorization and adversarial manifest paths are not audited; no deployment-security claim follows from Tailscale naming.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> fs.writeFileSync(filePath, content, 'utf-8');
> --- `src/lib/tailscale.ts:880`

#### RT-RTE-python-vault
Label: Independent Python vault client

Python caller → `Vault.store`/`remember`, search or wake → Markdown serialization/reload, per-query BM25 and optional semantic merging → Document/results/context string. Caller supplies admitted memory; software controls type routing and existing-file rejection. No per-content human veto or answer oracle is present. Constructor creates the directory, unlike TypeScript load's configuration-file precondition. This is an alternate implementation, not proof of parity. SRC-1, `python/src/clawvault/vault.py`.

- Immediate return: Stored Document, ranked search results or wake Markdown.
- Later read-back: list/search reload files; wake selects checkpoint, recent handoffs, active projects, pending commitments and recent decision/lesson titles.
- Delegated visibility: Caller receives returned values; semantic provider receives input through uninspected helpers when enabled.
- Selection predicate: Type/category and title for storage; query/category/limit for search; status/recency/category for wake.
- Invalidation or expiry: Explicit overwrite or independent filesystem changes; no automatic expiry in the inspected API.
- Activation or effect: Independent write and context construction, not a host prompt insertion by itself.
- Evidence limits: Search/semantic helper internals are not inspected; injected provider's distributed-parametric state, exact version and whether it changes parameters are uninspected because the constructor accepts an external provider. No parity or actual semantic benefit is inferred.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> file_path.write_text(markdown, encoding="utf-8")
> return self._load_document(file_path)
> --- `python/src/clawvault/vault.py`

#### RT-RTE-autoresearch-change
Label: Agent-driven product experiment admission

External coding agent following program guidance → hypothesis and source edit/commit → experiment script build, quick tests and Gemini benchmark → score comparison → keep entry or branch reset. Boundary is repository development plane over experiment rounds, not a production session. Proposed changes can affect prompts, retrieval code, fixtures and scoring functions. The stated objective is higher memory-quality benchmark score with tests passing; because scoring/fixtures are also editable, score gains alone do not identify improved real-world memory. The agent proposes and invokes; scripts decide strict scalar acceptance; an operator starts/stops the workflow. No automatic human review per edit is specified. Build/test/benchmark failure exits and records crash; a non-improving score records discard and resets the last commit. This destructive recovery assumes the agent's commit discipline. SRC-1, `autoresearch/program.md`, `autoresearch/run.sh`, `autoresearch/experiment.sh`, `src/observer/benchmark/runner.ts`.

- Immediate return: Experiment status/log and console report, or nonzero failure; run.sh ends at harness ready rather than driving code edits itself.
- Later read-back: Program asks the agent to consult results/Git state next round; kept commits and TSV/report files persist. This is prescribed agent behavior, not an observed autonomous sequence.
- Delegated visibility: Benchmark compressor receives fixture transcript plus configured existing observations; scorer receives expected and actual Markdown. Production host sees no automatic update in this path.
- Selection predicate: Script requires strictly greater aggregate overall score than prior kept best; ties discard. Doctrine separately permits a dimension improvement without regression, so doctrine and implemented script acceptance differ.
- Invalidation or expiry: Non-improving experiment invokes reset to HEAD~1; crash handling exits without the same reset. No automatic production deployment/rollback is established.
- Activation or effect: Can preserve/reject repository machinery changes when an agent supplies edits; subsequent live deployment is unobserved.
- Evidence limits: No execution/causal layer is registered; stored source-native scores are not used here as independently verified experiments. Tests cover a subset in the experiment script, not the entire package.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Answer oracle: fixture-authored expected observations and scoring configuration, supplied to `scoreFixtureObservations`; fixture-level provider overrides can differ from the report-level provider label. It assesses compressor outputs, not the complete host memory/answer loop. Operating mode: bounded fixture experiments inside an open-ended prescribed development loop. Rejection ability: script scalar gate and build/test failures; human interruption remains external.

> # The experiment loop is driven by the AI agent via the agent CLI
> # This script just provides the harness. The agent calls:
> --- `autoresearch/run.sh`

> git reset --hard HEAD~1
> --- `autoresearch/experiment.sh`

Theory account: the guidance asks an agent to formulate hypotheses about improving score; it does not expose an executed hypothesis/criticism sequence in the inspected paths. It retains code, commits, scores and requested research-log explanations, with next-round consumption prescribed. The following fields assess only this inspected development route, not inaccessible model thought:

Theory-builder conditions 1–4:

- condition 1 conclusion status: claimed

The program requests localized hypotheses, but no specific experiment theory was inspected.

- condition 2 conclusion status: claimed

Guidance asks the agent to choose edits from a hypothesis; code only establishes scalar acceptance.

- condition 3 conclusion status: uninspected

Score-based keep/discard does not establish content-directed criticism assigning blame to a theory, test, data or auxiliary assumption.

- condition 4 conclusion status: claimed

Next-round consultation is prescribed; no retained criticism-to-next-round execution is supplied.
- Addressability: source/prompt files are individually editable; addressability of formulated experiment theories and assumptions is uninspected.
- Persistence: repository commits/results/report files span rounds and potentially runs; subsequent actual agent consumption is unobserved.
- learning: uninspected. No improved future capacity or attribution is established from this inspected wiring alone.
- Reflection: afforded. Editable machinery and benchmark reports provide a self-representation/update channel in the development plane; semantic criticism and actual closed-loop use remain unobserved.
- Reflective theory builder: uninspected. No inspected criticism/revision of the program's own method texts against its operational records.
- Autonomous theory builder: claimed. Doctrine requests autonomous continuation, while the runner relies on an external agent to perform edits and reasoning.
- Self-improvement: afforded as a dormant development-plane pathway, not exercised self-improvement. Benchmark evidence is wired to script admission and kept edits can change repository organization; actual agent use of evidence to determine edits, entry into a later live behavioral-authority path, and subsequent operation depending on that change are unestablished. No success or causal benefit is attributed.

### Claims

#### RT-CLM-structured-memory
Label: Structured persistent agent memory

The declared work is typed durable memory and context engineering. This is supported as implementation capacity by the routes above, not universal recall, factual accuracy or measured benefit. SRC-1, `package.json`, `src/plugin/slot.ts`, `src/lib/vault.ts`.

> "description": "Structured memory system for AI agents — typed storage, knowledge graph, context profiles, canvas dashboards, neural graph themes, and Obsidian-native task views. An elephant never forgets. 🐘",
> --- `package.json`

#### RT-CLM-autonomous-research
Label: Continuous autonomous research claim

The program declares autonomous improvement; the shipped runner and script afford a benchmark-guided development workflow requiring an external editing agent. This claim is not operation evidence or proof of theory building. SRC-1, `autoresearch/program.md`, `autoresearch/run.sh`.

> This is a continuous autonomous research loop for improving ClawVault — an agent memory system.
> --- `autoresearch/program.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-system-context
Label: Retained content in host system context

Consumer: enclosing host model, if OpenClaw incorporates the hook result. Channel: `prependSystemContext` containing selected recap and vault snippets, alongside the static recall mandate; communication instructions use `appendSystemContext`. Force: requested natural-language influence through a privileged context channel, not code enforcement of correctness/compliance. Horizon: current prompt, with vault files available again in later invocations and transient once-injected session state. SRC-1, `src/plugin/hooks/before-prompt-build.ts`, `src/plugin/vault-context-injector.ts`; [RT-RTE-prompt-recall](#rt-rte-prompt-recall).

> prependSystemContext: prependSections.join("\n\n"),
> appendSystemContext: appendSections.join("\n\n")
> --- `src/plugin/hooks/before-prompt-build.ts`

#### RT-BAP-worker-state
Label: Processed hashes govern later maintenance

Consumer: later curator invocation. Channel: persisted maintenance state's processed-hash list. Force: symbolic exclusion from pending candidates, not advice to a model. Horizon: subsequent maintenance runs until content hash/state changes. This is retained operational control distinct from retrieved prose authority. SRC-1, `src/lib/maintenance/curator-worker.ts`, `src/commands/maintain.ts`; [RT-RTE-maintain-inbox](#rt-rte-maintain-inbox).

> const pending = items.filter((item) => !processed.has(item.hash));
> --- `src/lib/maintenance/curator-worker.ts`

## Annotations

none
