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
catalog gate, the note's type spec, its collection's `COLLECTION.md` or the
critique instruction. A criterion is named by its artifact identity: a
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

**Critique.** The `critique` lens applies the critique instruction as a
report criterion: the worker writes an open-ended report, and the outcome is
`report`. Critique is opt-in; `--all-gates` and the default status set leave
it out.

**Outcome.** A verdict review ends with exactly one `## Result: PASS`,
`## Result: WARN` or `## Result: FAIL` line as its last non-empty line; a
report ends with `## Result: REPORT`. An alias, a second result line or any
other result-like line rejects the review, and the worker is asked again
with the problem.

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

## Result files and freshness

Each accepted review writes
`kb/reports/state/review/results/<note-path>/<criterion-id>.md`. The
criterion id is the gate id for a catalog gate, the repository path without
`.md` for another repository criterion (`kb/types/note`), and `commonplace/`
plus the library path for another library criterion. The frontmatter holds
`note`, `note-sha256`, `criterion`, `criterion-sha256`, `outcome`, `profile`
(harness, launch model, effort), `model` (what the harness recorded), `run`,
`launch` and `completed-at`. The body is the worker's review, unchanged.

A pair is in one of three states:

- `fresh`: both hashes match the current files;
- `missing`: no result exists;
- `stale`: the note, the criterion, or both changed; status names which.

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
Without notes, it covers every stored result whose note and criterion still
exist. Each row shows the note, criterion id, state, outcome and model;
orphaned results are listed apart. A directory means its direct
frontmatter-bearing notes, not nested ones, and leaves out indexes, collection
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

`--criteria` takes gate ids, bundle names and the lenses; `--all-gates` means
every bundle plus `type` and `collection`. The sweep skips pairs with a fresh
result unless `--force` is given, and asks a worker for each other pair:

- `--grouping pair` (the default) makes one call per pair;
- `--grouping bundle` makes one call per note and bundle for that bundle's
  stale gates. Each gate is judged on its own and gets its own result. A
  bundle with one stale gate, and every type, collection and critique pair,
  is still one call per pair.

A call has three attempts; a rejected review and a launch that returned no
answer each spend one. A worker that cannot judge writes a problem instead
of guessing, and no result is written for its pairs. `--max-workers`
(default 4) bounds the launches running at once.

Each sweep opens a run directory under `kb/reports/state/review/runs/<UTC
stamp>/` and prints a JSON report: per pair its state (`fresh`, `reviewed`,
`problem`, `out-of-attempts` or `not-run`), the counts, what stopped the
sweep and the guard's finding. It exits 0 only when every pair has a current
result and the guard saw no change, 1 otherwise, and 2 when the command
failed.

### Stops, retry and resume

- **Launch failure or usage limit.** The sweep stops asking new calls; results
  already written stay. Repair the environment or wait for the reset, then
  rerun with `--resume RUN_DIR` and the same notes and criteria. Answered
  calls replay without a launch.
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

- `sonnet` (the default) and `opus` run Claude Code with read tools, edit
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

## Workflows beyond the sweep

**Full improvement pass.** `commonplace-review run full-pass NOTE` runs the
method reports, a packet, and for an accepted `keep` an edit, a copyedit and
a closing cycle with at most one repair. Workers write outputs only. Each
edited text stays in the run directory, and later steps work on that text.
The note is written once, only when closing is `ready` and the exact final
publication manifest has been approved. Until then, the candidate packet,
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

**Revision.** `commonplace-review run revise` applies the
[simplification passes](../instructions/simplification-passes/README.md) to
one artifact. Assessment, planning and settled intermediate passes are
preauthorized. The assessment report and generated plan stay in the run for
inspection; the validated plan runs without routine approval. `--plan FILE`
supplies a validated explicit input or override, including a stopped plan,
without approval. Editing the retained plan alone is not an override.
Each listed pass runs in order on the preceding text; its `effort` selects
the profile. Every pass must end `applied`, `no-change` or `skipped` before
changed final text is offered for publication approval. No revision has been
measured yet.

Plain-wording and abstractions still stop for explicit approval of each
selection proposal. These are temporary procedure-development points:
retain proposed, accepted and rejected choices with reasons, evolve the
selection rules and checks, and evaluate retained and fresh examples before
separately authorizing removal. This is not new automatic learning
infrastructure, and fewer proposals do not establish reliability.

**Runs of the two workflows.** Their run directory is derived from the
inputs: `kb/reports/state/review/runs/<workflow>/<note path without
.md>/<first 12 hex of the note's SHA-256>/`. Repeating the same command on
the same note text continues that run, and answered calls replay. An edited
note, including one the workflow itself wrote, has another hash, so the same
command opens a new run. A repeat reuses the options the run recorded,
including the full pass's `--direction`; an option given on the repeat
replaces the recorded value. A stop for the operator proposes a file in the
run directory, and the report's `waiting-for` gives what to do, the file,
the approval command and the command to repeat. Approval captures the file's
current text; repeating alone never approves it. Selection-list edits after
approval require another approval and appear under `unapproved-edits`.
Changed proposal inputs require fresh approval. A plan with `stop` set ends
the run; replace it explicitly with `--plan`, not an approval command. An
agent may approve only on the operator's stated word for that proposal.

For changed final text in either workflow, inspect `artifact/final.md` and
`artifact/final.diff`, then approve the exact generated
`artifact/publication.json` with `commonplace-review approve RUN FILE --key KEY`
and repeat. The manifest is not editable approval input: publication requires
an exact match. To revise, use `--plan` for revision, change workflow inputs,
or start a new run; do not edit the manifest or candidate. Publication also
requires the original artifact and captured brief to remain unchanged.
A conflict leaves the original untouched and names the proposed text.
Instructions remain the judgment authority; prompts name inputs only.

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
