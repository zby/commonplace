# Review workflows on Workjig

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
reached. Measured 2026-10-23:

| Surface | Size |
|---|---|
| `src/commonplace/review` and `cli/review` | 6,059 lines, 11 console commands |
| `src/commonplace/freshness` and `cli/freshness_*` | 1,432 lines, 3 commands |
| full pass guard and library | 510 lines, 1 command |
| tests under `tests/commonplace/review` and `freshness` | 5,877 lines in 26 files |
| ADRs that decide review or freshness behaviour | 12 of 122 |
| `kb/reports/state/commonplace-store.sqlite` | 50 MB, 9,217 baselines, 6,942 recorded jobs |
| `kb/reports/state/review-jobs/` | 82 MB of prompts and outputs |

Operating documents: the review README (240 lines),
[run review batches](../../instructions/run-review-batches.md),
[review architecture](../../reference/review-architecture.md),
[freshness architecture](../../reference/freshness-architecture.md),
[FIX-SYSTEM](../../instructions/FIX-SYSTEM.md); the full pass instruction
(305 lines) with the [full-pass-report type](../../types/full-pass-report.md),
its guard command and [resolve a disposition](../../instructions/resolve-full-pass-disposition.md);
the simplification passes (eight pass files and
[revise an article or note](../../instructions/simplification-passes/revise-an-article-or-note.md)).

Readers of the store besides the review commands: the warn selector and the
fix system, review triage, `commonplace-status`, retirement (freshness
retire) and relocation (review-store rekeying, which
[relocation-move-map-engine](../relocation-move-map-engine/README.md)
already wants gone). Phase 0 confirms this list from the code.

The runtime exists and has two consumers.
[ADR 118](../../reference/adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md)
and [ADR 119](../../reference/adr/119-analysis-workers-launch-through-workjig.md)
put the analysis workflow on Workjig; `commonplace-task`
([recurring-task-runner](../recurring-task-runner/README.md)) launches one
runbook the same way. `commonplace.headless.jobs` gives `ask`, `checked`,
`gather`, `accept`, a run lock, durable launch records, replay of answered
calls by the work they asked for, worker problems, usage-limit stops and
the operator's `retry` and `acknowledge`. Profiles in YAML name harness,
model, effort and flags.

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
change it.

1. **A result is a file.** Each completed pair writes
   `kb/reports/state/review/<note-path>/<criterion-id>.md` (untracked, as
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
     pass runs: the workflow runs it and stops with the report; the
     operator writes the approved pass list, the purpose and the defend
     lines into one file, and the next invocation takes that file as input;
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
   continues with the operator's answer as an input. Whether the operator
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
invalidate the evidence, has no replacement planned. Phase 0 counts how
often it was used; if it was rare, the rule is re-review, and an
acknowledgement command returns only when a sweep shows the cost.

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

## Order of work

**Phase 0, measurements**, no code: acknowledgement use in the store;
every reader of the store; launch cost of one gate against one bundle on
one note through `commonplace.headless` with the Sonnet profile from
`kb/tasks/profiles.yaml`.

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
