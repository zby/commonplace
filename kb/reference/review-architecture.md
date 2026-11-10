---
description: "How Commonplace review is built: workflows over the headless runtime, result files as the only durable review state, the two-input freshness hash with watched parts, the single write and the checkout guard"
type: types/note.md
tags: []
---

# Review architecture

Review is a set of Python workflows over the headless runtime, behind one
command, `commonplace-review`. Code owns the control flow, every check that
can be checked and every write to the checkout. Workers only judge and write
their output files. The only durable review state is files: one result per
(note, criterion) pair and one current packet per note that had a full pass.

For operation, see [the review-system guide](./README-REVIEW-SYSTEM.md).
[ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md) records
the decision. Exact behavior belongs to `commonplace.lib.review_workflows`,
`commonplace.headless` and `commonplace.cli.review_workflows`.

## Components

| Part | Role |
|---|---|
| `headless.jobs` | `ask()`, one agent call with named inputs and outputs; `checked()`, retry with a deterministic check; `gather()`, parallel calls; `Run`, a run directory with a lock, durable launch records and replay; `dismiss()` and `acknowledge_stopped()` |
| `headless.decisions` | `decide()`, an ask whose markdown frontmatter or YAML output is checked against a closed schema before code branches on it |
| `headless.harness` | worker profiles as Workjig command workers for Claude Code, codex and pi, and the model each harness recorded |
| `review_workflows.criteria` | criterion requests (gate ids, bundles, `type`, `collection`, `critique`) resolved into applicable pairs; reads only |
| `review_workflows.outcomes` | the strict result-line parser |
| `review_workflows.results` | result files, criterion ids, the watched-parts note hash, and freshness, status, summary and orphans as pure functions over the files |
| `review_workflows.gates` | the gate sweep, call grouping, the worker prompt and the checkout guard |
| `review_workflows.edits` | the bounds an edited text must keep, the single write of the final text, the run directory derived from the inputs and the guard minus a workflow's own write |
| `review_workflows.full_pass` | the full improvement pass and its packet |
| `review_workflows.revise` | the revision workflow over the simplification passes |

Workjig launches each worker in the checkout through the harness's headless
mode ([ADR 119](./adr/119-analysis-workers-launch-through-workjig.md)). The
worker loads the project's normal configuration and the profile's flags.

## Ownership

A workflow is ordinary Python that branches only on what code parsed: a
verdict line, a decision schema, an edit's bounds. A worker receives its
inputs as files Workjig writes for each launch, so it judges captured text,
not the live file, and the result hashes exactly that text. A worker writes
only its declared outputs, or a problem file when it cannot do the job. Code
turns an accepted output into a result file, a packet or a write to the
checkout.

An edit reaches the checkout only through code. Each edited text is checked
first; for the full pass, frontmatter `title` and `type` and the H1 must be
kept, `user-verified` removed after a body change, and no validation failure
added. An accepted text stays in memory and in the run's `artifact/`
directory, and the next step works on it. The workflow's last step writes the
final text once, atomically, and only over the start text. Any other text
is a change made outside the run: the run writes nothing and reports a
conflict that names the file holding the proposed text.

A full pass or revision is a function of its inputs. Its run directory is
derived from the workflow, the note's path and the hash of the note's start
text, so repeating the command continues the run by replay, and an edited
note opens a new run.

## Durable state and run state

| State | Location | Lifetime |
|---|---|---|
| result files | `kb/reports/state/review/results/<note-path>/<criterion-id>.md` | until replaced by a later review of the pair or deleted as orphaned |
| current full-pass packet | `kb/reports/state/review/packets/<note-path>` | until a later pass replaces it; holds the resolution of a pending hand-back |
| run directory | `kb/reports/state/review/runs/<stamp>/` for a sweep; `runs/<workflow>/<note path without .md>/<start-hash prefix>/` for a full pass or revision | a sweep and its resumes; every repeat of a workflow command on the same note text |

A run directory holds Workjig's records under `calls/`, the profile and
options it opened with in `sweep.json`, and accepted per-run artifacts under `artifact/`
(the start text, method reports, each accepted edited text and the packet copy). Its
records exist for replay inside the run and promise no format stability
across versions. Freshness across runs never reads them.

Result files are written atomically. One run holds a lock on its directory;
two runs over the same pair both write, and the later write stands.

## Freshness hash boundary

A result pins exactly two inputs: the note and the criterion. The criterion
hash covers the criterion file's whole text. The note hash covers the parts
the criterion declares in `watches:` (title, description, body) under the
criterion's current text, or the whole note without a valid declaration.
Parts are normalized: the title is the first `# ` heading, and the body drops
blank lines and trailing spaces, so a whitespace-only edit changes nothing.
A criterion edit that changes `watches:` may therefore report both inputs
changed.

Everything else is outside the hashes: the prompt around the inputs, the
type and collection wrappers, the output contract and the reading scope.
Judgment-bearing text therefore belongs in criterion files, where the hash
sees it ([ADRs 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)
and [041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)
apply this to their wrappers). A prompt change is part of each call's
identity, so a resumed run asks those calls again, but it stales no result. A
prompt change that shifts judgments needs a deliberate `--force` sweep.

Linked files a worker reads, including the one path a criterion may derive
from a link ([ADR 073](./adr/073-untracked-source-snapshots-require-ingest-grounding.md)),
are reading context, not freshness inputs.

## Criterion identity

A criterion is named by its artifact identity, and its text is read through
the library resolution. In this checkout the library is `kb/`, so every
criterion is a repository path. In an installed project, the gate catalog,
global types and the critique instruction are `commonplace:<path>`
identities, while project type specs and `COLLECTION.md` contracts are
repository paths ([ADR 086](./adr/086-projects-read-the-library-from-the-installed-package.md)).
The criterion id that keys a result file follows from the identity, so both
layouts store results the same way.

## Checkout guard

`gates.checkout_state()` records `HEAD` and, for each path `git status` lists
(including untracked files) outside `kb/reports/state/review/`, its status
code and content digest. A run compares the record before and after; a
workflow that writes the checkout drops its note when the note holds exactly
the final text the run applied. The guard can say that a path changed while the run was
open. It cannot attribute the change, and it misses ignored files and changes
undone before the run ended. It reverts nothing.

## Maintenance scope

Review this page when the ownership split between code and workers, the
durable state, the freshness inputs or the guard's claim changes. New
workflows, prompt wording, profile flags and command arguments do not by
themselves require an edit; source and `--help` own them.

## See also

- [ADR 118](./adr/118-analyses-run-as-a-workflow-over-headless-harnesses.md) — decided-by: the headless workflow runtime review shares with the analysis workflow
- [Storage architecture](./storage-architecture.md) — part-of: where review state sits among Commonplace's storage roles
- [Full improvement pass closure](./full-improvement-pass-closure.md) — see-also: why the full pass reviews its final text once more
