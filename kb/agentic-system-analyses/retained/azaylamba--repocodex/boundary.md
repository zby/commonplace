---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "RepoCodex's shipped repository-memory loop at Git commit 96978e292fcb3b100f53ac024b353e1b8b2c8af4, including agent skills, persistence, retrieval, maintenance and enforcement integrations."
run-id: AAS-2026-11-08-repocodex-bf22ac3623d8-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/azaylamba/repocodex
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/repocodex-7a5aff40a82e/related-systems/azaylamba--repocodex
  revision: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
  sha256: null
---

# RepoCodex boundary

## Boundary and evidence

This run covers RepoCodex as a repository-native memory system for coding agents, not merely its deterministic anchor-checking library or optional MCP server. Its intended use is to retain explanations of code decisions beside source code, retrieve those explanations before later edits, and detect when code changes require memory maintenance. The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system**: the shipped authoring instructions, command drivers, store, retrieval, maintenance paths and enforcement callers are included together (SRC-1, `README.md`, `src/repocodex/cli.py`, `src/repocodex/commands/install.py`).

The target qualifies even though its attester is deterministic. Model-dependent work is assigned to coding and review agents through shipped skills; a repair command can also invoke an external agent harness. Those agent-facing procedures are part of the product, not an excluded enclosing application (SRC-1, `src/repocodex/data/skills/repocodex-coding/SKILL.md`, `src/repocodex/data/skills/repocodex-review/SKILL.md`, `src/repocodex/commands/repair.py`). The coding skill explicitly requires later consumption:

> Read returned concept bodies. Related pages are titles only — open a body only if the edit might touch that scenario.
> --- `src/repocodex/data/skills/repocodex-coding/SKILL.md`

The repair implementation identifies the external harness boundary:

> HARNESS_ORDER = ("cursor", "claude", "codex")
> --- `src/repocodex/commands/repair.py`

The frozen evidence is the acquired repository at **96978e292fcb3b100f53ac024b353e1b8b2c8af4**, with applicability cutoff **2026-11-08**. HEAD matched that full revision and the checkout had no reported changes when inspected. The source mapping above preserves the acquired object. The overall evidence tier is **code-grounded**. Repository documentation and specifications supply declared design, not independent confirmation of agent compliance or effectiveness.

### Functional coverage

The console entry point in `pyproject.toml` and the module entry in `src/repocodex/__main__.py` lead to `src/repocodex/cli.py`. Its command consumers were traced through all command modules. They cover concept admission and persistence (`write`), draft production (`bootstrap`), later consumption (`context`), checking (`validate`), maintenance (`reconcile`, `relocate`, `audit`), external repair invocation (`repair`), advisory output and installation. MCP calls the same command implementations rather than being the only consumer (SRC-1, `pyproject.toml`, `src/repocodex/__main__.py`, `src/repocodex/cli.py`, `src/repocodex/mcp_server.py`, `src/repocodex/commands/write.py`, `src/repocodex/commands/bootstrap.py`, `src/repocodex/commands/context.py`, `src/repocodex/commands/validate.py`, `src/repocodex/commands/reconcile.py`, `src/repocodex/commands/relocate.py`, `src/repocodex/commands/audit.py`, `src/repocodex/commands/repair.py`, `src/repocodex/commands/advisory.py`, `src/repocodex/commands/install.py`).

The write path calls the gate for anchored concepts, writes accepted content, and regenerates indexes. The bundle implementation persists Markdown, catalogs and a log, and reloads typed concepts across discovered `.context` directories. Retrieval loads those concepts again and selects bodies by pinned paths, with related titles. These are shipped state producers and consumers, not hypothetical application code (SRC-1, `src/repocodex/commands/write.py`, `src/repocodex/engine/gate.py`, `src/repocodex/store/bundle.py`, `src/repocodex/store/reverse_index.py`, `src/repocodex/retrieval.py`).

> written = write_concept(repo, doc, context_root=shard)
> regenerate_all(repo)
> --- `src/repocodex/commands/write.py`

Packaged skills instruct agents to read, edit, write memory, validate and stage retained content. Installed rules point agents to those skills. The installer supplies the pre-commit hook, required and advisory Action jobs, skills and plugin tree. These integration artifacts are included because they initiate and enforce the memory loop. The engine repository's own test and publishing workflows are distinguished from the Action template installed in consuming repositories (SRC-1, `src/repocodex/data/skills/repocodex-coding/SKILL.md`, `src/repocodex/data/skills/repocodex-review/SKILL.md`, `src/repocodex/data/rules/claude/CLAUDE.md`, `src/repocodex/data/rules/cursor/repocodex.mdc`, `src/repocodex/commands/install.py`, `src/repocodex/data/hooks/pre-commit`, `src/repocodex/data/action/repocodex.yml`, `.github/workflows/engine-tests.yml`, `.github/workflows/publish.yml`).

### Top-level tracked coverage

“Included” fixes functional scope; it does not claim every file has already received a line-by-line audit. Initial inspection traced every shipped loop responsibility above. Available supporting internals and additional tests remain available to later analysts under SRC-1; they are not access gaps. No material shipped loop responsibility was excluded because it was inconvenient to inspect.

| Top-level tracked path | Treatment | Material paths, role and initial inspection | Limit or conclusion prevented |
| --- | --- | --- | --- |
| `.cursor/` | Excluded: engine-development workflow | `commands/opsx-*.md` and `skills/openspec-*/SKILL.md`; inspected the apply command and apply skill to identify OpenSpec change-implementation procedures. | No assessment of OpenSpec's development workflow or model behavior; these are not the RepoCodex skills installed into consuming repositories. |
| `.github/` | Included: development evaluation and distribution | Inspected `workflows/engine-tests.yml` and `workflows/publish.yml`: engine test invocation and package publication. | Source configuration only; no CI results or published-wheel equivalence established. |
| `.gitignore` | Included: evidence and packaging context | Inspected exclusions for local research, proposals, dependencies and telemetry. | Ignored local files are not part of this frozen tracked source set. |
| `AGENTS.md` | Included: contributor context | Inspected distinction between the engine repository and installed product, plus package layout. | Contributor instructions are evidence about development, not instructions governing this analysis. |
| `CONTRIBUTING.md` | Included: contributor context | Inspected test, specification and distribution guidance. | Does not establish tests passed. |
| `LICENSE` | Excluded: legal text | Tracked licensing artifact; no operational role used. | No legal analysis. |
| `README.md` | Included: product doctrine | Inspected intended retrieve/edit/write/check loop and installation surface. | Product claims require implementation support; no effectiveness result inferred. |
| `SECURITY.md` | Excluded: reporting policy | Tracked security-policy surface, not a state producer or consumer. | No security-policy or vulnerability-response assessment. |
| `docs/` | Included: product doctrine | Inspected `architecture.md`, `agents.md`, `memory.md`; `how-it-works.md` and `install.md` remain available supporting documentation, not yet inspected in this boundary job. | Documentation does not establish observed agent operation. |
| `googleaaee4c512b9e1474.html` | Excluded: site verification | Inspected single verification token. | No website-ownership conclusion or website analysis. |
| `hooks/` | Included: enforcement distribution | Inspected `pre-commit`, which invokes staged CLI validation and denies nonzero outcomes. | Hook source does not prove installation or enforcement in any real consuming repository. |
| `openspec/` | Included: declared behavior contracts | Inspected `config.yaml` and `specs/agent-interfaces/spec.md`; tree also identifies anchor verification, conformance, context retrieval, enforcement, governance, impact analysis, memory store and OKF conformance specs. Other specs remain available, not yet inspected here. | Normative requirements are not executable observations and may differ from implementation. |
| `package.json` | Included: development dependency context | Inspected OpenSpec dependency declaration. | Does not make the OpenSpec dependency's implementation part of RepoCodex. |
| `package-lock.json` | Excluded: dependency resolution detail | Tracked JavaScript lockfile; no operational claim depends on its contents. | No transitive JavaScript supply-chain assessment. |
| `plugin/` | Included: agent distribution | Inspected `plugin.json`, `mcp.json`, `hooks/claude-pre-commit`, `hooks/cursor-pre-commit`; coding/review skill paths identified. Installed counterparts are traced through the packaged data tree and installer. | No assertion that every client supports or actually loads the plugin; no assumption that root and packaged copies are byte-identical. |
| `pyproject.toml` | Included: package and entry contract | Inspected console script, Python requirements, optional MCP dependency and data packaging. | Declared dependencies do not pin their external behavior within this source boundary. |
| `src/` | Included: complete shipped functional system | Inspected `repocodex/__main__.py`, `cli.py`, every command module, `mcp_server.py`, `retrieval.py`, `store/bundle.py`, `store/reverse_index.py`, `engine/gate.py`, packaged coding/review skills, rules, hook, Action and plugin manifest. Tree and imports identify supporting `engine/` attestation/impact modules, `schema.py`, `config.py`, `metrics.py`, `tools/`, and remaining data copies; detailed internal analysis remains available. | Boundary inspection establishes coverage of state lifecycle and callers, not exhaustive correctness of every internal helper or distribution copy. |
| `tests/` | Included: source-defined evaluators | Inspected `test_e2e.py` and `test_retrieval.py`; searched `test_enforcement.py` for installed-hook and exemption cases. Tracked tree includes fixtures and command, engine, store, MCP, schema, sharding, first-touch and review-gap suites. | Tests are executable specifications, not observed runs; other test bodies have not yet been inspected here. |
| `uv.lock` | Excluded: dependency resolution detail | Tracked Python lockfile; runtime dependency contract inspected in `pyproject.toml`. | No transitive Python supply-chain or environment-reproduction assessment. |

### External dependencies and evidence limits

External coding/review agents, their models and harness internals are outside the source boundary. RepoCodex's shipped prompts, CLI invocation code and maintenance instructions remain inside it. This prevents attributing host scheduling, model quality, context limits or agent compliance to RepoCodex itself. The repair implementation passes a repair prompt to a harness and reports its process outcome; that is not evidence that retained knowledge was successfully repaired (SRC-1, `src/repocodex/commands/repair.py`).

Git, ripgrep, the Python runtime and dependencies, the optional MCP SDK, GitHub Actions services and consuming repositories are external dependencies. Their interfaces and shipped configuration are in scope, but their implementation sources and actual deployments are not registered. The external OKF specification linked by the product is not a second frozen source; this run can assess the repository's local schema and conformance claims, not independently certify conformance against an unacquired external revision (SRC-1, `pyproject.toml`, `docs/memory.md`, `src/repocodex/data/action/repocodex.yml`, `src/repocodex/mcp_server.py`).

No target execution, model call, test run, deployment trace or causal experiment was performed or supplied. Source-defined tests and instructions therefore support implementation and design analysis only. In particular, the included test named as an agent loop uses a no-hook commit and does not establish a production agent's successful loop (SRC-1, `tests/test_e2e.py`). The repository explicitly distinguishes itself from an application using its memory:

> This is not an application repo that *uses* RepoCodex. There is no `.context/` bundle here.
> --- `AGENTS.md`

Consequently, this boundary permits analysis of how the shipped system creates, maintains and consumes memory, but not conclusions about real retained-memory quality, long-term anti-regression benefit, latency distributions or autonomous repair success. These are evidence limits, not reasons to exclude the shipped loop.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/azaylamba/repocodex` | 96978e292fcb3b100f53ac024b353e1b8b2c8af4 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/repocodex-7a5aff40a82e/related-systems/azaylamba--repocodex`. Implementation: full tracked tree; CLI and module entry; all `src/repocodex/commands/` implementations; MCP wrappers; retrieval; bundle and reverse-index stores; write gate; installer and packaged skill/rule/hook/Action surfaces; root plugin metadata/adapters; root hook; selected test source and CI workflows as evaluators. Doctrine/design: README, architecture, memory, agent playbook, contributor docs, agent-interface spec, packaged coding/review procedures; development OpenSpec apply procedures inspected for exclusion. The coverage table distinguishes inspection from available supporting files. | Implementation: [CLI](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/src/repocodex/cli.py), [persistence](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/src/repocodex/store/bundle.py), [retrieval](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/src/repocodex/retrieval.py), [installer](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/src/repocodex/commands/install.py), [repair driver](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/src/repocodex/commands/repair.py). Doctrine/design: [coding skill](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/src/repocodex/data/skills/repocodex-coding/SKILL.md), [architecture](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/docs/architecture.md), [interface specification](https://github.com/azaylamba/repocodex/blob/96978e292fcb3b100f53ac024b353e1b8b2c8af4/openspec/specs/agent-interfaces/spec.md). | No source-access failure encountered. No observed-run or causal-experiment layer supplied. Excluded external hosts, dependencies and consuming deployments prevent claims about their behavior; source tests do not establish execution results. |
