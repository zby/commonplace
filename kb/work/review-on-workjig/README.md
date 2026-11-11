# Review workflows on Workjig

**State on 2026-11-10:** the three workflows, the retirement of the store
and its commands, ADR 127 and the rewritten documents are built and
committed. The [plan](./plan.md) records what was built, the live runs
and what remains for the operator: the first collection sweep, keeping or
reverting one result from each workflow, and deleting the abandoned
local data. Phase 5 of the plan then removed mid-run writes and
`--resume`: a run writes the note once, at its end, and repeating a
command continues its run. Its explicit-approval correction is now
implemented: repeating never approves a strike selection or final publication;
routine plan approval has been removed. Both selected ordinary revisions
completed through operator-approved publication. Live selection and full-pass
trials remain open. The [planning-free baseline](./planning-free-baseline.md)
now separates fixed single-pass execution and single-criterion review from
explicit assessment and composition. Evaluate those operations independently
before broader automation; fake-worker checks establish control flow, not
judgment quality. Phase 6 is a bounded
follow-on ingest experiment, not built; shared operations across Workjig
and agent orchestration remain a future direction. Neither extends this
review workshop's closing conditions. The sections below are the framing and design as posed;
where they describe the store-based system as present, read them as the
starting state.

## Goal

Rebuild the review and freshness system as Python workflows over Workjig,
through `commonplace.headless`, so that a gate sweep, the full improvement
pass and a simplification revision are three workflows in one small runtime
instead of an agent-orchestrated pipeline over a SQLite store. Two
properties are the point: simpler, in that the store, its commands and its
state machines go away where the runtime already supplies them; and more
flexible, in that adding a workflow means writing one Python function over
`ask`, `checked` and `gather` plus its criterion files.

Posed by the operator on 2026-10-23. The operator's direction: convert the
system described in [README-REVIEW-SYSTEM](../../reference/README-REVIEW-SYSTEM.md)
to Workjig, possibly using the structural (directory) types as well;
simplify it and make it more flexible; the
[full improvement pass](../../instructions/run-full-improvement-pass-on-note.md)
could be one workflow in it; the
[simplification passes](../../instructions/simplification-passes/README.md)
have interactive parts and need care.

## Starting state

The review system is the largest subsystem the headless runtime has not
reached. Measured 2026-10-23 and re-measured 2026-11-09; the code sizes did
not change, because no commit touched the review or freshness code between
the two dates:

| Surface | Size |
|---|---|
| `src/commonplace/review` and `cli/review` | 6,059 lines, 11 console commands |
| `src/commonplace/freshness` and `cli/freshness_*` | 1,432 lines, 3 commands |
| full pass guard and library | 510 lines, 1 command |
| tests under `tests/commonplace/review` and `freshness` | 5,855 lines in 25 files |
| ADRs that decide review or freshness behaviour | 12 of 125 |
| `kb/reports/state/commonplace-store.sqlite` | 50 MB, 9,217 baselines, 6,947 recorded jobs; the last job completed 2026-09-26 |
| `kb/reports/state/review-jobs/` | 84 MB of prompts and outputs |

Operating documents: the review README (240 lines),
[run review batches](../../instructions/run-review-batches.md),
[review architecture](../../reference/review-architecture.md),
the freshness architecture page (retired into review architecture),
[FIX-SYSTEM](../../instructions/FIX-SYSTEM.md); the full pass instruction
(305 lines) with the [full-pass-report type](../../types/full-pass-report.md),
its guard command and [resolve a disposition](../../instructions/resolve-full-pass-disposition.md);
the simplification passes (eight pass files and
[revise an article or note](../../instructions/simplification-passes/revise-an-article-or-note.md)).

Readers of the store besides the review commands: the warn selector and the
fix system, review triage, `commonplace-status`, retirement (freshness
retire) and relocation (review-store rekeying, which
[relocation-move-map-engine](../relocation-move-map-engine/README.md)
already wants gone). Phase 0 confirmed the code side of this list on
2026-11-09; see [Phase 0 results](#phase-0-results).

The runtime exists and has three consumers.
[ADR 118](../../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md)
and [ADR 119](../../reference/adr/119-analysis-workers-launch-through-workjig.md)
put the analysis workflow on Workjig, and
[ADR 121](../../reference/adr/121-audit-analysis-traces-without-gating-publication.md)
runs its advisory audits the same way; `commonplace-task`
([recurring-task-runner](../recurring-task-runner/README.md)) launches one
runbook through it. `commonplace.headless.jobs` gives `ask`, `checked`,
`gather`, `accept`, a run lock, durable launch records, replay of answered
calls by the work they asked for, worker problems, usage-limit stops, and
`dismiss` and `acknowledge_stopped`, which `commonplace-analysis` exposes
to the operator as `retry` and `acknowledge`. Profiles in YAML name
harness, model, effort and flags. Since the workshop opened the runtime
moved to Workjig 0.3.1 and runs on Windows; the `jobs` interface this
design relies on did not change.

Reading `jobs.py` on 2026-11-09 found three places where the design below
assumed more than the runtime gives. Each is small, and the
[plan](./plan.md) assigns it:

- **One profile per run.** `Run` builds its worker from one profile at
  construction, and the run lock allows one `Run` per root. Item 7's
  per-pass profile needs `ask` to accept a profile, which then enters the
  call's identity and provenance.
- **`accept` writes only under the run's `artifact/`.** A result file
  lives outside the run directory, so the workflow writes it with its own
  atomic write. `accept` stays for per-run artifacts such as a hand-back
  packet.
- **No worker profile is read-only.** The profiles in
  `kb/tasks/profiles.yaml` grant `Edit` and `git commit`, because a task
  commits. Item 5's rule that workers never write the checkout needs
  review profiles without those grants, and a check in code that the
  working tree is unchanged after a run, as `lib/tasks.py` checks
  `leftover`.

## What the runtime already supplies

Most of the review system's machinery exists because an agent in a
conversation coordinated workers through files and a database. Each row
names the review concept and what replaces it when code owns the run.

| Review system | Under Workjig |
|---|---|
| job, rendered prompt, `job-output.md` transport | one `ask` with inputs `note`, `criterion` and one named output |
| model partition, partition registry, `--model` validation at finalization | the worker profile; it is part of the call's identity, and the model the harness recorded is read from the launch |
| job grouping, batch size, result-kind-homogeneous jobs | call granularity chosen by the workflow; `Run(max_workers=n)` bounds concurrency |
| parent-scheduled sub-agents, fresh-context rules, ADR 067's one-prompt-one-output boundary | a headless launch is isolated by construction and writes only its output files |
| all-or-nothing finalization, outcome parser, `ERROR` | `checked()` with the outcome parser as the check; a malformed result is a rejected attempt whose problems go into the next prompt |
| queued, completed and failed jobs, `MANIFEST.json`, `review-job-list` | call status in the run's records; `recorded_calls` |
| full pass phases, re-entrancy preflight, guard captures, immutable `source.txt` and `final.txt` | the run lock, per-launch captured inputs, replay on rerun; a hand-back is the run stopping with the packet in `artifact/` |
| freshness baseline pinned to note and criterion snapshots | **not supplied across runs.** Workjig records are scoped to one run and carry no compatibility promise for their format. The durable baseline is a file the workflow writes with `accept`. |

The last row decides the shape. Freshness independent of Git, the property
the review README puts first, is a hash comparison between the text a
result was produced from and the current text. A result file that carries
both hashes gives it without a store.

## Design direction

A proposal, open until phase 1 has run it. Each item names what would
change it. The [plan](./plan.md) turns the items into build steps and
records the choices it had to make where an item was silent.

1. **A result is a file.** Each completed pair writes
   `kb/reports/state/review/results/<note-path>/<criterion-id>.md` (untracked, as
   the store is now) with frontmatter: note path and SHA-256, criterion
   path and SHA-256, outcome or `report`, profile, recorded model, run and
   launch identifiers; the body is the reviewer's text. The provenance
   fields name an executor, not a harness launch, so a result produced by
   a decision model (future work below) fits the same file. Fresh means both
   hashes match the current files; `missing`, `note-changed` and
   `criterion-changed` are the three other answers. A `status` command is
   a pure function over these files and the criterion catalog. It replaces
   the selector, `freshness-status`, `review-job-list` and the manifest.
   The fix system reads the same files.

   The current system keys a baseline by model partition as well, so a
   review under one model does not satisfy freshness under another. This
   item drops that: one result per pair, with the profile and recorded
   model as provenance. `status` can filter on them, so a sweep can
   re-ask the pairs a named profile did not judge. What would change it: a
   sweep in which the operator wants two models' verdicts on one pair kept
   side by side.

   Gates declare `watches:` (title, description, body), which the current
   system uses only to acknowledge note changes outside the watched
   parts. A result file can serve the same purpose without an
   acknowledgement: the note hash covers only the parts the criterion
   watches, and the whole file when it declares none. This is the first
   candidate answer to the acknowledgement question below, decided in
   phase 1.
2. **One Workjig run per invocation**, under
   `kb/reports/state/review/runs/<stamp>/`, as `commonplace-task` does.
   Replay serves crash-resume within a sweep; result files serve freshness
   across sweeps. A long-lived run was considered and set aside: Workjig
   keeps every call in one `run.json`, and a store of thousands of pairs
   would make it the database this workshop removes.
3. **One call per (note, criterion) pair** by default, so a criterion edit
   re-asks exactly its pairs. The bundle grouping the current system uses
   to share a prompt becomes an option. Phase 0 measures what a one-gate
   launch costs against a bundle launch on the same note; if a launch's
   fixed cost dominates, the default flips to one call per note and bundle.
   Moved on 2026-11-09 from phase 0 to phase 1's first sweep: the gate
   workflow is itself the measuring instrument, and the launch records
   carry the harness's usage evidence.
4. **A criterion is any markdown file.** Catalog gates, a type spec, a
   `COLLECTION.md`, the critique instruction and the compression criteria
   are all the `criterion` input; the workflow names the output contract
   (verdict line, or report) instead of persisting a result kind. The
   conformance pairs of ADR 038 and ADR 041 survive unchanged in meaning,
   since their criterion was already the file. The compression bundle,
   kept outside the review database on purpose, needs no exception any more.
5. **Workflows are functions, one command.** `gates(notes, criteria,
   profile)`, `full_pass(note, profile)` and `revise(artifact, purpose,
   passes, profile)` live in one module (name open) and run through
   `commonplace-review <workflow>` with `status`, `run`, `retry` and
   `acknowledge`, the shape `commonplace-analysis` has. Workers never
   write the checkout: a worker's revised note is an output file, and code
   decides whether it is accepted and written. This is stricter than the
   task runner's rule, and it is what keeps a workflow restartable.
6. **The full pass as a workflow.** Steps 1 to 6 are a `gather` of asks:
   compression, critique, friction, premises, the catalog gates, connect.
   Step 7 is one ask that writes the packet with its structured
   frontmatter; code reads `disposition` and branches. A `keep` asks an
   editor for the edited note as an output, then a copyeditor, and code
   writes the accepted text. The closing cycle is the same asks over the
   new text: new inputs mean new keys, so the launches are fresh and the
   initial records stay. The closing status is one more ask whose answer
   code applies: `ready` accepts, `repair-needed` allows one editor call,
   `hand-back` restores the captured start text. The phase table, the
   re-entrancy preflight, the guard and the capture triple are the run's
   records. What outlives a run is a pending disposition: the packet file
   keeps its hashes, and the resolution instruction keeps its job over
   that file. The full-pass-report type shrinks to the packet; whether the
   guard command survives as the same hash comparison the result files use
   is decided when the type is cut down.
7. **The simplification passes, carefully.** Each pass is already a
   worker packet (purpose, artifact, pass file, defend list, write scope,
   return), so a pass is one `ask` with the artifact as input and the
   revised artifact and report as outputs, run in order with code
   integrating each diff. The `effort: simple | judgment` field selects the
   profile per pass, the first per-role routing in a workflow after
   [runner-execution-profiles](../runner-execution-profiles/README.md)
   deferred it. Three points are interactive today and stay so:
   - the assessment, which the operator reads and may redirect before any
     pass runs: the workflow runs it and stops with the report and a
     proposed plan file; the operator edits the plan, and the next
     invocation takes the edited file as input;
   - the plain-wording list, which the operator strikes before it is
     applied: two asks with the struck list as an operator-supplied input
     between them;
   - narrow-overclaims, which the instruction runs in the parent context
     because the conversation is its evidence: no headless worker has that
     conversation. Either the defend list and purpose carry the evidence
     explicitly, which is what
     [fix what the executor can't determine](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md)
     asks for, or the pass stays interactive and the workflow runs the
     others around it.
   The rule under all three: a workflow stops with a file and a rerun
   continues with the operator's answer as an input.

   **The plan is a decision output.** The assessor chooses the passes and
   code runs them, so the choice must reach code through a channel code
   can parse. That channel is a declared output, not a new mechanism:
   the assessment ask has two outputs, `assessment.md` for the operator
   and `plan.yaml` for code. Declared outputs already carry fresh paths
   per launch, replay, attempt counting and provenance; a side file or
   JSON scraped from stdout would carry none of them. A worker that
   cannot plan writes the problem file, as for any ask.

   ```yaml
   purpose: "..."
   defend: ["claim text", ...]
   passes:              # in run order
     - pass: split-out-a-treatment
       scope: "§3 only"   # optional
     - pass: plain-wording
   stop: null           # or "rewrite-needed: <reason>"
   ```

   Code supplies the choices and keeps the dispatch:
   - the script lists the pass files and their `effort` values from
     `kb/instructions/simplification-passes/` and hands the list to the
     assessor as an input, so the assessor chooses from a closed set;
   - the check parses `plan.yaml` and rejects unknown passes, missing
     fields and an order that breaks the depth order of
     [revise an article or note](../../instructions/simplification-passes/revise-an-article-or-note.md);
     through `checked()`, a malformed plan costs one corrected attempt,
     not a crashed run. The analysis workflow's `verdict_check` is the
     precedent;
   - code branches on the parsed plan: a `stop` accepts the assessment
     and ends the run; otherwise each listed pass is one `ask`, with its
     profile chosen from the pass's `effort` and its diff checked before
     `accept`.

   The operator's edited plan returns as an input, so the passes' call
   identities change only when the plan does, and an unedited rerun
   replays. The same shape serves the full pass's `disposition`, the
   closing status of item 6 and the gate verdicts of item 1, so the
   generic piece is one helper in `commonplace.headless`, roughly
   `decide(job, prompt, schema, choices)`: `checked()` with a parse, a
   schema check and a closed-choices check, returning the parsed object.
   It is written when the first of these workflows needs it, with the
   result file and packet schemas of item 8. Whether the operator
   prefers that to the interactive skill is answered by phase 3, not here;
   the interactive orchestrator stays until then. Workjig's own README
   calls agent-led delegation the right tool for exploratory work, so a
   revision whose passes are chosen as the conversation goes is a
   legitimate reason to keep that path.
8. **Structural types.** A full-pass run directory has fixed roles (start
   capture, method reports, packet, final text) and could carry a layout
   whose closing role `verifies` the final, applied in code as ADR 118
   applies the analysis verifiers. A gate sweep has no fixed roles: its
   members vary by note and criterion. Recommendation: give the result
   file and the packet schemas, and decide a directory type for the full
   pass only after phase 2 shows what validating a run directory as one
   unit would catch that the schemas do not. ADR 114 and ADR 117 keep
   their meaning either way.

## Future work

**Isolation between concurrent runs.** [What review lost in isolation when the store went](./isolation-after-the-store.md)
records, at the operator's request on 2026-11-11, which of the store's
concurrency protections result files keep and which they drop. Nothing is
built until overlapping runs become routine.

**Bounded gates on decision models.** The current system bundled gates to
amortize one worker's context cost. The operator's direction (2026-10-24)
is not to chase that saving by routing easy gates to cheaper chat models
but to wait for judgment-specialized models, the category
[language models for bounded judgments](../../theory/language-models-for-bounded-judgments-form-an-emerging-category.md)
describes, with Jev as the operator's example. A closed-ended gate is the
shape such a model serves: supplied text, supplied criterion, a decision
among `pass`, `warn` and `fail`, with a distribution and a calibrated
deferral instead of prose. The migration is deferred because its real
cost is calibration, not plumbing: deciding per gate whether the
specialized model's accepted-case error, coverage and deferral match the
strong reviewer, under the never-run
[calibration proposal](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md).

What the present design must not foreclose, and does not: a decision
model is called from Python, not launched as a harness worker, so a gate
workflow needs an executor abstraction beside `ask`, and the result file
records which executor judged (item 1 above). Two cautions from the note
carry over. Grouping several questions in one request is a semantic
choice for at least one of these models, not a batching optimization, so
the bundling question returns as a quality question if it returns at all.
And a decision model selects an option without its justification, so a
`warn` from it has no finding text for the fix system to consume; the fix
path would need a second, generating call or the strong reviewer.

## What would be retired

Candidates, each confirmed or rejected in phase 1 against a named reader:
the SQLite review and freshness store with its schema, migrations and
backups; the selector, create-jobs, finalize, ack-review,
ack-trivial-note-changes, review-job-list, resolve-criteria,
freshness-status, freshness-ack and freshness-retire commands; the model
partition registry; link-consumption and availability telemetry;
result-kind homogeneity and job grouping; all-or-nothing finalization;
`MANIFEST.json`; relocation's review-store rekeying (result files key by
path, so a move is a path rewrite in files or a re-review).

Acknowledgement, which advances a baseline past a change that does not
invalidate the evidence, has no replacement planned. Phase 0 counted its
use (below): 37 of 9,217 current baselines stand on one. That is rare, so
the rule is re-review, softened by the watched-parts hash of item 1, and
an acknowledgement command returns only when a sweep shows the cost.

A new ADR would supersede ADR 010, 035, 043, 052, 065 and 067 and amend
038, 041, 051 and 080. The review README, run review batches, both
architecture pages and the full pass instruction are rewritten as the
operating documents of the new command or retired.

## Existing state

The 9,217 baselines are not migrated. The operator judged on 2026-10-24
that the stored reviews are outdated, so the new system starts empty and
the first sweep produces its own baselines. The store file and
`review-jobs/` stay on disk, untracked, until phase 4 deletes them; nothing
reads them meanwhile.

## Phase 0 results

Measured 2026-11-09 from the store and the code. No worker was launched.

**Acknowledgement use.** An acknowledgement leaves a baseline whose
accepted input snapshot differs from the snapshot its evidence pair
reviewed. 37 of 9,217 current baselines are in that state on the note
side and none on the criterion side. The count is a lower bound on
historical use, because a later review of the same pair replaces an
acknowledged baseline: 3,392 baselines are past their first revision, and
the store does not say which revisions were acknowledgements.

**Readers of the store in code.** Outside `src/commonplace/review`,
`src/commonplace/freshness` and their CLIs, three modules import the
store or the review and freshness packages: `store.py` (path resolution
and schema), `lib/project_status.py` (the review section of
`commonplace-status`) and `cli/store_healthcheck.py`. `lib/relocation.py`,
`lib/full_pass.py` and `lib/promotion.py` do not. Relocation's rekeying
therefore lives inside the review package and retires with it.

**Readers in documents.** Eighteen authored pages outside workshops,
reports, sources, ADRs and the proposal archive name the store or its
commands: the review README, run review batches, review triage,
FIX-SYSTEM and both fix-warnings instructions, the full pass instruction,
retire-artifact, the gate-migration instruction, the theory-layout
upgrade instruction, `commands.md`, storage architecture, where change
candidates come from, one theory note, and four live proposals
(structured output codec, review configuration object,
collection-as-artifact freshness, periodic connect-report mining). Phase
4 rewrites or retires each.

**Launch cost** was not measured in phase 0; see item 3. The first live
pair, recorded in the [plan](./plan.md#live-pair-2026-11-09), cost $0.095,
nearly all of it fixed context.

## Order of work

**Phase 0, measurements**, no code: done 2026-11-09 except launch cost,
which moved to phase 1.

**Phase 1, the gate sweep.** Result files, `status`, `gates`, one command.
Run over one collection with one profile; its results are the first
baselines. Decide call granularity and the acknowledgement question here.

**Phase 2, the full pass.** The workflow of item 6 on notes the current
instruction would accept. Judge it on the same four outcomes the
instruction has: accepted text, one bounded repair, hand-back with the
start text restored, pending disposition that survives the run. Decide the
directory type question here.

**Phase 3, one revision.** The assessment-stop design of item 7 on one
article with the operator, including a struck plain-wording list. The
operator judges whether the stop-and-rerun shape is usable.

**Phase 4, retirement.** Delete the store, commands, tests and documents
the earlier phases made redundant; write the ADR; rewrite the review
README as the command's operating page.

## Evaluation boundary

In scope: the three workflows, the result file and packet schemas, the
command, the status function, the retirement list, and the documents
named above.

Out of scope: the content of any gate or pass; the analysis workflow and
its worktrees (review runs happen in the checkout, as task runs do, and
only code writes it); the task heartbeat, although a stale-gate sweep is a
candidate recurring task once `status` is cheap; per-role routing beyond
the simple-or-judgment split, and decision-model routing (future work); the fix strategy taxonomy; the generic
freshness store for non-review targets, which ADR 065 already withdrew.

## What closes the workshop

The gate sweep, the full pass and one simplification revision have each run
end to end through the new command on real notes, with the operator keeping
or reverting at least one result from each; the SQLite store and the review
and freshness commands are deleted; the ADR is accepted; the review README,
the architecture pages and the instructions are rewritten or retired. The
workshop is then deleted. Durable outcomes go to the ADR, a reference page
for the command, and the rewritten instructions.

---

Relevant Notes:

- [The practical scheduler is the host language](../../theory/the-practical-scheduler-is-the-host-language.md) — rests-on: control flow stays in Python; the runtime journals results
- [An author should fix what the executor can't determine, not what it will](../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) — rests-on: interactive evidence becomes an explicit input or the step stays interactive
- [The boundary of automation is the boundary of verification](../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) — rests-on: code applies verdicts and writes the checkout; workers only produce outputs
- [Error correction works with above-chance oracles and decorrelated checks](../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rests-on: why the full pass keeps several independent asks rather than one
