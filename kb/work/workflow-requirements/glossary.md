# Glossary: one word per concept

Each concept in [requirements](./requirements.md) gets one word, used
unchanged in the requirements, the scenarios, the
[mapping](./analysis-workflow-as-job-set.md), the [API design](./api-design.md)
and the [sketch](./api_sketch.py). Applied to all five on 2026-10-07, and its 2026-10-09 decisions on
2026-10-09; the
mapping's Spec needs items keep their original wording as a record. The
Status column records what changed.

## Method

Drawn from McConnell (*Code Complete*, ch. 11 and 7.3), Martin (*Clean Code*,
ch. 2), Ousterhout (*A Philosophy of Software Design*, ch. 14) and Evans
(ubiquitous language), as recalled, not checked against the texts.

1. Concepts come from the requirements; the API uses only their words.
2. One word per concept, and no word for two concepts.
3. Part of speech fits the role: a class holding data is a noun for what it
   holds; a procedure is verb plus object; a function is named for its result.
4. The docstring's first sentence uses the name as its subject. If the
   natural sentence says the thing is something else, the name is wrong.
5. No false implication, such as "view" implying live currency.
6. A name that will not come is a design question first.

**Status:** *keep* — the earlier word passed; *changed* — replaced, with
what it replaced; *decided* — settled by the operator.

## Purpose and layers

The engine produces composite artifacts: artifacts whose members are
artifacts with types of their own, made by separate jobs that must agree.
Relations, scoped judgments, coverage and the pending-producer wait exist for
that agreement. A single document has none of it and is written and
validated by the ordinary write path, never by a plan. Whether a member can
itself be composite is out of scope (operator, 2026-10-09).

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| One execution of a plan, producing one artifact | artifact run | `Run`, package `artifactrun` | An artifact run executes a plan with parameters and produces one artifact. | decided 2026-10-09: the bare word *run* is the codebase's commonest verb, so the concept takes a compound; *setrun* rejected with *set*, *runset* rejected as reading "a set of runs". Inside the package the class stays `Run`. `commonplace.workflow` renamed 2026-10-09 |
| The code that runs artifact runs | engine | package `artifactrun` | The engine schedules, pins, judges and covers; it knows nothing of validation, Git or files outside its store. | added |
| What any consumer's handlers and command-line glue reuse | reuse modules | `artifactrun.checks`, `.sources`, `.effects`, `.worktree`, `.report` | The reuse modules are the engine's modules that code-job handlers and the coordinator's command line call. | decided 2026-10-09: no package of their own; every one imports the engine, so they live in it beside the core. The former `setrun` package was a namespace, not a concept |
| What supplies a plan, a type and any handlers | consumer | — | A consumer supplies a plan, a type and the handlers the plan names. | added: the former `setrun` docstring's word |

## Structure

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| The directory one command advances | artifact-run directory | `run_dir: Path` | The artifact-run directory holds one artifact and the state that produces it. | decided 2026-10-09: follows *artifact run*; was *run directory* |
| The typed subdirectory | artifact | `artifact/` | The artifact is the typed directory the run produces; only members live in it. | decided 2026-10-09: the KB's word for a typed thing, and ADR 095's kind; was *set*, ordinary English and the validator's word for the membership as a whole. Renamed 2026-10-09 |
| The type of the artifact | type | `Plan.type_spec` | The type declares the artifact's roles, relations and required members. | keep |
| A declared position in the artifact | role | `ModelJob.role`, `CodeJob.role`, `address: role` | A role is a position the type declares, with a path and relations. | changed: the spec said *slot*, the sketch *member* and *slot name*; decided 2026-10-09: *member* is ordinary English for a file of the artifact and names no concept; the input address resolving a role's current version is `role`, the validator's flag is `--role`, and *slot* is retired |
| A declared link between two roles | relation | `"verification:cites:runtime"` | A relation is a link the type declares from an origin role to a partner role, of a kind such as `identity` or `cites`. | decided: `<origin>:<kind>:<partner>`, replacing `<kind>:<partner>`; see [Relation](#relation) |
| Whether the set's disposition permits a role | permitted role | — | A permitted role is one the type permits given the members present; a job filling any other role is not ready. | changed: was *required role*; requiring admits only `always` roles until the discriminating member exists, so no complete run could start |

## Declaration

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| The declared work for an artifact | plan | `Plan`, module `plan` | A plan declares the jobs that produce one type of artifact. | decided 2026-10-09: was *job set*, whose *set* collided with the produced set. Renamed 2026-10-09 |
| A unit of work | job | `ModelJob`, `CodeJob` | A model job is handed out to a worker; a code job runs under the command. | keep |
| A code job's function | handler | `CodeJob.handler` | A handler is the package function a code job runs, named by dotted path. | keep |
| A model job's instruction file | instruction | `ModelJob.instruction` | The instruction is the input whose file the worker follows. | keep |
| A declared dependency of a job | input | `Input`; field `inputs` | An input is something a job depends on, required or optional. | changed: was *read* (`Read`, `reads`), an action named as a class, documented as a view |
| An input that orders without triggering | order-only input | `Input.order_only` | An order-only input must be present for its job to be ready, but its change never makes the job ready again. | borrowed: GNU Make's order-only prerequisites, same meaning; was *presence-only* (`trigger: false`) |
| What an input resolves to | address | `Input.address` | The address says where the engine resolves an input when an attempt opens. | changed: was `kind`, then `view`, which rule 5 rejects |
| Version an attempt was given, via its record | handed input | `address="handed"` | A handed input is the version a declared attempt record says that attempt was given. | changed: was `pinned`, but every input is pinned |
| A job's limit on attempts | max attempts | `ModelJob.max_attempts` | Max attempts is the most attempts a model job may make in the run, the first included. | borrowed: Temporal, Prefect and Airflow use it with this meaning, the first attempt counted; was *bound*, earlier `max_attempts` |
| A job's produced files | output | `outputs` | An output is a file a job writes; the first is its primary output. | keep, once the set directory no longer uses the word |
| An output not yet accepted | candidate | — | A candidate is an output not installed in a role. A status, not a separate thing. | keep in prose; no API name |

## Running

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| Creating a run | start | `start_run()` | Starting a run writes the metadata that names its plan and parameters. | added: no operation created a run, so nothing could name the plan that `advance()` loads |
| One call of the command | invocation | `advance()` | An invocation runs ready code jobs and hands out ready model jobs. | keep the function; drop *round*, which the decisions use for the same thing |
| What an invocation returns | run status | `RunStatus` | The run status lists hand-outs, open attempts, stops and publishability after an invocation. | changed: was `Advance`, the same word as the function |
| The agent calling the command | coordinator | — | The coordinator calls the command, runs workers and reports their attempts. | changed: spec says *orchestrating agent* and *agent* |
| The agent running a model job | worker | `AttemptResult.model`, `.effort` | A worker is the model run that carries out one attempt. | keep; drop `runner`, which is undefined |
| One execution of a job | attempt | `attempt: str` | An attempt is one execution of a job against inputs pinned when it opens. | keep; *execution*, not *run*, so that *run* keeps one meaning |
| An attempt's states | open, completed, failed | — | An attempt is open until reported; it closes completed or failed. | changed: the sketch says *finished*, the spec *completed*; use *completed* |
| The coordinator's report closing an attempt | attempt result | `AttemptResult` | An attempt result closes one open attempt as completed or failed. | changed: was `Completion`, which also closes failures; *Report* collides with analyst reports |
| The record written last for an attempt | attempt record | `address="attempt"` | An attempt record is the closed attempt with the versions it was handed. | keep |
| Fixing an input's version at open | pin | — | Pinning fixes the version of every input when an attempt opens. | keep as internal verb; no API name |
| What a hand-out gives a worker | hand-out | `Handout` | A hand-out is an open model attempt's prompt and output paths. | keep |
| Previous attempt's output in a hand-out | previous output | — | The previous output is supplied by identity and is not an input. | changed: the spec calls it *context*, colliding with untracked context |
| What a worker reads beyond its inputs | untracked context | — | Untracked context is anything a worker reads that is not an input. | keep; reserve *context* for this |
| A code job's handle on its attempt | code attempt | `CodeAttempt` | A code attempt gives a handler its pinned inputs and stages its judgments. | changed: was `CodeContext`, colliding with *context* |
| What inspection says about a whole run | run condition | `inspect()["condition"]` | The run condition is running, publishable, stopped or stuck. | added: replaces the analysis report's own "completed" and "stopped" |
| A completion that still stands | current completion | `current_outputs()` | A completion is current while its pins still resolve unchanged, no attempt of the job is open and the job is not ready. | added: the narrow "completed" the publication handoff used |
| An invocation ending for the operator | stop | `Stop` | A stop names the job and attempt that ended the invocation. | keep |
| A worker's declared inability | problem | `Handout.problem` | The problem file is where a worker reports why it cannot produce output. | keep |

## Judging

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| The engine primitive | judgment | `judge()` | A judgment accepts or refuses one version, with findings. | keep |
| The two outcomes | acceptance, refusal | `outcome="accepted"` / `"refused"` | — | keep |
| The version judged | subject | `judge(subject, …)` | The subject is the one version a judgment is about. | changed: the sketch says `target`, the design text *subject* |
| The inputs a judgment records | basis | — | The basis is the judging attempt's pinned inputs. | changed: the spec says "the reads the job used" |
| The relations a judgment covers | scope | `judge(…, scope=…)` | The scope is the relations a judgment covers, all among its basis. | changed: the sketch says `relations`, the design text *scopes*, the spec both |
| A judgment remaining valid | holds | — | A judgment holds while its basis is at its recorded versions. | keep |
| A judgment that holds, and one that does not | up to date, stale | — | A judgment is up to date while it holds and stale once an input in its basis has moved. | borrowed: build systems and Make use both words for derived results against their inputs |
| The versions a judgment or attempt recorded | lineage | — | Lineage is the record of which versions an attempt used and which judgment rests on them. | borrowed: data platforms and W3C PROV's *used* relation; the word for the record, not a new mechanism |
| An input no longer present | lapses | — | An input lapses when its address no longer resolves; lapsing is not a change. | keep |
| Cancelling a refusal implicitly | supersede | — | An acceptance supersedes a refusal whose scope its own includes. | keep |
| Cancelling a refusal explicitly | override | `judge(…, overrides=…)` | An override names a refusal the acceptance cancels. | keep; refusal identity must be exposed, see below |
| A rerun having read a refusal | answers | — | An attempt answers the refusal it read. | keep |
| A judgment's reasons | findings | `findings` | — | keep |
| The engine's coverage evidence as an input | coverage input | `address="coverage"` | A coverage input is present while the set minus the declaring job's role is publishable; its version names the members and covering claims. | added: replaces per-relation judgment inputs on assembly and publication |
| Coverage for publication | covers | — | A holding acceptance of the current member at one end covers a relation when the current member at the other end is in its basis. | keep |

## Relation

A relation needs a name before `scope` can be typed. The type layout has
two relation kinds, `identity` and `cites`, and one pair of roles can have
both: the runtime report has an identity relation to the boundary and also
cites it. So the partner role alone does not name a relation. Nor do kind
and partner: an apply job refuses the runtime report under the relation
from the verification to it, and `cites:runtime` would read as runtime
citing itself.

Decision: a relation is named `<origin>:<kind>:<partner>`, such as
`verification:cites:runtime`. A judgment may scope any declared relation
its subject's role is at either end of. A relation is covered by a holding
acceptance of the current member at either end whose basis has the current
member at the other end. The three prose relations (synthesis limits, amendment
index, profile source identity) need kinds when they are declared.

## Borrowed vocabulary

Established terms are borrowed only where their meaning matches exactly;
a near-match misleads an agent more than a coined word (method rule 5).

- **Kept as ours.** *Candidate* (an output not yet accepted; as in a release
  candidate), *member*, *role*, *artifact*, *judgment*, *acceptance*, *refusal*,
  *scope*, *hand-out*, *attempt* (also Temporal's word) and *plan*. ETL
  vocabulary has no exact counterpart, and *DAG* would be wrong: correction
  loops are cycles.
- **Pattern, not vocabulary.** Candidate, check and acceptance follow the
  write-audit-publish pattern of data engineering. Its *publish* is our
  *acceptance*, not our *publication*, so its words are not adopted.
- **Rejected.** Dagster's and dbt's *asset* and *materialization* (a
  materialization is a value at once, or a storage strategy), Airflow's
  *executor* for the coordinator (it never judges), and *XCom*, *sensor* and
  *backfill*, which name nothing here.

## Notes

- **The artifact directory.** Historical runs are unaffected by `artifact/`: a
  retained set holds the members directly, not the directory name.
- **Refusal identity.** The refusal address now carries the refusal's
  identity, which `overrides` names.
- **Read as a verb.** `CodeAttempt.read(name)` stays: it is an action on an
  input, which is now a noun of its own.
