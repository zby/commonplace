# Evidence packet — run AGS-2026-08-20-SWAMP-01

This is the frozen evidence packet for one agentic-system analysis run. Lens
workers consume this file plus targeted read-only reads inside the frozen
boundary. Lens workers must not reacquire, refresh, or widen sources, must not
change the revision, and must not create their own ID namespace.

## Run identity

- Run/result ID: `AGS-2026-08-20-SWAMP-01`
- Target system: Swamp (`github.com/swamp-club/swamp`), the `swamp` CLI
- Analysis cutoff: 2026-08-20
- Staging identity: `kb/work/multistage-write-analyse-agentic-system-20260820/trials/swamp/`

## Boundary declaration

Swamp is scoped in as an **agent operating layer**: a deterministic execution,
state, and instruction-supply substrate whose entire product framing is that an
external model-calling agent drives it (`README.md:7-11` "Deterministic
Automation for AI Agents… Built for agents"; `design/agent.md:1-6` "The primary
method for working with swamp is through an AI agent"). Swamp's shipped runtime
contains no LLM SDK (`deno.json` import map has no model-provider dependency);
the model calls sit in an external harness. The boundary is therefore drawn by
function, and the model-calling actor is an **external dependency, not an
inspected component**.

### Included (inspected)

Components whose scheduling, context selection, retained state, action
execution, checking, acceptance, or authority decisions produce or constrain the
behavior under review:

- CLI dispatch and command surface (`src/cli/`, `main.ts`)
- Workflow engine — DAG scheduling, jobs/steps, parallel groups, foreach,
  approvals (`src/domain/workflows/`, `src/serve/`, `src/worker/`)
- Model/definition system and method execution drivers — the external action
  boundary (`src/domain/models/`, `src/domain/definitions/`,
  `src/infrastructure/process/`, `src/infrastructure/http/`)
- Datastore and data layer — retained state, versioning, tags, namespaces, sync
  (`src/domain/datastore/`, `src/domain/data/`, `src/infrastructure/persistence/`)
- CEL expression evaluation and inputs resolution — context selection into
  definitions (`src/infrastructure/cel/`, `src/domain/expressions/`,
  `src/domain/inputs/`)
- Validation, doctor, freshness/staleness machinery — checking
  (`src/domain/audit/doctor/`, `swamp model validate`)
- Vaults, secrets, access control — authority constraints on runs
  (`src/domain/vaults/`, `src/domain/access/`, `src/domain/secrets/`)
- Audit subsystem — ingestion of the external agent's tool-use events and
  read-back timeline (`src/domain/audit/`, `src/cli/commands/audit.ts`)
- Skill and instruction installation into agent harness directories — the
  context-supply path to the model-calling actor (`src/domain/repo/repo_service.ts`,
  bundled skill assets, `swamp repo init|upgrade`, `swamp update`, `swamp agent setup`)
- Reports — post-execution derived artifacts (`src/domain/reports/`)
- Telemetry, tracing, harness detection (`src/domain/telemetry/`,
  `src/infrastructure/telemetry/`, `src/infrastructure/tracing/`)
- Remote execution and dispatch (`src/domain/remote/`)

### Excluded (named, not inspected)

- **The external AI coding harness** (Claude Code, Cursor, Codex, OpenCode,
  Copilot, Kiro) — where the model calls, agent turn loop, and tool selection
  actually happen. Out of the reviewed repository entirely.
- **The swamp-club backend** — extension registry, auth server, quest backend,
  telemetry ingest. Closed and not in this checkout.
- **Published extension packages** (e.g. `@swamp/s3-datastore`) — distributed
  separately; only the in-repo extension contract is inspected.
- **Swamp's own development harness** (`/.claude/`, `/.agents/`,
  `/agent-constraints/`, `/.github/workflows/`, `/scripts/`, `/evals/`) — this is
  the process that *produces* swamp, not the deployed system's runtime. Citable
  for provenance of bundled artifacts, never as deployed-runtime evidence.
- The hosted manual at `swamp-club.com/manual` — not fetched in this run.

### Boundary consequence

This is a whole-system boundary **for swamp**, and a partial boundary for the
composite agent loop (harness + swamp). Any conclusion about end-to-end agent
behavior — what the model actually does with delivered instructions, how it
selects swamp commands, whether it re-reads audit output — is out of boundary
and must be reported as such.

## Source register

| ID | Kind | Identity / location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps |
|---|---|---|---|---|---|---|---|
| SRC-01 | Git checkout, implementation | `/home/zby/llm/commonplace/related-systems/swamp-club--swamp` (`github.com/swamp-club/swamp`) | `cf38c4ec1068613bb7d3432eb74a1ad854156dd7`, authored 2026-07-17, branch `main`, working tree clean (0 dirty files) | `implementation` | `src/`, `main.ts`, `deno.json`, `packages/` | file path + line number | Binary never executed; no run observed |
| SRC-02 | In-repo design docs | `design/*.md` in SRC-01 | same revision | `doctrine/design` | all 27 files listed; several read in full | file path + line number | Some docs mark features planned/aspirational; see per-claim flags |
| SRC-03 | Product doctrine | `README.md`, `CLAUDE.md`, `CONTRIBUTING.md` in SRC-01 | same revision | `doctrine/design` | read in full (README, CLAUDE.md) | file path + line number | Marketing framing, not behavior evidence |
| SRC-04 | Tests | `integration/*_test.ts`, `src/**/*_test.ts` in SRC-01 | same revision | `implementation` (asserted behavior, not an observed run) | targeted reads | file path + line number | Not executed in this run; assertions are code, not observations |
| SRC-05 | Development-harness config | `/.claude/`, `/.agents/`, `/agent-constraints/`, `/.github/workflows/`, `/scripts/`, `/evals/` in SRC-01 | same revision | `doctrine/design` | targeted reads | file path + line number | Out of boundary as deployed-runtime evidence |

### Global access gaps

- No observed run and no causal experiment: the binary was not compiled or
  executed, no swamp repo was initialized, no workflow was run.
- The external harness is not inspected, so no evidence exists in this run for
  what the delivered skills or audit output do to model behavior.
- The swamp-club backend is not inspectable; every claim about registry, auth,
  quest, or telemetry-server behavior is client-side only.
- Boundary is ~1 month older than the analysis cutoff (HEAD 2026-07-17 vs cutoff
  2026-08-20) in a repository averaging ~270 commits/month, so the analysis may
  lag current `main` substantially.

## Vocabulary binding for lens workers

Use the run's conclusion statuses exactly: `absent`, `inapplicable`,
`uninspected`, `claimed`, `implemented`, `observed`, `causally supported`.
Nothing in this run can be `observed` or `causally supported` — there is no run
evidence and no experiment. Never upgrade context presence to activation,
implementation to deployment, observation to causality, or operational
continuation to warrant. Every negative or uncertain finding names the inspected
boundary and the exact conclusion it prevents.
