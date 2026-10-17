---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Pal's shipped personal knowledge application and its state lifecycle at commit 6516b8ede0c085e48f39f3bd04cb85b475a855dc."
run-id: AAS-2026-10-17-pal-e313a0902289-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/agno-agi/pal
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-pal/related-systems/agno-agi--pal
  revision: 6516b8ede0c085e48f39f3bd04cb85b475a855dc
  sha256: null
---

# Pal boundary

## Boundary and evidence

This run analyses Pal as the shipped personal knowledge application, not merely its wiki tool API. Its intended use is to retain personal information, gather sources, compile a wiki, retrieve retained content, and reuse operational learnings. The target class is **memory/knowledge/context-engineering system**. It qualifies as agentic because its shipped leader and specialist agents configure model calls and tools to perform these operations. The **whole-system** boundary includes the application server, scheduled and direct callers, agent prompts, retained-file scaffolds, database configuration, synchronization, and evaluation drivers. The underlying Agno runtime is a dependency, not a separately reviewed target. [SRC-1: `docs/SPEC.md`, `pal/team.py`, `pal/agents/navigator.py`, `app/main.py`]

The classification rests on both declared purpose and executable wiring:

> Pal is a personal knowledge agent that learns how you work and builds a compounding knowledge base.
> --- `docs/SPEC.md`

> pal = Team(
>     id="pal",
>     name="Pal",
>     mode=TeamMode.coordinate,
>     model=OpenAIResponses(id="gpt-5.4"),
> --- `pal/team.py`

The initial trace follows these material state paths, all within SRC-1:

- **Admit and produce:** `app/router.py` exposes direct text/URL ingestion through `pal/tools/ingest.py`; the Researcher also receives ingest tools through `pal/tools/build.py`. Ingest writes raw documents and the manifest. Leader delegation and the Researcher's conditional availability are part of the application, not an excluded host. [SRC-1: `app/router.py`, `pal/tools/ingest.py`, `pal/tools/build.py`, `pal/agents/researcher.py`, `pal/team.py`]
- **Maintain:** Compiler instructions direct raw-to-summary/concept compilation and manifest/index/state updates; Linter instructions direct wiki inspection and a retained lint report. Their model-driven steps are prompt contracts, not evidence that a run completed them. Concrete manifest/index/state writes are supplied by the custom tools. [SRC-1: `pal/agents/compiler.py`, `pal/agents/linter.py`, `pal/tools/ingest.py`, `pal/tools/wiki.py`]
- **Reload and consume:** `context/load_context.py` inserts compact file metadata into the routing knowledge store. The reload route and scheduled context-refresh call it. Navigator receives wiki-index, manifest, file, SQL and knowledge tools; its instructions prioritize wiki retrieval and reuse learnings. The leader and Navigator configure memory/history/session search. [SRC-1: `context/load_context.py`, `app/router.py`, `app/main.py`, `pal/agents/navigator.py`, `pal/instructions.py`, `pal/team.py`]
- **Persist and refresh:** `db/session.py` supplies PostgreSQL and PgVector knowledge stores; shared settings bind the agents to them. Startup initializes optional context Git sync, the leader is instructed to chain Syncer after file changes, and startup schedules periodic pull. These are distinct paths; a direct ingest route is not assumed to traverse the leader's sync chain. [SRC-1: `db/session.py`, `pal/agents/settings.py`, `pal/tools/git.py`, `pal/agents/syncer.py`, `pal/team.py`, `app/main.py`, `app/router.py`]
- **Evaluate:** the unified evaluator calls the actual team, while smoke drivers preserve session IDs across dependent cases. The extended driver can clear raw/wiki content before its knowledge pipeline suite. These are included shipped consumers and state mutators, not observed results. [SRC-1: `evals/run.py`, `evals/smoke.py`, `evals/extended_smoke.py`, `evals/cases/wiki.py`]

The reload mechanism explicitly distinguishes routing metadata from document content:

> Writes compact `File:` metadata entries into `pal_knowledge` for retrieval
> routing. Does not ingest raw document contents — FileTools reads those on
> demand from the context directory.
> --- `context/load_context.py`

The consumption contract makes later use of retained wiki content explicit:

> 1. Read the wiki index (`read_wiki_index`) first — scan for relevant articles
> 2. Pull specific concept articles or summaries via `read_file` as needed
> --- `pal/instructions.py`

### Top-level coverage

Every top-level tracked file or directory is classified below. “Included” establishes functional scope, not a claim that every line has already been inspected. Initial inspection traced the material loop above, read the canonical specification and repository agent guide, and searched the remaining documentation, context scaffolds, scripts and evaluation surfaces for entry points and responsibilities. Ancillary details not yet read in full remain available under SRC-1; they are not access gaps.

| Top-level tracked path | Classification | Material paths and role | Inspection or exclusion limit |
|---|---|---|---|
| `.dockerignore` | Included | Build-context filtering | Initially searched; no build executed. |
| `.github/` | Included | `.github/workflows/validate.yml`, development validation workflow | Tree inventoried; workflow body not yet inspected. No CI-success conclusion. |
| `.gitignore` | Included | Local generated-file and secret exclusions | Initially searched; not evidence that deployed secrets are protected. |
| `CLAUDE.md` | Included | Shipped development/maintenance instructions and architecture map | Read as source-native doctrine, not binding worker instructions. |
| `Dockerfile` | Included | Container entry point, Git credentials configuration, dependency installation | Read; image build and credential behavior not observed. |
| `LICENSE` | Excluded | Legal license | No licensing interpretation; no state-loop responsibility excluded. |
| `README.md` | Included | Setup, context bootstrap, user interfaces and operating guidance | Initially searched; setup success not established. |
| `app/` | Included | `main.py` AgentOS wiring, Slack interface, lifespan and schedules; `router.py` reload/ingest/compile/lint/pull callers; `config.yaml` UI prompts; package initializer | Main and router read; UI prompt details not yet inspected. Server and callers are within target. |
| `compose.yaml` | Included | API startup, PostgreSQL service, context mounts and environment | Read; no deployment tested. |
| `context/` | Included | `load_context.py`; `about-me.md`, `preferences.md`; `voice/{email,x-post,slack-message,document}.md`; `templates/{meeting-notes,project-brief,weekly-review}.md`; `meetings/`, `projects/`; `raw/.manifest.json`; `wiki/index.md`, `.state.json`, `concepts/`, `summaries/`, `outputs/`; package initializer and directory placeholders | Loader, preferences, manifest, wiki index/state read; other prompt/template headings searched. Tracked wiki and manifest are empty scaffolds, not a populated operational KB. |
| `db/` | Included | `session.py` SQL schema/knowledge factories, `url.py` connection configuration, `__init__.py` exports | Factory read and URL entry point searched; database contents unavailable. |
| `docs/` | Included | `SPEC.md` design; `GOOGLE_AUTH.md`, `SLACK_CONNECT.md` integration setup; `TEST_CASES.md` manual acceptance prompts | Specification read, other guides initially searched. Design declarations are not execution evidence. |
| `evals/` | Included | `__main__.py` and `run.py`; `cases/{security,routing,governance,knowledge,voice,wiki}.py`; `smoke.py`, `extended_smoke.py`, `test_load_context.py`; initializers | Unified runner/registry and wiki cases read; smoke state/session runner paths read; remaining test surfaces searched. No tests executed or scores established. |
| `example.env` | Included | Configuration/credential template | Tree inventoried; full template not yet inspected. No actual deployment configuration inferred. |
| `pal/` | Included | `team.py`; `agents/{navigator,researcher,compiler,linter,syncer,settings}.py`; `instructions.py`; `tools/{build,ingest,wiki,knowledge,git}.py`; `config.py`, `paths.py`, package initializers | Team, agents, prompts, tools, configuration and settings read; path constant searched. This includes prompt-based maintenance and memory settings, not only tool implementations. |
| `pyproject.toml` | Included | Package discovery, dependencies, development tool configuration | Read; dependency implementation is outside this repository. |
| `railway.json` | Included | Production server start command and deployment configuration | Start command searched; deployment not observed. |
| `requirements.txt` | Included | Deployment dependency versions | Tree inventoried; exact lock details not yet inspected. No dependency-version behavior inferred. |
| `scripts/` | Included | `entrypoint.sh`; `google_auth.py`; `build_image.sh`, `generate_requirements.sh`, `venv_setup.sh`; `railway_{up,env,redeploy}.sh`; `format.sh`, `validate.sh` | Entrypoint read; other script roles/entry points searched. OAuth and deployment setup remain included, without claims of successful execution. |

All table roles and traced paths refer to SRC-1 at the reviewed commit. The only deliberate repository exclusion is the license's legal interpretation. No material shipped runtime or retained-state path is deliberately excluded.

### Frozen evidence and limits

The evidence boundary is repository `https://github.com/agno-agi/pal` at **6516b8ede0c085e48f39f3bd04cb85b475a855dc**, accessed read-only at the acquired absolute checkout path. HEAD matched the supplied revision and the working-tree status was clean when inspected. The applicability cutoff is **2026-10-17**, the supplied run date; it is not a claim that source behavior was deployed or observed on that date. Overall evidence is **code-grounded**, supplemented by source-native doctrine/design. No target code, examples, tests or services were executed.

External dependencies include Agno/AgentOS and its learning, session, scheduler, authentication and tool implementations; OpenAI generation and embeddings; PostgreSQL/pgvector; Exa MCP and Parallel; optional Google and Slack services; Git/GitHub context storage; and container/Railway infrastructure. This boundary includes Pal's integration/configuration code but not those external implementations or live service contents. Their absence prevents conclusions about dependency-internal algorithms, actual model decisions, service guarantees, deployed authorization, synchronization success, or production reliability. User databases, remote context repositories and live sessions were not supplied, so the run cannot establish durable reuse in practice or measured improvement over time. [SRC-1: `pyproject.toml`, `db/session.py`, `pal/tools/build.py`, `pal/tools/ingest.py`, `pal/tools/git.py`, `pal/config.py`, `app/main.py`, `Dockerfile`, `compose.yaml`]

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/agno-agi/pal` | 6516b8ede0c085e48f39f3bd04cb85b475a855dc | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-pal/related-systems/agno-agi--pal`. Implementation: `app/main.py`, `app/router.py`, `context/load_context.py`, `db/session.py`, `pal/team.py`, `pal/agents/`, `pal/tools/`, `pal/instructions.py`, `pal/config.py`, `evals/run.py`, smoke runner paths and wiki cases, deployment wiring. Doctrine/design: `docs/SPEC.md`, `CLAUDE.md`, agent instruction strings, `context/preferences.md`; scoped searches of README, integration guides, templates/voice guides, tests and scripts. Tree coverage is recorded above; initially listed paths are not an allowlist. | Implementation: [team](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/team.py), [application](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/app/main.py), [routes](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/app/router.py), [loader](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/context/load_context.py), [tool assembly](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/tools/build.py), [evaluations](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/evals/run.py). Doctrine/design: [specification](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/docs/SPEC.md), [retrieval instructions](https://github.com/agno-agi/pal/blob/6516b8ede0c085e48f39f3bd04cb85b475a855dc/pal/instructions.py). | No repository access gap found. External dependencies, live service state, user databases and remote context contents are outside the frozen source. No supplied observed-run trace or causal experiment; executable eval drivers establish test design, not passing results or operational effectiveness. |
