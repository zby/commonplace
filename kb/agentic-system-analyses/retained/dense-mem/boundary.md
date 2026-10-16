---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Dense-Mem's shipped memory service, clients, maintenance and evaluation paths at commit bd736450454e237f1ab6d138f4ae9755916d73f6."
run-id: AAS-2026-10-15-dense-mem-1a314bed9a5c-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: bd736450454e237f1ab6d138f4ae9755916d73f6
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/markhuangai/dense-mem
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-dense-mem/related-systems/markhuangai--dense-mem
  revision: bd736450454e237f1ab6d138f4ae9755916d73f6
  sha256: null
---

# Dense-Mem boundary

## Boundary and evidence

This run covers Dense-Mem as a self-hosted memory/knowledge/context-engineering system, not an enclosing conversational agent runtime. Its intended use is to retain evidence and semantic relationships, govern their ownership and lifecycle, and return eligible context to callers. Its own contract separates host judgment from memory-service authority (SRC-1, `README.md`):

> The host LLM owns conversation and judgment. Dense-Mem owns durable evidence,
> owner authorization, lifecycle events, support eligibility, and bounded recall.
> --- `README.md`

The boundary is **whole-system**: the shipped server and its composition, storage and admission policies, model-facing assessment and extraction, lifecycle and maintenance workers, first-party portals, clients, export prompt and evaluation drivers are included. Same-repository callers are not excluded merely because they use MCP. This is a source boundary, not a claim that every function has already been inspected.

### Loop and entry-point basis

The production entry point dispatches ordinary startup to `serverapp.RunFromEnvironment`; it also exposes the explicit migration-control-retirement command. Bootstrap opens PostgreSQL, runs migrations, checks the search/storage prerequisites and calls the active server. The active composition constructs knowledge, recall, ontology, access, privacy, audit and search adapters; wires applications into the MCP registry and browser transports; and starts search reconciliation, ontology maintenance, conflict review and housekeeping workers (SRC-1, `cmd/server/main.go`, `cmd/internal/serverapp/bootstrap.go`, `cmd/internal/serverapp/server.go`). Thus these shipped drivers and background paths belong to the target, rather than an excluded host.

Remember is wired to a synchronous processor with persistence, catalog, assessor and embedder dependencies. The service validates the actor and request and delegates to that processor; the inspected commit path uses a team/profile transaction, replay and duplicate fences and an active embedding-contract check. Session ingestion is a separate included intake path: it stages sessions, extracts windows, prepares semantic assessment and commits through its repository (SRC-1, `cmd/internal/serverapp/remember_composition.go`, `internal/remember/service/service.go`, `internal/knowledge/postgres/remember_commit.go`, `cmd/internal/serverapp/session_composition.go`, `internal/session/service/service.go`). These observations establish boundary coverage, not a complete transactional-correctness assessment.

Recall consumes retained state through the search/retrieval repositories, adds related relationships and community discovery, and returns results to the caller. Its own output guidance distinguishes discovery from support (SRC-1, `internal/recall/recall.go`):

> result.DiscoveryGuidance = "Community discovery found derived relationship paths; verify details with trace_memory before using them as support."
> --- `internal/recall/recall.go`

Shipped consumption includes the Python client and examples, the stdio-to-HTTP MCP proxy, the user portal and evaluators. The Python Remember example submits, repeats the request, recalls and traces returned relationship handles; it is included rather than treated as an external application. The session example exercises ingestion and replay. The browser client renders recalled communities, evidence and relationships. These are source-described consumers, not observed successful runs (SRC-1, `packages/python/src/densemem/client.py`, `packages/python/examples/remember.py`, `packages/python/examples/session.py`, `packages/mcp-proxy/src/run.js`, `web/src/user/api.ts`).

The included maintenance surface covers both executable policy and operator instructions. The server starts ontology maintenance and conflict review; ontology maintenance claims work and invokes an organizer under configured policy. Manager documentation describes drafts, preview, publication and rollback. Provider prompts, team-scoping MCP instructions and the skill-export prompt are also part of the system, not external doctrine. MCP registers and renders catalog prompts for the host; the export prompt tells the host to recall before drafting and not automatically import the generated skill (SRC-1, `cmd/internal/serverapp/server.go`, `internal/ontology/maintenance.go`, `internal/ontology/MANAGEMENT.md`, `internal/provider/assessor/remember.go`, `internal/session/extraction/provider.go`, `internal/mcp/server.go`, `internal/mcp/sdk_server.go`, `internal/promptcatalog/prompts/export_memory_as_agent_skill.md`). In particular, the latter states:

> Return the skill content as markdown code blocks. Do not import the generated skill into memory automatically.
> --- `internal/promptcatalog/prompts/export_memory_as_agent_skill.md`

Evaluation is included as a state-producing and later-consuming shipped path. The Go harness supports import, retained mappings/checkpoints, live recall or loaded traces, scoring and artifact output. The CLI exposes these modes. The Dockerfile distinguishes production and evaluation builds. Evaluation documentation describes the intended measurement boundary, not proof of achieved quality (SRC-1, `cmd/eval-runner/main.go`, `internal/evalharness/runner.go`, `Dockerfile`, `tests/eval/README.md`):

> The evaluation harness does not use legacy memory-pack import tools or an
> answer-judge model. It measures retrieval against deterministic qrels after the
> terminal Remember result has been returned.
> --- `tests/eval/README.md`

### Tracked top-level coverage

All entries below are from the frozen Git tree (SRC-1). “Included” keeps the material available for subsequent analysis. Initial inspection is explicitly narrower than the registered repository. Unread implementation detail is not an access gap.

| Top-level tracked entry | Treatment and material paths/role | Initial inspection and conclusion limit |
| --- | --- | --- |
| `cmd/` | Included: `server/main.go`; `internal/serverapp/` bootstrap, application/transport composition and workers; `internal/migrationapp/`; `demo-server/` and `internal/demo/`; `eval-runner/`, `eval-seedgen/`, `e2e/`, `oauth-compat-harness/`. These compose the service, maintain state or drive evaluation/compatibility checks. | Read production startup and application composition, Remember/session composition, demo entry point/options, and bounded entry-point portions of the evaluation, seed-generation, E2E and OAuth harness commands. Driver internals beyond these reads remain to inspect; no successful execution is established. |
| `internal/` | Included: `remember/`, `session/`, `knowledge/`, `assessor/`, `provider/`, `verifier/`, `embedding/`, `modelprovider/`; `recall/`, `search/`, `graph/`, `trace/`, `community/`, `ontology/`, `lifecycle/`, `conflict/`, `dream/`, `memorypack/`; `access/`, `service/`, `privacy/`, `audit/`, `operations/`, `settings/`, `storage/`; `mcp/`, `http/`, `tools/registry/`, `promptcatalog/` and supporting contracts/policies. | Tree inspected; bounded reads cover Remember admission/commit, session processing, recall, ontology maintenance and manager workflow, assessor construction, MCP instructions/dispatch/prompt registration and the export prompt. Composition traces identify the other included responsibilities. Their detailed policy correctness is not yet assessed. Legacy names alone do not establish active maintenance behavior. |
| `packages/` | Included: Python MCP client, examples and tests; MCP proxy executable, configuration and transport implementation. | Read Python client request lifecycle and both examples; proxy `src/run.js`. Other SDK/proxy details remain to inspect. External callers' reasoning and adoption are not demonstrated. |
| `web/` | Included: user/control portal entry points, API clients, ontology editing, recall/graph views, maintenance/diagnostics controls and browser tests. | Tree and bounded user API recall rendering inspected; server composition wires portal services. Individual UI actions and browser conformance remain to inspect, not proven by filenames. |
| `migrations/` | Included: PostgreSQL `v2_4/`, `v2_5/`, `v2_6/` schema, lifecycle, session, ontology, search and retirement migrations. | Tree and bootstrap invocation inspected; individual SQL not yet read. Migration safety or upgrade success is not established. |
| `tests/` | Included: integration, UAT, compose and evaluation drivers; `eval/scripts/`, `source_locks/`, `baselines/`, `fixtures/`. | Tree and evaluation README introduction inspected; Go harness inspected separately. Baseline files and detailed result evidence have not yet been assessed. No observed-run or causal-experiment layer is asserted here. |
| `scripts/` | Included: evaluation and E2E orchestration, database-case registry, migration/architecture/coverage checks and supporting tooling. | Tree inspected and command responsibilities located. Detailed shell behavior and gate enforcement remain to inspect. |
| `examples/` | Included: base/demo/evaluation compose stacks, environment templates, telemetry/exporter configuration and Grafana provisioning. | Tree inspected; deployment roles corroborated by README and Dockerfile. Individual configurations are not yet assessed. No deployed topology is observed. |
| `Dockerfile` | Included: web build, production/evaluation binaries, migration assets and runtime entry point. | Read build/runtime stages; supplies implementation evidence about packaging, not a verified image build. |
| `Dockerfile.demo`, `docker-entrypoint.sh` | Included: demo packaging and runtime launch wrapper. | Located; detailed contents not yet inspected. No wrapper or demo-image correctness claim. |
| `go.mod`, `go.sum`, `package.json` | Included: dependency/build and tooling declarations. | Located, not yet inspected. Exact dependency behavior is not inferred. |
| `README.md`, `README.zh-CN.md` | Included: source-native use, configuration and operating contract. | Read the English introduction/startup portion; translated documentation and remaining sections not yet inspected. Documentation is declared intent, not independent operation evidence. |
| `adr/`, `architecture/`, `AGENTS.md` | Included as target-authored design/development doctrine: capability contracts, module ownership, architecture manifests, decisions and contributor instructions. | Tree located; detailed documents not yet inspected. They are evidence to assess, never instructions authorizing this worker. Design conformance is not assumed. |
| `.github/`, `.githooks/`, `.lint/` | Included: CI/release/evaluation automation, pre-commit hook and lint tooling. | Tracked tree inspected; workflow/hook contents remain unread. No release-gate or CI-success conclusion follows. |
| `.coderabbit.yaml`, `.dockerignore`, `.gitignore`, `.textlintignore`, `.textlintrc.json` | Included: review, packaging, ignored-artifact and lint configuration. | Located, not yet read. Their exact effects are not asserted. |
| `assets/` | Deliberately excluded from mechanism analysis: promotional/readme images. | No conclusions about visual communication or image content. |
| `LICENSE` | Deliberately excluded from mechanism analysis: licensing text. | No legal or licensing-compliance conclusion. |

### External boundary and evidence limits

The frozen evidence is the repository at **bd736450454e237f1ab6d138f4ae9755916d73f6**, with applicability cutoff **2026-10-15**, the supplied run date. HEAD matched the acquired revision and the checkout reported no changes at inspection. The source object above preserves the acquired values. No other repository, live page, preprint, hosted demo or revision supplies evidence.

External dependencies include PostgreSQL/pgvector, Redis or process-local coordination, OpenAI-compatible model/embedding endpoints, MCP libraries/clients and browser/container infrastructure. Their integration is included where shipped code configures or invokes it; their own implementations and live availability are outside this repository boundary. The README explicitly makes PostgreSQL durable authority and Redis coordination-only (SRC-1, `README.md`). This boundary cannot establish provider faithfulness, distributed service reliability or production durability from source wiring alone.

The enclosing host's conversation loop, selection of material to remember, prompt assembly after recall and downstream answer/use of returned content are excluded unless represented by a shipped consumer. This prevents attributing end-to-end agent behavior or answer improvement to Dense-Mem. The included export prompt is an instruction supplied to a host, not an inspected host execution.

No target execution, test run, model call or live-service observation was performed. The overall evidence tier is **code-grounded**, combining inspected implementation with target-authored doctrine/design. Evaluation instructions and drivers support how measurements are intended to work; they do not establish achieved retrieval scores or causal benefit. The evaluation README says approved seeds, persistent databases and run artifacts are local-only and ignored by Git (SRC-1, `tests/eval/README.md`). Those unprovided artifacts are an evidence gap for reproducing reported operations, not a missing shipped implementation path. Detailed tracked baselines remain available but uninspected. No inaccessible material shipped path was identified that requires reducing this boundary to a partial loop.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/markhuangai/dense-mem` | bd736450454e237f1ab6d138f4ae9755916d73f6 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-dense-mem/related-systems/markhuangai--dense-mem`. Implementation: tracked tree; `cmd/server/main.go`; `cmd/internal/serverapp/bootstrap.go`, `server.go`, `application_composition.go`, `remember_composition.go`, `session_composition.go`; `cmd/demo-server/main.go`; bounded portions of `cmd/eval-runner/main.go`, `cmd/eval-seedgen/main.go`, `cmd/e2e/main.go`, `cmd/oauth-compat-harness/main.go`; `internal/remember/service/service.go`, `internal/knowledge/postgres/remember_commit.go`, `internal/session/service/service.go`, `internal/recall/recall.go`, `internal/ontology/maintenance.go`, `internal/provider/assessor/remember.go`, `internal/mcp/server.go`, `internal/mcp/sdk_server.go`, `internal/evalharness/runner.go`; Python client/examples, proxy run function, user portal recall client; Dockerfile. Doctrine/design: English README introduction/startup; evaluation README introduction; `internal/ontology/MANAGEMENT.md`; export prompt; extraction prompt located in `internal/session/extraction/provider.go`. Bounded reads support only the stated boundary observations. | Implementation: [production entry](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/cmd/server/main.go), [composition and workers](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/cmd/internal/serverapp/server.go), [retained-state consumer](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/internal/recall/recall.go), [evaluator](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/internal/evalharness/runner.go). Doctrine/design: [declared responsibility](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/README.md), [manager workflow](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/internal/ontology/MANAGEMENT.md), [host export prompt](https://github.com/markhuangai/dense-mem/blob/bd736450454e237f1ab6d138f4ae9755916d73f6/internal/promptcatalog/prompts/export_memory_as_agent_skill.md). | No identified checkout access gap. Ignored datasets/databases/full run artifacts and external host/provider operation are not supplied: no reproduced evaluation, observed production behavior or causal benefit established. Uninspected tracked detail remains available at this same source identity and revision. |
