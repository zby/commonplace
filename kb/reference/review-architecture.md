---
description: "How review separates Workjig execution, retained observations, replaceable current results, captured validation contracts, freshness and isolated single-assessment fixtures"
type: types/note.md
tags: []
---

# Review architecture

Review is a set of Python workflows over the headless runtime, behind one
command, `commonplace-review`. Code owns the control flow, every check that
can be checked and every write to the checkout. Workers only judge and write
their output files. Durable state consists of run-owned observations and
captured evidence and replaceable current results per (note, criterion)
pair.

For operation, see [the review-system guide](./README-REVIEW-SYSTEM.md).
[ADR 127](./adr/127-review-runs-as-workflows-over-result-files.md) records
the workflow decision; [ADR 132](./adr/132-review-atoms-retain-observations-behind-current-results.md)
records the typed review, retained-observation and fixture boundary;
[ADR 133](./adr/133-edit-operations-run-alone-through-one-typed-route.md)
extends that boundary to edit operations;
[ADR 135](./adr/135-improvement-procedures-are-three-plans-on-one-runner.md)
makes the revise workflow the one runner of the improvement procedures. Exact behavior belongs to `commonplace.lib.review_workflows`,
`commonplace.headless` and `commonplace.cli.review_workflows`.

## Components

| Part | Role |
|---|---|
| `headless.jobs` | `ask()`, one agent call with named inputs and outputs; `checked()`, retry with a deterministic check; `gather()`, parallel calls; `Run`, a run directory with a lock, durable launch records and replay; `dismiss()` and `acknowledge_stopped()` |
| `headless.decisions` | `decide()`, an ask whose markdown frontmatter or YAML output is checked against a closed schema before code branches on it |
| `headless.operator` | `answer()`, a proposal that waits for an explicitly captured answer; `approve()`, capture under the run lock bound to the proposal and its inputs; `waiting()`, the file, proposal key, approval command and repeat command |
| `headless.harness` | worker profiles as Workjig command workers for Claude Code, codex and pi, and the model each harness recorded |
| `review_workflows.criteria` | criterion requests (gate ids, bundles, `type`, `collection`, compression check ids, and the report instructions `critique`, `friction`, `premises`, `compression-synthesis`, `role`) resolved into applicable pairs; reads only |
| `review_workflows.inbound` | the role report's inbound contexts: the passages under `kb/` that link to one note, with each linking file's path, title and description, capped; reads only |
| `review_workflows.result_contract` | captured library type/schema and project collection contract, worker/controller field ownership and typed acceptance; it captures the edit-result contract the same way |
| `review_workflows.observations` | exact input captures, execution provenance, launch diagnostics and retained result hashes |
| `review_workflows.fixtures` | retained single-execution baselines and isolated trials through the same gate or edit implementation |
| `review_workflows.results` | result files, criterion ids, the watched-parts note hash, and freshness, status, summary and orphans as pure functions over the files |
| `review_workflows.gates` | `ask()`, which retains individual typed assessments; the sweep, which skips fresh pairs and publishes current views; call grouping, the worker prompt and the checkout guard |
| `review_workflows.edit_operations` | one edit operation on one input text: the worker prompt, the typed edit result, its acceptance including the check of an `answers` input, its observation under `artifact/edits/`, and the `run edit` command's run |
| `review_workflows.edits` | the bounds an edited text must keep, including link targets and quoted spans, reading an answers file through the validator, the publication stop over the candidate, the single write of the final text, the run directory derived from the inputs and the guard minus a workflow's own write |
| `answers` | the [answers](../types/answers.md) type's question items, its pending file and its comparison with the question, which the validator runs for every answers file |
| `review_workflows.revise` | the one runner of the improvement procedures: the plan (fixed, one-entry, or written by the assessor after an optional review step), its order, per-item answers stops and publication; each operation runs through `edit_operations.ask()` |
| `review_workflows.decisions` | the read-only operator-decision record over run operator records, and over the packets and fix reports of the retired procedures |

Workjig launches each worker in the checkout through the harness's headless
mode ([ADR 119](./adr/119-analysis-workers-launch-through-workjig.md)). The
worker loads the project's normal configuration and the profile's flags.

## Ownership

A workflow is ordinary Python that branches only on what code parsed: a
typed outcome, a decision schema, an edit's bounds. A worker receives its
inputs as files Workjig writes for each launch, so it judges captured text,
not the live file, and the result hashes exactly that text. A worker writes
only its declared outputs, or a problem file when it cannot do the job. Code
turns an accepted output into a result file or a write to the checkout. Asking and publishing are separate: `gates.ask()` returns each
accepted review without publishing a current view; its captured inputs and
completed typed artifact remain in the run. The sweep publishes each result
as its answer arrives; so does the review step of the full procedure, which
runs through the sweep.

An edit reaches the checkout only through code. Each edited text is checked
first; frontmatter `title`, `type` and `brief` and the H1 must be
kept, `user-verified` removed after a body change, and no validation failure
added. A text from an edit operation also keeps every link target the result
does not name as removed and every quoted span. Every revision pass candidate
comes from `edit_operations.ask()`, which also serves `run edit`. An accepted text stays in memory and in the run's `artifact/`
directory, and the next step works on it. The workflow's last step writes the
final text once, atomically, only over the start text and after approved
answers that approve the exact candidate. Any other text
is a change made outside the run: the run writes nothing and reports a
conflict that names the file holding the proposed text.

A revise run reuses answers by each call's inputs. Its run directory is
derived from the workflow, the note's path and the hash of the note's start
text, so repeating the command continues the run by replay, and an edited
note opens a new run. The directory is not a complete input identity: changed
instructions, profiles, write briefs or approved answers can produce new calls inside it.
A new revision run explicitly chooses a fixed plan (`--plan`, `--pass` or
`--finding`), `--assess` or `--full`. Repeats retain that mode; changed artifact text requires a new
choice. Within the selected mode, ordinary intermediate work is preauthorized.
Revision retains its generated plan for inspection and runs it after
validation; `--plan` also supplies a validated override of a stopped plan,
without approval. Editing the retained plan alone is not an override.

Fixed-plan execution constructs no assessment request. Editors in both modes
receive the execution instruction and the assigned pass, not the planning
procedure. Fixed-plan publication binds those inputs, the supplied plan and
the profiles used by its passes; assessment-only instructions, unselected
passes and unused effort profiles do not invalidate it. Assessment-led runs
also bind the assessment request, answer and the catalog of edit operations. A single
criterion through `run gates` is report-only and never selects subsequent work.

Unsettled plain-wording and abstraction selections require the operator's
answer per proposal, in an [answers](../types/answers.md) file whose
question is the proposing run's edit result. These temporary
procedure-development points retain each answer with the operator's reason
for a rejection or deferral, in the run's operator record and the selection
context that binds publication. Removal needs separate authorization
after selection rules and checks have been revised and evaluated on retained
and fresh examples. This is not automatic learning infrastructure; a lower
proposal count does not establish reliability.

Changed final text requires an answers file,
`artifact/publication-answers.md`, whose question is the candidate
`artifact/final.md` and whose one item, naming the candidate's hash, the
operator approved; `commonplace-review approve RUN FILE --key KEY` records
it. `artifact/final.diff` is the inspection view. Repeating never approves.
The proposal key binds the start text, the candidate and the decision
context; a change in any of them withdraws the approval. The candidate is a
generated output, not a revision input: use `--plan` for revision, change
workflow inputs or start a new run. Judgment stays in instructions; prompts name inputs only.

A declared [write brief](../types/write-brief.md) is captured for revision
assessment and every pass. Its bytes
participate in those calls' identities and in final publication approval. A
worker reports a brief conflict as a problem, stopping the run. Code prevents
changing the declaration and checks that the captured brief is still current
before publication; it cannot verify semantic obedience. An amendment to the
commission must happen outside the run. Review workers do not receive this
input, and brief changes do not stale gate results.

## Durable state and run state

| State | Location | Lifetime |
|---|---|---|
| result files | `kb/reports/state/review/results/<note-path>/<criterion-id>.md` | until replaced by a later review of the pair or deleted as orphaned |
| full-pass packet (retired) | `kb/reports/state/review/packets/<note-path>` | written by the retired full-pass workflow; nothing writes it now, and `commonplace-review decisions` still reads it |
| run directory | `kb/reports/state/review/runs/v2/<stamp>/` for a sweep; `runs/v2/<workflow>/<note path without .md>/<start-hash prefix>/` for a revise run | a sweep and its resumes; every repeat of a workflow command on the same note text |
| observation | a run's `artifact/reviews/<id>/`, or `artifact/edits/<id>/` for an edit operation | one assessment or edit execution, including retries and replay; exact inputs, completed results, candidate texts and their hashes remain citable |
| fixture | `kb/reports/state/review/fixtures/<id>/` | one retained content baseline; each new trial owns independent mutable files and Git state |

A run directory holds Workjig's records under `calls/`, the profile and
options it opened with in `sweep.json`, operator proposals and approved answers
under `operator/`, and accepted per-run artifacts under `artifact/`
(the start text, the assessment and plan, each accepted edited text and the
publication candidate). Its
records exist for replay inside the run and promise no format stability
across versions. The current result references its observation, exact target
capture and raw launch output. Historical run state is evidence, not an input
pool: workers receive only explicitly selected, self-contained operational
copies. Provenance links do not grant access to another run.

Result files are written atomically. One run holds a lock on its directory;
two runs over the same pair both write, and the later write stands.

## Freshness hash boundary

Freshness compares the note, criterion and captured output-contract fingerprint.
Apart from the operator's finding decisions, described below, a review with
supplied operational inputs, such as the compression synthesis
over its findings or the role report over the note's inbound contexts, has no freshness: those inputs are outside every hash, so
it publishes no current result and is always asked again.
The latter includes the library type/schema closure and the project collection
contract governing review results. Validation context is checked before workers
start; missing dependencies are controller failures, not requests for model correction.
Exact target byte hashes are separate from normalized freshness hashes. The criterion
hash covers the criterion file's whole text. When the operator rejected a
finding of the pair at a triage, it also covers those finding decisions:
the sweep captures them from the approved triage answers of the note's revise
runs (`decisions.review_inputs()`), asks the pair alone and supplies them as
the input `finding-decisions`, whose text states the reviewer's rule for
them. A pair without a rejection keeps the plain criterion hash, its call
and its inputs, so this input stales no other result. A new rejection, or a
changed one, stales only its pair, and status names the criterion as
changed. The note hash covers the parts
the criterion declares in `watches:` (title, description, body) under the
criterion's current text, or the whole note without a valid declaration.
Parts are normalized: the title is the first `# ` heading, and the body drops
blank lines and trailing spaces, so a whitespace-only edit changes nothing.
A criterion edit that changes `watches:` may therefore report both inputs
changed.

The prompt, type and collection wrappers and reading scope remain outside
freshness hashes; observation records identify the invocation and executable
separately.
Judgment-bearing text therefore belongs in criterion files, where the hash
sees it ([ADRs 038](./adr/038-type-conformance-reviews-use-the-type-spec-as-the-gate.md)
and [041](./adr/041-collection-conformance-reviews-use-collection-md-as-the-gate.md)
apply this to their wrappers). A prompt change is part of each call's
identity, so a resumed run asks those calls again, but it stales no result. A
prompt change that shifts judgments needs a deliberate `--force` sweep.

Linked files a worker reads, including the one path a criterion may derive
from a link ([ADR 073](./adr/073-untracked-source-snapshots-require-ingest-grounding.md)),
are reading context, not freshness inputs.

## Controlled trials and historical state

Fixtures reconstruct the committed tree, retained target and criterion,
available dirty content and library, with hash checks. Missing historical
dirty content requires exact repair; it is not silently replaced. Creation
explicitly selects the current executable as a substitute baseline. Dependency
artifacts, user-level configuration and effective tool availability remain
recorded gaps, not claims of environment equivalence. Every trial bypasses
freshness skips and never publishes into the live result store. Resume stays
within that trial; it is not an independent observation. An edit fixture
reruns one edit execution from its captured operation, input text, supplied
inputs and contract, through `run edit --fixture`; a review fixture runs
through `run gates --fixture`, and each command refuses the other's fixture.

The runtime accepts one result format and one active run namespace. Old
results and runs must be archived rather than migrated or replayed. Before
cutover, settle active launches and obtain disposition of unfinished workflows;
old approvals confer no authority on new runs. Cited launch bytes can remain
at their historical paths outside active discovery.

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
