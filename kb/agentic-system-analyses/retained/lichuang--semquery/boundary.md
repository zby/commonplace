---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "semquery's shipped document indexing, persistent retrieval and model-backed answer system at commit 0820927160b1400990fa8cc057807c73bbf6d025."
run-id: AAS-2026-11-09-semquery-b21559990932-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "0820927160b1400990fa8cc057807c73bbf6d025"
analysis-cutoff: "2026-11-09"
evidence-tier: code-grounded
source:
  identity: https://github.com/lichuang/semquery
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/semquery-078b07358ebc/related-systems/lichuang--semquery
  revision: "0820927160b1400990fa8cc057807c73bbf6d025"
  sha256: null
---

# semquery boundary

## Boundary and evidence

This run covers semquery as shipped: the `semq` CLI, public Rust `Engine` facade and six supporting crates. Its intended use is local document search and cited question answering, not ownership of an autonomous agent's enclosing execution loop. The target class is **memory/knowledge/context-engineering system** because it produces persistent document representations, reloads them for retrieval and supplies retrieved content to a model-backed answer path. The boundary kind is **whole-system**: the shipped CLI that admits collections, triggers maintenance and consumes the persisted index is included, not treated as an external library caller. Evidence: SRC-1, `crates/semquery/Cargo.toml`, `crates/semquery/src/main.rs`, `crates/semquery/src/lib.rs`, `crates/semquery/src/engine.rs`.

The source describes the product's intent directly:

> `semquery` (short for **semantic query**) is a local, offline-ready RAG tool written in Rust. It indexes your personal document collections and lets you search or ask questions with cited answers — everything stays on your machine: indexes, models, and queries.
> --- `README.md`

The executable entry point is `semq`; `run_add` registers a canonical file or directory and drives indexing, including an all-collection reindex when the stored baseline differs from configuration. `Engine::open` reopens workspace storage without immediately loading models. The indexer reads supported files, chunks and embeds changed content, stores document/chunk associations and retrieval representations, and sweeps removed files. Search reloads retained chunks through concurrent keyword/vector recall, fusion and reranking. Ask retrieves chunks, constructs a citation-bearing prompt, invokes a local LLM and returns an answer. These are included responsibilities, not inferred responsibilities of a future agent host. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-indexer/src/indexer.rs`, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-retrieve/src/retriever.rs`, `crates/semquery-synth/src/synthesizer.rs`.

The source explicitly connects reopened state to deferred model-backed consumption:

> /// Open an engine without loading any models: no network access, no
> /// model-cache resolution. This is the canonical entry point —
> /// storage-level operations (`status`, `list_collections`,
> /// `add_collection`, `remove_collection`) work immediately, and
> /// model-backed operations (`index`, `search`, `ask`, plus their streaming
> /// variants) lazily load the models they need on first use, emitting
> /// `ModelDownloadStart` / `ModelDownloadComplete` events when a model file
> /// actually hits the network.
> --- `crates/semquery/src/engine.rs`

The answer path issues a model call rather than merely exposing a passive index:

> let prompt = build_ask_prompt(query, &hits);
> stats.prompt_ms = prompt_start.elapsed().as_millis() as u64;
> --- `crates/semquery-synth/src/synthesizer.rs`

> let raw = llm.complete_stream(&prompt, &mut on_token).await?;
> --- `crates/semquery-synth/src/synthesizer.rs`

The frozen evidence is SRC-1 at full commit `0820927160b1400990fa8cc057807c73bbf6d025`; the applicability cutoff is **2026-11-09**. HEAD was checked against the acquired pin. The evidence tier is **code-grounded**. This is source inspection, not target execution: test bodies and the integration driver establish shipped verification intent, not successful runs, measured retrieval quality, citation faithfulness or performance.

### Shipped-path coverage

Every top-level tracked file or directory is classified below. Included means within the functional/evidence boundary, not that every line has already been inspected. Initial inspection follows the shipped state producer, maintenance path, reload path and consumers. Unread implementation details remain available to later source inspection at the same pin; they are not access gaps.

| Top-level path | Status | Material paths, role and initial inspection | Exclusion or inspection limit |
|---|---|---|---|
| `.cargo/` | Included | `.cargo/config.toml`: native build/backend environment, read | Configuration is not evidence of GPU availability in a run. |
| `.github/` | Excluded | `workflows/release.yml`: release automation, tree inventoried only | No conclusion about actual release publication or CI success. |
| `.gitignore` | Excluded | Repository housekeeping, tree inventoried only | No conclusion about developer-local ignored state. |
| `AGENTS.md` | Included | Source-native architecture and maintenance doctrine; read as evidence, not binding instructions | Declared design does not override inspected implementation. |
| `CHANGELOG.md` | Included | Shipped change history, inventoried but not yet inspected | No historical-change claims established here. |
| `Cargo.lock` | Included | Dependency lock, inventoried but not yet inspected in detail | No dependency audit or reproducible-build claim. |
| `Cargo.toml` | Included | Workspace crate membership and dependency wiring, read | Dependency internals outside this repository are not captured. |
| `LICENSE` | Excluded | Licensing artifact, tree inventoried only | No legal/license assessment. |
| `README.md` | Included | Product purpose, CLI usage, architecture and roadmap, read | Comparison table is attributed documentation, not independent comparative evidence. |
| `cliff.toml` | Excluded | Changelog tooling, tree inventoried only | No changelog-generation assessment. |
| `crates/` | Included | `semquery/src/{main,engine,lib}.rs`: shipped CLI and library entry points, collection admission/deletion, lazy model setup, reindex decision, persisted-state reopen and search/ask consumers; read. `semquery/src/config.rs`: configuration and system-prompt surface, searched. `semquery-core/src/{traits,models}.rs`: shared state and model/storage interfaces, searched. `semquery-indexer/src/indexer.rs`: content-change preparation, embedding/storage writes and deleted-file sweep, read selected implementation ranges; `reader_registry.rs`: file admission/dispatch, read implementation; `chunker.rs`: chunking interface, searched; `reader/` and `tokenizer.rs`: included extraction/tokenization implementations, not yet inspected directly. `semquery-storage/src/sqlite.rs`: workspace database open and vector initialization read; schema and mutation surfaces searched. `semquery-retrieve/src/retriever.rs`: search pipeline read, evaluator names searched; `fusion.rs` included, not yet inspected directly. `semquery-model/src/{hub,gguf}.rs`: cache resolution/download and local inference entry read; `embed.rs` and `rerank.rs` interfaces searched; `registry.rs` included, not yet inspected directly. `semquery-synth/src/{prompt,synthesizer}.rs`: grounding prompt and streaming model consumer read; `citation.rs` included, not yet inspected directly. Inline tests include Engine reopen, indexing, deletion and answer checks; Engine tests read. | Initial inspection establishes the complete shipped responsibility chain, not exhaustive correctness of every extractor/backend or passing test results. |
| `docs/` | Included | `optimize.md` and `todo.md`: source-native optimization/maintenance records, inspected selected ranges | Intent, reported operation and historical diagnoses require implementation checks before use as present behavior; not observed-run evidence. |
| `pre-commit-check.sh` | Included | Shipped check/test/fmt/lint driver, read | Not executed; no check-success claim. |
| `rust-toolchain.toml` | Included | Build toolchain pin, inventoried but not yet inspected | No local compilation claim. |
| `rustfmt.toml` | Excluded | Formatting configuration, tree inventoried only | No formatting-policy assessment. |
| `scripts/` | Excluded | `publish-crate.sh`: package publishing driver, tree inventoried only | No crate publication or supply-chain process assessment. |
| `test-integration.sh` | Included | Shipped CLI driver: init, add/index, ask/search, status, document/collection deletion and post-deletion consumption; read | Driver source only, not an execution trace or answer-quality evaluator. |
| `testdata/` | Included | `README.md`, `md/`, `pdf/`, `docx/`: bundled corpus used by the integration driver, tree inventoried; driver reference inspected | Corpus contents not yet inspected; no representativeness, extraction-quality or benchmark claim. |
| `vendor/` | Included | `esaxx-rs/`: vendored tokenizer dependency; tree inventoried and root Cargo patch rationale read | Dependency implementation not yet inspected; no suffix-array/tokenizer correctness or platform-compatibility conclusion. |

### External dependencies and limits

Local filesystem documents are inputs; authoring those documents is outside semquery's shipped responsibilities. The SQLite/FTS5/sqlite-vec and FastEmbed/ONNX/llama.cpp implementations are dependencies rather than separately frozen repositories. ModelHub resolves model files through Hugging Face's hub/cache API. Source includes their integration contracts but not downloaded weights or an actual user's workspace. Consequently, this run can explain the persistence/retrieval/inference wiring, not certify model artifacts, offline readiness of a particular installation, extraction fidelity or real-world answer quality. Evidence: SRC-1, `Cargo.toml`, `crates/semquery-model/src/hub.rs`, `crates/semquery-model/src/gguf.rs`, `crates/semquery-storage/src/sqlite.rs`, `crates/semquery-indexer/src/reader_registry.rs`.

Downstream applications embedding the library are not frozen here. The facade explicitly mentions downstream embedding, but their task policies and lifecycle cannot be attributed to semquery (SRC-1, `crates/semquery/src/lib.rs`). Planned MCP integration is not a shipped host loop: the README lists it as roadmap material (SRC-1, `README.md`). No separate host repository, live web page, model download, runtime trace or causal experiment is registered. There is no unavailable repository path blocking initial boundary establishment; deliberate exclusions and material not yet inspected are distinguished above.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/lichuang/semquery` | 0820927160b1400990fa8cc057807c73bbf6d025 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/semquery-078b07358ebc/related-systems/lichuang--semquery`. Implementation: workspace/package manifests, CLI and Engine, Engine inline tests, selected indexer/storage/retriever/model/synth implementation, reader registry and integration/check drivers as detailed above. Doctrine/design: README, AGENTS, selected optimization/maintenance documentation. Reported operation: selected `docs/todo.md` entries, not independently verified. | [CLI](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/crates/semquery/src/main.rs), [Engine](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/crates/semquery/src/engine.rs), [indexer](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/crates/semquery-indexer/src/indexer.rs), [retriever](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/crates/semquery-retrieve/src/retriever.rs), [prompt](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/crates/semquery-synth/src/prompt.rs), [design](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/README.md), [maintenance/reported operation](https://github.com/lichuang/semquery/blob/0820927160b1400990fa8cc057807c73bbf6d025/docs/todo.md) | No initial source-access gap. No observed run or causal experiment supplied; prevents operational-success, measured-quality and causal-performance conclusions. External model weights, dependency internals and downstream hosts are not frozen evidence. |
