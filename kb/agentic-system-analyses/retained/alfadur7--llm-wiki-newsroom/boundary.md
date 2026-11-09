---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llm-wiki-newsroom's shipped knowledge-maintenance and consumption system at commit 8e209cab483da544852d7213f0e25291d06d8a88."
run-id: AAS-2026-11-08-llm-wiki-newsroom-ea04687a5ff6-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 8e209cab483da544852d7213f0e25291d06d8a88
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/alfadur7/llm-wiki-newsroom
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-newsroom-ded445f4e371/related-systems/alfadur7--llm-wiki-newsroom
  revision: 8e209cab483da544852d7213f0e25291d06d8a88
  sha256: null
---

# llm-wiki-newsroom boundary

## Boundary and evidence

This run examines the shipped, agent-operated wiki system: how documents become retained knowledge, how that knowledge is checked and maintained, and how later agents and readers consume it. The target class is **memory/knowledge/context-engineering system**, not an independently implemented enclosing agent runtime. Its model-dependent work is expressed through role prompts and command procedures served to an external coding-agent host. Its deterministic Python tools and browser are part of the same product, not excluded callers. The boundary kind is **whole-system**: it includes the shipped production, admission, maintenance, improvement, retrieval and export paths. [SRC-1: `CLAUDE.md`, `.claude/agents/editor-in-chief.md`, `.claude/commands/wiki-ingest.md`, `.claude/commands/wiki-query.md`, `tools/build.py`, `tools/query.py`, `tools/export.py`]

The distinction between the system and its host is explicit in its own entry instructions:

> When the user makes a request in natural language or runs a slash command, these instructions route the work to the appropriate one of the five roles.
> --- `CLAUDE.md`

The shipped ingest caller directs persistent writes and subsequent maintenance; it is not merely documentation for an isolated library API:

> **Cascade update** — add sources + strengthen facts on existing hubs linked in the source's `## Connections`; bump `last_updated` only where the body changed ([`layers/hub.md`](../layers/hub.md)). On bulk ingest, this may be skipped and post-processed by lint.
> --- `.claude/commands/wiki-ingest.md`

The consumption side is also shipped. The query command reloads retained pages, synthesizes answers and optionally routes a new retained synthesis through verification. The graph CLI loads persisted JSON; the browser fetches graph, cluster and overlay files; export creates a separate knowledge bundle with its own consumer instructions. These belong inside the functional boundary even though Claude.ai, QMD and the web browser are external dependencies. [SRC-1: `.claude/commands/wiki-query.md`, `tools/_query/graph.py`, `graph/graph.html`, `tools/export.py`, `wiki-export/README.md`]

> Search results (snippets·docids) are **only a lead** — pull the body via `mcp__qmd__get`/`multi_get` for facts·quotes·nuance before answering. Read the top ≤10 pages
> --- `.claude/commands/wiki-query.md`

The immutable evidence identity is repository `https://github.com/alfadur7/llm-wiki-newsroom` at **8e209cab483da544852d7213f0e25291d06d8a88**. The acquired checkout's HEAD was checked against that revision. The applicability cutoff is **2026-11-08**; later commits, live deployments and linked external articles are not evidence for this run. The overall evidence tier is **code-grounded**, with role and workflow intent separately treated as doctrine/design. No target code, tests, examples, model calls or services were executed. Source inspection does not establish successful operation or effectiveness.

### Tracked-root coverage

All rows refer to SRC-1 at the frozen commit. Included directories remain available for deeper source tracing; the initial inspection was structural and responsibility-oriented, not a claim that every file or every data record was read. Uninspected detail is not an access gap. No material shipped responsibility was deliberately excluded.

| Top-level tracked path | Treatment | Material paths and role; initial inspection and limits |
|---|---|---|
| `.claude/` | Included | `agents/{editor-in-chief,reporter,columnist,desk}.md` establish orchestration, authoring and review roles; `commands/README.md`, `wiki-ingest.md`, `wiki-query.md`, `wiki-lint.md` trace entry, persistence, retrieval, admission and repair. `layers/README.md` identifies source, hub, overview, contradiction, synthesis, timeline and trail contracts; the corresponding layer files, `_manifest.json` and `skills/*/{SKILL.md,criteria.json,checks.py}` remain included as authoring and evaluation machinery. `settings.json` wires `hooks/dispatch.sh`, `dispatch.py` and `lint-chain-guard.sh`; dispatcher source was sampled. `operations/{staleness-reground-runbook,bundle-reground-runbook}.md` cover post-publication maintenance; proposal validation and other operation runbooks are included. `policies/` governs layout and conventions. `memory/` and `operations/` include placeholder files, but local memory contents are not supplied; see access limits below. |
| `CLAUDE.md` | Included | Primary natural-language entry, role routing, four feedback scopes, instruction locations and human gates. Initial entry and routing sections inspected, together with its role and command consumers. |
| `AGENTS.md` | Included | Shipped alternate-host workflow: ingest writes sources, rebuilds, updates hubs and logs; query rereads retained pages. Explicitly marked legacy compatibility mode. This path is not excluded merely because Claude Code is primary. |
| `GEMINI.md` | Included | Alternate-host instructions, likewise marked legacy, with ingest/query/lint/build responsibilities. Does not establish parity with the richer Claude procedures. |
| `README.md` | Included | Product purpose, installation and host support, feature and command descriptions. Initial sections inspected as declared design and attributed operation, not proof of reliability or private-deployment performance. |
| `tools/` | Included | `build.py` dispatches graph → clusters → contradictions → index → dependencies. `_build/index.py` constructs and writes URL/path dedup state; `_build/dependencies.py` supplies maintenance dependencies. `lint.py` dispatches content and structural checks to `_lint/`; `log_defect.py`, `mine_failures.py`, `mine_feedback.py`, `_review.py`, `_defect-log.jsonl` and `regression_set.json` belong to the improvement/evaluation plane. `query.py` and `_query/{graph,qmd}.py` consume retained state or invoke external search. `_ingest/{fetch_inbox,fetch_article,prefilter_ingest,suggest_links,suggest_tags}.py` and `_news/` acquire and prefilter inputs; inbox and crawl entry descriptions inspected. `discover.py`/`_discover/` rank connections. `export.py`/`_export/` produce consumer bundles; `send_briefing.py`/`_briefing/` consume retained briefings for email. Shared `_lib.py` and `_net.py`, mention/count/list helpers, `patch_obsidian_qmd.py` and `show_workflow.py` remain included support paths. Initial inspection traced dispatcher imports, persistence writes, retrieval reads and external invocation, not every checker branch or ledger item. |
| `raw/` | Included, with unavailable originals | `_inbox.md` is the multi-channel URL queue; `_archive.md` records outcomes; `.gitkeep` preserves the source area. Queue instructions and fetch consumer inspected. Original scraped documents under raw subdirectories are not shipped in the tracked tree. The missing originals prevent full independent source-to-wiki fidelity assessment; retained wiki summaries are not substitutes for them. |
| `wiki/` | Included | `sources/` retains source pages, catalogs and `_source_map.json`; `entities/`, `concepts/`, `overviews/`, `contradictions/`, `syntheses/`, `timelines/`, `trails/`, root index/overview/contradiction and `_backlinks.json` are persistent system state. Initial inspection sampled `index.md` and `sources/deepseek-r1-release.md`, then traced index-map writing and later query consumption. The corpus is an example artifact, not a complete history of production operations. |
| `graph/` | Included | `_graph.json`, `_clusters.json`, `_dependencies.json`, `_overlays.json`, `cluster_labels.json` and `graph.html` cover derived state, operator labels and browser consumption. Browser fetch code and build/query consumers inspected. The ignored `_pages.json` body bundle is regenerable but not shipped; its absence prevents inspecting that exact generated reading-pane payload, not inspecting its producer/consumer code. |
| `wiki-export/` | Included | `README.md` supplies downstream project instructions; root copies and `all-*.md` bundles are retained consumer artifacts. Export producer and consumer instructions inspected. The boundary includes possible differences between exported instructions and local behavior; it does not presume synchronized exports or successful hosted retrieval. |
| `docs/` | Included | Public design/usage material, English and Korean pages, FAQ data, site configuration/layout/assets and illustration. `experiments/judge-model-2026-09/` includes preregistration, freeze manifests, labeler prompt, labels, scores, page features and `analyze.py`; its README was inspected to establish evaluation scope and missing inputs. These records are available for later evidence tracing, not independently verified results at boundary declaration. |
| `tests/` | Included | Regression suite covering tools, hooks, permissions, ingest, staleness and improvement infrastructure. Initial tree inventory and `test_defect_loop.py` sample inspected; tests count as executable assertions, not observed passing runs. |
| `log.md` | Included | Append-only operational record used by the ingest and orchestration instructions. Initially located and traced through its writers, not audited entry by entry; entries require individual inspection before supporting operation claims. |
| `requirements.txt` | Included | Python dependencies for graph/network processing, fetching, email rendering and tests; includes optional Leiden-related packages and fallback explanation. Dependency declarations inspected, not installed or exercised. |
| `.gitignore` | Included | Establishes omitted raw originals, local settings, `.mcp.json`, local memory, review watermarks, body bundles, health logs and deployment staging. Inspected to distinguish unavailable local evidence from deliberate analytical exclusion. |
| `.editorconfig`, `.gitattributes` | Excluded from functional analysis | Repository text/format configuration, located in tracked-tree inventory. No conclusion about cross-platform byte/line-ending behavior is supported by excluding their contents. |
| `LICENSE` | Excluded from functional analysis | Licensing metadata, located in tracked-tree inventory. No legal or licensing conclusion is made. |

### External dependencies and evidence limits

The external coding-agent host supplies model execution, tool access, context handling and agent invocation. Its implementation, provider behavior and host-specific enforcement are outside this repository source boundary; the role prompts and hook configuration inside the repository remain included. This prevents attributing the host's scheduling, isolation, permission semantics or model quality to the target. The alternate Codex/Gemini instructions are included without importing those hosts' implementations. [SRC-1: `README.md`, `AGENTS.md`, `GEMINI.md`, `.claude/settings.json`, `.claude/agents/editor-in-chief.md`]

QMD's installed binary and MCP service, Claude.ai's ingestion/retrieval internals, SMTP/Gmail, source websites and hosting infrastructure are external. The shipped wrappers, export instructions, email dispatcher and setup procedures remain included. There is no source basis here for end-to-end availability, hosted retrieval quality, mail delivery or external crawler success. [SRC-1: `tools/_query/qmd.py`, `wiki-export/README.md`, `tools/send_briefing.py`, `tools/_news/crawl.py`, `requirements.txt`]

Private raw documents, machine-local memory/settings, transcripts, review watermarks and generated local artifacts excluded by `.gitignore` are unavailable evidence, not paths intentionally removed from the system's functional scope. Their absence prevents reconstructing a deployment's full history, its exact context and original-document grounding. Private-deployment figures in the README remain attributed reports. [SRC-1: `.gitignore`, `README.md`, `tools/mine_feedback.py`]

The shipped judge-model experiment has inspectable labels, scores and analysis artifacts, but its README says the scorer and question wording are unpublished and private-corpus figures are not reproducible from the directory. Those limits prevent full scoring replication and independent assessment of the hidden judge prompt; they do not erase the supplied public experiment artifacts. No causal conclusion is established by registering them. [SRC-1: `docs/experiments/judge-model-2026-09/README.md`]

## Source register

| Source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alfadur7/llm-wiki-newsroom` | 8e209cab483da544852d7213f0e25291d06d8a88 | implementation; doctrine/design; reported operation; observed run | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llm-wiki-newsroom-ded445f4e371/related-systems/alfadur7--llm-wiki-newsroom`. Implementation: tracked-tree inventory, build/index persistence, graph/query reload, QMD invocation, browser fetch and hook dispatcher samples; tool and test entry points named above. Doctrine/design: primary and alternate host instructions, command routing/ingest/query/lint, role and layer contracts, reground runbooks, export consumer instructions. Reported operation: README deployment claims and experiment README's account. Observed run: shipped experiment labels/scores/manifests are registered as inspectable run artifacts, initially identified through their README and tree, not yet examined record by record. No target execution or causal experiment was performed by this analysis. | Implementation: [index persistence](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/tools/_build/index.py), [query graph](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/tools/_query/graph.py), [browser](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/graph/graph.html). Doctrine/design: [entry instructions](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/CLAUDE.md), [ingest](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/.claude/commands/wiki-ingest.md), [query](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/.claude/commands/wiki-query.md). Reported operation: [README](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/README.md). Run-artifact scope: [experiment inventory and limitations](https://github.com/alfadur7/llm-wiki-newsroom/blob/8e209cab483da544852d7213f0e25291d06d8a88/docs/experiments/judge-model-2026-09/README.md). | Frozen repository is available. Unavailable private originals/local context prevent full source-fidelity and deployment-history reconstruction. External hosts/services prevent conclusions about their internals. Missing judge wording/scorer prevents full experiment replication. Initially uninspected files are available for later inspection at this same commit, not access gaps. |
