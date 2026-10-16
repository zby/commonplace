---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "CQ's shipped agent knowledge-sharing system at commit 5765494a3840e5f5a7223c42101f41e85cb9d898, including prompts, clients, stores, remote admission and review."
run-id: AAS-2026-10-14-cq-8fb3dc41c334-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "5765494a3840e5f5a7223c42101f41e85cb9d898"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/mozilla-ai/cq
  revision: "5765494a3840e5f5a7223c42101f41e85cb9d898"
  path: /home/zby/llm/commonplace/.commonplace/worktrees/cq-8fb3dc41c334/related-systems/mozilla-ai--cq
  sha256: null
---

# CQ boundary

## Boundary and evidence

CQ is in scope as a **memory/knowledge/context-engineering system** serving model-driven agents. Its intended use is retaining and sharing structured knowledge so agents can query earlier lessons, propose new lessons, and confirm or flag retrieved guidance. The target is the shipped CQ system, not just its SDK or MCP handlers. Its **whole-system** boundary includes the behavioral prompts that produce and consume knowledge, host installation and lifecycle hooks, CLI and MCP entry points, Go and Python clients, local and remote persistence, remote human-review admission, schemas, maintenance utilities and source-level tests. SRC-1: `README.md`, `cli/main.go`, `plugins/cq/.claude-plugin/plugin.json`, `sdk/go/client.go`, `server/backend/src/cq_server/app.py`.

The model-dependent part is principally the consuming host agent following CQ's shipped instructions, not an enclosing agent runtime implemented by CQ. The skill specifies the retained-content consumption path:

> cq is a shared knowledge commons for AI agents. Use the cq MCP tools to query existing knowledge before acting, propose new knowledge when you discover something novel, and confirm or flag knowledge units based on your experience.
> --- `sdk/go/prompts/SKILL.md`

Session reflection also belongs inside the system boundary because CQ ships the procedure for producing candidates from session history. It does not establish a server-owned model loop:

> Reflection is agent-led — there is no MCP tool for this step. Using your own reasoning, scan the session for insights worth sharing.
> --- `sdk/go/prompts/reflect.md`

These are doctrine/design evidence under SRC-1. The executable MCP registration exposes query, propose, confirm, flag and status; the Python default reflector is a guidance-returning stub. SRC-1: `cli/mcpserver/server.go`, `sdk/python/src/cq/reflect.py`. The host owns its model calls, session history, application actions and decision to follow instructions. Those responsibilities are not attributed to CQ.

### Shipped loop traced for this boundary

- **Produce and consume:** plugin configuration launches `cq mcp` and supplies commands and skills. The CLI also exposes direct knowledge operations. The Pi adapter installs the shared skill, transformed reflection/status prompts and an instruction block mapping tool wording to shell invocations. These shipped callers are included rather than treated as external applications. SRC-1: `plugins/cq/.claude-plugin/plugin.json`, `cli/main.go`, `cli/internal/install/pi.go`, `sdk/go/prompts/SKILL.md`, `sdk/go/prompts/reflect.md`.
- **Persist and reload:** the CLI constructs the Go client; its store selection opens persistent SQLite by default or accepts a selected alternative. The SQLite store reads serialized knowledge back from the database. Python likewise selects a local store and its SQLite implementation inserts serialized units and reloads them. SRC-1: `cli/cmd/cli.go`, `sdk/go/client.go`, `sdk/go/store_sqlite.go`, `sdk/python/src/cq/client.py`, `sdk/python/src/cq/store.py`.
- **Transfer and maintain:** the Go client includes local/remote query merging, proposal fallback, confirmations, flags and draining. MCP startup initiates a background drain when a remote is configured. Cursor hooks persist bounded failure snippets and later surface and clear them; these are separate auxiliary session state, not knowledge units. SRC-1: `sdk/go/client.go`, `cli/cmd/mcp.go`, `cli/internal/hook/cursor.go`.
- **Admit and later retrieve:** the remote app assembles knowledge and review APIs and owns the database lifecycle. Knowledge proposals are persisted by the knowledge service; the review service approves or rejects pending units. The repository's ordinary query path loads approved units and ranks them. The browser review page is a shipped consumer and decision driver, so it is included. SRC-1: `server/backend/src/cq_server/app.py`, `server/backend/src/cq_server/api/routes/knowledge.py`, `server/backend/src/cq_server/services/knowledge.py`, `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/repositories/knowledge.py`, `server/backend/src/cq_server/repositories/_queries.py`, `server/frontend/src/pages/ReviewPage.tsx`.
- **Maintain and evaluate:** backup, migration and seeding utilities are included. The seed driver creates, approves and adjusts units through server APIs; it is not an excluded host. Source-level tests include an MCP propose/query/confirm/flag/status sequence and a server persistence-to-public-query smoke test. These are implementation evidence about test design, not observed test results. SRC-1: `server/scripts/backup-db.sh`, `server/scripts/migrate-team-db.sh`, `server/scripts/migrate-v1.sh`, `server/scripts/seed-kus.py`, `cli/mcpserver/e2e_test.go`, `server/backend/tests/test_sqlite_store_e2e.py`.

The persistent Python consumption path is explicit:

> return KnowledgeUnit.model_validate_json(row[0])
> --- `sdk/python/src/cq/store.py:479-488`

The supplied line range identifies this occurrence in `get`, rather than another deserialization call. This is SRC-1 implementation evidence of reloading a stored unit, not evidence that a host applied its advice.

### Top-level coverage

Every tracked top-level entry is classified below. “Included” defines the functional boundary; it does not claim every file has already been read. Paths listed as initially inspected were read or searched to establish responsibilities. Available but not yet inspected material remains available for later jobs under SRC-1; it is not an access gap.

| Top-level entry | Treatment and material paths or role | Initial inspection and bounded conclusions |
|---|---|---|
| `.claude-plugin/` | Included: marketplace distribution metadata | Tree inspected; marketplace body not yet inspected. No marketplace-install success claim. |
| `.env.example` | Included: deployment configuration example | Enumerated, not yet inspected; no completeness claim about documented settings. |
| `.gitbook-branch-readme.md` | Excluded: documentation publishing wrapper | No conclusion about rendered branch-site presentation. |
| `.gitbook.yaml` | Excluded: documentation publishing configuration | No conclusion about published-site configuration. |
| `.github/` | Included: CI/evaluation and release wiring, especially `workflows/ci-prompts-sync.yaml` and component CI workflows | Prompt-sync workflow inspected; other workflows and issue templates enumerated, not yet inspected. No CI results or release success inferred. |
| `.gitignore` | Excluded: checkout hygiene | No conclusion about ignored deployment artifacts. |
| `.golangci.yml` | Excluded: lint configuration | No Go lint-policy assessment. |
| `.pre-commit-config.yaml` | Excluded: development checks | No pre-commit-policy assessment. |
| `CONTRIBUTING.md` | Excluded: contribution process | No contributor-governance assessment. |
| `CONTRIBUTOR_AGREEMENT.md` | Excluded: legal contribution terms | No assessment of contributor legal obligations. |
| `DEVELOPMENT.md` | Included: component development and migration instructions | Enumerated, not yet inspected; no claim of exhaustive operator-documentation coverage. |
| `LICENSE` | Excluded: legal text | No license-compliance assessment. |
| `Makefile` | Included: shipped development/deployment/maintenance driver | Enumerated, not yet inspected; underlying maintenance scripts inspected, but make-target behavior not yet established. |
| `README.md` | Included: intended use, integration and storage overview | Read completely; declared intent is not hosted-service observation. |
| `SECURITY.md` | Excluded: vulnerability reporting policy | No security-response-process assessment. |
| `build/` | Included: `brew/` packaging and `licenses/` notice generation | Tree inspected, bodies not yet inspected; no package-build or distribution verification. |
| `cli/` | Included: `main.go`, `cmd/`, `mcpserver/`, `internal/install/`, `internal/hook/`, authentication and credential storage, tests | Entry tree, client construction, MCP startup and tool registration, Pi installer, Cursor hook and MCP E2E test inspected. Other host/auth adapters and command handlers remain for detailed analysis. |
| `docker-compose.yml` | Included: server deployment and durable volume | Read; configuration only, no deployment run. |
| `docs/` | Included: architecture, installation, discovery, proposal and historical design plan | `architecture.md` read; other documents enumerated. Design and historical plans do not establish current implementation. |
| `plugins/` | Included: `cq/.claude-plugin/plugin.json`, `cq/skills/cq/SKILL.md`, `cq/commands/reflect.md`, `cq/commands/status.md` | Manifest read; corresponding SDK skill/reflection copies read; copy-equality check inspected in CI source, not executed. Plugin copies/status remain available for direct inspection. |
| `ruff.toml` | Excluded: Python lint configuration | No Python lint-policy assessment. |
| `schema/` | Included: knowledge-unit, operation, scoring, review, discovery contracts; Go/Python package wrappers and fixtures/tests | Tree and README structure searched; detailed schema constraints not yet assessed. |
| `scripts/` | Excluded: docs-site preparation and lint wrappers, with their tests | No docs publishing or lint-tooling correctness assessment; these are not knowledge-state drivers. |
| `sdk/` | Included: `go/client.go`, local stores, `remote.go`, `discovery/`, `prompts/`, `scoring.go`, `stores/postgres/`; Python `src/cq/` clients, stores, prompts, reflection, scoring, discovery and tests | Go client fully read; SQLite reload, Python store selection/persistence, reflector, shared prompts and API surfaces inspected. PostgreSQL/discovery surfaces searched; algorithm and cross-language parity details remain to inspect. `go/ttl/ttl.go` read: API-key duration utility, not knowledge expiry. |
| `server/` | Included: `backend/src/cq_server/` entry point, routes, services, repositories, auth, migrations and optional semantic retrieval; `frontend/src/` review/auth/dashboard callers; `scripts/` maintenance and seeding; component tests and container build | App, knowledge route/services, review service, DB wrapper, repository persistence/query path, semantic enablement, browser review path, maintenance/seed source and SQLite smoke test inspected. Detailed auth, migration, frontend API and semantic ranking internals remain available. |

All source-dependent coverage entries refer to SRC-1 at the paths shown. No material shipped knowledge-loop responsibility is deliberately excluded. Remaining file-level inspection is work for later analysis, not unavailable evidence and not a claim of exhaustive correctness review.

### Frozen evidence and limits

The only frozen source is the acquired repository at full commit **5765494a3840e5f5a7223c42101f41e85cb9d898**. The checkout HEAD matched that pin and its status was clean when inspected. The applicability cutoff is **2026-10-14**, the supplied run date; it does not imply evidence about changes after the commit. The overall tier is **code-grounded** because the boundary follows executable entry points, state persistence/reload and review/retrieval consumers. Source-native documentation supplies intent separately from code behavior.

External dependencies include the consuming agents and their model providers, MCP transport/library, database engines, web/framework/package dependencies and an optional remote embedding service. CQ's semantic-search module enables embedding integration when `TOKEN_EMBEDDING_URL` and its dependencies are available; the server DB wrapper rejects enabled semantic search on its PostgreSQL backend. The embedding provider implementation and weights are outside this repository. Consequently this run cannot establish their semantic quality, latency or reliability. SRC-1: `server/backend/src/cq_server/semsearch/__init__.py`, `server/backend/src/cq_server/core/db.py`.

Live `cq.exchange`, external host runtimes, dependency source repositories, model services and linked external announcements are excluded from the frozen evidence set. This prevents conclusions about hosted service tenancy, deployed behavior, host compliance with the skill, or end-to-end learning benefit. No target execution, tests, examples, models or services were run. No observed execution trace or causal experiment was supplied. Test source and demonstration seed content cannot establish operational effectiveness. Architecture documentation is retained as doctrine/design, including its prospective mechanisms; later jobs must not substitute those declarations for implementation evidence. SRC-1: `README.md`, `docs/architecture.md`, `server/scripts/seed-kus.py`, `cli/mcpserver/e2e_test.go`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/mozilla-ai/cq` | 5765494a3840e5f5a7223c42101f41e85cb9d898 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/cq-8fb3dc41c334/related-systems/mozilla-ai--cq`. Implementation: tracked tree, `cli/main.go`, `cli/cmd/cli.go`, `cli/cmd/mcp.go`, `cli/mcpserver/server.go`, `cli/internal/install/pi.go`, `cli/internal/hook/cursor.go`, `sdk/go/client.go`, SQLite/Python persistence excerpts, SDK PostgreSQL/discovery API surfaces, server app/knowledge route/services/repository/DB/semantic enablement, frontend review, maintenance/seeding scripts and test source named above. Doctrine/design: `README.md`, `docs/architecture.md`, `sdk/go/prompts/SKILL.md`, `sdk/go/prompts/reflect.md`, component/schema surfaces. | Implementation: [CLI entry](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/cli/main.go), [client](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/sdk/go/client.go), [server entry](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/server/backend/src/cq_server/app.py), [review driver](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/server/frontend/src/pages/ReviewPage.tsx). Doctrine/design: [skill](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/sdk/go/prompts/SKILL.md), [reflection](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/sdk/go/prompts/reflect.md), [architecture](https://github.com/mozilla-ai/cq/blob/5765494a3840e5f5a7223c42101f41e85cb9d898/docs/architecture.md). Other commit-relative anchors appear in the boundary and coverage table. | No checkout access gap encountered. Implementation limits: source inspection only, no run artifacts or test results; cannot establish deployed behavior, host adherence or learning efficacy. Doctrine/design limits: declarations can be prospective or disagree with current code; cannot independently establish implementation or safety guarantees. External hosts, embedding provider and hosted deployment are not frozen sources. |
