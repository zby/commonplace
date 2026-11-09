---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "IWE's repository-shipped knowledge and agent-memory system at commit 930c184b7cc8508d207e6ca7999ca6e415bc02ac."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/iwe-org/iwe
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/iwe-8e5f495c47e6/related-systems/iwe-org--iwe
  revision: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
  sha256: null
---

# IWE boundary

## Boundary and evidence

This run analyses IWE as the knowledge and agent-memory system shipped in the registered repository, not as an enclosing agent runtime. Its intended use is a shared local document store that people and external agents can read, edit, organize and reuse across conversations. The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system** for the repository-shipped system: the CLI, MCP server, language server, shared graph and filesystem layers, initialization, agent instructions, memory-policy templates, transcript bookkeeping and later context delivery are included together. These are not reduced to the graph library API. SRC-1, `README.md`, `Cargo.toml`, `crates/iwe/src/main.rs`, `crates/iwec/src/main.rs`, `crates/iwes/src/main.rs`.

The target qualifies through the context and memory services it supplies to model-driven agents; ordinary document commands do not themselves need model calls. The project's own declaration separates these responsibilities:

> **Bring your own AI.** Neither the IWE CLI nor the iWe Mac app includes an AI model. Both work on their own as tools for your notes. When you want AI help, use your existing Claude/Codex agent — in terminal or directly in the Mac app.
> --- `README.md`

The source pin is commit **930c184b7cc8508d207e6ca7999ca6e415bc02ac**, verified against the acquired checkout's HEAD. The applicability cutoff is **2026-11-08**. All source evidence must come from this revision; the checkout is an access root, not a separately mutable evidence identity. The overall tier is **code-grounded**, supplemented by source-native doctrine/design. No target command, test, example or model was executed. Test definitions and benchmark harnesses are implementation evidence, not observed successful runs or causal experiments.

### Functional loop included

- **Produce and persist:** `iwe` dispatches initialization, create/update/delete, link-aware restructuring, queries and retrieval. Its command implementations load the workspace graph, prepare document changes and write to disk. `diwe` supplies filesystem loading and mutation; `liwe` supplies graph, parser, query and transformation machinery. The shipped CLI is an included state-owning caller, not an external application. SRC-1, `crates/iwe/src/main.rs`, `crates/diwe/src/fs.rs`, `crates/diwe/src/loader.rs`, `crates/liwe/src/lib.rs`, `crates/liwe/src/query/execute.rs`.
- **Admit agent memory:** Claude integration helpers enable a `MEMORY` policy document, read transcript spans, stage candidates, expose an inbox and record selections, writes and rejections. The distill prompt supplies the model-facing selection and writing procedure; these instructions are included evidence, not executable guarantees of user approval. CLI schema gating and MCP create's pre-persistence schema check are distinct code paths that later analysis can assess. SRC-1, `crates/iwe/src/internal/claude/enable.rs`, `crates/iwe/src/internal/claude/session.rs`, `crates/iwe/src/internal/claude/record.rs`, `crates/iwe/templates/claude/prompts/distill.md`, `crates/iwec/src/lib.rs`.
- **Maintain:** the reflect prompt governs policy changes, taxonomy, curation and forgetting; ordinary CLI and MCP mutation paths also remain included. Post-tool reporting inspects selected host-tool writes and reports schema or similarity issues. The prompt's claim to be the memory write procedure must not be generalized into exclusive filesystem access or a universal enforced admission gate. SRC-1, `crates/iwe/templates/claude/prompts/reflect.md`, `crates/iwe/src/internal/claude/hook/post_tool.rs`, `crates/iwe/src/main.rs`, `crates/iwec/src/lib.rs`.
- **Reload and consume later:** the session-start helper opens the configured store, selects injection slices and renders a memory index. CLI retrieval, MCP tools/resources/prompts and LSP navigation are other included consumers. MCP startup loads the workspace and starts watching it; persistence applies filesystem changes and updates its graph. The LSP loads state and reconciles external files with open editor buffers. These shipped consumers prevent treating retained content as write-only. SRC-1, `crates/iwe/src/internal/claude/hook/store.rs`, `crates/iwe/src/internal/claude/hook/index.rs`, `crates/iwec/src/main.rs`, `crates/iwec/src/lib.rs`, `crates/iwes/src/lib.rs`, `crates/iwes/src/router/server.rs`.

The model-facing capture procedure explicitly describes an intermediate store rather than immediate admission:

> Unattended (`claude -p`, a routine, a subagent — anywhere nobody can answer): read and stage, write nothing into the store, and say what is waiting in the inbox. An item named in the instruction is still written.
> --- `crates/iwe/templates/claude/prompts/distill.md`

Maintenance is likewise shipped as agent-facing instructions, not merely an inferred use of document APIs:

> The interactive layer of memory maintenance, and the only one: policy and taxonomy evolution, curation as far as the policy's curation section allows, and the forget verbs on demand — all with the user. Every command is a plain `iwe` command run from the repository root. No `MEMORY.md` document means nothing to govern: say so and point at `/iwe:init`. Never commit: every change, deletions included, is a file the user reviews.
> --- `crates/iwe/templates/claude/prompts/reflect.md`

### Tracked-root coverage

“Included” fixes functional and evidence scope, not a claim that every file has already been read. Initial inspection traced the material entry points and state loop above. Remaining available files are marked as such rather than described as inaccessible.

| Top-level tracked file or directory | Classification | Material paths and role; initial inspection and limits |
| --- | --- | --- |
| `crates/` | Included | All five workspace crates. `iwe/src/main.rs`, `iwe/src/init/agents.rs`, `iwe/src/internal/claude/{enable,session,record}.rs`, `iwe/src/internal/claude/hook/{store,index,post_tool}.rs`, and `iwe/templates/claude/prompts/{distill,reflect}.md` establish the CLI and memory loop. `iwec/src/{main,lib}.rs` establish MCP startup, prompts, admission and persistence. `iwes/src/{main,lib}.rs` and `iwes/src/router/server.rs` establish the editor consumer and reload responsibility. `diwe/src/{fs,loader}.rs`, `liwe/src/lib.rs` and `liwe/src/query/execute.rs` establish shared storage and query boundaries. These files were inspected fully or in responsibility-specific ranges. Remaining graph, schema, search, retrieval, watcher, rendering, init, template and help implementations remain included and available for detailed analysis, not yet exhaustively inspected. Test suites in each crate and `iwe/benches/` are included evaluators; initial samples were `iwe/tests/internal_test.rs` and `iwe/benches/load.rs`. No test result or benchmark measurement is established. |
| `docs/` | Included | Architecture, data model, query/schema, CLI workflows, MCP, editor integration, search ranking, benchmark and design documents; `docs/architecture.md` initially inspected and the tracked tree inventoried. Other documents, book sources, PDF and figures are available but not yet inspected. Their presence supplies no validated performance or agent-quality result. |
| `npm/` | Included | `iwe/bin/` launchers, `iwe/lib/run.js`, platform package manifests, `mcp/bin/iwe-mcp.js`, package documentation and `stamp.js` distribute and launch the same binaries. Initial inspection followed `iwe/lib/run.js` and `mcp/bin/iwe-mcp.js`; other package files remain available. No installed package or platform compatibility was tested. |
| `README.md` | Included | Initially read completely: declared shared-note purpose, external-agent relationship, supported entry points and separately linked products. |
| `README.ko.md`, `README.zh-CN.md` | Included | Translated project documentation; inventoried, not yet inspected. No independent implementation or translation-parity conclusion. |
| `Cargo.toml` | Included | Initially read: workspace membership and dependencies, including external parsing, validation, protocol and ranking crates. |
| `Cargo.lock` | Included | Frozen dependency resolution; inventoried, not yet inspected. Dependency internals are not automatically part of this repository's evidence. |
| `server.json`, `glama.json` | Included | Initially read: MCP registry/package metadata and maintainer listing, not a hosted model runtime. |
| `.github/` | Excluded from runtime analysis | `workflows/{rust,release,release-plz}.yml` and `dependabot.yaml` concern CI, release and dependency automation. Inventoried, not inspected; exclusion prevents claims about successful CI, supply-chain controls or released-binary provenance. |
| `.githooks/` | Excluded from runtime analysis | `pre-commit` is development automation; inventoried, not inspected. No conclusion about developer-side enforced checks. |
| `.gitattributes`, `.gitignore`, `.release-plz.toml` | Excluded from runtime analysis | Repository/release configuration; inventoried, not inspected. No conclusion about checkout filters, ignored development artifacts or release policy. Runtime workspace filtering remains included through `diwe`. |
| `CONTRIBUTING.md` | Excluded from runtime analysis | Contributor procedure; inventoried, not inspected. No conclusion about contribution governance or maintainer practice. |
| `LICENSE-APACHE` | Excluded from functional analysis | Licensing text; inventoried, not inspected. No legal or licensing-compliance assessment. |

### External dependencies and limits

External agent hosts supply model calls, tool scheduling, permissions, conversation state and actual compliance with the shipped prompts. The source includes Claude helper commands and embedded prompt bodies, but the README's `iwe-org/skills` marketplace/plugin is a separate repository and is not frozen here. Its installation and hook wiring cannot be verified by treating the embedded helper implementation as proof that a deployed host invokes it. Likewise, the separately advertised Mac app, editor clients/plugins, ready-made workspaces, live website, package registries and linked demonstrations are outside the registered source. Their absence prevents claims about their implementation, end-to-end integration, deployment reliability or actual memory benefits. It does not exclude the CLI, MCP or LSP drivers shipped here. SRC-1, `README.md`, `crates/iwe/src/main.rs`, `crates/iwe/src/init/agents.rs`, `npm/iwe/lib/run.js`.

Rust and JavaScript runtime dependencies, the filesystem and external protocol clients are environmental dependencies; this source pin does not freeze their implementations or a user's notes, policies and transcripts. No operational transcript, user-selection trace, retrieval-quality evaluation or controlled intervention was supplied. The boundary therefore permits source-grounded conclusions about available mechanisms and source-native procedure, not measured effectiveness, actual user authorization in a run, host-level safety, or causal improvement in agent behavior. Available but uninspected files remain discoverable under SRC-1 at this same commit; they are not access gaps or new source identities.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/iwe-org/iwe` | 930c184b7cc8508d207e6ca7999ca6e415bc02ac | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/iwe-8e5f495c47e6/related-systems/iwe-org--iwe`. Tracked tree inventoried. Implementation: workspace manifest; CLI command dispatch and implementations; agent initialization; Claude enable, session, record, store, index and post-tool helpers in selected ranges; MCP entry point, create, prompts and persistence; LSP entry points and reload/update handlers; shared filesystem loading and query dispatch; npm binary launcher. Evaluators: initial portions of CLI internal tests and load benchmark harness. Doctrine/design: complete root README and embedded distill/reflect prompts, plus architecture landing. The coverage table distinguishes initial reads from remaining available material. | [Project declaration](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/README.md); [CLI](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/crates/iwe/src/main.rs); [capture procedure](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/crates/iwe/templates/claude/prompts/distill.md); [maintenance procedure](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/crates/iwe/templates/claude/prompts/reflect.md); [later injection](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/crates/iwe/src/internal/claude/hook/index.rs); [MCP implementation](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/crates/iwec/src/lib.rs); [LSP implementation](https://github.com/iwe-org/iwe/blob/930c184b7cc8508d207e6ca7999ca6e415bc02ac/crates/iwes/src/router/server.rs). | No established access gap inside the frozen checkout. External plugin, app and hosts are not registered evidence; their invocation and end-to-end behavior cannot be established. No supplied observed run or causal experiment; test/benchmark source does not establish outcomes. |
