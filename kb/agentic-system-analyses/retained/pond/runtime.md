---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Pond runtime baseline: capture, model-directed recall, SQL escape paths and session restoration at the frozen revision."
run-id: AAS-2026-10-14-pond-7a589a889ca1-01
reviewed-boundary: "0c440e130faf44052d0d896a585e572090079f1f"
---

# Pond runtime report

## Runtime account

### Responsibility and evidence

Pond performs archival capture, retrieval and restoration, not the enclosing model/tool loop. The [boundary](boundary.md) fixes SRC-1 and the whole-system scope. External harnesses write original sessions and decide how later model context is used. Pond supplies codecs, durable tables, selectors, rendered recall and client integrations. It also ships instructions asking models to recall prior work. The ordinary model caller is therefore a host agent; the executor of archive operations is Pond's Rust process, sometimes supervised by a shipped plugin. Session IDs identify archive records, not authenticated caller principals. SRC-1, `packages/pond/src/adapter/mod.rs`, `packages/pond/src/handlers.rs`, `packages/pi-pond/src/tools.ts`.

All implementation conclusions below come from source inspection. No target executable, test, example, model provider or deployment was run. Delivery paths are wired; actual invocation, downstream behavioral activation and benefit remain unobserved. Added implementation coverage under SRC-1 includes the SQL parser gate, embedding loader, batch writer, restore writer, Pi service arguments/tool relay/session-switch path, OpenClaw scoped tool factories and Hermes handlers. Added doctrine coverage includes the complete adapter-development skill. Individual adapter codecs, host internals, external model artifacts and actual installation/release outcomes remain outside this runtime inspection's conclusions.

### Ordinary invocation: capture followed by recall

A representative shipped path starts with Pi's extension loading. Its managed service starts `pond serve --transport stdio --with-sync`, with a configured sync interval and a conditional first-run bootstrap. This is not per-record human approval: only a recorded capture decline removes the bootstrap argument; bootstrap itself refuses to change existing adapter configuration. The server and periodic sync share a store and embedding machinery. The sync loop takes the same per-host store lock as CLI sync, skips a busy cycle, logs errors without terminating serving, and retains last-sync status. These are orchestration rules, not multi-user authorization. SRC-1, `packages/pi-pond/src/service.ts`, `packages/pond/src/main.rs`; see [RT-RTE-adapter-config](#rt-rte-adapter-config) and [RT-RTE-session-capture](#rt-rte-session-capture).

The adapter reads native logs and emits canonical session/message/part events. `IngestValidator` buffers substreams and complete messages, strips caller-supplied core provenance, then calls `upsert_session_batch`. The writer filters existing keys, preserves stored immutable labels when incoming labels disagree, optionally embeds before message append, commits messages and parts, then inserts absent sessions. Table commits are separate; this is not an atomic whole-session transaction. Periodic sync refreshes freshness state and maintains indexes after insertion. A stopped or failed import can leave durable partial progress for a later ingest to complete. Individual codec losslessness is not established merely by this shared pipeline. SRC-1, `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`.

When a later user asks about prior work, shipped Pi tool guidelines ask the host model to call `pond_search`. The model chooses the query, filters and next tool. Pi checks arguments and clamps search limits, relays over MCP, and bounds returned UTF-8 bytes. Pond validates and plans retrieval, then selects one arm: full-text or query embedding plus vector search. A vector request is rejected when embedding is disabled; when enabled but no vectors exist it degrades to full-text. Results and scope counts return through the MCP renderer as transcript text, not a new model-authored answer. The model can then ask for a session page or a message with tool bodies and neighboring messages. The model owns answering and deciding whether evidence suffices; Pond supplies no task-answer oracle. SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`; see [RT-RTE-archive-recall](#rt-rte-archive-recall).

Working-context control here is requested reload, not Pond-controlled compaction: search selects archived material; snippets, session pagination, neighboring-message bounds and plugin byte clipping limit delivery. Static prompt guidelines shape when to reload. Content returned is copied into the host's context, not a dereferenceable pointer with liveness accounting. IDs permit another explicit tool call; omitted content remains in the archive. Host trimming, summarization, sub-agent frames and provider context management are not controlled by this path. SRC-1, `packages/pond/src/handlers.rs`, `packages/pi-pond/src/tools.ts`.

### Material alternates and forcing cases

1. **Cross-corpus SQL instead of search.** MCP, HTTP and CLI all reach the shared SQL implementation. It parses one query or EXPLAIN of a query before opening tables, rejects mutations/multiple statements, and constrains planning. CLI and MCP export modes can write result files; corpus read-only does not mean side-effect-free execution. OpenClaw withholds SQL unless visibility is `all`, but direct Pond SQL and Pi/Hermes projections do not inherit that gate. This challenges both a universal scoping claim and an overly broad read-only claim. SRC-1, `packages/pond/src/sql.rs`, `packages/pond/src/main.rs`, `packages/pond/src/transport.rs`, `packages/openclaw-pond/src/tools.ts`; [RT-RTE-corpus-sql](#rt-rte-corpus-sql).
2. **Read-only tools beside a write-enabled server.** HTTP exposes `/v1/ingest` even though MCP recall tools do not expose ingest. Periodic in-server sync can also change storage while a client only uses recall tools. The Host allowlist gates `/mcp` and `/v1/x/sql`, not search/get/ingest JSON routes. This is a route-specific DNS-rebinding mitigation, not caller authentication or a universal corpus ACL. SRC-1, `packages/pond/src/transport.rs`; [RT-CLM-transport-gates](#rt-clm-transport-gates).
3. **Targeted get after scoped search.** OpenClaw filters search and checks caller context, but passes a get ID without verifying that target's project against the scope. The implementation expressly describes this as policy, not an operator security boundary. Sub-agent contexts receive none of these projected tool factories, but host shell access/direct MCP connections would not be covered by that factory rule. Pi intentionally exposes the whole archive; Hermes source filtering applies to search, not arbitrary SQL or gets. SRC-1, `packages/openclaw-pond/src/tools.ts`, `packages/pi-pond/src/tools.ts`, `packages/hermes-pond/tools.py`; [RT-RTE-openclaw-tools](#rt-rte-openclaw-tools).
4. **Restore rather than transcript read.** CLI `resume` selects lineage, chooses native/foreign fidelity, plans destinations, refuses collisions and writes files. Pi's interactive command can then switch its host session to the restored file. This is a separate write-producing continuation path, not another model recall tool. URL mode refuses the local Pi resume bridge. The no-overwrite gate is executable; cleanup after errors is best effort, not crash-atomic rollback. SRC-1, `packages/pond/src/main.rs`, `packages/pond/src/adapter/mod.rs`, `packages/pi-pond/index.ts`; [RT-RTE-session-restore](#rt-rte-session-restore).

Other shipped entry paths include explicit CLI sync/search/get, HTTP canonical ingest, stdio and streamable-HTTP MCP, Unix-socket serving, scheduler-driven maintenance, optimize/re-embedding, durable store copy/archive import, and the fleet example's independent producers and shared-volume sidecar capture. They do not imply a Pond-owned agent loop. Store copy uses separate table progress and recovery, unlike a restored host session. The fleet worker installs a mutable `@latest` Pi and executes `pi -p "$PI_PROMPT"`; that external agent/provider execution is not evidence of Pond model behavior. SRC-1, `packages/pond/src/main.rs`, `packages/pond/src/schedule.rs`, `packages/pond/src/sessions.rs`, `ops/examples/pi-fleet/worker.sh`.

The forcing set inspects four consequential alternatives, not every codec or deployment. Direct library upsert methods, maintenance and archive imports are not all routed through wire ingestion validation. No guarantee below is extended to arbitrary host callbacks, shell commands, extension code, cloud credentials, native tools or remote worker isolation. Those capabilities depend on the enclosing host and deployment. Product capability, enabled adapter/model configuration, and actual deployed isolation must therefore remain separate. SRC-1, `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`.

### Change admission

Canonical events are admitted by software validation and store rules, not model judgment or per-content human review. This retains session evidence, without establishing a revised instruction or improved model capacity. Configuration changes alter what gets captured: explicit enable/disable and first-run bootstrap are distinct human and software contributions. Adapter capability changes follow a source-native development playbook: writer evidence, fixtures, mapping decisions, implementation, tests and a self-contained PR. The static Rust registry requires source/build changes; it is not runtime-generated extension loading. Review and actual merge/rollback enforcement remain uninspected. Memory transformations and revisions belong to the memory analyst; these records establish their entry and consumer boundaries without claiming that raw archival accumulation learns. SRC-1, `packages/pond/src/adapter/mod.rs`, `skills/pond-add-adapter/SKILL.md`; [RT-RTE-adapter-development](#rt-rte-adapter-development).

## Shared records

### Components

#### RT-CMP-candle-embedder
Label: CandleEmbedder

Source-native `CandleEmbedder` holds an XLM-RoBERTa model, tokenizer and device; the associated lazy loader supplies optional query and message embedding. Representational form: distributed-parametric weights. Storage substrate: HuggingFace file cache, mmaped safetensors and device memory. Default model ID is `intfloat/multilingual-e5-small`; configuration selects another ID. `api.model(id.to_owned())` does not provide an immutable artifact revision here. A fresh fetch for the same ID can therefore resolve different upstream artifacts; local cache and runtime-loaded weights are distinct horizons. No operational parameter-training path is shown in the inspected loader/inference implementation: loading and inference are wired, parameter revision during these calls is absent. External model provenance, exact fetched revision and provider internals are uninspected. Numerical message vectors are derived outputs, not updated model weights. SRC-1, `packages/pond/src/embed.rs`.

> let repo = api.model(id.to_owned());
> --- `packages/pond/src/embed.rs`

> /// inference - one message, one vector, bounded embed cost.
> pub(crate) const MAX_TOKENS: usize = 512;
> --- `packages/pond/src/embed.rs`

### Operative objects

#### RT-OBJ-adapter-config
Label: Adapter configuration

Source-native `[adapters.<name>]` configuration blobs select enabled adapters and source paths. Representational form: symbolic TOML/JSON fields consumed by deterministic discovery/sync rules. Storage substrate: configuration file, then loaded `Config`. This is the current capture grant/configuration, not an ACL over caller access to stored sessions. Bootstrap only acts on a completely unconfigured adapter map. SRC-1, `packages/pond/src/main.rs`.

> if !config.adapters.is_empty() {
>             tracing::info!(
>                 adapter = name,
>                 "bootstrap skipped: adapters already configured"
>             );
>             return false;
>         }
> --- `packages/pond/src/main.rs`

#### RT-OBJ-prompt-guidelines
Label: Pond prompt guidelines

Pi `POND_PROMPT_GUIDELINES` and bundled recall skill are natural-language behavioral instructions, stored in shipped TypeScript/Markdown. The TypeScript array is supplied through registered tool definitions' `promptGuidelines`; the skill is available through installation. Consumption depends on the host/model, not a Rust invariant. The instructions ask for search on prior-work questions, end-of-session reads for latest conclusions, and SQL for tool-body/exact-string queries. They are static shipped policy, not a trace-fed revised method in the inspected path. SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pond/SKILL.md`.

> Use pond_search when the user references past work, a prior session, or a decision made earlier - it searches sessions from every agent and machine, not just this one.
> --- `packages/pi-pond/src/tools.ts`

### Routes

#### RT-RTE-session-capture
Label: Session capture and canonical admission

External harness logs → configured adapter stream or HTTP canonical events → `IngestValidator` → store tables. CLI users, periodic supervisor or HTTP callers trigger it. Rust owns validation, batching and effects; the original human/model/tool mixture is supplied by the harness, not resolved by caller identity. Symbolic events carry natural-language bodies and optional numerical vectors into Lance. SRC-1, `packages/pond/src/sessions.rs`, `packages/pond/src/main.rs`, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI sync summary or HTTP per-row outcomes/error; periodic sync logs completion/error and last-sync state.
- Later read-back: Committed canonical rows reach later search/get/SQL, copy and restore invocations.
- Delegated visibility: Hosts receive rows only through requested recall/restore surfaces; independent fleet workers can contribute logs through shared-volume capture, not Pond-issued task delegation.
- Selection predicate: Enabled adapters, configured paths and freshness plan choose logs; validator event order/schema and store key checks govern admitted rows.
- Invalidation or expiry: Existing message/part keys are filtered; existing session labels win. OpenClaw deletion reconciliation in sync detects rather than purges bytes; maintenance is separate.
- Activation or effect: Durable archive insertion and optional message embedding; downstream host behavior from those rows is unobserved.
- Evidence limits: Shared seams were inspected, not every codec's field mapping or actual cloud concurrency behavior; partial commits are possible.

Admission: adapters/wire callers propose records; software validates and admits, can reject malformed events, and can discard conflicting labels while retaining new rows. Starting sync is not content approval. There is no task-answer oracle; validation references schema/order/keys, not expected task answers. Operating mode is open archival ingestion, with periodic or explicit triggers. Recovery is additive retry of missing rows, not rollback of the completed batch history. The guidance is the canonical schema and core provenance ownership; records and provenance persist. This route does not itself formulate or revise theories.

> options.remove("pond");
>             stamp_bytes = ingest_host_stamp_bytes(options);
> --- `packages/pond/src/sessions.rs`

> let (_messages_appended, _parts_appended) = tokio::try_join!(
>             append_messages,
>             self.append_filtered(
>                 Table::Parts,
>                 part_stream,
>                 Self::part_keep(existing_part_pks.clone()),
>             ),
>         )?;
> --- `packages/pond/src/sessions.rs`

#### RT-RTE-archive-recall
Label: Requested archive recall

Host model/user → Pi, Hermes, direct MCP/HTTP or CLI search → Rust planner/store → rendered snippets → explicit get/session/message follow-up → host consumer. Host model owns next-step selection and answering; Pond code owns query execution and pagination. State is query/filter/ID plus retained corpus, not a Pond reasoning episode. SRC-1, `packages/pond/src/handlers.rs`, `packages/pond/src/transport.rs`, `packages/pi-pond/src/tools.ts`, `packages/hermes-pond/tools.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked/grouped snippets or paged transcript/message bodies; plugins wrap errors and bound output text.
- Later read-back: A later request selects prior-session content by query or returned IDs; ordinary recall does not write a revised artifact to Pond.
- Delegated visibility: inapplicable — Pond returns to its requesting host; it does not dispatch a reasoning worker. Returned sub-agent-session content is archived history, not live delegated execution.
- Selection predicate: Query, retrieval mode, limits and optional project/session/source/date filters; requested get IDs, page anchors and neighbor counts select subsequent material.
- Invalidation or expiry: Per-call context is released; archive reachability persists. Pi clips returned text at its response byte budget and requests narrower queries for omitted material.
- Activation or effect: Transcript text reaches the host tool result; compliance with recall guidelines and changed answers remain unobserved.
- Evidence limits: No supplied host trace shows when a model calls, interprets or acts on this material; search is not completeness or truth certification.

Decision roles: foreground model/user requests; deterministic planner selects the retrieval arm and results; model/human interprets. Answer oracle: none supplied by this path. Operating mode: open recall requests, not evaluation curriculum. Runtime-client controls include search limits, byte bounding, pagination and error envelopes. The embedding component is [RT-CMP-candle-embedder](#rt-cmp-candle-embedder); its input truncation limits semantic representation even when full original bodies remain separately retrievable.

> // A `vector` request is refused when embedding is off on this instance,
>         // and degrades to `fts` when it is on but nothing is embedded yet.
> --- `packages/pond/src/handlers.rs`

> return `${clipped}\n\n[pond: response truncated to ${RESPONSE_MAX_BYTES} bytes; narrow the query or lower limit]`;
> --- `packages/pi-pond/src/tools.ts`

#### RT-RTE-corpus-sql
Label: Corpus SQL escape path

MCP/HTTP `pond_sql` or CLI `pond sql` → shared SQL precheck/parser → table opening/DataFusion planner → rows/text or exported results. Rust owns query admission and execution, caller chooses query/mode/timeout. This broadens recall to joins, aggregates and tool bodies beyond ordinary search. SRC-1, `packages/pond/src/sql.rs`, `packages/pond/src/handlers.rs`, `packages/pond/src/main.rs`, `packages/pond/src/transport.rs`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Capped inline results, typed errors, or export metadata/path depending on surface and mode.
- Later read-back: Queries read durable tables; exported files can be read later by callers, but their subsequent consumption is uninspected.
- Delegated visibility: Requesting host receives corpus-wide rows unless its own projection restricts tool availability; no worker dispatch.
- Selection predicate: Caller SQL AST plus read-only grammar/planning checks; optional SQL predicates rather than search scoping.
- Invalidation or expiry: Query timeout and inline row caps bound work/results; exported-file lifetime is not determined by the inspected recall path.
- Activation or effect: Corpus reads and optional export file writes; no admitted corpus mutation through this SQL gate.
- Evidence limits: External DataFusion/Lance behavior is not independently verified; read-only does not establish resource isolation or authorization.

Guarantee owner: shared SQL implementation. Enforcement: `parse_and_gate`, precheck before table access, and planning options disallowing DDL/DML. Guarantee strength: invariant for accepted grammar in these routed entry paths, dependent on parser/planner semantics. Covered paths: inspected CLI, HTTP and MCP SQL. Alternates: HTTP ingest, sync, library write APIs and archive imports remain write-capable; host shell execution is not covered. Export writes are not corpus mutation. Decision roles: caller proposes query, code vetoes grammar; no per-query human approval or task-answer oracle; open analytics mode.

> "pond's SQL surface is read-only: only a single SELECT/WITH (or EXPLAIN of one) is \
>          allowed (no INSERT/UPDATE/DELETE/CREATE/DROP/COPY/SET)"
> --- `packages/pond/src/sql.rs`

#### RT-RTE-openclaw-tools
Label: OpenClaw projected recall policy

OpenClaw tool context → projected factory/context resolver → allowed search/get/SQL request → Pond MCP. Plugin code decides availability and search filters; the model chooses requests after registration. Source-agent restriction is a search filter, not global authorization. SRC-1, `packages/openclaw-pond/src/tools.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Pond text wrapped as ok/error/forbidden, or no tool for a sub-agent context.
- Later read-back: Selected archived sessions/messages reach the calling host; raw get IDs are passed without per-target scope verification.
- Delegated visibility: Sub-agent contexts are refused these factory-produced tools; direct MCP, shell and other host capabilities are not fenced by this rule.
- Selection predicate: Resolved caller scope and combined project filter on search; valid context gate on gets; visibility must be `all` for SQL.
- Invalidation or expiry: Scope is resolved at execution; registered sub-agent factories return null. Archive data is not expired by that policy.
- Activation or effect: Search clamps and tool withholding are implemented; arbitrary get target confinement is not supplied by this mechanism.
- Evidence limits: Host context correctness and actual grant set/isolation are external; inspected resolver call sites do not prove all host principal mappings.

Guarantee owner: OpenClaw plugin. Enforcement point: factory/execution checks, not the store. Guarantee strength: policy. Required external contract: host supplies accurate tool context/config and prevents bypass if isolation is desired. Covered path: these projected factories only. Answer oracle: none; operating mode: open recall with deterministic policy gates.

> // Gets are targeted follow-ups to a scoped search; enforce the same
>   // ctx/leaf/fail-closed gate. The get tools have no project filter and their
>   // MCP output is text, so per-target scope is not re-verified server-side -
>   // this is deliberate (policy, not a security boundary against the operator).
> --- `packages/openclaw-pond/src/tools.ts`

#### RT-RTE-session-restore
Label: Session restoration and host continuation

CLI/user-selected session ID → complete supported lineage → adapter serialization → destination planning/write → CLI report; Pi local interactive command then passes the file to `ctx.switchSession`. `run_resume` owns fidelity and filesystem effects; Pi owns the host handoff, host owns actual continuation. Representation changes from canonical records to native symbolic session files carrying text. SRC-1, `packages/pond/src/main.rs`, `packages/pond/src/adapter/mod.rs`, `packages/pi-pond/index.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Written paths and actual per-session fidelity, or typed not-found/unsupported/too-deep/collision/write-failed outcome; Pi notifies and switches on successful local results.
- Later read-back: A restored file is passed to a later host session context; successful host parse and continuation are unobserved.
- Delegated visibility: Included supported children are restored together; this does not spawn them as live workers. Pi URL mode refuses the local handoff.
- Selection predicate: Requested session and one supported lineage level; same-origin requests native replay, foreign requests reconstruction, actual adapter output determines reported fidelity.
- Invalidation or expiry: Existing destination paths cause refusal; lineage that would require grandchild restoration is refused rather than partially restored.
- Activation or effect: Filesystem write and Pi session-switch request; no demonstrated resumed model action.
- Evidence limits: Individual codec round-trip fidelity was not audited; crash recovery, directory races and host semantics are not proven by the shared writer.

Admission: operator chooses session/target; code selects fidelity, rejects unsupported lineage/collisions and admits files. Guidance: source origin, codec and destination rules; files persist. No task-answer oracle; open restoration mode. Recovery: retry elsewhere or reuse existing files; shared writer attempts removal of files/directories created by a failed batch, ignoring cleanup errors. Guarantee owner/enforcement: shared writer's `create_new(true)` prevents overwriting final destinations; guarantee strength: invariant for that file-open operation under filesystem semantics. Whole-batch cleanup is best effort, not a power-loss-safe atomic transaction. Host switching and foreign fidelity are separate guarantees, not consequences of no-overwrite.

> let mut handle = std::fs::OpenOptions::new()
>                 .write(true)
>                 .create_new(true)
>                 .open(&dest)
> --- `packages/pond/src/adapter/mod.rs`

> for path in &written {
>         let _ = std::fs::remove_file(path);
>     }
> --- `packages/pond/src/adapter/mod.rs`

#### RT-RTE-adapter-config
Label: Capture configuration admission

CLI enable/disable or managed Pi first-run bootstrap → known adapter lookup/discovery → persisted adapter configuration → subsequent sync. Rust config code owns writes; explicit operator commands and plugin defaults are different proposal principals. SRC-1, `packages/pond/src/main.rs`, `packages/pi-pond/src/service.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CLI enabled/disabled report; bootstrap logs success or warning and allows degraded serving after failure.
- Later read-back: Later server/sync loads persisted adapter paths and enabled flags.
- Delegated visibility: inapplicable — configuration governs producer capture, not delegated task contexts.
- Selection predicate: Known factory name, existing path or discovered candidate; bootstrap only if no adapter entries exist.
- Invalidation or expiry: Disable changes future capture; it does not erase archived content. Existing adapter map prevents bootstrap changes.
- Activation or effect: Configuration can change future ingestion eligibility; real capture execution remains unobserved.
- Evidence limits: Discovery of every platform/client and actual user consent behavior are not established by the inspected call seams.

Admission: human explicit commands/manual config can accept or disable; software bootstrap can enable a discovered source without an interactive approval if its preconditions hold. Pi's recorded decline removes bootstrap. No expected-answer oracle; open setup/maintenance mode. Rejection: unknown/not-detected adapter, unreadable config or preexisting map; recovery: fix config, explicit path or disable. Guidance is source discovery plus bootstrap policy; symbolic configuration persists. This is operational configuration change, not automatic product-source modification.

> ...(config.captureConsent === "declined" ? [] : ["--bootstrap", "pi-coding-agent"]),
> --- `packages/pi-pond/src/service.ts`

#### RT-RTE-adapter-development
Label: Adapter capability development

Developer problem → prescribed writer investigation and sandbox fixture → decision table → codec/registry/test/docs PR → repository admission. The playbook is natural-language guidance; compiled Rust registry entries are symbolic capability wiring. SRC-1, `skills/pond-add-adapter/SKILL.md`, `packages/pond/src/adapter/mod.rs`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Requested self-contained PR containing specification, fixture, implementation, tests and documentation.
- Later read-back: Merged/built adapter source would be used by discovery, ingest and restore; actual merge/build/release is uninspected.
- Delegated visibility: inapplicable — the playbook may be followed by a developer or coding agent, but does not itself dispatch workers.
- Selection predicate: New/reworked format need; writer evidence and captured fixture ground mapping choices, prescribed conformance tests check them.
- Invalidation or expiry: Last-verified documentation is updated when touched; passive drift handling is prescribed. Source rollback/merge rejection mechanics are uninspected.
- Activation or effect: Static registry determines known compiled adapters; playbook compliance and delivered new capability are not observed.
- Evidence limits: This is doctrine/design evidence of a development procedure, not verified CI success, human approval enforcement or autonomous improvement.

Admission: developer/agent proposes; PR review and repository merge would decide, but exact veto ownership/protection is uninspected. Human account login may be needed for fixtures; computation alone is not established. Reference outcome/oracle: the prescribed upstream writer and sandbox captures provide expected field/round-trip behavior, not an answer oracle for later user questions. Operating mode: bounded conformance work with fixture comparisons; trigger: add/rework adapter. Guidance says lossless capture, no synthesis and honest restore refusal. It persists specs/fixtures/tests/source; rollback of admitted product changes is uninspected. The procedure asks for mapping decisions and tests, but this runtime inspection does not establish a formulated-theory criticism/iteration route or self-improvement attribution.

> Ship both in ONE self-contained PR: spec doc + fixture + adapter + tests + doc rows.
> --- `skills/pond-add-adapter/SKILL.md`

> /// The static, ordered registry of every adapter pond knows. A new adapter
> /// adds one `&Factory` here plus one file under `src/adapter/`. Order is the
> /// order discovery presents to the operator.
> --- `packages/pond/src/adapter/mod.rs`

### Claims

#### RT-CLM-transport-gates
Label: Route-specific HTTP Host gates

Claimed operation: Host checks protect MCP and arbitrary SQL against DNS rebinding; they do not authenticate archive callers or gate every JSON endpoint. Implementation owner is the transport router and rmcp configuration. Guarantee strength: protocol; implementation conclusion status: wired; operation conclusion status: uninspected. Covered paths: `/mcp`, `/v1/x/sql`; alternate paths: unguarded-by-this-check search/get/ingest routes, stdio and local CLI. Required external contract: network/socket exposure and permissions suited to single-user deployment, plus rmcp Host-check semantics. Actual deployed isolation/IAM is uninspected. SRC-1, `packages/pond/src/transport.rs`.

> /// those two routes with 403 until that name is listed; `/v1/x/sql` shares
>     /// the gate because it reads arbitrary corpus rows. The other `/v1/*`
>     /// routes carry no such check.
> --- `packages/pond/src/transport.rs`

#### RT-CLM-ingest-recovery
Label: Per-table durability and convergent retry

Claimed operation: messages/parts can commit before their session row; later ingest can complete missing durable state. Owner: store writer and transport shutdown. Guarantee strength: best effort at the session/retry horizon, relying on atomic Lance commits, available source records and a later successful retry. Implementation conclusion status: wired; operation conclusion status: uninspected. This is not whole-session atomicity or complete summary accounting: pipeline comments note a failed mid-flush adapter can lose its committed counts from the error summary. Covered path: shared ingestion; durable copy also has separate table progression but is not the same validation route. SRC-1, `packages/pond/src/sessions.rs`, `packages/pond/src/transport.rs`, `packages/pond/src/main.rs`.

> /// written yet. Every Lance commit is atomic and the next ingest of that
>     /// session rewrites the missing row, so the store converges.
> --- `packages/pond/src/transport.rs`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-recall-guidance
Label: Recall instructions to host model

Consumer: host model receiving registered Pi tool guidelines or installed recall skill. Channel: tool definition prompt fields and skill text. Force: advisory natural-language instructions asking recall first, latest-state reads and bounded interpretations; no demonstrated compliance. Horizon: subsequent host turns/sessions when those shipped instructions are loaded. This differs from recall delivery: the policy shapes selection, while returned historical text supplies task evidence. SRC-1, `packages/pi-pond/src/tools.ts`, `packages/pond/SKILL.md`; operative content is [RT-OBJ-prompt-guidelines](#rt-obj-prompt-guidelines).

> promptSnippet: POND_PROMPT_SNIPPET,
>       promptGuidelines: POND_PROMPT_GUIDELINES,
> --- `packages/pi-pond/src/tools.ts`

#### RT-BAP-session-switch
Label: Restored file into host session

Consumer: Pi host session loader. Channel: `ctx.switchSession` with a local restored session-file path. Force: executable session-switch request, distinct from advisory tool-result evidence. Horizon: replacement host session and possible later continuation; host load/operation is unobserved. It depends on [RT-RTE-session-restore](#rt-rte-session-restore), not on model compliance with recall instructions. SRC-1, `packages/pi-pond/index.ts`.

> await ctx.switchSession(outcome.sessionFile, {
>     withSession: async (fresh) => {
>       fresh.ui.notify(note, "info");
>     },
>   });
> --- `packages/pi-pond/index.ts`

## Annotations

none
