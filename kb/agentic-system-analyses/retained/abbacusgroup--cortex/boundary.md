---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Cortex's shipped knowledge capture, maintenance and serving system at commit a51c2209eb6d26812c19c97aaade3cb64ccfc23c."
run-id: AAS-2026-10-17-cortex-3da14ce55a2b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: a51c2209eb6d26812c19c97aaade3cb64ccfc23c
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/abbacusgroup/cortex
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-cortex/related-systems/abbacusgroup--cortex
  revision: a51c2209eb6d26812c19c97aaade3cb64ccfc23c
  sha256: null
---

# Cortex boundary

## Boundary and evidence

This run examines Cortex as a persistent knowledge service for AI agents and human operators, not as an enclosing conversational agent runtime. Its intended use is to retain typed knowledge objects and relationships, enrich that state, and return search results, context briefings, documents, dossiers and syntheses. The target class is **memory/knowledge/context-engineering system**. Its agent-facing tools and optional internal model calls make it in scope. SRC-1, `llms.txt`, `src/cortex/transport/mcp/server.py`, `src/cortex/services/llm.py` and `src/cortex/retrieval/presenters.py` establish that classification.

The agent-facing doctrine explicitly identifies later context consumption:

> Token-efficient briefing (summaries only). Use this for context injection.
> --- `llms.txt`

The boundary is **whole-system**: the shipped CLI, MCP server and client, REST facade, dashboard, importers, storage, ontology, intelligence pipeline, retrieval, access feedback, maintenance commands, prompts, deployment definitions and evaluators belong to the target. In particular, the repository's CLI and dashboard are not excluded hosts merely because they call MCP. The console entry point is `cortex.cli.main:app`; `serve` dispatches stdio MCP, HTTP MCP or REST, and the registration command configures an external Claude Code client. SRC-1, `pyproject.toml`, `src/cortex/cli/main.py`, `src/cortex/transport/api/server.py` and `src/cortex/dashboard/server.py`.

The initial trace covers these material paths:

- **Produce and admit:** MCP capture accepts raw content or caller-supplied classification; CLI capture routes through MCP or directly through the pipeline. The pipeline creates retained objects before running normalization, linking, enrichment and reasoning. Obsidian import can use that pipeline or create objects directly; the v1 importer is another direct ingestion route. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/cli/main.py`, `src/cortex/pipeline/orchestrator.py` and `src/cortex/pipeline/importer.py`.
- **Persist and reload:** the unified store opens graph and content stores from configuration, creates in both, reads content with graph relationships and initializes temporal versioning. Stage and tool code also accesses the component stores directly; inclusion does not imply that every mutation uses the unified update method. SRC-1, `src/cortex/db/store.py`, `src/cortex/db/content_store.py`, `src/cortex/db/graph_store.py`, `src/cortex/core/config.py`, `src/cortex/pipeline/normalize.py` and `src/cortex/transport/mcp/server.py`.
- **Maintain:** normalization can call an LLM or accept preclassified content; relationship discovery, tier/staleness enrichment, OWL-RL rules, advanced reasoning, object editing/classification/deletion, temporal history, backup/restore and doctor commands remain within scope. SRC-1, `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/link.py`, `src/cortex/pipeline/enrich.py`, `src/cortex/pipeline/reason.py`, `src/cortex/pipeline/advanced_reason.py`, `src/cortex/pipeline/temporal.py`, `src/cortex/cli/backup.py` and `src/cortex/cli/main.py`.
- **Consume and feed back:** MCP search/context/read use retrieval and presenters; document reads and positive feedback call access tracking. Dashboard and REST handlers forward capture, retrieval, maintenance and feedback to the shipped MCP client. This establishes service-side reuse paths, not proof that an external agent actually uses the returned content successfully. SRC-1, `src/cortex/transport/mcp/server.py`, `src/cortex/transport/mcp/client.py`, `src/cortex/retrieval/engine.py`, `src/cortex/retrieval/learner.py`, `src/cortex/retrieval/presenters.py`, `src/cortex/dashboard/server.py` and `src/cortex/transport/api/server.py`.

The persistence boundary is executable code, not just a proposed architecture:

> # Step 1: Ingest — create in both stores
> obj_id = self.store.create(
> --- `src/cortex/pipeline/orchestrator.py`

The MCP capture contract also assigns some classification responsibility to its external model caller:

> """Capture a knowledge object. When calling via MCP, YOU (Claude) are the classifier.
> --- `src/cortex/transport/mcp/server.py`

That contract and the shipped `llms.txt` instructions are evidence of intended agent behavior, not an observed agent trajectory. Cortex's internal completion wrapper and normalization path are implementation evidence for optional model-assisted processing; a model provider need not be configured for every capture. SRC-1, `src/cortex/services/llm.py` and `src/cortex/pipeline/normalize.py`.

### Repository coverage

Every top-level tracked entry is classified below. “Included” fixes functional scope, not a claim to have read every line. Initial inspection combines complete orientation/key implementation files, bounded implementation reads and scoped symbol/call searches. Detail not yet inspected remains available at the same pin; it is not an access gap.

| Top-level entry | Treatment and material paths | Inspection status and limits |
|---|---|---|
| `.env.example` | Included: configuration surface alongside `src/cortex/core/config.py`. | Listed; example settings not yet read. Configuration loader paths inspected. No claim of exhaustive setting coverage. |
| `.github/` | Included: `workflows/test.yml`, `workflows/release.yml` for evaluation/build definitions. Issue templates, ownership and dependency automation excluded from functional analysis. | Workflow command searches inspected; remaining governance files only listed. No claim about governance effectiveness or actual CI outcomes. |
| `.gitignore` | Excluded: checkout hygiene. | Listed, not read; ignored local state cannot be reconstructed from this run. |
| `.python-version` | Included: runtime packaging context. | Listed, not read; Python requirement inspected in `pyproject.toml`. No environment compatibility test. |
| `CHANGELOG.md` | Included as optional source-native release doctrine. | Listed, not read; no release-history conclusions established. |
| `CODEMAP.md` | Included: architecture and data-flow orientation. | Read completely; design claims require implementation checks. |
| `CODE_OF_CONDUCT.md` | Excluded: community governance. | Listed, not read; no conduct-policy assessment. |
| `CONTRIBUTING.md` | Excluded: contributor process. | Listed, not read; no contributor-workflow assessment. |
| `Dockerfile` | Included: setup/server container entry point. | Entrypoint and health-check command search inspected; image build not exercised. |
| `LICENSE` | Excluded: legal assessment. | Listed, not read; no licensing conclusion. |
| `README.md` | Included: product intent, entry points, architecture and operator maintenance instructions. | Read completely; statements of operation remain attributed unless code-grounded separately. |
| `SECURITY.md` | Included as optional security doctrine. | Listed, not read; no security-policy or vulnerability conclusion established. |
| `benchmarks/` | Included: `conftest.py`, `corpus/`, `metrics/`, and all five `b1_hybrid_retrieval/` through `b5_pattern_detection/` evaluators. | Shared fixtures read; evaluator assertions and test structure searched across all five suites. Corpus and metric internals not yet inspected. Synthetic retrieval fixture is not live-provider evidence. No benchmarks executed. |
| `deploy/` | Included: both launchd plists and both systemd service units for MCP/dashboard. | Tree and service entrypoint searches inspected. No evidence of installed-service behavior. |
| `docker-compose.yml` | Included: container deployment configuration. | Listed and searched with deployment files; detailed configuration not yet read. No deployment result inferred. |
| `docs/` | Excluded: `dashboard/dashboard1.png` through `dashboard/dashboard4.png` screenshots. | Listed, images not inspected. No visual/UI fidelity or operational-state claim follows from them. Dashboard executable paths remain included. |
| `homebrew/` | Included: `Formula/abbacus-cortex.rb` and `update-formula.sh` distribution support. | Tree and formula command searches inspected; update script not yet read. No installation/release success claim. |
| `llms.txt` | Included: agent tool descriptions and capture/classification/context/feedback maintenance instructions. | Read completely as doctrine/design, not proof of compliance. |
| `ontology/` | Included: development ontology `cortex.ttl`, paired with packaged ontology. | Listed; resolver fallback inspected. Root ontology contents not yet compared with packaged copy. No parity claim. |
| `pyproject.toml` | Included: console entry point, dependencies, packaging and evaluator configuration. | Read completely; dependency implementation is outside the frozen repository. |
| `resources/` | Included: both `ollama/*kb-classifier.Modelfile` prompt/model recipes. | Both read completely as shipped optional recipes. Their installation or selection by a running provider is not established. |
| `src/` | Included: `cortex/cli/main.py`, `cli/backup.py`, `cli/install.py`, setup/helpers; `core/`; `db/store.py`, `db/content_store.py`, `db/graph_store.py`; `ontology/`; `pipeline/`; `retrieval/`; `services/`; `transport/mcp/`, `transport/api/`; `dashboard/server.py`, templates/static assets; module entry points and package markers. | Full store, orchestrator, normalizer and learner reads; bounded CLI/server/presenter/LLM/ontology/importer reads; signatures and call searches for backing stores, pipeline stages, client, embeddings, install and backup. Dashboard route consumers searched. Setup internals, templates/static assets and some helper bodies not yet inspected. No material shipped state-producing or consuming subsystem is deliberately excluded. |
| `tests/` | Included: CLI, storage/sync, pipeline, retrieval, transports, dashboard, deployment, integration and distribution evaluators. | Tree inspected; scoped test-class searches cover orchestrator, dual-store sync, learner, MCP and REST concurrency. Other test bodies not yet inspected. Source assertions do not establish a passing suite. |
| `uv.lock` | Included: dependency resolution context. | Listed, not read; no resolved-dependency audit or reproducibility claim. |

### Frozen applicability and exclusions

The evidence is SRC-1 at commit **a51c2209eb6d26812c19c97aaade3cb64ccfc23c**, with applicability cutoff **2026-10-17**. The acquired checkout's HEAD was verified against that full commit. This run freezes the repository revision, not later upstream documentation, live services, installed models or a user's knowledge database. Overall evidence tier is **code-grounded**. No target code, tests, benchmarks or examples were executed.

External Claude Code/other MCP hosts and their task loops are outside this repository boundary. Their choices to capture, classify, read or act on returned content are not attributed to Cortex; consequently this run cannot establish end-to-end task improvement, actual context injection or caller compliance. The shipped registration code is included. SRC-1, `src/cortex/cli/main.py` and `src/cortex/transport/mcp/server.py`.

External model services and model weights, the implementations of Oxigraph/SQLite, MCP, FastAPI, LiteLLM and sentence-transformers, and OS/container service managers are dependencies, not additional frozen sources. Cortex's adapters, configuration, schemas, prompts and launch definitions remain included. This prevents conclusions about provider quality, dependency correctness, deployed locking/durability or platform reliability beyond what Cortex source specifies. SRC-1, `pyproject.toml`, `src/cortex/services/llm.py`, `src/cortex/services/embeddings.py`, `src/cortex/db/store.py` and `deploy/cortex-mcp.service`.

No required repository material was found unavailable. Uninspected available files are marked above rather than represented as access failures. No supplied execution trace, production corpus or experimental result was frozen; source-level evaluators support analysis of evaluation design, not measured outcomes or causal benefit.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/abbacusgroup/cortex` | a51c2209eb6d26812c19c97aaade3cb64ccfc23c | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-cortex/related-systems/abbacusgroup--cortex`. Implementation: `pyproject.toml`; `src/cortex/cli/main.py`; `src/cortex/pipeline/orchestrator.py`, `src/cortex/pipeline/normalize.py`, `src/cortex/pipeline/importer.py`; `src/cortex/db/store.py`; `src/cortex/retrieval/engine.py`, `src/cortex/retrieval/learner.py`, `src/cortex/retrieval/presenters.py`; `src/cortex/services/llm.py`; `src/cortex/transport/mcp/server.py`; `src/cortex/transport/api/server.py`; `src/cortex/dashboard/server.py`; `src/cortex/ontology/resolver.py`; benchmark fixtures. Further scoped searches and partial reads are described in the coverage table. Doctrine/design: complete `README.md`, `CODEMAP.md`, `llms.txt` and both classifier Modelfiles; packaged ontology class declarations. | Implementation: [entry point](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/pyproject.toml), [capture/pipeline](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/pipeline/orchestrator.py), [MCP tools](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/transport/mcp/server.py), [storage](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/src/cortex/db/store.py), [evaluation fixtures](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/benchmarks/conftest.py). Doctrine/design: [product contract](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/README.md), [agent instructions](https://github.com/abbacusgroup/cortex/blob/a51c2209eb6d26812c19c97aaade3cb64ccfc23c/llms.txt). | No required checkout access gap. Implementation is inspected source, not observed execution; no benchmark outcome, production effectiveness, provider behavior or external-host compliance established. Doctrine is declared intent, not an observed run. |
