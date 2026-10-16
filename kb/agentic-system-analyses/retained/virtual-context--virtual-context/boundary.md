---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Virtual Context's repository-shipped context and memory system at commit 74ccc570c40bb551820fcd330c42e0dfc0588f05, including its callers, maintenance surfaces and evaluators."
run-id: AAS-2026-10-14-virtual-context-bbd06cc3ac95-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "74ccc570c40bb551820fcd330c42e0dfc0588f05"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/virtual-context/virtual-context
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/virtual-context-bbd06cc3ac95/related-systems/virtual-context--virtual-context
  revision: "74ccc570c40bb551820fcd330c42e0dfc0588f05"
  sha256: null
---

# Virtual Context boundary

## Boundary and evidence

This run analyses the repository-shipped Virtual Context system for retaining conversation history and assembling bounded context for later model calls. It includes the Python engine, proxy, MCP surface, bundled OpenClaw integration, interactive and headless chat drivers, import and administrative paths, state stores, model-facing prompts, optional community and engagement mechanisms, and repository evaluators. It is not a review of only the library API. The target class is **memory/knowledge/context-engineering system** and the boundary kind is **whole-system**: the functional boundary covers production, persistence, maintenance, admission and later consumption of retained content across shipped paths.

The target is in scope because its memory operation includes model calls, rather than merely returning a deterministic database result. For example, completed-turn tagging delegates to a configured language model (SRC-1, `virtual_context/core/tag_generator.py`):

> response, _usage = self.llm.complete(
>     system=system,
>     user=prompt,
>     max_tokens=self.config.max_tokens,
> )
> --- `virtual_context/core/tag_generator.py`

The installed command is registered as `virtual-context = "virtual_context.cli.main:main"` in SRC-1, `pyproject.toml`. Its chat dispatch includes the bundled headless driver, not just an external host. The engine's blocking completion method joins tagging and compaction (SRC-1, `virtual_context/engine.py`):

> signal = self.tag_turn(conversation_history, payload_tokens)
> if signal is None:
>     return None
> return self.compact_if_needed(conversation_history, signal)
> --- `virtual_context/engine.py`

Initial boundary inspection traced the following shipped consumers and maintenance paths. These traces establish inclusion, not verified correctness of every branch:

- **Proxy:** CLI proxy dispatch and ASGI construction lead to request preparation, inbound engine assembly, upstream response handling and background completion. Include `virtual_context/proxy/server.py`, `virtual_context/proxy/handlers.py`, `virtual_context/proxy/continuation.py` and `virtual_context/proxy/state.py`. Session restoration and caching are part of this path, not external memory responsibilities: include `virtual_context/proxy/session_state.py`, `virtual_context/proxy/session_cache.py` and the engine's persisted-state recovery. The store read is explicit in SRC-1, `virtual_context/engine.py`:

> saved = self._store.load_engine_state(self.config.conversation_id)
> --- `virtual_context/engine.py:1593-1593`

- **Interactive and headless chat:** `virtual_context/cli/main.py` dispatches to `virtual_context/tui/app.py` or `virtual_context/tui/headless.py`. They build context before provider calls and complete the engine cycle after collecting replies. `virtual_context/tui/state.py` exports turn records and reloads user prompts for replay; that replay is not a lossless restoration of all session state. These drivers remain inside the boundary even though they supply the engine with conversation history. The headless consumer uses the assembled block directly (SRC-1, `virtual_context/tui/headless.py`):

> assembled = self.engine.on_message_inbound(
>     user_message, self._conversation_history
> )
> timing["inbound_ms"] = round((time.perf_counter() - t0) * 1000, 1)
> system_text = assembled.prepend_text
> --- `virtual_context/tui/headless.py`

- **MCP and OpenClaw:** `virtual_context/mcp/server.py` exposes retrieval, compaction, paging, resources and prompts around a lazy engine. The bundled `virtual_context/openclaw/virtual-context.mjs` invokes CLI `transform` before context transmission and CLI `compact` after an agent ends. Its hook wiring belongs to this source; the separately linked OpenClaw plugin repository and the enclosing OpenClaw runtime do not.
- **Import and repair:** `virtual_context/cli/import_cmd.py` converts exports through `virtual_context/import_adapters/`, ingests them into an engine bound to each conversation, and optionally compacts. CLI admin operations, `virtual_context/core/record_editing.py`, community rebuilds, storage mutation guards and the dated canonical-history repair scripts remain included. The record editor makes the host authorization boundary explicit (SRC-1, `virtual_context/core/record_editing.py`):

> Who may call these operations is the host's decision; the engine records the
> ``actor`` it is given.
> --- `virtual_context/core/record_editing.py`

- **Optional engagement:** include `virtual_context/core/engagement/runner.py` and its selection, composition, source verification, posting and history modules. This is a shipped use of retained information, not a reason to classify the entire target as an enclosing agent runtime. Its source fetcher, sender and model callables come from the caller; externally supplied scheduling and credentials remain outside the target. SRC-1, `virtual_context/core/engagement/runner.py` states:

> This is the entrypoint something outside the process invokes once a day. It
> installs nothing, schedules nothing and holds no credential: every capability
> that reaches the world — the source fetcher, the sender, the models — arrives
> as a callable the caller supplies, so this module can be read end to end
> without wondering what it can reach.
> --- `virtual_context/core/engagement/runner.py`

- **Evaluators:** include the memory ingestion, compaction, checkpointing and reader-tool paths in `benchmarks/longmemeval/vc_runner.py`, `benchmarks/locomo/vc_runner.py`, `benchmarks/beam/vc_runner.py` and `benchmarks/mrcr/vc_runner.py`, plus `benchmarks/amb/vc_provider.py`, the typed-judgment harness under `benchmarks/jev/`, and offline context contracts under `benchmarks/context_contracts/`. Initial searches traced the four reader runners through `ingest_history`, `compact_manual`, `_save_state`, `on_message_inbound` and `query_with_tools`. Evaluator code is implementation evidence about how evaluation is conducted, not evidence that a benchmark was run successfully.

### Repository coverage

Every top-level tracked entry is classified below. All rows refer to SRC-1; paths are commit-relative. “Included” means within the evidence and functional boundary, not fully audited during boundary declaration. The initial inspection used the tracked tree, entry-point source reads and scoped searches. Remaining source inspection is work for later jobs at the same pin. Available but unread bodies are **not yet inspected**, not access gaps. No material shipped path is excluded merely because it is optional, a CLI caller or outside the wheel.

| Top-level entry | Status | Material paths and role | Initial inspection / exclusion limit |
|---|---|---|---|
| `.github/` | Included | `.github/workflows/contracts.yml`, `.github/workflows/python-publish.yml`: contract checks, package checks and release workflow | Workflow searches; not evidence of successful CI or a deployed release. |
| `.gitignore` | Excluded | Repository hygiene | Tree only; no conclusions about completeness of ignored local artifacts. |
| `LICENSE` | Excluded | Licensing text | Tree only; no legal assessment. |
| `README.md` | Included | Declared product purpose, SDK and integration surfaces, reported benchmark results and limits | Fully read as doctrine and attributed reporting; claims require implementation or run evidence when used beyond that layer. |
| `assets/` | Excluded | `assets/dashboard.png`, `assets/hero.png`: illustrations | Images not inspected; no inference about the illustrated hosted deployment or its measured capacity. |
| `benchmarks/` | Included | `longmemeval/`, `locomo/`, `beam/`, `mrcr/`: dataset ingestion, memory reuse and reader loops; `amb/vc_provider.py`: external benchmark adapter; `jev/`: judgment evaluations; `context_contracts/`: offline assembly and paging contracts | Caller-chain searches and context-contract README read; detailed judges, datasets, scoring and reported results not yet inspected. External corpora and run artifacts not supplied cannot support reproduced scores. |
| `bugs.md` | Included | Source-native defect record | Listed, body not yet inspected; may supply attributed reported operation, not independent verification. |
| `docs/` | Included | `architecture.md`, `engine.md`, `fact-lifecycle.md`, `attribution.md`, `proxy.md`, `proxy-continuations.md`, `native-vector-search.md`, `configuration.md`, `commands.md`, `install.md`, `design.md`, `benchmarks.md`: design, lifecycle, maintenance, integration and evaluation contracts | Architecture fully read; other bodies not yet inspected. Documentation describes intended behavior, not measured runtime behavior. |
| `models.yaml` | Included | Root model/pricing catalogue | Scoped search; data interpretation not yet audited. |
| `pyproject.toml` | Included | Package dependencies, CLI entry point, wheel/data packaging and test policy | Fully read. |
| `scripts/` | Included | `install.sh`, `install.ps1`: installation; `check_contracts.py`, `smoke_recommended.py`, `smoke_recommended.sh`: verification; `export_discord_guild_transcript_20260802.py`, `rebuild_men_canonical_from_discord_20260802.py`, `extend_men_vast_disposition_20260802.py`, `apply_canonical_repair_artifact_20260802.py`: source export, disposition, canonical repair and application | Repair/export and contract/smoke source searches; complete script bodies and externally referenced repair inputs not yet inspected. Code presence does not establish that a repair was applied. |
| `tests/` | Included | `test_engine*`, `test_ingestion*`, `test_compaction*`, `test_canonical*`, `test_actor*`, `test_fact*`, `test_retrieval*`, `test_*store*`, `test_record_editing.py`, `test_mcp_server.py`, `test_headless.py`, `test_tui.py`, `test_engagement*`, `proxy/`, `haiku/`, `ollama/`, fixtures and `REGRESSION_MAP.md`: contracts and regression evidence across the loop | Tracked test tree inspected for coverage surfaces; assertions and fixtures not yet examined. Tests are not executed in this run. |
| `tests_by_section.sh` | Included | Subsystem test selection driver | Listed, body not yet inspected; no inference about suite outcomes. |
| `uv.lock` | Included | Frozen dependency resolution | Listed, entries not yet inspected; no installed-environment equivalence claim. |
| `virtual-context.yaml` | Included | Tracked agentic-preset configuration | Scoped search; not treated as the configuration of every consumer. |
| `virtual-context.yaml.example` | Included | Reference settings, custom summarization prompts and provider/storage options | Scoped search of settings and prompt surfaces; detailed defaults not yet audited. |
| `virtual_context/` | Included | `engine.py`, `types.py`, `config.py`, `conversation_identity.py`: orchestration and contracts; `core/tagging_pipeline.py`, `core/ingest_reconciler.py`, `core/compaction_pipeline.py`, `core/compactor.py`: production and maintenance; `core/community/`, `ingest/`: source admission, attribution, cards, fact curation and supersession; `core/retrieval_assembler.py`, `core/assembler.py`, `core/hint_builder.py`, `core/paging_manager.py`, `core/tool_loop.py`, `core/tool_query.py`, search modules: admission and consumption; `storage/`: canonical persistence, ledgers, mutation guards and utility backends; `proxy/`: request/response drivers, state and dashboard edits; `cli/`, `import_adapters/`, `mcp/`, `openclaw/`, `tui/`: shipped callers; `core/engagement/`: optional memory-consuming workflow; `providers/`, `presets/`, `data/`: model calls, configuration and bundled data | Engine API/recovery, driver, MCP, import, record-editor and engagement source reads; model-call, prompt, proxy-state, store-schema and state-cache searches. Remaining detailed implementation, prompts, backend utilities, UI and bundled data are not yet inspected. |

### Frozen evidence and external limits

The sole frozen source is the acquired Git object, unchanged, at commit **74ccc570c40bb551820fcd330c42e0dfc0588f05**. HEAD matched that revision during inspection. The applicability cutoff is **2026-10-14**, the supplied run date; it does not assert the date of a deployment or a benchmark run. The overall tier is **code-grounded**, with source-native documentation and reported results distinguished from inspected implementation. The register grants later jobs access to all files at this revision, not merely the initial inspected paths.

External dependencies include model-provider HTTP services and credentials, embedding models and their supporting libraries, optional PostgreSQL/pgvector and Redis services, optional MCP/TUI/proxy frameworks, host transport metadata and authorization, and benchmark datasets or evaluation services. Dependency declarations are inspectable in SRC-1, `pyproject.toml`; service implementations and live instances are not frozen by this checkout.

Excluded external applications include Claude Code, Cursor, other base-URL clients, the enclosing OpenClaw runtime and separate plugin repository, and the hosted service's untracked adapters, tenant authorization and deployment infrastructure. The prepared-payload interface and engine responsibilities remain included; an external REST host's endpoints and completion-delivery guarantees are not attributed to this repository. These exclusions prevent conclusions about end-to-end authorization, host hook delivery, cloud operational equivalence, production isolation and live multi-worker reliability. External source transcripts and databases referenced by repair scripts are unavailable here; the scripts support mechanism analysis, not a conclusion that a particular repaired history is faithful.

No target execution, provider call, service setup or test run was performed. No independently inspected run trace or causal intervention is registered. Consequently, static paths and source-native reports cannot establish realized answer quality, benchmark reproducibility, cost, latency, deployment scale or operational success. This is an evidence limitation, not a missing source-code access claim and not a restriction to a partial library loop.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/virtual-context/virtual-context` | 74ccc570c40bb551820fcd330c42e0dfc0588f05 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/virtual-context-bbd06cc3ac95/related-systems/virtual-context--virtual-context`. Implementation: tracked tree; `pyproject.toml`; `virtual_context/__init__.py`; selected engine API and persisted-state recovery; CLI chat/import and admin/entry-point searches; TUI/headless and replay/export state; MCP retrieval/compaction; bundled OpenClaw hooks; proxy prepare/completion/state/cache searches and completion source; record-editor source; engagement runner source and compose/history searches; tagger model-call source; compactor prompt searches; SQLite/PostgreSQL schema and checkpoint searches; benchmark caller-chain, contract-runner and judgment-runtime searches; repair/export and smoke/contract script searches; workflow and root-config searches. Doctrine/design: `README.md`, `docs/architecture.md`, `benchmarks/context_contracts/README.md`, inspected module contracts. Reported operation: README's attributed product and benchmark reports only; no run artifact verified. | Implementation: [package entry point](https://github.com/virtual-context/virtual-context/blob/74ccc570c40bb551820fcd330c42e0dfc0588f05/pyproject.toml), [engine](https://github.com/virtual-context/virtual-context/blob/74ccc570c40bb551820fcd330c42e0dfc0588f05/virtual_context/engine.py), `virtual_context/tui/headless.py`, `virtual_context/tui/state.py`, `virtual_context/cli/import_cmd.py`, `virtual_context/mcp/server.py`, `virtual_context/openclaw/virtual-context.mjs`, `virtual_context/proxy/server.py`, `virtual_context/proxy/state.py`, `virtual_context/proxy/continuation.py`, `virtual_context/proxy/session_state.py`, `virtual_context/core/tag_generator.py`, `virtual_context/core/record_editing.py`, `virtual_context/core/engagement/runner.py`, `benchmarks/longmemeval/vc_runner.py`. Doctrine/design: [architecture](https://github.com/virtual-context/virtual-context/blob/74ccc570c40bb551820fcd330c42e0dfc0588f05/docs/architecture.md), `benchmarks/context_contracts/README.md`. Reported operation: `README.md`. | No access gap established for tracked source. Not-yet-inspected files remain available at the pin. Unfrozen external services, hosts, benchmark corpora/results and repair input artifacts prevent deployment, reproduced-performance and particular-repair conclusions. No observed-run or causal-experiment layer established. |
