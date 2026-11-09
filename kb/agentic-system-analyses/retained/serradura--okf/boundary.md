---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OKF's agent-operated knowledge ecosystem, including its four gems, skills and host hooks, at cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c."
run-id: AAS-2026-11-08-okf-8bc42addf404-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/serradura/okf
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/okf-817c1d452ed0/related-systems/serradura--okf
  revision: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
  sha256: null
---

# OKF boundary

## Boundary and evidence

This run covers the OKF implementation ecosystem in the supplied monorepo, not only its baseline Ruby library and not the Open Knowledge Format independently of this implementation. Its intended use is to retain project knowledge between agent sessions in Markdown bundles, maintain that knowledge during work, and retrieve selected content for later tasks. The target is a **memory/knowledge/context-engineering system** with a **whole-system** boundary. Its model-dependent work is performed by the agent reading the shipped skills and prompts; the deterministic Ruby components provide storage, retrieval, checks and host integration. The model host is an external dependency, not an OKF-owned enclosing runtime. These distinctions follow SRC-1, `README.md`, `skills/okf/SKILL.md`, `skills/okf/playbooks/consume.md` and `gems/okf-mcp/lib/okf/mcp/server.rb`.

The skill explicitly assigns semantic judgment to its consumer rather than the executable:

> - **You judge — the CLI can't —** meaning: contradictions, semantic staleness
>   (parses fine, no longer true), whether a loose file is terminal-by-design, whether
>   a singleton tag is a deliberate marker. Tool output is evidence, never a verdict.
> --- `skills/okf/SKILL.md`

The persistence-to-consumption loop includes the prompts, not just a callable storage API. The consume playbook routes discoveries back into maintenance (SRC-1, `skills/okf/playbooks/consume.md`):

> 3. **Write-back reflex:** if you learn something durable while working — a fact the
>    bundle lacks, a link it is missing, a concept that no longer matches reality —
>    switch to [maintain](maintain.md) and record it. That reflex is what keeps the
>    bundle alive.
> --- `skills/okf/playbooks/consume.md`

### Functional inclusions and entry-point tracing

All four shipped gems and their consumers are inside the target. They are not excluded applications merely because they use the baseline library. The following initial trace establishes the system boundary; it does not claim every implementation branch has already been analyzed.

| Responsibility | Shipped path and initial trace (SRC-1) |
|---|---|
| Author, update and later consume durable knowledge | `skills/okf/SKILL.md` routes to playbooks. `skills/okf/playbooks/maintain.md` specifies concept, provenance, index and log updates followed by validation and curation. `skills/okf/playbooks/consume.md` supplies orientation, selective reading and write-back. The canonical packaged tree is `gems/okf/lib/okf/skill/`; plugin and installer copies remain included. |
| Parse, retain in memory, publish and reload bundles | `gems/okf/lib/okf/bundle/reader.rb` reads visible Markdown into concepts, reserved text and unparseable entries. `gems/okf/lib/okf/bundle.rb` exposes validation, lint, graph, catalog and directory maps. `gems/okf/lib/okf/bundle/folder.rb` connects load/save/reload to Reader and Writer. `gems/okf/lib/okf/bundle/writer.rb` materializes a temporary bundle, validates it and promotes it under a lock. |
| CLI dispatch and extension consumers | `gems/okf/exe/okf` calls `OKF::CLI.start`; `gems/okf/lib/okf/cli.rb` registers baseline command classes and discovers `okf/plugin.rb` extensions when needed. The sibling MCP, TUI and Pro command implementations are included, not treated as external hosts. |
| Human browsing and serving | `gems/okf/lib/okf/server/app.rb` receives a folder, serves graph/catalog/index/log/search and individual concept endpoints. `gems/okf-tui/lib/okf/tui/cli.rb` resolves requested bundles and starts the app; `gems/okf-tui/lib/okf/tui/workspace.rb` owns the selected workspace and registry-facing state. Graph rendering, hub and TUI views are included consumers. |
| Serve retained content to model hosts | `gems/okf-mcp/lib/okf/mcp/cli.rb` builds a registry, backend and server, then serves stdio or HTTP. `gems/okf-mcp/lib/okf/mcp/server.rb` supplies tools, resources, prompts and retrieval instructions. `gems/okf-mcp/lib/okf/mcp/backend.rb` selects an optional backend or the shipped memory backend. |
| Post-edit feedback | `plugin/hooks/hooks.json` registers the curation command after Write/Edit/MultiEdit. `plugin/hooks/scripts/curate.rb` identifies an edited bundle, invokes CLI validation/lint and returns findings as host context. This advisory path is distinct from Pro's gates. |
| Seed and operate a knowledge/work repository | `gems/okf-pro/lib/okf/pro/cli.rb` maps scaffold, state readers, writers and hook checks. `gems/okf-pro/lib/okf/pro/scaffold.rb` installs template trees. `gems/okf-pro/lib/okf/pro/writes.rb` implements targeted board/journal/closure operations. Pro's skill and guides govern filing, reconciliation, attribution, snapshots and workload state. |
| Admit edits, sessions and commits | `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json` wires pre-edit guards, post-edit checks, Stop and SessionStart. `gems/okf-pro/lib/okf/pro/template/gem/.claude/hooks/run` checks checker identity and normalizes failure statuses. The shipped `.githooks/pre-commit` audits staged state; `.github/workflows/okf-pro.yml` validates, lints and audits at CI time. These generated consumers remain inside the boundary. |
| Evaluate structural and integration contracts | The four gems' `test/` trees, the baseline browser suite and CI definitions are included source evidence. Initial test inspection covered skill-copy parity in `gems/okf/test/plugin/sync_test.rb` and wrapper-failure drills in `gems/okf-pro/test/integration/wrapper_test.rb`. No tests were executed and no passing result is inferred from their presence. |

The MCP instructions expose the host boundary directly (SRC-1, `gems/okf-mcp/lib/okf/mcp/server.rb`):

> validate and lint report a
> bundle's health: you may flag what they find, but fixing it belongs to
> the okf skill and CLI — the tools here never write. Bodies are read
> live from disk, so results always reflect the current files.
> --- `gems/okf-mcp/lib/okf/mcp/server.rb`

That is the MCP surface's contract, not a claim that the entire ecosystem is read-only. The baseline writer and Pro writers are included. The baseline executable also makes the shipped driver explicit (SRC-1, `gems/okf/exe/okf`):

> exit OKF::CLI.start(ARGV)
> --- `gems/okf/exe/okf`

### Top-level coverage

The inventory below accounts for every top-level tracked name at the frozen commit. “Included” fixes analytical scope; it does not assert exhaustive reading. Material entry points and consumers were inspected as above. Remaining implementation bodies are available for later inspection under SRC-1, not access gaps. Deliberately excluded ancillary material is identified separately from uninspected included material.

| Top-level file or directory | Treatment | Role, material paths and inspection status; exclusion consequence |
|---|---|---|
| `gems/` | Included | All four packages: `okf/lib/okf/{bundle,cli,server,skill,render}`, `okf-mcp/lib/okf/mcp`, `okf-tui/lib/okf/tui`, `okf-pro/lib/okf/pro` including template prompts, settings, hooks and CI; all package tests, fixtures, manifests, documentation and `.okf/` bundles. Initial executable and prompt trace is above; many individual analyzers, UI bodies and tests remain uninspected. No package is excluded. |
| `plugin/` | Included | `hooks/hooks.json` and `hooks/scripts/curate.rb` inspected; `commands/gem.md`, `.claude-plugin/plugin.json` and the generated skill/reference/template tree remain available as distribution and routing evidence. |
| `skills/` | Included | `okf/SKILL.md`, consume and maintain playbooks, and `okf-principles/SKILL.md` inspected. Other playbooks, specification, references and templates remain included. This covers both knowledge operation and instruction-restructuring doctrine. |
| `resources/` | Included | `ci/github/okf.yml` inspected; companion README is available. These are adopter check recipes, not observed CI executions. |
| `.okf/` | Included | Ecosystem knowledge bundle: `gems/`, `plugin/`, `skills/`, `format/`, `resources/`, `decisions/` and `design/`. Tree inspected and `design/nothing-runs-it.md` read as source-native doctrine. Other leaves remain available; self-description is not independently verified operation. |
| `.okf.json` | Included | Inspected project-local registry mapping the ecosystem and four package bundles. |
| `.claude-plugin/` | Included | `marketplace.json` inventoried as plugin distribution metadata; content not initially inspected. |
| `.claude/` | Included | `CLAUDE.md` inventoried as a maintainer-instruction entry point; not initially inspected. It is source evidence, not authority over this analysis. |
| `.github/` | Included workflows; excluded artwork | `workflows/main.yml` initially inspected for package test jobs; `workflows/docker.yml` and `workflows/okf.yml` remain available. PNG/SVG artwork is deliberately excluded from mechanism evidence; visual-branding and screenshot accuracy conclusions are not supported. |
| `README.md` | Included | Inspected ecosystem purpose, package boundaries, install surfaces, plugin and skill usage; claims remain declared intent unless traced to implementation. |
| `Dockerfile` | Included | Inspected build from `gems/okf/`, runtime image and CLI entry point. No built image or published-image equivalence was observed. |
| `Rakefile` | Included | Inventoried build/test entry point; body not initially inspected. Test and skill-sync implementations may be inspected later. |
| `AGENTS.md` | Included | Inventoried maintainer guidance; not initially inspected. Any later use is attributed doctrine, never an instruction to this worker. |
| `.rubocop.yml` | Included | Inventoried repository lint configuration; not initially inspected. |
| `.dockerignore` | Included | Inventoried build-context configuration; not initially inspected. |
| `.gitignore` | Included | Inventoried repository exclusion configuration; not initially inspected. |
| `CODE_OF_CONDUCT.md` | Excluded | Community conduct policy, not the operational mechanism. No community-governance assessment. |
| `LICENSE.txt` | Excluded | Legal terms; no independent licensing assessment. |
| `NOTICE` | Excluded | Attribution/legal notices; no legal provenance or compliance assessment. |

### Frozen evidence and external limits

The only registered source is `https://github.com/serradura/okf` at `cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c`, with applicability cutoff **2026-11-08**. The supplied checkout's HEAD matched the acquired revision and its Git status was clean when inspected. Its absolute path is an access root, not a second source identity. This run is **code-grounded** because shipped dispatch, storage, retrieval and hook wiring were inspected. Skills, playbooks, comments and repository knowledge also provide doctrine/design evidence; executable behavior and intended use must remain distinct.

External dependencies include an agent/model host capable of following the skills or making MCP requests, Claude Code's hook protocol for the shipped Claude integrations, Ruby and its package environment, and Git/GitHub Actions for commit and CI paths. Docker and the graph's web dependencies are deployment/presentation dependencies (SRC-1, `README.md`, `Dockerfile`, `gems/okf-mcp/lib/okf/mcp/cli.rb`, `gems/okf-pro/lib/okf/pro/template/seed/.claude/settings.json`, `gems/okf-pro/lib/okf/pro/template/gem/.github/workflows/okf-pro.yml`). The optional `okf-sqlite3` implementation is not in this tree; only its detection/fallback seam is covered (SRC-1, `gems/okf-mcp/lib/okf/mcp/backend.rb`). Its internals and comparative backend performance cannot be concluded here.

No external host implementation, model-provider execution, adopter corpus, live documentation site, published package/image contents, benchmark run or session trace is frozen as separate evidence. These exclusions prevent conclusions about host compliance, actual agent write-back frequency, semantic correctness of retained knowledge, cross-session task improvement, production reliability or measured retrieval effectiveness. They do not exclude the shipped prompts, drivers or evaluators from source analysis. No material shipped path was unavailable; available material not yet read is not an access gap. Later revisions and moving live pages are outside the time boundary.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/serradura/okf` | cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/okf-817c1d452ed0/related-systems/serradura--okf`. Complete tracked-tree inventory. Implementation: baseline executable and CLI dispatcher, Bundle/Reader/Writer and Folder routing, server App entry/routes, MCP CLI/backend and initial server definition, TUI CLI and initial Workspace, Pro CLI dispatch and writer/scaffold routing, plugin curation hook, Pro settings/wrapper/pre-commit/CI templates, skill parity tests and initial wrapper drills. Doctrine/design: README, OKF skill, consume/maintain playbooks, okf-principles skill, Pro operating skill, ecosystem enforcement note. Ranged initial reads are not exhaustive implementation coverage. | [baseline entry](https://github.com/serradura/okf/blob/cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c/gems/okf/exe/okf); [skill](https://github.com/serradura/okf/blob/cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c/skills/okf/SKILL.md); [MCP server](https://github.com/serradura/okf/blob/cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c/gems/okf-mcp/lib/okf/mcp/server.rb); [Pro dispatch](https://github.com/serradura/okf/blob/cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c/gems/okf-pro/lib/okf/pro/cli.rb); [curation hook](https://github.com/serradura/okf/blob/cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c/plugin/hooks/scripts/curate.rb). Additional commit-relative anchors appear in the coverage trace above. | No checkout access gap established. External host/dependency internals and live/published artifacts are excluded. No supplied observed run or causal experiment; tests and workflow definitions support intended checks, not passing executions or outcome efficacy. |
