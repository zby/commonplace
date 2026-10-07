# Glossary: one word per concept

Each concept in [requirements](./requirements.md) gets one word, used
unchanged in the requirements, the scenarios, the
[mapping](./analysis-workflow-as-job-set.md), the [API design](./api-design.md)
and the [sketch](./api_sketch.py). Applied to all five on 2026-10-07; the
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

## Structure

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| The directory one command advances | run directory | `run_dir: Path` | The run directory holds one typed set and the state that produces it. | changed: `directory` says nothing of what it holds |
| The typed subdirectory | set | — | The set is the typed directory the run produces; only members live in it. | decided: `set/`, replacing `output/`, which collided with *output* |
| The type of the set | type | `JobSet.type_spec` | The type declares the set's roles, relations and required members. | keep |
| A declared position in the set | role | `ModelJob.role`, `CodeJob.role` | A role is a position the type declares, with a path and relations. | changed: the spec says *slot*, the sketch says *member* and *slot name*, the type layout says `roles` |
| The accepted version in a role | member | — | A member is the version currently installed in a role. | keep; stop using it for the role itself |
| A declared link between two roles | relation | `"cites:runtime"` | A relation is a link the type declares from one role to another, of a kind such as `identity` or `cites`. | decided: `<kind>:<partner role>`; see [Relation](#relation) |
| Whether the set's disposition requires a role | required role | — | A required role is one the type requires given the members present. | keep (spec: "member the type does not require") |

## Declaration

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| The declared work for a set | job set | `JobSet` | A job set declares the jobs that produce one type of set. | keep |
| A unit of work | job | `ModelJob`, `CodeJob` | A model job is handed out to a worker; a code job runs under the command. | keep |
| A code job's function | handler | `CodeJob.handler` | A handler is the package function a code job runs, named by dotted path. | keep |
| A model job's instruction file | instruction | `ModelJob.instruction` | The instruction is the input whose file the worker follows. | keep |
| A declared dependency of a job | input | `Input`; field `inputs` | An input is something a job depends on, required or optional. | changed: was *read* (`Read`, `reads`), an action named as a class, documented as a view |
| What an input resolves to | address | `Input.address` | The address says where the engine resolves an input when an attempt opens. | changed: was `kind`, then `view`, which rule 5 rejects |
| Version an attempt was given, via its record | handed input | `address="handed"` | A handed input is the version a declared attempt record says that attempt was given. | changed: was `pinned`, but every input is pinned |
| A job's limit on attempts | bound | `ModelJob.bound` | The bound is the most attempts a model job may make in the run. | decided: `bound` in spec and API, replacing `max_attempts` |
| A job's produced files | output | `outputs` | An output is a file a job writes; the first is its primary output. | keep, once the set directory no longer uses the word |
| An output not yet accepted | candidate | — | A candidate is an output not installed as a member. A status, not a separate thing. | keep in prose; no API name |

## Running

| Concept | Word | API name | First sentence | Status |
|---|---|---|---|---|
| One call of the command | invocation | `advance()` | An invocation runs ready code jobs and hands out ready model jobs. | keep the function; drop *round*, which the decisions use for the same thing |
| What an invocation returns | run status | `RunStatus` | The run status lists hand-outs, open attempts, stops and publishability after an invocation. | changed: was `Advance`, the same word as the function |
| The agent calling the command | coordinator | — | The coordinator calls the command, runs workers and reports their attempts. | changed: spec says *orchestrating agent* and *agent* |
| The agent running a model job | worker | `AttemptResult.model`, `.effort` | A worker is the model run that carries out one attempt. | keep; drop `runner`, which is undefined |
| One run of a job | attempt | `attempt: str` | An attempt is one run of a job against inputs pinned when it opens. | keep |
| An attempt's states | open, completed, failed | — | An attempt is open until reported; it closes completed or failed. | changed: the sketch says *finished*, the spec *completed*; use *completed* |
| The coordinator's report closing an attempt | attempt result | `AttemptResult` | An attempt result closes one open attempt as completed or failed. | changed: was `Completion`, which also closes failures; *Report* collides with analyst reports |
| The record written last for an attempt | attempt record | `address="attempt"` | An attempt record is the closed attempt with the versions it was handed. | keep |
| Fixing an input's version at open | pin | — | Pinning fixes the version of every input when an attempt opens. | keep as internal verb; no API name |
| What a hand-out gives a worker | hand-out | `Handout` | A hand-out is an open model attempt's prompt and output paths. | keep |
| Previous attempt's output in a hand-out | previous output | — | The previous output is supplied by identity and is not an input. | changed: the spec calls it *context*, colliding with untracked context |
| What a worker reads beyond its inputs | untracked context | — | Untracked context is anything a worker reads that is not an input. | keep; reserve *context* for this |
| A code job's handle on its attempt | code attempt | `CodeAttempt` | A code attempt gives a handler its pinned inputs and stages its judgments. | changed: was `CodeContext`, colliding with *context* |
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
| An input no longer present | lapses | — | An input lapses when its address no longer resolves; lapsing is not a change. | keep |
| Cancelling a refusal implicitly | supersede | — | An acceptance supersedes a refusal whose scope its own includes. | keep |
| Cancelling a refusal explicitly | override | `judge(…, overrides=…)` | An override names a refusal the acceptance cancels. | keep; refusal identity must be exposed, see below |
| A rerun having read a refusal | answers | — | An attempt answers the refusal it read. | keep |
| A judgment's reasons | findings | `findings` | — | keep |
| Coverage for publication | covers | — | An acceptance covers a relation when the partner version in its basis is the partner's current member. | keep |

## Relation

A relation needs a name before `scope` can be typed. The type layout has
two relation kinds, `identity` and `cites`, and one pair of roles can have
both: the runtime report has an identity relation to the boundary and also
cites it. So the partner role alone does not name a relation.

Decision: a relation is named `<kind>:<partner role>`, such as
`cites:runtime`. The three prose relations (synthesis limits, amendment
index, profile source identity) need kinds when they are declared.

## Notes

- **The set directory.** Historical runs are unaffected by `set/`: a
  retained set holds the members directly, not the directory name.
- **Refusal identity.** The refusal address now carries the refusal's
  identity, which `overrides` names.
- **Read as a verb.** `CodeAttempt.read(name)` stays: it is an action on an
  input, which is now a noun of its own.
