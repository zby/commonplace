# Port the analysis workflow onto headless workers

Posed 2026-10-18 by the operator: plan porting `analyse-agentic-system` from
the artifact-run engine (`src/commonplace/artifactrun/`, about 4,530 lines)
and its coordinating agent onto a Python workflow script that launches each
worker through a harness's headless mode (`claude -p`, `codex exec`,
`pi -p`). The primitives are drafted and tested in
[headless-analysis](../headless-analysis/README.md); this workshop plans and
tracks the port. The operator asked for the plan; executing each phase is not
yet authorized beyond the probes in phase 0.

## Why headless now

The coordinator was an agent because, until recently, launching workers
programmatically on a subscription was not known to work. On 2026-10-18 one
real job each through `claude -p` (Haiku), `codex exec` and `pi -p` (both
`gpt-6-luna`) wrote its output with no API-key variables in the environment:
Claude Code on the claude.ai Max login, Codex on the ChatGPT login
(`plan_type: pro`), pi on its `openai` OAuth credential
([evidence](../headless-analysis/README.md#evidence-so-far)). With workers
launched from code, the coordinating agent, its driver instruction and the
hand-out/report protocol have no remaining job: scheduling, retries and
judgment become code.

## Constraints

- **Workers load the project's configuration** (operator, 2026-10-18): each
  runs in the prepared worktree with that harness's normal AGENTS.md /
  CLAUDE.md, skills, settings and permissions. No mdflow-style isolation.
- **The workflow's requirements do not change in the port**: roles, inputs,
  output types, acceptance checks, correction and verification rules,
  attempt limits, publication conditions and provenance stay as ADRs 098–117
  state them. A behaviour change is a separate decision, recorded as one.
  [Replaceable workflow orchestrators](../../reference/proposals/replaceable-workflow-orchestrators.md)
  is the frame: requirements portable, machinery replaceable.
- **Batch 22 and earlier runs are not disturbed.** Batch 22's packets in
  [agentic-system-reruns](../agentic-system-reruns/README.md) pin method
  commit `5af51ae1f` and the Pi coordinator route; about 290 prepared
  worktrees hold engine runs, some failed or unintegrated. The port lands on
  main without changing them; a run on the new method needs a deliberate new
  release selection there. Before deleting the engine, confirm how old runs
  are inspected, reset and integrated (phase 6).
- **Compare only same-model runs** when judging equivalence (Luna on pi for
  tests, Sol on Codex for production).
- **The port declines the requirements listed under
  [Exclusions for phase 3](#exclusions-for-phase-3-2026-10-19)** (Astra's
  review, 2026-10-19). Each exclusion names the machinery it removes; code
  that restores one is a behaviour change to decide, not robustness work.

## What stays, what goes

From the engine survey (2026-10-18):

| Engine part | Lines | Fate |
|---|---|---|
| `plan.py`, `compact.py` (plan loading, role expansion into check/apply jobs) | 850 | Replaced by the script; the derived check and apply steps become explicit calls |
| `engine.py`, `run.py`, `store.py` (advance, readiness, records, attempt counting, coverage) | 1,460 | Replaced by `Run.ask`/`checked`/`gather` and the answer cache; coverage becomes an explicit final assertion |
| `handouts.py` (prompt composition) | 300 | Coordinator protocol goes; prompt shape (instruction, bindings, inputs, outputs, prompt section) moves into the script |
| `reset.py`, `inspection.py` | 340 | Replaced by deleting cache entries and a status command over `log.jsonl` |
| `handlers.py`, `checks.py` (check, apply-verification, artifact check, correction protocol) | 440 | Kept as domain logic, re-signed from `CodeAttempt`/`Candidate` to plain values |
| `sources.py`, `effects.py`, `worktree.py` | 1,060 | Kept; mostly already plain-value |

About 3,000 lines go. In `src/commonplace/lib/agentic_analysis/` about
2,260 lines import engine types (`CodeAttempt`, `Run`, `RunStore`,
`Candidate`); their cores already call plain-value functions.

## Gaps in the primitives

Found by comparing the engine with `headless-analysis/jobs.py`; each is
resolved in phase 1 or 2, or deliberately dropped with a reason:

1. **Cache by input content.** The key hashes the prompt only; a prompt that
   names an input file by path would hit a stale answer after that file
   changes. Inputs must enter the key by digest (instructions, upstream
   outputs, type specs).
2. **Corrections as the engine does them.** A rerun receives the previous
   outputs and the blockers and must write an `answers` output with one
   `corrected:`/`declined:` line per blocker; "corrected" with identical
   bytes is rejected. `checked()` only appends problems.
3. **Cross-job verification loops.** A verifier's refusal reruns the authors
   it refused, their checks, then the verifier, all within the attempt
   limits. `checked()` covers one job.
4. **Problem, refusal and failure.** Engine `problem` is a failed attempt
   that counts toward the limit; engine refusals are code judgments; the
   draft's `refusal.md` is a cached result. Map these explicitly, and count
   failed launches and incomplete outputs toward the attempt limit.
5. **Worker identity and provenance.** Publication requires each role's
   attempt record with model and effort and that all workers used one model.
   The engine trusts self-report; headless launches pass `--model`, and the
   harness output or session file may record the model actually used.
6. **Worker self-validation.** The prompt section tells workers to run
   `commonplace-run validate-output <prompt-path>`, which resolves only
   engine hand-outs.
7. **Artifact materialization.** Draft validation reads accepted members in
   the run's `artifact/`; the cache stores outputs only in its records.
8. **Concurrency and locking.** No global worker limit, no cross-process run
   lock.
9. **Usage limits and permissions.** Unknown exhaustion messages; headless
   workers cannot answer permission prompts.

## Plan

Each phase ends with the selected tests passing and a commit.

0. **Probes** (authorized). Find each harness's usage-limit message and exit
   status; choose a permission setting per harness that lets an analyst read,
   write and run `commonplace-*` in a worktree without prompts; check whether
   Claude's JSON result, Codex's events and pi's session record the model
   actually used. Decides gaps 5 and 9.
1. **Primitives** in `headless-analysis`: inputs by digest in the key, a
   correction call matching the engine's protocol, attempt counting that
   includes failures, a worker limit, a run lock, materialized accepted
   outputs, a replacement for `validate-output`. Fake-harness tests for each.
2. **Domain code to plain values.** Re-sign `opening`, `acquire`, the
   declared checks, `apply_verification`, `artifact_check`, `assemble` and
   `publish` in `lib/agentic_analysis/` so the script calls them with bytes
   and paths. The engine keeps working through thin adapters until phase 6,
   so batch work on main is not blocked.
3. **The workflow script.** Port `plan.yaml`'s 14 jobs: opening, acquire,
   boundary (2 attempts, branch on its disposition), runtime then memory,
   epistemic and workflow in parallel, reconciliation, artifact check, report
   verification with its correction loop, memory profile and its
   verification, synthesis and its verification, assemble, publish. Prompts
   are composed from the existing `jobs-engine/*.md` instructions and prompt
   section. The script is ordinary functions for this one workflow:
   - The correction cascade is written in explicit order. A verifier's
     refusal leads directly to the correction calls of the authors it
     refused, their checks, then the verifier again, under ADR 108's budgets
     held as plain counters in the calling function (gap 3). No readiness,
     judgment-scope or coverage state is kept; publication asserts that every
     required member's current bytes passed its check.
   - The script asserts the worktree pins at start (HEAD equals the
     preparation commit, clean tree, running package equals the method
     commit) and relies on them for cache replay; it does not discover what
     a worker read.
   - A process killed between a launch and its record repeats that work on
     the rerun; the script does not reconcile interrupted attempts.
   - Provenance is filled from the launch records (audit item 1).
   A fake-harness end-to-end test drives the complete, blocked and
   out-of-scope branches, plus one cascade: a report verification refusal
   that corrects two authors, re-checks them and re-verifies, and a budget
   exhausted mid-cascade. The review of the script checks each exclusion
   against the code: which machinery it removed, and whether any crept back.
4. **Commands and instructions.** `commonplace-analysis prepare` stays;
   `start` plus the driver become one `run` command without `--harness` that
   refuses a second controller through the run lock; `inspect` becomes a
   status view over `log.jsonl` and the answer cache; a retry is deleting a
   cache entry and rerunning; `integrate` and the publication reset read the
   new records, and the reset keeps its journal reconciliation.
   Rewrite `SKILL.md` and the worker rules (audit items 5 and 8); delete
   `drive-a-code-scheduled-run.md` and the Pi coordinator agent if nothing
   else needs them; update `commands.md` and the prompt section.
5. **Equivalence pilot.** Run one system already analysed on the engine,
   same profile, and compare: validation result, accepted members, attempts
   used, corrections, wall time. Operator decides whether differences are
   defects of the port. Then a small batch (3–5 systems) driven by a loop over
   systems.
6. **Retire the engine.** ADR revising 113 and 117 (and 101/106 where run
   start and IDs change), stating the declined requirements and attempts as
   recorded executions. Unfinished engine runs are not migrated: decide how
   old worktree runs stay inspectable and integrable (likely: their own
   pinned `.venv`, since `prepare` installs one per worktree; verify). Delete `artifactrun/`, its tests, `commonplace-run`,
   `run_values` in `validate_notes`, and `prepare`'s origin startup guard and
   HEAD-behind-main stop (audit item 6). Close this workshop and
   `headless-analysis`.

## Architecture audit (2026-10-19)

Posed by the operator after phase 2: does the port carry requirements of the
engine and its coordinating agent that make no sense when code launches the
workers? The audit read the plan, the job instructions, the driver, the
engine's hand-out and check code, publication and the primitives, with an
independent survey of ADRs 098–117 classifying each requirement as workflow,
engine or mixed. Result: the workflow requirements (roles, types, acceptance,
the correction protocol, the verification protocol, pinned judgments,
publication from a prepared worktree, integration) stand. Ten items existed
only for the coordinator; the operator decided to simplify ("OK - simplify"):

1. **Provenance from launch and harness records.** Workers no longer
   self-report model and effort: no ADR asks for it, the script sets the
   launch model, and each harness records the model it used (phase 0).
   `Provenance` is the recorded model and the output digest; the manifest's
   `worker` block keeps profile, harness, launch-model, effort and model and
   drops the per-role `reported-effort` (optional in the schema; retained
   manifests keep theirs). The worker rules' "Report your runtime" section
   and the `worker-identity` file go with the engine. Done in phase 2's code.
2. **Attempt counting by ADR 108's budgets.** An attempt is one execution of
   a job (ADR 113); the engine counted failed launches because the coordinator
   reported them. Now a timeout or an incomplete result spends an attempt (the
   worker spent its work); a launch that still exits nonzero after its
   relaunches is an environment failure that stops the run and spends none,
   so a rerun after the repair asks again. The script implements ADR 108's
   budgets (three record verifications, two profile corrections, one
   synthesis correction, runtime corrections before memory and epistemic ones)
   directly, not as per-job attempt records. Done in the primitives.
3. **Relaunch on any nonzero exit, bounded.** The driver's three provider
   messages were observed in a launch tool's results and its "only when the
   caller authorizes" clause has no referent in code. Two relaunches with
   30 s and 120 s waits, usage limits excluded, timeouts not relaunched. Done
   in the primitives; re-derive from observed headless failures in phase 5.
4. **`problem`, not `refusal`, for a worker's inability report.** The
   primitives had reused "refusal", which names code's rejection of a
   candidate (ADR 116). A problem is a result the script stops on; the
   operator clears the cache entry to retry. Done in the primitives.
5. **One profile per run stays as a research choice** (compare same-model
   runs), no longer a mechanism. `--harness` on start, the per-harness default
   profile and the refusal of a profile from another harness existed because
   the coordinator could launch only its own harness; they go with the
   coordinator route in phase 4.
6. **The origin checkout's startup guard and the HEAD-behind-main stop in
   `prepare`** existed because the coordinating agent had loaded the origin's
   AGENTS.md, skills and settings. A headless run is a process; nothing it
   loaded reaches a worker. Both go when the coordinator route is deleted
   (phase 6); the worktree-side pins (HEAD equals the preparation commit,
   clean tree, running package equals the method commit) stay. This also
   removes the reason this port needed a sibling worktree.
7. **The judgment, scope and coverage record model** (scoped judgments,
   holds, superseded, refusal in force, coverage input, `verified-by` gates,
   order-only reads) served readiness with several open attempts. The script's
   call stack replaces it: when a verifier refuses a subject, the script
   reruns the correction, its check and the verifier; publication asserts
   that every required member is accepted by its current check. The script
   does not reimplement `Judgment.scope`.
8. **Coordinator residue in the worker rules and hand-out** (`job`,
   `attempt`, `prompt-path`, `workspace`; "closed attempt workspaces are
   disposable"; "read engine state only through this prompt's inputs"; "the
   coordinator owns scheduling"; the hand-out's duplicate-read validator; the
   launch pointer's "you may read this supplied prompt file") is deleted, not
   rephrased, in phase 4. Reading batches stay: truncation is a harness
   property.
9. **`integrate` and the publication reset read engine records** (run.json,
   the inspect view, the publish job's current outputs, the run store). The
   plan's "integrate stays" was wrong; phase 4 re-points both at the script's
   records.
10. **Self-validation** (ADR 105) stays as the analysts' convenience; the code
    check runs regardless. Phase 1's replacement of the resolver stands.

Each item is a behaviour change the retiring ADR states; gap 5 is resolved
by item 1 and gap 9's usage half by phase 1.

## Exclusions for phase 3 (2026-10-19)

Astra's review of `1c7542336` (relayed by the operator) accepts the audit
and asks that the requirements the port declines be stated once, bindingly,
so that later "robustness" work cannot restore them, and that phase 3 be
judged by whether each exclusion removes machinery. The list:

| Declined requirement | What it removes |
|---|---|
| Several controllers advancing one run | Readiness, replay, `step`/`fill`; one process owns control flow and the run lock rejects a second |
| Workers reporting asynchronously to a coordinator | Reporting, hand-out validation; calls return outputs |
| Resuming an engine run with the new code | Migration; old runs keep their pinned worktree and venv (phase 6 confirms) |
| Cancelling a parallel group at its first failure | Cancellation; `gather` waits for the group, then propagates |
| Automatic recovery from every operational failure | Launch ownership and reconciliation; the run stops, the operator repairs and reruns |
| Exact attempt counts across an abrupt interruption | Durable launch ownership; see below |
| A general scheduler or judgment-coverage state in the script | `Judgment.scope`, holds, coverage input (audit item 7) |

Three contracts follow from it:

- **Cache.** The key covers the prompt, the supplied inputs' digests, the
  output names and the profile; it does not cover what a worker reads from
  the worktree or the project's configuration. The contract is that a run
  belongs to one pinned method and source environment: the worktree-side
  pins (HEAD equals the preparation commit, clean tree, running package
  equals the method commit) hold for the run's whole life, and a changed
  environment is a new run, not a cache invalidation. Phase 3 asserts the
  pins when the script starts and does not try to discover filesystem
  dependencies.
- **Interruption.** `ask` records an answer or failure after the launch
  returns, so a process killed in between leaves the worker's output
  unrecorded; the rerun asks again and the work repeats. This is accepted:
  the ADR 108 budgets bound correction rounds and the evidence the script
  records, not the number of executions that ever occurred. The ADR revising
  113 states attempts as recorded executions.
- **Publication.** The intermediate cache tolerates a repeated call;
  publication does not. `publish_analysis` keeps the publication lock, the
  exact manifests, the destination checks and the reset's journal
  reconciliation, because they protect the retained artifact against a
  silently replaced incumbent. Simplification stops at the publication
  boundary.

The plan's phase 3, phase 4, phase 6 and the decision gate carry these into
the work. The correction cascade in explicit order is the part the
primitives have not yet demonstrated; it is phase 3's main result.

## Phase 4 results (2026-10-19)

The code moved into the package and is pinned by the worktree guards like
the rest: `headless-analysis/{headless,jobs,corrections}.py` became
`src/commonplace/headless/{harness,jobs,corrections}.py` (plus `run_lock`,
the lock a `Run` takes, for the commands that must not overlap a run), and
`analyse.py` became `src/commonplace/lib/agentic_analysis/workflow.py`
(`run_analysis` replaces its `main`). `commonplace-analysis` is now
`prepare`, `run`, `inspect`, `reset` and `integrate`:

- `run` starts a run (`--system`, `--source-identity`, `--source`,
  `--worker-profile`, optional `--source-revision`, `--timeout`,
  `--max-workers`) or resumes one (`run <run>`), exits 0 complete, 2
  stopped, 1 failed, and refuses a second controller through the run lock.
  `start` and `--harness` are gone (audit item 5): the profile is named, and
  `worker-profiles.yaml` lost its per-harness `defaults`.
- `inspect` is a status view over `log.jsonl`, the answer cache, `artifact/`
  and `receipt.json`: state (`published`, `local`, `stopped` with reason,
  `running`, `interrupted`, `allocated`), per-job launches, answers with
  their cache files, failures and rejections, verdicts, problems, member
  digests, receipt. A retry is deleting an answer's cache file and rerunning.
- `reset` withdraws an unreleased worktree publication: the engine's reset
  hook's checks were extracted into `_unreleased_publication`, shared with
  the engine hook until phase 6; the withdrawn tree and journal move under
  the run's `withdrawn/<time>/`, the incumbent moves back from the archive,
  the receipt is deleted.
- `integrate` proves publication from `code/opening.json`, `receipt.json`
  and `parameters.json` against the retained bytes and the archive (audit
  item 9); the engine's fixed-plan and type digest checks are dropped, since
  `merge_paths` refuses tracked changes outside the merged paths, so a method
  file changed in the worktree cannot be integrated.

Instructions: `SKILL.md` rewritten for the headless route (confirm target,
prepare, `run`, stops and reruns, report with `inspect`, integrate);
`follow-worker-rules.md` without the coordinator residue (audit item 8:
`job`, `attempt`, `worker-identity`, `workspace`, "Report your runtime",
engine state, coordinator ownership; the inputs table names what
`Analysis.prompt` and `Run.ask` emit, after the review added the frame's
`identity`/`cites`/`verifies` and criteria-file names and the workflow stopped
emitting the plan's always-absent `refusal:<role>` reads); `drive-a-code-scheduled-run.md`
deleted with its redirects re-pointed at the skill; `publish-analysis.md`,
the collection, `check-subagent-harness.md`, `commands.md`, the plan header,
the Pi docs and the boundary instruction's title updated. The Pi coordinator
agent (`.pi/agents/commonplace-coordinator.md`) stays: the rerun batches on
main still launch through it, and batch launching for the new method is the
phase 5 decision. `commonplace-run` and the engine stay until phase 6; the
`jobs-engine/` directory name goes with them.

Tests: `tests/commonplace/headless/test_jobs.py` (the selftest as 14 pytest
tests, about 6 s), `tests/commonplace/agentic_analysis/test_workflow.py` (17
slow tests, about 105 s: the five of phase 3 plus `inspect_analysis` after a
complete run and after a stop, the CLI refusing a held run, a CLI stop then
a retry by deleting the cache entry, `integrate` merging a published run into
an origin's `main` through a linked worktree, `reset` withdrawing a
publication with and without an incumbent and a rerun publishing the same
bytes again without a launch, `reset` refused with nothing published, an
interrupted withdrawal finished by a second `reset` while a `run` meanwhile
stops, the state view after a stray `start`, and the profile refusals before
any launch), the member generators moved from
`test_profile.py`/`test_verification.py` into `execution_fixtures.py`, the
`prepared_template` fixture completed with the types' link targets, and the
lifecycle tests (`test_integration.py`, `test_worktree.py`,
`test_analyses.py`) rewritten for the records. The engine's
`commonplace-analysis inspect` test and the driver-delivery test were
deleted with their subjects.

An independent review of the phase (code, instructions, residue, exclusions)
found no excluded mechanism restored and six defects, all fixed: `inspect`
derived the state from the whole log, so a resumed run killed midway showed
the old stop and a reset run showed `interrupted` (now the state is read from
the events after the latest `start`, with `withdrawn` logged by `reset`); the
exit-code contract excluded guard refusals, environment errors and uncertain
effects (now every stop the workflow logs exits 2, `STOPS` in `workflow.py`);
a profile's harness was checked only at the first launch, after acquisition
(now `Analysis` refuses an unknown harness, a command missing from `PATH`,
non-mapping `flags` and `flags` overriding the unattended settings before
anything runs); `reset` on a run with nothing published deleted its receipt
(now refused); a withdrawal interrupted between its two moves needed manual
recovery (now the journal is marked `withdrawing` first and a second `reset`
finishes it, while a `run` meanwhile stops on the unrecognised journal); the
receipt was not written atomically. Writing the reset tests found a seventh:
the overview and manifest listed members in the order the workers finished,
so a rerun's publication bytes differed from the first run's; members are now
ordered by the layout's roles and the rerun test compares the receipts byte
for byte. The review's residue findings in
`check-subagent-harness.md` (requirements A1, A2, R4 and the round probe
still described a coordinator launching workers), `commands.md` and the Pi
delegation contract were fixed too.

## Phase 3 results (2026-10-19)

The workflow script is `headless-analysis/analyse.py`: `start` allocates a
run in a prepared worktree and `run` resumes one; `Analysis.analyse()` is
the control flow, 325 lines in one class, with the plan file read as data
(instructions, outputs, reads, budgets, criteria groups, declared checks and
feedback, the frozen-source role, the prompt section). Prompts keep the
engine's frame (`Follow <instruction> with:`, `name = value` lines, the
rendered prompt section, reading batches and ranges); the attempt's paths
enter through tokens `Run.ask` fills after keying. The primitives gained
those tokens, `Answer.attempts` for per-job budgets, and `produce`, which
covers a first attempt, its check-driven retries and a verifier's correction
under one protocol, including the engine's rules for roles without an
`answers` output. The prompt section now names
`commonplace-validate {output} --artifact {artifact} --role {role}` for
both routes.

Verification: `headless-analysis/test_workflow.py` drives the script with a
fake harness through the engine tests' prepared-worktree and local-Git
fixtures, members built by the fixture generators (5 tests, slow): a
complete run with one correction round (runtime and memory refused;
runtime corrected before memory; epistemic and workflow not re-asked;
reconciliation re-asked under a new key; the manifest's model is the
harness-recorded one), blocked and out-of-scope boundaries (nothing but the
boundary asked, not published), the verifier's budget exhausted (three
verdicts, no correction after the third, nothing published), and a resume
after a synthesis problem (no earlier role re-launched). The primitives
selftest and the analysis and engine suites pass. An independent review of
the script against the plan, ADRs 108/113/114, the engine's check and
hand-out semantics and the exclusions found one defect (roles without an
`answers` output were held to correction answers) and eight deviations;
the script now matches the engine on: `previous-*` handed on every rerun,
no attempt spent on a role whose reads are unchanged, partner snapshots per
the derived check and apply jobs (identity, cites and frozen source for
producers; reads for verifiers; no incumbent for verifiers), members
re-checked against their partners after the parallel round and after each
correction round with a structural refusal when one fails, line ranges for
oversized inputs, the verifiers' `refusal:<role>` read absent as the engine
resolved it, and a final assertion that every member passes its check
before assembly. Parallel candidates are checked against the members
present before their round, so a rerun's checks do not depend on thread
timing.

Deviations kept, to decide at phase 5:

- Blockers at a verifier's last attempt stop the run before any correction
  is asked (ADR 108's text); the engine still ran the refused authors'
  corrections and a reconciliation before stopping.
- Every check validates against all criteria groups plus the whole type
  closure, a superset of the engine's per-job closure.
- A refusal handed to a producer is the findings body; the engine prefixed
  frontmatter with refusal id, version and scope.
- Reconciliation asked afresh after a correction round spends its budget
  (3), as in the engine; three rounds fit exactly, and a single check
  rejection of a fresh reconciliation ends the run.

Known gaps: the script's own code is not pinned by the worktree guards until
phase 4 moves it into the package; `test_workflow.py` imports member
generators from `test_profile.py` and `test_verification.py` (test modules
as fixture libraries) and copies the types' link targets into the prepared
worktree because the `prepared_template` fixture pins criteria whose links
publication checks; both move into `tests/` fixtures in phase 4. The
re-check path is exercised only by members that pass; no fixture fails
against a sibling yet.

Decision gate: 325 lines of control flow, no scheduler, no readiness or
coverage state; the cascade is plain calls with per-job counters. Proceed
to phase 4.

## Phase 2 results (2026-10-18)

The domain code takes plain values; the engine keeps working through thin
adapters. Three extractions, each with its tests and an independent review
of the diff by a fresh agent:

- **Candidate checks** (`artifactrun/checks.py`). `Candidate` carries plain
  values (run directory, layout, relations, type, criteria, run values, the
  declared inputs' bytes); `check_candidate`, `apply_verdict`,
  `artifact_check` and `judgment_scope` return findings and judgments. The
  engine's standard handlers (`artifactrun/handlers.py`) build the candidate
  from the attempt and stage what they return. The analysis's declared
  checks read `Candidate.inputs`.
- **Opening and acquisition** (`lib/agentic_analysis/opening.py`) take the
  parameters, the worker profiles, the run directory and the library.
- **Assembly and publication** (`lib/agentic_analysis/publication.py`) take
  the members by role, the metadata, the acquisition result, a `Provenance`
  per role (since the audit: the model the harness recorded and the output
  digest), the layout, type, criteria and run directory. The
  record-structure part of provenance (kind, job, output key) stays in the
  adapter, which feeds the engine's worker-reported model until the engine
  is retired; the headless script fills `Provenance` from its launch records.

The analysis's engine adapters live in `lib/agentic_analysis/handlers.py`,
which `plan.yaml` names; it also re-exports the publication reset hook,
which the engine looks up beside the handler. Known drift, accepted: when a
run has several defects at once, the adapters may report a different first
error than the old handlers did (provenance structure is now checked before
the boundary classification). A run started before this change has the old
handler paths frozen in its run store; advancing it with this code would call
a plain function with an attempt. Old runs advance with their worktree-local
commands, which pin their own code, so this only bars advancing an old run
from a newer checkout. Full fast suite: 1,591 passed; the slow analysis
tests pass.

## Phase 1 results (2026-10-18)

In `headless-analysis` ([evidence](../headless-analysis/README.md#evidence-so-far)),
with fake-harness selftests for each:

- Gap 1: inputs enter the key by digest; records keep the digests.
- Gap 2: `corrections.py` implements the engine's correction protocol over
  the engine's own `correction_findings` and `refusal_findings`.
- Gap 4: a failed launch or incomplete result is persisted per key and counts
  toward the attempt limit across reruns; a usage-limited launch stops the
  run without counting and without a relaunch (gap 9, usage half; the
  messages are build strings, unobserved in a real exhaustion).
- Gap 6: no resolver; the prompt names the `commonplace-validate` command
  with the output, artifact and role the script already knows.
- Gap 7: `Run.accept` materializes accepted outputs under `artifact/`.
- Gap 8: `Run(max_workers=)` and an exclusive run lock.

Open after phase 1: gap 3 (phase 3), gap 5 (the harness-recorded model is
not yet read into the record) and gap 9's permission half.

## Phase 0 results (2026-10-18)

Probes: `headless-analysis/probe.py`, run in this checkout with outputs in a
scratch directory and no API-key variables, Haiku on Claude Code and
`gpt-6-luna` on Codex and pi, low effort.

- **Unattended work.** All three workers read AGENTS.md, ran `rg`, ran
  `commonplace-validate --help` and listed the `analyse-agentic-system` skill,
  in about 16 s each, with no prompt. Settings that sufficed:
  - Claude Code: `permission-mode: acceptEdits`, the project's
    `Bash(commonplace-*)` allowance, and `add-dir` for a run directory outside
    the checkout (not needed when the run directory is in the worktree).
  - Codex: `sandbox: workspace-write`; writes outside the checkout went to
    the scratch directory under `/tmp`.
  - pi: `--approve`, without which pi ignores project-local files; this is the
    flag that makes a pi worker load the project's configuration, so it
    belongs in the pi defaults.
  Not probed: a denied action (what a headless worker does when a tool is not
  allowed), and runs inside a prepared worktree.
- **Model actually used.** Each harness records it: Claude Code's JSON result
  (`modelUsage`: `claude-haiku-5-5`), Codex's session file (`turn_context`
  payload `model`) and pi's session file (`model` on each reply). This can
  replace the workers' self-reported `worker-identity` (gap 5); the workers
  themselves could not name their model on Codex or pi.
- **Usage limits.** Not triggered; strings in the installed builds only.
  Claude Code 2.1.302 says "Usage limit reached" in several forms; codex-cli
  0.162.1 says "You've hit your usage limit…"; pi passes provider errors
  through and retries HTTP 429 itself with backoff. Proposed rule for phase 1:
  a failed launch whose output contains "usage limit" (any case) stops the run
  as usage-limited instead of retrying, and the operator reruns after the
  reset; the answer cache resumes it. Exit status and stream are unverified.
- **Resumption.** Rerunning the probe returned all three answers from the
  cache without launching a worker.

## For the ADR

Points the ADR retiring the engine must state:

- **Why the step program did not stay simple** (operator, 2026-10-18). With one
  execution thread, a step program is simple: replay the script, and every
  model job is either recorded or the next one to hand out. With parallel
  executions it unravels: several attempts are open at once, so the shared
  run state needs consistency rules for each open attempt, which round it
  belongs to, inputs changing while it runs, results reported late or twice,
  and which workers are known to have stopped. The engine's run lock,
  readiness rules, attempt closing and reset machinery largely exist to
  enforce them.
- **What the headless script keeps of that** (proposed, to confirm in phase
  3). Control flow lives in one process's call stack, and parallel calls share
  only the answer cache, where each entry is written once under its own key.
  The consistency needed reduces to a per-key lock, atomic record writes and
  a run lock against a second process. Whether the verification cascade keeps
  it that small is what phase 3 shows.
- **The declined requirements** from the exclusions table, each with the
  machinery it removes, and the three contracts (cache over a pinned
  environment, repeated work after an interruption, publication guarantees
  kept). An attempt is a recorded execution of a job.

## Returns to decision

- After phase 0: if a harness cannot run unattended (permissions or usage
  limits), the port targets the others, and that harness is listed as
  unsupported.
- After phase 3: if the script exceeds about 600 lines of control flow, or
  the verification cascade does not fit plain calls, or the script needs a
  scheduler (readiness or coverage state beyond the call stack), reconsider
  a small declarative layer before phase 4 rather than writing the scheduler.
  Passed 2026-10-19 (phase 3 results).
- Phase 5 is the decision point for adoption; nothing in phases 1–3 deletes
  engine code.
- Batch launching (a shell loop over systems) is barred for batch 22; for the
  new method it is the operator's call at phase 5.

## Working arrangement (2026-10-18)

Batches 21 and 22 run from the main checkout at `/home/zby/llm/commonplace`:
each Pi coordinator starts there, loads that checkout's startup files and
calls `commonplace-analysis prepare` through the user-level editable tool,
whose code is that checkout's `src/`. Preparation refuses a launch when any
startup file there differs from the pinned method commit, and a `src/` edit
there is run by the next coordinator. So the port is developed on branch
`headless-port` in the sibling worktree `/home/zby/llm/commonplace-headless`,
created from `b12b855f4`.

- The worktree has its own `.venv` from `uv sync`. Tests run as `uv run
  pytest`. When a command must run the branch's code, call the worktree's
  `.venv/bin/commonplace-*`: this deviates from the rule against project-venv
  paths because the user-level tool is the live coordinators' code and
  [INSTALL.md](../../../INSTALL.md) forbids repointing it during an analysis.
- Merge main into the branch before each phase commit; main advances with
  integration commits from the reruns.
- Land a phase on main by fast-forward merge in the main checkout only while
  no `bash-2x.sh` batch is running. Phase 1 touches only
  `kb/work/headless-analysis/` and may land at any time; phases 2 and 4 change
  `src/` and `SKILL.md` and wait for a gap between batches. A batch script
  captures `HEAD` at start, so the next batch runs the landed method
  deliberately.
- Sessions started in the worktree share the main checkout's auto-memory
  through a symlinked memory directory.

## Closes when

The engine is retired by ADR and its code deleted, or the operator abandons
the port after the pilot. Either way the conclusion goes to an ADR (or a note
on why headless orchestration did not fit) and this directory is deleted.
