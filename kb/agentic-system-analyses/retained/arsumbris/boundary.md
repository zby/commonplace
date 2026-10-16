---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Arsumbris's typed-knowledge IDE design and installation entry artifact at commit 716bb14f2bf50e249d414525c8e07c50478fc786, without the sibling runtime implementations."
run-id: AAS-2026-10-15-arsumbris-a9be6bac297f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "716bb14f2bf50e249d414525c8e07c50478fc786"
analysis-cutoff: "2026-10-15"
evidence-tier: doc-grounded
source:
  identity: https://github.com/arsumbris/arsumbris
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-arsumbris/related-systems/arsumbris--arsumbris
  revision: 716bb14f2bf50e249d414525c8e07c50478fc786
  sha256: null
---

# Arsumbris boundary

## Boundary and evidence

This run examines the design of Arsumbris, an agent-native IDE for typed knowledge, as documented in its installation and architecture entry repository. The intended use is to establish its declared knowledge substrate, agent integration, extension contracts and bootstrap responsibilities. The target class is `memory/knowledge/context-engineering system`: the declared system combines typed knowledge repositories with agent tools, guidance and context. It is not classified as an enclosing model runtime merely because it connects an agent harness. This classification rests on SRC-1, `README.md` and `au-mcp.md`:

> A malleable, agent-native IDE for typed knowledge.
> --- `README.md`

> Besides tools, a repo ships guidance and context.
> --- `au-mcp.md`

The boundary kind is `complete artifact, partial loop`. The frozen entry repository supplies architecture descriptions, installation instructions, release and safety declarations, and one executable device-configuration seeder. It does not contain the implementations of the graph engine, Electron host, MCP daemon, plugins, adapters or knowledge packages. Those are separately installed repositories, not invisible responsibilities attributed to this repository. SRC-1, `INSTALL.md` explicitly establishes the distribution boundary:

> arsumbris is not one repo. It is a set of repos that sit **side by side** under one parent:
> --- `INSTALL.md`

The complete disposition means a coherent, in-scope documentary boundary has been established, not that the full platform implementation or operational loop has been verified. The overall evidence tier is `doc-grounded`; the seeder alone adds a narrow implementation layer.

### Functional coverage and entry-point trace

The included documentary loop runs from repositories of Markdown/YAML through a live typed graph, UI projections and agent-facing plugins, then back to governed file changes. SRC-1, `au-engine.md` describes indexing, dependency/workspace mounting, diagnostics, a Unix-socket daemon and a guarded write path. SRC-1, `au-host.md` describes projection discovery, composition instances, file reads/writes, saved pane configuration and daemon supervision. SRC-1, `au-mcp.md` describes typed tools, hooks, skills, injects, profiles, the mediation/action/observation pipeline and a session ledger. These are declared responsibilities, not inspected executable behavior.

The shipped entry instruction in SRC-1, `README.md` sends an installing agent to `INSTALL.md`. That guide installs separately versioned sibling repositories, builds the engine and host, invokes `scripts/seed-device-config.py`, then hands host launch to the user. The script's `main` parses options, discovers repository manifests, merges existing device registries, resolves tool locations and writes only when `--write` is supplied. Its outputs are the engine's located-repository registry, the host's template-repository list and the host's tool-path configuration. The script constructs the MCP entry path as `src/cli.ts` within a discovered `au-mcp` repository; that entry is not a tracked file of this source. These implementation findings are limited to SRC-1, `scripts/seed-device-config.py`:

> if __name__ == "__main__":
>     main(sys.argv[1:])
> --- `scripts/seed-device-config.py`

> if not write:
>         print("\n--- would write (engine repos.yaml) ---")
> --- `scripts/seed-device-config.py`

The documented downstream consumers are the engine's repository resolution and the host's pre-graph launcher/tool spawning. SRC-1, `INSTALL.md` supplies that consumer contract, but not consumer code:

> The host's new-user setup runs **before any engine or daemon**, on no workspace yet (the engine only runs against the workspace setup creates). So it reads two device-global files by plain IO, and they must exist first. This step writes them from the repos you just cloned.
> --- `INSTALL.md`

The subsequent host launch materializes a workspace and starts the engine according to SRC-1, `INSTALL.md` and `au-host.md`. Agent launch, skill/inject materialization and lifecycle mapping are documented in SRC-1, `au-mcp.md`; their actual callers live outside this frozen repository. No runtime, example, installer or test was executed.

### Tracked top-level coverage

This table accounts for the entire tracked entry artifact. It does not promote a documentary platform overview into whole-system implementation coverage. All textual files listed as included were read in full.

| Top-level tracked path | Coverage | Material paths and role | Limit or conclusion prevented |
| --- | --- | --- | --- |
| `README.md` | Included; doctrine/design | System purpose, three-layer overview and agent-facing install prompt | Supports declared purpose, not demonstrated capability. |
| `INSTALL.md` | Included; doctrine/design and reported operation | Sibling-repository set, install order, seeder invocation, documented consumers, user launch handoff and claimed release coherence | External install/build/launch commands were not executed; no installation success or compatibility result is established. |
| `au-engine.md` | Included; doctrine/design | Repo/workspace declarations, type language, indexing, diagnostics and daemon access | Engine persistence, reindexing, mutation and validation code is absent from the frozen source; actual enforcement is not established. |
| `au-host.md` | Included; doctrine/design | Projection examples, mounting contract, file/config surfaces, composition and launcher description | Actual state reload, UI execution and engine supervision cannot be verified without the separate host implementation. |
| `au-mcp.md` | Included; doctrine/design | Plugin/hook examples, profiles, skills/injects, mediation pipeline, ledger and adapters | No daemon, adapter, ledger or guidance-materialization implementation is present; enforcement and later context consumption remain declarations. |
| `scripts/` | Included; implementation and doctrine/design | `scripts/seed-device-config.py`, the sole tracked script: discovery/pruning, registry merge, tool-path resolution, dry-run/write branches | Downstream readers are documented but absent here; source inspection establishes write logic, not successful execution or end-to-end initialization. |
| `VERSION.md` | Included; doctrine/design | Release 0.0.2-alpha component identifiers and internal contract integers | Listed sibling commits are release metadata, not acquired evidence or additional source pins; release testing is not verified. |
| `MIGRATION.md` | Included; doctrine/design and reported operation | Version policy, migration instructions, declared behavior changes and compatibility claims | No migration execution or compatibility trace is supplied. |
| `SAFETY.md` | Included; doctrine/design | Declared arbitrary-code execution, privileges and absence of sandboxing | Supports the warning, not an independent security audit. |
| `LICENSE.md` | Included; documentary context | Licensing terms | No legal interpretation or compliance assessment is made. |
| `img/` | Deliberately excluded; not inspected | `img/banner.png`, presentation asset linked from the README | No visual/UI inference is drawn from the banner; this exclusion prevents no claimed runtime conclusion. |

### Exclusions, dependencies and time boundary

The immutable evidence revision is `716bb14f2bf50e249d414525c8e07c50478fc786`; the applicability cutoff is 2026-10-15. The acquired checkout's HEAD matched this revision and its status was clean at inspection. This run adds no repositories or captures. Release labels and component hashes in SRC-1, `VERSION.md` do not expand the frozen evidence boundary.

The separate repositories named in SRC-1, `INSTALL.md` include the engine and SDK/type specification; host; MCP kernel, SDK, core plugins and Claude Code/Codex adapters; type code generator; defaults/templates; and knowledge packages for ontology, weaving, rules, writing, agent guidance, skills, governance, competency, ingest and tree research. They are not present in this acquired repository, so their implementation and substantive instructions are unavailable within the authorized frozen source. This is a source-boundary gap, not an assertion that those upstream repositories are inaccessible. It prevents whole-system claims about production, maintenance, admission and reuse of retained knowledge, actual shipped prompts, governance enforcement and evaluators. Adding their source would require a changed evidence boundary rather than silently treating linked repositories as inspected.

External execution dependencies documented by SRC-1, `INSTALL.md` include Rust/Cargo, Node/pnpm, Electron/native terminal support and an optional agent harness; SRC-1, `au-mcp.md` describes adapters between that harness and the MCP layer. Model inference and the harness's enclosing control loop are not inspected or attributed to the target. The inspected tree contains no evaluator implementation or run artifacts. Claims of testing in SRC-1, `INSTALL.md` and `MIGRATION.md` remain reported operation, not observed runs or causal experiments. No available textual file in this source was left uninspected; the banner is the deliberate nonfunctional exclusion.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/arsumbris/arsumbris` | 716bb14f2bf50e249d414525c8e07c50478fc786 | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-arsumbris/related-systems/arsumbris--arsumbris`. Implementation: full `scripts/seed-device-config.py`. Doctrine/design: full `README.md`, `INSTALL.md`, `au-engine.md`, `au-host.md`, `au-mcp.md`, `SAFETY.md`, `VERSION.md`, `MIGRATION.md`; licensing context: full `LICENSE.md`. Reported operation: installation/platform testing and compatibility assertions in `INSTALL.md` and `MIGRATION.md`. Tracked tree and source pin inspected. | Implementation: [seeder](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/scripts/seed-device-config.py). Doctrine/design: [overview](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/README.md), [installation](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/INSTALL.md), [engine](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/au-engine.md), [host](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/au-host.md), [agent layer](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/au-mcp.md), [safety](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/SAFETY.md), [release](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/VERSION.md). Reported operation: [migration/compatibility](https://github.com/arsumbris/arsumbris/blob/716bb14f2bf50e249d414525c8e07c50478fc786/MIGRATION.md) and installation anchor. | Sibling implementations, knowledge/maintenance instructions, evaluators and runtime traces are outside this frozen source. Implementation layer supports only seeder logic; documentary layer supports intended platform behavior; reported operation is unverified. No observed-run or causal-experiment layer. `img/banner.png` deliberately excluded, not an access failure. |
