---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "LLM Wiki's shipped knowledge-maintenance instructions, Markdown scaffold and CLI/MCP toolkit at commit a424e6875aa2d5736d9c0d03d7c28bdbe32892a5."
run-id: AAS-2026-10-14-llm-wiki-b437987c5802-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/cobusgreyling/llm-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-b437987c5802/related-systems/cobusgreyling--llm-wiki
  revision: a424e6875aa2d5736d9c0d03d7c28bdbe32892a5
  sha256: null
---

# llm-wiki boundary

## Boundary and evidence

This run examines LLM Wiki as a knowledge-maintenance system: human-curated raw sources, agent-maintained persistent Markdown, maintenance and query instructions, and the toolkit that scaffolds, inspects and retrieves that state. It includes the shipped instructions that assign model-dependent work to an external agent, not just the Python library or MCP tools. The intended use is to establish how this repository specifies and supports producing, maintaining and later consuming a wiki. SRC-1: `README.md`, `docs/ARCHITECTURE.md`, `AGENTS.md`, `src/llm_wiki/scaffold/AGENTS.md`.

The target class is **memory/knowledge/context-engineering system**, rather than an enclosing agent runtime. Its own architecture distinguishes the toolkit from the generated wiki and assigns content writing to an agent:

> | This repo (`llm-wiki`) | Your project (`wiki init`) |
> |------------------------|----------------------------|
> | Python package under `src/llm_wiki/` | Markdown wiki at project root |
> | CLI + MCP for read/lint/scaffold | Agent writes all `wiki/` pages |
> | Examples under `examples/` | Your `raw/` and `wiki/` |
> --- `docs/ARCHITECTURE.md`

The **whole-system** boundary covers this shipped system, including its delegated maintenance protocol. It does not mean that an external agent's execution loop is implemented here. The producer is specified in the bundled maintainer prompt; toolkit creation paths implement project and page scaffolding. The protocol includes index, synthesis, contradiction and log updates. Reload and later consumption are specified in the query instructions and implemented by CLI/MCP search and expansion. SRC-1: `src/llm_wiki/bootstrap.py`, `src/llm_wiki/new_page.py`, `src/llm_wiki/cli.py`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/scaffold/AGENTS.md`.

> 1. **Read** `wiki/index.md` first to locate relevant pages.
> 2. **Search** with `wiki search "<query>"` or the `wiki_search` MCP tool if available.
> 3. **Read** the most relevant pages (use `wiki expand <page> --section "Heading"` to load one section at a time).
> 4. **Synthesize** an answer with wikilinks and citations to source pages.
> 5. **Offer** to file the answer: valuable analyses should become `wiki/answers/<slug>.md`.
> --- `src/llm_wiki/scaffold/AGENTS.md`

Health inspection and raw-to-source coverage belong to the target. Semantic correction and integration belong to its agent-facing instructions, not to the status checker or watcher. The shipped watch caller reports pending sources; it does not itself perform a model-driven ingest. SRC-1: `src/llm_wiki/lint.py`, `src/llm_wiki/ingest.py`, `src/llm_wiki/watch.py`, `src/llm_wiki/cli.py`, `scripts/ingest-checklist.sh`.

> pending = [s.raw_file for s in statuses if s.status == "pending"]
> new_pending = [f for f in pending if f not in seen_pending]
>
> if new_pending:
>     for raw_file in new_pending:
>         message = f"New raw file pending ingest: raw/{raw_file}"
>         if on_pending:
>             on_pending(message, raw_file)
>         else:
>             print(message)
>     seen_pending.update(new_pending)
> --- `src/llm_wiki/watch.py`

### Frozen evidence and limits

The evidence is the single acquired Git repository at **a424e6875aa2d5736d9c0d03d7c28bdbe32892a5**, with applicability cutoff **2026-10-14**, the supplied run date. HEAD matched the acquisition pin and the checkout had no reported working-tree changes at inspection. No other repository, live documentation, release or external reference is evidence for this run. The overall tier is **code-grounded** for toolkit behavior; the model's maintenance and answer-writing behavior remains **doctrine/design** unless independently supported by execution evidence within this commit.

External dependencies are the agent host and its model, Python package dependencies, optional FastMCP, optional qmd, and optional human-facing Obsidian/Dataview/Marp integrations. The shipped CLI entry point, MCP server, host configuration files and integration instructions are included; the implementations of those external systems are not. This prevents conclusions about host prompt loading, model compliance, autonomous scheduling, qmd's internal retrieval algorithm, or actual editor behavior. The repository's qmd subprocess adapter remains included. SRC-1: `pyproject.toml`, `src/llm_wiki/mcp_server.py`, `src/llm_wiki/search.py`, `src/llm_wiki/scaffold/.mcp.json`, `src/llm_wiki/scaffold/.cursor/mcp.json`, `src/llm_wiki/scaffold/.windsurf/mcp.json`, `src/llm_wiki/scaffold/.opencode/mcp.json`, `docs/OBSIDIAN.md`.

Source tests and CI definitions support what is checked, not a claim that tests passed or that the model-maintained loop works in deployment. Populated example pages and their logs are shipped examples with reported operations, not authenticated agent execution traces or causal experiments. No target execution was performed. These limits prevent claims about answer quality, maintenance reliability, measured compounding benefit or comparative performance. SRC-1: `tests/test_ingest.py`, `tests/test_mcp.py`, `tests/test_lint_fixtures.py`, `.github/workflows/ci.yml`, `examples/demo/wiki/log.md`, `examples/demo/wiki/answers/llm-wiki-vs-rag.md`.

### Top-level coverage

All rows refer to SRC-1. “Not yet inspected” means available evidence, not an access gap. Included directories remain within the registered repository boundary beyond the initial inspection. Deliberate exclusions below concern packaging administration or presentation, not a missing producer or consumer of wiki state.

| Top-level tracked entry | Included or excluded | Material paths, role and initial inspection | Limit or conclusion prevented |
|---|---|---|---|
| `.github/` | Included for evaluation/integration; excluded for release and issue administration | Inspected `.github/workflows/ci.yml`: tests, prompt sync, example lint, demo caller and scaffold/build checks. `.github/mcp.json.example` not yet inspected. Issue templates and publish workflow deliberately excluded. | No verified CI result, release provenance or claim about the uninspected example config. |
| `.gitignore` | Excluded | Repository hygiene; not inspected. | No conclusion about ignored local state or accidental retention. |
| `.pre-commit-config.yaml` | Excluded | Development hooks; not inspected. | No conclusion about developer-side hook enforcement. |
| `AGENTS.md` | Included | Read in full: canonical schema and ingest/query/lint instructions. Byte hashes matched the scaffold and all four example copies. | Instructions establish prescribed behavior, not compliance. |
| `CHANGELOG.md` | Excluded | Historical release narrative; not inspected. | No version-history or migration claims. |
| `CONTRIBUTING.md` | Excluded | Contributor process; not inspected. | No governance or contribution-process claims. |
| `LAUNCH.md` | Excluded | Announcement material; not inspected. | No launch, adoption or publicity claims. |
| `LICENSE` | Excluded | Legal terms; not inspected. | No independent licensing assessment. |
| `MAINTAINERS.md` | Excluded | Release administration; not inspected. | No publishing or maintainer-process assessment. |
| `Makefile` | Included | Read in full: demo state consumers, lint/test shortcuts and instruction synchronization caller. | Static caller evidence, not execution results. |
| `README.md` | Included | Read in full: purpose, host handoff, source ingestion and CLI/MCP usage. | Marketing comparisons are declared claims, not measured findings. |
| `assets/` | Excluded | Header image, diagram SVGs and `assets/demo.cast`; tree inspected, contents not inspected. | No inference from diagrams or terminal recording, including no observed-run claim based on the cast. |
| `docs/` | Included for operating documentation; excluded for launch/presentation | Read `docs/ARCHITECTURE.md`, `docs/MCP.md`, `docs/LINT.md`, `docs/OBSIDIAN.md`. `docs/DEMO.md` and the two launch documents deliberately excluded. | No recording-production, outreach or external integration execution claims. |
| `examples/` | Included | All four domain trees inventoried, instruction copies checked against canonical text, README/log headings searched. Read demo index, log, synthesis, contradictions, source page `examples/demo/wiki/sources/karpathy-llm-wiki-gist.md` and filed answer `examples/demo/wiki/answers/llm-wiki-vs-rag.md`. Includes all shipped `raw/` and `wiki/` content for demo, business, reading and research. Remaining corpus pages not yet inspected. | Illustrative state and attributed operation only; no exhaustive corpus-quality judgment or measured agent success. |
| `pyproject.toml` | Included | Read in full: `wiki` entry point, dependencies, bundled scaffold and test/coverage configuration. | Configuration does not establish successful installation or test coverage. |
| `scripts/` | Included | Read all five scripts: bootstrap wrapper, two demo drivers consuming retained wiki pages, post-ingest checklist and canonical prompt synchronization. | Drivers are shipped callers, not excluded external applications; no execution claim. |
| `src/` | Included | Read `src/llm_wiki/cli.py`, `mcp_server.py`, `bootstrap.py`, `new_page.py`, `paths.py`, `search.py`, `expand.py`, `links.py`, `ingest.py`, `watch.py`, `lint.py`, `stats.py`; paths here are under `src/llm_wiki/`. Read bundled `scaffold/AGENTS.md`, `scaffold/CLAUDE.md`, four MCP configs, source and answer templates. Scaffold tree inventoried; concept/entity templates searched. Remaining scaffold seed pages and package marker files not yet inspected. | Covers project/page persistence, source coverage, structural inspection and retrieval/expansion consumers. Remaining seed details do not establish uninspected content quality. No model execution claim. |
| `tests/` | Included | Test definitions searched across all tracked test modules; read `tests/test_ingest.py`, `tests/test_mcp.py`, `tests/test_lint_fixtures.py`. Includes CLI, scaffolding, retrieval, lint, graph/path safety, watcher and prompt-sync tests. Remaining test bodies not yet inspected. | No assertion that tests ran, passed, comprehensively evaluate semantic quality or demonstrate causal improvement. |

No material shipped path needed to establish this functional boundary was unavailable. The initial inspection traced the shipped CLI and MCP entry points through their state-producing, inspecting and consuming helpers, and traced shell/Makefile callers and scaffold instructions. Later analysts may inspect further files at this same pin; the initial coverage is not an allowlist.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/cobusgreyling/llm-wiki` | a424e6875aa2d5736d9c0d03d7c28bdbe32892a5 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-b437987c5802/related-systems/cobusgreyling--llm-wiki`. Implementation: CLI/MCP entry points and all functional helper modules named in coverage; scripts, Makefile, CI and sampled test bodies. Doctrine/design: README, architecture/MCP/lint/Obsidian docs, canonical/bundled maintainer prompt, Claude handoff, host configs and sampled templates. Reported operation: demo log and illustrative compiled wiki pages. Complete tracked tree inspected; additional example/test paths searched as specified above. | Implementation: [CLI](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/cli.py), [MCP](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/mcp_server.py), [scaffolding](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/bootstrap.py), [lint](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/lint.py). Doctrine/design: [shipped prompt](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/src/llm_wiki/scaffold/AGENTS.md), [architecture](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/docs/ARCHITECTURE.md). Reported operation: [example log](https://github.com/cobusgreyling/llm-wiki/blob/a424e6875aa2d5736d9c0d03d7c28bdbe32892a5/examples/demo/wiki/log.md). | No checkout access gap found. External host/model/qmd/editor implementations are outside the frozen source. Uninspected available files are marked in coverage, not missing evidence. Tests were not executed; example logs are not authenticated traces. Prevents deployment, compliance, quality, performance and causal-effect conclusions. |
