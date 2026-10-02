---
type: types/agentic-system-runtime-report.md
description: "Runtime baseline of Instinctual Memory's Git-backed memory capture, retrieval, and change paths at the frozen repository commit"
run-id: AAS-2026-09-30-instinctual-memory-02
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# Instinctual Memory runtime report

## Runtime account

### Traced invocation and control surface

The ordinary automatic path is the Claude Code hook integration installed by `mem setup`: Claude Code invokes `mem hook start` at session start, `mem hook prompt` for each user prompt, and `mem hook end` at session end. The hook executable resolves the store from the working directory, then `MEM_ROOT`, the nearest local store, or the global store. At start it emits the user's preference facts and instructions for finding memory. At prompt time it searches curated facts only, lexically, and emits up to six facts matching the prompt's content words; short prompts and slash commands are skipped. Hook output is Claude-specific `additionalContext`. The host decides whether to install and invoke hooks; `mem` owns lookup and output. The host model's attention to or use of the injected text is outside the boundary.

> const PROMPT_FACTS: usize = 6;
> --- `src/hook.rs:25-25` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

At session end the hook starts synchronization in the background. Synchronization backfills the completed transcript, then consolidates when the configured threshold of new journal events is reached and a model key is available. The default threshold is 200; `MEM_AUTO_CONSOLIDATE=0` disables automatic consolidation. Errors in hooks are swallowed and the process exits successfully, so a missing store, malformed payload, or internal failure prevents context or synchronization but does not block the host session.

> A hook never fails the session: with no store, a bad payload, or any
> //! error, it prints nothing and exits 0.
> --- `src/hook.rs:13-14` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The alternate direct path is `mem serve --stdio`, an MCP server registered for Claude Code and Codex by setup, or explicitly by another MCP client. It uses the same operation layer and memory root. The server accepts JSON-RPC over standard input and returns tool results over standard output. Tools expose search, status, read, history, task-list operations, and validated remember/correct/forget changes. The tool caller controls whether and when to call them; the memory process applies the requested operation.

> One JSON-RPC message per line on stdin.
> --- `src/mcp.rs:3-3` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

> let result = ops::execute(root, scope_id, session_id, name, &args);
> --- `src/mcp.rs:186-186` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Other equivalent paths materially affect the limits of guarantees:

- `mem search`, `read`, `history`, `change`, `consolidate`, `ingest`, `backfill`, `erase`, and `writeback` are direct CLI routes. `mem shell` dispatches operations from a line-oriented interface; it is not a shell escape hatch. These routes do not depend on an MCP client or Claude hooks.
- `mem serve --http` exposes the operation layer through HTTP and server-sent events. Its listener rejects non-loopback addresses, but the inspected server has no request authentication. Any local process able to reach the bound port can request the exposed operations.
- The Rust library exposes core modules and functions to embedding code. The inspected crate does not establish restrictions on a caller embedding it or on host-process access to the store.
- Claude hooks and MCP are the shipped integrations examined here. There is no evidence in the inspected implementation that hooks are installed in Codex or OpenCode; Codex integration is MCP, and OpenCode can use the documented manual MCP path. Other host callbacks, extensions, subprocesses, remote workers, and manually orchestrated graph execution remain outside the inspected implementation boundary or are controlled by the host.

### Runtime boundaries and state progression

The journal is an append-only JSONL event store with idempotent ingestion. Consolidation reads events after its Git-stored checkpoint in bounded batches, filters by scope, extracts candidate facts using either rules or an external chat-completion model, applies code checks, then publishes changed entity files, the regenerated index, dispositions, and checkpoint as a Git commit. The `auto` extractor chooses the LLM path when an API key is configured and rules otherwise. For the LLM path, only user-authored words and memory files are candidates; assistant turns and harness-injected material are excluded. A proposed fact must point to an event in the batch and pass evidence checks, including matching its evidence text to the cited source event. No expected factual answer is supplied: the evidence check tests traceability and format, not whether the proposition is true or useful.

> // Only the user's own words and memory files can carry durable facts.
> --- `src/consolidate.rs:631-631` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Search resolves a published Git revision once, builds eligible facts from that pinned tree, scans the journal, combines results, and optionally reranks. Search filters suppressed, retracted, deleted, expired, and superseded material according to the selected operation and audience. Reranking prefers the configured remote JEV service when a key is present, then a cached local cross-encoder, then the lexical baseline. The automatic prompt hook disables reranking and searches facts only. Provider output affects ordering; it does not itself publish memory changes.

A live remember/correct/forget request is a separate change path. The requesting agent or user supplies the proposed fact or target; code validates the request and resulting memory structures. The change path records a durable intent, builds a change set including the entity and index (and controls for forget), validates the candidate tree, and advances the published memory ref with compare-and-swap. A concurrent writer causes a conflict that requires rereading and retrying. A repeated request ID with identical content replays its receipt; reuse with different content conflicts. A successful request returns the new revision and target ID. Correct marks the old fact superseded; forget retracts and suppresses it for future retrieval but preserves its history. Erasure is a distinct explicit CLI operation that redacts source events and rewrites the memory branch history, including pruning unreachable objects; the inspected implementation offers no reversal operation for that rewrite.

> // Compare-and-swap on the published branch.
> --- `src/repo.rs:312-312` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Writeback reads active facts from a published revision and writes a project-specific subset into a managed block in a destination `AGENTS.md` or another selected file. It preserves text outside the managed block unless `--force` is used. The output is ordinary natural-language material for a host to load; this repository cannot establish the host's precedence rules or whether the host model follows it.

`mem setup` is a separate capability-admission path. The user explicitly invokes the CLI. Setup edits Claude configuration to add start/prompt/end hooks, registers its MCP server, installs a `/mem` skill, and can register MCP for Codex. It backs up edited configuration files and supports removal. This changes how a host can access memory; it does not configure the host's permissions or enforce subsequent host behavior. Deployment of hooks/MCP is therefore an explicit operator action, not a property of an unconfigured installation.

### No dynamic check planned

Checks considered: an MCP stdio search/read round trip, a remember/correct/forget publication and retry, and hook context output. Static tracing was sufficient to identify their dispatch, operation, validation, persistence, and return paths at this boundary. No dynamic check was selected or run because no configured store, agent host, model credentials, or deployed environment is supplied, and exercising mutation would require creating a fixture store. This prevents claims about actual installed-host invocation, observed output, service response, or successful live deployment. No probe evidence is declared below.

## Probe evidence

none

## Shared records

### Components

#### RT-CMP-1 — Consolidation chat model

Source-native identity: model selected by `MEM_LLM_MODEL`, default `anthropic/claude-haiku-4.5`, called through `MEM_LLM_BASE_URL` or the default OpenRouter-compatible chat completions endpoint. The API accepts a model identifier and endpoint from environment configuration; no immutable provider model revision is pinned by the inspected code. Exact provider-side model resolution and any provider-side weight changes are uninspected. No parameter update is made by the operation: requests set temperature to zero and request JSON output. API key availability is a deployment condition and its value was not inspected. Evidence: `SRC-1` `src/consolidate.rs`, `src/jev.rs`, and `Cargo.toml`.

Distributed-parametric fixity: parameter changes during operation: `inapplicable` to the inspected client, which sends requests but does not train the model. Exact-version pinning: `absent` in the inspected client configuration; the configured model name can resolve to provider-managed versions. Mutable endpoint resolution: `claimed` by environment-configurable endpoint and provider alias; live resolution was not inspected. These findings concern the client's configuration surface, not provider internals.

#### RT-CMP-2 — JEV remote reranker

Source-native identity: TypeSafe JEV model, selected by `MEM_JEV_MODEL` or `JEV_MODEL`, default `~typesafe/jev-latest`, requested from a configurable Decisions API endpoint. Each candidate is sent with the query for a relevance decision. Query and candidate text leave the local process on this path; provider retention and actual model resolution are uninspected. The alias and endpoint are mutable configuration; no immutable model revision is pinned. No parameter update is made by the inspected operation. Evidence: `SRC-1` `src/jev.rs` and `src/search/rerank.rs`.

Distributed-parametric fixity: parameter changes during operation: `inapplicable` to the inspected client. Exact-version pinning: `absent`; the default is a moving alias and the configured endpoint controls resolution. Mutable endpoint resolution: `claimed` by environment configuration; provider-side routing is uninspected. API key value was not inspected.

#### RT-CMP-3 — Local fastembed cross-encoder

Source-native identity: one of the `fastembed` reranker models selected by `MEM_LAYA_MODEL` or the store's `models/selected` marker, default `bge-reranker-base`. The model is downloaded into the memory root's `.models` cache when explicitly pulled; ordinary search loads it only when its model directory is already cached and falls back otherwise. The inspected code identifies model names but does not pin or verify a revision digest. Once loaded, the runtime invokes inference without an update path. Evidence: `SRC-1` `Cargo.toml` and `src/search/laya.rs`.

Distributed-parametric fixity: parameter changes during operation: `inapplicable` to the inspected inference client. Exact-version pinning: `uninspected` at weight-file level; the selected model name is recorded, but no model digest or immutable upstream revision is retained in the inspected selection marker. Mutable endpoint resolution: `inapplicable` during ordinary inference from an existing local cache; download-time source resolution was not inspected here. This says nothing about other memory updates occurring through the journal or Git store.

### Operative objects

#### RT-OBJ-1 — Ingestion journal

Append-only JSONL events grouped in journal files, carrying source, role, scope, session, project, timestamps and message content. Ingestion deduplicates stable event identities. It is the input substrate for consolidation and direct journal search; it is not itself the curated fact store. Representational form: structured text/JSON. Evidence: `SRC-1` `src/journal.rs`, `src/ingest.rs`, and `src/cli.rs`.

#### RT-OBJ-2 — Published memory tree

The `memory.git` bare repository holds entity Markdown with fact frontmatter, `INDEX.md`, controls, checkpoint, dispositions, receipts and change intents. Search reads a selected Git revision; writes publish validated trees on the memory ref. Representational form: natural-language fact statements plus structured Markdown/YAML/JSON. Evidence: `SRC-1` `src/repo.rs`, `src/fact.rs`, `src/entity.rs`, and `src/consolidate.rs`.

#### RT-OBJ-3 — Host-provided context and project writeback

Hook context is emitted as Claude Code `additionalContext`; `mem writeback` writes generated facts inside a managed block in an instruction file such as `AGENTS.md`. These are natural-language inputs to host systems. Their delivery is wired by the integration, while host interpretation and behavioral effect are uninspected. Evidence: `SRC-1` `src/hook.rs`, `src/cli.rs`, `src/setup.rs`, and `skills/mem/SKILL.md`.

### Routes

#### RT-RTE-1 — Claude session and prompt hooks

- Trigger and principal: Claude Code calls hooks configured by `mem setup`; the user prompt supplies the prompt text. Host owns scheduling; `mem` owns store resolution, lexical matching, and rendering.
- Progression and context: start reads status and `pref_user`; prompt searches curated facts with a minimum meaningful-word overlap and emits at most six. Short prompts and slash commands return no injected context. The end hook launches backfill and may consolidate after the event threshold. Context is the host hook payload plus local store and current prompt; state is read from the published Git tree and journal.
- Executor, effects, persistence: the `mem` process performs lookup; prompt/start are read-only. End may append source events and may invoke consolidation, which can publish a new tree. Immediate return: hook-specific JSON `additionalContext`, or no output on no match/error. Later read-back: only facts that later become eligible and match a future prompt are automatically returned; journal events alone are not included by the prompt hook. Delegated visibility: `mem` controls the emitted content; host consumption is not visible to this repository. Selection predicate: prompt lexical matching, two shared meaningful words (one for one-word content), facts-only, limit six; session start preference lookup. Invalidation/expiry: fact eligibility and controls filter returned facts; no hook-specific cache. Activation/effect: implementation conclusion status `wired` for context output; operation status `uninspected` for whether the host/model used it or changed behavior. Evidence limit: no host session or deployed hook was inspected. `SRC-1` `src/hook.rs` and `src/setup.rs`.
- Runtime-client controls: setup installs configuration and supplies a 10-second timeout; hook failures fail open and exit zero. Guarantee owner is hook code, enforcement point is hook error handling, strength is `protocol` for fail-open hook result; covered path is these hook handlers only. MCP, CLI, HTTP, and other host operations are not covered by this guarantee.
- Change admission in the end phase: trigger is host session end plus the configured event threshold and model-key condition. Backfill proposes events; configured rules or LLM propose candidate facts; code applies source/evidence checks and domain validation; Git compare-and-swap admits the batch. The host/user can choose whether setup is installed and can disable automatic consolidation, but there is no per-fact human approval gate in this route. Rejected facts are omitted/quarantined; batch errors prevent publication; recovery is rerun from the stored checkpoint/receipt path. Answer oracle: none for factual correctness; code checks provenance and constraints, not expected truth. Operating mode: open session collection followed by bounded event batches, not a supplied curriculum. Guidance: bundled `/mem` skill and extractor system prompt; the skill guides memory search/change, and the extractor prompt guides fact proposals. Persisted material is source events, extracted fact statements and their evidence references, plus dispositions and checkpoint. No later route reading a retained history of criticism was identified. Evidence: `SRC-1` `src/hook.rs`, `src/consolidate.rs`, `src/repo.rs`, and `skills/mem/SKILL.md`.

#### RT-RTE-2 — MCP operation request

- Trigger and principal: an MCP client calls one of the declared tools; the external agent/client selects tool and arguments. `mem` dispatches to `ops::execute` against the chosen store, scope and session.
- Progression and effects: search returns matching facts and journal events, status returns counts/configuration, read/history return selected records, and `memory_request_change` invokes validated memory change. Task tools operate on the versioned task file. Immediate return: MCP text content with the operation payload and error flag. Later read-back: a successful memory change can be found through later search/read/history calls using the updated published tree; the caller must request those operations. Delegated visibility: the client receives the returned payload; downstream agent visibility/use is outside the boundary. Selection predicate: caller-supplied tool and parameters, then operation-specific filters. Invalidation/expiry: change operations use current Git state and fact eligibility; task updates require matching expected version. Activation/effect: implementation conclusion status `wired`; whether an agent uses results is `uninspected`. Evidence limit: no live MCP client or credentials were supplied. `SRC-1` `src/mcp.rs`, `src/ops.rs`, and `src/change.rs`.
- Admission roles for `memory_request_change`: agent or user proposes kind/entity/fact/target; `mem` validation and `DomainValidator` decide admissibility and can veto invalid paths or content; Git compare-and-swap can veto a stale base. No independent model or human approver is required by the implementation. Recovery uses the durable intent and idempotent request ID; conflicts require reread/reconcile/retry. Answer oracle: none for fact truth; validators provide structural and domain constraints only. Operating mode: open request. Guidance: the caller's request and bundled `/mem` skill can shape the proposal; the operation itself does not load the skill or establish that the caller did. Persisted result: fact/entity/control changes and receipt in the Git tree; the intent is operational recovery state. Evidence: `SRC-1` `src/mcp.rs`, `src/change.rs`, `src/repo.rs`, and `src/validate.rs`.
- Guarantee: `memory_request_change` is a validated, atomic publication protocol for the covered MCP operation path. It covers the MCP dispatcher only insofar as it reaches the shared operation layer; direct library writes and external edits are not shown to be constrained by MCP. It does not guarantee truth, host use, or durability properties of external providers.

#### RT-RTE-3 — Direct CLI, shell, and loopback HTTP

- Trigger and principal: an operator or host process invokes the `mem` CLI, enters a supported `mem shell` command, or sends an HTTP operation request to the loopback server. The caller selects the command and arguments; shared operation functions perform searches and changes. HTTP can be reached by any local process able to connect to the port; no authentication was found in the inspected request handler.
- Immediate return: CLI JSON/text/stream output, shell-rendered output, or HTTP JSON plus an operation ID and optional server-sent progress/result. Later read-back: published memory changes are available through later reads/searches; caller controls whether to perform them. Delegated visibility: outputs go to the invoking process or client; no remote principal identity or downstream use is tracked. Selection predicate: explicit command/operation and its arguments. Invalidation/expiry: current Git revision, fact eligibility, and operation-specific checks; HTTP operation result cache has process lifetime. Activation/effect: implementation conclusion status `wired` for operation dispatch; downstream behavior `uninspected`. Evidence limit: no deployed server or invocation was observed. `SRC-1` `src/cli.rs`, `src/shell.rs`, `src/http_serve.rs`, and `src/ops.rs`.
- Admission roles for explicit change, consolidation, erase, and writeback commands are specified on their respective routes below. Direct CLI and shell provide equivalent capabilities to MCP callers; the MCP transport is not the enforcement boundary. HTTP is loopback-only by bind-time check, a deployment boundary with no user authentication in the handler. Evidence: `SRC-1` `src/cli.rs`, `src/http_serve.rs`, `src/change.rs`, and `src/repo.rs`.

#### RT-RTE-4 — Manual ingestion and consolidation

- Trigger and principal: operator runs ingest/backfill/consolidate directly; alternatively the session-end hook triggers sync and thresholded consolidation. Inputs include recognized session exports, project instruction files, and other supported formats. Adapter selection is explicit or based on format/path detection. `mem` appends events to the journal; consolidation consumes events after checkpoint, scoped and bounded by `high_water`.
- Candidate selection and decision roles: rules or the configured LLM propose facts; existing entities and the new event batch are input context. `check_llm_fact`, extraction disposition logic, and `DomainValidator` decide acceptance and can reject candidates; no human per-fact approval is required. Candidate admission is not a truth oracle. No critique of a retained theory is specified by this route: a rejected candidate is dispositioned, but the implementation does not retain a content-directed criticism that a later extraction round is required to use.
- Operating mode and guidance: operator requests are open-ended ingests; consolidation processes bounded batches, not an explicit curriculum. The rules extractor or LLM system prompt guides extraction. Existing facts are supplied to deduplicate or place candidates, but this alone does not demonstrate that their content is criticized. Persisted material includes original journal inputs, accepted facts with sources, rejected/quarantined dispositions, checkpoint and Git commit. Immediate return: command report/status and new Git revision when changes publish. Later read-back: eligible facts are accessible to search/read and future prompt hooks; journal material is accessible through general search/read but not automatic facts-only prompt context. Delegated visibility: CLI caller receives report; future consumers query the resulting store. Selection predicate: source adapter, scope, checkpoint window, high-water bound, extractor selection and fact validators. Invalidation/expiry: source-file refresh may retire outdated file-derived facts; corrections and forget controls affect retrieval; checkpoint advances with batch. Activation/effect: implementation conclusion status `wired`; later consumer behavior `uninspected`. Evidence limit: no real event set or provider operation was supplied. `SRC-1` `src/ingest.rs`, `src/consolidate.rs`, `src/cli.rs`, and `src/repo.rs`.
- Admission and recovery: batches publish entity changes, index, dispositions and checkpoint through the same validated CAS repository mechanism. If generation or validation fails, the batch does not publish; retry continues from persisted checkpoint/receipt state. The operator can select rules instead of LLM, set scope/high-water, or not run consolidation. Answer oracle: none supplied for factual correctness; evidence matching and domain validation are local checks, not expected answers. No formulated criticism-and-revision loop was identified by this runtime pass. Theory-builder conditions 1–4: `uninspected` as a theory route; the implementation identifies extracted factual propositions, but the runtime evidence does not establish a consumed theory, content-directed criticism, and resulting iteration. This prevents a positive runtime finding that consolidation is a theory builder; the epistemic and memory lenses may assess particular retained content separately.

#### RT-RTE-5 — Explicit remember, correct, forget, and erase

- Trigger and principal: user or agent explicitly invokes MCP `memory_request_change` or CLI `mem change` for remember/correct/forget; erase is an explicit CLI command. The caller proposes the new statement, target, and optional reason. `mem` validates request ID, entity and fact structure, builds the changed entity/index/controls, records an intent, and publishes through validated Git CAS. Erase uses separate history-rewrite code to scrub matching material from entities, journal events, intents and branch commits.
- Admission roles and veto: caller proposes; request/domain validators and path controls decide whether to admit and can veto malformed or invalid changes; the Git ref update can veto a stale base. No model judge or expected answer decides truth. Forget suppresses retrieval while retaining ordinary Git history; erase rewrites history and prunes old objects. No rollback path for erase was identified; remember/correct/forget can be followed by a new compensating change, subject to validation and current state. Intent/receipt recovery covers retry of normal change requests.
- Operating mode and oracle: open user/agent request, not a bounded experiment or curriculum. The request text and `/mem` guidance may shape a proposal; the memory operation does not establish whether the guidance was read. Answer oracle: none for truth; validators test domain constraints. Persisted changes are fact statements/status/source references, controls for forget, Git history and operational receipts/intents. Immediate return is a published revision and outcome or a conflict/error; later read-back is through search/read/history under current eligibility. Delegated visibility is to the caller; later consumer visibility depends on subsequent retrieval or writeback. Selection predicate is explicit caller target/entity plus fact eligibility on later reads. Invalidation is by correction/supersession, forget controls, expiry, or erase. Activation/effect: implementation conclusion status `wired`; downstream use `uninspected`. Evidence limit: no live request was executed. `SRC-1` `src/change.rs`, `src/erasure.rs`, `src/repo.rs`, `src/validate.rs`, `src/mcp.rs`, and `src/cli.rs`.

#### RT-RTE-6 — Writeback into host instruction files

- Trigger and principal: operator invokes `mem writeback`; operator chooses target path/flags, or defaults to `AGENTS.md` in the current directory. Code selects current eligible facts by project and user preference scope, omitting facts sourced only from instruction files unless requested. It writes a generated natural-language managed block and preserves surrounding hand-written text unless `--force` is specified.
- Admission roles and answer oracle: operator decides to invoke and chooses target; code selects/presents active facts but no separate truth review or host approval is required. There is no expected answer oracle. The command can fail on file I/O; a later invocation can regenerate the managed block from current store state. It does not record a versioned admission receipt in the memory store for the host file write.
- Operating mode and guidance: open invocation, not a bounded experiment or curriculum. Stored fact statements guide output; the command itself does not consult the bundled skill. Persisted material is generated text in a managed instruction block. Immediate return is a count and path; later read-back occurs only if a host loads the edited file or an operator reads it. Delegated visibility and selection predicate: target host/file determines audience; project filtering and active-fact checks select content. Invalidation is replacement on a later writeback; facts changed in memory are reflected only after another writeback. Activation/effect: file write is `wired`; host loading and behavioral effect are `uninspected`. Evidence limit: host precedence and deployed project files were not supplied. `SRC-1` `src/cli.rs`, `skills/mem/SKILL.md`, and `README.md`.

#### RT-RTE-7 — Setup and integration configuration

- Trigger and principal: operator invokes `mem setup [claude|codex]` or `--remove`. The program edits host configuration to register Claude hooks/MCP/skill and Codex MCP; it backs up changed files, leaves an existing hook/skill/MCP registration in place, and supports removal. A missing Claude CLI prevents command-based MCP registration and is reported for manual completion.
- Admission roles and recovery: operator proposes the capability/configuration change by invoking setup and selects target; setup code decides exact edits and can refuse malformed settings or report unavailable integration commands. There is no model or content answer oracle. Recovery is backup restoration or `--remove`; rollback does not uninstall a separately existing/custom skill unless it matches the exact managed copy. Operating mode is explicit open configuration request. Guidance is the packaged integration setup code and bundled `/mem` skill. Persisted material is host configuration and installed skill text, not a revision in `memory.git`. Immediate return reports edits/status; later read-back is by host startup/configuration loading. Delegated visibility is limited to selected host installation. Selection predicate is requested target and existing configuration state; invalidation is removal or manual config change. Activation/effect: config writes are `wired`; host actually invoking each integration is `uninspected`. Evidence limit: no host installation or settings were supplied. `SRC-1` `src/setup.rs`, `src/cli.rs`, and `skills/mem/SKILL.md`.

### Claims

#### RT-CLM-1 — Hook failures do not fail the host session

Claimed operation: hook errors are swallowed and the hook returns successfully without context or sync output. The guarantee belongs to `src/hook.rs` error handling and covers only hook invocation; it does not cover MCP, HTTP, CLI, model service failures surfaced outside hooks, or successful delivery/consumption. Conclusion status: `wired` for implementation behavior; actual host response to exit status is `uninspected`. Guarantee strength: `protocol`. Evidence: `SRC-1` `src/hook.rs`.

#### RT-CLM-2 — Memory writes publish as validated compare-and-swap Git revisions

Claimed operation: normal memory writes are validated and published against the expected base; concurrent advancement returns a conflict rather than silently overwriting the newer published ref. Owner: repository publication layer, with domain validation at candidate tree. Enforcement point: `GitRepo::publish`. Guarantee strength: `protocol`. Covered routes: consolidation and normal remember/correct/forget operations that use this publication path. Alternate paths: erase rewrites history separately; external edits or embedded-library callers outside this path are not guaranteed by this claim. Conclusion status: `wired` from implementation; no live concurrent-write observation. Evidence: `SRC-1` `src/repo.rs` and `src/change.rs`.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-1 — Claude hook context

Consumer: Claude Code host model. Channel: hook `additionalContext` for session start and user prompt. Force: supplied contextual material; the host/model's actual authority treatment is uninspected. Horizon: current session or current prompt invocation, with no persistent effect established by the hook response itself. Evidence: `SRC-1` `src/hook.rs` and `src/setup.rs`.

#### RT-BAP-2 — MCP operation results

Consumer: calling MCP client and its host model. Channel: MCP tool result text. Force: tool output available to the caller; whether it is treated as evidence, instruction, or ignored is controlled by the client/model. Horizon: current tool call and any later use the host makes of the result. Evidence: `SRC-1` `src/mcp.rs` and `src/ops.rs`.

#### RT-BAP-3 — Writeback instruction block

Consumer: any host that loads the chosen instruction file. Channel: `AGENTS.md`-style natural-language managed block. Force: inherited from the consuming host's own instruction rules, uninspected here. Horizon: future sessions that load the file, until overwritten or removed. Evidence: `SRC-1` `src/cli.rs`, `README.md`, and `skills/mem/SKILL.md`.

## Annotations

none
