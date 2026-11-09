---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Stigmergy's shipped team-knowledge capture, filing, maintenance and consumption system at commit 0ca8bb1963ad9cf43eaf2c18329998023a9caa4f."
run-id: AAS-2026-11-08-stigmergy-2de42cc04367-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "0ca8bb1963ad9cf43eaf2c18329998023a9caa4f"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/sturlese/stigmergy
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/stigmergy-a6565e81e441/related-systems/sturlese--stigmergy
  revision: "0ca8bb1963ad9cf43eaf2c18329998023a9caa4f"
  sha256: null
---

# Stigmergy boundary

## Boundary and evidence

This run examines Stigmergy as a complete shipped team-knowledge system, not just its MCP server or librarian API. Its intended use is to accept captures from people and agents, retain evidence, compile a shared wiki, maintain it, and return visibility-scoped knowledge to later readers. The target class is **memory/knowledge/context-engineering system** and the boundary kind is **whole-system**. It is in scope because its knowledge-production and answering paths issue model calls; it is not merely a static store or a host-independent returning computation. The source's own description supplies the intended use (SRC-1, `README.md`):

> Immutable
> source material enters one queue, one librarian agent keeps a small Git-and-Markdown wiki current,
> and every search and answer is scoped to what the caller may see.
> --- `README.md`

The implementation trace starts at the console scripts declared in SRC-1, `pyproject.toml`. The librarian CLI constructs workspace dependencies and a worker; the worker claims a tenant's queued operation and invokes the writer. The capture writer extracts evidence, renders a source page, constructs a safe existing-context view and requests a filing plan (SRC-1, `src/stigmergy/librarian/cli.py`, `src/stigmergy/librarian/worker.py`, `src/stigmergy/knowledge/writer.py`). The planner actually supplies the shipped librarian instructions to its structured model call, rather than merely documenting an optional prompt (SRC-1, `src/stigmergy/knowledge/planner.py`):

> result = await self._run_structured(
>     output_type=FilingPlan,
>     instructions=_read_skill(),
> --- `src/stigmergy/knowledge/planner.py`

> return expected_librarian_skill().decode("utf-8")
> --- `src/stigmergy/knowledge/planner.py`

The packaged instructions establish the model-dependent state transformation (SRC-1, `src/stigmergy/knowledge/librarian_skill.md`):

> Read the complete source and return one `FilingPlan`: the note, concept, entity, and project pages
> this source creates or updates, and the wikilinks that connect them. The source is immutable evidence.
> The catalog and candidate pages are the existing graph. Do not narrate your work.
> --- `src/stigmergy/knowledge/librarian_skill.md`

The read loop is shipped here too. MCP wrappers call `BrainService`, the bridge proxies reads while acquiring submission artifacts locally, and the answer service invokes its synthesizer over service-backed evidence and verifies the result (SRC-1, `src/stigmergy/server/mcp_server.py`, `src/stigmergy/server/service.py`, `src/stigmergy/bridge/server.py`, `src/stigmergy/answer/service.py`). This is later consumption of retained wiki state, not just a write-only library. The answering implementation includes:

> prompt = first_message(question, self._first_search(question, ctx))
> --- `src/stigmergy/answer/service.py`

> verdict = verify(out, evidence, ctx.page_as_read, ctx.read_paths)
> --- `src/stigmergy/answer/service.py:264-264`

Functional inclusions are acquisition and normalization, original-evidence retention, queue admission and routing, tenant and audience policy, model planning and its instructions, candidate mutation and publication gates, Git publication and change records, scheduled repair and recompile, index construction and reconciliation, retrieval and verified answers, shipped adapters, backoffice readers and controls, erasure/refiling, deployment wiring, and evaluation drivers. The maintenance and lifecycle paths are part of the target, not an excluded host: the writer worker calls garden/rebuild/erasure paths, and the architecture declares recompile and refiling responsibilities (SRC-1, `src/stigmergy/librarian/worker.py`, `src/stigmergy/knowledge/writer.py`, `docs/ARCHITECTURE.md`). Their detailed semantics remain for later analysis; inclusion does not certify their correctness.

The frozen evidence is repository `https://github.com/sturlese/stigmergy` at full commit `0ca8bb1963ad9cf43eaf2c18329998023a9caa4f`, inspected read-only at the source path above. HEAD was checked against the acquired revision. The applicability cutoff is **2026-11-08**, the supplied run date, not a claim about when every file was authored. The overall tier is **code-grounded**: executable entry points and producer/consumer paths were inspected alongside design documentation. No target code, tests, examples, models or services were executed.

External dependencies include model routing/providers through OpenRouter, Postgres/pgvector, Git/GitHub and the librarian App, a private object store, Slack, Google Drive acquisition, and deployment services such as Fly. Their shipped clients, configuration and failure-handling code remain included; service internals and live deployments do not. This prevents conclusions about provider internals, actual deployment availability, production isolation, latency, cost or observed knowledge quality. The dependency declarations, process wiring and intended integrations are in SRC-1, `pyproject.toml`, `docker-compose.yml`, `README.md` and `docs/ARCHITECTURE.md`. External MCP hosts such as Claude Code and Codex are consumers, not Stigmergy-owned runtimes; this boundary cannot establish their autonomous submission policy or whether they actually reuse a returned answer. Tenant knowledge repositories and operator-created landing/legal content are not supplied as live evidence; fixtures and documentation cannot establish production corpus behavior (SRC-1, `README.md`, `docs/ARCHITECTURE.md`, `evals/README.md`). These are evidence limits, not reasons to omit the shipped producer or consumer code.

### Tracked-root coverage

The tracked tree was enumerated at the pin. Every top-level tracked file or directory is classified below. “Included” means within the functional/evidence boundary, not that every descendant has already received line-by-line analysis. Initial inspection traced the principal write/read entry points and maintenance dispatch. Detailed implementations, specs, fixtures, tests and operator instructions not yet read remain available under SRC-1; they are **not access gaps**. No material shipped path was inaccessible. Excluded rows are deliberate scope exclusions, not unavailable evidence.

| Top-level path(s) | Classification and material responsibility | Initial inspection and limits |
|---|---|---|
| `src/` | Included: `stigmergy/capture` produces and queues evidence; `knowledge` supplies context, librarian instructions, filing, gates and repair; `librarian` owns workspace checkout, writer dispatch, scheduling and Git transport; `changes` retains mutation records; `entities` maintains identity pages; `index` builds and reloads searchable state; `server` admits scoped requests; `answer` consumes retained pages through model synthesis and verification; `bridge` and `slack` supply captures and readers; `admin` serves controls and wiki views; `ops` erases, resets and replays state; `kernel` supplies tenancy, policy and model boundaries; `text.py` supplies text handling. | SRC-1: inspected `src/stigmergy/librarian/cli.py`, dispatch in `src/stigmergy/librarian/worker.py`, capture and maintenance call sites in `src/stigmergy/knowledge/writer.py`, planner and skill, MCP wrappers, service submission call sites, bridge tools, Slack startup, `src/stigmergy/index/cli.py`, `src/stigmergy/answer/service.py`, and `src/stigmergy/admin/routes.py`. Detailed downstream gates/storage/policies remain to be inspected, not excluded. |
| `web/` | Included: shipped backoffice caller and later wiki consumer; `src/features/wiki` reloads retained views, `src/features/ops` and `src/features/access` expose maintenance and admission controls, `src/features/platform` controls workspaces; build and client tests are included. | SRC-1: tree, `web/src/lib/api.ts`, and package/static-build declarations in `pyproject.toml`; frontend feature details remain available, not inspected yet. The API client uses `/admin/api/`, so this is not an external enclosing application. |
| `evals/` | Included: canonical and graph corpora, golden questions and scopes, retrieval/QA/routing/alias runners, filing planner and parity drivers, recorded history and corpus provenance. These are shipped evaluators and retained fixtures, not an excluded testing host. | SRC-1: `evals/README.md` and imports/driver contract in `evals/run_qa.py`; corpus and other runner details remain available for later inspection. No independent reproduction of scores or causal effect is established. |
| `tests/` | Included: subsystem, integration, ACL, adversarial and lifecycle contracts, fake-model paths, Postgres/Git fixtures and evaluation-driver tests. | SRC-1: tracked inventory and test configuration in `pyproject.toml`; test bodies not yet inspected. Their existence does not demonstrate passing tests in this run. |
| `docs/` | Included: `ARCHITECTURE.md`, `OPERATIONS.md`, `SELF-HOSTING.md`, `DATA-PROTECTION.md`, `ERASE.md`, `RESET.md` and explanatory assets. Maintenance and erasure instructions are within the boundary. | SRC-1: `docs/ARCHITECTURE.md` inspected; other documents/assets inventoried but not yet read. Design claims are attributed intent until checked against code. |
| `specs/` | Included: `karpathy-team-wiki.md`, `retrieval-and-curation.md`, `audience-layers.md`, `multi-tenancy.md`, `backoffice-users-and-wiki.md`, `data-erasure.md`. | SRC-1: tree and references in `README.md` / `docs/ARCHITECTURE.md`; specification details not yet inspected. |
| `deploy/` | Included: Slack app manifest admits the shipped Slack integration. | SRC-1: `deploy/slack-app-manifest.json` inventoried and identified by `README.md`; exact permission/event configuration not yet inspected. |
| `scripts/` | Included: staging deploy/checkout refresh, object-store smoke driver and Postgres test-database initialization. | SRC-1: tree; roles identified by `README.md` and `docker-compose.yml`. Script details not yet inspected; no deployment or smoke-test result inferred. |
| `.github/` | Included: CI workflow and contribution templates as shipped verification/release context. | SRC-1: `.github/workflows/ci.yml`, issue/PR templates inventoried; exact workflow gates not yet inspected. |
| `.claude/` | Included: `skills/land-a-change/SKILL.md` and `skills/validate-deployment/SKILL.md` as shipped maintenance instructions, not instructions binding this analyst. | SRC-1: tree only; detailed procedures not yet inspected. |
| `README.md` | Included: intended operation, user interfaces, deployments, model policy and quality claims. | SRC-1: inspected; claims are doctrine or reported operation, not reproduced measurements. |
| `pyproject.toml`, `uv.lock`, `ruff.toml` | Included: entry points, packaged prompt/static artifacts, dependency and development-tool boundary. | SRC-1: `pyproject.toml` inspected; lock and lint details not yet inspected. |
| `Dockerfile`, `docker-compose.yml`, `fly.toml`, `Makefile`, `.env.example` | Included: process/build/dependency wiring and operator configuration that determine shipped execution paths. | SRC-1: compose inspected and process roles traced from `README.md`; remaining files inventoried, not yet inspected in detail. No live configuration or secrets are evidence. |
| `.dockerignore`, `.gitignore`, `.gitleaks.toml` | Included: packaging exclusions, generated-state exclusions and secret-scanning configuration. | SRC-1: tree only; details not yet inspected. |
| `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md` | Included: shipped contributor/agent maintenance rules, security-reporting contract and attributed change history. | SRC-1: tree and README references; contents not yet inspected. They neither direct this run nor prove deployed behavior. |
| `CLA.md`, `CODE_OF_CONDUCT.md`, `LICENSE`, `THIRD-PARTY-LICENSES.md` | Excluded from functional analysis: legal/conduct texts, not knowledge-state producers or consumers. | SRC-1: tracked inventory and license/package references in `README.md` / `pyproject.toml`. This exclusion prevents legal-compliance, licensing-compatibility and conduct-enforcement conclusions. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/sturlese/stigmergy` | 0ca8bb1963ad9cf43eaf2c18329998023a9caa4f | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/stigmergy-a6565e81e441/related-systems/sturlese--stigmergy`. Implementation: package entry points; librarian CLI and worker claim/dispatch; workspace/planner dependencies by call-site search; capture writer and maintenance call sites; model planner and skill loading; MCP read wrappers and service submission call sites; bridge acquisition/proxy; Slack startup; index CLI; answer loop and verification call; admin route dependencies; web API client; QA runner contract/imports. Doctrine/design: README, architecture, compose, packaged librarian instruction and evaluation README. Reported operation: README quality/deployment claims only, not independently verified. The tracked tree was enumerated in full; remaining files are available at this same pin. | Implementation: [entry points](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/pyproject.toml), [writer](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/src/stigmergy/knowledge/writer.py), [planner](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/src/stigmergy/knowledge/planner.py), [answer consumer](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/src/stigmergy/answer/service.py), [QA driver](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/evals/run_qa.py). Doctrine/design: [architecture](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/docs/ARCHITECTURE.md), [librarian instructions](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/src/stigmergy/knowledge/librarian_skill.md). Reported operation and intended use: [README](https://github.com/sturlese/stigmergy/blob/0ca8bb1963ad9cf43eaf2c18329998023a9caa4f/README.md). Other local anchors above resolve at this same commit. | No checkout access gap. No external service internals, live tenant corpus or independently observed run was supplied or produced; implementation intent and attributed results cannot establish actual production reliability, security, quality or causal benefit. Unread available files are inspection work still to do, not missing sources. |
