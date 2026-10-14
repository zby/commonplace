---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Eidetic's shipped memory lifecycle, retrieval engine and integrations at commit 67506b62fdd0944c243537c3cb10938f7343b6b2."
run-id: AAS-2026-10-14-eidetic-0e54f3c114b3-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "67506b62fdd0944c243537c3cb10938f7343b6b2"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source: {"identity": "https://github.com/LARIkoz/eidetic", "kind": "git", "path": "/home/zby/llm/commonplace/.commonplace/worktrees/eidetic-0e54f3c114b3/related-systems/LARIkoz--eidetic", "revision": "67506b62fdd0944c243537c3cb10938f7343b6b2", "sha256": null}
---

# Eidetic boundary

## Boundary and evidence

This run characterizes Eidetic as a shipped memory/knowledge/context-engineering system for coding agents, not as the embedding library alone or as an enclosing coding-agent runtime. Its intended use is to retain personal knowledge across sessions and provide isolated, project-attached topic corpora. The boundary includes the repository's prompts, hook callers, durable writers, derived indexes, context assembly, maintenance, retrieval, exports and evaluation machinery. The whole-system classification refers to that shipped product; it does not claim that every optional path is enabled in an installed deployment. SRC-1: `README.md`, `skill/SKILL.md`, `skill/eidetic-base/SKILL.md`, `install.sh`.

The source declares the two consumption modes:

> - **Personal memory (PUSH)** — your own decisions, rules, and project context.
> --- `README.md`

> - **Topic bases (PULL)** — an external corpus (API docs, a methodology, a book) you turn into an isolated base and **attach only to the projects that need it**.
> --- `README.md`

The shipped loop is not just an API called by an unspecified external application. The installer registers SessionStart context injection, asynchronous Stop signal extraction, maintenance and PostToolUse lifecycle collection. The Stop hook reads a host-supplied transcript, calls an extraction model and passes filtered signals to `compound.py`; that module updates eligible existing cards or writes new signals. `remember.py` separately persists full answer cards. Later injection reindexes files and assembles retained content into a rules file; MCP and the recall skill expose on-demand search. These same-repository callers and writers are included. SRC-1: `install.sh`, `hooks/session-signals.sh`, `bin/compound.py`, `bin/remember.py`, `hooks/smart-memory-inject.sh`, `bin/assemble_context.py`, `mcp_server.py`, `skill/SKILL.md`.

> # Pass to compounding logic (now searches up-to-date index)
> printf '%s\n' "$RESULT" | python3 "$COMPOUND" "$(pwd)" 2>/dev/null || exit 0
> --- `hooks/session-signals.sh`

> # Assemble context via Python (crash-guarded — B6/H4: must not kill injection)
> python3 "$MEMORY_SYSTEM/bin/assemble_context.py" "$DB" "$RULES_FILE" "$(pwd)" || true
> --- `hooks/smart-memory-inject.sh`

Included maintenance extends beyond declared drift checks: pending ingest dispatches to M1 contradiction and M2 synthesis modules, while the shipped M3 transcript driver routes consolidation, acquisition and an independently gated agent lane. Their presence is not evidence of deployment activation or successful model judgments. SRC-1: `bin/index_impl.py`, `bin/m1_contradiction.py`, `bin/m2_synthesis.py`, `bin/m3_hook.py`, `hooks/semantic-maintenance.sh`.

> if os.environ.get("EIDETIC_M3_DRIVER", "").strip().lower() not in ("1", "on", "true", "yes"):
>     print(json.dumps({"m3_driver": "skip", "reason": "dark"}))
>     return 0
> --- `bin/m3_hook.py`

Topic-base creation, curated addition, indexing and attachment are included, as are the engine module and the Core-owned JSONL worker. The latter accepts logical index identifiers and resolves storage inside Core. The SDK consumer and source-specific applications described in the ownership document are outside this repository. The register freezes only Eidetic, not those applications. SRC-1: `bin/base.py`, `mcp_server.py`, `bin/engine.py`, `bin/eidetic_engine_worker.py`, `schemas/sdk/engine/v1/contract-manifest.json`, `docs/core-sdk-ownership.md`.

### Repository coverage

Every top-level tracked entry at the reviewed commit is classified below. All paths are SRC-1 commit-relative anchors. “Included” means available to this analysis, not exhaustively inspected or executed. Initial inspection traced the production, persistence, reload, admission and consumption seams named below. Remaining internal detail is available for later jobs; it is not an access gap.

| Top-level entry | Decision and role | Initial inspection / remaining coverage / exclusion consequence |
| --- | --- | --- |
| `.claude/` | Included: repository agent configuration | `.claude/settings.json` inspected; attribution settings, not the deployed lifecycle configuration. |
| `.github/` | Included: CI and contribution machinery | `.github/workflows/test.yml` matrix and index fixture/setup inspected; relevant signal and compounding checks located by search. Issue templates inventoried, not inspected; no runtime conclusion rests on them. |
| `.gitignore` | Excluded: repository hygiene | Inventoried only; no conclusion about ignored local artifacts or their retention rules. |
| `AGENTS.md` | Included: shipped agent installation procedure | Inspected in full; model choices, installation and verification instructions. |
| `CHANGELOG.md` | Included: release claims | Inventoried, not inspected; no historical claim established here. |
| `CLAUDE.md` | Included: agent consumption and maintenance instructions | Inspected in full; compound-before-create, weak-recall handling and lifecycle rules. |
| `CONTEXT.md` | Included: source-native terminology and loop intent | Inspected in full; acquisition/consolidation, miner/producer/judge distinctions. |
| `CONTRIBUTING.md` | Included: modification rules | Headings and invariants searched; not fully inspected. |
| `LICENSE` | Excluded: legal terms | Inventoried only; no legal-use conclusion. |
| `README.md` | Included: product contract and reported operation | Inspected in full; claims are declarations, not measured results of this run. |
| `README.ru.md` | Included: localized product contract | Inventoried, not inspected; no translation-parity conclusion. |
| `bin/` | Included: executable memory loop, utilities and evaluators | Traced `compound.py` and `remember.py` durable writes; `base.py` create/add/index/attach; `index_impl.py` file collection, indexing and pending M1/M2 dispatch; `assemble_context.py` reload and rules-file write; `search_impl.py` retrieval; `engine.py` API and `eidetic_engine_worker.py` protocol/storage seam. Searched lifecycle, confidence, curation, cleanup, M1/M2 and M3 responsibilities. Read `m3_hook.py` routing and activation, `recall_smoke.py` and `recall_lab.py` evaluation scope; located `canary.py` functional probes. Embed/rerank/translation, export, budget/worker, telemetry, replay and deployment utility internals remain available for deeper inspection. |
| `docs/` | Included: schema, prompts, architecture, maintenance and proposal evidence | Read `docs/MEMORY-SCHEMA.md` and `docs/core-sdk-ownership.md`. Inventory includes `docs/prompts.md`, `docs/topic-bases.md`, engine/SDK contracts, ADRs, bounded recall, semantic/resource maintenance, and `docs/eidetic-llm-wiki-ingestion/` phase/spec/review documents. Unread documents remain available; future-design prose is not automatically shipped executable behavior. |
| `examples/` | Included: shipped retained-content illustration | `examples/demo-vault/` rules, project/reference cards, hubs and Obsidian configuration inventoried, not inspected. No claim of live agent use or representative corpus quality. |
| `hooks/` | Included: host-triggered production and consumption | Read `hooks/smart-memory-inject.sh` and `hooks/semantic-maintenance.sh`; read extraction, filtering, M3 dispatch and compounding portion of `hooks/session-signals.sh`, searched provider routes; `hooks/lifecycle-signals.sh` entry point located. Provider-helper and lifecycle details remain for later inspection. |
| `install.sh` | Included: deployment and registration | Traced runtime/skill installation and read lifecycle hook registration, metadata and initial-index steps. Remaining setup details available. |
| `llms.txt` | Included: discovery/recommendation instructions | Headings and capability claims searched; full text not inspected. No recommendation claim adopted. |
| `mcp_server.py` | Included: personal and topic-base tool consumers | Read search/detail, reindex, health/lint/export handlers and base add/tool replacement. Dispatch entry points located; remaining transport details available. Personal-memory MCP surface is not assumed to have the base's add tool. |
| `requirements-mlx.txt` | Included: optional model dependency specification | Inventoried, not inspected; exact dependency compatibility not established. |
| `schemas/` | Included: shared engine protocol contracts | Read `schemas/sdk/engine/v1/contract-manifest.json`; request/response/record/freshness schemas inventoried and available, not fully inspected. |
| `skill/` | Included: model-facing callers and admission instructions | Read `skill/SKILL.md` and `skill/eidetic-base/SKILL.md` in full; weak results require inspection, curated base writes require explicit user instruction. |
| `tests/` | Included: shipped evaluators and fixtures | Located engine, truth-maintenance, bounded recall, lifecycle and M3 suites; read `tests/test_m3_v3_lanes.py` hook routing/cache/retry assertions, including mocked miner/producer/acquisition calls. Remaining tests and fixtures available. No tests executed and no pass result inferred. |

### External dependencies and limits

Claude Code owns lifecycle event delivery, transcript production and loading the generated rules; other MCP agents own when to call tools and how to use results. Eidetic's shipped adapters are included, but those hosts are not frozen. This prevents conclusions about actual host compliance, end-to-end agent behavior or cross-host parity. SRC-1: `install.sh`, `hooks/smart-memory-inject.sh`, `hooks/session-signals.sh`, `skill/SKILL.md`, `README.md`.

Extraction and judgment depend on model routes and external CLIs/services; semantic retrieval depends on embedding/reranking models and optional packages, with additional translation and MLX paths. Python, Bash, SQLite, file locking and local host configuration are deployment dependencies. Only the dependency-facing code and declarations in SRC-1 are frozen. No provider service, model weights, installed runtime, user memory corpus, transcript stream, private recall battery, external SDK, importer or YouGile consumer was acquired. This prevents provider-quality, deployment-activation, private-corpus performance and external-integration correctness conclusions. SRC-1: `README.md`, `hooks/session-signals.sh`, `bin/m3_hook.py`, `bin/recall_lab.py`, `bin/recall_smoke.py`, `docs/core-sdk-ownership.md`.

The fixed evidence is commit `67506b62fdd0944c243537c3cb10938f7343b6b2`, with an applicability cutoff of 2026-10-14. HEAD matched the acquired revision and the checkout reported no changes during boundary inspection. The overall tier is code-grounded: implementation and source-owned design are inspectable, but this job executed neither the target nor its tests and registered no observed-run or causal-experiment evidence. Available but unread files above are coverage work, not unavailable evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/LARIkoz/eidetic` | 67506b62fdd0944c243537c3cb10938f7343b6b2 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/eidetic-0e54f3c114b3/related-systems/LARIkoz--eidetic`. Implementation: tree inventory and entry-point/consumer tracing through installer, hooks, compound/remember/base writers, index/context/search, engine worker, M1/M2/M3 routing, and evaluator/test scope described in the coverage table. Doctrine/design: README, agent instructions, both skills, memory schema and Core/SDK ownership. Reported operation: README performance and deployment claims and ownership inventory, not independently verified. | Implementation: [installer](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/install.sh), [signal hook](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/hooks/session-signals.sh), [context assembly](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/bin/assemble_context.py), [M3 driver](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/bin/m3_hook.py), [engine worker](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/bin/eidetic_engine_worker.py). Doctrine/design and reported operation: [README](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/README.md), [ownership](https://github.com/LARIkoz/eidetic/blob/67506b62fdd0944c243537c3cb10938f7343b6b2/docs/core-sdk-ownership.md). Other initially inspected paths are recorded above. | No repository access gap found. External hosts, services, SDK/importer/application repositories and private deployment/corpus/probe evidence are not frozen; no end-to-end efficacy, activation, provider-quality or external-consumer parity conclusion. Tests and evaluator code supply implementation evidence, not observed test outcomes or causal support. |
