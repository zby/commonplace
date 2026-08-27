# Canonical records — run AGS-2026-08-20-SWAMP-01

Orchestrator-owned. Lenses **extend by ID** and never rename, re-inventory, or
re-number. Any new material object or route returns to the orchestrator for one
canonical ID. All citations are paths inside `SRC-01` unless marked otherwise.

## Components (`CMP-*`)

| ID | Component | Anchor | Notes |
|---|---|---|---|
| CMP-01 | CLI dispatcher (Cliffy command tree, 26 top-level groups) | `main.ts:40-69`, `src/cli/mod.ts:1429-1457` | Entry point for every in-boundary action |
| CMP-02 | libswamp operation layer (AsyncIterable event streams, `Context`) | `src/libswamp/`, `design/libswamp.md:29-45` | All orchestration; presentation-agnostic |
| CMP-03 | Workflow execution service (DAG, jobs, steps, levels) | `src/domain/workflows/execution_service.ts`, `topological_sort_service.ts:1-223` | Owns level-parallel execution |
| CMP-04 | Workflow scheduler (cron, `croner`) | `src/domain/workflows/workflow_scheduler.ts:44-118` | Pure registration layer; `onFire` callback |
| CMP-05 | Method execution / step executor | `src/domain/models/method_execution_service.ts`, `execution_service.ts` | In-process execution on loopback or worker |
| CMP-06 | Pre-flight check engine | `design/models.md:346-498` | Guards mutating methods; bypassable |
| CMP-07 | Datastore + unified data repository (filesystem default, extension backends) | `src/domain/datastore/`, `src/infrastructure/persistence/unified_data_repository.ts`, `design/datastores.md:12-52` | Versioned-immutable artifact store |
| CMP-08 | SQLite data catalog | `.swamp/data/_catalog.db`, `design/data-query.md:240-300` | Index over artifact versions incl. provenance |
| CMP-09 | Run tracker (SQLite `active_runs`) | `.swamp/run_tracker.db`, `design/run-tracker.md:14-72` | In-flight lifecycle, heartbeat, reaping |
| CMP-10 | CEL evaluator — three sealed surfaces | `src/infrastructure/cel/cel_evaluator.ts`, `grant_condition_environment.ts`, `design/expressions.md:10-42` | Internal / extension-facing / grant-condition |
| CMP-11 | Validation service (`swamp workflow validate`, `swamp model validate`) | `src/domain/workflows/validation_service.ts:1-640` | Pre-run structural checking |
| CMP-12 | Doctor subsystem (`audit`, `extensions`, `vaults`, `secrets`, `datastores`, `workflows`, `install`) | `src/domain/audit/doctor/`, `design/audit-doctor.md:23-61` | Preflight diagnostics with actionable hints |
| CMP-13 | Audit subsystem — per-tool hook normalizers, JSONL repo, timeline service | `src/domain/audit/hook_input.ts:1-263`, `src/infrastructure/persistence/jsonl_audit_repository.ts`, `src/domain/audit/audit_service.ts:119-235` | Records the *external agent's* tool calls |
| CMP-14 | Vault service + providers + read-access audit | `src/domain/vaults/`, `design/vaults.md:311-390` | Secret resolution, optional read trail |
| CMP-15 | Access control (grants, tokens, principals) | `src/domain/access/`, `grants/*.yaml` | Authorization for `swamp serve` |
| CMP-16 | Repo service — scaffolding, skill/instruction/hook installation | `src/domain/repo/repo_service.ts` | The context-supply installer for CMP-22 |
| CMP-17 | Reports engine | `src/domain/reports/report.ts`, `report_context.ts`, `design/reports.md:1-120` | Deterministic post-execution derivation |
| CMP-18 | Extension system (types, vaults, datastores, reports; registry pull/push, trust) | `src/domain/extensions/`, `src/libswamp/extensions/`, `design/extension.md` | Third-party code loading |
| CMP-19 | `swamp serve` orchestrator (HTTP/WS control plane + HTTP/2 data plane) | `src/serve/`, `design/remote-execution.md:49-76` | Owns DAG, datastore, vaults, scheduler, tokens |
| CMP-20 | Remote worker + dispatch runner | `src/worker/`, `src/domain/remote/`, `design/remote-execution.md:505-573` | Credential-free compute; 14-verb capability proxy |
| CMP-21 | Telemetry, OTEL tracing/logs, harness detection | `src/domain/telemetry/agent_harness_detection.ts`, `src/infrastructure/telemetry/`, `src/infrastructure/tracing/` | Anonymous usage events + optional OTLP |
| CMP-22 | **External AI coding harness** (Claude Code, Cursor, Codex, OpenCode, Copilot, Kiro) | out of boundary | Where the model calls and turn loop live; `uninspected` |
| CMP-23 | **swamp-club backend** (registry, auth, telemetry ingest, quest) | out of boundary | `telemetry.swamp-club.com`, `swamp-club.com` (`src/cli/mod.ts:1013`) |
| CMP-24 | Summarise service (repo activity aggregation) | `src/domain/summary/summary_service.ts`, `src/libswamp/summary/summarise.ts` | Deterministic; **no LLM** |

## Operative objects (`OBJ-*`)

| ID | Object | Representational form | Substrate | Anchor |
|---|---|---|---|---|
| OBJ-01 | Model type (metadata, attributes, methods, inputs as Zod/JsonSchema) | symbolic (TypeScript) | binary built-ins + extension packages | `design/models.md:15-30`, `src/domain/models/model.ts` |
| OBJ-02 | Model definition | symbolic (schema-validated YAML + CEL) | git-tracked `models/{type}/{id}.yaml` | `design/repo.md:76-77` |
| OBJ-03 | Workflow definition (DAG of jobs/steps) | symbolic (YAML + CEL) | git-tracked `workflows/workflow-{id}.yaml` | `design/workflow.md`, `design/repo.md:78` |
| OBJ-04 | Evaluated definition / evaluated workflow | symbolic (materialized post-CEL YAML) | datastore `definitions-evaluated/`, `workflows-evaluated/` (gitignored) | `design/expressions.md:554-566` |
| OBJ-05 | Data artifact (resource or file), versioned-immutable, auto-tagged | mixed (structured resource / raw file bytes) | `.swamp/data/{type}/{modelId}/{name}/{version}/` + `latest` marker | `design/models.md:499-562` |
| OBJ-06 | Catalog row (one per artifact version, with provenance fields) | symbolic (SQLite row) | `.swamp/data/_catalog.db` | `design/data-query.md:250-300` |
| OBJ-07 | Model output record (`ModelOutput`) | symbolic (YAML, write-once terminal) | `.swamp/outputs/…` | `design/repo.md:211`, `design/run-tracker.md:9-18` |
| OBJ-08 | Workflow run record (status, step states, captured inputs on suspend) | symbolic (YAML) | `.swamp/workflow-runs/…` | `design/repo.md:212`, `design/workflow.md:168-181` |
| OBJ-09 | Active-run row (pid, hostname, heartbeat, status) | symbolic (SQLite row) | `.swamp/run_tracker.db` | `design/run-tracker.md:22-56` |
| OBJ-10 | Agent tool-use audit row | symbolic (JSONL record) | `.swamp/audit/commands-YYYY-MM-DD.jsonl` | `design/audit.md:16-22` |
| OBJ-11 | Vault read-access audit row | symbolic (JSONL record) | `.swamp/audit/vault-reads-YYYY-MM-DD.jsonl` | `design/vaults.md:328-355` |
| OBJ-12 | Report artifact (markdown + JSON) | mixed | persisted as data artifacts | `design/reports.md:1-30` |
| OBJ-13 | **Bundled skill corpus** — `swamp` (121-line SKILL.md + routing table + ~1.1 MB `references/` tree) and `swamp-getting-started` (126-line prose state machine) | natural-language (prompt-path) | compiled into the binary; written to harness skill dirs | `.claude/skills/swamp/SKILL.md:1-121`, `.claude/skills/swamp-getting-started/SKILL.md:1-126` |
| OBJ-14 | Per-repo instructions file (`CLAUDE.md`, `AGENTS.md`, `.cursor/rules/swamp.mdc`, `.kiro/steering/…`) | natural-language (prompt-path) | repo working tree | `design/repo.md:15-17`, `design/global-skills.md:286-298` |
| OBJ-15 | Harness hook config (`.claude/settings.local.json`, `.cursor/hooks.json`, `.kiro/hooks/*`, `.opencode/plugins/*`, `.github/hooks/`) | symbolic (JSON/TS config) | harness config files in repo | `design/audit.md:41-58` |
| OBJ-16 | `.swamp.yaml` repo marker (version, enrolled tools, datastore, trust, logLevel, migration timestamps) | symbolic (YAML) | repo root | `design/repo.md:12-13,45-48`, `design/global-skills.md:230-235` |
| OBJ-17 | Global skill-dir registries | symbolic (JSON array of paths) | `~/.config/swamp/builtin-tool-skill-dirs.json`, `custom-tool-skill-dirs.json` | `design/global-skills.md:137-181` |
| OBJ-18 | Vault + secret (plus annotations, sensitive-field marks) | mixed | provider-backed (`local_encryption`, AWS SM, 1Password) | `design/vaults.md:21-110` |
| OBJ-19 | Grant (subject, effect, actions, resource, CEL condition) | symbolic (YAML + sealed CEL) | `grants/*.yaml` reconciled into store | `design/repo.md:79-83` |
| OBJ-20 | Manual-approval gate record (`prompt`, timeout, decidedBy) | symbolic (field on OBJ-08) | run record | `design/workflow.md:114-186`, `design/models.md:304-345` |
| OBJ-21 | Worker-pool bookkeeping models (`worker`, `enrollment-token`, `step-lease`, `pending-dispatch`, `fleet-probe`) | symbolic (built-in model data — same substrate as OBJ-05) | datastore | `design/remote-execution.md:400-441` |
| OBJ-22 | Extension bundle + fingerprinted bundle cache | symbolic (JS bundle) | pulled extensions dir + worker cache | `design/remote-execution.md:675-716`, `design/extension.md` |
| OBJ-23 | Telemetry event (`cli_invocation`, redacted) | symbolic (JSON) | local spool → `telemetry.swamp-club.com` | `README.md:394-427`, `src/cli/mod.ts:1013` |
| OBJ-24 | Deferred CLI warnings (superseded skills, local-skill shadowing, staleness) | natural-language | emitted to terminal, debounced via OBJ-16 | `design/repo.md:54-70`, `design/global-skills.md:206-223`, `src/cli/mod.ts:962-1009` |
| OBJ-25 | **Harness permission grant** — 27 pre-approved `Bash(swamp …:*)` entries in `.claude/settings.local.json`; Kiro `kiroAgent.trustedCommands: ["swamp *"]`; Kiro `chat.defaultAgent: "swamp"` and its 7-tool agent definition | symbolic (JSON config) | harness config in repo, gitignored for Claude | `src/domain/repo/repo_service.ts:1349-1379,1549-1556,1906-1910,1971-2017` |
| OBJ-26 | CLI schema document — `swamp help`, hidden, "Output full CLI schema for AI agent consumption", always JSON | symbolic (JSON) | generated on demand from the Cliffy tree | `src/cli/commands/help.ts:43-75`, `src/cli/cli_schema.ts:22-120` |
| OBJ-27 | Structured remediation payloads — `CheckResult.hint`, `nextSteps`, `SensitiveArgRemediation.expression`, stable error `code` catalogue, `skillWarning.message` | natural-language inside symbolic fields | JSON renderer output | `src/domain/audit/doctor/check.ts:54-63`, `src/presentation/renderers/repo_init.ts:42-52,200`, `src/domain/models/sensitive_field_extractor.ts:309-362`, `src/presentation/renderers/extension_pull.ts:104-115` |
| OBJ-28 | Extension-installed skills (third-party natural-language instructions fanned into every enrolled tool's repo-local skill dir) | natural-language (prompt-path) | repo-local per-tool skill dirs | `src/libswamp/extensions/pull.ts:1057-1058`, warning at `src/presentation/renderers/extension_pull.ts:104-115` |

## Routes (`RTE-*`)

Runtime owns endpoints and progression. Memory and epistemic lenses **annotate**.

### Control routes

| ID | Route | Next-step owner | Decision policy + form |
|---|---|---|---|
| RTE-01 | external agent or human → shell → `swamp <cmd>` → CMP-01 → CMP-02 | **CMP-22 (external model)** for which command runs; CMP-01 for dispatch | model-resolved from natural-language instruction (OBJ-13/OBJ-14); `uninspected` inside CMP-22 |
| RTE-02 | workflow YAML → topological sort → level-parallel job/step execution | CMP-03 | deterministic DAG order + `concurrency` caps; symbolic |
| RTE-03 | cron expression → CMP-04 `onFire` → workflow run | CMP-04 | cron pattern; symbolic |
| RTE-04 | `manual_approval` step → run suspends → approve/reject → resume | human operator via CLI, **or** a model method via `context.approveWorkflowGate` | explicit human/programmatic act; `decidedBy` auto-stamped |
| RTE-05 | ready step → dispatch scheduler → loopback executor or remote worker | CMP-19 scheduler | direct target → label selector → platform → least-loaded; symbolic |
| RTE-06 | method `followUpActions` → `continueCondition(dataHandles)` predicate → further method invocations, with `delayMs` and `maxRetries` | CMP-05 | extension-authored TypeScript predicate; depth-capped at 100 (`src/domain/models/model.ts:607-630`, `method_execution_service.ts:63,976-1078`). The **only** retry mechanism in the system — the DAG level has none |
| RTE-07 | pre-flight checks → pass/fail → method proceeds or aborts | CMP-06 | code predicates; bypassable via `--skip-checks*` |
| RTE-25 | inbound webhook → HMAC verification → bounded queue (depth 100) → serialized drain → workflow run | CMP-19 | route match + per-scheme signature check; symbolic (`src/serve/webhook.ts:298,343,406-416`, `webhook_verifiers.ts:38-52`) |
| RTE-26 | nested `workflow` step → child `WorkflowExecutionService.run()` | CMP-03 | depth cap 10, cycle detection by workflow name (`execution_service.ts:2797-2985`) |

### Context routes

| ID | Route | Direction | Selection signal |
|---|---|---|---|
| RTE-08 | bundled skills + instructions files → harness global/repo dirs → **model context** | push (installed), then pull (harness loads on description match) | harness-side description matching, then routing table inside OBJ-13 |
| RTE-09 | CLI output (`log` or `--json` renderers, doctor hints, deferred warnings) → terminal → model context | pull (the agent reads what it invoked) | whatever command the model ran |
| RTE-10 | CEL expression in OBJ-02/OBJ-03 → CMP-10 → data / vault / env / file values inlined into the evaluated artifact (OBJ-04) | pull | author-written expression, evaluated at definition-evaluation time |
| RTE-11 | inputs resolution (CLI `--input`, `--input-file`, stdin, workflow inputs, resume inputs) → expression context | push | declared inputs, strict: undeclared reference fails |
| RTE-12 | `swamp data get/query/search`, `data.*` CEL receivers, `context.readModelData` → CMP-08 catalog → artifact bytes | pull | explicit CEL predicate over validated field set; no implicit scoping |

### State routes

| ID | Route | Read/write | Anchor |
|---|---|---|---|
| RTE-13 | method `writeResource` / `createFileWriter` / `writeLine` → immediate durable versioned write (+ catalog row) | write | `design/remote-execution.md:719-736` |
| RTE-14 | run lifecycle: register → heartbeat (30 s) → complete/suspend → reap stale (>90 s) | write | `design/run-tracker.md:38-56` |
| RTE-15 | harness `postToolUse` hook → `swamp audit record --from-hook` → normalizer → JSONL append | write | `design/audit.md:16-40` |
| RTE-16 | `swamp audit` → timeline service (noise filter, swamp-vs-direct split, sentinel filter) → rendered timeline | read-back | `src/domain/audit/audit_service.ts:32-137` |
| RTE-17 | `swamp summarise` → aggregation over method executions, workflow runs, data in a time window | read-back | `src/libswamp/summary/summarise.ts` |
| RTE-18 | `VaultService.get()` → optional audit-read append | write | `design/vaults.md:322-333` |
| RTE-19 | data GC / `swamp run gc` / lifetime + `garbageCollection` policies → deletion | write (decay) | `design/repo.md:108-132`, `design/models.md:530-541` |
| RTE-20 | `swamp repo init|upgrade|update|agent setup` → write skills/instructions/hooks + register skill dirs (OBJ-17) → later `swamp update` reads registry and re-syncs | write, then read-back | `design/global-skills.md:120-181` |
| RTE-21 | datastore sync (S3 pull before / push after each command; file lock or S3 conditional-write lock) | read+write | `README.md:220-227`, `design/datastores.md:298+` |
| RTE-22 | telemetry spool → `telemetry.swamp-club.com` | write (external) | `README.md:388-450` |
| RTE-27 | `swamp workflow validate` / `swamp model validate` → structural + schema + reference conformance verdict | check | `src/domain/workflows/validation_service.ts:1-640`, `design/models.md:490-497` |
| RTE-28 | `swamp doctor audit` → five ordered checks incl. the end-to-end recording smoke test → pass/fail/skip + hint | check on the evidence channel itself | `design/audit-doctor.md:23-61` |
| RTE-29 | extension resolve → `trustedCollectives` / `trustMemberCollectives` → silent auto-resolution or refusal | disposition/admission | `design/repo.md:100-107` |
| RTE-30 | `latest` marker resolution vs. pinned `(dataId, version)` | lineage/freshness | `design/remote-execution.md:750-772` |
| RTE-31 | `swamp help` → full CLI schema JSON → external model | context (machine-facing self-description) | `src/cli/commands/help.ts:43-75` |

### Action routes

| ID | Route | Executor | Boundary |
|---|---|---|---|
| RTE-23 | model method → external API / CLI / SDK (subprocess `Deno.Command`, outbound HTTP, AWS cloudcontrol) | in-process on loopback executor or remote worker | inherits the invoking shell's environment and credentials (`README.md:70-75`); isolation is a worker deployment property, not a per-step field (`design/execution-drivers.md:1-12`) |
| RTE-24 | extension pull/push against the swamp-club registry, gated by `trustedCollectives` auto-resolve | CMP-18 | crosses into CMP-23 |

## Behavioral-authority paths (`BAP-*`)

Each record fixes **consumer / channel / force**, plus this run's `horizon`.

| ID | Object | Consumer | Channel | Force | Horizon |
|---|---|---|---|---|---|
| BAP-01 | OBJ-13 bundled `swamp` skill | CMP-22 external model | harness skill discovery, description-matched, progressive disclosure | advisory instruction — the model may ignore, and swamp cannot detect that it did | every session in any repo where the harness sees the global skill dir, until the next sync |
| BAP-02 | OBJ-13 `swamp-getting-started` prose state machine | CMP-22 external model | same | advisory sequencing instruction ("do not advance until Verify passes") | one onboarding session |
| BAP-03 | OBJ-14 per-repo instructions file | CMP-22 external model | harness auto-load of `CLAUDE.md`/`AGENTS.md`/rules file | advisory | every session in that repo |
| BAP-04 | OBJ-15 hook config | harness hook runner (deterministic code, inside CMP-22) | harness config file | binding on the harness — it executes the command; non-binding on the model | every matching tool call in that repo |
| BAP-05 | OBJ-01 + OBJ-02 type schema and definition | CMP-05 / CMP-11 | file read + Zod validation | binding — invalid definitions are rejected | every method run and validation |
| BAP-06 | OBJ-03 workflow definition | CMP-03 | file read + `validation_service` | binding — execution follows the declared DAG | every run of that workflow |
| BAP-07 | OBJ-19 grant with sealed CEL condition | CMP-15 inside CMP-19 | authorization check on each served request | binding — permits or blocks | lifetime of the grant; reconciled on serve start and `access reload` |
| BAP-08 | OBJ-20 approval gate | CMP-03 | run record state | binding gate — the run stays suspended until decided | one suspended run |
| BAP-09 | pre-flight checks (CMP-06) | CMP-05 | in-process call before mutating methods | binding **unless** the caller passes `--skip-checks` / `--skip-check` / `--skip-check-label` | one method invocation |
| BAP-10 | OBJ-24 deferred warnings + doctor hints | human operator and CMP-22 | terminal output | advisory | one invocation |
| BAP-11 | `trustedCollectives` in OBJ-16 | CMP-18 | config read on extension resolve | binding — decides silent auto-resolution vs. refusal | until the config changes |
| BAP-12 | 14-verb capability protocol | CMP-20 worker | ws control plane + h2 data plane | binding — an unlisted member fails loudly with `UnsupportedOnRemoteWorkerError` | every remote dispatch under the negotiated `protocolVersion` |
| BAP-13 | OBJ-25 harness permission grant | the harness's permission system (deterministic, inside CMP-22) | config file written by `swamp repo init` | **permissive** — pre-authorizes 27 `swamp` command patterns (Claude) or all `swamp *` (Kiro), removing the per-call human checkpoint | that repo, until the settings file changes; gitignored, so per developer |
| BAP-14 | OBJ-28 extension-shipped skills | CMP-22 external model | fanned into every enrolled tool's repo-local skill dir on `extension pull` | advisory instruction of **third-party** origin; swamp emits a review-before-use warning but does not gate installation | until the extension is removed |

## Claims (`CLM-*`) — orchestrator namespace, epistemic lens owns truth/scope/warrant fields

| ID | Claim, as the system states or embodies it | Source |
|---|---|---|
| CLM-01 | "Deterministic Automation for AI Agents" — swamp makes agent-produced operational automation "reviewable, shareable, and accurate" | `README.md:7-11` |
| CLM-02 | Swamp has 1:1 models of external APIs/CLI tools "which it can then validate are correct" | `design/high-level.md:5-7` |
| CLM-03 | A stored data artifact represents the state of an external resource ("Resources … represent external resource state, API responses") | `design/models.md:505-509` |
| CLM-04 | The vault read-access trail proves "which automation read which secret, when" for "security posture verification in autonomous agent fleets" | `design/vaults.md:313-315` |
| CLM-05 | `doctor audit` makes silent breakage of the agent-activity record surface loudly instead of silently | `design/audit-doctor.md:11-22` |
| CLM-06 | Everything is reviewable in `.swamp/` "before anything touches production" | `README.md:40-41` |
| CLM-07 | Applications, environments, and drift detection are aspirational and not implemented | `design/high-level.md:20-23` |
| CLM-08 | Quest event emission and the bingo board are designed but not present in the codebase | `design/quests.md:59-61,155-157,193` |
| CLM-09 | The "everything is the datastore / agents work on their own head" unification is an exploration, not a contract in force | `design/unification.md:18-41` |
