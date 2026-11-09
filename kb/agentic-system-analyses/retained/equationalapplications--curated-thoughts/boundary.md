---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Curated Thoughts desktop, headless and agent-facing memory system at commit 433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd."
run-id: AAS-2026-11-08-curated-thoughts-00ab3a770403-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/equationalapplications/curated-thoughts
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/curated-thoughts-1b731af19e7c/related-systems/equationalapplications--curated-thoughts
  revision: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
  sha256: null
---

# Curated Thoughts boundary

## Boundary and evidence

This run covers the Curated Thoughts repository's shipped memory system, not merely its retrieval API. Its intended use is to turn vault files and agent deposits into retained knowledge that people review and agents later recall. The target class is **memory/knowledge/context-engineering system**. Its model-dependent librarian, embedding queries and agent-facing context tools make it in scope. The boundary kind is **whole-system**: the desktop caller, headless operators, both MCP servers, maintenance, persistence and retrieval belong to the target. They are not excluded hosts simply because they call shared libraries. SRC-1, `INTENT.md`, `src-tauri/src/main.rs`, `src-tauri/src/pipeline/mod.rs`, `tools/src/bin/ct.rs` and `src-tauri/src/tool_dispatch.rs` establish these responsibilities.

The target's own statement of purpose is:

> You put raw material in as ordinary files. A component called the **Active
> Librarian** reads those files and turns them into short, trustworthy facts
> (the "wisdom layer"). Any agent, even a weak one, can then recall those
> facts. The goal is that good structure does the work, so agents don't need
> to be clever.
> --- `INTENT.md`

Initial tracing follows the desktop binary's GUI/MCP dispatch, GUI startup opening the configured database and starting its pipeline, successful ingest calling the librarian, synthesis calling a model and validating proposal JSON, and proposal review calling the shared commit layer. It also follows `ct` dispatch through its shared read/write modules and the separate read-only MCP server's recall implementation. These paths cover production, admission, persistence and later consumption of memory; inclusion does not assert that all paths have identical policies. SRC-1, `src-tauri/src/main.rs`, `src-tauri/src/lib.rs`, `src-tauri/src/pipeline/mod.rs`, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/proposals_api.rs`, `tools/src/bin/ct.rs`, `tools/src/cmds.rs`, `tools/src/queries.rs`, `tools/src/cli_common.rs`, `tools/src/bin/curated_thoughts_mcp.rs`.

One executable connection from ingest to model-dependent maintenance is:

> if let Err(e) = crate::librarian::generate_summary(
>                                     &mut conn,
>                                     &path,
>                                     crate::librarian::active_generation_model(
>                                         crate::setup::recommended_model(),
>                                     )
>                                     .as_str(),
>                                     false,
>                                 ) {
> --- `src-tauri/src/pipeline/mod.rs`

The scope includes shipped generation prompts, integration instructions and maintenance scheduling, not only Rust storage code. The frontend supplies model and embedding callbacks to its external wiki engine; startup also installs deletion-triggered healing and periodic pruning. The shipped skill instructs agents to recall before coding and deposit after non-trivial work. These are source-native instructions, not evidence that an external agent followed them. SRC-1, `src/lib/wiki.ts`, `src/App.tsx`, `.skills/curated-thoughts/skill.md`.

> const cleanupHeal = startAutoHeal();
>     const cleanupMaintenance = startAutoMaintenance();
> --- `src/App.tsx`

The frozen evidence is SRC-1 at full commit `433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd`, applicable through the run cutoff **2026-11-08**. The acquired source object is preserved unchanged. The checkout's HEAD matches that pin and its status was clean when inspected. The overall tier is **code-grounded**, with documentation used for declared intent and evaluator documentation. No target program, test, example, model endpoint or service was executed. This boundary establishes an inspectable operational scope, not successful deployment, benchmark reproduction or measured downstream benefit.

### Functional coverage

The tracked tree was enumerated at the reviewed commit. Every top-level tracked file or directory is classified below. Included means inside the functional evidence boundary, not exhaustively read. Initial inspection reached the material entry points and loop connections described above; deeper implementation and evaluation inspection remains for the analysts. Unread available files are not access gaps.

| Top-level tracked paths | Classification and material paths | Initial inspection and limits |
| --- | --- | --- |
| `src-tauri/` | Included: `src/main.rs` and `src/lib.rs` launch and configure the desktop/MCP surfaces; `src/pipeline/`, `src/watcher/`, `src/chunker/`, `src/indexer/`, `src/embedder/` and `src/librarian/` ingest and synthesize; `src/db/`, `src/okf/`, `src/outbox/`, `src/reconcile.rs` and `src/embed_sweep.rs` retain and maintain state; `src/proposals_api.rs`, `src/queue_api.rs`, `src/entities_api.rs`, `src/drafts_api.rs` and `src/okf_api.rs` expose human/state operations; `src/mcp_server.rs`, `src/tool_dispatch.rs`, `src/retrieval/`, `src/wisdom_deposit.rs`, `src/wisdom_match.rs`, `src/two_stage.rs`, `src/prompt_drop.rs` and `src/cloud_bridge/` serve agents and recall; `tests/` and `fixtures/` supply evaluators and fixture state. | Read main dispatch, startup and heal/prune ranges in `lib.rs`, pipeline worker, librarian context assembly and synthesis prompt/model/validation/write ranges, proposal resolution API, MCP startup and tool routing/recall, deposit interface and cloud bridge configuration. Read test README and a wisdom-gate benchmark range. Other modules remain available for deeper tracing; assets, packaging and build configuration are included as supporting material, without a platform or security certification. |
| `src/` | Included: `main.tsx`, `App.tsx`, `components/shell/`, `components/modes/`, `components/review/`, `components/queue/`, `components/settings/`, `components/setup/`, `hooks/` and `lib/` are shipped callers, review/confirmation interfaces, settings, retrieval and maintenance; `__tests__/` and component/a11y tests are evaluators. | Read `App.tsx`, wiki provider callbacks and maintenance ranges in `lib/wiki.ts`, `hooks/useMemoryRead.ts` and the ReviewMode interface/state range. The rest is included but not yet inspected at member-authoring depth. No UI execution or accessibility conformance conclusion. |
| `tools/` | Included: `src/bin/ct.rs`, `src/cmds.rs`, `src/queries.rs`, `src/write.rs`, `src/watcher.rs`, `src/reindex.rs`, `src/drift.rs`, `src/paths.rs` and `src/cli_common.rs` are headless callers and maintainers; `src/bin/curated_thoughts_mcp.rs` is the distinct read-only server; other `src/bin/` programs ingest, run the librarian, reindex, reanchor, backfill, export, generate fixtures, calibrate and profile; `tests/` checks these surfaces. | Read manifest, dispatch and librarian-command ranges, shared-module re-exports, librarian database/dirty-document loop, terminal review gate, wisdom-match query setup and read-only MCP recall. Helper implementations and remaining tests are available, not execution evidence. |
| `.skills/` | Included: `.skills/curated-thoughts/skill.md` is the shipped agent recall/deposit procedure. | Read completely; instructions may lag implementation and must not substitute for code. |
| `docs/` | Included: `design/`, `superpowers/specs/`, plans/references/rulings and `mcp-write-tools-okf-frontmatter.md` document design and maintenance; `benchmarks/` holds evaluator reports and artifacts; `a11y/` supports the UI. | Read benchmark index; other documents are available but not yet inspected. Plans and status claims are doctrine/reported operation unless independently grounded; this boundary claims no benchmark result or completed plan. |
| `calibration-run/` | Included: the two `grid-20261018-*` directories hold wisdom-gate/activity probe sets, recorded cells, sweeps, picks and proposed configuration patches. | Enumerated; contents not yet inspected. Evaluator source refers to these artifacts. Their inclusion permits later bounded inspection but establishes no calibration outcome here. |
| `scripts/` | Included supporting build/install, release configuration, sidecar verification/smoke and calibration drivers, especially `calibrate-two-stage.sh`, `runtime-smoke-clw.mjs`, `build-local-bundle.sh` and `install-ct.sh`. | Enumerated; not yet inspected. No installation, release-artifact or smoke-test success is claimed. |
| `Cargo.toml`, `Cargo.lock`, `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml` | Included: workspace/package/dependency identity and pinned dependency declarations. | Read workspace and package manifests, including nested Rust manifests. Lockfiles enumerated, not audited; dependency declarations do not supply dependency implementation evidence. |
| `README.md`, `INTENT.md` | Included: product surfaces, operational instructions and source-native intent. | README read completely; INTENT purpose, glossary and first rules inspected. Documentation is not authoritative over executable behavior. |
| `AGENTS.md`, `CHANGELOG.md`, `OIDC_SETUP.md` | Included supporting repository instructions, historical release claims and publication setup. | Enumerated, not yet inspected. No claim of agent compliance, release chronology or working authentication setup. |
| `.github/`, `.releaserc.json` | Included supporting CI, release, review and analysis configuration. | Tree enumerated; configurations not yet inspected. No conclusion that CI ran or release checks passed. |
| `specs/` | Excluded deliberately: `2026-11-05-brand-favicons/spec.md`, branding work. | Tree identified; content not inspected. Exclusion prevents assessing branding-spec implementation, not the memory loop. |
| `public/`, `index.html` | Included supporting desktop web entry and static assets. | Enumerated, not inspected; no rendering or asset correctness claim. |
| `.codegraph/`, `.hermes/`, `.vscode/` | Excluded deliberately: local analysis configuration, target-authored development plans/reviews and editor recommendations. | Tree enumerated only. No conclusions about development-agent behavior, review quality or editor setup. These do not replace shipped integration instructions under `.skills/`. |
| `.gitignore`, `clippy.toml`, `eslint.config.js`, `rust-toolchain.toml`, `tsconfig.json`, `tsconfig.node.json`, `vite.config.ts` | Included supporting build, lint and toolchain configuration. | Enumerated, not inspected. No build/lint reproducibility claim. |
| `CONTRIBUTORS.md`, `LICENSE` | Excluded deliberately: attribution and licensing. | Enumerated, not inspected. No legal or authorship assessment. |

All functional coverage above refers to SRC-1. No material shipped memory responsibility was deliberately excluded. Inspection is sufficient to establish the boundary and initial entry-point connections, not a full behavioral audit of every included file.

### External dependencies and prevented conclusions

The separate **curated-thoughts-integrations** repository is outside the frozen source set. The target explicitly identifies CTI as a separate consumer of `ct wisdom match`; this run includes the command's implementation and shipped local skill, but not CTI session-start, per-turn or mid-task delivery, harness caching, deduplication or installation behavior. It cannot infer those properties from this repository's README. SRC-1, `INTENT.md`, `README.md`, `tools/src/bin/ct.rs`, `tools/src/queries.rs`.

The npm wiki/ontology packages and Rust dependencies are external implementations. Their pinned declarations and this repository's adapters/callbacks are included; their package source is not acquired. That gap prevents independently verifying internal external-engine algorithms or assigning them to Curated Thoughts without qualifying the adapter boundary. Local Ollama/sidecar inference, external OpenAI-compatible generation/embedding endpoints, optional Jev classification, remote cloud bridge services and a PostgreSQL replica are deployment dependencies, not additional frozen sources. The run can inspect the local configuration/call/persistence contracts but cannot establish provider quality, hosted service behavior, end-to-end privacy or remote durability. SRC-1, `package.json`, `src-tauri/Cargo.toml`, `src/lib/wiki.ts`, `src-tauri/src/cloud_bridge/mod.rs`, `README.md`.

No actual user's vault, persistent brain or agent execution trace was supplied. Repository fixtures, benchmark snapshots and calibration artifacts remain available within SRC-1; they must be examined under their stated conditions before supporting empirical claims. Frozen-vector evaluator source explicitly distinguishes code-path regression from model quality:

> //! Frozen-vector regression guard for the `ct wisdom match` floor (issue #265).
> //! Recomputes hit@2 / FP through `wisdom_match_with_floor` from the vectors
> //! the calibration runs froze. Guards the CODE PATH, not the model.
> --- `src-tauri/tests/wisdom_gate_bench.rs`

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/equationalapplications/curated-thoughts` | 433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/curated-thoughts-1b731af19e7c/related-systems/equationalapplications--curated-thoughts`. Implementation: commit tree, manifests, desktop/MCP startup, pipeline worker, librarian context and synthesis ranges, review API, shared tool dispatch and recall, deposit interface, cloud bridge configuration, `ct` dispatch and shared CLI librarian/review/query ranges, read-only MCP recall, frontend caller/provider/maintenance/retrieval/review ranges, and wisdom-gate evaluator source. Doctrine/design: README, INTENT purpose/glossary/initial rules, shipped skill, Rust test README and benchmark index. | Implementation: [desktop entry](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/src-tauri/src/main.rs), [pipeline](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/src-tauri/src/pipeline/mod.rs), [librarian](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/src-tauri/src/librarian/synthesis.rs), [CLI](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/tools/src/bin/ct.rs), [frontend wiki](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/src/lib/wiki.ts), [evaluator](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/src-tauri/tests/wisdom_gate_bench.rs). Doctrine/design: [intent](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/INTENT.md), [skill](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/.skills/curated-thoughts/skill.md), [README](https://github.com/equationalapplications/curated-thoughts/blob/433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd/README.md). | No checkout access failure found. External package implementations, CTI and deployed providers/hosts were not acquired; their internals and end-to-end operation cannot be verified. No target execution or supplied user run evidence; implementation and declared intent do not establish operational success or causal benefit. Unread included files remain available at this pin, not access gaps. |
