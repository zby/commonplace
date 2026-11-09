---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "sqz's shipped context-compression and retention system at commit 495c078d8f4c94d060ecfbb4d919286670b87898."
run-id: AAS-2026-11-09-sqz-154fb86209ba-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "495c078d8f4c94d060ecfbb4d919286670b87898"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/ojuschugh1/sqz
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sqz-51a650c5586b/related-systems/ojuschugh1--sqz
  revision: "495c078d8f4c94d060ecfbb4d919286670b87898"
  sha256: null
---

# sqz boundary

## Boundary and evidence

This run examines sqz as a shipped context-compression and retention system for model-facing clients, not as an autonomous agent runtime. Its intended use is to reduce the material supplied to a model and let clients recover previously retained content. The target class is **memory/knowledge/context-engineering system**. Deterministic computation remains in scope because it serves model context; owning or issuing a model call is not a prerequisite for this class. SRC-1, `README.md`, declares:

> Pre-injection context compression and session deduplication for AI coding agents
> --- `README.md`

The boundary kind is **whole-system**: the repository's native engine, CLI callers, MCP server and proxy, state maintenance, generated agent guidance, browser implementation, IDE callers and shipped evaluation code are included. The library alone is not the target. These paths have distinct implementations and must not be assumed behaviorally equivalent merely because they share the sqz name. For example, SRC-1, `sqz-wasm/src/lib.rs`, exposes a separate `WasmEngine`, while the native facade is in `sqz_engine/src/engine.rs`.

The source is the entire registered repository at commit `495c078d8f4c94d060ecfbb4d919286670b87898`, acquired read-only; HEAD was checked against that pin. The applicability cutoff is **2026-11-09**, the supplied run date, not a claim that the source incorporates changes through that day. The overall evidence tier is **code-grounded**. Initial source inspection establishes entry-point and state-flow coverage, not exhaustive review of every module. All files at this commit remain available for later source inspection under SRC-1.

### Shipped loop and consumers

- **Native production and admission:** CLI dispatch in SRC-1, `sqz/src/main.rs`, reaches compression, hooks, recall, expand, import/export, resume, compact, reset and pin operations. `sqz/src/cli_proxy.rs` supplies command-aware interception; `sqz_engine/src/engine.rs` joins pipeline, routing, verification and cache admission. These callers belong to sqz, not to an excluded application.
- **Persistence and later consumption:** SRC-1, `sqz_engine/src/session_store.rs`, defines SQLite session and cache storage, including originals, alongside search indexes. `sqz-mcp/src/lib.rs` dispatches compression, read/search tools, recall and expand. CLI `cmd_resume` in `sqz/src/main.rs` loads stored sessions, constructs a snapshot and prints a guide. Presence of this consumer does not establish that every integration produces complete session records; producers and consumers must be traced separately in subsequent analysis.
- **Guidance and maintenance:** SRC-1, `sqz_engine/src/tool_hooks.rs`, generates client configuration and rules, including context-compaction integration. Its rule generator calls the shared guidance in `sqz_engine/src/codex_integration.rs`. This is part of the model-facing protocol, not incidental documentation:

> When the sqz MCP tools are available, prefer `sqz_read_file`, `sqz_grep`
> and `sqz_list_dir` over the built-in read, grep and `ls` for long or
> repeated reads, and use `sqz_recall` to find output seen earlier.
> --- `sqz_engine/src/codex_integration.rs`

- **MCP mediation:** SRC-1, `sqz-mcp/src/main.rs`, selects server versus upstream-proxy operation. `sqz-mcp/src/proxy.rs` contains response transformation, locally handled recovery tools and model instructions. Upstream MCP implementations are external, but sqz's relay, admission and recovery responsibilities remain included.
- **Browser consumers:** SRC-1, `extension/content/chatgpt.js`, supplies input getters/setters to shared interception in `extension/content/common.js`; acceptance can replace editor content and record statistics. `extension/background.js` loads the bundled WASM and answers compression messages. `extension-firefox/background.js` provides the Firefox loading path. Browser-local state is not assumed to use native SQLite.
- **IDE callers:** SRC-1, `vscode-extension/src/extension.ts`, registers commands through `vscode-extension/src/sqzBridge.ts`; the bridge invokes CLI compression and reads statistics. SRC-1, `jetbrains-plugin/src/main/kotlin/com/sqz/SqzPlugin.kt`, calls its `SqzBridge.kt` implementation. Both bridges include fallbacks. Inclusion does not certify compatibility of their arguments with the pinned CLI.
- **Evaluation:** SRC-1, `sqz/tests/quality_bench.rs`, is a shipped binary-level fixture evaluator, including critical-fact retention and recovery checks. Tests and benchmark reports are evidence of evaluation design or attributed results, not observed executions by this run.

The state-retention classification is supported by the executable cache path in SRC-1, `sqz_engine/src/engine.rs`:

> self.cache_manager.get_or_compress_with(
>             std::path::Path::new(""),
>             input.as_bytes(),
>             &|text| self.compress(text),
>         )
> --- `sqz_engine/src/engine.rs`

### Repository coverage

The table classifies every tracked top-level file or directory, grouping related entries. “Included” fixes analytical scope, not a claim that every contained file has already been read. Initial inspection below distinguishes tree inventory from traced material. All entries derive from SRC-1's pinned Git tree.

| Top-level entries | Scope and role; material paths | Initial inspection and limits |
|---|---|---|
| `sqz_engine/` | Included: native engine, state, transforms, integration generation, examples and module tests. Material paths include `src/engine.rs`, `src/pipeline.rs`, `src/cache_manager.rs`, `src/session_store.rs`, `src/session_continuity.rs`, `src/tool_hooks.rs`, `src/codex_integration.rs`, other integration modules, `src/api_proxy.rs`, `src/cmd_formatters/`, `src/verifier.rs`, `src/context_evictor.rs`, `src/pin_manager.rs`, `examples/` and regression inputs. | Facade, module register, storage schema and shared guidance inspected; detailed transform and maintenance algorithms remain for analyst inspection. Not an access gap. |
| `sqz/` | Included: shipped CLI producer, maintenance and consumption paths. `src/main.rs`, `src/cli_proxy.rs`, `src/post_hook.rs`, `src/shell_hook.rs`, `src/replay.rs`, `src/doctor.rs`, `src/vizit.rs`, `tests/`, embedded tests and completions. | Dispatch and compression/retention references searched; resume and compact entry inspected; quality evaluator inspected. Other callers remain available, not excluded. |
| `sqz-mcp/` | Included: `src/main.rs`, `src/lib.rs`, `src/proxy.rs`, `tests/stdio.rs`, package manifests and licenses. | Main, tool dispatch, compression and recall handlers, and proxy state/protocol inspected. Detailed relay and transport behavior remains available. |
| `sqz-wasm/` | Included: browser-facing independent engine and state import/export in `src/lib.rs`, manifests and licenses. | Public constructor/compress/import/export inspected; internal algorithms not exhaustively inspected. |
| `extension/`, `extension-firefox/` | Included: manifests, `background.js`, site scripts under `content/`, popup configuration/statistics, WASM glue/binaries, browser tests, Firefox build script and packaged archive. | Chrome shared interception, ChatGPT adapter and both background loaders inspected. Remaining site adapters and package bytes inventoried, not inspected; no claim of site-wide correctness or source-to-binary equivalence. |
| `vscode-extension/` | Included: `package.json`, `src/extension.ts`, `src/sqzBridge.ts`, `src/statusBar.ts`, tests and build configuration. | Command registration searched and compression/statistics bridge inspected. Other commands/tests not exhaustively inspected. |
| `jetbrains-plugin/` | Included: `src/main/kotlin/com/sqz/` bridge, plugin, file listener and status widget; plugin descriptor, tests and build files. | Plugin caller searched and bridge compression inspected. Other components inventoried, not deeply inspected. |
| `npm/`, `python/`, `pyproject.toml`, `install.sh`, `install.ps1` | Included: installation, package entry points and binary selection, including `npm/bin/sqz`, `npm/bin/sqz-mcp`, `npm/install.js`, `python/sqz/__main__.py`. | npm CLI delegation inspected; Python downloader entry inspected. Other installer paths inventoried. Downloaded release artifacts are not frozen by these scripts. |
| `.claude/`, `.cline/`, `.clinerules/`, `.gemini/`, `.windsurf/`, `opencode.json` | Included: repository-local integration settings and hook examples, including `.clinerules/hooks/PreToolUse`. | Tree inventory only; configuration is not evidence that a host executed it. |
| `presets/`, `completions/` | Included: code-review/debug/docs preset inputs and shell completion surfaces. | Inventoried; detailed configuration semantics remain available. |
| `docs/`, `README.md`, `llms.txt`, `BENCHMARKS.md`, `CHANGELOG.md` | Included: declared system design, client contracts, integration instructions, benchmark claims and paper sources. Material paths include `docs/integrations/`, `docs/quality-benchmark.md`, `docs/benchmark.md`, `docs/whitepaper.md`, `docs/arxiv/` and `docs/stop-rereading-files.md`. | README opening/use/evaluation claims inspected. Remaining documentation inventoried; claims require attribution and code checks, not automatic acceptance. |
| `demo/`, `assets/` | Included: `demo/auth.py`, `demo/cargo-test.txt`, demo instructions, `assets/demo.tape` and presentation diagrams/media. | Inventoried; no demonstration replay or verification of claimed measurements. |
| `Cargo.toml`, `.cargo/`, `Dockerfile`, `distribution/`, `.github/` | Included: build/deployment and distribution surfaces, including `distribution/docker/`, `distribution/mcp-registry/server.json`, `.github/workflows/benchmarks.yml` and release/publication workflows. | Workspace membership inspected; remaining files inventoried. No deployed build or registry behavior established. |
| `book.toml`, `i18n/` | Included: documentation build and translated descriptions, glossary/check tooling and tests. | Inventoried, not inspected for semantic parity; no translation-parity conclusion. |
| `.gitignore`, `.well-known/`, `funding.json`, `CLA.md`, `CONTRIBUTING.md`, `LICENSE-APACHE`, `LICENSE-MIT` | Excluded from functional analysis: repository hygiene, funding, contribution process and legal material. | Inventory establishes presence only. Exclusion prevents conclusions about licensing compliance, contributor governance or funding infrastructure; none is needed for the context-state loop. |

### External boundary and evidence limits

External dependencies include Rust/library dependencies, local OS shell/process/filesystem/SQLite facilities, browser extension APIs and DOMs, IDE plugin APIs, agent host hook/MCP support, upstream MCP servers and model services. Their implementations are not registered evidence. The shipped sqz integration code is included; external host scheduling, context compaction, actual retention of an earlier model-visible message and the model's interpretation of reference tokens are not attributed to sqz merely because its guidance expects them (SRC-1, `Cargo.toml`, `sqz_engine/src/tool_hooks.rs`, `sqz-mcp/src/proxy.rs`, `extension/content/common.js`).

No target execution, dependency installation, model call or experiment was performed. The absence of a supplied execution trace prevents conclusions about installed-client reliability, measured end-to-end model quality, actual token billing, or causal improvement from compression. README and benchmark numbers remain reported operation unless backed by inspectable run evidence at this pin. No live documentation, linked external benchmark, release download, marketplace build, or upstream repository is added to the evidence boundary. Their exclusion prevents conclusions about deployed versions and external comparisons. Available but not-yet-inspected source is not an access gap.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ojuschugh1/sqz` | 495c078d8f4c94d060ecfbb4d919286670b87898 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sqz-51a650c5586b/related-systems/ojuschugh1--sqz`. Implementation: pinned tree; workspace; native entry/facade/storage; MCP dispatch/proxy; WASM public API; browser interception/loaders; IDE bridges; package launchers; quality evaluator. Doctrine/design: README intent, generated agent guidance and source protocol comments. Reported operation: README token-saving and quality claims, not independently reproduced. Paths in the coverage table beyond these initial reads remain available under this same ID. | Implementation: [CLI](https://github.com/ojuschugh1/sqz/blob/495c078d8f4c94d060ecfbb4d919286670b87898/sqz/src/main.rs), [engine](https://github.com/ojuschugh1/sqz/blob/495c078d8f4c94d060ecfbb4d919286670b87898/sqz_engine/src/engine.rs), [MCP](https://github.com/ojuschugh1/sqz/blob/495c078d8f4c94d060ecfbb4d919286670b87898/sqz-mcp/src/lib.rs), [browser](https://github.com/ojuschugh1/sqz/blob/495c078d8f4c94d060ecfbb4d919286670b87898/extension/content/common.js). Doctrine/design: [guidance](https://github.com/ojuschugh1/sqz/blob/495c078d8f4c94d060ecfbb4d919286670b87898/sqz_engine/src/codex_integration.rs). Reported operation: [README](https://github.com/ojuschugh1/sqz/blob/495c078d8f4c94d060ecfbb4d919286670b87898/README.md). | No source-access failure found. External clients/providers and downloaded builds are outside the frozen evidence. No supplied observed run or causal experiment; implementation and reported operation do not establish end-to-end efficacy. |
