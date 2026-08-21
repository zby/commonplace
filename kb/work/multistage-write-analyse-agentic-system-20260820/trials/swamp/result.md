# AGS-2026-08-20-SWAMP-01 — Agentic-system analysis: Swamp

Logical result of one `analyse-agentic-system` run. Physical layout: this file
plus `evidence-packet.md` (records 1–3 in full). IDs resolve across both.

---

## 1. Run / staging identity

- **Run/result ID:** `AGS-2026-08-20-SWAMP-01`
- **Staging identity:** `kb/work/multistage-write-analyse-agentic-system-20260820/trials/swamp/`
- **Publication:** withheld — see record 11.

## 2. System boundary, revision, evidence tier

- **System:** Swamp (`github.com/swamp-club/swamp`), the `swamp` CLI — an agent
  operating layer.
- **Revision:** `cf38c4ec1068613bb7d3432eb74a1ad854156dd7` (2026-07-17, `main`,
  clean tree). Analysis cutoff 2026-08-20.
- **Boundary:** full declaration in `evidence-packet.md` §Boundary. In brief:
  the shipped `swamp` runtime is in boundary; the external model-calling harness,
  the swamp-club backend, separately published extensions, and swamp's own
  development harness are named exclusions.
- **Overall evidence tier:** `code-grounded`. Every material loop in record 5
  rests on inspected implementation material under `src/`, with design docs used
  for intent and cross-checked against code. Nothing in this run reaches
  `observed` or `causally supported`: the binary was never executed.

## 3. Source register

Full register with evidence layers and access gaps: `evidence-packet.md`
§Source register (`SRC-01`…`SRC-05`).

---

## 4. Shared component / object / route / claim / authority records

Full register: `canonical-records.md` — `CMP-01`…`CMP-24`, `OBJ-01`…`OBJ-28`,
`RTE-01`…`RTE-31`, `BAP-01`…`BAP-14`, `CLM-01`…`CLM-09`. The orchestrator owns
every ID; lens sections below extend records by ID and never re-inventory them.
Records added mid-run, after the initial registration pass, are marked in place:
objects `OBJ-25`…`OBJ-28`, routes `RTE-25`…`RTE-31`, authority paths `BAP-13` and
`BAP-14`. The epistemic lens split `OBJ-05` into `OBJ-05a` (resource) and
`OBJ-05b` (file); that split is recorded in record 7B.2 and reconciled in record 8.

## 5. Runtime account

Swamp's deployed behavior is produced by a **split loop**: the model-calling half
sits in the external harness (`CMP-22`, uninspected), and the deterministic half
is swamp. Nothing in swamp's shipped runtime calls a language model — the import
map carries no model-provider dependency (`deno.json`), and no provider endpoint
appears anywhere under `src/` or `packages/` (verified by search over
`api.anthropic|api.openai|generativelanguage|bedrock|chat/completions`). `swamp
summarise` (`CMP-24`) is deterministic aggregation, not model summarization.

### Material loops

**L1 — the agent/CLI loop (`RTE-01`).** *Trigger:* a user request in the harness.
*Next-step owner:* `CMP-22`, the external model, decides which `swamp` command
runs. *Decision policy and its form:* natural language — the bundled skill corpus
(`OBJ-13`) and the per-repo instructions file (`OBJ-14`), resolved by the model.
*Context selection and framing:* the harness matches a skill description, loads a
121-line `SKILL.md` whose body is largely a routing table into a ~1.1 MB
`references/` tree, and pulls deeper files on demand (`RTE-08`). *State reads and
writes:* whatever the chosen command does. *Action executor and boundary:*
`CMP-01` → `CMP-02`. *Coordination and return:* renderers emit `log` or `--json`
back to the terminal, which is the model's next input (`RTE-09`). *Retry /
cancellation / recovery:* none in swamp — the model retries by issuing another
command. *Output:* exit code plus rendered stream. This loop's control decision is
`uninspected` inside `CMP-22`; swamp can shape it (`BAP-01`…`BAP-03`) but cannot
observe or enforce it.

**L2 — the workflow DAG loop (`RTE-02`).** *Trigger:* `swamp workflow run`, a cron
fire (`RTE-03`), a webhook (`RTE-25`), or a resume after approval. *Next-step
owner:* `CMP-03`, deterministically. *Decision policy and form:* symbolic —
topological sort over declared dependencies (`topological_sort_service.ts`),
executing each level with all jobs and steps concurrent unless a `concurrency`
cap applies; `forEach` expands one step template into N instances. Exactly three
step kinds exist (`step_task.ts:38,47,52`): `model_method`, nested `workflow`
(`RTE-26`, depth cap 10 at `execution_service.ts:313,2838`), and
`manual_approval`. There is no external-script step kind. *State:* the run record
(`OBJ-08`) plus a run-tracker row (`OBJ-09`). *Retry:* **none at DAG level** — the
system's only retry is `followUpActions` returned by a method (`RTE-06`).
*Recovery:* boot reconciliation sweeps stale leases, dispatches, and workers on
`swamp serve` start.

**L3 — the method execution loop (`RTE-23`).** *Trigger:* a `model_method` step or
`swamp model method run`. *Decision policy:* the model type's TypeScript. *Context
selection and framing:* CEL evaluation inlines vault secrets, other models' data,
env vars, and file contents into the definition, materializing `OBJ-04`
(`RTE-10`); inputs resolve strictly — an undeclared reference fails (`RTE-11`).
*Checking:* pre-flight checks run before mutating methods (`create`, `update`,
`delete`, `action`; unrecognized names default to mutating) and are bypassable via
`--skip-checks` (`skipAllChecks` is wired from both `workflow_run.ts` and
`model_method_run.ts`). *Action executor and boundary:* in-process on whichever
executor holds it — subprocess (`Deno.Command`, the shell model at
`src/domain/models/command/shell/shell_strategy.ts`), outbound HTTP, or the AWS
cloudcontrol SDK — inheriting the invoking shell's environment and credentials
(`README.md:70-75`). The `raw`/`docker` driver abstraction is **removed**;
isolation is now a worker deployment property (`design/execution-drivers.md:1-12`,
superseded). *Persistence:* writes are immediately durable, not staged — a method
that writes then throws leaves its data visible by design. *Output:* `DataHandle`s
plus a write-once terminal `ModelOutput` (`OBJ-07`).

**L4 — the fan-out loop (`RTE-05`).** *Trigger:* a ready step under `swamp serve`.
*Next-step owner:* the dispatch scheduler in `CMP-19`. *Policy:* direct target →
label selector → platform → least-loaded, queueing rather than failing. *Boundary:*
workers hold no repository, datastore, vault, or credentials; every side effect
returns through a closed 14-verb capability protocol (`BAP-12`), and any
uncovered member fails loudly with `UnsupportedOnRemoteWorkerError`. *Coordination:*
worker-initiated WebSocket control plane plus HTTP/2 data plane. Notably, the
control plane's own state (`OBJ-21`) is stored as ordinary versioned swamp data,
so pool state is queryable with the same primitive workflows already use.

**L5 — the observation loop (`RTE-15` → `RTE-16`).** *Trigger:* the harness's
`postToolUse` hook firing on the external agent's tool call. *Owner:* the harness
runs the hook (`BAP-04`); swamp normalizes four upstream payload shapes into one
`NormalizedHookInput` and appends a JSONL row (`OBJ-10`). *Read-back:* `swamp
audit` renders a merged timeline that splits swamp-mediated from direct commands
and filters a 43-prefix noise denylist plus the doctor sentinel
(`audit_service.ts:32-137`). *Recovery:* `swamp doctor audit` exercises every link
of the chain, because the chain breaks silently when an upstream tool changes its
contract.

### Conditional surfaces inspected, with materiality

- **Permissions and governance (`OBJ-25`, `BAP-07`, `BAP-13`)** — material because
  they set what the external model may do without asking. `swamp repo init` writes
  27 pre-approved `Bash(swamp …:*)` entries into `.claude/settings.local.json`
  (`repo_service.ts:1349-1379`) and `kiroAgent.trustedCommands: ["swamp *"]` for
  Kiro (`repo_service.ts:1549-1556`). Grant conditions for `swamp serve` evaluate
  in a permanently sealed CEL environment with no I/O receivers and
  `unlistedVariablesAreDyn: false`, so undeclared references fail at write-time.
- **Observability (`CMP-21`, `RTE-22`)** — material to evidence strength: OTEL
  traces and logs are opt-in, anonymous usage telemetry is on by default with
  positional args redacted.
- **Machine-facing output (`OBJ-26`, `OBJ-27`)** — material because it is the
  model's return channel: a hidden `swamp help` emits the full CLI schema as JSON
  "for AI agent consumption" (`help.ts:43-56`), and doctor hints, `nextSteps`, and
  a stable error-code catalogue carry remediation text addressed to the caller.
- **Third-party instruction loading (`OBJ-28`, `RTE-24`)** — material because it
  widens the prompt surface: `swamp extension pull` fans extension-shipped skills
  into every enrolled tool's skill dir and warns that they load into agent context
  and may contain executable scripts (`extension_pull.ts:100-118`).

Anti-conflation held throughout: the datastore is not a scheduler; retaining an
artifact is not selecting it into context; a CLI schema present in context is not
command execution.

## 6. Lens applicability records

**Memory / context lens.**
`{lens: memory/context, disposition: applicable, trigger evidence: RTE-12, RTE-16,
RTE-17, RTE-20, OBJ-04, OBJ-16, OBJ-17, OBJ-21, OBJ-22, inspected boundary: SRC-01
src/ + design/ at cf38c4e, rationale: multiple inspected paths carry material
accumulated or changed through use back into a later invocation or action — data
artifacts written by one run and read by a later definition through CEL, the
audit JSONL written from agent use and rendered by a later `swamp audit`, the
skill-dir registry written at repo init and read by a later `swamp update`, and
the evaluated-definition and bundle caches; action: run the lens, output in record
7A, prevented conclusions: none — the trigger is implemented, not merely claimed}`

**Epistemic lens.**
`{lens: epistemic, disposition: applicable, trigger evidence: CLM-01, CLM-02,
CLM-03, CLM-04, CLM-05, OBJ-05, OBJ-10, OBJ-11, OBJ-12, CMP-06, CMP-11, CMP-12,
inspected boundary: SRC-01 src/ + design/ at cf38c4e, rationale: material routes
handle truth-apt content — a stored resource asserts the state of an external
system, reports derive further propositions from run context, and two append-only
trails are produced as evidence about what an agent or automation did — and the
system makes consequential warrant claims ("accurate", "validate they are
correct", "proving which automation read which secret, when"); action: invoke the
epistemic procedure, output in record 7B, prevented conclusions: none}`

The direct-adaptation exception was checked and does not apply: no evaluated
behavior- or policy-adaptation route without a truth-apt object was found that
would have to be kept in the runtime account alone.

## 7A. Memory / context lens

Executed sequentially in the orchestrator context after the fresh lens workers
were terminated (see `trial-notes.md`, friction 4). Same frozen boundary, same
registers, no source widening.

### Retained operative parts

| ID | Storage substrate | Form | Persistence | Lineage | Producer → consumer | Invalidation / regeneration | Promotion path |
|---|---|---|---|---|---|---|---|
| OBJ-05 | datastore dir (local FS, external FS, or S3 via extension) | mixed: schema-checked resource, or raw file bytes | versioned-immutable; `latest` marker mutates | written by the owning definition's method from a live external call | method → later definitions via CEL, `swamp data`, reports, workers | `lifetime` (duration, `ephemeral`, `job`, `workflow`, `infinite`) + `garbageCollection` version caps; `autoGc` off by default | none — data never becomes a definition |
| OBJ-06 | SQLite `.swamp/data/_catalog.db` | symbolic rows | one row per artifact version, `is_latest` flag | derived index over OBJ-05 | write path → query path | rebuilt/migrated by `datastore migrate-index`; deletions cascade from GC | none |
| OBJ-04 | datastore `definitions-evaluated/`, `workflows-evaluated/` | symbolic YAML | cache, gitignored | CEL evaluation of OBJ-02/OBJ-03 against current data, vault, env | evaluator → executor | regenerated on evaluation; inputs changing invalidates | none |
| OBJ-07 | `.swamp/outputs/` | symbolic YAML | write-once, terminal state only | one per method invocation | executor → `swamp model output`, reports | `swamp run gc`, default 30 days, terminal only | none |
| OBJ-08 | `.swamp/workflow-runs/` | symbolic YAML | survives process restart | one per run; captures effective inputs **only on suspend** | executor → resume path, `workflow history`, reports | `swamp run gc`, 30 days, terminal only; running and suspended runs never deleted | none |
| OBJ-09 | SQLite `.swamp/run_tracker.db` | symbolic rows | in-flight only | registered at start, heartbeat every 30 s | executor → `run history`, `run doctor` | stale >90 s reaped (same host checks pid; cross-host TTL); terminal rows purged after 7 days | none |
| OBJ-10 | `.swamp/audit/commands-YYYY-MM-DD.jsonl` | symbolic rows | append-only, date-partitioned | normalized from four harness payload shapes | harness hook → `swamp audit` | 7-day default retention | none |
| OBJ-11 | `.swamp/audit/vault-reads-YYYY-MM-DD.jsonl` | symbolic rows | append-only, date-partitioned, opt-in per vault | one row per `VaultService.get()` | vault service → `vault audit-trail` | not inspected | none |
| OBJ-12 | persisted as data artifacts | mixed markdown + JSON | same as OBJ-05 | deterministic function over run context | report → human, `swamp report`, agent | inherits OBJ-05 policy | none |
| OBJ-16 | `.swamp.yaml` | symbolic YAML | git-tracked, long-lived | accumulated across `repo init`/`upgrade`/warnings | CLI → every later invocation | rewritten on upgrade; lazy migration normalizes legacy shapes | — |
| OBJ-17 | `~/.config/swamp/{builtin,custom}-tool-skill-dirs.json` | symbolic JSON array | user-global, additive union | accumulated from every repo the user ever initialized | `repo init`/`upgrade` → later repo-less `swamp update` | stale entries pruned when directories vanish; heuristic fallback if absent | — |
| OBJ-21 | datastore, as ordinary built-in model data | symbolic | versioned-immutable like OBJ-05 | every status flip is a new version | scheduler → scheduler, `data query`, reports | declared `garbageCollection` caps + periodic orchestrator GC; boot reconciliation rewrites stale states | — |
| OBJ-22 | worker-local bundle cache, keyed by fingerprint | symbolic JS bundle | disposable | fetched from orchestrator on miss | orchestrator → worker | fingerprint change; freshness test exists | — |
| OBJ-23 | local spool → `telemetry.swamp-club.com` | symbolic JSON | spooled then exported | one per CLI invocation | CLI → vendor backend (`CMP-23`) | not inspected beyond the client | — |
| OBJ-24 | terminal, debounced through OBJ-16 | natural-language | transient | computed per invocation from on-disk state | CLI → human and model | once-per-day debounce via `lastSkillMigrationWarning` | — |

**Explicitly retained state, not read-back.** `OBJ-13` (the bundled skill corpus)
and `OBJ-14` (instructions files) are static shipped material: they are written
from the binary, not accumulated from use, so their delivery into model context is
context supply, not memory read-back. `OBJ-28`, extension-shipped skills, is the
same category with a third-party producer. Calling any of these "memory" would be
exactly the upgrade the run's vocabulary forbids. `OBJ-17` is the interesting
edge: the *skill files* are static, but the *registry of where to install them* is
genuinely accumulated from use, and it is what makes a later repo-less `swamp
update` reach the right directories.

### Write side versus read-back

*Write agency.* Automatic for OBJ-05 through OBJ-09, OBJ-21, OBJ-23 (a run writes
its own record). Automatic-on-command for OBJ-10 (the harness hook fires without
the model choosing to record) and OBJ-11 (per-vault opt-in). Manual for OBJ-02 and
OBJ-03, which the external model authors as files. Both for OBJ-16 and OBJ-17.

*Acquisition and index maintenance are separate from curation.* Acquisition is the
method's live call to an external system; index maintenance is the catalog row and
`latest` marker; curation is a distinct, small, and mostly **negative** set of
operations — the audit noise denylist and sentinel filter, GC by version count and
lifetime, `run gc` by age and terminal state, and boot reconciliation.

*What is absent, and what that prevents.* Within the inspected boundary
(`src/domain/data/`, `src/domain/audit/`, `src/domain/summary/`,
`src/infrastructure/persistence/`) there is **no** consolidation, deduplication,
merging, semantic evolution, or synthesis of retained content, and no promotion of
any retained artifact into a stronger form or force: `absent`. Nothing rewrites a
stored artifact into a distilled one; nothing turns run history into a rule.
Decay exists, but only as age-, count-, and state-based deletion. This prevents
any conclusion that swamp maintains a curated or self-improving knowledge store —
it maintains an append-only, GC-bounded record.

*Raw traces versus distilled artifacts.* Three distillations exist, all
deterministic and all computed **at read time** rather than stored: the `swamp
audit` timeline over raw JSONL, `swamp summarise` over a time window of method
executions, workflow runs, and data, and reports (`OBJ-12`) — which are the one
case where a derivation is persisted back as data. Post-turn capture (the hook
append) is write-side maintenance, not a second read-back point.

### Annotations on the runtime-owned context routes

| Route | Direction (receiver's view) | Selection signal | Targeting | Scope and budget | Delivery / consumption point | Faithfulness test |
|---|---|---|---|---|---|---|
| RTE-12 | pull | a CEL predicate **authored by the external model** and validated against a closed field list before evaluation | exact structured match over `modelName`, `specName`, tags, provenance (`workflowRunId`, `stepName`, …) | unscoped by default — "the predicate string is the contract"; `--select` projection; no ranking, no similarity, no top-k | rendered CLI output read by the model, or a CEL value inlined into `OBJ-04` | field validation rejects unknown identifiers; no test that the selection matched intent |
| RTE-10 | pull | author-written CEL in the definition | `data.latest`, `data.version`, `data.findBySpec`, `data.findByTag`, `data.query`, `vault.get`, `env`, `file.contents` | one definition evaluation; `latest` resolves live | inlined into the evaluated artifact before execution | strict input declaration; unresolved vault refs are left unresolved rather than failing the record |
| RTE-16 | pull | a fixed time window (`--hours`) plus fixed filters | all rows in range, minus noise denylist and sentinel | 7-day retention bound; `--include-diagnostic` reveals filtered rows | terminal output | `swamp doctor audit`'s end-to-end smoke test — the only behavioral-faithfulness test found anywhere in this lens, and it tests the *capture channel*, not the selection |
| RTE-17 | pull | a fixed time window | repo-wide activity aggregate | window-bounded | terminal output | none found |
| RTE-20 | push, then read-back | directory registry membership | every registered global skill dir | union across all repos ever initialized | filesystem write into harness dirs | none — version stamping of installed skills is `absent` in the inspected code despite `design/global-skills.md:106` describing it |

The two selection signals are worth separating. `RTE-12` is **model-authored
structured retrieval**: the model writes a predicate, and swamp validates its
fields but not its intent. `RTE-16` and `RTE-17` are **fixed-window retrieval**
with no model input at all. Neither is similarity-based; nothing in the inspected
boundary embeds, ranks, or scores retained content.

### Four separate findings

1. **Context presence** — `implemented`. Skills and instructions are written into
   directories the harness reads (`RTE-08`, `RTE-20`); CLI output lands in the
   model's terminal (`RTE-09`).
2. **Deployed wiring** — `implemented` for the swamp side: hook configs, skill
   dirs, permission entries, and the registry are all written by inspected code.
3. **Activation** — `uninspected`. Whether delivered material changed the model's
   behavior is a fact about `CMP-22`, outside the boundary, with no run evidence in
   this analysis. *Prevented conclusion:* nothing here supports any claim that the
   skill corpus, the routing table, or a rendered audit timeline actually changed
   what the agent did.
4. **Causal effect** — `uninspected`, and unreachable in principle from this
   evidence: no intervention, no comparison, no observed run. *Prevented
   conclusion:* no attribution of any behavioral outcome to any swamp-supplied
   artifact.

A fifth, sharper finding: within the inspected boundary there is **no automatic
path that returns accumulated material to the model's context**. Every read-back
route requires the model to issue a command and read the result. `swamp audit`
does not appear in the skill routing table (`SKILL.md:38-54`), so the accumulated
record of the agent's own past actions has an implemented read-back route with no
implemented delivery into the next session. This is `absent` within
`.claude/skills/swamp/` and `src/`; it prevents any conclusion that swamp gives an
agent memory of its own prior work, while leaving intact the weaker true claim
that it *retains* that record for a human or an explicitly-instructed agent.

### Authority

`BAP-01`…`BAP-03` are advisory: the skill corpus can instruct ("Use the routing
table, not memory", "Validate before acting", "Use swamp commands, don't go around
them") but nothing in the reviewed boundary detects or prevents non-compliance.
`BAP-04` is binding on the harness's hook runner and not on the model. `BAP-13`
(`OBJ-25`) is **permissive**: 27 command patterns pre-approved in the Claude
settings and `swamp *` trusted in Kiro, which is the single strongest
authority-shaped artifact swamp installs — it removes a per-call human checkpoint
for the model's swamp usage, with horizon "that repo, until the settings file
changes". Curation labels in this lens (`gc`, `prune`, `sync`, `reap`, `noise
filter`) establish nothing about semantic preservation or warrant; they are
deletion and formatting operations only.

## 7B. Epistemic lens — invoked procedure

Invoked `kb/instructions/analyse-external-system-epistemic-architecture.md` and
executed its accepted route-analysis method inside this run's boundary. Executed
sequentially in the orchestrator context after the fresh lens worker was
terminated (`trial-notes.md`, friction 4). No source reacquisition, no boundary
widening, no revision change, no parallel ID namespace, no publication decision,
no system-wide epistemic grade. Its six required output blocks follow.

### 7B.1 Source-and-claim boundary

- **System / revision:** Swamp at `cf38c4ec1068613bb7d3432eb74a1ad854156dd7`.
- **Declared scope and exclusions:** as `evidence-packet.md` §Boundary. The
  model-calling actor (`CMP-22`) is excluded, which is decisive here: swamp's
  boundary contains no generative step at all.
- **Analysis question:** within swamp's own boundary, which routes handle
  truth-apt content, what does each do to it, what checks and acceptance steps
  exist, and which of `CLM-01`…`CLM-09` do those routes support?
- **Assessed route families:** acquisition of external state into stored
  resources; derivation (reports, summarise, timeline); indexing and retrieval;
  checking (validation, pre-flight checks, doctor); disposition (approval gates,
  extension trust); retention and decay; freshness and lineage; authority
  (grants, capability protocol, harness permission grant).
- **Unassessed route families:** everything inside `CMP-22`; the swamp-club
  backend's own processing (`CMP-23`); third-party extension model internals;
  provider-native vault backends. No system-complete conclusion is drawn.
- **Source register:** `SRC-01`…`SRC-05` in `evidence-packet.md`, with evidence
  layers. Every row below cites source plus a local anchor.
- **Missing evidence → conclusion prevented:** no observed run and no `.swamp/`
  runtime data anywhere in the checkout → no observed candidate state for any
  lifecycle phase, therefore no finding that any route ever actually accepted,
  rejected, or integrated a real candidate. No causal experiment → no attribution
  of any outcome to any component.
- **System knowledge/warrant claims:** `CLM-01`…`CLM-06` are consequential;
  `CLM-07`…`CLM-09` are the system's own disclaimers of unimplemented scope.

### 7B.2 Epistemic-object inventory

| Object | System name | Form | Source / lineage | Producer → consumer | Candidate truth-apt content | Claimed role | Evidence | Gap |
|---|---|---|---|---|---|---|---|---|
| OBJ-05a | data artifact, `resource` | structured, Zod-schema'd | acquired by a method's live call to an external API/CLI | model method → later definitions, queries, reports, workers | **yes** — asserts the state of a named external resource at a time | "typed representations of external systems" | SRC-02 `design/models.md:505-509`; SRC-01 `data_writer.ts` | schema conformance is checked; correspondence to the real resource is not |
| OBJ-05b | data artifact, `file` | raw bytes + MIME type | written by a method, optionally streaming | same | **conditional** — truth-apt only if its content is; swamp treats it opaquely | "file artifacts, logs" | SRC-02 `design/models.md:511-519` | content never interpreted by swamp |
| OBJ-06 | catalog row | SQLite row | derived index over OBJ-05 | write path → query path | **yes**, but only metadata propositions (this version exists, has these tags, came from this run) | query performance backing | SRC-02 `design/data-query.md:240-300` | `attributes` deliberately excluded from the index |
| OBJ-12 | report | markdown + JSON | deterministic TypeScript over `ReportContext` | report extension → data store, human, agent | **yes** — derived propositions about a run or model | "post-execution analysis functions" | SRC-02 `design/reports.md:1-30` | report logic is third-party code; its domain is whatever the author wrote |
| OBJ-10 | agent tool-use audit row | JSONL | normalized from a harness hook payload | harness → `swamp audit` | **yes** — asserts that a given shell command was invoked at a time | "append-only activity log … reviewing what an agent has been doing" | SRC-02 `design/audit.md:1-8` | records **shell commands only**; file edits, file reads, and model turns are never captured |
| OBJ-11 | vault read-audit row | JSONL | one per `VaultService.get()` | vault service → `vault audit-trail` | **yes** — asserts that a caller read a named secret at a time | "proving which automation read which secret, when" | SRC-02 `design/vaults.md:311-355` | opt-in per vault; `callerContext` may be `unknown` |
| OBJ-07 / OBJ-08 / OBJ-09 / OBJ-21 | execution records | YAML / SQLite / model data | written by the executor | executor → history commands, scheduler | **yes** — assert what ran, when, with what status | run history and lifecycle | SRC-02 `design/run-tracker.md`, `design/repo.md:207-216` | `OBJ-08` persists inputs only on suspend |
| OBJ-02 / OBJ-03 | definitions and workflows | schema-checked YAML + CEL | authored by the external model or a human | author → validator, executor | **no** — these are prescriptions, not assertions | source of truth | SRC-02 `design/repo.md:74-83` | — |
| OBJ-04 | evaluated definition | materialized YAML | CEL evaluation against live data/vault/env | evaluator → executor | **yes, derivatively** — it embeds a snapshot of values that were true at evaluation time | internal working directory | SRC-02 `design/expressions.md:554-566` | no record that the snapshot is still valid at execution time |
| OBJ-13 / OBJ-14 / OBJ-28 | skills, instructions, extension skills | natural-language | shipped in the binary, or third-party | swamp → external model | **mixed** — descriptive statements about swamp plus imperatives | teach the agent how to work with swamp | SRC-01 `.claude/skills/swamp/SKILL.md` | staleness is uncontrolled: version stamping is `absent` in inspected code |
| OBJ-19 | grant | YAML + sealed CEL | authored | author → serve authorizer | **no** — a permission, not an assertion | authorization | SRC-02 `design/repo.md:79-83` | — |
| OBJ-26 | CLI schema | JSON | generated from the live Cliffy tree | swamp → external model | **yes** — asserts what commands and options exist in *this* binary | "for AI agent consumption" | SRC-01 `help.ts:43-56` | generated, so it cannot drift from the binary — the strongest lineage in the inventory |

Omitted route classes, named: transport/framing internals, rendering, logging,
telemetry export, and packaging, none of which change lineage or warrant here.

### 7B.3 Authority-route ledger

| Route | Function | Arch. status | Object | Content/update relation | Check target | Evaluator + domain | Activation | Result | Force | Epistemic authority + scope | Operational authority | Behavioral-authority path | Evidence | Claims | Mismatch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RTE-23 | content transformation | implemented | OBJ-05a | truth-apt transformation: **acquisition/import** | — | — | every method run | a stored resource | — | licenses only "the external API returned this at this time"; source warrant **preserved but unrecorded** — nothing stores which endpoint, credential, or account produced it beyond definition identity | writes durable data | BAP-05 | SRC-01 `data_writer.ts`, SRC-02 `design/remote-execution.md:719-736` | CLM-03 | none |
| RTE-13 | retention | implemented | OBJ-05a/b | no content change | — | — | on write | versioned-immutable artifact + catalog row | binding on later readers | none — retention licenses nothing | later reads resolve | BAP-05 | SRC-02 `design/models.md:543-549` | CLM-06 | none |
| RTE-12 | operational selection/consumption | implemented | OBJ-05, OBJ-06 | non-ampliative reshaping (projection, filtering) | predicate field names | field-name validator, closed list | every query | matching rows, unscoped by default | binding on what the caller sees | none — selection is not warrant | feeds later execution via CEL | BAP-05 | SRC-02 `design/data-query.md:185-238` | — | none |
| RTE-10 | content transformation | implemented | OBJ-04 | **entailed derivation** within CEL's declared semantics | — | CEL evaluator, sealed per surface | definition evaluation | a materialized definition | binding — this is what executes | carries premise warrant only as far as the premises were warranted; CEL guarantees the *substitution*, not the truth of the substituted values | determines the action taken | BAP-05 | SRC-02 `design/expressions.md:10-42` | CLM-02 | none |
| RTE-27 | check/evidence production | implemented | OBJ-02, OBJ-03 | no content change | structural well-formedness, schema conformance, reference resolvability of a definition or DAG | program, formal domain = the declared schema | on `validate`, and before run | pass / errors | binding when run | licenses "this artifact is well-formed and its references resolve"; **does not** license that it will succeed or that it describes reality | blocks a malformed run | BAP-05, BAP-06 | SRC-01 `validation_service.ts:1-640` | CLM-01, CLM-02 | **yes** — `design/high-level.md:5-7` says swamp can "validate [models] are correct"; the implemented check is conformance, not correctness |
| RTE-07 | check/evidence production | implemented | OBJ-01 method invocation | no content change | model-declared invariants: policy, dependency readiness, quota | extension-authored TypeScript, domain = whatever the author encoded; may make live API calls | before **mutating** methods only (`create`/`update`/`delete`/`action`; unknown names default mutating) | `{pass, errors}` | binding **unless bypassed** | licenses only what the specific check inspected | permits or blocks the method | BAP-09 | SRC-02 `design/models.md:346-410`; SRC-01 `workflow_run.ts`, `model_method_run.ts` (`skipAllChecks`) | CLM-01 | **yes** — the guard is caller-bypassable by the same actor it guards |
| RTE-28 | check/evidence production | implemented | OBJ-10's capture channel | no content change | whether the hook→normalizer→JSONL chain still records | program; end-to-end smoke test with a sentinel row | on `doctor audit` | pass/fail/skip + actionable hint; non-zero exit | binding in CI if gated | licenses "the recording chain worked just now for this tool"; **does not** license that past rows are complete | surfaces silent drift | BAP-10 | SRC-02 `design/audit-doctor.md:11-61` | CLM-05 | none — this is the best-warranted check in the system |
| RTE-04 | disposition/acceptance | implemented | OBJ-20 gate on OBJ-08 | no content change | whether the run may proceed past this step | **human operator via CLI, or a model method** via `context.approveWorkflowGate` | when a run suspends | approved / rejected, `decidedBy` auto-stamped and not overridable | binding — the run stays suspended until decided | licenses nothing about content; it is an authorization decision, not an evidence-consuming acceptance of a proposition | resumes or fails the run | BAP-08 | SRC-02 `design/workflow.md:114-186`, `design/models.md:304-345` | CLM-06 | **yes** — an approval named "manual" can be granted programmatically, and nothing in the boundary prevents the same agent that authored the workflow from approving its gate |
| RTE-29 | disposition/admission | implemented | OBJ-22, OBJ-28 | no content change | whether an extension may auto-resolve | config list membership, not inspection of the extension | on first use of an unresolved type | silent auto-resolution or refusal | binding | licenses nothing about the extension's content | loads third-party code and instructions | BAP-11, BAP-14 | SRC-02 `design/repo.md:100-107`; SRC-01 `extension_pull.ts:100-118` | — | none, but note the review burden is transferred to the user by a warning |
| RTE-17 / RTE-16 | content transformation | implemented | OBJ-10, execution records | **non-ampliative reshaping** — filtering, grouping, counting over a window | — | — | on command | a rendered timeline or activity summary | advisory | licenses only what the underlying rows license, minus what the filters removed | none | BAP-10 | SRC-01 `audit_service.ts:32-137` | CLM-04 | none |
| OBJ-12 via CMP-17 | content transformation | implemented | OBJ-12 | **entailed derivation** within the report author's declared domain — or ampliative if the author's code conjectures; not determinable in general | — | — | after a method or workflow, or on demand | markdown + JSON persisted as data | advisory | licenses whatever the report's own logic warrants; swamp adds none | none directly | BAP-10 | SRC-02 `design/reports.md:1-120` | CLM-01 | none |
| RTE-15 | check/evidence production | implemented | OBJ-10 | truth-apt transformation: acquisition/import (from the harness) | — | — | on every harness `postToolUse` for shell tools | one JSONL row | binding on the record | licenses "this shell command was invoked"; **does not** license any claim about what the agent did outside the shell | none | BAP-04 | SRC-02 `design/audit.md:16-40` | CLM-04 | **yes** — scope of the record is narrower than "what an agent has been doing" |
| RTE-18 | check/evidence production | implemented, **opt-in** | OBJ-11 | acquisition/import | — | — | per `VaultService.get()` when `auditReads: true` | one JSONL row | binding on the record | licenses "this caller read this key at this time" | none | BAP-10 | SRC-02 `design/vaults.md:322-355` | CLM-04 | none, given the opt-in is stated |
| RTE-30 | lineage/freshness | implemented | OBJ-05 | no content change | which version a bare reference means | program | every resolution | a concrete version | binding | a pinned `(dataId, version)` is immutable forever; a bare `dataId` silently means "latest", which mutates | changes what a later run reads | BAP-05 | SRC-02 `design/remote-execution.md:750-772` | CLM-06 | none, but freshness is **not** endorsement: nothing re-checks that a retained resource still matches reality |
| RTE-19 | lifecycle (decay) | implemented | OBJ-05, OBJ-07, OBJ-08 | no content change | — | age, version count, terminal state | GC commands, `autoGc` (default off) | deletion | binding | none | removes evidence | — | SRC-02 `design/repo.md:108-132` | — | none |
| RTE-20 / RTE-08 | operational admission of instruction content | implemented | OBJ-13, OBJ-14, OBJ-17 | non-truth-apt policy/content update: installs instruction text into the model's discovery path | — | — | `repo init`/`upgrade`/`update` | files on disk | advisory on the model | none — instructions are not evidence | shapes model behavior | BAP-01…BAP-03 | SRC-02 `design/global-skills.md:120-181` | CLM-01 | **yes** — `design/global-skills.md:106` describes version-stamping installed skills; not found in inspected code |
| BAP-13 route (`OBJ-25`) | operational admission | implemented | OBJ-25 | no content change | — | — | `repo init` | 27 pre-approved patterns / `swamp *` | **permissive** | none | removes the per-call human checkpoint for swamp commands | BAP-13 | SRC-01 `repo_service.ts:1349-1379,1549-1556` | CLM-06 | **yes** — `CLM-06` promises review "before anything touches production", yet the same scaffolding pre-authorizes unattended `swamp vault`, `swamp data`, `swamp repo` invocations |
| RTE-31 | operational consumption | implemented | OBJ-26 | non-ampliative reshaping of the live command tree | — | — | on `swamp help` | full CLI schema JSON | advisory | licenses "these commands exist in this binary" — generated, so it cannot drift | informs the model's next command | BAP-10 | SRC-01 `help.ts:43-75` | — | none |
| RTE-05 / BAP-12 | operational admission | implemented | worker capabilities | no content change | whether a context member may cross the wire | closed 14-verb list | every remote dispatch | proxied, or `UnsupportedOnRemoteWorkerError` | binding, fail-loud | none | bounds what remote code can touch | BAP-12 | SRC-02 `design/remote-execution.md:505-560` | — | none |
| — | check/evidence production over OBJ-05a's **correspondence to reality** | **no route found within boundary** | OBJ-05a | — | "does this stored resource still describe the real external resource?" | none found | — | — | none | — | — | — | searched `src/domain/data/`, `src/domain/models/`, `src/domain/audit/doctor/`, `design/` | CLM-02, CLM-03, CLM-06 | **yes** — drift detection is explicitly aspirational (`CLM-07`) |

### 7B.4 Per-object lifecycle disposition

**OBJ-05a (acquired resource) — non-ampliative.**
`candidate: OBJ-05a | routes: RTE-23, RTE-13, RTE-12, RTE-30 | transformation:
truth-apt acquisition/import | discovery lifecycle: not applicable | acquisition
route and warrant: acquired by a live external call; source warrant preserved only
as "the external system returned this to this definition at this time" and
degraded thereafter by the absence of any re-verification route; lineage is
retained through definition ownership, version immutability, and provenance
fields | missing evidence/limit: no observed run, so no instance of this object
was inspected; no route re-checks correspondence, so age is the only available
proxy for staleness.`

**OBJ-04 (evaluated definition) — non-ampliative.**
`candidate: OBJ-04 | routes: RTE-10 | transformation: entailed derivation within
CEL's declared semantics | discovery lifecycle: not applicable | derivation route
and warrant: substitution is guaranteed by the evaluator; the truth of substituted
values carries only the warrant of OBJ-05a and the vault | limit: warrant for
"the values are still current at execution time" is absent.`

**OBJ-10, OBJ-11, OBJ-07, OBJ-08, OBJ-09, OBJ-21 (event records) — non-ampliative.**
`transformation: acquisition/import of an event assertion | discovery lifecycle:
not applicable | warrant: each licenses a narrow existential claim about an
invocation; OBJ-10's scope is shell commands only, and RTE-28 is the only route
that tests whether the channel producing these records still works | limit: no
observed instance; retention windows (7 days for OBJ-10, 30 days for OBJ-07/08)
bound any later reconstruction.`

**OBJ-12 (report) — indeterminate.**
`candidate: OBJ-12 | routes: CMP-17 | transformation: indeterminate |
classifications still possible: entailed derivation (a report that only counts,
groups, or reformats run context) or ampliative conjecture (a report whose
TypeScript infers a cause, a cost estimate, or a risk) | preserved lineage: the
report receives `swampSha`, the definition, method args, execution status, and
data handles, so its inputs are fully traced | implemented checks, retention, or
use: none — reports are persisted as data and rendered; no route checks a report's
output against anything | current warrant limit: swamp adds no warrant of its own
to a report; the report's warrant is whatever its author's code establishes |
evidence needed to decide: the source of specific report extensions, which are
third-party and outside this boundary.`

**Per-object no-candidate lines.**
`No lifecycle record for OBJ-02, OBJ-03: no candidate truth-apt output for these
objects (they are prescriptions); relevant routes: RTE-27, RTE-10.`
`No lifecycle record for OBJ-19, OBJ-25: no candidate truth-apt output; relevant
direct-adaptation/admission routes: BAP-07, BAP-13.`
`No lifecycle record for OBJ-13, OBJ-14, OBJ-28: their descriptive statements
about swamp are truth-apt but swamp implements no route that checks, disposes, or
accepts them; relevant routes: RTE-20, RTE-08.`

No ampliative candidate within the boundary reaches a discovery lifecycle: there
is no conjecture-generating step in swamp at all, because the only generative
actor is `CMP-22`, outside the boundary.

### 7B.5 System-claim versus route comparison

| Claim | Claimed operation/warrant | Source + layer | Doctrine support | Implemented routes | Observed-run support | Causal support | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| CLM-01 | agent-built automation is "reviewable, shareable, and accurate" | `README.md:7-11`, doctrine | yes | reviewable: RTE-13, RTE-27, RTE-12, git-tracked OBJ-02/03. shareable: RTE-21, RTE-24. accurate: only RTE-27 + RTE-07 | none | none | **reviewable** and **shareable** are supported at the implementation layer: artifacts are files, versioned, queryable, and validated for conformance. **Accurate** is supported only in the weak sense of schema conformance and author-written invariants | mismatch on "accurate": no route checks correspondence to the external world |
| CLM-02 | 1:1 models that swamp "can then validate are correct" | `design/high-level.md:5-7`, doctrine | yes | RTE-27, RTE-07 | none | none | swamp validates **conformance** — that a definition matches its type schema and that declared checks pass | mismatch: "correct" overstates a conformance check |
| CLM-03 | a resource represents external resource state | `design/models.md:505-509`, doctrine | yes | RTE-23, RTE-13 | none | none | supported as an **acquisition** claim: the artifact records what the external system returned at write time | unknown at read time — RTE-30 resolves `latest`, not truth |
| CLM-04 | the vault trail proves "which automation read which secret, when" | `design/vaults.md:313-315`, doctrine | yes | RTE-18 (opt-in), RTE-16 | none | none | supported **within its scope** when enabled: each row licenses a narrow existential claim, and `callerContext` names the caller | limits: opt-in per vault, `callerContext` may be `unknown`, provider-native reads outside swamp are not covered |
| CLM-05 | drift in the agent-activity record surfaces loudly, not silently | `design/audit-doctor.md:11-22`, doctrine | yes | RTE-28 — five ordered checks with a real end-to-end write-and-read | none | none | **best-supported claim in the system**: the smoke test genuinely exercises the failure mode described, and a compile-time fixture/normalizer contract backs it | limit: it proves the channel works *now*, not that any past window is complete |
| CLM-06 | everything is reviewable in `.swamp/` "before anything touches production" | `README.md:40-41`, doctrine | yes | RTE-13, RTE-27, RTE-04 | none | none | supported as **availability**: the artifacts exist on disk and can be inspected before a run | mismatch: nothing *enforces* review — RTE-07 is bypassable, RTE-04's "manual" gate is programmatically satisfiable, and BAP-13 pre-authorizes unattended `swamp` invocations |
| CLM-07 | applications, environments, drift detection are not implemented | `design/high-level.md:20-23` | self-disclaimed | none found | — | — | confirmed by absence in the inspected boundary | none |
| CLM-08 | quest events are designed, not present | `design/quests.md:59-61` | self-disclaimed | `swamp quest` command exists; event emission not found | — | — | confirmed | none |
| CLM-09 | the datastore-unification model is exploration | `design/unification.md:18-41` | self-disclaimed | none found | — | — | confirmed; its "agents work on their own head by default" contract is not in force | none |

### 7B.6 Bounded conclusion

**Retains, retrieves, reshapes, uses.** Swamp retains versioned-immutable
artifacts, execution records, and two append-only event trails, indexes them in
SQLite with first-class provenance, and retrieves them by validated exact-match
CEL predicate. Reshaping (`RTE-12`, `RTE-16`, `RTE-17`) is non-ampliative
filtering, grouping, and counting. Retention and retrieval alone do not constitute
knowledge production, and nothing here should be read as such.

**Acquires.** The system's characteristic truth-apt object, `OBJ-05a`, is
**acquired, not produced**: a method calls a live external system and stores what
came back. Source warrant is preserved narrowly (this definition, this time) and
is not re-established afterwards. Because no route re-checks correspondence, a
retained resource's warrant degrades with age in a way the system does not track —
`latest` resolution (`RTE-30`) answers "which version" and never "is this still
so".

**Derives.** Two derivation routes are entailed within declared domains: CEL
evaluation (`RTE-10`) inside CEL's semantics, and the timeline and summarise
reductions inside their filters. Reports (`OBJ-12`) are `indeterminate` as a
class, since a report is arbitrary third-party TypeScript that may merely count or
may conjecture.

**Conjectures, tests, accepts, integrates.** Within the boundary: nothing
conjectures. The generative actor sits outside it. Consequently no ampliative
candidate reaches acceptance or post-acceptance integration inside swamp, and the
discovery lifecycle is not applicable to any inventoried object.

**Acceptance criteria, intended use, scope, authority.** Three disposition routes
carry real force. `RTE-27` (validation) licenses conformance only, and its
mismatch with the doctrine word "correct" is the clearest overstatement found.
`RTE-07` (pre-flight checks) is the system's only guard on external mutation and
is bypassable by the same caller it constrains. `RTE-04` (the approval gate) is an
**authorization** decision, not an evidence-consuming acceptance of a proposition;
it stamps an unoverridable `decidedBy`, which is genuine provenance, but it can be
satisfied programmatically. Authority is otherwise well-separated: sealed
grant-condition CEL, a closed fail-loud capability protocol, and data ownership
enforced in code (`OwnershipValidationError`).

**Direct adaptation without a truth-apt route.** `RTE-20`/`RTE-08` and `BAP-13`
change the external model's behavior by installing instructions and
pre-authorizing commands. These are non-truth-apt policy updates. They carry no
epistemic authority whatsoever, and the fact that they influence behavior must not
be read as licensing content.

**Unsupported for want of evidence.** No claim in `CLM-01`…`CLM-06` has
observed-run or causal support in this analysis. `CLM-05` is the strongest at the
implementation layer; "accurate" in `CLM-01`, "correct" in `CLM-02`, and "before
anything touches production" in `CLM-06` each exceed what the inspected routes
implement. This is a route-level finding and no system-wide epistemic grade is
given.

**Scope note, not a failure finding.** Swamp's declared purpose is operational —
run automation, record what happened, keep artifacts reviewable. Judged against
that scope, the absence of conjecture, acceptance, and integration routes is a
boundary of the product, not a defect. The mismatches recorded above are between
its own broader wording and its narrower implemented routes.

## 8. Cross-lens reconciliation

**Merged by canonical ID.** Both lenses annotated the same objects and routes
without duplication. `OBJ-05` was split by the epistemic lens into `OBJ-05a`
(resource — truth-apt) and `OBJ-05b` (file — opaque to swamp); the memory lens
had treated them as one retained part. The split stands, and both lenses' findings
attach to the correct half: retention policy and GC apply to both; acquisition
warrant applies only to `OBJ-05a`. `RTE-16` and `RTE-17` carry a memory-lens
annotation (fixed-window read-back) and an epistemic-lens annotation
(non-ampliative reshaping); these are compatible descriptions of one route, not a
conflict. Six routes were newly registered mid-run (`RTE-25`…`RTE-31`) and four
objects (`OBJ-25`…`OBJ-28`) plus two authority paths (`BAP-13`, `BAP-14`); all
received orchestrator IDs before use, and no lens created a parallel namespace.

**Ownership held.** The runtime account (record 5) owns the complete control and
context routes and their endpoints. The memory lens annotated read-back direction,
selection signal, and the presence/wiring/activation/causality split, and did not
touch transformation or warrant. The epistemic lens annotated transformation
class, checking, acceptance, retention-versus-integration, and the two
authorities, and did not redefine any route's endpoints.

**Consistency checks.** One revision (`cf38c4e`) and one boundary across every
record. Every shared route cites the same sources and the same `BAP-*`
references in both lenses. No route's endpoints differ between lens accounts.

**Conflicts preserved as conflicts, not resolved.**

1. *Skill version stamping.* `design/global-skills.md:106` states that installed
   global skills are version-stamped in SKILL.md frontmatter; the inspected
   installation code shows no stamping. Recorded as a doctrine-versus-implementation
   conflict in both lenses. Not resolved by preferring either side: the design doc
   is at the same revision and was refreshed three days before HEAD.
2. *"Manual" approval.* `design/workflow.md` frames the gate as an operator
   decision; `design/models.md:304-345` documents programmatic approval from
   inside a model method. Both are implemented. The conflict is in the label, not
   the code, and is preserved as such.
3. *Review before production.* `README.md:40-41` promises review before anything
   touches production; `repo_service.ts:1349-1379` pre-authorizes unattended
   `swamp` commands. Both are implemented facts about the shipped system.

**Boundary discipline held.** Memory curation labels (`gc`, `reap`, `prune`,
`noise filter`, `sync`) were not allowed to determine epistemic transformation:
no curation operation was classified as reshaping, derivation, or acceptance.
Behavioral influence was not allowed to imply authority: the skill corpus
demonstrably shapes what the model is told, and that fact licenses no epistemic or
operational authority anywhere in the ledger. Conversely, `BAP-13`'s real
operational authority was not allowed to imply any epistemic license.

## 9. Bounded synthesis

Swamp is best understood as a **deterministic operating layer built for an agent
that lives outside it**. Following the deployed system's progression:

**Scheduling.** Control divides cleanly in two. Above swamp, the next step is
chosen by a language model in an external harness that swamp neither observes nor
constrains — swamp's only instruments there are prose (`BAP-01`…`BAP-03`) and a
permission grant (`BAP-13`). Below swamp's CLI boundary, every scheduling decision
is symbolic and inspectable: a topological sort with level-parallel execution and
concurrency caps, cron registration, a bounded webhook queue, and a label/platform
dispatch scheduler. Three step kinds exist and no more. The design's own
consequence is that swamp offers no retry at the DAG level; the only retry lives
in method-returned `followUpActions`. The interesting architectural move is that
this dividing line is *deliberate*: swamp's pitch is that the nondeterministic
actor should author declarative artifacts, and that everything downstream of
authoring should be replayable without a model in the loop.

**Context assembly.** Two distinct mechanisms, easy to conflate and worth keeping
apart. Toward the model, swamp *pushes* a large static instruction corpus into
harness discovery paths and *offers* a generated CLI schema (`RTE-31`); that is
context supply from shipped material, not memory. Toward execution, swamp *pulls*
values into definitions through CEL — vault secrets, other models' data, env,
file contents — materializing an evaluated artifact before anything runs. Data
retrieval is exact-match and predicate-driven: fields are validated against a
closed list, provenance is first-class, and nothing is embedded, ranked, or scored.
Where a model does influence selection, it does so by *writing a predicate*, which
swamp validates syntactically and never for intent.

**External state and action.** The action boundary is wide and lightly fenced:
methods run in-process and reach the world through subprocesses, HTTP, and cloud
SDKs, inheriting the invoking shell's credentials. Fencing is real but conditional
— pre-flight checks guard mutating methods and are caller-bypassable; the sealed
grant environment and the closed capability protocol are genuinely binding, and
the remote-execution design's "orchestrator is the world, worker is pure compute"
split is the strongest containment property in the system. State is
versioned-immutable with a mutable `latest` pointer, immediately durable on write,
indexed in SQLite, and expired by age, version count, and terminal state.

**Memory return.** Real but narrow and entirely pull-based. Artifacts written by
one run are readable by later runs and commands; the agent's own shell activity is
captured automatically and rendered on request; a user-global registry
accumulated across repos is what lets a later repo-less update reach the right
directories. What is absent is as characteristic as what is present: no
consolidation, no synthesis, no promotion of retained material into stronger form,
and — the sharpest finding — no automatic path returning accumulated material to
the model's context, with `swamp audit` not even present in the skill routing
table. Swamp retains an agent's history for a human; it does not hand that history
back to the agent.

**Truth-apt and warrant routes.** Swamp's characteristic epistemic object is
acquired, not produced: a stored resource records what an external API returned to
a named definition at a time. Derivation exists and is entailed within declared
domains (CEL substitution, timeline and summary reductions); reports are
indeterminate because they are arbitrary third-party code. Nothing inside the
boundary conjectures, because the only generative actor is outside it —
so acceptance and post-acceptance integration are not applicable to any
inventoried object. Checking is where the design is most interesting and most
uneven: `swamp doctor audit` is a genuinely well-warranted check, testing
end-to-end that the evidence channel still records, precisely because that channel
fails silently; validation checks conformance and is described with the stronger
word "correct"; and the guard on real-world mutation can be switched off by the
same caller it constrains.

**Governing controls.** Authority separates cleanly in the places swamp took care
over — sealed grant CEL, a closed fail-loud capability protocol, code-enforced
data ownership, an unoverridable `decidedBy` stamp — and thins out at the harness
seam, where swamp's controls become advisory text plus one permissive grant that
removes a human checkpoint. Capability-versus-deployment matters throughout: every
finding above describes what the inspected code affords, and none of it
establishes that any of it was ever deployed, ran, or changed an agent's behavior.

No early exit bounded these conclusions; both lenses ran. No system-wide epistemic
grade is given, and none of the above should be read as one.

## 10. Limitations, each paired with the conclusion it prevents

1. **No observed run.** The binary was never compiled or executed and the checkout
   contains no `.swamp/` runtime data. → Prevents every observed candidate state in
   record 7B.4, any claim that a route ever actually fired, and any statement about
   real artifact contents. All lifecycle phases are `no instance observed`.
2. **No causal experiment.** → Prevents attributing any behavioral outcome to any
   component: no claim that skills, hints, permission grants, or audit output
   changed what an agent did.
3. **The model-calling actor is outside the boundary** (`CMP-22`). → Prevents any
   conclusion about activation, about how instructions are actually resolved, about
   whether the agent complies with `SKILL.md`'s rules, and about the composite
   agent loop end to end. Conclusions here are whole-system for *swamp* and
   partial for *swamp + harness*.
4. **The swamp-club backend is not inspectable** (`CMP-23`). → Prevents any claim
   about registry, auth, quest, or telemetry-server behavior; all such findings are
   client-side only.
5. **Third-party extension code is out of boundary.** → Prevents deciding whether
   `OBJ-12` reports are entailed or ampliative; the class stays `indeterminate`,
   and prevents any general statement about what extension models do to the world.
6. **Doc-versus-code conflicts unresolved in two places** (skill version stamping;
   the "manual" approval label). → Prevents a settled statement about installed-skill
   freshness and about who can satisfy an approval gate in practice.
7. **Boundary is ~1 month older than the cutoff** (HEAD 2026-07-17, cutoff
   2026-08-20) in a repo averaging ~270 commits/month. → Prevents any claim about
   current `main`; every finding is pinned to `cf38c4e`.
8. **Partial inspection of large subsystems.** The datastore sync/locking internals,
   the extension system's loading path, the serve authorization implementation, and
   `presentation/` were read at design-doc level with only spot checks in code. →
   Prevents implementation-layer claims about those specific mechanisms; they are
   recorded at the `doctrine/design` layer where cited, and this is a claim-local
   limitation that does not change the overall `code-grounded` tier, which rests on
   the inspected material loops.
9. **Two runtime fact-gathering workers and both fresh lens workers were terminated
   mid-run** by an external usage limit (see `trial-notes.md`). The lenses were
   re-executed sequentially in the orchestrator context against the same registers,
   which the instruction's worker topology permits; one worker's state/action
   findings were never received and were replaced by direct orchestrator reads. →
   Prevents any claim that this run achieved fresh-context lens isolation, and
   means the state/action surface rests on somewhat thinner targeted reads than the
   scheduling and agent-interface surfaces.

## 11. Verification and blocker report

### Verification performed

- **Source anchors and statuses:** every record cites `SRC-01`…`SRC-05` with a
  local anchor. Evidence layers kept distinct; design-doc claims marked as
  doctrine where they were not confirmed in code. Spot-verified anchors directly
  in the checkout after the interruption: `repo_service.ts:1349-1379` (27
  permission entries), `repo_service.ts:1549-1556` (Kiro trusted commands),
  `help.ts:43-56` (agent-facing schema), `extension_pull.ts:100-118` (skill
  warning), `step_task.ts:38,47,52` (three step kinds),
  `execution_service.ts:313,2838` (nesting cap), `webhook.ts:298,406` (queue
  depth), `skipAllChecks` wiring in both run commands.
- **IDs:** unique and resolving. `CMP-01`…`CMP-24`, `OBJ-01`…`OBJ-28` (with
  `OBJ-05` split into `05a`/`05b` by the epistemic lens), `RTE-01`…`RTE-31`,
  `BAP-01`…`BAP-14`, `CLM-01`…`CLM-09`, `SRC-01`…`SRC-05`. No collisions; no
  parallel namespace was created by either lens.
- **One boundary and one revision** across all records: `cf38c4e`, boundary as
  declared in `evidence-packet.md`.
- **Mandatory runtime coverage:** five material loops recorded with trigger,
  next-step owner, decision policy and form, context selection, state reads and
  writes, action executor and boundary, persistence, coordination, retry/recovery,
  and output. Conditional surfaces included only with stated materiality.
- **Both lens dispositions present** as explicit records (record 6); neither is
  implied by an absent section. Both applicable lenses produced output (7A, 7B).
- **Prevented conclusions stated** for every non-run and every negative: activation,
  causality, correspondence checking, consolidation/synthesis, automatic read-back.
- **Shared-route ownership respected**; see record 8.
- **No forbidden evidence upgrades.** Checked explicitly: retention is not
  read-back (`OBJ-13`/`OBJ-14` are named retained state, not memory); context
  presence is not activation (record 7A.4 keeps four separate findings);
  implementation is not deployment (every finding says what the code affords);
  observation is not causality (there is no observation at all here); curation is
  not warrant (record 8); use is not acceptance (`RTE-04` is authorization, not
  acceptance of a proposition); behavioral authority is not epistemic or
  operational authority (`BAP-13` carries operational force and zero epistemic
  license).

### Deterministic validation

No dedicated result contract exists for this artifact type, and the instruction
forbids improvising a collection contract or reusing the agent-memory review
schema. The applicable generic validation is therefore the semantic checklist
above, which was run item by item. No schema or parser was changed to manufacture
a validation path. `commonplace-validate` was not run against these files: they
sit in the workshop layer under a trial directory and carry no collection type,
so there is no contract for it to check.

### Blockers

- **Publication blocker: no authorized target contract.** This run had no
  authorized publication target. The logical result is retained under the run's
  staging identity (record 1). Publishing it would require either an existing
  collection whose contract can represent an eleven-record bounded system analysis
  with cross-file ID resolution, or a new contract — and improvising one is
  explicitly forbidden. Nothing else blocks the result: all eleven logical records
  are present, IDs resolve, and no unsupported material claim was made.
- **No other blockers.** No missing logical records, no ID collisions, no failed
  applicable validation.

### Report

- **Result identity and location:** `AGS-2026-08-20-SWAMP-01`, retained at
  `kb/work/multistage-write-analyse-agentic-system-20260820/trials/swamp/`
  (`result.md`, `evidence-packet.md`, `canonical-records.md`).
- **Boundary / revision / tier:** swamp as an agent operating layer, external
  harness and backend excluded; `cf38c4e`; `code-grounded`.
- **Lens dispositions:** memory/context `applicable` (run); epistemic `applicable`
  (run, via the invoked procedure).
- **Limitations:** record 10, nine entries, each paired with a prevented
  conclusion.
- **Blockers:** one publication blocker, recorded above.
