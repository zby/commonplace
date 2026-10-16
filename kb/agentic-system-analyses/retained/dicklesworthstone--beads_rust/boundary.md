---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "beads_rust's agent-facing issue memory, CLI, MCP server and shipped workflow instructions at commit 53f7a3d30aca8cab3c3e4abdefeade459e8a3089."
run-id: AAS-2026-10-16-beads-rust-e82d5506d2ff-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 53f7a3d30aca8cab3c3e4abdefeade459e8a3089
analysis-cutoff: "2026-10-16"
evidence-tier: code-grounded
source:
  identity: https://github.com/Dicklesworthstone/beads_rust
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-beads-rust/related-systems/Dicklesworthstone--beads_rust
  revision: 53f7a3d30aca8cab3c3e4abdefeade459e8a3089
  sha256: null
---

# beads_rust boundary

## Boundary and evidence

The target is beads_rust (`br`), used to retain project issues, dependencies, comments and work status for later retrieval by coding agents and humans. Its intended use is dependency-aware project work across sessions, not general autobiographical agent memory. It qualifies as an agent-facing memory/knowledge/context-engineering system: the shipped instructions prescribe a retrieve–claim–work–close cycle, and the optional MCP server serves retained issue state and data-bearing workflow prompts to an external model host. This classification does not attribute model invocation or autonomous task execution to the tracker (SRC-1: `README.md`, `docs/AGENT_INTEGRATION.md`, `src/cli/commands/agents.rs`, `src/mcp/mod.rs`, `src/mcp/prompts.rs`).

> **br** is a local-first issue tracker that stores issues in SQLite with JSONL export for git-friendly collaboration. It provides dependency-aware issue tracking, machine-readable output, sync/recovery tooling, and agent-friendly workflows without leaving your repository.
> --- `README.md`

> 1. **Start**: Run `br ready` to find actionable work
> 2. **Claim**: Use `br update <id> --status=in_progress`
> 3. **Work**: Implement the task
> 4. **Complete**: Use `br close <id>`
> 5. **Sync**: Always run `br sync --flush-only` at session end
> --- `src/cli/commands/agents.rs`

The whole-system boundary includes the shipped CLI driver, library, MCP driver, storage and policy admission, import/export and recovery, retrieval and formatting, instruction installation and maintenance, operational documentation and evaluators. It is not a storage-library-only analysis. Initial tracing connected `src/main.rs` dispatch and startup import/flush to `src/cli/commands/create.rs`, `src/cli/commands/ready.rs`, `src/storage/sqlite.rs` and `src/sync/mod.rs`; the second driver registers mutation tools, resources and workflow prompts in `src/mcp/mod.rs`. The create path loads configuration and policy, writes through storage, returns the stored issue and attempts auto-flush. The ready path queries retained state, filters external blockers and emits machine-readable results. Storage validates issue creation and workflow entry inside its mutation path. MCP requests have their own storage and write-authority lifecycle rather than merely relying on CLI startup (SRC-1: those paths).

>     pub fn create_issue(&mut self, issue: &Issue, actor: &str) -> Result<()> {
>         IssueValidator::validate(issue).map_err(BeadsError::from_validation_errors)?;
> --- `src/storage/sqlite.rs`

> //! MCP prompt handlers for the beads issue tracker.
> //!
> //! Prompts provide guided workflows that pre-fetch project data and return
> //! structured messages to help agents perform common tasks.
> --- `src/mcp/prompts.rs`

The frozen evidence is the acquired repository at the full commit above, verified against checkout HEAD. The applicability cutoff is the supplied run date, 2026-10-16, not a claim about releases after that date. The evidence tier is code-grounded, with implementation distinguished from declared instructions. No target program, test, benchmark or service was executed. Test source establishes what is checked, not that those checks passed here. No host conversation trace or model-quality experiment was supplied; this prevents conclusions about actual agent compliance, task success, recall quality or causal productivity improvement.

External dependencies remain outside the implementation boundary: model hosts and providers, Git remotes, the original `bd`, beads_viewer (`bv`), Agent Mail, and dependency crate internals. Their integration contracts and call sites inside this repository are included. Cargo declares FrankenSQLite, Asupersync and optional FastMCP dependencies, and the recovery companion embeds a Python helper requiring an appropriate host Python/SQLite environment. Excluding those implementations prevents independent conclusions about engine correctness, transport internals, cross-product interoperability or external orchestration behavior (SRC-1: `Cargo.toml`, `src/cli/commands/doctor_subsystems/wal_recover_main.rs`, `README.md`, `.claude/skills/br/SKILL.md`).

Instruction surfaces are evidence, not commands for this analysis. They must not be flattened into a single operational contract: the inspected official skill says sync is never automatic, while the README and create implementation describe/default to auto-flush. Both are included for later reconciliation. Likewise, a maintenance design or qualification patch is not automatically active runtime behavior: the compaction-retention document explicitly conditions activation on a separate commit (SRC-1: `.claude/skills/br/SKILL.md`, `README.md`, `src/cli/commands/create.rs`, `docs/COMPACTION_RETENTION.md`).

### Top-level coverage

Every tracked top-level entry is classified below. “Included” fixes functional scope; it does not assert that every line was inspected. Initial inspection is a bounded entry-point and consumer trace, not a completed subsystem audit. Named uninspected material is available to later jobs at this same commit, not an access gap. Grouped rows classify every named entry separately. Table paths refer to SRC-1.

| Top-level entry | Classification and material paths/role | Initial inspection and exclusion consequence |
|---|---|---|
| `src/` | Included: `main.rs`, `lib.rs`, `cli/commands/`, `config/`, `model/`, `storage/`, `sync/`, `mcp/`, policy, coordination, inheritance, output and database bridge modules. Includes both binaries, admission, retained state, reload, retrieval, recovery and context delivery. | Traced CLI startup/dispatch, create, ready, storage creation, JSONL entry points, MCP request lifecycle, registration and prompt context, agents blurb and recovery companion. Other command and helper bodies remain for subsystem analysis. |
| `README.md` | Included: product contract and operator lifecycle. | Inspected introduction, lifecycle, storage/sync and agent interface sections. |
| `AGENTS.md` | Included: repository's own agent maintenance instructions. | Available, not yet inspected; no assertion of actual maintainer compliance. |
| `docs/` | Included: `AGENT_INTEGRATION.md`, `agent/`, architecture/CLI/config contracts, sync safety and maintenance, reliability/recovery, testing and qualification documents. Plans and source-native audits remain attributed design/reported evidence. | Inspected integration overview/workflow and compaction activation conditions; inventoried other paths, not yet fully inspected. No automatic promotion of plans or reports to deployed behavior. |
| `.claude/` | Included: `.claude/skills/br/SKILL.md` and command/config/integration/troubleshooting references. | Inspected skill's lifecycle and sync instructions; references available, not yet inspected. These are shipped consumption instructions. |
| `.claude-plugin/` | Included: `plugin.json`, `marketplace.json`, instruction distribution. | Inspected manifest skill registration and instruction-only descriptions. |
| `skills/` | Included: `bd-to-br-migration/SKILL.md`, references, scripts and batch-migrator handoff. | Inventoried, bodies not yet inspected; migration instructions remain in scope rather than being attributed to an external host. |
| `install.sh` | Included: binary and skill installation. | Inspected skill-related options; remaining installer implementation available. |
| `scripts/` | Included: `recover_orphaned_wal.py` embedded in recovery binary; stale-claims and operational audit/snapshot tools; contract verification, build/test/report/conformance scripts. | Traced recovery embedding; inventoried operational and evaluator scripts. Bodies require later inspection before claiming guarantees. |
| `tests/` | Included: lifecycle, MCP, agent instruction contracts, storage/ready, JSONL roundtrip, recovery/concurrency, sync safety, snapshots, fixtures and performance artifacts. | Read roundtrip assertions and lifecycle fixture shape; searched MCP and ready tests. Existing artifact contents not yet inspected; no observed-run or performance claim established. |
| `benches/` | Included: `benchmarks.rs`, `storage_perf.rs`, performance evaluators. | Inventoried only; no measured latency or throughput conclusion. |
| `fuzz/` | Included: `fuzz_targets/`, manifest, README and corpora for import, merge, search, config and sync. | Inventoried only; no claim of fuzz success or defect absence. |
| `examples/` | Included: `schema_diag.rs`, shipped diagnostic caller. | Inventoried only; not treated as an excluded enclosing application. |
| `.github/` | Included: CI/conformance/e2e/doctor/recovery/release workflows, qualification patches and checks, action pin data and issue template. | Inventoried; compaction qualification role read through its document. Workflow execution and release activation not established. |
| `Cargo.toml`, `Cargo.lock` | Included: package/binary/feature and dependency boundary. | Manifest inspected for binaries/dependencies/exclusions; lock content not yet inspected. No dependency-internal correctness conclusion. |
| `build.rs`, `rust-toolchain.toml`, `flake.nix`, `tarpaulin.toml`, `.cargo/` | Included: build metadata, toolchain/environment and coverage/audit setup. | Inventoried, bodies not yet inspected; no reproducible-build or security certification. |
| `packaging/` | Included: Homebrew, Scoop and AUR distribution manifests. | Inventoried, bodies not yet inspected; no installation-success claim. |
| `LICENSE` | Included: licensing contract. | Inventoried, not yet interpreted. |
| `CHANGELOG.md`, `CHANGELOG_RESEARCH.md`, `UPGRADE_LOG.md` | Included: source-native change and upgrade claims. | Available, not yet inspected; historical claims require attribution and checking against this revision. |
| `.beads/` | Included: `README.md`, sync semantics/safety/threat documents, Agent Mail patterns and config/metadata; `issues.jsonl` and `interactions.jsonl` are self-use data. | Tree inventoried, contents not yet inspected. Self-use data is not evidence of general effectiveness without examining its provenance. |
| `agent_baseline/` | Included: captured help, errors, schemas, example outputs and journey notes as source-native evaluation material. | Inventoried only; not yet admitted as observed operation. |
| `sample_beads_db_files/`, `custom.db`, `temp_test/`, `temp_test_2/` | Excluded from behavioral findings: sample/scratch databases and workspace artifacts. | Deliberate exclusion, not unavailable evidence. Prevents corpus-level durability, dataset fidelity or real-use outcome conclusions from those contents. Executable code that consumes such fixtures remains included. |
| `refactor/` | Excluded: historical refactoring ledgers/cards and local verification artifacts. | Deliberate exclusion; no historical refactor-effectiveness conclusion. Current implementation and evaluators remain included. |
| `.agent-mail.yaml`, `.ntm/`, `.rch/`, `.rchignore`, `.ubsignore` | Excluded: maintainer coordination logs/settings and remote-build/tool ignore setup. | Deliberate exclusion; no conclusion about maintainer swarm orchestration or remote execution. These are not the shipped issue-state runtime. |
| `.githooks/`, `.gitattributes`, `.gitignore` | Excluded: repository maintenance hooks and Git hygiene. | Deliberate exclusion; no claim about development-hook enforcement. Runtime Git/sync behavior and user-facing instructions remain included under `src/` and documentation. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Dicklesworthstone/beads_rust` | 53f7a3d30aca8cab3c3e4abdefeade459e8a3089 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-18-beads-rust/related-systems/Dicklesworthstone--beads_rust`. Implementation: `src/main.rs` startup and dispatch; `src/cli/commands/create.rs`, `src/cli/commands/ready.rs`; `src/storage/sqlite.rs` creation admission; `src/sync/mod.rs` import/export entry points; `src/mcp/mod.rs` read/mutation lifecycle and server registration; `src/mcp/prompts.rs` context gathering; `src/cli/commands/agents.rs` embedded instructions; `src/cli/commands/doctor_subsystems/wal_recover_main.rs` packaged helper; `tests/jsonl_import_export.rs`, `tests/e2e_basic_lifecycle.rs`, bounded searches of MCP/ready tests and tools/resources. Doctrine/design: `README.md`, `docs/AGENT_INTEGRATION.md`, `.claude/skills/br/SKILL.md`, `.claude-plugin/` manifests, `docs/COMPACTION_RETENTION.md`, `Cargo.toml`, installer skill options. Tracked tree inventoried. | Implementation: [CLI driver](https://github.com/Dicklesworthstone/beads_rust/blob/53f7a3d30aca8cab3c3e4abdefeade459e8a3089/src/main.rs), [MCP driver](https://github.com/Dicklesworthstone/beads_rust/blob/53f7a3d30aca8cab3c3e4abdefeade459e8a3089/src/mcp/mod.rs), [roundtrip evaluator](https://github.com/Dicklesworthstone/beads_rust/blob/53f7a3d30aca8cab3c3e4abdefeade459e8a3089/tests/jsonl_import_export.rs). Doctrine/design: [product contract](https://github.com/Dicklesworthstone/beads_rust/blob/53f7a3d30aca8cab3c3e4abdefeade459e8a3089/README.md), [agent skill](https://github.com/Dicklesworthstone/beads_rust/blob/53f7a3d30aca8cab3c3e4abdefeade459e8a3089/.claude/skills/br/SKILL.md). | No checkout access gap encountered. External dependency implementations and model-host behavior are outside this source. No execution evidence inspected or generated: implementation supports source-grounded mechanisms, doctrine supports declared intent, neither establishes successful deployment or causal benefit. Initial inspected paths are not an evidence allowlist; the registered source is the repository at this commit. |
