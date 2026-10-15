---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Engraph's shipped vault knowledge service, CLI, maintenance paths and agent instructions at commit f9a95bc96accc792c02ee384d9e6bf768a88c8c8."
run-id: AAS-2026-10-14-engraph-0cd4f00695b0-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: f9a95bc96accc792c02ee384d9e6bf768a88c8c8
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/devwhodevs/engraph
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/engraph-0cd4f00695b0/related-systems/devwhodevs--engraph
  revision: f9a95bc96accc792c02ee384d9e6bf768a88c8c8
  sha256: null
---

# Engraph boundary

## Boundary and evidence

Engraph is in scope as a **memory/knowledge/context-engineering system**: a local Markdown-vault knowledge service that produces retained notes and derived indexes, maintains them, and returns searches and context to agents. It is not the enclosing conversational agent runtime. Its own retrieval issues embedding calls and optionally query-orchestration and reranking calls. The whole-system boundary includes the shipped binary and library, CLI callers, MCP and HTTP adapters, onboarding and identity, file synchronization, note-writing and migration paths, agent-facing skills, setup prompts and test definitions. These are parts of the target, not excluded applications merely because they call library functions (SRC-1, `src/main.rs`, `src/lib.rs`, `src/serve.rs`, `src/http.rs`, `src/search.rs`, `README.md`).

The intended use is to explain how a user's vault becomes persistent, searchable agent context, including the return path from agent-requested writing to later retrieval. The repository declares that purpose:

> engraph turns your markdown vault into a searchable knowledge graph that any AI agent can query
> --- `README.md`

The implementation establishes model-dependent consumption, rather than only a static tool catalog:

> let query_vec = embedder
>             .embed_one(expanded_query)
>             .context("embedding query")?;
> --- `src/search.rs`

Persistence, maintenance and reuse belong to the same shipped system. The CLI opens the stored vault and calls the writer; note creation writes Markdown and inserts chunks, vectors, full-text entries and edges. The server opens `engraph.db`, obtains its saved vault path, loads models and starts the watcher. Startup reconciliation runs the shared indexer before consuming filesystem events. Search handlers pass the shared store and loaded models to retrieval; context handlers return retained note content or assembled bundles (SRC-1, `src/main.rs`, `src/writer.rs`, `src/indexer.rs`, `src/serve.rs`, `src/watcher.rs`, `src/context.rs`). Identity extraction and formatting are also included: freshly indexed vault facts can subsequently supply the identity response (SRC-1, `src/indexer.rs`, `src/identity.rs`, `src/http.rs`).

> let store = Store::open(&db_path)?;
>     let config = Config::load()?;
>     let embedder = crate::llm::LlamaEmbed::new(&models_dir, &config)?;
> --- `src/serve.rs`

> let search_output = crate::search::search_internal(topic, 5, params.store, embedder)?;
>     context_topic_from_results(params, topic, &search_output.results, max_chars)
> --- `src/context.rs`

The boundary is **whole-system**, not only the retrieval library or MCP interface. The table below classifies every top-level tracked file or directory at the frozen commit. “Included” makes the paths available to later source inspection; it does not claim that every implementation detail has already been inspected. Initial inspection traced entry points and the material state loop. Supporting module internals not yet read are identified explicitly, not treated as unavailable evidence.

| Top-level tracked path | Inclusion and material paths / role | Initial inspection and limits |
| --- | --- | --- |
| `.claude-plugin/` | Included: `marketplace.json` wires the shipped skill directory and MCP launch command. | Read; declares `engraph serve` as the client launch path. Does not demonstrate a successful installation. |
| `.github/` | Included: `workflows/ci.yml` and `workflows/release.yml`, test/build and distribution declarations. | CI read; release workflow not yet inspected. No captured workflow results support build or release success. |
| `.gitignore` | Excluded: repository housekeeping. | No conclusion about repository ignore-policy correctness. Vault indexing exclusions remain included in source code. |
| `CHANGELOG.md` | Included: release-intent/history documentation. | Not yet inspected; no historical behavior inferred from it. |
| `CLAUDE.md` | Included: shipped developer maintenance instructions and architecture assertions. | Read as doctrine/design, not proof of current tool counts or passing tests. |
| `CONTRIBUTING.md` | Included: contributor maintenance instructions. | Not yet inspected; no contribution-process assessment. |
| `Cargo.lock` | Included: dependency resolution artifact. | Not yet inspected; no dependency-security or exact transitive-library assessment. |
| `Cargo.toml` | Included: package, library/binary dependencies and feature declarations. | Read; Rust package version 1.7.2 and local inference/server/storage dependencies. |
| `LICENSE` | Excluded: legal license text. | No legal interpretation or license-compliance conclusion. |
| `README.md` | Included: intended use, installation and client setup, write/search/maintenance workflows and ChatGPT instructions. | Read completely; declared examples and comparisons are not measured outcomes. |
| `assets/` | Excluded: `demo-search.tape`, `demo.tape`, `demo.gif`, `logo.png`, presentation material. | No demo-derived latency, retrieval-quality or operational claims. These are not required state producers or consumers. |
| `examples/` | Included: `claude-code-setup.md`, shipped caller setup and suggested search/read/write/context usage. | Read; external Claude behavior is a setup expectation, not observed execution. |
| `skills/` | Included: `engraph/SKILL.md`, `references/mcp-setup.md`, `references/http-rest-api.md`, agent invocation and retrieval instructions. | All three read. Skill installation and actual agent compliance unobserved. |
| `src/` | Included: `main.rs`, `lib.rs`, `serve.rs`, `http.rs`, `openapi.rs` entry points and adapters; `onboarding.rs`, `config.rs`, `profile.rs`, `identity.rs` setup and identity; `writer.rs`, `migrate.rs`, `watcher.rs`, `indexer.rs` production and maintenance; `store.rs`, `vecstore.rs`, `fts.rs`, `docid.rs` persistence/access; `chunker.rs`, `markdown.rs`, `tags.rs`, `links.rs`, `placement.rs`, `graph.rs`, `temporal.rs`, `llm.rs`, `fusion.rs`, `search.rs`, `context.rs`, `health.rs`, `obsidian.rs` transformations, retrieval, context and integrations. | Entry-point/state-loop ranges read in main, serve, HTTP, writer, indexer, watcher, search, context, identity and migration; module exports and selected inference/storage/placement declarations searched. Onboarding callers searched. Other supporting internals remain for later analysis; no material shipped path is deliberately excluded. |
| `tests/` | Included: `integration.rs`, `write_pipeline.rs`, Markdown fixtures under `fixtures/` including `.obsidian/config.md` and `subfolder/note4.md`. | Integration setup and test names inspected; write-pipeline file read completely. These define checks, not observed results. Fixture contents not yet inspected. |

All table classifications concern SRC-1 at the reviewed commit; paths in the table are commit-relative. The source register below supplies pinned navigation.

External dependencies include the vault and its user-supplied contents, local model files and their download hosts, llama.cpp bindings, SQLite/sqlite-vec, filesystem notification support, MCP clients and HTTP clients; optional Obsidian CLI delegation and ChatGPT tunnel/client setup are interface dependencies, not additional frozen implementations (SRC-1, `Cargo.toml`, `README.md`, `src/serve.rs`). Their vendored/runtime internals, actual user vaults, model weights, external agent conversation loops, and tunnel operations are outside this evidence set. This prevents conclusions about downstream answer quality, agent obedience, model accuracy, host scheduling or external service reliability. The repository's own integration code and suggested prompts remain inside the boundary.

The frozen revision is **f9a95bc96accc792c02ee384d9e6bf768a88c8c8**; applicability ends at **2026-10-14**. HEAD was checked against the acquired revision and the checkout was inspected read-only. No second repository, live webpage, model artifact or execution trace was added. The overall tier is **code-grounded**: implementation can support source-level behavior, while documentation supports attributed intent. No target, tests or examples were executed. In particular, ignored integration tests and CI declarations do not establish a passing current build or retrieval effectiveness (SRC-1, `tests/integration.rs`, `tests/write_pipeline.rs`, `.github/workflows/ci.yml`). This is an execution-evidence limit, not a source-access gap.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/devwhodevs/engraph` | f9a95bc96accc792c02ee384d9e6bf768a88c8c8 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/engraph-0cd4f00695b0/related-systems/devwhodevs--engraph`. Implementation: tracked tree; `Cargo.toml`, `src/lib.rs`; targeted state-loop ranges in `src/main.rs`, `src/serve.rs`, `src/http.rs`, `src/writer.rs`, `src/indexer.rs`, `src/watcher.rs`, `src/search.rs`, `src/context.rs`, `src/identity.rs`, `src/migrate.rs`; declaration searches in `src/onboarding.rs`, `src/llm.rs`, `src/store.rs`, `src/placement.rs`; `tests/write_pipeline.rs` and integration-test setup/names. Doctrine/design: complete `README.md`, `CLAUDE.md`, `examples/claude-code-setup.md`, `skills/engraph/SKILL.md`, both skill reference files, `.claude-plugin/marketplace.json`; CI declaration in `.github/workflows/ci.yml`. | Implementation: [CLI](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/main.rs), [server lifecycle](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/serve.rs), [writer](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/writer.rs), [indexer](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/indexer.rs), [search](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/src/search.rs). Doctrine/design: [README and client prompts](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/README.md), [agent skill](https://github.com/devwhodevs/engraph/blob/f9a95bc96accc792c02ee384d9e6bf768a88c8c8/skills/engraph/SKILL.md). | No source-access gap identified within this repository. Uninspected supporting files are available, not missing. Implementation establishes source behavior only; doctrine/design establishes declared contracts only. No observed-run or causal-experiment layer: no passing-build, deployment, latency, correctness or downstream agent-benefit conclusion. External clients, model weights and user-vault runs were not captured. |
