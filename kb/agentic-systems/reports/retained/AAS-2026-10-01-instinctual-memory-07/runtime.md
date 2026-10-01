---
type: types/agentic-system-runtime-report.md
description: "instinctual-memory runtime: store resolution, retrieval, consolidation, host delivery and controlled writes at the pinned commit"
run-id: AAS-2026-10-01-instinctual-memory-07
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# instinctual-memory runtime report

## Runtime account

The shipped product is `mem`, a memory service and CLI for an enclosing coding agent. It parses commands, reads and writes memory, calls optional models for extraction and ranking, and emits context to hosts. The enclosing agent owns task planning, tool choice and final answers; `mem` does not own that agent loop. The README's quick start initializes a store, backfills local sessions, consolidates them, searches them and writes selected facts into AGENTS.md (SRC-2, `README.md`). Implementation follows `main` through `Cli::resolve_store` and command dispatch (SRC-1, `src/main.rs`, `src/cli.rs`). Records RTE-1 through RTE-10 cover the inspected paths; CMP-1, CMP-2 and CMP-3 describe model mutability.

An ordinary `mem search "how do we deploy" --project shop` starts with the human or host agent as principal. Flags, then environment, then nearest local store, then global store determine the filesystem root. The selected root is a grant of access to that store; `--project` is a retrieval filter, not a user identity or authorization token. `cmd_search` builds `SearchParams`; `combined_search` pins a Git head, loads controls and scans eligible entity facts. It scans raw journal events separately, interleaves rows, optionally reranks and returns revision, ranker, judged flag and hits. The CLI renders text or JSON and may enrich snippets and source excerpts. The caller decides what to do with the result. No new memory is written by this search invocation (SRC-1, `src/cli.rs`, `src/ops.rs`, `src/search/mod.rs`). RTE-1 records its read-back and effect limits.

> /// The one search behind the CLI, MCP, HTTP, and the shell. Curated facts
> /// (eligibility and suppression enforced by `LexicalSearch`) and raw journal
> /// events are both searched; their rows are interleaved so each side
> /// reaches the reranker, and one rerank orders the combined pool.
> --- `src/ops.rs:156-159` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Alternate callable interfaces are MCP over newline JSON-RPC, loopback HTTP, and a restricted line-oriented memory shell. They use the shared operation dispatcher for search, read, history, status, memory changes and task updates. HTTP returns an operation ID only after executing the operation; its SSE endpoint replays stored progress/result records from an in-process map rather than continuing a durable worker. MCP requests are processed sequentially from stdin; HTTP spawns a connection thread. The memory shell dispatches enumerated commands and rejects shell syntax, rather than executing user lines as host commands. Internal subprocesses still invoke Git and `mem` for fixed functions. Library consumers can call public Rust functions directly; an excluded agent host may also possess independent shell/file access. Thus interface restrictions do not establish a sandbox for the enclosing agent (SRC-1, `src/mcp.rs`, `src/http_serve.rs`, `src/shell.rs`, `src/git.rs`, `src/lib.rs`).

Host callbacks and file writeback are materially different delivery routes. SessionStart emits up to twenty user preferences plus instructions to query and update memory. UserPromptSubmit selects at most six fact statements using a facts-only lexical search and meaningful-word overlap; it skips slash commands and prompts shorter than three words. Both write JSON `additionalContext`. SessionEnd spawns detached `mem hook sync`, which backfills and conditionally consolidates. Hook errors are swallowed unless debugging is enabled. File writeback emits persistent project instructions that a host may read on a later invocation. These routes wire delivery or persistence; host uptake, compliance and benefit remain unobserved at this boundary (SRC-1, `src/hook.rs`, `src/cli.rs`; RTE-4, RTE-5, RTE-6, BAP-1, BAP-2).

Three forcing cases limit important guarantees. First, project filtering happens after the fact lexical shortlist is capped at twenty; unrelated facts can occupy candidate slots before project filtering. The inspected ordering therefore does not guarantee top-k recall within a project, even though emitted fact rows pass the project predicate. The user can omit the predicate, and direct read/history accepts IDs without a project parameter. This is a scope convenience, not tenant isolation (SRC-1, `src/ops.rs`; RTE-1, RTE-2).

> fact_hits = LexicalSearch::search(&repo, &revision, &q, &controls)?;
>             if let Some(project) = p.project {
>                 let project_id = format!("w_{}", crate::consolidate::slug(project));
>                 fact_hits.retain(|h| project_entity_includes(&h.entity_id, &project_id));
>             }
> --- `src/ops.rs:181-185` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Second, reranker failure or decline falls through from remote JEV to a cached local model to lexical order; `MEM_RERANK=off` and no-rerank flags bypass model inference. This provides a best-effort search result, not invariant semantic ranking. The prompt hook always uses the lexical branch. Nothing in these branches establishes comparative accuracy or latency in operation (SRC-1, `src/search/rerank.rs`, `src/hook.rs`; RTE-1).

> match JevReranker::from_env() {
>         Ok(jev) => match JevRerankAdapter::new(jev).rerank(query, baseline.clone(), limit) {
>             Ok(r) if r.judged => return ("jev", true, r.hits),
>             Ok(_) => eprintln!("[search] jev declined; trying local reranker"),
>             Err(err) => eprintln!("[search] jev failed: {err}; trying local reranker"),
>         },
>         Err(Error::Jev(_)) => {} // no key configured
>         Err(err) => eprintln!("[search] jev unavailable: {err}"),
>     }
>     if let Some(local) = crate::search::laya::try_load_cached(models_dir) {
>         match local.rerank(query, baseline.clone(), limit) {
>             Ok(r) if r.judged => return ("laya", true, r.hits),
>             Ok(_) => {}
>             Err(err) => eprintln!("[search] local reranker failed: {err}"),
>         }
>     }
> --- `src/search/rerank.rs:170-185` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Third, `GitRepo::publish` validates a candidate and updates the memory ref with the expected base, while low-level replay checks compare a digest. Shared `memory_request_change` instead returns early on any receipt with the request ID, before comparing the submitted changes. A changed payload reusing an existing request ID can receive a replay response reporting its submitted statement without publishing that statement. This narrows end-to-end replay assurances on MCP/HTTP/shell compared with the low-level publisher. It is a source-inspected branch, not an executed reproduction (SRC-1, `src/repo.rs`, `src/ops.rs`; RTE-3).

> if let Ok(head) = repo.head() {
>         if repo
>             .read_receipt(&head, &request_id)
>             .ok()
>             .flatten()
>             .is_some()
>         {
>             let stored = count_statement(&repo, &entity_id, &statement).unwrap_or(0);
>             return ok(json!({
>                 "request_id": request_id,
>                 "replayed": true,
>                 "fact_id": fact_id,
>                 "entity_id": entity_id,
>                 "statement": statement,
>                 "stored": stored,
>             }));
>         }
>     }
> --- `src/ops.rs:436-453` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Load-bearing publication guarantee: owner `GitRepo`; enforcement point `publish` candidate validation followed by Git compare-and-swap; guarantee strength: invariant for successful calls through this function with an enforcing validator and Git's expected-old-ref semantics. Implementation conclusion status: wired. Operation conclusion status: uninspected, because no run traces are supplied. Covered paths include change, consolidation and tidy calls using DomainValidator. External contracts are reliable Git and filesystem operation and a caller that uses this publisher. Direct filesystem/Git access, setup, task JSON updates, project writeback and later erasure history rewriting have different enforcement. The public publisher accepts a caller-supplied validator; its signature alone does not force DomainValidator. DomainValidator validates parsing and references; it does not establish the truth or usefulness of a fact. Its checkpoint comment promises non-regression, but the inspected body parses then discards the checkpoint; regression protection cannot be credited to that validator (SRC-1, `src/repo.rs`, `src/validate.rs`).

> validator.validate(self, &candidate, &changed_paths)?;
>
>         // Compare-and-swap on the published branch.
>         let update_result = self
>             .git
>             .run_args(&["update-ref", MEMORY_REF, &candidate, base], None, None);
> --- `src/repo.rs:310-315` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Loopback guarantee: HTTP's `bind_listen` rejects non-loopback socket addresses before binding. Owner: HTTP server; enforcement point: bind function; guarantee strength: invariant for this listener path; implementation conclusion status: wired; operation conclusion status: uninspected. It requires OS socket semantics and does not authenticate local callers or control other interfaces. Hook non-blocking claim is best effort: errors are swallowed and end work is detached, but start/prompt still synchronously perform reads and lexical scans; no bounded host latency is observed. Managed-block preservation is a policy of default writeback with well-ordered markers; `--force` takes a whole-file replacement path (SRC-1, `src/http_serve.rs`, `src/hook.rs`, `src/cli.rs`).

The capability surface includes memory mutation, journal access, project-file writes, host configuration changes, local model downloads, optional provider calls and Git history erasure. Current grants are process filesystem permissions, selected store, supplied target paths, environment keys and explicit CLI mode flags. No deployed isolation envelope is supplied. `scope` and `session` labels organize requests, rather than representing verified identities. Model endpoints and host configuration are external contracts; provider-native execution of arbitrary tools is not part of the inspected extraction or ranking requests, which send data and request structured outputs (SRC-1, `src/cli.rs`, `src/ops.rs`, `src/consolidate.rs`, `src/jev.rs`, `src/setup.rs`).

No target process, test or service was executed. Checked-in test code is implementation evidence, not a passing run. Evaluation computes rubric-based comparisons but neither automatically changes the production ranker nor supplies results here (RTE-10). Model accuracy, actual forgetting across all external copies, activation by hosts and improved future capacity remain unobserved.

## Shared records

### Components

#### CMP-1 — Configurable extraction and tidy chat model

Source-native identity: `LlmConfig` and `chat_json`, shared by consolidation and tidy. Representational form: distributed model parameters outside the repository plus structured chat requests; storage substrate: external OpenAI-compatible endpoint, with model name/key/base URL from environment. Default model is `anthropic/claude-haiku-4.5`. Parameters changing during operation: no target-side parameter update in the inspected inference methods; provider updates uninspected. Exact version pinned: no immutable weight or deployment identifier. Mutable endpoint can resolve to another model: yes, configurable URL/model and external routing. Evidence: SRC-1, `src/consolidate.rs`, `src/tidy.rs`. Provider internals and exact weights remain uninspected.

> let body = serde_json::json!({
>         "model": cfg.model,
>         "temperature": 0,
>         "response_format": {"type": "json_object"},
>         "messages": [
>             {"role": "system", "content": system},
>             {"role": "user", "content": user},
>         ],
>     });
> --- `src/consolidate.rs:837-845` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### CMP-2 — Remote JEV relevance judge

Source-native identity: `JevReranker` using the Decisions API, default `~typesafe/jev-latest`. Representational form: distributed model parameters behind relevance scores; substrate: external provider endpoint. It sends clipped query and candidate statement in one request per document and uses parallel threads. Parameters changing during operation: no target-side training in the inspected request path; provider behavior uninspected. Exact version pinned: no, latest alias and configurable names. Mutable endpoint can resolve to another model: yes. Evidence: SRC-1, `src/jev.rs`, `src/search/rerank.rs`. Scores are relevance judgments, not an answer oracle.

#### CMP-3 — Local cross-encoder reranker

Source-native identity: `LayaReranker` backed by fastembed `TextRerank`, selecting BGE base, Jina turbo or BGE v2 m3. Representational form: ONNX model parameters; substrate: downloaded cache under `<root>/.models/`. Parameters changing during operation: inference methods do not train; selection/download can replace the loaded model. Exact version pinned: model family selected but no target-specified immutable model revision or weight hash in the inspected initialization. Mutable endpoint can resolve to another model: download resolution belongs to an excluded dependency; family is configurable and a selected-model file persists. Evidence: SRC-1, `src/search/laya.rs`. Inference is protected by a mutex; external model contents remain uninspected.

### Operative objects

#### OBJ-1 — Selected memory store

Source-native identity: memory root containing `memory.git`, journal and auxiliary state. Representational form: Git snapshots, YAML-frontmatter Markdown entities, JSON controls/checkpoints/receipts, JSONL journal and intent files. Storage substrate: local filesystem and bare Git repository. Evidence: SRC-1, `src/cli.rs`, `src/repo.rs`, `src/consolidate.rs`, `src/change.rs`. Its selection establishes the store operated on; it is not a verified tenant identity.

#### OBJ-2 — Versioned task file

Source-native identity: task version and title records accessed by `tasks_read`/`tasks_update`. Representational form: JSON task list; substrate: store-local file outside Git publication, updated under task lock and atomic rename. Evidence: SRC-1, `src/ops.rs`. It is retained task state, distinct from curated facts and consolidation checkpoint.

### Routes

All routes below have implementation conclusion status: wired and operation conclusion status: uninspected. This common statement applies individually; no supplied trace shows an invocation. Activation conclusion status is uninspected wherever the later consumer is an excluded model/host.

#### RTE-1 — Shared search and optional reranking

Endpoints/progression: CLI, MCP, HTTP or shell query → shared search → fact Git snapshot and journal scan → optional CMP-2/CMP-3 → result. Owner: command/operation dispatcher; caller owns successor action. Context/state/action effects: reads accumulated facts and events, optionally sends query/row text to provider; no store mutation. Immediate return: ranked statements with IDs and revision/ranker information. Later read-back: explicitly retrieves OBJ-1's accumulated facts and journal; search output itself is not durably retained by this route. Delegated visibility: any host receiving the returned result may pass it to another agent; propagation outside boundary is uninspected. Selection predicate: eligibility and controls, lexical terms, optional project/source filters, bounded candidate pool and configured ranker. Invalidation/expiry: current controls/status and time eligibility exclude curated rows; journal has its own scan path. Activation/effect: delivery to caller wired, changed answer behavior uninspected. Decision roles: computation selects shortlist/order; human/host selects query and optional flags, can bypass reranking. Answer oracle: none in ordinary search; CMP-2 supplies judgment. Operating mode: open requests, not a curriculum. Improvement trigger: none; scoring does not revise production machinery. Evidence limits: provider and host excluded; recall limited by pre-filter cap. Evidence: SRC-1, `src/ops.rs`, `src/search/mod.rs`, `src/search/rerank.rs`, `src/cli.rs`.

#### RTE-2 — Direct read and history

Endpoints/progression: caller ID → operation → fact/entity lookup or journal lookup → payload. Owner: shared dispatcher; caller chooses ID and subsequent interpretation. Immediate return: current fact/entity statements, status-labeled history or event text. Later read-back: stored facts and journal from OBJ-1. Delegated visibility: caller-controlled, outside boundary uninspected. Selection predicate: supplied ID and lookup controls; no project parameter. Invalidation/expiry: lookup filters stored controls/status; exact detailed eligibility remains for memory analysis. Context/state/action effects: read-only delivery. Activation: uninspected host uptake. Recovery: not-found/error response. Evidence limits: interface response not host behavior. Evidence: SRC-1, `src/ops.rs`.

#### RTE-3 — Remember, correct and forget admission

Endpoints/progression: CLI change or shared request operation → recovery → validated ChangeRequest → candidate entity/index/controls → durable intent → publisher → receipt. Owner: change module and GitRepo; caller proposes statements and target IDs. Human/computational roles: human or host model supplies open change request; computation validates and admits without an additional human approval stage. Veto/rejection: request validation, missing target, domain validation and publication conflict; caller may withhold request. Answer oracle: none; structural checks are not semantic ground truth. Trigger/proposed change: explicit remember/correct/forget, adding a fact, superseding one or retracting/suppressing one. Admission: successful validated publication. Rollback/recovery: Git history remains for soft changes; recovery republishes saved intents or sets stale/conflicting ones aside. Guidance: request/fact schema and correction/suppression rules; statements, controls, receipts and intents persist. Immediate return: receipt/result or conflict. Later read-back: changed facts/controls affect later RTE-1/RTE-2 and host delivery. Delegated visibility: store users share published head; excluded host delegation uninspected. Selection predicate: supplied entity/fact IDs; invalidation: subsequent correction/forget/erase. Activation/effect: published store change wired, consumer behavior uninspected. Evidence limits: shared receipt early return does not enforce the low-level digest comparison. Evidence: SRC-1, `src/change.rs`, `src/ops.rs`, `src/repo.rs`.

#### RTE-4 — Journal consolidation batches

Endpoints/progression: explicit consolidate or hook sync → checkpoint window → rules or CMP-1 extraction → placement/deduplication/file-fact retirement → entity/index/disposition/checkpoint publication. Owner/next-step: CLI loops until caught up unless explicit request ID bounds one batch; Consolidator computes each pass. Immediate return: revision and counters; later read-back: newly stored facts, dispositions and checkpoint shape subsequent consolidation/retrieval. Delegated visibility: shared store head, not an explicit agent delegation protocol. Selection predicate: events after checkpoint, bounded high-water window and scope filter; LLM branch uses note/user roles and filtered text. Invalidation/expiry: old file-derived facts can be retired, controls block IDs; subsequent change routes revise knowledge. Activation/effect: knowledge admission wired; later host activation uninspected. Trigger/proposed change: new events yield extracted sourced fact candidates. Proposer: deterministic extractor or CMP-1; decider/veto: local candidate checks, deduplication, controls, domain validator and CAS. Human role: supplies source material/configuration and starts manual run; no per-fact approval. Answer oracle: source passage occurrence is checked; it is not an independent oracle of truth or usefulness. Mode: bounded journal batches, optionally repeated to exhaustion; trigger is accumulated events, not measured capacity gain. Rollback/recovery: failed model request retries three times; failed batch does not publish through that path, later rerun starts from retained checkpoint. Guidance: fixed durable-fact prompt and placement policy; persists facts, source evidence, dispositions and checkpoint, not model reasoning. Theory account: this route applies fixed extraction guidance; no inspected route criticizes/revises that method text. Epistemic classification of retained fact content is deferred to its analyst.

Theory-builder conditions 1–4, assessed only for the shipped extraction method: condition 1 conclusion status: afforded, because the prompt states localized scope conditions and durability rules; condition 2 conclusion status: wired, because that prompt is supplied to CMP-1 to govern proposed facts, though sensitivity to its content is not experimentally observed; condition 3 conclusion status: absent within the inspected `llm_extract`/`chat_json` path, which checks proposals and retries requests without generating criticism of the method or revising its text; condition 4 conclusion status: absent for method criticism in that same path, because the persisted dispositions/checkpoint are not consumed to revise extraction guidance. Addressability: separately written prose exclusions and selection rules can be inspected in source, but the runtime exposes no method-edit admission. Persistence: static guidance is reconstructed from the executable every batch; facts and outcome records cross sessions. Learning conclusion status: uninspected, because future capacity and attribution lack operation/comparison evidence. Reflection conclusion status: uninspected for the extraction method; dispositions describe processing outcomes, but an outcome-mediated revision of method guidance is not wired in this path. Reflective theory builder conclusion status: absent for this method path because condition 3 is absent. Autonomous theory builder conclusion status: absent for this method path for the same reason, even though extraction/publication operations are computational. These findings do not classify every retained fact or inaccessible model-internal reasoning (SRC-1, `src/consolidate.rs`). Evidence: SRC-1, `src/consolidate.rs`, `src/cli.rs`.

> if !fact.lasting {
>         return Err("not lasting (true for one session only)");
>     }
>     if evidence.chars().count() < 8 {
>         return Err("evidence too short");
>     }
>     if !(8..=600).contains(&statement.chars().count()) {
>         return Err("statement empty or over 600 characters");
>     }
>     if !quote_found(&event.content, evidence) {
>         return Err("evidence not found in the cited event");
>     }
> --- `src/consolidate.rs:916-927` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-5 — Host context callbacks and detached synchronization

Endpoints/progression: host hook JSON → store selected by cwd → start preferences or prompt-match facts → `additionalContext`; end → detached executable → backfill and threshold-gated consolidation. Owner: hook code; host owns scheduling and model context incorporation. Immediate return: context JSON or silent success; end does not wait for background completion. Later read-back: start/prompt retrieve accumulated facts; background updates OBJ-1 through RTE-4. Delegated visibility: output only to invoking host; subprocess shares process environment and selected store. Selection predicate: start active fact availability; prompt ≥3 words, not slash command, meaningful-term overlap, facts-only limit; sync threshold and LLM configuration. Invalidation/expiry: current fact lookup/search policy at each callback; no revocation of already emitted context. Effects: context emission/backfill/consolidation wired; activation uninspected. Recovery: errors swallowed, debug optional, child statuses ignored; completion is not guaranteed. Admission decisions for knowledge follow RTE-4, not a separate hook semantic approval. Evidence: SRC-1, `src/hook.rs`, `src/cli.rs`.

> if let Some(text) = context {
>         let name = if event == HookEvent::Start { "SessionStart" } else { "UserPromptSubmit" };
>         let out = json!({"hookSpecificOutput": {"hookEventName": name, "additionalContext": text}});
>         writeln!(output, "{out}").map_err(|e| crate::error::Error::io("stdout", e))?;
>     }
> --- `src/hook.rs:75-79` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> if waiting >= threshold && status["extractor"] == "llm" {
>         let _ = quiet(&["consolidate"]);
>     }
> --- `src/hook.rs:209-211` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-6 — Project instruction writeback

Endpoints/progression: operator writeback target/flags → pinned head entities → selected facts → rendered managed block → filesystem write. Owner: CLI; host later decides whether to read instructions. Immediate return: written-fact count and path. Later read-back: persistent generated statements in target file can reach later host invocations. Delegated visibility: any file reader; host-specific propagation uninspected. Selection predicate: local-all or project-plus-preference entities, eligible statuses/visibility and source-type exclusions; flags include all/file-derived facts. Invalidation/expiry: overwritten only on another writeback; changes to Git memory do not automatically invalidate a previously written block. Effect/activation: persistent file change wired; model compliance uninspected. Trigger/proposed change: explicit command replaces generated instruction content. Proposer/decider: caller chooses file/flags; renderer selects material deterministically. Veto: filesystem error or caller withholding command, no semantic review. Answer oracle: none. Mode: open operator requests. Guidance/persistence: current retained statements and managed-block syntax shape file; original exterior text preserved by default. Recovery: no transactional rollback in inspected write call; `--force` discards exterior text. Evidence: SRC-1, `src/cli.rs`.

> // An existing file keeps its hand-written content; only the managed
>     // block between the markers is replaced. `--force` replaces the whole file.
>     let existing = if target.exists() && !force {
>         Some(std::fs::read_to_string(&target).map_err(|e| Error::io(&target, e))?)
>     } else {
>         None
>     };
> --- `src/cli.rs:1741-1747` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-7 — Host setup and model installation

Two separately controlled parts: setup writes host hooks/MCP/skill configuration under the user's home and invokes the Claude CLI; models pull downloads/loads the selected reranker and persists its name. Endpoints: explicit CLI setup/model selection → external configuration/cache. Owner: setup module or local reranker installer; human/host caller proposes installation/removal or model family; computation performs edits. Trigger/proposed change: enable host invocation capability or change model selection. Admission/rejection: explicit command, backup/write success for setup; dependency initialization/load success before recording selected model. No automatic semantic comparison chooses the model. Veto: caller chooses/remove target and filesystem/download errors reject changes. Answer oracle: none; load success is a compatibility check. Mode: open configuration requests. Guidance: fixed hook/MCP/skill templates and allowed model families; persists host configuration, skill text, downloaded parameters and selected-model file. Rollback/recovery: setup removal and backups; reranker selection can be changed by another pull/environment value, not an automatically evaluated rollback. Immediate return: installed actions or download/load error. Later read-back: hosts read edited config/skill; future reranking reads selected-model file/cache. Delegated visibility: host subprocess/config users; dependency/provider internals uninspected. Selection predicate: requested host target or model family. Invalidation/expiry: explicit removal/selection replacement; no expiry. Effect/activation: invocation wiring/cache installation wired; actual host activation uninspected. Evidence: SRC-1, `src/setup.rs`, `src/search/laya.rs`, `src/cli.rs`.

> /// Download `model` into `cache_dir` (showing progress), check it loads,
>     /// and record it as the model search uses.
>     pub fn pull(cache_dir: &Path, model: ModelKind) -> Result<()> {
>         std::fs::create_dir_all(cache_dir).map_err(|e| Error::io(cache_dir, e))?;
>         TextRerank::try_new(
>             RerankInitOptions::new(model.fastembed())
>                 .with_cache_dir(cache_dir.to_path_buf())
>                 .with_show_download_progress(true),
>         )
>         .map_err(|e| Error::SearchFailed(format!("downloading {}: {e}", model.name())))?;
>         let selected = cache_dir.join(SELECTED_FILE);
>         std::fs::write(&selected, model.name()).map_err(|e| Error::io(&selected, e))
>     }
> --- `src/search/laya.rs:116-128` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-8 — Version-checked task append

Endpoints: task update → exclusive task lock → compare expected_version → append title/increment version → atomic file replacement. Owner: task operations. Immediate return: new version/list or conflict with current list. Later read-back: later tasks_read retrieves OBJ-2. Delegated visibility: shared store callers; excluded host delegation uninspected. Selection predicate: expected version, supplied title. Invalidation/expiry: version advances; no task deletion/expiry in inspected update. State/action effect: append retained task record, no curated knowledge admission or autonomous task execution. Proposer: caller; decider/veto: lock-protected version check and required arguments, caller can withhold. Oracle: none. Operating mode: open task updates. Recovery: conflict allows re-read/retry; atomic rename protects replacement. Guidance: fixed schema/version protocol persists title/version. Activation: task execution by host uninspected. Evidence: SRC-1, `src/ops.rs`.

> if file.version != expected {
>             return Ok(OpResult {
>                 payload: json!({
>                     "conflict": true,
>                     "version": file.version,
>                     "tasks": file.tasks,
>                 }),
>                 progress: json!({"type": "progress", "stage": "tasks", "scanned": 0}),
>                 conflict: true,
>                 not_found: false,
>                 error: None,
>             });
>         }
> --- `src/ops.rs:501-513` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-9 — Tidy and erasure maintenance

Distinct admissions: tidy proposes duplicate/session-only suppression and applies it only with `--apply`; `--keep` vetoes IDs. Deterministic overlap keeps longer statements, CMP-1 flags session-only facts, computation publishes retained suppression reasons. Erase accepts an explicit fact/entity target, publishes current-tree removal and controls, redacts cited journal events, rewrites branch history and removes matching intents. Owner: tidy/erasure modules; caller owns target/apply decision. Immediate return: findings/apply revision or erasure counters/error. Later read-back: new controls/tree/journal affect later retrieval and consolidation; tidy reasons persist; erased content is removed from selected store structures. Delegated visibility: shared store users; external copies and source transcripts remain outside this erasure path. Selection predicate: duplicate overlap/model judgment/keep IDs or exact erase target plus cited event IDs and history scrub strings. Invalidation/expiry: persistent suppression, no expiry. Effect/activation: stored maintenance wired, behavioral change uninspected. Trigger/proposed change: manual maintenance; no measured performance-triggered improvement loop. Oracle: none; model lasting judgment is not ground truth. Guidance: fixed lasting-fact prompt and erasure scrub policy, not a revised production method. Admission/rejection: flags, target presence, validated publish and subsequent I/O success. Recovery: tidy preserves Git history; erasure is staged across multiple side effects and returns early on failures, so atomic erasure across journal/history/intents cannot be inferred. Comments promising rerun safety do not demonstrate recovery after every partial failure. Evidence: SRC-1, `src/tidy.rs`, `src/erasure.rs`.

Theory-builder conditions 1–4 for the tidy method: condition 1 conclusion status: afforded, with localized lasting/session-only rules in JUDGE_PROMPT; condition 2 conclusion status: wired, as the model receives those rules and its returned IDs drive suppression candidates; condition 3 conclusion status: absent in inspected `tidy`/`forget_all`, which evaluates facts rather than criticizing its selection rules; condition 4 conclusion status: absent for method criticism, because saved reasons do not revise JUDGE_PROMPT. Addressability: prompt parts are inspectable source prose, not runtime-editable method units. Persistence: executable guidance reused across runs, suppression reasons kept in controls. Learning conclusion status: uninspected, with no future-capacity comparison. Reflection conclusion status: uninspected for this method; no inspected feedback revises its own guidance. Reflective theory builder conclusion status: absent and autonomous theory builder conclusion status: absent for this method path because condition 3 is absent. Model-internal reasoning remains uninspected; these statements do not rule out content-directed criticism of particular retained facts (SRC-1, `src/tidy.rs`).

> //! Without `--apply` nothing changes. With it, every listed fact is
> //! forgotten in one commit: retracted in its entity file and suppressed in
> //! `state/controls.json` with the reason, so it disappears from every read
> //! and consolidation never re-adds it. Git history keeps the old versions.
> --- `src/tidy.rs:12-15` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> // Step 2: journal.
>     let events_redacted = journal.redact(&source_events)?;
>
>     // Step 3: history.
>     let mut needle_ids = ids.clone();
>     // An erased entity's own id is scrubbed from history too (older
>     // INDEX.md rows name it).
>     needle_ids.extend(erased_entities.iter().map(|id| format!("`{id}`")));
>     let needles = Needles::new(&erased, &needle_ids);
>     let commits_rewritten = rewrite_history(repo, &needles)?;
>
>     // Step 4: intents.
>     let intents_removed = remove_intents(repo, &needles)?;
> --- `src/erasure.rs:141-153` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-10 — Rubric comparison without automatic successor selection

Endpoints/progression: operator rubric file → same search lexical and reranked → expected-ID/include/exclude comparison → report. Owner: evaluation module; caller writes expected answers and decides any subsequent intervention. Immediate return: per-case pass/recall and aggregate report; optional CLI serialization. Later read-back: inapplicable for result, which this evaluation route does not store as a future control input; underlying facts are retrieved via RTE-1. Delegated visibility: report caller, further sharing uninspected. Selection predicate: rubric cases and top-k limit; expiry: none for a transient report. Effect: comparison wired, no automatic production admission or ranker revision. Human roles: rubric expectations and interpretation; computational roles: execute searches and score fixed string/ID predicates. Answer oracle: operator-supplied expected IDs and required/forbidden strings, used only in this bounded evaluation mode. Improvement trigger: operator command, not automatic failed-score repair. Theory account: compares retrieval outputs under fixed settings; does not criticize/revise extraction method text. Benefit and causal attribution remain unobserved without run results. Evidence: SRC-1, `src/evaluation.rs`, `src/cli.rs`.

### Claims

#### CLM-1 — Durable sourced memory reaches agents

Claimed operation: ingest prior sessions/files, extract sourced facts, retrieve and write them into project instructions; hooks make memory available without a tool request. Claim conclusion status: claimed. Implementation delivery conclusion status: wired, via RTE-1, RTE-4, RTE-5 and RTE-6. Activation conclusion status: uninspected; excluded hosts and absent traces prevent confirming memory changes answers. Evidence: SRC-2, `README.md`; SRC-1, `src/hook.rs`, `src/cli.rs`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### BAP-1 — Hook context as advisory guidance

Consumer: enclosing Claude Code model. Channel: hook `additionalContext` emitted on start/prompt. Force: advisory prose instructing search before guessing and recording new standing rules, accompanied by preference/fact statements; no target-enforced compliance. Horizon: current host invocation/session context, host retention beyond emission uninspected. Implementation conclusion status: wired; activation conclusion status: uninspected. Evidence: SRC-1, `src/hook.rs`; RTE-5.

#### BAP-2 — Generated project instruction block

Consumer: agent host reading AGENTS.md or selected writeback destination. Channel: persistent Markdown file. Force: project-instruction authority depends on excluded host file loading and precedence; `mem` does not enforce it. Horizon: later sessions until explicitly overwritten; source store updates alone do not refresh the block. Implementation conclusion status: wired; activation conclusion status: uninspected. Evidence: SRC-1, `src/cli.rs`; RTE-6.

## Annotations

none
