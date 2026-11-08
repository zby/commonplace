---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Amanuensis codebase memory, its agent workflow, MCP state service and publication loop at a98093dc7aad3c0e64d42132ece305fc5ea7f3f9."
run-id: AAS-2026-11-08-amanuensis-b3a8e3e53488-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: a98093dc7aad3c0e64d42132ece305fc5ea7f3f9
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/nfeldman/amanuensis
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/amanuensis-04147cbf1a99/related-systems/nfeldman--amanuensis
  revision: a98093dc7aad3c0e64d42132ece305fc5ea7f3f9
  sha256: null
---

# Amanuensis boundary

## Boundary and evidence

Amanuensis is an in-scope memory/knowledge/context-engineering system for coding agents. Its intended use is to retain an evidence-backed account of a codebase across sessions, expose it to later agents, and publish a human-readable conspectus. The target is the shipped system, not just its SQLite API. It includes the model-facing survey and maintenance instructions, MCP service, installation and host adapters, persistence and admission mechanisms, later-consumption readers, materializer, and shipped evaluation and development drivers. This is a `whole-system` boundary: the agent-facing method and repository-local callers are not treated as an excluded enclosing application. SRC-1: `README.md`, `.claude/skills/amanuensis/SKILL.md`, `mcp-server/package.json`, `mcp-server/src/index.ts`.

The shipped skill makes the model-dependent part explicit:

> You are the Amanuensis coordinator — a methodical architectural scribe. You
> survey codebases by running a **phased, evidence-driven, adversarially
> reviewed** methodology and recording everything in a persistent conspectus
> (the `amanuensis-memory` MCP server's SQLite DB plus prose artifacts in a
> git-backed storage directory).
> --- `.claude/skills/amanuensis/SKILL.md`

The functional boundary follows the shipped loop:

- **Produce and maintain:** the skill supplies cold/warm-start routing, phased survey, adversarial review, checkpoints, and later-session reading. Its refresh reference explicitly routes changed code back through examination and record updates. These are shipped agent instructions, not evidence that a host always obeys them. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `.claude/skills/amanuensis/references/refresh.md`.
- **Bind, admit, and retain:** the `amanuensis-memory` executable enters `mcp-server/src/index.ts`, binds a workspace, lazily opens its database, registers reader and writer tools, validates arguments, and invokes handlers. `openDatabase` applies migrations and schema before returning the SQLite connection. The inspected claim writer requires a session, resolves revisions, checks ancestry and evidence, then inserts inside a transaction. This establishes a real state service, without establishing that all semantic claims admitted by it are true. SRC-1: `mcp-server/package.json`, `mcp-server/src/index.ts`, `mcp-server/src/db.ts`, `mcp-server/src/tools/claims.ts`.
- **Checkpoint and reload:** `commit_phase_gate` checkpoints the database and calls the storage Git layer. New service connections open the bound database rather than reconstructing knowledge from a chat transcript. The repository's rebuild driver is an included caller: it starts MCP connections, reads project state and history, and imports predecessor findings through carry tools before closing the rebuilt store. SRC-1: `mcp-server/src/tools/storage-history.ts`, `mcp-server/src/index.ts`, `dev/rebuild-self-conspectus-store.mjs`.
- **Consume:** the skill's locus route and the installer's optional agent-instruction block direct later agents to `describe_locus`. The inspected handler reads standing, scope and matching findings from the database, then builds the requested account sections. The server also advertises `get_attention` and `get_history` in its opening instructions. These routes are part of the target's memory loop, not external consumers excluded merely because they call an API. SRC-1: `.claude/skills/amanuensis/SKILL.md`, `mcp-server/src/cli.ts`, `mcp-server/src/tools/locus.ts`, `mcp-server/src/index.ts`.
- **Project and check:** `materialize_docs` preflights reconciliation, launches the Python materializer with bound storage/workspace paths, and records read-back results. The Python entry point reads `memory.db` and prose and supports staged clean publication. Packaging copies the canonical skill and materializer into the npm artifact. Historical-evaluation code prepares participant trees and scores workspaces; tests and local receipt drivers are included evaluation surfaces, not proof of product effectiveness merely because they exist. SRC-1: `mcp-server/src/tools/materialize.ts`, `materializer/materialize.py`, `mcp-server/scripts/prepack-bundle-assets.mjs`, `mcp-server/scripts/historical-evaluation.mjs`, `.github/workflows/test.yml`.

Two short passages anchor the distinction between durable state and generated views, and the intended maintenance obligation:

> Both views are derived. Durable authority remains in `memory.db` and the
> registered prose artifacts. Publication read-back verifies HTML and Markdown
> independently, so a healthy companion cannot mask a damaged primary view.
> --- `.claude/skills/amanuensis/SKILL.md`

> `clear_staleness` asserts **"I re-examined this file at this commit."**
> It is a claim, not a counter reset.
> --- `.claude/skills/amanuensis/references/refresh.md`

### Frozen evidence and limits

The sole frozen source is SRC-1, the Git repository at full commit `a98093dc7aad3c0e64d42132ece305fc5ea7f3f9`. The acquired checkout's HEAD matched that revision during boundary inspection. The applicability cutoff is 2026-11-08: this analysis concerns that frozen tree, not later releases, live documentation, remote services, or the current npm package. The overall tier is `code-grounded`, combining executable source with shipped doctrine/design. Initial inspection used the tracked tree, complete small files and bounded source ranges; it did not execute Amanuensis, its tests, examples, providers, or development drivers.

External dependencies include the MCP host and its model execution, Node.js, Python, Git, SQLite through `better-sqlite3`, the MCP SDK and other declared packages. Their implementations are not separately frozen. The host supplies model calls and tool execution; Amanuensis ships the workflow and state interface. Excluding host/provider internals prevents conclusions about model scheduling, context assembly internal to those hosts, provider reliability, or guaranteed compliance with the skill. SRC-1: `mcp-server/package.json`, `mcp-server/src/index.ts`, `.claude/skills/amanuensis/SKILL.md`, `mcp-server/src/tools/materialize.ts`.

No live target workspace, private populated store, or independent longitudinal user trial is supplied as a separate source. Thus this boundary supports source-level mechanism analysis, not a claim that a particular deployed memory is accurate, that all gates passed in this environment, or that repeated explanation costs fell in practice. Repository-contained receipts, traces, generated self-documentation and design studies remain available at the pin; they must be inspected and attributed before supporting reported or observed operation. They are not independent evaluations. An available file not yet inspected is not an access gap.

### Top-level coverage

Every top-level tracked file or directory is classified below. “Included” defines functional coverage, not a claim that every descendant has already been read. Initial inspection is identified separately; remaining material paths are available to subsequent jobs within SRC-1. Tree membership alone supplies no behavioral finding.

| Top-level path | Classification and material paths/role | Initial inspection and consequence of exclusion or remaining work |
|---|---|---|
| `.claude/` | Included: `skills/amanuensis/SKILL.md` and `references/` supply agent prompts, survey phases, onboarding, refresh, audit and later-consumption instructions. | Skill and refresh read; other references available, not yet inspected. No shipped maintenance path is excluded. |
| `.github/` | Included: `workflows/test.yml`, publish, published-smoke and pages workflows; `FUNDING.yml` is ancillary. | Test workflow opening and test routing inspected; remaining workflow details not yet inspected. No claim of successful CI or publication. |
| `.gitignore` | Excluded: repository ignore policy. | Listed, not read. Cannot assess ignored local-state hygiene from it. Packaged asset provenance instead inspected in the prepack script. |
| `.mcp.json` | Included: repository-local stdio MCP launch registration and workspace/autoprogress environment. | Read. External `mise` and host internals are not included. |
| `.pecia/` | Included: configuration resolver to `dev/pecia-resolve-finding.mjs`, work ledger and snapshots as development-state integration. | `config.yaml` read; snapshot and work records not yet inspected. No claim of reconciled defect state. |
| `.tool-versions` | Excluded: developer tool-version selection. | Listed, not read; cannot establish exact author development environment. Runtime package requirements remain included. |
| `CONTRIBUTING.md` | Included: contributor and test procedure. | Available, not yet inspected; no assertion that procedures were followed. |
| `HISTORY.md` | Included: attributed release history. | Available, not yet inspected; release claims require reading. |
| `INSTALLATION.md` | Included: supported host setup, storage and operational instructions. | Available, not yet inspected; executable CLI and launch registration initially traced instead. |
| `LICENSE` | Excluded: legal terms, not the memory loop. | No legal/licensing assessment. |
| `README.md` | Included: intended use, deployment entry and stated product limits. | Read in full. Claims remain author declarations unless independently grounded. |
| `ROADMAP.md` | Included: declared plans and claim boundaries, not evidence of shipped behavior by itself. | Available, not yet inspected. No claim that planned work is implemented. |
| `design/` | Included: explanation, reader-lenses and survey-depth specifications; output-panel prototypes and validation material; plans, decisions and receipts. | Tree inventoried; contents not yet inspected. No prototype usability or design-completion conclusion. |
| `dev/` | Included: rebuild, carry, readback, regeneration and publication drivers; activation harnesses and receipts; ADRs; Pecia bridge/resolver; local tests and measurements. | Rebuild MCP client, state/history calls and carry import traced. Other drivers, ADRs and receipts available but not yet inspected. Not excluded as an external application. |
| `docs/` | Included as generated self-conspectus output: Markdown/HTML, manifests, search index and subsystem pages. | Tree inventoried, contents not yet inspected. Generated accounts are not substitutes for source inspection or independent confirmation of their findings. |
| `materializer/` | Included: `materialize.py`, `amanuensis_materializer/` database readers, renderers, projection/readback modules, tests and package metadata. | Entry point read in full; internals/tests available for deeper tracing. No execution or read-back success asserted. |
| `mcp-server/` | Included: `src/index.ts`, `cli.ts`, project/host binding, database/schema/invariants, all `src/tools/`; contracts, fixtures, scripts, tests, package and lockfile. Covers admission, persistence, maintenance, readers, review/design/research/learning/evaluation and adapters. | Package, server entry, claim handler, database opening, locus handler, storage-history tool, materialization wrapper, installer skill copying/consumer block, prepack and historical evaluator inspected. Remaining handlers and tests are included, not presumed verified. |
| `scholiast/` | Included as embedded research inputs and trial/evaluation material: platform-landscape capture/trials, report-record-presentation and task-workspace-reorientation-indexes. | Tree inventoried, contents not yet inspected. External works referenced there are not additional frozen sources; no claim about their correctness or general applicability. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/nfeldman/amanuensis` | a98093dc7aad3c0e64d42132ece305fc5ea7f3f9 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/amanuensis-04147cbf1a99/related-systems/nfeldman--amanuensis`. Implementation: MCP/package entry, database opening, claim admission, locus reading, storage checkpoints, materialization wrapper and Python entry, installer skill copy/consumer block, prepack copying, historical prepare/score functions, rebuild client and carry import. Doctrine/design: README, skill, refresh reference, repository MCP registration, Pecia resolver configuration and CI test routing. Full tracked tree inventoried. | Implementation: [server](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/mcp-server/src/index.ts), [claim admission](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/mcp-server/src/tools/claims.ts), [consumer](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/mcp-server/src/tools/locus.ts), [materializer](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/materializer/materialize.py), [rebuild caller](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/dev/rebuild-self-conspectus-store.mjs), [evaluator](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/mcp-server/scripts/historical-evaluation.mjs). Doctrine/design: [skill](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/.claude/skills/amanuensis/SKILL.md), [refresh](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/.claude/skills/amanuensis/references/refresh.md), [README](https://github.com/nfeldman/amanuensis/blob/a98093dc7aad3c0e64d42132ece305fc5ea7f3f9/README.md). Additional inspected paths are named above. | No checkout access gap identified. No target execution performed; external host/provider implementation, live stores and independent longitudinal results are outside the frozen source. These limits prevent guarantees of actual agent compliance, deployed content truth, runtime test success or sustained product benefit. Repository-contained traces and receipts are available but not yet inspected and confer no observed-run or causal-experiment support at this stage. |
