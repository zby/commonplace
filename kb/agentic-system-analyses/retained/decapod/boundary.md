---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Decapod's repository-native agent governance layer at commit 067b8f55071e13dd103779998168b4c9ffd31a79, including its CLI, retained state, context, shipped agent contracts and proof machinery."
run-id: AAS-2026-10-14-decapod-c44705119841-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "067b8f55071e13dd103779998168b4c9ffd31a79"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/DecapodLabs/decapod
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/decapod-c44705119841/related-systems/DecapodLabs--decapod
  revision: "067b8f55071e13dd103779998168b4c9ffd31a79"
  sha256: null
---

# Decapod boundary

## Boundary and evidence

This run examines how Decapod supplies context, preserves agent work, coordinates custody and gates accepted delivery. The target is the complete shipped repository-native governance layer, not an autonomous coding-agent harness or just its knowledge API. It qualifies as an **extension or tool mechanism** serving model-dependent agent work. Its shipped agent contracts require agents to consult context, record work and respond to governance feedback. An optional decision-provider implementation also submits repository state to Jev. These facts establish scope, not host compliance or model quality (SRC-1, `AGENTS.md`, `src/decapod/core/decision_provider.rs`).

> Decapod is a Rust CLI that agents use throughout development. It reads the
> project's configuration and recorded work, checks the relevant requirements, and
> returns context or a next step. The agent writes the code and operates the
> project's tools, including configuring builds and CI when needed.
> --- `README.md`

The boundary is **whole-system**: it includes the CLI and structured RPC, embedded constitution and agent documentation, generated host entrypoints, project overrides and living specifications, governance documents, database-backed knowledge and decisions, task/session/workspace custody, context retrieval and capsules, validation and publication, optional service adapters, and shipped build/release/CI drivers and evaluators. Same-repository callers and drivers remain inside the boundary. The table below covers every top-level tracked entry; inclusion is functional scope, not a claim that every file has been inspected.

Initial implementation tracing establishes more than a library surface. `src/main.rs` invokes `decapod::run`; `Cargo.toml` declares that executable, the library and feature-gated utility binaries. `src/decapod/lib.rs` parses commands, dispatches knowledge add/search/promotion to the database plugin, exposes RPC context resolution and recommends persistence and subsequent queries. `src/decapod/plugins/knowledge.rs` admits provenance-labelled entries, searches retained active rows, and implements expiry-based maintenance; this initial read does not establish an automatically scheduled decay caller. `src/decapod/core/governance_document.rs` reloads and writes governed sections. `src/decapod/core/project_specs.rs` reads project configuration and authored specs for later context, consumed by the RPC handler. Publication checkpoint verification calls governance/workspace checks. Thus state production, admission, maintenance, reload and consumption are all included, not cut at the API boundary (SRC-1, the paths named here).

> fn main() {
>     if let Err(error) = decapod::run() {
>         eprintln!("{error}");
>         std::process::exit(1);
>     }
> }
> --- `src/main.rs`

> op: "store.query".to_string(),
> reason: "Retrieve prior decisions and knowledge relevant to current task"
>     .to_string(),
> required_params: vec!["kind".to_string()],
> --- `src/decapod/lib.rs`

The shipped prompts are evidence about intended host behavior, not instructions to this analyst. `AGENTS.md`, `CLAUDE.md`, `CODEX.md` and `GEMINI.md` prescribe orientation, pre-inference context, durable trajectory records and living-spec maintenance. The build script ingests `assets/constitution.json` and `docs/agent/` into embedded content, while the constitution CLI returns embedded nodes or scoped fragments. Activation-conformance fixtures specify how to evaluate whether external hosts actually follow those entrypoints. Test source is not an observed host run (SRC-1, `assets/build/compress_constitution.rs`, `src/decapod/core/constitution_cli.rs`, `tests/fixtures/activation_conformance/README.md`).

> A host must receive only the task intent below and operate in a clean checkout. The repository's generated entrypoint is the activation contract; the host must not be given a hand-translated Decapod command sequence.
> --- `tests/fixtures/activation_conformance/README.md`

### Repository coverage

The tracked tree was enumerated at the frozen commit. “Initial read” identifies bounded inspection; “not yet inspected” means available evidence reserved for later source tracing, not an access gap. All directory descendants remain included unless explicitly excluded below.

| Top-level tracked entry | Classification and material paths | Initial inspection and limits |
| --- | --- | --- |
| `src/` | Included: `src/main.rs`; `src/decapod/lib.rs` and `cli.rs`; `core/` state, context, providers, proof, validation and workspace modules; `plugins/` knowledge, internalization, context, orchestration and maintenance; `constitution/`, hooks, plan governance and subsystem definitions | Entry, command/RPC dispatch, knowledge admission/search/decay, governance read/write, specs reload, constitution access, Jev request and checkpoint verification read. Remaining modules are available, not yet inspected in depth; no exhaustive enforcement claim follows from this boundary. |
| `assets/` | Included: `constitution.json`, `schemas/`, `templates/`, `build/`, `tools/` including source-CI, release proof, custody and docs-sync drivers; `benches/`, workspace Dockerfile and tool placeholder | Build embedding and build-lifecycle driver excerpts read; other executable drivers, schema contents and constitution nodes not yet inspected in depth. They are not excluded as unrelated utilities. |
| `docs/` | Included: `agent/` embedded orientation and API contracts; `architecture/` governed execution and interface contracts; `book/` concepts, configuration, workflows and references; storage permissions | Governed-execution architecture and agent MCP contract read. Other documentation available, not yet inspected in depth. |
| `.decapod/` | Included: repository's own `config.toml`, `OVERRIDE.md`, `governance.json`, contracts, managed specs/manifest and managed Dockerfile | README read; concrete self-governance state/specs available, not yet inspected in depth. Repository-local records alone cannot establish external deployment outcomes. |
| `.github/` | Included: workflows for CI, validation, constitution/docs sync, releases and security; actions/scripts for context, source-CI profiles, checkout, release proof and distribution; contribution templates and funding metadata | CI entry and source-profile handoff excerpt read. Remaining graph/actions/scripts not yet traced; no claim of CI success. |
| `tests/` | Included: integration/unit suites, core/plugin tests, activation fixtures, golden RPC/state vectors, cloud/live service tests, context/knowledge promotion, custody, validation/publication, build/release policy and supporting fixtures | Prompt-evaluation integration tests and activation-fixture contract read; remaining suites/fixtures available, not yet inspected in depth. No tests executed and no passing results inferred. |
| `AGENTS.md` | Included: universal agent contract | Complete initial read; doctrine/design, not proof of compliance. |
| `CLAUDE.md` | Included: shipped Claude host entrypoint | Complete initial read; no external host execution supplied. |
| `CODEX.md` | Included: shipped Codex host entrypoint | Complete initial read; no external host execution supplied. |
| `GEMINI.md` | Included: shipped Gemini host entrypoint | Complete initial read; no external host execution supplied. |
| `README.md` | Included: product purpose, operating responsibilities and boundary | Complete initial read. |
| `Cargo.toml` | Included: package, executable/library/utility entrypoints, dependencies and features | Complete initial read. |
| `Cargo.lock` | Included: dependency pins | Available, not yet inspected; dependency internals require evidence not supplied by this lockfile. |
| `.cargo/` | Included: `config.toml` command/build configuration | Available, not yet inspected. |
| `.config/` | Included: `build/` Bazel/Cargo inputs, policy tools and toolchain configuration; Clippy, deny and nextest policy | Available, not yet inspected; required for later build/proof tracing where consequential. |
| `BUILD.bazel` | Included: build/test graph | Available, not yet inspected. |
| `MODULE.bazel`, `MODULE.bazel.lock` | Included: Bazel dependencies and pins | Available, not yet inspected. |
| `.bazelrc`, `.bazelversion` | Included: Bazel invocation/version configuration | Available, not yet inspected. |
| `rust-toolchain.toml` | Included: Rust toolchain selection | Available, not yet inspected. |
| `flake.nix`, `flake.lock` | Included: Nix packaging/environment and dependency pins | Available, not yet inspected. |
| `dist-workspace.toml`, `dist.toml` | Included: release/distribution configuration | Available, not yet inspected. |
| `CHANGELOG.md` | Included: attributed release history | Available, not yet inspected; historical prose would not prove current execution. |
| `CONTRIBUTING.md`, `SECURITY.md` | Included: maintenance and security contracts | Available, not yet inspected. |
| `LICENSE`, `.gitignore` | Included: licensing and tracked/runtime-file boundary metadata | Available, not yet inspected. |

### External responsibilities and evidence limits

External model providers and coding harnesses supply reasoning, chat context, tool execution and host activation. They are deliberately excluded as implementations: this prevents conclusions about their internal loops, universal compliance with Decapod prompts or commands outside the governed surface. The Decapod-facing prompts and adapter code are included. The source itself warns about this boundary (SRC-1, `README.md`, `docs/architecture/governed-execution.md`).

> Validation covers the configured requirements; Decapod cannot govern commands an agent runs
> outside its workflow.
> --- `README.md`

Git and repository/filesystem behavior, Rust dependencies including dactyl-db, SQLite and configured cloud storage, container engines, GitHub/Buildkite execution and optional Jev are external dependencies, not additional frozen sources. Their Decapod interfaces and shipped drivers are included. Unacquired dependency/service implementations prevent independent claims about backend internals, remote availability or end-to-end service correctness (SRC-1, `Cargo.toml`, `src/decapod/core/decision_provider.rs`, `.github/workflows/ci.yml`). The MCP-named documentation describes an integration limit, not evidence of a shipped MCP host:

> Decapod currently provides a Decapod-specific structured RPC interface over process stdin/stdout. It does not currently implement an MCP server, MCP lifecycle, MCP resource discovery, or MCP tool discovery.
> --- `docs/agent/mcp.md`

No target execution, live-service inspection, host transcript or causal experiment was supplied or performed. This prevents observed-success, reliability-rate and causal-improvement claims. No material source path needed for classification was inaccessible. Uninspected available paths are explicitly separated from those external evidence limits.

The frozen evidence is the acquired Git checkout at `067b8f55071e13dd103779998168b4c9ffd31a79`; HEAD was checked against that pin. The applicability cutoff is the opening's run date, **2026-10-14**, not a claim that all documentation was independently current on that date. Later revisions, live issue content, external research links and service responses are outside the evidence boundary. Overall evidence is **code-grounded**, with source-native declarations retained separately as doctrine/design.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/DecapodLabs/decapod` | 067b8f55071e13dd103779998168b4c9ffd31a79 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/decapod-c44705119841/related-systems/DecapodLabs--decapod`. Implementation: `Cargo.toml`, `src/main.rs`, bounded `src/decapod/lib.rs` entry/knowledge/context/checkpoint paths, `src/decapod/plugins/knowledge.rs` admission/search/decay, `src/decapod/core/governance_document.rs` section I/O, `src/decapod/core/project_specs.rs` later context, `src/decapod/core/decision_provider.rs` Jev observation, `src/decapod/core/constitution_cli.rs`, `assets/build/compress_constitution.rs`, `assets/tools/build_lifecycle.rs`, `.github/workflows/ci.yml` entry and `tests/agent_eval.rs`. Doctrine/design: complete `README.md`, `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, `GEMINI.md`, `.decapod/README.md`, `docs/architecture/governed-execution.md`, `docs/agent/mcp.md`, `tests/fixtures/activation_conformance/README.md`. Tracked tree enumerated. | Implementation: [CLI entry](https://github.com/DecapodLabs/decapod/blob/067b8f55071e13dd103779998168b4c9ffd31a79/src/main.rs), [shipped caller and RPC](https://github.com/DecapodLabs/decapod/blob/067b8f55071e13dd103779998168b4c9ffd31a79/src/decapod/lib.rs), [knowledge](https://github.com/DecapodLabs/decapod/blob/067b8f55071e13dd103779998168b4c9ffd31a79/src/decapod/plugins/knowledge.rs). Doctrine/design: [agent contract](https://github.com/DecapodLabs/decapod/blob/067b8f55071e13dd103779998168b4c9ffd31a79/AGENTS.md), [responsibilities](https://github.com/DecapodLabs/decapod/blob/067b8f55071e13dd103779998168b4c9ffd31a79/docs/architecture/governed-execution.md). Other local anchors above resolve at this same commit. | No inaccessible material checkout path identified. Implementation layer is static inspection only; test source is not an observed run. Doctrine/design does not establish enforcement or host compliance. External dependencies and hosts are not acquired; remote correctness, actual activation, end-to-end success and causal benefit remain unestablished. Available paths not yet inspected are listed in coverage, not treated as access gaps. |
