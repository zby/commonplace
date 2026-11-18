---
description: How to operate commonplace-review — criteria, result files and freshness, gate sweeps, status, retry and resume, the checkout guard, worker profiles, cost, single edits, the improvement procedures and the rewrite of a note
type: types/note.md
tags: []
---

# Review system

Review asks a language-model worker to judge a note against a criterion file
and keeps the judgment while both texts stay unchanged. One command,
`commonplace-review`, runs review as Python workflows over headless harness
launches and keeps one result file per (note, criterion) pair. Notes and
criteria stay ordinary markdown files; no database is involved.

Two properties shape the rest:

- **Freshness is independent of Git.** A result records the SHA-256 of the
  note text and the criterion text the worker was given. A pair is fresh
  while both hashes match the current files.
- **Review is opt-in.** It is not part of the default writing flow, and no
  check runs it automatically. You run it when you want notes judged, and
  each run costs paid launches.

For how it is built, see [review architecture](./review-architecture.md);
[ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md) records
the decision. Exact arguments are in `commonplace-review --help` and
[commands](./commands.md).

## Concepts

**Criterion.** The markdown file a note is judged against. It may be a
catalog gate, a compression check, the note's type spec, its collection's
`COLLECTION.md`, or a report instruction: critique, friction, premises,
compression synthesis or the role report. The rewrite's review instruction is
also a criterion, which only the rewrite workflow runs. A criterion is named by its artifact identity: a
repository path, or `commonplace:<path>` for a library file outside the
repository, as the gates are in an installed project.

**Pair.** One note and one criterion: the unit of review, result and
freshness.

**Gate.** A catalog criterion with a closed question whose outcome is `pass`,
`warn` or `fail`. Gates live in the library's
`instructions/review-gates/<lens>/<name>.md` (`kb/instructions/review-gates/`
in this checkout). The gate id is `<lens>/<name>`, for example
`prose/source-residue`. A gate's `requires_type` and `requires_trait` filter
the notes it applies to; a skipped gate is not a passed gate.

**Bundle.** The gates of one lens directory: `prose` means every gate under
`review-gates/prose/`.

**Type-conformance pair.** The note judged against the type spec its `type:`
names ([ADR 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)).
Request it with the `type` lens, or `type/<name>` for one type's notes. A
fixed wrapper tells the worker how to apply a type spec as a gate; a
`## Review` section in the spec is the operative test. Structural checks stay
with the validator.

**Collection-conformance pair.** The note judged against its collection's
`COLLECTION.md` ([ADR 041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)).
Request it with the `collection` lens, or `collection/<path>` with the
collection directory relative to `kb/` (`collection/theory`). The wrapper
asks only for what the contract adds beyond the type spec, so the two
conformance pairs do not flag the same thing twice.

Both wrappers also leave four properties to the frontmatter gates that own
them: whether a claim title is a proposition, whether it is contestable,
whether it composes as a linkable phrase, and whether the description
discriminates the note. A conformance pair judges a title or description
only against a convention its own document adds
([ADR 131](./adr/131-conformance-reviews-leave-titles-and-descriptions-to-their-gates.md)).

**Critique.** The `critique` lens applies the critique instruction as a
report criterion: the worker writes an open-ended report, and the outcome is
`report`. Critique is opt-in; `--all-gates` and the default status set leave
it out.

**Compression check.** One of the four checks in the library's
`instructions/compression-bundle/`: `compression/core-claim-obscured`,
`compression/branch-bloat`, `compression/detail-overhang` and
`compression/marginal-value-redundancy`. Each is a verdict criterion,
requested by its own id; a bare `compression` request is refused. A check
reports PASS, INFO or WARN: INFO is a `pass` outcome with `info` findings, and
no check uses `fail`. Each check is one launch even under `--grouping bundle`.
The checks are opt-in like critique. The
[compression bundle](../instructions/run-compression-bundle-on-note.md) still
runs all four in one report of its own; that report is not a result file.

**Friction and premises.** The `friction` and `premises` selectors apply the
[composition-friction](../instructions/composition-friction-gate.md) and
[premise-decomposition](../instructions/premise-decomposition-gate.md)
instructions as report criteria. Neither gives an overall verdict. A friction
finding is one ranked inferential joint whose reason begins `UNSUPPORTED`,
`THIN` or `HOLDS`; the body adds the `SURVIVES` or `DISSOLVES` filter line. A
premise finding is one premise whose reason begins `HOLDS`, `DOUBTFUL` or
`DEFEATED` and routes a failure `LOCAL` or `GLOBAL`. Both use ordinary
freshness: the whole note, since they declare no `watches:`, the instruction
and the output contract. Files they consult that the note does not link,
such as the modality section premises reads in `kb/theory/COLLECTION.md`, are
reading context, not freshness inputs. Both are opt-in.

**Compression synthesis.** The `compression-synthesis` selector applies the
[synthesis instruction](../instructions/compression-bundle/high-impact-simplification-synthesis.md)
to one note and the compression findings supplied as `--input ROLE=PATH`
files, usually the four check results. It runs alone, on one note, and never
runs a check. No freshness hash covers the supplied findings, so its freshness
is unassessed: it writes no current result, is never skipped as fresh, and
`status` refuses it. Its result stays in the run's observation; read it with
`show RUN`.

**Role report.** The `role` selector applies the
[role-in-the-KB instruction](../instructions/role-in-the-kb-gate.md) to one
note and its inbound contexts, supplied under the input role `inbound`. The
inbound contexts are every Markdown file under `kb/` that links to the note,
outside `kb/reports/`, `kb/work/` and hidden directories, with its path,
title, description and each passage that holds the link. Code collects them
(`review_workflows.inbound`) and caps the files and passage length it shows.
The report opens with `## Role`, the note's role as its dependents use it;
then it reports what each dependent needs, duplication, recommendations in
linking sources the note has not taken up, and which dependents a change
would reach. `run gates NOTE --criteria role` collects the inbound contexts
itself; `--input inbound=PATH` supplies them instead. Like the synthesis, it
runs alone, its freshness is unassessed because other notes' text is an
input, it writes no current result, and `status` refuses it. In a full run,
each edit operation also receives the `## Role` section alone, as the input
`kb-role`, and may not rename, redefine or drop a term or claim that section
lists as relied on.

**Rewrite review.** The
[review of a rewrite candidate](../instructions/rewrite-a-note/review-a-rewrite-candidate.md)
is a verdict criterion that no request selects. Only `run rewrite` runs it,
alone, on its candidate text with the rewrite's inputs supplied; see
[rewriting a note](#rewriting-a-note). Its result becomes the note's current
result only when the note is published with exactly the judged candidate.
Then `status` and `--triage` treat it like a gate's result.

The role report feeds the note's [write brief](../types/write-brief.md)
only through the operator. No code writes a brief. When a role report lists
relied-on terms or claims that the note's brief does not keep, the session
agent tells the operator and offers to add them to the brief's Must keep, or
to create the brief when the note has none. The agent never amends a brief
without the operator's word.

**Connect.** [Connect](../instructions/cp-skill-connect/SKILL.md) keeps its
own route. It writes a connect report, not a review result, and its
candidates depend on the whole corpus, which no note or criterion hash
covers.

**Outcome.** Reviews use [review-result](../types/review-result.md).
Workers supply `type`, `findings`, `outcome` and the body; critique also
supplies `attack-outcome`, and no other report does. Verdict findings have
`info`, `warn` or `fail` levels. Each report method has its own required
sections, which the schema checks by the result's criterion. Passage quotations must match one span of the captured target, and only one;
matching ignores line wraps and quote-mark style, so a quotation identifies a
passage without being a byte-exact copy. Document findings use no quotations. Code supplies provenance and validates
the completed artifact against the captured library type/schema and project
collection contract. Invalid worker output receives specific retry diagnostics;
missing controller inputs or corrupt evidence stop the sweep instead.
Terminal result footers are unsupported.

**Watches.** A gate may declare `watches:` with any of `title`,
`description` and `body`. The note side of its freshness then hashes only
those parts, so an edit elsewhere, such as to `tags:`, leaves its pairs
fresh. A criterion without a valid declaration watches the whole note; type
specs and collection contracts declare none. The declaration therefore
decides which edits stale a gate's pairs.

**Criterion-derived local paths.** A worker reads the note, the criterion
and files the note links to. One exception is open to any criterion: it may
tell the worker to derive exactly one local path from a link in the note and
read it. `semantic/grounding-alignment` uses it for an ingest link marked
`(snapshot required)`, which sends the worker to the matching
`kb/sources/.snapshots/<slug>.md`
([ADR 073](./adr/073-untracked-source-snapshots-require-ingest-grounding.md)).
It permits one named path from a link already in the note, not a search of
the corpus.

| Do not conflate | Distinction |
|---|---|
| fresh and approved | Fresh means the result was produced from the current texts. It does not approve the note or resolve a report's findings. |
| `report` and a verdict | `report` says the report contract completed; it is not a fifth outcome. |
| pass and absence of problems | A pass says one gate found nothing to flag. |

## Order of concerns

Review operations and edit operations declare an optional `depth`, an
integer from 1. A lower depth is a higher-order concern: a procedure that
orders operations handles depth 1 before depth 2. One scale covers both
kinds, so a finding and the edit that answers it sit at the same depth.

| Depth | Concern | Review operations | Edit operations |
|---:|---|---|---|
| 1 | whether the note's claim and scope should stand | critique, composition friction, premise decomposition, the role report | split out a treatment |
| 2 | what the note asserts and on what grounds | the semantic bundle, `frontmatter/claim-strength`, `prose/source-residue`, the type and collection reviews | narrow overclaims |
| 3 | terms and what a reader needs to know | the accessibility bundle, `prose/unbridged-cross-domain` | abstractions |
| 4 | structure and proportion | the complexity bundle, the compression checks and their synthesis, three prose gates, `structural/general-before-specific` | readability and flow |
| 5 | wording | the sentence bundle, two prose gates, two structural gates | plain wording |
| 6 | title, description and opening | the other frontmatter gates | opening and title |

The values are best-effort declarations. Each file holds its own value;
the table summarizes them and the file governs. No code orders review
operations by depth yet: the revise workflow checks the depth order of
its passes, places a plan entry that fixes a finding at the depth of the
finding's criterion, and shows the assessor each finding's depth. Its full
procedure selects the review operations that declare a depth and runs them
together, not in depth order. Nothing else reads the field. The type and collection
conformance reviews declare no depth, because their criterion is a type
spec or a collection contract. Expect the first runs of an ordered
procedure to show wrong values, and correct them in the files.

## Result files and freshness

Each accepted review writes
`kb/reports/state/review/results/<note-path>/<criterion-id>.md`. The
criterion id is the gate id for a catalog gate, the repository path without
`.md` for another repository criterion (`kb/types/note`), and `commonplace/`
plus the library path for another library criterion. The typed frontmatter
holds structured findings, normalized freshness hashes and exact evidence
references. The run owns the target capture, raw launch output and completed
typed result; the current result is a replaceable view. Raw worker bytes and
completed-result bytes have distinct hashes. Explicit draft reviews and
reviews with supplied operational inputs retain evidence without replacing
catalog results.

A pair is in one of three states:

- `fresh`: note, criterion and output-contract hashes match;
- `missing`: no result exists;
- `stale`: a freshness input changed; status names which.

**Finding decisions.** When the operator rejected a finding of a pair at a
triage, the next review of that pair receives the rejections: each finding,
the operator's reason and the date, as the supplied input
`finding-decisions`. The input's text states the reviewer's rule: do not
raise the same finding again unless the note's text changed in a way that
answers the operator's reason, or the reviewer has an argument the reason
does not address; a finding raised again states that argument or change.
The criterion hash of such a pair covers the criterion text and these
decisions, so a new rejection stales that pair and no other; status names
the criterion as changed. A pair without a rejection keeps its plain
criterion hash and its request. Under `--grouping bundle`, a pair with
rejections is asked alone, outside its bundle call. Approved and deferred
findings are not given to the reviewer.

A result whose note or criterion file no longer exists is **orphaned**. A
moved note orphans its results too. Removing an orphan is deleting its file;
the moved note's pairs are reviewed again.

Result files are ignored by Git and stay on the machine that ran the review.
One result exists per pair, whichever profile produced it; a later review
replaces it.

## Reading status

`status` launches nothing.

```bash
commonplace-review status kb/theory/example.md              # every applicable gate pair, with missing ones
commonplace-review status kb/theory/ --criteria type collection
commonplace-review status --fresh --outcome warn            # current warnings, from every stored result
commonplace-review status --stale kb/theory/                # what a sweep would ask
commonplace-review status --json --fresh --outcome warn     # rows with each result file's path
```

With notes, status covers every applicable pair for the requested criteria
(all gates when `--criteria` is omitted), including pairs never reviewed.
It reads only results for those pairs and does not scan for orphans; the JSON
`orphaned` list is empty. Without notes, it covers every stored result whose
note and criterion still exist and lists orphaned results separately.
Each row shows the note, criterion id, state, outcome and model. A directory
means its direct frontmatter-bearing notes, not nested ones, and leaves out indexes, collection
contracts and type specs. Name the notes of a validation-ignored directory one
by one.

The current warnings are the fixing queue: read each finding in the result
file `--json` names, and fix one with the focused procedure,
`commonplace-review run revise NOTE --finding RESULT`, or have the operator
decide each finding of a note first with
`commonplace-review run revise NOTE --triage` (see
[improvement procedures](#improvement-procedures)).
`commonplace-status --review` adds counts of fresh, stale and orphaned
results and of current `warn` and `fail` outcomes to the project status.

## Running a gate sweep

```bash
commonplace-review run gates kb/theory/example.md --criteria prose semantic/grounding-alignment
commonplace-review run gates kb/theory/ --all-gates --grouping bundle --profile sonnet
```

`--criteria` takes gate ids, bundle names, compression check ids and the
lenses; `--all-gates` means every bundle plus `type` and `collection`. The sweep skips pairs with a fresh
result unless `--force` is given, and asks a worker for each other pair:

- `--grouping pair` (the default) makes one call per pair;
- `--grouping bundle` makes one call per note and bundle for that bundle's
  stale gates. Each gate is judged on its own and gets its own result. A
  bundle with one stale gate, and every type, collection, compression and
  report pair, is still one call per pair.

A call has three attempts; a rejected review and a launch that returned no
answer each spend one. A worker that cannot judge writes a problem instead
of guessing, and no result is written for its pairs. `--max-workers`
(default 4) bounds the launches running at once.

Each sweep opens a run directory under `kb/reports/state/review/runs/v2/<UTC
stamp>/` and prints a JSON report: per pair its state (`fresh`, `reviewed`,
`problem`, `out-of-attempts` or `not-run`), the counts, what stopped the
sweep and the guard's finding. It exits 0 only when every pair has a current
result, 1 otherwise, and 2 when the command failed.

### Drafts, evidence and fixtures

Use `run gates NOTE --criterion-file PATH` for a repository-local, possibly
untracked review-gate file. It must declare `reading-scope: linked-files`
and conform to its type. Repeating the same wording creates a new observation
without changing its `gate_id` or inserting it into the catalog.

`--input ROLE=PATH` supplies a self-contained operational text copy. Workers
must not browse its source run or recursively fetch provenance dependencies.
Resume uses the captured inputs, not later edits at their original paths.

`show RUN --observation ID --json` exposes findings, capture references,
launch associations and rejection diagnostics. Omit the observation selector
to inspect every observation in that run. Retries and replay stay within one
observation; a bundle launch does not provide independent trials.

`fixture create --from RUN --observation ID --substitute-current-executor`
retains a single-assessment baseline without calling a model. The flag
explicitly substitutes the current executable; missing historical dirty
content requires `--repair ORIGINAL=PATH` with matching bytes. In a Git library,
tracked and non-ignored untracked files enter the inventory; ignored files enter
only as explicitly selected inputs. A library installed without Git uses its
visible package files. Hidden paths and report state remain excluded from the
library inventory. Observations and fixtures record this inventory policy;
older policies are refused, not silently reinterpreted. Start a new observation
to create a baseline under the current policy.

Fixture trials currently use the Claude Code adapter, pair grouping and one worker.
`run gates --fixture PATH` opens a fresh isolated trial with no live result
publication or freshness skip; add `--resume TRIAL_RUN` only to continue that
trial. Target/profile/configuration overrides are rejected. Effective tool
availability and user configuration remain unverified until inspected; these
runs do not automatically establish environment equivalence or calibration.

### Stops, retry and resume

- **Launch failure or usage limit.** The sweep stops asking new calls; results
  already written stay. Repair the environment or wait for the reset, then
  rerun with `--resume RUN_DIR` and the same notes and criteria. Answered
  calls replay without a launch.
- **Controller failure.** Missing validation dependencies or corrupt evidence do
  not request model correction. Repair the controller or its inputs before
  trying again; incomplete captures are not silently backfilled on resume.
- **No progress.** Correction stops before repeating an already rejected
  prompt/input combination. Inspect the diagnostics rather than spending more
  calls on identical feedback. An explicit answer dismissal remains available
  when another attempt is warranted.
- **Worker problem.** Read it in the report. When the cause is fixed,
  `commonplace-review retry RUN JOB` dismisses it and a resumed run asks
  again. A pair's job is `<note>::<criterion-id>`; a bundle call's is
  `<note>::<bundle>/*`.
- **A wrong answer.** `retry RUN JOB --key KEY` dismisses one answer. Its
  result file still makes the pair fresh, so rerun with `--resume` and
  `--force`: the dismissed call is asked again and the others replay.
- **An interrupted controller.** If a run was killed while a launch was
  running, check that the worker process and its children are gone, then
  `commonplace-review acknowledge RUN LAUNCH`. The command inspects and kills
  nothing.

One process at a time may hold a run; a second exits 2.

## The checkout guard

A run records `git status` (with untracked files), the content digest of
every listed path and `HEAD`, before and after, ignoring
`kb/reports/state/review/`. The report lists every path that differs. A
revise run leaves out its note only when the note holds the text the run
wrote in that invocation.

What it can claim: these paths changed while the run was open. What it
cannot claim: that a worker changed them. Other sessions editing or
committing in the same checkout show up as well, so a guard that is not
clean means "inspect these paths". It does not make a run fail: `ok` and the
exit status of a sweep, an edit, a revise run and a rewrite run do not
depend on it. Fixture trials are the exception, because a changed trial tree
invalidates the evidence. Nothing is reverted. The guard also misses a change to
an ignored file and a change undone before the run ended.

## Worker profiles

Profiles live in the library's `instructions/review-profiles.yaml`, with the
entry shape of task profiles: harness, launch model, effort and harness
flags. `--profile NAME` picks one; the file's `default` applies otherwise. A
resumed sweep keeps the profile it opened with.

- `opus` (the default) and `sonnet` run Claude Code with read tools, edit
  rights only under `kb/reports/state/review/runs/`, and Bash denied. That
  this denial refuses a write has not been observed; the guard is the
  verified control.
- `codex` runs in a `workspace-write` sandbox, which cannot keep the
  checkout read-only. The prompt forbids writing and the guard reports it.

## Cost

A launch's fixed context dominates its cost. Single observations with the
`sonnet` profile:

| Run | Result |
|---|---|
| one gate on one note, one launch | $0.095, 13 s, nearly all fixed context |
| the ten `prose` gates on one short note, one bundle launch | nine pairs reviewed, $0.172, 31 s |

Bundle grouping shares the fixed context. Whether it changes verdict quality
has not been compared, which is why `pair` stays the default.

## Planning-free baseline

Evaluate one operation before composing it with planning or other operations:

- **One review:** `commonplace-review run gates NOTE --criteria GATE-ID --grouping pair`.
  Supply one gate id, not a bundle. The result is report-only; even a failure
  does not select more work or edit the note. Fresh pairs are skipped. One
  compression check runs the same way, for example with
  `--criteria compression/detail-overhang`.
- **One editing pass:** `commonplace-review run revise ARTIFACT --plan FILE`.
  The supplied YAML plan fixes purpose, protected claims, pass and scope. No
  assessment request is constructed. Editors receive execution instructions,
  not the planning procedure. See the [fixed-plan example](../instructions/simplification-passes/README.md#fixed-plan-execution-the-simple-baseline).

These operations still use judgment inside their fixed tasks. Planning means
choosing work, not merely using a model. The quick and full procedures
choose work, and their choices need separate evaluation; reliable replay does
not establish reliable selection or editing judgment.

## Workflows beyond the sweep

Beyond the sweep, `commonplace-review` runs one edit operation alone, runs
the improvement procedures, rewrites a note from its sources, and lists the
operator's decisions.

### One edit operation

`commonplace-review run edit OPERATION NOTE` runs one
[edit operation](../types/edit-operation.md) on one note and writes nothing
to the checkout ([ADR 133](./adr/133-edit-operations-run-alone-through-one-typed-route.md)).
The worker returns an [edit result](../types/edit-result.md) and, for
`changed`, a candidate text. Code completes the result with provenance and
accepts it only within the bounds: title, H1, type, brief declaration and
link targets kept, quoted spans unchanged, no new validation failure, and
proposal quotes that occur once in the input. A rejected answer goes back to
the worker; a worker problem becomes a `problem` result. The result and the
candidate stay in the run's observation under `artifact/edits/`, beside the
exact inputs, so `fixture create` and `run edit --fixture` rerun one
execution. An edit result has no freshness state and no current-result file.
`--text PATH` edits a saved text instead of the note's file; `--input
ROLE=PATH` supplies the files an operation names, such as `findings`.

A `per-item` operation (plain-wording, abstractions) runs twice. The first
run returns `proposed`; that result is the question of a stop.
`commonplace-review answers create --from RESULT` writes the pending
[answers](../types/answers.md) file, and the operator decides each item in a
session that follows [decide items](../instructions/decide-items.md). The
second run takes the answers as `--input answers=PATH`, applies the
`approved` items and returns `changed`. Code accepts the answers only when
the validator accepts them and their question is a result of the same
operation on the same text. It refuses a candidate that changed the passage
of an item that is not approved; it does not detect a change outside the
items ([ADR 134](./adr/134-stops-record-the-operators-answers-in-one-typed-file.md)).
This route does not collect earlier decisions. An operator can supply a file
of them with `--input earlier-decisions=PATH`; it is not carried over into
the answers file.

### Improvement procedures

`commonplace-review run revise ARTIFACT` is the one runner for improving a
note or another markdown artifact. It executes a plan: a list of
[edit operations](../types/edit-operation.md) from the
[simplification passes](../instructions/simplification-passes/README.md) in
increasing depth, each through the same route as `run edit`. It publishes
its candidate to the artifact without a stop (see [publication](#publication))
and ends at its first stop, leaving a [continuation record](#revise-runs-and-the-continuation-record)
([ADR 138](./adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)).
Four procedures differ only in
how the plan is made
([ways to make a plan](../instructions/simplification-passes/README.md#ways-to-make-a-plan),
[ADR 135](./adr/135-improvement-procedures-are-three-plans-on-one-runner.md)).
A new run requires one choice.

| Procedure | Flags | What chooses the edits | New review launches |
|---|---|---|---|
| focused | `--pass NAME`, `--finding RESULT`, `--plan FILE`, `--answers FILE` | the operator | none |
| triage | `--triage` | the operator, by deciding each finding of the fresh stored `warn` and `fail` results | none |
| quick | `--assess` | one assessor, from the artifact and its fresh stored `warn` and `fail` results | none |
| full | `--full` | one assessor, from the artifact, the new findings, the depth 1 reports and the role report | every review operation that declares a `depth`, and the type and collection reviews |

**Focused.** `--pass NAME` writes a one-entry plan for one edit operation on
the whole artifact. `--finding RESULT` writes a one-entry plan that runs
[fix a finding by a named strategy](../instructions/fix-warnings/fix-strategy-taxonomy.md)
with that review result of the artifact as its `finding` input; the
operation changes only the passage the finding names. `--plan FILE` supplies
any other plan. `--answers FILE` makes the plan from the operator's decided
answers files (see [the continuation record](#revise-runs-and-the-continuation-record)).

**Triage.** `--triage` presents the artifact's findings to the operator. It
takes the same results the quick procedure gives its assessor, the fresh
stored results with outcome `warn` or `fail`, and keeps those with a finding
of level `warn` or `fail`, and records them in `triage-inputs.json`. It
copies each result into the run's `artifact/findings/` and writes one
pending [answers](../types/answers.md) file per result,
`artifact/finding-answers-<key>.md`, whose question is the copy and whose
items are the result's `warn` and `fail` findings. Then it ends. The
report's `triage` lists each file, and the continuation record has one
`findings` item naming every file and the command that consumes them. In a
session, follow [decide items](../instructions/decide-items.md): the
operator approves a finding that is right, rejects one that is wrong with a
reason, and says whether it is wrong for this note only or the criterion is
too broad, or defers it. On the operator's word,
`run revise NOTE --answers FILE --answers FILE ...` names the decided files
and starts a new run. Its plan holds one entry for the fix per result with
at least one `approved` finding, in depth order, naming the copy as its
`finding`. The fix also receives the answers as `finding-answers` and fixes
only the approved findings; its report lists the findings it did not touch.
The run keeps a copy of every named file, including one that approves
nothing. It is refused when a result no longer matches the parts of the
note its criterion watches, or when no named file approves a finding; then
keep each file with `answers record FILE`. With no fresh `warn` or `fail` result the triage ends
at once, and `triage.what` says so. Nothing is reviewed and nothing is
assessed. A rejection feeds later work: the next review of the pair
receives it (see [finding decisions](#result-files-and-freshness)), and the
assessor plans no fix for it. Because a new rejection stales its result,
the quick procedure no longer receives that result until the pair is
reviewed again.

**Recording decisions on an overtaken run.** The operator may answer a
run's findings in a session instead of at a triage, for example by splitting
the note. The note's text then changes, and no command applies the run's
findings.
`commonplace-review record RUN` writes the triage's pending answers file over
each review result the run's assessor or triage received that has a `warn`
or `fail` finding, and prints each file with the command that records it. It
launches nothing, makes no plan and publishes nothing; a file that exists is
left as it is. Record each finding the operator discussed with its state and
reason, what was done in `resolution` and the new notes or commit in `refs`;
leave the rest `pending`
([decide items](../instructions/decide-items.md#findings-answered-by-a-structural-change)).
After `answers record FILE`, `decisions` lists the decided items, and the
undecided ones as `overtaken`. Later runs on the same note path receive the decisions as
they receive a triage's: a rejection reaches the next review of that
criterion as `finding-decisions`, with its `resolution`. A rejection whose
`resolution` states a retained question closes the rejected diagnosis, not
the question; the reviewer may still report on that question. Notes made by
the split receive nothing; review each of them afresh.

**Quick.** `--assess`: one assessor chooses the edit operations from the
artifact and its fresh stored `warn` and `fail` review results. No review is
launched, so an artifact that was never reviewed is assessed from its text
alone. A finding the operator rejected at a triage of that same result,
whose answers name the result's current hash, is removed from what the
assessor receives; a result left with no `warn` or `fail` finding is not
given. The assessor also receives the operator's rejected and deferred
findings of the note as `earlier-decisions`. By the planning instruction it
plans no fix for a rejected finding unless the text changed in a way that
answers the operator's reason, and no fix for a deferred one unless its
`revisit` condition is met. The full procedure's assessor receives the same.

**The write brief and `must-keep`.** The note's
[write brief](../types/write-brief.md) is the one lasting statement of what
the note must keep and exclude. The assessor and every edit operation receive
it as `brief`. A plan's `must-keep` list, and the `--must-keep` option that
feeds it, holds only what one run keeps beyond the brief's Must keep; the
planning instruction tells the assessor not to restate the brief there. The
assessor plans no pass that conflicts with the brief. When the purpose or the
operator's must-keep items conflict with it, the plan's `stop` names the brief
item. A plan with a field other than `purpose`, `must-keep`, `passes` and
`stop` is refused.

**Full.** `--full` first runs every review operation that declares a `depth`
on the artifact, and the type and collection reviews, through the sweep's
route. A type spec and a collection contract declare no depth; the
procedure treats their reviews as depth 2. Fresh results are reused, new
results go to the shared store. Then the compression synthesis runs on the
checks' results, and the role report on the artifact's inbound contexts,
each alone and without publishing a result. The assessor then also reads the
depth 1 reports, the compression synthesis report and the role report. When
one proposes changing what the artifact is, the plan's `stop` names the
proposal and its report, and nothing is edited. Before it stops on or plans
around a depth 1 proposal, the assessor checks against the role report
whether the proposal's cause may be a term or claim that dependents rely on;
when a change would reach dependents, the `stop` names them. A stopped plan leaves
`artifact/stop-answers.md`, where the operator's decision on the proposal is
recorded once. A stop is advice: the run has ended and nothing consumes that
file, so keep it with `answers record FILE`. What follows the decision is a
separate task: the route the stop names, or a replacement plan run with
`--plan`. The kept decision reaches the assessor of the next
run on the note, so the reason should state which of the stop's proposals it
covers. The full procedure does not review the candidate; the next sweep
finds the stale results after publication. A review without a result ends
the run before assessment; a new run reuses the results the review step
published, which are fresh.

A plan entry for an operation that declares `responds-to` names its
`finding` and takes the depth of that finding's criterion. Within the chosen
procedure, ordinary intermediate work is preauthorized. The assessment report
and generated plan stay in the run for inspection; the validated plan runs
without routine approval. `--plan FILE` also supplies a validated override
of a stopped plan. Editing the retained plan alone is not an override. Each
listed operation runs in order on the preceding text; its `effort` selects
the profile. Every operation must end `applied`, `no-change` or `skipped`
before the final text is published. Control-flow
checks do not establish the quality of the selected edits.

No procedure checks that an edit fixed its finding, and none records a
judgment over the whole note other than a plan's `stop` and its answers. A finding fixed by
the focused procedure leaves an edit result and a recorded publication; a
finding the operator rejects as spurious leaves a record only through a
triage, whose answers file holds the rejection and its reason.

Plain-wording and abstractions, the `per-item` passes, still stop for the
operator's answers on each proposal, in `artifact/<pass>-answers.md`.
These are temporary procedure-development points:
retain proposed, accepted and rejected choices with reasons, evolve the
selection rules and checks, and evaluate retained and fresh examples before
separately authorizing removal. This is not new automatic learning
infrastructure, and fewer proposals do not establish reliability.

**Earlier decisions.** Decisions carry over between revise and rewrite runs
on the same note. When a revise or rewrite run starts, code collects the
operator's decided items from the answers kept in the other revise and
rewrite runs on the same note path (`answers/` in each run). It takes
items whose state is not `pending` and whose proposal is an edit proposal,
with a `quote` and a `change`, or a finding of a triage, which it records
with its criterion. It skips publication and plan-stop answers, and answers the
validator refuses. When the same proposal, or the same finding of the same
criterion, was decided more than once, the latest `decided-at` wins. The run keeps what it collected in
`earlier-decisions.json`, as a record of what it read. Each per-item pass and each fix of a finding
receives them as the input `earlier-decisions`, when there is at least
one. A new proposal with the same `quote` and `change` as an earlier
decided item, or a triage finding with the same criterion and the same
`scope`, `quotes`, `reason` and `level`, starts decided in the answers file: code copies the earlier
`state`, `reason`, `revisit`, `decided-by` and `decided-at` and sets
`carried-from` to the earlier answers file. Only identical proposals are
carried over. The run still ends at the stop, even when every item is
carried over, and the operator may change a carried item; changing it
removes `carried-from`. `commonplace-review decisions` shows `carried-from`
on each carried item.

#### Revise runs and the continuation record

Every invocation opens a new run, in
`kb/reports/state/review/runs/v2/revise/<note path without .md>/<UTC
stamp>/`, with `-2`, `-3` on a collision. A note's runs are listed under the
note's directory; runs made before this layout are named by a 12-hex hash of
their start text, so the time of a run is in its records, not its name. The
run records the note, the hash of its start text and the hash of the write
brief it captured in `start.json`. No run is repeated or resumed, and every
invocation needs a procedure choice: a bare `run revise NOTE` is a command
error. Within one invocation, Workjig's call records serve retries.

A run ends in one of three ways, which its report states as `outcome`:

| `outcome` | Meaning |
|---|---|
| `completed` | Nothing is left. The run may have published |
| `needs-continuation` | The run did what it could and left a continuation record. It may have published; a run that finished its whole plan still has this outcome when the assessment left claim questions or the publication left reviews stale |
| `failed` | A worker, a review or the write to the note failed. Entries before the failure may have been published |

The report's `ok` is false, and the exit status 1, only for `failed`.
`plan-stop` is the text of the plan's `stop`; `stopped` is a failure's
message. [The checkout guard](#the-checkout-guard) is reported apart, as
`guard`.

It ends at its first stop: a plan `stop`, a triage, the first
per-item entry that proposes anything, a held candidate, or a failed entry.
What it could not finish is its continuation record, `continuation.json` in
the run directory and `continuation` in the report:

| Field | Content |
|---|---|
| `run-dir` | The run directory |
| `made-for` | The note's text when the run ended: `note`, `sha256` and `text`, the path of its last publication or of `artifact/start.md`. Every item was computed on it; it is never updated |
| `items` | One per piece of unfinished work, in dependency order |

Each item has an `id`; a `kind`; `what`, in words; `actor`, the actor
expected to be able to resolve it (`operator`, `session-agent`, or `worker`
with its `effort`), an estimate and not a permission; `after`, the ids of the
items to settle first; `how`, with `command` where a command proceeds, `record` where the
recording command applies and `revised` for a held candidate; `answers`, the
answers files it waits for; and `evidence`, the files it rests on.

A plan entry not run is continued by `run revise NOTE --plan FILE`, where
FILE is a one-entry plan the run wrote under `artifact/continue/<id>.yaml`
with the entry's pass, scope and finding and the plan's purpose and
must-keep list; an entry that applies the operator's answers is continued
by `--answers FILE` instead. A fix entry names the run's copy of its review
result, `artifact/findings/<criterion id>.md`, so a later sweep that
replaces the stored result does not change what the fix reads.

| `kind` | Left when |
|---|---|
| `failure` | a worker, review or publication failed, or the note changed during the run |
| `findings` | a triage wrote answers files over review results |
| `plan-stop` | the plan set `stop`; `artifact/stop-answers.md` waits |
| `held-candidate` | a candidate added a validation warning and was held |
| `proposals` | a per-item entry's proposals wait in `artifact/<pass>-answers.md` |
| `direct-entry` | a plan entry for an operation that applies directly was not run |
| `per-item-entry` | a plan entry for a per-item operation was not run |
| `fix-entry` | a plan entry that fixes a finding was not run |
| `interactive-entry` | `narrow-overclaims` without evidence, or `split-out-a-treatment`, was skipped |
| `claim-questions` | the assessment lists claim questions for the operator |
| `stale-reviews` | the run published and some stored review results of the note are stale; `what` counts them; nothing schedules them |

When the report carries a continuation record, a session agent continues
with the operator by [continue a revise pass](../instructions/continue-a-revise-pass.md).
A later command acts on a stop's output by naming the file or the run, and
naming it is the operator's approval
([ADR 138](./adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)).
The agent runs such a command only on the operator's stated word for that
exact file or run:

| Stop's output | Command |
|---|---|
| decided proposals of a per-item entry | `run revise NOTE --answers FILE` |
| decided answers over review results, from a triage or `record` | `run revise NOTE --answers FILE --answers FILE ...` |
| a held candidate | `publish RUN`, or `publish RUN --revised FILE` |
| answers nothing consumes: no item approved, a plan stop's answers, decisions on an overtaken run | `answers record FILE` |

`run revise NOTE --answers FILE` over a per-item entry's proposals starts a
new run of that one entry, which applies the `approved` items and publishes.
The entry keeps the scope the asking run's plan gave it. The run keeps a copy of the named file under `answers/`. It is refused when
the validator refuses the answers, when the note is not the text the
proposals were made for, when the write brief changed since the asking run,
or when no item is approved; nothing is applied then. A note changed by
anyone else leaves a run's pending files `overtaken`
([decision record](#the-operator-decision-record)).

#### Publication

A revise run writes its candidate to the note without a stop. Changes
applied without a decision, and items the operator already decided, need no
approval of the whole text. The run publishes at two points, so it may
publish twice:

- before a per-item entry is asked for proposals, what the earlier entries
  applied, so the proposals are made on the note's text;
- when the run ends, what its entries applied since the last publication,
  including the entries before a failed one.

It publishes only a text that differs from the note. It writes the note only
while the note holds the text the run last knew, its start text or the text
it last published, and only while the captured brief is unchanged.
Otherwise the run ends with a conflict and nothing is written. The check
and the write happen under the note's publication lock,
`kb/reports/state/review/publication-locks/<note path without .md>/`,
which every revise and rewrite run and `publish` share, so two runs on one
note cannot both publish over the same text. A plan `stop`,
the depth 1 stop of the full procedure and a triage publish nothing.

Each publication is recorded in the run's `published.json`: the published
text `artifact/publications/<n>.md`, its hash, its diff
`artifact/publications/<n>.diff` from the text before it, the plan entries it
covers, the time and who decided it. The report lists them under
`publications` and says `published: true` when the run wrote the note; a run
that left nothing has `complete: true` and no `continuation`.
`commonplace-review decisions` lists each automatic publication with class
`publication`, decided by `automatic`, never by the operator. Nothing is
committed: the change is in the working tree, `git diff` shows it, and git
reverses it. The session agent tells the operator what was published, with
the note's path and the diff's path
([approve a text](../instructions/approve-a-text.md)).

A candidate that adds a validation warning the note's text does not have is
not published. The run holds it and ends, before it asks a per-item entry
for proposals: it keeps `artifact/final.md`, its diff `artifact/final.diff`
from the text it is held over, and `held.json` with the hashes of the text
held over, the candidate and the diff, the new warnings and the plan entries
it covers. The report's `held` names the files, the warnings and the
commands that publish it; `new-warnings` lists the warnings, which do not
block publication. Follow [approve a text](../instructions/approve-a-text.md).

`commonplace-review publish RUN` publishes that exact candidate and launches
nothing. Naming the run is the operator's approval. It is refused, and
writes nothing, when the note no longer holds the text the candidate was
held over, when `final.md` or `final.diff` changed after the run, when the
write brief changed since the run, or when the operator already published
the candidate. `publish RUN --revised FILE` publishes the operator's full
revised text instead, from a file outside the run's `artifact/`, after the
same checks and the candidate checks of `edits.artifact_bounds()`: the
frontmatter parses and keeps `title`, `type` and `brief`, the H1 is kept,
`user-verified` is gone when the body changed, and the validator finds no
new failure. The per-pass bounds of edit operations do not apply. The run
keeps the revised text as `artifact/revised.md`, with
`artifact/revised-from-final.diff` from the candidate and
`artifact/revised.diff` from the note, and keeps `final.md` unchanged.
`decisions` lists the publication as decided by the operator, marked
`revised` for a revised text. The candidate is a workflow output, not an
input: do not edit it. To change it otherwise, start a new run, for revise
with `--plan`. Instructions remain the judgment authority; prompts name
inputs only.

### Rewriting a note

`commonplace-review run rewrite NOTE --commission FILE` rewrites one note
from its authorized sources. Use it instead of `run revise` when the note's
contribution is known but its claims or synthesis are unsettled: a review
found a problem with a claim, the claim overreaches its evidence, or the
note must be rebuilt from new sources. `run revise` edits a text whose claims
stand; its passes may not narrow or change claims generally. The rewrite may
change claims, and it may not change the title: a retitle is a separate
`commonplace-relocate-note` step on the operator's word. It ports the edit
path of [multistage writing](../instructions/cp-skill-write-multistage/SKILL.md),
which tells the session agent how to prepare and run it.

**Commission.** The session agent writes the commission with the operator
before the run. It is a Markdown file with YAML frontmatter:

```markdown
---
note: kb/theory/the-note.md
sources:
  - path: kb/sources/some-source.ingest.md
    role: the ingest that states the mechanism
  - path: kb/sources/.snapshots/some-source/page.md
    role: the full text, for exact wording
---

# Commission: <short note name>

## Intended contribution
## Must keep
## Must exclude
## Reserved decisions
## Current direction
```

The note's write brief is the one lasting statement of what the note must
do, keep and exclude; the commission adds only what is specific to this
rewrite. `## Current direction` is always required. The four sections that
repeat the brief's headings are required only when the note has no brief.
When it has one, they are optional and hold only what this rewrite adds to
the brief. A brief item the operator changes for this rewrite is amended in
the brief before the run, and the commission says which item.

Code checks that `note` is the note being rewritten, that each source is a
repository file other than the note, its write brief and run state, and that
every required section is present. Every invocation is a new run and needs
the commission. The run captures the commission in
`rewrite-inputs.json`, with the note's [write brief](../types/write-brief.md)
when the note declares one, the sources and the note's type spec and
collection contract. Every worker receives the brief as binding retained
intent; the commission must not contradict it, and a worker that finds a
conflict reports a problem, which stops the run.

**Sources.** A source that git does not ignore and that is UTF-8 text is
captured: its text is an input of the writer and reviewer. A source that git
ignores, such as a snapshot under `kb/sources/.snapshots/`, or any file under
a `.snapshots/` directory, or a file that is not text, is referenced: the
source list gives its path and SHA-256 and the worker reads the file there.
A referenced source is never copied into the run, so full external sources
stay out of run state. The report's `sources` says which mode each source
has. A referenced source whose bytes changed since capture stops the run
before a candidate is held; a new run rewrites from the current text. Grounding comes before the run: the session agent grounds
claims with `cp-skill-ground` and lists the ingests and snapshots as sources.

**Calls.** Each call is a fresh worker on the profile file's `judgment`
profile, or the one `--profile` names, with only its listed inputs. The
[writer](../instructions/rewrite-a-note/write-a-rewrite-candidate.md) and
[independent reviewer](../instructions/rewrite-a-note/review-a-rewrite-candidate.md)
work directly with the commission, sources and existing note.

| Job | Inputs | Output and the check code applies |
|---|---|---|
| `candidate` | instruction, commission, optional brief, sources, contracts, old note, incoming citation passages and earlier decisions | candidate within the note's bounds; report with `## Affected citations` |
| `review` | candidate as target; the same evidence and the writer's report | typed review with outcome `pass`, `warn` or `fail` |
| `candidate-repair` | the candidate inputs, plus the failed typed `review` and the `blocked-candidate` | as `candidate`, and different from the blocked candidate |
| `review-repair` | as `review`, for the repaired candidate; no earlier review | as `review` |

A rejected output goes back to its worker with the problems, up to three
attempts. A worker problem stops the run; a new run asks again. The
candidate checks are those of `--revised`: the frontmatter parses and keeps
`title`, `type` and `brief`, the H1 is kept, `user-verified` is gone when
the body changed, and validation finds no new failure. The per-pass bounds
of edit operations do not apply.

**The review operation.** The review is a review operation like a gate, run
alone. Its criterion is the review instruction; its target is the candidate
text, judged in place of the note's file. The rewrite's other inputs are its
operational inputs. It runs through the sweep in its own run under
`reviews/<12 hex>/` in the rewrite run, named by the hash of the candidate and
those inputs, and publishes nothing while it runs. Like any review, it also
receives the operator's rejected findings of this note against this criterion
as `finding-decisions`. Its output is a [review result](../types/review-result.md)
with a verdict: `fail` blocks the candidate, `warn` accepts it with findings,
and `pass` accepts it with none. Each finding quotes the passage it anchors
to in `quotes`, or has `scope: document` for an absence. Its `reason` states
`Basis:` and then `Required change:`. A blocking finding has level `fail`, a
non-blocking one `warn`, and a remark that asks for no change `info`. Code
refuses an outcome that does not match the levels and a `warn` or `fail`
reason without its basis and required change; the worker is asked again.
The result's target hash binds it to the candidate, and a result of another
text is refused. The run keeps a copy as `artifact/review-<n>.md`, and the
report's `reviews` lists each review with its outcome.

**Citation consequences.** Both workers see the bounded passages that cite the note, collected without a model call. These can suggest angles, not claims the writer must retain. Report affected passages; default to removing an unsupported reference and fixing the dependent separately. Both workers receive earlier operator decisions when present. The old note is not independent evidence.

**Repair and end.** On `fail`, one repair runs: `candidate-repair`, then
`review-repair`, a fresh reviewer. A second `fail` ends the run with
`blocked` in the report, every output kept and nothing published. When a
finding asks for evidence the sources lack, the session agent grounds or
adds a source and starts again with a changed commission. A candidate the
reviewer accepts that equals the start text ends with `unchanged` and no
publication. Otherwise the run holds the candidate and ends, as `run revise`
holds a candidate with a new warning ([publication](#publication)):
`artifact/final.md`, `artifact/final.diff`, `held.json` with the hash of
the accepted review, and `new-warnings`. The note is not written. The
report's `held` names the candidate, its diff, the warnings and the commands
that publish it. The report's `accepted` names the accepted review, its
outcome and its `warn` findings; when there are any, `held.what` says how
many and where the review is, and the session agent tells the operator
before the decision ([approve a text](../instructions/approve-a-text.md)).
`publish RUN` publishes the exact candidate on the operator's word, or
`publish RUN --revised FILE` the operator's revision of it, only over the
start text and under the captured brief; it is also refused when the
accepted review changed after the run. To change the candidate otherwise,
start a new run with a changed commission.

**After publication.** When the published text is exactly the candidate the
accepted review judged, the review result becomes the note's current result
for its criterion, at `kb/reports/state/review/results/<note>/<criterion
id>.md`. The report's `current-result` names it and its freshness. It is
fresh while the note, the review instruction, the operator's rejected
findings of that pair and the output contract are unchanged, so `run revise
NOTE --triage` presents its `warn` findings like any other result. A
rejection at that triage stales it, as for a gate. When the operator
published a revised candidate (`--revised`), the published text is not the
judged text: the result is not stored, and the report's `not-current` says
so. The other inputs of the review, such as the commission, are outside the
freshness hashes. `status NOTE` never lists this criterion as missing, since
no criterion request selects it; `status` without NOTES lists a stored one.
No sweep reruns a stale one: a new rewrite reviews again.

**Run directory.** Every invocation opens a new run in
`kb/reports/state/review/runs/v2/rewrite/<note path without .md>/<UTC
stamp>/`, named as a revise run is. It holds `start.json`, `sweep.json` (the worker profile), `rewrite-inputs.json`,
`earlier-decisions.json`, the review runs under `reviews/`, the Workjig records under
`calls/`, `held.json` and, after publication, `published.json`, and under
`artifact/`: `commission.md`, `brief.md` when there is a brief, `sources.md`
(the source list), `start.md`,
`candidate-1.md`, `candidate-1-report.md`, `review-1.md`, after a repair
`candidate-2.md`, `candidate-2-report.md` and `review-2.md`, `final.md`,
`final.diff` and the publication files. No run is repeated or resumed.

### The operator-decision record

`commonplace-review decisions` is the one path to the
operator-decision record ([ADR 130](./adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md)).
It reads, without writing, the revise and rewrite run directories, and lists
each decision with who proposed it, who decided it and whether it covered
one item or a bundle. An answers file becomes a decision when a command
keeps it in a run's `answers/`: the run that `--answers` names it to, or
`answers record FILE`. Each kept file gives one entry per item, with its
state, decider and reason; a file kept by two runs is listed once. A
decision on a finding has class `finding`, and its item names the
criterion, the level and the reviewer's reason. Each publication from a
run's `published.json` is one bundle entry with class `publication` and
decision `published`, decided by `automatic` or, through `publish RUN`, by
the operator. An answers file a continuation record waits for that no run
kept, and a held candidate not yet published, are listed as `pending`. A
pending entry is listed as `overtaken` instead when the note no longer holds
the text the run left it: its last publication, or its start text. So that
decisions recorded before the cutover stay visible, it also reads the
records of the two retired procedures
([ADR 135](./adr/135-improvement-procedures-are-three-plans-on-one-runner.md)):
operator records in full-pass run directories, full-pass packets under
`kb/reports/state/review/packets/` and fix reports under
`kb/reports/state/fixes/`. Operator records of revise and rewrite runs are
not read; the answered ones were converted to kept answers once
([ADR 138](./adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)).
This is computed when listing; nothing is written and no item changes state.
It computes no statistics; `--note`, `--class` and `--json` narrow and
format the listing.

## Interpreting results

A `pass` records that one gate found nothing to flag; it is not
certification. A fresh critique matches the current inputs; it does not mean
its findings were handled. When a fix produces a diff, review the diff rather
than the fixing agent's report of success. Open-ended methods stay
report-shaped instead of being forced into verdicts.

## Authoring a gate

Gates are typed `review-gate`; [that type spec](../types/review-gate.md) owns
their frontmatter and body. Keep the judgment in the gate text: the prompt
around the inputs is outside the freshness hashes, so only an edit to a
criterion file stales its results. Declare `watches:` with the note parts the
gate actually inspects, because it decides which edits stale its pairs.
`staleness: changed` is the only accepted value.
