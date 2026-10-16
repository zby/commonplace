---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "TheKnowledge's shipped knowledge gateway, agent instructions, state lifecycle and consumers at commit aca6e29e69c6a72b697b8178841d03e6296ee3fc."
run-id: AAS-2026-10-14-theknowledge-319a64927ee3-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: aca6e29e69c6a72b697b8178841d03e6296ee3fc
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/BadWally/TheKnowledge
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/theknowledge-319a64927ee3/related-systems/BadWally--TheKnowledge
  revision: aca6e29e69c6a72b697b8178841d03e6296ee3fc
  sha256: null
---

# TheKnowledge boundary

## Boundary and evidence

This run covers TheKnowledge as a personal knowledge system, not merely its Python library or MCP server. Its intended use is source ingestion, retained wiki authorship, maintenance, research synthesis and later grounding of human or agent answers. The target class is **memory/knowledge/context-engineering system**; the boundary kind is **whole-system**. The repository's shipped CLI, MCP tools, browser client, background drivers, model prompts and agent instructions belong to the target. SRC-1: `README.md`, `pyproject.toml`, `CLAUDE.md`.

> A personal knowledge base. Sources land as markdown + YAML on the local filesystem. Ranked retrieval (`wiki retrieve`) returns bounded, cited context blocks; queries return cited synthesis pages. NotebookLM artifacts file back to the same vault. Obsidian renders the citation graph.
> --- `README.md`

The frozen evidence is repository commit `aca6e29e69c6a72b697b8178841d03e6296ee3fc`, verified against the acquired checkout's HEAD. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim that the system operated on that date. Overall evidence is **code-grounded**: source text establishes shipped behavior; documentation establishes declared intent. No target execution, tests, provider calls or installation were performed. This boundary does not establish deployment, reliability, retrieval quality or successful live operation.

### Functional coverage and entry-point tracing

The initial inspection traced the package's `wiki` entry point into CLI handlers and operation modules; MCP deposit dispatch into the durable-intent path and CLI commit-worker into its drain driver; browser API calls into gateway operation endpoints; and watcher/scheduler entry points into ingestion and maintenance commands. These are included callers, not external enclosing applications. SRC-1: `pyproject.toml`, `src/gateway/cli.py`, `src/gateway/mcp_server.py`, `web/src/api.ts`, `src/gateway/web/routes/ops.py`, `src/gateway/watcher.py`, `src/gateway/scheduler.py`.

The state-producing loop includes converters, semantic filtering, authored plans and validation/application, plus research acquisition and NotebookLM synthesis. The ingest authoring path reloads existing pages, asks a plan client for structured updates, applies the plan and feeds failures back into repair prompts. The default plan client delegates model calls to the shipped Claude CLI wrapper. SRC-1: `src/gateway/ops/ingest.py`, `src/gateway/plan.py`, `src/gateway/research/orchestrator.py`, `src/gateway/ops/query.py`.

> source_text = _format_source_for_plan(front, body)
> existing_pages = _gather_existing_pages(domain, query=str(front.get("title", "")))
> --- `src/gateway/ops/ingest.py`

The separate deposit path is also included: an MCP tool calls `deposit`, while the shipped CLI driver constructs an embedding index and invokes `run_worker`; `drain_once` claims, renders and submits intents to `CommitGate`. This prevents mistaking a durable enqueue for a completed canonical write. The test source describes a deposit-to-commit-to-retrieve round trip, but it was read, not run. SRC-1: `src/gateway/mcp_server.py`, `src/gateway/ops/deposit.py`, `src/gateway/cli.py`, `src/gateway/ops/committer.py`, `tests/e2e/test_multiagent_flow.py`.

> from gateway.ops.deposit import deposit
>
> return _serialize(deposit(payload, identity, depends_on=depends_on))
> --- `src/gateway/mcp_server.py`

> idx = EmbeddingIndex()
> try:
>     run_worker(once=once, poll_interval=poll_interval, embedding_index=idx, sink=sink)
> --- `src/gateway/cli.py`

Later consumption is included, not left to an unspecified host: the index refresh scans retained markdown and reconciles derived rows; retrieval assembles ranked page sections; `answer` feeds that retained context into a model call; `query` files NotebookLM answers through `apply_plan`. SRC-1: `src/gateway/search_index.py`, `src/gateway/ops/retrieve.py`, `src/gateway/ops/answer.py`, `src/gateway/ops/query.py`.

> result = client.call_with_usage(
>     user_prompt=f"Question: {question}",
>     user_prompt_prefix=prefix,
>     system_prompt=_SYSTEM_PROMPT,
>     model=model or _DEFAULT_MODEL,
>     max_tokens=_DEFAULT_MAX_TOKENS,
> )
> --- `src/gateway/ops/answer.py`

Maintenance includes strict draft finalization, scheduled jobs, draft-closer automation and the six shipped agent skills. Session compaction/resumption hooks and their instructions are included as a distinct development-session memory path, not conflated with wiki content. Evaluators include both retrieval goldens and model-judged wiki-state evaluation. Inspection of evaluator source is not evidence that its reported scores or thresholds were achieved. SRC-1: `src/gateway/ops/finalize.py`, `src/gateway/agents/draft_closer.py`, `.knowledge/schedule.yaml`, `.claude/settings.json`, `.claude/hooks/precompact-snapshot.sh`, `.claude/hooks/session-start-reanchor.sh`, `.claude/skills/wiki-editorial-review/SKILL.md`, `src/gateway/evaluate/runner.py`, `src/gateway/evaluate/retrieval_eval.py`.

### Top-level tracked coverage

“Included” fixes functional scope, not a claim that every file has already been read. Initial inspection traced the material production, admission, maintenance and consumption paths above. Available files not yet read remain eligible SRC-1 evidence and are not access gaps. The table accounts for every tracked top-level file or directory.

| Tracked path | Classification | Material paths and role; initial inspection or limit |
|---|---|---|
| `.claude/` | Included | All six `skills/*/SKILL.md`, `settings.json` and both `hooks/*.sh` inspected: ingest, citation repair, research, domain creation, editorial review, draft finalization and session reanchoring. `scheduled_tasks.lock` inventoried, not yet inspected. |
| `.gitignore` | Included | Derived/local-state exclusions; inventoried, not yet read. No claim about the complete ignore policy. |
| `.knowledge/` | Included | `schedule.yaml` inspected; `policies/*/policy.yaml`, policy examples/versions, `agents/`, `eval/`, `retrieval.yaml`, contradictions, migration and batch reports inventoried. Configuration and retained evaluation state remain in scope; their individual records are not yet assessed. |
| `ARCHITECTURE.md` | Included | System design reference; not yet inspected. |
| `BUILD.md` | Included | Shipped milestone and design history; not yet inspected. |
| `CHANGELOG.md` | Included | Release history; not yet inspected. |
| `CLAUDE.md` | Included | Fully inspected agent control surface, retrieval ladder and session-state discipline. |
| `CONTRIBUTING.md` | Included | Contributor procedure; not yet inspected. |
| `GLOSSARY.md` | Included | Source-native terminology; not yet inspected. |
| `LICENSE` | Excluded | Licensing, not the operational state loop. No legal/licensing conclusions. |
| `MIGRATION.md` | Included | Declared migration workflow; not yet inspected. |
| `README.md` | Included | Fully inspected intended use, interfaces, integrations and layout. |
| `SESSION_TRANSCRIPT.md` | Included | Target-authored design-session narrative; not yet inspected. No observed-run status assigned to it. |
| `TUTORIAL.md` | Included | User workflow instructions; not yet inspected. |
| `WIKI.md` | Included | Schema, operation and editorial contracts; not yet inspected. README assertions are not substituted for implementation checks. |
| `docs/` | Included | `MCP_API.md`, `RUNBOOK.md`, `TESTING.md`, ADRs, session-state, plans, milestones, target-authored reviews and deployment/evaluation records inventoried, not yet inspected. These may support declared intent or attributed operation; they are not automatically trusted outcomes. Domain research/staging documents are retained payload, not authority on system effectiveness. |
| `index.md` | Included | Retained navigation surface; inventoried, not loaded wholesale. The default consumption path was inspected in retrieval/index code instead. |
| `log.md` | Included | Retained operation/event ledger; write and consumption responsibilities traced in code, log entries not yet inspected. No live-run conclusion from the ledger's presence. |
| `migrations/` | Included | `0001-import-legacy-vaults.py` through `0005-demote-source-pages.py`: legacy state import/schema maintenance; inventoried, not yet inspected. |
| `nlm/` | Included | `notebooks.yaml`, `query_plans/`, `source_maps/`: persistent external-corpus bookkeeping. Query consumption and source-map reload inspected in gateway code; individual retained records not yet inspected. |
| `pyproject.toml` | Included | Fully inspected package entry point and dependency declarations. |
| `raw/` | Included | Source markdown and sidecars under `arxiv/`, `csv/`, `docx/`, `note/`, `pdf/`, `pubmed/`, `web/`, `youtube/`: retained input state. Tree inventoried; individual domain claims not assessed. |
| `scripts/` | Included | `install_scheduler.sh` inspected; watcher/MCP/hook installers, retrieval probe, backfill, pre-push and ingest probe inventoried. Deployment drivers, maintenance and evaluator plumbing, not an external host. |
| `src/` | Included | `gateway/cli.py`, `mcp_server.py`, web operation routes, watcher/scheduler, plan/core, ingest/apply-plan, deposit/committer, query/retrieve/answer, index refresh, draft finalization/closer and evaluator entry points inspected. Converters, filter, research adapters, lint, commit gate, queue, embeddings, reversal and integration clients remain included for detailed tracing; no claim that every operation has already been verified. |
| `tests/` | Included | Gateway, integration and end-to-end test sources; initial inspection of `e2e/test_multiagent_flow.py`. Tests specify checks, not observed success in this run. |
| `web/` | Included | Browser consumer and authoring client: `src/api.ts` inspected, SPA pages/components and `dist/` inventoried. Gateway endpoints inspected; visual behavior and bundled/source parity not tested. |
| `wiki/` | Included | `sources/`, `entities/`, `concepts/`, `synthesis/`, `mocs/`, `proposals/`, `artifacts/` are retained knowledge state; `.obsidian/`, `Clippings/` and `flowchart.md` are auxiliary vault surfaces. Tree inventoried; production, draft admission and later consumption traced in code. No assessment of every page's truth or citation quality. |

### External dependencies and excluded responsibilities

Claude Code/Claude CLI and Anthropic services supply model execution and authentication; NotebookLM and its CLI supply remote synthesis and corpus services. Obsidian supplies visualization. Source APIs, web extraction services, local application bridges and optional transcription models supply acquisition/conversion capabilities. Their gateway adapters and configuration are included, but provider internals and independently installed hosts are outside this Git source. Consequently this run cannot establish their internal retrieval, model reasoning, authentication correctness or remote service guarantees. SRC-1: `README.md`, `pyproject.toml`, `src/gateway/plan.py`, `src/gateway/ops/answer.py`, `src/gateway/ops/query.py`.

Unshipped consumers in other projects are excluded. This prevents claims about all downstream agent behavior or universal adherence to gateway-only writes; it does not exclude shipped drivers or the `.claude/` instructions. Credentials, local derived indexes and running service state are not supplied as frozen evidence. Their absence prevents deployment-specific conclusions, not inspection of the shipped implementation. No material shipped path was found inaccessible during boundary inspection.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/BadWally/TheKnowledge` | aca6e29e69c6a72b697b8178841d03e6296ee3fc | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/theknowledge-319a64927ee3/related-systems/BadWally--TheKnowledge`. Complete tracked tree inventoried. Implementation: CLI/MCP/web dispatch, ingest plan/application, deposit drain driver, draft finalization/closer, query, answer, retrieval/index refresh, scheduler/watcher and evaluator entry points; session hook scripts and browser API. Doctrine/design: complete README and CLAUDE, all six shipped skill files, schedule configuration and inspected test source. Listed paths are initial inspection, not an allowlist. | Implementation: [CLI driver](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/src/gateway/cli.py), [ingest](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/src/gateway/ops/ingest.py), [answer](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/src/gateway/ops/answer.py), [retrieval](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/src/gateway/ops/retrieve.py), [evaluator](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/src/gateway/evaluate/runner.py). Doctrine/design: [README](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/README.md), [agent control surface](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/CLAUDE.md), [editorial skill](https://github.com/BadWally/TheKnowledge/blob/aca6e29e69c6a72b697b8178841d03e6296ee3fc/.claude/skills/wiki-editorial-review/SKILL.md). | No repository access gap encountered. External service internals and local deployment state are outside this source; no observed execution or causal experiment was established. Available but unread material is identified in the coverage table, not treated as unavailable evidence. |
