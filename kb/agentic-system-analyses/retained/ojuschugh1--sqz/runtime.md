---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "sqz runtime baseline: native compression, MCP mediation, browser and IDE alternatives, and configuration admission at the frozen commit."
run-id: AAS-2026-11-09-sqz-154fb86209ba-01
reviewed-boundary: "495c078d8f4c94d060ecfbb4d919286670b87898"
---

# sqz runtime report

## Runtime account

sqz transforms context for an external agent; it does not own that agent's next-action loop. Its consequential work is compression before delivery, replacement of repeated material with references or deltas, and recovery of retained originals. The caller decides whether to use the transformed text and whether to call recovery tools. SRC-1 supplies implementation and declared protocols, not an observed execution or causal experiment. All operation, actual model activation, and downstream benefit remain uninspected in this report.

### Ordinary invocation: an MCP file read

A host-selected `sqz_read_file` call reaches the MCP dispatcher with a JSON tool name and arguments. The server applies a pending preset before dispatch. The handler resolves the supplied path against the process environment, checks the file-size ceiling, reads bytes, converts them to UTF-8 with replacement for invalid bytes, optionally selects lines, and caps the returned text. Only that selected text reaches compression and cache admission. A header records path, original byte size, selected lines and continuation information. The header is outside compression. Thus a retained original on this path is the selected, decoded body, not necessarily the original whole file (SRC-1, `sqz-mcp/src/lib.rs`; [RT-RTE-file-read](#rt-rte-file-read)).

Code, not a model, chooses fresh text versus reference versus delta. A fresh file-tool body takes the lossless native pipeline with a default preset. An exact fresh hit can replace it with `§ref:HASH§`; a line slice can reference an earlier full body; a sufficiently similar body can become a delta. Tiny bodies and ranged reads have additional presentation gates. SQLite survives process restarts; request state and responses are ordinary current-call state. The return is text in a JSON-RPC response, not a model invocation. The external host/model owns the next step. Expansion is an explicit subsequent call; no dereferencing happens inside model attention (SRC-1, `sqz-mcp/src/lib.rs`, `sqz_engine/src/cache_manager.rs`; [RT-RTE-cache-recovery](#rt-rte-cache-recovery)).

### Native alternatives and enforcement limits

The CLI has two materially different compression entry paths. Stdin with automatic mode takes `CliProxy`; positional text or explicit mode takes the engine directly. The proxy probes exact/slice caches, tries a command formatter, and only then uses the generic engine. It can abbreviate phrases and annotate known paths after engine verification. Direct engine calls route by risk, run the configured pipeline, score preservation checks and, below a threshold, recompress with safer settings. Explicit Default and Aggressive modes still call `compress`; they are not demonstrated risk-router bypasses. Safe mode on content not itself risk-routed uses the reduced preset through the non-lossless pipeline, so the name does not imply byte identity (SRC-1, `sqz/src/main.rs`, `sqz/src/cli_proxy.rs`, `sqz_engine/src/engine.rs`; [RT-RTE-cli-compress](#rt-rte-cli-compress), [RT-RTE-engine-compress](#rt-rte-engine-compress)).

Four forcing comparisons bound the guarantees:

1. **General compression versus file-read bodies.** The latter skips content-altering stages on misses, but decode/range/cap operations precede it, and repeat reads can return references or deltas. “Lossless file read” is not an unconditional whole-file, byte-identical response contract.
2. **Engine versus CLI formatter and postprocessing.** The verifier judges the engine candidate, not a command formatter against the raw input, nor the final phrase-abbreviated/annotated CLI output. Formatter returns are reachable from automatic stdin calls with a command label. The verifier is a heuristic fallback policy, not a system-wide semantic invariant.
3. **Cache-enabled versus `--no-cache`.** The CLI option gates dedup lookups, not all persistence. Formatter/generic admission and dependency pre-caching do not use that option as their write guard. The MCP proxy instead passes the option to `compress_tool_result`, suppressing its content cache path and expansion advertisement; it still logs statistics. Neither option is a blanket “no disk writes” guarantee.
4. **Native versus browser.** The browser uses a separate WASM implementation and then a separate JavaScript fallback. Native risk routing, verifier and SQLite guarantees cannot be transferred to them by product name.

These comparisons are source traces, not executed probes. Short risk-bearing inputs also matter: `never_store` explicitly requires at least 100 bytes after ANSI removal. It is a bounded pattern policy, not a complete secrets detector. Public cache-manager calls are lower-level APIs without the engine's risk guard (SRC-1, `sqz_engine/src/confidence_router.rs`, `sqz_engine/src/cache_manager.rs`).

### Mediation, capability and isolation

The MCP proxy spawns the user-specified upstream process and relays JSON-RPC in two directions. Request IDs associate replies with initialization, tool listing and tool calls. It transforms eligible successful text items, not error/non-text items, and handles recovery/help calls locally. Lazy descriptions retain full documentation in process memory for an explicit help request. This is subprocess mediation, not delegation to an isolated model worker. Upstream code retains its OS capabilities; sqz does not grant it a narrower sandbox (SRC-1, `sqz-mcp/src/proxy.rs`; [RT-RTE-mcp-proxy](#rt-rte-mcp-proxy)).

The native file tool reads supplied absolute and traversal paths using process filesystem authority. The implementation assigns approval responsibility to the host. The shipped HTTP and MCP SSE listeners bind loopback; loopback binding is not per-file authorization or proof of a deployed security envelope. Hook generation changes integration configuration and, for Claude Code, adds allow rules for the shell option and compression command. Rewriting remains conditional on host payload, mode and command shape. Built-in Read/Grep/Glob are not intercepted by the shell hook; generated natural-language guidance asks the agent to choose sqz tools instead (SRC-1, `sqz-mcp/src/lib.rs`, `sqz/src/main.rs`, `sqz_engine/src/tool_hooks.rs`; [RT-RTE-integration-install](#rt-rte-integration-install)). Current grants and actual host enforcement are unobserved.

### Other shipped consumers

The HTTP `sqz proxy` is a returning transform, not an LLM gateway. It returns a compressed request body to its HTTP caller. Its message-age rules shorten old text by retaining first/last lines and a count; no summarizing model is called. The caller must submit the result to its provider. Unmatched shapes stay unchanged; provider support is therefore shape-specific, not a claim of complete request-format coverage (SRC-1, `sqz/src/main.rs`, `sqz_engine/src/api_proxy.rs`; [RT-RTE-request-transform](#rt-rte-request-transform)).

Browser content scripts propose replacements for long input/paste events. Accept applies text, Skip clears the pending proposal, and submission can apply pending compression without a separate Compress click. WASM memoizes compressed strings rather than emitting native references; if WASM gives no shorter result, JavaScript performs its own lossy passes. Editor setters and host submission supply the effect boundary. Browser statistics use extension local storage, not native SQLite. No source-to-bundled-WASM equivalence or live-site correctness was established (SRC-1, `extension/background.js`, `extension/content/common.js`, `sqz-wasm/src/lib.rs`; [RT-RTE-browser-compress](#rt-rte-browser-compress)).

VS Code pipes content to `sqz compress` on stdin; it trims output and removes lines beginning `[sqz]`. Unsupported languages or CLI failures take a line-based fallback. `usedAst: true` is a bridge label after CLI success, not evidence that the native invocation used AST extraction. JetBrains writes a temporary file and passes its path plus `--language`; the pinned CLI's Compress declaration has no `--language` option and its positional argument is text, not a file loader. Source comparison therefore identifies an incompatible supported-language call shape, with a caught-error line fallback; no installed execution was observed. Neither fallback inherits native verification or recovery guarantees (SRC-1, `vscode-extension/src/sqzBridge.ts`, `jetbrains-plugin/src/main/kotlin/com/sqz/SqzBridge.kt`, `sqz/src/main.rs`).

Session resume is a separate consumer of stored session records: it chooses a requested/latest session, constructs events from its summary, last five conversation turns (each clipped at 200 bytes using a text boundary), learnings and corrections, and prints a continuity guide. This consumer does not show that ordinary cache-producing CLI/MCP calls create those session records. `compact` computes eviction candidates from synthetic cache descriptors and prints a summary; on a nonempty eviction result it notifies cache compaction. It does not itself remove messages from an external host's window. PreCompact similarly marks refs stale, not host content. Detailed session, import/export, pin and knowledge-revision semantics are left to the memory member (SRC-1, `sqz/src/main.rs`, `sqz_engine/src/cache_manager.rs`).

### Evidence and change scope

The added inspection under SRC-1 covers implementation in the paths cited above, including confidence routing, verification, pipeline gates, sparse tool selection, preset reload and browser/IDE fallback branches. Generated guidance is doctrine/design consumed through host/model interpretation. No new source identity or revision was used. Installers, release machinery, benchmark execution, all browser site adapters, and external providers were not re-audited here; this prevents deployment, measured performance, model-quality and binary-equivalence conclusions, not a source-level account of the selected routes. No parameter update or model invocation is required by the inspected compression routes. The native `ModelRouter` returns configuration based on arithmetic heuristics; the MCP `ToolSelector` computes sparse TF-IDF/Jaccard similarities and explicitly ignores its model-path parameter. Numerical scores here are symbolic computed data, not evidence of distributed learned weights (SRC-1, `sqz_engine/src/model_router.rs`, `sqz_engine/src/tool_selector.rs`).

## Shared records

### Components

#### RT-CMP-compression-pipeline
Label: Native compression pipeline

Source-native `CompressionPipeline` is executable symbolic Rust with configurable stages, mutable dictionary/count caches in process memory and a TOML-derived preset. SRC-1, `sqz_engine/src/pipeline.rs`, implements stages plus JSON projection, run/template/sliding dedup, entropy truncation, prose pruning and encoding. It is not a summarizing model. Its lossless branch gates both stages and postprocessing; the file-tool path supplies a default preset. The helper permits custom transforms as well as ANSI stripping, so this is not a universal claim about every caller-supplied preset or inserted stage.

> fn stage_is_lossless(name: &str) -> bool {
>     matches!(name, "ansi_strip" | "custom_transforms")
> }
> --- `sqz_engine/src/pipeline.rs`

No distributed-parametric component is established on these routes. External models consuming output have uninspected parameters, exact versions and mutable-endpoint behavior; sqz does not pin those consumers in the inspected entry paths.

#### RT-CMP-wasm-engine
Label: Browser WasmEngine

Source-native `WasmEngine` is separate symbolic Rust compiled for WASM, with in-memory `SessionState`, a preset enum and hash-to-compressed-string memoization. It classifies JSON/code/log/prose and runs its own transforms. Native SQLite, risk-router and verifier behavior do not follow from this identity (SRC-1, `sqz-wasm/src/lib.rs`).

> if let Some(cached) = self.dedup_cache.get(&hash) {
>             return cached.clone();
>         }
> --- `sqz-wasm/src/lib.rs`

### Operative objects

#### RT-OBJ-preset
Label: Native preset configuration

Source-native `Preset` is symbolic structured configuration parsed from TOML and held behind engine mutexes. It determines stages, token-count family and tool-selection thresholds; model names are configuration strings rather than pinned model weights. Files can persist it across processes; the engine stores an active in-memory copy. Admission is [RT-RTE-preset-reload](#rt-rte-preset-reload) (SRC-1, `sqz_engine/src/engine.rs`, `sqz_engine/src/tool_selector.rs`).

> let new_preset = PresetParser::parse(toml)?;
> --- `sqz_engine/src/engine.rs`

### Routes

#### RT-RTE-file-read
Label: MCP file read and presentation

The host-selected tool call supplies a path and optional byte/line controls; `handle_sqz_read_file` owns progression from filesystem read to decoded/ranged/capped body, cached lossless transform and header. It acts with process filesystem authority, not a sqz path allowlist. General `compress` uses lossy caching instead; grep/list create bounded derived bodies before the same lossless cache path (SRC-1, `sqz-mcp/src/lib.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Header plus faithful selected text, reference or eligible delta in tool output; I/O and size failures return errors.
- Later read-back: The selected decoded body may enter persistent cache and be recovered by expansion; this does not retain bytes omitted by decoding/ranging/capping.
- Delegated visibility: Host receives the response; any model delivery or further delegation is outside sqz's control.
- Selection predicate: Tool ID, supplied path/range/cap; repeat presentation additionally depends on cache freshness, similarity, body token size and whether a range was requested.
- Invalidation or expiry: Content hash distinguishes changed bodies; reference freshness and compaction are handled by the cache route.
- Activation or effect: Reads OS files and constructs model-facing text; actual model use unobserved.
- Evidence limits: No executed host call; a fresh lossless body is not a whole-file binary guarantee.

Guarantee owner: native file-tool handler and pipeline. Enforcement: body preparation then `compress_cached(..., true, range.is_none())`. Strength: invariant only for the gated fresh transformation, excluding ANSI stripping; end-to-end retention is a protocol relying on a live cache and a consumer that can expand refs. Alternate general compression, binary decoding and caps delimit coverage.

> let full_text = String::from_utf8_lossy(&bytes).into_owned();
> --- `sqz-mcp/src/lib.rs`

> self.compress_cached(&raw_text, tokens_original, true, range.is_none())?;
> --- `sqz-mcp/src/lib.rs`

#### RT-RTE-engine-compress
Label: Native risk routing and verification

`SqzEngine::compress` receives text, locks preset/pipeline, creates a session-context label, routes by content risk, runs compression, verifies and may recompress safely. Code proposes and selects representations; there is no human veto per candidate. The original is the reference input for deterministic preservation checks, not an expected task answer oracle. Operating mode is open text transformation, not a model-improvement curriculum (SRC-1, `sqz_engine/src/engine.rs`, `sqz_engine/src/verifier.rs`, `sqz_engine/src/confidence_router.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: CompressedContent with text, counts, stages, provenance and optional verification; ordinary Result errors remain possible.
- Later read-back: inapplicable — plain compress does not itself admit content to persistent cache; caller routes can.
- Delegated visibility: inapplicable — no delegated model computation.
- Selection predicate: Risk patterns above the router's length gate, configured stages and verification score below 0.6; preservation failure caps confidence at 0.5.
- Invalidation or expiry: inapplicable — candidate is current-call state; preset changes affect later calls.
- Activation or effect: Selects delivered representation; no evidence that a model follows or benefits from it.
- Evidence limits: Checks sample some fields and numbers, and aggregate pass ratios are not semantic equivalence.

Guarantee owner: engine/verifier. Strength: best effort. Enforcement covers engine candidates and cache misses routed through this facade, not cache hits, standalone pipeline calls, CLI formatter output, final abbreviation, browser transforms or HTTP history summarization. Fallback recomputes once and returns the result with verification; it does not require every check to pass. The external contract needed for task preservation is that omitted or re-encoded content is dispensable or recoverable to the consumer; source inspection cannot establish it.

> let fallback_triggered = confidence < FALLBACK_THRESHOLD;
> --- `sqz_engine/src/verifier.rs`

> let safe_result = self.compress_safe(input, &pipeline, &ctx, false)?;
>             return Ok(safe_result);
> --- `sqz_engine/src/engine.rs`

#### RT-RTE-cli-compress
Label: CLI interception and shell delivery

Automatic stdin dispatch selects `CliProxy`; explicit modes/positional text select the engine. Proxy order is track file/dependencies, advance turn, cache exact/slice probes, command formatter, generic engine and postprocessing. A formatter passing the net-win gate can return without engine verification against the original. Errors/panics have passthrough branches; initialization behavior differs between direct `require_engine` failure and automatic proxy initialization fallback. Exit trailers on stdin are stripped and re-raised on the CLI's return paths (SRC-1, `sqz/src/main.rs`, `sqz/src/cli_proxy.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Transformed text or original bytes/text on applicable passthrough branches; counts go to stderr and statistics storage.
- Later read-back: Formatter/generic outputs admit original content to cache unless `never_store`; known-file and dependency records can affect future annotations/probes.
- Delegated visibility: Shell/host receives stdout and stderr; no agent subcontext is created.
- Selection predicate: Stdin plus auto mode chooses proxy; command label chooses formatter; exact/slice hits precede formatting; abbreviation is on unless opted out and is skipped for source/risk-safe results.
- Invalidation or expiry: Cache freshness applies to probes; no-cache disables probes but does not prevent later stores or tracking.
- Activation or effect: Changes shell-visible output, persists statistics and may pre-read dependency files; actual host/model effects unobserved.
- Evidence limits: No execution of shell grammars, approval flows or exit propagation; no-cache is not a privacy guarantee.

Admission: caller command triggers software admission without per-content human review. Risk pattern detection can reject writes; `--no-cache` does not veto the store branches. Original recovery or reset supplies recovery, subject to cache availability. Guidance recommends piping long output and opting out of refs/abbreviations when necessary. Native code makes the per-candidate formatting decisions; no expected-answer oracle is used.

> if !self.engine.never_store(output) {
> --- `sqz/src/cli_proxy.rs`

> self.engine
>                         .cache_manager()
>                         .store_compressed(output.as_bytes(), &compressed)
>                         .is_ok()
> --- `sqz/src/cli_proxy.rs`

#### RT-RTE-cache-recovery
Label: Cache admission, freshness and expansion

The engine's cache wrappers skip content for which `never_store` is true; otherwise `CacheManager` probes SHA-256 exact identity, line slices and near-duplicates, and stores originals plus compressed representations in SQLite. Plain manager APIs are lower-level and do not enforce that wrapper policy. Automatic software admission follows use, not a separate human approval. Similarity is heuristic selection, not an answer oracle. The operating mode is repeated open requests; recovery expands a requested hash prefix/token (SRC-1, `sqz_engine/src/engine.rs`, `sqz_engine/src/cache_manager.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Fresh representation, exact/slice ref, delta, or expansion result; ambiguous/missing prefixes and database failures have explicit failure outcomes.
- Later read-back: Persistent original/compressed bytes feed future probes, deltas and explicit expansion across invocations and sessions sharing the DB.
- Delegated visibility: No separate model worker; all users of the same DB can potentially request recovery subject to their OS access.
- Selection predicate: Hash identity, freshness, line containment, recent/LSH similarity candidates; explicit expansion selects a prefix and optional line range.
- Invalidation or expiry: Default ref age is 30 minutes; persisted compaction marker invalidates older accesses; pinned entries bypass those checks. Expansion needs retained storage, independently of ref freshness.
- Activation or effect: Replaces delivered bodies with refs/deltas and can restore retained content; actual model recognition or correct reconstruction unobserved.
- Evidence limits: Freshness estimates likely window residence from timestamps, not a host-window membership check. Pre-caching dependencies also makes admission different from actual prior model delivery.

Guarantee owner: cache manager. Strength: protocol for meaningful references, not invariant that the model has seen the body. Raw originals support recovery when captured and still available; legacy/compressed-only entries explicitly weaken byte-exact recovery. Rejection ability belongs to wrapper risk guards and callers choosing noncached routes; reset/invalidation can remove state, while expansion recovers content rather than rolling back model behavior.

> if let Ok(true) = self.store.is_cache_entry_pinned(hash) {
>             return true;
>         }
> --- `sqz_engine/src/cache_manager.rs`

> if let Some(bytes) = self.store.get_cache_entry_original(&hash)? {
>             return Ok(Some(ExpandResult::Original { hash, bytes }));
>         }
> --- `sqz_engine/src/cache_manager.rs`

#### RT-RTE-mcp-proxy
Label: Upstream MCP mediation

A CLI-specified command is spawned with piped stdin/stdout and inherited stderr. A request-ID map selects response rewriting; locally handled expansion/help calls do not reach upstream. Successful text items run `compress_tool_result`, which rejects small, Safe-routed or insufficient-saving transformations. Lazy tool descriptions are shortened and originals retained in process memory (SRC-1, `sqz-mcp/src/main.rs`, `sqz-mcp/src/proxy.rs`, `sqz_engine/src/engine.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rewritten JSON-RPC response, untouched error/non-text/notification paths, or locally generated expansion/help result.
- Later read-back: Content originals use the native cache unless disabled; lazy descriptions can be requested by name during this proxy process.
- Delegated visibility: Upstream process receives forwarded client calls, not sqz-local recovery/help calls; no isolated model context is created.
- Selection predicate: Pending request kind, result success and item text type; flags choose description/lazy/cache modes, then engine gates choose content changes.
- Invalidation or expiry: Content cache follows native policy; tool_docs is process-local and updated when shortened descriptions are seen in tools/list.
- Activation or effect: Rewrites descriptions/instructions and results; upstream tool execution itself is not authorized or sandboxed by compression.
- Evidence limits: No upstream execution or host trace. --no-cache suppresses cache-enabled content compression and expansion advertisement, but not statistics writes or unconditional dispatch recognition of recovery tool names.

> let c = self.engine.compress_tool_result(text, !self.no_cache)?;
> --- `sqz-mcp/src/proxy.rs`

> if name == EXPAND_TOOL_NAME || name == HELP_TOOL_NAME {
> --- `sqz-mcp/src/proxy.rs`

#### RT-RTE-request-transform
Label: HTTP request-body transformation

Loopback HTTP input is parsed as an API-format request; the handler calls `compress_request` and returns the transformed body, with no provider forwarding. Configured code rules select system/tool text and older history. Default history retention is ten recent messages; old long text gets first/last-line extraction with counts. OpenAI string content, Anthropic system strings/tool-result strings, and Google text parts take distinct branches; unmatched blocks are not proof of compressed coverage (SRC-1, `sqz/src/main.rs`, `sqz_engine/src/api_proxy.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP JSON containing a compressed request body and statistics, or route/parser errors; compression errors can return the original body.
- Later read-back: uninspected — persistence and reuse of returned history depend on the caller; this handler logs statistics, not a reloadable copy of the omitted middle.
- Delegated visibility: inapplicable — no provider/model call is issued.
- Selection predicate: URL format, message role, age, content shape, configuration and length; shorter candidate checks on several branches.
- Invalidation or expiry: inapplicable — body replacement is per request; future inputs are caller supplied.
- Activation or effect: Removes middle history text from the returned payload; caller must adopt and submit it for model effect.
- Evidence limits: No causal preservation or successful API-client compatibility established; engine verification does not govern summarize_text.

> format!(
>         "{first_line}\n[... {total_lines} lines, {} chars ...]\n{last_line}",
>         text.len()
>     )
> --- `sqz_engine/src/api_proxy.rs`

#### RT-RTE-browser-compress
Label: Browser proposal and submission

Input/paste events above 100 estimated tokens trigger asynchronous compression with an overlap lock for ordinary input. Background WASM is attempted first; a missing or non-shorter result falls through to JS. Preview callbacks accept or discard; submit/Enter can apply pending replacement. Decisions are code compression plus a human UI choice where used, not a model judgment or answer oracle. Operating mode is open editor input (SRC-1, `extension/content/common.js`, `extension/background.js`, `sqz-wasm/src/lib.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Editor replacement on acceptance/submission, or unchanged text when skipped/no proposal; statistics are recorded locally.
- Later read-back: WASM memoizes output for identical hashes in memory; extension local storage retains aggregate statistics/settings. No native original-expansion route is established here.
- Delegated visibility: Text crosses content-script/background messaging, not a delegated model context.
- Selection predicate: Input threshold/stability, WASM shortening and JS fallback, then pending proposal and UI events.
- Invalidation or expiry: Pending values clear on accept/skip/submit; in-memory WASM cache lasts with the engine instance.
- Activation or effect: Calls supplied site editor setter; host submission and model consumption remain external/unobserved.
- Evidence limits: UI preview is not mandatory per-content approval because submit applies pending compression. Native verifier/never-store policies are not wired into these implementations.

> if (wasmResult && wasmResult.length < text.length) {
>     return wasmResult;
>   }
> --- `extension/content/common.js`

> if (!pendingCompressed) return;
> --- `extension/content/common.js`

#### RT-RTE-preset-reload
Label: Preset change admission

A caller's TOML or a watched file proposes a configuration change. Native reload parses before updating pipeline/router/preset. MCP watches enqueue pending TOML and apply it before tool calls, also rebuilding tool selection. This admits software policy changes, not learned parameter updates (SRC-1, `sqz_engine/src/engine.rs`, `sqz-mcp/src/lib.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reload success/error or deferred pending application; watcher errors are logged and serving can continue without watching.
- Later read-back: The in-memory active preset shapes future compression/tool selection; a persistent TOML file can supply subsequent loads.
- Delegated visibility: inapplicable — no model delegation or candidate authoring.
- Selection predicate: File event and parse validity, then lock availability; MCP applies pending state at a tool-call boundary.
- Invalidation or expiry: Later valid configuration replaces active state; prior preset persists on parse rejection. Restore an earlier file/configuration to recover; no versioned rollback transaction was established.
- Activation or effect: Rebuilds active pipeline/router/selector configurations, potentially changing future output.
- Evidence limits: Parse validity is not task quality; separate mutex updates and ignored watcher-stage errors do not establish atomic cross-component replacement.

Proposal authorship is caller/filesystem-writer supplied; whether human is unresolved. Parser/code decides admission; a file writer can withhold or replace configuration. No per-content human veto, expected-answer oracle, autonomous experiment or improved-capacity evidence is supplied. Guidance is the structured configuration itself, persisted as TOML and active fields; no formulated criticism/revision loop is established.

> if let Ok(mut pipeline) = self.pipeline.lock() {
>             pipeline.reload_preset(&new_preset)?;
>         }
> --- `sqz_engine/src/engine.rs`

#### RT-RTE-integration-install
Label: Host integration and guidance admission

`sqz init` selects integration targets and writes hook/configuration/guidance through shipped integration helpers. Shared guidance requests shell piping, preference for sqz file tools, recall and expansion, and explains reference/abbreviation notation. Claude rewriting is gated by permission mode, shell grammar and installed allow rules; successful eligible untruncated Bash results have a post-hook alternative. Host-native file tools remain alternate nonintercepted paths (SRC-1, `sqz/src/main.rs`, `sqz_engine/src/tool_hooks.rs`, `sqz_engine/src/codex_integration.rs`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Installation/status output, hook-rewritten tool payload, post-hook replacement or unchanged/skipped path depending on entry.
- Later read-back: Host configuration/rule files and sentinel-bracketed AGENTS.md guidance are intended for later host/model reads; precompact markers persist in SQLite.
- Delegated visibility: Host receives hook replies; instructions can reach the host's agent, but no sqz-owned worker context exists.
- Selection predicate: Installed client support, init options, host event/tool name, mode, shell shape and post-hook eligibility.
- Invalidation or expiry: Uninstall/removal can excise sqz guidance blocks and hooks; precompact marks older unpinned references stale, not model messages deleted.
- Activation or effect: Changes host mediation/configuration and requests agent tool-selection behavior; actual host activation/compliance unobserved.
- Evidence limits: Host permission semantics are an external contract. Generated rules neither prove execution nor cover every tool path.

Admission is operator-triggered installation followed by software-generated content; starting init is not separate human approval of each generated instruction. Writers can edit/remove guidance or uninstall. The shipped text is proposal-shaping guidance, not a generated theory criticism. No answer oracle or model-authored capability change is involved. Recovery removes/replaces installed files/blocks; external host state may require its own reload.

> When the sqz MCP tools are available, prefer `sqz_read_file`, `sqz_grep`
> and `sqz_list_dir` over the built-in read, grep and `ls` for long or
> repeated reads, and use `sqz_recall` to find output seen earlier.
> --- `sqz_engine/src/codex_integration.rs`

> pub const CLAUDE_ALLOW_RULES: [&str; 2] = ["Bash(set -o pipefail)", "Bash(sqz compress --cmd *)"];
> --- `sqz_engine/src/tool_hooks.rs`

### Claims

#### RT-CLM-recoverable-results
Label: MCP recoverability claim

SRC-1, `sqz-mcp/src/lib.rs`, declares deterministic offline compression and byte-exact recovery:

> LLM calls, offline, and every compressed result is recoverable byte-exact.
> --- `sqz-mcp/src/lib.rs`

Claim conclusion status: claimed

The account limits this to captured originals and surviving storage, distinguishes capped/decoded tool bodies from original files, and excludes no-cache/browser/HTTP history routes. [RT-RTE-cache-recovery](#rt-rte-cache-recovery) establishes wired recovery with an explicit compressed-only alternative, not the universal claim.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-host-guidance
Label: Host-mediated guidance authority

Consumer: external coding agent. Channel: installed AGENTS.md/client rules and MCP initialization instructions. Force: natural-language protocol requesting tool preference, ref interpretation and recovery, not deterministic enforcement of model behavior. Horizon: later sessions while files remain installed; proxy instructions last with the host's initialized connection/context. Storage is filesystem text or generated JSON instructions; representational form is natural language at the model consumer (SRC-1, `sqz_engine/src/codex_integration.rs`, `sqz-mcp/src/proxy.rs`; [RT-RTE-integration-install](#rt-rte-integration-install), [RT-RTE-mcp-proxy](#rt-rte-mcp-proxy)).

> Tool results pass through the sqz \
> compression proxy.
> --- `sqz-mcp/src/proxy.rs`

This requests behavioral authority but supplies no evidence of model compliance or exercised improvement. No theory-builder, reflection or self-improvement attribution is inferred from installing or retaining this guidance.

## Annotations

none
