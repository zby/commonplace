---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Synthadoc's shipped knowledge compilation, maintenance and consumption system at Git revision b80d9388a3013e8051baf2854c7250942c46e91a."
run-id: AAS-2026-10-15-synthadoc-a3cae9152fff-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: b80d9388a3013e8051baf2854c7250942c46e91a
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/axoviq-ai/synthadoc
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/synthadoc-a3cae9152fff/related-systems/axoviq-ai--synthadoc
  revision: b80d9388a3013e8051baf2854c7250942c46e91a
  sha256: null
---

# Synthadoc boundary

## Boundary and evidence

This run covers Synthadoc as a shipped knowledge system, not merely its Python library or MCP interface. Its intended use is to turn source documents into a persistent Markdown wiki, maintain that wiki and supply retained content to subsequent questions and external model consumers. The target is in scope because its own model calls decide how source material becomes retained pages, synthesize answers from those pages and participate in maintenance. The target class is **memory/knowledge/context-engineering system**; the boundary kind is **whole-system**. This classification does not imply that Synthadoc supplies every responsibility of an external coding agent or editor (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/agents/query_agent.py`, `synthadoc/integration/mcp_server.py`).

The source describes its purpose as follows. This is declared intent, not evidence that every ingest produces correct knowledge (SRC-1, `synthadoc/knowledge/synthadoc-overview.md`):

> **Synthadoc** is an open-source, domain-agnostic LLM wiki engine (Community Edition, AGPL-3.0). It reads your raw source documents — PDFs, spreadsheets, Word files, presentations, images, web pages, YouTube videos, plain text — and uses an LLM to compile them into a persistent, structured wiki of Markdown files stored locally on your machine.
> --- `synthadoc/knowledge/synthadoc-overview.md`

### Functional coverage and entry-point trace

The executable entry point is `synthadoc.cli.main:app`, declared in `pyproject.toml`. Its command registrations include installation, ingest, query, lint, serve, scheduling, candidates, context, lifecycle, export, backup and workflows. The HTTP server constructs an `Orchestrator`, initializes its stores and launches a queue worker, scheduler and sensitive-data scan loop. The worker dispatches ingest, lint, scaffold and faithfulness jobs. MCP is mounted against that same orchestrator when enabled. These are shipped drivers inside the boundary, not excluded hosts (SRC-1, `pyproject.toml`, `synthadoc/cli/main.py`, `synthadoc/integration/http_server.py`).

The retained-state loop includes:

- **Produce and retain:** source analysis and decision prompts, model calls, create/update/flag handling, provenance, Markdown persistence, index and routing updates. The create path can write to `wiki/candidates/` under the staging policy rather than the live wiki (SRC-1, `synthadoc/agents/ingest_agent.py`, `synthadoc/storage/wiki.py`).
- **Admit and maintain:** candidate promotion/discard handlers, lifecycle transitions and snapshots, lint and adversarial checks, repair workflows, re-ingest, scheduled operations, audit, cache invalidation and sensitive-data retraction. These remain in scope even when they are optional or user-triggered (SRC-1, `synthadoc/integration/http_server.py`, `synthadoc/agents/lint_agent.py`, `synthadoc/agents/workflows/_loop.py`, `synthadoc/core/scheduler.py`).
- **Reload and consume:** `WikiStorage.read_page` parses persisted Markdown and frontmatter. Query retrieves wiki context and calls its provider to synthesize an answer. Context packs retrieve and budget page excerpts; MCP exposes those packs and direct page/search tools. Export reads retained pages and emits multiple formats, including OKF. The shipped OKF consumer reloads an exported bundle, constructs context and calls a provider. That consumer belongs to the evidence boundary despite residing under tests (SRC-1, `synthadoc/storage/wiki.py`, `synthadoc/agents/query_agent.py`, `synthadoc/agents/context_agent.py`, `synthadoc/integration/mcp_server.py`, `synthadoc/core/export.py`, `tests/integration/okf_consumer_agent.py`).
- **Operate through supplied clients and instructions:** the Web UI reloads sessions and streams queries; the Obsidian client invokes ingest, query, lint and state-management endpoints. Wiki initialization writes `AGENTS.md`, `CLAUDE.md` and `GEMINI.md`; shipped demos include instructions for ingest, lint, staging and later consumption. Those prompts and maintenance instructions are part of the system, not merely incidental examples (SRC-1, `web-ui/src/api.ts`, `obsidian-plugin/src/api.ts`, `synthadoc/cli/_init.py`, `synthadoc/demos/history-of-computing/AGENTS.md`).

The maintenance plane includes an actual model-driven tool loop, not only a collection of returning API calls. Its implementation repeatedly calls a provider, parses tool requests and dispatches registered callables. This is a bounded implementation classification; no successful execution or safety guarantee follows from it (SRC-1, `synthadoc/agents/workflows/_loop.py`):

> while True:
>         response = await provider.complete(messages, system=system_prompt, max_tokens=max_tokens)
>         text = response.text.strip()
> --- `synthadoc/agents/workflows/_loop.py`

The exported-content consumer supplies a concrete later consumption path (SRC-1, `tests/integration/okf_consumer_agent.py`):

> concepts = load_bundle(bundle_dir, type_filter)
> --- `tests/integration/okf_consumer_agent.py`

> context = build_context(concepts)
> --- `tests/integration/okf_consumer_agent.py`

### Repository coverage

The tracked root tree was inspected at the frozen commit. “Included” fixes functional scope; it does not claim that every file has already received a complete semantic review. Initial inspection below distinguishes source reading/search from inventory-only material. All included paths remain available to later analysts under SRC-1. No material shipped responsibility was found to require an unavailable repository or an excluded in-repository driver.

| Top-level tracked path | Classification and role | Initial inspection and limits |
|---|---|---|
| `synthadoc/` | Included: complete Python package and packaged assets. Material paths are `cli/` entry points and instruction generation; `agents/` ingest, query, context, lint and action agents; `agents/workflows/` repair and tool loops; `core/` orchestration, routing, queue, cache, scheduling, hooks, export, backup and retraction; `storage/` wiki, search and audit; `providers/`, `skills/`, `config.py`, `observability/`; `knowledge/`, `templates/`, `demos/` and `data/`. | Read orchestrator construction and ingestion entry; storage read/write; ingest prompts and create/staging path; query synthesis; lint resolution; workflow loop; context and export; scheduler execution; HTTP worker/startup and MCP tools; wiki initialization, overview and demo instructions. Searched action dispatch, candidate/lifecycle handlers, template installation and search/queue/provider interfaces. Skills, provider internals, remaining templates/demos, backup and packaged bundles are inventoried, not comprehensively inspected at this boundary stage; they are not excluded or inaccessible. |
| `obsidian-plugin/` | Included: shipped editor client, graph/source presentation, build and tests. Material paths include `src/main.ts`, `src/api.ts`, `src/sse.ts`, `src/graph-modal.ts` and corresponding tests. | Read API transport and query/ingest/lint calls; remaining UI and tests inventoried. The Obsidian host implementation itself is external. |
| `web-ui/` | Included: shipped browser client and client-side tests. Material paths include `src/App.tsx`, `src/api.ts`, session/query hooks, chat and confirmation components, and build configuration. | Read API session reload and streaming-query transport; confirmation event handling searched; remaining components inventoried. |
| `tests/` | Included: executable contracts, live/performance evaluators and the exported-bundle consumer. Material paths include `agents/`, `core/`, `storage/`, `integration/`, `live/`, `performance/`, `security/`, `providers/`, `skills/` and CLI tests. | Read `integration/okf_consumer_agent.py` bundle-to-model path; searched `integration/test_lifecycle_snapshots.py` assertions; inventoried subsystem and live evaluator paths. No tests or evaluators executed; presence is not a passing result. |
| `docs/` | Included: design, deployment and user contracts, examples and evaluations. Material paths include `design.md`, `user-quick-start-guide.md`, `docker-deploy.md`, `example/aquaflow/evaluation/`, raw example sources, media and screenshots. | Read evaluation runner's API call and fact-scoring code in `example/aquaflow/evaluation/scripts/eval_queries.py`; remaining documentation and benchmark report inventoried. No benchmark outcome is adopted here. |
| `hooks/` | Included: operational hook example and contract, especially `README.md` and `git-auto-commit.py`. | Read hook README; inventoried auto-commit script. The hook is part of the shipped maintenance surface; arbitrary user hook programs are not frozen evidence. |
| `docker/` | Included: deployment drivers in `compose/single-wiki.yml`, `compose/multi-wiki.yml`, `compose/with-ollama.yml`, and `examples/github-actions-ingest.yml`. | Inventoried; not yet inspected in detail. No container deployment was run. |
| `Dockerfile` | Included: packaged server entry point and deployment contract. | Read complete file; starts `synthadoc serve` with HTTP, MCP and Web UI as its stated default. Does not establish a working deployed image. |
| `pyproject.toml` | Included: console entry point, dependencies, package and test configuration. | Read project, script, test and build declarations. |
| `README.md`, `README-pypi.md` | Included: public usage and capability declarations. | Inventoried; not yet read for substantive claims. The inspected packaged overview supplies the intent statement used here. |
| `scripts/` | Included: build/asset synchronization and seed maintenance support. Material files include `sync_plugin.py`, `sync_web_ui.py`, `refresh_search_seeds.py`, `validate_seeds.py`, version/readme/badge helpers and `_url_quality.py`. | Inventoried only; not a separate runtime or an excluded state driver. No claim of synchronized bundle/source equivalence or validated seeds. |
| `VERSION` | Included: release identifier input. | Inventoried; the full Git commit, not the release label, is the evidence pin. |
| `skills-lock.json` | Included: repository skill dependency metadata. | Inventoried only; does not import external skill contents into the frozen evidence set. |
| `wiki/` | Included: tracked `wiki/log.md` repository artifact. | Inventoried, not read; no production operation inferred from its existence. |
| `.github/` | Excluded: CI and publication workflows (`workflows/ci.yml`, `docker-publish.yml`, `publish.yml`). | Deliberate exclusion from operational mechanism assessment; prevents claims about release-pipeline correctness or CI execution results. |
| `.dockerignore`, `.gitattributes`, `.gitignore` | Excluded: repository/build filtering and Git housekeeping. | Inventoried; prevents a claim that packaging exclusions or cross-platform checkout transformations have been audited. |
| `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `LICENSE` | Excluded: governance, contribution and licensing text. | Inventoried; no legal or contributor-process assessment. |

### Frozen evidence and external limits

The sole source is the acquired Git repository at **b80d9388a3013e8051baf2854c7250942c46e91a**, verified as the checkout HEAD with no reported worktree changes. The analysis cutoff is **2026-10-15**, the opening's run date. This cutoff fixes applicability; it is not a claim about releases after the pinned commit. The overall evidence tier is **code-grounded**. Source text and executable contracts establish inspectable mechanisms; target-authored help is doctrine/design. No target commands, examples, tests, provider calls or services were executed.

External dependencies include model APIs and coding-tool providers, optional embedding infrastructure, content/search services, Python/JavaScript libraries, the browser, Obsidian and any caller using MCP or exported files. Their integration code is in scope; their implementations, live responses and enclosing agent policies are not. This prevents conclusions about provider reliability, actual model compliance, host instruction delivery, end-to-end deployment security or real-world knowledge quality. The shipped OKF consumer shows how this repository consumes exports, not how every external agent does so (SRC-1, `pyproject.toml`, `synthadoc/agents/action_agent.py`, `synthadoc/integration/mcp_server.py`, `tests/integration/okf_consumer_agent.py`).

There is no identified access gap in the acquired repository. Inventory-only files are unfinished inspection, not unavailable evidence. No external live corpus, production wiki, execution trace or intervention/comparison evidence was supplied or captured. Consequently this boundary supports source-grounded analysis of the complete shipped loop, not observed operational success, benchmark reproduction or causal effectiveness claims.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/axoviq-ai/synthadoc` | b80d9388a3013e8051baf2854c7250942c46e91a | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/synthadoc-a3cae9152fff/related-systems/axoviq-ai--synthadoc`. Implementation: tracked tree; console registration; orchestration and HTTP worker/startup; ingest, staging and persistence; query/context consumption; lint resolution and workflow loop; MCP; export and OKF consumer; scheduler; client API transports; evaluation scoring. Doctrine/design: packaged overview, hook README, generated and demo wiki instructions, build/deployment declarations. Coverage table distinguishes read/search from inventory-only paths. | Implementation: [entry point](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/pyproject.toml), [server](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/synthadoc/integration/http_server.py), [ingest](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/synthadoc/agents/ingest_agent.py), [storage](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/synthadoc/storage/wiki.py), [consumer](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/tests/integration/okf_consumer_agent.py). Doctrine/design: [overview](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/synthadoc/knowledge/synthadoc-overview.md), [wiki instructions](https://github.com/axoviq-ai/synthadoc/blob/b80d9388a3013e8051baf2854c7250942c46e91a/synthadoc/demos/history-of-computing/AGENTS.md). | No identified repository access gap. External provider/host implementation and production evidence are absent. Implementation supports source behavior, not successful execution; doctrine supports intent, not compliance. No observed-run or causal-experiment layer established. |
