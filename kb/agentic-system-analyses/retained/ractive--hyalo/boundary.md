---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Hyalo's Markdown knowledgebase tooling, shipped agent workflows and optional Jev helper at commit 697f215fe8a90a5c760fceb686f2a321c9db7221."
run-id: AAS-2026-10-14-hyalo-ffe11d6a6d56-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "697f215fe8a90a5c760fceb686f2a321c9db7221"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/ractive/hyalo
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/hyalo-ffe11d6a6d56/related-systems/ractive--hyalo
  revision: 697f215fe8a90a5c760fceb686f2a321c9db7221
  sha256: null
---

# Hyalo boundary

## Boundary and evidence

This run examines Hyalo as a Markdown knowledgebase tooling system, including its shipped agent instructions, host integration and optional model-backed classification helper. Its intended use is structured retrieval and maintenance of an existing collection of Markdown files, not autonomous ownership of a general agent loop. The target class is `memory/knowledge/context-engineering system`; the boundary kind is `whole-system`, covering the shipped state-production, maintenance, validation and later-consumption paths rather than just the Rust library API. SRC-1, `README.md`, `crates/hyalo-cli/src/main.rs`, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `npm/jev/src/cli.ts`.

The target declares its relationship to the enclosing agent explicitly:

> Hyalo is the tooling layer that makes this practical. An LLM agent can use `hyalo find` to search across thousands of notes by metadata, full-text, or regex. It can use `hyalo set` to bulk-update frontmatter, `hyalo mv` to reorganize files while reporting any ambiguous or unsupported link rewrites, and `hyalo lint` to enforce schema consistency — without guessing at YAML syntax.
> --- `README.md`

The ordinary CLI remains useful without model calls. Scope qualification rests on the knowledge-system role, shipped model-consumed workflows and the optional Jev path, not an assertion that every query invokes a model. SRC-1, `README.md`, `crates/hyalo-cli/templates/skill-hyalo.md`, `npm/jev/src/provider.ts`.

### Functional coverage

Included responsibilities are Markdown/frontmatter discovery and parsing, metadata and task mutation, document scaffolding, link repair and move rewriting, schema and Markdown linting, profile generators, snapshot and BM25 indexing, query/read/summary consumption, installation of agent guidance, Pi tools and feedback, and Jev suggestion preparation and review. The CLI, its bundled templates, the TypeScript API, Pi package and Codex plugin are parts of this target, not excluded callers merely because they cross an API boundary. SRC-1, `crates/hyalo-cli/src/dispatch.rs`, `crates/hyalo-cli/src/commands/init.rs`, `package.json`, `npm/hyalo/src/api.ts`, `pi-package/extensions/hyalo.ts`, `crates/hyalo-cli/templates/jev/jev.md`.

Initial tracing establishes these connected paths:

- The executable enters `hyalo_cli::run`; prepared dispatch routes reads, searches and task mutations to command handlers. Snapshot creation builds scanned entries and BM25 data and publishes a snapshot; subsequent invocations load the snapshot subject to compatibility checks. Mutation finalization refreshes observed paths and flushes the index, or attempts persistent invalidation on failure. This includes both creation and later reuse of retained state. SRC-1, `crates/hyalo-cli/src/main.rs`, `crates/hyalo-cli/src/dispatch.rs`, `crates/hyalo-cli/src/commands/create_index.rs`, `crates/hyalo-cli/src/run.rs`, `crates/hyalo-cli/src/commands/journal.rs`.
- The shipped tidy instruction directs orientation, recent-signal collection, detection, authorized repair and a final fresh summary. It explicitly distinguishes read-only audits from repair runs. These instructions belong inside the boundary even though the enclosing agent supplies judgment and executes commands. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`.
- Init embeds and installs skill, rule, Pi extension/runtime and Jev assets. The npm API provides process transports, including Pi's `exec` adapter. The Pi extension exposes retrieval and mutation tools, optional session-summary injection and post-write lint feedback. These are shipped consumers of retained content, not a hypothetical application assembled around the core crate. SRC-1, `crates/hyalo-cli/src/commands/init.rs`, `npm/hyalo/src/api.ts`, `pi-package/extensions/hyalo.ts`.
- Jev prepares selected local evidence through read-only Hyalo commands, calls Typesafe through the SDK, validates suggestions and returns them. The shipped review procedure directs the agent to reassess evidence and schemas before using ordinary Hyalo mutations; the helper is not itself the persistence owner. SRC-1, `npm/jev/src/prepare.ts`, `npm/jev/src/provider.ts`, `npm/jev/src/cli.ts`, `crates/hyalo-cli/templates/jev/jev.md`.

> No helper
> command applies changes. Preserve existing values and unrelated metadata. Run
> lint on changed files and recheck links and original findings; report failures.
> --- `crates/hyalo-cli/templates/jev/jev.md`

### Repository coverage

Every top-level tracked entry is classified below. Included means within the analytical boundary, not a claim that every file was already read. Initial inspection traced the material loop above; remaining detailed implementation and evaluator inspection stays available within SRC-1. A tree-only classification is explicitly distinguished from inspected behavior. No material shipped path is known to be unavailable.

| Top-level entry | Coverage | Material paths and role; inspection status or exclusion limit |
|---|---|---|
| `.agents/` | Included | `plugins/marketplace.json`: Codex distribution discovery; tree inspected, manifest detail not yet inspected. |
| `.cargo/` | Included, supporting | `config.toml`: build/task configuration; tree inspected, no runtime behavior inferred. |
| `.claude/` | Included | `skills/hyalo/`, `skills/hyalo-tidy/`, `rules/knowledgebase.md` are repository-local agent surfaces; `CLAUDE.md`, `agents/` and other skills are development/maintenance guidance. Tree inspected; shipped workflow substance initially read through CLI templates, not assumed identical across copies. |
| `.gitattributes` | Included, supporting | Git file treatment; tree inspected only. |
| `.github/` | Included, supporting | `workflows/ci.yml`, `benchmarks.yml`, release and publishing workflows; dependency/release configuration. Tree inspected; no CI success inferred. |
| `.gitignore` | Included, supporting | Repository ignore policy; tree inspected only. |
| `.hyalo.toml` | Included | Repository's own vault/schema configuration; tree inspected, details not yet inspected. |
| `AI_NOTICE` | Included, supporting | Authorship notice; identified through README and tree. |
| `CHANGELOG.md` | Included, supporting | Release declarations, not proof of implementation; tree inspected only. |
| `CLAUDE.md` | Included, supporting | Repository agent entry guidance; tree inspected only, not treated as instructions for this worker. |
| `Cargo.lock` | Included, supporting | Rust dependency pinning; tree inspected only. |
| `Cargo.toml` | Included, supporting | Workspace/build manifest; tree inspected only. |
| `Cross.toml` | Included, supporting | Cross-build configuration; tree inspected only. |
| `LICENSE` | Included, supporting | Licensing; tree inspected only. |
| `README.md` | Included | Intended use, CLI examples, agent integrations and profile contracts; read. |
| `bench-e2e.sh` | Included, evaluator | CLI benchmark driver; tree inspected, not executed or yet read. |
| `crates/` | Included | `hyalo-cli/src/{main,run,dispatch}.rs`, `commands/`, `prepared*`, config and output implement command execution; `templates/` ships workflows, rules, profiles, Pi/Codex/Jev assets; `tests/e2e/` evaluates CLI behavior. `hyalo-core/src/` supplies discovery, parsing, indexing, search, links and rooted filesystem operations; `hyalo-mdlint/src/` supplies validation; `xtask/src/` supplies generation/distribution/drift checks. Selected entry, snapshot, journal, init, workflow and index regression-test paths read; deeper module and evaluator inspection remains. |
| `deny.toml` | Included, supporting | Dependency policy; tree inspected only. |
| `docs/` | Included | `configuration.md`, `ci.md`, `releasing.md`: configuration, validation and distribution contracts. Configuration opening read; others not yet inspected. |
| `fuzz/` | Included, evaluator | Targets for frontmatter splice, link parser, scanner and snapshot loader, with seeds; tree inspected, not run or yet read. |
| `hyalo-knowledgebase/` | Included, attributed design/development evidence | `docs/`, `decision-log.md`, `iterations/`, `backlog/`, `research/`, `dogfood-results/`, `reviews/` describe development, evaluations and the product's self-use corpus. Tree inspected only. Native reports may inform attributed claims later, but their presence establishes neither observed operation nor correctness. |
| `justfile` | Included, supporting | Developer/evaluation command entry points; tree inspected only. |
| `npm/` | Included | `hyalo/src/api.ts`, `pi-runtime.ts`, generated types and launcher/runtime support expose CLI access; `jev/src/{cli,prepare,provider,protocol,decisions,io}.ts` implements the optional model helper; both packages' tests and `platforms/` packaging remain in scope. API transport and Jev entry/preparation/provider read; remaining details not yet inspected. |
| `package.json` | Included | Root Pi package discovery routes to `pi-package/extensions` and `pi-package/skills`; read. |
| `pi-extension-e2e.sh` | Included, evaluator | Static/load/live-model integration driver; opening inspected, not executed. Its configured model is a test condition, not evidence of a completed run. |
| `pi-package/` | Included | `extensions/hyalo.ts`, `lib/hyalo-api.*`, `skills/hyalo/`, `skills/hyalo-tidy/` including Jev reference/bundle; tool registration, summary injection and host-write feedback read in extension; package copies remain available for drift comparison. |
| `plugins/` | Included | `hyalo/.codex-plugin/plugin.json`, six skills and their `agents/openai.yaml`, tidy Jev reference/bundle: distributed Codex workflow surface. Tree inspected; not excluded as an external consumer. |

### Exclusions, dependencies and evidence limits

The enclosing Claude Code, Codex and Pi runtimes, their model scheduling, conversation retention and user authorization mechanisms are external dependencies. Their implementations are not frozen here. This prevents attributing autonomous scheduling, cross-session recall guarantees or enforcement of all skill instructions to Hyalo. In particular, the tidy instruction can inspect Claude auto-memory but tells the agent not to modify it; that memory store is not Hyalo-owned persistence. SRC-1, `crates/hyalo-cli/templates/skill-hyalo-tidy.md`, `pi-package/extensions/hyalo.ts`.

Typesafe's hosted service, the SDK's external implementation, package registries, externally installed binaries, Obsidian and other consumers' vaults are outside the frozen repository. Source can establish the helper's request and response handling, not provider internals, service availability, classification accuracy or behavior of an installed package not represented by this commit. External links in README are declarations, not additional acquired sources. SRC-1, `npm/jev/src/provider.ts`, `README.md`.

The frozen revision is `697f215fe8a90a5c760fceb686f2a321c9db7221`; applicability is cut off at 2026-10-14. HEAD was checked against the acquisition pin and the checkout reported no changes. Overall evidence is code-grounded, supplemented by source-native doctrine/design. No target, example, test or model call was executed. Test source supports the existence and scope of checks, not their passing, and no observed-run or causal-experiment evidence is established at this boundary. SRC-1, `crates/hyalo-cli/tests/e2e/index_journal.rs`, `pi-extension-e2e.sh`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ractive/hyalo` | 697f215fe8a90a5c760fceb686f2a321c9db7221 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/hyalo-ffe11d6a6d56/related-systems/ractive--hyalo`. Complete tracked-path inventory. Implementation: CLI main; prepared dispatch; snapshot load, creation/publication and journal finalization excerpts; init asset selection; npm API transport; Pi tool/summary/feedback registration; Jev CLI, preparation and provider; index-journal test opening and Pi evaluator opening. Doctrine/design: README, full tidy and Jev instructions, main skill opening and configuration opening. | Implementation: [CLI entry](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/crates/hyalo-cli/src/main.rs), [dispatch](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/crates/hyalo-cli/src/dispatch.rs), [journal](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/crates/hyalo-cli/src/commands/journal.rs), [Pi consumer](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/pi-package/extensions/hyalo.ts), [Jev provider](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/npm/jev/src/provider.ts). Doctrine/design: [README](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/README.md), [tidy](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/crates/hyalo-cli/templates/skill-hyalo-tidy.md), [Jev review contract](https://github.com/ractive/hyalo/blob/697f215fe8a90a5c760fceb686f2a321c9db7221/crates/hyalo-cli/templates/jev/jev.md). | No known repository access gap. Available but uninspected files remain within this Git source, not missing evidence. External host/provider implementations and deployed user vaults are not captured; prevents conclusions about their internals or end-to-end operational effectiveness. No run executed here; evaluator source and workflow instructions are not passing-run evidence. |
