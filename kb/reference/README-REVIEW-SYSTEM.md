---
description: How to operate commonplace-review — criteria and pairs, result files and freshness, gate sweeps, status, retry and resume, the checkout guard, worker profiles, cost, and the full-pass and revision workflows
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
`COLLECTION.md`, or a report instruction: critique, friction, premises or
compression synthesis. A criterion is named by its artifact identity: a
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
[compression bundle](../instructions/run-compression-bundle-on-note.md) and
the full pass still run all four in one report of their own; that report is
not a result file.

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
| 1 | whether the note's claim and scope should stand | critique, composition friction, premise decomposition | split out a treatment |
| 2 | what the note asserts and on what grounds | the semantic bundle, `frontmatter/claim-strength`, `prose/source-residue` | narrow overclaims |
| 3 | terms and what a reader needs to know | the accessibility bundle, `prose/unbridged-cross-domain` | abstractions |
| 4 | structure and proportion | the complexity bundle, the compression checks and their synthesis, three prose gates, `structural/general-before-specific` | readability and flow |
| 5 | wording | the sentence bundle, two prose gates, two structural gates | plain wording |
| 6 | title, description and opening | the other frontmatter gates | opening and title |

The values are best-effort declarations. Each file holds its own value;
the table summarizes them and the file governs. No code orders review
operations by depth yet: the revise workflow checks the depth order of
its passes, places a plan entry that fixes a finding at the depth of the
finding's criterion, and shows the assessor each finding's depth. Nothing
else reads the field. The type and collection
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
file `--json` names, and fix under the [fix procedure](../instructions/FIX-SYSTEM.md).
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
result and the guard saw no change, 1 otherwise, and 2 when the command
failed.

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
`kb/reports/state/review/`. The report lists every path that differs. A full
pass or revision leaves out its note only when the note holds the final text
the run applied.

What it can claim: these paths changed while the run was open. What it
cannot claim: that a worker changed them. Other sessions editing or
committing in the same checkout show up as well, so a failed guard means
"inspect these paths". Nothing is reverted. The guard also misses a change to
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
| one full pass on one short note | 27 launches, $4.47, ended in a hand-back |

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
choosing work, not merely using a model. Assessment-led revision and full-pass
composition need separate evaluation; reliable replay does not establish
reliable selection or editing judgment.

## Workflows beyond the sweep

**Full improvement pass.** `commonplace-review run full-pass NOTE` runs the
method reports, a packet, and for an accepted `keep` an edit, a copyedit and
a closing cycle with at most one repair. Workers write outputs only. Each
edited text stays in the run directory, and later steps work on that text.
The note is written once, only when closing is `ready` and the operator's
publication answers approve the exact candidate. Until then, the candidate packet,
results and note remain unpublished. A hand-back leaves the note untouched;
no-edit dispositions may publish their report, packet and results automatically.
Gates and critique are asked over each text even
when a fresh result exists. The pass writes their result files once, at its
end, for the text the note then holds. The note's
current packet lives at `kb/reports/state/review/packets/<note-path>`;
`commonplace-review packet` checks its recorded hashes against the files.
Operate it with [run a full improvement pass](../instructions/run-full-improvement-pass-on-note.md)
and [resolve a full-pass disposition](../instructions/resolve-full-pass-disposition.md);
[full improvement pass closure](./full-improvement-pass-closure.md) explains
the closing cycle.

**One edit operation.** `commonplace-review run edit OPERATION NOTE` runs one
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

**Revision.** `commonplace-review run revise` applies the
[simplification passes](../instructions/simplification-passes/README.md) to
one artifact. It runs a plan, and the procedures differ in how the plan is
made ([three ways](../instructions/simplification-passes/README.md#three-ways-to-make-a-plan)).
A new run requires one choice. The focused procedure is fixed work:
`--pass NAME` writes a one-entry plan for one pass, `--finding RESULT` writes
a one-entry plan that runs
[fix a finding by a named strategy](../instructions/fix-warnings/fix-strategy-taxonomy.md)
with that review result of the artifact as its `finding` input, and
`--plan FILE` supplies any other plan. The quick procedure is `--assess`:
one assessor chooses the passes from the artifact and its fresh stored
`warn` and `fail` review results, and no review is launched. A plan entry
for a pass that declares `responds-to` names its `finding` and takes the
depth of that finding's criterion. Within the chosen mode, ordinary
intermediate work is preauthorized. The assessment report and generated plan
stay in the run for inspection; the validated plan runs without routine
approval. `--plan FILE` also supplies a validated override of a stopped plan.
Editing the retained plan alone is not an override.
Each listed pass runs in order on the preceding text, through the same route
as `run edit`; its `effort` selects the profile. Every pass must end `applied`, `no-change` or `skipped` before
changed final text is offered for publication approval. Control-flow checks
do not establish the quality of the selected edits.

Plain-wording and abstractions, the `per-item` passes, still stop for the
operator's answers on each proposal, in `artifact/<pass>-answers-<key>.md`.
These are temporary procedure-development points:
retain proposed, accepted and rejected choices with reasons, evolve the
selection rules and checks, and evaluate retained and fresh examples before
separately authorizing removal. This is not new automatic learning
infrastructure, and fewer proposals do not establish reliability.

**Runs of the two workflows.** Their run directory is derived from the
inputs: `kb/reports/state/review/runs/v2/<workflow>/<note path without
.md>/<first 12 hex of the note's SHA-256>/`. Repeating the same command on
the same note text continues that run, and answered calls replay. An edited
note, including one the workflow itself wrote, has another hash, so the same
command opens a new run. Revision then requires a new `--plan` or `--assess`
choice rather than silently assessing again. Older revision runs without a
recorded mode require an explicit choice too. A repeat reuses the options the run recorded,
including the full pass's `--direction`; an option given on the repeat
replaces the recorded value. A stop for the operator proposes a file in the
run directory, and the report's `waiting-for` gives what to do, the file,
the approval command and the command to repeat. Approval captures the file's
current text; repeating alone never approves it. Answers edited after
approval require another approval and appear under `unapproved-edits`.
Changed proposal inputs require fresh approval. A plan with `stop` set ends
the run; replace it explicitly with `--plan`, not an approval command. An
agent may approve only on the operator's stated word for that proposal.

For changed final text in either workflow, inspect `artifact/final.md` and
`artifact/final.diff`, record the operator's decision on the one item of
`artifact/publication-answers.md`, which names the candidate's hash, approve
that file with `commonplace-review approve RUN FILE --key KEY` and repeat
([approve a text](../instructions/approve-a-text.md)). Publication requires
answers that pass the validator and approve that exact candidate. The
proposal key binds the original, the candidate and the decision context, so
a change in any of them withdraws the approval. To revise, use `--plan` for
revision, change workflow inputs, or start a new run; do not edit the
candidate. Publication also requires the original artifact and captured
brief to remain unchanged.
A conflict leaves the original untouched and names the proposed text.
Instructions remain the judgment authority; prompts name inputs only.

**Decisions.** `commonplace-review decisions` is the one path to the
operator-decision record ([ADR 130](./adr/130-the-operator-decision-record-is-a-query-over-the-state-tree.md)).
It reads, without writing, the operator records in both workflows' run
directories, the packets and the fix reports, and lists each decision with
who proposed it, who decided it and whether it covered one item or a bundle.
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
