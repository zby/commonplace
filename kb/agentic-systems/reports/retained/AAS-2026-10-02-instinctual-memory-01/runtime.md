---
type: agentic-systems/types/agentic-system-runtime-report.md
description: "Runtime baseline of instinctual-memory tracing local ingestion, consolidation, search, client serving and memory publication"
run-id: AAS-2026-10-02-instinctual-memory-01
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
---

# instinctual-memory runtime report

## Runtime account

`mem` is the repository's portable CLI and library. A normal recall invocation starts at `mem` in `src/main.rs`; it parses a `mem search` command, resolves a store, and dispatches through `src/cli.rs` to the common search operation. Store resolution selects explicit `--root`, global/local flags, `MEM_ROOT`, nearest local `.mem`/legacy `mem`, then global `~/.mem` fallback. A project integration can instead invoke `mem serve --stdio` as MCP or `mem serve --http`; those adapters dispatch into the same operations. [`src/cli.rs` store selection]

> } else if let Some(env) = std::env::var_os("MEM_ROOT").filter(|v| !v.is_empty()) {
>             (PathBuf::from(env), StoreKind::Env)
>         } else if let Some(root) = find_local_store(&cwd) {
>             (root, StoreKind::Local)
>         } else if init {
>             (new_local(), StoreKind::Local)
>         } else {
>             self.store_fallback = true;
>             (global_store()?, StoreKind::Global)
> --- `src/cli.rs:181-189` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

An ordinary memory-building path begins with `mem backfill <paths>` or a specialized backfill command. The CLI selects a format adapter, reads input files into journal events tagged with scope/session and optional project, and appends them to the durable journal. Backfill can recurse, skip unknown formats when requested, or perform a dry run. The journal is immediate retained state; this step does not create curated facts. `mem consolidate` reads events after the checkpoint in bounded high-water batches, applies either rules or an LLM extractor, and prepares updated entity files, index, checkpoint and batch disposition. A validator checks the candidate before the Git publisher advances the memory ref. The default `auto` chooses LLM when an API key is configured, otherwise rules. [`src/cli.rs` ingestion]

> match adapter.read(path, &cli.scope, &cli.session) {
>             Ok(mut events) => {
>                 tag_project(&mut events, project);
>                 let n = events.len();
>                 for event in events {
>                     if journal.append(event)?.is_some() {
>                         ingested += 1;
>                     }
>                 }
> --- `src/cli.rs:1998-2006` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

On recall, lexical search combines eligible curated facts from a pinned Git revision with raw journal events; filters can narrow by project, scope or source, and callers can request facts only. Reranking is an optional next stage: JEV sends query and candidate text to an external Decisions endpoint when configured; if unavailable or declining, an installed local cross-encoder may be used, else lexical order is returned. Results contain hit IDs, statements/snippets and source references. An agent or user decides how to use results; host prompt assembly and model action lie outside the boundary. No supplied traces establish that an integration was installed, a result reached a host model, or it changed behavior. [`src/search/rerank.rs` external path]

> match JevReranker::from_env() {
>         Ok(jev) => match JevRerankAdapter::new(jev).rerank(query, baseline.clone(), limit) {
> --- `src/search/rerank.rs:170-171` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

Material alternate and forcing routes are direct CLI `change remember|correct|forget`, which immediately requests a validated memory-tree update; direct `erase`, which removes a fact/entity plus source events, branch history and pending intents; generated `writeback`, which overwrites its marked region in a project instruction file; setup, which configures host MCP/hooks; and the line-oriented `mem shell`, which interprets memory commands but does not pass input to the host shell. MCP stdio exposes search/read/history/status/change-request/task operations. HTTP exposes the operation layer over a listener and is optionally bound to a configured address; it is a separate network route, and the inspected code does not establish an authenticated deployment envelope. Host callbacks and hooks can trigger ingestion/sync, but their actual scheduling is controlled by excluded hosts. No process execution, remote worker, or dynamic extension framework was identified in the inspected CLI/library routes; this is bounded to the registered implementation modules, not proof about deployment wrappers.

Persistence is split between journal files and the bare `memory.git` tree. Journal appends provide later search and future consolidation input. Published facts, controls, index and checkpoint are visible to later invocations reading that store. Git publication validates a candidate then compare-and-swaps the branch ref against the base revision; a concurrent winner causes a conflict and requires reread/reconcile/retry. This is an implementation protocol, not evidence of deployment-wide isolation or successful operation. [`src/consolidate.rs` batch input]

> let extractor = resolve_extractor(options.extractor);
>         let all_after: Vec<JournalEvent> = journal.read_from(checkpoint.through_seq + 1)?;
> --- `src/consolidate.rs:114-115` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` [`src/repo.rs` stale base rejection]

> if current != base {
>             return Err(Error::Conflict(
>                 "published memory changed; re-read and reconcile".into(),
>             ));
>         }
> --- `src/repo.rs:234-238` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The principal decision policy is explicit code plus extractor behavior: deterministic rules match a narrow pattern set, while the configured LLM proposes structured candidate facts and evidence, and internal validation/filtering decides what enters the candidate tree. The model's own judgment is not an independent answer oracle. The operator chooses inputs, scope, extractor/high-water and optional explicit changes. There is no human review step in the ordinary consolidate publication path; domain validation and compare-and-swap are code gates. [`src/consolidate.rs` extractor selection]

> let mut extraction = match extractor {
>             ExtractorKind::Llm => llm_extract(existing, blocked, &bounded)?,
>             _ => rules_extract(existing, blocked, &bounded),
>         };
> --- `src/consolidate.rs:154-157` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

The strongest shipped write guarantee is the repository publisher's validated compare-and-swap for writes routed through it. Its owner is `GitRepo::publish`; the enforcement point is candidate validation and conditional ref update against the supplied base. Strength is `protocol`, not deployment guarantee. It covers writes using this publisher and validator; direct filesystem edits to the store, generated instruction-file writeback, external host configuration and arbitrary operator access do not share that transaction. Required external contracts include filesystem/Git behavior and the honesty of the supplied validator. The ref update prevents a stale-base write from silently winning, but does not prove all outputs correct, provide an approval gate, or establish backup/recovery beyond the explicitly implemented intent/replay and erasure paths. [`src/repo.rs` stale base rejection]

> if current != base {
>             return Err(Error::Conflict(
>                 "published memory changed; re-read and reconcile".into(),
>             ));
>         }
> --- `src/repo.rs:234-238` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

No observed-run evidence was supplied. Therefore invocation success, MCP/HTTP delivery to a client, activation of retrieved content, recovery in a real deployment, and benefit to future task performance remain unobserved. External provider internals and actual operator grants, host sandboxing and installation state are outside the boundary.

## Shared records

### Components

#### CMP-1 — LLM consolidation extractor

Representational form: distributed parametric model accessed through an OpenAI-compatible chat-completions endpoint. Storage substrate: external provider service. It receives bounded user/note event text and returns candidate facts with event references and copied evidence; the repository then validates and filters candidates. Parameters do not change through this invocation path. Exact model version is not pinned: `MEM_LLM_MODEL` can override the default `anthropic/claude-haiku-4.5`, and the endpoint is configurable through `MEM_LLM_BASE_URL`; provider-side resolution and internals are inaccessible. Evidence and scope: `SRC-2`, `src/consolidate.rs`; supplied absence of traces means actual call, returned data and effect are unobserved. The runtime extractor selection is cited above.

#### CMP-2 — JEV reranker

Representational form: distributed parametric judging service. Storage substrate: external OpenRouter-compatible Decisions endpoint. It receives the search query and candidate row text, then returns ranking judgments; errors or decline fall through. Parameters do not change through this code path. Exact model version is not pinned: `MEM_JEV_MODEL`/`JEV_MODEL` can select it and the endpoint is configurable; the default model label is `~typesafe/jev-latest`. Provider internals are uninspected. Evidence and scope: `SRC-2`, `src/jev.rs`, `src/search/rerank.rs`; configured activation and ranking effect are unobserved. [`src/search/rerank.rs` fallback selection]

> match JevReranker::from_env() {
>         Ok(jev) => match JevRerankAdapter::new(jev).rerank(query, baseline.clone(), limit) {
> --- `src/search/rerank.rs:170-171` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### CMP-3 — Local Laya cross-encoder

Representational form: local distributed-parametric model. Storage substrate: downloaded ONNX model under the memory root's `.models` cache and in-process inference. The inspected implementation offers BGE, Jina and BGE multilingual variants; model download/version pinning is not established by the inspected runtime boundary. Parameters do not change during inference. Evidence and scope: `SRC-2`, `src/search/laya.rs`, `src/search/rerank.rs`; installation, activation and effect are unobserved.

### Operative objects

#### OBJ-1 — Append-only source journal

Source-native identity and form: JSONL event journal containing normalized source events, roles, content, scope/session, source identifiers and metadata. Substrate is files under the resolved memory root's `journal/`. New events are appended and later read by search and consolidation. It is immediate return/read-back retained memory; it does not itself establish a curated fact. `SRC-2`, `src/cli.rs`, `src/journal.rs`.

#### OBJ-2 — Published memory tree

Source-native identity and form: Git tree in `memory.git`, containing entity fact files, controls, index, checkpoint and dispositions. Substrate is a bare Git repository. Search pins a head revision for a query; later writes publish a new revision. This is read-back retained memory across invocations. `SRC-2`, `src/consolidate.rs`, `src/repo.rs`, `src/ops.rs`.

#### OBJ-3 — Project instruction writeback region

Source-native identity and form: generated section in a project instruction file such as `AGENTS.md`, derived from selected project facts. Substrate is the host project's ordinary file system, outside the memory Git transaction. `mem writeback` can replace the marked generated region and leave surrounding content. Later host invocation may read it, but the host's actual delivery is outside this boundary; activation is unobserved. `SRC-2`, `src/cli.rs`. [`src/cli.rs` writeback marker]

> const WRITEBACK_BEGIN: &str = "<!-- mem:begin (generated by `mem writeback`; edits inside are replaced) -->";
> --- `src/cli.rs:1854-1854` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

### Routes

#### RTE-1 — File backfill to journal

Endpoints: selected local files/directories to `OBJ-1`. Principal: operator/host invokes CLI; code selects adapter and appends events. Next-step owner is operator or host, which chooses whether/when to consolidate. Decision policy is format adapter selection and event normalization; representation is structured journal events. Context/state: chosen store, scope, session and optional project. Executor is local CLI/library; effect boundary is journal files. Runtime-client controls: `--dry-run`, recursion and unknown-format options. Immediate return is event append; later read-back is by journal scan/search and consolidation. Selection predicate is supported format and adapter acceptance; repeated source IDs are idempotently handled by journal semantics. No explicit expiry. Activation/effect on host behavior is unobserved. `SRC-2`, `src/cli.rs`, `src/ingest.rs`, `src/journal.rs`. The append route is evidenced above.

#### RTE-2 — Journal consolidation to published facts

Endpoints: `OBJ-1` events and current `OBJ-2` to new entity facts/index/checkpoint/disposition in `OBJ-2`. Trigger/principal: operator or host invokes `mem consolidate`; next-step owner is the CLI's batch loop, then the selected rules or LLM extractor. Operator selects scope/extractor/high-water; code filters, validates and publishes. Answer oracle: none established; LLM judgment proposes but is not an expected-answer source. Mode: open-ended event ingestion and routine bounded batches, not a supplied curriculum. Improvement trigger is new journal sequence beyond the checkpoint. Context includes existing entities and controls (suppressions/deletions). Effect boundary is candidate Git tree, validation, then conditional branch update. Immediate result is a published revision or error; later read-back is search/read/consolidation. Selection predicate is extractor acceptance, quarantine/blocked fact checks and validator rules. No expiry of published facts is established here. Activation in agent behavior is unobserved. Publication is guarded by the protocol described above. `SRC-2`, `src/consolidate.rs`, `src/repo.rs`, `src/validate.rs`.

#### RTE-3 — Search and rerank to caller

Endpoints: `OBJ-2` and `OBJ-1` to CLI/MCP/HTTP/shell caller. Principal: caller supplies query and filters; code performs lexical search and optional reranking. Next-step owner is the calling agent/host or user. Decision policy ranks eligible fact and journal hits; representational form is structured search-hit output. Context includes store, project, scope and source filters. Effect is output only; runtime client controls include limit, facts-only, rerank, snippet and source-line options. Immediate return is hits; later read-back is by explicit read/history operations; delegated visibility to host model is not implemented within the boundary. Selection predicate is eligibility/filtering plus rank. No cache invalidation or expiry is established for returned hits; subsequent calls read current store state. Behavior activation and benefit are unobserved. `SRC-2`, `src/ops.rs`, `src/search/mod.rs`, `src/search/rerank.rs`, `src/mcp.rs`, `src/http_serve.rs`. MCP speaks line-delimited JSON-RPC and invokes shared operations. [`src/mcp.rs` stdio entry]

> pub fn serve_stdio(root: &Path, scope_id: &str, session_id: &str) -> Result<()> {
>     let stdin = std::io::stdin();
>     let mut stdout = std::io::stdout();
> --- `src/mcp.rs:17-19` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a` [`src/ops.rs` shared operation dispatch]

> match operation {
>         "memory_search" => search(root, args),
>         "memory_read" => read(root, args),
> --- `src/ops.rs:42-44` @ `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`

#### RTE-4 — Explicit change and erasure

Endpoints: operator-supplied fact/change or erasure target to `OBJ-2`, and for erasure also journal events, history and pending intents. Principal and proposer are the operator or calling client; code validates request and publishes. The operator chooses statement, target and reason; no answer oracle. Context is current tree/controls and request ID. Effect boundary for fact changes uses the Git publisher; erasure has its own cross-store procedure. Immediate return is accepted/rejected result; later read-back is current facts/history or absence. Predicate: domain validation and target existence; forget suppresses and erasure purges within implemented stores. Recovery semantics differ: forget can leave historical/suppression evidence, erase is intended to remove targeted records/history. `SRC-2`, `src/cli.rs`, `src/change.rs`, `src/erasure.rs`.

#### RTE-5 — Generated writeback and host setup

Endpoints: curated project facts to marked instruction-file region; setup separately changes host configuration to register MCP/hooks. Trigger is explicit operator command. Operator chooses destination, project and setup target; code merges generated sections or edits host config. Effect boundary is external project/host files, outside `memory.git` publication. Immediate return is written path/config status; later host reads are possible but not evidenced. Selection predicate is project/entity/fact eligibility. Writeback edits inside its marker are replaced on later writeback; no autonomous activation evidence. `SRC-2`, `src/cli.rs`, `src/setup.rs`.

### Claims

#### CLM-1 — Intended portable durable agent memory

The product description claims a Git-backed memory workflow with backfill, consolidation, search and host integrations. This report treats the implementation paths above as inspected affordances; it does not infer installation, delivery or improved outcomes. Source: `SRC-1`, `README.md`.

### Evidenced absences

#### ABS-1 — No operation traces or deployed host configuration in this boundary

Status: absent. Inspected boundary is the supplied whole-repository snapshot and registered source scope. Query: boundary register identifies implementation/documentation sources and records excluded stores, host configuration, services and operation traces at reviewed commit `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`. Evidence: `SRC-1` and `SRC-2` registers in the supplied boundary. Supports the conclusion that operation, delivery, activation and benefit cannot be claimed from this report; it does not establish those behaviors are absent in deployments.

### Behavioral-authority paths

none declared in this member

## Annotations

none
