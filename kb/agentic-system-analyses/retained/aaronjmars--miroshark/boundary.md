---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MiroShark's shipped simulation application, embedded Wonderwall runtime and graph-memory stack at e95d3d8c2a2206b8b6695648e8504cf23436d3de."
run-id: AAS-2026-10-15-miroshark-b3df0e053a29-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: e95d3d8c2a2206b8b6695648e8504cf23436d3de
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/aaronjmars/MiroShark
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-miroshark/related-systems/aaronjmars--MiroShark
  revision: e95d3d8c2a2206b8b6695648e8504cf23436d3de
  sha256: null
---

# MiroShark boundary

## Boundary and evidence

This run covers MiroShark as a shipped application for building document-derived agent populations, running social-media and prediction-market simulations, and consuming their retained results through reports, interviews and retrieval. Its intended analytical use is to explain the source-native runtime and state loop, not to establish that simulated outcomes predict real populations. The declared pipeline includes graph build, agent setup, simulation, reporting and interaction (SRC-1, `docs/ARCHITECTURE.md`).

The target class is **enclosing runtime**. MiroShark is not merely the graph-storage API or a client of a separately shipped simulation service: its server selects and launches shipped simulation drivers; those drivers create agents, supply context, advance environments and collect actions. The bundled Wonderwall package and graph-memory stack are internal mechanisms of this target. The shell launcher, browser client, HTTP CLI and stdio MCP server are also shipped paths, not excluded enclosing applications (SRC-1, `miroshark`, `backend/run.py`, `backend/app/__init__.py`, `backend/cli.py`, `backend/mcp_server.py`, `backend/app/services/simulation_runner.py`, `backend/scripts/run_parallel_simulation.py`).

The server's driver selection makes the ownership boundary explicit:

> if platform == "twitter":
>     script_name = "run_twitter_simulation.py"
> --- `backend/app/services/simulation_runner.py`

> elif platform == "polymarket":
>     script_name = "run_parallel_simulation.py"
> --- `backend/app/services/simulation_runner.py`

The parallel driver supplies the model-dependent action loop rather than returning a one-shot computation:

> async def _step_twitter(active_agents=active):
>     actions = {agent: LLMAction() for _, agent in active_agents}
>     await twitter_result.env.step(actions)
>     return active_agents
> --- `backend/scripts/run_parallel_simulation.py`

The agent obtains an environment observation and passes the resulting user message into its model-driven step (SRC-1, `backend/wonderwall/social_agent/agent.py`):

> response = await self.astep(user_msg)
> tool_calls_data = []
> for tool_call in response.info['tool_calls']:
> --- `backend/wonderwall/social_agent/agent.py`

### Functional scope and initial loop trace

The boundary kind is **whole-system**: it includes state producers, maintenance paths, admission/configuration, execution and later consumers, rather than isolating the embedded runtime. The following paths establish that functional scope; they are initial inspection anchors, not a file allowlist.

- **Input admission and graph production:** browser requests reach graph API routes; project management retains uploaded/extracted text and metadata; graph construction calls storage ingestion. Storage ingestion obtains the graph ontology, extracts entities and relations and embeds their text (SRC-1, `frontend/src/api/graph.js`, `backend/app/api/graph.py`, `backend/app/models/project.py`, `backend/app/services/graph_builder.py`, `backend/app/storage/neo4j_storage.py`).
- **Graph-to-agent consumption:** simulation preparation reads defined graph entities with edges, instantiates the profile generator with storage and graph ID, and supports real-time profile files. Configuration and profile reload paths remain included; they are not external fixtures (SRC-1, `backend/app/services/simulation_manager.py`, `backend/app/services/wonderwall_profile_generator.py`).
- **Prompts and maintenance:** the locale registry and shipped prompt packages, round-memory compaction, belief updates, cross-platform context and optional graph-memory updates all belong to the target. The parallel driver's post-round path records fetched actions, updates beliefs and compacts memory for subsequent rounds (SRC-1, `backend/app/prompts/registry.py`, `backend/app/prompts/locales/en/profile_generator.py`, `backend/scripts/run_parallel_simulation.py`, `backend/scripts/round_memory.py`, `backend/app/services/graph_memory_updater.py`).
- **Retained state and later use:** action logs feed report tools; report metadata and Markdown are saved and reloaded; optional reasoning traces are initialized through graph storage. Browser interaction reloads reports, profile data and action history. The stdio MCP server directly exposes graph search, community construction/browsing and retained report reasoning (SRC-1, `backend/app/services/report_agent.py`, `frontend/src/components/Step5Interaction.vue`, `backend/mcp_server.py`).
- **Other shipped control paths:** single-platform drivers, environment-only interview reload, branch/counterfactual preparation, simulation API control, MCP tool integration, publishing and export services remain inside the boundary. Initial inspection traced driver selection and parallel execution, reload/branch preparation, API call sites and MCP storage dispatch; it did not exhaustively assess each auxiliary route (SRC-1, `backend/app/services/simulation_runner.py`, `backend/app/services/simulation_manager.py`, `backend/app/api/simulation.py`, `backend/scripts/run_parallel_simulation.py`, `backend/mcp_server.py`).
- **Evaluators:** backend tests, script-based pipeline probes, CI and root deployment smoke tooling are included as source evidence about checks, not as successful executions. Initial inspection includes the stub-backed Camel compatibility test, CI job definitions and deployment smoke-test source (SRC-1, `backend/tests/test_smoke_camel_agent.py`, `.github/workflows/tests.yml`, `scripts/smoke_test.py`).

Two retained-state connections illustrate why this is not a storage-only boundary. The graph updater writes simulated activity back through ingestion:

> self.storage.add_text(
>     self.graph_id,
>     combined_text,
>     valid_at=valid_at,
>     kind=edge_kind,
>     source_type="agent",
>     source_id=source_id,
> )
> --- `backend/app/services/graph_memory_updater.py`

The report consumer reads the simulation's persisted per-platform actions:

> actions_path = os.path.join(sim_dir, platform, "actions.jsonl")
> --- `backend/app/services/report_agent.py`

### Top-level coverage

All tracked top-level entries are classified below from the pinned Git tree (SRC-1). **Included** means eligible for this whole-system analysis, not that every line has been inspected. Directory rows name material subpaths. **Excluded** means a deliberate functional exclusion, not inaccessible evidence. No material shipped loop path was unavailable. Files explicitly marked not yet inspected are available; no behavioral conclusion is drawn from their contents here.

| Top-level tracked entry | Coverage, material paths and role | Initial inspection / exclusion consequence |
|---|---|---|
| `.dockerignore` | Included: deployment packaging context | Tree inventoried; content not yet inspected; no packaging-completeness claim. |
| `.env.example` | Included: configuration contract | Tree inventoried; content not yet inspected; no claim that every flag or secret setting was assessed. |
| `.github/` | Included: `.github/workflows/tests.yml`, `docker-image.yml`, README translations, contribution/security and dependency-maintenance material | Tests workflow inspected; other contents inventoried, not yet inspected. CI source does not establish passing runs. |
| `.gitignore` | Included: retained/generated-file policy | Tree inventoried; content not yet inspected; no ignore-policy correctness claim. |
| `.x402books/` | Excluded: `.x402books/wallets.json` wallet metadata | Deliberate exclusion; no wallet ownership, funding or payment-operation conclusion. |
| `CLAUDE.md` | Included: shipped developer/agent guidance, treated only as target evidence | Inventoried, not yet inspected; no claim about its instructions' operational enforcement. |
| `Dockerfile` | Included: application image construction | Inventoried, not yet inspected; no image build or production parity claim. |
| `Dockerfile.railway` | Included: managed-deployment image construction | Inventoried, not yet inspected; no managed-image correctness claim. |
| `ECOSYSTEM.md` | Included: declared integration context | Inventoried, not yet inspected; no corroboration of third-party operation. |
| `LICENSE` | Excluded: legal terms | Deliberate exclusion; no licensing/legal assessment. |
| `README_DEPLOYMENT.md` | Included: deployment instructions | Inventoried, not yet inspected; no runbook validation claim. |
| `backend/` | Included: `run.py`, `cli.py`, `mcp_server.py`; `app/api/` admission/control/read surfaces; `app/models/` project/task retention; `app/services/` graph construction, persona/config production, simulation manager/runner, graph-memory updater, report/graph tools, exports and publishers; `app/storage/` ingestion/retrieval/maintenance/reasoning; `app/prompts/`, `app/utils/`, `app/countries/`, `app/preset_templates/`; `scripts/run_parallel_simulation.py`, single-platform drivers and memory/belief/director/MCP bridges; `wonderwall/environment/`, `social_agent/`, `social_platform/`, `simulations/` and SQL schemas; `tests/`, pipeline test scripts; manifests, lockfile, OpenAPI and run instructions | Entry points and representative end-to-end state paths inspected as listed above. Single-platform and auxiliary paths remain included for further inspection; full route, locale, schema and test coverage is not claimed. |
| `cloudbuild.yaml` | Included: build/deployment wiring | Inventoried, not yet inspected; no cloud-build success claim. |
| `cloudrun.env.yaml.example` | Included: deployment configuration | Inventoried, not yet inspected; no Cloud Run configuration-completeness claim. |
| `docker-compose.ollama.yml` | Included: local-provider deployment variant | Inventoried, not yet inspected; no variant parity claim. |
| `docker-compose.traefik.yml` | Included: proxy deployment variant | Inventoried, not yet inspected; no proxy/security claim. |
| `docker-compose.yml` | Included: application, Neo4j, Ollama and persistence mounts | Inspected; supports declared service/mount wiring only, not running deployment behavior. |
| `docs/` | Included: `ARCHITECTURE.md`, API/CLI/MCP/configuration/model/deployment/demographic/integration documentation and translations; `plans/` and `cleanup/` as attributed target-authored records; images only where explanatory | Architecture inspected; other material inventoried, not yet inspected. Documentation intent is distinct from executable behavior. No adoption of target-authored audit conclusions as established facts. |
| `frontend/` | Included: `src/api/graph.js`, `simulation.js`, `report.js` and other HTTP clients; `src/components/Step1GraphBuild.vue` through `Step5Interaction.vue`; `src/views/` simulation/report/replay/interaction clients; router, stores, settings, public worker/assets and build configuration | Graph/simulation/report clients and interaction reload path inspected/read or searched; full UI and service-worker behavior not yet inspected. Shipped client responsibilities remain in scope. |
| `miroshark` | Included: local setup/start/stop/status launcher | Inspected; launches backend and frontend and manages local Neo4j startup. |
| `miroshark-nobg.png` | Excluded: root brand image | Deliberate exclusion; no visual-branding assessment. |
| `package-lock.json` | Included: root dependency resolution | Inventoried, not yet inspected; no dependency integrity assessment. |
| `package.json` | Included: root backend/frontend orchestration scripts | Inspected; corroborates the shipped application entry points. |
| `railway.env.example` | Included: managed-deployment configuration | Inventoried, not yet inspected; no complete deployment-setting assessment. |
| `railway.json` | Included: managed-deployment wiring | Inventoried, not yet inspected; no deployment-success claim. |
| `render.yaml` | Included: managed-deployment wiring | Inventoried, not yet inspected; no Render operation claim. |
| `ruff.toml` | Included: static checking policy | Inventoried, not yet inspected; no lint-result claim. |
| `scripts/` | Included: `smoke_test.py`, `synthetic_seed.py`, `scan_i18n.py`, `deploy_cloudrun.sh`: deployment checks, seed utility, localization check and deployment helper | Smoke source inspected and localization CI consumer inspected; remaining scripts not yet inspected. No executed evaluation or deployment claimed. |

### Frozen evidence and external limits

The only frozen source is SRC-1 at full commit `e95d3d8c2a2206b8b6695648e8504cf23436d3de`; checkout HEAD was verified against the supplied acquisition pin. The applicability cutoff is **2026-10-15**, the supplied run date. It is not a claim that upstream activity after this commit was searched or that the checkout represents the latest upstream release. The overall evidence tier is **code-grounded**, with target-authored architecture and prompt text supplying declared design alongside implementation.

External dependencies are not additional frozen sources: Neo4j, model/embedding providers (including the illustrated Ollama deployment), Camel, numerical/retrieval libraries and external MCP hosts/services are outside this repository's implementation boundary. Their shipped adapters and configuration remain included. The backend manifest explicitly bundles Wonderwall while depending on Camel (SRC-1, `backend/pyproject.toml`):

> # Wonderwall (wonderwall package) is bundled directly in backend/wonderwall/
> # "camel-oasis==0.2.5",  # replaced by bundled Wonderwall
> "camel-ai==0.2.90",
> --- `backend/pyproject.toml`

No dependency repositories, provider outputs, deployed databases, live web enrichment, remote demographic datasets or external publication services were captured. These access limits prevent conclusions about dependency internals, actual model decisions, factual grounding supplied remotely, live integration reliability and deployed retention. No target code, tests, examples or service calls were executed. Test and architecture descriptions therefore support only attributed design/check intent; they do not establish observed runs, predictive validity, cost, latency or causal effects. The deliberate exclusions in the coverage table do not remove any identified simulation or graph-memory state-loop responsibility.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/aaronjmars/MiroShark` | e95d3d8c2a2206b8b6695648e8504cf23436d3de | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-miroshark/related-systems/aaronjmars--MiroShark`. Implementation: full tracked-tree inventory; `miroshark`, `package.json`, `backend/run.py`, `backend/app/__init__.py`; bounded reads/searches of `backend/cli.py`, `backend/mcp_server.py`, `backend/app/api/graph.py`, `backend/app/api/simulation.py`, `backend/app/api/report.py`, `backend/app/models/project.py`, `backend/app/services/graph_builder.py`, `backend/app/services/simulation_manager.py`, `backend/app/services/simulation_runner.py`, `backend/app/services/graph_memory_updater.py`, `backend/app/services/report_agent.py`, `backend/app/services/graph_tools.py`, `backend/app/storage/neo4j_storage.py`, `backend/scripts/run_parallel_simulation.py`, `backend/scripts/round_memory.py`, `backend/wonderwall/social_agent/agent.py`, `backend/wonderwall/environment/env.py`, prompt registry, browser graph/simulation/report clients and Step5 interaction; `backend/pyproject.toml`, `docker-compose.yml`, `.github/workflows/tests.yml`, `backend/tests/test_smoke_camel_agent.py`, `scripts/smoke_test.py`. Doctrine/design: `docs/ARCHITECTURE.md`, `backend/app/prompts/locales/en/profile_generator.py`, inline contracts in these files. | Implementation: [server](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/backend/app/__init__.py), [runner](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/backend/app/services/simulation_runner.py), [simulation driver](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/backend/scripts/run_parallel_simulation.py), [storage](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/backend/app/storage/neo4j_storage.py), [report retention/consumption](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/backend/app/services/report_agent.py). Doctrine/design: [architecture](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/docs/ARCHITECTURE.md), [persona prompt](https://github.com/aaronjmars/MiroShark/blob/e95d3d8c2a2206b8b6695648e8504cf23436d3de/backend/app/prompts/locales/en/profile_generator.py). | No inaccessible tracked path identified. Initial inspection is not exhaustive; further files at this same commit remain eligible. Dependency internals, remote content and actual runtime artifacts were not captured; no observed-run or causal-experiment layer. This prevents execution-success, predictive-performance, latency/cost and externally grounded correctness conclusions. |
