---
type: agentic-systems/types/agentic-system-runtime-report.md
description: "Instinctual-memory runtime: shared memory operations, consolidation, hooks and alternate publication paths"
run-id: AAS-2026-10-02-instinctual-memory-02
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual-memory runtime report

## Runtime account

The shipped `mem` library and CLI provide persistent memory operations for external coding agents. They do not own a conversational agent loop. A client chooses when to search, read or change memory; the target executes that request against a selected local or global store. This runtime account is source-grounded. No supplied trace, test result or experiment establishes operation, host activation, retrieval benefit or reliability. SRC-1: `src/main.rs`, `src/cli.rs`, `src/lib.rs`, `src/mcp.rs`; SRC-2: `README.md`.

An ordinary invocation is an MCP client's `memory_search` tool call (RTE-1). The CLI resolves a store and starts the stdio server with a root, scope and session. The server reads newline-delimited JSON-RPC, validates/parses the message, dispatches `tools/call`, and forwards the named operation and JSON arguments to `ops::execute`. The tool caller owns the next step; no target-side model decides whether to call another tool. `search` requires nonempty query text, clamps the limit to 1–20 and defaults reranking on. `combined_search` reads a pinned Git head for curated facts, loads controls, applies fact eligibility through lexical search, scans raw journal events, interleaves the two pools and optionally reranks. The terminal result supplies hit IDs, statements, source paths, scores, revision, ranker and judgment flag, wrapped as MCP content. Error payloads return without advancing an agent task. SRC-1: `src/cli.rs`, `src/mcp.rs`, `src/ops.rs`.

The computational ranking policy is executable Rust plus optional CMP-2/CMP-3 inference. The query and candidate pool are temporary invocation context. Existing facts and journal events persist independently of the search. Neither the MCP transport nor search establishes that a host follows the returned statements. RTE-1 records the distinction between delivery and activation. HTTP invokes the same operation dispatcher, using one thread per connection and a process-local operation/event map; its SSE stream reports stored progress/result after operation execution rather than a durable job log. Shell commands also enter the operation layer. CLI search exposes extra scope, source, disputed-fact, snippet and facts-only controls. Direct library users can invoke search and publication APIs. SRC-1: `src/http_serve.rs`, `src/shell.rs`, `src/cli.rs`, `src/lib.rs`, `src/ops.rs`.

Three forcing cases materially narrow guarantees. First, disabling reranking returns lexical results; remote failure or refusal falls through to a cached local ranker and then lexical results. A nonempty result therefore does not establish model judgment (RTE-1). Second, the lower Git publisher detects same-ID/different-payload conflicts, but `ops::request_change` returns early whenever a receipt with that request ID exists, without comparing its digest with this request. MCP, HTTP and shell use this shortcut; their replay acknowledgment therefore does not demonstrate payload identity (RTE-2). Third, the extractor's advertised verbatim evidence check normalizes text and admits ordered ellipsis fragments, discarding fragments shorter than eight characters. It checks occurrence, not entailment or factual truth (RTE-3). These are inspected branches, not executed reproductions. SRC-1: `src/search/rerank.rs`, `src/ops.rs`, `src/repo.rs`, `src/consolidate.rs`.

Validated atomic publication is owned by `GitRepo::publish`: build an isolated candidate index/commit, call the supplied validator and compare-and-swap the memory branch from the expected base. Its strength is an invariant for that branch update under Git's update-ref contract; implementation conclusion status: wired; operation conclusion status: uninspected because no run evidence is supplied. Normal change, consolidation, tidy and index callers supply domain validation. Direct public library callers choose their `Validator`; shell/filesystem access can bypass these APIs. The guarantee does not cover journal writes, task files, setup files, project writeback, remote inference or all stages of erasure. SRC-1: `src/repo.rs`, `src/change.rs`, `src/consolidate.rs`, `src/tidy.rs`, `src/erasure.rs`, `src/lib.rs`.

HTTP's loopback-only bind is a wired invariant at `bind_listen`, conditional on OS networking. It limits the listener address; it is not per-operation authentication. `handle_connection` accepts the named operations and discards the parsed headers. Stdio assumes an authorized local launcher; neither transport adds a human approval step. Current filesystem and provider grants depend on the process user and configured keys. No deployed isolation envelope is supplied. The system can write memory stores, host configuration and project files, spawn its own executable and Git, and send text to configured inference services. That capability surface cannot establish which grants a real host gives it. SRC-1: `src/http_serve.rs`, `src/mcp.rs`, `src/setup.rs`, `src/hook.rs`, `src/git.rs`, `src/consolidate.rs`.

> if !is_loopback(addr.ip()) {
>         return Err(Error::InvalidContent(format!(
>             "refusing non-loopback listen address {listen}"
>         )));
>     }
>     TcpListener::bind(addr).map_err(|e| Error::io(std::path::Path::new(listen), e))
> }
> --- `src/http_serve.rs:38-44` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Consolidation (RTE-3) is a separate CLI loop: choose rules or model extraction, read events beyond a checkpoint in bounded windows, propose facts, check/merge them and publish entities, index, checkpoint and dispositions together. It repeats until caught up unless a named single batch was requested. Host end hooks can spawn background backfill/consolidation with ignored child results (RTE-5). Tidy, erasure, tasks, writeback, setup and model installation admit distinct changes (RTE-4 through RTE-9). Their decision roles and recovery limits are recorded below. Evaluation and bench are explicit CLI mechanisms, not gates on normal publication; their source definitions provide no observed scores or timing. SRC-1: `src/cli.rs`, `src/consolidate.rs`, `src/hook.rs`, `src/tidy.rs`, `src/erasure.rs`, `src/evaluation.rs`.

## Shared records

### Components

#### CMP-1 — Configured chat-completion extractor

Source-native identity: `LlmConfig` / OpenAI-compatible chat completion, default `anthropic/claude-haiku-4.5`. Representational form: external distributed model parameters, receiving system text and JSON event/known-entity context. Storage substrate: hosted provider, outside the boundary. Parameters changing during operation: uninspected provider internals; target sends inference requests and implements no parameter update on RTE-3. Exact version pinned: no immutable weight/version identifier is enforced. Mutable endpoint can resolve another model: yes, base URL and model environment variables are configurable; resolution at the provider is uninspected. Implementation conclusion status: wired; operation conclusion status: uninspected without supplied inference evidence. SRC-1: `src/consolidate.rs`.

> model: std::env::var("MEM_LLM_MODEL")
>                 .ok()
>                 .filter(|v| !v.is_empty())
>                 .unwrap_or_else(|| "anthropic/claude-haiku-4.5".into()),
>         })
>     }
> }
> --- `src/consolidate.rs:562-568` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### CMP-2 — JEV remote relevance judge

Source-native identity: `JevReranker`, default `~typesafe/jev-latest`. Representational form: remote parametric relevance decisions, consumed as scores by RTE-1. Storage substrate: configured Decisions endpoint. Parameters changing during operation: uninspected; target adapter does not train. Exact version pinned: no, the default is a latest alias. Mutable endpoint can resolve another model: yes; both endpoint and model are configurable. Provider internals and scoring quality remain uninspected. Implementation conclusion status: wired; operation conclusion status: uninspected. SRC-1: `src/jev.rs`, `src/search/rerank.rs`.

> let model = first_nonempty(&["MEM_JEV_MODEL", "JEV_MODEL"])
>             .unwrap_or_else(|| DEFAULT_MODEL.to_string());
>         Ok(Self::new(decisions_url, api_key, model))
>     }
> --- `src/jev.rs:86-89` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### CMP-3 — Cached local cross-encoder

Source-native identity: `LayaReranker` with BGE-reranker-base, Jina-v1-turbo-en or BGE-v2-m3. Representational form: model weights executing through fastembed; output scores order candidate text. Storage substrate: `<root>/.models` cache, loaded model in memory. Parameters changing during operation: no update is implemented in inspected adapter; dependency internals are excluded. Exact version pinned: model family is selected, but this adapter supplies no immutable weight revision/hash. Mutable endpoint can resolve another model: runtime uses cached assets; asset acquisition and dependency resolution are outside inspected provider internals. Environment/selected-file changes can choose a different family (RTE-9). Implementation conclusion status: wired; operation conclusion status: uninspected. SRC-1: `src/search/laya.rs`.

> pub fn selected_model(cache_dir: &Path) -> ModelKind {
>         if let Some(model) = std::env::var("MEM_LAYA_MODEL").ok().and_then(|v| ModelKind::parse(&v)) {
>             return model;
>         }
>         std::fs::read_to_string(cache_dir.join(SELECTED_FILE))
>             .ok()
>             .and_then(|v| ModelKind::parse(v.trim()))
>             .unwrap_or(ModelKind::BgeRerankerBase)
>     }
> --- `src/search/laya.rs:106-114` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Operative objects

#### OBJ-1 — Published memory snapshot

Source-native identity: `memory.git` branch with entity Markdown, index, controls, checkpoint, dispositions and receipts. Representational form: structured fact metadata and prose statements plus JSON state. Storage substrate: local Git objects and branch reference. Later consumers: search, read/history, consolidation, hooks and writeback. The representation and eligibility mechanics are wired; actual later use is unobserved. SRC-1: `src/repo.rs`, `src/entity.rs`, `src/fact.rs`, `src/consolidate.rs`, `src/ops.rs`.

#### OBJ-2 — Source-event journal

Source-native identity: `Journal` / `JournalEvent` daily JSONL files with sequence and source identity. Representational form: transcript/file text plus structured provenance. Storage substrate: local journal directory, sequence counter and locks. It supplies raw retrieval and consolidation across invocations. Normal and bulk append have separate flush behavior; no execution evidence establishes crash durability. SRC-1: `src/journal.rs`, `src/ingest.rs`, `src/ops.rs`.

#### OBJ-3 — Integration output and host files

Source-native identity: `hookSpecificOutput.additionalContext`, managed `mem:begin` block, setup configuration and supplied `/mem` skill. Representational form: guidance and retrieved fact prose, JSON hook output, JSON/TOML registrations. Storage substrate: stdout for hooks; project and home-directory files for writeback/setup. Host consumption and behavioral compliance are outside boundary. SRC-1: `src/hook.rs`, `src/setup.rs`, `src/cli.rs`; SRC-2: `skills/mem/SKILL.md`.

#### OBJ-4 — Versioned task list

Source-native identity: task file read/updated by `tasks_read` and `tasks_update`. Representational form: JSON version and task titles/IDs. Storage substrate: root-local file protected by task lock and atomic writer. Separate from Git fact publication. SRC-1: `src/ops.rs`.

### Routes

#### RTE-1 — Retrieve facts and raw sessions

Endpoints/progression: host, CLI or shell query → operation/search layer → pinned OBJ-1 facts plus OBJ-2 events → optional CMP-2/CMP-3 score ordering → returned hit JSON/text. Owner: caller selects operation; Rust controls filters, pooling and fallback. Context/state/action effects: temporary query/pool; external request when JEV is enabled; no persistent memory mutation. Implementation conclusion status: wired; operation conclusion status: uninspected.

Immediate return: bounded hits, IDs, revision and ranker/judged information. Later read-back: reads accumulated OBJ-1/OBJ-2 from earlier use; search itself retains no new material. Delegated visibility: caller receives results; no autonomous delegation is implemented in this route. Selection predicate: lexical eligibility and scores, optional project/source/scope filters, then configured ranking and limit. Invalidation/expiry: controls and current fact status filter curated results; raw journal remains a separate channel. Activation/effect: delivery is wired; host behavior and benefit unobserved. Evidence limits: no inference trace or result comparison. Computational proposal/decision: lexical code and optional relevance judges select results; human contribution is query/configuration. Answer oracle: none in normal search; model judgment is not a reference answer. Operating mode: open requests, no automatic improvement trigger. SRC-1: `src/ops.rs`, `src/search/rerank.rs`, `src/search/lexical.rs`.

> match operation {
>         "memory_search" => search(root, args),
>         "memory_read" => read(root, args),
>         "memory_history" => history(root, args),
>         "memory_status" => status(root),
>         "memory_request_change" => request_change(root, scope_id, session_id, args),
>         "tasks_read" => tasks_read(root),
>         "tasks_update" => tasks_update(root, args),
> --- `src/ops.rs:42-49` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> if baseline.is_empty() || off {
>         let mut hits = baseline;
>         hits.truncate(limit);
>         return ("lexical", false, hits);
>     }
> --- `src/search/rerank.rs:165-169` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-2 — Admit immediate memory changes

Endpoints/progression: remember/correct/forget request → `ChangeRequest` validation → entity/index/control changes → durable intent → domain-validated candidate publication → receipt/intent completion. Owner: caller proposes content; Rust admission and CAS can reject malformed/stale requests. Context/state/action effects: change OBJ-1; forget adds suppression and retraction. Trigger/proposed change: explicit CLI/tool request. Admission: no human approval inside target; validation checks structure and repository state, not statement truth. Rejection ability: validators and conflicts; caller may decline to request. Rollback/recovery: durable intents allow interrupted requests to recover; stale intents can be set aside. No automatic semantic rollback is shown. Guidance shaping proposal: caller statement and change kind; statements, metadata, reasons, controls and receipts persist. SRC-1: `src/change.rs`, `src/ops.rs`, `src/repo.rs`.

Immediate return: published revision/replay/target or failure. Later read-back: new or revised facts and controls reach subsequent readers of OBJ-1. Delegated visibility: clients with access to the same root can read; no delegated-agent-specific grant is enforced here. Selection predicate: named entity/target and read eligibility. Invalidation/expiry: correction supersedes old fact; forget suppresses it; no TTL. Activation/effect: store mutation wired, downstream behavior unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. Roles: human or host supplies statement, code admits; no answer oracle. Mode: open changes; no performance-driven update trigger. Guarantee strength: invariant for validator-before-CAS branch publication under Git contract, not universal truth or transport-wide payload-checked replay.

> validator.validate(self, &candidate, &changed_paths)?;
>
>         // Compare-and-swap on the published branch.
>         let update_result = self
>             .git
>             .run_args(&["update-ref", MEMORY_REF, &candidate, base], None, None);
> --- `src/repo.rs:310-315` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The shared operation replay shortcut checks receipt existence before constructing and applying a request. This limits the stronger digest-checked replay guarantee of `GitRepo::publish` on this alternate path.

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

#### RTE-3 — Consolidate journal into facts

Endpoints/progression: explicit CLI or hook sync → checkpoint/window of OBJ-2 → rules or CMP-1 proposals → occurrence/shape checks and duplicate placement → entity/index/checkpoint/disposition candidate → domain validation/CAS into OBJ-1. Owner: Rust batch loop; model proposes only on the LLM path. Context/state/action effects: bounded event/known-entity context; external inference; retained facts, outcomes and checkpoint. Trigger: explicit consolidation or configured hook backlog threshold. Proposed change: durable fact insertion/retirement. Admission/rejection: deterministic checks, model `lasting` flag, placement/suppression checks and publisher; no human gate. Rollback/recovery: inference retries up to three attempts; failed extraction publishes no batch; re-run resumes from checkpoint. No observed recovery result. Guidance: shipped extractor prompt instructs durable standing facts and excludes tasks/boilerplate; prompt remains static, facts and dispositions persist. SRC-1: `src/consolidate.rs`, `src/cli.rs`, `src/hook.rs`.

Immediate return: revision/report or error. Later read-back: accepted facts reach later search/hooks/writeback; retained checkpoint/dispositions govern later batching. Delegated visibility: same-root consumers can read facts; external model receives selected event text and known entities. Selection predicate: sequence window/scope, role/content filters, extractor and placement checks. Invalidation/expiry: controls block suppressed/deleted IDs; changed file facts can retire earlier facts; no general TTL. Activation/effect: publication wired; later behavioral use/benefit unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. Roles: model or rules propose, code decides, operator chooses configuration and can refrain; no answer oracle. Mode: bounded batches over open input history; backlog is an operational trigger, not measured improvement.

Evidence check strength: invariant for ordered normalized fragment occurrence in cited event, conditional on helper implementation; it neither proves exact byte quotation nor statement entailment. The rules and immediate-change paths do not use this model-evidence gate.

> fn quote_found(source: &str, evidence: &str) -> bool {
>     let haystack = normalise(source);
>     let fragments: Vec<String> = evidence
>         .replace('…', "...")
>         .split("...")
>         .map(normalise)
>         .filter(|f| f.chars().count() >= 8)
>         .collect();
>     if fragments.is_empty() {
>         return false;
>     }
>     let mut from = 0usize;
>     for fragment in &fragments {
>         match haystack[from..].find(fragment.as_str()) {
>             Some(at) => from += at + fragment.len(),
>             None => return false,
>         }
>     }
>     true
> }
> --- `src/consolidate.rs:981-1000` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Theory account: guidance is the shipped durability-selection rule set; extraction applies it, but does not criticize/revise that rule set. What persists is facts, sources and dispositions, not an operationally revised prompt. Theory-builder conditions 1–4: 1 afforded, prompt is a whole inspectable content unit; 2 wired, prompt is supplied to extraction and deterministic rules drive decisions, with model uptake unobserved; 3 uninspected for opaque model processing and no exposed content-directed rule criticism in this inspected batch route; 4 uninspected for such criticism shaping a next round, despite ordinary checkpoint iteration. Addressability: prompt/rules are source-editable; no runtime parts editor. Persistence: shipped guidance across sessions, facts across invocations. Learning: uninspected, no improved-capacity or attribution evidence supplied. Reflection: uninspected, no two-direction representation-mediated revision of the extraction method observed. Reflective/autonomous theory builder: uninspected; operational automation alone cannot establish the required criticism cycle.

#### RTE-4 — Diagnose and suppress low-value facts

Endpoints/progression: `tidy` reads OBJ-1 → deterministic duplicate/session-only findings → report, or with `--apply` → retractions/controls/index publication. Owner: code proposes findings; operator chooses apply and can veto named IDs with `--keep`; code validates publication. Trigger/proposed change: manual cleanup, suppression of flagged facts. Admission/rejection: apply flag, keep list, domain validator/CAS. Rollback/recovery: retained Git history remains; no automatic semantic undo shown. Guidance: token overlap/containment, length ordering and session-only patterns; suppression reasons persist. Immediate return: findings and optional revision. Later read-back: controls affect later eligibility and consolidation; delegated visibility: same-root readers, no separate agent grant. Selection predicate: active unsuppressed facts and deterministic heuristics. Invalidation/expiry: retracted/suppressed until another authorized change; no TTL. Activation/effect: eligibility change wired, utility unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. No answer oracle; mode: operator-requested diagnosis/application. Theory account: fixed selection heuristics are applied; report concerns facts, not criticism/revision of the heuristics. Conditions 1–4: 1 afforded as inspectable whole rule units; 2 wired; 3 uninspected for content-directed criticism of those rules; 4 uninspected for retained criticism driving rule revision. Addressability: source units editable, runtime thresholds not revised by findings. Persistence: code and suppression reasons across invocations. Learning/reflection/reflective theory builder/autonomous theory builder: uninspected without improvement or method-revision evidence. SRC-1: `src/tidy.rs`.

#### RTE-5 — Inject hook context and sync asynchronously

Endpoints/progression: external host hook event → selected store → start preferences or prompt-matching curated facts → OBJ-3 JSON stdout; end event spawns `mem hook sync`, which backfills and may consolidate. Owner: host schedules hooks; Rust selects text and spawns child, host owns resulting agent action. Effects: context output or OBJ-2/OBJ-1 mutation through ingestion/RTE-3. Immediate return: optional context; no child success acknowledgment at session end. Later read-back: prior facts reach a later host invocation; sync accumulates events for later extraction. Delegated visibility: self subprocess inherits process environment/current directory, not an agent delegation. Selection predicate: start requires active facts; prompt ignores slash/short requests, uses facts-only lexical retrieval and meaningful-term overlap. Invalidation/expiry: current curated fact eligibility, no host-context retraction protocol. Activation/effect: emitted context wired; real host consumption unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. Admission fields for sync are RTE-3 plus journal append: host event/backlog triggers, source adapters propose events, journal writer admits; failure is intentionally quiet and no end-hook rollback shown. Guidance: emitted text asks host to search and remember standing rules; stored events/facts persist. SRC-1: `src/hook.rs`, `src/journal.rs`, `src/cli.rs`.

> if let Some(text) = context {
>         let name = if event == HookEvent::Start { "SessionStart" } else { "UserPromptSubmit" };
>         let out = json!({"hookSpecificOutput": {"hookEventName": name, "additionalContext": text}});
>         writeln!(output, "{out}").map_err(|e| crate::error::Error::io("stdout", e))?;
>     }
>     Ok(())
> }
> --- `src/hook.rs:75-81` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-6 — Erase current facts, source events and history

Endpoints/progression: CLI/library target → validated current-tree deletion/controls publication → journal redaction → locked history rewrite/prune → intent removal. Owner: explicit caller chooses target; code computes source-linked removal. Trigger/proposed change: explicit irreversible erasure. Admission/rejection: nonempty target, existing/deleted/suppressed checks and initial domain-valid publication; errors can stop later stages. Rollback/recovery: no cross-substrate transaction or automatic rollback is shown; completed deletion is recorded before subsequent stages. Guidance: target identity and optional reason; deletion/suppression records persist, targeted content is scrubbed. Immediate return: stage counts/revision or error. Later read-back: altered controls/current tree/journal/history affect later invocations. Delegated visibility: local Git subprocess, no agent delegation. Selection predicate: target fact/entity, cited source events and scrub needles. Invalidation/expiry: deletion by ID; does not erase excluded host originals, provider copies or previously written project files. Activation/effect: staged modifications wired; complete operational erasure unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. Human/computational roles as above; no answer oracle; mode: open explicit administrative operation. Guarantee strength: protocol across sequential stages, not an all-stage atomic invariant. SRC-1: `src/erasure.rs`.

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

#### RTE-7 — Admit task-list additions

Endpoints/progression: `tasks_update` → task lock → compare expected version → append title/increment version → atomic file write. Owner: caller proposes task, code decides version conflict. Trigger/proposed change: explicit title/version. Admission/rejection: required fields and version match; no human gate within target. Recovery: atomic file writer, caller can reread after conflict; no automatic rollback beyond failed comparison. Guidance: caller title, persists as OBJ-4. Immediate return: new list/version or conflict. Later read-back: subsequent `tasks_read` receives changed list. Delegated visibility: clients of same root; no autonomous delegation. Selection predicate: whole task file, no semantic retrieval. Invalidation/expiry: no removal/expiry on inspected append route. Activation/effect: list mutation wired, task execution outside boundary. Implementation conclusion status: wired; operation conclusion status: uninspected. No answer oracle; open requests. Guarantee strength: invariant for stale-version rejection under task lock/filesystem contract, separate from Git publication. SRC-1: `src/ops.rs`.

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

#### RTE-8 — Install host integration and project guidance

Two distinct admission parts share operator initiation but differ in recovery. Setup writes hook/MCP registrations and skill files, with per-file backups and a remove option. Writeback selects current active project facts/preferences, omits file-origin facts by default, and splices a managed project-file block; `--force` replaces the whole target file. Endpoints: operator CLI → local configuration/project files (OBJ-3) → potential later host startup consumption. Owner: operator chooses target/options; code renders and writes. Trigger/proposed change: explicit setup or writeback. Admission/rejection: file I/O/parse handling, no semantic reviewer and no Git publisher. Recovery: setup backup/remove; writeback has no inspected automatic undo or publication transaction. Guidance: shipped skill/hook instruction and selected fact statements; file content persists. Immediate return: edited-file summary/count or error. Later read-back: writeback exports accumulated knowledge for a future host invocation; static setup skill alone is shipped instruction, not accumulated memory. Delegated visibility: configured external hosts; actual launch/consumption unobserved. Selection predicate: setup target; writeback project/store/all flags and eligible facts. Invalidation/expiry: later rewrite/remove; prior exports are not automatically updated by suppression. Activation/effect: file creation wired, host behavior unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. No answer oracle; open operator requests. SRC-1: `src/setup.rs`, `src/cli.rs`; SRC-2: `skills/mem/SKILL.md`.

> fn backup(path: &Path) -> Result<()> {
>     if path.exists() {
>         let stamp = chrono::Utc::now().format("%Y%m%d%H%M%S");
>         let copy = path.with_extension(format!("{}.mem-backup-{stamp}", path.extension().and_then(|e| e.to_str()).unwrap_or("")));
>         std::fs::copy(path, &copy).map_err(|e| Error::io(path, e))?;
>     }
>     Ok(())
> }
> --- `src/setup.rs:72-79` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let out = match existing {
>         Some(current) => splice_managed_block(&current, &out),
>         None => format!("{WRITEBACK_BEGIN}\n{out}{WRITEBACK_END}\n"),
>     };
>     std::fs::write(&target, &out).map_err(|e| Error::io(&target, e))?;
> --- `src/cli.rs:1841-1845` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-9 — Admit local model selection changes

Endpoints/progression: `models pull` → fastembed asset acquisition/load check → `.models/selected` → later local reranking. Owner: operator names supported family; code/dependency load admits assets. Trigger/proposed change: explicit model pull; environment override can also select family on next invocation. Admission/rejection: supported-name parsing, successful download/load; no quality evaluation gate. Rollback/recovery: failure returns error, another pull or environment selection changes family; no automatic quality rollback. Guidance: model-name option and shipped supported set; weights/cache and selected marker persist. Immediate return: success/error. Later read-back: selected marker/cache changes later CMP-3 selection; this is production machinery, not learned facts. Delegated visibility: dependency downloader; no agent delegation. Selection predicate: environment first, selected marker second, default third. Invalidation/expiry: operator/environment changes, no TTL. Activation/effect: selected-model routing wired; quality/benefit unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. No answer oracle; open administration, not an experimental successor-selection loop. SRC-1: `src/search/laya.rs`, `src/cli.rs`.

#### RTE-10 — Admit source events through ingestion

Endpoints/progression: explicit ingest/backfill or hook sync → source-specific adapters → journal event identity/project metadata → normal or bulk journal append into OBJ-2. Owner: operator or scheduled hook chooses inputs; adapters propose events, journal writer admits serialized records. Trigger/proposed change: local transcript/file ingestion; add source records for retrieval and later consolidation. Admission/rejection: adapter parsing, bulk event-ID deduplication and writer/file checks; no truth review. Recovery: journal recovery/framing handles damaged tails; bulk flush interval and configured fsync bound durability. Guidance: adapter format and source identity; content/provenance persist. Immediate return: ingestion counts or error; hooks can discard child status. Later read-back: raw retrieval and RTE-3 read persisted records. Delegated visibility: local source readers and hook subprocess, not delegated agents. Selection predicate: explicit paths/backfill source/project selectors; bulk deduplication by event ID. Invalidation/expiry: erasure can redact cited records; no general TTL. Activation/effect: journal append wired; downstream behavior unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. No answer oracle; open ingestion requests. Guarantee strength: protocol for adapter/dedup/write/recovery, dependent on filesystem and flush configuration; it does not confer Git publication's atomic snapshot guarantee. SRC-1: `src/ingest.rs`, `src/journal.rs`, `src/cli.rs`, `src/hook.rs`.

> pub fn append(&self, mut event: JournalEvent) -> Result<Option<JournalEvent>> {
>         if !self.seen.lock().insert(event.event_id.clone()) {
>             return Ok(None);
>         }
> --- `src/journal.rs:519-522` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-11 — Compare retrieval against an explicit rubric

Endpoints/progression: operator-supplied rubric file → questions run through RTE-1 with reranking off/on → case checks → side-by-side report. Owner: caller provides expected outcomes; code calculates pass/recall and model components only rank. Computational proposal/decision: search proposes candidates, exact-ID and substring checks decide rubric success. Human contribution: rubric author supplies reference outcomes and operator interprets results. Answer oracle: external rubric's expected fact IDs and required/forbidden strings, used by deterministic checks; source correctness and independence of rubric are uninspected. Operating mode: bounded evaluation set, distinct from open production queries. Improvement trigger: explicit operator evaluation; no automatic successor admission, model update or search-policy revision follows in inspected route. Immediate return: lexical and optional judged-ranker reports. Later read-back: inapplicable, the evaluator returns a report and implements no retention/update loop. Delegated visibility: configured ranker gets ordinary candidate text, no agent delegation. Selection predicate: rubric cases/project and top limit. Invalidation/expiry: inapplicable, temporary report has no managed lifecycle. Activation/effect: scoring wired; actual results/benefit unobserved. Implementation conclusion status: wired; operation conclusion status: uninspected. Admission-change fields: inapplicable, this route reports comparisons without changing production. SRC-1: `src/evaluation.rs`, `src/cli.rs`.

> let recall = case.expected_fact_ids.iter().all(|id| ids.contains(&id.as_str()));
>         let first_expected_rank = ids
>             .iter()
>             .position(|id| case.expected_fact_ids.iter().any(|e| e == id))
>             .map(|i| i + 1);
>         let includes_ok = case.must_include.iter().all(|s| text.contains(&s.to_lowercase()));
>         let excludes_ok = case.must_not_include.iter().all(|s| !text.contains(&s.to_lowercase()));
> --- `src/evaluation.rs:130-136` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### BAP-1 — Retrieved statements enter host context

Consumer: external coding agent. Channel: tool result, hook `additionalContext` or project startup file. Force: information/guidance; the target cannot compel host obedience. Horizon: immediate tool response, subsequent hook invocation or persistent exported file across host sessions. Implementation conclusion status: wired on target emission; operation conclusion status: uninspected for excluded host consumption. Evidence: RTE-1, RTE-5, RTE-8; SRC-1: `src/mcp.rs`, `src/hook.rs`, `src/cli.rs`.

## Annotations

none
